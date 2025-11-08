**Navigation:** [← Previous](./08-hipaa-projects.md) | [Index](./index.md) | [Next →](./10-set-supabase-connection-session-pooler-on-port-543.md)

# Set Up SSO with Okta



<Admonition type="note">
  This feature is only available on the [Team and Enterprise Plans](/pricing). If you are an existing Team or Enterprise Plan customer, continue with the setup below.
</Admonition>

<Admonition type="tip">
  Looking for docs on how to add Single Sign-On support in your Supabase project? Head on over to [Single Sign-On with SAML 2.0 for Projects](/docs/guides/auth/enterprise-sso/auth-sso-saml).
</Admonition>

Supabase supports single sign-on (SSO) using Okta.



## Step 1: Choose to create an app integration in the applications dashboard \[#create-app-integration]

Navigate to the Applications dashboard of the Okta admin console. Click *Create App Integration*.

![Okta dashboard: Create App Integration button](/docs/img/sso-okta-step-01.png)



## Step 2: Choose SAML 2.0 in the app integration dialog \[#create-saml-app]

Supabase supports the SAML 2.0 SSO protocol. Choose it from the *Create a new app integration* dialog.

![Okta dashboard: Create new app integration dialog](/docs/img/sso-okta-step-02.png)



## Step 3: Fill out general settings \[#add-general-settings]

The information you enter here is for visibility into your Okta applications menu. You can choose any values you like. `Supabase` as a name works well for most use cases.

![Okta dashboard: Create SAML Integration wizard](/docs/img/sso-okta-step-03.png)



## Step 4: Fill out SAML settings \[#add-saml-settings]

These settings let Supabase use SAML 2.0 properly with your Okta application. Make sure you enter this information exactly as shown on in this table.

| Setting                                        | Value                                               |
| ---------------------------------------------- | --------------------------------------------------- |
| Single sign-on URL                             | `https://alt.supabase.io/auth/v1/sso/saml/acs`      |
| Use this for Recipient URL and Destination URL | ✔️                                                  |
| Audience URI (SP Entity ID)                    | `https://alt.supabase.io/auth/v1/sso/saml/metadata` |
| Default `RelayState`                           | `https://supabase.com/dashboard`                    |
| Name ID format                                 | `EmailAddress`                                      |
| Application username                           | Email                                               |
| Update application username on                 | Create and update                                   |

![Okta dashboard: Create SAML Integration wizard, Configure SAML step](/docs/img/sso-okta-step-04.png)



## Step 5: Fill out attribute statements \[#add-attribute-statements]

Attribute Statements allow Supabase to get information about your Okta users on each login.

**A `email` to `user.email` statement is required.** Other mappings shown below are optional and configurable depending on your Okta setup. If in doubt, replicate the same config as shown. You will use this mapping later in [Step 10](#dashboard-configure-attributes).

![Okta dashboard: Attribute Statements configuration screen](/docs/img/sso-okta-step-05.png)



## Step 6: Obtain IdP metadata URL \[#idp-metadata-url]

Supabase needs to finalize enabling single sign-on with your Okta application.

To do this scroll down to the *SAML Signing Certificates* section on the *Sign On* tab of the *Supabase* application. Pick the the *SHA-2* row with an *Active* status. Click on the *Actions* dropdown button and then on the *View IdP Metadata*.

This will open up the SAML 2.0 Metadata XML file in a new tab in your browser. You will need to enter this URL later in [Step 9](#dashboard-configure-metadata).

The link usually has this structure: `https://<okta-org>.okta.com/apps/<app-id>/sso/saml/metadata`

![Okta dashboard: SAML Signing Certificates, Actions button highlighted](/docs/img/sso-okta-step-06.png)



## Step 7: Enable SSO in the Dashboard \[#dashboard-enable-sso]

1.  Visit the [SSO tab](/dashboard/org/_/sso) under the Organization Settings page. ![SSO disabled](/docs/img/sso-dashboard-disabled.png)

2.  Toggle **Enable Single Sign-On** to begin configuration. Once enabled, the configuration form appears. ![SSO enabled](/docs/img/sso-dashboard-enabled.png)



## Step 8: Configure domains \[#dashboard-configure-domain]

Enter one or more domains associated with your users email addresses (e.g., `supabase.com`).
These domains determine which users are eligible to sign in via SSO.

![Domain configuration](/docs/img/sso-dashboard-configure-domain.png)

If your organization uses more than one email domain - for example, `supabase.com` for staff and `supabase.io` for contractors - you can add multiple domains here. All listed domains will be authorized for SSO sign-in.

![Domain configuration with multiple domains](/docs/img/sso-dashboard-configure-domain-multi.png)

<Admonition type="note">
  We do not permit use of public domains like `gmail.com`, `yahoo.com`.
</Admonition>



## Step 9: Configure metadata \[#dashboard-configure-metadata]

Enter the metadata URL you obtained from [Step 6](#idp-metadata-url) into the Metadata URL field:

![Metadata configuration with Okta](/docs/img/sso-dashboard-configure-metadata-okta.png)



## Step 10: Configure attribute mapping \[#dashboard-configure-attributes]

Enter the SAML attributes you filled out in [Step 5](#add-attribute-statements) into the Attribute Mapping section.

![Attribute mapping configuration](/docs/img/sso-dashboard-configure-attributes.png)

<Admonition type="note">
  If you did not customize your settings you may save some time by clicking the **Okta** preset.
</Admonition>



## Step 11: Join organization on signup (optional) \[#dashboard-configure-autojoin]

By default this setting is disabled, users logging in via SSO will not be added to your organization automatically.

![Auto-join disabled](/docs/img/sso-dashboard-configure-autojoin-disabled.png)

Toggle this on if you want SSO-authenticated users to be **automatically added to your organization** when they log in via SSO.

![Auto-join enable](/docs/img/sso-dashboard-configure-autojoin-enabled.png)

When auto-join is enabled, you can choose the **default role** for new users:

![Auto-join role selection](/docs/img/sso-dashboard-configure-autojoin-enabled-role.png)

Choose a role that fits the level of access you want to grant to new members.

<Admonition type="note">
  Visit [access-control](/docs/guides/platform/access-control) documentation for details about each role.
</Admonition>



## Step 12: Save changes and test single sign-on \[#dashboard-configure-save]

When you click **Save changes**, your new SSO configuration is applied immediately. From that moment, any user with an email address matching one of your configured domains who visits your organization's sign-in URL will be routed through the SSO flow.

We recommend asking a few users to test signing in via their Okta account. They can do this by entering their email address on the [Sign in with SSO](/dashboard/sign-in-sso) page.

If SSO sign-in doesn't work as expected, contact your Supabase support representative for assistance.



# Backup and Restore using the CLI

Learn how to backup and restore projects using the Supabase CLI


## Backup database using the CLI

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Install the Supabase CLI" fullWidth>
      Install the [Supabase CLI](/docs/guides/local-development/cli/getting-started).
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Install Docker Desktop" fullWidth>
      Install [Docker Desktop](https://www.docker.com) for your platform.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Get the new database connection string" fullWidth>
      On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true).

      <Admonition type="note">
        Use the [Session pooler](/dashboard/project/_?showConnect=true\&method=session) connection string by default. If your ISP supports IPv6 or you have the IPv4 add-on enabled, use the direct connection string.
      </Admonition>

      Session pooler connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
      ```

      Direct connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.com:5432/postgres
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Get the database password" fullWidth>
      Reset the password in the [Database Settings](/dashboard/project/_/database/settings).

      Replace `[YOUR-PASSWORD]` in the connection string with the database password.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Backup database" fullWidth>
      Run these commands after replacing `[CONNECTION_STRING]` with your connection string from the previous steps:

      ```bash
      supabase db dump --db-url [CONNECTION_STRING] -f roles.sql --role-only
      ```

      ```bash
      supabase db dump --db-url [CONNECTION_STRING] -f schema.sql
      ```

      ```bash
      supabase db dump --db-url [CONNECTION_STRING] -f data.sql --use-copy --data-only
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Before you begin

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6">
  <div className="border-b mt-3 pb-3">
    <AccordionItem header="Install Postgres and psql" id="install-postgres">
      <Tabs scrollable size="small" type="underlined" defaultActiveId="windows">
        <TabPanel id="windows" label="Windows">
          <StepHikeCompact>
            <StepHikeCompact.Step step={1}>
              <StepHikeCompact.Details title="Install Postgres" fullWidth>
                Download and run the installation file for the latest version from the [Postgres installer download page](https://www.postgresql.org/download/windows/).
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={2}>
              <StepHikeCompact.Details title="Add Postgres to your system PATH" fullWidth>
                Add the Postgres binary to your system PATH.

                In Control Panel, under the Advanced tab of System Properties, click Environment Variables. Edit the Path variable by adding the path to the SQL binary you just installed.

                The path will look something like this, though it may differ slightly depending on your installed version:

                ```
                C:\Program Files\PostgreSQL\17\bin
                ```
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={3}>
              <StepHikeCompact.Details title="Verify that psql is working" fullWidth>
                Open your terminal and run the following command:

                ```sh
                psql --version
                ```

                <Admonition type="tip">
                  If you get an error that psql is not available or cannot be found, check that you have correctly added the binary to your system PATH. Also try restarting your terminal.
                </Admonition>
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>
          </StepHikeCompact>
        </TabPanel>

        <TabPanel id="mac" label="MacOS">
          <StepHikeCompact>
            <StepHikeCompact.Step step={1}>
              <StepHikeCompact.Details title="Install Homebrew" fullWidth>
                Install [Homebrew](https://brew.sh/).
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={2}>
              <StepHikeCompact.Details title="Install Postgres" fullWidth>
                Install Postgres via Homebrew by running the following command in your terminal:

                ```sh
                brew install postgresql@17
                ```
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={3}>
              <StepHikeCompact.Details title="Verify that psql is working" fullWidth>
                Restart your terminal and run the following command:

                ```sh
                psql --version
                ```

                If you get an error that psql is not available or cannot be found then the PATH variable is likely either not correctly set or you need to restart your terminal.

                You can add the Postgres installation path to your PATH variable by running the following command:

                ```sh
                brew info postgresql@17
                ```

                The above command will give an output like this:

                ```sh
                If you need to have postgresql@17 first in your PATH, run:

                echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
                ```

                Run the command mentioned and restart the terminal.
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>
          </StepHikeCompact>
        </TabPanel>
      </Tabs>
    </AccordionItem>
  </div>
</Accordion>



## Restore backup using CLI

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create project" fullWidth>
      Create a [new project](https://database.new)
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Configure newly created project" fullWidth>
      In the new project:

      *   If Webhooks were used in the old database, enable [Database Webhooks](/dashboard/project/_/database/hooks).
      *   If any non-default extensions were used in the old database, enable the [Extensions](/dashboard/project/_/database/extensions).
      *   If Replication for Realtime was used in the old database, enable [Publication](/dashboard/project/_/database/publications) on the tables necessary
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Get the new database connection string" fullWidth>
      Go to the [project page](/dashboard/project/_/) and click the "**Connect**" button at the top of the page for the connection string.

      <Admonition type="note">
        Use the Session pooler connection string by default. If your ISP supports IPv6, use the direct connection string.
      </Admonition>

      Session pooler connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
      ```

      Direct connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.com:5432/postgres
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Get the database password" fullWidth>
      Reset the password in the [project connect page](/dashboard/project/_?showConnect=true).

      Replace `[YOUR-PASSWORD]` in the connection string with the database password.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Restore your Project with the CLI" fullWidth>
      <Tabs scrollable size="small" type="underlined" defaultActiveId="no-column-encryption">
        <TabPanel id="no-column-encryption" label="Column encryption disabled">
          Run these commands after replacing `[CONNECTION_STRING]` with your connection string from the previous steps:

          ```bash
          psql \
            --single-transaction \
            --variable ON_ERROR_STOP=1 \
            --file roles.sql \
            --file schema.sql \
            --command 'SET session_replication_role = replica' \
            --file data.sql \
            --dbname [CONNECTION_STRING]
          ```
        </TabPanel>

        <TabPanel id="column-encryption" label="Column encryption enabled">
          If you use [column encryption](/docs/guides/database/column-encryption), copy the root encryption key to your new project using your [Personal Access Token](/dashboard/account/tokens).

          You can restore the project using both the old and new project ref (the project ref is the value between "https://" and ".supabase.co" in the URL) instead of the URL.

          ```bash
          export OLD_PROJECT_REF="<old_project_ref>"
          export NEW_PROJECT_REF="<new_project_ref>"
          export SUPABASE_ACCESS_TOKEN="<personal_access_token>"

          curl "https://api.supabase.com/v1/projects/$OLD_PROJECT_REF/pgsodium" \
            -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" |
          curl "https://api.supabase.com/v1/projects/$NEW_PROJECT_REF/pgsodium" \
            -H "Authorization: Bearer $SUPABASE_ACCESS_TOKEN" \
            -X PUT --json @-
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Important project restoration notes


### Troubleshooting notes

*   Setting the `session_replication_role` to `replica` disables all triggers so that columns are not double encrypted.
*   If you have created any [custom roles](/dashboard/project/_/database/roles) with `login` attribute, you have to manually set their passwords in the new project.
*   If you run into any permission errors related to `supabase_admin` during restore, edit the `schema.sql` file and comment out any lines containing `ALTER ... OWNER TO "supabase_admin"`.


### Preserving migration history

If you were using Supabase CLI for managing migrations on your old database and would like to preserve the migration history in your newly restored project, you need to insert the migration records separately using the following commands.

```bash
supabase db dump --db-url "$OLD_DB_URL" -f history_schema.sql --schema supabase_migrations
supabase db dump --db-url "$OLD_DB_URL" -f history_data.sql --use-copy --data-only --schema supabase_migrations
psql \
  --single-transaction \
  --variable ON_ERROR_STOP=1 \
  --file history_schema.sql \
  --file history_data.sql \
  --dbname "$NEW_DB_URL"
```


### Schema changes to `auth` and `storage`

If you have modified the `auth` and `storage` schemas in your old project, such as adding triggers or Row Level Security(RLS) policies, you have to restore them separately. The Supabase CLI can help you diff the changes to these schemas using the following commands.

```bash
supabase link --project-ref "$OLD_PROJECT_REF"
supabase db diff --linked --schema auth,storage > changes.sql
```


### Migrate storage objects

The new project has the old project's Storage buckets, but the Storage objects need to be migrated manually. Use this script to move storage objects from one project to another.

```js
// npm install @supabase/supabase-js@2
const { createClient } = require('@supabase/supabase-js')

const OLD_PROJECT_URL = 'https://xxx.supabase.co'
const OLD_PROJECT_SERVICE_KEY = 'old-project-service-key-xxx'

const NEW_PROJECT_URL = 'https://yyy.supabase.co'
const NEW_PROJECT_SERVICE_KEY = 'new-project-service-key-yyy'

;(async () => {
  const oldSupabaseRestClient = createClient(OLD_PROJECT_URL, OLD_PROJECT_SERVICE_KEY, {
    db: {
      schema: 'storage',
    },
  })
  const oldSupabaseClient = createClient(OLD_PROJECT_URL, OLD_PROJECT_SERVICE_KEY)
  const newSupabaseClient = createClient(NEW_PROJECT_URL, NEW_PROJECT_SERVICE_KEY)

  // make sure you update max_rows in postgrest settings if you have a lot of objects
  // or paginate here
  const { data: oldObjects, error } = await oldSupabaseRestClient.from('objects').select()
  if (error) {
    console.log('error getting objects from old bucket')
    throw error
  }

  for (const objectData of oldObjects) {
    console.log(`moving ${objectData.id}`)
    try {
      const { data, error: downloadObjectError } = await oldSupabaseClient.storage
        .from(objectData.bucket_id)
        .download(objectData.name)
      if (downloadObjectError) {
        throw downloadObjectError
      }

      const { _, error: uploadObjectError } = await newSupabaseClient.storage
        .from(objectData.bucket_id)
        .upload(objectData.name, data, {
          upsert: true,
          contentType: objectData.metadata.mimetype,
          cacheControl: objectData.metadata.cacheControl,
        })
      if (uploadObjectError) {
        throw uploadObjectError
      }
    } catch (err) {
      console.log('error moving ', objectData)
      console.log(err)
    }
  }
})()
```



# Restore Dashboard backup

Learn how to restore your dashboard backup to a new Supabase project


## Before you begin

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6">
  <div className="border-b mt-3 pb-3">
    <AccordionItem header="Install Postgres and psql" id="install-postgres">
      <Tabs scrollable size="small" type="underlined" defaultActiveId="windows">
        <TabPanel id="windows" label="Windows">
          <StepHikeCompact>
            <StepHikeCompact.Step step={1}>
              <StepHikeCompact.Details title="Install Postgres" fullWidth>
                Download and run the installation file for the latest version from the [Postgres installer download page](https://www.postgresql.org/download/windows/).
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={2}>
              <StepHikeCompact.Details title="Add Postgres to your system PATH" fullWidth>
                Add the Postgres binary to your system PATH.

                In Control Panel, under the Advanced tab of System Properties, click Environment Variables. Edit the Path variable by adding the path to the SQL binary you just installed.

                The path will look something like this, though it may differ slightly depending on your installed version:

                ```
                C:\Program Files\PostgreSQL\17\bin
                ```
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={3}>
              <StepHikeCompact.Details title="Verify that psql is working" fullWidth>
                Open your terminal and run the following command:

                ```sh
                psql --version
                ```

                <Admonition type="tip">
                  If you get an error that psql is not available or cannot be found, check that you have correctly added the binary to your system PATH. Also try restarting your terminal.
                </Admonition>
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>
          </StepHikeCompact>
        </TabPanel>

        <TabPanel id="mac" label="MacOS">
          <StepHikeCompact>
            <StepHikeCompact.Step step={1}>
              <StepHikeCompact.Details title="Install Homebrew" fullWidth>
                Install [Homebrew](https://brew.sh/).
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={2}>
              <StepHikeCompact.Details title="Install Postgres" fullWidth>
                Install Postgres via Homebrew by running the following command in your terminal:

                ```sh
                brew install postgresql@17
                ```
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>

            <StepHikeCompact.Step step={3}>
              <StepHikeCompact.Details title="Verify that psql is working" fullWidth>
                Restart your terminal and run the following command:

                ```sh
                psql --version
                ```

                If you get an error that psql is not available or cannot be found then the PATH variable is likely either not correctly set or you need to restart your terminal.

                You can add the Postgres installation path to your PATH variable by running the following command:

                ```sh
                brew info postgresql@17
                ```

                The above command will give an output like this:

                ```sh
                If you need to have postgresql@17 first in your PATH, run:

                echo 'export PATH="/opt/homebrew/opt/postgresql@17/bin:$PATH"' >> ~/.zshrc
                ```

                Run the command mentioned and restart the terminal.
              </StepHikeCompact.Details>
            </StepHikeCompact.Step>
          </StepHikeCompact>
        </TabPanel>
      </Tabs>
    </AccordionItem>
  </div>

  <div className="border-b mt-3 pb-3">
    <AccordionItem header="Create and configure a new project" id="create-project">
      <StepHikeCompact>
        <StepHikeCompact.Step step={1}>
          <StepHikeCompact.Details title="Create New project" fullWidth>
            Create a new [Supabase project](https://database.new)
          </StepHikeCompact.Details>
        </StepHikeCompact.Step>

        <StepHikeCompact.Step step={2}>
          <StepHikeCompact.Details title="Configure your new project" fullWidth>
            In your new project:

            *   If you were using Webhooks, enable [Database Webhooks](/dashboard/project/_/database/hooks).
            *   If you were using any extensions, enable the [Extensions](/dashboard/project/_/database/extensions).
            *   If you were using Replication for Realtime, enable [Publication](/dashboard/project/_/database/publications) where needed.
          </StepHikeCompact.Details>
        </StepHikeCompact.Step>
      </StepHikeCompact>
    </AccordionItem>
  </div>
</Accordion>



## Things to keep in mind

Here are some things that are not stored directly in your database and will require you to re-create or setup on the new project:

*   Edge Functions
*   Auth Settings and API keys
*   Realtime settings
*   Database extensions and settings
*   Read Replicas



## Restore backup

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Get the new database connection string" fullWidth>
      On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true).

      <Admonition type="note">
        Use the [Session pooler](/dashboard/project/_?showConnect=true\&method=session) connection string by default. If your ISP supports IPv6 or you have the IPv4 add-on enabled, use the direct connection string.
      </Admonition>

      Session pooler connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres
      ```

      Direct connection string:

      ```bash
        postgresql://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.com:5432/postgres
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Get the database password" fullWidth>
      <Admonition type="caution">
        It can take a few minutes for the database password reset to take effect. Especially if multiple password resets are done.
      </Admonition>

      Reset the password in the [Database Settings](/dashboard/project/_/database/settings).

      Replace `[YOUR-PASSWORD]` in the connection string with the database password.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Get the backup file path" fullWidth>
      Get the relative file path of the downloaded backup file.

      If the restore is done in the same directory as the downloaded backup, the file path would look like this:

      `./backup_name.backup`
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Verify the backup file format" fullWidth>
      The backup file will be gzipped with a .gz extension. You will need to unzip the file to look like this:

      `backup_name.backup`
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Restore your backup" fullWidth>
      <StepHikeCompact.Code>
        ```sql
        psql -d [CONNECTION_STRING] -f /file/path
        ```
      </StepHikeCompact.Code>

      Replace `[CONNECTION_STRING]` with connection string from Steps 1 & 2.

      Replace `/file/path` with the file path from Step 3.

      Run the command with the replaced values to restore the backup to your new project.
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Migrate storage objects to new project's S3 storage

After restoring the backup, the buckets and files metadata will show up in the dashboard of the new project.
However, the storage files stored in the S3 buckets would not be present.

Use the following Google Colab script provided below to migrate your downloaded storage objects to your new project's S3 buckets.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PLyn/supabase-storage-migrate/blob/main/Supabase_Storage_migration.ipynb)

This method requires uploading to Google Colab and then to the S3 buckets. This could add significant upload time if there are large storage objects.



## Common errors with the backup restore process

"**object already exists**"
"**constraint x for relation y already exists**"
"**Many other variations of errors**"

These errors are expected when restoring to a new Supabase project. The backup from the dashboard is a full dump which contains the CREATE commands for all schemas. This is by design as the full dump allows you to rebuild the entire database from scratch even outside of Supabase.

One side effect of this method is that a new Supabase project has these commands already applied to schemas like storage and auth. The errors from this are not an issue because it skips to the next command to run. Another side effect of this is that all triggers will run during the restoration process which is not ideal but generally is not a problem.

There are circumstances where this method can fail and if it does, you should reach out to Supabase support for help.

"**psql: error: connection to server at "aws-0-us-east-1.pooler.supabase.com" (44.216.29.125), port 5432 failed: received invalid response to GSSAPI negotiation:**"

You are possibly using psql and Postgres version 15 or lower. Completely remove the Postgres installation and install the latest version as per the instructions above to resolve this issue.

"**psql: error: connection to server at "aws-0-us-east-1.pooler.supabase.com" (44.216.29.125), port 5432 failed: error received from server in SCRAM exchange: Wrong password**"

If the database password was reset, it may take a few minutes for it to reflect. Try again after a few minutes if you did a password reset.



# Migrate from Amazon RDS to Supabase

Migrate your Amazon RDS MySQL or MS SQL database to Supabase.

This guide aims to exhibit the process of transferring your Amazon RDS database from any of these engines Postgres, MySQL or MS SQL to Supabase's Postgres database. Although Amazon RDS is a favored managed database service provided by AWS, it may not suffice for all use cases. Supabase, on the other hand, provides an excellent free and open source option that encompasses all the necessary backend features to develop a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage.

Supabase's core is Postgres, enabling the use of row-level security and providing access to over 40 Postgres extensions. By migrating from Amazon RDS to Supabase, you can leverage Postgres to its fullest potential and acquire all the features you need to complete your project.



## Retrieve your Amazon RDS database credentials \[#retrieve-rds-credentials]

1.  Log in to your [Amazon RDS account](https://aws.amazon.com/rds/).
2.  Select the region where your RDS database is located.
3.  Navigate to the **Databases** tab.
4.  Select the database that you want to migrate.
5.  In the **Connectivity & Security** tab, note down the Endpoint and the port number.
6.  In the **Configuration** tab, note down the Database name and the Username.
7.  If you do not have the password, create a new one and note it down.

![Copying RDS credentials from AWS Management Console](/docs/img/guides/resources/migrating-to-supabase/amazon-rds/amazon-rds_credentials.png)



## Retrieve your Supabase host \[#retrieve-supabase-host]

1.  If you're new to Supabase, [create a project](https://database.new). Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).
2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)
3.  Under the Session pooler, click on the View parameters under the connect string. Note your Host (`$SUPABASE_HOST`).

![Finding Supabase host address](/docs/img/guides/resources/migrating-to-supabase/amazon-rds/database-settings-host.png)



## Migrate the database

The fastest way to migrate your database is with the Supabase migration tool on
[Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb).

Alternatively, you can use [pgloader](https://github.com/dimitri/pgloader), a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

<Tabs scrollable size="small" type="underlined" defaultActiveId="colab" queryGroup="migrate-method">
  <TabPanel id="colab" label="Migrate using Colab">
    1.  Select the Database Engine from the Source database in the dropdown
    2.  Set the environment variables (`HOST`, `USER`, `SOURCE_DB`,`PASSWORD`, `SUPABASE_URL`, and `SUPABASE_PASSWORD`) in the Colab notebook.
    3.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb) in order. The first sets engine and installs the necessary files.
    4.  Run the third step to start the migration. This will take a few minutes.
  </TabPanel>

  <TabPanel id="MySQL" label="Migrate from MySQL with pgloader">
    1.  Install pgloader.

    2.  Create a configuration file (e.g., config.load).

        For your destination, use your Supabase connection string with `Use connection pooling` enabled, and the mode set to `Session`. You can get the string from your [`Database Settings`](/dashboard/project/_/settings/general).

        ```sql
        load database
          from mysql://user:password@host/source_db
          into postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
        alter schema 'public' owner to 'postgres';
        set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
        ```

    3.  Run the migration with pgloader

        ```bash
        pgloader config.load
        ```
  </TabPanel>

  <TabPanel id="MS SQL" label="Migrate from MSSQL">
    1.  Install pgloader.

    2.  Create a configuration file (e.g., config.load).

        ```sql
        LOAD DATABASE
            FROM mssql://USER:PASSWORD@HOST/SOURCE_DB
            INTO postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres
        ALTER SCHEMA 'public' OWNER TO 'postgres';
        set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
        ```

    3.  Run the migration with pgloader

        ```bash
        pgloader config.load
        ```
  </TabPanel>
</Tabs>

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from Auth0 to Supabase Auth

Learn how to migrate your users from Auth0

You can migrate your users from Auth0 to Supabase Auth.

Changing authentication providers for a production app is an important operation. It can affect most aspects of your application. Prepare in advance by reading this guide, and develop a plan for handling the key migration steps and possible problems.

With advance planning, a smooth and safe Auth migration is possible.



## Before you begin

Before beginning, consider the answers to the following questions. They will help you need decide if you need to migrate, and which strategy to use:

*   How do Auth provider costs scale as your user base grows?
*   Does the new Auth provider provide all needed features? (for example, OAuth, password logins, Security Assertion Markup Language (SAML), Multi-Factor Authentication (MFA))
*   Is downtime acceptable during the migration?
*   What is your timeline to migrate before terminating the old Auth provider?



## Migration strategies

Depending on your evaluation, you may choose to go with one of the following strategies:

1.  Rolling migration
2.  One-off migration

| Strategy | Advantages                                                                                     | Disadvantages                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rolling  | <ul><li>0 downtime</li><li>Users may need to log in again</li></ul>                            | <ul><li>Need to maintain 2 different Auth services, which may be more costly in the short-term</li><li>Need to maintain separate codepaths for the period of the migration</li><li>Some existing users may be inactive and have not signed in with the new provider. This means that you eventually need to backfill these users. However, this is a much smaller-scale one-off migration with lower risks since these users are inactive.</li></ul> |
| One-off  | <ul><li>No need to maintain 2 different auth services for an extended period of time</li></ul> | <ul><li>Some downtime</li><li>Users will need to log in again. Risky for active users.</li></ul>                                                                                                                                                                                                                                                                                                                                                     |



## Migration steps

Auth provider migrations require 2 main steps:

1.  Export your user data from the old provider (Auth0)
2.  Import the data into your new provider (Supabase Auth)


### Step 1: Export your user data

Auth0 provides two methods for exporting user data:

1.  Use the [Auth0 data export feature](https://auth0.com/docs/troubleshoot/customer-support/manage-subscriptions/export-data)
2.  Use the [Auth0 management API](https://auth0.com/docs/api/management/v2/users/get-users). This endpoint has a rate limit, so you may need to export your users in several batches.

To export password hashes and MFA factors, contact Auth0 support.


### Step 2: Import your users into Supabase Auth

The steps for importing your users depends on the login methods that you support.

See the following sections for how to import users with:

*   [Password-based login](#password-based-methods)
*   [Passwordless login](#passwordless-methods)
*   [OAuth](#oauth)


#### Password-based methods

For users who sign in with passwords, we recommend a hybrid approach to reduce downtime:

1.  For new users, use Supabase Auth for sign up.
2.  Migrate existing users in a one-off migration.


##### Sign up new users

Sign up new users using Supabase Auth's [signin methods](/docs/guides/auth/passwords#signing-up-with-an-email-and-password).


##### Migrate existing users to Supabase Auth

Migrate existing users to Supabase Auth. This requires two main steps: first, check which users need to be migrated, then create their accounts using the Supabase admin endpoints.

1.  Get your Auth 0 user export and password hash export lists.

2.  Filter for users who use password login.
    *   Under the `identities` field in the user object, these users will have `auth0` as a provider. In the same identity object, you can find their Auth0 `user_id`.
    *   Check that the user has a corresponding password hash by comparing their Auth0 `user_id` to the `oid` field in the password hash export.

3.  Use Supabase Auth's [admin create user](/docs/reference/javascript/auth-admin-createuser) method to recreate the user in Supabase Auth. If the user has a confirmed email address or phone number, set `email_confirm` or `phone_confirm` to `true`.

    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const { data, error } = await supabase.auth.admin.createUser({
      email: 'valid.email@supabase.io',
      password_hash: '$2y$10$a9pghn27d7m0ltXvlX8LiOowy7XfFw0hW0G80OjKYQ1jaoejaA7NC',
      email_confirm: true,
    })
    ```

    <Admonition type="note" label="Supported password hashing algorithms">
      Supabase supports bcrypt and Argon2 password hashes.
    </Admonition>

    If you have a plaintext password instead of a hash, you can provide that instead. Supabase Auth will handle hashing the password for you. (Passwords are **always** stored hashed.)

    ```ts
    import { createClient } from '@supabase/supabase-js'
    const supabase = createClient('your_project_url', 'your_supabase_api_key')

    // ---cut---
    const { data, error } = await supabase.auth.admin.createUser({
      email: 'valid.email@supabase.io',
      password: 'supersecurepassword123!',
    })
    ```

4.  To sign in your migrated users, use the Supabase Auth [sign in methods](/docs/reference/javascript/auth-signinwithpassword).

    To check for edge cases where users aren't successfully migrated, use a fallback strategy. This ensures that users can continue to sign in seamlessly:

    1.  Try to sign in the user with Supabase Auth.
    2.  If the signin fails, try to sign in with Auth0.
    3.  If Auth0 signin succeeds, call the admin create user method again to create the user in Supabase Auth.


#### Passwordless methods

For passwordless signin via email or phone, check for users with verified email addresses or phone numbers. Create these users in Supabase Auth with `email_confirm` or `phone_confirm` set to `true`:

```ts
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const { data, error } = await supabase.auth.admin.createUser({
  email: 'valid.email@supabase.io',
  email_confirm: true,
})
```

Check your Supabase Auth [email configuration](/docs/guides/auth/auth-smtp) and configure your [email template](/dashboard/project/_/auth/templates) for use with magic links. See the [Email templates guide](/docs/guides/auth/auth-email-templates) to learn more.

Once you have imported your users, you can sign them in using the [`signInWithOtp`](/docs/reference/javascript/auth-signinwithotp) method.


#### OAuth

Configure your OAuth providers in Supabase by following the [Social login guides](/docs/guides/auth/social-login).

For both new and existing users, sign in the user using the [`signInWithOAuth`](/docs/reference/javascript/auth-signinwithoauth) method. This works without pre-migrating existing users, since the user always needs to sign in through the OAuth provider before being redirected to your service.

After the user has completed the OAuth flow successfully, you can check if the user is a new or existing user in Auth0 by mapping their social provider id to Auth0. Auth0 stores the social provider ID in the user ID, which has the format `provider_name|provider_id` (for example, `github|123456`). See the [Auth0 identity docs](https://auth0.com/docs/manage-users/user-accounts/identify-users) to learn more.



## Mapping between Auth0 and Supabase Auth

Each Auth provider has its own schema for tracking users and user information.

In Supabase Auth, your users are stored in your project's database under the `auth` schema. Every user has an identity (unless the user is an anonymous user), which represents the signin method they can use with Supabase. This is represented by the `auth.users` and `auth.identities` table.

See the [Users](/docs/guides/auth/users) and [Identities](/docs/guides/auth/identities) sections to learn more.


### Mapping user metadata and custom claims

Supabase Auth provides 2 fields which you can use to map user-specific metadata from Auth0:

*   `auth.users.raw_user_meta_data` : For storing non-sensitive user metadata that the user can update (e.g full name, age, favorite color).
*   `auth.users.raw_app_meta_data` : For storing non-sensitive user metadata that the user should not be able to update (e.g pricing plan, access control roles).

Both columns are accessible from the admin user methods. To create a user with custom metadata, you can use the following method:

```ts
import { createClient } from '@supabase/supabase-js'
const supabase = createClient('your_project_url', 'your_supabase_api_key')

// ---cut---
const { data, error } = await supabase.auth.admin.createUser({
  email: 'valid.email@supabase.io',
  user_metadata: {
    full_name: 'Foo Bar',
  },
  app_metadata: {
    role: 'admin',
  },
})
```

<Admonition type="caution">
  These fields will be exposed in the user's access token JWT so it is recommended not to store excessive metadata in these fields.
</Admonition>

These fields are stored as columns in the `auth.users` table using the `jsonb` type. Both fields can be updated by using the admin [`updateUserById` method](/docs/reference/javascript/auth-admin-updateuserbyid). If you want to allow the user to update their own `raw_user_meta_data` , you can use the [`updateUser` method](/docs/reference/javascript/auth-updateuser).

If you have a lot of user-specific metadata to store, it is recommended to create your own table in a private schema that uses the user id as a foreign key:

```sql
create table private.user_metadata (
	id int generated always as identity,
	user_id uuid references auth.users(id) on delete cascade,
	user_metadata jsonb
);
```



## Frequently Asked Questions (FAQ)

<Accordion type="default" openBehaviour="multiple" chevronAlign="right" justified size="medium" className="text-foreground-light mt-8 mb-6 [&>div]:space-y-4">
  <AccordionItem header={<span className="text-foreground">I have IDs assigned to existing users in my database, how can I maintain these IDs?</span>} id="custom-user-id">
    All users stored in Supabase Auth use the UUID V4 format as the ID. If your UUID format is identical, you can specify it in the admin create user method like this:

    <Admonition type="note">
      New users in Supabase Auth will always be created with a UUID V4 ID by default.
    </Admonition>

    ```ts
    // specify a custom id
    const { data, error } = await supabase.auth.admin.createUser({
      id: 'e7f5ae65-376e-4d05-a18c-10a91295727a',
      email: 'valid.email@supabase.io',
    })
    ```
  </AccordionItem>

  <AccordionItem header={<span className="text-foreground">How can I allow my users to retain their existing password?</span>} id="existing-password">
    Supabase Auth never stores passwords as plaintext. Since Supabase Auth supports reading bcrypt and argon2 password hashes, you can import your users passwords if they use the same hashing algorithm. New users in Supabase Auth who use password-based sign-in methods will always use a bcrypt hash. Passwords are stored in the `auth.users.encrypted_password` column.
  </AccordionItem>

  <AccordionItem header={<span className="text-foreground">My users have multi-factor authentication (MFA) enabled, how do I make sure they don't have to set up MFA again?</span>} id="mfa">
    You can obtain an export of your users' MFA secrets by opening a support ticket with Auth0, similar to obtaining the export for password hashes. Supabase Auth only supports time-based one-time passwords (TOTP). Users who have TOTP-based factors may need to re-enroll using their choice of TOTP-based authenticator instead (e.g. 1Password / Google authenticator).
  </AccordionItem>

  <AccordionItem header={<span className="text-foreground">How do I migrate existing SAML Single Sign-On (SSO) connections?</span>} id="saml">
    Customers may need to link their identity provider with Supabase Auth separately, but their users should still be able to sign-in as per-normal after authenticating with their identity provider. For more information about SSO with SAML 2.0, you can check out [this guide](/docs/guides/auth/enterprise-sso/auth-sso-saml). If you want to migrate your existing SAML SSO connections from Auth0 to Supabase Auth, reach out to us via support.
  </AccordionItem>

  <AccordionItem header={<span className="text-foreground">How do I migrate my Auth0 organizations to Supabase?</span>} id="migrate-org">
    This isn't supported by Supabase Auth yet.
  </AccordionItem>
</Accordion>



## Useful references

*   [Migrating 125k users from Auth0 to Supabase](https://kevcodez.medium.com/migrating-125-000-users-from-auth0-to-supabase-81c0568de307)
*   [Loper to Supabase migration](https://eigen.sh/posts/auth-migration)



# Migrate from Firebase Auth to Supabase

Migrate Firebase auth users to Supabase Auth.

Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/auth) to help migrate auth users from a Firebase project to a Supabase project. There are two parts to the migration process:

*   `firestoreusers2json` ([TypeScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/firestoreusers2json.ts), [JavaScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/firestoreusers2json.js)) exports users from an existing Firebase project to a `.json` file on your local system.
*   `import_users` ([TypeScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/import_users.ts), [JavaScript](https://github.com/supabase-community/firebase-to-supabase/blob/main/auth/import_users.js)) imports users from a saved `.json` file into your Supabase project (inserting those users into the `auth.users` table of your `Postgres` database instance).



## Set up the migration tool \[#set-up-migration-tool]

1.  Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:

    ```bash
    git clone https://github.com/supabase-community/firebase-to-supabase.git
    ```

2.  In the `/auth` directory, create a file named `supabase-service.json` with the following contents:

    ```json
    {
      "host": "database.server.com",
      "password": "secretpassword",
      "user": "postgres",
      "database": "postgres",
      "port": 5432
    }
    ```

3.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

4.  Under the Session pooler, click on the View parameters under the connect string. Replace the `Host` and `User` fields with the values shown.

5.  Enter the password you used when you created your Supabase project in the `password` entry in the `supabase-service.json` file.



## Generate a Firebase private key \[#generate-firebase-private-key]

1.  Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
2.  Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
3.  Click **Service Accounts** and select **Firebase Admin SDK**.
4.  Click **Generate new private key**.
5.  Rename the downloaded file to `firebase-service.json`.



## Save your Firebase password hash parameters \[#save-firebase-hash-parameters]

1.  Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
2.  Select **Authentication** (Build section) in the sidebar.
3.  Select **Users** in the top menu.
4.  At the top right of the users list, open the menu (3 dots) and click **Password hash parameters**.
5.  Copy and save the parameters for `base64_signer_key`, `base64_salt_separator`, `rounds`, and `mem_cost`.

```text Sample
hash_config {
  algorithm: SCRYPT,
  base64_signer_key: XXXX/XXX+XXXXXXXXXXXXXXXXX+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX==,
  base64_salt_separator: Aa==,
  rounds: 8,
  mem_cost: 14,
}
```



## Command line options


### Dump Firestore users to a JSON file \[#dump-firestore-users]

`node firestoreusers2json.js [<filename.json>] [<batch_size>]`

*   `filename.json`: (optional) output filename (defaults to `./users.json`)
*   `batchSize`: (optional) number of users to fetch in each batch (defaults to 100)


### Import JSON users file to Supabase Auth (Postgres: `auth.users`) \[#import-json-users-file]

`node import_users.js <path_to_json_file> [<batch_size>]`

*   `path_to_json_file`: full local path and filename of JSON input file (of users)
*   `batch_size`: (optional) number of users to process in a batch (defaults to 100)



## Notes

For more advanced migrations, including the use of a middleware server component for verifying a user's existing Firebase password and updating that password in your Supabase project the first time a user logs in, see the [`firebase-to-supabase` repo](https://github.com/supabase-community/firebase-to-supabase/tree/main/auth).



## Resources

*   [Supabase vs Firebase](/alternatives/supabase-vs-firebase)
*   [Firestore Data Migration](/docs/guides/migrations/firestore-data)
*   [Firestore Storage Migration](/docs/guides/migrations/firebase-storage)



## Migrate to Supabase

[Contact us](https://forms.supabase.com/firebase-migration) if you need more help migrating your project.



# Migrated from Firebase Storage to Supabase

Migrate Firebase Storage files to Supabase Storage.

Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/storage) to convert storage files from Firebase Storage to Supabase Storage. Conversion is a two-step process:

1.  Files are downloaded from a Firebase storage bucket to a local filesystem.
2.  Files are uploaded from the local filesystem to a Supabase storage bucket.



## Set up the migration tool \[#set-up-migration-tool]

1.  Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:

    ```bash
    git clone https://github.com/supabase-community/firebase-to-supabase.git
    ```

2.  In the `/storage` directory, rename [supabase-keys-sample.js](https://github.com/supabase-community/firebase-to-supabase/blob/main/storage/supabase-keys-sample.js) to `supabase-keys.js`.

3.  Go to your Supabase project's [API settings](/dashboard/project/_/settings/api) in the Dashboard.

4.  Copy the **Project URL** and update the `SUPABASE_URL` value in `supabase-keys.js`.

5.  Under **Project API keys**, copy the **service\_role** key and update the `SUPABASE_KEY` value in `supabase-keys.js`.



## Generate a Firebase private key \[#generate-firebase-private-key]

1.  Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
2.  Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
3.  Click **Service Accounts** and select **Firebase Admin SDK**.
4.  Click **Generate new private key**.
5.  Rename the downloaded file to `firebase-service.json`.



## Command line options


### Download Firestore Storage bucket to a local filesystem folder \[#download-firestore-storage-bucket]

`node download.js <prefix> [<folder>] [<batchSize>] [<limit>] [<token>]`

*   `<prefix>`: The prefix of the files to download. To process the root bucket, use an empty prefix: "".
*   `<folder>`: (optional) Name of subfolder for downloaded files. The selected folder is created as a subfolder of the current folder (e.g., `./downloads/`). The default is `downloads`.
*   `<batchSize>`: (optional) The default is 100.
*   `<limit>`: (optional) Stop after processing this many files. For no limit, use `0`.
*   `<token>`: (optional) Begin processing at this `pageToken`.

To process in batches using multiple command-line executions, you must use the same parameters with a new `<token>` on subsequent calls. Use the token displayed on the last call to continue the process at a given point.


### Upload files to Supabase Storage bucket \[#upload-to-supabase-storage-bucket]

`node upload.js <prefix> <folder> <bucket>`

*   `<prefix>`: The prefix of the files to download. To process all files, use an empty prefix: "".
*   `<folder>`: Name of subfolder of files to upload. The selected folder is read as a subfolder of the current folder (e.g., `./downloads/`). The default is `downloads`.
*   `<bucket>`: Name of the bucket to upload to.

<Admonition type="note">
  If the bucket doesn't exist, it's created as a `non-public` bucket. You must set permissions on this new bucket in the [Supabase Dashboard](/dashboard/project/_/storage/buckets) before users can download any files.
</Admonition>



## Resources

*   [Supabase vs Firebase](/alternatives/supabase-vs-firebase)
*   [Firestore Data Migration](/docs/guides/migrations/firestore-data)
*   [Firebase Auth Migration](/docs/guides/migrations/firebase-auth)



## Migrate to Supabase

[Contact us](https://forms.supabase.com/firebase-migration) if you need more help migrating your project.



# Migrate from Firebase Firestore to Supabase

Migrate your Firebase Firestore database to a Supabase Postgres database.

Supabase provides several [tools](https://github.com/supabase-community/firebase-to-supabase/tree/main/firestore) to convert data from a Firebase Firestore database to a Supabase Postgres database. The process copies the entire contents of a single Firestore `collection` to a single Postgres `table`.

The Firestore `collection` is "flattened" and converted to a table with basic columns of one of the following types: `text`, `numeric`, `boolean`, or `jsonb`. If your structure is more complex, you can write a program to split the newly-created `json` file into multiple, related tables before you import your `json` file(s) to Supabase.



## Set up the migration tool \[#set-up-migration-tool]

1.  Clone the [`firebase-to-supabase`](https://github.com/supabase-community/firebase-to-supabase) repository:

    ```bash
    git clone https://github.com/supabase-community/firebase-to-supabase.git
    ```

2.  In the `/firestore` directory, create a file named `supabase-service.json` with the following contents:

    ```json
    {
      "host": "database.server.com",
      "password": "secretpassword",
      "user": "postgres",
      "database": "postgres",
      "port": 5432
    }
    ```

3.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

4.  Under the Session pooler, click on the View parameters under the connect string. Replace the `Host` and `User` fields with the values shown.

5.  Enter the password you used when you created your Supabase project in the `password` entry in the `supabase-service.json` file.



## Generate a Firebase private key \[#generate-firebase-private-key]

1.  Log in to your [Firebase Console](https://console.firebase.google.com/project) and open your project.
2.  Click the gear icon next to **Project Overview** in the sidebar and select **Project Settings**.
3.  Click **Service Accounts** and select **Firebase Admin SDK**.
4.  Click **Generate new private key**.
5.  Rename the downloaded file to `firebase-service.json`.



## Command line options


### List all Firestore collections

`node collections.js`


### Dump Firestore collection to JSON file

`node firestore2json.js <collectionName> [<batchSize>] [<limit>]`

*   `batchSize` (optional) defaults to 1000
*   output filename is `<collectionName>.json`
*   `limit` (optional) defaults to 0 (no limit)


#### Customize the JSON file with hooks

You can customize the way your JSON file is written using a [custom hook](#custom-hooks). A common use for this is to "flatten" the JSON file, or to split nested data into separate, related database tables. For example, you could take a Firestore document that looks like this:

```json Firestore
[{ "user": "mark", "score": 100, "items": ["hammer", "nail", "glue"] }]
```

And split it into two files (one table for users and one table for items):

```json Users
[{ "user": "mark", "score": 100 }]
```

```json Items
[
  { "user": "mark", "item": "hammer" },
  { "user": "mark", "item": "nail" },
  { "user": "mark", "item": "glue" }
]
```


### Import JSON file to Supabase (Postgres) \[#import-to-supabase]

`node json2supabase.js <path_to_json_file> [<primary_key_strategy>] [<primary_key_name>]`

*   `<path_to_json_file>` The full path of the file you created in the previous step (`Dump Firestore collection to JSON file `), such as `./my_collection.json`
*   `[<primary_key_strategy>]` (optional) Is one of:
    *   `none` (default) No primary key is added to the table.
    *   `smallserial` Creates a key using `(id SMALLSERIAL PRIMARY KEY)` (autoincrementing 2-byte integer).
    *   `serial` Creates a key using `(id SERIAL PRIMARY KEY)` (autoincrementing 4-byte integer).
    *   `bigserial` Creates a key using `(id BIGSERIAL PRIMARY KEY)` (autoincrementing 8-byte integer).
    *   `uuid` Creates a key using `(id UUID PRIMARY KEY DEFAULT gen_random_uuid())` (randomly generated UUID).
    *   `firestore_id` Creates a key using `(id TEXT PRIMARY KEY)` (uses existing `firestore_id` random text as key).
*   `[<primary_key_name>]` (optional) Name of primary key. Defaults to "id".



## Custom hooks

Hooks are used to customize the process of exporting a collection of Firestore documents to JSON. They can be used for:

*   Customizing or modifying keys
*   Calculating data
*   Flattening nested documents into related SQL tables


### Write a custom hook


#### Create a `.js` file for your collection

If your Firestore collection is called `users`, create a file called `users.js` in the current folder.


#### Construct your `.js` file

The basic format of a hook file looks like this:

```js
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  // modify the doc here
  return doc
}
```


##### Parameters

*   `collectionName`: The name of the collection you are processing.
*   `doc`: The current document (JSON object) being processed.
*   `recordCounters`: An internal object that keeps track of how many records have been processed in each collection.
*   `writeRecord`: This function automatically handles the process of writing data to other JSON files (useful for "flatting" your document into separate JSON files to be written to separate database tables). `writeRecord` takes the following parameters:
    *   `name`: Name of the JSON file to write to.
    *   `doc`: The document to write to the file.
    *   `recordCounters`: The same `recordCounters` object that was passed to this hook (just passes it on).


### Examples


#### Add a new (unique) numeric key to a collection

```js
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  doc.unique_key = recordCounter[collectionName] + 1
  return doc
}
```


#### Add a timestamp of when this record was dumped from Firestore

```js
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  doc.dump_time = new Date().toISOString()
  return doc
}
```


#### Flatten JSON into separate files

Flatten the `users` collection into separate files:

```json
[
  {
    "uid": "abc123",
    "name": "mark",
    "score": 100,
    "weapons": ["toothpick", "needle", "rock"]
  },
  {
    "uid": "xyz789",
    "name": "chuck",
    "score": 9999999,
    "weapons": ["hand", "foot", "head"]
  }
]
```

The `users.js` hook file:

```js
module.exports = (collectionName, doc, recordCounters, writeRecord) => {
  for (let i = 0; i < doc.weapons.length; i++) {
    const weapon = {
      uid: doc.uid,
      weapon: doc.weapons[i],
    }
    writeRecord('weapons', weapon, recordCounters)
  }
  delete doc.weapons // moved to separate file
  return doc
}
```

The result is two separate JSON files:

```json users.json
[
  { "uid": "abc123", "name": "mark", "score": 100 },
  { "uid": "xyz789", "name": "chuck", "score": 9999999 }
]
```

```json weapons.json
[
  { "uid": "abc123", "weapon": "toothpick" },
  { "uid": "abc123", "weapon": "needle" },
  { "uid": "abc123", "weapon": "rock" },
  { "uid": "xyz789", "weapon": "hand" },
  { "uid": "xyz789", "weapon": "foot" },
  { "uid": "xyz789", "weapon": "head" }
]
```



## Resources

*   [Supabase vs Firebase](/alternatives/supabase-vs-firebase)
*   [Firestore Storage Migration](/docs/guides/migrations/firebase-storage)
*   [Firebase Auth Migration](/docs/guides/migrations/firebase-auth)



## Migrate to Supabase

[Contact us](https://forms.supabase.com/firebase-migration) if you need more help migrating your project.



# Migrate from Heroku to Supabase

Migrate your Heroku Postgres database to Supabase.

Supabase is one of the best [free alternatives to Heroku Postgres](/alternatives/supabase-vs-heroku-postgres). This guide shows how to migrate your Heroku Postgres database to Supabase. This migration requires the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) CLI tools, which are installed automatically as part of the complete Postgres installation package.

Alternatively, use the [Heroku to Supabase migration tool](https://migrate.supabase.com/) to migrate in just a few clicks.



## Quick demo

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/xsRhPMphtZ4" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Retrieve your Heroku database credentials \[#retrieve-heroku-credentials]

1.  Log in to your [Heroku account](https://heroku.com) and select the project you want to migrate.
2.  Click **Resources** in the menu and select your **Heroku Postgres** database.
3.  Click **Settings** in the menu.
4.  Click **View Credentials** and save the following information:
    *   Host (`$HEROKU_HOST`)
    *   Database (`$HEROKU_DATABASE`)
    *   User (`$HEROKU_USER`)
    *   Password (`$HEROKU_PASSWORD`)



## Retrieve your Supabase connection string \[#retrieve-supabase-connection-string]

1.  If you're new to Supabase, [create a project](/dashboard).
2.  Get your project's Session pooler connection string from your project dashboard by clicking [Connect](/dashboard/project/_?showConnect=true\&method=session).
3.  Replace \[YOUR-PASSWORD] in the connection string with your database password. You can reset your database password on the [Database Settings page](/dashboard/project/_/database/settings) if you do not have it.



## Export your Heroku database to a file \[#export-heroku-database]

Use `pg_dump` with your Heroku credentials to export your Heroku database to a file (e.g., `heroku_dump.sql`).

```bash
pg_dump --clean --if-exists --quote-all-identifiers \
 -h $HEROKU_HOST -U $HEROKU_USER -d $HEROKU_DATABASE \
 --no-owner --no-privileges > heroku_dump.sql
```



## Import the database to your Supabase project \[#import-database-to-supabase]

Use `psql` to import the Heroku database file to your Supabase project.

```bash
psql -d "$YOUR_CONNECTION_STRING" -f heroku_dump.sql
```



## Additional options

*   To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
*   To exclude a schema: `--exclude-schema=PATTERN`.
*   To only migrate a single table: `--table=PATTERN`.
*   To exclude a table: `--exclude-table=PATTERN`.

Run `pg_dump --help` for a full list of options.

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from MSSQL to Supabase

Migrate your Microsoft SQL Server database to Supabase.

This guide aims to demonstrate the process of transferring your Microsoft SQL Server database to Supabase's Postgres database. Supabase is a powerful and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MSSQL database to Supabase's Postgres enables you to leverage Postgres's capabilities and access all the features you need for your project.



## Retrieve your MSSQL database credentials

Before you begin the migration, you need to collect essential information about your MSSQL database. Follow these steps:

1.  Log in to your MSSQL database provider.
2.  Locate and note the following database details:
    *   Hostname or IP address
    *   Database name
    *   Username
    *   Password



## Retrieve your Supabase host \[#retrieve-supabase-host]

1.  If you're new to Supabase, [create a project](/dashboard).
    Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).

2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

3.  Under the Session pooler, click on the View parameters under the connect string. Note your Host (`$SUPABASE_HOST`).

![Finding Supabase host address](/docs/img/guides/resources/migrating-to-supabase/mssql/database-settings-host.png)



## Migrate the database

The fastest way to migrate your database is with the Supabase migration tool on
[Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb).

Alternatively, you can use [pgloader](https://github.com/dimitri/pgloader), a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

<Tabs scrollable size="small" type="underlined" defaultActiveId="colab" queryGroup="migrate-method">
  <TabPanel id="colab" label="Migrate using Colab">
    1.  Select the Database Engine from the Source database in the dropdown.
    2.  Set the environment variables (`HOST`, `USER`, `SOURCE_DB`,`PASSWORD`, `SUPABASE_URL`, and `SUPABASE_PASSWORD`) in the Colab notebook.
    3.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb) in order. The first sets engine and installs the necessary files.
    4.  Run the third step to start the migration. This will take a few minutes.
  </TabPanel>

  <TabPanel id="MS SQL" label="Migrate from MSSQL">
    1.  Install pgloader.

    2.  Create a configuration file (e.g., config.load).

        For your destination, use your Supabase connection string with `Use connection pooling` enabled, and the mode set to `Session`. You can get the string from your [`Database Settings`](/dashboard/project/_/settings/general).

        ```sql
        LOAD DATABASE
            FROM mssql://USER:PASSWORD@HOST/SOURCE_DB
            INTO postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
        ALTER SCHEMA 'public' OWNER TO 'postgres';
        set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
        ```

    3.  Run the migration with pgloader

        ```bash
        pgloader config.load
        ```
  </TabPanel>
</Tabs>

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from MySQL to Supabase

Migrate your MySQL database to Supabase Postgres database.

This guide aims to exhibit the process of transferring your MySQL database to Supabase's Postgres database. Supabase is a robust and open-source platform offering a wide range of backend features, including a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Migrating your MySQL database to Supabase's Postgres enables you to leverage PostgreSQL's capabilities and access all the features you need for your project.



## Retrieve your MySQL database credentials

Before you begin the migration, you need to collect essential information about your MySQL database. Follow these steps:

1.  Log in to your MySQL database provider.

2.  Locate and note the following database details:
    *   Hostname or IP address
    *   Database name
    *   Username
    *   Password



## Retrieve your Supabase host \[#retrieve-supabase-host]

1.  If you're new to Supabase, [create a project](/dashboard).
    Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).

2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

3.  Under the Session pooler, click on the View parameters under the connect string. Note your Host (`$SUPABASE_HOST`).

![Finding Supabase host address](/docs/img/guides/resources/migrating-to-supabase/mysql/database-settings-host.png)



## Migrate the database

The fastest way to migrate your database is with the Supabase migration tool on
[Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb).

Alternatively, you can use [pgloader](https://github.com/dimitri/pgloader), a flexible and powerful data migration tool that supports a wide range of source database engines, including MySQL and MS SQL, and migrates the data to a Postgres database. For databases using the Postgres engine, we recommend using the [`pg_dump`](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

<Tabs scrollable size="small" type="underlined" defaultActiveId="colab" queryGroup="migrate-method">
  <TabPanel id="colab" label="Migrate using Colab">
    1.  Select the Database Engine from the Source database in the dropdown
    2.  Set the environment variables (`HOST`, `USER`, `SOURCE_DB`,`PASSWORD`, `SUPABASE_URL`, and `SUPABASE_PASSWORD`) in the Colab notebook.
    3.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Amazon_RDS_to_Supabase.ipynb) in order. The first sets engine and installs the necessary files.
    4.  Run the third step to start the migration. This will take a few minutes.
  </TabPanel>

  <TabPanel id="MySQL" label="Migrate from MySQL with pgloader">
    1.  Install pgloader.

    2.  Create a configuration file (e.g., config.load).

        For your destination, use your Supabase connection string with `Use connection pooling` enabled, and the mode set to `Session`. You can get the string from your [`Database Settings`](/dashboard/project/_/settings/general).

        ```sql
        load database
          from mysql://user:password@host/source_db
          into postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:5432/postgres
        alter schema 'public' owner to 'postgres';
        set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
        ```

    3.  Run the migration with pgloader

        ```bash
        pgloader config.load
        ```
  </TabPanel>
</Tabs>

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from Neon to Supabase

Migrate your existing Neon database to Supabase.

This guide demonstrates how to migrate your Neon database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.



## Retrieve your Neon database credentials \[#retrieve-credentials]

1.  Log in to your Neon Console [https://console.neon.tech/login](https://console.neon.tech/login).
2.  Select **Projects** on the left.
3.  Click on your project in the list.
4.  From your Project Dashboard find your **Connection string** and click **Copy snippet** to copy it to the clipboard (do not check "pooled connection").

Example:

```bash
postgresql://neondb_owner:xxxxxxxxxxxxxxx-random-word-yyyyyyyy.us-west-2.aws.neon.tech/neondb?sslmode=require
```



## Set your `OLD_DB_URL` environment variable

Set the **OLD\_DB\_URL** environment variable at the command line using your Neon database credentials from the clipboard.

Example:

```bash
export OLD_DB_URL="postgresql://neondb_owner:xxxxxxxxxxxxxxx-random-word-yyyyyyyy.us-west-2.aws.neon.tech/neondb?sslmode=require"
```



## Retrieve your Supabase connection string \[#retrieve-supabase-connection-string]

1.  If you're new to Supabase, [create a project](/dashboard).
    Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).

2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

3.  Under the Session pooler, click the **Copy** button to the right of your connection string to copy it to the clipboard.



## Set your `NEW_DB_URL` environment variable

Set the **NEW\_DB\_URL** environment variable at the command line using your Supabase connection string. You will need to replace `[YOUR-PASSWORD]` with your actual database password.

Example:

```bash
export NEW_DB_URL="postgresql://postgres.xxxxxxxxxxxxxxxxxxxx:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
```



## Migrate the database

You will need the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full [Postgres installation](https://www.postgresql.org/download).

1.  Export your database to a file in console

    Use `pg_dump` with your Postgres credentials to export your database to a file (e.g., `dump.sql`).

```bash
pg_dump "$OLD_DB_URL" \
  --clean \
  --if-exists \
  --quote-all-identifiers \
  --no-owner \
  --no-privileges \
  > dump.sql
```

2.  Import the database to your Supabase project

    Use `psql` to import the Postgres database file to your Supabase project.

    ```bash
    psql -d "$NEW_DB_URL" -f dump.sql
    ```

Additional options

*   To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
*   To exclude a schema: `--exclude-schema=PATTERN`.
*   To only migrate a single table: `--table=PATTERN`.
*   To exclude a table: `--exclude-table=PATTERN`.

Run `pg_dump --help` for a full list of options.

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from Postgres to Supabase

Migrate your existing Postgres database to Supabase.

This is a guide for migrating your Postgres database to [Supabase](https://supabase.com).
Supabase is a robust and open-source platform. Supabase provides all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, real-time subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security, and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate your Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.

This guide provides three methods for migrating your Postgres database to Supabase:

1.  **Google Colab** - Guided notebook with copy-paste workflow
2.  **Manual Dump/Restore** - CLI approach, works for all versions
3.  **Logical Replication** - Minimal downtime, requires Postgres 10+



## Connection modes

Supabase provides the following connection modes:

*   Direct connection
*   Supavisor session mode
*   Supavisor transaction mode

Use Supavisor session mode for the database migration tasks (pg\_dump/restore and logical replication).



## Method 1: Google Colab (easiest)

Supabase provides a Google Colab migration notebook for a guided migration experience:
[Supabase Migration Colab Notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb)

This is ideal if you prefer a step-by-step, copy-paste workflow with minimal setup.



## Method 2: Manual dump/restore

This method works for all Postgres versions using CLI tools.


### Prerequisites


#### Source Postgres requirements

*   Connection string with rights to run `pg_dump`
*   No special settings required for dump/restore
*   Network access from migration VM


#### Migration environment

*   Cloud VM running Ubuntu in the same region as source or target database
*   Postgres client tools matching your source database version
*   tmux for session persistence
*   Sufficient disk space (usually ~50% of source database size is enough, but varies case by case)


### Pre-Migration checklist

```sql
-- Check database size
select pg_size_pretty(pg_database_size(current_database())) as size;

-- Check Postgres version
select version();

-- List installed extensions
select * from pg_extension order by extname;

-- Check active connections
select count(*) from pg_stat_activity;
```


#### Check available extensions in Supabase

```sql
-- Connect to your Supabase database and check available extensions
SELECT name, comment FROM pg_available_extensions ORDER BY name;

-- Compare with source database extensions
SELECT extname FROM pg_extension ORDER BY extname;

-- Install needed extensions
CREATE EXTENSION IF NOT EXISTS extension_name;
```


### Step 1: Set up migration VM

<Admonition type="tip">
  For optimal performance, run the migration from a cloud VM, not your local machine. The VM should be in the same region as either your source or target database to optimize network performance. See the Resource Requirements table in Step 2 for VM sizing recommendations.
</Admonition>


#### Set up Ubuntu VM

```bash

# Install Postgres client and tools
sudo apt update
sudo apt install software-properties-common
sudo sh -c 'echo "deb http://apt.Postgres.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.Postgres.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install Postgres-client-17 tmux htop iotop moreutils


# Start or attach to tmux session
tmux a -t migration || tmux new -s migration
```


### Step 2: Prepare Supabase project

1.  Create a Supabase project at [supabase.com/dashboard](/dashboard)
2.  Note your database password
3.  Install required extensions via SQL or Dashboard
4.  Get your connection string:
    *   Go to **Project → Settings → Database → Connection Pooling**
    *   Select **Session pooler** (port 5432) and copy the connection string
    *   Connection format: `Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres`

**Important Notes**:

*   **Users/roles are not migrated** - You'll need to recreate roles and privileges after import ([Supabase Roles Guide](/blog/postgres-roles-and-privileges))
*   **Row Level Security (RLS) status on tables is not migrated** - You'll need to enable RLS for tables after migration.

**Resource Requirements**:

| Database Size | Recommended Compute | Recommended VM            | Action Required                                 |
| ------------- | ------------------- | ------------------------- | ----------------------------------------------- |
| \< 10 GB      | Default             | 2 vCPUs, 4 GB RAM         | None                                            |
| 10-100 GB     | Default-Small       | 4 vCPUs, 8 GB RAM         | Consider compute upgrade                        |
| 100-500 GB    | Large compute       | 8 vCPUs, 16 GB RAM, NVMe  | Upgrade compute before restore                  |
| 500 GB - 1 TB | XL compute          | 16 vCPUs, 32 GB RAM, NVMe | Upgrade compute before restore                  |
| > 1 TB        | Custom              | Custom                    | [Contact support](/dashboard/support/new) first |

Also, you can temporarily increase compute size and/or disk IOPS and throughput via Settings → Compute and Disk if you want faster database restore (you can use larger -j for pg\_restore if you do so).


### Step 3: Create database dump


#### Set source database to read only mode for production migration

If doing a maintenance window migration, prevent data changes:

```sql
-- Connect to source database and run:
ALTER DATABASE your_database_name SET default_transaction_read_only = true;
```

For testing without a maintenance window, skip this step but use lower -j values.


#### Dump the database

```bash

# Determine number of parallel jobs based on:

# - Source database CPU cores (don't saturate production)

# - VM CPU cores

# - For testing without maintenance window: use lower values to be gentle

# - For production with maintenance window: can use higher values

DUMP_JOBS=4  # Adjust based on your setup


# Check available cores on VM
nproc


# Create dump with progress logging
pg_dump \
  --host=<source_host> \
  --port=<source_port> \
  --username=<source_username> \
  --dbname=<source_database> \
  --jobs=$DUMP_JOBS \
  --format=directory \
  --no-owner \
  --no-privileges \
  --no-subscriptions \
  --verbose \
  --file=./db_dump 2>&1 | ts | tee -a dump.log
```

**Notes about dump flags**:

*   `--no-owner --no-privileges`: Applied at dump time to prevent Supabase user management conflicts. While these could be used in pg\_restore instead, applying them during dump keeps the dump file cleaner and more portable.
*   `--no-subscriptions`: Logical replication subscriptions won't work in the target
*   The dump captures all data and schema but excludes ownership/privileges that would conflict with Supabase's managed environment
*   To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
*   To exclude a schema: `--exclude-schema=PATTERN`.
*   To only migrate a single table: `--table=PATTERN`.
*   To exclude a table: `--exclude-table=PATTERN`.

Run `pg_dump --help` for a full list of options.


#### Recommended parallelization (-j values)

| Database Size | Testing (no maintenance window) | Production (with maintenance window) | Limiting Factor |
| ------------- | ------------------------------- | ------------------------------------ | --------------- |
| \< 10 GB      | 2                               | 4                                    | Source CPU      |
| 10-100 GB     | 2-4                             | 8                                    | Source CPU      |
| 100-500 GB    | 4                               | 16                                   | Disk IOPS       |
| 500 GB - 1 TB | 4-8                             | 16-32                                | Disk IOPS + CPU |

**Note**: For testing without a maintenance window, use lower -j values to avoid impacting production performance.


### Step 4: Restore to Supabase


#### Set connection and restore

```bash

---
**Navigation:** [← Previous](./08-hipaa-projects.md) | [Index](./index.md) | [Next →](./10-set-supabase-connection-session-pooler-on-port-543.md)
