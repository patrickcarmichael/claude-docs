**Navigation:** [← Previous](./13-invalid-entry-inside-getstaticpaths-return-value.md) | [Index](./index.md) | [Next →](./15-build-your-first-astro-blog.md)

---

# Astro Integration API

**Astro Integrations** add new functionality and behaviors for your project with only a few lines of code.

This reference page is for anyone writing their own integration. To learn how to use an integration in your project, check out our [Using Integrations](/en/guides/integrations-guide/) guide instead.

## Examples

[Section titled “Examples”](#examples)

The official Astro integrations can act as reference for you as you go to build your own integrations.

* **Renderers:** [`svelte`](/en/guides/integrations-guide/svelte/), [`react`](/en/guides/integrations-guide/react/), [`preact`](/en/guides/integrations-guide/preact/), [`vue`](/en/guides/integrations-guide/vue/), [`solid`](/en/guides/integrations-guide/solid-js/)
* **Libraries:** [`partytown`](/en/guides/integrations-guide/partytown/)
* **Features:** [`sitemap`](/en/guides/integrations-guide/sitemap/)

## Quick API Reference

[Section titled “Quick API Reference”](#quick-api-reference)

```ts
interface AstroIntegration {
  name: string;
  hooks: {
    'astro:config:setup'?: (options: {
      config: AstroConfig;
      command: 'dev' | 'build' | 'preview' | 'sync';
      isRestart: boolean;
      updateConfig: (newConfig: DeepPartial<AstroConfig>) => AstroConfig;
      addRenderer: (renderer: AstroRenderer) => void;
      addWatchFile: (path: URL | string) => void;
      addClientDirective: (directive: ClientDirectiveConfig) => void;
      addMiddleware: (middleware: AstroIntegrationMiddleware) => void;
      addDevToolbarApp: (entrypoint: DevToolbarAppEntry) => void;
      injectScript: (stage: InjectedScriptStage, content: string) => void;
      injectRoute: (injectedRoute: InjectedRoute) => void;
      createCodegenDir: () => URL;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:route:setup'?: (options: {
      route: RouteOptions;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:routes:resolved'?: (options: {
      routes: IntegrationResolvedRoute[];
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:config:done'?: (options: {
      config: AstroConfig;
      setAdapter: (adapter: AstroAdapter) => void;
      injectTypes: (injectedType: InjectedType) => URL;
      logger: AstroIntegrationLogger;
      buildOutput: 'static' | 'server';
    }) => void | Promise<void>;
    'astro:server:setup'?: (options: {
      server: vite.ViteDevServer;
      logger: AstroIntegrationLogger;
      toolbar: ReturnType<typeof getToolbarServerCommunicationHelpers>;
      refreshContent?: (options: RefreshContentOptions) => Promise<void>;
    }) => void | Promise<void>;
    'astro:server:start'?: (options: {
      address: AddressInfo;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:server:done'?: (options: {
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:build:start'?: (options: {
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:build:setup'?: (options: {
      vite: vite.InlineConfig;
      pages: Map<string, PageBuildData>;
      target: 'client' | 'server';
      updateConfig: (newConfig: vite.InlineConfig) => void;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:build:ssr'?: (options: {
      manifest: SerializedSSRManifest;
      entryPoints: Map<IntegrationRouteData, URL>;
      middlewareEntryPoint: URL | undefined;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:build:generated'?: (options: {
      dir: URL;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;
    'astro:build:done'?: (options: {
      pages: { pathname: string }[];
      dir: URL;
      assets: Map<string, URL[]>;
      logger: AstroIntegrationLogger;
    }) => void | Promise<void>;


    // ... any custom hooks from integrations
  };
}
```

## Hooks

[Section titled “Hooks”](#hooks)

Astro provides hooks that integrations can implement to execute during certain parts of Astro’s lifecycle. Astro hooks are defined in the `IntegrationHooks` interface, which is part of the global `Astro` namespace. Each hook has a [`logger` option](#astrointegrationlogger) that allows you to use the Astro logger to write logs.

The following hooks are built in to Astro:

### `astro:config:setup`

[Section titled “astro:config:setup”](#astroconfigsetup)

**Next hook:** [`astro:route:setup`](#astroroutesetup)

**When:** On initialization, before either the [Vite](https://vite.dev/config/) or [Astro config](/en/reference/configuration-reference/) have resolved.

**Why:** To extend the project config. This includes updating the [Astro config](/en/reference/configuration-reference/), applying [Vite plugins](https://vite.dev/guide/api-plugin.html), adding component renderers, and injecting scripts onto the page.

```ts
'astro:config:setup'?: (options: {
  config: AstroConfig;
  command: 'dev' | 'build' | 'preview' | 'sync';
  isRestart: boolean;
  updateConfig: (newConfig: DeepPartial<AstroConfig>) => AstroConfig;
  addRenderer: (renderer: AstroRenderer) => void;
  addClientDirective: (directive: ClientDirectiveConfig) => void;
  addMiddleware: (middleware: AstroIntegrationMiddleware) => void;
  addDevToolbarApp: (entrypoint: DevToolbarAppEntry) => void;
  addWatchFile: (path: URL | string) => void;
  injectScript: (stage: InjectedScriptStage, content: string) => void;
  injectRoute: (injectedRoute: InjectedRoute) => void;
  createCodegenDir: () => URL;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `config` option

[Section titled “config option”](#config-option)

**Type:** `AstroConfig`

A read-only copy of the user-supplied [Astro config](/en/reference/configuration-reference/). This is resolved *before* any other integrations have run. If you need a copy of the config after all integrations have completed their config updates, [see the `astro:config:done` hook](#astroconfigdone).

#### `command` option

[Section titled “command option”](#command-option)

**Type:** `'dev' | 'build' | 'preview' | 'sync'`

* `dev` - Project is executed with `astro dev`
* `build` - Project is executed with `astro build`
* `preview` - Project is executed with `astro preview`
* `sync` - Project is executed with `astro sync`

#### `isRestart` option

[Section titled “isRestart option”](#isrestart-option)

**Type:** `boolean`

**Added in:** `astro@1.5.0`

`false` when the dev server starts, `true` when a reload is triggered. Useful to detect when this function is called more than once.

#### `updateConfig()` option

[Section titled “updateConfig() option”](#updateconfig-option)

**Type:** `(newConfig: DeepPartial<AstroConfig>) => AstroConfig;`

A callback function to update the user-supplied [Astro config](/en/reference/configuration-reference/). Any config you provide **will be merged with the user config + other integration config updates,** so you are free to omit keys!

For example, say you need to supply a [Vite](https://vite.dev/) plugin to the user’s project:

```js
import bananaCSS from '@vitejs/official-banana-css-plugin';


export default {
  name: 'banana-css-integration',
  hooks: {
    'astro:config:setup': ({ updateConfig }) => {
      updateConfig({
        vite: {
          plugins: [bananaCSS()],
        }
      })
    }
  }
}
```

#### `addRenderer()` option

[Section titled “addRenderer() option”](#addrenderer-option)

**Type:** `(renderer:` [`AstroRenderer`](https://github.com/withastro/astro/blob/fdd607c5755034edf262e7b275732519328a33b2/packages/astro/src/%40types/astro.ts#L872-L883) `) => void;`\
**Examples:** [`svelte`](https://github.com/withastro/astro/blob/main/packages/integrations/svelte/src/index.ts), [`react`](https://github.com/withastro/astro/blob/main/packages/integrations/react/src/index.ts), [`preact`](https://github.com/withastro/astro/blob/main/packages/integrations/preact/src/index.ts), [`vue`](https://github.com/withastro/astro/blob/main/packages/integrations/vue/src/index.ts), [`solid`](https://github.com/withastro/astro/blob/main/packages/integrations/solid/src/index.ts)

A callback function to add a component framework renderer (i.e. React, Vue, Svelte, etc). You can browse the examples and type definition above for more advanced options, but here are the 2 main options to be aware of:

* `clientEntrypoint` - path to a file that executes on the client whenever your component is used. This is mainly for rendering or hydrating your component with JS.
* `serverEntrypoint` - path to a file that executes during server-side requests or static builds whenever your component is used. These should render components to static markup, with hooks for hydration where applicable. [React’s `renderToString` callback](https://react.dev/reference/react-dom/server/renderToString) is a classic example.

**Added in:** `astro@5.0.0`

The functions `clientEntrypoint` and `serverEntrypoint` accept a `URL`.

#### `addWatchFile()` option

[Section titled “addWatchFile() option”](#addwatchfile-option)

**Type:** `(path: URL | string) => void`

**Added in:** `astro@1.5.0`

If your integration depends on some configuration file that Vite doesn’t watch and/or needs a full dev server restart to take effect, add it with `addWatchFile`. Whenever that file changes, the Astro dev server will be reloaded (you can check when a reload happens with `isRestart`).

Example usage:

```js
// Must be an absolute path!
addWatchFile('/home/user/.../my-config.json');
addWatchFile(new URL('./ec.config.mjs', config.root));
```

#### `addClientDirective()` option

[Section titled “addClientDirective() option”](#addclientdirective-option)

**Type:** `(directive:` [`ClientDirectiveConfig`](https://github.com/withastro/astro/blob/00327c213f74627ac9ca1dec774efa5bf71e9375/packages/astro/src/%40types/astro.ts#L1872-L1875) `) => void;`

**Added in:** `astro@2.6.0`

Adds a [custom client directive](/en/reference/directives-reference/#custom-client-directives) to be used in `.astro` files.

Note that directive entrypoints are only bundled through esbuild and should be kept small so they don’t slow down component hydration.

Example usage:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import clickDirective from './astro-click-directive/register.js'


// https://astro.build/config
export default defineConfig({
  integrations: [
    clickDirective()
  ],
});
```

astro-click-directive/register.js

```js
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "client:click",
  hooks: {
    "astro:config:setup": ({ addClientDirective }) => {
      addClientDirective({
        name: "click",
        entrypoint: "./astro-click-directive/click.js",
      });
    },
  },
});
```

astro-click-directive/click.js

```js
/**
 * Hydrate on first click on the window
 * @type {import('astro').ClientDirective}
 */
export default (load, opts, el) => {
  window.addEventListener('click', async () => {
    const hydrate = await load()
    await hydrate()
  }, { once: true })
}
```

You can also add types for the directives in your library’s type definition file:

astro-click-directive/index.d.ts

```ts
import 'astro'
declare module 'astro' {
  interface AstroClientDirectives {
    'client:click'?: boolean
  }
}
```

#### `addDevToolbarApp()` option

[Section titled “addDevToolbarApp() option”](#adddevtoolbarapp-option)

**Type:** `(entrypoint: DevToolbarAppEntry) => void;`

**Added in:** `astro@3.4.0`

Adds a [custom dev toolbar app](/en/reference/dev-toolbar-app-reference/).

Example usage:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import devToolbarIntegration from './astro-dev-toolbar-app/integration.js'


// https://astro.build/config
export default defineConfig({
  integrations: [
    devToolbarIntegration()
  ],
});
```

astro-dev-toolbar-app/integration.js

```js
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "dev-toolbar-app",
  hooks: {
    "astro:config:setup": ({ addDevToolbarApp }) => {
      addDevToolbarApp({
        entrypoint: "./astro-dev-toolbar-app/plugin.js",
        id: "my-plugin",
        name: "My Plugin"
      });
    },
  },
});
```

astro-dev-toolbar-app/plugin.js

```js
/**
 * @type {import('astro').DevToolbarApp}
 */
export default {
  id: "my-plugin",
  name: "My Plugin",
  icon: "<svg>...</svg>",
  init() {
    console.log("I'm a dev toolbar app!")
  },
};
```

#### `addMiddleware()` option

[Section titled “addMiddleware() option”](#addmiddleware-option)

**Type:** `(middleware:` [`AstroIntegrationMiddleware`](https://github.com/withastro/astro/blob/852ac0f75dfca1b2602e9cdbfa0447d9998e2449/packages/astro/src/%40types/astro.ts#L2124-L2127) `) => void;`

**Added in:** `astro@3.5.0`

Adds [middleware](/en/guides/middleware/) to run on each request. Takes the `entrypoint` module that contains the middleware, and an `order` to specify whether it should run before (`pre`) other middleware or after (`post`).

@my-package/integration.js

```js
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "my-middleware-package",
  hooks: {
    "astro:config:setup": ({ addMiddleware }) => {
      addMiddleware({
        entrypoint: '@my-package/middleware',
        order: 'pre'
      });
    },
  },
});
```

Middleware is defined in a package with an `onRequest` function, as with user-defined middleware.

@my-package/middleware.js

```js
import { defineMiddleware } from 'astro:middleware';


export const onRequest = defineMiddleware(async (context, next) => {
  if(context.url.pathname === '/some-test-path') {
    return Response.json({
      ok: true
    });
  }


  return next();
});
```

**Added in:** `astro@5.0.0`

The function also accepts a `URL` for `entrypoint`:

@my-package/integration.js

```diff
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "my-middleware-package",
  hooks: {
    "astro:config:setup": ({ addMiddleware }) => {
      addMiddleware({
+        entrypoint: new URL('./middleware.js', import.meta.url),
        order: 'pre'
      });
    },
  },
});
```

#### `injectRoute()` option

[Section titled “injectRoute() option”](#injectroute-option)

**Type:** `({ pattern: string; entrypoint: string | URL; prerender?: boolean }) => void;`

A callback function to inject routes into an Astro project. Injected routes can be [`.astro` pages](/en/basics/astro-pages/) or [`.js` and `.ts` route handlers](/en/guides/endpoints/#static-file-endpoints).

`injectRoute` takes an object with a `pattern` and an `entrypoint`.

* `pattern` - where the route should be output in the browser, for example `/foo/bar`. A `pattern` can use Astro’s filepath syntax for denoting dynamic routes, for example `/foo/[bar]` or `/foo/[...bar]`. Note that a file extension is **not** needed in the `pattern`.
* `entrypoint` - a bare module specifier pointing towards the `.astro` page or `.js`/`.ts` route handler that handles the route denoted in the `pattern`.
* `prerender` - a boolean to set if Astro can’t detect your `prerender` export.

##### Example usage

[Section titled “Example usage”](#example-usage)

```js
injectRoute({
  // Use Astro’s pattern syntax for dynamic routes.
  pattern: '/subfolder/[dynamic]',
  // Use relative path syntax for a local route.
  entrypoint: './src/dynamic-page.astro',
  // Use only if Astro can't detect your prerender export
  prerender: false
});
```

For an integration designed to be installed in other projects, use its package name to refer to the route entrypoint. The following example shows a package published to npm as `@fancy/dashboard` injecting a dashboard route:

```js
injectRoute({
  pattern: '/fancy-dashboard',
  entrypoint: '@fancy/dashboard/dashboard.astro'
});
```

When publishing your package (`@fancy/dashboard`, in this case) to npm, you must export `dashboard.astro` in your `package.json`:

package.json

```json
{
  "name": "@fancy/dashboard",
  // ...
  "exports": { "./dashboard.astro": "./dashboard.astro" }
}
```

**Added in:** `astro@5.0.0`

The function also accepts a `URL` for `entrypoint`:

```js
injectRoute({
  pattern: '/fancy-dashboard',
  entrypoint: new URL('./dashboard.astro', import.meta.url)
});
```

#### `injectScript()` option

[Section titled “injectScript() option”](#injectscript-option)

**Type:** `(stage: InjectedScriptStage, content: string) => void;`

A callback function to inject a string of JavaScript content onto every page.

The **`stage`** denotes how this script (the `content`) should be inserted. Some stages allow inserting scripts without modification, while others allow optimization during [Vite’s bundling step](https://vite.dev/guide/build.html):

* `"head-inline"`: Injected into a script tag in the `<head>` of every page. **Not** optimized or resolved by Vite.

* `"before-hydration"`: Imported client-side, before the hydration script runs. Optimized and resolved by Vite.

* `"page"`: Similar to `head-inline`, except that the injected snippet is handled by Vite and bundled with any other `<script>` tags defined inside of Astro components on the page. The script will be loaded with a `<script type="module">` in the final page output, optimized and resolved by Vite.

* `"page-ssr"`: Imported as a separate module in the frontmatter of every Astro page component. Because this stage imports your script, the `Astro` global is not available and your script will only be run once when the `import` is first evaluated.

  The main use for the `page-ssr` stage is injecting a CSS `import` into every page to be optimized and resolved by Vite:

  ```js
  injectScript('page-ssr', 'import "global-styles.css";');
  ```

#### `createCodegenDir`

[Section titled “createCodegenDir”](#createcodegendir)

**Type:** `() => URL;`

**Added in:** `astro@5.0.0`

A function that creates the `<root>/.astro/integrations/<normalized_integration_name>` folder and returns its path.

It allows you to have a dedicated folder, avoiding conflicts with another integration or Astro itself. This directory is created by calling this function so it’s safe to write files to it directly:

my-integration.ts

```ts
import { writeFileSync } from 'node:fs'


const integration = {
  name: 'my-integration',
  hooks: {
    'astro:config:setup': ({ createCodegenDir }) => {
      const codegenDir = createCodegenDir()
      writeFileSync(new URL('cache.json', codegenDir), '{}', 'utf-8')
    }
  }
}
```

### `astro:route:setup`

[Section titled “astro:route:setup”](#astroroutesetup)

**Added in:** `astro@4.14.0`

**Previous hook:** [`astro:config:setup`](#astroconfigsetup)

**Next hook:** [`astro:routes:resolved`](#astroroutesresolved)

**When:** In `astro build`, before bundling starts. In `astro dev`, while building the module graph and on every change to a file based route (added/removed/updated).

**Why:** To set options for a route at build or request time, such as enabling [on-demand server rendering](/en/guides/on-demand-rendering/#enabling-on-demand-rendering).

```js
'astro:route:setup'?: (options: {
  route: RouteOptions;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `route` option

[Section titled “route option”](#route-option)

**Type:** [`RouteOptions`](https://github.com/withastro/astro/blob/3b10b97a4fecd1dfd959b160a07b5b8427fe40a7/packages/astro/src/types/public/integrations.ts#L14-L27)

An object with a `component` property to identify the route and the following additional values to allow you to configure the generated route: `prerender`.

##### `route.component`

[Section titled “route.component”](#routecomponent)

**Type:** `string`

**Added in:** `astro@4.14.0`

The `component` property indicates the entrypoint that will be rendered on the route. You can access this value before the routes are built to configure on-demand server rendering for that page.

##### `route.prerender`

[Section titled “route.prerender”](#routeprerender)

**Type:** `boolean`\
**Default:** `undefined`

**Added in:** `astro@4.14.0`

The `prerender` property is used to configure [on-demand server rendering](/en/guides/on-demand-rendering/#enabling-on-demand-rendering) for a route. If the route file contains an explicit `export const prerender` value, the value will be used as the default instead of `undefined`.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  integrations: [setPrerender()],
});


function setPrerender() {
  return {
    name: 'set-prerender',
    hooks: {
      'astro:route:setup': ({ route }) => {
        if (route.component.endsWith('/blog/[slug].astro')) {
          route.prerender = true;
        }
      },
    },
  };
}
```

If the final value after running all the hooks is `undefined`, the route will fall back to a prerender default based on the [`output` option](/en/reference/configuration-reference/#output): prerendered for `static` mode, and on-demand rendered for `server` mode.

### `astro:routes:resolved`

[Section titled “astro:routes:resolved”](#astroroutesresolved)

**Added in:** `astro@5.0.0`

**Previous hook:** [`astro:route:setup`](#astroroutesetup)

**Next hook:** [`astro:config:done`](#astroconfigdone) (only during setup)

**When:** In `astro dev`, it also runs on every change to a file based route (added/removed/updated).

**Why:** To access routes and their metadata

```js
'astro:routes:resolved'?: (options: {
  routes: IntegrationResolvedRoute[];
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `routes` option

[Section titled “routes option”](#routes-option)

**Type:** [`IntegrationResolvedRoute[]`](#integrationresolvedroute-type-reference)

A list of all routes with their associated metadata.

Example use:

my-integration.mjs

```js
const integration = () => {
  return {
    name: 'my-integration',
    hooks: {
      'astro:routes:resolved': ({ routes }) => {
        const projectRoutes = routes.filter(r => r.origin === 'project').map(r => r.pattern)


        console.log(projectRoutes)
      },
    }
  }
}
```

### `astro:config:done`

[Section titled “astro:config:done”](#astroconfigdone)

**Previous hook:** [`astro:routes:resolved`](#astroroutesresolved)

**Next hook:** [`astro:server:setup`](#astroserversetup) when running in “dev” mode, or [`astro:build:start`](#astrobuildstart) during production builds

**When:** After the Astro config has resolved and other integrations have run their `astro:config:setup` hooks.

**Why:** To retrieve the final config for use in other hooks.

```js
'astro:config:done'?: (options: {
  config: AstroConfig;
  setAdapter: (adapter: AstroAdapter) => void;
  injectTypes: (injectedType: InjectedType) => URL;
  logger: AstroIntegrationLogger;
  buildOutput: 'static' | 'server';
}) => void | Promise<void>;
```

#### `config` option

[Section titled “config option”](#config-option-1)

**Type:** `AstroConfig`

A read-only copy of the user-supplied [Astro config](/en/reference/configuration-reference/). This is resolved *after* other integrations have run.

#### `setAdapter()` option

[Section titled “setAdapter() option”](#setadapter-option)

**Type:** `(adapter: AstroAdapter) => void;`

Makes the integration an adapter. Read more in the [adapter API](/en/reference/adapter-reference/).

#### `injectTypes()` option

[Section titled “injectTypes() option”](#injecttypes-option)

**Type:** `(injectedType: { filename: string; content: string }) => URL`

**Added in:** `astro@4.14.0`

Allows you to inject types into your user’s project by adding a new `*.d.ts` file.

The `filename` property will be used to generate a file at `/.astro/integrations/<normalized_integration_name>/<normalized_filename>.d.ts` and must end with `".d.ts"`.

The `content` property will create the body of the file and must be valid TypeScript.

Additionally, `injectTypes()` returns a URL to the normalized path so you can overwrite its content later on, or manipulate it in any way you want.

```js
const path = injectTypes({
  filename: "types.d.ts",
  content: "declare module 'virtual:integration' {}"
})
console.log(path) // URL
```

#### `buildOutput` option

[Section titled “buildOutput option”](#buildoutput-option)

**Type:** `'static' | 'server'`

**Added in:** `astro@5.0.0`

Allows you to adapt the logic of your integration depending on the user’s project output.

### `astro:server:setup`

[Section titled “astro:server:setup”](#astroserversetup)

**Previous hook:** [`astro:config:done`](#astroconfigdone)

**Next hook:** [`astro:server:start`](#astroserverstart)

**When:** Just after the Vite server is created in “dev” mode, but before the `listen()` event is fired. [See Vite’s createServer API](https://vite.dev/guide/api-javascript.html#createserver) for more.

**Why:** To update Vite server options and middleware, or enable support for refreshing the content layer.

```js
'astro:server:setup'?: (options: {
  server: vite.ViteDevServer;
  logger: AstroIntegrationLogger;
  toolbar: ReturnType<typeof getToolbarServerCommunicationHelpers>;
  refreshContent: (options: {
    loaders?: Array<string>;
    context?: Record<string, any>;
  }) => Promise<void>;
}) => void | Promise<void>;
```

#### `server` option

[Section titled “server option”](#server-option)

**Type:** [`ViteDevServer`](https://vite.dev/guide/api-javascript.html#vitedevserver)

A mutable instance of the Vite server used in “dev” mode. For instance, this is [used by our Partytown integration](/en/guides/integrations-guide/partytown/) to inject the Partytown server as middleware:

```js
export default {
  name: 'partytown',
  hooks: {
    'astro:server:setup': ({ server }) => {
      server.middlewares.use(
        function middleware(req, res, next) {
          // handle requests
        }
      );
    }
  }
}
```

#### `toolbar` option

[Section titled “toolbar option”](#toolbar-option)

**Type:** `ReturnType<typeof getToolbarServerCommunicationHelpers>`

**Added in:** `astro@4.7.0`

An object providing callback functions to interact with the [dev toolbar](/en/reference/dev-toolbar-app-reference/):

##### `on()`

[Section titled “on()”](#on)

**Type:** `<T>(event: string, callback: (data: T) => void) => void`

A function that takes an event name as first argument and a callback function as second argument. This allows you to receive a message from a dev toolbar app with data associated to that event.

##### `onAppInitialized()`

[Section titled “onAppInitialized()”](#onappinitialized)

**Type:** `(appId: string, callback: (data: Record<string, never>) => void) => void`

A function fired when a dev toolbar app is initialized. The first argument is the id of the app that was initialized. The second argument is a callback function to run when the app is initialized.

##### `onAppToggled()`

[Section titled “onAppToggled()”](#onapptoggled)

**Type:** `(appId: string, callback: (data: { state: boolean; }) => void) => void`

A function fired when a dev toolbar app is toggled on or off. The first argument is the id of the app that was toggled. The second argument is a callback function providing the state to execute when the application is toggled.

##### `send()`

[Section titled “send()”](#send)

**Type:** `<T>(event: string, payload: T) => void`

A function that sends a message to the dev toolbar that an app can listen for. This takes an event name as the first argument and a payload as the second argument which can be any serializable data.

#### `refreshContent()` option

[Section titled “refreshContent() option”](#refreshcontent-option)

**Type:** `(options: { loaders?: Array<string>; context?: Record<string, any>; }) => Promise<void>`

**Added in:** `astro@5.0.0`

A function for integrations to trigger an update to the content layer during `astro dev`. This can be used, for example, to register a webhook endpoint during dev, or to open a socket to a CMS to listen for changes.

By default, `refreshContent` will refresh all collections. You can optionally pass a `loaders` property, which is an array of loader names. If provided, only collections that use those loaders will be refreshed. For example, A CMS integration could use this property to only refresh its own collections.

You can also pass a `context` object to the loaders. This can be used to pass arbitrary data such as the webhook body, or an event from the websocket.

my-integration.ts

```ts
{
  name: 'my-integration',
  hooks: {
    'astro:server:setup': async ({ server, refreshContent }) => {
      // Register a dev server webhook endpoint
      server.middlewares.use('/_refresh', async (req, res) => {
        if(req.method !== 'POST') {
          res.statusCode = 405
          res.end('Method Not Allowed');
          return
        }
        let body = '';
        req.on('data', chunk => {
          body += chunk.toString();
        });
        req.on('end', async () => {
          try {
            const webhookBody = JSON.parse(body);
            await refreshContent({
              context: { webhookBody },
              loaders: ['my-loader']
            });
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ message: 'Content refreshed successfully' }));
          } catch (error) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to refresh content: ' + error.message }));
          }
        });
      });
    }
  }
}
```

The loader can then access the `refreshContextData` property to get the webhook body. See the [`refreshContextData`](/en/reference/content-loader-reference/#refreshcontextdata) property for more information.

### `astro:server:start`

[Section titled “astro:server:start”](#astroserverstart)

**Previous hook:** [`astro:server:setup`](#astroserversetup)

**Next hook:** [`astro:server:done`](#astroserverdone)

**When:** Just after the server’s `listen()` event has fired.

**Why:** To intercept network requests at the specified address. If you intend to use this address for middleware, consider using `astro:server:setup` instead.

```js
'astro:server:start'?: (options: {
  address: AddressInfo;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `address` option

[Section titled “address option”](#address-option)

**Type:** [`AddressInfo`](https://microsoft.github.io/PowerBI-JavaScript/interfaces/_node_modules__types_node_net_d_._net_.addressinfo.html)

The address, family and port number supplied by the [Node.js Net module](https://nodejs.org/api/net.html).

### `astro:server:done`

[Section titled “astro:server:done”](#astroserverdone)

**Previous hook:** [`astro:server:start`](#astroserverstart)

**When:** Just after the dev server is closed.

**Why:** To run any cleanup events you may trigger during the `astro:server:setup` or `astro:server:start` hooks.

```js
'astro:server:done'?: (options: {
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

### `astro:build:start`

[Section titled “astro:build:start”](#astrobuildstart)

**Previous hook:** [`astro:config:done`](#astroconfigdone)

**Next hook:** [`astro:build:setup`](#astrobuildsetup)

**When:** After the `astro:config:done` event, but before the production build begins.

**Why:** To set up any global objects or clients needed during a production build. This can also extend the build configuration options in the [adapter API](/en/reference/adapter-reference/).

```js
'astro:build:start'?: (options: {
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

### `astro:build:setup`

[Section titled “astro:build:setup”](#astrobuildsetup)

**Previous hook:** [`astro:build:start`](#astrobuildstart)

**Next hook:** [`astro:build:ssr`](#astrobuildssr)

**When:** After the `astro:build:start` hook, runs immediately before the build.

**Why:** At this point, the Vite config for the build has been completely constructed, this is your final chance to modify it. This can be useful for example to overwrite some defaults. If you’re not sure whether you should use this hook or `astro:build:start`, use `astro:build:start` instead.

```js
'astro:build:setup'?: (options: {
  vite: vite.InlineConfig;
  pages: Map<string, PageBuildData>;
  target: 'client' | 'server';
  updateConfig: (newConfig: vite.InlineConfig) => void;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `vite` option

[Section titled “vite option”](#vite-option)

**Type:** [`InlineConfig`](https://vite.dev/guide/api-javascript.html#inlineconfig)

An object that allows you to access the Vite configuration used in the build.

This can be useful if you need to access configuration options in your integration:

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:setup': ({ vite }) => {
      const { publicDir, root } = vite;
    },
  }
}
```

#### `pages` option

[Section titled “pages option”](#pages-option)

**Type:** `Map<string, PageBuildData>`

A `Map` with a list of pages as key and their build data as value.

This can be used to perform an action if a route matches a criteria:

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:setup': ({ pages }) => {
      pages.forEach((data) => {
        if (data.route.pattern.test("/blog")) {
          console.log(data.route.type);
        }
      });
    },
  }
}
```

#### `target` option

[Section titled “target option”](#target-option)

**Type:** `'client' | 'server'`

Builds are separated in two distinct phases: `client` and `server`. This option allow you to determine the current build phase.

This can be used to perform an action only in a specific phase:

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:setup': ({ target }) => {
      if (target === "server") {
        // do something in server build phase
      }
    },
  }
}
```

#### `updateConfig()` option

[Section titled “updateConfig() option”](#updateconfig-option-1)

**Type:** `(newConfig: InlineConfig) => void`

A callback function to update the [Vite](https://vite.dev/) options used in the build. Any config you provide **will be merged with the user config + other integration config updates**, so you are free to omit keys!

For example, this can be used to supply a plugin to the user’s project:

```js
import awesomeCssPlugin from 'awesome-css-vite-plugin';


export default {
  name: 'my-integration',
  hooks: {
    'astro:build:setup': ({ updateConfig }) => {
      updateConfig({
        plugins: [awesomeCssPlugin()],
      })
    }
  }
}
```

### `astro:build:ssr`

[Section titled “astro:build:ssr”](#astrobuildssr)

**Previous hook:** [`astro:build:setup`](#astrobuildsetup)

**Next hook:** [`astro:build:generated`](#astrobuildgenerated)

**When:** After a production SSR build has completed.

**Why:** To access the SSR manifest and map of the emitted entry points. This is useful when creating custom SSR builds in plugins or integrations.

* `entryPoints` maps a page route to the physical file emitted after the build;
* `middlewareEntryPoint` is the file system path of the middleware file;

```js
'astro:build:ssr'?: (options: {
  manifest: SerializedSSRManifest;
  entryPoints: Map<IntegrationRouteData, URL>;
  middlewareEntryPoint: URL | undefined;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `manifest` option

[Section titled “manifest option”](#manifest-option)

**Type:** [`SerializedSSRManifest`](https://github.com/withastro/astro/blob/3b10b97a4fecd1dfd959b160a07b5b8427fe40a7/packages/astro/src/core/app/types.ts#L91-L109)

Allows you to create a custom build by accessing the SSR manifest.

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:ssr': ({ manifest }) => {
      const { i18n } = manifest;
      if (i18n?.strategy === "domains-prefix-always") {
        // do something
      }
    },
  },
}
```

#### `entryPoints` option

[Section titled “entryPoints option”](#entrypoints-option)

**Type:** `Map<IntegrationRouteData, URL>`

**Added in:** `astro@2.7.0`

A `Map` of the emitted entry points with the `IntegrationRouteData` as key and the physical file URL as value.

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:ssr': ({ entryPoints }) => {
      entryPoints.forEach((url) => {
        console.log(url.href);
      });
    },
  },
}
```

#### `middlewareEntryPoint` option

[Section titled “middlewareEntryPoint option”](#middlewareentrypoint-option)

**Type:** `URL | undefined`

**Added in:** `astro@2.8.0`

Exposes the [middleware](/en/guides/middleware/) file path.

```js
export default {
  name: 'my-integration',
  hooks: {
    'astro:build:ssr': ({ middlewareEntryPoint }) => {
      if (middlewareEntryPoint) {
        // do some operations if a middleware exist
      }
    },
  },
}
```

### `astro:build:generated`

[Section titled “astro:build:generated”](#astrobuildgenerated)

**Added in:** `astro@1.3.0`

**Previous hook:** [`astro:build:ssr`](#astrobuildssr)

**Next hook:** [`astro:build:done`](#astrobuilddone)

**When:** After a static production build has finished generating routes and assets.

**Why:** To access generated routes and assets **before** build artifacts are cleaned up. This is a very uncommon use case. We recommend using [`astro:build:done`](#astrobuilddone) unless you really need to access the generated files before cleanup.

```js
'astro:build:generated'?: (options: {
  dir: URL;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `dir` option

[Section titled “dir option”](#dir-option)

**Type:** [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL)

A URL path to the build output directory. Note that if you need a valid absolute path string, you should use Node’s built-in [`fileURLToPath`](https://nodejs.org/api/url.html#urlfileurltopathurl-options) utility.

```js
import { fileURLToPath } from 'node:url';


export default {
  name: 'my-integration',
  hooks: {
    'astro:build:generated': ({ dir }) => {
      const outFile = fileURLToPath(new URL('./my-integration.json', dir));
    }
  }
}
```

### `astro:build:done`

[Section titled “astro:build:done”](#astrobuilddone)

**Previous hook:** [`astro:build:generated`](#astrobuildgenerated)

**When:** After a production build (SSG or SSR) has completed.

**Why:** To access generated routes and assets for extension (ex. copy content into the generated `/assets` directory). If you plan to transform generated assets, we recommend exploring the [Vite Plugin API](https://vite.dev/guide/api-plugin.html) and [configuring via `astro:config:setup`](#updateconfig-option) instead.

```js
'astro:build:done'?: (options: {
  pages: { pathname: string }[];
  dir: URL;
  /** @deprecated Use the `assets` map and the new `astro:routes:resolved` hook */
  routes: IntegrationRouteData[];
  assets: Map<string, URL[]>;
  logger: AstroIntegrationLogger;
}) => void | Promise<void>;
```

#### `dir` option

[Section titled “dir option”](#dir-option-1)

**Type:** [`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL)

A URL path to the build output directory. Note that if you need a valid absolute path string, you should use Node’s built-in [`fileURLToPath`](https://nodejs.org/api/url.html#urlfileurltopathurl-options) utility.

```js
import { writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';


export default function myIntegration() {
  return {
    hooks: {
      'astro:build:done': async ({ dir }) => {
        const metadata = await getIntegrationMetadata();
        // Use fileURLToPath to get a valid, cross-platform absolute path string
        const outFile = fileURLToPath(new URL('./my-integration.json', dir));
        await writeFile(outFile, JSON.stringify(metadata));
      }
    }
  }
}
```

#### `routes` option

[Section titled “routes option”](#routes-option-1)

Caution

This property is deprecated since v5.0. Check the [migration guide](/en/guides/upgrade-to/v5/#deprecated-routes-on-astrobuilddone-hook-integration-api).

**Type:** [`IntegrationRouteData[]`](#integrationroutedata-type-reference)

A list of all generated routes alongside their associated metadata.

You can reference the full `IntegrationRouteData` type below, but the most common properties are:

* `component` - the input file path relative to the project root
* `pathname` - the output file URL (undefined for routes using `[dynamic]` and `[...spread]` params)

#### `assets` option

[Section titled “assets option”](#assets-option)

**Type:** `Map<string, URL[]>`

**Added in:** `astro@5.0.0`

Contains URLs to output files paths, grouped by [`IntegrationResolvedRoute`](#integrationresolvedroute-type-reference) `pattern` property.

#### `pages` option

[Section titled “pages option”](#pages-option-1)

**Type:** `{ pathname: string }[]`

A list of all generated pages. It is an object with one property.

* `pathname` - the finalized path of the page.

### Custom hooks

[Section titled “Custom hooks”](#custom-hooks)

Custom hooks can be added to integrations by extending the `IntegrationHooks` interface through [global augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#global-augmentation).

```ts
declare global {
  namespace Astro {
    export interface IntegrationHook {
      'your:hook': (params: YourHookParameters) => Promise<void>
    }
  }
}
```

Astro reserves the `astro:` prefix for future built-in hooks. Please choose a different prefix when naming your custom hook.

## Integration types reference

[Section titled “Integration types reference”](#integration-types-reference)

### `AstroIntegrationLogger`

[Section titled “AstroIntegrationLogger”](#astrointegrationlogger)

An instance of the Astro logger, useful to write logs. This logger uses the same [log level](/en/reference/cli-reference/#--verbose) configured via CLI.

**Methods available** to write to terminal:

* `logger.info("Message")`;
* `logger.warn("Message")`;
* `logger.error("Message")`;
* `logger.debug("Message")`;

All the messages are prepended with a label that has the same value as the name of the integration.

integration.ts

```ts
import type { AstroIntegration } from "astro";
export function formatIntegration(): AstroIntegration {
  return {
    name: "astro-format",
    hooks: {
      "astro:build:done": ({ logger }) => {
        // do something
        logger.info("Integration ready.");
      }
    }
  }
}
```

The example above will log a message that includes the provided `info` message:

```shell
[astro-format] Integration ready.
```

To log some messages with a different label, use the `.fork` method to specify an alternative to the default `name`:

integration.ts

```ts
import type { AstroIntegration } from "astro";
export function formatIntegration(): AstroIntegration {
  return {
    name: "astro-format",
    hooks: {
      "astro:config:done": ({ logger }) => {
        // do something
        logger.info("Integration ready.");
      },
      "astro:build:done": ({ logger }) => {
        const buildLogger = logger.fork("astro-format/build");
        // do something
        buildLogger.info("Build finished.")
      }
    }
  }
}
```

The example above will produce logs with `[astro-format]` by default, and `[astro-format/build]` when specified:

```shell
[astro-format] Integration ready.
[astro-format/build] Build finished.
```

### `HookParameters`

[Section titled “HookParameters”](#hookparameters)

You can get the type of a hook’s arguments by passing the hook’s name to the `HookParameters` utility type. In the following example, a function’s `options` argument is typed to match the parameters of the `astro:config:setup` hook:

```ts
import type { HookParameters } from 'astro';


function mySetup(options: HookParameters<'astro:config:setup'>) {
  options.updateConfig({ /* ... */ });
}
```

### `IntegrationResolvedRoute` type reference

[Section titled “IntegrationResolvedRoute type reference”](#integrationresolvedroute-type-reference)

```ts
interface IntegrationResolvedRoute {
  pattern: RouteData['route'];
  patternRegex: RouteData['pattern'];
  entrypoint: RouteData['component'];
  isPrerendered: RouteData['prerender'];
  redirectRoute?: IntegrationResolvedRoute;
  generate: (data?: any) => string;
  params: string[];
  pathname?: string;
  segments: RoutePart[][];
  type: RouteType;
  redirect?: RedirectConfig;
  origin: 'internal' | 'external' | 'project';
}
```

#### `pattern`

[Section titled “pattern”](#pattern)

**Type:** `string`

Allows you to identify the type of route based on its path. Here are some examples of paths associated with their pattern:

* `src/pages/index.astro` will be `/`
* `src/pages/blog/[...slug].astro` will be `/blog/[...slug]`
* `src/pages/site/[blog]/[...slug].astro` will be `/site/[blog]/[...slug]`

#### `patternRegex`

[Section titled “patternRegex”](#patternregex)

**Type:** `RegExp`

Allows you to access a regex used for matching an input URL against a requested route.

For example, given a `[fruit]/about.astro` path, the regex will be `/^\/([^/]+?)\/about\/?$/`. Using `pattern.test("banana/about")` will return `true`.

#### `entrypoint`

[Section titled “entrypoint”](#entrypoint)

**Type:** `string`

The URL pathname of the source component.

#### `isPrerendered`

[Section titled “isPrerendered”](#isprerendered)

**Type:** `boolean`

Determines whether the route use [on demand rendering](/en/guides/on-demand-rendering/). The value will be `true` for projects configured with:

* `output: 'static'` when the route does not export `const prerender = true`
* `output: 'server'` when the route exports `const prerender = false`

#### `redirectRoute`

[Section titled “redirectRoute”](#redirectroute)

**Type:** `IntegrationResolvedRoute | undefined`

When the value of `IntegrationResolvedRoute.type` is `redirect`, the value will be the `IntegrationResolvedRoute` to redirect to. Otherwise, the value will be undefined.

#### `generate()`

[Section titled “generate()”](#generate)

**Type:** `(data?: any) => string`

A function that provides the optional parameters of the route, interpolates them with the route pattern, and returns the path name of the route.

For example, with a route such as `/blog/[...id].astro`, the `generate` function could return:

```js
console.log(generate({ id: 'presentation' })) // will log `/blog/presentation`
```

#### `params`

[Section titled “params”](#params)

**Type:** `string[]`

Allows you to access the route `params`. For example, when a project uses the following [dynamic routes](/en/guides/routing/#dynamic-routes) `/pages/[lang]/[...slug].astro`, the value will be `['lang', '...slug']`.

#### `pathname`

[Section titled “pathname”](#pathname)

**Type:** `string | undefined`

For regular routes, the value will be the URL pathname where this route will be served. When the project uses [dynamic routes](/en/guides/routing/#dynamic-routes) (ie. `[dynamic]` or `[...spread]`), the pathname will be undefined.

#### `segments`

[Section titled “segments”](#segments)

**Type:** `RoutePart[][]`

Allows you to access the route [`params`](#params) with additional metadata. Each object contains the following properties:

* `content`: the `param` name,
* `dynamic`: whether the route is dynamic or not,
* `spread`: whether the dynamic route uses the spread syntax or not.

For example, the following route `/pages/[blog]/[...slug].astro` will output the segments:

```js
[
  [ { content: 'pages', dynamic: false, spread: false } ],
  [ { content: 'blog', dynamic: true, spread: false } ],
  [ { content: '...slug', dynamic: true, spread: true } ]
]
```

#### `type`

[Section titled “type”](#type)

**Type:** `RouteType`

Allows you to identify the type of route. Possible values are:

* `page`: a route that lives in the file system, usually an Astro component
* `endpoint`: a route that lives in the file system, usually a JS file that exposes endpoints methods
* `redirect`: a route points to another route that lives in the file system
* `fallback`: a route that doesn’t exist in the file system that needs to be handled with other means, usually the middleware

#### `redirect`

[Section titled “redirect”](#redirect)

**Type:** `RedirectConfig | undefined`

Allows you to access the route to redirect to. This can be a string or an object containing information about the status code and its destination.

#### `origin`

[Section titled “origin”](#origin)

**Type:** `'internal' | 'external' | 'project'`

Determines if a route comes from Astro core (`internal`), an integration (`external`) or the user’s project (`project`).

### `IntegrationRouteData` type reference

[Section titled “IntegrationRouteData type reference”](#integrationroutedata-type-reference)

Caution

This type is deprecated since v5.0. Use [`IntegrationResolvedRoute`](#integrationresolvedroute-type-reference) instead.

A smaller version of the `RouteData` that is used in the integrations.

```ts
interface IntegrationRouteData {
  type: RouteType;
  component: string;
  pathname?: string;
  pattern: RegExp;
  params: string[];
  segments: { content: string; dynamic: boolean; spread: boolean; }[][];
  generate: (data?: any) => string;
  prerender: boolean;
  distURL?: URL[];
  redirect?: RedirectConfig;
  redirectRoute?: IntegrationRouteData;
}
```

#### `type`

[Section titled “type”](#type-1)

**Type:** `RouteType`

Allows you to identify the type of the route. The value can be:

* `page`: a route that lives in the file system, usually an Astro component
* `endpoint`: a route that lives in the file system, usually a JS file that exposes endpoints methods
* `redirect`: a route that points to another route that lives in the file system
* `fallback`: a route that doesn’t exist in the file system and needs to be handled with other means, usually middleware

#### `component`

[Section titled “component”](#component)

**Type:** `string`

Allows you to access the source component URL pathname.

#### `pathname`

[Section titled “pathname”](#pathname-1)

**Type:** `string | undefined`

For regular routes, the value will be the URL pathname where this route will be served. When the project uses [dynamic routes](/en/guides/routing/#dynamic-routes) (ie. `[dynamic]` or `[...spread]`), the pathname will be undefined.

#### `pattern`

[Section titled “pattern”](#pattern-1)

**Type:** `RegExp`

Allows you to access a regex used for matching an input URL against a requested route.

For example, given a `[fruit]/about.astro` path, the regex will be `/^\/([^/]+?)\/about\/?$/`. Using `pattern.test("banana/about")` will return `true`.

#### `params`

[Section titled “params”](#params-1)

**Type:** `string[]`

Allows you to access the route `params`. For example, when a project uses the following [dynamic routes](/en/guides/routing/#dynamic-routes) `/pages/[lang]/[...slug].astro`, the value will be `['lang', '...slug']`.

#### `segments`

[Section titled “segments”](#segments-1)

**Type:** `{ content: string; dynamic: boolean; spread: boolean; }[][]`

Allows you to access the route [`params`](#params-1) with additional metadata. Each object contains the following properties:

* `content`: the `param`,
* `dynamic`: whether the route is dynamic or not,
* `spread`: whether the dynamic route uses the spread syntax or not.

For example, the following route `/pages/[lang]/index.astro` will output the segments `[[ { content: 'lang', dynamic: true, spread: false } ]]`.

#### `generate()`

[Section titled “generate()”](#generate-1)

**Type:** `(data?: any) => string`

A function that provides the optional parameters of the route, interpolates them with the route pattern, and returns the path name of the route.

For example, with a route such as `/blog/[...id].astro`, the `generate` function could return:

```js
console.log(generate({ id: 'presentation' })) // will log `/blog/presentation`
```

#### `prerender`

[Section titled “prerender”](#prerender)

**Type:** `boolean`

Determines whether the route is prerendered or not.

#### `distURL`

[Section titled “distURL”](#disturl)

**Type:** `URL[] | undefined`

The paths of the physical files emitted by this route. When a route **isn’t** prerendered, the value is either `undefined` or an empty array.

#### `redirect`

[Section titled “redirect”](#redirect-1)

**Type:** `RedirectConfig | undefined`

Allows you to access the route to redirect to. This can be a string or an object containing information about the status code and its destination.

#### `redirectRoute`

[Section titled “redirectRoute”](#redirectroute-1)

**Type:** `IntegrationRouteData | undefined`

When the value of `RouteData.type` is `redirect`, the value will contains the `IntegrationRouteData` of the route to redirect to. Otherwise, the value will be undefined.

## Allow installation with `astro add`

[Section titled “Allow installation with astro add”](#allow-installation-with-astro-add)

[The `astro add` command](/en/reference/cli-reference/#astro-add) allows users to easily add integrations and adapters to their project. If you want *your* integration to be installable with this tool, **add `astro-integration` to the `keywords` field in your `package.json`**:

```json
{
  "name": "example",
  "keywords": ["astro-integration"],
}
```

Once you [publish your integration to npm](https://docs.npmjs.com/cli/v8/commands/npm-publish), running `astro add example` will install your package with any peer dependencies specified in your `package.json`. This will also apply your integration to the user’s `astro.config.*` like so:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import example from 'example';


export default defineConfig({
+  integrations: [example()],
})
```

Caution

This assumes your integration definition is 1) a `default` export and 2) a function. Ensure this is true before adding the `astro-integration` keyword!

## Integration Ordering

[Section titled “Integration Ordering”](#integration-ordering)

All integrations are run in the order that they are configured. For instance, for the array `[react(), svelte()]` in a user’s `astro.config.*`, `react` will run before `svelte`.

Your integration should ideally run in any order. If this isn’t possible, we recommend documenting that your integration needs to come first or last in your user’s `integrations` configuration array.

## Combine integrations into presets

[Section titled “Combine integrations into presets”](#combine-integrations-into-presets)

An integration can also be written as a collection of multiple, smaller integrations. We call these collections **presets.** Instead of creating a factory function that returns a single integration object, a preset returns an *array* of integration objects. This is useful for building complex features out of multiple integrations.

```js
integrations: [
  // Example: where examplePreset() returns: [integrationOne, integrationTwo, ...etc]
  examplePreset()
]
```

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Build your own Astro Integrations](https://www.freecodecamp.org/news/how-to-use-the-astro-ui-framework/#chapter-8-build-your-own-astro-integrations-1) - by Emmanuel Ohans on FreeCodeCamp
* [Astro Integration Template](https://github.com/florian-lefebvre/astro-integration-template) - by Florian Lefebvre on GitHub

# Legacy flags

To help some users migrate between versions of Astro, we occasionally introduce `legacy` flags.

These flags allow you to opt in to some deprecated or otherwise outdated behavior of Astro in the latest version, so that you can continue to upgrade and take advantage of new Astro releases until you are able to fully update your project code.

## Collections

[Section titled “Collections”](#collections)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.0.0`

Enable legacy behavior for content collections (as used in Astro v2 through v4)

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
export default defineConfig({
  legacy: {
    collections: true
  }
});
```

If enabled, `data` and `content` collections (only) are handled using the legacy content collections implementation. Collections with a `loader` (only) will continue to use the Content Layer API instead. Both kinds of collections may exist in the same project, each using their respective implementations.

The following limitations continue to exist:

* Any legacy (`type: 'content'` or `type: 'data'`) collections must continue to be located in the `src/content/` directory.
* These legacy collections will not be transformed to implicitly use the `glob()` loader, and will instead be handled by legacy code.
* Collections using the Content Layer API (with a `loader` defined) are forbidden in `src/content/`, but may exist anywhere else in your project.

When you are ready to remove this flag and migrate to the new Content Layer API for your legacy collections, you must define a collection for any directories in `src/content/` that you want to continue to use as a collection. It is sufficient to declare an empty collection, and Astro will implicitly generate an appropriate definition for your legacy collections:

src/content/config.ts

```js
import { defineCollection, z } from 'astro:content';


const blog = defineCollection({ })


export const collections = { blog };
```

# Actions API Reference

**Added in:** `astro@4.15.0`

Actions help you build a type-safe backend you can call from client code and HTML forms. All utilities to define and call actions are exposed by the `astro:actions` module. For examples and usage instructions, [see the Actions guide](/en/guides/actions/).

## Imports from `astro:actions`

[Section titled “Imports from astro:actions”](#imports-from-astroactions)

```js
import {
  ACTION_QUERY_PARAMS,
  ActionError,
  actions,
  defineAction,
  getActionContext,
  getActionPath,
  isActionError,
  isInputError,
 } from 'astro:actions';
```

### `defineAction()`

[Section titled “defineAction()”](#defineaction)

**Type:** `({ accept, input, handler }) => ActionClient`

A utility to define new actions in the `src/actions/index.ts` file. This accepts a [`handler()`](#handler-property) function containing the server logic to run, and an optional [`input`](#input-validator) property to validate input parameters at runtime.

src/actions/index.ts

```ts
import { defineAction } from 'astro:actions';
import { z } from 'astro:schema';


export const server = {
  getGreeting: defineAction({
    input: z.object({
      name: z.string(),
    }),
    handler: async (input, context) => {
      return `Hello, ${input.name}!`
    }
  })
}
```

#### `handler()` property

[Section titled “handler() property”](#handler-property)

**Type:** `(input: TInputSchema, context: ActionAPIContext) => TOutput | Promise<TOutput>`

A required function containing the server logic to run when the action is called. Data returned from the `handler()` is automatically serialized and sent to the caller.

The `handler()` is called with user input as its first argument. If an [`input`](#input-validator) validator is set, the user input will be validated before being passed to the handler. The second argument is [a subset of Astro’s `context` object](#actionapicontext).

Return values are parsed using the [devalue library](https://github.com/Rich-Harris/devalue). This supports JSON values and instances of `Date()`, `Map()`, `Set()`, and `URL()`.

#### `input` validator

[Section titled “input validator”](#input-validator)

**Type:** `ZodType | undefined`

An optional property that accepts a Zod validator (e.g. Zod object, Zod discriminated union) to validate handler inputs at runtime. If the action fails to validate, [a `BAD_REQUEST` error](#actionerror) is returned and the `handler` is not called.

If `input` is omitted, the `handler` will receive an input of type `unknown` for JSON requests and type `FormData` for form requests.

#### `accept` property

[Section titled “accept property”](#accept-property)

**Type:** `"form" | "json"`\
**Default:** `json`

Defines the format expected by an action:

* Use `form` when your action accepts `FormData`.
* Use `json`, the default, for all other cases.

When your action accepts form inputs, the `z.object()` validator will automatically parse `FormData` to a typed object. All Zod validators are supported to validate your inputs.

Learn about [using validators with form inputs](/en/guides/actions/#using-validators-with-form-inputs) in the Actions guide, including example usage and special input handling.

### `actions`

[Section titled “actions”](#actions)

**Type:** `Record<string, ActionClient>`

An object containing all your actions with the action name as key associated to a function to call this action.

src/pages/index.astro

```astro
---
---


<script>
import { actions } from 'astro:actions';


async () => {
  const { data, error } = await actions.myAction({ /* ... */ });
}
</script>
```

In order for Astro to recognize this property, you may need to restart the dev server or [run the `astro sync` command](/en/reference/cli-reference/#astro-sync) (`s + enter`).

### `isInputError()`

[Section titled “isInputError()”](#isinputerror)

**Type:** `(error?: unknown) => boolean`

A utility used to check whether [an `ActionError`](#actionerror) is an input validation error. When the `input` validator is a `z.object()`, input errors include a `fields` object with error messages grouped by name.

See the [form input errors guide](/en/guides/actions/#displaying-form-input-errors) for more on using `isInputError()`.

### `isActionError()`

[Section titled “isActionError()”](#isactionerror)

**Type:** `(error?: unknown) => boolean`

A utility to check whether your action raised [an `ActionError`](#actionerror) within the [handler property](#handler-property). This is useful when narrowing the type of a generic error.

src/pages/index.astro

```astro
---
---


<script>
import { isActionError, actions } from 'astro:actions';


async () => {
  const { data, error } = await actions.myAction({ /* ... */ });
  if (isActionError(error)) {
    // Handle action-specific errors
    console.log(error.code);
  }
}
</script>
```

### `ActionError`

[Section titled “ActionError”](#actionerror)

The `ActionError()` constructor is used to create errors thrown by an action `handler`. This accepts a `code` property describing the error that occurred (example: `"UNAUTHORIZED"`), and an optional `message` property with further details.

The following example creates a new `ActionError` when the user is not logged in:

src/actions/index.ts

```ts
import { defineAction, ActionError } from "astro:actions";


export const server = {
  getUserOrThrow: defineAction({
    accept: 'form',
    handler: async (_, { locals }) => {
      if (locals.user?.name !== 'florian') {
        throw new ActionError({
          code: 'UNAUTHORIZED',
          message: 'Not logged in',
        });
      }
      return locals.user;
    },
  }),
}
```

You can also use `ActionError` to narrow the error type when handling the results of an action:

src/pages/index.astro

```astro
---
---


<script>
import { ActionError, actions } from 'astro:actions';


async () => {
  const { data, error } = await actions.myAction({ /* ... */ });
  if (error instanceof ActionError) {
    // Handle action-specific errors
    console.log(error.code);
  }
}
</script>
```

#### `code`

[Section titled “code”](#code)

**Type:** `ActionErrorCode`

Defines a human-readable version of an [HTTP status code](#actionerrorcode).

#### `message`

[Section titled “message”](#message)

**Type:** `string`

An optional property to describe the error (e.g. “User must be logged in.”).

#### `stack`

[Section titled “stack”](#stack)

**Type:** `string`

An optional property to pass the stack trace.

### `getActionContext()`

[Section titled “getActionContext()”](#getactioncontext)

**Type:** `(context: APIContext) => AstroActionContext`

**Added in:** `astro@5.0.0`

A function called from your middleware handler to retrieve information about inbound action requests. This returns an `action` object with information about the request, a `deserializeActionResult()` method, and the `setActionResult()` and `serializeActionResult()` functions to programmatically set the value returned by `Astro.getActionResult()`.

`getActionContext()` lets you programmatically get and set action results using middleware, allowing you to persist action results from HTML forms, gate action requests with added security checks, and more.

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  const { action, setActionResult, serializeActionResult } = getActionContext(context);
  if (action?.calledFrom === 'form') {
    const result = await action.handler();
    setActionResult(action.name, serializeActionResult(result));
  }
  return next();
});
```

#### `action`

[Section titled “action”](#action)

**Type:** `{ calledFrom: “rpc” | “form”; name: string; handler: () => Promise<SafeResult>; } | undefined`

An object containing information about an inbound action request. It is available from [`getActionContext()`](#getactioncontext), and provides the action `name`, `handler`, and whether the action was called from a client-side RPC function (e.g. `actions.newsletter()`) or an HTML form action.

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  const { action, setActionResult, serializeActionResult } = getActionContext(context);
  if (action?.calledFrom === 'rpc' && action.name.startsWith('private')) {
    // Check for a valid session token
  }
  // ...
});
```

##### `calledFrom`

[Section titled “calledFrom”](#calledfrom)

**Type:** `"rpc" | "form"`

Whether an action was called using an RPC function or an HTML form action.

##### `name`

[Section titled “name”](#name)

**Type:** `string`

The name of the action. Useful to track the source of an action result during a redirect.

##### `handler()`

[Section titled “handler()”](#handler)

**Type:** `() => Promise<SafeResult>`

A method to programmatically call an action to get the result.

#### `setActionResult()`

[Section titled “setActionResult()”](#setactionresult)

**Type:** `(actionName: string, actionResult: SerializedActionResult) => void`

A function to programmatically set the value returned by `Astro.getActionResult()` in middleware. It is passed the action name and an action result serialized by [`serializeActionResult()`](#serializeactionresult). Calling this function from middleware will disable Astro’s own action result handling.

This is useful when calling actions from an HTML form to persist and load results from a session.

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';
export const onRequest = defineMiddleware(async (context, next) => {
  const { action, setActionResult, serializeActionResult } = getActionContext(context);
  if (action?.calledFrom === 'form') {
    const result = await action.handler();
    // ... handle the action result
    setActionResult(action.name, serializeActionResult(result));
  }
  return next();
});
```

See the [advanced sessions guide](/en/guides/actions/#advanced-persist-action-results-with-a-session) for a sample implementation using Netlify Blob.

#### `serializeActionResult()`

[Section titled “serializeActionResult()”](#serializeactionresult)

**Type:** `(res: SafeResult) => SerializedActionResult`

Serializes an action result to JSON for persistence. This is required to properly handle non-JSON return values like `Map` or `Date` as well as the `ActionError` object.

Call this function when serializing an action result to be passed to `setActionResult()`:

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  const { action, setActionResult, serializeActionResult } = getActionContext(context);
  if (action) {
    const result = await action.handler();
    setActionResult(action.name, serializeActionResult(result));
  }
  // ...
});
```

#### `deserializeActionResult()`

[Section titled “deserializeActionResult()”](#deserializeactionresult)

**Type:** `(res: SerializedActionResult) => SafeResult`

Reverses the effect of [`serializeActionResult()`](#serializeactionresult) and returns an action result to its original state. This is useful to access the `data` and `error` objects on a serialized action result.

### `getActionPath()`

[Section titled “getActionPath()”](#getactionpath)

**Type:** `(action: ActionClient) => string`

**Added in:** `astro@5.1.0`

A utility that accepts an action and returns a URL path so you can execute an action call as a `fetch()` operation directly. This allows you to provide details such as custom headers when you call your action. Then, you can [handle the custom-formatted returned data](/en/guides/actions/#handling-returned-data) as needed, just as if you had called an action directly.

This example shows how to call a defined `like` action passing the `Authorization` header and the [`keepalive`](https://developer.mozilla.org/en-US/docs/Web/API/Request/keepalive) option:

src/components/my-component.astro

```astro
<script>
import { actions, getActionPath } from 'astro:actions'


await fetch(getActionPath(actions.like), {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Authorization: 'Bearer YOUR_TOKEN'
  },
  body: JSON.stringify({ id: 'YOUR_ID' }),
  keepalive: true
})
</script>
```

This example shows how to call the same `like` action using the [`sendBeacon`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/sendBeacon) API:

src/components/my-component.astro

```astro
<script>
import { actions, getActionPath } from 'astro:actions'


navigator.sendBeacon(
  getActionPath(actions.like),
  new Blob([JSON.stringify({ id: 'YOUR_ID' })], {
    type: 'application/json'
  })
)
</script>
```

### `ACTION_QUERY_PARAMS`

[Section titled “ACTION\_QUERY\_PARAMS”](#action_query_params)

**Type:** `{ actionName: string, actionPayload: string }`

An object containing the query parameter names used internally by Astro when handling form action submissions.

When you submit a form using an action, the following query parameters are added to the URL to track the action call:

* `actionName` - The query parameter that contains the name of the action being called
* `actionPayload` - The query parameter that contains the serialized form data

This constant can be useful when you need to clean up URLs after a form submission. For example, you might want to remove action-related query parameters during a redirect:

src/pages/api/contact.ts

```ts
import type { APIRoute } from "astro";
import { ACTION_QUERY_PARAMS } from 'astro:actions'


export const GET: APIRoute = ({ params, request }) => {
  const link = request.url.searchParams;
  link.delete(ACTION_QUERY_PARAMS.actionName);
  link.delete(ACTION_QUERY_PARAMS.actionPayload);


  return redirect(link, 303);
};
```

## `astro:actions` types

[Section titled “astro:actions types”](#astroactions-types)

```ts
import type {
  ActionAPIContext,
  ActionClient,
  ActionErrorCode,
  ActionReturnType,
  SafeResult,
 } from 'astro:actions';
```

### `ActionAPIContext`

[Section titled “ActionAPIContext”](#actionapicontext)

A subset of the [Astro context object](/en/reference/api-reference/). The following properties are not available: `callAction`, `getActionResult`, `props`, and `redirect`.

### `ActionClient`

[Section titled “ActionClient”](#actionclient)

**Types:**

* `(input?: any) => Promise<SafeResult>`
* `{ queryString?: string; orThrow: (input?: any) => Promise<Awaited<TOutput>>; }`

Represents an action to be called on the client. You can use it as a function that accepts input data and returns a Promise with a [`SafeResult` object](#saferesult) containing the action result or validation errors.

The following example shows how you can provide error handling with an `if` statement when incrementing the like count fails:

src/pages/posts/post-1.astro

```astro
---
---


<!-- your template -->


<script>
import { actions } from 'astro:actions';


const post = document.querySelector('article');
const button = document.querySelector('button');
button?.addEventListener('click', async () => {
  const { data: updatedLikes, error } = await actions.likePost({ postId: post?.id });
  if (error) {
    /* handle errors */
  }
})
</script>
```

Alternatively, you can use it as an object giving you access to the `queryString` and an alternative `orThrow()` method.

#### `queryString` property

[Section titled “queryString property”](#querystring-property)

**Type:** `string`

A string representation of the action that can be used to construct form action URLs. This can be useful when your form component is used in multiple places but you need to redirect to a different URL on submit.

The following example uses `queryString` to construct a URL that will be passed to the form `action` attribute through a custom prop:

src/pages/postal-service.astro

```astro
---
import { actions } from 'astro:actions';
import FeedbackForm from "../components/FeedbackForm.astro";


const feedbackUrl = new URL('/feedback', Astro.url);
feedbackUrl.search = actions.myAction.queryString;
---
<FeedbackForm sendTo={feedbackUrl.pathname} />
```

#### `orThrow()` property

[Section titled “orThrow() property”](#orthrow-property)

**Type:** `(input?: any) => Promise<Awaited<TOutput>>`

A method that throws an error on failure instead of returning the errors. This is useful when you want exceptions rather than error handling.

The following example uses `orThrow()` to skip error handling when incrementing the like count fails:

src/pages/posts/post-1.astro

```astro
---
---


<!-- your template -->


<script>
import { actions } from 'astro:actions';


const post = document.querySelector('article');
const button = document.querySelector('button');
button?.addEventListener('click', async () => {
  const updatedLikes = await actions.likePost.orThrow({ postId: post?.id });
})
</script>
```

### `ActionErrorCode`

[Section titled “ActionErrorCode”](#actionerrorcode)

**Type:** `string`

A union type of standard HTTP status codes [defined by IANA](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) using the human-readable versions as uppercase strings separated by an underscore (e.g. `BAD_REQUEST` or `PAYLOAD_TOO_LARGE`).

### `ActionReturnType`

[Section titled “ActionReturnType”](#actionreturntype)

**Type:** `Awaited<ReturnType<ActionHandler>>`

A utility type that extracts the output type from [an action handler](#defineaction). This unwraps both the `Promise` (if the handler is async) and the `ReturnType` to give you the [actual output type](#saferesult). This can be useful if you need to reference an action’s output type in your own type definitions.

The following example uses `ActionReturnType` to retrieve the expected output type for an action named `contact`:

src/components/Form.astro

```astro
---
import { actions, ActionReturnType } from 'astro:actions';


type ContactResult = ActionReturnType<typeof actions.contact>;
---
```

### `SafeResult`

[Section titled “SafeResult”](#saferesult)

**Type:** `{ data: TOutput, error: undefined } | { data: undefined, error: ActionError }`

Represents the result of an action call:

* on success, `data` contains the output of the action and `error` is `undefined`.
* on failure, `error` contains an [`ActionError`](#actionerror) with validation errors or runtime errors, and `data` is `undefined`.

# Image and Assets API Reference

**Added in:** `astro@3.0.0`

Astro provides built-in components and helper functions for optimizing and displaying your images. For features and usage examples, [see our image guide](/en/guides/images/).

## Imports from `astro:assets`

[Section titled “Imports from astro:assets”](#imports-from-astroassets)

```js
import {
  Image,
  Picture,
  getImage,
  inferRemoteSize,
 } from 'astro:assets';
```

### `<Image />`

[Section titled “\<Image />”](#image-)

The `<Image />` component optimizes and transforms images.

This component can also be used to create [responsive images](#responsive-image-properties) that can adjust based on the size of their container or a device screen size and resolution.

src/components/MyComponent.astro

```astro
---
// import the Image component and the image
import { Image } from 'astro:assets';
import myImage from "../assets/my_image.png"; // Image is 1600x900
---


<!-- `alt` is mandatory on the Image component -->
<Image src={myImage} alt="A description of my image." />
```

```html
<!-- Output -->
<!-- Image is optimized, proper attributes are enforced -->
<img
  src="/_astro/my_image.hash.webp"
  width="1600"
  height="900"
  decoding="async"
  loading="lazy"
  alt="A description of my image."
/>
```

#### Image properties

[Section titled “Image properties”](#image-properties)

The `<Image />` component accepts the following listed properties and [responsive image properties](#responsive-image-properties) in addition to all properties accepted by the HTML `<img>` tag.

##### src (required)

[Section titled “src (required)”](#src-required)

**Type:** `ImageMetadata | string | Promise<{ default: ImageMetadata }>`

The format of the `src` value of your image file depends on where your image file is located:

* **Local images in `src/`** - you must **also import the image** using a relative file path or configure and use an [import alias](/en/guides/imports/#aliases). Then use the import name as the `src` value:

  src/pages/index.astro

  ```astro
  ---
  import { Image } from 'astro:assets';
  import myImportedImage from '../assets/my-local-image.png';
  ---
  <Image src={myImportedImage} alt="descriptive text" />
  ```

* **Images in the `public/` folder** - use the image’s **file path relative to the public folder**:

  src/pages/index.astro

  ```astro
  ---
  import { Image } from 'astro:assets';
  ---
  <Image
    src="/images/my-public-image.png"
    alt="descriptive text"
    width="200"
    height="150"
  />
  ```

* **Remote images** - use the image’s **full URL** as the property value:

  src/pages/index.astro

  ```astro
  ---
  import { Image } from 'astro:assets';
  ---
  <Image
    src="https://example.com/remote-image.jpg"
    alt="descriptive text"
    width="200"
    height="150"
  />
  ```

##### alt (required)

[Section titled “alt (required)”](#alt-required)

**Type:** `string`

Use the required `alt` attribute to provide a string of [descriptive alt text](https://www.w3.org/WAI/tutorials/images/) for images.

If an image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers and other assistive technologies know to ignore the image.

##### width and height (required for images in `public/`)

[Section titled “width and height (required for images in public/)”](#width-and-height-required-for-images-in-public)

**Type:** `number | undefined`

These properties define the dimensions to use for the image.

When a `layout` type is set, these are automatically generated based on the image’s dimensions and in most cases should not be set manually.

When using images in their original aspect ratio, `width` and `height` are optional. These dimensions can be automatically inferred from image files located in `src/`. For remote images, add [the `inferSize` attribute set to `true`](#infersize) on the `<Image />` or `<Picture />` component or use [`inferRemoteSize()` function](#inferremotesize).

However, both of these properties are required for images stored in your `public/` folder as Astro is unable to analyze these files.

##### densities

[Section titled “densities”](#densities)

**Type:** ``(number | `${number}x`)[] | undefined``

**Added in:** `astro@3.3.0`

A list of pixel densities to generate for the image.

The `densities` attribute is not compatible with [responsive images](#responsive-image-properties) with a `layout` prop or `image.layout` config set, and will be ignored if set.

If provided, this value will be used to generate a `srcset` attribute on the `<img>` tag. Do not provide a value for `widths` when using this value.

Densities that are equal to widths larger than the original image will be ignored to avoid upscaling the image.

src/components/MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---
<Image
  src={myImage}
  width={myImage.width / 2}
  densities={[1.5, 2]}
  alt="A description of my image."
/>
```

```html
<!-- Output -->
<img
  src="/_astro/my_image.hash.webp"
  srcset="
    /_astro/my_image.hash.webp 1.5x
    /_astro/my_image.hash.webp 2x
  "
  alt="A description of my image."
  width="800"
  height="450"
  loading="lazy"
  decoding="async"
/>
```

##### widths

[Section titled “widths”](#widths)

**Type:** `number[] | undefined`

**Added in:** `astro@3.3.0`

A list of widths to generate for the image.

If provided, this value will be used to generate a `srcset` attribute on the `<img>` tag. A [`sizes` property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/sizes) must also be provided.

The `widths` and `sizes` attributes will be automatically generated for responsive images using a `layout` property. Providing these values is generally not needed, but can be used to override any automatically generated values.

Do not provide a value for `densities` when using this value. Only one of these two values can be used to generate a `srcset`.

Widths that are larger than the original image will be ignored to avoid upscaling the image.

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png'; // Image is 1600x900
---
<Image
  src={myImage}
  widths={[240, 540, 720, myImage.width]}
  sizes={`(max-width: 360px) 240px, (max-width: 720px) 540px, (max-width: 1600px) 720px, ${myImage.width}px`}
  alt="A description of my image."
/>
```

```html
<!-- Output -->
<img
  src="/_astro/my_image.hash.webp"
  srcset="
    /_astro/my_image.hash.webp 240w,
    /_astro/my_image.hash.webp 540w,
    /_astro/my_image.hash.webp 720w,
    /_astro/my_image.hash.webp 1600w
  "
  sizes="
    (max-width: 360px) 240px,
    (max-width: 720px) 540px,
    (max-width: 1600px) 720px,
    1600px
  "
  alt="A description of my image."
  width="1600"
  height="900"
  loading="lazy"
  decoding="async"
/>
```

##### sizes

[Section titled “sizes”](#sizes)

**Type:** `string | undefined`

**Added in:** `astro@3.3.0`

Specifies the layout width of the image for each of a list of media conditions. Must be provided when specifying `widths`.

The `widths` and `sizes` attributes will be automatically generated for responsive images using a `layout` property. Providing these values is generally not needed, but can be used to override any automatically generated values.

The generated `sizes` attribute for `constrained` and `full-width` images is based on the assumption that the image is displayed close to the full width of the screen when the viewport is smaller than the image’s width. If it is significantly different (e.g. if it’s in a multi-column layout on small screens), you may need to adjust the `sizes` attribute manually for best results.

##### format

[Section titled “format”](#format)

**Type:** `ImageOutputFormat | undefined`

You can optionally state the [image file type](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types#common_image_file_types) output to be used.

By default, the `<Image />` component will produce a `.webp` file.

##### quality

[Section titled “quality”](#quality)

**Type:** `ImageQuality | undefined`

`quality` is an optional property that can either be:

* a preset (`low`, `mid`, `high`, `max`) that is automatically normalized between formats.
* a number from `0` to `100` (interpreted differently between formats).

##### inferSize

[Section titled “inferSize”](#infersize)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@4.4.0`

Allows you to set the original `width` and `height` of a remote image automatically.

By default, this value is set to `false` and you must manually specify both dimensions for your remote image.

Add `inferSize` to the `<Image />` component (or `inferSize: true` to `getImage()`) to infer these values from the image content when fetched. This is helpful if you don’t know the dimensions of the remote image, or if they might change:

src/components/MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
---
<Image src="https://example.com/cat.png" inferSize alt="A cat sleeping in the sun." />
```

`inferSize` can fetch the dimensions of a [remote image from a domain that has not been authorized](/en/guides/images/#authorizing-remote-images), however the image itself will remain unprocessed.

##### priority

[Section titled “priority”](#priority)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.10.0`

Allows you to automatically set the `loading`, `decoding`, and `fetchpriority` attributes to their optimal values for above-the-fold images.

src/components/MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---
<Image src={myImage} priority alt="A description of my image" />
```

When `priority="true"` (or the shorthand syntax `priority`) is added to the `<Image />` or `<Picture />` component, it will add the following attributes to instruct the browser to load the image immediately:

```html
loading="eager"
decoding="sync"
fetchpriority="high"
```

These individual attributes can still be set manually if you need to customize them further.

### `<Picture />`

[Section titled “\<Picture />”](#picture-)

**Added in:** `astro@3.3.0`

The `<Picture />` component generates an optimized image with multiple formats and/or sizes.

This component can also be used to create [responsive images](#responsive-image-properties) that can adjust based on the size of their container or a device screen size and resolution.

src/pages/index.astro

```astro
---
import { Picture } from 'astro:assets';
import myImage from "../assets/my_image.png"; // Image is 1600x900
---


<!-- `alt` is mandatory on the Picture component -->
<Picture src={myImage} formats={['avif', 'webp']} alt="A description of my image." />
```

```html
<!-- Output -->
<picture>
  <source srcset="/_astro/my_image.hash.avif" type="image/avif" />
  <source srcset="/_astro/my_image.hash.webp" type="image/webp" />
  <img
    src="/_astro/my_image.hash.png"
    width="1600"
    height="900"
    decoding="async"
    loading="lazy"
    alt="A description of my image."
  />
</picture>
```

#### Picture properties

[Section titled “Picture properties”](#picture-properties)

`<Picture />` accepts all the properties of [the `<Image />` component](#image-properties), including [responsive image properties](#responsive-image-properties), plus the following:

##### `formats`

[Section titled “formats”](#formats)

**Type:** `ImageOutputFormat[]`

An array of image formats to use for the `<source>` tags. Entries will be added as `<source>` elements in the order they are listed, and this order determines which format is displayed. For the best performance, list the most modern format first (e.g. `webp` or `avif`). By default, this is set to `['webp']`.

##### `fallbackFormat`

[Section titled “fallbackFormat”](#fallbackformat)

**Type:** `ImageOutputFormat`

Format to use as a fallback value for the `<img>` tag. Defaults to `.png` for static images (or `.jpg` if the image is a JPG), `.gif` for animated images, and `.svg` for SVG files.

##### `pictureAttributes`

[Section titled “pictureAttributes”](#pictureattributes)

**Type:** `HTMLAttributes<'picture'>`

An object of attributes to be added to the `<picture>` tag.

Use this property to apply attributes to the outer `<picture>` element itself. Attributes applied to the `<Picture />` component directly will apply to the inner `<img>` element, except for those used for image transformation.

src/components/MyComponent.astro

```astro
---
import { Picture } from "astro:assets";
import myImage from "../my_image.png"; // Image is 1600x900
---


<Picture
  src={myImage}
  alt="A description of my image."
  pictureAttributes={{ style: "background-color: red;" }}
/>
```

```html
<!-- Output -->
<picture style="background-color: red;">
  <source srcset="/_astro/my_image.hash.webp" type="image/webp" />
  <img
    src="/_astro/my_image.hash.png"
    alt="A description of my image."
    width="1600"
    height="900"
    loading="lazy"
    decoding="async"
  />
</picture>
```

### Responsive image properties

[Section titled “Responsive image properties”](#responsive-image-properties)

Setting the [`layout`](#layout) property on an [`<Image />`](#image-) or [`<Picture />`](#picture-) component creates a responsive image and enables additional property settings.

MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---
<Image src={myImage} alt="A description of my image." layout='constrained' width={800} height={600} />
```

When a layout is set, `srcset` and `sizes` attributes are automatically generated based on the image’s dimensions and the layout type. The previous `<Image />` component will generate the following HTML output:

```html
<img
  src="/_astro/my_image.hash3.webp"
  srcset="/_astro/my_image.hash1.webp 640w,
      /_astro/my_image.hash2.webp 750w,
      /_astro/my_image.hash3.webp 800w,
      /_astro/my_image.hash4.webp 828w,
      /_astro/my_image.hash5.webp 1080w,
      /_astro/my_image.hash6.webp 1280w,
      /_astro/my_image.hash7.webp 1600w"
  alt="A description of my image"
  sizes="(min-width: 800px) 800px, 100vw"
  loading="lazy"
  decoding="async"
  fetchpriority="auto"
  width="800"
  height="600"
  style="--fit: cover; --pos: center;"
  data-astro-image="constrained"
>
```

The value for `layout` also defines the default styles applied to the `<img>` tag to determine how the image should resize according to its container:

Responsive Image Styles

```css
:where([data-astro-image]) {
  object-fit: var(--fit);
  object-position: var(--pos);
}
:where([data-astro-image='full-width']) {
  width: 100%;
}
:where([data-astro-image='constrained']) {
  max-width: 100%;
}
```

You can override the default `object-fit` and `object-position` styles by setting the [`fit`](#fit) and [`position`](#position) props on the `<Image />` or `<Picture />` component.

##### layout

[Section titled “layout”](#layout)

**Type:** `'constrained' | 'full-width' | 'fixed' | 'none'`\
**Default:** `image.layout | 'none'`

**Added in:** `astro@5.10.0`

Defines a [responsive image](#responsive-image-properties) and determines how the image should resize when its container changes size. Can be used to override the default configured value for [`image.layout`](/en/reference/configuration-reference/#imagelayout).

* `constrained` - The image will scale down to fit the container, maintaining its aspect ratio, but will not scale up beyond the specified `width` and `height`, or the image’s original dimensions.

  Use this if you want the image to display at the requested size where possible, but shrink to fit smaller screens. This matches the default behavior for images when using Tailwind. If you’re not sure, this is probably the layout you should choose.

* `full-width` - The image will scale to fit the width of the container, maintaining its aspect ratio.

  Use this for hero images or other images that should take up the full width of the page.

* `fixed` - The image will maintain the requested dimensions and not resize. It will generate a `srcset` to support high density displays, but not for different screen sizes.

  Use this if the image will not resize, for example icons or logos smaller than any screen width, or other images in a fixed-width container.

* `none` - The image will not be responsive. No `srcset` or `sizes` will be automatically generated, and no styles will be applied.

  This is useful if you have enabled a default layout, but want to disable it for a specific image.

For example, with `constrained` set as the default layout, you can override any individual image’s `layout` property:

src/components/MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---
<Image src={myImage} alt="This will use constrained layout" width={800} height={600} />
<Image src={myImage} alt="This will use full-width layout" layout="full-width" />
<Image src={myImage} alt="This will disable responsive images" layout="none" />
```

##### fit

[Section titled “fit”](#fit)

**Type:** `'contain' | 'cover' | 'fill' | 'none' | 'scale-down'`\
**Default:** `image.objectFit | 'cover'`

**Added in:** `astro@5.10.0`

Enabled when the [`layout`](#layout) property is set or configured. Defines how a responsive image should be cropped if its aspect ratio is changed.

Values match those of CSS `object-fit`. Defaults to `cover`, or the value of [`image.objectFit`](/en/reference/configuration-reference/#imageobjectfit) if set. Can be used to override the default `object-fit` styles.

##### position

[Section titled “position”](#position)

**Type:** `string`\
**Default:** `image.objectPosition | 'center'`

**Added in:** `astro@5.10.0`

Enabled when the [`layout`](#layout) property is set or configured. Defines the position of the image crop for a responsive image if the aspect ratio is changed.

Values match those of CSS `object-position`. Defaults to `center`, or the value of [`image.objectPosition`](/en/reference/configuration-reference/#imageobjectposition) if set. Can be used to override the default `object-position` styles.

### `getImage()`

[Section titled “getImage()”](#getimage)

**Type:** `(options: UnresolvedImageTransform) => Promise<GetImageResult>`

Caution

`getImage()` relies on server-only APIs and breaks the build when used on the client.

The `getImage()` function is intended for generating images destined to be used somewhere else than directly in HTML, for example in an [API Route](/en/guides/endpoints/#server-endpoints-api-routes). It also allows you to create your own custom `<Image />` component.

`getImage()` takes an options object with the [same properties as the Image component](#image-properties) (except `alt`).

```astro
---
import { getImage } from "astro:assets";
import myBackground from "../background.png"


const optimizedBackground = await getImage({src: myBackground, format: 'avif'})
---


<div style={`background-image: url(${optimizedBackground.src});`}></div>
```

It returns an object with the following type:

```ts
type GetImageResult = {
  /* Additional HTML attributes needed to render the image (width, height, style, etc..) */
  attributes: Record<string, any>;
  /* Validated parameters passed */
  options: ImageTransform;
  /* Original parameters passed */
  rawOptions: ImageTransform;
  /* Path to the generated image */
  src: string;
  srcSet: {
    /* Generated values for srcset, every entry has a url and a size descriptor */
    values: SrcSetValue[];
    /* A value ready to use in`srcset` attribute */
    attribute: string;
  };
}
```

### inferRemoteSize()

[Section titled “inferRemoteSize()”](#inferremotesize)

**Type:** `(url: string) => Promise<Omit<ImageMetadata, 'src' | 'fsPath'>>`

**Added in:** `astro@4.12.0`

A function to infer the dimensions of remote images. This can be used as an alternative to passing the `inferSize` property.

```ts
import { inferRemoteSize } from 'astro:assets';
const {width, height} = await inferRemoteSize("https://example.com/cat.png");
```

# Config imports API Reference

**Added in:** `astro@5.7.0`

This virtual module `astro:config` exposes a non-exhaustive, serializable, type-safe version of the Astro configuration. There are two submodules for accessing different subsets of your configuration values: [`/client`](#imports-from-astroconfigclient) and [`/server`](#imports-from-astroconfigserver).

All available config values can be accessed from `astro:config/server`. However, for code executed on the client, only those values exposed by `astro:config/client` will be available. This protects your information by only making some data available to the client.

## Imports from `astro:config/client`

[Section titled “Imports from astro:config/client”](#imports-from-astroconfigclient)

```js
import {
  i18n,
  trailingSlash,
  base,
  build,
  site,
} from "astro:config/client";
```

Use this submodule for client-side code:

src/utils.js

```diff
+import { trailingSlash } from "astro:config/client";


function addForwardSlash(path) {
  if (trailingSlash === "always") {
    return path.endsWith("/") ? path : path + "/"
  } else {
    return path
  }
}
```

See more about the configuration imports available from `astro:config/client`:

* [`i18n`](/en/reference/configuration-reference/#i18n)
* [`trailingSlash`](/en/reference/configuration-reference/#trailingslash)
* [`base`](/en/reference/configuration-reference/#base)
* [`build.format`](/en/reference/configuration-reference/#buildformat)
* [`site`](/en/reference/configuration-reference/#site)

## Imports from `astro:config/server`

[Section titled “Imports from astro:config/server”](#imports-from-astroconfigserver)

```js
import {
  i18n,
  trailingSlash,
  base,
  build,
  site,
  srcDir,
  cacheDir,
  outDir,
  publicDir,
  root,
} from "astro:config/server";
```

These imports include everything available from `astro:config/client` as well as additional sensitive information about your file system configuration that is not safe to expose to the client.

Use this submodule for server side code:

astro.config.mjs

```js
import { integration } from "./integration.mjs";


export default defineConfig({
    integrations: [
      integration(),
    ]
});
```

integration.mjs

```diff
+import { outDir } from "astro:config/server";
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";


export default function() {
  return {
    name: "internal-integration",
    hooks: {
      "astro:build:done": () => {
        let file = new URL("result.json", outDir);
        // generate data from some operation
        let data = JSON.stringify([]);
        writeFileSync(fileURLToPath(file), data, "utf-8");
      }
    }
  }
}
```

See more about the configuration imports available from `astro:config/server`:

* [`i18n`](/en/reference/configuration-reference/#i18n)
* [`trailingSlash`](/en/reference/configuration-reference/#trailingslash)
* [`base`](/en/reference/configuration-reference/#base)
* [`build.format`](/en/reference/configuration-reference/#buildformat)
* [`build.client`](/en/reference/configuration-reference/#buildclient)
* [`build.server`](/en/reference/configuration-reference/#buildserver)
* [`build.serverEntry`](/en/reference/configuration-reference/#buildserverentry)
* [`build.assetsPrefix`](/en/reference/configuration-reference/#buildassetsprefix)
* [`site`](/en/reference/configuration-reference/#site)
* [`srcDir`](/en/reference/configuration-reference/#srcdir)
* [`cacheDir`](/en/reference/configuration-reference/#cachedir)
* [`outDir`](/en/reference/configuration-reference/#outdir)
* [`publicDir`](/en/reference/configuration-reference/#publicdir)
* [`root`](/en/reference/configuration-reference/#root)

# Content Collections API Reference

**Added in:** `astro@2.0.0`

Content collections offer APIs to configure and query your Markdown or MDX documents in `src/content/`. For features and usage examples, [see our content collections guide](/en/guides/content-collections/).

## Imports from `astro:content`

[Section titled “Imports from astro:content”](#imports-from-astrocontent)

```js
import {
  z,
  defineCollection,
  getCollection,
  getEntry,
  getEntries,
  reference,
  render
 } from 'astro:content';
```

### `defineCollection()`

[Section titled “defineCollection()”](#definecollection)

**Type:** `(input: CollectionConfig) => CollectionConfig`

**Added in:** `astro@2.0.0`

`defineCollection()` is a utility to configure a collection in a `src/content.config.*` file.

src/content.config.ts

```ts
import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';


const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/data/blog' }),
  schema: z.object({
    title: z.string(),
    permalink: z.string().optional(),
  }),
});


// Expose your defined collection to Astro
// with the `collections` export
export const collections = { blog };
```

This function accepts the following properties:

#### `loader`

[Section titled “loader”](#loader)

**Type:** `() => Promise<Array<{ id: string, [key: string]: any }> | Record<string, Record<string, any>>> | Loader`

**Added in:** `astro@5.0.0`

A `loader` is either an object or a function that allows you to load data from any source, local or remote, into content collections.

[See the `Content Collection` guide](/en/guides/content-collections/#defining-the-collection-loader) for example usage.

#### `schema`

[Section titled “schema”](#schema)

**Type:** `ZodType | (context: SchemaContext) => ZodType`

**Added in:** `astro@2.0.0`

`schema` is an optional Zod object to configure the type and shape of document frontmatter for a collection. Each value must use [a Zod validator](https://github.com/colinhacks/zod).

[See the `Content Collection` guide](/en/guides/content-collections/#defining-the-collection-schema) for example usage.

### `reference()`

[Section titled “reference()”](#reference)

**Type:** `(collection: string) => ZodEffects<ZodString, { collection, id: string }>`

**Added in:** `astro@2.5.0`

The `reference()` function is used in the content config to define a relationship, or “reference,” from one collection to another. This accepts a collection name and transforms the reference into an object containing the collection name and the reference id.

This example defines references from a blog author to the `authors` collection and an array of related posts to the same `blog` collection:

```ts
import { defineCollection, reference, z } from 'astro:content';
import { glob, file } from 'astro/loaders';


const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/data/blog' }),
  schema: z.object({
    // Reference a single author from the `authors` collection by `id`
    author: reference('authors'),
    // Reference an array of related posts from the `blog` collection by `slug`
    relatedPosts: z.array(reference('blog')),
  })
});


const authors = defineCollection({
  loader: file("src/data/authors.json"),
  schema: z.object({ /* ... */ })
});


export const collections = { blog, authors };
```

Validation of referenced entries happens at runtime when using `getEntry()` or `getEntries()`:

src/pages/\[posts].astro

```astro
// if a referenced entry is invalid, this will return undefined.
const relatedPosts = await getEntries(blogPost.data.relatedPosts);
```

[See the `Content Collection` guide](/en/guides/content-collections/#defining-collection-references) for example usage.

### `getCollection()`

[Section titled “getCollection()”](#getcollection)

**Type:** `(collection: string, filter?: (entry: CollectionEntry<collection>) => boolean) => CollectionEntry<collection>[]`

**Added in:** `astro@2.0.0`

`getCollection()` is a function that retrieves a list of content collection entries by collection name.

It returns all items in the collection by default, and accepts an optional `filter` function to narrow by entry properties. This allows you to query for only some items in a collection based on `id` or frontmatter values via the `data` object.

```astro
---
import { getCollection } from 'astro:content';


// Get all `src/content/blog/` entries
const allBlogPosts = await getCollection('blog');


// Only return posts with `draft: true` in the frontmatter
const draftBlogPosts = await getCollection('blog', ({ data }) => {
  return data.draft === true;
});
---
```

[See the `Content Collection` guide](/en/guides/content-collections/#querying-collections) for example usage.

### `getEntry()`

[Section titled “getEntry()”](#getentry)

**Types:**

* `(collection: string, id: string) => Promise<CollectionEntry<collection> | undefined>`
* `({ collection: string, id: string }) => Promise<CollectionEntry<collection> | undefined>`

**Added in:** `astro@2.5.0`

`getEntry()` is a function that retrieves a single collection entry by collection name and the entry `id`. `getEntry()` can also be used to get referenced entries to access the `data` or `body` properties:

```astro
---
import { getEntry } from 'astro:content';


// Get `src/content/blog/enterprise.md`
const enterprisePost = await getEntry('blog', 'enterprise');


// Get `src/content/captains/picard.json`
const picardProfile = await getEntry('captains', 'picard');


// Get the profile referenced by `data.captain`
const enterpriseCaptainProfile = await getEntry(enterprisePost.data.captain);
---
```

See the `Content Collections` guide for examples of [querying collection entries](/en/guides/content-collections/#querying-collections).

### `getEntries()`

[Section titled “getEntries()”](#getentries)

**Type:** `(Array<{ collection: string, id: string }>) => Array<CollectionEntry<collection>>`

**Added in:** `astro@2.5.0`

`getEntries()` is a function that retrieves multiple collection entries from the same collection. This is useful for [returning an array of referenced entries](/en/guides/content-collections/#defining-collection-references) to access their associated `data` and `body` properties.

```astro
---
import { getEntries, getEntry } from 'astro:content';


const enterprisePost = await getEntry('blog', 'enterprise');


// Get related posts referenced by `data.relatedPosts`
const enterpriseRelatedPosts = await getEntries(enterprisePost.data.relatedPosts);
---
```

### `render()`

[Section titled “render()”](#render)

**Type:** `(entry: CollectionEntry) => Promise<RenderedEntry>`

**Added in:** `astro@5.0.0`

A function to compile a given entry for rendering. This returns the following properties:

* `<Content />` - A component used to render the document’s contents in an Astro file.
* `headings` - A generated list of headings, [mirroring Astro’s `getHeadings()` utility](/en/guides/markdown-content/#available-properties) on Markdown and MDX imports.
* `remarkPluginFrontmatter `- The modified frontmatter object after any [remark or rehype plugins have been applied](/en/guides/markdown-content/#modifying-frontmatter-programmatically). Set to type `any`.

```astro
---
import { getEntry, render } from 'astro:content';
const entry = await getEntry('blog', 'entry-1');


if (!entry) {
   // Handle Error, for example:
  throw new Error('Could not find blog post 1');
}
const { Content, headings, remarkPluginFrontmatter } = await render(entry);
---
```

[See the `Content Collection` guide](/en/guides/content-collections/#rendering-body-content) for example usage.

## `astro:content` types

[Section titled “astro:content types”](#astrocontent-types)

```ts
import type {
  CollectionEntry,
  CollectionKey,
  ContentCollectionKey,
  DataCollectionKey,
  SchemaContext,
 } from 'astro:content';
```

### `CollectionEntry`

[Section titled “CollectionEntry”](#collectionentry)

Query functions including [`getCollection()`](#getcollection), [`getEntry()`](#getentry), and [`getEntries()`](#getentries) each return entries with the `CollectionEntry` type. This type is available as a utility from `astro:content`:

```ts
import type { CollectionEntry } from 'astro:content';
```

`CollectionEntry` is a generic type. Use it with the name of the collection you’re querying. For example, an entry in your `blog` collection would have the type `CollectionEntry<'blog'>`.

Each `CollectionEntry` is an object with the following values:

#### `id`

[Section titled “id”](#id)

**Type:** `string`

A unique ID. Note that all IDs from Astro’s built-in `glob()` loader are slugified.

#### `collection`

[Section titled “collection”](#collection)

**Example Type:** `'blog' | 'authors' | ...`

The name of a collection in which entries are located. This is the name used to reference the collection in your schema, and in querying functions.

#### `data`

[Section titled “data”](#data)

**Type:** `CollectionSchema<TCollectionName>`

An object of frontmatter properties inferred from your collection schema ([see `defineCollection()` reference](#definecollection)). Defaults to `any` if no schema is configured.

#### `body`

[Section titled “body”](#body)

**Type:** `string`

A string containing the raw, uncompiled body of the Markdown or MDX document.

### `CollectionKey`

[Section titled “CollectionKey”](#collectionkey)

**Added in:** `astro@3.1.0`

A string union of all collection names defined in your `src/content.config.*` file. This type can be useful when defining a generic function wrapping the built-in `getCollection()`.

```ts
import { type CollectionKey, getCollection } from 'astro:content';


async function queryCollection(collection: CollectionKey) {
  return getCollection(collection, ({ data }) => {
    return data.draft !== true;
  });
}
```

### `SchemaContext`

[Section titled “SchemaContext”](#schemacontext)

The `context` object that `defineCollection` uses for the function shape of `schema`. This type can be useful when building reusable schemas for multiple collections.

This includes the following property:

* `image` - The `image()` schema helper that allows you [to use local images in Content Collections](/en/guides/images/#images-in-content-collections)

```ts
import { defineCollection, z, type SchemaContext } from "astro:content";


export const imageSchema = ({ image }: SchemaContext) =>
    z.object({
        image: image(),
        description: z.string().optional(),
    });


const blog = defineCollection({
  loader: /* ... */,
  schema: ({ image }) => z.object({
    title: z.string(),
    permalink: z.string().optional(),
    image: imageSchema({ image })
  }),
});
```

# Environment Variables API Reference

**Added in:** `astro@5.0.0`

The `astro:env` API lets you configure a type-safe schema for environment variables you have set. This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties. For examples and usage instructions, [see the `astro:env` guide](/en/guides/environment-variables/#type-safe-environment-variables).

## Imports from `astro:env`

[Section titled “Imports from astro:env”](#imports-from-astroenv)

```js
import {
  getSecret,
 } from 'astro:env/server';
```

### `getSecret()`

[Section titled “getSecret()”](#getsecret)

**Added in:** `astro@5.0.0`

The `getSecret()` helper function allows retrieving the raw value of an environment variable by its key.

For example, you can retrieve a boolean value as a string:

```js
import {
  FEATURE_FLAG, // boolean
  getSecret
} from 'astro:env/server'


getSecret('FEATURE_FLAG') // string | undefined
```

This can also be useful to get a secret not defined in your schema, for example one that depends on dynamic data from a database or API.

If you need to retrieve environment variables programmatically, we recommend using `getSecret()` instead of `process.env` (or equivalent). Because its implementation is provided by your adapter, you won’t need to update all your calls if you switch adapters. It defaults to `process.env` in dev and build.

# Internationalization API Reference

**Added in:** `astro@3.5.0`

This module provides functions to help you create URLs using your project’s configured locales.

Creating routes for your project with the i18n router will depend on certain configuration values you have set that affect your page routes. When creating routes with these functions, be sure to take into account your individual settings for:

* [`base`](/en/reference/configuration-reference/#base)
* [`trailingSlash`](/en/reference/configuration-reference/#trailingslash)
* [`build.format`](/en/reference/configuration-reference/#buildformat)
* [`site`](/en/reference/configuration-reference/#site)

Also, note that the returned URLs created by these functions for your `defaultLocale` will reflect your `i18n.routing` configuration.

For features and usage examples, [see our i18n routing guide](/en/guides/internationalization/).

## Imports from `astro:i18n`

[Section titled “Imports from astro:i18n”](#imports-from-astroi18n)

```js
import {
  getRelativeLocaleUrl,
  getAbsoluteLocaleUrl,
  getRelativeLocaleUrlList,
  getAbsoluteLocaleUrlList,
  getPathByLocale,
  getLocaleByPath,
  redirectToDefaultLocale,
  redirectToFallback,
  notFound,
  middleware,
  requestHasLocale,
  normalizeTheLocale,
  pathHasLocale,
  toCodes,
  toPaths
 } from 'astro:i18n';
```

### `getRelativeLocaleUrl()`

[Section titled “getRelativeLocaleUrl()”](#getrelativelocaleurl)

**Type:** `(locale: string, path?: string, options?: GetLocaleOptions) => string`

Use this function to retrieve a relative path for a locale. If the locale doesn’t exist, Astro throws an error.

```astro
---
import { getRelativeLocaleUrl } from 'astro:i18n';


getRelativeLocaleUrl("fr");
// returns /fr


getRelativeLocaleUrl("fr", "");
// returns /fr/


getRelativeLocaleUrl("fr", "getting-started");
// returns /fr/getting-started


getRelativeLocaleUrl("fr_CA", "getting-started", {
  prependWith: "blog"
});
// returns /blog/fr-ca/getting-started


getRelativeLocaleUrl("fr_CA", "getting-started", {
  prependWith: "blog",
  normalizeLocale: false
});
// returns /blog/fr_CA/getting-started
---
```

### `getAbsoluteLocaleUrl()`

[Section titled “getAbsoluteLocaleUrl()”](#getabsolutelocaleurl)

**Type:** `(locale: string, path?: string, options?: GetLocaleOptions) => string`

Use this function to retrieve an absolute path for a locale when \[`site`] has a value. If \[`site`] isn’t configured, the function returns a relative URL. If the locale doesn’t exist, Astro throws an error.

src/pages/index.astro

```astro
---
import { getAbsoluteLocaleUrl } from 'astro:i18n';


// If `site` is set to be `https://example.com`


getAbsoluteLocaleUrl("fr");
// returns https://example.com/fr


getAbsoluteLocaleUrl("fr", "");
// returns https://example.com/fr/


getAbsoluteLocaleUrl("fr", "getting-started");
// returns https://example.com/fr/getting-started


getAbsoluteLocaleUrl("fr_CA", "getting-started", {
  prependWith: "blog"
});
// returns https://example.com/blog/fr-ca/getting-started


getAbsoluteLocaleUrl("fr_CA", "getting-started", {
  prependWith: "blog",
  normalizeLocale: false
});
// returns https://example.com/blog/fr_CA/getting-started
---
```

### `getRelativeLocaleUrlList()`

[Section titled “getRelativeLocaleUrlList()”](#getrelativelocaleurllist)

**Type:** `(path?: string, options?: GetLocaleOptions) => string[]`

Use this like [`getRelativeLocaleUrl`](#getrelativelocaleurl) to return a list of relative paths for all the locales.

### `getAbsoluteLocaleUrlList()`

[Section titled “getAbsoluteLocaleUrlList()”](#getabsolutelocaleurllist)

**Type:** `(path?: string, options?: GetLocaleOptions) => string[]`

Use this like [`getAbsoluteLocaleUrl`](/en/guides/internationalization/#custom-locale-paths) to return a list of absolute paths for all the locales.

### `getPathByLocale()`

[Section titled “getPathByLocale()”](#getpathbylocale)

**Type:** `(locale: string) => string`

A function that returns the `path` associated to one or more `codes` when [custom locale paths](/en/guides/internationalization/#custom-locale-paths) are configured.

astro.config.mjs

```js
export default defineConfig({
  i18n: {
    locales: ["es", "en", {
      path: "french",
      codes: ["fr", "fr-BR", "fr-CA"]
    }]
  }
})
```

src/pages/index.astro

```astro
---
import { getPathByLocale } from 'astro:i18n';


getPathByLocale("fr"); // returns "french"
getPathByLocale("fr-CA"); // returns "french"
---
```

### `getLocaleByPath()`

[Section titled “getLocaleByPath()”](#getlocalebypath)

**Type:** `(path: string) => string`

A function that returns the `code` associated to a locale `path`.

astro.config.mjs

```js
export default defineConfig({
  i18n: {
    locales: ["es", "en", {
      path: "french",
      codes: ["fr", "fr-BR", "fr-CA"]
    }]
  }
})
```

src/pages/index.astro

```astro
---
import { getLocaleByPath } from 'astro:i18n';


getLocaleByPath("french"); // returns "fr" because that's the first code configured
---
```

### `redirectToDefaultLocale()`

[Section titled “redirectToDefaultLocale()”](#redirecttodefaultlocale)

**Type:** `(context: APIContext, statusCode?: ValidRedirectStatus) => Promise<Response>`

**Added in:** `astro@4.6.0`

Note

Available only when `i18n.routing` is set to `"manual"`

A function that returns a `Response` that redirects to the `defaultLocale` configured. It accepts an optional valid redirect status code.

middleware.js

```js
import { defineMiddleware } from "astro:middleware";
import { redirectToDefaultLocale } from "astro:i18n";


export const onRequest = defineMiddleware((context, next) => {
  if (context.url.pathname.startsWith("/about")) {
    return next();
  } else {
    return redirectToDefaultLocale(context, 302);
  }
})
```

### `redirectToFallback()`

[Section titled “redirectToFallback()”](#redirecttofallback)

**Type:** `(context: APIContext, response: Response) => Promise<Response>`

**Added in:** `astro@4.6.0`

Note

Available only when `i18n.routing` is set to `"manual"`

A function that allows you to use your [`i18n.fallback` configuration](/en/reference/configuration-reference/#i18nfallback) in your own middleware.

middleware.js

```js
import { defineMiddleware } from "astro:middleware";
import { redirectToFallback } from "astro:i18n";


export const onRequest = defineMiddleware(async (context, next) => {
  const response = await next();
  if (response.status >= 300) {
    return redirectToFallback(context, response)
  }
  return response;
})
```

### `notFound()`

[Section titled “notFound()”](#notfound)

**Type:** `(context: APIContext, response?: Response) => Promise<Response> | undefined`

**Added in:** `astro@4.6.0`

Note

Available only when `i18n.routing` is set to `"manual"`

Use this function in your routing middleware to return a 404 when:

* the current path isn’t a root. e.g. `/` or `/<base>`
* the URL doesn’t contain a locale

When a `Response` is passed, the new `Response` emitted by this function will contain the same headers of the original response.

middleware.js

```js
import { defineMiddleware } from "astro:middleware";
import { notFound } from "astro:i18n";


export const onRequest = defineMiddleware((context, next) => {
  const pathNotFound = notFound(context);
  if (pathNotFound) {
    return pathNotFound;
  }
  return next();
})
```

### `middleware()`

[Section titled “middleware()”](#middleware)

**Type:** `(options: { prefixDefaultLocale: boolean, redirectToDefaultLocale: boolean }) => MiddlewareHandler`

**Added in:** `astro@4.6.0`

Note

Available only when `i18n.routing` is set to `"manual"`

A function that allows you to programmatically create the Astro i18n middleware.

This is useful when you still want to use the default i18n logic, but add only a few exceptions to your website.

middleware.js

```js
import { middleware } from "astro:i18n";
import { sequence, defineMiddleware } from "astro:middleware";


const customLogic = defineMiddleware(async (context, next) => {
  const response = await next();


  // Custom logic after resolving the response.
  // It's possible to catch the response coming from Astro i18n middleware.


  return response;
});


export const onRequest = sequence(customLogic, middleware({
  prefixDefaultLocale: true,
  redirectToDefaultLocale: false
}))
```

### `requestHasLocale()`

[Section titled “requestHasLocale()”](#requesthaslocale)

**Type:** `(context: APIContext) => boolean`

**Added in:** `astro@4.6.0`

Note

Available only when `i18n.routing` is set to `"manual"`

Checks whether the current URL contains a configured locale. Internally, this function will use `APIContext#url.pathname`.

middleware.js

```js
import { defineMiddleware } from "astro:middleware";
import { requestHasLocale } from "astro:i18n";


export const onRequest = defineMiddleware(async (context, next) => {
  if (requestHasLocale(context)) {
    return next();
  }
  return new Response("Not found", { status: 404 });
})
```

### `normalizeTheLocale()`

[Section titled “normalizeTheLocale()”](#normalizethelocale)

**Type:** `(locale: string) => string`

Replaces underscores (`_`) with hyphens (`-`) in the given locale before returning a lowercase version.

src/pages/index.astro

```astro
---
import { normalizeTheLocale } from "astro:i18n";


normalizeTheLocale("it_VT") // returns `it-vt`
// Assuming the current locale is `"pt-PT"`:
normalizeTheLocale(Astro.currentLocale) // returns `pt-pt`
---
```

### `pathHasLocale()`

[Section titled “pathHasLocale()”](#pathhaslocale)

**Type:** `(path: string) => boolean`

**Added in:** `astro@4.6.0`

Checks whether the given path contains a configured locale.

This is useful to prevent errors before using an i18n utility that relies on a locale from a URL path.

astro.config.mjs

```js
export default defineConfig({
  i18n: {
    locales: [
      { codes: ["it-VT", "it"], path: "italiano" },
      "es"
    ]
  }
})
```

src/pages/index.astro

```astro
---
import { pathHasLocale } from "astro:i18n";


pathHasLocale("italiano"); // returns `true`
pathHasLocale("es"); // returns `true`
pathHasLocale('/es/blog/'); // returns `true`
pathHasLocale("it-VT"); // returns `false`
---
```

### `toCodes()`

[Section titled “toCodes()”](#tocodes)

**Type:** `(locales: Locales) => string[]`

**Added in:** `astro@4.0.0`

Retrieves the configured locale codes for each locale defined in your configuration. When multiple codes are associated to a locale, only the first one will be added to the array.

astro.config.mjs

```js
export default defineConfig({
  i18n: {
    locales: [
      { codes: ["it-VT", "it"], path: "italiano" },
      "es"
    ]
  }
})
```

src/pages/index.astro

```astro
---
import { i18n } from "astro:config/client";
import { toCodes } from "astro:i18n";


toCodes(i18n!.locales); // ["it-VT", "es"]
---
```

### `toPaths()`

[Section titled “toPaths()”](#topaths)

**Type:** `(locales: Locales) => string[]`

**Added in:** `astro@4.0.0`

Retrieves the configured locale paths for each locale defined in your configuration.

astro.config.mjs

```js
export default defineConfig({
  i18n: {
    locales: [
      { codes: ["it-VT", "it"], path: "italiano" },
      "es"
    ]
  }
})
```

src/pages/index.astro

```astro
---
import { i18n } from "astro:config/client";
import { toPaths } from "astro:i18n";


toPaths(i18n!.locales); // ["italiano", "es"]
---
```

# Middleware API Reference

**Added in:** `astro@2.6.0`

Middleware allows you to intercept requests and responses and inject behaviors dynamically every time a page or endpoint is about to be rendered. For features and usage examples, [see our middleware guide](/en/guides/middleware/).

## Imports from `astro:middleware`

[Section titled “Imports from astro:middleware”](#imports-from-astromiddleware)

```js
import {
  sequence,
  createContext,
  trySerializeLocals,
  defineMiddleware,
 } from 'astro:middleware';
```

### `defineMiddleware()`

[Section titled “defineMiddleware()”](#definemiddleware)

You can import and use the utility function `defineMiddleware()` to take advantage of type safety:

src/middleware.ts

```ts
import { defineMiddleware } from "astro:middleware";


// `context` and `next` are automatically typed
export const onRequest = defineMiddleware((context, next) => {


});
```

### `sequence()`

[Section titled “sequence()”](#sequence)

**Type:** `(...handlers: MiddlewareHandler[]) => MiddlewareHandler`

A function that accepts middleware functions as arguments, and will execute them in the order in which they are passed.

src/middleware.js

```js
import { sequence } from "astro:middleware";


async function validation(_, next) {...}
async function auth(_, next) {...}
async function greeting(_, next) {...}


export const onRequest = sequence(validation, auth, greeting);
```

### `createContext()`

[Section titled “createContext()”](#createcontext)

**Type:** `(context: CreateContext) => APIContext`

**Added in:** `astro@2.8.0`

A low-level API to create an [`APIContext`](/en/reference/api-reference/)to be passed to an Astro middleware `onRequest()` function.

This function can be used by integrations/adapters to programmatically execute the Astro middleware.

### `trySerializeLocals()`

[Section titled “trySerializeLocals()”](#tryserializelocals)

**Type:** `(value: unknown) => string`

**Added in:** `astro@2.8.0`

A low-level API that takes in any value and tries to return a serialized version (a string) of it. If the value cannot be serialized, the function will throw a runtime error.

## Middleware exports

[Section titled “Middleware exports”](#middleware-exports)

When defining your project’s middleware in `src/middleware.js`, export the following user-defined functions:

### `onRequest()`

[Section titled “onRequest()”](#onrequest)

**Type:** `(context: APIContext, next: MiddlewareNext) => Promise<Response> | Response | Promise<void> | void`

A required exported function from `src/middleware.js` that will be called before rendering every page or API route. It receives two arguments: [context](#context) and [next()](#next). `onRequest()` must return a `Response`: either directly, or by calling `next()`.

src/middleware.js

```js
export function onRequest (context, next) {
    // intercept response data from a request
    // optionally, transform the response
    // return a Response directly, or the result of calling `next()`
    return next();
};
```

Your `onRequest()` function will be called with the following arguments:

#### `context`

[Section titled “context”](#context)

**Type:** `APIContext`

The first argument of `onRequest()` is a context object. It mirrors many of the `Astro` global properties.

See [Endpoint contexts](/en/reference/api-reference/) for more information about the context object.

#### `next()`

[Section titled “next()”](#next)

**Type:** `(rewritePayload?: string | URL | Request) => Promise<Response>`

The second argument of `onRequest()` is a function that calls all the subsequent middleware in the chain and returns a `Response`. For example, other middleware could modify the HTML body of a response and awaiting the result of `next()` would allow your middleware to respond to those changes.

Since Astro v4.13.0, `next()` accepts an optional URL path parameter in the form of a string, `URL`, or `Request` to [rewrite](/en/guides/routing/#rewrites) the current request without retriggering a new rendering phase.

# View Transitions Router API Reference

**Added in:** `astro@3.0.0`

These modules provide functions to control and interact with the View Transitions API and client-side router.

Note

This API is compatible with the `<ClientRouter />` included in `astro:transitions`, but can’t be used with native browser MPA routing.

For features and usage examples, [see our View Transitions guide](/en/guides/view-transitions/).

## Imports from `astro:transitions`

[Section titled “Imports from astro:transitions”](#imports-from-astrotransitions)

```ts
import { ClientRouter, fade, slide } from 'astro:transitions';
```

### `<ClientRouter />`

[Section titled “\<ClientRouter />”](#clientrouter-)

**Added in:** `astro@3.0.0`

Opt in to using view transitions on individual pages by importing and adding the `<ClientRouter />` routing component to `<head>` on every desired page.

src/pages/index.astro

```diff
---
+import { ClientRouter } from 'astro:transitions';
---
<html lang="en">
  <head>
    <title>My Homepage</title>
    +<ClientRouter />
  </head>
  <body>
    <h1>Welcome to my website!</h1>
  </body>
</html>
```

See more about how to [control the router](/en/guides/view-transitions/#router-control) and [add transition directives](/en/guides/view-transitions/#transition-directives) to page elements and components.

### `fade`

[Section titled “fade”](#fade)

**Type:** `(opts: { duration?: string | number }) => TransitionDirectionalAnimations`

**Added in:** `astro@3.0.0`

Utility function to support customizing the duration of the built-in `fade` animation.

```astro
---
import { fade } from 'astro:transitions';
---


<!-- Fade transition with the default duration -->
<div transition:animate="fade" />


<!-- Fade transition with a duration of 400 milliseconds -->
<div transition:animate={fade({ duration: '0.4s' })} />
```

### `slide`

[Section titled “slide”](#slide)

**Type:** `(opts: { duration?: string | number }) => TransitionDirectionalAnimations`

**Added in:** `astro@3.0.0`

Utility function to support customizing the duration of the built-in `slide` animation.

```astro
---
import { slide } from 'astro:transitions';
---


<!-- Slide transition with the default duration -->
<div transition:animate="slide" />


<!-- Slide transition with a duration of 400 milliseconds -->
<div transition:animate={slide({ duration: '0.4s' })} />
```

## Imports from `astro:transitions/client`

[Section titled “Imports from astro:transitions/client”](#imports-from-astrotransitionsclient)

```astro
<script>
  import {
    navigate,
    supportsViewTransitions,
    transitionEnabledOnThisPage,
    getFallback,
    swapFunctions,
  } from 'astro:transitions/client';
</script>
```

### `navigate()`

[Section titled “navigate()”](#navigate)

**Type:** `(href: string, options?: Options) => void`

**Added in:** `astro@3.2.0`

A function that executes a navigation to the given `href` using the View Transitions API.

This function signature is based on the [`navigate` function from the browser Navigation API](https://developer.mozilla.org/en-US/docs/Web/API/Navigation/navigate). Although based on the Navigation API, this function is implemented on top of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to allow for navigation without reloading the page.

#### `history` option

[Section titled “history option”](#history-option)

**Type:** `'auto' | 'push' | 'replace'`\
**Default:** `'auto'`

**Added in:** `astro@3.2.0`

Defines how this navigation should be added to the browser history.

* `'push'`: the router will use `history.pushState` to create a new entry in the browser history.
* `'replace'`: the router will use `history.replaceState` to update the URL without adding a new entry into navigation.
* `'auto'` (default): the router will attempt `history.pushState`, but if the URL cannot be transitioned to, the current URL will remain with no changes to the browser history.

This option follows the [`history` option](https://developer.mozilla.org/en-US/docs/Web/API/Navigation/navigate#history) from the browser Navigation API but simplified for the cases that can happen on an Astro project.

#### `formData` option

[Section titled “formData option”](#formdata-option)

**Type:** `FormData`

**Added in:** `astro@3.5.0`

A `FormData` object for `POST` requests.

When this option is provided, the requests to the navigation target page will be sent as a `POST` request with the form data object as the content.

Submitting an HTML form with view transitions enabled will use this method instead of the default navigation with page reload. Calling this method allows triggering the same behavior programmatically.

#### `info` option

[Section titled “info option”](#info-option)

**Type:** `any`

**Added in:** `astro@3.6.0`

Arbitrary data to be included in the `astro:before-preparation` and `astro:before-swap` events caused by this navigation.

This option mimics the [`info` option](https://developer.mozilla.org/en-US/docs/Web/API/Navigation/navigate#info) from the browser Navigation API.

#### `state` option

[Section titled “state option”](#state-option)

**Type:** `any`

**Added in:** `astro@3.6.0`

Arbitrary data to be associated with the `NavitationHistoryEntry` object created by this navigation. This data can then be retrieved using the [`history.getState` function](https://developer.mozilla.org/en-US/docs/Web/API/NavigationHistoryEntry/getState) from the History API.

This option mimics the [`state` option](https://developer.mozilla.org/en-US/docs/Web/API/Navigation/navigate#state) from the browser Navigation API.

#### `sourceElement` option

[Section titled “sourceElement option”](#sourceelement-option)

**Type:** `Element`

**Added in:** `astro@3.6.0`

The element that triggered this navigation, if any. This element will be available in the following events:

* `astro:before-preparation`
* `astro:before-swap`

### `supportsViewTransitions`

[Section titled “supportsViewTransitions”](#supportsviewtransitions)

**Type:** `boolean`

**Added in:** `astro@3.2.0`

Whether or not view transitions are supported and enabled in the current browser.

### `transitionEnabledOnThisPage`

[Section titled “transitionEnabledOnThisPage”](#transitionenabledonthispage)

**Type:** `boolean`

**Added in:** `astro@3.2.0`

Whether or not the current page has view transitions enabled for client-side navigation. This can be used to make components that behave differently when they are used on pages with view transitions.

### `getFallback()`

[Section titled “getFallback()”](#getfallback)

**Type:** `() => 'none' | 'animate' | 'swap'`

**Added in:** `astro@3.6.0`

Returns the fallback strategy to use in browsers that do not support view transitions.

See the guide on [Fallback control](/en/guides/view-transitions/#fallback-control) for how to choose and configure the fallback behavior.

### `swapFunctions`

[Section titled “swapFunctions”](#swapfunctions)

**Added in:** `astro@4.15.0`

An object containing the utility functions used to build Astro’s default swap function. These can be useful when [building a custom swap function](/en/guides/view-transitions/#building-a-custom-swap-function).

`swapFunctions` provides the following methods:

#### `deselectScripts()`

[Section titled “deselectScripts()”](#deselectscripts)

**Type:** `(newDocument: Document) => void`

Marks scripts in the new document that should not be executed. Those scripts are already in the current document and are not flagged for re-execution using [`data-astro-rerun`](/en/guides/view-transitions/#data-astro-rerun).

#### `swapRootAttributes()`

[Section titled “swapRootAttributes()”](#swaprootattributes)

**Type:** `(newDocument: Document) => void`

Swaps the attributes between the document roots, like the `lang` attribute. This also includes Astro-injected internal attributes like `data-astro-transition`, which makes the transition direction available to Astro-generated CSS rules.

When making a custom swap function, it is important to call this function so as not to break the view transition’s animations.

#### `swapHeadElements()`

[Section titled “swapHeadElements()”](#swapheadelements)

**Type:** `(newDocument: Document) => void`

Removes every element from the current document’s `<head>` that is not persisted to the new document. Then appends all new elements from the new document’s `<head>` to the current document’s `<head>`.

#### `saveFocus()`

[Section titled “saveFocus()”](#savefocus)

**Type:** `() => () => void`

Stores the element in focus on the current page and returns a function that when called, if the focused element was persisted, returns the focus to it.

#### `swapBodyElement()`

[Section titled “swapBodyElement()”](#swapbodyelement)

**Type:** `(newBody: Element, oldBody: Element) => void`

Replaces the old body with the new body. Then, goes through every element in the old body that should be persisted and have a matching element in the new body and swaps the old element back in place.

## Lifecycle events

[Section titled “Lifecycle events”](#lifecycle-events)

### `astro:before-preparation` event

[Section titled “astro:before-preparation event”](#astrobefore-preparation-event)

An event dispatched at the beginning of a navigation using the View Transitions router. This event happens before any request is made and any browser state is changed.

This event has the attributes:

* [`info`](#info)
* [`sourceElement`](#sourceelement)
* [`navigationType`](#navigationtype)
* [`direction`](#direction)
* [`from`](#from)
* [`to`](#to)
* [`formData`](#formdata)
* [`loader()`](#loader)

Read more about how to use this event on the [View Transitions guide](/en/guides/view-transitions/#astrobefore-preparation).

### `astro:after-preparation` event

[Section titled “astro:after-preparation event”](#astroafter-preparation-event)

An event dispatched after the next page in a navigation using View Transitions router is loaded.

This event has no attributes.

Read more about how to use this event on the [View Transitions guide](/en/guides/view-transitions/#astroafter-preparation).

### `astro:before-swap` event

[Section titled “astro:before-swap event”](#astrobefore-swap-event)

An event dispatched after the next page is parsed, prepared, and linked into a document in preparation for the transition but before any content is swapped between the documents.

This event can’t be canceled. Calling `preventDefault()` is a no-op.

This event has the attributes:

* [`info`](#info)
* [`sourceElement`](#sourceelement)
* [`navigationType`](#navigationtype)
* [`direction`](#direction)
* [`from`](#from)
* [`to`](#to)
* [`viewTransition`](#viewtransition)
* [`swap()`](#swap)

Read more about how to use this event on the [View Transitions guide](/en/guides/view-transitions/#astrobefore-swap).

### `astro:after-swap` event

[Section titled “astro:after-swap event”](#astroafter-swap-event)

An event dispatched after the contents of the page have been swapped but before the view transition ends.

The history entry and scroll position have already been updated when this event is triggered.

### `astro:page-load` event

[Section titled “astro:page-load event”](#astropage-load-event)

An event dispatched after a page completes loading, whether from a navigation using view transitions or native to the browser.

When view transitions is enabled on the page, code that would normally execute on `DOMContentLoaded` should be changed to execute on this event.

### Lifecycle events attributes

[Section titled “Lifecycle events attributes”](#lifecycle-events-attributes)

**Added in:** `astro@3.6.0`

#### `info`

[Section titled “info”](#info)

**Type:** `URL`

Arbitrary data defined during navigation.

This is the literal value passed on the [`info` option](#info-option) of the [`navigate()` function](#navigate).

#### `sourceElement`

[Section titled “sourceElement”](#sourceelement)

**Type:** `Element | undefined`

The element that triggered the navigation. This can be, for example, an `<a>` element that was clicked.

When using the [`navigate()` function](#navigate), this will be the element specified in the call.

#### `newDocument`

[Section titled “newDocument”](#newdocument)

**Type:** `Document`

The document for the next page in the navigation. The contents of this document will be swapped in place of the contents of the current document.

#### `navigationType`

[Section titled “navigationType”](#navigationtype)

**Type:** `'push' | 'replace' | 'traverse'`

Which kind of history navigation is happening.

* `push`: a new `NavigationHistoryEntry` is being created for the new page.
* `replace`: the current `NavigationHistoryEntry` is being replaced with an entry for the new page.
* `traverse`: no `NavigationHistoryEntry` is created. The position in the history is changing. The direction of the traversal is given on the [`direction` attribute](#direction)

#### `direction`

[Section titled “direction”](#direction)

**Type:** `Direction`

The direction of the transition.

* `forward`: navigating to the next page in the history or to a new page.
* `back`: navigating to the previous page in the history.
* Anything else some other listener might have set.

#### `from`

[Section titled “from”](#from)

**Type:** `URL`

The URL of the page initiating the navigation.

#### `to`

[Section titled “to”](#to)

**Type:** `URL`

The URL of the page being navigated to. This property can be modified, the value at the end of the lifecycle will be used in the `NavigationHistoryEntry` for the next page.

#### `formData`

[Section titled “formData”](#formdata)

**Type:** `FormData | undefined`

A `FormData` object for `POST` requests.

When this attribute is set, a `POST` request will be sent to the [`to` URL](#to) with the given form data object as the content instead of the normal `GET` request.

When submitting an HTML form with view transitions enabled, this field is automatically set to the data in the form. When using the [`navigate()` function](#navigate), this value is the same as given in the options.

#### `loader()`

[Section titled “loader()”](#loader)

**Type:** `() => Promise<void>`

Implementation of the following phase in the navigation (loading the next page). This implementation can be overridden to add extra behavior.

#### `viewTransition`

[Section titled “viewTransition”](#viewtransition)

**Type:** [`ViewTransition`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTransition)

The view transition object used in this navigation. On browsers that do not support the [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API), this is an object implementing the same API for convenience but without the DOM integration.

#### `swap()`

[Section titled “swap()”](#swap)

**Type:** `() => void`

Implementation of the document swap logic.

Read more about [building a custom swap function](/en/guides/view-transitions/#building-a-custom-swap-function) in the View Transitions guide.

By default, this implementation will call the following functions in order:

1. [`deselectScripts()`](#deselectscripts)
2. [`swapRootAttributes()`](#swaprootattributes)
3. [`swapHeadElements()`](#swapheadelements)
4. [`saveFocus()`](#savefocus)
5. [`swapBodyElement()`](#swapbodyelement)

# Programmatic Astro API (experimental)

If you need more control when running Astro, the `"astro"` package exports APIs to programmatically run the CLI commands.

These APIs are experimental and their API signature may change. Any updates will be mentioned in the [Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) and the information below will always show the current, up-to-date information.

## `AstroInlineConfig`

[Section titled “AstroInlineConfig”](#astroinlineconfig)

The `AstroInlineConfig` type is used by all of the command APIs below. It extends from the user [Astro config](/en/reference/configuration-reference/) type:

```ts
interface AstroInlineConfig extends AstroUserConfig {
  configFile?: string | false;
  mode?: string;
  logLevel?: "debug" | "info" | "warn" | "error" | "silent";
}
```

### `configFile`

[Section titled “configFile”](#configfile)

**Type:** `string | false`\
**Default:** `undefined`

A custom path to the Astro config file.

If this value is undefined (default) or unset, Astro will search for an `astro.config.(js,mjs,ts,mts)` file relative to the `root` and load the config file if found.

If a relative path is set, it will resolve based on the `root` option.

Set to `false` to disable loading any config files.

The inline config passed in this object will take highest priority when merging with the loaded user config.

### `mode`

[Section titled “mode”](#mode)

**Type:** `string`\
**Default:** `"development"` when running `astro dev`, `"production"` when running `astro build`

**Added in:** `astro@5.0.0`

The mode used when developing or building your site (e.g. `"production"`, `"testing"`).

This value is passed to Vite using [the `--mode` flag](/en/reference/cli-reference/#--mode-string) when the `astro build` or `astro dev` commands are run to determine the value of `import.meta.env.MODE`. This also determines which `.env` files are loaded, and therefore the values of `astro:env`. See the [environment variables page](/en/guides/environment-variables/) for more details.

To output a development-based build, you can run `astro build` with the [`--devOutput` flag](/en/reference/cli-reference/#--devoutput).

### `logLevel`

[Section titled “logLevel”](#loglevel)

**Type:** `"debug" | "info" | "warn" | "error" | "silent"`\
**Default:** `"info"`

The logging level to filter messages logged by Astro.

* `"debug"`: Log everything, including noisy debugging diagnostics.
* `"info"`: Log informational messages, warnings, and errors.
* `"warn"`: Log warnings and errors.
* `"error"`: Log errors only.
* `"silent"`: No logging.

## `dev()`

[Section titled “dev()”](#dev)

**Type:** `(inlineConfig: AstroInlineConfig) => Promise<DevServer>`

Similar to [`astro dev`](/en/reference/cli-reference/#astro-dev), it runs Astro’s development server.

```js
import { dev } from "astro";


const devServer = await dev({
  root: "./my-project",
});


// Stop the server if needed
await devServer.stop();
```

### `DevServer`

[Section titled “DevServer”](#devserver)

```ts
export interface DevServer {
  address: AddressInfo;
  handle: (req: http.IncomingMessage, res: http.ServerResponse<http.IncomingMessage>) => void;
  watcher: vite.FSWatcher;
  stop(): Promise<void>;
}
```

#### `address`

[Section titled “address”](#address)

**Type:** `AddressInfo`

The address the dev server is listening on.

This property contains the value returned by Node’s [`net.Server#address()` method](https://nodejs.org/api/net.html#serveraddress).

#### `handle()`

[Section titled “handle()”](#handle)

**Type:** `(req: http.IncomingMessage, res: http.ServerResponse<http.IncomingMessage>) => void`

A handle for raw Node HTTP requests. You can call `handle()` with an [`http.IncomingMessage`](https://nodejs.org/api/http.html#class-httpincomingmessage) and an [`http.ServerResponse`](https://nodejs.org/api/http.html#class-httpserverresponse) instead of sending a request through the network.

#### `watcher`

[Section titled “watcher”](#watcher)

**Type:** `vite.FSWatcher`

The [Chokidar file watcher](https://github.com/paulmillr/chokidar#getting-started) as exposed by [Vite’s development server](https://vite.dev/guide/api-javascript#vitedevserver).

#### `stop()`

[Section titled “stop()”](#stop)

**Type:** `Promise<void>`

Stops the development server. This closes all idle connections and stops listening for new connections.

Returns a `Promise` that resolves once all pending requests have been fulfilled and all idle connections have been closed.

## `build()`

[Section titled “build()”](#build)

**Type:** `(inlineConfig: AstroInlineConfig, options?: BuildOptions) => Promise<void>`

Similar to [`astro build`](/en/reference/cli-reference/#astro-build), it builds your site for deployment.

```js
import { build } from "astro";


await build({
  root: "./my-project",
});
```

### `BuildOptions`

[Section titled “BuildOptions”](#buildoptions)

```ts
export interface BuildOptions {
  devOutput?: boolean;
  teardownCompiler?: boolean;
}
```

#### `devOutput`

[Section titled “devOutput”](#devoutput)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.4.0`

Output a development-based build similar to code transformed in `astro dev`. This can be useful to test build-only issues with additional debugging information included.

#### `teardownCompiler`

[Section titled “teardownCompiler”](#teardowncompiler)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@5.4.0`

Teardown the compiler WASM instance after build. This can improve performance when building once but may cause a performance hit if building multiple times in a row.

When building multiple projects in the same execution (e.g. during tests), disabling this option can greatly increase performance and reduce peak memory usage at the cost of higher sustained memory usage.

## `preview()`

[Section titled “preview()”](#preview)

**Type:** `(inlineConfig: AstroInlineConfig) => Promise<PreviewServer>`

Similar to [`astro preview`](/en/reference/cli-reference/#astro-preview), it starts a local server to serve your build output.

If no adapter is set in the configuration, the preview server will only serve the built static files. If an adapter is set in the configuration, the preview server is provided by the adapter. Adapters are not required to provide a preview server, so this feature may not be available depending on your adapter of choice.

```js
import { preview } from "astro";


const previewServer = await preview({
  root: "./my-project",
});


// Stop the server if needed
await previewServer.stop();
```

### `PreviewServer`

[Section titled “PreviewServer”](#previewserver)

```ts
export interface PreviewServer {
  host?: string;
  port: number;
  closed(): Promise<void>;
  stop(): Promise<void>;
}
```

#### `host`

[Section titled “host”](#host)

**Type:** `string`

The host where the server is listening for connections.

Adapters are allowed to leave this field unset. The value of `host` is implementation-specific.

#### `port`

[Section titled “port”](#port)

**Type:** `number`

The port where the server is listening for connections.

#### `stop()`

[Section titled “stop()”](#stop-1)

**Type:** `Promise<void>`

Asks the preview server to close, stop accepting requests, and drop idle connections.

The returned `Promise` resolves when the close request has been sent. This does not mean that the server has closed yet. Use the [`closed()`](#closed) method if you need to ensure the server has fully closed.

#### `closed()`

[Section titled “closed()”](#closed)

**Type:** `Promise<void>`

Returns a `Promise` that will resolve once the server is closed and reject if an error happens on the server.

## `sync()`

[Section titled “sync()”](#sync)

**Type:** `(inlineConfig: AstroInlineConfig) => Promise<void>`

Similar to [`astro sync`](/en/reference/cli-reference/#astro-sync), it generates TypeScript types for all Astro modules.

```js
import { sync } from "astro";


await sync({
  root: "./my-project",
});
```

## `mergeConfig()`

[Section titled “mergeConfig()”](#mergeconfig)

**Type:** `<T extends AstroConfig | AstroInlineConfig>(config: T, overrides: DeepPartial<T>) => T`

**Added in:** `astro@5.4.0`

Imported from `astro/config`, merges a partial Astro configuration on top of an existing, valid, Astro configuration.

`mergeConfig()` accepts an Astro config object and a partial config (any set of valid Astro config options), and returns a valid Astro config combining both values such that:

* Arrays are concatenated (including integrations and remark plugins).
* Objects are merged recursively.
* Vite options are merged using [Vite’s own `mergeConfig` function](https://vite.dev/guide/api-javascript#mergeconfig) with the default `isRoot` flag.
* Options that can be provided as functions are wrapped into new functions that recursively merge the return values from both configurations with these same rules.
* All other options override the existing config.

```ts
import { mergeConfig } from "astro/config";


mergeConfig(
  {
    output: 'static',
    site: 'https://example.com',
    integrations: [partytown()],
    server: ({command}) => ({
      port: command === 'dev' ? 4321 : 1234,
    }),
    build: {
      client: './custom-client',
    },
  },
  {
    output: 'server',
    base: '/astro',
    integrations: [mdx()],
    server: ({command}) => ({
      host: command === 'dev' ? 'localhost' : 'site.localhost',
    }),
    build: {
      server: './custom-server',
    },
  }
);


// Result is equivalent to:
{
  output: 'server',
  site: 'https://example.com',
  base: '/astro',
  integrations: [partytown(), mdx()],
  server: ({command}) => ({
    port: command === 'dev' ? 4321 : 1234,
    host: command === 'dev' ? 'localhost' : 'site.localhost',
  }),
  build: {
    client: './custom-client',
    server: './custom-server',
  },
}
```

## `validateConfig()`

[Section titled “validateConfig()”](#validateconfig)

**Type:** `(userConfig: any, root: string, cmd: string): Promise<AstroConfig>`

**Added in:** `astro@5.4.0`

Imported from `astro/config`, validates an object as if it was exported from `astro.config.mjs` and imported by Astro.

It takes the following arguments:

* The configuration to be validated.
* The root directory of the project.
* The Astro command that is being executed (`build`, `dev`, `sync`, etc.)

The returned promise resolves to the validated configuration, filled with all default values appropriate for the given Astro command.

```ts
import { validateConfig } from "astro/config";


const config = await validateConfig({
  integrations: [partytown()],
}, "./my-project", "build");


// defaults are applied
await rm(config.outDir, { recursive: true, force: true });
```

# Publish to npm

> Learn how to publish Astro components to npm

Building a new Astro component? **Publish it to [npm!](https://npmjs.com/)**

Publishing an Astro component is a great way to reuse your existing work across your projects, and to share with the wider Astro community at large. Astro components can be published directly to and installed from npm, just like any other JavaScript package.

Looking for inspiration? Check out some of our favorite [themes](https://astro.build/themes/) and [components](https://astro.build/integrations/) from the Astro community. You can also [search npm](https://www.npmjs.com/search?q=keywords:astro-component,withastro) to see the entire public catalog.

Don’t want to go it alone?

Check out [Astro Community’s component template](https://github.com/astro-community/component-template) for a community-supported, out-of-the-box template!

## Quick Start

[Section titled “Quick Start”](#quick-start)

To get started developing your component quickly, you can use a template already set up for you.

```bash
# Initialize the Astro Component template in a new directory
npm create astro@latest my-new-component-directory -- --template component
# yarn
yarn create astro my-new-component-directory --template component
# pnpm
pnpm create astro@latest my-new-component-directory -- --template component
```

## Creating a package

[Section titled “Creating a package”](#creating-a-package)

Prerequisites

Before diving in, it will help to have a basic understanding of:

* [Node Modules](https://docs.npmjs.com/creating-node-js-modules)
* [Package Manifest (`package.json`)](https://docs.npmjs.com/creating-a-package-json-file)
* [Workspaces](https://docs.npmjs.com/cli/v7/configuring-npm/package-json#workspaces)

To create a new package, configure your development environment to use **workspaces** within your project. This will allow you to develop your component alongside a working copy of Astro.

* my-new-component-directory/

  * demo/

    * … for testing and demonstration

  * package.json

  * packages/

    * my-component/

      * index.js
      * package.json
      * … additional files used by the package

This example, named `my-project`, creates a project with a single package, named `my-component`, and a `demo/` directory for testing and demonstrating the component.

This is configured in the project root’s `package.json` file:

```json
{
  "name": "my-project",
  "workspaces": ["demo", "packages/*"]
}
```

In this example, multiple packages can be developed together from the `packages` directory. These packages can also be referenced from `demo`, where you can install a working copy of Astro.

```shell
npm create astro@latest demo -- --template minimal
# yarn
yarn create astro demo --template minimal
# pnpm
pnpm create astro@latest demo -- --template minimal
```

There are two initial files that will make up your individual package: `package.json` and `index.js`.

### `package.json`

[Section titled “package.json”](#packagejson)

The `package.json` in the package directory includes all of the information related to your package, including its description, dependencies, and any other package metadata.

```json
{
  "name": "my-component",
  "description": "Component description",
  "version": "1.0.0",
  "homepage": "https://github.com/owner/project#readme",
  "type": "module",
  "exports": {
    ".": "./index.js",
    "./astro": "./MyAstroComponent.astro",
    "./react": "./MyReactComponent.jsx"
  },
  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"],
  "keywords": ["astro", "withastro", "astro-component", "...", "..."]
}
```

#### `description`

[Section titled “description”](#description)

A short description of your component used to help others know what it does.

```json
{
  "description": "An Astro Element Generator"
}
```

#### `type`

[Section titled “type”](#type)

The module format used by Node.js and Astro to interpret your `index.js` files.

```json
{
  "type": "module"
}
```

Use `"type": "module"` so that your `index.js` can be used as an entrypoint with `import` and `export` .

#### `homepage`

[Section titled “homepage”](#homepage)

The url to the project homepage.

```json
{
  "homepage": "https://github.com/owner/project#readme"
}
```

This is a great way to direct users to an online demo, documentation, or homepage for your project.

#### `exports`

[Section titled “exports”](#exports)

The entry points of a package when imported by name.

```json
{
  "exports": {
    ".": "./index.js",
    "./astro": "./MyAstroComponent.astro",
    "./react": "./MyReactComponent.jsx"
  }
}
```

In this example, importing `my-component` would use `index.js`, while importing `my-component/astro` or `my-component/react` would use `MyAstroComponent.astro` or `MyReactComponent.jsx` respectively.

#### `files`

[Section titled “files”](#files)

An optional optimization to exclude unnecessary files from the bundle shipped to users via npm. Note that **only files listed here will be included in your package**, so if you add or change files necessary for your package to work, you must update this list accordingly.

```json
{
  "files": ["index.js", "MyAstroComponent.astro", "MyReactComponent.jsx"]
}
```

#### `keywords`

[Section titled “keywords”](#keywords)

An array of keywords relevant to your component, used to help others [find your component on npm](https://www.npmjs.com/search?q=keywords:astro-component,withastro) and in any other search catalogs.

Add `astro-component` or `withastro` as a special keyword to maximize its discoverability in the Astro ecosystem.

```json
{
  "keywords": ["astro-component", "withastro", "... etc", "... etc"]
}
```

Tip

Keywords are also used by our [integrations library](https://astro.build/integrations/)! [See below](#integrations-library) for a full list of keywords we look for in npm.

***

### `index.js`

[Section titled “index.js”](#indexjs)

The main **package entrypoint** used whenever your package is imported.

```js
export { default as MyAstroComponent } from './MyAstroComponent.astro';


export { default as MyReactComponent } from './MyReactComponent.jsx';
```

This allows you to package multiple components together into a single interface.

#### Example: Using Named Imports

[Section titled “Example: Using Named Imports”](#example-using-named-imports)

```astro
---
import { MyAstroComponent } from 'my-component';
import { MyReactComponent } from 'my-component';
---
<MyAstroComponent />
<MyReactComponent />
```

#### Example: Using Namespace Imports

[Section titled “Example: Using Namespace Imports”](#example-using-namespace-imports)

```astro
---
import * as Example from 'example-astro-component';
---
<Example.MyAstroComponent />
<Example.MyReactComponent />
```

#### Example: Using Individual Imports

[Section titled “Example: Using Individual Imports”](#example-using-individual-imports)

```astro
---
import MyAstroComponent from 'example-astro-component/astro';
import MyReactComponent from 'example-astro-component/react';
---
<MyAstroComponent />
<MyReactComponent />
```

***

## Developing your package

[Section titled “Developing your package”](#developing-your-package)

Astro does not have a dedicated “package mode” for development. Instead, you should use a demo project to develop and test your package inside of your project. This can be a private website only used for development, or a public demo/documentation website for your package.

If you are extracting components from an existing project, you can even continue to use that project to develop your now-extracted components.

## Testing your component

[Section titled “Testing your component”](#testing-your-component)

Astro does not currently ship a test runner. *(If you are interested in helping out with this, [join us on Discord!](https://astro.build/chat))*

In the meantime, our current recommendation for testing is:

1. Add a test `fixtures` directory to your `demo/src/pages` directory.

2. Add a new page for every test that you’d like to run.

3. Each page should include some different component usage that you’d like to test.

4. Run `astro build` to build your fixtures, then compare the output of the `dist/__fixtures__/` directory to what you expected.

   * my-project/demo/src/pages/\_\_fixtures\_\_/

     * test-name-01.astro
     * test-name-02.astro
     * test-name-03.astro

## Publishing your component

[Section titled “Publishing your component”](#publishing-your-component)

Once you have your package ready, you can publish it to npm using the `npm publish` command. If that fails, make sure that you have logged in via `npm login` and that your `package.json` is correct. If it succeeds, you’re done!

Notice that there was no `build` step for Astro packages. Any file type that Astro supports natively, such as `.astro`, `.ts`, `.jsx`, and `.css`, can be published directly without a build step.

If you need another file type that isn’t natively supported by Astro, add a build step to your package. This advanced exercise is left up to you.

## Integrations Library

[Section titled “Integrations Library”](#integrations-library)

Share your hard work by adding your integration to our [integrations library](https://astro.build/integrations/)!

Tip

Do you need some help building your integration, or just want to meet other integrations builders? We have a dedicated `#integrations` channel on our [Discord server](https://astro.build/chat). Come say hi!

### `package.json` data

[Section titled “package.json data”](#packagejson-data)

The library is automatically updated weekly, pulling in every package published to npm with the `astro-component` or `withastro` keyword.

The integrations library reads the `name`, `description`, `repository`, and `homepage` data from your `package.json`.

Avatars are a great way to highlight your brand in the library! Once your package is published you can [file a GitHub issue](https://github.com/withastro/astro.build/issues/new/choose) with your avatar attached and we will add it to your listing.

Tip

Need to override the information our library reads from npm? No problem! [File an issue](https://github.com/withastro/astro.build/issues/new/choose) with the updated information and we’ll make sure the custom `name`, `description`, or `homepage` is used instead.

### Categories

[Section titled “Categories”](#categories)

In addition to the required `astro-component` or `withastro` keyword, special keywords are also used to automatically organize packages. Including any of the keywords below will add your integration to the matching category in our integrations library.

| category          | keywords                                     |
| ----------------- | -------------------------------------------- |
| Accessibility     | `a11y`, `accessibility`                      |
| Adapters          | `astro-adapter`                              |
| Analytics         | `analytics`                                  |
| CSS + UI          | `css`, `ui`, `icon`, `icons`, `renderer`     |
| Frameworks        | `renderer`                                   |
| Content Loaders   | `astro-loader`                               |
| Images + Media    | `media`, `image`, `images`, `video`, `audio` |
| Performance + SEO | `performance`, `perf`, `seo`, `optimization` |
| Dev Toolbar       | `devtools`, `dev-overlay`, `dev-toolbar`     |
| Utilities         | `tooling`, `utils`, `utility`                |

Packages that don’t include any keyword matching a category will be shown as `Uncategorized`.

## Share

[Section titled “Share”](#share)

We encourage you to share your work, and we really do love seeing what our talented Astronauts create. Come and share what you create with us in our [Discord](https://astro.build/chat) or mention [@astrodotbuild](https://twitter.com/astrodotbuild) in a Tweet!

# Routing Reference

There is no separate routing configuration in Astro.

Every [supported page file](/en/basics/astro-pages/#supported-page-files) located within the special `src/pages/` directory creates a route. When the file name contains a [parameter](#params), a route can create multiple pages dynamically, otherwise it creates a single page.

By default, all Astro page routes and endpoints are generated and prerendered at build time. [On-demand server rendering](/en/guides/on-demand-rendering/) can be set for individual routes, or as the default.

## `prerender`

[Section titled “prerender”](#prerender)

**Type:** `boolean`\
**Default:** `true` in static mode (default); `false` with `output: 'server'` configuration

**Added in:** `astro@1.0.0`

A value exported from each individual route to determine whether or not it is prerendered.

By default, all pages and endpoints are prerendered and will be statically generated at build time. You can opt out of prerendering on one or more routes, and you can have both static and on-demand rendered routes in the same project.

### Per-page override

[Section titled “Per-page override”](#per-page-override)

You can override the default value to enable [on demand rendering](/en/guides/on-demand-rendering/) for an individual route by exporting `prerender` with the value `false` from that file:

src/pages/rendered-on-demand.astro

```astro
---
export const prerender = false
---
<!-- server-rendered content -->
<!-- the rest of my site is static -->
```

### Switch to `server` mode

[Section titled “Switch to server mode”](#switch-to-server-mode)

You can override the default value for all routes by configuring [`output: 'server'`](/en/reference/configuration-reference/#output). In this output mode, all pages and endpoints will be generated on the server upon request by default instead of being prerendered.

In `server` mode, enable prerendering for an individual route by exporting `prerender` with the value `true` from that file:

src/pages/static-about-page.astro

```astro
---
// with `output: 'server'` configured
export const prerender = true
---
<!-- My static about page -->
<!-- All other pages are rendered on demand -->
```

## `partial`

[Section titled “partial”](#partial)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@3.4.0`

A value exported from an individual route to determine whether or not it should be rendered as a full HTML page.

By default, all files located within the reserved `src/pages/` directory automatically include the `<!DOCTYPE html>` declaration and additional `<head>` content such as Astro’s scoped styles and scripts.

You can override the default value to designate the content as a [page partial](/en/basics/astro-pages/#page-partials) for an individual route by exporting a value for `partial` from that file:

src/pages/my-page-partial.astro

```astro
---
export const partial = true
---
<!-- Generated HTML available at a URL -->
<!-- Available to a rendering library -->
```

The `export const partial` must be identifiable statically. It can have the value of:

* The boolean **`true`**.
* An environment variable using import.meta.env such as `import.meta.env.USE_PARTIALS`.

## `getStaticPaths()`

[Section titled “getStaticPaths()”](#getstaticpaths)

**Type:** `(options: GetStaticPathsOptions) => Promise<GetStaticPathsResult> | GetStaticPathsResult`

**Added in:** `astro@1.0.0`

A function to generate multiple, prerendered page routes from a single `.astro` page component with one or more [parameters](#params) in its file path. Use this for routes that will be created at build time, also known as static site building.

The `getStaticPaths()` function must return an array of objects to determine which URL paths will be prerendered by Astro. Each object must include a `params` object, to specify route paths. The object may optionally contain a `props` object with [data to be passed](#data-passing-with-props) to each page template.

src/pages/blog/\[post].astro

```astro
---
// In 'server' mode, opt in to prerendering:
// export const prerender = true


export async function getStaticPaths() {
  return [
    // { params: { /* required */ }, props: { /* optional */ } },
    { params: { post: '1' } }, // [post] is the parameter
    { params: { post: '2' } }, // must match the file name
    // ...
  ];
}
---
<!-- Your HTML template here. -->
```

`getStaticPaths()` can also be used in static file endpoints for [dynamic routing](/en/guides/endpoints/#params-and-dynamic-routing).

Tip

When using TypeScript, use the [`GetStaticPaths`](/en/guides/typescript/#infer-getstaticpaths-types) type utility to ensure type-safe access of your `params` and `props`.

Caution

The `getStaticPaths()` function executes in its own isolated scope once, before any page loads. Therefore you can’t reference anything from its parent scope, other than file imports. The compiler will warn you if you break this requirement.

### `params`

[Section titled “params”](#params)

The `params` key of each object in the array returned by `getStaticPaths()` tells Astro what routes to build.

The keys in `params` must match the parameters defined in your component file path. The value for each `params` object must match the parameters used in the page name. `params` are encoded into the URL, so only strings are supported as values.

For example,`src/pages/posts/[id].astro`has an `id` parameter in its file name. The following `getStaticPaths()` function in this `.astro` component tells Astro to statically generate `posts/1`, `posts/2`, and `posts/3` at build time.

src/pages/posts/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: '1' } },
    { params: { id: '2' } },
    { params: { id: '3' } }
  ];
}


const { id } = Astro.params;
---
<h1>{id}</h1>
```

### Data passing with `props`

[Section titled “Data passing with props”](#data-passing-with-props)

To pass additional data to each generated page, you can set a `props` value on each object in the array returned by `getStaticPaths()`. Unlike `params`, `props` are not encoded into the URL and so aren’t limited to only strings.

For example, if you generate pages with data fetched from a remote API, you can pass the full data object to the page component inside of `getStaticPaths()`. The page template can reference the data from each post using `Astro.props`.

src/pages/posts/\[id].astro

```astro
---
export async function getStaticPaths() {
  const response = await fetch('...');
  const data = await response.json();


  return data.map((post) => {
    return {
      params: { id: post.id },
      props: { post },
    };
  });
}


const { id } = Astro.params;
const { post } = Astro.props;
---
<h1>{id}: {post.name}</h1>
```

### `routePattern`

[Section titled “routePattern”](#routepattern)

**Type:** `string`

**Added in:** `astro@5.14.0`

A property available in [`getStaticPaths()`](#getstaticpaths) options to access the current [`routePattern`](/en/reference/api-reference/#routepattern) as a string.

This provides data from the [Astro render context](/en/reference/api-reference/) that would not otherwise be available within the scope of `getStaticPaths()` and can be useful to calculate the `params` and `props` for each page route.

`routePattern` always reflects the original dynamic segment definition in the file path (e.g. `/[...locale]/[files]/[slug]`), unlike `params`, which are explicit values for a page (e.g. `/fr/fichiers/article-1/`).

The following example shows how to localize your route segments and return an array of static paths by passing `routePattern` to a custom `getLocalizedData()` helper function. The [params](/en/reference/routing-reference/#params) object will be set with explicit values for each route segment: `locale`, `files`, and `slug`. Then, these values will be used to generate the routes and can be used in your page template via `Astro.params`.

src/pages/\[...locale]/\[files]/\[slug].astro

```astro
---
import { getLocalizedData } from "../../../utils/i18n";


export async function getStaticPaths({ routePattern }) {
  const response = await fetch('...');
  const data = await response.json();


  console.log(routePattern); // [...locale]/[files]/[slug]


  // Call your custom helper with `routePattern` to generate the static paths
  return data.flatMap((file) => getLocalizedData(file, routePattern));
}


const { locale, files, slug } = Astro.params;
---
```

### `paginate()`

[Section titled “paginate()”](#paginate)

**Added in:** `astro@1.0.0`

A function that can be returned from [`getStaticPaths()`](#getstaticpaths) to divide a collection of content items into separate pages.

`paginate()` will automatically generate the necessary array to return from `getStaticPaths()` to create one URL for every page of your paginated collection. The page number will be passed as a `param`, and the page data will be passed as a `page` prop.

The following example fetches and passes 150 items to the `paginate` function, and creates static, prerendered pages at build time that will display 10 items per page:

src/pages/pokemon/\[page].astro

```astro
---
export async function getStaticPaths({ paginate }) {
  // Load your data with fetch(), getCollection(), etc.
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon?limit=150`);
  const result = await response.json();
  const allPokemon = result.results;


  // Return a paginated collection of paths for all items
  return paginate(allPokemon, { pageSize: 10 });
}


const { page } = Astro.props;
---
```

`paginate()` has the following arguments:

* `data` - array containing the page’s data passed to the `paginate()` function

* `options` - Optional object with the following properties:

  * `pageSize` - The number of items shown per page (`10` by default)
  * `params` - Send additional parameters for creating dynamic routes
  * `props` - Send additional props to be available on each page

`paginate()` assumes a file name of `[page].astro` or `[...page].astro`. The `page` param becomes the page number in your URL:

* `/posts/[page].astro` would generate the URLs `/posts/1`, `/posts/2`, `/posts/3`, etc.
* `/posts/[...page].astro` would generate the URLs `/posts`, `/posts/2`, `/posts/3`, etc.

#### The pagination `page` prop

[Section titled “The pagination page prop”](#the-pagination-page-prop)

**Type:** `Page<TData>`

Pagination will pass a `page` prop to every rendered page that represents a single page of data in the paginated collection. This includes the data that you’ve paginated (`page.data`) as well as metadata for the page (`page.url`, `page.start`, `page.end`, `page.total`, etc). This metadata is useful for things like a “Next Page” button or a “Showing 1-10 of 100” message.

##### `page.data`

[Section titled “page.data”](#pagedata)

**Type:** `Array<TData>`

Array of data returned from the `paginate()` function for the current page.

##### `page.start`

[Section titled “page.start”](#pagestart)

**Type:** `number`

Index of the first item on the current page, starting at `0`. (e.g. if `pageSize: 25`, this would be `0` on page 1, `25` on page 2, etc.)

##### `page.end`

[Section titled “page.end”](#pageend)

**Type:** `number`

Index of the last item on the current page.

##### `page.size`

[Section titled “page.size”](#pagesize)

**Type:** `number`\
**Default:** `10`

The total number of items per page.

##### `page.total`

[Section titled “page.total”](#pagetotal)

**Type:** `number`

The total number of items across all pages.

##### `page.currentPage`

[Section titled “page.currentPage”](#pagecurrentpage)

**Type:** `number`

The current page number, starting with `1`.

##### `page.lastPage`

[Section titled “page.lastPage”](#pagelastpage)

**Type:** `number`

The total number of pages.

##### `page.url.current`

[Section titled “page.url.current”](#pageurlcurrent)

**Type:** `string`

Get the URL of the current page (useful for canonical URLs). If a value is set for [`base`](/en/reference/configuration-reference/#base), the URL starts with that value.

##### `page.url.prev`

[Section titled “page.url.prev”](#pageurlprev)

**Type:** `string | undefined`

Get the URL of the previous page (will be `undefined` if on page 1). If a value is set for [`base`](/en/reference/configuration-reference/#base), prepend the base path to the URL.

##### `page.url.next`

[Section titled “page.url.next”](#pageurlnext)

**Type:** `string | undefined`

Get the URL of the next page (will be `undefined` if no more pages). If a value is set for [`base`](/en/reference/configuration-reference/#base), prepend the base path to the URL.

##### `page.url.first`

[Section titled “page.url.first”](#pageurlfirst)

**Type:** `string | undefined`

**Added in:** `astro@4.12.0`

Get the URL of the first page (will be `undefined` if on page 1). If a value is set for [`base`](/en/reference/configuration-reference/#base), prepend the base path to the URL.

##### `page.url.last`

[Section titled “page.url.last”](#pageurllast)

**Type:** `string | undefined`

**Added in:** `astro@4.12.0`

Get the URL of the last page (will be `undefined` if no more pages). If a value is set for [`base`](/en/reference/configuration-reference/#base), prepend the base path to the URL.


---

**Navigation:** [← Previous](./13-invalid-entry-inside-getstaticpaths-return-value.md) | [Index](./index.md) | [Next →](./15-build-your-first-astro-blog.md)
