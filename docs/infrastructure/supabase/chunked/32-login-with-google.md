**Navigation:** [← Previous](./31-login-with-bitbucket.md) | [Index](./index.md) | [Next →](./33-login-with-notion.md)

# Login with Google



Supabase Auth supports [Sign in with Google for the web](https://developers.google.com/identity/gsi/web/guides/overview), native applications ([Android](https://developer.android.com/identity/sign-in/credential-manager-siwg), [macOS and iOS](https://developers.google.com/identity/sign-in/ios/start-integrating)), and [Chrome extensions](https://cloud.google.com/identity-platform/docs/web/chrome-extension).

You can use Sign in with Google in two ways:

*   [By writing application code](#application-code) for the web, native applications or Chrome extensions
*   [By using Google's pre-built solutions](#google-pre-built) such as [personalized sign-in buttons](https://developers.google.com/identity/gsi/web/guides/personalized-button), [One Tap](https://developers.google.com/identity/gsi/web/guides/features) or [automatic sign-in](https://developers.google.com/identity/gsi/web/guides/automatic-sign-in-sign-out)



## Prerequisites

You need to do some setup to get started with Sign in with Google:

*   Prepare a Google Cloud project. Go to the [Google Cloud Platform](https://console.cloud.google.com/home/dashboard) and create a new project if necessary.
*   Use the [Google Auth Platform console](https://console.cloud.google.com/auth/overview) to register and set up your application's:
    *   [**Audience**](https://console.cloud.google.com/auth/audience) by configuring which Google users are allowed to sign in to your application.
    *   [**Data Access (Scopes)**](https://console.cloud.google.com/auth/scopes) define what your application can do with your user's Google data and APIs, such as access profile information or more.
    *   [**Branding**](https://console.cloud.google.com/auth/branding) and [**Verification**](https://console.cloud.google.com/auth/verification) show a logo and name instead of the Supabase project ID in the consent screen, improving user retention. Brand verification may take a few business days.


### Setup required scopes

Supabase Auth needs a few scopes granting access to profile data of your end users, which you have to configure in the [**Data Access (Scopes)**](https://console.cloud.google.com/auth/scopes) screen:

*   `openid` (add manually)
*   `.../auth/userinfo.email` (added by default)
*   `...auth/userinfo.profile` (added by default)

If you add more scopes, especially those on the sensitive or restricted list your application might be subject to verification which may take a long time.


### Setup consent screen branding

<Admonition type="note">
  It's strongly recommended you set up a custom domain and optionally verify your brand information with Google, as this makes phishing attempts easier to spot by your users.
</Admonition>

Google's consent screen is shown to users when they sign in. Optionally configure one of the following to improve the appearance of the screen, increasing the perception of trust by your users:

1.  Verify your application's brand (logo and name) by configuring it in the [Branding](https://console.cloud.google.com/auth/branding) section of the Google Auth Platform console. Brand verification is not automatic and may take a few business days.
2.  Set up a [custom domain for your project](/docs/guides/platform/custom-domains) to present the user with a clear relationship to the website they clicked Sign in with Google on.
    *   A good approach is to use `auth.example.com` or `api.example.com`, if your application is hosted on `example.com`.
    *   If you don't set this up, users will see `<project-id>.supabase.co` which does not inspire trust and can make your application more susceptible to successful phishing attempts.



## Project setup

To support Sign In with Google, you need to configure the Google provider for your Supabase project.

<Tabs scrollable size="large" type="underlined" defaultActiveId="web" queryGroup="platform">
  <TabPanel id="web" label="Web">
    Regardless of whether you use application code or Google's pre-built solutions to implement the sign in flow, you need to configure your project by obtaining a Client ID and Client Secret in the [Clients](https://console.cloud.google.com/auth/clients) section of the Google Auth Platform console:

    1.  [Create a new OAuth client ID](https://console.cloud.google.com/auth/clients/create) and choose **Web application** for the application type.
    2.  Under **Authorized JavaScript origins** add your application's URL. These should also be configured as the [Site URL or redirect configuration in your project](/docs/guides/auth/redirect-urls).
        *   If your app is hosted on `https://example.com/app` add `https://example.com`.
        *   Add `http://localhost:<port>` while developing locally. Remember to remove this when your application [goes into production](/docs/guides/deployment/going-into-prod).
    3.  Under **Authorized redirect URIs** add your Supabase project's callback URL.
        *   Access it from the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google).
        *   For local development, use `http://localhost:3000/auth/v1/callback`.
    4.  Click `Create` and make sure you save the Client ID and Client Secret.
        *   Add these values to the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google).
  </TabPanel>

  <TabPanel id="react-native" label="Expo React Native">
    1.  [Create a new OAuth client ID](https://console.cloud.google.com/auth/clients/create) and choose **Android** or **iOS** depending on the OS you're building the app for.
        *   For Android, use the instructions on screen to provide the SHA-1 certificate fingerprint used to sign your Android app.
        *   You will have a different set of SHA-1 certificate fingerprints for testing locally and going to production. Make sure to add both to the Google Cloud Console, and add all of the Client IDs to the Supabase dashboard.
        *   For iOS, use the instructions on screen to provide the app Bundle ID, and App Store ID and Team ID if the app is already published on the Apple App Store.
    2.  Register the Client ID in the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google).
  </TabPanel>

  <TabPanel id="flutter-mobile" label="Flutter (iOS and Android)">
    1.  [Create a new OAuth client ID](https://console.cloud.google.com/auth/clients/create) and choose **Android** or **iOS** depending on the OS you're building the app for.
        *   For Android, use the instructions on screen to provide the SHA-1 certificate fingerprint used to sign your Android app.
        *   You will have a different set of SHA-1 certificate fingerprints for testing locally and going to production. Make sure to add both to the Google Cloud Console, and add all of the Client IDs to the Supabase dashboard.
        *   For iOS, use the instructions on screen to provide the app Bundle ID, and App Store ID and Team ID if the app is already published on the Apple App Store.
    2.  Register the Client ID in the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google).
        *   For iOS enable the `Skip nonce check` option.

    For iOS add a `CFBundleURLTypes` key in the `<project>/ios/Runner/Info.plist` file:

    ```xml
    <!-- Put me in the [my_project]/ios/Runner/Info.plist file -->
    <!-- Google Sign-in Section -->
    <key>CFBundleURLTypes</key>
    <array>
      <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
          <!-- TODO Replace this value: -->
          <!-- Copied from GoogleService-Info.plist key REVERSED_CLIENT_ID -->
          <string>com.googleusercontent.apps.861823949799-vc35cprkp249096uujjn0vvnmcvjppkn</string>
        </array>
      </dict>
    </array>
    <!-- End of the Google Sign-in Section -->
    ```
  </TabPanel>

  <TabPanel id="flutter-other" label="Flutter (web, macOS, Windows, Linux)">
    Follow the same configuration guide as if your app was a Web application when building a desktop Flutter application.
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Google sign-in with Supabase is done through the [`GoogleSignIn-iOS`](https://github.com/google/GoogleSignIn-iOS) package.

    When the user provides consent, Google issues an identity token (commonly abbreviated as ID token) that is then sent to your project's Supabase Auth server. When valid, a new user session is started by issuing an access and refresh token from Supabase Auth.

    Follow the code sample below to implement native Google sign-in with Supabase in your iOS app.

    ```swift
    import GoogleSignIn

    class GoogleSignInViewController: UIViewController {
      ...

      func googleSignIn() async throws {
        let result = try await GIDSignIn.sharedInstance.signIn(withPresenting: self)

        guard let idToken = result.user.idToken?.tokenString else {
          print("No idToken found.")
          return
        }

        let accessToken = result.user.accessToken.tokenString

        try await supabase.auth.signInWithIdToken(
          credentials: OpenIDConnectCredentials(
            provider: .google,
            idToken: idToken,
            accessToken: accessToken
          )
        )
      }
      ...

    }
    ```

    ### Configuration \[#ios-configuration]

    1.  Follow the integration instructions on the [get started with Google Sign-In](https://developers.google.com/identity/sign-in/ios/start-integrating) for the iOS guide.
    2.  Configure the [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent). This information is shown to the user when giving consent to your app. In particular, make sure you have set up links to your app's privacy policy and terms of service.
    3.  Add web client ID and iOS client ID from step 1 in the [Google provider on the Supabase Dashboard](/dashboard/project/_/auth/providers), under *Client IDs*, separated by a comma. Enable the `Skip nonce check` option.
  </TabPanel>

  <TabPanel id="android" label="Android (Kotlin)">
    1.  [Create a new OAuth client ID](https://console.cloud.google.com/auth/clients/create) and choose **Android** or **iOS** if also building an iOS app with Kotlin Multiplatform.
        *   For Android, use the instructions on screen to provide the SHA-1 certificate fingerprint used to sign your Android app.
        *   You will have a different set of SHA-1 certificate fingerprints for testing locally and going to production. Make sure to add both to the Google Cloud Console, and add all of the Client IDs to the Supabase dashboard.
        *   For iOS (with Kotlin Multiplatform), use the instructions on screen to provide the app Bundle ID, and App Store ID and Team ID if the app is already published on the Apple App Store.
    2.  Register the Client ID in the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google).
  </TabPanel>

  <TabPanel id="chrome-extensions" label="Chrome Extensions">
    1.  [Create a new OAuth client ID](https://console.cloud.google.com/auth/clients/create) and choose **Chrome Extension** for application type.
        *   Enter your extension's Item ID and optionally verify app ownership.
    2.  Register the Client ID in the [Google provider page on the Dashboard](/dashboard/project/_/auth/providers?provider=Google) under *Client IDs*.
  </TabPanel>
</Tabs>


### Local development

To use the Google provider in local development:

1.  Add a new environment variable:
    ```env
    SUPABASE_AUTH_EXTERNAL_GOOGLE_CLIENT_SECRET="<client-secret>"
    ```
2.  Configure the provider:
    ```toml
    [auth.external.google]
    enabled = true
    client_id = "<client-id>"
    secret = "env(SUPABASE_AUTH_EXTERNAL_GOOGLE_CLIENT_SECRET)"
    skip_nonce_check = false
    ```

If you have multiple client IDs, such as one for Web, iOS and Android, concatenate all of the client IDs with a comma but make sure the web's client ID is first in the list.


### Using the management API

Use the [PATCH `/v1/projects/{ref}/config/auth` Management API endpoint](/docs/reference/api/v1-update-auth-service-config) to configure the project's Auth settings programmatically. For configuring the Google provider send these options:

```json
{
  "external_google_enabled": true,
  "external_google_client_id": "your-google-client-id",
  "external_google_secret": "your-google-client-secret"
}
```



## Signing users in

<Tabs scrollable size="large" type="underlined" defaultActiveId="web" queryGroup="platform">
  <TabPanel id="web" label="Web">
    ### Application code

    To use your own application code for the signin button, call the `signInWithOAuth` method (or the equivalent for your language).

    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    supabase.auth.signInWithOAuth({
      provider: 'google',
    })
    ```

    For an implicit flow, that's all you need to do. The user will be taken to Google's consent screen, and finally redirected to your app with an access and refresh token pair representing their session.

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

    After a successful code exchange, the user's session will be saved to cookies.

    ### Saving Google tokens

    The tokens saved by your application are the Supabase Auth tokens. Your app might additionally need the Google OAuth 2.0 tokens to access Google services on the user's behalf.

    On initial login, you can extract the `provider_token` from the session and store it in a secure storage medium. The session is available in the returned data from `signInWithOAuth` (implicit flow) and `exchangeCodeForSession` (PKCE flow).

    Google does not send out a refresh token by default, so you will need to pass parameters like these to `signInWithOAuth()` in order to extract the `provider_refresh_token`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: {
        queryParams: {
          access_type: 'offline',
          prompt: 'consent',
        },
      },
    })
    ```

    ### Google pre-built \[#google-pre-built]

    Most web apps and websites can utilize Google's [personalized sign-in buttons](https://developers.google.com/identity/gsi/web/guides/personalized-button), [One Tap](https://developers.google.com/identity/gsi/web/guides/features) or [automatic sign-in](https://developers.google.com/identity/gsi/web/guides/automatic-sign-in-sign-out) for the best user experience.

    1.  Load the Google client library in your app by including the third-party script:

        ```html
        <script src="https://accounts.google.com/gsi/client" async></script>
        ```

    2.  Use the [HTML Code Generator](https://developers.google.com/identity/gsi/web/tools/configurator) to customize the look, feel, features and behavior of the Sign in with Google button.

    3.  Pick the *Swap to JavaScript callback* option, and input the name of your callback function. This function will receive a [`CredentialResponse`](https://developers.google.com/identity/gsi/web/reference/js-reference#CredentialResponse) when sign in completes.

        To make your app compatible with Chrome's third-party-cookie phase-out, make sure to set `data-use_fedcm_for_prompt` to `true`.

        Your final HTML code might look something like this:

        ```html
        <div
          id="g_id_onload"
          data-client_id="<client ID>"
          data-context="signin"
          data-ux_mode="popup"
          data-callback="handleSignInWithGoogle"
          data-nonce=""
          data-auto_select="true"
          data-itp_support="true"
          data-use_fedcm_for_prompt="true"
        ></div>

        <div
          class="g_id_signin"
          data-type="standard"
          data-shape="pill"
          data-theme="outline"
          data-text="signin_with"
          data-size="large"
          data-logo_alignment="left"
        ></div>
        ```

    4.  Create a `handleSignInWithGoogle` function that takes the `CredentialResponse` and passes the included token to Supabase. The function needs to be available in the global scope for Google's code to find it.

        ```ts
        async function handleSignInWithGoogle(response) {
          const { data, error } = await supabase.auth.signInWithIdToken({
            provider: 'google',
            token: response.credential,
          })
        }
        ```

    5.  *(Optional)* Configure a nonce. The use of a nonce is recommended for extra security, but optional. The nonce should be generated randomly each time, and it must be provided in both the `data-nonce` attribute of the HTML code and the options of the callback function.

        ```ts
        async function handleSignInWithGoogle(response) {
          const { data, error } = await supabase.auth.signInWithIdToken({
            provider: 'google',
            token: response.credential,
            nonce: '<NONCE>',
          })
        }
        ```

        Note that the nonce should be the same in both places, but because Supabase Auth expects the provider to hash it (SHA-256, hexadecimal representation), you need to provide a hashed version to Google and a non-hashed version to `signInWithIdToken`.

        You can get both versions by using the in-built `crypto` library:

        ```js
        // Adapted from https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest#converting_a_digest_to_a_hex_string

        const nonce = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32))))
        const encoder = new TextEncoder()
        const encodedNonce = encoder.encode(nonce)
        crypto.subtle.digest('SHA-256', encodedNonce).then((hashBuffer) => {
          const hashArray = Array.from(new Uint8Array(hashBuffer))
          const hashedNonce = hashArray.map((b) => b.toString(16).padStart(2, '0')).join('')
        })

        // Use 'hashedNonce' when making the authentication request to Google
        // Use 'nonce' when invoking the supabase.auth.signInWithIdToken() method
        ```

    ### One-tap with Next.js

    If you're integrating Google One-Tap with your Next.js application, you can refer to the example below to get started:

    ```tsx
    'use client'

    import Script from 'next/script'
    import { createClient } from '@/utils/supabase/client'
    import type { accounts, CredentialResponse } from 'google-one-tap'
    import { useRouter } from 'next/navigation'

    declare const google: { accounts: accounts }

    // generate nonce to use for google id token sign-in
    const generateNonce = async (): Promise<string[]> => {
      const nonce = btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32))))
      const encoder = new TextEncoder()
      const encodedNonce = encoder.encode(nonce)
      const hashBuffer = await crypto.subtle.digest('SHA-256', encodedNonce)
      const hashArray = Array.from(new Uint8Array(hashBuffer))
      const hashedNonce = hashArray.map((b) => b.toString(16).padStart(2, '0')).join('')

      return [nonce, hashedNonce]
    }

    const OneTapComponent = () => {
      const supabase = createClient()
      const router = useRouter()

      const initializeGoogleOneTap = async () => {
        console.log('Initializing Google One Tap')
        const [nonce, hashedNonce] = await generateNonce()
        console.log('Nonce: ', nonce, hashedNonce)

        // check if there's already an existing session before initializing the one-tap UI
        const { data, error } = await supabase.auth.getSession()
        if (error) {
          console.error('Error getting session', error)
        }
        if (data.session) {
          router.push('/')
          return
        }

        /* global google */
        google.accounts.id.initialize({
          client_id: process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID,
          callback: async (response: CredentialResponse) => {
            try {
              // send id token returned in response.credential to supabase
              const { data, error } = await supabase.auth.signInWithIdToken({
                provider: 'google',
                token: response.credential,
                nonce,
              })

              if (error) throw error
              console.log('Session data: ', data)
              console.log('Successfully logged in with Google One Tap')

              // redirect to protected page
              router.push('/')
            } catch (error) {
              console.error('Error logging in with Google One Tap', error)
            }
          },
          nonce: hashedNonce,
          // with chrome's removal of third-party cookies, we need to use FedCM instead (https://developers.google.com/identity/gsi/web/guides/fedcm-migration)
          use_fedcm_for_prompt: true,
        })
        google.accounts.id.prompt() // Display the One Tap UI
      }

      return <Script onReady={initializeGoogleOneTap} src="https://accounts.google.com/gsi/client" />
    }

    export default OneTapComponent
    ```
  </TabPanel>

  <TabPanel id="react-native" label="Expo React Native">
    Unlike the OAuth flow which requires the use of a web browser, the native Sign in with Google flow on Android uses the [Credential Manager library](https://developer.android.com/identity/sign-in/credential-manager-siwg) to prompt the user for consent.

    When the user provides consent, Google issues an identity token (commonly abbreviated as ID token) that you then send to your project's Supabase Auth server. When valid, a new user session is started by issuing an access and refresh token from Supabase Auth.

    By default, Supabase Auth implements nonce validation during the authentication flow. This can be disabled in production under `Authentication > Providers > Google > Skip Nonce Check` in the Dashboard, or when developing locally by setting `auth.external.<provider>.skip_nonce_check`. Only disable this if your client libraries cannot properly handle nonce verification.

    When working with Expo, you can use the [`@react-native-google-signin/google-signin` library](https://github.com/react-native-google-signin/google-signin#expo-installation) to obtain an ID token that you can pass to supabase-js [`signInWithIdToken` method](/docs/reference/javascript/auth-signinwithidtoken).

    Follow the [Expo installation docs](https://react-native-google-signin.github.io/docs/setting-up/expo) for installation and configuration instructions. See the [supabase-js reference](/docs/reference/javascript/initializing?example=react-native-options-async-storage) for instructions on initializing the supabase-js client in React Native.

    ```tsx ./components/Auth.native.tsx
    import {
      GoogleSignin,
      GoogleSigninButton,
      statusCodes,
    } from '@react-native-google-signin/google-signin'
    import { supabase } from '../utils/supabase'

    export default function () {
      GoogleSignin.configure({
        webClientId: 'YOUR CLIENT ID FROM GOOGLE CONSOLE',
      })

      return (
        <GoogleSigninButton
          size={GoogleSigninButton.Size.Wide}
          color={GoogleSigninButton.Color.Dark}
          onPress={async () => {
            try {
              await GoogleSignin.hasPlayServices()
              const response = await GoogleSignin.signIn()
              if (isSuccessResponse(response)) {
                const { data, error } = await supabase.auth.signInWithIdToken({
                  provider: 'google',
                  token: response.data.idToken,
                })
                console.log(error, data)
              }
            } catch (error: any) {
              if (error.code === statusCodes.IN_PROGRESS) {
                // operation (e.g. sign in) is in progress already
              } else if (error.code === statusCodes.PLAY_SERVICES_NOT_AVAILABLE) {
                // play services not available or outdated
              } else {
                // some other error happened
              }
            }
          }}
        />
      )
    }
    ```
  </TabPanel>

  <TabPanel id="flutter-mobile" label="Flutter (iOS and Android)">
    Google sign-in with Supabase is done through the [google\_sign\_in](https://pub.dev/packages/google_sign_in) package for iOS and Android.

    When the user provides consent, Google issues an identity token (commonly abbreviated as ID token) that is then sent to your project's Supabase Auth server. When valid, a new user session is started by issuing an access and refresh token from Supabase Auth.

    Follow the code sample below to implement native Google sign-in with Supabase in your Flutter iOS and Android app.

    ```dart
    import 'package:google_sign_in/google_sign_in.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    ...
    Future<void> _nativeGoogleSignIn() async {
      /// TODO: update the Web client ID with your own.
      ///
      /// Web Client ID that you registered with Google Cloud.
      const webClientId = 'my-web.apps.googleusercontent.com';

      /// TODO: update the iOS client ID with your own.
      ///
      /// iOS Client ID that you registered with Google Cloud.
      const iosClientId = 'my-ios.apps.googleusercontent.com';

      final scopes = ['email', 'profile'];
      final googleSignIn = GoogleSignIn.instance;

      await googleSignIn.initialize(
        serverClientId: webClientId,
        clientId: iosClientId,
      );

      final googleUser = await googleSignIn.attemptLightweightAuthentication();
      // or await googleSignIn.authenticate(); which will return a GoogleSignInAccount or throw an exception

      if (googleUser == null) {
        throw AuthException('Failed to sign in with Google.');
      }

      /// Authorization is required to obtain the access token with the appropriate scopes for Supabase authentication,
      /// while also granting permission to access user information.
      final authorization =
          await googleUser.authorizationClient.authorizationForScopes(scopes) ??
          await googleUser.authorizationClient.authorizeScopes(scopes);

      final idToken = googleUser.authentication.idToken;

      if (idToken == null) {
        throw AuthException('No ID Token found.');
      }

      await supabase.auth.signInWithIdToken(
        provider: OAuthProvider.google,
        idToken: idToken,
        accessToken: authorization.accessToken,
      );
    }
    ...
    ```

    <div className="video-container">
      <iframe src="https://www.youtube-nocookie.com/embed/utMg6fVmX0U" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  </TabPanel>

  <TabPanel id="flutter-other" label="Flutter (web, macOS, Windows, Linux)">
    Google sign-in with Supabase on Web, macOS, Windows, and Linux is done through the [`signInWithOAuth`](docs/reference/dart/auth-signinwithoauth) method.

    This method of signing in is web based, and will open a browser window to perform the sign in. For non-web platforms, the user is brought back to the app via [deep linking](/docs/guides/auth/native-mobile-deep-linking?platform=flutter).

    ```dart
    await supabase.auth.signInWithOAuth(
      OAuthProvider.google,
      redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
      authScreenLaunchMode:
          kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
    );
    ```

    This call takes the user to Google's consent screen. Once the flow ends, the user's profile information is exchanged and validated with Supabase Auth before it redirects back to your Flutter application with an access and refresh token representing the user's session.

    <div className="video-container">
      <iframe src="https://www.youtube-nocookie.com/embed/utMg6fVmX0U" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  </TabPanel>

  <TabPanel id="android" label="Android (Kotlin)">
    ### Using Google sign-in on Android

    The Sign in with Google flow on Android uses the [operating system's built-in functionalities](https://developer.android.com/training/sign-in/credential-manager) to prompt the user for consent.

    When the user provides consent, Google issues an identity token (commonly abbreviated as ID token) that is then sent to your project's Supabase Auth server. When valid, a new user session is started by issuing an access and refresh token from Supabase Auth.

    **Note:** You have to create OAuth client IDs for both a Web and Android application. The Web client ID is the one used in your Android app.

    Add the following dependencies to your app. You can find the latest version of `credentials` [here](https://developer.android.com/jetpack/androidx/releases/credentials) and `googleid` [here](https://developers.google.com/identity/android-credential-manager/releases).

    ```kotlin
    implementation("androidx.credentials:credentials:<latest version>")
    implementation ("com.google.android.libraries.identity.googleid:googleid:<latest version>")

    // optional - needed for credentials support from play services, for devices running
    // Android 13 and below.
    implementation("androidx.credentials:credentials-play-services-auth:<latest version>")
    ```

    Add the following ProGuard rules to your `proguard-rules.pro` file:

    ```proguard
    -if class androidx.credentials.CredentialManager
    -keep class androidx.credentials.playservices.** {
      *;
    }
    ```

    Follow the code sample below to implement native Google sign-in with Supabase using Credential Manager in your Android app.

    ```kotlin
    @Composable
    fun GoogleSignInButton() {
        val coroutineScope = rememberCoroutineScope()
        val context = LocalContext.current

        val onClick: () -> Unit = {
            val credentialManager = CredentialManager.create(context)

            // Generate a nonce and hash it with sha-256
            // Providing a nonce is optional but recommended
            val rawNonce = UUID.randomUUID().toString() // Generate a random String. UUID should be sufficient, but can also be any other random string.
            val bytes = rawNonce.toString().toByteArray()
            val md = MessageDigest.getInstance("SHA-256")
            val digest = md.digest(bytes)
            val hashedNonce = digest.fold("") { str, it -> str + "%02x".format(it) } // Hashed nonce to be passed to Google sign-in


            val googleIdOption: GetGoogleIdOption = GetGoogleIdOption.Builder()
                .setFilterByAuthorizedAccounts(false)
                .setServerClientId("WEB_GOOGLE_CLIENT_ID")
                .setNonce(hashedNonce) // Provide the nonce if you have one
                .build()

            val request: GetCredentialRequest = GetCredentialRequest.Builder()
                .addCredentialOption(googleIdOption)
                .build()

            coroutineScope.launch {
                try {
                    val result = credentialManager.getCredential(
                        request = request,
                        context = context,
                    )

                    val googleIdTokenCredential = GoogleIdTokenCredential
                        .createFrom(result.credential.data)

                    val googleIdToken = googleIdTokenCredential.idToken

                    supabase.auth.signInWith(IDToken) {
                        idToken = googleIdToken
                        provider = Google
                        nonce = rawNonce
                    }

                    // Handle successful sign-in
                } catch (e: GetCredentialException) {
                    // Handle GetCredentialException thrown by `credentialManager.getCredential()`
                } catch (e: GoogleIdTokenParsingException) {
                    // Handle GoogleIdTokenParsingException thrown by `GoogleIdTokenCredential.createFrom()`
                } catch (e: RestException) {
                    // Handle RestException thrown by Supabase
                } catch (e: Exception) {
                    // Handle unknown exceptions
                }
            }
        }

        Button(
            onClick = onClick,
        ) {
            Text("Sign in with Google")
        }
    }
    ```

    ### Using Google sign-in with Kotlin Multiplatform

    When using [Compose Multiplatform](https://www.jetbrains.com/lp/compose-multiplatform/), you can use the [compose-auth](/docs/reference/kotlin/installing) plugin. On Android it uses the Credential Manager automatically and on other platforms it uses `auth.signInWith(Google)`.

    **Initialize the Supabase Client**

    **Note:** You have to create OAuth credentials for both a Web and Android application. [Learn more](https://developers.google.com/identity/one-tap/android/get-started#api-console)

    ```kotlin
    val supabaseClient = createSupabaseClient(
        supabaseUrl = "SUPABASE_URL",
        supabaseKey = "SUPABASE_KEY"
    ) {
        install(Auth)
        install(ComposeAuth) {
            googleNativeLogin("WEB_GOOGLE_CLIENT_ID") //Use the Web Client ID, not the Android one!
        }
    }
    ```

    **Use the Compose Auth plugin in your Auth Screen**

    ```kotlin
    val authState = supabaseClient.composeAuth.rememberSignInWithGoogle(
        onResult = {
            when(it) { //handle errors
                NativeSignInResult.ClosedByUser -> TODO()
                is NativeSignInResult.Error -> TODO()
                is NativeSignInResult.NetworkError -> TODO()
                NativeSignInResult.Success -> TODO()
            }
        }
    )

    Button(onClick = { authState.startFlow() }) {
        Text("Sign in with Google")
    }
    ```

    <div className="video-container">
      <iframe src="https://www.youtube-nocookie.com/embed/P_jZMDmodG4" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  </TabPanel>

  <TabPanel id="chrome-extensions" label="Chrome Extensions">
    ### Using native sign in for Chrome extensions

    Similar to the native sign in for Android, you can use the Chrome browser's [identity APIs](https://developer.chrome.com/docs/extensions/reference/identity/) to launch an authentication flow.

    First, you need to configure your `manifest.json` file like so:

    ```json
    {
      "permissions": ["identity"],
      "oauth2": {
        "client_id": "<client ID>",
        "scopes": ["openid", "email", "profile"]
      }
    }
    ```

    Then you should call the [`chrome.identity.launchWebAuthFlow()`](https://developer.chrome.com/docs/extensions/reference/identity/#method-launchWebAuthFlow) function to trigger the sign in flow. On success, call the `supabase.auth.signInWithIdToken()` function to complete sign in with your Supabase project.

    ```ts
    const manifest = chrome.runtime.getManifest()

    const url = new URL('https://accounts.google.com/o/oauth2/auth')

    url.searchParams.set('client_id', manifest.oauth2.client_id)
    url.searchParams.set('response_type', 'id_token')
    url.searchParams.set('access_type', 'offline')
    url.searchParams.set('redirect_uri', `https://${chrome.runtime.id}.chromiumapp.org`)
    url.searchParams.set('scope', manifest.oauth2.scopes.join(' '))

    chrome.identity.launchWebAuthFlow(
      {
        url: url.href,
        interactive: true,
      },
      async (redirectedTo) => {
        if (chrome.runtime.lastError) {
          // auth was not successful
        } else {
          // auth was successful, extract the ID token from the redirectedTo URL
          const url = new URL(redirectedTo)
          const params = new URLSearchParams(url.hash)

          const { data, error } = await supabase.auth.signInWithIdToken({
            provider: 'google',
            token: params.get('id_token'),
          })
        }
      }
    )
    ```
  </TabPanel>
</Tabs>



# Login with Kakao



To enable Kakao Auth for your project, you need to set up an Kakao OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Kakao OAuth consists of six broad steps:

*   Create and configure your app in the [Kakao Developer Portal](https://developers.kakao.com).
*   Obtaining a `REST API key` - this will serve as the `client_id`.
*   Generating the `Client secret code` - this will serve as the `client_secret`.
*   Additional configurations on Kakao Developers Portal.
*   Add your `client id` and `client secret` keys to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access your Kakao Developer account

*   Go to [Kakao Developers Portal](https://developers.kakao.com).
*   Click on `Login` at the top right to log in.

![Kakao Developers Portal.](/docs/img/guides/auth-kakao/kakao-developers-page.png)



## Create and configure your app

*   Go to `My Application`.
*   Click on `Add an application` at the top.
*   Fill out your app information:
    *   App icon.
    *   App name.
    *   Company name.
*   Click `Save` at the bottom right.



## Obtain a REST API key

This will serve as the `client_id` when you make API calls to authenticate the user.

*   Go to `My Application`.
*   Click on your app.
*   You will be redirected to `Summary` tab of your app.
*   In the `App Keys` section you will see `REST API key` -- this ID will become your `client_id` later.



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Kakao** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>

*   To add callback URL on Kakao, go to `Product settings` >
    `Kakao Login` > `Redirect URI`.



## Generate and activate a `client_secret`

*   Go to `Product settings` > `Kakao Login` > `Security`.
*   Click on the `Kakao Login` switch to enable Kakao Login.
*   Click on `generate code` at the bottom to generate the `Client secret code` -- this will serve as a `client_secret` for your Supabase project.
*   Make sure you enabled `Client secret code` by selecting `enable` from the `Activation state` section.



## Additional configurations on Kakao Developers portal

*   Make sure the Kakao Login is enabled in the `Kakao Login` tab.
*   Set following scopes under the "Consent Items": account\_email, profile\_image, profile\_nickname

![Consent items needs to be set.](/docs/img/guides/auth-kakao/kakao-developers-consent-items-set.png)



## Add your OAuth credentials to Supabase

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **Kakao** from the accordion list to expand and turn **Kakao Enabled** to ON
*   Enter your **Kakao Client ID** and **Kakao Client Secret** saved in the previous step
*   Click `Save`



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `kakao` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithKakao() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'kakao',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `kakao` as the `provider`:

    ```dart
    Future<void> signInWithKakao() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.kakao,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Kakao` as the `Provider`:

    ```kotlin
    suspend fun signInWithKakao() {
    	supabase.auth.signInWith(Kakao)
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



## Using Kakao Login JS SDK

[Kakao Login JS SDK](https://developers.kakao.com/docs/latest/en/kakaologin/js) is an official Kakao SDK for authenticating Kakao users on websites.

Exchange the [authorization code returned by Kakao API](https://developers.kakao.com/docs/latest/en/kakaologin/rest-api#request-code) for an [ID Token](https://developers.kakao.com/docs/latest/en/kakaologin/common#login-with-oidc).

For example, this code shows a how to get ID Token:

```
const requestUrl = new URL(request.url);
const code = requestUrl.searchParams.get('code');

if (code) {
  const res = await fetch('https://kauth.kakao.com/oauth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    },
    body: new URLSearchParams({
      grant_type: 'authorization_code',
      client_id: '<CLIENT_ID>',
      redirect_uri: '<url>/api/auth/kakao/oidc',
      code,
      client_secret: '<CLIENT_SECRET>',
    }),
  });

  const {id_token} = await res.json();
}
```

Use the ID Token to sign in:

```
const res = await auth.signInWithIdToken({
  provider: 'kakao',
  token: id_token,
});
```


### Configuration

1.  Set 'State' to 'ON' under [OpenID Connect Activation](https://developers.kakao.com/docs/latest/en/kakaologin/prerequisite#activate-oidc) on Kakao Developers portal Application Dashboard.
2.  Add `openid` to [scope](https://developers.kakao.com/docs/latest/en/kakaologin/common#additional-consent-scope) along with the scope values you wish to obtain consent for.



## Resources

*   [Kakao Developers Portal](https://developers.kakao.com).



# Login with Keycloak



To enable Keycloak Auth for your project, you need to set up an Keycloak OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

To get started with Keycloak, you can run it in a docker container with: `docker run -p 8080:8080 -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin quay.io/keycloak/keycloak:latest start-dev`

This guide will be assuming that you are running Keycloak in a docker container as described in the command above.

Keycloak OAuth consists of five broad steps:

*   Create a new client in your specified Keycloak realm.
*   Obtain the `issuer` from the "OpenID Endpoint Configuration". This will be used as the `Keycloak URL`.
*   Ensure that the new client has the "Client Protocol" set to `openid-connect` and the "Access Type" is set to "confidential".
*   The `Client ID` of the client created will be used as the `client id`.
*   Obtain the `Secret` from the credentials tab which will be used as the `client secret`.
*   Add the callback URL of your application to your allowlist.



## Access your Keycloak admin console

*   Login by visiting [`http://localhost:8080`](http://localhost:8080) and clicking on "Administration Console".



## Create a Keycloak realm

*   Once you've logged in to the Keycloak console, you can add a realm from the side panel. The default realm should be named "Master".
*   After you've added a new realm, you can retrieve the `issuer` from the "OpenID Endpoint Configuration" endpoint. The `issuer` will be used as the `Keycloak URL`.
*   You can find this endpoint from the realm settings under the "General Tab" or visit [`http://localhost:8080/realms/my_realm_name/.well-known/openid-configuration`](http://localhost:8080/realms/my_realm_name/.well-known/openid-configuration)

![Add a Keycloak Realm.](/docs/img/guides/auth-keycloak/keycloak-create-realm.png)



## Create a Keycloak client

The "Client ID" of the created client will serve as the `client_id` when you make API calls to authenticate the user.

![Add a Keycloak client](/docs/img/guides/auth-keycloak/keycloak-add-client.png)



## Client settings

After you've created the client successfully, ensure that you set the following settings:

1.  The "Client Protocol" should be set to `openid-connect`.
2.  The "Access Type" should be set to "confidential".
3.  The "Valid Redirect URIs" should be set to: `https://<project-ref>.supabase.co/auth/v1/callback`.

![Obtain the client id, set the client protocol and access type](/docs/img/guides/auth-keycloak/keycloak-client-id.png)
![Set redirect uri](/docs/img/guides/auth-keycloak/keycloak-redirect-uri.png)



## Obtain the client secret

This will serve as the `client_secret` when you make API calls to authenticate the user.
Under the "Credentials" tab, the `Secret` value will be used as the `client secret`.

![Obtain the client secret](/docs/img/guides/auth-keycloak/keycloak-client-secret.png)



## Add login code to your client app

Since Keycloak version 22, the `openid` scope must be passed. Add this to the [`supabase.auth.signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) method.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `keycloak` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithKeycloak() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'keycloak',
        options: {
          scopes: 'openid',
        },
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `keycloak` as the `provider`:

    ```dart
    Future<void> signInWithKeycloak() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.keycloak,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Keycloak` as the `Provider`:

    ```kotlin
    suspend fun signInWithKeycloak() {
    	supabase.auth.signInWith(Keycloak) {
    		scopes.add("openid")
    	}
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
    import { createClient } from '@supabase/supabase-js';
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>');

    // ---cut---
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   You can find the Keycloak OpenID endpoint configuration under the realm settings.
    ![Keycloak OpenID Endpoint Configuration](/docs/img/guides/auth-keycloak/keycloak-openid-endpoint-config.png)



# Login with LinkedIn



To enable LinkedIn Auth for your project, you need to set up a LinkedIn OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up LinkedIn logins for your application consists of 3 parts:

*   Create and configure a LinkedIn Project and App on the [LinkedIn Developer Dashboard](https://www.linkedin.com/developers/apps).
*   Add your *LinkedIn (OIDC)* `client_id` and `client_secret` to your [Supabase Project](/dashboard).
*   Add the login code to your [Supabase JS Client App](https://github.com/supabase/supabase-js).



## Access your LinkedIn Developer account

*   Go to [LinkedIn Developer Dashboard](https://www.linkedin.com/developers/apps).
*   Log in (if necessary.)

![LinkedIn Developer Portal](/docs/img/guides/auth-linkedin/linkedin_developers_page.png)



## Find your callback URL

The next step requires a callback URL, which looks like this: `https://<project-ref>.supabase.co/auth/v1/callback`

*   Go to your [Supabase Project Dashboard](/dashboard)
*   Click on the `Authentication` icon in the left sidebar
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **LinkedIn** from the accordion list to expand and you'll find your **Callback URL**, you can click `Copy` to copy it to the clipboard

<Admonition type="note">
  For testing OAuth locally with the Supabase CLI see the [local development docs](/docs/guides/cli/local-development#use-auth-locally).
</Admonition>



## Create a LinkedIn OAuth app

*   Go to [LinkedIn Developer Dashboard](https://www.linkedin.com/developers/apps).
*   Click on `Create App` at the top right
*   Enter your `LinkedIn Page` and `App Logo`
*   Save your app
*   Click `Products` from the top menu
*   Look for `Sign In with LinkedIn using OpenID Connect` and click on Request Access
*   Click `Auth` from the top menu
*   Add your `Redirect URL` to the `Authorized Redirect URLs for your app` section
*   Copy and save your newly-generated `Client ID`
*   Copy and save your newly-generated `Client Secret`

Ensure that the appropriate scopes have been added under OAuth 2.0 Scopes at the bottom of the `Auth` screen.

![Required OAuth 2.0 Scopes](/docs/img/guides/auth-linkedin/oauth-scopes.png)



## Enter your LinkedIn (OIDC) credentials into your Supabase project

*   Go to your [Supabase Project Dashboard](/dashboard)
*   In the left sidebar, click the `Authentication` icon (near the top)
*   Click on [`Providers`](/dashboard/project/_/auth/providers) under the Configuration section
*   Click on **LinkedIn (OIDC)** from the accordion list to expand and turn **LinkedIn (OIDC) Enabled** to ON
*   Enter your **LinkedIn (OIDC) Client ID** and **LinkedIn (OIDC) Client Secret** saved in the previous step
*   Click `Save`

You can also configure the LinkedIn (OIDC) auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure LinkedIn (OIDC) auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_linkedin_oidc_enabled": true,
    "external_linkedin_oidc_client_id": "your-linkedin-client-id",
    "external_linkedin_oidc_secret": "your-linkedin-client-secret"
  }'
```



## Add login code to your client app

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `linkedin_oidc` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-project-url>', '<sb_publishable_... or anon key>')

    // ---cut---
    async function signInWithLinkedIn() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'linkedin_oidc',
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `linkedin_oidc` as the `provider`:

    ```dart
    Future<void> signInWithLinkedIn() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.linkedinOidc,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `LinkedIn` as the `Provider`:

    ```kotlin
    suspend fun signInWithKaLinkedIn() {
    	supabase.auth.signInWith(LinkedIn)
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



## LinkedIn Open ID Connect (OIDC)

We will be replacing the *LinkedIn* provider with a new *LinkedIn (OIDC)* provider to support recent changes to the LinkedIn [OAuth APIs](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?context=linkedin%2Fcontext\&tabs=HTTPS1). The new provider utilizes the [Open ID Connect standard](https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/sign-in-with-linkedin-v2#validating-id-tokens). In view of this change, we have disabled edits on the *LinkedIn* provider and will be removing it effective 4th January 2024. Developers with LinkedIn OAuth Applications created prior to 1st August 2023 should create a new OAuth application [via the steps outlined above](/docs/guides/auth/social-login/auth-linkedin#create-a-linkedin-oauth-app) and migrate their credentials from the *LinkedIn* provider to the *LinkedIn (OIDC)* provider. Alternatively, you can also head to the `Products` section and add the newly release`Sign In with LinkedIn using OpenID Connect` to your existing OAuth application.

Developers using the Supabase CLI to test their LinkedIn OAuth application should also update their `config.toml` to make use of the new provider:

```
[auth.external.linkedin_oidc]
enabled = true
client_id = ...
secret = ...
```

Do reach out to support if you have any concerns around this change.



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [LinkedIn Developer Dashboard](https://www.linkedin.com/developers/apps)



---
**Navigation:** [← Previous](./31-login-with-bitbucket.md) | [Index](./index.md) | [Next →](./33-login-with-notion.md)
