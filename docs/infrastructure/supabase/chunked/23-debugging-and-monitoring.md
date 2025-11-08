**Navigation:** [← Previous](./22-connection-management.md) | [Index](./index.md) | [Next →](./24-securing-your-data.md)

# Debugging and monitoring



Database performance is a large topic and many factors can contribute. Some of the most common causes of poor performance include:

*   An inefficiently designed schema
*   Inefficiently designed queries
*   A lack of indexes causing slower than required queries over large tables
*   Unused indexes causing slow `INSERT`, `UPDATE` and `DELETE` operations
*   Not enough compute resources, such as memory, causing your database to go to disk for results too often
*   Lock contention from multiple queries operating on highly utilized tables
*   Large amount of bloat on your tables causing poor query planning

You can examine your database and queries for these issues using either the [Supabase CLI](/docs/guides/local-development/cli/getting-started) or SQL.



## Using the CLI

The Supabase CLI comes with a range of tools to help inspect your Postgres instances for potential issues. The CLI gets the information from <a href="https://www.postgresql.org/docs/current/internals.html" target="_blank">Postgres internals</a>. Therefore, most tools provided are compatible with any Postgres databases regardless if they are a Supabase project or not.

You can find installation instructions for the the Supabase CLI <a href="/docs/guides/cli" target="_blank">here</a>.


### The `inspect db` command

The inspection tools for your Postgres database are under then `inspect db` command. You can get a full list of available commands by running `supabase inspect db help`.

```
$ supabase inspect db help
Tools to inspect your Supabase database

Usage:
  supabase inspect db [command]

Available Commands:
  bloat                Estimates space allocated to a relation that is full of dead tuples
  blocking             Show queries that are holding locks and the queries that are waiting for them to be released
  cache-hit            Show cache hit rates for tables and indices

...
```


### Connect to any Postgres database

Most inspection commands are Postgres agnostic. You can run inspection routines on any Postgres database even if it is not a Supabase project by providing a connection string via `--db-url`.

For example you can connect to your local Postgres instance:

```
supabase --db-url postgresql://postgres:postgres@localhost:5432/postgres inspect db bloat
```


### Connect to a Supabase instance

Working with Supabase, you can link the Supabase CLI with your project:

```
supabase link --project-ref <project-id>
```

Then the CLI will automatically connect to your Supabase project whenever you are in the project folder and you no longer need to provide `—db-url`.


### Inspection commands

Below are the `db` inspection commands provided, grouped by different use cases.

<Admonition type="note">
  Some commands might require `pg_stat_statements` to be enabled or a specific Postgres version to be used.
</Admonition>


#### Disk storage

These commands are handy if you are running low on disk storage:

*   [bloat](/docs/reference/cli/supabase-inspect-db-bloat) - estimates the amount of wasted space
*   [vacuum-stats](/docs/reference/cli/supabase-inspect-db-vacuum-stats) - gives information on waste collection routines
*   [table-record-counts](/docs/reference/cli/supabase-inspect-db-table-record-counts) - estimates the number of records per table
*   [table-sizes](/docs/reference/cli/supabase-inspect-db-table-sizes) - shows the sizes of tables
*   [index-sizes](/docs/reference/cli/supabase-inspect-db-index-sizes) - shows the sizes of individual index
*   [table-index-sizes](/docs/reference/cli/supabase-inspect-db-table-index-sizes) - shows the sizes of indexes for each table


#### Query performance

The commands below are useful if your Postgres database consumes a lot of resources like CPU, RAM or Disk IO. You can also use them to investigate slow queries.

*   [cache-hit](/docs/reference/cli/supabase-inspect-db-cache-hit) - shows how efficient your cache usage is overall
*   [unused-indexes](/docs/reference/cli/supabase-inspect-db-unused-indexes) - shows indexes with low index scans
*   [index-usage](/docs/reference/cli/supabase-inspect-db-index-usage) - shows information about the efficiency of indexes
*   [seq-scans](/docs/reference/cli/supabase-inspect-db-seq-scans) - show number of sequential scans recorded against all tables
*   [long-running-queries](/docs/reference/cli/supabase-inspect-db-long-running-queries) - shows long running queries that are executing right now
*   [outliers](/docs/reference/cli/supabase-inspect-db-outliers) - shows queries with high execution time but low call count and queries with high proportion of execution time spent on synchronous I/O


#### Locks

*   [locks](/docs/reference/cli/supabase-inspect-db-locks) - shows statements which have taken out an exclusive lock on a relation
*   [blocking](/docs/reference/cli/supabase-inspect-db-blocking) - shows statements that are waiting for locks to be released


#### Connections

*   [role-connections](/docs/reference/cli/supabase-inspect-db-role-connections) - shows number of active connections for all database roles (Supabase-specific command)
*   [replication-slots](/docs/reference/cli/supabase-inspect-db-replication-slots) - shows information about replication slots on the database


### Notes on `pg_stat_statements`

Following commands require `pg_stat_statements` to be enabled: calls, locks, cache-hit, blocking, unused-indexes, index-usage, bloat, outliers, table-record-counts, replication-slots, seq-scans, vacuum-stats, long-running-queries.

When using `pg_stat_statements` also take note that it only stores the latest 5,000 statements. Moreover, consider resetting the analysis after optimizing any queries by running `select pg_stat_statements_reset();`

Learn more about pg\_stats [here](/docs/guides/database/extensions/pg_stat_statements).



## Using SQL

<Admonition type="note">
  If you're seeing an `insufficient privilege` error when viewing the Query Performance page from the dashboard, run this command:

  ```shell
  $ grant pg_read_all_stats to postgres;
  ```
</Admonition>


### Postgres cumulative statistics system

Postgres collects data about its own operations using the [cumulative statistics system](https://www.postgresql.org/docs/current/monitoring-stats.html). In addition to this, every Supabase project has the [pg\_stat\_statements extension](/docs/guides/database/extensions/pg_stat_statements) enabled by default. This extension records query execution performance details and is the best way to find inefficient queries. This information can be combined with the Postgres query plan analyzer to develop more efficient queries.

Here are some example queries to get you started.


### Most frequently called queries

```sql
select
  auth.rolname,
  statements.query,
  statements.calls,
  -- -- Postgres 13, 14, 15
  statements.total_exec_time + statements.total_plan_time as total_time,
  statements.min_exec_time + statements.min_plan_time as min_time,
  statements.max_exec_time + statements.max_plan_time as max_time,
  statements.mean_exec_time + statements.mean_plan_time as mean_time,
  -- -- Postgres <= 12
  -- total_time,
  -- min_time,
  -- max_time,
  -- mean_time,
  statements.rows / statements.calls as avg_rows
from
  pg_stat_statements as statements
  inner join pg_authid as auth on statements.userid = auth.oid
order by statements.calls desc
limit 100;
```

This query shows:

*   query statistics, ordered by the number of times each query has been executed
*   the role that ran the query
*   the number of times it has been called
*   the average number of rows returned
*   the cumulative total time the query has spent running
*   the min, max and mean query times.

This provides useful information about the queries you run most frequently. Queries that have high `max_time` or `mean_time` times and are being called often can be good candidates for optimization.


### Slowest queries by execution time

```sql
select
  auth.rolname,
  statements.query,
  statements.calls,
  -- -- Postgres 13, 14, 15
  statements.total_exec_time + statements.total_plan_time as total_time,
  statements.min_exec_time + statements.min_plan_time as min_time,
  statements.max_exec_time + statements.max_plan_time as max_time,
  statements.mean_exec_time + statements.mean_plan_time as mean_time,
  -- -- Postgres <= 12
  -- total_time,
  -- min_time,
  -- max_time,
  -- mean_time,
  statements.rows / statements.calls as avg_rows
from
  pg_stat_statements as statements
  inner join pg_authid as auth on statements.userid = auth.oid
order by max_time desc
limit 100;
```

This query will show you statistics about queries ordered by the maximum execution time. It is similar to the query above ordered by calls, but this one highlights outliers that may have high executions times. Queries which have high or mean execution times are good candidates for optimization.


### Most time consuming queries

```sql
select
  auth.rolname,
  statements.query,
  statements.calls,
  statements.total_exec_time + statements.total_plan_time as total_time,
  to_char(
    (
      (statements.total_exec_time + statements.total_plan_time) / sum(
        statements.total_exec_time + statements.total_plan_time
      ) over ()
    ) * 100,
    'FM90D0'
  ) || '%' as prop_total_time
from
  pg_stat_statements as statements
  inner join pg_authid as auth on statements.userid = auth.oid
order by total_time desc
limit 100;
```

This query will show you statistics about queries ordered by the cumulative total execution time. It shows the total time the query has spent running as well as the proportion of total execution time the query has taken up.

Queries which are the most time consuming are not necessarily bad, you may have a very efficient and frequently ran queries that end up taking a large total % time, but it can be useful to help spot queries that are taking up more time than they should.


### Hit rate

Generally for most applications a small percentage of data is accessed more regularly than the rest. To make sure that your regularly accessed data is available, Postgres tracks your data access patterns and keeps this in its [shared\_buffers](https://www.postgresql.org/docs/15/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) cache.

Applications with lower cache hit rates generally perform more poorly since they have to hit the disk to get results rather than serving them from memory. Very poor hit rates can also cause you to burst past your [Disk IO limits](./compute-add-ons#disk-io) causing significant performance issues.

You can view your cache and index hit rate by executing the following query:

```sql
select
  'index hit rate' as name,
  (sum(idx_blks_hit)) / nullif(sum(idx_blks_hit + idx_blks_read), 0) * 100 as ratio
from pg_statio_user_indexes
union all
select
  'table hit rate' as name,
  sum(heap_blks_hit) / nullif(sum(heap_blks_hit) + sum(heap_blks_read), 0) * 100 as ratio
from pg_statio_user_tables;
```

This shows the ratio of data blocks fetched from the Postgres [shared\_buffers](https://www.postgresql.org/docs/15/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-MEMORY) cache against the data blocks that were read from disk/OS cache.

If either of your index or table hit rate are \< 99% then this can indicate your compute plan is too small for your current workload and you would benefit from more memory. [Upgrading your compute](./compute-add-ons) is easy and can be done from your [project dashboard](/dashboard/project/_/settings/compute-and-disk).


### Optimizing poor performing queries

Postgres has built in tooling to help you optimize poorly performing queries. You can use the [query plan analyzer](https://www.postgresql.org/docs/current/sql-explain.html) on any expensive queries that you have identified:

```sql
explain analyze <query-statement-here>;
```

When you include `analyze` in the explain statement, the database attempts to execute the query and provides a detailed query plan along with actual execution times. So, be careful using `explain analyze` with `insert`/`update`/`delete` queries, because the query will actually run, and could have unintended side-effects.

If you run just `explain` without the `analyze` keyword, the database will only perform query planning without actually executing the query. This approach can be beneficial when you want to inspect the query plan without affecting the database or if you encounter timeouts in your queries.

Using the query plan analyzer to optimize your queries is a large topic, with a number of online resources available:

*   [Official docs.](https://www.postgresql.org/docs/current/using-explain.html)
    {/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}
*   [The Art of PostgreSQL.](https://theartofpostgresql.com/explain-plan-visualizer/)
*   [Postgres Wiki.](https://wiki.postgresql.org/wiki/Using_EXPLAIN)
*   [Enterprise DB.](https://www.enterprisedb.com/blog/postgresql-query-optimization-performance-tuning-with-explain-analyze)

You can pair the information available from `pg_stat_statements` with the detailed system metrics available [via your metrics endpoint](../platform/metrics) to better understand the behavior of your DB and the queries you're executing against it.



# Querying Joins and Nested tables



The data APIs automatically detect relationships between Postgres tables. Since Postgres is a relational database, this is a very common scenario.



## One-to-many joins

Let's use an example database that stores `orchestral_sections` and `instruments`:

<Tabs scrollable size="small" type="underlined" defaultActiveId="table" queryGroup="output-format">
  <TabPanel id="table" label="Tables">
    **Orchestral sections**

    | `id` | `name`    |
    | ---- | --------- |
    | 1    | strings   |
    | 2    | woodwinds |

    **Instruments**

    | `id` | `name` | `section_id` |
    | ---- | ------ | ------------ |
    | 1    | violin | 1            |
    | 2    | viola  | 1            |
    | 3    | flute  | 2            |
    | 4    | oboe   | 2            |
  </TabPanel>

  <TabPanel id="SQL" label="SQL">
    ```sql
    create table orchestral_sections (
      "id" serial primary key,
      "name" text
    );

    insert into orchestral_sections
      (id, name)
    values
      (1, 'strings'),
      (2, 'woodwinds');

    create table instruments (
      "id" serial primary key,
      "name" text,
      "section_id" int references "orchestral_sections"
    );

    insert into instruments
      (name, section_id)
    values
      ('violin', 1),
      ('viola', 1),
      ('flute', 2),
      ('oboe', 2);
    ```
  </TabPanel>
</Tabs>

The APIs will automatically detect relationships based on the foreign keys:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('orchestral_sections').select(`
      id,
      name,
      instruments ( id, name )
    `)
    ```

    ### TypeScript types for joins

    `supabase-js` always returns a `data` object (for success), and an `error` object (for unsuccessful requests).

    These helper types provide the result types from any query, including nested types for database joins.

    Given the following schema with a relation between orchestral sections and instruments:

    ```sql
    create table orchestral_sections (
      "id" serial primary key,
      "name" text
    );

    create table instruments (
      "id" serial primary key,
      "name" text,
      "section_id" int references "orchestral_sections"
    );
    ```

    We can get the nested `SectionsWithInstruments` type like this:

    ```ts
    import { QueryResult, QueryData, QueryError } from '@supabase/supabase-js'

    const sectionsWithInstrumentsQuery = supabase.from('orchestral_sections').select(`
      id,
      name,
      instruments (
        id,
        name
      )
    `)
    type SectionsWithInstruments = QueryData<typeof sectionsWithInstrumentsQuery>

    const { data, error } = await sectionsWithInstrumentsQuery
    if (error) throw error
    const sectionsWithInstruments: SectionsWithInstruments = data
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.from('orchestral_sections').select('id, name, instruments(id, name)');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct OrchestralSection: Codable {
      let id: Int
      let name: String
      let instruments: [Instrument]

      struct Instrument: Codable {
        let id: Int
        let name: String
      }
    }

    let orchestralSections: [OrchestralSection] = try await supabase
      .from("orchestral_sections")
      .select("id, name, instruments(id, name)")
      .execute()
      .value
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("orchestral_sections").select(Columns.raw("id, name, instruments(id, name)"))
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('orchestral_sections').select('id, name, instruments(id, name)').execute()
    ```
  </TabPanel>

  <TabPanel id="graphql" label="GraphQL">
    ```javascript
    const Query = `
      query {
        orchestral_sectionsCollection {
          edges {
            node {
              id
              name
              instruments {
                id,
                name
              }
            }
          }
        }
      }
    `
    ```
  </TabPanel>

  <TabPanel id="url" label="URL">
    ```bash
    GET https://[REF].supabase.co/rest/v1/orchestral_sections?select=id,name,instruments(id,name)
    ```
  </TabPanel>
</Tabs>



## Many-to-many joins

The data APIs will detect many-to-many joins. For example, if you have a database which stored teams of users (where each user could belong to many teams):

```sql
create table users (
  "id" serial primary key,
  "name" text
);

create table teams (
  "id" serial primary key,
  "team_name" text
);

create table members (
  "user_id" int references users,
  "team_id" int references teams,
  primary key (user_id, team_id)
);
```

In these cases you don't need to explicitly define the joining table (members). If we wanted to fetch all the teams and the members in each team:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('teams').select(`
      id,
      team_name,
      users ( id, name )
    `)
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.from('teams').select('id, team_name, users(id, name)');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct Team: Codable {
      let id: Int
      let name: String
      let users: [User]

      struct User: Codable {
        let id: Int
        let name: String
      }

      enum CodingKeys: String, CodingKey {
        case id, users
        case name = "team_name"
      }
    }
    let teams [Team] = try await supabase
      .from("teams")
      .select(
        """
          id,
          team_name,
          users ( id, name )
        """
      )
      .execute()
      .value
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("teams").select(Columns.raw("id, team_name, users(id, name)"));
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('teams').select('id, team_name, users(id, name)').execute()
    ```
  </TabPanel>

  <TabPanel id="graphql" label="GraphQL">
    ````javascript
    const Query = `
      query {

    </TabPanel>
    <TabPanel id="graphql" label="GraphQL">

    ```javascript
    const Query = `
      query {
        teamsCollection {
          edges {
            node {
              id
              team_name
              users {
                id,
                name
              }
            }
          }
        }
      }
    `
    ````
  </TabPanel>

  <TabPanel id="url" label="URL">
    ```bash
    GET https://[REF].supabase.co/rest/v1/teams?select=id,team_name,users(id,name)
    ```
  </TabPanel>
</Tabs>



## Specifying the `ON` clause for joins with multiple foreign keys

For example, if you have a project that tracks when employees check in and out of work shifts:

```sql
-- Employees
create table users (
  "id" serial primary key,
  "name" text
);

-- Badge scans
create table scans (
  "id" serial primary key,
  "user_id" int references users,
  "badge_scan_time" timestamp
);

-- Work shifts
create table shifts (
  "id" serial primary key,
  "user_id" int references users,
  "scan_id_start" int references scans, -- clocking in
  "scan_id_end" int references scans, -- clocking out
  "attendance_status" text
);
```

In this case, you need to explicitly define the join because the joining column on `shifts` is ambiguous as they are both referencing the `scans` table.

To fetch all the `shifts` with `scan_id_start` and `scan_id_end` related to a specific `scan`, use the following syntax:

<Tabs scrollable size="small" type="underlined" defaultActiveId="js" queryGroup="language">
  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('shifts').select(
      `
        *,
        start_scan:scans!scan_id_start (
          id,
          user_id,
          badge_scan_time
        ),
       end_scan:scans!scan_id_end (
         id,
         user_id,
         badge_scan_time
        )
      `
    )
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    final data = await supabase.from('shifts').select('''
      *,
      start_scan:scans!scan_id_start (
        id,
        user_id,
        badge_scan_time
      ),
    end_scan:scans!scan_id_end (
        id,
        user_id,
        badge_scan_time
      )
    ''');
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    struct Shift: Codable {
      let id: Int
      let userId: Int
      let attendanceStatus: String?

      let scans: [Scan]

      struct Scan: Codable {
        let id: Int
        let userId: Int
        let badgeScanTime: TimeInterval

        enum CodingKeys: String, CodingKey {
          case id
          case userId = "user_id"
          case badgeScanTime = "badge_scan_time"
        }
      }

      enum CodingKeys: String, CodingKey {
        case id
        case userId = "user_id"
        case attendanceStatus = "attendance_status"
      }
    }

    let shifts: [Shift] = try await supabase
      .from("shifts")
      .select(
        """
          *,
          start_scan:scans!scan_id_start (
            id,
            user_id,
            badge_scan_time
          ),
         scans: scan_id_end (
            id,
            user_id,
            badge_scan_time
         )
        """
      )
      .execute()
      .value
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("shifts").select(Columns.raw('''
      *,
      start_scan:scans!scan_id_start (
        id,
        user_id,
        badge_scan_time
      ),
    end_scan:scans!scan_id_end (
        id,
        user_id,
        badge_scan_time
      )
    '''));
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('shifts').select("""
      *,
      start_scan:scans!scan_id_start (
        id,
        user_id,
        badge_scan_time
      ),
      end_scan:scans!scan_id_end (
        id,
        user_id,
        badge_scan_time
      )
    """).execute()
    ```
  </TabPanel>

  <TabPanel id="graphql" label="GraphQL">
    ```javascript
    const Query = `
      query {
        shiftsCollection {
          edges {
            node {
              id
              user_id
              attendance_status
              scan_id_start {
                id
                user_id
                badge_scan_time
              }
              scan_id_end {
                id
                user_id
                badge_scan_time
              }
            }
          }
        }
      }
    `
    ```
  </TabPanel>
</Tabs>



# Managing JSON and unstructured data

Using the JSON data type in Postgres.

Postgres supports storing and querying unstructured data.



## JSON vs JSONB

Postgres supports two types of JSON columns: `json` (stored as a string) and `jsonb` (stored as a binary). The recommended type is `jsonb` for almost all cases.

*   `json` stores an exact copy of the input text. Database functions must reparse the content on each execution.
*   `jsonb` stores database in a decomposed binary format. While this makes it slightly slower to input due to added conversion overhead, it is significantly faster to process, since no reparsing is needed.



## When to use JSON/JSONB

Generally you should use a `jsonb` column when you have data that is unstructured or has a variable schema. For example, if you wanted to store responses for various webhooks, you might not know the format of the response when creating the table. Instead, you could store the `payload` as a `jsonb` object in a single column.

Don't go overboard with `json/jsonb` columns. They are a useful tool, but most of the benefits of a relational database come from the ability to query and join structured data, and the referential integrity that brings.



## Create JSONB columns

`json/jsonb` is just another "data type" for Postgres columns. You can create a `jsonb` column in the same way you would create a `text` or `int` column:

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    create table books (
      id serial primary key,
      title text,
      author text,
      metadata jsonb
    );
    ```
  </TabPanel>

  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table Editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Click **New Table** and create a table called `books`.
    3.  Include a primary key with the following properties and click save:

    *   Name: `id`
        *   Type: `int8`
        *   Default value: `Automatically generate as indentity`
    *   **title** column
        *   Name: `title`
        *   Type: `text`
    *   **author** column
        *   Name: `author`
        *   Type: `text`
    *   **metadata** column
        *   Name: `metadata`
        *   Type: `jsonb`
  </TabPanel>
</Tabs>



## Inserting JSON data

You can insert JSON data in the same way that you insert any other data. The data must be valid JSON.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    insert into books
      (title, author, metadata)
    values
      (
        'The Poky Little Puppy',
        'Janette Sebring Lowrey',
        '{"description":"Puppy is slower than other, bigger animals.","price":5.95,"ages":[3,6]}'
      ),
      (
        'The Tale of Peter Rabbit',
        'Beatrix Potter',
        '{"description":"Rabbit eats some vegetables.","price":4.49,"ages":[2,5]}'
      ),
      (
        'Tootle',
        'Gertrude Crampton',
        '{"description":"Little toy train has big dreams.","price":3.99,"ages":[2,5]}'
      ),
      (
        'Green Eggs and Ham',
        'Dr. Seuss',
        '{"description":"Sam has changing food preferences and eats unusually colored food.","price":7.49,"ages":[4,8]}'
      ),
      (
        'Harry Potter and the Goblet of Fire',
        'J.K. Rowling',
        '{"description":"Fourth year of school starts, big drama ensues.","price":24.95,"ages":[10,99]}'
      );
    ```
  </TabPanel>

  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Table Editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Select the `books` table in the sidebar.
    3.  Click **+ Insert row** and add 5 rows with the following properties:

    {/* supa-mdx-lint-disable Rule003Spelling */}

    | id | title                               | author                 | metadata                                                                                                              |
    | -- | ----------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
    | 1  | The Poky Little Puppy               | Janette Sebring Lowrey | `json {"ages":[3,6],"price":5.95,"description":"Puppy is slower than other, bigger animals."}`                        |
    | 2  | The Tale of Peter Rabbit            | Beatrix Potter         | `json {"ages":[2,5],"price":4.49,"description":"Rabbit eats some vegetables."}`                                       |
    | 3  | Tootle                              | Gertrude Crampton      | `json {"ages":[2,5],"price":3.99,"description":"Little toy train has big dreams."}`                                   |
    | 4  | Green Eggs and Ham                  | Dr. Seuss              | `json {"ages":[4,8],"price":7.49,"description":"Sam has changing food preferences and eats unusually colored food."}` |
    | 5  | Harry Potter and the Goblet of Fire | J.K. Rowling           | `json {"ages":[10,99],"price":24.95,"description":"Fourth year of school starts, big drama ensues."}`                 |

    {/* supa-mdx-lint-enable Rule003Spelling */}
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').insert([
      {
        title: 'The Poky Little Puppy',
        author: 'Janette Sebring Lowrey',
        metadata: {
          description: 'Puppy is slower than other, bigger animals.',
          price: 5.95,
          ages: [3, 6],
        },
      },
      {
        title: 'The Tale of Peter Rabbit',
        author: 'Beatrix Potter',
        metadata: {
          description: 'Rabbit eats some vegetables.',
          price: 4.49,
          ages: [2, 5],
        },
      },
      {
        title: 'Tootle',
        author: 'Gertrude Crampton',
        metadata: {
          description: 'Little toy train has big dreams.',
          price: 3.99,
          ages: [2, 5],
        },
      },
      {
        title: 'Green Eggs and Ham',
        author: 'Dr. Seuss',
        metadata: {
          description: 'Sam has changing food preferences and eats unusually colored food.',
          price: 7.49,
          ages: [4, 8],
        },
      },
      {
        title: 'Harry Potter and the Goblet of Fire',
        author: 'J.K. Rowling',
        metadata: {
          description: 'Fourth year of school starts, big drama ensues.',
          price: 24.95,
          ages: [10, 99],
        },
      },
    ])
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase.from('books').insert([
      {
        'title': 'The Poky Little Puppy',
        'author': 'Janette Sebring Lowrey',
        'metadata': {
          'description': 'Puppy is slower than other, bigger animals.',
          'price': 5.95,
          'ages': [3, 6],
        },
      },
      {
        'title': 'The Tale of Peter Rabbit',
        'author': 'Beatrix Potter',
        'metadata': {
          'description': 'Rabbit eats some vegetables.',
          'price': 4.49,
          'ages': [2, 5],
        },
      },
      {
        'title': 'Tootle',
        'author': 'Gertrude Crampton',
        'metadata': {
          'description': 'Little toy train has big dreams.',
          'price': 3.99,
          'ages': [2, 5],
        },
      },
      {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'metadata': {
          'description':
              'Sam has changing food preferences and eats unusually colored food.',
          'price': 7.49,
          'ages': [4, 8],
        },
      },
      {
        'title': 'Harry Potter and the Goblet of Fire',
        'author': 'J.K. Rowling',
        'metadata': {
          'description': 'Fourth year of school starts, big drama ensues.',
          'price': 24.95,
          'ages': [10, 99],
        },
      },
    ]);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    Supabase Swift provides a convenience `AnyJSON` type.

    ```swift
    struct Book {
        val title: String,
        val author: String,
        val metadata: [String: AnyJSON]
    }

    try await supabase.from("books")
      .insert(
        [
          Book(
            title: "The Poky Little Puppy",
            author: "Janette Sebring Lowrey",
            metadata: [
              "description": "Puppy is slower than other, bigger animals.",
              "price": 5.95,
              "ages": [3, 6]
            ]
          ),
          Book(
            title: "Tale of Peter Rabbit",
            author: "Beatrix Potter",
            metadata: [
              "description": "Rabbit eats some vegetables.",
              "price": 4.49,
              "ages": [2, 5]
            ]
          ),
          Book(
            title: "Tootle",
            author: "Gertrude Crampton",
            metadata: [
              "description": "Little toy train has big dreams.",
              "price": 3.99,
              "ages": [2, 5]
            ]
          ),
          Book(
            title: "Green Eggs and Ham",
            author: "Dr. Seuss",
            metadata: [
              "description": "Sam has changing food preferences and eats unusually colored food.",
              "price": 7.49,
              "ages": [4, 8]
            ]
          ),
          Book(
            title: "Harry Potter and the Goblet of Fire",
            author: "J.K. Rowling",
            metadata: [
              "description": "Fourth year of school starts, big drama ensues.",
              "price": 24.95,
              "ages": [10, 99]
            ]
          )
        ]
      )
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    @Serializable
    data class BookMetadata(
        val description: String,
        val price: Double,
        val ages: List<Int>
    )

    @Serializable
    data class Book(
        val title: String,
        val author: String,
        val metadata: BookMetadata
    )
    ```

    ```kotlin
    val data = supabase.from("books").insert(listOf(
        Book("The Poky Little Puppy", "Janette Sebring Lowrey", BookMetadata("Puppy is slower than other, bigger animals.", 5.95, listOf(3, 6))),
        Book("Tale of Peter Rabbit", "Beatrix Potter", BookMetadata("Rabbit eats some vegetables.", 4.49, listOf(2, 5))),
        Book("Tootle", "Gertrude Crampton", BookMetadata("Little toy train has big dreams.", 3.99, listOf(2, 5))),
        Book("Green Eggs and Ham", "Dr. Seuss", BookMetadata("Sam has changing food preferences and eats unusually colored food.", 7.49, listOf(4, 8))),
        Book("Harry Potter and the Goblet of Fire", "J.K. Rowling", BookMetadata("Fourth year of school starts, big drama ensues.", 24.95, listOf(10, 99)))
    ))
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    supabase.from_('books').insert([
      {
        'title': 'The Poky Little Puppy',
        'author': 'Janette Sebring Lowrey',
        'metadata': {
          'description': 'Puppy is slower than other, bigger animals.',
          'price': 5.95,
          'ages': [3, 6],
        },
      },
      {
        'title': 'The Tale of Peter Rabbit',
        'author': 'Beatrix Potter',
        'metadata': {
          'description': 'Rabbit eats some vegetables.',
          'price': 4.49,
          'ages': [2, 5],
        },
      },
      {
        'title': 'Tootle',
        'author': 'Gertrude Crampton',
        'metadata': {
          'description': 'Little toy train has big dreams.',
          'price': 3.99,
          'ages': [2, 5],
        },
      },
      {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'metadata': {
          'description':
              'Sam has changing food preferences and eats unusually colored food.',
          'price': 7.49,
          'ages': [4, 8],
        },
      },
      {
        'title': 'Harry Potter and the Goblet of Fire',
        'author': 'J.K. Rowling',
        'metadata': {
          'description': 'Fourth year of school starts, big drama ensues.',
          'price': 24.95,
          'ages': [10, 99],
        },
      },
    ]).execute()
    ```
  </TabPanel>
</Tabs>



## Query JSON data

Querying JSON data is similar to querying other data, with a few other features to access nested values.

Postgres support a range of [JSON functions and operators](https://www.postgresql.org/docs/current/functions-json.html). For example, the `->` operator returns values as `jsonb` data. If you want the data returned as `text`, use the `->>` operator.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    select
      title,
      metadata ->> 'description' as description, -- returned as text
      metadata -> 'price' as price,
      metadata -> 'ages' -> 0 as low_age,
      metadata -> 'ages' -> 1 as high_age
    from books;
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('books').select(`
        title,
        description:  metadata->>description,
        price:        metadata->price,
        low_age:      metadata->ages->0,
        high_age:     metadata->ages->1
      `)
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase
      .from("books")
      .select(
        """
          title,
          description:  metadata->>description,
          price:        metadata->price,
          low_age:      metadata->ages->0,
          high_age:     metadata->ages->1
        """
      )
      .execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    val data = supabase.from("books").select(Columns.raw("""
        title,
        description: metadata->>description,
        price: metadata->price,
        low_age: metadata->ages->0,
        high_age: metadata->ages->1
    """.trimIndent()))
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    data = supabase.from_('books').select("""
      title,
      description: metadata->>description,
      price: metadata->price,
      low_age: metadata->ages->0,
      high_age: metadata->ages->1
    """
    ).execute()
    ```
  </TabPanel>

  <TabPanel id="result" label="Result">
    | title                               | description                                                        | price | low\_age | high\_age |
    | ----------------------------------- | ------------------------------------------------------------------ | ----- | -------- | --------- |
    | The Poky Little Puppy               | Puppy is slower than other, bigger animals.                        | 5.95  | 3        | 6         |
    | The Tale of Peter Rabbit            | Rabbit eats some vegetables.                                       | 4.49  | 2        | 5         |
    | Tootle                              | Little toy train has big dreams.                                   | 3.99  | 2        | 5         |
    | Green Eggs and Ham                  | Sam has changing food preferences and eats unusually colored food. | 7.49  | 4        | 8         |
    | Harry Potter and the Goblet of Fire | Fourth year of school starts, big drama ensues.                    | 24.95 | 10       | 99        |
  </TabPanel>
</Tabs>



## Validating JSON data

Supabase provides the [`pg_jsonschema` extension](/docs/guides/database/extensions/pg_jsonschema) that adds the ability to validate `json` and `jsonb` data types against [JSON Schema](https://json-schema.org/) documents.

Once you have enabled the extension, you can add a "check constraint" to your table to validate the JSON data:

```sql
create table customers (
  id serial primary key,
  metadata json
);

alter table customers
add constraint check_metadata check (
  json_matches_schema(
    '{
        "type": "object",
        "properties": {
            "tags": {
                "type": "array",
                "items": {
                    "type": "string",
                    "maxLength": 16
                }
            }
        }
    }',
    metadata
  )
);
```



## Resources

*   [Postgres: JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html)
*   [Postgres JSON types](https://www.postgresql.org/docs/current/datatype-json.html)



# Connecting to Metabase



[`Metabase`](https://www.metabase.com/) is an Open Source data visualization tool. You can use it to explore your data stored in Supabase.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Register">
      Create a [Metabase account](https://store.metabase.com/checkout) or deploy locally with [Docker](https://www.docker.com/products/docker-desktop/)
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Deploying with Docker:

      ```sh
      docker pull metabase/metabase:latest
      ```

      Then run:

      ```sh
      docker run -d -p 3000:3000 --name metabase metabase/metabase
      ```

      The server should be available at [`http://localhost:3000/setup`](http://localhost:3000/setup)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Connect to Postgres">
      Connect your Postgres server to Metabase.

      *   On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true)
      *   View parameters under "Session pooler"

      <Admonition type="note" label="connection notice">
        If you're in an [IPv6 environment](/docs/guides/platform/ipv4-address#checking-your-network-ipv6-support) or have the [IPv4 Add-On](/docs/guides/platform/ipv4-address#understanding-ip-addresses), you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>

      *   Enter your database credentials into Metabase
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Example credentials:
      ![Name Postgres Server.](/docs/img/guides/database/connecting-to-postgres/metabase/add-pg-server.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Explore">
      Explore your data in Metabase
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![explore data](/docs/img/guides/database/connecting-to-postgres/metabase/explore.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# OrioleDB Overview



The [OrioleDB](https://www.orioledb.com/) Postgres extension provides a drop-in replacement storage engine for the default heap storage method. It is designed to improve Postgres' scalability and performance.

OrioleDB addresses PostgreSQL's scalability limitations by removing bottlenecks in the shared memory cache under high concurrency. It also optimizes write-ahead-log (WAL) insertion through row-level WAL logging. These changes lead to significant improvements in the industry standard TPC-C benchmark, which approximates a real-world transactional workload. The following benchmark was performed on a c7g.metal instance and shows OrioleDB's performance outperforming the default Postgres heap method with a 3.3x speedup.

<Image alt="TPC-C (warehouses = 500)" src="/docs/img/database/orioledb-tpc-c-500-warehouse.png" className="max-w-[550px] !mx-auto border rounded-md" zoomable />

<Admonition type="note">
  OrioleDB is in active development and currently has [certain limitations](https://www.orioledb.com/docs/usage/getting-started#current-limitations). Currently, only B-tree indexes are supported, so features like pg\_vector's HNSW indexes are not yet available. An Index Access Method bridge to unlock support for all index types used with heap storage is under active development. In the Supabase OrioleDB image the default storage method has been updated to use OrioleDB, granting better performance out of the box.
</Admonition>



## Concepts


### Index-organized tables

OrioleDB uses index-organized tables, where table data is stored in the index structure. This design eliminates the need for separate heap storage, reduces overhead and improves lookup performance for primary key queries.


### No buffer mapping

In-memory pages are connected to the storage pages using direct links. This allows OrioleDB to bypass PostgreSQL's shared buffer pool and eliminate the associated complexity and contention in buffer mapping.


### Undo log

Multi-Version Concurrency Control (MVCC) is implemented using an undo log. The undo log stores previous row versions and transaction information, which enables consistent reads while removing the need for table vacuuming completely.


### Copy-on-write checkpoints

OrioleDB implements copy-on-write checkpoints to persist data efficiently. This approach writes only modified data during a checkpoint, reducing the I/O overhead compared to traditional Postgres checkpointing and allowing row-level WAL logging.



## Usage


### Creating OrioleDB project

You can get started with OrioleDB by enabling the extension in your Supabase dashboard.
To get started with OrioleDB you need to [create a new Supabase project](/dashboard/new/_) and choose `OrioleDB Public Alpha` Postgres version.

<Image
  alt="Creating OrioleDB project"
  src={{
    light: '/docs/img/database/orioledb-creating-project--light.png',
    dark: '/docs/img/database/orioledb-creating-project.png',
  }}
  className="max-w-[550px] !mx-auto border rounded-md"
  zoomable
/>


### Creating tables

To create a table using the OrioleDB storage engine just execute the standard `CREATE TABLE` statement. By default it will create a table using OrioleDB storage engine. For example:

```sql
-- Create a table
create table blog_post (
  id int8 not null,
  title text not null,
  body text not null,
  author text not null,
  published_at timestamptz not null default CURRENT_TIMESTAMP,
  views bigint not null,
  primary key (id)
);
```


### Creating indexes

OrioleDB tables always have a primary key. If it wasn't defined explicitly, a hidden primary key is created using the `ctid` column.
Additionally you can create secondary indexes.

<Admonition type="note">
  Currently, only B-tree indexes are supported, so features like pg\_vector's HNSW indexes are not yet available.
</Admonition>

```sql
-- Create an index
create index blog_post_published_at on blog_post (published_at);

create index blog_post_views on blog_post (views) where (views > 1000);
```


### Data manipulation

You can query and modify data in OrioleDB tables using standard SQL statements, including `SELECT`, `INSERT`, `UPDATE`, `DELETE` and `INSERT ... ON CONFLICT`.

```sql
INSERT INTO blog_post (id, title, body, author, views)
VALUES (1, 'Hello, World!', 'This is my first blog post.', 'John Doe', 1000);

SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
 id │     title     │            body             │  author  │         published_at          │ views
────┼───────────────┼─────────────────────────────┼──────────┼───────────────────────────────┼───────
  1 │ Hello, World! │ This is my first blog post. │ John Doe │ 2024-11-15 12:04:18.756824+01 │  1000
```


### Viewing query plans

You can see the execution plan using standard `EXPLAIN` statement.

```sql
EXPLAIN SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
                                                 QUERY PLAN
────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Limit  (cost=0.15..1.67 rows=10 width=120)
   ->  Index Scan Backward using blog_post_published_at on blog_post  (cost=0.15..48.95 rows=320 width=120)

EXPLAIN SELECT * FROM blog_post WHERE id = 1;
                                    QUERY PLAN
──────────────────────────────────────────────────────────────────────────────────
 Index Scan using blog_post_pkey on blog_post  (cost=0.15..8.17 rows=1 width=120)
   Index Cond: (id = 1)

EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM blog_post ORDER BY published_at DESC LIMIT 10;
                                                                      QUERY PLAN
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Limit  (cost=0.15..1.67 rows=10 width=120) (actual time=0.052..0.054 rows=1 loops=1)
   ->  Index Scan Backward using blog_post_published_at on blog_post  (cost=0.15..48.95 rows=320 width=120) (actual time=0.050..0.052 rows=1 loops=1)
 Planning Time: 0.186 ms
 Execution Time: 0.088 ms
```



## Resources

*   [Official OrioleDB documentation](https://www.orioledb.com/docs)
*   [OrioleDB GitHub repository](https://github.com/orioledb/orioledb)



# Database



Every Supabase project comes with a full [Postgres](https://www.postgresql.org/) database, a free and open source database which is considered one of the world's most stable and advanced databases.



## Features


### Table view

You don't have to be a database expert to start using Supabase. Our table view makes Postgres as easy to use as a spreadsheet.

![Table View.](/docs/img/table-view.png)


### Relationships

Dig into the relationships within your data.

<video width="99%" loop muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/relational-drilldown-zoom.mp4" type="video/mp4" />
</video>


### Clone tables

You can duplicate your tables, just like you would inside a spreadsheet.

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/duplicate-tables.mp4" type="video/mp4" />
</video>


### The SQL editor

Supabase comes with a SQL Editor. You can also save your favorite queries to run later!

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/favorites.mp4" type="video/mp4" />
</video>


### Additional features

*   Supabase extends Postgres with realtime functionality using our [Realtime Server](https://github.com/supabase/realtime).
*   Every project is a full Postgres database, with `postgres` level access.
*   Supabase manages your database backups.
*   Import data directly from a CSV or excel spreadsheet.

<Admonition type="note">
  Database backups **do not** include objects stored via the Storage API, as the database only includes metadata about these objects. Restoring an old backup does not restore objects that have been deleted since then.
</Admonition>


### Extensions

To expand the functionality of your Postgres database, you can use extensions.
You can enable Postgres extensions with the click of a button within the Supabase dashboard.

<video width="99%" muted playsInline controls={true}>
  <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/toggle-extensions.mp4" type="video/mp4" />
</video>

[Learn more](/docs/guides/database/extensions) about all the extensions provided on Supabase.



## Terminology

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}


### Postgres or PostgreSQL?

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

PostgreSQL the database was derived from the POSTGRES Project, a package written at the University of California at Berkeley in 1986. This package included a query language called "PostQUEL".

In 1994, Postgres95 was built on top of POSTGRES code, adding an SQL language interpreter as a replacement for PostQUEL.

{/* supa-mdx-lint-disable-next-line Rule004ExcludeWords */}

Eventually, Postgres95 was renamed to PostgreSQL to reflect the SQL query capability.
After this, many people referred to it as Postgres since it's less prone to confusion. Supabase is all about simplicity, so we also refer to it as Postgres.



## Tips

Read about resetting your database password [here](/docs/guides/database/managing-passwords) and changing the timezone of your server [here](/docs/guides/database/managing-timezones).



## Next steps

*   Read more about [Postgres](https://www.postgresql.org/about/)
*   Sign in: [supabase.com/dashboard](/dashboard)



# Partitioning tables



Table partitioning is a technique that allows you to divide a large table into smaller, more manageable parts called “partitions”.

<Image
  alt="multi database"
  src={{
    light: '/docs/img/database/partitions-light.png',
    dark: '/docs/img/database/partitions-dark.png',
  }}
  className="max-h-[400px] !mx-auto"
/>

Each partition contains a subset of the data based on a specified criteria, such as a range of values or a specific condition. Partitioning can significantly improve query performance and simplify data management for large datasets.



## Benefits of table partitioning

*   **Improved query performance:** allows queries to target specific partitions, reducing the amount of data scanned and improving query execution time.
*   **Scalability:** With partitioning, you can add or remove partitions as your data grows or changes, enabling better scalability and flexibility.
*   **Efficient data management:** simplifies tasks such as data loading, archiving, and deletion by operating on smaller partitions instead of the entire table.
*   **Enhanced maintenance operations:** can optimize vacuuming and indexing, leading to faster maintenance tasks.



## Partitioning methods

Postgres supports various partitioning methods based on how you want to partition your data. The commonly used methods are:

1.  **Range Partitioning**: Data is divided into partitions based on a specified range of values. For example, you can partition a sales table by date, where each partition represents a specific time range (e.g., one partition for each month).
2.  **List Partitioning**: Data is divided into partitions based on a specified list of values. For instance, you can partition a customer table by region, where each partition contains customers from a specific region (e.g., one partition for customers in the US, another for customers in Europe).
3.  **Hash Partitioning**: Data is distributed across partitions using a hash function. This method provides a way to evenly distribute data among partitions, which can be useful for load balancing. However, it doesn't allow direct querying based on specific values.



## Creating partitioned tables

Let's consider an example of range partitioning for a sales table based on the order date. We'll create monthly partitions to store data for each month:

```sql
create table sales (
    id bigint generated by default as identity,
    order_date date not null,
    customer_id bigint,
    amount bigint,

    -- We need to include all the
    -- partitioning columns in constraints:
    primary key (order_date, id)
)
partition by range (order_date);

create table sales_2000_01
	partition of sales
  for values from ('2000-01-01') to ('2000-02-01');

create table sales_2000_02
	partition of sales
	for values from ('2000-02-01') to ('2000-03-01');

```

To create a partitioned table you append `partition by range (<column_name>)` to the table creation statement. The column that you are partitioning with *must* be included in any unique index, which is the reason why we specify a composite primary key here (`primary key (order_date, id)`).



## Querying partitioned tables

To query a partitioned table, you have two options:

1.  Querying the parent table
2.  Querying specific partitions


### Querying the parent table

When you query the parent table, Postgres automatically routes the query to the relevant partitions based on the conditions specified in the query. This allows you to retrieve data from all partitions simultaneously.

Example:

```sql
select *
from sales
where order_date >= '2000-01-01' and order_date < '2000-03-01';
```

This query will retrieve data from both the `sales_2000_01` and `sales_2000_02` partitions.


### Querying specific partitions

If you only need to retrieve data from a specific partition, you can directly query that partition instead of the parent table. This approach is useful when you want to target a specific range or condition within a partition.

```sql
select *
from sales_2000_02;
```

This query will retrieve data only from the `sales_2000_02` partition.



## When to partition your tables

There is no real threshold to determine when you should use partitions. Partitions introduce complexity, and complexity should be avoided until it's needed. A few guidelines:

*   If you are considering performance, avoid partitions until you see performance degradation on non-partitioned tables.
*   If you are using partitions as a management tool, it's fine to create the partitions any time.
*   If you don't know how you should partition your data, then it's probably too early.



## Examples

Here are simple examples for each of the partitioning types in Postgres.


### Range partitioning

Let's consider a range partitioning example for a table that stores sales data based on the order date. We'll create monthly partitions to store data for each month.

In this example, the **`sales`** table is partitioned into two partitions: **`sales_january`** and **`sales_february`**. The data in these partitions is based on the specified range of order dates:

```sql
create table sales (
    id bigint generated by default as identity,
    order_date date not null,
    customer_id bigint,
    amount bigint,

    -- We need to include all the
    -- partitioning columns in constraints:
    primary key (order_date, id)
)
partition by range (order_date);

create table sales_2000_01
	partition of sales
  for values from ('2000-01-01') to ('2000-02-01');

create table sales_2000_02
	partition of sales
	for values from ('2000-02-01') to ('2000-03-01');
```


### List partitioning

Let's consider a list partitioning example for a table that stores customer data based on their region. We'll create partitions to store customers from different regions.

In this example, the **`customers`** table is partitioned into two partitions: `customers_americas` and `customers_asia`. The data in these partitions is based on the specified list of regions:

```sql
-- Create the partitioned table
create table customers (
    id bigint generated by default as identity,
    name text,
    country text,

    -- We need to include all the
    -- partitioning columns in constraints:
    primary key (country, id)
)
partition by list(country);

create table customers_americas
	partition of customers
	for values in ('US', 'CANADA');

create table customers_asia
	partition of customers
  for values in ('INDIA', 'CHINA', 'JAPAN');
```


### Hash partitioning

You can use hash partitioning to evenly distribute data.

In this example, the **`products`** table is partitioned into two partitions: `products_one` and `products_two`. The data is distributed across these partitions using a hash function:

```sql
create table products (
    id bigint generated by default as identity,
    name text,
    category text,
    price bigint
)
partition by hash (id);

create table products_one
	partition of products
  for values with (modulus 2, remainder 1);

create table products_two
	partition of products
  for values with (modulus 2, remainder 0);
```



## Other tools

There are several other tools available for Postgres partitioning, most notably [pg\_partman](https://github.com/pgpartman/pg_partman). Native partitioning was introduced in Postgres 10 and is generally thought to have better performance.



# Connecting with pgAdmin




## What is pgAdmin?

[`pgAdmin`](https://www.pgadmin.org/) is a GUI tool for managing Postgres databases. You can use it to connect to your database via SSL.



## Connecting pgAdmin with your Postgres database

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Register">
      Register a new Postgres server.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Image
        alt="Register a new postgres server."
        src={{
          dark: '/docs/img/guides/database/connecting-to-postgres/pgadmin/register-server-pgAdmin.png?v=2',
          light:
            '/docs/img/guides/database/connecting-to-postgres/pgadmin/register-server-pgAdmin--light.png',
        }}
      />
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Name">
      Name your server.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![Name Postgres Server.](/docs/img/guides/database/connecting-to-postgres/pgadmin/name-pg-server.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Connect">
      Add the connection info. Click the "Connect" button at the top of the page to open the connect Modal. Scroll down to "session pooler", click "view parameters" to toggle the parameters menu open and copy your connection parameters. Fill in your Database password that you made when creating your project (It can be reset in Database Settings above if you don't have it).
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![Add Connection Info.](/docs/img/guides/database/connecting-to-postgres/pgadmin/add-pg-server-conn-info.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="SSL">
      Download your SSL certificate from Dashboard's [`Database Settings`](/dashboard/project/_/database/settings).

      In pgAdmin, navigate to the Parameters tab and select connection parameter as Root Certificate. Next navigate to the Root certificate input, it will open up a file-picker modal. Select the certificate you downloaded earlier and save the server details. pgAdmin should now be able to connect to your Postgres via SSL.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ![Add Connection Info.](/docs/img/guides/database/connecting-to-postgres/pgadmin/database-settings-host.png)
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Why connect to pgAdmin

Connecting your Postgres instance to `pgAdmin` gives you a free, cross-platform GUI that makes tasks such as browsing objects, writing queries with autocomplete, running backups, and monitoring performance much faster and safer than using `psql` alone.

It acts as a single control panel where you can manage multiple servers, inspect locks and slow queries in real time, and perform maintenance operations with a click.

For scripted migrations or ultra-light remote work you’ll still lean on plain SQL or CLI tools, but most teams find `pgAdmin` invaluable for exploration and routine administration.



# Postgres.js



### Connecting with Postgres.js

[Postgres.js](https://github.com/porsager/postgres) is a full-featured Postgres client for Node.js and Deno.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Install">
      Install Postgres.js and related dependencies.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```shell
      npm i postgres
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Connect">
      Create a `db.js` file with the connection details.

      To get your connection details, go to the [**Connect** panel](/dashboard/project/_?showConnect=true). Choose [**Transaction pooler**](/dashboard/project/_?showConnect=true\&method=transaction) if you're on a platform with transient connections, such as a serverless function, and [**Session pooler**](/dashboard/project/_?showConnect=true\&method=session) if you have a long-lived connection. Copy the URI and save it as the environment variable `DATABASE_URL`.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts
      // db.js
      import postgres from 'postgres'

      const connectionString = process.env.DATABASE_URL
      const sql = postgres(connectionString)

      export default sql
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Execute commands">
      Use the connection to execute commands.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts
      import sql from './db.js'

      async function getUsersOver(age) {
        const users = await sql`
          select name, age
          from users
          where age > ${ age }
        `
        // users = Result [{ name: "Walter", age: 80 }, { name: 'Murray', age: 68 }, ...]
        return users
      }
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Prisma



This quickly shows how to connect your Prisma application to Supabase Postgres. If you encounter any problems, reference the [Prisma troubleshooting docs](/docs/guides/database/prisma/prisma-troubleshooting).

<Admonition type="note">
  If you plan to solely use Prisma instead of the Supabase Data API (PostgREST), turn it off in the [API Settings](/dashboard/project/_/settings/api).
</Admonition>

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a custom user for Prisma">
      *   In the [SQL Editor](/dashboard/project/_/sql/new), create a Prisma DB user with full privileges on the public schema.
      *   This gives you better control over Prisma's access and makes it easier to monitor using Supabase tools like the [Query Performance Dashboard](/dashboard/project/_/advisors/query-performance) and [Log Explorer](/dashboard/project/_/logs/explorer).

      <Admonition type="note" label="password manager">
        For security, consider using a [password generator](https://bitwarden.com/password-generator/) for the Prisma role.
      </Admonition>
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      -- Create custom user
      create user "prisma" with password 'custom_password' bypassrls createdb;

      -- extend prisma's privileges to postgres (necessary to view changes in Dashboard)
      grant "prisma" to "postgres";

      -- Grant it necessary permissions over the relevant schemas (public)
      grant usage on schema public to prisma;
      grant create on schema public to prisma;
      grant all on all tables in schema public to prisma;
      grant all on all routines in schema public to prisma;
      grant all on all sequences in schema public to prisma;
      alter default privileges for role postgres in schema public grant all on tables to prisma;
      alter default privileges for role postgres in schema public grant all on routines to prisma;
      alter default privileges for role postgres in schema public grant all on sequences to prisma;
      ```

      ```sql
      -- alter prisma password if needed
      alter user "prisma" with password 'new_password';
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Create a Prisma Project">
      Create a new Prisma Project on your computer
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      Create a new directory

      ```bash Terminal
      mkdir hello-prisma
      cd hello-prisma
      ```

      Initiate a new Prisma project

      <Tabs scrollable size="small" type="underlined" defaultActiveId="npm_initiate" queryGroup="initiate">
        <TabPanel id="npm_initiate" label="npm">
          ```bash
          npm init -y
          npm install prisma typescript ts-node @types/node --save-dev

          npx tsc --init

          npx prisma init
          ```
        </TabPanel>

        <TabPanel id="pnpm_initiate" label="pnpm">
          ```bash
          pnpm init -y
          pnpm install prisma typescript ts-node @types/node --save-dev

          pnpx tsc --init

          pnpx prisma init
          ```
        </TabPanel>

        <TabPanel id="yarn_initiate" label="yarn">
          ```bash
          yarn init -y
          yarn add prisma typescript ts-node @types/node --save-dev

          npx tsc --init

          npx prisma init
          ```
        </TabPanel>

        <TabPanel id="bun_initiate" label="bun">
          ```bash
          bun init -y
          bun install prisma typescript ts-node @types/node --save-dev

          bunx tsc --init

          bunx prisma init
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={3}>
    <StepHikeCompact.Details title="Add your connection information to your .env file">
      *   On your project dashboard, click [Connect](/dashboard/project/_?showConnect=true)
      *   Find your Supavisor Session pooler string. It should end with 5432. It will be used in your `.env` file.

      <Admonition type="note">
        If you're in an [IPv6 environment](https://github.com/orgs/supabase/discussions/27034) or have the IPv4 Add-On, you can use the direct connection string instead of Supavisor in Session mode.
      </Admonition>

      *   If you plan on deploying Prisma to a serverless or auto-scaling environment, you'll also need your Supavisor transaction mode string.
      *   The string is identical to the session mode string but uses port 6543 at the end.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs>
        <TabPanel id="serverful" label="server-based deployments">
          In your .env file, set the DATABASE\_URL variable to your connection string

          ```text .env
          # Used for Prisma Migrations and within your application
          DATABASE_URL="postgres://[DB-USER].[PROJECT-REF]:[PRISMA-PASSWORD]@[DB-REGION].pooler.supabase.com:5432/postgres"
          ```

          Change your string's `[DB-USER]` to `prisma` and add the password you created in step 1

          ```md
          postgres://prisma.[PROJECT-REF]...
          ```
        </TabPanel>

        <TabPanel id="serverless" label="serverless deployments">
          Assign the connection string for Supavisor Transaction Mode (using port 6543) to the DATABASE\_URL variable in your .env file. Make sure to append "pgbouncer=true" to the end of the string to work with Supavisor.

          Next, create a DIRECT\_URL variable in your .env file and assign the connection string that ends with port 5432 to it.

          ```text .env # Used in your application (use transaction mode)
          DATABASE_URL="postgres://[DB-USER].[PROJECT-REF]:[PRISMA-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres?pgbouncer=true"

          # Used for Prisma Migrations (use session mode or direct connection)
          DIRECT_URL="postgres://[DB-USER].[PROJECT-REF]:[PRISMA-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
          ```

          Change both your strings' `[DB-USER]` to `prisma` and then add the password created in step 1

          ```md
          postgres://prisma.[PROJECT-REF]...
          ```

          In your schema.prisma file, edit your `datasource db` configs to reference your DIRECT\_URL

          ```text schema.prisma
          datasource db {
            provider  = "postgresql"
            url       = env("DATABASE_URL")
            directUrl = env("DIRECT_URL")
          }
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={4}>
    <StepHikeCompact.Details title="Create your migrations">
      If you have already modified your Supabase database, synchronize it with your migration file. Otherwise create new tables for your database
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs>
        <TabPanel id="new-projects" label="New Projects">
          Create new tables in your prisma.schema file

          ```ts prisma/schema.prisma
          model Post {
            id        Int     @id @default(autoincrement())
            title     String
            content   String?
            published Boolean @default(false)
            author    User?   @relation(fields: [authorId], references: [id])
            authorId  Int?
          }

          model User {
            id    Int     @id @default(autoincrement())
            email String  @unique
            name  String?
            posts Post[]
          }
          ```

          commit your migration

          <Tabs scrollable size="small" type="underlined" defaultActiveId="npm_migrate" queryGroup="migrate">
            <TabPanel id="npm_migrate" label="npm">
              ```bash
              npx prisma migrate dev --name first_prisma_migration

              ```
            </TabPanel>

            <TabPanel id="pnpm_migrate" label="pnpm">
              ```bash
              pnpx prisma migrate dev --name first_prisma_migration

              ```
            </TabPanel>

            <TabPanel id="yarn_migrate" label="yarn">
              ```bash
              npx prisma migrate dev --name first_prisma_migration

              ```
            </TabPanel>

            <TabPanel id="bun_migrate" label="bun">
              ```bash
              bunx prisma migrate dev --name first_prisma_migration

              ```
            </TabPanel>
          </Tabs>
        </TabPanel>

        <TabPanel id="established-projects" label="Populated Projects">
          Synchronize changes from your project:

          <Tabs scrollable size="small" type="underlined" defaultActiveId="npm_sync" queryGroup="sync">
            <TabPanel id="npm_sync" label="npm">
              ```bash
              npx prisma db pull
              ```

              Create a migration file

              ```bash
              mkdir -p prisma/migrations/0_init_supabase
              ```

              Synchronize the migrations

              ```bash
                npx prisma migrate diff \
                --from-empty \
                --to-schema-datamodel prisma/schema.prisma \
                --script > prisma/migrations/0_init_supabase/migration.sql
              ```

              <Admonition type="tip" label="conflict management">
                If there are any conflicts, reference [Prisma's official doc](https://www.prisma.io/docs/orm/prisma-migrate/getting-started#work-around-features-not-supported-by-prisma-schema-language) or the [trouble shooting guide](/docs/guides/database/prisma/prisma-troubleshooting) for more details
              </Admonition>

              ```bash
              npx prisma migrate resolve --applied 0_init_supabase
              ```
            </TabPanel>

            <TabPanel id="pnpm_sync" label="pnpm">
              ```bash
              pnpx prisma db pull
              ```

              Create a migration file

              ```bash
              mkdir -p prisma/migrations/0_init_supabase
              ```

              Synchronize the migrations

              ```bash
                pnpx prisma migrate diff \
                --from-empty \
                --to-schema-datamodel prisma/schema.prisma \
                --script > prisma/migrations/0_init_supabase/migration.sql
              ```

              <Admonition type="note" label="conflict management">
                If there are any conflicts, reference [Prisma's official doc](https://www.prisma.io/docs/orm/prisma-migrate/getting-started#work-around-features-not-supported-by-prisma-schema-language) or the [trouble shooting guide](/docs/guides/database/prisma/prisma-troubleshooting) for more details
              </Admonition>

              ```bash
              pnpx prisma migrate resolve --applied 0_init_supabase
              ```
            </TabPanel>

            <TabPanel id="yarn_sync" label="yarn">
              ```bash
              npx prisma db pull
              ```

              Create a migration file

              ```bash
              mkdir -p prisma/migrations/0_init_supabase
              ```

              Synchronize the migrations

              ```bash
                npx prisma migrate diff \
                --from-empty \
                --to-schema-datamodel prisma/schema.prisma \
                --script > prisma/migrations/0_init_supabase/migration.sql
              ```

              <Admonition type="note" label="conflict management">
                If there are any conflicts, reference [Prisma's official doc](https://www.prisma.io/docs/orm/prisma-migrate/getting-started#work-around-features-not-supported-by-prisma-schema-language) or the [trouble shooting guide](/docs/guides/database/prisma/prisma-troubleshooting) for more details
              </Admonition>

              ```bash
              npx prisma migrate resolve --applied 0_init_supabase
              ```
            </TabPanel>

            <TabPanel id="bun_sync" label="bun">
              ```bash
              bunx prisma db pull
              ```

              Create a migration file

              ```bash
              mkdir -p prisma/migrations/0_init_supabase
              ```

              Synchronize the migrations

              ```bash
                bunx prisma migrate diff \
                --from-empty \
                --to-schema-datamodel prisma/schema.prisma \
                --script > prisma/migrations/0_init_supabase/migration.sql
              ```

              <Admonition type="note" label="conflict management">
                If there are any conflicts, reference [Prisma's official doc](https://www.prisma.io/docs/orm/prisma-migrate/getting-started#work-around-features-not-supported-by-prisma-schema-language) or the [trouble shooting guide](/docs/guides/database/prisma-troubleshooting) for more details
              </Admonition>

              ```bash
              bunx prisma migrate resolve --applied 0_init_supabase
              ```
            </TabPanel>
          </Tabs>
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={5}>
    <StepHikeCompact.Details title="Install the prisma client">
      Install the Prisma client and generate its model
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      <Tabs scrollable size="small" type="underlined" defaultActiveId="npm_client" queryGroup="client">
        <TabPanel id="npm_client" label="npm">
          ```sh
          npm install @prisma/client
          npx prisma generate
          ```
        </TabPanel>

        <TabPanel id="pnpm_client" label="pnpm">
          ```sh
          pnpm install @prisma/client
          pnpx prisma generate
          ```
        </TabPanel>

        <TabPanel id="yarn_client" label="yarn">
          ```sh
          yarn add @prisma/client
          npx prisma generate
          ```
        </TabPanel>

        <TabPanel id="bun_client" label="bun">
          ```sh
          bun install @prisma/client
          bunx prisma generate
          ```
        </TabPanel>
      </Tabs>
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>

  <StepHikeCompact.Step step={6}>
    <StepHikeCompact.Details title="Test your API">
      Create a index.ts file and run it to test your connection
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```ts index.ts
      const { PrismaClient } = require('@prisma/client');

      const prisma = new PrismaClient();

      async function main() {
        //change to reference a table in your schema
        const val = await prisma.<SOME_TABLE_NAME>.findMany({
          take: 10,
        });
        console.log(val);
      }

      main()
        .then(async () => {
          await prisma.$disconnect();
        })
        .catch(async (e) => {
          console.error(e);
          await prisma.$disconnect();
        process.exit(1);
      });

      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



# Connecting with PSQL



[`psql`](https://www.postgresql.org/docs/current/app-psql.html) is a command-line tool that comes with Postgres.



## Connecting with SSL

You should connect to your database using SSL wherever possible, to prevent snooping and man-in-the-middle attacks.

You can obtain your connection info and Server root certificate from your application's dashboard:

![Connection Info and Certificate.](/docs/img/database/database-settings-ssl.png)

Download your [SSL certificate](#connecting-with-ssl) to `/path/to/prod-supabase.cer`.

Find your connection settings. Go to the project [**Connect** panel](/dashboard/project/_?showConnect=true\&method=session) and copy the URL from the `Session pooler` section, and copy the parameters into the connection string:

```shell
psql "sslmode=verify-full sslrootcert=/path/to/prod-supabase.cer host=[CLOUD_PROVIDER]-0-[REGION].pooler.supabase.com dbname=postgres user=postgres.[PROJECT_REF]"
```



# Query Optimization

Choosing indexes to improve your query performance.

When working with Postgres, or any relational database, indexing is key to improving query performance. Aligning indexes with common query patterns can speed up data retrieval by an order of magnitude.

This guide is intended to:

*   help identify parts of a query that have the potential to be improved by indexes
*   introduce tooling to help identify useful indexes

This is not a comprehensive resource, but rather a helpful starting point for your optimization journey.

If you're new to query optimization, you may be interested in [`index_advisor`](/docs/guides/database/extensions/index_advisor), our tool for automatically detecting indexes that improve performance on a given query.



## Example query

Consider the following example query that retrieves customer names and purchase dates from two tables:

```sql
select
  a.name,
  b.date_of_purchase
from
  customers as a
  join orders as b on a.id = b.customer_id
where a.sign_up_date > '2023-01-01' and b.status = 'shipped'
order by b.date_of_purchase
limit 10;
```

In this query, there are several parts that indexes could likely help in optimizing the performance:


### `where` clause:

The `where` clause filters rows based on certain conditions, and indexing the columns involved can improve this process:

*   `a.sign_up_date`: If filtering by `sign_up_date` is common, indexing this column can speed up the query.
*   `b.status`: Indexing the status may be beneficial if the column has diverse values.

```sql
create index idx_customers_sign_up_date on customers (sign_up_date);

create index idx_orders_status on orders (status);
```


### `join` columns

Indexes on the columns used for joining tables can help Postgres avoid scanning tables in their entirety when connecting tables.

*   Indexing `a.id` and `b.customer_id` would likely improve the performance of the join in this query.
*   Note that if `a.id` is the primary key of the `customers` table it is already indexed

```sql
create index idx_orders_customer_id on orders (customer_id);
```


### `order by` clause

Sorting can also be optimized by indexing:

*   An index on `b.date_of_purchase` can improve the sorting process, and is particularly beneficial when a subset of rows is being returned with a `limit` clause.

```sql
create index idx_orders_date_of_purchase on orders (date_of_purchase);
```



## Key concepts

Here are some concepts and tools to keep in mind to help you identify the best index for the job, and measure the impact that your index had:


### Analyze the query plan

Use the `explain` command to understand the query's execution. Look for slow parts, such as Sequential Scans or high cost numbers. If creating an index does not reduce the cost of the query plan, remove it.

For example:

```sql
explain select * from customers where sign_up_date > 25;
```


### Use appropriate index types

Postgres offers various index types like [B-tree, Hash, GIN, etc](https://www.postgresql.org/docs/current/indexes-types.html). Select the type that best suits your data and query pattern. Using the right index type can make a significant difference. For example, using a BRIN index on a field that always increases and lives within a table that updates infrequently - like `created_at` on an `orders` table - routinely results in indexes that are +10x smaller than the equivalent default B-tree index. That translates into better scalability.

```sql
create index idx_orders_created_at ON customers using brin(created_at);
```


### Partial indexes

For queries that frequently target a subset of data, a partial index could be faster and smaller than indexing the entire column. A partial index contains a `where` clause to filter the values included in the index. Note that a query's `where` clause must match the index for it to be used.

```sql
create index idx_orders_status on orders (status)
where status = 'shipped';
```


### Composite indexes

If filtering or joining on multiple columns, a composite index prevents Postgres from referring to multiple indexes when identifying the relevant rows.

```sql
create index idx_customers_sign_up_date_priority on customers (sign_up_date, priority);
```


### Over-Indexing

Avoid the urge to index columns you operate on infrequently. While indexes can speed up reads, they also slow down writes, so it's important to balance those factors when making indexing decisions.


### Statistics

Postgres maintains a set of statistics about the contents of your tables. Those statistics are used by the query planner to decide when it's is more efficient to use an index vs scanning the entire table. If the collected statistics drift too far from reality, the query planner may make poor decisions. To avoid this risk, you can periodically `analyze` tables.

```sql
analyze customers;
```

***

By following this guide, you'll be able to discern where indexes can optimize queries and enhance your Postgres performance. Remember that each database is unique, so always consider the specific context and use case of your queries.



# Replication and change data capture



Replication is the process of copying changes from your database to another location. It's also referred to as change data capture (CDC): capturing all the changes that occur to your data.



## Use cases

You might use replication for:

*   **Analytics and Data Warehousing**: Replicate your operational database to analytics platforms like BigQuery for complex analysis without impacting your application's performance.
*   **Data Integration**: Keep your data synchronized across different systems and services in your tech stack.
*   **Backup and Disaster Recovery**: Maintain up-to-date copies of your data in different locations.
*   **Read Scaling**: Distribute read operations across multiple database instances to improve performance.



## Replication in Postgres

Postgres comes with built-in support for replication via publications and replication slots. Refer to the [Concepts and terms](#concepts-and-terms) section to learn how replication works.



## Setting up and monitoring replication in Supabase

*   [Setting up replication](/docs/guides/database/replication/setting-up-replication)
*   [Monitoring replication](/docs/guides/database/replication/monitoring-replication)

<Admonition type="tip">
  If you want to set up a read replica, see [Read Replicas](/docs/guides/platform/read-replicas) instead. If you want to sync your data in real time to a client such as a browser or mobile app, see [Realtime](/docs/guides/realtime) instead. For configuring replication to an ETL destination, use the [Dashboard](/dashboard/project/_/database/replication).
</Admonition>



## Concepts and terms


### Write-Ahead Log (WAL)

Postgres uses a system called the Write-Ahead Log (WAL) to manage changes to the database. As you make changes, they are appended to the WAL (which is a series of files (also called "segments"), where the file size can be specified). Once one segment is full, Postgres will start appending to a new segment. After a period of time, a checkpoint occurs and Postgres synchronizes the WAL with your database. Once the checkpoint is complete, then the WAL files can be removed from disk and free up space.


### Logical replication and WAL

Logical replication is a method of replication where Postgres uses the WAL files and transmit those changes to another Postgres database, or a system that supports reading WAL files.


### LSN

LSN is a Log Sequence Number that is used to identify the position of a WAL file in the WAL directory. It is often used to determine the progress of replication in subscribers and calculate the lag of a replication slot.



## Logical replication architecture

When setting up logical replication, three key components are involved:

*   `publication` - A set of tables on your primary database that will be `published`
*   `replication slot` - A slot used for replicating the data from a single publication. The slot, when created, will specify the output format of the changes
*   `subscription` - A subscription is created from an external system (i.e. another Postgres database) and must specify the name of the `publication`. If you do not specify a replication slot, one is automatically created



## Logical replication output format

Logical replication is typically output in 2 forms, `pgoutput` and `wal2json`. The output method is how Postgres sends changes to any active replication slot.



## Logical replication configuration

When using logical replication, Postgres is then configured to keep WAL files around for longer than it needs them. If the files are removed too quickly, then your `replication slot` will become inactive and, if the database receives a large number of changes in a short time, then the `replication slot` can become lost as it was not able to keep up.

In order to mitigate this, Postgres has many options and settings that can be [tweaked](/docs/guides/database/custom-postgres-config) to manage the WAL usage effectively. Not all of these settings are user configurable as they can impact the stability of your database. For those that are, these should be considered as advanced configuration and not changed without understanding that they can cause additional disk space and resources to be used, as well as incur additional costs.

| Setting                                                                                  | Description                                            | User-facing | Default |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- | ------- |
| [`max_replication_slots`](https://postgresqlco.nf/doc/en/param/max_replication_slots/)   | Max count of replication slots allowed                 | No          |         |
| [`wal_keep_size`](https://postgresqlco.nf/doc/en/param/wal_keep_size/)                   | Minimum size of WAL files to keep for replication      | No          |         |
| [`max_slot_wal_keep_size`](https://postgresqlco.nf/doc/en/param/max_slot_wal_keep_size/) | Max WAL size that can be reserved by replication slots | No          |         |
| [`checkpoint_timeout`](https://postgresqlco.nf/doc/en/param/checkpoint_timeout/)         | Max time between WAL checkpoints                       | No          |         |



---
**Navigation:** [← Previous](./22-connection-management.md) | [Index](./index.md) | [Next →](./24-securing-your-data.md)
