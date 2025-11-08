**Navigation:** [← Previous](./13-build-a-user-management-app-with-expo-react-native.md) | [Index](./index.md) | [Next →](./15-build-a-user-management-app-with-nuxt-3.md)

# Build a User Management App with Ionic Vue



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/ionic-demos/ionic-angular-account.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/mhartington/supabase-ionic-vue).
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

Let's start building the Vue app from scratch.


### Initialize an Ionic Vue app

We can use the [Ionic CLI](https://ionicframework.com/docs/cli) to initialize an app called `supabase-ionic-vue`:

```bash
npm install -g @ionic/cli
ionic start supabase-ionic-vue blank --type vue
cd supabase-ionic-vue
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

Now that we have the API credentials in place, let's create a helper file to initialize the Supabase client. These variables will be exposed on the browser, and that's completely fine since we have [Row Level Security](/docs/guides/auth#row-level-security) enabled on our Database.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/supabase.ts" label="src/supabase.ts">
    ```js name=src/supabase.ts
    import { createClient } from '@supabase/supabase-js';

    const supabaseUrl = import.meta.env.VITE_SUPABASE_URL as string;
    const supabasePublishableKey = import.meta.env.VITE_SUPABASE_PUBLISHABLE_KEY as string;

    export const supabase = createClient(supabaseUrl, supabasePublishableKey);
    ```
  </TabPanel>
</Tabs>


### Set up a login route

Let's set up a Vue component to manage logins and sign ups. We'll use Magic Links, so users can sign in with their email without using passwords.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="/src/views/Login.vue" label="/src/views/Login.vue">
    ```html name=/src/views/Login.vue
    <template>
      <ion-page>
        <ion-header>
          <ion-toolbar>
            <ion-title>Login</ion-title>
          </ion-toolbar>
        </ion-header>

        <ion-content>
          <div class="ion-padding">
            <h1>Supabase + Ionic Vue</h1>
            <p>Sign in via magic link with your email below</p>
          </div>
          <ion-list inset="true">
            <form @submit.prevent="handleLogin">
              <ion-item>
                <ion-label position="stacked">Email</ion-label>
                <ion-input v-model="email" name="email" autocomplete type="email"></ion-input>
              </ion-item>
              <div class="ion-text-center">
                <ion-button type="submit" fill="clear">Login</ion-button>
              </div>
            </form>
          </ion-list>
          <p>{{ email }}</p>
        </ion-content>
      </ion-page>
    </template>

    <script lang="ts">
      import { supabase } from '../supabase'
      import {
        IonContent,
        IonHeader,
        IonPage,
        IonTitle,
        IonToolbar,
        IonList,
        IonItem,
        IonLabel,
        IonInput,
        IonButton,
        toastController,
        loadingController,
      } from '@ionic/vue'
      import { defineComponent, ref } from 'vue'

      export default defineComponent({
        name: 'LoginPage',
        components: {
          IonContent,
          IonHeader,
          IonPage,
          IonTitle,
          IonToolbar,
          IonList,
          IonItem,
          IonLabel,
          IonInput,
          IonButton,
        },
        setup() {
          const email = ref('')
          const handleLogin = async () => {
            const loader = await loadingController.create({})
            const toast = await toastController.create({ duration: 5000 })

            try {
              await loader.present()
              const { error } = await supabase.auth.signInWithOtp({ email: email.value })

              if (error) throw error

              toast.message = 'Check your email for the login link!'
              await toast.present()
            } catch (error: any) {
              toast.message = error.error_description || error.message
              await toast.present()
            } finally {
              await loader.dismiss()
            }
          }
          return { handleLogin, email }
        },
      })
    </script>
    ```
  </TabPanel>
</Tabs>


### Account page

After a user is signed in we can allow them to edit their profile details and manage their account.

Let's create a new component for that called `Account.vue`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/views/Account.vue" label="src/views/Account.vue">
    ```html name=src/views/Account.vue
    <template>
      <ion-page>
        <ion-header>
          <ion-toolbar>
            <ion-title>Account</ion-title>
          </ion-toolbar>
        </ion-header>

        <ion-content>
          <form @submit.prevent="updateProfile">
            <ion-item>
              <ion-label>
                <p>Email</p>
                <p>{{ user?.email }}</p>
              </ion-label>
            </ion-item>

            <ion-item>
              <ion-label position="stacked">Name</ion-label>
              <ion-input type="text" v-model="profile.username" />
            </ion-item>

            <ion-item>
              <ion-label position="stacked">Website</ion-label>
              <ion-input type="url" v-model="profile.website" />
            </ion-item>

            <div class="ion-text-center">
              <ion-button type="submit" fill="clear">Update Profile</ion-button>
            </div>
          </form>

          <div class="ion-text-center">
            <ion-button fill="clear" @click="signOut">Log Out</ion-button>
          </div>
        </ion-content>
      </ion-page>
    </template>

    <script lang="ts">
      import {
        IonPage,
        IonHeader,
        IonToolbar,
        IonTitle,
        IonContent,
        IonItem,
        IonLabel,
        IonInput,
        IonButton,
        toastController,
        loadingController,
      } from '@ionic/vue'
      import { defineComponent, onMounted, ref } from 'vue'
      import { useRouter } from 'vue-router'
      import { supabase } from '@/supabase'
      import type { User } from '@supabase/supabase-js'

      export default defineComponent({
        name: 'AccountPage',
        components: {
          IonPage,
          IonHeader,
          IonToolbar,
          IonTitle,
          IonContent,
          IonItem,
          IonLabel,
          IonInput,
          IonButton,
        },
        setup() {
          const router = useRouter()
          const user = ref<User | null>(null)

          const profile = ref({
            username: '',
            website: '',
            avatar_url: '',
          })

          const getProfile = async () => {
            const loader = await loadingController.create()
            const toast = await toastController.create({ duration: 5000 })
            await loader.present()

            try {
              const { data, error, status } = await supabase
                .from('profiles')
                .select('username, website, avatar_url')
                .eq('id', user.value?.id)
                .single()

              if (error && status !== 406) throw error

              if (data) {
                profile.value = {
                  username: data.username,
                  website: data.website,
                  avatar_url: data.avatar_url,
                }
              }
            } catch (error: any) {
              toast.message = error.message
              await toast.present()
            } finally {
              await loader.dismiss()
            }
          }

          const updateProfile = async () => {
            const loader = await loadingController.create()
            const toast = await toastController.create({ duration: 5000 })
            await loader.present()

            try {
              const updates = {
                id: user.value?.id,
                ...profile.value,
                updated_at: new Date(),
              }

              const { error } = await supabase.from('profiles').upsert(updates, {
                returning: 'minimal',
              })

              if (error) throw error
            } catch (error: any) {
              toast.message = error.message
              await toast.present()
            } finally {
              await loader.dismiss()
            }
          }

          const signOut = async () => {
            const loader = await loadingController.create()
            const toast = await toastController.create({ duration: 5000 })
            await loader.present()

            try {
              const { error } = await supabase.auth.signOut()
              if (error) throw error
              router.push('/')
            } catch (error: any) {
              toast.message = error.message
              await toast.present()
            } finally {
              await loader.dismiss()
            }
          }

          onMounted(async () => {
            const loader = await loadingController.create()
            await loader.present()

            const { data } = await supabase.auth.getSession()
            user.value = data.session?.user ?? null

            if (!user.value) {
              router.push('/')
            } else {
              await getProfile()
            }

            await loader.dismiss()
          })

          return {
            user,
            profile,
            updateProfile,
            signOut,
          }
        },
      })
    </script>
    ```
  </TabPanel>
</Tabs>


### Launch!

Now that we have all the components in place, let's update `App.vue` and our routes:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/router.index.ts" label="src/router.index.ts">
    ```ts name=src/router.index.ts
    import { createRouter, createWebHistory } from '@ionic/vue-router'
    import { RouteRecordRaw } from 'vue-router'
    import LoginPage from '../views/Login.vue'
    import AccountPage from '../views/Account.vue'
    const routes: Array<RouteRecordRaw> = [
      {
        path: '/',
        name: 'Login',
        component: LoginPage,
      },
      {
        path: '/account',
        name: 'Account',
        component: AccountPage,
      },
    ]

    const router = createRouter({
      history: createWebHistory(import.meta.env.BASE_URL),
      routes,
    })

    export default router
    ```
  </TabPanel>

  <TabPanel id="src/App.vue" label="src/App.vue">
    ```html name=src/App.vue
    <template>
      <ion-app>
        <ion-router-outlet />
      </ion-app>
    </template>

    <script lang="ts">
      import { IonApp, IonRouterOutlet, useIonRouter } from '@ionic/vue'
      import { defineComponent, ref, onMounted } from 'vue'
      import { supabase } from './supabase'

      export default defineComponent({
        name: 'App',
        components: {
          IonApp,
          IonRouterOutlet,
        },
        setup() {
          const router = useIonRouter()
          const user = ref(null)

          onMounted(() => {
            supabase.auth
              .getSession()
              .then((resp) => {
                user.value = resp.data.session?.user ?? null
              })
              .catch((err) => {
                console.log('Error fetching session', err)
              })

            supabase.auth.onAuthStateChange((_event, session) => {
              user.value = session?.user ?? null
            })
          })

          return { user }
        },
      })
    </script>
    ```
  </TabPanel>
</Tabs>

Once that's done, run this in a terminal window:

```bash
ionic serve
```

And then open the browser to [localhost:3000](http://localhost:3000) and you should see the completed app.

![Supabase Ionic Vue](/docs/img/ionic-demos/ionic-vue.png)



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like photos and videos.


### Create an upload widget

First install two packages in order to interact with the user's camera.

```bash
npm install @ionic/pwa-elements @capacitor/camera
```

[Capacitor](https://capacitorjs.com) is a cross-platform native runtime from Ionic that enables web apps to be deployed through the app store and provides access to native device API.

Ionic PWA elements is a companion package that will polyfill certain browser APIs that provide no user interface with custom Ionic UI.

With those packages installed we can update our `main.ts` to include an additional bootstrapping call for the Ionic PWA Elements.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/main.tsx" label="src/main.tsx">
    ```ts name=src/main.tsx
    import { createApp } from 'vue'
    import App from './App.vue'
    import router from './router'

    import { IonicVue } from '@ionic/vue'
    /* Core CSS required for Ionic components to work properly */
    import '@ionic/vue/css/ionic.bundle.css'

    /* Theme variables */
    import './theme/variables.css'

    import { defineCustomElements } from '@ionic/pwa-elements/loader'
    defineCustomElements(window)
    const app = createApp(App).use(IonicVue).use(router)

    router.isReady().then(() => {
      app.mount('#app')
    })
    ```
  </TabPanel>
</Tabs>

Then create an `AvatarComponent`.

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/components/Avatar.vue" label="src/components/Avatar.vue">
    ```html name=src/components/Avatar.vue
    <template>
      <div class="avatar">
        <div class="avatar_wrapper" @click="uploadAvatar">
          <img v-if="avatarUrl" :src="avatarUrl" />
          <ion-icon v-else name="person" class="no-avatar"></ion-icon>
        </div>
      </div>
    </template>

    <script lang="ts">
      import { ref, toRefs, watch, defineComponent } from 'vue'
      import { supabase } from '../supabase'
      import { Camera, CameraResultType } from '@capacitor/camera'
      import { IonIcon } from '@ionic/vue'
      import { person } from 'ionicons/icons'
      export default defineComponent({
        name: 'AppAvatar',
        props: { path: String },
        emits: ['upload', 'update:path'],
        components: { IonIcon },
        setup(prop, { emit }) {
          const { path } = toRefs(prop)
          const avatarUrl = ref('')

          const downloadImage = async () => {
            try {
              const { data, error } = await supabase.storage.from('avatars').download(path.value)
              if (error) throw error
              avatarUrl.value = URL.createObjectURL(data!)
            } catch (error: any) {
              console.error('Error downloading image: ', error.message)
            }
          }

          const uploadAvatar = async () => {
            try {
              const photo = await Camera.getPhoto({
                resultType: CameraResultType.DataUrl,
              })
              if (photo.dataUrl) {
                const file = await fetch(photo.dataUrl)
                  .then((res) => res.blob())
                  .then((blob) => new File([blob], 'my-file', { type: `image/${photo.format}` }))

                const fileName = `${Math.random()}-${new Date().getTime()}.${photo.format}`
                const { error: uploadError } = await supabase.storage
                  .from('avatars')
                  .upload(fileName, file)
                if (uploadError) {
                  throw uploadError
                }
                emit('update:path', fileName)
                emit('upload')
              }
            } catch (error) {
              console.log(error)
            }
          }

          watch(path, () => {
            if (path.value) downloadImage()
          })

          return { avatarUrl, uploadAvatar, person }
        },
      })
    </script>
    <style>
      .avatar {
        display: block;
        margin: auto;
        min-height: 150px;
      }
      .avatar .avatar_wrapper {
        margin: 16px auto 16px;
        border-radius: 50%;
        overflow: hidden;
        height: 150px;
        aspect-ratio: 1;
        background: var(--ion-color-step-50);
        border: thick solid var(--ion-color-step-200);
      }
      .avatar .avatar_wrapper:hover {
        cursor: pointer;
      }
      .avatar .avatar_wrapper ion-icon.no-avatar {
        width: 100%;
        height: 115%;
      }
      .avatar img {
        display: block;
        object-fit: cover;
        width: 100%;
        height: 100%;
      }
    </style>
    ```
  </TabPanel>
</Tabs>


### Add the new widget

And then we can add the widget to the Account page:

<Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
  <TabPanel id="src/views/Account.vue" label="src/views/Account.vue">
    ```html name=src/views/Account.vue
    <template>
      <ion-page>
        <ion-header>
          <ion-toolbar>
            <ion-title>Account</ion-title>
          </ion-toolbar>
        </ion-header>

        <ion-content>
          <avatar v-model:path="profile.avatar_url" @upload="updateProfile"></avatar>
    ...
    </template>
    <script lang="ts">
    import Avatar from '../components/Avatar.vue';
    export default defineComponent({
      name: 'AccountPage',
      components: {
        Avatar,
        ....
      }

    </script>
    ```
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



# Build a Product Management Android App with Jetpack Compose



This tutorial demonstrates how to build a basic product management app. The app demonstrates management operations, photo upload, account creation and authentication using:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - users log in through magic links sent to their email (without having to set up a password).
*   [Supabase Storage](/docs/guides/storage) - users can upload a profile photo.

![manage-product-cover](/docs/img/guides/kotlin/manage-product-cover.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/hieuwu/product-sample-supabase-kt).
</Admonition>



## Project setup

Before we start building we're going to set up our Database and API. This is as simple as starting a new Project in Supabase and then creating a "schema" inside the database.


### Create a project

1.  [Create a new project](https://app.supabase.com) in the Supabase Dashboard.
2.  Enter your project details.
3.  Wait for the new database to launch.


### Set up the database schema

Now we are going to set up the database schema. You can just copy/paste the SQL from below and run it yourself.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  {/* <TabPanel id="dashboard" label="Dashboard">

    1. Go to the [SQL Editor](https://app.supabase.com/project/_/sql) page in the Dashboard.
    2. Click **Product Management**.
    3. Click **Run**.

    </TabPanel> */}

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Create a table for public profiles

    create table
      public.products (
        id uuid not null default gen_random_uuid (),
        name text not null,
        price real not null,
        image text null,
        constraint products_pkey primary key (id)
      ) tablespace pg_default;

    -- Set up Storage!
    insert into storage.buckets (id, name)
      values ('Product Image', 'Product Image');

    -- Set up access controls for storage.
    -- See https://supabase.com/docs/guides/storage/security/access-control#policy-examples for more details.
    CREATE POLICY "Enable read access for all users" ON "storage"."objects"
    AS PERMISSIVE FOR SELECT
    TO public
    USING (true)

    CREATE POLICY "Enable insert for all users" ON "storage"."objects"
    AS PERMISSIVE FOR INSERT
    TO authenticated, anon
    WITH CHECK (true)

    CREATE POLICY "Enable update for all users" ON "storage"."objects"
    AS PERMISSIVE FOR UPDATE
    TO public
    USING (true)
    WITH CHECK (true)

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


### Set up Google authentication

From the [Google Console](https://console.developers.google.com/apis/library), create a new project and add OAuth2 credentials.

![Create Google OAuth credentials](/docs/img/guides/kotlin/google-cloud-oauth-credentials-create.png)

In your [Supabase Auth settings](https://app.supabase.com/project/_/auth/providers) enable Google as a provider and set the required credentials as outlined in the [auth docs](/docs/guides/auth/social-login/auth-google).



## Building the app


### Create new Android project

Open Android Studio > New Project > Base Activity (Jetpack Compose).

![Android Studio new project](/docs/img/guides/kotlin/android-studio-new-project.png)


### Set up API key and secret securely


#### Create local environment secret

Create or edit the `local.properties` file at the root (same level as `build.gradle`) of your project.

> **Note**: Do not commit this file to your source control, for example, by adding it to your `.gitignore` file!

```kotlin
SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
SUPABASE_URL=YOUR_SUPABASE_URL
```


#### Read and set value to `BuildConfig`

In your `build.gradle` (app) file, create a `Properties` object and read the values from your `local.properties` file by calling the `buildConfigField` method:

```kotlin
defaultConfig {
   applicationId "com.example.manageproducts"
   minSdkVersion 22
   targetSdkVersion 33
   versionCode 5
   versionName "1.0"
   testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"

   // Set value part
   Properties properties = new Properties()
   properties.load(project.rootProject.file("local.properties").newDataInputStream())
   buildConfigField("String", "SUPABASE_PUBLISHABLE_KEY", "\"${properties.getProperty("SUPABASE_PUBLISHABLE_KEY")}\"")
   buildConfigField("String", "SECRET", "\"${properties.getProperty("SECRET")}\"")
   buildConfigField("String", "SUPABASE_URL", "\"${properties.getProperty("SUPABASE_URL")}\"")
}
```


#### Use value from `BuildConfig`

Read the value from `BuildConfig`:

```kotlin
val url = BuildConfig.SUPABASE_URL
val apiKey = BuildConfig.SUPABASE_PUBLISHABLE_KEY
```


### Set up Supabase dependencies

![Gradle dependencies](/docs/img/guides/kotlin/gradle-dependencies.png)

In the `build.gradle` (app) file, add these dependencies then press "Sync now." Replace the dependency version placeholders `$supabase_version` and `$ktor_version` with their respective latest versions.

```kotlin
implementation "io.github.jan-tennert.supabase:postgrest-kt:$supabase_version"
implementation "io.github.jan-tennert.supabase:storage-kt:$supabase_version"
implementation "io.github.jan-tennert.supabase:auth-kt:$supabase_version"
implementation "io.ktor:ktor-client-android:$ktor_version"
implementation "io.ktor:ktor-client-core:$ktor_version"
implementation "io.ktor:ktor-utils:$ktor_version"
```

Also in the `build.gradle` (app) file, add the plugin for serialization. The version of this plugin should be the same as your Kotlin version.

```kotlin
plugins {
    ...
    id 'org.jetbrains.kotlin.plugin.serialization' version '$kotlin_version'
    ...
}
```

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### Set up Hilt for dependency injection

In the `build.gradle` (app) file, add the following:

```kotlin
implementation "com.google.dagger:hilt-android:$hilt_version"
annotationProcessor "com.google.dagger:hilt-compiler:$hilt_version"
implementation("androidx.hilt:hilt-navigation-compose:1.0.0")
```

Create a new `ManageProductApplication.kt` class extending Application with `@HiltAndroidApp` annotation:

```kotlin
// ManageProductApplication.kt
@HiltAndroidApp
class ManageProductApplication: Application()
```

Open the `AndroidManifest.xml` file, update name property of Application tag:

```xml
<application
...
    android:name=".ManageProductApplication"
...
</application>

```

Create the `MainActivity`:

```kotlin
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    //This will come later
}
```

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### Provide Supabase instances with Hilt

To make the app easier to test, create a `SupabaseModule.kt` file as follows:

```kotlin
@InstallIn(SingletonComponent::class)
@Module
object SupabaseModule {

    @Provides
    @Singleton
    fun provideSupabaseClient(): SupabaseClient {
        return createSupabaseClient(
            supabaseUrl = BuildConfig.SUPABASE_URL,
            supabaseKey = BuildConfig.SUPABASE_PUBLISHABLE_KEY
        ) {
            install(Postgrest)
            install(Auth) {
                flowType = FlowType.PKCE
                scheme = "app"
                host = "supabase.com"
            }
            install(Storage)
        }
    }

    @Provides
    @Singleton
    fun provideSupabaseDatabase(client: SupabaseClient): Postgrest {
        return client.postgrest
    }

    @Provides
    @Singleton
    fun provideSupabaseAuth(client: SupabaseClient): Auth {
        return client.auth
    }


    @Provides
    @Singleton
    fun provideSupabaseStorage(client: SupabaseClient): Storage {
        return client.storage
    }

}
```


### Create a data transfer object

Create a `ProductDto.kt` class and use annotations to parse data from Supabase:

```kotlin
@Serializable
data class ProductDto(

    @SerialName("name")
    val name: String,

    @SerialName("price")
    val price: Double,

    @SerialName("image")
    val image: String?,

    @SerialName("id")
    val id: String,
)
```

Create a Domain object in `Product.kt` expose the data in your view:

```kotlin
data class Product(
    val id: String,
    val name: String,
    val price: Double,
    val image: String?
)
```


### Implement repositories

Create a `ProductRepository` interface and its implementation named `ProductRepositoryImpl`. This holds the logic to interact with data sources from Supabase. Do the same with the `AuthenticationRepository`.

Create the Product Repository:

```kotlin
interface ProductRepository {
    suspend fun createProduct(product: Product): Boolean
    suspend fun getProducts(): List<ProductDto>?
    suspend fun getProduct(id: String): ProductDto
    suspend fun deleteProduct(id: String)
    suspend fun updateProduct(
        id: String, name: String, price: Double, imageName: String, imageFile: ByteArray
    )
}
```

```kotlin
class ProductRepositoryImpl @Inject constructor(
    private val postgrest: Postgrest,
    private val storage: Storage,
) : ProductRepository {
    override suspend fun createProduct(product: Product): Boolean {
        return try {
            withContext(Dispatchers.IO) {
                val productDto = ProductDto(
                    name = product.name,
                    price = product.price,
                )
                postgrest.from("products").insert(productDto)
                true
            }
            true
        } catch (e: java.lang.Exception) {
            throw e
        }
    }

    override suspend fun getProducts(): List<ProductDto>? {
        return withContext(Dispatchers.IO) {
            val result = postgrest.from("products")
                .select().decodeList<ProductDto>()
            result
        }
    }


    override suspend fun getProduct(id: String): ProductDto {
        return withContext(Dispatchers.IO) {
            postgrest.from("products").select {
                filter {
                    eq("id", id)
                }
            }.decodeSingle<ProductDto>()
        }
    }

    override suspend fun deleteProduct(id: String) {
        return withContext(Dispatchers.IO) {
            postgrest.from("products").delete {
                filter {
                    eq("id", id)
                }
            }
        }
    }

    override suspend fun updateProduct(
        id: String,
        name: String,
        price: Double,
        imageName: String,
        imageFile: ByteArray
    ) {
        withContext(Dispatchers.IO) {
            if (imageFile.isNotEmpty()) {
                val imageUrl =
                    storage.from("Product%20Image").upload(
                        path = "$imageName.png",
                        data = imageFile,
                        upsert = true
                    )
                postgrest.from("products").update({
                    set("name", name)
                    set("price", price)
                    set("image", buildImageUrl(imageFileName = imageUrl))
                }) {
                    filter {
                        eq("id", id)
                    }
                }
            } else {
                postgrest.from("products").update({
                    set("name", name)
                    set("price", price)
                }) {
                    filter {
                        eq("id", id)
                    }
                }
            }
        }
    }

    // Because I named the bucket as "Product Image" so when it turns to an url, it is "%20"
    // For better approach, you should create your bucket name without space symbol
    private fun buildImageUrl(imageFileName: String) =
        "${BuildConfig.SUPABASE_URL}/storage/v1/object/public/${imageFileName}".replace(" ", "%20")
}
```

Create the Authentication Repository:

```kotlin
interface AuthenticationRepository {
    suspend fun signIn(email: String, password: String): Boolean
    suspend fun signUp(email: String, password: String): Boolean
    suspend fun signInWithGoogle(): Boolean
}
```

```kotlin
class AuthenticationRepositoryImpl @Inject constructor(
    private val auth: Auth
) : AuthenticationRepository {
    override suspend fun signIn(email: String, password: String): Boolean {
        return try {
            auth.signInWith(Email) {
                this.email = email
                this.password = password
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    override suspend fun signUp(email: String, password: String): Boolean {
        return try {
            auth.signUpWith(Email) {
                this.email = email
                this.password = password
            }
            true
        } catch (e: Exception) {
            false
        }
    }

    override suspend fun signInWithGoogle(): Boolean {
        return try {
            auth.signInWith(Google)
            true
        } catch (e: Exception) {
            false
        }
    }
}
```


### Implement screens

To navigate screens, use the AndroidX navigation library. For routes, implement a `Destination` interface:

```kotlin

interface Destination {
    val route: String
    val title: String
}


object ProductListDestination : Destination {
    override val route = "product_list"
    override val title = "Product List"
}

object ProductDetailsDestination : Destination {
    override val route = "product_details"
    override val title = "Product Details"
    const val productId = "product_id"
    val arguments = listOf(navArgument(name = productId) {
        type = NavType.StringType
    })
    fun createRouteWithParam(productId: String) = "$route/${productId}"
}

object AddProductDestination : Destination {
    override val route = "add_product"
    override val title = "Add Product"
}

object AuthenticationDestination: Destination {
    override val route = "authentication"
    override val title = "Authentication"
}

object SignUpDestination: Destination {
    override val route = "signup"
    override val title = "Sign Up"
}
```

This will help later for navigating between screens.

Create a `ProductListViewModel`:

```kotlin
@HiltViewModel
class ProductListViewModel @Inject constructor(
private val productRepository: ProductRepository,
) : ViewModel() {

    private val _productList = MutableStateFlow<List<Product>?>(listOf())
    val productList: Flow<List<Product>?> = _productList


    private val _isLoading = MutableStateFlow(false)
    val isLoading: Flow<Boolean> = _isLoading

    init {
        getProducts()
    }

    fun getProducts() {
        viewModelScope.launch {
            val products = productRepository.getProducts()
            _productList.emit(products?.map { it -> it.asDomainModel() })
        }
    }

    fun removeItem(product: Product) {
        viewModelScope.launch {
            val newList = mutableListOf<Product>().apply { _productList.value?.let { addAll(it) } }
            newList.remove(product)
            _productList.emit(newList.toList())
            // Call api to remove
            productRepository.deleteProduct(id = product.id)
            // Then fetch again
            getProducts()
        }
    }

    private fun ProductDto.asDomainModel(): Product {
        return Product(
            id = this.id,
            name = this.name,
            price = this.price,
            image = this.image
        )
    }

}

```

Create the `ProductListScreen.kt`:

```kotlin
@OptIn(ExperimentalMaterial3Api::class, ExperimentalMaterialApi::class)
@Composable
fun ProductListScreen(
    modifier: Modifier = Modifier,
    navController: NavController,
    viewModel: ProductListViewModel = hiltViewModel(),
) {
    val isLoading by viewModel.isLoading.collectAsState(initial = false)
    val swipeRefreshState = rememberSwipeRefreshState(isRefreshing = isLoading)
    SwipeRefresh(state = swipeRefreshState, onRefresh = { viewModel.getProducts() }) {
        Scaffold(
            topBar = {
                TopAppBar(
                    backgroundColor = MaterialTheme.colorScheme.primary,
                    title = {
                        Text(
                            text = stringResource(R.string.product_list_text_screen_title),
                            color = MaterialTheme.colorScheme.onPrimary,
                        )
                    },
                )
            },
            floatingActionButton = {
                AddProductButton(onClick = { navController.navigate(AddProductDestination.route) })
            }
        ) { padding ->
            val productList = viewModel.productList.collectAsState(initial = listOf()).value
            if (!productList.isNullOrEmpty()) {
                LazyColumn(
                    modifier = modifier.padding(padding),
                    contentPadding = PaddingValues(5.dp)
                ) {
                    itemsIndexed(
                        items = productList,
                        key = { _, product -> product.name }) { _, item ->
                        val state = rememberDismissState(
                            confirmStateChange = {
                                if (it == DismissValue.DismissedToStart) {
                                    // Handle item removed
                                    viewModel.removeItem(item)
                                }
                                true
                            }
                        )
                        SwipeToDismiss(
                            state = state,
                            background = {
                                val color by animateColorAsState(
                                    targetValue = when (state.dismissDirection) {
                                        DismissDirection.StartToEnd -> MaterialTheme.colorScheme.primary
                                        DismissDirection.EndToStart -> MaterialTheme.colorScheme.primary.copy(
                                            alpha = 0.2f
                                        )
                                        null -> Color.Transparent
                                    }
                                )
                                Box(
                                    modifier = modifier
                                        .fillMaxSize()
                                        .background(color = color)
                                        .padding(16.dp),
                                ) {
                                    Icon(
                                        imageVector = Icons.Filled.Delete,
                                        contentDescription = null,
                                        tint = MaterialTheme.colorScheme.primary,
                                        modifier = modifier.align(Alignment.CenterEnd)
                                    )
                                }

                            },
                            dismissContent = {
                                ProductListItem(
                                    product = item,
                                    modifier = modifier,
                                    onClick = {
                                        navController.navigate(
                                            ProductDetailsDestination.createRouteWithParam(
                                                item.id
                                            )
                                        )
                                    },
                                )
                            },
                            directions = setOf(DismissDirection.EndToStart),
                        )
                    }
                }
            } else {
                Text("Product list is empty!")
            }

        }
    }
}

@Composable
private fun AddProductButton(
    modifier: Modifier = Modifier,
    onClick: () -> Unit,
) {
    FloatingActionButton(
        modifier = modifier,
        onClick = onClick,
        containerColor = MaterialTheme.colorScheme.primary,
        contentColor = MaterialTheme.colorScheme.onPrimary
    ) {
        Icon(
            imageVector = Icons.Filled.Add,
            contentDescription = null,
        )
    }
}
```

Create the `ProductDetailsViewModel.kt`:

```kotlin

@HiltViewModel
class ProductDetailsViewModel @Inject constructor(
    private val productRepository: ProductRepository,
    savedStateHandle: SavedStateHandle,
    ) : ViewModel() {

    private val _product = MutableStateFlow<Product?>(null)
    val product: Flow<Product?> = _product

    private val _name = MutableStateFlow("")
    val name: Flow<String> = _name

    private val _price = MutableStateFlow(0.0)
    val price: Flow<Double> = _price

    private val _imageUrl = MutableStateFlow("")
    val imageUrl: Flow<String> = _imageUrl

    init {
        val productId = savedStateHandle.get<String>(ProductDetailsDestination.productId)
        productId?.let {
            getProduct(productId = it)
        }
    }

    private fun getProduct(productId: String) {
        viewModelScope.launch {
           val result = productRepository.getProduct(productId).asDomainModel()
            _product.emit(result)
            _name.emit(result.name)
            _price.emit(result.price)
        }
    }

    fun onNameChange(name: String) {
        _name.value = name
    }

    fun onPriceChange(price: Double) {
        _price.value = price
    }

    fun onSaveProduct(image: ByteArray) {
        viewModelScope.launch {
            productRepository.updateProduct(
                id = _product.value?.id,
                price = _price.value,
                name = _name.value,
                imageFile = image,
                imageName = "image_${_product.value.id}",
            )
        }
    }

    fun onImageChange(url: String) {
        _imageUrl.value = url
    }

    private fun ProductDto.asDomainModel(): Product {
        return Product(
            id = this.id,
            name = this.name,
            price = this.price,
            image = this.image
        )
    }
}
```

Create the `ProductDetailsScreen.kt`:

```kotlin
@OptIn(ExperimentalCoilApi::class)
@SuppressLint("UnusedMaterialScaffoldPaddingParameter")
@Composable
fun ProductDetailsScreen(
    modifier: Modifier = Modifier,
    viewModel: ProductDetailsViewModel = hiltViewModel(),
    navController: NavController,
    productId: String?,
) {
    val snackBarHostState = remember { SnackbarHostState() }
    val coroutineScope = rememberCoroutineScope()

    Scaffold(
        snackbarHost = { SnackbarHost(snackBarHostState) },
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = {
                        navController.navigateUp()
                    }) {
                        Icon(
                            imageVector = Icons.Filled.ArrowBack,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onPrimary
                        )
                    }
                },
                backgroundColor = MaterialTheme.colorScheme.primary,
                title = {
                    Text(
                        text = stringResource(R.string.product_details_text_screen_title),
                        color = MaterialTheme.colorScheme.onPrimary,
                    )
                },
            )
        }
    ) {
        val name = viewModel.name.collectAsState(initial = "")
        val price = viewModel.price.collectAsState(initial = 0.0)
        var imageUrl = Uri.parse(viewModel.imageUrl.collectAsState(initial = null).value)
        val contentResolver = LocalContext.current.contentResolver

        Column(
            modifier = modifier
                .padding(16.dp)
                .fillMaxSize()
        ) {
            val galleryLauncher =
                rememberLauncherForActivityResult(ActivityResultContracts.GetContent())
                { uri ->
                    uri?.let {
                        if (it.toString() != imageUrl.toString()) {
                            viewModel.onImageChange(it.toString())
                        }
                    }
                }

            Image(
                painter = rememberImagePainter(imageUrl),
                contentScale = ContentScale.Fit,
                contentDescription = null,
                modifier = Modifier
                    .padding(16.dp, 8.dp)
                    .size(100.dp)
                    .align(Alignment.CenterHorizontally)
            )
            IconButton(modifier = modifier.align(alignment = Alignment.CenterHorizontally),
                onClick = {
                    galleryLauncher.launch("image/*")
                }) {
                Icon(
                    imageVector = Icons.Filled.Edit,
                    contentDescription = null,
                    tint = MaterialTheme.colorScheme.primary
                )
            }
            OutlinedTextField(
                label = {
                    Text(
                        text = "Product name",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 2,
                shape = RoundedCornerShape(32),
                modifier = modifier.fillMaxWidth(),
                value = name.value,
                onValueChange = {
                    viewModel.onNameChange(it)
                },
            )
            Spacer(modifier = modifier.height(12.dp))
            OutlinedTextField(
                label = {
                    Text(
                        text = "Product price",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 2,
                shape = RoundedCornerShape(32),
                modifier = modifier.fillMaxWidth(),
                value = price.value.toString(),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                onValueChange = {
                    viewModel.onPriceChange(it.toDouble())
                },
            )
            Spacer(modifier = modifier.weight(1f))
            Button(
                modifier = modifier.fillMaxWidth(),
                onClick = {
                    if (imageUrl.host?.contains("supabase") == true) {
                        viewModel.onSaveProduct(image = byteArrayOf())
                    } else {
                        val image = uriToByteArray(contentResolver, imageUrl)
                        viewModel.onSaveProduct(image = image)
                    }
                    coroutineScope.launch {
                        snackBarHostState.showSnackbar(
                            message = "Product updated successfully !",
                            duration = SnackbarDuration.Short
                        )
                    }
                }) {
                Text(text = "Save changes")
            }
            Spacer(modifier = modifier.height(12.dp))
            OutlinedButton(
                modifier = modifier
                    .fillMaxWidth(),
                onClick = {
                    navController.navigateUp()
                }) {
                Text(text = "Cancel")
            }

        }

    }
}


private fun getBytes(inputStream: InputStream): ByteArray {
    val byteBuffer = ByteArrayOutputStream()
    val bufferSize = 1024
    val buffer = ByteArray(bufferSize)
    var len = 0
    while (inputStream.read(buffer).also { len = it } != -1) {
        byteBuffer.write(buffer, 0, len)
    }
    return byteBuffer.toByteArray()
}


private fun uriToByteArray(contentResolver: ContentResolver, uri: Uri): ByteArray {
    if (uri == Uri.EMPTY) {
        return byteArrayOf()
    }
    val inputStream = contentResolver.openInputStream(uri)
    if (inputStream != null) {
        return getBytes(inputStream)
    }
    return byteArrayOf()
}
```

Create a `AddProductScreen`:

```kotlin
@SuppressLint("UnusedMaterial3ScaffoldPaddingParameter")
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AddProductScreen(
    modifier: Modifier = Modifier,
    navController: NavController,
    viewModel: AddProductViewModel = hiltViewModel(),
) {
    Scaffold(
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = {
                        navController.navigateUp()
                    }) {
                        Icon(
                            imageVector = Icons.Filled.ArrowBack,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onPrimary
                        )
                    }
                },
                backgroundColor = MaterialTheme.colorScheme.primary,
                title = {
                    Text(
                        text = stringResource(R.string.add_product_text_screen_title),
                        color = MaterialTheme.colorScheme.onPrimary,
                    )
                },
            )
        }
    ) { padding ->
        val navigateAddProductSuccess =
            viewModel.navigateAddProductSuccess.collectAsState(initial = null).value
        val isLoading =
            viewModel.isLoading.collectAsState(initial = null).value
        if (isLoading == true) {
            LoadingScreen(message = "Adding Product",
                onCancelSelected = {
                    navController.navigateUp()
                })
        } else {
            SuccessScreen(
                message = "Product added",
                onMoreAction = {
                    viewModel.onAddMoreProductSelected()
                },
                onNavigateBack = {
                    navController.navigateUp()
                })
        }

    }
}
```

Create the `AddProductViewModel.kt`:

```kotlin
@HiltViewModel
class AddProductViewModel @Inject constructor(
    private val productRepository: ProductRepository,
) : ViewModel() {

    private val _isLoading = MutableStateFlow(false)
    val isLoading: Flow<Boolean> = _isLoading

    private val _showSuccessMessage = MutableStateFlow(false)
    val showSuccessMessage: Flow<Boolean> = _showSuccessMessage

    fun onCreateProduct(name: String, price: Double) {
        if (name.isEmpty() || price <= 0) return
        viewModelScope.launch {
            _isLoading.value = true
            val product = Product(
                id = UUID.randomUUID().toString(),
                name = name,
                price = price,
            )
            productRepository.createProduct(product = product)
            _isLoading.value = false
            _showSuccessMessage.emit(true)

        }
    }
}
```

Create a `SignUpViewModel`:

```kotlin
@HiltViewModel
class SignUpViewModel @Inject constructor(
    private val authenticationRepository: AuthenticationRepository
) : ViewModel() {

    private val _email = MutableStateFlow("")
    val email: Flow<String> = _email

    private val _password = MutableStateFlow("")
    val password = _password

    fun onEmailChange(email: String) {
        _email.value = email
    }

    fun onPasswordChange(password: String) {
        _password.value = password
    }

    fun onSignUp() {
        viewModelScope.launch {
            authenticationRepository.signUp(
                email = _email.value,
                password = _password.value
            )
        }
    }
}
```

Create the `SignUpScreen.kt`:

```kotlin
@Composable
fun SignUpScreen(
    modifier: Modifier = Modifier,
    navController: NavController,
    viewModel: SignUpViewModel = hiltViewModel()
) {
    val snackBarHostState = remember { SnackbarHostState() }
    val coroutineScope = rememberCoroutineScope()
    Scaffold(
        snackbarHost = { androidx.compose.material.SnackbarHost(snackBarHostState) },
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = {
                        navController.navigateUp()
                    }) {
                        Icon(
                            imageVector = Icons.Filled.ArrowBack,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onPrimary
                        )
                    }
                },
                backgroundColor = MaterialTheme.colorScheme.primary,
                title = {
                    Text(
                        text = "Sign Up",
                        color = MaterialTheme.colorScheme.onPrimary,
                    )
                },
            )
        }
    ) { paddingValues ->
        Column(
            modifier = modifier
                .padding(paddingValues)
                .padding(20.dp)
        ) {
            val email = viewModel.email.collectAsState(initial = "")
            val password = viewModel.password.collectAsState()
            OutlinedTextField(
                label = {
                    Text(
                        text = "Email",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 1,
                shape = RoundedCornerShape(32),
                modifier = modifier.fillMaxWidth(),
                value = email.value,
                onValueChange = {
                    viewModel.onEmailChange(it)
                },
            )
            OutlinedTextField(
                label = {
                    Text(
                        text = "Password",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 1,
                shape = RoundedCornerShape(32),
                modifier = modifier
                    .fillMaxWidth()
                    .padding(top = 12.dp),
                value = password.value,
                onValueChange = {
                    viewModel.onPasswordChange(it)
                },
            )
            val localSoftwareKeyboardController = LocalSoftwareKeyboardController.current
            Button(modifier = modifier
                .fillMaxWidth()
                .padding(top = 12.dp),
                onClick = {
                    localSoftwareKeyboardController?.hide()
                    viewModel.onSignUp()
                    coroutineScope.launch {
                        snackBarHostState.showSnackbar(
                            message = "Create account successfully. Sign in now!",
                            duration = SnackbarDuration.Long
                        )
                    }
                }) {
                Text("Sign up")
            }
        }
    }
}
```

Create a `SignInViewModel`:

```kotlin
@HiltViewModel
class SignInViewModel @Inject constructor(
    private val authenticationRepository: AuthenticationRepository
) : ViewModel() {

    private val _email = MutableStateFlow("")
    val email: Flow<String> = _email

    private val _password = MutableStateFlow("")
    val password = _password

    fun onEmailChange(email: String) {
        _email.value = email
    }

    fun onPasswordChange(password: String) {
        _password.value = password
    }

    fun onSignIn() {
        viewModelScope.launch {
            authenticationRepository.signIn(
                email = _email.value,
                password = _password.value
            )
        }
    }

    fun onGoogleSignIn() {
        viewModelScope.launch {
            authenticationRepository.signInWithGoogle()
        }
    }

}
```

Create the `SignInScreen.kt`:

```kotlin
@OptIn(ExperimentalMaterial3Api::class, ExperimentalComposeUiApi::class)
@Composable
fun SignInScreen(
    modifier: Modifier = Modifier,
    navController: NavController,
    viewModel: SignInViewModel = hiltViewModel()
) {
    val snackBarHostState = remember { SnackbarHostState() }
    val coroutineScope = rememberCoroutineScope()
    Scaffold(
        snackbarHost = { androidx.compose.material.SnackbarHost(snackBarHostState) },
        topBar = {
            TopAppBar(
                navigationIcon = {
                    IconButton(onClick = {
                        navController.navigateUp()
                    }) {
                        Icon(
                            imageVector = Icons.Filled.ArrowBack,
                            contentDescription = null,
                            tint = MaterialTheme.colorScheme.onPrimary
                        )
                    }
                },
                backgroundColor = MaterialTheme.colorScheme.primary,
                title = {
                    Text(
                        text = "Login",
                        color = MaterialTheme.colorScheme.onPrimary,
                    )
                },
            )
        }
    ) { paddingValues ->
        Column(
            modifier = modifier
                .padding(paddingValues)
                .padding(20.dp)
        ) {
            val email = viewModel.email.collectAsState(initial = "")
            val password = viewModel.password.collectAsState()
            androidx.compose.material.OutlinedTextField(
                label = {
                    Text(
                        text = "Email",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 1,
                shape = RoundedCornerShape(32),
                modifier = modifier.fillMaxWidth(),
                value = email.value,
                onValueChange = {
                    viewModel.onEmailChange(it)
                },
            )
            androidx.compose.material.OutlinedTextField(
                label = {
                    Text(
                        text = "Password",
                        color = MaterialTheme.colorScheme.primary,
                        style = MaterialTheme.typography.titleMedium
                    )
                },
                maxLines = 1,
                shape = RoundedCornerShape(32),
                modifier = modifier
                    .fillMaxWidth()
                    .padding(top = 12.dp),
                value = password.value,
                onValueChange = {
                    viewModel.onPasswordChange(it)
                },
            )
            val localSoftwareKeyboardController = LocalSoftwareKeyboardController.current
            Button(modifier = modifier
                .fillMaxWidth()
                .padding(top = 12.dp),
                onClick = {
                    localSoftwareKeyboardController?.hide()
                    viewModel.onGoogleSignIn()
                }) {
                Text("Sign in with Google")
            }
            Button(modifier = modifier
                .fillMaxWidth()
                .padding(top = 12.dp),
                onClick = {
                    localSoftwareKeyboardController?.hide()
                    viewModel.onSignIn()
                    coroutineScope.launch {
                        snackBarHostState.showSnackbar(
                            message = "Sign in successfully !",
                            duration = SnackbarDuration.Long
                        )
                    }
                }) {
                Text("Sign in")
            }
            OutlinedButton(modifier = modifier
                .fillMaxWidth()
                .padding(top = 12.dp), onClick = {
                navController.navigate(SignUpDestination.route)
            }) {
                Text("Sign up")
            }
        }
    }
}
```


### Implement the `MainActivity`

In the `MainActivity` you created earlier, show your newly created screens:

```kotlin
@AndroidEntryPoint
class MainActivity : ComponentActivity() {
    @Inject
    lateinit var supabaseClient: SupabaseClient

    @OptIn(ExperimentalMaterial3Api::class)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ManageProductsTheme {
                // A surface container using the 'background' color from the theme
                val navController = rememberNavController()
                val currentBackStack by navController.currentBackStackEntryAsState()
                val currentDestination = currentBackStack?.destination
                Scaffold { innerPadding ->
                    NavHost(
                        navController,
                        startDestination = ProductListDestination.route,
                        Modifier.padding(innerPadding)
                    ) {
                        composable(ProductListDestination.route) {
                            ProductListScreen(
                                navController = navController
                            )
                        }

                        composable(AuthenticationDestination.route) {
                            SignInScreen(
                                navController = navController
                            )
                        }

                        composable(SignUpDestination.route) {
                            SignUpScreen(
                                navController = navController
                            )
                        }

                        composable(AddProductDestination.route) {
                            AddProductScreen(
                                navController = navController
                            )
                        }

                        composable(
                            route = "${ProductDetailsDestination.route}/{${ProductDetailsDestination.productId}}",
                            arguments = ProductDetailsDestination.arguments
                        ) { navBackStackEntry ->
                            val productId =
                                navBackStackEntry.arguments?.getString(ProductDetailsDestination.productId)
                            ProductDetailsScreen(
                                productId = productId,
                                navController = navController,
                            )
                        }
                    }
                }
            }
        }
    }
}
```


### Create the success screen

To handle OAuth and OTP signins, create a new activity to handle the deep link you set in `AndroidManifest.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:name=".ManageProductApplication"
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:enableOnBackInvokedCallback="true"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/Theme.ManageProducts"
        tools:targetApi="31">
        <activity
            android:name=".DeepLinkHandlerActivity"
            android:exported="true"
            android:theme="@style/Theme.ManageProducts" >
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data
                    android:host="supabase.com"
                    android:scheme="app" />
            </intent-filter>
        </activity>
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.ManageProducts">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
```

Then create the `DeepLinkHandlerActivity`:

```kotlin
@AndroidEntryPoint
class DeepLinkHandlerActivity : ComponentActivity() {

    @Inject
    lateinit var supabaseClient: SupabaseClient

    private lateinit var callback: (String, String) -> Unit

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        supabaseClient.handleDeeplinks(intent = intent,
            onSessionSuccess = { userSession ->
                Log.d("LOGIN", "Log in successfully with user info: ${userSession.user}")
                userSession.user?.apply {
                    callback(email ?: "", createdAt.toString())
                }
            })
        setContent {
            val navController = rememberNavController()
            val emailState = remember { mutableStateOf("") }
            val createdAtState = remember { mutableStateOf("") }
            LaunchedEffect(Unit) {
                callback = { email, created ->
                    emailState.value = email
                    createdAtState.value = created
                }
            }
            ManageProductsTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    SignInSuccessScreen(
                        modifier = Modifier.padding(20.dp),
                        navController = navController,
                        email = emailState.value,
                        createdAt = createdAtState.value,
                        onClick = { navigateToMainApp() }
                    )
                }
            }
        }
    }

    private fun navigateToMainApp() {
        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_CLEAR_TOP
        }
        startActivity(intent)
    }
}
```



# Build a User Management App with Next.js



This tutorial demonstrates how to build a basic user management app. The app authenticates and identifies the user, stores their profile information in the database, and allows the user to log in, update their profile details, and upload a profile photo. The app uses:

*   [Supabase Database](/docs/guides/database) - a Postgres database for storing your user data and [Row Level Security](/docs/guides/auth#row-level-security) so data is protected and users can only access their own information.
*   [Supabase Auth](/docs/guides/auth) - allow users to sign up and log in.
*   [Supabase Storage](/docs/guides/storage) - allow users to upload a profile photo.

![Supabase User Management example](/docs/img/user-management-demo.png)

<Admonition type="note">
  If you get stuck while working through this guide, refer to the [full example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management).
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

Start building the Next.js app from scratch.


### Initialize a Next.js app

Use [`create-next-app`](https://nextjs.org/docs/getting-started) to initialize an app called `supabase-nextjs`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```bash
    npx create-next-app@latest --use-npm supabase-nextjs
    cd supabase-nextjs
    ```
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    ```bash
    npx create-next-app@latest --ts --use-npm supabase-nextjs
    cd supabase-nextjs
    ```
  </TabPanel>
</Tabs>

Then install the Supabase client library: [supabase-js](https://github.com/supabase/supabase-js)

```bash
npm install @supabase/supabase-js
```

Save the environment variables in a `.env.local` file at the root of the project, and paste the API URL and the key that you copied [earlier](#get-api-details).

```bash .env.local
NEXT_PUBLIC_SUPABASE_URL=YOUR_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=YOUR_SUPABASE_PUBLISHABLE_KEY
```


### App styling (optional)

An optional step is to update the CSS file `app/globals.css` to make the app look nice.
You can find the full contents of this file [in the example repository](https://raw.githubusercontent.com/supabase/supabase/master/examples/user-management/nextjs-user-management/app/globals.css).


### Supabase Server-Side Auth

Next.js is a highly versatile framework offering pre-rendering at build time (SSG), server-side rendering at request time (SSR), API routes, and middleware edge-functions.

To better integrate with the framework, we've created the `@supabase/ssr` package for Server-Side Auth. It has all the functionalities to quickly configure your Supabase project to use cookies for storing user sessions. Read the [Next.js Server-Side Auth guide](/docs/guides/auth/server-side/nextjs) for more information.

Install the package for Next.js.

```bash
npm install @supabase/ssr
```


### Supabase utilities

There are two different types of clients in Supabase:

1.  **Client Component client** - To access Supabase from Client Components, which run in the browser.
2.  **Server Component client** - To access Supabase from Server Components, Server Actions, and Route Handlers, which run only on the server.

It is recommended to create the following essential utilities files for creating clients, and organize them within `utils/supabase` at the root of the project.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Create a `client.js` and a `server.js` with the following functionalities for client-side Supabase and server-side Supabase, respectively.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="utils/supabase/client.js" label="utils/supabase/client.js">
        ```jsx name=utils/supabase/client.js
        import { createBrowserClient } from '@supabase/ssr'

        export function createClient() {
          // Create a supabase client on the browser with project's credentials
          return createBrowserClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL,
            process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY
          )
        }
        ```
      </TabPanel>

      <TabPanel id="utils/supabase/server.js" label="utils/supabase/server.js">
        ```jsx name=utils/supabase/server.js
        import { createServerClient } from '@supabase/ssr'
        import { cookies } from 'next/headers'

        export async function createClient() {
          const cookieStore = await cookies()

          // Create a server's supabase client with newly configured cookie,
          // which could be used to maintain user's session
          return createServerClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL,
            process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY,
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
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    Create a `client.ts` and a `server.ts` with the following functionalities for client-side Supabase and server-side Supabase, respectively.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="utils/supabase/client.ts" label="utils/supabase/client.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/utils/supabase/client.ts">
          ```typescript name=utils/supabase/client.ts
          import { createBrowserClient } from "@supabase/ssr";

          export function createClient() {
            // Create a supabase client on the browser with project's credentials
            return createBrowserClient(
              process.env.NEXT_PUBLIC_SUPABASE_URL!,
              process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
            );
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>

      <TabPanel id="utils/supabase/server.ts" label="utils/supabase/server.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/utils/supabase/server.ts">
          ```typescript name=utils/supabase/server.ts
          import { createServerClient } from "@supabase/ssr";
          import { cookies } from "next/headers";

          export async function createClient() {
            const cookieStore = await cookies();

            // Create a server's supabase client with newly configured cookie,
            // which could be used to maintain user's session
            return createServerClient(
              process.env.NEXT_PUBLIC_SUPABASE_URL!,
              process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
              {
                cookies: {
                  getAll() {
                    return cookieStore.getAll();
                  },
                  setAll(cookiesToSet) {
                    try {
                      cookiesToSet.forEach(({ name, value, options }) =>
                        cookieStore.set(name, value, options)
                      );
                    } catch {
                      // The `setAll` method was called from a Server Component.
                      // This can be ignored if you have middleware refreshing
                      // user sessions.
                    }
                  },
                },
              }
            );
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Next.js middleware

Since Server Components can't write cookies, you need middleware to refresh expired Auth tokens and store them. This is accomplished by:

*   Refreshing the Auth token with the call to `supabase.auth.getUser`.
*   Passing the refreshed Auth token to Server Components through `request.cookies.set`, so they don't attempt to refresh the same token themselves.
*   Passing the refreshed Auth token to the browser, so it replaces the old token. This is done with `response.cookies.set`.

You could also add a matcher, so that the middleware only runs on routes that access Supabase. For more information, read [the Next.js matcher documentation](https://nextjs.org/docs/app/api-reference/file-conventions/middleware#matcher).

<Admonition type="danger">
  Be careful when protecting pages. The server gets the user session from the cookies, which anyone can spoof.

  Always use `supabase.auth.getUser()` to protect pages and user data.

  *Never* trust `supabase.auth.getSession()` inside server code such as middleware. It isn't guaranteed to revalidate the Auth token.

  It's safe to trust `getUser()` because it sends a request to the Supabase Auth server every time to revalidate the Auth token.
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Create a `middleware.js` file at the project root and another one within the `utils/supabase` folder. The `utils/supabase` file contains the logic for updating the session. This is used by the `middleware.js` file, which is a Next.js convention.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="middleware.js" label="middleware.js">
        ```jsx name=middleware.js
        import { updateSession } from '@/utils/supabase/middleware'

        export async function middleware(request) {
          // update user's auth session
          return await updateSession(request)
        }

        export const config = {
          matcher: [
            /*
             * Match all request paths except for the ones starting with:
             * - _next/static (static files)
             * - _next/image (image optimization files)
             * - favicon.ico (favicon file)
             * Feel free to modify this pattern to include more paths.
             */
            '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
          ],
        }
        ```
      </TabPanel>

      <TabPanel id="utils/supabase/middleware.js" label="utils/supabase/middleware.js">
        ```jsx name=utils/supabase/middleware.js
        import { createServerClient } from '@supabase/ssr'
        import { NextResponse } from 'next/server'

        export async function updateSession(request) {
          let supabaseResponse = NextResponse.next({
            request,
          })

          const supabase = createServerClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL,
            process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return request.cookies.getAll()
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) => request.cookies.set(name, value))
                  supabaseResponse = NextResponse.next({
                    request,
                  })
                  cookiesToSet.forEach(({ name, value, options }) =>
                    supabaseResponse.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          // refreshing the auth token
          await supabase.auth.getUser()

          return supabaseResponse
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    Create a `middleware.ts` file at the project root and another one within the `utils/supabase` folder. The `utils/supabase` file contains the logic for updating the session. This is used by the `middleware.ts` file, which is a Next.js convention.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="middleware.ts" label="middleware.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/middleware.ts">
          ```typescript name=middleware.ts
          import { type NextRequest } from 'next/server'
          import { updateSession } from '@/utils/supabase/middleware'

          export async function middleware(request: NextRequest) {
            // update user's auth session
            return await updateSession(request)
          }

          export const config = {
            matcher: [
              /*
               * Match all request paths except for the ones starting with:
               * - _next/static (static files)
               * - _next/image (image optimization files)
               * - favicon.ico (favicon file)
               * Feel free to modify this pattern to include more paths.
               */
              '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
            ],
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>

      <TabPanel id="utils/supabase/middleware.ts" label="utils/supabase/middleware.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/utils/supabase/middleware.ts">
          ```typescript name=utils/supabase/middleware.ts
          import { createServerClient } from '@supabase/ssr'
          import { NextResponse, type NextRequest } from 'next/server'

          export async function updateSession(request: NextRequest) {
            let supabaseResponse = NextResponse.next({
              request,
            })

            const supabase = createServerClient(
              process.env.NEXT_PUBLIC_SUPABASE_URL!,
              process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
              {
                cookies: {
                  getAll() {
                    return request.cookies.getAll()
                  },
                  setAll(cookiesToSet) {
                    cookiesToSet.forEach(({ name, value, options }) => request.cookies.set(name, value))
                    supabaseResponse = NextResponse.next({
                      request,
                    })
                    cookiesToSet.forEach(({ name, value, options }) =>
                      supabaseResponse.cookies.set(name, value, options)
                    )
                  },
                },
              }
            )

            // refreshing the auth token
            await supabase.auth.getUser()

            return supabaseResponse
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



## Set up a login page


### Login and signup form

Create a login/signup page for your application:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Create a new folder named `login`, containing a `page.jsx` file with a login/signup form.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/login/page.jsx" label="app/login/page.jsx">
        ```jsx name=app/login/page.jsx
        import { login, signup } from './actions'

        export default function LoginPage() {
          return (
            <form>
              <label htmlFor="email">Email:</label>
              <input id="email" name="email" type="email" required />
              <label htmlFor="password">Password:</label>
              <input id="password" name="password" type="password" required />
              <button formAction={login}>Log in</button>
              <button formAction={signup}>Sign up</button>
            </form>
          )
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    Create a new folder named `login`, containing a `page.tsx` file with a login/signup form.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/login/page.tsx" label="app/login/page.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/login/page.tsx">
          ```tsx name=app/login/page.tsx
          import { login, signup } from './actions'

          export default function LoginPage() {
            return (
              <form>
                <label htmlFor="email">Email:</label>
                <input id="email" name="email" type="email" required />
                <label htmlFor="password">Password:</label>
                <input id="password" name="password" type="password" required />
                <button formAction={login}>Log in</button>
                <button formAction={signup}>Sign up</button>
              </form>
            )
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>

Next, you need to create the login/signup actions to hook up the form to the function. Which does the following:

*   Retrieve the user's information.
*   Send that information to Supabase as a signup request, which in turns sends a confirmation email.
*   Handle any error that arises.

<Admonition type="caution">
  The `cookies` method is called before any calls to Supabase, which takes fetch calls out of Next.js's caching. This is important for authenticated data fetches, to ensure that users get access only to their own data.

  Read the Next.js docs to learn more about [opting out of data caching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#opting-out-of-data-caching).
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Create the `action.js` file in the `app/login` folder, which contains the login and signup functions and the `error/page.jsx` file, and displays an error message if the login or signup fails.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/login/actions.js" label="app/login/actions.js">
        ```js name=app/login/actions.js
        'use server'

        import { revalidatePath } from 'next/cache'
        import { redirect } from 'next/navigation'

        import { createClient } from '@/utils/supabase/server'

        export async function login(formData) {
          const supabase = await createClient()

          // type-casting here for convenience
          // in practice, you should validate your inputs
          const data = {
            email: formData.get('email'),
            password: formData.get('password'),
          }

          const { error } = await supabase.auth.signInWithPassword(data)

          if (error) {
            redirect('/error')
          }

          revalidatePath('/', 'layout')
        }

        export async function signup(formData) {
          const supabase = await createClient()

          const data = {
            email: formData.get('email'),
            password: formData.get('password'),
          }

          const { error } = await supabase.auth.signUp(data)

          if (error) {
            redirect('/error')
          }

          revalidatePath('/', 'layout')
        }
        ```
      </TabPanel>

      <TabPanel id="app/error/page.jsx" label="app/error/page.jsx">
        ```jsx name=app/error/page.jsx
        export default function ErrorPage() {
          return <p>Sorry, something went wrong</p>
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    Create the `action.ts` file in the `app/login` folder, which contains the login and signup functions and the `error/page.tsx` file, which displays an error message if the login or signup fails.

    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/login/actions.ts" label="app/login/actions.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/login/actions.ts">
          ```typescript name=app/login/actions.ts
          'use server'

          import { revalidatePath } from 'next/cache'
          import { redirect } from 'next/navigation'

          import { createClient } from '@/utils/supabase/server'

          export async function login(formData: FormData) {
            const supabase = await createClient()

            // type-casting here for convenience
            // in practice, you should validate your inputs
            const data = {
              email: formData.get('email') as string,
              password: formData.get('password') as string,
            }

            const { error } = await supabase.auth.signInWithPassword(data)

            if (error) {
              redirect('/error')
            }

            revalidatePath('/', 'layout')
            redirect('/account')
          }

          export async function signup(formData: FormData) {
            const supabase = await createClient()

            // type-casting here for convenience
            // in practice, you should validate your inputs
            const data = {
              email: formData.get('email') as string,
              password: formData.get('password') as string,
            }

            const { error } = await supabase.auth.signUp(data)

            if (error) {
              redirect('/error')
            }

            revalidatePath('/', 'layout')
            redirect('/account')
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>

      <TabPanel id="app/error/page.tsx" label="app/error/page.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/error/page.tsx">
          ```tsx name=app/error/page.tsx
          export default function ErrorPage() {
              return <p>Sorry, something went wrong</p>
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Email template

Before proceeding, change the email template to support support a server-side authentication flow that sends a token hash:

*   Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard.
*   Select the **Confirm signup** template.
*   Change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.

<Admonition type="tip">
  **Did you know?** You can also customize other emails sent out to new users, including the email's looks, content, and query parameters. Check out the [settings of your project](/dashboard/project/_/auth/templates).
</Admonition>


### Confirmation endpoint

As you are working in a server-side rendering (SSR) environment, you need to create a server endpoint responsible for exchanging the `token_hash` for a session.

The code performs the following steps:

*   Retrieves the code sent back from the Supabase Auth server using the `token_hash` query parameter.
*   Exchanges this code for a session, which you store in your chosen storage mechanism (in this case, cookies).
*   Finally, redirects the user to the `account` page.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/auth/confirm/route.js" label="app/auth/confirm/route.js">
        ```js name=app/auth/confirm/route.js
        import { NextResponse } from 'next/server'
        import { createClient } from '@/utils/supabase/server'

        // Creating a handler to a GET request to route /auth/confirm
        export async function GET(request) {
          const { searchParams } = new URL(request.url)
          const token_hash = searchParams.get('token_hash')
          const type = searchParams.get('type')
          const next = '/account'

          // Create redirect link without the secret token
          const redirectTo = request.nextUrl.clone()
          redirectTo.pathname = next
          redirectTo.searchParams.delete('token_hash')
          redirectTo.searchParams.delete('type')

          if (token_hash && type) {
            const supabase = await createClient()

            const { error } = await supabase.auth.verifyOtp({
              type,
              token_hash,
            })
            if (!error) {
              redirectTo.searchParams.delete('next')
              return NextResponse.redirect(redirectTo)
            }
          }

          // return the user to an error page with some instructions
          redirectTo.pathname = '/error'
          return NextResponse.redirect(redirectTo)
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/auth/confirm/route.ts" label="app/auth/confirm/route.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/auth/confirm/route.ts">
          ```typescript name=app/auth/confirm/route.ts
          import { type EmailOtpType } from '@supabase/supabase-js'
          import { type NextRequest, NextResponse } from 'next/server'
          import { createClient } from '@/utils/supabase/server'

          // Creating a handler to a GET request to route /auth/confirm
          export async function GET(request: NextRequest) {
            const { searchParams } = new URL(request.url)
            const token_hash = searchParams.get('token_hash')
            const type = searchParams.get('type') as EmailOtpType | null
            const next = '/account'

            // Create redirect link without the secret token
            const redirectTo = request.nextUrl.clone()
            redirectTo.pathname = next
            redirectTo.searchParams.delete('token_hash')
            redirectTo.searchParams.delete('type')

            if (token_hash && type) {
              const supabase = await createClient()

              const { error } = await supabase.auth.verifyOtp({
                type,
                token_hash,
              })
              if (!error) {
                redirectTo.searchParams.delete('next')
                return NextResponse.redirect(redirectTo)
              }
            }

            // return the user to an error page with some instructions
            redirectTo.pathname = '/error'
            return NextResponse.redirect(redirectTo)
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Account page

After a user signs in, allow them to edit their profile details and manage their account.

Create a new component for that called `AccountForm` within the `app/account` folder.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/account-form.jsx" label="app/account/account-form.jsx">
        ```jsx name=app/account/account-form.jsx
        'use client'
        import { useCallback, useEffect, useState } from 'react'
        import { createClient } from '@/utils/supabase/client'

        export default function AccountForm({ user }) {
          const supabase = createClient()
          const [loading, setLoading] = useState(true)
          const [fullname, setFullname] = useState(null)
          const [username, setUsername] = useState(null)
          const [website, setWebsite] = useState(null)

          const getProfile = useCallback(async () => {
            try {
              setLoading(true)

              const { data, error, status } = await supabase
                .from('profiles')
                .select(`full_name, username, website, avatar_url`)
                .eq('id', user?.id)
                .single()

              if (error && status !== 406) {
                throw error
              }

              if (data) {
                setFullname(data.full_name)
                setUsername(data.username)
                setWebsite(data.website)
              }
            } catch (error) {
              alert('Error loading user data!')
            } finally {
              setLoading(false)
            }
          }, [user, supabase])

          useEffect(() => {
            getProfile()
          }, [user, getProfile])

          async function updateProfile({ username, website, avatar_url }) {
            try {
              setLoading(true)

              const { error } = await supabase.from('profiles').upsert({
                id: user?.id,
                full_name: fullname,
                username,
                website,
                updated_at: new Date().toISOString(),
              })
              if (error) throw error
              alert('Profile updated!')
            } catch (error) {
              alert('Error updating the data!')
            } finally {
              setLoading(false)
            }
          }

          return (
            <div className="form-widget">
              <div>
                <label htmlFor="email">Email</label>
                <input id="email" type="text" value={user?.email} disabled />
              </div>
              <div>
                <label htmlFor="fullName">Full Name</label>
                <input
                  id="fullName"
                  type="text"
                  value={fullname || ''}
                  onChange={(e) => setFullname(e.target.value)}
                />
              </div>
              <div>
                <label htmlFor="username">Username</label>
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
                  onClick={() => updateProfile({ fullname, username, website })}
                  disabled={loading}
                >
                  {loading ? 'Loading ...' : 'Update'}
                </button>
              </div>

              <div>
                <form action="/auth/signout" method="post">
                  <button className="button block" type="submit">
                    Sign out
                  </button>
                </form>
              </div>
            </div>
          )
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/account-form.tsx" label="app/account/account-form.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/account/account-form.tsx">
          ```tsx name=app/account/account-form.tsx
          'use client'
          import { useCallback, useEffect, useState } from 'react'
          import { createClient } from '@/utils/supabase/client'
          import { type User } from '@supabase/supabase-js'

          // ...

          export default function AccountForm({ user }: { user: User | null }) {
              const supabase = createClient()
              const [loading, setLoading] = useState(true)
              const [fullname, setFullname] = useState<string | null>(null)
              const [username, setUsername] = useState<string | null>(null)
              const [website, setWebsite] = useState<string | null>(null)
              const [avatar_url, setAvatarUrl] = useState<string | null>(null)

              const getProfile = useCallback(async () => {
                  try {
                      setLoading(true)

                      const { data, error, status } = await supabase
                          .from('profiles')
                          .select(`full_name, username, website, avatar_url`)
                          .eq('id', user?.id)
                          .single()

                      if (error && status !== 406) {
                          console.log(error)
                          throw error
                      }

                      if (data) {
                          setFullname(data.full_name)
                          setUsername(data.username)
                          setWebsite(data.website)
                          setAvatarUrl(data.avatar_url)
                      }
                  } catch (error) {
                      alert('Error loading user data!')
                  } finally {
                      setLoading(false)
                  }
              }, [user, supabase])

              useEffect(() => {
                  getProfile()
              }, [user, getProfile])

              async function updateProfile({
                  username,
                  website,
                  avatar_url,
              }: {
                  username: string | null
                  fullname: string | null
                  website: string | null
                  avatar_url: string | null
              }) {
                  try {
                      setLoading(true)

                      const { error } = await supabase.from('profiles').upsert({
                          id: user?.id as string,
                          full_name: fullname,
                          username,
                          website,
                          avatar_url,
                          updated_at: new Date().toISOString(),
                      })
                      if (error) throw error
                      alert('Profile updated!')
                  } catch (error) {
                      alert('Error updating the data!')
                  } finally {
                      setLoading(false)
                  }
              }

              return (
                  <div className="form-widget">

                      {/* ... */}

                      <div>
                          <label htmlFor="email">Email</label>
                          <input id="email" type="text" value={user?.email} disabled />
                      </div>
                      <div>
                          <label htmlFor="fullName">Full Name</label>
                          <input
                              id="fullName"
                              type="text"
                              value={fullname || ''}
                              onChange={(e) => setFullname(e.target.value)}
                          />
                      </div>
                      <div>
                          <label htmlFor="username">Username</label>
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
                              onClick={() => updateProfile({ fullname, username, website, avatar_url })}
                              disabled={loading}
                          >
                              {loading ? 'Loading ...' : 'Update'}
                          </button>
                      </div>

                      <div>
                          <form action="/auth/signout" method="post">
                              <button className="button block" type="submit">
                                  Sign out
                              </button>
                          </form>
                      </div>
                  </div>
              )
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>

Create an account page for the `AccountForm` component you just created

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/page.jsx" label="app/account/page.jsx">
        ```jsx name=app/account/page.jsx
        import AccountForm from './account-form'
        import { createClient } from '@/utils/supabase/server'

        export default async function Account() {
          const supabase = await createClient()

          const {
            data: { user },
          } = await supabase.auth.getUser()

          return <AccountForm user={user} />
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/page.tsx" label="app/account/page.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/account/page.tsx">
          ```tsx name=app/account/page.tsx
          import AccountForm from './account-form'
          import { createClient } from '@/utils/supabase/server'

          export default async function Account() {
              const supabase = await createClient()

              const {
                  data: { user },
              } = await supabase.auth.getUser()

              return <AccountForm user={user} />
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Sign out

Create a route handler to handle the sign out from the server side, making sure to check if the user is logged in first.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/auth/signout/route.js" label="app/auth/signout/route.js">
        ```js name=app/auth/signout/route.js
        import { createClient } from '@/utils/supabase/server'
        import { revalidatePath } from 'next/cache'
        import { NextResponse } from 'next/server'

        export async function POST(req) {
          const supabase = await createClient()

          // Check if a user's logged in
          const {
            data: { user },
          } = await supabase.auth.getUser()

          if (user) {
            await supabase.auth.signOut()
          }

          revalidatePath('/', 'layout')
          return NextResponse.redirect(new URL('/login', req.url), {
            status: 302,
          })
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/auth/signout/route.ts" label="app/auth/signout/route.ts">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/auth/signout/route.ts">
          ```typescript name=app/auth/signout/route.ts
          import { createClient } from "@/utils/supabase/server";
          import { revalidatePath } from "next/cache";
          import { type NextRequest, NextResponse } from "next/server";

          export async function POST(req: NextRequest) {
            const supabase = await createClient();

            // Check if a user's logged in
            const {
              data: { user },
            } = await supabase.auth.getUser();

            if (user) {
              await supabase.auth.signOut();
            }

            revalidatePath("/", "layout");
            return NextResponse.redirect(new URL("/login", req.url), {
              status: 302,
            });
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Launch!

Now you have all the pages, route handlers, and components in place, run the following in a terminal window:

```bash
npm run dev
```

And then open the browser to [localhost:3000/login](http://localhost:3000/login) and you should see the completed app.

When you enter your email and password, you will receive an email with the title **Confirm Your Signup**. Congrats 🎉!!!



## Bonus: Profile photos

Every Supabase project is configured with [Storage](/docs/guides/storage) for managing large files like
photos and videos.


### Create an upload widget

Create an avatar widget for the user so that they can upload a profile photo. Start by creating a new component:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/avatar.jsx" label="app/account/avatar.jsx">
        ```jsx name=app/account/avatar.jsx
        'use client'
        import React, { useEffect, useState } from 'react'
        import { createClient } from '@/utils/supabase/client'
        import Image from 'next/image'

        export default function Avatar({ uid, url, size, onUpload }) {
          const supabase = createClient()
          const [avatarUrl, setAvatarUrl] = useState(url)
          const [uploading, setUploading] = useState(false)

          useEffect(() => {
            async function downloadImage(path) {
              try {
                const { data, error } = await supabase.storage.from('avatars').download(path)
                if (error) {
                  throw error
                }

                const url = URL.createObjectURL(data)
                setAvatarUrl(url)
              } catch (error) {
                console.log('Error downloading image: ', error)
              }
            }

            if (url) downloadImage(url)
          }, [url, supabase])

          const uploadAvatar = async (event) => {
            try {
              setUploading(true)

              if (!event.target.files || event.target.files.length === 0) {
                throw new Error('You must select an image to upload.')
              }

              const file = event.target.files[0]
              const fileExt = file.name.split('.').pop()
              const filePath = `${uid}-${Math.random()}.${fileExt}`

              const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

              if (uploadError) {
                throw uploadError
              }

              onUpload(filePath)
            } catch (error) {
              alert('Error uploading avatar!')
            } finally {
              setUploading(false)
            }
          }

          return (
            <div>
              {avatarUrl ? (
                <Image
                  width={size}
                  height={size}
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
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/avatar.tsx" label="app/account/avatar.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/account/avatar.tsx">
          ```tsx name=app/account/avatar.tsx
          'use client'
          import React, { useEffect, useState } from 'react'
          import { createClient } from '@/utils/supabase/client'
          import Image from 'next/image'

          export default function Avatar({
            uid,
            url,
            size,
            onUpload,
          }: {
            uid: string | null
            url: string | null
            size: number
            onUpload: (url: string) => void
          }) {
            const supabase = createClient()
            const [avatarUrl, setAvatarUrl] = useState<string | null>(url)
            const [uploading, setUploading] = useState(false)

            useEffect(() => {
              async function downloadImage(path: string) {
                try {
                  const { data, error } = await supabase.storage.from('avatars').download(path)
                  if (error) {
                    throw error
                  }

                  const url = URL.createObjectURL(data)
                  setAvatarUrl(url)
                } catch (error) {
                  console.log('Error downloading image: ', error)
                }
              }

              if (url) downloadImage(url)
            }, [url, supabase])

            const uploadAvatar: React.ChangeEventHandler<HTMLInputElement> = async (event) => {
              try {
                setUploading(true)

                if (!event.target.files || event.target.files.length === 0) {
                  throw new Error('You must select an image to upload.')
                }

                const file = event.target.files[0]
                const fileExt = file.name.split('.').pop()
                const filePath = `${uid}-${Math.random()}.${fileExt}`

                const { error: uploadError } = await supabase.storage.from('avatars').upload(filePath, file)

                if (uploadError) {
                  throw uploadError
                }

                onUpload(filePath)
              } catch (error) {
                alert('Error uploading avatar!')
              } finally {
                setUploading(false)
              }
            }

            return (
              <div>
                {avatarUrl ? (
                  <Image
                    width={size}
                    height={size}
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
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>


### Add the new widget

Then add the widget to the `AccountForm` component:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/account-form.jsx" label="app/account/account-form.jsx">
        ```jsx name=app/account/account-form.jsx
        // Import the new component
        import Avatar from './avatar'

        // ...

        return (
          <div className="form-widget">
            {/* Add to the body */}
            <Avatar
              uid={user?.id}
              url={avatar_url}
              size={150}
              onUpload={(url) => {
                setAvatarUrl(url)
                updateProfile({ fullname, username, website, avatar_url: url })
              }}
            />
            {/* ... */}
          </div>
        )
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="ts" label="TypeScript">
    <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
      <TabPanel id="app/account/account-form.tsx" label="app/account/account-form.tsx">
        <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/user-management/nextjs-user-management/app/account/account-form.tsx">
          ```tsx name=app/account/account-form.tsx
          // ...

          import Avatar from './avatar'

              // ...

              return (
                  <div className="form-widget">
                      <Avatar
                          uid={user?.id ?? null}
                          url={avatar_url}
                          size={150}
                          onUpload={(url) => {
                              setAvatarUrl(url)
                              updateProfile({ fullname, username, website, avatar_url: url })
                          }}
                      />

                  {/* ... */}

                  </div>
              )
          }
          ```
        </CodeSampleWrapper>
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>

At this stage you have a fully functional application!



## See also

*   See the complete [example on GitHub](https://github.com/supabase/supabase/tree/master/examples/user-management/nextjs-user-management) and deploy it to Vercel
*   [Build a Twitter Clone with the Next.js App Router and Supabase - free egghead course](https://egghead.io/courses/build-a-twitter-clone-with-the-next-js-app-router-and-supabase-19bebadb)
*   Explore the [pre-built Auth components](/ui/docs/nextjs/password-based-auth)
*   Explore the [Supabase Cache Helpers](https://github.com/psteinroe/supabase-cache-helpers)
*   See the [Next.js Subscription Payments Starter](https://github.com/vercel/nextjs-subscription-payments) template on GitHub



---
**Navigation:** [← Previous](./13-build-a-user-management-app-with-expo-react-native.md) | [Index](./index.md) | [Next →](./15-build-a-user-management-app-with-nuxt-3.md)
