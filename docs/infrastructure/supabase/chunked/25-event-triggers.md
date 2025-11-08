**Navigation:** [← Previous](./24-securing-your-data.md) | [Index](./index.md) | [Next →](./26-pg_stat_statements-query-performance-monitoring.md)

# Event Triggers

Automatically execute SQL on database events.

In Postgres, an [event trigger](https://www.postgresql.org/docs/current/event-triggers.html) is similar to a [trigger](/docs/guides/database/postgres/triggers), except that it is triggered by database level events (and is usually reserved for [superusers](/docs/guides/database/postgres/roles-superuser))

With our `Supautils` extension (installed automatically for all Supabase projects), the `postgres` user has the ability to create and manage event triggers.

Some use cases for event triggers are:

*   Capturing Data Definition Language (DDL) changes - these are changes to your database schema (though the [pgAudit](/docs/guides/database/extensions/pgaudit) extension provides a more complete solution)
*   Enforcing/monitoring/preventing actions - such as preventing tables from being dropped in Production or enforcing RLS on all new tables

The guide covers two example event triggers:

1.  Preventing accidental dropping of a table
2.  Automatically enabling Row Level Security on new tables in the `public` schema



## Creating an event trigger

Only the `postgres` user can create event triggers, so make sure you are authenticated as them. As with triggers, event triggers consist of 2 parts

1.  A [Function](/docs/guides/database/functions) which will be executed when the triggering event occurs
2.  The actual Event Trigger object, with parameters around when the trigger should be run


### Example trigger function - prevent dropping tables

This example protects any table from being dropped. You can override it by temporarily disabling the event trigger: `ALTER EVENT TRIGGER dont_drop_trigger DISABLE;`

```sql
-- Function
CREATE OR REPLACE FUNCTION dont_drop_function()
  RETURNS event_trigger LANGUAGE plpgsql AS $$
DECLARE
    obj record;
    tbl_name text;
BEGIN
    FOR obj IN SELECT * FROM pg_event_trigger_dropped_objects()
    LOOP
        IF obj.object_type = 'table' THEN
            RAISE EXCEPTION 'ERROR: All tables in this schema are protected and cannot be dropped';
        END IF;
    END LOOP;
END;
$$;

-- Event trigger
CREATE EVENT TRIGGER dont_drop_trigger
ON sql_drop
EXECUTE FUNCTION dont_drop_function();
```


### Example trigger function - auto enable Row Level Security

```sql
CREATE OR REPLACE FUNCTION rls_auto_enable()
RETURNS EVENT_TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = pg_catalog
AS $$
DECLARE
  cmd record;
BEGIN
  FOR cmd IN
    SELECT *
    FROM pg_event_trigger_ddl_commands()
    WHERE command_tag IN ('CREATE TABLE', 'CREATE TABLE AS', 'SELECT INTO')
      AND object_type IN ('table','partitioned table')
  LOOP
     IF cmd.schema_name IS NOT NULL AND cmd.schema_name IN ('public') AND cmd.schema_name NOT IN ('pg_catalog','information_schema') AND cmd.schema_name NOT LIKE 'pg_toast%' AND cmd.schema_name NOT LIKE 'pg_temp%' THEN
      BEGIN
        EXECUTE format('alter table if exists %s enable row level security', cmd.object_identity);
        RAISE LOG 'rls_auto_enable: enabled RLS on %', cmd.object_identity;
      EXCEPTION
        WHEN OTHERS THEN
          RAISE LOG 'rls_auto_enable: failed to enable RLS on %', cmd.object_identity;
      END;
     ELSE
        RAISE LOG 'rls_auto_enable: skip % (either system schema or not in enforced list: %.)', cmd.object_identity, cmd.schema_name;
     END IF;
  END LOOP;
END;
$$;

DROP EVENT TRIGGER IF EXISTS ensure_rls;
CREATE EVENT TRIGGER ensure_rls
ON ddl_command_end
WHEN TAG IN ('CREATE TABLE', 'CREATE TABLE AS', 'SELECT INTO')
EXECUTE FUNCTION rls_auto_enable();
```


### Event trigger Functions and firing events

Event triggers can be triggered on:

*   `ddl_command_start` - occurs just before a DDL command for almost all objects within a schema
*   `ddl_command_end` - occurs just after a DDL command for almost all objects within a schema
*   `sql_drop` - occurs just before `ddl_command_end` for any DDL commands that `DROP` a database object (note that altering a table can cause it to be dropped)
*   `table_rewrite` - occurs just before a table is rewritten using the `ALTER TABLE` command

<Admonition type="caution">
  Event triggers run for each DDL command specified above and can consume resources which may cause performance issues if not used carefully.
</Admonition>

Within each event trigger, helper functions exist to view the objects being modified or the command being run. For example, our example calls `pg_event_trigger_dropped_objects()` to view the object(s) being dropped. For a more comprehensive overview of these functions, read the [official event trigger definition documentation](https://www.postgresql.org/docs/current/event-trigger-definition.html)

To view the matrix commands that cause an event trigger to fire, read the [official event trigger matrix documentation](https://www.postgresql.org/docs/current/event-trigger-matrix.html)



## Disabling an event trigger

You can disable an event trigger using the `alter event trigger` command:

```sql
ALTER EVENT TRIGGER dont_drop_trigger DISABLE;
```



## Dropping an event trigger

You can delete a trigger using the `drop event trigger` command:

```sql
DROP EVENT TRIGGER dont_drop_trigger;
```



## Resources

*   Official Postgres Docs: [Event Trigger Behaviours](https://www.postgresql.org/docs/current/event-trigger-definition.html)
*   Official Postgres Docs: [Event Trigger Firing Matrix](https://www.postgresql.org/docs/current/event-trigger-matrix.html)
*   Supabase blog: [Postgres Event Triggers without superuser access](/blog/event-triggers-wo-superuser)



# Select first row for each group in PostgreSQL



Given a table `seasons`:

| id |    team   | points |
| -- | :-------: | -----: |
| 1  | Liverpool |     82 |
| 2  | Liverpool |     84 |
| 3  |  Brighton |     34 |
| 4  |  Brighton |     28 |
| 5  | Liverpool |     79 |

We want to find the rows containing the maximum number of points *per team*.

The expected output we want is:

| id |    team   | points |
| -- | :-------: | -----: |
| 3  |  Brighton |     34 |
| 2  | Liverpool |     84 |

From the [SQL Editor](/dashboard/project/_/sql), you can run a query like:

```sql
select distinct
  on (team) id,
  team,
  points
from
  seasons
order BY
  id,
  points desc,
  team;
```

The important bits here are:

*   The `desc` keyword to order the `points` from highest to lowest.
*   The `distinct` keyword that tells Postgres to only return a single row per team.

This query can also be executed via `psql` or any other query editor if you prefer to [connect directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).



# Managing Indexes in PostgreSQL



An index makes your Postgres queries faster. The index is like a "table of contents" for your data - a reference list which allows queries to quickly locate a row in a given table without needing to scan the entire table (which in large tables can take a long time).

Indexes can be structured in a few different ways. The type of index chosen depends on the values you are indexing. By far the most common index type, and the default in Postgres, is the B-Tree. A B-Tree is the generalized form of a binary search tree, where nodes can have more than two children.

Even though indexes improve query performance, the Postgres query planner may not always make use of a given index when choosing which optimizations to make. Additionally indexes come with some overhead - additional writes and increased storage - so it's useful to understand how and when to use indexes, if at all.



## Create an index

Let's take an example table:

```sql
create table persons (
  id bigint generated by default as identity primary key,
  age int,
  height int,
  weight int,
  name text,
  deceased boolean
);
```

<Admonition type="tip">
  All the queries in this guide can be run using the [SQL Editor](/dashboard/project/_/sql) in the Supabase Dashboard, or via `psql` if you're [connecting directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).
</Admonition>

We might want to frequently query users based on their age:

```sql
select name from persons where age = 32;
```

Without an index, Postgres will scan every row in the table to find equality matches on age.

You can verify this by doing an explain on the query:

```sql
explain select name from persons where age = 32;
```

Outputs:

```
Seq Scan on persons  (cost=0.00..22.75 rows=x width=y)
Filter: (age = 32)
```

To add a simple B-Tree index you can run:

```sql
create index idx_persons_age on persons (age);
```

<Admonition type="caution">
  It can take a long time to build indexes on large datasets and the default behaviour of `create index` is to lock the table from writes.

  Luckily Postgres provides us with `create index concurrently` which prevents blocking writes on the table, but does take a bit longer to build.
</Admonition>

Here is a simplified diagram of the index we just created (note that in practice, nodes actually have more than two children).

<Image
  alt="B-Tree index example in Postgres"
  zoomable
  src={{
    dark: '/docs/img/database/managing-indexes/creating-indexes.png',
    light: '/docs/img/database/managing-indexes/creating-indexes--light.png',
  }}
/>

You can see that in any large data set, traversing the index to locate a given value can be done in much less operations (O(log n)) than compared to scanning the table one value at a time from top to bottom (O(n)).



## Partial indexes

If you are frequently querying a subset of rows then it may be more efficient to build a partial index. In our example, perhaps we only want to match on `age` where `deceased is false`. We could build a partial index:

```sql
create index idx_living_persons_age on persons (age)
where deceased is false;
```



## Ordering indexes

By default B-Tree indexes are sorted in ascending order, but sometimes you may want to provide a different ordering. Perhaps our application has a page featuring the top 10 oldest people. Here we would want to sort in descending order, and include `NULL` values last. For this we can use:

```sql
create index idx_persons_age_desc on persons (age desc nulls last);
```



## Reindexing

After a while indexes can become stale and may need rebuilding. Postgres provides a `reindex` command for this, but due to Postgres locks being placed on the index during this process, you may want to make use of the `concurrent` keyword.

```sql
reindex index concurrently idx_persons_age;
```

Alternatively you can reindex all indexes on a particular table:

```sql
reindex table concurrently persons;
```

Take note that `reindex` can be used inside a transaction, but `reindex [index/table] concurrently` cannot.



## Index Advisor

Indexes can improve query performance of your tables as they grow. The Supabase Dashboard offers an Index Advisor, which suggests potential indexes to add to your tables.

For more information on the Index Advisor and its suggestions, see the [`index_advisor` extension](/docs/guides/database/extensions/index_advisor).

To use the Dashboard Index Advisor:

1.  Go to the [Query Performance](/dashboard/project/_/advisors/query-performance) page.
2.  Click on a query to bring up the Details side panel.
3.  Select the Indexes tab.
4.  Enable Index Advisor if prompted.


### Understanding Index Advisor results

The Indexes tab shows the existing indexes used in the selected query. Note that indexes suggested in the "New Index Recommendations" section may not be used when you create them. Postgres' query planner may intentionally ignore an available index if it determines that the query will be faster without. For example, on a small table, a sequential scan might be faster than an index scan. In that case, the planner will switch to using the index as the table size grows, helping to future proof the query.

If additional indexes might improve your query, the Index Advisor shows the suggested indexes with the estimated improvement in startup and total costs:

*   Startup cost is the cost to fetch the first row
*   Total cost is the cost to fetch all the rows

Costs are in arbitrary units, where a single sequential page read costs 1.0 units.



# Roles, superuser access and unsupported operations



Supabase provides the default `postgres` role to all instances deployed. Superuser access is not given as it allows destructive operations to be performed on the database.

To ensure you are not impacted by this, additional privileges are granted to the `postgres` user to allow it to run some operations that are normally restricted to superusers.

However, this does mean that some operations, that typically require `superuser` privileges, are not available on Supabase. These are documented below:



## Unsupported operations

*   `COPY ... FROM PROGRAM`
*   `ALTER USER ... WITH SUPERUSER`



# Postgres Roles

Managing access to your Postgres database and configuring permissions.

Postgres manages database access permissions using the concept of roles. Generally you wouldn't use these roles for your own application - they are mostly for configuring *system access* to your database. If you want to configure *application access*, then you should use [Row Level Security](/docs/guides/database/postgres/row-level-security) (RLS). You can also implement [Role-based Access Control](/docs/guides/database/postgres/custom-claims-and-role-based-access-control-rbac) on top of RLS.



## Users vs roles

In Postgres, roles can function as users or groups of users. Users are roles with login privileges, while groups (also known as role groups) are roles that don't have login privileges but can be used to manage permissions for multiple users.



## Creating roles

You can create a role using the `create role` command:

```sql
create role "role_name";
```



## Creating users

Roles and users are essentially the same in Postgres, however if you want to use password-logins for a specific role, then you can use `WITH LOGIN PASSWORD`:

```sql
create role "role_name" with login password 'extremely_secure_password';
```



## Passwords

Your Postgres database is the core of your Supabase project, so it's important that every role has a strong, secure password at all times. Here are some tips for creating a secure password:

*   Use a password manager to generate it.
*   Make a long password (12 characters at least).
*   Don't use any common dictionary words.
*   Use both upper and lower case characters, numbers, and special symbols.


### Special symbols in passwords

If you use special symbols in your Postgres password, you must remember to [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding) your password later if using the Postgres connection string, for example, `postgresql://postgres.projectref:p%3Dword@aws-0-us-east-1.pooler.supabase.com:6543/postgres`


### Changing your project password

When you created your project you were also asked to enter a password. This is the password for the `postgres` role in your database. You can update this from the Dashboard under the [Database Settings](/dashboard/project/_/database/settings) page. You should *never* give this to third-party service unless you absolutely trust them. Instead, we recommend that you create a new user for every service that you want to give access too. This will also help you with debugging - you can see every query that each role is executing in your database within `pg_stat_statements`.

Changing the password does not result in any downtime. All connected services, such as PostgREST, PgBouncer, and other Supabase managed services, are automatically updated to use the latest password to ensure availability. However, if you have any external services connecting to the Supabase database using hardcoded username/password credentials, a manual update will be required.



## Granting permissions

Roles can be granted various permissions on database objects using the `GRANT` command. Permissions include `SELECT`, `INSERT`, `UPDATE`, and `DELETE`. You can configure access to almost any object inside your database - including tables, views, functions, and triggers.



## Revoking permissions

Permissions can be revoked using the `REVOKE` command:

```sql
REVOKE permission_type ON object_name FROM role_name;
```



## Role hierarchy

Roles can be organized in a hierarchy, where one role can inherit permissions from another. This simplifies permission management, as you can define permissions at a higher level and have them automatically apply to all child roles.


### Role inheritance

To create a role hierarchy, you first need to create the parent and child roles. The child role will inherit permissions from its parent. Child roles can be added using the INHERIT option when creating the role:

```sql
create role "child_role_name" inherit "parent_role_name";
```


### Preventing inheritance

In some cases, you might want to prevent a role from having a child relationship (typically superuser roles). You can prevent inheritance relations using `NOINHERIT`:

```sql
alter role "child_role_name" noinherit;
```



## Supabase roles

Postgres comes with a set of [predefined roles](https://www.postgresql.org/docs/current/predefined-roles.html). Supabase extends this with a default set of roles which are configured on your database when you start a new project:


### `postgres`

The default Postgres role. This has admin privileges.


### `anon`

For unauthenticated, public access. This is the role which the API (PostgREST) will use when a user *is not* logged in.


### `authenticator`

A special role for the API (PostgREST). It has very limited access, and is used to validate a JWT and then
"change into" another role determined by the JWT verification.


### `authenticated`

For "authenticated access." This is the role which the API (PostgREST) will use when a user *is* logged in.


### `service_role`

For elevated access. This role is used by the API (PostgREST) to bypass Row Level Security.


### `supabase_auth_admin`

Used by the Auth middleware to connect to the database and run migration. Access is scoped to the `auth` schema.


### `supabase_storage_admin`

Used by the Auth middleware to connect to the database and run migration. Access is scoped to the `storage` schema.


### `dashboard_user`

For running commands via the Supabase UI.


### `supabase_admin`

An internal role Supabase uses for administrative tasks, such as running upgrades and automations.



## Resources

*   Official Postgres docs: [Database Roles](https://www.postgresql.org/docs/current/database-roles.html)
*   Official Postgres docs: [Role Membership](https://www.postgresql.org/docs/current/role-membership.html)
*   Official Postgres docs: [Function Permissions](https://www.postgresql.org/docs/current/perm-functions.html)



# Row Level Security

Secure your data using Postgres Row Level Security.

When you need granular authorization rules, nothing beats Postgres's [Row Level Security (RLS)](https://www.postgresql.org/docs/current/ddl-rowsecurity.html).



## Row Level Security in Supabase

<Admonition type="danger">
  Supabase allows convenient and secure data access from the browser, as long as you enable RLS.

  RLS *must* always be enabled on any tables stored in an exposed schema. By default, this is the `public` schema.

  RLS is enabled by default on tables created with the Table Editor in the dashboard. If you create one in raw SQL or with the SQL editor, remember to enable RLS yourself:

  ```sql
  alter table <schema_name>.<table_name>
  enable row level security;
  ```
</Admonition>

RLS is incredibly powerful and flexible, allowing you to write complex SQL rules that fit your unique business needs. RLS can be combined with [Supabase Auth](/docs/guides/auth) for end-to-end user security from the browser to the database.

RLS is a Postgres primitive and can provide "[defense in depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\))" to protect your data from malicious actors even when accessed through third-party tooling.



## Policies

[Policies](https://www.postgresql.org/docs/current/sql-createpolicy.html) are Postgres's rule engine. Policies are easy to understand once you get the hang of them. Each policy is attached to a table, and the policy is executed every time a table is accessed.

You can just think of them as adding a `WHERE` clause to every query. For example a policy like this ...

```sql
create policy "Individuals can view their own todos."
on todos for select
using ( (select auth.uid()) = user_id );
```

.. would translate to this whenever a user tries to select from the todos table:

```sql
select *
from todos
where auth.uid() = todos.user_id;
-- Policy is implicitly added.
```



## Enabling Row Level Security

You can enable RLS for any table using the `enable row level security` clause:

```sql
alter table "table_name" enable row level security;
```

Once you have enabled RLS, no data will be accessible via the [API](/docs/guides/api) when using the public `anon` key, until you create policies.

<Admonition type="caution" label="`auth.uid()` Returns `null` When Unauthenticated">
  When a request is made without an authenticated user (e.g., no access token is provided or the session has expired), `auth.uid()` returns `null`.

  This means that a policy like:

  ```sql
  USING (auth.uid() = user_id)
  ```

  will silently fail for unauthenticated users, because:

  ```sql
  null = user_id
  ```

  is always false in SQL.

  To avoid confusion and make your intention clear, we recommend explicitly checking for authentication:

  ```sql
  USING (auth.uid() IS NOT NULL AND auth.uid() = user_id)
  ```
</Admonition>



## Authenticated and unauthenticated roles

Supabase maps every request to one of the roles:

*   `anon`: an unauthenticated request (the user is not logged in)
*   `authenticated`: an authenticated request (the user is logged in)

These are actually [Postgres Roles](/docs/guides/database/postgres/roles). You can use these roles within your Policies using the `TO` clause:

```sql
create policy "Profiles are viewable by everyone"
on profiles for select
to authenticated, anon
using ( true );

-- OR

create policy "Public profiles are viewable only by authenticated users"
on profiles for select
to authenticated
using ( true );
```

<Admonition type="note" label="Anonymous user vs the anon key">
  Using the `anon` Postgres role is different from an [anonymous user](/docs/guides/auth/auth-anonymous) in Supabase Auth. An anonymous user assumes the `authenticated` role to access the database and can be differentiated from a permanent user by checking the `is_anonymous` claim in the JWT.
</Admonition>



## Creating policies

Policies are SQL logic that you attach to a Postgres table. You can attach as many policies as you want to each table.

Supabase provides some [helpers](#helper-functions) that simplify RLS if you're using Supabase Auth. We'll use these helpers to illustrate some basic policies:


### SELECT policies

You can specify select policies with the `using` clause.

Let's say you have a table called `profiles` in the public schema and you want to enable read access to everyone.

```sql
-- 1. Create table
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

-- 2. Enable RLS
alter table profiles enable row level security;

-- 3. Create Policy
create policy "Public profiles are visible to everyone."
on profiles for select
to anon         -- the Postgres Role (recommended)
using ( true ); -- the actual Policy
```

Alternatively, if you only wanted users to be able to see their own profiles:

```sql
create policy "User can see their own profile only."
on profiles
for select using ( (select auth.uid()) = user_id );
```


### INSERT policies

You can specify insert policies with the `with check` clause. The `with check` expression ensures that any new row data adheres to the policy constraints.

Let's say you have a table called `profiles` in the public schema and you only want users to be able to create a profile for themselves. In that case, we want to check their User ID matches the value that they are trying to insert:

```sql
-- 1. Create table
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

-- 2. Enable RLS
alter table profiles enable row level security;

-- 3. Create Policy
create policy "Users can create a profile."
on profiles for insert
to authenticated                          -- the Postgres Role (recommended)
with check ( (select auth.uid()) = user_id );      -- the actual Policy
```


### UPDATE policies

You can specify update policies by combining both the `using` and `with check` expressions.

The `using` clause represents the condition that must be true for the update to be allowed, and `with check` clause ensures that the updates made adhere to the policy constraints.

Let's say you have a table called `profiles` in the public schema and you only want users to be able to update their own profile.

You can create a policy where the `using` clause checks if the user owns the profile being updated. And the `with check` clause ensures that, in the resultant row, users do not change the `user_id` to a value that is not equal to their User ID, maintaining that the modified profile still meets the ownership condition.

```sql
-- 1. Create table
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

-- 2. Enable RLS
alter table profiles enable row level security;

-- 3. Create Policy
create policy "Users can update their own profile."
on profiles for update
to authenticated                    -- the Postgres Role (recommended)
using ( (select auth.uid()) = user_id )       -- checks if the existing row complies with the policy expression
with check ( (select auth.uid()) = user_id ); -- checks if the new row complies with the policy expression
```

If no `with check` expression is defined, then the `using` expression will be used both to determine which rows are visible (normal USING case) and which new rows will be allowed to be added (WITH CHECK case).

<Admonition type="caution">
  To perform an `UPDATE` operation, a corresponding [`SELECT` policy](#select-policies) is required. Without a `SELECT` policy, the `UPDATE` operation will not work as expected.
</Admonition>


### DELETE policies

You can specify delete policies with the `using` clause.

Let's say you have a table called `profiles` in the public schema and you only want users to be able to delete their own profile:

```sql
-- 1. Create table
create table profiles (
  id uuid primary key,
  user_id uuid references auth.users,
  avatar_url text
);

-- 2. Enable RLS
alter table profiles enable row level security;

-- 3. Create Policy
create policy "Users can delete a profile."
on profiles for delete
to authenticated                     -- the Postgres Role (recommended)
using ( (select auth.uid()) = user_id );      -- the actual Policy
```


### Views

Views bypass RLS by default because they are usually created with the `postgres` user. This is a feature of Postgres, which automatically creates views with `security definer`.

In Postgres 15 and above, you can make a view obey the RLS policies of the underlying tables when invoked by `anon` and `authenticated` roles by setting `security_invoker = true`.

```sql
create view <VIEW_NAME>
with(security_invoker = true)
as select <QUERY>
```

In older versions of Postgres, protect your views by revoking access from the `anon` and `authenticated` roles, or by putting them in an unexposed schema.



## Helper functions

Supabase provides some helper functions that make it easier to write Policies.


### `auth.uid()`

Returns the ID of the user making the request.


### `auth.jwt()`

<Admonition type="caution">
  Not all information present in the JWT should be used in RLS policies. For instance, creating an RLS policy that relies on the `user_metadata` claim can create security issues in your application as this information can be modified by authenticated end users.
</Admonition>

Returns the JWT of the user making the request. Anything that you store in the user's `raw_app_meta_data` column or the `raw_user_meta_data` column will be accessible using this function. It's important to know the distinction between these two:

*   `raw_user_meta_data` - can be updated by the authenticated user using the `supabase.auth.update()` function. It is not a good place to store authorization data.
*   `raw_app_meta_data` - cannot be updated by the user, so it's a good place to store authorization data.

The `auth.jwt()` function is extremely versatile. For example, if you store some team data inside `app_metadata`, you can use it to determine whether a particular user belongs to a team. For example, if this was an array of IDs:

```sql
create policy "User is in team"
on my_table
to authenticated
using ( team_id in (select auth.jwt() -> 'app_metadata' -> 'teams'));
```

<Admonition type="caution">
  Keep in mind that a JWT is not always "fresh". In the example above, even if you remove a user from a team and update the `app_metadata` field, that will not be reflected using `auth.jwt()` until the user's JWT is refreshed.

  Also, if you are using Cookies for Auth, then you must be mindful of the JWT size. Some browsers are limited to 4096 bytes for each cookie, and so the total size of your JWT should be small enough to fit inside this limitation.
</Admonition>


### MFA

The `auth.jwt()` function can be used to check for [Multi-Factor Authentication](/docs/guides/auth/auth-mfa#enforce-rules-for-mfa-logins). For example, you could restrict a user from updating their profile unless they have at least 2 levels of authentication (Assurance Level 2):

```sql
create policy "Restrict updates."
on profiles
as restrictive
for update
to authenticated using (
  (select auth.jwt()->>'aal') = 'aal2'
);
```



## Bypassing Row Level Security

Supabase provides special "Service" keys, which can be used to bypass RLS. These should never be used in the browser or exposed to customers, but they are useful for administrative tasks.

<Admonition type="note">
  Supabase will adhere to the RLS policy of the signed-in user, even if the client library is initialized with a Service Key.
</Admonition>

You can also create new [Postgres Roles](/docs/guides/database/postgres/roles) which can bypass Row Level Security using the "bypass RLS" privilege:

```sql
alter role "role_name" with bypassrls;
```

This can be useful for system-level access. You should *never* share login credentials for any Postgres Role with this privilege.



## RLS performance recommendations

Every authorization system has an impact on performance. While row level security is powerful, the performance impact is important to keep in mind. This is especially true for queries that scan every row in a table - like many `select` operations, including those using limit, offset, and ordering.

Based on a series of [tests](https://github.com/GaryAustin1/RLS-Performance), we have a few recommendations for RLS:


### Add indexes

Make sure you've added [indexes](/docs/guides/database/postgres/indexes) on any columns used within the Policies which are not already indexed (or primary keys). For a Policy like this:

```sql
create policy "rls_test_select" on test_table
to authenticated
using ( (select auth.uid()) = user_id );
```

You can add an index like:

```sql
create index userid
on test_table
using btree (user_id);
```


#### Benchmarks

| Test                                                                                          | Before (ms) | After (ms) | % Improvement | Change                                                                                                       |
| --------------------------------------------------------------------------------------------- | ----------- | ---------- | ------------- | ------------------------------------------------------------------------------------------------------------ |
| [test1-indexed](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test1-indexed) | 171         | \< 0.1     | 99.94%        | <details className="cursor-pointer">Before:<br />No index<br /><br />After:<br />`user_id` indexed</details> |


### Call functions with `select`

You can use `select` statement to improve policies that use functions. For example, instead of this:

```sql
create policy "rls_test_select" on test_table
to authenticated
using ( auth.uid() = user_id );
```

You can do:

```sql
create policy "rls_test_select" on test_table
to authenticated
using ( (select auth.uid()) = user_id );
```

This method works well for JWT functions like `auth.uid()` and `auth.jwt()` as well as `security definer` Functions. Wrapping the function causes an `initPlan` to be run by the Postgres optimizer, which allows it to "cache" the results per-statement, rather than calling the function on each row.

<Admonition type="caution">
  You can only use this technique if the results of the query or function do not change based on the row data.
</Admonition>


#### Benchmarks

| Test                                                                                                                              | Before (ms) | After (ms) | % Improvement | Change                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [test2a-wrappedSQL-uid](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test2a-wrappedSQL-uid\(\))                 | 179         | 9          | 94.97%        | <details className="cursor-pointer">Before:<br />`auth.uid() = user_id` <br /><br />After:<br /> `(select auth.uid()) = user_id`</details>                                    |
| [test2b-wrappedSQL-isadmin](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test2b-wrappedSQL-isadmin\(\))         | 11,000      | 7          | 99.94%        | <details className="cursor-pointer">Before:<br />`is_admin()` *table join*<br /><br />After:<br />`(select is_admin())` *table join*</details>                                |
| [test2c-wrappedSQL-two-functions](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test2c-wrappedSQL-two-functions) | 11,000      | 10         | 99.91%        | <details className="cursor-pointer">Before:<br />`is_admin() OR auth.uid() = user_id`<br /><br />After:<br />`(select is_admin()) OR (select auth.uid() = user_id)`</details> |
| [test2d-wrappedSQL-sd-fun](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test2d-wrappedSQL-sd-fun)               | 178,000     | 12         | 99.993%       | <details className="cursor-pointer">Before:<br />`has_role() = role` <br /><br />After:<br />(select has\_role()) = role</details>                                            |
| [test2e-wrappedSQL-sd-fun-array](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test2e-wrappedSQL-sd-fun-array)   | 173000      | 16         | 99.991%       | <details className="cursor-pointer">Before:<br />`team_id=any(user_teams())` <br /><br />After:<br />team\_id=any(array(select user\_teams()))</details>                      |


### Add filters to every query

Policies are "implicit where clauses," so it's common to run `select` statements without any filters. This is a bad pattern for performance. Instead of doing this (JS client example):

{/* prettier-ignore */}

```js
const { data } = supabase
  .from('table')
  .select()
```

You should always add a filter:

{/* prettier-ignore */}

```js
const { data } = supabase
  .from('table')
  .select()
  .eq('user_id', userId)
```

Even though this duplicates the contents of the Policy, Postgres can use the filter to construct a better query plan.


#### Benchmarks

| Test                                                                                              | Before (ms) | After (ms) | % Improvement | Change                                                                                                                                     |
| ------------------------------------------------------------------------------------------------- | ----------- | ---------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [test3-addfilter](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test3-addfilter) | 171         | 9          | 94.74%        | <details className="cursor-pointer">Before:<br />`auth.uid() = user_id`<br /><br />After:<br />add `.eq` or `where` on `user_id`</details> |


### Use security definer functions

A "security definer" function runs using the same role that *created* the function. This means that if you create a role with a superuser (like `postgres`), then that function will have `bypassrls` privileges. For example, if you had a policy like this:

```sql
create policy "rls_test_select" on test_table
to authenticated
using (
  exists (
    select 1 from roles_table
    where (select auth.uid()) = user_id and role = 'good_role'
  )
);
```

We can instead create a `security definer` function which can scan `roles_table` without any RLS penalties:

```sql
create function private.has_good_role()
returns boolean
language plpgsql
security definer -- will run as the creator
as $$
begin
  return exists (
    select 1 from roles_table
    where (select auth.uid()) = user_id and role = 'good_role'
  );
end;
$$;

-- Update our policy to use this function:
create policy "rls_test_select"
on test_table
to authenticated
using ( (select private.has_good_role()) );
```

<Admonition type="caution">
  Security-definer functions should never be created in a schema in the "Exposed schemas" inside your [API settings](/dashboard/project/_/settings/api)\`.
</Admonition>


### Minimize joins

You can often rewrite your Policies to avoid joins between the source and the target table. Instead, try to organize your policy to fetch all the relevant data from the target table into an array or set, then you can use an `IN` or `ANY` operation in your filter.

For example, this is an example of a slow policy which joins the source `test_table` to the target `team_user`:

```sql
create policy "rls_test_select" on test_table
to authenticated
using (
  (select auth.uid()) in (
    select user_id
    from team_user
    where team_user.team_id = team_id -- joins to the source "test_table.team_id"
  )
);
```

We can rewrite this to avoid this join, and instead select the filter criteria into a set:

```sql
create policy "rls_test_select" on test_table
to authenticated
using (
  team_id in (
    select team_id
    from team_user
    where user_id = (select auth.uid()) -- no join
  )
);
```

In this case you can also consider [using a `security definer` function](#use-security-definer-functions) to bypass RLS on the join table:

<Admonition type="note">
  If the list exceeds 1000 items, a different approach may be needed or you may need to analyze the approach to ensure that the performance is acceptable.
</Admonition>


#### Benchmarks

| Test                                                                                                | Before (ms) | After (ms) | % Improvement | Change                                                                                                                                                |
| --------------------------------------------------------------------------------------------------- | ----------- | ---------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [test5-fixed-join](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test5-fixed-join) | 9,000       | 20         | 99.78%        | <details className="cursor-pointer">Before:<br />`auth.uid()` in table join on col<br /><br />After:<br />col in table join on `auth.uid()`</details> |


### Specify roles in your policies

Always use the Role of inside your policies, specified by the `TO` operator. For example, instead of this query:

```sql
create policy "rls_test_select" on rls_test
using ( auth.uid() = user_id );
```

Use:

```sql
create policy "rls_test_select" on rls_test
to authenticated
using ( (select auth.uid()) = user_id );
```

This prevents the policy `( (select auth.uid()) = user_id )` from running for any `anon` users, since the execution stops at the `to authenticated` step.


#### Benchmarks

| Test                                                                                          | Before (ms) | After (ms) | % Improvement | Change                                                                                                                               |
| --------------------------------------------------------------------------------------------- | ----------- | ---------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [test6-To-role](https://github.com/GaryAustin1/RLS-Performance/tree/main/tests/test6-To-role) | 170         | \< 0.1     | 99.78%        | <details className="cursor-pointer">Before:<br />No `TO` policy<br /><br />After:<br />`TO authenticated` (anon accessing)</details> |



## More resources

*   [Testing your database](/docs/guides/database/testing)
*   [Row Level Security and Supabase Auth](/docs/guides/database/postgres/row-level-security)
*   [RLS Guide and Best Practices](https://github.com/orgs/supabase/discussions/14576)
*   Community repo on testing RLS using [pgTAP and dbdev](https://github.com/usebasejump/supabase-test-helpers/tree/main)



# Replicate to another Postgres database using Logical Replication



For this example, you will need:

*   A Supabase project
*   A Postgres database (running v10 or newer)

You will be running commands on both of these databases to publish changes from the Supabase database to the external database.

1.  Create a `publication` on the **Supabase database**:

```sql
CREATE PUBLICATION example_pub;
```

2.  Also on the **Supabase database**, create a `replication slot`:

```sql
select pg_create_logical_replication_slot('example_slot', 'pgoutput');
```

3.  Now we will connect to our **external database** and subscribe to our `publication` Note: ):

<Admonition type="note">
  This will need a **direct** connection (not a Connection Pooler) to your database and you can find the connection info in the [**Connect** panel](/dashboard/project/_?showConnect=true) in the `Direct connection` section.

  You will also need to ensure that IPv6 is supported by your replication destination (or you can enable the [IPv4 add-on](/docs/guides/platform/ipv4-address))

  If you would prefer not to use the `postgres` user, then you can run `CREATE ROLE <user> WITH REPLICATION;` using the `postgres` user.
</Admonition>

```sql
CREATE SUBSCRIPTION example_sub
CONNECTION 'host=db.oaguxblfdassqxvvwtfe.supabase.co user=postgres password=YOUR_PASS dbname=postgres'
PUBLICATION example_pub
WITH (copy_data = true, create_slot=false, slot_name=example_slot);
```

<Admonition type="note">
  `create_slot` is set to `false` because `slot_name` is provided and the slot was already created in Step 2.
  To copy data from before the slot was created, set `copy_data` to `true`.
</Admonition>

4.  Now we'll go back to the Supabase DB and add all the tables that you want replicated to the publication.

```sql
ALTER PUBLICATION example_pub ADD TABLE example_table;
```

5.  Check the replication status using `pg_stat_replication`

```sql
select * from pg_stat_replication;
```

<Admonition type="note">
  You can add more tables to the initial publication, but you're going to need to do a REFRESH on the subscribing database.
  See [https://www.postgresql.org/docs/current/sql-alterpublication.html](https://www.postgresql.org/docs/current/sql-alterpublication.html)
</Admonition>



# Timeouts

Extend database timeouts to execute longer transactions

<Admonition type="note">
  Dashboard and [Client](/docs/guides/api/rest/client-libs) queries have a max-configurable timeout of 60 seconds. For longer transactions, use [Supavisor or direct connections](/docs/guides/database/connecting-to-postgres#quick-summary).
</Admonition>



## Change Postgres timeout

You can change the Postgres timeout at the:

1.  [Session level](#session-level)
2.  [Function level](#function-level)
3.  [Global level](#global-level)
4.  [Role level](#role-level)


### Session level

Session level settings persist only for the duration of the connection.

Set the session timeout by running:

```sql
set statement_timeout = '10min';
```

Because it applies to sessions only, it can only be used with connections through Supavisor in session mode (port 5432) or a direct connection. It cannot be used in the Dashboard, with the Supabase Client API, nor with Supavisor in Transaction mode (port 6543).

This is most often used for single, long running, administrative tasks, such as creating an HSNW index. Once the setting is implemented, you can view it by executing:

```sql
SHOW statement_timeout;
```

See the full guide on [changing session timeouts](https://github.com/orgs/supabase/discussions/21133).


### Function level

This works with the Database REST API when called from the Supabase client libraries:

```sql
create or replace function myfunc()
returns void as $$
 select pg_sleep(3); -- simulating some long-running process
$$
language sql
set statement_timeout TO '4s'; -- set custom timeout
```

This is mostly for recurring functions that need a special exemption for runtimes.


### Role level

This sets the timeout for a specific role.

The default role timeouts are:

*   `anon`: 3s
*   `authenticated`: 8s
*   `service_role`: none (defaults to the `authenticator` role's 8s timeout if unset)
*   `postgres`: none (capped by default global timeout to be 2min)

Run the following query to change a role's timeout:

```sql
alter role example_role set statement_timeout = '10min'; -- could also use seconds '10s'
```

<Admonition type="tip">
  If you are changing the timeout for the Supabase Client API calls, you will need to reload PostgREST to reflect the timeout changes by running the following script:

  ```sql
  NOTIFY pgrst, 'reload config';
  ```
</Admonition>

Unlike global settings, the result cannot be checked with `SHOW
statement_timeout`. Instead, run:

```sql
select
  rolname,
  rolconfig
from pg_roles
where
  rolname in (
    'anon',
    'authenticated',
    'postgres',
    'service_role'
    -- ,<ANY CUSTOM ROLES>
  );
```


### Global level

This changes the statement timeout for all roles and sessions without an explicit timeout already set.

```sql
alter database postgres set statement_timeout TO '4s';
```

Check if your changes took effect:

```sql
show statement_timeout;
```

Although not necessary, if you are uncertain if a timeout has been applied, you can run a quick test:

```sql
create or replace function myfunc()
returns void as $$
  select pg_sleep(601); -- simulating some long-running process
$$
language sql;
```



## Identifying timeouts

The Supabase Dashboard contains tools to help you identify timed-out and long-running queries.


### Using the Logs Explorer

Go to the [Logs Explorer](/dashboard/project/_/logs/explorer), and run the following query to identify timed-out events (`statement timeout`) and queries that successfully run for longer than 10 seconds (`duration`).

```sql
select
  cast(postgres_logs.timestamp as datetime) as timestamp,
  event_message,
  parsed.error_severity,
  parsed.user_name,
  parsed.query,
  parsed.detail,
  parsed.hint,
  parsed.sql_state_code,
  parsed.backend_type
from
  postgres_logs
  cross join unnest(metadata) as metadata
  cross join unnest(metadata.parsed) as parsed
where
  regexp_contains(event_message, 'duration|statement timeout')
  -- (OPTIONAL) MODIFY OR REMOVE
  and parsed.user_name = 'authenticator' -- <--------CHANGE
order by timestamp desc
limit 100;
```


### Using the Query Performance page

Go to the [Query Performance page](/dashboard/project/_/advisors/query-performance?preset=slowest_execution) and filter by relevant role and query speeds. This only identifies slow-running but successful queries. Unlike the Log Explorer, it does not show you timed-out queries.


### Understanding roles in logs

Each API server uses a designated user for connecting to the database:

| Role                         | API/Tool                                                                  |
| ---------------------------- | ------------------------------------------------------------------------- |
| `supabase_admin`             | Used by Realtime and for project configuration                            |
| `authenticator`              | PostgREST                                                                 |
| `supabase_auth_admin`        | Auth                                                                      |
| `supabase_storage_admin`     | Storage                                                                   |
| `supabase_replication_admin` | Synchronizes Read Replicas                                                |
| `postgres`                   | Supabase Dashboard and External Tools (e.g., Prisma, SQLAlchemy, PSQL...) |
| Custom roles                 | External Tools (e.g., Prisma, SQLAlchemy, PSQL...)                        |

Filter by the `parsed.user_name` field to only retrieve logs made by specific users:

```sql
-- find events based on role/server
... query
where
  -- find events from the relevant role
  parsed.user_name = '<ROLE>'
```



# Postgres Triggers

Automatically execute SQL on table events.

In Postgres, a trigger executes a set of actions automatically on table events such as INSERTs, UPDATEs, DELETEs, or TRUNCATE operations.



## Creating a trigger

Creating triggers involve 2 parts:

1.  A [Function](/docs/guides/database/functions) which will be executed (called the Trigger Function)
2.  The actual Trigger object, with parameters around when the trigger should be run.

An example of a trigger is:

```sql
create trigger "trigger_name"
after insert on "table_name"
for each row
execute function trigger_function();
```



## Trigger functions

A trigger function is a user-defined [Function](/docs/guides/database/functions) that Postgres executes when the trigger is fired.


### Example trigger function

Here is an example that updates `salary_log` whenever an employee's salary is updated:

```sql
-- Example: Update salary_log when salary is updated
create function update_salary_log()
returns trigger
language plpgsql
as $$
begin
  insert into salary_log(employee_id, old_salary, new_salary)
  values (new.id, old.salary, new.salary);
  return new;
end;
$$;

create trigger salary_update_trigger
after update on employees
for each row
execute function update_salary_log();
```


### Trigger variables

Trigger functions have access to several special variables that provide information about the context of the trigger event and the data being modified. In the example above you can see the values inserted into the salary log are `old.salary` and `new.salary` - in this case `old` specifies the previous values and `new` specifies the updated values.

Here are some of the key variables and options available within trigger functions:

*   `TG_NAME`: The name of the trigger being fired.
*   `TG_WHEN`: The timing of the trigger event (`BEFORE` or `AFTER`).
*   `TG_OP`: The operation that triggered the event (`INSERT`, `UPDATE`, `DELETE`, or `TRUNCATE`).
*   `OLD`: A record variable holding the old row's data in `UPDATE` and `DELETE` triggers.
*   `NEW`: A record variable holding the new row's data in `UPDATE` and `INSERT` triggers.
*   `TG_LEVEL`: The trigger level (`ROW` or `STATEMENT`), indicating whether the trigger is row-level or statement-level.
*   `TG_RELID`: The object ID of the table on which the trigger is being fired.
*   `TG_TABLE_NAME`: The name of the table on which the trigger is being fired.
*   `TG_TABLE_SCHEMA`: The schema of the table on which the trigger is being fired.
*   `TG_ARGV`: An array of string arguments provided when creating the trigger.
*   `TG_NARGS`: The number of arguments in the `TG_ARGV` array.



## Types of triggers

There are two types of trigger, `BEFORE` and `AFTER`:


### Trigger before changes are made

Executes before the triggering event.

```sql
create trigger before_insert_trigger
before insert on orders
for each row
execute function before_insert_function();
```


### Trigger after changes are made

Executes after the triggering event.

```sql
create trigger after_delete_trigger
after delete on customers
for each row
execute function after_delete_function();
```



## Execution frequency

There are two options available for executing triggers:

*   `for each row`: specifies that the trigger function should be executed once for each affected row.
*   `for each statement`: the trigger is executed once for the entire operation (for example, once on insert). This can be more efficient than `for each row` when dealing with multiple rows affected by a single SQL statement, as they allow you to perform calculations or updates on groups of rows at once.



## Dropping a trigger

You can delete a trigger using the `drop trigger` command:

```sql
drop trigger "trigger_name" on "table_name";
```

If your trigger is inside a restricted schema, you won't be able to drop it due to permission restrictions. In those cases, you can drop the function it depends on instead using the CASCADE clause to automatically remove all triggers that call it:

```sql
drop function if exists restricted_schema.function_name() cascade;
```

Make sure you take a backup of the function before removing it in case you're planning to recreate it later.



## Resources

*   Official Postgres Docs: [Triggers](https://www.postgresql.org/docs/current/triggers.html)
*   Official Postgres Docs: [Overview of Trigger Behavior](https://www.postgresql.org/docs/current/trigger-definition.html)
*   Official Postgres Docs: [CREATE TRIGGER](https://www.postgresql.org/docs/current/sql-createtrigger.html)



# Print PostgreSQL version



It's important to know which version of Postgres you are running as each major version has different features and may cause breaking changes. You may also need to update your schema when [upgrading](https://www.postgresql.org/docs/current/pgupgrade.html) or downgrading to a major Postgres version.

Run the following query using the [SQL Editor](/dashboard/project/_/sql) in the Supabase Dashboard:

```sql
select
  version();
```

Which should return something like:

```sql
PostgreSQL 15.1 on aarch64-unknown-linux-gnu, compiled by gcc (Ubuntu 10.3.0-1ubuntu1~20.04) 10.3.0, 64-bit
```

This query can also be executed via `psql` or any other query editor if you prefer to [connect directly to the database](/docs/guides/database/connecting-to-postgres#direct-connections).



# http: RESTful Client



The `http` extension allows you to call RESTful endpoints within Postgres.



## Quick demo

<div className="video-container">
  <iframe src="https://www.youtube-nocookie.com/embed/rARgrELRCwY" frameBorder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</div>



## Overview

Let's cover some basic concepts:

*   REST: stands for REpresentational State Transfer. It's a way to request data from external services.
*   RESTful APIs are servers which accept HTTP "calls". The calls are typically:
    *   `GET` − Read only access to a resource.
    *   `POST` − Creates a new resource.
    *   `DELETE` − Removes a resource.
    *   `PUT` − Updates an existing resource or creates a new resource.

You can use the `http` extension to make these network requests from Postgres.



## Usage


### Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `http` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "http" extension
    create extension http with schema extensions;

    -- Example: disable the "http" extension
    drop extension if exists http;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>


### Available functions

While the main usage is `http('http_request')`, there are 5 wrapper functions for specific functionality:

*   `http_get()`
*   `http_post()`
*   `http_put()`
*   `http_delete()`
*   `http_head()`


### Returned values

A successful call to a web URL from the `http` extension returns a record with the following fields:

*   `status`: integer
*   `content_type`: character varying
*   `headers`: http\_header\[]
*   `content`: character varying. Typically you would want to cast this to `jsonb` using the format `content::jsonb`



## Examples


### Simple `GET` example

```sql
select
  "status", "content"::jsonb
from
  extensions.http_get('https://jsonplaceholder.typicode.com/todos/1');
```


### Simple `POST` example

```sql
select
  "status", "content"::jsonb
from
  extensions.http_post(
    'https://jsonplaceholder.typicode.com/posts',
    '{ "title": "foo", "body": "bar", "userId": 1 }',
    'application/json'
  );
```



## Resources

*   Official [`http` GitHub Repository](https://github.com/pramsey/pgsql-http)



# HypoPG: Hypothetical indexes



`HypoPG` is Postgres extension for creating hypothetical/virtual indexes. HypoPG allows users to rapidly create hypothetical/virtual indexes that have no resource cost (CPU, disk, memory) that are visible to the Postgres query planner.

The motivation for HypoPG is to allow users to quickly search for an index to improve a slow query without consuming server resources or waiting for them to build.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `hypopg` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "hypopg" extension
    create extension hypopg with schema extensions;

    -- Disable the "hypopg" extension
    drop extension if exists hypopg;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>


### Speeding up a query

Given the following table and a simple query to select from the table by `id`:

{/* prettier-ignore */}

```sql
create table account (
  id int,
  address text
);

insert into account(id, address)
select
  id,
  id || ' main street'
from
  generate_series(1, 10000) id;
```

We can generate an explain plan for a description of how the Postgres query planner
intends to execute the query.

{/* prettier-ignore */}

```sql
explain select * from account where id=1;

                      QUERY PLAN
-------------------------------------------------------
 Seq Scan on account  (cost=0.00..180.00 rows=1 width=13)
   Filter: (id = 1)
(2 rows)
```

Using HypoPG, we can create a hypothetical index on the `account(id)` column to check if it would be useful to the query planner and then re-run the explain plan.

Note that the virtual indexes created by HypoPG are only visible in the Postgres connection that they were created in. Supabase connects to Postgres through a connection pooler so the `hypopg_create_index` statement and the `explain` statement should be executed in a single query.

{/* prettier-ignore */}

```sql
select * from hypopg_create_index('create index on account(id)');

explain select * from account where id=1;

                                     QUERY PLAN
------------------------------------------------------------------------------------
 Index Scan using <13504>btree_account_id on hypo  (cost=0.29..8.30 rows=1 width=13)
   Index Cond: (id = 1)
(2 rows)
```

The query plan has changed from a `Seq Scan` to an `Index Scan` using the newly created virtual index, so we may choose to create a real version of the index to improve performance on the target query:

{/* prettier-ignore */}

```sql
create index on account(id);
```



## Functions

*   [`hypo_create_index(text)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#create-a-hypothetical-index): A function to create a hypothetical index.
*   [`hypopg_list_indexes`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A View that lists all hypothetical indexes that have been created.
*   [`hypopg()`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function that lists all hypothetical indexes that have been created with the same format as `pg_index`.
*   [`hypopg_get_index_def(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to display the `create index` statement that would create the index.
*   [`hypopg_get_relation_size(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to estimate how large a hypothetical index would be.
*   [`hypopg_drop_index(oid)`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to remove a given hypothetical index by `oid`.
*   [`hypopg_reset()`](https://hypopg.readthedocs.io/en/rel1_stable/usage.html#manipulate-hypothetical-indexes): A function to remove all hypothetical indexes.



## Resources

*   Official [HypoPG documentation](https://hypopg.readthedocs.io/en/rel1_stable/)



# index_advisor: query optimization



[Index advisor](https://github.com/supabase/index_advisor) is a Postgres extension for recommending indexes to improve query performance.

Features:

*   Supports generic parameters e.g. `$1`, `$2`
*   Supports materialized views
*   Identifies tables/columns obfuscated by views
*   Skips duplicate indexes

`index_advisor` is accessible directly through Supabase Studio by navigating to the [Query Performance Report](/dashboard/project/_/advisors/query-performance) and selecting a query and then the "indexes" tab.

![Supabase Studio index\_advisor integration.](/docs/img/index_advisor_studio.png)

Alternatively, you can use index\_advisor directly via SQL.

For example:

```sql
select
    *
from
  index_advisor('select book.id from book where title = $1');

 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------
 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}
(1 row)
```



## Installation

To get started, enable index\_advisor by running

```sql
create extension index_advisor;
```



## API

Index advisor exposes a single function `index_advisor(query text)` that accepts a query and searches for a set of SQL DDL `create index` statements that improve the query's execution time.

The function's signature is:

```sql
index_advisor(query text)
returns
    table  (
        startup_cost_before jsonb,
        startup_cost_after jsonb,
        total_cost_before jsonb,
        total_cost_after jsonb,
        index_statements text[],
        errors text[]
    )
```



## Usage

As a minimal example, the `index_advisor` function can be given a single table query with a filter on an unindexed column.

```sql
create extension if not exists index_advisor cascade;

create table book(
  id int primary key,
  title text not null
);

select
  *
from
  index_advisor('select book.id from book where title = $1');

 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                   | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------+--------
 0.00                | 1.17               | 25.88             | 6.40             | {"CREATE INDEX ON public.book USING btree (title)"},| {}
(1 row)
```

and will return a row recommending an index on the unindexed column.

More complex queries may generate additional suggested indexes:

```sql
create extension if not exists index_advisor cascade;

create table author(
    id serial primary key,
    name text not null
);

create table publisher(
    id serial primary key,
    name text not null,
    corporate_address text
);

create table book(
    id serial primary key,
    author_id int not null references author(id),
    publisher_id int not null references publisher(id),
    title text
);

create table review(
    id serial primary key,
    book_id int references book(id),
    body text not null
);

select
    *
from
    index_advisor('
        select
            book.id,
            book.title,
            publisher.name as publisher_name,
            author.name as author_name,
            review.body review_body
        from
            book
            join publisher
                on book.publisher_id = publisher.id
            join author
                on book.author_id = author.id
            join review
                on book.id = review.book_id
        where
            author.id = $1
            and publisher.id = $2
    ');

 startup_cost_before | startup_cost_after | total_cost_before | total_cost_after |                  index_statements                         | errors
---------------------+--------------------+-------------------+------------------+-----------------------------------------------------------+--------
 27.26               | 12.77              | 68.48             | 42.37            | {"CREATE INDEX ON public.book USING btree (author_id)",   | {}
                                                                                    "CREATE INDEX ON public.book USING btree (publisher_id)",
                                                                                    "CREATE INDEX ON public.review USING btree (book_id)"}
(3 rows)
```



## Limitations

*   index\_advisor will only recommend single column, B-tree indexes. More complex indexes will be supported in future releases.
*   when a generic argument's type is not discernible from context, an error is returned in the `errors` field. To resolve those errors, add explicit type casting to the argument. e.g. `$1::int`.



## Resources

*   [`index_advisor`](https://github.com/supabase/index_advisor) repo



# pg_cron: Schedule Recurring Jobs with Cron Syntax in Postgres



See the [Supabase Cron docs](/docs/guides/cron).



# pg_graphql: GraphQL for PostgreSQL



[pg\_graphql](https://supabase.github.io/pg_graphql/) is Postgres extension for interacting with the database using [GraphQL](https://graphql.org) instead of SQL.

The extension reflects a GraphQL schema from the existing SQL schema and exposes it through a SQL function, `graphql.resolve(...)`. This enables any programming language that can connect to Postgres to query the database via GraphQL with no additional servers, processes, or libraries.

The `pg_graphql` resolve method is designed to interop with [PostgREST](https://postgrest.org/en/stable/index.html), the tool that underpins the Supabase API, such that the `graphql.resolve` function can be called via RPC to safely and performantly expose the GraphQL API over HTTP/S.

For more information about how the SQL schema is reflected into a GraphQL schema, see the [pg\_graphql API docs](https://supabase.github.io/pg_graphql/api/).



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "pg\_graphql" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pg_graphql" extension
    create extension pg_graphql;

    -- Disable the "pg_graphql" extension
    drop extension if exists pg_graphql;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension you can call `drop extension`.
  </TabPanel>
</Tabs>



## Usage

Given a table

{/* prettier-ignore */}

```sql
create table "Blog"(
  id serial primary key,
  name text not null,
  description text
);

insert into "Blog"(name)
values ('My Blog');
```

The reflected GraphQL schema can be queried immediately as

{/* prettier-ignore */}

```sql
select
  graphql.resolve($$
    {
      blogCollection(first: 1) {
        edges {
          node {
            id,
            name
          }
        }
      }
    }
  $$);
```

returning the JSON

{/* prettier-ignore */}

```json
{
  "data": {
    "blogCollection": {
      "edges": [
        {
          "node": {
            "id": 1
            "name": "My Blog"
          }
        }
      ]
    }
  }
}
```

Note that `pg_graphql` fully supports schema introspection so you can connect any GraphQL IDE or schema inspection tool to see the full set of fields and arguments available in the API.



## API

*   [`graphql.resolve`](https://supabase.github.io/pg_graphql/sql_interface/): A SQL function for executing GraphQL queries.



## Resources

*   Official [`pg_graphql` documentation](https://github.com/supabase/pg_graphql)



# pg_hashids: Short UIDs



[pg\_hashids](https://github.com/iCyberon/pg_hashids) provides a secure way to generate short, unique, non-sequential ids from numbers. The hashes are intended to be small, easy-to-remember identifiers that can be used to obfuscate data (optionally) with a password, alphabet, and salt. For example, you may wish to hide data like user IDs, order numbers, or tracking codes in favor of `pg_hashid`'s unique identifiers.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "pg\_hashids" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pg_hashids" extension
    create extension pg_hashids with schema extensions;

    -- Disable the "pg_hashids" extension
    drop extension if exists pg_hashids;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep your `public` schema clean.
  </TabPanel>
</Tabs>



## Usage

Suppose we have a table that stores order information, and we want to give customers a unique identifier without exposing the sequential `id` column. To do this, we can use `pg_hashid`'s `id_encode` function.

```sql
create table orders (
  id serial primary key,
  description text,
  price_cents bigint
);

insert into orders (description, price_cents)
values ('a book', 9095);

select
  id,
  id_encode(id) as short_id,
  description,
  price_cents
from
  orders;

  id | short_id | description | price_cents
----+----------+-------------+-------------
  1 | jR       | a book      |        9095
(1 row)
```

To reverse the `short_id` back into an `id`, there is an equivalent function named `id_decode`.



## Resources

*   Official [pg\_hashids documentation](https://github.com/iCyberon/pg_hashids)



# pg_jsonschema: JSON Schema Validation



[JSON Schema](https://json-schema.org) is a language for annotating and validating JSON documents. [`pg_jsonschema`](https://github.com/supabase/pg_jsonschema) is a Postgres extension that adds the ability to validate PostgreSQL's built-in `json` and `jsonb` data types against JSON Schema documents.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for `pg_jsonschema` and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Enable the "pg_jsonschema" extension
    create extension pg_jsonschema with schema extensions;

    -- Disable the "pg_jsonschema" extension
    drop extension if exists pg_jsonschema;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of enabling the extension.
    To disable an extension you can call `drop extension`.

    It's good practice to create the extension within a separate schema (like `extensions`) to keep the `public` schema clean.
  </TabPanel>
</Tabs>



## Functions

*   [`json_matches_schema(schema json, instance json)`](https://github.com/supabase/pg_jsonschema#api): Checks if a `json` *instance* conforms to a JSON Schema *schema*.
*   [`jsonb_matches_schema(schema json, instance jsonb)`](https://github.com/supabase/pg_jsonschema#api): Checks if a `jsonb` *instance* conforms to a JSON Schema *schema*.



## Usage

Since `pg_jsonschema` exposes its utilities as functions, we can execute them with a select statement:

{/* prettier-ignore */}

```sql
select
  extensions.json_matches_schema(
    schema := '{"type": "object"}',
    instance := '{}'
  );
```

`pg_jsonschema` is generally used in tandem with a [check constraint](https://www.postgresql.org/docs/current/ddl-constraints.html) as a way to constrain the contents of a json/b column to match a JSON Schema.

{/* prettier-ignore */}

```sql
create table customer(
    id serial primary key,
    ...
    metadata json,

    check (
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
    )
);

-- Example: Valid Payload
insert into customer(metadata)
values ('{"tags": ["vip", "darkmode-ui"]}');
-- Result:
--   INSERT 0 1

-- Example: Invalid Payload
insert into customer(metadata)
values ('{"tags": [1, 3]}');
-- Result:
--   ERROR:  new row for relation "customer" violates check constraint "customer_metadata_check"
--   DETAIL:  Failing row contains (2, {"tags": [1, 3]}).
```



## Resources

*   Official [`pg_jsonschema` documentation](https://github.com/supabase/pg_jsonschema)



# pg_net: Async Networking



<Admonition type="caution">
  The pg\_net API is in beta. Functions signatures may change.
</Admonition>

[pg\_net](https://github.com/supabase/pg_net/) enables Postgres to make asynchronous HTTP/HTTPS requests in SQL. It differs from the [`http`](/docs/guides/database/extensions/http) extension in that it is asynchronous by default. This makes it useful in blocking functions (like triggers).

It eliminates the need for servers to continuously poll for database changes and instead allows the database to proactively notify external resources about significant events.



## Enable the extension

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "pg\_net" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    ```sql
    -- Example: enable the "pg_net" extension.
    create extension pg_net;
    -- Note: The extension creates its own schema/namespace named "net" to avoid naming conflicts.

    -- Example: disable the "pg_net" extension
    drop extension if exists pg_net;
    drop schema net;
    ```

    Even though the SQL code is `create extension`, this is the equivalent of "enabling the extension".
    To disable an extension, call `drop extension`.

    Procedural languages are automatically installed within `pg_catalog`, so you don't need to specify a schema.
  </TabPanel>
</Tabs>



## `http_get`

Creates an HTTP GET request returning the request's ID. HTTP requests are not started until the transaction is committed.


### Signature \[#get-signature]

<Admonition type="caution">
  This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function.
</Admonition>

```sql
net.http_get(
    -- url for the request
    url text,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint

    strict
    volatile
    parallel safe
    language plpgsql
```


### Usage \[#get-usage]

```sql
select
    net.http_get('https://news.ycombinator.com')
    as request_id;
request_id
----------
         1
(1 row)
```



## `http_post`

Creates an HTTP POST request with a JSON body, returning the request's ID. HTTP requests are not started until the transaction is committed.

The body's character set encoding matches the database's `server_encoding` setting.


### Signature \[#post-signature]

<Admonition type="caution">
  This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function
</Admonition>

```sql
net.http_post(
    -- url for the request
    url text,
    -- body of the POST request
    body jsonb default '{}'::jsonb,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{"Content-Type": "application/json"}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint

    volatile
    parallel safe
    language plpgsql
```


### Usage \[#post-usage]

```sql
select
    net.http_post(
        url:='https://httpbin.org/post',
        body:='{"hello": "world"}'::jsonb
    ) as request_id;
request_id
----------
         1
(1 row)
```



## `http_delete`

Creates an HTTP DELETE request, returning the request's ID. HTTP requests are not started until the transaction is committed.


### Signature \[#post-signature]

<Admonition type="caution">
  This is a Postgres [SECURITY DEFINER](/docs/guides/database/postgres/row-level-security#use-security-definer-functions) function
</Admonition>

```sql
net.http_delete(
    -- url for the request
    url text,
    -- key/value pairs to be url encoded and appended to the `url`
    params jsonb default '{}'::jsonb,
    -- key/values to be included in request headers
    headers jsonb default '{}'::jsonb,
    -- the maximum number of milliseconds the request may take before being canceled
    timeout_milliseconds int default 2000
)
    -- request_id reference
    returns bigint

    strict
    volatile
    parallel safe
    language plpgsql
    security definer
```


### Usage \[#delete-usage]

```sql
select
    net.http_delete(
        'https://dummy.restapiexample.com/api/v1/delete/2'
    ) as request_id;
----------
         1
(1 row)
```



## Analyzing responses

Waiting requests are stored in the `net.http_request_queue` table. Upon execution, they are deleted.

```sql
CREATE UNLOGGED TABLE
    net.http_request_queue (
        id bigint NOT NULL DEFAULT nextval('net.http_request_queue_id_seq'::regclass),
        method text NOT NULL,
        url text NOT NULL,
        headers jsonb NOT NULL,
        body bytea NULL,
        timeout_milliseconds integer NOT NULL
    )
```

Once a response is returned, by default, it is stored for 6 hours in the `net._http_response` table.

```sql
CREATE UNLOGGED TABLE
    net._http_response (
        id bigint NULL,
        status_code integer NULL,
        content_type text NULL,
        headers jsonb NULL,
        content text NULL,
        timed_out boolean NULL,
        error_msg text NULL,
        created timestamp with time zone NOT NULL DEFAULT now()
    )
```

The responses can be observed with the following query:

```sql
select * from net._http_response;
```

The data can also be observed in the `net` schema with the [Supabase Dashboard's SQL Editor](/dashboard/project/_/editor)



## Debugging requests


### Inspecting request data

The [Postman Echo API](https://documenter.getpostman.com/view/5025623/SWTG5aqV) returns a response with the same body and content
as the request. It can be used to inspect the data being sent.

Sending a post request to the echo API

```sql
select
    net.http_post(
        url := 'https://postman-echo.com/post',
        body := '{"key1": "value", "key2": 5}'::jsonb
    ) as request_id;
```

Inspecting the echo API response content to ensure it contains the right body

```sql
select
    "content"
from net._http_response
where id = <request_id>
-- returns information about the request
-- including the body sent: {"key": "value", "key": 5}
```

Alternatively, by wrapping a request in a [database function](/docs/guides/database/functions), sent row data can be logged or returned for inspection and debugging.

```sql
create or replace function debugging_example (row_id int)
returns jsonb as $$
declare
    -- Store payload data
    row_data_var jsonb;
begin
    -- Retrieve row data and convert to JSON
    select to_jsonb("<example_table>".*) into row_data_var
    from "<example_table>"
    where "<example_table>".id = row_id;

    -- Initiate HTTP POST request to URL
    perform
        net.http_post(
            url := 'https://postman-echo.com/post',
            -- Use row data as payload
            body := row_data_var
        ) as request_id;

    -- Optionally Log row data or other data for inspection in Supabase Dashboard's Postgres Logs
    raise log 'Logging an entire row as JSON (%)', row_data_var;

    -- return row data to inspect
    return row_data_var;

-- Handle exceptions here if needed
exception
    when others then
        raise exception 'An error occurred: %', SQLERRM;
end;
$$ language plpgsql;

-- calling function
select debugging_example(<row_id>);
```


### Inspecting failed requests

Finds all failed requests

```sql
select
  *
from net._http_response
where "status_code" >= 400 or "error_msg" is not null
order by "created" desc;
```



## Configuration

<Admonition type="note" label="Must be on pg_net v0.12.0 or above to reconfigure ">
  Supabase supports reconfiguring pg\*net starting from v0.12.0+. For the latest release, initiate a Postgres upgrade in the [Infrastructure Settings](/dashboard/project/*/settings/infrastructure).
</Admonition>

The extension is configured to reliably execute up to 200 requests per second. The response messages are stored for only 6 hours to prevent needless buildup. The default behavior can be modified by rewriting config variables.


### Get current settings

```sql
select
  "name",
  "setting"
from pg_settings
where "name" like 'pg_net%';
```


### Alter settings

Change variables:

```sql
alter role "postgres" set pg_net.ttl to '24 hours';
alter role "postgres" set pg_net.batch_size to 500;
```

Then reload the settings and restart the `pg_net` background worker with:

```sql
select net.worker_restart();
```



## Examples


### Invoke a Supabase Edge Function

Make a POST request to a Supabase Edge Function with auth header and JSON body payload:

```sql
select
    net.http_post(
        url:='https://project-ref.supabase.co/functions/v1/function-name',
        headers:='{"Content-Type": "application/json", "Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,
        body:='{"name": "pg_net"}'::jsonb
    ) as request_id;
```


### Call an endpoint every minute with [pg\_cron](/docs/guides/database/extensions/pgcron)

The pg\_cron extension enables Postgres to become its own cron server. With it you can schedule regular calls with up to a minute precision to endpoints.

```sql
select cron.schedule(
	'cron-job-name',
	'* * * * *', -- Executes every minute (cron syntax)
	$$
	    -- SQL query
	    select "net"."http_post"(
            -- URL of Edge function
            url:='https://project-ref.supabase.co/functions/v1/function-name',
            headers:='{"Authorization": "Bearer <YOUR_ANON_KEY>"}'::jsonb,
            body:='{"name": "pg_net"}'::jsonb
	    ) as "request_id";
	$$
);
```


### Execute pg\_net in a trigger

Make a call to an external endpoint when a trigger event occurs.

```sql
-- function called by trigger
create or replace function <function_name>()
    returns trigger
    language plpgSQL
as $$
begin
    -- calls pg_net function net.http_post
    -- sends request to postman API
    perform "net"."http_post"(
      'https://postman-echo.com/post'::text,
      jsonb_build_object(
        'old_row', to_jsonb(old.*),
        'new_row', to_jsonb(new.*)
      ),
      headers:='{"Content-Type": "application/json"}'::jsonb
    ) as request_id;
    return new;
END $$;

-- trigger for table update
create trigger <trigger_name>
    after update on <table_name>
    for each row
    execute function <function_name>();
```


### Send multiple table rows in one request

```sql
with "selected_table_rows" as (
    select
        -- Converts all the rows into a JSONB array
        jsonb_agg(to_jsonb(<table_name>.*)) as JSON_payload
    from <table_name>
    -- good practice to LIMIT the max amount of rows
)
select
    net.http_post(
        url := 'https://postman-echo.com/post'::text,
        body := JSON_payload
    ) AS request_id
FROM "selected_table_rows";
```

More examples can be seen on the [Extension's GitHub page](https://github.com/supabase/pg_net/)



## Limitations

*   To improve speed and performance, the requests and responses are stored in [unlogged tables](https://pgpedia.info/u/unlogged-table.html), which are not preserved during a crash or unclean shutdown.
*   By default, response data is saved for only 6 hours
*   Can only make POST requests with JSON data. No other data formats are supported
*   Intended to handle at most 200 requests per second. Increasing the rate can introduce instability
*   Does not have support for PATCH/PUT requests
*   Can only work with one database at a time. It defaults to the `postgres` database.



## Resources

*   Source code: [github.com/supabase/pg\_net](https://github.com/supabase/pg_net/)
*   Official Docs: [github.com/supabase/pg\_net](https://github.com/supabase/pg_net/)



# pg_plan_filter: Restrict Total Cost



[`pg_plan_filter`](https://github.com/pgexperts/pg_plan_filter) is Postgres extension to block execution of statements where query planner's estimate of the total cost exceeds a threshold. This is intended to give database administrators a way to restrict the contribution an individual query has on database load.



## Enable the extension

The extension is already enabled by default via `shared_preload_libraries` setting.

You can follow the instructions below.



## API

`plan_filter.statement_cost_limit`: restricts the maximum total cost for executed statements
`plan_filter.limit_select_only`: restricts to `select` statements

Note that `limit_select_only = true` is not the same as read-only because `select` statements may modify data, for example, through a function call.



## Example

To demonstrate total cost filtering, we'll compare how `plan_filter.statement_cost_limit` treats queries that are under and over its cost limit. First, we set up a table with some data:

{/* prettier-ignore */}

```sql
create table book(
  id int primary key
);
-- CREATE TABLE

insert into book(id) select * from generate_series(1, 10000);
-- INSERT 0 10000
```

Next, we can review the explain plans for a single record select, and a whole table select.

{/* prettier-ignore */}

```sql
explain select * from book where id =1;
                                QUERY PLAN
---------------------------------------------------------------------------
 Index Only Scan using book_pkey on book  (cost=0.28..2.49 rows=1 width=4)
   Index Cond: (id = 1)
(2 rows)

explain select * from book;
                       QUERY PLAN
---------------------------------------------------------
 Seq Scan on book  (cost=0.00..135.00 rows=10000 width=4)
(1 row)
```

Now we can choose a `statement_cost_filter` value between the total cost for the single select (2.49) and the whole table select (135.0) so one statement will succeed and one will fail.

{/* prettier-ignore */}

```sql
set plan_filter.statement_cost_limit = 50; -- between 2.49 and 135.0

select * from book where id = 1;
 id
----
  1
(1 row)
-- SUCCESS
```

{/* prettier-ignore */}

```sql
select * from book;

ERROR:  plan cost limit exceeded
HINT:  The plan for your query shows that it would probably have an excessive run time. This may be due to a logic error in the SQL, or it maybe just a very costly query. Rewrite your query or increase the configuration parameter "plan_filter.statement_cost_limit".
-- FAILURE
```



## Resources

*   Official [`pg_plan_filter` documentation](https://github.com/pgexperts/pg_plan_filter)



# pg_repack: Physical storage optimization and maintenance



[pg\_repack](https://github.com/reorg/pg_repack) is a Postgres extension to remove bloat from tables and indexes, and optionally restore the physical order of clustered indexes. Unlike CLUSTER and VACUUM FULL, pg\_repack runs "online" and does not hold a exclusive locks on the processed tables that could prevent ongoing database operations. pg\_repack's efficiency is comparable to using CLUSTER directly.

pg\_repack provides the following methods to optimize physical storage:

*   Online CLUSTER: ordering table data by cluster index in a non-blocking way
*   Ordering table data by specified columns
*   Online VACUUM FULL: packing rows only in a non-blocking way
*   Rebuild or relocate only the indexes of a table

pg\_repack has 2 components, the database extension and a client-side CLI to control it.



## Requirements

*   A target table must have a PRIMARY KEY, or a UNIQUE total index on a NOT NULL column.
*   Performing a full-table repack requires free disk space about twice as large as the target table and its indexes.

pg\_repack requires the Postgres superuser role by default. That role is not available to users on the Supabase platform. To avoid that requirement, use the `-k` or `--no-superuser-check` flags on every `pg_repack` CLI command.

The first version of pg\_repack with full support for non-superuser repacking is 1.5.2. You can check the version installed on your Supabase instance using

```sql
select default_version
from pg_available_extensions
where name = 'pg_repack';
```

If pg\_repack is not present, or the version is \< 1.5.2, [upgrade to the latest version](/docs/guides/platform/upgrading) of Supabase to gain access.



## Usage


### Enable the extension

Get started with pg\_repack by enabling the extension in the Supabase Dashboard.

<Tabs scrollable size="small" type="underlined" defaultActiveId="dashboard" queryGroup="database-method">
  <TabPanel id="dashboard" label="Dashboard">
    1.  Go to the [Database](/dashboard/project/_/database/tables) page in the Dashboard.
    2.  Click on **Extensions** in the sidebar.
    3.  Search for "pg\_repack" and enable the extension.
  </TabPanel>

  <TabPanel id="sql" label="SQL">
    {/* prettier-ignore */}

    ```sql
    -- Example: enable the "pg_repack" extension
    create extension pg_repack with schema extensions;
    ```
  </TabPanel>
</Tabs>


### Install the CLI

Select an option from the pg\_repack docs to [install the client CLI](https://reorg.github.io/pg_repack/#download).


### Syntax

All pg\_repack commands should include the `-k` flag to skip the client-side superuser check.

{/* prettier-ignore */}

```sh
pg_repack -k [OPTION]... [DBNAME]
```



## Example

Perform an online `VACUUM FULL` on the tables `public.foo` and `public.bar` in the database `postgres`:

{/* prettier-ignore */}

```sh
pg_repack -k -h db.<PROJECT_REF>.supabase.co -p 5432 -U postgres -d postgres --no-order --table public.foo --table public.bar
```

See the [official pg\_repack documentation](https://reorg.github.io/pg_repack/) for the full list of options.



## Limitations

*   pg\_repack cannot reorganize temporary tables.
*   pg\_repack cannot cluster tables by GiST indexes.
*   You cannot perform DDL commands of the target tables except VACUUM or ANALYZE while pg\_repack is working.
    pg\_repack holds an ACCESS SHARE lock on the target table to enforce this restriction.



## Resources

*   [Official pg\_repack documentation](https://reorg.github.io/pg_repack/)



---
**Navigation:** [← Previous](./24-securing-your-data.md) | [Index](./index.md) | [Next →](./26-pg_stat_statements-query-performance-monitoring.md)
