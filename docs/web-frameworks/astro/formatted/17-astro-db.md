---
title: "Astro DB"
section: 17
---

# Astro DB

> Learn how to use Astro DB, a fully-managed SQL database designed exclusively for Astro.

Astro DB is a fully-managed SQL database designed for the Astro ecosystem. Develop locally in Astro and deploy to any libSQL-compatible database.

Astro DB is a complete solution to configuring, developing, and querying your data. A local database is created in `.astro/content.db` whenever you run `astro dev` to manage your data without the need for Docker or a network connection.

## Installation

[Section titled “Installation”](#installation)

Install the [`@astrojs/db` integration](/en/guides/integrations-guide/db/) using the built-in `astro add` command:

* npm

  ```sh
  npx astro add db
  ```jsx
* pnpm

  ```sh
  pnpm astro add db
  ```jsx
* Yarn

  ```sh
  yarn astro add db
  ```jsx
## Define your database

[Section titled “Define your database”](#define-your-database)

Installing `@astrojs/db` with the `astro add` command will automatically create a `db/config.ts` file in your project where you will define your database tables:

db/config.ts

```ts
import { defineDb } from 'astro:db';


export default defineDb({
  tables: { },
})
```jsx
### Tables

[Section titled “Tables”](#tables)

Data in Astro DB is stored using SQL tables. Tables structure your data into rows and columns, where columns enforce the type of each row value.

Define your tables in your `db/config.ts` file by providing the structure of the data in your existing libSQL database, or the data you will collect in a new database. This will allow Astro to generate a TypeScript interface to query that table from your project. The result is full TypeScript support when you access your data with property autocompletion and type-checking.

To configure a database table, import and use the `defineTable()` and `column` utilities from `astro:db`. Then, define a name (case-sensitive) for your table and the type of data in each column.

This example configures a `Comment` table with required text columns for `author` and `body`. Then, makes it available to your project through the `defineDb()` export.

db/config.ts

```ts
import { defineDb, defineTable, column } from 'astro:db';


const Comment = defineTable({
  columns: {
    author: column.text(),
    body: column.text(),
  }
})


export default defineDb({
  tables: { Comment },
})
```jsx
See the [table configuration reference](/en/guides/integrations-guide/db/#table-configuration-reference) for a complete reference of table options.

### Columns

[Section titled “Columns”](#columns)

Astro DB supports the following column types:

db/config.ts

```ts
import { defineTable, column } from 'astro:db';


const Comment = defineTable({
  columns: {
    // A string of text.
    author: column.text(),
    // A whole integer value.
    likes: column.number(),
    // A true or false value.
    flagged: column.boolean(),
    // Date/time values queried as JavaScript Date objects.
    published: column.date(),
    // An untyped JSON object.
    metadata: column.json(),
  }
});
```jsx
See the [table columns reference](/en/guides/integrations-guide/db/#table-configuration-reference) for more details.

### Table References

[Section titled “Table References”](#table-references)

Relationships between tables are a common pattern in database design. For example, a `Blog` table may be closely related to other tables of `Comment`, `Author`, and `Category`.

You can define these relations between tables and save them into your database schema using **reference columns**. To establish a relationship, you will need:

* An **identifier column** on the referenced table. This is usually an `id` column with the `primaryKey` property.
* A column on the base table to **store the referenced `id`**. This uses the `references` property to establish a relationship.

This example shows a `Comment` table’s `authorId` column referencing an `Author` table’s `id` column.

db/config.ts

```ts
const Author = defineTable({
  columns: {
    id: column.number({ primaryKey: true }),
    name: column.text(),
  }
});


const Comment = defineTable({
  columns: {
    authorId: column.number({ references: () => Author.columns.id }),
    body: column.text(),
  }
});
```jsx
## Seed your database for development

[Section titled “Seed your database for development”](#seed-your-database-for-development)

In development, Astro will use your DB config to generate local types according to your schemas. These will be generated fresh from your seed file each time the dev server is started, and will allow you to query and work with the shape of your data with type safety and autocompletion.

You will not have access to production data during development unless you [connect to a remote database](#connecting-to-remote-databases) during development. This protects your data while allowing you to test and develop with a working database with type-safety.

To seed development data for testing and debugging into your Astro project, create a `db/seed.ts` file. Import both the `db` object and your tables defined in `astro:db`. `insert` some initial data into each table. This development data should match the form of both your database schema and production data.

The following example defines two rows of development data for a `Comment` table, and an `Author` table:

db/seed.ts

```ts
import { db, Comment, Author } from 'astro:db';


export default async function() {
  await db.insert(Author).values([
    { id: 1, name: "Kasim" },
    { id: 2, name: "Mina" },
  ]);


  await db.insert(Comment).values([
    { authorId: 1, body: 'Hope you like Astro DB!' },
    { authorId: 2, body: 'Enjoy!'},
  ])
}
```jsx
Your development server will automatically restart your database whenever this file changes, regenerating your types and seeding this development data from `seed.ts` fresh each time.

## Connect a libSQL database for production

[Section titled “Connect a libSQL database for production”](#connect-a-libsql-database-for-production)

Astro DB can connect to any local libSQL database or to any server that exposes the libSQL remote protocol, whether managed or self-hosted.

To connect Astro DB to a libSQL database, set the following environment variables obtained from your database provider:

* `ASTRO_DB_REMOTE_URL`: the connection URL to the location of your local or remote libSQL DB. This may include [URL configuration options](#remote-url-configuration-options) such as sync and encryption as parameters.
* `ASTRO_DB_APP_TOKEN`: the auth token to your libSQL server. This is required for remote databases, and not needed for [local DBs like files or in-memory](#url-scheme-and-host) databases

Depending on your service, you may have access to a CLI or web UI to retrieve these values. The following section will demonstrate connecting to Turso and setting these values as an example, but you are free to use any provider.

### Getting started with Turso

[Section titled “Getting started with Turso”](#getting-started-with-turso)

Turso is the company behind [libSQL](https://github.com/tursodatabase/libsql), the open-source fork of SQLite that powers Astro DB. They provide a fully managed libSQL database platform and are fully compatible with Astro.

The steps below will guide you through the process of installing the Turso CLI, logging in (or signing up), creating a new database, getting the required environmental variables, and pushing the schema to the remote database.

1. Install the [Turso CLI](https://docs.turso.tech/cli/installation).

2. [Log in or sign up](https://docs.turso.tech/cli/authentication) to Turso.

3. Create a new database. In this example the database name is `andromeda`.

   ```sh
   turso db create andromeda
   ```jsx
4. Run the `show` command to see information about the newly created database:

   ```sh
   turso db show andromeda
   ```jsx
   Copy the `URL` value and set it as the value for `ASTRO_DB_REMOTE_URL`.

   .env

   ```dotenv
   ASTRO_DB_REMOTE_URL=libsql://andromeda-houston.turso.io
   ```jsx
5. Create a new token to authenticate requests to the database:

   ```sh
   turso db tokens create andromeda
   ```jsx
   Copy the output of the command and set it as the value for `ASTRO_DB_APP_TOKEN`.

   .env

   ```diff
   ASTRO_DB_REMOTE_URL=libsql://andromeda-houston.turso.io
   +ASTRO_DB_APP_TOKEN=eyJhbGciOiJF...3ahJpTkKDw
   ```jsx
6. Push your DB schema and metadata to the new Turso database.

   ```sh
   astro db push --remote
   ```jsx
7. Congratulations, now you have a database connected! Give yourself a break. 👾

   ```sh
   turso relax
   ```jsx
To explore more features of Turso, check out the [Turso docs](https://docs.turso.tech).

### Connecting to remote databases

[Section titled “Connecting to remote databases”](#connecting-to-remote-databases)

Astro DB allows you to connect to both local and remote databases. By default, Astro uses a local database file for `dev` and `build` commands, recreating tables and inserting development seed data each time.

To connect to a hosted remote database, use the `--remote` flag. This flag enables both readable and writable access to your remote database, allowing you to [accept and persist user data](#insert) in production environments.

Configure your build command to use the `--remote` flag:

package.json

```json
{
  "scripts": {
    "build": "astro build --remote"
  }
}
```jsx
You can also use the flag directly in the command line:

```bash

---

[← Previous](16-actions.md) | [Index](index.md) | [Next →](index.md)
