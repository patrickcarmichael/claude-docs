**Navigation:** [← Previous](./16-instrumentationjs.md) | [Index](./index.md) | [Next →](./18-turbopack.md)

---

# images

@router: Pages Router

If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure `next.config.js` with the following:

```js filename="next.config.js"
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

This `loaderFile` must point to a file relative to the root of your Next.js application. The file must export a default function that returns a string, for example:

```js filename="my/image/loader.js"
export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

Alternatively, you can use the [`loader` prop](/docs/pages/api-reference/components/image.md#loader) to pass the function to each instance of `next/image`.

To learn more about configuring the behavior of the built-in [Image Optimization API](/docs/pages/api-reference/components/image.md) and the [Image Component](/docs/pages/api-reference/components/image.md), see [Image Configuration Options](/docs/pages/api-reference/components/image.md#configuration-options) for available options.

## Example Loader Configuration

* [Akamai](#akamai)
* [AWS CloudFront](#aws-cloudfront)
* [Cloudinary](#cloudinary)
* [Cloudflare](#cloudflare)
* [Contentful](#contentful)
* [Fastly](#fastly)
* [Gumlet](#gumlet)
* [ImageEngine](#imageengine)
* [Imgix](#imgix)
* [PixelBin](#pixelbin)
* [Sanity](#sanity)
* [Sirv](#sirv)
* [Supabase](#supabase)
* [Thumbor](#thumbor)
* [Imagekit](#imagekitio)
* [Nitrogen AIO](#nitrogen-aio)

### Akamai

```js
// Docs: https://techdocs.akamai.com/ivm/reference/test-images-on-demand
export default function akamaiLoader({ src, width, quality }) {
  return `https://example.com/${src}?imwidth=${width}`
}
```

### AWS CloudFront

```js
// Docs: https://aws.amazon.com/developer/application-security-performance/articles/image-optimization
export default function cloudfrontLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  url.searchParams.set('format', 'auto')
  url.searchParams.set('width', width.toString())
  url.searchParams.set('quality', (quality || 75).toString())
  return url.href
}
```

### Cloudinary

```js
// Demo: https://res.cloudinary.com/demo/image/upload/w_300,c_limit,q_auto/turtles.jpg
export default function cloudinaryLoader({ src, width, quality }) {
  const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
  return `https://example.com/${params.join(',')}${src}`
}
```

### Cloudflare

```js
// Docs: https://developers.cloudflare.com/images/transform-images
export default function cloudflareLoader({ src, width, quality }) {
  const params = [`width=${width}`, `quality=${quality || 75}`, 'format=auto']
  return `https://example.com/cdn-cgi/image/${params.join(',')}/${src}`
}
```

### Contentful

```js
// Docs: https://www.contentful.com/developers/docs/references/images-api/
export default function contentfulLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  url.searchParams.set('fm', 'webp')
  url.searchParams.set('w', width.toString())
  url.searchParams.set('q', (quality || 75).toString())
  return url.href
}
```

### Fastly

```js
// Docs: https://developer.fastly.com/reference/io/
export default function fastlyLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  url.searchParams.set('auto', 'webp')
  url.searchParams.set('width', width.toString())
  url.searchParams.set('quality', (quality || 75).toString())
  return url.href
}
```

### Gumlet

```js
// Docs: https://docs.gumlet.com/reference/image-transform-size
export default function gumletLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  url.searchParams.set('format', 'auto')
  url.searchParams.set('w', width.toString())
  url.searchParams.set('q', (quality || 75).toString())
  return url.href
}
```

### ImageEngine

```js
// Docs: https://support.imageengine.io/hc/en-us/articles/360058880672-Directives
export default function imageengineLoader({ src, width, quality }) {
  const compression = 100 - (quality || 50)
  const params = [`w_${width}`, `cmpr_${compression}`)]
  return `https://example.com${src}?imgeng=/${params.join('/')`
}
```

### Imgix

```js
// Demo: https://static.imgix.net/daisy.png?format=auto&fit=max&w=300
export default function imgixLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  const params = url.searchParams
  params.set('auto', params.getAll('auto').join(',') || 'format')
  params.set('fit', params.get('fit') || 'max')
  params.set('w', params.get('w') || width.toString())
  params.set('q', (quality || 50).toString())
  return url.href
}
```

### PixelBin

```js
// Doc (Resize): https://www.pixelbin.io/docs/transformations/basic/resize/#width-w
// Doc (Optimise): https://www.pixelbin.io/docs/optimizations/quality/#image-quality-when-delivering
// Doc (Auto Format Delivery): https://www.pixelbin.io/docs/optimizations/format/#automatic-format-selection-with-f_auto-url-parameter
export default function pixelBinLoader({ src, width, quality }) {
  const name = '<your-cloud-name>'
  const opt = `t.resize(w:${width})~t.compress(q:${quality || 75})`
  return `https://cdn.pixelbin.io/v2/${name}/${opt}/${src}?f_auto=true`
}
```

### Sanity

```js
// Docs: https://www.sanity.io/docs/image-urls
export default function sanityLoader({ src, width, quality }) {
  const prj = 'zp7mbokg'
  const dataset = 'production'
  const url = new URL(`https://cdn.sanity.io/images/${prj}/${dataset}${src}`)
  url.searchParams.set('auto', 'format')
  url.searchParams.set('fit', 'max')
  url.searchParams.set('w', width.toString())
  if (quality) {
    url.searchParams.set('q', quality.toString())
  }
  return url.href
}
```

### Sirv

```js
// Docs: https://sirv.com/help/articles/dynamic-imaging/
export default function sirvLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  const params = url.searchParams
  params.set('format', params.getAll('format').join(',') || 'optimal')
  params.set('w', params.get('w') || width.toString())
  params.set('q', (quality || 85).toString())
  return url.href
}
```

### Supabase

```js
// Docs: https://supabase.com/docs/guides/storage/image-transformations#nextjs-loader
export default function supabaseLoader({ src, width, quality }) {
  const url = new URL(`https://example.com${src}`)
  url.searchParams.set('width', width.toString())
  url.searchParams.set('quality', (quality || 75).toString())
  return url.href
}
```

### Thumbor

```js
// Docs: https://thumbor.readthedocs.io/en/latest/
export default function thumborLoader({ src, width, quality }) {
  const params = [`${width}x0`, `filters:quality(${quality || 75})`]
  return `https://example.com${params.join('/')}${src}`
}
```

### ImageKit.io

```js
// Docs: https://imagekit.io/docs/image-transformation
export default function imageKitLoader({ src, width, quality }) {
  const params = [`w-${width}`, `q-${quality || 80}`]
  return `https://ik.imagekit.io/your_imagekit_id/${src}?tr=${params.join(',')}`
}
```

### Nitrogen AIO

```js
// Docs: https://docs.n7.io/aio/intergrations/
export default function aioLoader({ src, width, quality }) {
  const url = new URL(src, window.location.href)
  const params = url.searchParams
  const aioParams = params.getAll('aio')
  aioParams.push(`w-${width}`)
  if (quality) {
    aioParams.push(`q-${quality.toString()}`)
  }
  params.set('aio', aioParams.join(';'))
  return url.href
}
```


--------------------------------------------------------------------------------
title: "isolatedDevBuild"
description: "Use isolated build outputs for development server to prevent conflicts with production builds."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/isolatedDevBuild"
--------------------------------------------------------------------------------

# isolatedDevBuild

@router: Pages Router

> This feature is currently experimental and subject to change, it is not recommended for production.

The experimental `isolatedDevBuild` option separates development and production build outputs into different directories. When enabled, the development server (`next dev`) writes its output to `.next/dev` instead of `.next`, preventing conflicts when running `next dev` and `next build` concurrently.

This is especially helpful when automated tools (for example, AI agents) run `next build` to validate changes while your development server is running, ensuring the dev server is not affected by changes made by the build process.

This feature is **enabled by default** to keep development and production outputs separate and prevent conflicts.

## Configuration

To opt out of this feature, set `isolatedDevBuild` to `false` in your configuration:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    isolatedDevBuild: false, // defaults to true
  },
}

export default nextConfig
```

```js filename="next.config.mjs" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    isolatedDevBuild: false, // defaults to true
  },
}

export default nextConfig
```

## Version History

| Version   | Changes                                        |
| --------- | ---------------------------------------------- |
| `v16.0.0` | `experimental.isolatedDevBuild` is introduced. |


--------------------------------------------------------------------------------
title: "onDemandEntries"
description: "Configure how Next.js will dispose and keep in memory pages created in development."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries"
--------------------------------------------------------------------------------

# onDemandEntries

@router: Pages Router

Next.js exposes some options that give you some control over how the server will dispose or keep in memory built pages in development.

To change the defaults, open `next.config.js` and add the `onDemandEntries` config:

```js filename="next.config.js"
module.exports = {
  onDemandEntries: {
    // period (in ms) where the server will keep pages in the buffer
    maxInactiveAge: 25 * 1000,
    // number of pages that should be kept simultaneously without being disposed
    pagesBufferLength: 2,
  },
}
```


--------------------------------------------------------------------------------
title: "optimizePackageImports"
description: "API Reference for optimizePackageImports Next.js Config Option"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports"
--------------------------------------------------------------------------------

# optimizePackageImports

@router: Pages Router

Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.

Adding a package to `experimental.optimizePackageImports` will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.

```js filename="next.config.js"
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

The following libraries are optimized by default:

* `lucide-react`
* `date-fns`
* `lodash-es`
* `ramda`
* `antd`
* `react-bootstrap`
* `ahooks`
* `@ant-design/icons`
* `@headlessui/react`
* `@headlessui-float/react`
* `@heroicons/react/20/solid`
* `@heroicons/react/24/solid`
* `@heroicons/react/24/outline`
* `@visx/visx`
* `@tremor/react`
* `rxjs`
* `@mui/material`
* `@mui/icons-material`
* `recharts`
* `react-use`
* `@material-ui/core`
* `@material-ui/icons`
* `@tabler/icons-react`
* `mui-core`
* `react-icons/*`
* `effect`
* `@effect/*`


--------------------------------------------------------------------------------
title: "output"
description: "Next.js automatically traces which files are needed by each page to allow for easy deployment of your application. Learn how it works here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/output"
--------------------------------------------------------------------------------

# output

@router: Pages Router

During a build, Next.js will automatically trace each page and its dependencies to determine all of the files that are needed for deploying a production version of your application.

This feature helps reduce the size of deployments drastically. Previously, when deploying with Docker you would need to have all files from your package's `dependencies` installed to run `next start`. Starting with Next.js 12, you can leverage Output File Tracing in the `.next/` directory to only include the necessary files.

Furthermore, this removes the need for the deprecated `serverless` target which can cause various issues and also creates unnecessary duplication.

## How it Works

During `next build`, Next.js will use [`@vercel/nft`](https://github.com/vercel/nft) to statically analyze `import`, `require`, and `fs` usage to determine all files that a page might load.

Next.js' production server is also traced for its needed files and output at `.next/next-server.js.nft.json` which can be leveraged in production.

To leverage the `.nft.json` files emitted to the `.next` output directory, you can read the list of files in each trace that are relative to the `.nft.json` file and then copy them to your deployment location.

## Automatically Copying Traced Files

Next.js can automatically create a `standalone` folder that copies only the necessary files for a production deployment including select files in `node_modules`.

To leverage this automatic copying you can enable it in your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  output: 'standalone',
}
```

This will create a folder at `.next/standalone` which can then be deployed on its own without installing `node_modules`.

Additionally, a minimal `server.js` file is also output which can be used instead of `next start`. This minimal server does not copy the `public` or `.next/static` folders by default as these should ideally be handled by a CDN instead, although these folders can be copied to the `standalone/public` and `standalone/.next/static` folders manually, after which `server.js` file will serve these automatically.

To copy these manually, you can use the `cp` command-line tool after you `next build`:

```bash filename="Terminal"
cp -r public .next/standalone/ && cp -r .next/static .next/standalone/.next/
```

To start your minimal `server.js` file locally, run the following command:

```bash filename="Terminal"
node .next/standalone/server.js
```

> **Good to know**:
>
> * `next.config.js` is read during `next build` and serialized into the `server.js` output file.
> * If your project needs to listen to a specific port or hostname, you can define `PORT` or `HOSTNAME` environment variables before running `server.js`. For example, run `PORT=8080 HOSTNAME=0.0.0.0 node server.js` to start the server on `http://0.0.0.0:8080`.

## Caveats

* While tracing in monorepo setups, the project directory is used for tracing by default. For `next build packages/web-app`, `packages/web-app` would be the tracing root and any files outside of that folder will not be included. To include files outside of this folder you can set `outputFileTracingRoot` in your `next.config.js`.

```js filename="packages/web-app/next.config.js"
const path = require('path')

module.exports = {
  // this includes files from the monorepo base two directories up
  outputFileTracingRoot: path.join(__dirname, '../../'),
}
```

* There are some cases in which Next.js might fail to include required files, or might incorrectly include unused files. In those cases, you can leverage `outputFileTracingExcludes` and `outputFileTracingIncludes` respectively in `next.config.js`. Each option accepts an object whose keys are **route globs** (matched with [picomatch](https://www.npmjs.com/package/picomatch#basic-globbing) against the route path, e.g. `/api/hello`) and whose values are **glob patterns resolved from the project root** that specify files to include or exclude in the trace.

> **Good to know**:
> In a monorepo, `project root` refers to the Next.js project root (the folder containing next.config.js, e.g., packages/web-app), not necessarily the monorepo root.

```js filename="next.config.js"
module.exports = {
  outputFileTracingExcludes: {
    '/api/hello': ['./un-necessary-folder/**/*'],
  },
  outputFileTracingIncludes: {
    '/api/another': ['./necessary-folder/**/*'],
    '/api/login/\\[\\[\\.\\.\\.slug\\]\\]': [
      './node_modules/aws-crt/dist/bin/**/*',
    ],
  },
}
```

Using a `src/` directory does not change how you write these options:

* **Keys** still match the route path (`'/api/hello'`, `'/products/[id]'`, etc.).
* **Values** can reference paths under `src/` since they are resolved relative to the project root.

```js filename="next.config.js"
module.exports = {
  outputFileTracingIncludes: {
    '/products/*': ['src/lib/payments/**/*'],
    '/*': ['src/config/runtime/**/*.json'],
  },
  outputFileTracingExcludes: {
    '/api/*': ['src/temp/**/*', 'public/large-logs/**/*'],
  },
}
```

You can also target all routes using a global key like `'/*'`:

```js filename="next.config.js"
module.exports = {
  outputFileTracingIncludes: {
    '/*': ['src/i18n/locales/**/*.json'],
  },
}
```

These options are applied to server traces and do not affect routes that do not produce a server trace file:

* Edge Runtime routes are not affected.
* Fully static pages are not affected.

In monorepos or when you need to include files outside the app folder, combine `outputFileTracingRoot` with includes:

```js filename="next.config.js"
const path = require('path')

module.exports = {
  // Trace from the monorepo root
  outputFileTracingRoot: path.join(__dirname, '../../'),
  outputFileTracingIncludes: {
    '/route1': ['../shared/assets/**/*'],
  },
}
```

> **Good to know**:
>
> * Prefer forward slashes (`/`) in patterns for cross-platform compatibility.
> * Keep patterns as narrow as possible to avoid oversized traces (avoid `**/*` at the repo root).

Common include patterns for native/runtime assets:

```js filename="next.config.js"
module.exports = {
  outputFileTracingIncludes: {
    '/*': ['node_modules/sharp/**/*', 'node_modules/aws-crt/dist/bin/**/*'],
  },
}
```


--------------------------------------------------------------------------------
title: "pageExtensions"
description: "Extend the default page extensions used by Next.js when resolving pages in the Pages Router."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions"
--------------------------------------------------------------------------------

# pageExtensions

@router: Pages Router

You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects *all* Next.js pages, including the following:

* [`proxy.js`](/docs/pages/api-reference/file-conventions/proxy.md)
* [`instrumentation.js`](/docs/pages/guides/instrumentation.md)
* `pages/_document.js`
* `pages/_app.js`
* `pages/api/`

For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.

## Including non-page files in the `pages` directory

You can colocate test files or other files used by components in the `pages` directory. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
}
```

Then, rename your pages to have a file extension that includes `.page` (e.g. rename `MyPage.tsx` to `MyPage.page.tsx`). Ensure you rename *all* Next.js pages, including the files mentioned above.


--------------------------------------------------------------------------------
title: "poweredByHeader"
description: "Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader"
--------------------------------------------------------------------------------

# poweredByHeader

@router: Pages Router

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```


--------------------------------------------------------------------------------
title: "productionBrowserSourceMaps"
description: "Enables browser source map generation during the production build."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps"
--------------------------------------------------------------------------------

# productionBrowserSourceMaps

@router: Pages Router

Source Maps are enabled by default during development. During production builds, they are disabled to prevent you leaking your source on the client, unless you specifically opt-in with the configuration flag.

Next.js provides a configuration flag you can use to enable browser source map generation during the production build:

```js filename="next.config.js"
module.exports = {
  productionBrowserSourceMaps: true,
}
```

When the `productionBrowserSourceMaps` option is enabled, the source maps will be output in the same directory as the JavaScript files. Next.js will automatically serve these files when requested.

* Adding source maps can increase `next build` time
* Increases memory usage during `next build`


--------------------------------------------------------------------------------
title: "proxyClientMaxBodySize"
description: "Configure the maximum request body size when using proxy."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize"
--------------------------------------------------------------------------------

# experimental.proxyClientMaxBodySize

@router: Pages Router

> This feature is currently experimental and subject to change, it is not recommended for production.

When proxy is used, Next.js automatically clones the request body and buffers it in memory to enable multiple reads - both in proxy and the underlying route handler. To prevent excessive memory usage, this configuration option sets a size limit on the buffered body.

By default, the maximum body size is **10MB**. If a request body exceeds this limit, the body will only be buffered up to the limit, and a warning will be logged indicating which route exceeded the limit.

## Options

### String format (recommended)

Specify the size using a human-readable string format:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    proxyClientMaxBodySize: '1mb',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    proxyClientMaxBodySize: '1mb',
  },
}

module.exports = nextConfig
```

Supported units: `b`, `kb`, `mb`, `gb`

### Number format

Alternatively, specify the size in bytes as a number:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    proxyClientMaxBodySize: 1048576, // 1MB in bytes
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    proxyClientMaxBodySize: 1048576, // 1MB in bytes
  },
}

module.exports = nextConfig
```

## Behavior

When a request body exceeds the configured limit:

1. Next.js will buffer only the first N bytes (up to the limit)
2. A warning will be logged to the console indicating the route that exceeded the limit
3. The request will continue processing normally, but only the partial body will be available
4. The request will **not** fail or return an error to the client

If your application needs to process the full request body, you should either:

* Increase the `proxyClientMaxBodySize` limit
* Handle the partial body gracefully in your application logic

## Example

```ts filename="proxy.ts"
import { NextRequest, NextResponse } from 'next/server'

export async function proxy(request: NextRequest) {
  // Next.js automatically buffers the body with the configured size limit
  // You can read the body in proxy...
  const body = await request.text()

  // If the body exceeded the limit, only partial data will be available
  console.log('Body size:', body.length)

  return NextResponse.next()
}
```

```ts filename="app/api/upload/route.ts"
import { NextRequest, NextResponse } from 'next/server'

export async function POST(request: NextRequest) {
  // ...and the body is still available in your route handler
  const body = await request.text()

  console.log('Body in route handler:', body.length)

  return NextResponse.json({ received: body.length })
}
```

## Good to know

* This setting only applies when proxy is used in your application
* The default limit of 10MB is designed to balance memory usage and typical use cases
* The limit applies per-request, not globally across all concurrent requests
* For applications handling large file uploads, consider increasing the limit accordingly


--------------------------------------------------------------------------------
title: "reactStrictMode"
description: "The complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode"
--------------------------------------------------------------------------------

# reactStrictMode

@router: Pages Router

> **Good to know**: Since Next.js 13.5.1, Strict Mode is `true` by default with `app` router, so the above configuration is only necessary for `pages`. You can still disable Strict Mode by setting `reactStrictMode: false`.

> **Suggested**: We strongly suggest you enable Strict Mode in your Next.js application to better prepare your application for the future of React.

React's [Strict Mode](https://react.dev/reference/react/StrictMode) is a development mode only feature for highlighting potential problems in an application. It helps to identify unsafe lifecycles, legacy API usage, and a number of other features.

The Next.js runtime is Strict Mode-compliant. To opt-in to Strict Mode, configure the following option in your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  reactStrictMode: true,
}
```

If you or your team are not ready to use Strict Mode in your entire application, that's OK! You can incrementally migrate on a page-by-page basis using `<React.StrictMode>`.


--------------------------------------------------------------------------------
title: "redirects"
description: "Add redirects to your Next.js app."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects"
--------------------------------------------------------------------------------

# redirects

@router: Pages Router

Redirects allow you to redirect an incoming request path to a different destination path.

To use redirects you can use the `redirects` key in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
    ]
  },
}
```

`redirects` is an async function that expects an array to be returned holding objects with `source`, `destination`, and `permanent` properties:

* `source` is the incoming request path pattern.
* `destination` is the path you want to route to.
* `permanent` `true` or `false` - if `true` will use the 308 status code which instructs clients/search engines to cache the redirect forever, if `false` will use the 307 status code which is temporary and is not cached.

> **Why does Next.js use 307 and 308?** Traditionally a 302 was used for a temporary redirect, and a 301 for a permanent redirect, but many browsers changed the request method of the redirect to `GET`, regardless of the original method. For example, if the browser made a request to `POST /v1/users` which returned status code `302` with location `/v2/users`, the subsequent request might be `GET /v2/users` instead of the expected `POST /v2/users`. Next.js uses the 307 temporary redirect, and 308 permanent redirect status codes to explicitly preserve the request method used.

* `basePath`: `false` or `undefined` - if false the `basePath` won't be included when matching, can be used for external redirects only.
* `locale`: `false` or `undefined` - whether the locale should not be included when matching.
* `has` is an array of [has objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
* `missing` is an array of [missing objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.

Redirects are checked before the filesystem which includes pages and `/public` files.

When using the Pages Router, redirects are not applied to client-side routing (`Link`, `router.push`) unless [Proxy](/docs/app/api-reference/file-conventions/proxy.md) is present and matches the path.

When a redirect is applied, any query values provided in the request will be passed through to the redirect destination. For example, see the following redirect configuration:

```js
{
  source: '/old-blog/:path*',
  destination: '/blog/:path*',
  permanent: false
}
```

> **Good to know**: Remember to include the forward slash `/` before the colon `:` in path parameters of the `source` and `destination` paths, otherwise the path will be treated as a literal string and you run the risk of causing infinite redirects.

When `/old-blog/post-1?hello=world` is requested, the client will be redirected to `/blog/post-1?hello=world`.

## Path Matching

Path matches are allowed, for example `/old-blog/:slug` will match `/old-blog/first-post` (no nested paths):

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        source: '/old-blog/:slug',
        destination: '/news/:slug', // Matched parameters can be used in the destination
        permanent: true,
      },
    ]
  },
}
```

The pattern `/old-blog/:slug` matches `/old-blog/first-post` and `/old-blog/post-1` but not `/old-blog/a/b` (no nested paths). Patterns are anchored to the start: `/old-blog/:slug` will not match `/archive/old-blog/first-post`.

You can use modifiers on parameters: `*` (zero or more), `+` (one or more), `?` (zero or one). For example, `/blog/:slug*` matches `/blog`, `/blog/a`, and `/blog/a/b/c`.

Read more details on [path-to-regexp](https://github.com/pillarjs/path-to-regexp) documentation.

### Wildcard Path Matching

To match a wildcard path you can use `*` after a parameter, for example `/blog/:slug*` will match `/blog/a/b/c/d/hello-world`:

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        source: '/blog/:slug*',
        destination: '/news/:slug*', // Matched parameters can be used in the destination
        permanent: true,
      },
    ]
  },
}
```

### Regex Path Matching

To match a regex path you can wrap the regex in parentheses after a parameter, for example `/post/:slug(\\d{1,})` will match `/post/123` but not `/post/abc`:

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        source: '/post/:slug(\\d{1,})',
        destination: '/news/:slug', // Matched parameters can be used in the destination
        permanent: false,
      },
    ]
  },
}
```

The following characters `(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` are used for regex path matching, so when used in the `source` as non-special values they must be escaped by adding `\\` before them:

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        // this will match `/english(default)/something` being requested
        source: '/english\\(default\\)/:slug',
        destination: '/en-us/:slug',
        permanent: false,
      },
    ]
  },
}
```

## Header, Cookie, and Query Matching

To only match a redirect when header, cookie, or query values also match the `has` field or don't match the `missing` field can be used. Both the `source` and all `has` items must match and all `missing` items must not match for the redirect to be applied.

`has` and `missing` items can have the following fields:

* `type`: `String` - must be either `header`, `cookie`, `host`, or `query`.
* `key`: `String` - the key from the selected type to match against.
* `value`: `String` or `undefined` - the value to check for, if undefined any value will match. A regex like string can be used to capture a specific part of the value, e.g. if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`.

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      // if the header `x-redirect-me` is present,
      // this redirect will be applied
      {
        source: '/:path((?!another-page$).*)',
        has: [
          {
            type: 'header',
            key: 'x-redirect-me',
          },
        ],
        permanent: false,
        destination: '/another-page',
      },
      // if the header `x-dont-redirect` is present,
      // this redirect will NOT be applied
      {
        source: '/:path((?!another-page$).*)',
        missing: [
          {
            type: 'header',
            key: 'x-do-not-redirect',
          },
        ],
        permanent: false,
        destination: '/another-page',
      },
      // if the source, query, and cookie are matched,
      // this redirect will be applied
      {
        source: '/specific/:path*',
        has: [
          {
            type: 'query',
            key: 'page',
            // the page value will not be available in the
            // destination since value is provided and doesn't
            // use a named capture group e.g. (?<page>home)
            value: 'home',
          },
          {
            type: 'cookie',
            key: 'authorized',
            value: 'true',
          },
        ],
        permanent: false,
        destination: '/another/:path*',
      },
      // if the header `x-authorized` is present and
      // contains a matching value, this redirect will be applied
      {
        source: '/',
        has: [
          {
            type: 'header',
            key: 'x-authorized',
            value: '(?<authorized>yes|true)',
          },
        ],
        permanent: false,
        destination: '/home?authorized=:authorized',
      },
      // if the host is `example.com`,
      // this redirect will be applied
      {
        source: '/:path((?!another-page$).*)',
        has: [
          {
            type: 'host',
            value: 'example.com',
          },
        ],
        permanent: false,
        destination: '/another-page',
      },
    ]
  },
}
```

### Redirects with basePath support

When leveraging [`basePath` support](/docs/app/api-reference/config/next-config-js/basePath.md) with redirects each `source` and `destination` is automatically prefixed with the `basePath` unless you add `basePath: false` to the redirect:

```js filename="next.config.js"
module.exports = {
  basePath: '/docs',

  async redirects() {
    return [
      {
        source: '/with-basePath', // automatically becomes /docs/with-basePath
        destination: '/another', // automatically becomes /docs/another
        permanent: false,
      },
      {
        // does not add /docs since basePath: false is set
        source: '/without-basePath',
        destination: 'https://example.com',
        basePath: false,
        permanent: false,
      },
    ]
  },
}
```

### Redirects with i18n support

When leveraging [`i18n` support](/docs/pages/guides/internationalization.md) with redirects each `source` and `destination` is automatically prefixed to handle the configured `locales` unless you add `locale: false` to the redirect. If `locale: false` is used you must prefix the `source` and `destination` with a locale for it to be matched correctly.

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['en', 'fr', 'de'],
    defaultLocale: 'en',
  },

  async redirects() {
    return [
      {
        source: '/with-locale', // automatically handles all locales
        destination: '/another', // automatically passes the locale on
        permanent: false,
      },
      {
        // does not handle locales automatically since locale: false is set
        source: '/nl/with-locale-manual',
        destination: '/nl/another',
        locale: false,
        permanent: false,
      },
      {
        // this matches '/' since `en` is the defaultLocale
        source: '/en',
        destination: '/en/another',
        locale: false,
        permanent: false,
      },
      // it's possible to match all locales even when locale: false is set
      {
        source: '/:locale/page',
        destination: '/en/newpage',
        permanent: false,
        locale: false,
      },
      {
        // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
        // `/` or `/fr` routes like /:path* would
        source: '/(.*)',
        destination: '/another',
        permanent: false,
      },
    ]
  },
}
```

In some rare cases, you might need to assign a custom status code for older HTTP Clients to properly redirect. In these cases, you can use the `statusCode` property instead of the `permanent` property, but not both. To ensure IE11 compatibility, a `Refresh` header is automatically added for the 308 status code.

## Other Redirects

* Inside [API Routes](/docs/pages/building-your-application/routing/api-routes.md) and [Route Handlers](/docs/app/api-reference/file-conventions/route.md), you can redirect based on the incoming request.
* Inside [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) and [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md), you can redirect specific pages at request-time.

## Version History

| Version   | Changes            |
| --------- | ------------------ |
| `v13.3.0` | `missing` added.   |
| `v10.2.0` | `has` added.       |
| `v9.5.0`  | `redirects` added. |


--------------------------------------------------------------------------------
title: "rewrites"
description: "Add rewrites to your Next.js app."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites"
--------------------------------------------------------------------------------

# rewrites

@router: Pages Router

Rewrites allow you to map an incoming request path to a different destination path.

Rewrites act as a URL proxy and mask the destination path, making it appear the user hasn't changed their location on the site. In contrast, [redirects](/docs/pages/api-reference/config/next-config-js/redirects.md) will reroute to a new page and show the URL changes.

To use rewrites you can use the `rewrites` key in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/about',
        destination: '/',
      },
    ]
  },
}
```

Rewrites are applied to client-side routing. In the example above, navigating to `<Link href="/about">` will serve content from `/` while keeping the URL as `/about`.

`rewrites` is an async function that expects to return either an array or an object of arrays (see below) holding objects with `source` and `destination` properties:

* `source`: `String` - is the incoming request path pattern.
* `destination`: `String` is the path you want to route to.
* `basePath`: `false` or `undefined` - if false the basePath won't be included when matching, can be used for external rewrites only.
* `locale`: `false` or `undefined` - whether the locale should not be included when matching.
* `has` is an array of [has objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
* `missing` is an array of [missing objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.

When the `rewrites` function returns an array, rewrites are applied after checking the filesystem (pages and `/public` files) and before dynamic routes. When the `rewrites` function returns an object of arrays with a specific shape, this behavior can be changed and more finely controlled, as of `v10.1` of Next.js:

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return {
      beforeFiles: [
        // These rewrites are checked after headers/redirects
        // and before all files including _next/public files which
        // allows overriding page files
        {
          source: '/some-page',
          destination: '/somewhere-else',
          has: [{ type: 'query', key: 'overrideMe' }],
        },
      ],
      afterFiles: [
        // These rewrites are checked after pages/public files
        // are checked but before dynamic routes
        {
          source: '/non-existent',
          destination: '/somewhere-else',
        },
      ],
      fallback: [
        // These rewrites are checked after both pages/public files
        // and dynamic routes are checked
        {
          source: '/:path*',
          destination: `https://my-old-site.com/:path*`,
        },
      ],
    }
  },
}
```

> **Good to know**: rewrites in `beforeFiles` do not check the filesystem/dynamic routes immediately after matching a source, they continue until all `beforeFiles` have been checked.

The order Next.js routes are checked is:

1. [headers](/docs/pages/api-reference/config/next-config-js/headers.md) are checked/applied
2. [redirects](/docs/pages/api-reference/config/next-config-js/redirects.md) are checked/applied
3. `beforeFiles` rewrites are checked/applied
4. static files from the [public directory](/docs/pages/api-reference/file-conventions/public-folder.md), `_next/static` files, and non-dynamic pages are checked/served
5. `afterFiles` rewrites are checked/applied, if one of these rewrites is matched we check dynamic routes/static files after each match
6. `fallback` rewrites are checked/applied, these are applied before rendering the 404 page and after dynamic routes/all static assets have been checked. If you use [fallback: true/'blocking'](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true) in `getStaticPaths`, the fallback `rewrites` defined in your `next.config.js` will *not* be run.

## Rewrite parameters

When using parameters in a rewrite the parameters will be passed in the query by default when none of the parameters are used in the `destination`.

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/old-about/:path*',
        destination: '/about', // The :path parameter isn't used here so will be automatically passed in the query
      },
    ]
  },
}
```

If a parameter is used in the destination none of the parameters will be automatically passed in the query.

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/docs/:path*',
        destination: '/:path*', // The :path parameter is used here so will not be automatically passed in the query
      },
    ]
  },
}
```

You can still pass the parameters manually in the query if one is already used in the destination by specifying the query in the `destination`.

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/:first/:second',
        destination: '/:first?second=:second',
        // Since the :first parameter is used in the destination the :second parameter
        // will not automatically be added in the query although we can manually add it
        // as shown above
      },
    ]
  },
}
```

> **Good to know**: Static pages from [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md) or [prerendering](/docs/pages/building-your-application/data-fetching/get-static-props.md) params from rewrites will be parsed on the client after hydration and provided in the query.

## Path Matching

Path matches are allowed, for example `/blog/:slug` will match `/blog/first-post` (no nested paths):

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/blog/:slug',
        destination: '/news/:slug', // Matched parameters can be used in the destination
      },
    ]
  },
}
```

The pattern `/blog/:slug` matches `/blog/first-post` and `/blog/post-1` but not `/blog/a/b` (no nested paths). Patterns are anchored to the start: `/blog/:slug` will not match `/archive/blog/first-post`.

You can use modifiers on parameters: `*` (zero or more), `+` (one or more), `?` (zero or one). For example, `/blog/:slug*` matches `/blog`, `/blog/a`, and `/blog/a/b/c`.

Read more details on [path-to-regexp](https://github.com/pillarjs/path-to-regexp) documentation.

### Wildcard Path Matching

To match a wildcard path you can use `*` after a parameter, for example `/blog/:slug*` will match `/blog/a/b/c/d/hello-world`:

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/blog/:slug*',
        destination: '/news/:slug*', // Matched parameters can be used in the destination
      },
    ]
  },
}
```

### Regex Path Matching

To match a regex path you can wrap the regex in parenthesis after a parameter, for example `/blog/:slug(\\d{1,})` will match `/blog/123` but not `/blog/abc`:

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/old-blog/:post(\\d{1,})',
        destination: '/blog/:post', // Matched parameters can be used in the destination
      },
    ]
  },
}
```

The following characters `(`, `)`, `{`, `}`, `[`, `]`, `|`, `\`, `^`, `.`, `:`, `*`, `+`, `-`, `?`, `$` are used for regex path matching, so when used in the `source` as non-special values they must be escaped by adding `\\` before them:

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        // this will match `/english(default)/something` being requested
        source: '/english\\(default\\)/:slug',
        destination: '/en-us/:slug',
      },
    ]
  },
}
```

## Header, Cookie, and Query Matching

To only match a rewrite when header, cookie, or query values also match the `has` field or don't match the `missing` field can be used. Both the `source` and all `has` items must match and all `missing` items must not match for the rewrite to be applied.

`has` and `missing` items can have the following fields:

* `type`: `String` - must be either `header`, `cookie`, `host`, or `query`.
* `key`: `String` - the key from the selected type to match against.
* `value`: `String` or `undefined` - the value to check for, if undefined any value will match. A regex like string can be used to capture a specific part of the value, e.g. if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`.

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      // if the header `x-rewrite-me` is present,
      // this rewrite will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'header',
            key: 'x-rewrite-me',
          },
        ],
        destination: '/another-page',
      },
      // if the header `x-rewrite-me` is not present,
      // this rewrite will be applied
      {
        source: '/:path*',
        missing: [
          {
            type: 'header',
            key: 'x-rewrite-me',
          },
        ],
        destination: '/another-page',
      },
      // if the source, query, and cookie are matched,
      // this rewrite will be applied
      {
        source: '/specific/:path*',
        has: [
          {
            type: 'query',
            key: 'page',
            // the page value will not be available in the
            // destination since value is provided and doesn't
            // use a named capture group e.g. (?<page>home)
            value: 'home',
          },
          {
            type: 'cookie',
            key: 'authorized',
            value: 'true',
          },
        ],
        destination: '/:path*/home',
      },
      // if the header `x-authorized` is present and
      // contains a matching value, this rewrite will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'header',
            key: 'x-authorized',
            value: '(?<authorized>yes|true)',
          },
        ],
        destination: '/home?authorized=:authorized',
      },
      // if the host is `example.com`,
      // this rewrite will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'host',
            value: 'example.com',
          },
        ],
        destination: '/another-page',
      },
    ]
  },
}
```

## Rewriting to an external URL

<details>
<summary>Examples</summary>

* [Using Multiple Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)

</details>

Rewrites allow you to rewrite to an external URL. This is especially useful for incrementally adopting Next.js. The following is an example rewrite for redirecting the `/blog` route of your main app to an external site.

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return [
      {
        source: '/blog',
        destination: 'https://example.com/blog',
      },
      {
        source: '/blog/:slug',
        destination: 'https://example.com/blog/:slug', // Matched parameters can be used in the destination
      },
    ]
  },
}
```

If you're using `trailingSlash: true`, you also need to insert a trailing slash in the `source` parameter. If the destination server is also expecting a trailing slash it should be included in the `destination` parameter as well.

```js filename="next.config.js"
module.exports = {
  trailingSlash: true,
  async rewrites() {
    return [
      {
        source: '/blog/',
        destination: 'https://example.com/blog/',
      },
      {
        source: '/blog/:path*/',
        destination: 'https://example.com/blog/:path*/',
      },
    ]
  },
}
```

### Incremental adoption of Next.js

You can also have Next.js fall back to proxying to an existing website after checking all Next.js routes.

This way you don't have to change the rewrites configuration when migrating more pages to Next.js

```js filename="next.config.js"
module.exports = {
  async rewrites() {
    return {
      fallback: [
        {
          source: '/:path*',
          destination: `https://custom-routes-proxying-endpoint.vercel.app/:path*`,
        },
      ],
    }
  },
}
```

### Rewrites with basePath support

When leveraging [`basePath` support](/docs/app/api-reference/config/next-config-js/basePath.md) with rewrites each `source` and `destination` is automatically prefixed with the `basePath` unless you add `basePath: false` to the rewrite:

```js filename="next.config.js"
module.exports = {
  basePath: '/docs',

  async rewrites() {
    return [
      {
        source: '/with-basePath', // automatically becomes /docs/with-basePath
        destination: '/another', // automatically becomes /docs/another
      },
      {
        // does not add /docs to /without-basePath since basePath: false is set
        // Note: this can not be used for internal rewrites e.g. `destination: '/another'`
        source: '/without-basePath',
        destination: 'https://example.com',
        basePath: false,
      },
    ]
  },
}
```

### Rewrites with i18n support

When leveraging [`i18n` support](/docs/pages/guides/internationalization.md) with rewrites each `source` and `destination` is automatically prefixed to handle the configured `locales` unless you add `locale: false` to the rewrite. If `locale: false` is used you must prefix the `source` and `destination` with a locale for it to be matched correctly.

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['en', 'fr', 'de'],
    defaultLocale: 'en',
  },

  async rewrites() {
    return [
      {
        source: '/with-locale', // automatically handles all locales
        destination: '/another', // automatically passes the locale on
      },
      {
        // does not handle locales automatically since locale: false is set
        source: '/nl/with-locale-manual',
        destination: '/nl/another',
        locale: false,
      },
      {
        // this matches '/' since `en` is the defaultLocale
        source: '/en',
        destination: '/en/another',
        locale: false,
      },
      {
        // it's possible to match all locales even when locale: false is set
        source: '/:locale/api-alias/:path*',
        destination: '/api/:path*',
        locale: false,
      },
      {
        // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
        // `/` or `/fr` routes like /:path* would
        source: '/(.*)',
        destination: '/another',
      },
    ]
  },
}
```

## Version History

| Version   | Changes          |
| --------- | ---------------- |
| `v13.3.0` | `missing` added. |
| `v10.2.0` | `has` added.     |
| `v9.5.0`  | Headers added.   |


--------------------------------------------------------------------------------
title: "serverExternalPackages"
description: "Opt-out specific dependencies from the dependency bundling enabled by `bundlePagesRouterDependencies`."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages"
--------------------------------------------------------------------------------

# serverExternalPackages

@router: Pages Router

Opt-out specific dependencies from being included in the automatic bundling of the [`bundlePagesRouterDependencies`](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies.md) option.

These pages will then use native Node.js `require` to resolve the dependency.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['@acme/ui'],
}

module.exports = nextConfig
```

Next.js includes a [short list of popular packages](https://github.com/vercel/next.js/blob/canary/packages/next/src/lib/server-external-packages.json) that currently are working on compatibility and automatically opt-ed out:

* `@appsignal/nodejs`
* `@aws-sdk/client-s3`
* `@aws-sdk/s3-presigned-post`
* `@blockfrost/blockfrost-js`
* `@highlight-run/node`
* `@huggingface/transformers`
* `@jpg-store/lucid-cardano`
* `@libsql/client`
* `@mikro-orm/core`
* `@mikro-orm/knex`
* `@node-rs/argon2`
* `@node-rs/bcrypt`
* `@prisma/client`
* `@react-pdf/renderer`
* `@sentry/profiling-node`
* `@sparticuz/chromium`
* `@sparticuz/chromium-min`
* `@statsig/statsig-node-core`
* `@swc/core`
* `@xenova/transformers`
* `argon2`
* `autoprefixer`
* `aws-crt`
* `bcrypt`
* `better-sqlite3`
* `canvas`
* `chromadb-default-embed`
* `config`
* `cpu-features`
* `cypress`
* `dd-trace`
* `eslint`
* `express`
* `firebase-admin`
* `htmlrewriter`
* `import-in-the-middle`
* `isolated-vm`
* `jest`
* `jsdom`
* `keyv`
* `libsql`
* `mdx-bundler`
* `mongodb`
* `mongoose`
* `newrelic`
* `next-mdx-remote`
* `next-seo`
* `node-cron`
* `node-pty`
* `node-web-audio-api`
* `onnxruntime-node`
* `oslo`
* `pg`
* `playwright`
* `playwright-core`
* `postcss`
* `prettier`
* `prisma`
* `puppeteer-core`
* `puppeteer`
* `ravendb`
* `require-in-the-middle`
* `rimraf`
* `sharp`
* `shiki`
* `sqlite3`
* `ts-node`
* `ts-morph`
* `typescript`
* `vscode-oniguruma`
* `webpack`
* `websocket`
* `zeromq`


--------------------------------------------------------------------------------
title: "trailingSlash"
description: "Configure Next.js pages to resolve with or without a trailing slash."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash"
--------------------------------------------------------------------------------

# trailingSlash

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages"
--------------------------------------------------------------------------------

# transpilePackages

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbopack"
--------------------------------------------------------------------------------

# turbopack

@router: Pages Router

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
title: "typescript"
description: "Next.js reports TypeScript errors by default. Learn to opt-out of this behavior here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript"
--------------------------------------------------------------------------------

# typescript

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports"
--------------------------------------------------------------------------------

# urlImports

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss"
--------------------------------------------------------------------------------

# useLightningcss

@router: Pages Router

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
title: "Custom Webpack Config"
description: "Learn how to customize the webpack config used by Next.js"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack"
--------------------------------------------------------------------------------

# webpack

@router: Pages Router

> **Good to know**: changes to webpack config are not covered by semver so proceed at your own risk

Before continuing to add custom webpack configuration to your application make sure Next.js doesn't already support your use-case:

* [CSS imports](/docs/app/getting-started/css.md)
* [CSS modules](/docs/app/getting-started/css.md)
* [Sass/SCSS imports](/docs/pages/guides/sass.md)
* [Sass/SCSS modules](/docs/pages/guides/sass.md)
* [Customizing babel configuration](/docs/pages/guides/babel.md)

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
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution"
--------------------------------------------------------------------------------

# webVitalsAttribution

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/config/typescript"
--------------------------------------------------------------------------------

# TypeScript

@router: Pages Router

Next.js comes with built-in TypeScript, automatically installing the necessary packages and configuring the proper settings when you create a new project with `create-next-app`.

To add TypeScript to an existing project, rename a file to `.ts` / `.tsx`. Run `next dev` and `next build` to automatically install the necessary dependencies and add a `tsconfig.json` file with the recommended config options.

> **Good to know**: If you already have a `jsconfig.json` file, copy the `paths` compiler option from the old `jsconfig.json` into the new `tsconfig.json` file, and delete the old `jsconfig.json` file.

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

### Static Generation and Server-side Rendering

For [`getStaticProps`](/docs/pages/api-reference/functions/get-static-props.md), [`getStaticPaths`](/docs/pages/api-reference/functions/get-static-paths.md), and [`getServerSideProps`](/docs/pages/api-reference/functions/get-server-side-props.md), you can use the `GetStaticProps`, `GetStaticPaths`, and `GetServerSideProps` types respectively:

```tsx filename="pages/blog/[slug].tsx"
import type { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

export const getStaticProps = (async (context) => {
  // ...
}) satisfies GetStaticProps

export const getStaticPaths = (async () => {
  // ...
}) satisfies GetStaticPaths

export const getServerSideProps = (async (context) => {
  // ...
}) satisfies GetServerSideProps
```

> **Good to know:** `satisfies` was added to TypeScript in [4.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html). We recommend upgrading to the latest version of TypeScript.

### With API Routes

The following is an example of how to use the built-in types for API routes:

```ts filename="pages/api/hello.ts"
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ name: 'John Doe' })
}
```

You can also type the response data:

```ts filename="pages/api/hello.ts"
import type { NextApiRequest, NextApiResponse } from 'next'

type Data = {
  name: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: 'John Doe' })
}
```

### With custom `App`

If you have a [custom `App`](/docs/pages/building-your-application/routing/custom-app.md), you can use the built-in type `AppProps` and change file name to `./pages/_app.tsx` like so:

```ts
import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

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
source: "https://nextjs.org/docs/pages/api-reference/config/eslint"
--------------------------------------------------------------------------------

# ESLint

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/cli"
--------------------------------------------------------------------------------

# CLI

@router: Pages Router

Next.js comes with **two** Command Line Interface (CLI) tools:

* **`create-next-app`**: Quickly create a new Next.js application using the default template or an [example](https://github.com/vercel/next.js/tree/canary/examples) from a public GitHub repository.
* **`next`**: Run the Next.js development server, build your application, and more.

 - [create-next-app CLI](/docs/pages/api-reference/cli/create-next-app.md)
 - [next CLI](/docs/pages/api-reference/cli/next.md)

--------------------------------------------------------------------------------
title: "create-next-app"
description: "Create Next.js apps using one command with the create-next-app CLI."
source: "https://nextjs.org/docs/pages/api-reference/cli/create-next-app"
--------------------------------------------------------------------------------

# create-next-app CLI

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/cli/next"
--------------------------------------------------------------------------------

# next CLI

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/edge"
--------------------------------------------------------------------------------

# Edge Runtime

@router: Pages Router

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
source: "https://nextjs.org/docs/pages/api-reference/turbopack"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./16-instrumentationjs.md) | [Index](./index.md) | [Next →](./18-turbopack.md)
