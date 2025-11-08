**Navigation:** [← Previous](./15-getstaticprops.md) | [Index](./index.md) | [Next →](./17-images.md)

---

# instrumentation.js

@router: Pages Router

The `instrumentation.js|ts` file is used to integrate observability tools into your application, allowing you to track the performance and behavior, and to debug issues in production.

To use it, place the file in the **root** of your application or inside a [`src` folder](/docs/app/api-reference/file-conventions/src-folder.md) if using one.

## Exports

### `register` (optional)

The file exports a `register` function that is called **once** when a new Next.js server instance is initiated. `register` can be an async function.

```ts filename="instrumentation.ts" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel('next-app')
}
```

```js filename="instrumentation.js" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel('next-app')
}
```

### `onRequestError` (optional)

You can optionally export an `onRequestError` function to track **server** errors to any custom observability provider.

* If you're running any async tasks in `onRequestError`, make sure they're awaited. `onRequestError` will be triggered when the Next.js server captures the error.
* The `error` instance might not be the original error instance thrown, as it may be processed by React if encountered during Server Components rendering. If this happens, you can use `digest` property on an error to identify the actual error type.

```ts filename="instrumentation.ts" switcher
import { type Instrumentation } from 'next'

export const onRequestError: Instrumentation.onRequestError = async (
  err,
  request,
  context
) => {
  await fetch('https://.../report-error', {
    method: 'POST',
    body: JSON.stringify({
      message: err.message,
      request,
      context,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
}
```

```js filename="instrumentation.js" switcher
export async function onRequestError(err, request, context) {
  await fetch('https://.../report-error', {
    method: 'POST',
    body: JSON.stringify({
      message: err.message,
      request,
      context,
    }),
    headers: {
      'Content-Type': 'application/json',
    },
  })
}
```

#### Parameters

The function accepts three parameters: `error`, `request`, and `context`.

```ts filename="Types"
export function onRequestError(
  error: { digest: string } & Error,
  request: {
    path: string // resource path, e.g. /blog?name=foo
    method: string // request method. e.g. GET, POST, etc
    headers: { [key: string]: string | string[] }
  },
  context: {
    routerKind: 'Pages Router' | 'App Router' // the router type
    routePath: string // the route file path, e.g. /app/blog/[dynamic]
    routeType: 'render' | 'route' | 'action' | 'proxy' // the context in which the error occurred
    renderSource:
      | 'react-server-components'
      | 'react-server-components-payload'
      | 'server-rendering'
    revalidateReason: 'on-demand' | 'stale' | undefined // undefined is a normal request without revalidation
    renderType: 'dynamic' | 'dynamic-resume' // 'dynamic-resume' for PPR
  }
): void | Promise<void>
```

* `error`: The caught error itself (type is always `Error`), and a `digest` property which is the unique ID of the error.
* `request`: Read-only request information associated with the error.
* `context`: The context in which the error occurred. This can be the type of router (App or Pages Router), and/or (Server Components (`'render'`), Route Handlers (`'route'`), Server Actions (`'action'`), or Proxy (`'proxy'`)).

### Specifying the runtime

The `instrumentation.js` file works in both the Node.js and Edge runtime, however, you can use `process.env.NEXT_RUNTIME` to target a specific runtime.

```js filename="instrumentation.js"
export function register() {
  if (process.env.NEXT_RUNTIME === 'edge') {
    return require('./register.edge')
  } else {
    return require('./register.node')
  }
}

export function onRequestError() {
  if (process.env.NEXT_RUNTIME === 'edge') {
    return require('./on-request-error.edge')
  } else {
    return require('./on-request-error.node')
  }
}
```

## Version History

| Version   | Changes                                                 |
| --------- | ------------------------------------------------------- |
| `v15.0.0` | `onRequestError` introduced, `instrumentation` stable   |
| `v14.0.4` | Turbopack support for `instrumentation`                 |
| `v13.2.0` | `instrumentation` introduced as an experimental feature |
## Learn more about Instrumentation- [Instrumentation](/docs/app/guides/instrumentation.md)
  - Learn how to use instrumentation to run code at server startup in your Next.js app


--------------------------------------------------------------------------------
title: "proxy.js"
description: "API reference for the proxy.js file."
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/proxy"
--------------------------------------------------------------------------------

# Proxy

@router: Pages Router

> **Note**: The `middleware` file convention is deprecated and has been renamed to `proxy`. See [Migration to Proxy](#migration-to-proxy) for more details.

The `proxy.js|ts` file is used to write [Proxy](/docs/app/getting-started/proxy.md) and run code on the server before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.

Proxy executes before routes are rendered. It's particularly useful for implementing custom server-side logic like authentication, logging, or handling redirects.

> **Good to know**:
>
> Proxy is meant to be invoked separately of your render code and in optimized cases deployed to your CDN for fast redirect/rewrite handling, you should not attempt relying on shared modules or globals.
>
> To pass information from Proxy to your application, use [headers](#setting-headers), [cookies](#using-cookies), [rewrites](/docs/app/api-reference/functions/next-response.md#rewrite), [redirects](/docs/app/api-reference/functions/next-response.md#redirect), or the URL.

Create a `proxy.ts` (or `.js`) file in the project root, or inside `src` if applicable, so that it is located at the same level as `pages` or `app`.

If you’ve customized [`pageExtensions`](/docs/app/api-reference/config/next-config-js/pageExtensions.md), for example to `.page.ts` or `.page.js`, name your file `proxy.page.ts` or `proxy.page.js` accordingly.

```tsx filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}

export const config = {
  matcher: '/about/:path*',
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request) {
  return NextResponse.redirect(new URL('/home', request.url))
}

export const config = {
  matcher: '/about/:path*',
}
```

## Exports

### Proxy function

The file must export a single function, either as a default export or named `proxy`. Note that multiple proxy from the same file are not supported.

```js filename="proxy.js"
// Example of default export
export default function proxy(request) {
  // Proxy logic
}
```

### Config object (optional)

Optionally, a config object can be exported alongside the Proxy function. This object includes the [matcher](#matcher) to specify paths where the Proxy applies.

### Matcher

The `matcher` option allows you to target specific paths for the Proxy to run on. You can specify these paths in several ways:

* For a single path: Directly use a string to define the path, like `'/about'`.
* For multiple paths: Use an array to list multiple paths, such as `matcher: ['/about', '/contact']`, which applies the Proxy to both `/about` and `/contact`.

```js filename="proxy.js"
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
}
```

Additionally, the `matcher` option supports complex path specifications using regular expressions. For example, you can exclude certain paths with a regular expression matcher:

```js filename="proxy.js"
export const config = {
  matcher: [
    // Exclude API routes, static files, image optimizations, and .png files
    '/((?!api|_next/static|_next/image|.*\\.png$).*)',
  ],
}
```

This enables precise control over which paths to include or exclude.

The `matcher` option accepts an array of objects with the following keys:

* `source`: The path or pattern used to match the request paths. It can be a string for direct path matching or a pattern for more complex matching.
* `locale` (optional): A boolean that, when set to `false`, ignores locale-based routing in path matching.
* `has` (optional): Specifies conditions based on the presence of specific request elements such as headers, query parameters, or cookies.
* `missing` (optional): Focuses on conditions where certain request elements are absent, like missing headers or cookies.

```js filename="proxy.js"
export const config = {
  matcher: [
    {
      source: '/api/:path*',
      locale: false,
      has: [
        { type: 'header', key: 'Authorization', value: 'Bearer Token' },
        { type: 'query', key: 'userId', value: '123' },
      ],
      missing: [{ type: 'cookie', key: 'session', value: 'active' }],
    },
  ],
}
```

Configured matchers:

1. MUST start with `/`
2. Can include named parameters: `/about/:path` matches `/about/a` and `/about/b` but not `/about/a/c`
3. Can have modifiers on named parameters (starting with `:`): `/about/:path*` matches `/about/a/b/c` because `*` is *zero or more*. `?` is *zero or one* and `+` *one or more*
4. Can use regular expression enclosed in parenthesis: `/about/(.*)` is the same as `/about/:path*`
5. Are anchored to the start of the path: `/about` matches `/about` and `/about/team` but not `/blog/about`

Read more details on [path-to-regexp](https://github.com/pillarjs/path-to-regexp#path-to-regexp-1) documentation.

> **Good to know**:
>
> * The `matcher` values need to be constants so they can be statically analyzed at build-time. Dynamic values such as variables will be ignored.
> * For backward compatibility, Next.js always considers `/public` as `/public/index`. Therefore, a matcher of `/public/:path` will match.

## Params

### `request`

When defining Proxy, the default export function accepts a single parameter, `request`. This parameter is an instance of `NextRequest`, which represents the incoming HTTP request.

```tsx filename="proxy.ts" switcher
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  // Proxy logic goes here
}
```

```js filename="proxy.js" switcher
export function proxy(request) {
  // Proxy logic goes here
}
```

> **Good to know**:
>
> * `NextRequest` is a type that represents incoming HTTP requests in Next.js Proxy, whereas [`NextResponse`](#nextresponse) is a class used to manipulate and send back HTTP responses.

## NextResponse

The `NextResponse` API allows you to:

* `redirect` the incoming request to a different URL
* `rewrite` the response by displaying a given URL
* Set request headers for API Routes, `getServerSideProps`, and `rewrite` destinations
* Set response cookies
* Set response headers

To produce a response from Proxy, you can:

1. `rewrite` to a route ([Page](/docs/pages/building-your-application/routing/pages-and-layouts.md) or [Edge API Route](/docs/pages/building-your-application/routing/api-routes.md)) that produces a response
2. return a `NextResponse` directly. See [Producing a Response](#producing-a-response)

## Execution order

Proxy will be invoked for **every route in your project**. Given this, it's crucial to use [matchers](#matcher) to precisely target or exclude specific routes. The following is the execution order:

1. `headers` from `next.config.js`
2. `redirects` from `next.config.js`
3. Proxy (`rewrites`, `redirects`, etc.)
4. `beforeFiles` (`rewrites`) from `next.config.js`
5. Filesystem routes (`public/`, `_next/static/`, `pages/`, `app/`, etc.)
6. `afterFiles` (`rewrites`) from `next.config.js`
7. Dynamic Routes (`/blog/[slug]`)
8. `fallback` (`rewrites`) from `next.config.js`

## Runtime

Proxy defaults to using the Node.js runtime. The [`runtime`](/docs/app/api-reference/file-conventions/route-segment-config.md#runtime) config option is not available in Proxy files. Setting the `runtime` config option in Proxy will throw an error.

## Advanced Proxy flags

In `v13.1` of Next.js two additional flags were introduced for proxy, `skipMiddlewareUrlNormalize` and `skipTrailingSlashRedirect` to handle advanced use cases.

`skipTrailingSlashRedirect` disables Next.js redirects for adding or removing trailing slashes. This allows custom handling inside proxy to maintain the trailing slash for some paths but not others, which can make incremental migrations easier.

```js filename="next.config.js"
module.exports = {
  skipTrailingSlashRedirect: true,
}
```

```js filename="proxy.js"
const legacyPrefixes = ['/docs', '/blog']

export default async function proxy(req) {
  const { pathname } = req.nextUrl

  if (legacyPrefixes.some((prefix) => pathname.startsWith(prefix))) {
    return NextResponse.next()
  }

  // apply trailing slash handling
  if (
    !pathname.endsWith('/') &&
    !pathname.match(/((?!\.well-known(?:\/.*)?)(?:[^/]+\/)*[^/]+\.\w+)/)
  ) {
    return NextResponse.redirect(
      new URL(`${req.nextUrl.pathname}/`, req.nextUrl)
    )
  }
}
```

`skipMiddlewareUrlNormalize` allows for disabling the URL normalization in Next.js to make handling direct visits and client-transitions the same. In some advanced cases, this option provides full control by using the original URL.

```js filename="next.config.js"
module.exports = {
  skipMiddlewareUrlNormalize: true,
}
```

```js filename="proxy.js"
export default async function proxy(req) {
  const { pathname } = req.nextUrl

  // GET /_next/data/build-id/hello.json

  console.log(pathname)
  // with the flag this now /_next/data/build-id/hello.json
  // without the flag this would be normalized to /hello
}
```

## Examples

### Conditional Statements

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/about')) {
    return NextResponse.rewrite(new URL('/about-2', request.url))
  }

  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.rewrite(new URL('/dashboard/user', request.url))
  }
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  if (request.nextUrl.pathname.startsWith('/about')) {
    return NextResponse.rewrite(new URL('/about-2', request.url))
  }

  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.rewrite(new URL('/dashboard/user', request.url))
  }
}
```

### Using Cookies

Cookies are regular headers. On a `Request`, they are stored in the `Cookie` header. On a `Response` they are in the `Set-Cookie` header. Next.js provides a convenient way to access and manipulate these cookies through the `cookies` extension on `NextRequest` and `NextResponse`.

1. For incoming requests, `cookies` comes with the following methods: `get`, `getAll`, `set`, and `delete` cookies. You can check for the existence of a cookie with `has` or remove all cookies with `clear`.
2. For outgoing responses, `cookies` have the following methods `get`, `getAll`, `set`, and `delete`.

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  // Assume a "Cookie:nextjs=fast" header to be present on the incoming request
  // Getting cookies from the request using the `RequestCookies` API
  let cookie = request.cookies.get('nextjs')
  console.log(cookie) // => { name: 'nextjs', value: 'fast', Path: '/' }
  const allCookies = request.cookies.getAll()
  console.log(allCookies) // => [{ name: 'nextjs', value: 'fast' }]

  request.cookies.has('nextjs') // => true
  request.cookies.delete('nextjs')
  request.cookies.has('nextjs') // => false

  // Setting cookies on the response using the `ResponseCookies` API
  const response = NextResponse.next()
  response.cookies.set('vercel', 'fast')
  response.cookies.set({
    name: 'vercel',
    value: 'fast',
    path: '/',
  })
  cookie = response.cookies.get('vercel')
  console.log(cookie) // => { name: 'vercel', value: 'fast', Path: '/' }
  // The outgoing response will have a `Set-Cookie:vercel=fast;path=/` header.

  return response
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  // Assume a "Cookie:nextjs=fast" header to be present on the incoming request
  // Getting cookies from the request using the `RequestCookies` API
  let cookie = request.cookies.get('nextjs')
  console.log(cookie) // => { name: 'nextjs', value: 'fast', Path: '/' }
  const allCookies = request.cookies.getAll()
  console.log(allCookies) // => [{ name: 'nextjs', value: 'fast' }]

  request.cookies.has('nextjs') // => true
  request.cookies.delete('nextjs')
  request.cookies.has('nextjs') // => false

  // Setting cookies on the response using the `ResponseCookies` API
  const response = NextResponse.next()
  response.cookies.set('vercel', 'fast')
  response.cookies.set({
    name: 'vercel',
    value: 'fast',
    path: '/',
  })
  cookie = response.cookies.get('vercel')
  console.log(cookie) // => { name: 'vercel', value: 'fast', Path: '/' }
  // The outgoing response will have a `Set-Cookie:vercel=fast;path=/` header.

  return response
}
```

### Setting Headers

You can set request and response headers using the `NextResponse` API (setting *request* headers is available since Next.js v13.0.0).

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  // Clone the request headers and set a new header `x-hello-from-proxy1`
  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-hello-from-proxy1', 'hello')

  // You can also set request headers in NextResponse.next
  const response = NextResponse.next({
    request: {
      // New request headers
      headers: requestHeaders,
    },
  })

  // Set a new response header `x-hello-from-proxy2`
  response.headers.set('x-hello-from-proxy2', 'hello')
  return response
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  // Clone the request headers and set a new header `x-hello-from-proxy1`
  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-hello-from-proxy1', 'hello')

  // You can also set request headers in NextResponse.next
  const response = NextResponse.next({
    request: {
      // New request headers
      headers: requestHeaders,
    },
  })

  // Set a new response header `x-hello-from-proxy2`
  response.headers.set('x-hello-from-proxy2', 'hello')
  return response
}
```

Note that the snippet uses:

* `NextResponse.next({ request: { headers: requestHeaders } })` to make `requestHeaders` available upstream
* **NOT** `NextResponse.next({ headers: requestHeaders })` which makes `requestHeaders` available to clients

Learn more in [NextResponse headers in Proxy](/docs/app/api-reference/functions/next-response.md#next).

> **Good to know**: Avoid setting large headers as it might cause [431 Request Header Fields Too Large](https://developer.mozilla.org/docs/Web/HTTP/Status/431) error depending on your backend web server configuration.

### CORS

You can set CORS headers in Proxy to allow cross-origin requests, including [simple](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#simple_requests) and [preflighted](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#preflighted_requests) requests.

```tsx filename="proxy.ts" switcher
import { NextRequest, NextResponse } from 'next/server'

const allowedOrigins = ['https://acme.com', 'https://my-app.org']

const corsOptions = {
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
}

export function proxy(request: NextRequest) {
  // Check the origin from the request
  const origin = request.headers.get('origin') ?? ''
  const isAllowedOrigin = allowedOrigins.includes(origin)

  // Handle preflighted requests
  const isPreflight = request.method === 'OPTIONS'

  if (isPreflight) {
    const preflightHeaders = {
      ...(isAllowedOrigin && { 'Access-Control-Allow-Origin': origin }),
      ...corsOptions,
    }
    return NextResponse.json({}, { headers: preflightHeaders })
  }

  // Handle simple requests
  const response = NextResponse.next()

  if (isAllowedOrigin) {
    response.headers.set('Access-Control-Allow-Origin', origin)
  }

  Object.entries(corsOptions).forEach(([key, value]) => {
    response.headers.set(key, value)
  })

  return response
}

export const config = {
  matcher: '/api/:path*',
}
```

```jsx filename="proxy.js" switcher
import { NextResponse } from 'next/server'

const allowedOrigins = ['https://acme.com', 'https://my-app.org']

const corsOptions = {
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization',
}

export function proxy(request) {
  // Check the origin from the request
  const origin = request.headers.get('origin') ?? ''
  const isAllowedOrigin = allowedOrigins.includes(origin)

  // Handle preflighted requests
  const isPreflight = request.method === 'OPTIONS'

  if (isPreflight) {
    const preflightHeaders = {
      ...(isAllowedOrigin && { 'Access-Control-Allow-Origin': origin }),
      ...corsOptions,
    }
    return NextResponse.json({}, { headers: preflightHeaders })
  }

  // Handle simple requests
  const response = NextResponse.next()

  if (isAllowedOrigin) {
    response.headers.set('Access-Control-Allow-Origin', origin)
  }

  Object.entries(corsOptions).forEach(([key, value]) => {
    response.headers.set(key, value)
  })

  return response
}

export const config = {
  matcher: '/api/:path*',
}
```

### Producing a response

You can respond from Proxy directly by returning a `Response` or `NextResponse` instance. (This is available since [Next.js v13.1.0](https://nextjs.org/blog/next-13-1#nextjs-advanced-proxy))

```ts filename="proxy.ts" switcher
import type { NextRequest } from 'next/server'
import { isAuthenticated } from '@lib/auth'

// Limit the proxy to paths starting with `/api/`
export const config = {
  matcher: '/api/:function*',
}

export function proxy(request: NextRequest) {
  // Call our authentication function to check the request
  if (!isAuthenticated(request)) {
    // Respond with JSON indicating an error message
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

```js filename="proxy.js" switcher
import { isAuthenticated } from '@lib/auth'

// Limit the proxy to paths starting with `/api/`
export const config = {
  matcher: '/api/:function*',
}

export function proxy(request) {
  // Call our authentication function to check the request
  if (!isAuthenticated(request)) {
    // Respond with JSON indicating an error message
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

### Negative matching

The `matcher` config allows full regex so matching like negative lookaheads or character matching is supported. An example of a negative lookahead to match all except specific paths can be seen here:

```js filename="proxy.js"
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico, sitemap.xml, robots.txt (metadata files)
     */
    '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
  ],
}
```

You can also bypass Proxy for certain requests by using the `missing` or `has` arrays, or a combination of both:

```js filename="proxy.js"
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico, sitemap.xml, robots.txt (metadata files)
     */
    {
      source:
        '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },

    {
      source:
        '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
      has: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },

    {
      source:
        '/((?!api|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
      has: [{ type: 'header', key: 'x-present' }],
      missing: [{ type: 'header', key: 'x-missing', value: 'prefetch' }],
    },
  ],
}
```

> **Good to know**:
>
> Even when `_next/data` is excluded in a negative matcher pattern, proxy will still be invoked for `_next/data` routes. This is intentional behavior to prevent accidental security issues where you might protect a page but forget to protect the corresponding data route.

```js filename="proxy.js"
export const config = {
  matcher:
    '/((?!api|_next/data|_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)',
}

// Proxy will still run for /_next/data/* routes despite being excluded
```

### `waitUntil` and `NextFetchEvent`

The `NextFetchEvent` object extends the native [`FetchEvent`](https://developer.mozilla.org/docs/Web/API/FetchEvent) object, and includes the [`waitUntil()`](https://developer.mozilla.org/docs/Web/API/ExtendableEvent/waitUntil) method.

The `waitUntil()` method takes a promise as an argument, and extends the lifetime of the Proxy until the promise settles. This is useful for performing work in the background.

```ts filename="proxy.ts"
import { NextResponse } from 'next/server'
import type { NextFetchEvent, NextRequest } from 'next/server'

export function proxy(req: NextRequest, event: NextFetchEvent) {
  event.waitUntil(
    fetch('https://my-analytics-platform.com', {
      method: 'POST',
      body: JSON.stringify({ pathname: req.nextUrl.pathname }),
    })
  )

  return NextResponse.next()
}
```

### Unit testing (experimental)

Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test proxy files. Unit testing proxy can help ensure that it's only run on desired paths and that custom routing logic works as intended before code reaches production.

The `unstable_doesProxyMatch` function can be used to assert whether proxy will run for the provided URL, headers, and cookies.

```js
import { unstable_doesProxyMatch } from 'next/experimental/testing/server'

expect(
  unstable_doesProxyMatch({
    config,
    nextConfig,
    url: '/test',
  })
).toEqual(false)
```

The entire proxy function can also be tested.

```js
import { isRewrite, getRewrittenUrl } from 'next/experimental/testing/server'

const request = new NextRequest('https://nextjs.org/docs')
const response = await proxy(request)
expect(isRewrite(response)).toEqual(true)
expect(getRewrittenUrl(response)).toEqual('https://other-domain.com/docs')
// getRedirectUrl could also be used if the response were a redirect
```

## Platform support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure Proxy](/docs/app/guides/self-hosting.md#proxy) when self-hosting Next.js.

## Migration to Proxy

### Why the Change

The reason behind the renaming of `middleware` is that the term "middleware" can often be confused with Express.js middleware, leading to a misinterpretation of its purpose. Also, Middleware is highly capable, so it may encourage the usage; however, this feature is recommended to be used as a last resort.

Next.js is moving forward to provide better APIs with better ergonomics so that developers can achieve their goals without Middleware. This is the reason behind the renaming of `middleware`.

### Why "Proxy"

The name Proxy clarifies what Middleware is capable of. The term "proxy" implies that it has a network boundary in front of the app, which is the behavior of Middleware. Also, Middleware defaults to run at the [Edge Runtime](/docs/app/api-reference/edge.md), which can run closer to the client, separated from the app's region. These behaviors align better with the term "proxy" and provide a clearer purpose of the feature.

### How to Migrate

We recommend users avoid relying on Middleware unless no other options exist. Our goal is to give them APIs with better ergonomics so they can achieve their goals without Middleware.

The term “middleware” often confuses users with Express.js middleware, which can encourage misuse. To clarify our direction, we are renaming the file convention to “proxy.” This highlights that we are moving away from Middleware, breaking down its overloaded features, and making the Proxy clear in its purpose.

Next.js provides a codemod to migrate from `middleware.ts` to `proxy.ts`. You can run the following command to migrate:

```bash
npx @next/codemod@canary middleware-to-proxy .
```

The codemod will rename the file and the function name from `middleware` to `proxy`.

```diff
// middleware.ts -> proxy.ts

- export function middleware() {
+ export function proxy() {
```

## Version history

| Version   | Changes                                                                                       |
| --------- | --------------------------------------------------------------------------------------------- |
| `v16.0.0` | Middleware is deprecated and renamed to Proxy                                                 |
| `v15.5.0` | Middleware can now use the Node.js runtime (stable)                                           |
| `v15.2.0` | Middleware can now use the Node.js runtime (experimental)                                     |
| `v13.1.0` | Advanced Middleware flags added                                                               |
| `v13.0.0` | Middleware can modify request headers, response headers, and send responses                   |
| `v12.2.0` | Middleware is stable, please see the [upgrade guide](/docs/messages/middleware-upgrade-guide.md) |
| `v12.0.9` | Enforce absolute URLs in Edge Runtime ([PR](https://github.com/vercel/next.js/pull/33410))    |
| `v12.0.0` | Middleware (Beta) added                                                                       |
## Learn more about Proxy- [NextRequest](/docs/app/api-reference/functions/next-request.md)
  - API Reference for NextRequest.
- [NextResponse](/docs/app/api-reference/functions/next-response.md)
  - API Reference for NextResponse.


--------------------------------------------------------------------------------
title: "public Folder"
description: "Next.js allows you to serve static files, like images, in the public directory. You can learn how it works here."
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder"
--------------------------------------------------------------------------------

# public

@router: Pages Router

Next.js can serve static files, like images, under a folder called `public` in the root directory. Files inside `public` can then be referenced by your code starting from the base URL (`/`).

For example, the file `public/avatars/me.png` can be viewed by visiting the `/avatars/me.png` path. The code to display that image might look like:

```jsx filename="avatar.js"
import Image from 'next/image'

export function Avatar({ id, alt }) {
  return <Image src={`/avatars/${id}.png`} alt={alt} width="64" height="64" />
}

export function AvatarOfMe() {
  return <Avatar id="me" alt="A portrait of me" />
}
```

## Caching

Next.js cannot safely cache assets in the `public` folder because they may change. The default caching headers applied are:

```jsx
Cache-Control: public, max-age=0
```

## Robots, Favicons, and others

The folder is also useful for `robots.txt`, `favicon.ico`, Google Site Verification, and any other static files (including `.html`). But make sure to not have a static file with the same name as a file in the `pages/` directory, as this will result in an error. [Read more](/docs/messages/conflicting-public-file-page.md).


--------------------------------------------------------------------------------
title: "src Folder"
description: "Save pages under the `src` folder as an alternative to the root `pages` directory."
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder"
--------------------------------------------------------------------------------

# src Directory

@router: Pages Router

As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` folder.

This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.

To use the `src` folder, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.

![An example folder structure with the src folder](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-src-directory.png)

> **Good to know**:
>
> * The `/public` directory should remain in the root of your project.
> * Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
> * `.env.*` files should remain in the root of your project.
> * `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
> * If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
> * If you're using Proxy, ensure it is placed inside the `src` folder.
> * If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the [content section](https://tailwindcss.com/docs/content-configuration).
> * If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.
- [Project Structure](/docs/app/getting-started/project-structure.md)
  - Learn the folder and file conventions in Next.js, and how to organize your project.


--------------------------------------------------------------------------------
title: "Functions"
description: "API Reference for Next.js Functions and Hooks."
source: "https://nextjs.org/docs/pages/api-reference/functions"
--------------------------------------------------------------------------------

# Functions

@router: Pages Router



 - [getInitialProps](/docs/pages/api-reference/functions/get-initial-props.md)
 - [getServerSideProps](/docs/pages/api-reference/functions/get-server-side-props.md)
 - [getStaticPaths](/docs/pages/api-reference/functions/get-static-paths.md)
 - [getStaticProps](/docs/pages/api-reference/functions/get-static-props.md)
 - [NextRequest](/docs/pages/api-reference/functions/next-request.md)
 - [NextResponse](/docs/pages/api-reference/functions/next-response.md)
 - [useReportWebVitals](/docs/pages/api-reference/functions/use-report-web-vitals.md)
 - [useRouter](/docs/pages/api-reference/functions/use-router.md)
 - [userAgent](/docs/pages/api-reference/functions/userAgent.md)

--------------------------------------------------------------------------------
title: "getInitialProps"
description: "Fetch dynamic data on the server for your React component with getInitialProps."
source: "https://nextjs.org/docs/pages/api-reference/functions/get-initial-props"
--------------------------------------------------------------------------------

# getInitialProps

@router: Pages Router

> **Good to know**: `getInitialProps` is a legacy API. We recommend using [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md) instead.

`getInitialProps` is an `async` function that can be added to the default exported React component for the page. It will run on both the server-side and again on the client-side during page transitions. The result of the function will be forwarded to the React component as `props`.

```tsx filename="pages/index.tsx" switcher
import { NextPageContext } from 'next'

Page.getInitialProps = async (ctx: NextPageContext) => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const json = await res.json()
  return { stars: json.stargazers_count }
}

export default function Page({ stars }: { stars: number }) {
  return stars
}
```

```jsx filename="pages/index.js" switcher
Page.getInitialProps = async (ctx) => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const json = await res.json()
  return { stars: json.stargazers_count }
}

export default function Page({ stars }) {
  return stars
}
```

> **Good to know**:
>
> * Data returned from `getInitialProps` is serialized when server rendering. Ensure the returned object from `getInitialProps` is a plain `Object`, and not using `Date`, `Map` or `Set`.
> * For the initial page load, `getInitialProps` will run on the server only. `getInitialProps` will then also run on the client when navigating to a different route with the [`next/link`](/docs/pages/api-reference/components/link.md) component or by using [`next/router`](/docs/pages/api-reference/functions/use-router.md).
> * If `getInitialProps` is used in a custom `_app.js`, and the page being navigated to is using `getServerSideProps`, then `getInitialProps` will also run on the server.

## Context Object

`getInitialProps` receives a single argument called `context`, which is an object with the following properties:

| Name       | Description                                                                                           |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| `pathname` | Current route, the path of the page in `/pages`                                                       |
| `query`    | Query string of the URL, parsed as an object                                                          |
| `asPath`   | `String` of the actual path (including the query) shown in the browser                                |
| `req`      | [HTTP request object](https://nodejs.org/api/http.html#http_class_http_incomingmessage) (server only) |
| `res`      | [HTTP response object](https://nodejs.org/api/http.html#http_class_http_serverresponse) (server only) |
| `err`      | Error object if any error is encountered during the rendering                                         |

## Caveats

* `getInitialProps` can only be used in `pages/` top level files, and not in nested components. To have nested data fetching at the component level, consider exploring the [App Router](/docs/app/getting-started/fetching-data.md).
* Regardless of whether your route is static or dynamic, any data returned from `getInitialProps` as `props` will be able to be examined on the client-side in the initial HTML. This is to allow the page to be [hydrated](https://react.dev/reference/react-dom/hydrate) correctly. Make sure that you don't pass any sensitive information that shouldn't be available on the client in `props`.


--------------------------------------------------------------------------------
title: "getServerSideProps"
description: "API reference for `getServerSideProps`. Learn how to fetch data on each request with Next.js."
source: "https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props"
--------------------------------------------------------------------------------

# getServerSideProps

@router: Pages Router

When exporting a function called `getServerSideProps` (Server-Side Rendering) from a page, Next.js will pre-render this page on each request using the data returned by `getServerSideProps`. This is useful if you want to fetch data that changes often, and have the page update to show the most current data.

```tsx filename="pages/index.tsx" switcher
import type { InferGetServerSidePropsType, GetServerSideProps } from 'next'

type Repo = {
  name: string
  stargazers_count: number
}

export const getServerSideProps = (async () => {
  // Fetch data from external API
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo: Repo = await res.json()
  // Pass data to the page via props
  return { props: { repo } }
}) satisfies GetServerSideProps<{ repo: Repo }>

export default function Page({
  repo,
}: InferGetServerSidePropsType<typeof getServerSideProps>) {
  return (
    <main>
      <p>{repo.stargazers_count}</p>
    </main>
  )
}
```

```jsx filename="pages/index.js" switcher
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  // Pass data to the page via props
  return { props: { repo } }
}

export default function Page({ repo }) {
  return (
    <main>
      <p>{repo.stargazers_count}</p>
    </main>
  )
}
```

You can import modules in top-level scope for use in `getServerSideProps`. Imports used will **not be bundled for the client-side**. This means you can write **server-side code directly in `getServerSideProps`**, including fetching data from your database.

## Context parameter

The `context` parameter is an object containing the following keys:

| Name            | Description                                                                                                                                                                                                           |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `params`        | If this page uses a [dynamic route](/docs/pages/building-your-application/routing/dynamic-routes.md), `params` contains the route parameters. If the page name is `[id].js`, then `params` will look like `{ id: ... }`. |
| `req`           | [The `HTTP` IncomingMessage object](https://nodejs.org/api/http.html#http_class_http_incomingmessage), with an additional `cookies` prop, which is an object with string keys mapping to string values of cookies.    |
| `res`           | [The `HTTP` response object](https://nodejs.org/api/http.html#http_class_http_serverresponse).                                                                                                                        |
| `query`         | An object representing the query string, including dynamic route parameters.                                                                                                                                          |
| `preview`       | (Deprecated for `draftMode`) `preview` is `true` if the page is in the [Preview Mode](/docs/pages/guides/preview-mode.md) and `false` otherwise.                                                                         |
| `previewData`   | (Deprecated for `draftMode`) The [preview](/docs/pages/guides/preview-mode.md) data set by `setPreviewData`.                                                                                                             |
| `draftMode`     | `draftMode` is `true` if the page is in the [Draft Mode](/docs/pages/guides/draft-mode.md) and `false` otherwise.                                                                                                        |
| `resolvedUrl`   | A normalized version of the request `URL` that strips the `_next/data` prefix for client transitions and includes original query values.                                                                              |
| `locale`        | Contains the active locale (if enabled).                                                                                                                                                                              |
| `locales`       | Contains all supported locales (if enabled).                                                                                                                                                                          |
| `defaultLocale` | Contains the configured default locale (if enabled).                                                                                                                                                                  |

## getServerSideProps return values

The `getServerSideProps` function should return an object with **any one of the following** properties:

### `props`

The `props` object is a key-value pair, where each value is received by the page component. It should be a [serializable object](https://developer.mozilla.org/docs/Glossary/Serialization) so that any props passed, could be serialized with [`JSON.stringify`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

```jsx
export async function getServerSideProps(context) {
  return {
    props: { message: `Next.js is awesome` }, // will be passed to the page component as props
  }
}
```

### `notFound`

The `notFound` boolean allows the page to return a `404` status and [404 Page](/docs/pages/building-your-application/routing/custom-error.md#404-page). With `notFound: true`, the page will return a `404` even if there was a successfully generated page before. This is meant to support use cases like user-generated content getting removed by its author.

```js
export async function getServerSideProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

### `redirect`

The `redirect` object allows redirecting to internal and external resources. It should match the shape of `{ destination: string, permanent: boolean }`. In some rare cases, you might need to assign a custom status code for older `HTTP` clients to properly redirect. In these cases, you can use the `statusCode` property instead of the `permanent` property, but not both.

```js
export async function getServerSideProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
      },
    }
  }

  return {
    props: {}, // will be passed to the page component as props
  }
}
```

## Version History

| Version   | Changes                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------- |
| `v13.4.0` | [App Router](/docs/app/getting-started/fetching-data.md) is now stable with simplified data fetching |
| `v10.0.0` | `locale`, `locales`, `defaultLocale`, and `notFound` options added.                               |
| `v9.3.0`  | `getServerSideProps` introduced.                                                                  |


--------------------------------------------------------------------------------
title: "getStaticPaths"
description: "API reference for `getStaticPaths`. Learn how to fetch data and generate static pages with `getStaticPaths`."
source: "https://nextjs.org/docs/pages/api-reference/functions/get-static-paths"
--------------------------------------------------------------------------------

# getStaticPaths

@router: Pages Router

When exporting a function called `getStaticPaths` from a page that uses [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md), Next.js will statically pre-render all the paths specified by `getStaticPaths`.

```tsx filename="pages/repo/[name].tsx" switcher
import type {
  InferGetStaticPropsType,
  GetStaticProps,
  GetStaticPaths,
} from 'next'

type Repo = {
  name: string
  stargazers_count: number
}

export const getStaticPaths = (async () => {
  return {
    paths: [
      {
        params: {
          name: 'next.js',
        },
      }, // See the "paths" section below
    ],
    fallback: true, // false or "blocking"
  }
}) satisfies GetStaticPaths

export const getStaticProps = (async (context) => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  return { props: { repo } }
}) satisfies GetStaticProps<{
  repo: Repo
}>

export default function Page({
  repo,
}: InferGetStaticPropsType<typeof getStaticProps>) {
  return repo.stargazers_count
}
```

```jsx filename="pages/repo/[name].js" switcher
export async function getStaticPaths() {
  return {
    paths: [
      {
        params: {
          name: 'next.js',
        },
      }, // See the "paths" section below
    ],
    fallback: true, // false or "blocking"
  }
}

export async function getStaticProps() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  return { props: { repo } }
}

export default function Page({ repo }) {
  return repo.stargazers_count
}
```

## getStaticPaths return values

The `getStaticPaths` function should return an object with the following **required** properties:

### `paths`

The `paths` key determines which paths will be pre-rendered. For example, suppose that you have a page that uses [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md) named `pages/posts/[id].js`. If you export `getStaticPaths` from this page and return the following for `paths`:

```js
return {
  paths: [
    { params: { id: '1' }},
    {
      params: { id: '2' },
      // with i18n configured the locale for the path can be returned as well
      locale: "en",
    },
  ],
  fallback: ...
}
```

Then, Next.js will statically generate `/posts/1` and `/posts/2` during `next build` using the page component in `pages/posts/[id].js`.

The value for each `params` object must match the parameters used in the page name:

* If the page name is `pages/posts/[postId]/[commentId]`, then `params` should contain `postId` and `commentId`.
* If the page name uses [catch-all routes](/docs/pages/building-your-application/routing/dynamic-routes.md#catch-all-segments) like `pages/[...slug]`, then `params` should contain `slug` (which is an array). If this array is `['hello', 'world']`, then Next.js will statically generate the page at `/hello/world`.
* If the page uses an [optional catch-all route](/docs/pages/building-your-application/routing/dynamic-routes.md#optional-catch-all-segments), use `null`, `[]`, `undefined` or `false` to render the root-most route. For example, if you supply `slug: false` for `pages/[[...slug]]`, Next.js will statically generate the page `/`.

The `params` strings are **case-sensitive** and ideally should be normalized to ensure the paths are generated correctly. For example, if `WoRLD` is returned for a param it will only match if `WoRLD` is the actual path visited, not `world` or `World`.

Separate of the `params` object a `locale` field can be returned when [i18n is configured](/docs/pages/guides/internationalization.md), which configures the locale for the path being generated.

### `fallback: false`

If `fallback` is `false`, then any paths not returned by `getStaticPaths` will result in a **404 page**.

When `next build` is run, Next.js will check if `getStaticPaths` returned `fallback: false`, it will then build **only** the paths returned by `getStaticPaths`. This option is useful if you have a small number of paths to create, or new page data is not added often. If you find that you need to add more paths, and you have `fallback: false`, you will need to run `next build` again so that the new paths can be generated.

The following example pre-renders one blog post per page called `pages/posts/[id].js`. The list of blog posts will be fetched from a CMS and returned by `getStaticPaths`. Then, for each page, it fetches the post data from a CMS using [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md).

```jsx filename="pages/posts/[id].js"
function Post({ post }) {
  // Render post...
}

// This function gets called at build time
export async function getStaticPaths() {
  // Call an external API endpoint to get posts
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // Get the paths we want to pre-render based on posts
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }))

  // We'll pre-render only these paths at build time.
  // { fallback: false } means other routes should 404.
  return { paths, fallback: false }
}

// This also gets called at build time
export async function getStaticProps({ params }) {
  // params contains the post `id`.
  // If the route is like /posts/1, then params.id is 1
  const res = await fetch(`https://.../posts/${params.id}`)
  const post = await res.json()

  // Pass post data to the page via props
  return { props: { post } }
}

export default Post
```

### `fallback: true`

<details>
<summary>Examples</summary>

* [Static generation of a large number of pages](https://react-tweet.vercel.app/)

</details>

If `fallback` is `true`, then the behavior of `getStaticProps` changes in the following ways:

* The paths returned from `getStaticPaths` will be rendered to `HTML` at build time by `getStaticProps`.
* The paths that have not been generated at build time will **not** result in a 404 page. Instead, Next.js will serve a [“fallback”](#fallback-pages) version of the page on the first request to such a path. Web crawlers, such as Google, won't be served a fallback and instead the path will behave as in [`fallback: 'blocking'`](#fallback-blocking).
* When a page with `fallback: true` is navigated to through `next/link` or `next/router` (client-side) Next.js will *not* serve a fallback and instead the page will behave as [`fallback: 'blocking'`](#fallback-blocking).
* In the background, Next.js will statically generate the requested path `HTML` and `JSON`. This includes running `getStaticProps`.
* When complete, the browser receives the `JSON` for the generated path. This will be used to automatically render the page with the required props. From the user’s perspective, the page will be swapped from the fallback page to the full page.
* At the same time, Next.js adds this path to the list of pre-rendered pages. Subsequent requests to the same path will serve the generated page, like other pages pre-rendered at build time.

> **Good to know**: `fallback: true` is not supported when using [`output: 'export'`](/docs/pages/guides/static-exports.md).

#### When is `fallback: true` useful?

`fallback: true` is useful if your app has a very large number of static pages that depend on data (such as a very large e-commerce site). If you want to pre-render all product pages, the builds would take a very long time.

Instead, you may statically generate a small subset of pages and use `fallback: true` for the rest. When someone requests a page that is not generated yet, the user will see the page with a loading indicator or skeleton component.

Shortly after, `getStaticProps` finishes and the page will be rendered with the requested data. From now on, everyone who requests the same page will get the statically pre-rendered page.

This ensures that users always have a fast experience while preserving fast builds and the benefits of Static Generation.

`fallback: true` will not *update* generated pages, for that take a look at [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md).

### `fallback: 'blocking'`

If `fallback` is `'blocking'`, new paths not returned by `getStaticPaths` will wait for the `HTML` to be generated, identical to SSR (hence why *blocking*), and then be cached for future requests so it only happens once per path.

`getStaticProps` will behave as follows:

* The paths returned from `getStaticPaths` will be rendered to `HTML` at build time by `getStaticProps`.
* The paths that have not been generated at build time will **not** result in a 404 page. Instead, Next.js will SSR on the first request and return the generated `HTML`.
* When complete, the browser receives the `HTML` for the generated path. From the user’s perspective, it will transition from "the browser is requesting the page" to "the full page is loaded". There is no flash of loading/fallback state.
* At the same time, Next.js adds this path to the list of pre-rendered pages. Subsequent requests to the same path will serve the generated page, like other pages pre-rendered at build time.

`fallback: 'blocking'` will not *update* generated pages by default. To update generated pages, use [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md) in conjunction with `fallback: 'blocking'`.

> **Good to know**: `fallback: 'blocking'` is not supported when using [`output: 'export'`](/docs/pages/guides/static-exports.md).

### Fallback pages

In the “fallback” version of a page:

* The page’s props will be empty.
* Using the [router](/docs/pages/api-reference/functions/use-router.md), you can detect if the fallback is being rendered, `router.isFallback` will be `true`.

The following example showcases using `isFallback`:

```jsx filename="pages/posts/[id].js"
import { useRouter } from 'next/router'

function Post({ post }) {
  const router = useRouter()

  // If the page is not yet generated, this will be displayed
  // initially until getStaticProps() finishes running
  if (router.isFallback) {
    return <div>Loading...</div>
  }

  // Render post...
}

// This function gets called at build time
export async function getStaticPaths() {
  return {
    // Only `/posts/1` and `/posts/2` are generated at build time
    paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
    // Enable statically generating additional pages
    // For example: `/posts/3`
    fallback: true,
  }
}

// This also gets called at build time
export async function getStaticProps({ params }) {
  // params contains the post `id`.
  // If the route is like /posts/1, then params.id is 1
  const res = await fetch(`https://.../posts/${params.id}`)
  const post = await res.json()

  // Pass post data to the page via props
  return {
    props: { post },
    // Re-generate the post at most once per second
    // if a request comes in
    revalidate: 1,
  }
}

export default Post
```

## Version History

| Version   | Changes                                                                                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v13.4.0` | [App Router](/docs/app/getting-started/fetching-data.md) is now stable with simplified data fetching, including [`generateStaticParams()`](/docs/app/api-reference/functions/generate-static-params.md) |
| `v12.2.0` | [On-Demand Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath) is stable.                                             |
| `v12.1.0` | [On-Demand Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath) added (beta).                                          |
| `v9.5.0`  | Stable [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md)                                                                                                      |
| `v9.3.0`  | `getStaticPaths` introduced.                                                                                                                                                                      |


--------------------------------------------------------------------------------
title: "getStaticProps"
description: "API reference for `getStaticProps`. Learn how to use `getStaticProps` to generate static pages with Next.js."
source: "https://nextjs.org/docs/pages/api-reference/functions/get-static-props"
--------------------------------------------------------------------------------

# getStaticProps

@router: Pages Router

Exporting a function called `getStaticProps` will pre-render a page at build time using the props returned from the function:

```tsx filename="pages/index.tsx" switcher
import type { InferGetStaticPropsType, GetStaticProps } from 'next'

type Repo = {
  name: string
  stargazers_count: number
}

export const getStaticProps = (async (context) => {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  return { props: { repo } }
}) satisfies GetStaticProps<{
  repo: Repo
}>

export default function Page({
  repo,
}: InferGetStaticPropsType<typeof getStaticProps>) {
  return repo.stargazers_count
}
```

```jsx filename="pages/index.js" switcher
export async function getStaticProps() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const repo = await res.json()
  return { props: { repo } }
}

export default function Page({ repo }) {
  return repo.stargazers_count
}
```

You can import modules in top-level scope for use in `getStaticProps`. Imports used will **not be bundled for the client-side**. This means you can write **server-side code directly in `getStaticProps`**, including fetching data from your database.

## Context parameter

The `context` parameter is an object containing the following keys:

| Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `params`           | Contains the route parameters for pages using [dynamic routes](/docs/pages/building-your-application/routing/dynamic-routes.md). For example, if the page name is `[id].js`, then `params` will look like `{ id: ... }`. You should use this together with `getStaticPaths`, which we'll explain later.                                                                                                                                 |
| `preview`          | (Deprecated for `draftMode`) `preview` is `true` if the page is in the [Preview Mode](/docs/pages/guides/preview-mode.md) and `false` otherwise.                                                                                                                                                                                                                                                                                        |
| `previewData`      | (Deprecated for `draftMode`) The [preview](/docs/pages/guides/preview-mode.md) data set by `setPreviewData`.                                                                                                                                                                                                                                                                                                                            |
| `draftMode`        | `draftMode` is `true` if the page is in the [Draft Mode](/docs/pages/guides/draft-mode.md) and `false` otherwise.                                                                                                                                                                                                                                                                                                                       |
| `locale`           | Contains the active locale (if enabled).                                                                                                                                                                                                                                                                                                                                                                                             |
| `locales`          | Contains all supported locales (if enabled).                                                                                                                                                                                                                                                                                                                                                                                         |
| `defaultLocale`    | Contains the configured default locale (if enabled).                                                                                                                                                                                                                                                                                                                                                                                 |
| `revalidateReason` | Provides a reason for why the function was called. Can be one of: "build" (run at build time), "stale" (revalidate period expired, or running in [development mode](/docs/pages/building-your-application/data-fetching/get-static-props.md#runs-on-every-request-in-development)), "on-demand" (triggered via [on-demand revalidation](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath)) |

## getStaticProps return values

The `getStaticProps` function should return an object containing either `props`, `redirect`, or `notFound` followed by an **optional** `revalidate` property.

### `props`

The `props` object is a key-value pair, where each value is received by the page component. It should be a [serializable object](https://developer.mozilla.org/docs/Glossary/Serialization) so that any props passed, could be serialized with [`JSON.stringify`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify).

```jsx
export async function getStaticProps(context) {
  return {
    props: { message: `Next.js is awesome` }, // will be passed to the page component as props
  }
}
```

### `revalidate`

The `revalidate` property is the amount in seconds after which a page re-generation can occur (defaults to `false` or no revalidation).

```js
// This function gets called at build time on server-side.
// It may be called again, on a serverless function, if
// revalidation is enabled and a new request comes in
export async function getStaticProps() {
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  return {
    props: {
      posts,
    },
    // Next.js will attempt to re-generate the page:
    // - When a request comes in
    // - At most once every 10 seconds
    revalidate: 10, // In seconds
  }
}
```

Learn more about [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md).

The cache status of a page leveraging ISR can be determined by reading the value of the `x-nextjs-cache` response header. The possible values are the following:

* `MISS` - the path is not in the cache (occurs at most once, on the first visit)
* `STALE` - the path is in the cache but exceeded the revalidate time so it will be updated in the background
* `HIT` - the path is in the cache and has not exceeded the revalidate time

### `notFound`

The `notFound` boolean allows the page to return a `404` status and [404 Page](/docs/pages/building-your-application/routing/custom-error.md#404-page). With `notFound: true`, the page will return a `404` even if there was a successfully generated page before. This is meant to support use cases like user-generated content getting removed by its author. Note, `notFound` follows the same `revalidate` behavior [described here](#revalidate).

```js
export async function getStaticProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

> **Good to know**: `notFound` is not needed for [`fallback: false`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-false) mode as only paths returned from `getStaticPaths` will be pre-rendered.

### `redirect`

The `redirect` object allows redirecting to internal or external resources. It should match the shape of `{ destination: string, permanent: boolean }`.

In some rare cases, you might need to assign a custom status code for older `HTTP` clients to properly redirect. In these cases, you can use the `statusCode` property instead of the `permanent` property, **but not both**. You can also set `basePath: false` similar to redirects in `next.config.js`.

```js
export async function getStaticProps(context) {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!data) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
        // statusCode: 301
      },
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

If the redirects are known at build-time, they should be added in [`next.config.js`](/docs/pages/api-reference/config/next-config-js/redirects.md) instead.

## Reading files: Use `process.cwd()`

Files can be read directly from the filesystem in `getStaticProps`.

In order to do so you have to get the full path to a file.

Since Next.js compiles your code into a separate directory you can't use `__dirname` as the path it returns will be different from the Pages Router.

Instead you can use `process.cwd()` which gives you the directory where Next.js is being executed.

```jsx
import { promises as fs } from 'fs'
import path from 'path'

// posts will be populated at build time by getStaticProps()
function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>
          <h3>{post.filename}</h3>
          <p>{post.content}</p>
        </li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  const postsDirectory = path.join(process.cwd(), 'posts')
  const filenames = await fs.readdir(postsDirectory)

  const posts = filenames.map(async (filename) => {
    const filePath = path.join(postsDirectory, filename)
    const fileContents = await fs.readFile(filePath, 'utf8')

    // Generally you would parse/transform the contents
    // For example you can transform markdown to HTML here

    return {
      filename,
      content: fileContents,
    }
  })
  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts: await Promise.all(posts),
    },
  }
}

export default Blog
```

## Version History

| Version   | Changes                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v13.4.0` | [App Router](/docs/app/getting-started/fetching-data.md) is now stable with simplified data fetching                                                        |
| `v12.2.0` | [On-Demand Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath) is stable.    |
| `v12.1.0` | [On-Demand Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath) added (beta). |
| `v10.0.0` | `locale`, `locales`, `defaultLocale`, and `notFound` options added.                                                                                      |
| `v10.0.0` | `fallback: 'blocking'` return option added.                                                                                                              |
| `v9.5.0`  | Stable [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md)                                                             |
| `v9.3.0`  | `getStaticProps` introduced.                                                                                                                             |


--------------------------------------------------------------------------------
title: "NextRequest"
description: "API Reference for NextRequest."
source: "https://nextjs.org/docs/pages/api-reference/functions/next-request"
--------------------------------------------------------------------------------

# NextRequest

@router: Pages Router

NextRequest extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional convenience methods.

## `cookies`

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the request.

### `set(name, value)`

Given a name, set a cookie with the given value on the request.

```ts
// Given incoming request /home
// Set a cookie to hide the banner
// request will have a `Set-Cookie:show-banner=false;path=/home` header
request.cookies.set('show-banner', 'false')
```

### `get(name)`

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```ts
// Given incoming request /home
// { name: 'show-banner', value: 'false', Path: '/home' }
request.cookies.get('show-banner')
```

### `getAll()`

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the request.

```ts
// Given incoming request /home
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
request.cookies.getAll('experiments')
// Alternatively, get all cookies for the request
request.cookies.getAll()
```

### `delete(name)`

Given a cookie name, delete the cookie from the request.

```ts
// Returns true for deleted, false is nothing is deleted
request.cookies.delete('experiments')
```

### `has(name)`

Given a cookie name, return `true` if the cookie exists on the request.

```ts
// Returns true if cookie exists, false if it does not
request.cookies.has('experiments')
```

### `clear()`

Remove the `Set-Cookie` header from the request.

```ts
request.cookies.clear()
```

## `nextUrl`

Extends the native [`URL`](https://developer.mozilla.org/docs/Web/API/URL) API with additional convenience methods, including Next.js specific properties.

```ts
// Given a request to /home, pathname is /home
request.nextUrl.pathname
// Given a request to /home?name=lee, searchParams is { 'name': 'lee' }
request.nextUrl.searchParams
```

The following options are available:

| Property          | Type                      | Description                                                                                                                            |
| ----------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `basePath`        | `string`                  | The [base path](/docs/pages/api-reference/config/next-config-js/basePath.md) of the URL.                                                  |
| `buildId`         | `string` | `undefined`   | The build identifier of the Next.js application. Can be [customized](/docs/pages/api-reference/config/next-config-js/generateBuildId.md). |
| `defaultLocale`   | `string` | `undefined`   | The default locale for [internationalization](/docs/pages/guides/internationalization.md).                                                |
| `domainLocale`    |                           |                                                                                                                                        |
| - `defaultLocale` | `string`                  | The default locale within a domain.                                                                                                    |
| - `domain`        | `string`                  | The domain associated with a specific locale.                                                                                          |
| - `http`          | `boolean` | `undefined`  | Indicates if the domain is using HTTP.                                                                                                 |
| `locales`         | `string[]` | `undefined` | An array of available locales.                                                                                                         |
| `locale`          | `string` | `undefined`   | The currently active locale.                                                                                                           |
| `url`             | `URL`                     | The URL object.                                                                                                                        |

## Version History

| Version   | Changes                 |
| --------- | ----------------------- |
| `v15.0.0` | `ip` and `geo` removed. |


--------------------------------------------------------------------------------
title: "NextResponse"
description: "API Reference for NextResponse."
source: "https://nextjs.org/docs/pages/api-reference/functions/next-response"
--------------------------------------------------------------------------------

# NextResponse

@router: Pages Router

NextResponse extends the [Web Response API](https://developer.mozilla.org/docs/Web/API/Response) with additional convenience methods.

## `cookies`

Read or mutate the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header of the response.

### `set(name, value)`

Given a name, set a cookie with the given value on the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// Set a cookie to hide the banner
response.cookies.set('show-banner', 'false')
// Response will have a `Set-Cookie:show-banner=false;path=/home` header
return response
```

### `get(name)`

Given a cookie name, return the value of the cookie. If the cookie is not found, `undefined` is returned. If multiple cookies are found, the first one is returned.

```ts
// Given incoming request /home
let response = NextResponse.next()
// { name: 'show-banner', value: 'false', Path: '/home' }
response.cookies.get('show-banner')
```

### `getAll()`

Given a cookie name, return the values of the cookie. If no name is given, return all cookies on the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// [
//   { name: 'experiments', value: 'new-pricing-page', Path: '/home' },
//   { name: 'experiments', value: 'winter-launch', Path: '/home' },
// ]
response.cookies.getAll('experiments')
// Alternatively, get all cookies for the response
response.cookies.getAll()
```

### `delete(name)`

Given a cookie name, delete the cookie from the response.

```ts
// Given incoming request /home
let response = NextResponse.next()
// Returns true for deleted, false if nothing is deleted
response.cookies.delete('experiments')
```

## `json()`

Produce a response with the given JSON body.

```ts filename="app/api/route.ts" switcher
import { NextResponse } from 'next/server'

export async function GET(request: Request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```

```js filename="app/api/route.js" switcher
import { NextResponse } from 'next/server'

export async function GET(request) {
  return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 })
}
```

## `redirect()`

Produce a response that redirects to a [URL](https://developer.mozilla.org/docs/Web/API/URL).

```ts
import { NextResponse } from 'next/server'

return NextResponse.redirect(new URL('/new', request.url))
```

The [URL](https://developer.mozilla.org/docs/Web/API/URL) can be created and modified before being used in the `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.

```ts
import { NextResponse } from 'next/server'

// Given an incoming request...
const loginUrl = new URL('/login', request.url)
// Add ?from=/incoming-url to the /login URL
loginUrl.searchParams.set('from', request.nextUrl.pathname)
// And redirect to the new URL
return NextResponse.redirect(loginUrl)
```

## `rewrite()`

Produce a response that rewrites (proxies) the given [URL](https://developer.mozilla.org/docs/Web/API/URL) while preserving the original URL.

```ts
import { NextResponse } from 'next/server'

// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
return NextResponse.rewrite(new URL('/proxy', request.url))
```

## `next()`

The `next()` method is useful for Proxy, as it allows you to return early and continue routing.

```ts
import { NextResponse } from 'next/server'

return NextResponse.next()
```

You can also forward `headers` upstream when producing the response, using `NextResponse.next({ request: { headers } })`:

```ts
import { NextResponse } from 'next/server'

// Given an incoming request...
const newHeaders = new Headers(request.headers)
// Add a new header
newHeaders.set('x-version', '123')
// Forward the modified request headers upstream
return NextResponse.next({
  request: {
    // New request headers
    headers: newHeaders,
  },
})
```

This forwards `newHeaders` upstream to the target page, route, or server action, and does not expose them to the client. While this pattern is useful for passing data upstream, it should be used with caution because the headers containing this data may be forwarded to external services.

In contrast, `NextResponse.next({ headers })` is a shorthand for sending headers from proxy to the client. This is **NOT** good practice and should be avoided. Among other reasons because setting response headers like `Content-Type`, can override framework expectations (for example, the `Content-Type` used by Server Actions), leading to failed submissions or broken streaming responses.

```ts
import { type NextRequest, NextResponse } from 'next/server'

async function proxy(request: NextRequest) {
  const headers = await injectAuth(request.headers)
  // DO NOT forward headers like this
  return NextResponse.next({ headers })
}
```

In general, avoid copying all incoming request headers because doing so can leak sensitive data to clients or upstream services.

Prefer a defensive approach by creating a subset of incoming request headers using an allow-list. For example, you might discard custom `x-*` headers and only forward known-safe headers:

```ts
import { type NextRequest, NextResponse } from 'next/server'

function proxy(request: NextRequest) {
  const incoming = new Headers(request.headers)
  const forwarded = new Headers()

  for (const [name, value] of incoming) {
    const headerName = name.toLowerCase()
    // Keep only known-safe headers, discard custom x-* and other sensitive ones
    if (
      !headerName.startsWith('x-') &&
      headerName !== 'authorization' &&
      headerName !== 'cookie'
    ) {
      // Preserve original header name casing
      forwarded.set(name, value)
    }
  }

  return NextResponse.next({
    request: {
      headers: forwarded,
    },
  })
}
```


--------------------------------------------------------------------------------
title: "useReportWebVitals"
description: "API Reference for the useReportWebVitals function."
source: "https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals"
--------------------------------------------------------------------------------

# useReportWebVitals

@router: Pages Router

The `useReportWebVitals` hook allows you to report [Core Web Vitals](https://web.dev/vitals/), and can be used in combination with your analytics service.

New functions passed to `useReportWebVitals` are called with the available metrics up to that point. To prevent reporting duplicated data, ensure that the callback function reference does not change (as shown in the code examples below).

```jsx filename="pages/_app.js"
import { useReportWebVitals } from 'next/web-vitals'

const logWebVitals = (metric) => {
  console.log(metric)
}

function MyApp({ Component, pageProps }) {
  useReportWebVitals(logWebVitals)

  return <Component {...pageProps} />
}
```

## useReportWebVitals

The `metric` object passed as the hook's argument consists of a number of properties:

* `id`: Unique identifier for the metric in the context of the current page load
* `name`: The name of the performance metric. Possible values include names of [Web Vitals](#web-vitals) metrics (TTFB, FCP, LCP, FID, CLS) specific to a web application.
* `delta`: The difference between the current value and the previous value of the metric. The value is typically in milliseconds and represents the change in the metric's value over time.
* `entries`: An array of [Performance Entries](https://developer.mozilla.org/docs/Web/API/PerformanceEntry) associated with the metric. These entries provide detailed information about the performance events related to the metric.
* `navigationType`: Indicates the [type of navigation](https://developer.mozilla.org/docs/Web/API/PerformanceNavigationTiming/type) that triggered the metric collection. Possible values include `"navigate"`, `"reload"`, `"back_forward"`, and `"prerender"`.
* `rating`: A qualitative rating of the metric value, providing an assessment of the performance. Possible values are `"good"`, `"needs-improvement"`, and `"poor"`. The rating is typically determined by comparing the metric value against predefined thresholds that indicate acceptable or suboptimal performance.
* `value`: The actual value or duration of the performance entry, typically in milliseconds. The value provides a quantitative measure of the performance aspect being tracked by the metric. The source of the value depends on the specific metric being measured and can come from various [Performance API](https://developer.mozilla.org/docs/Web/API/Performance_API)s.

## Web Vitals

[Web Vitals](https://web.dev/vitals/) are a set of useful metrics that aim to capture the user
experience of a web page. The following web vitals are all included:

* [Time to First Byte](https://developer.mozilla.org/docs/Glossary/Time_to_first_byte) (TTFB)
* [First Contentful Paint](https://developer.mozilla.org/docs/Glossary/First_contentful_paint) (FCP)
* [Largest Contentful Paint](https://web.dev/lcp/) (LCP)
* [First Input Delay](https://web.dev/fid/) (FID)
* [Cumulative Layout Shift](https://web.dev/cls/) (CLS)
* [Interaction to Next Paint](https://web.dev/inp/) (INP)

You can handle all the results of these metrics using the `name` property.

```jsx filename="pages/_app.js"
import { useReportWebVitals } from 'next/web-vitals'

const handleWebVitals = (metric) => {
  switch (metric.name) {
    case 'FCP': {
      // handle FCP results
    }
    case 'LCP': {
      // handle LCP results
    }
    // ...
  }
}

function MyApp({ Component, pageProps }) {
  useReportWebVitals(handleWebVitals)

  return <Component {...pageProps} />
}
```

## Custom Metrics

In addition to the core metrics listed above, there are some additional custom metrics that
measure the time it takes for the page to hydrate and render:

* `Next.js-hydration`: Length of time it takes for the page to start and finish hydrating (in ms)
* `Next.js-route-change-to-render`: Length of time it takes for a page to start rendering after a
  route change (in ms)
* `Next.js-render`: Length of time it takes for a page to finish render after a route change (in ms)

You can handle all the results of these metrics separately:

```jsx filename="pages/_app.js"
import { useReportWebVitals } from 'next/web-vitals'

function handleCustomMetrics(metrics) {
  switch (metric.name) {
    case 'Next.js-hydration':
      // handle hydration results
      break
    case 'Next.js-route-change-to-render':
      // handle route-change to render results
      break
    case 'Next.js-render':
      // handle render results
      break
    default:
      break
  }
}

function MyApp({ Component, pageProps }) {
  useReportWebVitals(handleCustomMetrics)

  return <Component {...pageProps} />
}
```

These metrics work in all browsers that support the [User Timing API](https://caniuse.com/#feat=user-timing).

## Sending results to external systems

You can send results to any endpoint to measure and track
real user performance on your site. For example:

```js
function postWebVitals(metrics) {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'

  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
}

useReportWebVitals(postWebVitals)
```

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the
> `id` value can allow you to construct metric distributions manually (to calculate percentiles,
> etc.)

> ```js
> useReportWebVitals(metric => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   });
> }
> ```
>
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).


--------------------------------------------------------------------------------
title: "useRouter"
description: "Learn more about the API of the Next.js Router, and access the router instance in your page with the useRouter hook."
source: "https://nextjs.org/docs/pages/api-reference/functions/use-router"
--------------------------------------------------------------------------------

# useRouter

@router: Pages Router

If you want to access the [`router` object](#router-object) inside any function component in your app, you can use the `useRouter` hook, take a look at the following example:

```jsx
import { useRouter } from 'next/router'

function ActiveLink({ children, href }) {
  const router = useRouter()
  const style = {
    marginRight: 10,
    color: router.asPath === href ? 'red' : 'black',
  }

  const handleClick = (e) => {
    e.preventDefault()
    router.push(href)
  }

  return (
    <a href={href} onClick={handleClick} style={style}>
      {children}
    </a>
  )
}

export default ActiveLink
```

> `useRouter` is a [React Hook](https://react.dev/learn#using-hooks), meaning it cannot be used with classes. You can either use [withRouter](#withrouter) or wrap your class in a function component.

## `router` object

The following is the definition of the `router` object returned by both [`useRouter`](#top) and [`withRouter`](#withrouter):

* `pathname`: `String` - The path for current route file that comes after `/pages`. Therefore, `basePath`, `locale` and trailing slash (`trailingSlash: true`) are not included.
* `query`: `Object` - The query string parsed to an object, including [dynamic route](/docs/pages/building-your-application/routing/dynamic-routes.md) parameters. It will be an empty object during prerendering if the page doesn't use [Server-side Rendering](/docs/pages/building-your-application/data-fetching/get-server-side-props.md). Defaults to `{}`
* `asPath`: `String` - The path as shown in the browser including the search params and respecting the `trailingSlash` configuration. `basePath` and `locale` are not included.
* `isFallback`: `boolean` - Whether the current page is in [fallback mode](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true).
* `basePath`: `String` - The active [basePath](/docs/app/api-reference/config/next-config-js/basePath.md) (if enabled).
* `locale`: `String` - The active locale (if enabled).
* `locales`: `String[]` - All supported locales (if enabled).
* `defaultLocale`: `String` - The current default locale (if enabled).
* `domainLocales`: `Array<{domain, defaultLocale, locales}>` - Any configured domain locales.
* `isReady`: `boolean` - Whether the router fields are updated client-side and ready for use. Should only be used inside of `useEffect` methods and not for conditionally rendering on the server. See related docs for use case with [automatically statically optimized pages](/docs/pages/building-your-application/rendering/automatic-static-optimization.md)
* `isPreview`: `boolean` - Whether the application is currently in [preview mode](/docs/pages/guides/preview-mode.md).

> Using the `asPath` field may lead to a mismatch between client and server if the page is rendered using server-side rendering or [automatic static optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md). Avoid using `asPath` until the `isReady` field is `true`.

The following methods are included inside `router`:

### router.push

Handles client-side transitions, this method is useful for cases where [`next/link`](/docs/pages/api-reference/components/link.md) is not enough.

```js
router.push(url, as, options)
```

* `url`: `UrlObject | String` - The URL to navigate to (see [Node.JS URL module documentation](https://nodejs.org/api/url.html#legacy-urlobject) for `UrlObject` properties).
* `as`: `UrlObject | String` - Optional decorator for the path that will be shown in the browser URL bar. Before Next.js 9.5.3 this was used for dynamic routes.
* `options` - Optional object with the following configuration options:
  * `scroll` - Optional boolean, controls scrolling to the top of the page after navigation. Defaults to `true`
  * [`shallow`](/docs/pages/building-your-application/routing/linking-and-navigating.md#shallow-routing): Update the path of the current page without rerunning [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md), [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md) or [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md). Defaults to `false`
  * `locale` - Optional string, indicates locale of the new page

> You don't need to use `router.push` for external URLs. [window.location](https://developer.mozilla.org/docs/Web/API/Window/location) is better suited for those cases.

Navigating to `pages/about.js`, which is a predefined route:

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/about')}>
      Click me
    </button>
  )
}
```

Navigating `pages/post/[pid].js`, which is a dynamic route:

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/post/abc')}>
      Click me
    </button>
  )
}
```

Redirecting the user to `pages/login.js`, useful for pages behind [authentication](/docs/pages/guides/authentication.md):

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

// Here you would fetch and return the user
const useUser = () => ({ user: null, loading: false })

export default function Page() {
  const { user, loading } = useUser()
  const router = useRouter()

  useEffect(() => {
    if (!(user || loading)) {
      router.push('/login')
    }
  }, [user, loading])

  return <p>Redirecting...</p>
}
```

#### Resetting state after navigation

When navigating to the same page in Next.js, the page's state **will not** be reset by default as React does not unmount unless the parent component has changed.

```jsx filename="pages/[slug].js"
import Link from 'next/link'
import { useState } from 'react'
import { useRouter } from 'next/router'

export default function Page(props) {
  const router = useRouter()
  const [count, setCount] = useState(0)
  return (
    <div>
      <h1>Page: {router.query.slug}</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase count</button>
      <Link href="/one">one</Link> <Link href="/two">two</Link>
    </div>
  )
}
```

In the above example, navigating between `/one` and `/two` **will not** reset the count . The `useState` is maintained between renders because the top-level React component, `Page`, is the same.

If you do not want this behavior, you have a couple of options:

* Manually ensure each state is updated using `useEffect`. In the above example, that could look like:

  ```jsx
  useEffect(() => {
    setCount(0)
  }, [router.query.slug])
  ```

* Use a React `key` to [tell React to remount the component](https://react.dev/learn/rendering-lists#keeping-list-items-in-order-with-key). To do this for all pages, you can use a custom app:

  ```jsx filename="pages/_app.js"
  import { useRouter } from 'next/router'

  export default function MyApp({ Component, pageProps }) {
    const router = useRouter()
    return <Component key={router.asPath} {...pageProps} />
  }
  ```

#### With URL object

You can use a URL object in the same way you can use it for [`next/link`](/docs/pages/api-reference/components/link.md#passing-a-url-object). Works for both the `url` and `as` parameters:

```jsx
import { useRouter } from 'next/router'

export default function ReadMore({ post }) {
  const router = useRouter()

  return (
    <button
      type="button"
      onClick={() => {
        router.push({
          pathname: '/post/[pid]',
          query: { pid: post.id },
        })
      }}
    >
      Click here to read more
    </button>
  )
}
```

### router.replace

Similar to the `replace` prop in [`next/link`](/docs/pages/api-reference/components/link.md), `router.replace` will prevent adding a new URL entry into the `history` stack.

```js
router.replace(url, as, options)
```

* The API for `router.replace` is exactly the same as the API for [`router.push`](#routerpush).

Take a look at the following example:

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.replace('/home')}>
      Click me
    </button>
  )
}
```

### router.prefetch

Prefetch pages for faster client-side transitions. This method is only useful for navigations without [`next/link`](/docs/pages/api-reference/components/link.md), as `next/link` takes care of prefetching pages automatically.

> This is a production only feature. Next.js doesn't prefetch pages in development.

```js
router.prefetch(url, as, options)
```

* `url` - The URL to prefetch, including explicit routes (e.g. `/dashboard`) and dynamic routes (e.g. `/product/[id]`)
* `as` - Optional decorator for `url`. Before Next.js 9.5.3 this was used to prefetch dynamic routes.
* `options` - Optional object with the following allowed fields:
  * `locale` - allows providing a different locale from the active one. If `false`, `url` has to include the locale as the active locale won't be used.

Let's say you have a login page, and after a login, you redirect the user to the dashboard. For that case, we can prefetch the dashboard to make a faster transition, like in the following example:

```jsx
import { useCallback, useEffect } from 'react'
import { useRouter } from 'next/router'

export default function Login() {
  const router = useRouter()
  const handleSubmit = useCallback((e) => {
    e.preventDefault()

    fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        /* Form data */
      }),
    }).then((res) => {
      // Do a fast client-side transition to the already prefetched dashboard page
      if (res.ok) router.push('/dashboard')
    })
  }, [])

  useEffect(() => {
    // Prefetch the dashboard page
    router.prefetch('/dashboard')
  }, [router])

  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields */}
      <button type="submit">Login</button>
    </form>
  )
}
```

### router.beforePopState

In some cases (for example, if using a [Custom Server](/docs/pages/guides/custom-server.md)), you may wish to listen to [popstate](https://developer.mozilla.org/docs/Web/API/Window/popstate_event) and do something before the router acts on it.

```js
router.beforePopState(cb)
```

* `cb` - The function to run on incoming `popstate` events. The function receives the state of the event as an object with the following props:
  * `url`: `String` - the route for the new state. This is usually the name of a `page`
  * `as`: `String` - the url that will be shown in the browser
  * `options`: `Object` - Additional options sent by [router.push](#routerpush)

If `cb` returns `false`, the Next.js router will not handle `popstate`, and you'll be responsible for handling it in that case. See [Disabling file-system routing](/docs/pages/guides/custom-server.md#disabling-file-system-routing).

You could use `beforePopState` to manipulate the request, or force a SSR refresh, as in the following example:

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  useEffect(() => {
    router.beforePopState(({ url, as, options }) => {
      // I only want to allow these two routes!
      if (as !== '/' && as !== '/other') {
        // Have SSR render bad routes as a 404.
        window.location.href = as
        return false
      }

      return true
    })
  }, [router])

  return <p>Welcome to the page</p>
}
```

### router.back

Navigate back in history. Equivalent to clicking the browser’s back button. It executes `window.history.back()`.

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.back()}>
      Click here to go back
    </button>
  )
}
```

### router.reload

Reload the current URL. Equivalent to clicking the browser’s refresh button. It executes `window.location.reload()`.

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.reload()}>
      Click here to reload
    </button>
  )
}
```

### router.events

You can listen to different events happening inside the Next.js Router. Here's a list of supported events:

* `routeChangeStart(url, { shallow })` - Fires when a route starts to change
* `routeChangeComplete(url, { shallow })` - Fires when a route changed completely
* `routeChangeError(err, url, { shallow })` - Fires when there's an error when changing routes, or a route load is cancelled
  * `err.cancelled` - Indicates if the navigation was cancelled
* `beforeHistoryChange(url, { shallow })` - Fires before changing the browser's history
* `hashChangeStart(url, { shallow })` - Fires when the hash will change but not the page
* `hashChangeComplete(url, { shallow })` - Fires when the hash has changed but not the page

> **Good to know**: Here `url` is the URL shown in the browser, including the [`basePath`](/docs/app/api-reference/config/next-config-js/basePath.md).

For example, to listen to the router event `routeChangeStart`, open or create `pages/_app.js` and subscribe to the event, like so:

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

export default function MyApp({ Component, pageProps }) {
  const router = useRouter()

  useEffect(() => {
    const handleRouteChange = (url, { shallow }) => {
      console.log(
        `App is changing to ${url} ${
          shallow ? 'with' : 'without'
        } shallow routing`
      )
    }

    router.events.on('routeChangeStart', handleRouteChange)

    // If the component is unmounted, unsubscribe
    // from the event with the `off` method:
    return () => {
      router.events.off('routeChangeStart', handleRouteChange)
    }
  }, [router])

  return <Component {...pageProps} />
}
```

> We use a [Custom App](/docs/pages/building-your-application/routing/custom-app.md) (`pages/_app.js`) for this example to subscribe to the event because it's not unmounted on page navigations, but you can subscribe to router events on any component in your application.

Router events should be registered when a component mounts ([useEffect](https://react.dev/reference/react/useEffect) or [componentDidMount](https://react.dev/reference/react/Component#componentdidmount) / [componentWillUnmount](https://react.dev/reference/react/Component#componentwillunmount)) or imperatively when an event happens.

If a route load is cancelled (for example, by clicking two links rapidly in succession), `routeChangeError` will fire. And the passed `err` will contain a `cancelled` property set to `true`, as in the following example:

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

export default function MyApp({ Component, pageProps }) {
  const router = useRouter()

  useEffect(() => {
    const handleRouteChangeError = (err, url) => {
      if (err.cancelled) {
        console.log(`Route to ${url} was cancelled!`)
      }
    }

    router.events.on('routeChangeError', handleRouteChangeError)

    // If the component is unmounted, unsubscribe
    // from the event with the `off` method:
    return () => {
      router.events.off('routeChangeError', handleRouteChangeError)
    }
  }, [router])

  return <Component {...pageProps} />
}
```

## The `next/compat/router` export

This is the same `useRouter` hook, but can be used in both `app` and `pages` directories.

It differs from `next/router` in that it does not throw an error when the pages router is not mounted, and instead has a return type of `NextRouter | null`.
This allows developers to convert components to support running in both `app` and `pages` as they transition to the `app` router.

A component that previously looked like this:

```jsx
import { useRouter } from 'next/router'
const MyComponent = () => {
  const { isReady, query } = useRouter()
  // ...
}
```

Will error when converted over to `next/compat/router`, as `null` can not be destructured. Instead, developers will be able to take advantage of new hooks:

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/compat/router'
import { useSearchParams } from 'next/navigation'
const MyComponent = () => {
  const router = useRouter() // may be null or a NextRouter instance
  const searchParams = useSearchParams()
  useEffect(() => {
    if (router && !router.isReady) {
      return
    }
    // In `app/`, searchParams will be ready immediately with the values, in
    // `pages/` it will be available after the router is ready.
    const search = searchParams.get('search')
    // ...
  }, [router, searchParams])
  // ...
}
```

This component will now work in both `pages` and `app` directories. When the component is no longer used in `pages`, you can remove the references to the compat router:

```jsx
import { useSearchParams } from 'next/navigation'
const MyComponent = () => {
  const searchParams = useSearchParams()
  // As this component is only used in `app/`, the compat router can be removed.
  const search = searchParams.get('search')
  // ...
}
```

### Using `useRouter` outside of Next.js context in pages

Another specific use case is when rendering components outside of a Next.js application context, such as inside `getServerSideProps` on the `pages` directory. In this case, the compat router can be used to avoid errors:

```jsx
import { renderToString } from 'react-dom/server'
import { useRouter } from 'next/compat/router'
const MyComponent = () => {
  const router = useRouter() // may be null or a NextRouter instance
  // ...
}
export async function getServerSideProps() {
  const renderedComponent = renderToString(<MyComponent />)
  return {
    props: {
      renderedComponent,
    },
  }
}
```

## Potential ESLint errors

Certain methods accessible on the `router` object return a Promise. If you have the ESLint rule, [no-floating-promises](https://typescript-eslint.io/rules/no-floating-promises) enabled, consider disabling it either globally, or for the affected line.

If your application needs this rule, you should either `void` the promise – or use an `async` function, `await` the Promise, then void the function call. **This is not applicable when the method is called from inside an `onClick` handler**.

The affected methods are:

* `router.push`
* `router.replace`
* `router.prefetch`

### Potential solutions

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

// Here you would fetch and return the user
const useUser = () => ({ user: null, loading: false })

export default function Page() {
  const { user, loading } = useUser()
  const router = useRouter()

  useEffect(() => {
    // disable the linting on the next line - This is the cleanest solution
    // eslint-disable-next-line no-floating-promises
    router.push('/login')

    // void the Promise returned by router.push
    if (!(user || loading)) {
      void router.push('/login')
    }
    // or use an async function, await the Promise, then void the function call
    async function handleRouteChange() {
      if (!(user || loading)) {
        await router.push('/login')
      }
    }
    void handleRouteChange()
  }, [user, loading])

  return <p>Redirecting...</p>
}
```

## withRouter

If [`useRouter`](#router-object) is not the best fit for you, `withRouter` can also add the same [`router` object](#router-object) to any component.

### Usage

```jsx
import { withRouter } from 'next/router'

function Page({ router }) {
  return <p>{router.pathname}</p>
}

export default withRouter(Page)
```

### TypeScript

To use class components with `withRouter`, the component needs to accept a router prop:

```tsx
import React from 'react'
import { withRouter, NextRouter } from 'next/router'

interface WithRouterProps {
  router: NextRouter
}

interface MyComponentProps extends WithRouterProps {}

class MyComponent extends React.Component<MyComponentProps> {
  render() {
    return <p>{this.props.router.pathname}</p>
  }
}

export default withRouter(MyComponent)
```


--------------------------------------------------------------------------------
title: "userAgent"
description: "The userAgent helper extends the Web Request API with additional properties and methods to interact with the user agent object from the request."
source: "https://nextjs.org/docs/pages/api-reference/functions/userAgent"
--------------------------------------------------------------------------------

# userAgent

@router: Pages Router

The `userAgent` helper extends the [Web Request API](https://developer.mozilla.org/docs/Web/API/Request) with additional properties and methods to interact with the user agent object from the request.

```ts filename="proxy.ts" switcher
import { NextRequest, NextResponse, userAgent } from 'next/server'

export function proxy(request: NextRequest) {
  const url = request.nextUrl
  const { device } = userAgent(request)

  // device.type can be: 'mobile', 'tablet', 'console', 'smarttv',
  // 'wearable', 'embedded', or undefined (for desktop browsers)
  const viewport = device.type || 'desktop'

  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

```js filename="proxy.js" switcher
import { NextResponse, userAgent } from 'next/server'

export function proxy(request) {
  const url = request.nextUrl
  const { device } = userAgent(request)

  // device.type can be: 'mobile', 'tablet', 'console', 'smarttv',
  // 'wearable', 'embedded', or undefined (for desktop browsers)
  const viewport = device.type || 'desktop'

  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

## `isBot`

A boolean indicating whether the request comes from a known bot.

## `browser`

An object containing information about the browser used in the request.

* `name`: A string representing the browser's name, or `undefined` if not identifiable.
* `version`: A string representing the browser's version, or `undefined`.

## `device`

An object containing information about the device used in the request.

* `model`: A string representing the model of the device, or `undefined`.
* `type`: A string representing the type of the device, such as `console`, `mobile`, `tablet`, `smarttv`, `wearable`, `embedded`, or `undefined`.
* `vendor`: A string representing the vendor of the device, or `undefined`.

## `engine`

An object containing information about the browser's engine.

* `name`: A string representing the engine's name. Possible values include: `Amaya`, `Blink`, `EdgeHTML`, `Flow`, `Gecko`, `Goanna`, `iCab`, `KHTML`, `Links`, `Lynx`, `NetFront`, `NetSurf`, `Presto`, `Tasman`, `Trident`, `w3m`, `WebKit` or `undefined`.
* `version`: A string representing the engine's version, or `undefined`.

## `os`

An object containing information about the operating system.

* `name`: A string representing the name of the OS, or `undefined`.
* `version`: A string representing the version of the OS, or `undefined`.

## `cpu`

An object containing information about the CPU architecture.

* `architecture`: A string representing the architecture of the CPU. Possible values include: `68k`, `amd64`, `arm`, `arm64`, `armhf`, `avr`, `ia32`, `ia64`, `irix`, `irix64`, `mips`, `mips64`, `pa-risc`, `ppc`, `sparc`, `sparc64` or `undefined`


--------------------------------------------------------------------------------
title: "Configuration"
description: "Learn how to configure your Next.js application."
source: "https://nextjs.org/docs/pages/api-reference/config"
--------------------------------------------------------------------------------

# Configuration

@router: Pages Router



 - [next.config.js Options](/docs/pages/api-reference/config/next-config-js.md)
 - [TypeScript](/docs/pages/api-reference/config/typescript.md)
 - [ESLint](/docs/pages/api-reference/config/eslint.md)

--------------------------------------------------------------------------------
title: "next.config.js"
description: "Learn how to configure your application with next.config.js."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js"
--------------------------------------------------------------------------------

# next.config.js Options

@router: Pages Router

Next.js can be configured through a `next.config.js` file in the root of your project directory (for example, by `package.json`) with a default export.

```js filename="next.config.js"
// @ts-check

/** @type {import('next').NextConfig} */
const nextConfig = {
  /* config options here */
}

module.exports = nextConfig
```

## ECMAScript Modules

`next.config.js` is a regular Node.js module, not a JSON file. It gets used by the Next.js server and build phases, and it's not included in the browser build.

If you need [ECMAScript modules](https://nodejs.org/api/esm.html), you can use `next.config.mjs`:

```js filename="next.config.mjs"
// @ts-check

/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  /* config options here */
}

export default nextConfig
```

> **Good to know**: `next.config` with the `.cjs` or `.cts` extensions are currently **not** supported.

## Configuration as a Function

You can also use a function:

```js filename="next.config.mjs"
// @ts-check

export default (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Async Configuration

Since Next.js 12.1.0, you can use an async function:

```js filename="next.config.js"
// @ts-check

module.exports = async (phase, { defaultConfig }) => {
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    /* config options here */
  }
  return nextConfig
}
```

### Phase

`phase` is the current context in which the configuration is loaded. You can see the [available phases](https://github.com/vercel/next.js/blob/5e6b008b561caf2710ab7be63320a3d549474a5b/packages/next/shared/lib/constants.ts#L19-L23). Phases can be imported from `next/constants`:

```js filename="next.config.js"
// @ts-check

const { PHASE_DEVELOPMENT_SERVER } = require('next/constants')

module.exports = (phase, { defaultConfig }) => {
  if (phase === PHASE_DEVELOPMENT_SERVER) {
    return {
      /* development only config options here */
    }
  }

  return {
    /* config options for all phases except development here */
  }
}
```

## TypeScript

If you are using TypeScript in your project, you can use `next.config.ts` to use TypeScript in your configuration:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  /* config options here */
}

export default nextConfig
```

The commented lines are the place where you can put the configs allowed by `next.config.js`, which are [defined in this file](https://github.com/vercel/next.js/blob/canary/packages/next/src/server/config-shared.ts).

However, none of the configs are required, and it's not necessary to understand what each config does. Instead, search for the features you need to enable or modify in this section and they will show you what to do.

> Avoid using new JavaScript features not available in your target Node.js version. `next.config.js` will not be parsed by Webpack or Babel.

This page documents all the available configuration options:

## Unit Testing (experimental)

Starting in Next.js 15.1, the `next/experimental/testing/server` package contains utilities to help unit test `next.config.js` files.

The `unstable_getResponseFromNextConfig` function runs the [`headers`](/docs/app/api-reference/config/next-config-js/headers.md), [`redirects`](/docs/app/api-reference/config/next-config-js/redirects.md), and [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md) functions from `next.config.js` with the provided request information and returns `NextResponse` with the results of the routing.

> The response from `unstable_getResponseFromNextConfig` only considers `next.config.js` fields and does not consider proxy or filesystem routes, so the result in production may be different than the unit test.

```js
import {
  getRedirectUrl,
  unstable_getResponseFromNextConfig,
} from 'next/experimental/testing/server'

const response = await unstable_getResponseFromNextConfig({
  url: 'https://nextjs.org/test',
  nextConfig: {
    async redirects() {
      return [{ source: '/test', destination: '/test2', permanent: false }]
    },
  },
})
expect(response.status).toEqual(307)
expect(getRedirectUrl(response)).toEqual('https://nextjs.org/test2')
```

 - [experimental.adapterPath](/docs/pages/api-reference/config/next-config-js/adapterPath.md)
 - [allowedDevOrigins](/docs/pages/api-reference/config/next-config-js/allowedDevOrigins.md)
 - [assetPrefix](/docs/pages/api-reference/config/next-config-js/assetPrefix.md)
 - [basePath](/docs/pages/api-reference/config/next-config-js/basePath.md)
 - [bundlePagesRouterDependencies](/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies.md)
 - [compress](/docs/pages/api-reference/config/next-config-js/compress.md)
 - [crossOrigin](/docs/pages/api-reference/config/next-config-js/crossOrigin.md)
 - [devIndicators](/docs/pages/api-reference/config/next-config-js/devIndicators.md)
 - [distDir](/docs/pages/api-reference/config/next-config-js/distDir.md)
 - [env](/docs/pages/api-reference/config/next-config-js/env.md)
 - [exportPathMap](/docs/pages/api-reference/config/next-config-js/exportPathMap.md)
 - [generateBuildId](/docs/pages/api-reference/config/next-config-js/generateBuildId.md)
 - [generateEtags](/docs/pages/api-reference/config/next-config-js/generateEtags.md)
 - [headers](/docs/pages/api-reference/config/next-config-js/headers.md)
 - [httpAgentOptions](/docs/pages/api-reference/config/next-config-js/httpAgentOptions.md)
 - [images](/docs/pages/api-reference/config/next-config-js/images.md)
 - [isolatedDevBuild](/docs/pages/api-reference/config/next-config-js/isolatedDevBuild.md)
 - [onDemandEntries](/docs/pages/api-reference/config/next-config-js/onDemandEntries.md)
 - [optimizePackageImports](/docs/pages/api-reference/config/next-config-js/optimizePackageImports.md)
 - [output](/docs/pages/api-reference/config/next-config-js/output.md)
 - [pageExtensions](/docs/pages/api-reference/config/next-config-js/pageExtensions.md)
 - [poweredByHeader](/docs/pages/api-reference/config/next-config-js/poweredByHeader.md)
 - [productionBrowserSourceMaps](/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps.md)
 - [experimental.proxyClientMaxBodySize](/docs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize.md)
 - [reactStrictMode](/docs/pages/api-reference/config/next-config-js/reactStrictMode.md)
 - [redirects](/docs/pages/api-reference/config/next-config-js/redirects.md)
 - [rewrites](/docs/pages/api-reference/config/next-config-js/rewrites.md)
 - [serverExternalPackages](/docs/pages/api-reference/config/next-config-js/serverExternalPackages.md)
 - [trailingSlash](/docs/pages/api-reference/config/next-config-js/trailingSlash.md)
 - [transpilePackages](/docs/pages/api-reference/config/next-config-js/transpilePackages.md)
 - [turbopack](/docs/pages/api-reference/config/next-config-js/turbopack.md)
 - [typescript](/docs/pages/api-reference/config/next-config-js/typescript.md)
 - [urlImports](/docs/pages/api-reference/config/next-config-js/urlImports.md)
 - [useLightningcss](/docs/pages/api-reference/config/next-config-js/useLightningcss.md)
 - [webpack](/docs/pages/api-reference/config/next-config-js/webpack.md)
 - [webVitalsAttribution](/docs/pages/api-reference/config/next-config-js/webVitalsAttribution.md)

--------------------------------------------------------------------------------
title: "experimental.adapterPath"
description: "Configure a custom adapter for Next.js to hook into the build process with modifyConfig and onBuildComplete callbacks."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/adapterPath"
--------------------------------------------------------------------------------

# experimental.adapterPath

@router: Pages Router

Next.js provides an experimental API that allows you to create custom adapters to hook into the build process. This is useful for deployment platforms or custom build integrations that need to modify the Next.js configuration or process the build output.

## Configuration

To use an adapter, specify the path to your adapter module in `experimental.adapterPath`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    adapterPath: require.resolve('./my-adapter.js'),
  },
}

module.exports = nextConfig
```

## Creating an Adapter

An adapter is a module that exports an object implementing the `NextAdapter` interface:

```typescript
export interface NextAdapter {
  name: string
  modifyConfig?: (
    config: NextConfigComplete,
    ctx: {
      phase: PHASE_TYPE
    }
  ) => Promise<NextConfigComplete> | NextConfigComplete
  onBuildComplete?: (ctx: {
    routes: {
      headers: Array<ManifestHeaderRoute>
      redirects: Array<ManifestRedirectRoute>
      rewrites: {
        beforeFiles: Array<ManifestRewriteRoute>
        afterFiles: Array<ManifestRewriteRoute>
        fallback: Array<ManifestRewriteRoute>
      }
      dynamicRoutes: ReadonlyArray<ManifestRoute>
    }
    outputs: AdapterOutputs
    projectDir: string
    repoRoot: string
    distDir: string
    config: NextConfigComplete
    nextVersion: string
  }) => Promise<void> | void
}
```

### Basic Adapter Structure

Here's a minimal adapter example:

```js filename="my-adapter.js"
/** @type {import('next').NextAdapter} */
const adapter = {
  name: 'my-custom-adapter',

  async modifyConfig(config, { phase }) {
    // Modify the Next.js config based on the build phase
    if (phase === 'phase-production-build') {
      return {
        ...config,
        // Add your modifications
      }
    }
    return config
  },

  async onBuildComplete({
    routes,
    outputs,
    projectDir,
    repoRoot,
    distDir,
    config,
    nextVersion,
  }) {
    // Process the build output
    console.log('Build completed with', outputs.pages.length, 'pages')

    // Access different output types
    for (const page of outputs.pages) {
      console.log('Page:', page.pathname, 'at', page.filePath)
    }

    for (const apiRoute of outputs.pagesApi) {
      console.log('API Route:', apiRoute.pathname, 'at', apiRoute.filePath)
    }

    for (const appPage of outputs.appPages) {
      console.log('App Page:', appPage.pathname, 'at', appPage.filePath)
    }

    for (const prerender of outputs.prerenders) {
      console.log('Prerendered:', prerender.pathname)
    }
  },
}

module.exports = adapter
```

## API Reference

### `modifyConfig(config, context)`

Called for any CLI command that loads the next.config to allow modification of the configuration.

**Parameters:**

* `config`: The complete Next.js configuration object
* `context.phase`: The current build phase (see [phases](/docs/app/api-reference/config/next-config-js.md#phase))

**Returns:** The modified configuration object (can be async)

### `onBuildComplete(context)`

Called after the build process completes with detailed information about routes and outputs.

**Parameters:**

* `routes`: Object containing route manifests for headers, redirects, rewrites, and dynamic routes
  * `routes.headers`: Array of header route objects with `source`, `sourceRegex`, `headers`, `has`, `missing`, and optional `priority` fields
  * `routes.redirects`: Array of redirect route objects with `source`, `sourceRegex`, `destination`, `statusCode`, `has`, `missing`, and optional `priority` fields
  * `routes.rewrites`: Object with `beforeFiles`, `afterFiles`, and `fallback` arrays, each containing rewrite route objects with `source`, `sourceRegex`, `destination`, `has`, and `missing` fields
  * `routes.dynamicRoutes`: Array of dynamic route objects with `source`, `sourceRegex`, `destination`, `has`, and `missing` fields
* `outputs`: Detailed information about all build outputs organized by type
* `projectDir`: Absolute path to the Next.js project directory
* `repoRoot`: Absolute path to the detected repository root
* `distDir`: Absolute path to the build output directory
* `config`: The final Next.js configuration (with `modifyConfig` applied)
* `nextVersion`: Version of Next.js being used
* `buildId`: Unique identifier for the current build

## Output Types

The `outputs` object contains arrays of different output types:

### Pages (`outputs.pages`)

React pages from the `pages/` directory:

```typescript
{
  type: 'PAGES'
  id: string           // Route identifier
  filePath: string     // Path to the built file
  pathname: string     // URL pathname
  sourcePage: string   // Original source file path in pages/ directory
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>  // Traced dependencies (key: relative path from repo root, value: absolute path)
  wasmAssets?: Record<string, string>  // Bundled wasm files (key: name, value: absolute path)
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>  // Environment variables (edge runtime only)
  }
}
```

### API Routes (`outputs.pagesApi`)

API routes from `pages/api/`:

```typescript
{
  type: 'PAGES_API'
  id: string
  filePath: string
  pathname: string
  sourcePage: string   // Original relative source file path
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### App Pages (`outputs.appPages`)

React pages from the `app/` directory with `page.{js,ts,jsx,tsx}`:

```typescript
{
  type: 'APP_PAGE'
  id: string
  filePath: string
  pathname: string     // Includes .rsc suffix for RSC routes
  sourcePage: string   // Original relative source file path
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### App Routes (`outputs.appRoutes`)

API and metadata routes from `app/` with `route.{js,ts,jsx,tsx}`:

```typescript
{
  type: 'APP_ROUTE'
  id: string
  filePath: string
  pathname: string
  sourcePage: string
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
  }
}
```

### Prerenders (`outputs.prerenders`)

ISR-enabled routes and static prerenders:

```typescript
{
  type: 'PRERENDER'
  id: string
  pathname: string
  parentOutputId: string  // ID of the source page/route
  groupId: number        // Revalidation group identifier (prerenders with same groupId revalidate together)
  pprChain?: {
    headers: Record<string, string>  // PPR chain headers (e.g., 'x-nextjs-resume': '1')
  }
  parentFallbackMode?: 'blocking' | false | null  // Fallback mode from getStaticPaths
  fallback?: {
    filePath: string
    initialStatus?: number
    initialHeaders?: Record<string, string | string[]>
    initialExpiration?: number
    initialRevalidate?: number
    postponedState?: string  // PPR postponed state
  }
  config: {
    allowQuery?: string[]     // Allowed query parameters
    allowHeader?: string[]    // Allowed headers for ISR
    bypassFor?: RouteHas[]    // Cache bypass conditions
    renderingMode?: RenderingMode
    bypassToken?: string
  }
}
```

### Static Files (`outputs.staticFiles`)

Static assets and auto-statically optimized pages:

```typescript
{
  type: 'STATIC_FILE'
  id: string
  filePath: string
  pathname: string
}
```

### Middleware (`outputs.middleware`)

Middleware function (if present):

```typescript
{
  type: 'MIDDLEWARE'
  id: string
  filePath: string
  pathname: string      // Always '/_middleware'
  sourcePage: string    // Always 'middleware'
  runtime: 'nodejs' | 'edge'
  assets: Record<string, string>
  wasmAssets?: Record<string, string>
  config: {
    maxDuration?: number
    preferredRegion?: string | string[]
    env?: Record<string, string>
    matchers?: Array<{
      source: string
      sourceRegex: string
      has: RouteHas[] | undefined
      missing: RouteHas[] | undefined
    }>
  }
}
```

## Routes Information

The `routes` object in `onBuildComplete` provides complete routing information with processed patterns ready for deployment:

### Headers

Each header route includes:

* `source`: Original route pattern (e.g., `/about`)
* `sourceRegex`: Compiled regex for matching requests
* `headers`: Key-value pairs of headers to apply
* `has`: Optional conditions that must be met
* `missing`: Optional conditions that must not be met
* `priority`: Optional flag for internal routes

### Redirects

Each redirect route includes:

* `source`: Original route pattern
* `sourceRegex`: Compiled regex for matching
* `destination`: Target URL (can include captured groups)
* `statusCode`: HTTP status code (301, 302, 307, 308)
* `has`: Optional positive conditions
* `missing`: Optional negative conditions
* `priority`: Optional flag for internal routes

### Rewrites

Rewrites are categorized into three phases:

* `beforeFiles`: Checked before filesystem (including pages and public files)
* `afterFiles`: Checked after pages/public files but before dynamic routes
* `fallback`: Checked after all other routes

Each rewrite includes `source`, `sourceRegex`, `destination`, `has`, and `missing`.

### Dynamic Routes

Generated from dynamic route segments (e.g., `[slug]`, `[...path]`). Each includes:

* `source`: Route pattern
* `sourceRegex`: Compiled regex with named capture groups
* `destination`: Internal destination with parameter substitution
* `has`: Optional positive conditions
* `missing`: Optional negative conditions

## Use Cases

Common use cases for adapters include:

* **Deployment Platform Integration**: Automatically configure build outputs for specific hosting platforms
* **Asset Processing**: Transform or optimize build outputs
* **Monitoring Integration**: Collect build metrics and route information
* **Custom Bundling**: Package outputs in platform-specific formats
* **Build Validation**: Ensure outputs meet specific requirements
* **Route Generation**: Use processed route information to generate platform-specific routing configs


--------------------------------------------------------------------------------
title: "allowedDevOrigins"
description: "Use `allowedDevOrigins` to configure additional origins that can request the dev server."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins"
--------------------------------------------------------------------------------

# allowedDevOrigins

@router: Pages Router

Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default) you can use the `allowedDevOrigins` config option.

`allowedDevOrigins` allows you to set additional origins that can be used in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:

```js filename="next.config.js"
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```


--------------------------------------------------------------------------------
title: "assetPrefix"
description: "Learn how to use the assetPrefix config option to configure your CDN."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix"
--------------------------------------------------------------------------------

# assetPrefix

@router: Pages Router

> **Attention**: [Deploying to Vercel](/docs/pages/getting-started/deploying.md) automatically configures a global CDN for your Next.js project.
> You do not need to manually setup an Asset Prefix.

> **Good to know**: Next.js 9.5+ added support for a customizable [Base Path](/docs/app/api-reference/config/next-config-js/basePath.md), which is better
> suited for hosting your application on a sub-path like `/docs`.
> We do not suggest you use a custom Asset Prefix for this use case.

## Set up a CDN

To set up a [CDN](https://en.wikipedia.org/wiki/Content_delivery_network), you can set up an asset prefix and configure your CDN's origin to resolve to the domain that Next.js is hosted on.

Open `next.config.mjs` and add the `assetPrefix` config based on the [phase](/docs/app/api-reference/config/next-config-js.md#async-configuration):

```js filename="next.config.mjs"
// @ts-check
import { PHASE_DEVELOPMENT_SERVER } from 'next/constants'

export default (phase) => {
  const isDev = phase === PHASE_DEVELOPMENT_SERVER
  /**
   * @type {import('next').NextConfig}
   */
  const nextConfig = {
    assetPrefix: isDev ? undefined : 'https://cdn.mydomain.com',
  }
  return nextConfig
}
```

Next.js will automatically use your asset prefix for the JavaScript and CSS files it loads from the `/_next/` path (`.next/static/` folder). For example, with the above configuration, the following request for a JS chunk:

```
/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

Would instead become:

```
https://cdn.mydomain.com/_next/static/chunks/4b9b41aaa062cbbfeff4add70f256968c51ece5d.4d708494b3aed70c04f0.js
```

The exact configuration for uploading your files to a given CDN will depend on your CDN of choice. The only folder you need to host on your CDN is the contents of `.next/static/`, which should be uploaded as `_next/static/` as the above URL request indicates. **Do not upload the rest of your `.next/` folder**, as you should not expose your server code and other configuration to the public.

While `assetPrefix` covers requests to `_next/static`, it does not influence the following paths:

* Files in the [public](/docs/pages/api-reference/file-conventions/public-folder.md) folder; if you want to serve those assets over a CDN, you'll have to introduce the prefix yourself
* `/_next/data/` requests for `getServerSideProps` pages. These requests will always be made against the main domain since they're not static.
* `/_next/data/` requests for `getStaticProps` pages. These requests will always be made against the main domain to support [Incremental Static Generation](/docs/pages/guides/incremental-static-regeneration.md), even if you're not using it (for consistency).


--------------------------------------------------------------------------------
title: "basePath"
description: "Use `basePath` to deploy a Next.js application under a sub-path of a domain."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath"
--------------------------------------------------------------------------------

# basePath

@router: Pages Router

To deploy a Next.js application under a sub-path of a domain you can use the `basePath` config option.

`basePath` allows you to set a path prefix for the application. For example, to use `/docs` instead of `''` (an empty string, the default), open `next.config.js` and add the `basePath` config:

```js filename="next.config.js"
module.exports = {
  basePath: '/docs',
}
```

> **Good to know**: This value must be set at build time and cannot be changed without re-building as the value is inlined in the client-side bundles.

### Links

When linking to other pages using `next/link` and `next/router` the `basePath` will be automatically applied.

For example, using `/about` will automatically become `/docs/about` when `basePath` is set to `/docs`.

```js
export default function HomePage() {
  return (
    <>
      <Link href="/about">About Page</Link>
    </>
  )
}
```

Output html:

```html
<a href="/docs/about">About Page</a>
```

This makes sure that you don't have to change all links in your application when changing the `basePath` value.

### Images

When using the [`next/image`](/docs/pages/api-reference/components/image.md) component, you will need to add the `basePath` in front of `src`.

For example, using `/docs/me.png` will properly serve your image when `basePath` is set to `/docs`.

```jsx
import Image from 'next/image'

function Home() {
  return (
    <>
      <h1>My Homepage</h1>
      <Image
        src="/docs/me.png"
        alt="Picture of the author"
        width={500}
        height={500}
      />
      <p>Welcome to my homepage!</p>
    </>
  )
}

export default Home
```


--------------------------------------------------------------------------------
title: "bundlePagesRouterDependencies"
description: "Enable automatic dependency bundling for Pages Router"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies"
--------------------------------------------------------------------------------

# bundlePagesRouterDependencies

@router: Pages Router

Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```

Explicitly opt-out certain packages from being bundled using the [`serverExternalPackages`](/docs/pages/api-reference/config/next-config-js/serverExternalPackages.md) option.

## Version History

| Version   | Changes                                                                                                   |
| --------- | --------------------------------------------------------------------------------------------------------- |
| `v15.0.0` | Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies` |


--------------------------------------------------------------------------------
title: "compress"
description: "Next.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress"
--------------------------------------------------------------------------------

# compress

@router: Pages Router

By default, Next.js uses `gzip` to compress rendered content and static files when using `next start` or a custom server. This is an optimization for applications that do not have compression configured. If compression is *already* configured in your application via a custom server, Next.js will not add compression.

You can check if compression is enabled and which algorithm is used by looking at the [`Accept-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding) (browser accepted options) and [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) (currently used) headers in the response.

## Disabling compression

To disable **compression**, set the `compress` config option to `false`:

```js filename="next.config.js"
module.exports = {
  compress: false,
}
```

We **do not recommend disabling compression** unless you have compression configured on your server, as compression reduces bandwidth usage and improves the performance of your application. For example, you're using [nginx](https://nginx.org/) and want to switch to `brotli`, set the `compress` option to `false` to allow nginx to handle compression.


--------------------------------------------------------------------------------
title: "crossOrigin"
description: "Use the `crossOrigin` option to add a crossOrigin tag on the `script` tags generated by `next/script`."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin"
--------------------------------------------------------------------------------

# crossOrigin

@router: Pages Router

Use the `crossOrigin` option to add a [`crossOrigin` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin) in all `<script>` tags generated by the  [`next/script`](/docs/pages/guides/scripts.md) and [`next/head`](/docs/pages/api-reference/components/head.md)components, and define how cross-origin requests should be handled.

```js filename="next.config.js"
module.exports = {
  crossOrigin: 'anonymous',
}
```

## Options

* `'anonymous'`: Adds [`crossOrigin="anonymous"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#anonymous) attribute.
* `'use-credentials'`: Adds [`crossOrigin="use-credentials"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#use-credentials).


--------------------------------------------------------------------------------
title: "devIndicators"
description: "Configuration options for the on-screen indicator that gives context about the current route you're viewing during development."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators"
--------------------------------------------------------------------------------

# devIndicators

@router: Pages Router

`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.

```ts filename="Types"
  devIndicators: false | {
    position?: 'bottom-right'
    | 'bottom-left'
    | 'top-right'
    | 'top-left', // defaults to 'bottom-left',
  },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.

## Troubleshooting

### Indicator not marking a route as static

If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.

You can confirm if a route is [static](/docs/app/guides/caching.md#static-rendering) or [dynamic](/docs/app/guides/caching.md#dynamic-rendering) by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:

```bash filename="Build Output"
Route (app)
┌ ○ /_not-found
└ ƒ /products/[id]

○  (Static)   prerendered as static content
ƒ  (Dynamic)  server-rendered on demand
```

When exporting [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md) or [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md) from a page, it will be marked as dynamic.

## Version History

| Version   | Changes                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed.                                                             |
| `v15.2.0` | Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated. |
| `v15.0.0` | Static on-screen indicator added with `appIsrStatus` option.                                                                                        |


--------------------------------------------------------------------------------
title: "distDir"
description: "Set a custom build directory to use instead of the default .next directory."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir"
--------------------------------------------------------------------------------

# distDir

@router: Pages Router

You can specify a name to use for a custom build directory to use instead of `.next`.

Open `next.config.js` and add the `distDir` config:

```js filename="next.config.js"
module.exports = {
  distDir: 'build',
}
```

Now if you run `next build` Next.js will use `build` instead of the default `.next` folder.

> `distDir` **should not** leave your project directory. For example, `../build` is an **invalid** directory.


--------------------------------------------------------------------------------
title: "env"
description: "Learn to add and access environment variables in your Next.js application at build time."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/env"
--------------------------------------------------------------------------------

# env

@router: Pages Router

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](/docs/pages/guides/environment-variables.md). Give it a try!

> **Good to know**: environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](/docs/pages/guides/environment-variables.md).

To add environment variables to the JavaScript bundle, open `next.config.js` and add the `env` config:

```js filename="next.config.js"
module.exports = {
  env: {
    customKey: 'my-value',
  },
}
```

Now you can access `process.env.customKey` in your code. For example:

```jsx
function Page() {
  return <h1>The value of customKey is: {process.env.customKey}</h1>
}

export default Page
```

Next.js will replace `process.env.customKey` with `'my-value'` at build time. Trying to destructure `process.env` variables won't work due to the nature of webpack [DefinePlugin](https://webpack.js.org/plugins/define-plugin/).

For example, the following line:

```jsx
return <h1>The value of customKey is: {process.env.customKey}</h1>
```

Will end up being:

```jsx
return <h1>The value of customKey is: {'my-value'}</h1>
```


--------------------------------------------------------------------------------
title: "exportPathMap"
description: "Customize the pages that will be exported as HTML files when using `next export`."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap"
--------------------------------------------------------------------------------

# exportPathMap

@router: Pages Router

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

> This feature is exclusive to `next export` and currently **deprecated** in favor of `getStaticPaths` with `pages` or `generateStaticParams` with `app`.

`exportPathMap` allows you to specify a mapping of request paths to page destinations, to be used during export. Paths defined in `exportPathMap` will also be available when using [`next dev`](/docs/app/api-reference/cli/next.md#next-dev-options).

Let's start with an example, to create a custom `exportPathMap` for an app with the following pages:

* `pages/index.js`
* `pages/about.js`
* `pages/post.js`

Open `next.config.js` and add the following `exportPathMap` config:

```js filename="next.config.js"
module.exports = {
  exportPathMap: async function (
    defaultPathMap,
    { dev, dir, outDir, distDir, buildId }
  ) {
    return {
      '/': { page: '/' },
      '/about': { page: '/about' },
      '/p/hello-nextjs': { page: '/post', query: { title: 'hello-nextjs' } },
      '/p/learn-nextjs': { page: '/post', query: { title: 'learn-nextjs' } },
      '/p/deploy-nextjs': { page: '/post', query: { title: 'deploy-nextjs' } },
    }
  },
}
```

> **Good to know**: the `query` field in `exportPathMap` cannot be used with [automatically statically optimized pages](/docs/pages/building-your-application/rendering/automatic-static-optimization.md) or [`getStaticProps` pages](/docs/pages/building-your-application/data-fetching/get-static-props.md) as they are rendered to HTML files at build-time and additional query information cannot be provided during `next export`.

The pages will then be exported as HTML files, for example, `/about` will become `/about.html`.

`exportPathMap` is an `async` function that receives 2 arguments: the first one is `defaultPathMap`, which is the default map used by Next.js. The second argument is an object with:

* `dev` - `true` when `exportPathMap` is being called in development. `false` when running `next export`. In development `exportPathMap` is used to define routes.
* `dir` - Absolute path to the project directory
* `outDir` - Absolute path to the `out/` directory ([configurable with `-o`](#customizing-the-output-directory)). When `dev` is `true` the value of `outDir` will be `null`.
* `distDir` - Absolute path to the `.next/` directory (configurable with the [`distDir`](/docs/pages/api-reference/config/next-config-js/distDir.md) config)
* `buildId` - The generated build id

The returned object is a map of pages where the `key` is the `pathname` and the `value` is an object that accepts the following fields:

* `page`: `String` - the page inside the `pages` directory to render
* `query`: `Object` - the `query` object passed to `getInitialProps` when prerendering. Defaults to `{}`

> The exported `pathname` can also be a filename (for example, `/readme.md`), but you may need to set the `Content-Type` header to `text/html` when serving its content if it is different than `.html`.

## Adding a trailing slash

It is possible to configure Next.js to export pages as `index.html` files and require trailing slashes, `/about` becomes `/about/index.html` and is routable via `/about/`. This was the default behavior prior to Next.js 9.

To switch back and add a trailing slash, open `next.config.js` and enable the `trailingSlash` config:

```js filename="next.config.js"
module.exports = {
  trailingSlash: true,
}
```

## Customizing the output directory

[`next export`](/docs/pages/guides/static-exports.md) will use `out` as the default output directory, you can customize this using the `-o` argument, like so:

```bash filename="Terminal"
next export -o outdir
```

> **Warning**: Using `exportPathMap` is deprecated and is overridden by `getStaticPaths` inside `pages`. We don't recommend using them together.


--------------------------------------------------------------------------------
title: "generateBuildId"
description: "Configure the build id, which is used to identify the current build in which your application is being served."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId"
--------------------------------------------------------------------------------

# generateBuildId

@router: Pages Router

Next.js generates an ID during `next build` to identify which version of your application is being served. The same build should be used and boot up multiple containers.

If you are rebuilding for each stage of your environment, you will need to generate a consistent build ID to use between containers. Use the `generateBuildId` command in `next.config.js`:

```jsx filename="next.config.js"
module.exports = {
  generateBuildId: async () => {
    // This could be anything, using the latest git hash
    return process.env.GIT_HASH
  },
}
```


--------------------------------------------------------------------------------
title: "generateEtags"
description: "Next.js will generate etags for every page by default. Learn more about how to disable etag generation here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags"
--------------------------------------------------------------------------------

# generateEtags

@router: Pages Router

Next.js will generate [etags](https://en.wikipedia.org/wiki/HTTP_ETag) for every page by default. You may want to disable etag generation for HTML pages depending on your cache strategy.

Open `next.config.js` and disable the `generateEtags` option:

```js filename="next.config.js"
module.exports = {
  generateEtags: false,
}
```


--------------------------------------------------------------------------------
title: "headers"
description: "Add custom HTTP headers to your Next.js app."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers"
--------------------------------------------------------------------------------

# headers

@router: Pages Router

Headers allow you to set custom HTTP headers on the response to an incoming request on a given path.

To set custom HTTP headers you can use the `headers` key in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/about',
        headers: [
          {
            key: 'x-custom-header',
            value: 'my custom header value',
          },
          {
            key: 'x-another-custom-header',
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

`headers` is an async function that expects an array to be returned holding objects with `source` and `headers` properties:

* `source` is the incoming request path pattern.
* `headers` is an array of response header objects, with `key` and `value` properties.
* `basePath`: `false` or `undefined` - if false the basePath won't be included when matching, can be used for external rewrites only.
* `locale`: `false` or `undefined` - whether the locale should not be included when matching.
* `has` is an array of [has objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
* `missing` is an array of [missing objects](#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.

Headers are checked before the filesystem which includes pages and `/public` files.

## Header Overriding Behavior

If two headers match the same path and set the same header key, the last header key will override the first. Using the below headers, the path `/hello` will result in the header `x-hello` being `world` due to the last header value set being `world`.

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'x-hello',
            value: 'there',
          },
        ],
      },
      {
        source: '/hello',
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
    ]
  },
}
```

## Path Matching

Path matches are allowed, for example `/blog/:slug` will match `/blog/first-post` (no nested paths):

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/blog/:slug',
        headers: [
          {
            key: 'x-slug',
            value: ':slug', // Matched parameters can be used in the value
          },
          {
            key: 'x-slug-:slug', // Matched parameters can be used in the key
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

The pattern `/blog/:slug` matches `/blog/first-post` and `/blog/post-1` but not a nested path like `/blog/a/b`. Patterns are anchored to the start, `/blog/:slug` will not match `/archive/blog/first-post`.

You can use modifiers on parameters: `*` (zero or more), `+` (one or more), `?` (zero or one). For example, `/blog/:slug*` matches `/blog`, `/blog/a`, and `/blog/a/b/c`.

Read more details on [path-to-regexp](https://github.com/pillarjs/path-to-regexp) documentation.

### Wildcard Path Matching

To match a wildcard path you can use `*` after a parameter, for example `/blog/:slug*` will match `/blog/a/b/c/d/hello-world`:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/blog/:slug*',
        headers: [
          {
            key: 'x-slug',
            value: ':slug*', // Matched parameters can be used in the value
          },
          {
            key: 'x-slug-:slug*', // Matched parameters can be used in the key
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

### Regex Path Matching

To match a regex path you can wrap the regex in parenthesis after a parameter, for example `/blog/:slug(\\d{1,})` will match `/blog/123` but not `/blog/abc`:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/blog/:post(\\d{1,})',
        headers: [
          {
            key: 'x-post',
            value: ':post',
          },
        ],
      },
    ]
  },
}
```

The following characters `(`, `)`, `{`, `}`, `:`, `*`, `+`, `?` are used for regex path matching, so when used in the `source` as non-special values they must be escaped by adding `\\` before them:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        // this will match `/english(default)/something` being requested
        source: '/english\\(default\\)/:slug',
        headers: [
          {
            key: 'x-header',
            value: 'value',
          },
        ],
      },
    ]
  },
}
```

## Header, Cookie, and Query Matching

To only apply a header when header, cookie, or query values also match the `has` field or don't match the `missing` field can be used. Both the `source` and all `has` items must match and all `missing` items must not match for the header to be applied.

`has` and `missing` items can have the following fields:

* `type`: `String` - must be either `header`, `cookie`, `host`, or `query`.
* `key`: `String` - the key from the selected type to match against.
* `value`: `String` or `undefined` - the value to check for, if undefined any value will match. A regex like string can be used to capture a specific part of the value, e.g. if the value `first-(?<paramName>.*)` is used for `first-second` then `second` will be usable in the destination with `:paramName`.

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      // if the header `x-add-header` is present,
      // the `x-another-header` header will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'header',
            key: 'x-add-header',
          },
        ],
        headers: [
          {
            key: 'x-another-header',
            value: 'hello',
          },
        ],
      },
      // if the header `x-no-header` is not present,
      // the `x-another-header` header will be applied
      {
        source: '/:path*',
        missing: [
          {
            type: 'header',
            key: 'x-no-header',
          },
        ],
        headers: [
          {
            key: 'x-another-header',
            value: 'hello',
          },
        ],
      },
      // if the source, query, and cookie are matched,
      // the `x-authorized` header will be applied
      {
        source: '/specific/:path*',
        has: [
          {
            type: 'query',
            key: 'page',
            // the page value will not be available in the
            // header key/values since value is provided and
            // doesn't use a named capture group e.g. (?<page>home)
            value: 'home',
          },
          {
            type: 'cookie',
            key: 'authorized',
            value: 'true',
          },
        ],
        headers: [
          {
            key: 'x-authorized',
            value: ':authorized',
          },
        ],
      },
      // if the header `x-authorized` is present and
      // contains a matching value, the `x-another-header` will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'header',
            key: 'x-authorized',
            value: '(?<authorized>yes|true)',
          },
        ],
        headers: [
          {
            key: 'x-another-header',
            value: ':authorized',
          },
        ],
      },
      // if the host is `example.com`,
      // this header will be applied
      {
        source: '/:path*',
        has: [
          {
            type: 'host',
            value: 'example.com',
          },
        ],
        headers: [
          {
            key: 'x-another-header',
            value: ':authorized',
          },
        ],
      },
    ]
  },
}
```

## Headers with basePath support

When leveraging [`basePath` support](/docs/app/api-reference/config/next-config-js/basePath.md) with headers each `source` is automatically prefixed with the `basePath` unless you add `basePath: false` to the header:

```js filename="next.config.js"
module.exports = {
  basePath: '/docs',

  async headers() {
    return [
      {
        source: '/with-basePath', // becomes /docs/with-basePath
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
      {
        source: '/without-basePath', // is not modified since basePath: false is set
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
        basePath: false,
      },
    ]
  },
}
```

## Headers with i18n support

When leveraging [`i18n` support](/docs/pages/guides/internationalization.md) with headers each `source` is automatically prefixed to handle the configured `locales` unless you add `locale: false` to the header. If `locale: false` is used you must prefix the `source` with a locale for it to be matched correctly.

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['en', 'fr', 'de'],
    defaultLocale: 'en',
  },

  async headers() {
    return [
      {
        source: '/with-locale', // automatically handles all locales
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
      {
        // does not handle locales automatically since locale: false is set
        source: '/nl/with-locale-manual',
        locale: false,
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
      {
        // this matches '/' since `en` is the defaultLocale
        source: '/en',
        locale: false,
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
      {
        // this gets converted to /(en|fr|de)/(.*) so will not match the top-level
        // `/` or `/fr` routes like /:path* would
        source: '/(.*)',
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
    ]
  },
}
```

## Cache-Control

Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` for truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](/docs/app/getting-started/images.md#local-images). You cannot set `Cache-Control` headers in `next.config.js` for these assets.

However, you can set `Cache-Control` headers for other responses or data.

If you need to revalidate the cache of a page that has been [statically generated](/docs/pages/building-your-application/rendering/static-site-generation.md), you can do so by setting the `revalidate` prop in the page's [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) function.

To cache the response from an [API Route](/docs/pages/building-your-application/routing/api-routes.md), you can use `res.setHeader`:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.setHeader('Cache-Control', 's-maxage=86400')
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

```js filename="pages/api/hello.js" switcher
export default function handler(req, res) {
  res.setHeader('Cache-Control', 's-maxage=86400')
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

You can also use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/).

```ts filename="pages/index.tsx" switcher
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

// This value is considered fresh for ten seconds (s-maxage=10).
// If a request is repeated within the next 10 seconds, the previously
// cached value will still be fresh. If the request is repeated before 59 seconds,
// the cached value will be stale but still render (stale-while-revalidate=59).
//
// In the background, a revalidation request will be made to populate the cache
// with a fresh value. If you refresh the page, you will see the new value.
export const getServerSideProps = (async (context) => {
  context.res.setHeader(
    'Cache-Control',
    'public, s-maxage=10, stale-while-revalidate=59'
  )

  return {
    props: {},
  }
}) satisfies GetServerSideProps
```

```js filename="pages/index.js" switcher
// This value is considered fresh for ten seconds (s-maxage=10).
// If a request is repeated within the next 10 seconds, the previously
// cached value will still be fresh. If the request is repeated before 59 seconds,
// the cached value will be stale but still render (stale-while-revalidate=59).
//
// In the background, a revalidation request will be made to populate the cache
// with a fresh value. If you refresh the page, you will see the new value.
export async function getServerSideProps({ req, res }) {
  res.setHeader(
    'Cache-Control',
    'public, s-maxage=10, stale-while-revalidate=59'
  )

  return {
    props: {},
  }
}
```

## Options

### CORS

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS) is a security feature that allows you to control which sites can access your resources. You can set the `Access-Control-Allow-Origin` header to allow a specific origin to access your API Endpoints.

```js
async headers() {
    return [
      {
        source: "/api/:path*",
        headers: [
          {
            key: "Access-Control-Allow-Origin",
            value: "*", // Set your origin
          },
          {
            key: "Access-Control-Allow-Methods",
            value: "GET, POST, PUT, DELETE, OPTIONS",
          },
          {
            key: "Access-Control-Allow-Headers",
            value: "Content-Type, Authorization",
          },
        ],
      },
    ];
  },
```

### X-DNS-Prefetch-Control

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-DNS-Prefetch-Control) controls DNS prefetching, allowing browsers to proactively perform domain name resolution on external links, images, CSS, JavaScript, and more. This prefetching is performed in the background, so the [DNS](https://developer.mozilla.org/docs/Glossary/DNS) is more likely to be resolved by the time the referenced items are needed. This reduces latency when the user clicks a link.

```js
{
  key: 'X-DNS-Prefetch-Control',
  value: 'on'
}
```

### Strict-Transport-Security

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) informs browsers it should only be accessed using HTTPS, instead of using HTTP. Using the configuration below, all present and future subdomains will use HTTPS for a `max-age` of 2 years. This blocks access to pages or subdomains that can only be served over HTTP.

```js
{
  key: 'Strict-Transport-Security',
  value: 'max-age=63072000; includeSubDomains; preload'
}
```

### X-Frame-Options

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Frame-Options) indicates whether the site should be allowed to be displayed within an `iframe`. This can prevent against clickjacking attacks.

**This header has been superseded by CSP's `frame-ancestors` option**, which has better support in modern browsers (see [Content Security Policy](/docs/app/guides/content-security-policy.md) for configuration details).

```js
{
  key: 'X-Frame-Options',
  value: 'SAMEORIGIN'
}
```

### Permissions-Policy

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Permissions-Policy) allows you to control which features and APIs can be used in the browser. It was previously named `Feature-Policy`.

```js
{
  key: 'Permissions-Policy',
  value: 'camera=(), microphone=(), geolocation=(), browsing-topics=()'
}
```

### X-Content-Type-Options

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/X-Content-Type-Options) prevents the browser from attempting to guess the type of content if the `Content-Type` header is not explicitly set. This can prevent XSS exploits for websites that allow users to upload and share files.

For example, a user trying to download an image, but having it treated as a different `Content-Type` like an executable, which could be malicious. This header also applies to downloading browser extensions. The only valid value for this header is `nosniff`.

```js
{
  key: 'X-Content-Type-Options',
  value: 'nosniff'
}
```

### Referrer-Policy

[This header](https://developer.mozilla.org/docs/Web/HTTP/Headers/Referrer-Policy) controls how much information the browser includes when navigating from the current website (origin) to another.

```js
{
  key: 'Referrer-Policy',
  value: 'origin-when-cross-origin'
}
```

### Content-Security-Policy

Learn more about adding a [Content Security Policy](/docs/app/guides/content-security-policy.md) to your application.

## Version History

| Version   | Changes          |
| --------- | ---------------- |
| `v13.3.0` | `missing` added. |
| `v10.2.0` | `has` added.     |
| `v9.5.0`  | Headers added.   |


--------------------------------------------------------------------------------
title: "httpAgentOptions"
description: "Next.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here."
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions"
--------------------------------------------------------------------------------

# httpAgentOptions

@router: Pages Router

In Node.js versions prior to 18, Next.js automatically polyfills `fetch()` with [undici](/docs/architecture/supported-browsers.md#polyfills) and enables [HTTP Keep-Alive](https://developer.mozilla.org/docs/Web/HTTP/Headers/Keep-Alive) by default.

To disable HTTP Keep-Alive for all `fetch()` calls on the server-side, open `next.config.js` and add the `httpAgentOptions` config:

```js filename="next.config.js"
module.exports = {
  httpAgentOptions: {
    keepAlive: false,
  },
}
```


--------------------------------------------------------------------------------
title: "images"
description: "Custom configuration for the next/image loader"
source: "https://nextjs.org/docs/pages/api-reference/config/next-config-js/images"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./15-getstaticprops.md) | [Index](./index.md) | [Next →](./17-images.md)
