**Navigation:** [← Previous](./10-usesearchparams.md) | [Index](./index.md) | [Next →](./12-fonts.md)

---

# staticGeneration*

> This feature is currently experimental and subject to change, it is not recommended for production.

The `staticGeneration*` options allow you to configure the Static Generation process for advanced use cases.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  experimental: {
    staticGenerationRetryCount: 1,
    staticGenerationMaxConcurrency: 8,
    staticGenerationMinPagesPerWorker: 25,
  },
}

export default nextConfig
```

## Config Options

The following options are available:

* `staticGenerationRetryCount`: The number of times to retry a failed page generation before failing the build.
* `staticGenerationMaxConcurrency`: The maximum number of pages to be processed per worker.
* `staticGenerationMinPagesPerWorker`: The minimum number of pages to be processed before starting a new worker.


--------------------------------------------------------------------------------
title: "taint"
description: "Enable tainting Objects and Values."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/taint"
--------------------------------------------------------------------------------

# taint

> This feature is currently experimental and subject to change, it is not recommended for production.

## Usage

The `taint` option enables support for experimental React APIs for tainting objects and values. This feature helps prevent sensitive data from being accidentally passed to the client. When enabled, you can use:

* [`experimental_taintObjectReference`](https://react.dev/reference/react/experimental_taintObjectReference) taint objects references.
* [`experimental_taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue) to taint unique values.

> **Good to know**: Activating this flag also enables the React `experimental` channel for `app` directory.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    taint: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    taint: true,
  },
}

module.exports = nextConfig
```

> **Warning:** Do not rely on the taint API as your only mechanism to prevent exposing sensitive data to the client. See our [security recommendations](/blog/security-nextjs-server-components-actions).

The taint APIs allows you to be defensive, by declaratively and explicitly marking data that is not allowed to pass through the Server-Client boundary. When an object or value, is passed through the Server-Client boundary, React throws an error.

This is helpful for cases where:

* The methods to read data are out of your control
* You have to work with sensitive data shapes not defined by you
* Sensitive data is accessed during Server Component rendering

It is recommended to model your data and APIs so that sensitive data is not returned to contexts where it is not needed.

## Caveats

* Tainting can only keep track of objects by reference. Copying an object creates an untainted version, which loses all guarantees given by the API. You'll need to taint the copy.
* Tainting cannot keep track of data derived from a tainted value. You also need to taint the derived value.
* Values are tainted for as long as their lifetime reference is within scope. See the [`experimental_taintUniqueValue` parameters reference](https://react.dev/reference/react/experimental_taintUniqueValue#parameters), for more information.

## Examples

### Tainting an object reference

In this case, the `getUserDetails` function returns data about a given user. We taint the user object reference, so that it cannot cross a Server-Client boundary. For example, assuming `UserCard` is a Client Component.

```ts switcher
import { experimental_taintObjectReference } from 'react'

function getUserDetails(id: string): UserDetails {
  const user = await db.queryUserById(id)

  experimental_taintObjectReference(
    'Do not use the entire user info object. Instead, select only the fields you need.',
    user
  )

  return user
}
```

```js switcher
import { experimental_taintObjectReference } from 'react'

function getUserDetails(id) {
  const user = await db.queryUserById(id)

  experimental_taintObjectReference(
    'Do not use the entire user info object. Instead, select only the fields you need.',
    user
  )

  return user
}
```

We can still access individual fields from the tainted `userDetails` object.

```tsx filename="app/contact/page.tsx switcher
export async function ContactPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const userDetails = await getUserDetails(id)

  return (
    <UserCard
      firstName={userDetails.firstName}
      lastName={userDetails.lastName}
    />
  )
}
```

```jsx filename="app/contact/page.js switcher
export async function ContactPage({ params }) {
  const { id } = await params
  const userDetails = await getUserDetails(id)

  return (
    <UserCard
      firstName={userDetails.firstName}
      lastName={userDetails.lastName}
    />
  )
}
```

Now, passing the entire object to the Client Component will throw an error.

```tsx switcher
export async function ContactPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const userDetails = await getUserDetails(id)

  // Throws an error
  return <UserCard user={userDetails} />
}
```

```jsx switcher
export async function ContactPage({ params }) {
  const { id } = await params
  const userDetails = await getUserDetails(id)

  // Throws an error
  return <UserCard user={userDetails} />
}
```

### Tainting a unique value

In this case, we can access the server configuration by awaiting calls to `config.getConfigDetails`. However, the system configuration contains the `SERVICE_API_KEY` that we don't want to expose to clients.

We can taint the `config.SERVICE_API_KEY` value.

```ts switcher
import { experimental_taintUniqueValue } from 'react'

function getSystemConfig(): SystemConfig {
  const config = await config.getConfigDetails()

  experimental_taintUniqueValue(
    'Do not pass configuration tokens to the client',
    config,
    config.SERVICE_API_KEY
  )

  return config
}
```

```js switcher
import { experimental_taintUniqueValue } from 'react'

function getSystemConfig() {
  const config = await config.getConfigDetails()

  experimental_taintUniqueValue(
    'Do not pass configuration tokens to the client',
    config,
    config.SERVICE_API_KEY
  )

  return config
}
```

We can still access other properties of the `systemConfig` object.

```tsx
export async function Dashboard() {
  const systemConfig = await getSystemConfig()

  return <ClientDashboard version={systemConfig.SERVICE_API_VERSION} />
}
```

However, passing `SERVICE_API_KEY` to `ClientDashboard` throws an error.

```tsx
export async function Dashboard() {
  const systemConfig = await getSystemConfig()
  // Someone makes a mistake in a PR
  const version = systemConfig.SERVICE_API_KEY

  return <ClientDashboard version={version} />
}
```

Note that, even though, `systemConfig.SERVICE_API_KEY` is reassigned to a new variable. Passing it to a Client Component still throws an error.

Whereas, a value derived from a tainted unique value, will be exposed to the client.

```tsx
export async function Dashboard() {
  const systemConfig = await getSystemConfig()
  // Someone makes a mistake in a PR
  const version = `version::${systemConfig.SERVICE_API_KEY}`

  return <ClientDashboard version={version} />
}
```

A better approach is to remove `SERVICE_API_KEY` from the data returned by `getSystemConfig`.


--------------------------------------------------------------------------------
title: "trailingSlash"
description: "Configure Next.js pages to resolve with or without a trailing slash."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash"
--------------------------------------------------------------------------------

# trailingSlash

By default Next.js will redirect URLs with trailing slashes to their counterpart without a trailing slash. For example `/about/` will redirect to `/about`. You can configure this behavior to act the opposite way, where URLs without trailing slashes are redirected to their counterparts with trailing slashes.

Open `next.config.js` and add the `trailingSlash` config:

```js filename="next.config.js"
module.exports = {
  trailingSlash: true,
}
```

With this option set, URLs like `/about` will redirect to `/about/`.

When using `trailingSlash: true`, certain URLs are exceptions and will not have a trailing slash appended:

* Static file URLs, such as files with extensions.
* Any paths under `.well-known/`.

For example, the following URLs will remain unchanged: `/file.txt`, `images/photos/picture.png`, and `.well-known/subfolder/config.json`.

When used with [`output: "export"`](/docs/app/guides/static-exports.md) configuration, the `/about` page will output `/about/index.html` (instead of the default `/about.html`).

## Version History

| Version  | Changes                |
| -------- | ---------------------- |
| `v9.5.0` | `trailingSlash` added. |


--------------------------------------------------------------------------------
title: "transpilePackages"
description: "Automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`)."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages"
--------------------------------------------------------------------------------

# transpilePackages

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ['package-name'],
}

module.exports = nextConfig
```

## Version History

| Version   | Changes                    |
| --------- | -------------------------- |
| `v13.0.0` | `transpilePackages` added. |


--------------------------------------------------------------------------------
title: "turbopack"
description: "Configure Next.js with Turbopack-specific options"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack"
--------------------------------------------------------------------------------

# turbopack

The `turbopack` option lets you customize [Turbopack](/docs/app/api-reference/turbopack.md) to transform different files and change how modules are resolved.

> **Good to know**: The `turbopack` option was previously named `experimental.turbo` in Next.js versions 13.0.0 to 15.2.x. The `experimental.turbo` option will be removed in Next.js 16.
>
> If you are using an older version of Next.js, run `npx @next/codemod@latest next-experimental-turbo-to-turbopack .` to automatically migrate your configuration.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  turbopack: {
    // ...
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  turbopack: {
    // ...
  },
}

module.exports = nextConfig
```

> **Good to know**:
>
> * Turbopack for Next.js does not require loaders or loader configuration for built-in functionality. Turbopack has built-in support for CSS and compiling modern JavaScript, so there's no need for `css-loader`, `postcss-loader`, or `babel-loader` if you're using `@babel/preset-env`.

## Reference

### Options

The following options are available for the `turbopack` configuration:

| Option              | Description                                                                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `root`              | Sets the application root directory. Should be an absolute path.                                                                         |
| `rules`             | List of supported webpack loaders to apply when running with Turbopack.                                                                  |
| `resolveAlias`      | Map aliased imports to modules to load in their place.                                                                                   |
| `resolveExtensions` | List of extensions to resolve when importing files.                                                                                      |
| `debugIds`          | Enable generation of [debug IDs](https://github.com/tc39/ecma426/blob/main/proposals/debug-id.md) in JavaScript bundles and source maps. |

### Supported loaders

The following loaders have been tested to work with Turbopack's webpack loader implementation, but many other webpack loaders should work as well even if not listed here:

* [`babel-loader`](https://www.npmjs.com/package/babel-loader) [*(Configured automatically if a Babel configuration file is found)*](/docs/app/api-reference/turbopack.md#language-features)
* [`@svgr/webpack`](https://www.npmjs.com/package/@svgr/webpack)
* [`svg-inline-loader`](https://www.npmjs.com/package/svg-inline-loader)
* [`yaml-loader`](https://www.npmjs.com/package/yaml-loader)
* [`string-replace-loader`](https://www.npmjs.com/package/string-replace-loader)
* [`raw-loader`](https://www.npmjs.com/package/raw-loader)
* [`sass-loader`](https://www.npmjs.com/package/sass-loader) [*(Configured automatically)*](/docs/app/api-reference/turbopack.md#css-and-styling)
* [`graphql-tag/loader`](https://www.npmjs.com/package/graphql-tag)

#### Missing Webpack loader features

Turbopack uses the [`loader-runner`](https://github.com/webpack/loader-runner) library to execute webpack loaders, which provides most of the standard loader API. However, some features are not supported:

**Module loading:**

* [`importModule`](https://webpack.js.org/api/loaders/#thisimportmodule) - No support
* [`loadModule`](https://webpack.js.org/api/loaders/#thisloadmodule) - No support

**File system and output:**

* [`fs`](https://webpack.js.org/api/loaders/#thisfs) - Partial support: only `fs.readFile` is currently implemented.
* [`emitFile`](https://webpack.js.org/api/loaders/#thisemitfile) - No support

**Context properties:**

* [`version`](https://webpack.js.org/api/loaders/#thisversion) - No support
* [`mode`](https://webpack.js.org/api/loaders/#thismode) - No support
* [`target`](https://webpack.js.org/api/loaders/#thistarget) - No support

**Utilities:**

* [`utils`](https://webpack.js.org/api/loaders/#thisutils) - No support
* [`resolve`](https://webpack.js.org/api/loaders/#thisresolve) - No support (use [`getResolve`](https://webpack.js.org/api/loaders/#thisgetresolve) instead)

If you have a loader that is critically dependent upon one of these features please file an issue.

## Examples

### Root directory

Turbopack uses the root directory to resolve modules. Files outside of the project root are not resolved.

Next.js automatically detects the root directory of your project. It does so by looking for one of these files:

* `pnpm-lock.yaml`
* `package-lock.json`
* `yarn.lock`
* `bun.lock`
* `bun.lockb`

If you have a different project structure, for example if you don't use workspaces, you can manually set the `root` option:

```js filename="next.config.js"
const path = require('path')
module.exports = {
  turbopack: {
    root: path.join(__dirname, '..'),
  },
}
```

### Configuring webpack loaders

If you need loader support beyond what's built in, many webpack loaders already work with Turbopack. There are currently some limitations:

* Only a core subset of the webpack loader API is implemented. Currently, there is enough coverage for some popular loaders, and we'll expand our API support in the future.
* Only loaders that return JavaScript code are supported. Loaders that transform files like stylesheets or images are not currently supported.
* Options passed to webpack loaders must be plain JavaScript primitives, objects, and arrays. For example, it's not possible to pass `require()` plugin modules as option values.

To configure loaders, add the names of the loaders you've installed and any options in `next.config.js`, mapping file extensions to a list of loaders. Rules are evaluated in order.

Here is an example below using the [`@svgr/webpack`](https://www.npmjs.com/package/@svgr/webpack) loader, which enables importing `.svg` files and rendering them as React components.

```js filename="next.config.js"
module.exports = {
  turbopack: {
    rules: {
      '*.svg': {
        loaders: ['@svgr/webpack'],
        as: '*.js',
      },
    },
  },
}
```

> **Good to know**: Globs used in the `rules` object match based on file name, unless the glob contains a `/` character, which will cause it to match based on the full project-relative file path. Windows file paths are normalized to use unix-style `/` path separators.
>
> Turbopack uses a modified version of the [Rust `globset` library](https://docs.rs/globset/latest/globset/).

For loaders that require configuration options, you can use an object format instead of a string:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    rules: {
      '*.svg': {
        loaders: [
          {
            loader: '@svgr/webpack',
            options: {
              icon: true,
            },
          },
        ],
        as: '*.js',
      },
    },
  },
}
```

> **Good to know**: Prior to Next.js version 13.4.4, `turbopack.rules` was named `turbo.loaders` and only accepted file extensions like `.mdx` instead of `*.mdx`.

### Advanced webpack loader conditions

You can further restrict where a loader runs using the advanced `condition` syntax:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    rules: {
      // '*' will match all file paths, but we restrict where our
      // rule runs with a condition.
      '*': {
        condition: {
          all: [
            // 'foreign' is a built-in condition.
            { not: 'foreign' },
            // 'path' can be a RegExp or a glob string. A RegExp matches
            // anywhere in the full project-relative file path.
            { path: /^img\/[0-9]{3}\// },
            {
              any: [
                { path: '*.svg' },
                // 'content' is always a RegExp, and can match
                // anywhere in the file.
                { content: /\<svg\W/ },
              ],
            },
          ],
        },
        loaders: ['@svgr/webpack'],
        as: '*.js',
      },
    },
  },
}
```

* Supported boolean operators are `{all: [...]}`, `{any: [...]}` and `{not: ...}`.
* Supported customizable operators are `{path: string | RegExp}` and `{content: RegExp}`. If `path` and `content` are specified in the same object, it acts as an implicit `and`.

In addition, a number of built-in conditions are supported:

* `browser`: Matches code that will execute on the client. Server code can be matched using `{not: 'browser'}`.
* `foreign`: Matches code in `node_modules`, as well as some Next.js internals. Usually you'll want to restrict loaders to `{not: 'foreign'}`. This can improve performance by reducing the number of files the loader is invoked on.
* `development`: Matches when using `next dev`.
* `production`: Matches when using `next build`.
* `node`: Matches code that will run on the default Node.js runtime.
* `edge-light`: Matches code that will run on the [Edge runtime](/docs/app/api-reference/edge.md).

Rules can be an object or an array of objects. An array is often useful for modeling disjoint conditions:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    rules: {
      '*.svg': [
        {
          condition: 'browser',
          loaders: ['@svgr/webpack'],
          as: '*.js',
        },
        {
          condition: { not: 'browser' },
          loaders: [require.resolve('./custom-svg-loader.js')],
          as: '*.js',
        },
      ],
    },
  },
}
```

> **Good to know**: All matching rules are executed in order.

### Resolving aliases

Turbopack can be configured to modify module resolution through aliases, similar to webpack's [`resolve.alias`](https://webpack.js.org/configuration/resolve/#resolvealias) configuration.

To configure resolve aliases, map imported patterns to their new destination in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    resolveAlias: {
      underscore: 'lodash',
      mocha: { browser: 'mocha/browser-entry.js' },
    },
  },
}
```

This aliases imports of the `underscore` package to the `lodash` package. In other words, `import underscore from 'underscore'` will load the `lodash` module instead of `underscore`.

Turbopack also supports conditional aliasing through this field, similar to Node.js' [conditional exports](https://nodejs.org/docs/latest-v18.x/api/packages.html#conditional-exports). At the moment only the `browser` condition is supported. In the case above, imports of the `mocha` module will be aliased to `mocha/browser-entry.js` when Turbopack targets browser environments.

### Resolving custom extensions

Turbopack can be configured to resolve modules with custom extensions, similar to webpack's [`resolve.extensions`](https://webpack.js.org/configuration/resolve/#resolveextensions) configuration.

To configure resolve extensions, use the `resolveExtensions` field in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.mjs', '.json'],
  },
}
```

This overwrites the original resolve extensions with the provided list. Make sure to include the default extensions.

For more information and guidance for how to migrate your app to Turbopack from webpack, see [Turbopack's documentation on webpack compatibility](https://turbo.build/pack/docs/migrating-from-webpack).

### Debug IDs

Turbopack can be configured to generate [debug IDs](https://github.com/tc39/ecma426/blob/main/proposals/debug-id.md) in JavaScript bundles and source maps.

To configure debug IDs, use the `debugIds` field in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    debugIds: true,
  },
}
```

The option automatically adds a polyfill for debug IDs to the JavaScript bundle to ensure compatibility. The debug IDs are available in the `globalThis._debugIds` global variable.

## Version History

| Version  | Changes                                         |
| -------- | ----------------------------------------------- |
| `16.0.0` | `turbopack.debugIds` was added.                 |
| `16.0.0` | `turbopack.rules.*.condition` was added.        |
| `15.3.0` | `experimental.turbo` is changed to `turbopack`. |
| `13.0.0` | `experimental.turbo` introduced.                |


--------------------------------------------------------------------------------
title: "Turbopack FileSystem Caching"
description: "Learn how to enable FileSystem Caching for Turbopack builds"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache"
--------------------------------------------------------------------------------

# turbopackFileSystemCache

## Usage

Turbopack FileSystem Cache enables Turbopack to reduce work across `next dev` or `next build` commands. When enabled, Turbopack will save and restore data to the `.next` folder between builds, which can greatly speed up subsequent builds and dev sessions.

> **Good to know:** The FileSystem Cache feature is Beta and is still under development. Users adopting should expect some stability issues. We recommend first adopting it for development.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    // Enable filesystem caching for `next dev`
    turbopackFileSystemCacheForDev: true,
    // Enable filesystem caching for `next build`
    turbopackFileSystemCacheForBuild: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    // Enable filesystem caching for `next dev`
    turbopackFileSystemCacheForDev: true,
    // Enable filesystem caching for `next build`
    turbopackFileSystemCacheForBuild: true,
  },
}

module.exports = nextConfig
```

## Version Changes

| Version   | Changes                                                        |
| --------- | -------------------------------------------------------------- |
| `v16.0.0` | Beta release with separate flags for build and dev             |
| `v15.5.0` | Persistent caching released as experimental on canary releases |


--------------------------------------------------------------------------------
title: "typedRoutes"
description: "Enable support for statically typed links."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes"
--------------------------------------------------------------------------------

# typedRoutes

> **Note**: This option has been marked as stable, so you should use `typedRoutes` instead of `experimental.typedRoutes`.

Support for [statically typed links](/docs/app/api-reference/config/typescript.md#statically-typed-links). This feature requires using TypeScript in your project.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  typedRoutes: true,
}

module.exports = nextConfig
```


--------------------------------------------------------------------------------
title: "typescript"
description: "Next.js reports TypeScript errors by default. Learn to opt-out of this behavior here."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript"
--------------------------------------------------------------------------------

# typescript

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

Open `next.config.js` and enable the `ignoreBuildErrors` option in the `typescript` config:

```js filename="next.config.js"
module.exports = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}
```


--------------------------------------------------------------------------------
title: "urlImports"
description: "Configure Next.js to allow importing modules from external URLs."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports"
--------------------------------------------------------------------------------

# urlImports

> This feature is currently experimental and subject to change, it is not recommended for production.

URL imports are an experimental feature that allows you to import modules directly from external servers (instead of from the local disk).

> **Warning**: Only use domains that you trust to download and execute on your machine. Please exercise discretion, and caution until the feature is flagged as stable.

To opt-in, add the allowed URL prefixes inside `next.config.js`:

```js filename="next.config.js"
module.exports = {
  experimental: {
    urlImports: ['https://example.com/assets/', 'https://cdn.skypack.dev'],
  },
}
```

Then, you can import modules directly from URLs:

```js
import { a, b, c } from 'https://example.com/assets/some/module.js'
```

URL Imports can be used everywhere normal package imports can be used.

## Security Model

This feature is being designed with **security as the top priority**. To start, we added an experimental flag forcing you to explicitly allow the domains you accept URL imports from. We're working to take this further by limiting URL imports to execute in the browser sandbox using the [Edge Runtime](/docs/app/api-reference/edge.md).

## Lockfile

When using URL imports, Next.js will create a `next.lock` directory containing a lockfile and fetched assets.
This directory **must be committed to Git**, not ignored by `.gitignore`.

* When running `next dev`, Next.js will download and add all newly discovered URL Imports to your lockfile.
* When running `next build`, Next.js will use only the lockfile to build the application for production.

Typically, no network requests are needed and any outdated lockfile will cause the build to fail.
One exception is resources that respond with `Cache-Control: no-cache`.
These resources will have a `no-cache` entry in the lockfile and will always be fetched from the network on each build.

## Examples

### Skypack

```js
import confetti from 'https://cdn.skypack.dev/canvas-confetti'
import { useEffect } from 'react'

export default () => {
  useEffect(() => {
    confetti()
  })
  return <p>Hello</p>
}
```

### Static Image Imports

```js
import Image from 'next/image'
import logo from 'https://example.com/assets/logo.png'

export default () => (
  <div>
    <Image src={logo} placeholder="blur" />
  </div>
)
```

### URLs in CSS

```css
.className {
  background: url('https://example.com/assets/hero.jpg');
}
```

### Asset Imports

```js
const logo = new URL('https://example.com/assets/file.txt', import.meta.url)

console.log(logo.pathname)

// prints "/_next/static/media/file.a9727b5d.txt"
```


--------------------------------------------------------------------------------
title: "useLightningcss"
description: "Enable experimental support for Lightning CSS."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss"
--------------------------------------------------------------------------------

# useLightningcss

> This feature is currently experimental and subject to change, it is not recommended for production.

Experimental support for using [Lightning CSS](https://lightningcss.dev) with webpack. Lightning CSS is a fast CSS transformer and minifier, written in Rust.

If this option is not set, Next.js on webpack uses [PostCSS](https://postcss.org/) with [`postcss-preset-env`](https://www.npmjs.com/package/postcss-preset-env) by default.

Turbopack uses Lightning CSS by default since Next 14.2. This configuration option has no effect on Turbopack. Turbopack always uses Lightning CSS.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    useLightningcss: false, // default, ignored on Turbopack
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    useLightningcss: true, // disables PostCSS on webpack
  },
}

module.exports = nextConfig
```

## Version History

| Version  | Changes                                                                                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `15.1.0` | Support for `useSwcCss` was removed from Turbopack.                                                                                                                                          |
| `14.2.0` | Turbopack's default CSS processor was changed from `@swc/css` to Lightning CSS. `useLightningcss` became ignored on Turbopack, and a legacy `experimental.turbo.useSwcCss` option was added. |


--------------------------------------------------------------------------------
title: "viewTransition"
description: "Enable ViewTransition API from React in App Router"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition"
--------------------------------------------------------------------------------

# viewTransition

> This feature is currently experimental and subject to change, it is not recommended for production.

`viewTransition` is an experimental flag that enables the new [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) in React. This API allows you to leverage the native View Transitions browser API to create seamless transitions between UI states.

To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
}

module.exports = nextConfig
```

> Important Notice: The `<ViewTransition>` Component is already available in React's Canary release channel.
> `experimental.viewTransition` is only required to enable deeper integration with Next.js features e.g. automatically
> [adding Transition types](https://react.dev/reference/react/addTransitionType) for navigations. Next.js specific transition types are not implemented yet.

## Usage

You can import the [`<ViewTransition>` Component](https://react.dev/reference/react/ViewTransition) from React in your application:

```jsx
import { ViewTransition } from 'react'
```

### Live Demo

Check out our [Next.js View Transition Demo](https://view-transition-example.vercel.app) to see this feature in action.

As this API evolves, we will update our documentation and share more examples. However, for now, we strongly advise against using this feature in production.


--------------------------------------------------------------------------------
title: "Custom Webpack Config"
description: "Learn how to customize the webpack config used by Next.js"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack"
--------------------------------------------------------------------------------

# webpack

> **Good to know**: changes to webpack config are not covered by semver so proceed at your own risk

Before continuing to add custom webpack configuration to your application make sure Next.js doesn't already support your use-case:

* [CSS imports](/docs/app/getting-started/css.md)
* [CSS modules](/docs/app/getting-started/css.md#css-modules)
* [Sass/SCSS imports](/docs/app/guides/sass.md)
* [Sass/SCSS modules](/docs/app/guides/sass.md)

Some commonly asked for features are available as plugins:

* [@next/mdx](https://github.com/vercel/next.js/tree/canary/packages/next-mdx)
* [@next/bundle-analyzer](https://github.com/vercel/next.js/tree/canary/packages/next-bundle-analyzer)

In order to extend our usage of `webpack`, you can define a function that extends its config inside `next.config.js`, like so:

```js filename="next.config.js"
module.exports = {
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    // Important: return the modified config
    return config
  },
}
```

> The `webpack` function is executed three times, twice for the server (nodejs / edge runtime) and once for the client. This allows you to distinguish between client and server configuration using the `isServer` property.

The second argument to the `webpack` function is an object with the following properties:

* `buildId`: `String` - The build id, used as a unique identifier between builds.
* `dev`: `Boolean` - Indicates if the compilation will be done in development.
* `isServer`: `Boolean` - It's `true` for server-side compilation, and `false` for client-side compilation.
* `nextRuntime`: `String | undefined` - The target runtime for server-side compilation; either `"edge"` or `"nodejs"`, it's `undefined` for client-side compilation.
* `defaultLoaders`: `Object` - Default loaders used internally by Next.js:
  * `babel`: `Object` - Default `babel-loader` configuration.

Example usage of `defaultLoaders.babel`:

```js
// Example config for adding a loader that depends on babel-loader
// This source was taken from the @next/mdx plugin source:
// https://github.com/vercel/next.js/tree/canary/packages/next-mdx
module.exports = {
  webpack: (config, options) => {
    config.module.rules.push({
      test: /\.mdx/,
      use: [
        options.defaultLoaders.babel,
        {
          loader: '@mdx-js/loader',
          options: pluginOptions.options,
        },
      ],
    })

    return config
  },
}
```

#### `nextRuntime`

Notice that `isServer` is `true` when `nextRuntime` is `"edge"` or `"nodejs"`, `nextRuntime` `"edge"` is currently for proxy and Server Components in edge runtime only.


--------------------------------------------------------------------------------
title: "webVitalsAttribution"
description: "Learn how to use the webVitalsAttribution option to pinpoint the source of Web Vitals issues."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution"
--------------------------------------------------------------------------------

# webVitalsAttribution

> This feature is currently experimental and subject to change, it is not recommended for production.

When debugging issues related to Web Vitals, it is often helpful if we can pinpoint the source of the problem.
For example, in the case of Cumulative Layout Shift (CLS), we might want to know the first element that shifted when the single largest layout shift occurred.
Or, in the case of Largest Contentful Paint (LCP), we might want to identify the element corresponding to the LCP for the page.
If the LCP element is an image, knowing the URL of the image resource can help us locate the asset we need to optimize.

Pinpointing the biggest contributor to the Web Vitals score, aka [attribution](https://github.com/GoogleChrome/web-vitals/blob/4ca38ae64b8d1e899028c692f94d4c56acfc996c/README.md#attribution),
allows us to obtain more in-depth information like entries for [PerformanceEventTiming](https://developer.mozilla.org/docs/Web/API/PerformanceEventTiming), [PerformanceNavigationTiming](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming) and [PerformanceResourceTiming](https://developer.mozilla.org/docs/Web/API/PerformanceResourceTiming).

Attribution is disabled by default in Next.js but can be enabled **per metric** by specifying the following in `next.config.js`.

```js filename="next.config.js"
module.exports = {
  experimental: {
    webVitalsAttribution: ['CLS', 'LCP'],
  },
}
```

Valid attribution values are all `web-vitals` metrics specified in the [`NextWebVitalsMetric`](https://github.com/vercel/next.js/blob/442378d21dd56d6e769863eb8c2cb521a463a2e0/packages/next/shared/lib/utils.ts#L43) type.


--------------------------------------------------------------------------------
title: "TypeScript"
description: "Next.js provides a TypeScript-first development experience for building your React application."
source: "https://nextjs.org/docs/app/api-reference/config/typescript"
--------------------------------------------------------------------------------

# TypeScript

Next.js comes with built-in TypeScript, automatically installing the necessary packages and configuring the proper settings when you create a new project with `create-next-app`.

To add TypeScript to an existing project, rename a file to `.ts` / `.tsx`. Run `next dev` and `next build` to automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

> **Good to know**: If you already have a `jsconfig.json` file, copy the `paths` compiler option from the old `jsconfig.json` into the new `tsconfig.json` file, and delete the old `jsconfig.json` file.

## IDE Plugin

Next.js includes a custom TypeScript plugin and type checker, which VSCode and other code editors can use for advanced type-checking and auto-completion.

You can enable the plugin in VS Code by:

1. Opening the command palette (`Ctrl/⌘` + `Shift` + `P`)
2. Searching for "TypeScript: Select TypeScript Version"
3. Selecting "Use Workspace Version"

![TypeScript Command Palette](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/typescript-command-palette.png)

Now, when editing files, the custom plugin will be enabled. When running `next build`, the custom type checker will be used.

The TypeScript plugin can help with:

* Warning if the invalid values for [segment config options](/docs/app/api-reference/file-conventions/route-segment-config.md) are passed.
* Showing available options and in-context documentation.
* Ensuring the `'use client'` directive is used correctly.
* Ensuring client hooks (like `useState`) are only used in Client Components.

> **🎥 Watch:** Learn about the built-in TypeScript plugin → [YouTube (3 minutes)](https://www.youtube.com/watch?v=pqMqn9fKEf8)

## End-to-End Type Safety

The Next.js App Router has **enhanced type safety**. This includes:

1. **No serialization of data between fetching function and page**: You can `fetch` directly in components, layouts, and pages on the server. This data *does not* need to be serialized (converted to a string) to be passed to the client side for consumption in React. Instead, since `app` uses Server Components by default, we can use values like `Date`, `Map`, `Set`, and more without any extra steps. Previously, you needed to manually type the boundary between server and client with Next.js-specific types.
2. **Streamlined data flow between components**: With the removal of `_app` in favor of root layouts, it is now easier to visualize the data flow between components and pages. Previously, data flowing between individual `pages` and `_app` were difficult to type and could introduce confusing bugs. With [colocated data fetching](/docs/app/getting-started/fetching-data.md) in the App Router, this is no longer an issue.

[Data Fetching in Next.js](/docs/app/getting-started/fetching-data.md) now provides as close to end-to-end type safety as possible without being prescriptive about your database or content provider selection.

We're able to type the response data as you would expect with normal TypeScript. For example:

```tsx filename="app/page.tsx" switcher
async function getData() {
  const res = await fetch('https://api.example.com/...')
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.
  return res.json()
}

export default async function Page() {
  const name = await getData()

  return '...'
}
```

For *complete* end-to-end type safety, this also requires your database or content provider to support TypeScript. This could be through using an [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) or type-safe query builder.

## Route-Aware Type Helpers

Next.js generates global helpers for App Router route types. These are available without imports and are generated during `next dev`, `next build`, or via [`next typegen`](/docs/app/api-reference/cli/next.md#next-typegen-options):

* [`PageProps`](/docs/app/api-reference/file-conventions/page.md#page-props-helper)
* [`LayoutProps`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper)
* [`RouteContext`](/docs/app/api-reference/file-conventions/route.md#route-context-helper)

## Examples

### Type Checking Next.js Configuration Files

You can use TypeScript and import types in your Next.js configuration by using `next.config.ts`.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  /* config options here */
}

export default nextConfig
```

Module resolution in `next.config.ts` is currently limited to CommonJS. However, ECMAScript Modules (ESM) syntax is available when [using Node.js native TypeScript resolver](#using-nodejs-native-typescript-resolver-for-nextconfigts) for Node.js v22.10.0 and higher.

When using the `next.config.js` file, you can add some type checking in your IDE using JSDoc as below:

```js filename="next.config.js"
// @ts-check

/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
}

module.exports = nextConfig
```

### Using Node.js Native TypeScript Resolver for `next.config.ts`

> **Note**: Available on Node.js v22.10.0+ and only when the feature is enabled. Next.js does not enable it.

Next.js detects the [Node.js native TypeScript resolver](https://nodejs.org/api/typescript.html) via [`process.features.typescript`](https://nodejs.org/api/process.html#processfeaturestypescript), added in **v22.10.0**. When present, `next.config.ts` can use native ESM, including top‑level `await` and dynamic `import()`. This mechanism inherits the capabilities and limitations of Node's resolver.

In Node.js versions **v22.18.0+**, `process.features.typescript` is enabled by default. For versions between **v22.10.0** and **22.17.x**, opt in with `NODE_OPTIONS=--experimental-transform-types`:

```bash filename="Terminal"
NODE_OPTIONS=--experimental-transform-types next <command>
```

#### For CommonJS Projects (Default)

Although `next.config.ts` supports native ESM syntax on CommonJS projects, Node.js will still assume `next.config.ts` is a CommonJS file by default, resulting in Node.js reparsing the file as ESM when module syntax is detected. Therefore, we recommend using the `next.config.mts` file for CommonJS projects to explicitly indicate it's an ESM module:

```ts filename="next.config.mts"
import type { NextConfig } from 'next'

// Top-level await and dynamic import are supported
const flags = await import('./flags.js').then((m) => m.default ?? m)

const nextConfig: NextConfig = {
  /* config options here */
  typedRoutes: Boolean(flags?.typedRoutes),
}

export default nextConfig
```

#### For ESM Projects

When `"type"` is set to `"module"` in `package.json`, your project uses ESM. Learn more about this setting [in the Node.js docs](https://nodejs.org/api/packages.html#type). In this case, you can write `next.config.ts` directly with ESM syntax.

> **Good to know**: When using `"type": "module"` in your `package.json`, all `.js` and `.ts` files in your project are treated as ESM modules by default. You may need to rename files with CommonJS syntax to `.cjs` or `.cts` extensions if needed.

### Statically Typed Links

Next.js can statically type links to prevent typos and other errors when using `next/link`, improving type safety when navigating between pages.

Works in both the Pages and App Router for the `href` prop in `next/link`. In the App Router, it also types `next/navigation` methods like `push`, `replace`, and `prefetch`. It does not type `next/router` methods in Pages Router.

Literal `href` strings are validated, while non-literal `href`s may require a cast with `as Route`.

To opt-into this feature, `typedRoutes` need to be enabled and the project needs to be using TypeScript.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  typedRoutes: true,
}

export default nextConfig
```

Next.js will generate a link definition in `.next/types` that contains information about all existing routes in your application, which TypeScript can then use to provide feedback in your editor about invalid links.

> **Good to know**: If you set up your project without `create-next-app`, ensure the generated Next.js types are included by adding `.next/types/**/*.ts` to the `include` array in your `tsconfig.json`:

```json filename="tsconfig.json" highlight={4}
{
  "include": [
    "next-env.d.ts",
    ".next/types/**/*.ts",
    "**/*.ts",
    "**/*.tsx"
  ],
  "exclude": ["node_modules"]
}
```

Currently, support includes any string literal, including dynamic segments. For non-literal strings, you need to manually cast with `as Route`. The example below shows both `next/link` and `next/navigation` usage:

```tsx filename="app/example-client.tsx"
'use client'

import type { Route } from 'next'
import Link from 'next/link'
import { useRouter } from 'next/navigation'

export default function Example() {
  const router = useRouter()
  const slug = 'nextjs'

  return (
    <>
      {/* Link: literal and dynamic */}
      <Link href="/about" />
      <Link href={`/blog/${slug}`} />
      <Link href={('/blog/' + slug) as Route} />
      {/* TypeScript error if href is not a valid route */}
      <Link href="/aboot" />

      {/* Router: literal and dynamic strings are validated */}
      <button onClick={() => router.push('/about')}>Push About</button>
      <button onClick={() => router.replace(`/blog/${slug}`)}>
        Replace Blog
      </button>
      <button onClick={() => router.prefetch('/contact')}>
        Prefetch Contact
      </button>

      {/* For non-literal strings, cast to Route */}
      <button onClick={() => router.push(('/blog/' + slug) as Route)}>
        Push Non-literal Blog
      </button>
    </>
  )
}
```

The same applies for redirecting routes defined by proxy:

```ts filename="proxy.ts"
import { NextRequest, NextResponse } from 'next/server'

export function proxy(request: NextRequest) {
  if (request.nextUrl.pathname === '/proxy-redirect') {
    return NextResponse.redirect(new URL('/', request.url))
  }

  return NextResponse.next()
}
```

```tsx filename="app/some/page.tsx"
import type { Route } from 'next'

export default function Page() {
  return <Link href={'/proxy-redirect' as Route}>Link Text</Link>
}
```

To accept `href` in a custom component wrapping `next/link`, use a generic:

```tsx
import type { Route } from 'next'
import Link from 'next/link'

function Card<T extends string>({ href }: { href: Route<T> | URL }) {
  return (
    <Link href={href}>
      <div>My Card</div>
    </Link>
  )
}
```

You can also type a simple data structure and iterate to render links:

```ts filename="components/nav-items.ts"
import type { Route } from 'next'

type NavItem<T extends string = string> = {
  href: T
  label: string
}

export const navItems: NavItem<Route>[] = [
  { href: '/', label: 'Home' },
  { href: '/about', label: 'About' },
  { href: '/blog', label: 'Blog' },
]
```

Then, map over the items to render `Link`s:

```tsx filename="components/nav.tsx"
import Link from 'next/link'
import { navItems } from './nav-items'

export function Nav() {
  return (
    <nav>
      {navItems.map((item) => (
        <Link key={item.href} href={item.href}>
          {item.label}
        </Link>
      ))}
    </nav>
  )
}
```

> **How does it work?**
>
> When running `next dev` or `next build`, Next.js generates a hidden `.d.ts` file inside `.next` that contains information about all existing routes in your application (all valid routes as the `href` type of `Link`). This `.d.ts` file is included in `tsconfig.json` and the TypeScript compiler will check that `.d.ts` and provide feedback in your editor about invalid links.

### Type IntelliSense for Environment Variables

During development, Next.js generates a `.d.ts` file in `.next/types` that contains information about the loaded environment variables for your editor's IntelliSense. If the same environment variable key is defined in multiple files, it is deduplicated according to the [Environment Variable Load Order](/docs/app/guides/environment-variables.md#environment-variable-load-order).

To opt-into this feature, `experimental.typedEnv` needs to be enabled and the project needs to be using TypeScript.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    typedEnv: true,
  },
}

export default nextConfig
```

> **Good to know**: Types are generated based on the environment variables loaded at development runtime, which excludes variables from `.env.production*` files by default. To include production-specific variables, run `next dev` with `NODE_ENV=production`.

### With Async Server Components

To use an `async` Server Component with TypeScript, ensure you are using TypeScript `5.1.3` or higher and `@types/react` `18.2.8` or higher.

If you are using an older version of TypeScript, you may see a `'Promise<Element>' is not a valid JSX element` type error. Updating to the latest version of TypeScript and `@types/react` should resolve this issue.

### Incremental type checking

Since `v10.2.1` Next.js supports [incremental type checking](https://www.typescriptlang.org/tsconfig#incremental) when enabled in your `tsconfig.json`, this can help speed up type checking in larger applications.

### Custom `tsconfig` path

In some cases, you might want to use a different TypeScript configuration for builds or tooling. To do that, set `typescript.tsconfigPath` in `next.config.ts` to point Next.js to another `tsconfig` file.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  typescript: {
    tsconfigPath: 'tsconfig.build.json',
  },
}

export default nextConfig
```

For example, switch to a different config for production builds:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const isProd = process.env.NODE_ENV === 'production'

const nextConfig: NextConfig = {
  typescript: {
    tsconfigPath: isProd ? 'tsconfig.build.json' : 'tsconfig.json',
  },
}

export default nextConfig
```

<details>
<summary>Why you might use a separate `tsconfig` for builds</summary>

You might need to relax checks in scenarios like monorepos, where the build also validates shared dependencies that don't match your project's standards, or when loosening checks in CI to continue delivering while migrating locally to stricter TypeScript settings (and still wanting your IDE to highlight misuse).

For example, if your project uses `useUnknownInCatchVariables` but some monorepo dependencies still assume `any`:

```json filename="tsconfig.build.json"
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "useUnknownInCatchVariables": false
  }
}
```

This keeps your editor strict via `tsconfig.json` while allowing the production build to use relaxed settings.

</details>

> **Good to know**:
>
> * IDEs typically read `tsconfig.json` for diagnostics and IntelliSense, so you can still see IDE warnings while production builds use the alternate config. Mirror critical options if you want parity in the editor.
> * In development, only `tsconfig.json` is watched for changes. If you edit a different file name via `typescript.tsconfigPath`, restart the dev server to apply changes.
> * The configured file is used in `next dev`, `next build`, and `next typegen`.

### Disabling TypeScript errors in production

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

Open `next.config.ts` and enable the `ignoreBuildErrors` option in the `typescript` config:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}

export default nextConfig
```

> **Good to know**: You can run `tsc --noEmit` to check for TypeScript errors yourself before building. This is useful for CI/CD pipelines where you'd like to check for TypeScript errors before deploying.

### Custom type declarations

When you need to declare custom types, you might be tempted to modify `next-env.d.ts`. However, this file is automatically generated, so any changes you make will be overwritten. Instead, you should create a new file, let's call it `new-types.d.ts`, and reference it in your `tsconfig.json`:

```json filename="tsconfig.json"
{
  "compilerOptions": {
    "skipLibCheck": true
    //...truncated...
  },
  "include": [
    "new-types.d.ts",
    "next-env.d.ts",
    ".next/types/**/*.ts",
    "**/*.ts",
    "**/*.tsx"
  ],
  "exclude": ["node_modules"]
}
```

## Version Changes

| Version   | Changes                                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `v15.0.0` | [`next.config.ts`](#type-checking-nextjs-configuration-files) support added for TypeScript projects.                                 |
| `v13.2.0` | Statically typed links are available in beta.                                                                                        |
| `v12.0.0` | [SWC](/docs/architecture/nextjs-compiler.md) is now used by default to compile TypeScript and TSX for faster builds.                    |
| `v10.2.1` | [Incremental type checking](https://www.typescriptlang.org/tsconfig#incremental) support added when enabled in your `tsconfig.json`. |


--------------------------------------------------------------------------------
title: "ESLint Plugin"
description: "Learn how to use and configure the ESLint plugin to catch common issues and problems in a Next.js application."
source: "https://nextjs.org/docs/app/api-reference/config/eslint"
--------------------------------------------------------------------------------

# ESLint

Next.js provides an ESLint plugin, [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next), already bundled within the base configuration that makes it possible to catch common issues and problems in a Next.js application.

## Setup ESLint

Get linting working quickly with the ESLint CLI (flat config):

1. Install ESLint and the Next.js config:

   ```bash package="pnpm"
   pnpm add -D eslint eslint-config-next
   ```

   ```bash package="npm"
   npm i -D eslint eslint-config-next
   ```

   ```bash package="yarn"
   yarn add --dev eslint eslint-config-next
   ```

   ```bash package="bun"
   bun add -d eslint eslint-config-next
   ```

2. Create `eslint.config.mjs` with the Next.js config:

   ```js filename="eslint.config.mjs"
   import { defineConfig, globalIgnores } from 'eslint/config'
   import nextVitals from 'eslint-config-next/core-web-vitals'

   const eslintConfig = defineConfig([
     ...nextVitals,
     // Override default ignores of eslint-config-next.
     globalIgnores([
       // Default ignores of eslint-config-next:
       '.next/**',
       'out/**',
       'build/**',
       'next-env.d.ts',
     ]),
   ])

   export default eslintConfig
   ```

3. Run ESLint:

   ```bash package="pnpm"
   pnpm exec eslint .
   ```

   ```bash package="npm"
   npx eslint .
   ```

   ```bash package="yarn"
   yarn eslint .
   ```

   ```bash package="bun"
   bunx eslint .
   ```

## Reference

Recommended rule-sets from the following ESLint plugins are all used within `eslint-config-next`:

* [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react)
* [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks)
* [`@next/eslint-plugin-next`](https://www.npmjs.com/package/@next/eslint-plugin-next)

### Rules

The full set of rules is as follows:

| Enabled in recommended config | Rule                                                                                                                     | Description                                                                                                      |
| :---------------------------: | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
|            | [@next/next/google-font-display](/docs/messages/google-font-display.md)                                                     | Enforce font-display behavior with Google Fonts.                                                                 |
|            | [@next/next/google-font-preconnect](/docs/messages/google-font-preconnect.md)                                               | Ensure `preconnect` is used with Google Fonts.                                                                   |
|            | [@next/next/inline-script-id](/docs/messages/inline-script-id.md)                                                           | Enforce `id` attribute on `next/script` components with inline content.                                          |
|            | [@next/next/next-script-for-ga](/docs/messages/next-script-for-ga.md)                                                       | Prefer `next/script` component when using the inline script for Google Analytics.                                |
|            | [@next/next/no-assign-module-variable](/docs/messages/no-assign-module-variable.md)                                         | Prevent assignment to the `module` variable.                                                                     |
|            | [@next/next/no-async-client-component](/docs/messages/no-async-client-component.md)                                         | Prevent Client Components from being async functions.                                                            |
|            | [@next/next/no-before-interactive-script-outside-document](/docs/messages/no-before-interactive-script-outside-document.md) | Prevent usage of `next/script`'s `beforeInteractive` strategy outside of `pages/_document.js`.                   |
|            | [@next/next/no-css-tags](/docs/messages/no-css-tags.md)                                                                     | Prevent manual stylesheet tags.                                                                                  |
|            | [@next/next/no-document-import-in-page](/docs/messages/no-document-import-in-page.md)                                       | Prevent importing `next/document` outside of `pages/_document.js`.                                               |
|            | [@next/next/no-duplicate-head](/docs/messages/no-duplicate-head.md)                                                         | Prevent duplicate usage of `<Head>` in `pages/_document.js`.                                                     |
|            | [@next/next/no-head-element](/docs/messages/no-head-element.md)                                                             | Prevent usage of `<head>` element.                                                                               |
|            | [@next/next/no-head-import-in-document](/docs/messages/no-head-import-in-document.md)                                       | Prevent usage of `next/head` in `pages/_document.js`.                                                            |
|            | [@next/next/no-html-link-for-pages](/docs/messages/no-html-link-for-pages.md)                                               | Prevent usage of `<a>` elements to navigate to internal Next.js pages.                                           |
|            | [@next/next/no-img-element](/docs/messages/no-img-element.md)                                                               | Prevent usage of `<img>` element due to slower LCP and higher bandwidth.                                         |
|            | [@next/next/no-page-custom-font](/docs/messages/no-page-custom-font.md)                                                     | Prevent page-only custom fonts.                                                                                  |
|            | [@next/next/no-script-component-in-head](/docs/messages/no-script-component-in-head.md)                                     | Prevent usage of `next/script` in `next/head` component.                                                         |
|            | [@next/next/no-styled-jsx-in-document](/docs/messages/no-styled-jsx-in-document.md)                                         | Prevent usage of `styled-jsx` in `pages/_document.js`.                                                           |
|            | [@next/next/no-sync-scripts](/docs/messages/no-sync-scripts.md)                                                             | Prevent synchronous scripts.                                                                                     |
|            | [@next/next/no-title-in-document-head](/docs/messages/no-title-in-document-head.md)                                         | Prevent usage of `<title>` with `Head` component from `next/document`.                                           |
|            | @next/next/no-typos                                                                                                      | Prevent common typos in [Next.js's data fetching functions](/docs/pages/building-your-application/data-fetching.md) |
|            | [@next/next/no-unwanted-polyfillio](/docs/messages/no-unwanted-polyfillio.md)                                               | Prevent duplicate polyfills from Polyfill.io.                                                                    |

We recommend using an appropriate [integration](https://eslint.org/docs/user-guide/integrations#editors) to view warnings and errors directly in your code editor during development.

<details>
<summary>`next lint` removal</summary>

Starting with Next.js 16, `next lint` is removed.

As part of the removal, the `eslint` option in your Next config file is no longer needed and can be safely removed.

</details>

## Examples

### Specifying a root directory within a monorepo

If you're using `@next/eslint-plugin-next` in a project where Next.js isn't installed in your root directory (such as a monorepo), you can tell `@next/eslint-plugin-next` where to find your Next.js application using the `settings` property in your `eslint.config.mjs`:

```js filename="eslint.config.mjs"
import { defineConfig } from 'eslint/config'
import eslintNextPlugin from '@next/eslint-plugin-next'

const eslintConfig = defineConfig([
  {
    plugins: {
      next: eslintNextPlugin,
    },
    settings: {
      next: {
        rootDir: 'packages/my-app/',
      },
    },
    files: [
      // ...files
    ],
    ignores: [
      // ...ignores
    ],
  },
])

export default eslintConfig
```

`rootDir` can be a path (relative or absolute), a glob (i.e. `"packages/*/"`), or an array of paths and/or globs.

### Disabling rules

If you would like to modify or disable any rules provided by the supported plugins (`react`, `react-hooks`, `next`), you can directly change them using the `rules` property in your `eslint.config.mjs`:

```js filename="eslint.config.mjs"
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'

const eslintConfig = defineConfig([
  ...nextVitals,
  {
    rules: {
      'react/no-unescaped-entities': 'off',
      '@next/next/no-page-custom-font': 'off',
    },
  },
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])

export default eslintConfig
```

### With Core Web Vitals

Enable the `next/core-web-vitals` rule set by extending it in your ESLint config.

```js filename="eslint.config.mjs"
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'

const eslintConfig = defineConfig([
  ...nextVitals,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])

export default eslintConfig
```

`next/core-web-vitals` updates `@next/eslint-plugin-next` to error on a number of rules that are warnings by default if they affect [Core Web Vitals](https://web.dev/vitals/).

> The `next/core-web-vitals` entry point is automatically included for new applications built with [Create Next App](/docs/app/api-reference/cli/create-next-app.md).

### With TypeScript

In addition to the Next.js ESLint rules, `create-next-app --typescript` will also add TypeScript-specific lint rules with `next/typescript` to your config:

```js filename="eslint.config.mjs"
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import nextTs from 'eslint-config-next/typescript'

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])

export default eslintConfig
```

Those rules are based on [`plugin:@typescript-eslint/recommended`](https://typescript-eslint.io/linting/configs#recommended).
See [typescript-eslint > Configs](https://typescript-eslint.io/linting/configs) for more details.

### With Prettier

ESLint also contains code formatting rules, which can conflict with your existing [Prettier](https://prettier.io/) setup. We recommend including [eslint-config-prettier](https://github.com/prettier/eslint-config-prettier) in your ESLint config to make ESLint and Prettier work together.

First, install the dependency:

```bash package="pnpm"
pnpm add -D eslint-config-prettier
```

```bash package="npm"
npm i -D eslint-config-prettier
```

```bash package="yarn"
yarn add --dev eslint-config-prettier
```

```bash package="bun"
bun add -d eslint-config-prettier
```

Then, add `prettier` to your existing ESLint config:

```js filename="eslint.config.mjs"
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import prettier from 'eslint-config-prettier/flat'

const eslintConfig = defineConfig([
  ...nextVitals,
  prettier,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    '.next/**',
    'out/**',
    'build/**',
    'next-env.d.ts',
  ]),
])

export default eslintConfig
```

### Running lint on staged files

If you would like to use ESLint with [lint-staged](https://github.com/okonet/lint-staged) to run the linter on staged git files, add the following to the `.lintstagedrc.js` file in the root of your project:

```js filename=".lintstagedrc.js"
const path = require('path')

const buildEslintCommand = (filenames) =>
  `eslint --fix ${filenames
    .map((f) => `"${path.relative(process.cwd(), f)}"`)
    .join(' ')}`

module.exports = {
  '*.{js,jsx,ts,tsx}': [buildEslintCommand],
}
```

### Migrating existing config

If you already have ESLint configured in your application, we recommend extending from this plugin directly instead of including `eslint-config-next` unless a few conditions are met.

#### Recommended plugin ruleset

If the following conditions are true:

* You have one or more of the following plugins already installed (either separately or through a different config such as `airbnb` or `react-app`):
  * `react`
  * `react-hooks`
  * `jsx-a11y`
  * `import`
* You've defined specific `parserOptions` that are different from how Babel is configured within Next.js (this is not recommended unless you have [customized your Babel configuration](/docs/pages/guides/babel.md))
* You have `eslint-plugin-import` installed with Node.js and/or TypeScript [resolvers](https://github.com/benmosher/eslint-plugin-import#resolvers) defined to handle imports

Then we recommend either removing these settings if you prefer how these properties have been configured within [`eslint-config-next`](https://github.com/vercel/next.js/blob/canary/packages/eslint-config-next/index.js) or extending directly from the Next.js ESLint plugin instead:

```js
module.exports = {
  extends: [
    //...
    'plugin:@next/next/recommended',
  ],
}
```

The plugin can be installed normally in your project:

```bash package="pnpm"
pnpm add -D @next/eslint-plugin-next
```

```bash package="npm"
npm i -D @next/eslint-plugin-next
```

```bash package="yarn"
yarn add --dev @next/eslint-plugin-next
```

```bash package="bun"
bun add -d @next/eslint-plugin-next
```

This eliminates the risk of collisions or errors that can occur due to importing the same plugin or parser across multiple configurations.

#### Additional configurations

If you already use a separate ESLint configuration and want to include `eslint-config-next`, ensure that it is extended last after other configurations. For example:

```js filename="eslint.config.mjs"
import { defineConfig, globalIgnores } from 'eslint/config'
import nextPlugin from '@next/eslint-plugin-next'

const eslintConfig = defineConfig([
  nextPlugin.configs['core-web-vitals'],
  // List of ignore patterns.
  globalIgnores([]),
])

export default eslintConfig
```

The `next` configuration already handles setting default values for the `parser`, `plugins` and `settings` properties. There is no need to manually re-declare any of these properties unless you need a different configuration for your use case.

If you include any other shareable configurations, **you will need to make sure that these properties are not overwritten or modified**. Otherwise, we recommend removing any configurations that share behavior with the `next` configuration or extending directly from the Next.js ESLint plugin as mentioned above.

| Version   | Changes                                                                                                                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `next lint` and the `eslint` next.config.js option were removed in favor of the ESLint CLI. A [codemod](/docs/app/guides/upgrading/codemods.md#migrate-from-next-lint-to-eslint-cli) is available to help you migrate. |


--------------------------------------------------------------------------------
title: "CLI"
description: "API Reference for the Next.js Command Line Interface (CLI) tools."
source: "https://nextjs.org/docs/app/api-reference/cli"
--------------------------------------------------------------------------------

# CLI

Next.js comes with **two** Command Line Interface (CLI) tools:

* **`create-next-app`**: Quickly create a new Next.js application using the default template or an [example](https://github.com/vercel/next.js/tree/canary/examples) from a public GitHub repository.
* **`next`**: Run the Next.js development server, build your application, and more.

 - [create-next-app](/docs/app/api-reference/cli/create-next-app.md)
 - [next CLI](/docs/app/api-reference/cli/next.md)

--------------------------------------------------------------------------------
title: "create-next-app"
description: "Create Next.js apps using one command with the create-next-app CLI."
source: "https://nextjs.org/docs/app/api-reference/cli/create-next-app"
--------------------------------------------------------------------------------

# create-next-app

The `create-next-app` CLI allow you to create a new Next.js application using the default template or an [example](https://github.com/vercel/next.js/tree/canary/examples) from a public GitHub repository. It is the easiest way to get started with Next.js.

Basic usage:

```bash filename="Terminal"
npx create-next-app@latest [project-name] [options]
```

## Reference

The following options are available:

| Options                                 | Description                                                           |
| --------------------------------------- | --------------------------------------------------------------------- |
| `-h` or `--help`                        | Show all available options                                            |
| `-v` or `--version`                     | Output the version number                                             |
| `--no-*`                                | Negate default options. E.g. `--no-ts`                                |
| `--ts` or `--typescript`                | Initialize as a TypeScript project (default)                          |
| `--js` or `--javascript`                | Initialize as a JavaScript project                                    |
| `--tailwind`                            | Initialize with Tailwind CSS config (default)                         |
| `--react-compiler`                      | Initialize with React Compiler enabled                                |
| `--eslint`                              | Initialize with ESLint config                                         |
| `--biome`                               | Initialize with Biome config                                          |
| `--no-linter`                           | Skip linter configuration                                             |
| `--app`                                 | Initialize as an App Router project                                   |
| `--api`                                 | Initialize a project with only route handlers                         |
| `--src-dir`                             | Initialize inside a `src/` directory                                  |
| `--turbopack`                           | Force enable Turbopack in generated package.json (enabled by default) |
| `--webpack`                             | Force enable Webpack in generated package.json                        |
| `--import-alias <alias-to-configure>`   | Specify import alias to use (default "@/\*")                          |
| `--empty`                               | Initialize an empty project                                           |
| `--use-npm`                             | Explicitly tell the CLI to bootstrap the application using npm        |
| `--use-pnpm`                            | Explicitly tell the CLI to bootstrap the application using pnpm       |
| `--use-yarn`                            | Explicitly tell the CLI to bootstrap the application using Yarn       |
| `--use-bun`                             | Explicitly tell the CLI to bootstrap the application using Bun        |
| `-e` or `--example [name] [github-url]` | An example to bootstrap the app with                                  |
| `--example-path <path-to-example>`      | Specify the path to the example separately                            |
| `--reset-preferences`                   | Explicitly tell the CLI to reset any stored preferences               |
| `--skip-install`                        | Explicitly tell the CLI to skip installing packages                   |
| `--disable-git`                         | Explicitly tell the CLI to disable git initialization                 |
| `--yes`                                 | Use previous preferences or defaults for all options                  |

## Examples

### With the default template

To create a new app using the default template, run the following command in your terminal:

```bash filename="Terminal"
npx create-next-app@latest
```

On installation, you'll see the following prompts:

```txt filename="Terminal"
What is your project named? my-app
Would you like to use the recommended Next.js defaults?
    Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
    No, reuse previous settings
    No, customize settings - Choose your own preferences
```

If you choose to `customize settings`, you'll see the following prompts:

```txt filename="Terminal"
Would you like to use TypeScript? No / Yes
Which linter would you like to use? ESLint / Biome / None
Would you like to use React Compiler? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

After the prompts, `create-next-app` will create a folder with your project name and install the required dependencies.

### Linter Options

**ESLint**: The traditional and most popular JavaScript linter. Includes Next.js-specific rules from `@next/eslint-plugin-next`.

**Biome**: A fast, modern linter and formatter that combines the functionality of ESLint and Prettier. Includes built-in Next.js and React domain support for optimal performance.

**None**: Skip linter configuration entirely. You can always add a linter later.

Once you've answered the prompts, a new project will be created with your chosen configuration.

### With an official Next.js example

To create a new app using an official Next.js example, use the `--example` flag. For example:

```bash filename="Terminal"
npx create-next-app@latest --example [example-name] [your-project-name]
```

You can view a list of all available examples along with setup instructions in the [Next.js repository](https://github.com/vercel/next.js/tree/canary/examples).

### With any public GitHub example

To create a new app using any public GitHub example, use the `--example` option with the GitHub repo's URL. For example:

```bash filename="Terminal"
npx create-next-app@latest --example "https://github.com/.../" [your-project-name]
```


--------------------------------------------------------------------------------
title: "next CLI"
description: "Learn how to run and build your application with the Next.js CLI."
source: "https://nextjs.org/docs/app/api-reference/cli/next"
--------------------------------------------------------------------------------

# next CLI

The Next.js CLI allows you to develop, build, start your application, and more.

Basic usage:

```bash filename="Terminal"
npx next [command] [options]
```

## Reference

The following options are available:

| Options             | Description                        |
| ------------------- | ---------------------------------- |
| `-h` or `--help`    | Shows all available options        |
| `-v` or `--version` | Outputs the Next.js version number |

### Commands

The following commands are available:

| Command                                | Description                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [`dev`](#next-dev-options)             | Starts Next.js in development mode with Hot Module Reloading, error reporting, and more.                      |
| [`build`](#next-build-options)         | Creates an optimized production build of your application. Displaying information about each route.           |
| [`start`](#next-start-options)         | Starts Next.js in production mode. The application should be compiled with `next build` first.                |
| [`info`](#next-info-options)           | Prints relevant details about the current system which can be used to report Next.js bugs.                    |
| [`telemetry`](#next-telemetry-options) | Allows you to enable or disable Next.js' completely anonymous telemetry collection.                           |
| [`typegen`](#next-typegen-options)     | Generates TypeScript definitions for routes, pages, layouts, and route handlers without running a full build. |

> **Good to know**: Running `next` without a command is an alias for `next dev`.

### `next dev` options

`next dev` starts the application in development mode with Hot Module Reloading (HMR), error reporting, and more. The following options are available when running `next dev`:

| Option                                   | Description                                                                                                                                          |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-h, --help`                             | Show all available options.                                                                                                                          |
| `[directory]`                            | A directory in which to build the application. If not provided, current directory is used.                                                           |
| `--turbopack`                            | Force enable [Turbopack](/docs/app/api-reference/turbopack.md) (enabled by default). Also available as `--turbo`.                                       |
| `--webpack`                              | Use Webpack instead of the default [Turbopack](/docs/app/api-reference/turbopack.md) bundler for development.                                           |
| `-p` or `--port <port>`                  | Specify a port number on which to start the application. Default: 3000, env: PORT                                                                    |
| `-H`or `--hostname <hostname>`           | Specify a hostname on which to start the application. Useful for making the application available for other devices on the network. Default: 0.0.0.0 |
| `--experimental-https`                   | Starts the server with HTTPS and generates a self-signed certificate.                                                                                |
| `--experimental-https-key <path>`        | Path to a HTTPS key file.                                                                                                                            |
| `--experimental-https-cert <path>`       | Path to a HTTPS certificate file.                                                                                                                    |
| `--experimental-https-ca <path>`         | Path to a HTTPS certificate authority file.                                                                                                          |
| `--experimental-upload-trace <traceUrl>` | Reports a subset of the debugging trace to a remote HTTP URL.                                                                                        |

### `next build` options

`next build` creates an optimized production build of your application. The output displays information about each route. For example:

```bash filename="Terminal"
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]

○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

The following options are available for the `next build` command:

| Option                             | Description                                                                                                                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-h, --help`                       | Show all available options.                                                                                                                                                        |
| `[directory]`                      | A directory on which to build the application. If not provided, the current directory will be used.                                                                                |
| `--turbopack`                      | Force enable [Turbopack](/docs/app/api-reference/turbopack.md) (enabled by default). Also available as `--turbo`.                                                                     |
| `--webpack`                        | Build using Webpack.                                                                                                                                                               |
| `-d` or `--debug`                  | Enables a more verbose build output. With this flag enabled additional build output like rewrites, redirects, and headers will be shown.                                           |
|                                    |
| `--profile`                        | Enables production [profiling for React](https://react.dev/reference/react/Profiler).                                                                                              |
| `--no-lint`                        | Disables linting. *Note: linting will be removed from `next build` in Next 16. If you're using Next 15.5+ with a linter other than `eslint`, linting during build will not occur.* |
| `--no-mangling`                    | Disables [mangling](https://en.wikipedia.org/wiki/Name_mangling). This may affect performance and should only be used for debugging purposes.                                      |
| `--experimental-app-only`          | Builds only App Router routes.                                                                                                                                                     |
| `--experimental-build-mode [mode]` | Uses an experimental build mode. (choices: "compile", "generate", default: "default")                                                                                              |
| `--debug-prerender`                | Debug prerender errors in development.                                                                                                                                             |
| `--debug-build-paths=<patterns>`   | Build only specific routes for debugging.                                                                                                                                          |

### `next start` options

`next start` starts the application in production mode. The application should be compiled with [`next build`](#next-build-options) first.

The following options are available for the `next start` command:

| Option                                  | Description                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `-h` or `--help`                        | Show all available options.                                                                                     |
| `[directory]`                           | A directory on which to start the application. If no directory is provided, the current directory will be used. |
| `-p` or `--port <port>`                 | Specify a port number on which to start the application. (default: 3000, env: PORT)                             |
| `-H` or `--hostname <hostname>`         | Specify a hostname on which to start the application (default: 0.0.0.0).                                        |
| `--keepAliveTimeout <keepAliveTimeout>` | Specify the maximum amount of milliseconds to wait before closing the inactive connections.                     |

### `next info` options

`next info` prints relevant details about the current system which can be used to report Next.js bugs when opening a [GitHub issue](https://github.com/vercel/next.js/issues). This information includes Operating System platform/arch/version, Binaries (Node.js, npm, Yarn, pnpm), package versions (`next`, `react`, `react-dom`), and more.

The output should look like this:

```bash filename="Terminal"
Operating System:
  Platform: darwin
  Arch: arm64
  Version: Darwin Kernel Version 23.6.0
  Available memory (MB): 65536
  Available CPU cores: 10
Binaries:
  Node: 20.12.0
  npm: 10.5.0
  Yarn: 1.22.19
  pnpm: 9.6.0
Relevant Packages:
  next: 15.0.0-canary.115 // Latest available version is detected (15.0.0-canary.115).
  eslint-config-next: 14.2.5
  react: 19.0.0-rc
  react-dom: 19.0.0
  typescript: 5.5.4
Next.js Config:
  output: N/A
```

The following options are available for the `next info` command:

| Option           | Description                                    |
| ---------------- | ---------------------------------------------- |
| `-h` or `--help` | Show all available options                     |
| `--verbose`      | Collects additional information for debugging. |

### `next telemetry` options

Next.js collects **completely anonymous** telemetry data about general usage. Participation in this anonymous program is optional, and you can opt-out if you prefer not to share information.

The following options are available for the `next telemetry` command:

| Option       | Description                             |
| ------------ | --------------------------------------- |
| `-h, --help` | Show all available options.             |
| `--enable`   | Enables Next.js' telemetry collection.  |
| `--disable`  | Disables Next.js' telemetry collection. |

Learn more about [Telemetry](/telemetry).

### `next typegen` options

`next typegen` generates TypeScript definitions for your application's routes without performing a full build. This is useful for IDE autocomplete and CI type-checking of route usage.

Previously, route types were only generated during `next dev` or `next build`, which meant running `tsc --noEmit` directly wouldn't validate your route types. Now you can generate types independently and validate them externally:

```bash filename="Terminal"
# Generate route types first, then validate with TypeScript
next typegen && tsc --noEmit

# Or in CI workflows for type checking without building
next typegen && npm run type-check
```

The following options are available for the `next typegen` command:

| Option        | Description                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------- |
| `-h, --help`  | Show all available options.                                                                  |
| `[directory]` | A directory on which to generate types. If not provided, the current directory will be used. |

Output files are written to `<distDir>/types` (typically: `.next/dev/types` or `.next/types`, see [`isolatedDevBuild`](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md)):

```bash filename="Terminal"
next typegen
# or for a specific app
next typegen ./apps/web
```

Additionally, `next typegen` generates a `next-env.d.ts` file. We recommend adding `next-env.d.ts` to your `.gitignore` file.

The `next-env.d.ts` file is included into your `tsconfig.json` file, to make Next.js types available to your project.

To ensure `next-env.d.ts` is present before type-checking run `next typegen`. The commands `next dev` and `next build` also generate the `next-env.d.ts` file, but it is often undesirable to run these just to type-check, for example in CI/CD environments.

> **Good to know**: `next typegen` loads your Next.js config (`next.config.js`, `next.config.mjs`, or `next.config.ts`) using the production build phase. Ensure any required environment variables and dependencies are available so the config can load correctly.

## Examples

### Debugging prerender errors

If you encounter prerendering errors during `next build`, you can pass the `--debug-prerender` flag to get more detailed output:

```bash filename="Terminal"
next build --debug-prerender
```

This enables several experimental options to make debugging easier:

* Disables server code minification:
  * `experimental.serverMinification = false`
  * `experimental.turbopackMinify = false`
* Generates source maps for server bundles:
  * `experimental.serverSourceMaps = true`
* Enables source map consumption in child processes used for prerendering:
  * `enablePrerenderSourceMaps = true`
* Continues building even after the first prerender error, so you can see all issues at once:
  * `experimental.prerenderEarlyExit = false`

This helps surface more readable stack traces and code frames in the build output.

> **Warning**: `--debug-prerender` is for debugging in development only. Do not deploy builds generated with `--debug-prerender` to production, as it may impact performance.

### Building specific routes

You can build only specific routes in the App and Pages Routers using the `--debug-build-paths` option. This is useful for faster debugging when working with large applications. The `--debug-build-paths` option accepts comma-separated file paths and supports glob patterns:

```bash filename="Terminal"
# Build a specific route
next build --debug-build-paths="app/page.tsx"

# Build more than one route
next build --debug-build-paths="app/page.tsx,pages/index.tsx"

# Use glob patterns
next build --debug-build-paths="app/**/page.tsx"
next build --debug-build-paths="pages/*.tsx"
```

### Changing the default port

By default, Next.js uses `http://localhost:3000` during development and with `next start`. The default port can be changed with the `-p` option, like so:

```bash filename="Terminal"
next dev -p 4000
```

Or using the `PORT` environment variable:

```bash filename="Terminal"
PORT=4000 next dev
```

> **Good to know**: `PORT` cannot be set in `.env` as booting up the HTTP server happens before any other code is initialized.

### Using HTTPS during development

For certain use cases like webhooks or authentication, you can use [HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS) to have a secure environment on `localhost`. Next.js can generate a self-signed certificate with `next dev` using the `--experimental-https` flag:

```bash filename="Terminal"
next dev --experimental-https
```

With the generated certificate, the Next.js development server will exist at `https://localhost:3000`. The default port `3000` is used unless a port is specified with `-p`, `--port`, or `PORT`.

You can also provide a custom certificate and key with `--experimental-https-key` and `--experimental-https-cert`. Optionally, you can provide a custom CA certificate with `--experimental-https-ca` as well.

```bash filename="Terminal"
next dev --experimental-https --experimental-https-key ./certificates/localhost-key.pem --experimental-https-cert ./certificates/localhost.pem
```

`next dev --experimental-https` is only intended for development and creates a locally trusted certificate with [`mkcert`](https://github.com/FiloSottile/mkcert). In production, use properly issued certificates from trusted authorities.

### Configuring a timeout for downstream proxies

When deploying Next.js behind a downstream proxy (e.g. a load-balancer like AWS ELB/ALB), it's important to configure Next's underlying HTTP server with [keep-alive timeouts](https://nodejs.org/api/http.html#http_server_keepalivetimeout) that are *larger* than the downstream proxy's timeouts. Otherwise, once a keep-alive timeout is reached for a given TCP connection, Node.js will immediately terminate that connection without notifying the downstream proxy. This results in a proxy error whenever it attempts to reuse a connection that Node.js has already terminated.

To configure the timeout values for the production Next.js server, pass `--keepAliveTimeout` (in milliseconds) to `next start`, like so:

```bash filename="Terminal"
next start --keepAliveTimeout 70000
```

### Passing Node.js arguments

You can pass any [node arguments](https://nodejs.org/api/cli.html#cli_node_options_options) to `next` commands. For example:

```bash filename="Terminal"
NODE_OPTIONS='--throw-deprecation' next
NODE_OPTIONS='-r esm' next
NODE_OPTIONS='--inspect' next
```

| Version   | Changes                                                                         |
| --------- | ------------------------------------------------------------------------------- |
| `v16.0.0` | The JS bundle size metrics have been removed from `next build`                  |
| `v15.5.0` | Add the `next typegen` command                                                  |
| `v15.4.0` | Add `--debug-prerender` option for `next build` to help debug prerender errors. |


--------------------------------------------------------------------------------
title: "Edge Runtime"
description: "API Reference for the Edge Runtime."
source: "https://nextjs.org/docs/app/api-reference/edge"
--------------------------------------------------------------------------------

# Edge Runtime

Next.js has two server runtimes you can use in your application:

* The **Node.js Runtime** (default), which has access to all Node.js APIs and is used for rendering your application.
* The **Edge Runtime** which contains a more limited [set of APIs](#reference), used in [Proxy](/docs/app/api-reference/file-conventions/proxy.md).

## Caveats

* The Edge Runtime does not support all Node.js APIs. Some packages may not work as expected.
* The Edge Runtime does not support Incremental Static Regeneration (ISR).
* Both runtimes can support [streaming](/docs/app/api-reference/file-conventions/loading.md) depending on your deployment adapter.

## Reference

The Edge Runtime supports the following APIs:

### Network APIs

| API                                                                             | Description                       |
| ------------------------------------------------------------------------------- | --------------------------------- |
| [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob)                       | Represents a blob                 |
| [`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API)                 | Fetches a resource                |
| [`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent)           | Represents a fetch event          |
| [`File`](https://developer.mozilla.org/docs/Web/API/File)                       | Represents a file                 |
| [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData)               | Represents form data              |
| [`Headers`](https://developer.mozilla.org/docs/Web/API/Headers)                 | Represents HTTP headers           |
| [`Request`](https://developer.mozilla.org/docs/Web/API/Request)                 | Represents an HTTP request        |
| [`Response`](https://developer.mozilla.org/docs/Web/API/Response)               | Represents an HTTP response       |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Represents URL search parameters  |
| [`WebSocket`](https://developer.mozilla.org/docs/Web/API/WebSocket)             | Represents a websocket connection |

### Encoding APIs

| API                                                                                 | Description                        |
| ----------------------------------------------------------------------------------- | ---------------------------------- |
| [`atob`](https://developer.mozilla.org/en-US/docs/Web/API/atob)                     | Decodes a base-64 encoded string   |
| [`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/btoa)                     | Encodes a string in base-64        |
| [`TextDecoder`](https://developer.mozilla.org/docs/Web/API/TextDecoder)             | Decodes a Uint8Array into a string |
| [`TextDecoderStream`](https://developer.mozilla.org/docs/Web/API/TextDecoderStream) | Chainable decoder for streams      |
| [`TextEncoder`](https://developer.mozilla.org/docs/Web/API/TextEncoder)             | Encodes a string into a Uint8Array |
| [`TextEncoderStream`](https://developer.mozilla.org/docs/Web/API/TextEncoderStream) | Chainable encoder for streams      |

### Stream APIs

| API                                                                                                     | Description                             |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| [`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream)                           | Represents a readable stream            |
| [`ReadableStreamBYOBReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader)       | Represents a reader of a ReadableStream |
| [`ReadableStreamDefaultReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamDefaultReader) | Represents a reader of a ReadableStream |
| [`TransformStream`](https://developer.mozilla.org/docs/Web/API/TransformStream)                         | Represents a transform stream           |
| [`WritableStream`](https://developer.mozilla.org/docs/Web/API/WritableStream)                           | Represents a writable stream            |
| [`WritableStreamDefaultWriter`](https://developer.mozilla.org/docs/Web/API/WritableStreamDefaultWriter) | Represents a writer of a WritableStream |

### Crypto APIs

| API                                                                       | Description                                                                                         |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [`crypto`](https://developer.mozilla.org/docs/Web/API/Window/crypto)      | Provides access to the cryptographic functionality of the platform                                  |
| [`CryptoKey`](https://developer.mozilla.org/docs/Web/API/CryptoKey)       | Represents a cryptographic key                                                                      |
| [`SubtleCrypto`](https://developer.mozilla.org/docs/Web/API/SubtleCrypto) | Provides access to common cryptographic primitives, like hashing, signing, encryption or decryption |

### Web Standard APIs

| API                                                                                                                   | Description                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`AbortController`](https://developer.mozilla.org/docs/Web/API/AbortController)                                       | Allows you to abort one or more DOM requests as and when desired                                                                                                                                     |
| [`Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array)                           | Represents an array of values                                                                                                                                                                        |
| [`ArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer)               | Represents a generic, fixed-length raw binary data buffer                                                                                                                                            |
| [`Atomics`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Atomics)                       | Provides atomic operations as static methods                                                                                                                                                         |
| [`BigInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt)                         | Represents a whole number with arbitrary precision                                                                                                                                                   |
| [`BigInt64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array)           | Represents a typed array of 64-bit signed integers                                                                                                                                                   |
| [`BigUint64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array)         | Represents a typed array of 64-bit unsigned integers                                                                                                                                                 |
| [`Boolean`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean)                       | Represents a logical entity and can have two values: `true` and `false`                                                                                                                              |
| [`clearInterval`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearInterval)                 | Cancels a timed, repeating action which was previously established by a call to `setInterval()`                                                                                                      |
| [`clearTimeout`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout)                   | Cancels a timed, repeating action which was previously established by a call to `setTimeout()`                                                                                                       |
| [`console`](https://developer.mozilla.org/docs/Web/API/Console)                                                       | Provides access to the browser's debugging console                                                                                                                                                   |
| [`DataView`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/DataView)                     | Represents a generic view of an `ArrayBuffer`                                                                                                                                                        |
| [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date)                             | Represents a single moment in time in a platform-independent format                                                                                                                                  |
| [`decodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)                   | Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI` or by a similar routine                                                                                                |
| [`decodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) | Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent` or by a similar routine                                                                             |
| [`DOMException`](https://developer.mozilla.org/docs/Web/API/DOMException)                                             | Represents an error that occurs in the DOM                                                                                                                                                           |
| [`encodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)                   | Encodes a Uniform Resource Identifier (URI) by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character           |
| [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) | Encodes a Uniform Resource Identifier (URI) component by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character |
| [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error)                           | Represents an error when trying to execute a statement or accessing a property                                                                                                                       |
| [`EvalError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/EvalError)                   | Represents an error that occurs regarding the global function `eval()`                                                                                                                               |
| [`Float32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float32Array)             | Represents a typed array of 32-bit floating point numbers                                                                                                                                            |
| [`Float64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float64Array)             | Represents a typed array of 64-bit floating point numbers                                                                                                                                            |
| [`Function`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function)                     | Represents a function                                                                                                                                                                                |
| [`Infinity`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Infinity)                     | Represents the mathematical Infinity value                                                                                                                                                           |
| [`Int8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int8Array)                   | Represents a typed array of 8-bit signed integers                                                                                                                                                    |
| [`Int16Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int16Array)                 | Represents a typed array of 16-bit signed integers                                                                                                                                                   |
| [`Int32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int32Array)                 | Represents a typed array of 32-bit signed integers                                                                                                                                                   |
| [`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl)                             | Provides access to internationalization and localization functionality                                                                                                                               |
| [`isFinite`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isFinite)                     | Determines whether a value is a finite number                                                                                                                                                        |
| [`isNaN`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isNaN)                           | Determines whether a value is `NaN` or not                                                                                                                                                           |
| [`JSON`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON)                             | Provides functionality to convert JavaScript values to and from the JSON format                                                                                                                      |
| [`Map`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map)                               | Represents a collection of values, where each value may occur only once                                                                                                                              |
| [`Math`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Math)                             | Provides access to mathematical functions and constants                                                                                                                                              |
| [`Number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number)                         | Represents a numeric value                                                                                                                                                                           |
| [`Object`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object)                         | Represents the object that is the base of all JavaScript objects                                                                                                                                     |
| [`parseFloat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)                 | Parses a string argument and returns a floating point number                                                                                                                                         |
| [`parseInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseInt)                     | Parses a string argument and returns an integer of the specified radix                                                                                                                               |
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)                       | Represents the eventual completion (or failure) of an asynchronous operation, and its resulting value                                                                                                |
| [`Proxy`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Proxy)                           | Represents an object that is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc)                                     |
| [`queueMicrotask`](https://developer.mozilla.org/docs/Web/API/queueMicrotask)                                         | Queues a microtask to be executed                                                                                                                                                                    |
| [`RangeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RangeError)                 | Represents an error when a value is not in the set or range of allowed values                                                                                                                        |
| [`ReferenceError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)         | Represents an error when a non-existent variable is referenced                                                                                                                                       |
| [`Reflect`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Reflect)                       | Provides methods for interceptable JavaScript operations                                                                                                                                             |
| [`RegExp`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RegExp)                         | Represents a regular expression, allowing you to match combinations of characters                                                                                                                    |
| [`Set`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Set)                               | Represents a collection of values, where each value may occur only once                                                                                                                              |
| [`setInterval`](https://developer.mozilla.org/docs/Web/API/setInterval)                                               | Repeatedly calls a function, with a fixed time delay between each call                                                                                                                               |
| [`setTimeout`](https://developer.mozilla.org/docs/Web/API/setTimeout)                                                 | Calls a function or evaluates an expression after a specified number of milliseconds                                                                                                                 |
| [`SharedArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)   | Represents a generic, fixed-length raw binary data buffer                                                                                                                                            |
| [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String)                         | Represents a sequence of characters                                                                                                                                                                  |
| [`structuredClone`](https://developer.mozilla.org/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)            | Creates a deep copy of a value                                                                                                                                                                       |
| [`Symbol`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Symbol)                         | Represents a unique and immutable data type that is used as the key of an object property                                                                                                            |
| [`SyntaxError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)               | Represents an error when trying to interpret syntactically invalid code                                                                                                                              |
| [`TypeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/TypeError)                   | Represents an error when a value is not of the expected type                                                                                                                                         |
| [`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array)                 | Represents a typed array of 8-bit unsigned integers                                                                                                                                                  |
| [`Uint8ClampedArray`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray)   | Represents a typed array of 8-bit unsigned integers clamped to 0-255                                                                                                                                 |
| [`Uint32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array)               | Represents a typed array of 32-bit unsigned integers                                                                                                                                                 |
| [`URIError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/URIError)                     | Represents an error when a global URI handling function was used in a wrong way                                                                                                                      |
| [`URL`](https://developer.mozilla.org/docs/Web/API/URL)                                                               | Represents an object providing static methods used for creating object URLs                                                                                                                          |
| [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern)                                                 | Represents a URL pattern                                                                                                                                                                             |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams)                                       | Represents a collection of key/value pairs                                                                                                                                                           |
| [`WeakMap`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakMap)                       | Represents a collection of key/value pairs in which the keys are weakly referenced                                                                                                                   |
| [`WeakSet`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)                       | Represents a collection of objects in which each object may occur only once                                                                                                                          |
| [`WebAssembly`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly)               | Provides access to WebAssembly                                                                                                                                                                       |

### Next.js Specific Polyfills

* [`AsyncLocalStorage`](https://nodejs.org/api/async_context.html#class-asynclocalstorage)

### Environment Variables

You can use `process.env` to access [Environment Variables](/docs/app/guides/environment-variables.md) for both `next dev` and `next build`.

### Unsupported APIs

The Edge Runtime has some restrictions including:

* Native Node.js APIs **are not supported**. For example, you can't read or write to the filesystem.
* `node_modules` *can* be used, as long as they implement ES Modules and do not use native Node.js APIs.
* Calling `require` directly is **not allowed**. Use ES Modules instead.

The following JavaScript language features are disabled, and **will not work:**

| API                                                                                                                             | Description                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval)                                       | Evaluates JavaScript code represented as a string                   |
| [`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function)               | Creates a new function with the code provided as an argument        |
| [`WebAssembly.compile`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/compile)         | Compiles a WebAssembly module from a buffer source                  |
| [`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate) | Compiles and instantiates a WebAssembly module from a buffer source |

In rare cases, your code could contain (or import) some dynamic code evaluation statements which *can not be reached at runtime* and which can not be removed by treeshaking.
You can relax the check to allow specific files with your Proxy configuration:

```javascript filename="proxy.ts"
export const config = {
  unstable_allowDynamic: [
    // allows a single file
    '/lib/utilities.js',
    // use a glob to allow anything in the function-bind 3rd party module
    '**/node_modules/function-bind/**',
  ],
}
```

`unstable_allowDynamic` is a [glob](https://github.com/micromatch/micromatch#matching-features), or an array of globs, ignoring dynamic code evaluation for specific files. The globs are relative to your application root folder.

Be warned that if these statements are executed on the Edge, *they will throw and cause a runtime error*.


--------------------------------------------------------------------------------
title: "Turbopack"
description: "Turbopack is an incremental bundler optimized for JavaScript and TypeScript, written in Rust, and built into Next.js."
source: "https://nextjs.org/docs/app/api-reference/turbopack"
--------------------------------------------------------------------------------

# Turbopack

Turbopack is an **incremental bundler** optimized for JavaScript and TypeScript, written in Rust, and built into **Next.js**. You can use Turbopack with both the Pages and App Router for a **much faster** local development experience.

## Why Turbopack?

We built Turbopack to push the performance of Next.js, including:

* **Unified Graph:** Next.js supports multiple output environments (e.g., client and server). Managing multiple compilers and stitching bundles together can be tedious. Turbopack uses a **single, unified graph** for all environments.
* **Bundling vs Native ESM:** Some tools skip bundling in development and rely on the browser's native ESM. This works well for small apps but can slow down large apps due to excessive network requests. Turbopack **bundles** in dev, but in an optimized way to keep large apps fast.
* **Incremental Computation:** Turbopack parallelizes work across cores and **caches** results down to the function level. Once a piece of work is done, Turbopack won’t repeat it.
* **Lazy Bundling:** Turbopack only bundles what is actually requested by the dev server. This lazy approach can reduce initial compile times and memory usage.

## Getting started

Turbopack is now the **default bundler** in Next.js. No configuration is needed to use Turbopack:

```json filename="package.json" highlight={3}
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

### Using Webpack instead

If you need to use Webpack instead of Turbopack, you can opt-in with the `--webpack` flag:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack",
    "start": "next start"
  }
}
```

## Supported features

Turbopack in Next.js has **zero-configuration** for the common use cases. Below is a summary of what is supported out of the box, plus some references to how you can configure Turbopack further when needed.

### Language features

| Feature                     | Status        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JavaScript & TypeScript** | **Supported** | Uses SWC under the hood. Type-checking is not done by Turbopack (run `tsc --watch` or rely on your IDE for type checks).                                                                                                                                                                                                                                                                                                |
| **ECMAScript (ESNext)**     | **Supported** | Turbopack supports the latest ECMAScript features, matching SWC’s coverage.                                                                                                                                                                                                                                                                                                                                             |
| **CommonJS**                | **Supported** | `require()` syntax is handled out of the box.                                                                                                                                                                                                                                                                                                                                                                           |
| **ESM**                     | **Supported** | Static and dynamic `import` are fully supported.                                                                                                                                                                                                                                                                                                                                                                        |
| **Babel**                   | **Supported** | Starting in Next.js 16, Turbopack uses Babel automatically if it detects [a configuration file][babel-config]. Unlike in webpack, SWC is always used for Next.js's internal transforms and downleveling to older ECMAScript revisions. Next.js with webpack disables SWC if a Babel configuration file is present. Files in `node_modules` are excluded, unless you [manually configure `babel-loader`][manual-loader]. |

[babel-config]: https://babeljs.io/docs/config-files

[manual-loader]: /docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders

### Framework and React features

| Feature                           | Status        | Notes                                                                                                                  |
| --------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **JSX / TSX**                     | **Supported** | SWC handles JSX/TSX compilation.                                                                                       |
| **Fast Refresh**                  | **Supported** | No configuration needed.                                                                                               |
| **React Server Components (RSC)** | **Supported** | For the Next.js App Router. Turbopack ensures correct server/client bundling.                                          |
| **Root layout creation**          | Unsupported   | Automatic creation of a root layout in App Router is not supported. Turbopack will instruct you to create it manually. |

### CSS and styling

| Feature            | Status                  | Notes                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Global CSS**     | **Supported**           | Import `.css` files directly in your application.                                                                                                                                                                                                                                                                                                                     |
| **CSS Modules**    | **Supported**           | `.module.css` files work natively (Lightning CSS).                                                                                                                                                                                                                                                                                                                    |
| **CSS Nesting**    | **Supported**           | Lightning CSS supports [modern CSS nesting](https://lightningcss.dev/).                                                                                                                                                                                                                                                                                               |
| **@import syntax** | **Supported**           | Combine multiple CSS files.                                                                                                                                                                                                                                                                                                                                           |
| **PostCSS**        | **Supported**           | Automatically processes `postcss.config.js` in a Node.js worker pool. Useful for Tailwind, Autoprefixer, etc.                                                                                                                                                                                                                                                         |
| **Sass / SCSS**    | **Supported** (Next.js) | For Next.js, Sass is supported out of the box. Custom Sass functions (`sassOptions.functions`) are not supported because Turbopack's Rust-based architecture cannot directly execute JavaScript functions, unlike webpack's Node.js environment. Use webpack if you need this feature. In the future, Turbopack standalone usage will likely require a loader config. |
| **Less**           | Planned via plugins     | Not yet supported by default. Will likely require a loader config once custom loaders are stable.                                                                                                                                                                                                                                                                     |
| **Lightning CSS**  | **In Use**              | Handles CSS transformations. Some low-usage CSS Modules features (like `:local/:global` as standalone pseudo-classes) are not yet supported. [See below for more details.](#unsupported-and-unplanned-features)                                                                                                                                                       |

### Assets

| Feature                           | Status        | Notes                                                                                                                      |
| --------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Static Assets** (images, fonts) | **Supported** | Importing `import img from './img.png'` works out of the box. In Next.js, returns an object for the `<Image />` component. |
| **JSON Imports**                  | **Supported** | Named or default imports from `.json` are supported.                                                                       |

### Module resolution

| Feature               | Status              | Notes                                                                                                                                                           |
| --------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path Aliases**      | **Supported**       | Reads `tsconfig.json`'s `paths` and `baseUrl`, matching Next.js behavior.                                                                                       |
| **Manual Aliases**    | **Supported**       | [Configure `resolveAlias` in `next.config.js`](/docs/app/api-reference/config/next-config-js/turbopack.md#resolving-aliases) (similar to `webpack.resolve.alias`). |
| **Custom Extensions** | **Supported**       | [Configure `resolveExtensions` in `next.config.js`](/docs/app/api-reference/config/next-config-js/turbopack.md#resolving-custom-extensions).                       |
| **AMD**               | Partially Supported | Basic transforms work; advanced AMD usage is limited.                                                                                                           |

### Performance and Fast Refresh

| Feature                  | Status        | Notes                                                                                    |
| ------------------------ | ------------- | ---------------------------------------------------------------------------------------- |
| **Fast Refresh**         | **Supported** | Updates JavaScript, TypeScript, and CSS without a full refresh.                          |
| **Incremental Bundling** | **Supported** | Turbopack lazily builds only what’s requested by the dev server, speeding up large apps. |

## Known gaps with webpack

There are a number of non-trivial behavior differences between webpack and Turbopack that are important to be aware of when migrating an application. Generally, these are less of a concern for new applications.

### CSS Module Ordering

Turbopack will follow JS import order to order [CSS modules](/docs/app/getting-started/css.md#css-modules) which are not otherwise ordered. For example:

```jsx filename="components/BlogPost.jsx"
import utilStyles from './utils.module.css'
import buttonStyles from './button.module.css'
export default function BlogPost() {
  return (
    <div className={utilStyles.container}>
      <button className={buttonStyles.primary}>Click me</button>
    </div>
  )
}
```

In this example, Turbopack will ensure that `utils.module.css` will appear before `button.module.css` in the produced CSS chunk, following the import order

Webpack generally does this as well, but there are cases where it will ignore JS inferred ordering, for example if it infers the JS file is side-effect-free.

This can lead to subtle rendering changes when adopting Turbopack, if applications have come to rely on an arbitrary ordering. Generally, the solution is easy, e.g. have `button.module.css` `@import utils.module.css` to force the ordering, or identify the conflicting rules and change them to not target the same properties.

### Sass node\_modules imports

Turbopack supports importing `node_modules` Sass files out of the box. Webpack supports a legacy tilde `~` syntax for this, which is not supported by Turbopack.

From:

```scss filename="styles/globals.scss"
@import '~bootstrap/dist/css/bootstrap.min.css';
```

To:

```scss filename="styles/globals.scss"
@import 'bootstrap/dist/css/bootstrap.min.css';
```

If you can't update the imports, you can add a `turbopack.resolveAlias` configuration to map the `~` syntax to the actual path:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    resolveAlias: {
      '~*': '*',
    },
  },
}
```

### Bundle Sizes

From our testing on production applications, we observed that Turbopack generally produces bundles that are similar in size to Webpack. However, the comparison can be difficult since turbopack tends to produce fewer but larger chunks. Our advice is to focus on higher level metrics like [Core Web Vitals](https://web.dev/articles/vitals) or your own application level metrics to compare performance across the two bundlers. We are however aware of one gap that can occasionally cause a large regression.

Turbopack does not yet have an equivalent to the [Inner Graph Optimization](https://webpack.js.org/configuration/optimization/#optimizationinnergraph) in webpack which is enabled by default. This optimization is useful to tree shake large modules. For example:

```js filename=large.module.js
import heavy from 'some-heavy-dependency.js'

export function usesHeavy() {
  return heavy.run()
}

export const CONSTANT_VALUE = 3
```

If an application only uses `CONSTANT_VALUE` Turbopack will detect this and delete the `usesHeavy` export but not the corresponding `import`. However, with the Inner Graph Optimization, webpack can delete the `import` too which can drop the dependency as well.

We are planning to offer an equivalent to the Inner Graph Optimization in Turbopack but it is still under development. If you are affected by this gap, consider manually splitting modules.

### Build Caching

Webpack supports [disk build caching](https://webpack.js.org/configuration/cache/#cache) to improve build performance. Turbopack provides a similar opt-in feature, currently in beta. Starting with Next 16, you can enable Turbopack’s filesystem cache by setting the following experimental flags:

* [`experimental.turbopackFileSystemCacheForDev`](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache.md)
* [`experimental.turbopackFileSystemCacheForBuild`](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache.md)

> **Good to know:** For this reason, when comparing webpack and Turbopack performance, make sure to delete the `.next` folder between builds to see a fair comparison or enable the turbopack filesystem cache feature.

### Webpack plugins

Turbopack does not support webpack plugins. This affects third-party tools that rely on webpack's plugin system for integration. We do support [webpack loaders](/docs/app/api-reference/config/next-config-js/turbopack.md#configuring-webpack-loaders). If you depend on webpack plugins, you'll need to find Turbopack-compatible alternatives or continue using webpack until equivalent functionality is available.

## Unsupported and unplanned features

Some features are not yet implemented or not planned:

* **Legacy CSS Modules features**
  * Standalone `:local` and `:global` pseudo-classes (only the function variant `:global(...)` is supported).
  * The `@value` rule (superseded by CSS variables).
  * `:import` and `:export` ICSS rules.
  * `composes` in `.module.css` composing a `.css` file. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `composes` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
  * `@import` in CSS Modules importing `.css` as a CSS Module. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `@import` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
* **`sassOptions.functions`**
  Custom Sass functions defined in `sassOptions.functions` are not supported. This feature allows defining JavaScript functions that can be called from Sass code during compilation. Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through `sassOptions.functions`, unlike webpack's Node.js-based sass-loader which runs entirely in JavaScript. If you're using custom Sass functions, you'll need to use webpack instead of Turbopack.
* **`webpack()` configuration** in `next.config.js`
  Turbopack replaces webpack, so `webpack()` configs are not recognized. Use the [`turbopack` config](/docs/app/api-reference/config/next-config-js/turbopack.md) instead.
* **Yarn PnP**
  Not planned for Turbopack support in Next.js.
* **`experimental.urlImports`**
  Not planned for Turbopack.
* **`experimental.esmExternals`**
  Not planned. Turbopack does not support the legacy `esmExternals` configuration in Next.js.
* **Some Next.js Experimental Flags**
  * `experimental.nextScriptWorkers`
  * `experimental.sri.algorithm`
  * `experimental.fallbackNodePolyfills`
    We plan to implement these in the future.

For a full, detailed breakdown of each feature flag and its status, see the [Turbopack API Reference](/docs/app/api-reference/config/next-config-js/turbopack.md).

## Configuration

Turbopack can be configured via `next.config.js` (or `next.config.ts`) under the `turbopack` key. Configuration options include:

* **`rules`**
  Define additional [webpack loaders](/docs/app/api-reference/config/next-config-js/turbopack.md#configuring-webpack-loaders) for file transformations.
* **`resolveAlias`**
  Create manual aliases (like `resolve.alias` in webpack).
* **`resolveExtensions`**
  Change or extend file extensions for module resolution.

```js filename="next.config.js"
module.exports = {
  turbopack: {
    // Example: adding an alias and custom file extension
    resolveAlias: {
      underscore: 'lodash',
    },
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
  },
}
```

For more in-depth configuration examples, see the [Turbopack config documentation](/docs/app/api-reference/config/next-config-js/turbopack.md).

## Generating trace files for performance debugging

If you encounter performance or memory issues and want to help the Next.js team diagnose them, you can generate a trace file by appending `NEXT_TURBOPACK_TRACING=1` to your dev command:

```bash
NEXT_TURBOPACK_TRACING=1 next dev
```

This will produce a `.next/dev/trace-turbopack` file. Include that file when creating a GitHub issue on the [Next.js repo](https://github.com/vercel/next.js) to help us investigate.

By default the development server outputs to `.next/dev`. Read more about [isolatedDevBuild](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md).

## Summary

Turbopack is a **Rust-based**, **incremental** bundler designed to make local development and builds fast—especially for large applications. It is integrated into Next.js, offering zero-config CSS, React, and TypeScript support.

## Version Changes

| Version   | Changes                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| `v16.0.0` | Turbopack becomes the default bundler for Next.js. Automatic support for Babel when a configuration file is found. |
| `v15.5.0` | Turbopack support for `build` beta                                                                                 |
| `v15.3.0` | Experimental support for `build`                                                                                   |
| `v15.0.0` | Turbopack for `dev` stable                                                                                         |



--------------------------------------------------------------------------------
title: "Getting Started - Pages Router"
description: "Learn how to create full-stack web applications with Next.js with the Pages Router."
source: "https://nextjs.org/docs/pages/getting-started"
--------------------------------------------------------------------------------

# Getting Started

@router: Pages Router



 - [Installation](/docs/pages/getting-started/installation.md)
 - [Project Structure](/docs/pages/getting-started/project-structure.md)
 - [Images](/docs/pages/getting-started/images.md)
 - [Fonts](/docs/pages/getting-started/fonts.md)
 - [CSS](/docs/pages/getting-started/css.md)
 - [Deploying](/docs/pages/getting-started/deploying.md)

--------------------------------------------------------------------------------
title: "Installation"
description: "Learn how to create a new Next.js application with the `create-next-app` CLI, and set up TypeScript, ESLint, and Module Path Aliases."
source: "https://nextjs.org/docs/pages/getting-started/installation"
--------------------------------------------------------------------------------

# Installation

@router: Pages Router

## System requirements

Before you begin, make sure your development environment meets the following requirements:

* Minimum Node.js version: [20.9](https://nodejs.org/)
* Operating systems: macOS, Windows (including WSL), and Linux.

## Supported browsers

Next.js supports modern browsers with zero configuration.

* Chrome 111+
* Edge 111+
* Firefox 111+
* Safari 16.4+

Learn more about [browser support](/docs/architecture/supported-browsers.md), including how to configure polyfills and target specific browsers.

## Create with the CLI

The quickest way to create a new Next.js app is using [`create-next-app`](/docs/app/api-reference/cli/create-next-app.md), which sets up everything automatically for you. To create a project, run:

```bash filename="Terminal"
npx create-next-app@latest
```

On installation, you'll see the following prompts:

```txt filename="Terminal"
What is your project named? my-app
Would you like to use the recommended Next.js defaults?
    Yes, use recommended defaults - TypeScript, ESLint, Tailwind CSS, App Router, Turbopack
    No, reuse previous settings
    No, customize settings - Choose your own preferences
```

If you choose to `customize settings`, you'll see the following prompts:

```txt filename="Terminal"
Would you like to use TypeScript? No / Yes
Which linter would you like to use? ESLint / Biome / None
Would you like to use React Compiler? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
What import alias would you like configured? @/*
```

After the prompts, [`create-next-app`](/docs/app/api-reference/cli/create-next-app.md) will create a folder with your project name and install the required dependencies.

## Manual installation

To manually create a new Next.js app, install the required packages:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest
```

> **Good to know**: The App Router uses [React canary releases](https://react.dev/blog/2023/05/03/react-canaries) built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks. The Pages Router uses the React version you install in `package.json`.

Then, add the following scripts to your `package.json` file:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

These scripts refer to the different stages of developing an application:

* `next dev`: Starts the development server using Turbopack (default bundler).
* `next build`: Builds the application for production.
* `next start`: Starts the production server.
* `eslint`: Runs ESLint.

Turbopack is now the default bundler. To use Webpack run `next dev --webpack` or `next build --webpack`. See the [Turbopack docs](/docs/app/api-reference/turbopack.md) for configuration details.

### Create the `pages` directory

Next.js uses file-system routing, which means the routes in your application are determined by how you structure your files.

Create a `pages` directory at the root of your project. Then, add an `index.tsx` file inside your `pages` folder. This will be your home page (`/`):

```tsx filename="pages/index.tsx" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

```jsx filename="pages/index.js" switcher
export default function Page() {
  return <h1>Hello, Next.js!</h1>
}
```

Next, add an `_app.tsx` file inside `pages/` to define the global layout. Learn more about the [custom App file](/docs/pages/building-your-application/routing/custom-app.md).

```tsx filename="pages/_app.tsx" switcher
import type { AppProps } from 'next/app'

export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

```jsx filename="pages/_app.js" switcher
export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Finally, add a `_document.tsx` file inside `pages/` to control the initial response from the server. Learn more about the [custom Document file](/docs/pages/building-your-application/routing/custom-document.md).

```tsx filename="pages/_document.tsx" switcher
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

```jsx filename="pages/_document.js" switcher
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

### Create the `public` folder (optional)

Create a [`public` folder](/docs/app/api-reference/file-conventions/public-folder.md) at the root of your project to store static assets such as images, fonts, etc. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

You can then reference these assets using the root path (`/`). For example, `public/profile.png` can be referenced as `/profile.png`:

```tsx filename="app/page.tsx" highlight={4} switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

```jsx filename="app/page.js" highlight={4} switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="/profile.png" alt="Profile" width={100} height={100} />
}
```

## Run the development server

1. Run `npm run dev` to start the development server.
2. Visit `http://localhost:3000` to view your application.
3. Edit the `pages/index.tsx` file and save it to see the updated result in your browser.

## Set up TypeScript

> Minimum TypeScript version: `v5.1.0`

Next.js comes with built-in TypeScript support. To add TypeScript to your project, rename a file to `.ts` / `.tsx` and run `next dev`. Next.js will automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

See the [TypeScript reference](/docs/app/api-reference/config/next-config-js/typescript.md) page for more information.

## Set up linting

Next.js supports linting with either ESLint or Biome. Choose a linter and run it directly via `package.json` scripts.

* Use **ESLint** (comprehensive rules):

```json filename="package.json"
{
  "scripts": {
    "lint": "eslint",
    "lint:fix": "eslint --fix"
  }
}
```

* Or use **Biome** (fast linter + formatter):

```json filename="package.json"
{
  "scripts": {
    "lint": "biome check",
    "format": "biome format --write"
  }
}
```

If your project previously used `next lint`, migrate your scripts to the ESLint CLI with the codemod:

```bash filename="Terminal"
npx @next/codemod@canary next-lint-to-eslint-cli .
```

If you use ESLint, create an explicit config (recommended `eslint.config.mjs`). ESLint supports both [the legacy `.eslintrc.*` and the newer `eslint.config.mjs` formats](https://eslint.org/docs/latest/use/configure/configuration-files#configuring-eslint). See the [ESLint API reference](/docs/app/api-reference/config/eslint.md#with-core-web-vitals) for a recommended setup.

> **Good to know**: Starting with Next.js 16, `next build` no longer runs the linter automatically. Instead, you can run your linter through NPM scripts.

See the [ESLint Plugin](/docs/app/api-reference/config/eslint.md) page for more information.

## Set up Absolute Imports and Module Path Aliases

Next.js has in-built support for the `"paths"` and `"baseUrl"` options of `tsconfig.json` and `jsconfig.json` files.

These options allow you to alias project directories to absolute paths, making it easier and cleaner to import modules. For example:

```jsx
// Before
import { Button } from '../../../components/button'

// After
import { Button } from '@/components/button'
```

To configure absolute imports, add the `baseUrl` configuration option to your `tsconfig.json` or `jsconfig.json` file. For example:

```json filename="tsconfig.json or jsconfig.json"
{
  "compilerOptions": {
    "baseUrl": "src/"
  }
}
```

In addition to configuring the `baseUrl` path, you can use the `"paths"` option to `"alias"` module paths.

For example, the following configuration maps `@/components/*` to `components/*`:

```json filename="tsconfig.json or jsconfig.json"
{
  "compilerOptions": {
    "baseUrl": "src/",
    "paths": {
      "@/styles/*": ["styles/*"],
      "@/components/*": ["components/*"]
    }
  }
}
```

Each of the `"paths"` are relative to the `baseUrl` location.


--------------------------------------------------------------------------------
title: "Project structure and organization"
description: "Learn the folder and file conventions in Next.js, and how to organize your project."
source: "https://nextjs.org/docs/pages/getting-started/project-structure"
--------------------------------------------------------------------------------

# Project Structure

@router: Pages Router

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

## Folder and file conventions

### Top-level folders

Top-level folders are used to organize your application's code and static assets.

![Route segments to path segments](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/top-level-folders.png)

|                                                                    |                                    |
| ------------------------------------------------------------------ | ---------------------------------- |
| [`app`](/docs/app.md)                                                 | App Router                         |
| [`pages`](/docs/pages/building-your-application/routing.md)           | Pages Router                       |
| [`public`](/docs/app/api-reference/file-conventions/public-folder.md) | Static assets to be served         |
| [`src`](/docs/app/api-reference/file-conventions/src-folder.md)       | Optional application source folder |

### Top-level files

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

|                                                                              |                                         |
| ---------------------------------------------------------------------------- | --------------------------------------- |
| **Next.js**                                                                  |                                         |
| [`next.config.js`](/docs/app/api-reference/config/next-config-js.md)            | Configuration file for Next.js          |
| [`package.json`](/docs/app/getting-started/installation.md#manual-installation) | Project dependencies and scripts        |
| [`instrumentation.ts`](/docs/app/guides/instrumentation.md)                     | OpenTelemetry and Instrumentation file  |
| [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy.md)                 | Next.js request proxy                   |
| [`.env`](/docs/app/guides/environment-variables.md)                             | Environment variables                   |
| [`.env.local`](/docs/app/guides/environment-variables.md)                       | Local environment variables             |
| [`.env.production`](/docs/app/guides/environment-variables.md)                  | Production environment variables        |
| [`.env.development`](/docs/app/guides/environment-variables.md)                 | Development environment variables       |
| [`eslint.config.mjs`](/docs/app/api-reference/config/eslint.md)                 | Configuration file for ESLint           |
| `.gitignore`                                                                 | Git files and folders to ignore         |
| `next-env.d.ts`                                                              | TypeScript declaration file for Next.js |
| `tsconfig.json`                                                              | Configuration file for TypeScript       |
| `jsconfig.json`                                                              | Configuration file for JavaScript       |

### File conventions

|                                                                                                             |                     |                   |
| ----------------------------------------------------------------------------------------------------------- | ------------------- | ----------------- |
| [`_app`](/docs/pages/building-your-application/routing/custom-app.md)                                          | `.js` `.jsx` `.tsx` | Custom App        |
| [`_document`](/docs/pages/building-your-application/routing/custom-document.md)                                | `.js` `.jsx` `.tsx` | Custom Document   |
| [`_error`](/docs/pages/building-your-application/routing/custom-error.md#more-advanced-error-page-customizing) | `.js` `.jsx` `.tsx` | Custom Error Page |
| [`404`](/docs/pages/building-your-application/routing/custom-error.md#404-page)                                | `.js` `.jsx` `.tsx` | 404 Error Page    |
| [`500`](/docs/pages/building-your-application/routing/custom-error.md#500-page)                                | `.js` `.jsx` `.tsx` | 500 Error Page    |

### Routes

|                                                                                                |                     |             |
| ---------------------------------------------------------------------------------------------- | ------------------- | ----------- |
| **Folder convention**                                                                          |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`folder/index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes) | `.js` `.jsx` `.tsx` | Nested page |
| **File convention**                                                                            |                     |             |
| [`index`](/docs/pages/building-your-application/routing/pages-and-layouts.md#index-routes)        | `.js` `.jsx` `.tsx` | Home page   |
| [`file`](/docs/pages/building-your-application/routing/pages-and-layouts.md)                      | `.js` `.jsx` `.tsx` | Nested page |

### Dynamic routes

|                                                                                                                   |                     |                                  |
| ----------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------- |
| **Folder convention**                                                                                             |                     |                                  |
| [`[folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md)                                  | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...folder]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md#catch-all-segments)            | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...folder]]/index`](/docs/pages/building-your-application/routing/dynamic-routes.md#optional-catch-all-segments) | `.js` `.jsx` `.tsx` | Optional catch-all route segment |
| **File convention**                                                                                               |                     |                                  |
| [`[file]`](/docs/pages/building-your-application/routing/dynamic-routes.md)                                          | `.js` `.jsx` `.tsx` | Dynamic route segment            |
| [`[...file]`](/docs/pages/building-your-application/routing/dynamic-routes.md#catch-all-segments)                    | `.js` `.jsx` `.tsx` | Catch-all route segment          |
| [`[[...file]]`](/docs/pages/building-your-application/routing/dynamic-routes.md#optional-catch-all-segments)         | `.js` `.jsx` `.tsx` | Optional catch-all route segment |


--------------------------------------------------------------------------------
title: "Image Optimization"
description: "Learn how to optimize images in Next.js"
source: "https://nextjs.org/docs/pages/getting-started/images"
--------------------------------------------------------------------------------

# Images

@router: Pages Router

The Next.js [`<Image>`](/docs/app/api-reference/components/image.md) component extends the HTML `<img>` element to provide:

* **Size optimization:** Automatically serving correctly sized images for each device, using modern image formats like WebP.
* **Visual stability:** Preventing [layout shift](https://web.dev/articles/cls) automatically when images are loading.
* **Faster page loads:** Only loading images when they enter the viewport using native browser lazy loading, with optional blur-up placeholders.
* **Asset flexibility:** Resizing images on-demand, even images stored on remote servers.

To start using `<Image>`, import it from `next/image` and render it within your component.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="" alt="" />
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return <Image src="" alt="" />
}
```

The `src` property can be a [local](#local-images) or [remote](#remote-images) image.

> **🎥 Watch:** Learn more about how to use `next/image` → [YouTube (9 minutes)](https://youtu.be/IU_qq_c_lKA).

## Local images

You can store static files, like images and fonts, under a folder called [`public`](/docs/app/api-reference/file-conventions/public-folder.md) in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

![Folder structure showing app and public folders](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/public-folder.png)

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

If the image is statically imported, Next.js will automatically determine the intrinsic [`width`](/docs/app/api-reference/components/image.md#width-and-height) and [`height`](/docs/app/api-reference/components/image.md#width-and-height). These values are used to determine the image ratio and prevent [Cumulative Layout Shift](https://web.dev/articles/cls) while your image is loading.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'
import ProfileImage from './profile.png'

export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'
import ProfileImage from './profile.png'

export default function Page() {
  return (
    <Image
      src={ProfileImage}
      alt="Picture of the author"
      // width={500} automatically provided
      // height={500} automatically provided
      // blurDataURL="data:..." automatically provided
      // placeholder="blur" // Optional blur-up while loading
    />
  )
}
```

## Remote images

To use a remote image, you can provide a URL string for the `src` property.

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](/docs/app/api-reference/components/image.md#width-and-height), [`height`](/docs/app/api-reference/components/image.md#width-and-height) and optional [`blurDataURL`](/docs/app/api-reference/components/image.md#blurdataurl) props manually. The `width` and `height` are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. Alternatively, you can use the [`fill` property](/docs/app/api-reference/components/image.md#fill) to make the image fill the size of the parent element.

To safely allow images from remote servers, you need to define a list of supported URL patterns in [`next.config.js`](/docs/app/api-reference/config/next-config-js.md). Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
        search: '',
      },
    ],
  },
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
        search: '',
      },
    ],
  },
}
```
## API Reference

See the API Reference for the full feature set of Next.js Image.

- [Image Component](/docs/app/api-reference/components/image.md)
  - Optimize Images in your Next.js Application using the built-in `next/image` Component.


--------------------------------------------------------------------------------
title: "Font Optimization"
description: "Learn how to optimize fonts in Next.js"
source: "https://nextjs.org/docs/pages/getting-started/fonts"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./10-usesearchparams.md) | [Index](./index.md) | [Next →](./12-fonts.md)
