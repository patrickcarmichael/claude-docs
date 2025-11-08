**Navigation:** [← Previous](./09-testing.md) | [Index](./index.md) | [Next →](./11-create-a-dev-toolbar-app.md)

---

# Upgrade to Astro v5

> How to upgrade your project to Astro v5.0.

This guide will help you migrate from Astro v4 to Astro v5.

Need to upgrade an older project to v4 first? See our [older migration guide](/en/guides/upgrade-to/v4/).

Need to see the v4 docs? Visit this [older version of the docs site (unmaintained v4.16 snapshot)](https://v4.docs.astro.build/).

## Upgrade Astro

[Section titled “Upgrade Astro”](#upgrade-astro)

Update your project’s version of Astro to the latest version using your package manager:

* npm

  ```shell
  # Upgrade Astro and official integrations together
  npx @astrojs/upgrade
  ```

* pnpm

  ```shell
  # Upgrade Astro and official integrations together
  pnpm dlx @astrojs/upgrade
  ```

* Yarn

  ```shell
  # Upgrade Astro and official integrations together
  yarn dlx @astrojs/upgrade
  ```

You can also [upgrade your Astro integrations manually](/en/guides/integrations-guide/#manual-upgrading) if needed, and you may also need to upgrade other dependencies in your project.

Need to continue?

After upgrading Astro, you may not need to make any changes to your project at all!

But, if you notice errors or unexpected behavior, please check below for what has changed that might need updating in your project.

Astro v5.0 includes [potentially breaking changes](#breaking-changes), as well as the removal and deprecation of some features.

If your project doesn’t work as expected after upgrading to v5.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See [the Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for full release notes.

## Dependency Upgrades

[Section titled “Dependency Upgrades”](#dependency-upgrades)

Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Vite 6.0

[Section titled “Vite 6.0”](#vite-60)

Astro v5.0 upgrades to Vite v6.0 as the development server and production bundler.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do)

If you are using Vite-specific plugins, configuration, or APIs, check the [Vite migration guide](https://vite.dev/guide/migration.html) for their breaking changes and upgrade your project as needed.

### `@astrojs/mdx`

[Section titled “@astrojs/mdx”](#astrojsmdx)

[Implementation PR: Cleanup unused JSX code (#11741)](https://github.com/withastro/astro/pull/11741)

In Astro v4.x, Astro performed internal JSX handling for the `@astrojs/mdx` integration.

Astro v5.0 moves this responsibility to handle and render JSX and MDX to the `@astrojs/mdx` package directly. This means that Astro 5.0 is no longer compatible with older versions of the MDX integration.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-1)

If your project includes `.mdx` files, you must upgrade `@astrojs/mdx` to the latest version (v4.0.0) so that your JSX can be handled properly by the integration.

If you are using an MDX server renderer with the experimental [Astro Container API](/en/reference/container-reference/) you must update the import to reflect the new location:

```diff
-import mdxRenderer from "astro/jsx/server.js";
+import mdxRenderer from "@astrojs/mdx/server.js";
```

Learn more about [using MDX in your project](/en/guides/integrations-guide/mdx/).

## Legacy

[Section titled “Legacy”](#legacy)

The following features are now considered legacy features. They should function normally but are no longer recommended and are in maintenance mode. They will see no future improvements and documentation will not be updated. These features will eventually be deprecated, and then removed entirely.

### Legacy: v2.0 Content Collections API

[Section titled “Legacy: v2.0 Content Collections API”](#legacy-v20-content-collections-api)

In Astro 4.x, content collections were defined, queried, and rendered using [the Content Collections API first introduced in Astro v2.0](https://astro.build/blog/introducing-content-collections/). All collection entries were local files within the reserved `src/content/` folder. Additionally, Astro’s [file name convention to exclude building individual pages](/en/guides/routing/#excluding-pages) was built in to the Content Collections API.

Astro 5.0 introduces a new version of content collections using the Content Layer API which brings several performance improvements and added capabilities. While old (legacy) and new (Content Layer API) collections can continue exist together in this release, there are potentially breaking changes to existing legacy collections.

This release also removes the option to prefix collection entry file names with an underscore (`_`) to prevent building a route.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-2)

We recommend [converting any existing collections to the new Content Layer API](#updating-existing-collections) as soon as you are able and making any new collections using the Content Layer API.

If you are unable to convert your collections, then please consult the [legacy collections breaking changes](#breaking-changes-to-legacy-content-and-data-collections) to see whether your existing collections are affected and require updating.

If you are unable to make any changes to your collections at this time, you can [enable the `legacy.collections` flag](#enabling-the-legacycollections-flag) which will allow you to keep your collections in their current state until the legacy flag is no longer supported.

Learn more about the updated [content collections](/en/guides/content-collections/).

##### Updating existing collections

[Section titled “Updating existing collections”](#updating-existing-collections)

See the instructions below for updating an existing content collection (`type: 'content'` or `type: 'data'`) to use the Content Layer API.

Step-by-step instructions to update a collection

1. **Move the content config file**. This file no longer lives within the `src/content/` folder. This file should now exist at `src/content.config.ts`.

2. **Edit the collection definition**. Your updated collection requires a `loader` which indicates both a folder for the location of your collection (`base`) and a `pattern` defining the collection entry filenames and extensions to match. (You may need to update the example below accordingly. You can use [globster.xyz](https://globster.xyz/) to check your glob pattern.) The option to select a collection `type` is no longer available.

   src/content.config.ts

   ```diff
   import { defineCollection, z } from 'astro:content';
   +import { glob } from 'astro/loaders';


   const blog = defineCollection({
     // For content layer you no longer define a `type`
     type: 'content',
     loader: glob({ pattern: '**/[^_]*.{md,mdx}', base: "./src/data/blog" }),
     schema: z.object({
       title: z.string(),
       description: z.string(),
       pubDate: z.coerce.date(),
       updatedDate: z.coerce.date().optional(),
     }),
   });
   ```

3. **Change references from `slug` to `id`**. Content layer collections do not have a reserved `slug` field. Instead, all updated collections will have an `id`:

   src/pages/\[slug].astro

   ```diff
   ---
   export async function getStaticPaths() {
     const posts = await getCollection('blog');
     return posts.map((post) => ({
   -    params: { slug: post.slug },
   +    params: { slug: post.id },
       props: post,
     }));
   }
   ---
   ```

   You can also update the dynamic routing file names to match the value of the changed `getStaticPaths()` parameter.

4. **Switch to the new `render()` function**. Entries no longer have a `render()` method, as they are now serializable plain objects. Instead, import the `render()` function from `astro:content`.

   src/pages/index.astro

   ```diff
   ---
   import { getEntry, render } from 'astro:content';


   const post = await getEntry('blog', params.slug);


   -const { Content, headings } = await post.render();
   +const { Content, headings } = await render(post);
   ---
   <Content />
   ```

##### Breaking changes to legacy `content` and `data` collections

[Section titled “Breaking changes to legacy content and data collections”](#breaking-changes-to-legacy-content-and-data-collections)

[Implementation PR: Implement legacy collections using glob (#11976)](https://github.com/withastro/astro/pull/11976)

By default, collections that use the old `type` property (`content` or `data`) and do not define a `loader` are now implemented under the hood using the Content Layer API’s built-in `glob()` loader, with extra backward-compatibility handling.

Additionally, temporary backwards compatibility exists for keeping the content config file in its original location of `src/content/config.ts`.

This backwards compatibility implementation is able to emulate most of the features of legacy collections and will allow many legacy collections to continue to work even without updating your code. However, **there are some differences and limitations that may cause breaking changes to existing collections**:

* In previous versions of Astro, collections would be generated for all folders in `src/content/`, even if they were not defined in `src/content/config.ts`. This behavior is now deprecated, and collections should always be defined in `src/content.config.ts`. For existing collections, these can just be empty declarations (e.g. `const blog = defineCollection({})`) and Astro will implicitly define your legacy collection for you in a way that is compatible with the new loading behavior.
* The special `layout` field is not supported in Markdown collection entries. This property is intended only for standalone page files located in `src/pages/` and not likely to be in your collection entries. However, if you were using this property, you must now create dynamic routes that include your page styling.
* Sort order of generated collections is non-deterministic and platform-dependent. This means that if you are calling `getCollection()`, the order in which entries are returned may be different than before. If you need a specific order, you must sort the collection entries yourself.
* `image().refine()` is not supported. If you need to validate the properties of an image you will need to do this at runtime in your page or component.
* The `key` argument of `getEntry(collection, key)` is typed as `string`, rather than having types for every entry.
* Previously when calling `getEntry(collection, key)` with a static string as the key, the return type was not nullable. The type now includes `undefined` so you must check if the entry is defined before using the result or you will have type errors.

##### Enabling the `legacy.collections` flag

[Section titled “Enabling the legacy.collections flag”](#enabling-the-legacycollections-flag)

[Implementation PR: Implement legacy collections using glob (#11976)](https://github.com/withastro/astro/pull/11976)

If you are not yet ready to update your existing collections, you can enable the [`legacy.collections`](/en/reference/legacy-flags/) flag and your existing collections will continue to function as before.

## Deprecated

[Section titled “Deprecated”](#deprecated)

The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `Astro.glob()`

[Section titled “Deprecated: Astro.glob()”](#deprecated-astroglob)

[Implementation PR: Deprecate glob (#11826)](https://github.com/withastro/astro/pull/11826)

In Astro v4.x, you could use `Astro.glob()` in your `.astro` components to query multiple files in your project. This had some limitations (where it could be used, performance, etc.), and using querying functions from the Content Collections API or Vite’s own `import.meta.glob()` often provided more function and flexibility.

Astro 5.0 deprecates `Astro.glob()` in favor of using `getCollection()` to query your collections, and `import.meta.glob()` to query other source files in your project.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-3)

Replace all use of `Astro.glob()` with `import.meta.glob()`. Note that `import.meta.glob()` no longer returns a `Promise`, so you may have to update your code accordingly. You should not require any updates to your [glob patterns](/en/guides/imports/#glob-patterns).

src/pages/blog.astro

```diff
---
-const posts = await Astro.glob('./posts/*.md');
+const posts = Object.values(import.meta.glob('./posts/*.md', { eager: true }));
---


{posts.map((post) => <li><a href={post.url}>{post.frontmatter.title}</a></li>)}
```

Where appropriate, consider using [content collections](/en/guides/content-collections/) to organize your content, which has its own newer, more performant querying functions.

You may also wish to consider using glob packages from NPM, such as [`fast-glob`](https://www.npmjs.com/package/fast-glob).

Learn more about [importing files with `import.meta.glob`](/en/guides/imports/#importmetaglob).

### Deprecated: `functionPerRoute` (Adapter API)

[Section titled “Deprecated: functionPerRoute (Adapter API)”](#deprecated-functionperroute-adapter-api)

[Implementation PR: Remove functionPerRoute option (#11714)](https://github.com/withastro/astro/pull/11714)

In Astro v4.x, you could opt into creating a separate file for each route defined in the project, mirroring your `src/pages/` directory in the build folder. By default, Astro emitted a single `entry.mjs` file, which was responsible for emitting the rendered page on each request.

Astro v5.0 removes the option to opt out of the default behavior. This behavior is now standard, and non-configurable.

Remove the `functionPerRoute` property from your `adapterFeatures` configuration. It is no longer available.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@matthewp/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@matthewp/my-adapter',
          serverEntrypoint: '@matthewp/my-adapter/server.js',
          adapterFeatures: {
-              functionPerRoute: true
          }
        });
      },
    },
  };
}
```

Learn more about [the Adapter API](/en/reference/adapter-reference/) for building adapter integrations.

### Deprecated: `routes` on `astro:build:done` hook (Integration API)

[Section titled “Deprecated: routes on astro:build:done hook (Integration API)”](#deprecated-routes-on-astrobuilddone-hook-integration-api)

[Implementation PR: feat(next): astro:routes:resolved (#12329)](https://github.com/withastro/astro/pull/12329)

In Astro v4.x, integrations accessed routes from the `astro:build:done` hook.

Astro v5.0 deprecates the `routes` array passed to this hook. Instead, it exposes a new `astro:routes:resolved` hook that runs before `astro:config:done`, and whenever a route changes in development. It has all the same properties of the deprecated `routes` list, except `distURL` which is only available during build.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-4)

Remove any instance of `routes` passed to `astro:build:done` and replace it with the new `astro:routes:resolved` hook. Access `distURL` on the newly exposed `assets` map:

my-integration.mjs

```diff
const integration = () => {
    let routes
    return {
        name: 'my-integration',
        hooks: {
            +'astro:routes:resolved': (params) => {
                +routes = params.routes
            },
            'astro:build:done': ({
                -routes
                +assets
            }) => {
                for (const route of routes) {
                    const distURL = assets.get(route.pattern)
                    if (distURL) {
                        +Object.assign(route, { distURL })
                    }
                }
                console.log(routes)
            }
        }
    }
}
```

Learn more about [the Integration API `astro:routes:resolved` hook](/en/reference/integrations-reference/#astroroutesresolved) for building integrations.

## Removed

[Section titled “Removed”](#removed)

The following features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: The Lit integration

[Section titled “Removed: The Lit integration”](#removed-the-lit-integration)

[Implementation PR: Remove \`@astrojs/lit\` (#11680)](https://github.com/withastro/astro/pull/11680)

In Astro v4.x, [Lit](https://lit.dev/) was a core-maintained framework library through the `@astrojs/lit` package.

Astro v5.0 removes the integration and it will not receive further updates for compatibility with 5.x and above.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-5)

You can continue to use Lit for client components by adding a client-side script tag. For example:

```astro
<script>
  import "../components/MyTabs";
</script>


<my-tabs title="These are my tabs">...</my-tabs>
```

If you’re interested in maintaining a Lit integration yourself, you may wish to use the [last published version of `@astrojs/lit`](https://github.com/withastro/astro/tree/astro%404.13.0/packages/integrations/lit) as a starting point and upgrade the relevant packages.

Learn more about [Astro’s official integrations](/en/guides/integrations-guide/).

### Removed: `hybrid` rendering mode

[Section titled “Removed: hybrid rendering mode”](#removed-hybrid-rendering-mode)

[Implementation PR: Merge output:hybrid and output:static (#11824)](https://github.com/withastro/astro/pull/11824)

In Astro v4.x, Astro provided three rendering `output` rendering modes: `'static'`, `'hybrid'`, and `'server'`

Astro v5.0 merges the `output: 'hybrid'` and `output: 'static'` configurations into one single configuration (now called `'static'`) that works the same way as the previous hybrid option.

It is no longer necessary to specify `output: 'hybrid'` in your Astro config to use server-rendered pages. The new `output: 'static'` has this capability included.

Astro will now automatically allow you to opt out of prerendering in your static site with no change to your output configuration required. Any page route or endpoint can include `export const prerender = false` to be server-rendered on demand, while the rest of your site is statically generated.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-6)

If your project used hybrid rendering, you must now remove the `output: 'hybrid'` option from your Astro config as it no longer exists. However, no other changes to your project are required, and you should have no breaking changes. The previous `'hybrid'` behavior is now the default, under a new name `'static'`.

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
-  output: 'hybrid',
});
```

If you were using the `output: 'static'` (default) option, you can continue to use it as before. By default, all of your pages will continue to be prerendered and you will have a completely static site. You should have no breaking changes to your project.

An adapter is still required to deploy an Astro project with any server-rendered pages, no matter which `output` mode your project uses. Failure to include an adapter will result in a warning in development and an error at build time.

Learn more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).

### Removed: support for dynamic `prerender` values in routes

[Section titled “Removed: support for dynamic prerender values in routes”](#removed-support-for-dynamic-prerender-values-in-routes)

[Implementation PR: Merge output:hybrid and output:static (#11824)](https://github.com/withastro/astro/pull/11824)

In Astro 4.x, environment variables could be used to dynamically set the value of `prerender` exports in routes, for example `export const prerender = import.meta.env.SOME_VAR`.

Astro v5.0 removes support for dynamic values in `prerender` exports. Only the static values `true` and `false` are supported.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-7)

1. Remove any dynamic `prerender` exports in your routes:

   src/pages/blog/\[slug].astro

   ```diff
   ---
   -export const prerender = import.meta.env.SOME_VAR;
   ---
   ```

2. Use an Astro integration in your `astro.config.mjs` file to set `prerender` values that need to be dynamic in the `"astro:route:setup"` hook:

   astro.config.mjs

   ```js
   import { defineConfig } from 'astro/config';
   import { loadEnv } from 'vite';


   export default defineConfig({
     integrations: [
       {
         name: 'set-prerender',
         hooks: {
           'astro:route:setup': ({ route }) => {
             // Load environment variables from .env files (if needed)
             const { PRERENDER } = loadEnv(process.env.NODE_ENV, process.cwd(), '');
             // Find routes matching the expected filename.
             if (route.component.endsWith('/blog/[slug].astro')) {
               // Set the prerender value on routes as needed.
               route.prerender = PRERENDER;
             }
           },
         },
       }
     ],
   });
   ```

### Removed: Squoosh image service

[Section titled “Removed: Squoosh image service”](#removed-squoosh-image-service)

[Implementation PR: remove the squoosh image service (#11770)](https://github.com/withastro/astro/pull/11770)

In Astro 4.x, you could configure `image.service: squooshImageService()` to use Squoosh to transform your images instead of Sharp. However, the underlying library `libsquoosh` is no longer maintained and has memory and performance issues.

Astro 5.0 removes the Squoosh image optimization service entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-8)

To switch to the built-in Sharp image service, remove the `squooshImageService` import from your Astro config. By default, you will use Sharp for `astro:assets`.

astro.config.mjs

```diff
-import { squooshImageService } from "astro/config";
import { defineConfig } from "astro/config";


export default defineConfig({
- image: {
-   service: squooshImageService()
- }
});
```

If you are using a strict package manager like `pnpm`, you may need to install the `sharp` package manually to use the Sharp image service, even though it is built into Astro by default.

If your adapter does not support Astro’s built-in Sharp image optimization, you can [configure a no-op image service](/en/guides/images/#configure-no-op-passthrough-service) to allow you to use the `<Image />` and `<Picture />` components.

Alternatively, you may wish to consider [a community-maintained Squoosh image service](https://github.com/Princesseuh/astro-image-service-squoosh) if you are unable to use the Sharp image service.

##### For adapters

[Section titled “For adapters”](#for-adapters)

If your adapter previously precised its compatibility status with Squoosh, you should now remove this information from your adapter configuration.

my-adapter.mjs

```diff
supportedAstroFeatures: {
-  assets: {
-    isSquooshCompatible: true
-  }
}
```

Read more about [configuring your default image service](/en/guides/images/#default-image-service).

### Removed: some public-facing types

[Section titled “Removed: some public-facing types”](#removed-some-public-facing-types)

[Implementation PR: Refactor/types (#11715)](https://github.com/withastro/astro/pull/11715)

In Astro v4.x, `@types/astro.ts` exposed all types publicly to users, whether or not they were still actively used or only intended for internal use.

Astro v5.0 refactors this file to remove outdated and internal types. This refactor brings improvements to your editor (e.g. faster completions, lower memory usage, and more relevant completion options). However, this refactor may cause errors in some projects that have been relying on types that are no longer available to the public.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-9)

Remove any types that now cause errors in your project as you no longer have access to them. These are mostly APIs that have previously been deprecated and removed, but may also include types that are now internal.

See the [public types exposed for use](https://github.com/withastro/astro/tree/main/packages/astro/src/types/public).

### Experimental Flags

[Section titled “Experimental Flags”](#experimental-flags)

The following experimental flags have been removed in Astro v5.0 and these features are available for use:

* `env`
* `serverIslands`

Additionally, the following experimental flags have been removed and **are now the default or recommended behavior in Astro v5.0**.

* `directRenderScript` (See below for breaking changes to [default `<script>` behavior](#script-tags-are-rendered-directly-as-declared).)
* `globalRoutePriority` (See below for breaking changes to [default route priority order](#route-priority-order-for-injected-routes-and-redirects).)
* `contentLayer` (See guidance for [upgrading existing content collections](#legacy-v20-content-collections-api) to the new, preferred Content Layer API.)

The following experimental flags have been removed and **their corresponding features are not part of Astro v5.0**.

* `contentCollectionsCache`

Remove these experimental flags if you were previously using them, and move your `env` configuration to the root of your Astro config:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
-    directRenderScript: true,
-    globalRoutePriority: true,
-    contentLayer: true,
-    serverIslands: true,
-    contentCollectionsCache: true,
-    env: {
-      schema: {...}
-    }
  },
+  env: {
+      schema: {...}
+  }
})
```

These features are all available by default in Astro v5.0.

Read about these exciting features and more in [the v5.0 Blog post](https://astro.build/blog/astro-5/).

## Changed Defaults

[Section titled “Changed Defaults”](#changed-defaults)

Some default behavior has changed in Astro v5.0 and your project code may need updating to account for these changes.

In most cases, the only action needed is to review your existing project’s deployment and ensure that it continues to function as you expect, making updates to your code as necessary. In some cases, there may be a configuration setting to allow you to continue to use the previous default behavior.

### CSRF protection is now set by default

[Section titled “CSRF protection is now set by default”](#csrf-protection-is-now-set-by-default)

[Implementation PR: change default value of checkOrigin (#11788)](https://github.com/withastro/astro/pull/11788)

In Astro v4.x, The default value of `security.checkOrigin` was `false`. Previously, you had to explicitly set this value to `true` to enable Cross-Site Request Forgery (CSRF) protection.

Astro v5.0 changes the default value of this option to `true`, and will automatically check that the “origin” header matches the URL sent by each request in on-demand rendered pages.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-10)

If you had previously configured `security.checkOrigin: true`, you no longer need this line in your Astro config. This is now the default.

To disable this behavior, you must explicitly set `security.checkOrigin: false`.

astro.config.mjs

```diff
export default defineConfig({
  output: "server",
+  security: {
+    checkOrigin: false
+  }
})
```

Read more about [security configuration options](/en/reference/configuration-reference/#security)

### Route priority order for injected routes and redirects

[Section titled “Route priority order for injected routes and redirects”](#route-priority-order-for-injected-routes-and-redirects)

[Implementation PR: Remove legacy route prioritization (#11798)](https://github.com/withastro/astro/pull/11798)

In Astro v4.x, `experimental.globalRoutePriority` was an optional flag that ensured that injected routes, file-based routes, and redirects were all prioritized using the [route priority order rules for all routes](/en/guides/routing/#route-priority-order). This allowed more control over routing in your project by not automatically prioritizing certain kinds of routes and standardizing the route priority order.

Astro v5.0 removes this experimental flag and makes this the new default behavior in Astro: redirects and injected routes are now prioritized equally alongside file-based project routes.

Note that this was already the default behavior in Starlight, and should not affect updated Starlight projects.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-11)

If your project includes injected routes or redirects, please check that your routes are building page URLs as expected. An example of the new expected behavior is shown below.

In a project containing the following routes:

* File-based route: `/blog/post/[pid]`
* File-based route: `/[page]`
* Injected route: `/blog/[...slug]`
* Redirect: `/blog/tags/[tag] -> /[tag]`
* Redirect: `/posts -> /blog`

The following URLs will be built (instead of following the route priority order of Astro v4.x):

* `/blog/tags/astro` is built by the redirect to `/tags/[tag]` (instead of the injected route `/blog/[...slug]`)
* `/blog/post/0` is built by the file-based route `/blog/post/[pid]` (instead of the injected route `/blog/[...slug]`)
* `/posts` is built by the redirect to `/blog` (instead of the file-based route `/[page]`)

In the event of route collisions, where two routes of equal route priority attempt to build the same URL, Astro will log a warning identifying the conflicting routes.

Read more about the [route priority order rules](/en/guides/routing/#route-priority-order).

### `<script>` tags are rendered directly as declared

[Section titled “\<script> tags are rendered directly as declared”](#script-tags-are-rendered-directly-as-declared)

[Implementation PR: Make directRenderScript the default (#11791)](https://github.com/withastro/astro/pull/11791)

In Astro v4.x, `experimental.directRenderScript` was an optional flag to directly render `<scripts>` as declared in `.astro` files (including existing features like TypeScript, importing `node_modules`, and deduplicating scripts). This strategy prevented scripts from being executed in places where they were not used. Additionally, conditionally rendered scripts were previously implicitly inlined, as if an `is:inline` directive was automatically added to them.

Astro 5.0 removes this experimental flag and makes this the new default behavior in Astro: scripts are no longer hoisted to the `<head>`, multiple scripts on a page are no longer bundled together, and a `<script>` tag may interfere with CSS styling. Additionally, conditionally rendered scripts are no longer implicitly inlined.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-12)

Please review your `<script>` tags and ensure they behave as desired.

If you previously had conditionally rendered `<script>` tags, you will need to add an `is:inline` attribute to preserve the same behavior as before:

src/components/MyComponent.astro

```astro
---
type Props = {
  showAlert: boolean
}


const { showAlert } = Astro.props;
---
{
  showAlert && <script is:inline>alert("Some very important code!!")</script>
}
```

Read more about [using `script` tags in Astro](/en/guides/client-side-scripts/).

## Breaking Changes

[Section titled “Breaking Changes”](#breaking-changes)

The following changes are considered breaking changes in Astro v5.0. Breaking changes may or may not provide temporary backwards compatibility. If you were using these features, you may have to update your code as recommended in each entry.

### Renamed: `<ViewTransitions />` component

[Section titled “Renamed: \<ViewTransitions /> component”](#renamed-viewtransitions--component)

[Implementation PR: Rename the ViewTransitions component to ClientRouter (#11980)](https://github.com/withastro/astro/pull/11980)

In Astro 4.x, Astro’s View Transitions API included a `<ViewTransitions />` router component to enable client-side routing, page transitions, and more.

Astro 5.0 renames this component to `<ClientRouter />` to clarify the role of the component within the API. This makes it more clear that the features you get from Astro’s `<ClientRouter />` routing component are slightly different from the native CSS-based MPA router.

No functionality has changed. This component has only changed its name.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-13)

Replace all occurrences of the `ViewTransitions` import and component with `ClientRouter`:

src/layouts/MyLayout.astro

```diff
-import { ViewTransitions } from 'astro:transitions';
+import { ClientRouter } from 'astro:transitions';


<html>
  <head>
    ...
   -<ViewTransitions />
   +<ClientRouter />
  </head>
</html>
```

Read more about [view transitions and client-side routing in Astro](/en/guides/view-transitions/).

### Changed: TypeScript configuration

[Section titled “Changed: TypeScript configuration”](#changed-typescript-configuration)

[Implementation PR: better tsconfig (#11859)](https://github.com/withastro/astro/pull/11859)

In Astro v4.x, Astro relied on a `src/env.d.ts` file for type inferencing and defining modules for features that relied on generated types.

Astro 5.0 instead uses a `.astro/types.d.ts` file for type inferencing, and now recommends setting `include` and `exclude` in `tsconfig.json` to benefit from Astro types and avoid checking built files.

Running `astro sync` no longer creates, nor updates, `src/env.d.ts` as it is not required for type-checking standard Astro projects.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-14)

To update your project to Astro’s recommended TypeScript settings, add the following `include` and `exclude` properties to your existing `tsconfig.json`:

tsconfig.json

```diff
{
  "extends": "astro/tsconfigs/base",
  +"include": [".astro/types.d.ts", "**/*"],
  +"exclude": ["dist"]
}
```

Note that `src/env.d.ts` is only necessary if you have added custom configurations, or if you’re not using a `tsconfig.json` file.

Read more about [TypeScript configuration in Astro](/en/guides/typescript/#setup).

### Changed: Actions submitted by HTML forms no longer use cookie redirects

[Section titled “Changed: Actions submitted by HTML forms no longer use cookie redirects”](#changed-actions-submitted-by-html-forms-no-longer-use-cookie-redirects)

[Implementation PR: Actions middleware (#12373)](https://github.com/withastro/astro/pull/12373)

In Astro 4.x, actions called from an HTML form would trigger a redirect with the result forwarded using cookies. This caused issues for large form errors and return values that exceeded the 4 KB limit of cookie-based storage.

Astro 5.0 now renders the result of an action as a POST result without any forwarding. This will introduce a “confirm form resubmission?” dialog when a user attempts to refresh the page, though it no longer imposes a 4 KB limit on action return value.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-15)

You should update handling for action results that relies on redirects, and optionally address the “confirm form resubmission?” dialog with middleware.

##### To redirect to the previous route on error

[Section titled “To redirect to the previous route on error”](#to-redirect-to-the-previous-route-on-error)

If your HTML form action is directed to a different route (i.e. `action={"/success-page" + actions.name}`), Astro will no longer redirect to the previous route on error. You can implement this behavior manually using redirects from your Astro component. This example instead redirects to a new route on success, and handles errors on the current page otherwise:

src/pages/newsletter.astro

```diff
---
import { actions } from 'astro:actions';


+const result = Astro.getActionResult(actions.newsletter);
+if (!result?.error) {
  +// Embed relevant result data in the URL if needed
  +// example: redirect(`/confirmation?email=${result.data.email}`);
  +return redirect('/confirmation');
+}
---


<form method="POST" action={'/confirmation' + actions.newsletter}>
  <label>E-mail <input required type="email" name="email" /></label>
  <button>Sign up</button>
</form>
```

##### (Optional) To remove the confirm dialog on refresh

[Section titled “(Optional) To remove the confirm dialog on refresh”](#optional-to-remove-the-confirm-dialog-on-refresh)

To address the “confirm form resubmission?” dialog on refresh, or to preserve action results across sessions, you can now [customize action result handling from middleware](/en/guides/actions/#advanced-persist-action-results-with-a-session).

We recommend using a session storage provider [as described in our Netlify Blob example](/en/guides/actions/#advanced-persist-action-results-with-a-session). However, if you prefer the cookie forwarding behavior from 4.X and accept the 4 KB size limit, you can implement the pattern as shown in this sample snippet:

src/middleware.ts

```ts
import { defineMiddleware } from 'astro:middleware';
import { getActionContext } from 'astro:actions';


export const onRequest = defineMiddleware(async (context, next) => {
  // Skip requests for prerendered pages
  if (context.isPrerendered) return next();


  const { action, setActionResult, serializeActionResult } = getActionContext(context);


  // If an action result was forwarded as a cookie, set the result
  // to be accessible from `Astro.getActionResult()`
  const payload = context.cookies.get('ACTION_PAYLOAD');
  if (payload) {
    const { actionName, actionResult } = payload.json();
    setActionResult(actionName, actionResult);
    context.cookies.delete('ACTION_PAYLOAD', { path: '/' });
    return next();
  }


  // If an action was called from an HTML form action,
  // call the action handler and redirect with the result as a cookie.
  if (action?.calledFrom === 'form') {
    const actionResult = await action.handler();


    context.cookies.set('ACTION_PAYLOAD', {
      actionName: action.name,
      actionResult: serializeActionResult(actionResult),
    }, {
      path: '/',
      httpOnly: true,
      sameSite: 'lax',
      maxAge: 60
    });


    if (actionResult.error) {
    // Redirect back to the previous page on error
      const referer = context.request.headers.get('Referer');
      if (!referer) {
        throw new Error('Internal: Referer unexpectedly missing from Action POST request.');
      }
      return context.redirect(referer);
    }
    // Redirect to the destination page on success
    return context.redirect(context.originPathname);
  }


  return next();
})
```

### Changed: `compiledContent()` is now an async function

[Section titled “Changed: compiledContent() is now an async function”](#changed-compiledcontent-is-now-an-async-function)

[Implementation PR: Remove TLA by making compiledContent async (#11782)](https://github.com/withastro/astro/pull/11782)

In Astro 4.x, top level await was included in Markdown modules. This caused some issues with custom image services and images inside Markdown, causing Node to suddenly exit with no error message.

Astro 5.0 makes the `compiledContent()` property on Markdown import an async function, requiring an `await` to resolve the content.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-16)

Update your code to use `await` when calling `compiledContent()`.

src/pages/post.astro

```diff
---
import * as myPost from "../blog/post.md";


-const content = myPost.compiledContent();
+const content = await myPost.compiledContent();
---


<Fragment set:html={content} />
```

Read more about the [`compiledContent()` function](/en/guides/markdown-content/#importing-markdown) for returning compiled Markdown.

### Changed: `astro:content` can no longer be used on the client

[Section titled “Changed: astro:content can no longer be used on the client”](#changed-astrocontent-can-no-longer-be-used-on-the-client)

[Implementation PR: Prevent usage of \`astro:content\` in the client (#11827)](https://github.com/withastro/astro/pull/11827)

In Astro 4.x, it was possible to access the `astro:content` module on the client.

Astro 5.0 removes this access as it was never intentionally exposed for client use. Using `astro:content` this way had limitations and bloated client bundles.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-17)

If you are currently using `astro:content` in the client, pass the data you need through props to your client components instead:

src/pages/blog.astro

```astro
---
import { getCollection } from 'astro:content';
import ClientComponent from '../components/ClientComponent';


const posts = await getCollection('blog');
const postsData = posts.map(post => post.data);
---


<ClientComponent posts={postsData} />
```

Read more about [the `astro:content` API](/en/reference/modules/astro-content/).

### Renamed: Shiki `css-variables` theme color token names

[Section titled “Renamed: Shiki css-variables theme color token names”](#renamed-shiki-css-variables-theme-color-token-names)

[Implementation PR: Update to new shiki token names (#11661)](https://github.com/withastro/astro/pull/11661)

In Astro v4.x, the Shiki `css-variables` theme used the `--astro-code-color-text` and `--astro-code-color-background` tokens for styling the foreground and background colors of code blocks respectively.

Astro v5.0 renames them to `--astro-code-foreground` and `--astro-code-background` respectively to better align with the Shiki v1 defaults.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-18)

You can perform a global find and replace in your project to migrate to the new token names.

src/styles/global.css

```diff
:root {
  ---astro-code-color-text: #000;
  ---astro-code-color-background: #fff;
  +--astro-code-foreground: #000;
  +--astro-code-background: #fff;
}
```

Read more about [syntax highlighting in Astro](/en/guides/syntax-highlighting/).

### Changed: internal Shiki rehype plugin for highlighting code blocks

[Section titled “Changed: internal Shiki rehype plugin for highlighting code blocks”](#changed-internal-shiki-rehype-plugin-for-highlighting-code-blocks)

[Implementation PR: Refactor createShikiHighlighter (#11825)](https://github.com/withastro/astro/pull/11825)

In Astro 4.x, Astro’s internal Shiki rehype plugin highlighted code blocks as HTML.

Astro 5.0 updates this plugin to highlight code blocks as hast. This allows a more direct Markdown and MDX processing and improves the performance when building the project. However, this may cause issues with existing Shiki transformers.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-19)

If you are using Shiki transformers passed to `markdown.shikiConfig.transformers`, you must make sure they do not use the `postprocess` hook. This hook no longer runs on code blocks in `.md` and `.mdx` files. (See [the Shiki documentation on transformer hooks](https://shiki.style/guide/transformers#transformer-hooks) for more information).

Code blocks in `.mdoc` files and Astro’s built-in `<Code />` component do not use the internal Shiki rehype plugin and are unaffected.

Read more about [syntax highlighting in Astro](/en/guides/syntax-highlighting/).

### Changed: Automatic `charset=utf-8` behavior for Markdown and MDX pages

[Section titled “Changed: Automatic charset=utf-8 behavior for Markdown and MDX pages”](#changed-automatic-charsetutf-8-behavior-for-markdown-and-mdx-pages)

[Implementation PR: Unset charset=utf-8 content-type for md/mdx pages (#12231)](https://github.com/withastro/astro/pull/12231)

In Astro 4.0, Markdown and MDX pages (located in `src/pages/`) automatically responded with `charset=utf-8` in the `Content-Type` header, which allowed rendering non-ASCII characters in your pages.

Astro 5.0 updates the behaviour to add the `<meta charset="utf-8">` tag instead, and only for pages that do not use Astro’s special `layout` frontmatter property. Similarly for MDX pages, Astro will only add the tag if the MDX content does not import a wrapping `Layout` component.

If your Markdown or MDX pages use the `layout` frontmatter property, or if the MDX page content imports a wrapping `Layout` component, then the HTML encoding will be handled by the designated layout component instead, and the `<meta charset="utf-8">` tag will not be added to your page by default.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-20)

If you require `charset=utf-8` to render your page correctly, make sure that your layout components contain the `<meta charset="utf-8">` tag. You may need to add this if you have not already done so.

Read more about [Markdown layouts](/en/basics/layouts/#markdown-layouts).

### Changed: Astro-specific metadata attached in remark and rehype plugins

[Section titled “Changed: Astro-specific metadata attached in remark and rehype plugins”](#changed-astro-specific-metadata-attached-in-remark-and-rehype-plugins)

[Implementation PR: Clean up Astro metadata in vfile.data (#11861)](https://github.com/withastro/astro/pull/11861)

In Astro 4.x, the Astro-specific metadata attached to `vfile.data` in remark and rehype plugins was attached in different locations with inconsistent names.

Astro 5 cleans up the API and the metadata is now renamed as below:

* `vfile.data.__astroHeadings` -> `vfile.data.astro.headings`
* `vfile.data.imagePaths` -> `vfile.data.astro.imagePaths`

The types of `imagePaths` has also been updated from `Set<string>` to `string[]`. The `vfile.data.astro.frontmatter` metadata is left unchanged.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-21)

While we don’t consider these APIs public, they can be accessed by remark and rehype plugins that want to re-use Astro’s metadata. If you are using these APIs, make sure to access them in the new locations.

Read more about [using Markdown plugins in Astro](/en/guides/markdown-content/#markdown-plugins).

### Changed: image endpoint configuration

[Section titled “Changed: image endpoint configuration”](#changed-image-endpoint-configuration)

[Implementation PR: Allow customising the route of the image endpoint (#11908)](https://github.com/withastro/astro/pull/11908)

In Astro 4.x, you could set an endpoint in your `image` configuration to use for image optimization.

Astro 5.0 allows you to customize a `route` and `entrypoint` of the `image.endpoint` config. This can be useful in niche situations where the default route `/_image` conflicts with an existing route or your local server setup.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-22)

If you had previously customized `image.endpoint`, move this endpoint to the new `endpoint.entrypoint` property. Optionally, you may customize a `route`:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


defineConfig({
  image: {
-    endpoint: './src/image-endpoint.ts',
+    endpoint: {
+      route: "/image",
+      entrypoint: "./src/image_endpoint.ts"
+    }
  },
})
```

Read more about [setting an endpoint to use for image optimization](/en/reference/configuration-reference/#imageendpoint).

### Changed: `build.client` and `build.server` resolve behavior

[Section titled “Changed: build.client and build.server resolve behavior”](#changed-buildclient-and-buildserver-resolve-behavior)

[Implementation PR: Fix build.client and build.server resolve behaviour (#11916)](https://github.com/withastro/astro/pull/11916)

In Astro v4.x, the `build.client` and `build.server` options were documented to resolve relatively from the `outDir` option, but it didn’t always work as expected.

Astro 5.0 fixes the behavior to correctly resolve from the `outDir` option. For example, if `outDir` is set to `./dist/nested/`, then by default:

* `build.client` will resolve to `<root>/dist/nested/client/`
* `build.server` will resolve to `<root>/dist/nested/server/`

Previously the values were incorrectly resolved:

* `build.client` was resolved to `<root>/dist/nested/dist/client/`
* `build.server` was resolved to `<root>/dist/nested/dist/server/`

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-23)

If you were relying on the previous build paths, make sure that your project code is updated to the new build paths.

Read more about [`build` configuration options in Astro](/en/reference/configuration-reference/#build-options).

### Changed: JS dependencies in config file are no longer processed by Vite

[Section titled “Changed: JS dependencies in config file are no longer processed by Vite”](#changed-js-dependencies-in-config-file-are-no-longer-processed-by-vite)

[Implementation PR: Set external: true when loading astro config (#11819)](https://github.com/withastro/astro/pull/11819)

In Astro 4.x, locally-linked JS dependencies (e.g. `npm link`, in a monorepo, etc) were able to use Vite features like `import.meta.glob` when imported by the Astro config file.

Astro 5 updates the Astro config loading flow to ignore processing locally-linked JS dependencies with Vite. Dependencies exporting raw TypeScript files are unaffected. Instead, these JS dependencies will be normally imported by the Node.js runtime the same way as other dependencies from `node_modules`.

This change was made as the previous behavior caused confusion among integration authors who tested against a package that worked locally, but not when published. It also restricted using CJS-only dependencies because Vite required the code to be ESM. While this change only affects JS dependencies, it’s also recommended for packages to export JavaScript instead of raw TypeScript where possible to prevent accidental Vite-specific usage as it’s an implementation detail of Astro’s config loading flow.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-24)

Make sure your locally-linked JS dependencies are built before running your Astro project. Then, the config loading should work as before.

Read more about [Vite configuration settings in Astro](/en/reference/configuration-reference/#vite).

### Changed: URLs returned by `paginate()`

[Section titled “Changed: URLs returned by paginate()”](#changed-urls-returned-by-paginate)

[Implementation PR: Add base to paginate (#11253)](https://github.com/withastro/astro/pull/11253)

In Astro v4.x, the URL returned by `paginate()` (e.g. `page.url.next`, `page.url.first`, etc.) did not include the value set for `base` in your Astro config. You had to manually prepend your configured value for `base` to the URL path.

Astro 5.0 automatically includes the `base` value in `page.url`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-25)

If you are using the `paginate()` function for these URLs, remove any existing `base` value as it is now added for you:

```diff
---
export async function getStaticPaths({ paginate }) {
  const astronautPages = [{
    astronaut: 'Neil Armstrong',
  }, {
    astronaut: 'Buzz Aldrin',
  }, {
    astronaut: 'Sally Ride',
  }, {
    astronaut: 'John Glenn',
  }];
  return paginate(astronautPages, { pageSize: 1 });
}
const { page } = Astro.props;
// `base: /'docs'` configured in `astro.config.mjs`
-const prev = "/docs" + page.url.prev;
+const prev = page.url.prev;
---
<a id="prev" href={prev}>Back</a>
```

Read more about [pagination in Astro](/en/guides/routing/#pagination).

### Changed: non-boolean HTML attribute values

[Section titled “Changed: non-boolean HTML attribute values”](#changed-non-boolean-html-attribute-values)

[Implementation PR: Fix attribute rendering for boolean values (take 2) (#11660)](https://github.com/withastro/astro/pull/11660)

In Astro v4.x, non-[boolean HTML attributes](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML) may not have included their values when rendered to HTML.

Astro v5.0 renders the values explicitly as `="true"` or `="false"`, matching proper attribute handling in browsers.

In the following `.astro` examples, only `allowfullscreen` is a boolean attribute:

src/pages/index.astro

```astro
<!-- `allowfullscreen` is a boolean attribute -->
<p allowfullscreen={true}></p>
<p allowfullscreen={false}></p>
<!-- `inherit` is *not* a boolean attribute -->
<p inherit={true}></p>
<p inherit={false}></p>
<!-- `data-*` attributes are not boolean attributes -->
<p data-light={true}></p>
<p data-light={false}></p>
```

Astro v5.0 now preserves the full data attribute with its value when rendering the HTML of non-boolean attributes:

```diff
<p allowfullscreen></p>
<p></p>


<p inherit="true"></p>
<p inherit></p>
<p inherit="false"></p>


<p data-light></p>
<p data-light="true"></p>
<p></p>
<p data-light="false"></p>
```

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-26)

If you rely on attribute values, for example, to locate elements or to conditionally render, update your code to match the new non-boolean attribute values:

```diff
-el.getAttribute('inherit') === ''
+el.getAttribute('inherit') === 'false'


-el.hasAttribute('data-light')
+el.dataset.light === 'true'
```

Read more about [using HTML attributes in Astro](/en/reference/astro-syntax/#dynamic-attributes).

### Changed: adding values to `context.locals`

[Section titled “Changed: adding values to context.locals”](#changed-adding-values-to-contextlocals)

[Implementation PR: TODOs (#11987)](https://github.com/withastro/astro/pull/11987)

In Astro 4.x, it was possible to completely replace the entire `locals` object in middleware, API endpoints, and pages when adding new values.

Astro 5.0 requires you to append values to the existing `locals` object without deleting it. Locals in middleware, API endpoints, and pages, can no longer be completely overridden.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-27)

Where you previously were overwriting the object, you must now instead assign values to it:

src/middleware.js

```diff
-ctx.locals = {
Object.assign(ctx.locals, {
  one: 1,
  two: 2
-}
+})
```

See more about [storing data in `context.locals`](/en/guides/middleware/#storing-data-in-contextlocals).

### Changed: `params` no longer decoded

[Section titled “Changed: params no longer decoded”](#changed-params-no-longer-decoded)

[Implementation PR: decode pathname early, don't decode params (#12079)](https://github.com/withastro/astro/pull/12079)

In Astro v4.x, `params` passed to `getStaticPath()` were automatically decoded using `decodeURIComponent`.

Astro v5.0 no longer decodes the value of `params` passed to `getStaticPaths`. You must manually decode them yourself if needed.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-28)

If you were previously relying on the automatic decoding, use `decodeURI` when passing `params`.

src/pages/\[id].astro

```diff
---
export function getStaticPaths() {
  return [
-    { params: { id: "%5Bpage%5D" } },
+    { params: { id: decodeURI("%5Bpage%5D") } },
  ]
}


const { id } = Astro.params;
---
```

Note that the use of [`decodeURIComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) is discouraged for `getStaticPaths` because it decodes more characters than it should, for example `/`, `?`, `#` and more.

Read more about [creating dynamic routes with `params`](/en/guides/routing/#static-ssg-mode).

### Changed: `RouteData` type replaced by `IntegrationsRouteData` (Integrations API)

[Section titled “Changed: RouteData type replaced by IntegrationsRouteData (Integrations API)”](#changed-routedata-type-replaced-by-integrationsroutedata-integrations-api)

[Implementation PR: send \`IntegrationRouteData\` to integrations (#11864)](https://github.com/withastro/astro/pull/11864)

In Astro v4.x, the `entryPoints` type inside the `astro:build:ssr` and `astro:build:done` hooks was `RouteData`.

Astro v5.0 the `entryPoints` type is now `IntegrationRouteData`, which contains a subset of the `RouteData` type. The fields `isIndex` and `fallbackRoutes` were removed.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-29)

Update your adapter to change the type of `entryPoints` from `RouteData` to `IntegrationRouteData`.

```diff
-import type {RouteData} from 'astro';
+import type {IntegrationRouteData} from "astro"


-function useRoute(route: RouteData) {
+function useRoute(route: IntegrationRouteData) {
}
```

See the [API reference for `IntegrationRouteData`](/en/reference/integrations-reference/#integrationroutedata-type-reference).

### Changed: `distURL` is now an array (Integrations API)

[Section titled “Changed: distURL is now an array (Integrations API)”](#changed-disturl-is-now-an-array-integrations-api)

[Implementation PR: send \`IntegrationRouteData\` to integrations (#11864)](https://github.com/withastro/astro/pull/11864)

In Astro v4.x, `RouteData.distURL` was `undefined` or a `URL`.

Astro v5.0 updates the shape of `IntegrationRouteData.distURL` to be `undefined` or an array of `URL`s. This fixes a previous error because a route can generate multiple files on disk, especially when using dynamic routes such as `[slug]` or `[...slug]`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-30)

Update your code to handle `IntegrationRouteData.distURL` as an array.

```diff
if (route.distURL) {
  -if (route.distURL.endsWith('index.html')) {
    -// do something
-  }
  +for (const url of route.distURL) {
    +if (url.endsWith('index.html')) {
      +// do something
+    }
+  }
}
```

See the [API reference for `IntegrationRouteData`](/en/reference/integrations-reference/#integrationroutedata-type-reference).

### Changed: Arguments passed to `app.render()` (Adapter API)

[Section titled “Changed: Arguments passed to app.render() (Adapter API)”](#changed-arguments-passed-to-apprender-adapter-api)

[Implementation PR: TODOs (#11987)](https://github.com/withastro/astro/pull/11987)

In Astro 4.x, The Adapter API method `app.render()` could receive three arguments: a mandatory `request`, an object of options or a `routeData` object, and `locals`.

Astro 5.0 combines these last two arguments into a single options argument named `renderOptions`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-31)

Pass an object as the second argument to `app.render()`, which can include `routeData` and `locals` as properties.

```diff
-const response = await app.render(request, routeData, locals);
+const response = await app.render(request, {routeData, locals});
```

See the [Adapter API reference for `renderOptions`](/en/reference/adapter-reference/#renderoptions).

### Changed: Properties on `supportedAstroFeatures` (Adapter API)

[Section titled “Changed: Properties on supportedAstroFeatures (Adapter API)”](#changed-properties-on-supportedastrofeatures-adapter-api)

[Implementation PR: rework supportedAstroFeatures (#11806)](https://github.com/withastro/astro/pull/11806)

In Astro 4.x, `supportedAstroFeatures`, which allows adapter authors to specify which features their integration supports, included an `assets` property to specify which of Astro’s image services were supported.

Astro 5.0 replaces this property with a dedicated `sharpImageService` property, used to determine whether the adapter is compatible with the built-in sharp image service.

v5.0 also adds a new `limited` value for the different properties of `supportedAstroFeatures` for adapters, which indicates that the adapter is compatible with the feature, but with some limitations. This is useful for adapters that support a feature, but not in all cases or with all options.

Additionally, the value of the different properties on `supportedAstroFeatures` for adapters can now be objects, with `support` and `message` properties. The content of the `message` property will show a helpful message in the Astro CLI when the adapter is not compatible with a feature. This is notably useful with the new `limited` value, to explain to the user why support is limited.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-32)

If you were using the `assets` property, remove this as it is no longer available. To specify that your adapter supports the built-in sharp image service, replace this with `sharpImageService`.

You may also wish to update your supported features with the new `limited` option and include a message about your adapter’s support.

my-adapter.mjs

```diff
supportedAstroFeatures: {
-  assets: {
-    supportKind: "stable",
-    isSharpCompatible: true,
-    isSquooshCompatible: true,
-  },
+  sharpImageService: {
+    support: "limited",
+    message: 'This adapter supports the built-in sharp image service, but with some limitations.'
+  }
}
```

Read more about [specifying supported Astro features in an adapter](/en/reference/adapter-reference/#astro-features).

### Removed: Deprecated definition shape for dev toolbar apps (Dev Toolbar API)

[Section titled “Removed: Deprecated definition shape for dev toolbar apps (Dev Toolbar API)”](#removed-deprecated-definition-shape-for-dev-toolbar-apps-dev-toolbar-api)

[Implementation PR: Remove deprecated dev toolbar app shape (#11987)](https://github.com/withastro/astro/pull/11987)

In Astro 4.x, when building a dev toolbar app, it was still possible to use the previously deprecated `addDevToolbarApp(string);` signature. The `id`, `title`, and `icon` properties to define the app were then made available through the default export of the app’s `entrypoint`.

Astro 5.0 completely removes this option entirely in favor of the current object shape when defining a dev toolbar app in an integration that’s more intuitive and allows Astro to provide better errors when toolbar apps fail to load correctly.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-33)

If you were using the deprecated shape, update your dev toolbar app to use the new shape:

my-integration.mjs

```diff
-// Old shape
-addDevToolbarApp("./my-dev-toolbar-app.mjs");


+// New shape
+addDevToolbarApp({
+  id: "my-app",
+  name: "My App",
+  icon: "<svg>...</svg>",
+  entrypoint: "./my-dev-toolbar-app.mjs",
+});
```

my-dev-toolbar-app.mjs

```diff
export default {
-  id: 'my-dev-toolbar-app',
-  title: 'My Dev Toolbar App',
-  icon: '🚀',
  init() {
    // ...
  }
}
```

Read more about [developing a dev toolbar app for Astro using the Dev Toolbar API](/en/reference/dev-toolbar-app-reference/).

### Removed: configuring Typescript during `create-astro`

[Section titled “Removed: configuring Typescript during create-astro”](#removed-configuring-typescript-during-create-astro)

[Implementation PR: create-astro updates (#12083)](https://github.com/withastro/astro/pull/12083)

In Astro v4.x, it was possible to choose between Astro’s three TypeScript settings when creating a new project using `create astro`, either by answering a question or by passing an associated `--typescript` flag with the desired TypeScript setting.

Astro 5.0 updates the `create astro` CLI command to remove the TypeScript question and its associated `--typescript` flag. The “strict” preset is now the default for all new projects created with the command line and it is no longer possible to customize this at that time. However, the TypeScript template can still be changed manually in `tsconfig.json`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-34)

If you were using the `--typescript` flag with `create-astro`, remove it from your command.

* npm

  ```diff
  -npm create astro@latest -- --template <example-name> --typescript strict
  +npm create astro@latest -- --template <example-name>
  ```

* pnpm

  ```diff
  -pnpm create astro@latest --template <example-name> --typescript strict
  +pnpm create astro@latest --template <example-name>
  ```

* Yarn

  ```diff
  -yarn create astro --template <example-name> --typescript strict
  +yarn create astro --template <example-name>
  ```

See [all the available `create astro` command flags](https://github.com/withastro/astro/blob/main/packages/create-astro/README.md)

## Community Resources

[Section titled “Community Resources”](#community-resources)

Know a good resource for Astro v5.0? [Edit this page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/upgrade-to/v5.mdx) and add a link below!

## Known Issues

[Section titled “Known Issues”](#known-issues)

Please check [Astro’s issues on GitHub](https://github.com/withastro/astro/issues/) for any reported issues, or to file an issue yourself.

# View transitions

> Enable seamless navigation between pages in Astro with view transitions.

[View transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) are animated transitions between different website views. They are a popular design choice for preserving visual continuity as visitors move between states or views of an application.

Astro’s view transitions and client-side routing support is powered by the [View Transitions browser API](https://developer.chrome.com/docs/web-platform/view-transitions/) and also includes:

* A few [built-in animation options](#built-in-animation-directives), such as `fade`, `slide`, and `none`.
* Support for both forwards and backwards navigation animations.
* The ability to fully [customize all aspects of transition animation](#customizing-animations), and build your own animations.
* A way to carry HTML elements from the current page to the next during navigation.
* The option to [prevent client-side navigation for non-page links](#preventing-client-side-navigation).
* [Control over fallback behavior](#fallback-control) for browsers that do not yet support the View Transition APIs.
* Automatic support for [`prefers-reduced-motion`](#prefers-reduced-motion).

Note

By default, every page will use regular, full-page, browser navigation. You must opt in to view transitions and can use them either on a per-page basis or site-wide.

## Differences between browser-native view transitions and Astro’s `<ClientRouter />`

[Section titled “Differences between browser-native view transitions and Astro’s \<ClientRouter />”](#differences-between-browser-native-view-transitions-and-astros-clientrouter-)

[Browser-native, cross-document view transitions](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#basic_mpa_view_transition) can be used in Astro to animate the navigation between documents in a multi-page app (MPA), often providing the experience of client-side routing of single-page applications. They don’t alter the core functionality of a multi-page application, nor do they affect any existing scripts or add additional JavaScript to your page load. They simply add animations.

For enhanced client-side routing and view transition features not yet fully supported by the View Transition API, Astro provides a built-in, lightweight component to enable client-side routing and turn your multi-page app into a [single-page app](#enabling-view-transitions-spa-mode) with smooth animations on navigation.

That comes with some benefits, like shared state across pages and persistent elements, and some drawbacks, such as needing to manually reinitialize scripts or state after navigation.

Adding Astro’s built-in `<ClientRouter />` component:

* [intercepts page navigation](#client-side-navigation-process) and gives you considerable control over this process.
* extends and enhances some View Transition/Navigation API features.
* allows you to [configure fallback strategies](#fallback-control) for when [native browser support is lacking](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API#browser_compatibility).

However, as browser APIs and web standards evolve, using Astro’s `<ClientRouter />` for this additional functionality [will increasingly become unnecessary](https://astro.build/blog/future-of-astro-zero-js-view-transitions/). We recommend keeping up with the current state of browser APIs so you can [decide whether you still need Astro’s client-side routing](https://events-3bg.pages.dev/jotter/astro-view-transitions/) for the specific features you use.

## Enabling view transitions (SPA mode)

[Section titled “Enabling view transitions (SPA mode)”](#enabling-view-transitions-spa-mode)

Import and add the `<ClientRouter />` component to your common `<head>` or shared layout component. Astro will create default page animations based on the similarities between the old and new page, and will also provide fallback behavior for unsupported browsers.

The example below shows adding Astro’s default page navigation animations site-wide, including the default fallback control option for non-supporting browsers, by importing and adding this component to a `<CommonHead />` Astro component:

src/components/CommonHead.astro

```diff
---
+import { ClientRouter } from "astro:transitions";
---
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<meta name="generator" content={Astro.generator} />


<!-- Primary Meta Tags -->
<title>{title}</title>
<meta name="title" content={title} />
<meta name="description" content={description} />


+<ClientRouter />
```

No other configuration is necessary to enable Astro’s default client-side navigation!

Use [transition directives](#transition-directives) or [override default client-side navigation](#preventing-client-side-navigation) on individual elements for finer control.

## Transition Directives

[Section titled “Transition Directives”](#transition-directives)

Astro will automatically assign corresponding elements found in both the old page and the new page a shared, unique `view-transition-name`. This pair of matching elements is inferred by both the type of element and its location in the DOM.

Use optional `transition:*` directives on page elements in your `.astro` components for finer control over the page transition behaviour during navigation.

* `transition:name`: Allows you to override Astro’s default element matching for old/new content animation and [specify a transition name](#naming-a-transition) to associate a pair of DOM elements.
* `transition:animate`: Allows you to override Astro’s default animation while replacing the old element with the new one by specifying an animation type. Use Astro’s [built-in animation directives](#built-in-animation-directives) or [create custom transition animations](#customizing-animations).
* `transition:persist`: Allows you to override Astro’s default replacing old elements for new ones and instead [persist components and HTML elements](#maintaining-state) when navigating to another page.

### Naming a transition

[Section titled “Naming a transition”](#naming-a-transition)

In some cases, you may want or need to identify the corresponding view transition elements yourself. You can specify a name for a pair of elements using the `transition:name` directive.

src/pages/old-page.astro

```astro
<aside transition:name="hero">
```

src/pages/new-page.astro

```astro
<aside transition:name="hero">
```

Note that the provided `transition:name` value can only be used once on each page. Set this manually when Astro can’t infer a proper name itself, or for more fine control over matching elements.

### Maintaining State

[Section titled “Maintaining State”](#maintaining-state)

**Added in:** `astro@2.10.0`

You can persist components and HTML elements (instead of replacing them) across page navigations using the `transition:persist` directive.

For example, the following `<video>` will continue to play as you navigate to another page that contains the same video element. This works for both forwards and backwards navigation.

src/components/Video.astro

```astro
<video controls muted autoplay transition:persist>
  <source
    src="https://ia804502.us.archive.org/33/items/GoldenGa1939_3/GoldenGa1939_3_512kb.mp4"
    type="video/mp4"
  />
</video>
```

You can also place the directive on an [Astro island](/en/concepts/islands/) (a UI framework component with a [`client:` directive](/en/reference/directives-reference/#client-directives)). If that component exists on the next page, the island from the old page **with its current state** will continue to be displayed, instead of replacing it with the island from the new page.

In the example below, the component’s internal state of the count will not be reset when navigating back and forth across pages that contain the `<Counter />` component with the `transition:persist` attribute.

components/Header.astro

```astro
<Counter client:load transition:persist initialCount={5} />
```

Known limitations

Not all state can be preserved in this way. The restart of CSS animations and the reload of iframes cannot be avoided during view transitions even when using `transition:persist`.

You can also [manually identify corresponding elements](#naming-a-transition) if the island/element is in a different component between the two pages.

src/pages/old-page.astro

```astro
<video
  controls
  muted
  autoplay
  transition:name="media-player"
  transition:persist
/>
```

src/pages/new-page.astro

```astro
<MyVideo
  controls
  muted
  autoplay
  transition:name="media-player"
  transition:persist
/>
```

As a convenient shorthand, `transition:persist` can alternatively take a transition name as a value.

src/pages/index.astro

```astro
<video controls muted autoplay transition:persist="media-player">
```

#### `transition:persist-props`

[Section titled “transition:persist-props”](#transitionpersist-props)

**Added in:** `astro@4.5.0`

This allows you to control whether or not an island’s props should be persisted upon navigation.

By default, when you add `transition:persist` to an island, the state is retained upon navigation, but your component will re-render with new props. This is useful, for example, when a component receives page-specific props such as the current page’s `title`.

You can override this behavior by setting `transition:persist-props` in addition to `transition:persist`. Adding this directive will keep an island’s existing props (not re-render with new values) in addition to maintaining its existing state.

### Built-in Animation Directives

[Section titled “Built-in Animation Directives”](#built-in-animation-directives)

Astro comes with a few built-in animations to override the default `fade` transition. Add the `transition:animate` directive to individual elements to customize the behavior of specific transitions.

* `fade` (default): An opinionated crossfade animation. The old content fades out and the new content fades in.
* `initial`: Opt out of Astro’s opinionated crossfade animation and use the browser’s default styling.
* `slide`: An animation where the old content slides out to the left and new content slides in from the right. On backwards navigation, the animations are the opposite.
* `none`: Disable the browser’s default animations. Use on a page’s `<html>` element to disable the default fade for every element on the page.

Combine directives for full control over your page animation. Set a page default on the `<html>` element, and override on any individual elements as desired.

The example below produces a slide animation for the body content while disabling the browser’s default fade animation for the rest of the page:

```astro
---
import CommonHead from "../components/CommonHead.astro";
---


<html transition:name="root" transition:animate="none">
  <head>
    <CommonHead />
  </head>
  <body>
    <header>
      ...
    </header>
    <!-- Override your page default on a single element -->
    <main transition:animate="slide">
      ...
    </main>
  </body>
</html>
```

### Customizing Animations

[Section titled “Customizing Animations”](#customizing-animations)

You can customize all aspects of a transition with any CSS animation properties.

To customize a built-in animation, first import the animation from `astro:transitions`, and then pass in customization options.

The example below customizes the duration of the built-in `fade` animation:

```astro
---
import { fade } from "astro:transitions";
---
<header transition:animate={fade({ duration: "0.4s" })}>
```

You can also define your own animations for use with `transition:animate` by defining both the forwards and backwards behavior, as well as new and old pages, according to the following types:

```ts
export interface TransitionAnimation {
  name: string; // The name of the keyframe
  delay?: number | string;
  duration?: number | string;
  easing?: string;
  fillMode?: string;
  direction?: string;
}


export interface TransitionAnimationPair {
  old: TransitionAnimation | TransitionAnimation[];
  new: TransitionAnimation | TransitionAnimation[];
}


export interface TransitionDirectionalAnimations {
  forwards: TransitionAnimationPair;
  backwards: TransitionAnimationPair;
}
```

The following example shows all the necessary properties to define a custom `bump` animation inside a `<style is:global>` tag in your root layout file:

src/layouts/Layout.astro

```astro
---
import { ClientRouter } from "astro:transitions";
---
<html lang="en">
  <head>
    <ClientRouter />
  </head>
  <body>
    <slot />
  </body>
</html>


<style is:global>
  @keyframes bump {
    0% {
      opacity: 0;
      transform: scale(1) translateX(200px);
    }
    50% {
      opacity: 0.5;
      transform: scale(1.1);
    }
    100% {
      opacity: 1;
      transform: scale(1) translateX(0);
    }
  }
</style>
```

The animation’s behavior must be defined in the frontmatter of every component using the animation:

src/pages/index.astro

```astro
---
const anim = {
  old: {
    name: "bump",
    duration: "0.5s",
    easing: "ease-in",
    direction: "reverse",
  },
  new: {
    name: "bump",
    duration: "0.5s",
    easing: "ease-in-out",
  },
};


const customTransition = {
  forwards: anim,
  backwards: anim,
};
---
<header transition:animate={customTransition}> ... </header>
```

You have great flexibility when defining custom animations. To achieve your desired result, you may wish to consider unusual combinations such as using different objects for forward and backward, or providing separate keyframe animations for old and new.

## Router control

[Section titled “Router control”](#router-control)

The `<ClientRouter />` router handles navigation by listening to:

* Clicks on `<a>` elements.
* Backwards and forwards navigation events.

The following options allow you to further control when navigation occurs within the router:

* `data-astro-reload`: an `<a>` tag attribute to [force a full-page navigation](#preventing-client-side-navigation)
* `data-astro-history="auto | push | replace"`: an `<a>` tag attribute to [control the browser’s history](#replace-entries-in-the-browser-history)
* `navigate(href, options)`: a method available to any client script or client component to [trigger navigation](#trigger-navigation)

### Preventing client-side navigation

[Section titled “Preventing client-side navigation”](#preventing-client-side-navigation)

There are some cases where you cannot navigate via client-side routing since both pages involved must use the `<ClientRouter />` router to prevent a full-page reload. You may also not want client-side routing on every navigation change and would prefer a traditional page navigation on select routes instead.

You can opt out of client-side routing on a per-link basis by adding the `data-astro-reload` attribute to any `<a>` or `<form>` tag. This attribute will override any existing `<ClientRouter />` component and instead trigger a browser refresh during navigation.

The following example shows preventing client-side routing when navigating to an article from the home page only. This still allows you to have animation on shared elements, such as a hero image, when navigating to the same page from an article listing page:

src/pages/index.astro

```astro
<a href="/articles/emperor-penguins" data-astro-reload>
```

src/pages/articles.astro

```astro
<a href="/articles/emperor-penguins">
```

Links with the `data-astro-reload` attribute will be ignored by the router and a full-page navigation will occur.

### Trigger navigation

[Section titled “Trigger navigation”](#trigger-navigation)

You can also trigger client-side navigation via events not normally listened to by the `<ClientRouter />` router using `navigate`. This function from the `astro:transitions/client` module can be used in scripts, and in framework components that are hydrated with a [client directive](/en/reference/directives-reference/#client-directives).

The following example shows an Astro component that navigates a visitor to another page they select from a menu:

src/components/Form.astro

```astro
<script>
  import { navigate } from "astro:transitions/client";


  // Navigate to the selected option automatically.
  document.querySelector("select").onchange = (event) => {
    let href = event.target.value;
    navigate(href);
  };
</script>
<select>
  <option value="/play">Play</option>
  <option value="/blog">Blog</option>
  <option value="/about">About</option>
  <option value="/contact">Contact</option>
</select>
```

src/pages/index.astro

```astro
---
import Form from "../components/Form.astro";
import { ClientRouter } from "astro:transitions";
---
<html>
  <head>
    <ClientRouter />
  </head>
  <body>
    <Form />
  </body>
</html>
```

The following example implements the same using `navigate()` in a React `<Form />` component:

src/components/Form.jsx

```js
import { navigate } from "astro:transitions/client";


export default function Form() {
  return (
    <select onChange={(e) => navigate(e.target.value)}>
      <option value="/play">Play</option>
      <option value="/blog">Blog</option>
      <option value="/about">About</option>
      <option value="/contact">Contact</option>
    </select>
  );
}
```

The `<Form />` component can then be rendered on an Astro page that uses the `<ClientRouter />` router, with a client directive:

src/pages/index.astro

```astro
---
import Form from "../components/Form.jsx";
import { ClientRouter } from "astro:transitions";
---
<html>
  <head>
    <ClientRouter />
  </head>
  <body>
    <Form client:load />
  </body>
</html>
```

The `navigate` method takes these arguments:

* `href` (required) - The new page to navigate to.

* `options` - An optional object with the following properties:

  * `history`: `"push"` | `"replace"` | `"auto"`

    * `"push"`: the router will use `history.pushState` to create a new entry in the browser history.
    * `"replace"`: the router will use `history.replaceState` to update the URL without adding a new entry into navigation.
    * `"auto"` (default): the router will attempt `history.pushState`, but if the URL is not one that can be transitioned to, the current URL will remain with no changes to the browser history.

  * `formData`: A [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData) object for `POST` requests.

For backward and forward navigation through the browser history, you can combine `navigate()` with the built-in `history.back()`, `history.forward()` and `history.go()` functions of the browser. If `navigate()` is called during the server-side render of your component, it has no effect.

### Replace entries in the browser history

[Section titled “Replace entries in the browser history”](#replace-entries-in-the-browser-history)

Normally, each time you navigate, a new entry is written to the browser’s history. This allows navigation between pages using the browser’s `back` and `forward` buttons.

The `<ClientRouter />` router allows you to overwrite history entries by adding the `data-astro-history` attribute to any individual `<a>` tag.

The `data-astro-history` attribute can be set to the same three values as the [`history` option of the `navigate()` function](#trigger-navigation):

`data-astro-history`: `"push"` | `"replace"` | `"auto"`

* `"push"`: the router will use `history.pushState` to create a new entry in the browser history.
* `"replace"`: the router will use `history.replaceState` to update the URL without adding a new entry into navigation.
* `"auto"` (default): the router will attempt `history.pushState`, but if the URL is not one that can be transitioned to, the current URL will remain with no changes to the browser history.

The following example navigates to the `/main` page but does not add a new entry to the browsing history. Instead, it reuses the current entry in the history (`/confirmation`) and overwrites it.

src/pages/confirmation.astro

```astro
<a href="/main" data-astro-history="replace">
```

This has the effect that if you go back from the `/main` page, the browser will not display the `/confirmation` page, but the page before it.

### Transitions with forms

[Section titled “Transitions with forms”](#transitions-with-forms)

**Added in:** `astro@4.0.0`

The `<ClientRouter />` router will trigger in-page transitions from `<form>` elements, supporting both `GET` and `POST` requests.

By default, Astro submits your form data as `multipart/form-data` when your `method` is set to `POST`. If you want to match the default behavior of web browsers, use the `enctype` attribute to submit your data encoded as `application/x-www-form-urlencoded`:

src/components/Form.astro

```astro
<form
  action="/contact"
  method="POST"
  enctype="application/x-www-form-urlencoded"
>
```

You can opt out of router transitions on any individual form using the `data-astro-reload` attribute:

src/components/Form.astro

```astro
<form action="/contact" data-astro-reload>
```

## Fallback control

[Section titled “Fallback control”](#fallback-control)

The `<ClientRouter />` router works best in browsers that support View Transitions (i.e. Chromium browsers), but also includes default fallback support for other browsers. Even if the browser does not support the View Transitions API, Astro’s client router can still provide in-browser navigation using one of the fallback options.

Depending on browser support, you may need to explicitly set the `name` or `animate` [transition directives](#transition-directives) on the elements you wish to animate for a comparable experience across all browsers:

src/pages/about.astro

```astro
---
import Layout from "../layouts/LayoutUsingClientRouter.astro";
---
<title transition:animate="fade">About my site</title>
```

You can override Astro’s default fallback support by adding a `fallback` property on the `<ClientRouter />` component and setting it to `swap` or `none`:

* `animate` (default, recommended): Astro will simulate view transitions using custom attributes before updating page content.
* `swap`: Astro will not attempt to animate the page. Instead, the old page will be immediately replaced by the new one.
* `none`: Astro will not do any animated page transitions at all. Instead, you will get full page navigation in non-supporting browsers.

```astro
---
import { ClientRouter } from "astro:transitions";
---
<title>My site</title>


<ClientRouter fallback="swap" />
```

Known limitations

The `initial` browser animation is not simulated by Astro. So any element using this animation will not currently be animated.

## Client-side navigation process

[Section titled “Client-side navigation process”](#client-side-navigation-process)

When using the `<ClientRouter />` router, the following steps occur to produce Astro’s client-side navigation:

1. A visitor to your site triggers navigation by any of the following actions:

   * Clicking an `<a>` tag linking internally to another page on your site.
   * Clicking the back button.
   * Clicking the forward button.

2. The router starts fetching the next page.

3. The router adds the `data-astro-transition` attribute to the HTML element with a value of `"forward"` or `"back"` as appropriate.

4. The router calls `document.startViewTransition`. This triggers the browser’s own [view transition process](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API/Using#the_view_transition_process). Importantly, the browser screenshots the current state of the page.

5. Inside the `startViewTransition` callback, the router performs a **swap**, which consists of the following sequence of events:

   * The contents of the `<head>` are swapped out, with some elements kept:

     * Stylesheet DOM nodes are left in if they exist on the new page, to prevent FOUC.
     * Scripts are left in if they exist on the new page.
     * Any other head elements with `transition:persist` are left in if there is a corresponding element in the new page.

   * The `<body>` is completely replaced with the new page’s body.

   * Elements marked `transition:persist` are moved over to the new DOM if they exist on the new page.

   * Scroll position is restored if necessary.

   * The `astro:after-swap` event is triggered on the `document`. This is the end of the **swap** process.

6. The router waits for any new stylesheets to load before resolving the transition.

7. The router executes any new scripts added to the page.

8. The `astro:page-load` event fires. This is the end of the navigation process.

## Script behavior with view transitions

[Section titled “Script behavior with view transitions”](#script-behavior-with-view-transitions)

When you add view transitions to an existing Astro project, some of your scripts may no longer re-run after page navigation like they did with full-page browser refreshes. Use the following information to ensure that your scripts execute as expected.

### Script order

[Section titled “Script order”](#script-order)

When navigating between pages with the `<ClientRouter />` component, scripts are run in sequential order to match browser behavior.

### Script re-execution

[Section titled “Script re-execution”](#script-re-execution)

[Bundled module scripts](/en/guides/client-side-scripts/#script-processing), which are the default scripts in Astro, are only ever executed once. After initial execution they will be ignored, even if the script exists on the new page after a transition.

Unlike bundled module scripts, [inline scripts](/en/guides/client-side-scripts/#unprocessed-scripts) have the potential to be re-executed during a user’s visit to a site if they exist on a page that is visited multiple times. Inline scripts might also re-execute when a visitor navigates to a page without the script, and then back to one with the script.

With view transitions, some scripts may no longer re-run after page navigation like they do with full-page browser refreshes. There are several [events during client-side routing that you can listen for](#lifecycle-events), and fire events when they occur. You can wrap an existing script in an event listener to ensure it runs at the proper time in the navigation cycle.

The following example wraps a script for a mobile “hamburger” menu in an event listener for `astro:page-load` which runs at the end of page navigation to make the menu responsive to being clicked after navigating to a new page:

src/scripts/menu.js

```diff
+document.addEventListener("astro:page-load", () => {
  document.querySelector(".hamburger").addEventListener("click", () => {
    document.querySelector(".nav-links").classList.toggle("expanded");
  });
+});
```

The following example shows a function that runs in response to the `astro:after-swap` event, which happens immediately after the new page has replaced the old page and before the DOM elements are painted to the screen. This avoids a flash of light mode theme after page navigation by checking and, if necessary, setting the dark mode theme before the new page is rendered:

src/components/ThemeToggle.astro

```astro
<script is:inline>
  function applyTheme() {
    localStorage.theme === "dark"
      ? document.documentElement.classList.add("dark")
      : document.documentElement.classList.remove("dark");
  }


  document.addEventListener("astro:after-swap", applyTheme);
  applyTheme();
</script>
```

#### `data-astro-rerun`

[Section titled “data-astro-rerun”](#data-astro-rerun)

**Added in:** `astro@4.5.0`

To force inline scripts to re-execute after every transition, add the `data-astro-rerun` property. Adding any attribute to a script also implicitly adds `is:inline`, so this is only available for scripts that are not bundled and processed by Astro.

```astro
<script is:inline data-astro-rerun>...</script>
```

To ensure that a script runs every time a page is loaded during client-side navigation, it should be executed by a [lifecycle event](#lifecycle-events). For example, event listeners for `DOMContentLoaded` can be replaced by the [`astro:page-load`](/en/guides/view-transitions/#astropage-load) lifecycle event.

If you have code that sets up a global state in an inline script, this state will need to take into account that the script might execute more than once. Check for the global state in your `<script>` tag, and conditionally execute your code where possible. This works because `window` is preserved.

```astro
<script is:inline>
  if (!window.SomeGlobal) {
    window.SomeGlobal = {};
  }
</script>
```

## Lifecycle events

[Section titled “Lifecycle events”](#lifecycle-events)

The `<ClientRouter />` router fires a number of events on the `document` during navigation. These events provide hooks into the lifecycle of navigation, allowing you to do things like show indicators that a new page is loading, override default behavior, and restore state as navigation is completing.

The navigation process involves a **preparation** phase, when new content is loaded; a **DOM swap** phase, where the old page’s content is replaced by the new page’s content; and a **completion** phase where scripts are executed, loading is reported as completed and clean-up work is carried out.

Astro’s View Transition API lifecycle events in order are:

* [`astro:before-preparation`](#astrobefore-preparation)
* [`astro:after-preparation`](#astroafter-preparation)
* [`astro:before-swap`](#astrobefore-swap)
* [`astro:after-swap`](#astroafter-swap)
* [`astro:page-load`](#astropage-load)

Tip

`before-` events allow you to influence and modify actions that are about to take place, and `after-` events are notifications that a phase is complete.

While some actions can be triggered during any event, some tasks can only be performed during a specific event for best results, such as displaying a loading spinner before preparation or overriding animation pairs before swapping content.

### `astro:before-preparation`

[Section titled “astro:before-preparation”](#astrobefore-preparation)

**Added in:** `astro@3.6.0`

An event that fires at the beginning of the preparation phase, after navigation has started (e.g. after the user has clicked a link), but before content is loaded.

This event is used:

* To do something before loading has started, such as showing a loading spinner.
* To alter loading, such as loading content you’ve defined in a template rather than from the external URL.
* To change the `direction` of the navigation (which is usually either `forward` or `backward`) for custom animation.

Here is an example of using the `astro:before-preparation` event to load a spinner before the content is loaded and stop it immediately after loading. Note that using the `loader` callback in this way allows asynchronous execution of code.

```astro
<script is:inline>
  document.addEventListener("astro:before-preparation", (event) => {
    const originalLoader = event.loader;
    event.loader = async function () {
      const { startSpinner } = await import("./spinner.js");
      const stop = startSpinner();
      await originalLoader();
      stop();
    };
  });
</script>
```

### `astro:after-preparation`

[Section titled “astro:after-preparation”](#astroafter-preparation)

**Added in:** `astro@3.6.0`

An event that fires at the end of the preparation phase, after the new page’s content has been loaded and parsed into a document. This event occurs before the view transitions phase.

This example uses the `astro:before-preparation` event to start a loading indicator and the `astro:after-preparation` event to stop it:

```astro
<script is:inline>
  document.addEventListener("astro:before-preparation", () => {
    document.querySelector("#loading").classList.add("show");
  });
  document.addEventListener("astro:after-preparation", () => {
    document.querySelector("#loading").classList.remove("show");
  });
</script>
```

This is a simpler version of loading a spinner than the example shown above: if all of the listener’s code can be executed synchronously, there is no need to hook into the `loader` callback.

### `astro:before-swap`

[Section titled “astro:before-swap”](#astrobefore-swap)

**Added in:** `astro@3.6.0`

An event that fires before the new document (which is populated during the preparation phase) replaces the current document. This event occurs inside of the view transition, where the user is still seeing a snapshot of the old page.

This event can be used to make changes before the swap occurs. The `newDocument` property on the event represents the incoming document. Here is an example of ensuring the browser’s light or dark mode preference in `localStorage` is carried over to the new page:

```astro
<script>
  document.addEventListener("astro:before-swap", (event) => {
    event.newDocument.documentElement.dataset.theme =
      localStorage.getItem("darkMode") ? "dark" : "light";
  });
</script>
```

The `astro:before-swap` event can also be used to change the *implementation* of the swap. The default swap implementation diffs head content, moves **persistent** elements from the old document to the `newDocument`, and then replaces the entire `body` with the body of the new document.

At this point of the lifecycle, you could choose to define your own swap implementation, for example to diff the entire contents of the existing document (which some other routers do):

```astro
<script is:inline>
  document.addEventListener("astro:before-swap", (event) => {
    event.swap = () => {
      diff(document, event.newDocument);
    };
  });
</script>
```

#### Building a custom swap function

[Section titled “Building a custom swap function”](#building-a-custom-swap-function)

**Added in:** `astro@4.15.0`

The `swapFunctions` object of the `astro:transitions/client` module provides five utility functions that handle specific swap-related tasks, including handling document attributes, page elements, and script execution. These functions can be used directly to define a custom swap implementation.

The following example demonstrates how to use these functions to recreate Astro’s built-in swap implementation:

```astro
<script>
  import { swapFunctions } from "astro:transitions/client";


  // substitutes `window.document` with `doc`
  function mySwap(doc: Document) {
    swapFunctions.deselectScripts(doc);
    swapFunctions.swapRootAttributes(doc);
    swapFunctions.swapHeadElements(doc);
    const restoreFocusFunction = swapFunctions.saveFocus();
    swapFunctions.swapBodyElement(doc.body, document.body);
    restoreFocusFunction();
  }


  document.addEventListener("astro:before-swap", (event) => {
    event.swap = () => mySwap(event.newDocument);
  });
<script>
```

Custom swap implementations can start with this template and add or replace individual steps with custom logic as needed.

### `astro:after-swap`

[Section titled “astro:after-swap”](#astroafter-swap)

An event that fires immediately after the new page replaces the old page. You can listen to this event on the `document` and trigger actions that will occur before the new page’s DOM elements render and scripts run.

This event, when listened to on the **outgoing page**, is useful to pass along and restore any state on the DOM that needs to transfer over to the new page.

This is the latest point in the lifecycle where it is still safe to, for example, add a dark mode class name (`<html class="dark-mode">`), though you may wish to do so in an earlier event.

The `astro:after-swap` event occurs immediately after the browser history has been updated and the scroll position has been set. Therefore, one use of targeting this event is to override the default scroll restore for history navigation. The following example resets the horizontal and vertical scroll position to the top left corner of the page for each navigation.

```js
document.addEventListener("astro:after-swap", () =>
  window.scrollTo({ left: 0, top: 0, behavior: "instant" }),
);
```

### `astro:page-load`

[Section titled “astro:page-load”](#astropage-load)

An event that fires at the end of page navigation, after the new page is visible to the user and blocking styles and scripts are loaded. You can listen to this event on the `document`.

The `<ClientRouter />` component fires this event both on initial page navigation for a pre-rendered page and on any subsequent navigation, either forwards or backwards.

You can use this event to run code on every page navigation, for example to set up event listeners that would otherwise be lost during navigation.

```astro
<script>
  document.addEventListener("astro:page-load", () => {
    // This runs on first page load and after every navigation.
    setupStuff(); // e.g. add event listeners
  });
</script>
```

## Accessibility

[Section titled “Accessibility”](#accessibility)

Enabling client-side routing and animating page transitions both come with accessibility challenges, and Astro aims to make sites opting in to View Transitions as accessible-by-default as possible.

### Route announcement

[Section titled “Route announcement”](#route-announcement)

**Added in:** `astro@3.2.0`

The `<ClientRouter />` component includes a route announcer for page navigation during client-side routing. No configuration or action is needed to enable this.

Assistive technologies let visitors know that the page has changed by announcing the new page title after navigation. When using server-side routing with traditional full-page browser refreshes, this happens by default after the new page loads. In client-side routing, the `<ClientRouter />` component performs this action.

To add route announcement to client-side routing, the component adds an element to the new page with the `aria-live` attribute set to `assertive`. This tells AT (assistive technology) to announce immediately. The component also checks for the following, in priority order, to determine the announcement text:

* The `<title>`, if it exists.
* The first `<h1>` it finds.
* The `pathname` of the page.

We strongly recommend you always include a `<title>` in each page for accessibility.

### `prefers-reduced-motion`

[Section titled “prefers-reduced-motion”](#prefers-reduced-motion)

Astro’s `<ClientRouter />` component includes a CSS media query that disables *all* view transition animations, including fallback animation, whenever the [`prefer-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) setting is detected. Instead, the browser will simply swap the DOM elements without an animation.

# Astro recipes

> Short, focused how-to guides.

See guided examples of adding features to your Astro project.

## Official Recipes

[Section titled “Official Recipes”](#official-recipes)

Astro’s official recipes are short, focused how-to guides that walk a reader through completing a working example of a specific task. Recipes are a great way to add new features or behavior to your Astro project by following step-by-step instructions!

* ### [Installing a Vite or Rollup plugin](/en/recipes/add-yaml-support/)

  Learn how you can import YAML data by adding a Rollup plugin to your project.

* ### [Analyze bundle size](/en/recipes/analyze-bundle-size/)

  Learn how to analyze the bundle generated by Astro using \`rollup-plugin-visualizer\`.

* ### [Build a custom image component](/en/recipes/build-custom-img-component/)

  Learn how to build a custom image component that supports media queries using the getImage function.

* ### [Build forms with API routes](/en/recipes/build-forms-api/)

  Learn how to use JavaScript to send form submissions to an API Route.

* ### [Use Bun with Astro](/en/recipes/bun/)

  Learn how to use Bun with your Astro site.

* ### [Build HTML forms in Astro pages](/en/recipes/build-forms/)

  Learn how to build HTML forms and handle submissions in your frontmatter.

* ### [Call endpoints from the server](/en/recipes/call-endpoints/)

  Learn how to call endpoints from the server in Astro.

* ### [Verify a Captcha](/en/recipes/captcha/)

  Learn how to create an API route and fetch it from the client.

* ### [Customize file names in the build output](/en/recipes/customizing-output-filenames/)

  Learn how to change the default naming pattern for your built assets like JavaScript, CSS, and images in Astro using Vite's Rollup options.

* ### [Build your Astro site with Docker](/en/recipes/docker/)

  Learn how to build your Astro site using Docker.

* ### [Add icons to external links](/en/recipes/external-links/)

  Learn how to install a rehype plugin to add icons to external links in your Markdown files.

* ### [Dynamically import images](/en/recipes/dynamically-importing-images/)

  Learn how to dynamically import images using Vite's import.meta.glob function.

* ### [Add i18n features](/en/recipes/i18n/)

  Use dynamic routing and content collections to add internationalization support to your Astro site.

* ### [Create a dev toolbar app](/en/recipes/making-toolbar-apps/)

  Learn how to create a dev toolbar app for your site.

* ### [Add last modified time](/en/recipes/modified-time/)

  Build a remark plugin to add the last modified time to your Markdown and MDX.

* ### [Add reading time](/en/recipes/reading-time/)

  Build a remark plugin to add reading time to your Markdown or MDX files.

* ### [Add an RSS feed](/en/recipes/rss/)

  Add an RSS feed to your Astro site to let users subscribe to your content.

* ### [Share state between islands](/en/recipes/sharing-state-islands/)

  Learn how to share state across framework components with Nano Stores.

* ### [Share state between Astro components](/en/recipes/sharing-state/)

  Learn how to share state across Astro components with Nano Stores.

* ### [Using streaming to improve page performance](/en/recipes/streaming-improve-page-performance/)

  Learn how to use streaming to improve page performance.

* ### [Style rendered Markdown with Tailwind Typography](/en/recipes/tailwind-rendered-markdown/)

  Learn how to use @tailwind/typography to style your rendered Markdown.

## Community Resources

[Section titled “Community Resources”](#community-resources)

Find more recipes written and submitted by the community at [Astro Tips](https://astro-tips.dev).

# Installing a Vite or Rollup plugin

> Learn how you can import YAML data by adding a Rollup plugin to your project.

Astro builds on top of Vite, and supports both Vite and Rollup plugins. This recipe uses a Rollup plugin to add the ability to import a YAML (`.yml`) file in Astro.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install `@rollup/plugin-yaml`:

   * npm

     ```shell
     npm install @rollup/plugin-yaml --save-dev
     ```

   * pnpm

     ```shell
     pnpm add @rollup/plugin-yaml --save-dev
     ```

   * Yarn

     ```shell
     yarn add @rollup/plugin-yaml --dev
     ```

2. Import the plugin in your `astro.config.mjs` and add it to the Vite plugins array:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import yaml from '@rollup/plugin-yaml';


   export default defineConfig({
   +  vite: {
   +    plugins: [yaml()]
   +  }
   });
   ```

3. Finally, you can import YAML data using an `import` statement:

   ```js
   import yml from './data.yml';
   ```

   Note

   While you can now import YAML data in your Astro project, your editor will not provide types for the imported data. To add types, create or find an existing `*.d.ts` file in the `src` directory of your project and add the following:

   src/files.d.ts

   ```ts
   // Specify the file extension you want to import
   declare module "*.yml" {
     const value: any; // Add type definitions here if desired
     export default value;
   }
   ```

   This will allow your editor to provide type hints for your YAML data.

# Analyze bundle size

> Learn how to analyze the bundle generated by Astro using `rollup-plugin-visualizer`.

Understanding what is a part of an Astro bundle is important for improving site performance. Visualizing the bundle can give clues as to where changes can be made in your project to reduce the bundle size.

## Recipe

[Section titled “Recipe”](#recipe)

The [`rollup-plugin-visualizer` library](https://github.com/btd/rollup-plugin-visualizer) allows you to visualize and analyze your Rollup bundle to see which modules are taking up space.

1. Install `rollup-plugin-visualizer`:

   * npm

     ```shell
     npm install rollup-plugin-visualizer --save-dev
     ```

   * pnpm

     ```shell
     pnpm add rollup-plugin-visualizer --save-dev
     ```

   * Yarn

     ```shell
     yarn add rollup-plugin-visualizer --save-dev
     ```

2. Add the plugin to the `astro.config.mjs` file:

   ```js
   // @ts-check
   import { defineConfig } from 'astro/config';
   import { visualizer } from "rollup-plugin-visualizer";


   export default defineConfig({
   vite: {
       plugins: [visualizer({
           emitFile: true,
           filename: "stats.html",
       })]
   }
   });
   ```

3. Run the build command:

   * npm

     ```shell
     npm run build
     ```

   * pnpm

     ```shell
     pnpm build
     ```

   * Yarn

     ```shell
     yarn build
     ```

4. Find the `stats.html` file(s) for your project.

   This will be at the root of your `dist/` directory for entirely static sites and will allow you to see what is included in the bundle.

   If your Astro project uses on-demand rendering, you will have two `stats.html` files. One will be for the client, and the other for the server, and each will be located at the root of the `dist/client` and `dist/server/` directories.

   See [the Rollup Plugin Visualizer documentation](https://github.com/btd/rollup-plugin-visualizer#how-to-use-generated-files) for guidance on how to interpret these files, or configure specific options.

Note

Given Astro’s unique approach to hydration, the build isn’t necessarily representative of the bundle that the client will receive.

The Rollup visualizer shows all dependencies that are used across the site, but it does not break down the bundle size on a per-page basis.

# Build a custom image component

> Learn how to build a custom image component that supports media queries using the getImage function.

Astro provides two built-in components that you can use to display and optimize your images. The `<Picture>` component allows you to display responsive images and work with different formats and sizes. The `<Image>` component will optimize your images and allow you to pass in different formats and quality properties.

When you need options that the `<Picture>` and `<Image>` components do not currently support, you can use the `getImage()` function to create a custom component.

In this recipe, you will use the [`getImage()` function](/en/guides/images/#generating-images-with-getimage) to create your own custom image component that displays different source images based on media queries.

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a new Astro component and import the `getImage()` function

   src/components/MyCustomImageComponent.astro

   ```astro
   ---
    import { getImage } from "astro:assets";
   ---
   ```

2. Create a new component for your custom image. `MyCustomComponent.astro` will receive three `props` from `Astro.props`. The `mobileImgUrl` and `desktopImgUrl` props are used for creating your image at different viewport sizes. The `alt` prop is used for the image’s alt text. These props will be passed wherever you render your custom image components. Add the following imports and define the props that you will use in your component. You can also use TypeScript to type the props.

   src/components/MyCustomImageComponent.astro

   ```diff
   ---
   import type { ImageMetadata } from "astro";
   +import { getImage } from "astro:assets";


   interface Props {
       mobileImgUrl: string | ImageMetadata;
       desktopImgUrl: string | ImageMetadata;
       alt: string;
   }


   +const { mobileImgUrl, desktopImgUrl, alt } = Astro.props;
   ---
   ```

3. Define each of your responsive images by calling the `getImage()` function with your desired properties.

   src/components/MyCustomImageComponent.astro

   ```diff
   ---
   import type { ImageMetadata } from "astro";
   import { getImage } from "astro:assets";


   interface Props {
       mobileImgUrl: string | ImageMetadata;
       desktopImgUrl: string | ImageMetadata;
       alt: string;
   }


   const { mobileImgUrl, desktopImgUrl, alt } = Astro.props;


   +const mobileImg = await getImage({
       src: mobileImgUrl,
       format: "webp",
       width: 200,
       height: 200,
   +});


   +const desktopImg = await getImage({
       src: desktopImgUrl,
       format: "webp",
       width: 800,
       height: 200,
   +});
   ---
   ```

4. Create a `<picture>` element that generates a `srcset` with your different images based on your desired media queries.

   src/components/MyCustomImageComponent.astro

   ```diff
   ---
   import type { ImageMetadata } from "astro";
   import { getImage } from "astro:assets";


   interface Props {
       mobileImgUrl: string | ImageMetadata;
       desktopImgUrl: string | ImageMetadata;
       alt: string;
   }


   const { mobileImgUrl, desktopImgUrl, alt } = Astro.props;


   const mobileImg = await getImage({
       src: mobileImgUrl,
       format: "webp",
       width: 200,
       height: 200,
   });


   const desktopImg = await getImage({
       src: desktopImgUrl,
       format: "webp",
       width: 800,
       height: 200,
   });
   ---


   <picture>
       <source media="(max-width: 799px)" srcset={mobileImg.src} />
       <source media="(min-width: 800px)" srcset={desktopImg.src} />
       <img src={desktopImg.src} alt={alt} />
   </picture>
   ```

5. Import and use `<MyCustomImageComponent />` in any `.astro` file. Be sure to pass the necessary props for generating two different images at the different viewport sizes:

   src/pages/index.astro

   ```astro
   ---
   import MyCustomImageComponent from "../components/MyCustomImageComponent.astro";
   import mobileImage from "../images/mobile-profile-image.jpg";
   import desktopImage from "../images/desktop-profile-image.jpg";
   ---


   <MyCustomImageComponent
       mobileImgUrl={mobileImage}
       desktopImgUrl={desktopImage}
       alt="user profile picture"
   />
   ```

# Build HTML forms in Astro pages

> Learn how to build HTML forms and handle submissions in your frontmatter.

Astro pages that are rendered on demand can both display and handle forms. In this recipe, you’ll use a standard HTML form to submit data to the server. Your frontmatter script will handle the data on the server, sending no JavaScript to the client.

Build forms with Astro Actions

In v4.15, Astro added actions which provide several benefits over basic HTML forms including validating your form data and updating your UI based on the form submission. To use this method for building forms instead, see our [actions guide](/en/guides/actions/) to learn more about these features.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project with a [server adapter](/en/guides/on-demand-rendering/#server-adapters) installed.

## Recipe

[Section titled “Recipe”](#recipe)

1. Create or identify a `.astro` page which will contain your form and your handling code. For example, you could add a registration page:

   src/pages/register.astro

   ```astro
   ---
   ---
   <h1>Register</h1>
   ```

2. Add a `<form>` tag with some inputs to the page. Each input should have a `name` attribute that describes the value of that input.

   Be sure to include a `<button>` or `<input type="submit">` element to submit the form.

   src/pages/register.astro

   ```astro
   ---
   ---
   <h1>Register</h1>
   <form>
     <label>
       Username:
       <input type="text" name="username" />
     </label>
     <label>
       Email:
       <input type="email" name="email" />
     </label>
     <label>
       Password:
       <input type="password" name="password" />
     </label>
     <button>Submit</button>
   </form>
   ```

3. Use [validation attributes](https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation#using_built-in_form_validation) to provide basic client-side validation that works even if JavaScript is disabled.

   In this example,

   * `required` prevents form submission until the field is filled.
   * `minlength` sets a minimum required length for the input text.
   * `type="email"` also introduces validation that will only accept a valid email format.

   src/pages/register.astro

   ```astro
   ---
   ---
   <h1>Register</h1>
   <form>
     <label>
       Username:
       <input type="text" name="username" required />
     </label>
     <label>
       Email:
       <input type="email" name="email" required />
     </label>
     <label>
       Password:
       <input type="password" name="password" required minlength="6" />
     </label>
     <button>Submit</button>
   </form>
   ```

   Tip

   You can add custom validation logic that refers to multiple fields using a `<script>` tag and the [Constraint Validation API](https://developer.mozilla.org/en-US/docs/Web/HTML/Constraint_validation#complex_constraints_using_the_constraint_validation_api).

   To write complex validation logic more easily, you can build your form using a [frontend framework](/en/guides/framework-components/) and choose a form library like [React Hook Form](https://react-hook-form.com/) or [Felte](https://felte.dev/).

4. The form submission will cause the browser to request the page again. Change the form’s data transfer `method` to `POST` to send the form data as part of the `Request` body, rather than as URL parameters.

   src/pages/register.astro

   ```astro
   ---
   ---
   <h1>Register</h1>
   <form method="POST">
     <label>
       Username:
       <input type="text" name="username" required />
     </label>
     <label>
       Email:
       <input type="email" name="email" required />
     </label>
     <label>
       Password:
       <input type="password" name="password" required minlength="6" />
     </label>
     <button>Submit</button>
   </form>
   ```

5. Check for the `POST` method in the frontmatter and access the form data using `Astro.request.formData()`. Wrap this in a `try ... catch` block to handle cases when the `POST` request wasn’t sent by a form and the `formData` is invalid.

   src/pages/register.astro

   ```diff
   ---
   +export const prerender = false; // Not needed in 'server' mode


   +if (Astro.request.method === "POST") {
     +try {
       +const data = await Astro.request.formData();
       +const name = data.get("username");
       +const email = data.get("email");
       +const password = data.get("password");
       +// Do something with the data
   +  } catch (error) {
       +if (error instanceof Error) {
   +      console.error(error.message);
   +    }
   +  }
   +}
   ---
   <h1>Register</h1>
   <form method="POST">
     <label>
       Username:
       <input type="text" name="username" required />
     </label>
     <label>
       Email:
       <input type="email" name="email" required />
     </label>
     <label>
       Password:
       <input type="password" name="password" required minlength="6" />
     </label>
     <button>Submit</button>
   </form>
   ```

6. Validate the form data on the server. This should include the same validation done on the client to prevent malicious submissions to your endpoint and to support the rare legacy browser that doesn’t have form validation.

   It can also include validation that can’t be done on the client. For example, this example checks if the email is already in the database.

   Error messages can be sent back to the client by storing them in an `errors` object and accessing it in the template.

   src/pages/register.astro

   ```diff
   ---
   export const prerender = false; // Not needed in 'server' mode


   import { isRegistered, registerUser } from "../../data/users"
   import { isValidEmail } from "../../utils/isValidEmail";


   +const errors = { username: "", email: "", password: "" };
   if (Astro.request.method === "POST") {
     try {
       const data = await Astro.request.formData();
       const name = data.get("username");
       const email = data.get("email");
       const password = data.get("password");
       +if (typeof name !== "string" || name.length < 1) {
   +      errors.username += "Please enter a username. ";
   +    }
       +if (typeof email !== "string" || !isValidEmail(email)) {
   +      errors.email += "Email is not valid. ";
   +    } else if (await isRegistered(email)) {
   +      errors.email += "Email is already registered. ";
   +    }
       +if (typeof password !== "string" || password.length < 6) {
   +      errors.password += "Password must be at least 6 characters. ";
   +    }
       const hasErrors = Object.values(errors).some(msg => msg)
       if (!hasErrors) {
         await registerUser({name, email, password});
         return Astro.redirect("/login");
       }
     } catch (error) {
       if (error instanceof Error) {
         console.error(error.message);
       }
     }
   }
   ---
   <h1>Register</h1>
   <form method="POST">
     <label>
       Username:
       <input type="text" name="username" />
     </label>
     +{errors.username && <p>{errors.username}</p>}
     <label>
       Email:
       <input type="email" name="email" required />
     </label>
     +{errors.email && <p>{errors.email}</p>}
     <label>
       Password:
       <input type="password" name="password" required minlength="6" />
     </label>
     +{errors.password && <p>{errors.password}</p>}
     <button>Register</button>
   </form>
   ```

# Build forms with API routes

> Learn how to use JavaScript to send form submissions to an API Route.

An HTML form causes the browser to refresh the page or navigate to a new one. To send form data to an API endpoint instead, you must intercept the form submission using JavaScript.

This recipe shows you how to send form data to an API endpoint and handle that data.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [an adapter for on-demand rendering](/en/guides/on-demand-rendering/)
* A [UI Framework integration](/en/guides/framework-components/) installed

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `POST` API endpoint at `/api/feedback` that will receive the form data. Use `request.formData()` to process it. Be sure to validate the form values before you use them.

   This example sends a JSON object with a message back to the client.

   src/pages/api/feedback.ts

   ```ts
   export const prerender = false; // Not needed in 'server' mode
   import type { APIRoute } from "astro";


   export const POST: APIRoute = async ({ request }) => {
     const data = await request.formData();
     const name = data.get("name");
     const email = data.get("email");
     const message = data.get("message");
     // Validate the data - you'll probably want to do more than this
     if (!name || !email || !message) {
       return new Response(
         JSON.stringify({
           message: "Missing required fields",
         }),
         { status: 400 }
       );
     }
     // Do something with the data, then return a success response
     return new Response(
       JSON.stringify({
         message: "Success!"
       }),
       { status: 200 }
     );
   };
   ```

2. Create a form component using your UI framework. Each input should have a `name` attribute that describes the value of that input.

   Be sure to include a `<button>` or `<input type="submit">` element to submit the form.

   * Preact

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```

   * React

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```

   * Solid

     src/components/FeedbackForm.tsx

     ```tsx
     export default function Form() {
       return (
         <form>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
         </form>
       );
     }
     ```

   * Svelte

     src/components/FeedbackForm.svelte

     ```svelte
     <form>
       <label>
         Name
         <input type="text" id="name" name="name" required />
       </label>
       <label>
         Email
         <input type="email" id="email" name="email" required />
       </label>
       <label>
         Message
         <textarea id="message" name="message" required />
       </label>
       <button>Send</button>
     </form>
     ```

   * Vue

     src/components/FeedbackForm.vue

     ```vue
     <template>
       <form>
         <label>
           Name
           <input type="text" id="name" name="name" required />
         </label>
         <label>
           Email
           <input type="email" id="email" name="email" required />
         </label>
         <label>
           Message
           <textarea id="message" name="message" required />
         </label>
         <button>Send</button>
       </form>
     </template>
     ```

3. Create a function that accepts a submit event, then pass it as a `submit` handler to your form.

   In the function:

   * Call `preventDefault()` on the event to override the browser’s default submission process.
   * Create a `FormData` object and send it in a `POST` request to your endpoint using `fetch()`.

   - Preact

     src/components/FeedbackForm.tsx

     ```diff
     +import { useState } from "preact/hooks";


     export default function Form() {
       +const [responseMessage, setResponseMessage] = useState("");


       +async function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +const formData = new FormData(e.target as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
         +if (data.message) {
           +setResponseMessage(data.message);
     +    }
     +  }


       return (
         <form onSubmit={submit}>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
           +{responseMessage && <p>{responseMessage}</p>}
         </form>
       );
     }
     ```

   - React

     src/components/FeedbackForm.tsx

     ```diff
     +import { useState } from "react";
     +import type { FormEvent } from "react";


     export default function Form() {
       +const [responseMessage, setResponseMessage] = useState("");


       +async function submit(e: FormEvent<HTMLFormElement>) {
     +    e.preventDefault();
         +const formData = new FormData(e.target as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
         +if (data.message) {
           +setResponseMessage(data.message);
     +    }
     +  }


       return (
         <form onSubmit={submit}>
           <label htmlFor="name">
             Name
             <input type="text" id="name" name="name" autoComplete="name" required />
           </label>
           <label htmlFor="email">
             Email
             <input type="email" id="email" name="email" autoComplete="email" required />
           </label>
           <label htmlFor="message">
             Message
             <textarea id="message" name="message" autoComplete="off" required />
           </label>
           <button>Send</button>
           +{responseMessage && <p>{responseMessage}</p>}
         </form>
       );
     }
     ```

   - Solid

     src/components/FeedbackForm.tsx

     ```diff
     +import { createSignal, createResource, Suspense } from "solid-js";


     +async function postFormData(formData: FormData) {
       +const response = await fetch("/api/feedback", {
         method: "POST",
         body: formData,
       });
       +const data = await response.json();
       +return data;
     }


     export default function Form() {
       +const [formData, setFormData] = createSignal<FormData>();
       +const [response] = createResource(formData, postFormData);


       +function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +setFormData(new FormData(e.target as HTMLFormElement));
     +  }


       return (
         <form onSubmit={submit}>
           <label>
             Name
             <input type="text" id="name" name="name" required />
           </label>
           <label>
             Email
             <input type="email" id="email" name="email" required />
           </label>
           <label>
             Message
             <textarea id="message" name="message" required />
           </label>
           <button>Send</button>
           +<Suspense>{response() && <p>{response().message}</p>}</Suspense>
         </form>
       );
     }
     ```

   - Svelte

     src/components/FeedbackForm.svelte

     ```diff
     <script lang="ts">
       +let responseMessage: string;


       +async function submit(e: SubmitEvent) {
     +    e.preventDefault();
         +const formData = new FormData(e.currentTarget as HTMLFormElement);
         +const response = await fetch("/api/feedback", {
           method: "POST",
           body: formData,
         });
         +const data = await response.json();
     +    responseMessage = data.message;
     +  }
     </script>


     <form on:submit={submit}>
       <label>
         Name
         <input type="text" id="name" name="name" required />
       </label>
       <label>
         Email
         <input type="email" id="email" name="email" required />
       </label>
       <label>
         Message
         <textarea id="message" name="message" required />
       </label>
       <button>Send</button>
     +  {#if responseMessage}
         <p>{responseMessage}</p>
     +  {/if}
     </form>
     ```

   - Vue

     src/components/FeedbackForm.vue

     ```diff
     <script setup lang="ts">
     +import { ref } from "vue";


     +const responseMessage = ref<string>();


     +async function submit(e: Event) {
     +  e.preventDefault();
       +const formData = new FormData(e.currentTarget as HTMLFormElement);
       +const response = await fetch("/api/feedback", {
         method: "POST",
         body: formData,
       });
       +const data = await response.json();
     +  responseMessage.value = data.message;
     +}
     </script>


     <template>
       <form @submit="submit">
         <label>
           Name
           <input type="text" id="name" name="name" required />
         </label>
         <label>
           Email
           <input type="email" id="email" name="email" required />
         </label>
         <label>
           Message
           <textarea id="message" name="message" required />
         </label>
         <button>Send</button>
         <p v-if="responseMessage">{{ responseMessage }}</p>
       </form>
     </template>
     ```

4. Import and include your `<FeedbackForm />` component on a page. Be sure to use a `client:*` directive to ensure that the form logic is hydrated when you want it to be.

   * Preact

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```

   * React

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```

   * Solid

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm"
     ---
     <FeedbackForm client:load />
     ```

   * Svelte

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm.svelte"
     ---
     <FeedbackForm client:load />
     ```

   * Vue

     src/pages/index.astro

     ```astro
     ---
     import FeedbackForm from "../components/FeedbackForm.vue"
     ---
     <FeedbackForm client:load />
     ```

# Use Bun with Astro

> Learn how to use Bun with your Astro site.

[Bun](https://bun.sh/) is an all-in-one JavaScript runtime & toolkit. See [Bun’s documentation](https://bun.sh/docs) for more information.

Caution

Using Bun with Astro may reveal rough edges. Some integrations may not work as expected. Consult [Bun’s official documentation for working with Astro](https://bun.sh/guides/ecosystem/astro) for details.

If you have any problems using Bun, please [open an Issue on GitHub with Bun directly](https://github.com/oven-sh/bun/issues/new/choose).

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Bun installed locally on your machine. See the [installation instructions](https://bun.sh/docs/installation) in Bun’s official documentation.

## Create a new Astro project with Bun

[Section titled “Create a new Astro project with Bun”](#create-a-new-astro-project-with-bun)

Create a new Astro project with Bun using the following `create-astro` command:

```bash
bun create astro my-astro-project-using-bun
```

## Install dependencies

[Section titled “Install dependencies”](#install-dependencies)

If you skipped the “Install dependencies?” step during the CLI wizard, then be sure to install your dependencies before continuing.

```bash
bun install
```

## Add Types

[Section titled “Add Types”](#add-types)

Bun publishes the [`@types/bun`](https://www.npmjs.com/package/@types/bun) package, containing the runtime types for Bun.

Install `@types/bun` using the following command:

```sh
bun add -d @types/bun
```

## CLI installation flags

[Section titled “CLI installation flags”](#cli-installation-flags)

### Using integrations

[Section titled “Using integrations”](#using-integrations)

You can also use any of the official Astro integrations with the `astro add` command:

```bash
bun astro add react
```

### Use a theme or starter template

[Section titled “Use a theme or starter template”](#use-a-theme-or-starter-template)

You can start a new Astro project based on an [official example](https://github.com/withastro/astro/tree/main/examples) or the main branch of any GitHub repository by passing a `--template` argument to the `create astro` command.

Run the following command in your terminal, substituting the official Astro starter template name, or the GitHub username and repository of the theme you want to use:

```bash
# create a new project with an official example
bun create astro@latest --template <example-name>
# create a new project based on a GitHub repository’s main branch
bun create astro@latest --template <github-username>/<github-repo>
```

## Develop and build

[Section titled “Develop and build”](#develop-and-build)

To run the development server, use following command:

```bash
bun run dev
```

### Build and preview your site

[Section titled “Build and preview your site”](#build-and-preview-your-site)

To build your site, use the following command:

```bash
bun run build
```

When the build is finished, run the appropriate preview command (e.g. `bun run preview`) in your terminal and you can view the built version of your site locally in the same browser preview window.

## Testing

[Section titled “Testing”](#testing)

Bun ships with a fast, built-in, Jest-compatible test runner through the [`bun test` command](https://bun.sh/docs/cli/test). You can also use any other [testing tools for Astro](/en/guides/testing/).

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Build an app with Astro and Bun](https://bun.sh/guides/ecosystem/astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

Using Bun with Astro? Add your blog post or video to this page!

* [Building a Cloudflare Pages site with Bun](https://blog.otterlord.dev/posts/hello-from-bun/) - blog post
* [Using Bun with Astro and Cloudflare Pages](https://handerson.hashnode.dev/using-bun-with-astro-and-cloudflare-pages) - blog post

# Call endpoints from the server

> Learn how to call endpoints from the server in Astro.

Endpoints can be used to serve many kinds of data. This recipe calls a server endpoint from a page’s component script to display a greeting, without requiring an additional fetch request.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [SSR](/en/guides/on-demand-rendering/) (output: ‘server’) enabled

## Recipe

[Section titled “Recipe”](#recipe)

1. Create an endpoint in a new file `src/pages/api/hello.ts` that returns some data:

   src/pages/api/hello.ts

   ```ts
   import type { APIRoute } from 'astro'


   export const GET: APIRoute = () => {
     return new Response(
       JSON.stringify({
         greeting: 'Hello',
       }),
     )
   }
   ```

2. On any Astro page, import the `GET()` method from the endpoint. Call it with the [`Astro` global](/en/reference/api-reference/) to provide the request context, and use the response on the page:

   src/pages/index.astro

   ```astro
   ---
   import { GET } from './api/hello.ts'


   let response = await GET(Astro)
   const data = await response.json()
   ---


   <h1>{data.greeting} world!</h1>
   ```

# Verify a Captcha

> Learn how to create an API route and fetch it from the client.

[Server endpoints](/en/guides/endpoints/#server-endpoints-api-routes) can be used as REST API endpoints to run functions such as authentications, database access, and verifications without exposing sensitive data to the client.

In this recipe, an API route is used to verify Google reCAPTCHA v3 without exposing the secret to clients.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [SSR](/en/guides/on-demand-rendering/) (`output: 'server'`) enabled

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a `POST` endpoint that accepts recaptcha data, then verifies it with reCAPTCHA’s API. Here, you can safely define secret values or read environment variables.

   src/pages/recaptcha.js

   ```js
   export async function POST({ request }) {
     const data = await request.json();


     const recaptchaURL = 'https://www.google.com/recaptcha/api/siteverify';
     const requestHeaders = {
       'Content-Type': 'application/x-www-form-urlencoded'
     };
     const requestBody = new URLSearchParams({
       secret: "YOUR_SITE_SECRET_KEY",   // This can be an environment variable
       response: data.recaptcha          // The token passed in from the client
     });


     const response = await fetch(recaptchaURL, {
       method: "POST",
       headers: requestHeaders,
       body: requestBody.toString()
     });


     const responseData = await response.json();


     return new Response(JSON.stringify(responseData), { status: 200 });
   }
   ```

2. Access your endpoint using `fetch` from a client script:

   src/pages/index.astro

   ```astro
   <html>
     <head>
       <script is:inline src="https://www.google.com/recaptcha/api.js"></script>
     </head>


     <body>
       <button class="g-recaptcha"
         data-sitekey="PUBLIC_SITE_KEY"
         data-callback="onSubmit"
         data-action="submit"> Click me to verify the captcha challenge! </button>


       <script is:inline>
         function onSubmit(token) {
           fetch("/recaptcha", {
             method: "POST",
             body: JSON.stringify({ recaptcha: token })
           })
           .then((response) => response.json())
           .then((gResponse) => {
             if (gResponse.success) {
               // Captcha verification was a success
             } else {
               // Captcha verification failed
             }
           })
         }
       </script>
     </body>
   </html>
   ```

# Customize file names in the build output

> Learn how to change the default naming pattern for your built assets like JavaScript, CSS, and images in Astro using Vite's Rollup options.

By default, the `astro build` command outputs your built assets from [your project source](/en/basics/project-structure/#src), like JavaScript and CSS files located in the `src/` directory, into an `_astro` directory with hashed filenames (e.g. `_astro/index.DRf8L97S.js`) which are excellent for long-term caching.

Although it is normally not necessary, you can customise the output file names when needed. For example, this can be helpful if you have scripts with names that might trigger ad blockers (e.g. `ads.js`), or if you want to organize your assets with a particular naming convention. By customizing Rollup output options, you can gain more control over your project’s build structure, allowing you to meet specific organizational or deployment requirements.

## Recipe

[Section titled “Recipe”](#recipe)

This recipe configures `vite.build.rollupOptions` to output built assets with the following structure and naming pattern:

* JavaScript entry files (e.g. scripts directly associated with your pages or layouts): `dist/js/[name]-[hash].js`
* JavaScript code-split chunks (e.g. dynamically imported components or shared modules): `dist/js/chunks/[name]-[hash].js`
* Other assets (e.g. CSS, images, fonts): `dist/static/[name]-[hash][extname]` (e.g. `dist/static/styles-a1b2c3d4.css`, `dist/static/logo-e5f6g7h8.svg`)

1. Add Vite Rollup Output Options.

   Modify your `astro.config.mjs` to include the following `vite.build.rollupOptions.output` configuration. This is where you can define the custom naming patterns for your assets using Rollup’s [`entryFileNames`](https://rollupjs.org/configuration-options/#output-entryfilenames), [`chunkFileNames`](https://rollupjs.org/configuration-options/#output-chunkfilenames), and [`assetFileNames`](https://rollupjs.org/configuration-options/#output-assetfilenames):

   astro.config.mjs

   ```javascript
   import { defineConfig } from 'astro/config';


   export default defineConfig({
     // ...
     vite: {
       build: {
         rollupOptions: {
           output: {
             // path names relative to `outDir`
             entryFileNames: 'js/[name]-[hash].js',
             chunkFileNames: 'js/chunks/[name]-[hash].js',
             assetFileNames: 'static/[name]-[hash][extname]',
           },
         },
       },
     },
   });
   ```

   This example uses the following file name placeholders:

   * `[name]`: The original name of the file (without the extension and path).
   * `[hash]`: A content-based hash generated for the file, crucial for cache busting. You can also specify a length, e.g. `[hash:8]`. This ensures that when you update an asset, the filename changes, forcing browsers to download the new version instead of serving a stale cached version.
   * `[extname]`: The original file extension, including the leading dot (e.g. `.js`, `.css`, `.svg`).

   For a full list of available placeholders and advanced patterns for these options, refer to the [Rollup configuration documentation](https://rollupjs.org/configuration-options/).

2. Build your project.

   Since these filename customizations apply to the production build output only, you will need to run your project’s build command:

   * npm

     ```shell
     npm run build
     ```

   * pnpm

     ```shell
     pnpm build
     ```

   * Yarn

     ```shell
     yarn build
     ```

3. After the build completes, inspect your [output directory](/en/reference/configuration-reference/#outdir) (`dist/` by default).

   Verify that the build assets from your project `src` are named and organized according to the new patterns. (Files from [your `public/` directory](/en/basics/project-structure/#public) are copied directly to the output directory and are not affected by these Rollup naming options.)

   Depending on your project’s specific contents, your build folder will now look something like this:

   * dist/

     * js/

       * index-a1b2c3d4.js

       * chunks/

         * common-e5f6g7h8.js

     * img/

       * logo-i9j0k1l2.png

     * fonts/

       * myfont-q2w3e4r5.woff2

     * static\_assets/

       * styles-m3n4o5p6.css

     * index.html

     * about/

       * index.html

     * … (other HTML files and public assets)

# Build your Astro site with Docker

> Learn how to build your Astro site using Docker.

[Docker](https://docker.com) is a tool to build, deploy, and run applications using containers.

Docker images and containers can be deployed to many different platforms, like AWS, Azure, and [Google Cloud](/en/guides/deploy/google-cloud/#cloud-run-ssr-and-static). This recipe won’t cover how to deploy your site to a specific platform but will show you how to set up Docker for your project.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Docker installed on your local machine. You can find [installation instructions for your operating system here](https://docs.docker.com/get-docker/).
* A Dockerfile in your project. You can [learn more about Dockerfiles here](https://docs.docker.com/engine/reference/builder/) and use the Dockerfiles in the following section as a starting point.

## Creating a Dockerfile

[Section titled “Creating a Dockerfile”](#creating-a-dockerfile)

Create a file called `Dockerfile` in your project’s root directory. This file contains the instructions to build your site, which will differ depending on your needs. This guide can’t show all possible options but will give you starting points for SSR and static mode.

If you’re using another package manager than npm, you’ll need to adjust the commands accordingly.

### SSR

[Section titled “SSR”](#ssr)

This Dockerfile will build your site and serve it using Node.js on port `4321` and therefore requires the [Node adapter](/en/guides/integrations-guide/node/) installed in your Astro project.

Dockerfile

```docker
FROM node:lts AS runtime
WORKDIR /app


COPY . .


RUN npm install
RUN npm run build


ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "./dist/server/entry.mjs"]
```

Keep this in mind

These are just examples of Dockerfiles. You can customize them to your needs. For example, you could use another image, like `node:lts-alpine`:

Dockerfile

```diff
-FROM node:lts as runtime
+FROM node:lts-alpine as runtime
```

### Adding a .dockerignore

[Section titled “Adding a .dockerignore”](#adding-a-dockerignore)

Adding a `.dockerignore` file to your project is best practice. This file describes which files or folders should be ignored in the Docker `COPY` or `ADD` commands, very similar to how `.gitignore` works. This speeds up the build process and reduces the size of the final image.

.dockerignore

```docker
.DS_Store
node_modules
dist
```

This file should go in the same directory as the `Dockerfile` itself. [Read the `.dockerignore` documentation for extra info](https://docs.docker.com/engine/reference/builder/#dockerignore-file)

### Static

[Section titled “Static”](#static)

#### Apache (httpd)

[Section titled “Apache (httpd)”](#apache-httpd)

The following Dockerfile will build your site and serve it using Apache httpd on port `80` with the default configuration.

Dockerfile

```docker
FROM node:lts AS build
WORKDIR /app
COPY . .
RUN npm i
RUN npm run build


FROM httpd:2.4 AS runtime
COPY --from=build /app/dist /usr/local/apache2/htdocs/
EXPOSE 80
```

Recommendation

Use this approach for simple websites that don’t need any special configuration. For more complex websites, it is recommended to use a custom configuration, either in Apache or NGINX.

#### NGINX

[Section titled “NGINX”](#nginx)

Dockerfile

```docker
FROM node:lts AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


FROM nginx:alpine AS runtime
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
```

In order to build the Dockerfile above, you’ll also need to create a configuration file for NGINX. Create a folder called `nginx` in your project’s root directory and create a file called `nginx.conf` inside.

nginx.conf

```nginx
worker_processes  1;


events {
  worker_connections  1024;
}


http {
  server {
    listen 8080;
    server_name   _;


    root   /usr/share/nginx/html;
    index  index.html index.htm;
    include /etc/nginx/mime.types;


    gzip on;
    gzip_min_length 1000;
    gzip_proxied expired no-cache no-store private auth;
    gzip_types text/plain text/css application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss text/javascript;


    error_page 404 /404.html;
    location = /404.html {
            root /usr/share/nginx/html;
            internal;
    }


    location / {
            try_files $uri $uri/index.html =404;
    }
  }
}
```

### Multi-stage build (using SSR)

[Section titled “Multi-stage build (using SSR)”](#multi-stage-build-using-ssr)

Here’s an example of a more advanced Dockerfile that, thanks to Docker’s [multi-stage builds](https://docs.docker.com/build/building/multi-stage/), optimizes the build process for your site by not reinstalling the npm dependencies when only the source code changes. This can reduce the build time even by minutes, depending on the size of your dependencies.

Dockerfile

```docker
FROM node:lts AS base
WORKDIR /app


# By copying only the package.json and package-lock.json here, we ensure that the following `-deps` steps are independent of the source code.
# Therefore, the `-deps` steps will be skipped if only the source code changes.
COPY package.json package-lock.json ./


FROM base AS prod-deps
RUN npm install --omit=dev


FROM base AS build-deps
RUN npm install


FROM build-deps AS build
COPY . .
RUN npm run build


FROM base AS runtime
COPY --from=prod-deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist


ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
CMD ["node", "./dist/server/entry.mjs"]
```

## Recipe

[Section titled “Recipe”](#recipe)

1. Build your container by running the following command in your project’s root directory. Use any name for `<your-astro-image-name>`:

   ```bash
   docker build -t <your-astro-image-name> .
   ```

   This will output an image, which you can run locally or deploy to a platform of your choice.

2. To run your image as a local container, use the following command.

   Replace `<local-port>` with an open port on your machine. Replace `<container-port>` with the port exposed by your Docker container (`4321`, `80`, or `8080` in the above examples.)

   ```bash
   docker run -p <local-port>:<container-port> <your-astro-image-name>
   ```

   You should be able to access your site at `http://localhost:<local-port>`.

3. Now that your website is successfully built and packaged in a container, you can deploy it to a cloud provider. See the [Google Cloud](/en/guides/deploy/google-cloud/#cloud-run-ssr-and-static) deployment guide for one example, and the [Deploy your app](https://docs.docker.com/language/nodejs/deploy/) page in the Docker docs.

# Dynamically import images

> Learn how to dynamically import images using Vite's import.meta.glob function.

Local [images](/en/guides/images/) must be imported into `.astro` files in order to display them. There will be times where you will want or need to dynamically import the image paths of your images instead of explicitly importing each individual image.

In this recipe, you will learn how to dynamically import your images using Vite’s `import.meta.glob` function. You will build a card component that displays the name, age, and photo of a person.

## Recipe

[Section titled “Recipe”](#recipe)

1. Create a new `assets` folder under the `src` directory and add your images inside that new folder.

   * src/

     * assets/

       * avatar-1.jpg
       * avatar-2.png
       * avatar-3.jpeg

   Note

   `assets` is a popular folder name convention for placing images but you are free to name the folder whatever you like.

2. Create a new Astro component for your card and import the `<Image />` component.

   src/components/MyCustomCardComponent.astro

   ```astro
   ---
   import { Image } from 'astro:assets';
   ---
   ```

3. Specify the `props` that your component will receive in order to display the necessary information on each card. You can optionally define their types, if you are using TypeScript in your project.

   src/components/MyCustomCardComponent.astro

   ```diff
   ---
   import { Image } from 'astro:assets';


   +interface Props {
   +   imagePath: string;
   +   altText: string;
   +   name: string;
   +   age: number;
   +}


   +const { imagePath, altText, name, age } = Astro.props;
   ---
   ```

4. Create a new `images` variable and use the `import.meta.glob` function which returns an object of all of the image paths inside the `assets` folder. You will also need to import `ImageMetadata` type to help define the type of the `images` variable.

   src/components/MyCustomCardComponent.astro

   ```diff
   ---
   +import type { ImageMetadata } from 'astro';
   import { Image } from 'astro:assets';


   interface Props {
      imagePath: string;
      altText: string;
      name: string;
      age: number;
   }


   const { imagePath, altText, name, age } = Astro.props;
   +const images = import.meta.glob<{ default: ImageMetadata }>('/src/assets/*.{jpeg,jpg,png,gif}')
   ---
   ```

5. Use the props to create the markup for your card component.

   src/components/MyCustomCardComponent.astro

   ```diff
   ---
   import type { ImageMetadata } from 'astro';
   import { Image } from 'astro:assets';


   interface Props {
      imagePath: string;
      altText: string;
      name: string;
      age: number;
   }


   const { imagePath, altText, name, age } = Astro.props;
   const images = import.meta.glob<{ default: ImageMetadata }>('/src/assets/*.{jpeg,jpg,png,gif}');
   ---
   <div class="card">
       <h2>{name}</h2>
       <p>Age: {age}</p>
       +<Image src={} alt={altText} />
   </div>
   ```

6. Inside the `src` attribute, pass in the `images` object and use bracket notation for the image path. Then make sure to invoke the glob function.

   Since you are accessing the `images` object which has an unknown type, you should also `throw` an error in case an invalid file path is passed as a prop.

   src/components/MyCustomCardComponent.astro

   ```diff
   ---
   import type { ImageMetadata } from 'astro';
   import { Image } from 'astro:assets';


   interface Props {
      imagePath: string;
      altText: string;
      name: string;
      age: number;
   }


   const { imagePath, altText, name, age } = Astro.props;
   const images = import.meta.glob<{ default: ImageMetadata }>('/src/assets/*.{jpeg,jpg,png,gif}');
   +if (!images[imagePath]) throw new Error(`"${imagePath}" does not exist in glob: "src/assets/*.{jpeg,jpg,png,gif}"`);
   ---
   <div class="card">
       <h2>{name}</h2>
       <p>Age: {age}</p>
       <Image src={images[imagePath]()} alt={altText} />
   </div>
   ```

   Note

   `images` is an object that contains all of the image paths inside the `assets` folder.

   ```js
   const images = {
     './assets/avatar-1.jpg': () => import('./assets/avatar-1.jpg'),
     './assets/avatar-2.png': () => import('./assets/avatar-2.png'),
     './assets/avatar-3.jpeg': () => import('./assets/avatar-3.jpeg')
   }
   ```

   The `imagePath` prop is a string that contains the path to the image that you want to display. The `import.meta.glob()` is doing the work of finding the image path that matches the `imagePath` prop and handling the import for you.

7. Import and use the card component inside an Astro page, passing in the values for the `props`.

   src/pages/index.astro

   ```astro
   ---
   import MyCustomCardComponent from '../components/MyCustomCardComponent.astro';
   ---
   <MyCustomCardComponent
       imagePath="/src/assets/avatar-1.jpg"
       altText="A headshot of Priya against a brick wall background."
       name="Priya"
       age={25}
   />
   ```

# Add icons to external links

> Learn how to install a rehype plugin to add icons to external links in your Markdown files.

Using a rehype plugin, you can identify and modify links in your Markdown files that point to external sites. This example adds icons to the end of each external link, so that visitors will know they are leaving your site.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An Astro project using Markdown for content pages.

## Recipe

[Section titled “Recipe”](#recipe)

1. Install the `rehype-external-links` plugin.

   * npm

     ```shell
     npm install rehype-external-links
     ```

   * pnpm

     ```shell
     pnpm add rehype-external-links
     ```

   * Yarn

     ```shell
     yarn add rehype-external-links
     ```

2. Import the plugin into your `astro.config.mjs` file.

   Pass `rehypeExternalLinks` to the `rehypePlugins` array, along with an options object that includes a content property. Set this property’s `type` to `text` if you want to add plain text to the end of the link. To add HTML to the end of the link instead, set the property `type` to `raw`.

   ```ts
   // ...
   import rehypeExternalLinks from 'rehype-external-links';


   export default defineConfig({
     // ...
     markdown: {
       rehypePlugins: [
         [
           rehypeExternalLinks,
           {
             content: { type: 'text', value: ' 🔗' }
           }
         ],
       ]
     },
   });
   ```

   Note

   The value of the `content` property is [not represented in the accessibility tree](https://developer.mozilla.org/en-US/docs/Web/CSS/content#accessibility_concerns). As such, it’s best to make clear that the link is external in the surrounding content, rather than relying on the icon alone.

## Resources

[Section titled “Resources”](#resources)

* [rehype-external-links](https://www.npmjs.com/package/rehype-external-links)

# Add i18n features

> Use dynamic routing and content collections to add internationalization support to your Astro site.

In this recipe, you will learn how to use content collections and dynamic routing to build your own internationalization (i18n) solution and serve your content in different languages.

Tip

In v4.0, Astro added built-in support for i18n routing that allows you to configure default and supported languages and includes valuable helper functions to assist you in serving an international audience. If you want to use this instead, see our [internationalization guide](/en/guides/internationalization/) to learn about these features.

This example serves each language at its own subpath, e.g. `example.com/en/blog` for English and `example.com/fr/blog` for French.

If you prefer the default language to not be visible in the URL unlike other languages, there are [instructions to hide the default language](/en/recipes/i18n/#hide-default-language-in-the-url) below.

See the [resources section](#resources) for external links to related topics such as right-to-left (RTL) styling and choosing language tags.

## Recipe

[Section titled “Recipe”](#recipe)

### Set up pages for each language

[Section titled “Set up pages for each language”](#set-up-pages-for-each-language)

1. Create a directory for each language you want to support. For example, `en/` and `fr/` if you are supporting English and French:

   * src/

     * pages/

       * **en/**

         * about.astro
         * index.astro

       * **fr/**

         * about.astro
         * index.astro

       * index.astro

2. Set up `src/pages/index.astro` to redirect to your default language.

   * Static

     src/pages/index.astro

     ```astro
     <meta http-equiv="refresh" content="0;url=/en/" />
     ```

     This approach uses a [meta refresh](https://en.wikipedia.org/wiki/Meta_refresh) and will work however you deploy your site. Some static hosts also let you configure server redirects with a custom configuration file. See your deploy platform’s documentation for more details.

   * On demand

     If you are using an SSR adapter, you can use [`Astro.redirect`](/en/guides/routing/#dynamic-redirects) to redirect to the default language on the server.

     src/pages/index.astro

     ```astro
     ---
     return Astro.redirect('/en/');
     ---
     ```

### Use collections for translated content

[Section titled “Use collections for translated content”](#use-collections-for-translated-content)

1. Create a folder in `src/content/` for each type of content you want to include and add subdirectories for each supported language. For example, to support English and French blog posts:

   * src/

     * content/

       * blog/

         * **en/** Blog posts in English

           * post-1.md
           * post-2.md

         * **fr/** Blog posts in French

           * post-1.md
           * post-2.md

2. Create a `src/content.config.ts` file and export a collection for each type of content.

   src/content.config.ts

   ```ts
   import { defineCollection, z } from 'astro:content';


   const blogCollection = defineCollection({
     schema: z.object({
       title: z.string(),
       author: z.string(),
       date: z.date()
     })
   });


   export const collections = {
     'blog': blogCollection
   };
   ```

   Read more about [Content Collections](/en/guides/content-collections/).

3. Use [dynamic routes](/en/guides/routing/#dynamic-routes) to fetch and render content based on a `lang` and a `slug` parameter.

   * Static

     In static rendering mode, use `getStaticPaths` to map each content entry to a page:

     src/pages/\[lang]/blog/\[...slug].astro

     ```astro
     ---
     import { getCollection, render } from 'astro:content';


     export async function getStaticPaths() {
       const pages = await getCollection('blog');


       const paths = pages.map(page => {
         const [lang, ...slug] = page.id.split('/');
         return { params: { lang, slug: slug.join('/') || undefined }, props: page };
       });


       return paths;
     }


     const { lang, slug } = Astro.params;
     const page = Astro.props;
     const formattedDate = page.data.date.toLocaleString(lang);
     const { Content } = await render(page);
     ---
     <h1>{page.data.title}</h1>
     <p>by {page.data.author} • {formattedDate}</p>
     <Content/>
     ```

   * On demand

     In [SSR mode](/en/guides/on-demand-rendering/), fetch the requested entry directly:

     src/pages/\[lang]/blog/\[...slug].astro

     ```astro
     ---
     import { getEntry, render } from 'astro:content';


     const { lang, slug } = Astro.params;
     const page = await getEntry('blog', `${lang}/${slug}`);


     if (!page) {
       return Astro.redirect('/404');
     }


     const formattedDate = page.data.date.toLocaleString(lang);
     const { Content, headings } = await render(page);
     ---
     <h1>{page.data.title}</h1>
     <p>by {page.data.author} • {formattedDate}</p>
     <Content/>
     ```

   Read more about [dynamic routing](/en/guides/routing/#dynamic-routes).

   Date formatting

   The example above uses the built-in [`toLocaleString()` date-formatting method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString) to create a human-readable string from the frontmatter date. This ensures the date and time are formatted to match the user’s language.

### Translate UI strings

[Section titled “Translate UI strings”](#translate-ui-strings)

Create dictionaries of terms to translate the labels for UI elements around your site. This allows your visitors to experience your site fully in their language.

1. Create a `src/i18n/ui.ts` file to store your translation strings:

   src/i18n/ui.ts

   ```ts
   export const languages = {
     en: 'English',
     fr: 'Français',
   };


   export const defaultLang = 'en';


   export const ui = {
     en: {
       'nav.home': 'Home',
       'nav.about': 'About',
       'nav.twitter': 'Twitter',
     },
     fr: {
       'nav.home': 'Accueil',
       'nav.about': 'À propos',
     },
   } as const;
   ```

2. Create two helper functions: one to detect the page language based on the current URL, and one to get translations strings for different parts of the UI in `src/i18n/utils.ts`:

   src/i18n/utils.ts

   ```js
   import { ui, defaultLang } from './ui';


   export function getLangFromUrl(url: URL) {
     const [, lang] = url.pathname.split('/');
     if (lang in ui) return lang as keyof typeof ui;
     return defaultLang;
   }


   export function useTranslations(lang: keyof typeof ui) {
     return function t(key: keyof typeof ui[typeof defaultLang]) {
       return ui[lang][key] || ui[defaultLang][key];
     }
   }
   ```

   Did you notice?

   In step 1, the `nav.twitter` string was not translated to French. You may not want every term translated, such as proper names or common industry terms. The `useTranslations` helper will return the default language’s value if a key is not translated. In this example, French users will also see “Twitter” in the nav bar.

3. Import the helpers where needed and use them to choose the UI string that corresponds to the current language. For example, a nav component might look like:

   src/components/Nav.astro

   ```astro
   ---
   import { getLangFromUrl, useTranslations } from '../i18n/utils';


   const lang = getLangFromUrl(Astro.url);
   const t = useTranslations(lang);
   ---
   <ul>
       <li>
           <a href={`/${lang}/home/`}>
             {t('nav.home')}
           </a>
       </li>
       <li>
           <a href={`/${lang}/about/`}>
             {t('nav.about')}
           </a>
       </li>
       <li>
           <a href="https://twitter.com/astrodotbuild">
             {t('nav.twitter')}
           </a>
       </li>
   </ul>
   ```

4. Each page must have a `lang` attribute on the `<html>` element that matches the language on the page. In this example, a [reusable layout](/en/basics/layouts/) extracts the language from the current route:

   src/layouts/Base.astro

   ```astro
   ---
   import { getLangFromUrl } from '../i18n/utils';


   const lang = getLangFromUrl(Astro.url);
   ---
   <html lang={lang}>
       <head>
           <meta charset="utf-8" />
           <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
           <meta name="viewport" content="width=device-width" />
           <title>Astro</title>
       </head>
       <body>
           <slot />
       </body>
   </html>
   ```

   You can then use this base layout to ensure that pages use the correct `lang` attribute automatically.

   src/pages/en/about.astro

   ```astro
   ---
   import Base from '../../layouts/Base.astro';
   ---
   <Base>
       <h1>About me</h1>
       ...
   </Base>
   ```

### Let users switch between languages

[Section titled “Let users switch between languages”](#let-users-switch-between-languages)

Create links to the different languages you support so users can choose the language they want to read your site in.

1. Create a component to show a link for each language:

   src/components/LanguagePicker.astro

   ```astro
   ---
   import { languages } from '../i18n/ui';
   ---
   <ul>
     {Object.entries(languages).map(([lang, label]) => (
       <li>
         <a href={`/${lang}/`}>{label}</a>
       </li>
     ))}
   </ul>
   ```

2. Add `<LanguagePicker />` to your site so it is shown on every page. The example below adds it to the site footer in a base layout:

   src/layouts/Base.astro

   ```diff
   ---
   +import LanguagePicker from '../components/LanguagePicker.astro';
   import { getLangFromUrl } from '../i18n/utils';


   const lang = getLangFromUrl(Astro.url);
   ---
   <html lang={lang}>
       <head>
           <meta charset="utf-8" />
           <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
           <meta name="viewport" content="width=device-width" />
           <title>Astro</title>
       </head>
       <body>
           <slot />
           <footer>
             +<LanguagePicker />
           </footer>
       </body>
   </html>
   ```

### Hide default language in the URL

[Section titled “Hide default language in the URL”](#hide-default-language-in-the-url)

1. Create a directory for each language except the default language. For example, store your default language pages directly in `pages/`, and your translated pages in `fr/`:

   * src/

     * pages/

       * about.astro

       * index.astro

       * **fr/**

         * about.astro
         * index.astro

2. Add another line to the `src/i18n/ui.ts` file to toggle the feature:

   src/i18n/ui.ts

   ```ts
   export const showDefaultLang = false;
   ```

3. Add a helper function to `src/i18n/utils.ts`, to translate paths based on the current language:

   src/i18n/utils.ts

   ```js
   import { ui, defaultLang, showDefaultLang } from './ui';


   export function useTranslatedPath(lang: keyof typeof ui) {
     return function translatePath(path: string, l: string = lang) {
       return !showDefaultLang && l === defaultLang ? path : `/${l}${path}`
     }
   }
   ```

4. Import the helper where needed. For example, a `nav` component might look like:

   src/components/Nav.astro

   ```astro
   ---
   import { getLangFromUrl, useTranslations, useTranslatedPath } from '../i18n/utils';


   const lang = getLangFromUrl(Astro.url);
   const t = useTranslations(lang);
   const translatePath = useTranslatedPath(lang);
   ---
   <ul>
       <li>
           <a href={translatePath('/home/')}>
             {t('nav.home')}
           </a>
       </li>
       <li>
           <a href={translatePath('/about/')}>
             {t('nav.about')}
           </a>
       </li>
       <li>
           <a href="https://twitter.com/astrodotbuild">
             {t('nav.twitter')}
           </a>
       </li>
   </ul>
   ```

5. The helper function can also be used to translate paths for a specific language. For example, when users switch between languages:

   src/components/LanguagePicker.astro

   ```astro
   ---
   import { languages } from '../i18n/ui';
   import { getLangFromUrl, useTranslatedPath } from '../i18n/utils';


   const lang = getLangFromUrl(Astro.url);
   const translatePath = useTranslatedPath(lang);
   ---
   <ul>
     {Object.entries(languages).map(([lang, label]) => (
       <li>
         <a href={translatePath('/', lang)}>{label}</a>
       </li>
     ))}
   </ul>
   ```

### Translate Routes

[Section titled “Translate Routes”](#translate-routes)

Translate the routes of your pages for each language.

1. Add route mappings to `src/i18n/ui.ts`:

   src/i18n/ui.ts

   ```ts
   export const routes = {
     de: {
       'services': 'leistungen',
     },
     fr: {
       'services': 'prestations-de-service',
     },
   }
   ```

2. Update the `useTranslatedPath` helper function in `src/i18n/utils.ts` to add router translation logic.

   src/i18n/utils.ts

   ```js
   import { ui, defaultLang, showDefaultLang, routes } from './ui';


   export function useTranslatedPath(lang: keyof typeof ui) {
     return function translatePath(path: string, l: string = lang) {
       const pathName = path.replaceAll('/', '')
       const hasTranslation = defaultLang !== l && routes[l] !== undefined && routes[l][pathName] !== undefined
       const translatedPath = hasTranslation ? '/' + routes[l][pathName] : path


       return !showDefaultLang && l === defaultLang ? translatedPath : `/${l}${translatedPath}`
     }
   }
   ```

3. Create a helper function to get the route, if it exists based on the current URL, in `src/i18n/utils.ts`:

   src/i18n/utils.ts

   ```js
   import { ui, defaultLang, showDefaultLang, routes } from './ui';


   export function getRouteFromUrl(url: URL): string | undefined {
     const pathname = new URL(url).pathname;
     const parts = pathname?.split('/');
     const path = parts.pop() || parts.pop();


     if (path === undefined) {
       return undefined;
     }


     const currentLang = getLangFromUrl(url);


     if (defaultLang === currentLang) {
       const route = Object.values(routes)[0];
       return route[path] !== undefined ? route[path] : undefined;
     }


     const getKeyByValue = (obj: Record<string, string>, value: string): string | undefined  => {
         return Object.keys(obj).find((key) => obj[key] === value);
     }


     const reversedKey = getKeyByValue(routes[currentLang], path);


     if (reversedKey !== undefined) {
       return reversedKey;
     }


     return undefined;
   }
   ```

4. The helper function can be used to get a translated route. For example, when no translated route is defined, the user will be redirected to the home page:

   src/components/LanguagePicker.astro

   ```astro
   ---
   import { languages } from '../i18n/ui';
   import { getRouteFromUrl, useTranslatedPath } from '../i18n/utils';


   const route = getRouteFromUrl(Astro.url);
   ---
   <ul>
     {Object.entries(languages).map(([lang, label]) => {
       const translatePath = useTranslatedPath(lang);
       return (
         <li>
           <a href={translatePath(`/${route ? route : ''}`)}>{label}</a>
         </li>
       )
     })}
   </ul>
   ```

## Resources

[Section titled “Resources”](#resources)

* [Choosing a Language Tag](https://www.w3.org/International/questions/qa-choosing-language-tags)
* [Right-to-left (RTL) Styling 101](https://rtlstyling.com/)

## Community libraries

[Section titled “Community libraries”](#community-libraries)

* [astro-i18next](https://github.com/yassinedoghri/astro-i18next) — An Astro integration for i18next including some utility components.
* [astro-i18n](https://github.com/alexandre-fernandez/astro-i18n) — A TypeScript-first internationalization library for Astro.
* [astro-i18n-aut](https://github.com/jlarmstrongiv/astro-i18n-aut) — An Astro integration for i18n that supports the `defaultLocale` without page generation. The integration is adapter agnostic and UI framework agnostic.
* [astro-react-i18next](https://github.com/jeremyxgo/astro-react-i18next) — An Astro integration that seamlessly enables the use of i18next and react-i18next in React components on Astro websites.
* [paraglide](https://inlang.com/c/astro) — A fully type-safe i18n library specifically designed for partial hydration patterns like Astro islands.
* [astro-loader-i18n](https://github.com/openscript/astro-loader-i18n) — An Astro glob content loader for i18n files and folder structures supporting the translation of routes.


---

**Navigation:** [← Previous](./09-testing.md) | [Index](./index.md) | [Next →](./11-create-a-dev-toolbar-app.md)
