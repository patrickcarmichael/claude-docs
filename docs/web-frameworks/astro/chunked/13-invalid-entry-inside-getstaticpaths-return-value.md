**Navigation:** [← Previous](./12-configuration-reference.md) | [Index](./index.md) | [Next →](./14-astro-integration-api.md)

---

# Invalid entry inside getStaticPath's return value

> **InvalidGetStaticPathsEntry**: Invalid entry returned by getStaticPaths. Expected an object, got `ENTRY_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects. In most cases, this error happens because an array of array was returned. Using [`.flatMap()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flatMap) or a [`.flat()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat) call may be useful.

pages/blog/\[id].astro

```ts
export async function getStaticPaths() {
  return [ // <-- Array
    { params: { slug: "blog" } }, // <-- Object
    { params: { slug: "about" } }
  ];
}
```

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)

# Invalid value returned by getStaticPaths.

> **InvalidGetStaticPathsReturn**: Invalid type returned by `getStaticPaths`. Expected an `array`, got `RETURN_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths`’s return value must be an array of objects.

pages/blog/\[id].astro

```ts
export async function getStaticPaths() {
  return [ // <-- Array
    { params: { slug: "blog" } },
    { params: { slug: "about" } }
  ];
}
```

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

# Invalid glob pattern.

> **InvalidGlob**: Invalid glob pattern: `GLOB_PATTERN`. Glob patterns must start with ’./’, ‘../’ or ’/‘.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an invalid glob pattern. This is often caused by the glob pattern not being a valid file path.

**See Also:**

* [Glob Patterns](/en/guides/imports/#glob-patterns)

# Error while loading image service.

> **InvalidImageService**: There was an error loading the configured image service. Please see the stack trace for more information.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

There was an error while loading the configured image service. This can be caused by various factors, such as your image service not properly exporting a compatible object in its default export, or an incorrect path.

If you believe that your service is properly configured and this error is wrong, please [open an issue](https://astro.build/issues/).

**See Also:**

* [Image Service API](/en/reference/image-service-reference/)

# Invalid prerender export.

> **Example error messages:**\
> InvalidPrerenderExport: A `prerender` export has been detected, but its value cannot be statically analyzed.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `prerender` feature only supports a subset of valid JavaScript — be sure to use exactly `export const prerender = true` so that our compiler can detect this directive at build time. Variables, `let`, and `var` declarations are not supported.

# You attempted to rewrite a 404 inside a static page, and this isn't allowed.

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **InvalidRewrite404**: Rewriting a 404 is only allowed inside on-demand pages.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The user tried to rewrite a 404 page inside a static page.

# Error in live content config.

> **Example error message:**\
> The schema cannot be a function for live collections. Please use a schema object instead. Check your collection definitions in your live content config file.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Error in live content config.

**See Also:**

* [Experimental live content](/en/reference/experimental-flags/live-content-collections/)

# Local images must be imported.

> **LocalImageUsedWrongly**: `Image`’s and `getImage`’s `src` parameter must be an imported image or an URL, it cannot be a string filepath. Received `IMAGE_FILE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

When using the default image services, `Image`’s and `getImage`’s `src` parameter must be either an imported image or an URL, it cannot be a string of a filepath.

For local images from content collections, you can use the [image() schema helper](/en/guides/images/#images-in-content-collections) to resolve the images.

```astro
---
import { Image } from "astro:assets";
import myImage from "../my_image.png";
---


<!-- GOOD: `src` is the full imported image. -->
<Image src={myImage} alt="Cool image" />


<!-- GOOD: `src` is a URL. -->
<Image src="https://example.com/my_image.png" alt="Cool image" />


<!-- BAD: `src` is an image's `src` path instead of the full image object. -->
<Image src={myImage.src} alt="Cool image" />


<!-- BAD: `src` is a string filepath. -->
<Image src="../my_image.png" alt="Cool image" />
```

**See Also:**

* [Images](/en/guides/images/)

# Value assigned to locals is not accepted.

> **LocalsNotAnObject**: `locals` can only be assigned to an object. Other values like numbers, strings, etc. are not accepted.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when `locals` is overwritten with something that is not an object

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware((context, next) => {
  context.locals = 1541;
  return next();
});
```

# Astro.locals is not serializable

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **LocalsNotSerializable**: The information stored in `Astro.locals` for the path “`HREF`” is not serializable. Make sure you store only serializable data. (E03034)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when a user attempts to store something that is not serializable in `locals`.

For example:

```ts
import {defineMiddleware} from "astro/middleware";
export const onRequest = defineMiddleware((context, next) => {
  context.locals = {
    foo() {
      alert("Hello world!")
    }
  };
  return next();
});
```

# locals must not be reassigned.

> **LocalsReassigned**: `locals` can not be assigned directly.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when a value is being set as the `locals` field on the Astro global or context.

# Content collection frontmatter invalid.

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **Example error message:**\
> Could not parse frontmatter in **blog** → **post.md**\
> “title” is required.\
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A Markdown document’s frontmatter in `src/content/` does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content/config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

# Failed to parse Markdown frontmatter.

> **Example error messages:**\
> can not read an implicit mapping pair; a colon is missed\
> unexpected end of the stream within a double quoted scalar\
> can not read a block mapping entry; a multiline key may not be an implicit key

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an error while parsing the frontmatter of your Markdown file. This is often caused by a mistake in the syntax, such as a missing colon or a missing end quote.

# Image not found.

Deprecated

This error is no longer Markdown specific and as such, as been replaced by `ImageNotFound`

> Could not find requested image `IMAGE_PATH` at `FULL_IMAGE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find an image you included in your Markdown content. Usually, this is simply caused by a typo in the path.

Images in Markdown are relative to the current file. To refer to an image that is located in the same folder as the `.md` file, the path should start with `./`

**See Also:**

* [Images](/en/guides/images/)

# MDX integration missing.

> **MdxIntegrationMissingError**: Unable to render FILE. Ensure that the `@astrojs/mdx` integration is installed.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Unable to find the official `@astrojs/mdx` integration. This error is raised when using MDX files without an MDX integration installed.

**See Also:**

* [MDX installation and usage](/en/guides/integrations-guide/mdx/)

# Can't load the middleware.

> **MiddlewareCantBeLoaded**: An unknown error was thrown while loading your middleware.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware throws an error while attempting to loading it.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
throw new Error("Error thrown while loading the middleware.")
export const onRequest = defineMiddleware(() => {
  return "string"
});
```

# The middleware didn't return a Response.

> **MiddlewareNoDataOrNextCalled**: Make sure your middleware returns a `Response` object, either directly or by returning the `Response` from calling the `next` function.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when the middleware does not return any data or call the `next` function.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware((context, _) => {
  // doesn't return anything or call `next`
  context.locals.someData = false;
});
```

# The middleware returned something that is not a Response object.

> **MiddlewareNotAResponse**: Any data returned from middleware must be a valid `Response` object.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when middleware returns something that is not a `Response` object.

For example:

```ts
import {defineMiddleware} from "astro:middleware";
export const onRequest = defineMiddleware(() => {
  return "string"
});
```

# Missing image dimensions

> Missing width and height attributes for `IMAGE_URL`. When using remote images, both dimensions are required in order to avoid cumulative layout shift (CLS).

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

For remote images, `width` and `height` cannot automatically be inferred from the original file. To avoid cumulative layout shift (CLS), either specify these two properties, or set [`inferSize`](/en/reference/modules/astro-assets/#infersize) to `true` to fetch a remote image’s original dimensions.

If your image is inside your `src` folder, you probably meant to import it instead. See [the Imports guide for more information](/en/guides/imports/#other-assets).

**See Also:**

* [Images](/en/guides/images/)
* [Image component#width-and-height-required](/en/reference/modules/astro-assets/#width-and-height-required-for-images-in-public)

# Index page not found.

> **MissingIndexForInternationalization**: Could not find index page. A root index page is required in order to create a redirect to the index URL of the default locale. (`/DEFAULT_LOCALE`)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find the index URL of your website. An index page is required so that Astro can create a redirect from the main index page to the localized index page of the default locale when using [`i18n.routing.prefixDefaultLocale`](/en/reference/configuration-reference/#i18nroutingprefixdefaultlocale).

**See Also:**

* [Internationalization](/en/guides/internationalization/#routing)
* [`i18n.routing` Configuration Reference](/en/reference/configuration-reference/#i18nrouting)

# The provided locale does not exist.

> **MissingLocale**: The locale/path `LOCALE` does not exist in the configured `i18n.locales`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro can’t find the requested locale. All supported locales must be configured in [i18n.locales](/en/reference/configuration-reference/#i18nlocales) and have corresponding directories within `src/pages/`.

# Missing value for client:media directive.

> **MissingMediaQueryDirective**: Media query not provided for `client:media` directive. A media query similar to `client:media="(max-width: 600px)"` must be provided

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries) parameter is required when using the `client:media` directive.

```astro
<Counter client:media="(max-width: 640px)" />
```

**See Also:**

* [`client:media`](/en/reference/directives-reference/#clientmedia)

# Enabled manual internationalization routing without having a middleware.

> **MissingMiddlewareForInternationalization**: Your configuration setting `i18n.routing: 'manual'` requires you to provide your own i18n `middleware` file.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro throws an error if the user enables manual routing, but it doesn’t have a middleware file.

# Could not find Sharp.

> **MissingSharp**: Could not find Sharp. Please install Sharp (`sharp`) manually into your project or migrate to another image service.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Sharp is the default image service used for `astro:assets`. When using a [strict package manager](https://pnpm.io/pnpm-vs-npm#npms-flat-tree) like pnpm, Sharp must be installed manually into your project in order to use image processing.

If you are not using `astro:assets` for image processing, and do not wish to install Sharp, you can configure the following passthrough image service that does no processing:

```js
import { defineConfig, passthroughImageService } from "astro/config";
export default defineConfig({
 image: {
   service: passthroughImageService(),
 },
});
```

**See Also:**

* [Default Image Service](/en/guides/images/#default-image-service)
* [Image Services API](/en/reference/image-service-reference/)

# Content and data cannot be in same collection.

> **MixedContentDataCollectionError**: **COLLECTION\_NAME** contains a mix of content and data entries. All entries must be of the same type.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A legacy content collection cannot contain a mix of content and data entries. You must store entries in separate collections by type.

**See Also:**

* [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

# Cannot use Server-side Rendering without an adapter.

> **NoAdapterInstalled**: Cannot use server-rendered pages without an adapter. Please install and configure the appropriate server adapter for your final deployment.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

To use server-side rendering, an adapter needs to be installed so Astro knows how to generate the proper output for your targeted deployment platform.

**See Also:**

* [Server-side Rendering](/en/guides/on-demand-rendering/)

# Cannot use Server Islands without an adapter.

> **NoAdapterInstalledServerIslands**: Cannot use server islands without an adapter. Please install and configure the appropriate server adapter for your final deployment.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

To use server islands, the same constraints exist as for sever-side rendering, so an adapter is needed.

**See Also:**

* [On-demand Rendering](/en/guides/on-demand-rendering/)

# No client entrypoint specified in renderer.

> **NoClientEntrypoint**: `COMPONENT_NAME` component has a `client:CLIENT_DIRECTIVE` directive, but no client entrypoint was provided by `RENDERER_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro tried to hydrate a component on the client, but the renderer used does not provide a client entrypoint to use to hydrate.

**See Also:**

* [addRenderer option](/en/reference/integrations-reference/#addrenderer-option)
* [Hydrating framework components](/en/guides/framework-components/#hydrating-interactive-components)

# Missing hint on client:only directive.

> **NoClientOnlyHint**: Unable to render `COMPONENT_NAME`. When using the `client:only` hydration strategy, Astro needs a hint to use the correct renderer.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`client:only` components are not run on the server, as such Astro does not know (and cannot guess) which renderer to use and require a hint. Like such:

```astro
  <SomeReactComponent client:only="react" />
```

**See Also:**

* [`client:only`](/en/reference/directives-reference/#clientonly)

# Could not process image metadata.

> Could not process image metadata for `IMAGE_PATH`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not process the metadata of an image you imported. This is often caused by a corrupted or malformed image and re-exporting the image from your image editor may fix this issue.

**See Also:**

* [Images](/en/guides/images/)

# No import found for component.

> **NoMatchingImport**: Could not render `COMPONENT_NAME`. No matching import has been found for `COMPONENT_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

No import statement was found for one of the components. If there is an import statement, make sure you are using the same identifier in both the imports and the component usage.

# No matching renderer found.

> Unable to render `COMPONENT_NAME`. There are `RENDERER_COUNT` renderer(s) configured in your `astro.config.mjs` file, but none were able to server-side render `COMPONENT_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

None of the installed integrations were able to render the component you imported. Make sure to install the appropriate integration for the type of component you are trying to include in your page.

For JSX / TSX files, [@astrojs/react](/en/guides/integrations-guide/react/), [@astrojs/preact](/en/guides/integrations-guide/preact/) or [@astrojs/solid-js](/en/guides/integrations-guide/solid-js/) can be used. For Vue and Svelte files, the [@astrojs/vue](/en/guides/integrations-guide/vue/) and [@astrojs/svelte](/en/guides/integrations-guide/svelte/) integrations can be used respectively

**See Also:**

* [Frameworks components](/en/guides/framework-components/)
* [UI Frameworks](/en/guides/integrations-guide/#official-integrations)

# No static path found for requested path.

> **NoMatchingStaticPathFound**: A `getStaticPaths()` route pattern was matched, but no matching static path was found for requested path `PATH_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A [dynamic route](/en/guides/routing/#dynamic-routes) was matched, but no corresponding path was found for the requested parameters. This is often caused by a typo in either the generated or the requested path.

**See Also:**

* [getStaticPaths()](/en/reference/routing-reference/#getstaticpaths)

# Prerendered routes aren't supported when internationalization domains are enabled.

> **NoPrerenderedRoutesWithDomains**: Static pages aren’t yet supported with multiple domains. To enable this feature, you must disable prerendering for the page COMPONENT

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Static pages aren’t yet supported with i18n domains. If you wish to enable this feature, you have to disable prerendering.

# Invalid type returned by Astro page.

> Route returned a `RETURNED_VALUE`. Only a Response can be returned from Astro files.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Only instances of [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) can be returned inside Astro files.

pages/login.astro

```astro
---
return new Response(null, {
 status: 404,
 statusText: 'Not found'
});


// Alternatively, for redirects, Astro.redirect also returns an instance of Response
return Astro.redirect('/login');
---
```

**See Also:**

* [Response](/en/guides/on-demand-rendering/#response)

# Page number param not found.

> **PageNumberParamNotFound**: \[paginate()] page number param `PARAM_NAME` not found in your filepath.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The page number parameter was not found in your filepath.

**See Also:**

* [Pagination](/en/guides/routing/#pagination)

# Astro.clientAddress cannot be used inside prerendered routes.

> **PrerenderClientAddressNotAvailable**: `Astro.clientAddress` cannot be used inside prerendered route NAME

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.clientAddress` property cannot be used inside prerendered routes.

**See Also:**

* [On-demand rendering](/en/guides/on-demand-rendering/)
* [Astro.clientAddress](/en/reference/api-reference/#clientaddress)

# Prerendered dynamic endpoint has path collision.

> **PrerenderDynamicEndpointPathCollide**: Could not render `PATHNAME` with an `undefined` param as the generated path will collide during prerendering. Prevent passing `undefined` as `params` for the endpoint’s `getStaticPaths()` function, or add an additional extension to the endpoint’s filename.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The endpoint is prerendered with an `undefined` param so the generated path will collide with another route.

If you cannot prevent passing `undefined`, then an additional extension can be added to the endpoint file name to generate the file with a different name. For example, renaming `pages/api/[slug].ts` to `pages/api/[slug].json.ts`.

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

# Prerendered route generates the same path as another route.

> **PrerenderRouteConflict**: Could not render `PATHNAME` from route `THIS_ROUTE` as it conflicts with higher priority route `WINNING_ROUTE`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Two prerendered routes generate the same path, resulting in a collision. A static path can only be generated by one route.

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

# A redirect must be given a location with the Location header.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A redirect must be given a location with the `Location` header.

**See Also:**

* [Astro.redirect](/en/reference/api-reference/#redirect)

# Attempted to render an undefined content collection entry.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro tried to render a content collection entry that was undefined. This can happen if you try to render an entry that does not exist.

# Invalid slot name.

> **ReservedSlotName**: Unable to create a slot named `SLOT_NAME`. `SLOT_NAME` is a reserved slot name. Please update the name of this slot.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Certain words cannot be used for slot names due to being already used internally.

**See Also:**

* [Named slots](/en/basics/astro-components/#named-slots)

# Unable to set response.

> **ResponseSentError**: The response has already been sent to the browser and cannot be altered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Making changes to the response, such as setting headers, cookies, and the status code can only be done in [page components](/en/basics/astro-pages/).

**See Also:**

* [HTML streaming](/en/guides/on-demand-rendering/#html-streaming)

# Astro couldn't find the route to rewrite, or if was found but it emitted an error during the rendering phase.

Deprecated

This error cannot be emitted by Astro anymore

> **RewriteEncounteredAnError**: The route ROUTE that you tried to render doesn’t exist, or it emitted an error during the rendering phase. STACK ? STACK : ”.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The user tried to rewrite using a route that doesn’t exist, or it emitted a runtime error during its rendering phase.

# Cannot use Astro.rewrite after the request body has been read

> **RewriteWithBodyUsed**: Astro.rewrite() cannot be used if the request body has already been read. If you need to read the body, first clone the request.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` cannot be used if the request body has already been read. If you need to read the body, first clone the request. For example:

```js
const data = await Astro.request.clone().formData();


Astro.rewrite("/target")
```

**See Also:**

* [Request.clone()](https://developer.mozilla.org/en-US/docs/Web/API/Request/clone)
* [Astro.rewrite](/en/reference/api-reference/#rewrite)

# Route not found.

> **RouteNotFound**: Astro could not find a route that matches the one you requested.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro couldn’t find a route matching the one provided by the user

# Module is only available server-side

> **ServerOnlyModule**: The “NAME” module is only available server-side.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

This module is only available server-side.

# Session storage was enabled but not configured.

Deprecated

This error was removed in Astro 5.7, when the Sessions feature stopped being experimental.

> The `experimental.session` flag was set to `true`, but no storage was configured. Either configure the storage manually or use an adapter that provides session storage.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when session storage is enabled but not configured.

**See Also:**

* [Sessions](/en/guides/sessions/)

# Session flag not set

Deprecated

This error was removed in Astro 5.7, when the Sessions feature stopped being experimental.

> Session config was provided without enabling the `experimental.session` flag

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when session storage is configured but the `experimental.session` flag is not enabled.

**See Also:**

* [Sessions](/en/guides/sessions/)

# Session storage could not be initialized.

> Error when initializing session storage with driver `DRIVER`. `ERROR`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when the session storage could not be initialized.

**See Also:**

* [Sessions](/en/guides/sessions/)

# Session data could not be saved.

> Error when saving session data with driver `DRIVER`. `ERROR`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when the session data could not be saved.

**See Also:**

* [Sessions](/en/guides/sessions/)

# Sessions cannot be used with an adapter that doesn't support server output.

Deprecated

This error was removed in Astro 5.7, when the Sessions feature stopped being experimental.

> **SessionWithoutSupportedAdapterOutputError**: Sessions require an adapter that supports server output. The adapter must set `"server"` in the `buildOutput` adapter feature.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Your adapter must support server output to use sessions.

**See Also:**

* [Sessions](/en/guides/sessions/)

# Astro.clientAddress is not available in prerendered pages.

> **StaticClientAddressNotAvailable**: `Astro.clientAddress` is only available on pages that are server-rendered.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.clientAddress` property is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To get the user’s IP address in static mode, different APIs such as [Ipify](https://www.ipify.org/) can be used in a [Client-side script](/en/guides/client-side-scripts/) or it may be possible to get the user’s IP using a serverless function hosted on your hosting provider.

**See Also:**

* [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
* [Astro.clientAddress](/en/reference/api-reference/#clientaddress)

# Astro.redirect is not available in static mode.

Deprecated

Deprecated since version 2.6.

> **StaticRedirectNotAvailable**: Redirects are only available when using `output: 'server'` or `output: 'hybrid'`. Update your Astro config if you need SSR features.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `Astro.redirect` function is only available when [Server-side rendering](/en/guides/on-demand-rendering/) is enabled.

To redirect on a static website, the [meta refresh attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) can be used. Certain hosts also provide config-based redirects (ex: [Netlify redirects](https://docs.netlify.com/routing/redirects/)).

**See Also:**

* [Enabling SSR in Your Project](/en/guides/on-demand-rendering/)
* [Astro.redirect](/en/reference/api-reference/#redirect)

# Unhandled rejection

> **UnhandledRejection**: Astro detected an unhandled rejection. Here’s the stack trace:\
> STACK

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find any code to handle a rejected `Promise`. Make sure all your promises have an `await` or `.catch()` handler.

# Unknown CLI Error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error while starting one of its CLI commands. The error message should contain more information.

If you can reliably cause this error to happen, we’d appreciate if you could [open an issue](https://astro.build/issues/)

# Unknown compiler error.

> Unknown compiler error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error while compiling your files. In most cases, this is not your fault, but an issue in our compiler.

If there isn’t one already, please [create an issue](https://astro.build/issues/compiler).

**See Also:**

* [withastro/compiler issues list](https://astro.build/issues/compiler)

# Unknown configuration error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error loading your Astro configuration file. This is often caused by a syntax error in your config and the message should offer more information.

If you can reliably cause this error to happen, we’d appreciate if you could [open an issue](https://astro.build/issues/)

**See Also:**

* [Configuration Reference](/en/reference/configuration-reference/)

# Unknown Content Collection Error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error loading your content collections. This can be caused by certain errors inside your `src/content.config.ts` file or some internal errors.

If you can reliably cause this error to happen, we’d appreciate if you could [open an issue](https://astro.build/issues/)

# Unknown CSS Error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error while parsing your CSS. Oftentimes, this is caused by a syntax error and the error message should contain more information.

**See Also:**

* [Styles and CSS](/en/guides/styling/)

# An unknown error occurred while reading or writing files to disk.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An unknown error occurred while reading or writing files to disk. It can be caused by many things, eg. missing permissions or a file not existing we attempt to read.

# Unknown Markdown Error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an unknown error while parsing your Markdown. Oftentimes, this is caused by a syntax error and the error message should contain more information.

# Unknown Vite Error.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Vite encountered an unknown error while rendering your project. We unfortunately do not know what happened (or we would tell you!)

If you can reliably cause this error to happen, we’d appreciate if you could [open an issue](https://astro.build/issues/)

**See Also:**

* [Vite troubleshooting guide](https://vite.dev/guide/troubleshooting.html)

# Unsupported transform in content config.

> **UnsupportedConfigTransformError**: `transform()` functions in your content config must return valid JSON, or data types compatible with the devalue library (including Dates, Maps, and Sets).\
> Full error: PARSE\_ERROR

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`transform()` functions in your content config must return valid JSON, or data types compatible with the devalue library (including Dates, Maps, and Sets).

**See Also:**

* [devalue library](https://github.com/rich-harris/devalue)

# Unsupported or malformed URL.

> **UnsupportedExternalRedirect**: The destination URL in the external redirect from “FROM” to “TO” is unsupported.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An external redirect must start with http or https, and must be a valid URL.

**See Also:**

* [Astro.redirect](/en/reference/api-reference/#redirect)

# Unsupported image conversion

> **UnsupportedImageConversion**: Converting between vector (such as SVGs) and raster (such as PNGs and JPEGs) images is not currently supported.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro does not currently supporting converting between vector (such as SVGs) and raster (such as PNGs and JPEGs) images.

**See Also:**

* [Images](/en/guides/images/)

# Unsupported image format

> **UnsupportedImageFormat**: Received unsupported format `FORMAT` from `IMAGE_PATH`. Currently only SUPPORTED\_FORMATS.JOIN(’, ’) are supported by our image services.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The built-in image services do not currently support optimizing all image formats.

For unsupported formats such as GIFs, you may be able to use an `img` tag directly:

```astro
---
import rocket from '../assets/images/rocket.gif';
---


<img src={rocket.src} width={rocket.width} height={rocket.height} alt="A rocketship in space." />
```

# Configuring experimental flags

Experimental features are available only after enabling a flag in the Astro configuration file.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
    experimental: {
        // enable experimental flags
        // to try out new features
    },
});
```

Astro offers experimental flags to give users early access to new features for testing and feedback.

These flags allow you to participate in feature development by reporting issues and sharing your opinions. These features are not guaranteed to be stable and may include breaking changes even in small `patch` releases while the feature is actively developed.

We recommend [updating Astro](/en/upgrade-astro/#upgrade-to-the-latest-version) frequently, and keeping up with release notes in the [Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) which will inform you of any changes needed to your project code. The experimental feature documentation will always be updated for the current released version only.

# Experimental Chrome DevTools workspace

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.13.0`

Enables experimental [Chrome DevTools workspace integration](https://developer.chrome.com/docs/devtools/workspaces) for the Astro dev server.

This feature allows you to edit files directly in Chrome DevTools and have those changes reflected in your local file system via a connected workspace folder. This is useful for applying edits such as adjusting CSS values without leaving your browser tab.

With this feature enabled, running `astro dev` will automatically configure a Chrome DevTools workspace for your project. Your project will then appear as an available [workspace source that you can connect](#connecting-your-project). Then, changes that you make in the “Sources” panel are automatically saved to your project source code.

To enable this feature, add the experimental flag `chromeDevtoolsWorkspace` to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  experimental: {
+    chromeDevtoolsWorkspace: true,
+  },
});
```

## Connecting your project

[Section titled “Connecting your project”](#connecting-your-project)

Astro will create the necessary configuration file to support Chrome DevTools workspaces. However, your project must also be [connected as a source](https://developer.chrome.com/docs/devtools/workspaces#manual-connection) to enable file saving.

1. [Start the Astro dev server](/en/develop-and-build/#start-the-astro-dev-server) with the appropriate CLI command for your package manager.

2. Navigate to your site preview (e.g. `http://localhost:4321/`) in Chrome and open DevTools.

3. Under the **Sources** > **Workspaces** tab, you will find your Astro project folder. Click **Connect** to add your directory as a workspace.

See the [Chrome DevTools workspace documentation](https://developer.chrome.com/docs/devtools/workspaces#connect) for more information.

# Experimental client prerendering

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@4.2.0`

Enables pre-rendering your prefetched pages on the client in supported browsers.

This feature uses the experimental [Speculation Rules Web API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) and enhances the default `prefetch` behavior globally to prerender links on the client. You may wish to review the [possible risks when prerendering on the client](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API#unsafe_prefetching) before enabling this feature.

Enable client side prerendering in your `astro.config.mjs` along with any desired `prefetch` configuration options:

astro.config.mjs

```js
{
  prefetch: {
    prefetchAll: true,
    defaultStrategy: 'viewport',
  },
  experimental: {
    clientPrerender: true,
  },
}
```

Continue to use the `data-astro-prefetch` attribute on any `<a />` link on your site to opt in to prefetching. Instead of appending a `<link>` tag to the head of the document or fetching the page with JavaScript, a `<script>` tag will be appended with the corresponding speculation rules.

Client side prerendering requires browser support. If the Speculation Rules API is not supported, `prefetch` will fallback to the supported strategy.

See the [Prefetch Guide](/en/guides/prefetch/) for more `prefetch` options and usage.

# Experimental Intellisense for content collections

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@4.14.0`

Enables Intellisense features (e.g. code completion, quick hints) for your content collection entries in compatible editors.

When enabled, this feature will generate and add JSON schemas to the `.astro` directory in your project. These files can be used by the Astro language server to provide Intellisense inside content files (`.md`, `.mdx`, `.mdoc`).

```js
{
  experimental: {
    contentIntellisense: true,
  },
}
```

To use this feature with the Astro VS Code extension, you must also enable the `astro.content-intellisense` option in your VS Code settings. For editors using the Astro language server directly, pass the `contentIntellisense: true` initialization parameter to enable this feature.

# Experimental Content Security Policy (CSP)

**Type:** `boolean | object`\
**Default:** `false`

**Added in:** `astro@5.9.0`

Enables support for [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) to help minimize certain types of security threats by controlling which resources a document is allowed to load. This provides additional protection against [cross-site scripting (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) attacks.

Enabling this feature adds additional security to **Astro’s handling of processed and bundled scripts and styles** by default, and allows you to further configure these, and additional, content types.

This experimental CSP feature has some limitations. Inline scripts are not supported out of the box, but you can [provide your own hashes](#hashes) for external and inline scripts. [Astro’s view transitions](/en/guides/view-transitions/) using the `<ClientRouter />` are not supported, but you can [consider migrating to the browser native View Transition API](https://events-3bg.pages.dev/jotter/astro-view-transitions/) instead if you are not using Astro’s enhancements to the native View Transitions and Navigation APIs.

Note

Due to the nature of the Vite dev server, this feature isn’t supported while working in `dev` mode. Instead, you can test this in your Astro project using `build` and `preview`.

To enable this feature, add the experimental flag in your Astro config:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  experimental: {
+    csp: true
+  }
});
```

When enabled, Astro will add a `<meta>` element inside the `<head>` element of each page.

This element will have the `http-equiv="content-security-policy"` attribute, and the `content` attribute will provide values for the `script-src` and `style-src` [directives](#directives) based on the script and styles used in the page.

```html
<head>
  <meta
    http-equiv="content-security-policy"
    content="
      script-src 'self' 'sha256-somehash';
      style-src 'self' 'sha256-somehash';
    "
  >
</head>
```

## Configuration

[Section titled “Configuration”](#configuration)

You can further customize the `<meta>` element by enabling this feature with a configuration object that includes additional options.

### `algorithm`

[Section titled “algorithm”](#algorithm)

**Type:** `'SHA-256' | 'SHA-512' | 'SHA-384'`\
**Default:** `'SHA-256'`

**Added in:** `astro@5.9.0`

The [hash function](https://developer.mozilla.org/en-US/docs/Glossary/Hash_function) to use when generating the hashes of the styles and scripts emitted by Astro.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      algorithm: 'SHA-512'
    }
  }
});
```

### `directives`

[Section titled “directives”](#directives)

**Type:** `CspDirective[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of [CSP directives](https://content-security-policy.com/#directive) that defines valid sources for specific content types.

While Astro needs to control the `script-src` and `style-src` directives, it is possible to control other CSP directives using the `csp.directives` field. These directives are added to all pages. It accepts a list of type-safe directives:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      directives: [
        "default-src 'self'",
        "img-src 'self' https://images.cdn.example.com"
      ]
    }
  }
});
```

After the build, the `<meta>` element will add your directives into the `content` value alongside Astro’s default directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    default-src 'self';
    img-src 'self' 'https://images.cdn.example.com';
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```

### `styleDirective` and `scriptDirective`

[Section titled “styleDirective and scriptDirective”](#styledirective-and-scriptdirective)

**Type:** `object`\
**Default:** `{}`

**Added in:** `astro@5.9.0`

Configuration objects that allow you to override the default sources for the `style-src` and `script-src` directives with the [`resources`](#resources) property, or to provide additional [hashes](#hashes) to be rendered.

These properties are added to all pages and **completely override Astro’s default resources**, not add to them. Therefore, you must explicitly specify any default values that you want to be included.

#### `resources`

[Section titled “resources”](#resources)

**Type:** `string[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of valid sources for the `script-src` and `style-src` directives.

The `script-src` and `style-src` directives are handled by Astro by default, and use the `'self'` resource. This means that scripts and styles can only be downloaded by the current host (usually the current website).

To override the default source, you can provide a list of resources instead. This will not include `'self'` by default, and must be included in this list if you wish to keep it. These resources are added to all pages.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      styleDirective: {
        resources: [
          "'self'",
          "https://styles.cdn.example.com"
        ]
      },
      scriptDirective: {
        resources: [
          "https://cdn.example.com"
        ]
      }
    }
  }
});
```

After the build, the `<meta>` element will instead apply your sources to the `style-src` and `script-src` directives:

```html
<head>
  <meta
    http-equiv="content-security-policy"
    content="
      script-src https://cdn.example.com 'sha256-somehash';
      style-src 'self' https://styles.cdn.example.com 'sha256-somehash';
    "
  >
</head>
```

#### `hashes`

[Section titled “hashes”](#hashes)

**Type:** `CspHash[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of additional hashes to be rendered.

If you have external scripts or styles that aren’t generated by Astro, or inline scripts, this configuration option allows you to provide additional hashes to be rendered.

You must provide hashes that start with `sha384-`, `sha512-` or `sha256-`. Other values will cause a validation error. These hashes are added to all pages.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      styleDirective: {
        hashes: [
          "sha384-styleHash",
          "sha512-styleHash",
          "sha256-styleHash"
        ]
      },
      scriptDirective: {
        hashes: [
          "sha384-scriptHash",
          "sha512-scriptHash",
          "sha256-scriptHash"
        ]
      }
    }
  }
});
```

After the build, the `<meta>` element will include your additional hashes in the `script-src` and `style-src` directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha384-scriptHash' 'sha512-scriptHash' 'sha256-scriptHash' 'sha256-generatedByAstro';
    style-src 'self' 'sha384-styleHash' 'sha512-styleHash' 'sha256-styleHash' 'sha256-generatedByAstro';
  "
>
```

#### `strictDynamic`

[Section titled “strictDynamic”](#strictdynamic)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.9.0`

Enables [the `strict-dynamic` keyword](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP#the_strict-dynamic_keyword) to support the dynamic injection of scripts.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      scriptDirective: {
        strictDynamic: true
      }
    }
  }
});
```

## Runtime APIs

[Section titled “Runtime APIs”](#runtime-apis)

You can customize the `<meta>` element per page via runtime APIs available from the `Astro` global inside `.astro` components, or the `APIContext` type in endpoints and middleware.

### `csp.insertDirective`

[Section titled “csp.insertDirective”](#cspinsertdirective)

**Type:** `(directive: CspDirective) => void`

**Added in:** `astro@5.9.0`

Adds a single directive to the current page. You can call this method multiple times to add additional directives.

```astro
---
Astro.csp.insertDirective("default-src 'self'");
Astro.csp.insertDirective("img-src 'self' https://images.cdn.example.com");
---
```

After the build, the `<meta>` element for this individual page will incorporate your additional directives alongside the existing `script-src` and `style-src` directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    default-src 'self';
    img-src 'self' https://images.cdn.example.com;
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```

### `csp.insertStyleResource`

[Section titled “csp.insertStyleResource”](#cspinsertstyleresource)

**Type:** `(resource: string) => void`

**Added in:** `astro@5.9.0`

Inserts a new resource to be used for the `style-src` directive.

```astro
---
Astro.csp.insertStyleResource("https://styles.cdn.example.com");
---
```

After the build, the `<meta>` element for this individual page will add your source to the default `style-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash';
    style-src https://styles.cdn.example.com 'sha256-somehash';
  "
>
```

### `csp.insertStyleHash`

[Section titled “csp.insertStyleHash”](#cspinsertstylehash)

**Type:** `(hash: CspHash) => void`

**Added in:** `astro@5.9.0`

Adds a new hash to the `style-src` directive.

```astro
---
Astro.csp.insertStyleHash("sha512-styleHash");
---
```

After the build, the `<meta>` element for this individual page will add your hash to the default `style-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash' 'sha512-styleHash';
  "
>
```

### `csp.insertScriptResource`

[Section titled “csp.insertScriptResource”](#cspinsertscriptresource)

**Type:** `(resource: string) => void`

**Added in:** `astro@5.9.0`

Inserts a new valid source to be used for the `script-src` directive.

```astro
---
Astro.csp.insertScriptResource("https://scripts.cdn.example.com");
---
```

After the build, the `<meta>` element for this individual page will add your source to the default `script-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src https://scripts.cdn.example.com 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```

### `csp.insertScriptHash`

[Section titled “csp.insertScriptHash”](#cspinsertscripthash)

**Type:** `(hash: CspHash) => void`

**Added in:** `astro@5.9.0`

Adds a new hash to the `script-src` directive.

```astro
---
Astro.csp.insertScriptHash("sha512-scriptHash");
---
```

After the build, the `<meta>` element for this individual page will add your hash to the default `script-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash' 'sha512-styleHash';
    style-src 'self' 'sha256-somehash';
  "
>
```

# Experimental prerender conflict error

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.14.0`

Turns prerender conflict warnings into errors during the build process.

Astro currently warns you during the build about any conflicts between multiple dynamic routes that can result in the same output path. For example `/blog/[slug]` and `/blog/[...all]` both could try to prerender the `/blog/post-1` path. In such cases, Astro renders only the [highest priority route](/en/guides/routing/#route-priority-order) for the conflicting path. This allows your site to build successfully, although you may discover that some pages are rendered by unexpected routes.

With this experimental flag set, the build will instead fail immediately with an error. This will require you to resolve any routing conflicts immediately, and will ensure that Astro is building your routes as you intend.

To enable this behavior, add the `experimental.failOnPrerenderConflict` feature flag to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"


defineConfig({
+  experimental: {
+    failOnPrerenderConflict: true,
+  },
});
```

## Usage

[Section titled “Usage”](#usage)

After enabling this flag, you may encounter errors about conflicting prerendered routes when you attempt to build your project. If this happens, you will need to update one or more of your [dynamic routes](/en/guides/routing/#dynamic-routes) to avoid ambiguous routing.

# Experimental fonts API

**Type:** `FontFamily[]`

**Added in:** `astro@5.7.0`

This experimental feature allows you to use fonts from your filesystem and various font providers (eg. Google, Fontsource, Bunny) through a unified, fully customizable, and type-safe API.

Web fonts can impact page performance at both load time and rendering time. This API helps you keep your site performant with automatic [web font optimizations](https://web.dev/learn/performance/optimize-web-fonts) including preload links, optimized fallbacks, and opinionated defaults. [See common usage examples](#usage-examples).

The Fonts API focuses on performance and privacy by downloading and caching fonts so they’re served from your site. This can avoid sending user data to third-party sites, and also ensures that a consistent set of fonts is available to all your visitors.

To enable this feature, configure an `experimental.fonts` object with at least one font:

astro.config.mjs

```diff
import { defineConfig, fontProviders } from "astro/config";


export default defineConfig({
    experimental: {
+        fonts: [{
+            provider: fontProviders.google(),
+            name: "Roboto",
+            cssVariable: "--font-roboto"
+        }]
    }
});
```

Then, add the `<Font />` component and site-wide styling in your `<head>`:

src/components/Head.astro

```diff
---
+import { Font } from 'astro:assets';
---


+<Font cssVariable='--font-roboto' preload />


<style>
+body {
    +font-family: var(--font-roboto);
+}
</style>
```

## Usage

[Section titled “Usage”](#usage)

1. `experimental.fonts` accepts an array of font objects. For each font, you must specify a `provider`, the family `name`, and define a `cssVariable` to refer to your font.

   * [`provider`](#provider): You can choose from the list of [built-in remote providers](#available-remote-font-providers), build your own [custom font provider](#build-your-own-font-provider), or use the [local provider](#local-font-variants) to register local font files.
   * [`name`](#name): Choose a font family supported by your provider.
   * [`cssVariable`](#cssvariable-1): Must be a valid [ident](https://developer.mozilla.org/en-US/docs/Web/CSS/ident) in the form of a CSS variable.

   The following example configures the [“Roboto” family from Google Fonts](https://fonts.google.com/specimen/Roboto):

   astro.config.mjs

   ```diff
   import { defineConfig, fontProviders } from "astro/config";


   export default defineConfig({
   +  experimental: {
   +    fonts: [{
   +      provider: fontProviders.google(),
   +      name: "Roboto",
   +      cssVariable: "--font-roboto"
   +    }]
   +  }
   });
   ```

   More configuration options, such as defining [fallback font families](#fallbacks) and which [`weights`](#weights) and [`styles`](#styles) to download, are available and some will depend on your chosen provider.

   See the full [configuration reference](#font-configuration-reference) to learn more.

2. Apply styles using the `<Font />` component. It must be imported and added to your page `<head>`. Providing the font’s [`cssVariable`](#cssvariable) is required, and you can optionally [output preload links](#preload):

   src/components/Head.astro

   ```diff
   ---
   +import { Font } from 'astro:assets';
   ---


   +<Font cssVariable="--font-roboto" preload />
   ```

   This is commonly done in a component such as `Head.astro` that is used in a common site layout.

   See the full [`<Font>` component reference](#font--component-reference) for more information.

   Since the `<Font />` component generates CSS with font declarations, you can reference the font family using the `cssVariable`:

   * CSS

     ```diff
     <style>
     body {
         +font-family: var(--font-roboto);
     }
     </style>
     ```

   * Tailwind CSS 4.0

     src/styles/global.css

     ```diff
     @import 'tailwindcss';


     @theme inline {
         +--font-sans: var(--font-roboto);
     }
     ```

   * Tailwind CSS 3.0

     tailwind.config.mjs

     ```diff
     /** @type {import("tailwindcss").Config} */
     export default {
     content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
     theme: {
         extend: {},
     +    fontFamily: {
     +        sans: ["var(--font-roboto)"]
     +    }
     },
     plugins: []
     };
     ```

## Available remote font providers

[Section titled “Available remote font providers”](#available-remote-font-providers)

Astro re-exports most [unifont](https://github.com/unjs/unifont/) providers. The following have built-in support:

* [Adobe](https://fonts.adobe.com/)
* [Bunny](https://fonts.bunny.net/)
* [Fontshare](https://www.fontshare.com/)
* [Fontsource](https://fontsource.org/)
* [Google](https://fonts.google.com/)

To use a built-in remote provider, configure `provider` with the appropriate value for your chosen font provider:

* Adobe

  ```js
  provider: fontProviders.adobe({ id: process.env.ADOBE_ID })
  ```

* Bunny

  ```js
  provider: fontProviders.bunny()
  ```

* Fontshare

  ```js
  provider: fontProviders.fontshare()
  ```

* Fontsource

  ```js
  provider: fontProviders.fontsource()
  ```

* Google

  ```js
  provider: fontProviders.google()
  ```

  Additionally, the `google()` font provider accepts all options available for the [unifont Google `ProviderOption`](https://github.com/unjs/unifont/blob/main/src/providers/google.ts#L10-L26):

  ```js
  provider: fontProviders.google({
    glyphs: {
      Roboto: ["a"]
    }
  })
  ```

You can also [make a custom Astro font provider](#build-your-own-font-provider) for any unifont provider.

## Usage examples

[Section titled “Usage examples”](#usage-examples)

astro.config.mjs

```js
import { defineConfig, fontProviders } from "astro/config";


export default defineConfig({
  experimental: {
    fonts: [
      {
        name: "Roboto",
        cssVariable: "--font-roboto"
        provider: fontProviders.google(),
        // Default included:
        // weights: [400] ,
        // styles: ["normal", "italics"],
        // subsets: ["cyrillic-ext", "cyrillic", "greek-ext", "greek", "vietnamese", "latin-ext", "latin"],
        // fallbacks: ["sans-serif"],
      },
      {
        name: "Inter",
        cssVariable: "--font-inter",
        provider: fontProviders.fontsource(),
        // Specify weights that are actually used
        weights: [400, 500, 600, 700],
        // Specify styles that are actually used
        styles: ["normal"],
        // Download only font files for characters used on the page
        subsets: ["cyrillic"],
      },
      {
        name: "JetBrains Mono",
        cssVariable: "--font-jetbrains-mono",
        provider: fontProviders.fontsource(),
        // Download only font files for characters used on the page
        subsets: ["latin"],
        // Use a fallback font family matching the intended appearance
        fallbacks: ["monospace"],
      },
      {
        name: "Poppins",
        cssVariable: "--font-poppins",
        provider: "local",
        // Weight and style are not specified so Astro
        // will try to infer them for each variant
        variants: [
          {
            src: [
              "./src/assets/fonts/Poppins-regular.woff2",
              "./src/assets/fonts/Poppins-regular.woff",
            ]
          },
          {
            src: [
              "./src/assets/fonts/Poppins-bold.woff2",
              "./src/assets/fonts/Poppins-bold.woff",
            ]
          },
        ]
      }
    ],
  }
});
```

## `<Font />` component reference

[Section titled “\<Font /> component reference”](#font--component-reference)

This component outputs style tags and can optionally output preload links for a given font family.

It must be imported and added to your page `<head>`. This is commonly done in a component such as `Head.astro` that is used in a common site layout for global use but may be added to individual pages as needed.

With this component, you have control over which font family is used on which page, and which fonts are preloaded.

### cssVariable

[Section titled “cssVariable”](#cssvariable)

**Example type:** `"--font-roboto" | "--font-comic-sans" | ...`

The [`cssVariable`](#cssvariable-1) registered in your Astro configuration:

src/components/Head.astro

```astro
---
import { Font } from 'astro:assets';
---


<Font cssVariable="--font-roboto" />
```

### preload

[Section titled “preload”](#preload)

**Type:** `boolean | { weight?: string | number; style?: string; subset?: string }[]`\
**Default:** `false`

Whether to output [preload links](https://web.dev/learn/performance/optimize-web-fonts#preload) or not:

src/components/Head.astro

```astro
---
import { Font } from 'astro:assets';
---


<Font cssVariable="--font-roboto" preload />
```

With the `preload` directive, the browser will immediately begin downloading all possible font links during page load.

#### Granular preloads

[Section titled “Granular preloads”](#granular-preloads)

**Added in:** `astro@5.15.0` New

You may not always want to preload every font link, as this can block loading other important resources or may download fonts that are not needed for the current page.

To selectively control which font files are preloaded, you can provide an array of objects describing any combination of font `weight`, `style`, or `subset` to preload.

The following example will only preload font files with a `400` weight or a `normal` style in the `latin` subset:

src/components/Head.astro

```astro
---
import { Font } from 'astro:assets';
---


<Font
  cssVariable="--font-roboto"
  preload={[
    { subset: 'latin', style: 'normal' },
    { weight: '400' },
  ]}
/>
```

Variable weight font files will be preloaded if any weight within its range is requested. For example, a font file for font weight `100 900` will be included when `400` is specified in a `preload` object.

## Accessing font data programmatically

[Section titled “Accessing font data programmatically”](#accessing-font-data-programmatically)

The `getFontData()` function is intended for retrieving lower-level font family data programmatically, for example, in an [API Route](/en/guides/endpoints/#server-endpoints-api-routes) or to generate your own meta tags.

### `getFontData()`

[Section titled “getFontData()”](#getfontdata)

**Type:** `(cssVariable: CssVariable) => FontData[]`

**Added in:** `astro@5.14.0`

Returns an array of `FontData` objects for the provided [`cssVariable`](#cssvariable-1), which contains `src`, `weight` and `style`.

The following example uses `getFontData()` to get the font buffer from the URL when using [satori](https://github.com/vercel/satori) to generate OpenGraph images:

src/pages/og.png.ts

```tsx
import type{ APIRoute } from "astro"
import { getFontData } from "astro:assets"
import satori from "satori"


export const GET: APIRoute = (context) => {
  const data = getFontData("--font-roboto")


  const svg = await satori(
    <div style={{ color: "black" }}>hello, world</div>,
    {
      width: 600,
      height: 400,
      fonts: [
        {
          name: "Roboto",
          data: await fetch(new URL(data[0].src[0].url, context.url.origin)).then(res => res.arrayBuffer()),
          weight: 400,
          style: "normal",
        },
      ],
    },
  )


  // ...
}
```

## Font configuration reference

[Section titled “Font configuration reference”](#font-configuration-reference)

All properties of your fonts must be configured in the Astro config. Some properties are common to both remote and local fonts, and other properties are available depending on your chosen font provider.

### Common properties

[Section titled “Common properties”](#common-properties)

The following properties are available for remote and local fonts. `provider`, `name`, and `cssVariable` are required.

astro.config.mjs

```js
import { defineConfig, fontProviders } from "astro/config";


export default defineConfig({
  experimental: {
    fonts: [{
      provider: fontProviders.google(),
      name: "Roboto",
      cssVariable: "--font-roboto"
    }]
  }
});
```

#### provider

[Section titled “provider”](#provider)

**Type:** `AstroFontProvider | "local"`

The source of your font files. You can use a [built-in provider](#available-remote-font-providers), write your own [custom provider](#build-your-own-font-provider), or set to `"local"` to use local font files:

astro.config.mjs

```js
import { defineConfig, fontProviders } from "astro/config";


export default defineConfig({
  experimental: {
    fonts: [{
      provider: fontProviders.google(),
      name: "Roboto",
      cssVariable: "--font-roboto"
    }]
  }
});
```

#### name

[Section titled “name”](#name)

**Type:** `string`

The font family name, as identified by your font provider:

```js
name: "Roboto"
```

#### cssVariable

[Section titled “cssVariable”](#cssvariable-1)

**Type:** `string`

A valid [ident](https://developer.mozilla.org/en-US/docs/Web/CSS/ident) of your choosing in the form of a CSS variable (i.e. starting with `--`):

```js
cssVariable: "--font-roboto"
```

#### fallbacks

[Section titled “fallbacks”](#fallbacks)

**Type:** `string[]`\
**Default:** `["sans-serif"]`

An array of fonts to use when your chosen font is unavailable, or loading. Fallback fonts will be chosen in the order listed. The first available font will be used:

```js
fallbacks: ["CustomFont", "serif"]
```

To disable fallback fonts completely, configure an empty array:

```js
fallbacks: []
```

Specify at least a [generic family name](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family#generic-name) matching the intended appearance of your font. Astro will then attempt to generate [optimized fallbacks](https://developer.chrome.com/blog/font-fallbacks) using font metrics. To disable this optimization, set `optimizedFallbacks` to false.

#### optimizedFallbacks

[Section titled “optimizedFallbacks”](#optimizedfallbacks)

**Type:** `boolean`\
**Default:** `true`

Whether or not to enable Astro’s default optimization when generating fallback fonts. You may disable this default optimization to have full control over how [`fallbacks`](#fallbacks) are generated:

```js
optimizedFallbacks: false
```

### Remote font properties

[Section titled “Remote font properties”](#remote-font-properties)

Further configuration options are available for remote fonts. Set these to customize the data loaded from your [font provider](#available-remote-font-providers), for example to only download certain font weights or styles.

Under the hood, these options are handled by [unifont](https://github.com/unjs/unifont/). Some properties may not be supported by some providers and may be handled differently by each provider.

#### weights

[Section titled “weights”](#weights)

**Type:** `(number | string)[]`\
**Default:** `[400]`

An array of [font weights](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight). If no value is specified in your configuration, only weight `400` is included by default to prevent unnecessary downloads. You will need to include this property to access any other font weights:

```js
weights: [200, "400", "bold"]
```

If the associated font is a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide), you can specify a range of weights:

```js
weights: ["100 900"]
```

#### styles

[Section titled “styles”](#styles)

**Type:** `("normal" | "italic" | "oblique")[]`\
**Default:** `["normal", "italic"]`

An array of [font styles](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style):

```js
styles: ["normal", "oblique"]
```

#### subsets

[Section titled “subsets”](#subsets)

**Type:** `string[]`\
**Default:** `["cyrillic-ext", "cyrillic", "greek-ext", "greek", "vietnamese", "latin-ext", "latin"]`

Defines a list of [font subsets](https://knaap.dev/posts/font-subsetting/) to preload.

```js
subsets: ["latin"]
```

#### display

[Section titled “display”](#display)

**Type:** `"auto" | "block" | "swap" | "fallback" | "optional"`\
**Default:** `"swap"`

Defines [how a font displays](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display) based on when it is downloaded and ready for use:

```js
display: "block"
```

#### unicodeRange

[Section titled “unicodeRange”](#unicoderange)

**Type:** `string[]`\
**Default:** `undefined`

Determines when a font must be downloaded and used based on a specific [range of unicode characters](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range). If a character on the page matches the configured range, the browser will download the font and all characters will be available for use on the page. To configure a subset of characters preloaded for a single font, see the [subsets](#subsets) property instead.

This can be useful for localization to avoid unnecessary font downloads when a specific part of your website uses a different alphabet and will be displayed with a separate font. For example, a website that offers both English and Japanese versions can prevent the browser from downloading the Japanese font on English versions of the page that do not contain any of the Japanese characters provided in `unicodeRange`.

```js
unicodeRange: ["U+26"]
```

#### stretch

[Section titled “stretch”](#stretch)

**Type:** `string`\
**Default:** `undefined`

A [font stretch](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-stretch):

```js
stretch: "condensed"
```

#### featureSettings

[Section titled “featureSettings”](#featuresettings)

**Type:** `string`\
**Default:** `undefined`

Controls the [typographic font features](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-feature-settings) (e.g. ligatures, small caps, or swashes):

```js
featureSettings: "'smcp' 2"
```

#### variationSettings

[Section titled “variationSettings”](#variationsettings)

**Type:** `string`\
**Default:** `undefined`

Font [variation settings](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-variation-settings):

```js
variationSettings: "'xhgt' 0.7"
```

### Local font `variants`

[Section titled “Local font variants”](#local-font-variants)

**Type:** `LocalFontFamily["variants"]`

The `variants` property is required when using local font files. Each variant represents a [`@font-face` declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/) and requires a `weight`, `style`, and `src` value.

Additionally, [some other properties of remote fonts](#other-properties) may be specified within each variant.

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
    experimental: {
        fonts: [{
            provider: "local",
            name: "Custom",
            cssVariable: "--font-custom",
            variants: [
                {
                    weight: 400,
                    style: "normal",
                    src: ["./src/assets/fonts/custom-400.woff2"]
                },
                {
                    weight: 700,
                    style: "normal",
                    src: ["./src/assets/fonts/custom-700.woff2"]
                }
                // ...
            ]
        }]
    }
});
```

#### weight

[Section titled “weight”](#weight)

**Type:** `number | string`\
**Default:** `undefined`

A [font weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight):

```js
weight: 200
```

If the associated font is a [variable font](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_fonts/Variable_fonts_guide), you can specify a range of weights:

```js
weight: "100 900"
```

When the value is not set, by default Astro will try to infer the value based on the first [`source`](#src).

#### style

[Section titled “style”](#style)

**Type:** `"normal" | "italic" | "oblique"`\
**Default:** `undefined`

A [font style](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style):

```js
style: "normal"
```

When the value is not set, by default Astro will try to infer the value based on the first [`source`](#src).

#### src

[Section titled “src”](#src)

**Type:** `(string | URL | { url: string | URL; tech?: string })[]`

Font [sources](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/src). It can be a path relative to the root, a package import or a URL. URLs are particularly useful if you inject local fonts through an integration:

* Relative path

  ```js
  src: ["./src/assets/fonts/MyFont.woff2", "./src/assets/fonts/MyFont.woff"]
  ```

* URL

  ```js
  src: [new URL("./custom.ttf", import.meta.url)]
  ```

* Package import

  ```js
  src: ["my-package/SomeFont.ttf"]
  ```

Caution

We recommend not putting your font files in [the `public/` directory](/en/reference/configuration-reference/#publicdir). Since Astro will copy these files into that folder at build time, this will result in duplicated files in your build output. Instead, store them somewhere else in your project, such as in [`src/`](/en/reference/configuration-reference/#srcdir).

You can also specify a [tech](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/src#tech) by providing objects:

```js
src: [{ url:"./src/assets/fonts/MyFont.woff2", tech: "color-COLRv1" }]
```

#### Other properties

[Section titled “Other properties”](#other-properties)

The following options from remote font families are also available for local font families within variants:

* [display](#display)
* [unicodeRange](#unicoderange)
* [stretch](#stretch)
* [featureSettings](#featuresettings)
* [variationSettings](#variationsettings)

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
    experimental: {
        fonts: [{
            provider: "local",
            name: "Custom",
            cssVariable: "--font-custom",
            variants: [
                {
                    weight: 400,
                    style: "normal",
                    src: ["./src/assets/fonts/custom-400.woff2"],
                    display: "block"
                }
            ]
        }]
    }
});
```

## Build your own font provider

[Section titled “Build your own font provider”](#build-your-own-font-provider)

If you do not wish to use one of the [built-in providers](#available-remote-font-providers) (eg. you want to use a 3rd-party unifont provider or build something for a private registry), you can build your own.

An Astro font provider is made up of two parts: the config object and the actual implementation.

1. Using the `defineAstroFontProvider()` type helper, create a function that returns a font provider config object containing:

   * `entrypoint`: A URL, a path relative to the root, or a package import.
   * `config`: An optional serializable object passed to the unifont provider.

   - Without config

     provider/config.ts

     ```ts
     import { defineAstroFontProvider } from 'astro/config';


     export function myProvider() {
         return defineAstroFontProvider({
             entrypoint: new URL('./implementation.js', import.meta.url)
         });
     };
     ```

   - With config

     provider/config.ts

     ```ts
     import { defineAstroFontProvider } from 'astro/config';


     interface Config {
         // ...
     };


     export function myProvider(config: Config) {
         return defineAstroFontProvider({
             entrypoint: new URL('./implementation.js', import.meta.url),
             config
         });
     };
     ```

2. Create a second file to export your unifont `provider` implementation:

   implementation.ts

   ```ts
   import { defineFontProvider } from "unifont";


   export const provider = defineFontProvider("my-provider", async (options, ctx) => {
       // fetch/define your custom fonts
       // ...
   });
   ```

   Tip

   You can check out [the source code for unifont’s providers](https://github.com/unjs/unifont/blob/main/src/providers/) to learn more about how to create a unifont provider.

3. Add your custom provider to your font configuration.

   astro.config.mjs

   ```js
   fonts: [{
     provider: fontProviders.myProvider(),
     name: "Custom Font",
     cssVariable: "--font-custom"
    }]
   ```

## Caching

[Section titled “Caching”](#caching)

The Fonts API caching implementation was designed to be practical in development and efficient in production. During builds, font files are copied to the `_astro/fonts` output directory, so they can benefit from HTTP caching of static assets (usually a year).

To clear the cache in development, remove the `.astro/fonts` directory. To clear the build cache, remove the `node_modules/.astro/fonts` directory

## Further reading

[Section titled “Further reading”](#further-reading)

For full details and to give feedback on this experimental API, see [the Fonts RFC](https://github.com/withastro/roadmap/blob/rfc/fonts/proposals/0055-fonts.md).

# Experimental Markdown heading ID compatibility

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.5.0`

The `experimental.headingIdCompat` flag makes the IDs generated by Astro for Markdown headings compatible with common platforms like GitHub and npm.

To enable heading ID compatibility, set the flag to `true` in your Astro configuration:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"


export default defineConfig({
+  experimental: {
+    headingIdCompat: true,
+  }
})
```

## Usage

[Section titled “Usage”](#usage)

This experimental flag allows you to retain the trailing hyphens on the end of IDs for Markdown headings ending in special characters, creating IDs compatible with those generated by other common platforms. It requires no specific usage and only affects how Astro generates the `id` for your headings written using Markdown syntax.

Astro, like many platforms, uses the popular [`github-slugger`](https://github.com/Flet/github-slugger) package to convert the text content of a Markdown heading to a slug to use in IDs. This experimental flag allows you to omit Astro’s additional default processing step that strips a trailing hyphen from the end of IDs for headings ending in special characters.

For example, the following Markdown heading:

```md
## `<Picture />`
```

will generate the following HTML in Astro by default:

```html
<h2 id="picture"><code>&lt;Picture /&gt;</h2>
```

Using `experimental.headingIdCompat`, the same Markdown will generate the following HTML, which is identical to that of platforms such as GitHub:

```html
<h2 id="picture-"><code>&lt;Picture /&gt;</h2>
```

In a future major version, Astro will switch to use the compatible ID style by default, but you can opt in to the future behavior early using the `experimental.headingIdCompat` flag.

## Usage with `rehypeHeadingIds` plugin

[Section titled “Usage with rehypeHeadingIds plugin”](#usage-with-rehypeheadingids-plugin)

If you are [using the `rehypeHeadingIds` plugin](/en/guides/markdown-content/#heading-ids-and-plugins) directly, opt in to the compatibility mode when passing the plugin in your Astro configuration:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import { rehypeHeadingIds } from '@astrojs/markdown-remark';
import { otherPluginThatReliesOnHeadingIDs } from 'some/plugin/source';


export default defineConfig({
  markdown: {
    rehypePlugins: [
      [rehypeHeadingIds, { headingIdCompat: true }],
      otherPluginThatReliesOnHeadingIDs,
    ],
  },
});
```

# Experimental live content collections

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.10.0`

Enables support for live content collections in your project.

Live content collections are a new type of [content collection](/en/guides/content-collections/) that fetch their data at runtime rather than build time. This allows you to access frequently updated data from CMSs, APIs, databases, or other sources using a unified API, without needing to rebuild your site when the data changes.

## Basic usage

[Section titled “Basic usage”](#basic-usage)

To enable the feature, make sure you have an adapter configured for [on-demand rendering](/en/guides/on-demand-rendering/) and add the `experimental.liveContentCollections` flag to your `astro.config.mjs` file:

astro.config.mjs

```js
{
  experimental: {
    liveContentCollections: true,
  },
}
```

Then create a new `src/live.config.ts` file (alongside your `src/content.config.ts` if you have one) to define your live collections with a [live loader](#creating-a-live-loader) and optionally a [schema](#using-zod-schemas) using the new `defineLiveCollection()` function from the `astro:content` module.

src/live.config.ts

```ts
import { defineLiveCollection } from 'astro:content';
import { storeLoader } from '@mystore/astro-loader';


const products = defineLiveCollection({
  loader: storeLoader({
    apiKey: process.env.STORE_API_KEY,
    endpoint: 'https://api.mystore.com/v1',
  }),
});


export const collections = { products };
```

You can then use the dedicated `getLiveCollection()` and `getLiveEntry()` functions to access your live data:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveCollection, getLiveEntry } from 'astro:content';


// Get all products
const { entries: allProducts, error } = await getLiveCollection('products');
if (error) {
  // Handle error appropriately
  console.error(error.message);
}


// Get products with a filter (if supported by your loader)
const { entries: electronics } = await getLiveCollection('products', { category: 'electronics' });


// Get a single product by ID (string syntax)
const { entry: product, error: productError } = await getLiveEntry('products', Astro.params.id);
if (productError) {
  return Astro.redirect('/404');
}


// Get a single product with a custom query (if supported by your loader) using a filter object
const { entry: productBySlug } = await getLiveEntry('products', { slug: Astro.params.slug });
---
```

## When to use live content collections

[Section titled “When to use live content collections”](#when-to-use-live-content-collections)

Live content collections are designed for data that changes frequently and needs to be up-to-date when a page is requested. Consider using them when:

* **You need real-time information** (e.g. user-specific data, current stock levels)
* **You want to avoid constant rebuilds** for content that changes often
* **Your data updates frequently** (e.g. up-to-the-minute product inventory, prices, availability)
* **You need to pass dynamic filters** to your data source based on user input or request parameters
* **You’re building preview functionality** for a CMS where editors need to see draft content immediately

In contrast, use build-time content collections when:

* **Performance is critical** and you want to pre-render data at build time
* **Your data is relatively static** (e.g., blog posts, documentation, product descriptions)
* **You want to benefit from build-time optimization** and caching
* **You need to process MDX** or perform image optimization
* **Your data can be fetched once and reused** across multiple builds

See the [limitations of experimental live collections](#live-collection-limitations) and [key differences from build-time collections](#differences-from-build-time-collections) for more details on choosing between live and preloaded collections.

## Using live collections

[Section titled “Using live collections”](#using-live-collections)

You can [create your own live loaders](#creating-a-live-loader) for your data source, or you can use community loaders distributed as npm packages. Here’s how you could use example CMS and e-commerce loaders:

src/live.config.ts

```ts
import { defineLiveCollection } from 'astro:content';
import { cmsLoader } from '@example/cms-astro-loader';
import { productLoader } from '@example/store-astro-loader';


const articles = defineLiveCollection({
  loader: cmsLoader({
    apiKey: process.env.CMS_API_KEY,
    contentType: 'article',
  }),
});


const products = defineLiveCollection({
  loader: productLoader({
    apiKey: process.env.STORE_API_KEY,
  }),
});


export const collections = { articles, products };
```

You can then get content from both loaders with a unified API:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveCollection, getLiveEntry } from 'astro:content';


// Use loader-specific filters
const { entries: draftArticles } = await getLiveCollection('articles', {
  status: 'draft',
  author: 'john-doe',
});


// Get a specific product by ID
const { entry: product } = await getLiveEntry('products', Astro.params.slug);
---
```

### Error handling

[Section titled “Error handling”](#error-handling)

Live loaders can fail due to network issues, API errors, or validation problems. The API is designed to make error handling explicit.

When you call `getLiveCollection()` or `getLiveEntry()`, the error will be one of:

* The error type defined by the loader (if it returned an error)
* A `LiveEntryNotFoundError` if the entry was not found
* A `LiveCollectionValidationError` if the collection data does not match the expected schema
* A `LiveCollectionCacheHintError` if the cache hint is invalid
* A `LiveCollectionError` for other errors, such as uncaught errors thrown in the loader

These errors have a static `is()` method that you can use to check the type of error at runtime:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry, LiveEntryNotFoundError } from 'astro:content';


const { entry, error } = await getLiveEntry('products', Astro.params.id);


if (error) {
  if (LiveEntryNotFoundError.is(error)) {
    console.error(`Product not found: ${error.message}`);
    Astro.response.status = 404;
  } else {
    console.error(`Error loading product: ${error.message}`);
    return Astro.redirect('/500');
  }
}
---
```

## Creating a live loader

[Section titled “Creating a live loader”](#creating-a-live-loader)

A live loader is an object with two methods: `loadCollection()` and `loadEntry()`. These methods should handle errors gracefully and return either data or an [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) object.

The standard pattern is to export a function that returns this loader object, allowing you to pass configuration options like API keys or endpoints.

Here’s a basic example:

myloader.ts

```ts
import type { LiveLoader } from 'astro/loaders';
import { fetchFromCMS } from './cms-client.js';


interface Article {
  id: string;
  title: string;
  content: string;
  author: string;
}


export function articleLoader(config: { apiKey: string }): LiveLoader<Article> {
  return {
    name: 'article-loader',
    loadCollection: async ({ filter }) => {
      try {
        const articles = await fetchFromCMS({
          apiKey: config.apiKey,
          type: 'article',
          filter,
        });


        return {
          entries: articles.map((article) => ({
            id: article.id,
            data: article,
          })),
        };
      } catch (error) {
        return {
          error: new Error(`Failed to load articles: ${error.message}`),
        };
      }
    },
    loadEntry: async ({ filter }) => {
      try {
        // filter will be { id: "some-id" } when called with a string
        const article = await fetchFromCMS({
          apiKey: config.apiKey,
          type: 'article',
          id: filter.id,
        });


        if (!article) {
          return {
            error: new Error('Article not found'),
          };
        }


        return {
          id: article.id,
          data: article,
        };
      } catch (error) {
        return {
          error: new Error(`Failed to load article: ${error.message}`),
        };
      }
    },
  };
}
```

### Rendering content

[Section titled “Rendering content”](#rendering-content)

A loader can add support for directly rendered content by returning [a `rendered` property](/en/reference/content-loader-reference/#rendered) in the entry. This allows you to use [the `render()` function and `<Content />` component](/en/guides/content-collections/#rendering-body-content) to render the content directly in your pages. If the loader does not return a `rendered` property for an entry, the `<Content />` component will render nothing.

myloader.ts

```ts
// ...
export function articleLoader(config: { apiKey: string }): LiveLoader<Article> {
  return {
    name: 'article-loader',
    loadEntry: async ({ filter }) => {
      try {
        const article = await fetchFromCMS({
          apiKey: config.apiKey,
          type: 'article',
          id: filter.id,
        });


        return {
          id: article.id,
          data: article,
          rendered: {
            // Assuming the CMS returns HTML content
            html: article.htmlContent,
          },
        };
      } catch (error) {
        return {
          error: new Error(`Failed to load article: ${error.message}`),
        };
      }
    },
    // ...
  };
}
```

You can then render both content and metadata from live collection entries in pages using the same method as built-time collections. You also have access to any [error returned by the live loader](#error-handling-in-loaders), for example, to rewrite to a 404 page when content cannot be displayed:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry, render } from 'astro:content';
const { entry, error } = await getLiveEntry('articles', Astro.params.id);
if (error) {
  return Astro.rewrite('/404');
}


const { Content } = await render(entry);
---


<h1>{entry.data.title}</h1>
<Content />
```

### Error handling in loaders

[Section titled “Error handling in loaders”](#error-handling-in-loaders)

Loaders should handle all errors and return an [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) subclass for errors. You can create custom error types and use them for more specific error handling if needed. If an error is thrown in the loader, it will be caught and returned, wrapped in a `LiveCollectionError`. You can also create [custom error types](#custom-error-types) for proper typing.

Astro will generate some errors itself, depending on the response from the loader:

* If `loadEntry` returns `undefined`, Astro will return a `LiveEntryNotFoundError` to the user.
* If a schema is defined for the collection and the data does not match the schema, Astro will return a `LiveCollectionValidationError`.
* If the loader returns an invalid cache hint, Astro will return a `LiveCollectionCacheHintError`. The `cacheHint` field is optional, so if you do not have valid data to return, you can simply omit it.

my-loader.ts

```ts
import type { LiveLoader } from 'astro/loaders';
import { MyLoaderError } from './errors.js';


export function myLoader(config): LiveLoader<MyData, undefined, undefined, MyLoaderError> {
  return {
    name: 'my-loader',
    loadCollection: async ({ filter }) => {
      // Return your custom error type
      return {
        error: new MyLoaderError('Failed to load', 'LOAD_ERROR'),
      };
    },
    // ...
  };
}
```

### Distributing your loader

[Section titled “Distributing your loader”](#distributing-your-loader)

Loaders can be defined in your site or as a separate npm package. If you want to share your loader with the community, you can [publish it to NPM with the `astro-component` and `astro-loader` keywords](/en/reference/publish-to-npm/#packagejson-data).

The loader should export a function that returns the `LiveLoader` object, allowing users to configure it with their own settings.

## Type safety

[Section titled “Type safety”](#type-safety)

Like regular content collections, live collections can be typed to ensure type safety in your data. [Using Zod schemas](#using-zod-schemas) is supported, but not required to define types for live collections. Unlike preloaded collections defined at build time, live loaders can instead choose to pass generic types to the `LiveLoader` interface. You can define the types for your collection and entry data, as well as custom filter types for querying, and custom error types for error handling.

### Type-safe data

[Section titled “Type-safe data”](#type-safe-data)

Live loaders can define types for the data they return. This allows TypeScript to provide type checking and autocompletion when working with the data in your components.

store-loader.ts

```ts
import type { LiveLoader } from 'astro/loaders';
import { fetchProduct, fetchCategory, type Product } from './store-client';


export function storeLoader(): LiveLoader<Product> {
  // ...
}
```

When you use `getLiveCollection()` or `getLiveEntry()`, TypeScript will infer the types based on the loader’s definition:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry } from 'astro:content';
const { entry: product } = await getLiveEntry('products', '123');
// TypeScript knows product.data is of type Product
console.log(product?.data.name);
---
```

### Type-safe filters

[Section titled “Type-safe filters”](#type-safe-filters)

Live loaders can define custom filter types for both `getLiveCollection()` and `getLiveEntry()`. This enables type-safe querying that matches your API’s capabilities, making it easier for users to discover available filters and ensure they are used correctly. If you include JSDoc comments in your filter types, the user will see these in their IDE as hints when using the loader.

store-loader.ts

```ts
import type { LiveLoader } from 'astro/loaders';
import { fetchProduct, fetchCategory, type Product } from './store-client';


interface CollectionFilter {
  category?: string;
  /** Minimum price to filter products */
  minPrice?: number;
  /** Maximum price to filter products */
  maxPrice?: number;
}


interface EntryFilter {
  /** Alias for `sku` */
  id?: string;
  slug?: string;
  sku?: string;
}


export function productLoader(config: {
  apiKey: string;
  endpoint: string;
}): LiveLoader<Product, EntryFilter, CollectionFilter> {
  return {
    name: 'product-loader',
    loadCollection: async ({ filter }) => {
      // filter is typed as CollectionFilter
      const data = await fetchCategory({
        apiKey: config.apiKey,
        category: filter?.category ?? 'all',
        minPrice: filter?.minPrice,
        maxPrice: filter?.maxPrice,
      });


      return {
        entries: data.products.map((product) => ({
          id: product.sku,
          data: product,
        })),
      };
    },
    loadEntry: async ({ filter }) => {
      // filter is typed as EntryFilter | { id: string }
      const product = await fetchProduct({
        apiKey: config.apiKey,
        slug: filter.slug,
        sku: filter.sku || filter.id,
      });
      if (!product) {
        return {
          error: new Error('Product not found'),
        };
      }
      return {
        id: product.sku,
        entry: product,
      };
    },
  };
}
```

### Custom error types

[Section titled “Custom error types”](#custom-error-types)

You can create custom error types for [errors returned by your loader](#error-handling-in-loaders) and pass them as a generic to get proper typing:

my-loader.ts

```ts
class MyLoaderError extends Error {
  constructor(
    message: string,
    public code?: string
  ) {
    super(message);
    this.name = 'MyLoaderError';
  }
}


export function myLoader(config): LiveLoader<MyData, undefined, undefined, MyLoaderError> {
  return {
    name: 'my-loader',
    loadCollection: async ({ filter }) => {
      // Return your custom error type
      return {
        error: new MyLoaderError('Failed to load', 'LOAD_ERROR'),
      };
    },
    // ...
  };
}
```

When you use `getLiveCollection()` or `getLiveEntry()`, TypeScript will infer the custom error type, allowing you to handle it appropriately:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry } from 'astro:content';


const { entry, error } = await getLiveEntry('products', '123');


if (error) {
  if (error.name === 'MyLoaderError') {
    console.error(`Loader error: ${error.message} (code: ${error.code})`);
  } else {
    console.error(`Unexpected error: ${error.message}`);
  }
  return Astro.rewrite('/500');
}
---
```

## Using Zod schemas

[Section titled “Using Zod schemas”](#using-zod-schemas)

Just like with build-time collections, you can use [Zod schemas](/en/guides/content-collections/#defining-the-collection-schema) with live collections to validate and transform data at runtime. When you define a schema, it takes precedence over [the loader’s types](#type-safe-data) when you query the collection:

src/live.config.ts

```ts
import { z, defineLiveCollection } from 'astro:content';
import { apiLoader } from './loaders/api-loader';


const products = defineLiveCollection({
  loader: apiLoader({ endpoint: process.env.API_URL }),
  schema: z
    .object({
      id: z.string(),
      name: z.string(),
      price: z.number(),
      // Transform the API's category format
      category: z.string().transform((str) => str.toLowerCase().replace(/\s+/g, '-')),
      // Coerce the date to a Date object
      createdAt: z.coerce.date(),
    })
    .transform((data) => ({
      ...data,
      // Add a formatted price field
      displayPrice: `$${data.price.toFixed(2)}`,
    })),
});


export const collections = { products };
```

When using Zod schemas, validation errors are automatically caught and returned as `AstroError` objects:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry, LiveCollectionValidationError } from 'astro:content';


const { entry, error } = await getLiveEntry('products', '123');


// You can handle validation errors specifically
if (LiveCollectionValidationError.is(error)) {
  console.error(error.message);
  return Astro.rewrite('/500');
}


// TypeScript knows entry.data matches your Zod schema, not the loader's type
console.log(entry?.data.displayPrice); // e.g., "$29.99"
---
```

## Cache hints

[Section titled “Cache hints”](#cache-hints)

Live loaders can provide cache hints to help with response caching. You can use this data to send HTTP cache headers or otherwise inform your caching strategy.

my-loader.ts

```ts
export function myLoader(config): LiveLoader<MyData> {
  return {
    name: 'cached-loader',
    loadCollection: async ({ filter }) => {
      // ... fetch data
      return {
        entries: data.map((item) => ({
          id: item.id,
          data: item,
          // You can optionally provide cache hints for each entry
          cacheHint: {
            tags: [`product-${item.id}`, `category-${item.category}`],
          },
        })),
        cacheHint: {
          // All fields are optional, and are combined with each entry's cache hints
          // tags are merged from all entries
          // lastModified is the most recent lastModified of all entries and the collection
          lastModified: new Date(item.lastModified),
          tags: ['products'],
        },
      };
    },
    loadEntry: async ({ filter }) => {
      // ... fetch single item
      return {
        id: item.id,
        data: item,
        cacheHint: {
          lastModified: new Date(item.lastModified),
          tags: [`product-${item.id}`, `category-${item.category}`],
        },
      };
    },
  };
}
```

You can then use these hints in your pages:

```astro
---
export const prerender = false; // Not needed in 'server' mode


import { getLiveEntry } from 'astro:content';


const { entry, error, cacheHint } = await getLiveEntry('products', Astro.params.id);


if (error) {
  return Astro.redirect('/404');
}


// Apply cache hints to response headers
if (cacheHint?.tags) {
  Astro.response.headers.set('Cache-Tag', cacheHint.tags.join(','));
}
if (cacheHint?.lastModified) {
  Astro.response.headers.set('Last-Modified', cacheHint.lastModified.toUTCString());
}
---


<h1>{entry.data.name}</h1>
<p>{entry.data.description}</p>
```

Note

Cache hints only provide values that can be used in other parts of your project and do not automatically cause the response to be cached by Astro. You can use them to create your own caching strategy, such as setting HTTP headers or using a CDN.

## Live collection limitations

[Section titled “Live collection limitations”](#live-collection-limitations)

Live content collections have some limitations compared to build-time collections:

* **No MDX support**: MDX cannot be rendered at runtime
* **No image optimization**: Images cannot be processed at runtime
* **Performance considerations**: Data is fetched on each request (unless cached)
* **No data store persistence**: Data is not saved to the content layer data store

## Differences from build-time collections

[Section titled “Differences from build-time collections”](#differences-from-build-time-collections)

Live collections use a different API than current preloaded content collections. Key differences include:

1. **Execution time**: Run at request time instead of build time
2. **Configuration file**: Use `src/live.config.ts` instead of `src/content.config.ts`
3. **Collection definition**: Use `defineLiveCollection()` instead of `defineCollection()`
4. **Loader API**: Implement `loadCollection` and `loadEntry` methods instead of the `load` method
5. **Data return**: Return data directly instead of storing in the data store
6. **User-facing functions**: Use `getLiveCollection`/`getLiveEntry` instead of `getCollection`/`getEntry`

For a complete overview and to give feedback on this experimental API, see the [Live Content collections RFC](https://github.com/withastro/roadmap/blob/feat/live-loaders/proposals/0055-live-content-loaders.md).

# Experimental preserve scripts order

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.5.0`

Renders multiple `<style>` and `<script>` tags in the same order as they were declared in the source code.

To enable this behavior, add the `experimental.preserveScriptOrder` feature flag to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"


export default defineConfig({
+  experimental: {
+    preserveScriptOrder: true
+  }
})
```

## Usage

[Section titled “Usage”](#usage)

This experimental flag requires no specific usage and only affects the order in which Astro renders your styles and scripts.

When rendering multiple `<style>` and `<script>` tags on the same page, Astro currently reverses their order in your generated HTML output. This can give unexpected results, for example, CSS styles being overridden by earlier defined style tags when your site is built. This experimental flag instead renders `<script>` and `<style>` tags in the order they are defined.

For example, the following component has two `<style>` tags and two `<script>` tags:

src/components/MyComponent.astro

```astro
<p>I am a component</p>
<style>
  body {
    background: red;
  }
</style>
<style>
  body {
    background: yellow;
  }
</style>
<script>
    console.log("hello")
</script>
<script>
    console.log("world!")
</script>
```

After compiling, Astro’s default behavior will create an inline style where `yellow` appears first, and then `red`. This means the `red` background is applied. Similarly with the two scripts, the word `world!` is logged first, and then `hello` second:

```css
body {background:#ff0} body {background:red}
```

```js
console.log("world!")
console.log("hello")
```

When `experimental.preserveScriptOrder` is set to `true`, the rendering order of `<style>` and `<script>` tags matches the order in which they are written. For the same example component, the style generated `red` appears first, and then `yellow`; as for the scripts, `hello` is logged first, and then `world!`:

```css
body {background:red} body {background:#ff0}
```

```js
console.log("hello")
console.log("world!")
```

In a future major version, Astro will preserve style and script order by default, but you can opt in to the future behavior early using the `experimental.preserveScriptOrder` flag.

# Experimental private meta environment variables inlining

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.13.0`

Astro 6.0 preview

The behavior enabled by this feature will become the default behavior in Astro 6.0.

You may wish to add this flag whenever it is convenient to do so. You can start enjoying the benefits sooner and will avoid the need to update your project code for the next major Astro version.

Astro allows you to configure a [type-safe schema for your environment variables](/en/guides/environment-variables/#type-safe-environment-variables), and converts variables imported via `astro:env` into the expected type. This is the recommended way to use environment variables in Astro, as it allows you to easily see and manage whether your variables are public or secret, available on the client or only on the server at build time, and the data type of your values.

However, you can still access your environment variables through `process.env` as well as `import.meta.env` directly if needed. This was the only way to use environment variables in Astro before `astro:env` was added in Astro 5.0, and its handling of `import.meta.env` includes some logic that was intended for earlier versions of Astro that is no longer necessary.

The `experimental.staticImportMetaEnv` flag updates the behavior when accessing `import.meta.env` directly to align with [Vite’s handling of environment variables](https://vite.dev/guide/env-and-mode.html#env-variables) and ensures that `import.meta.env` values are always inlined.

Currently, non-public environment variables are replaced by a reference to `process.env`. Additionally, Astro may also convert the value type of your environment variables used through `import.meta.env`, which can prevent access to some values such as the strings `"true"` (which is converted to a boolean value), and `"1"` (which is converted to a number).

The `experimental.staticImportMetaEnv` flag simplifies Astro’s default behavior, making it easier to understand and use. Astro will no longer replace any `import.meta.env` environment variables with a `process.env` call, nor will it coerce values.

To enable this feature, add the experimental flag in your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config"


export default defineConfig({
+  experimental: {
+    staticImportMetaEnv: true,
+  }
})
```

## Usage

[Section titled “Usage”](#usage)

Enabling this experimental flag will no longer convert string values into booleans or numbers, nor turn `import.meta.env` values into `process.env` calls. This aligns `import.meta.env`’s behavior in Astro with [Vite](https://vite.dev/guide/env-and-mode.html#env-variables).

In a future major version, Astro will switch to this behavior by default, but you can opt in to the future behavior early using the `experimental.staticImportMetaEnv` flag and, if necessary, [updating your project](#updating-your-project) accordingly.

### Updating your project

[Section titled “Updating your project”](#updating-your-project)

If you were relying on coercion, you may need to update your project code to apply it manually:

src/components/MyComponent.astro

```diff
-const enabled: boolean = import.meta.env.ENABLED;
+const enabled: boolean = import.meta.env.ENABLED === "true";
```

If you were relying on the transformation into `process.env`, you may need to update your project code to apply it manually:

src/components/MyComponent.astro

```diff
-const enabled: boolean = import.meta.env.DB_PASSWORD;
+const enabled: boolean = process.env.DB_PASSWORD;
```

You may also need to update types:

src/env.d.ts

```diff
interface ImportMetaEnv {
  readonly PUBLIC_POKEAPI: string;
  -readonly DB_PASSWORD: string;
  -readonly ENABLED: boolean;
  +readonly ENABLED: string;
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}


+namespace NodeJS {
  +interface ProcessEnv {
+    DB_PASSWORD: string;
+  }
+}
```

If you need more control over environment variables in Astro, we recommend you use [`astro:env`](/en/guides/environment-variables/).

# Image Service API

`astro:assets` was designed to make it easy for any image optimization service to build a service on top of Astro.

## What is an Image Service?

[Section titled “What is an Image Service?”](#what-is-an-image-service)

Astro provides two types of image services: Local and External.

* **Local services** handle image transformations directly at build for static sites, or at runtime both in development mode and for on-demand rendering. These are often wrappers around libraries like Sharp, ImageMagick, or Squoosh. In dev mode and in production routes rendered on demand, local services use an API endpoint to do the transformation.
* **External services** point to URLs and can add support for services such as Cloudinary, Vercel, or any [RIAPI](https://github.com/riapi/riapi)-compliant server.

## Building using the Image Services API

[Section titled “Building using the Image Services API”](#building-using-the-image-services-api)

Service definitions take the shape of an exported default object with various required methods (“hooks”).

External services provide a `getURL()` that points to the `src` of the output `<img>` tag.

Local services provide a `transform()` method to perform transformations on your image, and `getURL()` and `parseURL()` methods to use an endpoint for dev mode and when rendered on demand.

Both types of services can provide `getHTMLAttributes()` to determine the other attributes of the output `<img>` and `validateOptions()` to validate and augment the passed options.

### External Services

[Section titled “External Services”](#external-services)

An external service points to a remote URL to be used as the `src` attribute of the final `<img>` tag. This remote URL is responsible for downloading, transforming, and returning the image.

```ts
import type { ExternalImageService, ImageTransform, AstroConfig } from "astro";


const service: ExternalImageService = {
  validateOptions(options: ImageTransform, imageConfig: AstroConfig['image']) {
    const serviceConfig = imageConfig.service.config;


    // Enforce the user set max width.
    if (options.width && options.width > serviceConfig.maxWidth) {
      console.warn(`Image width ${options.width} exceeds max width ${serviceConfig.maxWidth}. Falling back to max width.`);
      options.width = serviceConfig.maxWidth;
    }


    return options;
  },
  getURL(options, imageConfig) {
    return `https://mysupercdn.com/${options.src}?q=${options.quality}&w=${options.width}&h=${options.height}`;
  },
  getHTMLAttributes(options, imageConfig) {
    const { src, format, quality, ...attributes } = options;
    return {
      ...attributes,
      loading: options.loading ?? 'lazy',
      decoding: options.decoding ?? 'async',
    };
  }
};




export default service;
```

### Local Services

[Section titled “Local Services”](#local-services)

To create your own local service, you can point to the [built-in endpoint](https://github.com/withastro/astro/blob/main/packages/astro/src/assets/endpoint/generic.ts) (`/_image`), or you can additionally create your own endpoint that can call the service’s methods.

```ts
import type { ImageTransform, LocalImageService, AstroConfig } from "astro";


const service: LocalImageService<AstroConfig["image"]> = {
  getURL(options: ImageTransform, imageConfig) {
    const searchParams = new URLSearchParams();
    searchParams.append('href', typeof options.src === "string" ? options.src : options.src.src);
    options.width && searchParams.append('w', options.width.toString());
    options.height && searchParams.append('h', options.height.toString());
    options.quality && searchParams.append('q', options.quality.toString());
    options.format && searchParams.append('f', options.format);
    return `/my_custom_endpoint_that_transforms_images?${searchParams}`;
    // Or use the built-in endpoint, which will call your parseURL and transform functions:
    // return `/_image?${searchParams}`;
  },
  parseURL(url: URL, imageConfig) {
    const params = url.searchParams;
    return {
      src: params.get('href')!,
      width: params.has('w') ? parseInt(params.get('w')!) : undefined,
      height: params.has('h') ? parseInt(params.get('h')!) : undefined,
      format: params.get('f'),
      quality: params.get('q'),
    };
  },
  async transform(inputBuffer: Uint8Array, options: { src: string, [key: string]: any }, imageConfig) {
    const { buffer } = await mySuperLibraryThatEncodesImages(options);
    return {
      data: buffer,
      format: options.format,
    };
  },
  getHTMLAttributes(options, imageConfig) {
    let targetWidth = options.width;
    let targetHeight = options.height;
    if (typeof options.src === "object") {
      const aspectRatio = options.src.width / options.src.height;


      if (targetHeight && !targetWidth) {
        targetWidth = Math.round(targetHeight * aspectRatio);
      } else if (targetWidth && !targetHeight) {
        targetHeight = Math.round(targetWidth / aspectRatio);
      }
    }


    const { src, width, height, format, quality, ...attributes } = options;


    return {
      ...attributes,
      width: targetWidth,
      height: targetHeight,
      loading: attributes.loading ?? 'lazy',
      decoding: attributes.decoding ?? 'async',
    };
  },
  propertiesToHash: ['src', 'width', 'height', 'format', 'quality'],
};
export default service;
```

At build time for static sites and pre-rendered routes, both `<Image />` and `getImage(options)` call the `transform()` function. They pass options either through component attributes or an `options` argument, respectively. The transformed images will be built to a `dist/_astro` folder. Their file names will contain a hash of the properties passed to `propertiesToHash`. This property is optional and will default to `['src', 'width', 'height', 'format', 'quality']`. If your custom image service has more options that change the generated images, add these to the array.

In dev mode and when using an adapter to render on demand, Astro doesn’t know ahead of time which images need to be optimized. Astro uses a GET endpoint (by default, `/_image`) to process the images at runtime. `<Image />` and `getImage()` pass their options to `getURL()`, which will return the endpoint URL. Then, the endpoint calls `parseURL()` and passes the resulting properties to `transform()`.

#### getConfiguredImageService & imageConfig

[Section titled “getConfiguredImageService & imageConfig”](#getconfiguredimageservice--imageconfig)

If you implement your own endpoint as an Astro endpoint, you can use `getConfiguredImageService` and `imageConfig` to call your service’s `parseURL` and `transform` methods and provide the image config.

To access the image service config ([`image.service.config`](/en/reference/configuration-reference/#imageservice)), you can use `imageConfig.service.config`.

src/api/my\_custom\_endpoint\_that\_transforms\_images.ts

```ts
import type { APIRoute } from "astro";
import { getConfiguredImageService, imageConfig } from 'astro:assets';


export const GET: APIRoute = async ({ request }) => {
  const imageService = await getConfiguredImageService();


  const imageTransform = imageService.parseURL(new URL(request.url), imageConfig);
  // ... fetch the image from imageTransform.src and store it in inputBuffer
  const { data, format } = await imageService.transform(inputBuffer, imageTransform, imageConfig);
  return new Response(data, {
      status: 200,
      headers: {
        'Content-Type': mime.getType(format) || ''
      }
    }
  );
}
```

[See the built-in endpoint](https://github.com/withastro/astro/blob/main/packages/astro/src/assets/endpoint/generic.ts) for a full example.

## Hooks

[Section titled “Hooks”](#hooks)

### `getURL()`

[Section titled “getURL()”](#geturl)

**Type:** `(options: ImageTransform, imageConfig: AstroConfig['image']) => string | Promise<string>`

**Added in:** `astro@2.1.0`

**Required for local and external services**

For local services, this hook returns the URL of the endpoint that generates your image (for on-demand rendering and in dev mode). It is unused during build. The local endpoint that `getURL()` points to may call both `parseURL()` and `transform()`.

For external services, this hook returns the final URL of the image.

For both types of services, `options` are the properties passed by the user as attributes of the `<Image />` component or as options to `getImage()`. They are of the following type:

```ts
export type ImageTransform = {
    // ESM imported images | remote/public image paths
    src: ImageMetadata | string;
    width?: number | undefined;
    height?: number | undefined;
    widths?: number[] | undefined;
    densities?: (number | `${number}x`)[] | undefined;
    quality?: ImageQuality  | undefined;
    format?: OutputFormat | undefined;
    fit?: ImageFit | undefined;
    position?: string | undefined;
    [key: string]: any;
};
```

### `parseURL()`

[Section titled “parseURL()”](#parseurl)

**Type:** `(url: URL, imageConfig: AstroConfig['image']) => { src: string, [key: string]: any } | undefined | Promise<{ src: string, [key: string]: any }> | Promise<undefined>`

**Added in:** `astro@2.1.0`

**Required for local services only; unavailable for external services**

This hook parses the generated URLs by `getURL()` back into an object with the different properties to be used by `transform` (for on-demand rendering and in dev mode). It is unused during build.

### `transform()`

[Section titled “transform()”](#transform)

**Type:** `(inputBuffer: Uint8Array, options: { src: string, [key: string]: any }, imageConfig: AstroConfig['image']) => Promise<{ data: Uint8Array; format: ImageOutputFormat }>`

**Added in:** `astro@2.1.0`

**Required for local services only; unavailable for external services**

This hook transforms and returns the image and is called during the build to create the final asset files.

You must return a `format` to ensure that the proper MIME type is served to users for on-demand rendering and development mode.

### `getHTMLAttributes()`

[Section titled “getHTMLAttributes()”](#gethtmlattributes)

**Type:** `(options: ImageTransform, imageConfig: AstroConfig['image'] ) => Record<string, any> | Promise<Record<string, any>>`

**Added in:** `astro@2.1.0`

**Optional for both local and external services**

This hook returns all additional attributes used to render the image as HTML, based on the parameters passed by the user (`options`).

### `getSrcSet()`

[Section titled “getSrcSet()”](#getsrcset)

**Type:** `(options: ImageTransform, imageConfig: AstroConfig['image'] ) => UnresolvedSrcSetValue[] | Promise<UnresolvedSrcSetValue[]>`

**Added in:** `astro@3.3.0`

**Optional for both local and external services.**

This hook generates multiple variants of the specified image, for example, to generate a `srcset` attribute on an `<img>` or `<picture>`’s `source`.

This hook returns an array of objects with the following properties:

```ts
export type UnresolvedSrcSetValue = {
  transform: ImageTransform;
  descriptor?: string;
  attributes?: Record<string, any>;
};
```

### `validateOptions()`

[Section titled “validateOptions()”](#validateoptions)

**Type:** `(options: ImageTransform, imageConfig: AstroConfig['image'] ) => ImageTransform | Promise<ImageTransform>`

**Added in:** `astro@2.1.4`

**Optional for both local and external services**

This hook allows you to validate and augment the options passed by the user. This is useful for setting default options, or telling the user that a parameter is required.

[See how `validateOptions()` is used in Astro built-in services](https://github.com/withastro/astro/blob/0ab6bad7dffd413c975ab00e545f8bc150f6a92f/packages/astro/src/assets/services/service.ts#L124).

## User configuration

[Section titled “User configuration”](#user-configuration)

Configure the image service to use in `astro.config.mjs`. The config takes the following form:

astro.config.mjs

```js
import { defineConfig } from "astro/config";


export default defineConfig({
  image: {
    service: {
      entrypoint: "your-entrypoint", // 'astro/assets/services/sharp' | string,
      config: {
        // ... service-specific config. Optional.
      }
    }
  },
});
```

## Utilities

[Section titled “Utilities”](#utilities)

Astro exposes a number of helper functions that can be used to develop a custom image service. These utilities can be imported from `astro/assets/utils`:

```ts
import {
    isRemoteAllowed,
    matchHostname,
    matchPathname,
    matchPattern,
    matchPort,
    matchProtocol,
    isESMImportedImage,
    isRemoteImage,
    resolveSrc,
    imageMetadata,
    emitESMImage,
    emitImageMetadata,
    getOrigQueryParams,
    inferRemoteSize,
    propsToFilename,
    hashTransform
} from "astro/assets/utils";
```

### `isRemoteAllowed()`

[Section titled “isRemoteAllowed()”](#isremoteallowed)

**Type:** `(src: string, { domains, remotePatterns }: { domains: string[], remotePatterns: RemotePattern[] }) => boolean`

**Added in:** `astro@4.0.0`

Determines whether a given remote resource, identified by its source URL, is allowed based on specified domains and remote patterns.

```ts
import { isRemoteAllowed } from 'astro/assets/utils';


const testImageURL = 'https://example.com/images/test.jpg';
const domains = ['example.com', 'anotherdomain.com'];
const remotePatterns = [
  { protocol: 'https', hostname: 'images.example.com', pathname: '/**' }, // Allow any path under this hostname
];


const url = new URL(testImageURL);
const isAllowed = isRemoteAllowed(url.href, { domains, remotePatterns });


console.log(`Is the remote image allowed? ${isAllowed}`);
```

### `matchHostname()`

[Section titled “matchHostname()”](#matchhostname)

**Type:** `(url: URL, hostname?: string, allowWildcard = false) => boolean`

**Added in:** `astro@4.0.0`

Matches a given URL’s hostname against a specified hostname, with optional support for wildcard patterns.

```ts
import { matchHostname } from 'astro/assets/utils';


const testURL = new URL('https://sub.example.com/path/to/resource');


// Example usage of matchHostname
const hostnameToMatch = 'example.com';


// Match without wildcard
const isMatchWithoutWildcard = matchHostname(testURL, hostnameToMatch);
console.log(`Does the hostname match without wildcard? ${isMatchWithoutWildcard}`); // Output: false


// Match with wildcard
const isMatchWithWildcard = matchHostname(testURL, hostnameToMatch, true);
console.log(`Does the hostname match with wildcard? ${isMatchWithWildcard}`); // Output: true
```

### `matchPathname()`

[Section titled “matchPathname()”](#matchpathname)

**Type:** `(url: URL, pathname?: string, allowWildcard = false) => boolean`

**Added in:** `astro@4.0.0`

Matches a given URL’s pathname against a specified pattern, with optional support for wildcards.

```ts
import { matchPathname } from 'astro/assets/utils';


const testURL = new URL('https://example.com/images/photo.jpg');


// Example pathname to match
const pathnameToMatch = '/images/photo.jpg';


// Match without wildcard
const isMatchWithoutWildcard = matchPathname(testURL, pathnameToMatch);
console.log(`Does the pathname match without wildcard? ${isMatchWithoutWildcard}`); // Output: true


// Match with wildcard
const wildcardPathname = '/images/*';
const isMatchWithWildcard = matchPathname(testURL, wildcardPathname, true);
console.log(`Does the pathname match with wildcard? ${isMatchWithWildcard}`); // Output: true
```

### `matchPattern()`

[Section titled “matchPattern()”](#matchpattern)

**Type:** `(url: URL, remotePattern: RemotePattern) => boolean`

**Added in:** `astro@4.0.0`

Evaluates whether a given URL matches the specified remote pattern based on protocol, hostname, port, and pathname.

```ts
import { matchPattern } from 'astro/assets/utils';


const testURL = new URL('https://images.example.com/photos/test.jpg');


// Define a remote pattern to match the URL
const remotePattern = {
  protocol: 'https',
  hostname: 'images.example.com',
  pathname: '/photos/**', // Wildcard to allow all files under /photos/
  port: '', // Optional: Match any port or leave empty for default
};


// Check if the URL matches the remote pattern
const isPatternMatched = matchPattern(testURL, remotePattern);


console.log(`Does the URL match the remote pattern? ${isPatternMatched}`); // Output: true
```

### `matchPort()`

[Section titled “matchPort()”](#matchport)

**Type:** `(url: URL, port?: string) => boolean`

**Added in:** `astro@4.0.0`

Checks if the given URL’s port matches the specified port. If no port is provided, it returns `true`.

```ts
import { matchPort } from 'astro/assets/utils';


const testURL1 = new URL('https://example.com:8080/resource');
const testURL2 = new URL('https://example.com/resource');


// Example usage of matchPort
const portToMatch = '8080';


// Match a URL with a port specified
const isPortMatch1 = matchPort(testURL1, portToMatch);
console.log(`Does the port match? ${isPortMatch1}`); // Output: true


// Match a URL without a port specified (default port will be assumed)
const isPortMatch2 = matchPort(testURL2, portToMatch);
console.log(`Does the port match? ${isPortMatch2}`); // Output: false


// Check a URL without explicitly providing a port (defaults to true if port is undefined)
const isPortMatch3 = matchPort(testURL1);
console.log(`Does the port match (no port specified)? ${isPortMatch3}`); // Output: true
```

### `matchProtocol()`

[Section titled “matchProtocol()”](#matchprotocol)

**Type:** `(url: URL, protocol?: string) => boolean`

**Added in:** `astro@4.0.0`

Compares the protocol of the provided URL with a specified protocol.

```ts
import { matchProtocol } from 'astro/assets/utils';


const testURL1 = new URL('https://example.com/resource');
const testURL2 = new URL('http://example.com/resource');


// Example usage of matchProtocol
const protocolToMatch = 'https';


// Match a URL with correct protocol
const isProtocolMatch1 = matchProtocol(testURL1, protocolToMatch);
console.log(`Does the protocol match for testURL1? ${isProtocolMatch1}`); // Output: true


// Match a URL with incorrect protocol
const isProtocolMatch2 = matchProtocol(testURL2, protocolToMatch);
console.log(`Does the protocol match for testURL2? ${isProtocolMatch2}`); // Output: false


// Match a URL without explicitly providing a protocol (defaults to true if protocol is undefined)
const isProtocolMatch3 = matchProtocol(testURL1);
console.log(`Does the protocol match (no protocol specified)? ${isProtocolMatch3}`); // Output: true
```

### `isESMImportedImage()`

[Section titled “isESMImportedImage()”](#isesmimportedimage)

**Type:** `(src: ImageMetadata | string) => boolean`

**Added in:** `astro@4.0.0`

Determines if the given source is an ECMAScript Module (ESM) imported image.

```ts
import { isESMImportedImage } from 'astro/assets/utils';


// Example usage of isESMImportedImage
const imageMetadataExample = {
  src: '/images/photo.jpg',
  width: 800,
  height: 600,
  format: 'jpg',
};


const filePathExample = '/images/photo.jpg';


// Check if the input is an ESM imported image
const isMetadataImage = isESMImportedImage(imageMetadataExample);
console.log(`Is imageMetadataExample an ESM imported image? ${isMetadataImage}`); // Output: true


const isFilePathImage = isESMImportedImage(filePathExample);
console.log(`Is filePathExample an ESM imported image? ${isFilePathImage}`); // Output: false
```

### `isRemoteImage()`

[Section titled “isRemoteImage()”](#isremoteimage)

**Type:** `(src: ImageMetadata | string) => boolean`

**Added in:** `astro@4.0.0`

Determines if the provided source is a remote image URL in the form of a string.

```ts
import { isRemoteImage } from 'astro/assets/utils';


// Example usage of isRemoteImage
const remoteImageUrl = 'https://example.com/images/photo.jpg';
const localImageMetadata = {
  src: '/images/photo.jpg',
  width: 800,
  height: 600,
  format: 'jpg',
};


// Check if the input is a remote image URL
const isRemote1 = isRemoteImage(remoteImageUrl);
console.log(`Is remoteImageUrl a remote image? ${isRemote1}`); // Output: true


const isRemote2 = isRemoteImage(localImageMetadata);
console.log(`Is localImageMetadata a remote image? ${isRemote2}`); // Output: false
```

### `resolveSrc()`

[Section titled “resolveSrc()”](#resolvesrc)

**Type:** `(src: UnresolvedImageTransform['src']) => Promise<string | ImageMetadata>`

**Added in:** `astro@4.0.0`

Returns the image source. This function ensures that if `src` is a Promise (e.g., a dynamic `import()`), it is awaited and the correct `src` is extracted. If `src` is already a resolved value, it is returned as-is.

```ts
import { resolveSrc } from 'astro/assets/utils';
import localImage from "./images/photo.jpg";


const resolvedLocal = await resolveSrc(localImage);
// will be `{ src: '/images/photo.jpg', width: 800, height: 600, format: 'jpg' }`


const resolvedRemote = await resolveSrc("https://example.com/remote-img.jpg");
// will be `"https://example.com/remote-img.jpg"`


const resolvedDynamic = await resolveSrc(import("./images/dynamic-image.jpg"))
// will be `{ src: '/images/dynamic-image.jpg', width: 800, height: 600, format: 'jpg' }`
```

### `imageMetadata()`

[Section titled “imageMetadata()”](#imagemetadata)

**Type:** `(data: Uint8Array, src?: string) => Promise<Omit<ImageMetadata, 'src' | 'fsPath'>>`

**Added in:** `astro@4.0.0`

Extracts image metadata such as dimensions, format, and orientation from the provided image data.

```ts
import { imageMetadata } from 'astro/assets/utils';


async function extractImageMetadata() {
  // Example image data (Uint8Array)
  const exampleImageData = new Uint8Array([/* ...binary image data... */]);


  // Optional source path (useful for debugging or additional metadata context)
  const sourcePath = '/images/photo.jpg';


  try {
    // Extract metadata from the image data
    const metadata = await imageMetadata(exampleImageData, sourcePath);


    console.log('Extracted Image Metadata:', metadata);
    // Example output:
    // {
    //   width: 800,
    //   height: 600,
    //   format: 'jpg',
    //   orientation: undefined
    // }
  } catch (error) {
    console.error('Failed to extract metadata from image:', error);
  }
}


await extractImageMetadata();
```

### `emitESMImage()`

[Section titled “emitESMImage()”](#emitesmimage)

Deprecated

Use the [`emitImageMetadata`](#emitimagemetadata) function instead.

**Type:** `(id: string | undefined, _watchMode: boolean, experimentalSvgEnabled: boolean, fileEmitter?: FileEmitter) => Promise<ImageMetadataWithContents | undefined>`

**Added in:** `astro@4.0.0`

Processes an image file and emits its metadata and optionally its contents. In build mode, the function uses `fileEmitter` to generate an asset reference. In development mode, it resolves to a local file URL with query parameters for metadata.

```ts
import { emitESMImage } from 'astro/assets/utils';


const imageId = '/images/photo.jpg';
const unusedWatchMode = false; // Deprecated, unused
const unusedExperimentalSvgEnabled = false; // Set to `true` only if you are using SVG and want the file data to be embedded


try {
  const result = await emitESMImage(imageId, unusedWatchMode, unusedExperimentalSvgEnabled);
  if (result) {
    console.log('Image metadata with contents:', result);
    // Example output:
    // {
    //   width: 800,
    //   height: 600,
    //   format: 'jpg',
    //   contents: Uint8Array([...])
    // }
  } else {
    console.log('No metadata was emitted for this image.');
  }
} catch (error) {
  console.error('Failed to emit ESM image:', error);
}
```

### `emitImageMetadata()`

[Section titled “emitImageMetadata()”](#emitimagemetadata)

**Type:** `(id: string | undefined, fileEmitter?: FileEmitter) => Promise<ImageMetadataWithContents | undefined>`

**Added in:** `astro@5.7.0`

Processes an image file and emits its metadata and optionally its contents. In build mode, the function uses `fileEmitter` to generate an asset reference. In development mode, it resolves to a local file URL with query parameters for metadata.

```ts
import { emitImageMetadata } from 'astro/assets/utils';


const imageId = '/images/photo.jpg';


try {
  const result = await emitImageMetadata(imageId);
  if (result) {
    console.log('Image metadata with contents:', result);
    // Example output:
    // {
    //   width: 800,
    //   height: 600,
    //   format: 'jpg',
    //   contents: Uint8Array([...])
    // }
  } else {
    console.log('No metadata was emitted for this image.');
  }
} catch (error) {
  console.error('Failed to emit ESM image:', error);
}
```

### `getOrigQueryParams()`

[Section titled “getOrigQueryParams()”](#getorigqueryparams)

**Type:** `(params: URLSearchParams) => Pick<ImageMetadata, 'width' | 'height' | 'format'> | undefined`

**Added in:** `astro@4.0.0`

Retrieves the `width`, `height`, and `format` of an image from a [`URLSearchParams` object](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams). If any of these parameters are missing or invalid, the function returns `undefined`.

```ts
import { getOrigQueryParams } from 'astro/assets/utils';


const url = new URL('https://example.com/image.jpg?width=800&height=600&format=jpg');
const queryParams = url.searchParams;


// Extract the original query parameters
const origParams = getOrigQueryParams(queryParams);


if (origParams) {
  console.log('Original query parameters:', origParams);
  // Example output:
  // {
  //   width: 800,
  //   height: 600,
  //   format: 'jpg'
  // }
} else {
  console.log('Failed to extract original query parameters.');
}
```

### `inferRemoteSize()`

[Section titled “inferRemoteSize()”](#inferremotesize)

**Type:** `(url: string) => Promise<Omit<ImageMetadata, 'src' | 'fsPath'>>`

**Added in:** `astro@4.0.0`

Infers the dimensions of a remote image by streaming its data and analyzing it progressively until sufficient metadata is available.

```ts
import { inferRemoteSize } from 'astro/assets/utils';


async function getRemoteImageSize() {
  const remoteImageUrl = 'https://example.com/image.jpg';


  try {
    // Infer remote image size from the URL
    const imageSize = await inferRemoteSize(remoteImageUrl);


    console.log('Inferred remote image size:', imageSize);
    // Example output:
    // {
    //   width: 1920,
    //   height: 1080,
    //   format: 'jpg'
    // }
  } catch (error) {
    console.error('Failed to infer the size of the remote image:', error);
  }
}


await getRemoteImageSize();
```

### `propsToFilename()`

[Section titled “propsToFilename()”](#propstofilename)

**Type:** `(filePath: string, transform: ImageTransform, hash: string) => string`

**Added in:** `astro@4.0.0`

Generates a formatted filename for an image based on its source path, transformation properties, and a unique hash.

The formatted filename follows this structure:

`<prefixDirname>/<baseFilename>_<hash><outputExtension>`

* `prefixDirname`: If the image is an ESM imported image, this is the directory name of the original file path; otherwise, it will be an empty string.
* `baseFilename`: The base name of the file or a hashed short name if the file is a `data:` URI.
* `hash`: A unique hash string generated to distinguish the transformed file.
* `outputExtension`: The desired output file extension derived from the `transform.format` or the original file extension.

```ts
import { propsToFilename } from 'astro/assets/utils';


function generateTransformedFilename() {
  const filePath = '/images/photo.jpg';
  const transform = {
    format: 'png',
    src: '/images/photo.jpg'
  };
  const hash = 'abcd1234';


  // Generate the transformed filename based on the file path, transformation, and hash
  const filename = propsToFilename(filePath, transform, hash);


  console.log('Generated transformed filename:', filename);
  // Example output: '/images/photo_abcd1234.png'
}


generateTransformedFilename();
```

### `hashTransform()`

[Section titled “hashTransform()”](#hashtransform)

**Type:** `(transform: ImageTransform, imageService: string, propertiesToHash: string[]) => string`

**Added in:** `astro@4.0.0`

Transforms the provided `transform` object into a hash string based on selected properties and the specified `imageService`.

```ts
import { hashTransform } from 'astro/assets/utils';


function generateTransformHash() {
  const transform = {
    src: '/images/photo.jpg',
    width: 800,
    height: 600,
    format: 'jpg',
  };


  const imageService = 'astroImageService';
  const propertiesToHash = ['width', 'height', 'format'];


  // Generate the hash based on the transform, image service, and properties
  const hash = hashTransform(transform, imageService, propertiesToHash);


  console.log('Generated transform hash:', hash);
  // Example output: 'd41d8cd98f00b204e9800998ecf8427e'
}


generateTransformHash();
```


---

**Navigation:** [← Previous](./12-configuration-reference.md) | [Index](./index.md) | [Next →](./14-astro-integration-api.md)
