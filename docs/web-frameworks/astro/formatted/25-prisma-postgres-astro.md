---
title: "Prisma Postgres & Astro"
section: 25
---

# Prisma Postgres & Astro

> Add a serverless Postgres database to your Astro project with Prisma Postgres

[Prisma Postgres](https://www.prisma.io/) is a fully managed, serverless Postgres database built for modern web apps.

## Connect via Prisma ORM (Recommended)

[Section titled “Connect via Prisma ORM (Recommended)”](#connect-via-prisma-orm-recommended)

[Prisma ORM](https://www.prisma.io/orm) is the recommended way to connect to your Prisma Postgres database. It provides type-safe queries, migrations, and global performance.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project with an adapter installed to enable [on-demand rendering (SSR)](/en/guides/on-demand-rendering/).

### Install dependencies and initialize Prisma

[Section titled “Install dependencies and initialize Prisma”](#install-dependencies-and-initialize-prisma)

Run the following commands to install the necessary Prisma dependencies:

```bash
npm install prisma tsx --save-dev
npm install @prisma/extension-accelerate @prisma/client
```jsx
Once installed, initialize Prisma in your project with the following command:

```bash
npx prisma init --db --output ../src/generated/prisma
```jsx
You’ll need to answer a few questions while setting up your Prisma Postgres database. Select the region closest to your location and a memorable name for your database, like “My Astro Project.”

This will create:

* A `prisma/` directory with a `schema.prisma` file
* A `.env` file with a `DATABASE_URL` already set

### Define a Model

[Section titled “Define a Model”](#define-a-model)

Even if you don’t need any specific data models yet, Prisma requires at least one model in the schema in order to generate a client and apply migrations.

The following example defines a `Post` model as a placeholder. Add the model to your schema to get started. You can safely delete or replace it later with models that reflect your actual data.

Update the generator provider from `prisma-client-js` to `prisma-client` in your `prisma/schema.prisma` file:

prisma/schema.prisma

```diff
generator client {
  provider = "prisma-client"
  output   = "../src/generated/prisma"
}


datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}


+model Post {
  +id        Int     @id @default(autoincrement())
  +title     String
  +content   String?
  +published Boolean @default(false)
+}
```jsx
Learn more about configuring your Prisma ORM setup in the [Prisma schema reference](https://www.prisma.io/docs/concepts/components/prisma-schema).

### Generate migration files

[Section titled “Generate migration files”](#generate-migration-files)

Run the following command to create the database tables and generate the Prisma Client from your schema. This will also create a `prisma/migrations/` directory with migration history files.

```bash
npx prisma migrate dev --name init
```jsx
### Create a Prisma Client

[Section titled “Create a Prisma Client”](#create-a-prisma-client)

Inside of `/src/lib`, create a `prisma.ts` file. This file will initialize and export your Prisma Client instance so you can query your database throughout your Astro project.

src/lib/prisma.ts

```typescript
import { PrismaClient } from "../generated/prisma/client";
import { withAccelerate } from "@prisma/extension-accelerate";


const prisma = new PrismaClient({
  datasourceUrl: import.meta.env.DATABASE_URL,
}).$extends(withAccelerate());


export default prisma;
```jsx
### Querying and displaying data

[Section titled “Querying and displaying data”](#querying-and-displaying-data)

The following example shows fetching only your published posts with the Prisma Client sorted by `id`, and then displaying titles and post content in your Astro template:

src/pages/posts.astro

```astro
---
import prisma from '../lib/prisma';


const posts = await prisma.post.findMany({
  where: { published: true },
  orderBy: { id: 'desc' }
});
---


<html>
  <head>
    <title>Published Posts</title>
  </head>
  <body>
    <h1>Published Posts</h1>
    <ul>
      {posts.map((post) => (
        <li>
          <h2>{post.title}</h2>
          {post.content && <p>{post.content}</p>}
        </li>
      ))}
    </ul>
  </body>
</html>
```jsx
It is best practice to handle queries in an API route. For more information on how to use Prisma ORM in your Astro project, see the [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro).

## Direct TCP connection

[Section titled “Direct TCP connection”](#direct-tcp-connection)

To connect to Prisma Postgres via direct TCP, you can create a direct connection string in your Prisma Console. This allows you to connect any other ORM, database library, or tool of your choice.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

* A [Prisma Postgres](https://pris.ly/ppg) database with a TCP enabled connection string

### Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

This example will make a direct TCP connection using [`pg`, a PostgreSQL client for Node.js](https://github.com/brianc/node-postgres).

Run the following command to install the `pg` package:

```bash
npm install pg
```jsx
### Query your database client

[Section titled “Query your database client”](#query-your-database-client)

Provide your connection string to the `pg` client to communicate with your SQL server and fetch data from your database.

The following example of creating a table and inserting data can be used to validate your query URL and TCP connection:

src/pages/index.astro

```astro
---
import { Client } from 'pg';
const client = new Client({
  connectionString: import.meta.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});
await client.connect();


await client.query(`
  CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT UNIQUE,
    content TEXT
  );


  INSERT INTO posts (title, content)
  VALUES ('Hello', 'World')
  ON CONFLICT (title) DO NOTHING;
`);


const { rows } = await client.query('SELECT * FROM posts');
await client.end();
---


<h1>Posts</h1>
<p>{rows[0].title}: {rows[0].content}</p>
```jsx
## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro + Prisma ORM Guide](https://www.prisma.io/docs/guides/astro)

---

[← Previous](24-neon-postgres-astro.md) | [Index](index.md) | [Next →](index.md)
