---
title: "This will be available everywhere!"
section: 118
---

# This will be available everywhere!
PUBLIC_POKEAPI="https://pokeapi.co/api/v2"
```jsx
You can also add `.production`, `.development` or a custom mode name to the filename itself (e.g `.env.testing`, `.env.staging`). This allows you to use different sets of environment variables at different times.

The `astro dev` and `astro build` commands default to `"development"` and `"production"` modes, respectively. You can run these commands with the [`--mode` flag](/en/reference/cli-reference/#--mode-string) to pass a different value for `mode` and load the matching `.env` file.

This allows you to run the dev server or build your site connecting to different APIs:

* npm

  ```shell
  # Run the dev server connected to a "staging" API
  npm run astro dev -- --mode staging


  # Build a site that connects to a "production" API with additional debug information
  npm run astro build -- --devOutput


  # Build a site that connects to a "testing" API
  npm run astro build -- --mode testing
  ```jsx
* pnpm

  ```shell
  # Run the dev server connected to a "staging" API
  pnpm astro dev --mode staging


  # Build a site that connects to a "production" API with additional debug information
  pnpm astro build --devOutput


  # Build a site that connects to a "testing" API
  pnpm astro build --mode testing
  ```jsx
* Yarn

  ```shell
  # Run the dev server connected to a "staging" API
  yarn astro dev --mode staging


  # Build a site that connects to a "production" API with additional debug information
  yarn astro build --devOutput


  # Build a site that connects to a "testing" API
  yarn astro build --mode testing
  ```jsx
For more on `.env` files, [see the Vite documentation](https://vite.dev/guide/env-and-mode.html#env-files).

### In the Astro config file

[Section titled “In the Astro config file”](#in-the-astro-config-file)

Astro evaluates configuration files before it loads your other files. This means that you cannot use `import.meta.env` in `astro.config.mjs` to access environment variables that were set in `.env` files.

You can use `process.env` in a configuration file to access other environment variables, like those [set by the CLI](#using-the-cli).

You can also use [Vite’s `loadEnv` helper](https://main.vite.dev/config/#using-environment-variables-in-config) to manually load `.env` files.

astro.config.mjs

```js
import { loadEnv } from "vite";


const { SECRET_PASSWORD } = loadEnv(process.env.NODE_ENV, process.cwd(), "");
```jsx
Note

`pnpm` does not allow you to import modules that are not directly installed in your project. If you are using `pnpm`, you will need to install `vite` to use the `loadEnv` helper.

```sh
pnpm add -D vite
```jsx
### Using the CLI

[Section titled “Using the CLI”](#using-the-cli)

You can also add environment variables as you run your project:

* npm

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 npm run dev
  ```jsx
* pnpm

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 pnpm run dev
  ```jsx
* Yarn

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 yarn run dev
  ```jsx
## Getting environment variables

[Section titled “Getting environment variables”](#getting-environment-variables)

Environment variables in Astro are accessed with `import.meta.env`, using the [`import.meta` feature added in ES2020](https://tc39.es/ecma262/2020/#prod-ImportMeta), instead of `process.env`.

For example, use `import.meta.env.PUBLIC_POKEAPI` to get the `PUBLIC_POKEAPI` environment variable.

```js
// When import.meta.env.SSR === true
const data = await db(import.meta.env.DB_PASSWORD);


// When import.meta.env.SSR === false
const data = fetch(`${import.meta.env.PUBLIC_POKEAPI}/pokemon/squirtle`);
```jsx
When using SSR, environment variables can be accessed at runtime based on the SSR adapter being used. With most adapters you can access environment variables with `process.env`, but some adapters work differently. For the Deno adapter, you will use `Deno.env.get()`. See how to [access the Cloudflare runtime](/en/guides/integrations-guide/cloudflare/#cloudflare-runtime) to handle environment variables when using the Cloudflare adapter. Astro will first check the server environment for variables, and if they don’t exist, Astro will look for them in `.env` files.

## Type safe environment variables

[Section titled “Type safe environment variables”](#type-safe-environment-variables)

The `astro:env` API lets you configure a type-safe schema for [environment variables you have set](#setting-environment-variables). This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties.

Developing an adapter? See how to [make an adapter compatible with `astro:env`](/en/reference/adapter-reference/#envgetsecret).

### Basic Usage

[Section titled “Basic Usage”](#basic-usage)

#### Define your schema

[Section titled “Define your schema”](#define-your-schema)

To configure a schema, add the `env.schema` option to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
+  env: {
+    schema: {
      +// ...
+    }
+  }
})
```jsx
You can then [register variables as a string, number, enum, or boolean](#data-types) using the `envField` helper. Define the [kind of environment variable](#variable-types) by providing a `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) for each variable, and pass any additional properties such as `optional` or `default` in an object:

astro.config.mjs

```js
import { defineConfig, envField } from "astro/config";


export default defineConfig({
  env: {
    schema: {
      API_URL: envField.string({ context: "client", access: "public", optional: true }),
      PORT: envField.number({ context: "server", access: "public", default: 4321 }),
      API_SECRET: envField.string({ context: "server", access: "secret" }),
    }
  }
})
```jsx
Types will be generated for you when running `astro dev` or `astro build`, but you can run `astro sync` to generate types only.

#### Use variables from your schema

[Section titled “Use variables from your schema”](#use-variables-from-your-schema)

Import and use your defined variables from the appropriate `/client` or `/server` module:

```astro
---
import { API_URL } from "astro:env/client";
import { API_SECRET_TOKEN } from "astro:env/server";


const data = await fetch(`${API_URL}/users`, {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${API_SECRET_TOKEN}`
  },
})
---


<script>
  import { API_URL } from "astro:env/client";


  fetch(`${API_URL}/ping`)
</script>
```jsx
### Variable types

[Section titled “Variable types”](#variable-types)

There are three kinds of environment variables, determined by the combination of `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) settings defined in your schema:

* **Public client variables**: These variables end up in both your final client and server bundles, and can be accessed from both client and server through the `astro:env/client` module:

  ```js
  import { API_URL } from "astro:env/client";
  ```jsx
* **Public server variables**: These variables end up in your final server bundle and can be accessed on the server through the `astro:env/server` module:

  ```js
  import { PORT } from "astro:env/server";
  ```jsx
* **Secret server variables**: These variables are not part of your final bundle and can be accessed on the server through the `astro:env/server` module:

  ```js
  import { API_SECRET } from "astro:env/server";
  ```jsx
  By default, secrets are only validated at runtime. You can enable validating private variables on start by [configuring `validateSecrets: true`](/en/reference/configuration-reference/#envvalidatesecrets).

Note

**Secret client variables** are not supported because there is no safe way to send this data to the client. Therefore, it is not possible to configure both `context: "client"` and `access: "secret"` in your schema.

### Data types

[Section titled “Data types”](#data-types)

There are currently four data types supported: strings, numbers, enums, and booleans:

```js
import { envField } from "astro/config";


envField.string({
   // context & access
   optional: true,
   default: "foo",
})


envField.number({
   // context & access
   optional: true,
   default: 15,
})


envField.boolean({
   // context & access
   optional: true,
   default: true,
})


envField.enum({
   // context & access
   values: ["foo", "bar", "baz"],
   optional: true,
   default: "baz",
})
```jsx
For a complete list of validation fields, see the [`envField` API reference](/en/reference/configuration-reference/#envschema).

### Retrieving secrets dynamically

[Section titled “Retrieving secrets dynamically”](#retrieving-secrets-dynamically)

Despite defining your schema, you may want to retrieve the raw value of a given secret or to retrieve secrets not defined in your schema. In this case, you can use `getSecret()` exported from `astro:env/server`:

```js
import {
   FOO, // boolean
   getSecret
} from "astro:env/server";


getSecret("FOO"); // string | undefined
```jsx
Learn more in [the API reference](/en/reference/modules/astro-env/#getsecret).

### Limitations

[Section titled “Limitations”](#limitations)

`astro:env` is a virtual module which means it can only be used inside the Astro context. For example, you can use it in:

* Middlewares
* Astro routes and endpoints
* Astro components
* Framework components
* Modules

You cannot use it in the following and will have to resort to `process.env`:

* `astro.config.mjs`
* Scripts

---

[← Previous](117-this-will-only-be-available-when-run-on-the-server.md) | [Index](index.md) | [Next →](index.md)
