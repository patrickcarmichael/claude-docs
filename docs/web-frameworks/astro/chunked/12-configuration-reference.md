**Navigation:** [← Previous](./11-create-a-dev-toolbar-app.md) | [Index](./index.md) | [Next →](./13-invalid-entry-inside-getstaticpaths-return-value.md)

---

# Configuration Reference

The following reference covers all supported configuration options in Astro. To learn more about configuring Astro, read our guide on [Configuring Astro](/en/guides/configuring-astro/).

astro.config.mjs

```js
import { defineConfig } from 'astro/config'


export default defineConfig({
  // your configuration options here...
})
```

## Top-Level Options

[Section titled “Top-Level Options”](#top-level-options)

### site

[Section titled “site”](#site)

**Type:** `string`

Your final, deployed URL. Astro uses this full URL to generate your sitemap and canonical URLs in your final build. It is strongly recommended that you set this configuration to get the most out of Astro.

```js
{
  site: 'https://www.my-site.dev'
}
```

### base

[Section titled “base”](#base)

**Type:** `string`

The base path to deploy to. Astro will use this path as the root for your pages and assets both in development and in production build.

In the example below, `astro dev` will start your server at `/docs`.

```js
{
  base: '/docs'
}
```

When using this option, all of your static asset imports and URLs should add the base as a prefix. You can access this value via `import.meta.env.BASE_URL`.

The value of `import.meta.env.BASE_URL` will be determined by your `trailingSlash` config, no matter what value you have set for `base`.

A trailing slash is always included if `trailingSlash: "always"` is set. If `trailingSlash: "never"` is set, `BASE_URL` will not include a trailing slash, even if `base` includes one.

Additionally, Astro will internally manipulate the configured value of `config.base` before making it available to integrations. The value of `config.base` as read by integrations will also be determined by your `trailingSlash` configuration in the same way.

In the example below, the values of `import.meta.env.BASE_URL` and `config.base` when processed will both be `/docs`:

```js
{
   base: '/docs/',
   trailingSlash: "never"
}
```

In the example below, the values of `import.meta.env.BASE_URL` and `config.base` when processed will both be `/docs/`:

```js
{
   base: '/docs',
   trailingSlash: "always"
}
```

### trailingSlash

[Section titled “trailingSlash”](#trailingslash)

**Type:** `'always' | 'never' | 'ignore'`\
**Default:** `'ignore'`

Set the route matching behavior for trailing slashes in the dev server and on-demand rendered pages. Choose from the following options:

* `'ignore'` - Match URLs regardless of whether a trailing ”/” exists. Requests for “/about” and “/about/” will both match the same route.
* `'always'` - Only match URLs that include a trailing slash (e.g: “/about/”). In production, requests for on-demand rendered URLs without a trailing slash will be redirected to the correct URL for your convenience. However, in development, they will display a warning page reminding you that you have `always` configured.
* `'never'` - Only match URLs that do not include a trailing slash (e.g: “/about”). In production, requests for on-demand rendered URLs with a trailing slash will be redirected to the correct URL for your convenience. However, in development, they will display a warning page reminding you that you have `never` configured.

When redirects occur in production for GET requests, the redirect will be a 301 (permanent) redirect. For all other request methods, it will be a 308 (permanent, and preserve the request method) redirect.

Trailing slashes on prerendered pages are handled by the hosting platform, and may not respect your chosen configuration. See your hosting platform’s documentation for more information. You cannot use Astro [redirects](#redirects) for this use case at this point.

```js
{
  // Example: Require a trailing slash during development
  trailingSlash: 'always'
}
```

**See Also:**

* build.format

### redirects

[Section titled “redirects”](#redirects)

**Type:** `Record<string, RedirectConfig>`\
**Default:** `{}`

**Added in:** `astro@2.9.0`

Specify a mapping of redirects where the key is the route to match and the value is the path to redirect to.

You can redirect both static and dynamic routes, but only to the same kind of route. For example, you cannot have a `'/article': '/blog/[...slug]'` redirect.

```js
export default defineConfig({
  redirects: {
   '/old': '/new',
   '/blog/[...slug]': '/articles/[...slug]',
   '/about': 'https://example.com/about',
   '/news': {
     status: 302,
     destination: 'https://example.com/news'
   },
   // '/product1/', '/product1' // Note, this is not supported
  }
})
```

For statically-generated sites with no adapter installed, this will produce a client redirect using a [`<meta http-equiv="refresh">` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#http-equiv) and does not support status codes.

When using SSR or with a static adapter in `output: static` mode, status codes are supported. Astro will serve redirected GET requests with a status of `301` and use a status of `308` for any other request method.

You can customize the [redirection status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#redirection_messages) using an object in the redirect config:

```js
export default defineConfig({
  redirects: {
    '/other': {
      status: 302,
      destination: '/place',
    },
  }
})
```

### output

[Section titled “output”](#output)

**Type:** `'static' | 'server'`\
**Default:** `'static'`

Specifies the output target for builds.

* `'static'` - Prerender all your pages by default, outputting a completely static site if none of your pages opt out of prerendering.
* `'server'` - Use server-side rendering (SSR) for all pages by default, always outputting a server-rendered site.

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  output: 'static'
})
```

**See Also:**

* adapter

### adapter

[Section titled “adapter”](#adapter)

**Type:** `AstroIntegration`

Deploy to your favorite server, serverless, or edge host with build adapters. Import one of our first-party adapters ([Cloudflare](/en/guides/integrations-guide/cloudflare/), [Netlify](/en/guides/integrations-guide/netlify/), [Node.js](/en/guides/integrations-guide/node/), [Vercel](/en/guides/integrations-guide/vercel/)) or explore [community adapters](https://astro.build/integrations/2/?search=\&categories%5B%5D=adapters) to enable on-demand rendering in your Astro project.

See our [on-demand rendering guide](/en/guides/on-demand-rendering/) for more on Astro’s server rendering options.

```js
import netlify from '@astrojs/netlify';
{
  // Example: Build for Netlify serverless deployment
  adapter: netlify(),
}
```

**See Also:**

* output

### integrations

[Section titled “integrations”](#integrations)

**Type:** `AstroIntegration[]`

Extend Astro with custom integrations. Integrations are your one-stop-shop for adding framework support (like Solid.js), new features (like sitemaps), and new libraries (like Partytown).

Read our [Integrations Guide](/en/guides/integrations-guide/) for help getting started with Astro Integrations.

```js
import react from '@astrojs/react';
import mdx from '@astrojs/mdx';
{
  // Example: Add React + MDX support to Astro
  integrations: [react(), mdx()]
}
```

### root

[Section titled “root”](#root)

**Type:** `string`\
**CLI:** `--root`\
**Default:** `"."` (current working directory)

You should only provide this option if you run the `astro` CLI commands in a directory other than the project root directory. Usually, this option is provided via the CLI instead of the Astro config file, since Astro needs to know your project root before it can locate your config file.

If you provide a relative path (ex: `--root: './my-project'`) Astro will resolve it against your current working directory.

#### Examples

[Section titled “Examples”](#examples)

```js
{
  root: './my-project-directory'
}
```

```bash
$ astro build --root ./my-project-directory
```

### srcDir

[Section titled “srcDir”](#srcdir)

**Type:** `string`\
**Default:** `"./src"`

Set the directory that Astro will read your site from.

The value can be either an absolute file system path or a path relative to the project root.

```js
{
  srcDir: './www'
}
```

### publicDir

[Section titled “publicDir”](#publicdir)

**Type:** `string`\
**Default:** `"./public"`

Set the directory for your static assets. Files in this directory are served at `/` during dev and copied to your build directory during build. These files are always served or copied as-is, without transform or bundling.

The value can be either an absolute file system path or a path relative to the project root.

```js
{
  publicDir: './my-custom-publicDir-directory'
}
```

### outDir

[Section titled “outDir”](#outdir)

**Type:** `string`\
**Default:** `"./dist"`

Set the directory that `astro build` writes your final build to.

The value can be either an absolute file system path or a path relative to the project root.

```js
{
  outDir: './my-custom-build-directory'
}
```

**See Also:**

* build.server

### cacheDir

[Section titled “cacheDir”](#cachedir)

**Type:** `string`\
**Default:** `"./node_modules/.astro"`

Set the directory for caching build artifacts. Files in this directory will be used in subsequent builds to speed up the build time.

The value can be either an absolute file system path or a path relative to the project root.

```js
{
  cacheDir: './my-custom-cache-directory'
}
```

### compressHTML

[Section titled “compressHTML”](#compresshtml)

**Type:** `boolean`\
**Default:** `true`

This is an option to minify your HTML output and reduce the size of your HTML files.

By default, Astro removes whitespace from your HTML, including line breaks, from `.astro` components in a lossless manner. Some whitespace may be kept as needed to preserve the visual rendering of your HTML. This occurs both in development mode and in the final build.

To disable HTML compression, set `compressHTML` to false.

```js
{
  compressHTML: false
}
```

### scopedStyleStrategy

[Section titled “scopedStyleStrategy”](#scopedstylestrategy)

**Type:** `'where' | 'class' | 'attribute'`\
**Default:** `'attribute'`

**Added in:** `astro@2.4`

Specify the strategy used for scoping styles within Astro components. Choose from:

* `'where'` - Use `:where` selectors, causing no specificity increase.
* `'class'` - Use class-based selectors, causing a +1 specificity increase.
* `'attribute'` - Use `data-` attributes, causing a +1 specificity increase.

Using `'class'` is helpful when you want to ensure that element selectors within an Astro component override global style defaults (e.g. from a global stylesheet). Using `'where'` gives you more control over specificity, but requires that you use higher-specificity selectors, layers, and other tools to control which selectors are applied. Using `'attribute'` is useful when you are manipulating the `class` attribute of elements and need to avoid conflicts between your own styling logic and Astro’s application of styles.

### security

[Section titled “security”](#security)

**Type:** `Record<"checkOrigin", boolean> | undefined`\
**Default:** `{checkOrigin: true}`

**Added in:** `astro@4.9.0`

Enables security measures for an Astro website.

These features only exist for pages rendered on demand (SSR) using `server` mode or pages that opt out of prerendering in `static` mode.

By default, Astro will automatically check that the “origin” header matches the URL sent by each request in on-demand rendered pages. You can disable this behavior by setting `checkOrigin` to `false`:

astro.config.mjs

```js
export default defineConfig({
  output: "server",
  security: {
    checkOrigin: false
  }
})
```

#### security.checkOrigin

[Section titled “security.checkOrigin”](#securitycheckorigin)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@4.9.0`

Performs a check that the “origin” header, automatically passed by all modern browsers, matches the URL sent by each `Request`. This is used to provide Cross-Site Request Forgery (CSRF) protection.

The “origin” check is executed only for pages rendered on demand, and only for the requests `POST`, `PATCH`, `DELETE` and `PUT` with one of the following `content-type` headers: `'application/x-www-form-urlencoded'`, `'multipart/form-data'`, `'text/plain'`.

If the “origin” header doesn’t match the `pathname` of the request, Astro will return a 403 status code and will not render the page.

#### security.allowedDomains

[Section titled “security.allowedDomains”](#securityalloweddomains)

**Type:** `Array<RemotePattern>`\
**Default:** `[]`

**Added in:** `astro@5.14.2`

Defines a list of permitted host patterns for incoming requests when using SSR. When configured, Astro will validate the `X-Forwarded-Host` header against these patterns for security. If the header doesn’t match any allowed pattern, the header is ignored and the request’s original host is used instead.

This prevents host header injection attacks where malicious actors can manipulate the `Astro.url` value by sending crafted `X-Forwarded-Host` headers.

Each pattern can specify `protocol`, `hostname`, and `port`. All three are validated if provided. The patterns support wildcards for flexible hostname matching:

```js
{
  security: {
    // Example: Allow any subdomain of example.com on https
    allowedDomains: [
      {
        hostname: '**.example.com',
        protocol: 'https'
      },
      {
        hostname: 'staging.myapp.com',
        protocol: 'https',
        port: '443'
      }
    ]
  }
}
```

When not configured, `X-Forwarded-Host` headers are not trusted and will be ignored.

### vite

[Section titled “vite”](#vite)

**Type:** `ViteUserConfig`

Pass additional configuration options to Vite. Useful when Astro doesn’t support some advanced configuration that you may need.

View the full `vite` configuration object documentation on [vite.dev](https://vite.dev/config/).

#### Examples

[Section titled “Examples”](#examples-1)

```js
{
  vite: {
    ssr: {
      // Example: Force a broken package to skip SSR processing, if needed
      external: ['broken-npm-package'],
    }
  }
}
```

```js
{
  vite: {
    // Example: Add custom vite plugins directly to your Astro project
    plugins: [myPlugin()],
  }
}
```

## Build Options

[Section titled “Build Options”](#build-options)

### build.format

[Section titled “build.format”](#buildformat)

**Type:** `('file' | 'directory' | 'preserve')`\
**Default:** `'directory'`

Control the output file format of each page. This value may be set by an adapter for you.

* `'file'`: Astro will generate an HTML file named for each page route. (e.g. `src/pages/about.astro` and `src/pages/about/index.astro` both build the file `/about.html`)
* `'directory'`: Astro will generate a directory with a nested `index.html` file for each page. (e.g. `src/pages/about.astro` and `src/pages/about/index.astro` both build the file `/about/index.html`)
* `'preserve'`: Astro will generate HTML files exactly as they appear in your source folder. (e.g. `src/pages/about.astro` builds `/about.html` and `src/pages/about/index.astro` builds the file `/about/index.html`)

```js
{
  build: {
    // Example: Generate `page.html` instead of `page/index.html` during build.
    format: 'file'
  }
}
```

#### Effect on Astro.url

[Section titled “Effect on Astro.url”](#effect-on-astrourl)

Setting `build.format` controls what `Astro.url` is set to during the build. When it is:

* `directory` - The `Astro.url.pathname` will include a trailing slash to mimic folder behavior. (e.g. `/foo/`)
* `file` - The `Astro.url.pathname` will include `.html`. (e.g. `/foo.html`)

This means that when you create relative URLs using `new URL('./relative', Astro.url)`, you will get consistent behavior between dev and build.

To prevent inconsistencies with trailing slash behaviour in dev, you can restrict the [`trailingSlash` option](#trailingslash) to `'always'` or `'never'` depending on your build format:

* `directory` - Set `trailingSlash: 'always'`
* `file` - Set `trailingSlash: 'never'`

### build.client

[Section titled “build.client”](#buildclient)

**Type:** `string`\
**Default:** `'./client'`

Controls the output directory of your client-side CSS and JavaScript when building a website with server-rendered pages. `outDir` controls where the code is built to.

This value is relative to the `outDir`.

```js
{
  output: 'server',
  build: {
    client: './client'
  }
}
```

### build.server

[Section titled “build.server”](#buildserver)

**Type:** `string`\
**Default:** `'./server'`

Controls the output directory of server JavaScript when building to SSR.

This value is relative to the `outDir`.

```js
{
  build: {
    server: './server'
  }
}
```

### build.assets

[Section titled “build.assets”](#buildassets)

**Type:** `string`\
**Default:** `'_astro'`

**Added in:** `astro@2.0.0`

Specifies the directory in the build output where Astro-generated assets (bundled JS and CSS for example) should live.

```js
{
  build: {
    assets: '_custom'
  }
}
```

**See Also:**

* outDir

### build.assetsPrefix

[Section titled “build.assetsPrefix”](#buildassetsprefix)

**Type:** `string | Record<string, string>`\
**Default:** `undefined`

**Added in:** `astro@2.2.0`

Specifies the prefix for Astro-generated asset links. This can be used if assets are served from a different domain than the current site.

This requires uploading the assets in your local `./dist/_astro` folder to a corresponding `/_astro/` folder on the remote domain. To rename the `_astro` path, specify a new directory in `build.assets`.

To fetch all assets uploaded to the same domain (e.g. `https://cdn.example.com/_astro/...`), set `assetsPrefix` to the root domain as a string (regardless of your `base` configuration):

```js
{
  build: {
    assetsPrefix: 'https://cdn.example.com'
  }
}
```

**Added in:** `astro@4.5.0`

You can also pass an object to `assetsPrefix` to specify a different domain for each file type. In this case, a `fallback` property is required and will be used by default for any other files.

```js
{
  build: {
    assetsPrefix: {
      'js': 'https://js.cdn.example.com',
      'mjs': 'https://js.cdn.example.com',
      'css': 'https://css.cdn.example.com',
      'fallback': 'https://cdn.example.com'
    }
  }
}
```

### build.serverEntry

[Section titled “build.serverEntry”](#buildserverentry)

**Type:** `string`\
**Default:** `'entry.mjs'`

Specifies the file name of the server entrypoint when building to SSR. This entrypoint is usually dependent on which host you are deploying to and will be set by your adapter for you.

Note that it is recommended that this file ends with `.mjs` so that the runtime detects that the file is a JavaScript module.

```js
{
  build: {
    serverEntry: 'main.mjs'
  }
}
```

### build.redirects

[Section titled “build.redirects”](#buildredirects)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@2.6.0`

Specifies whether redirects will be output to HTML during the build. This option only applies to `output: 'static'` mode; in SSR redirects are treated the same as all responses.

This option is mostly meant to be used by adapters that have special configuration files for redirects and do not need/want HTML based redirects.

```js
{
  build: {
    redirects: false
  }
}
```

### build.inlineStylesheets

[Section titled “build.inlineStylesheets”](#buildinlinestylesheets)

**Type:** `'always' | 'auto' | 'never'`\
**Default:** `auto`

**Added in:** `astro@2.6.0`

Control whether project styles are sent to the browser in a separate css file or inlined into `<style>` tags. Choose from the following options:

* `'always'` - project styles are inlined into `<style>` tags
* `'auto'` - only stylesheets smaller than `ViteConfig.build.assetsInlineLimit` (default: 4kb) are inlined. Otherwise, project styles are sent in external stylesheets.
* `'never'` - project styles are sent in external stylesheets

```js
{
  build: {
    inlineStylesheets: `never`,
  },
}
```

### build.concurrency

[Section titled “build.concurrency”](#buildconcurrency)

**Type:** `number`\
**Default:** `1`

**Added in:** `astro@4.16.0`

The number of pages to build in parallel.

**In most cases, you should not change the default value of `1`.**

Use this option only when other attempts to reduce the overall rendering time (e.g. batch or cache long running tasks like fetch calls or data access) are not possible or are insufficient. If the number is set too high, page rendering may slow down due to insufficient memory resources and because JS is single-threaded.

```js
{
  build: {
    concurrency: 2
  }
}
```

Breaking changes possible

This feature is stable and is not considered experimental. However, this feature is only intended to address difficult performance issues, and breaking changes may occur in a [minor release](/en/upgrade-astro/#semantic-versioning) to keep this option as performant as possible. Please check the [Astro CHANGELOG](https://github.com/withastro/astro/blob/refs/heads/next/packages/astro/CHANGELOG.md) for every minor release if you are using this feature.

## Server Options

[Section titled “Server Options”](#server-options)

Customize the Astro dev server, used by both `astro dev` and `astro preview`.

```js
{
  server: { port: 1234, host: true}
}
```

To set different configuration based on the command run (“dev”, “preview”) a function can also be passed to this configuration option.

```js
{
  // Example: Use the function syntax to customize based on command
  server: ({ command }) => ({ port: command === 'dev' ? 4321 : 4000 })
}
```

### server.host

[Section titled “server.host”](#serverhost)

**Type:** `string | boolean`\
**Default:** `false`

**Added in:** `astro@0.24.0`

Set which network IP addresses the server should listen on (i.e. non-localhost IPs).

* `false` - do not expose on a network IP address
* `true` - listen on all addresses, including LAN and public addresses
* `[custom-address]` - expose on a network IP address at `[custom-address]` (ex: `192.168.0.1`)

### server.port

[Section titled “server.port”](#serverport)

**Type:** `number`\
**Default:** `4321`

Set which port the server should listen on.

If the given port is already in use, Astro will automatically try the next available port.

```js
{
  server: { port: 8080 }
}
```

### server.allowedHosts

[Section titled “server.allowedHosts”](#serverallowedhosts)

**Type:** `Array<string> | true`\
**Default:** `[]`

**Added in:** `astro@5.4.0`

A list of hostnames that Astro is allowed to respond to. When the value is set to `true`, any hostname is allowed.

```js
{
  server: {
    allowedHosts: ['staging.example.com', 'qa.example.com']
  }
}
```

### server.open

[Section titled “server.open”](#serveropen)

**Type:** `string | boolean`\
**Default:** `false`

**Added in:** `astro@4.1.0`

Controls whether the dev server should open in your browser window on startup.

Pass a full URL string (e.g. “<http://example.com>”) or a pathname (e.g. “/about”) to specify the URL to open.

```js
{
  server: { open: "/about" }
}
```

### server.headers

[Section titled “server.headers”](#serverheaders)

**Type:** `OutgoingHttpHeaders`\
**Default:** `{}`

**Added in:** `astro@1.7.0`

Set custom HTTP response headers to be sent in `astro dev` and `astro preview`.

## Session Options

[Section titled “Session Options”](#session-options)

**Added in:** `astro@5.7.0`

Configures session storage for your Astro project. This is used to store session data in a persistent way, so that it can be accessed across different requests. Some adapters may provide a default session driver, but you can override it with your own configuration.

See [the sessions guide](/en/guides/sessions/) for more information.

astro.config.mjs

```js
  {
    session: {
      // The name of the Unstorage driver
      driver: 'redis',
      // The required options depend on the driver
      options: {
        url: process.env.REDIS_URL,
      },
      ttl: 3600, // 1 hour
    }
  }
```

### session.driver

[Section titled “session.driver”](#sessiondriver)

**Type:** `string | undefined`

**Added in:** `astro@5.7.0`

The Unstorage driver to use for session storage. The [Node](/en/guides/integrations-guide/node/#sessions), [Cloudflare](/en/guides/integrations-guide/cloudflare/#sessions), and [Netlify](/en/guides/integrations-guide/netlify/#sessions) adapters automatically configure a default driver for you, but you can specify your own if you would prefer or if you are using an adapter that does not provide one.

The value is the “Driver name” from the [Unstorage driver documentation](https://unstorage.unjs.io/drivers).

astro.config.mjs

```diff
{
  adapter: vercel(),
  session: {
+    driver: "redis",
  },
}
```

Note

Some drivers may need extra packages to be installed. Some drivers may also require environment variables or credentials to be set. See the [Unstorage documentation](https://unstorage.unjs.io/drivers) for more information.

### session.options

[Section titled “session.options”](#sessionoptions)

**Type:** `Record<string, unknown> | undefined`\
**Default:** `{}`

**Added in:** `astro@5.7.0`

The driver-specific options to use for session storage. The options depend on the driver you are using. See the [Unstorage documentation](https://unstorage.unjs.io/drivers) for more information on the options available for each driver.

astro.config.mjs

```diff
{
   session: {
     driver: "redis",
+     options: {
+       url: process.env.REDIS_URL
+     },
   }
}
```

### session.cookie

[Section titled “session.cookie”](#sessioncookie)

**Type:** `string | AstroCookieSetOptions | undefined`\
**Default:** `{ name: "astro-session", sameSite: "lax", httpOnly: true, secure: true }`

**Added in:** `astro@5.7.0`

The session cookie configuration. If set to a string, it will be used as the cookie name. Alternatively, you can pass an object with additional options. These will be merged with the defaults.

astro.config.mjs

```diff
{
 session: {
   +// If set to a string, it will be used as the cookie name.
+   cookie: "my-session-cookie",
 }
}
```

astro.config.mjs

```diff
{
 session: {
   // If set to an object, it will be used as the cookie options.
+   cookie: {
+     name: "my-session-cookie",
+     sameSite: "lax",
+     secure: true,
+   }
 }
}
```

### session.ttl

[Section titled “session.ttl”](#sessionttl)

**Type:** `number | undefined`\
**Default:** Infinity

**Added in:** `astro@5.7.0`

An optional default time-to-live expiration period for session values, in seconds.

By default, session values persist until they are deleted or the session is destroyed, and do not automatically expire because a particular amount of time has passed. Set `session.ttl` to add a default expiration period for your session values. Passing a `ttl` option to [`session.set()`](/en/reference/api-reference/#set) will override the global default for that individual entry.

astro.config.mjs

```diff
{
 session: {
   +// Set a default expiration period of 1 hour (3600 seconds)
+   ttl: 3600,
 }
}
```

Note

Setting a value for `ttl` does not automatically delete the value from storage after the time limit has passed.

Values from storage will only be deleted when there is an attempt to access them after the `ttl` period has expired. At this time, the session value will be undefined and only then will the value be deleted.

Individual drivers may also support a `ttl` option that will automatically delete sessions after the specified time. See your chosen driver’s documentation for more information.

## Dev Toolbar Options

[Section titled “Dev Toolbar Options”](#dev-toolbar-options)

### devToolbar.enabled

[Section titled “devToolbar.enabled”](#devtoolbarenabled)

**Type:** `boolean`\
**Default:** `true`

Whether to enable the Astro Dev Toolbar. This toolbar allows you to inspect your page islands, see helpful audits on performance and accessibility, and more.

This option is scoped to the entire project, to only disable the toolbar for yourself, run `npm run astro preferences disable devToolbar`. To disable the toolbar for all your Astro projects, run `npm run astro preferences disable devToolbar --global`.

## Prefetch Options

[Section titled “Prefetch Options”](#prefetch-options)

**Type:** `boolean | object`

Enable prefetching for links on your site to provide faster page transitions. (Enabled by default on pages using the `<ClientRouter />` router. Set `prefetch: false` to opt out of this behaviour.)

This configuration automatically adds a prefetch script to every page in the project giving you access to the `data-astro-prefetch` attribute. Add this attribute to any `<a />` link on your page to enable prefetching for that page.

```html
<a href="/about" data-astro-prefetch>About</a>
```

Further customize the default prefetching behavior using the [`prefetch.defaultStrategy`](#prefetchdefaultstrategy) and [`prefetch.prefetchAll`](#prefetchprefetchall) options.

See the [Prefetch guide](/en/guides/prefetch/) for more information.

### prefetch.prefetchAll

[Section titled “prefetch.prefetchAll”](#prefetchprefetchall)

**Type:** `boolean`

Enable prefetching for all links, including those without the `data-astro-prefetch` attribute. This value defaults to `true` when using the `<ClientRouter />` router. Otherwise, the default value is `false`.

```js
prefetch: {
  prefetchAll: true
}
```

When set to `true`, you can disable prefetching individually by setting `data-astro-prefetch="false"` on any individual links.

```html
<a href="/about" data-astro-prefetch="false">About</a>
```

### prefetch.defaultStrategy

[Section titled “prefetch.defaultStrategy”](#prefetchdefaultstrategy)

**Type:** `'tap' | 'hover' | 'viewport' | 'load'`\
**Default:** `'hover'`

The default prefetch strategy to use when the `data-astro-prefetch` attribute is set on a link with no value.

* `'tap'`: Prefetch just before you click on the link.
* `'hover'`: Prefetch when you hover over or focus on the link. (default)
* `'viewport'`: Prefetch as the links enter the viewport.
* `'load'`: Prefetch all links on the page after the page is loaded.

You can override this default value and select a different strategy for any individual link by setting a value on the attribute.

```html
<a href="/about" data-astro-prefetch="viewport">About</a>
```

## Image Options

[Section titled “Image Options”](#image-options)

### image.endpoint

[Section titled “image.endpoint”](#imageendpoint)

**Type:** `Object`\
**Default:** `{route: '/_image', entrypoint: undefined}`

**Added in:** `astro@3.1.0`

Set the endpoint to use for image optimization in dev and SSR. The `entrypoint` property can be set to `undefined` to use the default image endpoint.

```js
{
  image: {
    // Example: Use a custom image endpoint at `/custom_endpoint`
    endpoint: {
       route: '/custom_endpoint',
       entrypoint: 'src/my_endpoint.ts',
    },
  },
}
```

### image.service

[Section titled “image.service”](#imageservice)

**Type:** `Object`\
**Default:** `{entrypoint: 'astro/assets/services/sharp', config?: {}}`

**Added in:** `astro@2.1.0`

Set which image service is used for Astro’s assets support.

The value should be an object with an entrypoint for the image service to use and optionally, a config object to pass to the service.

The service entrypoint can be either one of the included services, or a third-party package.

```js
{
  image: {
    // Example: Enable the Sharp-based image service with a custom config
    service: {
       entrypoint: 'astro/assets/services/sharp',
       config: {
         limitInputPixels: false,
      },
     },
  },
}
```

#### image.service.config.limitInputPixels

[Section titled “image.service.config.limitInputPixels”](#imageserviceconfiglimitinputpixels)

**Type:** `number | boolean`\
**Default:** `true`

**Added in:** `astro@4.1.0`

Whether or not to limit the size of images that the Sharp image service will process.

Set `false` to bypass the default image size limit for the Sharp image service and process large images.

### image.domains

[Section titled “image.domains”](#imagedomains)

**Type:** `Array<string>`\
**Default:** `[]`

**Added in:** `astro@2.10.10`

Defines a list of permitted image source domains for remote image optimization. No other remote images will be optimized by Astro.

This option requires an array of individual domain names as strings. Wildcards are not permitted. Instead, use [`image.remotePatterns`](#imageremotepatterns) to define a list of allowed source URL patterns.

astro.config.mjs

```js
{
  image: {
    // Example: Allow remote image optimization from a single domain
    domains: ['astro.build'],
  },
}
```

### image.remotePatterns

[Section titled “image.remotePatterns”](#imageremotepatterns)

**Type:** `Array<RemotePattern>`\
**Default:** `[]`

**Added in:** `astro@2.10.10`

Defines a list of permitted image source URL patterns for remote image optimization.

`remotePatterns` can be configured with four properties:

1. protocol
2. hostname
3. port
4. pathname

```js
{
  image: {
    // Example: allow processing all images from your aws s3 bucket
    remotePatterns: [{
      protocol: 'https',
      hostname: '**.amazonaws.com',
    }],
  },
}
```

You can use wildcards to define the permitted `hostname` and `pathname` values as described below. Otherwise, only the exact values provided will be configured: `hostname`:

* Start with ’\*\*.’ to allow all subdomains (‘endsWith’).
* Start with ’\*.’ to allow only one level of subdomain.

`pathname`:

* End with ’/\*\*’ to allow all sub-routes (‘startsWith’).
* End with ’/\*’ to allow only one level of sub-route.

### image.responsiveStyles

[Section titled “image.responsiveStyles”](#imageresponsivestyles)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.10.0`

Whether to automatically add global styles for responsive images. You should enable this option unless you are styling the images yourself.

This option is only used when `layout` is set to `constrained`, `full-width`, or `fixed` using the configuration or the `layout` prop on the image component.

See [the images docs](/en/guides/images/#responsive-image-styles) for more information.

### image.layout

[Section titled “image.layout”](#imagelayout)

**Type:** `ImageLayout`\
**Default:** `undefined`

**Added in:** `astro@5.10.0`

The default layout type for responsive images. Can be overridden by the `layout` prop on the image component.

* `constrained` - The image will scale to fit the container, maintaining its aspect ratio, but will not exceed the specified dimensions.
* `fixed` - The image will maintain its original dimensions.
* `full-width` - The image will scale to fit the container, maintaining its aspect ratio.

See [the `layout` component property](/en/reference/modules/astro-assets/#layout) for more details.

### image.objectFit

[Section titled “image.objectFit”](#imageobjectfit)

**Type:** `ImageFit`\
**Default:** `"cover"`

**Added in:** `astro@5.10.0`

The [`object-fit` CSS property value](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit) for responsive images. Can be overridden by the `fit` prop on the image component. Requires a value for `layout` to be set.

See [the `fit` component property](/en/reference/modules/astro-assets/#fit) for more details.

### image.objectPosition

[Section titled “image.objectPosition”](#imageobjectposition)

**Type:** `string`\
**Default:** `"center"`

**Added in:** `astro@5.10.0`

The default [`object-position` CSS property value](https://developer.mozilla.org/en-US/docs/Web/CSS/object-position) for responsive images. Can be overridden by the `position` prop on the image component. Requires a value for `layout` to be set.

See [the `position` component property](/en/reference/modules/astro-assets/#position) for more details.

### image.breakpoints

[Section titled “image.breakpoints”](#imagebreakpoints)

**Type:** `Array<number>`\
**Default:** `[640, 750, 828, 1080, 1280, 1668, 2048, 2560] | [640, 750, 828, 960, 1080, 1280, 1668, 1920, 2048, 2560, 3200, 3840, 4480, 5120, 6016]`

**Added in:** `astro@5.10.0`

The breakpoints used to generate responsive images. Requires a value for `layout` to be set. The full list is not normally used, but is filtered according to the source and output size. The defaults used depend on whether a local or remote image service is used. For remote services the more comprehensive list is used, because only the required sizes are generated. For local services, the list is shorter to reduce the number of images generated.

## Markdown Options

[Section titled “Markdown Options”](#markdown-options)

### markdown.shikiConfig

[Section titled “markdown.shikiConfig”](#markdownshikiconfig)

**Type:** `Partial<ShikiConfig>`

Shiki is our default syntax highlighter. You can configure all options via the `markdown.shikiConfig` object:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
    shikiConfig: {
      // Choose from Shiki's built-in themes (or add your own)
      // https://shiki.style/themes
      theme: 'dracula',
      // Alternatively, provide multiple themes
      // See note below for using dual light/dark themes
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      // Disable the default colors
      // https://shiki.style/guide/dual-themes#without-default-color
      // (Added in v4.12.0)
      defaultColor: false,
      // Add custom languages
      // Note: Shiki has countless langs built-in, including .astro!
      // https://shiki.style/languages
      langs: [],
      // Add custom aliases for languages
      // Map an alias to a Shiki language ID: https://shiki.style/languages#bundled-languages
      // https://shiki.style/guide/load-lang#custom-language-aliases
      langAlias: {
        cjs: "javascript"
      },
      // Enable word wrap to prevent horizontal scrolling
      wrap: true,
      // Add custom transformers: https://shiki.style/guide/transformers
      // Find common transformers: https://shiki.style/packages/transformers
      transformers: [],
    },
  },
});
```

See the [code syntax highlighting guide](/en/guides/syntax-highlighting/) for usage and examples.

### markdown.syntaxHighlight

[Section titled “markdown.syntaxHighlight”](#markdownsyntaxhighlight)

**Type:** `SyntaxHighlightConfig | SyntaxHighlightConfigType | false`\
**Default:** `{ type: 'shiki', excludeLangs: ['math'] }`

Which syntax highlighter to use for Markdown code blocks (\`\`\`), if any. This determines the CSS classes that Astro will apply to your Markdown code blocks.

* `shiki` - use the [Shiki](https://shiki.style) highlighter (`github-dark` theme configured by default)
* `prism` - use the [Prism](https://prismjs.com/) highlighter and [provide your own Prism stylesheet](/en/guides/syntax-highlighting/#add-a-prism-stylesheet)
* `false` - do not apply syntax highlighting.

```js
{
  markdown: {
    // Example: Switch to use prism for syntax highlighting in Markdown
    syntaxHighlight: 'prism',
  }
}
```

For more control over syntax highlighting, you can instead specify a configuration object with the properties listed below.

#### markdown.syntaxHighlight.type

[Section titled “markdown.syntaxHighlight.type”](#markdownsyntaxhighlighttype)

**Type:** `'shiki' | 'prism'`\
**Default:** `'shiki'`

**Added in:** `astro@5.5.0`

The default CSS classes to apply to Markdown code blocks. (If no other syntax highlighting configuration is needed, you can instead set `markdown.syntaxHighlight` directly to `shiki`, `prism`, or `false`.)

#### markdown.syntaxHighlight.excludeLangs

[Section titled “markdown.syntaxHighlight.excludeLangs”](#markdownsyntaxhighlightexcludelangs)

**Type:** `Array<string>`\
**Default:** `['math']`

**Added in:** `astro@5.5.0`

An array of languages to exclude from the default syntax highlighting specified in `markdown.syntaxHighlight.type`. This can be useful when using tools that create diagrams from Markdown code blocks, such as Mermaid.js and D2.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
    syntaxHighlight: {
      type: 'shiki',
      excludeLangs: ['mermaid', 'math'],
    },
  },
});
```

### markdown.remarkPlugins

[Section titled “markdown.remarkPlugins”](#markdownremarkplugins)

**Type:** `RemarkPlugins`

Pass [remark plugins](https://github.com/remarkjs/remark) to customize how your Markdown is built. You can import and apply the plugin function (recommended), or pass the plugin name as a string.

```js
import remarkToc from 'remark-toc';
{
  markdown: {
    remarkPlugins: [ [remarkToc, { heading: "contents"} ] ]
  }
}
```

### markdown.rehypePlugins

[Section titled “markdown.rehypePlugins”](#markdownrehypeplugins)

**Type:** `RehypePlugins`

Pass [rehype plugins](https://github.com/remarkjs/remark-rehype) to customize how your Markdown’s output HTML is processed. You can import and apply the plugin function (recommended), or pass the plugin name as a string.

```js
import { rehypeAccessibleEmojis } from 'rehype-accessible-emojis';
{
  markdown: {
    rehypePlugins: [rehypeAccessibleEmojis]
  }
}
```

### markdown.gfm

[Section titled “markdown.gfm”](#markdowngfm)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@2.0.0`

Astro uses [GitHub-flavored Markdown](https://github.com/remarkjs/remark-gfm) by default. To disable this, set the `gfm` flag to `false`:

```js
{
  markdown: {
    gfm: false,
  }
}
```

### markdown.smartypants

[Section titled “markdown.smartypants”](#markdownsmartypants)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@2.0.0`

Astro uses the [SmartyPants formatter](https://daringfireball.net/projects/smartypants/) by default. To disable this, set the `smartypants` flag to `false`:

```js
{
  markdown: {
    smartypants: false,
  }
}
```

### markdown.remarkRehype

[Section titled “markdown.remarkRehype”](#markdownremarkrehype)

**Type:** `RemarkRehype`

Pass options to [remark-rehype](https://github.com/remarkjs/remark-rehype#api).

```js
{
  markdown: {
    // Example: Translate the footnotes text to another language, here are the default English values
    remarkRehype: { footnoteLabel: "Footnotes", footnoteBackLabel: "Back to reference 1"},
  },
};
```

## i18n

[Section titled “i18n”](#i18n)

**Type:** `object`

**Added in:** `astro@3.5.0`

Configures i18n routing and allows you to specify some customization options.

See our guide for more information on [internationalization in Astro](/en/guides/internationalization/)

### i18n.locales

[Section titled “i18n.locales”](#i18nlocales)

**Type:** `Locales`

**Added in:** `astro@3.5.0`

A list of all locales supported by the website. This is a required field.

Languages can be listed either as individual codes (e.g. `['en', 'es', 'pt-br']`) or mapped to a shared `path` of codes (e.g. `{ path: "english", codes: ["en", "en-US"]}`). These codes will be used to determine the URL structure of your deployed site.

No particular language code format or syntax is enforced, but your project folders containing your content files must match exactly the `locales` items in the list. In the case of multiple `codes` pointing to a custom URL path prefix, store your content files in a folder with the same name as the `path` configured.

### i18n.defaultLocale

[Section titled “i18n.defaultLocale”](#i18ndefaultlocale)

**Type:** `string`

**Added in:** `astro@3.5.0`

The default locale of your website/application, that is one of the specified `locales`. This is a required field.

No particular language format or syntax is enforced, but we suggest using lower-case and hyphens as needed (e.g. “es”, “pt-br”) for greatest compatibility.

### i18n.fallback

[Section titled “i18n.fallback”](#i18nfallback)

**Type:** `Record<string, string>`

**Added in:** `astro@3.5.0`

The fallback strategy when navigating to pages that do not exist (e.g. a translated page has not been created).

Use this object to declare a fallback `locale` route for each language you support. If no fallback is specified, then unavailable pages will return a 404.

##### Example

[Section titled “Example”](#example)

The following example configures your content fallback strategy to redirect unavailable pages in `/pt-br/` to their `es` version, and unavailable pages in `/fr/` to their `en` version. Unavailable `/es/` pages will return a 404.

```js
export default defineConfig({
  i18n: {
    defaultLocale: "en",
    locales: ["en", "fr", "pt-br", "es"],
    fallback: {
      pt: "es",
      fr: "en"
    }
  }
})
```

### i18n.routing

[Section titled “i18n.routing”](#i18nrouting)

**Type:** `object | "manual"`\
**Default:** `object`

**Added in:** `astro@3.7.0`

Controls the routing strategy to determine your site URLs. Set this based on your folder/URL path configuration for your default language.

```js
export default defineConfig({
  i18n: {
    defaultLocale: "en",
    locales: ["en", "fr"],
    routing: {
      prefixDefaultLocale: false,
      redirectToDefaultLocale: true,
      fallbackType: "redirect",
    }
  }
})
```

Since 4.6.0, this option can also be set to `manual`. When this routing strategy is enabled, Astro will **disable** its i18n middleware and no other `routing` options (e.g. `prefixDefaultLocale`) may be configured. You will be responsible for writing your own routing logic, or executing Astro’s i18n middleware manually alongside your own.

```js
export default defineConfig({
  i18n: {
    defaultLocale: "en",
    locales: ["en", "fr"],
    routing: "manual"
  }
})
```

#### i18n.routing.prefixDefaultLocale

[Section titled “i18n.routing.prefixDefaultLocale”](#i18nroutingprefixdefaultlocale)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@3.7.0`

When `false`, only non-default languages will display a language prefix. The `defaultLocale` will not show a language prefix and content files do not exist in a localized folder. URLs will be of the form `example.com/[locale]/content/` for all non-default languages, but `example.com/content/` for the default locale.

When `true`, all URLs will display a language prefix. URLs will be of the form `example.com/[locale]/content/` for every route, including the default language. Localized folders are used for every language, including the default.

```js
export default defineConfig({
  i18n: {
    defaultLocale: "en",
    locales: ["en", "fr", "pt-br", "es"],
    routing: {
      prefixDefaultLocale: true,
    }
  }
})
```

#### i18n.routing.redirectToDefaultLocale

[Section titled “i18n.routing.redirectToDefaultLocale”](#i18nroutingredirecttodefaultlocale)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@4.2.0`

Configures whether or not the home URL (`/`) generated by `src/pages/index.astro` will redirect to `/[defaultLocale]` when `prefixDefaultLocale: true` is set.

Set `redirectToDefaultLocale: false` to disable this automatic redirection at the root of your site:

astro.config.mjs

```js
export default defineConfig({
  i18n:{
    defaultLocale: "en",
    locales: ["en", "fr"],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false
    }
  }
})
```

#### i18n.routing.fallbackType

[Section titled “i18n.routing.fallbackType”](#i18nroutingfallbacktype)

**Type:** `"redirect" | "rewrite"`\
**Default:** `"redirect"`

**Added in:** `astro@4.15.0`

When [`i18n.fallback`](#i18nfallback) is configured to avoid showing a 404 page for missing page routes, this option controls whether to [redirect](/en/guides/routing/#redirects) to the fallback page, or to [rewrite](/en/guides/routing/#rewrites) the fallback page’s content in place.

By default, Astro’s i18n routing creates pages that redirect your visitors to a new destination based on your fallback configuration. The browser will refresh and show the destination address in the URL bar.

When `i18n.routing.fallback: "rewrite"` is configured, Astro will create pages that render the contents of the fallback page on the original, requested URL.

With the following configuration, if you have the file `src/pages/en/about.astro` but not `src/pages/fr/about.astro`, the `astro build` command will generate `dist/fr/about.html` with the same content as the `dist/en/about.html` page. Your site visitor will see the English version of the page at `https://example.com/fr/about/` and will not be redirected.

astro.config.mjs

```js
export default defineConfig({
   i18n: {
    defaultLocale: "en",
    locales: ["en", "fr"],
    routing: {
      prefixDefaultLocale: false,
      fallbackType: "rewrite",
    },
    fallback: {
      fr: "en",
    }
  },
})
```

### i18n.domains

[Section titled “i18n.domains”](#i18ndomains)

**Type:** `Record<string, string>`\
**Default:** `{}`

**Added in:** `astro@4.3.0`

Configures the URL pattern of one or more supported languages to use a custom domain (or sub-domain).

When a locale is mapped to a domain, a `/[locale]/` path prefix will not be used. However, localized folders within `src/pages/` are still required, including for your configured `defaultLocale`.

Any other locale not configured will default to a localized path-based URL according to your `prefixDefaultLocale` strategy (e.g. `https://example.com/[locale]/blog`).

astro.config.mjs

```js
export default defineConfig({
   site: "https://example.com",
   output: "server", // required, with no prerendered pages
   adapter: node({
     mode: 'standalone',
   }),
   i18n: {
    defaultLocale: "en",
    locales: ["en", "fr", "pt-br", "es"],
    prefixDefaultLocale: false,
    domains: {
      fr: "https://fr.example.com",
      es: "https://example.es"
    }
  },
})
```

Both page routes built and URLs returned by the `astro:i18n` helper functions [`getAbsoluteLocaleUrl()`](/en/reference/modules/astro-i18n/#getabsolutelocaleurl) and [`getAbsoluteLocaleUrlList()`](/en/reference/modules/astro-i18n/#getabsolutelocaleurllist) will use the options set in `i18n.domains`.

See the [Internationalization Guide](/en/guides/internationalization/#domains) for more details, including the limitations of this feature.

## env

[Section titled “env”](#env)

**Type:** `object`\
**Default:** `{}`

**Added in:** `astro@5.0.0`

Configuration options for type-safe environment variables.

See our guide for more information on [environment variables in Astro](/en/guides/environment-variables/).

### env.schema

[Section titled “env.schema”](#envschema)

**Type:** `EnvSchema`\
**Default:** `{}`

**Added in:** `astro@5.0.0`

An object that uses `envField` to define the data type and properties of your environment variables: `context` (client or server), `access` (public or secret), a `default` value to use, and whether or not this environment variable is `optional` (defaults to `false`).

astro.config.mjs

```js
import { defineConfig, envField } from "astro/config"


export default defineConfig({
  env: {
    schema: {
      API_URL: envField.string({ context: "client", access: "public", optional: true }),
      PORT: envField.number({ context: "server", access: "public", default: 4321 }),
      API_SECRET: envField.string({ context: "server", access: "secret" }),
    }
  }
})
```

`envField` supports four data types: string, number, enum, and boolean. `context` and `access` are required properties for all data types. The following shows the complete list of properties available for each data type:

```js
import { envField } from "astro/config"


envField.string({
   // context & access
   optional: true,
   default: "foo",
   max: 20,
   min: 1,
   length: 13,
   url: true,
   includes: "oo",
   startsWith: "f",
   endsWith: "o",
})
envField.number({
   // context & access
   optional: true,
   default: 15,
   gt: 2,
   min: 1,
   lt: 3,
   max: 4,
   int: true,
})
envField.boolean({
   // context & access
   optional: true,
   default: true,
})
envField.enum({
   // context & access
   values: ['foo', 'bar', 'baz'], // required
   optional: true,
   default: 'baz',
})
```

### env.validateSecrets

[Section titled “env.validateSecrets”](#envvalidatesecrets)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.0.0`

Whether or not to validate secrets on the server when starting the dev server or running a build.

By default, only public variables are validated on the server when starting the dev server or a build, and private variables are validated at runtime only. If enabled, private variables will also be checked on start. This is useful in some continuous integration (CI) pipelines to make sure all your secrets are correctly set before deploying.

astro.config.mjs

```js
import { defineConfig, envField } from "astro/config"


export default defineConfig({
  env: {
    schema: {
      // ...
    },
    validateSecrets: true
  }
})
```

# Astro Container API (experimental)

**Added in:** `astro@4.9.0`

The Container API allows you to render Astro components in isolation.

This experimental server-side API unlocks a variety of potential future uses, but is currently scoped to allow [testing of `.astro` component output](/en/guides/testing/#vitest-and-container-api) in `vite` environments such as `vitest`.

It also allows you to [manually load rendering scripts](#adding-a-renderer-manually) for creating containers in pages rendered on demand or other “shell” environments outside of `vite` (e.g. inside a PHP or Elixir application).

This API allows you to [create a new container](#create), and render an Astro component returning [a string](#rendertostring) or a [`Response`](#rendertoresponse).

This API is experimental and subject to breaking changes, even in [minor or patch releases](/en/upgrade-astro/#semantic-versioning). Please consult [the Astro CHANGELOG](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for changes as they occur. This page will always be updated with the most current information for the latest version of Astro.

## `create()`

[Section titled “create()”](#create)

**Type:** `(options?: AstroContainerOptions) => Promise<experimental_AstroContainer>`

Creates a new instance of the container.

```js
import { experimental_AstroContainer } from "astro/container";


const container = await experimental_AstroContainer.create();
```

It accepts an object with the following options:

```ts
export type AstroContainerOptions = {
  streaming?: boolean;
  renderers?: AddServerRenderer[];
};


export type AddServerRenderer =
  | {
      renderer: NamedSSRLoadedRendererValue;
      name: never;
    }
  | {
      renderer: SSRLoadedRendererValue;
      name: string;
    };
```

### `streaming` option

[Section titled “streaming option”](#streaming-option)

**Type:** `boolean`\
**Default:** `false`

Enables rendering components using [HTML streaming](/en/guides/on-demand-rendering/#html-streaming).

### `renderers` option

[Section titled “renderers option”](#renderers-option)

**Type:** `AddServerRenderer[]`\
**Default:** `[]`

A list of loaded client renderers required by the component. Use this if your `.astro` component renders any [UI framework components](/en/guides/framework-components/) or MDX using an official Astro integration (e.g. React, Vue, etc.).

Renderers can be added through the Container API automatically for static applications, or cases where the container isn’t called at runtime (e.g. testing with `vitest`).

For [on-demand rendered applications](/en/guides/on-demand-rendering/), or cases where the container is called at runtime or inside other “shells” (e.g. PHP, Ruby, Java, etc.), renderers must be manually imported.

#### Adding a renderer through the Container API

[Section titled “Adding a renderer through the Container API”](#adding-a-renderer-through-the-container-api)

For each official Astro integration, import and use the `getContainerRenderer()` helper function to expose its client and server rendering scripts. These are available for `@astrojs/react`, `@astrojs/preact`, `@astrojs/solid-js`, `@astrojs/svelte`, `@astrojs/vue`, and `@astrojs/mdx`.

For renderer packages outside the `@astrojs` npm org, look in their documentation for `getContainerRenderer()` or a similar function provided.

When using `vite` (`vitest`, Astro integrations, etc.), the renderers are loaded with the function `loadRenderers()` from the virtual module `astro:container`.

Caution

Outside `vite` or for on-demand usage, you’ll have to [load the renderers manually](#adding-a-renderer-manually).

The following example provides the necessary object to render an Astro component that renders a React component and a Svelte component:

```js
import { getContainerRenderer as reactContainerRenderer } from "@astrojs/react";
import { getContainerRenderer as svelteContainerRenderer } from "@astrojs/svelte";
import { loadRenderers } from "astro:container";


const renderers = await loadRenderers([reactContainerRenderer(), svelteContainerRenderer()]);
const container = await experimental_AstroContainer.create({
    renderers
})
const result = await container.renderToString(ReactWrapper);
```

#### Adding a renderer manually

[Section titled “Adding a renderer manually”](#adding-a-renderer-manually)

When the container is called at runtime, or inside other “shells”, the `astro:container` virtual module’s helper functions are not available. You must import the necessary server and client renderers manually and store them inside the container using `addServerRenderer` and `addClientRenderer`.

Server renderers are required to build your project, and must be stored in the container for every framework used. Client renderers are additionally needed to any hydrate client-side components using [`client:*` directives](/en/reference/directives-reference/#client-directives).

Only one import statement is needed per framework. Importing a renderer makes both the server and client renderers available to your container. However, **server renderers must be added to your container before client renderers**. This allows your entire container to render first, and then hydrate any interactive components.

The following example manually imports the necessary server renderers to be able to display static Vue components and `.mdx` pages. It additionally adds both server and client renderers for interactive React components.

```js
import reactRenderer from "@astrojs/react/server.js";
import vueRenderer from "@astrojs/vue/server.js";
import mdxRenderer from "@astrojs/mdx/server.js";


const container = await experimental_AstroContainer.create();
container.addServerRenderer({ renderer: vueRenderer });
container.addServerRenderer({ renderer: mdxRenderer });


container.addServerRenderer({ renderer: reactRenderer });
container.addClientRenderer({ name: "@astrojs/react", entrypoint: "@astrojs/react/client.js" });
```

## `renderToString()`

[Section titled “renderToString()”](#rendertostring)

**Type:** `(component: AstroComponentFactory; options?: ContainerRenderOptions) => Promise<string>`

This function renders a specified component inside a container. It takes an Astro component as an argument and it returns a string that represents the HTML/content rendered by the Astro component.

```js
import { experimental_AstroContainer } from "astro/container";
import Card from "../src/components/Card.astro";


const container = await experimental_AstroContainer.create();
const result = await container.renderToString(Card);
```

Under the hood, this function calls [`renderToResponse()`](#rendertoresponse) and `Response.text()`.

It also accepts an object as a second argument that can contain a [number of options](#rendering-options).

## `renderToResponse()`

[Section titled “renderToResponse()”](#rendertoresponse)

**Type:** `(component: AstroComponentFactory; options?: ContainerRenderOptions) => Promise<Response>`

It renders a component, and it returns a `Response` object.

```js
import { experimental_AstroContainer } from "astro/container";
import Card from "../src/components/Card.astro";


const container = await experimental_AstroContainer.create();
const result = await container.renderToResponse(Card);
```

It also accepts an object as a second argument that can contain a [number of options](#rendering-options).

## Rendering options

[Section titled “Rendering options”](#rendering-options)

Both [`renderToResponse()`](#rendertoresponse) and [`renderToString()`](#rendertostring) accept an object as their second argument:

```ts
export type ContainerRenderOptions = {
  slots?: Record<string, any>;
  props?: Record<string, unknown>;
  request?: Request;
  params?: Record<string, string | undefined>;
  locals?: App.Locals;
  routeType?: RouteType;
  partial?: boolean;
};
```

These optional values can be passed to the rendering function in order to provide additional information necessary for an Astro component to properly render.

### `slots`

[Section titled “slots”](#slots)

**Type**: `Record<string, any>`

An option to pass content to be rendered with [`<slots>`](/en/basics/astro-components/#slots).

If your Astro component renders one default slot, pass an object with `default` as the key:

```js
import Card from "../src/components/Card.astro";


const result = await container.renderToString(Card, {
  slots: { default: "Some value" }
});
```

If your component renders named slots, use the slot names as the object keys:

```astro
---
---
<div>
  <slot name="header" />
  <slot name="footer" />
</div>
```

```js
import Card from "../src/components/Card.astro";


const result = await container.renderToString(Card, {
  slots: {
    header: "Header content",
    footer: "Footer"
  }
});
```

You can also render components in cascade:

```astro
---
---
<div>
  <slot name="header" />
  <slot name="footer" />
</div>
```

```js
import Card from "../src/components/Card.astro";
import CardHeader from "../src/components/CardHeader.astro";
import CardFooter from "../src/components/CardFooter.astro";


const result = await container.renderToString(Card, {
  slots: {
    header: await container.renderToString(CardHeader),
    footer:  await container.renderToString(CardFooter)
  }
});
```

### `props` option

[Section titled “props option”](#props-option)

**Type**: `Record<string, unknown>`

An option to pass [properties](/en/basics/astro-components/#component-props) for Astro components.

```js
import Card from "../src/components/Card.astro";


const result = await container.renderToString(Card, {
  props: { name: "Hello, world!" }
});
```

```astro
---
// For TypeScript support
interface Props {
  name: string;
};


const { name } = Astro.props;
---
<div>
  {name}
</div>
```

### `request` option

[Section titled “request option”](#request-option)

**Type**: `Request`

An option to pass a `Request` with information about the path/URL the component will render.

Use this option when your component needs to read information like `Astro.url` or `Astro.request`.

You can also inject possible headers or cookies.

```js
import Card from "../src/components/Card.astro";


const result = await container.renderToString(Card, {
  request: new Request("https://example.com/blog", {
    headers: {
      "x-some-secret-header": "test-value"
    }
  })
});
```

### `params` option

[Section titled “params option”](#params-option)

**Type**: `Record<string, string | undefined>`

An object to pass information about the path parameter to an Astro component responsible for [generating dynamic routes](/en/guides/routing/#dynamic-routes).

Use this option when your component needs a value for `Astro.params` in order to generate a single route dynamically.

```astro
---
const { locale, slug } = Astro.params;
---
<div></div>
```

```js
import LocaleSlug from "../src/components/[locale]/[slug].astro";


const result = await container.renderToString(LocaleSlug, {
  params: {
    locale: "en",
    slug: "getting-started"
  }
});
```

### `locals` options

[Section titled “locals options”](#locals-options)

**Type**: `App.Locals`

An option to pass information from [`Astro.locals`](/en/reference/api-reference/#locals) for rendering your component.

Use this option to when your component needs information stored during the lifecycle of a request in order to render, such as logged in status.

```astro
---
const { checkAuth } = Astro.locals;
const isAuthenticated = checkAuth();
---
{isAuthenticated ? <span>You're in</span> : <span>You're out</span> }
```

```js
import Card from "../src/components/Card.astro";


test("User is in", async () => {
  const result = await container.renderToString(Card, {
    locals: {
      checkAuth() { return true; }
    }
  });


  // assert result contains "You're in"
});




test("User is out", async () => {
  const result = await container.renderToString(Card, {
    locals: {
      checkAuth() { return false; }
    }
  });


  // assert result contains "You're out"
});
```

### `routeType` option

[Section titled “routeType option”](#routetype-option)

**Type**: `RouteType`

An option available when using `renderToResponse()` to specify that you are rendering an [endpoint](/en/guides/endpoints/):

```js
container.renderToString(Endpoint, { routeType: "endpoint" });
```

```js
import * as Endpoint from "../src/pages/api/endpoint.js";


const response = await container.renderToResponse(Endpoint, {
  routeType: "endpoint"
});
const json = await response.json();
```

To test your endpoint on methods such as `POST`, `PATCH`, etc., use the `request` option to call the correct function:

```js
export function GET() {}


// need to test this
export function POST() {}
```

```diff
import * as Endpoint from "../src/pages/api/endpoint.js";


const response = await container.renderToResponse(Endpoint, {
    routeType: "endpoint",
    request: new Request("https://example.com", {
      method: "POST" // Specify POST method for testing
    })
});
const json = await response.json();
```

### `partial` option

[Section titled “partial option”](#partial-option)

**Type:** `boolean`\
**Default:** `true`

**Added in:** `astro@4.16.6`

Whether or not the Container API renders components as if they were [page partials](/en/basics/astro-pages/#page-partials). This is usually the behavior you want when rendering `components.boolean` so you can render components without a full page shell.

To render a component as a full Astro page, including `<!DOCTYPE html>`, you can opt-out of this behavior by setting `partial` to `false`:

```diff
import Blog from "../src/pages/Blog.astro";


const result = await container.renderToString(Card, {
    partial: false
});
console.log(result) // includes `<!DOCTYPE html>` at the beginning of the HTML
```

# Astro Content Loader API

Astro’s Content Loader API allows you to load your data from any source, local or remote, and interact with Astro’s content layer to manage your [content collections](/en/guides/content-collections/).

## What is a loader?

[Section titled “What is a loader?”](#what-is-a-loader)

Astro loaders allow you to load data into [content collections](/en/guides/content-collections/), which can then be used in pages and components. The [built-in `glob()` and `file()` loaders](/en/guides/content-collections/#built-in-loaders) are used to load content from the file system, and you can create your own loaders to load content from other sources.

Each collection needs [a loader defined in its schema](/en/guides/content-collections/#defining-the-collection-loader). You can define a loader inline in your project’s `src/content.config.ts` file, share one loader between multiple collections, or even [publish your loader to NPM as a package](/en/reference/publish-to-npm/) to share with others and be included in our integrations library.

## Built-in loaders

[Section titled “Built-in loaders”](#built-in-loaders)

Astro provides two built-in loaders to help you fetch your collections. Both offer options to suit a wide range of use cases.

### `glob()` loader

[Section titled “glob() loader”](#glob-loader)

**Type:** `(options: GlobOptions) => Loader`

**Added in:** `astro@5.0.0`

The `glob()` loader creates entries from directories of files from anywhere on the filesystem. The supported file types are Markdown, MDX, Markdoc, JSON, YAML, and TOML files.

This loader accepts an object with the following properties: `pattern`, `base` (optional), and `generateId` (optional).

src/content.config.ts

```ts
import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';


const pages = defineCollection({
  /* Retrieve all Markdown files in your pages directory. */
  loader: glob({ pattern: "**/*.md", base: "./src/data/pages" }),
  schema: /* ... */
});
const blog = defineCollection({
  /* Retrieve all Markdown and MDX files in your blog directory. */
  loader: glob({ pattern: "**/*.(md|mdx)", base: "./src/data/blog" }),
  schema: /* ... */
});
const authors = defineCollection({
  /* Retrieve all JSON files in your authors directory while retaining
   * uppercase letters in the ID. */
  loader: glob({
    pattern: '**/*.json',
    base: "./src/data/authors",
    generateId: ({ entry }) => entry.replace(/\.json$/, ''),
  }),
  schema: /* ... */
});
```

#### `pattern`

[Section titled “pattern”](#pattern)

**Type:** `string | string[]`

The `pattern` property accepts a string or an array of strings using glob matching (e.g. wildcards, globstars). The patterns must be relative to the base directory of entry files to match.

You can learn more about the syntax to use in the [micromatch documentation](https://github.com/micromatch/micromatch#matching-features). You can also verify the validity of your pattern using an online tool like the [DigitalOcean Glob Tool](https://www.digitalocean.com/community/tools/glob).

#### `base`

[Section titled “base”](#base)

**Type:** `string | URL`\
**Default:** `"."`

A relative path or [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL) to the directory from which to resolve the `pattern`.

#### `generateId()`

[Section titled “generateId()”](#generateid)

**Type:** `(options: GenerateIdOptions) => string`

A callback function that returns a unique string per entry in a collection. It accepts an object as parameter with the following properties:

* `entry` - the path to the entry file, relative to the base directory
* `base` - the base directory [URL](https://developer.mozilla.org/en-US/docs/Web/API/URL)
* `data` - the parsed, unvalidated data of the entry

By default it uses [`github-slugger`](https://github.com/Flet/github-slugger) to generate a slug with [kebab-cased](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case) words.

### `file()` loader

[Section titled “file() loader”](#file-loader)

**Type:** `(fileName: string, options?: FileOptions) => Loader`

**Added in:** `astro@5.0.0`

The `file()` loader creates entries from a single file that contains an array of objects with a unique `id` field, or an object with IDs as keys and entries as values. It supports JSON, YAML, or TOML files and you can provide a custom `parser` for data files it cannot parse by default.

This loader accepts a `fileName` property and an optional object as second argument:

src/content.config.ts

```ts
import { defineCollection } from 'astro:content';
import { file } from 'astro/loaders';


const authors = defineCollection({
  /* Retrieve all entries from a JSON file. */
  loader: file("src/data/authors.json"),
  schema: /* ... */
});
const products = defineCollection({
  /* Retrieve all entries from a CSV file using a custom parser. */
  loader: file("src/data/products.csv", {
    parser: (fileContent) => { /* your parser logic */ },
  }),
  schema: /* ... */
});
```

#### `fileName`

[Section titled “fileName”](#filename)

**Type:** `string`

Sets the path to the file to load, relative to the root directory.

#### Options

[Section titled “Options”](#options)

**Type:** `FileOptions`

An optional object with the following properties:

##### `parser()`

[Section titled “parser()”](#parser)

**Type:** `(text: string) => Record<string, Record<string, unknown>> | Array<Record<string, unknown>>`

A callback function to create a collection from a file’s contents. Use it when you need to process file not supported by default (e.g. `.csv`) or when using [nested `.json` documents](/en/guides/content-collections/#nested-json-documents).

## Loader types

[Section titled “Loader types”](#loader-types)

Loaders can be defined either as a simple function that returns an array of entries or with the more powerful object Content Loader API for more control over the loading process.

### Inline loaders

[Section titled “Inline loaders”](#inline-loaders)

An inline loader is an async function that returns an array or object containing entries. Use this for simple loaders, particularly those that are defined inline in the `src/content.config.ts` file.

The function can be async and must return either an array of entries that each contain a unique `id` field, or an object where each key is a unique ID and each value is the entry. Whenever the loader is invoked, it will clear the store and reload all the entries.

src/content.config.ts

```ts
const countries = defineCollection({
  loader: async () => {
    const response = await fetch("https://restcountries.com/v3.1/all");
    const data = await response.json();
    // Must return an array of entries with an id property
    // or an object with IDs as keys and entries as values
    return data.map((country) => ({
      id: country.cca3,
      ...country,
    }));
  },
  schema: /* ... */
});
```

### Object loaders

[Section titled “Object loaders”](#object-loaders)

A loader is an object with a `load()` method that is called at build time to fetch data and update the data store. It allows entries to be updated incrementally, or for the store to be cleared only when necessary. It can also define a schema for the entries, which can be used to validate the data and generate static types.

The recommended pattern is to define a function that accepts configuration options and returns the loader object, in the same way that you would normally define an Astro integration or Vite plugin.

loader.ts

```ts
import type { Loader, LoaderContext } from 'astro/loaders';
import { z } from 'astro:content';
import { loadFeedData } from "./feed.js";


// Define any options that the loader needs
export function myLoader(options: { url: string, apiKey: string }): Loader {
  // Configure the loader
  const feedUrl = new URL(options.url);
  // Return a loader object
  return {
    name: "my-loader",
    // Called when updating the collection.
    load: async (context: LoaderContext): Promise<void> => {
      // Load data and update the store
      const response = await loadFeedData(feedUrl, options.apiKey);
    },
    // Optionally, define the schema of an entry.
    // It will be overridden by user-defined schema.
    schema: async () => z.object({
      // ...
    })
  };
}
```

These configuration options can then be set when defining a collection:

src/content.config.ts

```ts
import { defineCollection, z } from 'astro:content';
import myLoader from '../../loader.ts';


const blog = defineCollection({
  loader: myLoader({
    url: "https://api.example.com/posts",
    apiKey: "my-secret",
  }),
  schema: /* ... */
});
```

## Object loader API

[Section titled “Object loader API”](#object-loader-api)

The API for [inline loaders](#inline-loaders) is very simple, and is shown above. This section shows the API for defining an object loader.

### The `Loader` object

[Section titled “The Loader object”](#the-loader-object)

The loader object has the following properties:

#### `name`

[Section titled “name”](#name)

**Type**: `string`

A unique name for the loader, used in logs and [for conditional loading](/en/reference/integrations-reference/#refreshcontent-option).

#### `load`

[Section titled “load”](#load)

**Type**: `(context: LoaderContext) => Promise<void>`

An async function that is called at build time to load data and update the store. See [`LoaderContext`](#loadercontext) for more information.

#### `schema`

[Section titled “schema”](#schema)

**Type**: `ZodSchema | Promise<ZodSchema> | (() => ZodSchema | Promise<ZodSchema>)`

An optional [Zod schema](/en/guides/content-collections/#defining-datatypes-with-zod) that defines the shape of the entries. It is used to both validate the data and also to generate TypeScript types for the collection.

If a function is provided, it will be called at build time before `load()` to generate the schema. You can use this to dynamically generate the schema based on the configuration options or by introspecting an API.

### `LoaderContext`

[Section titled “LoaderContext”](#loadercontext)

This object is passed to the `load()` method of the loader, and contains the following properties:

#### `collection`

[Section titled “collection”](#collection)

**Type**: `string`

The unique name of the collection. This is the key in the `collections` object in the `src/content.config.ts` file.

#### `store`

[Section titled “store”](#store)

**Type**: [`DataStore`](#datastore)

A database to store the actual data. Use this to update the store with new entries. See [`DataStore`](#datastore) for more information.

#### `meta`

[Section titled “meta”](#meta)

**Type**: `MetaStore`

A key-value store scoped to the collection, designed for things like sync tokens and last-modified times. This metadata is persisted between builds alongside the collection data but is only available inside the loader.

```ts
const lastModified = meta.get("lastModified");
// ...
meta.set("lastModified", new Date().toISOString());
```

#### `logger`

[Section titled “logger”](#logger)

**Type**: [`AstroIntegrationLogger`](/en/reference/integrations-reference/#astrointegrationlogger)

A logger that can be used to log messages to the console. Use this instead of `console.log` for more helpful logs that include the loader name in the log message. See [`AstroIntegrationLogger`](/en/reference/integrations-reference/#astrointegrationlogger) for more information.

#### `config`

[Section titled “config”](#config)

**Type**: `AstroConfig`

The full, resolved Astro configuration object with all defaults applied. See [the configuration reference](/en/reference/configuration-reference/) for more information.

#### `parseData`

[Section titled “parseData”](#parsedata)

**Type**: `(props: ParseDataOptions<TData>) => Promise<TData>`

Validates and parses the data according to the collection schema. Pass data to this function to validate and parse it before storing it in the data store.

loader.ts

```ts
import type { Loader } from "astro/loaders";
import { loadFeed } from "./feed.js";


export function feedLoader({ url }): Loader {
  const feedUrl = new URL(url);
  return {
    name: "feed-loader",
    load: async ({ store, logger, parseData, meta, generateDigest }) => {
      logger.info("Loading posts");
      const feed = loadFeed(feedUrl);
      store.clear();


      for (const item of feed.items) {
        const data = await parseData({
          id: item.guid,
          data: item,
        });
        store.set({
          id,
          data,
        });
      }
    },
  };
}
```

#### `renderMarkdown`

[Section titled “renderMarkdown”](#rendermarkdown)

**Type**: `(markdown: string) => Promise<RenderedContent>`

**Added in:** `astro@5.9.0`

Renders a Markdown string to HTML, returning a `RenderedContent` object.

This allows you to render Markdown content directly within your loaders using the same Markdown processing as Astro’s built-in `glob` loader and provides access to the `render()` function and `<Content />` component for [rendering body content](/en/guides/content-collections/#rendering-body-content).

Assign this object to the [rendered](#rendered) field of the [DataEntry](#dataentry) object to allow users to [render the content in a page](/en/guides/content-collections/#rendering-body-content).

loader.ts

```ts
import type { Loader } from 'astro/loaders';
import { loadFromCMS } from './cms.js';


export function myLoader(settings): Loader {
  return {
    name: 'cms-loader',
    async load({ renderMarkdown, store }) {
      const entries = await loadFromCMS();


      store.clear();


      for (const entry of entries) {
        store.set({
          id: entry.id,
          data: entry,
          // Assume each entry has a 'content' field with markdown content
          rendered: await renderMarkdown(entry.content),
        });
      }
    },
  };
}
```

#### `generateDigest`

[Section titled “generateDigest”](#generatedigest)

**Type**: `(data: Record<string, unknown> | string) => string`

Generates a non-cryptographic content digest of an object or string. This can be used to track if the data has changed by setting [the `digest` field](#digest) of an entry.

loader.ts

```ts
import type { Loader } from "astro/loaders";
import { loadFeed } from "./feed.js";


export function feedLoader({ url }): Loader {
  const feedUrl = new URL(url);
  return {
    name: "feed-loader",
    load: async ({ store, logger, parseData, meta, generateDigest }) => {
      logger.info("Loading posts");
      const feed = loadFeed(feedUrl);
      store.clear();


      for (const item of feed.items) {
        const data = await parseData({
          id: item.guid,
          data: item,
        });


        const digest = generateDigest(data);


        store.set({
          id,
          data,
          digest,
        });
      }
    },
  };
}
```

#### `watcher`

[Section titled “watcher”](#watcher)

**Type**: `FSWatcher`

When running in dev mode, this is a filesystem watcher that can be used to trigger updates. See [`ViteDevServer`](https://vite.dev/guide/api-javascript.html#vitedevserver) for more information.

Extract from the file() loader

```ts
return {
  name: 'file-loader',
  load: async ({ config, store, watcher }) => {
    const url = new URL(fileName, config.root);
    const filePath = fileURLToPath(url);
    await syncData(filePath, store);


    watcher?.on('change', async (changedPath) => {
      if (changedPath === filePath) {
        logger.info(`Reloading data from ${fileName}`);
        await syncData(filePath, store);
      }
    });
  },
};
```

#### `refreshContextData`

[Section titled “refreshContextData”](#refreshcontextdata)

**Type**: `Record<string, unknown>`

If the loader has been triggered by an integration, this may optionally contain extra data set by that integration. It is only set when the loader is triggered by an integration. See the [`astro:server:setup`](/en/reference/integrations-reference/#refreshcontent-option) hook reference for more information.

loader.ts

```ts
export function myLoader(options: { url: string }): Loader {
  return {
    name: "my-loader",
    load: async ({ refreshContextData, store, logger }) => {
      if(refreshContextData?.webhookBody) {
        logger.info("Webhook triggered with body");
        processWebhook(store, refreshContextData.webhookBody);
      }
      // ...
    },
  };
}
```

### `DataStore`

[Section titled “DataStore”](#datastore)

The data store is a loader’s interface to the content collection data. It is a key-value (KV) store, scoped to the collection, and therefore a loader can only access the data for its own collection.

#### `get`

[Section titled “get”](#get)

**Type**: `(key: string) => DataEntry | undefined`

Get an entry from the store by its ID. Returns `undefined` if the entry does not exist.

```ts
const existingEntry = store.get("my-entry");
```

The returned object is a [`DataEntry`](#dataentry) object.

#### `set`

[Section titled “set”](#set)

**Type**: `(entry: DataEntry) => boolean`

Used after data has been [validated and parsed](#parsedata) to add an entry to the store, returning `true` if the entry was set. This returns `false` when the [`digest`](#digest) property determines that an entry has not changed and should not be updated.

loader.ts

```ts
    for (const item of feed.items) {
      const data = await parseData({
        id: item.guid,
        data: item,
      });
      const digest = generateDigest(data);
      store.set({
        id,
        data,
        rendered: {
          html: data.description ?? "",
        },
        digest,
      });
    }
```

#### `entries`

[Section titled “entries”](#entries)

**Type**: `() => Array<[id: string, DataEntry]>`

Get all entries in the collection as an array of key-value pairs.

#### `keys`

[Section titled “keys”](#keys)

**Type**: `() => Array<string>`

Get all the keys of the entries in the collection.

#### `values`

[Section titled “values”](#values)

**Type**: `() => Array<DataEntry>`

Get all entries in the collection as an array.

#### `delete`

[Section titled “delete”](#delete)

**Type**: `(key: string) => void`

Delete an entry from the store by its ID.

#### `clear`

[Section titled “clear”](#clear)

**Type**: `() => void`

Clear all entries from the collection.

#### `has`

[Section titled “has”](#has)

**Type**: `(key: string) => boolean`

Check if an entry exists in the store by its ID.

### `DataEntry`

[Section titled “DataEntry”](#dataentry)

This is the type of the object that is stored in the data store. It has the following properties:

#### `id`

[Section titled “id”](#id)

**Type**: `string`

An identifier for the entry, which must be unique within the collection. This is used to look up the entry in the store and is the key used with `getEntry` for that collection.

#### `data`

[Section titled “data”](#data)

**Type**: `Record<string, unknown>`

The actual data for the entry. When a user accesses the collection, this will have TypeScript types generated according to the collection schema.

It is the loader’s responsibility to use [`parseData`](#parsedata) to validate and parse the data before storing it in the data store: no validation is done when getting or setting the data.

#### `filePath`

[Section titled “filePath”](#filepath)

**Type**: `string | undefined`

A path to the file that is the source of this entry, relative to the root of the site. This only applies to file-based loaders and is used to resolve paths such as images or other assets.

If not set, then any fields in the schema that use [the `image()` helper](/en/guides/images/#images-in-content-collections) will be treated as [public paths](/en/guides/images/#where-to-store-images) and not transformed.

#### `body`

[Section titled “body”](#body)

**Type**: `string | undefined`

The raw body of the entry, if applicable. If the entry includes [rendered content](#rendered), then this field can be used to store the raw source. This is optional and is not used internally.

#### `digest`

[Section titled “digest”](#digest)

**Type**: `string | undefined`

An optional content digest for the entry. This can be used to check if the data has changed.

When [setting an entry](#set), the entry will only update if the digest does not match an existing entry with the same ID.

The format of the digest is up to the loader, but it must be a string that changes when the data changes. This can be done with the [`generateDigest`](#generatedigest) function.

#### `rendered`

[Section titled “rendered”](#rendered)

**Type**: `RenderedContent | undefined`

Stores an object with an entry’s rendered content and metadata if it has been rendered to HTML. For example, this can be used to store the rendered content of a Markdown entry, or HTML from a CMS.

If this field is provided, then [the `render()` function and `<Content />` component](/en/guides/content-collections/#rendering-body-content) are available to render the entry in a page.

The format of the `RenderedContent` object is:

```ts
{
  /** Rendered HTML string. If present then `render(entry)` will return a component that renders this HTML. */
  html: string;
  metadata?: {
    /** Any images that are present in this entry. Relative to the DataEntry filePath. */
    imagePaths?: Array<string>;
    /** Any headings that are present in this file. Returned as `headings` from `render()` */
    headings?: MarkdownHeading[];
    /** Raw frontmatter, parsed from the file. This may include data from remark plugins. */
    frontmatter?: Record<string, any>;
    /** Any other metadata that is present in this file. */
    [key: string]: unknown;
  };
}
```

If the entry has Markdown content then you can use the [`renderMarkdown()`](#rendermarkdown) function to generate this object from the Markdown string.

# Dev Toolbar App API

The Astro Dev Toolbar App API allows you to create [Astro Integrations](/en/reference/integrations-reference/) that add apps to the Astro Dev Toolbar. This allows you to add new features and integrations with third-party services.

![](/houston_chef.webp) **Related recipe:** [Create a dev toolbar app](/en/recipes/making-toolbar-apps/)

## Toolbar app integration setup

[Section titled “Toolbar app integration setup”](#toolbar-app-integration-setup)

Integrations can add apps to the dev toolbar in [the `astro:config:setup` hook](/en/reference/integrations-reference/#astroconfigsetup).

my-integration.js

```ts
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "my-integration",
  hooks: {
    "astro:config:setup": ({ addDevToolbarApp }) => {
      addDevToolbarApp({
        id: "my-app",
        name: "My App",
        icon: "<svg>...</svg>",
        entrypoint: "./my-app.js",
      });
    },
  },
});
```

### `addDevToolbarApp()`

[Section titled “addDevToolbarApp()”](#adddevtoolbarapp)

**Type:** `(entrypoint: DevToolbarAppEntry) => void`

**Added in:** `astro@4.0.0`

A function available to [the `astro:config:setup` hook](/en/reference/integrations-reference/#astroconfigsetup) that adds dev toolbar apps. It takes an object with the following required properties to define the toolbar app: [`id`](#id), [`name`](#name), and [`entrypoint`](#entrypoint). Optionally, you can also define an [`icon`](#icon) for your app.

### `id`

[Section titled “id”](#id)

**Type:** `string`

A unique identifier for the app. This will be used to uniquely identify the app in hooks and events.

my-integration.js

```ts
{
  id: 'my-app',
  // ...
}
```

### `name`

[Section titled “name”](#name)

**Type:** `string`

The name of the app. This will be shown to users whenever the app needs to be referenced using a human-readable name.

my-integration.js

```ts
{
  // ...
  name: 'My App',
  // ...
}
```

### `icon`

[Section titled “icon”](#icon)

**Type:** `Icon | string`\
**Default**: `"?"`

The icon used to display the app in the toolbar. This can either be an icon from [the icon list](#icons), or a string containing the SVG markup of the icon.

my-integration.js

```ts
{
  // ...
  icon: '<svg>...</svg>', // or, e.g. 'astro:logo'
  // ...
}
```

### `entrypoint`

[Section titled “entrypoint”](#entrypoint)

**Type:** `string | URL`

The path to the file that exports the dev toolbar app.

my-integration.js

```ts
{
  // ...
  entrypoint: './my-app.js',
}
```

**Added in:** `astro@5.0.0`

The function also accepts a `URL` as `entrypoint`:

my-integration.js

```ts
/**
 * @type {() => import('astro').AstroIntegration}
 */
export default () => ({
  name: "my-integration",
  hooks: {
    "astro:config:setup": ({ addDevToolbarApp }) => {
      addDevToolbarApp({
        id: "my-app",
        name: "My App",
        icon: "<svg>...</svg>",
        entrypoint: new URL("./my-app.js", import.meta.url),
      });
    },
  },
});
```

## Structure of a Dev Toolbar App

[Section titled “Structure of a Dev Toolbar App”](#structure-of-a-dev-toolbar-app)

A Dev Toolbar App is a `.js` or `.ts` file that default exports an object using the [`defineToolbarApp()` function](#definetoolbarapp) available from the `astro/toolbar` module.

src/my-app.js

```ts
import { defineToolbarApp } from "astro/toolbar";


export default defineToolbarApp({
  init(canvas) {
    const text = document.createTextNode('Hello World!');
    canvas.appendChild(text);
  },
  beforeTogglingOff() {
    const confirmation = window.confirm('Really exit?');
    return confirmation;
  }
});
```

### `defineToolbarApp()`

[Section titled “defineToolbarApp()”](#definetoolbarapp)

**Type:** `(app: DevToolbarApp) => DevToolbarApp`

**Added in:** `astro@4.7.0`

A function that defines the logic of your toolbar app when it is loaded and toggled off.

This function takes an object with an [`init()`](#init) function that will be called when the dev toolbar app is loaded. It can also take a [`beforeTogglingOff()`](#beforetogglingoff) function that will run when the toolbar app is clicked to toggle off its active status.

### `init()`

[Section titled “init()”](#init)

**Type:** `(canvas: ShadowRoot, app: ToolbarAppEventTarget, server: ToolbarServerHelpers) => void | Promise<void>`

Although not required, most apps will use this function to define the core behavior of the app. This function will be called only once when the app is loaded, which will either be when the browser is idle or when the user clicks on the app in the UI, depending on which one comes first.

The function receives three arguments to define your app logic: [`canvas`](#canvas) (to render elements to the screen), [`app`](#app) (to send and receive client-side events from the dev toolbar), and [`server`](#server) (to communicate with the server).

#### `canvas`

[Section titled “canvas”](#canvas)

**Type:** `ShadowRoot`

A standard [ShadowRoot](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot) that the app can use to render its UI. Elements can be created and added to the ShadowRoot using the standard DOM APIs.

Every app receives its own dedicated ShadowRoot for rendering its UI. Additionally, the parent element is positioned using `position: absolute;` so the app UI will not affect the layout of an Astro page.

src/my-app.js

```ts
export default defineToolbarApp({
  init(canvas) {
    canvas.appendChild(document.createTextNode('Hello World!'))
  }
});
```

#### `app`

[Section titled “app”](#app)

**Type:** `ToolbarAppEventTarget`

**Added in:** `astro@4.7.0`

A standard [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget) with a few additional [helpers for client-side events](#client-side-events) that can be used to send and receive events from the Dev toolbar.

src/my-app.js

```ts
export default defineToolbarApp({
  init(canvas, app) {
    app.onToggled(({ state }) => {
      const text = document.createTextNode(
        `The app is now ${state ? "enabled" : "disabled"}!`,
      );
      canvas.appendChild(text);
    });
  },
});
```

#### `server`

[Section titled “server”](#server)

**Type:** `ToolbarServerHelpers`

**Added in:** `astro@4.7.0`

An object that can be used to [communicate with the server](#client-server-communication).

src/my-app.js

```ts
export default defineToolbarApp({
  init(canvas, app, server) {
    server.send('my-message', { message: 'Hello!' });


    server.on('server-message', (data) => {
      console.log(data.message);
    });
  },
});
```

### `beforeTogglingOff()`

[Section titled “beforeTogglingOff()”](#beforetogglingoff)

**Type:** `(canvas: ShadowRoot) => boolean | Promise<boolean>`

**Added in:** `astro@4.7.0`

This optional function will be called when the user clicks on the app icon in the UI to toggle off the app. This function can be used, for example, to perform cleanup operations, or to ask the user for confirmation before toggling off the app.

If a falsy value is returned, the toggling off will be cancelled and the app will stay enabled.

src/my-app.js

```ts
export default defineToolbarApp({
  // ...
  beforeTogglingOff() {
    const confirmation = window.confirm('Are you sure you want to disable this app?');
    return confirmation;
  }
});
```

#### canvas

[Section titled “canvas”](#canvas-1)

**Type:** `ShadowRoot`

The ShadowRoot of the app, can be used to render any UI needed before closing. Same as the [`canvas` argument of the `init` function](#canvas).

## Client-side Events

[Section titled “Client-side Events”](#client-side-events)

In addition to the standard methods of an `EventTarget` ([`addEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget), [`dispatchEvent`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/dispatchEvent), [`removeEventListener`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener)etc.), the [`app`](#app) object also has the following methods:

### `onToggled()`

[Section titled “onToggled()”](#ontoggled)

**Type:** `(callback: (options: {state: boolean})) => void`

**Added in:** `astro@4.7.0`

Registers a callback to be called when the user clicks on the app icon in the UI to toggle the app on or off.

src/my-app.js

```ts
app.onToggled((options) => {
  console.log(`The app is now ${options.state ? 'enabled' : 'disabled'}!`);
});
```

### `onToolbarPlacementUpdated()`

[Section titled “onToolbarPlacementUpdated()”](#ontoolbarplacementupdated)

**Type:** `(callback: (options: {placement: 'bottom-left' | 'bottom-center' | 'bottom-right'})) => void`

**Added in:** `astro@4.7.0`

This event is fired when the user changes the placement of the Dev Toolbar. This can, for example, be used to reposition the app’s UI when the toolbar is moved.

src/my-app.js

```ts
app.onToolbarPlacementUpdated((options) => {
  console.log(`The toolbar is now placed at ${options.placement}!`);
});
```

### `toggleState()`

[Section titled “toggleState()”](#togglestate)

**Type:** `(options: {state: boolean}) => void`

**Added in:** `astro@4.7.0`

Changes the state of the app. This can be used to enable or disable the app programmatically, for example, when the user clicks on a button in the app’s UI.

src/my-app.js

```ts
app.toggleState({ state: false });
```

### `toggleNotification()`

[Section titled “toggleNotification()”](#togglenotification)

**Type:** `(options: {state?: boolean, level?: 'error' | 'warning' | 'info'}) => void`

**Added in:** `astro@4.7.0`

Toggles a notification on the app icon. This can be used to inform the user that the app requires attention, or remove the current notification.

src/my-app.js

```ts
app.toggleNotification({
  state: true,
  level: 'warning',
});
```

#### `state`

[Section titled “state”](#state)

**Type:** `boolean`

Indicates whether or not the app has a notification for the user. When `true`, the app icon will be highlighted. Conversely, when `false`, the highlight will be removed. If this property is not specified, `true` will be assumed.

#### `level`

[Section titled “level”](#level)

**Type:** `'error' | 'warning' | 'info'`\
**Default:** `'error'`

Indicates the level of the notification. This will be used to determine the color and shape (dark pink circle, gold triangle, or blue square) of the highlight on the app icon. If this property is not specified, `'error'` will be assumed.

## Client-Server Communication

[Section titled “Client-Server Communication”](#client-server-communication)

Using [Vite’s methods for client-server communication](https://vite.dev/guide/api-plugin.html#client-server-communication), Dev Toolbar Apps and the server can communicate with each other. In order to facilitate sending and receiving custom messages, helper methods are provided for use both in your toolbar app (on the client) and in your integration (on the server).

### On the client

[Section titled “On the client”](#on-the-client)

In your app, use the [`server` object on the `init()` hook](#server) to send and receive messages to and from the server.

src/my-app.js

```ts
export default defineToolbarApp({
  init(canvas, app, server) {
    server.send('my-message', { message: 'Hello!' });


    server.on('server-message', (data) => {
      console.log(data.message);
    });
  },
});
```

#### `send()`

[Section titled “send()”](#send)

**Type:** `<T>(event: string, payload: T) => void`

**Added in:** `astro@4.7.0`

Sends data to the server from logic defined in your toolbar app.

src/my-app.js

```ts
init(canvas, app, server) {
  server.send('my-app:my-message', { message: 'Hello!' });
}
```

When sending messages from the client to the server, it is good practice to prefix the event name with the app ID or other namespaces to avoid conflicts with other apps or other integrations that may be listening for messages.

#### `on()`

[Section titled “on()”](#on)

**Type:** `<T>(event: string, callback: (data: T) => void) => void`

**Added in:** `astro@4.7.0`

Registers a callback to be called when the server sends a message with the specified event.

src/my-app.js

```ts
init(canvas, app, server) {
  server.on('server-message', (data) => {
    console.log(data.message);
  });
}
```

### On the server

[Section titled “On the server”](#on-the-server)

In an integration, such as [the integration that adds your toolbar app](#toolbar-app-integration-setup), use the [`astro:server:setup` hook](/en/reference/integrations-reference/#astroserversetup) to access the `toolbar` object to send and receive messages to and from your apps.

my-integration.js

```ts
export default () => ({
  name: "my-integration",
  hooks: {
    "astro:config:setup": ({ addDevToolbarApp }) => {},
    "astro:server:setup": ({ toolbar }) => {},
  },
});
```

#### `send()`

[Section titled “send()”](#send-1)

**Type:** `<T>(event: string, payload: T) => void`

**Added in:** `astro@4.7.0`

Sends data to the client.

my-integration.js

```ts
'astro:server:setup': ({ toolbar }) => {
  toolbar.send('server-message', { message: 'Hello!' });
},
```

#### `on()`

[Section titled “on()”](#on-1)

**Type:** `<T>(event: string, callback: (data: T) => void) => void`

**Added in:** `astro@4.7.0`

Registers a callback to be called when the client sends a message with the specified event.

my-integration.js

```ts
'astro:server:setup': ({ toolbar }) => {
  toolbar.on('my-app:my-message', (data) => {
    console.log(data.message);
  });
},
```

#### `onAppInitialized()`

[Section titled “onAppInitialized()”](#onappinitialized)

**Type:** `(appId: string, callback: () => void) => void`

**Added in:** `astro@4.7.0`

Registers a callback to be called when the app is initialized.

my-integration.js

```ts
'astro:server:setup': ({ toolbar }) => {
  toolbar.onAppInitialized('my-app', () => {
    console.log('The app is now initialized!');
  });
},
```

Note

The built-in `connection` event from Vite fires **before** Dev Toolbar apps are initialized and therefore cannot be used directly by apps. Use the `onAppInitialized` method to ensure that the app is fully initialized before sending messages to it.

#### `onAppToggled()`

[Section titled “onAppToggled()”](#onapptoggled)

**Type:** `(appId: string, callback: (options: {state: boolean}) => void) => void`

**Added in:** `astro@4.7.0`

Registers a callback to be called when the user clicks on the app icon in the UI to toggle the app on or off.

my-integration.js

```ts
'astro:server:setup': ({ toolbar }) => {
  toolbar.onAppToggled('my-app', ({ state }) => {
    console.log(`The app is now ${state ? 'enabled' : 'disabled'}!`);
  });
},
```

## Component Library

[Section titled “Component Library”](#component-library)

The Dev Toolbar includes a set of web components that can be used to build apps with a consistent look and feel.

### `astro-dev-toolbar-window`

[Section titled “astro-dev-toolbar-window”](#astro-dev-toolbar-window)

Shows a window.

The slot of the component will be used as the content of the window.

```html
<astro-dev-toolbar-window>
  <p>My content</p>
</astro-dev-toolbar-window>
```

When building a window using JavaScript, slotted content must go inside the light DOM of the component.

```js
const myWindow = document.createElement('astro-dev-toolbar-window');
const myContent = document.createElement('p');
myContent.textContent = 'My content';


// use appendChild directly on `window`, not `myWindow.shadowRoot`
myWindow.appendChild(myContent);
```

### `astro-dev-toolbar-button`

[Section titled “astro-dev-toolbar-button”](#astro-dev-toolbar-button)

Shows a button.

The slot of the component will be used as the content of the button.

```js
const myButton = document.createElement('astro-dev-toolbar-button');
myButton.textContent = 'Click me!';
myButton.buttonStyle = "purple";
myButton.size = "medium";


myButton.addEventListener('click', () => {
  console.log('Clicked!');
});
```

#### `size`

[Section titled “size”](#size)

**Type:** `"small" | "medium" | "large"`\
**Default:** `"small"`

The size of the button.

#### `button-style`

[Section titled “button-style”](#button-style)

**Type:** `"ghost" | "outline" | "purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"purple"`

The style of the button. When using `ghost`, the button itself is invisible and only the content of the button will be shown.

In JavaScript, set this property using the `buttonStyle` property to avoid conflict with the native `style` property.

#### `button-border-radius`

[Section titled “button-border-radius”](#button-border-radius)

**Type:** `"normal" | "rounded"`\
**Default:** `"normal"`

**Added in:** `astro@4.8.0`

The border radius of the button. When using `rounded`, the button will have rounded corners and uniform padding on all sides.

In JavaScript, set this property using the `buttonBorderRadius` property.

### `astro-dev-toolbar-badge`

[Section titled “astro-dev-toolbar-badge”](#astro-dev-toolbar-badge)

Shows a badge.

The slot of the component will be used as the content of the badge.

```html
<astro-dev-toolbar-badge>My badge</astro-dev-toolbar-badge>
```

#### `size`

[Section titled “size”](#size-1)

**Type:** `"small" | "large"`\
**Default:** `"small"`

The size of the badge.

#### `badge-style`

[Section titled “badge-style”](#badge-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"purple"`

The style (color) of the badge.

In JavaScript, set this property using the `badgeStyle` property to avoid conflict with the native `style` property.

### `astro-dev-toolbar-card`

[Section titled “astro-dev-toolbar-card”](#astro-dev-toolbar-card)

Shows a card. Specify an optional `link` attribute to make the card act like an `<a>` element.

When making a card using JavaScript, a `clickAction` property can be specified to make the card act like a `<button>` element.

The slot of the component will be used as the content of the card.

```html
<astro-dev-toolbar-card icon="astro:logo" link="https://github.com/withastro/astro/issues/new/choose">Report an issue</astro-dev-toolbar-card>
```

#### `card-style`

[Section titled “card-style”](#card-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"purple"`

The style of the card. The color is only applied to the border of the card on hover.

In JavaScript, set this property using the `cardStyle`.

### `astro-dev-toolbar-toggle`

[Section titled “astro-dev-toolbar-toggle”](#astro-dev-toolbar-toggle)

Shows a toggle element, acting as a checkbox. This element internally is a simple wrapper around a native `<input type="checkbox">` element. The checkbox element can be accessed using the `input` property.

```ts
const toggle = document.createElement('astro-dev-toolbar-toggle');


toggle.input.addEventListener('change', (evt) => {
  console.log(`The toggle is now ${evt.currentTarget.checked ? 'enabled' : 'disabled'}!`);
});
```

#### `toggle-style`

[Section titled “toggle-style”](#toggle-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"gray"`

The style of the toggle.

In JavaScript, set this property using the `toggleStyle` property.

### `astro-dev-toolbar-radio-checkbox`

[Section titled “astro-dev-toolbar-radio-checkbox”](#astro-dev-toolbar-radio-checkbox)

**Added in:** `astro@4.8.0`

Shows a radio checkbox. Similar to the `astro-dev-toolbar-toggle` component, this element is a simple wrapper around a native `<input type="radio">` element. The radio element can be accessed using the `input` property.

```ts
const radio = document.createElement('astro-dev-toolbar-radio-checkbox');


radio.input.addEventListener('change', (evt) => {
  console.log(`The radio is now ${evt.currentTarget.checked ? 'enabled' : 'disabled'}!`);
});
```

#### `radio-style`

[Section titled “radio-style”](#radio-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"purple"`

The style of the radio.

In JavaScript, set this property using the `radioStyle` property.

### `astro-dev-toolbar-highlight`

[Section titled “astro-dev-toolbar-highlight”](#astro-dev-toolbar-highlight)

Can be used to highlight an element on the page. In most cases, you’ll want to position and resize this element using the `top`, `left`, `width` and `height` CSS properties to match the element you want to highlight.

```html
<!-- Highlight the entire page -->
<astro-dev-toolbar-highlight style="top: 0; left: 0; width: 100%; height: 100%;"></astro-dev-toolbar-highlight>
```

```ts
const elementToHighlight = document.querySelector('h1');
const rect = elementToHighlight.getBoundingClientRect();


const highlight = document.createElement('astro-dev-toolbar-highlight');


highlight.style.top = `${Math.max(rect.top + window.scrollY - 10, 0)}px`;
highlight.style.left = `${Math.max(rect.left + window.scrollX - 10, 0)}px`;
highlight.style.width = `${rect.width + 15}px`;
highlight.style.height = `${rect.height + 15}px`;
highlight.icon = 'astro:logo';
```

#### `highlight-style`

[Section titled “highlight-style”](#highlight-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"purple"`

The style of the highlight.

#### `icon`

[Section titled “icon”](#icon-1)

An [icon](#icons) to show in the top right corner of the highlight.

### `astro-dev-toolbar-tooltip`

[Section titled “astro-dev-toolbar-tooltip”](#astro-dev-toolbar-tooltip)

Shows a tooltip with different sections. This component is set to `display: none;` by default and can be made visible using a `data-show="true"` attribute.

Sections are defined using the `sections` property. This property is an array of objects with the following shape:

```ts
{
  title?: string; // Title of the section
  inlineTitle?: string; // Title of the section, shown inline next to the title
  icon?: Icon; // Icon of the section
  content?: string; // Content of the section
  clickAction?: () => void | Promise<void>; // Action to perform when clicking on the section
  clickDescription?: string; // Description of the action to perform when clicking on the section
}
```

```ts
const tooltip = document.createElement('astro-dev-toolbar-tooltip');


tooltip.sections = [{
  title: 'My section',
  icon: 'astro:logo',
  content: 'My content',
  clickAction: () => {
    console.log('Clicked!')
  },
  clickDescription: 'Click me!'
}]
```

This component is often combined with the `astro-dev-toolbar-highlight` component to show a tooltip when hovering a highlighted element:

```ts
const highlight = document.createElement('astro-dev-toolbar-highlight');


// Position the highlight...


const tooltip = document.createElement('astro-dev-toolbar-tooltip');


// Add sections to the tooltip...


highlight.addEventListener('mouseover', () => {
  tooltip.dataset.show = 'true';
});


highlight.addEventListener('mouseout', () => {
  tooltip.dataset.show = 'false';
});
```

### `astro-dev-toolbar-icon`

[Section titled “astro-dev-toolbar-icon”](#astro-dev-toolbar-icon)

Shows an icon. An icon from [the icon list](#icons) can be specified using the `icon` attribute, or the SVG markup of an icon can be passed as a slot.

```html
<astro-dev-toolbar-icon icon="astro:logo" />
```

```html
<astro-dev-toolbar-icon>
  <svg>...</svg>
</astro-dev-toolbar-icon>
```

### `astro-dev-toolbar-select`

[Section titled “astro-dev-toolbar-select”](#astro-dev-toolbar-select)

**Added in:** `astro@4.6.0`

Shows a select element. Similar to the `astro-dev-toolbar-toggle` component, this element is a simple wrapper around a native `<select>` element. Use the `element` property to have access to the select element.

```ts
const mySelect = document.createElement("astro-dev-toolbar-select");
const options = [
  { label: "First option", value: "first" },
  { label: "Second option", value: "second", isDefault: true },
];
const myOptions = options.map((option) => {
  const optionEl = document.createElement("option");
  optionEl.textContent = option.label;
  optionEl.setAttribute("value", option.value);
  optionEl.selected = option.isDefault || false;
  return optionEl;
});


mySelect.selectStyle = "green";
mySelect.append(...myOptions);


mySelect.element.addEventListener("change", (evt) => {
  if (evt.currentTarget instanceof HTMLSelectElement) {
    console.log(`The select value is now ${evt.currentTarget.value}!`);
  }
});
```

#### `select-style`

[Section titled “select-style”](#select-style)

**Type:** `"purple" | "gray" | "red" | "green" | "yellow" | "blue"`\
**Default:** `"gray"`

The style of the select.

In JavaScript, set this property using the `selectStyle` property.

#### Icons

[Section titled “Icons”](#icons)

Currently, the following icons are available and can be used in any component that accepts an icon:

* `astro:logo`
* `warning`
* `arrow-down`
* `bug`
* `check-circle`
* `gear`
* `lightbulb`
* `file-search`
* `star`
* `checkmark`
* `dots-three`
* `copy`
* `compress`
* `grid`
* `puzzle`
* `approveUser`
* `checkCircle`
* `resizeImage`
* `searchFile`
* `image`
* `robot`
* `sitemap`
* `gauge`
* `person-arms-spread`
* `arrow-left`
* `houston-detective`

All of the above icons have `fill="currentColor"` set by default and will inherit their color from the parent element.

# Template directives reference

**Template directives** are a special kind of HTML attribute available inside of any Astro component template (`.astro` files), and some can also be used in `.mdx` files.

Template directives are used to control an element or component’s behavior in some way. A template directive could enable some compiler feature that makes your life easier (like using `class:list` instead of `class`). Or, a directive could tell the Astro compiler to do something special with that component (like hydrating with `client:load`).

This page describes all of the template directives available to you in Astro, and how they work.

## Rules

[Section titled “Rules”](#rules)

For a template directive to be valid, it must:

* Include a colon `:` in its name, using the form `X:Y` (ex: `client:load`).
* Be visible to the compiler (ex: `<X {...attr}>` would not work if `attr` contained a directive).

Some template directives, but not all, can take a custom value:

* `<X client:load />` (takes no value)
* `<X class:list={['some-css-class']} />` (takes an array)

A template directive is never included directly in the final HTML output of a component.

## Common Directives

[Section titled “Common Directives”](#common-directives)

### `class:list`

[Section titled “class:list”](#classlist)

`class:list={...}` takes an array of class values and converts them into a class string. This is powered by @lukeed’s popular [clsx](https://github.com/lukeed/clsx) helper library.

`class:list` takes an array of several different possible value kinds:

* `string`: Added to the element `class`
* `Object`: All truthy keys are added to the element `class`
* `Array`: flattened
* `false`, `null`, or `undefined`: skipped

```astro
<!-- This -->
<span class:list={[ 'hello goodbye', { world: true }, [ 'friend' ] ]} />
<!-- Becomes -->
<span class="hello goodbye world friend"></span>
```

### `set:html`

[Section titled “set:html”](#sethtml)

`set:html={string}` injects an HTML string into an element, similar to setting `el.innerHTML`.

**The value is not automatically escaped by Astro!** Be sure that you trust the value, or that you have escaped it manually before passing it to the template. Forgetting to do this will open you up to [Cross Site Scripting (XSS) attacks.](https://owasp.org/www-community/attacks/xss/)

```astro
---
const rawHTMLString = "Hello <strong>World</strong>"
---
<h1>{rawHTMLString}</h1>
  <!-- Output: <h1>Hello &lt;strong&gt;World&lt;/strong&gt;</h1> -->
<h1 set:html={rawHTMLString} />
  <!-- Output: <h1>Hello <strong>World</strong></h1> -->
```

You can also use `set:html` on a `<Fragment>` to avoid adding an unnecessary wrapper element. This can be especially useful when fetching HTML from a CMS.

```astro
---
const cmsContent = await fetchHTMLFromMyCMS();
---
<Fragment set:html={cmsContent}>
```

`set:html={Promise<string>}` injects an HTML string into an element that is wrapped in a Promise.

This can be used to inject HTML stored externally, such as in a database.

```astro
---
import api from '../db/api.js';
---
<article set:html={api.getArticle(Astro.props.id)}></article>
```

`set:html={Promise<Response>}` injects a [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) into an element.

This is most helpful when using `fetch()`. For example, fetching old posts from a previous static-site generator.

```astro
<article set:html={fetch('http://example/old-posts/making-soup.html')}></article>
```

`set:html` can be used on any tag and does not have to include HTML. For example, use with [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify) on a `<script>` tag to add a [JSON-LD](https://json-ld.org/) schema to your page.

```astro
<script type="application/ld+json" set:html={JSON.stringify({
  "@context": "https://schema.org/",
  "@type": "Person",
  name: "Houston",
  hasOccupation: {
    "@type": "Occupation",
    name: "Astronaut"
  }
})}/>
```

### `set:text`

[Section titled “set:text”](#settext)

`set:text={string}` injects a text string into an element, similar to setting `el.innerText`. Unlike `set:html`, the `string` value that is passed is automatically escaped by Astro.

This is equivalent to just passing a variable into a template expression directly (ex: `<div>{someText}</div>`) and therefore this directive is not commonly used.

## Client Directives

[Section titled “Client Directives”](#client-directives)

These directives control how [UI Framework components](/en/guides/framework-components/) are hydrated on the page.

By default, a UI Framework component is not hydrated in the client. If no `client:*` directive is provided, its HTML is rendered onto the page without JavaScript.

A client directive can only be used on a UI framework component that is directly imported into a `.astro` component. Hydration directives are not supported when using [dynamic tags](/en/reference/astro-syntax/#dynamic-tags) and [custom components passed via the `components` prop](/en/guides/integrations-guide/mdx/#passing-components-to-mdx-content).

### `client:load`

[Section titled “client:load”](#clientload)

* **Priority:** High
* **Useful for:** Immediately-visible UI elements that need to be interactive as soon as possible.

Load and hydrate the component JavaScript immediately on page load.

```astro
<BuyButton client:load />
```

### `client:idle`

[Section titled “client:idle”](#clientidle)

* **Priority:** Medium
* **Useful for:** Lower-priority UI elements that don’t need to be immediately interactive.

Load and hydrate the component JavaScript once the page is done with its initial load and the `requestIdleCallback` event has fired. If you are in a browser that doesn’t support [`requestIdleCallback`](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback), then the document [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event) event is used.

```astro
<ShowHideButton client:idle />
```

#### `timeout`

[Section titled “timeout”](#timeout)

**Added in:** `astro@4.15.0`

The maximum time to wait, in milliseconds, before hydrating the component, even if the page is not yet done with its initial load.

This allows you to pass a value for [the `timeout` option from the `requestIdleCallback()` specification](https://www.w3.org/TR/requestidlecallback/#the-requestidlecallback-method). This means you can delay hydration for lower-priority UI elements with more control to ensure your element is interactive within a specified time frame.

```astro
<ShowHideButton client:idle={{timeout: 500}} />
```

### `client:visible`

[Section titled “client:visible”](#clientvisible)

* **Priority:** Low
* **Useful for:** Low-priority UI elements that are either far down the page (“below the fold”) or so resource-intensive to load that you would prefer not to load them at all if the user never saw the element.

Load and hydrate the component JavaScript once the component has entered the user’s viewport. This uses an `IntersectionObserver` internally to keep track of visibility.

```astro
<HeavyImageCarousel client:visible />
```

#### `client:visible={{rootMargin}}`

[Section titled “client:visible={{rootMargin}}”](#clientvisiblerootmargin)

**Added in:** `astro@4.1.0`

Optionally, a value for `rootMargin` can be passed to the underlying `IntersectionObserver`. When `rootMargin` is specified, the component JavaScript will hydrate when a specified margin (in pixels) around the component enters the viewport, rather than the component itself.

```astro
<HeavyImageCarousel client:visible={{rootMargin: "200px"}} />
```

Specifying a `rootMargin` value can reduce layout shifts (CLS), allow more time for a component to hydrate on slower internet connections, and make components interactive sooner, enhancing the stability and responsiveness of the page.

### `client:media`

[Section titled “client:media”](#clientmedia)

* **Priority:** Low
* **Useful for:** Sidebar toggles, or other elements that might only be visible on certain screen sizes.

`client:media={string}` loads and hydrates the component JavaScript once a certain CSS media query is met.

Note

If the component is already hidden and shown by a media query in your CSS, then it can be easier to just use `client:visible` and not pass that same media query into the directive.

```astro
<SidebarToggle client:media="(max-width: 50em)" />
```

### `client:only`

[Section titled “client:only”](#clientonly)

`client:only={string}` **skips** HTML server rendering, and renders only on the client. It acts similarly to `client:load` in that it loads, renders, and hydrates the component immediately on page load.

**You must pass the component’s correct framework as a value!** Because Astro doesn’t run the component during your build / on the server, Astro doesn’t know what framework your component uses unless you tell it explicitly.

```astro
<SomeReactComponent client:only="react" />
<SomePreactComponent client:only="preact" />
<SomeSvelteComponent client:only="svelte" />
<SomeVueComponent client:only="vue" />
<SomeSolidComponent client:only="solid-js" />
```

#### Display loading content

[Section titled “Display loading content”](#display-loading-content)

For components that render only on the client, it is also possible to display fallback content while they are loading. Use `slot="fallback"` on any child element to create content that will be displayed only until your client component is available:

```astro
<ClientComponent client:only="vue">
  <div slot="fallback">Loading</div>
</ClientComponent>
```

### Custom Client Directives

[Section titled “Custom Client Directives”](#custom-client-directives)

Since Astro 2.6.0, integrations can also add custom `client:*` directives to change how and when components should be hydrated.

Visit the [`addClientDirective` API](/en/reference/integrations-reference/#addclientdirective-option) page to learn more about creating a custom client directive.

## Server Directives

[Section titled “Server Directives”](#server-directives)

These directives control how server island components are rendered.

### `server:defer`

[Section titled “server:defer”](#serverdefer)

The `server:defer` directive transforms the component into a server island, causing it to be rendered on demand, outside the scope of the rest of the page rendering.

See more about using [server island components](/en/guides/server-islands/).

```astro
<Avatar server:defer />
```

## Script & Style Directives

[Section titled “Script & Style Directives”](#script--style-directives)

These directives can only be used on HTML `<script>` and `<style>` tags, to control how your client-side JavaScript and CSS are handled on the page.

### `is:global`

[Section titled “is:global”](#isglobal)

By default, Astro automatically scopes `<style>` CSS rules to the component. You can opt-out of this behavior with the `is:global` directive.

`is:global` makes the contents of a `<style>` tag apply globally on the page when the component is included. This disables Astro’s CSS scoping system. This is equivalent to wrapping all of the selectors within a `<style>` tag with `:global()`.

You can combine `<style>` and `<style is:global>` together in the same component, to create some global style rules while still scoping most of your component CSS.

See the [Styling & CSS](/en/guides/styling/#global-styles) page for more details about how global styles work.

```astro
<style is:global>
  body a { color: red; }
</style>
```

### `is:inline`

[Section titled “is:inline”](#isinline)

By default, Astro will process, optimize, and bundle any `<script>` and `<style>` tags that it sees on the page. You can opt-out of this behavior with the `is:inline` directive.

`is:inline` tells Astro to leave the `<script>` or `<style>` tag as-is in the final output HTML. The contents will not be processed, optimized, or bundled. This limits some Astro features, like importing an npm package or using a compile-to-CSS language like Sass.

The `is:inline` directive means that `<style>` and `<script>` tags:

* Will not be bundled into an external file. This means that [attributes like `defer`](https://javascript.info/script-async-defer) which control the loading of an external file will have no effect.
* Will not be deduplicated—the element will appear as many times as it is rendered.
* Will not have its `import`/`@import`/`url()` references resolved relative to the `.astro` file.
* Will be rendered in the final output HTML exactly where it is authored.
* Styles will be global and not scoped to the component.

Caution

The `is:inline` directive is implied whenever any attribute other than `src` is used on a `<script>` or `<style>` tag. The one exception is using the [`define:vars` directive](/en/reference/directives-reference/#definevars) on the `<style>` tag, which does not automatically imply `is:inline`.

```astro
<style is:inline>
  /* inline: relative & npm package imports are not supported. */
  @import '/assets/some-public-styles.css';
  span { color: green; }
</style>


<script is:inline>
  /* inline: relative & npm package imports are not supported. */
  console.log('I am inlined right here in the final output HTML.');
</script>
```

See how [client-side scripts](/en/guides/client-side-scripts/) work in Astro components.

### `define:vars`

[Section titled “define:vars”](#definevars)

`define:vars={...}` can pass server-side variables from your component frontmatter into the client `<script>` or `<style>` tags. Any JSON-serializable frontmatter variable is supported, including `props` passed to your component through `Astro.props`. Values are serialized with [`JSON.stringify()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

```astro
---
const foregroundColor = "rgb(221 243 228)";
const backgroundColor = "rgb(24 121 78)";
const message = "Astro is awesome!";
---
<style define:vars={{ textColor: foregroundColor, backgroundColor }}>
  h1 {
    background-color: var(--backgroundColor);
    color: var(--textColor);
  }
</style>


<script define:vars={{ message }}>
  alert(message);
</script>
```

Caution

Using `define:vars` on a `<script>` tag implies the [`is:inline` directive](#isinline), which means your scripts won’t be bundled and will be inlined directly into the HTML.

This is because when Astro bundles a script, it includes and runs the script once even if you include the component containing the script multiple times on one page. `define:vars` requires a script to rerun with each set of values, so Astro creates an inline script instead.

For scripts, try [passing variables to scripts manually](/en/guides/client-side-scripts/#pass-frontmatter-variables-to-scripts) instead.

## Advanced Directives

[Section titled “Advanced Directives”](#advanced-directives)

### `is:raw`

[Section titled “is:raw”](#israw)

`is:raw` instructs the Astro compiler to treat any children of that element as text. This means that all special Astro templating syntax will be ignored inside of this component.

For example, if you had a custom Katex component that converted some text to HTML, you could have users do this:

```astro
---
import Katex from '../components/Katex.astro';
---
<Katex is:raw>Some conflicting {syntax} here</Katex>
```

# Error reference

The following reference is a complete list of the errors you may encounter while using Astro. For additional assistance, including common pitfalls, please also see our [Troubleshooting Guide](/en/guides/troubleshooting/).

## Astro Errors

[Section titled “Astro Errors”](#astro-errors)

* [**UnknownCompilerError**](/en/reference/errors/unknown-compiler-error/)\
  Unknown compiler error.
* [**ClientAddressNotAvailable**](/en/reference/errors/client-address-not-available/)\
  `Astro.clientAddress` is not available in current adapter.
* [**PrerenderClientAddressNotAvailable**](/en/reference/errors/prerender-client-address-not-available/)\
  `Astro.clientAddress` cannot be used inside prerendered routes.
* [**StaticClientAddressNotAvailable**](/en/reference/errors/static-client-address-not-available/)\
  `Astro.clientAddress` is not available in prerendered pages.
* [**NoMatchingStaticPathFound**](/en/reference/errors/no-matching-static-path-found/)\
  No static path found for requested path.
* [**OnlyResponseCanBeReturned**](/en/reference/errors/only-response-can-be-returned/)\
  Invalid type returned by Astro page.
* [**MissingMediaQueryDirective**](/en/reference/errors/missing-media-query-directive/)\
  Missing value for `client:media` directive.
* [**NoMatchingRenderer**](/en/reference/errors/no-matching-renderer/)\
  No matching renderer found.
* [**NoClientEntrypoint**](/en/reference/errors/no-client-entrypoint/)\
  No client entrypoint specified in renderer.
* [**NoClientOnlyHint**](/en/reference/errors/no-client-only-hint/)\
  Missing hint on `client:only` directive.
* [**InvalidGetStaticPathParam**](/en/reference/errors/invalid-get-static-path-param/)\
  Invalid value returned by a `getStaticPaths` path.
* [**InvalidGetStaticPathsEntry**](/en/reference/errors/invalid-get-static-paths-entry/)\
  Invalid entry inside getStaticPath’s return value
* [**InvalidGetStaticPathsReturn**](/en/reference/errors/invalid-get-static-paths-return/)\
  Invalid value returned by getStaticPaths.
* [**GetStaticPathsExpectedParams**](/en/reference/errors/get-static-paths-expected-params/)\
  Missing params property on `getStaticPaths` route.
* [**GetStaticPathsInvalidRouteParam**](/en/reference/errors/get-static-paths-invalid-route-param/)\
  Invalid value for `getStaticPaths` route parameter.
* [**GetStaticPathsRequired**](/en/reference/errors/get-static-paths-required/)\
  `getStaticPaths()` function required for dynamic routes.
* [**ReservedSlotName**](/en/reference/errors/reserved-slot-name/)\
  Invalid slot name.
* [**NoAdapterInstalled**](/en/reference/errors/no-adapter-installed/)\
  Cannot use Server-side Rendering without an adapter.
* [**AdapterSupportOutputMismatch**](/en/reference/errors/adapter-support-output-mismatch/)\
  Adapter does not support server output.
* [**NoAdapterInstalledServerIslands**](/en/reference/errors/no-adapter-installed-server-islands/)\
  Cannot use Server Islands without an adapter.
* [**NoMatchingImport**](/en/reference/errors/no-matching-import/)\
  No import found for component.
* [**InvalidPrerenderExport**](/en/reference/errors/invalid-prerender-export/)\
  Invalid prerender export.
* [**InvalidComponentArgs**](/en/reference/errors/invalid-component-args/)\
  Invalid component arguments.
* [**PageNumberParamNotFound**](/en/reference/errors/page-number-param-not-found/)\
  Page number param not found.
* [**ImageMissingAlt**](/en/reference/errors/image-missing-alt/)\
  Image missing required “alt” property.
* [**InvalidImageService**](/en/reference/errors/invalid-image-service/)\
  Error while loading image service.
* [**MissingImageDimension**](/en/reference/errors/missing-image-dimension/)\
  Missing image dimensions
* [**FailedToFetchRemoteImageDimensions**](/en/reference/errors/failed-to-fetch-remote-image-dimensions/)\
  Failed to retrieve remote image dimensions
* [**UnsupportedImageFormat**](/en/reference/errors/unsupported-image-format/)\
  Unsupported image format
* [**UnsupportedImageConversion**](/en/reference/errors/unsupported-image-conversion/)\
  Unsupported image conversion
* [**PrerenderDynamicEndpointPathCollide**](/en/reference/errors/prerender-dynamic-endpoint-path-collide/)\
  Prerendered dynamic endpoint has path collision.
* [**PrerenderRouteConflict**](/en/reference/errors/prerender-route-conflict/)\
  Prerendered route generates the same path as another route.
* [**ExpectedImage**](/en/reference/errors/expected-image/)\
  Expected src to be an image.
* [**ExpectedImageOptions**](/en/reference/errors/expected-image-options/)\
  Expected image options.
* [**ExpectedNotESMImage**](/en/reference/errors/expected-not-esmimage/)\
  Expected image options, not an ESM-imported image.
* [**IncompatibleDescriptorOptions**](/en/reference/errors/incompatible-descriptor-options/)\
  Cannot set both `densities` and `widths`
* [**ImageNotFound**](/en/reference/errors/image-not-found/)\
  Image not found.
* [**NoImageMetadata**](/en/reference/errors/no-image-metadata/)\
  Could not process image metadata.
* [**CouldNotTransformImage**](/en/reference/errors/could-not-transform-image/)\
  Could not transform image.
* [**ResponseSentError**](/en/reference/errors/response-sent-error/)\
  Unable to set response.
* [**MiddlewareNoDataOrNextCalled**](/en/reference/errors/middleware-no-data-or-next-called/)\
  The middleware didn’t return a `Response`.
* [**MiddlewareNotAResponse**](/en/reference/errors/middleware-not-aresponse/)\
  The middleware returned something that is not a `Response` object.
* [**EndpointDidNotReturnAResponse**](/en/reference/errors/endpoint-did-not-return-aresponse/)\
  The endpoint did not return a `Response`.
* [**LocalsNotAnObject**](/en/reference/errors/locals-not-an-object/)\
  Value assigned to `locals` is not accepted.
* [**LocalsReassigned**](/en/reference/errors/locals-reassigned/)\
  `locals` must not be reassigned.
* [**AstroResponseHeadersReassigned**](/en/reference/errors/astro-response-headers-reassigned/)\
  `Astro.response.headers` must not be reassigned.
* [**MiddlewareCantBeLoaded**](/en/reference/errors/middleware-cant-be-loaded/)\
  Can’t load the middleware.
* [**LocalImageUsedWrongly**](/en/reference/errors/local-image-used-wrongly/)\
  Local images must be imported.
* [**AstroGlobUsedOutside**](/en/reference/errors/astro-glob-used-outside/)\
  Astro.glob() used outside of an Astro file.
* [**AstroGlobNoMatch**](/en/reference/errors/astro-glob-no-match/)\
  Astro.glob() did not match any files.
* [**RedirectWithNoLocation**](/en/reference/errors/redirect-with-no-location/)\
  A redirect must be given a location with the `Location` header.
* [**UnsupportedExternalRedirect**](/en/reference/errors/unsupported-external-redirect/)\
  Unsupported or malformed URL.
* [**InvalidDynamicRoute**](/en/reference/errors/invalid-dynamic-route/)\
  Invalid dynamic route.
* [**MissingSharp**](/en/reference/errors/missing-sharp/)\
  Could not find Sharp.
* [**UnknownViteError**](/en/reference/errors/unknown-vite-error/)\
  Unknown Vite Error.
* [**FailedToLoadModuleSSR**](/en/reference/errors/failed-to-load-module-ssr/)\
  Could not import file.
* [**InvalidGlob**](/en/reference/errors/invalid-glob/)\
  Invalid glob pattern.
* [**FailedToFindPageMapSSR**](/en/reference/errors/failed-to-find-page-map-ssr/)\
  Astro couldn’t find the correct page to render
* [**MissingLocale**](/en/reference/errors/missing-locale/)\
  The provided locale does not exist.
* [**MissingIndexForInternationalization**](/en/reference/errors/missing-index-for-internationalization/)\
  Index page not found.
* [**IncorrectStrategyForI18n**](/en/reference/errors/incorrect-strategy-for-i18n/)\
  You can’t use the current function with the current strategy
* [**NoPrerenderedRoutesWithDomains**](/en/reference/errors/no-prerendered-routes-with-domains/)\
  Prerendered routes aren’t supported when internationalization domains are enabled.
* [**MissingMiddlewareForInternationalization**](/en/reference/errors/missing-middleware-for-internationalization/)\
  Enabled manual internationalization routing without having a middleware.
* [**CantRenderPage**](/en/reference/errors/cant-render-page/)\
  Astro can’t render the route.
* [**UnhandledRejection**](/en/reference/errors/unhandled-rejection/)\
  Unhandled rejection
* [**i18nNotEnabled**](/en/reference/errors/i18n-not-enabled/)\
  i18n Not Enabled
* [**i18nNoLocaleFoundInPath**](/en/reference/errors/i18n-no-locale-found-in-path/)\
  The path doesn’t contain any locale
* [**RouteNotFound**](/en/reference/errors/route-not-found/)\
  Route not found.
* [**EnvInvalidVariables**](/en/reference/errors/env-invalid-variables/)\
  Invalid Environment Variables
* [**ServerOnlyModule**](/en/reference/errors/server-only-module/)\
  Module is only available server-side
* [**RewriteWithBodyUsed**](/en/reference/errors/rewrite-with-body-used/)\
  Cannot use Astro.rewrite after the request body has been read
* [**ForbiddenRewrite**](/en/reference/errors/forbidden-rewrite/)\
  Forbidden rewrite to a static route.
* [**UnknownFilesystemError**](/en/reference/errors/unknown-filesystem-error/)\
  An unknown error occurred while reading or writing files to disk.
* [**CannotExtractFontType**](/en/reference/errors/cannot-extract-font-type/)\
  Cannot extract the font type from the given URL.
* [**CannotDetermineWeightAndStyleFromFontFile**](/en/reference/errors/cannot-determine-weight-and-style-from-font-file/)\
  Cannot determine weight and style from font file.
* [**CannotFetchFontFile**](/en/reference/errors/cannot-fetch-font-file/)\
  Cannot fetch the given font file.
* [**CannotLoadFontProvider**](/en/reference/errors/cannot-load-font-provider/)\
  Cannot load font provider
* [**ExperimentalFontsNotEnabled**](/en/reference/errors/experimental-fonts-not-enabled/)\
  Experimental fonts are not enabled
* [**FontFamilyNotFound**](/en/reference/errors/font-family-not-found/)\
  Font family not found
* [**CspNotEnabled**](/en/reference/errors/csp-not-enabled/)\
  CSP feature isn’t enabled

## CSS Errors

[Section titled “CSS Errors”](#css-errors)

* [**UnknownCSSError**](/en/reference/errors/unknown-csserror/)\
  Unknown CSS Error.
* [**CSSSyntaxError**](/en/reference/errors/csssyntax-error/)\
  CSS Syntax Error.

## Markdown Errors

[Section titled “Markdown Errors”](#markdown-errors)

* [**UnknownMarkdownError**](/en/reference/errors/unknown-markdown-error/)\
  Unknown Markdown Error.
* [**MarkdownFrontmatterParseError**](/en/reference/errors/markdown-frontmatter-parse-error/)\
  Failed to parse Markdown frontmatter.
* [**InvalidFrontmatterInjectionError**](/en/reference/errors/invalid-frontmatter-injection-error/)\
  Invalid frontmatter injection.
* [**MdxIntegrationMissingError**](/en/reference/errors/mdx-integration-missing-error/)\
  MDX integration missing.
* [**UnknownConfigError**](/en/reference/errors/unknown-config-error/)\
  Unknown configuration error.
* [**ConfigNotFound**](/en/reference/errors/config-not-found/)\
  Specified configuration file not found.
* [**ConfigLegacyKey**](/en/reference/errors/config-legacy-key/)\
  Legacy configuration detected.

## CLI Errors

[Section titled “CLI Errors”](#cli-errors)

* [**UnknownCLIError**](/en/reference/errors/unknown-clierror/)\
  Unknown CLI Error.
* [**GenerateContentTypesError**](/en/reference/errors/generate-content-types-error/)\
  Failed to generate content types.

## Content Collection Errors

[Section titled “Content Collection Errors”](#content-collection-errors)

* [**UnknownContentCollectionError**](/en/reference/errors/unknown-content-collection-error/)\
  Unknown Content Collection Error.
* [**RenderUndefinedEntryError**](/en/reference/errors/render-undefined-entry-error/)\
  Attempted to render an undefined content collection entry.
* [**GetEntryDeprecationError**](/en/reference/errors/get-entry-deprecation-error/)\
  Invalid use of `getDataEntryById` or `getEntryBySlug` function.
* [**InvalidContentEntryFrontmatterError**](/en/reference/errors/invalid-content-entry-frontmatter-error/)\
  Content entry frontmatter does not match schema.
* [**InvalidContentEntryDataError**](/en/reference/errors/invalid-content-entry-data-error/)\
  Content entry data does not match schema.
* [**ContentLoaderReturnsInvalidId**](/en/reference/errors/content-loader-returns-invalid-id/)\
  Content loader returned an entry with an invalid `id`.
* [**ContentEntryDataError**](/en/reference/errors/content-entry-data-error/)\
  Content entry data does not match schema.
* [**LiveContentConfigError**](/en/reference/errors/live-content-config-error/)\
  Error in live content config.
* [**ContentLoaderInvalidDataError**](/en/reference/errors/content-loader-invalid-data-error/)\
  Content entry is missing an ID
* [**InvalidContentEntrySlugError**](/en/reference/errors/invalid-content-entry-slug-error/)\
  Invalid content entry slug.
* [**ContentSchemaContainsSlugError**](/en/reference/errors/content-schema-contains-slug-error/)\
  Content Schema should not contain `slug`.
* [**MixedContentDataCollectionError**](/en/reference/errors/mixed-content-data-collection-error/)\
  Content and data cannot be in same collection.
* [**ContentCollectionTypeMismatchError**](/en/reference/errors/content-collection-type-mismatch-error/)\
  Collection contains entries of a different type.
* [**DataCollectionEntryParseError**](/en/reference/errors/data-collection-entry-parse-error/)\
  Data collection entry failed to parse.
* [**DuplicateContentEntrySlugError**](/en/reference/errors/duplicate-content-entry-slug-error/)\
  Duplicate content entry slug.
* [**UnsupportedConfigTransformError**](/en/reference/errors/unsupported-config-transform-error/)\
  Unsupported transform in content config.
* [**FileParserNotFound**](/en/reference/errors/file-parser-not-found/)\
  File parser not found
* [**FileGlobNotSupported**](/en/reference/errors/file-glob-not-supported/)\
  Glob patterns are not supported in the file loader

## Action Errors

[Section titled “Action Errors”](#action-errors)

* [**ActionsWithoutServerOutputError**](/en/reference/errors/actions-without-server-output-error/)\
  Actions must be used with server output.
* [**ActionsReturnedInvalidDataError**](/en/reference/errors/actions-returned-invalid-data-error/)\
  Action handler returned invalid data.
* [**ActionNotFoundError**](/en/reference/errors/action-not-found-error/)\
  Action not found.
* [**ActionCalledFromServerError**](/en/reference/errors/action-called-from-server-error/)\
  Action unexpected called from the server.
* [**ActionsCantBeLoaded**](/en/reference/errors/actions-cant-be-loaded/)\
  Can’t load the Astro actions.

## Session Errors

[Section titled “Session Errors”](#session-errors)

* [**SessionStorageInitError**](/en/reference/errors/session-storage-init-error/)\
  Session storage could not be initialized.
* [**SessionStorageSaveError**](/en/reference/errors/session-storage-save-error/)\
  Session data could not be saved.
* [**SessionWithoutSupportedAdapterOutputError**](/en/reference/errors/session-without-supported-adapter-output-error/)\
  Sessions cannot be used with an adapter that doesn’t support server output.
* [**SessionConfigMissingError**](/en/reference/errors/session-config-missing-error/)\
  Session storage was enabled but not configured.
* [**SessionConfigWithoutFlagError**](/en/reference/errors/session-config-without-flag-error/)\
  Session flag not set

# Action unexpected called from the server.

> **ActionCalledFromServerError**: Action called from a server page or endpoint without using `Astro.callAction()`. This wrapper must be used to call actions from server code.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Action called from a server page or endpoint without using `Astro.callAction()`.

**See Also:**

* [`Astro.callAction()` reference](/en/reference/api-reference/#callaction)

# Action not found.

> **ActionNotFoundError**: The server received a request for an action named `ACTION_NAME` but could not find a match. If you renamed an action, check that you’ve updated your `actions/index` file and your calling code to match.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The server received a request for an action but could not find a match with the same name.

# An invalid Action query string was passed by a form.

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **ActionQueryStringInvalidError**: The server received the query string `?_astroAction=ACTION_NAME`, but could not find an action with that name. If you changed an action’s name in development, remove this query param from your URL and refresh.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The server received the query string `?_astroAction=name`, but could not find an action with that name. Use the action function’s `.queryString` property to retrieve the form `action` URL.

**See Also:**

* [Actions RFC](https://github.com/withastro/roadmap/blob/actions/proposals/0046-actions.md)

# Can't load the Astro actions.

> **ActionsCantBeLoaded**: An unknown error was thrown while loading the Astro actions file.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown in development mode when the actions file can’t be loaded.

# Action handler returned invalid data.

> **ActionsReturnedInvalidDataError**: Action handler returned invalid data. Handlers should return serializable data types like objects, arrays, strings, and numbers. Parse error: ERROR

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Action handler returned invalid data. Handlers should return serializable data types, and cannot return a Response object.

**See Also:**

* [Actions handler reference](/en/reference/modules/astro-actions/#handler-property)

# An invalid Action query string was passed by a form.

Deprecated

Deprecated since version 4.13.2.

> **ActionsUsedWithForGetError**: Action ACTION\_NAME was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Action was called from a form using a GET request, but only POST requests are supported. This often occurs if `method="POST"` is missing on the form.

**See Also:**

* [Actions RFC](https://github.com/withastro/roadmap/blob/actions/proposals/0046-actions.md)

# Actions must be used with server output.

> **ActionsWithoutServerOutputError**: A server is required to create callable backend functions. To deploy routes to a server, add an adapter to your Astro config and configure your route for on-demand rendering

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Your project must have a server output to create backend functions with Actions.

**See Also:**

* [On-demand rendering](/en/guides/on-demand-rendering/)

# Adapter does not support server output.

> **AdapterSupportOutputMismatch**: The `ADAPTER_NAME` adapter is configured to output a static website, but the project contains server-rendered pages. Please install and configure the appropriate server adapter for your final deployment.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The currently configured adapter does not support server-side rendering, which is required for the current project setup.

Depending on your adapter, there may be a different entrypoint to use for server-side rendering. For example, the `@astrojs/vercel` adapter has a `@astrojs/vercel/static` entrypoint for static rendering, and a `@astrojs/vercel/serverless` entrypoint for server-side rendering.

**See Also:**

* [Server-side Rendering](/en/guides/on-demand-rendering/)

# Astro.glob() did not match any files.

> **AstroGlobNoMatch**: `Astro.glob(GLOB_STR)` did not return any matching files.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.glob()` did not return any matching files. There might be a typo in the glob pattern.

**See Also:**

* [Astro.glob](/en/reference/api-reference/#astroglob)

# Astro.glob() used outside of an Astro file.

> **AstroGlobUsedOutside**: `Astro.glob(GLOB_STR)` can only be used in `.astro` files. `import.meta.glob(GLOB_STR)` can be used instead to achieve a similar result.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.glob()` can only be used in `.astro` files. You can use [`import.meta.glob()`](https://vite.dev/guide/features.html#glob-import) instead to achieve the same result.

**See Also:**

* [Astro.glob](/en/reference/api-reference/#astroglob)

# Astro.response.headers must not be reassigned.

> **AstroResponseHeadersReassigned**: Individual headers can be added to and removed from `Astro.response.headers`, but it must not be replaced with another instance of `Headers` altogether.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when a value is being set as the `headers` field on the `ResponseInit` object available as `Astro.response`.

# Cannot determine weight and style from font file.

> An error occurred while determining the weight and style from the local font file.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Cannot determine weight and style from font file, update your family config and set `weight` and `style` manually instead.

# Cannot extract the font type from the given URL.

> An error occurred while trying to extract the font type from the given URL.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Cannot extract the font type from the given URL.

# Cannot fetch the given font file.

> An error occurred while fetching font file from the given URL.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Cannot fetch the given font file

# Cannot load font provider

> Astro is unable to load the given font provider. Open an issue on the corresponding provider’s repository.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Cannot load font provider

# Astro can't render the route.

> **CantRenderPage**: Astro cannot find any content to render for this route. There is no file or redirect associated with this route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find an associated file with content while trying to render the route. This is an Astro error and not a user error. If restarting the dev server does not fix the problem, please file an issue.

# Cannot use the astro:config module without enabling the experimental feature.

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **CantUseAstroConfigModuleError**: Cannot import the module “MODULE\_NAME” because the experimental feature is disabled. Enable `experimental.serializeConfig` in your `astro.config.mjs`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Cannot use the module `astro:config` without enabling the experimental feature.

# Astro.clientAddress is not available in current adapter.

> **ClientAddressNotAvailable**: `Astro.clientAddress` is not available in the `ADAPTER_NAME` adapter. File an issue with the adapter to add support.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The adapter you’re using unfortunately does not support `Astro.clientAddress`.

**See Also:**

* [Official integrations](/en/guides/integrations-guide/#official-integrations)
* [Astro.clientAddress](/en/reference/api-reference/#clientaddress)

# Collection does not exist

Deprecated

Collections that do not exist no longer result in an error. A warning is given instead.

> A collection queried via `getCollection()` does not exist.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

When querying a collection, ensure a collection directory with the requested name exists under `src/content/`.

# Legacy configuration detected.

> **ConfigLegacyKey**: Legacy configuration detected: `LEGACY_CONFIG_KEY`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro detected a legacy configuration option in your configuration file.

**See Also:**

* [Configuration reference](/en/reference/configuration-reference/)

# Specified configuration file not found.

> **ConfigNotFound**: Unable to resolve `--config "CONFIG_FILE"`. Does the file exist?

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The specified configuration file using `--config` could not be found. Make sure that it exists or that the path is correct

**See Also:**

* [--config](/en/reference/cli-reference/#--config-path)

# Collection contains entries of a different type.

> **ContentCollectionTypeMismatchError**: COLLECTION contains EXPECTED\_TYPE entries, but is configured as a ACTUAL\_TYPE collection.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Legacy content collections must contain entries of the type configured. Collections are `type: 'content'` by default. Try adding `type: 'data'` to your collection config for data collections.

**See Also:**

* [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

# Content entry data does not match schema.

> **Example error message:**\
> **blog** → **post** data does not match collection schema.\
> “title” is required.\
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A content entry does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content.config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

# Content entry is missing an ID

> **Example error message:**\
> The loader for **blog** returned invalid data.\
> Object is missing required property “id”.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The loader for a content collection returned invalid data. Inline loaders must return an array of objects with unique ID fields or a plain object with IDs as keys and entries as values.

# Content loader returned an entry with an invalid id.

> **Example error message:**\
> The content loader for the collection **blog** returned an entry with an invalid `id`:\
> {\
> “id”: 1,\
> “title”: “Hello, World!”\
> }

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A content loader returned an invalid `id`. Make sure that the `id` of the entry is a string. See the [Content collections documentation](/en/guides/content-collections/) for more information.

# Content Schema should not contain slug.

> **ContentSchemaContainsSlugError**: A content collection schema should not contain `slug` since it is reserved for slug generation. Remove this from your COLLECTION\_NAME collection schema.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A legacy content collection schema should not contain the `slug` field. This is reserved by Astro for generating entry slugs. Remove `slug` from your schema. You can still use custom slugs in your frontmatter.

**See Also:**

* [Legacy content collections](/en/guides/upgrade-to/v5/#updating-existing-collections)

# Could not transform image.

> **CouldNotTransformImage**: Could not transform image `IMAGE_PATH`. See the stack trace for more information.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not transform one of your images. Often, this is caused by a corrupted or malformed image. Re-exporting the image from your image editor may fix this issue.

Depending on the image service you are using, the stack trace may contain more information on the specific error encountered.

**See Also:**

* [Images](/en/guides/images/)

# CSP feature isn't enabled

> The `experimental.csp` configuration isn’t enabled.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The CSP feature isn’t enabled

# CSS Syntax Error.

> **Example error messages:**\
> CSSSyntaxError: Missed semicolon\
> CSSSyntaxError: Unclosed string

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro encountered an error while parsing your CSS, due to a syntax error. This is often caused by a missing semicolon.

# Data collection entry failed to parse.

> `COLLECTION_ENTRY_NAME` failed to parse.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Collection entries of `type: 'data'` must return an object with valid JSON (for `.json` entries), YAML (for `.yaml` entries) or TOML (for `.toml` entries).

# Duplicate content entry slug.

> `COLLECTION_NAME` contains multiple entries with the same slug: `SLUG`. Slugs must be unique.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Content collection entries must have unique slugs. Duplicates are often caused by the `slug` frontmatter property.

# The endpoint did not return a Response.

> **EndpointDidNotReturnAResponse**: An endpoint must return either a `Response`, or a `Promise` that resolves with a `Response`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Thrown when an endpoint does not return anything or returns an object that is not a `Response` object.

An endpoint must return either a `Response`, or a `Promise` that resolves with a `Response`. For example:

```ts
import type { APIContext } from 'astro';


export async function GET({ request, url, cookies }: APIContext): Promise<Response> {
    return Response.json({
        success: true,
        result: 'Data from Astro Endpoint!'
    })
}
```

# Invalid Environment Variable

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **EnvInvalidVariable**: The following environment variable does not match the data type and/or properties defined in `experimental.env.schema`: KEY is not of type TYPE

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An environment variable does not match the data type and/or properties defined in `experimental.env.schema`.

# Invalid Environment Variables

> The following environment variables defined in `env.schema` are invalid.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Some environment variables do not match the data type and/or properties defined in `env.schema`.

# Unsupported astro:env getSecret

Deprecated

This error is from an older version of Astro and is no longer in use. If you are unable to upgrade your project to a more recent version, then you can consult [unmaintained snapshots of older documentation](/en/upgrade-astro/#older-docs-unmaintained) for assistance.

> **EnvUnsupportedGetSecret**: `astro:env/server` exported function `getSecret` is not supported by your adapter.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `astro:env/server` exported function `getSecret()` is not supported by your adapter.

# Expected src to be an image.

> **ExpectedImage**: Expected `src` property for `getImage` or `<Image />` to be either an ESM imported image or a string with the path of a remote image. Received `SRC` (type: `TYPEOF_OPTIONS`).\
> \
> Full serialized options received: `FULL_OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An image’s `src` property is not valid. The Image component requires the `src` attribute to be either an image that has been ESM imported or a string. This is also true for the first parameter of `getImage()`.

```astro
---
import { Image } from "astro:assets";
import myImage from "../assets/my_image.png";
---


<Image src={myImage} alt="..." />
<Image src="https://example.com/logo.png" width={300} height={300} alt="..." />
```

In most cases, this error happens when the value passed to `src` is undefined.

**See Also:**

* [Images](/en/guides/images/)

# Expected image options.

> **ExpectedImageOptions**: Expected getImage() parameter to be an object. Received `OPTIONS`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getImage()`’s first parameter should be an object with the different properties to apply to your image.

```ts
import { getImage } from "astro:assets";
import myImage from "../assets/my_image.png";


const optimizedImage = await getImage({src: myImage, width: 300, height: 300});
```

In most cases, this error happens because parameters were passed directly instead of inside an object.

**See Also:**

* [Images](/en/guides/images/)

# Expected image options, not an ESM-imported image.

> **ExpectedNotESMImage**: An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An ESM-imported image cannot be passed directly to `getImage()`. Instead, pass an object with the image in the `src` property.

```diff
import { getImage } from "astro:assets";
import myImage from "../assets/my_image.png";
 const optimizedImage = await getImage( myImage );
 const optimizedImage = await getImage({ src: myImage });
```

**See Also:**

* [Images](/en/guides/images/)

# Experimental fonts are not enabled

> **ExperimentalFontsNotEnabled**: The Font component is used but experimental fonts have not been registered in the config.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Font component is used but experimental fonts have not been registered in the config.

# Failed to retrieve remote image dimensions

> Failed to get the dimensions for `IMAGE_URL`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Determining the remote image’s dimensions failed. This is typically caused by an incorrect URL or attempting to infer the size of an image in the public folder which is not possible.

# Astro couldn't find the correct page to render

> **FailedToFindPageMapSSR**: Astro couldn’t find the correct page to render, probably because it wasn’t correctly mapped for SSR usage. This is an internal error. Please file an issue.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro couldn’t find the correct page to render, probably because it wasn’t correctly mapped for SSR usage. This is an internal error.

# Could not import file.

> **FailedToLoadModuleSSR**: Could not import `IMPORT_NAME`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not import the requested file. Oftentimes, this is caused by the import path being wrong (either because the file does not exist, or there is a typo in the path)

This message can also appear when a type is imported without specifying that it is a [type import](/en/guides/typescript/#type-imports).

**See Also:**

* [Type Imports](/en/guides/typescript/#type-imports)

# Glob patterns are not supported in the file loader

> **FileGlobNotSupported**: Glob patterns are not supported in the `file` loader. Use the `glob` loader instead.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `file` loader must be passed a single local file. Glob patterns are not supported. Use the built-in `glob` loader to create entries from patterns of multiple local files.

**See Also:**

* [Astro’s built-in loaders](/en/guides/content-collections/#built-in-loaders)

# File parser not found

> **FileParserNotFound**: No parser was found for ‘FILE\_NAME’. Pass a parser function (e.g. `parser: csv`) to the `file` loader.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `file` loader can’t determine which parser to use. Please provide a custom parser (e.g. `csv-parse`) to create a collection from your file type.

**See Also:**

* [Passing a `parser` to the `file` loader](/en/guides/content-collections/#parser-function)

# Font family not found

> No data was found for the `cssVariable` passed to the `<Font />` component or to the `getFontData()` function.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Font family not found

# Forbidden rewrite to a static route.

> **ForbiddenRewrite**: You tried to rewrite the on-demand route ‘FROM’ with the static route ‘TO’, when using the ‘server’ output.\
> \
> The static route ‘TO’ is rendered by the component ‘COMPONENT’, which is marked as prerendered. This is a forbidden operation because during the build the component ‘COMPONENT’ is compiled to an HTML file, which can’t be retrieved at runtime by Astro.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`Astro.rewrite()` can’t be used to rewrite an on-demand route with a static route when using the `"server"` output.

# Failed to generate content types.

> **GenerateContentTypesError**: `astro sync` command failed to generate content collection types: ERROR\_MESSAGE

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`astro sync` command failed to generate content collection types.

**See Also:**

* [Content collections documentation](/en/guides/content-collections/)

# Invalid use of getDataEntryById or getEntryBySlug function.

> **GetEntryDeprecationError**: The `METHOD` function is deprecated and cannot be used to query the “COLLECTION” collection. Use `getEntry` instead.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `getDataEntryById` and `getEntryBySlug` functions are deprecated and cannot be used with content layer collections. Use the `getEntry` function instead.

# Missing params property on getStaticPaths route.

> **GetStaticPathsExpectedParams**: Missing or empty required `params` property on `getStaticPaths` route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Every route specified by `getStaticPaths` require a `params` property specifying the path parameters needed to match the route.

For instance, the following code:

pages/blog/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: '1' } }
  ];
}
---
```

Will create the following route: `site.com/blog/1`.

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

# Invalid value for getStaticPaths route parameter.

> **GetStaticPathsInvalidRouteParam**: Invalid getStaticPaths route parameter for `KEY`. Expected undefined, a string or a number, received `VALUE_TYPE` (`VALUE`)

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Since `params` are encoded into the URL, only certain types are supported as values.

/route/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: '1' } } // Works
    { params: { id: 2 } } // Works
    { params: { id: false } } // Does not work
  ];
}
---
```

In routes using [rest parameters](/en/guides/routing/#rest-parameters), `undefined` can be used to represent a path with no parameters passed in the URL:

/route/\[...id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { id: 1 } } // /route/1
    { params: { id: 2 } } // /route/2
    { params: { id: undefined } } // /route/
  ];
}
---
```

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)

# getStaticPaths RSS helper is not available anymore.

Deprecated

Deprecated since Astro 4.0. The RSS helper no longer exists with an error fallback.

> **GetStaticPathsRemovedRSSHelper**: The RSS helper has been removed from `getStaticPaths`. Try the new @astrojs/rss package instead.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

`getStaticPaths` no longer expose an helper for generating a RSS feed. We recommend migrating to the [@astrojs/rss](/en/recipes/rss/#setting-up-astrojsrss)integration instead.

**See Also:**

* [RSS Guide](/en/recipes/rss/)

# getStaticPaths() function required for dynamic routes.

> **GetStaticPathsRequired**: `getStaticPaths()` function is required for dynamic routes. Make sure that you `export` a `getStaticPaths` function from your dynamic route.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

In [Static Mode](/en/guides/routing/#static-ssg-mode), all routes must be determined at build time. As such, dynamic routes must `export` a `getStaticPaths` function returning the different paths to generate.

**See Also:**

* [Dynamic Routes](/en/guides/routing/#dynamic-routes)
* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [Server-side Rendering](/en/guides/on-demand-rendering/)

# The path doesn't contain any locale

> **i18nNoLocaleFoundInPath**: You tried to use an i18n utility on a path that doesn’t contain any locale. You can use `pathHasLocale` first to determine if the path has a locale.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

An i18n utility tried to use the locale from a URL path that does not contain one. You can prevent this error by using pathHasLocale to check URLs for a locale first before using i18n utilities.

# i18n Not Enabled

> **i18nNotEnabled**: The `astro:i18n` module can not be used without enabling i18n in your Astro config.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `astro:i18n` module can not be used without enabling i18n in your Astro config. To enable i18n, add a default locale and a list of supported locales to your Astro config:

```js
import { defineConfig } from 'astro'
export default defineConfig({
 i18n: {
   locales: ['en', 'fr'],
   defaultLocale: 'en',
  },
})
```

For more information on internationalization support in Astro, see our [Internationalization guide](/en/guides/internationalization/).

**See Also:**

* [Internationalization](/en/guides/internationalization/)
* [`i18n` Configuration Reference](/en/reference/configuration-reference/#i18n)

# Image missing required "alt" property.

> **ImageMissingAlt**: Image missing “alt” property. “alt” text is required to describe important images on the page.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `alt` property allows you to provide descriptive alt text to users of screen readers and other assistive technologies. In order to ensure your images are accessible, the `Image` component requires that an `alt` be specified.

If the image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers know to ignore the image.

**See Also:**

* [Images](/en/guides/images/)
* [Image component](/en/reference/modules/astro-assets/#image-)
*  [Image component#alt](/en/reference/modules/astro-assets/#alt-required)

# Image not found.

> **ImageNotFound**: Could not find requested image `IMAGE_PATH`. Does it exist?

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro could not find an image you imported. Often, this is simply caused by a typo in the path.

Images in Markdown are relative to the current file. To refer to an image that is located in the same folder as the `.md` file, the path should start with `./`

**See Also:**

* [Images](/en/guides/images/)

# Cannot set both densities and widths

> **IncompatibleDescriptorOptions**: Only one of `densities` or `widths` can be specified. In most cases, you’ll probably want to use only `widths` if you require specific widths.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Only one of `densities` or `widths` can be specified. Those attributes are used to construct a `srcset` attribute, which cannot have both `x` and `w` descriptors.

**See Also:**

* [Images](/en/guides/images/)

# You can't use the current function with the current strategy

> **IncorrectStrategyForI18n**: The function `FUNCTION_NAME` can only be used when the `i18n.routing.strategy` is set to `"manual"`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Some internationalization functions are only available when Astro’s own i18n routing is disabled by the configuration setting `i18n.routing: "manual"`.

**See Also:**

* [`i18n` routing](/en/guides/internationalization/#routing)

# Invalid component arguments.

> **Example error messages:**\
> InvalidComponentArgs: Invalid arguments passed to `<MyAstroComponent>` component.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

Astro components cannot be rendered manually via a function call, such as `Component()` or `{items.map(Component)}`. Prefer the component syntax `<Component />` or `{items.map(item => <Component {...item} />)}`.

# Content entry data does not match schema.

> **Example error message:**\
> **blog** → **post** frontmatter does not match collection schema.\
> “title” is required.\
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A content entry does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content.config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

# Content entry frontmatter does not match schema.

> **Example error message:**\
> **blog** → **post.md** frontmatter does not match collection schema.\
> “title” is required.\
> “date” must be a valid date.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A Markdown or MDX entry does not match its collection schema. Make sure that all required fields are present, and that all fields are of the correct type. You can check against the collection schema in your `src/content.config.*` file. See the [Content collections documentation](/en/guides/content-collections/) for more information.

# Invalid content entry slug.

> `COLLECTION_NAME` → `ENTRY_ID` has an invalid slug. `slug` must be a string.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A collection entry has an invalid `slug`. This field is reserved for generating entry slugs, and must be a string when present.

**See Also:**

* [The reserved entry `slug` field](/en/guides/content-collections/)

# Invalid dynamic route.

> **InvalidDynamicRoute**: The INVALID\_PARAM param for route ROUTE is invalid. Received **RECEIVED**.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A dynamic route param is invalid. This is often caused by an `undefined` parameter or a missing [rest parameter](/en/guides/routing/#rest-parameters).

**See Also:**

* [Dynamic routes](/en/guides/routing/#dynamic-routes)

# Invalid frontmatter injection.

> **InvalidFrontmatterInjectionError**: A remark or rehype plugin attempted to inject invalid frontmatter. Ensure “astro.frontmatter” is set to a valid JSON object that is not `null` or `undefined`.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

A remark or rehype plugin attempted to inject invalid frontmatter. This occurs when “astro.frontmatter” is set to `null`, `undefined`, or an invalid JSON object.

**See Also:**

* [Modifying frontmatter programmatically](/en/guides/markdown-content/#modifying-frontmatter-programmatically)

# Invalid value returned by a getStaticPaths path.

> **InvalidGetStaticPathParam**: Invalid params given to `getStaticPaths` path. Expected an `object`, got `PARAM_TYPE`

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `params` property in `getStaticPaths`’s return value (an array of objects) should also be an object.

pages/blog/\[id].astro

```astro
---
export async function getStaticPaths() {
  return [
    { params: { slug: "blog" } },
    { params: { slug: "about" } }
  ];
}
---
```

**See Also:**

* [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths)
* [`params`](/en/reference/api-reference/#params)


---

**Navigation:** [← Previous](./11-create-a-dev-toolbar-app.md) | [Index](./index.md) | [Next →](./13-invalid-entry-inside-getstaticpaths-return-value.md)
