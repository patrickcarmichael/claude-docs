**Navigation:** [← Previous](./09-set-up-sso-with-okta.md) | [Index](./index.md) | [Next →](./11-manage-point-in-time-recovery-usage.md)

# Set Supabase connection (Session Pooler on port 5432 or direct connection)
export SUPABASE_DB_URL="Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres"


# Determine restore parallelization based on your Supabase compute size:

# Free tier: 2 cores → use -j 2

# Small compute: 2 cores → use -j 2

# Medium compute: 4 cores → use -j 4

# Large compute: 8 cores → use -j 8

# XL compute: 16 cores → use -j 16

RESTORE_JOBS=8  # Adjust based on your Supabase compute size


# Restore the dump (parallel mode)

# Note: -j cannot be used with --single-transaction
pg_restore \
  --dbname="$SUPABASE_DB_URL" \
  --jobs=$RESTORE_JOBS \
  --format=directory \
  --no-owner \
  --no-privileges \
  --verbose \
  ./db_dump 2>&1 | ts | tee -a restore.log
```

If restore fails with extension errors, check that errors are only extension-related.


### Step 5: Post-Migration tasks


#### Update statistics (important)

```bash
psql "$SUPABASE_DB_URL" -c "VACUUM VERBOSE ANALYZE;"
```

<Admonition type="note">
  For Postgres 18+, pg\_dump includes statistics with `--with-statistics`, but you should still run VACUUM for optimal performance.
</Admonition>


#### Verify migration

```sql
-- Check row counts
select schemaname, tablename, n_live_tup
from pg_stat_user_tables
order by n_live_tup desc
limit 20;
-- Verify data with application-specific queries
```


#### Re-enable writes on source (if keeping it)

```sql
ALTER DATABASE your_database_name SET default_transaction_read_only = false;
```


### Migration time estimates

| Database Size | Dump Time | Restore Time | Total Time  |
| ------------- | --------- | ------------ | ----------- |
| 10 GB         | ~5 min   | ~10 min     | ~15 min    |
| 100 GB        | ~30 min  | ~45 min     | ~1.5 hours |
| 500 GB        | ~2 hours | ~3 hours    | ~5 hours   |
| 1 TB          | ~4 hours | ~6 hours    | ~10 hours  |

*Times vary based on hardware, network, and parallelization settings*


### Important notes

1.  **Region proximity matters**: VM should be in the same region as the source or target for best performance
2.  **Downgrade migrations**: While technically possible in some cases, highly not recommended
3.  **Testing without downtime**: Use lower `-j` values for pg\_dump to avoid impacting production
4.  **For pg\_restore**: Can use full parallelization regardless of production impact
5.  **Monitor resources**: Watch CPU, disk I/O with `htop`, `iotop`
6.  **Disk I/O**: Often the bottleneck before network bandwidth

***



## Method 3: Logical replication

This method allows migration with minimal downtime using Postgres's logical replication feature. Requires Postgres 10+ on both source and target.


### When to use logical replication

*   You need minimal downtime (minutes instead of hours)
*   Source database is Postgres 10 or higher
*   You can configure logical replication on the source
*   Database has high write activity that can't be paused for long


### Source Postgres prerequisites


#### Access & privileges

*   Connection string with rights to CREATE PUBLICATION and read tables
*   Superuser or replication privileges recommended


#### Required settings for logical replication

*   `wal_level = logical`
*   `max_wal_senders ≥ 1`
*   `max_replication_slots ≥ 1`
*   Sufficient `max_connections` (current + 1 for subscription)


#### Replica identity

Every table receiving UPDATE/DELETE must have a replica identity (typically a PRIMARY KEY). For tables without one:

```sql
ALTER TABLE schema.table_name REPLICA IDENTITY FULL;
```


#### Non-Replicated items

*   **DDL changes** (schema modifications)
*   **Sequences** (need manual sync)
*   **Large Objects (LOBs)** (use dump/restore or store in regular bytea columns)

Plan a schema freeze, sequence sync before cutover, and handle LOBs separately.


### Step 1: Configure source database

Edit Postgres configuration files:


#### Postgres.conf

```bash

# Set Supabase connection (Session Pooler on port 5432 or direct connection)
export SUPABASE_DB_URL="Postgres://postgres.[ref]:[password]@aws-0-[region].pooler.supabase.com:5432/postgres"


# Set WAL level to logical
wal_level = logical


# Ensure sufficient replication slots
max_replication_slots = 10


# Ensure sufficient WAL senders
max_wal_senders = 10


# Set appropriate max_connections (current connections + 1 for subscription)
max_connections = 200  # Adjust based on your needs


# Optional: Enable SSL for secure replication
ssl = on


# Allow connections from Supabase
listen_addresses = '*'  # Or specific IP addresses
```

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}


#### pg\_hba.conf

```bash

# Allow replication connections from Supabase

# Replace <supabase_ip_range> with actual Supabase IP range
host    replication     all     <supabase_ip_range>    md5
host    all            all     <supabase_ip_range>    md5


# With SSL:
hostssl replication     all     <supabase_ip_range>    md5
hostssl all            all     <supabase_ip_range>    md5
```

Restart Postgres:

```bash
sudo systemctl restart Postgres
sudo systemctl status Postgres
```


### Step 2: Verify configuration

```sql
-- Should return 'logical'
SHOW wal_level;

-- Check other parameters
SHOW max_replication_slots;
SHOW max_wal_senders;

-- Check current connections
SELECT count(*) FROM pg_stat_activity;
```


### Step 3: Check and set replica identity

```sql
-- Find tables without primary keys
SELECT n.nspname, c.relname
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
LEFT JOIN pg_constraint pk ON pk.conrelid = c.oid AND pk.contype = 'p'
WHERE c.relkind = 'r'
  AND pk.oid IS NULL
  AND n.nspname NOT IN ('pg_catalog','information_schema');

-- For tables without a primary key, set REPLICA IDENTITY FULL
ALTER TABLE my_schema.my_table REPLICA IDENTITY FULL;
```


### Step 4: Export and restore schema only

```bash

# Export schema from source
pg_dump \
  -h <source_host> \
  -U <source_user> \
  -p <source_port> \
  -d <source_database> \
  --schema-only \
  --no-privileges \
  --no-subscriptions \
  --format=directory \
  -f ./schema_dump


# Restore schema to Supabase (use Session Pooler)
pg_restore \
  --dbname="$SUPABASE_DB_URL" \
  --format=directory \
  --schema-only \
  --no-privileges \
  --single-transaction \
  --verbose \
  ./schema_dump
```


### Step 5: Create publication on source

```sql
-- Create publication for all tables
CREATE PUBLICATION supabase_migration FOR ALL TABLES;

-- Or for specific tables only (doesn't require superuser)
CREATE PUBLICATION supabase_migration FOR TABLE
  schema1.table1,
  schema1.table2,
  public.table3;

-- Verify publication was created
SELECT * FROM pg_publication;
```


### Step 6: Create subscription on Supabase

Connect to your Supabase database:

```sql
-- Create subscription with SSL (recommended)
CREATE SUBSCRIPTION supabase_subscription
CONNECTION 'host=<source_host> port=<source_port> user=<source_user> password=<source_password> dbname=<source_database> sslmode=require'
PUBLICATION supabase_migration;

-- Or without SSL (if source doesn't support it)
CREATE SUBSCRIPTION supabase_subscription
CONNECTION 'host=<source_host> port=<source_port> user=<source_user> password=<source_password> dbname=<source_database> sslmode=disable'
PUBLICATION supabase_migration;
```


### Step 7: Monitor replication status

```sql
-- On Supabase (subscriber) - check subscription status
select * from pg_subscription_rel;

-- srsubstate = 'r' means ready (synchronized)
-- srsubstate = 'i' means initializing
-- srsubstate = 'd' means data is being copied

-- Overall subscription status
select * from pg_stat_subscription;

-- On source database - check replication status
select * from pg_stat_replication;

-- Check replication lag
select
  slot_name,
  pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn)) as lag_size
from pg_replication_slots;
```

Wait until all tables show `srsubstate = 'r'` (ready) status.


### Step 8: Synchronize sequences

After initial data sync is complete, but BEFORE switching to Supabase:

```bash

# Set source to read-only
psql -h <source_host> -c "ALTER DATABASE <source_database> SET default_transaction_read_only = true;"


# Export sequences from source
pg_dump \
  -h <source_host> \
  -U <source_user> \
  -p <source_port> \
  -d <source_database> \
  --data-only \
  --table='*_seq' \
  --table='*_id_seq' > sequences.sql


# Import sequences to Supabase
psql "$SUPABASE_DB_URL" -f sequences.sql
```


### Step 9: Switch to Supabase

1.  Ensure replication lag is zero:

```sql
-- On Supabase
select * from pg_stat_subscription;
-- Check that latest_end_lsn is current
```

2.  Stop writes to the source database (if not already read-only)

3.  Drop subscription on Supabase:

```sql
DROP SUBSCRIPTION supabase_subscription;
```

4.  Update application connection strings to point to Supabase

5.  Verify application functionality


### Step 10: Cleanup

On source database (after successful migration):

```sql
-- Remove publication
DROP PUBLICATION supabase_migration;

-- Check and remove any remaining replication slots
SELECT * FROM pg_replication_slots;
DROP REPLICATION SLOT slot_name;  -- if any remain

-- The source database should remain read-only or be decommissioned
-- Do NOT re-enable writes to avoid a split-brain scenario!
```


### Troubleshooting logical replication

| Issue                                | Solution                                                            |
| ------------------------------------ | ------------------------------------------------------------------- |
| "could not connect to the publisher" | Check network connectivity, firewall rules, pg\_hba.conf            |
| "role does not exist"                | Ensure replication user exists on source with REPLICATION privilege |
| "publication does not exist"         | Verify publication name and that it was created successfully        |
| Replication lag growing              | Check network bandwidth, source database load, add more WAL senders |
| Tables stuck in `i` state            | Check for locks on source tables, verify table structure matches    |
| "out of replication slots"           | Increase max\_replication\_slots in Postgres.conf                   |


### Important limitations

*   **DDL changes**: Schema modifications are not replicated - freeze schema during migration
*   **Sequences**: Need manual synchronization before cutover
*   **Large Objects (LOBs)**: Not replicated - use dump/restore or store in regular bytea columns
*   **Custom types**: May need special handling
*   **Users and roles**: Must be recreated manually on Supabase

For detailed restrictions, see [Postgres Logical Replication Restrictions](https://www.Postgres.org/docs/current/logical-replication-restrictions.html)


### When to use which method

**Use Dump/Restore when:**

*   Downtime window is acceptable
*   Source is Postgres \< 10
*   Simpler process preferred
*   Cannot configure logical replication on the source

**Use Logical Replication when:**

*   Minimal downtime required
*   Postgres 10+ on both sides
*   Can modify source configuration
*   Have replication privileges



## Getting help

*   For databases > 150 GB: [Contact Supabase support](/dashboard/support/new) before starting
*   [Supabase Dashboard Support](/dashboard/support/new)
*   [Supabase Discord](https://discord.supabase.com)
*   [Postgres Roles and Privileges Guide](/blog/postgres-roles-and-privileges)
*   [Row Level Security Guide](/docs/guides/database/postgres/row-level-security)



# Migrate from Render to Supabase

Migrate your Render Postgres database to Supabase.

Render is a popular Web Hosting service in the online services category that also has a managed Postgres service. Render has a great developer experience, allowing users to deploy straight from GitHub or GitLab. This is the core of their product and they do it really well. However, when it comes to Postgres databases, it may not be the best option.

Supabase is one of the best free alternative to Render Postgres. Supabase provide all the backend features developers need to build a product: a Postgres database, authentication, instant APIs, edge functions, realtime subscriptions, and storage. Postgres is the core of Supabase—for example, you can use row-level security and there are more than 40 Postgres extensions available.

This guide demonstrates how to migrate from Render to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.



## Retrieve your Render database credentials \[#retrieve-render-credentials]

1.  Log in to your [Render account](https://render.com) and select the project you want to migrate.
2.  Click **Dashboard** in the menu and click in your **Postgres** database.
3.  Scroll down in the **Info** tab.
4.  Click on **PSQL Command** and edit it adding the content after `PSQL_COMMAND=`.

![Copying PSQL command from Render dashboard](/docs/img/guides/resources/migrating-to-supabase/render/render_dashboard.png)
Example:

```bash
%env PSQL_COMMAND=PGPASSWORD=RgaMDfTS_password_FTPa7 psql -h dpg-a_server_in.oregon-postgres.render.com -U my_db_pxl0_user my_db_pxl0
```



## Retrieve your Supabase connection string \[#retrieve-supabase-connection-string]

1.  If you're new to Supabase, [create a project](/dashboard).
    Make a note of your password, you will need this later. If you forget it, you can [reset it here](/dashboard/project/_/database/settings).

2.  On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true\&method=session)

3.  Under Session pooler, Copy the connection string and replace the password placeholder with your database password.

    <Admonition type="note">
      If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
    </Admonition>



## Migrate the database

The fastest way to migrate your database is with the Supabase migration tool on [Google Colab](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb). Alternatively, you can use the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools, which are included in a full Postgres installation.

<Tabs scrollable size="small" type="underlined" defaultActiveId="colab" queryGroup="migrate-method">
  <TabPanel id="colab" label="Migrate using Colab">
    1.  Set the environment variables (`PSQL_COMMAND`, `SUPABASE_HOST`, `SUPABASE_PASSWORD`) in the Colab notebook.
    2.  Run the first two steps in [the notebook](https://colab.research.google.com/github/mansueli/Supa-Migrate/blob/main/Migrate_Postgres_Supabase.ipynb) in order. The first sets the variables and the second installs PSQL and the migration script.
    3.  Run the third step to start the migration. This will take a few minutes.
  </TabPanel>

  <TabPanel id="cli" label="Migrate using CLI tools">
    1.  Export your Render database to a file in console

        Use `pg_dump` with your Render credentials to export your Render database to a file (e.g., `render_dump.sql`).

        ```bash
        pg_dump --clean --if-exists --quote-all-identifiers \
        -h $RENDER_HOST -U $RENDER_USER -d $RENDER_DATABASE \
        --no-owner --no-privileges > render_dump.sql
        ```

    2.  Import the database to your Supabase project

        Use `psql` to import the Render database file to your Supabase project.

        ```bash
        psql -d "$YOUR_CONNECTION_STRING" -f render_dump.sql
        ```

    Additional options

    *   To only migrate a single database schema, add the `--schema=PATTERN` parameter to your `pg_dump` command.
    *   To exclude a schema: `--exclude-schema=PATTERN`.
    *   To only migrate a single table: `--table=PATTERN`.
    *   To exclude a table: `--exclude-table=PATTERN`.

    Run `pg_dump --help` for a full list of options.
  </TabPanel>
</Tabs>

<Admonition type="caution">
  *   If you're planning to migrate a database larger than 6 GB, we recommend [upgrading to at least a Large compute add-on](/docs/guides/platform/compute-add-ons). This will ensure you have the necessary resources to handle the migration efficiently.

  *   We strongly advise you to pre-provision the disk space you will need for your migration. On paid projects, you can do this by navigating to the [Compute and Disk Settings](/dashboard/project/_/settings/compute-and-disk) page. For more information on disk scaling and disk limits, check out our [disk settings](/docs/guides/platform/compute-and-disk#disk) documentation.
</Admonition>



## Enterprise

[Contact us](https://forms.supabase.com/enterprise) if you need more help migrating your project.



# Migrate from Vercel Postgres to Supabase

Migrate your existing Vercel Postgres database to Supabase.

This guide demonstrates how to migrate your Vercel Postgres database to Supabase to get the most out of Postgres while gaining access to all the features you need to build a project.



## Retrieve your Vercel Postgres database credentials \[#retrieve-credentials]

1.  Log in to your Vercel Dashboard [https://vercel.com/login](https://vercel.com/login).
2.  Click on the **Storage** tab.
3.  Click on your Postgres Database.
4.  Under the **Quickstart** section, select **psql** then click **Show Secret** to reveal your database password.
5.  Copy the string after `psql ` to the clipboard.

Example:

```bash
psql "postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```

Copy this part to your clipboard:

```bash
"postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
```



## Set your `OLD_DB_URL` environment variable

Set the **OLD\_DB\_URL** environment variable at the command line using your Vercel Postgres Database credentials.

Example:

```bash
export OLD_DB_URL="postgres://default:xxxxxxxxxxxx@yy-yyyyy-yyyyyy-yyyyyyy.us-west-2.aws.neon.tech:5432/verceldb?sslmode=require"
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



# Enforce MFA on Organization



Supabase provides multi-factor authentication (MFA) enforcement on the organization level. With MFA enforcement, you can ensure that all organization members use MFA. Members cannot interact with your organization or your organization's projects without a valid MFA-backed session.

<Admonition type="note">
  MFA enforcement is only available on the [Pro, Team and Enterprise plans](/pricing).
</Admonition>



## Manage MFA enforcement

To enable MFA on an organization, visit the [security settings](/dashboard/org/_/security) page and toggle `Require MFA to access organization` on.

*   Only organization **owners** can modify this setting
*   The owner must have [MFA on their own account](/docs/guides/platform/multi-factor-authentication)
*   Supabase recommends creating two distinct MFA apps on your user account

<Admonition type="caution">
  When MFA enforcement is enabled, users without MFA will immediately lose access all resources in the organization. The users will still be members of the organization and will regain their original permissions once they enable MFA on their account.
</Admonition>



## Personal access tokens

Personal access tokens are not affected by MFA enforcement. Personal access tokens are designed for programmatic access and issuing of these require a valid Supabase session backed by MFA, if enabled on the account.



# Manage Advanced MFA Phone usage




## What you are charged for

You are charged for having the feature [Advanced Multi-Factor Authentication Phone](/docs/guides/auth/auth-mfa/phone) enabled for your project.

<Admonition type="note">
  Additional charges apply for each SMS or WhatsApp message sent, depending on your third-party messaging provider (such as Twilio or MessageBird).
</Admonition>



## How charges are calculated

MFA Phone is charged by the hour, meaning you are charged for the exact number of hours that the feature is enabled for a project. If the feature is enabled for part of an hour, you are still charged for the full hour.


### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you enable the MFA Phone feature for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window                                 | MFA Phone | Hours Billed | Description         |
| ------------------------------------------- | --------- | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | Disabled  | 0            |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | Disabled  | 0            |                     |
| January 10, 04:30 PM - January 10, 5:00 PM  | Enabled   | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Enabled   | 511          |                     |


### Usage on your invoice

Usage is shown as "Auth MFA Phone Hours" on your invoice.



## Pricing



## Pricing

<Price price="0.1027" /> per hour (<Price price="75" /> per month) for the first project. <Price price="0.0137" /> per
hour (<Price price="10" /> per month) for every additional project.

| Plan       | Project 1 per month  | Project 2 per month  | Project 3 per month  |
| ---------- | -------------------- | -------------------- | -------------------- |
| Pro        | <Price price="75" /> | <Price price="10" /> | <Price price="10" /> |
| Team       | <Price price="75" /> | <Price price="10" /> | <Price price="10" /> |
| Enterprise | Custom               | Custom               | Custom               |

For a detailed breakdown of how charges are calculated, refer to [Manage Advanced MFA Phone usage](/docs/guides/platform/manage-your-usage/advanced-mfa-phone).



## Billing examples


### One project

The project has MFA Phone activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                     |
| ----------------------------- | ----- | ------------------------- |
| Pro Plan                      | -     | <Price price="25" />      |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />      |
| MFA Phone Hours               | 744   | <Price price="75" />      |
| **Subtotal**                  |       | **<Price price="110" />** |
| Compute Credits               |       | -<Price price="10" />     |
| **Total**                     |       | **<Price price="100" />** |


### Multiple projects

All projects have MFA Phone activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                     |
| ----------------------------- | ----- | ------------------------- |
| Pro Plan                      | -     | <Price price="25" />      |
|                               |       |                           |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />      |
| MFA Phone Hours Project 1     | 744   | <Price price="75" />      |
|                               |       |                           |
| Compute Hours Micro Project 2 | 744   | <Price price="10" />      |
| MFA Phone Hours Project 2     | 744   | <Price price="10" />      |
|                               |       |                           |
| Compute Hours Micro Project 3 | 744   | <Price price="10" />      |
| MFA Phone Hours Project 3     | 744   | <Price price="10" />      |
|                               |       |                           |
| **Subtotal**                  |       | **<Price price="150" />** |
| Compute Credits               |       | -<Price price="10" />     |
| **Total**                     |       | **<Price price="140" />** |



# Manage Branching usage




## What you are charged for

Each [Preview branch](/docs/guides/deployment/branching) is a separate environment with all Supabase services (Database, Auth, Storage, etc.). You're charged for usage within that environment—such as [Compute](/docs/guides/platform/manage-your-usage/compute), [Disk Size](/docs/guides/platform/manage-your-usage/disk-size), [Egress](/docs/guides/platform/manage-your-usage/egress), and [Storage](/docs/guides/platform/manage-your-usage/storage-size)—just like the project you branched from.

Usage by Preview branches counts toward your subscription plan's quota.



## How charges are calculated

Refer to individual [usage items](/docs/guides/platform/manage-your-usage) for details on how charges are calculated. Branching charges are the sum of all these items.


### Usage on your invoice

Compute incurred by Preview branches is shown as "Branching Compute Hours" on your invoice. Other usage items are not shown separately for branches and are rolled up into the project.



## Pricing

There is no fixed fee for a Preview branch. You only pay for the usage it incurs. A branch running on the default Micro Compute size starts at <Price price="0.01344" /> per hour.



## Billing examples

The project has a Preview branch "XYZ", that runs for 30 hours, incurring Compute and Egress costs. Disk Size usage remains within the 8 GB included in the subscription plan, so no additional charges apply.

| Line Item                      | Costs                      |
| ------------------------------ | -------------------------- |
| Pro Plan                       | <Price price="25" />       |
|                                |                            |
| Compute Hours Small Project 1  | <Price price="15" />       |
| Egress Project 1               | <Price price="7" />        |
| Disk Size Project 1            | <Price price="3" />        |
|                                |                            |
| Compute Hours Micro Branch XYZ | <Price price="0.4" />      |
| Egress Branch XYZ              | <Price price="1" />        |
| Disk Size Branch XYZ           | <Price price="0" />        |
|                                |                            |
| **Subtotal**                   | **<Price price="51.4" />** |
| Compute Credits                | -<Price price="10" />      |
| **Total**                      | **<Price price="41.4" />** |



## View usage

You can view Branching usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Usage Summary section, you can see how many hours your Preview branches existed during the selected time period. Hover over "Branching Compute Hours" for a detailed breakdown.

<Image
  alt="Usage summary Branching Compute Hours"
  src={{
    light: '/docs/img/guides/platform/usage-summary-branch-hours--light.png',
    dark: '/docs/img/guides/platform/usage-summary-branch-hours--dark.png',
  }}
  zoomable
/>



## Optimize usage

*   Merge Preview branches as soon as they are ready
*   Delete Preview branches that are no longer in use
*   Check whether your [persistent branches](/docs/guides/deployment/branching#persistent-branches) need to be defined as persistent, or if they can be ephemeral instead. Persistent branches will remain active even after the underlying PR is closed.



## FAQ


### Do Compute Credits apply to Branching Compute?

No, Compute Credits do not apply to Branching Compute.



# Manage Compute usage




## What you are charged for

Each project on the Supabase platform includes a dedicated Postgres instance running on its own server. You are charged for the [Compute](/docs/guides/platform/compute-and-disk#compute) resources of that server, independent of your database usage.

Paused projects do not count towards Compute usage.



## How charges are calculated

Compute is charged by the hour, meaning you are charged for the exact number of hours that a project is running and, therefore, incurring Compute usage. If a project runs for part of an hour, you are still charged for the full hour.

<Admonition type="caution">
  Each project you launch increases your monthly Compute costs.
</Admonition>


### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you switch your project from the Micro Compute size to the Small Compute size. At the end of the billing cycle you are billed for 233 hours of Micro Compute size and 511 hours of Small Compute size.

| Time Window                                 | Compute Size | Hours Billed | Description         |
| ------------------------------------------- | ------------ | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | Micro        | 232          |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | Micro        | 1            | full hour is billed |
| January 10, 04:30 PM - January 10, 5:00 PM  | Small        | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Small        | 511          |                     |


### Usage on your invoice

Usage is shown as "Compute Hours" on your invoice.



## Compute Credits

Paid plans include <Price price="10" /> in Compute Credits, which cover one project running on the Micro/Nano Compute size or portions of other Compute sizes. Compute Credits are applied to your Compute costs and are provided to an organization each month. They reset monthly and do not accumulate.



## Pricing

| Compute Size | Hourly Price USD          | Monthly Price USD                                                                                        |
| ------------ | ------------------------- | -------------------------------------------------------------------------------------------------------- |
| Nano\[^1]     | <Price price="0" />       | <Price price="0" />                                                                                      |
| Micro        | <Price price="0.01344" /> | ~<Price price="10" />                                                                                   |
| Small        | <Price price="0.0206" />  | ~<Price price="15" />                                                                                   |
| Medium       | <Price price="0.0822" />  | ~<Price price="60" />                                                                                   |
| Large        | <Price price="0.1517" />  | ~<Price price="110" />                                                                                  |
| XL           | <Price price="0.2877" />  | ~<Price price="210" />                                                                                  |
| 2XL          | <Price price="0.562" />   | ~<Price price="410" />                                                                                  |
| 4XL          | <Price price="1.32" />    | ~<Price price="960" />                                                                                  |
| 8XL          | <Price price="2.562" />   | ~<Price price="1,870" />                                                                                |
| 12XL         | <Price price="3.836" />   | ~<Price price="2,800" />                                                                                |
| 16XL         | <Price price="5.12" />    | ~<Price price="3,730" />                                                                                |
| >16XL        | -                         | [Contact Us](/dashboard/support/new?category=sales\&subject=Enquiry%20about%20larger%20instance%20sizes) |

\[^1]: Compute resources on the Free Plan are subject to change.

<Admonition type="note" label="Nano Compute size in paid plan organizations">
  In paid organizations, Nano Compute are billed at the same price as Micro Compute. It is recommended to upgrade your Project from Nano Compute to Micro Compute when it's convenient for you. Compute sizes are not auto-upgraded because of the downtime incurred. See [Supabase Pricing](/pricing) for more information. You cannot launch Nano instances on paid plans, only Micro and above - but you might have Nano instances after upgrading from Free Plan.
</Admonition>



## Billing examples


### One project

The project runs on the same Compute size throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| **Subtotal**                  |       | **<Price price="35" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="25" />** |


### Multiple projects

All projects run on the same Compute size throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| Compute Hours Micro Project 2 | 744   | <Price price="10" />     |
| Compute Hours Micro Project 3 | 744   | <Price price="10" />     |
| **Subtotal**                  |       | **<Price price="55" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="45" />** |


### One project on different Compute sizes

The project's Compute size changes throughout the billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
| Compute Hours Micro Project 1 | 233   | <Price price="3" />      |
| Compute Hours Small Project 1 | 511   | <Price price="11" />     |
| **Subtotal**                  |       | **<Price price="39" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="29" />** |



## View usage

You can view Compute usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Compute Hours section, you can see how many hours of a specific Compute size your projects have used during the selected time period. Hover over a specific date for a daily breakdown.

<Image
  alt="Usage page Compute Hours section"
  src={{
    light: '/docs/img/guides/platform/usage-compute--light.png',
    dark: '/docs/img/guides/platform/usage-compute--dark.png',
  }}
  zoomable
/>



## Optimize usage

*   Start out on a smaller Compute size, [create a report](/dashboard/project/_/reports) on the Dashboard to monitor your CPU and memory utilization, and upgrade the Compute size as needed
*   Load test your application in staging to understand your Compute requirements
*   [Transfer projects](/docs/guides/platform/project-transfer) to a Free Plan organization to reduce Compute usage
*   Delete unused projects



## FAQ


### Do Compute Credits apply to line items other than Compute?

No, Compute Credits apply only to Compute and do not cover other line items, including Read Replica Compute and Branching Compute.



# Manage Custom Domain usage




## What you are charged for

You can configure a [custom domain](/docs/guides/platform/custom-domains) for a project by enabling the [Custom Domain add-on](/dashboard/project/_/settings/addons?panel=customDomain). You are charged for all custom domains configured across your projects.



## How charges are calculated

Custom domains are charged by the hour, meaning you are charged for the exact number of hours that a custom domain is active. If a custom domain is active for part of an hour, you are still charged for the full hour.


### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you activate a custom domain for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window                                 | Custom Domain Activated | Hours Billed | Description         |
| ------------------------------------------- | ----------------------- | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | No                      | 0            |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | No                      | 0            |                     |
| January 10, 04:30 PM - January 10, 5:00 PM  | Yes                     | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Yes                     | 511          |                     |


### Usage on your invoice

Usage is shown as "Custom Domain Hours" on your invoice.



## Pricing

<Price price="0.0137" /> per hour (<Price price="10" /> per month).



## Billing examples


### One project

The project has a custom domain activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| Custom Domain Hours           | 744   | <Price price="10" />     |
| **Subtotal**                  |       | **<Price price="45" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="35" />** |


### Multiple projects

All projects have a custom domain activated throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
|                               |       |                          |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| Custom Domain Hours Project 1 | 744   | <Price price="10" />     |
|                               |       |                          |
| Compute Hours Micro Project 2 | 744   | <Price price="10" />     |
| Custom Domain Hours Project 2 | 744   | <Price price="10" />     |
|                               |       |                          |
| **Subtotal**                  |       | **<Price price="65" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="55" />** |



## Optimize usage

*   Regularly check your projects and remove custom domains that are no longer needed
*   Use free [Vanity subdomains](/docs/guides/platform/custom-domains#vanity-subdomains) where applicable



# Manage Disk IOPS usage




## What you are charged for

Each database has a dedicated disk, and you are charged for its provisioned disk IOPS. However, unless you explicitly opt in for additional IOPS, no charges apply.

Refer to our [disk guide](/docs/guides/platform/compute-and-disk#disk) for details on how disk IOPS, disk throughput, disk size, disk type and compute size interact, along with their limitations and constraints.

<Admonition type="note">
  Launching a Read Replica creates an additional database with its own dedicated disk. Read Replicas inherit the primary database's disk IOPS settings. You are charged for the provisioned IOPS of the Read Replica. Refer to [Manage Read Replica usage](/docs/guides/platform/manage-your-usage/read-replicas) for details on billing.
</Admonition>



## How charges are calculated

Disk IOPS is charged by IOPS-Hrs. 1 IOPS-Hr represents 1 IOPS being provisioned for 1 hour. For example, having 10 IOPS provisioned for 5 hours results in 50 IOPS-Hrs (10 IOPS × 5 hours).


### Usage on your invoice

Usage is shown as "Disk IOPS-Hrs" on your invoice.



## Pricing

Pricing depends on the [disk type](/docs/guides/platform/compute-and-disk#disk-types), with type gp3 being the default.


### General purpose disks (gp3)

<Price price="0.00003288" /> per IOPS-Hr (<Price price="0.024" /> per IOPS per month). gp3 disks
come with a default IOPS of 3,000. You are only charged for provisioned IOPS exceeding these 3,000
IOPS.

| Plan       | Included Disk IOPS | Over-Usage per IOPS per month | Over-Usage per IOPS-Hr       |
| ---------- | ------------------ | ----------------------------- | ---------------------------- |
| Pro        | 3,000              | <Price price="0.024" />       | <Price price="0.00003288" /> |
| Team       | 3,000              | <Price price="0.024" />       | <Price price="0.00003288" /> |
| Enterprise | Custom             | Custom                        | Custom                       |


### High performance disks (io2)

<Price price="0.000163" /> per IOPS-Hr (<Price price="0.119" /> per IOPS per month). Unlike general
purpose disks, high performance disks are billed from the first provisioned IOPS.

| Plan       | Included Disk IOPS | Usage per IOPS per month | Usage per IOPS-Hr          |
| ---------- | ------------------ | ------------------------ | -------------------------- |
| Pro        | 0                  | <Price price="0.119" />  | <Price price="0.000163" /> |
| Team       | 0                  | <Price price="0.119" />  | <Price price="0.000163" /> |
| Enterprise | Custom             | Custom                   | Custom                     |



## Billing examples


### Gp3

Project 1 doesn't exceed the included IOPS, so no charges for IOPS apply. Project 2 exceeds the included IOPS by 600, incurring charges for this additional usage.

| Line Item                     | Units      | Costs                        |
| ----------------------------- | ---------- | ---------------------------- |
| Pro Plan                      | 1          | <Price price="25" />         |
|                               |            |                              |
| Compute Hours Micro Project 1 | 744 hours  | <Price price="10" />         |
| Disk IOPS Project 1           | 3,000 IOPS | <Price price="0" />          |
|                               |            |                              |
| Compute Hours Large Project 2 | 744 hours  | <Price price="110" />        |
| Disk IOPS Project 2           | 3,600 IOPS | <Price price="14.40" />      |
|                               |            |                              |
| **Subtotal**                  |            | **<Price price="159.40" />** |
| Compute Credits               |            | -<Price price="10" />        |
| **Total**                     |            | **<Price price="149.40" />** |


### Io2

This disk type is billed from the first IOPS provisioned, meaning for 8000 IOPS.

| Line Item                     | Units      | Costs                       |
| ----------------------------- | ---------- | --------------------------- |
| Pro Plan                      | 1          | <Price price="25" />        |
| Compute Hours Large Project 1 | 744 hours  | <Price price="110" />       |
| Disk IOPS Project 1           | 8,000 IOPS | <Price price="952" />       |
| **Subtotal**                  |            | **<Price price="1" />,087** |
| Compute Credits               |            | -<Price price="10" />       |
| **Total**                     |            | **<Price price="1" />,077** |



# Manage Disk size usage




## What you are charged for

Each database has a dedicated [disk](/docs/guides/platform/compute-and-disk#disk). You are charged for the provisioned disk size.

<Admonition type="note">
  Disk size is not relevant for the Free Plan. Instead Free Plan customers are limited by [Database size](/docs/guides/platform/database-size).
</Admonition>



## How charges are calculated

Disk size is charged by Gigabyte-Hours (GB-Hrs). 1 GB-Hr represents 1 GB being provisioned for 1 hour.
For example, having 10 GB provisioned for 5 hours results in 50 GB-Hrs (10 GB × 5 hours).


### Usage on your invoice

Usage is shown as "Disk Size GB-Hrs" on your invoice.



## Pricing

Pricing depends on the [disk type](/docs/guides/platform/compute-and-disk#disk-types), with gp3 being the default disk type.


### General purpose disks (gp3)

<Price price="0.000171" /> per GB-Hr (<Price price="0.125" /> per GB per month). The primary
database of your project gets provisioned with an 8 GB disk. You are only charged for provisioned
disk size exceeding these 8 GB.

| Plan       | Included Disk Size | Over-Usage per GB per month | Over-Usage per GB-Hr       |
| ---------- | ------------------ | --------------------------- | -------------------------- |
| Pro        | 8 GB               | <Price price="0.125" />     | <Price price="0.000171" /> |
| Team       | 8 GB               | <Price price="0.125" />     | <Price price="0.000171" /> |
| Enterprise | Custom             | Custom                      | Custom                     |

<Admonition type="note">
  Launching a Read Replica creates an additional database with its own dedicated disk. You are charged from the first byte of provisioned disk for the Read Replica. Refer to [Manage Read Replica usage](/docs/guides/platform/manage-your-usage/read-replicas) for details on billing.
</Admonition>


### High performance disks (io2)

<Price price="0.000267" /> per GB-Hr (<Price price="0.195" /> per GB per month). Unlike general
purpose disks, high performance disks are billed from the first byte of provisioned disk.

| Plan       | Included Disk size | Usage per GB per month  | Usage per GB-Hr            |
| ---------- | ------------------ | ----------------------- | -------------------------- |
| Pro        | 0 GB               | <Price price="0.195" /> | <Price price="0.000267" /> |
| Team       | 0 GB               | <Price price="0.195" /> | <Price price="0.000267" /> |
| Enterprise | Custom             | Custom                  | Custom                     |



## Billing examples


### Gp3

Project 1 and 2 don't exceed the included disk size, so no charges for Disk size apply. Project 3 exceeds the included disk size by 42 GB, incurring charges for this additional usage.

| Line Item                     | Units     | Costs                       |
| ----------------------------- | --------- | --------------------------- |
| Pro Plan                      | 1         | <Price price="25" />        |
|                               |           |                             |
| Compute Hours Micro Project 1 | 744 hours | <Price price="10" />        |
| Disk Size Project 1           | 8 GB      | <Price price="0" />         |
|                               |           |                             |
| Compute Hours Micro Project 2 | 744 hours | <Price price="10" />        |
| Disk Size Project 2           | 8 GB      | <Price price="0" />         |
|                               |           |                             |
| Compute Hours Micro Project 3 | 744 hours | <Price price="10" />        |
| Disk Size Project 3           | 50 GB     | <Price price="5.25" />      |
|                               |           |                             |
| **Subtotal**                  |           | **<Price price="50.25" />** |
| Compute Credits               |           | -<Price price="10" />       |
| **Total**                     |           | **<Price price="40.25" />** |


### Io2

This disk type is billed from the first byte of provisioned disk, meaning for 66 GB across all projects.

| Line Item                     | Units     | Costs                       |
| ----------------------------- | --------- | --------------------------- |
| Pro Plan                      | 1         | <Price price="25" />        |
|                               |           |                             |
| Compute Hours Micro Project 1 | 744 hours | <Price price="10" />        |
| Disk Size Project 1           | 8 GB      | <Price price="1.56" />      |
|                               |           |                             |
| Compute Hours Micro Project 2 | 744 hours | <Price price="10" />        |
| Disk Size Project 2           | 8 GB      | <Price price="1.56" />      |
|                               |           |                             |
| Compute Hours Micro Project 3 | 744 hours | <Price price="10" />        |
| Disk Size Project 3           | 50 GB     | <Price price="9.75" />      |
|                               |           |                             |
| **Subtotal**                  |           | **<Price price="67.87" />** |
| Compute Credits               |           | -<Price price="10" />       |
| **Total**                     |           | **<Price price="57.87" />** |



## View usage

You can view Disk size usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Disk size section, you can see how much disk size your projects have provisioned.

<Image
  alt="Usage page Disk Size section"
  src={{
    light: '/docs/img/guides/platform/usage-disk-size--light.png',
    dark: '/docs/img/guides/platform/usage-disk-size--dark.png',
  }}
  zoomable
/>


### Disk size distribution

To see how your disk usage is distributed across Database, WAL, and System categories, refer to [Disk size distribution](/docs/guides/platform/database-size#disk-size-distribution).



## Reduce Disk size

To see how you can downsize your disk, refer to [Reducing disk size](/docs/guides/platform/database-size#reducing-disk-size)



# Manage Disk Throughput usage




## What you are charged for

Each database has a dedicated disk, and you are charged for its provisioned disk throughput. However, unless you explicitly opt in for additional throughput, no charges apply.

Refer to our [disk guide](/docs/guides/platform/compute-and-disk#disk) for details on how disk throughput, disk IOPS, disk size, disk type and compute size interact, along with their limitations and constraints.

<Admonition type="note">
  Launching a Read Replica creates an additional database with its own dedicated disk. Read Replicas inherit the primary database's disk throughput settings. You are charged for the provisioned throughput of the Read Replica.
</Admonition>



## How charges are calculated

Disk throughput is charged by MB/s-Hrs (MB/s stands for megabytes per second). 1 MB/s-Hr represents disk throughput of 1 MB/s being provisioned for 1 hour. For example, having 10 MB/s provisioned for 5 hours results in 50 MB/s-Hrs (10 MB/s × 5 hours).


### Usage on your invoice

Usage is shown as "Disk Throughput MB/s-Hrs" on your invoice.



## Pricing

Pricing depends on the [disk type](/docs/guides/platform/compute-and-disk#disk-types), with type gp3 being the default.


### General purpose disks (gp3)

<Price price="0.00013" /> per MB/s-Hr (<Price price="0.095" /> per MB/s per month). gp3 disks come
with a baseline throughput of 125 MB/s. You are only charged for provisioned throughput exceeding
these 125 MB/s.

| Plan       | Included Disk Throughput | Over-Usage per MB/s per month | Over-Usage per MB/s-Hr    |
| ---------- | ------------------------ | ----------------------------- | ------------------------- |
| Pro        | 125 MB/s                 | <Price price="0.095" />       | <Price price="0.00013" /> |
| Team       | 125 MB/s                 | <Price price="0.095" />       | <Price price="0.00013" /> |
| Enterprise | Custom                   | Custom                        | Custom                    |


### High performance disks (io2)

There are no charges. Throughput scales with IOPS at no additional cost.



## Billing examples


### No additional throughput configured

| Line Item                     | Units     | Costs                    |
| ----------------------------- | --------- | ------------------------ |
| Pro Plan                      | 1         | <Price price="25" />     |
|                               |           |                          |
| Compute Hours Micro Project 1 | 744 hours | <Price price="10" />     |
| Disk Throughput Project 1     | 125 MB/s  | <Price price="0" />      |
|                               |           |                          |
| **Subtotal**                  |           | **<Price price="35" />** |
| Compute Credits               |           | -<Price price="10" />    |
| **Total**                     |           | **<Price price="25" />** |


### Additional throughput configured

| Line Item                     | Units     | Costs                        |
| ----------------------------- | --------- | ---------------------------- |
| Pro Plan                      | 1         | <Price price="25" />         |
|                               |           |                              |
| Compute Hours Large Project 1 | 744 hours | <Price price="110" />        |
| Disk Throughput Project 1     | 200 MB/s  | <Price price="7.13" />       |
|                               |           |                              |
| **Subtotal**                  |           | **<Price price="142.13" />** |
| Compute Credits               |           | -<Price price="10" />        |
| **Total**                     |           | **<Price price="132.13" />** |


### Additional throughput configured with Read Replica

| Line Item                     | Units     | Costs                        |
| ----------------------------- | --------- | ---------------------------- |
| Pro Plan                      | 1         | <Price price="25" />         |
|                               |           |                              |
| Compute Hours Large Project 1 | 744 hours | <Price price="110" />        |
| Disk Throughput Project 1     | 200 MB/s  | <Price price="7.13" />       |
|                               |           |                              |
| Compute Hours Large Replica   | 744 hours | <Price price="110" />        |
| Disk Throughput Replica       | 200 MB/s  | <Price price="7.13" />       |
|                               |           |                              |
| **Subtotal**                  |           | **<Price price="259.26" />** |
| Compute Credits               |           | -<Price price="10" />        |
| **Total**                     |           | **<Price price="249.26" />** |



# Manage Edge Function Invocations usage




## What you are charged for

You are charged for the number of times your functions get invoked, regardless of the response status code. Preflight (OPTIONS) requests are not billed.



## How charges are calculated

Edge Function Invocations are billed using Package pricing, with each package representing 1 million invocations. If your usage falls between two packages, you are billed for the next whole package.


### Example

For simplicity, let's assume a package size of 1 million and a charge of <Price price="2" /> per package without a free quota.

| Invocations | Packages Billed | Costs               |
| ----------- | --------------- | ------------------- |
| 999,999     | 1               | <Price price="2" /> |
| 1,000,000   | 1               | <Price price="2" /> |
| 1,000,001   | 2               | <Price price="4" /> |
| 1,500,000   | 2               | <Price price="4" /> |


### Usage on your invoice

Usage is shown as "Function Invocations" on your invoice.



## Pricing

<Price price="2" /> per 1 million invocations. You are only charged for usage exceeding your subscription
plan's quota.

| Plan       | Quota     | Over-Usage                                    |
| ---------- | --------- | --------------------------------------------- |
| Free       | 500,000   | -                                             |
| Pro        | 2 million | <Price price="2" /> per 1 million invocations |
| Team       | 2 million | <Price price="2" /> per 1 million invocations |
| Enterprise | Custom    | Custom                                        |



## Billing examples


### Within quota

The organization's function invocations are within the quota, so no charges apply.

| Line Item            | Units                 | Costs                    |
| -------------------- | --------------------- | ------------------------ |
| Pro Plan             | 1                     | <Price price="25" />     |
| Compute Hours Micro  | 744 hours             | <Price price="10" />     |
| Function Invocations | 1,800,000 invocations | <Price price="0" />      |
| **Subtotal**         |                       | **<Price price="35" />** |
| Compute Credits      |                       | -<Price price="10" />    |
| **Total**            |                       | **<Price price="25" />** |


### Exceeding quota

The organization's function invocations exceed the quota by 1.4 million, incurring charges for this additional usage.

| Line Item            | Units                 | Costs                    |
| -------------------- | --------------------- | ------------------------ |
| Pro Plan             | 1                     | <Price price="25" />     |
| Compute Hours Micro  | 744 hours             | <Price price="10" />     |
| Function Invocations | 3,400,000 invocations | <Price price="4" />      |
| **Subtotal**         |                       | **<Price price="39" />** |
| Compute Credits      |                       | -<Price price="10" />    |
| **Total**            |                       | **<Price price="29" />** |



## View usage

You can view Edge Function Invocations usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Edge Function Invocations section, you can see how many invocations your projects have had during the selected time period.

<Image
  alt="Usage page Edge Function Invocations section"
  src={{
    light: '/docs/img/guides/platform/usage-function-invocations--light.png',
    dark: '/docs/img/guides/platform/usage-function-invocations--dark.png',
  }}
  zoomable
/>



# Manage Egress usage




## What you are charged for

You are charged for the network data transmitted out of the system to a connected client. Egress is incurred by all services - Database, Auth, Storage, Edge Functions, Realtime and Log Drains.


### Database Egress

Data sent to the client when retrieving data stored in your database.

**Example:** A user views their order history in an online shop. The client application requests the database to retrieve the user's past orders. The order data is sent back to the client, contributing to Database Egress.

<Admonition type="note">
  There are various ways to interact with your database, such as through the PostgREST API using one of the client SDKs or via the Supavisor connection pooler. On the Supabase Dashboard, Egress from the PostgREST API is labeled as **Database Egress**, while Egress through Supavisor is labeled as **Shared Pooler Egress**.
</Admonition>


### Auth Egress

Data sent from Supabase Auth to the client while managing your application's users. This includes actions like signing in, signing out, or creating new users, e.g. via the JavaScript Client SDK.

**Example:** A user signs in to an online shop. The client application requests the Supabase Auth service to authenticate and authorize the user. The session data, including authentication tokens and user profile details, is sent back to the client, contributing to Auth Egress.


### Storage Egress

Data sent from Supabase Storage to the client when retrieving assets. This includes actions like downloading files, images, or other stored content, e.g. via the JavaScript Client SDK.

**Example:** A user downloads an invoice from an online shop. The client application requests Supabase Storage to retrieve the PDF file from the storage bucket. The file is sent back to the client, contributing to Storage Egress.


### Edge Functions Egress

Data sent to the client when executing Edge Functions.

**Example:** A user completes a checkout process in an online shop. The client application triggers an Edge Function to process the payment and confirm the order. The confirmation response, along with any necessary details, is sent back to the client, contributing to Edge Functions Egress.


### Realtime Egress

Data pushed to clients via Supabase Realtime for subscribed events.

**Example:** When a user views a product page in an online shop, their client subscribes to real-time inventory updates. As stock levels change, Supabase Realtime pushes updates to all subscribed clients, contributing to Realtime Egress.


### Shared pooler Egress

Data sent to the client when using the shared connection pooler (Supavisor) to access your database. When using the shared connection pooler, we do not count database egress, as this would otherwise count double (Database -> Shared Pooler + Shared Pooler -> Client).

**Example:** You are using our [shared connection pooler](/docs/guides/database/connecting-to-postgres#shared-pooler) and you query a list of invoices in your backend. The data returned from that query is contributing to Shared Pooler Egress.


### Log Drain Egress

Data pushed to the connected log drain.

**Example:** You set up a log drain, each log sent to the log drain is considered egress. You can toggle the GZIP option to reduce egress, in case your provider supports it.


### Cached Egress

Cached and uncached egress have independent quotas and independent pricing. Cached egress is egress that is served from our CDN via cache hits. Cached egress is typically incurred for storage through our [Smart CDN](/docs/guides/storage/cdn/smart-cdn).



## How charges are calculated

Egress is charged by gigabyte. Charges apply only for usage exceeding your subscription plan's quota. This quota is called the Unified Egress Quota because it can be used across all services (Database, Auth, Storage etc.).


### Usage on your invoice

Usage is shown as "Egress GB" and "Cached Egress GB" on your invoice.



## Pricing

<Price price="0.09" /> per GB per month for uncached egress, <Price price="0.03" /> per GB per month
for cached egress. You are only charged for usage exceeding your subscription plan's quota.

| Plan       | Egress Quota (Uncached / Cached) | Over-Usage per month (Uncached / Cached)                      |
| ---------- | -------------------------------- | ------------------------------------------------------------- |
| Free       | 5 GB / 5 GB                      | -                                                             |
| Pro        | 250 GB / 250 GB                  | <Price price="0.09" /> per GB / <Price price="0.03" /> per GB |
| Team       | 250 GB / 250 GB                  | <Price price="0.09" /> per GB / <Price price="0.03" /> per GB |
| Enterprise | Custom                           | Custom                                                        |



## Billing examples


### Within quota

The organization's Egress usage is within the quota, so no charges for Egress apply.

| Line Item           | Units     | Costs                    |
| ------------------- | --------- | ------------------------ |
| Pro Plan            | 1         | <Price price="25" />     |
| Compute Hours Micro | 744 hours | <Price price="10" />     |
| Egress              | 200 GB    | <Price price="0" />      |
| Cached Egress       | 230 GB    | <Price price="0" />      |
| **Subtotal**        |           | **<Price price="35" />** |
| Compute Credits     |           | -<Price price="10" />    |
| **Total**           |           | **<Price price="25" />** |


### Exceeding quota

The organization's Egress usage exceeds the uncached egress quota by 50 GB and the cached egress quota by 550 GB, incurring charges for this additional usage.

| Line Item           | Units     | Costs                      |
| ------------------- | --------- | -------------------------- |
| Pro Plan            | 1         | <Price price="25" />       |
| Compute Hours Micro | 744 hours | <Price price="10" />       |
| Egress              | 300 GB    | <Price price="4.5" />      |
| Cached Egress       | 800 GB    | <Price price="16.5" />     |
| **Subtotal**        |           | **<Price price="47.5" />** |
| Compute Credits     |           | -<Price price="10" />      |
| **Total**           |           | **<Price price="37.5" />** |



## View usage


### Usage page

You can view Egress usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Total Egress section, you can see the usage for the selected time period. Hover over a specific date to view a breakdown by service. Note that this includes the cached egress.

<Image
  alt="Unified Egress"
  src={{
    light: '/docs/img/guides/platform/unified-egress--light.png',
    dark: '/docs/img/guides/platform/unified-egress.png',
  }}
/>

Separately, you can see the cached egress right below:

<Image
  alt="Unified Egress"
  src={{
    light: '/docs/img/guides/platform/cached-egress--light.png',
    dark: '/docs/img/guides/platform/cached-egress.png',
  }}
/>


### Custom report

1.  On the [reports page](/dashboard/project/_/reports), click **New custom report** in the left navigation menu
2.  After creating a new report, add charts for one or more Supabase services by clicking **Add block**

<Image
  alt="Egress report"
  src={{
    light: '/docs/img/guides/platform/egress-report--light.png',
    dark: '/docs/img/guides/platform/egress-report--dark.png',
  }}
  zoomable
/>



## Debug usage

To better understand your Egress usage, identify what’s driving the most traffic. Check the most frequent database queries, or analyze the most requested API paths to pinpoint high-egress endpoints.


### Frequent database queries

On the Advisors [Query performance view](/dashboard/project/_/database/query-performance?preset=most_frequent\&sort=calls\&order=desc) you can see the most frequent queries and the average number of rows returned.

<Image
  alt="Most frequent queries"
  src={{
    light: '/docs/img/guides/platform/advisor-most-frequent-queries--light.png',
    dark: '/docs/img/guides/platform/advisor-most-frequent-queries--dark.png',
  }}
  zoomable
/>


### Most requested API endpoints

In the [Logs Explorer](/dashboard/project/_/logs/explorer) you can access Edge Logs, and review the top paths to identify heavily queried endpoints. These logs currently do not include response byte data. That data will be available in the future too.

<Image
  alt="Top paths"
  src={{
    light: '/docs/img/guides/platform/logs-top-paths--light.png',
    dark: '/docs/img/guides/platform/logs-top-paths--dark.png',
  }}
  zoomable
/>



## Optimize usage

*   Reduce the number of fields or entries selected when querying your database
*   Reduce the number of queries or calls by optimizing client code or using caches
*   For update or insert queries, configure your ORM or queries to not return the entire row if not needed
*   When running manual backups through Supavisor, remove unneeded tables and/or reduce the frequency
*   Refer to the [Storage Optimizations guide](/docs/guides/storage/production/scaling#egress) for tips on reducing Storage Egress



# Manage IPv4 usage




## What you are charged for

You can assign a dedicated [IPv4 address](/docs/guides/platform/ipv4-address) to a database by enabling the [IPv4 add-on](/dashboard/project/_/settings/addons?panel=ipv4). You are charged for all IPv4 addresses configured across your databases.

<Admonition type="note">
  If the primary database has a dedicated IPv4 address configured, its Read Replicas are also assigned one, with charges for each.
</Admonition>



## How charges are calculated

IPv4 addresses are charged by the hour, meaning you are charged for the exact number of hours that an IPv4 address is assigned to a database. If an address is assigned for part of an hour, you are still charged for the full hour.


### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you enable the IPv4 add-on for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window                                 | IPv4 add-on | Hours Billed | Description         |
| ------------------------------------------- | ----------- | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | Disabled    | 0            |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | Disabled    | 0            |                     |
| January 10, 04:30 PM - January 10, 5:00 PM  | Enabled     | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Enabled     | 511          |                     |


### Usage on your invoice

Usage is shown as "IPv4 Hours" on your invoice.



## Pricing

<Price price="0.0055" /> per hour (<Price price="4" /> per month).



## Billing examples


### One project

The project has the IPv4 add-on enabled throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| IPv4 Hours                    | 744   | <Price price="4" />      |
| **Subtotal**                  |       | **<Price price="39" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="29" />** |


### Multiple projects

All projects have the IPv4 add-on enabled throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
|                               |       |                          |
| Compute Hours Micro Project 1 | 744   | <Price price="10" />     |
| IPv4 Hours Project 1          | 744   | <Price price="4" />      |
|                               |       |                          |
| Compute Hours Micro Project 2 | 744   | <Price price="10" />     |
| IPv4 Hours Project 2          | 744   | <Price price="4" />      |
|                               |       |                          |
| Compute Hours Micro Project 3 | 744   | <Price price="10" />     |
| IPv4 Hours Project 3          | 744   | <Price price="4" />      |
|                               |       |                          |
| **Subtotal**                  |       | **<Price price="67" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="57" />** |


### One project with Read Replicas

The project has two Read Replicas and the IPv4 add-on enabled throughout the entire billing cycle.

| Line Item                     | Hours | Costs                    |
| ----------------------------- | ----- | ------------------------ |
| Pro Plan                      | -     | <Price price="25" />     |
|                               |       |                          |
| Compute Hours Small Project 1 | 744   | <Price price="15" />     |
| IPv4 Hours Project 1          | 744   | <Price price="4" />      |
|                               |       |                          |
| Compute Hours Small Replica 1 | 744   | <Price price="15" />     |
| IPv4 Hours Replica 1          | 744   | <Price price="4" />      |
|                               |       |                          |
| Compute Hours Small Replica 2 | 744   | <Price price="15" />     |
| IPv4 Hours Replica 2          | 744   | <Price price="4" />      |
|                               |       |                          |
| **Subtotal**                  |       | **<Price price="82" />** |
| Compute Credits               |       | -<Price price="10" />    |
| **Total**                     |       | **<Price price="72" />** |



## Optimize usage

To see whether your database actually needs a dedicated IPv4 address, refer to [When you need the IPv4 add-on](/docs/guides/platform/ipv4-address#when-you-need-the-ipv4-add-on).



# Manage Log Drain usage




## What you are charged for

You can configure log drains in the [project settings](/dashboard/project/_/settings/log-drains) to send logs to one or more destinations. You are charged for each log drain that is configured (referred to as [Log Drain Hours](/docs/guides/platform/manage-your-usage/log-drains#log-drain-hours)), the log events sent (referred to as [Log Drain Events](/docs/guides/platform/manage-your-usage/log-drains#log-drain-events)), and the [Egress](/docs/guides/platform/manage-your-usage/egress) incurred by the export—across all your projects.



## Log Drain Hours


### How charges are calculated

You are charged by the hour, meaning you are charged for the exact number of hours that a log drain is configured for a project. If a log drain is configured for part of an hour, you are still charged for the full hour.


#### Example

Your billing cycle runs from January 1 to January 31. On January 10 at 4:30 PM, you configure a log drain for your project. At the end of the billing cycle you are billed for 512 hours.

| Time Window                                 | Log Drain Configured | Hours Billed | Description         |
| ------------------------------------------- | -------------------- | ------------ | ------------------- |
| January 1, 00:00 AM - January 10, 4:00 PM   | No                   | 0            |                     |
| January 10, 04:00 PM - January 10, 4:30 PM  | No                   | 0            |                     |
| January 10, 04:30 PM - January 10, 5:00 PM  | Yes                  | 1            | full hour is billed |
| January 10, 05:00 PM - January 31, 23:59 PM | Yes                  | 511          |                     |


#### Usage on your invoice

Usage is shown as "Log Drain Hours" on your invoice.


### Pricing

Log Drains are available as a project Add-On for all Team and Enterprise users. Each Log Drain costs <Price price="0.0822" /> per hour (<Price price="60" /> per month).



## Log Drain Events


### How charges are calculated

Log Drain Events are billed using Package pricing, with each package representing 1 million events. If your usage falls between two packages, you are billed for the next whole package.


#### Example

| Events    | Packages Billed | Costs                 |
| --------- | --------------- | --------------------- |
| 999,999   | 1               | <Price price="0.2" /> |
| 1,000,000 | 1               | <Price price="0.2" /> |
| 1,000,001 | 2               | <Price price="0.4" /> |
| 1,500,000 | 2               | <Price price="0.4" /> |


#### Usage on your invoice

Usage is shown as "Log Drain Events" on your invoice.


### Pricing

<Price price="0.2" /> per 1 million events.



## Billing example

The project has two log drains configured throughout the entire billing cycle with 800,000 and 1.6 million events each. In this example we assume that the organization is exceeding its Unified Egress Quota, so charges for Egress apply.

| Line Item                     | Units              | Costs                        |
| ----------------------------- | ------------------ | ---------------------------- |
| Team Plan                     | 1                  | <Price price="599" />        |
|                               |                    |                              |
| Compute Hours Micro Project 1 | 744 hours          | <Price price="10" />         |
|                               |                    |                              |
| Log Drain Hours Drain 1       | 744 hours          | <Price price="60" />         |
| Log Drain Events Drain 1      | 800,000 events     | <Price price="0.2" />        |
| Egress Drain 1                | 2 GB               | <Price price="0.18" />       |
|                               |                    |                              |
| Log Drain Hours Drain 2       | 744 hours          | <Price price="60" />         |
| Log Drain Events Drain 2      | 1.6 million events | <Price price="0.4" />        |
| Egress Drain 2                | 4 GB               | <Price price="0.36" />       |
|                               |                    |                              |
| **Subtotal**                  |                    | **<Price price="730.14" />** |
| Compute Credits               |                    | -<Price price="10" />        |
| **Total**                     |                    | **<Price price="720.14" />** |



## View usage

You can view Log Drain Events usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page usage summary"
  src={{
    light: '/docs/img/guides/platform/usage-logdrain-events--light.png',
    dark: '/docs/img/guides/platform/usage-logdrain-events--dark.png',
  }}
/>



# Manage Monthly Active SSO Users usage




## What you are charged for

You are charged for the number of distinct users who log in or refresh their token during the billing cycle using a SAML 2.0 compatible identity provider (e.g. Google Workspace, Microsoft Active Directory). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "SSO MAUs".


### Example

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single SSO MAU for this billing cycle.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Sign User-1 in on January 3" fullWidth>
      The SSO MAU count increases from 0 to 1.

      ```javascript
      const { data, error } = await supabase.auth.signInWithSSO({
      domain: 'company.com'
      })

      if (data?.url) {
      // redirect User-1 to the identity provider's authentication flow
      window.location.href = data.url
      }
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  {' '}

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Sign User-1 out on January 4" fullWidth>
      ```javascript

      const { error } = await supabase.auth.signOut()

      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Sign User-1 in again on January 17" fullWidth>
      The SSO MAU count remains 1.

      ```javascript
      const { data, error } = await supabase.auth.signInWithSSO({
      domain: 'company.com'
      })

      if (data?.url) {
      // redirect User-1 to the identity provider's authentication flow
      window.location.href = data.url
      }
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## How charges are calculated

You are charged by SSO MAU.


### Usage on your invoice

Usage is shown as "Monthly Active SSO Users" on your invoice.



## Pricing



## Pricing

<Price price="0.015" /> per SSO MAU. You are only charged for usage exceeding your subscription plan's
quota.

For a detailed breakdown of how charges are calculated, refer to [Manage Monthly Active SSO Users usage](/docs/guides/platform/manage-your-usage/monthly-active-users-sso).

<Admonition type="note">
  The count resets at the start of each billing cycle.
</Admonition>

| Plan       | Quota  | Over-Usage                          |
| ---------- | ------ | ----------------------------------- |
| Pro        | 50     | <Price price="0.015" /> per SSO MAU |
| Team       | 50     | <Price price="0.015" /> per SSO MAU |
| Enterprise | Custom | Custom                              |



## Billing examples


### Within quota

The organization's SSO MAU usage for the billing cycle is within the quota, so no charges apply.

| Line Item                | Units      | Costs                    |
| ------------------------ | ---------- | ------------------------ |
| Pro Plan                 | 1          | <Price price="25" />     |
| Compute Hours Micro      | 744 hours  | <Price price="10" />     |
| Monthly Active SSO Users | 37 SSO MAU | <Price price="0" />      |
| **Subtotal**             |            | **<Price price="35" />** |
| Compute Credits          |            | -<Price price="10" />    |
| **Total**                |            | **<Price price="25" />** |


### Exceeding quota

The organization's SSO MAU usage for the billing cycle exceeds the quota by 10, incurring charges for this additional usage.

| Line Item                | Units      | Costs                       |
| ------------------------ | ---------- | --------------------------- |
| Pro Plan                 | 1          | <Price price="25" />        |
| Compute Hours Micro      | 744 hours  | <Price price="10" />        |
| Monthly Active SSO Users | 60 SSO MAU | <Price price="0.15" />      |
| **Subtotal**             |            | **<Price price="35.15" />** |
| Compute Credits          |            | -<Price price="10" />       |
| **Total**                |            | **<Price price="25.15" />** |



## View usage

You can view Monthly Active SSO Users usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Monthly Active SSO Users section, you can see the usage for the selected time period.

<Image
  alt="Usage page Monthly Active SSO Users section"
  src={{
    light: '/docs/img/guides/platform/usage-mau-sso--light.png',
    dark: '/docs/img/guides/platform/usage-mau-sso--dark.png',
  }}
/>



# Manage Monthly Active Third-Party Users usage




## What you are charged for

You are charged for the number of distinct users who log in or refresh their token during the billing cycle using a third-party authentication provider (Clerk, Firebase Auth, Auth0, AWS Cognito). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "Third-Party MAUs".


### Example

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single SSO MAU for this billing cycle.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="User-1 signs in via Auth0 on January 3">
      The Third-Party MAU count increases
      from 0 to 1.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Image
        alt="Third-Party MAU login screen"
        src={{
          light: '/docs/img/guides/platform/third-party-mau-auth0-login-screen.png',
          dark: '/docs/img/guides/platform/third-party-mau-auth0-login-screen.png',
        }}
        className="max-h-[190px]"
        zoomable
      />
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  {' '}

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="User-1 signs out on January 4." />
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="User-1 signs in via Auth0 again on January 17">
      The Third-Party MAU count remains 1.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Image
        alt="Third-Party MAU login screen"
        src={{
          light: '/docs/img/guides/platform/third-party-mau-auth0-login-screen.png',
          dark: '/docs/img/guides/platform/third-party-mau-auth0-login-screen.png',
        }}
        className="max-h-[190px]"
        zoomable
      />
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## How charges are calculated

You are charged by Third-Party MAU.


### Usage on your invoice

Usage is shown as "Monthly Active Third-Party Users" on your invoice.



## Pricing



## Pricing

<Price price="0.00325" /> per Third-Party MAU. You are only charged for usage exceeding your subscription
plan's quota.

For a detailed breakdown of how charges are calculated, refer to [Manage Monthly Active Third-Party Users usage](/docs/guides/platform/manage-your-usage/monthly-active-users-third-party).

<Admonition type="note">
  The count resets at the start of each billing cycle.
</Admonition>

| Plan       | Quota   | Over-Usage                                    |
| ---------- | ------- | --------------------------------------------- |
| Free       | 50,000  | -                                             |
| Pro        | 100,000 | <Price price="0.00325" /> per Third-Party MAU |
| Team       | 100,000 | <Price price="0.00325" /> per Third-Party MAU |
| Enterprise | Custom  | Custom                                        |



## Billing examples


### Within quota

The organization's Third-Party MAU usage for the billing cycle is within the quota, so no charges apply.

| Line Item                        | Units                  | Costs                    |
| -------------------------------- | ---------------------- | ------------------------ |
| Pro Plan                         | 1                      | <Price price="25" />     |
| Compute Hours Micro              | 744 hours              | <Price price="10" />     |
| Monthly Active Third-Party Users | 37,000 Third-Party MAU | <Price price="0" />      |
| **Subtotal**                     |                        | **<Price price="35" />** |
| Compute Credits                  |                        | -<Price price="10" />    |
| **Total**                        |                        | **<Price price="25" />** |


### Exceeding quota

The organization's Third-Party MAU usage for the billing cycle exceeds the quota by 4950, incurring charges for this additional usage.

| Line Item                        | Units                   | Costs                        |
| -------------------------------- | ----------------------- | ---------------------------- |
| Pro Plan                         | 1                       | <Price price="25" />         |
| Compute Hours Micro              | 744 hours               | <Price price="10" />         |
| Monthly Active Third-Party Users | 130,000 Third-Party MAU | <Price price="97.50" />      |
| **Subtotal**                     |                         | **<Price price="132.50" />** |
| Compute Credits                  |                         | -<Price price="10" />        |
| **Total**                        |                         | **<Price price="122.50" />** |



## View usage

You can view Monthly Active Third-Party Users usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page Monthly Active SSO Users section"
  src={{
    light: '/docs/img/guides/platform/usage-mau-third-party--light.png',
    dark: '/docs/img/guides/platform/usage-mau-third-party--dark.png',
  }}
/>



# Manage Monthly Active Users usage




## What you are charged for

You are charged for the number of distinct users who log in or refresh their token during the billing cycle (including Social Login with e.g. Google, Facebook, GitHub). Each unique user is counted only once per billing cycle, regardless of how many times they authenticate. These users are referred to as "MAUs".


### Example

Your billing cycle runs from January 1 to January 31. Although User-1 was signed in multiple times, they are counted as a single MAU for this billing cycle.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Sign User-1 in on January 3" fullWidth>
      The MAU count increases from 0 to 1.

      ```javascript
      const {data, error} = await supabase.auth.signInWithPassword({
      email: 'user-1@email.com',
      password: 'example-password-1',
      })
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  {' '}

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Sign User-1 out on January 4" fullWidth>
      `javascript const {error} = await supabase.auth.signOut() `
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Sign User-1 in again on January 17" fullWidth>
      The MAU count remains 1.

      ```javascript
      const {data, error} = await supabase.auth.signInWithPassword({
      email: 'user-1@email.com',
      password: 'example-password-1',
      })
      ```
    </StepHikeCompact.Details>
  </StepHikeCompact.Step>
</StepHikeCompact>



## How charges are calculated

You are charged by MAU.


### Usage on your invoice

Usage is shown as "Monthly Active Users" on your invoice.



## Pricing

<Price price="0.00325" /> per MAU. You are only charged for usage exceeding your subscription plan's
quota.

<Admonition type="note">
  The count resets at the start of each billing cycle.
</Admonition>

| Plan       | Quota   | Over-Usage                        |
| ---------- | ------- | --------------------------------- |
| Free       | 50,000  | -                                 |
| Pro        | 100,000 | <Price price="0.00325" /> per MAU |
| Team       | 100,000 | <Price price="0.00325" /> per MAU |
| Enterprise | Custom  | Custom                            |



## Billing examples


### Within quota

The organization's MAU usage for the billing cycle is within the quota, so no charges apply.

| Line Item            | Units      | Costs                    |
| -------------------- | ---------- | ------------------------ |
| Pro Plan             | 1          | <Price price="25" />     |
| Compute Hours Micro  | 744 hours  | <Price price="10" />     |
| Monthly Active Users | 23,000 MAU | <Price price="0" />      |
| **Subtotal**         |            | **<Price price="35" />** |
| Compute Credits      |            | -<Price price="10" />    |
| **Total**            |            | **<Price price="25" />** |


### Exceeding quota

The organization's MAU usage for the billing cycle exceeds the quota by 60,000, incurring charges for this additional usage.

| Line Item            | Units       | Costs                     |
| -------------------- | ----------- | ------------------------- |
| Pro Plan             | 1           | <Price price="25" />      |
| Compute Hours Micro  | 744 hours   | <Price price="10" />      |
| Monthly Active Users | 160,000 MAU | <Price price="195" />     |
| **Subtotal**         |             | **<Price price="230" />** |
| Compute Credits      |             | -<Price price="10" />     |
| **Total**            |             | **<Price price="220" />** |



## View usage

You can view Monthly Active Users usage on the [organization's usage page](/dashboard/org/_/usage). The page shows the usage of all projects by default. To view the usage for a specific project, select it from the dropdown. You can also select a different time period.

<Image
  alt="Usage page navigation bar"
  src={{
    light: '/docs/img/guides/platform/usage-navbar--light.png',
    dark: '/docs/img/guides/platform/usage-navbar--dark.png',
  }}
  zoomable
/>

In the Monthly Active Users section, you can see the usage for the selected time period.

<Image
  alt="Usage page Monthly Active Users section"
  src={{
    light: '/docs/img/guides/platform/usage-mau--light.png',
    dark: '/docs/img/guides/platform/usage-mau--dark.png',
  }}
/>



---
**Navigation:** [← Previous](./09-set-up-sso-with-okta.md) | [Index](./index.md) | [Next →](./11-manage-point-in-time-recovery-usage.md)
