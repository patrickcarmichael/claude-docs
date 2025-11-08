**Navigation:** [← Previous](./20-custom-auth-emails-with-react-email-and-resend.md) | [Index](./index.md) | [Next →](./22-connection-management.md)

# Production Checklist



After developing your project and deciding it's Production Ready, you should run through this checklist to ensure that your project:

*   is secure
*   won't falter under the expected load
*   remains available whilst in production



## Security

*   Ensure RLS is enabled
    *   Tables that do not have RLS enabled with reasonable policies allow any client to access and modify their data. This is unlikely to be what you want in the majority of cases.
    *   [Learn more about RLS](/docs/guides/database/postgres/row-level-security).
*   Enable replication on tables containing sensitive data by enabling Row Level Security (RLS) and setting row security policies:
    *   Go to the Authentication > Policies page in the Supabase Dashboard to enable RLS and create security policies.
    *   Go to the Database > Publications page in the Supabase Dashboard to manage replication tables.
*   Turn on [SSL Enforcement](/docs/guides/platform/ssl-enforcement) (see: [dashboard](/dashboard/project/_/auth/policies))
*   Enable [Network Restrictions](/docs/guides/platform/network-restrictions) for your database (see: [dashboard](/dashboard/project/_/database/settings#network-restrictions)).
*   Ensure that your Supabase Account is protected with multi-factor authentication (MFA).
    *   If using a GitHub signin, [enable 2FA on GitHub](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication). Since your GitHub account gives you administrative rights to your Supabase org, you should protect it with a strong password and 2FA using a U2F key or a TOTP app.
    *   If using email+password signin, set up [MFA for your Supabase account](/docs/guides/platform/multi-factor-authentication#enable-mfa).
*   Enable [MFA enforcement on your organization](/docs/guides/platform/network-restrictions). This ensures all users must have a valid MFA backed session to interact with organization and project resources.
*   Consider [adding multiple owners on your Supabase org](/dashboard/org/_/team). This ensures that if one of the owners is unreachable or loses access to their account, you still have Owner access to your org.
*   Ensure email confirmations are [enabled](/dashboard/project/_/auth/providers) in the `Settings > Auth` page.
*   Ensure that you've [set the expiry](/dashboard/project/_/auth/providers) for one-time passwords (OTPs) to a reasonable value that you are comfortable with. We recommend setting this to 3600 seconds (1 hour) or lower.
*   Increase the length of the OTP if you need a higher level of entropy.
*   If your application requires a higher level of security, consider setting up [multi-factor authentication](/docs/guides/auth/auth-mfa) (MFA) for your users.
*   Use a custom SMTP server for auth emails so that your users can see that the mails are coming from a trusted domain (preferably the same domain that your app is hosted on). Grab SMTP credentials from any major email provider such as SendGrid, AWS SES, etc.
*   Think hard about how *you* would abuse your service as an attacker, and mitigate.
*   Review these [common cybersecurity threats](https://auth0.com/docs/security/prevent-threats).
*   Check and review issues in your database using [Security Advisor](/dashboard/project/_/database/security-advisor).



## Performance

*   Ensure that you have suitable indices to cater to your common query patterns
    *   [Learn more about indexes in Postgres](https://www.enterprisedb.com/postgres-tutorials/overview-postgresql-indexes).
    *   `pg_stat_statements` can help you [identify hot or slow queries](https://www.virtual-dba.com/blog/postgresql-performance-identifying-hot-and-slow-queries/).
*   Perform load testing (preferably on a staging env)
    *   Tools like [k6](https://k6.io/) can simulate traffic from many different users.
*   Upgrade your database if you require more resources. If you need anything beyond what is listed, contact [enterprise@supabase.io](mailto:enterprise@supabase.io).
*   If you are expecting a surge in traffic (for a big launch) and are on a Team or Enterprise Plan, [contact support](/dashboard/support/new) with more details about your launch and we'll help keep an eye on your project.
*   If you expect your database size to be > 4 GB, [enable](/dashboard/project/_/settings/addons?panel=pitr) the Point in Time Recovery (PITR) add-on. Daily backups can take up resources from your database when the backup is in progress. PITR is more resource efficient, since only the changes to the database are backed up.
*   Check and review issues in your database using [Performance Advisor](/dashboard/project/_/database/performance-advisor).



## Availability

*   Use your own SMTP credentials so that you have full control over the deliverability of your transactional auth emails (see Settings > Auth)
    *   you can grab SMTP credentials from any major email provider such as SendGrid, AWS SES, etc. You can refer to our [SMTP guide](/docs/guides/auth/auth-smtp) for more details.
    *   The default rate limit for auth emails when using a custom SMTP provider is 30 new users per hour, if doing a major public announcement you will likely require more than this.
*   Applications on the Free Plan that exhibit extremely low activity in a 7 day period may be paused by Supabase to save on server resources.
    *   You can restore paused projects from the Supabase dashboard.
    *   Upgrade to Pro to guarantee that your project will not be paused for inactivity.
*   Database backups are not available for download on the Free Plan.
    *   You can set up your own backup systems using tools like [pg\_dump](https://www.postgresqltutorial.com/postgresql-backup-database/) or [wal-g](https://github.com/wal-g/wal-g).
    *   Nightly backups for Pro Plan projects are available on the Supabase dashboard for up to 7 days.
    *   Point in Time Recovery (PITR) allows a project to be backed up at much shorter intervals. This provides users an option to restore to any chosen point of up to seconds in granularity. In terms of Recovery Point Objective (RPO), Daily Backups would be suitable for projects willing to lose up to 24 hours worth of data. If a lower RPO is required, enable PITR.
*   Supabase Projects use disks that offer 99.8-99.9% durability by default.
    *   Use Read Replicas if you require availability resilience to a disk failure event
    *   Use PITR if you require durability resilience to a disk failure event
*   Upgrading to the Supabase Pro Plan will give you [access to our support team](/dashboard/support/new).



## Rate limiting, resource allocation, & abuse prevention

*   Supabase employs a number of safeguards against bursts of incoming traffic to prevent abuse and help maximize stability across the platform
    *   If you're on a Team or Enterprise Plan and expect high load events, such as production launches, heavy load testing, or prolonged high resource usage, open a ticket via the [support form](https://supabase.help) for help. Provide at least 2 weeks notice.


### Auth rate limits

*   The table below shows the rate limit quotas on the following authentication endpoints. You can configure the auth rate limits for your project [here](/dashboard/project/_/auth/rate-limits).

| Endpoint                                         | Path                                                           | Limited By               | Rate Limit                                                                                                                                                                                                                                         |
| ------------------------------------------------ | -------------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All endpoints that send emails                   | `/auth/v1/signup` `/auth/v1/recover` `/auth/v1/user`\[^1]      | Sum of combined requests | As of 3 Sep 2024, this has been updated to <SharedData data="config">auth.rate\_limits.email.inbuilt\_smtp\_per\_hour.value</SharedData> emails per hour. You can only change this with your own [custom SMTP setup](/docs/guides/auth/auth-smtp). |
| All endpoints that send One-Time-Passwords (OTP) | `/auth/v1/otp`                                                 | Sum of combined requests | Defaults to 360 OTPs per hour. Is customizable.                                                                                                                                                                                                    |
| Send OTPs or magic links                         | `/auth/v1/otp`                                                 | Last request             | Defaults to 60 seconds window before a new request is allowed. Is customizable.                                                                                                                                                                    |
| Signup confirmation request                      | `/auth/v1/signup`                                              | Last request             | Defaults to 60 seconds window before a new request is allowed. Is customizable.                                                                                                                                                                    |
| Password Reset Request                           | `/auth/v1/recover`                                             | Last request             | Defaults to 60 seconds window before a new request is allowed. Is customizable.                                                                                                                                                                    |
| Verification requests                            | `/auth/v1/verify`                                              | IP Address               | 360 requests per hour (with bursts up to 30 requests)                                                                                                                                                                                              |
| Token refresh requests                           | `/auth/v1/token`                                               | IP Address               | 1800 requests per hour (with bursts up to 30 requests)                                                                                                                                                                                             |
| Create or Verify an MFA challenge                | `/auth/v1/factors/:id/challenge` `/auth/v1/factors/:id/verify` | IP Address               | 15 requests per minute (with bursts up to 30 requests)                                                                                                                                                                                             |
| Anonymous sign-ins                               | `/auth/v1/signup`\[^2]                                         | IP Address               | 30 requests per hour (with bursts up to 30 requests)                                                                                                                                                                                               |


### Realtime quotas

*   Review the [Realtime quotas](/docs/guides/realtime/quotas).
*   If you need quotas increased you can always [contact support](/dashboard/support/new).


### Abuse prevention

*   Supabase provides CAPTCHA protection on the signup, sign-in and password reset endpoints. Refer to [our guide](/docs/guides/auth/auth-captcha) on how to protect against abuse using this method.


### Email link validity

*   When working with enterprise systems, email scanners may scan and make a `GET` request to the reset password link or sign up link in your email. Since links in Supabase Auth are single use, a user who opens an email post-scan to click on a link will receive an error. To get around this problem,
    consider altering the email template to replace the original magic link with a link to a domain you control. The domain can present the user with a "Sign-in" button which redirect the user to the original magic link URL when clicked.

*   When using a custom SMTP service, some services might have link tracking enabled which may overwrite or disform the email confirmation links sent by Supabase Auth. To prevent this from happening, we recommend that you disable link tracking when using a custom SMTP service.



## Subscribe to Supabase status page

Stay informed about Supabase service status by subscribing to the [Status Page](https://status.supabase.com/). We recommend setting up Slack notifications through an RSS feed to ensure your team receives timely updates about service status changes.


### Setting up Slack notifications

1.  Install the RSS app in Slack:

    *   Visit the [RSS app page](https://slack.com/marketplace/A0F81R7U7-rss) in the Slack marketplace
    *   Click `Add to Slack` if not already installed
    *   Otherwise you will get straight to next step, no need to reinstall the app

2.  Configure the Supabase status feed:

    *   Create a channel (e.g., `#supabase-status-alerts`) for status updates
    *   On the [RSS app page](https://slack.com/marketplace/A0F81R7U7-rss) go to *Add a Feed* section and set Feed URL to `https://status.supabase.com/history.rss`
    *   Select your designated channel and click "Subscribe to this feed"

Once configured, your team will receive automatic notifications in Slack whenever the Supabase Status Page is updated.

For detailed setup instructions, see the [Add RSS feeds to Slack](https://slack.com/intl/en-nz/help/articles/218688467-Add-RSS-feeds-to-Slack).



## Next steps

This checklist is always growing so be sure to check back frequently, and also feel free to suggest additions and amendments by making a PR on [GitHub](https://github.com/supabase/supabase).



# Managing Environments

Manage multiple environments using Database Migrations and GitHub Actions.

This guide shows you how to set up your local Supabase development environment that integrates with GitHub Actions to automatically test and release schema changes to staging and production Supabase projects.

<Image
  alt="Diagram showing a possible environment setup for Supabase development. There are 3 branches and 3 corresponding databases: feature branch and local database, develop branch and staging database, and main branch and production database."
  src={{
    light: '/docs/img/local-dev-environment--light.svg',
    dark: '/docs/img/local-dev-environment.svg',
  }}
  zoomable
/>



## Set up a local environment

The first step is to set up your local repository with the Supabase CLI:

```bash
supabase init
```

You should see a new `supabase` directory. Then you need to link your local repository with your Supabase project:

```bash
supabase login
supabase link --project-ref $PROJECT_ID
```

You can get your `$PROJECT_ID` from your project's dashboard URL:

```
https://supabase.com/dashboard/project/<project-id>
```

If you're using an existing Supabase project, you might have made schema changes through the Dashboard.
Run the following command to pull these changes before making local schema changes from the CLI:

```sql
supabase db pull
```

This command creates a new migration in `supabase/migrations/<timestamp>_remote_schema.sql` which reflects the schema changes you have made previously.

Now commit your local changes to Git and run the local development setup:

```bash
git add .
git commit -m "init supabase"
supabase start
```

You are now ready to develop schema changes locally and create your first migration.



## Create a new migration

There are two ways to make schema changes:

1.  Manual migration: Write DDL statements manually into a migration file
2.  Auto schema diff: Make changes through Studio UI and auto generate a schema diff


### Manual migration

Create a new migration script by running:

```bash
supabase migration new new_employee
```

You should see a new file created: `supabase/migrations/<timestamp>_new_employee.sql`. You can then write SQL statements in this script using a text editor:

```sql
create table public.employees (
  id integer primary key generated always as identity,
  name text
);
```

Apply the new migration to your local database:

```bash
supabase db reset
```

This command recreates your local database from scratch and applies all migration scripts under `supabase/migrations` directory. Now your local database is up to date.

<Admonition type="tip">
  The new migration command also supports stdin as input. This allows you to pipe in an existing script from another file or stdout:

  `supabase migration new new_employee < create_employees_table.sql`
</Admonition>


### Auto schema diff

Unlike manual migrations, auto schema diff creates a new migration script from changes **already** applied to your local database.

Create an `employees` table under the `public` schema using Studio UI, accessible at [localhost:54323](http://localhost:54323/) by default.

Next, generate a schema diff by running the following command:

```bash
supabase db diff -f new_employee
```

You should see that a new file `supabase/migrations/<timestamp>_new_employee.sql` is created. Open the file and verify that the generated DDL statements are the same as below.

```sql
-- This script was generated by the Schema Diff utility in pgAdmin 4
-- For the circular dependencies, the order in which Schema Diff writes the objects is not very sophisticated
-- and may require manual changes to the script to ensure changes are applied in the correct order.
-- Please report an issue for any failure with the reproduction steps.

CREATE TABLE IF NOT EXISTS public.employees
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name text COLLATE pg_catalog."default",
    CONSTRAINT employees_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.employees
    OWNER to postgres;

GRANT ALL ON TABLE public.employees TO anon;

GRANT ALL ON TABLE public.employees TO authenticated;

GRANT ALL ON TABLE public.employees TO postgres;

GRANT ALL ON TABLE public.employees TO service_role;
```

You may notice that the auto-generated migration script is more verbose than the manually written one.
This is because the default schema diff tool does not account for default privileges added by the initial schema.

Commit the new migration script to git and you are ready to deploy.

<Admonition type="tip">
  Alternatively, you may pass in the `--use-migra` experimental flag to generate a more concise migration using [`migra`](https://github.com/djrobstep/migra).

  Without the `-f` file flag, the output is written to stdout by default.

  `supabase db diff --use-migra`
</Admonition>



## Deploy a migration

In a production environment, we recommend using a CI/CD pipeline to deploy new migrations with GitHub Actions rather than deploying from your local machine.

<Image
  alt="Diagram showing a possible environment setup for Supabase development. There are 3 branches and 3 corresponding databases: feature branch and local database, develop branch and staging database, and main branch and production database."
  src={{
    light: '/docs/img/local-dev-environment--light.svg',
    dark: '/docs/img/local-dev-environment.svg',
  }}
/>

This example uses two Supabase projects, one for production and one for staging.

Prepare your environments by:

*   Creating separate Supabase projects for staging and production
*   Pushing your git repository to GitHub and enabling GitHub Actions

<Admonition type="caution">
  You need a *new* project for staging. A project which has already been modified to reflect the production project's schema can't be used because the CLI would reapply these changes.
</Admonition>


### Configure GitHub Actions

The Supabase CLI requires a few environment variables to run in non-interactive mode.

*   `SUPABASE_ACCESS_TOKEN` is your personal access token
*   `SUPABASE_DB_PASSWORD` is your project specific database password
*   `SUPABASE_PROJECT_ID` is your project specific reference string

We recommend adding these as [encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to your GitHub Actions runners.

Create the following files inside the `.github/workflows` directory:

<Tabs scrollable size="small" type="underlined" defaultActiveId="ci" queryGroup="environment">
  <TabPanel id="ci" label="ci.yaml">
    ```yaml .github/workflows/ci.yml
    name: CI

    on:
      pull_request:
      workflow_dispatch:

    jobs:
      test:
        runs-on: ubuntu-latest

        steps:
          - uses: actions/checkout@v4

          - uses: supabase/setup-cli@v1
            with:
              version: latest

          - name: Start Supabase local development setup
            run: supabase db start

          - name: Verify generated types are checked in
            run: |
              supabase gen types typescript --local > types.gen.ts
              if ! git diff --ignore-space-at-eol --exit-code --quiet types.gen.ts; then
                echo "Detected uncommitted changes after build. See status below:"
                git diff
                exit 1
              fi
    ```
  </TabPanel>

  <TabPanel id="staging" label="staging.yaml">
    ```yaml .github/workflows/staging.yml
    name: Deploy Migrations to Staging

    on:
      push:
        branches:
          - develop
      workflow_dispatch:

    jobs:
      deploy:
        runs-on: ubuntu-latest

        env:
          SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
          SUPABASE_DB_PASSWORD: ${{ secrets.STAGING_DB_PASSWORD }}
          SUPABASE_PROJECT_ID: ${{ secrets.STAGING_PROJECT_ID }}

        steps:
          - uses: actions/checkout@v4

          - uses: supabase/setup-cli@v1
            with:
              version: latest

          - run: supabase link --project-ref $SUPABASE_PROJECT_ID
          - run: supabase db push
    ```
  </TabPanel>

  <TabPanel id="production" label="production.yaml">
    ```yaml .github/workflows/production.yml
    name: Deploy Migrations to Production

    on:
      push:
        branches:
          - main
      workflow_dispatch:

    jobs:
      deploy:
        runs-on: ubuntu-latest

        env:
          SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
          SUPABASE_DB_PASSWORD: ${{ secrets.PRODUCTION_DB_PASSWORD }}
          SUPABASE_PROJECT_ID: ${{ secrets.PRODUCTION_PROJECT_ID }}

        steps:
          - uses: actions/checkout@v4

          - uses: supabase/setup-cli@v1
            with:
              version: latest

          - run: supabase link --project-ref $SUPABASE_PROJECT_ID
          - run: supabase db push
    ```
  </TabPanel>
</Tabs>

The full example code is available in the [demo repository](https://github.com/supabase/supabase-action-example).

Commit these files to git and push to your `main` branch on GitHub. Update these environment variables to match your Supabase projects:

*   `SUPABASE_ACCESS_TOKEN`
*   `PRODUCTION_PROJECT_ID`
*   `PRODUCTION_DB_PASSWORD`
*   `STAGING_PROJECT_ID`
*   `STAGING_DB_PASSWORD`

When configured correctly, your repository will have CI and Release workflows that trigger on new commits pushed to `main` and `develop` branches.

![Correctly configured repo](/docs/img/guides/cli/ci-main.png)


### Open a PR with new migration

Follow the [migration steps](#create-a-new-migration) to create a `supabase/migrations/<timestamp>_new_employee.sql` file.

Checkout a new branch `feat/employee` from `develop` , commit the migration file, and push to GitHub.

```bash
git checkout -b feat/employee
git add supabase/migrations/<timestamp>_new_employee.sql
git commit -m "Add employee table"
git push --set-upstream origin feat/employee
```

Open a PR from `feat/employee` to the `develop` branch to see that the CI workflow has been triggered.

Once the test error is resolved, merge this PR and watch the deployment in action.


### Release to production

After verifying your staging project has successfully migrated, create another PR from `develop` to `main` and merge it to deploy the migration to the production project.

The `release` job applies all new migration scripts merged in `supabase/migrations` directory to a linked Supabase project. You can control which project the job links to via `PROJECT_ID` environment variable.



## Troubleshooting


### Sync production project to staging

When setting up a new staging project, you might need to sync the initial schema with migrations previously applied to the production project.

One way is to leverage the Release workflow:

*   Create a new branch `develop` and choose `main` as the branch source
*   Push the `develop` branch to GitHub

The GitHub Actions runner will deploy your existing migrations to the staging project.

Alternatively, you can also apply migrations through your local CLI to a linked remote database.

```sql
supabase db push
```

Once pushed, check that the migration version is up to date for both local and remote databases.

```sql
supabase migration list
```


### Permission denied on `db pull`

If you have been using Supabase hosted projects for a long time, you might encounter the following permission error when executing `db pull`.

```bash
Error: Error running pg_dump on remote database: pg_dump: error: query failed: ERROR:  permission denied for table _type

pg_dump: error: query was: LOCK TABLE "graphql"."_type" IN ACCESS SHARE MODE
```

To resolve this error, you need to grant `postgres` role permissions to `graphql` schema. You can do that by running the following query from Supabase dashboard's SQL Editor.

```sql
grant all on all tables in schema graphql to postgres, anon, authenticated, service_role;
grant all on all functions in schema graphql to postgres, anon, authenticated, service_role;
grant all on all sequences in schema graphql to postgres, anon, authenticated, service_role;
```


### Permission denied on `db push`

If you created a table through Supabase dashboard, and your new migration script contains `ALTER TABLE` statements, you might run into permission error when applying them on staging or production databases.

```bash
ERROR: must be owner of table employees (SQLSTATE 42501); while executing migration <timestamp>
```

This is because tables created through Supabase dashboard are owned by `supabase_admin` role while the migration scripts executed through CLI are under `postgres` role.

One way to solve this is to reassign the owner of those tables to `postgres` role. For example, if your table is named `users` in the public schema, you can run the following command to reassign owner.

```sql
ALTER TABLE users OWNER TO postgres;
```

Apart from tables, you also need to reassign owner of other entities using their respective commands, including [types](https://www.postgresql.org/docs/current/sql-altertype.html), [functions](https://www.postgresql.org/docs/current/sql-alterroutine.html), and [schemas](https://www.postgresql.org/docs/current/sql-alterschema.html).


### Rebasing new migrations

Sometimes your teammate may merge a new migration file to git main branch, and now you need to rebase your local schema changes on top.

We can handle this scenario gracefully by renaming your old migration file with a new timestamp.

```bash
git pull
supabase migration new dev_A

# Assume the new file is: supabase/migrations/<t+2>_dev_A.sql
mv <time>_dev_A.sql <t+2>_dev_A.sql
supabase db reset
```

In case [`reset`](/docs/reference/cli/usage#supabase-db-reset) fails, you can manually resolve conflicts by editing `<t+2>_dev_A.sql` file.

Once validated locally, commit your changes to Git and push to GitHub.



# Maturity Model



Supabase is great for building something very fast *and* for scaling up. However, it's important to note that as your application matures and your team expands, the practices you use for managing an application in production should not be the same as the practices you used for prototyping.



## Prototyping

The Dashboard is a quick and easy tool for building applications while you are prototyping. That said, we strongly recommend using [Migrations](/docs/guides/deployment/database-migrations) to manage your database changes. You can use our CLI to [capture any changes](/docs/reference/cli/supabase-db-diff) you have made on the Dashboard so that you can commit them a version control system, like git.



## Collaborating

As soon as you start collaborating with team members, all project changes should be in version control. At this point we strongly recommend moving away from using the Dashboard for schema changes. Use migrations to manage your database, and check them into your version control system to track every change.

Resources:

*   [Database migrations](/docs/guides/deployment/database-migrations)
*   [Managing access on the Dashboard](/docs/guides/platform/access-control)
*   [PGAudit for Postgres](/docs/guides/database/extensions/pgaudit)



## In production

Once your application is live, you should never change your database using the Dashboard - everything should be done with [Migrations](/docs/guides/cli/managing-environments#create-a-new-migration). Some other important things to consider at this point include:

*   The Dashboard has various [access levels](/docs/guides/platform/access-control) that can prevent changes being made via the UI.
*   Design a [safe workflow](/docs/guides/platform/shared-responsibility-model#you-decide-your-own-workflow) for managing your database. We strongly recommend running [multiple environments](/docs/guides/cli/managing-environments) as part of your development workflow (`local` -> `staging` -> `prod`).
*   Do not share any production passwords with your team, *especially* your `postgres` password. All changes should be made via version-controlled migrations which run via a bastion host or a CI platform (like [GitHub Actions](/docs/guides/cli/managing-environments#configure-github-actions). If you use GitHub Actions, use [approval workflows](https://docs.github.com/en/actions/managing-workflow-runs/reviewing-deployments) to prevent any migrations being run accidentally.
*   Restrict production access to your database using [Network Restrictions](/docs/guides/platform/network-restrictions).
*   As your database to grows, we strongly recommend moving to [Point-in-Time Recovery](/docs/guides/platform/backups#point-in-time-recovery). This is safer and has less impact on your database performance during maintenance windows.
*   Read the [Production Checklist](/docs/guides/platform/going-into-prod) and familiarize your team with the [Shared Responsibilities](/docs/guides/platform/shared-responsibility-model) between your organization and Supabase.

Resources:

*   [Database migrations](/docs/guides/deployment/database-migrations)
*   [Managing access on the Dashboard](/docs/guides/platform/access-control)
*   [PGAudit for Postgres](/docs/guides/database/extensions/pgaudit)
*   [Managing environments](/docs/guides/cli/managing-environments)



## Enterprise

For a more secure setup, consider running your workload across several organizations. It's a common pattern to have a Production organization which is restricted to only those team members who are qualified to have direct access to production databases.

Reach out to [growth](https://forms.supabase.com/enterprise) if you need help designing a secure development workflow for your organization.



# Shared Responsibility Model



Running databases is a shared responsibility between you and Supabase. There are some things that we can take care of for you, and some things that you are responsible for. This is by design: we want to give you the freedom to use your database however you want. While we *could* put many more restrictions in place to ensure that you can’t do anything wrong, you will eventually find those restrictions prohibitive.

<Image
  alt="Diagram showing the shared responsibility model between Supabase and the customer. The customer is responsible for Application architecture and implementation, information and data, the database schema and user management. The responsibility for API rate-limiting, Postgres security controls, upgrades, performance tuning and resource allocation is shared. Supabase is responsible for Postgres backups and observability, operating system maintenance, infrastructure and the monitoring and security thereof."
  src={{
    light: '/docs/img/platform/shared-responsibility-model--light.png',
    dark: '/docs/img/platform/shared-responsibility-model--dark.png',
  }}
  zoomable
/>

To summarize, you are always responsible for:

*   Your Supabase account
*   Access management (Supabase account, database, tables, etc)
*   Data
*   Applying security controls

Generally, we aim to reduce your burden of managing infrastructure and knowing about Postgres internals, minimizing configuration as much as we can. Here are a few things that you should know:



## You share the security responsibility

We give you full access to the database. If you share that access with other people (either people on your team, or the public in general) then it is your responsibility to ensure that the access levels you provide are correctly managed.

If you have an inexperienced member on your team, then you probably shouldn’t give them access to Production. You should set internal workflows around what they should and should not be able to do, with restricted access to avoid anything that might be deemed dangerous.

You are also responsible for ensuring that tables with sensitive data have the right level of access. You are also responsible for managing your database secrets and API keys, storing them safely in an encrypted store.

Supabase provides controls for [securing your data](/docs/guides/database/secure-data), and it is recommended that you always apply [Row Level Security](/docs/guides/database/postgres/row-level-security) (RLS).

We will also provide you with security alerts through [Security Advisor](/dashboard/project/_/database/security-advisor) and applying the recommendations are your responsibility.



## You decide your own workflow

There are *many* ways to work with Supabase.

You can use our Dashboard, our client libraries, external tools like Prisma and Drizzle, or migration tools like our CLI, Flyway, Sqitch, and anything else that is Postgres-compatible. You can develop directly on your database while you're getting started, run migrations from [local to production](/docs/guides/getting-started/local-development), or you can use [multiple environments](/docs/guides/cli/managing-environments).

None of these are right or wrong. It depends on the stage of your project. You *definitely* shouldn’t be developing on your database directly when you’re in production - but that’s absolutely fine when you’re prototyping and don’t have users.



## You are responsible for your application architecture

Supabase isn't a silver-bullet for bad architectural decisions. A poorly designed database will run poorly, no matter where it’s hosted.

You can get away with a poorly-designed database for a while by adding compute. After a while, things will start to break. The database schema is the area you want to spend *the most* time thinking about. That’s the benefit of Supabase - you can spend more time designing a scalable database system and less time thinking about the mundane tasks like implementing CRUD APIs.

If you don’t want to implement logic inside your database, that is 100% fine. You can use *any* tools which work with Postgres.



## You are responsible for third-party services

Supabase offers a lot of opportunities for flexibly integrating with third-party services, such as:

*   OAuth and SAML login providers
*   SMTP and SMS sending APIs
*   Calls to external APIs within Postgres functions or triggers
*   Calls to external APIs within Edge Functions

You are free to use and integrate with any service, but you're also responsible for ensuring that the performance, availability, and security of the services you use match up with your application's requirements. We do not monitor for outages or performance issues within integrations with third-party services. Depending on the implementation, an issue with such an integration could also result in performance degradation or an outage for your Supabase project.

If your application architecture relies on such integrations, you should monitor the relevant logs and metrics to ensure optimal performance.



## You choose your level of comfort with Postgres

Our goal at Supabase is to make *all* of Postgres easy to use. That doesn’t mean you have to use all of it. If you’re a Postgres veteran, you’ll probably love the tools that we offer. If you’ve never used Postgres before, then start smaller and grow into it. If you just want to treat Postgres like a simple table-store, that’s perfectly fine.



## You are in control of your database

Supabase places very few guard-rails around your database. That gives you a lot of control, but it also means you can break things. ”Break” is used liberally here. It refers to any situation that affects your application because of the way you're using the database.

You are responsible for using best-practices to optimize and manage your database: adding indexes, adding filters on large queries, using caching strategies, optimizing your database queries, and managing connections to the database.

You are responsible of provisioning enough compute to run the workload that your application requires. The Supabase Dashboard provides [observability tooling](/dashboard/project/_/reports/database) to help with this.



## Before going to production

We recommend reviewing and applying the recommendations offered in our [Production Checklist](/docs/guides/platform/going-into-prod). This checklist covers the responsibilities discussed here and a few additional general production readiness best practices.



## SOC 2 and compliance

Supabase provides a SOC 2 compliant environment for hosting and managing sensitive data. We recommend reviewing the [SOC 2 compliance responsibilities document](/docs/guides/security/soc-2-compliance) alongside the aforementioned production checklist.



## Managing healthcare data

You can use Supabase to store and process Protected Health Information (PHI). You are responsible for the following

*   Signing a Business Associate Agreement (BAA) with Supabase. Submit a [HIPAA add-on request](https://forms.supabase.com/hipaa2) to get started. You will need to be at least on the [Team Plan](/pricing) to sign a BAA with us.
*   [Marking specific projects as HIPAA projects](/docs/guides/platform/hipaa-projects) and addressing security issues raised by the advisor.
*   Ensuring [MFA is enabled](/docs/guides/platform/multi-factor-authentication) on all Supabase accounts.
    *   [Enforce MFA](/docs/guides/platform/org-mfa-enforcement) as a requirement to access the organization
*   Enabling [Point in Time Recovery](/docs/guides/platform/backups#point-in-time-recovery) which requires at least a [small compute add-on](/docs/guides/platform/compute-add-ons).
*   Turning on [SSL Enforcement](/docs/guides/platform/ssl-enforcement).
*   Enabling [Network Restrictions](/docs/guides/platform/network-restrictions).
*   Complying with encryption requirements in the HIPAA Security Rule. Data is encrypted at rest and in transit by Supabase. You can consider encrypting the data at your application layer.
*   Not storing PHI in [public Storage buckets](/docs/guides/storage/buckets/fundamentals#public-buckets).
*   Not [transferring projects](/docs/guides/platform/project-transfer) to a non-HIPAA organization.

For more information on the shared responsibilities and rules under HIPAA, review the [HIPAA compliance responsibilities document](/docs/guides/security/hipaa-compliance).



# Configuration

Configure your Supabase branches using configuration as code

This guide covers how to configure your Supabase branches, using the `config.toml` file. In one single file, you can configure all your branches, including branch settings and secrets.



## Branch configuration with remotes

When Branching is enabled, your `config.toml` settings automatically sync to all ephemeral branches through a one-to-one mapping between your Git and Supabase branches.


### Basic configuration

To update configuration for a Supabase branch, modify `config.toml` and push to git. The Supabase integration will detect the changes and apply them to the corresponding branch.


### Remote-specific configuration

For persistent branches that need specific settings, you can use the `[remotes]` block in your `config.toml`. Each remote configuration must reference an existing project ID.

Here's an example of configuring a separate seed script for a staging environment:

```toml
[remotes.staging]
project_id = "your-project-ref"

[remotes.staging.db.seed]
enabled = true
sql_paths = ["./seeds/staging.sql"]
```

Since the `project_id` field must reference an existing branch, you need to create the persistent branch before adding its configuration. Use the CLI to create a persistent branch first:

```bash
supabase --experimental branches create --persistent

# Do you want to create a branch named develop? [Y/n]
```

<Admonition type="tip">
  To retrieve the project ID for an existing branch, use the `branches list` command:

  ```bash
  supabase --experimental branches list
  ```

  This will display a table showing all your branches with their corresponding project ID.
  Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.
</Admonition>


### Configuration merging

When merging a PR into a persistent branch, the Supabase integration:

1.  Checks for configuration changes
2.  Logs the changes
3.  Applies them to the target remote

If no remote is declared or the project ID is incorrect, the configuration step is skipped.


### Available configuration options

All standard configuration options are available in the `[remotes]` block. This includes:

*   Database settings
*   API configurations
*   Authentication settings
*   Edge Functions configuration
*   And more

You can use this to maintain different configurations for different environments while keeping them all in version control.



## Managing secrets for branches

For sensitive configuration like SMTP credentials or API keys, you can use the Supabase CLI to manage secrets for your branches. This is especially useful for custom SMTP setup or other services that require secure credentials.

To set secrets for a persistent branch:

```bash

# Set secrets from a .env file
supabase secrets set --env-file ./supabase/.env


# Or set individual secrets
supabase secrets set SMTP_HOST=smtp.example.com
supabase secrets set SMTP_USER=your-username
supabase secrets set SMTP_PASSWORD=your-password
```

These secrets will be available to your branch's services and can be used in your configuration. For example, in your `config.toml`:

```toml
[auth.smtp]
host = "env(SMTP_HOST)"
user = "env(SMTP_USER)"
password = "env(SMTP_PASSWORD)"
```

<Admonition type="note" label="Secrets are branch-specific">
  Secrets set for one branch are not automatically available in other branches. You'll need to set them separately for each branch that needs them.
</Admonition>


### Using dotenvx for git-based workflow

For managing environment variables across different branches, you can use [dotenvx](https://dotenvx.com/) to securely manage your configurations. This approach is particularly useful for teams working with Git branches and preview deployments.


#### Environment file structure

Following the conventions used in the [example repository](https://github.com/supabase/supabase/blob/master/examples/slack-clone/nextjs-slack-clone-dotenvx/README.md), environments are configured using dotenv files in the `supabase` directory:

| File            | Environment | `.gitignore` it? | Encrypted |
| --------------- | ----------- | ---------------- | --------- |
| .env.keys       | All         | Yes              | No        |
| .env.local      | Local       | Yes              | No        |
| .env.production | Production  | No               | Yes       |
| .env.preview    | Branches    | No               | Yes       |
| .env            | Any         | Maybe            | Yes       |


#### Setting up encrypted secrets

1.  Generate key pair and encrypt your secrets:

```bash
npx @dotenvx/dotenvx set SUPABASE_AUTH_EXTERNAL_GITHUB_SECRET "<your-secret>" -f supabase/.env.preview
```

This creates a new encryption key in `supabase/.env.preview` and a new decryption key in `supabase/.env.keys`.

2.  Update project secrets:

```bash
npx supabase secrets set --env-file supabase/.env.keys
```

3.  Choose your configuration approach in `config.toml`:

Option A: Use encrypted values directly:

```toml
[auth.external.github]
enabled = true
secret = "encrypted:<encrypted-value>"
```

Option B: Use environment variables:

```toml
[auth.external.github]
enabled = true
client_id = "env(SUPABASE_AUTH_EXTERNAL_GITHUB_CLIENT_ID)"
secret = "env(SUPABASE_AUTH_EXTERNAL_GITHUB_SECRET)"
```

<Admonition type="note" label="Secret fields">
  The `encrypted:` syntax only works for designated "secret" fields in the configuration (like `secret` in auth providers). Using encrypted values in other fields will not be automatically decrypted and may cause issues. For non-secret fields, use environment variables with the `env()` syntax instead.
</Admonition>


#### Using with preview branches

When you commit your `.env.preview` file with encrypted values, the branching executor will automatically retrieve and use these values when deploying your branch. This allows you to maintain different configurations for different branches while keeping sensitive information secure.



## Configuration examples


### Multi-environment setup

Here's an example of a complete multi-environment configuration:

```toml

# Default configuration for all branches
[api]
enabled = true
port = 54321
schemas = ["public", "storage", "graphql_public"]

[db]
port = 54322
pool_size = 10


# Staging-specific configuration
[remotes.staging]
project_id = "staging-project-ref"

[remotes.staging.api]
max_rows = 1000

[remotes.staging.db.seed]
sql_paths = ["./seeds/staging.sql"]


# Production-specific configuration
[remotes.production]
project_id = "prod-project-ref"

[remotes.production.api]
max_rows = 500

[remotes.production.db]
pool_size = 25
```

<Admonition type="tip">
  To retrieve the project ID for an existing branch, use the `branches list` command:

  ```bash
  supabase --experimental branches list
  ```

  This will display a table showing all your branches with their corresponding project ID.
  Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.
</Admonition>


### Feature branch configuration

For feature branches that need specific settings:

```toml
[remotes.feature-oauth]
project_id = "feature-branch-ref"

[remotes.feature-oauth.auth.external.google]
enabled = true
client_id = "env(GOOGLE_CLIENT_ID)"
secret = "env(GOOGLE_CLIENT_SECRET)"
```

<Admonition type="tip">
  To retrieve the project ID for an existing branch, use the `branches list` command:

  ```bash
  supabase --experimental branches list
  ```

  This will display a table showing all your branches with their corresponding project ID.
  Use the value from the `BRANCH PROJECT ID` column as your `project_id` in the remote configuration.
</Admonition>



## Next steps

*   Explore [branching integrations](/docs/guides/deployment/branching/integrations)
*   Learn about [troubleshooting branches](/docs/guides/deployment/branching/troubleshooting)
*   Review [branching pricing](/docs/guides/deployment/branching/pricing)



# Branching via the dashboard

Create, manage, review, and merge branches directly in the dashboard

You can create, manage, review, and merge Supabase branches directly via the dashboard. This is useful for quick testing, prototyping, or when you prefer to work in a no-code way. You can also connect a Supabase branch to a GitHub branch at a later time if needed.

<Admonition type="note" label="Public Alpha">
  Branch management via the dashboard is currently in public alpha. Features and functionality may change.
</Admonition>



## How Branching works

You can do the following directly from the Supabase dashboard:

*   Create preview branches
*   Make changes to your public schema or edge functions
*   Merge these changes back into production when ready
*   Pull in updates from production



## Enable branch management via the dashboard

This functionality is currently in beta and requires opting in. To opt in you must enable the feature preview:

1.  Open the user menu by clicking on your user icon in the top right.
2.  Select **Branching via dashboard**.
3.  Click **Enable feature**.



## Creating a branch

Once you've enabled the feature, you can create a new branch:

1.  Click the arrows next to the branch name in the top menu bar. (The top menu bar has the format `YOUR_ORGANIZATION / YOUR_PROJECT / CURRENT_BRANCH_NAME`.)
2.  Click `Create branch`.



## Making changes to a branch

Use the branch selector in the top bar to change to your branch. Any changes you make (including SQL run in the SQL editor, table editor changes, and configuration changes) are now made against the currently selected branch.

You can also use the branch's API keys and connection strings to run changes against the branch from your own code or SQL client.



## Creating a merge request

To review and merge changes from a branch back into your production branch, you must first create a merge request. There are two ways to do this.

The first is to click the merge request button next to the branch selector that's located in the top menu. This will create the merge request and redirect you to the merge page where you can review and merge any changes.

The second is to click on manage branches from within the branch selector, then in the left hand navigation you can click on merge requests. From here you can view all open merge requests and create new ones.



## Pulling changes from production into a branch

When reviewing a merge request you may see a notice at the top of the page asking you to update your branch. This appears when your preview branch has drifted from your production branch. There may be public schema or edge function changes that have been made after your preview branch was created. Clicking update branch will attempt to pull in these changes, but be aware that by doing this your existing edge functions will be replaced. Any new edge functions created on the preview branch will remain untouched.



## Limitations

There are a few limitations you should be aware of before deciding to use branching without git.

*   Custom roles created through the dashboard are not captured on branch creation
*   Branches can only be merged to main; merging between preview branches is not supported
*   If your branch is out of date, you can pull in latest changes from main, but keep in mind that all functions will be overwritten
*   Deleting functions must be done manually on main branch
*   Migration conflicts must be manually resolved on the preview branch
*   If you have run migrations on main, new branches will be created from existing migrations instead of a full schema dump



# GitHub integration

Connect with GitHub to sync branches with your repository

Supabase Branching uses the Supabase GitHub integration to read files from your GitHub repository. With this integration, Supabase watches all commits, branches, and pull requests of your GitHub repository.



## Installation

In the Supabase Dashboard:

1.  Go to **Project Settings** > [**Integrations**](/dashboard/project/_/settings/integrations).
2.  Under **GitHub Integration**, click **Authorize GitHub**.
3.  You are redirected to a GitHub authorization page. Click **Authorize Supabase**.
4.  You are redirected back to the Integrations page. Choose a GitHub repository to connect your project to.
5.  Fill in the relative path to the Supabase directory from your repository root.
6.  Configure the other options as needed to automate your GitHub connection.
7.  Click **Enable integration**.



## Preparing your Git repository

You will be using the [Supabase CLI](/docs/guides/cli) to initialise your local `./supabase` directory:

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Initialize Supabase locally" fullWidth>
      If you don't have a `./supabase` directory, you can create one:

      ```markdown
      supabase init
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Pull your database migration" fullWidth>
      Pull your database changes using `supabase db pull`. To get your database connection string, go to your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session) and look for the Session pooler connection string.

      ```markdown
      supabase db pull --db-url <db_connection_string>

      # Your Database connection string will look like this:
      # postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
      ```

      <Admonition type="note">
        If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Commit the `supabase` directory to Git" fullWidth>
      Commit the `supabase` directory to Git, and push your changes to your remote repository.

      ```bash
      git add supabase
      git commit -m "Initial migration"
      git push
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Syncing GitHub branches

Enable the **Automatic branching** option in your GitHub Integration configuration to automatically sync GitHub branches with Supabase branches.

When a new branch is created in GitHub, a corresponding branch is created in Supabase. (You can enable the **Supabase changes only** option to only create Supabase branches when Supabase files change.)


### Configuration

You can test configuration changes on your Preview Branch by configuring the `config.toml` file in your Supabase directory. See the [Configuration docs](/docs/guides/deployment/branching/configuration) for more information.

A comment is added to your PR with the deployment status of your preview branch.


### Migrations

The migrations in the `migrations` subdirectory of your Supabase directory are automatically run.


### Seeding

No production data is copied to your Preview branch. This is meant to protect your sensitive production data.

You can seed your Preview Branch with sample data using the `seed.sql` file in your Supabase directory. See the [Seeding docs](/docs/guides/local-development/seeding-your-database) for more information.

Data changes in your seed files are not merged to production.



## Deploying changes to production

Enable the **Deploy to production** option in your GitHub Integration configuration to automatically deploy changes when you push or merge to production branch.

The following changes are deployed:

*   New migrations are applied
*   Edge Functions declared in `config.toml` are deployed
*   Storage buckets declared in `config.toml` are deployed

All other configurations, including API, Auth, and seed files, are ignored by default.



## Preventing migration failures

We highly recommend turning on a 'required check' for the Supabase integration. You can do this from your GitHub repository settings. This prevents PRs from being merged when migration checks fail, and stops invalid migrations from being merged into your production branch.

<Image zoomable className="max-w-[700px] !mx-auto" alt="Check the &#x22;Require status checks to pass before merging&#x22; option." caption="Check the &#x22;Require status checks to pass before merging&#x22; option." src="/docs/img/guides/platform/branching/github-required-check.jpg?v=1" />


### Email notifications

To catch failures early, we also recommend subscribing to email notifications on your branch. Common errors include migration conflict, function deployment failure, or invalid configuration file.

You can setup a custom GitHub Action to monitor the status of any Supabase Branch.

<NamedCodeBlock name=".github/workflows/notify-failure.yaml">
  ```yaml name=.github/workflows/notify-failure.yaml
  name: Branch Status

  on:
    pull_request:
      types:
        - opened
        - reopened
        - synchronize
      branches:
        - main
        - develop
      paths:
        - 'supabase/**'

  jobs:
    failed:
      runs-on: ubuntu-latest
      steps:
        - uses: fountainhead/action-wait-for-check@v1.2.0
          id: check
          with:
            checkName: Supabase Preview
            ref: ${{ github.event.pull_request.head.sha || github.sha }}
            token: ${{ secrets.GITHUB_TOKEN }}

        - if: ${{ steps.check.outputs.conclusion == 'failure' }}
          run: exit 1
  ```
</NamedCodeBlock>



# Integrations

Use Supabase branching with hosting providers and other tools

Branching works with hosting providers that support preview deployments. Learn how to integrate Supabase branching with various platforms and tools.



## Hosting providers

With the Supabase branching integration, you can sync the Git branch used by the hosting provider with the corresponding Supabase preview branch. This means that the preview deployment built by your hosting provider is matched to the correct database schema, edge functions, and other Supabase configurations.


### Vercel

Install the Vercel integration:

*   From the [Vercel marketplace](https://vercel.com/integrations/supabase) or
*   By clicking the blue `Deploy` button in a Supabase example app's `README` file

<Admonition type="note" label="Vercel GitHub integration also required.">
  For branching to work with Vercel, you also need the [Vercel GitHub integration](https://vercel.com/docs/deployments/git/vercel-for-github).
</Admonition>

And make sure you have [connected](/dashboard/org/_/integrations) your Supabase project to your Vercel project.

Supabase automatically updates your Vercel project with the correct environment variables for the corresponding preview branches. The synchronization happens at the time of Pull Request being opened, not at the time of branch creation.

As branching integration is tied to the Preview Deployments feature in Vercel, there are possible race conditions between Supabase setting correct variables, and Vercel running a deployment process. Because of that, Supabase is always automatically re-deploying the most recent deployment of the given pull request.



# Troubleshooting

Common issues and solutions for Supabase branching

This guide covers common issues you might encounter when using Supabase branching and how to resolve them.



## Monitoring deployments

To check deployment status and troubleshoot failures:

1.  Go to your project dashboard
2.  Navigate to "Manage Branches"
3.  Click on your branch to view deployment logs
4.  Check the "View logs" section for detailed error messages

For programmatic monitoring, you can use the [Management API](https://api.supabase.com/api/v1#tag/environments/post/v1/projects/\{ref}/branches) to poll branch status.

For detailed troubleshooting guidance, see our [Troubleshooting guide](/docs/guides/deployment/branching/troubleshooting).



## Common issues


### Rolling back migrations

You might want to roll back changes you've made in an earlier migration change. For example, you may have pushed a migration file containing schema changes you no longer want.

To fix this, push the latest changes, then delete the preview branch in Supabase and reopen it.

The new preview branch is reseeded from the `./supabase/seed.sql` file by default. Any additional data changes made on the old preview branch are lost. This is equivalent to running `supabase db reset` locally. All migrations are rerun in sequential order.


### Deployment failures

A deployment might fail for various reasons, including invalid SQL statements and schema conflicts in migrations, errors within the `config.toml` config, or something else.

To check the error message, see the Supabase workflow run for your branch under the [View logs](/dashboard/project/_/branches) section.


### Network restrictions

If you enable [network restrictions](/docs/guides/platform/network-restrictions) on your project, the branching cluster will be blocked from connecting to your project by default. This often results in database connection failures when migrating your production project after merging a development branch.

The workaround is to explicitly allow the IPv6 CIDR range of the branching cluster in your project's [Database Settings](/dashboard/project/_/database/settings) page: `2600:1f18:2b7d:f600::/56`

<Image
  alt="Network restrictions to allow connections from branching cluster"
  src={{
    dark: '/docs/img/guides/branching/cidr-dark.png',
    light: '/docs/img/guides/branching/cidr-light.png',
  }}
  className="max-w-[550px] !mx-auto border rounded-md"
  zoomable
/>


### Schema drift between preview branches

If multiple preview branches exist, each preview branch might contain different schema changes. This is similar to Git branches, where each branch might contain different code changes.

When a preview branch is merged into the production branch, it creates a schema drift between the production branch and the preview branches that haven't been merged yet.

These conflicts can be resolved in the same way as normal Git Conflicts: merge or rebase from the production Git branch to the preview Git branch. Since migrations are applied sequentially, ensure that migration files are timestamped correctly after the rebase. Changes that build on top of earlier changes should always have later timestamps.


### Changing production branch

It's not possible to change the Git branch used as the Production branch for Supabase Branching. The only way to change it is to disable and re-enable branching. See [Disable Branching](#disable-branching).



## Migration issues


### Failed migrations

When migrations fail, check:

1.  **SQL syntax**: Ensure your migration files contain valid SQL
2.  **Dependencies**: Check if migrations depend on objects that don't exist
3.  **Permissions**: Verify the migration doesn't require superuser privileges

To debug:

```bash

# Test migrations locally first
supabase db reset


# Check migration logs in the dashboard

# Navigate to Branches > Your Branch > View Logs
```


### Migration order problems

Migrations must run in the correct order. Common issues:

1.  **Timestamp conflicts**: Ensure migration files have unique timestamps
2.  **Dependency issues**: Later migrations depending on earlier ones
3.  **Rebase problems**: Timestamps getting out of order after Git rebase

Fix by:

```bash

# Rename migration files to fix timestamp order
mv 20240101000000_old.sql 20240102000000_old.sql


# Reset local database to test
supabase db reset
```



## Connection issues


### Cannot connect to preview branch

If you can't connect to a preview branch:

1.  **Check credentials**: Ensure you're using the correct branch-specific credentials
2.  **Auto-pause**: The branch might be paused. It will resume on the first request
3.  **Network restrictions**: Check if network restrictions are blocking access


### Connection timeouts

Preview branches auto-pause after inactivity. First connections after pause may timeout:

1.  **Retry**: The branch will wake up after the first request
2.  **Persistent branches**: Convert frequently-used branches to persistent



## Configuration problems


### Config.toml not applying

If configuration changes aren't applying:

1.  **Syntax errors**: Validate your `config.toml` syntax
2.  **Git sync**: Ensure changes are committed and pushed
3.  **Branch refresh**: Try deleting and recreating the branch


### Secrets not available

If secrets aren't working in your branch:

1.  **Branch-specific**: Remember secrets are set per branch
2.  **Syntax**: Use correct syntax: `env(SECRET_NAME)`
3.  **CLI version**: Ensure you're using the latest CLI version



## Performance issues


### Slow branch creation

Branch creation might be slow due to:

1.  **Large migrations**: Many or complex migration files
2.  **Seed data**: Large seed files take time to process
3.  **Network latency**: Geographic distance from the branch region


### Query performance

Preview branches may have different performance characteristics:

1.  **Cold starts**: First queries after auto-pause are slower
2.  **Resource limits**: Preview branches have different resource allocations
3.  **Indexing**: Ensure proper indexes exist in your migrations



## Data issues


### Seed data not loading

If seed data isn't loading:

1.  **File location**: Ensure `seed.sql` is in `./supabase/` directory
2.  **SQL errors**: Check for syntax errors in seed file
3.  **Dependencies**: Seed data might reference non-existent tables


### Data persistence

Remember that preview branch data:

1.  **Is temporary**: Data is lost when branch is deleted
2.  **Isn't migrated**: Data doesn't move between branches
3.  **Resets on recreation**: Deleting and recreating branch loses data



## Getting help

If you're still experiencing issues:

1.  **Check logs**: Review branch logs in the dashboard
2.  **Community**: Ask in [GitHub discussions](https://github.com/orgs/supabase/discussions/18937)
3.  **Support**: Contact support for project-specific issues
4.  **Documentation**: Review the latest documentation for updates



# Working with branches

Learn how to develop and manage your Supabase branches

This guide covers how to work with Supabase branches effectively, including migration management, seeding behavior, and development workflows.



## Subscribing to notifications

You can subscribe to webhook notifications when an action run completes on a persistent branch. The payload format follows the [webhook standards](https://www.standardwebhooks.com).

```json
{
  "type": "run.completed",
  "timestamp": "2025-10-17T02:27:18.705861793Z",
  "data": {
    "project_ref": "xuqpsshjxdecrwdyuxvs",
    "details_url": "https://supabase.com/dashboard/project/xuqpsshjxdecrwdyuxvs/branches",
    "action_run": {
      "id": "d5f8b4298d0a4d37b99e255c7837e7af",
      "created_at": "2025-10-17T02:27:10.133329324Z"
      "steps": [
        {
          "name": "clone",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:10.788435466Z"
        },
        {
          "name": "pull",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:11.701742857Z"
        },
        {
          "name": "health",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:12.79205717Z"
        },
        {
          "name": "configure",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:13.726839657Z"
        },
        {
          "name": "migrate",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:14.97017507Z"
        },
        {
          "name": "seed",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:15.637684921Z"
        },
        {
          "name": "deploy",
          "status": "exited",
          "updated_at": "2025-10-17T02:27:18.604193114Z"
        }
      ]
    }
  }
}
```

We recommend registering a single webhooks processor that dispatches events to downstream services based on the payload type. The easiest way to do that is by deploying an Edge Function. For example, the following Edge Function listens for run completed events to notify a Slack channel.

<NamedCodeBlock name="supabase/functions/notify-slack/index.ts">
  ```typescript name=supabase/functions/notify-slack/index.ts
  // Setup type definitions for built-in Supabase Runtime APIs
  import 'jsr:@supabase/functions-js/edge-runtime.d.ts'

  console.log('Branching notification booted!')
  const slack = Deno.env.get('SLACK_WEBHOOK_URL') ?? ''

  Deno.serve(async (request) => {
    const body = await request.json()
    const blocks = [
      {
        type: 'header',
        text: {
          type: 'plain_text',
          text: `Action run ${body.data.action_run.failure ? 'failed' : 'completed'}`,
          emoji: true,
        },
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Branch ref:*\n${body.data.project_ref}`,
          },
          {
            type: 'mrkdwn',
            text: `*Run ID:*\n${body.data.action_run.id}`,
          },
        ],
      },
      {
        type: 'section',
        fields: [
          {
            type: 'mrkdwn',
            text: `*Started at:*\n${body.data.action_run.created_at}`,
          },
          {
            type: 'mrkdwn',
            text: `*Completed at:*\n${body.timestamp}`,
          },
        ],
      },
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: `<${body.data.details_url}|View logs>`,
        },
      },
    ]
    const resp = await fetch(slack, {
      method: 'POST',
      body: JSON.stringify({
        blocks,
      }),
    })
    const message = await resp.text()
    return new Response(
      JSON.stringify({
        message,
      }),
      {
        status: 200,
      }
    )
  })
  ```
</NamedCodeBlock>

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Setup Slack webhook URL" fullWidth>
      Create a [Slack webhook URL](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/) and set it as Function secrets.

      ```markdown
      supabase secrets set --project-ref <branch-ref> SLACK_WEBHOOK_URL=<your-webhook-url>
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Deploy your webhooks processor" fullWidth>
      Create and deploy an Edge Function to process webhooks.

      ```markdown
      supabase functions deploy --project-ref <branch-ref> --use-api notify-slack
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Update branch notification URL" fullWidth>
      Update the notification URL of your target branch to point to your Edge Function.

      ```markdown
      supabase branches update <branch-ref> --notify-url https://<branch-ref>.supabase.co/functions/v1/notify-slack
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>

After completing the steps above, you should receive a Slack message whenever an action run completes on your target branch.



## Migration and seeding behavior

Migrations are run in sequential order. Each migration builds upon the previous one.

The preview branch has a record of which migrations have been applied, and only applies new migrations for each commit. This can create an issue when rolling back migrations.


### Using ORM or custom seed scripts

If you want to use your own ORM for managing migrations and seed scripts, you will need to run them in GitHub Actions after the preview branch is ready. The branch credentials can be fetched using the following example GHA workflow.

<NamedCodeBlock name=".github/workflows/custom-orm.yaml">
  ```yaml name=.github/workflows/custom-orm.yaml
  name: Custom ORM

  on:
    pull_request:
      types:
        - opened
        - reopened
        - synchronize
      branches:
        - main
      paths:
        - 'supabase/**'

  jobs:
    wait:
      runs-on: ubuntu-latest
      outputs:
        status: ${{ steps.check.outputs.conclusion }}
      steps:
        - uses: fountainhead/action-wait-for-check@v1.2.0
          id: check
          with:
            checkName: Supabase Preview
            ref: ${{ github.event.pull_request.head.sha || github.sha }}
            token: ${{ secrets.GITHUB_TOKEN }}

    migrate:
      needs:
        - wait
      if: ${{ needs.wait.outputs.status == 'success' }}
      runs-on: ubuntu-latest
      env:
        SUPABASE_ACCESS_TOKEN: ${{ secrets.SUPABASE_ACCESS_TOKEN }}
        SUPABASE_PROJECT_ID: ${{ secrets.SUPABASE_PROJECT_ID }}
      steps:
        - uses: supabase/setup-cli@v1
          with:
            version: latest
        - run: supabase --experimental branches get "$GITHUB_HEAD_REF" -o env >> $GITHUB_ENV
        - name: Custom ORM migration
          run: psql "$POSTGRES_URL_NON_POOLING" -c 'select 1'
  ```
</NamedCodeBlock>


### Rolling back migrations

You might want to roll back changes you've made in an earlier migration change. For example, you may have pushed a migration file containing schema changes you no longer want.

To fix this, push the latest changes, then delete the preview branch in Supabase and reopen it.

The new preview branch is reseeded from the `./supabase/seed.sql` file by default. Any additional data changes made on the old preview branch are lost. This is equivalent to running `supabase db reset` locally. All migrations are rerun in sequential order.


### Seeding behavior

Your Preview Branches are seeded with sample data using the same as [local seeding behavior](/docs/guides/local-development/seeding-your-database).

The database is only seeded once, when the preview branch is created. To rerun seeding, delete the preview branch and recreate it by closing, and reopening your pull request.



## Developing with branches

You can develop with branches using either local or remote development workflows.


### Local development workflow

1.  Create a new Git branch for your feature
2.  Make schema changes using the Supabase CLI
3.  Generate migration files with `supabase db diff`
4.  Test your changes locally
5.  Commit and push to GitHub
6.  Open a pull request to create a preview branch


### Remote development workflow

1.  Create a preview branch in the Supabase dashboard
2.  Switch to the branch using the branch dropdown
3.  Make schema changes in the dashboard
4.  Pull changes locally using `supabase db pull`
5.  Commit the generated migration files
6.  Push to your Git repository



## Managing branch environments


### Switching between branches

Use the branch dropdown in the Supabase dashboard to switch between different branches. Each branch has its own:

*   Database instance
*   API endpoints
*   Authentication settings
*   Storage buckets


### Accessing branch credentials

Each branch has unique credentials that you can find in the dashboard:

1.  Switch to your desired branch
2.  Navigate to Settings > API
3.  Copy the branch-specific URLs and keys


### Branch isolation

Branches are completely isolated from each other. Changes made in one branch don't affect others, including:

*   Database schema and data
*   Storage objects
*   Edge Functions
*   Auth configurations



## Next steps

*   Learn about [branch configuration](/docs/guides/deployment/branching/configuration)
*   Explore [integrations](/docs/guides/deployment/branching/integrations)
*   Review [troubleshooting guide](/docs/guides/deployment/branching/troubleshooting)



# Working With Arrays



Postgres supports flexible [array types](https://www.postgresql.org/docs/12/arrays.html). These arrays are also supported in the Supabase Dashboard and in the JavaScript API.



## Create a table with an array column

Create a test table with a text array (an array of strings):

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Click **New Table** and create a table with the name `arraytest`.
    3.  Click **Save**.
    4.  Click **New Column** and create a column with the name `textarray`, type `text`, and select **Define as array**.
    5.  Click **Save**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create table arraytest (
      id integer not null,
      textarray text array
    );
    ```
  </TabPanel>
</Tabs>



## Insert a record with an array value

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Select the `arraytest` table.
    3.  Click **Insert row** and add `["Harry", "Larry", "Moe"]`.
    4.  Click **Save.**
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    INSERT INTO arraytest (id, textarray) VALUES (1, ARRAY['Harry', 'Larry', 'Moe']);
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    Insert a record from the JavaScript client:

    ```js
    const { data, error } = await supabase
      .from('arraytest')
      .insert([{ id: 2, textarray: ['one', 'two', 'three', 'four'] }])
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Insert a record from the Swift client:

    ```swift
    struct ArrayTest: Encodable {
      let id: Int
      let textarray: [String]
    }

    try await supabase
      .from("arraytest")
      .insert(
        [
          ArrayTest(
            id: 2,
            textarray: ["one", "two", "three", "four"]
          )
        ]
      )
      .execute()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    Insert a record from the Python client:

    ```python
    supabase.from_('arraytest').insert(
      [
        {
          id: 2,
          textarray: ["one", "two", "three", "four"]
        }
      ]
    )
    .execute()
    ```
  </TabPanel>
</Tabs>



## View the results

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Select the `arraytest` table.

    You should see:

    ```
    | id  | textarray               |
    | --- | ----------------------- |
    | 1   | ["Harry","Larry","Moe"] |
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    select * from arraytest;
    ```

    You should see:

    ```
    | id  | textarray               |
    | --- | ----------------------- |
    | 1   | ["Harry","Larry","Moe"] |
    ```
  </TabPanel>
</Tabs>



## Query array data

Postgres uses 1-based indexing (e.g., `textarray[1]` is the first item in the array).

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    To select the first item from the array and get the total length of the array:

    ```js
    SELECT textarray[1], array_length(textarray, 1) FROM arraytest;
    ```

    returns:

    ```
    | textarray | array_length |
    | --------- | ------------ |
    | Harry     | 3            |
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    This returns the entire array field:

    ```js
    const { data, error } = await supabase.from('arraytest').select('textarray')
    console.log(JSON.stringify(data, null, 2))
    ```

    returns:

    ```json
    [
      {
        "textarray": ["Harry", "Larry", "Moe"]
      }
    ]
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    This returns the entire array field:

    ```swift
    struct Response: Decodable {
      let textarray: [String]
    }

    let response: [Response] = try await supabase.from("arraytest").select("textarray").execute().value
    dump(response)
    ```

    returns:

    ```
    [
      Response(
        textarray: ["Harry", "Larry", "Moe"],
      )
    ]
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Supabase JS Client](https://github.com/supabase/supabase-js)
*   [Supabase - Get started for free](https://supabase.com)
*   [Postgres Arrays](https://www.postgresql.org/docs/15/arrays.html)



# Connecting with Beekeeper Studio



[`Beekeeper Studio Community`](https://www.beekeeperstudio.io/get-community) is a free GUI tool for interacting with databases.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a new connection">
      In Beekeeper, create a new Postgres connection.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![Postgres connection](/docs/img/guides/database/connecting-to-postgres/beekeeper-studio/new-connection.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Get your connection credentials">
      Get your connection credentials from the [**Connect** panel](/dashboard/project/_/?showConnect=true). You will need:

      *   host
      *   username
      *   password
      *   port
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Add your credentials to Beekeeper's connection form

      ![Credentials](/docs/img/guides/database/connecting-to-postgres/beekeeper-studio/beekeeper-credentials.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Download your SSL Certificate">
      Download your SSL certificate from the Dashboard's [`Database Settings`](/dashboard/project/_/database/settings)
      ![SSL](/docs/img/guides/database/connecting-to-postgres/beekeeper-studio/certificate.png)
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Add your SSL to the connection form
      ![SSL](/docs/img/guides/database/connecting-to-postgres/beekeeper-studio/certificate-beekeeper.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Test and connect">
      Test your connection and then connect
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![SSL](/docs/img/guides/database/connecting-to-postgres/beekeeper-studio/connect.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Connect to your database

Supabase provides multiple methods to connect to your Postgres database, whether you’re working on the frontend, backend, or utilizing serverless functions.


## How to connect to your Postgres databases

How you connect to your database depends on where you're connecting from:

*   For frontend applications, use the [Data API](#data-apis-and-client-libraries)
*   For Postgres clients, use a connection string
    *   For single sessions (for example, database GUIs) or Postgres native commands (for example, using client applications like [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) or specifying connections for [replication](/docs/guides/database/postgres/setup-replication-external)) use the [direct connection string](#direct-connection) if your environment supports IPv6
    *   For persistent clients, and support for both IPv4 and IPv6, use [pooler session mode](#pooler-session-mode)
    *   For temporary clients (for example, serverless or edge functions) use [pooler transaction mode](#pooler-transaction-mode)



## Quickstarts

<div className="grid grid-cols-[repeat(auto-fit,minmax(150px,1fr))] gap-6   not-prose">
  <NavData data="ormQuickstarts">
    {(data) =>
              data.items?.map((quickstart) => (
                <Link key={quickstart.url} href={quickstart.url} passHref>
                  <GlassPanel
                    key={quickstart.name}
                    title={quickstart.name}
                    className="[&>div]:p-2 flex justify-center [&_p]:text-foreground-light"
                  />
                </Link>
              ))
            }
  </NavData>

  <NavData data="guiQuickstarts">
    {(data) =>
              data.items?.map((quickstart) => (
                <Link key={quickstart.url} href={quickstart.url} passHref>
                  <GlassPanel
                    key={quickstart.name}
                    title={quickstart.name}
                    className="[&>div]:p-2 flex justify-center [&_p]:text-foreground-light"
                  />
                </Link>
              ))
            }
  </NavData>
</div>



## Data APIs and client libraries

The Data APIs allow you to interact with your database using REST or GraphQL requests. You can use these APIs to fetch and insert data from the frontend, as long as you have [RLS](/docs/guides/database/postgres/row-level-security) enabled.

*   [REST](/docs/guides/api)
*   [GraphQL](/docs/guides/graphql/api)

For convenience, you can also use the [Supabase client libraries](/docs/reference), which wrap the Data APIs with a developer-friendly interface and automatically handle authentication:

*   [JavaScript](/docs/reference/javascript)
*   [Flutter](/docs/reference/dart)
*   [Swift](/docs/reference/swift)
*   [Python](/docs/reference/python)
*   [C#](/docs/reference/csharp)
*   [Kotlin](/docs/reference/kotlin)



## Direct connection

The direct connection string connects directly to your Postgres instance. It is ideal for persistent servers, such as virtual machines (VMs) and long-lasting containers. Examples include AWS EC2 machines, Fly.io VMs, and DigitalOcean Droplets.

<Admonition type="caution">
  Direct connections use IPv6 by default. If your environment doesn't support IPv6, use [Supavisor session mode](#supavisor-session-mode) or get the [IPv4 add-on](/docs/guides/platform/ipv4-address).
</Admonition>

The connection string looks like this:

```
postgresql://postgres:[YOUR-PASSWORD]@db.abcdefghijklmnopqrst.supabase.co:5432/postgres
```

Get your project's direct connection string from your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true).



## Poolers

Every Supabase project includes a connection pooler. This is ideal for persistent servers when IPv6 is not supported.


### Pooler session mode

The session mode connection string connects to your Postgres instance via a proxy. This is only recommended as an alternative to a Direct Connection, when connecting via an IPv4 network.

The connection string looks like this:

```
postgres://postgres.apbkobhfnmcqqzqeeqss:[YOUR-PASSWORD]@aws-0-[REGION].pooler.supabase.com:5432/postgres
```

Get your project's Session pooler connection string from your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true\&method=session).


### Pooler transaction mode

The transaction mode connection string connects to your Postgres instance via a proxy which serves as a connection pooler. This is ideal for serverless or edge functions, which require many transient connections.

<Admonition type="caution">
  Transaction mode does not support [prepared statements](https://postgresql.org/docs/current/sql-prepare.html). To avoid errors, [turn off prepared statements](https://github.com/orgs/supabase/discussions/28239) for your connection library.
</Admonition>

The connection string looks like this:

```
postgres://postgres:[YOUR-PASSWORD]@db.abcdefghijklmnopqrst.supabase.co:6543/postgres
```

Get your project's Transaction pooler connection string from your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true\&method=transaction).



## Dedicated pooler

For paying customers, we provision a Dedicated Pooler ([PgBouncer](https://www.pgbouncer.org/)) that's co-located with your Postgres database. This will require you to connect with IPv6 or, if that's not an option, you can use the [IPv4 add-on](/docs/guides/platform/ipv4-address).

The Dedicated Pooler ensures best performance and latency, while using up more of your project's compute resources. If your network supports IPv6 or you have the IPv4 add-on, we encourage you to use the Dedicated Pooler over the Shared Pooler.

Get your project's Dedicated pooler connection string from your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true\&method=transaction).

<Admonition type="note">
  PgBouncer always runs in Transaction mode and the current version does not support prepared statement (will be added in a few weeks).
</Admonition>



## More about connection pooling

Connection pooling improves database performance by reusing existing connections between queries. This reduces the overhead of establishing connections and improves scalability.

You can use an application-side pooler or a server-side pooler (Supabase automatically provides one called Supavisor), depending on whether your backend is persistent or serverless.


### Application-side poolers

Application-side poolers are built into connection libraries and API servers, such as Prisma, SQLAlchemy, and PostgREST. They maintain several active connections with Postgres or a server-side pooler, reducing the overhead of establishing connections between queries. When deploying to static architecture, such as long-standing containers or VMs, application-side poolers are satisfactory on their own.


### Serverside poolers

Postgres connections are like a WebSocket. Once established, they are preserved until the client (application server) disconnects. A server might only make a single 10 ms query, but needlessly reserve its database connection for seconds or longer.

Serverside-poolers, such as Supabase's [Supavisor](https://github.com/supabase/supavisor) in transaction mode, sit between clients and the database and can be thought of as load balancers for Postgres connections.

<Image
  alt="New migration files trigger migrations on the preview instance."
  src={{
    dark: '/docs/img/guides/database/connecting-to-postgres/how-connection-pooling-works.png',
    light:
      '/docs/img/guides/database/connecting-to-postgres/how-connection-pooling-works--light.png',
  }}
  caption="Connecting to the database directly vs using a Connection Pooler"
  zoomable
/>

They maintain hot connections with the database and intelligently share them with clients only when needed, maximizing the amount of queries a single connection can service. They're best used to manage queries from auto-scaling systems, such as edge and serverless functions.



## Connecting with SSL

You should connect to your database using SSL wherever possible, to prevent snooping and man-in-the-middle attacks.

You can obtain your connection info and Server root certificate from your application's dashboard:

![Connection Info and Certificate.](/docs/img/database/database-settings-ssl.png)



## Resources

*   [Connection management](/docs/guides/database/connection-management)
*   [Connecting with psql](/docs/guides/database/psql)
*   [Importing data into Supabase](/docs/guides/database/import-data)



## Troubleshooting and Postgres connection string FAQs

Below are answers to common challenges and queries.


### What is a “connection refused” error?

A “Connection refused” error typically means your database isn’t reachable. Ensure your Supabase project is running, confirm your database’s connection string, check firewall settings, and validate network permissions.


### What is the “FATAL: Password authentication failed” error?

This error occurs when your credentials are incorrect. Double-check your username and password from the Supabase dashboard. If the problem persists, reset your database password from the project settings.


### How do you connect using IPv4?

Supabase’s default direct connection supports IPv6 only. To connect over IPv4, consider using the Supavisor session or transaction modes, or a connection pooler (shared or dedicated), which support both IPv4 and IPv6.


### Where is the Postgres connection string in Supabase?

Your connection string is located in the Supabase Dashboard. Click the [Connect](/dashboard/project/_?showConnect=true) button at the top of the page.


### Can you use Supavisor and PgBouncer together?

You can technically use both, but it’s not recommended unless you’re specifically trying to increase the total number of concurrent client connections. In most cases, it is better to choose either PgBouncer or Supavisor for pooled or transaction-based traffic. Direct connections remain the best choice for long-lived sessions, and, if IPv4 is required for those sessions, Supavisor session mode can be used as an alternative. Running both poolers simultaneously increases the risk of hitting your database’s maximum connection limit on smaller compute tiers.


### How does the default pool size work?

Supavisor and PgBouncer work independently, but both reference the same pool size setting. For example, if you set the pool size to 30, Supavisor can open up to 30 server-side connections to Postgres each for its session mode port (5432) and transaction mode port (6543), and PgBouncer can also open up to 30. If both poolers are active and reach their roles/modes limits at the same time, you could have as many as 60 backend connections hitting your database, in addition to any direct connections. You can adjust the pool size in [Database settings](/dashboard/project/_/database/settings) in the dashboard.


### What is the difference between client connections and backend connections?

There are two different limits to understand when working with poolers. The first is client connections, which refers to how many clients can connect to a pooler at the same time. This number is capped by your [compute tier’s “max pooler clients” limit](/docs/guides/platform/compute-and-disk#postgres-replication-slots-wal-senders-and-connections), and it applies independently to Supavisor and PgBouncer. The second is backend connections, which is the number of active connections a pooler opens to Postgres. This number is set by the pool size for that pooler.

```
Total backend load on Postgres =
 Direct connections +
 Supavisor backend connections (≤ supavisor_pool_size) +
 PgBouncer backend connections (≤ pgbouncer_pool_size)
≤ Postgres max connections for your compute instance
```


### What is the max pooler clients limit?

The “max pooler clients” limit for your compute tier applies separately to Supavisor and PgBouncer. One pooler reaching its client limit does not affect the other. When a pooler reaches this limit, it stops accepting new client connections until existing ones are closed, but the other pooler remains unaffected. You can check your tier’s connection limits in the [compute and disk limits documentation](/docs/guides/platform/compute-and-disk#postgres-replication-slots-wal-senders-and-connections).


### Where can you see current connection usage?

You can track connection usage from the [Reports](/dashboard/project/_/reports/database) section in your project dashboard. There are three key reports:

*   **Database Connections:** shows total active connections by role (this includes direct and pooled connections).
*   **Dedicated Pooler Client Connections:** shows the number of active client connections to PgBouncer.
*   **Shared Pooler (Supavisor) Client Connections:** shows the number of active client connections to Supavisor.

Keep in mind that the Roles page is not real-time, it shows the connection count from the last refresh. If you need up-to-the-second data, set up Grafana or run the query against `pg_stat_activity` directly in SQL Editor. We have a few helpful queries for checking connections.

```sql
-- Count connections by application and user name
select
  count(usename),
  count(application_name),
  application_name,
  usename
from
  pg_stat_ssl
  join pg_stat_activity on pg_stat_ssl.pid = pg_stat_activity.pid
group by usename, application_name;
```

```sql
-- View all connections
 SELECT
   pg_stat_activity.pid,
   ssl AS ssl_connection,
   datname AS database,
   usename AS connected_role,
   application_name,
   client_addr,
   query,
   query_start,
   state,
   backend_start
FROM pg_stat_ssl
JOIN pg_stat_activity
 ON pg_stat_ssl.pid = pg_stat_activity.pid;
```


### Why are there active connections when the app is idle?

Even if your application isn’t making queries, some Supabase services keep persistent connections to your database. For example, Storage, PostgREST, and our health checker all maintain long-lived connections. You usually see a small baseline of active connections from these services.


### Why do connection strings have different ports?

Different modes use different ports:

*   Direct connection: `5432` (database server)
*   PgBouncer: `6543` (database server)
*   Supavisor transaction mode: `6543` (separate server)
*   Supavisor session mode: `5432` (separate server)

The port helps route the connection to the right pooler/mode.


### Does connection pooling affect latency?

Because the dedicated pooler is hosted on the same machine as your database, it connects with lower latency than the shared pooler, which is hosted on a separate server. Direct connections have no pooler overhead but require IPv6 unless you have the IPv4 add-on.


### How to choose the right connection method?

**Direct connection:**

*   Best for: persistent backend services
*   Limitation: IPv6 only

**Shared pooler:**

*   Best for: general-purpose connections (supports IPv4 and IPv6)
    *   Supavisor session mode → persistent backend that require IPv4
    *   Supavisor transaction mode → serverless functions or short-lived tasks

**Dedicated pooler (paid tier):**

*   Best for: high-performance apps that need dedicated resources
*   Uses PgBouncer

You can follow the decision flow in the connection method diagram to quickly choose the right option for your environment.

<Image
  alt="Decision tree diagram showing when to connect directly to Postgres or use a connection pooler."
  src={{
    dark: '/docs/img/guides/database/connecting-to-postgres/connection-decision-tree.svg',
    light: '/docs/img/guides/database/connecting-to-postgres/connection-decision-tree-light.svg',
  }}
  caption="Choosing between direct Postgres connections and connection pooling"
  zoomable
/>



---
**Navigation:** [← Previous](./20-custom-auth-emails-with-react-email-and-resend.md) | [Index](./index.md) | [Next →](./22-connection-management.md)
