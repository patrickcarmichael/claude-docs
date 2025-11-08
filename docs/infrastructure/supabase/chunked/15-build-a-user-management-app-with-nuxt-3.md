**Navigation:** [← Previous](./14-build-a-user-management-app-with-ionic-vue.md) | [Index](./index.md) | [Next →](./16-build-a-user-management-app-with-solidjs.md)

# Build a User Management App with Nuxt 3



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nuxt3-user-management).
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


### Initialize a Nuxt 3 app

We can use [`nuxi init`](https://nuxt.com/docs/getting-started/installation) to create an app called `nuxt-user-management`:

```bash
npx nuxi init nuxt-user-management

cd nuxt-user-management
```

Then let's install the only additional dependency: [Nuxt Supabase](https://supabase.nuxtjs.org/). We only need to import Nuxt Supabase as a dev dependency.

```bash
npm install @nuxtjs/supabase --save-dev
```

And finally we want to save the environment variables in a `.env`.
All we need are the API URL and the key that you copied [earlier](#get-api-details).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    SUPABASE_URL="YOUR_SUPABASE_URL"
    SUPABASE_KEY="YOUR_SUPABASE_PUBLISHABLE_KEY"
    ```
  </TabPanel>
</Tabs>

These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.
Amazing thing about [Nuxt Supabase](https://supabase.nuxtjs.org/) is that setting environment variables is all we need to do in order to start using Supabase.
No need to initialize Supabase. The library will take care of it automatically.


### App styling (optional)

An optional step is to update the CSS file `assets/main.css` to make the app look nice.
You can find the full contents of this file [here](https://github.com/supabase-community/nuxt3-quickstarter/blob/main/assets/main.css).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="nuxt.config.ts" label="nuxt.config.ts">
    ```typescript name=nuxt.config.ts
    import { defineNuxtConfig } from 'nuxt'

    // https://v3.nuxtjs.org/api/configuration/nuxt.config
    export default defineNuxtConfig({
      modules: ['@nuxtjs/supabase'],
      css: ['@/assets/main.css'],
    })
    ```
  </TabPanel>
</Tabs>


### Set up Auth component

Let's set up a Vue component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="/components/Auth.vue" label="/components/Auth.vue">
    ```vue name=/components/Auth.vue
    <script setup>
    const supabase = useSupabaseClient()

    const loading = ref(false)
    const email = ref('')

    const handleLogin = async () => {
      try {
        loading.value = true
        const { error } = await supabase.auth.signInWithOtp({ email: email.value })
        if (error) throw error
        alert('Check your email for the login link!')
      } catch (error) {
        alert(error.error_description || error.message)
      } finally {
        loading.value = false
      }
    }
    </script>

    <template>
      <form class="row flex-center flex" @submit.prevent="handleLogin">
        <div class="col-6 form-widget">
          <h1 class="header">Supabase + Nuxt 3</h1>
          <p class="description">Sign in via magic link with your email below</p>
          <div>
            <input class="inputField" type="email" placeholder="Your email" v-model="email" />
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


### User state

To access the user information, use the composable [`useSupabaseUser`](https://supabase.nuxtjs.org/composables/usesupabaseuser) provided by the Supabase Nuxt module.


### Account component

After a user is signed in we can allow them to edit their profile details and manage their account.
Let's create a new component for that called `Account.vue`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Account.vue" label="components/Account.vue">
    ```vue name=components/Account.vue
    <script setup>
    const supabase = useSupabaseClient()

    const loading = ref(true)
    const username = ref('')
    const website = ref('')
    const avatar_path = ref('')

    loading.value = true
    const user = useSupabaseUser()

    const { data } = await supabase
      .from('profiles')
      .select(`username, website, avatar_url`)
      .eq('id', user.value.id)
      .single()

    if (data) {
      username.value = data.username
      website.value = data.website
      avatar_path.value = data.avatar_url
    }

    loading.value = false

    async function updateProfile() {
      try {
        loading.value = true
        const user = useSupabaseUser()

        const updates = {
          id: user.value.id,
          username: username.value,
          website: website.value,
          avatar_url: avatar_path.value,
          updated_at: new Date(),
        }

        const { error } = await supabase.from('profiles').upsert(updates, {
          returning: 'minimal', // Don't return the value after inserting
        })
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
        user.value = null
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
          <input id="email" type="text" :value="user.email" disabled />
        </div>
        <div>
          <label for="username">Username</label>
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

Now that we have all the components in place, let's update `app.vue`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="app.vue" label="app.vue">
    ```vue name=app.vue
    <script setup>
    const user = useSupabaseUser()
    </script>

    <template>
      <div class="container" style="padding: 50px 0 100px 0">
        <Account v-if="user" />
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

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase Nuxt 3](/docs/img/supabase-vue-3-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Avatar.vue" label="components/Avatar.vue">
    ```vue name=components/Avatar.vue
    <script setup>
    const props = defineProps(['path'])
    const { path } = toRefs(props)

    const emit = defineEmits(['update:path', 'upload'])

    const supabase = useSupabaseClient()

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
        const fileName = `${Math.random()}.${fileExt}`
        const filePath = `${fileName}`

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

    downloadImage()

    watch(path, () => {
      if (path.value) {
        downloadImage()
      }
    })
    </script>

    <template>
      <div>
        <img
          v-if="src"
          :src="src"
          alt="Avatar"
          class="avatar image"
          style="width: 10em; height: 10em;"
        />
        <div v-else class="avatar no-image" :style="{ height: size, width: size }" />

        <div style="width: 10em; position: relative;">
          <label class="button primary block" for="single">
            {{ uploading ? 'Uploading ...' : 'Upload' }}
          </label>
          <input
            style="position: absolute; visibility: hidden;"
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

And then we can add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="components/Account.vue" label="components/Account.vue">
    ```vue name=components/Account.vue
    <script setup>
    const supabase = useSupabaseClient()

    const loading = ref(true)
    const username = ref('')
    const website = ref('')
    const avatar_path = ref('')

    loading.value = true
    const user = useSupabaseUser()

    const { data } = await supabase
      .from('profiles')
      .select(`username, website, avatar_url`)
      .eq('id', user.value.id)
      .single()

    if (data) {
      username.value = data.username
      website.value = data.website
      avatar_path.value = data.avatar_url
    }

    loading.value = false

    async function updateProfile() {
      try {
        loading.value = true
        const user = useSupabaseUser()

        const updates = {
          id: user.value.id,
          username: username.value,
          website: website.value,
          avatar_url: avatar_path.value,
          updated_at: new Date(),
        }

        const { error } = await supabase.from('profiles').upsert(updates, {
          returning: 'minimal', // Don't return the value after inserting
        })

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
        <Avatar v-model:path="avatar_path" @upload="updateProfile" />
        <div>
          <label for="email">Email</label>
          <input id="email" type="text" :value="user.email" disabled />
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

That is it! You should now be able to upload a profile photo to Supabase Storage and you have a fully functional application.



# Build a User Management App with React



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/react-user-management).
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


### Initialize a React app

We can use [Vite](https://vitejs.dev/guide/) to initialize
an app called `supabase-react`:

```bash
npm create vite@latest supabase-react -- --template react
cd supabase-react
```

Then let's install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js).

```bash
npm install @supabase/supabase-js
```

And finally, save the environment variables in a `.env.local` file.
All we need are the Project URL and the key that you copied [earlier](#get-api-details).

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

Create and edit `src/supabaseClient.js`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/supabaseClient.js" label="src/supabaseClient.js">
    ```js name=src/supabaseClient.js
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

    export const supabase = createClient(supabaseUrl, supabasePublishableKey)
    ```
  </TabPanel>
</Tabs>


### App styling (optional)

An optional step is to update the CSS file `src/index.css` to make the app look nice.
You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/react-user-management/src/index.css).


### Set up a login component

Let's set up a React component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

Create and edit `src/Auth.jsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Auth.jsx" label="src/Auth.jsx">
    ```jsx name=src/Auth.jsx
    import { useState } from 'react'
    import { supabase } from './supabaseClient'

    export default function Auth() {
      const [loading, setLoading] = useState(false)
      const [email, setEmail] = useState('')

      const handleLogin = async (event) => {
        event.preventDefault()

        setLoading(true)
        const { error } = await supabase.auth.signInWithOtp({ email })

        if (error) {
          alert(error.error_description || error.message)
        } else {
          alert('Check your email for the login link!')
        }
        setLoading(false)
      }

      return (
        <div className="row flex flex-center">
          <div className="col-6 form-widget">
            <h1 className="header">Supabase + React</h1>
            <p className="description">Sign in via magic link with your email below</p>
            <form className="form-widget" onSubmit={handleLogin}>
              <div>
                <input
                  className="inputField"
                  type="email"
                  placeholder="Your email"
                  value={email}
                  required={true}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div>
                <button className={'button block'} disabled={loading}>
                  {loading ? <span>Loading</span> : <span>Send magic link</span>}
                </button>
              </div>
            </form>
          </div>
        </div>
      )
    }
    ```
  </TabPanel>
</Tabs>


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `src/Account.jsx`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Account.jsx" label="src/Account.jsx">
    ```jsx name=src/Account.jsx
    import { useState, useEffect } from 'react'
    import { supabase } from './supabaseClient'

    export default function Account({ session }) {
      const [loading, setLoading] = useState(true)
      const [username, setUsername] = useState(null)
      const [website, setWebsite] = useState(null)
      const [avatar_url, setAvatarUrl] = useState(null)

      useEffect(() => {
        let ignore = false
        async function getProfile() {
          setLoading(true)
          const { user } = session

          const { data, error } = await supabase
            .from('profiles')
            .select(`username, website, avatar_url`)
            .eq('id', user.id)
            .single()

          if (!ignore) {
            if (error) {
              console.warn(error)
            } else if (data) {
              setUsername(data.username)
              setWebsite(data.website)
              setAvatarUrl(data.avatar_url)
            }
          }

          setLoading(false)
        }

        getProfile()

        return () => {
          ignore = true
        }
      }, [session])

      async function updateProfile(event, avatarUrl) {
        event.preventDefault()

        setLoading(true)
        const { user } = session

        const updates = {
          id: user.id,
          username,
          website,
          avatar_url: avatarUrl,
          updated_at: new Date(),
        }

        const { error } = await supabase.from('profiles').upsert(updates)

        if (error) {
          alert(error.message)
        } else {
          setAvatarUrl(avatarUrl)
        }
        setLoading(false)
      }

      return (
        <form onSubmit={updateProfile} className="form-widget">
          <div>
            <label htmlFor="email">Email</label>
            <input id="email" type="text" value={session.user.email} disabled />
          </div>
          <div>
            <label htmlFor="username">Name</label>
            <input
              id="username"
              type="text"
              required
              value={username || ''}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div>
            <label htmlFor="website">Website</label>
            <input
              id="website"
              type="url"
              value={website || ''}
              onChange={(e) => setWebsite(e.target.value)}
            />
          </div>

          <div>
            <button className="button block primary" type="submit" disabled={loading}>
              {loading ? 'Loading ...' : 'Update'}
            </button>
          </div>

          <div>
            <button className="button block" type="button" onClick={() => supabase.auth.signOut()}>
              Sign Out
            </button>
          </div>
        </form>
      )
    }
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `src/App.jsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.jsx" label="src/App.jsx">
    ```jsx name=src/App.jsx
    import './App.css'
    import { useState, useEffect } from 'react'
    import { supabase } from './supabaseClient'
    import Auth from './Auth'
    import Account from './Account'

    function App() {
      const [session, setSession] = useState(null)

      useEffect(() => {
        supabase.auth.getSession().then(({ data: { session } }) => {
          setSession(session)
        })

        supabase.auth.onAuthStateChange((_event, session) => {
          setSession(session)
        })
      }, [])

      return (
        <div className="container" style={{ padding: '50px 0 100px 0' }}>
          {!session ? <Auth /> : <Account key={session.user.id} session={session} />}
        </div>
      )
    }

    export default App
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase React](/docs/img/supabase-react-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

Create and edit `src/Avatar.jsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Avatar.jsx" label="src/Avatar.jsx">
    ```jsx name=src/Avatar.jsx
    import { useEffect, useState } from 'react'
    import { supabase } from './supabaseClient'

    export default function Avatar({ url, size, onUpload }) {
      const [avatarUrl, setAvatarUrl] = useState(null)
      const [uploading, setUploading] = useState(false)

      useEffect(() => {
        if (url) downloadImage(url)
      }, [url])

      async function downloadImage(path) {
        try {
          const { data, error } = await supabase.storage.from('avatars').download(path)
          if (error) {
            throw error
          }
          const url = URL.createObjectURL(data)
          setAvatarUrl(url)
        } catch (error) {
          console.log('Error downloading image: ', error.message)
        }
      }

      async function uploadAvatar(event) {
        try {
          setUploading(true)

          if (!event.target.files || event.target.files.length === 0) {
            throw new Error('You must select an image to upload.')
          }

          const file = event.target.files[0]
          const fileExt = file.name.split('.').pop()
          const fileName = `${Math.random()}.${fileExt}`
          const filePath = `${fileName}`

          const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

          if (uploadError) {
            throw uploadError
          }

          onUpload(event, filePath)
        } catch (error) {
          alert(error.message)
        } finally {
          setUploading(false)
        }
      }

      return (
        <div>
          {avatarUrl ? (
            <img
              src={avatarUrl}
              alt="Avatar"
              className="avatar image"
              style={{ height: size, width: size }}
            />
          ) : (
            <div className="avatar no-image" style={{ height: size, width: size }} />
          )}
          <div style={{ width: size }}>
            <label className="button primary block" htmlFor="single">
              {uploading ? 'Uploading ...' : 'Upload'}
            </label>
            <input
              style={{
                visibility: 'hidden',
                position: 'absolute',
              }}
              type="file"
              id="single"
              accept="image/*"
              onChange={uploadAvatar}
              disabled={uploading}
            />
          </div>
        </div>
      )
    }
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page at `src/Account.jsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Account.jsx" label="src/Account.jsx">
    ```jsx name=src/Account.jsx
    // Import the new component
    import Avatar from './Avatar'

    // ...

    return (
      <form onSubmit={updateProfile} className="form-widget">
        {/* Add to the body */}
        <Avatar
          url={avatar_url}
          size={150}
          onUpload={(event, url) => {
            updateProfile(event, url)
          }}
        />
        {/* ... */}
      </form>
    )
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



# Build a User Management App with RedwoodJS



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/redwoodjs/redwoodjs-supabase-quickstart).
</Admonition>



## About RedwoodJS

A Redwood application is split into two parts: a frontend and a backend. This is represented as two node projects within a single monorepo.

The frontend project is called **`web`** and the backend project is called **`api`**. For clarity, we will refer to these in prose as **"sides,"** that is, the `web side` and the `api side`.
They are separate projects because code on the `web side` will end up running in the user's browser while code on the `api side` will run on a server somewhere.

<Admonition type="note">
  Important: When this guide refers to "API," that means the Supabase API and when it refers to `api side`, that means the RedwoodJS `api side`.
</Admonition>

The **`api side`** is an implementation of a GraphQL API. The business logic is organized into "services" that represent their own internal API and can be called both from external GraphQL requests and other internal services.

The **`web side`** is built with React. Redwood's router makes it simple to map URL paths to React "Page" components (and automatically code-split your app on each route).
Pages may contain a "Layout" component to wrap content. They also contain "Cells" and regular React components.
Cells allow you to declaratively manage the lifecycle of a component that fetches and displays data.

For the sake of consistency with the other framework tutorials, we'll build this app a little differently than normal.
We ***won't use*** Prisma to connect to the Supabase Postgres database or [Prisma migrations](https://redwoodjs.com/docs/cli-commands#prisma-migrate) as one typically might in a Redwood app.
Instead, we'll rely on the Supabase client to do some of the work on the **`web`** side and use the client again on the **`api`** side to do data fetching as well.

That means you will want to refrain from running any `yarn rw prisma migrate` commands and also double check your build commands on deployment to ensure Prisma won't reset your database. Prisma currently doesn't support cross-schema foreign keys, so introspecting the schema fails due
to how your Supabase `public` schema references the `auth.users`.



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

Let's start building the RedwoodJS app from scratch.

<Admonition type="note">
  RedwoodJS requires Node.js `>= 14.x <= 16.x` and Yarn `>= 1.15`.
</Admonition>

Make sure you have installed yarn since RedwoodJS relies on it to [manage its packages in workspaces](https://classic.yarnpkg.com/lang/en/docs/workspaces/) for its `web` and `api` "sides."


### Initialize a RedwoodJS app

We can use [Create Redwood App](https://redwoodjs.com/docs/quick-start) command to initialize
an app called `supabase-redwoodjs`:

```bash
yarn create redwood-app supabase-redwoodjs
cd supabase-redwoodjs
```

While the app is installing, you should see:

```bash
✔ Creating Redwood app
  ✔ Checking node and yarn compatibility
  ✔ Creating directory 'supabase-redwoodjs'
✔ Installing packages
  ✔ Running 'yarn install'... (This could take a while)
✔ Convert TypeScript files to JavaScript
✔ Generating types

Thanks for trying out Redwood!
```

Then let's install the only additional dependency [supabase-js](https://github.com/supabase/supabase-js) by running the `setup auth` command:

```bash
yarn redwood setup auth supabase
```

When prompted:

> Overwrite existing /api/src/lib/auth.\[jt]s?

Say, **yes** and it will setup the Supabase client in your app and also provide hooks used with Supabase authentication.

```bash
✔ Generating auth lib...
  ✔ Successfully wrote file `./api/src/lib/auth.js`
  ✔ Adding auth config to web...
  ✔ Adding auth config to GraphQL API...
  ✔ Adding required web packages...
  ✔ Installing packages...
  ✔ One more thing...

  You will need to add your Supabase URL (SUPABASE_URL), public API KEY,
  and JWT SECRET (SUPABASE_KEY, and SUPABASE_JWT_SECRET) to your .env file.
```

Next, we want to save the environment variables in a `.env`.
We need the `API URL` as well as the key and `jwt_secret` that you copied [earlier](#get-api-details).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    SUPABASE_URL=YOUR_SUPABASE_URL
    SUPABASE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
    SUPABASE_JWT_SECRET=YOUR_SUPABASE_JWT_SECRET
    ```
  </TabPanel>
</Tabs>

And finally, you will also need to save **just** the `web side` environment variables to the `redwood.toml`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="redwood.toml" label="redwood.toml">
    ```bash name=redwood.toml
    [web]
      title = "Supabase Redwood Tutorial"
      port = 8910
      apiProxyPath = "/.redwood/functions"
      includeEnvironmentVariables = ["SUPABASE_URL", "SUPABASE_KEY"]
    [api]
      port = 8911
    [browser]
      open = true
    ```
  </TabPanel>
</Tabs>

These variables will be exposed on the browser, and that's completely fine.
They allow your web app to initialize the Supabase client with your public anon key
since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

You'll see these being used to configure your Supabase client in `web/src/App.js`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/App.js" label="web/src/App.js">
    ```js name=web/src/App.js
    // ... Redwood imports
    import { AuthProvider } from '@redwoodjs/auth'
    import { createClient } from '@supabase/supabase-js'

    // ...

    const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY)

    const App = () => (
      <FatalErrorBoundary page={FatalErrorPage}>
        <RedwoodProvider titleTemplate="%PageTitle | %AppTitle">
          <AuthProvider client={supabase} type="supabase">
            <RedwoodApolloProvider>
              <Routes />
            </RedwoodApolloProvider>
          </AuthProvider>
        </RedwoodProvider>
      </FatalErrorBoundary>
    )

    export default App
    ```
  </TabPanel>
</Tabs>


### App styling (optional)

An optional step is to update the CSS file `web/src/index.css` to make the app look nice.
You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/react-user-management/src/index.css).


### Start RedwoodJS and your first page

Let's test our setup at the moment by starting up the app:

```bash
yarn rw dev
```

<Admonition type="note">
  `rw` is an alias for `redwood`, as in `yarn rw` to run Redwood CLI commands.
</Admonition>

You should see a "Welcome to RedwoodJS" page and a message about not having any pages yet.

So, let's create a "home" page:

```bash
yarn rw generate page home /

✔ Generating page files...
  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.stories.js`
  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.test.js`
  ✔ Successfully wrote file `./web/src/pages/HomePage/HomePage.js`
✔ Updating routes file...
✔ Generating types ...
```

<Admonition type="note">
  The `/` is important here as it creates a root level route.
</Admonition>

You can stop the `dev` server if you want; to see your changes, just be sure to run `yarn rw dev` again.

You should see the `Home` page route in `web/src/Routes.js`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/Routes.js" label="web/src/Routes.js">
    ```bash name=web/src/Routes.js
    import { Router, Route } from '@redwoodjs/router'

    const Routes = () => {
      return (
        <Router>
          <Route path="/" page={HomePage} name="home" />
          <Route notfound page={NotFoundPage} />
        </Router>
      )
    }

    export default Routes
    ```
  </TabPanel>
</Tabs>


### Set up a login component

Let's set up a Redwood component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

```bash
yarn rw g component auth

  ✔ Generating component files...
    ✔ Successfully wrote file `./web/src/components/Auth/Auth.test.js`
    ✔ Successfully wrote file `./web/src/components/Auth/Auth.stories.js`
    ✔ Successfully wrote file `./web/src/components/Auth/Auth.js`

```

Now, update the `Auth.js` component to contain:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="/web/src/components/Auth/Auth.js" label="/web/src/components/Auth/Auth.js">
    ```jsx name=/web/src/components/Auth/Auth.js
    import { useState } from 'react'
    import { useAuth } from '@redwoodjs/auth'

    const Auth = () => {
      const { logIn } = useAuth()
      const [loading, setLoading] = useState(false)
      const [email, setEmail] = useState('')

      const handleLogin = async (email) => {
        try {
          setLoading(true)
          const { error } = await logIn({ email })
          if (error) throw error
          alert('Check your email for the login link!')
        } catch (error) {
          alert(error.error_description || error.message)
        } finally {
          setLoading(false)
        }
      }

      return (
        <div className="row flex-center flex">
          <div className="col-6 form-widget">
            <h1 className="header">Supabase + RedwoodJS</h1>
            <p className="description">Sign in via magic link with your email below</p>
            <div>
              <input
                className="inputField"
                type="email"
                placeholder="Your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div>
              <button
                onClick={(e) => {
                  e.preventDefault()
                  handleLogin(email)
                }}
                className={'button block'}
                disabled={loading}
              >
                {loading ? <span>Loading</span> : <span>Send magic link</span>}
              </button>
            </div>
          </div>
        </div>
      )
    }

    export default Auth
    ```
  </TabPanel>
</Tabs>


### Set up an account component

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `Account.js`.

```bash
yarn rw g component account

  ✔ Generating component files...
    ✔ Successfully wrote file `./web/src/components/Account/Account.test.js`
    ✔ Successfully wrote file `./web/src/components/Account/Account.stories.js`
    ✔ Successfully wrote file `./web/src/components/Account/Account.js`
```

And then update the file to contain:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/components/Account/Account.js" label="web/src/components/Account/Account.js">
    ```jsx name=web/src/components/Account/Account.js
    import { useState, useEffect } from 'react'
    import { useAuth } from '@redwoodjs/auth'

    const Account = () => {
      const { client: supabase, currentUser, logOut } = useAuth()
      const [loading, setLoading] = useState(true)
      const [username, setUsername] = useState(null)
      const [website, setWebsite] = useState(null)
      const [avatar_url, setAvatarUrl] = useState(null)

      useEffect(() => {
        getProfile()
      }, [supabase.auth.session])

      async function getProfile() {
        try {
          setLoading(true)
          const user = supabase.auth.user()

          const { data, error, status } = await supabase
            .from('profiles')
            .select(`username, website, avatar_url`)
            .eq('id', user.id)
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
          alert(error.message)
        } finally {
          setLoading(false)
        }
      }

      async function updateProfile({ username, website, avatar_url }) {
        try {
          setLoading(true)
          const user = supabase.auth.user()

          const updates = {
            id: user.id,
            username,
            website,
            avatar_url,
            updated_at: new Date(),
          }

          const { error } = await supabase.from('profiles').upsert(updates, {
            returning: 'minimal', // Don't return the value after inserting
          })

          if (error) {
            throw error
          }

          alert('Updated profile!')
        } catch (error) {
          alert(error.message)
        } finally {
          setLoading(false)
        }
      }

      return (
        <div className="row flex-center flex">
          <div className="col-6 form-widget">
            <h1 className="header">Supabase + RedwoodJS</h1>
            <p className="description">Your profile</p>
            <div className="form-widget">
              <div>
                <label htmlFor="email">Email</label>
                <input id="email" type="text" value={currentUser.email} disabled />
              </div>
              <div>
                <label htmlFor="username">Name</label>
                <input
                  id="username"
                  type="text"
                  value={username || ''}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </div>
              <div>
                <label htmlFor="website">Website</label>
                <input
                  id="website"
                  type="url"
                  value={website || ''}
                  onChange={(e) => setWebsite(e.target.value)}
                />
              </div>

              <div>
                <button
                  className="button primary block"
                  onClick={() => updateProfile({ username, website, avatar_url })}
                  disabled={loading}
                >
                  {loading ? 'Loading ...' : 'Update'}
                </button>
              </div>

              <div>
                <button className="button block" onClick={() => logOut()}>
                  Sign Out
                </button>
              </div>
            </div>
          </div>
        </div>
      )
    }

    export default Account
    ```
  </TabPanel>
</Tabs>

You'll see the use of `useAuth()` several times. Redwood's `useAuth` hook provides convenient ways to access
`logIn`, `logOut`, `currentUser`, and access the `supabase` authenticate client. We'll use it to get an instance
of the Supabase client to interact with your API.


### Update home page

Now that we have all the components in place, let's update your `HomePage` page to use them:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/pages/HomePage/HomePage.js" label="web/src/pages/HomePage/HomePage.js">
    ```jsx name=web/src/pages/HomePage/HomePage.js
    import { useAuth } from '@redwoodjs/auth'
    import { MetaTags } from '@redwoodjs/web'

    import Account from 'src/components/Account'
    import Auth from 'src/components/Auth'

    const HomePage = () => {
      const { isAuthenticated } = useAuth()

      return (
        <>
          <MetaTags title="Welcome" />
          {!isAuthenticated ? <Auth /> : <Account />}
        </>
      )
    }

    export default HomePage
    ```
  </TabPanel>
</Tabs>

<Admonition type="note">
  What we're doing here is showing the sign in form if you aren't logged in and your account profile if you are.
</Admonition>


### Launch!

Once that's done, run this in a terminal window to launch the `dev` server:

```bash
yarn rw dev
```

And then open the browser to [localhost:8910](http://localhost:8910) and you should see the completed app.

![Supabase RedwoodJS](/docs/img/supabase-redwoodjs-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

```bash
yarn rw g component avatar
  ✔ Generating component files...
    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.test.js`
    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.stories.js`
    ✔ Successfully wrote file `./web/src/components/Avatar/Avatar.js`
```

Now, update your Avatar component to contain the following widget:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/components/Avatar/Avatar.js" label="web/src/components/Avatar/Avatar.js">
    ```jsx name=web/src/components/Avatar/Avatar.js
    import { useEffect, useState } from 'react'
    import { useAuth } from '@redwoodjs/auth'

    const Avatar = ({ url, size, onUpload }) => {
      const { client: supabase } = useAuth()

      const [avatarUrl, setAvatarUrl] = useState(null)
      const [uploading, setUploading] = useState(false)

      useEffect(() => {
        if (url) downloadImage(url)
      }, [url])

      async function downloadImage(path) {
        try {
          const { data, error } = await supabase.storage.from('avatars').download(path)
          if (error) {
            throw error
          }
          const url = URL.createObjectURL(data)
          setAvatarUrl(url)
        } catch (error) {
          console.log('Error downloading image: ', error.message)
        }
      }

      async function uploadAvatar(event) {
        try {
          setUploading(true)

          if (!event.target.files || event.target.files.length === 0) {
            throw new Error('You must select an image to upload.')
          }

          const file = event.target.files[0]
          const fileExt = file.name.split('.').pop()
          const fileName = `${Math.random()}.${fileExt}`
          const filePath = `${fileName}`

          const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

          if (uploadError) {
            throw uploadError
          }

          onUpload(filePath)
        } catch (error) {
          alert(error.message)
        } finally {
          setUploading(false)
        }
      }

      return (
        <div>
          {avatarUrl ? (
            <img
              src={avatarUrl}
              alt="Avatar"
              className="avatar image"
              style={{ height: size, width: size }}
            />
          ) : (
            <div className="avatar no-image" style={{ height: size, width: size }} />
          )}
          <div style={{ width: size }}>
            <label className="button primary block" htmlFor="single">
              {uploading ? 'Uploading ...' : 'Upload'}
            </label>
            <input
              style={{
                visibility: 'hidden',
                position: 'absolute',
              }}
              type="file"
              id="single"
              accept="image/*"
              onChange={uploadAvatar}
              disabled={uploading}
            />
          </div>
        </div>
      )
    }

    export default Avatar
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="web/src/components/Account/Account.js" label="web/src/components/Account/Account.js">
    ```jsx name=web/src/components/Account/Account.js
    // Import the new component
    import Avatar from 'src/components/Avatar'

    // ...

    return (
      <div className="form-widget">
        {/* Add to the body */}
        <Avatar
          url={avatar_url}
          size={150}
          onUpload={(url) => {
            setAvatarUrl(url)
            updateProfile({ username, website, avatar_url: url })
          }}
        />
        {/* ... */}
      </div>
    )
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



## See also

*   Learn more about [RedwoodJS](https://redwoodjs.com)
*   Visit the [RedwoodJS Discourse Community](https://community.redwoodjs.com)



# Build a User Management App with refine



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/refine-user-management).
</Admonition>



## About refine

[refine](https://github.com/refinedev/refine) is a React-based framework used to rapidly build data-heavy applications like admin panels, dashboards, storefronts and any type of CRUD apps. It separates app concerns into individual layers, each backed by a React context and respective provider object. For example, the auth layer represents a context served by a specific set of [`authProvider`](https://refine.dev/docs/tutorial/understanding-authprovider/index/) methods that carry out authentication and authorization actions such as logging in, logging out, getting roles data, etc. Similarly, the data layer offers another level of abstraction that is equipped with [`dataProvider`](https://refine.dev/docs/tutorial/understanding-dataprovider/index/) methods to handle CRUD operations at appropriate backend API endpoints.

refine provides hassle-free integration with Supabase backend with its supplementary [`@refinedev/supabase`](https://github.com/refinedev/refine/tree/master/packages/supabase) package. It generates `authProvider` and `dataProvider` methods at project initialization, so we don't need to expend much effort to define them ourselves. We just need to choose Supabase as our backend service while creating the app with `create refine-app`.

<Admonition type="note">
  It is possible to customize the `authProvider` for Supabase and as we'll see below, it can be tweaked from `src/authProvider.ts` file. In contrast, the Supabase `dataProvider` is part of `node_modules` and therefore is not subject to modification.
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

Let's start building the refine app from scratch.


### Initialize a refine app

We can use [create refine-app](https://refine.dev/docs/tutorial/getting-started/headless/create-project/#launch-the-refine-cli-setup) command to initialize
an app. Run the following in the terminal:

```bash
npm create refine-app@latest -- --preset refine-supabase
```

In the above command, we are using the `refine-supabase` preset which chooses the Supabase supplementary package for our app. We are not using any UI framework, so we'll have a headless UI with plain React and CSS styling.

The `refine-supabase` preset installs the `@refinedev/supabase` package which out-of-the-box includes the Supabase dependency: [supabase-js](https://github.com/supabase/supabase-js).

We also need to install `@refinedev/react-hook-form` and `react-hook-form` packages that allow us to use [React Hook Form](https://react-hook-form.com) inside refine apps. Run:

```bash
npm install @refinedev/react-hook-form react-hook-form
```

With the app initialized and packages installed, at this point before we begin discussing refine concepts, let's try running the app:

```bash
cd app-name
npm run dev
```

We should have a running instance of the app with a Welcome page at `http://localhost:5173`.

Let's move ahead to understand the generated code now.


### Refine `supabaseClient`

The `create refine-app` generated a Supabase client for us in the `src/utility/supabaseClient.ts` file. It has two constants: `SUPABASE_URL` and `SUPABASE_KEY`. We want to replace them as `supabaseUrl` and `supabasePublishableKey` respectively and assign them our own Supabase server's values.

We'll update it with environment variables managed by Vite:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/utility/supabaseClient.ts" label="src/utility/supabaseClient.ts">
    ```ts name=src/utility/supabaseClient.ts
    import { createClient } from '@refinedev/supabase'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

    export const supabaseClient = createClient(supabaseUrl, supabasePublishableKey, {
      db: {
        schema: 'public',
      },
      auth: {
        persistSession: true,
      },
    })
    ```
  </TabPanel>
</Tabs>

And then, we want to save the environment variables in a `.env.local` file. All you need are the API URL and the key that you copied [earlier](#get-api-details).

```bash .env.local
VITE_SUPABASE_URL=YOUR_SUPABASE_URL
VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```

The `supabaseClient` will be used in fetch calls to Supabase endpoints from our app. As we'll see below, the client is instrumental in implementing authentication using Refine's auth provider methods and CRUD actions with appropriate data provider methods.

One optional step is to update the CSS file `src/App.css` to make the app look nice.
You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/refine-user-management/src/App.css).

In order for us to add login and user profile pages in this App, we have to tweak the `<Refine />` component inside `App.tsx`.


### The `<Refine />` component

The `App.tsx` file initially looks like this:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.tsx" label="src/App.tsx">
    ```tsx name=src/App.tsx
    import { Refine, WelcomePage } from '@refinedev/core'
    import { RefineKbar, RefineKbarProvider } from '@refinedev/kbar'
    import routerBindings, {
      DocumentTitleHandler,
      UnsavedChangesNotifier,
    } from '@refinedev/react-router-v6'
    import { dataProvider, liveProvider } from '@refinedev/supabase'
    import { BrowserRouter, Route, Routes } from 'react-router-dom'

    import './App.css'
    import authProvider from './authProvider'
    import { supabaseClient } from './utility'

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
            >
              <Routes>
                <Route index element={<WelcomePage />} />
              </Routes>
              <RefineKbar />
              <UnsavedChangesNotifier />
              <DocumentTitleHandler />
            </Refine>
          </RefineKbarProvider>
        </BrowserRouter>
      )
    }

    export default App
    ```
  </TabPanel>
</Tabs>

We'd like to focus on the [`<Refine />`](https://refine.dev/docs/api-reference/core/components/refine-config/) component, which comes with several props passed to it. Notice the `dataProvider` prop. It uses a `dataProvider()` function with `supabaseClient` passed as argument to generate the data provider object. The `authProvider` object also uses `supabaseClient` in implementing its methods. You can look it up in `src/authProvider.ts` file.



## Customize `authProvider`

If you examine the `authProvider` object you can notice that it has a `login` method that implements a OAuth and Email / Password strategy for authentication. We'll, however, remove them and use Magic Links to allow users sign in with their email without using passwords.

We want to use `supabaseClient` auth's `signInWithOtp` method inside `authProvider.login` method:

<NamedCodeBlock name="src/authProvider.ts">
  ```ts name=src/authProvider.ts
  login: async ({ email }) => {
    try {
      const { error } = await supabaseClient.auth.signInWithOtp({ email });

      if (!error) {
        alert("Check your email for the login link!");
        return {
          success: true,
        };
      };

      throw error;
    } catch (e: any) {
      alert(e.message);
      return {
        success: false,
        e,
      };
    }
  },
  ```
</NamedCodeBlock>

We also want to remove `register`, `updatePassword`, `forgotPassword` and `getPermissions` properties, which are optional type members and also not necessary for our app. The final `authProvider` object looks like this:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/authProvider.ts" label="src/authProvider.ts">
    ```ts name=src/authProvider.ts
    import { AuthBindings } from '@refinedev/core'

    import { supabaseClient } from './utility'

    const authProvider: AuthBindings = {
      login: async ({ email }) => {
        try {
          const { error } = await supabaseClient.auth.signInWithOtp({ email })

          if (!error) {
            alert('Check your email for the login link!')
            return {
              success: true,
            }
          }

          throw error
        } catch (e: any) {
          alert(e.message)
          return {
            success: false,
            e,
          }
        }
      },
      logout: async () => {
        const { error } = await supabaseClient.auth.signOut()

        if (error) {
          return {
            success: false,
            error,
          }
        }

        return {
          success: true,
          redirectTo: '/',
        }
      },
      onError: async (error) => {
        console.error(error)
        return { error }
      },
      check: async () => {
        try {
          const { data } = await supabaseClient.auth.getSession()
          const { session } = data

          if (!session) {
            return {
              authenticated: false,
              error: {
                message: 'Check failed',
                name: 'Session not found',
              },
              logout: true,
              redirectTo: '/login',
            }
          }
        } catch (error: any) {
          return {
            authenticated: false,
            error: error || {
              message: 'Check failed',
              name: 'Not authenticated',
            },
            logout: true,
            redirectTo: '/login',
          }
        }

        return {
          authenticated: true,
        }
      },
      getIdentity: async () => {
        const { data } = await supabaseClient.auth.getUser()

        if (data?.user) {
          return {
            ...data.user,
            name: data.user.email,
          }
        }

        return null
      },
    }

    export default authProvider
    ```
  </TabPanel>
</Tabs>


### Set up a login component

We have chosen to use the headless refine core package that comes with no supported UI framework. So, let's set up a plain React component to manage logins and sign ups.

Create and edit `src/components/auth.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/auth.tsx" label="src/components/auth.tsx">
    ```ts name=src/components/auth.tsx
    import { useState } from 'react'
    import { useLogin } from '@refinedev/core'

    export default function Auth() {
      const [email, setEmail] = useState('')
      const { isLoading, mutate: login } = useLogin()

      const handleLogin = async (event: { preventDefault: () => void }) => {
        event.preventDefault()
        login({ email })
      }

      return (
        <div className="row flex flex-center container">
          <div className="col-6 form-widget">
            <h1 className="header">Supabase + refine</h1>
            <p className="description">Sign in via magic link with your email below</p>
            <form className="form-widget" onSubmit={handleLogin}>
              <div>
                <input
                  className="inputField"
                  type="email"
                  placeholder="Your email"
                  value={email}
                  required={true}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div>
                <button className={'button block'} disabled={isLoading}>
                  {isLoading ? <span>Loading</span> : <span>Send magic link</span>}
                </button>
              </div>
            </form>
          </div>
        </div>
      )
    }
    ```
  </TabPanel>
</Tabs>

Notice we are using the [`useLogin()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogin/) refine auth hook to grab the `mutate: login` method to use inside `handleLogin()` function and `isLoading` state for our form submission. The `useLogin()` hook conveniently offers us access to `authProvider.login` method for authenticating the user with OTP.


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that in `src/components/account.tsx`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/account.tsx" label="src/components/account.tsx">
    ```tsx name=src/components/account.tsx
    import { BaseKey, useGetIdentity, useLogout } from '@refinedev/core'
    import { useForm } from '@refinedev/react-hook-form'

    interface IUserIdentity {
      id?: BaseKey
      username: string
      name: string
    }

    export interface IProfile {
      id?: string
      username?: string
      website?: string
      avatar_url?: string
    }

    export default function Account() {
      const { data: userIdentity } = useGetIdentity<IUserIdentity>()

      const { mutate: logOut } = useLogout()

      const {
        refineCore: { formLoading, queryResult, onFinish },
        register,
        control,
        handleSubmit,
      } = useForm<IProfile>({
        refineCoreProps: {
          resource: 'profiles',
          action: 'edit',
          id: userIdentity?.id,
          redirect: false,
          onMutationError: (data) => alert(data?.message),
        },
      })

      return (
        <div className="container" style={{ padding: '50px 0 100px 0' }}>
          <form onSubmit={handleSubmit(onFinish)} className="form-widget">
            <div>
              <label htmlFor="email">Email</label>
              <input id="email" name="email" type="text" value={userIdentity?.name} disabled />
            </div>
            <div>
              <label htmlFor="username">Name</label>
              <input id="username" type="text" {...register('username')} />
            </div>
            <div>
              <label htmlFor="website">Website</label>
              <input id="website" type="url" {...register('website')} />
            </div>

            <div>
              <button className="button block primary" type="submit" disabled={formLoading}>
                {formLoading ? 'Loading ...' : 'Update'}
              </button>
            </div>

            <div>
              <button className="button block" type="button" onClick={() => logOut()}>
                Sign Out
              </button>
            </div>
          </form>
        </div>
      )
    }
    ```
  </TabPanel>
</Tabs>

Notice above that, we are using three refine hooks, namely the [`useGetIdentity()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useGetIdentity/), [`useLogOut()`](https://refine.dev/docs/api-reference/core/hooks/authentication/useLogout/) and [`useForm()`](https://refine.dev/docs/packages/documentation/react-hook-form/useForm/) hooks.

`useGetIdentity()` is a auth hook that gets the identity of the authenticated user. It grabs the current user by invoking the `authProvider.getIdentity` method under the hood.

`useLogOut()` is also an auth hook. It calls the `authProvider.logout` method to end the session.

`useForm()`, in contrast, is a data hook that exposes a series of useful objects that serve the edit form. For example, we are grabbing the `onFinish` function to submit the form with the `handleSubmit` event handler. We are also using `formLoading` property to present state changes of the submitted form.

The `useForm()` hook is a higher-level hook built on top of Refine's `useForm()` core hook. It fully supports form state management, field validation and submission using React Hook Form. Behind the scenes, it invokes the `dataProvider.getOne` method to get the user profile data from our Supabase `/profiles` endpoint and also invokes `dataProvider.update` method when `onFinish()` is called.


### Launch!

Now that we have all the components in place, let's define the routes for the pages in which they should be rendered.

Add the routes for `/login` with the `<Auth />` component and the routes for `index` path with the `<Account />` component. So, the final `App.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.tsx" label="src/App.tsx">
    ```tsx name=src/App.tsx
    import { Authenticated, Refine } from '@refinedev/core'
    import { RefineKbar, RefineKbarProvider } from '@refinedev/kbar'
    import routerBindings, {
      CatchAllNavigate,
      DocumentTitleHandler,
      UnsavedChangesNotifier,
    } from '@refinedev/react-router-v6'
    import { dataProvider, liveProvider } from '@refinedev/supabase'
    import { BrowserRouter, Outlet, Route, Routes } from 'react-router-dom'

    import './App.css'
    import authProvider from './authProvider'
    import { supabaseClient } from './utility'
    import Account from './components/account'
    import Auth from './components/auth'

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
            >
              <Routes>
                <Route
                  element={
                    <Authenticated fallback={<CatchAllNavigate to="/login" />}>
                      <Outlet />
                    </Authenticated>
                  }
                >
                  <Route index element={<Account />} />
                </Route>
                <Route element={<Authenticated fallback={<Outlet />} />}>
                  <Route path="/login" element={<Auth />} />
                </Route>
              </Routes>
              <RefineKbar />
              <UnsavedChangesNotifier />
              <DocumentTitleHandler />
            </Refine>
          </RefineKbarProvider>
        </BrowserRouter>
      )
    }

    export default App
    ```
  </TabPanel>
</Tabs>

Let's test the App by running the server again:

```bash
npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase refine](/docs/img/supabase-refine-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

Create and edit `src/components/avatar.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/avatar.tsx" label="src/components/avatar.tsx">
    ```tsx name=src/components/avatar.tsx
    import { useEffect, useState } from 'react'
    import { supabaseClient } from '../utility/supabaseClient'

    type TAvatarProps = {
      url?: string
      size: number
      onUpload: (filePath: string) => void
    }

    export default function Avatar({ url, size, onUpload }: TAvatarProps) {
      const [avatarUrl, setAvatarUrl] = useState('')
      const [uploading, setUploading] = useState(false)

      useEffect(() => {
        if (url) downloadImage(url)
      }, [url])

      async function downloadImage(path: string) {
        try {
          const { data, error } = await supabaseClient.storage.from('avatars').download(path)
          if (error) {
            throw error
          }
          const url = URL.createObjectURL(data)
          setAvatarUrl(url)
        } catch (error: any) {
          console.log('Error downloading image: ', error?.message)
        }
      }

      async function uploadAvatar(event: React.ChangeEvent<HTMLInputElement>) {
        try {
          setUploading(true)

          if (!event.target.files || event.target.files.length === 0) {
            throw new Error('You must select an image to upload.')
          }

          const file = event.target.files[0]
          const fileExt = file.name.split('.').pop()
          const fileName = `${Math.random()}.${fileExt}`
          const filePath = `${fileName}`

          const { error: uploadError } = await supabaseClient.storage
            .from('avatars')
            .upload(filePath, file)

          if (uploadError) {
            throw uploadError
          }
          onUpload(filePath)
        } catch (error: any) {
          alert(error.message)
        } finally {
          setUploading(false)
        }
      }

      return (
        <div>
          {avatarUrl ? (
            <img
              src={avatarUrl}
              alt="Avatar"
              className="avatar image"
              style={{ height: size, width: size }}
            />
          ) : (
            <div className="avatar no-image" style={{ height: size, width: size }} />
          )}
          <div style={{ width: size }}>
            <label className="button primary block" htmlFor="single">
              {uploading ? 'Uploading ...' : 'Upload'}
            </label>
            <input
              style={{
                visibility: 'hidden',
                position: 'absolute',
              }}
              type="file"
              id="single"
              name="avatar_url"
              accept="image/*"
              onChange={uploadAvatar}
              disabled={uploading}
            />
          </div>
        </div>
      )
    }
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page at `src/components/account.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/account.tsx" label="src/components/account.tsx">
    ```tsx name=src/components/account.tsx
    // Import the new components
    import { Controller } from 'react-hook-form'
    import Avatar from './avatar'

    // ...

    return (
      <div className="container" style={{ padding: '50px 0 100px 0' }}>
        <form onSubmit={handleSubmit} className="form-widget">
          <Controller
            control={control}
            name="avatar_url"
            render={({ field }) => {
              return (
                <Avatar
                  url={field.value}
                  size={150}
                  onUpload={(filePath) => {
                    onFinish({
                      ...queryResult?.data?.data,
                      avatar_url: filePath,
                      onMutationError: (data: { message: string }) => alert(data?.message),
                    })
                    field.onChange({
                      target: {
                        value: filePath,
                      },
                    })
                  }}
                />
              )
            }}
          />
          {/* ... */}
        </form>
      </div>
    )
    ```
  </TabPanel>
</Tabs>

At this stage, you have a fully functional application!



---
**Navigation:** [← Previous](./14-build-a-user-management-app-with-ionic-vue.md) | [Index](./index.md) | [Next →](./16-build-a-user-management-app-with-solidjs.md)
