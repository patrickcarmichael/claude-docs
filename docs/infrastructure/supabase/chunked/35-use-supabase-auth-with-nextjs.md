**Navigation:** [← Previous](./34-implicit-flow.md) | [Index](./index.md) | [Next →](./36-error-codes.md)

# Use Supabase Auth with Next.js

Learn how to configure Supabase Auth for the Next.js App Router.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a new Supabase project">
      Head over to [database.new](https://database.new) and create a new Supabase project.

      Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql/new).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="SQL_EDITOR">
        ```sql name=SQL_EDITOR
         select * from auth.users;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Next.js app">
      Use the `create-next-app` command and the `with-supabase` template, to create a Next.js app pre-configured with:

      *   [Cookie-based Auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=package-manager\&package-manager=npm\&queryGroups=framework\&framework=nextjs\&queryGroups=environment\&environment=server)
      *   [TypeScript](https://www.typescriptlang.org/)
      *   [Tailwind CSS](https://tailwindcss.com/)

      [See GitHub repo](https://github.com/vercel/next.js/tree/canary/examples/with-supabase)
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx create-next-app -e with-supabase
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Rename `.env.example` to `.env.local` and populate with [your project's URL and Key](/dashboard/project/_/settings/api).

      {/* TODO: How to completely consolidate partials? */}

      <Admonition type="note" title="Changes to API keys">
        Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

        To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

        *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
        *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name=".env.local">
        ```text name=.env.local
        NEXT_PUBLIC_SUPABASE_URL=your-project-url
        NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon key
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Start the app">
      Start the development server, go to [http://localhost:3000](http://localhost:3000) in a browser, and you should see the contents of `app/page.tsx`.

      To sign up a new user, navigate to [http://localhost:3000/sign-up](http://localhost:3000/sign-up), and click `Sign up`. *NOTE: .env.example must be renamed to .env.local before this route becomes available*
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run dev
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Learn more

*   [Setting up Server-Side Auth for Next.js](/docs/guides/auth/server-side/nextjs) for a Next.js deep dive
*   [Supabase Auth docs](/docs/guides/auth#authentication) for more Supabase authentication methods



# Use Supabase Auth with React Native

Learn how to use Supabase Auth with React Native

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a new Supabase project">
      [Launch a new project](/dashboard) in the Supabase Dashboard.

      Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="SQL_EDITOR">
        ```sql name=SQL_EDITOR
         select * from auth.users;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a React app">
      Create a React app using the `create-expo-app` command.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx create-expo-app -t expo-template-blank-typescript my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      Install `supabase-js` and the required dependencies.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npx expo install @supabase/supabase-js @react-native-async-storage/async-storage @rneui/themed react-native-url-polyfill
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Set up your login component">
      Create a helper file `lib/supabase.ts` that exports a Supabase client using your Project URL and key.

      {/* TODO: How to completely consolidate partials? */}

      <Admonition type="note" title="Changes to API keys">
        Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

        To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

        *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
        *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="lib/supabase.ts">
        ```ts name=lib/supabase.ts
        import { AppState, Platform } from 'react-native'
        import 'react-native-url-polyfill/auto'
        import AsyncStorage from '@react-native-async-storage/async-storage'
        import { createClient, processLock } from '@supabase/supabase-js'

        const supabaseUrl = YOUR_REACT_NATIVE_SUPABASE_URL
        const supabaseAnonKey = YOUR_REACT_NATIVE_SUPABASE_PUBLISHABLE_KEY

        export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
          auth: {
            ...(Platform.OS !== "web" ? { storage: AsyncStorage } : {}),
            autoRefreshToken: true,
            persistSession: true,
            detectSessionInUrl: false,
            lock: processLock,
          },
        })

        // Tells Supabase Auth to continuously refresh the session automatically
        // if the app is in the foreground. When this is added, you will continue
        // to receive `onAuthStateChange` events with the `TOKEN_REFRESHED` or
        // `SIGNED_OUT` event if the user's session is terminated. This should
        // only be registered once.
        if (Platform.OS !== "web") {
          AppState.addEventListener('change', (state) => {
            if (state === 'active') {
              supabase.auth.startAutoRefresh()
            } else {
              supabase.auth.stopAutoRefresh()
            }
          })
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create a login component">
      Let's set up a React Native component to manage logins and sign ups.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="components/Auth.tsx">
        ```tsx name=components/Auth.tsx
        import React, { useState } from 'react'
        import { Alert, StyleSheet, View } from 'react-native'
        import { supabase } from '../lib/supabase'
        import { Button, Input } from '@rneui/themed'

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
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Add the Auth component to your app">
      Add the `Auth` component to your `App.tsx` file. If the user is logged in, print the user id to the screen.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="App.tsx">
        ```tsx name=App.tsx
        import 'react-native-url-polyfill/auto'
        import { useState, useEffect } from 'react'
        import { supabase } from './lib/supabase'
        import Auth from './components/Auth'
        import { View, Text } from 'react-native'
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
              <Auth />
              {session && session.user && <Text>{session.user.id}</Text>}
            </View>
          )
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Start the app">
      Start the app, and follow the instructions in the terminal.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm start
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase Auth with React

Learn how to use Supabase Auth with React.js.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a new Supabase project">
      [Launch a new project](/dashboard) in the Supabase Dashboard.

      Your new database has a table for storing your users. You can see that this table is currently empty by running some SQL in the [SQL Editor](/dashboard/project/_/sql).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="SQL_EDITOR">
        ```sql name=SQL_EDITOR
         select * from auth.users;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a React app">
      Create a React app using [Vite](https://vitejs.dev/).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm create vite@latest my-app -- --template react
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use Supabase's `auth-ui-react` library which provides a convenient interface for working with Supabase Auth from a React app.

      Navigate to the React app and install the Supabase libraries.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js @supabase/auth-ui-react @supabase/auth-ui-shared
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Set up your login component">
      In `App.jsx`, create a Supabase client using your Project URL and key.

      {/* TODO: How to completely consolidate partials? */}

      <Admonition type="note" title="Changes to API keys">
        Supabase is changing the way keys work to improve project security and developer experience. You can [read the full announcement](https://github.com/orgs/supabase/discussions/29260), but in the transition period, you can use both the current `anon` and `service_role` keys and the new publishable key with the form `sb_publishable_xxx` which will replace the older keys.

        To get the key values, open [the API Keys section of a project's Settings page](/dashboard/project/_/settings/api-keys/) and do the following:

        *   **For legacy keys**, copy the `anon` key for client-side operations and the `service_role` key for server-side operations from the **Legacy API Keys** tab.
        *   **For new keys**, open the **API Keys** tab, if you don't have a publishable key already, click **Create new API Keys**, and copy the value from the **Publishable key** section.
      </Admonition>

      You can configure the Auth component to display whenever there is no session inside `supabase.auth.getSession()`
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/App.jsx">
        ```jsx name=src/App.jsx
          import './index.css'
          import { useState, useEffect } from 'react'
          import { createClient } from '@supabase/supabase-js'
          import { Auth } from '@supabase/auth-ui-react'
          import { ThemeSupa } from '@supabase/auth-ui-shared'

          const supabase = createClient('https://<project>.supabase.co', '<sb_publishable_... or anon key>')

          export default function App() {
            const [session, setSession] = useState(null)

            useEffect(() => {
              supabase.auth.getSession().then(({ data: { session } }) => {
                setSession(session)
              })

              const {
                data: { subscription },
              } = supabase.auth.onAuthStateChange((_event, session) => {
                setSession(session)
              })

              return () => subscription.unsubscribe()
            }, [])

            if (!session) {
              return (<Auth supabaseClient={supabase} appearance={{ theme: ThemeSupa }} />)
            }
            else {
              return (<div>Logged in!</div>)
            }
          }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Start the app">
      Start the app, go to [http://localhost:3000](http://localhost:3000) in a browser, and open the browser console and you should be able to log in.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run dev
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Build a Social Auth App with Expo React Native



This tutorial demonstrates how to build a React Native app with [Expo](https://expo.dev) that implements social authentication. The app showcases a complete authentication flow with protected navigation using:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data with [Row Level Security](/docs/guides/auth#row-level-security) to ensure data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - enables users to log in through social authentication providers (Apple and Google).

![Supabase Social Auth example](/docs/img/supabase-expo-social-auth-login.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/auth/expo-social-auth).
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

Start by building the React Native app from scratch.


### Initialize a React Native app

Use [Expo](https://docs.expo.dev/get-started/create-a-project/) to initialize an app called `expo-social-auth` with the [standard template](https://docs.expo.dev/more/create-expo/#--template):

```bash
npx create-expo-app@latest

cd expo-social-auth
```

Install the additional dependencies:

*   [supabase-js](https://github.com/supabase/supabase-js)
*   [@react-native-async-storage/async-storage](https://github.com/react-native-async-storage/async-storage) - A key-value store for React Native.
*   [expo-secure-store](https://docs.expo.dev/versions/latest/sdk/securestore/) - Provides a way to securely store key-value pairs locally on the device.
*   [expo-splash-screen](https://docs.expo.dev/versions/latest/sdk/splash-screen/) - Provides a way to programmatically manage the splash screen.

```bash
npx expo install @supabase/supabase-js @react-native-async-storage/async-storage expo-secure-store expo-splash-screen
```

Now, create a helper file to initialize the Supabase client for both web and React Native platforms using platform-specific [storage adapters](https://docs.expo.dev/develop/user-interface/store-data/): [Expo SecureStore](https://docs.expo.dev/develop/user-interface/store-data/#secure-storage) for mobile and [AsyncStorage](https://docs.expo.dev/develop/user-interface/store-data/#async-storage) for web.

<Tabs scrollable size="large" type="underlined" defaultActiveId="async-storage" queryGroup="auth-store">
  <TabPanel id="async-storage" label="AsyncStorage">
    {/* TODO: Future task to extract to repo and transclude */}

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="lib/supabase.web.ts" label="lib/supabase.web.ts">
        ```ts name=lib/supabase.web.ts
        import AsyncStorage from '@react-native-async-storage/async-storage';
        import { createClient } from '@supabase/supabase-js';
        import 'react-native-url-polyfill/auto';

        const ExpoWebSecureStoreAdapter = {
          getItem: (key: string) => {
            console.debug("getItem", { key })
            return AsyncStorage.getItem(key)
          },
          setItem: (key: string, value: string) => {
            return AsyncStorage.setItem(key, value)
          },
          removeItem: (key: string) => {
            return AsyncStorage.removeItem(key)
          },
        };

        export const supabase = createClient(
          process.env.EXPO_PUBLIC_SUPABASE_URL ?? '',
          process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY ?? '',
          {
            auth: {
              storage: ExpoWebSecureStoreAdapter,
              autoRefreshToken: true,
              persistSession: true,
              detectSessionInUrl: false,
            },
          },
        );
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="secure-store" label="SecureStore">
    If you want to encrypt the user's session information, use `aes-js` and store the encryption key in [Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore). The [`aes-js` library](https://github.com/ricmoo/aes-js) is a reputable JavaScript-only implementation of the AES encryption algorithm in CTR mode. A new 256-bit encryption key is generated using the `react-native-get-random-values` library. This key is stored inside Expo's SecureStore, while the value is encrypted and placed inside AsyncStorage.

    Make sure that:

    *   You keep the `expo-secure-storage`, `aes-js` and `react-native-get-random-values` libraries up-to-date.
    *   Choose the correct [`SecureStoreOptions`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestoreoptions) for your app's needs. E.g. [`SecureStore.WHEN_UNLOCKED`](https://docs.expo.dev/versions/latest/sdk/securestore/#securestorewhen_unlocked) regulates when the data can be accessed.
    *   Carefully consider optimizations or other modifications to the above example, as those can lead to introducing subtle security vulnerabilities.

    Implement a `ExpoSecureStoreAdapter` to pass in as Auth storage adapter for the `supabase-js` client:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="lib/supabase.ts" label="lib/supabase.ts">
        ```ts name=lib/supabase.ts
        import { createClient } from '@supabase/supabase-js';
        import { deleteItemAsync, getItemAsync, setItemAsync } from 'expo-secure-store';

        const ExpoSecureStoreAdapter = {
          getItem: (key: string) => {
            console.debug("getItem", { key, getItemAsync })
            return getItemAsync(key)
          },
          setItem: (key: string, value: string) => {
            if (value.length > 2048) {
              console.warn('Value being stored in SecureStore is larger than 2048 bytes and it may not be stored successfully. In a future SDK version, this call may throw an error.')
            }
            return setItemAsync(key, value)
          },
          removeItem: (key: string) => {
            return deleteItemAsync(key)
          },
        };

        export const supabase = createClient(
          process.env.EXPO_PUBLIC_SUPABASE_URL ?? '',
          process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY ?? '',
          {
            auth: {
              storage: ExpoSecureStoreAdapter as any,
              autoRefreshToken: true,
              persistSession: true,
              detectSessionInUrl: false,
            },
          },
        );
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Set up environment variables

You need the API URL and the `anon` key copied [earlier](#get-the-api-keys).
These variables are safe to expose in your Expo app since Supabase has [Row Level Security](/docs/guides/database/postgres/row-level-security) enabled on your database.

Create a `.env` file containing these variables:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    EXPO_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL
    EXPO_PUBLIC_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
    ```
  </TabPanel>
</Tabs>


### Set up protected navigation

Next, you need to protect app navigation to prevent unauthenticated users from accessing protected routes. Use the [Expo `SplashScreen`](https://docs.expo.dev/versions/latest/sdk/splash-screen/) to display a loading screen while fetching the user profile and verifying authentication status.


#### Create the `AuthContext`

Create [a React context](https://react.dev/learn/passing-data-deeply-with-context) to manage the authentication session, making it accessible from any component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="hooks/use-auth-context.tsx" label="hooks/use-auth-context.tsx">
    ```tsx name=hooks/use-auth-context.tsx
    import { Session } from '@supabase/supabase-js'
    import { createContext, useContext } from 'react'

    export type AuthData = {
      session?: Session | null
      profile?: any | null
      isLoading: boolean
      isLoggedIn: boolean
    }

    export const AuthContext = createContext<AuthData>({
      session: undefined,
      profile: undefined,
      isLoading: true,
      isLoggedIn: false,
    })

    export const useAuthContext = () => useContext(AuthContext)
    ```
  </TabPanel>
</Tabs>


#### Create the `AuthProvider`

Next, create a provider component to manage the authentication session throughout the app:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="providers/auth-provider.tsx" label="providers/auth-provider.tsx">
    ```tsx name=providers/auth-provider.tsx
    import { AuthContext } from '@/hooks/use-auth-context'
    import { supabase } from '@/lib/supabase'
    import type { Session } from '@supabase/supabase-js'
    import { PropsWithChildren, useEffect, useState } from 'react'

    export default function AuthProvider({ children }: PropsWithChildren) {
      const [session, setSession] = useState<Session | undefined | null>()
      const [profile, setProfile] = useState<any>()
      const [isLoading, setIsLoading] = useState<boolean>(true)

      // Fetch the session once, and subscribe to auth state changes
      useEffect(() => {
        const fetchSession = async () => {
          setIsLoading(true)

          const {
            data: { session },
            error,
          } = await supabase.auth.getSession()

          if (error) {
            console.error('Error fetching session:', error)
          }

          setSession(session)
          setIsLoading(false)
        }

        fetchSession()

        const {
          data: { subscription },
        } = supabase.auth.onAuthStateChange((_event, session) => {
          console.log('Auth state changed:', { event: _event, session })
          setSession(session)
        })

        // Cleanup subscription on unmount
        return () => {
          subscription.unsubscribe()
        }
      }, [])

      // Fetch the profile when the session changes
      useEffect(() => {
        const fetchProfile = async () => {
          setIsLoading(true)

          if (session) {
            const { data } = await supabase
              .from('profiles')
              .select('*')
              .eq('id', session.user.id)
              .single()

            setProfile(data)
          } else {
            setProfile(null)
          }

          setIsLoading(false)
        }

        fetchProfile()
      }, [session])

      return (
        <AuthContext.Provider
          value={{
            session,
            isLoading,
            profile,
            isLoggedIn: session != undefined,
          }}
        >
          {children}
        </AuthContext.Provider>
      )
    }
    ```
  </TabPanel>
</Tabs>


#### Create the `SplashScreenController`

Create a `SplashScreenController` component to display the [Expo `SplashScreen`](https://docs.expo.dev/versions/latest/sdk/splash-screen/) while the authentication session is loading:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/splash-screen-controller.tsx" label="components/splash-screen-controller.tsx">
    ```tsx name=components/splash-screen-controller.tsx
    import { useAuthContext } from '@/hooks/use-auth-context'
    import { SplashScreen } from 'expo-router'

    SplashScreen.preventAutoHideAsync()

    export function SplashScreenController() {
      const { isLoading } = useAuthContext()

      if (!isLoading) {
        SplashScreen.hideAsync()
      }

      return null
    }
    ```
  </TabPanel>
</Tabs>


### Create a logout component

Create a logout button component to handle user sign-out:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/social-auth-buttons/sign-out-button.tsx" label="components/social-auth-buttons/sign-out-button.tsx">
    ```tsx name=components/social-auth-buttons/sign-out-button.tsx
    import { supabase } from '@/lib/supabase'
    import React from 'react'
    import { Button } from 'react-native'

    async function onSignOutButtonPress() {
      const { error } = await supabase.auth.signOut()

      if (error) {
        console.error('Error signing out:', error)
      }
    }

    export default function SignOutButton() {
      return <Button title="Sign out" onPress={onSignOutButtonPress} />
    }
    ```
  </TabPanel>
</Tabs>

And add it to the `app/(tabs)/index.tsx` file used to display the user profile data and the logout button:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app/(tabs)/index.tsx" label="app/(tabs)/index.tsx">
    ```tsx name=app/(tabs)/index.tsx
    import { Image } from 'expo-image'
    import { StyleSheet } from 'react-native'

    import { HelloWave } from '@/components/hello-wave'
    import ParallaxScrollView from '@/components/parallax-scroll-view'
    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'
    import SignOutButton from '@/components/social-auth-buttons/sign-out-button'
    import { useAuthContext } from '@/hooks/use-auth-context'

    export default function HomeScreen() {
      const { profile } = useAuthContext()

      return (
        <ParallaxScrollView
          headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
          headerImage={
            <Image
              source={require('@/assets/images/partial-react-logo.png')}
              style={styles.reactLogo}
            />
          }
        >
          <ThemedView style={styles.titleContainer}>
            <ThemedText type="title">Welcome!</ThemedText>
            <HelloWave />
          </ThemedView>
          <ThemedView style={styles.stepContainer}>
            <ThemedText type="subtitle">Username</ThemedText>
            <ThemedText>{profile?.username}</ThemedText>
            <ThemedText type="subtitle">Full name</ThemedText>
            <ThemedText>{profile?.full_name}</ThemedText>
          </ThemedView>
          <SignOutButton />
        </ParallaxScrollView>
      )
    }

    const styles = StyleSheet.create({
      titleContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        gap: 8,
      },
      stepContainer: {
        gap: 8,
        marginBottom: 8,
      },
      reactLogo: {
        height: 178,
        width: 290,
        bottom: 0,
        left: 0,
        position: 'absolute',
      },
    })
    ```
  </TabPanel>
</Tabs>


### Create a login screen

Next, create a basic login screen component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app/login.tsx" label="app/login.tsx">
    ```tsx name=app/login.tsx
    import { Link, Stack } from 'expo-router'
    import { StyleSheet } from 'react-native'

    import { ThemedText } from '@/components/themed-text'
    import { ThemedView } from '@/components/themed-view'

    export default function LoginScreen() {
      return (
        <>
          <Stack.Screen options={{ title: 'Login' }} />
          <ThemedView style={styles.container}>
            <ThemedText type="title">Login</ThemedText>
            <Link href="/" style={styles.link}>
              <ThemedText type="link">Try to navigate to home screen!</ThemedText>
            </Link>
          </ThemedView>
        </>
      )
    }

    const styles = StyleSheet.create({
      container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        padding: 20,
      },
      link: {
        marginTop: 15,
        paddingVertical: 15,
      },
    })
    ```
  </TabPanel>
</Tabs>


#### Implement protected routes

Wrap the navigation with the `AuthProvider` and `SplashScreenController`.

Using [Expo Router's protected routes](https://docs.expo.dev/router/advanced/authentication/#using-protected-routes), you can secure navigation:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app/_layout.tsx" label="app/_layout.tsx">
    ```tsx name=app/_layout.tsx
    import { DarkTheme, DefaultTheme, ThemeProvider } from '@react-navigation/native'
    import { useFonts } from 'expo-font'
    import { Stack } from 'expo-router'
    import { StatusBar } from 'expo-status-bar'
    import 'react-native-reanimated'

    import { SplashScreenController } from '@/components/splash-screen-controller'

    import { useAuthContext } from '@/hooks/use-auth-context'
    import { useColorScheme } from '@/hooks/use-color-scheme'
    import AuthProvider from '@/providers/auth-provider'

    // Separate RootNavigator so we can access the AuthContext
    function RootNavigator() {
      const { isLoggedIn } = useAuthContext()

      return (
        <Stack>
          <Stack.Protected guard={isLoggedIn}>
            <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
          </Stack.Protected>
          <Stack.Protected guard={!isLoggedIn}>
            <Stack.Screen name="login" options={{ headerShown: false }} />
          </Stack.Protected>
          <Stack.Screen name="+not-found" />
        </Stack>
      )
    }

    export default function RootLayout() {
      const colorScheme = useColorScheme()

      const [loaded] = useFonts({
        SpaceMono: require('../assets/fonts/SpaceMono-Regular.ttf'),
      })

      if (!loaded) {
        // Async font loading only occurs in development.
        return null
      }

      return (
        <ThemeProvider value={colorScheme === 'dark' ? DarkTheme : DefaultTheme}>
          <AuthProvider>
            <SplashScreenController />
            <RootNavigator />
            <StatusBar style="auto" />
          </AuthProvider>
        </ThemeProvider>
      )
    }
    ```
  </TabPanel>
</Tabs>

You can now test the app by running:

```bash
npx expo prebuild
npx expo start --clear
```

Verify that the app works as expected. The splash screen displays while fetching the user profile, and the login page appears even when attempting to navigate to the home screen using the `Link` button.

<Admonition type="note">
  By default Supabase Auth requires email verification before a session is created for the user. To support email verification you need to [implement deep link handling](/docs/guides/auth/native-mobile-deep-linking?platform=react-native)!

  While testing, you can disable email confirmation in your [project's email auth provider settings](/dashboard/project/_/auth/providers).
</Admonition>



## Integrate social authentication

Now integrate social authentication with Supabase Auth, starting with Apple authentication.
If you only need to implement Google authentication, you can skip to the [Google authentication](#google-authentication) section.


### Apple authentication

Start by adding the button inside the login screen:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app/login.tsx" label="app/login.tsx">
    ```tsx name=app/login.tsx
    ...
    import AppleSignInButton from '@/components/social-auth-buttons/apple/apple-sign-in-button';
    ...
    export default function LoginScreen() {
      return (
        <>
          <Stack.Screen options={{ title: 'Login' }} />
          <ThemedView style={styles.container}>
            ...
            <AppleSignInButton />
            ...
          </ThemedView>
        </>
      );
    }
    ...
    ```
  </TabPanel>
</Tabs>

For Apple authentication, you can choose between:

*   [Invertase's React Native Apple Authentication library](https://github.com/invertase/react-native-apple-authentication) - that supports iOS, Android
*   [react-apple-signin-auth](https://react-apple-signin-auth.ahmedtokyo.com/) - that supports Web, also suggested by Invertase
*   [Expo's AppleAuthentication library](https://docs.expo.dev/versions/latest/sdk/apple-authentication/) - that supports iOS only

For either option, you need to obtain a Service ID from the [Apple Developer Console](/docs/guides/auth/social-login/auth-apple?queryGroups=framework\&framework=nextjs\&queryGroups=platform\&platform=web#configuration-web).

<Admonition type="note">
  To enable Apple sign-up on Android and Web, you also need to register the tunnelled URL (e.g., `https://arnrer1-anonymous-8081.exp.direct`) obtained by running:

  ```bash
  npx expo start --tunnel
  ```

  And add it to the **Redirect URLs** field in [your Supabase dashboard Authentication configuration](/dashboard/project/_/auth/url-configuration).

  For more information, follow the [Supabase Login with Apple](docs/guides/auth/social-login/auth-apple) guide.
</Admonition>

<Tabs scrollable size="large" type="underlined" defaultActiveId="invertase-react-native-apple-authentication" queryGroup="apple-authentication">
  <TabPanel id="invertase-react-native-apple-authentication" label="Invertase">
    #### Prerequisites

    Before proceeding, ensure you have followed the Invertase prerequisites documented in the [Invertase Initial Setup Guide](https://github.com/invertase/react-native-apple-authentication/blob/main/docs/INITIAL_SETUP.md) and the [Invertase Android Setup Guide](https://github.com/invertase/react-native-apple-authentication/blob/main/docs/ANDROID_EXTRA.md).

    You need to add two new environment variables to the `.env` file:

    ```bash
    EXPO_PUBLIC_APPLE_AUTH_SERVICE_ID="YOUR_APPLE_AUTH_SERVICE_ID"
    EXPO_PUBLIC_APPLE_AUTH_REDIRECT_URI="YOUR_APPLE_AUTH_REDIRECT_URI"
    ```

    #### iOS

    Install the `@invertase/react-native-apple-authentication` library:

    ```bash
    npx expo install @invertase/react-native-apple-authentication
    ```

    Then create the iOS specific button component `AppleSignInButton`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx" label="components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx">
        ```tsx name=components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx
        import { supabase } from '@/lib/supabase';
        import { AppleButton, appleAuth } from '@invertase/react-native-apple-authentication';
        import type { SignInWithIdTokenCredentials } from '@supabase/supabase-js';
        import { router } from 'expo-router';
        import { Platform } from 'react-native';

        async function onAppleButtonPress() {
          // Performs login request
          const appleAuthRequestResponse = await appleAuth.performRequest({
            requestedOperation: appleAuth.Operation.LOGIN,
            // Note: it appears putting FULL_NAME first is important, see issue #293
            requestedScopes: [appleAuth.Scope.FULL_NAME, appleAuth.Scope.EMAIL],
          });

          // Get the current authentication state for user
          // Note: This method must be tested on a real device. On the iOS simulator it always throws an error.
          const credentialState = await appleAuth.getCredentialStateForUser(appleAuthRequestResponse.user);

          console.log('Apple sign in successful:', { credentialState, appleAuthRequestResponse });

          if (credentialState === appleAuth.State.AUTHORIZED && appleAuthRequestResponse.identityToken && appleAuthRequestResponse.authorizationCode) {
            const signInWithIdTokenCredentials: SignInWithIdTokenCredentials = {
              provider: 'apple',
              token: appleAuthRequestResponse.identityToken,
              nonce: appleAuthRequestResponse.nonce,
              access_token: appleAuthRequestResponse.authorizationCode,
            };

            const { data, error } = await supabase.auth.signInWithIdToken(signInWithIdTokenCredentials);

            if (error) {
              console.error('Error signing in with Apple:', error);
            }

            if (data) {
              console.log('Apple sign in successful:', data);
              router.navigate('/(tabs)/explore');
            }
          }
        }

        export default function AppleSignInButton() {
          if (Platform.OS !== 'ios') { return <></>; }

          return <AppleButton
            buttonStyle={AppleButton.Style.BLACK}
            buttonType={AppleButton.Type.SIGN_IN}
            style={{ width: 160, height: 45 }}
            onPress={() => onAppleButtonPress()}
          />;
        }
        ```
      </TabPanel>
    </Tabs>

    <Admonition type="note">
      To test functionality on the simulator, remove the `getCredentialStateForUser` check:

      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx" label="components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx">
          ```tsx name=components/social-auth-buttons/apple/apple-sign-in-button.ios.tsx
          ...
          const credentialState = await appleAuth.getCredentialStateForUser(appleAuthRequestResponse.user);
          ...
          ```
        </TabPanel>
      </Tabs>
    </Admonition>

    Enable the Apple authentication capability in iOS:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app.json" label="app.json">
        ```json name=app.json
        {
          "expo": {
            ...
            "ios": {
              ...
              "usesAppleSignIn": true
              ...
            },
            ...
          }
        }
        ```
      </TabPanel>
    </Tabs>

    Add the capabilities to the `Info.plist` file by following the [Expo documentation](https://docs.expo.dev/build-reference/ios-capabilities/#xcode).

    <Admonition type="note">
      Before testing the app, if you've already built the iOS app, clean the project artifacts:

      ```bash
      npx react-native-clean-project clean-project-auto
      ```

      If issues persist, try completely cleaning the cache, as reported by many users in this [closed issue](https://github.com/invertase/react-native-apple-authentication/issues/23).
    </Admonition>

    Finally, update the iOS project by installing the Pod library and running the Expo prebuild command:

    ```bash
    cd ios
    pod install
    cd ..
    npx expo prebuild
    ```

    Now test the application on a physical device:

    ```bash
    npx expo run:ios --no-build-cache --device
    ```

    You should see the login screen with the Apple authentication button.

    <Admonition type="note">
      If you get stuck while working through this guide, refer to the [full Invertase example on GitHub](https://github.com/invertase/react-native-apple-authentication?tab=readme-ov-file#react-native-apple-authentication).
    </Admonition>

    #### Android

    Install the required libraries:

    ```bash
    npx expo install @invertase/react-native-apple-authentication react-native-get-random-values uuid
    ```

    Next, create the Android-specific `AppleSignInButton` component:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/apple/apple-sign-in-button.android.tsx" label="components/social-auth-buttons/apple/apple-sign-in-button.android.tsx">
        ```tsx name=components/social-auth-buttons/apple/apple-sign-in-button.android.tsx
        import { supabase } from '@/lib/supabase';
        import { appleAuthAndroid, AppleButton } from '@invertase/react-native-apple-authentication';
        import { SignInWithIdTokenCredentials } from '@supabase/supabase-js';
        import { Platform } from 'react-native';
        import 'react-native-get-random-values';
        import { v4 as uuid } from 'uuid';

        async function onAppleButtonPress() {
          // Generate secure, random values for state and nonce
          const rawNonce = uuid();
          const state = uuid();

          // Configure the request
          appleAuthAndroid.configure({
            // The Service ID you registered with Apple
            clientId: process.env.EXPO_PUBLIC_APPLE_AUTH_SERVICE_ID ?? '',

            // Return URL added to your Apple dev console. We intercept this redirect, but it must still match
            // the URL you provided to Apple. It can be an empty route on your backend as it's never called.
            redirectUri: process.env.EXPO_PUBLIC_APPLE_AUTH_REDIRECT_URI ?? '',

            // The type of response requested - code, id_token, or both.
            responseType: appleAuthAndroid.ResponseType.ALL,

            // The amount of user information requested from Apple.
            scope: appleAuthAndroid.Scope.ALL,

            // Random nonce value that will be SHA256 hashed before sending to Apple.
            nonce: rawNonce,

            // Unique state value used to prevent CSRF attacks. A UUID will be generated if nothing is provided.
            state,
          });

          // Open the browser window for user sign in
          const credentialState = await appleAuthAndroid.signIn();
          console.log('Apple sign in successful:', credentialState);

          if (credentialState.id_token && credentialState.code && credentialState.nonce) {
            const signInWithIdTokenCredentials: SignInWithIdTokenCredentials = {
              provider: 'apple',
              token: credentialState.id_token,
              nonce: credentialState.nonce,
              access_token: credentialState.code,
            };

            const { data, error } = await supabase.auth.signInWithIdToken(signInWithIdTokenCredentials);

            if (error) {
              console.error('Error signing in with Apple:', error);
            }

            if (data) {
              console.log('Apple sign in successful:', data);
            }
          }
        }

        export default function AppleSignInButton() {
          if (Platform.OS !== 'android' || appleAuthAndroid.isSupported !== true) { return <></> }

          return <AppleButton
            buttonStyle={AppleButton.Style.BLACK}
            buttonType={AppleButton.Type.SIGN_IN}
            onPress={() => onAppleButtonPress()}
          />;
        }
        ```
      </TabPanel>
    </Tabs>

    You should now be able to test the authentication by running it on a physical device or simulator:

    ```bash
    npx expo run:android --no-build-cache
    ```
  </TabPanel>

  <TabPanel id="react-apple-signin-auth" label="Web">
    #### Prerequisites

    Before proceeding, as per the mobile options you need an Apple Service ID. To obtain it you can follow the [Invertase Initial Setup Guide](https://github.com/invertase/react-native-apple-authentication/blob/main/docs/INITIAL_SETUP.md) and the [Invertase Android Setup Guide](https://github.com/invertase/react-native-apple-authentication/blob/main/docs/ANDROID_EXTRA.md) mentioned in the Invertase tab.

    You also need to add two new environment variables to the `.env` file:

    ```bash
    EXPO_PUBLIC_APPLE_AUTH_SERVICE_ID="YOUR_APPLE_AUTH_SERVICE_ID"
    EXPO_PUBLIC_APPLE_AUTH_REDIRECT_URI="YOUR_APPLE_AUTH_REDIRECT_URI"
    ```

    #### Web

    Install the required libraries:

    ```bash
    npx expo install react-apple-signin-auth
    ```

    Next, create the Web-specific `AppleSignInButton` component:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/apple/apple-sign-in-button.web.tsx" label="components/social-auth-buttons/apple/apple-sign-in-button.web.tsx">
        ```tsx name=components/social-auth-buttons/apple/apple-sign-in-button.web.tsx
        import { supabase } from '@/lib/supabase';
        import type { SignInWithIdTokenCredentials } from '@supabase/supabase-js';
        import { useEffect, useState } from 'react';
        import AppleSignin, { type AppleAuthResponse } from 'react-apple-signin-auth';
        import { Platform } from 'react-native';

        export default function AppleSignInButton() {
          const [nonce, setNonce] = useState('');
          const [sha256Nonce, setSha256Nonce] = useState('');

          async function onAppleButtonSuccess(appleAuthRequestResponse: AppleAuthResponse) {
            console.debug('Apple sign in successful:', { appleAuthRequestResponse });
            if (appleAuthRequestResponse.authorization && appleAuthRequestResponse.authorization.id_token && appleAuthRequestResponse.authorization.code) {
              const signInWithIdTokenCredentials: SignInWithIdTokenCredentials = {
                provider: 'apple',
                token: appleAuthRequestResponse.authorization.id_token,
                nonce,
                access_token: appleAuthRequestResponse.authorization.code,
              };

              const { data, error } = await supabase.auth.signInWithIdToken(signInWithIdTokenCredentials)

              if (error) {
                console.error('Error signing in with Apple:', error);
              }

              if (data) {
                console.log('Apple sign in successful:', data);
              }
            };
          }

          useEffect(() => {
            function generateNonce(): string {
              const array = new Uint32Array(1);
              window.crypto.getRandomValues(array);
              return array[0].toString();
            };

            async function generateSha256Nonce(nonce: string): Promise<string> {
              const buffer = await window.crypto.subtle.digest('sha-256', new TextEncoder().encode(nonce));
              const array = Array.from(new Uint8Array(buffer));
              return array.map(b => b.toString(16).padStart(2, '0')).join('');
            }

            let nonce = generateNonce();
            setNonce(nonce);

            generateSha256Nonce(nonce)
              .then((sha256Nonce) => { setSha256Nonce(sha256Nonce) });
          }, []);

          if (Platform.OS !== 'web') { return <></>; }

          return <AppleSignin
            authOptions={{
              clientId: process.env.EXPO_PUBLIC_APPLE_AUTH_SERVICE_ID ?? '',
              redirectURI: process.env.EXPO_PUBLIC_APPLE_AUTH_REDIRECT_URI ?? '',
              scope: 'email name',
              state: 'state',
              nonce: sha256Nonce,
              usePopup: true,
            }}
            onSuccess={onAppleButtonSuccess}
          />;
        }
        ```
      </TabPanel>
    </Tabs>

    Test the authentication in your browser using the tunneled HTTPS URL:

    ```bash
    npx expo start --tunnel
    ```
  </TabPanel>

  <TabPanel id="expo-apple-authentication" label="Expo">
    #### Prerequisites

    Before proceeding, ensure you have followed the Expo prerequisites documented in the [Expo Setup Guide](https://docs.expo.dev/versions/latest/sdk/apple-authentication/).

    #### iOS

    Install the `expo-apple-authentication` library:

    ```bash
    npx expo install expo-apple-authentication
    ```

    Enable the Apple authentication capability in iOS and the plugin in `app.json`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app.json" label="app.json">
        ```json name=app.json
        {
          "expo": {
            ...
            "ios": {
              ...
              "usesAppleSignIn": true
              ...
            },
            "plugins": ["expo-apple-authentication"]
            ...
          }
        }
        ```
      </TabPanel>
    </Tabs>

    Then create the iOS specific button component `AppleSignInButton`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/apple/apple-sign-in-button.tsx" label="components/social-auth-buttons/apple/apple-sign-in-button.tsx">
        ```tsx name=components/social-auth-buttons/apple/apple-sign-in-button.tsx
        import { supabase } from '@/lib/supabase';
        import { AppleButton, appleAuth } from '@invertase/react-native-apple-authentication';
        import type { SignInWithIdTokenCredentials } from '@supabase/supabase-js';
        import { router } from 'expo-router';
        import { Platform } from 'react-native';

        async function onAppleButtonPress() {
          // Performs login request
          const appleAuthRequestResponse = await appleAuth.performRequest({
            requestedOperation: appleAuth.Operation.LOGIN,
            // Note: it appears putting FULL_NAME first is important, see issue #293
            requestedScopes: [appleAuth.Scope.FULL_NAME, appleAuth.Scope.EMAIL],
          });

          // Get the current authentication state for user
          // Note: This method must be tested on a real device. On the iOS simulator it always throws an error.
          const credentialState = await appleAuth.getCredentialStateForUser(appleAuthRequestResponse.user);

          console.log('Apple sign in successful:', { credentialState, appleAuthRequestResponse });

          if (credentialState === appleAuth.State.AUTHORIZED && appleAuthRequestResponse.identityToken && appleAuthRequestResponse.authorizationCode) {
            const signInWithIdTokenCredentials: SignInWithIdTokenCredentials = {
              provider: 'apple',
              token: appleAuthRequestResponse.identityToken,
              nonce: appleAuthRequestResponse.nonce,
              access_token: appleAuthRequestResponse.authorizationCode,
            };

            const { data, error } = await supabase.auth.signInWithIdToken(signInWithIdTokenCredentials);

            if (error) {
              console.error('Error signing in with Apple:', error);
            }

            if (data) {
              console.log('Apple sign in successful:', data);
              router.navigate('/(tabs)/explore');
            }
          }
        }

        export default function AppleSignInButton() {
          if (Platform.OS !== 'ios') { return <></>; }

          return <AppleButton
            buttonStyle={AppleButton.Style.BLACK}
            buttonType={AppleButton.Type.SIGN_IN}
            style={{ width: 160, height: 45 }}
            onPress={() => onAppleButtonPress()}
          />;
        }
        ```
      </TabPanel>
    </Tabs>

    <Admonition type="note">
      The Expo Apple Sign In button does not support the Simulator, so you need to test it on a physical device.
    </Admonition>
  </TabPanel>
</Tabs>


### Google authentication

Start by adding the button to the login screen:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app/login.tsx" label="app/login.tsx">
    ```tsx name=app/login.tsx
    ...
    import GoogleSignInButton from '@/components/social-auth-buttons/google/google-sign-in-button';
    ...
    export default function LoginScreen() {
      return (
        <>
          <Stack.Screen options={{ title: 'Login' }} />
          <ThemedView style={styles.container}>
            ...
            <GoogleSignInButton />
            ...
          </ThemedView>
        </>
      );
    }
    ...
    ```
  </TabPanel>
</Tabs>

For Google authentication, you can choose between the following options:

*   [GN Google Sign In Premium](https://react-native-google-signin.github.io/docs/install#sponsor-only-version) - that supports iOS, Android, and Web by using the latest Google's One Tap sign-in (but [it requires a subscription](https://universal-sign-in.com/))
*   [@react-oauth/google](https://github.com/MomenSherif/react-oauth#googlelogin) - that supports Web (so it's not a good option for mobile, but it works)
*   Relying on the [\`\`signInWithOAuth](/docs/reference/javascript/auth-signinwithoauth) function of the Supabase Auth - that also supports iOS, Android and Web (useful also to manage any other OAuth provider)

<Admonition type="note">
  The [GN Google Sign In Free](https://react-native-google-signin.github.io/docs/install#public-version-free) doesn't support iOS or Android, as [it doesn't allow to pass a custom nonce](https://github.com/react-native-google-signin/google-signin/issues/1176) to the sign-in request.
</Admonition>

For either option, you need to obtain a Web Client ID from the Google Cloud Engine, as explained in the [Google Sign In](/docs/guides/auth/social-login/auth-google?queryGroups=platform\&platform=react-native#react-native) guide.

This guide only uses the [@react-oauth/google@latest](https://github.com/MomenSherif/react-oauth#googlelogin) option for the Web, and the [`signInWithOAuth`](/docs/reference/javascript/auth-signinwithoauth) for the mobile platforms.

Before proceeding, add a new environment variable to the `.env` file:

```bash
EXPO_PUBLIC_GOOGLE_AUTH_WEB_CLIENT_ID="YOUR_GOOGLE_AUTH_WEB_CLIENT_ID"
```

<Tabs scrollable size="large" type="underlined" defaultActiveId="web" queryGroup="google-authentication">
  <TabPanel id="mobile" label="Mobile">
    Create the mobile generic button component `GoogleSignInButton`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/google/google-sign-in-button.tsx" label="components/social-auth-buttons/google/google-sign-in-button.tsx">
        ```tsx name=components/social-auth-buttons/google/google-sign-in-button.tsx
        import { supabase } from '@/lib/supabase';
        import { useEffect } from 'react';
        import { TouchableOpacity } from 'react-native';

        import { expo } from '@/app.json';
        import { Text } from '@react-navigation/elements';
        import { Image } from 'expo-image';
        import * as WebBrowser from "expo-web-browser";

        WebBrowser.maybeCompleteAuthSession();

        export default function GoogleSignInButton() {

          function extractParamsFromUrl(url: string) {
            const parsedUrl = new URL(url);
            const hash = parsedUrl.hash.substring(1); // Remove the leading '#'
            const params = new URLSearchParams(hash);

            return {
              access_token: params.get("access_token"),
              expires_in: parseInt(params.get("expires_in") || "0"),
              refresh_token: params.get("refresh_token"),
              token_type: params.get("token_type"),
              provider_token: params.get("provider_token"),
              code: params.get("code"),
            };
          };

          async function onSignInButtonPress() {
            console.debug('onSignInButtonPress - start');
            const res = await supabase.auth.signInWithOAuth({
              provider: "google",
              options: {
                redirectTo: `${expo.scheme}://google-auth`,
                queryParams: { prompt: "consent" },
                skipBrowserRedirect: true,
              },
            });

            const googleOAuthUrl = res.data.url;

            if (!googleOAuthUrl) {
              console.error("no oauth url found!");
              return;
            }

            const result = await WebBrowser.openAuthSessionAsync(
              googleOAuthUrl,
              `${expo.scheme}://google-auth`,
              { showInRecents: true },
            ).catch((err) => {
              console.error('onSignInButtonPress - openAuthSessionAsync - error', { err });
              console.log(err);
            });

            console.debug('onSignInButtonPress - openAuthSessionAsync - result', { result });

            if (result && result.type === "success") {
              console.debug('onSignInButtonPress - openAuthSessionAsync - success');
              const params = extractParamsFromUrl(result.url);
              console.debug('onSignInButtonPress - openAuthSessionAsync - success', { params });

              if (params.access_token && params.refresh_token) {
                console.debug('onSignInButtonPress - setSession');
                const { data, error } = await supabase.auth.setSession({
                  access_token: params.access_token,
                  refresh_token: params.refresh_token,
                });
                console.debug('onSignInButtonPress - setSession - success', { data, error });
                return;
              } else {
                console.error('onSignInButtonPress - setSession - failed');
                // sign in/up failed
              }
            } else {
              console.error('onSignInButtonPress - openAuthSessionAsync - failed');
            }
          }

          // to warm up the browser
          useEffect(() => {
            WebBrowser.warmUpAsync();

            return () => {
              WebBrowser.coolDownAsync();
            };
          }, []);

          return (
            <TouchableOpacity
              onPress={onSignInButtonPress}
              style={{
                flexDirection: 'row',
                alignItems: 'center',
                backgroundColor: '#ffffff',
                borderWidth: 1,
                borderColor: '#dbdbdb',
                borderRadius: 4,
                paddingVertical: 10,
                paddingHorizontal: 15,
                justifyContent: 'center',
                shadowColor: '#000',
                shadowOffset: { width: 0, height: 1 },
                shadowOpacity: 0.1,
                shadowRadius: 2,
                elevation: 2, // For Android shadow
              }}
              activeOpacity={0.8}
            >
              <Image
                source={{ uri: 'https://developers.google.com/identity/images/g-logo.png' }}
                style={{ width: 24, height: 24, marginRight: 10 }}
              />
              <Text
                style={{
                  fontSize: 16,
                  color: '#757575',
                  fontFamily: 'Roboto-Regular', // Assuming Roboto is available; install via expo-google-fonts or similar if needed
                  fontWeight: '500',
                }}
              >
                Sign in with Google
              </Text>
            </TouchableOpacity>
          );
        }

        ```
      </TabPanel>
    </Tabs>

    Finally, update the iOS and Android projects by running the Expo prebuild command:

    ```bash
    npx expo prebuild --clean
    ```

    Now test the application on both iOS and Android:

    ```bash
    npx expo run:ios && npx expo run:android
    ```

    You should see the login screen with the Google authentication button.

    ![Supabase Social Auth example](/docs/img/supabase-expo-social-auth-tabs.png)
  </TabPanel>

  <TabPanel id="web" label="Web">
    Install the `@react-oauth/google` library:

    ```bash
    npx expo install @react-oauth/google
    ```

    Enable the `expo-web-browser` plugin in `app.json`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app.json" label="app.json">
        ```json name=app.json
        {
          "expo": {
            ...
            "plugins": {
              ...
              [
                "expo-web-browser",
                {
                  "experimentalLauncherActivity": false
                }
              ]
              ...
            },
            ...
          }
        }
        ```
      </TabPanel>
    </Tabs>

    Then create the iOS specific button component `GoogleSignInButton`:

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="components/social-auth-buttons/google/google-sign-in-button.web.tsx" label="components/social-auth-buttons/google/google-sign-in-button.web.tsx">
        ```tsx name=components/social-auth-buttons/google/google-sign-in-button.web.tsx

        import { supabase } from '@/lib/supabase';
        import { CredentialResponse, GoogleLogin, GoogleOAuthProvider } from '@react-oauth/google';
        import { SignInWithIdTokenCredentials } from '@supabase/supabase-js';
        import { useEffect, useState } from 'react';

        import 'react-native-get-random-values';

        export default function GoogleSignInButton() {

          // Generate secure, random values for state and nonce
          const [nonce, setNonce] = useState('');
          const [sha256Nonce, setSha256Nonce] = useState('');

          async function onGoogleButtonSuccess(authRequestResponse: CredentialResponse) {
            console.debug('Google sign in successful:', { authRequestResponse });
            if (authRequestResponse.clientId && authRequestResponse.credential) {
              const signInWithIdTokenCredentials: SignInWithIdTokenCredentials = {
                provider: 'google',
                token: authRequestResponse.credential,
                nonce: nonce,
              };

              const { data, error } = await supabase.auth.signInWithIdToken(signInWithIdTokenCredentials);

              if (error) {
                console.error('Error signing in with Google:', error);
              }

              if (data) {
                console.log('Google sign in successful:', data);
              }
            }
          }

          function onGoogleButtonFailure() {
            console.error('Error signing in with Google');
          }

          useEffect(() => {
            function generateNonce(): string {
              const array = new Uint32Array(1);
              window.crypto.getRandomValues(array);
              return array[0].toString();
            }

            async function generateSha256Nonce(nonce: string): Promise<string> {
              const buffer = await window.crypto.subtle.digest('sha-256', new TextEncoder().encode(nonce));
              const array = Array.from(new Uint8Array(buffer));
              return array.map(b => b.toString(16).padStart(2, '0')).join('');
            }

            let nonce = generateNonce();
            setNonce(nonce);

            generateSha256Nonce(nonce)
              .then((sha256Nonce) => { setSha256Nonce(sha256Nonce) });
          }, []);

          return (
            <GoogleOAuthProvider
              clientId={process.env.EXPO_PUBLIC_GOOGLE_AUTH_WEB_CLIENT_ID ?? ''}
              nonce={sha256Nonce}
            >
              <GoogleLogin
                nonce={sha256Nonce}
                onSuccess={onGoogleButtonSuccess}
                onError={onGoogleButtonFailure}
                useOneTap={true}
                auto_select={true}
              />
            </GoogleOAuthProvider>
          );
        }

        ```
      </TabPanel>
    </Tabs>

    Test the authentication in your browser using the tunnelled HTTPS URL:

    ```bash
    npx expo start --tunnel
    ```

    <Admonition type="note">
      To allow the Google Sign In to work, as you did before for Apple, you need to register the tunnelled URL (e.g., `https://arnrer1-anonymous-8081.exp.direct`) obtained to the Authorized JavaScript origins list of your [Google Cloud Console's OAuth 2.0 Client IDs](https://console.cloud.google.com/auth/clients/) configuration.
    </Admonition>
  </TabPanel>
</Tabs>



# Single Sign-On with SAML 2.0 for Projects



<Admonition type="tip">
  Looking for guides on how to use Single Sign-On with the Supabase dashboard? Head on over to [Enable SSO for Your Organization](/docs/guides/platform/sso).
</Admonition>

Supabase Auth supports enterprise-level Single Sign-On (SSO) for any identity providers compatible with the SAML 2.0 protocol. This is a non-exclusive list of supported identity providers:

*   Google Workspaces (formerly known as G Suite)
*   Okta, Auth0
*   Microsoft Active Directory, Azure Active Directory, Microsoft Entra
*   PingIdentity
*   OneLogin

If you're having issues with identity provider software not on this list, [open a support ticket](/dashboard/support/new).



## Prerequisites

This guide requires the use of the [Supabase CLI](/docs/guides/cli). Make sure you're using version v1.46.4 or higher. You can use `supabase -v` to see the currently installed version.
You can use the `supabase sso` [subcommands](/docs/reference/cli/supabase-sso) to manage your project's configuration.

SAML 2.0 support is disabled by default on Supabase projects. You can configure this on the [Auth Providers](/dashboard/project/_/auth/providers) page on your project.

Note that SAML 2.0 support is offered on plans Pro and above. Check the [Pricing](/pricing) page for more information.



## Terminology

The number of SAML and SSO acronyms can often be overwhelming. Here's a glossary which you can refer back to at any time:

*   **Identity Provider**, **IdP**, or **IDP**
    An identity provider is a service that manages user accounts at a company or organization. It can verify the identity of a user and exchange that information with your Supabase project and other applications. It acts as a single source of truth for user identities and access rights. Commonly used identity providers are: Microsoft Active Directory (Azure AD, Microsoft Entra), Okta, Google Workspaces (G Suite), PingIdentity, OneLogin, and many others. There are also self-hosted and on-prem versions of identity providers, and sometimes they are accessible only by having access to a company VPN or being in a specific building.
*   **Service Provider**, **SP**
    This is the software that is asking for user information from an identity provider. In Supabase, this is your project's Auth server.
*   **Assertion**
    An assertion is a statement issued by an identity provider that contains information about a user.
*   **`EntityID`**
    A globally unique ID (usually a URL) that identifies an Identity Provider or Service Provider across the world.
*   **`NameID`**
    A unique ID (usually an email address) that identifies a user at an Identity Provider.
*   **Metadata**
    An XML document that describes the features and configuration of an Identity Provider or Service Provider. It can be as a standalone document or as a URL. Usually (but not always) the `EntityID` is the URL at which you can access the Metadata.
*   **Certificate**
    Supabase Auth (the Service Provider) trusts assertions from an Identity Provider based on the signature attached to the assertion. The signature is verified according to the certificate present in the Metadata.
*   **Assertion Consumer Service (ACS) URL**
    This is one of the most important SAML URLs. It is the URL where Supabase Auth will accept assertions from an identity provider. Basically, once the identity provider verifies the user's identity it will redirect to this URL and the redirect request will contain the assertion.
*   **Binding (Redirect, POST, or Artifact)**
    This is a description of the way an identity provider communicates with Supabase Auth. When using the Redirect binding, the communication occurs using HTTP 301 redirects. When it's `POST`, it's using `POST` requests sent with `<form>` elements on a page. When using Artifact, it's using a more secure exchange over a Redirect or `POST`.
*   **`RelayState`**
    State used by Supabase Auth to hold information about a request to verify the identity of a user.



## Important SAML 2.0 information

Below is information about your project's SAML 2.0 configuration which you can share with the company or organization that you're trying to on-board.

| Name                         | Value                                                                   |
| ---------------------------- | ----------------------------------------------------------------------- |
| `EntityID`                   | `https://<project>.supabase.co/auth/v1/sso/saml/metadata`               |
| Metadata URL                 | `https://<project>.supabase.co/auth/v1/sso/saml/metadata`               |
| Metadata URL<br />(download) | `https://<project>.supabase.co/auth/v1/sso/saml/metadata?download=true` |
| ACS URL                      | `https://<project>.supabase.co/auth/v1/sso/saml/acs`                    |
| SLO URL                      | `https://<project>.supabase.co/auth/v1/sso/slo`                         |
| `NameID`                     | Required `emailAddress` or `persistent`                                 |

Note that SLO (Single Logout) is not supported at this time with Supabase Auth as it is a rarely supported feature by identity providers. However, the URL is registered and advertised for when this does become available. SLO is a best-effort service, so we recommend considering [Session Timebox or Session Inactivity Timeout](/docs/guides/auth/sessions#limiting-session-lifetime-and-number-of-allowed-sessions-per-user) instead to force your end-users to authenticate regularly.

Append `?download=true` to the Metadata URL to download the Metadata XML file. This is useful in cases where the identity provider requires a file.

Alternatively, you can use the `supabase sso info --project-ref <your-project>` [command](/docs/reference/cli/supabase-sso-info) to get setup information for your project.


### User accounts and identities

User accounts and identities created via SSO differ from regular (email, phone, password, social login...) accounts in these ways:

*   **No automatic linking.**
    Each user account verified using a SSO identity provider will not be automatically linked to existing user accounts in the system. That is, if a user `valid.email@supabase.io` had signed up with a password, and then uses their company SSO login with your project, there will be two `valid.email@supabase.io` user accounts in the system.
*   **Emails are not necessarily unique.**
    Given the behavior with no automatic linking, email addresses are no longer a unique identifier for a user account. Always use the user's UUID to correctly reference user accounts.
*   **Sessions may have a maximum duration.**
    Depending on the configuration of the identity provider, a login session established with SSO may forcibly log out a user after a certain period of time.


### Row Level Security

You can use information about the SSO identity provider in Row Level Security policies.

Here are some commonly used statements to extract SSO related information from the user's JWT:

*   `auth.jwt()#>>'{amr,0,method}'`
    Returns the name of the last method used to verify the identity of this user. With SAML SSO this is `sso/saml`.
*   `auth.jwt()#>>'{amr,0,provider}'`
    Returns the UUID of the SSO identity provider used by the user to sign-in.
*   `auth.jwt()#>>'{user_metadata,iss}'`
    Returns the identity provider's SAML 2.0 `EntityID`

<Admonition type="caution">
  If you use [Multi-Factor Authentication](/docs/guides/auth/auth-mfa) with SSO, the `amr` array may have a different method at index `0`!
</Admonition>

A common use case with SSO is to use the UUID of the identity provider as the identifier for the organization the user belongs to -- frequently known as a tenant. By associating the identity provider's UUID with your tenants, you can use restrictive RLS policies to scope down actions and data that a user is able to access.

For example, let's say you have a table like:

```sql
create table organization_settings (
  -- the organization's unique ID
  id uuid not null primary key,
  -- the organization's SSO identity provider
  sso_provider_id uuid unique,
  -- name of the organization
  name text,
  -- billing plan (paid, Free, Enterprise)
  billing_plan text
);
```

You can use the information present in the user's JWT to scope down which rows from this table the user can see, without doing any additional user management:

```sql
CREATE POLICY "View organization settings."
  ON organization_settings
  AS RESTRICTIVE
  USING (
    sso_provider_id = (select auth.jwt()#>>'{amr,0,provider}')
  );
```



## Managing SAML 2.0 connections

Once you've enabled SAML 2.0 support on your project via the [Auth Providers](/dashboard/project/_/auth/providers) page in the dashboard, you can use the [Supabase CLI](/docs/reference/cli/supabase-sso) to add, update, remove and view information about identity providers.


### Add a connection

To establish a connection to a SAML 2.0 Identity Provider (IdP) you will need:

*   A SAML 2.0 Metadata XML file, or a SAML 2.0 Metadata URL pointing to an XML file
*   (Optional) Email domains that the organization's IdP uses
*   (Optional) Attribute mappings between the user properties of the IdP and the claims stored by Supabase Auth

You should obtain the SAML 2.0 Metadata XML file or URL from the organization whose IdP you wish to connect. Most SAML 2.0 Identity Providers support the Metadata URL standard, and we recommend using a URL if this is available.

Commonly used SAML 2.0 Identity Providers that support Metadata URLs:

*   Okta
*   Azure AD (Microsoft Entra)
*   PingIdentity

Commonly used SAML 2.0 Identity Providers that only support Metadata XML files:

*   Google Workspaces (G Suite)
*   Any self-hosted or on-prem identity provider behind a VPN

Once you've obtained the SAML 2.0 Metadata XML file or URL you can [establish a connection](/docs/reference/cli/supabase-sso-add) with your project's Supabase Auth server by running:

```bash
supabase sso add --type saml --project-ref <your-project> \
  --metadata-url 'https://company.com/idp/saml/metadata' \
  --domains company.com
```

If you wish to use a Metadata XML file instead, you can use:

```bash
supabase sso add --type saml --project-ref <your-project> \
  --metadata-file /path/to/saml/metadata.xml \
  --domains company.com
```

This command will register a new identity provider with your project's Auth server. When successful, you will see the details of the provider such as it's SAML information and registered domains.

Note that only persons with write access to the project can register, update or remove identity providers.

Once you've added an identity provider, users who have access to it can sign in to your application. With SAML 2.0 there are two ways that users can sign in to your project:

*   By signing-in from your application's user interface, commonly known as **SP (Service Provider) Initiated Flow**
*   By clicking on an icon in the application menu on the company intranet or identity provider page, commonly known as **Identity Provider Initiated (IdP) Flow**

To initiate a sign-in request from your application's user interface (i.e. the SP Initiated Flow), you can use:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    supabase.auth.signInWithSSO({
      domain: 'company.com',
    })
    ```

    Calling [`signInWithSSO`](/docs/reference/javascript/auth-signinwithsso) starts the sign-in process using the identity provider registered for the `company.com` domain name. It is not required that identity providers be assigned one or multiple domain names, in which case you can use the provider's unique ID instead.
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase.auth.signInWithSSO(
      domain: 'company.com',
    );
    ```

    Calling [`signInWithSSO`](/docs/reference/dart/auth-signinwithsso) starts the sign-in process using the identity provider registered for the `company.com` domain name. It is not required that identity providers be assigned one or multiple domain names, in which case you can use the provider's unique ID instead.
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signInWithSSO(
      domain: "company.com"
    )
    ```

    Calling [`signInWithSSO`](/docs/reference/swift/auth-signinwithsso) starts the sign-in process using the identity provider registered for the `company.com` domain name. It is not required that identity providers be assigned one or multiple domain names, in which case you can use the provider's unique ID instead.
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.signInWith(SSO) {
        domain = "company.com"
    }
    ```

    Calling [`signInWith(SSO)`](/docs/reference/kotlin/auth-signinwithsso) starts the sign-in process using the identity provider registered for the `company.com` domain name. It is not required that identity providers be assigned one or multiple domain names, in which case you can use the provider's unique ID instead.
  </TabPanel>
</Tabs>


### Understanding attribute mappings

When a user signs in using the SAML 2.0 Single Sign-On protocol, an XML document called the SAML Assertion is exchanged between the identity provider and Supabase Auth.

This assertion contains information about the user's identity and other authentication information, such as:

*   Unique ID of the user (called `NameID` in SAML)
*   Email address
*   Name of the user
*   Department or organization
*   Other attributes present in the users directory managed by the identity provider

With exception of the unique user ID, SAML does not require any other attributes in the assertion. Identity providers can be configured so that only select user information is shared with your project.

Your project can be configured to recognize these attributes and map them into your project's database using a JSON structure. This process is called attribute mapping, and varies according to the configuration of the identity provider.

For example, the following JSON structure configures attribute mapping for the `email` and `first_name` user identity properties.

```json
{
  "keys": {
    "email": {
      "name": "mail"
    },
    "first_name": {
      "name": "givenName"
    }
  }
}
```

When creating or updating an identity provider with the [Supabase CLI](/docs/guides/cli) you can include this JSON as a file with the `--attribute-mapping-file /path/to/attribute/mapping.json` flag.

For example, to change the attribute mappings to an existing provider you can use:

```bash
supabase sso update <provider-uuid> --project-ref <your-project> \
  --attribute-mapping-file /path/to/attribute/mapping.json
```

Given a SAML 2.0 assertion that includes these attributes:

```xml
<saml:AttributeStatement>
  <!-- will be mapped to the email key -->
  <saml:Attribute
    Name="mail"
    NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"
    >
    <saml:AttributeValue xsi:type="xs:string">
      valid.email@supabase.io
    </saml:AttributeValue>
  </saml:Attribute>

  <!-- will be mapped to the first_name key -->
  <saml:Attribute
    Name="givenName"
    NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:basic"
    >
    <saml:AttributeValue xsi:type="xs:string">
      Jane Doe
    </saml:AttributeValue>
  </saml:Attribute>
</saml:AttributeStatement>
```

Will result in the following claims in the user's identity in the database and JWT:

```json
{
  "email": "valid.email@supabase.io",
  "custom_claims": {
    "first_name": "Jane Doe"
  }
}
```

Supabase Auth does not require specifying attribute mappings if you only need access to the user's email. It will attempt to find an email attribute specified in the assertion. All other properties will not be automatically included, and it is those you need to map.

At this time it is not possible to have users without an email address, so SAML assertions without one will be rejected.

Most SAML 2.0 identity providers use Lightweight Directory Access Protocol (LDAP) attribute names. However, due to their variability and complexity operators of identity providers are able to customize both the `Name` and attribute value that is sent to Supabase Auth in an assertion. Refer to the identity provider's documentation and contact the operator for details on what attributes are mapped for your project.

**Accessing the stored attributes**

The stored attributes, once mapped, show up in the access token (a JWT) of the user. If you need to look these values up in the database, you can find them in the `auth.identities` table under the `identity_data` JSON column. Identities created for SSO providers have `sso:<uuid-of-provider>` in the `provider` column, while `id` contains the unique `NameID` of the user account.

Furthermore, you can find the same identity data under `raw_app_meta_data` inside `auth.users`.


### Remove a connection

Once a connection to an identity provider is established, you can [remove it](/docs/reference/cli/supabase-sso-remove) by running:

```bash
supabase sso remove <provider-id> --project-ref <your-project>
```

If successful, the details of the removed identity provider will be shown. All user accounts from that identity provider will be immediately logged out. User information will remain in the system, but it will no longer be possible for any of those accounts to be accessed in the future, even if you add the connection again.

If you need to reassign those user accounts to another identity provider, [open a support ticket](/dashboard/support/new).
A [list of all](/docs/reference/cli/supabase-sso-list) registered identity providers can be displayed by running:

```bash
supabase sso list --project-ref <your-project>
```


### Update a connection

You may wish to update settings about a connection to a SAML 2.0 identity provider.

Commonly this is necessary when:

*   Cryptographic keys are rotated or have expired
*   Metadata URL has changed, but is the same identity provider
*   Other SAML 2.0 Metadata attributes have changed, but it is still the same identity provider
*   You are updating the domains or attribute mapping

You can use this command to [update](/docs/reference/cli/supabase-sso-update) the configuration of an identity provider:

```bash
supabase sso update <provider-id> --project-ref <your-project>
```

Use `--help` to see all available flags.

It is not possible to change the unique SAML identifier of the identity provider, known as `EntityID`. Everything else can be updated. If the SAML `EntityID` of your identity provider has changed, it is regarded as a new identity provider and you will have to register it like a new connection.


### Retrieving information about a connection

You can always obtain a [list](/docs/reference/cli/supabase-sso-list) of all registered providers using:

```bash
supabase sso list --project-ref <your-project>
```

This list will only include basic information about each provider. To see [all of the information](/docs/reference/cli/supabase-sso-show) about a provider you can use:

```bash
supabase sso show <provider-id> --project-ref <your-project>
```

You can use the `-o json` flag to output the information as JSON, should you need to. Other formats may be supported, use `--help` to see all available options.



## Pricing

<Price price="0.015" /> per SSO MAU. You are only charged for usage exceeding your subscription plan's
quota.

For a detailed breakdown of how charges are calculated, refer to [Manage Monthly Active SSO Users usage](/docs/guides/platform/manage-your-usage/monthly-active-users-sso).



## Frequently asked questions


### Publishing your application to an identity provider's marketplace

Many cloud-based identity providers offer a marketplace where you can register your application for easy on-boarding with customers. When you use Supabase Auth's SAML 2.0 support you can register your project in any one of these marketplaces.

Refer to the relevant documentation for each cloud-based identity provider on how you can do this. Some common marketplaces are:

*   [Okta Integration Network](https://developer.okta.com/docs/guides/build-sso-integration/saml2/main/)
*   [Azure Active Directory App Gallery](https://learn.microsoft.com/en-us/azure/active-directory-b2c/publish-app-to-azure-ad-app-gallery)
*   [Google Workspaces Pre-integrated SAML apps catalog](https://support.google.com/a/table/9217027)


### Why do some users get: SAML assertion does not contain email address?

Identity providers do not have to send back and email address for the user, though they often do. Supabase Auth requires that an email address is present.

The following list of commonly used SAML attribute names is inspected, in order of appearance, to discover the email address in the assertion:

*   `urn:oid:0.9.2342.19200300.100.1.3`
*   `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
*   `http://schemas.xmlsoap.org/claims/EmailAddress`
*   `mail`
*   `email`

Finally if there is no such attribute, it will use the SAML `NameID` value but only if the format is advertised as `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

Should you run into this problem, it is most likely a misconfiguration issue **on the identity provider side.** Instruct your contact at the company to map the user's email address to one of the above listed attribute names, typically `email`.


### Accessing the private key used for SAML in your project

At this time it is not possible to extract the RSA private key used by your project's Supabase Auth server. This is done to keep the private key as secure as possible, given that SAML does not offer an easy way to rotate keys without disrupting service. (Use a SAML 2.0 Metadata URL whenever possible for this reason!)

If you really need access to the key, [open a support ticket](/dashboard/support/new) and we'll try to support you as best as possible.


### Is multi-tenant SSO with SAML supported?

Yes, Supabase supports multi-tenant Single Sign-On (SSO) using SAML 2.0. While the dashboard displays only one SAML field, you can set up multiple SAML connections using the Supabase CLI.
Each connection is assigned a unique `sso_provider_id`, which is included in the user's JWT and can be used in Row Level Security (RLS) policies. You can configure custom attribute mappings for each connection to include tenant-specific information, such as roles.
This setup allows you to implement multi-tenant SSO for multiple clients or organizations within a single application. For example, if you have an app with multiple clients using different Azure Active Directories, you can create separate SAML connections for each and use the `sso_provider_id` to manage access and apply appropriate security policies.


### Is multi-subdomain SSO with SAML supported?

Yes, also referred to as [cross-origin authentication within the same site](https://web.dev/articles/same-site-same-origin). To redirect to a URL other than the [Site URL](/docs/guides/auth/redirect-urls), following the SAML response from the IdP, the `redirectTo` option can be added to [`signInWithSSO`](/docs/reference/javascript/auth-signinwithsso).

```ts
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

// ---cut---
const { data, error } = await supabase.auth.signInWithSSO({
  domain: 'company.com',
  options: {
    redirectTo: `https://app.company.com/callback`,
  },
})
```

When redirecting to a URL other than the Site URL, a `/callback` endpoint is necessary to process the auth code from the IdP and exchange it for a session. This assumes the [Supabase SSR client](/docs/guides/auth/server-side/creating-a-client) has already been configured.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sveltekit" queryGroup="framework">
  <TabPanel id="sveltekit" label="SvelteKit">
    ```ts
    import { error, redirect } from '@sveltejs/kit'
    import type { RequestHandler } from './$types'

    export const GET: RequestHandler = async ({ url, locals }) => {
      const code = url.searchParams.get('code')

      if (!code) {
        error(400, 'No authorization code provided')
      }

      const { error: tokenExchangeError } = await locals.supabase.auth.exchangeCodeForSession(code)

      if (tokenExchangeError) {
        error(400, 'Failed to exchange authorization code for session')
      }

      redirect(303, '/')
    }
    ```
  </TabPanel>
</Tabs>


### Why doesn't IdP-initiated SAML flow work with PKCE, and what's the alternative?

Traditional IdP-initiated SAML flows aren't compatible with PKCE (Proof Key for Code Exchange) because PKCE requires a `code_challenge` and `code_verifier` that are generated when your application initiates the authentication flow. In IdP-initiated flows, Supabase receives an unsolicited response without this information, causing the code exchange step to fail.

To achieve the same user experience while maintaining PKCE security, you can implement a "bookmark app" approach:

Create an endpoint in your application (for example, `https://your-app.com/auth/saml-init`) that initiates the SAML flow using `signInWithSSO`. Then create a bookmark or linked application in your IdP that points to this endpoint. When users access the bookmark app, it triggers a secure SP-initiated flow.

This approach supports custom SAML assertions and lets you embed the link anywhere in your application.



---
**Navigation:** [← Previous](./34-implicit-flow.md) | [Index](./index.md) | [Next →](./36-error-codes.md)
