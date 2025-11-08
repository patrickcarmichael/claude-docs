**Navigation:** [← Previous](./25-event-triggers.md) | [Index](./index.md) | [Next →](./27-install.md)

# pg_stat_statements: Query Performance Monitoring



`pg_stat_statements` is a database extension that exposes a view, of the same name, to track statistics about SQL statements executed on the database. The following table shows some of the available statistics and metadata:

| Column Name       | Column Type                          | Description                                                                                                                     |
| ----------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| `userid`          | `oid` (references `pg_authid.oid`)   | OID of user who executed the statement                                                                                          |
| `dbid`            | `oid` (references `pg_database.oid`) | OID of database in which the statement was executed                                                                             |
| `toplevel`        | `bool`                               | True if the query was executed as a top-level statement (always true if pg\_stat\_statements.track is set to top)               |
| `queryid`         | `bigint`                             | Hash code to identify identical normalized queries.                                                                             |
| `query`           | `text`                               | Text of a representative statement                                                                                              |
| `plans`           | `bigint`                             | Number of times the statement was planned (if pg\_stat\_statements.track\_planning is enabled, otherwise zero)                  |
| `total_plan_time` | `double precision`                   | Total time spent planning the statement, in milliseconds (if pg\_stat\_statements.track\_planning is enabled, otherwise zero)   |
| `min_plan_time`   | `double precision`                   | Minimum time spent planning the statement, in milliseconds (if pg\_stat\_statements.track\_planning is enabled, otherwise zero) |

A full list of statistics is available in the [pg\_stat\_statements docs](https://www.postgresql.org/docs/current/pgstatstatements.html).

For more information on query optimization, check out the [query performance guide](/docs/guides/platform/performance#examining-query-performance).



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "pg\_stat\_statements" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pg_stat_statements" extension
    create extension pg_stat_statements with schema extensions;

    -- Disable the "pg_stat_statements" extension
    drop extension if exists pg_stat_statements;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>



## Inspecting activity

A common use for `pg_stat_statements` is to track down expensive or slow queries. The `pg_stat_statements` view contains a row for each executed query with statistics inlined. For example, you can leverage the statistics to identify frequently executed and slow queries against a given table.

{/* prettier-ignore */}

```sql
select
	calls,
	mean_exec_time,
	max_exec_time,
	total_exec_time,
	stddev_exec_time,
	query
from
	pg_stat_statements
where
    calls > 50                   -- at least 50 calls
    and mean_exec_time > 2.0     -- averaging at least 2ms/call
    and total_exec_time > 60000  -- at least one minute total server time spent
    and query ilike '%user_in_organization%' -- filter to queries that touch the user_in_organization table
order by
	calls desc
```

From the results, we can make an informed decision about which queries to optimize or index.



## Resources

*   Official [pg\_stat\_statements documentation](https://www.postgresql.org/docs/current/pgstatstatements.html)



# PGAudit: Postgres Auditing



[PGAudit](https://www.pgaudit.org) extends Postgres's built-in logging abilities. It can be used to selectively track activities within your database.

This helps you with:

*   **Compliance**: Meeting audit requirements for regulations
*   **Security**: Detecting suspicious database activity
*   **Troubleshooting**: Identifying and fixing database issues



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pgaudit` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Enable the "pgaudit" extension
    create extension pgaudit;

    -- Disable the "pgaudit" extension
    drop extension if exists pgaudit;
    ```
  </TabPanel>
</Tabs>



## Configure the extension

PGAudit can be configured with different levels of precision.

**PGAudit logging precision:**

*   **[Session](#session-logging):** Logs activity within a connection, such as a [psql](/docs/guides/database/connecting-to-postgres#connecting-with-psql) connection.
*   **[User](#user-logging):** Logs activity by a particular database user (for example, `anon` or `postgres`).
*   **[Global](#global-logging):** Logs activity across the entire database.
*   **[Object](#object-logging):** Logs events related to specific database objects (for example, the auth.users table).

Although Session, User, and Global modes differ in their precision, they're all considered variants of **Session Mode** and are configured with the same input categories.


### Session mode categories

These modes can monitor predefined categories of database operations:

| Category   | What it Logs                                                          | Description                                                                |
| ---------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `read`     | Data retrieval (SELECT, COPY)                                         | Tracks what data is being accessed.                                        |
| `write`    | Data modification (INSERT, DELETE, UPDATE, TRUNCATE, COPY)            | Tracks changes made to your database.                                      |
| `function` | FUNCTION, PROCEDURE, and DO/END block executions                      | Tracks routine/function executions                                         |
| `role`     | User management actions (CREATE, DROP, ALTER on users and privileges) | Tracks changes to user permissions and access.                             |
| `ddl`      | Schema changes (CREATE, DROP, ALTER statements)                       | Monitors modifications to your database structure (tables, indexes, etc.). |
| `misc`     | Less common commands (FETCH, CHECKPOINT)                              | Captures obscure actions for deeper analysis if needed.                    |
| `all`      | Everything above                                                      | Comprehensive logging for complete audit trails.                           |

Below is a limited example of how to assign PGAudit to monitor specific categories.

```sql
-- log all CREATE, ALTER, and DROP events
... pgaudit.log = 'ddl';

-- log all CREATE, ALTER, DROP, and SELECT events
... pgaudit.log = 'read, ddl';

-- log nothing
... pgaudit.log = 'none';
```


### Session logging

When you are connecting in a session environment, such as a [psql](/docs/guides/database/connecting-to-postgres#connecting-with-psql) connection, you can configure PGAudit to record events initiated within the session.

<Admonition type="note">
  The [Dashboard](/dashboard/project/_) is a transactional environment and won't sustain a session.
</Admonition>

Inside a session, by default, PGAudit will log nothing:

```sql
-- returns 'none'
show pgaudit.log;
```

In the session, you can `set` the `pgaudit.log` variable to record events:

```sql
-- log CREATE, ALTER, and DROP events
set pgaudit.log = 'ddl';

-- log all CREATE, ALTER, DROP, and SELECT events
set pgaudit.log = 'read, ddl';

-- log nothing
set pgaudit.log = 'none';
```


### User logging

There are some cases where you may want to monitor a database user's actions. For instance, let's say you connected your database to [Zapier](/partners/integrations/zapier) and created a custom role for it to use:

```sql
create user "zapier" with password '<new password>';
```

You may want to log all actions initiated by `zapier`, which can be done with the following command:

```sql
alter role "zapier" set pgaudit.log to 'all';
```

To remove the settings, execute the following code:

```sql
-- disables role's log
alter role "zapier" set pgaudit.log to 'none';

-- check to make sure the changes are finalized:
select
  rolname,
  rolconfig
from pg_roles
where rolname = 'zapier';
-- should return a rolconfig path with "pgaudit.log=none" present
```


### Global logging

<Admonition type="caution">
  Use global logging cautiously. It can generate many logs and make it difficult to find important events. Consider limiting the scope of what is logged by using session, user, or object logging where possible.
</Admonition>

The below SQL configures PGAudit to record all events associated with the `postgres` role. Since it has extensive privileges, this effectively monitors all database activity.

```sql
alter role "postgres" set pgaudit.log to 'all';
```

To check if the `postgres` role is auditing, execute the following command:

```sql
select
  rolname,
  rolconfig
from pg_roles
where rolname = 'postgres';
-- should return a rolconfig path with "pgaudit.log=all" present
```

To remove the settings, execute the following code:

```sql
alter role "postgres" set pgaudit.log to 'none';
```


### Object logging

To fine-tune what object events PGAudit will record, you must create a custom database role with limited permissions:

```sql
create role "some_audit_role" noinherit;
```

No other Postgres user can assume or login via this role. It solely exists to securely define what PGAudit will record.

Once the role is created, you can direct PGAudit to log by assigning it to the `pgaudit.role` variable:

```sql
alter role "postgres" set pgaudit.role to 'some_audit_role';
```

You can then assign the role to monitor only approved object events, such as `select` statements that include a specific table:

```sql
grant select on random_table to "some_audit_role";
```

With this privilege granted, PGAudit will record all select statements that reference the `random_table`, regardless of *who* or *what* actually initiated the event. All assignable privileges can be viewed in the [Postgres documentation](https://www.postgresql.org/docs/current/ddl-priv.html).

If you would no longer like to use object logging, you will need to unassign the `pgaudit.role` variable:

```sql
-- change pgaudit.role to no longer reference some_audit_role
alter role "postgres" set pgaudit.role to '';

-- view if pgaudit.role changed with the following command:
select
  rolname,
  rolconfig
from pg_roles
where rolname = 'postgres';
-- should return a rolconfig path with "pgaudit.role="
```



## Interpreting Audit Logs

PGAudit was designed for storing logs as CSV files with the following headers:

<Admonition type="note">
  Referenced from the [PGAudit official docs](https://github.com/pgaudit/pgaudit/blob/master/README.md#format)
</Admonition>

| header           | Description                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| AUDIT\_TYPE      | SESSION or OBJECT                                                                                                                        |
| STATEMENT\_ID    | Unique statement ID for this session. Sequential even if some statements are not logged.                                                 |
| SUBSTATEMENT\_ID | Sequential ID for each sub-statement within the main statement. Continuous even if some are not logged.                                  |
| CLASS            | ..., READ, ROLE (see pgaudit.log).                                                                                                       |
| COMMAND          | ..., ALTER TABLE, SELECT.                                                                                                                |
| OBJECT\_TYPE     | TABLE, INDEX, VIEW, etc. Available for SELECT, DML, and most DDL statements.                                                             |
| OBJECT\_NAME     | The fully qualified object name (for example, public.account). Available for SELECT, DML, and most DDL.                                  |
| STATEMENT        | Statement executed on the backend.                                                                                                       |
| PARAMETER        | If pgaudit.log\_parameter is set, this field contains the statement parameters as quoted CSV, or \<none>. Otherwise, it's \<not logged>. |

A log made from the following create statement:

```sql
create table account (
  id int primary key,
  name text,
  description text
);
```

Generates the following log in the [Dashboard's Postgres Logs](/dashboard/project/_/logs/postgres-logs):

```
 AUDIT: SESSION,1,1,DDL,CREATE TABLE,TABLE,public.account,create table account(
  id int,
  name text,
  description text
); <not logged>
```



## Finding and filtering audit logs

Logs generated by PGAudit can be found in [Postgres Logs](/dashboard/project/_/logs/postgres-logs?s=AUDIT). To find a specific log, you can use the log explorer. Below is a basic example to extract logs referencing `CREATE TABLE` events

```sql
select
  cast(t.timestamp as datetime) as timestamp,
  event_message
from
  postgres_logs as t
  cross join unnest(metadata) as m
  cross join unnest(m.parsed) as p
where event_message like 'AUDIT%CREATE TABLE%'
order by timestamp desc
limit 100;
```



## Practical examples


### Monitoring API events

<Admonition type="note">
  API requests are already recorded in the [API Edge Network](/dashboard/project/_/logs/edge-logs) logs.
</Admonition>

To monitor all writes initiated by the PostgREST API roles:

```sql
alter role "authenticator" set pgaudit.log to 'write';

-- the above is the practical equivalent to:
-- alter role "anon" set pgaudit.log TO 'write';
-- alter role "authenticated" set pgaudit.log TO 'write';
-- alter role "service_role" set pgaudit.log TO 'write';
```


### Monitoring the `auth.users` table

In the worst case scenario, where a privileged roles' password is exposed, you can use PGAudit to monitor if the `auth.users` table was targeted. It should be stated that API requests are already monitored in the [API Edge Network](/dashboard/project/_/logs/edge-logs) and this is more about providing greater clarity about what is happening at the database level.

Logging `auth.user` should be done in Object Mode and requires a custom role:

```sql
-- create logging role
create role "auth_auditor" noinherit;

-- give role permission to observe relevant table events
grant select on auth.users to "auth_auditor";
grant delete on auth.users to "auth_auditor";

-- assign auth_auditor to pgaudit.role
alter role "postgres" set pgaudit.role to 'auth_auditor';
```

With the above code, any query involving reading or deleting from the auth.users table will be logged.



## Best practices


### Disabling excess logging

PGAudit, if not configured mindfully, can log all database events, including background tasks. This can generate an undesirably large amount of logs in a few hours.

The first step to solve this problem is to identify which database users PGAudit is observing:

```sql
-- find all users monitored by pgaudit
select
  rolname,
  rolconfig
from pg_roles
where
  exists (
    select
      1
    from UNNEST(rolconfig) as c
    where c like '%pgaudit.role%' or c like '%pgaudit.log%'
  );
```

To prevent PGAudit from monitoring the problematic roles, you'll want to change their `pgaudit.log` values to `none` and `pgaudit.role` values to `empty quotes ''`

```sql
  -- Use to disable object level logging
  alter role "<role name>" set pgaudit.role to '';

  -- Use to disable global and user level logging
  alter role "<role name>" set pgaudit.log to 'none';
```



## FAQ


#### Using PGAudit to debug database functions

Technically yes, but it is not the best approach. It is better to check out our [function debugging guide](/docs/guides/database/functions#general-logging) instead.


#### Downloading database logs

In the [Logs Dashboard](/dashboard/project/_/logs/postgres-logs) you can download logs as CSVs.


#### Logging observed table rows

By default, PGAudit records queries, but not the returned rows. You can modify this behavior with the `pgaudit.log_rows` variable:

```sql
--enable
alter role "postgres" set pgaudit.log_rows to 'on';

-- disable
alter role "postgres" set pgaudit.log_rows to 'off';
```

You should not do this unless you are *absolutely* certain it is necessary for your use case. It can expose sensitive values to your logs that ideally should not be preserved. Furthermore, if done in excess, it can noticeably reduce database performance.


#### Logging function parameters

We don't currently support configuring `pgaudit.log_parameter` because it may log secrets in encrypted columns if you are using [pgsodium](/docs/guides/database/extensions/pgsodium) or[Vault](/docs/guides/database/vault).

You can upvote this [feature request](https://github.com/orgs/supabase/discussions/20183) with your use-case if you'd like this restriction lifted.


#### Does PGAudit support system wide configurations?

PGAudit allows settings to be applied to 3 different database scopes:

| Scope    | Description        | Configuration File/Command |
| -------- | ------------------ | -------------------------- |
| System   | Entire server      | ALTER SYSTEM commands      |
| Database | Specific database  | ALTER DATABASE commands    |
| Role     | Specific user/role | ALTER ROLE commands        |

Supabase limits full privileges for file system and database variables, meaning PGAudit modifications can only occur at the role level. Assigning PGAudit to the `postgres` role grants it nearly complete visibility into the database, making role-level adjustments a practical alternative to configuring at the database or system level.

PGAudit's [official documentation](https://www.pgaudit.org) focuses on system and database level configs, but its docs officially supports role level configs, too.



## Resources

*   [Official `PGAudit` documentation](https://www.pgaudit.org)
*   [Database Function Logging](/docs/guides/database/functions#general-logging)
*   [Supabase Logging](/docs/guides/platform/logs)
*   [Self-Hosting Logs](/docs/reference/self-hosting-analytics/introduction)



# pgjwt: JSON Web Tokens



{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

<Admonition type="deprecation">
  The `pgjwt` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.
</Admonition>

The [`pgjwt`](https://github.com/michelp/pgjwt) (Postgres JSON Web Token) extension allows you to create and parse [JSON Web Tokens (JWTs)](https://en.wikipedia.org/wiki/JSON_Web_Token) within a Postgres database. JWTs are commonly used for authentication and authorization in web applications and services.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pgjwt` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pgjwt" extension
    create extension pgjwt schema extensions;

    -- Disable the "pgjwt" extension
    drop extension if exists pgjwt;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>



## API

*   [`sign(payload json, secret text, algorithm text default 'HSA256')`](https://github.com/michelp/pgjwt#usage): Signs a JWT containing *payload* with *secret* using *algorithm*.
*   [`verify(token text, secret text, algorithm text default 'HSA256')`](https://github.com/michelp/pgjwt#usage): Decodes a JWT *token* that was signed with *secret* using *algorithm*.

Where:

*   `payload` is an encrypted JWT represented as a string.
*   `secret` is the private/secret passcode which is used to sign the JWT and verify its integrity.
*   `algorithm` is the method used to sign the JWT using the secret.
*   `token` is an encrypted JWT represented as a string.



## Usage

Once the extension is installed, you can use its functions to create and parse JWTs. Here's an example of how you can use the `sign` function to create a JWT:

{/* prettier-ignore */}

```sql
select
  extensions.sign(
    payload   := '{"sub":"1234567890","name":"John Doe","iat":1516239022}',
    secret    := 'secret',
    algorithm := 'HS256'
  );
```

The `pgjwt_encode` function returns a string that represents the JWT, which can then be safely transmitted between parties.

{/* prettier-ignore */}

```
              sign
---------------------------------
 eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX
 VCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiw
 ibmFtZSI6IkpvaG4gRG9lIiwiaWF0Ijo
 xNTE2MjM5MDIyfQ.XbPfbIHMI6arZ3Y9
 22BhjWgQzWXcXNrz0ogtVhfEd2o
(1 row)
```

To parse a JWT and extract its claims, you can use the `verify` function. Here's an example:

{/* prettier-ignore */}

```sql
select
  extensions.verify(
    token := 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiRm9vIn0.Q8hKjuadCEhnCPuqIj9bfLhTh_9QSxshTRsA5Aq4IuM',
    secret    := 'secret',
    algorithm := 'HS256'
  );
```

Which returns the decoded contents and some associated metadata.

{/* prettier-ignore */}

```sql
           header            |    payload     | valid
-----------------------------+----------------+-------
 {"alg":"HS256","typ":"JWT"} | {"name":"Foo"} | t
(1 row)
```



## Resources

*   Official [`pgjwt` documentation](https://github.com/michelp/pgjwt)



# pgmq: Queues



See the [Supabase Queues docs](/docs/guides/queues).



# PGroonga: Multilingual Full Text Search



`PGroonga` is a Postgres extension adding a full text search indexing method based on [Groonga](https://groonga.org). While native Postgres supports full text indexing, it is limited to alphabet and digit based languages. `PGroonga` offers a wider range of character support making it viable for a superset of languages supported by Postgres including Japanese, Chinese, etc.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pgroonga` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pgroonga" extension
    create extension pgroonga with schema extensions;

    -- Disable the "pgroonga" extension
    drop extension if exists pgroonga;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.
  </TabPanel>
</Tabs>



## Creating a full text search index

Given a table with a `text` column:

{/* prettier-ignore */}

```sql
create table memos (
  id serial primary key,
  content text
);
```

We can index the column for full text search with a `pgroonga` index:

{/* prettier-ignore */}

```sql
create index ix_memos_content ON memos USING pgroonga(content);
```

To test the full text index, we'll add some data.

{/* prettier-ignore */}

```sql
insert into memos(content)
values
  ('PostgreSQL is a relational database management system.'),
  ('Groonga is a fast full text search engine that supports all languages.'),
  ('PGroonga is a PostgreSQL extension that uses Groonga as index.'),
  ('There is groonga command.');
```

The Postgres query planner is smart enough to know that, for extremely small tables, it's faster to scan the whole table rather than loading an index. To force the index to be used, we can disable sequential scans:

{/* prettier-ignore */}

```sql
-- For testing only. Don't do this in production
set enable_seqscan = off;
```

Now if we run an explain plan on a query filtering on `memos.content`:

{/* prettier-ignore */}

```sql
explain select * from memos where content like '%engine%';

                               QUERY PLAN
-----------------------------------------------------------------------------
Index Scan using ix_memos_content on memos  (cost=0.00..1.11 rows=1 width=36)
  Index Cond: (content ~~ '%engine%'::text)
(2 rows)
```

The `pgroonga` index is used to retrieve the result set:

```markdown
| id  | content                                                                  |
| --- | ------------------------------------------------------------------------ |
| 2   | 'Groonga is a fast full text search engine that supports all languages.' |
```



## Full text search

The `&@~` operator performs full text search. It returns any matching results. Unlike `LIKE` operator, `pgroonga` can search any text that contains the keyword case insensitive.

Take the following example:

{/* prettier-ignore */}

```sql
select * from memos where content &@~ 'groonga';
```

And the result:

```markdown
id | content  
----+------------------------------------------------------------------------
2 | Groonga is a fast full text search engine that supports all languages.
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
4 | There is groonga command.
(3 rows)
```


### Match all search words

To find all memos where content contains BOTH of the words `postgres` and `pgroonga`, we can just use space to separate each words:

{/* prettier-ignore */}

```sql
select * from memos where content &@~ 'postgres pgroonga';
```

And the result:

```markdown
id | content  
----+----------------------------------------------------------------
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
(1 row)
```


### Match any search words

To find all memos where content contain ANY of the words `postgres` or `pgroonga`, use the upper case `OR`:

{/* prettier-ignore */}

```sql
select * from memos where content &@~ 'postgres OR pgroonga';
```

And the result:

```markdown
id | content  
----+----------------------------------------------------------------
1 | PostgreSQL is a relational database management system.
3 | PGroonga is a PostgreSQL extension that uses Groonga as index.
(2 rows)
```


### Search that matches words with negation

To find all memos where content contain the word `postgres` but not `pgroonga`, use `-` symbol:

{/* prettier-ignore */}

```sql
select * from memos where content &@~ 'postgres -pgroonga';
```

And the result:

```markdown
id | content  
----+--------------------------------------------------------
1 | PostgreSQL is a relational database management system.
(1 row)
```



## Resources

*   Official [PGroonga documentation](https://pgroonga.github.io/tutorial/)



# pgrouting: Geospatial Routing



[`pgRouting`](http://pgrouting.org) is Postgres and [PostGIS](http://postgis.net) extension adding geospatial routing functionality.

The core functionality of `pgRouting` is a set of path finding algorithms including:

*   All Pairs Shortest Path, Johnson’s Algorithm
*   All Pairs Shortest Path, Floyd-Warshall Algorithm
*   Shortest Path A\*
*   Bi-directional Dijkstra Shortest Path
*   Bi-directional A\* Shortest Path
*   Shortest Path Dijkstra
*   Driving Distance
*   K-Shortest Path, Multiple Alternative Paths
*   K-Dijkstra, One to Many Shortest Path
*   Traveling Sales Person
*   Turn Restriction Shortest Path (TRSP)



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pgrouting` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pgRouting" extension
    create extension pgrouting cascade;

    -- Disable the "pgRouting" extension
    drop extension if exists pgRouting;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.
  </TabPanel>
</Tabs>



## Example

As an example, we'll solve the [traveling salesperson problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) using the `pgRouting`'s `pgr_TSPeuclidean` function from some PostGIS coordinates.

A summary of the traveling salesperson problem is, given a set of city coordinates, solve for a path that goes through each city and minimizes the total distance traveled.

First we populate a table with some X, Y coordinates

{/* prettier-ignore */}

```sql
create table wi29 (
  id bigint,
  x float,
  y float,
  geom gis.geometry
);

insert into wi29 (id, x, y)
values
  (1,20833.3333,17100.0000),
  (2,20900.0000,17066.6667),
  (3,21300.0000,13016.6667),
  (4,21600.0000,14150.0000),
  (5,21600.0000,14966.6667),
  (6,21600.0000,16500.0000),
  (7,22183.3333,13133.3333),
  (8,22583.3333,14300.0000),
  (9,22683.3333,12716.6667),
  (10,23616.6667,15866.6667),
  (11,23700.0000,15933.3333),
  (12,23883.3333,14533.3333),
  (13,24166.6667,13250.0000),
  (14,25149.1667,12365.8333),
  (15,26133.3333,14500.0000),
  (16,26150.0000,10550.0000),
  (17,26283.3333,12766.6667),
  (18,26433.3333,13433.3333),
  (19,26550.0000,13850.0000),
  (20,26733.3333,11683.3333),
  (21,27026.1111,13051.9444),
  (22,27096.1111,13415.8333),
  (23,27153.6111,13203.3333),
  (24,27166.6667,9833.3333),
  (25,27233.3333,10450.0000),
  (26,27233.3333,11783.3333),
  (27,27266.6667,10383.3333),
  (28,27433.3333,12400.0000),
  (29,27462.5000,12992.2222);
```

Next we use the `pgr_TSPeuclidean` function to find the best path.

{/* prettier-ignore */}

```sql
select
    *
from
     pgr_TSPeuclidean($$select * from wi29$$)
```

{/* prettier-ignore */}

```sql
 seq | node |       cost       |     agg_cost     
-----+------+------------------+------------------
   1 |    1 |                0 |                0
   2 |    2 |  74.535614157127 |  74.535614157127
   3 |    6 | 900.617093380362 | 975.152707537489
   4 |   10 | 2113.77757765045 | 3088.93028518793
   5 |   11 | 106.718669615254 | 3195.64895480319
   6 |   12 | 1411.95293791574 | 4607.60189271893
   7 |   13 | 1314.23824873744 | 5921.84014145637
   8 |   14 | 1321.76283931305 | 7243.60298076942
   9 |   17 | 1202.91366735569 |  8446.5166481251
  10 |   18 | 683.333268292684 | 9129.84991641779
  11 |   15 | 1108.05137466134 | 10237.9012910791
  12 |   19 | 772.082339448903 |  11009.983630528
  13 |   22 | 697.666150054665 | 11707.6497805827
  14 |   23 | 220.141999627513 | 11927.7917802102
  15 |   21 | 197.926372783442 | 12125.7181529937
  16 |   29 | 440.456596290771 | 12566.1747492844
  17 |   28 | 592.939989005405 | 13159.1147382898
  18 |   26 | 648.288376333318 | 13807.4031146231
  19 |   20 | 509.901951359278 | 14317.3050659824
  20 |   25 | 1330.83095428717 | 15648.1360202696
  21 |   27 |  74.535658878487 | 15722.6716791481
  22 |   24 | 559.016994374947 |  16281.688673523
  23 |   16 | 1243.87392358622 | 17525.5625971092
  24 |    9 |  4088.0585364911 | 21613.6211336004
  25 |    7 |  650.85409697993 | 22264.4752305803
  26 |    3 | 891.004385199336 | 23155.4796157796
  27 |    4 | 1172.36699411442 |  24327.846609894
  28 |    8 | 994.708187806297 | 25322.5547977003
  29 |    5 | 1188.01888359478 | 26510.5736812951
  30 |    1 | 2266.91173136004 | 28777.4854126552
```



## Resources

*   Official [`pgRouting` documentation](https://docs.pgrouting.org/latest/en/index.html)



# pgsodium (pending deprecation): Encryption Features



Supabase DOES NOT RECOMMEND any new usage of [`pgsodium`](https://github.com/michelp/pgsodium).

The [`pgsodium`](https://github.com/michelp/pgsodium) extension is expected to go through a deprecation cycle in the near future. We will reach out to owners of impacted projects to assist with migrations away from [`pgsodium`](https://github.com/michelp/pgsodium) once the deprecation process begins.

<Admonition type="note">
  The [Vault extension](/docs/guides/database/vault) won’t be impacted. Its internal implementation will shift away from pgsodium, but the interface and API will remain unchanged.
</Admonition>

[`pgsodium`](https://github.com/michelp/pgsodium) is a Postgres extension which provides SQL access to [`libsodium`'s](https://doc.libsodium.org/) high-level cryptographic algorithms.

Supabase previously documented two features derived from pgsodium. Namely [Server Key Management](https://github.com/michelp/pgsodium#server-key-management) and [Transparent Column Encryption](https://github.com/michelp/pgsodium#transparent-column-encryption). At this time, we do not recommend using either on the Supabase platform due to their high level of operational complexity and misconfiguration risk.

Note that Supabase projects are encrypted at rest by default which likely is sufficient for your compliance needs e.g. SOC2 & HIPAA.



## Get the root encryption key for your Supabase project

Encryption requires keys. Keeping the keys in the same database as the encrypted data would be unsafe. For more information about managing the `pgsodium` root encryption key on your Supabase project see **[encryption key location](/docs/guides/database/vault#encryption-key-location)**. This key is required to decrypt values stored in [Supabase Vault](/docs/guides/database/vault) and data encrypted with Transparent Column Encryption.



## Resources

*   [Supabase Vault](/docs/guides/database/vault)
*   Read more about Supabase Vault in the [blog post](/blog/vault-now-in-beta)
*   [Supabase Vault on GitHub](https://github.com/supabase/vault)



## Resources

*   Official [`pgsodium` documentation](https://github.com/michelp/pgsodium)



# pgTAP: Unit Testing



`pgTAP` is a unit testing extension for Postgres.



## Overview

Let's cover some basic concepts:

*   Unit tests: allow you to test small parts of a system (like a database table!).
*   TAP: stands for [Test Anything Protocol](http://testanything.org/). It is an framework which aims to simplify the error reporting during testing.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pgtap` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Enable the "pgtap" extension
    create extension pgtap with schema extensions;

    -- Disable the "pgtap" extension
    drop extension if exists pgtap;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>



## Testing tables

```sql
begin;
select plan( 1 );

select has_table( 'profiles' );

select * from finish();
rollback;
```

API:

*   [`has_table()`](https://pgtap.org/documentation.html#has_table): Tests whether or not a table exists in the database
*   [`has_index()`](https://pgtap.org/documentation.html#has_index): Checks for the existence of a named index associated with the named table.
*   [`has_relation()`](https://pgtap.org/documentation.html#has_relation): Tests whether or not a relation exists in the database.



## Testing columns

```sql
begin;
select plan( 2 );

select has_column( 'profiles', 'id' ); -- test that the "id" column exists in the "profiles" table
select col_is_pk( 'profiles', 'id' ); -- test that the "id" column is a primary key

select * from finish();
rollback;
```

API:

*   [`has_column()`](https://pgtap.org/documentation.html#has_column): Tests whether or not a column exists in a given table, view, materialized view or composite type.
*   [`col_is_pk()`](https://pgtap.org/documentation.html#col_is_pk): Tests whether the specified column or columns in a table is/are the primary key for that table.



## Testing RLS policies

```sql
begin;
select plan( 1 );

select policies_are(
  'public',
  'profiles',
  ARRAY [
    'Profiles are public', -- Test that there is a policy called  "Profiles are public" on the "profiles" table.
    'Profiles can only be updated by the owner'  -- Test that there is a policy called  "Profiles can only be updated by the owner" on the "profiles" table.
  ]
);

select * from finish();
rollback;
```

API:

*   [`policies_are()`](https://pgtap.org/documentation.html#policies_are): Tests that all of the policies on the named table are only the policies that should be on that table.
*   [`policy_roles_are()`](https://pgtap.org/documentation.html#policy_roles_are): Tests whether the roles to which policy applies are only the roles that should be on that policy.
*   [`policy_cmd_is()`](https://pgtap.org/documentation.html#policy_cmd_is): Tests whether the command to which policy applies is same as command that is given in function arguments.

You can also use the `results_eq()` method to test that a Policy returns the correct data:

```sql
begin;
select plan( 1 );

select results_eq(
    'select * from profiles()',
    $$VALUES ( 1, 'Anna'), (2, 'Bruce'), (3, 'Caryn')$$,
    'profiles() should return all users'
);


select * from finish();
rollback;
```

API:

*   [`results_eq()`](https://pgtap.org/documentation.html#results_eq)
*   [`results_ne()`](https://pgtap.org/documentation.html#results_ne)



## Testing functions

```sql
prepare hello_expr as select 'hello'

begin;
select plan(3);
-- You'll need to create a hello_world and is_even function
select function_returns( 'hello_world', 'text' );                   -- test if the function "hello_world" returns text
select function_returns( 'is_even', ARRAY['integer'], 'boolean' );  -- test if the function "is_even" returns a boolean
select results_eq('select * from hello_world()', 'hello_expr');          -- test if the function "hello_world" returns "hello"

select * from finish();
rollback;
```

API:

*   [`function_returns()`](https://pgtap.org/documentation.html#function_returns): Tests that a particular function returns a particular data type
*   [`is_definer()`](https://pgtap.org/documentation.html#is_definer): Tests that a function is a security definer (that is, a `setuid` function).



## Resources

*   Official [`pgTAP` documentation](https://pgtap.org/)



# pgvector: Embeddings and vector similarity



[pgvector](https://github.com/pgvector/pgvector/) is a Postgres extension for vector similarity search. It can also be used for storing [embeddings](/blog/openai-embeddings-postgres-vector).

<Admonition type="note">
  The name of pgvector's Postgres extension is [vector](https://github.com/pgvector/pgvector/blob/258eaf58fdaff1843617ff59ea855e0768243fe9/README.md?plain=1#L64).
</Admonition>

Learn more about Supabase's [AI & Vector](/docs/guides/ai) offering.



## Concepts


### Vector similarity

Vector similarity refers to a measure of the similarity between two related items. For example, if you have a list of products, you can use vector similarity to find similar products. To do this, you need to convert each product into a "vector" of numbers, using a mathematical model. You can use a similar model for text, images, and other types of data. Once all of these vectors are stored in the database, you can use vector similarity to find similar items.


### Embeddings

This is particularly useful if you're building AI applications with large language models. You can create and store [embeddings](/docs/guides/ai/quickstarts/generate-text-embeddings) for retrieval augmented generation (RAG).



## Usage


### Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "vector" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
     -- Example: enable the "vector" extension.
    create extension vector
    with
      schema extensions;

    -- Example: disable the "vector" extension
    drop
      extension if exists vector;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.
  </TabPanel>
</Tabs>



## Usage


### Create a table to store vectors

```sql
create table posts (
  id serial primary key,
  title text not null,
  body text not null,
  embedding extensions.vector(384)
);
```


### Storing a vector / embedding

In this example we'll generate a vector using Transformer.js, then store it in the database using the Supabase client.

```js
import { pipeline } from '@xenova/transformers'
const generateEmbedding = await pipeline('feature-extraction', 'Supabase/gte-small')

const title = 'First post!'
const body = 'Hello world!'

// Generate a vector using Transformers.js
const output = await generateEmbedding(body, {
  pooling: 'mean',
  normalize: true,
})

// Extract the embedding output
const embedding = Array.from(output.data)

// Store the vector in Postgres
const { data, error } = await supabase.from('posts').insert({
  title,
  body,
  embedding,
})
```



## Specific usage cases


### Queries with filtering

If you use an IVFFlat or HNSW index and naively filter the results based on the value of another column, you may get fewer rows returned than requested.

For example, the following query may return fewer than 5 rows, even if 5 corresponding rows exist in the database. This is because the embedding index may not return 5 rows matching the filter.

```
SELECT * FROM items WHERE category_id = 123 ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

To get the exact number of requested rows, use [iterative search](https://github.com/pgvector/pgvector/?tab=readme-ov-file#iterative-index-scans) to continue scanning the index until enough results are found.



## More pgvector and Supabase resources

*   [Supabase Clippy: ChatGPT for Supabase Docs](/blog/chatgpt-supabase-docs)
*   [Storing OpenAI embeddings in Postgres with pgvector](/blog/openai-embeddings-postgres-vector)
*   [A ChatGPT Plugins Template built with Supabase Edge Runtime](/blog/building-chatgpt-plugins-template)
*   [Template for building your own custom ChatGPT style doc search](https://github.com/supabase-community/nextjs-openai-doc-search)



# plpgsql_check: PL/pgSQL Linter



[plpgsql\_check](https://github.com/okbob/plpgsql_check) is a Postgres extension that lints plpgsql for syntax, semantic and other related issues. The tool helps developers to identify and correct errors before executing the code. plpgsql\_check is most useful for developers who are working with large or complex SQL codebases, as it can help identify and resolve issues early in the development cycle.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "plpgsql\_check" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "plpgsql_check" extension
    create extension plpgsql_check;

    -- Disable the "plpgsql_check" extension
    drop extension if exists plpgsql_check;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension you can call `drop extension`.
  </TabPanel>
</Tabs>



## API

*   [`plpgsql_check_function( ... )`](https://github.com/okbob/plpgsql_check#active-mode): Scans a function for errors.

`plpgsql_check_function` is highly customizable. For a complete list of available arguments see [the docs](https://github.com/okbob/plpgsql_check#arguments)



## Usage

To demonstrate `plpgsql_check` we can create a function with a known error. In this case we create a function `some_func`, that references a non-existent column `place.created_at`.

{/* prettier-ignore */}

```sql
create table place(
  x float,
  y float
);

create or replace function public.some_func()
  returns void
  language plpgsql
as $$
declare
  rec record;
begin
  for rec in select * from place
  loop
    -- Bug: There is no column `created_at` on table `place`
    raise notice '%', rec.created_at;
  end loop;
end;
$$;
```

Note that executing the function would not catch the invalid reference error because the `loop` does not execute if no rows are present in the table.

{/* prettier-ignore */}

```sql
select public.some_func();
  some_func
 ───────────

 (1 row)
```

Now we can use plpgsql\_check's `plpgsql_check_function` function to identify the known error.

{/* prettier-ignore */}

```sql
select plpgsql_check_function('public.some_func()');

                   plpgsql_check_function
------------------------------------------------------------
 error:42703:8:RAISE:record "rec" has no field "created_at"
 Context: SQL expression "rec.created_at"
```



## Resources

*   Official [`plpgsql_check` documentation](https://github.com/okbob/plpgsql_check)



# plv8: JavaScript Language



<Admonition type="deprecation">
  The `plv8` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.
</Admonition>

The `plv8` extension allows you use JavaScript within Postgres.



## Overview

While Postgres natively runs SQL, it can also run other procedural languages.
`plv8` allows you to run JavaScript code - specifically any code that runs on the [V8 JavaScript engine](https://v8.dev).

It can be used for database functions, triggers, queries and more.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "plv8" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "plv8" extension
    create extension plv8;

    -- Example: disable the "plv8" extension
    drop extension if exists plv8;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension, call `drop extension`.

    Procedural languages are automatically installed within `pg_catalog`, so you don't need to specify a schema.
  </TabPanel>
</Tabs>



## Create `plv8` functions

Functions written in `plv8` are written just like any other Postgres functions, only
with the `language` identifier set to `plv8`.

```sql
create or replace function function_name()
returns void as $$
    // V8 JavaScript
    // code
    // here
$$ language plv8;
```

You can call `plv8` functions like any other Postgres function:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select function_name();
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = supabase.rpc('function_name')
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc("function_name")
    ```
  </TabPanel>
</Tabs>



## Examples


### Scalar functions

A [scalar function](https://plv8.github.io/#scalar-function-calls) is anything that takes in some user input and returns a single result.

```sql
create or replace function hello_world(name text)
returns text as $$

    let output = `Hello, ${name}!`;
    return output;

$$ language plv8;
```


### Executing SQL

You can execute SQL within `plv8` code using the [`plv8.execute` function](https://plv8.github.io/#plv8-execute).

```sql
create or replace function update_user(id bigint, first_name text)
returns smallint as $$

    var num_affected = plv8.execute(
        'update profiles set first_name = $1 where id = $2',
        [first_name, id]
    );

    return num_affected;
$$ language plv8;
```


### Set-returning functions

A [set-returning function](https://plv8.github.io/#set-returning-function-calls) is anything that returns a full set of results - for example, rows in a table.

```sql
create or replace function get_messages()
returns setof messages as $$

    var json_result = plv8.execute(
        'select * from messages'
    );

    return json_result;
$$ language plv8;

select * from get_messages();
```



## Resources

*   Official [`plv8` documentation](https://plv8.github.io/)
*   [plv8 GitHub Repository](https://github.com/plv8/plv8)



# PostGIS: Geo queries



[PostGIS](https://postgis.net/) is a Postgres extension that allows you to interact with Geo data within Postgres. You can sort your data by geographic location, get data within certain geographic boundaries, and do much more with it.



## Overview

While you may be able to store simple lat/long geographic coordinates as a set of decimals, it does not scale very well when you try to query through a large data set. PostGIS comes with special data types that are efficient, and indexable for high scalability.

The additional data types that PostGIS provides include [Point](https://postgis.net/docs/using_postgis_dbmanagement.html#Point), [Polygon](https://postgis.net/docs/using_postgis_dbmanagement.html#Polygon), [LineString](https://postgis.net/docs/using_postgis_dbmanagement.html#LineString), and many more to represent different types of geographical data. In this guide, we will mainly focus on how to interact with `Point` type, which represents a single set of latitude and longitude. If you are interested in digging deeper, you can learn more about different data types on the [data management section of PostGIS docs](https://postgis.net/docs/using_postgis_dbmanagement.html).



## Enable the extension

You can get started with PostGIS by enabling the PostGIS extension in your Supabase dashboard.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `postgis` and enable the extension.
    4.  In the confirmation prompt select "Create a new schema" and name it `gis` for example.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "postgis" extension
    create extension postgis with schema "extensions";

    -- Example: disable the "postgis" extension
    drop extension if exists postgis;
    ```
  </TabPanel>
</Tabs>



## Examples

Now that we are ready to get started with PostGIS, let’s create a table and see how we can utilize PostGIS for some typical use cases. Let’s imagine we are creating a simple restaurant-searching app.

Let’s create our table. Each row represents a restaurant with its location stored in `location` column as a `Point` type.

```sql
create table if not exists public.restaurants (
	id int generated by default as identity primary key,
	name text not null,
	location extensions.geography(POINT) not null
);
```

We can then set a [spatial index](https://postgis.net/docs/using_postgis_dbmanagement.html#build-indexes) on the `location` column of this table.

```sql
create index restaurants_geo_index
  on public.restaurants
  using GIST (location);
```


### Inserting data

You can insert geographical data through SQL or through our API.

<Tabs scrollable size="small" type="underlined" defaultActiveId="data" queryGroup="language">
  <TabPanel id="data" label="Data">
    <h4>Restaurants</h4>

    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | name        | location                         |
    | -- | ----------- | -------------------------------- |
    | 1  | Supa Burger | lat: 40.807416, long: -73.946823 |
    | 2  | Supa Pizza  | lat: 40.807475, long: -73.94581  |
    | 3  | Supa Taco   | lat: 40.80629, long: -73.945826  |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    insert into public.restaurants
      (name, location)
    values
      ('Supa Burger', extensions.st_point(-73.946823, 40.807416)),
      ('Supa Pizza', extensions.st_point(-73.94581, 40.807475)),
      ('Supa Taco', extensions.st_point(-73.945826, 40.80629));
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { error } = await supabase.from('restaurants').insert([
      {
        name: 'Supa Burger',
        location: 'POINT(-73.946823 40.807416)',
      },
      {
        name: 'Supa Pizza',
        location: 'POINT(-73.94581 40.807475)',
      },
      {
        name: 'Supa Taco',
        location: 'POINT(-73.945826 40.80629)',
      },
    ])
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase.from('restaurants').insert([
      {
        'name': 'Supa Burger',
        'location': 'POINT(-73.946823 40.807416)',
      },
      {
        'name': 'Supa Pizza',
        'location': 'POINT(-73.94581 40.807475)',
      },
      {
        'name': 'Supa Taco',
        'location': 'POINT(-73.945826 40.80629)',
      },
    ]);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct Restaurant: Codable {
        let name: String
        let location: String // You could also use a custom type with a custom `Encodable` conformance for convenience.
    }

    try await supabase.from("restaurants")
      .insert(
        [
          Restaurant(name: "Supa Burger", location: "POINT(-73.946823 40.807416)"),
          Restaurant(name: "Supa Pizza", location: "POINT(-73.94581 40.807475)"),
          Restaurant(name: "Supa Taco", location: "POINT(-73.945826 40.80629)"),
        ]
      )
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    @Serializable
    data class Restaurant(
        val name: String,
        val location: String //you could also use a custom type with a custom serializer for more type safety
    )
    ```

    ```kotlin
    val data = supabase.from("restaurants").insert(listOf(
        Restaurant("Supa Burger", "POINT(-73.946823 40.807416)"),
        Restaurant("Supa Pizza", "POINT(-73.94581 40.807475)"),
        Restaurant("Supa Taco", "POINT(-73.945826 40.80629)"),
    ))
    ```
  </TabPanel>
</Tabs>

Notice the order in which you pass the latitude and longitude. Longitude comes first, and is because longitude represents the x-axis of the location. Another thing to watch for is when inserting data from the client library, there is no comma between the two values, just a single space.

At this point, if you go into your Supabase dashboard and look at the data, you will notice that the value of the `location` column looks something like this.

```
0101000020E6100000A4DFBE0E9C91614044FAEDEBC0494240
```

We can query the `restaurants` table directly, but it will return the `location` column in the format you see above.
We will create [database functions](/docs/guides/database/functions) so that we can use the [st\_y()](https://postgis.net/docs/ST_Y.html) and [st\_x()](https://postgis.net/docs/ST_X.html) function to convert it back to lat and long floating values.


### Order by distance

Sorting datasets from closest to farthest, sometimes called nearest-neighbor sort, is a very common use case in Geo-queries. PostGIS can handle it with the use of the [`<->`](https://postgis.net/docs/geometry_distance_knn.html) operator. `<->` operator returns the two-dimensional distance between two geometries and will utilize the spatial index when used within `order by` clause. You can create the following database function to sort the restaurants from closest to farthest by passing the current locations as parameters.

```sql
create or replace function nearby_restaurants(lat float, long float)
returns table (id public.restaurants.id%TYPE, name public.restaurants.name%TYPE, lat float, long float, dist_meters float)
set search_path = ''
language sql
as $$
  select id, name, extensions.st_y(location::extensions.geometry) as lat, extensions.st_x(location::extensions.geometry) as long, extensions.st_distance(location, extensions.st_point(long, lat)::extensions.geography) as dist_meters
  from public.restaurants
  order by location operator(extensions.<->) extensions.st_point(long, lat)::extensions.geography;
$$;
```

Now you can call this function from your client using `rpc()` like this:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('nearby_restaurants', {
      lat: 40.807313,
      long: -73.946713,
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.rpc('nearby_restaurants',params: {
      'lat': 40.807313,
      'long': -73.946713,
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct Response: Codable {
      let id: Int
      let name: String
      let lat: Double
      let long: Double
      let distance: Double

      enum CodingKeys: String, CodingKey {
        case id, name, lat, long
        case distance = "dist_meters"
      }
    }

    let response: Response = try await supabase.rpc(
      "nearby_restaurants",
      params: [
        "lat": 40.807313,
        "long": -73.946713
      ]
    )
    .execute()
    .value
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc(
        function = "nearby_restaurants",
        parameters = buildJsonObject { //You can put here any serializable object including your own classes
            put("lat", 40.807313)
            put("lon", -73.946713)
        }
    )
    ```
  </TabPanel>

  <TabPanel id="result" label="Result">
    ```json
    [
      {
        "id": 1,
        "name": "Supa Burger",
        "lat": 40.807416,
        "long": -73.946823,
        "dist_meters": 14.73033739
      },
      {
        "id": 2,
        "name": "Supa Pizza",
        "lat": 40.807475,
        "long": -73.94581,
        "dist_meters": 78.28980007
      },
      {
        "id": 3,
        "name": "Supa Taco",
        "lat": 40.80629,
        "long": -73.945826,
        "dist_meters": 136.04329002
      }
    ]
    ```
  </TabPanel>
</Tabs>


### Finding all data points within a bounding box

![Searching within a bounding box of a map](/docs/img/guides/database/extensions/postgis/map.png)

When you are working on a map-based application where the user scrolls through your map, you might want to load the data that lies within the bounding box of the map every time your users scroll. PostGIS can return the rows that are within the bounding box just by supplying the bottom left and the top right coordinates. Let’s look at what the function would look like:

```sql
create or replace function restaurants_in_view(min_lat float, min_long float, max_lat float, max_long float)
returns table (id public.restaurants.id%TYPE, name public.restaurants.name%TYPE, lat float, long float)
set search_path to ''
language sql
as $$
	select id, name, extensions.st_y(location::extensions.geometry) as lat, extensions.st_x(location::extensions.geometry) as long
	from public.restaurants
	where location operator(extensions.&&) extensions.ST_SetSRID(extensions.ST_MakeBox2D(extensions.ST_Point(min_long, min_lat), extensions.ST_Point(max_long, max_lat)), 4326)
$$;
```

The [`&&`](https://postgis.net/docs/geometry_overlaps.html) operator used in the `where` statement here returns a boolean of whether the bounding box of the two geometries intersect or not. We are basically creating a bounding box from the two points and finding those points that fall under the bounding box. We are also utilizing a few different PostGIS functions:

*   [ST\_MakeBox2D](https://postgis.net/docs/ST_MakeBox2D.html): Creates a 2-dimensional box from two points.
*   [ST\_SetSRID](https://postgis.net/docs/ST_SetSRID.html): Sets the [SRID](https://postgis.net/docs/manual-dev/using_postgis_dbmanagement.html#spatial_ref_sys), which is an identifier of what coordinate system to use for the geometry. 4326 is the standard longitude and latitude coordinate system.

You can call this function from your client using `rpc()` like this:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.rpc('restaurants_in_view', {
      min_lat: 40.807,
      min_long: -73.946,
      max_lat: 40.808,
      max_long: -73.945,
    })
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.rpc('restaurants_in_view', params: {
      'min_lat': 40.807,
      'min_long': -73.946,
      'max_lat': 40.808,
      'max_long': -73.945,
    });
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct Response: Codable {
      let id: Int
      let name: String
      let lat: Double
      let long: Double
    }

    let response: Response = try await supabase.rpc(
      "restaurants_in_view",
      params: [
        "min_lat": 40.807,
        "min_long": -73.946,
        "max_long": -73.945,
        "max_lat": 40.808,
      ]
    )
    .execute()
    .value
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.postgrest.rpc(
        function = "restaurants_in_view",
        parameters = buildJsonObject { //You can put here any serializable object including your own classes
            put("min_lat", 40.807)
            put("min_lon", -73.946)
            put("max_lat", 40.808)
            put("max_lon", -73.945)
        }
    )
    ```
  </TabPanel>

  <TabPanel id="result" label="Result">
    ```json
    [
      {
        "id": 2,
        "name": "Supa Pizza",
        "lat": 40.807475,
        "long": -73.94581
      }
    ]
    ```
  </TabPanel>
</Tabs>



## Troubleshooting

As of PostGIS 2.3 or newer, the PostGIS extension is no longer relocatable from one schema to another. If you need to move it from one schema to another for any reason (e.g. from the public schema to the extensions schema for security reasons), you would normally run a ALTER EXTENSION to relocate the schema. However, you will now to do the following steps:

1.  Backup your Database to prevent data loss - You can do this through the [CLI](/docs/reference/cli/supabase-db-dump) or Postgres backup tools such as [pg\_dumpall](https://www.postgresql.org/docs/current/backup-dump.html#BACKUP-DUMP-ALL)

2.  Drop all dependencies you created and the PostGIS extension - `DROP EXTENSION postgis CASCADE;`

3.  Enable PostGIS extension in the new schema - `CREATE EXTENSION postgis SCHEMA extensions;`

4.  Restore dropped data via the Backup if necessary from step 1 with your tool of choice.

Alternatively, you can contact the [Supabase Support Team](/dashboard/support/new) and ask them to run the following SQL on your instance:

```sql
BEGIN;
	UPDATE pg_extension
	  SET extrelocatable = true
	WHERE extname = 'postgis';

	ALTER EXTENSION postgis
	  SET SCHEMA extensions;

	ALTER EXTENSION postgis
	  UPDATE TO "<POSTGIS_VERSION>next";

	ALTER EXTENSION postgis UPDATE;

	UPDATE pg_extension
	  SET extrelocatable = false
	WHERE extname = 'postgis';
COMMIT;
```



## Resources

*   [Official PostGIS documentation](https://postgis.net/documentation/)



# postgres_fdw



The extension enables Postgres to query tables and views on a remote Postgres server.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "postgres\_fdw" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "postgres_fdw" extension
    create extension if not exists postgres_fdw;

    -- Example: disable the "postgres_fdw" extension
    drop extension if exists postgres_fdw;
    ```

    Procedural languages are automatically installed within `pg_catalog`, so you don't need to specify a schema.
  </TabPanel>
</Tabs>



## Create a connection to another database

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a foreign server">
      Define the remote database address
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
          create server "<foreign_server_name>"
          foreign data wrapper postgres_fdw
          options (
              host '<host>',
              port '<port>',
              dbname '<dbname>'
          );
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a server mapping">
      Set the user credentials for the remote server
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      create user mapping for "<dbname>"
      server "<foreign_server_name>"
      options (
          user '<db_user>',
          password '<password>'
      );
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Import tables">
      Import tables from the foreign database
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Example: Import all tables from a schema

      ```sql
      import foreign schema "<foreign_schema>"
      from server "<foreign_server>"
      into "<host_schema>";
      ```

      Example: Import specific tables

      ```sql
      import foreign schema "<foreign_schema>"
      limit to (
          "<table_name1>",
          "<table_name2>"
      )
      from server "<foreign_server>"
      into "<host_schema>";
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Query foreign table" />

    <StepHikeCompact.Code>
      ```sql
      select * from "<foreign_table>"
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>


### Configuring execution options


#### Fetch\_size

Maximum rows fetched per operation. For example, fetching 200 rows with `fetch_size` set to 100 requires 2 requests.

```sql
alter server "<foreign_server_name>"
options (fetch_size '10000');
```


#### Batch\_size

Maximum rows inserted per cycle. For example, inserting 200 rows with `batch_size` set to 100 requires 2 requests.

```sql
alter server "<foreign_server_name>"
options (batch_size '1000');
```


#### Extensions

Lists shared extensions. Without them, queries involving unlisted extension functions or operators may fail or omit references.

```sql
alter server "<foreign_server_name>"
options (extensions 'vector, postgis');
```

For more server options, check the extension's [official documentation](https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW)



## Resources

*   Official [`postgres_fdw` documentation](https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW)



# RUM: improved inverted index for full-text search based on GIN index



[RUM](https://github.com/postgrespro/rum) is an extension which adds a RUM index to Postgres.

RUM index is based on GIN that stores additional per-entry information in a posting tree. For example, positional information of lexemes or timestamps. In comparison to GIN it can use this information to make faster index-only scans for:

*   Phrase search
*   Text search with ranking by text distance operator
*   Text `SELECT`s with ordering by some non-indexed additional column e.g. by timestamp.

RUM works best in scenarios when the possible keys are highly repeatable. I.e. all texts are composed of a
limited amount of words, so per-lexeme indexing gives significant speed-up in searching texts containing word
combinations or phrases.

Main operators for ordering are:

`tsvector` `<=>` `tsquery` | `float4` | Distance between `tsvector` and `tsquery`.
value `<=>` value | `float8` | Distance between two values.

Where value is `timestamp`, `timestamptz`, `int2`, `int4`, `int8`, `float4`, `float8`, `money` and `oid`



## Usage


### Enable the extension

You can get started with rum by enabling the extension in your Supabase dashboard.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "rum" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "rum" extension
    create extension rum with schema extensions;

    -- Example: disable the "rum" extension
    drop extension if exists rum;
    ```
  </TabPanel>
</Tabs>


### Syntax


#### For type: `tsvector`

To understand the following you may need first to see [Official Postgres documentation on text
search](https://www.postgresql.org/docs/current/functions-textsearch.html)

`rum_tsvector_ops`

```sql
CREATE TABLE test_rum(t text, a tsvector);

CREATE TRIGGER tsvectorupdate
BEFORE UPDATE OR INSERT ON test_rum
FOR EACH ROW EXECUTE PROCEDURE tsvector_update_trigger('a', 'pg_catalog.english', 't');

INSERT INTO test_rum(t) VALUES ('The situation is most beautiful');
INSERT INTO test_rum(t) VALUES ('It is a beautiful');
INSERT INTO test_rum(t) VALUES ('It looks like a beautiful place');

CREATE INDEX rumidx ON test_rum USING rum (a rum_tsvector_ops);
```

And we can execute `tsvector` selects with ordering by text distance operator:

```sql
SELECT t, a `<=>` to_tsquery('english', 'beautiful | place') AS rank
    FROM test_rum
    WHERE a @@ to_tsquery('english', 'beautiful | place')
    ORDER BY a `<=>` to_tsquery('english', 'beautiful | place');
                t                |  rank
---------------------------------+---------
 It looks like a beautiful place | 8.22467
 The situation is most beautiful | 16.4493
 It is a beautiful               | 16.4493
(3 rows)
```

`rum_tsvector_addon_ops`

```sql
CREATE TABLE tsts (id int, t tsvector, d timestamp);
CREATE INDEX tsts_idx ON tsts USING rum (t rum_tsvector_addon_ops, d)
    WITH (attach = 'd', to = 't');
```

Now we can execute the selects with ordering distance operator on attached column:

```sql
SELECT id, d, d `<=>` '2016-05-16 14:21:25' FROM tsts WHERE t @@ 'wr&qh' ORDER BY d `<=>` '2016-05-16 14:21:25' LIMIT 5;
 id  |                d                |   ?column?
-----+---------------------------------+---------------
 355 | Mon May 16 14:21:22.326724 2016 |      2.673276
 354 | Mon May 16 13:21:22.326724 2016 |   3602.673276
 371 | Tue May 17 06:21:22.326724 2016 |  57597.326724
 406 | Wed May 18 17:21:22.326724 2016 | 183597.326724
 415 | Thu May 19 02:21:22.326724 2016 | 215997.326724
(5 rows)
```


#### For type: `anyarray`

`rum_anyarray_ops`

This operator class stores `anyarray` elements with length of the array. It supports operators `&&`, `@>`, `<@`, `=`, `%` operators. It also supports ordering by `<=>` operator.

```sql
CREATE TABLE test_array (i int2[]);
INSERT INTO test_array VALUES ('{}'), ('{0}'), ('{1,2,3,4}'), ('{1,2,3}'), ('{1,2}'), ('{1}');
CREATE INDEX idx_array ON test_array USING rum (i rum_anyarray_ops);
```

Now we can execute the query using index scan:

```sql
SELECT * FROM test_array WHERE i && '{1}' ORDER BY i `<=>` '{1}' ASC;
     i
-----------
 {1}
 {1,2}
 {1,2,3}
 {1,2,3,4}
(4 rows)
```

`rum_anyarray_addon_ops`

The does the same with `anyarray` index as `rum_tsvector_addon_ops` i.e. allows to order select results using distance
operator by attached column.



## Limitations

`RUM` has slower build and insert times than `GIN` due to:

1.  It is bigger due to the additional attributes stored in the index.
2.  It uses generic WAL records.



## Resources

*   [Official RUM documentation](https://github.com/postgrespro/rum)



# timescaledb: Time-Series data



<Admonition type="deprecation">
  The `timescaledb` extension is deprecated in projects using Postgres 17. It continues to be supported in projects using Postgres 15, but will need to dropped before those projects are upgraded to Postgres 17. See the [Upgrading to Postgres 17 notes](/docs/guides/platform/upgrading#upgrading-to-postgres-17) for more information.
</Admonition>

[`timescaledb`](https://docs.timescale.com/timescaledb/latest/) is a Postgres extension designed for improved handling of time-series data. It provides a scalable, high-performance solution for storing and querying time-series data on top of a standard Postgres database.

`timescaledb` uses a time-series-aware storage model and indexing techniques to improve performance of Postgres in working with time-series data. The extension divides data into chunks based on time intervals, allowing it to scale efficiently, especially for large data sets. The data is then compressed, optimized for write-heavy workloads, and partitioned for parallel processing. `timescaledb` also includes a set of functions, operators, and indexes that work with time-series data to reduce query times, and make data easier to work with.

<Admonition type="note">
  Supabase projects come with [TimescaleDB Apache 2 Edition](https://docs.timescale.com/about/latest/timescaledb-editions/#timescaledb-apache-2-edition). Functionality only available under the Community Edition is not available.
</Admonition>



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `timescaledb` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "timescaledb" extension
    create extension timescaledb with schema extensions;

    -- Disable the "timescaledb" extension
    drop extension if exists timescaledb;
    ```
  </TabPanel>
</Tabs>

Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension". To disable an extension you can call `drop extension`.

It's good practice to create the extension within a separate schema (like `extensions`) to keep your `public` schema clean.



## Usage

To demonstrate how `timescaledb` works, let's consider a simple example where we have a table that stores temperature data from different sensors. We will create a table named "temperatures" and store data for two sensors.

First we create a hypertable, which is a virtual table that is partitioned into chunks based on time intervals. The hypertable acts as a proxy for the actual table and makes it easy to query and manage time-series data.

{/* prettier-ignore */}

```sql
create table temperatures (
  time timestamptz not null,
  sensor_id int not null,
  temperature double precision not null
);

select create_hypertable('temperatures', 'time');
```

Next, we can populate some values

{/* prettier-ignore */}

```sql
insert into temperatures (time, sensor_id, temperature)
values
    ('2023-02-14 09:00:00', 1, 23.5),
    ('2023-02-14 09:00:00', 2, 21.2),
    ('2023-02-14 09:05:00', 1, 24.5),
    ('2023-02-14 09:05:00', 2, 22.3),
    ('2023-02-14 09:10:00', 1, 25.1),
    ('2023-02-14 09:10:00', 2, 23.9),
    ('2023-02-14 09:15:00', 1, 24.9),
    ('2023-02-14 09:15:00', 2, 22.7),
    ('2023-02-14 09:20:00', 1, 24.7),
    ('2023-02-14 09:20:00', 2, 23.5);
```

And finally we can query the table using `timescaledb`'s `time_bucket` function to divide the time-series into intervals of the specified size (in this case, 1 hour) averaging the `temperature` reading within each group.

{/* prettier-ignore */}

```sql
select
    time_bucket('1 hour', time) AS hour,
    avg(temperature) AS average_temperature
from
    temperatures
where
    sensor_id = 1
    and time > NOW() - interval '1 hour'
group by
    hour;
```



## Resources

*   Official [`timescaledb` documentation](https://docs.timescale.com/timescaledb/latest/)



# uuid-ossp: Unique Identifiers



The `uuid-ossp` extension can be used to generate a `UUID`.



## Overview

A `UUID` is a "Universally Unique Identifier" and it is, for practical purposes, unique.
This makes them particularly well suited as Primary Keys. It is occasionally referred to as a `GUID`, which stands for "Globally Unique Identifier".



## Enable the extension

**Note**:
Currently `uuid-ossp` extension is enabled by default and cannot be disabled.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `uuid-ossp` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "uuid-ossp" extension
    create extension "uuid-ossp" with schema extensions;

    -- Example: disable the "uuid-ossp" extension
    drop extension if exists "uuid-ossp";
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.

    **Note**:
    Currently `uuid-ossp` extension is enabled by default and cannot be disabled.
  </TabPanel>
</Tabs>



## The `uuid` type

Once the extension is enabled, you now have access to a `uuid` type.



## `uuid_generate_v1()`

Creates a UUID value based on the combination of computer’s MAC address, current timestamp, and a random value.

<Admonition type="note">
  UUIDv1 leaks identifiable details, which might make it unsuitable for certain security-sensitive applications.
</Admonition>



## `uuid_generate_v4()`

Creates UUID values based solely on random numbers. You can also use Postgres's built-in [`gen_random_uuid()`](https://www.postgresql.org/docs/current/functions-uuid.html) function to generate a UUIDv4.



## Examples


### Within a query

```sql
select uuid_generate_v4();
```


### As a primary key

Automatically create a unique, random ID in a table:

```sql
create table contacts (
  id uuid default uuid_generate_v4(),
  first_name text,
  last_name text,
  primary key (id)
);
```



## Resources

*   [Choosing a Postgres Primary Key](/blog/choosing-a-postgres-primary-key)
*   [The Basics Of Postgres `UUID` Data Type](https://www.postgresqltutorial.com/postgresql-uuid/)



# Foreign Data Wrappers

Connecting to external systems using Postgres Foreign Data Wrappers.

Foreign Data Wrappers (FDW) are a core feature of Postgres that allow you to access and query data stored in external data sources as if they were native Postgres tables.

Postgres includes several built-in foreign data wrappers, such as [`postgres_fdw`](https://www.postgresql.org/docs/current/postgres-fdw.html) for accessing other Postgres databases, and [`file_fdw`](https://www.postgresql.org/docs/current/file-fdw.html) for reading data from files. Supabase extends this feature to query other databases or any other external systems. We do this with our open source [Wrappers](https://github.com/supabase/wrappers) framework. In these guides we'll refer to them as "Wrappers", Foreign Data Wrappers, or FDWs. They are conceptually the same thing.



## Concepts

Wrappers introduce some new terminology and different workflows.

<Image
  alt="Foreign Data Wrappers (FDW)"
  zoomable
  src={{
    dark: '/docs/img/database/foreign-data-wrappers/extracting-data.png',
    light: '/docs/img/database/foreign-data-wrappers/extracting-data--light.png',
  }}
/>


### Remote servers

A Remote Server is an external database, API, or any system containing data that you want to query from your Postgres database. Examples include:

*   An external database, like Postgres or Firebase.
*   A remote data warehouse, like ClickHouse, BigQuery, or Snowflake.
*   An API, like Stripe or GitHub.

It's possible to connect to multiple remote servers of the same type. For example, you can connect to two different Firebase projects within the same Supabase database.


### Foreign tables

A table in your database which maps to some data inside a Remote Server.

Examples:

*   An `analytics` table which maps to a table inside your data warehouse.
*   A `subscriptions` table which maps to your Stripe subscriptions.
*   A `collections` table which maps to a Firebase collection.

Although a foreign table behaves like any other table, the data is not stored inside your database. The data remains inside the Remote Server.


### ETL with Wrappers

ETL stands for Extract, Transform, Load. It's an established process for moving data from one system to another. For example, it's common to move data from a production database to a data warehouse.

There are many popular ETL tools, such as [Fivetran](https://fivetran.com/) and [Airbyte](https://airbyte.io/).

Wrappers provide an alternative to these tools. You can use SQL to move data from one table to another:

```sql
-- Copy data from your production database to your
-- data warehouse for the last 24 hours:

insert into warehouse.analytics
select * from public.analytics
where ts > (now() - interval '1 DAY');
```

This approach provides several benefits:

1.  **Simplicity:** the Wrappers API is just SQL, so data engineers don't need to learn new tools and languages.
2.  **Save on time:** avoid setting up additional data pipelines.
3.  **Save on Data Engineering costs:** less infrastructure to be managed.

One disadvantage is that Wrappers are not as feature-rich as ETL tools. They also couple the ETL process to your database.


### On-demand ETL with Wrappers

Supabase extends the ETL concept with real-time data access. Instead of moving gigabytes of data from one system to another before you can query it, you can instead query the data directly from the remote server. This additional option, "Query", extends the ETL process and is called [QETL](https://www.sciencedirect.com/science/article/abs/pii/S0169023X1730438X) (pronounced "kettle"): Query, Extract, Transform, Load.

{/* prettier-ignore */}

```sql
-- Get all purchases for a user from your data warehouse:
select
  auth.users.id as user_id,
  warehouse.orders.id as order_id
from
  warehouse.orders
join 
  auth.users on auth.users.id = warehouse.orders.user_id
where 
  auth.users.id = '<some_user_id>';
```

This approach has several benefits:

1.  **On-demand:** analytical data is immediately available within your application with no additional infrastructure.
2.  **Always in sync:** since the data is queried directly from the remote server, it's always up-to-date.
3.  **Integrated:** large datasets are available within your application, and can be joined with your operational/transactional data.
4.  **Save on egress:** only extract/load what you need.


### Batch ETL with Wrappers

A common use case for Wrappers is to extract data from a production database and load it into a data warehouse. This can be done within your database using [pg\_cron](/docs/guides/database/extensions/pg_cron). For example, you can schedule a job to run every night to extract data from your production database and load it into your data warehouse.

```sql
-- Every day at 3am, copy data from your
-- production database to your data warehouse:
select cron.schedule(
  'nightly-etl',
  '0 3 * * *',
  $$
    insert into warehouse.analytics
    select * from public.analytics
    where ts > (now() - interval '1 DAY');
  $$
);
```

<Image
  alt="FDW with pg_cron"
  zoomable
  src={{
    dark: '/docs/img/database/foreign-data-wrappers/extracting-data-pgcron.png',
    light: '/docs/img/database/foreign-data-wrappers/extracting-data-pgcron--light.png',
  }}
/>

This process can be taxing on your database if you are moving large amounts of data. Often, it's better to use an external tool for batch ETL, such as [Fivetran](https://fivetran.com/) or [Airbyte](https://airbyte.io/).


### WebAssembly Wrappers

WebAssembly (Wasm) is a binary instruction format that enables high-performance execution of code on the web. Wrappers now includes a Wasm runtime, which provides a sandboxed execution environment, to run Wasm foreign data wrappers. Combined Wrappers with Wasm, developing and distributing new FDW becomes much easier and you can even build your own Wasm FDW and use it on Supabase platform.

To learn more about Wasm FDW, visit [Wrappers official documentation](https://supabase.github.io/wrappers/).



## Security

Foreign Data Wrappers do not provide Row Level Security, thus it is not advised to expose them via your API. Wrappers should *always* be stored in a private schema. For example, if you are connecting to your Stripe account, you should create a `stripe` schema to store all of your foreign tables inside. This schema should *not* be added to the “Additional Schemas” setting in the API section.

If you want to expose any of the foreign table columns to your public API, you can create a [Database Function with security definer](/docs/guides/database/functions#security-definer-vs-invoker) in the `public` schema, and then you can interact with your foreign table through API. For better access control, the function should have appropriate filters on the foreign table to apply security rules based on your business needs.

As an example, go to [SQL Editor](/dashboard/project/_/sql/new) and then follow below steps,

1.  Create a Stripe Products foreign table:

    ```sql
    create foreign table stripe.stripe_products (
      id text,
      name text,
      active bool,
      default_price text,
      description text,
      created timestamp,
      updated timestamp,
      attrs jsonb
    )
      server stripe_fdw_server
      options (
        object 'products',
        rowid_column 'id'
      );
    ```

2.  Create a security definer function that queries the foreign table and filters on the name prefix parameter:

    ```sql
    create function public.get_stripe_products(name_prefix text)
    returns table (
      id text,
      name text,
      active boolean,
      default_price text,
      description text
    )
    language plpgsql
    security definer set search_path = ''
    as $$
    begin
      return query
      select
        t.id,
        t.name,
        t.active,
        t.default_price,
        t.description
      from
        stripe.stripe_products t
      where
        t.name like name_prefix || '%'
      ;
    end;
    $$;
    ```

3.  Restrict the function execution to a specific role only, for example, the authenticated users:

    <Admonition type="danger">
      By default, the function created can be executed by any roles like `anon`, that means the
      foreign table is public accessible. Always limit the function execution permission to
      appropriate roles.
    </Admonition>

    ```sql
    -- revoke public execute permission
    revoke execute on function public.get_stripe_products from public;
    revoke execute on function public.get_stripe_products from anon;

    -- grant execute permission to a specific role only
    grant execute on function public.get_stripe_products to authenticated;
    ```

Once the preceding steps are finished, the function can be invoked from Supabase client to query the foreign table:

```js
const { data, error } = await supabase
  .rpc('get_stripe_products', { name_prefix: 'Test' })
  .select('*')
if (error) console.error(error)
else console.log(data)
```



## Resources

*   Official [`supabase/wrappers` documentation](https://supabase.github.io/wrappers/)



# Serverless Drivers

Connecting to your Postgres database in serverless environments.

Supabase provides several options for connecting to your Postgres database from serverless environments.

[supabase-js](/docs/reference/javascript/introduction) is an isomorphic JavaScript client that uses the [auto-generated REST API](/docs/guides/api) and therefore works in any environment that supports HTTPS connections. This API has a built-in [connection pooler](/docs/guides/database/connecting-to-postgres#connection-pooler) and can serve thousands of simultaneous requests, and therefore is ideal for Serverless workloads.



## Vercel Edge Functions

Vercel's [Edge runtime](https://vercel.com/docs/functions/runtimes/edge-runtime) is built on top of the [V8 engine](https://v8.dev/), that provides a limited set of Web Standard APIs.


### Quickstart

Choose one of these Vercel Deploy Templates which use our [Vercel Deploy Integration](https://vercel.com/integrations/supabase) to automatically configure your connection strings as environment variables on your Vercel project!

<div>
  <div className="grid grid-cols-12 gap-6 not-prose">
    {[
              {
                title: 'supabase-js',
                hasLightIcon: true,
                href: 'https://supabase.link/nextjs-with-supabase-starter',
                description: 'A Next.js App Router template configured with cookie-based auth using Supabase, TypeScript and Tailwind CSS.'
              },
              /* { TODO: Link the correct next.js template that uses drizzle ORM with supabase database.
                hasLightIcon: true,
                href: 'https://supabase.link/nextjs-supabase-drizzle',
                description: "Simple Next.js template that uses Supabase as the database and Drizzle as the ORM.",
              },*/
              {
                title: 'Kysely',
                hasLightIcon: true,
                href: 'https://supabase.link/nextjs-supabase-kysely',
                description: 'Simple Next.js template that uses Supabase as the database and Kysely as the query builder.',
              },
              /* { TODO: figure out how to get around Prisma accelerate requirement...
                title: 'Prisma',
                hasLightIcon: true,
                href: 'https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fstorage%2Fpostgres-prisma&project-name=postgres-prisma&repository-name=postgres-prisma&demo-title=Vercel%20Postgres%20%2B%20Prisma%20Next.js%20Starter&demo-description=Simple%20Next.js%20template%20that%20uses%20Vercel%20Postgres%20as%20the%20database%20and%20Prisma%20as%20the%20ORM.&demo-url=https%3A%2F%2Fpostgres-prisma.vercel.app%2F&demo-image=https%3A%2F%2Fpostgres-prisma.vercel.app%2Fopengraph-image.png&integration-ids=oac_VqOgBHqhEoFTPzGkPd7L0iH6',
                description: 'Simple Next.js template that uses Vercel Postgres as the database and Prisma as the ORM.',
              } */
            ].map((resource) => {
              return (
                <Link
                  href={`${resource.href}`}
                  key={resource.title}
                  className={'col-span-12 md:col-span-4'}
                  passHref
                >
                  <GlassPanel {...resource} background={false} showIconBg={true}>
                    {resource.description}
                  </GlassPanel>
                </Link>
              )

        })}
  </div>
</div>


### Manual configuration

In your [`Database Settings`](/dashboard/project/_?showConnect=true\&method=transaction) and copy the URI from the `Transaction pooler` section and save it as the `POSTGRES_URL` environment variable. Remember to replace the password placeholder with your actual database password and add the following suffix `?workaround=supabase-pooler.vercel`.

```txt .env.local
POSTGRES_URL="postgres://postgres.cfcxynqnhdybqtbhjemm:[YOUR-PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres?workaround=supabase-pooler.vercel"
```

<Tabs scrollable defaultActiveId="drizzle" type="underlined" size="small">
  <TabPanel id="drizzle" label="Drizzle">
    ```ts lib/drizzle.ts
    import { pgTable, serial, text, timestamp, uniqueIndex } from 'drizzle-orm/pg-core'
    import { InferSelectModel, InferInsertModel } from 'drizzle-orm'
    import { sql } from '@vercel/postgres'
    import { drizzle } from 'drizzle-orm/vercel-postgres'

    export const UsersTable = pgTable(
      'users',
      {
        id: serial('id').primaryKey(),
        name: text('name').notNull(),
        email: text('email').notNull(),
        image: text('image').notNull(),
        createdAt: timestamp('createdAt').defaultNow().notNull(),
      },
      (users) => {
        return {
          uniqueIdx: uniqueIndex('unique_idx').on(users.email),
        }
      }
    )

    export type User = InferSelectModel<typeof UsersTable>
    export type NewUser = InferInsertModel<typeof UsersTable>

    // Connect to Vercel Postgres
    export const db = drizzle(sql)
    ```
  </TabPanel>

  <TabPanel id="kysely" label="Kysely">
    ```ts lib/kysely.ts
    import { Generated, ColumnType } from 'kysely'
    import { createKysely } from '@vercel/postgres-kysely'

    interface UserTable {
      // Columns that are generated by the database should be marked
      // using the `Generated` type. This way they are automatically
      // made optional in inserts and updates.
      id: Generated<number>
      name: string
      email: string
      image: string

      // You can specify a different type for each operation (select, insert and
      // update) using the `ColumnType<SelectType, InsertType, UpdateType>`
      // wrapper. Here we define a column `createdAt` that is selected as
      // a `Date`, can optionally be provided as a `string` in inserts and
      // can never be updated:
      createdAt: ColumnType<Date, string | undefined, never>
    }

    // Keys of this interface are table names.
    export interface Database {
      users: UserTable
    }

    export const db = createKysely<Database>()
    export { sql } from 'kysely'
    ```
  </TabPanel>
</Tabs>



## Cloudflare Workers

Cloudflare's Workers runtime also uses the [V8 engine](https://v8.dev/) but provides polyfills for a subset of Node.js APIs and [TCP Sockets API](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/), giving you a couple of options:

*   [supabase-js](https://developers.cloudflare.com/workers/databases/native-integrations/supabase/)
*   [Postgres.js](https://github.com/porsager/postgres?tab=readme-ov-file#cloudflare-workers-support)
*   [node-postgres](https://developers.cloudflare.com/workers/tutorials/postgres/)



## Supabase Edge Functions

Supabase Edge Functions uses the [Deno runtime](https://deno.com/) which has native support for TCP connections allowing you to choose your favorite client:

*   [supabase-js](/docs/guides/functions/connect-to-postgres#using-supabase-js)
*   [Deno Postgres driver](/docs/guides/functions/connect-to-postgres#using-a-postgres-client)
*   [Postgres.js](https://github.com/porsager/postgres)
*   [Drizzle](/docs/guides/functions/connect-to-postgres#using-drizzle)



---
**Navigation:** [← Previous](./25-event-triggers.md) | [Index](./index.md) | [Next →](./27-install.md)
