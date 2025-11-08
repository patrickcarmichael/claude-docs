**Navigation:** [← Previous](./23-debugging-and-monitoring.md) | [Index](./index.md) | [Next →](./25-event-triggers.md)

# Securing your data



Supabase helps you control access to your data. With access policies, you can protect sensitive data and make sure users only access what they're allowed to see.



## Connecting your app securely

Supabase allows you to access your database using the auto-generated [Data APIs](/docs/guides/database/connecting-to-postgres#data-apis). This speeds up the process of building web apps, since you don't need to write your own backend services to pass database queries and results back and forth.

You can keep your data secure while accessing the Data APIs from the frontend, so long as you:

*   Turn on [Row Level Security](/docs/guides/database/postgres/row-level-security) (RLS) for your tables
*   Use your Supabase **anon key** when you create a Supabase client

Your anon key is safe to expose with RLS enabled, because row access permission is checked against your access policies and the user's [JSON Web Token (JWT)](/docs/learn/auth-deep-dive/auth-deep-dive-jwts). The JWT is automatically sent by the Supabase client libraries if the user is logged in using Supabase Auth.

<Admonition type="danger" label="Never expose your service role key on the frontend">
  Unlike your anon key, your **service role key** is **never** safe to expose because it bypasses RLS. Only use your service role key on the backend. Treat it as a secret (for example, import it as a sensitive environment variable instead of hardcoding it).
</Admonition>



## More information

Supabase and Postgres provide you with multiple ways to manage security, including but not limited to Row Level Security. See the Access and Security pages for more information:

*   [Row Level Security](/docs/guides/database/postgres/row-level-security)
*   [Column Level Security](/docs/guides/database/postgres/column-level-security)
*   [Hardening the Data API](/docs/guides/database/hardening-data-api)
*   [Managing Postgres roles](/docs/guides/database/postgres/roles)
*   [Managing secrets with Vault](/docs/guides/database/vault)



# Supavisor

Troubleshooting Supavisor errors

Supavisor logs are available under [Pooler Logs](/dashboard/project/_/logs/pooler-logs) in the Dashboard. The following are common errors and their solutions:

| Error Type                                                                | Description                                                                                                                                                                                                                                                                 | Resolution Link                                                                     |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Max client connections reached                                            | This error happens when the number of connections to Supavisor is more than [the allowed limit of your compute add-on](/docs/guides/platform/compute-add-ons).                                                                                                              | Follow this [guide](https://github.com/orgs/supabase/discussions/22305) to resolve. |
| Connection failed `{:error, :eaddrnotavail}` to 'db.xxx.supabase.co':5432 | Supavisor cannot connect to the customer database. This is usually caused if the target database is unable to respond.                                                                                                                                                      | N/A                                                                                 |
| Connection failed `{:error, :nxdomain}` to 'db.xxx.supabase.co':5432      | Supavisor cannot connect to the customer database. This is usually caused if the target database is unable to respond.                                                                                                                                                      | N/A                                                                                 |
| Connection closed when state was authentication                           | This error happens when either the database doesn’t exist or if the user doesn't have the right credentials.                                                                                                                                                                | N/A                                                                                 |
| Subscribe error: `{:error, :worker_not_found}`                            | This log event is emitted when the client tries to connect to the database, but Supavisor does not have the necessary information to route the connection. Try reconnecting to the database as it can take some time for the project information to propagate to Supavisor. | N/A                                                                                 |
| Subscribe error: `{:error, {:badrpc, {:error, {:erpc, :timeout}}}}`       | This is a timeout error when the communication between different Supavisor nodes takes longer than expected. Try reconnecting to the database.                                                                                                                              | N/A                                                                                 |
| Terminating with reason :client\_termination when state was :busy         | This error happens when the client terminates the connection before the connection with the database is completed.                                                                                                                                                          | N/A                                                                                 |
| Error: received invalid response to GSSAPI negotiation: S                 | This error happens due to `gssencmode` parameter not set to disabled.                                                                                                                                                                                                       | Follow this [guide](https://github.com/orgs/supabase/discussions/30173) to resolve. |



# Tables and Data



Tables are where you store your data.

Tables are similar to excel spreadsheets. They contain columns and rows.
For example, this table has 3 "columns" (`id`, `name`, `description`) and 4 "rows" of data:

{/* supa-mdx-lint-disable Rule003Spelling */}

| `id` | `name`               | `description`                                                                                                                                                 |
| ---- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | The Phantom Menace   | Two Jedi escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force.                                             |
| 2    | Attack of the Clones | Ten years after the invasion of Naboo, the Galactic Republic is facing a Separatist movement.                                                                 |
| 3    | Revenge of the Sith  | As Obi-Wan pursues a new threat, Anakin acts as a double agent between the Jedi Council and Palpatine and is lured into a sinister plan to rule the galaxy.   |
| 4    | Star Wars            | Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station. |

{/* supa-mdx-lint-enable Rule003Spelling */}

There are a few important differences from a spreadsheet, but it's a good starting point if you're new to Relational databases.



## Creating tables

When creating a table, it's best practice to add columns at the same time.

<Image
  alt="Tables and columns"
  zoomable
  src={{
    dark: '/docs/img/database/managing-tables/creating-tables.png',
    light: '/docs/img/database/managing-tables/creating-tables--light.png',
  }}
/>

You must define the "data type" of each column when it is created. You can add and remove columns at any time after creating a table.

Supabase provides several options for creating tables. You can use the Dashboard or create them directly using SQL.
We provide a SQL editor within the Dashboard, or you can [connect](../../guides/database/connecting-to-postgres) to your database
and run the SQL queries yourself.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    <video width="99%" muted playsInline controls={true}>
      <source src="https://xguihxuzqibwxjnimxev.supabase.co/storage/v1/object/public/videos/docs/api/api-create-table-sm.mp4" type="video/mp4" />
    </video>

    1.  Go to the [Table Editor](/dashboard/project/_/editor) page in the Dashboard.
    2.  Click **New Table** and create a table with the name `todos`.
    3.  Click **Save**.
    4.  Click **New Column** and create a column with the name `task` and type `text`.
    5.  Click **Save**.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create table movies (
      id bigint generated by default as identity primary key,
      name text,
      description text
    );
    ```
  </TabPanel>
</Tabs>

<Admonition type="note">
  When naming tables, use lowercase and underscores instead of spaces (e.g., `table_name`, not `Table Name`).
</Admonition>



## Columns

You must define the "data type" when you create a column.


### Data types

Every column is a predefined type. Postgres provides many [default types](https://www.postgresql.org/docs/current/datatype.html), and you can even design your own (or use extensions) if the default types don't fit your needs. You can use any data type that Postgres supports via the SQL editor. We only support a subset of these in the Table Editor in an effort to keep the experience simple for people with less experience with databases.

<details>
  <summary>Show/Hide default data types</summary>

  | `Name`                            | `Aliases`     | `Description`                                                     |
  | --------------------------------- | ------------- | ----------------------------------------------------------------- |
  | `bigint`                          | `int8`        | signed eight-byte integer                                         |
  | `bigserial`                       | `serial8`     | autoincrementing eight-byte integer                               |
  | `bit`                             |               | fixed-length bit string                                           |
  | `bit varying`                     | `varbit`      | variable-length bit string                                        |
  | `boolean`                         | `bool`        | logical Boolean (true/false)                                      |
  | `box`                             |               | rectangular box on a plane                                        |
  | `bytea`                           |               | binary data (“byte array”)                                        |
  | `character`                       | `char`        | fixed-length character string                                     |
  | `character varying`               | `varchar`     | variable-length character string                                  |
  | `cidr`                            |               | IPv4 or IPv6 network address                                      |
  | `circle`                          |               | circle on a plane                                                 |
  | `date`                            |               | calendar date (year, month, day)                                  |
  | `double precision`                | `float8`      | double precision floating-point number (8 bytes)                  |
  | `inet`                            |               | IPv4 or IPv6 host address                                         |
  | `integer`                         | `int`, `int4` | signed four-byte integer                                          |
  | `interval [ fields ]`             |               | time span                                                         |
  | `json`                            |               | textual JSON data                                                 |
  | `jsonb`                           |               | binary JSON data, decomposed                                      |
  | `line`                            |               | infinite line on a plane                                          |
  | `lseg`                            |               | line segment on a plane                                           |
  | `macaddr`                         |               | MAC (Media Access Control) address                                |
  | `macaddr8`                        |               | MAC (Media Access Control) address (EUI-64 format)                |
  | `money`                           |               | currency amount                                                   |
  | `numeric`                         | `decimal`     | exact numeric of selectable precision                             |
  | `path`                            |               | geometric path on a plane                                         |
  | `pg_lsn`                          |               | Postgres Log Sequence Number                                      |
  | `pg_snapshot`                     |               | user-level transaction ID snapshot                                |
  | `point`                           |               | geometric point on a plane                                        |
  | `polygon`                         |               | closed geometric path on a plane                                  |
  | `real`                            | `float4`      | single precision floating-point number (4 bytes)                  |
  | `smallint`                        | `int2`        | signed two-byte integer                                           |
  | `smallserial`                     | `serial2`     | autoincrementing two-byte integer                                 |
  | `serial`                          | `serial4`     | autoincrementing four-byte integer                                |
  | `text`                            |               | variable-length character string                                  |
  | `time [ without time zone ]`      |               | time of day (no time zone)                                        |
  | `time with time zone`             | `timetz`      | time of day, including time zone                                  |
  | `timestamp [ without time zone ]` |               | date and time (no time zone)                                      |
  | `timestamp with time zone`        | `timestamptz` | date and time, including time zone                                |
  | `tsquery`                         |               | text search query                                                 |
  | `tsvector`                        |               | text search document                                              |
  | `txid_snapshot`                   |               | user-level transaction ID snapshot (deprecated; see pg\_snapshot) |
  | `uuid`                            |               | universally unique identifier                                     |
  | `xml`                             |               | XML data                                                          |
</details>

<br />

You can "cast" columns from one type to another, however there can be some incompatibilities between types.
For example, if you cast a `timestamp` to a `date`, you will lose all the time information that was previously saved.


### Primary keys

A table can have a "primary key" - a unique identifier for every row of data. A few tips for Primary Keys:

*   It's recommended to create a Primary Key for every table in your database.
*   You can use any column as a primary key, as long as it is unique for every row.
*   It's common to use a `uuid` type or a numbered `identity` column as your primary key.

```sql
create table movies (
  id bigint generated always as identity primary key
);
```

In the example above, we have:

1.  created a column called `id`
2.  assigned the data type `bigint`
3.  instructed the database that this should be `generated always as identity`, which means that Postgres will automatically assign a unique number to this column.
4.  Because it's unique, we can also use it as our `primary key`.

We could also use `generated by default as identity`, which would allow us to insert our own unique values.

```sql
create table movies (
  id bigint generated by default as identity primary key
);
```



## Loading data

There are several ways to load data in Supabase. You can load data directly into the database or using the [APIs](../../guides/database/api).
Use the "Bulk Loading" instructions if you are loading large data sets.


### Basic data loading

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="language">
  <TabPanel id="sql" label="SQL">
    ```sql
    insert into movies
      (name, description)
    values
      (
        'The Empire Strikes Back',
        'After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.'
      ),
      (
        'Return of the Jedi',
        'After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star.'
      );
    ```
  </TabPanel>

  <TabPanel id="js" label="JavaScript">
    ```js
    const { data, error } = await supabase.from('movies').insert([
      {
        name: 'The Empire Strikes Back',
        description:
          'After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.',
      },
      {
        name: 'Return of the Jedi',
        description:
          'After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star.',
      },
    ])
    ```
  </TabPanel>

  <TabPanel id="dart" label="Dart">
    ```dart
    await supabase
      .from('movies')
      .insert([{
        name: 'The Empire Strikes Back',
        description: 'After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.'
      }, {
        name: 'Return of the Jedi',
        description: 'After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star.'
      }]);
    ```
  </TabPanel>

  <TabPanel id="swift" label="Swift">
    ```swift
    try await supabase.from("movies")
      .insert(
        [
          [
            "name": "The Empire Strikes Back",
            "description":
              "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda.",
          ],
          [
            "name": "Return of the Jedi",
            "description":
              "After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star.",
          ],
        ]
      )
      .execute()
    ```
  </TabPanel>

  <TabPanel id="python" label="Python">
    ```python
    client.from_("movies").insert([
        {
            "name": "The Empire Strikes Back",
            "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda."
        },
        {
            "name": "Return of the Jedi",
            "description": "After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star."
        }
    ]).execute()
    ```
  </TabPanel>

  <TabPanel id="kotlin" label="Kotlin">
    ```kotlin
    @Serializable
    data class Movie(
        val name: String,
        val description: String
    )
    ```

    ```kotlin
    supabase
        .from("movies")
        .insert(listOf(
            Movie("The Empire Strikes Back", "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda."),
            Movie("Return of the Jedi", "After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star."),
        ))
    ```
  </TabPanel>
</Tabs>


### Bulk data loading

When inserting large data sets it's best to use PostgreSQL's [COPY](https://www.postgresql.org/docs/current/sql-copy.html) command.
This loads data directly from a file into a table. There are several file formats available for copying data: text, CSV, binary, JSON, etc.

For example, if you wanted to load a CSV file into your movies table:

```text ./movies.csv
"The Empire Strikes Back", "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda."
"Return of the Jedi", "After a daring mission to rescue Han Solo from Jabba the Hutt, the Rebels dispatch to Endor to destroy the second Death Star."
```

You would [connect](../../guides/database/connecting-to-postgres#direct-connections) to your database directly and load the file with the COPY command:

```bash
psql -h DATABASE_URL -p 5432 -d postgres -U postgres \
  -c "\COPY movies FROM './movies.csv';"
```

Additionally use the `DELIMITER`, `HEADER` and `FORMAT` options as defined in the Postgres [COPY](https://www.postgresql.org/docs/current/sql-copy.html) docs.

```bash
psql -h DATABASE_URL -p 5432 -d postgres -U postgres \
  -c "\COPY movies FROM './movies.csv' WITH DELIMITER ',' CSV HEADER"
```

If you receive an error `FATAL:  password authentication failed for user "postgres"`, reset your database password in the Database Settings and try again.



## Joining tables with foreign keys

Tables can be "joined" together using Foreign Keys.

<Image
  alt="Foreign Keys"
  zoomable
  src={{
    dark: '/docs/img/database/managing-tables/joining-tables.png',
    light: '/docs/img/database/managing-tables/joining-tables--light.png',
  }}
/>

This is where the "Relational" naming comes from, as data typically forms some sort of relationship.

In our "movies" example above, we might want to add a "category" for each movie (for example, "Action", or "Documentary").
Let's create a new table called `categories` and "link" our `movies` table.

```sql
create table categories (
  id bigint generated always as identity primary key,
  name text -- category name
);

alter table movies
  add column category_id bigint references categories;
```

You can also create "many-to-many" relationships by creating a "join" table.
For example if you had the following situations:

*   You have a list of `movies`.
*   A movie can have several `actors`.
*   An `actor` can perform in several movies.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    <div className="video-container">
      <iframe src="https://www.youtube-nocookie.com/embed/TKwF3IGij5c" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
    </div>
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    create table movies (
      id bigint generated by default as identity primary key,
      name text,
      description text
    );

    create table actors (
      id bigint generated by default as identity primary key,
      name text
    );

    create table performances (
      id bigint generated by default as identity primary key,
      movie_id bigint not null references movies,
      actor_id bigint not null references actors
    );
    ```
  </TabPanel>
</Tabs>



## Schemas

Tables belong to `schemas`. Schemas are a way of organizing your tables, often for security reasons.

<Image
  alt="Schemas and tables"
  zoomable
  src={{
    dark: '/docs/img/database/managing-tables/schemas.png',
    light: '/docs/img/database/managing-tables/schemas--light.png',
  }}
/>

If you don't explicitly pass a schema when creating a table, Postgres will assume that you want to create the table in the `public` schema.

We can create schemas for organizing tables. For example, we might want a private schema which is hidden from our API:

```sql
create schema private;
```

Now we can create tables inside the `private` schema:

```sql
create table private.salaries (
  id bigint generated by default as identity primary key,
  salary bigint not null,
  actor_id bigint not null references public.actors
);
```



## Views

A View is a convenient shortcut to a query. Creating a view does not involve new tables or data. When run, an underlying query is executed, returning its results to the user.

Say we have the following tables from a database of a university:

**`students`**

{/* supa-mdx-lint-disable Rule003Spelling */}

| id | name             | type          |
| -- | ---------------- | ------------- |
| 1  | Princess Leia    | undergraduate |
| 2  | Yoda             | graduate      |
| 3  | Anakin Skywalker | graduate      |

{/* supa-mdx-lint-enable Rule003Spelling */}

**`courses`**

| id | title                    | code    |
| -- | ------------------------ | ------- |
| 1  | Introduction to Postgres | PG101   |
| 2  | Authentication Theories  | AUTH205 |
| 3  | Fundamentals of Supabase | SUP412  |

**`grades`**

| id | student\_id | course\_id | result |
| -- | ----------- | ---------- | ------ |
| 1  | 1           | 1          | B+     |
| 2  | 1           | 3          | A+     |
| 3  | 2           | 2          | A      |
| 4  | 3           | 1          | A-     |
| 5  | 3           | 2          | A      |
| 6  | 3           | 3          | B-     |

Creating a view consisting of all the three tables will look like this:

```sql
create view transcripts as
    select
        students.name,
        students.type,
        courses.title,
        courses.code,
        grades.result
    from grades
    left join students on grades.student_id = students.id
    left join courses on grades.course_id = courses.id;

grant all on table transcripts to authenticated;
```

Once done, we can now access the underlying query with:

```sql
select * from transcripts;
```


### View security

By default, views are accessed with their creator's permission ("security definer"). If a privileged role creates a view, others accessing it will use that role's elevated permissions. To enforce row level security policies, define the view with the "security invoker" modifier.

```sql
-- alter a security_definer view to be security_invoker
alter view <view name>
set (security_invoker = true);

-- create a view with the security_invoker modifier
create view <view name> with(security_invoker=true) as (
  select * from <some table>
);
```


### When to use views

Views provide several benefits:

*   Simplicity
*   Consistency
*   Logical Organization
*   Security


#### Simplicity

As a query becomes more complex, it can be a hassle to call it over and over - especially when we run it regularly. In the example above, instead of repeatedly running:

```sql
select
  students.name,
  students.type,
  courses.title,
  courses.code,
  grades.result
from
  grades
  left join students on grades.student_id = students.id
  left join courses on grades.course_id = courses.id;
```

We can run this instead:

```sql
select * from transcripts;
```

Additionally, a view behaves like a typical table. We can safely use it in table `JOIN`s or even create new views using existing views.


#### Consistency

Views ensure that the likelihood of mistakes decreases when repeatedly executing a query. In our example above, we may decide that we want to exclude the course *Introduction to Postgres*. The query would become:

```sql
select
  students.name,
  students.type,
  courses.title,
  courses.code,
  grades.result
from
  grades
  left join students on grades.student_id = students.id
  left join courses on grades.course_id = courses.id
where courses.code != 'PG101';
```

Without a view, we would need to go into every dependent query to add the new rule. This would increase in the likelihood of errors and inconsistencies, as well as introducing a lot of effort for a developer. With views, we can alter just the underlying query in the view **transcripts**. The change will be applied to all applications using this view.


#### Logical organization

With views, we can give our query a name. This is extremely useful for teams working with the same database. Instead of guessing what a query is supposed to do, a well-named view can explain it. For example, by looking at the name of the view **transcripts**, we can infer that the underlying query might involve the **students**, **courses**, and **grades** tables.


#### Security

Views can restrict the amount and type of data presented to a user. Instead of allowing a user direct access to a set of tables, we provide them a view instead. We can prevent them from reading sensitive columns by excluding them from the underlying query.


### Materialized views

A [materialized view](https://www.postgresql.org/docs/12/rules-materializedviews.html) is a form of view but it also stores the results to disk. In subsequent reads of a materialized view, the time taken to return its results would be much faster than a conventional view. This is because the data is readily available for a materialized view while the conventional view executes the underlying query each time it is called.

Using our example above, a materialized view can be created like this:

```sql
create materialized view transcripts as
  select
    students.name,
    students.type,
    courses.title,
    courses.code,
    grades.result
  from
    grades
    left join students on grades.student_id = students.id
    left join courses on grades.course_id = courses.id;
```

Reading from the materialized view is the same as a conventional view:

```sql
select * from transcripts;
```


### Refreshing materialized views

Unfortunately, there is a trade-off - data in materialized views are not always up to date. We need to refresh it regularly to prevent the data from becoming too stale. To do so:

```sql
refresh materialized view transcripts;
```

It's up to you how regularly refresh your materialized views, and it's probably different for each view depending on its use-case.


### Materialized views vs conventional views

Materialized views are useful when execution times for queries or views are too slow. These could likely occur in views or queries involving multiple tables and billions of rows. When using such a view, however, there should be tolerance towards data being outdated. Some use-cases for materialized views are internal dashboards and analytics.

Creating a materialized view is not a solution to inefficient queries. You should always seek to optimize a slow running query even if you are implementing a materialized view.



## Resources

*   [Official Docs: Create table](https://www.postgresql.org/docs/current/sql-createtable.html)
*   [Official Docs: Create view](https://www.postgresql.org/docs/12/sql-createview.html)
*   [Postgres Tutorial: Create tables](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table/)
*   [Postgres Tutorial: Add column](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-add-column/)
*   [Postgres Tutorial: Views](https://www.postgresqltutorial.com/postgresql-views/)



# Testing Your Database



To ensure that queries return the expected data, RLS policies are correctly applied and etc., we encourage you to write automated tests. There are essentially two approaches to testing:

*   Firstly, you can write tests that interface with a Supabase client instance (same way you use Supabase client in your application code) in the programming language(s) you use in your application and using your favorite testing framework.

*   Secondly, you can test through the Supabase CLI, which is a more low-level approach where you write tests in SQL.



# Testing using the Supabase CLI

You can use the Supabase CLI to test your database. The minimum required version of the CLI is [v1.11.4](https://github.com/supabase/cli/releases). To get started:

*   [Install the Supabase CLI](/docs/guides/cli) on your local machine



## Creating a test

Create a tests folder inside the `supabase` folder:

```bash
mkdir -p ./supabase/tests/database
```

Create a new file with the `.sql` extension which will contain the test.

```bash
touch ./supabase/tests/database/hello_world.test.sql
```



## Writing tests

All `sql` files use [pgTAP](/docs/guides/database/extensions/pgtap) as the test runner.

Let's write a simple test to check that our `auth.users` table has an ID column. Open `hello_world.test.sql` and add the following code:

```sql
begin;
select plan(1); -- only one statement to run

SELECT has_column(
    'auth',
    'users',
    'id',
    'id should exist'
);

select * from finish();
rollback;
```



## Running tests

To run the test, you can use:

```bash
supabase test db
```

This will produce the following output:

```bash
$ supabase test db
supabase/tests/database/hello_world.test.sql .. ok
All tests successful.
Files=1, Tests=1,  1 wallclock secs ( 0.01 usr  0.00 sys +  0.04 cusr  0.02 csys =  0.07 CPU)
Result: PASS
```



## More resources

*   [Testing RLS policies](/docs/guides/database/extensions/pgtap#testing-rls-policies)
*   [pgTAP extension](/docs/guides/database/extensions/pgtap)
*   Official [pgTAP documentation](https://pgtap.org/)



# Vault

Managing secrets in Postgres.

Vault is a Postgres extension and accompanying Supabase UI that makes it safe and easy to store encrypted secrets and other data in your database. This opens up a lot of possibilities to use Postgres in ways that go beyond what is available in a stock distribution.

Under the hood, the Vault is a table of Secrets that are stored using [Authenticated Encryption](https://en.wikipedia.org/wiki/Authenticated_encryption) on disk. They are then available in decrypted form through a Postgres view so that the secrets can be used by applications from SQL. Because the secrets are stored on disk encrypted and authenticated, any backups or replication streams also preserve this encryption in a way that can't be decrypted or forged.

Supabase provides a dashboard UI for the Vault that makes storing secrets easy. Click a button, type in your secret, and save.

<video width="99%" muted playsInline controls="true">
  <source src="/docs/img/guides/database/vault-hello-compressed.mp4" type="video/mp4" muted playsInline />
</video>

You can use Vault to store secrets - everything from Environment Variables to API Keys. You can then use these secrets anywhere in your database: Postgres [Functions](/docs/guides/database/functions), Triggers, and [Webhooks](/docs/guides/database/webhooks). From a SQL perspective, accessing secrets is as easy as querying a table (or in this case, a view). The underlying secrets tables will be stored in encrypted form.



## Using Vault

You can manage secrets from the UI or using SQL.


### Adding secrets

There is also a handy function for creating secrets called `vault.create_secret()`:

```sql
select vault.create_secret('my_s3kre3t');
```

The function returns the UUID of the new secret.

<details>
  <summary>Show Result</summary>

  ```sql
  -[ RECORD 1 ]-+-------------------------------------
  create_secret | c9b00867-ca8b-44fc-a81d-d20b8169be17
  ```
</details>

Secrets can also have an optional *unique* name and an optional description. These are also arguments to `vault.create_secret()`:

```sql
select vault.create_secret('another_s3kre3t', 'unique_name', 'This is the description');
```

<details>
  <summary>Show Result</summary>

  ```sql
  -[ RECORD 1 ]-----------------------------------------------------------------
  id          | 7095d222-efe5-4cd5-b5c6-5755b451e223
  name        | unique_name
  description | This is the description
  secret      | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=
  key_id      |
  nonce       | \x9f2d60954ba5eb566445736e0760b0e3
  created_at  | 2022-12-14 02:34:23.85159+00
  updated_at  | 2022-12-14 02:34:23.85159+00
  ```
</details>


### Viewing secrets

If you look in the `vault.secrets` table, you will see that your data is stored encrypted. To decrypt the data, there is an automatically created view `vault.decrypted_secrets`. This view will decrypt secret data on the fly:

{/* prettier-ignore */}

```sql
select * 
from vault.decrypted_secrets 
order by created_at desc 
limit 3;
```

<details>
  <summary>Show Result</summary>

  ```sql
  -[ RECORD 1 ]----+-----------------------------------------------------------------
  id               | 7095d222-efe5-4cd5-b5c6-5755b451e223
  name             | unique_name
  description      | This is the description
  secret           | 3mMeOcoG84a5F2uOfy2ugWYDp9sdxvCTmi6kTeT97bvA8rCEsG5DWWZtTU8VVeE=
  decrypted_secret | another_s3kre3t
  key_id           |
  nonce            | \x9f2d60954ba5eb566445736e0760b0e3
  created_at       | 2022-12-14 02:34:23.85159+00
  updated_at       | 2022-12-14 02:34:23.85159+00
  -[ RECORD 2 ]----+-----------------------------------------------------------------
  id               | c9b00867-ca8b-44fc-a81d-d20b8169be17
  name             |
  description      |
  secret           | a1CE4vXwQ53+N9bllJj1D7fasm59ykohjb7K90PPsRFUd9IbBdxIGZNoSQLIXl4=
  decrypted_secret | another_s3kre3t
  key_id           |
  nonce            | \x1d3b2761548c4efb2d29ca11d44aa22f
  created_at       | 2022-12-14 02:32:50.58921+00
  updated_at       | 2022-12-14 02:32:50.58921+00
  -[ RECORD 3 ]----+-----------------------------------------------------------------
  id               | d91596b8-1047-446c-b9c0-66d98af6d001
  name             |
  description      |
  secret           | S02eXS9BBY+kE3r621IS8beAytEEtj+dDHjs9/0AoMy7HTbog+ylxcS22A==
  decrypted_secret | s3kre3t_k3y
  key_id           |
  nonce            | \x3aa2e92f9808e496aa4163a59304b895
  created_at       | 2022-12-14 02:29:21.3625+00
  updated_at       | 2022-12-14 02:29:21.3625+00
  ```
</details>

Notice how this view has a `decrypted_secret` column that contains the decrypted secrets. Views are not stored on disk, they are only run at query time, so the secret remains encrypted on disk, and in any backup dumps or replication streams.

You should ensure that you protect access to this view with the appropriate SQL privilege settings at all times, as anyone that has access to the view has access to decrypted secrets.


### Updating secrets

A secret can be updated with the `vault.update_secret()` function, this function makes updating secrets easy, just provide the secret UUID as the first argument, and then an updated secret, updated optional unique name, or updated description:

```sql
select
  vault.update_secret(
    '7095d222-efe5-4cd5-b5c6-5755b451e223',
    'n3w_upd@ted_s3kret',
    'updated_unique_name',
    'This is the updated description'
  );
```

<details>
  <summary>Show Result</summary>

  ```sql
  -[ RECORD 1 ]-+-
  update_secret |

  postgres=> select * from vault.decrypted_secrets where id = '7095d222-efe5-4cd5-b5c6-5755b451e223';
  -[ RECORD 1 ]----+---------------------------------------------------------------------
  id               | 7095d222-efe5-4cd5-b5c6-5755b451e223
  name             | updated_unique_name
  description      | This is the updated description
  secret           | lhb3HBFxF+qJzp/HHCwhjl4QFb5dYDsIQEm35DaZQOovdkgp2iy6UMufTKJGH4ThMrU=
  decrypted_secret | n3w_upd@ted_s3kret
  key_id           |
  nonce            | \x9f2d60954ba5eb566445736e0760b0e3
  created_at       | 2022-12-14 02:34:23.85159+00
  updated_at       | 2022-12-14 02:51:13.938396+00
  ```
</details>



## Deep dive

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/QHLPNDrdN2w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
</div>

As we mentioned, Vault uses Transparent Column Encryption (TCE) to store secrets in an authenticated encrypted form. There are some details around that you may be curious about. What does authenticated mean? Where is the encryption key stored? This section explains those details.


### Authenticated encryption with associated data

The first important feature of TCE is that it uses an [Authenticated Encryption with Associated Data](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data_\(AEAD\)) encryption algorithm (based on `libsodium`).


### Encryption key location

**Authenticated Encryption** means that in addition to the data being encrypted, it is also signed so that it cannot be forged. You can guarantee that the data was encrypted by someone you trust, which you wouldn't get with encryption alone. The decryption function verifies that the signature is valid *before decrypting the value*.

**Associated Data** means that you can include any other columns from the same row as part of the signature computation. This doesn't encrypt those other columns - rather it ensures that your encrypted value is only associated with columns from that row. If an attacker were to copy an encrypted value from another row to the current one, the signature would be rejected (assuming you used a unique column in the associated data).

Another important feature is that the encryption key is never stored in the database alongside the encrypted data. Even if an attacker can capture a dump of your entire database, they will see only encrypted data, *never the encryption key itself*.

This is an important safety precaution - there is little value in storing the encryption key in the database itself as this would be like locking your front door but leaving the key in the lock! Storing the key outside the database fixes this issue.

Where is the key stored? Supabase creates and manages the encryption key in our secured backend systems. We keep this key safe and separate from your data. You remain in control of your key - a separate API endpoint is available that you can use to access the key if you want to decrypt your data outside of Supabase.

Which roles should have access to the `vault.secrets` table should be carefully considered. There are two ways to grant access, the first is that the `postgres` user can explicitly grant access to the vault table itself.


### Resources

*   Read more about Supabase Vault in the [blog post](/blog/vault-now-in-beta)
*   [Supabase Vault on GitHub](https://github.com/supabase/vault)
*   [Column Encryption](/docs/guides/database/column-encryption)



# Database Webhooks

Trigger external payloads on database events.

Database Webhooks allow you to send real-time data from your database to another system whenever a table event occurs.

You can hook into three table events: `INSERT`, `UPDATE`, and `DELETE`. All events are fired *after* a database row is changed.



## Webhooks vs triggers

Database Webhooks are very similar to triggers, and that's because Database Webhooks are just a convenience wrapper around triggers using the [pg\_net](/docs/guides/database/extensions/pgnet) extension. This extension is asynchronous, and therefore will not block your database changes for long-running network requests.

This video demonstrates how you can create a new customer in Stripe each time a row is inserted into a `profiles` table:

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/codAs9-NeHM" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Creating a webhook

1.  Create a new [Database Webhook](/dashboard/project/_/integrations/webhooks/overview) in the Dashboard.
2.  Give your Webhook a name.
3.  Select the table you want to hook into.
4.  Select one or more events (table inserts, updates, or deletes) you want to hook into.

Since webhooks are just database triggers, you can also create one from SQL statement directly.

```sql
create trigger "my_webhook" after insert
on "public"."my_table" for each row
execute function "supabase_functions"."http_request"(
  'http://host.docker.internal:3000',
  'POST',
  '{"Content-Type":"application/json"}',
  '{}',
  '1000'
);
```

We currently support HTTP webhooks. These can be sent as `POST` or `GET` requests with a JSON payload.



## Payload

The payload is automatically generated from the underlying table record:

```typescript
type InsertPayload = {
  type: 'INSERT'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: null
}
type UpdatePayload = {
  type: 'UPDATE'
  table: string
  schema: string
  record: TableRecord<T>
  old_record: TableRecord<T>
}
type DeletePayload = {
  type: 'DELETE'
  table: string
  schema: string
  record: null
  old_record: TableRecord<T>
}
```



## Monitoring

Logging history of webhook calls is available under the `net` schema of your database. For more info, see the [GitHub Repo](https://github.com/supabase/pg_net).



## Local development

When using Database Webhooks on your local Supabase instance, you need to be aware that the Postgres database runs inside a Docker container. This means that `localhost` or `127.0.0.1` in your webhook URL will refer to the container itself, not your host machine where your application is running.

To target services running on your host machine, use `host.docker.internal`. If that doesn't work, you may need to use your machine's local IP address instead.

For example, if you want to trigger an edge function when a webhook fires, your webhook URL would be:

```
http://host.docker.internal:54321/functions/v1/my-function-name
```

If you're experiencing connection issues with webhooks locally, verify you're using the correct hostname instead of `localhost`.



## Resources

*   [pg\_net](/docs/guides/database/extensions/pgnet): an async networking extension for Postgres



# FAQs




# Which connection string should be used?

Always use the direct connection string for logical replication.

Connections through a pooler, such as Supavisor, will not work.



# The tool in use does not support IPv6

You can enable the [IPv4 add-on](/docs/guides/platform/ipv4-address) for your project.



# What is XMIN and should it be used?

Xmin is a different form of replication from logical replication and should only be used if logical replication is not available for your database (i.e. older versions of Postgres).

Xmin performs replication by checking the [xmin system column](https://www.postgresql.org/docs/current/ddl-system-columns.html) and determining if that row has already been synchronized.

It does not capture deletion of data and is **not recommended**, particularly for larger databases.



# Can replication be configured in the Dashboard?

You can view [publications](/dashboard/project/default/database/publications) in the Dashboard but all steps to configure replication must be done using the [SQL Editor](/dashboard/project/default/sql/new) or a CLI tool of your choice.



# How to configure database settings for replication?

Yes. Using the Supabase CLI, you can [configure database settings](/docs/guides/database/custom-postgres-config#cli-configurable-settings) to optimize them for your replication needs. These values can vary depending on the activity of your database size and activity.



# What are some important configuration options?

Some of the more important options to be aware of are:

*   `max_wal_size`
*   `max_slot_wal_keep_size`
*   `wal_keep_size`
*   `max_wal_senders`



# Monitoring replication



Monitoring replication lag is important and there are 3 ways to do this:

1.  Dashboard - Under the [Reports](/docs/guides/platform/reports) of the dashboard, you can view the replication lag of your project
2.  Database -
    *   pg\_stat\_subscription (subscriber) - if PID is null, then the subscription is not active
    *   pg\_stat\_subscription\_stats - look here for error\_count to see if there were issues applying or syncing (if yes, check the logs for why)
    *   pg\_replication\_slots - use this to check if the slot is active and you can also calculate the lag from here
3.  [Metrics](/docs/guides/telemetry/metrics) - Using the prometheus endpoint for your project
    *   replication\_slots\_max\_lag\_bytes - this is the more important one
    *   pg\_stat\_replication\_replay\_lag - lag to replay WAL files from the source DB on the target DB (throttled by disk or high activity)
    *   pg\_stat\_replication\_send\_lag - lag in sending WAL files from the source DB (a high lag means that the publisher is not being asked to send new WAL files OR a network issues)



## Primary


### Replication status and lag

The `pg_stat_replication` table shows the status of any replicas connected to the primary database.

```sql
select pid, application_name, state, sent_lsn, write_lsn, flush_lsn, replay_lsn, sync_state
from pg_stat_replication;
```


### Replication slot status

A replication slot can be in one of three states:

*   `active` - The slot is active and is receiving data
*   `inactive` - The slot is not active and is not receiving data
*   `lost` - The slot is lost and is not receiving data

The state can be checked using the `pg_replication_slots` table:

```sql
select slot_name, active, state from pg_replication_slots;
```


### WAL size

The WAL size can be checked using the `pg_ls_waldir()` function:

```sql
select * from pg_ls_waldir();
```


### Check LSN

```sql
select pg_current_wal_lsn();
```



## Subscriber


### Subscription status

The `pg_subscription` table shows the status of any subscriptions on a replica and the `pg_subscription_rel` table shows the status of each table within a subscription.

The `srsubstate` column in `pg_subscription_rel` can be one of the following:

*   `i` - Initializing - The subscription is being initialized
*   `d` - Data Synchronizing - The subscription is synchronizing data for the first time (i.e. doing the initial copy)
*   `s` - Synchronized - The subscription is synchronized
*   `r` - Replicating - The subscription is replicating data

```sql
SELECT
    sub.subname AS subscription_name,
    relid::regclass AS table_name,
    srel.srsubstate AS replication_state,
    CASE srel.srsubstate
        WHEN 'i' THEN 'Initializing'
        WHEN 'd' THEN 'Data Synchronizing'
        WHEN 's' THEN 'Synchronized'
        WHEN 'r' THEN 'Replicating'
        ELSE 'Unknown'
    END AS state_description,
    srel.srsyncedlsn AS last_synced_lsn
FROM
    pg_subscription sub
JOIN
    pg_subscription_rel srel ON sub.oid = srel.srsubid
ORDER BY
    table_name;
```


### Check LSN

```sql
select pg_last_wal_replay_lsn();
```



# Setting up replication and CDC with Supabase




## Prerequisites

To set up replication, the following is recommended:

*   Instance size of XL or greater
*   [IPv4 add-on](/docs/guides/platform/ipv4-address) enabled

To create a replication slot, you will need to use the `postgres` user and follow the instructions in our [guide](/docs/guides/database/postgres/setup-replication-external).

<Admonition type="note">
  If you are running Postgres 17 or higher, you can create a new user and grant them replication permissions with the `postgres` user. For versions below 17, you will need to use the `postgres` user.
</Admonition>

If you are replicating to an external system and using any of the tools below, check their documentation first and we have added additional information where the setup with Supabase can vary.

<Tabs scrollable size="small" type="underlined" defaultActiveId="estuary" queryGroup="tool">
  <TabPanel id="airbyte" label="Airbyte">
    Airbyte has the following [documentation](https://docs.airbyte.com/integrations/sources/postgres/) for setting up Postgres as a source, either in their cloud offering or by self-hosting.

    You can follow those steps with the following modifications:

    1.  Use the `postgres` user
    2.  Select `logical replication` as the replication method (`xmin` is possible, but not recommended)

    ## Troubleshooting

    Airbyte has a known [issue](https://discuss.airbyte.io/t/postgres-source-replication-slot-safe-wal-size-only-reset-when-a-change-occurs/3263/7) where it does not clear WAL files on each successful sync. The recommended workaround is to have a `heartbeat` table that you write changes to once an hour.>
  </TabPanel>

  <TabPanel id="estuary" label="Estuary">
    Estuary has the following [documentation](https://docs.estuary.dev/reference/Connectors/capture-connectors/PostgreSQL/Supabase/) for setting up Postgres as a source.
  </TabPanel>

  <TabPanel id="fivetran" label="Fivetran">
    Fivetran has the following [documentation](https://fivetran.com/docs/connectors/databases/postgresql/setup-guide) for setting up Postgres as a source.

    You can follow those steps with the following modifications:

    1.  In Step 2, choose `logical replication` as the sync mechanism
    2.  In Step 3, do not create a user and use the existing `postgres` user for replication
    3.  In Step 5, no need to modify any WAL settings as we have done that for you
  </TabPanel>

  <TabPanel id="materialize" label="Materialize">
    Materialize has the following [documentation](https://materialize.com/docs/sql/create-source/postgres/) on setting up Postgres as a source.

    You can follow those steps with the following modifications:

    1.  Follow the steps in our [guide](/docs/guides/database/postgres/setup-replication-external) to create a publication slot
  </TabPanel>

  <TabPanel id="stitch" label="Stitch">
    Stitch has the following [documentation](https://www.stitchdata.com/docs/integrations/databases/postgresql/v2#extract-data) on configuring Postgres as a source.

    You can follow those steps with the following modifications:

    1.  Use the `postgres` user for replication
    2.  Skip step 3
  </TabPanel>
</Tabs>



# Troubleshooting prisma errors



This guide addresses common Prisma errors that you might encounter while using Supabase.

<Admonition type="note">
  A full list of errors can be found in [Prisma's official docs](https://www.prisma.io/docs/orm/reference/error-reference).
</Admonition>



## Understanding connection string parameters: \[#start]

Unlike other libraries, Prisma lets you configure [its settings](https://www.prisma.io/docs/orm/overview/databases/postgresql#arguments) through special options appended to your connection string.

These options, called "query parameters," can be used to address specific errors.

```md

# Example of query parameters

connection_string.../postgres?KEY1=VALUE&KEY2=VALUE&KEY3=VALUE
```



# Errors

{/* supa-mdx-lint-disable-next-line Rule001HeadingCase */}



## ... prepared statement already exists

Supavisor in transaction mode (port 6543) does not support [prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html), which Prisma will try to create in the background.


### Solution: \[#solution-prepared-statement-exists]

*   Add `pgbouncer=true` to the connection string. This turns off prepared statements in Prisma.

```md
.../postgres?pgbouncer=true
```

***



## Can't reach database server at:

Prisma couldn't establish a connection with Postgres or Supavisor before the timeout


### Possible causes: \[#possible-causes-cant-reach-database-server-at]

*   **Database overload**: The database server is under heavy load, causing Prisma to struggle to connect.
*   **Malformed connection string**: The connection string used by Prisma is incorrect or incomplete.
*   **Transient network issues**: Temporary network problems are disrupting the connection.


### Solutions: \[#solution-cant-reach-database-server-at]

*   **Check database health**: Use the [Reports Dashboard](/dashboard/project/_/reports/database) to monitor CPU, memory, and I/O usage. If the database is overloaded, consider increasing your [compute size](/docs/guides/platform/compute-add-ons) or [optimizing your queries](/docs/guides/database/query-optimization).
*   **Verify connection string**: Double-check the connection string in your Prisma configuration to ensure it matches in your [project connect page](/dashboard/project/_?showConnect=true).
*   **Increase connection timeout**: Try increasing the `connect_timeout` parameter in your Prisma configuration to give it more time to establish a connection.

```md
.../postgres?connect_timeout=30
```

***



## Timed out fetching a new connection from the connection pool:

Prisma is unable to allocate connections to pending queries fast enough to meet demand.


### Possible causes: \[#possible-causes-timed-out-fetching-a-new-connection]

*   **Overwhelmed server**: The server hosting Prisma is under heavy load, limiting its ability to manage connections. By default, Prisma will create the default `num_cpus * 2 + 1` worth of connections. A common cause for server strain is increasing the `connection_limit` significantly past the default.
*   **Insufficient pool size**: The Supavisor pooler does not have enough connections available to quickly satisfy Prisma's requests.
*   **Slow queries**: Prisma's queries are taking too long to execute, preventing it from releasing connections for reuse.


### Solutions: \[#solution-timed-out-fetching-a-new-connection]

*   **Increase the pool timeout**: Increase the `pool_timeout` parameter in your Prisma configuration to give the pooler more time to allocate connections.
*   **Reduce the connection limit**: If you've explicitly increased the `connection_limit` parameter in your Prisma configuration, try reducing it to a more reasonable value.
*   **Increase pool size**: If you are connecting with Supavisor, try increasing the pool size in the [Database Settings](/dashboard/project/_/database/settings).
*   **Optimize queries**: [Improve the efficiency of your queries](/docs/guides/database/query-optimization) to reduce execution time.
*   **Increase compute size**: Like the preceding option, this is a strategy to reduce query execution time.

***



## Server has closed the connection

According to this [GitHub Issue for Prisma](https://github.com/prisma/prisma/discussions/7389), this error may be related to large return values for queries. It may also be caused by significant database strain.


### Solutions: \[#solution-server-has-closed-the-connection]

*   **Limit row return sizes**: Try to limit the total amount of rows returned for particularly large requests.
*   **Minimize database strain**:Check the Reports Page for database strain. If there is obvious strain, consider [optimizing](/docs/guides/database/query-optimization) or increasing compute size

***



## Drift detected: Your database schema is not in sync with your migration history

Prisma relies on migration files to ensure your database aligns with Prisma's model. External schema changes are detected as "drift", which Prisma will try to overwrite, potentially causing data loss.


### Possible causes: \[#possible-causes-your-database-schema-is-not-in-sync]

*   **Supabase Managed Schemas**: Supabase may update managed schemas like auth and storage to introduce new features. Granting Prisma access to these schemas can lead to drift during updates.
*   **External Schema Modifications**: Your team or another tool might have modified the database schema outside of Prisma, causing drift.


### Solution: \[#solution-your-database-schema-is-not-in-sync]

*   **Baselining migrations**: [baselining](https://www.prisma.io/docs/orm/prisma-migrate/workflows/baselining) re-syncs Prisma by capturing the current database schema as the starting point for future migrations.

***



## Max client connections reached

Postgres or Supavisor rejected a request for more connections


### Possible causes:\[#possible-causes-max-client-connections-reached]

*   **When working in transaction mode (port 6543):** The error "Max client connections reached" occurs when clients try to form more connections with the pooler than it can support.
*   **When working in session mode (port 5432):** The max amount of clients is restricted to the "Pool Size" value in the [Database Settings](/dashboard/project/_/database/settings). If the "Pool Size" is set to 15, even if the pooler can handle 200 client connections, it will still be effectively capped at 15 for each unique ["database-role+database" combination](https://github.com/orgs/supabase/discussions/21566).
*   **When working with direct connections**: Postgres is already servicing the max amount of connections


### Solutions \[#solutions-causes-max-client-connections-reached]

*   **Transaction Mode for serverless apps**: If you are using serverless functions (Supabase Edge, Vercel, AWS Lambda), switch to transaction mode (port 6543). It handles more connections than session mode or direct connections.
*   **Reduce the number of Prisma connections**: A single client-server can establish multiple connections with a pooler. Typically, serverless setups do not need many connections. Starting with fewer, like five or three, or even just one, is often sufficient. In serverless setups, begin with `connection_limit=1`, increasing cautiously if needed to avoid maxing out connections.
*   **Increase pool size**: If you are connecting with Supavisor, try increasing the pool size in the [Database Settings](/dashboard/project/_/database/settings).
*   **Disconnect appropriately**: Close Prisma connections when they are no longer needed.
*   **Decrease query time**: Reduce query complexity or add [strategic indexes](/docs/guides/database/postgres/indexes) to your tables to speed up queries.
*   **Increase compute size**: Sometimes the best option is to increase your compute size, which also increases your max client size and query execution speed

***



## Cross schema references are only allowed when the target schema is listed in the schemas property of your data-source

A Prisma migration is referencing a schema it is not permitted to manage.


### Possible causes: \[#possible-causes-cross-schema-references]

*   A migration references a schema that Prisma is not permitted to manage


### Solutions: \[#solutions-cross-schema-references]

*   Multi-Schema support: If the external schema isn't Supabase managed, modify your `prisma.schema` file to enable the multi-Schema preview

```ts prisma.schema
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["multiSchema"]  //Add line
}

datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")
  directUrl = env("DIRECT_URL")
  schemas   = ["public", "other_schema"] //list out relevant schemas
}
```

*   Supabase managed schemas: Schemas managed by Supabase, such as `auth` and `storage`, may be changed to support new features. Referencing these schemas directly will cause schema drift in the future. It is best to remove references to these schemas from your migrations.

An alternative strategy to reference these tables is to duplicate values into Prisma managed table with triggers. Below is an example for duplicating values from `auth.users` into a table called `profiles`.

<details>
  <summary>Show/Hide Details</summary>

  ```sql table_in_public
  -- Create the 'profiles' table in the 'public' schema
  create table public.profiles (
    id uuid primary key,             -- 'id' is a UUID and the primary key for the table
    email varchar(256)               -- 'email' is a variable character field with a maximum length of 256 characters
  );
  ```

  ```sql trigger_on_insert
  -- Function to handle the insertion of a new user into the 'profiles' table
  create function public.handle_new_user()
  returns trigger
  language plpgsql
  security definer set search_path = ''
  as $$
  begin

    -- Insert the new user's data into the 'profiles' table
    insert into public.profiles (id, email)
    values (new.id, new.email);

    return new;     -- Return the new record
  end;
  $$;
  ```

  ```sql trigger_on_update
  -- Function to handle the updating of a user's information in the 'profiles' table
  create function public.update_user()
  returns trigger
  language plpgsql
  security definer set search_path = ''
  as
  $$
  begin
    -- Update the user's data in the 'profiles' table
    update public.profiles
    set email = new.email     -- Update the 'email' field
    where id = new.id;        -- Match the 'id' field with the new record

    return new;  -- Return the new record
  end;
  $$;
  ```

  ```sql trigger_on_delete
  -- Function to handle the deletion of a user from the 'profiles' table
  create function public.delete_user()
  returns trigger
  language plpgsql
  security definer set search_path = ''
  as
  $$
  begin
    -- Delete the user's data from the 'profiles' table
    delete from public.profiles
    where id = old.id;  -- Match the 'id' field with the old record

    return old;  -- Return the old record
  end;
  $$;
  ```

  ```sql triggers_on_auth
  -- Trigger to run 'handle_new_user' function after a new user is inserted into 'auth.users' table
  create trigger on_auth_user_created
    after insert on auth.users
    for each row execute procedure public.handle_new_user();

  -- Trigger to run 'update_user' function after a user is updated in the 'auth.users' table
  create trigger on_auth_user_updated
    after update on auth.users
    for each row execute procedure public.update_user();

  -- Trigger to run 'delete_user' function after a user is deleted from the 'auth.users' table
  create trigger on_auth_user_deleted
    after delete on auth.users
    for each row execute procedure public.delete_user();
  ```
</details>



# Cascade Deletes



There are 5 options for foreign key constraint deletes:

1.  **CASCADE:** When a row is deleted from the parent table, all related rows in the child tables are deleted as well.
2.  **RESTRICT:** When a row is deleted from the parent table, the delete operation is aborted if there are any related rows in the child tables.
3.  **SET NULL:** When a row is deleted from the parent table, the values of the foreign key columns in the child tables are set to NULL.
4.  **SET DEFAULT:** When a row is deleted from the parent table, the values of the foreign key columns in the child tables are set to their default values.
5.  **NO ACTION:** This option is similar to RESTRICT, but it also has the option to be “deferred” to the end of a transaction. This means that other cascading deletes can run first, and then this delete constraint will only throw an error if there is referenced data remaining *at the end of the transaction*.

These options can be specified when defining a foreign key constraint using the "ON DELETE" clause. For example, the following SQL statement creates a foreign key constraint with the `CASCADE` option:

```sql
alter table child_table
add constraint fk_parent foreign key (parent_id) references parent_table (id)
  on delete cascade;
```

This means that when a row is deleted from the `parent_table`, all related rows in the `child_table` will be deleted as well.



## `RESTRICT` vs `NO ACTION`

The difference between `NO ACTION` and `RESTRICT` is subtle and can be a bit confusing.

Both `NO ACTION` and `RESTRICT` are used to prevent deletion of a row in a parent table if there are related rows in a child table. However, there is a subtle difference in how they behave.

When a foreign key constraint is defined with the option `RESTRICT`, it means that if a row in the parent table is deleted, the database will immediately raise an error and prevent the deletion of the row in the parent table. The database will not delete, update or set to NULL any rows in the referenced tables.

When a foreign key constraint is defined with the option `NO ACTION`, it means that if a row in the parent table is deleted, the database will also raise an error and prevent the deletion of the row in the parent table. However unlike `RESTRICT`, `NO ACTION` has the option to defer the check using `INITIALLY DEFERRED`. This will only raise the above error *if* the referenced rows still exist at the end of the transaction.

The difference from `RESTRICT` is that a constraint marked as `NO ACTION INITIALLY DEFERRED` is deferred until the end of the transaction, rather than running immediately. If, for example there is another foreign key constraint between the same tables marked as `CASCADE`, the cascade will occur first and delete the referenced rows, and no error will be thrown by the deferred constraint. Otherwise if there are still rows referencing the parent row by the end of the transaction, an error will be raised just like before. Just like `RESTRICT`, the database will not delete, update or set to NULL any rows in the referenced tables.

In practice, you can use either `NO ACTION` or `RESTRICT` depending on your needs. `NO ACTION` is the default behavior if you do not specify anything. If you prefer to defer the check until the end of the transaction, use `NO ACTION INITIALLY DEFERRED`.



## Example

Let's further illustrate the difference with an example. We'll use the following data:

`grandparent`

| id | name      |
| -- | --------- |
| 1  | Elizabeth |

`parent`

| id | name    | `parent_id` |
| -- | ------- | ----------- |
| 1  | Charles | 1           |
| 2  | Diana   | 1           |

`child`

| id | name    | father | mother |
| -- | ------- | ------ | ------ |
| 1  | William | 1      | 2      |

To create these tables and their data, we run:

```sql
create table grandparent (
  id serial primary key,
  name text
);

create table parent (
  id serial primary key,
  name text,
  parent_id integer references grandparent (id)
    on delete cascade
);

create table child (
  id serial primary key,
  name text,
  father integer references parent (id)
    on delete restrict
);

insert into grandparent
  (id, name)
values
  (1, 'Elizabeth');

insert into parent
  (id, name, parent_id)
values
  (1, 'Charles', 1);

insert into parent
  (id, name, parent_id)
values
  (2, 'Diana', 1);

-- We'll just link the father for now
insert into child
  (id, name, father)
values
  (1, 'William', 1);
```


### `RESTRICT`

`RESTRICT` will prevent a delete and raise an error:

```shell
postgres=# delete from grandparent;
ERROR: update or delete on table "parent" violates foreign key constraint "child_father_fkey" on table "child"
DETAIL: Key (id)=(1) is still referenced from table "child".
```

Even though the foreign key constraint between parent and grandparent is `CASCADE`, the constraint between child and father is `RESTRICT`. Therefore an error is raised and no records are deleted.


### `NO ACTION`

Let's change the child-father relationship to `NO ACTION`:

```sql
alter table child
drop constraint child_father_fkey;

alter table child
add constraint child_father_fkey foreign key (father) references parent (id)
  on delete no action;
```

We see that `NO ACTION` will also prevent a delete and raise an error:

```shell
postgres=# delete from grandparent;
ERROR: update or delete on table "parent" violates foreign key constraint "child_father_fkey" on table "child"
DETAIL: Key (id)=(1) is still referenced from table "child".
```


### `NO ACTION INITIALLY DEFERRED`

We'll change the foreign key constraint between child and father to be `NO ACTION INITIALLY DEFERRED`:

```sql
alter table child
drop constraint child_father_fkey;

alter table child
add constraint child_father_fkey foreign key (father) references parent (id)
  on delete no action initially deferred;
```

Here you will see that `INITIALLY DEFFERED` seems to operate like `NO ACTION` or `RESTRICT`. When we run a delete, it seems to make no difference:

```shell
postgres=# delete from grandparent;
ERROR: update or delete on table "parent" violates foreign key constraint "child_father_fkey" on table "child"
DETAIL: Key (id)=(1) is still referenced from table "child".
```

But, when we combine it with *other* constraints, then any other constraints take precedence. For example, let's run the same but add a `mother` column that has a `CASCADE` delete:

```sql
alter table child
add column mother integer references parent (id)
  on delete cascade;

update child
set mother = 2
where id = 1;
```

Then let's run a delete on the `grandparent` table:

```shell
postgres=# delete from grandparent;
DELETE 1

postgres=# select * from parent;
 id | name | parent_id
----+------+-----------
(0 rows)

postgres=# select * from child;
 id | name | father | mother
----+------+--------+--------
(0 rows)
```

The `mother` deletion took precedence over the `father`, and so William was deleted. After William was deleted, there was no reference to “Charles” and so he was free to be deleted, even though previously he wasn't (without `INITIALLY DEFERRED`).



# Column Level Security



PostgreSQL's [Row Level Security (RLS)](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) gives you granular control over who can access rows of data. However, it doesn't give you control over which columns they can access within rows. Sometimes you want to restrict access to specific columns in your database. Column Level Privileges allows you to do just that.

<Admonition type="caution">
  This is an advanced feature. We do not recommend using column-level privileges for most users. Instead, we recommend using RLS policies in combination with a dedicated table for handling user roles.
</Admonition>

<Admonition type="caution">
  Restricted roles cannot use the wildcard operator (`*`) on the affected table. Instead of using `SELECT * FROM <restricted_table>;` or its API equivalent, you must specify the column names explicitly.
</Admonition>



## Policies at the row level

Policies in Row Level Security (RLS) are used to restrict access to rows in a table. Think of them like adding a `WHERE` clause to every query.

For example, let's assume you have a `posts` table with the following columns:

*   `id`
*   `user_id`
*   `title`
*   `content`
*   `created_at`
*   `updated_at`

You can restrict updates to just the user who created it using [RLS](/docs/guides/auth#row-level-security), with the following policy:

```sql
create policy "Allow update for owners" on posts for
update
  using ((select auth.uid()) = user_id);
```

However, this gives the post owner full access to update the row, including all of the columns.



## Privileges at the column level

To restrict access to columns, you can use [Privileges](https://www.postgresql.org/docs/current/ddl-priv.html).

There are two types of privileges in Postgres:

1.  **table-level**: Grants the privilege on all columns in the table.
2.  **column-level** Grants the privilege on a specific column in the table.

You can have both types of privileges on the same table. If you have both, and you revoke the column-level privilege, the table-level privilege will still be in effect.

By default, our table will have a table-level `UPDATE` privilege, which means that the `authenticated` role can update all the columns in the table.

```sql
revoke
update
  on table public.posts
from
  authenticated;

grant
update
  (title, content) on table public.posts to authenticated;
```

In the above example, we are revoking the table-level `UPDATE` privilege from the `authenticated` role and granting a column-level `UPDATE` privilege on just the `title` and `content` columns.

If we want to restrict access to updating the `title` column:

```sql
revoke
update
  (title) on table public.posts
from
  authenticated;
```

This time, we are revoking the column-level `UPDATE` privilege of the `title` column from the `authenticated` role. We didn't need to revoke the table-level `UPDATE` privilege because it's already revoked.



## Manage column privileges in the Dashboard

<Admonition type="caution">
  Column-level privileges are a powerful tool, but they're also quite advanced and in many cases, not the best fit for common access control needs. For that reason, we've intentionally moved the UI for this feature under the Feature Preview section in the dashboard.
</Admonition>

You can view and edit the privileges in the [Supabase Studio](/dashboard/project/_/database/column-privileges).

![Column level privileges](/docs/img/guides/privileges/column-level-privileges-2.png)



## Manage column privileges in migrations

While you can manage privileges directly from the Dashboard, as your project grows you may want to manage them in your migrations. Read about database migrations in the [Local Development](/docs/guides/deployment/database-migrations) guide.

<StepHikeCompact>
  <StepHikeCompact.Step step={1}>
    <StepHikeCompact.Details title="Create a migration file">
      To get started, generate a [new migration](/docs/reference/cli/supabase-migration-new) to store the SQL needed to create your table along with row and column-level privileges.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```bash
      supabase migration new create_posts_table
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>

<StepHikeCompact>
  <StepHikeCompact.Step step={2}>
    <StepHikeCompact.Details title="Add the SQL to your migration file">
      This creates a new migration: supabase/migrations/\<timestamp>
      \_create\_posts\_table.sql.

      To that file, add the SQL to create this `posts` table with row and column-level privileges.
    </StepHikeCompact.Details>

    <StepHikeCompact.Code>
      ```sql
      create table
      posts (
      id bigint primary key generated always as identity,
      user_id text,
      title text,
      content text,
      created_at timestamptz default now()
      updated_at timestamptz default now()
      );

      -- Add row-level security
      create policy "Allow update for owners" on posts for
      update
      using ((select auth.uid()) = user_id);

      -- Add column-level security
      revoke
      update
      (title) on table public.posts
      from
      authenticated;
      ```
    </StepHikeCompact.Code>
  </StepHikeCompact.Step>
</StepHikeCompact>



## Considerations when using column-level privileges

*   If you turn off a column privilege you won't be able to use that column at all.
*   All operations (insert, update, delete) as well as using `select *` will fail.



# Database configuration

Updating the default configuration for your Postgres database.

Postgres provides a set of sensible defaults for you database size. In some cases, these defaults can be updated. We do not recommend changing these defaults unless you know what you're doing.



## Timeouts

See the [Timeouts](/docs/guides/database/postgres/timeouts) section.



## Statement optimization

All Supabase projects come with the [`pg_stat_statements`](https://www.postgresql.org/docs/current/pgstatstatements.html) extension installed, which tracks planning and execution statistics for all statements executed against it. These statistics can be used in order to diagnose the performance of your project.

This data can further be used in conjunction with the [`explain`](https://www.postgresql.org/docs/current/using-explain.html) functionality of Postgres to optimize your usage.



## Managing timezones

Every hosted Supabase database is set to UTC timezone by default. We strongly recommend keeping it this way, even if your users are in a different location. This is because it makes it much easier to calculate differences between timezones if you adopt the mental model that everything in your database is in UTC time.

<Admonition type="tip">
  On self-hosted databases, the timezone defaults to your local timezone. We recommend [changing this to UTC](/docs/guides/database/postgres/configuration#change-timezone) for the same reasons.
</Admonition>


### Change timezone

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    alter database postgres
    set timezone to 'America/New_York';
    ```
  </TabPanel>
</Tabs>


### Full list of timezones

Get a full list of timezones supported by your database. This will return the following columns:

*   `name`: Time zone name
*   `abbrev`: Time zone abbreviation
*   `utc_offset`: Offset from UTC (positive means east of Greenwich)
*   `is_dst`: True if currently observing daylight savings

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    select name, abbrev, utc_offset, is_dst
    from pg_timezone_names()
    order by name;
    ```
  </TabPanel>
</Tabs>


### Search for a specific timezone

Use `ilike` (case insensitive search) to find specific timezones.

<Tabs scrollable size="small" type="underlined" defaultActiveId="sql" queryGroup="database-method">
  <TabPanel id="sql" label="SQL">
    ```sql
    select *
    from pg_timezone_names()
    where name ilike '%york%';
    ```
  </TabPanel>
</Tabs>



# Custom Claims & Role-based Access Control (RBAC)



Custom Claims are special attributes attached to a user that you can use to control access to portions of your application. For example:

```json
{
  "user_role": "admin",
  "plan": "TRIAL",
  "user_level": 100,
  "group_name": "Super Guild!",
  "joined_on": "2022-05-20T14:28:18.217Z",
  "group_manager": false,
  "items": ["toothpick", "string", "ring"]
}
```

To implement Role-Based Access Control (RBAC) with `custom claims`, use a [Custom Access Token Auth Hook](/docs/guides/auth/auth-hooks#hook-custom-access-token). This hook runs before a token is issued. You can use it to add additional claims to the user's JWT.

This guide uses the [Slack Clone example](https://github.com/supabase/supabase/tree/master/examples/slack-clone/nextjs-slack-clone) to demonstrate how to add a `user_role` claim and use it in your [Row Level Security (RLS) policies](/docs/guides/database/postgres/row-level-security).



## Create a table to track user roles and permissions

In this example, you will implement two user roles with specific permissions:

*   `moderator`: A moderator can delete all messages but not channels.
*   `admin`: An admin can delete all messages and channels.

```sql supabase/migrations/init.sql
-- Custom types
create type public.app_permission as enum ('channels.delete', 'messages.delete');
create type public.app_role as enum ('admin', 'moderator');

-- USER ROLES
create table public.user_roles (
  id        bigint generated by default as identity primary key,
  user_id   uuid references auth.users on delete cascade not null,
  role      app_role not null,
  unique (user_id, role)
);
comment on table public.user_roles is 'Application roles for each user.';

-- ROLE PERMISSIONS
create table public.role_permissions (
  id           bigint generated by default as identity primary key,
  role         app_role not null,
  permission   app_permission not null,
  unique (role, permission)
);
comment on table public.role_permissions is 'Application permissions for each role.';
```

<Admonition type="note">
  For the [full schema](https://github.com/supabase/supabase/blob/master/examples/slack-clone/nextjs-slack-clone/README.md), see the example application on [GitHub](https://github.com/supabase/supabase/tree/master/examples/slack-clone/nextjs-slack-clone).
</Admonition>

You can now manage your roles and permissions in SQL. For example, to add the mentioned roles and permissions from above, run:

```sql supabase/seed.sql
insert into public.role_permissions (role, permission)
values
  ('admin', 'channels.delete'),
  ('admin', 'messages.delete'),
  ('moderator', 'messages.delete');
```



## Create Auth Hook to apply user role

The [Custom Access Token Auth Hook](/docs/guides/auth/auth-hooks#hook-custom-access-token) runs before a token is issued. You can use it to edit the JWT.

<Tabs scrollable size="small" type="underlined" defaultActiveId="plpgsql" queryGroup="language">
  <TabPanel id="plpgsql" label="PL/pgSQL (best performance)">
    ```sql supabase/migrations/auth_hook.sql
    -- Create the auth hook function
    create or replace function public.custom_access_token_hook(event jsonb)
    returns jsonb
    language plpgsql
    stable
    as $$
      declare
        claims jsonb;
        user_role public.app_role;
      begin
        -- Fetch the user role in the user_roles table
        select role into user_role from public.user_roles where user_id = (event->>'user_id')::uuid;

        claims := event->'claims';

        if user_role is not null then
          -- Set the claim
          claims := jsonb_set(claims, '{user_role}', to_jsonb(user_role));
        else
          claims := jsonb_set(claims, '{user_role}', 'null');
        end if;

        -- Update the 'claims' object in the original event
        event := jsonb_set(event, '{claims}', claims);

        -- Return the modified or original event
        return event;
      end;
    $$;

    grant usage on schema public to supabase_auth_admin;

    grant execute
      on function public.custom_access_token_hook
      to supabase_auth_admin;

    revoke execute
      on function public.custom_access_token_hook
      from authenticated, anon, public;

    grant all
      on table public.user_roles
    to supabase_auth_admin;

    revoke all
      on table public.user_roles
      from authenticated, anon, public;

    create policy "Allow auth admin to read user roles" ON public.user_roles
    as permissive for select
    to supabase_auth_admin
    using (true)
    ```
  </TabPanel>
</Tabs>


### Enable the hook

In the dashboard, navigate to [`Authentication > Hooks (Beta)`](/dashboard/project/_/auth/hooks) and select the appropriate Postgres function from the dropdown menu.

When developing locally, follow the [local development](/docs/guides/auth/auth-hooks#local-development) instructions.

<Admonition type="note">
  To learn more about Auth Hooks, see the [Auth Hooks docs](/docs/guides/auth/auth-hooks).
</Admonition>



## Accessing custom claims in RLS policies

To utilize Role-Based Access Control (RBAC) in Row Level Security (RLS) policies, create an `authorize` method that reads the user's role from their JWT and checks the role's permissions:

```sql supabase/migrations/init.sql
create or replace function public.authorize(
  requested_permission app_permission
)
returns boolean as $$
declare
  bind_permissions int;
  user_role public.app_role;
begin
  -- Fetch user role once and store it to reduce number of calls
  select (auth.jwt() ->> 'user_role')::public.app_role into user_role;

  select count(*)
  into bind_permissions
  from public.role_permissions
  where role_permissions.permission = requested_permission
    and role_permissions.role = user_role;

  return bind_permissions > 0;
end;
$$ language plpgsql stable security definer set search_path = '';
```

<Admonition type="note">
  You can read more about using functions in RLS policies in the [RLS guide](/docs/guides/database/postgres/row-level-security#using-functions).
</Admonition>

You can then use the `authorize` method within your RLS policies. For example, to enable the desired delete access, you would add the following policies:

```sql
create policy "Allow authorized delete access" on public.channels for delete to authenticated using ( (SELECT authorize('channels.delete')) );
create policy "Allow authorized delete access" on public.messages for delete to authenticated using ( (SELECT authorize('messages.delete')) );
```



## Accessing custom claims in your application

The auth hook will only modify the access token JWT but not the auth response. Therefore, to access the custom claims in your application, e.g. your browser client, or server-side middleware, you will need to decode the `access_token` JWT on the auth session.

In a JavaScript client application you can for example use the [`jwt-decode` package](https://www.npmjs.com/package/jwt-decode):

```js
import { jwtDecode } from 'jwt-decode'

const { subscription: authListener } = supabase.auth.onAuthStateChange(async (event, session) => {
  if (session) {
    const jwt = jwtDecode(session.access_token)
    const userRole = jwt.user_role
  }
})
```

For server-side logic you can use packages like [`express-jwt`](https://github.com/auth0/express-jwt), [`koa-jwt`](https://github.com/stiang/koa-jwt), [`PyJWT`](https://github.com/jpadilla/pyjwt), [dart\_jsonwebtoken](https://pub.dev/packages/dart_jsonwebtoken), [Microsoft.AspNetCore.Authentication.JwtBearer](https://www.nuget.org/packages/Microsoft.AspNetCore.Authentication.JwtBearer), etc.



## Conclusion

You now have a robust system in place to manage user roles and permissions within your database that automatically propagates to Supabase Auth.



## More resources

*   [Auth Hooks](/docs/guides/auth/auth-hooks)
*   [Row Level Security](/docs/guides/database/postgres/row-level-security)
*   [RLS Functions](/docs/guides/database/postgres/row-level-security#using-functions)
*   [Next.js Slack Clone Example](https://github.com/supabase/supabase/tree/master/examples/slack-clone/nextjs-slack-clone)



# Drop all tables in a PostgreSQL schema



Execute the following query to drop all tables in a given schema.
Replace `my-schema-name` with the name of your schema. In Supabase, the default schema is `public`.

<Admonition type="caution">
  This deletes all tables and their associated data. Ensure you have a recent [backup](/docs/guides/platform/backups) before proceeding.
</Admonition>

```sql
do $$ declare
    r record;
begin
    for r in (select tablename from pg_tables where schemaname = 'my-schema-name') loop
        execute 'drop table if exists ' || quote_ident(r.tablename) || ' cascade';
    end loop;
end $$;
```

This query works by listing out all the tables in the given schema and then executing a `drop table` for each (hence the `for... loop`).

You can run this query using the [SQL Editor](/dashboard/project/_/sql) in the Supabase Dashboard, or via `psql` if you're [connecting directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).



# Managing Enums in Postgres



Enums in Postgres are a custom data type. They allow you to define a set of values (or labels) that a column can hold. They are useful when you have a fixed set of possible values for a column.



## Creating enums

You can define a Postgres Enum using the `create type` statement. Here's an example:

{/* prettier-ignore */}

```sql
create type mood as enum (
  'happy',
  'sad',
  'excited',
  'calm'
);
```

In this example, we've created an Enum called "mood" with four possible values.



## When to use enums

There is a lot of overlap between Enums and foreign keys. Both can be used to define a set of values for a column. However, there are some advantages to using Enums:

*   Performance: You can query a single table instead of finding the value from a lookup table.
*   Simplicity: Generally the SQL is easier to read and write.

There are also some disadvantages to using Enums:

*   Limited Flexibility: Adding and removing values requires modifying the database schema (i.e.: using migrations) rather than adding data to a table.
*   Maintenance Overhead: Enum types require ongoing maintenance. If your application's requirements change frequently, maintaining enums can become burdensome.

In general you should only use Enums when the list of values is small, fixed, and unlikely to change often. Things like "a list of continents" or "a list of departments" are good candidates for Enums.



## Using enums in tables

To use the Enum in a table, you can define a column with the Enum type. For example:

{/* prettier-ignore */}

```sql
create table person (
  id serial primary key,
  name text,
  current_mood mood
);
```

Here, the `current_mood` column can only have values from the "mood" Enum.


### Inserting data with enums

You can insert data into a table with Enum columns by specifying one of the Enum values:

{/* prettier-ignore */}

```sql
insert into person
  (name, current_mood)
values
  ('Alice', 'happy');
```


### Querying data with enums

When querying data, you can filter and compare Enum values as usual:

{/* prettier-ignore */}

```sql
select * 
from person 
where current_mood = 'sad';
```



## Managing enums

You can manage your Enums using the `alter type` statement. Here are some examples:


### Updating enum values

You can update the value of an Enum column:

{/* prettier-ignore */}

```sql
update person
set current_mood = 'excited'
where name = 'Alice';
```


### Adding enum values

To add new values to an existing Postgres Enum, you can use the `ALTER TYPE` statement. Here's how you can do it:

Let's say you have an existing Enum called `mood`, and you want to add a new value, `content`:

{/* prettier-ignore */}

```sql
alter type mood add value 'content';
```


### Removing enum values

Even though it is possible, it is unsafe to remove enum values once they have been created. It's better to leave the enum value in place.

<Admonition type="caution">
  Read the [Postgres mailing list](https://www.postgresql.org/message-id/21012.1459434338%40sss.pgh.pa.us) for more information:

  There is no `ALTER TYPE DELETE VALUE` in Postgres. Even if you delete every occurrence of an Enum value within a table (and vacuumed away those rows), the target value could still exist in upper index pages. If you delete the `pg_enum` entry you'll break the index.
</Admonition>


### Getting a list of enum values

Check your existing Enum values by querying the enum\_range function:

{/* prettier-ignore */}

```sql
select enum_range(null::mood);
```



## Resources

*   Official Postgres Docs: [Enumerated Types](https://www.postgresql.org/docs/current/datatype-enum.html)



---
**Navigation:** [← Previous](./23-debugging-and-monitoring.md) | [Index](./index.md) | [Next →](./25-event-triggers.md)
