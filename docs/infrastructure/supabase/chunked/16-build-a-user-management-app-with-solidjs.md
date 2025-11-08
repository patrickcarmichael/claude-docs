**Navigation:** [← Previous](./15-build-a-user-management-app-with-nuxt-3.md) | [Index](./index.md) | [Next →](./17-build-a-user-management-app-with-vue-3.md)

# Build a User Management App with SolidJS



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/solid-user-management).
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

Let's start building the SolidJS app from scratch.


### Initialize a SolidJS app

We can use [degit](https://github.com/Rich-Harris/degit) to initialize an app called `supabase-solid`:

```bash
npx degit solidjs/templates/ts supabase-solid
cd supabase-solid
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
  <TabPanel id="src/supabaseClient.tsx" label="src/supabaseClient.tsx">
    ```tsx name=src/supabaseClient.tsx
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

    export const supabase = createClient(supabaseUrl, supabasePublishableKey)
    ```
  </TabPanel>
</Tabs>


### App styling (optional)

An optional step is to update the CSS file `src/index.css` to make the app look nice.
You can find the full contents of this file [here](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/solid-user-management/src/index.css).


### Set up a login component

Let's set up a SolidJS component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Auth.tsx" label="src/Auth.tsx">
    ```jsx name=src/Auth.tsx
    import { createSignal } from 'solid-js'
    import { supabase } from './supabaseClient'

    export default function Auth() {
      const [loading, setLoading] = createSignal(false)
      const [email, setEmail] = createSignal('')

      const handleLogin = async (e: SubmitEvent) => {
        e.preventDefault()

        try {
          setLoading(true)
          const { error } = await supabase.auth.signInWithOtp({ email: email() })
          if (error) throw error
          alert('Check your email for the login link!')
        } catch (error) {
          if (error instanceof Error) {
            alert(error.message)
          }
        } finally {
          setLoading(false)
        }
      }

      return (
        <div class="row flex-center flex">
          <div class="col-6 form-widget" aria-live="polite">
            <h1 class="header">Supabase + SolidJS</h1>
            <p class="description">Sign in via magic link with your email below</p>
            <form class="form-widget" onSubmit={handleLogin}>
              <div>
                <label for="email">Email</label>
                <input
                  id="email"
                  class="inputField"
                  type="email"
                  placeholder="Your email"
                  value={email()}
                  onChange={(e) => setEmail(e.currentTarget.value)}
                />
              </div>
              <div>
                <button type="submit" class="button block" aria-live="polite">
                  {loading() ? <span>Loading</span> : <span>Send magic link</span>}
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

Let's create a new component for that called `Account.tsx`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Account.tsx" label="src/Account.tsx">
    ```tsx name=src/Account.tsx
    import { AuthSession } from '@supabase/supabase-js'
    import { Component, createEffect, createSignal } from 'solid-js'
    import { supabase } from './supabaseClient'

    interface Props {
      session: AuthSession
    }

    const Account: Component<Props> = ({ session }) => {
      const [loading, setLoading] = createSignal(true)
      const [username, setUsername] = createSignal<string | null>(null)
      const [website, setWebsite] = createSignal<string | null>(null)
      const [avatarUrl, setAvatarUrl] = createSignal<string | null>(null)

      createEffect(() => {
        getProfile()
      })

      const getProfile = async () => {
        try {
          setLoading(true)
          const { user } = session

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
          if (error instanceof Error) {
            alert(error.message)
          }
        } finally {
          setLoading(false)
        }
      }

      const updateProfile = async (e: Event) => {
        e.preventDefault()

        try {
          setLoading(true)
          const { user } = session

          const updates = {
            id: user.id,
            username: username(),
            website: website(),
            avatar_url: avatarUrl(),
            updated_at: new Date().toISOString(),
          }

          const { error } = await supabase.from('profiles').upsert(updates)

          if (error) {
            throw error
          }
        } catch (error) {
          if (error instanceof Error) {
            alert(error.message)
          }
        } finally {
          setLoading(false)
        }
      }

      return (
        <div aria-live="polite">
          <form onSubmit={updateProfile} class="form-widget">
            <div>Email: {session.user.email}</div>
            <div>
              <label for="username">Name</label>
              <input
                id="username"
                type="text"
                value={username() || ''}
                onChange={(e) => setUsername(e.currentTarget.value)}
              />
            </div>
            <div>
              <label for="website">Website</label>
              <input
                id="website"
                type="text"
                value={website() || ''}
                onChange={(e) => setWebsite(e.currentTarget.value)}
              />
            </div>
            <div>
              <button type="submit" class="button primary block" disabled={loading()}>
                {loading() ? 'Saving ...' : 'Update profile'}
              </button>
            </div>
            <button type="button" class="button block" onClick={() => supabase.auth.signOut()}>
              Sign Out
            </button>
          </form>
        </div>
      )
    }

    export default Account
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `App.tsx`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/App.tsx" label="src/App.tsx">
    ```jsx name=src/App.tsx
    import { Component, createEffect, createSignal } from 'solid-js'
    import { supabase } from './supabaseClient'
    import { AuthSession } from '@supabase/supabase-js'
    import Account from './Account'
    import Auth from './Auth'

    const App: Component = () => {
      const [session, setSession] = createSignal<AuthSession | null>(null)

      createEffect(() => {
        supabase.auth.getSession().then(({ data: { session } }) => {
          setSession(session)
        })

        supabase.auth.onAuthStateChange((_event, session) => {
          setSession(session)
        })
      })

      return (
        <div class="container" style={{ padding: '50px 0 100px 0' }}>
          {!session() ? <Auth /> : <Account session={session()!} />}
        </div>
      )
    }

    export default App
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
npm start
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase SolidJS](/docs/img/supabase-solidjs-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Let's create an avatar for the user so that they can upload a profile photo. We can start by creating a new component:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Avatar.tsx" label="src/Avatar.tsx">
    ```jsx name=src/Avatar.tsx
    import { Component, createEffect, createSignal, JSX } from 'solid-js'
    import { supabase } from './supabaseClient'

    interface Props {
      size: number
      url: string | null
      onUpload: (event: Event, filePath: string) => void
    }

    const Avatar: Component<Props> = (props) => {
      const [avatarUrl, setAvatarUrl] = createSignal<string | null>(null)
      const [uploading, setUploading] = createSignal(false)

      createEffect(() => {
        if (props.url) downloadImage(props.url)
      })

      const downloadImage = async (path: string) => {
        try {
          const { data, error } = await supabase.storage.from('avatars').download(path)
          if (error) {
            throw error
          }
          const url = URL.createObjectURL(data)
          setAvatarUrl(url)
        } catch (error) {
          if (error instanceof Error) {
            console.log('Error downloading image: ', error.message)
          }
        }
      }

      const uploadAvatar: JSX.EventHandler<HTMLInputElement, Event> = async (event) => {
        try {
          setUploading(true)

          const target = event.currentTarget
          if (!target?.files || target.files.length === 0) {
            throw new Error('You must select an image to upload.')
          }

          const file = target.files[0]
          const fileExt = file.name.split('.').pop()
          const fileName = `${Math.random()}.${fileExt}`
          const filePath = `${fileName}`

          const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

          if (uploadError) {
            throw uploadError
          }

          props.onUpload(event, filePath)
        } catch (error) {
          if (error instanceof Error) {
            alert(error.message)
          }
        } finally {
          setUploading(false)
        }
      }

      return (
        <div style={{ width: `${props.size}px` }} aria-live="polite">
          {avatarUrl() ? (
            <img
              src={avatarUrl()!}
              alt={avatarUrl() ? 'Avatar' : 'No image'}
              class="avatar image"
              style={{ height: `${props.size}px`, width: `${props.size}px` }}
            />
          ) : (
            <div
              class="avatar no-image"
              style={{ height: `${props.size}px`, width: `${props.size}px` }}
            />
          )}
          <div style={{ width: `${props.size}px` }}>
            <label class="button primary block" for="single">
              {uploading() ? 'Uploading ...' : 'Upload avatar'}
            </label>
            <span style="display:none">
              <input
                type="file"
                id="single"
                accept="image/*"
                onChange={uploadAvatar}
                disabled={uploading()}
              />
            </span>
          </div>
        </div>
      )
    }

    export default Avatar
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/Account.tsx" label="src/Account.tsx">
    ```jsx name=src/Account.tsx
    // Import the new component
    import Avatar from './Avatar'

    // ...

    return (
      <form onSubmit={updateProfile} class="form-widget">
        {/* Add to the body */}
        <Avatar
          url={avatarUrl()}
          size={150}
          onUpload={(e: Event, url: string) => {
            setAvatarUrl(url)
            updateProfile(e)
          }}
        />
        {/* ... */}
      </div>
    )
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



# Build a User Management App with Svelte



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/svelte-user-management).
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

Start building the Svelte app from scratch.


### Initialize a Svelte app

You can use the Vite Svelte TypeScript Template to initialize an app called `supabase-svelte`:

```bash
npm create vite@latest supabase-svelte -- --template svelte-ts
cd supabase-svelte
npm install
```

Install the only additional dependency: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npm install @supabase/supabase-js
```

Finally, save the environment variables in a `.env`.
All you need are the API URL and the key that you copied [earlier](#get-api-details).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    VITE_SUPABASE_URL=YOUR_SUPABASE_URL
    VITE_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
    ```
  </TabPanel>
</Tabs>

Now you have the API credentials in place, create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's fine since you have [Row Level Security](/docs/guides/auth#row-level-security) enabled on the Database.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/supabaseClient.ts">
  <NamedCodeBlock name="src/supabaseClient.ts">
    ```typescript name=src/supabaseClient.ts
    import { createClient } from '@supabase/supabase-js'

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY

    export const supabase = createClient(supabaseUrl, supabasePublishableKey)
    ```
  </NamedCodeBlock>
</CodeSampleWrapper>


### App styling (optional)

Optionally, update the CSS file `src/app.css` to make the app look nice.
You can find the full contents of this file [on GitHub](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/svelte-user-management/src/app.css).


### Set up a login component

Set up a Svelte component to manage logins and sign ups. It uses Magic Links, so users can sign in with their email without using passwords.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/lib/Auth.svelte">
  <NamedCodeBlock name="src/lib/Auth.svelte">
    ```svelte name=src/lib/Auth.svelte
    <script lang="ts">
      import { supabase } from "../supabaseClient";

      let loading = $state(false);
      let email = $state("");

      const handleLogin = async () => {
        try {
          loading = true;
          const { error } = await supabase.auth.signInWithOtp({ email });
          if (error) throw error;
          alert("Check your email for login link!");
        } catch (error) {
          if (error instanceof Error) {
            alert(error.message);
          }
        } finally {
          loading = false;
        }
      };
    </script>

    <div class="row flex-center flex">
      <div class="col-6 form-widget" aria-live="polite">
        <h1 class="header">Supabase + Svelte</h1>
        <p class="description">Sign in via magic link with your email below</p>
        <form class="form-widget" onsubmit={(e) => { e.preventDefault(); handleLogin(); }}>
          <div>
            <label for="email">Email</label>
            <input
              id="email"
              class="inputField"
              type="email"
              placeholder="Your email"
              bind:value={email}
            />
          </div>
          <div>
            <button
              type="submit"
              class="button block"
              aria-live="polite"
              disabled={loading}
            >
              <span>{loading ? "Loading" : "Send magic link"}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
    ```
  </NamedCodeBlock>
</CodeSampleWrapper>


### Account page

After a user is signed in, allow them to edit their profile details and manage their account.
Create a new component for that called `Account.svelte`.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/lib/Account.svelte">
  ```svelte src/lib/Account.svelte
  <script lang="ts">
    import { onMount } from "svelte";
    import type { AuthSession } from "@supabase/supabase-js";
    import { supabase } from "../supabaseClient";

    // ...

    interface Props {
      session: AuthSession;
    }

    let { session }: Props = $props();

    // ...

    let username = $state<string | null>(null);
    let website = $state<string | null>(null);
    let avatarUrl = $state<string | null>(null);

    onMount(() => {
      getProfile();
    });

    const getProfile = async () => {
      try {
        loading = true;
        const { user } = session;

        const { data, error, status } = await supabase
          .from("profiles")
          .select("username, website, avatar_url")
          .eq("id", user.id)
          .single();

        if (error && status !== 406) throw error;

  // ...


        if (data) {
          username = data.username;
          website = data.website;
          avatarUrl = data.avatar_url;
        }
      } catch (error) {
        if (error instanceof Error) {
          alert(error.message);
        }
      } finally {
        loading = false;
      }
    };

    const updateProfile = async () => {
      try {
        loading = true;
        const { user } = session;


          // ...

          id: user.id,
          username,
          website,
          avatar_url: avatarUrl,
          updated_at: new Date().toISOString(),
        };

        const { error } = await supabase.from("profiles").upsert(updates);

        if (error) {
          throw error;
        }
      } catch (error) {
        if (error instanceof Error) {
          alert(error.message);
        }
      } finally {
        loading = false;
      }

  // ...

  </script>

  <form onsubmit={(e) => { e.preventDefault(); updateProfile(); }} class="form-widget">
    <div>Email: {session.user.email}</div>
    <div>
      <Avatar bind:url={avatarUrl} size={150} onupload={updateProfile} />
      <label for="username">Name</label>
      <input id="username" type="text" bind:value={username} />
    </div>
    <div>
      <label for="website">Website</label>
      <input id="website" type="text" bind:value={website} />
    </div>
    <div>
      <button type="submit" class="button primary block" disabled={loading}>
        {loading ? "Saving ..." : "Update profile"}
      </button>
    </div>
    <button
      type="button"
      class="button block"
      onclick={() => supabase.auth.signOut()}
    >
      Sign Out
    </button>
  </form>
  ```
</CodeSampleWrapper>


### Launch!

Now that you have all the components in place, update `App.svelte`:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/App.svelte">
  <NamedCodeBlock name="src/App.svelte">
    ```svelte name=src/App.svelte
    <script lang="ts">
      import { onMount } from 'svelte'
      import { supabase } from './supabaseClient'
      import type { AuthSession } from '@supabase/supabase-js'
      import Account from './lib/Account.svelte'
      import Auth from './lib/Auth.svelte'

      let session = $state<AuthSession | null>(null)

      onMount(() => {
        supabase.auth.getSession().then(({ data }) => {
          session = data.session
        })

        supabase.auth.onAuthStateChange((_event, _session) => {
          session = _session
        })
      })
    </script>

    <div class="container" style="padding: 50px 0 100px 0">
      {#if !session}
      <Auth />
      {:else}
      <Account {session} />
      {/if}
    </div>
    ```
  </NamedCodeBlock>
</CodeSampleWrapper>

Once that's done, run this in a terminal window:

```bash
npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

<Admonition type="tip">
  Svelte uses Vite and the default port is `5173`, Supabase uses `port 3000`. To change the redirection port for Supabase go to: **Authentication > URL Configuration** and change the **Site URL** to `http://localhost:5173/`
</Admonition>

![Supabase Svelte](/docs/img/supabase-svelte-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/lib/Avatar.svelte">
  <NamedCodeBlock name="src/lib/Avatar.svelte">
    ```svelte name=src/lib/Avatar.svelte
    <script lang="ts">
      import { supabase } from "../supabaseClient";

      interface Props {
        size: number;
        url?: string | null;
        onupload?: () => void;
      }

      let { size, url = $bindable(null), onupload }: Props = $props();

      let avatarUrl = $state<string | null>(null);
      let uploading = $state(false);
      let files = $state<FileList>();

      const downloadImage = async (path: string) => {
        try {
          const { data, error } = await supabase.storage
            .from("avatars")
            .download(path);

          if (error) {
            throw error;
          }

          const url = URL.createObjectURL(data);
          avatarUrl = url;
        } catch (error) {
          if (error instanceof Error) {
            console.log("Error downloading image: ", error.message);
          }
        }
      };

      const uploadAvatar = async () => {
        try {
          uploading = true;

          if (!files || files.length === 0) {
            throw new Error("You must select an image to upload.");
          }

          const file = files[0];
          const fileExt = file.name.split(".").pop();
          const filePath = `${Math.random()}.${fileExt}`;

          const { error } = await supabase.storage
            .from("avatars")
            .upload(filePath, file);

          if (error) {
            throw error;
          }

          url = filePath;
          onupload?.();
        } catch (error) {
          if (error instanceof Error) {
            alert(error.message);
          }
        } finally {
          uploading = false;
        }
      };

      $effect(() => {
        if (url) downloadImage(url);
      });
    </script>

    <div style="width: {size}px" aria-live="polite">
      {#if avatarUrl}
        <img
          src={avatarUrl}
          alt={avatarUrl ? "Avatar" : "No image"}
          class="avatar image"
          style="height: {size}px, width: {size}px"
        />
      {:else}
        <div class="avatar no-image" style="height: {size}px, width: {size}px"></div>
      {/if}
      <div style="width: {size}px">
        <label class="button primary block" for="single">
          {uploading ? "Uploading ..." : "Upload avatar"}
        </label>
        <span style="display:none">
          <input
            type="file"
            id="single"
            accept="image/*"
            bind:files
            onchange={uploadAvatar}
            disabled={uploading}
          />
        </span>
      </div>
    </div>
    ```
  </NamedCodeBlock>
</CodeSampleWrapper>


### Add the new widget

And then you can add the widget to the Account page:

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/svelte-user-management/src/lib/Account.svelte">
  ```svelte src/lib/Account.svelte
  <script lang="ts">

    // ...

    import Avatar from "./Avatar.svelte";

      // ...

      } finally {
        loading = false;
      }

    // ...

    };

    // ...

    </div>
    <button
      type="button"
      class="button block"
      onclick={() => supabase.auth.signOut()}
    >
      Sign Out
    </button>
  </form>
  ```
</CodeSampleWrapper>

At this stage you have a fully functional application!



# Build a User Management App with SvelteKit



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/sveltekit-user-management).
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

Start building the Svelte app from scratch.


### Initialize a Svelte app

Use the [SvelteKit Skeleton Project](https://svelte.dev/docs/kit) to initialize an app called `supabase-sveltekit` (for this tutorial, select "SvelteKit minimal" and use TypeScript):

```bash
npx sv create supabase-sveltekit
cd supabase-sveltekit
npm install
```

Then install the Supabase client library: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npm install @supabase/supabase-js
```

And finally, save the environment variables in a `.env` file.
All you need are the `PUBLIC_SUPABASE_URL` and the key that you copied [earlier](#get-api-details).

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id=".env" label=".env">
    ```bash name=.env
    PUBLIC_SUPABASE_URL="YOUR_SUPABASE_URL"
    PUBLIC_SUPABASE_PUBLISHABLE_KEY="YOUR_SUPABASE_PUBLISHABLE_KEY"
    ```
  </TabPanel>
</Tabs>


### App styling (optional)

An optional step is to update the CSS file `src/styles.css` to make the app look nice.
You can find the full contents of this file [in the example repository](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/sveltekit-user-management/src/styles.css).


### Creating a Supabase client for SSR

The `ssr` package configures Supabase to use Cookies, which are required for server-side languages and frameworks.

Install the SSR package:

```bash
npm install @supabase/ssr
```

Creating a Supabase client with the `ssr` package automatically configures it to use Cookies. This means the user's session is available throughout the entire SvelteKit stack - page, layout, server, and hooks.

Add the code below to a `src/hooks.server.ts` file to initialize the client on the server:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/hooks.server.ts" label="src/hooks.server.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/hooks.server.ts">
      ```typescript name=src/hooks.server.ts
      // src/hooks.server.ts
      import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public'
      import { createServerClient } from '@supabase/ssr'
      import type { Handle } from '@sveltejs/kit'

      export const handle: Handle = async ({ event, resolve }) => {
        event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll: () => event.cookies.getAll(),
            /**
             * Note: You have to add the `path` variable to the
             * set and remove method due to sveltekit's cookie API
             * requiring this to be set, setting the path to `/`
             * will replicate previous/standard behaviour (https://kit.svelte.dev/docs/types#public-types-cookies)
             */
            setAll: (cookiesToSet) => {
              cookiesToSet.forEach(({ name, value, options }) => {
                event.cookies.set(name, value, { ...options, path: '/' })
              })
            },
          },
        })

        /**
         * Unlike `supabase.auth.getSession`, which is unsafe on the server because it
         * doesn't validate the JWT, this function validates the JWT by first calling
         * `getUser` and aborts early if the JWT signature is invalid.
         */
        event.locals.safeGetSession = async () => {
          const {
            data: { user },
            error,
          } = await event.locals.supabase.auth.getUser()
          if (error) {
            return { session: null, user: null }
          }

          const {
            data: { session },
          } = await event.locals.supabase.auth.getSession()
          return { session, user }
        }

        return resolve(event, {
          filterSerializedResponseHeaders(name: string) {
            return name === 'content-range' || name === 'x-supabase-api-version'
          },
        })
      }
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

<Admonition type="danger">
  Note that `auth.getSession` reads the auth token and the unencoded session data from the local storage medium. It *doesn't* send a request back to the Supabase Auth server unless the local session is expired.

  You should **never** trust the unencoded session data if you're writing server code, since it could be tampered with by the sender. If you need verified, trustworthy user data, call `auth.getUser` instead, which always makes a request to the Auth server to fetch trusted data.
</Admonition>

{/* TODO: Change when adding JS autoconversion */}

As this tutorial uses TypeScript the compiler complains about `event.locals.supabase` and `event.locals.safeGetSession`, you can fix this by updating the `src/app.d.ts` with the content below:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/app.d.ts" label="src/app.d.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/app.d.ts">
      ```typescript name=src/app.d.ts
      import { SupabaseClient, Session } from '@supabase/supabase-js'
      // See https://kit.svelte.dev/docs/types#app
      // for information about these interfaces
      declare global {
      	namespace App {
      		// interface Error {}
      		interface Locals {
      			supabase: SupabaseClient
      			safeGetSession(): Promise<{ session: Session | null; user?: Session["user"] | null }>
      		}
      		interface PageData {
      			session: Session | null
      			user?: Session["user"] | null
      		}
      		// interface PageState {}
      		// interface Platform {}
      	}
      }

      export {};
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

Create a new `src/routes/+layout.server.ts` file to handle the session on the server-side.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/+layout.server.ts" label="src/routes/+layout.server.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/+layout.server.ts">
      ```typescript name=src/routes/+layout.server.ts
      // src/routes/+layout.server.ts
      import type { LayoutServerLoad } from './$types'

      export const load: LayoutServerLoad = async ({ locals: { safeGetSession }, cookies }) => {
        const { session, user } = await safeGetSession()

        return {
          session,
          user,
          cookies: cookies.getAll(),
        }
      }
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

<Admonition type="tip">
  Start the dev server (`npm run dev`) to generate the `./$types` files we are referencing in our project.
</Admonition>

Create a new `src/routes/+layout.ts` file to handle the session and the `supabase` object on the client-side.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/+layout.ts" label="src/routes/+layout.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/+layout.ts">
      ```typescript name=src/routes/+layout.ts
      // src/routes/+layout.ts
      import { PUBLIC_SUPABASE_PUBLISHABLE_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'
      import type { LayoutLoad } from './$types'
      import { createBrowserClient, createServerClient, isBrowser } from '@supabase/ssr'

      export const load: LayoutLoad = async ({ fetch, data, depends }) => {
        depends('supabase:auth')

        const supabase = isBrowser()
          ? createBrowserClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {
              global: {
                fetch,
              },
            })
          : createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {
              global: {
                fetch,
              },
              cookies: {
                getAll() {
                  return data.cookies
                },
              },
            })

        /**
         * It's fine to use `getSession` here, because on the client, `getSession` is
         * safe, and on the server, it reads `session` from the `LayoutData`, which
         * safely checked the session using `safeGetSession`.
         */
        const {
          data: { session },
        } = await supabase.auth.getSession()

        return { supabase, session }
      }
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

Create `src/routes/+layout.svelte`:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/+layout.svelte" label="src/routes/+layout.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/+layout.svelte">
      ```svelte name=src/routes/+layout.svelte
      <!-- src/routes/+layout.svelte -->
      <script lang="ts">
      	import '../styles.css'
      	import { invalidate } from '$app/navigation'
      	import { onMount } from 'svelte'

      	let { data, children } = $props()
      	let { supabase, session } = $derived(data)

      	onMount(() => {
      		const { data } = supabase.auth.onAuthStateChange((event, _session) => {
      			if (_session?.expires_at !== session?.expires_at) {
      				invalidate('supabase:auth')
      			}
      		})

      		return () => data.subscription.unsubscribe()
      	})
      </script>

      <svelte:head>
      	<title>User Management</title>
      </svelte:head>

      <div class="container" style="padding: 50px 0 100px 0">
      	{@render children()}
      </div>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>



## Set up a login page

Create a magic link login/signup page for your application by updating the `routes/+page.svelte` file:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/+page.svelte" label="src/routes/+page.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/+page.svelte">
      ```svelte name=src/routes/+page.svelte
      <!-- src/routes/+page.svelte -->
      <script lang="ts">
      	import { enhance } from '$app/forms'
      	import type { ActionData, SubmitFunction } from './$types.js'

      	interface Props {
      		form: ActionData
      	}
      	let { form }: Props = $props()

      	let loading = $state(false)

      	const handleSubmit: SubmitFunction = () => {
      		loading = true
      		return async ({ update }) => {
      			update()
      			loading = false
      		}
      	}
      </script>

      <svelte:head>
      	<title>User Management</title>
      </svelte:head>

      <form class="row flex flex-center" method="POST" use:enhance={handleSubmit}>
      	<div class="col-6 form-widget">
      		<h1 class="header">Supabase + SvelteKit</h1>
      		<p class="description">Sign in via magic link with your email below</p>
      		{#if form?.message !== undefined}
      		<div class="success {form?.success ? '' : 'fail'}">
      			{form?.message}
      		</div>
      		{/if}
      		<div>
      			<label for="email">Email address</label>
      			<input 
      				id="email" 
      				name="email" 
      				class="inputField" 
      				type="email" 
      				placeholder="Your email" 
      				value={form?.email ?? ''} 
      			/>
      		</div>
      		{#if form?.errors?.email}
      		<span class="flex items-center text-sm error">
      			{form?.errors?.email}
      		</span>
      		{/if}
      		<div>
      			<button class="button primary block">
      				{ loading ? 'Loading' : 'Send magic link' }
      			</button>
      		</div>
      	</div>
      </form>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

Create a `src/routes/+page.server.ts` file that handles the magic link form when submitted.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/+page.server.ts" label="src/routes/+page.server.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/+page.server.ts">
      ```typescript name=src/routes/+page.server.ts
      // src/routes/+page.server.ts
      import { fail, redirect } from '@sveltejs/kit'
      import type { Actions, PageServerLoad } from './$types'

      export const load: PageServerLoad = async ({ url, locals: { safeGetSession } }) => {
        const { session } = await safeGetSession()

        // if the user is already logged in return them to the account page
        if (session) {
          redirect(303, '/account')
        }

        return { url: url.origin }
      }

      export const actions: Actions = {
      	default: async (event) => {
      		const {
      			url,
      			request,
      			locals: { supabase }
      		} = event
      		const formData = await request.formData()
      		const email = formData.get('email') as string
          const validEmail = /^[\w-\.+]+@([\w-]+\.)+[\w-]{2,8}$/.test(email)
          
      		if (!validEmail) {
      			return fail(400, { errors: { email: "Please enter a valid email address" }, email })
      		}

      		const { error } = await supabase.auth.signInWithOtp({ email })

      		if (error) {
      			return fail(400, {
      				success: false,
      				email,
      				message: `There was an issue, Please contact support.`
      			})
      		}

      		return {
      			success: true,
      			message: 'Please check your email for a magic link to log into the website.'
      		}
      	}
      }
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>


### Email template

Change the email template to support a server-side authentication flow.

Before we proceed, let's change the email template to support sending a token hash:

*   Go to the [**Auth** > **Emails**](/dashboard/project/_/auth/templates) page in the project dashboard.
*   Select the **Confirm signup** template.
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
*   Repeat the previous step for **Magic link** template.

<Admonition type="tip">
  **Did you know?** You can also customize emails sent out to new users, including the email's looks, content, and query parameters. Check out the [settings of your project](/dashboard/project/_/auth/templates).
</Admonition>


### Confirmation endpoint

As this is a server-side rendering (SSR) environment, you need to create a server endpoint responsible for exchanging the `token_hash` for a session.

The following code snippet performs the following steps:

*   Retrieves the `token_hash` sent back from the Supabase Auth server using the `token_hash` query parameter.
*   Exchanges this `token_hash` for a session, which you store in storage (in this case, cookies).
*   Finally, redirect the user to the `account` page or the `error` page.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/auth/confirm/+server.ts" label="src/routes/auth/confirm/+server.ts">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/auth/confirm/+server.ts">
      ```typescript name=src/routes/auth/confirm/+server.ts
      // src/routes/auth/confirm/+server.js
      import type { EmailOtpType } from '@supabase/supabase-js'
      import { redirect } from '@sveltejs/kit'

      import type { RequestHandler } from './$types'

      export const GET: RequestHandler = async ({ url, locals: { supabase } }) => {
        const token_hash = url.searchParams.get('token_hash')
        const type = url.searchParams.get('type') as EmailOtpType | null
        const next = url.searchParams.get('next') ?? '/account'

        /**
         * Clean up the redirect URL by deleting the Auth flow parameters.
         *
         * `next` is preserved for now, because it's needed in the error case.
         */
        const redirectTo = new URL(url)
        redirectTo.pathname = next
        redirectTo.searchParams.delete('token_hash')
        redirectTo.searchParams.delete('type')

        if (token_hash && type) {
          const { error } = await supabase.auth.verifyOtp({ type, token_hash })
          if (!error) {
            redirectTo.searchParams.delete('next')
            redirect(303, redirectTo)
          }
        }

        redirectTo.pathname = '/auth/error'
        redirect(303, redirectTo)
      }
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>


### Authentication error page

If there is an error with confirming the token, redirect the user to an error page.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/auth/error/+page.svelte" label="src/routes/auth/error/+page.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/auth/error/+page.svelte">
      ```svelte name=src/routes/auth/error/+page.svelte
      <p>Login error</p>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>


### Account page

After a user signs in, they need to be able to edit their profile details page.
Create a new `src/routes/account/+page.svelte` file with the content below.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/account/+page.svelte" label="src/routes/account/+page.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/account/+page.svelte">
      ```svelte name=src/routes/account/+page.svelte
      <script lang="ts">
      	import { enhance } from '$app/forms';
      	import type { SubmitFunction } from '@sveltejs/kit';

      	// ...

      	let { data, form } = $props()
      	let { session, supabase, profile } = $derived(data)
      	let profileForm: HTMLFormElement
      	let loading = $state(false)
      	let fullName: string = profile?.full_name ?? ''
      	let username: string = profile?.username ?? ''
      	let website: string = profile?.website ?? ''

      	// ...

      	const handleSubmit: SubmitFunction = () => {
      		loading = true
      		return async () => {
      			loading = false
      		}
      	}

      	const handleSignOut: SubmitFunction = () => {
      		loading = true
      		return async ({ update }) => {
      			loading = false
      			update()
      		}
      	}
      </script>

      <div class="form-widget">
      	<form
      		class="form-widget"
      		method="post"
      		action="?/update"
      		use:enhance={handleSubmit}
      		bind:this={profileForm}
      	>

      		// ...

      		<div>
      			<label for="email">Email</label>
      			<input id="email" type="text" value={session.user.email} disabled />
      		</div>

      		<div>
      			<label for="fullName">Full Name</label>
      			<input id="fullName" name="fullName" type="text" value={form?.fullName ?? fullName} />
      		</div>

      		<div>
      			<label for="username">Username</label>
      			<input id="username" name="username" type="text" value={form?.username ?? username} />
      		</div>

      		<div>
      			<label for="website">Website</label>
      			<input id="website" name="website" type="url" value={form?.website ?? website} />
      		</div>

      		<div>
      			<input
      				type="submit"
      				class="button block primary"
      				value={loading ? 'Loading...' : 'Update'}
      				disabled={loading}
      			/>
      		</div>
      	</form>

      	<form method="post" action="?/signout" use:enhance={handleSignOut}>
      		<div>
      			<button class="button block" disabled={loading}>Sign Out</button>
      		</div>
      	</form>
      </div>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

Now, create the associated `src/routes/account/+page.server.ts` file that handles loading data from the server through the `load` function
and handle all form actions through the `actions` object.

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/account/+page.server.ts">
  <NamedCodeBlock name="src/routes/account/+page.server.ts">
    ```typescript name=src/routes/account/+page.server.ts
    import { fail, redirect } from '@sveltejs/kit'
    import type { Actions, PageServerLoad } from './$types'

    export const load: PageServerLoad = async ({ locals: { supabase, safeGetSession } }) => {
      const { session } = await safeGetSession()

      if (!session) {
        redirect(303, '/')
      }

      const { data: profile } = await supabase
        .from('profiles')
        .select(`username, full_name, website, avatar_url`)
        .eq('id', session.user.id)
        .single()

      return { session, profile }
    }

    export const actions: Actions = {
      update: async ({ request, locals: { supabase, safeGetSession } }) => {
        const formData = await request.formData()
        const fullName = formData.get('fullName') as string
        const username = formData.get('username') as string
        const website = formData.get('website') as string
        const avatarUrl = formData.get('avatarUrl') as string

        const { session } = await safeGetSession()

        const { error } = await supabase.from('profiles').upsert({
          id: session?.user.id,
          full_name: fullName,
          username,
          website,
          avatar_url: avatarUrl,
          updated_at: new Date(),
        })

        if (error) {
          return fail(500, {
            fullName,
            username,
            website,
            avatarUrl,
          })
        }

        return {
          fullName,
          username,
          website,
          avatarUrl,
        }
      },
      signout: async ({ locals: { supabase, safeGetSession } }) => {
        const { session } = await safeGetSession()
        if (session) {
          await supabase.auth.signOut()
          redirect(303, '/')
        }
      },
    }
    ```
  </NamedCodeBlock>
</CodeSampleWrapper>


### Launch!

With all the pages in place, run this command in a terminal:

```bash
npm run dev
```

And then open the browser to [localhost:5173](http://localhost:5173) and you should see the completed app.

![Supabase Svelte](/docs/img/supabase-svelte-demo.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

Create an avatar for the user so that they can upload a profile photo. Start by creating a new component called `Avatar.svelte` in the `src/routes/account` directory:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/account/Avatar.svelte" label="src/routes/account/Avatar.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/account/Avatar.svelte">
      ```svelte name=src/routes/account/Avatar.svelte
      <!-- src/routes/account/Avatar.svelte -->
      <script lang="ts">
      	import type { SupabaseClient } from '@supabase/supabase-js'

      	interface Props {
      		size?: number
      		url?: string
      		supabase: SupabaseClient
      		onupload?: () => void
      	}
      	let { size = 10, url = $bindable(), supabase, onupload }: Props = $props()

      	let avatarUrl: string | null = $state(null)
      	let uploading = $state(false)
      	let files: FileList = $state()

      	const downloadImage = async (path: string) => {
      		try {
      			const { data, error } = await supabase.storage.from('avatars').download(path)

      			if (error) {
      				throw error
      			}

      			const url = URL.createObjectURL(data)
      			avatarUrl = url
      		} catch (error) {
      			if (error instanceof Error) {
      				console.log('Error downloading image: ', error.message)
      			}
      		}
      	}

      	const uploadAvatar = async () => {
      		try {
      			uploading = true

      			if (!files || files.length === 0) {
      				throw new Error('You must select an image to upload.')
      			}

      			const file = files[0]
      			const fileExt = file.name.split('.').pop()
      			const filePath = `${Math.random()}.${fileExt}`

      			const { error } = await supabase.storage.from('avatars').upload(filePath, file)

      			if (error) {
      				throw error
      			}

      			url = filePath
      			setTimeout(() => {
      				onupload?.()
      			}, 100)
      		} catch (error) {
      			if (error instanceof Error) {
      				alert(error.message)
      			}
      		} finally {
      			uploading = false
      		}
      	}

      	$effect(() => {
      		if (url) downloadImage(url)
      	})
      </script>

      <div>
      	{#if avatarUrl}
      		<img
      			src={avatarUrl}
      			alt={avatarUrl ? 'Avatar' : 'No image'}
      			class="avatar image"
      			style="height: {size}em; width: {size}em;"
      		/>
      	{:else}
      		<div class="avatar no-image" style="height: {size}em; width: {size}em;"></div>
      	{/if}
      	<input type="hidden" name="avatarUrl" value={url} />

      	<div style="width: {size}em;">
      		<label class="button primary block" for="single">
      			{uploading ? 'Uploading ...' : 'Upload'}
      		</label>
      		<input
      			style="visibility: hidden; position:absolute;"
      			type="file"
      			id="single"
      			accept="image/*"
      			bind:files
      			onchange={uploadAvatar}
      			disabled={uploading}
      		/>
      	</div>
      </div>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>


### Add the new widget

Add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/routes/account/+page.svelte" label="src/routes/account/+page.svelte">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/sveltekit-user-management/src/routes/account/+page.svelte">
      ```svelte name=src/routes/account/+page.svelte
      <script lang="ts">

          // ...

          import Avatar from './Avatar.svelte'

      // ...

      <div class="form-widget">

              // ...

              <Avatar
                  {supabase}
                  bind:url={avatarUrl}
                  size={10}
                  onupload={() => {
                      profileForm.requestSubmit();
                  }}
              />

      // ...

      </div>
      ```
    </CodeSampleWrapper>
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



# Build a User Management App with Swift and SwiftUI



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/supabase-swift-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/swift-user-management).
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

Let's start building the SwiftUI app from scratch.


### Create a SwiftUI app in Xcode

Open Xcode and create a new SwiftUI project.

Add the [supabase-swift](https://github.com/supabase/supabase-swift) dependency.

Add the `https://github.com/supabase/supabase-swift` package to your app. For instructions, see the [Apple tutorial on adding package dependencies](https://developer.apple.com/documentation/xcode/adding-package-dependencies-to-your-app).

Create a helper file to initialize the Supabase client.
You need the API URL and the key that you copied [earlier](#get-api-details).
These variables will be exposed on the application, and that's completely fine since you have
[Row Level Security](/docs/guides/auth#row-level-security) enabled on your database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Supabase.swift" label="Supabase.swift">
    ```swift name=Supabase.swift
    import Foundation
    import Supabase

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "YOUR_SUPABASE_URL")!,
      supabaseKey: "YOUR_SUPABASE_PUBLISHABLE_KEY"
    )
    ```
  </TabPanel>
</Tabs>


### Set up a login view

Set up a SwiftUI view to manage logins and sign ups.
Users should be able to sign in using a magic link.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="AuthView.swift" label="AuthView.swift">
    ```swift name=AuthView.swift
    import SwiftUI
    import Supabase

    struct AuthView: View {
      @State var email = ""
      @State var isLoading = false
      @State var result: Result<Void, Error>?

      var body: some View {
        Form {
          Section {
            TextField("Email", text: $email)
              .textContentType(.emailAddress)
              .textInputAutocapitalization(.never)
              .autocorrectionDisabled()
          }

          Section {
            Button("Sign in") {
              signInButtonTapped()
            }

            if isLoading {
              ProgressView()
            }
          }

          if let result {
            Section {
              switch result {
              case .success:
                Text("Check your inbox.")
              case .failure(let error):
                Text(error.localizedDescription).foregroundStyle(.red)
              }
            }
          }
        }
        .onOpenURL(perform: { url in
          Task {
            do {
              try await supabase.auth.session(from: url)
            } catch {
              self.result = .failure(error)
            }
          }
        })
      }

      func signInButtonTapped() {
        Task {
          isLoading = true
          defer { isLoading = false }

          do {
            try await supabase.auth.signInWithOTP(
                email: email,
                redirectTo: URL(string: "io.supabase.user-management://login-callback")
            )
            result = .success(())
          } catch {
            result = .failure(error)
          }
        }
      }
    }
    ```
  </TabPanel>
</Tabs>

<Admonition type="note">
  The example uses a custom `redirectTo` URL. For this to work, add a custom redirect URL to Supabase and a custom URL scheme to your SwiftUI application. Follow the guide on [implementing deep link handling](/docs/guides/auth/native-mobile-deep-linking?platform=swift).
</Admonition>


### Account view

After a user is signed in, you can allow them to edit their profile details and manage their account.

Create a new view for that called `ProfileView.swift`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="ProfileView.swift" label="ProfileView.swift">
    ```swift name=ProfileView.swift
    import SwiftUI

    struct ProfileView: View {
      @State var username = ""
      @State var fullName = ""
      @State var website = ""

      @State var isLoading = false

      var body: some View {
        NavigationStack {
          Form {
            Section {
              TextField("Username", text: $username)
                .textContentType(.username)
                .textInputAutocapitalization(.never)
              TextField("Full name", text: $fullName)
                .textContentType(.name)
              TextField("Website", text: $website)
                .textContentType(.URL)
                .textInputAutocapitalization(.never)
            }

            Section {
              Button("Update profile") {
                updateProfileButtonTapped()
              }
              .bold()

              if isLoading {
                ProgressView()
              }
            }
          }
          .navigationTitle("Profile")
          .toolbar(content: {
            ToolbarItem(placement: .topBarLeading){
              Button("Sign out", role: .destructive) {
                Task {
                  try? await supabase.auth.signOut()
                }
              }
            }
          })
        }
        .task {
          await getInitialProfile()
        }
      }

      func getInitialProfile() async {
        do {
          let currentUser = try await supabase.auth.session.user

          let profile: Profile =
          try await supabase
            .from("profiles")
            .select()
            .eq("id", value: currentUser.id)
            .single()
            .execute()
            .value

          self.username = profile.username ?? ""
          self.fullName = profile.fullName ?? ""
          self.website = profile.website ?? ""

        } catch {
          debugPrint(error)
        }
      }

      func updateProfileButtonTapped() {
        Task {
          isLoading = true
          defer { isLoading = false }
          do {
            let currentUser = try await supabase.auth.session.user

            try await supabase
              .from("profiles")
              .update(
                UpdateProfileParams(
                  username: username,
                  fullName: fullName,
                  website: website
                )
              )
              .eq("id", value: currentUser.id)
              .execute()
          } catch {
            debugPrint(error)
          }
        }
      }
    }
    ```
  </TabPanel>
</Tabs>


### Models

In `ProfileView.swift`, you used 2 model types for deserializing the response and serializing the request to Supabase. Add those in a new `Models.swift` file.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Models.swift" label="Models.swift">
    ```swift name=Models.swift
    struct Profile: Decodable {
      let username: String?
      let fullName: String?
      let website: String?

      enum CodingKeys: String, CodingKey {
        case username
        case fullName = "full_name"
        case website
      }
    }

    struct UpdateProfileParams: Encodable {
      let username: String
      let fullName: String
      let website: String

      enum CodingKeys: String, CodingKey {
        case username
        case fullName = "full_name"
        case website
      }
    }
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that you've created all the views, add an entry point for the application. This will verify if the user has a valid session and route them to the authenticated or non-authenticated state.

Add a new `AppView.swift` file.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="AppView.swift" label="AppView.swift">
    ```swift name=AppView.swift
    import SwiftUI

    struct AppView: View {
      @State var isAuthenticated = false

      var body: some View {
        Group {
          if isAuthenticated {
            ProfileView()
          } else {
            AuthView()
          }
        }
        .task {
          for await state in supabase.auth.authStateChanges {
            if [.initialSession, .signedIn, .signedOut].contains(state.event) {
              isAuthenticated = state.session != nil
            }
          }
        }
      }
    }
    ```
  </TabPanel>
</Tabs>

Update the entry point to the newly created `AppView`. Run in Xcode to launch your application in the simulator.



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like
photos and videos.

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### Add `PhotosPicker`

Let's add support for the user to pick an image from the library and upload it.
Start by creating a new type to hold the picked avatar image:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="AvatarImage.swift" label="AvatarImage.swift">
    ```swift name=AvatarImage.swift
    import SwiftUI

    struct AvatarImage: Transferable, Equatable {
      let image: Image
      let data: Data

      static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(importedContentType: .image) { data in
          guard let image = AvatarImage(data: data) else {
            throw TransferError.importFailed
          }

          return image
        }
      }
    }

    extension AvatarImage {
      init?(data: Data) {
        guard let uiImage = UIImage(data: data) else {
          return nil
        }

        let image = Image(uiImage: uiImage)
        self.init(image: image, data: data)
      }
    }

    enum TransferError: Error {
      case importFailed
    }
    ```
  </TabPanel>
</Tabs>

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


#### Add `PhotosPicker` to profile page

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="ProfileView.swift" label="ProfileView.swift">
    ```swift name=ProfileView.swift
    import PhotosUI
    import Storage
    import Supabase
    import SwiftUI

    struct ProfileView: View {
      @State var username = ""
      @State var fullName = ""
      @State var website = ""

      @State var isLoading = false

     @State var imageSelection: PhotosPickerItem?
     @State var avatarImage: AvatarImage?

      var body: some View {
        NavigationStack {
          Form {
            Section {
              HStack {
                Group {
                  if let avatarImage {
                    avatarImage.image.resizable()
                  } else {
                    Color.clear
                  }
                }
                .scaledToFit()
                .frame(width: 80, height: 80)

                Spacer()

                PhotosPicker(selection: $imageSelection, matching: .images) {
                  Image(systemName: "pencil.circle.fill")
                    .symbolRenderingMode(.multicolor)
                    .font(.system(size: 30))
                    .foregroundColor(.accentColor)
                }
              }
            }

            Section {
              TextField("Username", text: $username)
                .textContentType(.username)
                .textInputAutocapitalization(.never)
              TextField("Full name", text: $fullName)
                .textContentType(.name)
              TextField("Website", text: $website)
                .textContentType(.URL)
                .textInputAutocapitalization(.never)
            }

            Section {
              Button("Update profile") {
                updateProfileButtonTapped()
              }
              .bold()

              if isLoading {
                ProgressView()
              }
            }
          }
          .navigationTitle("Profile")
          .toolbar(content: {
            ToolbarItem {
              Button("Sign out", role: .destructive) {
                Task {
                  try? await supabase.auth.signOut()
                }
              }
            }
          })
          .onChange(of: imageSelection) { _, newValue in
            guard let newValue else { return }
            loadTransferable(from: newValue)
          }
        }
        .task {
          await getInitialProfile()
        }
      }

      func getInitialProfile() async {
        do {
          let currentUser = try await supabase.auth.session.user

          let profile: Profile =
          try await supabase
            .from("profiles")
            .select()
            .eq("id", value: currentUser.id)
            .single()
            .execute()
            .value

          username = profile.username ?? ""
          fullName = profile.fullName ?? ""
          website = profile.website ?? ""

          if let avatarURL = profile.avatarURL, !avatarURL.isEmpty {
            try await downloadImage(path: avatarURL)
          }

        } catch {
          debugPrint(error)
        }
      }

      func updateProfileButtonTapped() {
        Task {
          isLoading = true
          defer { isLoading = false }
          do {
            let imageURL = try await uploadImage()

            let currentUser = try await supabase.auth.session.user

            let updatedProfile = Profile(
              username: username,
              fullName: fullName,
              website: website,
              avatarURL: imageURL
            )

            try await supabase
              .from("profiles")
              .update(updatedProfile)
              .eq("id", value: currentUser.id)
              .execute()
          } catch {
            debugPrint(error)
          }
        }
      }

      private func loadTransferable(from imageSelection: PhotosPickerItem) {
        Task {
          do {
            avatarImage = try await imageSelection.loadTransferable(type: AvatarImage.self)
          } catch {
            debugPrint(error)
          }
        }
      }

      private func downloadImage(path: String) async throws {
        let data = try await supabase.storage.from("avatars").download(path: path)
        avatarImage = AvatarImage(data: data)
      }

      private func uploadImage() async throws -> String? {
        guard let data = avatarImage?.data else { return nil }

        let filePath = "\(UUID().uuidString).jpeg"

        try await supabase.storage
          .from("avatars")
          .upload(
            filePath,
            data: data,
            options: FileOptions(contentType: "image/jpeg")
          )

        return filePath
      }
    }
    ```
  </TabPanel>
</Tabs>

Finally, update your Models.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="Models.swift" label="Models.swift">
    ```swift name=Models.swift
    struct Profile: Codable {
      let username: String?
      let fullName: String?
      let website: String?
      let avatarURL: String?

      enum CodingKeys: String, CodingKey {
        case username
        case fullName = "full_name"
        case website
        case avatarURL = "avatar_url"
      }
    }
    ```
  </TabPanel>
</Tabs>

You no longer need the `UpdateProfileParams` struct, as you can now reuse the `Profile` struct for both request and response calls.

At this stage you have a fully functional application!



---
**Navigation:** [← Previous](./15-build-a-user-management-app-with-nuxt-3.md) | [Index](./index.md) | [Next →](./17-build-a-user-management-app-with-vue-3.md)
