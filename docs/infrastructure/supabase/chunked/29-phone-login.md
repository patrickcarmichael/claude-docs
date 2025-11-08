**Navigation:** [← Previous](./28-send-emails-with-custom-smtp.md) | [Index](./index.md) | [Next →](./30-clerk.md)

# Phone Login



Phone Login is a method of authentication that allows users to log in to a website or application without using a password. The user authenticates through a one-time password (OTP) sent via a channel (SMS or WhatsApp).

<Admonition type="note">
  At this time, `WhatsApp` is only supported as a channel for the Twilio and Twilio Verify Providers.
</Admonition>

Users can also log in with their phones using Native Mobile Login with the built-in identity provider. For Native Mobile Login with Android and iOS, see the [Social Login guides](/docs/guides/auth/social-login).

Phone OTP login can:

*   Improve the user experience by not requiring users to create and remember a password
*   Increase security by reducing the risk of password-related security breaches
*   Reduce support burden of dealing with password resets and other password-related flows

<CostWarning />



## Enabling phone login

Enable phone authentication on the [Auth Providers page](/dashboard/project/_/auth/providers) for hosted Supabase projects.

For self-hosted projects or local development, use the [configuration file](/docs/guides/cli/config#auth.sms.enable_signup). See the configuration variables namespaced under `auth.sms`.

You also need to set up an SMS provider. Each provider has its own configuration. Supported providers include MessageBird, Twilio, Vonage, and TextLocal (community-supported).

<AuthSmsProviderConfig />

By default, a user can only request an OTP once every <SharedData data="config">auth.rate\_limits.otp.period</SharedData> and they expire after <SharedData data="config">auth.rate\_limits.otp.validity</SharedData>.



## Signing in with phone OTP

With OTP, a user can sign in without setting a password on their account. They need to verify their phone number each time they sign in.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOtp({
      phone: '+13334445555',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signInWithOTP(
      phone: "+13334445555"
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.signInWith(OTP) {
        phone = "+13334445555"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.auth.sign_in_with_otp({
      'phone': '+13334445555',
    })
    ```
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    ```bash
    curl -X POST 'https://cvwawazfelidkloqmbma.supabase.co/auth/v1/otp' \
    -H "apikey: SUPABASE_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "phone": "+13334445555"
    }'
    ```
  </TabPanel>
</Tabs>

The user receives an SMS with a 6-digit pin that you must verify within 60 seconds.



## Verifying a phone OTP

To verify the one-time password (OTP) sent to the user's phone number, call [`verifyOtp()`](/docs/reference/javascript/auth-verifyotp) with the phone number and OTP:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOtp`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    const {
      data: { session },
      error,
    } = await supabase.auth.verifyOtp({
      phone: '13334445555',
      token: '123456',
      type: 'sms',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyOTP`:

    ```swift
    try await supabase.auth.verifyOTP(
      phone: "+13334445555",
      token: "123456",
      type: .sms
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verifyPhoneOtp`:

    ```kotlin
    supabase.auth.verifyPhoneOtp(
        type = OtpType.Phone.SMS,
        phone = "+13334445555",
        token = "123456"
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    You should present a form to the user so they can input the 6 digit pin, then send it along with the phone number to `verify_otp`:

    ```python
    response = supabase.auth.verify_otp({
      'phone': '13334445555',
      'token': '123456',
      'type': 'sms',
    })
    ```
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    ```bash
    curl -X POST 'https://<PROJECT_REF>.supabase.co/auth/v1/verify' \
    -H "apikey: <SUPABASE_KEY>" \
    -H "Content-Type: application/json" \
    -d '{
      "type": "sms",
      "phone": "+13334445555",
      "token": "123456"
    }'
    ```
  </TabPanel>
</Tabs>

If successful the user will now be logged in and you should receive a valid session like:

```json
{
  "access_token": "<ACCESS_TOKEN>",
  "token_type": "bearer",
  "expires_in": 3600,
  "refresh_token": "<REFRESH_TOKEN>"
}
```

The access token can be sent in the Authorization header as a Bearer token for any CRUD operations on supabase-js. See our guide on [Row Level Security](/docs/guides/auth#row-level-security) for more info on restricting access on a user basis.



## Updating a phone number

To update a user's phone number, the user must be logged in. Call [`updateUser()`](/docs/reference/javascript/auth-updateuser) with their phone number:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    const { data, error } = await supabase.auth.updateUser({
      phone: '123456789',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.updateUser(
      user: UserAttributes(
        phone: "123456789"
      )
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.updateUser {
        phone = "123456789"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.auth.update_user({
      'phone': '123456789',
    })
    ```
  </TabPanel>
</Tabs>

The user receives an SMS with a 6-digit pin that you must [verify](#verifying-a-phone-otp) within 60 seconds.
Use the `phone_change` type when calling `verifyOTP` to update a user’s phone number.



# Rate limits

Rate limits protect your services from abuse

Supabase Auth enforces rate limits on endpoints to prevent abuse. Some rate limits are [customizable](/dashboard/project/_/auth/rate-limits).

You can also manage rate limits using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get current rate limits
curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  | jq 'to_entries | map(select(.key | startswith("rate_limit_"))) | from_entries'


# Update rate limits
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "rate_limit_anonymous_users": 10,
    "rate_limit_email_sent": 10,
    "rate_limit_sms_sent": 10,
    "rate_limit_verify": 10,
    "rate_limit_token_refresh": 10,
    "rate_limit_otp": 10,
    "rate_limit_web3": 10
  }'
```

| Endpoint                                         | Path                                                           | Limited By               | Rate Limit                                                                                                                                                                                                                                                         |
| ------------------------------------------------ | -------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| All endpoints that send emails                   | `/auth/v1/signup` `/auth/v1/recover` `/auth/v1/user`\[^1]       | Sum of combined requests | Defaults to 4 emails per hour as of 14th July 2023. As of 21 Oct 2023, this has been updated to <SharedData data="config">auth.rate\_limits.email.inbuilt\_smtp\_per\_hour</SharedData> emails per hour. You can only change this with your own custom SMTP setup. |
| All endpoints that send One-Time-Passwords (OTP) | `/auth/v1/otp`                                                 | Sum of combined requests | Defaults to <SharedData data="config">auth.rate\_limits.otp.requests\_per\_hour</SharedData> OTPs per hour. Is customizable.                                                                                                                                       |
| Send OTPs or magic links                         | `/auth/v1/otp`                                                 | Last request of the user | Defaults to <SharedData data="config">auth.rate\_limits.otp.period</SharedData> window before a new request is allowed to the same user. Is customizable.                                                                                                          |
| Signup confirmation request                      | `/auth/v1/signup`                                              | Last request of the user | Defaults to <SharedData data="config">auth.rate\_limits.signup\_confirmation.period</SharedData> window before a new request is allowed to the same user. Is customizable.                                                                                         |
| Password Reset Request                           | `/auth/v1/recover`                                             | Last request of the user | Defaults to <SharedData data="config">auth.rate\_limits.password\_reset.period</SharedData> window before a new request is allowed to the same user. Is customizable.                                                                                              |
| Verification requests                            | `/auth/v1/verify`                                              | IP Address               | <SharedData data="config">auth.rate\_limits.verification.requests\_per\_hour</SharedData> requests per hour (with bursts up to <SharedData data="config">auth.rate\_limits.verification.requests\_burst</SharedData> requests)                                     |
| Token refresh requests                           | `/auth/v1/token`                                               | IP Address               | <SharedData data="config">auth.rate\_limits.token\_refresh.requests\_per\_hour</SharedData> requests per hour (with bursts up to <SharedData data="config">auth.rate\_limits.token\_refresh.requests\_burst</SharedData> requests)                                 |
| Create or Verify an MFA challenge                | `/auth/v1/factors/:id/challenge` `/auth/v1/factors/:id/verify` | IP Address               | <SharedData data="config">auth.rate\_limits.mfa.requests\_per\_hour</SharedData> requests per hour (with bursts up to <SharedData data="config">auth.rate\_limits.verification.mfa</SharedData> requests)                                                          |
| Anonymous sign-ins                               | `/auth/v1/signup`\[^2]                                          | IP Address               | <SharedData data="config">auth.rate\_limits.anonymous\_signin.requests\_per\_hour</SharedData> requests per hour (with bursts up to <SharedData data="config">auth.rate\_limits.anonymous\_signin.requests\_burst</SharedData> requests)                           |

\[^1]: The rate limit is only applied on `/auth/v1/user` if this endpoint is called to update the user's email address.

\[^2]: The rate limit is only applied on `/auth/v1/signup` if this endpoint is called without passing in an email or phone number in the request body.



# Redirect URLs

Set up redirect urls with Supabase Auth.


## Overview

Supabase Auth allows you to control how the [user sessions](/docs/guides/auth/sessions) are handled by your application.

When using [passwordless sign-ins](/docs/reference/javascript/auth-signinwithotp) or [third-party providers](/docs/reference/javascript/auth-signinwithoauth#sign-in-using-a-third-party-provider-with-redirect), the Supabase client library provides a `redirectTo` parameter to specify where to redirect the user after authentication. The URL in `redirectTo` should match the [Redirect URLs](/dashboard/project/_/auth/url-configuration) list configuration.

To configure allowed redirect URLs, go to the [URL Configuration](/dashboard/project/_/auth/url-configuration) page. Once you've added necessary URLs, you can use the URL you want the user to be redirected to in the `redirectTo` parameter.

The Site URL in [URL Configuration](/dashboard/project/_/auth/url-configuration) defines the **default redirect URL** when no `redirectTo` is specified in the code. Change this from `http://localhost:3000` to your production URL (e.g., [https://example.com](https://example.com)). This setting is critical for email confirmations and password resets.

When using [Sign in with Web3](/docs/guides/auth/auth-web3), the message signed by the user in the Web3 wallet application will indicate the URL on which the signature took place. Supabase Auth will reject messages that are signed for URLs that are not on the allowed list.

In local development or self-hosted projects, use the [configuration file](/docs/guides/local-development/cli/config#auth.additional_redirect_urls). See below for more information on configuring `SITE_URL` when deploying to Vercel or Netlify.



## Use wildcards in redirect URLs

Supabase allows you to specify wildcards when adding redirect URLs to the [allow list](/dashboard/project/_/auth/url-configuration). You can use wildcard match patterns to support preview URLs from providers like Netlify and Vercel.

| Wildcard                 | Description                                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `*`                      | matches any sequence of non-separator characters                                                                                           |
| `**`                     | matches any sequence of characters                                                                                                         |
| `?`                      | matches any single non-separator character                                                                                                 |
| `c`                      | matches character c (c != `*`, `**`, `?`, `\`, `[`, `{`, `}`)                                                                              |
| `\c`                     | matches character c                                                                                                                        |
| `[!{ character-range }]` | matches any sequence of characters not in the `{ character-range }`. For example, `[!a-z]` will not match any characters ranging from a-z. |

The separator characters in a URL are defined as `.` and `/`. Use [this tool](https://www.digitalocean.com/community/tools/glob?comments=true\&glob=http%3A%2F%2Flocalhost%3A3000%2F%2A%2A\&matches=false\&tests=http%3A%2F%2Flocalhost%3A3000\&tests=http%3A%2F%2Flocalhost%3A3000%2F\&tests=http%3A%2F%2Flocalhost%3A3000%2F%3Ftest%3Dtest\&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest-test%3Ftest%3Dtest\&tests=http%3A%2F%2Flocalhost%3A3000%2Ftest%2Ftest%3Ftest%3Dtest) to test your patterns.

<Admonition type="note" label="Recommendation">
  While the "globstar" (`**`) is useful for local development and preview URLs, we recommend setting the exact redirect URL path for your site URL in production.
</Admonition>


### Redirect URL examples with wildcards

| Redirect URL                   | Description                                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `http://localhost:3000/*`      | matches `http://localhost:3000/foo`, `http://localhost:3000/bar` but not `http://localhost:3000/foo/bar` or `http://localhost:3000/foo/` (note the trailing slash) |
| `http://localhost:3000/**`     | matches `http://localhost:3000/foo`, `http://localhost:3000/bar` and `http://localhost:3000/foo/bar`                                                               |
| `http://localhost:3000/?`      | matches `http://localhost:3000/a` but not `http://localhost:3000/foo`                                                                                              |
| `http://localhost:3000/[!a-z]` | matches `http://localhost:3000/1` but not `http://localhost:3000/a`                                                                                                |



## Netlify preview URLs

For deployments with Netlify, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:

*   `http://localhost:3000/**`
*   `https://**--my_org.netlify.app/**`



## Vercel preview URLs

For deployments with Vercel, set the `SITE_URL` to your official site URL. Add the following additional redirect URLs for local development and deployment previews:

*   `http://localhost:3000/**`
*   `https://*-<team-or-account-slug>.vercel.app/**`

Vercel provides an environment variable for the URL of the deployment called `NEXT_PUBLIC_VERCEL_URL`. See the [Vercel docs](https://vercel.com/docs/concepts/projects/environment-variables#system-environment-variables) for more details. You can use this variable to dynamically redirect depending on the environment. You should also set the value of the environment variable called NEXT\_PUBLIC\_SITE\_URL, this should be set to your site URL in production environment to ensure that redirects function correctly.

```js
const getURL = () => {
  let url =
    process?.env?.NEXT_PUBLIC_SITE_URL ?? // Set this to your site URL in production env.
    process?.env?.NEXT_PUBLIC_VERCEL_URL ?? // Automatically set by Vercel.
    'http://localhost:3000/'
  // Make sure to include `https://` when not localhost.
  url = url.startsWith('http') ? url : `https://${url}`
  // Make sure to include a trailing `/`.
  url = url.endsWith('/') ? url : `${url}/`
  return url
}

const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'github',
  options: {
    redirectTo: getURL(),
  },
})
```



## Email templates when using `redirectTo`

When using a `redirectTo` option, you may need to replace the `{{ .SiteURL }}` with `{{ .RedirectTo }}` in your email templates. See the [Email Templates guide](/docs/guides/auth/auth-email-templates) for more information.

For example, change the following:

```html
<!-- Old -->
<a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Confirm your mail</a>

<!-- New -->
<a href="{{ .RedirectTo }}/auth/confirm?token_hash={{ .TokenHash }}&type=email"
  >Confirm your mail</a
>
```



## Mobile deep linking URIs

For mobile applications you can use deep linking URIs. For example, for your `SITE_URL` you can specify something like `com.supabase://login-callback/` and for additional redirect URLs something like `com.supabase.staging://login-callback/` if needed.

Read more about deep linking and find code examples for different frameworks [here](/docs/guides/auth/native-mobile-deep-linking).



## Error handling

When authentication fails, the user will still be redirected to the redirect URL provided. However, the error details will be returned as query fragments in the URL. You can parse these query fragments and show a custom error message to the user. For example:

```js
const params = new URLSearchParams(window.location.hash.slice())

if (params.get('error_code').startsWith('4')) {
  // show error message if error is a 4xx error
  window.alert(params.get('error_description'))
}
```



# Server-Side Rendering

How SSR works with Supabase Auth.

SSR frameworks move rendering and data fetches to the server, to reduce client bundle size and execution time.

Supabase Auth is fully compatible with SSR. You need to make a few changes to the configuration of your Supabase client, to store the user session in cookies instead of local storage. After setting up your Supabase client, follow the instructions for any flow in the How-To guides.

<Admonition type="tip">
  Make sure to use the PKCE flow instructions where those differ from the implicit flow instructions. If no difference is mentioned, don't worry about this.
</Admonition>



## `@supabase/ssr`

We have developed an [`@supabase/ssr`](https://www.npmjs.com/package/@supabase/ssr) package to make setting up the Supabase client as simple as possible. This package is currently in beta. Adoption is recommended but be aware that the API is still unstable and may have breaking changes in the future.

<Admonition type="caution">
  The Auth helpers package is deprecated. Use the new `@supabase/ssr` package for Server Side Authentication. `@supabase/ssr` takes the core concepts of the Auth Helpers package and makes them available to any server framework. Read out the [migration doc](/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers) to learn more.
</Admonition>



## Framework quickstarts

<div className="grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-6 mb-6 not-prose">
  {[
        {
          title: 'Next.js',
          href: '/guides/auth/server-side/nextjs',
          description:
            'Automatically configure Supabase in Next.js to use cookies, making your user and their session available on the client and server.',
          icon: '/docs/img/icons/nextjs-icon',
        },
        {
          title: 'SvelteKit',
          href: '/guides/auth/server-side/sveltekit',
          description:
            'Automatically configure Supabase in SvelteKit to use cookies, making your user and their session available on the client and server.',
          icon: '/docs/img/icons/svelte-icon',
        },
      ].map((item) => {
        return (
          <Link href={`${item.href}`} key={item.title} passHref>
            <GlassPanel title={item.title} background={false} icon={item.icon}>
              {item.description}
            </GlassPanel>
          </Link>
        )
      })}
</div>



# User sessions



Supabase Auth provides fine-grained control over your user's sessions.

Some security sensitive applications, or those that need to be SOC 2, HIPAA, PCI-DSS or ISO27000 compliant will require some sort of additional session controls to enforce timeouts or provide additional security guarantees. Supabase Auth makes it easy to build compliant applications.



## What is a session?

A session is created when a user signs in. By default, it lasts indefinitely and a user can have an unlimited number of active sessions on as many devices.

A session is represented by the Supabase Auth access token in the form of a JWT, and a refresh token which is a unique string.

Access tokens are designed to be short lived, usually between 5 minutes and 1 hour while refresh tokens never expire but can only be used once. You can exchange a refresh token only once to get a new access and refresh token pair.

This process is called **refreshing the session.**

A session terminates, depending on configuration, when:

*   The user clicks sign out.
*   The user changes their password or performs a security sensitive action.
*   It times out due to inactivity.
*   It reaches its maximum lifetime.
*   A user signs in on another device.



## Access token (JWT) claims

Every access token contains a `session_id` claim, a UUID, uniquely identifying the session of the user. You can correlate this ID with the primary key of the `auth.sessions` table.



## Initiating a session

A session is initiated when a user signs in. The session is stored in the `auth.sessions` table, and your app should receive the access and refresh tokens.

There are two flows for initiating a session and receiving the tokens:

*   [Implicit flow](/docs/guides/auth/sessions/implicit-flow)
*   [PKCE flow](/docs/guides/auth/sessions/pkce-flow)



## Limiting session lifetime and number of allowed sessions per user

<Admonition type="note">
  This feature is only available on Pro Plans and up.
</Admonition>

Supabase Auth can be configured to limit the lifetime of a user's session. By default, all sessions are active until the user signs out or performs some other action that terminates a session.

In some applications, it's useful or required for security to ensure that users authenticate often, or that sessions are not left active on devices for too long.

There are three ways to limit the lifetime of a session:

*   Time-boxed sessions, which terminate after a fixed amount of time.
*   Set an inactivity timeout, which terminates sessions that haven't been refreshed within the timeout duration.
*   Enforce a single-session per user, which only keeps the most recently active session.

To make sure that users are required to re-authenticate periodically, you can set a positive value for the **Time-box user sessions** option in the [Auth settings](/dashboard/project/_/auth/sessions) for your project.

To make sure that sessions expire after a period of inactivity, you can set a positive duration for the **Inactivity timeout** option in the [Auth settings](/dashboard/project/_/auth/sessions).

You can also enforce only one active session per user per device or browser. When this is enabled, the session from the most recent sign in will remain active, while the rest are terminated. Enable this via the *Single session per user* option in the [Auth settings](/dashboard/project/_/auth/sessions).

Sessions are not proactively destroyed when you change these settings, but rather the check is enforced whenever a session is refreshed next. This can confuse developers because the actual duration of a session is the configured timeout plus the JWT expiration time. For single session per user, the effect will only be noticed at intervals of the JWT expiration time. Make sure you adjust this setting depending on your needs. We do not recommend going below 5 minutes for the JWT expiration time.

Otherwise sessions are progressively deleted from the database 24 hours after they expire, which prevents you from causing a high load on your project by accident and allows you some freedom to undo changes without adversely affecting all users.



## Frequently asked questions


### What are recommended values for access token (JWT) expiration?

Most applications should use the default expiration time of 1 hour. This can be customized in your project's [Auth settings](/dashboard/project/_/settings/jwt) in the Advanced Settings section.

Setting a value over 1 hour is generally discouraged for security reasons, but it may make sense in certain situations.

Values below 5 minutes, and especially below 2 minutes, should not be used in most situations because:

*   The shorter the expiration time, the more frequently refresh tokens are used, which increases the load on the Auth server.
*   Time is not absolute. Servers can often be off sync for tens of seconds, but user devices like laptops, desktops or mobile devices can sometimes be off by minutes or even hours. Having too short expiration time can cause difficult-to-debug errors due to clock skew.
*   Supabase's client libraries always try to refresh the session ahead of time, which won't be possible if the expiration time is too short.
*   Access tokens should generally be valid for at least as long as the longest running request in your application. This helps you avoid issues where the access token becomes invalid midway through processing.


### What is refresh token reuse detection and what does it protect from?

As your users continue using your app, refresh tokens are being constantly exchanged for new access tokens.

The general rule is that a refresh token can only be used once. However, strictly enforcing this can cause certain issues to arise. There are two exceptions to this design to prevent the early and unexpected termination of user's sessions:

*   A refresh token can be used more than once within a defined reuse interval. By default this is 10 seconds and we do not recommend changing this value. This exception is granted for legitimate situations such as:
    *   Using server-side rendering where the same refresh token needs to be reused on the server and soon after on the client
    *   To allow some leeway for bugs or issues with serializing access to the refresh token request
*   If the parent of the currently active refresh token for the user's session is being used, the active token will be returned. This exception solves an important and often common situation:
    *   All clients such as browsers, mobile or desktop apps, and even some servers are inherently unreliable due to network issues. A request does not indicate that they received a response or even processed the response they received.
    *   If a refresh token is revoked after being used only once, and the response wasn't received and processed by the client, when the client comes back online, it will attempt to use the refresh token that was already used. Since this might happen outside of the reuse interval, it can cause sudden and unexpected session termination.

Should the reuse attempt not fall under these two exceptions, the whole session is regarded as terminated and all refresh tokens belonging to it are marked as revoked. You can disable this behavior in the Advanced Settings of the [Auth settings](/dashboard/project/_/auth/sessions) page, though it is generally not recommended.

The purpose of this mechanism is to guard against potential security issues where a refresh token could have been stolen from the user, for example by exposing it accidentally in logs that leak (like logging cookies, request bodies or URL params) or via vulnerable third-party servers. It does not guard against the case where a user's session is stolen from their device.


### What are the benefits of using access and refresh tokens instead of traditional sessions?

Traditionally user sessions were implemented by using a unique string stored in cookies that identified the authorization that the user had on a specific browser. Applications would use this unique string to constantly fetch the attached user information on every API call.

This approach has some tradeoffs compared to using a JWT-based approach:

*   If the authentication server or its database crashes or is unavailable for even a few seconds, the whole application goes down. Scheduling maintenance or dealing with transient errors becomes very challenging.
*   A failing authentication server can cause a chain of failures across other systems and APIs, paralyzing the whole application system.
*   All requests that require authentication has to be routed through the authentication, which adds an additional latency overhead to all requests.

Supabase Auth prefers a JWT-based approach using access and refresh tokens because session information is encoded within the short-lived access token, enabling transfer across APIs and systems without dependence on a central server's availability or performance. This approach enhances an application's tolerance to transient failures or performance issues. Furthermore, proactively refreshing the access token allows the application to function reliably even during significant outages.

It's better for cost optimization and scaling as well, as the authentication system's servers and database only handle traffic for this use case.


### How to ensure an access token (JWT) cannot be used after a user signs out

Most applications rarely need such strong guarantees. Consider adjusting the JWT expiry time to an acceptable value. If this is still necessary, you should try to use this validation logic only for the most sensitive actions within your application.

When a user signs out, the sessions affected by the logout are removed from the database entirely. You can check that the `session_id` claim in the JWT corresponds to a row in the `auth.sessions` table. If such a row does not exist, it means that the user has logged out.

Note that sessions are not proactively terminated when their maximum lifetime (time-box) or inactivity timeout are reached. These sessions are cleaned up progressively 24 hours after reaching that status. This allows you to tweak the values or roll back changes without causing unintended user friction.


### Using HTTP-only cookies to store access and refresh tokens

This is possible, but only for apps that use the traditional server-only web app approach where all of the application logic is implemented on the server and it returns rendered HTML only.

If your app uses any client side JavaScript to build a rich user experience, using HTTP-Only cookies is not feasible since only your server will be able to read and refresh the session of the user. The browser will not have access to the access and refresh tokens.

Because of this, the Supabase JavaScript libraries provide only limited support. You can override the `storage` option when creating the Supabase client **on the server** to store the values in cookies or your preferred storage choice, for example:

```typescript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient('SUPABASE_URL', 'SUPABASE_PUBLISHABLE_KEY', {
  auth: {
    storage: {
      getItem: () => {
        return Promise.resolve('FETCHED_COOKIE')
      },
      setItem: () => {},
      removeItem: () => {},
    },
  },
})
```

The `customStorageObject` should implement the `getItem`, `setItem`, and `removeItem` methods from the [`Storage` interface](https://developer.mozilla.org/en-US/docs/Web/API/Storage). Async versions of these methods are also supported.

When using cookies to store access and refresh tokens, make sure that the [`Expires` or `Max-Age` attributes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie#attributes) of the cookies is set to a timestamp very far into the future. Browsers will clear the cookies, but the session will remain active in Supabase Auth. Therefore it's best to let Supabase Auth control the validity of these tokens and instruct the browser to always store the cookies indefinitely.



# JWT Signing Keys

Best practices on managing keys used by Supabase Auth to create and verify JSON Web Tokens

Supabase Auth continuously issues a new JWT for each user session, for as long as the user remains signed in. JWT signing keys provide fine grained control over this important process for the security of your application.

Before continuing check the comprehensive guide on [Sessions](/docs/guides/auth/sessions) for all the details about how Auth creates tokens for a user's session. Read up on [JWTs](/docs/guides/auth/jwts) if you are not familiar with the basics.



## Overview

When a JWT is issued by Supabase Auth, the key used to create its [signature](https://en.wikipedia.org/wiki/Digital_signature) is known as the signing key. Supabase provides two systems for dealing with signing keys: the Legacy system based on the JWT secret, and the new Signing keys system.

| System       | Type                                  | Description                                                                                                                                                                                                                                                                                                                                                                  |
| ------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Legacy       | JWT secret                            | Initially Supabase was designed to use a single shared secret key to sign all JWTs. This includes <span className="!whitespace-nowrap">the `anon` and `service_role`</span> keys, all user access tokens including some [Storage pre-signed URLs](/docs/reference/javascript/storage-from-createsignedurl). **No longer recommended.** Available for backward compatibility. |
| Signing keys | Asymmetric key (RSA, Elliptic Curves) | A JWT signing key based on [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) (RSA, Elliptic Curves) that follows industry best practices and significantly improves the security, reliability and performance of your applications.                                                                                                           |
| Signing keys | Shared secret key                     | A JWT signing key based on a [shared secret](https://en.wikipedia.org/wiki/HMAC).                                                                                                                                                                                                                                                                                            |


### Benefits of the signing keys system

We've designed the Signing keys system to address many problems the legacy system had. It goes hand-in-hand with the [publishable and secret API keys](/docs/guides/api/api-keys).

| Benefit                                     | Legacy JWT secret                                                                                                | JWT signing keys                                                                                                                                                                       |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Performance                                 | Increased app latency as JWT validation is done by Auth server.                                                  | If using asymmetric signing key, JWT validation is fast and does not involve Auth server.                                                                                              |
| Reliability                                 | To ensure secure revocation, Auth server is in the hot path of your application.                                 | If using asymmetric signing key, JWT validation is local and fast and does not involve Auth server.                                                                                    |
| Security                                    | Requires changing of your application's backend components to fully revoke a compromised secret.                 | If using asymmetric signing key, revocation is automatic via the key discovery endpoint.                                                                                               |
| Zero-downtime rotation                      | Downtime, sometimes being significant. Requires careful coordination with [API keys](/docs/guides/api/api-keys). | No downtime, as each rotation step is independent and reversible.                                                                                                                      |
| Users signed out during rotation            | Currently active users get immediately signed out.                                                               | No users get signed out.                                                                                                                                                               |
| Independence from API keys                  | `anon` and `service_role` must be rotated simultaneously.                                                        | [Publishable and secret API keys](/docs/guides/api/api-keys) no longer are based on the JWT signing key and can be independently managed.                                              |
| Security compliance frameworks (SOC2, etc.) | Difficult to remain aligned as the secret can be extracted from Supabase.                                        | Easier alignment as the private key or shared secret can't be extracted. [Row Level Security](/docs/guides/database/postgres/row-level-security) has strong key revocation guarantees. |



## Getting started

You can start migrating away from the legacy JWT secret through the Supabase dashboard. This process does not cause downtime for your application.

1.  Start off by clicking the *Migrate JWT secret* button on the [JWT signing keys](/dashboard/project/_/settings/jwt/signing-keys) page. This step will import the existing legacy JWT secret into the new JWT signing keys system. Once this process completes, you will no longer be able to rotate the legacy JWT secret using the old system.
2.  Simultaneously, we're creating a new asymmetric JWT signing key for you to rotate to. This key starts off as standby key -- meaning it's being advertised as a key that Supabase Auth will use in the future to create JWTs.
3.  If you're not ready to switch away from the legacy JWT secret right now, you can stop here without any issue. If you wish to use a different signing key -- either to use a different signing algorithm (RSA, Elliptic Curve or shared secret) or to import a private key or shared secret you already have -- feel free to move the standby key to *Previously used* before finally moving it to *Revoked.*
4.  If you do wish to start using the standby key for all new JWT use the *Rotate keys* button. A few important notes:
    *   Make sure your app does not directly rely on the legacy JWT secret. If it's verifying every JWT against the legacy JWT secret (using a library like `jose`, `jsonwebtoken` or similar), continuing with the rotation might break those components.
    *   If you're using [Edge Functions](/docs/guides/functions) that have the Verify JWT setting, continuing with the rotation might break your app. You will need to turn off this setting.
    *   In both cases, change or add code to your app or Edge Function that verifies the JWT. Use the `supabase.auth.getClaims()` function or read more about [Verifying a JWT from Supabase](/docs/guides/auth/jwts#verifying-a-jwt-from-supabase) on the best way to do this.
5.  Rotating the keys immediately causes the Auth server to issue new JWT access tokens for signed in users signed with the new key. Non-expired access tokens will remain to be accepted, so no users will be forcefully signed out.
6.  Plan for revocation of the legacy JWT secret.
    *   If your access token expiry time is configured to be 1 hour, wait at least 1 hour and 15 minutes before revoking the legacy JWT secret -- now under the *Previously used* section.
    *   This prevents currently active users from being forcefully signed out.
    *   In some situations, such as an active security incident you may want to revoke the legacy JWT secret immediately.



## Rotating and revoking keys

Key rotation and revocation are one of the most important processes for maintaining the security of your project and applications. The signing keys system allows you to efficiently execute these without causing downtime of your app, a deficiency present in the legacy system. Below are some common reasons when and why you should consider key rotation and revocation.

**Malicious actors abusing the legacy JWT secret, or imported private key**

*   The legacy JWT secret has been leaked in logs, committed to source control, or accidentally exposed in the frontend build of your application, a library, desktop or mobile app package, etc.
*   You suspect that a [member of your organization](/docs/guides/platform/access-control) has lost control of their devices, and a malicious actor may have accessed the JWT secret via the Supabase dashboard or by accessing your application's backend configuration.
*   You suspect that an ex-team-member of your organization may be a malicious actor, by abusing the power the legacy JWT secret provides.
*   Make sure you also switch to [publishable and secret API keys](/docs/guides/api/api-keys) and disable the `anon` and `service_role` keys.
*   If you've imported a private key, and you're suspecting that this private key has been compromised on your end similarly.

**Closer alignment to security best practices and compliance frameworks (SOC2, PCI-DSS, ISO27000, HIPAA, ...)**

*   It is always prudent to rotate signing keys at least once a year.
*   Some security compliance frameworks strongly encourage or require frequent cryptographic key rotation.
*   If you're using Supabase as part of a large enterprise, this may be required by your organization's security department.
*   Creating muscle memory for the time you'll need to respond to an active security incident.

**Changing key algorithm for technical reasons**

*   You may wish to switch signing algorithms due to compatibility problems or to simplify development on your end.


### Lifetime of a signing key

<div className="flex flex-row gap-6 items-center w-full">
  <Image
    alt="Diagram showing the state transitions of a signing key"
    src={{
    light: '/docs/img/guides/auth-signing-keys/states.svg',
    dark: '/docs/img/guides/auth-signing-keys/states.svg',
  }}
    containerClassName="max-w-[300px] min-w-[180px]"
  />

  <div>
    A newly created key starts off as standby, before being rotated into in use (becoming the current key) while the existing current key becomes previously used.

    At any point you can move a key from the previously used or revoked states back to being a standby key, and rotate to it. This gives you the confidence to revert back to an older key if you identify problems with the rotation, such as forgetting to update a component of your application that is relying on a specific key (for example, the legacy JWT secret).

    Each action on a key is reversible (except permanent deletion).
  </div>
</div>

| Action                                                                           | Accepted JWT signatures                                                | Description                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span className="!whitespace-nowrap">Create a new key</span>                     | Current key only, new key has not created any JWTs yet.                | When you initially create a key, after choosing the signing algorithm or importing a private key you already have, it starts out in the standby state. If using an asymmetric key (RSA, Elliptic Curve) its public key will be available in the discovery endpoint. Supabase Auth does not use this key to create new JWTs. |
| <span className="!whitespace-nowrap">Rotate keys</span>                          | Both keys in the rotation.                                             | Rotation only changes the key used by Supabase Auth to create new JWTs, but the trust relationship with both keys remains.                                                                                                                                                                                                  |
| <span className="!whitespace-nowrap">Revoke key</span>                           | <span className="!whitespace-nowrap">Only from the current key.</span> | Once all regularly valid JWTs have expired (or sooner) revoke the previously used key to revoke trust in it.                                                                                                                                                                                                                |
| <span className="!whitespace-nowrap">Move to standby</span> from revoked         | Current and previously revoked key.                                    | If you've made a mistake or need more time to adjust your application, you can move a revoked key to standby. Follow up with a rotation to ensure Auth starts using the originally revoked key again to make new JWTs.                                                                                                      |
| <span className="!whitespace-nowrap">Move to standby</span> from previously used | Both keys.                                                             | This only prepares the key from the last rotation to be used by Auth to make new JWTs with it.                                                                                                                                                                                                                              |
| <span className="!whitespace-nowrap">Delete key</span>                           | -                                                                      | Permanently destroys the private key or shared secret of a key, so it will not be possible to re-use or rotate again into it.                                                                                                                                                                                               |


### Public key discovery and caching

When your signing keys use an asymmetric algorithm based on [public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) Supabase Auth exposes the public key in the JSON Web Key Set discovery endpoint, for anyone to see. This is an important security feature allowing you to rotate and revoke keys without needing to deploy new versions of your app's backend infrastructure.

Access the currently trusted signing keys at the following endpoint:

```http
GET https://project-id.supabase.co/auth/v1/.well-known/jwks.json
```

Note that this is secure as public keys are irreversible and can only be used to verify the signature of JSON Web Tokens, but not create new ones.

This discovery endpoint is cached by Supabase's edge servers for 10 minutes. Furthermore the Supabase client libraries may cache the keys in memory for an additional 10 minutes. Your application may be using different caching behavior if you're not relying only on the Supabase client library.

This multi-level cache is a trade-off allowing fast JWT verification without placing the Auth server in the hot path of your application, increasing its reliability and performance.

Importantly Supabase products **do not rely on this cache**, so stronger security guarantees are provided especially when keys are revoked. If your application only uses [Row Level Security](/docs/guides/database/postgres/row-level-security) policies and does not have any other backend components (such as APIs, Edge Functions, servers, etc.) key rotation and revocation are instantaneous.

Finally this multi-level cache is cleared every 20 minutes, or longer if you have a custom setup. Consider the following problems that may arise due to it:

*   **Urgent key revocation.** If you are in a security incident where a signing key must be urgently revoked, due to the multi-level cache your application components may still trust and authenticate JWTs signed with the revoked key. Supabase products (Auth, Data API, Storage, Realtime) **do not rely on this cache and revocation is instantaneous.** Should this be an issue for you, ensure you've built a cache busting mechanism as part of your app's backend infrastructure.
*   **Quick key creation and rotation.** If you're migrating away from the legacy JWT secret or when only using the `supabase.auth.getClaims()` method this case is handled for you automatically. If you're verifying JWTs on your own, without the help of the Supabase client library, ensure that **all caches in your app** have picked up the newly created standby key before proceeding to rotation.



## Choosing the right signing algorithm

To strike the right balance between performance, security and ease-of-use, JWT signing keys are based on capabilities available in the [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API).

| Algorithm                                                                                                                                   | <span className="!whitespace-nowrap">JWT `alg`</span> | Information                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span className="!whitespace-nowrap">[NIST P-256 Curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)</span><br />(Asymmetric) | <span className="!whitespace-nowrap">`ES256`</span>   | Elliptic Curves are a faster alternative than RSA, while providing comparable security. Especially important for Auth use cases is the fact that signatures using the P-256 curve are significantly shorter than those created by RSA, which reduces data transfer sizes and helps in managing cookie size. Web Crypto and most other cryptography libraries and runtimes support this curve. |
| <span className="!whitespace-nowrap">[RSA 2048](https://en.wikipedia.org/wiki/RSA_cryptosystem)</span><br />(Asymmetric)                    | <span className="!whitespace-nowrap">`RS256`</span>   | RSA is the oldest and most widely supported public-key cryptosystem in use. While being easy to code by hand, it can be significantly slower than elliptic curves in certain aspects. We recommend using the P-256 elliptic curve instead.                                                                                                                                                    |
| <span className="!whitespace-nowrap">[Ed25519 Curve](https://en.wikipedia.org/wiki/EdDSA#Ed25519)</span><br />(Asymmetric)                  | <span className="!whitespace-nowrap">`EdDSA`</span>   | Coming soon. This algorithm is based on a different elliptic curve cryptosystem developed in the open, unlike the P-256 curve. Web Crypto or other crypto libraries may not support it in all runtimes, making it difficult to work with.                                                                                                                                                     |
| <span className="!whitespace-nowrap">[HMAC with shared secret](https://en.wikipedia.org/wiki/HMAC)</span><br />(Symmetric)                  | <span className="!whitespace-nowrap">`HS256`</span>   | **Not recommended for production applications.** A shared secret uses a message authentication code to verify the authenticity of a JSON Web Token. This requires that both the creator of the JWT (Auth) and the system verifying the JWT know the secret. As there is no public key counterpart, revoking this key might require deploying changes to your app's backend infrastructure.    |

<Admonition type="caution">
  There is almost no benefit from using a JWT signed with a shared secret. Although it's computationally more efficient and verification is simpler to code by hand, using this approach can expose your project's data to significant security vulnerabilities or weaknesses.

  Consider the following:

  *   Using a shared secret can make it more difficult to keep aligned with security compliance frameworks such as SOC2, PCI-DSS, ISO27000, HIPAA, etc.
  *   A shared secret that is in the hands of a malicious actor can be used to impersonate your users, give them access to privileged actions or data.
  *   It is difficult to detect or identify when or how a shared secret has been given to a malicious actor.
  *   Consider who might have even accidental access to the shared secret: systems, staff, devices (and their disk encryption and vulnerability patch status).
  *   A malicious actor can use a shared secret **far into the future**, so lacking current evidence of compromise does not mean your data is secure.
  *   It can be very easy to accidentally leak the shared secret in publicly available source code such as in your website or frontend, mobile app package or other executable. This is especially true if you accidentally add the secret in environment variables prefixed with `NEXT_PUBLIC_`, `VITE_`, `PUBLIC_` or other conventions by web frameworks.
  *   Rotating shared secrets might require careful coordination to avoid downtime of your app.
</Admonition>



## Frequently asked questions


### Why is it not possible to extract the private key or shared secret from Supabase?

You can only extract the legacy JWT secret. Once you've moved to using the JWT signing keys feature extracting of the private key or shared secret from Supabase is not possible. This ensures that no one in your organization is able to impersonate your users or gain privileged access to your project's data.

This guarantee provides your application with close alignment with security compliance frameworks (SOC2, PCI-DSS, ISO27000, HIPAA) and security best practices.


### How to create (mint) JWTs if access to the private key or shared secret is not possible?

If you wish to make your own JWTs or have access to the private key or shared secret used by Supabase, you can create a new JWT signing key by importing a private key or setting a shared secret yourself.

Use the [Supabase CLI](/docs/reference/cli/introduction) to quickly and securely generate a private key ready for import:

```sh
supabase gen signing-key --algorithm ES256
```

Make sure you store this private key in a secure location, as it will not be extractable from Supabase.

To import the generated private key to your project, create a [new standby key](/dashboard/project/_/settings/jwt/signing-keys) from the dashboard:

```json
{
  "kty": "EC",
  "kid": "3a18cfe2-7226-43b0-bbb4-7c5242f2406e",
  "d": "RDbwqThwtGP4WnvACvO_0nL0oMMSmMFSYMPosprlAog",
  "crv": "P-256",
  "x": "gyLVvp9dyEgylYH7nR2E2qdQ_-9Pv5i1tk7c2qZD4Nk",
  "y": "CD9RfYOTyjR5U-PC9UDlsthRpc7vAQQQ2FTt8UsX0fY"
}
```

Once imported, click **Rotate key** to activate your new signing key. Any JWT signed by your old key will continue to be usable until your old signing key is manually revoked.

To mint a new JWT using the asymmetric signing key, you need to set the following [JWT headers](/docs/guides/auth/jwts#introduction) to match your generated private key.

```json
{
  "alg": "ES256",
  "kid": "3a18cfe2-7226-43b0-bbb4-7c5242f2406e",
  "typ": "JWT"
}
```

<Admonition type="note">
  The `kid` header is used to identify your public key for verification. You must use the same value when importing on platform.
</Admonition>

In addition, you need to provide the following custom claims as the JWT payload.

```json
{
  "sub": "ef0493c9-3582-425f-a362-aef909588df7",
  "role": "authenticated",
  "exp": 1757749466
}
```

*   `sub` is an optional UUID that uniquely identifies a user you want to impersonate in `auth.users` table.
*   `role` must be set to an existing Postgres role in your database, such as `anon`, `authenticated`, or `service_role`.
*   `exp` must be set to a timestamp in the future (seconds since 1970) when this token expires. Prefer shorter-lived tokens.

For simplicity, use the following CLI command to generate tokens with the desired header and payload.

```bash
supabase gen bearer-jwt --role authenticated --sub ef0493c9-3582-425f-a362-aef909588df7
```

Finally, you can use your newly minted JWT by setting the `Authorization: Bearer <JWT>` header to all [Data API requests](/docs/guides/auth/jwts#using-custom-or-third-party-jwts).

<Admonition type="note">
  A separate `apikey` header is required to access your project's APIs. This can be a [publishable, secret or the legacy `anon` or `service_role` keys](/docs/guides/api/api-keys). Using your minted JWT is not possible in this header.
</Admonition>


### Why is a 5 minute wait imposed when changing signing key states?

Changing a JWT signing key's state sets off many changes inside the Supabase platform. To ensure a consistent setup, most actions that change the state of a JWT signing key are throttled for approximately 5 minutes.


### Why is deleting the legacy JWT secret disallowed?

This is to ensure you have the ability, should you need it, to go back to the legacy JWT secret. In the future this capability will be allowed from the dashboard.


### Why does revoking the legacy JWT secret require disabling of `anon` and `service_role` API keys?

Unfortunately `anon` and `service_role` are not just API keys, but are also valid JSON Web Tokens, signed by the legacy JWT secret. Revoking the legacy JWT secret means that your application no longer trusts any JWT signed with it. Therefore before you revoke the legacy JWT secret, you must disable the `anon` and `service_role` to ensure a consistent security setup.



# Signing out

Signing out a user

Signing out a user works the same way no matter what method they used to sign in.

Call the sign out method from the client library. It removes the active session and clears Auth data from the storage medium.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
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

  <TabPanel id="dart" label="Dart">
    ```dart
    Future<void> signOut() async {
       await supabase.auth.signOut();
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signOut()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    suspend fun logout() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.auth.sign_out()
    ```
  </TabPanel>
</Tabs>



## Sign out and scopes

Supabase Auth allows you to specify three different scopes for when a user invokes the [sign out API](/docs/reference/javascript/auth-signout) in your application:

*   `global` (default) when all sessions active for the user are terminated.
*   `local` which only terminates the current session for the user but keep sessions on other devices or browsers active.
*   `others` to terminate all but the current session for the user.

You can invoke these by providing the `scope` option:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient(
      'https://your-project-id.supabase.co',
      'sb_publishable_... or anon key'
    )

    // ---cut---
    // defaults to the global scope
    await supabase.auth.signOut()

    // sign out from the current session only
    await supabase.auth.signOut({ scope: 'local' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    // defaults to the local scope
    await supabase.auth.signOut();

    // sign out from all sessions
    await supabase.auth.signOut(scope: SignOutScope.global);
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    // defaults to the local scope
    await supabase.auth.signOut();

    // sign out from all sessions
    supabase.auth.signOut(SignOutScope.GLOBAL)
    ```
  </TabPanel>
</Tabs>

Upon sign out, all refresh tokens and potentially other database objects related to the affected sessions are destroyed and the client library removes the session stored in the local storage medium.

<Admonition type="caution">
  Access Tokens of revoked sessions remain valid until their expiry time, encoded in the `exp` claim. The user won't be immediately logged out and will only be logged out when the Access Token expires.
</Admonition>



# Social Login



Social Login (OAuth) is an open standard for authentication that allows users to log in to one website or application using their credentials from another website or application. OAuth allows users to grant third-party applications access to their online accounts without sharing their passwords.
OAuth is commonly used for things like logging in to a social media account from a third-party app. It is a secure and convenient way to authenticate users and share information between applications.



## Benefits

There are several reasons why you might want to add social login to your applications:

*   **Improved user experience**: Users can register and log in to your application using their existing social media accounts, which can be faster and more convenient than creating a new account from scratch. This makes it easier for users to access your application, improving their overall experience.

*   **Better user engagement**: You can access additional data and insights about your users, such as their interests, demographics, and social connections. This can help you tailor your content and marketing efforts to better engage with your users and provide a more personalized experience.

*   **Increased security**: Social login can improve the security of your application by leveraging the security measures and authentication protocols of the social media platforms that your users are logging in with. This can help protect against unauthorized access and account takeovers.



## Set up a social provider with Supabase Auth

Supabase supports a suite of social providers. Follow these guides to configure a social provider for your platform.

<div className="grid grid-cols-12 xs:gap-x-10 gap-y-10 not-prose py-8">
  <NavData data="socialLoginItems">
    {(data) =>
              data.map((item) => (
                <Link
                  href={`${item.url}`}
                  key={item.name}
                  passHref
                  className="col-span-12 xs:col-span-6 lg:col-span-4 xl:col-span-3"
                >
                  <IconPanel
                    title={item.name}
                    span="col-span-6"
                    icon={item.icon}
                    isDarkMode={item.isDarkMode}
                    hasLightIcon={item.hasLightIcon}
                  >
                    {item.description}
                  </IconPanel>
                </Link>
              ))
            }
  </NavData>
</div>



## Provider tokens

You can use the provider token and provider refresh token returned to make API calls to the OAuth provider. For example, you can use the Google provider token to access Google APIs on behalf of your user.

Supabase Auth does not manage refreshing the provider token for the user. Your application will need to use the provider refresh token to obtain a new provider token. If no provider refresh token is returned, then it could mean one of the following:

*   The OAuth provider does not return a refresh token
*   Additional scopes need to be specified in order for the OAuth provider to return a refresh token.

Provider tokens are intentionally not stored in your project's database. This is because provider tokens give access to potentially sensitive user data in third-party systems. Different applications have different needs, and one application's OAuth scopes may be significantly more permissive than another. If you want to use the provider token outside of the browser that completed the OAuth flow, it is recommended to send it to a trusted and secure server you control.



# Users



A **user** in Supabase Auth is someone with a user ID, stored in the Auth schema. Once someone is a user, they can be issued an Access Token, which can be used to access Supabase endpoints. The token is tied to the user, so you can restrict access to resources via [RLS policies](/docs/guides/database/postgres/row-level-security).



## Permanent and anonymous users

Supabase distinguishes between permanent and anonymous users.

*   **Permanent users** are tied to a piece of Personally Identifiable Information (PII), such as an email address, a phone number, or a third-party identity. They can use these identities to sign back into their account after signing out.
*   **Anonymous users** aren't tied to any identities. They have a user ID and a personalized Access Token, but they have no way of signing back in as the same user if they are signed out.

Anonymous users are useful for:

*   E-commerce applications, to create shopping carts before checkout
*   Full-feature demos without collecting personal information
*   Temporary or throw-away accounts

See the [Anonymous Signins guide](/docs/guides/auth/auth-anonymous) to learn more about anonymous users.

<Admonition type="caution" title="Anonymous users do not use the anon role">
  Just like permanent users, anonymous users use the **authenticated** role for database access.

  The **anon** role is for those who aren't signed in at all and are not tied to any user ID. We refer to these as unauthenticated or public users.
</Admonition>



## The user object

The user object stores all the information related to a user in your application. The user object can be retrieved using one of these methods:

1.  [`supabase.auth.getUser()`](/docs/reference/javascript/auth-getuser)
2.  Retrieve a user object as an admin using [`supabase.auth.admin.getUserById()`](/docs/reference/javascript/auth-admin-listusers)

A user can sign in with one of the following methods:

*   Password-based method (with email or phone)
*   Passwordless method (with email or phone)
*   OAuth
*   SAML SSO

An identity describes the authentication method that a user can use to sign in. A user can have multiple identities. These are the types of identities supported:

*   Email
*   Phone
*   OAuth
*   SAML

<Admonition type="note">
  A user with an email or phone identity will be able to sign in with either a password or passwordless method (e.g. use a one-time password (OTP) or magic link). By default, a user with an unverified email or phone number will not be able to sign in.
</Admonition>

The user object contains the following attributes:

| Attributes           | Type             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id                   | `string`         | The unique id of the identity of the user.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| aud                  | `string`         | The audience claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| role                 | `string`         | The role claim used by Postgres to perform Row Level Security (RLS) checks.                                                                                                                                                                                                                                                                                                                                                                                        |
| email                | `string`         | The user's email address.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| email\_confirmed\_at | `string`         | The timestamp that the user's email was confirmed. If null, it means that the user's email is not confirmed.                                                                                                                                                                                                                                                                                                                                                       |
| phone                | `string`         | The user's phone number.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| phone\_confirmed\_at | `string`         | The timestamp that the user's phone was confirmed. If null, it means that the user's phone is not confirmed.                                                                                                                                                                                                                                                                                                                                                       |
| confirmed\_at        | `string`         | The timestamp that either the user's email or phone was confirmed. If null, it means that the user does not have a confirmed email address and phone number.                                                                                                                                                                                                                                                                                                       |
| last\_sign\_in\_at   | `string`         | The timestamp that the user last signed in.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| app\_metadata        | `object`         | The `provider` attribute indicates the first provider that the user used to sign up with. The `providers` attribute indicates the list of providers that the user can use to login with.                                                                                                                                                                                                                                                                           |
| user\_metadata       | `object`         | Defaults to the first provider's identity data but can contain additional custom user metadata if specified. Refer to [**User Identity**](/docs/guides/auth/auth-identity-linking#the-user-identity) for more information about the identity object. Don't rely on the order of information in this field. Do not use it in security sensitive context (such as in RLS policies or authorization logic), as this value is editable by the user without any checks. |
| identities           | `UserIdentity[]` | Contains an object array of identities linked to the user.                                                                                                                                                                                                                                                                                                                                                                                                         |
| created\_at          | `string`         | The timestamp that the user was created.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| updated\_at          | `string`         | The timestamp that the user was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| is\_anonymous        | `boolean`        | Is true if the user is an anonymous user.                                                                                                                                                                                                                                                                                                                                                                                                                          |



## Resources

*   [User Management guide](/docs/guides/auth/managing-user-data)



# Auth0

Use Auth0 with your Supabase project

Auth0 can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.



## Getting started

1.  First you need to add an integration to connect your Supabase project with your Auth0 tenant. You will need your tenant ID (and in some cases region ID).
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party).
3.  Assign the `role: 'authenticated'` custom claim to all JWTs by using an Auth0 Action.
4.  Finally setup the Supabase client in your application.



## Setup the Supabase client library

<Tabs type="underlined" queryGroup="auth0-create-client">
  <TabPanel id="ts" label="TypeScript">
    ```typescript
    import { createClient } from '@supabase/supabase-js'
    import Auth0Client from '@auth0/auth0-spa-js'

    const auth0 = new Auth0Client({
      domain: '<AUTH0_DOMAIN>',
      clientId: '<AUTH0_CLIENT_ID>',
      authorizationParams: {
        redirect_uri: '<MY_CALLBACK_URL>',
      },
    })

    const supabase = createClient(
      'https://<supabase-project>.supabase.co',
      'SUPABASE_PUBLISHABLE_KEY',
      {
        accessToken: async () => {
          const accessToken = await auth0.getTokenSilently()

          // Alternatively you can use (await auth0.getIdTokenClaims()).__raw to
          // use an ID token instead.

          return accessToken
        },
      }
    )
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift (iOS)">
    ```swift
    import Auth0
    import Supabase

    extension CredentialsManager {
      static let shared = Auth0.CredentialsManager(authentication: Auth0.authentication())
    }

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://<supabase-project>.supabase.co")!,
      supabaseKey: "SUPABASE_PUBLISHABLE_KEY",
      options: SupabaseClientOptions(
        auth: SupabaseClientOptions.AuthOptions(
          accessToken: {
            try await CredentialsManager.shared.credentials().idToken
          }
        )
      )
    )
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    import 'package:auth0_flutter/auth0_flutter.dart';
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    Future<void> main() async {
      final auth0 = Auth0('AUTH0_DOMAIN', 'AUTH0_CLIENT_ID');
      await Supabase.initialize(
        url: 'https://<supabase-project>.supabase.co',
        anonKey: 'SUPABASE_PUBLISHABLE_KEY',
        accessToken: () async {
          final credentials = await auth0.credentialsManager.credentials();
          return credentials.accessToken;
        },
      );
      runApp(const MyApp());
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    import com.auth0.android.result.Credentials

    val supabase = createSupabaseClient(
        "https://<supabase-project>.supabase.co",
        "SUPABASE_PUBLISHABLE_KEY"
    ) {
        accessToken = {
            val credentials: Credentials = ...; // Get credentials from Auth0
            credentials.accessToken
        }
    }
    ```
  </TabPanel>
</Tabs>



## Add a new Third-Party Auth integration to your project

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

In the CLI add the following config to your `supabase/config.toml` file:

```toml
[auth.third_party.auth0]
enabled = true
tenant = "<id>"
tenant_region = "<region>" # if your tenant has a region
```



## Use an Auth0 Action to assign the authenticated role

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

By default, Auth0 JWTs (both access token and ID token) do not contain a `role` claim in them. If you were to send such a JWT to your Supabase project, the `anon` role would be assigned when executing the Postgres query. Most of your app's logic will be accessible by the `authenticated` role.

A recommended approach to do this is to configure the [`onExecutePostLogin` Auth0 Action](https://auth0.com/docs/secure/tokens/json-web-tokens/create-custom-claims#create-custom-claims) which will add the custom claim:

```javascript
exports.onExecutePostLogin = async (event, api) => {
  api.accessToken.setCustomClaim('role', 'authenticated')
}
```



## Limitations

At this time, Auth0 tenants with the following [signing algorithms](https://auth0.com/docs/get-started/applications/signing-algorithms) are not supported:

*   HS256 (HMAC with SHA-256) -- also known as symmetric JWTs
*   PS256 (RSA-PSS with SHA-256)



# Amazon Cognito (Amplify)

Use Amazon Cognito via Amplify or standalone with your Supabase project

Amazon Cognito User Pools (via AWS Amplify or on its own) can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.



## Getting started

1.  First you need to add an integration to connect your Supabase project with your Amazon Cognito User Pool. You will need the pool's ID and region.
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party) or configure it in the CLI.
3.  Assign the `role: 'authenticated'` custom claim to all JWTs by using a Pre-Token Generation Trigger.
4.  Finally setup the Supabase client in your application.



## Setup the Supabase client library

<Tabs type="underlined" queryGroup="cognito-create-client">
  <TabPanel id="ts" label="TypeScript (Amplify)">
    ```typescript
    import { fetchAuthSession, Hub } from 'aws-amplify/auth'

    const supabase = createClient(
      'https://<supabase-project>.supabase.co',
      'SUPABASE_PUBLISHABLE_KEY',
      {
        accessToken: async () => {
          const tokens = await fetchAuthSession()

          // Alternatively you can use tokens?.idToken instead.
          return tokens?.accessToken
        },
      }
    )

    // if you're using Realtime you also need to set up a listener for Cognito auth changes
    Hub.listen('auth', () => {
      fetchAuthSession().then((tokens) => supabase.realtime.setAuth(tokens?.accessToken))
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift (iOS)">
    ```swift
    import Supabase
    import AWSPluginsCore

    struct UnexpectedAuthSessionError: Error {}

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://<supabase-project>.supabase.co")!,
      supabaseKey: "SUPABASE_PUBLISHABLE_KEY",
      options: SupabaseClientOptions(
        auth: SupabaseClientOptions.AuthOptions(
          accessToken: {
            let session = try await Amplify.Auth.fetchAuthSession()

            guard let cognitoTokenProvider = session as? AuthCognitoTokensProvider else {
              throw UnexpectedAuthSessionError()
            }

            let tokens = try cognitoTokenProvider.getCognitoTokens().get()
            return tokens.idToken
          }
        )
      )
    )
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    import 'package:amplify_auth_cognito/amplify_auth_cognito.dart';
    import 'package:amplify_flutter/amplify_flutter.dart';
    import 'package:flutter/material.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    Future<void> main() async {
      await Supabase.initialize(
        url: 'https://<supabase-project>.supabase.co',
        anonKey: 'SUPABASE_PUBLISHABLE_KEY',
        accessToken: () async {
          final session = await Amplify.Auth.fetchAuthSession();
          final cognitoSession = session as CognitoAuthSession;
          return cognitoSession.userPoolTokensResult.value.accessToken.raw;
        },
      );
      runApp(const MyApp());
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    import com.amplifyframework.auth.AuthSession
    import com.amplifyframework.auth.cognito.AWSCognitoAuthSession
    import com.amplifyframework.core.Amplify

    val supabase = createSupabaseClient(
        "https://<supabase-project>.supabase.co",
        "SUPABASE_PUBLISHABLE_KEY"
    ) {
        accessToken = {
            getAccessToken()
        }
    }

    suspend fun getAccessToken(): String? {
        return suspendCoroutine {
            Amplify.Auth.fetchAuthSession(
                { result: AuthSession ->
                    val cognitoAuthSession = result as AWSCognitoAuthSession
                    it.resume(cognitoAuthSession.userPoolTokensResult.value?.accessToken)
                },
                { _ ->
                    // Handle error
                })
        }
    }
    ```
  </TabPanel>
</Tabs>



## Add a new Third-Party Auth integration to your project

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

In the CLI add the following config to your `supabase/config.toml` file:

```toml
[auth.third_party.aws_cognito]
enabled = true
user_pool_id = "<id>"
user_pool_region = "<region>"
```



## Use a pre-token generation trigger to assign the authenticated role

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

By default, Amazon Cognito JWTs (both ID token and access tokens) do not contain a `role` claim in them. If you were to send such a JWT to your Supabase project, the `anon` role would be assigned when executing the Postgres query. Most of your app's logic will be accessible by the `authenticated` role.

A recommended approach to do this is to configure a [Pre-Token Generation Trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) either `V1_0` (ID token only) or `V2_0` (both access and ID token). To do this you will need to create a new Lambda function (in any language and runtime) and assign it to the [Amazon Cognito User Pool's Lambda Triggers configuration](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html). For example, the Lambda function should look similar to this:

<Tabs type="underlined" queryGroup="cognito-lambda">
  <TabPanel id="blocking-nodejs" label="Node.js">
    ```javascript
    export const handler = async (event) => {
      event.response = {
        claimsOverrideDetails: {
          claimsToAddOrOverride: {
            role: 'authenticated',
          },
        },
      }

      return event
    }
    ```
  </TabPanel>
</Tabs>



---
**Navigation:** [← Previous](./28-send-emails-with-custom-smtp.md) | [Index](./index.md) | [Next →](./30-clerk.md)
