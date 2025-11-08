**Navigation:** [← Previous](./06-add-integrations.md) | [Index](./index.md) | [Next →](./08-migrating-from-nextjs.md)

---

# @astrojs/vercel

> Learn how to use the @astrojs/vercel adapter to deploy your Astro project.

This adapter allows Astro to deploy your [on-demand rendered routes and features](/en/guides/on-demand-rendering/) to [Vercel](https://www.vercel.com/), including [server islands](/en/guides/server-islands/), [actions](/en/guides/actions/), and [sessions](/en/guides/sessions/).

If you’re using Astro as a static site builder, you only need this adapter if you are using additional Vercel services (e.g. [Vercel Web Analytics](https://vercel.com/docs/analytics), [Vercel Image Optimization](https://vercel.com/docs/image-optimization)). Otherwise, you do not need an adapter to deploy your static site.

Learn how to deploy your Astro site in our [Vercel deployment guide](/en/guides/deploy/vercel/).

## Why Astro Vercel?

[Section titled “Why Astro Vercel?”](#why-astro-vercel)

[Vercel](https://www.vercel.com/) is a deployment platform that allows you to host your site by connecting directly to your GitHub repository. This adapter enhances the Astro build process to prepare your project for deployment through Vercel.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

Add the Vercel adapter to enable on-demand rendering in your Astro project with the following `astro add` command. This will install `@astrojs/vercel` and make the appropriate changes to your `astro.config.mjs` file in one step.

* npm

  ```sh
  npx astro add vercel
  ```

* pnpm

  ```sh
  pnpm astro add vercel
  ```

* Yarn

  ```sh
  yarn astro add vercel
  ```

Now, you can enable [on-demand rendering per page](/en/guides/on-demand-rendering/#enabling-on-demand-rendering), or set your build output configuration to `output: 'server'` to [server-render all your pages by default](/en/guides/on-demand-rendering/#server-mode).

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, add the `@astrojs/vercel` adapter to your project’s dependencies using your preferred package manager:

* npm

  ```sh
  npm install @astrojs/vercel
  ```

* pnpm

  ```sh
  pnpm add @astrojs/vercel
  ```

* Yarn

  ```sh
  yarn add @astrojs/vercel
  ```

Then, add the adapter to your `astro.config.*` file:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
+  adapter: vercel(),
});
```

## Usage

[Section titled “Usage”](#usage)

Find out more about [deploying your project to Vercel](/en/guides/deploy/vercel/).

You can deploy by CLI (`vercel deploy`) or by connecting your new repo in the [Vercel Dashboard](https://vercel.com/). Alternatively, you can create a production build locally:

```sh
astro build
vercel deploy --prebuilt
```

## Configuration

[Section titled “Configuration”](#configuration)

To configure this adapter, pass an object to the `vercel()` function call in `astro.config.mjs`:

### `webAnalytics`

[Section titled “webAnalytics”](#webanalytics)

**Type:** `VercelWebAnalyticsConfig`\
**Available for:** Serverless, Static

**Added in:** `@astrojs/vercel@3.8.0`

With `@vercel/analytics@1.3.x` or earlier, you can set `webAnalytics: { enabled: true }` in your Astro config to inject Vercel’s tracking scripts into all of your pages.

For `@vercel/analytics@1.4.0` and later, use Vercel’s Analytics component to enable [Vercel Web Analytics](https://vercel.com/docs/concepts/analytics) instead.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
+    webAnalytics: {
+      enabled: true,
+    },
  }),
});
```

### `imagesConfig`

[Section titled “imagesConfig”](#imagesconfig)

**Type:** `VercelImageConfig`\
**Available for:** Serverless, Static

**Added in:** `@astrojs/vercel@3.3.0`

Configuration options for [Vercel’s Image Optimization API](https://vercel.com/docs/concepts/image-optimization). See [Vercel’s image configuration documentation](https://vercel.com/docs/build-output-api/v3/configuration#images) for a complete list of supported parameters.

The `domains` and `remotePatterns` properties will automatically be filled using [the Astro corresponding `image` settings](/en/reference/configuration-reference/#image-options).

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  output: 'static',
  adapter: vercel({
+    imagesConfig: {
+      sizes: [320, 640, 1280],
+    },
  }),
});
```

### `imageService`

[Section titled “imageService”](#imageservice)

**Type:** `boolean`\
**Available for:** Serverless, Static

**Added in:** `@astrojs/vercel@3.3.0`

When enabled, an [Image Service](/en/reference/image-service-reference/) powered by the Vercel Image Optimization API will be automatically configured and used in production. In development, the image service specified by [`devImageService`](#devimageservice) will be used instead.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  output: 'static',
  adapter: vercel({
+    imageService: true,
  }),
});
```

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import astroLogo from '../assets/logo.png';
---


<!-- This component -->
<Image src={astroLogo} alt="My super logo!" />


<!-- will become the following HTML -->
<img
  src="/_vercel/image?url=_astro/logo.hash.png&w=...&q=..."
  alt="My super logo!"
  loading="lazy"
  decoding="async"
  width="..."
  height="..."
/>
```

### `devImageService`

[Section titled “devImageService”](#devimageservice)

**Type:** `'sharp' | string`\
**Default:** `sharp`\
**Available for:** Serverless, Static

**Added in:** `@astrojs/vercel@3.8.0`

Allows you to configure which image service to use in development when [imageService](#imageservice) is enabled. This can be useful if you cannot install Sharp’s dependencies on your development machine, but using another image service like Squoosh would allow you to preview images in your dev environment. Build is unaffected and will always use Vercel’s Image Optimization.

It can also be set to any arbitrary value in order to use a custom image service instead of Astro’s built-in ones.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
+    imageService: true,
+    devImageService: 'sharp',
  }),
});
```

### `isr`

[Section titled “isr”](#isr)

**Type:** `boolean | VercelISRConfig`\
**Default:** `false`\
**Available for:** Serverless

**Added in:** `@astrojs/vercel@7.2.0`

Allows your project to be deployed as an [ISR (Incremental Static Regeneration)](https://vercel.com/docs/incremental-static-regeneration) function, which caches your on-demand rendered pages in the same way as prerendered pages after first request.

To enable this feature, set `isr` to true in your Vercel adapter configuration in `astro.config.mjs`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
+    isr: true,
  }),
});
```

Note that ISR function requests do not include search params, similar to [requests](/en/reference/api-reference/#request) in static mode.

#### ISR cache invalidation

[Section titled “ISR cache invalidation”](#isr-cache-invalidation)

By default, an ISR function caches for the duration of your deployment. You can further control caching by setting an expiration time, or by excluding particular routes from caching entirely.

##### Time-based invalidation

[Section titled “Time-based invalidation”](#time-based-invalidation)

You can change the length of time to cache routes this by configuring an `expiration` value in seconds:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
    isr: {
      // caches all pages on first request and saves for 1 day
      expiration: 60 * 60 * 24,
    },
  }),
});
```

##### Excluding paths from caching

[Section titled “Excluding paths from caching”](#excluding-paths-from-caching)

To implement Vercel’s [Draft mode](https://vercel.com/docs/build-output-api/v3/features#draft-mode), or [On-Demand Incremental Static Regeneration (ISR)](https://vercel.com/docs/build-output-api/v3/features#on-demand-incremental-static-regeneration-isr), you can create a bypass token and provide it to the `isr` config along with any routes to exclude from caching:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
    adapter: vercel({
        isr: {
            // A secret random string that you create.
            bypassToken: "005556d774a8",
            // Paths that will always be served fresh.
            exclude: [
              '/preview',
              '/auth/[page]',
              /^\/api\/.+/ // Regular expressions supported since @astrojs/vercel@v8.1.0
            ]
        }
    })
})
```

### `includeFiles`

[Section titled “includeFiles”](#includefiles)

**Type:** `string[]`\
**Available for:** Serverless

Use this property to force files to be bundled with your function. This is helpful when you notice missing files.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
+    includeFiles: ['./my-data.json'],
  }),
});
```

### `excludeFiles`

[Section titled “excludeFiles”](#excludefiles)

**Type:** `string[]`\
**Available for:** Serverless

Use this property to exclude any files from the bundling process that would otherwise be included.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
+    excludeFiles: ['./src/some_big_file.jpg'],
  }),
});
```

### `maxDuration`

[Section titled “maxDuration”](#maxduration)

**Type:** `number`\
**Available for:** Serverless

Use this property to extend or limit the maximum duration (in seconds) that Serverless Functions can run before timing out. See the [Vercel documentation](https://vercel.com/docs/functions/serverless-functions/runtimes#maxduration) for the default and maximum limit for your account plan.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
// ...
  adapter: vercel({
+    maxDuration: 60
  }),
});
```

### `skewProtection`

[Section titled “skewProtection”](#skewprotection)

**Type:** `boolean`\
**Available for:** Serverless

**Added in:** `@astrojs/vercel@7.6.0`

Use this property to enable [Vercel Skew protection](https://vercel.com/docs/deployments/skew-protection) (available with Vercel Pro and Enterprise accounts).

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
// ...
  adapter: vercel({
+    skewProtection: true
  }),
});
```

### Running Astro middleware on Vercel Edge Functions

[Section titled “Running Astro middleware on Vercel Edge Functions”](#running-astro-middleware-on-vercel-edge-functions)

The `@astrojs/vercel` adapter can create an [edge function](https://vercel.com/docs/functions/edge-functions) from an Astro middleware in your code base. When `edgeMiddleware` is enabled, an edge function will execute your middleware code for all requests including static assets, prerendered pages, and on-demand rendered pages.

For on-demand rendered pages, the `context.locals` object is serialized using JSON and sent in a header for the serverless function, which performs the rendering. As a security measure, the serverless function will refuse to serve requests with a `403 Forbidden` response unless they come from the generated edge function.

This is an opt-in feature. To enable it, set `edgeMiddleware` to `true`:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  // ...
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

The edge middleware has access to Vercel’s [`RequestContext`](https://vercel.com/docs/functions/edge-middleware/middleware-api#requestcontext) as `ctx.locals.vercel.edge`. If you’re using TypeScript, you can [get proper typings](/en/guides/typescript/#extending-global-types) by updating `src/env.d.ts` to use `EdgeLocals`:

```ts
type EdgeLocals = import('@astrojs/vercel').EdgeLocals


declare namespace App {
  interface Locals extends EdgeLocals {
    // ...
  }
}
```

### Sessions

[Section titled “Sessions”](#sessions)

The Astro [Sessions API](/en/guides/sessions/) allows you to easily store user data between requests. This can be used for things like user data and preferences, shopping carts, and authentication credentials. Unlike cookie storage, there are no size limits on the data, and it can be restored on different devices.

When using sessions on Vercel, you need to [configure a driver](/en/reference/configuration-reference/#sessiondriver) for session storage. You can install a storage provider from [the Vercel marketplace](https://vercel.com/marketplace?category=storage).

For example, if you have installed [a Redis integration](https://vercel.com/marketplace?category=storage\&search=redis) and linked a database to your site:

1. Install the `ioredis` package:

   * npm

     ```sh
     npm install ioredis
     ```

   * pnpm

     ```sh
     pnpm install ioredis
     ```

   * Yarn

     ```sh
     yarn add ioredis
     ```

2. Use [the Vercel CLI](https://vercel.com/docs/cli) to load your environment variables:

   ```sh
   vercel env pull .env.local
   ```

   This will create a `.env.local` file in your project root with the environment variables needed to connect to your Redis database when developing locally.

3. Configure the session driver:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   import vercel from '@astrojs/vercel';


   export default defineConfig({
     adapter: vercel(),
   +  session: {
   +    driver: 'redis',
   +    options: {
   +      url: process.env.REDIS_URL,
   +    },
   +  },
   });
   ```

## Node.js Version Support

[Section titled “Node.js Version Support”](#nodejs-version-support)

The `@astrojs/vercel` adapter supports specific Node.js versions for deploying your Astro project on Vercel. To view the supported Node.js versions on Vercel, click on the settings tab for a project and scroll down to “Node.js Version” section.

Check out the [Vercel documentation](https://vercel.com/docs/functions/serverless-functions/runtimes/node-js#default-and-available-versions) to learn more.

## Experimental features

[Section titled “Experimental features”](#experimental-features)

The following features are also available for use, but may be subject to breaking changes in future updates. Please follow the [`@astrojs/vercel` CHANGELOG](https://github.com/withastro/astro/tree/main/packages/integrations/vercel/CHANGELOG.md) carefully for updates if you are using these features in your project.

### `experimentalStaticHeaders`

[Section titled “experimentalStaticHeaders”](#experimentalstaticheaders)

**Type:** `boolean`\
**Default:** `false`\
**Available for:** Serverless

**Added in:** `@astrojs/vercel@8.2.0`

Enables specifying custom headers for prerendered pages in Vercel’s configuration.

If enabled, the adapter will save [static headers in the Vercel `vercel.json` file](https://vercel.com/docs/project-configuration#headers) when provided by Astro features, such as Content Security Policy.

For example, when [experimental Content Security Policy](/en/reference/experimental-flags/csp/) is enabled, `experimentalStaticHeaders` can be used to add the CSP `headers` to your Vercel configuration, instead of creating a `<meta>` element:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';


export default defineConfig({
  experimental: {
    csp: true
  },
  adapter: vercel({
    experimentalStaticHeaders: true
  })
});
```

# @astrojs/vue

> Learn how to use the @astrojs/vue framework integration to extend component support in your Astro project.

This **[Astro integration](/en/guides/integrations-guide/)** enables rendering and client-side hydration for your [Vue 3](https://vuejs.org/) components.

## Installation

[Section titled “Installation”](#installation)

Astro includes an `astro add` command to automate the setup of official integrations. If you prefer, you can [install integrations manually](#manual-install) instead.

To install `@astrojs/vue`, run the following from your project directory and follow the prompts:

* npm

  ```sh
  npx astro add vue
  ```

* pnpm

  ```sh
  pnpm astro add vue
  ```

* Yarn

  ```sh
  yarn astro add vue
  ```

If you run into any issues, [feel free to report them to us on GitHub](https://github.com/withastro/astro/issues) and try the manual installation steps below.

### Manual Install

[Section titled “Manual Install”](#manual-install)

First, install the `@astrojs/vue` package:

* npm

  ```sh
  npm install @astrojs/vue
  ```

* pnpm

  ```sh
  pnpm add @astrojs/vue
  ```

* Yarn

  ```sh
  yarn add @astrojs/vue
  ```

Most package managers will install associated peer dependencies as well. If you see a `Cannot find package 'vue'` (or similar) warning when you start up Astro, you’ll need to install Vue:

* npm

  ```sh
  npm install vue
  ```

* pnpm

  ```sh
  pnpm add vue
  ```

* Yarn

  ```sh
  yarn add vue
  ```

Then, apply the integration to your `astro.config.*` file using the `integrations` property:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [vue()],
});
```

## Getting started

[Section titled “Getting started”](#getting-started)

To use your first Vue component in Astro, head to our [UI framework documentation](/en/guides/framework-components/#using-framework-components). You’ll explore:

* 📦 how framework components are loaded,
* 💧 client-side hydration options, and
* 🤝 opportunities to mix and nest frameworks together

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

For help, check out the `#support` channel on [Discord](https://astro.build/chat). Our friendly Support Squad members are here to help!

You can also check our [Astro Integration Documentation](/en/guides/integrations-guide/) for more on integrations.

## Contributing

[Section titled “Contributing”](#contributing)

This package is maintained by Astro’s Core team. You’re welcome to submit an issue or PR!

## Options

[Section titled “Options”](#options)

This integration is powered by `@vitejs/plugin-vue`. To customize the Vue compiler, options can be provided to the integration. See the `@vitejs/plugin-vue` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue) for more details.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [
    vue({
      template: {
        compilerOptions: {
          // treat any tag that starts with ion- as custom elements
          isCustomElement: (tag) => tag.startsWith('ion-'),
        },
      },
      // ...
    }),
  ],
});
```

### `appEntrypoint`

[Section titled “appEntrypoint”](#appentrypoint)

**Type:** `string`

**Added in:** `@astrojs/vue@1.2.0`

You can extend the Vue `app` instance setting the `appEntrypoint` option to a root-relative import specifier (for example, `appEntrypoint: "/src/pages/_app"`).

The default export of this file should be a function that accepts a Vue `App` instance prior to rendering, allowing the use of [custom Vue plugins](https://vuejs.org/guide/reusability/plugins.html), `app.use`, and other customizations for advanced use cases.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [vue({ appEntrypoint: '/src/pages/_app' })],
});
```

src/pages/\_app.ts

```ts
import type { App } from 'vue';
import i18nPlugin from 'my-vue-i18n-plugin';


export default (app: App) => {
  app.use(i18nPlugin);
};
```

### `jsx`

[Section titled “jsx”](#jsx)

**Type:** `boolean | object`

**Added in:** `@astrojs/vue@1.2.0`

You can use Vue JSX by setting `jsx: true`.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [vue({ jsx: true })],
});
```

This will enable rendering for both Vue and Vue JSX components. To customize the Vue JSX compiler, pass an options object instead of a boolean. See the `@vitejs/plugin-vue-jsx` [docs](https://www.npmjs.com/package/@vitejs/plugin-vue-jsx) for more details.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [
    vue({
      jsx: {
        // treat any tag that starts with ion- as custom elements
        isCustomElement: (tag) => tag.startsWith('ion-'),
      },
    }),
  ],
});
```

### `devtools`

[Section titled “devtools”](#devtools)

**Type:** `boolean | object`

**Added in:** `@astrojs/vue@4.2.0`

You can enable [Vue DevTools](https://devtools-next.vuejs.org/) in development by passing an object with `devtools: true` to your `vue()` integration config:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import vue from '@astrojs/vue';


export default defineConfig({
  // ...
  integrations: [vue({ devtools: true })],
});
```

#### Customizing Vue DevTools

[Section titled “Customizing Vue DevTools”](#customizing-vue-devtools)

**Added in:** `@astrojs/vue@4.3.0`

For more customization, you can instead pass options that the [Vue DevTools Vite Plugin](https://devtools-next.vuejs.org/guide/vite-plugin#options) supports. (Note: `appendTo` is not supported.)

For example, you can set `launchEditor` to your preferred editor if you are not using Visual Studio Code:

astro.config.mjs

```js
import { defineConfig } from "astro/config";
import vue from "@astrojs/vue";


export default defineConfig({
  // ...
  integrations: [
    vue({
      devtools: { launchEditor: "webstorm" },
    }),
  ],
});
```

# Internationalization (i18n) Routing

> Learn how to use Astro’s i18n routing features to localize your site’s pages.

Astro’s internationalization (i18n) features allow you to adapt your project for an international audience. This routing API helps you generate, use, and verify the URLs that your multi-language site produces.

Astro’s i18n routing allows you to bring your multilingual content with support for configuring a default language, computing relative page URLs, and accepting preferred languages provided by your visitor’s browser. You can also specify fallback languages on a per-language basis so that your visitors can always be directed to existing content on your site.

## Routing Logic

[Section titled “Routing Logic”](#routing-logic)

Astro uses a [middleware](/en/guides/middleware/) to implement its routing logic. This middleware function is placed in the [first position](/en/guides/middleware/#chaining-middleware) where it awaits every `Response` coming from any additional middleware and each page route before finally executing its own logic.

This means that operations (e.g. redirects) from your own middleware and your page logic are run first, your routes are rendered, and then the i18n middleware performs its own actions such as verifying that a localized URL corresponds to a valid route.

You can also choose to [add your own i18n logic in addition to or instead of Astro’s i18n middleware](#manual), giving you even more control over your routes while still having access to the `astro:i18n` helper functions.

## Configure i18n routing

[Section titled “Configure i18n routing”](#configure-i18n-routing)

Both a list of all supported languages ([`locales`](/en/reference/configuration-reference/#i18nlocales)) and a default language ([`defaultLocale`](/en/reference/configuration-reference/#i18ndefaultlocale)), which must be one of the languages listed in `locales`, need to be specified in an `i18n` configuration object. Additionally, you can configure more specific routing and fallback behavior to match your desired URLs.

astro.config.mjs

```js
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
    locales: ["es", "en", "pt-br"],
    defaultLocale: "en",
  }
})
```

### Create localized folders

[Section titled “Create localized folders”](#create-localized-folders)

Organize your content folders with localized content by language. Create individual `/[locale]/` folders anywhere within `src/pages/` and Astro’s [file-based routing](/en/guides/routing/) will create your pages at corresponding URL paths.

Your folder names must match the items in `locales` exactly. Include a localized folder for your `defaultLocale` only if you configure `prefixDefaultLocale: true` to show a localized URL path for your default language (e.g. `/en/about/`).

* src

  * pages

    * about.astro

    * index.astro

    * es

      * about.astro
      * index.astro

    * pt-br

      * about.astro
      * index.astro

Note

The localized folders do not need to be at the root of the `/pages/` folder.

### Create links

[Section titled “Create links”](#create-links)

With i18n routing configured, you can now compute links to pages within your site using the helper functions such as [`getRelativeLocaleUrl()`](/en/reference/modules/astro-i18n/#getrelativelocaleurl) available from the [`astro:i18n` module](/en/reference/modules/astro-i18n/). These generated links will always provide the correct, localized route and can help you correctly use, or check, URLs on your site.

You can also still write the links manually.

src/pages/es/index.astro

```astro
---
import { getRelativeLocaleUrl } from 'astro:i18n';


// defaultLocale is "es"
const aboutURL = getRelativeLocaleUrl("es", "about");
---


<a href="/get-started/">¡Vamos!</a>
<a href={getRelativeLocaleUrl('es', 'blog')}>Blog</a>
<a href={aboutURL}>Acerca</a>
```

## `routing`

[Section titled “routing”](#routing)

Astro’s built-in file-based routing automatically creates URL routes for you based on your file structure within `src/pages/`.

When you configure i18n routing, information about this file structure (and the corresponding URL paths generated) is available to the i18n helper functions so they can generate, use, and verify the routes in your project. Many of these options can be used together for even more customization and per-language flexibility.

You can even choose to [implement your own routing logic manually](#manual) for even greater control.

### `prefixDefaultLocale`

[Section titled “prefixDefaultLocale”](#prefixdefaultlocale)

**Added in:** `astro@3.5.0`

This routing option defines whether or not your default language’s URLs should use a language prefix (e.g. `/en/about/`).

All non-default supported languages **will** use a localized prefix (e.g. `/fr/` or `/french/`) and content files must be located in appropriate folders. This configuration option allows you to specify whether your default language should also follow a localized URL structure.

This setting also determines where the page files for your default language must exist (e.g. `src/pages/about/` or `src/pages/en/about`) as the file structure and URL structure must match for all languages.

* `"prefixDefaultLocale: false"` (default): URLs in your default language will **not** have a `/[locale]/` prefix. All other locales will.

* `"prefixDefaultLocale: true"`: All URLs, including your default language, will have a `/[locale]/` prefix.

#### `prefixDefaultLocale: false`

[Section titled “prefixDefaultLocale: false”](#prefixdefaultlocale-false)

astro.config.mjs

```diff
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
    locales: ["es", "en", "fr"],
    defaultLocale: "en",
    routing: {
+        prefixDefaultLocale: false
    }
  }
})
```

This is the **default** value. Set this option when URLs in your default language will **not** have a `/[locale]/` prefix and files in your default language exist at the root of `src/pages/`:

* src

  * pages

    * about.astro

    * index.astro

    * es

      * about.astro
      * index.astro

    * fr

      * about.astro
      * index.astro

- `src/pages/about.astro` will produce the route `example.com/about/`
- `src/pages/fr/about.astro` will produce the route `example.com/fr/about/`

#### `prefixDefaultLocale: true`

[Section titled “prefixDefaultLocale: true”](#prefixdefaultlocale-true)

astro.config.mjs

```diff
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
    locales: ["es", "en", "fr"],
    defaultLocale: "en",
    routing: {
+        prefixDefaultLocale: true
    }
  }
})
```

Set this option when all routes will have their `/locale/` prefix in their URL and when all page content files, including those for your `defaultLocale`, exist in a localized folder:

* src

  * pages

    * **index.astro** // Note: this file is always required

    * en

      * index.astro
      * about.astro

    * es

      * about.astro
      * index.astro

    * pt-br

      * about.astro
      * index.astro

- URLs without a locale prefix, (e.g. `example.com/about/`) will return a 404 (not found) status code unless you specify a [fallback strategy](#fallback).

### `redirectToDefaultLocale`

[Section titled “redirectToDefaultLocale”](#redirecttodefaultlocale)

**Added in:** `astro@4.2.0`

Configures whether or not the home URL (`/`) generated by `src/pages/index.astro` will redirect to `/<defaultLocale>`.

Setting `prefixDefaultLocale: true` will also automatically set `redirectToDefaultLocale: true` in your `routing` config object. By default, the required `src/pages/index.astro` file will automatically redirect to the index page of your default locale.

You can opt out of this behavior by [setting `redirectToDefaultLocale: false`](/en/reference/configuration-reference/#i18nroutingredirecttodefaultlocale). This allows you to have a site home page that exists outside of your configured locale folder structure.

### `manual`

[Section titled “manual”](#manual)

**Added in:** `astro@4.6.0`

When this option is enabled, Astro will **disable** its i18n middleware so that you can implement your own custom logic. No other `routing` options (e.g. `prefixDefaultLocale`) may be configured with `routing: "manual"`.

You will be responsible for writing your own routing logic, or [executing Astro’s i18n middleware manually](#middleware-function) alongside your own.

astro.config.mjs

```js
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
    locales: ["es", "en", "fr"],
    defaultLocale: "en",
    routing: "manual"
  }
})
```

Astro provides helper functions for your middleware so you can control your own default routing, exceptions, fallback behavior, error catching, etc: [`redirectToDefaultLocale()`](/en/reference/modules/astro-i18n/#redirecttodefaultlocale), [`notFound()`](/en/reference/modules/astro-i18n/#notfound), and [`redirectToFallback()`](/en/reference/modules/astro-i18n/#redirecttofallback):

src/middleware.js

```js
import { defineMiddleware } from "astro:middleware";
import { redirectToDefaultLocale } from "astro:i18n"; // function available with `manual` routing
export const onRequest = defineMiddleware(async (ctx, next) => {
  if (ctx.url.startsWith("/about")) {
    return next();
  } else {
    return redirectToDefaultLocale(302);
  }
})
```

#### middleware function

[Section titled “middleware function”](#middleware-function)

The [`middleware`](#middleware-function) function manually creates Astro’s i18n middleware. This allows you to extend Astro’s i18n routing instead of completely replacing it.

You can run `middleware` with [routing options](#routing) in combination with your own middleware, using the [`sequence`](/en/reference/modules/astro-middleware/#sequence) utility to determine the order:

src/middleware.js

```js
import {defineMiddleware, sequence} from "astro:middleware";
import { middleware } from "astro:i18n"; // Astro's own i18n routing config


export const userMiddleware = defineMiddleware(async (ctx, next) => {
  // this response might come from Astro's i18n middleware, and it might return a 404
  const response = await next();
  // the /about page is an exception and we want to render it
  if (ctx.url.startsWith("/about")) {
    return new Response("About page", {
      status: 200
    });
  } else {
    return response;
  }
});




export const onRequest = sequence(
  userMiddleware,
  middleware({
    redirectToDefaultLocale: false,
    prefixDefaultLocale: true
  })
)
```

## `domains`

[Section titled “domains”](#domains)

**Added in:** `astro@4.9.0`

This routing option allows you to customize your domains on a per-language basis for `server` rendered projects using the [`@astrojs/node`](/en/guides/integrations-guide/node/) or [`@astrojs/vercel`](/en/guides/integrations-guide/vercel/) adapter with a `site` configured.

Add `i18n.domains` to map any of your supported `locales` to custom URLs:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"
export default defineConfig({
  site: "https://example.com",
  output: "server", // required, with no prerendered pages
  adapter: node({
    mode: 'standalone',
  }),
  i18n: {
    locales: ["es", "en", "fr", "ja"],
    defaultLocale: "en",
    routing: {
      prefixDefaultLocale: false
    },
+    domains: {
+      fr: "https://fr.example.com",
+      es: "https://example.es"
+    }
  }
})
```

All non-mapped `locales` will follow your `prefixDefaultLocales` configuration. However, even if this value is `false`, page files for your `defaultLocale` must also exist within a localized folder. For the configuration above, an `/en/` folder is required.

With the above configuration:

* The file `/fr/about.astro` will create the URL `https://fr.example.com/about`.
* The file `/es/about.astro` will create the URL `https://example.es/about`.
* The file `/ja/about.astro` will create the URL `https://example.com/ja/about`.
* The file `/en/about.astro` will create the URL `https://example.com/about`.

The above URLs will also be returned by the `getAbsoluteLocaleUrl()` and `getAbsoluteLocaleUrlList()` functions.

## Fallback

[Section titled “Fallback”](#fallback)

When a page in one language doesn’t exist (e.g. a page that is not yet translated), instead of displaying a 404 page, you can choose to display fallback content from another `locale` on a per-language basis. This is useful when you do not yet have a page for every route, but you want to still provide some content to your visitors.

Your fallback strategy consists of two parts: choosing which languages should fallback to which other languages ([`i18n.fallback`](/en/reference/configuration-reference/#i18nfallback)) and choosing whether to perform a [redirect](/en/guides/routing/#redirects) or a [rewrite](/en/guides/routing/#rewrites) to show the fallback content ([`i18n.routing.fallbackType`](/en/reference/configuration-reference/#i18nroutingfallbacktype) added in Astro v4.15.0).

For example, when you configure `i18n.fallback: { fr: "es" }`, Astro will ensure that a page is built in `src/pages/fr/` for every page that exists in `src/pages/es/`.

If any page does not already exist, then a page will be created depending on your `fallbackType`:

* With a redirect to the corresponding `es` route (default behavior).
* With the content of the `/es/` page (`i18n.routing.fallbackType: "rewrite"`).

For example, the configuration below sets `es` as the fallback locale for any missing `fr` routes. This means that a user visiting `example.com/fr/my-page/` will be shown the content for `example.com/es/my-page/` (without being redirected) instead of being taken to a 404 page when `src/pages/fr/my-page.astro` does not exist.

astro.config.mjs

```diff
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
    locales: ["es", "en", "fr"],
    defaultLocale: "en",
+    fallback: {
+      fr: "es"
+    },
    routing: {
+      fallbackType: "rewrite"
    }
  }
})
```

## Custom locale paths

[Section titled “Custom locale paths”](#custom-locale-paths)

In addition to defining your site’s supported `locales` as strings (e.g. “en”, “pt-br”), Astro also allows you to map an arbitrary number of [browser-recognized language `codes`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language#syntax) to a custom URL `path`. While locales can be strings of any format as long as they correspond to your project folder structure, `codes` must follow the browser’s accepted syntax.

Pass an object to the `locales` array with a `path` key to define a custom URL prefix, and `codes` to indicate the languages mapped to this URL. In this case, your `/[locale]/` folder name must match exactly the value of the `path` and your URLs will be generated using the `path` value.

This is useful if you support multiple variations of a language (e.g. `"fr"`, `"fr-BR"`, and `"fr-CA"`) and you want to have all these variations mapped under the same URL `/fr/`, or even customize it entirely (e.g. `/french/`):

astro.config.mjs

```diff
import { defineConfig } from "astro/config"
export default defineConfig({
  i18n: {
-    locales: ["es", "en", "fr"],
+    locales: ["es", "en", {
+      path: "french", // no slashes included
+      codes: ["fr", "fr-BR", "fr-CA"]
+    }],
    defaultLocale: "en",
    routing: {
        prefixDefaultLocale: true
    }
  }
})
```

When using functions from the [`astro:i18n` virtual module](/en/reference/modules/astro-i18n/) to compute valid URL paths based on your configuration (e.g. `getRelativeLocaleUrl()`), [use the `path` as the value for `locale`](/en/reference/modules/astro-i18n/#getlocalebypath).

#### Limitations

[Section titled “Limitations”](#limitations)

This feature has some restrictions:

* The `site` option is mandatory.
* The `output` option must be set to `"server"`.
* There cannot be any individual prerendered pages.

Astro relies on the following headers in order to support the feature:

* [`X-Forwarded-Host`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Host) and [`Host`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host). Astro will use the former, and if not present, will try the latter.
* [`X-Forwarded-Proto`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-Proto) and [`URL#protocol`](https://developer.mozilla.org/en-US/docs/Web/API/URL/protocol) of the server request.

Make sure that your server proxy/hosting platform is able to provide this information. Failing to retrieve these headers will result in a 404 (status code) page.

## Browser language detection

[Section titled “Browser language detection”](#browser-language-detection)

Astro’s i18n routing allows you to access two properties for browser language detection in pages rendered on demand: `Astro.preferredLocale` and `Astro.preferredLocaleList`. All pages, including static prerendered pages, have access to `Astro.currentLocale`.

These combine the browser’s `Accept-Language` header, and your `locales` (strings or `codes`) to automatically respect your visitor’s preferred languages.

* [`Astro.preferredLocale`](/en/reference/api-reference/#preferredlocale): Astro can compute a **preferred locale** for your visitor if their browser’s preferred locale is included in your `locales` array. This value is undefined if no such match exists.

* [`Astro.preferredLocaleList`](/en/reference/api-reference/#preferredlocalelist): An array of all locales that are both requested by the browser and supported by your website. This produces a list of all compatible languages between your site and your visitor. The value is `[]` if none of the browser’s requested languages are found in your `locales` array. If the browser does not specify any preferred languages, then this value will be [`i18n.locales`](/en/reference/configuration-reference/#i18nlocales).

* [`Astro.currentLocale`](/en/reference/api-reference/#currentlocale): The locale computed from the current URL, using the syntax specified in your `locales` configuration. If the URL does not contain a `/[locale]/` prefix, then the value will default to [`i18n.defaultLocale`](/en/reference/configuration-reference/#i18ndefaultlocale).

In order to successfully match your visitors’ preferences, provide your `codes` using the same pattern [used by the browser](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language#syntax).

# Markdown in Astro

> Learn about Astro's built-in support for Markdown.

[Markdown](https://daringfireball.net/projects/markdown/) is commonly used to author text-heavy content like blog posts and documentation. Astro includes built-in support for Markdown files that can also include [frontmatter YAML](https://dev.to/paulasantamaria/introduction-to-yaml-125f) (or [TOML](https://toml.io)) to define custom properties such as a title, description, and tags.

In Astro, you can author content in [GitHub Flavored Markdown](https://github.github.com/gfm/), then render it in `.astro` components. This combines a familiar writing format designed for content with the flexibility of Astro’s component syntax and architecture.

Tip

For additional functionality, such as including components and JSX expressions in Markdown, add the [`@astrojs/mdx` integration](/en/guides/integrations-guide/mdx/) to write your Markdown content using [MDX](https://mdxjs.com/).

## Organizing Markdown files

[Section titled “Organizing Markdown files”](#organizing-markdown-files)

Your local Markdown files can be kept anywhere within your `src/` directory. Markdown files located within `src/pages/` will automatically generate [Markdown pages on your site](#individual-markdown-pages).

Your Markdown content and frontmatter properties are available to use in components through [local file imports](#importing-markdown) or when [queried and rendered from data fetched by a content collections helper function](#markdown-from-content-collections-queries).

### File imports vs content collections queries

[Section titled “File imports vs content collections queries”](#file-imports-vs-content-collections-queries)

Local Markdown can be imported into `.astro` components using an `import` statement for a single file and [Vite’s `import.meta.glob()`](/en/guides/imports/#importmetaglob) to query multiple files at once. The [exported data from these Markdown files](#importing-markdown) can then be used in the `.astro` component.

If you have groups of related Markdown files, consider [defining them as collections](/en/guides/content-collections/). This gives you several advantages, including the ability to store Markdown files anywhere on your filesystem or remotely.

Collections use content-specific, optimized APIs for [querying and rendering your Markdown content](#markdown-from-content-collections-queries) instead of file imports. Collections are intended for sets of data that share the same structure, such as blog posts or product items. When you define that shape in a schema, you additionally get validation, type safety, and Intellisense in your editor.

See more about [when to use content collections](/en/guides/content-collections/#when-to-create-a-collection) instead of file imports.

## Dynamic JSX-like expressions

[Section titled “Dynamic JSX-like expressions”](#dynamic-jsx-like-expressions)

After importing or querying Markdown files, you can write dynamic HTML templates in your `.astro` components that include frontmatter data and body content.

src/pages/posts/great-post.md

```md
---
title: 'The greatest post of all time'
author: 'Ben'
---


Here is my _great_ post!
```

src/pages/my-posts.astro

```astro
---
import * as greatPost from './posts/great-post.md';
const posts = Object.values(import.meta.glob('./posts/*.md', { eager: true }));
---


<p>{greatPost.frontmatter.title}</p>
<p>Written by: {greatPost.frontmatter.author}</p>


<p>Post Archive:</p>
<ul>
  {posts.map(post => <li><a href={post.url}>{post.frontmatter.title}</a></li>)}
</ul>
```

### Available Properties

[Section titled “Available Properties”](#available-properties)

#### Markdown from content collections queries

[Section titled “Markdown from content collections queries”](#markdown-from-content-collections-queries)

When fetching data from your collections with the helper functions `getCollection()` or `getEntry()`, your Markdown’s frontmatter properties are available on a `data` object (e.g. `post.data.title`). Additionally, `body` contains the raw, uncompiled body content as a string.

The [`render()`](/en/reference/modules/astro-content/#render) function returns your Markdown body content, a generated list of headings, as well as a modified frontmatter object after any remark or rehype plugins have been applied.

Read more about [using content returned by a collections query](/en/guides/content-collections/#using-content-in-astro-templates).

#### Importing Markdown

[Section titled “Importing Markdown”](#importing-markdown)

The following exported properties are available in your `.astro` component when importing Markdown using `import` or `import.meta.glob()`:

* **`file`** - The absolute file path (e.g. `/home/user/projects/.../file.md`).
* **`url`** - The URL of the page (e.g. `/en/guides/markdown-content`).
* **`frontmatter`** - Contains any data specified in the file’s YAML (or TOML) frontmatter.
* **`<Content />`** - A component that returns the full, rendered contents of the file.
* **`rawContent()`** - A function that returns the raw Markdown document as a string.
* **`compiledContent()`** - An async function that returns the Markdown document compiled to an HTML string.
* **`getHeadings()`** - An async function that returns an array of all headings (`<h1>` to `<h6>`) in the file with the type: `{ depth: number; slug: string; text: string }[]`. Each heading’s `slug` corresponds to the generated ID for a given heading and can be used for anchor links.

An example Markdown blog post may pass the following `Astro.props` object:

```js
Astro.props = {
  file: "/home/user/projects/.../file.md",
  url: "/en/guides/markdown-content/",
  frontmatter: {
    /** Frontmatter from a blog post */
    title: "Astro 0.18 Release",
    date: "Tuesday, July 27 2021",
    author: "Matthew Phillips",
    description: "Astro 0.18 is our biggest release since Astro launch.",
  },
  getHeadings: () => [
    {"depth": 1, "text": "Astro 0.18 Release", "slug": "astro-018-release"},
    {"depth": 2, "text": "Responsive partial hydration", "slug": "responsive-partial-hydration"}
    /* ... */
  ],
  rawContent: () => "# Astro 0.18 Release\nA little over a month ago, the first public beta [...]",
  compiledContent: () => "<h1>Astro 0.18 Release</h1>\n<p>A little over a month ago, the first public beta [...]</p>",
}
```

## The `<Content />` Component

[Section titled “The \<Content /> Component”](#the-content--component)

The `<Content />` component is available by importing `Content` from a Markdown file. This component returns the file’s full body content, rendered to HTML. You can optionally rename `Content` to any component name you prefer.

You can similarly [render the HTML content of a Markdown collection entry](/en/guides/content-collections/#rendering-body-content) by rendering a `<Content />` component.

src/pages/content.astro

```astro
---
// Import statement
import {Content as PromoBanner} from '../components/promoBanner.md';


// Collections query
import { getEntry, render } from 'astro:content';


const product = await getEntry('products', 'shirt');
const { Content } = await render(product);
---
<h2>Today's promo</h2>
<PromoBanner />


<p>Sale Ends: {product.data.saleEndDate.toDateString()}</p>
<Content />
```

## Heading IDs

[Section titled “Heading IDs”](#heading-ids)

Writing headings in Markdown will automatically give you anchor links so you can link directly to certain sections of your page.

src/pages/page-1.md

```markdown
---
title: My page of content
---
## Introduction


I can link internally to [my conclusion](#conclusion) on the same page when writing Markdown.


## Conclusion


I can visit `https://example.com/page-1/#introduction` in a browser to navigate directly to my Introduction.
```

Astro generates heading `id`s based on `github-slugger`. You can find more examples in [the github-slugger documentation](https://github.com/Flet/github-slugger#usage).

### Heading IDs and plugins

[Section titled “Heading IDs and plugins”](#heading-ids-and-plugins)

Astro injects an `id` attribute into all heading elements (`<h1>` to `<h6>`) in Markdown and MDX files. You can retrieve this data from the `getHeadings()` utility available as a [Markdown exported property](#available-properties) from an imported file, or from the `render()` function when [using Markdown returned from a content collections query](#markdown-from-content-collections-queries).

You can customize these heading IDs by adding a rehype plugin that injects `id` attributes (e.g. `rehype-slug`). Your custom IDs, instead of Astro’s defaults, will be reflected in the HTML output and the items returned by `getHeadings()`.

By default, Astro injects `id` attributes after your rehype plugins have run. If one of your custom rehype plugins needs to access the IDs injected by Astro, you can import and use Astro’s `rehypeHeadingIds` plugin directly. Be sure to add `rehypeHeadingIds` before any plugins that rely on it:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import { rehypeHeadingIds } from '@astrojs/markdown-remark';
import { otherPluginThatReliesOnHeadingIDs } from 'some/plugin/source';


export default defineConfig({
  markdown: {
    rehypePlugins: [
+      rehypeHeadingIds,
      otherPluginThatReliesOnHeadingIDs,
    ],
  },
});
```

## Markdown Plugins

[Section titled “Markdown Plugins”](#markdown-plugins)

Markdown support in Astro is powered by [remark](https://remark.js.org/), a powerful parsing and processing tool with an active ecosystem. Other Markdown parsers like Pandoc and markdown-it are not currently supported.

Astro applies the [GitHub-flavored Markdown](https://github.com/remarkjs/remark-gfm) and [SmartyPants](https://github.com/silvenon/remark-smartypants) plugins by default. This brings some niceties like generating clickable links from text, and formatting for [quotations and em-dashes](https://daringfireball.net/projects/smartypants/).

You can customize how remark parses your Markdown in `astro.config.mjs`. See the full list of [Markdown configuration options](/en/reference/configuration-reference/#markdown-options).

### Adding remark and rehype plugins

[Section titled “Adding remark and rehype plugins”](#adding-remark-and-rehype-plugins)

Astro supports adding third-party [remark](https://github.com/remarkjs/remark) and [rehype](https://github.com/rehypejs/rehype) plugins for Markdown. These plugins allow you to extend your Markdown with new capabilities, like [auto-generating a table of contents](https://github.com/remarkjs/remark-toc), [applying accessible emoji labels](https://github.com/florianeckerstorfer/remark-a11y-emoji), and [styling your Markdown](/en/guides/styling/#markdown-styling).

We encourage you to browse [awesome-remark](https://github.com/remarkjs/awesome-remark) and [awesome-rehype](https://github.com/rehypejs/awesome-rehype) for popular plugins! See each plugin’s own README for specific installation instructions.

This example applies [`remark-toc`](https://github.com/remarkjs/remark-toc) and [`rehype-accessible-emojis`](https://www.npmjs.com/package/rehype-accessible-emojis) to Markdown files:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import remarkToc from 'remark-toc';
import { rehypeAccessibleEmojis } from 'rehype-accessible-emojis';


export default defineConfig({
  markdown: {
    remarkPlugins: [ [remarkToc, { heading: 'toc', maxDepth: 3 } ] ],
    rehypePlugins: [rehypeAccessibleEmojis],
  },
});
```

### Customizing a plugin

[Section titled “Customizing a plugin”](#customizing-a-plugin)

In order to customize a plugin, provide an options object after it in a nested array.

The example below adds the [heading option to the `remarkToc` plugin](https://github.com/remarkjs/remark-toc#options) to change where the table of contents is placed, and the [`behavior` option to the `rehype-autolink-headings` plugin](https://github.com/rehypejs/rehype-autolink-headings#options) in order to add the anchor tag after the headline text.

astro.config.mjs

```js
import remarkToc from 'remark-toc';
import rehypeSlug from 'rehype-slug';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';


export default {
  markdown: {
    remarkPlugins: [ [remarkToc, { heading: "contents"} ] ],
    rehypePlugins: [rehypeSlug, [rehypeAutolinkHeadings, { behavior: 'append' }]],
  },
}
```

### Modifying frontmatter programmatically

[Section titled “Modifying frontmatter programmatically”](#modifying-frontmatter-programmatically)

You can add frontmatter properties to all of your Markdown and MDX files by using a [remark or rehype plugin](#markdown-plugins).

1. Append a `customProperty` to the `data.astro.frontmatter` property from your plugin’s `file` argument:

   example-remark-plugin.mjs

   ```js
   export function exampleRemarkPlugin() {
     // All remark and rehype plugins return a separate function
     return function (tree, file) {
       file.data.astro.frontmatter.customProperty = 'Generated property';
     }
   }
   ```

   Tip

   **Added in:** `astro@2.0.0`

   `data.astro.frontmatter` contains all properties from a given Markdown or MDX document. This allows you to modify existing frontmatter properties, or compute new properties from this existing frontmatter.

2. Apply this plugin to your `markdown` or `mdx` integration config:

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { exampleRemarkPlugin } from './example-remark-plugin.mjs';


   export default defineConfig({
     markdown: {
       remarkPlugins: [exampleRemarkPlugin]
     },
   });
   ```

   or

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { exampleRemarkPlugin } from './example-remark-plugin.mjs';


   export default defineConfig({
     integrations: [
       mdx({
         remarkPlugins: [exampleRemarkPlugin],
       }),
     ],
   });
   ```

Now, every Markdown or MDX file will have `customProperty` in its frontmatter, making it available when [importing your markdown](#importing-markdown) and from [the `Astro.props.frontmatter` property in your layouts](#frontmatter-layout-property).

![](/houston_chef.webp) **Related recipe:** [Add reading time](/en/recipes/reading-time/)

### Extending Markdown config from MDX

[Section titled “Extending Markdown config from MDX”](#extending-markdown-config-from-mdx)

Astro’s MDX integration will extend [your project’s existing Markdown configuration](/en/reference/configuration-reference/#markdown-options) by default. To override individual options, you can specify their equivalent in your MDX configuration.

The following example disables GitHub-Flavored Markdown and applies a different set of remark plugins for MDX files:

astro.config.mjs

```ts
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  markdown: {
    syntaxHighlight: 'prism',
    remarkPlugins: [remarkPlugin1],
    gfm: true,
  },
  integrations: [
    mdx({
      // `syntaxHighlight` inherited from Markdown


      // Markdown `remarkPlugins` ignored,
      // only `remarkPlugin2` applied.
      remarkPlugins: [remarkPlugin2],
      // `gfm` overridden to `false`
      gfm: false,
    })
  ]
});
```

To avoid extending your Markdown config from MDX, set [the `extendMarkdownConfig` option](/en/guides/integrations-guide/mdx/#extendmarkdownconfig) (enabled by default) to `false`:

astro.config.mjs

```ts
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  markdown: {
    remarkPlugins: [remarkPlugin],
  },
  integrations: [
    mdx({
      // Markdown config now ignored
      extendMarkdownConfig: false,
      // No `remarkPlugins` applied
    })
  ]
});
```

## Individual Markdown pages

[Section titled “Individual Markdown pages”](#individual-markdown-pages)

Tip

[Content collections](/en/guides/content-collections/) and [importing Markdown into `.astro` components](#dynamic-jsx-like-expressions) provide more features for rendering your Markdown and are the recommended way to handle most of your content. However, there may be times when you want the convenience of just adding a file to `src/pages/` and having a simple page automatically created for you.

Astro treats [any supported file inside of the `/src/pages/` directory](/en/basics/astro-pages/#supported-page-files) as a page, including `.md` and other Markdown file types.

Placing a file in this directory, or any sub-directory, will automatically build a page route using the pathname of the file and display the Markdown content rendered to HTML. Astro will automatically add a `<meta charset="utf-8">` tag to your page to allow easier authoring of non-ASCII content.

src/pages/page-1.md

```markdown
---
title: Hello, World
---


# Hi there!


This Markdown file creates a page at `your-domain.com/page-1/`


It probably isn't styled much, but Markdown does support:
- **bold** and _italics._
- lists
- [links](https://astro.build)
- <p>HTML elements</p>
- and more!
```

### Frontmatter `layout` property

[Section titled “Frontmatter layout property”](#frontmatter-layout-property)

To help with the limited functionality of individual Markdown pages, Astro provides a special frontmatter `layout` property which is a relative path to an Astro [Markdown layout component](/en/basics/layouts/#markdown-layouts). `layout` is not a special property when using [content collections](/en/guides/content-collections/) to query and render your Markdown content, and is not guaranteed to be supported outside of its intended use case.

If your Markdown file is located within `src/pages/`, create a layout component and add it in this layout property to provide a page shell around your Markdown content.

src/pages/posts/post-1.md

```markdown
---
layout: ../../layouts/BlogPostLayout.astro
title: Astro in brief
author: Himanshu
description: Find out what makes Astro awesome!
---
This is a post written in Markdown.
```

This layout component is a regular Astro component with [specific properties automatically available](/en/basics/layouts/#markdown-layout-props) through `Astro.props` for your Astro template. For example, you can access your Markdown file’s frontmatter properties through `Astro.props.frontmatter`:

src/layouts/BlogPostLayout.astro

```astro
---
const {frontmatter} = Astro.props;
---
<html>
  <head>
    <!-- ... -->
    <meta charset="utf-8"> // no longer added by default
  </head>
  <!-- ... -->
  <h1>{frontmatter.title}</h1>
  <h2>Post author: {frontmatter.author}</h2>
  <p>{frontmatter.description}</p>
  <slot /> <!-- Markdown content is injected here -->
  <!-- ... -->
</html>
```

When using the frontmatter `layout` property, you must include the `<meta charset="utf-8">` tag in your layout as Astro will no longer add it automatically. You can now also [style your Markdown](/en/guides/styling/#markdown-styling) in your layout component.

Learn more about [Markdown Layouts](/en/basics/layouts/#markdown-layouts).

## Fetching Remote Markdown

[Section titled “Fetching Remote Markdown”](#fetching-remote-markdown)

Astro’s internal Markdown processor is not available for processing remote Markdown.

To fetch remote Markdown for use in [content collections](/en/guides/content-collections/), you can [build a custom loader](/en/guides/content-collections/#building-a-custom-loader) with access to a [`renderMarkdown()` function](/en/reference/content-loader-reference/#rendermarkdown).

To fetch remote Markdown directly and render it to HTML, you will need to install and configure your own Markdown parser from NPM. This will not inherit from any of Astro’s built-in Markdown settings that you have configured.

Be sure that you understand these limitations before implementing this in your project, and consider fetching your remote Markdown using a content collections loader instead.

src/pages/remote-example.astro

```astro
---
// Example: Fetch Markdown from a remote API
// and render it to HTML, at runtime.
// Using "marked" (https://github.com/markedjs/marked)
import { marked } from 'marked';
const response = await fetch('https://raw.githubusercontent.com/wiki/adam-p/markdown-here/Markdown-Cheatsheet.md');
const markdown = await response.text();
const content = marked.parse(markdown);
---
<article set:html={content} />
```

# Image and video hosting with Astro

> How to use a hosted media service to add images and videos to Astro

Follow one of our guides to integrate images and videos from a hosted media service.

## Hosted Media Guides

[Section titled “Hosted Media Guides”](#hosted-media-guides)

* ![](/logos/cloudinary.svg)

  ### [Cloudinary](/en/guides/media/cloudinary/)

* ![](/logos/mux.svg)

  ### [Mux](/en/guides/media/mux/)

## Why use hosted media?

[Section titled “Why use hosted media?”](#why-use-hosted-media)

Hosted media helps individuals, teams, and organizations store, manage, optimize, and deliver their image and video assets with dedicated APIs from a central location.

This centralization can be useful, particularly when using a single source of truth for your assets between multiple web or mobile properties. This is important if you’re part of an organization that requires multiple teams to use the same assets, or are integrating into other content systems like a PIM (Product Information Manager) to connect your assets to products.

Image hosting services can transform and optimize your images, automatically delivering optimized versions for your visitors. These [remote images](/en/guides/images/#remote-images) can be used in Astro’s built-in `<Image />` and `<Picture />` components, and are available to all file types in your project, including Markdown, MDX, and UI Framework components.

Video hosting services like [Mux](/en/guides/media/mux/) can provide performant on-demand and live-streaming video delivery along with customizable video players, giving significant reliability and scaling benefits over handling local content. They will handle video transcoding, compression, and transformation to provide a smooth user experience. A platform like Mux may also include data analysis to help you understand your user engagement.

## Which hosted media systems work well with Astro?

[Section titled “Which hosted media systems work well with Astro?”](#which-hosted-media-systems-work-well-with-astro)

Much like when using a CMS, you’ll want to use hosted services that allow you to fetch and interact with your assets via an API or SDK. Some services may additionally include Astro-native components for displaying your images or videos.

## Can I use Astro without a hosted media system?

[Section titled “Can I use Astro without a hosted media system?”](#can-i-use-astro-without-a-hosted-media-system)

Yes! Astro provides built-in ways to [store images](/en/guides/images/#where-to-store-images), including support for referencing remote images.

However, there is no native video support in Astro, and we recommend choosing a service like [Mux](/en/guides/media/mux/) to handle the demands of optimizing and streaming video content.

# Cloudinary & Astro

> Add images and videos to your Astro project using Cloudinary

[Cloudinary](https://cloudinary.com) is an image and video platform and headless Digital Asset Manager (DAM) that lets you host assets and deliver them from their content delivery network (CDN).

When delivering from Cloudinary, you additionally get access to their Transformation API, giving you the ability to edit your assets with tools like background removal, dynamic cropping and resizing, and generative AI.

## Using Cloudinary in Astro

[Section titled “Using Cloudinary in Astro”](#using-cloudinary-in-astro)

Cloudinary supports a wide variety of SDKs that can be used depending on your Astro environment.

The [Cloudinary Astro SDK](https://astro.cloudinary.dev/) provides native Astro components, including image, video, and upload components, as well as a content loader that can be used with Astro content collections.

Alternatively, both the Cloudinary [Node.js SDK](https://cloudinary.com/documentation/node_integration) and [JavaScript SDK](https://cloudinary.com/documentation/javascript_integration) can be used to generate URLs for your images. The Node.js SDK can additionally make requests to the Cloudinary API including uploading assets, requesting resources, and running content analysis.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An existing Astro project
* A Cloudinary account

## Installing Astro Cloudinary

[Section titled “Installing Astro Cloudinary”](#installing-astro-cloudinary)

Install the Cloudinary Astro SDK by running the appropriate command for your package manager:

* npm

  ```shell
  npm install astro-cloudinary
  ```

* pnpm

  ```shell
  pnpm add astro-cloudinary
  ```

* Yarn

  ```shell
  yarn add astro-cloudinary
  ```

## Configuring your account

[Section titled “Configuring your account”](#configuring-your-account)

Create a new `.env` file in the root of your project and add your Cloudinary credentials:

.env

```shell
PUBLIC_CLOUDINARY_CLOUD_NAME="<Your Cloud Name>"


// Only needed if using CldUploadWidget or cldAssetsLoader
PUBLIC_CLOUDINARY_API_KEY="<Your API Key>"
CLOUDINARY_API_SECRET="<Your API Secret>"
```

## Using Cloudinary images

[Section titled “Using Cloudinary images”](#using-cloudinary-images)

Add images in `.astro` components by passing image data (e.g. `src`, `width`, `alt`) to the `<CldImage>` component. This will automatically optimize your image and give you access to the Transformations API.

Component.astro

```jsx
---
import { CldImage } from 'astro-cloudinary';
---
<CldImage
  src="<Public ID>"
  width="<Width>"
  height="<Height>"
  alt="<Description>"
/>
```

See [Cloudinary’s `<CldImage>` documentation](https://astro.cloudinary.dev/cldimage/basic-usage) for more information.

## Using Cloudinary videos

[Section titled “Using Cloudinary videos”](#using-cloudinary-videos)

To add video to your `.astro` components, add the `<CldVideoPlayer>` and pass the appropriate properties. This component will automatically optimize and embed your video using the [Cloudinary Video Player](https://cloudinary.com/documentation/cloudinary_video_player).

Component.astro

```jsx
---
import { CldVideoPlayer } from 'astro-cloudinary';
---
<CldVideoPlayer
  src="<Public ID>"
  width="<Width>"
  height="<Height>"
/>
```

See [Cloudinary’s `<CldVideoPlayer>` documentation](https://astro.cloudinary.dev/cldvideoplayer/basic-usage) for more information.

## Enabling Cloudinary uploads

[Section titled “Enabling Cloudinary uploads”](#enabling-cloudinary-uploads)

To enable file uploading in your website or app’s UI, add the `<CldUploadWidget>` which will embed the [Cloudinary Upload Widget](https://cloudinary.com/documentation/upload_widget).

The following example creates a widget to allow unsigned uploads by passing an unsigned [Upload Preset](https://cloudinary.com/documentation/upload_presets):

Component.astro

```jsx
---
import { CldUploadWidget } from 'astro-cloudinary';
---
<CldUploadWidget uploadPreset="<Upload Preset>">
  <button>Upload</button>
</CldUploadWidget>
```

For signed uploads, you can find [a guide and example](https://astro.cloudinary.dev/clduploadwidget/signed-uploads) on the Astro Cloudinary docs.

See [Cloudinary’s `<CldUploadWidget>` documentation](https://astro.cloudinary.dev/clduploadwidget/basic-usage) for more information.

## Cloudinary content loader

[Section titled “Cloudinary content loader”](#cloudinary-content-loader)

The Cloudinary Astro SDK provides the `cldAssetsLoader` content loader to load Cloudinary assets for content collections.

To load a collection of images or videos, set `loader: cldAssetsLoader ({})` with a `folder`, if required:

config.ts

```jsx
import { defineCollection } from 'astro:content';
import { cldAssetsLoader } from 'astro-cloudinary/loaders';


export const collections = {
  assets: defineCollection({
    loader: cldAssetsLoader({
      folder: '<Folder>' // Optional, without loads root directory
    })
  }),
}
```

You can then use the [`getCollection()` or `getEntry()` query functions](/en/guides/content-collections/#querying-collections) to select one or many images or videos from your collection.

See [Cloudinary’s `cldAssetsLoader` documentation](https://astro.cloudinary.dev/cldassetsloader/basic-usage) for more information.

## Generating Cloudinary image URLs

[Section titled “Generating Cloudinary image URLs”](#generating-cloudinary-image-urls)

The Astro Cloudinary SDK provides a `getCldOgImageUrl()` helper for generating and using URLs for your images. Use this when you need a URL instead of a component to display your image.

One common use for a URL is for an Open Graph image in `<meta>` tags for social media cards. This helper, like the components, provides you access to Cloudinary transformations to create dynamic, unique social cards for any of your pages.

The following example shows the necessary `<meta>` tags for a social media card, using `getCldOgImageUrl()` to generate an Open Graph image:

Layout.astro

```jsx
---
import { getCldOgImageUrl } from 'astro-cloudinary/helpers';
const ogImageUrl = getCldOgImageUrl({ src: '<Public ID>' });
---
<meta property="og:image" content={ogImageUrl} />
<meta property="og:image:secure_url" content={ogImageUrl} />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="twitter:title" content="<Twitter Title>" />
<meta property="twitter:card" content="summary_large_image" />
<meta property="twitter:image" content={ogImageUrl} />
```

Find [Cloudinary Social Media Card templates](https://astro.cloudinary.dev/templates/social-media-cards) on the Cloudinary docs.

See [Cloudinary’s `getCldOgImageUrl()` documentation](https://astro.cloudinary.dev/getcldogimageurl/basic-usage) for more information.

## Using Cloudinary in Node.js

[Section titled “Using Cloudinary in Node.js”](#using-cloudinary-in-nodejs)

For more complex asset management, uploading, or analysis, you can use the Cloudinary Node.js SDK when working in an Astro Node.js environment.

Install the Cloudinary Node.js SDK by running the appropriate command for your package manager:

* npm

  ```shell
  npm install cloudinary
  ```

* pnpm

  ```shell
  pnpm add cloudinary
  ```

* Yarn

  ```shell
  yarn add cloudinary
  ```

Add the following environment variables in your `.env` file:

.env

```shell
PUBLIC_CLOUDINARY_CLOUD_NAME="<Your Cloud Name>"
PUBLIC_CLOUDINARY_API_KEY="<Your API Key>"
CLOUDINARY_API_SECRET="<Your API Secret>"
```

Configure your account with a new Cloudinary instance by adding the following code between the fences of your Astro component:

Component.astro

```js
---
import { v2 as cloudinary } from "cloudinary";


cloudinary.config({
  cloud_name: import.meta.env.PUBLIC_CLOUDINARY_CLOUD_NAME,
  api_key: import.meta.env.PUBLIC_CLOUDINARY_API_KEY,
  api_secret: import.meta.env.CLOUDINARY_API_SECRET,
});
---
```

This will give you access to all of the Cloudinary APIs to allow you to interact with your images, videos, and other supported files.

Component.astro

```js
await cloudinary.uploader.upload('./path/to/file');
```

Learn how to [upload files using the Cloudinary Node.js SDK with Astro Forms](https://www.youtube.com/watch?v=DQUYMyT2MTM).

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Cloudinary Astro SDK](https://astro.cloudinary.dev/)
* [Cloudinary Node.js SDK](https://cloudinary.com/documentation/node_integration)
* [Using Cloudinary with Astro (YouTube)](https://www.youtube.com/playlist?list=PL8dVGjLA2oMqnpf2tShn1exf5GkSWuu5-)
* [Code Examples Using Cloudinary Astro SDK (GitHub)](https://github.com/cloudinary-community/cloudinary-examples/tree/main/examples/astro-cloudinary)

# Mux & Astro

> Add high-performance video to your Astro project using Mux

[Mux](https://www.mux.com?utm_campaign=21819274-Astro\&utm_source=astro-docs) is a hosted media service that provides video streaming infrastructure and performance analytics for businesses of all scales.

When you use Mux to store and host your video content, you’ll have access to Astro-native video components for [Mux Player](#mux-player), a drop-in component for adding Mux videos in your Astro project, and [Mux Uploader](#mux-uploader) for uploading videos to Mux from your website. These components integrate seamlessly with [Mux Data](https://www.mux.com/docs/guides/data?utm_campaign=21819274-Astro\&utm_source=astro-docs) to track your video engagement and performance.

You can also interact with your content through the [Mux Node SDK](#mux-node-sdk).

Tip

Learn more about features such as embedding, storing, streaming, and customizing video at [Mux’s dedicated page for video in Astro](https://www.mux.com/video-for/astro?utm_campaign=21819274-Astro\&utm_source=astro-docs)!

## Using Mux in Astro

[Section titled “Using Mux in Astro”](#using-mux-in-astro)

Mux’s APIs and web components work in Astro to compress and optimize your videos and streams for the web, adapt the quality of your video to network conditions, and integrate additional features like captions, thumbnails, and analytics. The [Mux Node SDK](https://www.mux.com/docs/integrations/mux-node-sdk?utm_campaign=21819274-Astro\&utm_source=astro-docs) supports both Mux Data and the Mux Video API.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An existing Astro project. Some features may additionally require an adapter installed for [on-demand server rendering](/en/guides/on-demand-rendering/).
* A Mux account. If you don’t have an account, you can [sign up with Mux](https://dashboard.mux.com/login?utm_campaign=21819274-Astro\&utm_source=astro-docs) using the code `ASTRO` to receive a $50 credit.

## Mux Player

[Section titled “Mux Player”](#mux-player)

In Astro, you can use the full-featured [Mux Player](https://www.mux.com/docs/guides/mux-player-web?utm_campaign=21819274-Astro\&utm_source=astro-docs) as a native Astro component for optimized, responsive video playback and live streams.

Mux Player provides a responsive UI based on video player dimensions and stream type, automatic thumbnail previews and poster images, and modern video player capabilities (e.g. fullscreen, picture-in-picture, Chromecast, AirPlay).

src/components/MyMuxVideoPlayer.astro

```astro
---
import { MuxPlayer } from "@mux/mux-player-astro";
---
<MuxPlayer
  playbackId="DS00Spx1CV902MCtPj5WknGlR102V5HFkDe"
  metadata={{ video_title: 'My Astro Video' }}
/>
```

Mux Player has built-in support for Mux Data analytics, and will automatically show visitor engagement and video quality metrics in your dashboard once your video has views on your deployed site.

### Installation

[Section titled “Installation”](#installation)

Install the Astro version of Mux Player using your preferred package manager:

* npm

  ```shell
  npm install @mux/mux-player-astro
  ```

* pnpm

  ```shell
  pnpm add @mux/mux-player-astro
  ```

* Yarn

  ```shell
  yarn add @mux/mux-player-astro
  ```

Mux Player can also be used in your Astro project as:

* a web component (`<mux-player>` from `@mux/mux-player` )
* a React component (`<MuxPlayer />` from `@mux/mux-player-react`)
* an HTML web embed (`<iframe>`)

### Play a video from Mux

[Section titled “Play a video from Mux”](#play-a-video-from-mux)

Import and use the native `<MuxPlayer />` Astro component directly in your `.astro` files like any other Astro component.

You will need the `playbackId` for your asset, which can be found in your Mux dashboard or [retrieved from its `ASSET_ID`](#retrieve-asset-data).

All other [options to control the Mux web player](https://www.mux.com/docs/guides/player-api-reference/?utm_campaign=21819274-Astro\&utm_source=astro-docs) (e.g. hide or display controls, style elements, disable cookies) are optional:

src/components/StarlightVideo.astro

```astro
<MuxPlayer
  playbackId="FOTbeIxKeMPzyhrob722wytaTGI02Y3zbV00NeFQbTbK00"
  metadata={{
    video_title: 'Starlight by Astro',
  }}
  style={{
    display: 'block',
    aspectRatio: '16/9',
    backgroundColor: '#000',
    margin: '1rem 0 2rem',
  }}
  primaryColor="#f2ec3a"
  secondaryColor="#0caa09"
  accentColor="#6e1e99"
  defaultShowRemainingTime={true}
/>
```

If your `playbackId` belongs to a live stream instead of a prerecorded video on demand, then the Mux Player will allow you to further customize the player with options such as whether or not to enable [DVR mode](https://www.mux.com/docs/guides/stream-recordings-of-live-streams#dvr-mode-vs-non-dvr-mode?utm_campaign=21819274-Astro\&utm_source=astro-docs).

```astro
<MuxPlayer
  playbackId="FOTbeIxKeMPzyhrob722wytaTGI02Y3zbV00NeFQbTbK00"
  metadata={{
    video_title: 'Starlight stream with Astro',
  }}
  streamType="live:dvr"
/>
```

Every live stream is recorded and saved on Mux as a video asset for future on-demand playback.

## Mux video Element

[Section titled “Mux video Element”](#mux-video-element)

The [Mux video element](https://www.mux.com/docs/guides/play-your-videos#mux-video-element?utm_campaign=21819274-Astro\&utm_source=astro-docs) is a drop-in replacement for the HTML5 `<video>` element that provides browser support for HLS playback, and has Mux Data automatically configured to show visitor and performance metrics. Use this when you do not need or want all the features of [Mux Player](#mux-player).

To use the `<mux-video>` web component, first install `mux-video` using your preferred package manager:

* npm

  ```shell
  npm install @mux/mux-video
  ```

* pnpm

  ```shell
  pnpm add @mux/mux-video
  ```

* Yarn

  ```shell
  yarn add @mux/mux-video
  ```

Then, you can import and render the web component in a `<script>` tag in your `.astro` file.

You will need the `playback-id` for your video asset, which can be found in your Mux dashboard or [retrieved from its `ASSET_ID`](#retrieve-asset-data).

All attributes for the HTML 5 `<video>` element (e.g. `poster`, `controls`, `muted`) are available, as well as additional Mux video player controls (e.g. to provide metadata, control the resolution, disable cookies):

src/components/StarlightVideo.astro

```astro
<script>import '@mux/mux-video'</script>


<mux-video
  playback-id="FOTbeIxKeMPzyhrob722wytaTGI02Y3zbV00NeFQbTbK00"
  metadata-video-title="Starlight by Astro"
  controls
  disable-tracking
></mux-video>
```

## Mux Node SDK

[Section titled “Mux Node SDK”](#mux-node-sdk)

The [Mux Node SDK](https://www.mux.com/docs/integrations/mux-node-sdk?utm_campaign=21819274-Astro\&utm_source=astro-docs) provides authenticated access to the Mux REST API from server-side TypeScript or JavaScript. This allows you to interact with your Mux assets and data in the component script of your `.astro` files.

While the Mux Player and Mux Video components do not require authentication and can play any publicly accessible video given its `playbackId`, connecting to your hosted Mux data via the Node SDK requires [a Mux API access token](#mux-environment-api-access).

### Installation

[Section titled “Installation”](#installation-1)

Install the Mux Node SDK using your preferred package manager:

* npm

  ```shell
  npm install @mux/mux-node
  ```

* pnpm

  ```shell
  pnpm add @mux/mux-node
  ```

* Yarn

  ```shell
  yarn add @mux/mux-node
  ```

### Mux Environment API access

[Section titled “Mux Environment API access”](#mux-environment-api-access)

API tokens are tied to a specific Mux Environment, which is essentially a container for your videos and related data. When you sign up for Mux, an Environment is created for you automatically. If you’ve created additional Environments, make sure you select the correct one before generating your tokens. From there, you can [get your ID and SECRET tokens](https://www.mux.com/docs/core/stream-video-files#1-get-an-api-access-token) and provide them to the Node SDK. These tokens can be passed into your Astro components as environment variables stored in a `.env` file.

This will allow you to create an instance of the Mux Node SDK for retrieving information about your videos, creating new assets, accessing metrics and real-time performance, and more:

src/components/StarlightVideo.astro

```astro
---
import Mux from "@mux/mux-node";


const mux = new Mux ({
  tokenId: import.meta.env.MUX_TOKEN_ID,
  tokenSecret: import.meta.env.MUX_TOKEN_SECRET,
})
---
```

Read more about using [environment variables](/en/guides/environment-variables/) in your Astro project, including creating a [type-safe schema](/en/guides/environment-variables/#type-safe-environment-variables) for your Mux credentials.

### Retrieve asset data

[Section titled “Retrieve asset data”](#retrieve-asset-data)

To fetch information about your video to use in your Astro project, provide the video’s `ASSET_ID` (available in the Mux dashboard) to the `retrieve()` helper function. This will allow you to pass values to both your Mux components and your HTML template, such as the video’s title or duration:

```astro
---
import Mux from "@mux/mux-node";
import { MuxPlayer } from "@mux/mux-player-astro";


const mux = new Mux({
  tokenId: import.meta.env.MUX_TOKEN_ID,
  tokenSecret: import.meta.env.MUX_TOKEN_SECRET,
})


const ASSET_ID = "E01irAaN8c6dk1010153uC2mzst7RVbAdJJWtHECAHFvDo";
const asset = await mux.video.assets.retrieve(ASSET_ID);


const playbackId = asset.playback_ids?.find((id)=> id.policy=== "public")?.id;
const videoTitle = asset?.meta?.title;
const createdAt = Number(asset?.created_at);
const duration = Number(asset?.duration)


const date = new Date(createdAt * 1000).toDateString()
const time = new Date(Math.round(duration) * 1000).toISOString().substring(14, 19)
---
<h1>My Video Page</h1>
<p>Title: {videoTitle}</p>
<p>Upload Date: {date}</p>
<p>Length: {time}</p>


<MuxPlayer
  playbackId={playbackId}
  metadata={{video_title: videoTitle}}
/>
```

See all asset properties in the [Mux Asset API documentation](https://www.mux.com/docs/api-reference/video/assets?utm_campaign=21819274-Astro\&utm_source=astro-docs).

## Mux Uploader

[Section titled “Mux Uploader”](#mux-uploader)

[Mux Uploader](https://www.mux.com/docs/guides/mux-uploader?utm_campaign=21819274-Astro\&utm_source=astro-docs) is a fully-functional, customizable video upload UI for your Astro website. The native Astro `<MuxUpload />` component allows you to build video upload functionality into your web app.

Mux Uploader supports both manual file selection and drag and drop for file uploads, optional pausing and resuming of uploads, and more.

### Installation

[Section titled “Installation”](#installation-2)

Install the Astro version of Mux Uploader using your preferred package manager:

* npm

  ```shell
  npm install @mux/mux-uploader-astro
  ```

* pnpm

  ```shell
  pnpm add @mux/mux-uploader-astro
  ```

* Yarn

  ```shell
  yarn add @mux/mux-uploader-astro
  ```

### Upload a video to Mux

[Section titled “Upload a video to Mux”](#upload-a-video-to-mux)

Before uploading a video, make sure you have your [Mux API access tokens](#mux-environment-api-access) configured. With those in place, you can use the `create()` function from the Mux Node SDK to start a new video upload:

```astro
---
import Layout from '../../layouts/Layout.astro';
import Mux from "@mux/mux-node";
import { MuxUploader } from "@mux/mux-uploader-astro";


const mux = new Mux({
  tokenId: import.meta.env.MUX_TOKEN_ID,
  tokenSecret: import.meta.env.MUX_TOKEN_SECRET
});


const upload = await mux.video.uploads.create({
  new_asset_settings: {
    playback_policy: ['public'],
    video_quality: 'basic'
  },
  cors_origin: '*',
});
---
<Layout title="Upload a video to Mux">
  <MuxUploader endpoint={upload.url} />
</Layout>
```

### Customize the uploader

[Section titled “Customize the uploader”](#customize-the-uploader)

You can customize the functionality and appearance of the `<MuxUploader />` with additional component attributes. In addition to styling your element, this allows you to control options such as the ability to pause a download or set a maximum file size.

```astro
---
import { MuxUploader } from '@mux/mux-uploader-astro';
---


<MuxUploader
  endpoint="https://my-authenticated-url/storage?your-url-params"
  pausable
  maxFileSize={1000000000}
  chunkSize={8192}
  style={{
    '--progress-bar-fill-color': '#7e22ce',
    '--button-background-color': '#f0f0f0',
  }}
/>
```

See the [Mux Uploader customization guide](https://www.mux.com/docs/guides/uploader-web-customize-look-and-feel?utm_campaign=21819274-Astro\&utm_source=astro-docs) for more options.

### Event handling for uploads

[Section titled “Event handling for uploads”](#event-handling-for-uploads)

Mux Uploader provides a feature-rich, dynamic UI that changes based on the current state of your media upload. The uploader’s behavior responds to both user-driven events (e.g. selecting a file, retrying after an error) and state-driven events (e.g. upload in-progress, upload successfully completed).

You can listen for these events and handle them in your Astro component with [client-side scripts](/en/guides/client-side-scripts/). A `MuxUploaderElement` type is also available.

```astro
---
import { MuxUploader } from '@mux/mux-uploader-astro';
---


<MuxUploader
  id="my-uploader"
  endpoint="https://my-authenticated-url/storage?your-url-params"
  pausable
/>


<script>
  import type { MuxUploaderElement } from '@mux/mux-uploader-astro';


  const uploader = document.getElementById('my-uploader') as MuxUploaderElement;


  uploader.addEventListener('uploadstart', (event) => {
    console.log('Upload started!', event.detail);
  });


  uploader.addEventListener('success', (event) => {
    console.log('Upload successful!', event.detail);
  });


  uploader.addEventListener('uploaderror', (event) => {
    console.error('Upload error!', event.detail);
  });


  uploader.addEventListener('progress', (event) => {
    console.log('Upload progress: ', event.detail);
  });
</script>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

For the full API and webhook reference, usage guides, and information about additional topics, such as integrating with a CMS, building custom video workflows, and more, please see:

* [The official Mux documentation for Astro](https://www.mux.com/docs/integrations/astro?utm_campaign=21819274-Astro\&utm_source=astro-docs)
* [`@mux/mux-player-astro` API reference](https://github.com/muxinc/elements/blob/main/packages/mux-player-astro/README.md)
* [`@mux/mux-uploader-astro` API reference](https://github.com/muxinc/elements/blob/main/packages/mux-uploader-astro/REFERENCE.md)
* [Building a video uploader with Mux and Astro (YouTube)](https://www.youtube.com/watch?v=aaL1k5FsWfE)
* [Astro uploader and player code example (GitHub)](https://github.com/muxinc/examples/tree/main/astro-uploader-and-player)

# Middleware

> Learn how to use middleware in Astro.

**Middleware** allows you to intercept requests and responses and inject behaviors dynamically every time a page or endpoint is about to be rendered. This rendering occurs at build time for all prerendered pages, but occurs when the route is requested for pages rendered on demand, making [additional SSR features like cookies and headers](/en/guides/on-demand-rendering/#on-demand-rendering-features) available.

Middleware also allows you to set and share request-specific information across endpoints and pages by mutating a `locals` object that is available in all Astro components and API endpoints. This object is available even when this middleware runs at build time.

## Basic Usage

[Section titled “Basic Usage”](#basic-usage)

1. Create `src/middleware.js|ts` (Alternatively, you can create `src/middleware/index.js|ts`.)

2. Inside this file, export an [`onRequest()`](/en/reference/modules/astro-middleware/#onrequest) function that can be passed a [`context` object](#the-context-object) and `next()` function. This must not be a default export.

   src/middleware.js

   ```js
   export function onRequest (context, next) {
       // intercept data from a request
       // optionally, modify the properties in `locals`
       context.locals.title = "New title";


       // return a Response or the result of calling `next()`
       return next();
   };
   ```

3. Inside any `.astro` file, access response data using `Astro.locals`.

   src/components/Component.astro

   ```astro
   ---
   const data = Astro.locals;
   ---
   <h1>{data.title}</h1>
   <p>This {data.property} is from middleware.</p>
   ```

### The `context` object

[Section titled “The context object”](#the-context-object)

The [`context`](/en/reference/api-reference/) object includes information to be made available to other middleware, API routes and `.astro` routes during the rendering process.

This is an optional argument passed to `onRequest()` that may contain the `locals` object as well as any additional properties to be shared during rendering. For example, the `context` object may include cookies used in authentication.

### Storing data in `context.locals`

[Section titled “Storing data in context.locals”](#storing-data-in-contextlocals)

`context.locals` is an object that can be manipulated inside the middleware.

This `locals` object is forwarded across the request handling process and is available as a property to [`APIContext`](/en/reference/api-reference/#locals) and [`AstroGlobal`](/en/reference/api-reference/#locals). This allows data to be shared between middlewares, API routes, and `.astro` pages. This is useful for storing request-specific data, such as user data, across the rendering step.

Integration properties

[Integrations](/en/guides/integrations-guide/) may set properties and provide functionality through the `locals` object. If you are using an integration, check its documentation to ensure you are not overriding any of its properties or doing unnecessary work.

You can store any type of data inside `locals`: strings, numbers, and even complex data types such as functions and maps.

src/middleware.js

```js
export function onRequest (context, next) {
    // intercept data from a request
    // optionally, modify the properties in `locals`
    context.locals.user.name = "John Wick";
    context.locals.welcomeTitle = () => {
        return "Welcome back " + locals.user.name;
    };


    // return a Response or the result of calling `next()`
    return next();
};
```

Then you can use this information inside any `.astro` file with `Astro.locals`.

src/pages/orders.astro

```astro
---
const title = Astro.locals.welcomeTitle();
const orders = Array.from(Astro.locals.orders.entries());
const data = Astro.locals;
---
<h1>{title}</h1>
<p>This {data.property} is from middleware.</p>
<ul>
    {orders.map(order => {
        return <li>{/* do something with each order */}</li>;
    })}
</ul>
```

`locals` is an object that lives and dies within a single Astro route; when your route page is rendered, `locals` won’t exist anymore and a new one will be created. Information that needs to persist across multiple page requests must be stored elsewhere.

Note

The value of `locals` cannot be overridden at run time. Doing so would risk wiping out all the information stored by the user. Astro performs checks and will throw an error if `locals` are overridden.

## Example: redacting sensitive information

[Section titled “Example: redacting sensitive information”](#example-redacting-sensitive-information)

The example below uses middleware to replace “PRIVATE INFO” with the word “REDACTED” to allow you to render modified HTML on your page:

src/middleware.js

```js
export const onRequest = async (context, next) => {
    const response = await next();
    const html = await response.text();
    const redactedHtml = html.replaceAll("PRIVATE INFO", "REDACTED");


    return new Response(redactedHtml, {
        status: 200,
        headers: response.headers
    });
};
```

## Middleware types

[Section titled “Middleware types”](#middleware-types)

You can import and use the utility function `defineMiddleware()` to take advantage of type safety:

src/middleware.ts

```ts
import { defineMiddleware } from "astro:middleware";


// `context` and `next` are automatically typed
export const onRequest = defineMiddleware((context, next) => {


});
```

Instead, if you’re using JsDoc to take advantage of type safety, you can use `MiddlewareHandler`:

src/middleware.js

```js
/**
 * @type {import("astro").MiddlewareHandler}
 */
// `context` and `next` are automatically typed
export const onRequest = (context, next) => {


};
```

To type the information inside `Astro.locals`, which gives you autocompletion inside `.astro` files and middleware code, [extend the global types](/en/guides/typescript/#extending-global-types) by declaring a global namespace in the `env.d.ts` file:

src/env.d.ts

```ts
type User = {
  id: number;
  name: string;
};


declare namespace App {
  interface Locals {
    user: User;
    welcomeTitle: () => string;
    orders: Map<string, object>;
    session: import("./lib/server/session").Session | null;
  }
}
```

Then, inside the middleware file, you can take advantage of autocompletion and type safety.

## Chaining middleware

[Section titled “Chaining middleware”](#chaining-middleware)

Multiple middlewares can be joined in a specified order using [`sequence()`](/en/reference/modules/astro-middleware/#sequence):

src/middleware.js

```js
import { sequence } from "astro:middleware";


async function validation(_, next) {
    console.log("validation request");
    const response = await next();
    console.log("validation response");
    return response;
}


async function auth(_, next) {
    console.log("auth request");
    const response = await next();
    console.log("auth response");
    return response;
}


async function greeting(_, next) {
    console.log("greeting request");
    const response = await next();
    console.log("greeting response");
    return response;
}


export const onRequest = sequence(validation, auth, greeting);
```

This will result in the following console order:

```sh
validation request
auth request
greeting request
greeting response
auth response
validation response
```

## Rewriting

[Section titled “Rewriting”](#rewriting)

**Added in:** `astro@4.13.0`

The `APIContext` exposes a method called `rewrite()` which works the same way as [Astro.rewrite](/en/guides/routing/#rewrites).

Use `context.rewrite()` inside middleware to display a different page’s content without [redirecting](/en/guides/routing/#dynamic-redirects) your visitor to a new page. This will trigger a new rendering phase, causing any middleware to be re-executed.

src/middleware.js

```js
import { isLoggedIn } from "~/auth.js"
export function onRequest (context, next) {
  if (!isLoggedIn(context)) {
    // If the user is not logged in, update the Request to render the `/login` route and
    // add header to indicate where the user should be sent after a successful login.
    // Re-execute middleware.
    return context.rewrite(new Request("/login", {
      headers: {
        "x-redirect-to": context.url.pathname
      }
    }));
  }


  return next();
};
```

You can also pass the `next()` function an optional URL path parameter to rewrite the current `Request` without retriggering a new rendering phase. The location of the rewrite path can be provided as a string, URL, or `Request`:

src/middleware.js

```js
import { isLoggedIn } from "~/auth.js"
export function onRequest (context, next) {
  if (!isLoggedIn(context)) {
    // If the user is not logged in, update the Request to render the `/login` route and
    // add header to indicate where the user should be sent after a successful login.
    // Return a new `context` to any following middlewares.
    return next(new Request("/login", {
      headers: {
        "x-redirect-to": context.url.pathname
      }
    }));
  }


  return next();
};
```

The `next()` function accepts the same payload of [the `Astro.rewrite()` function](/en/reference/api-reference/#rewrite). The location of the rewrite path can be provided as a string, URL, or `Request`.

When you have multiple middleware functions chained via [sequence()](#chaining-middleware), submitting a path to `next()` will rewrite the `Request` in place and the middleware will not execute again. The next middleware function in the chain will receive the new `Request` with its updated `context`:

Calling `next()` with this signature will create a new `Request` object using the old `ctx.request`. This means that trying to consume `Request.body`, either before or after this rewrite, will throw a runtime error. This error is often raised with [Astro Actions that use HTML forms](/en/guides/actions/#call-actions-from-an-html-form-action). In these cases, we recommend handling rewrites from your Astro templates using `Astro.rewrite()` instead of using middleware.

src/middleware.js

```js
// Current URL is https://example.com/blog


// First middleware function
async function first(context, next) {
  console.log(context.url.pathname) // this will log "/blog"
  // Rewrite to a new route, the homepage
  // Return updated `context` which is passed to next function
  return next("/")
}


// Current URL is still https://example.com/blog


// Second middleware function
async function second(context, next) {
  // Receives updated `context`
  console.log(context.url.pathname) // this will log  "/"
  return next()
}


export const onRequest = sequence(first, second);
```

## Error pages

[Section titled “Error pages”](#error-pages)

Middleware will attempt to run for all on-demand rendered pages, even when a matching route cannot be found. This includes Astro’s default (blank) 404 page and any custom 404 pages. However, it is up to the [adapter](/en/guides/on-demand-rendering/) to decide whether that code runs. Some adapters may serve a platform-specific error page instead.

Middleware will also attempt to run before serving a 500 error page, including a custom 500 page, unless the server error occurred in the execution of the middleware itself. If your middleware does not run successfully, then you will not have access to `Astro.locals` to render your 500 page.

# Migrate an existing project to Astro

> Some tips and tricks for converting your site to Astro.

**Ready to convert your site to Astro?** See one of our guides for migration tips.

## Migration Guides

[Section titled “Migration Guides”](#migration-guides)

* ![](/logos/create-react-app.svg)

  ### [Create React App](/en/guides/migrate-to-astro/from-create-react-app/)

* ![](/logos/docusaurus.svg)

  ### [Docusaurus](/en/guides/migrate-to-astro/from-docusaurus/)

* ![](/logos/eleventy.svg)

  ### [Eleventy](/en/guides/migrate-to-astro/from-eleventy/)

* ![](/logos/gatsby.svg)

  ### [Gatsby](/en/guides/migrate-to-astro/from-gatsby/)

* ![](/logos/gitbook.svg)

  ### [GitBook](/en/guides/migrate-to-astro/from-gitbook/)

* ![](/logos/gridsome.svg)

  ### [Gridsome](/en/guides/migrate-to-astro/from-gridsome/)

* ![](/logos/hugo.svg)

  ### [Hugo](/en/guides/migrate-to-astro/from-hugo/)

* ![](/logos/jekyll.png)

  ### [Jekyll](/en/guides/migrate-to-astro/from-jekyll/)

* ![](/logos/nextjs.svg)

  ### [Next.js](/en/guides/migrate-to-astro/from-nextjs/)

* ![](/logos/nuxtjs.svg)

  ### [NuxtJS](/en/guides/migrate-to-astro/from-nuxtjs/)

* ![](/logos/pelican.svg)

  ### [Pelican](/en/guides/migrate-to-astro/from-pelican/)

* ![](/logos/sveltekit.svg)

  ### [SvelteKit](/en/guides/migrate-to-astro/from-sveltekit/)

* ![](/logos/vuepress.png)

  ### [VuePress](/en/guides/migrate-to-astro/from-vuepress/)

* ![](/logos/wordpress.svg)

  ### [WordPress](/en/guides/migrate-to-astro/from-wordpress/)

Note that many of these pages are **stubs**: they’re collections of resources waiting for your contribution!

## Why migrate your site to Astro?

[Section titled “Why migrate your site to Astro?”](#why-migrate-your-site-to-astro)

Astro provides many benefits: performance, simplicity, and many of the features you want built right into the framework. When you do need to extend your site, Astro provides several [official and 3rd-party community integrations](https://astro.build/integrations).

Migrating may be less work than you think!

Depending on your existing project, you may be able to use your existing:

* [UI framework components](/en/guides/framework-components/) directly in Astro.

* [CSS stylesheets or libraries](/en/guides/styling/) including Tailwind.

* [Markdown/MDX files](/en/guides/markdown-content/), configured using your existing [remark and rehype plugins](/en/guides/markdown-content/#markdown-plugins).

* [Content from a CMS](/en/guides/cms/) through an integration or API.

## Which projects can I convert to Astro?

[Section titled “Which projects can I convert to Astro?”](#which-projects-can-i-convert-to-astro)

[Many existing sites can be built with Astro](/en/concepts/why-astro/). Astro is ideally suited for your existing content-based sites like blogs, landing pages, marketing sites and portfolios. Astro integrates with several popular headless CMSes, and allows you to connect eCommerce shop carts.

Astro allows you have a fully statically-generated website, a dynamic app with routes rendered on demand, or a combination of both with [complete control over your project rendering](/en/guides/on-demand-rendering/), making it a great replacement for SSGs or for sites that need to fetch some page data on the fly.

## How will my project design change?

[Section titled “How will my project design change?”](#how-will-my-project-design-change)

Depending on your existing project, you may need to think differently about:

* Designing in [Astro Islands](/en/concepts/islands/#what-is-an-island) to avoid sending unnecessary JavaScript to the browser.

* Providing client-side interactivity with [client-side `<script>` tags](/en/guides/client-side-scripts/) or [UI framework components](/en/guides/framework-components/).

* Managing [shared state](/en/recipes/sharing-state-islands/) with Nano Stores or local storage instead of app-wide hooks or wrappers.

# Migrating from Create React App (CRA)

> Tips for migrating an existing Create React App project to Astro

Astro’s [React integration](/en/guides/integrations-guide/react/) provides support for [using React components inside Astro components](/en/guides/framework-components/), including entire React apps like Create React App (CRA)!

src/pages/index.astro

```astro
---
// Import your root App component
import App from '../cra-project/App.jsx';
---
<!-- Use a client directive to load your app -->
<App client:load />
```

See how to [Build a Single Page Application (SPA) with Astro](https://logsnag.com/blog/react-spa-with-astro) External using React Router.

Many apps will “just work” as full React apps when you add them directly to your Astro project with the React integration installed. This is a great way to get your project up and running immediately and keep your app functional while you migrate to Astro.

Over time, you can convert your structure piece-by-piece to a combination of `.astro` and `.jsx` components. You will probably discover you need fewer React components than you think!

Here are some key concepts and migration strategies to help you get started. Use the rest of our docs and our [Discord community](https://astro.build/chat) to keep going!

## Key Similarities between CRA and Astro

[Section titled “Key Similarities between CRA and Astro”](#key-similarities-between-cra-and-astro)

* The [syntax of `.astro` files is similar to JSX](/en/reference/astro-syntax/#differences-between-astro-and-jsx). Writing Astro should feel familiar.

* Astro uses file-based routing, and [allows specially named pages to create dynamic routes](/en/guides/routing/#dynamic-routes).

* Astro is [component-based](/en/basics/astro-components/), and your markup structure will be similar before and after your migration.

* Astro has [official integrations for React, Preact, and Solid](/en/guides/integrations-guide/react/) so you can use your existing JSX components. Note that in Astro, these files **must** have a `.jsx` or `.tsx` extension.

* Astro has support for [installing NPM packages](/en/guides/imports/#npm-packages), including React libraries. Many of your existing dependencies will work in Astro.

## Key Differences between CRA and Astro

[Section titled “Key Differences between CRA and Astro”](#key-differences-between-cra-and-astro)

When you rebuild your CRA site in Astro, you will notice some important differences:

* CRA is a single-page application that uses `index.js` as your project’s root. Astro is a multi-page site, and `index.astro` is your home page.

* [`.astro` components](/en/basics/astro-components/) are not written as exported functions that return page templating. Instead, you’ll split your code into a “code fence” for your JavaScript and a body exclusively for the HTML you generate.

* [content-driven](/en/concepts/why-astro/#content-driven): Astro was designed to showcase your content and to allow you to opt-in to interactivity only as needed. An existing CRA app might be built for high client-side interactivity and may require advanced Astro techniques to include items that are more challenging to replicate using `.astro` components, such as dashboards.

## Add your CRA to Astro

[Section titled “Add your CRA to Astro”](#add-your-cra-to-astro)

Your existing app can be rendered directly inside a new Astro project, often with no changes to your app’s code.

### Create a new Astro project

[Section titled “Create a new Astro project”](#create-a-new-astro-project)

Use the `create astro` command for your package manager to launch Astro’s CLI wizard and select a new “empty” Astro project.

* npm

  ```shell
  npm create astro@latest
  ```

* pnpm

  ```shell
  pnpm create astro@latest
  ```

* Yarn

  ```shell
  yarn create astro@latest
  ```

### Add integrations and dependencies

[Section titled “Add integrations and dependencies”](#add-integrations-and-dependencies)

Add the React integration using the `astro add` command for your package manager. If your app uses other packages supported by the `astro add` command, like Tailwind and MDX, you can add them all with one command:

* npm

  ```shell
  npx astro add react
  npx astro add react tailwind mdx
  ```

* pnpm

  ```shell
  pnpm astro add react
  pnpm astro add react tailwind mdx
  ```

* Yarn

  ```shell
  yarn astro add react
  yarn astro add react tailwind mdx
  ```

If your CRA requires any dependencies (e.g. NPM packages), then install them individually using the command line or by adding them to your new Astro project’s `package.json` manually and then running an install command. Note that many, but not all, React dependencies will work in Astro.

### Add your existing app files

[Section titled “Add your existing app files”](#add-your-existing-app-files)

Copy your existing Create React App (CRA) project source files and folders (e.g. `components`, `hooks`, `styles`, etc.) into a new folder inside `src/`, keeping its file structure so your app will continue to work. Note that all `.js` file extensions must be renamed to `.jsx` or `.tsx`.

Do not include any configuration files. You will use Astro’s own `astro.config.mjs`, `package.json`, and `tsconfig.json`.

Move the contents of your app’s `public/` folder (e.g. static assets) into Astro’s `public/` folder.

* public/

  * logo.png
  * favicon.ico
  * …

* src/

  * cra-project/

    * App.jsx
    * …

  * pages/

    * index.astro

* astro.config.mjs

* package.json

* tsconfig.json

### Render your app

[Section titled “Render your app”](#render-your-app)

Import your app’s root component in the frontmatter section of `index.astro`, then render the `<App />` component in your page template:

src/pages/index.astro

```astro
---
import App from '../cra-project/App.jsx';
---
<App client:load />
```

Client directives

Your app needs a [client directive](/en/reference/directives-reference/#client-directives) for interactivity. Astro will render your React app as static HTML until you opt-in to client-side JavaScript.

Use `client:load` to ensure your app loads immediately from the server, or `client:only="react"` to skip rendering on the server and run your app entirely client-side.

## Convert your CRA to Astro

[Section titled “Convert your CRA to Astro”](#convert-your-cra-to-astro)

After [adding your existing app to Astro](#add-your-cra-to-astro), you will probably want to convert your app itself to Astro!

You will replicate a similar component-based design [using Astro HTML templating components for your basic structure](/en/basics/astro-components/) while importing and including individual React components (which may themselves be entire apps!) for islands of interactivity.

Every migration will look different and can be done incrementally without disrupting your working app. Convert individual pieces at your own pace so that more and more of your app is powered by Astro components over time.

As you convert your React app, you will decide which React components you will [rewrite as Astro components](#converting-jsx-files-to-astro-files). Your only restriction is that Astro components can import React components, but React components must only import other React components:

src/pages/static-components.astro

```diff
---
+import MyReactComponent from '../components/MyReactComponent.jsx';
---
<html>
  <body>
    <h1>Use React components directly in Astro!</h1>
    +<MyReactComponent />
  </body>
</html>
```

Instead of importing Astro components into React components, you can nest React components inside a single Astro component:

src/pages/nested-components.astro

```astro
---
import MyReactSidebar from '../components/MyReactSidebar.jsx';
import MyReactButton from '../components/MyReactButton.jsx';
---
<MyReactSidebar>
  <p>Here is a sidebar with some text and a button.</p>
  <div slot="actions">
    <MyReactButton client:idle />
  </div>
</MyReactSidebar>
```

You may find it helpful to learn about [Astro islands](/en/concepts/islands/) and [Astro components](/en/basics/astro-components/) before restructuring your CRA as an Astro project.

### Compare: JSX vs Astro

[Section titled “Compare: JSX vs Astro”](#compare-jsx-vs-astro)

Compare the following CRA component and a corresponding Astro component:

* JSX

  StarCount.jsx

  ```jsx
  import React, { useState, useEffect } from 'react';
  import Header from './Header';
  import Footer from './Footer';


  const Component = () => {
  const [stars, setStars] = useState(0);
  const [message, setMessage] = useState('');


  useEffect(() => {
      const fetchData = async () => {
          const res = await fetch('https://api.github.com/repos/withastro/astro');
          const json = await res.json();


          setStars(json.stargazers_count || 0);
          setMessage(json.message);
      };


      fetchData();
  }, []);


  return (
      <>
          <Header />
          <p style={{
              backgroundColor: `#f4f4f4`,
              padding: `1em 1.5em`,
              textAlign: `center`,
              marginBottom: `1em`
          }}>Astro has {stars} 🧑‍🚀</p>
          <Footer />
      </>
  )
  };


  export default Component;
  ```

* Astro

  StarCount.astro

  ```astro
  ---
  import Header from './Header.astro';
  import Footer from './Footer.astro';
  import './layout.css';
  const res = await fetch('https://api.github.com/repos/withastro/astro')
  const json = await res.json();
  const message = json.message;
  const stars = json.stargazers_count || 0;
  ---
  <Header />
  <p class="banner">Astro has {stars} 🧑‍🚀</p>
  <Footer />
  <style>
    .banner {
      background-color: #f4f4f4;
      padding: 1em 1.5em;
      text-align: center;
      margin-bottom: 1em;
    }
  </style>
  ```

### Converting JSX files to `.astro` files

[Section titled “Converting JSX files to .astro files”](#converting-jsx-files-to-astro-files)

Here are some tips for converting a CRA `.js` component into a `.astro` component:

1. Use the returned JSX of the existing CRA component function as the basis for your HTML template.

2. Change any [CRA or JSX syntax to Astro](#reference-convert-cra-syntax-to-astro) or to HTML web standards. This includes `{children}` and `className`, for example.

3. Move any necessary JavaScript, including import statements, into a [“code fence” (`---`)](/en/basics/astro-components/#the-component-script). Note: JavaScript to [conditionally render content](/en/reference/astro-syntax/#dynamic-html) is often written inside the HTML template directly in Astro.

4. Use [`Astro.props`](/en/reference/api-reference/#props) to access any additional props that were previously passed to your CRA function.

5. Decide whether any imported components also need to be converted to Astro. You can keep them as React components for now, or forever. But, you may eventually want to convert them to `.astro` components, especially if they do not need to be interactive!

6. Replace `useEffect()` with import statements or [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to query your local files. Use `fetch()` to fetch external data.

### Migrating Tests

[Section titled “Migrating Tests”](#migrating-tests)

As Astro outputs raw HTML, it is possible to write end-to-end tests using the output of the build step. Any end-to-end tests written previously might work out-of-the-box if you have been able to match the markup of your CRA site. Testing libraries such as Jest and React Testing Library can be imported and used in Astro to test your React components.

See Astro’s [testing guide](/en/guides/testing/) for more.

## Reference: Convert CRA Syntax to Astro

[Section titled “Reference: Convert CRA Syntax to Astro”](#reference-convert-cra-syntax-to-astro)

### CRA Imports to Astro

[Section titled “CRA Imports to Astro”](#cra-imports-to-astro)

Update any [file imports](/en/guides/imports/) to reference relative file paths exactly. This can be done using [import aliases](/en/guides/typescript/#import-aliases), or by writing out a relative path in full.

Note that `.astro` and several other file types must be imported with their full file extension.

src/pages/authors/Fred.astro

```astro
---
import Card from '../../components/Card.astro';
---
<Card />
```

### CRA Children Props to Astro

[Section titled “CRA Children Props to Astro”](#cra-children-props-to-astro)

Convert any instances of `{children}` to an Astro `<slot />`. Astro does not need to receive `{children}` as a function prop and will automatically render child content in a `<slot />`.

src/components/MyComponent.astro

```diff
---
---
-export default function MyComponent(props) {
    -return (
      <div>
        -{props.children}
      </div>
-    );
-}


<div>
  <slot />
</div>
```

React components that pass multiple sets of children can be migrated to an Astro component using [named slots](/en/basics/astro-components/#named-slots).

See more about [specific `<slot />` usage in Astro](/en/basics/astro-components/#slots).

### CRA Data Fetching to Astro

[Section titled “CRA Data Fetching to Astro”](#cra-data-fetching-to-astro)

Fetching data in a Create React App component is similar to Astro, with some slight differences.

You will need to remove any instances of a side effect hook (`useEffect`) for either `import.meta.glob()` or `getCollection()`/`getEntry()` to access data from other files in your project source.

To [fetch remote data](/en/guides/data-fetching/), use `fetch()`.

These data requests are made in the frontmatter of the Astro component and use top-level await.

src/pages/index.astro

```astro
---
import { getCollection } from 'astro:content';


// Get all `src/content/blog/` entries
const allBlogPosts = await getCollection('blog');


// Get all `src/pages/posts/` entries
const allPosts = Object.values(import.meta.glob('../pages/post/*.md', { eager: true }));


// Fetch remote data
const response = await fetch('https://randomuser.me/api/');
const data = await response.json();
const randomUser = data.results[0];
---
```

See more about local files imports with [`import.meta.glob()`](/en/guides/imports/#importmetaglob), [querying using the Collections API](/en/guides/content-collections/#querying-collections) or [fetching remote data](/en/guides/data-fetching/).

### CRA Styling to Astro

[Section titled “CRA Styling to Astro”](#cra-styling-to-astro)

You may need to replace any [CSS-in-JS libraries](https://github.com/withastro/astro/issues/4432) (e.g. styled-components) with other available CSS options in Astro.

If necessary, convert any inline style objects (`style={{ fontWeight: "bold" }}`) to inline HTML style attributes (`style="font-weight:bold;"`). Or, use an [Astro `<style>` tag](/en/guides/styling/#styling-in-astro) for scoped CSS styles.

src/components/Card.astro

```diff
<div style={{backgroundColor: `#f4f4f4`, padding: `1em`}}>{message}</div>
<div style="background-color: #f4f4f4; padding: 1em;">{message}</div>
```

Tailwind is supported after installing the [Tailwind Vite plugin](/en/guides/styling/#tailwind). No changes to your existing Tailwind code are required!

See more about [Styling in Astro](/en/guides/styling/).

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

Your CRA might “just work” in Astro! But, you may likely need to make minor adjustments to duplicate your existing app’s functionality and/or styles.

If you cannot find your answers within these docs, please visit the [Astro Discord](https://astro.build/chat) and ask questions in our support forum!

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Code Fix: The SIBA Website's Move from Create-React-App to Astro ](https://brittanisavery.com/post/move-siba-to-astro)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Create React App to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-create-react-app.mdx)!

# Migrating from Docusaurus

> Tips for migrating an existing Docusaurus project to Astro

[Docusaurus](https://Docusaurus.io) is a popular documentation website builder built on React.

## Key Similarities between Docusaurus and Astro

[Section titled “Key Similarities between Docusaurus and Astro”](#key-similarities-between-docusaurus-and-astro)

Docusaurus and Astro share some similarities that will help you migrate your project:

* Both Astro and Docusaurus are modern, JavaScript-based (Jamstack) site builders intended for [content-driven websites](/en/concepts/why-astro/#content-driven), like documentation sites.

* Both Astro and Docusaurus support [MDX pages](/en/guides/markdown-content/). You should be able to use your existing `.mdx` files with Astro.

* Both Astro and Docusaurus use [file-based routing](/en/guides/routing/) to generate page routes automatically for any MDX file located in `src/pages`. Using Astro’s file structure for your existing content and when adding new pages should feel familiar.

* Astro has an [official integration for using React components](/en/guides/integrations-guide/react/). Note that in Astro, React files **must** have a `.jsx` or `.tsx` extension.

* Astro supports [installing NPM packages](/en/guides/imports/#npm-packages), including several for React. You may be able to keep some or all of your existing React components and dependencies.

* [Astro’s JSX-like syntax](/en/basics/astro-components/#the-component-template) should feel familiar if you are used to writing React.

## Key Differences between Docusaurus and Astro

[Section titled “Key Differences between Docusaurus and Astro”](#key-differences-between-docusaurus-and-astro)

When you rebuild your Docusaurus site in Astro, you will notice some important differences:

* Docusaurus is a React-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](/en/basics/astro-components/), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](/en/guides/framework-components/) and raw HTML templating.

* Docusaurus was designed to build documentation websites and has some built-in, documentation-specific website features that you would have to build yourself in Astro. Instead, Astro offers some of these features through [Starlight: an official docs theme](https://starlight.astro.build). This website was the inspiration for Starlight, and now runs on it! You can also find more [community docs themes](https://astro.build/themes?search=\&categories%5B%5D=docs) with built-in features in our Themes Showcase.

* Docusaurus sites use MDX pages for content. Astro’s docs theme uses Markdown (`.md`) files by default and does not require you to use MDX. You can optionally [install Astro’s MDX integration](/en/guides/integrations-guide/mdx/) (included in our Starlight theme by default) and use `.mdx` files in addition to standard Markdown files.

## Switch from Docusaurus to Astro

[Section titled “Switch from Docusaurus to Astro”](#switch-from-docusaurus-to-astro)

To convert a Docusaurus documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=\&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template starlight
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template starlight
  ```

* Yarn

  ```shell
  yarn create astro --template starlight
  ```

Astro’s MDX integration is included by default, so you can [bring your existing content files to Starlight](https://starlight.astro.build/getting-started/#add-content) right away.

You can find Astro’s docs starter, and other official templates, on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Speeding up documentation by 10 times (Russian) ](https://habr.com/ru/articles/880220/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Docusaurus site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-docusaurus.mdx)!

# Migrating from Eleventy

> Tips for migrating an existing Eleventy project to Astro

[Eleventy](https://11ty.dev) is an open-source static site generator that works with multiple template languages.

## Key Similarities between Eleventy (11ty) and Astro

[Section titled “Key Similarities between Eleventy (11ty) and Astro”](#key-similarities-between-eleventy-11ty-and-astro)

Eleventy (11ty) and Astro share some similarities that will help you migrate your project:

* Both Astro and Eleventy are modern, JavaScript-based (Jamstack) site builders.

* Astro and Eleventy both allow you to use a [headless CMS, APIs or Markdown files for data](/en/guides/data-fetching/). You can continue to use your preferred content authoring system, and will be able to keep your existing content.

## Key Differences between Eleventy (11ty) and Astro

[Section titled “Key Differences between Eleventy (11ty) and Astro”](#key-differences-between-eleventy-11ty-and-astro)

When you rebuild your Eleventy (11ty) site in Astro, you will notice some important differences:

* Eleventy supports a variety of templating languages. Astro supports [including components from several popular JS Frameworks (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/), but uses [Astro layouts, pages and components](/en/basics/astro-components/) for most page templating.

* Astro uses a [`src/` directory](/en/basics/project-structure/#src) for all files, including site metadata, that are available for querying and processing during site build. Within this is a [special `src/pages/` folder for file-based routing](/en/basics/astro-pages/).

* Astro uses a [`public/` folder for static assets](/en/basics/project-structure/#public) that do not need to be processed nor transformed during the build.

* In Eleventy, bundling CSS, JavaScript, and other assets needs to be configured manually. [Astro handles this for you out-of-the-box](/en/concepts/why-astro/#easy-to-use).

## Switch from Eleventy to Astro

[Section titled “Switch from Eleventy to Astro”](#switch-from-eleventy-to-astro)

To convert an Eleventy blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/).

Your Eleventy project allowed you to use a variety of templating languages to build your site. In an Astro project, your page templating will mostly be achieved with Astro components, which can be used as UI elements, layouts and even full pages. You may want to explore [Astro’s component syntax](/en/basics/astro-components/) to see how to template in Astro using components.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[This Site Is Now Built with Astro ](https://aqandrew.com/blog/now-built-with-astro/)Why I switched from Eleventy.

[Website Rewrite: 2025 ](https://www.welchcanavan.com/posts/site-rewrite-2025/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting an Eleventy site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-eleventy.mdx)!

# Migrating from Gatsby

> Tips for migrating an existing Gatsby project to Astro

Here are some key concepts and migration strategies to help you get started. Use the rest of our docs and our [Discord community](https://astro.build/chat) to keep going!

## Key Similarities between Gatsby and Astro

[Section titled “Key Similarities between Gatsby and Astro”](#key-similarities-between-gatsby-and-astro)

Gatsby and Astro share some similarities that will help you migrate your project:

* The [syntax of `.astro` files is similar to JSX](/en/reference/astro-syntax/#jsx-like-expressions). Writing Astro should feel familiar.

* Astro has built-in support for [Markdown](/en/guides/markdown-content/) and an integration for using MDX files. Also, you can configure and continue to use many of your existing Markdown plugins.

* Astro also has an [official integration for using React components](/en/guides/integrations-guide/react/). Note that in Astro, React files **must** have a `.jsx` or `.tsx` extension.

* Astro has support for [installing NPM packages](/en/guides/imports/#npm-packages), including React libraries. Many of your existing dependencies will work in Astro.

* Like Gatsby, Astro projects can be SSG or [SSR with page-level prerendering](/en/guides/on-demand-rendering/).

## Key Differences between Gatsby and Astro

[Section titled “Key Differences between Gatsby and Astro”](#key-differences-between-gatsby-and-astro)

When you rebuild your Gatsby site in Astro, you will notice some important differences:

* Gatsby projects are React single-page apps and use `index.js` as your project’s root. Astro projects are multi-page sites, and `index.astro` is your home page.

* [Astro components](/en/basics/astro-components/) are not written as exported functions that return page templating. Instead, you’ll split your code into a “code fence” for your JavaScript and a body exclusively for the HTML you generate.

* [Local file data](/en/guides/imports/): Gatsby uses GraphQL to retrieve data from your project files. Astro uses ESM imports and top-level await functions (e.g. [`import.meta.glob()`](/en/guides/imports/#importmetaglob), [`getCollection()`](/en/guides/content-collections/#querying-collections)) to import data from your project files. You can manually add GraphQL to your Astro project but it is not included by default.

## Convert your Gatsby Project

[Section titled “Convert your Gatsby Project”](#convert-your-gatsby-project)

Each project migration will look different, but there are some common actions you will perform when converting from Gatsby to Astro.

### Create a new Astro project

[Section titled “Create a new Astro project”](#create-a-new-astro-project)

Use the `create astro` command for your package manager to launch Astro’s CLI wizard or choose a community theme from the [Astro Theme Showcase](https://astro.build/themes).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters (e.g. `docs`, `blog`, `portfolio`). Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  # launch the Astro CLI Wizard
  npm create astro@latest


  # create a new project with an official example
  npm create astro@latest -- --template <example-name>
  ```

* pnpm

  ```shell
  # launch the Astro CLI Wizard
  pnpm create astro@latest


  # create a new project with an official example
  pnpm create astro@latest --template <example-name>
  ```

* Yarn

  ```shell
  # launch the Astro CLI Wizard
  yarn create astro@latest


  # create a new project with an official example
  yarn create astro@latest --template <example-name>
  ```

Then, copy your existing Gatsby project files over to your new Astro project into a separate folder outside of `src`.

Tip

Visit <https://astro.new> for the full list of official starter templates, and links for opening a new project in IDX, StackBlitz, CodeSandbox, or Gitpod.

### Install integrations (optional)

[Section titled “Install integrations (optional)”](#install-integrations-optional)

You may find it useful to install some of [Astro’s optional integrations](/en/guides/integrations-guide/) to use while converting your Gatsby project to Astro:

* **@astrojs/react**: to reuse some existing React UI components in your new Astro site or keep writing with React components.

* **@astrojs/mdx**: to bring existing MDX files from your Gatsby project, or to use MDX in your new Astro site.

### Put your code in `src`

[Section titled “Put your code in src”](#put-your-code-in-src)

Following [Astro’s project structure](/en/basics/project-structure/):

1. **Delete** Gatsby’s `public/` folder.

   Gatsby uses the `public/` directory for its build output, so you can safely discard this folder. You will no longer need a built version of your Gatsby site. (Astro uses `dist/` by default for the build output.)

2. **Rename** Gatsby’s `static/` folder to `public/`, and use it as Astro’s `public/` folder.

   Astro uses a folder called `public/` for static assets. You can alternatively copy the contents of `static/` into your existing Astro `public/` folder.

3. **Copy or Move** Gatsby’s other files and folders (e.g. `components`, `pages`, etc.) as needed into your Astro `src/` folder as you rebuild your site, following [Astro’s project structure](/en/basics/project-structure/).

   Astro’s `src/pages/` folder is a special folder used for file-based routing to create your site’s pages and posts from `.astro`, `.md` and `.mdx` files. You will not have to configure any routing behavior for your Astro, Markdown, and MDX files.

   All other folders are optional, and you can organize the contents of your `src/` folder any way you like. Other common folders in Astro projects include `src/layouts/`, `src/components`, `src/styles`, and `src/scripts`.

### Tips: Convert JSX files to `.astro` files

[Section titled “Tips: Convert JSX files to .astro files”](#tips-convert-jsx-files-to-astro-files)

Here are some tips for converting a Gatsby `.js` component into a `.astro` component:

1. Use only the `return()` of the existing Gatsby component function as your HTML template.

2. Change any [Gatsby or JSX syntax to Astro syntax](#reference-convert-to-astro-syntax) or to HTML web standards. This includes `<Link to="">`, `{children}`, and `className`, for example.

3. Move any necessary JavaScript, including import statements, into a [“code fence” (`---`)](/en/basics/astro-components/#the-component-script). Note: JavaScript to [conditionally render content](/en/reference/astro-syntax/#dynamic-html) is often written inside the HTML template directly in Astro.

4. Use [`Astro.props`](/en/reference/api-reference/#props) to access any additional props that were previously passed to your Gatsby function.

5. Decide whether any imported components also need to be converted to Astro. With the official React integration installed, you can [use existing React components in your Astro files](/en/guides/framework-components/). But, you may want to convert them to `.astro` components, especially if they do not need to be interactive!

6. Remove any GraphQL queries. Instead, use import and [`import.meta.glob()`](/en/guides/imports/#importmetaglob) statements to query your local files.

See [an example from Gatsby’s Blog starter template converted step-by-step](#guided-example-gatsby-layout-to-astro)

#### Compare: `.jsx` vs `.astro`

[Section titled “Compare: .jsx vs .astro”](#compare-jsx-vs-astro)

Compare the following Gatsby component and a corresponding Astro component:

* JSX

  component.jsx

  ```jsx
  import * as React from "react"
  import { useStaticQuery, graphql } from "gatsby"
  import Header from "./header"
  import Footer from "./footer"
  import "./layout.css"


  const Component = ({ message, children }) => {
    const data = useStaticQuery(graphql`
      query SiteTitleQuery {
        site {
          siteMetadata {
            title
          }
        }
      }
    `)
    return (
      <>
        <Header siteTitle={data.site.siteMetadata.title} />
        <div style={{ margin: `0`, maxWidth: `960`}}>{message}</div>
        <main>{children}</main>
        <Footer siteTitle={data.site.siteMetadata} />
      </>
    )
  }


  export default Component
  ```

* Astro

  component.astro

  ```astro
  ---
  import Header from "./Header.astro"
  import Footer from "./Footer.astro"
  import "../styles/stylesheet.css"
  import { site } from "../data/siteMetaData.js"
  const { message } = Astro.props
  ---
  <Header siteTitle={site.title} />
    <div style="margin: 0; max-width: 960;">{message}</div>
    <main>
      <slot />
    </main>
  <Footer siteTitle={site.title} />
  ```

### Migrating Layout Files

[Section titled “Migrating Layout Files”](#migrating-layout-files)

You may find it helpful to start by converting your Gatsby layouts and templates into [Astro layout components](/en/basics/layouts/).

Each Astro page explicitly requires `<html>`, `<head>`, and `<body>` tags to be present, so it is common to reuse a layout file across pages. Astro uses a [`<slot />`](/en/basics/astro-components/#slots) instead of React’s `{children}` prop for page content, with no import statement required. Your Gatsby `layout.js` and templates will not include these.

Note the standard HTML templating, and direct access to `<head>`:

src/layouts/Layout.astro

```astro
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <title>Astro</title>
  </head>
  <body>
    <!-- Wrap the slot element with your existing layout templating -->
    <slot />
  </body>
</html>
```

You may also wish to reuse code from Gatsby’s `src/components/seo.js` to include additional site metadata. Notice that Astro uses neither `<Helmet>` nor `<Header>` but instead creates `<head>` directly. You may import and use components, even within `<head>`, to separate and organize your page content.

### Migrating Pages and Posts

[Section titled “Migrating Pages and Posts”](#migrating-pages-and-posts)

In Gatsby, your [pages and posts](/en/basics/astro-pages/) may exist in `src/pages/` or outside of `src` in another folder, like `content`. In Astro, all your page content must live within `src/` unless you are using [content collections](/en/guides/content-collections/).

#### React Pages

[Section titled “React Pages”](#react-pages)

Your existing Gatsby JSX (`.js`) pages will need to be [converted from JSX files to `.astro` pages](#tips-convert-jsx-files-to-astro-files). You cannot use an existing JSX page file in Astro.

These [`.astro` pages](/en/basics/astro-pages/) must be located within `src/pages/` and will have page routes generated automatically based on their file path.

#### Markdown and MDX pages

[Section titled “Markdown and MDX pages”](#markdown-and-mdx-pages)

Astro has built-in support for Markdown and an optional integration for MDX files. Your existing [Markdown and MDX files](/en/guides/markdown-content/) can be reused but may require some adjustments to their frontmatter, such as adding [Astro’s special `layout` frontmatter property](/en/basics/layouts/#markdown-layouts). They can also be placed within `src/pages/` to take advantage of automatic file-based routing.

Alternatively, you can use [content collections](/en/guides/content-collections/) in Astro to store and manage your content. You will retrieve the content yourself and [generate those pages dynamically](/en/guides/content-collections/#generating-routes-from-content).

### Migrating Tests

[Section titled “Migrating Tests”](#migrating-tests)

As Astro outputs raw HTML, it is possible to write end-to-end tests using the output of the build step. Any end-to-end tests written previously might work out-of-the-box if you have been able to match the markup of the older Gatsby site. Testing libraries such as Jest and React Testing Library can be imported and used in Astro to test your React components.

See Astro’s [testing guide](/en/guides/testing/) for more.

### Repurpose config files

[Section titled “Repurpose config files”](#repurpose-config-files)

Gatsby has several top-level configuration files that also include site and page metadata and are used for routing. You will not use any of these `gatsby-*.js` files in your Astro project, but there may be some content that you can reuse as you build your Astro project:

* `gatsby-config.js`: Move your `siteMetadata: {}` into `src/data/siteMetadata.js` (or `siteMetadata.json`) to import data about your site (title, description, social accounts, etc.) into page layouts.

* `gatsby-browser.js`: Consider adding anything used here directly into your [main layout](#migrating-layout-files)’s `<head>` tag.

* `gatsby-node.js`: You will not need to create your own nodes in Astro, but viewing the schema in this file may help you with defining types in your Astro project.

* `gatsby-ssr.js`: If you choose to use SSR in Astro, you will [add and configure the SSR adapter](/en/guides/on-demand-rendering/) of your choice directly in `astro.config.mjs`.

## Reference: Convert to Astro Syntax

[Section titled “Reference: Convert to Astro Syntax”](#reference-convert-to-astro-syntax)

The following are some examples of Gatsby-specific syntax that you will need to convert to Astro. See more [differences between Astro and JSX](/en/reference/astro-syntax/#differences-between-astro-and-jsx) in the guide to writing Astro components.

### Gatsby Links to Astro

[Section titled “Gatsby Links to Astro”](#gatsby-links-to-astro)

Convert any Gatsby `<Link to="">`, `<NavLink>` etc. components to HTML `<a href="">` tags.

```diff
-<Link to="/blog">Blog</Link>
<a href="/blog">Blog</a>
```

Astro does not use any special component for links, although you are welcome to build your own `<Link>` component. You can then import and use this `<Link>` just as you would any other component.

src/components/Link.astro

```astro
---
const { to } = Astro.props
---
<a href={to}><slot /></a>
```

### Gatsby Imports to Astro

[Section titled “Gatsby Imports to Astro”](#gatsby-imports-to-astro)

If necessary, update any [file imports](/en/guides/imports/) to reference relative file paths exactly. This can be done using [import aliases](/en/guides/typescript/#import-aliases), or by writing out a relative path in full.

Note that `.astro` and several other file types must be imported with their full file extension.

src/pages/authors/Fred.astro

```astro
---
import Card from `../../components/Card.astro`;
---
<Card />
```

### Gatsby Children Props to Astro

[Section titled “Gatsby Children Props to Astro”](#gatsby-children-props-to-astro)

Convert any instances of `{children}` to an Astro `<slot />`. Astro does not need to receive `{children}` as a function prop and will automatically render child content in a `<slot />`.

src/components/MyComponent

```diff
---
---
-export default function MyComponent(props) {
    -return (
      <div>
        -{props.children}
      </div>
-    );
-}


<div>
  <slot />
</div>
```

React components that pass multiple sets of children can be migrated to an Astro component using [named slots](/en/basics/astro-components/#named-slots).

See more about [specific `<slot />` usage in Astro](/en/basics/astro-components/#slots).

### Gatsby Styling to Astro

[Section titled “Gatsby Styling to Astro”](#gatsby-styling-to-astro)

You may need to replace any [CSS-in-JS libraries](https://github.com/withastro/astro/issues/4432) (e.g. styled-components) with other available CSS options in Astro.

If necessary, convert any inline style objects (`style={{ fontWeight: "bold" }}`) to inline HTML style attributes (`style="font-weight:bold;"`). Or, use an [Astro `<style>` tag](/en/guides/styling/#styling-in-astro) for scoped CSS styles.

src/components/Card.astro

```diff
<div style={{backgroundColor: `#f4f4f4`, padding: `1em`}}>{message}</div>
<div style="background-color: #f4f4f4; padding: 1em;">{message}</div>
```

Tailwind is supported after installing the [Tailwind Vite plugin](/en/guides/styling/#tailwind). No changes to your existing Tailwind code are required!

Global styling is achieved in Gatsby using CSS imports in `gatsby-browser.js`. In Astro, you will import `.css` files directly into a main layout component to achieve global styles.

See more about [Styling in Astro](/en/guides/styling/).

### Gatsby Image Plugin to Astro

[Section titled “Gatsby Image Plugin to Astro”](#gatsby-image-plugin-to-astro)

Convert Gatsby’s `<StaticImage />` and `<GatsbyImage />` components to [Astro’s own image integration components](/en/guides/images/), or to a [standard HTML `<img>` / JSX `<img />`](/en/guides/images/#images-in-ui-framework-components) tag as appropriate in your React components.

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';
---
<Image src={rocket} alt="A rocketship in space." />
<img src={rocket.src} alt="A rocketship in space.">
```

Astro’s `<Image />` component works in `.astro` and `.mdx` files only. See a [full list of its component attributes](/en/reference/modules/astro-assets/#image-properties) and note that several will differ from Gatsby’s attributes.

To continue using [images in Markdown (`.md`) files](/en/guides/images/#images-in-markdown-files) using standard Markdown syntax (`![]()`), you may need to update the link. Using the HTML `<img>` tag directly is not supported in `.md` files for local images, and must be converted to Markdown syntax.

src/pages/post-1.md

```md
# My Markdown Page


<!-- Local image stored at src/assets/stars.png -->
![A starry night sky.](../assets/stars.png)
```

In React (`.jsx`) components, use standard JSX image syntax (`<img />`). Astro will not optimize these images, but you can install and use NPM packages for more flexibility.

You can learn more about [using images in Astro](/en/guides/images/) in the Images Guide.

### Gatsby GraphQL to Astro

[Section titled “Gatsby GraphQL to Astro”](#gatsby-graphql-to-astro)

Remove all references to GraphQL queries, and instead use [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to access data from your local files.

Or, if using content collections, query your Markdown and MDX files using [`getEntry()` and `getCollection()`](/en/guides/content-collections/#generating-routes-from-content).

These data requests are made in the frontmatter of the Astro component using the data.

src/pages/index.astro

```diff
---
-import { graphql } from "gatsby"
import { getCollection } from 'astro:content';


// Get all `src/content/blog/` entries
const allBlogPosts = await getCollection('blog');


// Get all `src/pages/posts/` entries
const allPosts = Object.values(import.meta.glob('../pages/post/*.md', { eager: true }));
---


-export const pageQuery = graphql`
  -{
    -allMarkdownRemark(sort: { frontmatter: { date: DESC } }) {
-      nodes {
-        excerpt
-        fields {
-          slug
-        }
-        frontmatter {
          -date(formatString: "MMMM DD, YYYY")
-          title
-          description
-        }
-      }
-    }
  -}
-`
```

## Guided example: Gatsby layout to Astro

[Section titled “Guided example: Gatsby layout to Astro”](#guided-example-gatsby-layout-to-astro)

This example converts the main project layout (`layout.js`) from Gatsby’s blog starter to `src/layouts/Layout.astro`.

This page layout shows one header when visiting the home page, and a different header with a link back to Home for all other pages.

1. Identify the `return()` JSX.

   layout.js

   ```jsx
   import * as React from "react"
   import { Link } from "gatsby"
   const Layout = ({ location, title, children }) => {
     const rootPath = `${__PATH_PREFIX__}/`
     const isRootPath = location.pathname === rootPath
     let header
     if (isRootPath) {
       header = (
         <h1 className="main-heading">
           <Link to="/">{title}</Link>
         </h1>
       )
     } else {
       header = (
         <Link className="header-link-home" to="/">
           Home
         </Link>
       )
     }
     return (
       <div className="global-wrapper" data-is-root-path={isRootPath}>
         <header className="global-header">{header}</header>
         <main>{children}</main>
         <footer>
           © {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.gatsbyjs.com">Gatsby</a>
         </footer>
       </div>
     )
   }
   export default Layout
   ```

2. Create `Layout.astro` and add this `return` value, [converted to Astro syntax](#reference-convert-to-astro-syntax).

   Note that:

   * `{new Date().getFullYear()}` just works 🎉
   * `{children}` becomes `<slot />` 🦥
   * `className` becomes `class` 📛
   * `Gatsby` becomes `Astro` 🚀

   src/layouts/Layout.astro

   ```astro
   ---
   ---
   <div class="global-wrapper" data-is-root-path={isRootPath}>
     <header class="global-header">{header}</header>
     <main><slot /></main>
     <footer>
       © {new Date().getFullYear()}, Built with
       {` `}
       <a href="https://www.astro.build">Astro</a>
     </footer>
   </div>
   ```

3. Add a page shell so that your layout provides each page with the necessary parts of an HTML document:

   src/layouts/Layout.astro

   ```diff
   ---
   ---
   <html>
     <head>
       <meta charset="utf-8" />
       <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
       <meta name="viewport" content="width=device-width" />
       <title>Astro</title>
     </head>
     <body>
       <div class="global-wrapper" data-is-root-path={isRootPath}>
         <header class="global-header">{header}</header>
         <main>
           <slot />
         </main>
         <footer>
           &#169; {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.astro.build">Astro</a>
         </footer>
       </div>
     </body>
   </html>
   ```

4. Add any needed imports, props, and JavaScript

   To conditionally render a header based on the page route and title in Astro:

   * Provide the props via `Astro.props`. (Remember: your Astro templating accesses props from its frontmatter, not passed into a function.)
   * Use a ternary operator to show one heading if this is the home page, and a different heading otherwise.
   * Remove variables for `{header}` and `{isRootPath}` as they are no longer needed.
   * Replace Gatsby’s `<Link/>` tags with `<a>` anchor tags.
   * Use `class` instead of `className`.
   * Import a local stylesheet from your project for the class names to take effect.

   src/layouts/Layout.astro

   ```diff
   ---
   +import '../styles/style.css';
   +const { title, pathname } = Astro.props
   ---
   <html>
     <head>
       <meta charset="utf-8" />
       <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
       <meta name="viewport" content="width=device-width" />
       <title>Astro</title>
     </head>
     <body>
       <div class="global-wrapper">
         <header class="global-header">
           +{ pathname === "/"
           +?
             <h1 class="main-heading">
             <a href="/">{title}</a>
             </h1>
           +:
             <h1 class="main-heading">
             <a class="header-link-home" href="/">Home</a>
             </h1>
           +}
         </header>
         <main>
           <slot />
         </main>
         <footer>
           &#169; {new Date().getFullYear()}, Built with
           {` `}
           <a href="https://www.astro.build">Astro</a>
         </footer>
       </div>
     </body>
   </html>
   ```

5. Update `index.astro` to use this new layout and pass it the necessary `title` and `pathname` props:

   src/pages/index.astro

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   const pagePathname = Astro.url.pathname
   ---
   <Layout title="Home Page" pathname={pagePathname}>
       <p>Astro</p>
   </Layout>
   ```

   Tip

   You can [get the current page’s path using `Astro.url`](/en/reference/api-reference/#url).

6. To test the conditional header, create a second page, `about.astro` using the same pattern:

   src/pages/about.astro

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   const pagePathname = Astro.url.pathname
   ---
   <Layout title="About" pathname={pagePathname}>
       <p>About</p>
   </Layout>
   ```

   You should see a link to “Home” only when visiting the About page.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Migrating from Gatsby to Astro ](https://loige.co/migrating-from-gatsby-to-astro/)How and why I migrated this blog from Gatsby to Astro and what I learned in the process.

[Migrating to Astro was EZ ](https://joelhooks.com/migrating-to-astro-was-ez)This is about the process of migrating from Gatsby to Astro, and why I chose Astro.

[My Switch from Gatsby to Astro ](https://www.joshfinnie.com/blog/my-switch-from-gatsby-to-astro/)The switch to Astro is definitely worth a blog post! It’s revolutionizing the static web development scene for the better.

[Why I moved to Astro from Gatsby ](https://dev.to/askrodney/why-i-moved-to-astro-from-gatsby-3fck)Taking a quick look at what made me want to switch and why Astro was a good fit.

[Another Migration: From Gatsby to Astro ](https://logarithmicspirals.com/blog/migrating-from-gatsby-to-astro/)Learn about how I transitioned my personal website from Gatsby to Astro as I share insights and experiences from the migration process.

[From Gatsby gridlock to Astro bliss: my personal site redesign ](https://jwn.gr/posts/migrating-from-gatsby-to-astro/)Gatsby has shown its age and I found myself seeking a modern alternative. Enter Astro — a framework that has breathed some new life into this site.

[Why and how I moved my blog away from Gatsby and React to Astro Js and Preact ](https://www.helmerdavila.com/blog/en/why-and-how-i-moved-my-blog-away-from-gatsby-and-react-to-astro-js-and-preact)All is about simplicity and power at the same time.

[How I rewrote my HUGE Gatsby site in Astro and learned to love it in the process ](https://dunedinsound.com/blog/how_i_rewrote_my_huge_gatsby_site_in_astro_and_learned_to_love_it_in_the_process/)Everything is faster. Happier. More productive.

[How I switched from Gatsby to Astro (While Keeping Drupal in the Mix) ](https://albert.skibinski.nl/en/blog/how-i-switched-gatsby-astro-while-keeping-drupal-mix/)I came across the relatively new Astro, which ticked all the boxes.

[Migrating my website from Gatsby to Astro ](https://dev.to/flashblaze/migrating-my-website-from-gatsby-to-astro-2ej5)Astro has entered the chat.

[Gatsby to Astro ](https://alvin.codes/writing/gatsby-to-astro)Why and how I migrated this website from Gatsby to Astro.

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Gatsby site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gatsby.mdx)!

# Migrating from GitBook

> Tips for migrating an existing GitBook project to Astro

[GitBook](https://gitbook.com) is a web-based platform for creating and publishing documentation and books in a collaborative manner, with version control integration and customizable features.

## Key Similarities between GitBook and Astro

[Section titled “Key Similarities between GitBook and Astro”](#key-similarities-between-gitbook-and-astro)

GitBook and Astro share some similarities that will help you migrate your project:

* Both Astro and GitBook support [Markdown](/en/guides/markdown-content/). You can migrate all your existing documentation utilizing GitBook’s Git Sync feature.

* Both Astro and GitBook use some form of [file-based routing](/en/guides/routing/). Using Astro’s file structure for your existing content and when adding new pages should feel familiar.

## Key Differences between GitBook and Astro

[Section titled “Key Differences between GitBook and Astro”](#key-differences-between-gitbook-and-astro)

When you migrate your GitBook docs to Astro, you will notice some important differences:

* A GitBook site is edited using an online dashboard. In Astro, you will use a [code editor](/en/editor-setup/) and development environment to maintain your site. You can develop locally on your machine, or choose a cloud editor/development environment like IDX, StackBlitz, CodeSandbox, or Gitpod.

* GitBook stores your content in a database. In Astro, you will have individual files (typically Markdown or MDX) in your [project directory](/en/basics/project-structure/) for each page’s content. Or, you can choose to use a [CMS for your content](/en/guides/cms/) and use Astro to fetch and present the data.

* GitBook uses a custom syntax on top of Markdown for content. Astro supports Markdoc via the optional [Markdoc integration](/en/guides/integrations-guide/markdoc/), which features a similar syntax to the one you would use in GitBook.

## Switch from GitBook to Astro

[Section titled “Switch from GitBook to Astro”](#switch-from-gitbook-to-astro)

To convert a GitBook documentation site to Astro, start with our official [Starlight docs theme starter template](https://starlight.astro.build), or explore more community docs themes in our [theme showcase](https://astro.build/themes?search=\&categories%5B%5D=docs).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template starlight
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template starlight
  ```

* Yarn

  ```shell
  yarn create astro --template starlight
  ```

Once you have a new Astro project, you can sync your existing GitBook content to your new Astro project. GitBook has a [Git Sync feature](https://docs.gitbook.com/product-tour/git-sync) that will automatically sync your GitBook content to a GitHub/GitLab repository.

To sync directly to the docs template’s content collection, specify `src/content/docs/en` or `src/content/docs` as the project directory.

Caution

When enabling Git Sync be sure to specify “**GitBook to GitHub**” as the priority. This will ensure that your GitBook content is synced to your GitHub repository. Otherwise, you will overwrite your existing GitBook content.

After syncing the content, you will now have a copy of your GitBook content in your Astro repository. Disable git sync to prevent future syncing with GitBook.

Note that although you now have your content migrated to your Astro project, it will not be immediately usable. To use this content in your Astro site, you will need to spend some time manually changing GitBook’s syntax into a format compatible with Astro. In particular:

* Astro’s [Markdoc integration](/en/guides/integrations-guide/markdoc/) requires that the file extension be `.mdoc`. This is to avoid conflicts with other Markdown extensions like `.mdx` and `.md`.
* GitBook syntax differs from Markdoc where the `/` prefix denoting a closing tag is replaced with `end` for GitBook files. You will need to update this notation throughout your files.
* Some features of GitBook rely on custom components. These components will not exist in Astro and must be created and added to your project through [Markdoc’s config `tags` attribute](/en/guides/integrations-guide/markdoc/#use-astro-components-as-markdoc-tags) or removed from your files.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a GitBook site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gitbook.mdx)!

# Migrating from Gridsome

> Tips for migrating an existing Gridsome project to Astro

[Gridsome](https://gridsome.org) is an open-source static site generator built on Vue and GraphQL.

## Key Similarities between Gridsome and Astro

[Section titled “Key Similarities between Gridsome and Astro”](#key-similarities-between-gridsome-and-astro)

Gridsome and Astro share some similarities that will help you migrate your project:

* Both Gridsome and Astro are modern JavaScript static-site generators with similar [project file structures](/en/basics/project-structure/#directories-and-files).

* Both Gridsome and Astro use a `src/` folder for your project files and a [special `src/pages/` folder for file-based routing](/en/basics/astro-pages/). Creating and managing pages for your site should feel familiar.

* Astro has [an official integration for using Vue components](/en/guides/integrations-guide/vue/) and supports [installing NPM packages](/en/guides/imports/#npm-packages), including several for Vue. You will be able to write Vue UI components, and may be able to keep some or all of your existing Gridsome Vue components and dependencies.

* Astro and Gridsome both allow you to use a [headless CMS, APIs or Markdown files for data](/en/guides/data-fetching/). You can continue to use your preferred content authoring system, and will be able to keep your existing content.

## Key Differences between Gridsome and Astro

[Section titled “Key Differences between Gridsome and Astro”](#key-differences-between-gridsome-and-astro)

When you rebuild your Gridsome site in Astro, you will notice some important differences:

* Gridsome is a Vue-based single-page application (SPA). Astro sites are multi-page apps built using [`.astro` components](/en/basics/astro-components/), but can also support [React, Preact, Vue.js, Svelte, SolidJS, AlpineJS](/en/guides/framework-components/) and raw HTML templating.

* As an SPA, Gridsome uses `vue-router` for SPA routing, and `vue-meta` for managing `<head>`. In Astro, you will create separate HTML pages and control your page `<head>` directly, or in a [layout component](/en/basics/layouts/).

* [Local file data](/en/guides/imports/): Gridsome uses GraphQL to retrieve data from your project files. Astro uses ESM imports and [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to import data from local project files. Remote resources can be loaded using the standard `fetch()` API. GraphQL may be optionally added to your project, but is not included by default.

## Switch from Gridsome to Astro

[Section titled “Switch from Gridsome to Astro”](#switch-from-gridsome-to-astro)

To convert a Gridsome blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/).

Since Gridsome’s project structure is similar to Astro’s, you may be able to copy several existing files from your project into the same location in your new Astro project. However, the two project structures are not identical. You may want to examine [Astro’s project structure](/en/basics/project-structure/) to see what the differences are.

Since Astro queries and imports your local files differently than Gridsome, you may want to read about how to load files using [`import.meta.glob()`](/en/guides/imports/#importmetaglob) to understand how to work with your local files.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Migration from Gridsome to Astro ](https://fyodor.io/migration-from-gridsome-to-astro/)

[Hello Astro! ](https://thamas.hu/astro-hello)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Gridsome site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-gridsome.mdx)!

# Migrating from Hugo

> Tips for migrating an existing Hugo project to Astro

[Hugo](https://gohugo.io) is an open-source static site generator built on Go.

## Key Similarities between Hugo and Astro

[Section titled “Key Similarities between Hugo and Astro”](#key-similarities-between-hugo-and-astro)

Hugo and Astro share some similarities that will help you migrate your project:

* Hugo and Astro are both modern static-site generators, ideally suited to [content-driven websites](/en/concepts/why-astro/#content-driven) like blogs.

* Hugo and Astro both allow you to [author your content in Markdown](/en/guides/markdown-content/). However, Hugo includes several special frontmatter properties and allows you to write frontmatter in YAML, TOML or JSON. Even though many of your existing Hugo frontmatter properties will not be “special” in Astro, you can continue to use your existing Markdown files and YAML (or TOML) frontmatter values.

* Hugo and Astro both allow you to enhance your site with a variety of [integrations and external packages](https://astro.build/integrations/).

## Key Differences between Hugo and Astro

[Section titled “Key Differences between Hugo and Astro”](#key-differences-between-hugo-and-astro)

When you rebuild your Hugo site in Astro, you will notice some important differences:

* Hugo uses Go Templating for page templating. [Astro syntax](/en/basics/astro-components/) is a JSX-like superset of HTML.

* Astro does not use shortcodes for dynamic content in standard Markdown files, but [Astro’s MDX integration](/en/guides/integrations-guide/mdx/) does allow you to use JSX and import components in MDX files.

* While Hugo can use “partials” for reusable layout elements, [Astro is entirely component-based](/en/basics/astro-components/). Any `.astro` file can be a component, a layout or an entire page, and can import and render any other Astro components. Astro components can also include [other UI framework components (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/) as well as content or metadata from [other files in your project](/en/guides/imports/), such as Markdown or MDX.

## Switch from Hugo to Astro

[Section titled “Switch from Hugo to Astro”](#switch-from-hugo-to-astro)

To convert a Hugo blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

Bring your existing Markdown (or MDX, with our optional integration) files as content to [create Markdown or MDX pages](/en/guides/markdown-content/). Astro allows YAML or TOML frontmatter in these files, so if you are using JSON frontmatter, you will need to convert it.

To continue to use dynamic content such as variables, expressions or UI components within your Markdown content, add Astro’s optional MDX integration and convert your existing Markdown files to [MDX pages](/en/guides/markdown-content/). MDX supports YAML and TOML frontmatter, so you can keep your existing frontmatter properties. But, you must replace any shortcode syntax with [MDX’s own syntax](https://mdxjs.com/docs/what-is-mdx/#mdx-syntax), which allows JSX expressions and/or component imports.

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Elio Struyf's migration story from Hugo to Astro ](https://www.eliostruyf.com/migration-story-hugo-astro/)

[Hugo Vs Astro - Which Static Site Generator To Choose In 2023 ](https://onebite.dev/hugo-vs-astro-which-static-site-generator-to-choose-in-2023/)

[Lessons from an AI-assisted migration to Astro ](https://bennet.org/blog/lessons-from-ai-assisted-migration-to-astro/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Hugo site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-hugo.mdx)!

# Migrating from Jekyll

> Tips for migrating an existing Jekyll project to Astro

[Jekyll](https://jekyllrb.com) is a static site generator built on Ruby.

## Key Similarities between Jekyll and Astro

[Section titled “Key Similarities between Jekyll and Astro”](#key-similarities-between-jekyll-and-astro)

Jekyll and Astro share some similarities that will help you migrate your project:

* Both Jekyll and Astro are static-site generators, commonly used to create blogs.

* Both Jekyll and Astro allow you to write your content in Markdown and HTML. Jekyll and Astro both provide some special frontmatter YAML properties for page layout and unpublished draft posts. You can continue to use your existing Markdown files in Astro.

* Both Jekyll and Astro use [file-based routing](/en/guides/routing/) for creating pages from your blog posts. Astro provides a [special `src/pages/` directory for all pages and posts](/en/basics/project-structure/#srcpages). Jekyll uses a similar special folder called `_posts/` for your Markdown blog posts, however your site pages can exist elsewhere. Creating new blog posts should feel familiar.

## Key Differences between Jekyll and Astro

[Section titled “Key Differences between Jekyll and Astro”](#key-differences-between-jekyll-and-astro)

When you rebuild your Jekyll site in Astro, you will notice some important differences:

* As Jekyll is primarily a blogging platform, several blog features are built-in that you may have to build yourself in Astro. Or, choose a [blog starter template theme](https://astro.build/themes?search=\&categories%5B%5D=blog) that includes these features. For example, Jekyll has built-in support for tags and categories which you will find in several Astro blog themes, but is not included in a minimal Astro project.

* Jekyll uses Liquid templates for reusable layout elements and templating. Astro uses JSX-like [`.astro` files for templating and components](/en/basics/astro-components/). Any `.astro` file can be a component, a layout or an entire page, and can import and render any other Astro components. You can also build using [other UI framework components (e.g. React, Svelte, Vue, Solid)](/en/guides/framework-components/) as well as content or metadata from [other files in your project](/en/guides/imports/), such as Markdown or MDX.

## Switch from Jekyll to Astro

[Section titled “Switch from Jekyll to Astro”](#switch-from-jekyll-to-astro)

To convert a Jekyll blog to Astro, start with our blog theme starter template, or explore more community blog themes in our [theme showcase](https://astro.build/themes/).

You can pass a `--template` argument to the `create astro` command to start a new Astro project with one of our official starters. Or, you can [start a new project from any existing Astro repository on GitHub](/en/install-and-setup/#install-from-the-cli-wizard).

* npm

  ```shell
  npm create astro@latest -- --template blog
  ```

* pnpm

  ```shell
  pnpm create astro@latest --template blog
  ```

* Yarn

  ```shell
  yarn create astro --template blog
  ```

Bring your existing Markdown files as content to [create Markdown pages](/en/guides/markdown-content/), using an [Astro Markdown layout](/en/basics/layouts/#markdown-layouts) instead of a Liquid template.

Much of your existing HTML page content can be converted into [Astro pages](/en/basics/astro-pages/), and you will additionally be able to [use variables, JSX-like expressions and component imports directly in your HTML templating](/en/reference/astro-syntax/#jsx-like-expressions).

Astro does not have a `permalink` property that accepts placeholders. You may need to read more about [Astro’s page routing](/en/guides/routing/) if you want to keep your existing URL structure. Or, consider [setting redirects at a host like Netlify](https://docs.netlify.com/routing/redirects/).

To convert other types of sites, such as a portfolio or documentation site, see more official starter templates on [astro.new](https://astro.new). You’ll find a link to each project’s GitHub repository, as well as one-click links to open a working project in IDX, StackBlitz, CodeSandbox and Gitpod online development environments.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[From Jekyll to Astro ](https://jackcarey.co.uk/posts/astro-rewrite/)

[Goodbye Jekyll, Hello Astro ](https://kiranrao.in/blog/bye-jekyll-hello-astro/)

[Back to the Future: Our Tech Blog's Transition from Jekyll to Astro ](https://alasco.tech/2023/09/06/migrating-to-astro)

Have a resource to share?

If you found (or made!) a helpful video or blog post about converting a Jekyll site to Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/migrate-to-astro/from-jekyll.mdx)!


---

**Navigation:** [← Previous](./06-add-integrations.md) | [Index](./index.md) | [Next →](./08-migrating-from-nextjs.md)
