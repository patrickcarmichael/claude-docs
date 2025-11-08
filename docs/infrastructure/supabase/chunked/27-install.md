**Navigation:** [← Previous](./26-pg_stat_statements-query-performance-monitoring.md) | [Index](./index.md) | [Next →](./28-send-emails-with-custom-smtp.md)

# Install



Install the Supabase Cron Postgres Module to begin scheduling recurring Jobs.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Cron Postgres Module](/dashboard/project/_/integrations/cron/overview) under Integrations in the Dashboard.
    2.  Enable the `pg_cron` extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create extension pg_cron with schema pg_catalog;

    grant usage on schema cron to postgres;
    grant all privileges on all tables in schema cron to postgres;
    ```
  </TabPanel>
</Tabs>



## Uninstall

Uninstall Supabase Cron by disabling the `pg_cron` extension:

```sql
drop extension if exists pg_cron;
```

<Admonition type="danger">
  Disabling the `pg_cron` extension will permanently delete all Jobs.
</Admonition>



# Quickstart



<Admonition type="note">
  Job names are case sensitive and cannot be edited once created.

  Attempting to create a second Job with the same name (and case) will overwrite the first Job.
</Admonition>



## Schedule a job

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard-schedule-job" queryGroup="database-method">
  <TabPanel id="dashboard-schedule-job" label="Dashboard">
    1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section to schedule your first Job.
    2.  Click on `Create job` button or navigate to the new Cron Job form [here](/dashboard/project/_/integrations/cron/jobs?dialog-shown=true).
    3.  Name your Cron Job.
    4.  Choose a schedule for your Job by inputting cron syntax (refer to the syntax chart in the form) or natural language.
    5.  Input SQL snippet or select a Database function, HTTP request, or Supabase Edge Function.
  </TabPanel>

  <TabPanel id="sql-schedule-job" label="SQL">
    ```sql
    -- Cron Job name cannot be edited
    select cron.schedule('permanent-cron-job-name', '30 seconds', 'CALL do_something()');
    ```
  </TabPanel>
</Tabs>

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6">
  <div className="border-b mt-3 pb-3">
    <AccordionItem header="Cron syntax" id="item-1">
      ```
      ┌───────────── min (0 - 59)
      │ ┌────────────── hour (0 - 23)
      │ │ ┌─────────────── day of month (1 - 31)
      │ │ │ ┌──────────────── month (1 - 12)
      │ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are Sunday to
      │ │ │ │ │                  Saturday, or use names; 7 is also Sunday)
      │ │ │ │ │
      │ │ │ │ │
      * * * * *
      ```

      You can use \[1-59] seconds (e.g. `30 seconds`) as the cron syntax to schedule sub-minute Jobs.
    </AccordionItem>
  </div>
</Accordion>

<Admonition type="note">
  You can input seconds for your Job schedule interval as long as you're on Postgres version 15.1.1.61 or later.
</Admonition>



## Edit a job

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard-edit-job" queryGroup="database-method">
  <TabPanel id="dashboard-edit-job" label="Dashboard">
    1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to edit.
    2.  Click on the three vertical dots menu on the right side of the Job and click `Edit cron job`.
    3.  Make your changes and then click `Save cron job`.
  </TabPanel>

  <TabPanel id="sql-edit-job" label="SQL">
    ```sql
    select cron.alter_job(
      job_id := (select jobid from cron.job where jobname = 'permanent-cron-job-name'),
      schedule := '*/5 * * * *'
    );
    ```

    Full options for the `cron.alter_job()` function are:

    ```sql
    cron.alter_job(
      job_id bigint,
      schedule text default null,
      command text default null,
      database text default null,
      username text default null,
      active boolean default null
    )
    ```

    It is also possible to modify a job by using the `cron.schedule()` function by inputting the same job name. This will replace the existing job via upsert.
  </TabPanel>
</Tabs>



## Activate/Deactivate a job

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard-unschedule-job" queryGroup="database-method">
  <TabPanel id="dashboard-unschedule-job" label="Dashboard">
    1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to unschedule.
    2.  Toggle the `Active`/`Inactive` switch next to Job name.
  </TabPanel>

  <TabPanel id="sql-unschedule-job" label="SQL">
    ```sql
    -- Activate Job
    select cron.alter_job(
      job_id := (select jobid from cron.job where jobname = 'permanent-cron-job-name'),
      active := true
    );

    -- Deactivate Job
    select cron.alter_job(
      job_id := (select jobid from cron.job where jobname = 'permanent-cron-job-name'),
      active := false
    );
    ```
  </TabPanel>
</Tabs>



## Unschedule a job

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard-delete-job" queryGroup="database-method">
  <TabPanel id="dashboard-delete-job" label="Dashboard">
    1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you'd like to delete.
    2.  Click on the three vertical dots menu on the right side of the Job and click `Delete cron job`.
    3.  Confirm deletion by entering the Job name.
  </TabPanel>

  <TabPanel id="sql-delete-job" label="SQL">
    ```sql
    select cron.unschedule('permanent-cron-job-name');
    ```

    <Admonition type="caution">
      Unscheduling a Job will permanently delete the Job from `cron.job` table but its run history remain in `cron.job_run_details` table.
    </Admonition>
  </TabPanel>
</Tabs>



## Inspecting job runs

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard-runs-job" queryGroup="database-method">
  <TabPanel id="dashboard-runs-job" label="Dashboard">
    1.  Go to the [Jobs](/dashboard/project/_/integrations/cron/jobs) section and find the Job you want to see the runs of.
    2.  Click on the `History` button next to the Job name.
  </TabPanel>

  <TabPanel id="sql-runs-job" label="SQL">
    ```sql
    select
      *
    from cron.job_run_details
    where jobid = (select jobid from cron.job where jobname = 'permanent-cron-job-name')
    order by start_time desc
    limit 10;
    ```

    <Admonition type="caution">
      The records in the `cron.job_run_details` table are not cleaned up automatically. They are also not removed when jobs are unscheduled, which will take up disk space in your database.
    </Admonition>
  </TabPanel>
</Tabs>



## Examples


### Delete data every week

{/* <!-- vale off --> */}

Delete old data every Saturday at 3:30AM (GMT):

{/* <!-- vale on --> */}

```sql
select cron.schedule (
  'saturday-cleanup', -- name of the cron job
  '30 3 * * 6', -- Saturday at 3:30AM (GMT)
  $$ delete from events where event_time < now() - interval '1 week' $$
);
```


### Run a vacuum every day

{/* <!-- vale off --> */}

Vacuum every day at 3:00AM (GMT):

{/* <!-- vale on --> */}

```sql
select cron.schedule('nightly-vacuum', '0 3 * * *', 'VACUUM');
```


### Call a database function every 5 minutes

Create a [`hello_world()`](/docs/guides/database/functions?language=sql#simple-functions) database function and then call it every 5 minutes:

```sql
select cron.schedule('call-db-function', '*/5 * * * *', 'SELECT hello_world()');
```


### Call a database stored procedure

To use a stored procedure, you can call it like this:

```sql
select cron.schedule('call-db-procedure', '*/5 * * * *', 'CALL my_procedure()');
```


### Invoke Supabase Edge Function every 30 seconds

Make a POST request to a Supabase Edge Function every 30 seconds:

```sql
select
  cron.schedule(
    'invoke-function-every-half-minute',
    '30 seconds',
    $$
    select
      net.http_post(
          url:='https://project-ref.supabase.co/functions/v1/function-name',
          headers:=jsonb_build_object('Content-Type','application/json', 'Authorization', 'Bearer ' || 'YOUR_ANON_KEY'),
          body:=jsonb_build_object('time', now() ),
          timeout_milliseconds:=5000
      ) as request_id;
    $$
  );
```

<Admonition type="note">
  This requires the [`pg_net` extension](/docs/guides/database/extensions/pg_net) to be enabled.
</Admonition>



## Caution: Scheduling system maintenance

Be extremely careful when setting up Jobs for system maintenance tasks as they can have unintended consequences.

For instance, scheduling a command to terminate idle connections with `pg_terminate_backend(pid)` can disrupt critical background processes like nightly backups. Often, there is an existing Postgres setting, such as `idle_session_timeout`, that can perform these common maintenance tasks without the risk.

Reach out to [Supabase Support](/support) if you're unsure if that applies to your use case.



# Auth architecture

The architecture behind Supabase Auth.

There are four major layers to Supabase Auth:

1.  [Client layer.](#client-layer) This can be one of the Supabase client SDKs, or manually made HTTP requests using the HTTP client of your choice.
2.  Kong API gateway. This is shared between all Supabase products.
3.  [Auth service](#auth-service) (formerly known as GoTrue).
4.  [Postgres database.](#postgres) This is shared between all Supabase products.

<Image
  alt="Diagram showing the architecture of Supabase. The Kong API gateway sits in front of 7 services: GoTrue, PostgREST, Realtime, Storage, pg_meta, Functions, and pg_graphql. All the services talk to a single Postgres instance."
  src={{
    dark: '/docs/img/supabase-architecture.svg',
    light: '/docs/img/supabase-architecture--light.svg',
  }}
/>



## Client layer

The client layer runs in your app. This could be running in many places, including:

*   Your frontend browser code
*   Your backend server code
*   Your native application

The client layer provides the functions that you use to sign in and manage users. We recommend using the Supabase client SDKs, which handle:

*   Configuration and authentication of HTTP calls to the Supabase Auth backend
*   Persistence, refresh, and removal of Auth Tokens in your app's storage medium
*   Integration with other Supabase products

But at its core, this layer manages the making of HTTP calls, so you could write your own client layer if you wanted to.

See the Client SDKs for more information:

*   [JavaScript](/docs/reference/javascript/introduction)
*   [Flutter](/docs/reference/dart/introduction)
*   [Swift](/docs/reference/swift/introduction)
*   [Python](/docs/reference/python/introduction)
*   [C#](/docs/reference/csharp/introduction)
*   [Kotlin](/docs/reference/kotlin/introduction)



## Auth service

The [Auth service](https://github.com/supabase/auth) is an Auth API server written and maintained by Supabase. It is a fork of the GoTrue project, originally created by Netlify.

When you deploy a new Supabase project, we deploy an instance of this server alongside your database, and inject your database with the required Auth schema.

The Auth service is responsible for:

*   Validating, issuing, and refreshing JWTs
*   Serving as the intermediary between your app and Auth information in the database
*   Communicating with external providers for Social Login and SSO



## Postgres

Supabase Auth uses the `auth` schema in your Postgres database to store user tables and other information. For security, this schema is not exposed on the auto-generated API.

You can connect Auth information to your own objects using [database triggers](/docs/guides/database/postgres/triggers) and [foreign keys](https://www.postgresql.org/docs/current/tutorial-fk.html). Make sure that any views you create for Auth data are adequately protected by [enabling RLS](/docs/guides/database/postgres/row-level-security) or [revoking grants](https://www.postgresql.org/docs/current/sql-revoke.html).

<Admonition type="danger">
  Make sure any views you create for Auth data are protected.

  Starting in Postgres version 15, views inherit the RLS policies of the underlying tables if created with `security_invoker`. Views in earlier versions, or those created without `security_invoker`, inherit the permissions of the owner, who can bypass RLS policies.
</Admonition>



# Auth Audit Logs

Monitor and track authentication events with audit logging.

Auth audit logs provide comprehensive tracking of authentication events in your Supabase project. Audit logs are automatically captured for all authentication events and help you monitor user authentication activities, detect suspicious behavior, and maintain compliance with security requirements.



## What gets logged

Supabase auth audit logs automatically capture all authentication events including:

*   User signups and logins
*   Password changes and resets
*   Email verification events
*   Token refresh and logout events



## Storage options

By default, audit logs are stored in two places:

1.  **Your project's Postgres database** - Stored in the `auth.audit_log_entries` table, searchable via SQL but uses database storage
2.  **External log storage** - Cost-efficient storage accessible through the dashboard

You can disable Postgres storage to reduce database storage costs while keeping the external log storage.


### Configuring audit log storage

1.  Navigate to your project dashboard
2.  Go to **Authentication**
3.  Find the **Audit Logs** under **Configuration** section
4.  Toggle on "Disable writing auth audit logs to project database" to disable database storage

<Admonition type="tip">
  Disabling Postgres storage reduces your database storage costs. Audit logs will still be available through the dashboard.
</Admonition>



## Log format

Audit logs contain detailed information about each authentication event:

```json
{
  "timestamp": "2025-08-01T10:30:00Z",
  "user_id": "uuid",
  "action": "user_signedup",
  "ip_address": "192.168.1.1",
  "user_agent": "Mozilla/5.0...",
  "metadata": {
    "provider": "email"
  }
}
```


### Log actions reference

| Action                          | Description                             |
| ------------------------------- | --------------------------------------- |
| `login`                         | User login attempt                      |
| `logout`                        | User logout                             |
| `invite_accepted`               | Team invitation accepted                |
| `user_signedup`                 | New user registration                   |
| `user_invited`                  | User invitation sent                    |
| `user_deleted`                  | User account deleted                    |
| `user_modified`                 | User profile updated                    |
| `user_recovery_requested`       | Password reset request                  |
| `user_reauthenticate_requested` | User reauthentication required          |
| `user_confirmation_requested`   | Email/phone confirmation requested      |
| `user_repeated_signup`          | Duplicate signup attempt                |
| `user_updated_password`         | Password change completed               |
| `token_revoked`                 | Refresh token revoked                   |
| `token_refreshed`               | Refresh token used to obtain new tokens |
| `generate_recovery_codes`       | MFA recovery codes generated            |
| `factor_in_progress`            | MFA factor enrollment started           |
| `factor_unenrolled`             | MFA factor removed                      |
| `challenge_created`             | MFA challenge initiated                 |
| `verification_attempted`        | MFA verification attempt                |
| `factor_deleted`                | MFA factor deleted                      |
| `recovery_codes_deleted`        | MFA recovery codes deleted              |
| `factor_updated`                | MFA factor settings updated             |
| `mfa_code_login`                | Login with MFA code                     |
| `identity_unlinked`             | An identity unlinked from account       |



## Limitations

*   There may be a short delay before logs appear
*   Query capabilities are limited to the dashboard interface



# Anonymous Sign-Ins

Create and use anonymous users to authenticate with Supabase

[Enable Anonymous Sign-Ins](/dashboard/project/_/auth/providers) to build apps which provide users an authenticated experience without requiring users to enter an email address, password, use an OAuth provider or provide any other PII (Personally Identifiable Information). Later, when ready, the user can link an authentication method to their account.

<Admonition type="note" label="Anonymous user vs the anon key">
  Calling `signInAnonymously()` creates an anonymous user. It's just like a permanent user, except the user can't access their account if they sign out, clear browsing data, or use another device.

  Like permanent users, the `authenticated` Postgres role will be used when using the Data APIs to access your project. JWTs for these users will have an `is_anonymous` claim which you can use to distinguish in RLS policies.

  This is different from the `anon` API key which does not create a user and can be used to implement public access to your database as it uses the `anonymous` Postgres role.
</Admonition>

Anonymous sign-ins can be used to build:

*   E-commerce applications, such as shopping carts before check-out
*   Full-feature demos without collecting personal information
*   Temporary or throw-away accounts

<Admonition type="caution">
  Review your existing RLS policies before enabling anonymous sign-ins. Anonymous users use the `authenticated` role. To distinguish between anonymous users and permanent users, your policies need to check the `is_anonymous` field of the user's JWT.

  See the [Access control section](#access-control) for more details.
</Admonition>

<Admonition type="caution" label="Use Dynamic Rendering with Next.js">
  The Supabase team has received reports of user metadata being cached across unique anonymous users as a result of Next.js static page rendering. For the best user experience, utilize dynamic page rendering.
</Admonition>

<Admonition type="note" label="Self hosting and local development">
  For self-hosting, you can update your project configuration using the files and environment variables provided. See the [local development docs](/docs/guides/cli/config) for more details.
</Admonition>



## Sign in anonymously

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Call the [`signInAnonymously()`](/docs/reference/javascript/auth-signinanonymously) method:

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data, error } = await supabase.auth.signInAnonymously()
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    Call the [`signInAnonymously()`](/docs/reference/dart/auth-signinanonymously) method:

    ```dart
    await supabase.auth.signInAnonymously();
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Call the [`signInAnonymously()`](/docs/reference/swift/auth-signinanonymously) method:

    ```swift
    let session = try await supabase.auth.signInAnonymously()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Call the [`signInAnonymously()`](/docs/reference/kotlin/auth-signinanonymously) method:

    ```kotlin
    supabase.auth.signInAnonymously()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Call the [`sign_in_anonymously()`](/docs/reference/python/auth-signinanonymously) method:

    ```python
    response = supabase.auth.sign_in_anonymously()
    ```
  </TabPanel>
</Tabs>



## Convert an anonymous user to a permanent user

Converting an anonymous user to a permanent user requires [linking an identity](/docs/guides/auth/auth-identity-linking#manual-linking-beta) to the user. This requires you to [enable manual linking](/dashboard/project/_/auth/providers) in your Supabase project.


### Link an email / phone identity

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You can use the [`updateUser()`](/docs/reference/javascript/auth-updateuser) method to link an email or phone identity to the anonymous user. To add a password for the anonymous user, the user's email or phone number needs to be verified first.

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data: updateEmailData, error: updateEmailError } = await supabase.auth.updateUser({
      email: 'valid.email@supabase.io',
    })

    // verify the user's email by clicking on the email change link
    // or entering the 6-digit OTP sent to the email address

    // once the user has been verified, update the password
    const { data: updatePasswordData, error: updatePasswordError } = await supabase.auth.updateUser({
      password: 'password',
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    You can use the [`updateUser()`](/docs/reference/dart/auth-updateuser) method to link an email or phone identity to the anonymous user.

    ```dart
    await supabase.auth.updateUser(UserAttributes(email: 'valid.email@supabase.io'));
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You can use the [`update(user:)`](/docs/reference/swift/auth-updateuser) method to link an email or phone identity to the anonymous user.

    ```swift
    try await supabase.auth.update(
      user: UserAttributes(email: "valid.email@supabase.io")
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    You can use the [`updateUser()`](/docs/reference/kotlin/auth-updateuser) method to link an email or phone identity to the anonymous user.

    ```kotlin
    supabase.auth.updateUser {
        email = "valid.email@supabase.io"
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    You can use the [`update_user()`](/docs/reference/python/auth-updateuser) method to link an email or phone identity to the anonymous user. To add a password for the anonymous user, the user's email or phone number needs to be verified first.

    ```python
    response = supabase.auth.update_user({
      'email': 'valid.email@supabase.io',
    })

    # verify the user's email by clicking on the email change link
    # or entering the 6-digit OTP sent to the email address

    # once the user has been verified, update the password
    response = supabase.auth.update_user({
      'password': 'password',
    })
    ```
  </TabPanel>
</Tabs>


### Link an OAuth identity

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You can use the [`linkIdentity()`](/docs/reference/javascript/auth-linkidentity) method to link an OAuth identity to the anonymous user.

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('https://your-project.supabase.co', 'sb_publishable_... or anon key')

    // ---cut---
    const { data, error } = await supabase.auth.linkIdentity({ provider: 'google' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Flutter">
    You can use the [`linkIdentity()`](/docs/reference/dart/auth-linkidentity) method to link an OAuth identity to the anonymous user.

    ```dart
    await supabase.auth.linkIdentity(OAuthProvider.google);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You can use the [`linkIdentity()`](/docs/reference/swift/auth-linkidentity) method to link an OAuth identity to the anonymous user.

    ```swift
    try await supabase.auth.linkIdentity(provider: .google)
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    You can use the [`linkIdentity()`](/docs/reference/kotlin/auth-linkidentity) method to link an OAuth identity to the anonymous user.

    ```kotlin
    supabase.auth.linkIdentity(Google)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    You can use the [`link_identity()`](/docs/reference/python/auth-linkidentity) method to link an OAuth identity to the anonymous user.

    ```python
    response = supabase.auth.link_identity({'provider': 'google'})
    ```
  </TabPanel>
</Tabs>



## Access control

An anonymous user assumes the `authenticated` role just like a permanent user. You can use row-level security (RLS) policies to differentiate between an anonymous user and a permanent user by checking for the `is_anonymous` claim in the JWT returned by `auth.jwt()`:

```sql
create policy "Only permanent users can post to the news feed"
on news_feed as restrictive for insert
to authenticated
with check ((select (auth.jwt()->>'is_anonymous')::boolean) is false );

create policy "Anonymous and permanent users can view the news feed"
on news_feed for select
to authenticated
using ( true );
```

<Admonition type="note" label="Use restrictive policies">
  RLS policies are permissive by default, which means that they are combined using an "OR" operator when multiple policies are applied. It is important to construct restrictive policies to ensure that the checks for an anonymous user are always enforced when combined with other policies.
  Be aware that a single 'restrictive' RLS policy alone will fail unless combined with another policy that returns true, ensuring the combined condition is met.
</Admonition>



## Resolving identity conflicts

Depending on your application requirements, data conflicts can arise when an anonymous user is converted to a permanent user. For example, in the context of an e-commerce application, an anonymous user would be allowed to add items to the shopping cart without signing up / signing in. When they decide to sign-in to an existing account, you will need to decide how you want to resolve data conflicts in the shopping cart:

1.  Overwrite the items in the cart with those in the existing account
2.  Overwrite the items in the cart with those from the anonymous user
3.  Merge the items in the cart together


### Linking an anonymous user to an existing account

In some cases, you may need to link an anonymous user to an existing account rather than creating a new permanent account. This process requires manual handling of potential conflicts. Here's a general approach:

```javascript
// 1. Sign in anonymously (assuming the user is already signed in anonymously)
const { data: anonData, error: anonError } = await supabase.auth.getSession()

// 2. Attempt to update the user with the existing email
const { data: updateData, error: updateError } = await supabase.auth.updateUser({
  email: 'valid.email@supabase.io',
})

// 3. Handle the error (since the email belongs to an existing user)
if (updateError) {
  console.log('This email belongs to an existing user. Please sign in to that account.')

  // 4. Sign in to the existing account
  const {
    data: { user: existingUser },
    error: signInError,
  } = await supabase.auth.signInWithPassword({
    email: 'valid.email@supabase.io',
    password: 'user_password',
  })

  if (existingUser) {
    // 5. Reassign entities tied to the anonymous user
    // This step will vary based on your specific use case and data model
    const { data: reassignData, error: reassignError } = await supabase
      .from('your_table')
      .update({ user_id: existingUser.id })
      .eq('user_id', anonData.session.user.id)

    // 6. Implement your chosen conflict resolution strategy
    // This could involve merging data, overwriting, or other custom logic
    await resolveDataConflicts(anonData.session.user.id, existingUser.id)
  }
}

// Helper function to resolve data conflicts (implement based on your strategy)
async function resolveDataConflicts(anonymousUserId, existingUserId) {
  // Implement your conflict resolution logic here
  // This could involve ignoring the anonymous user's metadata, overwriting the existing user's metadata, or merging the data of both the anonymous and existing user.
}
```



## Abuse prevention and rate limits

Since anonymous users are stored in your database, bad actors can abuse the endpoint to increase your database size drastically. It is strongly recommended to [enable invisible CAPTCHA or Cloudflare Turnstile](/docs/guides/auth/auth-captcha) to prevent abuse for anonymous sign-ins. An IP-based rate limit is enforced at 30 requests per hour which can be modified in your [dashboard](/dashboard/project/_/auth/rate-limits). You can refer to the full list of rate limits [here](/docs/guides/platform/going-into-prod#rate-limiting-resource-allocation--abuse-prevention).



## Automatic cleanup

Automatic cleanup of anonymous users is currently not available. Instead, you can delete anonymous users from your project by running the following SQL:

```sql
-- deletes anonymous users created more than 30 days ago
delete from auth.users
where is_anonymous is true and created_at < now() - interval '30 days';
```



## Resources

*   [Supabase - Get started for free](https://supabase.com)
*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Supabase Flutter Client](https://github.com/supabase/supabase-flutter)
*   [Supabase Kotlin Client](https://github.com/supabase-community/supabase-kt)



# Enable CAPTCHA Protection



Supabase provides you with the option of adding CAPTCHA to your sign-in, sign-up, and password reset forms. This keeps your website safe from bots and malicious scripts. Supabase authentication has support for [hCaptcha](https://www.hcaptcha.com/) and [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/).



## Sign up for CAPTCHA

<Tabs scrollable size="small" type="underlined" defaultActiveId="hcaptcha-1" queryGroup="captcha-method">
  <TabPanel id="hcaptcha-1" label="HCaptcha">
    Go to the [hCaptcha](https://www.hcaptcha.com/) website and sign up for an account. On the Welcome page, copy the **Sitekey** and **Secret key**.

    If you have already signed up and didn't copy this information from the Welcome page, you can get the **Secret key** from the Settings page.

    ![site\_secret\_settings.png](/docs/img/guides/auth-captcha/site_secret_settings.png)

    The **Sitekey** can be found in the **Settings** of the active site you created.

    ![sites\_dashboard.png](/docs/img/guides/auth-captcha/sites_dashboard.png)

    In the Settings page, look for the **Sitekey** section and copy the key.

    ![sitekey\_settings.png](/docs/img/guides/auth-captcha/sitekey_settings.png)
  </TabPanel>

  <TabPanel id="turnstile-1" label="Turnstile">
    Go to the [Cloudflare website](https://dash.cloudflare.com/login) and sign up for an account. On the Welcome page, head to the Turnstile section and add a new site. Create a site and take note of the **Sitekey** and **Secret Key** as shown below
    ![cloudflare\_settings.png](/docs/img/guides/auth-captcha/cloudflare_settings.png)
  </TabPanel>
</Tabs>



## Enable CAPTCHA protection for your Supabase project

Navigate to the **[Auth](/dashboard/project/_/auth/protection)** section of your Project Settings in the Supabase Dashboard and find the **Enable CAPTCHA protection** toggle under Settings > Authentication > Bot and Abuse Protection > Enable CAPTCHA protection.

Select your CAPTCHA provider from the dropdown, enter your CAPTCHA **Secret key**, and click **Save**.



## Add the CAPTCHA frontend component

The frontend requires some changes to provide the CAPTCHA on-screen for the user. This example uses React and the corresponding CAPTCHA React component, but both CAPTCHA providers can be used with any JavaScript framework.

<Tabs scrollable size="small" type="underlined" defaultActiveId="hcaptcha-2" queryGroup="captcha-method">
  <TabPanel id="hcaptcha-2" label="HCaptcha">
    Install `@hcaptcha/react-hcaptcha` in your project as a dependency.

    ```bash
    npm install @hcaptcha/react-hcaptcha
    ```

    Now import the `HCaptcha` component from the `@hcaptcha/react-hcaptcha` library.

    ```javascript
    import HCaptcha from '@hcaptcha/react-hcaptcha'
    ```

    Let's create a empty state to store our `captchaToken`

    ```jsx
    const [captchaToken, setCaptchaToken] = useState()
    ```

    Now lets add the `HCaptcha` component to the JSX section of our code

    ```jsx
    <HCaptcha />
    ```

    We will pass it the sitekey we copied from the hCaptcha website as a property along with a `onVerify` property which takes a callback function. This callback function will have a token as one of its properties. Let's set the token in the state using `setCaptchaToken`

    ```jsx
    <HCaptcha
      sitekey="your-sitekey"
      onVerify={(token) => {
        setCaptchaToken(token)
      }}
    />
    ```

    Now lets use the CAPTCHA token we receive in our Supabase signUp function.

    ```jsx
    await supabase.auth.signUp({
      email,
      password,
      options: { captchaToken },
    })
    ```

    We will also need to reset the CAPTCHA challenge after we have made a call to the function above.

    Create a ref to use on our `HCaptcha` component.

    ```jsx
    const captcha = useRef()
    ```

    Let's add a ref attribute on the `HCaptcha` component and assign the `captcha` constant to it.

    ```jsx
    <HCaptcha
      ref={captcha}
      sitekey="your-sitekey"
      onVerify={(token) => {
        setCaptchaToken(token)
      }}
    />
    ```

    Reset the `captcha` after the signUp function is called using the following code:

    ```jsx
    captcha.current.resetCaptcha()
    ```

    In order to test that this works locally we will need to use something like [ngrok](https://ngrok.com/) or add an entry to your hosts file. You can read more about this in the [hCaptcha docs](https://docs.hcaptcha.com/#local-development).
  </TabPanel>

  <TabPanel id="turnstile-2" label="Turnstile">
    The frontend requires some changes to provide the CAPTCHA on-screen for the user. Turnstile can be used with any JavaScript framework but we'll use React and the Turnstile React component for this example.

    Install @marsidev/react-turnstile in your project as a dependency.

    ```bash
    npm install @marsidev/react-turnstile
    ```

    Now import the Turnstile component from the @marsidev/react-turnstile library.

    ```jsx
    import { Turnstile } from '@marsidev/react-turnstile'
    ```

    Let's create an empty state to store our `captchaToken`

    ```jsx
    const [captchaToken, setCaptchaToken] = useState()
    ```

    Now lets add the Cloudflare Turnstile component to the JSX section of our code:

    ```jsx
    <Turnstile />
    ```

    We will pass it the sitekey we copied from the Cloudflare website as a property along with a `onSuccess` property which takes a callback function. This callback function will have a token as one of its properties. Let's set the token in the state using `setCaptchaToken`:

    ```jsx
    <Turnstile
      siteKey="your-sitekey"
      onSuccess={(token) => {
        setCaptchaToken(token)
      }}
    />
    ```

    We can now use the `captchaToken` we receive in our Supabase `signUp` function.

    ```jsx
    await supabase.auth.signUp({
      email,
      password,
      options: { captchaToken },
    })
    ```

    To test locally, you will need to add localhost to the domain allowlist as per the [Cloudflare docs](https://developers.cloudflare.com/turnstile/reference/testing/)
  </TabPanel>
</Tabs>

Run the application and you should now be provided with a CAPTCHA challenge.



# Passwordless email logins

Email logins using Magic Links or One-Time Passwords (OTPs)

Supabase Auth provides several passwordless login methods. Passwordless logins allow users to sign in without a password, by clicking a confirmation link or entering a verification code.

Passwordless login can:

*   Improve the user experience by not requiring users to create and remember a password
*   Increase security by reducing the risk of password-related security breaches
*   Reduce support burden of dealing with password resets and other password-related flows

Supabase Auth offers two passwordless login methods that use the user's email address:

*   [Magic Link](#with-magic-link)
*   [OTP](#with-otp)



## With Magic Link

Magic Links are a form of passwordless login where users click on a link sent to their email address to log in to their accounts. Magic Links only work with email addresses and are one-time use only.


### Enabling Magic Link

Email authentication methods, including Magic Links, are enabled by default.

Configure the Site URL and any additional redirect URLs. These are the only URLs that are allowed as redirect destinations after the user clicks a Magic Link. You can change the URLs on the [URL Configuration page](/dashboard/project/_/auth/url-configuration) for hosted projects, or in the [configuration file](/docs/guides/cli/config#auth.additional_redirect_urls) for self-hosted projects.

By default, a user can only request a magic link once every <SharedData data="config">auth.rate\_limits.magic\_link.period</SharedData> and they expire after <SharedData data="config">auth.rate\_limits.magic\_link.validity</SharedData>.


### Signing in with Magic Link

Call the "sign in with OTP" method from the client library.

Though the method is labelled "OTP", it sends a Magic Link by default. The two methods differ only in the content of the confirmation email sent to the user.

If the user hasn't signed up yet, they are automatically signed up by default. To prevent this, set the `shouldCreateUser` option to `false`.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    async function signInWithEmail() {
      const { data, error } = await supabase.auth.signInWithOtp({
        email: 'valid.email@supabase.io',
        options: {
          // set this to false if you do not want the user to be automatically signed up
          shouldCreateUser: false,
          emailRedirectTo: 'https://example.com/welcome',
        },
      })
    }
    ```
  </TabPanel>

  <TabPanel id="react-native" label="Expo React Native">
    ```ts
    import { makeRedirectUri } from 'expo-auth-session'

    const redirectTo = makeRedirectUri()

    const { error } = await supabase.auth.signInWithOtp({
      email: 'valid.email@supabase.io',
      options: {
        emailRedirectTo: redirectTo,
      },
    })
    ```

    Read the [Deep Linking Documentation](/docs/guides/auth/native-mobile-deep-linking) to learn how to handle deep linking.
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    Future<void> signInWithEmail() async {
      final AuthResponse res = await supabase.auth.signinwithotp(email: 'valid.email@supabase.io');
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signInWithOTP(
      email: "valid.email@supabase.io",
      redirectTo: URL(string: "https://example.com/welcome"),
      // set this to false if you do not want the user to be automatically signed up
      shouldCreateUser: false
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    suspend fun signInWithEmail() {
    	supabase.auth.signInWith(OTP) {
    		email = "valid.email@supabase.io"
    	}
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.auth.sign_in_with_otp({
      'email': 'valid.email@supabase.io',
      'options': {
        # set this to false if you do not want the user to be automatically signed up
        'should_create_user': False,
        'email_redirect_to': 'https://example.com/welcome',
      },
    })
    ```
  </TabPanel>
</Tabs>

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

That's it for the implicit flow.

If you're using PKCE flow, edit the Magic Link [email template](/docs/guides/auth/auth-email-templates) to send a token hash:

```html
<h2>Magic Link</h2>

<p>Follow this link to login:</p>
<p><a href="{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=email">Log In</a></p>
```

At the `/auth/confirm` endpoint, exchange the hash for the session:

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('url', 'anonKey')

// ---cut---
const { error } = await supabase.auth.verifyOtp({
  token_hash: 'hash',
  type: 'email',
})
```



## With OTP

Email one-time passwords (OTP) are a form of passwordless login where users key in a six digit code sent to their email address to log in to their accounts.


### Enabling email OTP

Email authentication methods, including Email OTPs, are enabled by default.

Email OTPs share an implementation with Magic Links. To send an OTP instead of a Magic Link, alter the **Magic Link** email template. For a hosted Supabase project, go to [Email Templates](/dashboard/project/_/auth/templates) in the Dashboard. For a self-hosted project or local development, see the [Email Templates guide](/docs/guides/auth/auth-email-templates).

Modify the template to include the `{{ .Token }}` variable, for example:

```html
<h2>One time login code</h2>

<p>Please enter this code: {{ .Token }}</p>
```

By default, a user can only request an OTP once every <SharedData data="config">auth.rate\_limits.otp.period</SharedData> and they expire after <SharedData data="config">auth.rate\_limits.otp.validity</SharedData>. This is configurable via `Auth > Providers > Email > Email OTP Expiration`. An expiry duration of more than 86400 seconds (one day) is disallowed to guard against brute force attacks. The longer an OTP remains valid, the more time an attacker has to attempt brute force attacks. If the OTP is valid for several days, an attacker might have more opportunities to guess the correct OTP through repeated attempts.


### Signing in with email OTP


#### Step 1: Send the user an OTP code

Get the user's email and call the "sign in with OTP" method from your client library.

If the user hasn't signed up yet, they are automatically signed up by default. To prevent this, set the `shouldCreateUser` option to `false`.

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    const { data, error } = await supabase.auth.signInWithOtp({
      email: 'valid.email@supabase.io',
      options: {
        // set this to false if you do not want the user to be automatically signed up
        shouldCreateUser: false,
      },
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    Future<void> signInWithEmailOtp() async {
      final AuthResponse res = await supabase.auth.signInWithOtp(email: 'valid.email@supabase.io');
    }
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.signInWithOTP(
      email: "valid.email@supabase.io",
      // set this to false if you do not want the user to be automatically signed up
      shouldCreateUser: false
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    suspend fun signInWithEmailOtp() {
    	supabase.auth.signInWith(OTP) {
    		email = "valid.email@supabase.io"
    	}
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.auth.sign_in_with_otp({
      'email': 'valid.email@supabase.io',
      'options': {
        # set this to false if you do not want the user to be automatically signed up
        'should_create_user': False,
      },
    })
    ```
  </TabPanel>
</Tabs>

If the request is successful, you receive a response with `error: null` and a `data` object where both `user` and `session` are null. Let the user know to check their email inbox.

```json
{
  "data": {
    "user": null,
    "session": null
  },
  "error": null
}
```


#### Step 2: Verify the OTP to create a session

Provide an input field for the user to enter their one-time code.

Call the "verify OTP" method from your client library with the user's email address, the code, and a type of `email`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('url', 'anonKey')

    // ---cut---
    const {
      data: { session },
      error,
    } = await supabase.auth.verifyOtp({
      email: 'email@example.com',
      token: '123456',
      type: 'email',
    })
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.auth.verifyOTP(
      email: email,
      token: "123456",
      type: .email
    )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    supabase.auth.verifyEmailOtp(type = OtpType.Email.EMAIL, email = "email", token = "151345")
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = supabase.auth.verify_otp({
      'email': email,
      'token': '123456',
      'type': 'email',
    })
    ```
  </TabPanel>
</Tabs>

If successful, the user is now logged in, and you receive a valid session that looks like:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjI3MjkxNTc3LCJzdWIiOiJmYTA2NTQ1Zi1kYmI1LTQxY2EtYjk1NC1kOGUyOTg4YzcxOTEiLCJlbWFpbCI6IiIsInBob25lIjoiNjU4NzUyMjAyOSIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6InBob25lIn0sInVzZXJfbWV0YWRhdGEiOnt9LCJyb2xlIjoiYXV0aGVudGljYXRlZCJ9.1BqRi0NbS_yr1f6hnr4q3s1ylMR3c1vkiJ4e_N55dhM",
  "token_type": "bearer",
  "expires_in": 3600,
  "refresh_token": "LSp8LglPPvf0DxGMSj-vaQ",
  "user": {...}
}
```



# Email Templates

Learn how to manage the email templates in Supabase.

You can customize the email messages used for the authentication flows. You can edit the following email templates:

*   Confirm signup
*   Invite user
*   Magic Link
*   Change Email Address
*   Reset Password



## Terminology

The templating system provides the following variables for use:

| Name                     | Description                                                                                                                                                                                                                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `{{ .ConfirmationURL }}` | Contains the confirmation URL. For example, a signup confirmation URL would look like: `https://project-ref.supabase.co/auth/v1/verify?token={{ .TokenHash }}&type=email&redirect_to=https://example.com/path` .                                                                      |
| `{{ .Token }}`           | Contains a 6-digit One-Time-Password (OTP) that can be used instead of the `{{. ConfirmationURL }}` .                                                                                                                                                                                 |
| `{{ .TokenHash }}`       | Contains a hashed version of the `{{ .Token }}`. This is useful for constructing your own email link in the email template.                                                                                                                                                           |
| `{{ .SiteURL }}`         | Contains your application's Site URL. This can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration).                                                                                                                                |
| `{{ .RedirectTo }}`      | Contains the redirect URL passed when `signUp`, `signInWithOtp`, `signInWithOAuth`, `resetPasswordForEmail` or `inviteUserByEmail` is called. The redirect URL allow list can be configured in your project's [authentication settings](/dashboard/project/_/auth/url-configuration). |
| `{{ .Data }}`            | Contains metadata from `auth.users.user_metadata`. Use this to personalize the email message.                                                                                                                                                                                         |
| `{{ .Email }}`           | Contains the original email address of the user. Empty when when trying to [link an email address to an anonymous user](/docs/guides/auth/auth-anonymous#link-an-email--phone-identity).                                                                                              |
| `{{ .NewEmail }}`        | Contains the new email address of the user. This variable is only supported in the "Change Email Address" template.                                                                                                                                                                   |



## Editing email templates

On hosted Supabase projects, edit your email templates on the [Email Templates](/dashboard/project/_/auth/templates) page. On self-hosted projects or in local development, edit your [configuration files](/docs/guides/local-development/customizing-email-templates).

You can also manage email templates using the Management API:

```bash

# Get your access token from https://supabase.com/dashboard/account/tokens
export SUPABASE_ACCESS_TOKEN="your-access-token"
export PROJECT_REF="your-project-ref"


# Get current email templates
curl -X GET "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  | jq 'to_entries | map(select(.key | startswith("mailer_templates"))) | from_entries'


# Update email templates
curl -X PATCH "https://api.supabase.com/v1/projects/$PROJECT_REF/config/auth" \
  -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
      "mailer_subjects_confirmation": "Confirm your signup",
      "mailer_templates_confirmation_content": "<h2>Confirm your signup</h2><p>Follow this link to confirm your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Confirm your email</a></p>",
      "mailer_subjects_magic_link": "Your Magic Link",
      "mailer_templates_magic_link_content": "<h2>Magic Link</h2><p>Follow this link to login:</p><p><a href=\"{{ .ConfirmationURL }}\">Log In</a></p>",
      "mailer_subjects_recovery": "Rest Your Password",
      "mailer_templates_recovery_content": "<h2>Reset Password</h2><p>Follow this link to reset the password for your user:</p><p><a href=\"{{ .ConfirmationURL }}\">Reset Password</a></p>",
      "mailer_subjects_invite": "You have been invited",
      "mailer_templates_invite_content": "<h2>You have been invited</h2><p>You have been invited to create a user on {{ .SiteURL }}. Follow this link to accept the invite:</p><p><a href=\"{{ .ConfirmationURL }}\">Accept the invite</a></p>",
      "mailer_subjects_email_change": "Confirm email change",
      "mailer_templates_email_change_content": "<h2>Confirm email change</h2><p>Follow this link to confirm the update of your email:</p><p><a href=\"{{ .ConfirmationURL }}\">Change email</a></p>",
  }'
```



## Mobile deep linking

For mobile applications, you might need to link or redirect to a specific page within your app. See the [Mobile Deep Linking guide](/docs/guides/auth/native-mobile-deep-linking) to set this up.



## Limitations


### Email prefetching

Certain email providers may have spam detection or other security features that prefetch URL links from incoming emails (e.g. [Safe Links in Microsoft Defender for Office 365](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links-about?view=o365-worldwide)).
In this scenario, the `{{ .ConfirmationURL }}` sent will be consumed instantly which leads to a "Token has expired or is invalid" error.
To guard against this there are the options below:

**Option 1**

*   Use an email OTP instead by including `{{ .Token }}` in the email template
*   Create your own custom email link to redirect the user to a page where they can enter with their email and token to login

```html
<a href="{{ .SiteURL }}/confirm-signup">Confirm your signup</a>
```

*   Log them in by verifying the OTP token value with their email e.g. with [`supabase.auth.verifyOtp`](/docs/reference/javascript/auth-verifyotp) show below

```ts
const { data, error } = await supabase.auth.verifyOtp({ email, token, type: 'email' })
```

**Option 2**

*   Create your own custom email link to redirect the user to a page where they can click on a button to confirm the action

```html
<a href="{{ .SiteURL }}/confirm-signup?confirmation_url={{ .ConfirmationURL }}"
  >Confirm your signup</a
>
```

*   The button should contain the actual confirmation link which can be obtained from parsing the `confirmation_url={{ .ConfirmationURL }}` query parameter in the URL.


### Email tracking

If you are using an external email provider that enables "email tracking", the links inside the Supabase email templates will be overwritten and won't perform as expected. We recommend disabling email tracking to ensure email links are not overwritten.


### Redirecting the user to a server-side endpoint

If you intend to use [Server-side rendering](/docs/guides/auth/server-side-rendering), you might want the email link to redirect the user to a server-side endpoint to check if they are authenticated before returning the page. However, the default email link will redirect the user after verification to the redirect URL with the session in the query fragments. Since the session is returned in the query fragments by default, you won't be able to access it on the server-side.

You can customize the email link in the email template to redirect the user to a server-side endpoint successfully. For example:

```html
<a
  href="https://api.example.com/v1/authenticate?token_hash={{ .TokenHash }}&type=invite&redirect_to={{ .RedirectTo }}"
  >Accept the invite
</a>
```

When the user clicks on the link, the request will hit `https://api.example.com/v1/authenticate` and you can grab the `token_hash`, `type` and `redirect_to` query parameters from the URL. Then, you can call the [`verifyOtp`](/docs/reference/javascript/auth-verifyotp) method to get back an authenticated session before redirecting the user back to the client. Since the `verifyOtp` method makes a `POST` request to Supabase Auth to verify the user, the session will be returned in the response body, which can be read by the server. For example:

```ts
import { createClient, type EmailOtpType } from '@supabase/supabase-js'
const supabase = createClient(
  'https://your-project-id.supabase.co',
  'sb_publishable_... or anon key'
)

// ---cut---
const { token_hash, type } = Object.fromEntries(new URLSearchParams(window.location.search))
const {
  data: { session },
  error,
} = await supabase.auth.verifyOtp({ token_hash, type: type as EmailOtpType })

// subsequently redirect the user back to the client using the redirect_to param
// ...
```



## Customization

Supabase Auth makes use of [Go Templates](https://pkg.go.dev/text/template). This means it is possible to conditionally render information based on template properties.


### Send different email to early access users

Send a different email to users who signed up via an early access domain (`https://www.earlyaccess.trial.com`).

```
{{ if eq .Data.Domain "https://www.example.com" }}
<h1>Welcome to Our Database Service!</h1>
  <p>Dear Developer,</p>
  <p>Welcome to Billy, the scalable developer platform!</p>
  <p>Best Regards,<br>
Billy Team</p>
{{ else if eq .Data.Domain "https://www.earlyaccess.trial.com" }}
<h1>Welcome to Our Database Service!</h1>
  <p>Dear Developer,</p>
  <p>Welcome Billy, the scalable developer platform!</p>
  <p> As an early access member, you have access to select features like Point To Space Restoration.</p>
  <p>Best Regards,<br>
Billy Team</p>
{{ end }}
```



# Auth Helpers



<Admonition type="caution">
  The Auth helpers package is deprecated. Use the new `@supabase/ssr` package for Server Side Authentication. `@supabase/ssr` takes the core concepts of the Auth Helpers package and makes them available to any server framework. Read out the [migration doc](/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers) to learn more.
</Admonition>

Working with server-side frameworks is slightly different to client-side frameworks. In this section we cover the various ways of handling server-side authentication and demonstrate how to use the Supabase helper-libraries to make the process more seamless.

<div className="container" style={{ padding: 0 }}>
  <div className="grid md:grid-cols-12 gap-4">
    {/* Next.js */}

    <div className="col-span-6">
      <ButtonCard to={'/guides/auth/auth-helpers/nextjs'} title={'Next.js'} description={'Helpers for authenticating users in Next.js applications.'} />
    </div>

    {/* SvelteKit */}

    <div className="col-span-6">
      <ButtonCard to={'/guides/auth/auth-helpers/sveltekit'} title={'SvelteKit'} description={'Helpers for authenticating users in SvelteKit applications.'} />
    </div>

    {/* Remix */}

    <div className="col-span-6">
      <ButtonCard to={'/guides/auth/auth-helpers/remix'} title={'Remix'} description={'Helpers for authenticating users in Remix applications.'} />
    </div>
  </div>
</div>



## Status

The Auth Helpers are `deprecated`. Use the new `@supabase/ssr` package for Server Side Authentication. Use the [migration doc](/docs/guides/auth/server-side/migrating-to-ssr-from-auth-helpers) to learn more.



## Additional links

*   [Source code](https://github.com/supabase/auth-helpers)
*   [Known bugs and issues](https://github.com/supabase/auth-helpers/issues)



# Auth Hooks

Use HTTP or Postgres Functions to customize your authentication flow


## What is a hook

A hook is an endpoint that allows you to alter the default Supabase Auth flow at specific execution points. Developers can use hooks to add custom behavior that's not supported natively.

Hooks help you:

*   Track the origin of user signups by adding metadata
*   Improve security by adding additional checks to password and multi-factor authentication
*   Support legacy systems by integrating with identity credentials from external authentication systems
*   Add additional custom claims to your JWT
*   Send authentication emails or SMS messages through a custom provider

The following hooks are available:

| Hook                                                                                     | Available on Plan    |
| ---------------------------------------------------------------------------------------- | -------------------- |
| [Before User Created](/docs/guides/auth/auth-hooks/before-user-created-hook)             | Free, Pro            |
| [Custom Access Token](/docs/guides/auth/auth-hooks/custom-access-token-hook)             | Free, Pro            |
| [Send SMS](/docs/guides/auth/auth-hooks/send-sms-hook)                                   | Free, Pro            |
| [Send Email](/docs/guides/auth/auth-hooks/send-email-hook)                               | Free, Pro            |
| [MFA Verification Attempt](/docs/guides/auth/auth-hooks/mfa-verification-hook)           | Teams and Enterprise |
| [Password Verification Attempt](/docs/guides/auth/auth-hooks/password-verification-hook) | Teams and Enterprise |

Supabase supports 2 ways to [configure a hook](/dashboard/project/_/auth/hooks) in your project:

<Tabs scrollable size="small" type="underlined" defaultActiveId="postgres-function">
  <TabPanel id="postgres-function" label="Postgres Function">
    A [Postgres function](/docs/guides/database/functions) can be configured as a hook. The function should take in a single argument -- the event of type JSONB -- and return a JSONB object. Since the Postgres function runs on your database, the request does not leave your project's instance.
  </TabPanel>

  <TabPanel id="http" label="HTTP Endpoint">
    A HTTP Hook is an endpoint which takes in a JSON event payload and returns a JSON response. You can use any HTTP endpoint as a Hook, including an endpoint in your application. The easiest way to create a HTTP hook is to create a [Supabase Edge Function](/docs/guides/functions/quickstart).
  </TabPanel>
</Tabs>



## Security model

Sign the payload and grant permissions selectively in order to guard the integrity of the payload.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    When you configure a Postgres function as a hook, Supabase will automatically apply the following grants to the function for these reasons:

    *   Allow the `supabase_auth_admin` role to execute the function. The `supabase_auth_admin` role is the Postgres role that is used by Supabase Auth to make requests to your database.
    *   Revoke permissions from other roles (e.g. `anon`, `authenticated`, `public`) to ensure the function is not accessible by Supabase Data APIs.

    ```sql
    -- Grant access to function to supabase_auth_admin
    grant execute
      on function public.custom_access_token_hook
      to supabase_auth_admin;

    -- Grant access to schema to supabase_auth_admin
    grant usage on schema public to supabase_auth_admin;

    -- Revoke function permissions from authenticated, anon and public
    revoke execute
      on function public.custom_access_token_hook
      from authenticated, anon, public;
    ```

    You will need to alter your row-level security (RLS) policies to allow the `supabase_auth_admin` role to access tables that you have RLS policies on. You can read more about RLS policies [here](/docs/guides/database/postgres/row-level-security).

    Alternatively, you can create your Postgres function via the dashboard with the `security definer` tag. The `security definer` tag specifies that the function is to be executed with the privileges of the user that owns it.

    Currently, functions created via the dashboard take on the `postgres` role. Read more about the `security definer` tag [in our database guide](/docs/guides/database/functions#security-definer-vs-invoker)
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    HTTP Hooks in Supabase follow the [Standard Webhooks Specification](https://www.standardwebhooks.com/), which is a set of guidelines aligning how hooks are implemented. The specification attaches three security headers to guarantee the integrity of the payload:

    *   `webhook-id`: the unique webhook identifier described in the preceding sections.
    *   `webhook-timestamp`: integer UNIX timestamp (seconds since epoch).
    *   `webhook-signature`: the signatures of this webhook. This is generated from body of the hook.

    When the request is made to the HTTP hook, you should use the [Standard Webhooks libraries](https://github.com/standard-webhooks/standard-webhooks/tree/main/libraries) to verify these headers.

    When a HTTP hook is created, the secret generated should be of the `v1,whsec_<base64-secret>` format:

    *   `v1` denotes the version of the hook
    *   `whsec_` signifies that the secret is symmetric
    *   `<base64-secret>` implies a Standard Base64 encoded secret which can contain the characters `+`, `/` and `=`

    The secret is used to verify the payload received in your hook. Create an entry in your `.env.local` file to store the `<standard-base64-secret>` portion of the secret for each hook that you have. For example:

    ```ini
    SEND_SMS_HOOK_SECRETS=v1,whsec_<base64-secret>
    ```

    There field is expressed in plural rather than singular as there are plans to allow for asymmetric signing and multiple hook secrets for ease of secret rotation. For instance: `<standard-base-64-secret>|<another-standard-base-64-secret>`.

    Use the secret in conjunction with the Standard Webhooks package to verify the payload before processing it:

    ```jsx
    import { Webhook } from 'https://esm.sh/standardwebhooks@1.0.0'

    Deno.serve(async (req) => {
      const payload = await req.text()
      const hookSecret = Deno.env.get('SEND_SMS_HOOK_SECRETS').replace('v1,whsec_', '')
      // Extract headers and security specific fields
      const headers = Object.fromEntries(req.headers)
      const wh = new Webhook(hookSecret)
      const data = wh.verify(payload, headers)

      // Payload data is verified, continue with business logic here
      // ...
    })
    ```
  </TabPanel>
</Tabs>



## Using Hooks


### Developing

Let us develop a Hook locally and then deploy it to the cloud. As a recap, here’s a list of available Hooks

| Hook                          | Suggested Function Name         | When it is called                                  | What it Does                                                                                              |
| ----------------------------- | ------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Send SMS                      | `send_sms`                      | Each time an SMS is sent                           | Allows you to customize message content and SMS Provider                                                  |
| Send Email                    | `send_email`                    | Each time an Email is sent                         | Allows you to customize message content and Email Provider                                                |
| Custom Access Token           | `custom_access_token`           | Each time a new JWT is created                     | Returns the claims you wish to be present in the JWT.                                                     |
| MFA Verification Attempt      | `mfa_verification_attempt`      | Each time a user tries to verify an MFA factor.    | Returns a decision on whether to reject the attempt and future ones, or to allow the user to keep trying. |
| Password Verification Attempt | `password_verification_attempt` | Each time a user tries to sign in with a password. | Return a decision whether to allow the user to reject the attempt, or to allow the user to keep trying.   |

Edit `config.toml` to set up the Auth Hook locally.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    Modify the `auth.hook.<hook_name>` field and set `uri` to a value of `pg-functions://postgres/<schema>/<function_name>`

    ```
    [auth.hook.<hook_name>]
    enabled = true
    uri = "pg-functions://...."

    ```

    You need to assign additional permissions so that Supabase Auth can access the hook as well as the tables it interacts with.

    The `supabase_auth_admin` role does not have permissions to the `public` schema. You need to grant the role permission to execute your hook:

    ```sql
    grant execute
      on function public.custom_access_token_hook
      to supabase_auth_admin;

    ```

    You also need to grant usage to `supabase_auth_admin`:

    ```sql
    grant usage on schema public to supabase_auth_admin;

    ```

    Also revoke permissions from the `authenticated` and `anon` roles to ensure the function is not accessible by Supabase Serverless APIs.

    ```sql
    revoke execute
      on function public.custom_access_token_hook
      from authenticated, anon;

    ```

    For security, we recommend against the use the `security definer` tag. The `security definer` tag specifies that the function is to be executed with the privileges of the user that owns it. When a function is created via the Supabase dashboard with the tag, it will have the extensive permissions of the `postgres` role which make it easier for undesirable actions to occur.

    We recommend that you do not use any tag and explicitly grant permissions to `supabase_auth_admin` as described above.

    Read more about `security definer` tag [in our database guide](/docs/guides/database/functions#security-definer-vs-invoker).

    Once done, save your Auth Hook as a migration in order to version the Auth Hook and share it with other team members. Run [`supabase migration new`](/docs/reference/cli/supabase-migration-new) to create a migration.

    <Admonition type="caution">
      If you're using the Supabase SQL Editor, there's an issue when using the `?` (*Does the string exist as a top-level key within the JSON value?*) operator. Use a direct connection to the database if you need to use it when defining a function.
    </Admonition>

    Here is an example hook signature:

    ```sql
    create or replace function public.custom_access_token_hook(event jsonb)
    returns jsonb
    language plpgsql
    as $$
    declare
      -- Insert variables here
    begin
      -- Insert logic here
      return event;
    end;
    $$;

    ```

    You can visit `SQL Editor > Templates` for hook templates.
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    Modify the `auth.hook.<hook_name>` field and set `uri` to a valid HTTP URI. For example, the `send_sms` hook would take the following fields:

    ```toml
    [auth.hook.send_sms]
    enabled = true
    uri = "http://host.docker.internal:54321/functions/v1/send_sms"
    # Comma separated list of secrets
    secrets = "env(SEND_SMS_HOOK_SECRETS)"
    ```

    <Admonition type="note">
      `host.docker.internal` is a special DNS name used in Docker to allow a container to access the host machine's network. This allows the Auth container to reach your HTTP function, no matter if it's a Supabase Edge Function or a custom endpoint.
    </Admonition>

    Fill in the Hook Secret in `supabase/functions/.env`

    ```ini
    SEND_SMS_HOOK_SECRETS='v1,whsec_<base64-secret>'
    ```

    Start the function locally:

    ```bash
    supabase functions serve send-sms --no-verify-jwt
    ```

    Disable JWT verification via the `--no-verify-jwt` to accommodate hooks which are run before a JWT is issued. Payload authenticity is instead protected via the appended security headers associated with the Standard Webhooks Standard.

    Note that payloads are sent uncompressed in order to accurately track Content Length. In addition, there is a 20KB payload limit to guard against payload stuffing attacks.
  </TabPanel>
</Tabs>


### Deploying

In the dashboard, navigate to [`Authentication > Hooks`](/dashboard/project/_/auth/hooks) and select the appropriate function type (SQL or HTTP) from the dropdown menu.


### Error handling

You should return an error when facing a runtime error. Runtime errors are specific to your application and arise from specific business rules rather than programmer errors.

Runtime errors could happen when:

*   The user does not have appropriate permissions
*   The event payload received does not have required claims.
*   The user has performed an action which violates a business rule.
*   The email or phone provider used in the webhook returned an error.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    The error is a JSON object and has the following properties:

    *   `error` An object that contains information about the error.
        *   `http_code` A number indicating the HTTP code to be returned. If not set, the code is HTTP 500 Internal Server Error.
        *   `message` A message to be returned in the HTTP response. Required.

    Here's an example:

    ```json
    {
      "error": {
        "http_code": 429,
        "message": "You can only verify a factor once every 10 seconds."
      }
    }
    ```

    Errors returned from a Postgres Hook are not retry-able. When an error is returned, the error is propagated from the hook to Supabase Auth and translated into a HTTP error which is returned to your application. Supabase Auth will only take into account the error and disregard the rest of the payload.
  </TabPanel>

  <TabPanel id="http" label="HTTP">
    Hooks return status codes based on the nature of the response. These status codes help determine the next steps in the processing flow:

    | HTTP Status Code | Description                                                   | Example Usage                                  |
    | ---------------- | ------------------------------------------------------------- | ---------------------------------------------- |
    | 200, 202, 204    | Valid response, proceed                                       | Successful processing of the request           |
    | 403, 400         | Treated as Internal Server Errors and return a 500 Error Code | Malformed requests or insufficient permissions |
    | 429, 503         | Retry-able errors                                             | Temporary server overload or maintenance       |

    <Admonition type="note">
      `204` Status is not supported by the following hooks which require a response body:

      *   [Custom Access Token](/docs/guides/auth/auth-hooks/custom-access-token-hook)
      *   [MFA Verification Attempt](/docs/guides/auth/auth-hooks/mfa-verification-hook)
      *   [Password Verification Attempt](/docs/guides/auth/auth-hooks/password-verification-hook)
    </Admonition>

    Errors are responses which contain status codes 400 and above. On a retry-able error, such as an error with a `429` or `503` status code, HTTP Hooks will attempt up to three retries with a back-off of two seconds. We have a time budget of 5s for the entire webhook invocation, including retry requests.

    Here's a sample HTTP retry schedule:

    | Time Since Start (HH:MM:SS) | Event                 | Notes                                                                            |
    | --------------------------- | --------------------- | -------------------------------------------------------------------------------- |
    | 00:00:00                    | Initial Attempt       | Initial invocation begins.                                                       |
    | 00:00:02                    | Initial Attempt Fails | Initial invocation returns `429` or `503` with non-empty `retry-after` header.   |
    | 00:00:04                    | Retry Start #1        | After 2 sec delay, first retry begins.                                           |
    | 00:00:05                    | Retry Timeout #1      | First retry times out, exceeded 5 second budget and invocation returns an error. |

    Return a retry-able error by attaching a appropriate status code (`429`, `503`) and a non-empty `retry-after` header

    <Admonition type="note">
      `Retry-After` Supabase Auth does not fully support the `Retry-After` header as described in RFC7231, we only check if it is a non-empty value such as `true` or `10`. Setting this to your preferred value is fine as a future update may address this.
    </Admonition>

    ```jsx
    return new Response(
      JSON.stringify({
        error: `Failed to process the request: ${error}`,
      }),
      { status: 429, headers: { 'Content-Type': 'application/json', 'retry-after': 'true' } }
    )
    ```

    Note that all responses, including error responses, need a `Content-Type` of `application/json` - not specifying the appropriate `Content-Type` will result in the function returning an error response. Supabase Auth will in turn return an Internal Server Error.
  </TabPanel>
</Tabs>

Outside of runtime errors, both HTTP Hooks and Postgres Hooks return timeout errors. Postgres Hooks have <SharedData data="config">auth.hook\_timeouts.postgres\_hooks</SharedData> seconds to complete processing while HTTP Hooks should complete in <SharedData data="config">auth.hook\_timeouts.http\_hooks</SharedData> seconds. Both HTTP Hooks and Postgres Hooks are run in a transaction do limit the duration of execution to avoid delays in authentication process.



## Available Hooks

Each Hook description contains an example JSON Schema which you can use in conjunction with [JSON Schema Faker](https://json-schema-faker.js.org/) in order to generate a mock payload. For HTTP Hooks, you can also use [the Standard Webhooks Testing Tool](https://www.standardwebhooks.com/simulate) to simulate a request.

<div className="grid md:grid-cols-12 gap-4 not-prose">
  {[
        {
          name: 'Custom Access Token',
          description: 'Customize the access token issued by Supabase Auth',
          href: '/guides/auth/auth-hooks/custom-access-token-hook',
        },
        {
          name: 'Send SMS',
          description: 'Use a custom SMS provider to send authentication messages',
          href: '/guides/auth/auth-hooks/send-sms-hook',
        },
        {
          name: 'Send Email',
          description: 'Use a custom email provider to send authentication messages',
          href: '/guides/auth/auth-hooks/send-email-hook',
        },
        {
          name: 'MFA Verification',
          description: 'Add additional checks to the MFA verification flow',
          href: '/guides/auth/auth-hooks/mfa-verification-hook',
        },
        {
          name: 'Password verification',
          description: 'Add additional checks to the password verification flow',
          href: '/guides/auth/auth-hooks/password-verification-hook',
        },
      ].map((x) => (
        <div className="col-span-4" key={x.href}>
          <Link href={x.href} passHref>
            <GlassPanel title={x.name}>{x.description}</GlassPanel>
          </Link>
        </div>
      ))}
</div>



# Identity Linking

Manage the identities associated with your user


## Identity linking strategies

Currently, Supabase Auth supports 2 strategies to link an identity to a user:

1.  [Automatic Linking](#automatic-linking)
2.  [Manual Linking](#manual-linking-beta)


### Automatic linking

Supabase Auth automatically links identities with the same email address to a single user. This helps to improve the user experience when multiple OAuth login options are presented since the user does not need to remember which OAuth account they used to sign up with. When a new user signs in with OAuth, Supabase Auth will attempt to look for an existing user that uses the same email address. If a match is found, the new identity is linked to the user.

In order for automatic linking to correctly identify the user for linking, Supabase Auth needs to ensure that all user emails are unique. It would also be an insecure practice to automatically link an identity to a user with an unverified email address since that could lead to pre-account takeover attacks. To prevent this from happening, when a new identity can be linked to an existing user, Supabase Auth will remove any other unconfirmed identities linked to an existing user.

Users that signed up with [SAML SSO](/docs/guides/auth/sso/auth-sso-saml) will not be considered as targets for automatic linking.


### Manual linking (beta)

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`linkIdentity()`](/docs/reference/javascript/auth-linkidentity):

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-supabase-url>', '<your-supabase-anon-key>')

    // ---cut---
    const { data, error } = await supabase.auth.linkIdentity({ provider: 'google' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`linkIdentity()`](/docs/reference/dart/auth-linkidentity):

    ```dart
    await supabase.auth.linkIdentity(OAuthProvider.google);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`linkIdentity()`](/docs/reference/swift/auth-linkidentity):

    ```swift
    try await supabase.auth.linkIdentity(provider: .google)
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`linkIdentity()`](/docs/reference/kotlin/auth-linkidentity):

    ```kotlin
    supabase.auth.linkIdentity(Google)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Supabase Auth allows a user to initiate identity linking with a different email address when they are logged in. To link an OAuth identity to the user, call [`link_identity()`](/docs/reference/python/auth-linkidentity):

    ```python
    response = supabase.auth.link_identity({'provider': 'google'})
    ```
  </TabPanel>
</Tabs>

In the example above, the user will be redirected to Google to complete the OAuth2.0 flow. Once the OAuth2.0 flow has completed successfully, the user will be redirected back to the application and the Google identity will be linked to the user. You can enable manual linking from your project's authentication [configuration options](/dashboard/project/_/auth/providers) or by setting the environment variable `GOTRUE_SECURITY_MANUAL_LINKING_ENABLED: true` when self-hosting.


### Link identity with native OAuth (ID token)

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    For native mobile applications, you can link an identity using an ID token obtained from a third-party OAuth provider. This is useful when you want to use native OAuth flows (like Google Sign-In or Sign in with Apple) rather than web-based OAuth redirects.

    ```js
    // Example with Google Sign-In (using a native Google Sign-In library)
    const idToken = 'ID_TOKEN_FROM_GOOGLE'
    const accessToken = 'ACCESS_TOKEN_FROM_GOOGLE'

    const { data, error } = await supabase.auth.linkIdentity({
      provider: 'google',
      token: idToken,
      access_token: accessToken,
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    For Flutter applications, you can link an identity using an ID token obtained from native OAuth packages like `google_sign_in` or `sign_in_with_apple`. Call [`linkIdentityWithIdToken()`](/docs/reference/dart/auth-linkidentitywithidtoken):

    ```dart
    import 'package:google_sign_in/google_sign_in.dart';
    import 'package:supabase_flutter/supabase_flutter.dart';

    // First, obtain the ID token from the native provider
    final GoogleSignIn googleSignIn = GoogleSignIn(
      clientId: iosClientId,
      serverClientId: webClientId,
    );
    final googleUser = await googleSignIn.signIn();
    final googleAuth = await googleUser!.authentication;

    // Link the Google identity to the current user
    final response = await supabase.auth.linkIdentityWithIdToken(
      provider: OAuthProvider.google,
      idToken: googleAuth.idToken!,
      accessToken: googleAuth.accessToken!,
    );
    ```

    This method supports the same OAuth providers as `signInWithIdToken()`: Google, Apple, Facebook, Kakao, and Keycloak.
  </TabPanel>
</Tabs>



## Unlink an identity

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    You can use [`getUserIdentities()`](/docs/reference/javascript/auth-getuseridentities) to fetch all the identities linked to a user. Then, call [`unlinkIdentity()`](/docs/reference/javascript/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

    ```js
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('<your-supabase-url>', '<your-supabase-anon-key>')

    // ---cut---
    // retrieve all identities linked to a user
    const { data: identities, error: identitiesError } = await supabase.auth.getUserIdentities()

    if (!identitiesError) {
      // find the google identity linked to the user
      const googleIdentity = identities.identities.find((identity) => identity.provider === 'google')

      if (googleIdentity) {
        // unlink the google identity from the user
        const { data, error } = await supabase.auth.unlinkIdentity(googleIdentity)
      }
    }
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    You can use [`getUserIdentities()`](/docs/reference/dart/auth-getuseridentities) to fetch all the identities linked to a user. Then, call [`unlinkIdentity()`](/docs/reference/dart/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

    ```dart
    // retrieve all identities linked to a user
    final List<UserIdentity> identities = await supabase.auth.getUserIdentities();

    // find the google identity linked to the user
    final UserIdentity googleIdentity =
        identities.singleWhere((identity) => identity.provider == 'google');

    // unlink the google identity from the user
    await supabase.auth.unlinkIdentity(googleIdentity);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    You can use [`getUserIdentities()`](/docs/reference/swift/auth-getuseridentities) to fetch all the identities linked to a user. Then, call [`unlinkIdentity()`](/docs/reference/swift/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

    ```swift
    // retrieve all identities linked to a user
    let identities = try await supabase.auth.userIdentities()

    // find the google identity linked to the user
    let googleIdentity = identities.first { $0.provider == .google }

    // unlink the google identity from the user
    try await supabase.auth.unlinkIdentity(googleIdentity)
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    You can use [`currentIdentitiesOrNull()`](/docs/reference/kotlin/auth-getuseridentities) to get all the identities linked to a user. Then, call [`unlinkIdentity()`](/docs/reference/kotlin/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

    ```kotlin
    //get all identities linked to a user
    val identities = supabase.auth.currentIdentitiesOrNull() ?: emptyList()

    //find the google identity linked to the user
    val googleIdentity = identities.first { it.provider == "google" }

    //unlink the google identity from the user
    supabase.auth.unlinkIdentity(googleIdentity.identityId!!)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    You can use [`get_user_identities()`](/docs/reference/python/auth-getuseridentities) to fetch all the identities linked to a user. Then, call [`unlink_identity()`](/docs/reference/python/auth-unlinkidentity) to unlink the identity. The user needs to be logged in and have at least 2 linked identities in order to unlink an existing identity.

    ```python
    # retrieve all identities linked to a user
    response = supabase.auth.get_user_identities()

    # find the google identity linked to the user
    google_identity = next((identity for identity in response.identities if identity.provider == 'google'), None)

    # unlink the google identity from the user
    if google_identity:
        response = supabase.auth.unlink_identity(google_identity.identity_id)
    ```
  </TabPanel>
</Tabs>



## Frequently asked questions


### How to add email/password login to an OAuth account?

Call the `updateUser({ password: 'validpassword'})` to add email with password authentication to an account created with an OAuth provider (Google, GitHub, etc.).


### Can you sign up with email if already using OAuth?

If you try to create an email account after previously signing up with OAuth using the same email, you'll receive an obfuscated user response with no verification email sent. This prevents user enumeration attacks.



# Multi-Factor Authentication



Multi-factor authentication (MFA), sometimes called two-factor authentication (2FA), adds an additional layer of security to your application by verifying their identity through additional verification steps.

It is considered a best practice to use MFA for your applications.

Users with weak passwords or compromised social login accounts are prone to malicious account takeovers. These can be prevented with MFA because they require the user to provide proof of both of these:

*   Something they know.
    Password, or access to a social-login account.
*   Something they have.
    Access to an authenticator app (a.k.a. TOTP) or a mobile phone.



## Overview

Supabase Auth implements MFA via two methods: App Authenticator, which makes use of a Time based-one Time Password, and phone messaging, which makes use of a code generated by Supabase Auth.

Applications using MFA require two important flows:

1.  **Enrollment flow.**
    This lets users set up and control MFA in your app.
2.  **Authentication flow.**
    This lets users sign in using any factors after the conventional login step.

Supabase Auth provides:

*   **Enrollment API** - build rich user interfaces for adding and removing factors.
*   **Challenge and Verify APIs** - securely verify that the user has access to a factor.
*   **List Factors API** - build rich user interfaces for signing in with additional factors.

You can control access to the Enrollment API as well as the Challenge and Verify APIs via the Supabase Dashboard. A setting of `Verification Disabled` will disable both the challenge API and the verification API.

These sets of APIs let you control the MFA experience that works for you. You can create flows where MFA is optional, mandatory for all, or only specific groups of users.

Once users have enrolled or signed-in with a factor, Supabase Auth adds additional metadata to the user's access token (JWT) that your application can use to allow or deny access.

This information is represented by an [Authenticator Assurance Level](https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/), a standard measure about the assurance of the user's identity Supabase Auth has for that particular session. There are two levels recognized today:

1.  **Assurance Level 1: `aal1`**
    Means that the user's identity was verified using a conventional login method
    such as email+password, magic link, one-time password, phone auth or social
    login.
2.  **Assurance Level 2: `aal2`**
    Means that the user's identity was additionally verified using at least one
    second factor, such as a TOTP code or One-Time Password code.

This assurance level is encoded in the `aal` claim in the JWT associated with the user. By decoding this value you can create custom authorization rules in your frontend, backend, and database that will enforce the MFA policy that works for your application. JWTs without an `aal` claim are at the `aal1` level.



## Adding to your app

Adding MFA to your app involves these four steps:

1.  **Add enrollment flow.**
    You need to provide a UI within your app that your users will be able to set-up
    MFA in. You can add this right after sign-up, or as part of a separate flow in
    the settings portion of your app.
2.  **Add unenroll flow.**
    You need to support a UI through which users can see existing devices and unenroll
    devices which are no longer relevant.
3.  **Add challenge step to login.**
    If a user has set-up MFA, your app's login flow needs to present a challenge
    screen to the user asking them to prove they have access to the additional
    factor.
4.  **Enforce rules for MFA logins.**
    Once your users have a way to enroll and log in with MFA, you need to enforce
    authorization rules across your app: on the frontend, backend, API servers or
    Row-Level Security policies.

The enrollment flow and the challenge steps differ by factor and are covered on a separate page. Visit the [Phone](/docs/guides/auth/auth-mfa/phone) or [App Authenticator](/docs/guides/auth/auth-mfa/totp) pages to see how to add the flows for the respective factors. You can combine both flows and allow for use of both Phone and App Authenticator Factors.


### Add unenroll flow

The unenroll process is the same for both Phone and TOTP factors.

An unenroll flow provides a UI for users to manage and unenroll factors linked to their accounts. Most applications do so via a factor management page where users can view and unlink selected factors.

When a user unenrolls a factor, call `supabase.auth.mfa.unenroll()` with the ID of the factor. For example, call:

```js
import { createClient } from '@supabase/supabase-js'
const supabase = createClient(
  'https://your-project-id.supabase.co',
  'sb_publishable_... or anon key'
)

// ---cut---
supabase.auth.mfa.unenroll({ factorId: 'd30fd651-184e-4748-a928-0a4b9be1d429' })
```

to unenroll a factor with ID `d30fd651-184e-4748-a928-0a4b9be1d429`.


### Enforce rules for MFA logins

Adding MFA to your app's UI does not in-and-of-itself offer a higher level of security to your users. You also need to enforce the MFA rules in your application's database, APIs, and server-side rendering.

Depending on your application's needs, there are three ways you can choose to enforce MFA.

1.  **Enforce for all users (new and existing).**
    Any user account will have to enroll MFA to continue using your app.
    The application will not allow access without going through MFA first.
2.  **Enforce for new users only.**
    Only new users will be forced to enroll MFA, while old users will be encouraged
    to do so.
    The application will not allow access for new users without going through MFA
    first.
3.  **Enforce only for users that have opted-in.**
    Users that want MFA can enroll in it and the application will not allow access
    without going through MFA first.


#### Example: React

Below is an example that creates a new `UnenrollMFA` component that illustrates the important pieces of the MFA enrollment flow. Note that users can only unenroll a factor after completing the enrollment flow and obtaining an `aal2` JWT claim. Here are some points of note:

*   When the component appears on screen, the `supabase.auth.mfa.listFactors()` endpoint
    fetches all existing factors together with their details.
*   The existing factors for a user are displayed in a table.
*   Once the user has selected a factor to unenroll, they can type in the `factorId` and click **Unenroll**
    which creates a confirmation modal.

<Admonition type="note">
  Unenrolling a factor will downgrade the assurance level from `aal2` to `aal1` only after the refresh interval has lapsed. For an immediate downgrade from `aal2` to `aal1` after enrolling one will need to manually call `refreshSession()`
</Admonition>

```tsx
/**
 * UnenrollMFA shows a simple table with the list of factors together with a button to unenroll.
 * When a user types in the factorId of the factor that they wish to unenroll and clicks unenroll
 * the corresponding factor will be unenrolled.
 */
export function UnenrollMFA() {
  const [factorId, setFactorId] = useState('')
  const [factors, setFactors] = useState([])
  const [error, setError] = useState('') // holds an error message

  useEffect(() => {
    ;(async () => {
      const { data, error } = await supabase.auth.mfa.listFactors()
      if (error) {
        throw error
      }

      setFactors([...data.totp, ...data.phone])
    })()
  }, [])

  return (
    <>
      {error && <div className="error">{error}</div>}
      <tbody>
        <tr>
          <td>Factor ID</td>
          <td>Friendly Name</td>
          <td>Factor Status</td>
          <td>Phone Number</td>
        </tr>
        {factors.map((factor) => (
          <tr>
            <td>{factor.id}</td>
            <td>{factor.friendly_name}</td>
            <td>{factor.factor_type}</td>
            <td>{factor.status}</td>
            <td>{factor.phone}</td>
          </tr>
        ))}
      </tbody>
      <input type="text" value={verifyCode} onChange={(e) => setFactorId(e.target.value.trim())} />
      <button onClick={() => supabase.auth.mfa.unenroll({ factorId })}>Unenroll</button>
    </>
  )
}
```


#### Database

Your app should sufficiently deny or allow access to tables or rows based on the user's current and possible authenticator levels.

<Admonition type="caution">
  Postgres has two types of policies: permissive and restrictive. This guide uses restrictive policies. Make sure you don't omit the `as restrictive` clause.
</Admonition>


##### Enforce for all users (new and existing)

If your app falls under this case, this is a template Row Level Security policy you can apply to all your tables:

```sql
create policy "Policy name."
  on table_name
  as restrictive
  to authenticated
  using ((select auth.jwt()->>'aal') = 'aal2');
```

*   Here the policy will not accept any JWTs with an `aal` claim other than
    `aal2`, which is the highest authenticator assurance level.
*   **Using `as restrictive` ensures this policy will restrict all commands on the
    table regardless of other policies!**


##### Enforce for new users only

If your app falls under this case, the rules get more complex. User accounts created past a certain timestamp must have a `aal2` level to access the database.

```sql
create policy "Policy name."
  on table_name
  as restrictive -- very important!
  to authenticated
  using
    (array[(select auth.jwt()->>'aal')] <@ (
       select
         case
           when created_at >= '2022-12-12T00:00:00Z' then array['aal2']
           else array['aal1', 'aal2']
         end as aal
       from auth.users
       where (select auth.uid()) = id));
```

*   The policy will accept both `aal1` and `aal2` for users with a `created_at`
    timestamp prior to 12th December 2022 at 00:00 UTC, but will only accept
    `aal2` for all other timestamps.
*   The `<@` operator is PostgreSQL's ["contained in"
    operator.](https://www.postgresql.org/docs/current/functions-array.html)
*   **Using `as restrictive` ensures this policy will restrict all commands on the
    table regardless of other policies!**


##### Enforce only for users that have opted-in

Users that have enrolled MFA on their account are expecting that your
application only works for them if they've gone through MFA.

```sql
create policy "Policy name."
  on table_name
  as restrictive -- very important!
  to authenticated
  using (
    array[(select auth.jwt()->>'aal')] <@ (
      select
          case
            when count(id) > 0 then array['aal2']
            else array['aal1', 'aal2']
          end as aal
        from auth.mfa_factors
        where ((select auth.uid()) = user_id) and status = 'verified'
    ));
```

*   The policy will only accept only `aal2` when the user has at least one MFA
    factor verified.
*   Otherwise, it will accept both `aal1` and `aal2`.
*   The `<@` operator is PostgreSQL's ["contained in"
    operator.](https://www.postgresql.org/docs/current/functions-array.html)
*   **Using `as restrictive` ensures this policy will restrict all commands on the
    table regardless of other policies!**


### Server-Side Rendering

<Admonition type="tip">
  When using the Supabase JavaScript library in a server-side rendering context, make sure you always create a new object for each request! This will prevent you from accidentally rendering and serving content belonging to different users.
</Admonition>

It is possible to enforce MFA on the Server-Side Rendering level. However, this can be tricky do to well.

You can use the `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` and `supabase.auth.mfa.listFactors()` APIs to identify the AAL level of the session and any factors that are enabled for a user, similar to how you would use these on the browser.

However, encountering a different AAL level on the server may not actually be a security problem. Consider these likely scenarios:

1.  User signed-in with a conventional method but closed their tab on the MFA
    flow.
2.  User forgot a tab open for a very long time. (This happens more often than
    you might imagine.)
3.  User has lost their authenticator device and is confused about the next
    steps.

We thus recommend you redirect users to a page where they can authenticate using their additional factor, instead of rendering a HTTP 401 Unauthorized or HTTP 403 Forbidden content.


### APIs

If your application uses the Supabase Database, Storage or Edge Functions, just using Row Level Security policies will give you sufficient protection. In the event that you have other APIs that you wish to protect, follow these general guidelines:

1.  **Use a good JWT verification and parsing library for your language.**
    This will let you securely parse JWTs and extract their claims.
2.  **Retrieve the `aal` claim from the JWT and compare its value according to
    your needs.**
    If you've encountered an AAL level that can be increased, ask the user to
    continue the login process instead of logging them out.
3.  **Use the `https://<project-ref>.supabase.co/rest/v1/auth/factors` REST
    endpoint to identify if the user has enrolled any MFA factors.**
    Only `verified` factors should be acted upon.



## Frequently asked questions

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6 [&>div]:space-y-4">
  <AccordionItem header={<span className="text-foreground">How do I check when a user went through MFA?</span>} id="how-do-i-check-when-a-user-went-through-mfa">
    Access tokens issued by Supabase Auth contain an `amr` (Authentication Methods Reference) claim. It is an array of objects that indicate what authentication methods the user has used so far.

    For example, the following structure describes a user that first signed in with a password-based method, and then went through TOTP MFA 2 minutes and 12 seconds later. The entries are ordered most recent method first!

    ```json
    {
      "amr": [
        {
          "method": "totp",
          "timestamp": 1666086056
        },
        {
          "method": "password",
          "timestamp": 1666085924
        }
      ]
    }
    ```

    Use the `supabase.auth.mfa.getAuthenticatorAssuranceLevel()` method to get easy access to this information in your browser app.

    You can use this Postgres snippet in RLS policies, too:

    ```sql
    jsonb_path_query((select auth.jwt()), '$.amr[0]')
    ```

    *   [`jsonb_path_query(json, path)`](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-JSON-PROCESSING-TABLE)
        is a function that allows access to elements in a JSON object according to a
        [SQL/JSON
        path](https://www.postgresql.org/docs/current/functions-json.html#FUNCTIONS-SQLJSON-PATH).
    *   `$.amr[0]` is a SQL/JSON path expression that fetches the most recent
        authentication method in the JWT.

    Once you have extracted the most recent entry in the array, you can compare the `method` and `timestamp` to enforce stricter rules. For instance, you can mandate that access will be only be granted on a table to users who have recently signed in with a password.

    Currently recognized authentication methods are:

    *   `oauth` - any OAuth based sign in (social login).
    *   `password` - any password based sign in.
    *   `otp` - any one-time password based sign in (email code, SMS code, magic
        link).
    *   `totp` - a TOTP additional factor.
    *   `sso/saml` - any Single Sign On (SAML) method.
    *   `anonymous` - any anonymous sign in.

    The following additional claims are available when using PKCE flow:

    *   `invite` - any sign in via an invitation.
    *   `magiclink` - any sign in via magic link. Excludes logins resulting from invocation of `signUp`.
    *   `email/signup` - any login resulting from an email signup.
    *   `email_change` - any login resulting from a change in email.

    More authentication methods will be added over time as we increase the number of authentication methods supported by Supabase.
  </AccordionItem>
</Accordion>



---
**Navigation:** [← Previous](./26-pg_stat_statements-query-performance-monitoring.md) | [Index](./index.md) | [Next →](./28-send-emails-with-custom-smtp.md)
