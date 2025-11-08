**Navigation:** [← Previous](./29-phone-login.md) | [Index](./index.md) | [Next →](./31-login-with-bitbucket.md)

# Clerk

Use Clerk with your Supabase project

Clerk can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.



## Getting started

Getting started is incredibly easy. Start off by visiting [Clerk's Connect with Supabase page](https://dashboard.clerk.com/setup/supabase) to configure your Clerk instance for Supabase compatibility.

Finally add a [new Third-Party Auth integration with Clerk](/dashboard/project/_/auth/third-party) in the Supabase dashboard.


### Configure for local development or self-hosting

When developing locally or self-hosting with the Supabase CLI, add the following config to your `supabase/config.toml` file:

```toml
[auth.third_party.clerk]
enabled = true
domain = "example.clerk.accounts.dev"
```

You will still need to configure your Clerk instance for Supabase compatibility.


### Manually configuring your Clerk instance

If you are not able to use [Clerk's Connect with Supabase page](https://dashboard.clerk.com/setup/supabase) to configure your Clerk instance for working with Supabase, follow these steps.

1.  Add the `role` claim to [Clerk session tokens](https://clerk.com/docs/backend-requests/resources/session-tokens) by [customizing them](https://clerk.com/docs/backend-requests/custom-session-token). End-users who are authenticated should have the `authenticated` value for the claim. If you have an advanced Postgres setup where authenticated end-users use different Postgres roles to access the database, adjust the value to use the correct role name.
2.  Once all Clerk session tokens for your instance contain the `role` claim, add a [new Third-Party Auth integration with Clerk](/dashboard/project/_/auth/third-party) in the Supabase dashboard or register it in the CLI as instructed above.



## Setup the Supabase client library

<Tabs type="underlined" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    <CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/clerk/hooks/useSupabaseClient.ts">
      ```typescript
      const supabaseClient = createClient(
          process.env.NEXT_PUBLIC_SUPABASE_URL!,
          process.env.NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY!,
          {
            // Session accessed from Clerk SDK, either as Clerk.session (vanilla
            // JavaScript) or useSession (React)
            accessToken: async () => session?.getToken() ?? null,
          }
        )
      ```
    </CodeSampleWrapper>
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    ```dart
    import 'package:clerk_flutter/clerk_flutter.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    ...

    await Supabase.initialize(
      url: 'SUPABASE_URL',
      anonKey: 'SUPABASE_PUBLISHABLE_KEY',
      accessToken: () async {
        final token = await ClerkAuth.of(context).sessionToken();
        return token.jwt;
      },
    );
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift (iOS)">
    ```swift
    import Clerk
    import Supabase

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://project-ref.supabase.io")!,
      supabaseKey: "supabase.anon.key",
      options: SupabaseClientOptions(
        auth: SupabaseClientOptions.AuthOptions(
          accessToken: {
            try await Clerk.shared.session?.getToken()?.jwt
          }
        )
      )
    )
    ```
  </TabPanel>
</Tabs>



## Using RLS policies

Once you've configured the Supabase client library to use Clerk session tokens, you can use RLS policies to secure access to your project's database, Storage objects and Realtime channels.

The recommended way to design RLS policies with Clerk is to use claims present in your Clerk session token to allow or reject access to your project's data. Check [Clerk's docs](https://clerk.com/docs/backend-requests/resources/session-tokens) on the available JWT claims and their values.


### Example: Check user organization role

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/clerk/supabase/migrations/20250501155648_setup_database.sql">
  ```sql
  create policy "Only organization admins can insert in table"
  on secured_table
  for insert
  to authenticated
  with check (
    (((select auth.jwt()->>'org_role') = 'org:admin') or ((select auth.jwt()->'o'->>'rol') = 'admin'))
      and
    (organization_id = (select coalesce(auth.jwt()->>'org_id', auth.jwt()->'o'->>'id')))
  );
  ```
</CodeSampleWrapper>

This RLS policy checks that the newly inserted row in the table has the user's declared organization ID in the `organization_id` column. Additionally it ensures that they're an `org:admin`.

This way only organization admins can add rows to the table, for organizations they're a member of.


### Example: Check user has passed second factor verification

<CodeSampleWrapper source="https://github.com/supabase/supabase/blob/2415776436927dedb360dae082d03caee607891a/examples/clerk/supabase/migrations/20250501155648_setup_database.sql">
  ```sql
  create policy "Only users that have passed second factor verification can read from table"
  on secured_table
  as restrictive
  for select
  to authenticated
  using (
    ((select auth.jwt()->'fva'->>1) != '-1')
  );
  ```
</CodeSampleWrapper>

This example uses a restrictive RLS policy checks that the [second factor verification](https://clerk.com/docs/guides/reverification) age element in the `fva` claim is not `'-1'` indicating the user has passed through second factor verification.



## Deprecated integration with JWT templates

As of 1st April 2025 the previously available [Clerk Integration with Supabase](/partners/integrations/clerk) is considered deprecated and is no longer recommended for use. All projects using the deprecated integration will be excluded from Third-Party Monthly Active User (TP-MAU) charges until at least 1st January 2026.

This integration used low-level primitives that are still available in Supabase and Clerk, such as a [configurable JWT secret](/dashboard/project/_/settings/api) and [JWT templates from Clerk](https://clerk.com/docs/backend-requests/jwt-templates). This enables you to keep using it in an unofficial manner, though only limited support will be provided from Supabase.

Deprecation is done for the following reasons:

*   Sharing your project's JWT secret with a third-party is a problematic security practice
*   Rotating the project's JWT secret in this case almost always results in significant downtime for your application
*   Additional latency to [generate a new JWT](https://clerk.com/docs/backend-requests/jwt-templates#generate-a-jwt) for use with Supabase, instead of using the Clerk [session tokens](https://clerk.com/docs/backend-requests/resources/session-tokens)



# Firebase Auth

Use Firebase Auth with your Supabase project

Firebase Auth can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.



## Getting started

1.  First you need to add an integration to connect your Supabase project with your Firebase project. You will need to get the Project ID in the [Firebase Console](https://console.firebase.google.com/u/0/project/_/settings/general).
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party).
3.  If you are using Third Party Auth when self hosting, create and attach restrictive RLS policies to all tables in your public schema, Storage and Realtime to **prevent unauthorized access from unrelated Firebase projects**.
4.  Assign the `role: 'authenticated'` [custom user claim](https://firebase.google.com/docs/auth/admin/custom-claims) to all your users.
5.  Finally set up the Supabase client in your application.



## Setup the Supabase client library

<Tabs type="underlined" queryGroup="firebase-create-client">
  <TabPanel id="ts" label="TypeScript">
    Creating a client for the Web is as easy as passing the `accessToken` async function. This function should [return the Firebase Auth JWT of the current user](https://firebase.google.com/docs/auth/admin/verify-id-tokens#web) (or null if no such user) is found.

    ```typescript
    import { createClient } from '@supabase/supabase-js'

    const supabase = createClient(
      'https://<supabase-project>.supabase.co',
      'SUPABASE_PUBLISHABLE_KEY',
      {
        accessToken: async () => {
          return (await firebase.auth().currentUser?.getIdToken(/* forceRefresh */ false)) ?? null
        },
      }
    )
    ```

    Make sure the all users in your application have the `role: 'authenticated'` [custom claim](https://firebase.google.com/docs/auth/admin/custom-claims) set. If you're using the `onCreate` Cloud Function to add this custom claim to newly signed up users, you will need to call `getIdToken(/* forceRefresh */ true)` immediately after sign up as the `onCreate` function does not run synchronously.
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    Creating a client for the Web is as easy as passing the `accessToken` async function. This function should [return the Firebase Auth JWT of the current user](https://firebase.google.com/docs/auth/admin/verify-id-tokens) (or null if no such user) is found.

    ```dart
    await Supabase.initialize(
      url: supabaseUrl,
      anonKey: supabaseKey,
      debug: false,
      accessToken: () async {
        final token = await FirebaseAuth.instance.currentUser?.getIdToken();
        return token;
      },
    );
    ```

    Make sure the all users in your application have the `role: 'authenticated'` [custom claim](https://firebase.google.com/docs/auth/admin/custom-claims) set. If you're using the `onCreate` Cloud Function to add this custom claim to newly signed up users, you will need to call `getIdToken(/* forceRefresh */ true)` immediately after sign up as the `onCreate` function does not run synchronously.
  </TabPanel>

  <TabPanel id="swift" label="Swift (iOS)">
    ```swift
    import Supabase
    import FirebaseAuth

    struct MissingFirebaseTokenError: Error {}

    let supabase = SupabaseClient(
      supabaseURL: URL(string: "https://<supabase-project>.supabase.co")!,
      supabaseKey: "SUPABASE_PUBLISHABLE_KEY",
      options: SupabaseClientOptions(
        auth: SupabaseClientOptions.AuthOptions(
          accessToken: {
            guard let token = await Auth.auth().currentUser?.getIDToken() else {
              throw MissingFirebaseTokenError()
            }

            return token
          }
        )
      )
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin (Android)">
    Create a Supabase client with the `accessToken` function that returns the Firebase Auth JWT of the current user. This code uses the [official Firebase SDK](https://firebase.google.com/docs/auth/android/start) for Android.

    ```kotlin
    import com.google.firebase.auth.ktx.auth
    import com.google.firebase.ktx.Firebase

    val supabase = createSupabaseClient(
        "https://<supabase-project>.supabase.co",
        "SUPABASE_PUBLISHABLE_KEY"
    ) {
        accessToken = {
            Firebase.auth.currentUser?.getIdToken(false)?.await()?.token
        }
    }
    ```
  </TabPanel>

  <TabPanel id="kotlinmp" label="Kotlin (Multiplatform)">
    Create a Supabase client with the `accessToken` function that returns the Firebase Auth JWT of the current user. This code uses a [community Firebase SDK](https://github.com/GitLiveApp/firebase-kotlin-sdk) which supports Kotlin Multiplatform.

    ```kotlin
    import dev.gitlive.firebase.Firebase
    import dev.gitlive.firebase.auth.auth

    val supabase = createSupabaseClient(
        "https://<supabase-project>.supabase.co",
        "SUPABASE_PUBLISHABLE_KEY"
    ) {
        accessToken = {
            Firebase.auth.currentUser?.getIdToken(false)
        }
    }
    ```
  </TabPanel>
</Tabs>



## Add a new Third-Party Auth integration to your project

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.

In the CLI add the following config to your `supabase/config.toml` file:

```toml
[auth.third_party.firebase]
enabled = true
project_id = "<id>"
```



## Adding an extra layer of security to your project's RLS policies (self-hosting only)

<Admonition type="caution">
  **Follow this section carefully to prevent unauthorized access to your project's data when self-hosting.**

  When using the Supabase hosted platform, following this step is optional.
</Admonition>

Firebase Auth uses a single set of JWT signing keys for all projects. This means that JWTs issued from an unrelated Firebase project to yours could access data in your Supabase project.

When using the Supabase hosted platform, JWTs coming from Firebase project IDs you have not registered will be rejected before they reach your database. When self-hosting implementing this mechanism is your responsibility. An easy way to guard against this is to create and maintain the following RLS policies for **all of your tables in the `public` schema**. You should also attach this policy to [Storage](/docs/guides/storage/security/access-control) buckets or [Realtime](/docs/guides/realtime/authorization) channels.

It's recommended you use a [restrictive Postgres Row-Level Security policy](https://www.postgresql.org/docs/current/sql-createpolicy.html).

Restrictive RLS policies differ from regular (or permissive) policies in that they use the `as restrictive` clause when being defined. They do not grant permissions, but rather restrict any existing or future permissions. They're great for cases like this where the technical limitations of Firebase Auth remain separate from your app's logic.

<Admonition type="danger">
  Postgres has two types of policies: permissive and restrictive. This example uses restrictive policies so make sure you don't omit the `as restrictive` clause.
</Admonition>

This is an example of such an RLS policy that will restrict access to only your project's (denoted with `<firebase-project-id>`) users, and not any other Firebase project.

```sql
create policy "Restrict access to Supabase Auth and Firebase Auth for project ID <firebase-project-id>"
  on table_name
  as restrictive
  to authenticated
  using (
    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')
    or
    (
        auth.jwt()->>'iss' = 'https://securetoken.google.com/<firebase-project-id>'
        and
        auth.jwt()->>'aud' = '<firebase-project-id>'
     )
  );
```

If you have a lot of tables in your app, or need to manage complex RLS policies for [Storage](/docs/guides/storage) or [Realtime](/docs/guides/realtime) it can be useful to define a [stable Postgres function](https://www.postgresql.org/docs/current/xfunc-volatility.html) that performs the check to cut down on duplicate code. For example:

```sql
create function public.is_supabase_or_firebase_project_jwt()
  returns bool
  language sql
  stable
  returns null on null input
  return (
    (auth.jwt()->>'iss' = 'https://<project-ref>.supabase.co/auth/v1')
    or
    (
        auth.jwt()->>'iss' = concat('https://securetoken.google.com/<firebase-project-id>')
        and
        auth.jwt()->>'aud' = '<firebase-project-id>'
     )
  );
```

Make sure you substitute `<project-ref>` with your Supabase project's ID and the `<firebase-project-id>` to your Firebase Project ID. Then the restrictive policies on all your tables, buckets and channels can be simplified to be:

```sql
create policy "Restrict access to correct Supabase and Firebase projects"
  on table_name
  as restrictive
  to authenticated
  using ((select public.is_supabase_or_firebase_project_jwt()) is true);
```



## Assign the "role" custom claim

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

By default, Firebase JWTs do not contain a `role` claim in them. If you were to send such a JWT to your Supabase project, the `anon` role would be assigned when executing the Postgres query. Most of your app's logic will be accessible by the `authenticated` role.


### Use Firebase Authentication functions to assign the authenticated role

You have two choices to set up a Firebase Authentication function depending on your Firebase project's configuration:

1.  Easiest: Use a [blocking Firebase Authentication function](https://firebase.google.com/docs/auth/extend-with-blocking-functions) but this is only available if your project uses [Firebase Authentication with Identity Platform](https://cloud.google.com/security/products/identity-platform).
2.  Manually assign the custom claims to all users with the [admin SDK](https://firebase.google.com/docs/auth/admin/custom-claims#set_and_validate_custom_user_claims_via_the_admin_sdk) and define an [`onCreate` Firebase Authentication Cloud Function](https://firebase.google.com/docs/auth/extend-with-functions) to persist the role to all newly created users.

<Tabs type="underlined" queryGroup="firebase-functions">
  <TabPanel id="blocking-nodejs" label="Node.js (Blocking Functions Gen 2)">
    ```typescript
    import { beforeUserCreated, beforeUserSignedIn } from 'firebase-functions/v2/identity'

    export const beforecreated = beforeUserCreated((event) => {
      return {
        customClaims: {
          // The Supabase project will use this role to assign the `authenticated`
          // Postgres role.
          role: 'authenticated',
        },
      }
    })

    export const beforesignedin = beforeUserSignedIn((event) => {
      return {
        customClaims: {
          // The Supabase project will use this role to assign the `authenticated`
          // Postgres role.
          role: 'authenticated',
        },
      }
    })
    ```

    Note that instead of using `customClaims` you can instead use `sessionClaims`. The difference is that `session_claims` are not saved in the Firebase user profile, but remain valid for as long as the user is signed in.
  </TabPanel>

  <TabPanel id="blocking-python" label="Python (Blocking Functions Gen 2)">
    ```python
    @identity_fn.before_user_created()
    def set_supabase_role_sign_up(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeCreateResponse | None:
      return identity_fn.BeforeCreateResponse(
        # The Supabase project will use this role to assign the `authenticated`
        # Postgres role.
        custom_claims={'role': 'authenticated'})

    @identity_fn.before_user_signed_in()
    def set_supabase_role_sign_in(event: identity_fn.AuthBlockingEvent) -> identity_fn.BeforeSignInResponse | None:
      return identity_fn.BeforeSignInResponse(
        # The Supabase project will use this role to assign the `authenticated`
        # Postgres role.
        custom_claims={'role': 'authenticated'})
    ```

    Note that instead of using `custom_claims` you can instead use `session_claims`. The difference is that `session_claims` are not saved in the Firebase user profile, but remain valid for as long as the user is signed in.
  </TabPanel>

  <TabPanel id="oncreate-nodejs" label="onCreate Cloud Function in Node.js">
    ```javascript
    const functions = require('firebase-functions')
    const { initializeApp } = require('firebase-admin/app')
    const { getAuth } = require('firebase-admin/auth')
    const { getDatabase } = require('firebase-admin/database')

    initializeApp()

    // On sign up.
    exports.processSignUp = functions.auth.user().onCreate(async (user) => {
      try {
        // Set custom user claims on this newly created user.
        await getAuth().setCustomUserClaims(user.uid, {
          role: 'authenticated',
        })
      } catch (error) {
        console.log(error)
      }
    })
    ```

    Note that the `onCreate` Firebase Cloud Function is not *synchronous* (unlike the Blocking Functions), so the very first ID token received by the Firebase client library in your app *will not contain* the `role: 'authenticated'` claim. Force-refresh the ID token immediately after sign-up to fetch an ID token with the applied role.
  </TabPanel>
</Tabs>

Finally deploy your functions for the changes to take effect:

```
firebase deploy --only functions
```

Note that these functions are only called on new sign-ups and sign-ins. Existing users will not have these claims in their ID tokens. You will need to use the admin SDK to assign the role custom claim to all users. Make sure you do this after the blocking Firebase Authentication functions as described above are deployed.


### Use the admin SDK to assign the role custom claim to all users

You need to run a script that will assign the `role: 'authenticated'` custom claim to all of your existing Firebase Authentication users. You can do this by combining the [list users](https://firebase.google.com/docs/auth/admin/manage-users#list_all_users) and [set custom user claims](https://firebase.google.com/docs/auth/admin/create-custom-tokens) admin APIs. An example script is provided below:

```javascript
'use strict';
const { initializeApp } = require('firebase-admin/app');
const { getAuth } = require('firebase-admin/auth');
initializeApp();

async function setRoleCustomClaim() => {
  let nextPageToken = undefined

  do {
    const listUsersResult = await getAuth().listUsers(1000, nextPageToken)

    nextPageToken = listUsersResult.pageToken

    await Promise.all(listUsersResult.users.map(async (userRecord) => {
      try {
        await getAuth().setCustomUserClaims(userRecord.id, {
          role: 'authenticated'
        })
      } catch (error) {
        console.error('Failed to set custom role for user', userRecord.id)
      }
    })
  } while (nextPageToken);
};

setRoleCustomClaim().then(() => process.exit(0))
```

After all users have received the `role: 'authenticated'` claim, it will appear in all newly issued ID tokens for the user.



# Third-party auth

First-class support for authentication providers

Supabase has first-class support for these third-party authentication providers:

*   [Clerk](/docs/guides/auth/third-party/clerk)
*   [Firebase Auth](/docs/guides/auth/third-party/firebase-auth)
*   [Auth0](/docs/guides/auth/third-party/auth0)
*   [AWS Cognito (with or without AWS Amplify)](/docs/guides/auth/third-party/aws-cognito)
*   [WorkOS](/docs/guides/auth/third-party/workos)

You can use these providers alongside Supabase Auth, or on their own, to access the [Data API (REST and GraphQL)](/docs/guides/database), [Storage](/docs/guides/storage), [Realtime](/docs/guides/storage) and [Functions](/docs/guides/functions) from your existing apps.

If you already have production apps using one of these authentication providers, and would like to use a Supabase feature, you no longer need to migrate your users to Supabase Auth or use workarounds like translating JWTs into the Supabase Auth format and using your project's signing secret.



## How does it work?

To use Supabase products like Data APIs for your Postgres database, Storage or Realtime, you often need to send access tokens or JWTs via the Supabase client libraries or via the REST API. Third-party auth support means that when you add a new integration with one of these providers, the API will trust JWTs issued by the provider similar to how it trusts JWTs issued by Supabase Auth.

This is made possible if the providers are using JWTs signed with asymmetric keys, which means that the Supabase APIs will be able to only verify but not create JWTs.



## Limitations

There are some limitations you should be aware of when using third-party authentication providers with Supabase.

1.  The third-party provider must use asymmetrically signed JWTs (exposed as an OIDC Issuer Discovery URL by the third-party authentication provider). The signed JWTs must have a `kid` header parameter to identify which key must be used. Using symmetrically signed JWTs is not possible at this time.
2.  The JWT signing keys from the third-party provider are stored in the configuration of your project, and are checked for changes periodically. If you are rotating your keys (when supported) allow up to 30 minutes for the change to be picked up.
3.  It is not possible to disable Supabase Auth at this time.



## Pricing

<Price price="0.00325" /> per Third-Party MAU. You are only charged for usage exceeding your subscription
plan's quota.

For a detailed breakdown of how charges are calculated, refer to [Manage Monthly Active Third-Party Users usage](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party).



# WorkOS

Use WorkOS with your Supabase project

WorkOS can be used as a third-party authentication provider alongside Supabase Auth, or standalone, with your Supabase project.



## Getting started

1.  First you need to add an integration to connect your Supabase project with your WorkOS tenant. You will need your WorkOS issuer. The issuer is `https://api.workos.com/user_management/<your-client-id>`. Substitute your [custom auth domain](https://workos.com/docs/custom-domains/auth-api) for "api.workos.com" if configured.
2.  Add a new Third-party Auth integration in your project's [Authentication settings](/dashboard/project/_/auth/third-party).
3.  Set up a JWT template to assign the `role: 'authenticated'` claim to your access token.



## Setup the Supabase client library

<Tabs type="underlined" queryGroup="language">
  <TabPanel id="ts" label="TypeScript">
    ```typescript
    import { createClient } from '@supabase/supabase-js'
    import { createClient as createAuthKitClient } from '@workos-inc/authkit-js'

    const authkit = await createAuthKitClient('WORKOS_CLIENT_ID', {
      apiHostname: '<WORKOS_AUTH_DOMAIN>',
    })

    const supabase = createClient(
      'https://<supabase-project>.supabase.co',
      'SUPABASE_PUBLISHABLE_KEY',
      {
        accessToken: async () => {
          return authkit.getAccessToken()
        },
      }
    )
    ```
  </TabPanel>
</Tabs>



## Add a new Third-Party Auth integration to your project

In the dashboard navigate to your project's [Authentication settings](/dashboard/project/_/auth/third-party) and find the Third-Party Auth section to add a new integration.



## Set up a JWT template to add the authenticated role.

Your Supabase project inspects the `role` claim present in all JWTs sent to it, to assign the correct Postgres role when using the Data API, Storage or Realtime authorization.

WorkOS JWTs already contain a `role` claim that corresponds to the user's role in their organization. It is necessary to adjust the `role` claim to be `"authenticated"` like Supabase expects. This can be done using JWT templates (navigate to Authentication -> Sessions -> JWT Template in the WorkOS Dashboard).

This template overrides the `role` claim to meet Supabase's expectations, and adds the WorkOS role in a new `user_role` claim:

```json
{
  "role": "authenticated",
  "user_role": {{organization_membership.role}}
}
```



# Login with Apple



Supabase Auth supports using [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) on the web and in native apps for iOS, macOS, watchOS or tvOS.



## Overview

To support Sign in with Apple, you need to configure the [Apple provider in the Supabase dashboard](/dashboard/project/_/auth/providers) for your project.

There are three general ways to use Sign in with Apple, depending on the application you're trying to build:

*   Sign in on the web or in web-based apps
    *   Using an OAuth flow initiated by Supabase Auth using the [Sign in with Apple REST API](https://developer.apple.com/documentation/signinwithapplerestapi).
    *   Using [Sign in with Apple JS](https://developer.apple.com/documentation/signinwithapplejs/) directly in the browser, usually suitable for websites.
*   Sign in natively inside iOS, macOS, watchOS or tvOS apps using [Apple's Authentication Services](https://developer.apple.com/documentation/authenticationservices)

In some cases you're able to use the OAuth flow within web-based native apps such as with [React Native](https://reactnative.dev), [Expo](https://expo.dev) or other similar frameworks. It is best practice to use native Sign in with Apple capabilities on those platforms instead.

When developing with Expo, you can test Sign in with Apple via the Expo Go app, in all other cases you will need to obtain an [Apple Developer](https://developer.apple.com) account to enable the capability.

<Admonition type="caution" label="Secret Key Rotation Required">
  If you're using the OAuth flow (web, Flutter web, Kotlin non-iOS platforms), Apple requires you to generate a new secret key every 6 months using the signing key (`.p8` file). This is a critical maintenance task that will cause authentication failures if missed.

  *   Set a recurring calendar reminder for every 6 months to rotate your secret key
  *   Store the `.p8` file securely - you'll need it for each rotation
  *   If you lose the `.p8` file or it's compromised, immediately revoke it in the Apple Developer Console and create a new one
  *   Consider automating this process if possible to prevent service disruptions

  This requirement only applies if you're configuring OAuth settings (Services ID, signing key, etc.). Native-only implementations don't require secret key rotation.
</Admonition>

<Admonition type="caution" label="Apple Does Not Provide Full Name in Identity Token">
  Apple's identity token does not include the user's full name in its claims. This means the Supabase Auth server cannot automatically populate the user's name metadata when users sign in with Apple.

  *   Apple only provides the user's full name during the **first sign-in attempt** (when the user initially authorizes your app)
  *   All subsequent sign-ins return `null` for the full name fields
  *   The full name must be captured from Apple's native authentication response and manually saved using the `updateUser` method

  **Recommended Approach:**
  After a successful Sign in with Apple, check if the full name is available in the authentication response, and if so, use the `updateUser` method to save it to the user's metadata:

  ```typescript
  // Example: Handling full name after successful sign in
  if (credential.fullName) {
    // Full name is only provided on first sign-in
    await supabase.auth.updateUser({
      data: {
        full_name: `${credential.fullName.givenName} ${credential.fullName.familyName}`,
        given_name: credential.fullName.givenName,
        family_name: credential.fullName.familyName,
      },
    })
  }
  ```

  If a user revokes your app's access and then re-authorizes it, Apple will provide the full name again as if it were a first sign-in.

  The platform-specific examples below demonstrate how to implement this pattern for each SDK.
</Admonition>

<Tabs scrollable size="large" type="underlined" defaultActiveId="web" queryGroup="platform">
  <TabPanel id="web" label="Web">
    ## Using the OAuth flow for web

    Sign in with Apple's OAuth flow is designed for web or browser based sign in methods. It can be used on web-based apps as well as websites, though some users can benefit by using Sign in with Apple JS directly.

    Behind the scenes, Supabase Auth uses the [REST APIs](https://developer.apple.com/documentation/signinwithapplerestapi) provided by Apple.

    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    To initiate sign in, you can use the `signInWithOAuth()` method from the Supabase JavaScript library:

    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    supabase.auth.signInWithOAuth({
      provider: 'apple',
    })
    ```

    This call takes the user to Apple's consent screen. Once the flow ends, the user's profile information is exchanged and validated with Supabase Auth before it redirects back to your web application with an access and refresh token representing the user's session.

    <Admonition type="note" label="Full Name Not Available in OAuth Flow">
      When using the OAuth flow, the user's full name is not accessible from Apple's response. Apple only provides the full name through native authentication methods (Sign in with Apple JS, or native iOS/macOS SDKs) during the first sign-in.

      If you need to collect user names, consider:

      *   Using Sign in with Apple JS instead (see below)
      *   Collecting the name through a separate onboarding form
      *   Using a profiles table to store user information
    </Admonition>

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

    ### Configuration \[#configuration-web-oauth]

    You will require the following information:

    1.  Your Apple Developer account's **Team ID**, which is an alphanumeric string of 10 characters that uniquely identifies the developer of the app. It's often accessible in the upper right-side menu on the Apple Developer Console.
    2.  Register email sources for *Sign in with Apple for Email Communication* which can be found in the [Services](https://developer.apple.com/account/resources/services/list) section of the Apple Developer Console. This enables Apple to send relay emails through your domain when users choose to hide their email addresses.
    3.  An **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple once you create an App ID in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    4.  A **Services ID** which uniquely identifies the web services provided by the app you registered in the previous step. You can create a new Services ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/serviceId) section in the Apple Developer Console (use the filter menu in the upper right side to see all Services IDs). These usually are a reverse domain name string, for example `com.example.app.web`.
    5.  Configure Website URLs for the newly created **Services ID**. The web domain you should use is the domain your Supabase project is hosted on. This is usually `<project-id>.supabase.co` while the redirect URL is `https://<project-id>.supabase.co/auth/v1/callback`.
    6.  Create a signing **Key** in the [Keys](https://developer.apple.com/account/resources/authkeys/list) section of the Apple Developer Console. You can use this key to generate a secret key using the tool below, which is added to your Supabase project's Auth configuration. Make sure you safely store the `AuthKey_XXXXXXXXXX.p8` file. If you ever lose access to it, or make it public accidentally, revoke it from the Apple Developer Console and create a new one immediately.
    7.  Finally, add the information you configured above to the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers).

    You can also configure the Apple auth provider using the Management API:

    ```bash
    # Get your access token from https://supabase.com/dashboard/account/tokens
    export SUPABASE_ACCESS_TOKEN="your-access-token"
    export PROJECT_REF="your-project-ref"

    # Configure Apple auth provider
    curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
      -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "external_apple_enabled": true,
        "external_apple_client_id": "your-services-id",
        "external_apple_secret": "your-generated-secret-key"
      }'
    ```

    <Admonition type="tip">
      Use this tool to generate a new Apple client secret. No keys leave your browser! Be aware that this tool does not currently work in Safari, so use Firefox or a Chrome-based browser instead.
    </Admonition>

    <AppleSecretGenerator />

    ## Using sign in with Apple JS

    [Sign in with Apple JS](https://developer.apple.com/documentation/signinwithapplejs/) is an official Apple framework for authenticating Apple users on websites. Although it can be used in web-based apps, those use cases will benefit more with the OAuth flow described above. We recommend using this method on classic websites only.

    You can use the `signInWithIdToken()` method from the Supabase JavaScript library on the website to obtain an access and refresh token once the user has given consent using Sign in with Apple JS:

    ```ts
    async function signIn() {
      try {
        // Generate a nonce for security
        const nonce = crypto.randomUUID() // or use your preferred nonce generation method

        const data = await AppleID.auth.signIn()

        const { data: authData, error } = await supabase.auth.signInWithIdToken({
          provider: 'apple',
          token: data.id_token,
          nonce: nonce,
        })

        if (error) {
          throw error
        }

        // Apple only provides the user's name on the first sign-in
        // The user object contains name information from Apple's response
        if (data.user && data.user.name) {
          const fullName = [
            data.user.name.firstName,
            data.user.name.middleName,
            data.user.name.lastName
          ].filter(Boolean).join(' ')

          // Save the name to user metadata for future use
          await supabase.auth.updateUser({
            data: {
              full_name: fullName,
              given_name: data.user.name.firstName,
              family_name: data.user.name.lastName,
            }
          })
        }
      } catch (error) {
        console.error('Apple sign in failed:', error)
        // Handle sign-in errors appropriately
      }
    }
    ```

    Alternatively, you can use the `AppleIDSignInOnSuccess` event with the `usePopup` option:

    ```ts
    // Generate and store nonce for verification
    const nonce = crypto.randomUUID()

    // Initialize Apple ID with nonce
    AppleID.auth.init({
      clientId: 'your-services-id',
      scope: 'name email',
      redirectURI: 'https://your-domain.com/auth/callback',
      usePopup: true,
      nonce: nonce,
    })

    // Listen for authorization success
    document.addEventListener('AppleIDSignInOnSuccess', async (event) => {
      try {
        const { data: authData, error } = await supabase.auth.signInWithIdToken({
          provider: 'apple',
          token: event.detail.authorization.id_token,
          nonce: nonce,
        })

        if (error) {
          throw error
        }

        // Apple only provides the user's name on the first sign-in
        if (event.detail.user && event.detail.user.name) {
          const fullName = [
            event.detail.user.name.firstName,
            event.detail.user.name.middleName,
            event.detail.user.name.lastName
          ].filter(Boolean).join(' ')

          // Save the name to user metadata for future use
          await supabase.auth.updateUser({
            data: {
              full_name: fullName,
              given_name: event.detail.user.name.firstName,
              family_name: event.detail.user.name.lastName,
            }
          })
        }
      } catch (error) {
        console.error('Apple sign in failed:', error)
      }
    })
    ```

    Make sure you request the scope `name email` when initializing the library, as shown in the example above.

    ### Configuration \[#configuration-web-apple-js]

    To use Sign in with Apple JS you need to configure these options:

    1.  Have an **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple for the App ID you created or already have, in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    2.  Obtain a **Services ID** attached to the App ID that uniquely identifies the website. Use this value as the client ID when initializing Sign in with Apple JS. You can create a new Services ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/serviceId) section in the Apple Developer Console (use the filter menu in the upper right side to see all Services IDs). These usually are a reverse domain name string, for example `com.example.app.website`.
    3.  Configure Website URLs for the newly created **Services ID**. The web domain you should use is the domain your website is hosted on. The redirect URL must also point to a page on your website that will receive the callback from Apple.
    4.  Register the Services ID you created to your project's [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers) under *Client IDs*.

    <Admonition type="note">
      If you're using Sign in with Apple JS you do not need to configure the OAuth settings.
    </Admonition>
  </TabPanel>

  <TabPanel id="react-native" label="Expo React Native">
    ## Using native sign in with Apple in Expo

    When working with Expo, you can use the [Expo AppleAuthentication](https://docs.expo.dev/versions/latest/sdk/apple-authentication/) library to obtain an ID token that you can pass to supabase-js [`signInWithIdToken` method](/docs/reference/javascript/auth-signinwithidtoken).

    Follow the [Expo docs](https://docs.expo.dev/versions/latest/sdk/apple-authentication/#installation) for installation and configuration instructions. See the [supabase-js reference](/docs/reference/javascript/initializing?example=react-native-options-async-storage) for instructions on initializing the supabase-js client in React Native.

    <NamedCodeBlock name="./components/Auth.native.tsx">
      ```tsx name=./components/Auth.native.tsx
      import { Platform } from 'react-native'
      import * as AppleAuthentication from 'expo-apple-authentication'
      import { supabase } from 'app/utils/supabase'

      export function Auth() {
        if (Platform.OS === 'ios')
          return (
            <AppleAuthentication.AppleAuthenticationButton
              buttonType={AppleAuthentication.AppleAuthenticationButtonType.SIGN_IN}
              buttonStyle={AppleAuthentication.AppleAuthenticationButtonStyle.BLACK}
              cornerRadius={5}
              style={{ width: 200, height: 64 }}
              onPress={async () => {
                try {
                  const credential = await AppleAuthentication.signInAsync({
                    requestedScopes: [
                      AppleAuthentication.AppleAuthenticationScope.FULL_NAME,
                      AppleAuthentication.AppleAuthenticationScope.EMAIL,
                    ],
                  })
                  // Sign in via Supabase Auth.
                  if (credential.identityToken) {
                    const {
                      error,
                      data: { user },
                    } = await supabase.auth.signInWithIdToken({
                      provider: 'apple',
                      token: credential.identityToken,
                    })
                    console.log(JSON.stringify({ error, user }, null, 2))
                    if (!error) {
                      // Apple only provides the user's full name on the first sign-in
                      // Save it to user metadata if available
                      if (credential.fullName) {
                        const nameParts = []
                        if (credential.fullName.givenName) nameParts.push(credential.fullName.givenName)
                        if (credential.fullName.middleName) nameParts.push(credential.fullName.middleName)
                        if (credential.fullName.familyName) nameParts.push(credential.fullName.familyName)

                        const fullName = nameParts.join(' ')

                        await supabase.auth.updateUser({
                          data: {
                            full_name: fullName,
                            given_name: credential.fullName.givenName,
                            family_name: credential.fullName.familyName,
                          }
                        })
                      }
                      // User is signed in.
                    }
                  } else {
                    throw new Error('No identityToken.')
                  }
                } catch (e) {
                  if (e.code === 'ERR_REQUEST_CANCELED') {
                    // handle that the user canceled the sign-in flow
                  } else {
                    // handle other errors
                  }
                }
              }}
            />
          )
        return (
          <>
            {/*
              On Android, Sign in with Apple is not natively supported.
              You have two options:
              1. Use the OAuth flow via signInWithOAuth (see Flutter Android example below)
              2. Use a web-based solution like react-native-app-auth

              For most cases, we recommend using the OAuth flow:
            */}
            <Button
              onPress={async () => {
                const { error } = await supabase.auth.signInWithOAuth({
                  provider: 'apple',
                  options: {
                    redirectTo: 'your-app-scheme://auth/callback',
                    skipBrowserRedirect: false,
                  },
                })
                if (error) {
                  console.error('Sign in error:', error)
                }
              }}
            >
              Sign in with Apple
            </Button>
          </>
        )
      }
      ```
    </NamedCodeBlock>

    <Admonition type="note" label="Android Implementation Notes">
      *   Sign in with Apple is not natively available on Android devices
      *   The OAuth flow opens a browser window for authentication
      *   You must configure [deep linking](/docs/guides/auth/native-mobile-deep-linking) for the callback to work properly
      *   The OAuth configuration (Services ID, etc.) must be set up as described in the [Web OAuth Configuration section](#configuration-web-oauth)
    </Admonition>

    When working with bare React Native, you can use [invertase/react-native-apple-authentication](https://github.com/invertase/react-native-apple-authentication) to obtain the ID token on iOS. For Android, use the OAuth flow as shown above.

    ### Configuration \[#configuration-expo-native]

    <Admonition type="note">
      When testing with Expo Go, the Expo App ID `host.exp.Exponent` will be used. Make sure to add this to the "Client IDs" list in your [Supabase dashboard Apple provider configuration](/dashboard/project/_/auth/providers)!
    </Admonition>

    <Admonition type="note">
      When testing with Expo development build with custom `bundleIdentifier`, for example com.example.app , com.example.app.dev , com.example.app.preview. Make sure to add all these variants to the "Client IDs" list in your [Supabase dashboard Apple provider configuration](/dashboard/project/_/auth/providers)!
    </Admonition>

    1.  Have an **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple for the App ID you created or already have, in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    2.  Register all of the App IDs that will be using your Supabase project in the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers) under *Client IDs*.

    <Admonition type="note">
      If you're building a native app only, you do not need to configure the OAuth settings.
    </Admonition>
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    ## Sign in with Apple on iOS and macOS

    You can perform Sign in with Apple using the [sign\_in\_with\_apple](https://pub.dev/packages/sign_in_with_apple) package on Flutter apps running on iOS or macOS.
    Follow the instructions in the package README to set up native Sign in with Apple on iOS and macOS.

    Once the setup is complete on the Flutter app, add the bundle ID of your app to your Supabase dashboard in `Authentication -> Providers -> Apple` in order to register your app with Supabase.

    ```dart
    import 'package:sign_in_with_apple/sign_in_with_apple.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';
    import 'package:crypto/crypto.dart';

    /// Performs Apple sign in on iOS or macOS
    Future<AuthResponse> signInWithApple() async {
      final rawNonce = supabase.auth.generateRawNonce();
      final hashedNonce = sha256.convert(utf8.encode(rawNonce)).toString();

      final credential = await SignInWithApple.getAppleIDCredential(
        scopes: [
          AppleIDAuthorizationScopes.email,
          AppleIDAuthorizationScopes.fullName,
        ],
        nonce: hashedNonce,
      );

      final idToken = credential.identityToken;
      if (idToken == null) {
        throw const AuthException(
            'Could not find ID Token from generated credential.');
      }

      final authResponse = await supabase.auth.signInWithIdToken(
        provider: OAuthProvider.apple,
        idToken: idToken,
        nonce: rawNonce,
      );

      // Apple only provides the user's full name on the first sign-in
      // Save it to user metadata if available
      if (credential.givenName != null || credential.familyName != null) {
        final nameParts = <String>[];
        if (credential.givenName != null) nameParts.add(credential.givenName!);
        if (credential.familyName != null) nameParts.add(credential.familyName!);

        final fullName = nameParts.join(' ');

        await supabase.auth.updateUser(
          UserAttributes(
            data: {
              'full_name': fullName,
              'given_name': credential.givenName,
              'family_name': credential.familyName,
            },
          ),
        );
      }

      return authResponse;
    }
    ```

    ### Configuration \[#configuration-flutter-native]

    1.  Have an **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple for the App ID you created or already have, in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    2.  Register all of the App IDs that will be using your Supabase project in the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers) under *Client IDs*.

    ## Sign in with Apple on Android, Web, Windows and Linux

    For platforms that don't support native Sign in with Apple, you can use the `signInWithOAuth()` method to perform Sign in with Apple.

    <Admonition type="note">
      Do **NOT** follow the Android or Web setup instructions on [sign\_in\_with\_apple](https://pub.dev/packages/sign_in_with_apple) package README for these platforms.　sign\_in\_with\_apple package is not used for performing Apple sign-in on non-Apple platforms for Supabase.
    </Admonition>

    This method of signing in is web based, and will open a browser window to perform the sign in. For non-web platforms, the user is brought back to the app via [deep linking](/docs/guides/auth/native-mobile-deep-linking?platform=flutter).

    ```dart
    await supabase.auth.signInWithOAuth(
      OAuthProvider.apple,
      redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
      authScreenLaunchMode:
          kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
    );
    ```

    This call takes the user to Apple's consent screen. Once the flow ends, the user's profile information is exchanged and validated with Supabase Auth before it redirects back to your Flutter application with an access and refresh token representing the user's session.

    ### Configuration \[#configuration-flutter-web]

    You will require the following information:

    1.  Your Apple Developer account's **Team ID**, which is an alphanumeric string of 10 characters that uniquely identifies the developer of the app. It's often accessible in the upper right-side menu on the Apple Developer Console.
    2.  Register email sources for *Sign in with Apple for Email Communication* which can be found in the [Services](https://developer.apple.com/account/resources/services/list) section of the Apple Developer Console.
    3.  An **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple once you create an App ID in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    4.  A **Services ID** which uniquely identifies the web services provided by the app you registered in the previous step. You can create a new Services ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/serviceId) section in the Apple Developer Console (use the filter menu in the upper right side to see all Services IDs). These usually are a reverse domain name string, for example `com.example.app.web`.
    5.  Configure Website URLs for the newly created **Services ID**. The web domain you should use is the domain your Supabase project is hosted on. This is usually `<project-id>.supabase.co` while the redirect URL is `https://<project-id>.supabase.co/auth/v1/callback`.
    6.  Create a signing **Key** in the [Keys](https://developer.apple.com/account/resources/authkeys/list) section of the Apple Developer Console. You can use this key to generate a secret key using the tool below, which is added to your Supabase project's Auth configuration. Make sure you safely store the `AuthKey_XXXXXXXXXX.p8` file. If you ever lose access to it, or make it public accidentally, revoke it from the Apple Developer Console and create a new one immediately. You will have to generate a new secret key using this file every 6 months, so make sure you schedule a recurring reminder in your calendar!
    7.  Finally, add the information you configured above to the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers).

    <Admonition type="tip">
      Use this tool to generate a new Apple client secret. No keys leave your browser! Be aware that this tool does not currently work in Safari, so use Firefox or a Chrome-based browser instead.
    </Admonition>

    <AppleSecretGenerator />
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ## Using native sign in with Apple in Swift

    For apps written in Swift, follow the [Apple Developer docs](https://developer.apple.com/documentation/sign_in_with_apple/implementing_user_authentication_with_sign_in_with_apple) for obtaining the ID token and then pass it to the [Swift client's `signInWithIdToken`](https://github.com/supabase-community/gotrue-swift/blob/main/Examples/Shared/Sources/SignInWithAppleView.swift#L36) method.

    ```swift
    import SwiftUI
    import AuthenticationServices
    import Supabase

    struct SignInView: View {
        let client = SupabaseClient(supabaseURL: URL(string: "your url")!, supabaseKey: "your anon key")

        var body: some View {
          SignInWithAppleButton { request in
            request.requestedScopes = [.email, .fullName]
          } onCompletion: { result in
            Task {
              do {
                guard let credential = try result.get().credential as? ASAuthorizationAppleIDCredential
                else {
                  return
                }

                guard let idToken = credential.identityToken
                  .flatMap({ String(data: $0, encoding: .utf8) })
                else {
                  return
                }

                try await client.auth.signInWithIdToken(
                  credentials: .init(
                    provider: .apple,
                    idToken: idToken
                  )
                )

                // Apple only provides the user's full name on the first sign-in
                // Save it to user metadata if available
                if let fullName = credential.fullName {
                  var nameParts: [String] = []
                  if let givenName = fullName.givenName {
                    nameParts.append(givenName)
                  }
                  if let middleName = fullName.middleName {
                    nameParts.append(middleName)
                  }
                  if let familyName = fullName.familyName {
                    nameParts.append(familyName)
                  }

                  let fullNameString = nameParts.joined(separator: " ")

                  try await client.auth.update(
                    user: UserAttributes(
                      data: [
                        "full_name": .string(fullNameString),
                        "given_name": .string(fullName.givenName ?? ""),
                        "family_name": .string(fullName.familyName ?? "")
                      ]
                    )
                  )
                }

                // User successfully signed in
                print("Sign in with Apple successful!")
              } catch {
                // Handle sign-in errors
                print("Sign in with Apple failed: \(error.localizedDescription)")
                // Show error alert to user
              }
            }
          }
          .fixedSize()
        }
    }
    ```

    ### Configuration \[#configuration-swift-native]

    1.  Have an **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple for the App ID you created or already have, in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank. (In the past App IDs were referred to as *bundle IDs.*)
    2.  Register all of the App IDs that will be using your Supabase project in the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers) under *Client IDs*.

    <Admonition type="note">
      If you're building a native app only, you do not need to configure the OAuth settings.
    </Admonition>
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ## Using native sign in with Apple in Kotlin

    When using [Compose Multiplatform](https://github.com/JetBrains/compose-multiplatform/), you can use the [compose-auth](/docs/reference/kotlin/installing) plugin. On iOS it uses Native Apple Login automatically and on other platforms it uses `gotrue.signInWith(Apple)`.

    **Initialize the Supabase Client**

    ```kotlin
    val supabaseClient = createSupabaseClient(
    	supabaseUrl = "SUPABASE_URL",
    	supabaseKey = "SUPABASE_KEY"
    ) {
    	install(GoTrue)
    	install(ComposeAuth) {
    		appleNativeLogin()
    	}
    }
    ```

    **Use the Compose Auth plugin in your Auth Screen**

    ```kotlin
    val authState = supabaseClient.composeAuth.rememberLoginWithApple(
    	onResult = { result ->
    		when(result) {
    			NativeSignInResult.ClosedByUser -> {
    				// User cancelled the sign-in flow
    				println("User cancelled Apple sign in")
    			}
    			is NativeSignInResult.Error -> {
    				// An error occurred during sign in
    				println("Apple sign in error: ${result.message}")
    				// Show error to user
    			}
    			is NativeSignInResult.NetworkError -> {
    				// Network error occurred
    				println("Network error during Apple sign in: ${result.error}")
    				// Show network error to user
    			}
    			is NativeSignInResult.Success -> {
    				// User successfully signed in
    				println("Apple sign in successful!")

    				// Apple only provides the user's full name on the first sign-in (iOS only)
    				// Save it to user metadata if available
    				result.data?.let { appleData ->
    					appleData.fullName?.let { fullName ->
    						val nameParts = mutableListOf<String>()
    						fullName.givenName?.let { nameParts.add(it) }
    						fullName.middleName?.let { nameParts.add(it) }
    						fullName.familyName?.let { nameParts.add(it) }

    						val fullNameString = nameParts.joinToString(" ")

    						scope.launch {
    							try {
    								supabaseClient.auth.updateUser {
    									data = buildJsonObject {
    										put("full_name", fullNameString)
    										fullName.givenName?.let { put("given_name", it) }
    										fullName.familyName?.let { put("family_name", it) }
    									}
    								}
    							} catch (e: Exception) {
    								println("Failed to update user metadata: ${e.message}")
    							}
    						}
    					}
    				}

    				// Navigate to home screen or update UI
    			}
    		}
    	}
    )

    Button(onClick = { authState.startFlow() }) {
    	Text("Sign in with Apple")
    }
    ```

    ### Configuration \[#configuration-kotlin]

    **For iOS (native Sign in with Apple):**

    1.  Have an **App ID** which uniquely identifies the app you are building. You can create a new App ID from the [Identifiers](https://developer.apple.com/account/resources/identifiers/list/bundleId) section in the Apple Developer Console (use the filter menu in the upper right side to see all App IDs). These usually are a reverse domain name string, for example `com.example.app`. Make sure you configure Sign in with Apple for the App ID you created or already have, in the Capabilities list. At this time Supabase Auth does not support Server-to-Server notification endpoints, so you should leave that setting blank.
    2.  Register all of the App IDs that will be using your Supabase project in the [Apple provider configuration in the Supabase dashboard](/dashboard/project/_/auth/providers) under *Client IDs*.

    **For other platforms (Android, Desktop, Web):**

    On non-iOS platforms, ComposeAuth automatically falls back to the OAuth flow. You need to configure the OAuth settings as described in the [Web OAuth Configuration section](#configuration-web-oauth) above, including:

    *   Team ID
    *   Email sources registration
    *   Services ID
    *   Signing Key and secret generation

    **Dependencies:**

    Add the following to your `build.gradle.kts`:

    ```kotlin
    dependencies {
        implementation("io.github.jan-tennert.supabase:gotrue-kt:VERSION")
        implementation("io.github.jan-tennert.supabase:compose-auth:VERSION")
        implementation("io.github.jan-tennert.supabase:compose-auth-ui:VERSION") // Optional, for UI components
    }
    ```

    <Admonition type="note">
      **Platform-Specific Notes**

      *   **iOS**: Uses native Apple Authentication Services automatically
      *   **Android/Desktop/Web**: Falls back to OAuth flow (requires web OAuth configuration)
      *   **Minimum Versions**: Kotlin 1.9.0+, Compose Multiplatform 1.5.0+
    </Admonition>
  </TabPanel>
</Tabs>



# Login with Azure (Microsoft)



To enable Azure (Microsoft) Auth for your project, you need to set up an Azure OAuth application and add the application credentials to your Supabase Dashboard.



## Overview

Setting up OAuth with Azure consists of four broad steps:

*   Create an OAuth application under Azure Entra ID.
*   Add a secret to the application.
*   Add the Supabase Auth callback URL to the allowlist in the OAuth application in Azure.
*   Configure the client ID and secret of the OAuth application within the Supabase Auth dashboard.



## Access your Azure Developer account

*   Go to [portal.azure.com](https://portal.azure.com/#home).
*   Login and select Microsoft Entra ID under the list of Azure Services.



## Register an application

*   Under Microsoft Entra ID, select *App registrations* in the side panel and select *New registration.*
*   Choose a name and select your preferred option for the supported account types.
*   Specify a *Web* *Redirect URI*. It should look like this: `https://<project-ref>.supabase.co/auth/v1/callback`
*   Finally, select *Register* at the bottom of the screen.

![Register an application.](/docs/img/guides/auth-azure/azure-register-app.png)



## Obtain a client ID and secret

*   Once your app has been registered, the client ID can be found under the [list of app registrations](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps) under the column titled *Application (client) ID*.
*   You can also find it in the app overview screen.
*   Place the Client ID in the Azure configuration screen in the Supabase Auth dashboard.

![Obtain the client ID](/docs/img/guides/auth-azure/azure-client-id.png)

*   Select *Add a certificate or secret* in the app overview screen and open the *Client secrets* tab.
*   Select *New client secret* to create a new client secret.
*   Choose a preferred expiry time of the secret. Make sure you record this in your calendar days in advance so you have enough time to create a new one without suffering from any downtime.
*   Once the secret is generated place the *Value* column (not *Secret ID*) in the Azure configuration screen in the Supabase Auth dashboard.

![Obtain the client secret](/docs/img/guides/auth-azure/azure-client-secret.png)

You can also configure the Azure auth provider using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Configure Azure auth provider
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "external_azure_enabled": true,
    "external_azure_client_id": "your-azure-client-id",
    "external_azure_secret": "your-azure-client-secret",
    "external_azure_url": "your-azure-url"
  }'
```



## Guarding against unverified email domains

Microsoft Entra ID can send out unverified email domains in certain cases. This may open up your project to a vulnerability where a malicious user can impersonate already existing accounts on your project.

This only applies in at least one of these cases:

*   You have configured the `authenticationBehaviors` setting of your OAuth application to allow unverified email domains
*   You are using an OAuth app configured as single-tenant in the supported account types
*   Your OAuth app was created before June 20th 2023 after Microsoft announced this vulnerability, and the app had used unverified emails prior

This means that most OAuth apps *are not susceptible* to this vulnerability.

Despite this, we recommend configuring the [optional `xms_edov` claim](https://learn.microsoft.com/en-us/azure/active-directory/develop/migrate-off-email-claim-authorization#using-the-xms_edov-optional-claim-to-determine-email-verification-status-and-migrate-users) on the OAuth app. This claim allows Supabase Auth to identify with certainty whether the email address sent over by Microsoft Entra ID is verified or not.

Configure this in the following way:

*   Select the *App registrations* menu in Microsoft Entra ID on the Azure portal.
*   Select the OAuth app.
*   Select the *Manifest* menu in the sidebar.
*   Make a backup of the JSON just in case.
*   Identify the `optionalClaims` key.
*   Edit it by specifying the following object:
    ```json
      "optionalClaims": {
          "idToken": [
              {
                  "name": "xms_edov",
                  "source": null,
                  "essential": false,
                  "additionalProperties": []
              },
              {
                  "name": "email",
                  "source": null,
                  "essential": false,
                  "additionalProperties": []
              }
          ],
          "accessToken": [
              {
                  "name": "xms_edov",
                  "source": null,
                  "essential": false,
                  "additionalProperties": []
              }
          ],
          "saml2Token": []
      },
    ```
*   Select *Save* to apply the new configuration.



## Configure a tenant URL (optional)

A Microsoft Entra tenant is the directory of users who are allowed to access your project. This section depends on what your OAuth registration uses for *Supported account types.*

By default, Supabase Auth uses the *common* Microsoft tenant (`https://login.microsoftonline.com/common`) which generally allows any Microsoft account to sign in to your project. Microsoft Entra further limits what accounts can access your project depending on the type of OAuth application you registered.

If your app is registered as *Personal Microsoft accounts only* for the *Supported account types* set Microsoft tenant to *consumers* (`https://login.microsoftonline.com/consumers`).

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

If your app is registered as *My organization only* for the *Supported account types* you may want to configure Supabase Auth with the organization's tenant URL. This will use the tenant's authorization flows instead, and will limit access at the Supabase Auth level to Microsoft accounts arising from only the specified tenant.

Configure this by storing a value under *Azure Tenant URL* in the Supabase Auth provider configuration page for Azure that has the following format `https://login.microsoftonline.com/<tenant-id>`.



## Add login code to your client app

<Admonition type="tip">
  Supabase Auth requires that Azure returns a valid email address. Therefore you must request the `email` scope in the `signInWithOAuth` method.
</Admonition>

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    <Admonition type="tip">
      Make sure you're using the right `supabase` client in the following code.

      If you're not using Server-Side Rendering or cookie-based Auth, you can directly use the `createClient` from `@supabase/supabase-js`. If you're using Server-Side Rendering, see the [Server-Side Auth guide](/docs/guides/auth/server-side/creating-a-client) for instructions on creating your Supabase client.
    </Admonition>

    When your user signs in, call [`signInWithOAuth()`](/docs/reference/javascript/auth-signinwithoauth) with `azure` as the `provider`:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    async function signInWithAzure() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'azure',
        options: {
          scopes: 'email',
        },
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    When your user signs in, call [`signInWithOAuth()`](/docs/reference/dart/auth-signinwithoauth) with `azure` as the `provider`:

    ```dart
    Future<void> signInWithAzure() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.azure,
        redirectTo: kIsWeb ? null : 'my.scheme://my-host', // Optionally set the redirect link to bring back the user via deeplink.
        authScreenLaunchMode:
            kIsWeb ? LaunchMode.platformDefault : LaunchMode.externalApplication, // Launch the auth screen in a new webview on mobile.
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs in, call [signInWith(Provider)](/docs/reference/kotlin/auth-signinwithoauth) with `Azure` as the `Provider`:

    ```kotlin
    suspend fun signInWithAzure() {
        supabase.auth.signInWith(Azure) {
            scopes.add("email")
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

  <TabPanel id="kotlin" label="Kotlin">
    When your user signs out, call [signOut()](/docs/reference/kotlin/auth-signout) to remove them from the browser session and any objects from localStorage:

    ```kotlin
    suspend fun signOut() {
    	supabase.auth.signOut()
    }
    ```
  </TabPanel>
</Tabs>



## Obtain the provider refresh token

Azure OAuth2.0 doesn't return the `provider_refresh_token` by default. If you need the `provider_refresh_token` returned, you will need to include the following scope:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    async function signInWithAzure() {
      const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'azure',
        options: {
          scopes: 'offline_access',
        },
      })
    }
    ```
  </TabPanel>

  <TabPanel id="flutter" label="Flutter">
    ```dart
    Future<void> signInWithAzure() async {
      await supabase.auth.signInWithOAuth(
        OAuthProvider.azure,
        scopes: 'offline_access',
      );
    }
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    suspend fun signInWithAzure() {
        supabase.auth.signInWith(Azure) {
            scopes.add("offline_access")
        }
    }
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Azure Developer Account](https://portal.azure.com)
*   [GitHub Discussion](https://github.com/supabase/gotrue/pull/54#issuecomment-757043573)
*   [Potential Risk of Privilege Escalation in Azure AD Applications](https://msrc.microsoft.com/blog/2023/06/potential-risk-of-privilege-escalation-in-azure-ad-applications/)



---
**Navigation:** [← Previous](./29-phone-login.md) | [Index](./index.md) | [Next →](./31-login-with-bitbucket.md)
