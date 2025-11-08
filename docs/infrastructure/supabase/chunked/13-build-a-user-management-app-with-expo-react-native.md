**Navigation:** [← Previous](./12-advanced-pgtap-testing.md) | [Index](./index.md) | [Next →](./14-build-a-user-management-app-with-ionic-vue.md)

# Build a User Management App with Expo React Native



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/supabase-flutter-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/expo-user-management).
</Admonition>



## Project setup

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.


### Create a project

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.


### Set up the database schema

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
    3.  Click **Run**.

    <Admonition type="note">
      You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

      ```bash
      supabase link --project-ref <project-id>
      # You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>
      supabase db pull
      ```
    </Admonition>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    <Admonition type="note">
      When working locally you can run the following command to create a new migration file:
    </Admonition>

    ```bash
    supabase migration new user_management_starter
    ```

    ```sql
    -- Create a table for public profiles
    create table profiles (
      id uuid references auth.users not null primary key,
      updated_at timestamp with time zone,
      username text unique,
      full_name text,
      avatar_url text,
      website text,

      constraint username_length check (char_length(username) >= 3)
    );
    -- Set up Row Level Security (RLS)
    -- See https://supabase.com/docs/guides/database/postgres/row-level-security for more details.
    alter table profiles
      enable row level security;

    create policy "Public profiles are viewable by everyone." on profiles
      for select using (true);

    create policy "Users can insert their own profile." on profiles
      for insert with check ((select auth.uid()) = id);

    create policy "Users can update own profile." on profiles
      for update using ((select auth.uid()) = id);

    -- This trigger automatically creates a profile entry when a new user signs up via Supabase Auth.
    -- See https://supabase.com/docs/guides/auth/managing-user-data#using-triggers for more details.
    create function public.handle_new_user()
    returns trigger
    set search_path = ''
    as $$
    begin
      insert into public.profiles (id, full_name, avatar_url)
      values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
      return new;
    end;
    $$ language plpgsql security definer;
    create trigger on_auth_user_created
      after insert on auth.users
      for each row execute procedure public.handle_new_user();

    -- Set up Storage!
    insert into storage.buckets (id, name)
      values ('avatars', 'avatars');

    -- Set up access controls for storage.
    -- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
    create policy "Avatar images are publicly accessible." on storage.objects
      for select using (bucket_id = 'avatars');

    create policy "Anyone can upload an avatar." on storage.objects
      for insert with check (bucket_id = 'avatars');

    create policy "Anyone can update their own avatar." on storage.objects
      for update using ((select auth.uid()) = owner) with check (bucket_id = 'avatars');
    ```
  </TabPanel>
</Tabs>


### Get API details

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key. Get the URL from [the API settings section](/dashboard/project/_/settings/api) of a project and the key from the [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/).

<Admonition type="note" title="Changes to API keys">
  Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

  To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

  *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
  *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
</Admonition>



## Building the app

Let's start building the React Native app from scratch.


### Initialize a React Native app

We can use [`expo`](https://docs.expo.dev/get-started/create-a-new-app/) to initialize
an app called `expo-user-management`:

```bash
npx create-expo-app -t expo-template-blank-typescript expo-user-management

cd expo-user-management
```

Then let's install the additional dependencies: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npx expo install @supabase/supabase-js @react-native-async-storage/async-storage @rneui/themed
```

Now let's create a helper file to initialize the Supabase client.
We need the API URL and the key that you copied [earlier](#get-api-details).
These variables are safe to expose in your Expo app since Supabase has
[Row Level Security](/docs/guides/database/postgres/row-level-security) enabled on your Database.

<Tabs scrollable size="large" type="underlined" defaultActiveId="async-storage" queryGroup="auth-store">
  <TabPanel id="async-storage" label="AsyncStorage">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="lib/supabase.ts" label="lib/supabase.ts">
        ```ts name=lib/supabase.ts
        import AsyncStorage from '@react-native-async-storage/async-storage'
        import { createClient } from '@supabase/supabase-js'

        const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL
        const supabasePublishableKey = YOUR_REACT_NATIVE_SUPABASE_PUBLISHABLE_KEY

        export const supabase = createClient(supabaseUrl, supabasePublishableKey, {
          auth: {
            storage: AsyncStorage,
            autoRefreshToken: true,
            persistSession: true,
            detectSessionInUrl: false,
          },
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="secure-store" label="SecureStore">
    If you wish to encrypt the user's session information, you can use `aes-js` and store the encryption key in [Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore). The [`aes-js` library](https://github.com/ricmoo/aes-js) is a reputable JavaScript-only implementation of the AES encryption algorithm in CTR mode. A new 256-bit encryption key is generated using the `react-native-get-random-values` library. This key is stored inside Expo's SecureStore, while the value is encrypted and placed inside AsyncStorage.

    Make sure that:

    *   You keep the `expo-secure-storage`, `aes-js` and `react-native-get-random-values` libraries up-to-date.
    *   Choose the correct [`SecureStoreOptions`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestoreoptions) for your app's needs. E.g. [`SecureStore.WHEN_UNLOCKED`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestorewhen_unlocked) regulates when the data can be accessed.
    *   Carefully consider optimizations or other modifications to the above example, as those can lead to introducing subtle security vulnerabilities.

    Install the necessary dependencies in the root of your Expo project:

    ```bash
    npm install @supabase/supabase-js
    npm install @rneui/themed @react-native-async-storage/async-storage
    npm install aes-js react-native-get-random-values
    npm install --save-dev @types/aes-js
    npx expo install expo-secure-store
    ```

    Implement a `LargeSecureStore` class to pass in as Auth storage for the `supabase-js` client:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="lib/supabase.ts" label="lib/supabase.ts">
        ```ts name=lib/supabase.ts
        import { createClient } from "@supabase/supabase-js";
        import AsyncStorage from "@react-native-async-storage/async-storage";
        import * as SecureStore from 'expo-secure-store';
        import * as aesjs from 'aes-js';
        import 'react-native-get-random-values';

        // As Expo's SecureStore does not support values larger than 2048
        // bytes, an AES-256 key is generated and stored in SecureStore, while
        // it is used to encrypt/decrypt values stored in AsyncStorage.
        class LargeSecureStore {
          private async _encrypt(key: string, value: string) {
            const encryptionKey = crypto.getRandomValues(new Uint8Array(256 / 8));

            const cipher = new aesjs.ModeOfOperation.ctr(encryptionKey, new aesjs.Counter(1));
            const encryptedBytes = cipher.encrypt(aesjs.utils.utf8.toBytes(value));

            await SecureStore.setItemAsync(key, aesjs.utils.hex.fromBytes(encryptionKey));

            return aesjs.utils.hex.fromBytes(encryptedBytes);
          }

          private async _decrypt(key: string, value: string) {
            const encryptionKeyHex = await SecureStore.getItemAsync(key);
            if (!encryptionKeyHex) {
              return encryptionKeyHex;
            }

            const cipher = new aesjs.ModeOfOperation.ctr(aesjs.utils.hex.toBytes(encryptionKeyHex), new aesjs.Counter(1));
            const decryptedBytes = cipher.decrypt(aesjs.utils.hex.toBytes(value));

            return aesjs.utils.utf8.fromBytes(decryptedBytes);
          }

          async getItem(key: string) {
            const encrypted = await AsyncStorage.getItem(key);
            if (!encrypted) { return encrypted; }

            return await this._decrypt(key, encrypted);
          }

          async removeItem(key: string) {
            await AsyncStorage.removeItem(key);
            await SecureStore.deleteItemAsync(key);
          }

          async setItem(key: string, value: string) {
            const encrypted = await this._encrypt(key, value);

            await AsyncStorage.setItem(key, encrypted);
          }
        }

        const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL
        const supabasePublishableKey = YOUR_REACT_NATIVE_SUPABASE_PUBLISHABLE_KEY

        const supabase = createClient(supabaseUrl, supabasePublishableKey, {
          auth: {
            storage: new LargeSecureStore(),
            autoRefreshToken: true,
            persistSession: true,
            detectSessionInUrl: false,
          },
        });
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Set up a login component

Let's set up a React Native component to manage logins and sign ups.
Users would be able to sign in with their email and password.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Auth.tsx" label="components/Auth.tsx">
    ```tsx name=components/Auth.tsx
    import React, { useState } from 'react'
    import { Alert, StyleSheet, View, AppState } from 'react-native'
    import { supabase } from '../lib/supabase'
    import { Button, Input } from '@rneui/themed'

    // Tells Supabase Auth to continuously refresh the session automatically if
    // the app is in the foreground. When this is added, you will continue to receive
    // `onAuthStateChange` events with the `TOKEN_REFRESHED` or `SIGNED_OUT` event
    // if the user's session is terminated. This should only be registered once.
    AppState.addEventListener('change', (state) => {
      if (state === 'active') {
        supabase.auth.startAutoRefresh()
      } else {
        supabase.auth.stopAutoRefresh()
      }
    })

    export default function Auth() {
      const [email, setEmail] = useState('')
      const [password, setPassword] = useState('')
      const [loading, setLoading] = useState(false)

      async function signInWithEmail() {
        setLoading(true)
        const { error } = await supabase.auth.signInWithPassword({
          email: email,
          password: password,
        })

        if (error) Alert.alert(error.message)
        setLoading(false)
      }

      async function signUpWithEmail() {
        setLoading(true)
        const {
          data: { session },
          error,
        } = await supabase.auth.signUp({
          email: email,
          password: password,
        })

        if (error) Alert.alert(error.message)
        if (!session) Alert.alert('Please check your inbox for email verification!')
        setLoading(false)
      }

      return (
        <View style={styles.container}>
          <View style={[styles.verticallySpaced, styles.mt20]}>
            <Input
              label="Email"
              leftIcon={{ type: 'font-awesome', name: 'envelope' }}
              onChangeText={(text) => setEmail(text)}
              value={email}
              placeholder="email@address.com"
              autoCapitalize={'none'}
            />
          </View>
          <View style={styles.verticallySpaced}>
            <Input
              label="Password"
              leftIcon={{ type: 'font-awesome', name: 'lock' }}
              onChangeText={(text) => setPassword(text)}
              value={password}
              secureTextEntry={true}
              placeholder="Password"
              autoCapitalize={'none'}
            />
          </View>
          <View style={[styles.verticallySpaced, styles.mt20]}>
            <Button title="Sign in" disabled={loading} onPress={() => signInWithEmail()} />
          </View>
          <View style={styles.verticallySpaced}>
            <Button title="Sign up" disabled={loading} onPress={() => signUpWithEmail()} />
          </View>
        </View>
      )
    }

    const styles = StyleSheet.create({
      container: {
        marginTop: 40,
        padding: 12,
      },
      verticallySpaced: {
        paddingTop: 4,
        paddingBottom: 4,
        alignSelf: 'stretch',
      },
      mt20: {
        marginTop: 20,
      },
    })
    ```
  </TabPanel>
</Tabs>

<Admonition type="note">
  By default Supabase Auth requires email verification before a session is created for the users. To support email verification you need to [implement deep link handling](/docs/guides/auth/native-mobile-deep-linking?platform=react-native)!

  While testing, you can disable email confirmation in your [project's email auth provider settings](/dashboard/project/_/auth/providers).
</Admonition>


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `Account.tsx`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Account.tsx" label="components/Account.tsx">
    ```tsx name=components/Account.tsx
    import { useState, useEffect } from 'react'
    import { supabase } from '../lib/supabase'
    import { StyleSheet, View, Alert } from 'react-native'
    import { Button, Input } from '@rneui/themed'
    import { Session } from '@supabase/supabase-js'

    export default function Account({ session }: { session: Session }) {
      const [loading, setLoading] = useState(true)
      const [username, setUsername] = useState('')
      const [website, setWebsite] = useState('')
      const [avatarUrl, setAvatarUrl] = useState('')

      useEffect(() => {
        if (session) getProfile()
      }, [session])

      async function getProfile() {
        try {
          setLoading(true)
          if (!session?.user) throw new Error('No user on the session!')

          const { data, error, status } = await supabase
            .from('profiles')
            .select(`username, website, avatar_url`)
            .eq('id', session?.user.id)
            .single()
          if (error && status !== 406) {
            throw error
          }

          if (data) {
            setUsername(data.username)
            setWebsite(data.website)
            setAvatarUrl(data.avatar_url)
          }
        } catch (error) {
          if (error instanceof Error) {
            Alert.alert(error.message)
          }
        } finally {
          setLoading(false)
        }
      }

      async function updateProfile({
        username,
        website,
        avatar_url,
      }: {
        username: string
        website: string
        avatar_url: string
      }) {
        try {
          setLoading(true)
          if (!session?.user) throw new Error('No user on the session!')

          const updates = {
            id: session?.user.id,
            username,
            website,
            avatar_url,
            updated_at: new Date(),
          }

          const { error } = await supabase.from('profiles').upsert(updates)

          if (error) {
            throw error
          }
        } catch (error) {
          if (error instanceof Error) {
            Alert.alert(error.message)
          }
        } finally {
          setLoading(false)
        }
      }

      return (
        <View style={styles.container}>
          <View style={[styles.verticallySpaced, styles.mt20]}>
            <Input label="Email" value={session?.user?.email} disabled />
          </View>
          <View style={styles.verticallySpaced}>
            <Input label="Username" value={username || ''} onChangeText={(text) => setUsername(text)} />
          </View>
          <View style={styles.verticallySpaced}>
            <Input label="Website" value={website || ''} onChangeText={(text) => setWebsite(text)} />
          </View>

          <View style={[styles.verticallySpaced, styles.mt20]}>
            <Button
              title={loading ? 'Loading ...' : 'Update'}
              onPress={() => updateProfile({ username, website, avatar_url: avatarUrl })}
              disabled={loading}
            />
          </View>

          <View style={styles.verticallySpaced}>
            <Button title="Sign Out" onPress={() => supabase.auth.signOut()} />
          </View>
        </View>
      )
    }

    const styles = StyleSheet.create({
      container: {
        marginTop: 40,
        padding: 12,
      },
      verticallySpaced: {
        paddingTop: 4,
        paddingBottom: 4,
        alignSelf: 'stretch',
      },
      mt20: {
        marginTop: 20,
      },
    })
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `App.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="App.tsx" label="App.tsx">
    ```tsx name=App.tsx
    import { useState, useEffect } from 'react'
    import { supabase } from './lib/supabase'
    import Auth from './components/Auth'
    import Account from './components/Account'
    import { View } from 'react-native'
    import { Session } from '@supabase/supabase-js'

    export default function App() {
      const [session, setSession] = useState<Session | null>(null)

      useEffect(() => {
        supabase.auth.getSession().then(({ data: { session } }) => {
          setSession(session)
        })

        supabase.auth.onAuthStateChange((_event, session) => {
          setSession(session)
        })
      }, [])

      return (
        <View>
          {session && session.user ? <Account key={session.user.id} session={session} /> : <Auth />}
        </View>
      )
    }
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
npm start
```

And then press the appropriate key for the environment you want to test the app in and you should see the completed app.



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like
photos and videos.


### Additional dependency installation

You will need an image picker that works on the environment you will build the project for, we will use `expo-image-picker` in this example.

```bash
npx expo install expo-image-picker
```


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo.
We can start by creating a new component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Avatar.tsx" label="components/Avatar.tsx">
    ```tsx name=components/Avatar.tsx
    import { useState, useEffect } from 'react'
    import { supabase } from '../lib/supabase'
    import { StyleSheet, View, Alert, Image, Button } from 'react-native'
    import * as ImagePicker from 'expo-image-picker'

    interface Props {
      size: number
      url: string | null
      onUpload: (filePath: string) => void
    }

    export default function Avatar({ url, size = 150, onUpload }: Props) {
      const [uploading, setUploading] = useState(false)
      const [avatarUrl, setAvatarUrl] = useState<string | null>(null)
      const avatarSize = { height: size, width: size }

      useEffect(() => {
        if (url) downloadImage(url)
      }, [url])

      async function downloadImage(path: string) {
        try {
          const { data, error } = await supabase.storage.from('avatars').download(path)

          if (error) {
            throw error
          }

          const fr = new FileReader()
          fr.readAsDataURL(data)
          fr.onload = () => {
            setAvatarUrl(fr.result as string)
          }
        } catch (error) {
          if (error instanceof Error) {
            console.log('Error downloading image: ', error.message)
          }
        }
      }

      async function uploadAvatar() {
        try {
          setUploading(true)

          const result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.Images, // Restrict to only images
            allowsMultipleSelection: false, // Can only select one image
            allowsEditing: true, // Allows the user to crop / rotate their photo before uploading it
            quality: 1,
            exif: false, // We don't want nor need that data.
          })

          if (result.canceled || !result.assets || result.assets.length === 0) {
            console.log('User cancelled image picker.')
            return
          }

          const image = result.assets[0]
          console.log('Got image', image)

          if (!image.uri) {
            throw new Error('No image uri!') // Realistically, this should never happen, but just in case...
          }

          const arraybuffer = await fetch(image.uri).then((res) => res.arrayBuffer())

          const fileExt = image.uri?.split('.').pop()?.toLowerCase() ?? 'jpeg'
          const path = `${Date.now()}.${fileExt}`
          const { data, error: uploadError } = await supabase.storage
            .from('avatars')
            .upload(path, arraybuffer, {
              contentType: image.mimeType ?? 'image/jpeg',
            })

          if (uploadError) {
            throw uploadError
          }

          onUpload(data.path)
        } catch (error) {
          if (error instanceof Error) {
            Alert.alert(error.message)
          } else {
            throw error
          }
        } finally {
          setUploading(false)
        }
      }

      return (
        <View>
          {avatarUrl ? (
            <Image
              source={{ uri: avatarUrl }}
              accessibilityLabel="Avatar"
              style={[avatarSize, styles.avatar, styles.image]}
            />
          ) : (
            <View style={[avatarSize, styles.avatar, styles.noImage]} />
          )}
          <View>
            <Button
              title={uploading ? 'Uploading ...' : 'Upload'}
              onPress={uploadAvatar}
              disabled={uploading}
            />
          </View>
        </View>
      )
    }

    const styles = StyleSheet.create({
      avatar: {
        borderRadius: 5,
        overflow: 'hidden',
        maxWidth: '100%',
      },
      image: {
        objectFit: 'cover',
        paddingTop: 0,
      },
      noImage: {
        backgroundColor: '#333',
        borderWidth: 1,
        borderStyle: 'solid',
        borderColor: 'rgb(200, 200, 200)',
        borderRadius: 5,
      },
    })
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Account.tsx" label="components/Account.tsx">
    ```tsx name=components/Account.tsx
    // Import the new component
    import Avatar from './Avatar'

    // ...
    return (
      <View>
        {/* Add to the body */}
        <View>
          <Avatar
            size={200}
            url={avatarUrl}
            onUpload={(url: string) => {
              setAvatarUrl(url)
              updateProfile({ username, website, avatar_url: url })
            }}
          />
        </View>
        {/* ... */}
      </View>
    )
    // ...
    ```
  </TabPanel>
</Tabs>

Now you will need to run the prebuild command to get the application working on your chosen platform.

```bash
npx expo prebuild
```

At this stage you have a fully functional application!



# Build a User Management App with Flutter



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/supabase-flutter-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/flutter-user-management).
</Admonition>



## Project setup

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.


### Create a project

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.


### Set up the database schema

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
    3.  Click **Run**.

    <Admonition type="note">
      You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

      ```bash
      supabase link --project-ref <project-id>
      # You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>
      supabase db pull
      ```
    </Admonition>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    <Admonition type="note">
      When working locally you can run the following command to create a new migration file:
    </Admonition>

    ```bash
    supabase migration new user_management_starter
    ```

    ```sql
    -- Create a table for public profiles
    create table profiles (
      id uuid references auth.users not null primary key,
      updated_at timestamp with time zone,
      username text unique,
      full_name text,
      avatar_url text,
      website text,

      constraint username_length check (char_length(username) >= 3)
    );
    -- Set up Row Level Security (RLS)
    -- See https://supabase.com/docs/guides/database/postgres/row-level-security for more details.
    alter table profiles
      enable row level security;

    create policy "Public profiles are viewable by everyone." on profiles
      for select using (true);

    create policy "Users can insert their own profile." on profiles
      for insert with check ((select auth.uid()) = id);

    create policy "Users can update own profile." on profiles
      for update using ((select auth.uid()) = id);

    -- This trigger automatically creates a profile entry when a new user signs up via Supabase Auth.
    -- See https://supabase.com/docs/guides/auth/managing-user-data#using-triggers for more details.
    create function public.handle_new_user()
    returns trigger
    set search_path = ''
    as $$
    begin
      insert into public.profiles (id, full_name, avatar_url)
      values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
      return new;
    end;
    $$ language plpgsql security definer;
    create trigger on_auth_user_created
      after insert on auth.users
      for each row execute procedure public.handle_new_user();

    -- Set up Storage!
    insert into storage.buckets (id, name)
      values ('avatars', 'avatars');

    -- Set up access controls for storage.
    -- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
    create policy "Avatar images are publicly accessible." on storage.objects
      for select using (bucket_id = 'avatars');

    create policy "Anyone can upload an avatar." on storage.objects
      for insert with check (bucket_id = 'avatars');

    create policy "Anyone can update their own avatar." on storage.objects
      for update using ((select auth.uid()) = owner) with check (bucket_id = 'avatars');
    ```
  </TabPanel>
</Tabs>


### Get API details

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key. Get the URL from [the API settings section](/dashboard/project/_/settings/api) of a project and the key from the [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/).

<Admonition type="note" title="Changes to API keys">
  Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

  To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

  *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
  *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
</Admonition>



## Building the app

Let's start building the Flutter app from scratch.


### Initialize a Flutter app

We can use [`flutter create`](https://flutter.dev/docs/get-started/test-drive) to initialize
an app called `supabase_quickstart`:

```bash
flutter create supabase_quickstart
```

Then let's install the only additional dependency: [`supabase_flutter`](https://pub.dev/packages/supabase_flutter)

Copy and paste the following line in your pubspec.yaml to install the package:

```yaml
supabase_flutter: ^2.0.0
```

Run `flutter pub get` to install the dependencies.


### Setup deep links

Now that we have the dependencies installed let's setup deep links.
Setting up deep links is required to bring back the user to the app when they click on the magic link to sign in.
We can setup deep links with just a minor tweak on our Flutter application.

We have to use `io.supabase.flutterquickstart` as the scheme. In this example, we will use `login-callback` as the host for our deep link, but you can change it to whatever you would like.

First, add `io.supabase.flutterquickstart://login-callback/` as a new [redirect URL](/dashboard/project/_/auth/url-configuration) in the Dashboard.

![Supabase console deep link setting](/docs/img/deeplink-setting.png)

That is it on Supabase's end and the rest are platform specific settings:

<Tabs scrollable size="small" type="underlined" defaultActiveId="ios" queryGroup="platform">
  <TabPanel id="ios" label="iOS">
    Edit the `ios/Runner/Info.plist` file.

    Add `CFBundleURLTypes` to enable deep linking:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="ios/Runner/Info.plist&#x22;" label="ios/Runner/Info.plist&#x22;">
        ```xml name=ios/Runner/Info.plist"
        <!-- ... other tags -->
        <plist>
        <dict>
          <!-- ... other tags -->

          <!-- Add this array for Deep Links -->
          <key>CFBundleURLTypes</key>
          <array>
            <dict>
              <key>CFBundleTypeRole</key>
              <string>Editor</string>
              <key>CFBundleURLSchemes</key>
              <array>
                <string>io.supabase.flutterquickstart</string>
              </array>
            </dict>
          </array>
          <!-- ... other tags -->
        </dict>
        </plist>
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="android" label="Android">
    Edit the `android/app/src/main/AndroidManifest.xml` file.

    Add an intent-filter to enable deep linking:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="android/app/src/main/AndroidManifest.xml" label="android/app/src/main/AndroidManifest.xml">
        ```xml name=android/app/src/main/AndroidManifest.xml
        <manifest ...>
          <!-- ... other tags -->
          <application ...>
            <activity ...>
              <!-- ... other tags -->

              <!-- Add this intent-filter for Deep Links -->
              <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <!-- Accepts URIs that begin with YOUR_SCHEME://YOUR_HOST -->
                <data
                  android:scheme="io.supabase.flutterquickstart"
                  android:host="login-callback" />
              </intent-filter>

            </activity>
          </application>
        </manifest>
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="web" label="Web">
    Supabase redirects do not work with Flutter's [default URL strategy](https://docs.flutter.dev/ui/navigation/url-strategies).
    We can switch to the path URL strategy as follows:

    ```dart
    import 'package:flutter_web_plugins/url_strategy.dart';

    void main() {
      usePathUrlStrategy();
      runApp(ExampleApp());
    }
    ```
  </TabPanel>
</Tabs>


### Main function

Now that we have deep links ready let's initialize the Supabase client inside our `main` function with the API credentials that you copied [earlier](#get-the-api-keys). These variables will be exposed on the app, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/main.dart" label="lib/main.dart">
    ```dart name=lib/main.dart
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    Future<void> main() async {
      await Supabase.initialize(
        url: 'YOUR_SUPABASE_URL',
        anonKey: 'YOUR_SUPABASE_PUBLISHABLE_KEY',
      );
      runApp(const MyApp());
    }

    final supabase = Supabase.instance.client;

    class MyApp extends StatelessWidget {
      const MyApp({super.key});

      @override
      Widget build(BuildContext context) {
        return const MaterialApp(title: 'Supabase Flutter');
      }
    }

    extension ContextExtension on BuildContext {
      void showSnackBar(String message, {bool isError = false}) {
        ScaffoldMessenger.of(this).showSnackBar(
          SnackBar(
            content: Text(message),
            backgroundColor: isError
                ? Theme.of(this).colorScheme.error
                : Theme.of(this).snackBarTheme.backgroundColor,
          ),
        );
      }
    }
    ```
  </TabPanel>
</Tabs>

Notice that we have a `showSnackBar` extension method that we will use to show snack bars in the app. You could define this method in a separate file and import it where needed, but for simplicity, we will define it here.


### Set up a login page

Let's create a Flutter widget to manage logins and sign ups. We will use Magic Links, so users can sign in with their email without using passwords.

Notice that this page sets up a listener on the user's auth state using `onAuthStateChange`. A new event will fire when the user comes back to the app by clicking their magic link, which this page can catch and redirect the user accordingly.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/pages/login_page.dart" label="lib/pages/login_page.dart">
    ```dart name=lib/pages/login_page.dart
    import 'dart:async';

    import 'package:flutter/foundation.dart';
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:supabase_quickstart/main.dart';
    import 'package:supabase_quickstart/pages/account_page.dart';

    class LoginPage extends StatefulWidget {
      const LoginPage({super.key});

      @override
      State<LoginPage> createState() => _LoginPageState();
    }

    class _LoginPageState extends State<LoginPage> {
      bool _isLoading = false;
      bool _redirecting = false;
      late final TextEditingController _emailController = TextEditingController();
      late final StreamSubscription<AuthState> _authStateSubscription;

      Future<void> _signIn() async {
        try {
          setState(() {
            _isLoading = true;
          });
          await supabase.auth.signInWithOtp(
            email: _emailController.text.trim(),
            emailRedirectTo:
                kIsWeb ? null : 'io.supabase.flutterquickstart://login-callback/',
          );
          if (mounted) {
            context.showSnackBar('Check your email for a login link!');

            _emailController.clear();
          }
        } on AuthException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            setState(() {
              _isLoading = false;
            });
          }
        }
      }

      @override
      void initState() {
        _authStateSubscription = supabase.auth.onAuthStateChange.listen(
          (data) {
            if (_redirecting) return;
            final session = data.session;
            if (session != null) {
              _redirecting = true;
              Navigator.of(context).pushReplacement(
                MaterialPageRoute(builder: (context) => const AccountPage()),
              );
            }
          },
          onError: (error) {
            if (error is AuthException) {
              context.showSnackBar(error.message, isError: true);
            } else {
              context.showSnackBar('Unexpected error occurred', isError: true);
            }
          },
        );
        super.initState();
      }

      @override
      void dispose() {
        _emailController.dispose();
        _authStateSubscription.cancel();
        super.dispose();
      }

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Sign In')),
          body: ListView(
            padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 12),
            children: [
              const Text('Sign in via the magic link with your email below'),
              const SizedBox(height: 18),
              TextFormField(
                controller: _emailController,
                decoration: const InputDecoration(labelText: 'Email'),
              ),
              const SizedBox(height: 18),
              ElevatedButton(
                onPressed: _isLoading ? null : _signIn,
                child: Text(_isLoading ? 'Sending...' : 'Send Magic Link'),
              ),
            ],
          ),
        );
      }
    }
    ```
  </TabPanel>
</Tabs>


### Set up account page

After a user is signed in we can allow them to edit their profile details and manage their account.
Let's create a new widget called `account_page.dart` for that.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/pages/account_page.dart&#x22;" label="lib/pages/account_page.dart&#x22;">
    ```dart name=lib/pages/account_page.dart"
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:supabase_quickstart/main.dart';
    import 'package:supabase_quickstart/pages/login_page.dart';

    class AccountPage extends StatefulWidget {
      const AccountPage({super.key});

      @override
      State<AccountPage> createState() => _AccountPageState();
    }

    class _AccountPageState extends State<AccountPage> {
      final _usernameController = TextEditingController();
      final _websiteController = TextEditingController();

      String? _avatarUrl;
      var _loading = true;

      /// Called once a user id is received within `onAuthenticated()`
      Future<void> _getProfile() async {
        setState(() {
          _loading = true;
        });

        try {
          final userId = supabase.auth.currentSession!.user.id;
          final data =
              await supabase.from('profiles').select().eq('id', userId).single();
          _usernameController.text = (data['username'] ?? '') as String;
          _websiteController.text = (data['website'] ?? '') as String;
          _avatarUrl = (data['avatar_url'] ?? '') as String;
        } on PostgrestException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            setState(() {
              _loading = false;
            });
          }
        }
      }

      /// Called when user taps `Update` button
      Future<void> _updateProfile() async {
        setState(() {
          _loading = true;
        });
        final userName = _usernameController.text.trim();
        final website = _websiteController.text.trim();
        final user = supabase.auth.currentUser;
        final updates = {
          'id': user!.id,
          'username': userName,
          'website': website,
          'updated_at': DateTime.now().toIso8601String(),
        };
        try {
          await supabase.from('profiles').upsert(updates);
          if (mounted) context.showSnackBar('Successfully updated profile!');
        } on PostgrestException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            setState(() {
              _loading = false;
            });
          }
        }
      }

      Future<void> _signOut() async {
        try {
          await supabase.auth.signOut();
        } on AuthException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            Navigator.of(context).pushReplacement(
              MaterialPageRoute(builder: (_) => const LoginPage()),
            );
          }
        }
      }

      @override
      void initState() {
        super.initState();
        _getProfile();
      }

      @override
      void dispose() {
        _usernameController.dispose();
        _websiteController.dispose();
        super.dispose();
      }

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Profile')),
          body: ListView(
            padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 12),
            children: [
              TextFormField(
                controller: _usernameController,
                decoration: const InputDecoration(labelText: 'User Name'),
              ),
              const SizedBox(height: 18),
              TextFormField(
                controller: _websiteController,
                decoration: const InputDecoration(labelText: 'Website'),
              ),
              const SizedBox(height: 18),
              ElevatedButton(
                onPressed: _loading ? null : _updateProfile,
                child: Text(_loading ? 'Saving...' : 'Update'),
              ),
              const SizedBox(height: 18),
              TextButton(onPressed: _signOut, child: const Text('Sign Out')),
            ],
          ),
        );
      }
    }
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `lib/main.dart`.
The `home` of the `MaterialApp`, meaning the initial page shown to the user, will be the `LoginPage` if the user is not authenticated, and the `AccountPage` if the user is authenticated.
We also included some theming to make the app look a bit nicer.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/main.dart" label="lib/main.dart">
    ```dart name=lib/main.dart
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:supabase_quickstart/pages/account_page.dart';
    import 'package:supabase_quickstart/pages/login_page.dart';

    Future<void> main() async {
      await Supabase.initialize(
        url: 'YOUR_SUPABASE_URL',
        anonKey: 'YOUR_SUPABASE_PUBLISHABLE_KEY',
      );
      runApp(const MyApp());
    }

    final supabase = Supabase.instance.client;

    class MyApp extends StatelessWidget {
      const MyApp({super.key});

      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          title: 'Supabase Flutter',
          theme: ThemeData.dark().copyWith(
            primaryColor: Colors.green,
            textButtonTheme: TextButtonThemeData(
              style: TextButton.styleFrom(
                foregroundColor: Colors.green,
              ),
            ),
            elevatedButtonTheme: ElevatedButtonThemeData(
              style: ElevatedButton.styleFrom(
                foregroundColor: Colors.white,
                backgroundColor: Colors.green,
              ),
            ),
          ),
          home: supabase.auth.currentSession == null
              ? const LoginPage()
              : const AccountPage(),
        );
      }
    }

    extension ContextExtension on BuildContext {
      void showSnackBar(String message, {bool isError = false}) {
        ScaffoldMessenger.of(this).showSnackBar(
          SnackBar(
            content: Text(message),
            backgroundColor: isError
                ? Theme.of(this).colorScheme.error
                : Theme.of(this).snackBarTheme.backgroundColor,
          ),
        );
      }
    }
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window to launch on Android or iOS:

```bash
flutter run
```

Or for web, run the following command to launch it on `localhost:3000`

```bash
flutter run -d web-server --web-hostname localhost --web-port 3000
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase User Management example](/docs/img/supabase-flutter-account-page.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like
photos and videos.


### Making sure we have a public bucket

We will be storing the image as a publicly sharable image.
Make sure your `avatars` bucket is set to public, and if it is not, change the publicity by clicking the dot menu that appears when you hover over the bucket name.
You should see an orange `Public` badge next to your bucket name if your bucket is set to public.


### Adding image uploading feature to account page

We will use [`image_picker`](https://pub.dev/packages/image_picker) plugin to select an image from the device.

Add the following line in your pubspec.yaml file to install `image_picker`:

```yaml
image_picker: ^1.0.5
```

Using [`image_picker`](https://pub.dev/packages/image_picker) requires some additional preparation depending on the platform.
Follow the instruction on README.md of [`image_picker`](https://pub.dev/packages/image_picker) on how to set it up for the platform you are using.

Once you are done with all of the above, it is time to dive into coding.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo.
We can start by creating a new component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/components/avatar.dart" label="lib/components/avatar.dart">
    ```dart name=lib/components/avatar.dart
    import 'package:flutter/material.dart';
    import 'package:image_picker/image_picker.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:supabase_quickstart/main.dart';

    class Avatar extends StatefulWidget {
      const Avatar({
        super.key,
        required this.imageUrl,
        required this.onUpload,
      });

      final String? imageUrl;
      final void Function(String) onUpload;

      @override
      State<Avatar> createState() => _AvatarState();
    }

    class _AvatarState extends State<Avatar> {
      bool _isLoading = false;

      @override
      Widget build(BuildContext context) {
        return Column(
          children: [
            if (widget.imageUrl == null || widget.imageUrl!.isEmpty)
              Container(
                width: 150,
                height: 150,
                color: Colors.grey,
                child: const Center(
                  child: Text('No Image'),
                ),
              )
            else
              Image.network(
                widget.imageUrl!,
                width: 150,
                height: 150,
                fit: BoxFit.cover,
              ),
            ElevatedButton(
              onPressed: _isLoading ? null : _upload,
              child: const Text('Upload'),
            ),
          ],
        );
      }

      Future<void> _upload() async {
        final picker = ImagePicker();
        final imageFile = await picker.pickImage(
          source: ImageSource.gallery,
          maxWidth: 300,
          maxHeight: 300,
        );
        if (imageFile == null) {
          return;
        }
        setState(() => _isLoading = true);

        try {
          final bytes = await imageFile.readAsBytes();
          final fileExt = imageFile.path.split('.').last;
          final fileName = '${DateTime.now().toIso8601String()}.$fileExt';
          final filePath = fileName;
          await supabase.storage.from('avatars').uploadBinary(
                filePath,
                bytes,
                fileOptions: FileOptions(contentType: imageFile.mimeType),
              );
          final imageUrlResponse = await supabase.storage
              .from('avatars')
              .createSignedUrl(filePath, 60 * 60 * 24 * 365 * 10);
          widget.onUpload(imageUrlResponse);
        } on StorageException catch (error) {
          if (mounted) {
            context.showSnackBar(error.message, isError: true);
          }
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        }

        setState(() => _isLoading = false);
      }
    }
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page as well as some logic to update the `avatar_url` whenever the user uploads a new avatar.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="lib/pages/account_page.dart" label="lib/pages/account_page.dart">
    ```dart name=lib/pages/account_page.dart
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:supabase_quickstart/components/avatar.dart';
    import 'package:supabase_quickstart/main.dart';
    import 'package:supabase_quickstart/pages/login_page.dart';

    class AccountPage extends StatefulWidget {
      const AccountPage({super.key});

      @override
      State<AccountPage> createState() => _AccountPageState();
    }

    class _AccountPageState extends State<AccountPage> {
      final _usernameController = TextEditingController();
      final _websiteController = TextEditingController();

      String? _avatarUrl;
      var _loading = true;

      /// Called once a user id is received within `onAuthenticated()`
      Future<void> _getProfile() async {
        setState(() {
          _loading = true;
        });

        try {
          final userId = supabase.auth.currentSession!.user.id;
          final data =
              await supabase.from('profiles').select().eq('id', userId).single();
          _usernameController.text = (data['username'] ?? '') as String;
          _websiteController.text = (data['website'] ?? '') as String;
          _avatarUrl = (data['avatar_url'] ?? '') as String;
        } on PostgrestException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            setState(() {
              _loading = false;
            });
          }
        }
      }

      /// Called when user taps `Update` button
      Future<void> _updateProfile() async {
        setState(() {
          _loading = true;
        });
        final userName = _usernameController.text.trim();
        final website = _websiteController.text.trim();
        final user = supabase.auth.currentUser;
        final updates = {
          'id': user!.id,
          'username': userName,
          'website': website,
          'updated_at': DateTime.now().toIso8601String(),
        };
        try {
          await supabase.from('profiles').upsert(updates);
          if (mounted) context.showSnackBar('Successfully updated profile!');
        } on PostgrestException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            setState(() {
              _loading = false;
            });
          }
        }
      }

      Future<void> _signOut() async {
        try {
          await supabase.auth.signOut();
        } on AuthException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        } finally {
          if (mounted) {
            Navigator.of(context).pushReplacement(
              MaterialPageRoute(builder: (_) => const LoginPage()),
            );
          }
        }
      }

      /// Called when image has been uploaded to Supabase storage from within Avatar widget
      Future<void> _onUpload(String imageUrl) async {
        try {
          final userId = supabase.auth.currentUser!.id;
          await supabase.from('profiles').upsert({
            'id': userId,
            'avatar_url': imageUrl,
          });
          if (mounted) {
            const SnackBar(
              content: Text('Updated your profile image!'),
            );
          }
        } on PostgrestException catch (error) {
          if (mounted) context.showSnackBar(error.message, isError: true);
        } catch (error) {
          if (mounted) {
            context.showSnackBar('Unexpected error occurred', isError: true);
          }
        }
        if (!mounted) {
          return;
        }

        setState(() {
          _avatarUrl = imageUrl;
        });
      }

      @override
      void initState() {
        super.initState();
        _getProfile();
      }

      @override
      void dispose() {
        _usernameController.dispose();
        _websiteController.dispose();
        super.dispose();
      }

      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(title: const Text('Profile')),
          body: ListView(
            padding: const EdgeInsets.symmetric(vertical: 18, horizontal: 12),
            children: [
              Avatar(
                imageUrl: _avatarUrl,
                onUpload: _onUpload,
              ),
              const SizedBox(height: 18),
              TextFormField(
                controller: _usernameController,
                decoration: const InputDecoration(labelText: 'User Name'),
              ),
              const SizedBox(height: 18),
              TextFormField(
                controller: _websiteController,
                decoration: const InputDecoration(labelText: 'Website'),
              ),
              const SizedBox(height: 18),
              ElevatedButton(
                onPressed: _loading ? null : _updateProfile,
                child: Text(_loading ? 'Saving...' : 'Update'),
              ),
              const SizedBox(height: 18),
              TextButton(onPressed: _signOut, child: const Text('Sign Out')),
            ],
          ),
        );
      }
    }
    ```
  </TabPanel>
</Tabs>

Congratulations, you've built a fully functional user management app using Flutter and Supabase!



## See also

*   [Flutter Tutorial: building a Flutter chat app](/blog/flutter-tutorial-building-a-chat-app)
*   [Flutter Tutorial - Part 2: Authentication and Authorization with RLS](/blog/flutter-authentication-and-authorization-with-rls)



# Build a User Management App with Ionic Angular



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/ionic-demos/ionic-angular-account.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/mhartington/supabase-ionic-angular).
</Admonition>



## Project setup

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.


### Create a project

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.


### Set up the database schema

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
    3.  Click **Run**.

    <Admonition type="note">
      You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

      ```bash
      supabase link --project-ref <project-id>
      # You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>
      supabase db pull
      ```
    </Admonition>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    <Admonition type="note">
      When working locally you can run the following command to create a new migration file:
    </Admonition>

    ```bash
    supabase migration new user_management_starter
    ```

    ```sql
    -- Create a table for public profiles
    create table profiles (
      id uuid references auth.users not null primary key,
      updated_at timestamp with time zone,
      username text unique,
      full_name text,
      avatar_url text,
      website text,

      constraint username_length check (char_length(username) >= 3)
    );
    -- Set up Row Level Security (RLS)
    -- See https://supabase.com/docs/guides/database/postgres/row-level-security for more details.
    alter table profiles
      enable row level security;

    create policy "Public profiles are viewable by everyone." on profiles
      for select using (true);

    create policy "Users can insert their own profile." on profiles
      for insert with check ((select auth.uid()) = id);

    create policy "Users can update own profile." on profiles
      for update using ((select auth.uid()) = id);

    -- This trigger automatically creates a profile entry when a new user signs up via Supabase Auth.
    -- See https://supabase.com/docs/guides/auth/managing-user-data#using-triggers for more details.
    create function public.handle_new_user()
    returns trigger
    set search_path = ''
    as $$
    begin
      insert into public.profiles (id, full_name, avatar_url)
      values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
      return new;
    end;
    $$ language plpgsql security definer;
    create trigger on_auth_user_created
      after insert on auth.users
      for each row execute procedure public.handle_new_user();

    -- Set up Storage!
    insert into storage.buckets (id, name)
      values ('avatars', 'avatars');

    -- Set up access controls for storage.
    -- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
    create policy "Avatar images are publicly accessible." on storage.objects
      for select using (bucket_id = 'avatars');

    create policy "Anyone can upload an avatar." on storage.objects
      for insert with check (bucket_id = 'avatars');

    create policy "Anyone can update their own avatar." on storage.objects
      for update using ((select auth.uid()) = owner) with check (bucket_id = 'avatars');
    ```
  </TabPanel>
</Tabs>


### Get API details

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key. Get the URL from [the API settings section](/dashboard/project/_/settings/api) of a project and the key from the [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/).

<Admonition type="note" title="Changes to API keys">
  Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

  To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

  *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
  *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
</Admonition>



## Building the app

Let's start building the Angular app from scratch.


### Initialize an Ionic Angular app

We can use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize
an app called `supabase-ionic-angular`:

```bash
npm install -g @ionic/cli
ionic start supabase-ionic-angular blank --type angular
cd supabase-ionic-angular
```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npm install @supabase/supabase-js
```

And finally, we want to save the environment variables in the `src/environments/environment.ts` file.
All we need are the API URL and the key that you copied [earlier](#get-api-details).
These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="environment.ts" label="environment.ts">
    ```ts name=environment.ts
    export const environment = {
      production: false,
      supabaseUrl: 'YOUR_SUPABASE_URL',
      supabaseKey: 'YOUR_SUPABASE_KEY',
    }
    ```
  </TabPanel>
</Tabs>

Now that we have the API credentials in place, let's create a `SupabaseService` with `ionic g s supabase` to initialize the Supabase client and implement functions to communicate with the Supabase API.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/supabase.service.ts" label="src/app/supabase.service.ts">
    ```ts name=src/app/supabase.service.ts
    import { Injectable } from '@angular/core'
    import { LoadingController, ToastController } from '@ionic/angular'
    import { AuthChangeEvent, createClient, Session, SupabaseClient } from '@supabase/supabase-js'
    import { environment } from '../environments/environment'

    export interface Profile {
      username: string
      website: string
      avatar_url: string
    }

    @Injectable({
      providedIn: 'root',
    })
    export class SupabaseService {
      private supabase: SupabaseClient

      constructor(
        private loadingCtrl: LoadingController,
        private toastCtrl: ToastController
      ) {
        this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
      }

      get user() {
        return this.supabase.auth.getUser().then(({ data }) => data?.user)
      }

      get session() {
        return this.supabase.auth.getSession().then(({ data }) => data?.session)
      }

      get profile() {
        return this.user
          .then((user) => user?.id)
          .then((id) =>
            this.supabase.from('profiles').select(`username, website, avatar_url`).eq('id', id).single()
          )
      }

      authChanges(callback: (event: AuthChangeEvent, session: Session | null) => void) {
        return this.supabase.auth.onAuthStateChange(callback)
      }

      signIn(email: string) {
        return this.supabase.auth.signInWithOtp({ email })
      }

      signOut() {
        return this.supabase.auth.signOut()
      }

      async updateProfile(profile: Profile) {
        const user = await this.user
        const update = {
          ...profile,
          id: user?.id,
          updated_at: new Date(),
        }

        return this.supabase.from('profiles').upsert(update)
      }

      downLoadImage(path: string) {
        return this.supabase.storage.from('avatars').download(path)
      }

      uploadAvatar(filePath: string, file: File) {
        return this.supabase.storage.from('avatars').upload(filePath, file)
      }

      async createNotice(message: string) {
        const toast = await this.toastCtrl.create({ message, duration: 5000 })
        await toast.present()
      }

      createLoader() {
        return this.loadingCtrl.create()
      }
    }
    ```
  </TabPanel>
</Tabs>


### Set up a login route

Let's set up a route to manage logins and signups. We'll use Magic Links so users can sign in with their email without using passwords.
Create a `LoginPage` with the `ionic g page login` Ionic CLI command.

<Admonition type="tip">
  This guide will show the template inline, but the example app will have `templateUrl`s
</Admonition>

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/login/login.page.ts" label="src/app/login/login.page.ts">
    ```ts name=src/app/login/login.page.ts
    import { Component, OnInit } from '@angular/core'
    import { SupabaseService } from '../supabase.service'

    @Component({
      selector: 'app-login',
      template: `
        <ion-header>
          <ion-toolbar>
            <ion-title>Login</ion-title>
          </ion-toolbar>
        </ion-header>

        <ion-content>
          <div class="ion-padding">
            <h1>Supabase + Ionic Angular</h1>
            <p>Sign in via magic link with your email below</p>
          </div>
          <ion-list inset="true">
            <form (ngSubmit)="handleLogin($event)">
              <ion-item>
                <ion-label position="stacked">Email</ion-label>
                <ion-input [(ngModel)]="email" name="email" autocomplete type="email"></ion-input>
              </ion-item>
              <div class="ion-text-center">
                <ion-button type="submit" fill="clear">Login</ion-button>
              </div>
            </form>
          </ion-list>
        </ion-content>
      `,
      styleUrls: ['./login.page.scss'],
    })
    export class LoginPage {
      email = ''

      constructor(private readonly supabase: SupabaseService) {}

      async handleLogin(event: any) {
        event.preventDefault()
        const loader = await this.supabase.createLoader()
        await loader.present()
        try {
          const { error } = await this.supabase.signIn(this.email)
          if (error) {
            throw error
          }
          await loader.dismiss()
          await this.supabase.createNotice('Check your email for the login link!')
        } catch (error: any) {
          await loader.dismiss()
          await this.supabase.createNotice(error.error_description || error.message)
        }
      }
    }
    ```
  </TabPanel>
</Tabs>


### Account page

After a user is signed in, we can allow them to edit their profile details and manage their account.
Create an `AccountComponent` with `ionic g page account` Ionic CLI command.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/account.page.ts" label="src/app/account.page.ts">
    ```ts name=src/app/account.page.ts
    import { Component, OnInit } from '@angular/core'
    import { Router } from '@angular/router'
    import { Profile, SupabaseService } from '../supabase.service'

    @Component({
      selector: 'app-account',
      template: `
        <ion-header>
          <ion-toolbar>
            <ion-title>Account</ion-title>
          </ion-toolbar>
        </ion-header>

        <ion-content>
          <form>
            <ion-item>
              <ion-label position="stacked">Email</ion-label>
              <ion-input type="email" name="email" [(ngModel)]="email" readonly></ion-input>
            </ion-item>

            <ion-item>
              <ion-label position="stacked">Name</ion-label>
              <ion-input type="text" name="username" [(ngModel)]="profile.username"></ion-input>
            </ion-item>

            <ion-item>
              <ion-label position="stacked">Website</ion-label>
              <ion-input type="url" name="website" [(ngModel)]="profile.website"></ion-input>
            </ion-item>
            <div class="ion-text-center">
              <ion-button fill="clear" (click)="updateProfile()">Update Profile</ion-button>
            </div>
          </form>

          <div class="ion-text-center">
            <ion-button fill="clear" (click)="signOut()">Log Out</ion-button>
          </div>
        </ion-content>
      `,
      styleUrls: ['./account.page.scss'],
    })
    export class AccountPage implements OnInit {
      profile: Profile = {
        username: '',
        avatar_url: '',
        website: '',
      }

      email = ''

      constructor(
        private readonly supabase: SupabaseService,
        private router: Router
      ) {}
      ngOnInit() {
        this.getEmail()
        this.getProfile()
      }

      async getEmail() {
        this.email = await this.supabase.user.then((user) => user?.email || '')
      }

      async getProfile() {
        try {
          const { data: profile, error, status } = await this.supabase.profile
          if (error && status !== 406) {
            throw error
          }
          if (profile) {
            this.profile = profile
          }
        } catch (error: any) {
          alert(error.message)
        }
      }

      async updateProfile(avatar_url: string = '') {
        const loader = await this.supabase.createLoader()
        await loader.present()
        try {
          const { error } = await this.supabase.updateProfile({ ...this.profile, avatar_url })
          if (error) {
            throw error
          }
          await loader.dismiss()
          await this.supabase.createNotice('Profile updated!')
        } catch (error: any) {
          await loader.dismiss()
          await this.supabase.createNotice(error.message)
        }
      }

      async signOut() {
        console.log('testing?')
        await this.supabase.signOut()
        this.router.navigate(['/'], { replaceUrl: true })
      }
    }
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `AppComponent`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/app.component.ts" label="src/app/app.component.ts">
    ```ts name=src/app/app.component.ts
    import { Component } from '@angular/core'
    import { Router } from '@angular/router'
    import { SupabaseService } from './supabase.service'

    @Component({
      selector: 'app-root',
      template: `
        <ion-app>
          <ion-router-outlet></ion-router-outlet>
        </ion-app>
      `,
      styleUrls: ['app.component.scss'],
    })
    export class AppComponent {
      constructor(
        private supabase: SupabaseService,
        private router: Router
      ) {
        this.supabase.authChanges((_, session) => {
          console.log(session)
          if (session?.user) {
            this.router.navigate(['/account'])
          }
        })
      }
    }
    ```
  </TabPanel>
</Tabs>

Then update the `AppRoutingModule`

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/app-routing.module.ts&#x22;" label="src/app/app-routing.module.ts&#x22;">
    ```ts name=src/app/app-routing.module.ts"
    import { NgModule } from '@angular/core'
    import { PreloadAllModules, RouterModule, Routes } from '@angular/router'

    const routes: Routes = [
      {
        path: '',
        loadChildren: () => import('./login/login.module').then((m) => m.LoginPageModule),
      },
      {
        path: 'account',
        loadChildren: () => import('./account/account.module').then((m) => m.AccountPageModule),
      },
    ]

    @NgModule({
      imports: [
        RouterModule.forRoot(routes, {
          preloadingStrategy: PreloadAllModules,
        }),
      ],
      exports: [RouterModule],
    })
    export class AppRoutingModule {}
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
ionic serve
```

And the browser will automatically open to show the app.

![Supabase Angular](/docs/img/ionic-demos/ionic-angular.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo.

First, install two packages in order to interact with the user's camera.

```bash
npm install @ionic/pwa-elements @capacitor/camera
```

[Capacitor](https://capacitorjs.com) is a cross-platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.

Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.

With those packages installed, we can update our `main.ts` to include an additional bootstrapping call for the Ionic PWA Elements.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/main.ts" label="src/main.ts">
    ```ts name=src/main.ts
    import { enableProdMode } from '@angular/core'
    import { platformBrowserDynamic } from '@angular/platform-browser-dynamic'

    import { AppModule } from './app/app.module'
    import { environment } from './environments/environment'

    import { defineCustomElements } from '@ionic/pwa-elements/loader'
    defineCustomElements(window)

    if (environment.production) {
      enableProdMode()
    }
    platformBrowserDynamic()
      .bootstrapModule(AppModule)
      .catch((err) => console.log(err))
    ```
  </TabPanel>
</Tabs>

Then create an `AvatarComponent` with this Ionic CLI command:

```bash
 ionic g component avatar --module=/src/app/account/account.module.ts --create-module
```

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/avatar.component.ts" label="src/app/avatar.component.ts">
    ```ts name=src/app/avatar.component.ts
    import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core'
    import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser'
    import { SupabaseService } from '../supabase.service'
    import { Camera, CameraResultType } from '@capacitor/camera'
    import { addIcons } from 'ionicons'
    import { person } from 'ionicons/icons'
    @Component({
      selector: 'app-avatar',
      template: `
        <div class="avatar_wrapper" (click)="uploadAvatar()">
          <img *ngIf="_avatarUrl; else noAvatar" [src]="_avatarUrl" />
          <ng-template #noAvatar>
            <ion-icon name="person" class="no-avatar"></ion-icon>
          </ng-template>
        </div>
      `,
      style: [
        `
        :host {
           display: block;
           margin: auto;
           min-height: 150px;
        }
         :host .avatar_wrapper {
           margin: 16px auto 16px;
           border-radius: 50%;
           overflow: hidden;
           height: 150px;
           aspect-ratio: 1;
           background: var(--ion-color-step-50);
           border: thick solid var(--ion-color-step-200);
        }
         :host .avatar_wrapper:hover {
           cursor: pointer;
        }
         :host .avatar_wrapper ion-icon.no-avatar {
           width: 100%;
           height: 115%;
        }
         :host img {
           display: block;
           object-fit: cover;
           width: 100%;
           height: 100%;
        }
      `,
      ],
    })
    export class AvatarComponent {
      _avatarUrl: SafeResourceUrl | undefined
      uploading = false

      @Input()
      set avatarUrl(url: string | undefined) {
        if (url) {
          this.downloadImage(url)
        }
      }

      @Output() upload = new EventEmitter<string>()

      constructor(
        private readonly supabase: SupabaseService,
        private readonly dom: DomSanitizer
      ) {
        addIcons({ person })
      }

      async downloadImage(path: string) {
        try {
          const { data, error } = await this.supabase.downLoadImage(path)
          if (error) {
            throw error
          }
          this._avatarUrl = this.dom.bypassSecurityTrustResourceUrl(URL.createObjectURL(data!))
        } catch (error: any) {
          console.error('Error downloading image: ', error.message)
        }
      }

      async uploadAvatar() {
        const loader = await this.supabase.createLoader()
        try {
          const photo = await Camera.getPhoto({
            resultType: CameraResultType.DataUrl,
          })

          const file = await fetch(photo.dataUrl!)
            .then((res) => res.blob())
            .then((blob) => new File([blob], 'my-file', { type: `image/${photo.format}` }))

          const fileName = `${Math.random()}-${new Date().getTime()}.${photo.format}`

          await loader.present()
          const { error } = await this.supabase.uploadAvatar(fileName, file)

          if (error) {
            throw error
          }

          this.upload.emit(fileName)
        } catch (error: any) {
          this.supabase.createNotice(error.message)
        } finally {
          loader.dismiss()
        }
      }
    }
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then, we can add the widget on top of the `AccountComponent` HTML template:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app/account.component.ts" label="src/app/account.component.ts">
    ```ts name=src/app/account.component.ts
    template: `
    <ion-header>
      <ion-toolbar>
        <ion-title>Account</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
      <app-avatar
        [avatarUrl]="this.profile?.avatar_url"
        (upload)="updateProfile($event)"
      ></app-avatar>

    <!-- input fields -->
    `
    ```
  </TabPanel>
</Tabs>

At this stage, you have a fully functional application!



## See also

*   [Authentication in Ionic Angular with Supabase](/blog/authentication-in-ionic-angular)



# Build a User Management App with Ionic React



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/ionic-demos/ionic-angular-account.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/mhartington/supabase-ionic-react).
</Admonition>



## Project setup

Before you start building you need to set up the Database and API. You can do this by starting a new Project in Supabase and then creating a "schema" inside the database.


### Create a project

1.  [Create a new project](/dashboard) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.


### Set up the database schema

Now set up the database schema. You can use the "User Management Starter" quickstart in the SQL Editor, or you can copy/paste the SQL from below and run it.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [SQL Editor](/dashboard/project/_/sql) page in the Dashboard.
    2.  Click **User Management Starter** under the **Community > Quickstarts** tab.
    3.  Click **Run**.

    <Admonition type="note">
      You can pull the database schema down to your local project by running the `db pull` command. Read the [local development docs](/docs/guides/cli/local-development#link-your-project) for detailed instructions.

      ```bash
      supabase link --project-ref <project-id>
      # You can get <project-id> from your project's dashboard URL: https://supabase.com/dashboard/project/<project-id>
      supabase db pull
      ```
    </Admonition>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    <Admonition type="note">
      When working locally you can run the following command to create a new migration file:
    </Admonition>

    ```bash
    supabase migration new user_management_starter
    ```

    ```sql
    -- Create a table for public profiles
    create table profiles (
      id uuid references auth.users not null primary key,
      updated_at timestamp with time zone,
      username text unique,
      full_name text,
      avatar_url text,
      website text,

      constraint username_length check (char_length(username) >= 3)
    );
    -- Set up Row Level Security (RLS)
    -- See https://supabase.com/docs/guides/database/postgres/row-level-security for more details.
    alter table profiles
      enable row level security;

    create policy "Public profiles are viewable by everyone." on profiles
      for select using (true);

    create policy "Users can insert their own profile." on profiles
      for insert with check ((select auth.uid()) = id);

    create policy "Users can update own profile." on profiles
      for update using ((select auth.uid()) = id);

    -- This trigger automatically creates a profile entry when a new user signs up via Supabase Auth.
    -- See https://supabase.com/docs/guides/auth/managing-user-data#using-triggers for more details.
    create function public.handle_new_user()
    returns trigger
    set search_path = ''
    as $$
    begin
      insert into public.profiles (id, full_name, avatar_url)
      values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
      return new;
    end;
    $$ language plpgsql security definer;
    create trigger on_auth_user_created
      after insert on auth.users
      for each row execute procedure public.handle_new_user();

    -- Set up Storage!
    insert into storage.buckets (id, name)
      values ('avatars', 'avatars');

    -- Set up access controls for storage.
    -- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
    create policy "Avatar images are publicly accessible." on storage.objects
      for select using (bucket_id = 'avatars');

    create policy "Anyone can upload an avatar." on storage.objects
      for insert with check (bucket_id = 'avatars');

    create policy "Anyone can update their own avatar." on storage.objects
      for update using ((select auth.uid()) = owner) with check (bucket_id = 'avatars');
    ```
  </TabPanel>
</Tabs>


### Get API details

Now that you've created some database tables, you are ready to insert data using the auto-generated API.

To do this, you need to get the Project URL and key. Get the URL from [the API settings section](/dashboard/project/_/settings/api) of a project and the key from the [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/).

<Admonition type="note" title="Changes to API keys">
  Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

  To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

  *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
  *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
</Admonition>



## Building the app

Let's start building the React app from scratch.


### Initialize an Ionic React app

We can use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize
an app called `supabase-ionic-react`:

```bash
npm install -g @ionic/cli
ionic start supabase-ionic-react blank --type react
cd supabase-ionic-react
```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npm install @supabase/supabase-js
```

And finally we want to save the environment variables in a `.env`.
All we need are the API URL and the key that you copied [earlier](#get-api-details).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    VITE_SUPABASE_URL=YOUR_SUPABASE_URL
    VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
    ```
  </TabPanel>
</Tabs>

Now that we have the API credentials in place, let's create a helper file to initialize the Supabase client. These variables will be exposed
on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/supabaseClient.ts" label="src/supabaseClient.ts">
    ```js name=src/supabaseClient.ts
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || ''
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY || ''

    export const supabase = createClient(supabaseUrl, supabasePublishableKey)
    ```
  </TabPanel>
</Tabs>


### Set up a login route

Let's set up a React component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="/src/pages/Login.tsx" label="/src/pages/Login.tsx">
    ```jsx name=/src/pages/Login.tsx
    import { useState } from 'react';
    import {
      IonButton,
      IonContent,
      IonHeader,
      IonInput,
      IonItem,
      IonLabel,
      IonList,
      IonPage,
      IonTitle,
      IonToolbar,
      useIonToast,
      useIonLoading,
    } from '@ionic/react';

    import {supabase} from '../supabaseClient'

    export function LoginPage() {
      const [email, setEmail] = useState('');

      const [showLoading, hideLoading] = useIonLoading();
      const [showToast ] = useIonToast();
      const handleLogin = async (e: React.FormEvent<HTMLFormElement>) => {
        console.log()
        e.preventDefault();
        await showLoading();
        try {
          await supabase.auth.signInWithOtp({
            "email": email
          });
          await showToast({ message: 'Check your email for the login link!' });
        } catch (e: any) {
          await showToast({ message: e.error_description || e.message , duration: 5000});
        } finally {
          await hideLoading();
        }
      };
      return (
        <IonPage>
          <IonHeader>
            <IonToolbar>
              <IonTitle>Login</IonTitle>
            </IonToolbar>
          </IonHeader>

          <IonContent>
            <div className="ion-padding">
              <h1>Supabase + Ionic React</h1>
              <p>Sign in via magic link with your email below</p>
            </div>
            <IonList inset={true}>
              <form onSubmit={handleLogin}>
                <IonItem>
                  <IonLabel position="stacked">Email</IonLabel>
                  <IonInput
                    value={email}
                    name="email"
                    onIonChange={(e) => setEmail(e.detail.value ?? '')}
                    type="email"
                  ></IonInput>
                </IonItem>
                <div className="ion-text-center">
                  <IonButton type="submit" fill="clear">
                    Login
                  </IonButton>
                </div>
              </form>
            </IonList>
          </IonContent>
        </IonPage>
      );
    }
    ```
  </TabPanel>
</Tabs>


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `Account.tsx`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/pages/Account.tsx" label="src/pages/Account.tsx">
    ```jsx name=src/pages/Account.tsx
    import {
      IonButton,
      IonContent,
      IonHeader,
      IonInput,
      IonItem,
      IonLabel,
      IonPage,
      IonTitle,
      IonToolbar,
      useIonLoading,
      useIonToast,
      useIonRouter
    } from '@ionic/react';
    import { useEffect, useState } from 'react';
    import { supabase } from '../supabaseClient';
    import { Session } from '@supabase/supabase-js';

    export function AccountPage() {
      const [showLoading, hideLoading] = useIonLoading();
      const [showToast] = useIonToast();
      const [session, setSession] = useState<Session | null>(null)
      const router = useIonRouter();
      const [profile, setProfile] = useState({
        username: '',
        website: '',
        avatar_url: '',
      });

      useEffect(() => {
        const getSession = async () => {
          setSession(await supabase.auth.getSession().then((res) => res.data.session))
        }
        getSession()
        supabase.auth.onAuthStateChange((_event, session) => {
          setSession(session)
        })
      }, [])

      useEffect(() => {
        getProfile();
      }, [session]);
      const getProfile = async () => {
        console.log('get');
        await showLoading();
        try {
          const user = await supabase.auth.getUser();
          const { data, error, status } = await supabase
            .from('profiles')
            .select(`username, website, avatar_url`)
            .eq('id', user!.data.user?.id)
            .single();

          if (error && status !== 406) {
            throw error;
          }

          if (data) {
            setProfile({
              username: data.username,
              website: data.website,
              avatar_url: data.avatar_url,
            });
          }
        } catch (error: any) {
          showToast({ message: error.message, duration: 5000 });
        } finally {
          await hideLoading();
        }
      };
      const signOut = async () => {
        await supabase.auth.signOut();
        router.push('/', 'forward', 'replace');
      }
      const updateProfile = async (e?: any, avatar_url: string = '') => {
        e?.preventDefault();

        console.log('update ');
        await showLoading();

        try {
          const user = await supabase.auth.getUser();

          const updates = {
            id: user!.data.user?.id,
            ...profile,
            avatar_url: avatar_url,
            updated_at: new Date(),
          };

          const { error } = await supabase.from('profiles').upsert(updates);

          if (error) {
            throw error;
          }
        } catch (error: any) {
          showToast({ message: error.message, duration: 5000 });
        } finally {
          await hideLoading();
        }
      };
      return (
        <IonPage>
          <IonHeader>
            <IonToolbar>
              <IonTitle>Account</IonTitle>
            </IonToolbar>
          </IonHeader>

          <IonContent>
            <form onSubmit={updateProfile}>
              <IonItem>
                <IonLabel>
                  <p>Email</p>
                  <p>{session?.user?.email}</p>
                </IonLabel>
              </IonItem>

              <IonItem>
                <IonLabel position="stacked">Name</IonLabel>
                <IonInput
                  type="text"
                  name="username"
                  value={profile.username}
                  onIonChange={(e) =>
                    setProfile({ ...profile, username: e.detail.value ?? '' })
                  }
                ></IonInput>
              </IonItem>

              <IonItem>
                <IonLabel position="stacked">Website</IonLabel>
                <IonInput
                  type="url"
                  name="website"
                  value={profile.website}
                  onIonChange={(e) =>
                    setProfile({ ...profile, website: e.detail.value ?? '' })
                  }
                ></IonInput>
              </IonItem>
              <div className="ion-text-center">
                <IonButton fill="clear" type="submit">
                  Update Profile
                </IonButton>
              </div>
            </form>

            <div className="ion-text-center">
              <IonButton fill="clear" onClick={signOut}>
                Log Out
              </IonButton>
            </div>
          </IonContent>
        </IonPage>
      );
    }
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `App.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.tsx" label="src/App.tsx">
    ```jsx name=src/App.tsx
    import { Redirect, Route } from 'react-router-dom'
    import { IonApp, IonRouterOutlet, setupIonicReact } from '@ionic/react'
    import { IonReactRouter } from '@ionic/react-router'
    import { supabase } from './supabaseClient'

    import '@ionic/react/css/ionic.bundle.css'

    /* Theme variables */
    import './theme/variables.css'
    import { LoginPage } from './pages/Login'
    import { AccountPage } from './pages/Account'
    import { useEffect, useState } from 'react'
    import { Session } from '@supabase/supabase-js'

    setupIonicReact()

    const App: React.FC = () => {
      const [session, setSession] = useState<Session | null>(null)
      useEffect(() => {
        const getSession = async () => {
          setSession(await supabase.auth.getSession().then((res) => res.data.session))
        }
        getSession()
        supabase.auth.onAuthStateChange((_event, session) => {
          setSession(session)
        })
      }, [])
      return (
        <IonApp>
          <IonReactRouter>
            <IonRouterOutlet>
              <Route
                exact
                path="/"
                render={() => {
                  return session ? <Redirect to="/account" /> : <LoginPage />
                }}
              />
              <Route exact path="/account">
                <AccountPage />
              </Route>
            </IonRouterOutlet>
          </IonReactRouter>
        </IonApp>
      )
    }

    export default App
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
ionic serve
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase Ionic React](/docs/img/ionic-demos/ionic-react.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

First install two packages in order to interact with the user's camera.

```bash
npm install @ionic/pwa-elements @capacitor/camera
```

[Capacitor](https://capacitorjs.com) is a cross platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.

Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.

With those packages installed we can update our `index.tsx` to include an additional bootstrapping call for the Ionic PWA Elements.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/index.tsx" label="src/index.tsx">
    ```ts name=src/index.tsx
    import React from 'react'
    import ReactDOM from 'react-dom'
    import App from './App'
    import * as serviceWorkerRegistration from './serviceWorkerRegistration'
    import reportWebVitals from './reportWebVitals'

    import { defineCustomElements } from '@ionic/pwa-elements/loader'
    defineCustomElements(window)

    ReactDOM.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>,
      document.getElementById('root')
    )

    serviceWorkerRegistration.unregister()
    reportWebVitals()
    ```
  </TabPanel>
</Tabs>

Then create an `AvatarComponent`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/Avatar.tsx" label="src/components/Avatar.tsx">
    ```jsx name=src/components/Avatar.tsx
    import { IonIcon } from '@ionic/react';
    import { person } from 'ionicons/icons';
    import { Camera, CameraResultType } from '@capacitor/camera';
    import { useEffect, useState } from 'react';
    import { supabase } from '../supabaseClient';
    import './Avatar.css'
    export function Avatar({
      url,
      onUpload,
    }: {
      url: string;
      onUpload: (e: any, file: string) => Promise<void>;
    }) {
      const [avatarUrl, setAvatarUrl] = useState<string | undefined>();

      useEffect(() => {
        if (url) {
          downloadImage(url);
        }
      }, [url]);
      const uploadAvatar = async () => {
        try {
          const photo = await Camera.getPhoto({
            resultType: CameraResultType.DataUrl,
          });

          const file = await fetch(photo.dataUrl!)
            .then((res) => res.blob())
            .then(
              (blob) =>
                new File([blob], 'my-file', { type: `image/${photo.format}` })
            );

          const fileName = `${Math.random()}-${new Date().getTime()}.${
            photo.format
          }`;
          const { error: uploadError } = await supabase.storage
            .from('avatars')
            .upload(fileName, file);
          if (uploadError) {
            throw uploadError;
          }
          onUpload(null, fileName);
        } catch (error) {
          console.log(error);
        }
      };

      const downloadImage = async (path: string) => {
        try {
          const { data, error } = await supabase.storage
            .from('avatars')
            .download(path);
          if (error) {
            throw error;
          }
          const url = URL.createObjectURL(data!);
          setAvatarUrl(url);
        } catch (error: any) {
          console.log('Error downloading image: ', error.message);
        }
      };

      return (
        <div className="avatar">
        <div className="avatar_wrapper" onClick={uploadAvatar}>
          {avatarUrl ? (
            <img src={avatarUrl} />
          ) : (
            <IonIcon icon={person} className="no-avatar" />
          )}
        </div>

        </div>
      );
    }
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/pages/Account.tsx" label="src/pages/Account.tsx">
    ```jsx name=src/pages/Account.tsx
    // Import the new component

    import { Avatar } from '../components/Avatar';

    // ...
    return (
      <IonPage>
        <IonHeader>
          <IonToolbar>
            <IonTitle>Account</IonTitle>
          </IonToolbar>
        </IonHeader>

        <IonContent>
          <Avatar url={profile.avatar_url} onUpload={updateProfile}></Avatar>
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



---
**Navigation:** [← Previous](./12-advanced-pgtap-testing.md) | [Index](./index.md) | [Next →](./14-build-a-user-management-app-with-ionic-vue.md)
