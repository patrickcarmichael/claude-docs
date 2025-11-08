**Navigation:** [← Previous](./33-login-with-notion.md) | [Index](./index.md) | [Next →](./35-use-supabase-auth-with-nextjs.md)

# Implicit flow

About authenticating with implicit flow.

The implicit flow is one of two ways that a user can authenticate and your app can receive the necessary access and refresh tokens.

The flow is an implementation detail handled for you by Supabase Auth, but understanding the difference between implicit and [PKCE flow](/docs/guides/auth/sessions/pkce-flow) is important for understanding the difference between client-only and server-side auth.



## How it works

After a successful signin, the user is redirected to your app with a URL that looks like this:

```
https://yourapp.com/...#access_token=<...>&refresh_token=<...>&...
```

The access and refresh tokens are contained in the URL fragment.

The client libraries:

*   Detect this type of URL
*   Extract the access token, refresh token, and some extra information
*   Persist this information to local storage for further use by the library and your app



## Limitations

The implicit flow only works on the client. Web browsers do not send the URL fragment to the server by design. This is a security feature:

*   You may be hosting your single-page app on a third-party server. The third-party service shouldn't get access to your user's credentials.
*   Even if the server is under your direct control, `GET` requests and their full URLs are often logged. This approach avoids leaking credentials in request or access logs.

If you wish to obtain the access token and refresh token on a server, use the [PKCE flow](/docs/guides/auth/sessions/pkce-flow).



# PKCE flow

About authenticating with PKCE flow.

The Proof Key for Code Exchange (PKCE) flow is one of two ways that a user can authenticate and your app can receive the necessary access and refresh tokens.

The flow is an implementation detail handled for you by Supabase Auth, but understanding the difference between PKCE and [implicit flow](/docs/guides/auth/sessions/implicit-flow) is important for understanding the difference between client-only and server-side auth.



## How it works

After a successful verification, the user is redirected to your app with a URL that looks like this:

```
https://yourapp.com/...?code=<...>
```

The `code` parameter is commonly known as the Auth Code and can be exchanged for an access token by calling `exchangeCodeForSession(code)`.

<Admonition type="note">
  For security purposes, the code has a validity of 5 minutes and can only be exchanged for an access token once. You will need to restart the authentication flow from scratch if you wish to obtain a new access token.
</Admonition>

As the flow is run server side, `localStorage` may not be available. You may configure the client library to use a custom storage adapter and an alternate backing storage such as cookies by setting the `storage` option to an object with the following methods:

```js
import { type SupportedStorage } from '@supabase/supabase-js';
const supportsLocalStorage = () => true

// ---cut---
const customStorageAdapter: SupportedStorage = {
    getItem: (key) => {
    if (!supportsLocalStorage()) {
        // Configure alternate storage
        return null
    }
    return globalThis.localStorage.getItem(key)
    },
    setItem: (key, value) => {
    if (!supportsLocalStorage()) {
        // Configure alternate storage here
        return
    }
    globalThis.localStorage.setItem(key, value)
    },
    removeItem: (key) => {
    if (!supportsLocalStorage()) {
        // Configure alternate storage here
        return
    }
    globalThis.localStorage.removeItem(key)
    },
}
```

You may also configure the client library to automatically exchange it for a session after a successful redirect. This can be done by setting the `detectSessionInUrl` option to `true`.

Putting it all together, your client library initialization may look like this:

```js
import { createClient } from '@supabase/supabase-js'

// ---cut---
const supabase = createClient('https://xyzcompany.supabase.co', 'publishable-or-anon-key', {
  // ...
  auth: {
    // ...
    detectSessionInUrl: true,
    flowType: 'pkce',
    storage: {
      getItem: () => Promise.resolve('FETCHED_TOKEN'),
      setItem: () => {},
      removeItem: () => {},
    },
  },
  // ...
})
```



## Limitations

Behind the scenes, the code exchange requires a code verifier. Both the code in the URL and the code verifier are sent back to the Auth server for a successful exchange.

The code verifier is created and stored locally when the Auth flow is first initiated. That means the code exchange must be initiated on the same browser and device where the flow was started.



## Resources

*   [OAuth 2.0 guide](https://oauth.net/2/pkce/) to PKCE flow



# Advanced guide

Details about SSR Auth flows and implementation for advanced users.

When a user authenticates with Supabase Auth, two pieces of information are issued by the server:

1.  **Access token** in the form of a JWT.
2.  **Refresh token** which is a randomly generated string.

The default behavior if you're not using SSR is to store this information in local storage. Local storage isn't accessible by the server, so for SSR, the tokens instead need to be stored in a secure cookie. The cookie can then be passed back and forth between your app code in the client and your app code in the server.

If you're not using SSR, you might also be using the [implicit flow](/docs/guides/auth/sessions/implicit-flow) to get the access and refresh tokens. The server can't access the tokens in this flow, so for SSR, you should change to the [PKCE flow](/docs/guides/auth/sessions/pkce-flow). You can change the flow type when initiating your Supabase client if your client library provides this option.

<Admonition type="tip">
  In the `@supabase/ssr` package, Supabase clients are initiated to use the PKCE flow by default. They are also automatically configured to handle the saving and retrieval of session information in cookies.
</Admonition>



## How it works

In the PKCE flow, a redirect is made to your app, with an Auth Code contained in the URL. When you exchange this code using `exchangeCodeForSession`, you receive the session information, which contains the access and refresh tokens.

To maintain the session, these tokens must be stored in a storage medium securely shared between client and server, which is traditionally cookies. Whenever the session is refreshed, the auth and refresh tokens in the shared storage medium must be updated. Supabase client libraries provide a customizable `storage` option when a client is initiated, allowing you to change where tokens are stored.



## Frequently asked questions

{/* supa-mdx-lint-disable Rule004ExcludeWords */}


### No session on the server side with Next.js route prefetching?

When you use route prefetching in Next.js using `<Link href="/...">` components or the `Router.push()` APIs can send server-side requests before the browser processes the access and refresh tokens. This means that those requests may not have any cookies set and your server code will render unauthenticated content.

To improve experience for your users, we recommend redirecting users to one specific page after sign-in that does not include any route prefetching from Next.js. Once the Supabase client library running in the browser has obtained the access and refresh tokens from the URL fragment, you can send users to any pages that use prefetching.


### How do I make the cookies `HttpOnly`?

This is not necessary. Both the access token and refresh token are designed to be passed around to different components in your application. The browser-based side of your application needs access to the refresh token to properly maintain a browser session anyway.

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


### My server is getting invalid refresh token errors. What's going on?

It is likely that the refresh token sent from the browser to your server is stale. Make sure the `onAuthStateChange` listener callback is free of bugs and is registered relatively early in your application's lifetime

When you receive this error on the server-side, try to defer rendering to the browser where the client library can access an up-to-date refresh token and present the user with a better experience.


### Should I set a shorter `Max-Age` parameter on the cookies?

The `Max-Age` or `Expires` cookie parameters only control whether the browser sends the value to the server. Since a refresh token represents the long-lived authentication session of the user on that browser, setting a short `Max-Age` or `Expires` parameter on the cookies only results in a degraded user experience.

The only way to ensure that a user has logged out or their session has ended is to get the user's details with `getUser()`. The `getClaims()` method only checks local JWT validation (signature and expiration), but it doesn't verify with the auth server whether the session is still valid or if the user has logged out server-side.


### What should I use for the `SameSite` property?

Make sure you [understand the behavior of the property in different situations](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite) as some properties can degrade the user experience.

A good default is to use `Lax` which sends cookies when users are navigating to your site. Cookies typically require the `Secure` attribute, which only sends them over HTTPS. However, this can be a problem when developing on `localhost`.


### Can I use server-side rendering with a CDN or cache?

Yes, but you need to be careful to include at least the refresh token cookie value in the cache key. Otherwise you may be accidentally serving pages with data belonging to different users!

Also be sure you set proper cache control headers. We recommend invalidating cache keys every hour or less.


### Which authentication flows have PKCE support?

At present, PKCE is supported on the Magic Link, OAuth, Sign Up, and Password Recovery routes. These correspond to the `signInWithOtp`, `signInWithOAuth`, `signUp`, and `resetPasswordForEmail` methods on the Supabase client library. When using PKCE with Phone and Email OTPs, there is no behavior change with respect to the implicit flow - an access token will be returned in the body when a request is successful.



# Creating a Supabase client for SSR

Configure your Supabase client to use cookies

To use Server-Side Rendering (SSR) with Supabase, you need to configure your Supabase client to use cookies. The `@supabase/ssr` package helps you do this for JavaScript/TypeScript applications.



## Install

Install the `@supabase/ssr` and `@supabase/supabase-js` packages:

<Tabs size="small" type="underlined" queryGroup="package-manager" defaultActiveId="npm">
  <TabPanel id="npm" label="npm">
    ```bash
    npm install @supabase/ssr @supabase/supabase-js
    ```
  </TabPanel>

  <TabPanel id="yarn" label="yarn">
    ```bash
    yarn add @supabase/ssr @supabase/supabase-js
    ```
  </TabPanel>

  <TabPanel id="pnpm" label="pnpm">
    ```bash
    pnpm add @supabase/ssr @supabase/supabase-js
    ```
  </TabPanel>
</Tabs>



## Set environment variables

In your environment variables file, set your Supabase URL and Key:

<ProjectConfigVariables variable="url" />

<ProjectConfigVariables variable="publishable" />

<ProjectConfigVariables variable="anon" />

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    ```bash .env.local
    NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
    NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    ```bash .env.local
    PUBLIC_SUPABASE_URL=your_supabase_project_url
    PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    ```bash .env
    PUBLIC_SUPABASE_URL=your_supabase_project_url
    PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    ```bash .env
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```
  </TabPanel>

  <TabPanel id="react-router" label="React Router">
    ```bash .env
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_ANON_KEY=your_supabase_anon_key
    ```
  </TabPanel>

  <TabPanel id="express" label="Express">
    ```bash .env
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```

    Install [dotenv](https://www.npmjs.com/package/dotenv):

    ```bash
    npm i dotenv
    ```

    And initialize it:

    <Tabs size="small" type="underlined" queryGroup="package-manager" defaultActiveId="npm">
      <TabPanel id="npm" label="npm">
        ```bash
        npm install dotenv
        ```
      </TabPanel>

      <TabPanel id="yarn" label="yarn">
        ```bash
        yarn add dotenv
        ```
      </TabPanel>

      <TabPanel id="pnpm" label="pnpm">
        ```bash
        pnpm add dotenv
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="hono" label="Hono">
    ```bash .env
    SUPABASE_URL=your_supabase_project_url
    SUPABASE_PUBLISHABLE_KEY=sb_publishable_... or anon keyY
    ```
  </TabPanel>
</Tabs>



## Create a client

You'll need some one-time setup code to configure your Supabase client to use cookies. Once your utility code is set up, you can use your new `createClient` utility functions to get a properly configured Supabase client.

Use the browser client in code that runs on the browser, and the server client in code that runs on the server.

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    The following code samples are for App Router. For help with Pages Router, see the [Next.js Server-Side Auth guide](/docs/guides/auth/server-side/nextjs?queryGroups=router\&router=pages).

    <Tabs scrollable size="small" type="underlined" defaultActiveId="client-component" queryGroup="environment">
      <TabPanel id="client" label="Client-side">
        ```ts utils/supabase/client.ts
        import { createBrowserClient } from '@supabase/ssr'

        export function createClient() {
          return createBrowserClient(
            process.env.NEXT_PUBLIC_SUPABASE_URL!,
            process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
          )
        }
        ```
      </TabPanel>

      <TabPanel id="server" label="Server-side">
        ```ts utils/supabase/server.ts
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

      <TabPanel id="middleware" label="Middleware">
        In Next.js, because Server Components cannot set cookies, you'll also need a middleware client to handle cookie refreshes. The middleware should run before every route that needs access to Supabase, or that is protected by Supabase Auth.

        ```ts middleware.ts
        import { type NextRequest } from 'next/server'
        import { updateSession } from '@/utils/supabase/middleware'

        export async function middleware(request: NextRequest) {
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

        ```ts utils/supabase/middleware.ts
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

          // IMPORTANT: Avoid writing any logic between createServerClient and
          // supabase.auth.getClaims(). A simple mistake could make it very hard to debug
          // issues with users being randomly logged out.

          // IMPORTANT: Don't remove getClaims()
          const { data } = await supabase.auth.getClaims()

          const user = data?.claims

          if (
            !user &&
            !request.nextUrl.pathname.startsWith('/login') &&
            !request.nextUrl.pathname.startsWith('/auth')
          ) {
            // no user, potentially respond by redirecting the user to the login page
            const url = request.nextUrl.clone()
            url.pathname = '/login'
            return NextResponse.redirect(url)
          }

          // IMPORTANT: You *must* return the supabaseResponse object as it is. If you're
          // creating a new response object with NextResponse.next() make sure to:
          // 1. Pass the request in it, like so:
          //    const myNewResponse = NextResponse.next({ request })
          // 2. Copy over the cookies, like so:
          //    myNewResponse.cookies.setAll(supabaseResponse.cookies.getAll())
          // 3. Change the myNewResponse object to fit your needs, but avoid changing
          //    the cookies!
          // 4. Finally:
          //    return myNewResponse
          // If this is not done, you may be causing the browser and server to go out
          // of sync and terminate the user's session prematurely!

          return supabaseResponse
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="hooks" queryGroup="environment">
      <TabPanel id="hooks" label="Hooks">
        ```ts hooks.server.ts
        import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public'
        import { createServerClient } from '@supabase/ssr'
        import type { Handle } from '@sveltejs/kit'

        export const handle: Handle = async ({ event, resolve }) => {
          event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {
            cookies: {
              getAll() {
                return event.cookies.getAll()
              },
              setAll(cookiesToSet) {
                /**
                 * Note: You have to add the `path` variable to the
                 * set and remove method due to sveltekit's cookie API
                 * requiring this to be set, setting the path to an empty string
                 * will replicate previous/standard behavior (https://kit.svelte.dev/docs/types#public-types-cookies)
                 */
                cookiesToSet.forEach(({ name, value, options }) =>
                  event.cookies.set(name, value, { ...options, path: '/' })
                )
              },
            },
          })

          /**
           * Unlike `supabase.auth.getSession()`, which returns the session _without_
           * validating the JWT, this function also calls `getUser()` to validate the
           * JWT before returning the session.
           */
          event.locals.safeGetSession = async () => {
            const {
              data: { session },
            } = await event.locals.supabase.auth.getSession()
            if (!session) {
              return { session: null, user: null }
            }

            const {
              data: { user },
              error,
            } = await event.locals.supabase.auth.getUser()
            if (error) {
              // JWT validation has failed
              return { session: null, user: null }
            }

            return { session, user }
          }

          return resolve(event, {
            filterSerializedResponseHeaders(name) {
              return name === 'content-range' || name === 'x-supabase-api-version'
            },
          })
        }
        ```
      </TabPanel>

      <TabPanel id="layout" label="Root Layout Load">
        Page components can get access to the Supabase client from the `data` object due to this load function.

        ```ts +layout.ts
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
      </TabPanel>

      <TabPanel id="layout-server" label="Root Server Layout">
        ```ts +layout.server.ts
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
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="astro" label="Astro">
    By default, Astro apps are static. This means the requests for data happen at build time, rather than when the user requests a page. At build time, there is no user, session or cookies. Therefore, we need to configure Astro for Server-side Rendering (SSR) if you want data to be fetched dynamically per request.

    ```js astro.config.mjs
    import { defineConfig } from 'astro/config'

    export default defineConfig({
      output: 'server',
    })
    ```

    <Tabs scrollable size="small" type="underlined" defaultActiveId="astro-server" queryGroup="environment">
      <TabPanel id="astro-server" label="Server">
        ```ts index.astro
        ---
        import { createServerClient, parseCookieHeader } from "@supabase/ssr";

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
                  Astro.cookies.set(name, value, options))
              },
            },
          }
        );
        ---
        ```
      </TabPanel>

      <TabPanel id="astro-browser" label="Browser">
        ```html index.astro
        <script>
          import { createBrowserClient } from "@supabase/ssr";

          const supabase = createBrowserClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY
          );
        </script>
        ```
      </TabPanel>

      <TabPanel id="astro-server-endpoint" label="Server Endpoint">
        ```ts route.ts
        import { createServerClient, parseCookieHeader } from "@supabase/ssr";
        import type { APIContext } from "astro";

        export async function GET(context: APIContext) {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(context.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    context.cookies.set(name, value, options))
                },
              },
            }
          );

          return ...
        }
        ```
      </TabPanel>

      <TabPanel id="astro-middleware" label="Middleware">
        ```ts middleware.ts
        import { createServerClient, parseCookieHeader } from '@supabase/ssr'
        import { defineMiddleware } from 'astro:middleware'

        export const onRequest = defineMiddleware(async (context, next) => {
          const supabase = createServerClient(
            import.meta.env.PUBLIC_SUPABASE_URL,
            import.meta.env.PUBLIC_SUPABASE_PUBLISHABLE_KEY,
            {
              cookies: {
                getAll() {
                  return parseCookieHeader(context.request.headers.get('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) =>
                    context.cookies.set(name, value, options)
                  )
                },
              },
            }
          )

          return next()
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="remix-loader" queryGroup="environment">
      <TabPanel id="remix-loader" label="Loader">
        ```ts _index.tsx
        import { type LoaderFunctionArgs } from '@remix-run/node'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

        export async function loader({ request }: LoaderFunctionArgs) {
          const headers = new Headers()

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

          return new Response('...', {
            headers,
          })
        }
        ```
      </TabPanel>

      <TabPanel id="remix-action" label="Action">
        ```ts _index.tsx
        import { type ActionFunctionArgs } from '@remix-run/node'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

        export async function action({ request }: ActionFunctionArgs) {
          const headers = new Headers()

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

          return new Response('...', {
            headers,
          })
        }
        ```
      </TabPanel>

      <TabPanel id="remix-component" label="Component">
        ```ts _index.tsx
        import { type LoaderFunctionArgs } from "@remix-run/node";
        import { useLoaderData } from "@remix-run/react";
        import { createBrowserClient } from "@supabase/ssr";

        export async function loader({}: LoaderFunctionArgs) {
          return {
            env: {
              SUPABASE_URL: process.env.SUPABASE_URL!,
              SUPABASE_PUBLISHABLE_KEY: process.env.SUPABASE_PUBLISHABLE_KEY!,
            },
          };
        }

        export default function Index() {
          const { env } = useLoaderData<typeof loader>();

          const supabase = createBrowserClient(env.SUPABASE_URL, env.SUPABASE_PUBLISHABLE_KEY);

          return ...
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="react-router" label="React Router">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="react-router-loader" queryGroup="environment">
      <TabPanel id="react-router-loader" label="Loader">
        ```ts _index.tsx
        import { LoaderFunctionArgs } from 'react-router'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

        export async function loader({ request }: LoaderFunctionArgs) {
          const headers = new Headers()

          const supabase = createServerClient(process.env.SUPABASE_URL!, process.env.SUPABASE_ANON_KEY!, {
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
          })

          return new Response('...', {
            headers,
          })
        }
        ```
      </TabPanel>

      <TabPanel id="react-router-action" label="Action">
        ```ts _index.tsx
        import { type ActionFunctionArgs } from '@react-router'
        import { createServerClient, parseCookieHeader, serializeCookieHeader } from '@supabase/ssr'

        export async function action({ request }: ActionFunctionArgs) {
          const headers = new Headers()

          const supabase = createServerClient(process.env.SUPABASE_URL!, process.env.SUPABASE_ANON_KEY!, {
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
          })

          return new Response('...', {
            headers,
          })
        }
        ```
      </TabPanel>

      <TabPanel id="react-router-component" label="Component">
        ```ts _index.tsx
        import { type LoaderFunctionArgs } from "react-router";
        import { useLoaderData } from "react-router";
        import { createBrowserClient } from "@supabase/ssr";

        export async function loader({}: LoaderFunctionArgs) {
          return {
            env: {
              SUPABASE_URL: process.env.SUPABASE_URL!,
              SUPABASE_ANON_KEY: process.env.SUPABASE_ANON_KEY!,
            },
          };
        }

        export default function Index() {
          const { env } = useLoaderData<typeof loader>();

          const supabase = createBrowserClient(env.SUPABASE_URL, env.SUPABASE_ANON_KEY);

          return ...
        }
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="express" label="Express">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="server-client" queryGroup="environment">
      <TabPanel id="server-client" label="Server Client">
        ```ts lib/supabase.js
        const { createServerClient, parseCookieHeader, serializeCookieHeader } = require('@supabase/ssr')

        exports.createClient = (context) => {
          return createServerClient(process.env.SUPABASE_URL, process.env.SUPABASE_PUBLISHABLE_KEY, {
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
        }
        ```
      </TabPanel>

      <TabPanel id="express-route" label="Route">
        ```ts app.js
        const express = require("express")
        const dotenv = require("dotenv")

        const { createClient } = require("./lib/supabase")

        const app = express()

        app.post("/hello-world", async function (req, res, next) {
          const { email, emailConfirm } = req.body
          ...

          const supabase = createClient({ req, res })
        })
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>

  <TabPanel id="hono" label="Hono">
    <Tabs scrollable size="small" type="underlined" defaultActiveId="server-client" queryGroup="environment">
      <TabPanel id="server-client" label="Server Client">
        Create a Hono middleware that creates a Supabase client.

        ```ts middleware/auth.middleware.ts
        import { createServerClient, parseCookieHeader } from '@supabase/ssr'
        import { SupabaseClient } from '@supabase/supabase-js'
        import type { Context, MiddlewareHandler } from 'hono'
        import { env } from 'hono/adapter'
        import { setCookie } from 'hono/cookie'

        declare module 'hono' {
          interface ContextVariableMap {
            supabase: SupabaseClient
          }
        }

        export const getSupabase = (c: Context) => {
          return c.get('supabase')
        }

        type SupabaseEnv = {
          SUPABASE_URL: string
          SUPABASE_PUBLISHABLE_KEY: string
        }

        export const supabaseMiddleware = (): MiddlewareHandler => {
          return async (c, next) => {
            const supabaseEnv = env<SupabaseEnv>(c)
            const supabaseUrl = supabaseEnv.SUPABASE_URL
            const supabaseAnonKey = supabaseEnv.SUPABASE_PUBLISHABLE_KEY

            if (!supabaseUrl) {
              throw new Error('SUPABASE_URL missing!')
            }

            if (!supabaseAnonKey) {
              throw new Error('SUPABASE_PUBLISHABLE_KEY missing!')
            }

            const supabase = createServerClient(supabaseUrl, supabaseAnonKey, {
              cookies: {
                getAll() {
                  return parseCookieHeader(c.req.header('Cookie') ?? '')
                },
                setAll(cookiesToSet) {
                  cookiesToSet.forEach(({ name, value, options }) => setCookie(c, name, value, options))
                },
              },
            })

            c.set('supabase', supabase)

            await next()
          }
        }
        ```
      </TabPanel>

      <TabPanel id="hono-route" label="Route">
        You can now use this middleware in your Hono application to create a server Supabase client that can be used to make authenticated requests.

        ```ts index.tsx
        import { Hono } from 'hono'
        import { getSupabase, supabaseMiddleware } from './middleware/auth.middleware'

        const app = new Hono()
        app.use('*', supabaseMiddleware())

        app.get('/api/user', async (c) => {
          const supabase = getSupabase(c)
          const { data, error } = await supabase.auth.getUser()

          if (error) console.log('error', error)

          if (!data?.user) {
            return c.json({
              message: 'You are not logged in.',
            })
          }

          return c.json({
            message: 'You are logged in!',
            userId: data.user,
          })
        })

        app.get('/signout', async (c) => {
          const supabase = getSupabase(c)
          await supabase.auth.signOut()
          console.log('Signed out server-side!')
          return c.redirect('/')
        })

        // Retrieve data with RLS enabled. The signed in user's auth token is automatically sent.
        app.get('/countries', async (c) => {
          const supabase = getSupabase(c)
          const { data, error } = await supabase.from('countries').select('*')
          if (error) console.log(error)
          return c.json(data)
        })

        export default app
        ```
      </TabPanel>
    </Tabs>
  </TabPanel>
</Tabs>



## Next steps

*   Implement [Authentication using Email and Password](/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)
*   Implement [Authentication using OAuth](/docs/guides/auth/server-side/oauth-with-pkce-flow-for-ssr)
*   [Learn more about SSR](/docs/guides/auth/server-side-rendering)



# Migrating to the SSR package from Auth Helpers



The new `ssr` package takes the core concepts of the Auth Helpers and makes them available to any server language or framework. This page will guide you through migrating from the Auth Helpers package to `ssr`.


### Replacing Supabase packages

<Tabs scrollable size="small" type="underlined" defaultActiveId="nextjs" queryGroup="framework">
  <TabPanel id="nextjs" label="Next.js">
    ```bash
    npm uninstall @supabase/auth-helpers-nextjs
    ```
  </TabPanel>

  <TabPanel id="sveltekit" label="SvelteKit">
    ```bash
    npm uninstall @supabase/auth-helpers-sveltekit
    ```
  </TabPanel>

  <TabPanel id="remix" label="Remix">
    ```bash
    npm uninstall @supabase/auth-helpers-remix
    ```
  </TabPanel>
</Tabs>

```bash
npm install @supabase/ssr
```


### Creating a client

The new `ssr` package exports two functions for creating a Supabase client. The `createBrowserClient` function is used in the client, and the `createServerClient` function is used in the server.

Check out the [Creating a client](/docs/guides/auth/server-side/creating-a-client) page for examples of creating a client in your framework.



## Next steps

*   Implement [Authentication using Email and Password](/docs/guides/auth/server-side/email-based-auth-with-pkce-flow-for-ssr)
*   Implement [Authentication using OAuth](/docs/guides/auth/server-side/oauth-with-pkce-flow-for-ssr)
*   [Learn more about SSR](/docs/guides/auth/server-side-rendering)



# Setting up Server-Side Auth for Next.js



Next.js comes in two flavors: the [App Router](https://nextjs.org/docs/app) and the [Pages Router](https://nextjs.org/docs/pages). You can set up Server-Side Auth with either strategy. You can even use both in the same application.

<Tabs scrollable size="small" type="underlined" defaultActiveId="app" queryGroup="router">
  <TabPanel id="app" label="App Router">
    <StepHikeCompact>
      <StepHikeCompact.Step step={1}>
        <StepHikeCompact.Details title="Install Supabase packages">
          Install the `@supabase/supabase-js` package and the helper `@supabase/ssr` package.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```sh
          npm install @supabase/supabase-js @supabase/ssr
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={2}>
        <StepHikeCompact.Details title="Set up environment variables">
          Create a `.env.local` file in your project root directory.

          Fill in your `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`:

          <ProjectConfigVariables variable="url" />

          <ProjectConfigVariables variable="publishable" />

          <ProjectConfigVariables variable="anon" />
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id=".env.local" label=".env.local">
              ```txt name=.env.local
              NEXT_PUBLIC_SUPABASE_URL=<your_supabase_project_url>
              NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=<sb_publishable_... or anon keyY>
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={3}>
        <StepHikeCompact.Details title="Write utility functions to create Supabase clients">
          To access Supabase from your Next.js app, you need 2 types of Supabase clients:

          1.  **Client Component client** - To access Supabase from Client Components, which run in the browser.
          2.  **Server Component client** - To access Supabase from Server Components, Server Actions, and Route Handlers, which run only on the server.

          Create a `utils/supabase` folder at the root of your project, or inside the `./src` folder if you are using one, with a file for each type of client. Then copy the utility functions for each client type.

          <Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6">
            <div className="border-b mt-3 pb-3">
              <AccordionItem header={<span className="text-foreground">What does the `cookies` object do?</span>} id="utility-cookies">
                The cookies object lets the Supabase client know how to access the cookies, so it can read and write the user session data. To make `@supabase/ssr` framework-agnostic, the cookies methods aren't hard-coded. These utility functions adapt `@supabase/ssr`'s cookie handling for Next.js.

                The `set` and `remove` methods for the server client need error handlers, because Next.js throws an error if cookies are set from Server Components. You can safely ignore this error because you'll set up middleware in the next step to write refreshed cookies to storage.

                The cookie is named `sb-<project_ref>-auth-token` by default.
              </AccordionItem>
            </div>

            <div className="border-b mt-3 pb-3">
              <AccordionItem header={<span className="text-foreground">Do I need to create a new client for every route?</span>} id="client-deduplication">
                Yes! Creating a Supabase client is lightweight.

                *   On the server, it basically configures a `fetch` call. You need to reconfigure the fetch call anew for every request to your server, because you need the cookies from the request.
                *   On the client, `createBrowserClient` already uses a singleton pattern, so you only ever create one instance, no matter how many times you call your `createClient` function.
              </AccordionItem>
            </div>
          </Accordion>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="utils/supabase/client.ts" label="utils/supabase/client.ts">
              ```ts name=utils/supabase/client.ts
              import { createBrowserClient } from '@supabase/ssr'

              export function createClient() {
                return createBrowserClient(
                  process.env.NEXT_PUBLIC_SUPABASE_URL!,
                  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
                )
              }
              ```
            </TabPanel>

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

      <StepHikeCompact.Step step={4}>
        <StepHikeCompact.Details title="Hook up middleware">
          Create a `middleware.ts` file at the root of your project, or inside the `./src` folder if you are using one.

          Since Server Components can't write cookies, you need middleware to refresh expired Auth tokens and store them.

          The middleware is responsible for:

          1.  Refreshing the Auth token (by calling `supabase.auth.getUser`).
          2.  Passing the refreshed Auth token to Server Components, so they don't attempt to refresh the same token themselves. This is accomplished with `request.cookies.set`.
          3.  Passing the refreshed Auth token to the browser, so it replaces the old token. This is accomplished with `response.cookies.set`.

          Copy the middleware code for your app.

          Add a [matcher](https://nextjs.org/docs/app/building-your-application/routing/middleware#matching-paths) so the middleware doesn't run on routes that don't access Supabase.

          <Admonition type="danger">
            Be careful when protecting pages. The server gets the user session from the cookies, which can be spoofed by anyone.

            Always use `supabase.auth.getUser()` to protect pages and user data.

            *Never* trust `supabase.auth.getSession()` inside server code such as middleware. It isn't guaranteed to revalidate the Auth token.

            It's safe to trust `getUser()` because it sends a request to the Supabase Auth server every time to revalidate the Auth token.
          </Admonition>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="middleware.ts" label="middleware.ts">
              ```ts name=middleware.ts
              import { type NextRequest } from 'next/server'
              import { updateSession } from '@/utils/supabase/middleware'

              export async function middleware(request: NextRequest) {
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

            <TabPanel id="utils/supabase/middleware.ts" label="utils/supabase/middleware.ts">
              ```ts name=utils/supabase/middleware.ts
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
                        cookiesToSet.forEach(({ name, value }) => request.cookies.set(name, value))
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

                // Do not run code between createServerClient and
                // supabase.auth.getUser(). A simple mistake could make it very hard to debug
                // issues with users being randomly logged out.

                // IMPORTANT: DO NOT REMOVE auth.getUser()

                const {
                  data: { user },
                } = await supabase.auth.getUser()

                if (
                  !user &&
                  !request.nextUrl.pathname.startsWith('/login') &&
                  !request.nextUrl.pathname.startsWith('/auth') &&
                  !request.nextUrl.pathname.startsWith('/error')
                ) {
                  // no user, potentially respond by redirecting the user to the login page
                  const url = request.nextUrl.clone()
                  url.pathname = '/login'
                  return NextResponse.redirect(url)
                }

                // IMPORTANT: You *must* return the supabaseResponse object as it is.
                // If you're creating a new response object with NextResponse.next() make sure to:
                // 1. Pass the request in it, like so:
                //    const myNewResponse = NextResponse.next({ request })
                // 2. Copy over the cookies, like so:
                //    myNewResponse.cookies.setAll(supabaseResponse.cookies.getAll())
                // 3. Change the myNewResponse object to fit your needs, but avoid changing
                //    the cookies!
                // 4. Finally:
                //    return myNewResponse
                // If this is not done, you may be causing the browser and server to go out
                // of sync and terminate the user's session prematurely!

                return supabaseResponse
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={5}>
        <StepHikeCompact.Details title="Create a login page">
          Create a login page for your app. Use a Server Action to call the Supabase signup function.

          Since Supabase is being called from an Action, use the client defined in `@/utils/supabase/server.ts`.

          <Admonition type="note">
            Note that `cookies` is called before any calls to Supabase, which opts fetch calls out of Next.js's caching. This is important for authenticated data fetches, to ensure that users get access only to their own data.

            See the Next.js docs to learn more about [opting out of data caching](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#opting-out-of-data-caching).
          </Admonition>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="app/login/page.tsx" label="app/login/page.tsx">
              ```ts name=app/login/page.tsx
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

            <TabPanel id="app/login/actions.ts" label="app/login/actions.ts">
              ```ts name=app/login/actions.ts
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
                redirect('/')
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
                redirect('/')
              }
              ```
            </TabPanel>

            <TabPanel id="app/error/page.tsx" label="app/error/page.tsx">
              ```ts name=app/error/page.tsx
              'use client'

              export default function ErrorPage() {
                return <p>Sorry, something went wrong</p>
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={6}>
        <StepHikeCompact.Details title="Change the Auth confirmation path">
          If you have email confirmation turned on (the default), a new user will receive an email confirmation after signing up.

          Change the email template to support a server-side authentication flow.

          Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard. In the `Confirm signup` template, change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={7}>
        <StepHikeCompact.Details title="Create a route handler for Auth confirmation">
          Create a Route Handler for `auth/confirm`. When a user clicks their confirmation email link, exchange their secure code for an Auth token.

          Since this is a Router Handler, use the Supabase client from `@/utils/supabase/server.ts`.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="app/auth/confirm/route.ts" label="app/auth/confirm/route.ts">
              ```ts name=app/auth/confirm/route.ts
              import { type EmailOtpType } from '@supabase/supabase-js'
              import { type NextRequest } from 'next/server'

              import { createClient } from '@/utils/supabase/server'
              import { redirect } from 'next/navigation'

              export async function GET(request: NextRequest) {
                const { searchParams } = new URL(request.url)
                const token_hash = searchParams.get('token_hash')
                const type = searchParams.get('type') as EmailOtpType | null
                const next = searchParams.get('next') ?? '/'

                if (token_hash && type) {
                  const supabase = await createClient()

                  const { error } = await supabase.auth.verifyOtp({
                    type,
                    token_hash,
                  })
                  if (!error) {
                    // redirect user to specified redirect URL or root of app
                    redirect(next)
                  }
                }

                // redirect the user to an error page with some instructions
                redirect('/error')
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={8}>
        <StepHikeCompact.Details title="Access user info from Server Component">
          Server Components can read cookies, so you can get the Auth status and user info.

          Since you're calling Supabase from a Server Component, use the client created in `@/utils/supabase/server.ts`.

          Create a `private` page that users can only access if they're logged in. The page displays their email.

          <Admonition type="danger">
            Be careful when protecting pages. The server gets the user session from the cookies, which can be spoofed by anyone.

            Always use `supabase.auth.getUser()` to protect pages and user data.

            *Never* trust `supabase.auth.getSession()` inside Server Components. It isn't guaranteed to revalidate the Auth token.

            It's safe to trust `getUser()` because it sends a request to the Supabase Auth server every time to revalidate the Auth token.
          </Admonition>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="app/private/page.tsx" label="app/private/page.tsx">
              ```ts name=app/private/page.tsx
              import { redirect } from 'next/navigation'

              import { createClient } from '@/utils/supabase/server'

              export default async function PrivatePage() {
                const supabase = await createClient()

                const { data, error } = await supabase.auth.getUser()
                if (error || !data?.user) {
                  redirect('/login')
                }

                return <p>Hello {data.user.email}</p>
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>
    </StepHikeCompact>

    ## Congratulations

    You're done! To recap, you've successfully:

    *   Called Supabase from a Server Action.
    *   Called Supabase from a Server Component.
    *   Set up a Supabase client utility to call Supabase from a Client Component. You can use this if you need to call Supabase from a Client Component, for example to set up a realtime subscription.
    *   Set up middleware to automatically refresh the Supabase Auth session.

    You can now use any Supabase features from your client or server code!
  </TabPanel>

  <TabPanel id="pages" label="Pages Router">
    <StepHikeCompact>
      <StepHikeCompact.Step step={1}>
        <StepHikeCompact.Details title="Install Supabase packages">
          Install the `@supabase/supabase-js` package and the helper `@supabase/ssr` package.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```sh
          npm install @supabase/supabase-js @supabase/ssr
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={2}>
        <StepHikeCompact.Details title="Set up environment variables">
          Create a `.env.local` file in your project root directory.

          Fill in your `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`:

          <ProjectConfigVariables variable="url" />

          <ProjectConfigVariables variable="publishable" />

          <ProjectConfigVariables variable="anon" />
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <NamedCodeBlock name=".env.local">
            ```txt name=.env.local
            NEXT_PUBLIC_SUPABASE_URL=<your_supabase_project_url>
            NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=<sb_publishable_... or anon keyY>
            ```
          </NamedCodeBlock>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={3}>
        <StepHikeCompact.Details title="Write utility functions to create Supabase clients">
          To access Supabase from your Next.js app, you need 4 types of Supabase clients:

          1.  **`getServerSideProps` client** - To access Supabase from `getServerSideProps`.
          2.  **`getStaticProps` client** - To access Supabase from `getStaticProps`.
          3.  **Component client** - To access Supabase from within components.
          4.  **API route client** - To access Supabase from API route handlers.

          Create a `utils/supabase` folder with a file for each type of client. Then copy the utility functions for each client type.

          <Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6">
            <div className="border-b pb-3">
              <AccordionItem header={<span className="text-foreground">Why do I need so many types of clients?</span>} id="nextjs-clients">
                A Supabase client reads and sets cookies in order to access and update the user session. Depending on where the client is used, it needs to interact with cookies in a different way:

                *   **`getServerSideProps`** - Runs on the server. Reads cookies from the request, which is passed through from `GetServerSidePropsContext`.
                *   **`getStaticProps`** - Runs at build time, where there is no user, session, or cookies.
                *   **Component** - Runs on the client. Reads cookies from browser storage. Behind the scenes, `createBrowserClient` reuses the same client instance if called multiple times, so don't worry about deduplicating the client yourself.
                *   **API route** - Runs on the server. Reads cookies from the request, which is passed through from `NextApiRequest`.
              </AccordionItem>
            </div>

            <div className="border-b mt-3 pb-3">
              <AccordionItem header={<span className="text-foreground">What does the `cookies` object do?</span>} id="client-storage-cookies">
                The cookies object lets the Supabase client know how to access the cookies, so it can read and write the user session. To make `@supabase/ssr` framework-agnostic, the cookies methods aren't hard-coded. But you only need to set them up once. You can then reuse your utility functions whenever you need a Supabase client.

                The cookie is named `sb-<project_ref>-auth-token` by default.
              </AccordionItem>
            </div>
          </Accordion>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="utils/supabase/server-props.ts" label="utils/supabase/server-props.ts">
              ```ts name=utils/supabase/server-props.ts
              import { type GetServerSidePropsContext } from 'next'
              import { createServerClient, serializeCookieHeader } from '@supabase/ssr'

              export function createClient({ req, res }: GetServerSidePropsContext) {
                const supabase = createServerClient(
                  process.env.NEXT_PUBLIC_SUPABASE_URL!,
                  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
                  {
                    cookies: {
                      getAll() {
                        return Object.keys(req.cookies).map((name) => ({ name, value: req.cookies[name] || '' }))
                      },
                      setAll(cookiesToSet) {
                        res.setHeader(
                          'Set-Cookie',
                          cookiesToSet.map(({ name, value, options }) =>
                            serializeCookieHeader(name, value, options)
                          )
                        )
                      },
                    },
                  }
                )

                return supabase
              }
              ```
            </TabPanel>

            <TabPanel id="utils/supabase/static-props.ts" label="utils/supabase/static-props.ts">
              ```ts name=utils/supabase/static-props.ts
              import { createClient as createClientPrimitive } from '@supabase/supabase-js'

              export function createClient() {
                const supabase = createClientPrimitive(
                  process.env.NEXT_PUBLIC_SUPABASE_URL!,
                  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
                )

                return supabase
              }
              ```
            </TabPanel>

            <TabPanel id="utils/supabase/component.ts" label="utils/supabase/component.ts">
              ```ts name=utils/supabase/component.ts
              import { createBrowserClient } from '@supabase/ssr'

              export function createClient() {
                const supabase = createBrowserClient(
                  process.env.NEXT_PUBLIC_SUPABASE_URL!,
                  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!
                )

                return supabase
              }
              ```
            </TabPanel>

            <TabPanel id="utils/supabase/api.ts" label="utils/supabase/api.ts">
              ```ts name=utils/supabase/api.ts
              import { createServerClient, serializeCookieHeader } from '@supabase/ssr'
              import { type NextApiRequest, type NextApiResponse } from 'next'

              export default function createClient(req: NextApiRequest, res: NextApiResponse) {
                const supabase = createServerClient(
                  process.env.NEXT_PUBLIC_SUPABASE_URL!,
                  process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
                  {
                    cookies: {
                      getAll() {
                        return Object.keys(req.cookies).map((name) => ({ name, value: req.cookies[name] || '' }))
                      },
                      setAll(cookiesToSet) {
                        res.setHeader(
                          'Set-Cookie',
                          cookiesToSet.map(({ name, value, options }) =>
                            serializeCookieHeader(name, value, options)
                          )
                        )
                      },
                    },
                  }
                )

                return supabase
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={4}>
        <StepHikeCompact.Details title="Create a login page">
          Create a login page for your app.

          Since Supabase is being called from a component, use the client defined in `@/utils/supabase/component.ts`.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="pages/login.tsx" label="pages/login.tsx">
              ```ts name=pages/login.tsx
              import { useRouter } from 'next/router'
              import { useState } from 'react'

              import { createClient } from '@/utils/supabase/component'

              export default function LoginPage() {
                const router = useRouter()
                const supabase = createClient()

                const [email, setEmail] = useState('')
                const [password, setPassword] = useState('')

                async function logIn() {
                  const { error } = await supabase.auth.signInWithPassword({ email, password })
                  if (error) {
                    console.error(error)
                  }
                  router.push('/')
                }

                async function signUp() {
                  const { error } = await supabase.auth.signUp({ email, password })
                  if (error) {
                    console.error(error)
                  }
                  router.push('/')
                }

                return (
                  <main>
                    <form>
                      <label htmlFor="email">Email:</label>
                      <input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
                      <label htmlFor="password">Password:</label>
                      <input
                        id="password"
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                      />
                      <button type="button" onClick={logIn}>
                        Log in
                      </button>
                      <button type="button" onClick={signUp}>
                        Sign up
                      </button>
                    </form>
                  </main>
                )
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={5}>
        <StepHikeCompact.Details title="Change the Auth confirmation path">
          If you have email confirmation turned on (the default), a new user will receive an email confirmation after signing up.

          Change the email template to support a server-side authentication flow.

          Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard. In the `Confirm signup` template, change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/api/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
        </StepHikeCompact.Details>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={6}>
        <StepHikeCompact.Details title="Create a route handler for Auth confirmation">
          Create an API route for `api/auth/confirm`. When a user clicks their confirmation email link, exchange their secure code for an Auth token.

          Since this is an API route, use the Supabase client from `@/utils/supabase/api.ts`.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
            <TabPanel id="pages/api/auth/confirm.ts" label="pages/api/auth/confirm.ts">
              ```ts name=pages/api/auth/confirm.ts
              import { type EmailOtpType } from '@supabase/supabase-js'
              import type { NextApiRequest, NextApiResponse } from 'next'

              import createClient from '@/utils/supabase/api'

              function stringOrFirstString(item: string | string[] | undefined) {
                return Array.isArray(item) ? item[0] : item
              }

              export default async function handler(req: NextApiRequest, res: NextApiResponse) {
                if (req.method !== 'GET') {
                  res.status(405).appendHeader('Allow', 'GET').end()
                  return
                }

                const queryParams = req.query
                const token_hash = stringOrFirstString(queryParams.token_hash)
                const type = stringOrFirstString(queryParams.type)

                let next = '/error'

                if (token_hash && type) {
                  const supabase = createClient(req, res)
                  const { error } = await supabase.auth.verifyOtp({
                    type: type as EmailOtpType,
                    token_hash,
                  })
                  if (error) {
                    console.error(error)
                  } else {
                    next = stringOrFirstString(queryParams.next) || '/'
                  }
                }

                res.redirect(next)
              }
              ```
            </TabPanel>

            <TabPanel id="pages/error.tsx" label="pages/error.tsx">
              ```tsx name=pages/error.tsx
              export default function ErrorPage() {
                return <p>Sorry, something went wrong</p>
              }
              ```
            </TabPanel>
          </Tabs>
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={7}>
        <StepHikeCompact.Details title="Make an authenticated-only page using `getServerSideProps`">
          If you use dynamic server-side rendering, you can serve a page to authenticated users only by checking for the user data in `getServerSideProps`. Unauthenticated users will be redirected to the home page.

          Since you're calling Supabase from `getServerSideProps`, use the client from `@/utils/supabase/server-props.ts`.

          <Admonition type="danger">
            Be careful when protecting pages. The server gets the user session from the cookies, which can be spoofed by anyone.

            Always use `supabase.auth.getUser()` to protect pages and user data.

            *Never* trust `supabase.auth.getSession()` inside server code. It isn't guaranteed to revalidate the Auth token.

            It's safe to trust `getUser()` because it sends a request to the Supabase Auth server every time to revalidate the Auth token.
          </Admonition>
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```ts pages/private.tsx
          import type { User } from '@supabase/supabase-js'
          import type { GetServerSidePropsContext } from 'next'

          import { createClient } from '@/utils/supabase/server-props'

          export default function PrivatePage({ user }: { user: User }) {
            return <h1>Hello, {user.email || 'user'}!</h1>
          }

          export async function getServerSideProps(context: GetServerSidePropsContext) {
            const supabase = createClient(context)

            const { data, error } = await supabase.auth.getUser()

            if (error || !data) {
              return {
                redirect: {
                  destination: '/',
                  permanent: false,
                },
              }
            }

            return {
              props: {
                user: data.user,
              },
            }
          }
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>

      <StepHikeCompact.Step step={8}>
        <StepHikeCompact.Details title="Fetch static data using `getStaticProps`">
          You can also fetch static data at build time using Supabase. Note that there's no session or user at build time, so the data will be the same for everyone who sees the page.

          Add some colors data to your database by running the [Colors Quickstart](/dashboard/project/_/sql/quickstarts) in the dashboard.

          Then fetch the colors data using `getStaticProps` with the client from `@/utils/supabase/static-props.ts`.
        </StepHikeCompact.Details>

        <StepHikeCompact.Code>
          ```ts pages/public.tsx
          import { createClient } from '@/utils/supabase/static-props'

          export default function PublicPage({ data }: { data?: any[] }) {
            return <pre>{data && JSON.stringify(data, null, 2)}</pre>
          }

          export async function getStaticProps() {
            const supabase = createClient()

            const { data, error } = await supabase.from('colors').select()

            if (error || !data) {
              return { props: {} }
            }

            return { props: { data } }
          }
          ```
        </StepHikeCompact.Code>
      </StepHikeCompact.Step>
    </StepHikeCompact>

    ## Congratulations

    You're done! To recap, you've successfully:

    *   Called Supabase from a component
    *   Called Supabase from an API route
    *   Called Supabase from `getServerSideProps`
    *   Called Supabase from `getStaticProps`

    You can now use any Supabase features from your client or server code!
  </TabPanel>

  <TabPanel id="hybrid" label="Hybrid router strategies">
    You can use both the App and Pages Routers together.

    Follow the instructions for both the App and Pages Routers. Whenever you need to connect to Supabase, import the `createClient` utility that you need:

    | Router       | Code location                                     | Which `createClient` to use |
    | ------------ | ------------------------------------------------- | --------------------------- |
    | App Router   | Server Component, Server Action, or Route Handler | `server.ts`                 |
    |              | Client Component                                  | `client.ts`                 |
    | Pages Router | `getServerSideProps`                              | `server-props.ts`           |
    |              | `getStaticProps`                                  | `static-props.ts`           |
    |              | Component                                         | `component.ts`              |
    |              | API route                                         | `api.ts`                    |

    Remember to create the `middleware.ts` file for the App Router so the session refreshes for App Router pages.
  </TabPanel>
</Tabs>



# Setting up Server-Side Auth for SvelteKit



Set up Server-Side Auth to use cookie-based authentication with SvelteKit.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Install Supabase packages">
      Install the `@supabase/supabase-js` package and the helper `@supabase/ssr` package.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sh
      npm install @supabase/supabase-js @supabase/ssr
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Set up environment variables">
      Create a `.env.local` file in your project root directory.

      Fill in your `PUBLIC_SUPABASE_URL` and `PUBLIC_SUPABASE_PUBLISHABLE_KEY`:

      <ProjectConfigVariables variable="url" />

      <ProjectConfigVariables variable="publishable" />

      <ProjectConfigVariables variable="anon" />
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id=".env.local" label=".env.local">
          ```txt name=.env.local
          PUBLIC_SUPABASE_URL=<your_supabase_project_url>
          PUBLIC_SUPABASE_PUBLISHABLE_KEY=<sb_publishable_... or anon keyY>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Set up server-side hooks">
      Set up server-side hooks in `src/hooks.server.ts`. The hooks:

      *   Create a request-specific Supabase client, using the user credentials from the request cookie. This client is used for server-only code.
      *   Check user authentication.
      *   Guard protected pages.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/hooks.server.ts" label="src/hooks.server.ts">
          ```ts name=src/hooks.server.ts
          import { createServerClient } from '@supabase/ssr'
          import { type Handle, redirect } from '@sveltejs/kit'
          import { sequence } from '@sveltejs/kit/hooks'

          import { PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY } from '$env/static/public'

          const supabase: Handle = async ({ event, resolve }) => {
            /**
             * Creates a Supabase client specific to this server request.
             *
             * The Supabase client gets the Auth token from the request cookies.
             */
            event.locals.supabase = createServerClient(PUBLIC_SUPABASE_URL, PUBLIC_SUPABASE_PUBLISHABLE_KEY, {
              cookies: {
                getAll: () => event.cookies.getAll(),
                /**
                 * SvelteKit's cookies API requires `path` to be explicitly set in
                 * the cookie options. Setting `path` to `/` replicates previous/
                 * standard behavior.
                 */
                setAll: (cookiesToSet) => {
                  cookiesToSet.forEach(({ name, value, options }) => {
                    event.cookies.set(name, value, { ...options, path: '/' })
                  })
                },
              },
            })

            /**
             * Unlike `supabase.auth.getSession()`, which returns the session _without_
             * validating the JWT, this function also calls `getUser()` to validate the
             * JWT before returning the session.
             */
            event.locals.safeGetSession = async () => {
              const {
                data: { session },
              } = await event.locals.supabase.auth.getSession()
              if (!session) {
                return { session: null, user: null }
              }

              const {
                data: { user },
                error,
              } = await event.locals.supabase.auth.getUser()
              if (error) {
                // JWT validation has failed
                return { session: null, user: null }
              }

              return { session, user }
            }

            return resolve(event, {
              filterSerializedResponseHeaders(name) {
                /**
                 * Supabase libraries use the `content-range` and `x-supabase-api-version`
                 * headers, so we need to tell SvelteKit to pass it through.
                 */
                return name === 'content-range' || name === 'x-supabase-api-version'
              },
            })
          }

          const authGuard: Handle = async ({ event, resolve }) => {
            const { session, user } = await event.locals.safeGetSession()
            event.locals.session = session
            event.locals.user = user

            if (!event.locals.session && event.url.pathname.startsWith('/private')) {
              redirect(303, '/auth')
            }

            if (event.locals.session && event.url.pathname === '/auth') {
              redirect(303, '/private')
            }

            return resolve(event)
          }

          export const handle: Handle = sequence(supabase, authGuard)
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Create TypeScript definitions">
      To prevent TypeScript errors, add type definitions for the new `event.locals` properties.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/app.d.ts" label="src/app.d.ts">
          ```ts name=src/app.d.ts
          import type { Session, SupabaseClient, User } from '@supabase/supabase-js'
          import type { Database } from './database.types.ts' // import generated types

          declare global {
            namespace App {
              // interface Error {}
              interface Locals {
                supabase: SupabaseClient<Database>
                safeGetSession: () => Promise<{ session: Session | null; user: User | null }>
                session: Session | null
                user: User | null
              }
              interface PageData {
                session: Session | null
              }
              // interface PageState {}
              // interface Platform {}
            }
          }

          export {}
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Create a Supabase client in your root layout">
      Create a Supabase client in your root `+layout.ts`. This client can be used to access Supabase from the client or the server. In order to get access to the Auth token on the server, use a `+layout.server.ts` file to pass in the session from `event.locals`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/+layout.ts" label="src/routes/+layout.ts">
          ```ts name=src/routes/+layout.ts
          import { createBrowserClient, createServerClient, isBrowser } from '@supabase/ssr'
          import { PUBLIC_SUPABASE_PUBLISHABLE_KEY, PUBLIC_SUPABASE_URL } from '$env/static/public'
          import type { LayoutLoad } from './$types'

          export const load: LayoutLoad = async ({ data, depends, fetch }) => {
            /**
             * Declare a dependency so the layout can be invalidated, for example, on
             * session refresh.
             */
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

            const {
              data: { user },
            } = await supabase.auth.getUser()

            return { session, supabase, user }
          }
          ```
        </TabPanel>

        <TabPanel id="src/routes/+layout.server.ts" label="src/routes/+layout.server.ts">
          ```ts name=src/routes/+layout.server.ts
          import type { LayoutServerLoad } from './$types'

          export const load: LayoutServerLoad = async ({ locals: { safeGetSession }, cookies }) => {
            const { session } = await safeGetSession()
            return {
              session,
              cookies: cookies.getAll(),
            }
          }
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Listen to Auth events">
      Set up a listener for Auth events on the client, to handle session refreshes and signouts.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/+layout.svelte" label="src/routes/+layout.svelte">
          ```svelte name=src/routes/+layout.svelte
          <script>
            import { invalidate } from '$app/navigation'
            import { onMount } from 'svelte'

            let { data, children } = $props()
            let { session, supabase } = $derived(data)

            onMount(() => {
              const { data } = supabase.auth.onAuthStateChange((_, newSession) => {
                if (newSession?.expires_at !== session?.expires_at) {
                  invalidate('supabase:auth')
                }
              })

              return () => data.subscription.unsubscribe()
            })
          </script>

          {@render children()}
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Create your first page">
      Create your first page. This example page calls Supabase from the server to get a list of colors from the database.

      This is an example of a public page that uses publicly readable data.

      To populate your database, run the [colors quickstart](/dashboard/project/_/sql/quickstarts) from your dashboard.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/+page.server.ts" label="src/routes/+page.server.ts">
          ```ts name=src/routes/+page.server.ts
          import type { PageServerLoad } from './$types'

          export const load: PageServerLoad = async ({ locals: { supabase } }) => {
            const { data: colors } = await supabase.from('colors').select('name').limit(5).order('name')
            return { colors: colors ?? [] }
          }
          ```
        </TabPanel>

        <TabPanel id="src/routes/+page.svelte" label="src/routes/+page.svelte">
          ```svelte name=src/routes/+page.svelte
          <script>
            let { data } = $props()
            let { colors } = $derived(data)
          </script>

          <h1>Welcome to Supabase!</h1>
          <ul>
            {#each colors as color}
              <li>{color.name}</li>
            {/each}
          </ul>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={8}>
    <StepHikeCompact.Details title="Change the Auth confirmation path">
      If you have email confirmation turned on (the default), a new user will receive an email confirmation after signing up.

      Change the email template to support a server-side authentication flow.

      Go to the [Auth templates](/dashboard/project/_/auth/templates) page in your dashboard. In the `Confirm signup` template, change `{{ .ConfirmationURL }}` to `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email`.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={9}>
    <StepHikeCompact.Details title="Create a login page">
      Next, create a login page to let users sign up and log in.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/auth/+page.server.ts" label="src/routes/auth/+page.server.ts">
          ```ts name=src/routes/auth/+page.server.ts
          import { redirect } from '@sveltejs/kit'

          import type { Actions } from './$types'

          export const actions: Actions = {
            signup: async ({ request, locals: { supabase } }) => {
              const formData = await request.formData()
              const email = formData.get('email') as string
              const password = formData.get('password') as string

              const { error } = await supabase.auth.signUp({ email, password })
              if (error) {
                console.error(error)
                redirect(303, '/auth/error')
              } else {
                redirect(303, '/')
              }
            },
            login: async ({ request, locals: { supabase } }) => {
              const formData = await request.formData()
              const email = formData.get('email') as string
              const password = formData.get('password') as string

              const { error } = await supabase.auth.signInWithPassword({ email, password })
              if (error) {
                console.error(error)
                redirect(303, '/auth/error')
              } else {
                redirect(303, '/private')
              }
            },
          }
          ```
        </TabPanel>

        <TabPanel id="src/routes/auth/+page.svelte" label="src/routes/auth/+page.svelte">
          ```svelte name=src/routes/auth/+page.svelte
          <form method="POST" action="?/login">
            <label>
              Email
              <input name="email" type="email" />
            </label>
            <label>
              Password
              <input name="password" type="password" />
            </label>
            <button>Login</button>
            <button formaction="?/signup">Sign up</button>
          </form>
          ```
        </TabPanel>

        <TabPanel id="src/routes/auth/+layout.svelte" label="src/routes/auth/+layout.svelte">
          ```svelte name=src/routes/auth/+layout.svelte
          <script>
            let { children } = $props()
          </script>

          <header>
            <nav>
              <a href="/">Home</a>
            </nav>
          </header>

          {@render children()}
          ```
        </TabPanel>

        <TabPanel id="src/routes/auth/error/+page.svelte" label="src/routes/auth/error/+page.svelte">
          ```svelte name=src/routes/auth/error/+page.svelte
          <p>Login error</p>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={10}>
    <StepHikeCompact.Details title="Create the signup confirmation route">
      Finish the signup flow by creating the API route to handle email verification.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/auth/confirm/+server.ts" label="src/routes/auth/confirm/+server.ts">
          ```ts name=src/routes/auth/confirm/+server.ts
          import type { EmailOtpType } from '@supabase/supabase-js'
          import { redirect } from '@sveltejs/kit'

          import type { RequestHandler } from './$types'

          export const GET: RequestHandler = async ({ url, locals: { supabase } }) => {
            const token_hash = url.searchParams.get('token_hash')
            const type = url.searchParams.get('type') as EmailOtpType | null
            const next = url.searchParams.get('next') ?? '/'

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
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={11}>
    <StepHikeCompact.Details title="Create private routes">
      Create private routes that can only be accessed by authenticated users. The routes in the `private` directory are protected by the route guard in `hooks.server.ts`.

      To ensure that `hooks.server.ts` runs for every nested path, put a `+layout.server.ts` file in the `private` directory. This file can be empty, but must exist to protect routes that don't have their own `+layout|page.server.ts`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs listClassNames="flex-nowrap overflow-x-auto -mb-6">
        <TabPanel id="src/routes/private/+layout.server.ts" label="src/routes/private/+layout.server.ts">
          ```ts name=src/routes/private/+layout.server.ts
          /**
           * This file is necessary to ensure protection of all routes in the `private`
           * directory. It makes the routes in this directory _dynamic_ routes, which
           * send a server request, and thus trigger `hooks.server.ts`.
           **/
          ```
        </TabPanel>

        <TabPanel id="src/routes/private/+layout.svelte" label="src/routes/private/+layout.svelte">
          ```svelte name=src/routes/private/+layout.svelte
          <script>
            let { data, children } = $props()
            let { supabase } = $derived(data)

            const logout = async () => {
              const { error } = await supabase.auth.signOut()
              if (error) {
                console.error(error)
              }
            }
          </script>

          <header>
            <nav>
              <a href="/">Home</a>
            </nav>
            <button onclick={logout}>Logout</button>
          </header>
          <main>
            {@render children()}
          </main>
          ```
        </TabPanel>

        <TabPanel id="SQL" label="SQL">
          ```sql name=SQL
          -- Run this SQL against your database to create a `notes` table.

          create table notes (
            id bigint primary key generated always as identity,
            created_at timestamp with time zone not null default now(),
            user_id uuid references auth.users on delete cascade not null default auth.uid(),
            note text not null
          );

          alter table notes enable row level security;

          revoke all on table notes from authenticated;
          revoke all on table notes from anon;

          grant all (note) on table notes to authenticated;
          grant select (id) on table notes to authenticated;
          grant delete on table notes to authenticated;

          create policy "Users can access and modify their own notes"
          on notes
          for all
          to authenticated
          using ((select auth.uid()) = user_id);
          ```
        </TabPanel>

        <TabPanel id="src/routes/private/+page.server.ts" label="src/routes/private/+page.server.ts">
          ```svelte name=src/routes/private/+page.server.ts
          import type { PageServerLoad } from './$types'

          export const load: PageServerLoad = async ({ depends, locals: { supabase } }) => {
            depends('supabase:db:notes')
            const { data: notes } = await supabase.from('notes').select('id,note').order('id')
            return { notes: notes ?? [] }
          }
          ```
        </TabPanel>

        <TabPanel id="src/routes/private/+page.svelte" label="src/routes/private/+page.svelte">
          ```svelte name=src/routes/private/+page.svelte
          <script lang="ts">
            import { invalidate } from '$app/navigation'
            import type { EventHandler } from 'svelte/elements'

            import type { PageData } from './$types'

            let { data } = $props()
            let { notes, supabase, user } = $derived(data)

            const handleSubmit: EventHandler<SubmitEvent, HTMLFormElement> = async (evt) => {
              evt.preventDefault()
              if (!evt.target) return

              const form = evt.target as HTMLFormElement

              const note = (new FormData(form).get('note') ?? '') as string
              if (!note) return

              const { error } = await supabase.from('notes').insert({ note })
              if (error) console.error(error)

              invalidate('supabase:db:notes')
              form.reset()
            }
          </script>

          <h1>Private page for user: {user?.email}</h1>
          <h2>Notes</h2>
          <ul>
            {#each notes as note}
              <li>{note.note}</li>
            {/each}
          </ul>
          <form onsubmit={handleSubmit}>
            <label>
              Add a note
              <input name="note" type="text" />
            </label>
          </form>
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



---
**Navigation:** [← Previous](./33-login-with-notion.md) | [Index](./index.md) | [Next →](./35-use-supabase-auth-with-nextjs.md)
