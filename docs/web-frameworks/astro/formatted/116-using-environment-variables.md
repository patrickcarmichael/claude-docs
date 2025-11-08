---
title: "Using environment variables"
section: 116
---

# Using environment variables

> Learn how to use environment variables in an Astro project.

Astro gives you access to [Vite’s built-in environment variables support](#vites-built-in-support) and includes some [default environment variables for your project](#default-environment-variables) that allow you to access configuration values for your current project (e.g. `site`, `base`), whether your project is running in development or production, and more.

Astro also provides a way to [use and organize your environment variables with type safety](#type-safe-environment-variables). It is available for use inside the Astro context (e.g. Astro components, routes and endpoints, UI framework components, middleware), and managed with [a schema in your Astro configuration](/en/reference/configuration-reference/#env).

## Vite’s built-in support

[Section titled “Vite’s built-in support”](#vites-built-in-support)

Astro uses Vite’s built-in support for environment variables, which are statically replaced at build time, and lets you [use any of its methods](https://vite.dev/guide/env-and-mode.html) to work with them.

Note that while *all* environment variables are available in server-side code, only environment variables prefixed with `PUBLIC_` are available in client-side code for security purposes.

.env

```ini
SECRET_PASSWORD=password123
PUBLIC_ANYBODY=there
```jsx
In this example, `PUBLIC_ANYBODY` (accessible via `import.meta.env.PUBLIC_ANYBODY`) will be available in server or client code, while `SECRET_PASSWORD` (accessible via `import.meta.env.SECRET_PASSWORD`) will be server-side only.

Caution

`.env` files are not loaded inside [configuration files](#in-the-astro-config-file).

### IntelliSense for TypeScript

[Section titled “IntelliSense for TypeScript”](#intellisense-for-typescript)

By default, Astro provides a type definition for `import.meta.env` in `astro/client.d.ts`.

While you can define more custom env variables in `.env.[mode]` files, you may want to get TypeScript IntelliSense for user-defined env variables which are prefixed with `PUBLIC_`.

To achieve this, you can create an `env.d.ts` in `src/` to [extend the global types](/en/guides/typescript/#extending-global-types) and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly DB_PASSWORD: string;
  readonly PUBLIC_POKEAPI: string;
  // more env variables...
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```jsx
## Default environment variables

[Section titled “Default environment variables”](#default-environment-variables)

Astro includes a few environment variables out of the box:

* `import.meta.env.MODE`: The mode your site is running in. This is `development` when running `astro dev` and `production` when running `astro build`.
* `import.meta.env.PROD`: `true` if your site is running in production; `false` otherwise.
* `import.meta.env.DEV`: `true` if your site is running in development; `false` otherwise. Always the opposite of `import.meta.env.PROD`.
* `import.meta.env.BASE_URL`: The base URL your site is being served from. This is determined by the [`base` config option](/en/reference/configuration-reference/#base).
* `import.meta.env.SITE`: This is set to [the `site` option](/en/reference/configuration-reference/#site) specified in your project’s `astro.config`.
* `import.meta.env.ASSETS_PREFIX`: The prefix for Astro-generated asset links if the [`build.assetsPrefix` config option](/en/reference/configuration-reference/#buildassetsprefix) is set. This can be used to create asset links not handled by Astro.

Use them like any other environment variable.

```ts
const isProd = import.meta.env.PROD;
const isDev = import.meta.env.DEV;
```jsx
## Setting environment variables

[Section titled “Setting environment variables”](#setting-environment-variables)

### `.env` files

[Section titled “.env files”](#env-files)

Environment variables can be loaded from `.env` files in your project directory.

Just create a `.env` file in the project directory and add some variables to it.

.env

```ini

---

[← Previous](115-endpoints.md) | [Index](index.md) | [Next →](index.md)
