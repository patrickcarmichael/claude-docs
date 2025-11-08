---
title: "Astro Adapter API"
section: 222
---

# Astro Adapter API

Astro is designed to make it easy to deploy to any cloud provider for on-demand rendering, also known as server-side rendering (SSR). This ability is provided by **adapters**, which are [integrations](/en/reference/integrations-reference/). See the [on-demand rendering guide](/en/guides/on-demand-rendering/) to learn how to use an existing adapter.

## What is an adapter?

[Section titled “What is an adapter?”](#what-is-an-adapter)

An adapter is a special kind of [integration](/en/reference/integrations-reference/) that provides an entrypoint for server rendering at request time. An adapter does two things:

* Implements host-specific APIs for handling requests.
* Configures the build according to host conventions.

## Building an Adapter

[Section titled “Building an Adapter”](#building-an-adapter)

An adapter is an [integration](/en/reference/integrations-reference/) and can do anything that an integration can do.

An adapter **must** call the `setAdapter` API in the `astro:config:done` hook like so:

my-adapter.mjs

```js
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
              staticOutput: 'stable'
          }
        });
      },
    },
  };
}
```jsx
The object passed into `setAdapter` is defined as:

```ts
interface AstroAdapter {
  name: string;
  serverEntrypoint?: string;
  previewEntrypoint?: string;
  exports?: string[];
  args?: any;
  adapterFeatures?: AstroAdapterFeatures;
  supportedAstroFeatures: AstroAdapterFeatureMap;
  client?: {
    /**
     * Headers to inject into Astro's internal fetch calls (Actions, View Transitions, Server Islands, Prefetch).
     * Can be an object of headers or a function that returns headers.
     */
    internalFetchHeaders?: Record<string, string> | (() => Record<string, string>);
    /**
     * Query parameters to append to all asset URLs (images, stylesheets, scripts, etc.).
     * Useful for adapters that need to track deployment versions or other metadata.
     */
    assetQueryParams?: URLSearchParams;
  };
}


export interface AstroAdapterFeatures {
  /**
   * Creates an edge function that will communicate with the Astro middleware.
   */
  edgeMiddleware: boolean;
  /**
   * Determine the type of build output the adapter is intended for. Defaults to `server`;
   */
  buildOutput?: 'static' | 'server';
}


export type AdapterSupportsKind = 'unsupported' | 'stable' | 'experimental' | 'deprecated' | 'limited';


export type AdapterSupportWithMessage = {
  support: Exclude<AdapterSupportsKind, 'stable'>;
  message: string;
  suppress?: 'default' | 'all';
};


export type AdapterSupport = AdapterSupportsKind | AdapterSupportWithMessage;


export type AstroAdapterFeatureMap = {
  /**
   * The adapter is able to serve static pages
   */
  staticOutput?: AdapterSupport;
  /**
   * The adapter is able to serve pages that are static or rendered via server
   */
  hybridOutput?: AdapterSupport;
  /**
   * The adapter is able to serve pages rendered on demand
   */
  serverOutput?: AdapterSupport;
  /**
   * The adapter is able to support i18n domains
   */
  i18nDomains?: AdapterSupport;
  /**
   * The adapter is able to support `getSecret` exported from `astro:env/server`
   */
  envGetSecret?: AdapterSupport;
  /**
   * The adapter supports the Sharp image service
   */
  sharpImageService?: AdapterSupport;
};
```jsx
The properties are:

* **name**: A unique name for your adapter, used for logging.
* **serverEntrypoint**: The entrypoint for on-demand server rendering.
* **exports**: An array of named exports when used in conjunction with `createExports` (explained below).
* **adapterFeatures**: An object that enables specific features that must be supported by the adapter. These features will change the built output, and the adapter must implement the proper logic to handle the different output.
* **supportedAstroFeatures**: A map of Astro built-in features. This allows Astro to determine which features an adapter is unable or unwilling to support so appropriate error messages can be provided.

### Server Entrypoint

[Section titled “Server Entrypoint”](#server-entrypoint)

Astro’s adapter API attempts to work with any type of host, and gives a flexible way to conform to the host APIs.

#### Exports

[Section titled “Exports”](#exports)

Some serverless hosts expect you to export a function, such as `handler`:

```js
export function handler(event, context) {
  // ...
}
```jsx
With the adapter API you achieve this by implementing `createExports` in your `serverEntrypoint`:

```js
import { App } from 'astro/app';


export function createExports(manifest) {
  const app = new App(manifest);


  const handler = (event, context) => {
    // ...
  };


  return { handler };
}
```jsx
And then in your integration, where you call `setAdapter`, provide this name in `exports`:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          exports: ['handler'],
        });
      },
    },
  };
}
```jsx
#### Start

[Section titled “Start”](#start)

Some hosts expect you to *start* the server yourselves, for example by listening to a port. For these types of hosts, the adapter API allows you to export a `start` function which will be called when the bundle script is run.

```js
import { App } from 'astro/app';


export function start(manifest) {
  const app = new App(manifest);


  addEventListener('fetch', event => {
    // ...
  });
}
```jsx
#### `astro/app`

[Section titled “astro/app”](#astroapp)

This module is used for rendering pages that have been prebuilt through `astro build`. Astro uses the standard [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) objects. Hosts that have a different API for request/response should convert to these types in their adapter.

```js
import { App } from 'astro/app';
import http from 'http';


export function start(manifest) {
  const app = new App(manifest);


  addEventListener('fetch', event => {
    event.respondWith(
      app.render(event.request)
    );
  });
}
```jsx
The following methods are provided:

##### `app.render()`

[Section titled “app.render()”](#apprender)

**Type:** `(request: Request, options?: RenderOptions) => Promise<Response>`

This method calls the Astro page that matches the request, renders it, and returns a Promise to a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object. This also works for API routes that do not render pages.

```js
const response = await app.render(request);
```jsx
##### `RenderOptions`

[Section titled “RenderOptions”](#renderoptions)

**Type:** `{addCookieHeader?: boolean; clientAddress?: string; locals?: object; prerenderedErrorPageFetch?: (url: ErrorPagePath) => Promise<Response>; routeData?: RouteData;}`

The `app.render()` method accepts a mandatory `request` argument, and an optional `RenderOptions` object for [`addCookieHeader`](#addcookieheader), [`clientAddress`](#clientaddress), [`locals`](#locals), [`prerenderedErrorPageFetch`](#prerenderederrorpagefetch), and [`routeData`](#routedata).

###### `addCookieHeader`

[Section titled “addCookieHeader”](#addcookieheader)

**Type:** `boolean`\
**Default:** `false`

Whether or not to automatically add all cookies written by `Astro.cookie.set()` to the response headers.

When set to `true`, they will be added to the `Set-Cookie` header of the response as comma separated key-value pairs. You can use the standard `response.headers.getSetCookie()` API to read them individually. When set to `false`(default), the cookies will only be available from `App.getSetCookieFromResponse(response)`.

```js
const response = await app.render(request, { addCookieHeader: true });
```jsx
###### `clientAddress`

[Section titled “clientAddress”](#clientaddress)

**Type:** `string`\
**Default:** `request[Symbol.for("astro.clientAddress")]`

The client IP address that will be made available as [`Astro.clientAddress`](/en/reference/api-reference/#clientaddress) in pages, and as `ctx.clientAddress` in API routes and middleware.

The example below reads the `x-forwarded-for` header and passes it as `clientAddress`. This value becomes available to the user as `Astro.clientAddress`.

```js
const clientAddress = request.headers.get("x-forwarded-for");
const response = await app.render(request, { clientAddress });
```jsx
###### `locals`

[Section titled “locals”](#locals)

**Type:** `object`

The [`context.locals` object](/en/reference/api-reference/#locals) used to store and access information during the lifecycle of a request.

The example below reads a header named `x-private-header`, attempts to parse it as an object and pass it to `locals`, which can then be passed to any [middleware function](/en/guides/middleware/).

```js
const privateHeader = request.headers.get("x-private-header");
let locals = {};
try {
    if (privateHeader) {
        locals = JSON.parse(privateHeader);
    }
} finally {
    const response = await app.render(request, { locals });
}
```jsx
###### `prerenderedErrorPageFetch`

[Section titled “prerenderedErrorPageFetch”](#prerenderederrorpagefetch)

**Type:** `(url: ErrorPagePath) => Promise<Response>`\
**Default:** `fetch`

**Added in:** `astro@5.6.0`

A function that allows you to provide custom implementations for fetching prerendered error pages.

This is used to override the default `fetch()` behavior, for example, when `fetch()` is unavailable or when you cannot call the server from itself.

The following example reads `500.html` and `404.html` from disk instead of performing an HTTP call:

```js
return app.render(request, {
  prerenderedErrorPageFetch: async (url: string): Promise<Response> => {
    if (url.includes("/500")) {
        const content = await fs.promises.readFile("500.html", "utf-8");
        return new Response(content, {
          status: 500,
          headers: { "Content-Type": "text/html" },
        });
    }


    const content = await fs.promises.readFile("404.html", "utf-8");
      return new Response(content, {
        status: 404,
        headers: { "Content-Type": "text/html" },
      });
});
```jsx
If not provided, Astro will fallback to its default behavior for fetching error pages.

###### `routeData`

[Section titled “routeData”](#routedata)

**Type:** `RouteData`\
**Default:** `app.match(request)`

Provide a value for [`integrationRouteData`](/en/reference/integrations-reference/#integrationroutedata-type-reference) if you already know the route to render. Doing so will bypass the internal call to [`app.match`](#appmatch) to determine the route to render.

```js
const routeData = app.match(request);
if (routeData) {
    return app.render(request, { routeData });
} else {
    /* adapter-specific 404 response */
    return new Response(..., { status: 404 });
}
```jsx
##### `app.match()`

[Section titled “app.match()”](#appmatch)

**Type:** `(request: Request) => RouteData | undefined`

This method is used to determine if a request is matched by the Astro app’s routing rules.

```js
if(app.match(request)) {
  const response = await app.render(request);
}
```jsx
You can usually call `app.render(request)` without using `.match` because Astro handles 404s if you provide a `404.astro` file. Use `app.match(request)` if you want to handle 404s in a different way.

## Allow installation via `astro add`

[Section titled “Allow installation via astro add”](#allow-installation-via-astro-add)

[The `astro add` command](/en/reference/cli-reference/#astro-add) allows users to easily add integrations and adapters to their project. If you want *your* adapter to be installable with this tool, **add `astro-adapter` to the `keywords` field in your `package.json`**:

```json
{
  "name": "example",
  "keywords": ["astro-adapter"],
}
```jsx
Once you [publish your adapter to npm](https://docs.npmjs.com/cli/v8/commands/npm-publish), running `astro add example` will install your package with any peer dependencies specified in your `package.json`. We will also instruct users to update their project config manually.

## Astro features

[Section titled “Astro features”](#astro-features)

**Added in:** `astro@3.0.0`

Astro features are a way for an adapter to tell Astro whether they are able to support a feature, and also the adapter’s level of support.

When using these properties, Astro will:

* run specific validation;
* emit contextual information to the logs;

These operations are run based on the features supported or not supported, their level of support, the [desired amount of logging](#suppress), and the user’s own configuration.

The following configuration tells Astro that this adapter has experimental support for the Sharp-powered built-in image service:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          supportedAstroFeatures: {
+            sharpImageService: 'experimental'
+          }
        });
      },
    },
  };
}
```jsx
If the Sharp image service is used, Astro will log a warning and error to the terminal based on your adapter’s support:

```plaintext
[@example/my-adapter] The feature is experimental and subject to issues or changes.


[@example/my-adapter] The currently selected adapter `@example/my-adapter` is not compatible with the service "Sharp". Your project will NOT be able to build.
```jsx
A message can additionally be provided to give more context to the user:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          supportedAstroFeatures: {
+            sharpImageService: {
+              support: 'limited',
+              message: 'This adapter has limited support for Sharp. Certain features may not work as expected.'
+            }
+          }
        });
      },
    },
  };
}
```jsx
### `suppress`

[Section titled “suppress”](#suppress)

**Type:** `'default' | 'all'`

**Added in:** `astro@5.9.0`

An option to prevent showing some or all logged messages about an adapter’s support for a feature.

If Astro’s default log message is redundant, or confusing to the user in combination with your custom `message`, you can use `suppress: "default"` to suppress the default message and only log your message:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
            sharpImageService: {
              support: 'limited',
              message: 'The adapter has limited support for Sharp. It will be used for images during build time, but will not work at runtime.',
+              suppress: 'default' // custom message is more detailed than the default
            }
          }
        });
      },
    },
  };
}
```jsx
You can also use `suppress: "all"` to suppress all messages about support for the feature. This is useful when these messages are unhelpful to users in a specific context, such as when they have a configuration setting that means they are not using that feature. For example, you can choose to prevent logging any messages about Sharp support from your adapter:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          supportedAstroFeatures: {
            sharpImageService: {
              support: 'limited',
              message: 'This adapter has limited support for Sharp. Certain features may not work as expected.',
+              suppress: 'all'
            }
          }
        });
      },
    },
  };
}
```jsx
## Adapter features

[Section titled “Adapter features”](#adapter-features)

A set of features that changes the output of the emitted files. When an adapter opts in to these features, they will get additional information inside specific hooks.

### `edgeMiddleware`

[Section titled “edgeMiddleware”](#edgemiddleware)

**Type:** `boolean`

Defines whether any on-demand rendering middleware code will be bundled when built.

When enabled, this prevents middleware code from being bundled and imported by all pages during the build:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+              edgeMiddleware: true
+          }
        });
      },
    },
  };
}
```jsx
Then, consume the hook [`astro:build:ssr`](/en/reference/integrations-reference/#astrobuildssr), which will give you a `middlewareEntryPoint`, an `URL` to the physical file on the file system.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
          adapterFeatures: {
              edgeMiddleware: true
          }
        });
      },


      +'astro:build:ssr': ({ middlewareEntryPoint }) => {
          +// remember to check if this property exits, it will be `undefined` if the adapter doesn't opt in to the feature
          +if (middlewareEntryPoint) {
             +createEdgeMiddleware(middlewareEntryPoint)
+          }
+      }
    },
  };
}


function createEdgeMiddleware(middlewareEntryPoint) {
    // emit a new physical file using your bundler
}
```jsx
### envGetSecret

[Section titled “envGetSecret”](#envgetsecret)

**Type:** `AdapterSupportsKind`

This is a feature to allow your adapter to retrieve secrets configured by users in `env.schema`.

Enable the feature by passing any valid `AdapterSupportsKind` value to the adapter:

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+              envGetSecret: 'stable'
+          }
        });
      },
    },
  };
}
```jsx
The `astro/env/setup` module allows you to provide an implementation for `getSecret()`. In your server entrypoint, call `setGetEnv()` as soon as possible:

```diff
import { App } from 'astro/app';
+import { setGetEnv } from "astro/env/setup"


+setGetEnv((key) => process.env[key])


export function createExports(manifest) {
  const app = new App(manifest);


  const handler = (event, context) => {
    // ...
  };


  return { handler };
}
```jsx
If you support secrets, be sure to call `setGetEnv()` before `getSecret()` when your environment variables are tied to the request:

```diff
import type { SSRManifest } from 'astro';
import { App } from 'astro/app';
+import { setGetEnv } from 'astro/env/setup';
import { createGetEnv } from '../utils/env.js';


type Env = {
  [key: string]: unknown;
};


export function createExports(manifest: SSRManifest) {
  const app = new App(manifest);


  const fetch = async (request: Request, env: Env) => {
    +setGetEnv(createGetEnv(env));


    const response = await app.render(request);


    return response;
  };


  return { default: { fetch } };
}
```jsx
### buildOutput

[Section titled “buildOutput”](#buildoutput)

**Type:** `'static' | 'server'`

**Added in:** `astro@5.0.0`

This property allows you to force a specific output shape for the build. This can be useful for adapters that only work with a specific output type, for instance, your adapter might expect a static website, but uses an adapter to create host-specific files. Defaults to `server` if not specified.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+            buildOutput: 'static'
+          }
        });
      },
    },
  };
}
```jsx
### experimentalStaticHeaders

[Section titled “experimentalStaticHeaders”](#experimentalstaticheaders)

**Type:** `true | false`

**Added in:** `astro@5.9.3`

When this feature is enabled, Astro will return a map of the `Headers` emitted by the static pages. This map `experimentalRouteToHeaders` is available in the `astro:build:generated` hook.

The value of the headers might change based on the features enabled/used by the application.

For example, if CSP enabled, the `<meta http-equiv="content-security-policy">` element is not added to the static page. Instead its `content` is available in the `experimentalRouteToHeaders` map.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@example/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@example/my-adapter',
          serverEntrypoint: '@example/my-adapter/server.js',
+          adapterFeatures: {
+            experimentalStaticHeaders: true,
+          },
        });
      },
      'astro:build:generated': ({ experimentalRouteToHeaders }) => {
        // use `experimentalRouteToHeaders` to generate a configuration file
        // for your virtual host of choice
      },
    },
  };
}
```

---

[← Previous](221-style-rendered-markdown-with-tailwind-typography.md) | [Index](index.md) | [Next →](index.md)
