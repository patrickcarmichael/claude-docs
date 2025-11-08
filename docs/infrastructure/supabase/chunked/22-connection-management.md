**Navigation:** [← Previous](./21-production-checklist.md) | [Index](./index.md) | [Next →](./23-debugging-and-monitoring.md)

# Connection management

Using your connections resourcefully


## Connections

Every [Compute Add-On](/docs/guides/platform/compute-add-ons) has a pre-configured direct connection count and Supavisor pool size. This guide discusses ways to observe and manage them resourcefully.


### Configuring Supavisor's pool size

You can change how many database connections Supavisor can manage by altering the pool size in the "Connection pooling configuration" section of the [Database Settings](/dashboard/project/_/database/settings):

![Connection Info and Certificate.](/docs/img/database/pool-size.png)

The general rule is that if you are heavily using the PostgREST database API, you should be conscientious about raising your pool size past 40%. Otherwise, you can commit 80% to the pool. This leaves adequate room for the Authentication server and other utilities.

These numbers are generalizations and depends on other Supabase products that you use and the extent of their usage. The actual values depend on your concurrent peak connection usage. For instance, if you were only using 80 connections in a week period and your database max connections is set to 500, then realistically you could allocate the difference of 420 (minus a reasonable buffer) to service more demand.



## Monitoring connections


### Capturing historical usage


#### Dashboard monitoring charts

<Image
  alt="Database client connections chart"
  zoomable
  src={{
    dark: '/docs/img/database/reports/db-connections-chart-dark.png',
    light: '/docs/img/database/reports/db-connections-chart-light.png',
  }}
/>

For Teams and Enterprise plans, Supabase provides Advanced Telemetry charts directly within the Dashboard. The `Database client connections` chart displays historical connection data broken down by connection type:

*   **Postgres**: Direct connections from your application
*   **PostgREST**: Connections from the PostgREST API layer
*   **Reserved**: Administrative connections for Supabase services
*   **Auth**: Connections from Supabase Auth service
*   **Storage**: Connections from Supabase Storage service
*   **Other roles**: Miscellaneous database connections

This chart helps you monitor connection pool usage, identify connection leaks, and plan capacity. It also shows a reference line for your compute size's maximum connection limit.

For more details on using these monitoring charts, see the [Reports guide](/docs/guides/telemetry/reports#advanced-telemetry).


#### Grafana Dashboard

Supabase offers a Grafana Dashboard that records and visualizes over 200 project metrics, including connections. For setup instructions, check the [metrics docs](/docs/guides/platform/metrics).

Its "Client Connections" graph displays connections for both Supavisor and Postgres
![client connection graph](/docs/img/database/grafana-connections.png)


### Observing live connections

`pg_stat_activity` is a special view that keeps track of processes being run by your database, including live connections. It's particularly useful for determining if idle clients are hogging connection slots.

Query to get all live connections:

```sql
SELECT
  pg_stat_activity.pid as connection_id,
  ssl,
  datname as database,
  usename as connected_role,
  application_name,
  client_addr as IP,
  query,
  query_start,
  state,
  backend_start
FROM pg_stat_ssl
JOIN pg_stat_activity
ON pg_stat_ssl.pid = pg_stat_activity.pid;
```

Interpreting the query:

| Column             | Description                                         |
| ------------------ | --------------------------------------------------- |
| `connection_id`    | connection id                                       |
| `ssl`              | Indicates if SSL is in use                          |
| `database`         | Name of the connected database (usually `postgres`) |
| `usename`          | Role of the connected user                          |
| `application_name` | Name of the connecting application                  |
| `client_addr`      | IP address of the connecting server                 |
| `query`            | Last query executed by the connection               |
| `query_start`      | Time when the last query was executed               |
| `state`            | Querying state: active or idle                      |
| `backend_start`    | Timestamp of the connection's establishment         |

The username can be used to identify the source:

| Role                         | API/Tool                                                                  |
| ---------------------------- | ------------------------------------------------------------------------- |
| `supabase_admin`             | Used by Supabase for monitoring and by Realtime                           |
| `authenticator`              | Data API (PostgREST)                                                      |
| `supabase_auth_admin`        | Auth                                                                      |
| `supabase_storage_admin`     | Storage                                                                   |
| `supabase_replication_admin` | Synchronizes Read Replicas                                                |
| `postgres`                   | Supabase Dashboard and External Tools (e.g., Prisma, SQLAlchemy, PSQL...) |
| Custom roles defined by user | External Tools (e.g., Prisma, SQLAlchemy, PSQL...)                        |



# Customizing Postgres configs



Each Supabase project is a pre-configured Postgres cluster. You can override some configuration settings to suit your needs. This is an advanced topic, and we don't recommend touching these settings unless it is necessary.

<Admonition type="note">
  Customizing Postgres configurations provides *advanced* control over your database, but inappropriate settings can lead to severe performance degradation or project instability.
</Admonition>


### Viewing settings

To list all Postgres settings and their descriptions, run:

```sql
select * from pg_settings;
```



## Configurable settings


### User-context settings

The [`pg_settings`](https://www.postgresql.org/docs/current/view-pg-settings.html) table's `context` column specifies the requirements for changing a setting. By default, those with a `user` context can be changed at the `role` or `database` level with [SQL](/dashboard/project/_/sql/).

To list all user-context settings, run:

```sql
select * from pg_settings where context = 'user';
```

As an example, the `statement_timeout` setting can be altered:

```sql
alter database "postgres" set "statement_timeout" TO '60s';
```

To verify the change, execute:

```sql
show "statement_timeout";
```


### Superuser settings

Some settings can only be modified by a superuser. Supabase pre-enables the [`supautils` extension](/blog/roles-postgres-hooks#setting-up-the-supautils-extension), which allows the `postgres` role to retain certain superuser privileges. It enables modification of the below reserved configurations at the `role` level:

| Setting                      | Description                                                                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auto_explain.*`             | Configures the [auto\_explain module](https://www.postgresql.org/docs/current/auto-explain.html). Can be configured to log execution plans for queries expected to exceed x seconds, including function queries. |
| `log_lock_waits`             | Controls whether a log message is produced when a session waits longer than [deadlock\_timeout](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-DEADLOCK-TIMEOUT) to acquire a lock.       |
| `log_min_duration_statement` | Causes the duration of each completed statement to be logged if the statement ran for at least the specified amount of time.                                                                                     |
| `log_min_messages`           | Minimum severity level of messages to log.                                                                                                                                                                       |
| `log_replication_commands`   | Logs all replication commands                                                                                                                                                                                    |
| `log_statement`              | Controls which SQL statements are logged. Valid values are `none` (off), `ddl`, `mod`, and `all` (all statements).                                                                                               |
| `log_temp_files`             | Controls logging of temporary file names and sizes.                                                                                                                                                              |
| `pg_net.ttl`                 | Sets how long the [pg\_net extension](/docs/guides/database/extensions/pg_net) saves responses                                                                                                                   |
| `pg_net.batch_size`          | Sets how many requests the [pg\_net extension](/docs/guides/database/extensions/pg_net) can make per second                                                                                                      |
| `pg_stat_statements.*`       | Configures the [pg\_stat\_statements extension](https://www.postgresql.org/docs/current/pgstatstatements.html).                                                                                                  |
| `pgaudit.*`                  | Configures the [PGAudit extension](/docs/guides/database/extensions/pgaudit). The `log_parameter` is still restricted to protect secrets                                                                         |
| `pgrst.*`                    | [`PostgREST` settings](https://docs.postgrest.org/en/stable/references/configuration.html#db-aggregates-enabled)                                                                                                 |
| `plan_filter.*`              | Configures the [pg\_plan\_filter extension](/docs/guides/database/extensions/pg_plan_filter)                                                                                                                     |
| `session_replication_role`   | Sets the session's behavior for triggers and rewrite rules.                                                                                                                                                      |
| `track_io_timing`            | Collects timing statistics for database I/O activity.                                                                                                                                                            |
| `wal_compression`            | This parameter enables compression of WAL using the specified compression method.                                                                                                                                |

For example, to enable `log_nested_statements` for the `postgres` role, execute:

```sql
alter role "postgres" set "auto_explain.log_nested_statements" to 'on';
```

To view the change:

```sql
select
  rolname,
  rolconfig
from pg_roles
where rolname = 'postgres';
```


### CLI configurable settings

While many Postgres parameters are configurable directly, some configurations can be changed with the Supabase CLI at the [`system`](https://www.postgresql.org/docs/current/config-setting.html#CONFIG-SETTING-SQL) level.

<Admonition type="caution">
  CLI changes permanently overwrite default settings, so `reset all` and `set to default` commands won't revert to the original values.
</Admonition>

<Admonition type="danger">
  In order to overwrite the default settings, you must have `Owner` or `Administrator` privileges within your organizations.
</Admonition>


#### CLI supported parameters

<Admonition type="tip">
  If a setting you need is not yet configurable, [share your use case with us](/dashboard/support/new)! Let us know what setting you'd like to control, and we'll consider adding support in future updates.
</Admonition>

The following parameters are available for overrides:

1.  [checkpoint\_timeout](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-CHECKPOINT-TIMEOUT)
2.  [effective\_cache\_size](https://www.postgresql.org/docs/current/runtime-config-query.html#GUC-EFFECTIVE-CACHE-SIZE)
3.  [hot\_standby\_feedback](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-HOT-STANDBY-FEEDBACK)
4.  [logical\_decoding\_work\_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM) (CLI only)
5.  [maintenance\_work\_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAINTENANCE-WORK-MEM)
6.  [max\_connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-MAX-CONNECTIONS) (CLI only)
7.  [max\_locks\_per\_transaction](https://www.postgresql.org/docs/current/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION) (CLI only)
8.  [max\_parallel\_maintenance\_workers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-MAINTENANCE-WORKERS)
9.  [max\_parallel\_workers\_per\_gather](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER)
10. [max\_parallel\_workers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS)
11. [max\_replication\_slots](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) (CLI only)
12. [max\_slot\_wal\_keep\_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-SLOT-WAL-KEEP-SIZE) (CLI only)
13. [max\_standby\_archive\_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-ARCHIVE-DELAY) (CLI only)
14. [max\_standby\_streaming\_delay](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-STANDBY-STREAMING-DELAY) (CLI only)
15. [max\_wal\_size](https://www.postgresql.org/docs/current/runtime-config-wal.html#GUC-MAX-WAL-SIZE) (CLI only)
16. [max\_wal\_senders](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) (CLI only)
17. [max\_worker\_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) (CLI only)
18. [session\_replication\_role](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-SESSION-REPLICATION-ROLE)
19. [shared\_buffers](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-SHARED-BUFFERS) (CLI only)
20. [statement\_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT)
21. [track\_activity\_query\_size](https://www.postgresql.org/docs/current/runtime-config-statistics.html#GUC-TRACK-ACTIVITY-QUERY-SIZE)
22. [track\_commit\_timestamp](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-TRACK-COMMIT-TIMESTAMP)
23. [wal\_keep\_size](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-KEEP-SIZE) (CLI only)
24. [wal\_sender\_timeout](https://www.postgresql.org/docs/current/runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT) (CLI only)
25. [work\_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM)


#### Managing Postgres configuration with the CLI

To start:

1.  [Install](/docs/guides/resources/supabase-cli) Supabase CLI 1.69.0+.
2.  [Log in](/docs/guides/cli/local-development#log-in-to-the-supabase-cli) to your Supabase account using the CLI.

To update Postgres configurations, use the [`postgres config`](/docs/reference/cli/supabase-postgres-config) command:

```bash
supabase --experimental \
--project-ref <project-ref> \
postgres-config update --config shared_buffers=250MB
```

By default, the CLI will merge any provided config overrides with any existing ones. The `--replace-existing-overrides` flag can be used to instead force all existing overrides to be replaced with the ones being provided:

```bash
supabase --experimental \
--project-ref <project-ref> \
postgres-config update --config max_parallel_workers=3 \
--replace-existing-overrides
```

To delete specific configuration overrides, use the `postgres-config delete` command:

```bash
supabase --experimental \
--project-ref <project-ref> \
postgres-config delete --config shared_buffers,work_mem
```

By default, CLI v2 (≥ 2.0.0) checks the parameter’s context and requests the correct action (reload or restart):

*   If the setting can be reloaded (`pg_settings.context = 'sighup'`), then the Management API will detect this and apply the change with a configuration reload.
*   If the setting requires a restart (`pg_settings.context = 'postmaster'`), then both the primary and any read replicas will restart to apply the change.

To check whether a parameter can be reloaded without a restart, see the [Postgres docs](https://www.postgresql.org/docs/current/runtime-config.html).

You can verify whether changes have been applied with the following checks:

```bash
supabase --version;
```

```sql
-- Check whether the parameters were updated (and if a restart is pending):
select name, setting, context, pending_restart
from pg_settings
where name in ('max_slot_wal_keep_size', 'shared_buffers', 'max_connections');
```

```sql
-- If the timestamp hasn’t changed, no restart occurred
select pg_postmaster_start_time();
```

You can also pass the `--no-restart` flag to attempt a reload-only apply. If the parameter cannot be reloaded, the change stays pending until the next restart.

<Admonition type="note" label="Read Replicas and Custom Config">
  Postgres requires several parameters to be synchronized between the Primary cluster and [Read Replicas](/docs/guides/platform/read-replicas).

  By default, Supabase ensures that this propagation is executed correctly. However, if the `--no-restart` behavior is used in conjunction with parameters that cannot be reloaded without a restart, the user is responsible for ensuring that both the primaries and the read replicas get restarted in a timely manner to ensure a stable running state. Leaving the configuration updated, but not utilized (via a restart) in such a case can result in read replica failure if the primary, or a read replica, restarts in isolation (e.g. due to an out-of-memory event, or hardware failure).
</Admonition>

```bash
supabase --experimental \
--project-ref <project-ref> \
postgres-config delete --config shared_buffers --no-restart
```


### Resetting to default config

To reset a setting to its default value at the database level:

```sql
-- reset a single setting at the database level
alter database "postgres" set "<setting_name>" to default;

-- reset all settings at the database level
alter database "postgres" reset all;
```

For `role` level configurations, you can run:

```sql
alter role "<role_name>" set "<setting_name>" to default;
```


### Considerations

1.  Changes through the CLI might restart the database causing momentary disruption to existing database connections; in most cases this should not take more than a few seconds. However, you can use the --no-restart flag to bypass the restart and keep the connections intact. Keep in mind that this depends on the specific configuration changes you're making. if the change requires a restart, using the --no-restart flag will prevent the restart but you won't see those changes take effect until a restart is manually triggered. Additionally, some parameters are required to be the same on Primary and Read Replicas; not restarting in these cases can result in read replica failure if the Primary/Read Replicas restart in isolation.
2.  Custom Postgres Config will always override the default optimizations generated by Supabase. When changing compute add-ons, you should also review and update your custom Postgres Config to ensure they remain compatible and effective with the updated compute.
3.  Some parameters (e.g. `wal_keep_size`) can increase disk utilization, triggering disk expansion, which in turn can lead to [increases in your bill](/docs/guides/platform/compute-add-ons#disk-io).



# Connecting with DBeaver



If you do not have DBeaver, you can download it from its [website](https://dbeaver.io/download/).

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a new database connection">
      Create a new database connection
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![new database connection](/docs/img/guides/database/connecting-to-postgres/dbeaver/new_database_connection.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Select PostgreSQL" />

    <StepHikeCompact.Code>
      ![Selection Menu](/docs/img/guides/database/connecting-to-postgres/dbeaver/select_postgres.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Get Your Credentials">
      On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true), note your session pooler's:

      *   host
      *   username

      You will also need your database's password. If you forgot it, you can generate a new one in the settings.

      <Admonition type="note">
        If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![database credentials](/docs/img/guides/database/connecting-to-postgres/dbeaver/session_mode.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Fill out credentials">
      In DBeaver's Main menu, add your host, username, and password
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![filling out form](/docs/img/guides/database/connecting-to-postgres/dbeaver/filling_credentials.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Download certificate">
      In the [Database Settings](/dashboard/project/_/database/settings), download your SSL certificate.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![filling out form](/docs/img/guides/database/connecting-to-postgres/dbeaver/certificate.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Secure your connection">
      In DBeaver's SSL tab, add your SSL certificate
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![filling out form](/docs/img/guides/database/connecting-to-postgres/dbeaver/ssl_tab.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={7}>
    <StepHikeCompact.Details title="Connect">
      Test your connection and then click finish. You should now be able to interact with your database with DBeaver
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![connected dashboard](/docs/img/guides/database/connecting-to-postgres/dbeaver/finished.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Debugging performance issues

Debug slow-running queries using the Postgres execution planner.

`explain()` is a method that provides the Postgres `EXPLAIN` execution plan of a query. It is a powerful tool for debugging slow queries and understanding how Postgres will execute a given query. This feature is applicable to any query, including those made through `rpc()` or write operations.



## Enabling `explain()`

`explain()` is disabled by default to protect sensitive information about your database structure and operations. We recommend using `explain()` in a non-production environment. Run the following SQL to enable `explain()`:

{/* prettier-ignore */}

```sql
-- enable explain
alter role authenticator
set pgrst.db_plan_enabled to 'true';

-- reload the config
notify pgrst, 'reload config';
```



## Using `explain()`

To get the execution plan of a query, you can chain the `explain()` method to a Supabase query:

{/* prettier-ignore */}

```ts
const { data, error } = await supabase
  .from('instruments')
  .select()
  .explain()
```


### Example data

To illustrate, consider the following setup of a `instruments` table:

{/* prettier-ignore */}

```sql
create table instruments (
  id int8 primary key,
  name text
);

insert into books
  (id, name)
values
  (1, 'violin'),
  (2, 'viola'),
  (3, 'cello');
```


### Expected response

The response would typically look like this:

{/* prettier-ignore */}

```markdown
Aggregate  (cost=33.34..33.36 rows=1 width=112)
  ->  Limit  (cost=0.00..18.33 rows=1000 width=40)
        ->  Seq Scan on instruments  (cost=0.00..22.00 rows=1200 width=40)
```

By default, the execution plan is returned in TEXT format. However, you can also retrieve it as JSON by specifying the `format` parameter.



## Production use with pre-request protection

If you need to enable `explain()` in a production environment, ensure you protect your database by restricting access to the `explain()` feature. You can do so by using a pre-request function that filters requests based on the IP address:

{/* prettier-ignore */}

```sql
create or replace function filter_plan_requests()
returns void as $$
declare
  headers   json := current_setting('request.headers', true)::json;
  client_ip text := coalesce(headers->>'cf-connecting-ip', '');
  accept    text := coalesce(headers->>'accept', '');
  your_ip   text := '123.123.123.123'; -- replace this with your IP
begin
  if accept like 'application/vnd.pgrst.plan%' and client_ip != your_ip then
    raise insufficient_privilege using
      message = 'Not allowed to use application/vnd.pgrst.plan';
  end if;
end; $$ language plpgsql;
alter role authenticator set pgrst.db_pre_request to 'filter_plan_requests';
notify pgrst, 'reload config';
```

Replace `'123.123.123.123'` with your actual IP address.



## Disabling explain

To disable the `explain()` method after use, execute the following SQL commands:

{/* prettier-ignore */}

```sql
-- disable explain
alter role authenticator
set pgrst.db_plan_enabled to 'false';

-- if you used the above pre-request
alter role authenticator
set pgrst.db_pre_request to '';

-- reload the config
notify pgrst, 'reload config';
```



# Drizzle



### Connecting with Drizzle

[Drizzle ORM](https://github.com/drizzle-team/drizzle-orm) is a TypeScript ORM for SQL databases designed with maximum type safety in mind. You can use their ORM to connect to your database.

<Admonition type="note">
  If you plan on solely using Drizzle instead of the Supabase Data API (PostgREST), you can turn off the latter in the [API Settings](/dashboard/project/_/settings/api).
</Admonition>

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Install">
      Install Drizzle and related dependencies.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```shell
      npm i drizzle-orm postgres
      npm i -D drizzle-kit
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create your models">
      Create a `schema.ts` file and define your models.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts schema.ts
      import { pgTable, serial, text, varchar } from "drizzle-orm/pg-core";

      export const users = pgTable('users', {
        id: serial('id').primaryKey(),
        fullName: text('full_name'),
        phone: varchar('phone', { length: 256 }),
      });
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Connect">
      Connect to your database using the Connection Pooler.

      From the project  [**Connect** panel](/dashboard/project/_?showConnect=true), copy the URI from the "Shared Pooler" option and save it as the `DATABASE_URL` environment variable. Remember to replace the password placeholder with your actual database password.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts db.ts
      import 'dotenv/config'

      import { drizzle } from 'drizzle-orm/postgres-js'
      import postgres from 'postgres'

      const connectionString = process.env.DATABASE_URL

      // Disable prefetch as it is not supported for "Transaction" pool mode
      export const client = postgres(connectionString, { prepare: false })
      export const db = drizzle(client);
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Postgres Extensions Overview



Extensions are exactly as they sound - they "extend" the database with functionality which isn't part of the Postgres core.
Supabase has pre-installed some of the most useful open source extensions.


### Enable and disable extensions

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click **Extensions** in the sidebar.
    3.  Enable or disable an extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
     -- Example: enable the "pgtap" extension and ensure it is installed
    create extension pgtap
    with
      schema extensions;

    -- Example: disable the "pgtap" extension
    drop
      extension pgtap;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension call `drop extension`.
  </TabPanel>
</Tabs>

<Admonition type="note">
  Most extensions are installed under the `extensions` schema, which is accessible to public by default. To avoid namespace pollution, we do not recommend creating other entities in the `extensions` schema.

  If you need to restrict user access to tables managed by extensions, we recommend creating a separate schema for installing that specific extension.

  Some extensions can only be created under a specific schema, for example, `postgis_tiger_geocoder` extension creates a schema named `tiger`. Before enabling such extensions, make sure you have not created a conflicting schema with the same name.

  In addition to the pre-configured extensions, you can also install your own SQL extensions directly in the database using Supabase's SQL editor. The SQL code for the extensions, including plpgsql extensions, can be added through the SQL editor.
</Admonition>


### Upgrade extensions

If a new version of an extension becomes available on Supabase, you need to initiate a software upgrade in the [Infrastructure Settings](/dashboard/project/_/settings/infrastructure) to access it. Software upgrades can also be initiated by restarting your server in the [General Settings](/dashboard/project/_/settings/general).


### Full list of extensions

Supabase is pre-configured with over 50 extensions and you can install additional extensions through the [database.dev](https://database.dev/) package manager.

You can install pure SQL extensions directly in the database using the SQL editor or any Postgres client.

If you would like to request an extension, add (or upvote) it in the [GitHub Discussion](https://github.com/orgs/supabase/discussions/33754).

<Extensions />



# Full Text Search

How to use full text search in PostgreSQL.

Postgres has built-in functions to handle `Full Text Search` queries. This is like a "search engine" within Postgres.



## Preparation

For this guide we'll use the following example data:

<Tabs scrollable size="small" type="underlined" defaultActiveId="data" queryGroup="example-view">
  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title                               | author                 | description                                                        |
    | -- | ----------------------------------- | ---------------------- | ------------------------------------------------------------------ |
    | 1  | The Poky Little Puppy               | Janette Sebring Lowrey | Puppy is slower than other, bigger animals.                        |
    | 2  | The Tale of Peter Rabbit            | Beatrix Potter         | Rabbit eats some vegetables.                                       |
    | 3  | Tootle                              | Gertrude Crampton      | Little toy train has big dreams.                                   |
    | 4  | Green Eggs and Ham                  | Dr. Seuss              | Sam has changing food preferences and eats unusually colored food. |
    | 5  | Harry Potter and the Goblet of Fire | J.K. Rowling           | Fourth year of school starts, big drama ensues.                    |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create table books (
      id serial primary key,
      title text,
      author text,
      description text
    );

    insert into books
      (title, author, description)
    values
      (
        'The Poky Little Puppy',
        'Janette Sebring Lowrey',
        'Puppy is slower than other, bigger animals.'
      ),
      ('The Tale of Peter Rabbit', 'Beatrix Potter', 'Rabbit eats some vegetables.'),
      ('Tootle', 'Gertrude Crampton', 'Little toy train has big dreams.'),
      (
        'Green Eggs and Ham',
        'Dr. Seuss',
        'Sam has changing food preferences and eats unusually colored food.'
      ),
      (
        'Harry Potter and the Goblet of Fire',
        'J.K. Rowling',
        'Fourth year of school starts, big drama ensues.'
      );
    ```
  </TabPanel>
</Tabs>



## Usage

The functions we'll cover in this guide are:


### `to_tsvector()` \[#to-tsvector]

Converts your data into searchable tokens. `to_tsvector()` stands for "to text search vector." For example:

```sql
select to_tsvector('green eggs and ham');
-- Returns 'egg':2 'green':1 'ham':4
```

Collectively these tokens are called a "document" which Postgres can use for comparisons.


### `to_tsquery()` \[#to-tsquery]

Converts a query string into tokens to match. `to_tsquery()` stands for "to text search query."

This conversion step is important because we will want to "fuzzy match" on keywords.
For example if a user searches for `eggs`, and a column has the value `egg`, we probably still want to return a match.

Postgres provides several functions to create tsquery objects:

*   **`to_tsquery()`** - Requires manual specification of operators (`&`, `|`, `!`)
*   **`plainto_tsquery()`** - Converts plain text to an AND query: `plainto_tsquery('english', 'fat rats')` → `'fat' & 'rat'`
*   **`phraseto_tsquery()`** - Creates phrase queries: `phraseto_tsquery('english', 'fat rats')` → `'fat' <-> 'rat'`
*   **`websearch_to_tsquery()`** - Supports web search syntax with quotes, "or", and negation


### Match: `@@` \[#match]

The `@@` symbol is the "match" symbol for Full Text Search. It returns any matches between a `to_tsvector` result and a `to_tsquery` result.

Take the following example:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select *
    from books
    where title = 'Harry';
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').select().eq('title', 'Harry')
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .eq('title', 'Harry');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.from("books")
      .select()
      .eq("title", value: "Harry")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            eq("title", "Harry")
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('books').select().eq('title', 'Harry').execute()
    ```
  </TabPanel>
</Tabs>

The equality symbol above (`=`) is very "strict" on what it matches. In a full text search context, we might want to find all "Harry Potter" books and so we can rewrite the
example above:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select *
    from books
    where to_tsvector(title) @@ to_tsquery('Harry');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').select().textSearch('title', `'Harry'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('title', "'Harry'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.from("books")
      .select()
      .textSearch("title", value: "'Harry'")
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("title", "'Harry'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>
</Tabs>



## Basic full text queries


### Search a single column

To find all `books` where the `description` contain the word `big`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description)
      @@ to_tsquery('big');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').select().textSearch('description', `'big'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'big'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = await client.from("books")
      .select()
      .textSearch("description", value: "'big'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'big'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('books').select().text_search('description', "'big'").execute()
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title                               | author            | description                                     |
    | -- | ----------------------------------- | ----------------- | ----------------------------------------------- |
    | 3  | Tootle                              | Gertrude Crampton | Little toy train has big dreams.                |
    | 5  | Harry Potter and the Goblet of Fire | J.K. Rowling      | Fourth year of school starts, big drama ensues. |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>
</Tabs>


### Search multiple columns

Right now there is no direct way to use JavaScript or Dart to search through multiple columns but you can do it by creating [computed columns](https://postgrest.org/en/stable/api.html#computed-virtual-columns) on the database.

To find all `books` where `description` or `title` contain the word `little`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description || ' ' || title) -- concat columns, but be sure to include a space to separate them!
      @@ to_tsquery('little');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```sql
    create function title_description(books) returns text as $$
      select $1.title || ' ' || $1.description;
    $$ language sql immutable;
    ```

    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('title_description', `little`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```sql
    create function title_description(books) returns text as $$
      select $1.title || ' ' || $1.description;
    $$ language sql immutable;
    ```

    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('title_description', "little")
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```sql
    create function title_description(books) returns text as $$
      select $1.title || ' ' || $1.description;
    $$ language sql immutable;
    ```

    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("title_description", value: "little")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```sql
    create function title_description(books) returns text as $$
      select $1.title || ' ' || $1.description;
    $$ language sql immutable;
    ```

    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("title_description", "title", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```sql
    create function title_description(books) returns text as $$
      select $1.title || ' ' || $1.description;
    $$ language sql immutable;
    ```

    ```python
    data = supabase.from_('books').select().text_search('title_description', "little").execute()
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title                 | author                 | description                                 |
    | -- | --------------------- | ---------------------- | ------------------------------------------- |
    | 1  | The Poky Little Puppy | Janette Sebring Lowrey | Puppy is slower than other, bigger animals. |
    | 3  | Tootle                | Gertrude Crampton      | Little toy train has big dreams.            |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>
</Tabs>


### Match all search words

To find all `books` where `description` contains BOTH of the words `little` and `big`, we can use the `&` symbol:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description)
      @@ to_tsquery('little & big'); -- use & for AND in the search query
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', `'little' & 'big'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'little' & 'big'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("description", value: "'little' & 'big'");
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'title' & 'big'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('books').select().text_search('description', "'little' & 'big'").execute()
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title  | author            | description                      |
    | -- | ------ | ----------------- | -------------------------------- |
    | 3  | Tootle | Gertrude Crampton | Little toy train has big dreams. |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>
</Tabs>


### Match any search words

To find all `books` where `description` contain ANY of the words `little` or `big`, use the `|` symbol:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description)
      @@ to_tsquery('little | big'); -- use | for OR in the search query
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', `'little' | 'big'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'little' | 'big'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("description", value: "'little' | 'big'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'title' | 'big'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    response = client.from_('books').select().text_search('description', "'little' | 'big'").execute()
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title                 | author                 | description                                 |
    | -- | --------------------- | ---------------------- | ------------------------------------------- |
    | 1  | The Poky Little Puppy | Janette Sebring Lowrey | Puppy is slower than other, bigger animals. |
    | 3  | Tootle                | Gertrude Crampton      | Little toy train has big dreams.            |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>
</Tabs>

Notice how searching for `big` includes results with the word `bigger` (or `biggest`, etc).



## Partial search

Partial search is particularly useful when you want to find matches on substrings within your data.


### Implementing partial search

You can use the `:*` syntax with `to_tsquery()`. Here's an example that searches for any book titles beginning with "Lit":

```sql
select title from books where to_tsvector(title) @@ to_tsquery('Lit:*');
```


### Extending functionality with RPC

To make the partial search functionality accessible through the API, you can wrap the search logic in a stored procedure.

After creating this function, you can invoke it from your application using the SDK for your platform. Here's an example:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    create or replace function search_books_by_title_prefix(prefix text)
    returns setof books AS $$
    begin
      return query
      select * from books where to_tsvector('english', title) @@ to_tsquery(prefix || ':*');
    end;
    $$ language plpgsql;
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('search_books_by_title_prefix', { prefix: 'Lit' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.rpc('search_books_by_title_prefix', params: { 'prefix': 'Lit' });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.rpc(
      "search_books_by_title_prefix",
      params: ["prefix": "Lit"]
    )
    .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val rpcParams = mapOf("prefix" to "Lit")
    val result = supabase.postgrest.rpc("search_books_by_title_prefix", rpcParams)
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.rpc('search_books_by_title_prefix', { 'prefix': 'Lit' }).execute()
    ```
  </TabPanel>
</Tabs>

This function takes a prefix parameter and returns all books where the title contains a word starting with that prefix. The `:*` operator is used to denote a prefix match in the `to_tsquery()` function.



## Handling spaces in queries

When you want the search term to include a phrase or multiple words, you can concatenate words using a `+` as a placeholder for space:

```sql
select * from search_books_by_title_prefix('Little+Puppy');
```



## Web search syntax with `websearch_to_tsquery()` \[#websearch-to-tsquery]

The `websearch_to_tsquery()` function provides an intuitive search syntax similar to popular web search engines, making it ideal for user-facing search interfaces.


### Basic usage

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select *
    from books
    where to_tsvector(description) @@ websearch_to_tsquery('english', 'green eggs');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', 'green eggs', { type: 'websearch' })
    ```
  </TabPanel>
</Tabs>


### Quoted phrases

Use quotes to search for exact phrases:

```sql
select * from books
where to_tsvector(description || ' ' || title) @@ websearch_to_tsquery('english', '"Green Eggs"');
-- Matches documents containing "Green" immediately followed by "Eggs"
```


### OR searches

Use "or" (case-insensitive) to search for multiple terms:

```sql
select * from books
where to_tsvector(description) @@ websearch_to_tsquery('english', 'puppy or rabbit');
-- Matches documents containing either "puppy" OR "rabbit"
```


### Negation

Use a dash (-) to exclude terms:

```sql
select * from books
where to_tsvector(description) @@ websearch_to_tsquery('english', 'animal -rabbit');
-- Matches documents containing "animal" but NOT "rabbit"
```


### Complex queries

Combine multiple operators for sophisticated searches:

```sql
select * from books
where to_tsvector(description || ' ' || title) @@
  websearch_to_tsquery('english', '"Harry Potter" or "Dr. Seuss" -vegetables');
-- Matches books by "Harry Potter" or "Dr. Seuss" but excludes those mentioning vegetables
```



## Creating indexes

Now that you have Full Text Search working, create an `index`. This allows Postgres to "build" the documents preemptively so that they
don't need to be created at the time we execute the query. This will make our queries much faster.


### Searchable columns

Let's create a new column `fts` inside the `books` table to store the searchable index of the `title` and `description` columns.

We can use a special feature of Postgres called
[Generated Columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html)
to ensure that the index is updated any time the values in the `title` and `description` columns change.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="example-view">
  <TabPanel id="sql" label="SQL">
    ```sql
    alter table
      books
    add column
      fts tsvector generated always as (to_tsvector('english', description || ' ' || title)) stored;

    create index books_fts on books using gin (fts); -- generate the index

    select id, fts
    from books;
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    ```
    | id  | fts                                                                                                             |
    | --- | --------------------------------------------------------------------------------------------------------------- |
    | 1   | 'anim':7 'bigger':6 'littl':10 'poki':9 'puppi':1,11 'slower':3                                                 |
    | 2   | 'eat':2 'peter':8 'rabbit':1,9 'tale':6 'veget':4                                                               |
    | 3   | 'big':5 'dream':6 'littl':1 'tootl':7 'toy':2 'train':3                                                         |
    | 4   | 'chang':3 'color':9 'eat':7 'egg':12 'food':4,10 'green':11 'ham':14 'prefer':5 'sam':1 'unus':8                |
    | 5   | 'big':6 'drama':7 'ensu':8 'fire':15 'fourth':1 'goblet':13 'harri':9 'potter':10 'school':4 'start':5 'year':2 |
    ```
  </TabPanel>
</Tabs>


### Search using the new column

Now that we've created and populated our index, we can search it using the same techniques as before:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      fts @@ to_tsquery('little & big');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').select().textSearch('fts', `'little' & 'big'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('fts', "'little' & 'big'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("fts", value: "'little' & 'big'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("fts", "'title' & 'big'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.from_('books').select().text_search('fts', "'little' & 'big'").execute()
    ```
  </TabPanel>

  <TabPanel id="data" label="Data">
    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title  | author            | description                      | fts                                                     |
    | -- | ------ | ----------------- | -------------------------------- | ------------------------------------------------------- |
    | 3  | Tootle | Gertrude Crampton | Little toy train has big dreams. | 'big':5 'dream':6 'littl':1 'tootl':7 'toy':2 'train':3 |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>
</Tabs>



## Query operators

Visit [Postgres: Text Search Functions and Operators](https://www.postgresql.org/docs/current/functions-textsearch.html)
to learn about additional query operators you can use to do more advanced `full text queries`, such as:


### Proximity: `<->` \[#proximity]

The proximity symbol is useful for searching for terms that are a certain "distance" apart.
For example, to find the phrase `big dreams`, where the a match for "big" is followed immediately by a match for "dreams":

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description) @@ to_tsquery('big <-> dreams');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', `'big' <-> 'dreams'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'big' <-> 'dreams'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("description", value: "'big' <-> 'dreams'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'big' <-> 'dreams'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.from_('books').select().text_search('description', "'big' <-> 'dreams'").execute()
    ```
  </TabPanel>
</Tabs>

We can also use the `<->` to find words within a certain distance of each other. For example to find `year` and `school` within 2 words of each other:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description) @@ to_tsquery('year <2> school');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', `'year' <2> 'school'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'year' <2> 'school'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase
      .from("books")
      .select()
      .textSearch("description", value: "'year' <2> 'school'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'year' <2> 'school'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.from_('books').select().text_search('description', "'year' <2> 'school'").execute()
    ```
  </TabPanel>
</Tabs>


### Negation: `!` \[#negation]

The negation symbol can be used to find phrases which *don't* contain a search term.
For example, to find records that have the word `big` but not `little`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      *
    from
      books
    where
      to_tsvector(description) @@ to_tsquery('big & !little');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase
      .from('books')
      .select()
      .textSearch('description', `'big' & !'little'`)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .from('books')
      .select()
      .textSearch('description', "'big' & !'little'");
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await client
      .from("books")
      .select()
      .textSearch("description", value: "'big' & !'little'")
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select {
        filter {
            textSearch("description", "'big' & !'little'", TextSearchType.NONE)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.from_('books').select().text_search('description', "'big' & !'little'").execute()
    ```
  </TabPanel>
</Tabs>



## Ranking search results \[#ranking]

Postgres provides ranking functions to sort search results by relevance, helping you present the most relevant matches first. Since ranking functions need to be computed server-side, use RPC functions and generated columns.


### Creating a search function with ranking \[#search-function-ranking]

First, create a Postgres function that handles search and ranking:

```sql
create or replace function search_books(search_query text)
returns table(id int, title text, description text, rank real) as $$
begin
  return query
  select
    books.id,
    books.title,
    books.description,
    ts_rank(to_tsvector('english', books.description), to_tsquery(search_query)) as rank
  from books
  where to_tsvector('english', books.description) @@ to_tsquery(search_query)
  order by rank desc;
end;
$$ language plpgsql;
```

Now you can call this function from your client:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('search_books', { search_query: 'big' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .rpc('search_books', params: { 'search_query': 'big' });
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.rpc('search_books', { 'search_query': 'big' }).execute()
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    select * from search_books('big');
    ```
  </TabPanel>
</Tabs>


### Ranking with weighted columns \[#weighted-ranking]

Postgres allows you to assign different importance levels to different parts of your documents using weight labels. This is especially useful when you want matches in certain fields (like titles) to rank higher than matches in other fields (like descriptions).


#### Understanding weight labels

Postgres uses four weight labels: **A**, **B**, **C**, and **D**, where:

*   **A** = Highest importance (weight 1.0)
*   **B** = High importance (weight 0.4)
*   **C** = Medium importance (weight 0.2)
*   **D** = Low importance (weight 0.1)


#### Creating weighted search columns

First, create a weighted tsvector column that gives titles higher priority than descriptions:

```sql
-- Add a weighted fts column
alter table books
add column fts_weighted tsvector
generated always as (
  setweight(to_tsvector('english', title), 'A') ||
  setweight(to_tsvector('english', description), 'B')
) stored;

-- Create index for the weighted column
create index books_fts_weighted on books using gin (fts_weighted);
```

Now create a search function that uses this weighted column:

```sql
create or replace function search_books_weighted(search_query text)
returns table(id int, title text, description text, rank real) as $$
begin
  return query
  select
    books.id,
    books.title,
    books.description,
    ts_rank(books.fts_weighted, to_tsquery(search_query)) as rank
  from books
  where books.fts_weighted @@ to_tsquery(search_query)
  order by rank desc;
end;
$$ language plpgsql;
```


#### Custom weight arrays

You can also specify custom weights by providing a weight array to `ts_rank()`:

```sql
create or replace function search_books_custom_weights(search_query text)
returns table(id int, title text, description text, rank real) as $$
begin
  return query
  select
    books.id,
    books.title,
    books.description,
    ts_rank(
      '{0.0, 0.2, 0.5, 1.0}'::real[], -- Custom weights {D, C, B, A}
      books.fts_weighted,
      to_tsquery(search_query)
    ) as rank
  from books
  where books.fts_weighted @@ to_tsquery(search_query)
  order by rank desc;
end;
$$ language plpgsql;
```

This example uses custom weights where:

*   A-labeled terms (titles) have maximum weight (1.0)
*   B-labeled terms (descriptions) have medium weight (0.5)
*   C-labeled terms have low weight (0.2)
*   D-labeled terms are ignored (0.0)


#### Using the weighted search

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    // Search with standard weighted ranking
    const { data, error } = await supabase.rpc('search_books_weighted', { search_query: 'Harry' })

    // Search with custom weights
    const { data: customData, error: customError } = await supabase.rpc('search_books_custom_weights', {
      search_query: 'Harry',
    })
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    # Search with standard weighted ranking
    data = client.rpc('search_books_weighted', { 'search_query': 'Harry' }).execute()

    # Search with custom weights
    custom_data = client.rpc('search_books_custom_weights', { 'search_query': 'Harry' }).execute()
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Standard weighted search
    select * from search_books_weighted('Harry');

    -- Custom weighted search
    select * from search_books_custom_weights('Harry');
    ```
  </TabPanel>
</Tabs>


#### Practical example with results

Say you search for "Harry". With weighted columns:

1.  **"Harry Potter and the Goblet of Fire"** (title match) gets weight A = 1.0
2.  **Books mentioning "Harry" in description** get weight B = 0.4

This ensures that books with "Harry" in the title ranks significantly higher than books that only mention "Harry" in the description, providing more relevant search results for users.


### Using ranking with indexes \[#ranking-with-indexes]

When using the `fts` column you created earlier, ranking becomes more efficient. Create a function that uses the indexed column:

```sql
create or replace function search_books_fts(search_query text)
returns table(id int, title text, description text, rank real) as $$
begin
  return query
  select
    books.id,
    books.title,
    books.description,
    ts_rank(books.fts, to_tsquery(search_query)) as rank
  from books
  where books.fts @@ to_tsquery(search_query)
  order by rank desc;
end;
$$ language plpgsql;
```

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('search_books_fts', { search_query: 'little & big' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final result = await client
      .rpc('search_books_fts', params: { 'search_query': 'little & big' });
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = client.rpc('search_books_fts', { 'search_query': 'little & big' }).execute()
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    select * from search_books_fts('little & big');
    ```
  </TabPanel>
</Tabs>


### Using web search syntax with ranking \[#websearch-ranking]

You can also create a function that combines `websearch_to_tsquery()` with ranking for user-friendly search:

```sql
create or replace function websearch_books(search_text text)
returns table(id int, title text, description text, rank real) as $$
begin
  return query
  select
    books.id,
    books.title,
    books.description,
    ts_rank(books.fts, websearch_to_tsquery('english', search_text)) as rank
  from books
  where books.fts @@ websearch_to_tsquery('english', search_text)
  order by rank desc;
end;
$$ language plpgsql;
```

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    // Support natural search syntax
    const { data, error } = await supabase.rpc('websearch_books', {
      search_text: '"little puppy" or train -vegetables',
    })
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    select * from websearch_books('"little puppy" or train -vegetables');
    ```
  </TabPanel>
</Tabs>



## Resources

*   [Postgres: Text Search Functions and Operators](https://www.postgresql.org/docs/12/functions-textsearch.html)



# Database Functions



Postgres has built-in support for [SQL functions](https://www.postgresql.org/docs/current/sql-createfunction.html).
These functions live inside your database, and they can be [used with the API](../../reference/javascript/rpc).



## Quick demo

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/MJZCCpCYEqk" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Getting started

Supabase provides several options for creating database functions. You can use the Dashboard or create them directly using SQL.
We provide a SQL editor within the Dashboard, or you can [connect](../../guides/database/connecting-to-postgres) to your database
and run the SQL queries yourself.

1.  Go to the "SQL editor" section.
2.  Click "New Query".
3.  Enter the SQL to create or replace your Database function.
4.  Click "Run" or cmd+enter (ctrl+enter).



## Simple functions

Let's create a basic Database Function which returns a string "hello world".

```sql
create or replace function hello_world() -- 1
returns text -- 2
language sql -- 3
as $$  -- 4
  select 'hello world';  -- 5
$$; --6

```

<details>
  <summary>Show/Hide Details</summary>

  At it's most basic a function has the following parts:

  1.  `create or replace function hello_world()`: The function declaration, where `hello_world` is the name of the function. You can use either `create` when creating a new function or `replace` when replacing an existing function. Or you can use `create or replace` together to handle either.
  2.  `returns text`: The type of data that the function returns. If it returns nothing, you can `returns void`.
  3.  `language sql`: The language used inside the function body. This can also be a procedural language: `plpgsql`, `plpython`, etc.
  4.  `as $$`: The function wrapper. Anything enclosed inside the `$$` symbols will be part of the function body.
  5.  `select 'hello world';`: A simple function body. The final `select` statement inside a function body will be returned if there are no statements following it.
  6.  `$$;`: The closing symbols of the function wrapper.
</details>

<br />

<Admonition type="caution">
  When naming your functions, make the name of the function unique as overloaded functions are not supported.
</Admonition>

After the Function is created, we have several ways of "executing" the function - either directly inside the database using SQL, or with one of the client libraries.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select hello_world();
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('hello_world')
    ```

    Reference: [`rpc()`](../../reference/javascript/rpc)
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase
      .rpc('hello_world');
    ```

    Reference: [`rpc()`](../../reference/dart/rpc)
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.rpc("hello_world").execute()
    ```

    Reference: [`rpc()`](../../reference/swift/rpc)
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc("hello_world")
    ```

    Reference: [`rpc()`](../../reference/kotlin/rpc)
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.rpc('hello_world').execute()
    ```

    Reference: [`rpc()`](../../reference/python/rpc)
  </TabPanel>
</Tabs>



## Returning data sets

Database Functions can also return data sets from [Tables](../../guides/database/tables) or Views.

For example, if we had a database with some Star Wars data inside:

<Tabs scrollable size="small" type="underlined" defaultActiveId="data" queryGroup="example-view">
  <TabPanel id="data" label="Data">
    <h4>Planets</h4>

    ```
    | id  | name     |
    | --- | -------- |
    | 1   | Tatooine |
    | 2   | Alderaan |
    | 3   | Kashyyyk |
    ```

    <h4>People</h4>

    ```
    | id  | name             | planet_id |
    | --- | ---------------- | --------- |
    | 1   | Anakin Skywalker | 1         |
    | 2   | Luke Skywalker   | 1         |
    | 3   | Princess Leia    | 2         |
    | 4   | Chewbacca        | 3         |
    ```
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create table planets (
      id serial primary key,
      name text
    );

    insert into planets
      (id, name)
    values
      (1, 'Tattoine'),
      (2, 'Alderaan'),
      (3, 'Kashyyyk');

    create table people (
      id serial primary key,
      name text,
      planet_id bigint references planets
    );

    insert into people
      (id, name, planet_id)
    values
      (1, 'Anakin Skywalker', 1),
      (2, 'Luke Skywalker', 1),
      (3, 'Princess Leia', 2),
      (4, 'Chewbacca', 3);
    ```
  </TabPanel>
</Tabs>

We could create a function which returns all the planets:

```sql
create or replace function get_planets()
returns setof planets
language sql
as $$
  select * from planets;
$$;
```

Because this function returns a table set, we can also apply filters and selectors. For example, if we only wanted the first planet:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select *
    from get_planets()
    where id = 1;
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = supabase.rpc('get_planets').eq('id', 1)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase
      .rpc('get_planets')
      .eq('id', 1);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    let response = try await supabase.rpc("get_planets").eq("id", value: 1).execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc("get_planets") {
        filter {
            eq("id", 1)
        }
    }
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.rpc('get_planets').eq('id', 1).execute()
    ```
  </TabPanel>
</Tabs>



## Passing parameters

Let's create a Function to insert a new planet into the `planets` table and return the new ID. Note that this time we're using the `plpgsql` language.

```sql
create or replace function add_planet(name text)
returns bigint
language plpgsql
as $$
declare
  new_row bigint;
begin
  insert into planets(name)
  values (add_planet.name)
  returning id into new_row;

  return new_row;
end;
$$;
```

Once again, you can execute this function either inside your database using a `select` query, or with the client libraries:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select * from add_planet('Jakku');
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('add_planet', { name: 'Jakku' })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase
      .rpc('add_planet', params: { 'name': 'Jakku' });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Using `Encodable` type:

    ```swift
    struct Planet: Encodable {
      let name: String
    }

    try await supabase.rpc(
      "add_planet",
      params: Planet(name: "Jakku")
    )
    .execute()
    ```

    Using `AnyJSON` convenience\` type:

    ```swift
    try await supabase.rpc(
      "add_planet",
      params: ["name": AnyJSON.string("Jakku")]
    )
    .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc(
        function = "add_planet",
        parameters = buildJsonObject { //You can put here any serializable object including your own classes
            put("name", "Jakku")
        }
    )
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.rpc('add_planet', params={'name': 'Jakku'}).execute()
    ```
  </TabPanel>
</Tabs>



## Suggestions


### Database Functions vs Edge Functions

For data-intensive operations, use Database Functions, which are executed within your database
and can be called remotely using the [REST and GraphQL API](../api).

For use-cases which require low-latency, use [Edge Functions](../../guides/functions), which are globally-distributed and can be written in Typescript.


### Security `definer` vs `invoker`

Postgres allows you to specify whether you want the function to be executed as the user *calling* the function (`invoker`), or as the *creator* of the function (`definer`). For example:

```sql
create function hello_world()
returns text
language plpgsql
security definer set search_path = ''
as $$
begin
  select 'hello world';
end;
$$;
```

It is best practice to use `security invoker` (which is also the default). If you ever use `security definer`, you *must* set the `search_path`.
If you use an empty search path (`search_path = ''`), you must explicitly state the schema for every relation in the function body (e.g. `from public.table`).
This limits the potential damage if you allow access to schemas which the user executing the function should not have.


### Function privileges

By default, database functions can be executed by any role. There are two main ways to restrict this:

1.  On a case-by-case basis. Specifically revoke permissions for functions you want to protect. Execution needs to be revoked for both `public` and the role you're restricting:

    ```sql
    revoke execute on function public.hello_world from public;
    revoke execute on function public.hello_world from anon;
    ```

2.  Restrict function execution by default. Specifically *grant* access when you want a function to be executable by a specific role.

    To restrict all existing functions, revoke execution permissions from both `public` *and* the role you want to restrict:

    ```sql
    revoke execute on all functions in schema public from public;
    revoke execute on all functions in schema public from anon, authenticated;
    ```

    To restrict all new functions, change the default privileges for both `public` *and* the role you want to restrict:

    ```sql
    alter default privileges in schema public revoke execute on functions from public;
    alter default privileges in schema public revoke execute on functions from anon, authenticated;
    ```

    You can then regrant permissions for a specific function to a specific role:

    ```sql
    grant execute on function public.hello_world to authenticated;
    ```


### Debugging functions

You can add logs to help you debug functions. This is especially recommended for complex functions.

Good targets to log include:

*   Values of (non-sensitive) variables
*   Returned results from queries


#### General logging

To create custom logs in the [Dashboard's Postgres Logs](/dashboard/project/_/logs/postgres-logs), you can use the `raise` keyword. By default, there are 3 observed severity levels:

*   `log`
*   `warning`
*   `exception` (error level)

```sql
create function logging_example(
  log_message text,
  warning_message text,
  error_message text
)
returns void
language plpgsql
as $$
begin
  raise log 'logging message: %', log_message;
  raise warning 'logging warning: %', warning_message;

  -- immediately ends function and reverts transaction
  raise exception 'logging error: %', error_message;
end;
$$;

select logging_example('LOGGED MESSAGE', 'WARNING MESSAGE', 'ERROR MESSAGE');
```


#### Error handling

You can create custom errors with the `raise exception` keywords.

A common pattern is to throw an error when a variable doesn't meet a condition:

```sql
create or replace function error_if_null(some_val text)
returns text
language plpgsql
as $$
begin
  -- error if some_val is null
  if some_val is null then
    raise exception 'some_val should not be NULL';
  end if;
  -- return some_val if it is not null
  return some_val;
end;
$$;

select error_if_null(null);
```

Value checking is common, so Postgres provides a shorthand: the `assert` keyword. It uses the following format:

```sql
-- throw error when condition is false
assert <some condition>, 'message';
```

Below is an example

```sql
create function assert_example(name text)
returns uuid
language plpgsql
as $$
declare
  student_id uuid;
begin
  -- save a user's id into the user_id variable
  select
    id into student_id
  from attendance_table
  where student = name;

  -- throw an error if the student_id is null
  assert student_id is not null, 'assert_example() ERROR: student not found';

  -- otherwise, return the user's id
  return student_id;
end;
$$;

select assert_example('Harry Potter');
```

Error messages can also be captured and modified with the `exception` keyword:

```sql
create function error_example()
returns void
language plpgsql
as $$
begin
  -- fails: cannot read from nonexistent table
  select * from table_that_does_not_exist;

  exception
      when others then
          raise exception 'An error occurred in function <function name>: %', sqlerrm;
end;
$$;
```


#### Advanced logging

For more complex functions or complicated debugging, try logging:

*   Formatted variables
*   Individual rows
*   Start and end of function calls

```sql
create or replace function advanced_example(num int default 10)
returns text
language plpgsql
as $$
declare
    var1 int := 20;
    var2 text;
begin
    -- Logging start of function
    raise log 'logging start of function call: (%)', (select now());

    -- Logging a variable from a SELECT query
    select
      col_1 into var1
    from some_table
    limit 1;
    raise log 'logging a variable (%)', var1;

    -- It is also possible to avoid using variables, by returning the values of your query to the log
    raise log 'logging a query with a single return value(%)', (select col_1 from some_table limit 1);

    -- If necessary, you can even log an entire row as JSON
    raise log 'logging an entire row as JSON (%)', (select to_jsonb(some_table.*) from some_table limit 1);

    -- When using INSERT or UPDATE, the new value(s) can be returned
    -- into a variable.
    -- When using DELETE, the deleted value(s) can be returned.
    -- All three operations use "RETURNING value(s) INTO variable(s)" syntax
    insert into some_table (col_2)
    values ('new val')
    returning col_2 into var2;

    raise log 'logging a value from an INSERT (%)', var2;

    return var1 || ',' || var2;
exception
    -- Handle exceptions here if needed
    when others then
        raise exception 'An error occurred in function <advanced_example>: %', sqlerrm;
end;
$$;

select advanced_example();
```



## Resources

*   Official Client libraries: [JavaScript](../../reference/javascript/rpc) and [Flutter](../../reference/dart/rpc)
*   Community client libraries: [github.com/supabase-community](https://github.com/supabase-community)
*   Postgres Official Docs: [Chapter 9. Functions and Operators](https://www.postgresql.org/docs/current/functions.html)
*   Postgres Reference: [CREATE FUNCTION](https://www.postgresql.org/docs/9.1/sql-createfunction.html)



## Deep dive


### Create Database Functions

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/MJZCCpCYEqk" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>


### Call Database Functions using JavaScript

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/I6nnp9AINJk" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>


### Using Database Functions to call an external API

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/rARgrELRCwY" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



# Hardening the Data API



Your database's auto-generated Data API exposes the `public` schema by default. You can change this to any schema in your database, or even disable the Data API completely.

Any tables that are accessible through the Data API *must* have [Row Level Security](/docs/guides/database/postgres/row-level-security) enabled. Row Level Security (RLS) is enabled by default when you create tables from the Supabase Dashboard. If you create a table using the SQL editor or your own SQL client or migration runner, you*must* enable RLS yourself.



## Shared responsibility

Your application's security is your responsibility as a developer. This includes RLS, falling under the [Shared Responsibility](/docs/guides/deployment/shared-responsibility-model) model. To help you:

*   Supabase sends daily emails warning of any tables that are exposed to the Data API which do not have RLS enabled.
*   Supabase provides a Security Advisor and other tools in the Supabase Dashboard to fix any issues.



## Private schemas

We highly recommend creating a `private` schema for storing tables that you do not want to expose via the Data API. These tables can be accessed via Supabase Edge Functions or any other serverside tool. In this model, you should implement your security model in your serverside code. Although it's not required, we *still* recommend enabling RLS for private tables and then connecting to your database using a Postgres role with `bypassrls` privileges.



## Managing the public schema

If your `public` schema is used by other tools as a default space, you might want to lock down this schema. This helps prevent accidental exposure of data that's automatically added to `public`.

There are two levels of security hardening for the Data API:

*   Disabling the Data API entirely. This is recommended if you *never* need to access your database via Supabase client libraries or the REST and GraphQL endpoints.
*   Removing the `public` schema from the Data API and replacing it with a custom schema (such as `api`).



## Disabling the Data API

You can disable the Data API entirely if you never intend to use the Supabase client libraries or the REST and GraphQL data endpoints. For example, if you only access your database via a direct connection on the server, disabling the Data API gives you the greatest layer of protection.

1.  Go to [API Settings](/dashboard/project/_/settings/api) in the Supabase Dashboard.
2.  Under **Data API Settings**, toggle **Enable Data API** off.



## Exposing a custom schema instead of `public`

If you want to use the Data API but with increased security, you can expose a custom schema instead of `public`. By not using `public`, which is often used as a default space and has laxer default permissions, you get more conscious control over your exposed data.

Any data, views, or functions that should be exposed need to be deliberately put within your custom schema (which we will call `api`), rather than ending up there by default.


### Step 1: Remove `public` from exposed schemas

1.  Go to [**API Settings**](/dashboard/project/_/settings/api) in the Supabase Dashboard.
2.  Under **Data API Settings**, remove `public` from **Exposed schemas**. Also remove `public` from **Extra search path**.
3.  Click **Save**.
4.  Go to [**Database Extensions**](/dashboard/project/_/database/extensions) and disable the `pg_graphql` extension.


### Step 2: Create an `api` schema and expose it

1.  Connect to your database. You can use `psql`, the [Supabase SQL Editor](/dashboard/project/_/sql), or the Postgres client of your choice.

2.  Create a new schema named `api`:

    ```sql
    create schema if not exists api;
    ```

3.  Grant the `anon` and `authenticated` roles usage on this schema.

    ```sql
    grant usage on schema api to anon, authenticated;
    ```

4.  Go to [API Settings](/dashboard/project/_/settings/api) in the Supabase Dashboard.

5.  Under **Data API Settings**, add `api` to **Exposed schemas**. Make sure it is the first schema in the list, so that it will be searched first by default.

6.  Under these new settings, `anon` and `authenticated` can execute functions defined in the `api` schema, but they have no automatic permissions on any tables. On a table-by-table basis, you can grant them permissions. For example:

    ```sql
    grant select on table api.<your_table> to anon;
    grant select, insert, update, delete on table api.<your_table> to authenticated;
    ```



# Import data into Supabase



You can import data into Supabase in multiple ways. The best method depends on your data size and app requirements.

If you're working with small datasets in development, you can experiment quickly using CSV import in the Supabase dashboard. If you're working with a large dataset in production, you should plan your data import to minimize app latency and ensure data integrity.



## How to import data into Supabase

You have multiple options for importing your data into Supabase:

1.  [CSV import via the Supabase dashboard](#option-1-csv-import-via-supabase-dashboard)
2.  [Bulk import using `pgloader`](#option-2-bulk-import-using-pgloader)
3.  [Using the Postgres `COPY` command](#option-3-using-postgres-copy-command)
4.  [Using the Supabase API](#option-4-using-the-supabase-api)

<Admonition type="tip">
  If you're importing a large dataset or importing data into production, plan ahead and [prepare your database](#preparing-to-import-data).
</Admonition>


### Option 1: CSV import via Supabase dashboard

Supabase dashboard provides a user-friendly way to import data. However, for very large datasets, this method may not be the most efficient choice, given the size limit is 100MB. It's generally better suited for smaller datasets and quick data imports. Consider using alternative methods like pgloader for large-scale data imports.

1.  Navigate to the relevant table in the [Table Editor.](/dashboard/project/_/editor)
2.  Click on *+ New table* (for new, empty projects) or *Insert* (for existing tables), then choose *Import Data from CSV* and follow the on-screen instructions to upload your CSV file.


### Option 2: Bulk import using pgloader

[pgloader](https://pgloader.io/) is a powerful tool for efficiently importing data into a Postgres database that supports a wide range of source database engines, including MySQL and MS SQL.

You can use it in conjunction with Supabase by following these steps:

1.  Install pgloader on your local machine or a server. For more info, you can refer to the [official pgloader installation page](https://pgloader.readthedocs.io/en/latest/install.html).

    ```bash
    $ apt-get install pgloader
    ```

2.  Create a configuration file that specifies the source data and the target Supabase database (e.g., config.load).
    Here's an example configuration file:

    ```sql
    LOAD DATABASE
        FROM sourcedb://USER:PASSWORD@HOST/SOURCE_DB
        INTO postgres://postgres.xxxx:password@xxxx.pooler.supabase.com:6543/postgres
    ALTER SCHEMA 'public' OWNER TO 'postgres';
    set wal_buffers = '64MB', max_wal_senders = 0, statement_timeout = 0, work_mem to '2GB';
    ```

    Customize the source and Supabase database URL and options to fit your specific use case:

    *   `wal_buffers`: This parameter is set to '64MB' to allocate 64 megabytes of memory for write-ahead logging buffers. A larger value can help improve write performance by caching more data in memory before writing it to disk. This can be useful during data import operations to speed up the writing of transaction logs.
    *   `max_wal_senders`: It is set to 0, to disable replication connections. This is done during the data import process to prevent replication-related conflicts and issues.
    *   `statement_timeout`: The value is set to 0, which means it's disabled, allowing SQL statements to run without a time limit.
    *   `work_mem`: It is set to '2GB', allocating 2 GB of memory for query operations. This enhances the performance of complex queries by allowing larger in-memory datasets.

3.  Run pgloader with the configuration file.
    ```jsx
    pgloader config.load
    ```

For databases using the Postgres engine, we recommend using the [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html) and [psql](https://www.postgresql.org/docs/current/app-psql.html) command line tools.


### Option 3: Using Postgres copy command

Read more about [Bulk data loading.](/docs/guides/database/tables#bulk-data-loading)


### Option 4: Using the Supabase API

The Supabase API allows you to programmatically import data into your tables. You can use various client libraries to interact with the API and perform data import operations. This approach is useful when you need to automate data imports, and it gives you fine-grained control over the process. Refer to our [API guide](/docs/guides/api) for more details.

<Admonition type="note">
  When importing data via the Supabase API, it's advisable to refrain from bulk imports. This helps ensure a smooth data transfer process and prevents any potential disruptions.

  Read more about [Rate Limiting, Resource Allocation, & Abuse Prevention.](/docs/guides/platform/going-into-prod#rate-limiting-resource-allocation--abuse-prevention)
</Admonition>



## Preparing to import data

Large data imports can affect your database performance. Failed imports can also cause data corruption. Importing data is a safe and common operation, but you should plan ahead if you're importing a lot of data, or if you're working in a production environment.


### 1. Back up your data

Backups help you restore your data if something goes wrong. Databases on Pro, Team and Enterprise Plans are automatically backed up on schedule, but you can also take your own backup. See [Database Backups](/docs/guides/platform/backups) for more information.


### 2. Increase statement timeouts

By default, Supabase enforces query statement timeouts to ensure fair resource allocation and prevent long-running queries from affecting the overall system. When importing large datasets, you may encounter timeouts. To address this:

*   **Increase the Statement Timeout**: You can adjust the statement timeout for your session or connection to accommodate longer-running queries. Be cautious when doing this, as excessively long queries can negatively impact system performance. Read more about [Statement Timeouts](/docs/guides/database/postgres/configuration).


### 3. Estimate your required disk size

Large datasets consume disk space. Ensure your Supabase project has sufficient disk capacity to accommodate the imported data. If you know how big your database is going to be, you can manually increase the size in your [projects database settings](/dashboard/project/_/database/settings).

Read more about [disk management](/docs/guides/platform/database-size#disk-management).


### 4. Disable triggers

When importing large datasets, it's often beneficial to disable triggers temporarily. Triggers can significantly slow down the import process, especially if they involve complex logic or referential integrity checks. After the import, you can re-enable the triggers.

To disable triggers, use the following SQL commands:

```sql
-- Disable triggers on a specific table
ALTER TABLE table_name DISABLE TRIGGER ALL;

-- To re-enable triggers
ALTER TABLE table_name ENABLE TRIGGER ALL;
```


### 5. Rebuild indices after data import is complete

Indexing is crucial for query performance, but building indices while importing a large dataset can be time-consuming. Consider building or rebuilding indices after the data import is complete. This approach can significantly speed up the import process and reduce the overall time required.

To build an index after the data import:

```sql
-- Create an index on a table
create index index_name on table_name (column_name);
```

Read more about [Managing Indexes in Postgres](/docs/guides/database/postgres/indexes).



---
**Navigation:** [← Previous](./21-production-checklist.md) | [Index](./index.md) | [Next →](./23-debugging-and-monitoring.md)
