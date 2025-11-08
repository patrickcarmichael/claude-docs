**Navigation:** [← Previous](./32-login-with-google.md) | [Index](./index.md) | [Next →](./34-implicit-flow.md)

# Login with Notion



To enable Notion Auth for your project, you need to set up a Notion Application and add the Application OAuth credentials to your Supabase Dashboard.



## Overview

Setting up Notion logins for your application consists of 3 parts:

*   Create and configure a Notion Application [Notion Developer Portal](https://www.notion.so/my-integrations)
*   Retrieve your OAuth client ID and OAuth client secret and add them to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Create your notion integration

*   Go to [developers.notion.com](https://developers.notion.com/).
    {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

*   Click "View my integrations" and login.
    ![notion.so](/docs/img/guides/auth-notion/notion.png)

*   Once logged in, go to [notion.so/my-integrations](https://notion.so/my-integrations) and create a new integration.

*   When creating your integration, ensure that you select "Public integration" under "Integration type" and "Read user information including email addresses" under "Capabilities".

*   You will need to add a redirect URI, see [Add the redirect URI](#add-the-redirect-uri)

*   Once you've filled in the necessary fields, click "Submit" to finish creating the integration.

![notion.so](/docs/img/guides/auth-notion/notion-developer.png)



## Add the redirect URI

*   After selecting "Public integration", you should see an option to add "Redirect URIs".

![notion.so](/docs/img/guides/auth-notion/notion-redirect-uri.png)

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Notion** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Add your Notion credentials into your Supabase project

*   Once you've created your notion integration, you should be able to retrieve the "OAuth client ID" and "OAuth client secret" from the "OAuth Domain and URIs" tab.

![notion.so](/docs/img/guides/auth-notion/notion-creds.png)

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Notion** from the accordion list to expand and turn **Notion Enabled** to ON
*   Enter your **Notion Client ID** and **Notion Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `notion` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithNotion() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'notion',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `notion` as the `provider`:

    ```dart
    Future<void> signInWithNotion() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.notion,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Notion` as the `Provider`:

    ```kotlin
    suspend fun signInWithNotion() {
    	supabase.auth.signInWith(Notion)
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
*   [Notion Account](https://notion.so)
*   [Notion Developer Portal](https://www.notion.so/my-integrations)



# Login with Slack



To enable Slack Auth for your project, you need to set up a Slack OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

<Admonition type="caution">
  We will be replacing the existing Slack provider with a new Slack (OIDC) provider. Developers with Slack OAuth Applications created prior to 24th June 2024 should create a new application and migrate their credentials from the Slack provider to the Slack (OIDC) provider. Existing OAuth Applications built with the old Slack provider will continue to work up till 10th October. You can refer to the [**list of supported scopes**](https://api.slack.com/scopes?filter=user) for the new Slack (OIDC) User.
</Admonition>

Setting up Slack logins for your application consists of 3 parts:

*   Create and configure a Slack Project and App on the [Slack Developer Dashboard](https://api.slack.com/apps).
*   Add your Slack `API Key` and `API Secret Key` to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access your Slack Developer account

*   Go to [api.slack.com](https://api.slack.com/apps).
*   Click on `Your Apps` at the top right to log in.

![Slack Developer Portal.](/docs/img/guides/auth-slack/slack-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Slack** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Slack OAuth app

*   Go to [api.slack.com](https://api.slack.com/apps).
*   Click on `Create New App`

Under `Create an app...`:

*   Click `From scratch`
*   Type the name of your app
*   Select your `Slack Workspace`
*   Click `Create App`

Under `App Credentials`:

*   Copy and save your newly-generated `Client ID`
*   Copy and save your newly-generated `Client Secret`

Under the sidebar, select `OAuth & Permissions` and look for `Redirect URLs`:

*   Click `Add New Redirect URL`
*   Paste your `Callback URL` then click `Add`
*   Click `Save URLs`

Under `Scopes`:

*   Add the following scopes under the `User Token Scopes`: `profile`, `email`, `openid`. These scopes are the default scopes that Supabase Auth uses to request for user information. Do not add other scopes as [Sign In With Slack only supports `profile`, `email`, `openid`](https://api.slack.com/authentication/sign-in-with-slack#request).



## Enter your Slack credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Slack** from the accordion list to expand and turn **Slack Enabled** to ON
*   Enter your **Slack Client ID** and **Slack Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Slack (OIDC) auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Slack (OIDC) auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_slack_oidc_enabled": true,
    "external_slack_oidc_client_id": "your-slack-client-id",
    "external_slack_oidc_secret": "your-slack-client-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `slack_oidc` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithSlack() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'slack_oidc',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `slack` as the `provider`:

    ```dart
    Future<void> signInWithSlack() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.slack,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `SlackOIDC` as the `Provider`:

    ```kotlin
    suspend fun signInWithSlack() {
    	supabase.auth.signInWith(SlackOIDC)
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
*   [Slack Developer Dashboard](https://api.slack.com/apps)



# Login with Spotify



To enable Spotify Auth for your project, you need to set up a Spotify OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up Spotify logins for your application consists of 3 parts:

*   Create and configure a Spotify Project and App on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
*   Add your Spotify `API Key` and `API Secret Key` to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access your Spotify Developer account

*   Log into [Spotify](https://spotify.com)
*   Access the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

![Spotify Developer Portal.](/docs/img/guides/auth-spotify/spotify-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Spotify** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Spotify OAuth app

*   Log into [Spotify](https://spotify.com).
*   Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
*   Click `Create an App`
*   Type your `App name`
*   Type your `App description`
*   Check the box to agree with the `Developer TOS and Branding Guidelines`
*   Click `Create`
*   Save your `Client ID`
*   Save your `Client Secret`
*   Click `Edit Settings`

Under `Redirect URIs`:

*   Paste your Supabase Callback URL in the box
*   Click `Add`
*   Click `Save` at the bottom



## Enter your Spotify credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Spotify** from the accordion list to expand and turn **Spotify Enabled** to ON
*   Enter your **Spotify Client ID** and **Spotify Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Spotify auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Spotify auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_spotify_enabled": true,
    "external_spotify_client_id": "your-spotify-client-id",
    "external_spotify_secret": "your-spotify-client-secret"
  }'
```



## Add login code to your client app

The following outlines the steps to sign in using Spotify with Supabase Auth.

1.  Call the signin method from the client library.
2.  The user is redirected to the Spotify login page.
3.  After completing the sign-in process, the user will be redirected to your app with an error that says the email address needs to be confirmed. Simultaneously the user receives a confirmation email from Supabase Auth.
4.  The user clicks the confirmation link in the email.
5.  The user is brought back to the app and is now signed in.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `spotify` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithSpotify() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'spotify',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `spotify` as the `provider`:

    ```dart
    Future<void> signInWithSpotify() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.spotify,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Spotify` as the `Provider`:

    ```kotlin
    suspend fun signInWithSpotify() {
    	supabase.auth.signInWith(Spotify)
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
*   [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)



# Login with Twitch



To enable Twitch Auth for your project, you need to set up a Twitch Application and add the Application OAuth credentials to your Supabase Dashboard.



## Overview

Setting up Twitch logins for your application consists of 3 parts:

*   Create and configure a Twitch Application [Twitch Developer Console](https://dev.twitch.tv/console)
*   Add your Twitch OAuth Consumer keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your Twitch Developer account

*   Go to [dev.twitch.tv](https://dev.twitch.tv).
*   Click on `Log in with Twitch` at the top right to log in.
*   If you have not already enabled 2-Factor Authentication for your Twitch Account, you will need to do that at [Twitch Security Settings](https://www.twitch.tv/settings/security) before you can continue.

![Twitch Developer Page](/docs/img/guides/auth-twitch/twitch-developer-page.png)

*   Once logged in, go to the [Twitch Developer Console](https://dev.twitch.tv/console).

![Twitch Developer Console](/docs/img/guides/auth-twitch/twitch-console.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Twitch** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Twitch application

![Twitch Developer Console](/docs/img/guides/auth-twitch/twitch-console.png)

*   Click on `+ Register Your Application` at the top right.

![Register Application](/docs/img/guides/auth-twitch/twitch-register-your-application.png)

*   Enter the name of your application.
*   Type or paste your `OAuth Redirect URL` (the callback URL from the previous step.)
*   Select a category for your app.
*   Check the CAPTCHA box and click `Create`.



## Retrieve your Twitch OAuth client ID and client secret

*   Click `Manage` at the right of your application entry in the list.

![Twitch Applications List](/docs/img/guides/auth-twitch/twitch-applications-list.png)

*   Copy your Client ID.
*   Click `New Secret` to create a new Client Secret.
*   Copy your Client Secret.

![Get Client ID and Secret](/docs/img/guides/auth-twitch/twitch-get-keys.png)



## Add your Twitch credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Twitch** from the accordion list to expand and turn **Twitch Enabled** to ON
*   Enter your **Twitch Client ID** and **Twitch Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `twitch` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithTwitch() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'twitch',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `twitch` as the `provider`:

    ```dart
    Future<void> signInWithTwitch() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.twitch,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Twitch` as the `Provider`:

    ```kotlin
    suspend fun signInWithTwitch() {
    	supabase.auth.signInWith(Twitch)
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
*   [Twitch Account](https://twitch.tv)
*   [Twitch Developer Console](https://dev.twitch.tv/console)



# Login with Twitter



To enable Twitter Auth for your project, you need to set up a Twitter OAuth application and add the application credentials in the Supabase Dashboard.



## Overview

Setting up Twitter logins for your application consists of 3 parts:

*   Create and configure a Twitter Project and App on the [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard).
*   Add your Twitter `API Key` and `API Secret Key` to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access your Twitter Developer account

*   Go to [developer.twitter.com](https://developer.twitter.com).
*   Click on `Sign in` at the top right to log in.

![Twitter Developer Portal.](/docs/img/guides/auth-twitter/twitter-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Twitter** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Twitter OAuth app

*   Click `+ Create Project`.
    *   Enter your project name, click `Next`.
    *   Select your use case, click `Next`.
    *   Enter a description for your project, click `Next`.
    *   Enter a name for your app, click `Next`.
    *   Copy and save your `API Key` (this is your `client_id`).
    *   Copy and save your `API Secret Key` (this is your `client_secret`).
    *   Click on `App settings` to proceed to next steps.
*   At the bottom, you will find `User authentication settings`. Click on `Set up`.
*   Under `User authentication settings`, you can configure `App permissions`.
*   Make sure you turn ON `Request email from users`.
*   Select `Web App...` as the `Type of App`.
*   Under `App info` configure the following.
    *   Enter your `Callback URL`. Check the **Find your callback URL** section above to learn how to obtain your callback URL.
    *   Enter your `Website URL` (tip: try `http://127.0.0.1:port` or `http://www.localhost:port` during development)
    *   Enter your `Terms of service URL`.
    *   Enter your `Privacy policy URL`.
*   Click `Save`.



## Enter your Twitter credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Twitter** from the accordion list to expand and turn **Twitter Enabled** to ON
*   Enter your **Twitter Client ID** and **Twitter Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Twitter auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Twitter auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_twitter_enabled": true,
    "external_twitter_client_id": "your-twitter-api-key",
    "external_twitter_secret": "your-twitter-api-secret-key"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `twitter` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    async function signInWithTwitter() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'twitter',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `twitter` as the `provider`:

    ```dart
    Future<void> signInWithTwitter() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.twitter,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Twitter` as the `Provider`:

    ```kotlin
    suspend fun signInWithTwitter() {
    	supabase.auth.signInWith(Twitter)
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
*   [Twitter Developer Dashboard](https://developer.twitter.com/en/portal/dashboard)



# SSO and Social Login with WorkOS




## Use Social Login with WorkOS


### Step 1. Create a WorkOS organization

Log in to the WorkOS dashboard and visit the Organizations tab to create an organization.
![Create an Organization](/docs/img/guides/auth-workos/workos-create-organization.png)

Alternatively, you can [create an organization via the WorkOS API](https://workos.com/docs/reference/organization/create).



## Step 2. Obtain your `Client ID` and `WORKOS_API_KEY` values

![Get your Environment's Client ID and Secret](/docs/img/guides/auth-workos/workos-dashboard-get-client-id-and-key.png)

Visit the getting started page of the [WorkOS Dashboard](https://dashboard.workos.com/get-started). Copy the following values from the Quickstart panel:

*   `WORKOS_CLIENT_ID`
*   `WORKOS_API_KEY`

<Admonition type="tip">
  You must be signed in to see these values.
</Admonition>



## Step 3. Add your WorkOS credentials to your Supabase project

![Enter your WorkOS application details in your Supabase app's auth provider settings panel](/docs/img/guides/auth-workos/supabase-workos-configuration.png)

1.  Go to your Supabase Project Dashboard.
2.  In the left sidebar, click the Authentication icon (near the top).
3.  Click on Providers under the Configuration section.
4.  Click on WorkOS from the accordion list to expand.
5.  Toggle the `WorkOS Enabled` switch to ON.
6.  Enter `https://api.workos.com` in the WorkOS URL field.
7.  Enter your WorkOS Client ID and WorkOS Client Secret saved in the previous step.
8.  Copy the `Callback URL (for OAuth)` value from the form and save it somewhere handy.
9.  Click Save.

You can also configure the WorkOS auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure WorkOS auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_workos_enabled": true,
    "external_workos_url": "https://api.workos.com",
    "external_workos_client_id": "your-workos-client-id",
    "external_workos_secret": "your-workos-client-secret"
  }'
```



## Step 4. Set your Supabase redirect URI in the WorkOS Dashboard

Visit the WorkOS dashboard and click the redirects button in the left navigation panel.

On the redirects page, enter your Supabase project's `Callback URL (for OAuth)` which you saved in the previous step, as shown below:

![Set your Supbase project redirect URL in the WorkOS dashboard](/docs/img/guides/auth-workos/workos-set-supabase-redirect.png)



## Step 5. Add login code to your client app

When a user signs in, call `signInWithOAuth` with `workos` as the provider.

```javascript
import { createClient } from '@supabase/supabase-js';
const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>');
const redirect = (url: string) => {}

// ---cut---
async function signInWithWorkOS() {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider: 'workos',
    options: {
      redirectTo: 'http://example.com/auth/v1/callback', // Make sure your redirect URL is configured in the Supabase Dashboard Auth settings
      queryParams: {
        connection: '<connection_id>',
      },
    },
  })

  if (data.url) {
    redirect(data.url) // use the redirect API for your server or framework
  }
}
```

<Admonition type="tip">
  You can find your `connection_id` in the WorkOS dashboard under the Organizations tab. Select your organization and then click View connection.
</Admonition>

Within your specified callback URL, you'll exchange the code for a logged-in user profile:

```javascript auth/v1/callback/route.ts
import { NextResponse } from 'next/server'
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



## Resources

*   [WorkOS Documentation](https://workos.com/docs/sso/guide)



# Login with Zoom



To enable Zoom Auth for your project, you need to set up a Zoom OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up Zoom logins for your application consists of 3 parts:

*   Create and configure a Zoom OAuth App on [Zoom App Marketplace](https://marketplace.zoom.us/)
*   Add your Zoom OAuth keys to your [Supabase Project](/dashboard)
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js)



## Access your Zoom Developer account

*   Go to [marketplace.zoom.us](https://marketplace.zoom.us/).
*   Click on `Sign In` at the top right to log in.

![Zoom Developer Portal.](/docs/img/guides/auth-zoom/zoom-portal.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Zoom** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a Zoom OAuth app

*   Go to [marketplace.zoom.us](https://marketplace.zoom.us/).
*   Click on `Sign In` at the top right to log in.
*   Click `Build App` (from the dropdown Develop)
*   In the OAuth card, click `Create`
*   Type the name of your app
*   Choose app type
*   Click `Create`

Under `App credentials`

*   Copy and save your `Client ID`.
*   Copy and save your `Client secret`.
*   Add your `Callback URL` in the OAuth allow list.

Under `Redirect URL for OAuth`

*   Paste your `Callback URL`

Under `Scopes`

*   Click on `Add scopes`
*   Click on `User`
*   Choose `user:read`
*   Click `Done`
*   Click `Continue`



## Enter your Zoom credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Zoom** from the accordion list to expand and turn **Zoom Enabled** to ON
*   Enter your **Zoom Client ID** and **Zoom Client Secret** saved in the previous step
*   Click `Save`

You can also configure the Zoom auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Zoom auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_zoom_enabled": true,
    "external_zoom_client_id": "your-zoom-client-id",
    "external_zoom_secret": "your-zoom-client-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `zoom` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithZoom() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'zoom',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `zoom` as the `provider`:

    ```dart
    Future<void> signInWithZoom() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.zoom,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Zoom` as the `Provider`:

    ```kotlin
    suspend fun signInWithZoom() {
    	supabase.auth.signInWith(Zoom)
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
*   [Zoom App Marketplace](https://marketplace.zoom.us/)



---
**Navigation:** [← Previous](./32-login-with-google.md) | [Index](./index.md) | [Next →](./34-implicit-flow.md)
