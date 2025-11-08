**Navigation:** [← Previous](./16-build-a-user-management-app-with-solidjs.md) | [Index](./index.md) | [Next →](./18-use-supabase-with-sveltekit.md)

# Build a User Management App with Vue 3



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/vue3-user-management).
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

Let's start building the Vue 3 app from scratch.


### Initialize a Vue 3 app

We can quickly use [Vite with Vue 3 Template](https://vitejs.dev/guide/#scaffolding-your-first-vite-project) to initialize
an app called `supabase-vue-3`:

```bash

# npm 6.x
npm create vite@latest supabase-vue-3 --template vue


# npm 7+, extra double-dash is needed:
npm create vite@latest supabase-vue-3 -- --template vue

cd supabase-vue-3
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

With the API credentials in place, create an `src/supabase.js` helper file to initialize the Supabase client. These variables are exposed
on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/supabase.js" label="src/supabase.js">
    ```js name=src/supabase.js
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

    export const supabase = createClient(supabaseUrl, supabasePublishableKey)
    ```
  </TabPanel>
</Tabs>

Optionally, update [src/style.css](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/vue3-user-management/src/style.css) to style the app.


### Set up a login component

Set up an `src/components/Auth.vue` component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="/src/components/Auth.vue" label="/src/components/Auth.vue">
    ```vue name=/src/components/Auth.vue
    <script setup>
    import { ref } from 'vue'
    import { supabase } from '../supabase'

    const loading = ref(false)
    const email = ref('')

    const handleLogin = async () => {
      try {
        loading.value = true
        const { error } = await supabase.auth.signInWithOtp({
          email: email.value,
        })
        if (error) throw error
        alert('Check your email for the login link!')
      } catch (error) {
        if (error instanceof Error) {
          alert(error.message)
        }
      } finally {
        loading.value = false
      }
    }
    </script>

    <template>
      <form class="row flex-center flex" @submit.prevent="handleLogin">
        <div class="col-6 form-widget">
          <h1 class="header">Supabase + Vue 3</h1>
          <p class="description">Sign in via magic link with your email below</p>
          <div>
            <input class="inputField" required type="email" placeholder="Your email" v-model="email" />
          </div>
          <div>
            <input
              type="submit"
              class="button block"
              :value="loading ? 'Loading' : 'Send magic link'"
              :disabled="loading"
            />
          </div>
        </div>
      </form>
    </template>
    ```
  </TabPanel>
</Tabs>


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.
Create a new `src/components/Account.vue` component to handle this.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/Account.vue" label="src/components/Account.vue">
    ```vue name=src/components/Account.vue
    <script setup>
    import { supabase } from '../supabase'
    import { onMounted, ref, toRefs } from 'vue'

    const props = defineProps(['session'])
    const { session } = toRefs(props)

    const loading = ref(true)
    const username = ref('')
    const website = ref('')
    const avatar_url = ref('')

    onMounted(() => {
      getProfile()
    })

    async function getProfile() {
      try {
        loading.value = true
        const { user } = session.value

        const { data, error, status } = await supabase
          .from('profiles')
          .select(`username, website, avatar_url`)
          .eq('id', user.id)
          .single()

        if (error && status !== 406) throw error

        if (data) {
          username.value = data.username
          website.value = data.website
          avatar_url.value = data.avatar_url
        }
      } catch (error) {
        alert(error.message)
      } finally {
        loading.value = false
      }
    }

    async function updateProfile() {
      try {
        loading.value = true
        const { user } = session.value

        const updates = {
          id: user.id,
          username: username.value,
          website: website.value,
          avatar_url: avatar_url.value,
          updated_at: new Date(),
        }

        const { error } = await supabase.from('profiles').upsert(updates)

        if (error) throw error
      } catch (error) {
        alert(error.message)
      } finally {
        loading.value = false
      }
    }

    async function signOut() {
      try {
        loading.value = true
        const { error } = await supabase.auth.signOut()
        if (error) throw error
      } catch (error) {
        alert(error.message)
      } finally {
        loading.value = false
      }
    }
    </script>

    <template>
      <form class="form-widget" @submit.prevent="updateProfile">
        <div>
          <label for="email">Email</label>
          <input id="email" type="text" :value="session.user.email" disabled />
        </div>
        <div>
          <label for="username">Name</label>
          <input id="username" type="text" v-model="username" />
        </div>
        <div>
          <label for="website">Website</label>
          <input id="website" type="url" v-model="website" />
        </div>

        <div>
          <input
            type="submit"
            class="button primary block"
            :value="loading ? 'Loading ...' : 'Update'"
            :disabled="loading"
          />
        </div>

        <div>
          <button class="button block" @click="signOut" :disabled="loading">Sign Out</button>
        </div>
      </form>
    </template>
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `App.vue`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.vue" label="src/App.vue">
    ```vue name=src/App.vue
    <script setup>
    import { onMounted, ref } from 'vue'
    import Account from './components/Account.vue'
    import Auth from './components/Auth.vue'
    import { supabase } from './supabase'

    const session = ref()

    onMounted(() => {
      supabase.auth.getSession().then(({ data }) => {
        session.value = data.session
      })

      supabase.auth.onAuthStateChange((_, _session) => {
        session.value = _session
      })
    })
    </script>

    <template>
      <div class="container" style="padding: 50px 0 100px 0">
        <Account v-if="session" :session="session" />
        <Auth v-else />
      </div>
    </template>
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase Vue 3](/docs/img/supabase-vue-3-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Create a new `src/components/Avatar.vue` component that allows users to upload profile photos:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/Avatar.vue" label="src/components/Avatar.vue">
    ```vue name=src/components/Avatar.vue
    <script setup>
    import { ref, toRefs, watchEffect } from 'vue'
    import { supabase } from '../supabase'

    const prop = defineProps(['path', 'size'])
    const { path, size } = toRefs(prop)

    const emit = defineEmits(['upload', 'update:path'])
    const uploading = ref(false)
    const src = ref('')
    const files = ref()

    const downloadImage = async () => {
      try {
        const { data, error } = await supabase.storage.from('avatars').download(path.value)
        if (error) throw error
        src.value = URL.createObjectURL(data)
      } catch (error) {
        console.error('Error downloading image: ', error.message)
      }
    }

    const uploadAvatar = async (evt) => {
      files.value = evt.target.files
      try {
        uploading.value = true
        if (!files.value || files.value.length === 0) {
          throw new Error('You must select an image to upload.')
        }

        const file = files.value[0]
        const fileExt = file.name.split('.').pop()
        const filePath = `${Math.random()}.${fileExt}`

        const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

        if (uploadError) throw uploadError
        emit('update:path', filePath)
        emit('upload')
      } catch (error) {
        alert(error.message)
      } finally {
        uploading.value = false
      }
    }

    watchEffect(() => {
      if (path.value) downloadImage()
    })
    </script>

    <template>
      <div>
        <img
          v-if="src"
          :src="src"
          alt="Avatar"
          class="avatar image"
          :style="{ height: size + 'em', width: size + 'em' }"
        />
        <div v-else class="avatar no-image" :style="{ height: size + 'em', width: size + 'em' }" />

        <div :style="{ width: size + 'em' }">
          <label class="button primary block" for="single">
            {{ uploading ? 'Uploading ...' : 'Upload' }}
          </label>
          <input
            style="visibility: hidden; position: absolute"
            type="file"
            id="single"
            accept="image/*"
            @change="uploadAvatar"
            :disabled="uploading"
          />
        </div>
      </div>
    </template>
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page in `src/components/Account.vue`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/Account.vue" label="src/components/Account.vue">
    ```vue name=src/components/Account.vue
    <script>
    // Import the new component
    import Avatar from './Avatar.vue'
    //...
    const avatar_url = ref('')
    //...
    </script>

    <template>
      <form class="form-widget" @submit.prevent="updateProfile">
        <!-- Add to body -->
        <Avatar v-model:path="avatar_url" @upload="updateProfile" size="10" />

        <!-- Other form elements -->
      </form>
    </template>
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



# Use Supabase with Flutter

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Flutter app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Flutter app">
      Create a Flutter app using the `flutter create` command. You can skip this step if you already have a working app.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        flutter create my_app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use the [`supabase_flutter`](https://pub.dev/packages/supabase_flutter) client library which provides a convenient interface for working with Supabase from a Flutter app.

      Open the `pubspec.yaml` file inside your Flutter app and add `supabase_flutter` as a dependency.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="pubspec.yaml">
        ```yaml name=pubspec.yaml
        supabase_flutter: ^2.0.0
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Initialize the Supabase client">
      Open `lib/main.dart` and edit the main function to initialize Supabase using your project URL and public API (anon) key:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="lib/main.dart">
        ```dart name=lib/main.dart
        import 'package:supabase_flutter/supabase_flutter.dart';

        Future<void> main() async {
          WidgetsFlutterBinding.ensureInitialized();

          await Supabase.initialize(
            url: 'YOUR_SUPABASE_URL',
            anonKey: 'YOUR_SUPABASE_PUBLISHABLE_KEY',
          );
          runApp(MyApp());
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Query data from the app">
      Use a `FutureBuilder` to fetch the data when the home page loads and display the query result in a `ListView`.

      Replace the default `MyApp` and `MyHomePage` classes with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="lib/main.dart">
        ```dart name=lib/main.dart
        class MyApp extends StatelessWidget {
          const MyApp({super.key});

          @override
          Widget build(BuildContext context) {
            return const MaterialApp(
              title: 'Instruments',
              home: HomePage(),
            );
          }
        }

        class HomePage extends StatefulWidget {
          const HomePage({super.key});

          @override
          State<HomePage> createState() => _HomePageState();
        }

        class _HomePageState extends State<HomePage> {
          final _future = Supabase.instance.client
              .from('instruments')
              .select();

          @override
          Widget build(BuildContext context) {
            return Scaffold(
              body: FutureBuilder(
                future: _future,
                builder: (context, snapshot) {
                  if (!snapshot.hasData) {
                    return const Center(child: CircularProgressIndicator());
                  }
                  final instruments = snapshot.data!;
                  return ListView.builder(
                    itemCount: instruments.length,
                    itemBuilder: ((context, index) {
                      final instrument = instruments[index];
                      return ListTile(
                        title: Text(instrument['name']),
                      );
                    }),
                  );
                },
              ),
            );
          }
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Run your app on a platform of your choosing! By default an app should launch in your web browser.

      Note that `supabase_flutter` is compatible with web, iOS, Android, macOS, and Windows apps.
      Running the app on macOS requires additional configuration to [set the entitlements](https://docs.flutter.dev/development/platform-integration/macos/building#setting-up-entitlements).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        flutter run
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Setup deep links

Many sign in methods require deep links to redirect the user back to your app after authentication. Read more about setting deep links up for all platforms (including web) in the [Flutter Mobile Guide](/docs/guides/getting-started/tutorials/with-flutter#setup-deep-links).



## Going to production


### Android

In production, your Android app needs explicit permission to use the internet connection on the user's device which is required to communicate with Supabase APIs.
To do this, add the following line to the `android/app/src/main/AndroidManifest.xml` file.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
  <!-- Required to fetch data from the internet. -->
  <uses-permission android:name="android.permission.INTERNET" />
  <!-- ... -->
</manifest>
```



# Use Supabase with Hono

Learn how to create a Supabase project, add some sample data to your database, secure it with auth, and query the data from a Hono app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Hono app">
      Bootstrap the Hono example app from the Supabase Samples using the CLI.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx supabase@latest bootstrap hono
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The `package.json` file in the project includes the necessary dependencies, including `@supabase/supabase-js` and `@supabase/ssr` to help with server-side auth.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm install
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Set up the required environment variables">
      Copy the `.env.example` file to `.env` and update the values with your Supabase project URL and anon key.

      Lastly, [enable anonymous sign-ins](/dashboard/project/_/auth/providers) in the Auth settings.

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cp .env.example .env
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Start the app">
      Start the app, go to [http://localhost:5173](http://localhost:5173).

      Learn how [server side auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=framework\&framework=hono) works with Hono.
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



## Next steps

*   Learn how [server side auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=framework\&framework=hono) works with Hono.
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)



# Use Supabase with iOS and SwiftUI

Learn how to create a Supabase project, add some sample data to your database, and query the data from an iOS app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create an iOS SwiftUI app with Xcode">
      Open Xcode > New Project > iOS > App. You can skip this step if you already have a working app.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      Install Supabase package dependency using Xcode by following Apple's [tutorial](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

      Make sure to add `Supabase` product package as dependency to the application.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Initialize the Supabase client">
      Create a new `Supabase.swift` file add a new Supabase instance using your project URL and public API (anon) key:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Supabase.swift">
        ```swift name=Supabase.swift
        import Supabase

        let supabase = SupabaseClient(
          supabaseURL: URL(string: "YOUR_SUPABASE_URL")!,
          supabaseKey: "YOUR_SUPABASE_PUBLISHABLE_KEY"
        )
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create a data model for instruments">
      Create a decodable struct to deserialize the data from the database.

      Add the following code to a new file named `Instrument.swift`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Supabase.swift">
        ```swift name=Supabase.swift
        struct Instrument: Decodable, Identifiable {
          let id: Int
          let name: String
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Query data from the app">
      Use a `task` to fetch the data from the database and display it using a `List`.

      Replace the default `ContentView` with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="ContentView.swift">
        ```swift name=ContentView.swift
        struct ContentView: View {

          @State var instruments: [Instrument] = []

          var body: some View {
            List(instruments) { instrument in
              Text(instrument.name)
            }
            .overlay {
              if instruments.isEmpty {
                ProgressView()
              }
            }
            .task {
              do {
                instruments = try await supabase.from("instruments").select().execute().value
              } catch {
                dump(error)
              }
            }
          }
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Start the app">
      Run the app on a simulator or a physical device by hitting `Cmd + R` on Xcode.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with Android Kotlin

Learn how to create a Supabase project, add some sample data to your database, and query the data from an Android Kotlin app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create an Android app with Android Studio">
      Open Android Studio > New > New Android Project.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Dependencies">
      Open `build.gradle.kts` (app) file and add the serialization plug, Ktor client, and Supabase client.

      Replace the version placeholders `$kotlin_version` with the Kotlin version of the project, and  `$supabase_version` and `$ktor_version` with the respective latest versions.

      The latest supabase-kt version can be found [here](https://github.com/supabase-community/supabase-kt/releases) and Ktor version can be found [here](https://ktor.io/docs/welcome.html).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```kotlin
      plugins {
        ...
        kotlin("plugin.serialization") version "$kotlin_version"
      }
      ...
      dependencies {
        ...
        implementation(platform("io.github.jan-tennert.supabase:bom:$supabase_version"))
        implementation("io.github.jan-tennert.supabase:postgrest-kt")
        implementation("io.ktor:ktor-client-android:$ktor_version")
      }
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Add internet access permission">
      Add the following line to the `AndroidManifest.xml` file under the `manifest` tag and outside the `application` tag.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```xml
      ...
      <uses-permission android:name="android.permission.INTERNET" />
      ...
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Initialize the Supabase client">
      You can create a Supabase client whenever you need to perform an API call.

      For the sake of simplicity, we will create a client in the `MainActivity.kt` file at the top just below the imports.

      Replace the `supabaseUrl` and `supabaseKey` with your own:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```kotlin
      import ...

      val supabase = createSupabaseClient(
          supabaseUrl = "https://xyzcompany.supabase.co",
          supabaseKey = "your_public_anon_key"
        ) {
          install(Postgrest)
      }
      ...
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Create a data model for instruments">
      Create a serializable data class to represent the data from the database.

      Add the following below the `createSupabaseClient` function in the `MainActivity.kt` file.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```kotlin
      @Serializable
      data class Instrument(
          val id: Int,
          val name: String,
      )
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Query data from the app">
      Use `LaunchedEffect` to fetch data from the database and display it in a `LazyColumn`.

      Replace the default `MainActivity` class with the following code.

      Note that we are making a network request from our UI code. In production, you should probably use a `ViewModel` to separate the UI and data fetching logic.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```kotlin
      class MainActivity : ComponentActivity() {
          override fun onCreate(savedInstanceState: Bundle?) {
              super.onCreate(savedInstanceState)
              setContent {
                  SupabaseTutorialTheme {
                      // A surface container using the 'background' color from the theme
                      Surface(
                          modifier = Modifier.fillMaxSize(),
                          color = MaterialTheme.colorScheme.background
                      ) {
                          InstrumentsList()
                      }
                  }
              }
          }
      }

      @Composable
      fun InstrumentsList() {
          var instruments by remember { mutableStateOf<List<Instrument>>(listOf()) }
          LaunchedEffect(Unit) {
              withContext(Dispatchers.IO) {
                  instruments = supabase.from("instruments")
                                    .select().decodeList<Instrument>()
              }
          }
          LazyColumn {
              items(
                  instruments,
                  key = { instrument -> instrument.id },
              ) { instrument ->
                  Text(
                      instrument.name,
                      modifier = Modifier.padding(8.dp),
                  )
              }
          }
      }
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={8}>
    <StepHikeCompact.Details title="Start the app">
      Run the app on an emulator or a physical device by clicking the `Run app` button in Android Studio.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with Laravel

Learn how to create a PHP Laravel project, connect it to your Supabase Postgres database, and configure user authentication.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Laravel Project">
      Make sure your PHP and Composer versions are up to date, then use `composer create-project` to scaffold a new Laravel project.

      See the [Laravel docs](https://laravel.com/docs/10.x/installation#creating-a-laravel-project) for more details.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        composer create-project laravel/laravel example-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Install the Authentication template">
      Install [Laravel Breeze](https://laravel.com/docs/10.x/starter-kits#laravel-breeze), a simple implementation of all of Laravel's [authentication features](https://laravel.com/docs/10.x/authentication).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        composer require laravel/breeze --dev
        php artisan breeze:install
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Set up the Postgres connection details">
      Go to [database.new](https://database.new) and create a new Supabase project. Save your database password securely.

      When your project is up and running, navigate to your project dashboard and click on [Connect](/dashboard/project/_?showConnect=true\&method=session).

      Look for the Session Pooler connection string and copy the string. You will need to replace the Password with your saved database password. You can reset your database password in your [Database Settings](/dashboard/project/_/database/settings) if you do not have it.

      <Admonition type="note">
        If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name=".env">
        ```bash name=.env
        DB_CONNECTION=pgsql
        DB_URL=postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Change the default schema">
      By default Laravel uses the `public` schema. We recommend changing this as Supabase exposes the `public` schema as a [data API](/docs/guides/api).

      You can change the schema of your Laravel application by modifying the `search_path` variable `app/config/database.php`.

      The schema you specify in `search_path` has to exist on Supabase. You can create a new schema from the [Table Editor](/dashboard/project/_/editor).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="app/config/database.php">
        ```php name=app/config/database.php
        'pgsql' => [
            'driver' => 'pgsql',
            'url' => env('DB_URL'),
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'laravel'),
            'username' => env('DB_USERNAME', 'root'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => env('DB_CHARSET', 'utf8'),
            'prefix' => '',
            'prefix_indexes' => true,
            'search_path' => 'laravel',
            'sslmode' => 'prefer',
        ],
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Run the database migrations">
      Laravel ships with database migration files that set up the required tables for Laravel Authentication and User Management.

      Note: Laravel does not use Supabase Auth but rather implements its own authentication system!
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        php artisan migrate
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Run the development server. Go to [http://127.0.0.1:8000](http://127.0.0.1:8000) in a browser to see your application. You can also navigate to [http://127.0.0.1:8000/register](http://127.0.0.1:8000/register) and [http://127.0.0.1:8000/login](http://127.0.0.1:8000/login) to register and log in users.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        php artisan serve
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with Next.js

Learn how to create a Supabase project, add some sample data, and query from a Next.js app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Next.js app">
      Use the `create-next-app` command and the `with-supabase` template, to create a Next.js app pre-configured with:

      *   [Cookie-based Auth](/docs/guides/auth/server-side/creating-a-client?queryGroups=package-manager\&package-manager=npm\&queryGroups=framework\&framework=nextjs\&queryGroups=environment\&environment=server)
      *   [TypeScript](https://www.typescriptlang.org/)
      *   [Tailwind CSS](https://tailwindcss.com/)
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash
      npx create-next-app -e with-supabase
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Rename `.env.example` to `.env.local` and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```text name=.env.local
          NEXT_PUBLIC_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Create Supabase client">
      Create a new file at `utils/supabase/server.ts` and populate with the following.

      This creates a Supabase client, using the credentials from the `env.local` file.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="utils/supabase/server.ts" label="utils/supabase/server.ts">
          ```ts name=utils/supabase/server.ts
          import { createServerClient } from '@supabase/ssr'
          import { cookies } from 'next/headers'

          export async function createClient() {
            const cookieStore = await cookies()

            return createServerClient(
              process.env.NEXT_PUBLIC_SUPABASE_URL!,
              process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
              {
                cookies: {
                  getAll() {
                    return cookieStore.getAll()
                  },
                  setAll(cookiesToSet) {
                    try {
                      cookiesToSet.forEach(({ name, value, options }) =>
                        cookieStore.set(name, value, options)
                      )
                    } catch {
                      // The `setAll` method was called from a Server Component.
                      // This can be ignored if you have middleware refreshing
                      // user sessions.
                    }
                  },
                },
              }
            )
          }
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Query Supabase data from Next.js">
      Create a new file at `app/instruments/page.tsx` and populate with the following.

      This selects all the rows from the `instruments` table in Supabase and render them on the page.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="app/instruments/page.tsx" label="app/instruments/page.tsx">
          ```ts name=app/instruments/page.tsx
          import { createClient } from '@/utils/supabase/server';

          export default async function Instruments() {
            const supabase = await createClient();
            const { data: instruments } = await supabase.from("instruments").select();

            return <pre>{JSON.stringify(instruments, null, 2)}</pre>
          }
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Run the development server, go to [http://localhost:3000/instruments](http://localhost:3000/instruments) in a browser and you should see the list of instruments.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash Terminal
      npm run dev
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Next steps

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)



# Use Supabase with Nuxt

Learn how to create a Supabase project, add some sample data to your database, and query the data from a Nuxt app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Nuxt app">
      Create a Nuxt app using the `npx nuxi` command.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx nuxi@latest init my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a Nuxt app.

      Navigate to the Nuxt app and install `supabase-js`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Create a `.env` file and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```text name=.env.local
          SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>

        <TabPanel id="nuxt.config.tsx" label="nuxt.config.tsx">
          ```ts name=nuxt.config.tsx
          export default defineNuxtConfig({
            runtimeConfig: {
              public: {
                supabaseUrl: process.env.SUPABASE_URL,
                supabasePublishableKey: process.env.SUPABASE_PUBLISHABLE_KEY,
              },
            },
          });
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Query data from the app">
      In `app.vue`, create a Supabase client using your config values and replace the existing content with the following code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="app.vue">
        ```vue name=app.vue
        <script setup>
        import { createClient } from '@supabase/supabase-js'
        const config = useRuntimeConfig()
        const supabase = createClient(config.public.supabaseUrl, config.public.supabasePublishableKey)
        const instruments = ref([])

        async function getInstruments() {
          const { data } = await supabase.from('instruments').select()
          instruments.value = data
        }

        onMounted(() => {
          getInstruments()
        })
        </script>

        <template>
          <ul>
            <li v-for="instrument in instruments" :key="instrument.id">{{ instrument.name }}</li>
          </ul>
        </template>
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Start the app, navigate to [http://localhost:3000](http://localhost:3000) in the browser, open the browser console, and you should see the list of instruments.
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

<Admonition type="tip">
  The community-maintained [@nuxtjs/supabase](https://supabase.nuxtjs.org/) module provides an alternate DX for working with Supabase in Nuxt.
</Admonition>



# Use Supabase with React

Learn how to create a Supabase project, add some sample data to your database, and query the data from a React app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a React app">
      Create a React app using a [Vite](https://vitejs.dev/guide/) template.
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
      The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a React app.

      Navigate to the React app and install `supabase-js`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Create a `.env.local` file and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```text name=.env.local
          VITE_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          VITE_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Query data from the app">
      Replace the contents of `App.jsx` to add a `getInstruments` function to fetch the data and display the query result to the page using a Supabase client.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/App.jsx">
        ```js name=src/App.jsx
        import { useEffect, useState } from "react";
        import { createClient } from "@supabase/supabase-js";

        const supabase = createClient(import.meta.env.VITE_SUPABASE_URL, import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY);

        function App() {
          const [instruments, setInstruments] = useState([]);

          useEffect(() => {
            getInstruments();
          }, []);

          async function getInstruments() {
            const { data } = await supabase.from("instruments").select();
            setInstruments(data);
          }

          return (
            <ul>
              {instruments.map((instrument) => (
                <li key={instrument.name}>{instrument.name}</li>
              ))}
            </ul>
          );
        }

        export default App;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Run the development server, go to [http://localhost:5173](http://localhost:5173) in a browser and you should see the list of instruments.
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



## Next steps

*   Set up [Auth](/docs/guides/auth) for your app
*   [Insert more data](/docs/guides/database/import-data) into your database
*   Upload and serve static files using [Storage](/docs/guides/storage)



# Use Supabase with RedwoodJS

Learn how to create a Supabase project, add some sample data to your database using Prisma migration and seeds, and query the data from a RedwoodJS app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Setup your new Supabase Project">
      [Create a new project](/dashboard) in the Supabase Dashboard.

      <Admonition type="tip">
        Be sure to make note of the Database Password you used as you will need this later to connect to your database.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![New project for redwoodjs](/docs/img/guides/getting-started/quickstarts/redwoodjs/new-project.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Gather Database Connection Strings">
      Open the project [**Connect** panel](/dashboard/project/_?showConnect=true). This quickstart connects using the [**Transaction pooler**](/dashboard/project/_?showConnect=true\&method=transaction) and [**Session pooler**](/dashboard/project/_?showConnect=true\&method=session) mode. Transaction mode is used for application queries and Session mode is used for running migrations with Prisma.

      To do this, set the connection mode to `Transaction` in the [Database Settings page](/dashboard/project/_/database/settings) and copy the connection string and append `?pgbouncer=true&&connection_limit=1`. `pgbouncer=true` disables Prisma from generating prepared statements. This is required since our connection pooler does not support prepared statements in transaction mode yet. The `connection_limit=1` parameter is only required if you are using Prisma from a serverless environment. This is the Transaction mode connection string.

      To get the Session mode connection pooler string, change the port of the connection string from the dashboard to 5432.

      You will need the Transaction mode connection string and the Session mode connection string to setup environment variables in Step 5.

      <Admonition type="tip">
        You can copy and paste these connection strings from the Supabase Dashboard when needed in later steps.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![pooled connection for redwoodjs](/docs/img/guides/getting-started/quickstarts/redwoodjs/pooled-connection-strings.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Create a RedwoodJS app">
      Create a RedwoodJS app with TypeScript.

      <Admonition type="note">
        The [`yarn` package manager](https://yarnpkg.com) is required to create a RedwoodJS app. You will use it to run RedwoodJS commands later.

        While TypeScript is recommended, If you want a JavaScript app, omit the `--ts` flag.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        yarn create redwood-app my-app --ts
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Open your RedwoodJS app in VS Code">
      You'll develop your app, manage database migrations, and run your app in VS Code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app
        code .
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Configure Environment Variables">
      In your `.env` file, add the following environment variables for your database connection:

      *   The `DATABASE_URL` should use the Transaction mode connection string you copied in Step 1.

      *   The `DIRECT_URL` should use the Session mode connection string you copied in Step 1.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name=".env">
        ```bash name=.env
        # Transaction mode connection string used for migrations
        DATABASE_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:6543/postgres?pgbouncer=true&connection_limit=1"

        # Session mode connection string — used by Prisma Client
        DIRECT_URL="postgres://postgres.[project-ref]:[db-password]@xxx.pooler.supabase.com:5432/postgres"
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Update your Prisma Schema">
      By default, RedwoodJS ships with a SQLite database, but we want to use Postgres.

      Update your Prisma schema file `api/db/schema.prisma` to use your Supabase Postgres database connection environment variables you setup in Step 5.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="api/db/schema.prisma">
        ```prisma name=api/db/schema.prisma
        datasource db {
          provider  = "postgresql"
          url       = env("DATABASE_URL")
          directUrl = env("DIRECT_URL")
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Create the Instrument model and apply a schema migration">
      Create the Instrument model in `api/db/schema.prisma` and then run `yarn rw prisma migrate dev` from your terminal to apply the migration.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="api/db/schema.prisma">
        ```prisma name=api/db/schema.prisma
        model Instrument {
          id   Int    @id @default(autoincrement())
          name String @unique
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={8}>
    <StepHikeCompact.Details title="Update seed script">
      Let's seed the database with a few instruments.

      Update the file `scripts/seeds.ts` to contain the following code:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="scripts/seed.ts">
        ```ts name=scripts/seed.ts
        import type { Prisma } from '@prisma/client'
        import { db } from 'api/src/lib/db'

        export default async () => {
          try {
            const data: Prisma.InstrumentCreateArgs['data'][] = [
              { name: 'dulcimer' },
              { name: 'harp' },
              { name: 'guitar' },
            ]

            console.log('Seeding instruments ...')

            const instruments = await db.instrument.createMany({ data })

            console.log('Done.', instruments)
          } catch (error) {
            console.error(error)
          }
        }
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={9}>
    <StepHikeCompact.Details title="Seed your database">
      Run the seed database command to populate the `Instrument` table with the instruments you just created.

      <Admonition type="tip">
        The reset database command `yarn rw prisma db reset` will recreate the tables and will also run the seed script.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        yarn rw prisma db seed
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={10}>
    <StepHikeCompact.Details title="Scaffold the Instrument UI">
      Now, we'll use RedwoodJS generators to scaffold a CRUD UI for the `Instrument` model.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        yarn rw g scaffold instrument
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={11}>
    <StepHikeCompact.Details title="Start the app">
      Start the app via `yarn rw dev`. A browser will open to the RedwoodJS Splash page.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![RedwoodJS Splash Page](/docs/img/redwoodjs-qs-splash.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={12}>
    <StepHikeCompact.Details title="View Books UI">
      Click on `/instruments` to visit [http://localhost:8910/instruments](http://localhost:8910/instruments) where should see the list of instruments.

      You may now edit, delete, and add new books using the scaffolded UI.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with refine

Learn how to create a Supabase project, add some sample data to your database, and query the data from a refine app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a refine app">
      Create a [refine](https://github.com/refinedev/refine) app using the [create refine-app](https://refine.dev/docs/getting-started/quickstart/).

      The `refine-supabase` preset adds `@refinedev/supabase` supplementary package that supports Supabase in a refine app. `@refinedev/supabase` out-of-the-box includes the Supabase dependency: [supabase-js](https://github.com/supabase/supabase-js).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm create refine-app@latest -- --preset refine-supabase my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Open your refine app in VS Code">
      You will develop your app, connect to the Supabase backend and run the refine app in VS Code.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app
        code .
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Start the app">
      Start the app, go to [http://localhost:5173](http://localhost:5173) in a browser, and you should be greeted with the refine Welcome page.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run dev
        ```
      </NamedCodeBlock>

      <StepHikeCompact.Code>
        ![refine welcome page](/docs/img/refine-qs-welcome-page.png)
      </StepHikeCompact.Code>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Update `supabaseClient`">
      You now have to update the `supabaseClient` with the `SUPABASE_URL` and `SUPABASE_KEY` of your Supabase API. The `supabaseClient` is used in auth provider and data provider methods that allow the refine app to connect to your Supabase backend.

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/utility/supabaseClient.ts">
        ```ts name=src/utility/supabaseClient.ts
        import { createClient } from "@refinedev/supabase";

        const SUPABASE_URL = YOUR_SUPABASE_URL;
        const SUPABASE_KEY = YOUR_SUPABASE_KEY

        export const supabaseClient = createClient(SUPABASE_URL, SUPABASE_KEY, {
          db: {
            schema: "public",
          },
          auth: {
            persistSession: true,
          },
        });
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Add instruments resource and pages">
      You have to then configure resources and define pages for `instruments` resource.

      Use the following command to automatically add resources and generate code for pages for `instruments` using refine Inferencer.

      This defines pages for `list`, `create`, `show` and `edit` actions inside the `src/pages/instruments/` directory with `<HeadlessInferencer />` component.

      The `<HeadlessInferencer />` component depends on `@refinedev/react-table` and `@refinedev/react-hook-form` packages. In order to avoid errors, you should install them as dependencies with `npm install @refinedev/react-table @refinedev/react-hook-form`.

      <Admonition type="note">
        The `<HeadlessInferencer />` is a refine Inferencer component that automatically generates necessary code for the `list`, `create`, `show` and `edit` pages.

        More on [how the Inferencer works is available in the docs here](https://refine.dev/docs/packages/documentation/inferencer/).
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npm run refine create-resource instruments
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Add routes for instruments pages">
      Add routes for the `list`, `create`, `show`, and `edit` pages.

      <Admonition type="tip">
        You should remove the `index` route for the Welcome page presented with the `<Welcome />` component.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/App.tsx">
        ```tsx name=src/App.tsx
        import { Refine, WelcomePage } from "@refinedev/core";
        import { RefineKbar, RefineKbarProvider } from "@refinedev/kbar";
        import routerBindings, {
          DocumentTitleHandler,
          NavigateToResource,
          UnsavedChangesNotifier,
        } from "@refinedev/react-router-v6";
        import { dataProvider, liveProvider } from "@refinedev/supabase";
        import { BrowserRouter, Route, Routes } from "react-router-dom";

        import "./App.css";
        import authProvider from "./authProvider";
        import { supabaseClient } from "./utility";
        import { InstrumentsCreate, InstrumentsEdit, InstrumentsList, InstrumentsShow } from "./pages/instruments";

        function App() {
          return (
            <BrowserRouter>
              <RefineKbarProvider>
                <Refine
                  dataProvider={dataProvider(supabaseClient)}
                  liveProvider={liveProvider(supabaseClient)}
                  authProvider={authProvider}
                  routerProvider={routerBindings}
                  options={{
                    syncWithLocation: true,
                    warnWhenUnsavedChanges: true,
                  }}
                  resources={[{
                    name: "instruments",
                    list: "/instruments",
                    create: "/instruments/create",
                    edit: "/instruments/edit/:id",
                    show: "/instruments/show/:id"
                  }]}>
                  <Routes>
                    <Route index
                      element={<NavigateToResource resource="instruments" />}
                    />
                    <Route path="/instruments">
                      <Route index element={<InstrumentsList />} />
                      <Route path="create" element={<InstrumentsCreate />} />
                      <Route path="edit/:id" element={<InstrumentsEdit />} />
                      <Route path="show/:id" element={<InstrumentsShow />} />
                    </Route>
                  </Routes>
                  <RefineKbar />
                  <UnsavedChangesNotifier />
                  <DocumentTitleHandler />
                </Refine>
              </RefineKbarProvider>
            </BrowserRouter>
          );
        }

        export default App;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={8}>
    <StepHikeCompact.Details title="View instruments pages">
      Now you should be able to see the instruments pages along the `/instruments` routes. You may now edit and add new instruments using the Inferencer generated UI.

      The Inferencer auto-generated code gives you a good starting point on which to keep building your `list`, `create`, `show` and `edit` pages. They can be obtained by clicking the `Show the auto-generated code` buttons in their respective pages.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with Ruby on Rails

Learn how to create a Rails project and connect it to your Supabase Postgres database.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Rails Project">
      Make sure your Ruby and Rails versions are up to date, then use `rails new` to scaffold a new Rails project. Use the `-d=postgresql` flag to set it up for Postgres.

      Go to the [Rails docs](https://guides.rubyonrails.org/getting_started.html) for more details.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        rails new blog -d=postgresql
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Set up the Postgres connection details">
      Go to [database.new](https://database.new) and create a new Supabase project. Save your database password securely.

      When your project is up and running, navigate to your project dashboard and click on [Connect](/dashboard/project/_?showConnect=true\&method=session).

      Look for the Session Pooler connection string and copy the string. You will need to replace the Password with your saved database password. You can reset your database password in your [Database Settings](/dashboard/project/_/database/settings) if you do not have it.

      <Admonition type="note">
        If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        export DATABASE_URL=postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Create and run a database migration">
      Rails includes Active Record as the ORM as well as database migration tooling which generates the SQL migration files for you.

      Create an example `Article` model and generate the migration files.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        bin/rails generate model Article title:string body:text
        bin/rails db:migrate
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Use the Model to interact with the database">
      You can use the included Rails console to interact with the database. For example, you can create new entries or list all entries in a Model's table.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        bin/rails console
        ```
      </NamedCodeBlock>

      <NamedCodeBlock name="irb">
        ```rb name=irb
        article = Article.new(title: "Hello Rails", body: "I am on Rails!")
        article.save # Saves the entry to the database

        Article.all
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Start the app">
      Run the development server. Go to [http://127.0.0.1:3000](http://127.0.0.1:3000) in a browser to see your application running.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        bin/rails server
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Use Supabase with SolidJS

Learn how to create a Supabase project, add some sample data to your database, and query the data from a SolidJS app.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a Supabase project">
      Go to [database.new](https://database.new) and create a new Supabase project.

      Alternatively, you can create a project using the Management API:

      ```bash
      # First, get your access token from https://supabase.com/dashboard/account/tokens
      export SUPABASE_ACCESS_TOKEN="your-access-token"

      # List your organizations to get the organization ID
      curl -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        https://api.supabase.com/v1/organizations

      # Create a new project (replace <org-id> with your organization ID)
      curl -X POST https://api.supabase.com/v1/projects \
        -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "organization_id": "<org-id>",
          "name": "My Project",
          "region": "us-east-1",
          "db_pass": "<your-secure-password>"
        }'
      ```

      When your project is up and running, go to the [Table Editor](/dashboard/project/_/editor), create a new table and insert some data.

      Alternatively, you can run the following snippet in your project's [SQL Editor](/dashboard/project/_/sql/new). This will create a `instruments` table with some sample data.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      -- Create the table
      create table instruments (
        id bigint primary key generated always as identity,
        name text not null
      );
      -- Insert some sample data into the table
      insert into instruments (name)
      values
        ('violin'),
        ('viola'),
        ('cello');

      alter table instruments enable row level security;
      ```
    </StepHikeCompact.Code>

    <StepHikeCompact.Details>
      Make the data in your table publicly readable by adding an RLS policy:
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql SQL_EDITOR
      create policy "public can read instruments"
      on public.instruments
      for select to anon
      using (true);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a SolidJS app">
      Create a SolidJS app using the `degit` command.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        npx degit solidjs/templates/js my-app
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Install the Supabase client library">
      The fastest way to get started is to use the `supabase-js` client library which provides a convenient interface for working with Supabase from a SolidJS app.

      Navigate to the SolidJS app and install `supabase-js`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="Terminal">
        ```bash name=Terminal
        cd my-app && npm install @supabase/supabase-js
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Declare Supabase Environment Variables">
      Create a `.env.local` file and populate with your Supabase connection variables:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```text name=.env.local
          VITE_SUPABASE_URL=<SUBSTITUTE_SUPABASE_URL>
          VITE_SUPABASE_PUBLISHABLE_KEY=<SUBSTITUTE_SUPABASE_PUBLISHABLE_KEY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Query data from the app">
      In `App.jsx`, create a Supabase client to fetch the instruments data.

      Add a `getInstruments` function to fetch the data and display the query result to the page.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <NamedCodeBlock name="src/App.jsx">
        ```jsx name=src/App.jsx
        import { createClient } from "@supabase/supabase-js";
        import { createResource, For } from "solid-js";

        const supabase = createClient('https://<project>.supabase.co', '<sb_publishable_... or anon key>');

        async function getInstruments() {
          const { data } = await supabase.from("instruments").select();
          return data;
        }

        function App() {
          const [instruments] = createResource(getInstruments);

          return (
            <ul>
              <For each={instruments()}>{(instrument) => <li>{instrument.name}</li>}</For>
            </ul>
          );
        }

        export default App;
        ```
      </NamedCodeBlock>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Start the app">
      Start the app and go to [http://localhost:3000](http://localhost:3000) in a browser and you should see the list of instruments.
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



---
**Navigation:** [← Previous](./16-build-a-user-management-app-with-solidjs.md) | [Index](./index.md) | [Next →](./18-use-supabase-with-sveltekit.md)
