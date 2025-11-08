**Navigation:** [← Previous](./30-clerk.md) | [Index](./index.md) | [Next →](./32-login-with-google.md)

# Login with Bitbucket



To enable Bitbucket Auth for your project, you need to set up a Bitbucket OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up Bitbucket logins for your application consists of 3 parts:

*   Create and configure a Bitbucket OAuth Consumer on [Bitbucket](https://bitbucket.org)
*   Add your Bitbucket OAuth Consumer keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your Bitbucket account

*   Go to [bitbucket.org](https://bitbucket.org/).
*   Click on `Login` at the top right to log in.

![Bitbucket Developer Portal.](/docs/img/guides/auth-bitbucket/bitbucket-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Bitbucket** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Bitbucket OAuth app

*   Click on your profile icon at the bottom left
*   Click on `All Workspaces`
*   Select a workspace and click on it to select it
*   Click on `Settings` on the left
*   Click on `OAuth consumers` on the left under `Apps and Features` (near the bottom)
*   Click `Add Consumer` at the top
*   Enter the name of your app under `Name`
*   In `Callback URL`, type the callback URL of your app
*   Check the permissions you need (Email, Read should be enough)
*   Click `Save` at the bottom
*   Click on your app name (the name of your new OAuth Consumer)
*   Copy your `Key` (`client_key`) and `Secret` (`client_secret`) codes



## Add your Bitbucket credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **BitBucket** from the accordion list to expand and turn **BitBucket Enabled** to ON
*   Enter your **BitBucket Client ID** and **BitBucket Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `bitbucket` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signInWithBitbucket() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'bitbucket',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `bitbucket` as the `provider`:

    ```dart
    Future<void> signInWithBitbucket() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.bitbucket,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Bitbucket` as the `Provider`:

    ```kotlin
    suspend fun signInWithBitbucket() {
    	supabase.auth.signInWith(Bitbucket)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Bitbucket Account](https://bitbucket.org)



# Login with Discord



To enable Discord Auth for your project, you need to set up a Discord Application and add the Application OAuth credentials to your Supabase Dashboard.



## Overview

Setting up Discord logins for your application consists of 3 parts:

*   Create and configure a Discord Application [Discord Developer Portal](https://discord.com/developers)
*   Add your Discord OAuth Consumer keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your Discord account

*   Go to [discord.com](https://discord.com/).
*   Click on `Login` at the top right to log in.

![Discord Portal.](/docs/img/guides/auth-discord/discord-portal.png)

*   Once logged in, go to [discord.com/developers](https://discord.com/developers).

![Discord Portal.](/docs/img/guides/auth-discord/discord-developer-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Discord** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Discord application

*   Click on `New Application` at the top right.
*   Enter the name of your application and click `Create`.
*   Click on `OAuth2` under `Settings` in the left side panel.
*   Click `Add Redirect` under `Redirects`.
*   Type or paste your `callback URL` into the `Redirects` box.
*   Click `Save Changes` at the bottom.
*   Copy your `Client ID` and `Client Secret` under `Client information`.



## Add your Discord credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Discord** from the accordion list to expand and turn **Discord Enabled** to ON
*   Enter your **Discord Client ID** and **Discord Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Discord auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Discord auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_discord_enabled": true,
    "external_discord_client_id": "your-discord-client-id",
    "external_discord_secret": "your-discord-client-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `discord` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signInWithDiscord() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'discord',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `discord` as the `provider`:

    ```dart
    Future<void> signInWithDiscord() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.discord,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Discord` as the `Provider`:

    ```kotlin
    suspend fun signInWithDiscord() {
    	supabase.auth.signInWith(Discord)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

If your user is already signed in, Discord prompts the user again for authorization.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Discord Account](https://discord.com)
*   [Discord Developer Portal](https://discord.com/developers)



# Login with Facebook



To enable Facebook Auth for your project, you need to set up a Facebook OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up Facebook logins for your application consists of 3 parts:

*   Create and configure a Facebook Application on the [Facebook Developers Site](https://developers.facebook.com)
*   Add your Facebook keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your Facebook Developer account

*   Go to [developers.facebook.com](https://developers.facebook.com).
*   Click on `Log In` at the top right to log in.

![Facebook Developer Portal.](/docs/img/guides/auth-facebook/facebook-portal.png)



## Create a Facebook app

*   Click on `My Apps` at the top right.
*   Click `Create App` near the top right.
*   Select your app type and click `Continue`.
*   Fill in your app information, then click `Create App`.
*   This should bring you to the screen: `Add Products to Your App`. (Alternatively you can click on `Add Product` in the left sidebar to get to this screen.)

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Facebook** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Set up Facebook login for your Facebook app

From the `Add Products to your App` screen:

*   Click `Setup` under `Facebook Login`
*   Skip the Quickstart screen, instead, in the left sidebar, click `Settings` under `Facebook Login`
*   Enter your callback URI under `Valid OAuth Redirect URIs` on the `Facebook Login Settings` page
*   Enter this in the `Valid OAuth Redirect URIs` box
*   Click `Save Changes` at the bottom right

Be aware that you have to set the right use case permissions to enable Third party applications to read the email address. To do so:

Under `Build Your App`, click on `Use Cases` screen. From there, do the following steps:

*   Click the Edit button in `Authentication and Account Creation` on the right side. This action will lead to the other page.
*   `public_profile` is set by default, so make sure it and `email` have status of **Ready for testing** in the redirected page.
*   If not, click the **Add** button in email on right side.



## Copy your Facebook app ID and secret

*   Click `Settings / Basic` in the left sidebar
*   Copy your App ID from the top of the `Basic Settings` page
*   Under `App Secret` click `Show` then copy your secret
*   Make sure all required fields are completed on this screen.



## Enter your Facebook app ID and secret into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Facebook** from the accordion list to expand and turn **Facebook Enabled** to ON
*   Enter your **Facebook Client ID** and **Facebook Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Facebook auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Facebook auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_facebook_enabled": true,
    "external_facebook_client_id": "your-facebook-app-id",
    "external_facebook_secret": "your-facebook-app-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `facebook` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    async function signInWithFacebook() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'facebook',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `facebook` as the `provider`:

    ```dart
    Future<void> signInWithFacebook() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.facebook,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```

    ### Alternative: Using Facebook SDK with signInWithIdToken

    For more control over the Facebook authentication flow, you can use the Facebook SDK directly and then authenticate with Supabase using [`signInWithIdToken()`](/docs/reference/dart/auth-signinwithidtoken):

    First, add the Facebook SDK dependency to your `pubspec.yaml`:

    ```yaml
    dependencies:
      flutter_facebook_auth: ^7.0.1
    ```

    Then implement the Facebook authentication:

    ```dart
    import 'package:flutter_facebook_auth/flutter_facebook_auth.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    Future<void> signInWithFacebook() async {
      try {
        final LoginResult result = await FacebookAuth.instance.login(
          permissions: ['public_profile', 'email'],
        );

        if (result.status == LoginStatus.success) {
          final accessToken = result.accessToken!.tokenString;

          await Supabase.instance.client.auth.signInWithIdToken(
            provider: OAuthProvider.facebook,
            idToken: accessToken,
          );

          // Authentication successful
        } else {
          // Handle login cancellation or failure
          throw Exception('Facebook login failed: ${result.status}');
        }
      } catch (e) {
        // Handle errors
        throw Exception('Facebook authentication error: ${e.toString()}');
      }
    }
    ```

    <Admonition type="note">
      Make sure to configure your Facebook app properly and add the required permissions in the Facebook Developer Console. The `signInWithIdToken` method requires the Facebook access token to be valid and properly scoped.
    </Admonition>
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/swift/auth-signinwithoauth) with `facebook` as the `provider`:

    ```swift
    func signInWithFacebook() async throws {
      try await supabase.auth.signInWithOAuth(
        provider: .facebook,
        redirectTo: URL(string: "my.scheme://my-host")!, // Optionally set the redirect link to bring back the user via deeplink.
        launchFlow: { url in
          // use url to start OAuth flow
          // and return a result url that contains the OAuth token.
          // ...
          return resultURL
        }
      )
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Facebook` as the `Provider`:

    ```kotlin
    suspend fun signInWithFacebook() {
    	supabase.auth.signInWith(Facebook)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    When your user signs out, call [signOut()](/docs/reference/swift/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```swift
    func signOut() async throws {
      try await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>

Now, you should be able to login with Facebook and alert you to `Submit for Login Review` when users try to sign into your app. Follow the instructions there to make your app go live for full features and products.
You can read more about App Review [here](https://developers.facebook.com/docs/app-review/).



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Facebook Developers Dashboard](https://developers.facebook.com/)



# Login with Figma



To enable Figma Auth for your project, you need to set up a Figma OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up Figma logins for your application consists of 3 parts:

*   Create and configure a Figma App on the [Figma Developers page](https://www.figma.com/developers).
*   Add your Figma `client_id` and `client_secret` to your [Supabase Project](https://app.supabase.com).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access the Figma Developers page

*   Go to the [Figma Developers page](https://www.figma.com/developers)
*   Click on `My apps` at the top right
*   Log in (if necessary)

![Figma Developers page](/docs/img/guides/auth-figma/figma_developers_page.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Figma** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Figma OAuth app

*   Enter your `App name`, `Website URL` and upload your app logo
*   Click on `Add callback`
*   Add your `Callback URL`
*   Click on `Save`

![Create Figma app](/docs/img/guides/auth-figma/figma_create_app.png)

*   Copy and save your newly-generated `Client ID`
*   Copy and save your newly-generated `Client Secret`

![Get Figma app credentials](/docs/img/guides/auth-figma/figma_app_credentials.png)



## Enter your Figma credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Figma** from the accordion list to expand and turn **Figma Enabled** to ON
*   Enter your **Figma Client ID** and **Figma Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `figma` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithFigma() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'figma',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/flutter/auth-signinwithoauth) with `figma` as the `provider`:

    ```dart
    Future<void> signInWithFigma() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.figma,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Figma` as the `Provider`:

    ```kotlin
    suspend fun signInWithFigma() {
    	supabase.auth.signInWith(Figma)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Figma Developers page](https://www.figma.com/developers)



# Login with GitHub



To enable GitHub Auth for your project, you need to set up a GitHub OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up GitHub logins for your application consists of 3 parts:

*   Create and configure a GitHub OAuth App on [GitHub](https://github.com)
*   Add your GitHub OAuth keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitHub** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Register a new OAuth application on GitHub

*   Navigate to the [OAuth apps page](https://github.com/settings/developers)
*   Click `Register a new application`. If you've created an app before, click `New OAuth App` here.
*   In `Application name`, type the name of your app.
*   In `Homepage URL`, type the full URL to your app's website.
*   In `Authorization callback URL`, type the callback URL of your app.
*   Leave `Enable Device Flow` unchecked.
*   Click `Register Application`.

Copy your new OAuth credentials

*   Copy and save your `Client ID`.
*   Click `Generate a new client secret`.
*   Copy and save your `Client secret`.



## Enter your GitHub credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitHub** from the accordion list to expand and turn **GitHub Enabled** to ON
*   Enter your **GitHub Client ID** and **GitHub Client Secret** saved in the previous step
*   Click `Save`

You can also configure the GitHub auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure GitHub auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_github_enabled": true,
    "external_github_client_id": "your-github-client-id",
    "external_github_secret": "your-github-client-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `github` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signInWithGithub() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'github',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `github` as the `provider`:

    ```dart
    Future<void> signInWithGithub() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.github,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    When your user signs in, call [`signInWithOAuth`](/docs/reference/swift/auth-signinwithoauth) with `.github` as the `Provider`:

    ```swift
    func signInWithGithub() async throws {
      try await supabase.auth.signInWithOAuth(
        provider: .github,
        redirectTo: URL(string: "my-custom-scheme://my-app-host")
      )
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with [`Github`](https://github.com/supabase-community/supabase-kt/blob/master/Auth/src/commonMain/kotlin/io/github/jan/supabase/auth/providers/Providers.kt#L16-L20) as the `Provider`:

    ```kotlin
    suspend fun signInWithGithub() {
    	supabase.auth.signInWith(Github)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [GitHub Developer Settings](https://github.com/settings/developers)



# Login with GitLab



To enable GitLab Auth for your project, you need to set up a GitLab OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up GitLab logins for your application consists of 3 parts:

*   Create and configure a GitLab Application on [GitLab](https://gitlab.com)
*   Add your GitLab Application keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your GitLab account

*   Go to [gitlab.com](https://gitlab.com).
*   Click on `Login` at the top right to log in.

![GitLab Developer Portal.](/docs/img/guides/auth-gitlab/gitlab-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitLab** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create your GitLab application

*   Click on your `profile logo` (avatar) in the top-right corner.
*   Select `Edit profile`.
*   In the left sidebar, select Applications.
*   Enter the name of the application.
*   In the `Redirect URI` box, type the callback URL of your app.
*   Check the box next to `Confidential` (make sure it is checked).
*   Check the scope named `read_user` (this is the only required scope).
*   Click `Save Application` at the bottom.
*   Copy and save your `Application ID` (`client_id`) and `Secret` (`client_secret`) which you'll need later.



## Add your GitLab credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **GitLab** from the accordion list to expand and turn **GitLab Enabled** to ON
*   Enter your **GitLab Client ID** and **GitLab Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `gitlab` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signInWithGitLab() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'gitlab',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `gitlab` as the `provider`:

    ```dart
    Future<void> signInWithGitLab() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.gitlab,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Gitlab` as the `Provider`:

    ```kotlin
    suspend fun signInWithGitLab() {
    	supabase.auth.signInWith(Gitlab)
    }
    ```
  </TabPanel>
</Tabs>

For a PKCE flow, for example in Server-Side Auth, you need an extra step to handle the code exchange. When calling `signInWithOAuth`, provide a `redirectTo` URL which points to a callback route. This redirect URL should be added to your [redirect allow list](/docs/guides/auth/redirect-urls).

<Tabs scrollable size="small" type="underlined" defaultActiveId="client" queryGroup="environment">
  <TabPanel id="client" label="Client">
    In the browser, `signInWithOAuth` automatically redirects to the OAuth provider's authentication endpoint, which then redirects to your endpoint.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js';
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider

    // ---cut---
    await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `http://example.com/auth/callback`,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="server" label="Server">
    In the server, you need to handle the redirect to the OAuth provider's authentication endpoint. The `signInWithOAuth` method returns the endpoint URL, which you can redirect to.

    ```js
    import { createClient, type Provider } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')
    const provider = 'provider' as Provider
    const redirect = (url: string) => {}

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: 'http://example.com/auth/callback',
      },
    })

    if (data.url) {
      redirect(data.url) // use the redirect API for your server framework
    }
    ```
  </TabPanel>
</Tabs>

At the callback endpoint, handle the code exchange to save the user session.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    Create a new file at `app/auth/callback/route.ts` and populate with the following:

    <NamedCodeBlock name="app/auth/callback/route.ts">
      ```ts name=app/auth/callback/route.ts
      import { NextResponse } from 'next/server'
      // The client you created from the Server-Side Auth instructions
      import { createClient } from '@/utils/supabase/server'

      export async function GET(request: Request) {
        const { searchParams, origin } = new URL(request.url)
        const code = searchParams.get('code')
        // if "next" is in param, use it as the redirect URL
        let next = searchParams.get('next') ?? '/'
        if (!next.startsWith('/')) {
          // if "next" is not a relative URL, use the default
          next = '/'
        }

        if (code) {
          const supabase = await createClient()
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            const forwardedHost = request.headers.get('x-forwarded-host') // original origin before load balancer
            const isLocalEnv = process.env.NODE_ENV === 'development'
            if (isLocalEnv) {
              // we can be sure that there is no load balancer in between, so no need to watch for X-Forwarded-Host
              return NextResponse.redirect(`${origin}${next}`)
            } else if (forwardedHost) {
              return NextResponse.redirect(`https://${forwardedHost}${next}`)
            } else {
              return NextResponse.redirect(`${origin}${next}`)
            }
          }
        }

        // return the user to an error page with instructions
        return NextResponse.redirect(`${origin}/auth/auth-code-error`)
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    Create a new file at `src/routes/auth/callback/+server.js` and populate with the following:

    <NamedCodeBlock name="src/routes/auth/callback/+server.js">
      ```js name=src/routes/auth/callback/+server.js
      import { redirect } from '@sveltejs/kit';

      export const GET = async (event) => {
      	const {
      		url,
      		locals: { supabase }
      	} = event;
      	const code = url.searchParams.get('code') as string;
      	const next = url.searchParams.get('next') ?? '/';

        if (code) {
          const { error } = await supabase.auth.exchangeCodeForSession(code)
          if (!error) {
            redirect(303, `/${next.slice(1)}`);
          }
        }

        // return the user to an error page with instructions
        redirect(303, '/auth/auth-code-error');
      };
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    Create a new file at `src/pages/auth/callback.ts` and populate with the following:

    <NamedCodeBlock name="src/pages/auth/callback.ts">
      ```ts name=src/pages/auth/callback.ts
      import { createServerClient, parseCookieHeader } from '@supabase/ssr'
      import { type APIRoute } from 'astro'

      export const GET: APIRoute = async ({ request, cookies, redirect }) => {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'

        if (code) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(Astro.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    Astro.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next)
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error')
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    Create a new file at `app/routes/auth.callback.tsx` and populate with the following:

    <NamedCodeBlock name="app/routes/auth.callback.tsx">
      ```ts name=app/routes/auth.callback.tsx
      import { redirect, type LoaderFunctionArgs } from '@remix-run/node'
      import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

      export async function loader({ request }: LoaderFunctionArgs) {
        const requestUrl = new URL(request.url)
        const code = requestUrl.searchParams.get('code')
        const next = requestUrl.searchParams.get('next') || '/'
        const headers = new Headers()

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL!,
            process.env.SUPABASE_PUBLISHABLE_KEY!,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    headers.append('Set-Cookie', serializeCookieHeader(name, value, options))
                  )
                },
              },
            }
          )

          const { error } = await supabase.auth.exchangeCodeForSession(code)

          if (!error) {
            return redirect(next, { headers })
          }
        }

        // return the user to an error page with instructions
        return redirect('/auth/auth-code-error', { headers })
      }
      ```
    </NamedCodeBlock>
  </TabPanel>

  <TabPanel id="express" label="Express">
    Create a new route in your express app and populate with the following:

    <NamedCodeBlock name="app.js">
      ```js name=app.js
      ...
      app.get("/auth/callback", async function (req, res) {
        const code = req.query.code
        const next = req.query.next ?? "/"

        if (code) {
          const supabase = createServerClient(
            process.env.SUPABASE_URL,
            process.env.SUPABASE_PUBLISHABLE_KEY, {
          cookies: {
            getAll() {
              return parseCookieHeader(context.req.headers.cookie ?? '')
            },
            setAll(cookiesToSet) {
              cookiesToSet.forEach(({ name, value, options }) =>
                context.res.appendHeader('Set-Cookie', serializeCookieHeader(name, value, options))
              )
            },
          },
        })
          await supabase.auth.exchangeCodeForSession(code)
        }

        res.redirect(303, `/${next.slice(1)}`)
      })
      ```
    </NamedCodeBlock>
  </TabPanel>
</Tabs>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    When your user signs out, call [signOut()](/docs/reference/javascript/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signOut() {
      const { error } = await supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs out, call [signOut()](/docs/reference/dart/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```dart
    Future<void> signOut() async {
      await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [GitLab Account](https://gitlab.com)



---
**Navigation:** [← Previous](./30-clerk.md) | [Index](./index.md) | [Next →](./32-login-with-google.md)
