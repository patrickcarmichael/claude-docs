**Navigation:** [← Previous](./07-link-component.md) | [Index](./index.md) | [Next →](./09-generatemetadata.md)

---

# route.js

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

```ts filename="route.ts" switcher
export async function GET() {
  return Response.json({ message: 'Hello World' })
}
```

```js filename="route.js" switcher
export async function GET() {
  return Response.json({ message: 'Hello World' })
}
```

## Reference

### HTTP Methods

A **route** file allows you to create custom request handlers for a given route. The following [HTTP methods](https://developer.mozilla.org/docs/Web/HTTP/Methods) are supported: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`.

```ts filename="route.ts" switcher
export async function GET(request: Request) {}

export async function HEAD(request: Request) {}

export async function POST(request: Request) {}

export async function PUT(request: Request) {}

export async function DELETE(request: Request) {}

export async function PATCH(request: Request) {}

// If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
export async function OPTIONS(request: Request) {}
```

```js filename="route.js" switcher
export async function GET(request) {}

export async function HEAD(request) {}

export async function POST(request) {}

export async function PUT(request) {}

export async function DELETE(request) {}

export async function PATCH(request) {}

// If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
export async function OPTIONS(request) {}
```

### Parameters

#### `request` (optional)

The `request` object is a [NextRequest](/docs/app/api-reference/functions/next-request.md) object, which is an extension of the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) API. `NextRequest` gives you further control over the incoming request, including easily accessing `cookies` and an extended, parsed, URL object `nextUrl`.

```ts filename="route.ts" switcher
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const url = request.nextUrl
}
```

```js filename="route.js" switcher
export async function GET(request) {
  const url = request.nextUrl
}
```

#### `context` (optional)

* **`params`**: a promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) for the current route.

```ts filename="app/dashboard/[team]/route.ts" switcher
export async function GET(
  request: Request,
  { params }: { params: Promise<{ team: string }> }
) {
  const { team } = await params
}
```

```js filename="app/dashboard/[team]/route.js" switcher
export async function GET(request, { params }) {
  const { team } = await params
}
```

| Example                          | URL            | `params`                           |
| -------------------------------- | -------------- | ---------------------------------- |
| `app/dashboard/[team]/route.js`  | `/dashboard/1` | `Promise<{ team: '1' }>`           |
| `app/shop/[tag]/[item]/route.js` | `/shop/1/2`    | `Promise<{ tag: '1', item: '2' }>` |
| `app/blog/[...slug]/route.js`    | `/blog/1/2`    | `Promise<{ slug: ['1', '2'] }>`    |

### Route Context Helper

You can type the Route Handler context using `RouteContext` to get strongly typed `params` from a route literal. `RouteContext` is a globally available helper.

```ts filename="app/users/[id]/route.ts"
import type { NextRequest } from 'next/server'

export async function GET(_req: NextRequest, ctx: RouteContext<'/users/[id]'>) {
  const { id } = await ctx.params
  return Response.json({ id })
}
```

> **Good to know**
>
> * Types are generated during `next dev`, `next build` or `next typegen`.
> * After type generation, the `RouteContext` helper is globally available. It doesn't need to be imported.

## Examples

### Cookies

You can read or set cookies with [`cookies`](/docs/app/api-reference/functions/cookies.md) from `next/headers`.

```ts filename="route.ts" switcher
import { cookies } from 'next/headers'

export async function GET(request: NextRequest) {
  const cookieStore = await cookies()

  const a = cookieStore.get('a')
  const b = cookieStore.set('b', '1')
  const c = cookieStore.delete('c')
}
```

```js filename="route.js" switcher
import { cookies } from 'next/headers'

export async function GET(request) {
  const cookieStore = await cookies()

  const a = cookieStore.get('a')
  const b = cookieStore.set('b', '1')
  const c = cookieStore.delete('c')
}
```

Alternatively, you can return a new `Response` using the [`Set-Cookie`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie) header.

```ts filename="app/api/route.ts" switcher
import { cookies } from 'next/headers'

export async function GET(request: Request) {
  const cookieStore = await cookies()
  const token = cookieStore.get('token')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { 'Set-Cookie': `token=${token.value}` },
  })
}
```

```js filename="app/api/route.js" switcher
import { cookies } from 'next/headers'

export async function GET(request) {
  const cookieStore = await cookies()
  const token = cookieStore.get('token')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { 'Set-Cookie': `token=${token.value}` },
  })
}
```

You can also use the underlying Web APIs to read cookies from the request ([`NextRequest`](/docs/app/api-reference/functions/next-request.md)):

```ts filename="app/api/route.ts" switcher
import { type NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const token = request.cookies.get('token')
}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {
  const token = request.cookies.get('token')
}
```

### Headers

You can read headers with [`headers`](/docs/app/api-reference/functions/headers.md) from `next/headers`.

```ts filename="route.ts" switcher
import { headers } from 'next/headers'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const headersList = await headers()
  const referer = headersList.get('referer')
}
```

```js filename="route.js" switcher
import { headers } from 'next/headers'

export async function GET(request) {
  const headersList = await headers()
  const referer = headersList.get('referer')
}
```

This `headers` instance is read-only. To set headers, you need to return a new `Response` with new `headers`.

```ts filename="app/api/route.ts" switcher
import { headers } from 'next/headers'

export async function GET(request: Request) {
  const headersList = await headers()
  const referer = headersList.get('referer')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { referer: referer },
  })
}
```

```js filename="app/api/route.js" switcher
import { headers } from 'next/headers'

export async function GET(request) {
  const headersList = await headers()
  const referer = headersList.get('referer')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { referer: referer },
  })
}
```

You can also use the underlying Web APIs to read headers from the request ([`NextRequest`](/docs/app/api-reference/functions/next-request.md)):

```ts filename="app/api/route.ts" switcher
import { type NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const requestHeaders = new Headers(request.headers)
}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {
  const requestHeaders = new Headers(request.headers)
}
```

### Revalidating Cached Data

You can [revalidate cached data](/docs/app/guides/incremental-static-regeneration.md) using the `revalidate` route segment config option.

```ts filename="app/posts/route.ts" switcher
export const revalidate = 60

export async function GET() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()

  return Response.json(posts)
}
```

```js filename="app/posts/route.js" switcher
export const revalidate = 60

export async function GET() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()

  return Response.json(posts)
}
```

### Redirects

```ts filename="app/api/route.ts" switcher
import { redirect } from 'next/navigation'

export async function GET(request: Request) {
  redirect('https://nextjs.org/')
}
```

```js filename="app/api/route.js" switcher
import { redirect } from 'next/navigation'

export async function GET(request) {
  redirect('https://nextjs.org/')
}
```

### Dynamic Route Segments

Route Handlers can use [Dynamic Segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) to create request handlers from dynamic data.

```ts filename="app/items/[slug]/route.ts" switcher
export async function GET(
  request: Request,
  { params }: { params: Promise<{ slug: string }> }
) {
  const { slug } = await params // 'a', 'b', or 'c'
}
```

```js filename="app/items/[slug]/route.js" switcher
export async function GET(request, { params }) {
  const { slug } = await params // 'a', 'b', or 'c'
}
```

| Route                       | Example URL | `params`                 |
| --------------------------- | ----------- | ------------------------ |
| `app/items/[slug]/route.js` | `/items/a`  | `Promise<{ slug: 'a' }>` |
| `app/items/[slug]/route.js` | `/items/b`  | `Promise<{ slug: 'b' }>` |
| `app/items/[slug]/route.js` | `/items/c`  | `Promise<{ slug: 'c' }>` |

### URL Query Parameters

The request object passed to the Route Handler is a `NextRequest` instance, which includes [some additional convenience methods](/docs/app/api-reference/functions/next-request.md#nexturl), such as those for more easily handling query parameters.

```ts filename="app/api/search/route.ts" switcher
import { type NextRequest } from 'next/server'

export function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const query = searchParams.get('query')
  // query is "hello" for /api/search?query=hello
}
```

```js filename="app/api/search/route.js" switcher
export function GET(request) {
  const searchParams = request.nextUrl.searchParams
  const query = searchParams.get('query')
  // query is "hello" for /api/search?query=hello
}
```

### Streaming

Streaming is commonly used in combination with Large Language Models (LLMs), such as OpenAI, for AI-generated content. Learn more about the [AI SDK](https://sdk.vercel.ai/docs/introduction).

```ts filename="app/api/chat/route.ts" switcher
import { openai } from '@ai-sdk/openai'
import { StreamingTextResponse, streamText } from 'ai'

export async function POST(req: Request) {
  const { messages } = await req.json()
  const result = await streamText({
    model: openai('gpt-4-turbo'),
    messages,
  })

  return new StreamingTextResponse(result.toAIStream())
}
```

```js filename="app/api/chat/route.js" switcher
import { openai } from '@ai-sdk/openai'
import { StreamingTextResponse, streamText } from 'ai'

export async function POST(req) {
  const { messages } = await req.json()
  const result = await streamText({
    model: openai('gpt-4-turbo'),
    messages,
  })

  return new StreamingTextResponse(result.toAIStream())
}
```

These abstractions use the Web APIs to create a stream. You can also use the underlying Web APIs directly.

```ts filename="app/api/route.ts" switcher
// https://developer.mozilla.org/docs/Web/API/ReadableStream#convert_async_iterator_to_stream
function iteratorToStream(iterator: any) {
  return new ReadableStream({
    async pull(controller) {
      const { value, done } = await iterator.next()

      if (done) {
        controller.close()
      } else {
        controller.enqueue(value)
      }
    },
  })
}

function sleep(time: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, time)
  })
}

const encoder = new TextEncoder()

async function* makeIterator() {
  yield encoder.encode('<p>One</p>')
  await sleep(200)
  yield encoder.encode('<p>Two</p>')
  await sleep(200)
  yield encoder.encode('<p>Three</p>')
}

export async function GET() {
  const iterator = makeIterator()
  const stream = iteratorToStream(iterator)

  return new Response(stream)
}
```

```js filename="app/api/route.js" switcher
// https://developer.mozilla.org/docs/Web/API/ReadableStream#convert_async_iterator_to_stream
function iteratorToStream(iterator) {
  return new ReadableStream({
    async pull(controller) {
      const { value, done } = await iterator.next()

      if (done) {
        controller.close()
      } else {
        controller.enqueue(value)
      }
    },
  })
}

function sleep(time) {
  return new Promise((resolve) => {
    setTimeout(resolve, time)
  })
}

const encoder = new TextEncoder()

async function* makeIterator() {
  yield encoder.encode('<p>One</p>')
  await sleep(200)
  yield encoder.encode('<p>Two</p>')
  await sleep(200)
  yield encoder.encode('<p>Three</p>')
}

export async function GET() {
  const iterator = makeIterator()
  const stream = iteratorToStream(iterator)

  return new Response(stream)
}
```

### Request Body

You can read the `Request` body using the standard Web API methods:

```ts filename="app/items/route.ts" switcher
export async function POST(request: Request) {
  const res = await request.json()
  return Response.json({ res })
}
```

```js filename="app/items/route.js" switcher
export async function POST(request) {
  const res = await request.json()
  return Response.json({ res })
}
```

### Request Body FormData

You can read the `FormData` using the `request.formData()` function:

```ts filename="app/items/route.ts" switcher
export async function POST(request: Request) {
  const formData = await request.formData()
  const name = formData.get('name')
  const email = formData.get('email')
  return Response.json({ name, email })
}
```

```js filename="app/items/route.js" switcher
export async function POST(request) {
  const formData = await request.formData()
  const name = formData.get('name')
  const email = formData.get('email')
  return Response.json({ name, email })
}
```

Since `formData` data are all strings, you may want to use [`zod-form-data`](https://www.npmjs.com/zod-form-data) to validate the request and retrieve data in the format you prefer (e.g. `number`).

### CORS

You can set CORS headers for a specific Route Handler using the standard Web API methods:

```ts filename="app/api/route.ts" switcher
export async function GET(request: Request) {
  return new Response('Hello, Next.js!', {
    status: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  })
}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {
  return new Response('Hello, Next.js!', {
    status: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  })
}
```

> **Good to know**:
>
> * To add CORS headers to multiple Route Handlers, you can use [Proxy](/docs/app/api-reference/file-conventions/proxy.md#cors) or the [`next.config.js` file](/docs/app/api-reference/config/next-config-js/headers.md#cors).

### Webhooks

You can use a Route Handler to receive webhooks from third-party services:

```ts filename="app/api/route.ts" switcher
export async function POST(request: Request) {
  try {
    const text = await request.text()
    // Process the webhook payload
  } catch (error) {
    return new Response(`Webhook error: ${error.message}`, {
      status: 400,
    })
  }

  return new Response('Success!', {
    status: 200,
  })
}
```

```js filename="app/api/route.js" switcher
export async function POST(request) {
  try {
    const text = await request.text()
    // Process the webhook payload
  } catch (error) {
    return new Response(`Webhook error: ${error.message}`, {
      status: 400,
    })
  }

  return new Response('Success!', {
    status: 200,
  })
}
```

Notably, unlike API Routes with the Pages Router, you do not need to use `bodyParser` to use any additional configuration.

### Non-UI Responses

You can use Route Handlers to return non-UI content. Note that [`sitemap.xml`](/docs/app/api-reference/file-conventions/metadata/sitemap.md#generating-a-sitemap-using-code-js-ts), [`robots.txt`](/docs/app/api-reference/file-conventions/metadata/robots.md#generate-a-robots-file), [`app icons`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#generate-icons-using-code-js-ts-tsx), and [open graph images](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md) all have built-in support.

```ts filename="app/rss.xml/route.ts" switcher
export async function GET() {
  return new Response(
    `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Next.js Documentation</title>
  <link>https://nextjs.org/docs</link>
  <description>The React Framework for the Web</description>
</channel>

</rss>`,
    {
      headers: {
        'Content-Type': 'text/xml',
      },
    }
  )
}
```

```js filename="app/rss.xml/route.js" switcher
export async function GET() {
  return new Response(`<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Next.js Documentation</title>
  <link>https://nextjs.org/docs</link>
  <description>The React Framework for the Web</description>
</channel>

</rss>`)
}
```

### Segment Config Options

Route Handlers use the same [route segment configuration](/docs/app/api-reference/file-conventions/route-segment-config.md) as pages and layouts.

```ts filename="app/items/route.ts" switcher
export const dynamic = 'auto'
export const dynamicParams = true
export const revalidate = false
export const fetchCache = 'auto'
export const runtime = 'nodejs'
export const preferredRegion = 'auto'
```

```js filename="app/items/route.js" switcher
export const dynamic = 'auto'
export const dynamicParams = true
export const revalidate = false
export const fetchCache = 'auto'
export const runtime = 'nodejs'
export const preferredRegion = 'auto'
```

See the [API reference](/docs/app/api-reference/file-conventions/route-segment-config.md) for more details.

## Version History

| Version      | Changes                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------- |
| `v15.0.0-RC` | `context.params` is now a promise. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available |
| `v15.0.0-RC` | The default caching for `GET` handlers was changed from static to dynamic                            |
| `v13.2.0`    | Route Handlers are introduced.                                                                       |


--------------------------------------------------------------------------------
title: "Route Groups"
description: "Route Groups can be used to partition your Next.js application into different sections."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-groups"
--------------------------------------------------------------------------------

# Route Groups

Route Groups are a folder convention that let you organize routes by category or team.

## Convention

A route group can be created by wrapping a folder's name in parenthesis: `(folderName)`.

This convention indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![An example folder structure using route groups](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/project-organization-route-groups.png)

## Use cases

* Organizing routes by team, concern, or feature.
* Defining multiple [root layouts](/docs/app/api-reference/file-conventions/layout.md#root-layout).
* Opting specific route segments into sharing a layout, while keeping others out.

## Caveats

* **Full page load**: If you navigate between routes that use different root layouts, it'll trigger a full page reload. For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js`. This **only** applies to multiple root layouts.
* **Conflicting paths**: Routes in different groups should not resolve to the same URL path. For example, `(marketing)/about/page.js` and `(shop)/about/page.js` would both resolve to `/about` and cause an error.
* **Top-level root layout**: If you use multiple root layouts without a top-level `layout.js` file, make sure your home route (/) is defined within one of the route groups, e.g. app/(marketing)/page.js.


--------------------------------------------------------------------------------
title: "Route Segment Config"
description: "Learn about how to configure options for Next.js route segments."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config"
--------------------------------------------------------------------------------

# Route Segment Config

> **Good to know**:
>
> * The options outlined on this page are disabled if the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) flag is on, and will eventually be deprecated in the future.
> * Route Segment options only take effect in Server Component Pages, Layouts, or Route Handlers.
> * `generateStaticParams` cannot be used inside a `'use client'` file.

The Route Segment options allows you to configure the behavior of a [Page](/docs/app/api-reference/file-conventions/layout.md), [Layout](/docs/app/api-reference/file-conventions/layout.md), or [Route Handler](/docs/app/api-reference/file-conventions/route.md) by directly exporting the following variables:

| Option                                | Type                                                                                                                      | Default                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [`dynamic`](#dynamic)                 | `'auto' \| 'force-dynamic' \| 'error' \| 'force-static'`                                                                  | `'auto'`                   |
| [`dynamicParams`](#dynamicparams)     | `boolean`                                                                                                                 | `true`                     |
| [`revalidate`](#revalidate)           | `false \| 0 \| number`                                                                                                    | `false`                    |
| [`fetchCache`](#fetchcache)           | `'auto' \| 'default-cache' \| 'only-cache' \| 'force-cache' \| 'force-no-store' \| 'default-no-store' \| 'only-no-store'` | `'auto'`                   |
| [`runtime`](#runtime)                 | `'nodejs' \| 'edge'`                                                                                                      | `'nodejs'`                 |
| [`preferredRegion`](#preferredregion) | `'auto' \| 'global' \| 'home' \| string \| string[]`                                                                      | `'auto'`                   |
| [`maxDuration`](#maxduration)         | `number`                                                                                                                  | Set by deployment platform |

## Options

### `dynamic`

Change the dynamic behavior of a layout or page to fully static or fully dynamic.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const dynamic = 'auto'
// 'auto' | 'force-dynamic' | 'error' | 'force-static'
```

```js filename="layout.js | page.js | route.js" switcher
export const dynamic = 'auto'
// 'auto' | 'force-dynamic' | 'error' | 'force-static'
```

> **Good to know**: The new model in the `app` directory favors granular caching control at the `fetch` request level over the binary all-or-nothing model of `getServerSideProps` and `getStaticProps` at the page-level in the `pages` directory. The `dynamic` option is a way to opt back in to the previous model as a convenience and provides a simpler migration path.

* **`'auto'`** (default): The default option to cache as much as possible without preventing any components from opting into dynamic behavior.

* **`'force-dynamic'`**: Force [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering), which will result in routes being rendered for each user at request time. This option is equivalent to:
  * Setting the option of every `fetch()` request in a layout or page to `{ cache: 'no-store', next: { revalidate: 0 } }`.
  * Setting the segment config to `export const fetchCache = 'force-no-store'`

* **`'error'`**: Force static rendering and cache the data of a layout or page by causing an error if any components use [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) or uncached data. This option is equivalent to:
  * `getStaticProps()` in the `pages` directory.
  * Setting the option of every `fetch()` request in a layout or page to `{ cache: 'force-cache' }`.
  * Setting the segment config to `fetchCache = 'only-cache'`.

* **`'force-static'`**: Force static rendering and cache the data of a layout or page by forcing [`cookies`](/docs/app/api-reference/functions/cookies.md), [`headers()`](/docs/app/api-reference/functions/headers.md) and [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md) to return empty values. It is possible to [`revalidate`](#revalidate), [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md), or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md), in pages or layouts rendered with `force-static`.

> **Good to know**:
>
> * Instructions on [how to migrate](/docs/app/guides/migrating/app-router-migration.md#step-6-migrating-data-fetching-methods) from `getServerSideProps` and `getStaticProps` to `dynamic: 'force-dynamic'` and `dynamic: 'error'` can be found in the [upgrade guide](/docs/app/guides/migrating/app-router-migration.md#step-6-migrating-data-fetching-methods).

### `dynamicParams`

Control what happens when a dynamic segment is visited that was not generated with [generateStaticParams](/docs/app/api-reference/functions/generate-static-params.md).

```tsx filename="layout.tsx | page.tsx" switcher
export const dynamicParams = true // true | false
```

```js filename="layout.js | page.js | route.js" switcher
export const dynamicParams = true // true | false
```

* **`true`** (default): Dynamic segments not included in `generateStaticParams` are generated on demand.
* **`false`**: Dynamic segments not included in `generateStaticParams` will return a 404.

> **Good to know**:
>
> * This option replaces the `fallback: true | false | blocking` option of `getStaticPaths` in the `pages` directory.
> * To statically render all paths the first time they're visited, you'll need to return an empty array in `generateStaticParams` or utilize `export const dynamic = 'force-static'`.
> * When `dynamicParams = true`, the segment uses [Streaming Server Rendering](/docs/app/getting-started/linking-and-navigating.md#streaming).

### `revalidate`

Set the default revalidation time for a layout or page. This option does not override the `revalidate` value set by individual `fetch` requests.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const revalidate = false
// false | 0 | number
```

```js filename="layout.js | page.js | route.js" switcher
export const revalidate = false
// false | 0 | number
```

* **`false`** (default): The default heuristic to cache any `fetch` requests that set their `cache` option to `'force-cache'` or are discovered before a [Dynamic API](/docs/app/guides/caching.md#dynamic-rendering) is used. Semantically equivalent to `revalidate: Infinity` which effectively means the resource should be cached indefinitely. It is still possible for individual `fetch` requests to use `cache: 'no-store'` or `revalidate: 0` to avoid being cached and make the route dynamically rendered. Or set `revalidate` to a positive number lower than the route default to increase the revalidation frequency of a route.
* **`0`**: Ensure a layout or page is always [dynamically rendered](/docs/app/guides/caching.md#dynamic-rendering) even if no Dynamic APIs or uncached data fetches are discovered. This option changes the default of `fetch` requests that do not set a `cache` option to `'no-store'` but leaves `fetch` requests that opt into `'force-cache'` or use a positive `revalidate` as is.
* **`number`**: (in seconds) Set the default revalidation frequency of a layout or page to `n` seconds.

> **Good to know**:
>
> * The revalidate value needs to be statically analyzable. For example `revalidate = 600` is valid, but `revalidate = 60 * 10` is not.
> * The revalidate value is not available when using `runtime = 'edge'`.
> * In Development, Pages are *always* rendered on-demand and are never cached. This allows you to see changes immediately without waiting for a revalidation period to pass.

#### Revalidation Frequency

* The lowest `revalidate` across each layout and page of a single route will determine the revalidation frequency of the *entire* route. This ensures that child pages are revalidated as frequently as their parent layouts.
* Individual `fetch` requests can set a lower `revalidate` than the route's default `revalidate` to increase the revalidation frequency of the entire route. This allows you to dynamically opt-in to more frequent revalidation for certain routes based on some criteria.

### `fetchCache`

<details>
<summary>This is an advanced option that should only be used if you specifically need to override the default behavior.</summary>

By default, Next.js **will cache** any `fetch()` requests that are reachable **before** any [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) are used and **will not cache** `fetch` requests that are discovered **after** Dynamic APIs are used.

`fetchCache` allows you to override the default `cache` option of all `fetch` requests in a layout or page.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const fetchCache = 'auto'
// 'auto' | 'default-cache' | 'only-cache'
// 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'
```

```js filename="layout.js | page.js | route.js" switcher
export const fetchCache = 'auto'
// 'auto' | 'default-cache' | 'only-cache'
// 'force-cache' | 'force-no-store' | 'default-no-store' | 'only-no-store'
```

* **`'auto'`** (default): The default option to cache `fetch` requests before Dynamic APIs with the `cache` option they provide and not cache `fetch` requests after Dynamic APIs.
* **`'default-cache'`**: Allow any `cache` option to be passed to `fetch` but if no option is provided then set the `cache` option to `'force-cache'`. This means that even `fetch` requests after Dynamic APIs are considered static.
* **`'only-cache'`**: Ensure all `fetch` requests opt into caching by changing the default to `cache: 'force-cache'` if no option is provided and causing an error if any `fetch` requests use `cache: 'no-store'`.
* **`'force-cache'`**: Ensure all `fetch` requests opt into caching by setting the `cache` option of all `fetch` requests to `'force-cache'`.
* **`'default-no-store'`**: Allow any `cache` option to be passed to `fetch` but if no option is provided then set the `cache` option to `'no-store'`. This means that even `fetch` requests before Dynamic APIs are considered dynamic.
* **`'only-no-store'`**: Ensure all `fetch` requests opt out of caching by changing the default to `cache: 'no-store'` if no option is provided and causing an error if any `fetch` requests use `cache: 'force-cache'`
* **`'force-no-store'`**: Ensure all `fetch` requests opt out of caching by setting the `cache` option of all `fetch` requests to `'no-store'`. This forces all `fetch` requests to be re-fetched every request even if they provide a `'force-cache'` option.

#### Cross-route segment behavior

* Any options set across each layout and page of a single route need to be compatible with each other.
  * If both the `'only-cache'` and `'force-cache'` are provided, then `'force-cache'` wins. If both `'only-no-store'` and `'force-no-store'` are provided, then `'force-no-store'` wins. The force option changes the behavior across the route so a single segment with `'force-*'` would prevent any errors caused by `'only-*'`.
  * The intention of the `'only-*'` and `'force-*'` options is to guarantee the whole route is either fully static or fully dynamic. This means:
    * A combination of `'only-cache'` and `'only-no-store'` in a single route is not allowed.
    * A combination of `'force-cache'` and `'force-no-store'` in a single route is not allowed.
  * A parent cannot provide `'default-no-store'` if a child provides `'auto'` or `'*-cache'` since that could make the same fetch have different behavior.
* It is generally recommended to leave shared parent layouts as `'auto'` and customize the options where child segments diverge.

</details>

### `runtime`

We recommend using the Node.js runtime for rendering your application. This option cannot be used in [Proxy](/docs/app/api-reference/file-conventions/proxy.md).

> **Good to know**: Using `runtime: 'edge'` is **not supported** for Cache Components.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

```js filename="layout.js | page.js | route.js" switcher
export const runtime = 'nodejs'
// 'nodejs' | 'edge'
```

* **`'nodejs'`** (default)
* **`'edge'`**

### `preferredRegion`

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const preferredRegion = 'auto'
// 'auto' | 'global' | 'home' | ['iad1', 'sfo1']
```

```js filename="layout.js | page.js | route.js" switcher
export const preferredRegion = 'auto'
// 'auto' | 'global' | 'home' | ['iad1', 'sfo1']
```

Support for `preferredRegion`, and regions supported, is dependent on your deployment platform.

> **Good to know**:
>
> * If a `preferredRegion` is not specified, it will inherit the option of the nearest parent layout.
> * The root layout defaults to `all` regions.

### `maxDuration`

By default, Next.js does not limit the execution of server-side logic (rendering a page or handling an API).
Deployment platforms can use `maxDuration` from the Next.js build output to add specific execution limits.

**Note**: This setting requires Next.js `13.4.10` or higher.

```tsx filename="layout.tsx | page.tsx | route.ts" switcher
export const maxDuration = 5
```

```js filename="layout.js | page.js | route.js" switcher
export const maxDuration = 5
```

> **Good to know**:
>
> * If using [Server Actions](/docs/app/getting-started/updating-data.md), set the `maxDuration` at the page level to change the default timeout of all Server Actions used on the page.

### `generateStaticParams`

The `generateStaticParams` function can be used in combination with [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes.md) to define the list of route segment parameters that will be statically generated at build time instead of on-demand at request time.

See the [API reference](/docs/app/api-reference/functions/generate-static-params.md) for more details.

## Version History

| Version      |                                                                                                                                                                                                                |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0`    | `export const experimental_ppr = true` removed. A [codemod](/docs/app/guides/upgrading/codemods.md#remove-experimental_ppr-route-segment-config-from-app-router-pages-and-layouts) is available.                  |
| `v15.0.0-RC` | `export const runtime = "experimental-edge"` deprecated. A [codemod](/docs/app/guides/upgrading/codemods.md#transform-app-router-route-segment-config-runtime-value-from-experimental-edge-to-edge) is available. |


--------------------------------------------------------------------------------
title: "src Folder"
description: "Save pages under the `src` folder as an alternative to the root `pages` directory."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/src-folder"
--------------------------------------------------------------------------------

# src

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
title: "template.js"
description: "API Reference for the template.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/template"
--------------------------------------------------------------------------------

# template.js

A **template** file is similar to a [layout](/docs/app/getting-started/layouts-and-pages.md#creating-a-layout) in that it wraps a layout or page. Unlike layouts that persist across routes and maintain state, templates are given a unique key, meaning children Client Components reset their state on navigation.

They are useful when you need to:

* Resynchronize `useEffect` on navigation.
* Reset the state of a child Client Components on navigation. For example, an input field.
* To change default framework behavior. For example, Suspense boundaries inside layouts only show a fallback on first load, while templates show it on every navigation.

## Convention

A template can be defined by exporting a default React component from a `template.js` file. The component should accept a `children` prop.

![template.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/template-special-file.png)

```tsx filename="app/template.tsx" switcher
export default function Template({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

```jsx filename="app/template.js" switcher
export default function Template({ children }) {
  return <div>{children}</div>
}
```

In terms of nesting, `template.js` is rendered between a layout and its children. Here's a simplified output:

```jsx filename="Output"
<Layout>
  {/* Note that the template is given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

## Props

### `children` (required)

Template accepts a `children` prop.

```jsx filename="Output"
<Layout>
  {/* Note that the template is automatically given a unique key. */}
  <Template key={routeParam}>{children}</Template>
</Layout>
```

## Behavior

* **Server Components**: By default, templates are Server Components.
* **With navigation**: Templates receive a unique key for their own segment level. They remount when that segment (including its dynamic params) changes. Navigations within deeper segments do not remount higher-level templates. Search params do not trigger remounts.
* **State reset**: Any Client Component inside the template will reset its state on navigation.
* **Effect re-run**: Effects like `useEffect` will re-synchronize as the component remounts.
* **DOM reset**: DOM elements inside the template are fully recreated.

### Templates during navigation and remounting

This section illustrates how templates behave during navigation. It shows, step by step, which templates remount on each route change and why.

Using this project tree:

```
app
├── about
│   ├── page.tsx
├── blog
│   ├── [slug]
│   │   └── page.tsx
│   ├── page.tsx
│   └── template.tsx
├── layout.tsx
├── page.tsx
└── template.tsx
```

Starting at `/`, the React tree looks roughly like this.

> Note: The `key` values shown in the examples are illustrative, the values in your application may differ.

```jsx filename="Output"
<RootLayout>
  {/* app/template.tsx */}
  <Template key="/">
    <Page />
  </Template>
</RootLayout>
```

Navigating to `/about` (first segment changes), the root template key changes, it remounts:

```jsx filename="Output"
<RootLayout>
  {/* app/template.tsx */}
  <Template key="/about">
    <AboutPage />
  </Template>
</RootLayout>
```

Navigating to `/blog` (first segment changes), the root template key changes, it remounts and the blog-level template mounts:

```jsx filename="Output"
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    <Template key="/blog">
      <BlogIndexPage />
    </Template>
  </Template>
</RootLayout>
```

Navigating within the same first segment to `/blog/first-post` (child segment changes), the root template key doesn't change, but the blog-level template key changes, it remounts:

```jsx filename="Output"
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    {/* remounts because the child segment at this level changed */}
    <Template key="/blog/first-post">
      <BlogPostPage slug="first-post" />
    </Template>
  </Template>
</RootLayout>
```

Navigating to `/blog/second-post` (same first segment, different child segment), the root template key doesn't change, but the blog-level template key changes, it remounts again:

```jsx filename="Output"
<RootLayout>
  {/* app/template.tsx (root) */}
  <Template key="/blog">
    {/* app/blog/template.tsx */}
    {/* remounts again due to changed child segment */}
    <Template key="/blog/second-post">
      <BlogPostPage slug="second-post" />
    </Template>
  </Template>
</RootLayout>
```

## Version History

| Version   | Changes                |
| --------- | ---------------------- |
| `v13.0.0` | `template` introduced. |


--------------------------------------------------------------------------------
title: "unauthorized.js"
description: "API reference for the unauthorized.js special file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized"
--------------------------------------------------------------------------------

# unauthorized.js

> This feature is currently experimental and subject to change, it is not recommended for production.

The **unauthorized** file is used to render UI when the [`unauthorized`](/docs/app/api-reference/functions/unauthorized.md) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `401` status code.

```tsx filename="app/unauthorized.tsx" switcher
import Login from '@/app/components/Login'

export default function Unauthorized() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

```jsx filename="app/unauthorized.js" switcher
import Login from '@/app/components/Login'

export default function Unauthorized() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

## Reference

### Props

`unauthorized.js` components do not accept any props.

## Examples

### Displaying login UI to unauthenticated users

You can use [`unauthorized`](/docs/app/api-reference/functions/unauthorized.md) function to render the `unauthorized.js` file with a login UI.

```tsx filename="app/dashboard/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  return <div>Dashboard</div>
}
```

```jsx filename="app/dashboard/page.js" switcher
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  return <div>Dashboard</div>
}
```

```tsx filename="app/unauthorized.tsx" switcher
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

```jsx filename="app/unauthorized.js" switcher
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

## Version History

| Version   | Changes                       |
| --------- | ----------------------------- |
| `v15.1.0` | `unauthorized.js` introduced. |
- [unauthorized](/docs/app/api-reference/functions/unauthorized.md)
  - API Reference for the unauthorized function.


--------------------------------------------------------------------------------
title: "Metadata Files API Reference"
description: "API documentation for the metadata file conventions."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata"
--------------------------------------------------------------------------------

# Metadata Files

This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.

Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).

Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.

> **Good to know**:
>
> * Special Route Handlers like [`sitemap.ts`](/docs/app/api-reference/file-conventions/metadata/sitemap.md), [`opengraph-image.tsx`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md), and [`icon.tsx`](/docs/app/api-reference/file-conventions/metadata/app-icons.md), and other [metadata files](/docs/app/api-reference/file-conventions/metadata.md) are cached by default.
> * If using along with [`proxy.ts`](/docs/app/api-reference/file-conventions/proxy.md), [configure the matcher](/docs/app/api-reference/file-conventions/proxy.md#matcher) to exclude the metadata files.

 - [favicon, icon, and apple-icon](/docs/app/api-reference/file-conventions/metadata/app-icons.md)
 - [manifest.json](/docs/app/api-reference/file-conventions/metadata/manifest.md)
 - [opengraph-image and twitter-image](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md)
 - [robots.txt](/docs/app/api-reference/file-conventions/metadata/robots.md)
 - [sitemap.xml](/docs/app/api-reference/file-conventions/metadata/sitemap.md)

--------------------------------------------------------------------------------
title: "favicon, icon, and apple-icon"
description: "API Reference for the Favicon, Icon and Apple Icon file conventions."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons"
--------------------------------------------------------------------------------

# favicon, icon, and apple-icon

The `favicon`, `icon`, or `apple-icon` file conventions allow you to set icons for your application.

They are useful for adding app icons that appear in places like web browser tabs, phone home screens, and search engine results.

There are two ways to set app icons:

* [Using image files (.ico, .jpg, .png)](#image-files-ico-jpg-png)
* [Using code to generate an icon (.js, .ts, .tsx)](#generate-icons-using-code-js-ts-tsx)

## Image files (.ico, .jpg, .png)

Use an image file to set an app icon by placing a `favicon`, `icon`, or `apple-icon` image file within your `/app` directory.
The `favicon` image can only be located in the top level of `app/`.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.

| File convention             | Supported file types                    | Valid locations |
| --------------------------- | --------------------------------------- | --------------- |
| [`favicon`](#favicon)       | `.ico`                                  | `app/`          |
| [`icon`](#icon)             | `.ico`, `.jpg`, `.jpeg`, `.png`, `.svg` | `app/**/*`      |
| [`apple-icon`](#apple-icon) | `.jpg`, `.jpeg`, `.png`                 | `app/**/*`      |

### `favicon`

Add a `favicon.ico` image file to the root `/app` route segment.

```html filename="<head> output"
<link rel="icon" href="/favicon.ico" sizes="any" />
```

### `icon`

Add an `icon.(ico|jpg|jpeg|png|svg)` image file.

```html filename="<head> output"
<link
  rel="icon"
  href="/icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

### `apple-icon`

Add an `apple-icon.(jpg|jpeg|png)` image file.

```html filename="<head> output"
<link
  rel="apple-touch-icon"
  href="/apple-icon?<generated>"
  type="image/<generated>"
  sizes="<generated>"
/>
```

> **Good to know**:
>
> * You can set multiple icons by adding a number suffix to the file name. For example, `icon1.png`, `icon2.png`, etc. Numbered files will sort lexically.
> * Favicons can only be set in the root `/app` segment. If you need more granularity, you can use [`icon`](#icon).
> * The appropriate `<link>` tags and attributes such as `rel`, `href`, `type`, and `sizes` are determined by the icon type and metadata of the evaluated file.
> * For example, a 32 by 32px `.png` file will have `type="image/png"` and `sizes="32x32"` attributes.
> * `sizes="any"` is added to icons when the extension is `.svg` or the image size of the file is not determined. More details in this [favicon handbook](https://evilmartians.com/chronicles/how-to-favicon-in-2021-six-files-that-fit-most-needs).

## Generate icons using code (.js, .ts, .tsx)

In addition to using [literal image files](#image-files-ico-jpg-png), you can programmatically **generate** icons using code.

Generate an app icon by creating an `icon` or `apple-icon` route that default exports a function.

| File convention | Supported file types |
| --------------- | -------------------- |
| `icon`          | `.js`, `.ts`, `.tsx` |
| `apple-icon`    | `.js`, `.ts`, `.tsx` |

The easiest way to generate an icon is to use the [`ImageResponse`](/docs/app/api-reference/functions/image-response.md) API from `next/og`.

```tsx filename="app/icon.tsx" switcher
import { ImageResponse } from 'next/og'

// Image metadata
export const size = {
  width: 32,
  height: 32,
}
export const contentType = 'image/png'

// Image generation
export default function Icon() {
  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 24,
          background: 'black',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
        }}
      >
        A
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported icons size metadata
      // config to also set the ImageResponse's width and height.
      ...size,
    }
  )
}
```

```jsx filename="app/icon.js" switcher
import { ImageResponse } from 'next/og'

// Image metadata
export const size = {
  width: 32,
  height: 32,
}
export const contentType = 'image/png'

// Image generation
export default function Icon() {
  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 24,
          background: 'black',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
        }}
      >
        A
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported icons size metadata
      // config to also set the ImageResponse's width and height.
      ...size,
    }
  )
}
```

```html filename="<head> output"
<link rel="icon" href="/icon?<generated>" type="image/png" sizes="32x32" />
```

> **Good to know**:
>
> * By default, generated icons are [**statically optimized**](/docs/app/guides/caching.md#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) or uncached data.
> * You can generate multiple icons in the same file using [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata.md).
> * You cannot generate a `favicon` icon. Use [`icon`](#icon) or a [favicon.ico](#favicon) file instead.
> * App icons are special Route Handlers that are cached by default unless they use a [Dynamic API](/docs/app/guides/caching.md#dynamic-apis) or [dynamic config](/docs/app/guides/caching.md#segment-config-options) option.

### Props

The default export function receives the following props:

#### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) object from the root segment down to the segment `icon` or `apple-icon` is colocated in.

> **Good to know**: If you use [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata.md), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.

```tsx filename="app/shop/[slug]/icon.tsx" switcher
export default async function Icon({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

```jsx filename="app/shop/[slug]/icon.js" switcher
export default async function Icon({ params }) {
  const { slug } = await params
  // ...
}
```

| Route                           | URL         | `params`                           |
| ------------------------------- | ----------- | ---------------------------------- |
| `app/shop/icon.js`              | `/shop`     | `undefined`                        |
| `app/shop/[slug]/icon.js`       | `/shop/1`   | `Promise<{ slug: '1' }>`           |
| `app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>` |

### Returns

The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.

> **Good to know**: `ImageResponse` satisfies this return type.

### Config exports

You can optionally configure the icon's metadata by exporting `size` and `contentType` variables from the `icon` or `apple-icon` route.

| Option                        | Type                                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [`size`](#size)               | `{ width: number; height: number }`                                                                             |
| [`contentType`](#contenttype) | `string` - [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types) |

#### `size`

```tsx filename="icon.tsx | apple-icon.tsx" switcher
export const size = { width: 32, height: 32 }

export default function Icon() {}
```

```jsx filename="icon.js | apple-icon.js" switcher
export const size = { width: 32, height: 32 }

export default function Icon() {}
```

```html filename="<head> output"
<link rel="icon" sizes="32x32" />
```

#### `contentType`

```tsx filename="icon.tsx | apple-icon.tsx" switcher
export const contentType = 'image/png'

export default function Icon() {}
```

```jsx filename="icon.js | apple-icon.js" switcher
export const contentType = 'image/png'

export default function Icon() {}
```

```html filename="<head> output"
<link rel="icon" type="image/png" />
```

#### Route Segment Config

`icon` and `apple-icon` are specialized [Route Handlers](/docs/app/api-reference/file-conventions/route.md) that can use the same [route segment configuration](/docs/app/api-reference/file-conventions/route-segment-config.md) options as Pages and Layouts.

## Version History

| Version   | Changes                                              |
| --------- | ---------------------------------------------------- |
| `v16.0.0` | `params` is now a promise that resolves to an object |
| `v13.3.0` | `favicon` `icon` and `apple-icon` introduced         |


--------------------------------------------------------------------------------
title: "manifest.json"
description: "API Reference for manifest.json file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest"
--------------------------------------------------------------------------------

# manifest.json

Add or generate a `manifest.(json|webmanifest)` file that matches the [Web Manifest Specification](https://developer.mozilla.org/docs/Web/Manifest) in the **root** of `app` directory to provide information about your web application for the browser.

## Static Manifest file

```json filename="app/manifest.json | app/manifest.webmanifest"
{
  "name": "My Next.js Application",
  "short_name": "Next.js App",
  "description": "An application built with Next.js",
  "start_url": "/"
  // ...
}
```

## Generate a Manifest file

Add a `manifest.js` or `manifest.ts` file that returns a [`Manifest` object](#manifest-object).

> Good to know: `manifest.js` is special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/guides/caching.md#dynamic-apis) or [dynamic config](/docs/app/guides/caching.md#segment-config-options) option.

```ts filename="app/manifest.ts" switcher
import type { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js App',
    short_name: 'Next.js App',
    description: 'Next.js App',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}
```

```js filename="app/manifest.js" switcher
export default function manifest() {
  return {
    name: 'Next.js App',
    short_name: 'Next.js App',
    description: 'Next.js App',
    start_url: '/',
    display: 'standalone',
    background_color: '#fff',
    theme_color: '#fff',
    icons: [
      {
        src: '/favicon.ico',
        sizes: 'any',
        type: 'image/x-icon',
      },
    ],
  }
}
```

### Manifest Object

The manifest object contains an extensive list of options that may be updated due to new web standards. For information on all the current options, refer to the `MetadataRoute.Manifest` type in your code editor if using [TypeScript](/docs/app/api-reference/config/typescript.md#ide-plugin) or see the [MDN](https://developer.mozilla.org/docs/Web/Manifest) docs.


--------------------------------------------------------------------------------
title: "opengraph-image and twitter-image"
description: "API Reference for the Open Graph Image and Twitter Image file conventions."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image"
--------------------------------------------------------------------------------

# opengraph-image and twitter-image

The `opengraph-image` and `twitter-image` file conventions allow you to set Open Graph and Twitter images for a route segment.

They are useful for setting the images that appear on social networks and messaging apps when a user shares a link to your site.

There are two ways to set Open Graph and Twitter images:

* [Using image files (.jpg, .png, .gif)](#image-files-jpg-png-gif)
* [Using code to generate images (.js, .ts, .tsx)](#generate-images-using-code-js-ts-tsx)

## Image files (.jpg, .png, .gif)

Use an image file to set a route segment's shared image by placing an `opengraph-image` or `twitter-image` image file in the segment.

Next.js will evaluate the file and automatically add the appropriate tags to your app's `<head>` element.

| File convention                                 | Supported file types            |
| ----------------------------------------------- | ------------------------------- |
| [`opengraph-image`](#opengraph-image)           | `.jpg`, `.jpeg`, `.png`, `.gif` |
| [`twitter-image`](#twitter-image)               | `.jpg`, `.jpeg`, `.png`, `.gif` |
| [`opengraph-image.alt`](#opengraph-imagealttxt) | `.txt`                          |
| [`twitter-image.alt`](#twitter-imagealttxt)     | `.txt`                          |

> **Good to know**:
>
> The `twitter-image` file size must not exceed [5MB](https://developer.x.com/en/docs/x-for-websites/cards/overview/summary), and the `opengraph-image` file size must not exceed [8MB](https://developers.facebook.com/docs/sharing/webmasters/images). If the image file size exceeds these limits, the build will fail.

### `opengraph-image`

Add an `opengraph-image.(jpg|jpeg|png|gif)` image file to any route segment.

```html filename="<head> output"
<meta property="og:image" content="<generated>" />
<meta property="og:image:type" content="<generated>" />
<meta property="og:image:width" content="<generated>" />
<meta property="og:image:height" content="<generated>" />
```

### `twitter-image`

Add a `twitter-image.(jpg|jpeg|png|gif)` image file to any route segment.

```html filename="<head> output"
<meta name="twitter:image" content="<generated>" />
<meta name="twitter:image:type" content="<generated>" />
<meta name="twitter:image:width" content="<generated>" />
<meta name="twitter:image:height" content="<generated>" />
```

### `opengraph-image.alt.txt`

Add an accompanying `opengraph-image.alt.txt` file in the same route segment as the `opengraph-image.(jpg|jpeg|png|gif)` image it's alt text.

```txt filename="opengraph-image.alt.txt"
About Acme
```

```html filename="<head> output"
<meta property="og:image:alt" content="About Acme" />
```

### `twitter-image.alt.txt`

Add an accompanying `twitter-image.alt.txt` file in the same route segment as the `twitter-image.(jpg|jpeg|png|gif)` image it's alt text.

```txt filename="twitter-image.alt.txt"
About Acme
```

```html filename="<head> output"
<meta property="twitter:image:alt" content="About Acme" />
```

## Generate images using code (.js, .ts, .tsx)

In addition to using [literal image files](#image-files-jpg-png-gif), you can programmatically **generate** images using code.

Generate a route segment's shared image by creating an `opengraph-image` or `twitter-image` route that default exports a function.

| File convention   | Supported file types |
| ----------------- | -------------------- |
| `opengraph-image` | `.js`, `.ts`, `.tsx` |
| `twitter-image`   | `.js`, `.ts`, `.tsx` |

> **Good to know**:
>
> * By default, generated images are [**statically optimized**](/docs/app/guides/caching.md#static-rendering) (generated at build time and cached) unless they use [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) or uncached data.
> * You can generate multiple Images in the same file using [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata.md).
> * `opengraph-image.js` and `twitter-image.js` are special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/guides/caching.md#dynamic-apis) or [dynamic config](/docs/app/guides/caching.md#segment-config-options) option.

The easiest way to generate an image is to use the [ImageResponse](/docs/app/api-reference/functions/image-response.md) API from `next/og`.

```tsx filename="app/about/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'
import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

// Image metadata
export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
  // Font loading, process.cwd() is Next.js project directory
  const interSemiBold = await readFile(
    join(process.cwd(), 'assets/Inter-SemiBold.ttf')
  )

  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        About Acme
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported opengraph-image
      // size config to also set the ImageResponse's width and height.
      ...size,
      fonts: [
        {
          name: 'Inter',
          data: interSemiBold,
          style: 'normal',
          weight: 400,
        },
      ],
    }
  )
}
```

```jsx filename="app/about/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'
import { readFile } from 'node:fs/promises'
import { join } from 'node:path'

// Image metadata
export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}

export const contentType = 'image/png'

// Image generation
export default async function Image() {
  // Font loading, process.cwd() is Next.js project directory
  const interSemiBold = await readFile(
    join(process.cwd(), 'assets/Inter-SemiBold.ttf')
  )

  return new ImageResponse(
    (
      // ImageResponse JSX element
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        About Acme
      </div>
    ),
    // ImageResponse options
    {
      // For convenience, we can re-use the exported opengraph-image
      // size config to also set the ImageResponse's width and height.
      ...size,
      fonts: [
        {
          name: 'Inter',
          data: interSemiBold,
          style: 'normal',
          weight: 400,
        },
      ],
    }
  )
}
```

```html filename="<head> output"
<meta property="og:image" content="<generated>" />
<meta property="og:image:alt" content="About Acme" />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

### Props

The default export function receives the following props:

#### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) object from the root segment down to the segment `opengraph-image` or `twitter-image` is colocated in.

> **Good to know**: If you use [`generateImageMetadata`](/docs/app/api-reference/functions/generate-image-metadata.md), the function will also receive an `id` prop that is a promise resolving to the `id` value from one of the items returned by `generateImageMetadata`.

```tsx filename="app/shop/[slug]/opengraph-image.tsx" switcher
export default async function Image({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

```jsx filename="app/shop/[slug]/opengraph-image.js" switcher
export default async function Image({ params }) {
  const { slug } = await params
  // ...
}
```

| Route                                      | URL         | `params`                           |
| ------------------------------------------ | ----------- | ---------------------------------- |
| `app/shop/opengraph-image.js`              | `/shop`     | `undefined`                        |
| `app/shop/[slug]/opengraph-image.js`       | `/shop/1`   | `Promise<{ slug: '1' }>`           |
| `app/shop/[tag]/[item]/opengraph-image.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>` |

### Returns

The default export function should return a `Blob` | `ArrayBuffer` | `TypedArray` | `DataView` | `ReadableStream` | `Response`.

> **Good to know**: `ImageResponse` satisfies this return type.

### Config exports

You can optionally configure the image's metadata by exporting `alt`, `size`, and `contentType` variables from `opengraph-image` or `twitter-image` route.

| Option                        | Type                                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| [`alt`](#alt)                 | `string`                                                                                                        |
| [`size`](#size)               | `{ width: number; height: number }`                                                                             |
| [`contentType`](#contenttype) | `string` - [image MIME type](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/MIME_types#image_types) |

#### `alt`

```tsx filename="opengraph-image.tsx | twitter-image.tsx" switcher
export const alt = 'My images alt text'

export default function Image() {}
```

```jsx filename="opengraph-image.js | twitter-image.js" switcher
export const alt = 'My images alt text'

export default function Image() {}
```

```html filename="<head> output"
<meta property="og:image:alt" content="My images alt text" />
```

#### `size`

```tsx filename="opengraph-image.tsx | twitter-image.tsx" switcher
export const size = { width: 1200, height: 630 }

export default function Image() {}
```

```jsx filename="opengraph-image.js | twitter-image.js" switcher
export const size = { width: 1200, height: 630 }

export default function Image() {}
```

```html filename="<head> output"
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

#### `contentType`

```tsx filename="opengraph-image.tsx | twitter-image.tsx" switcher
export const contentType = 'image/png'

export default function Image() {}
```

```jsx filename="opengraph-image.js | twitter-image.js" switcher
export const contentType = 'image/png'

export default function Image() {}
```

```html filename="<head> output"
<meta property="og:image:type" content="image/png" />
```

#### Route Segment Config

`opengraph-image` and `twitter-image` are specialized [Route Handlers](/docs/app/api-reference/file-conventions/route.md) that can use the same [route segment configuration](/docs/app/api-reference/file-conventions/route-segment-config.md) options as Pages and Layouts.

### Examples

#### Using external data

This example uses the `params` object and external data to generate the image.

> **Good to know**:
> By default, this generated image will be [statically optimized](/docs/app/guides/caching.md#static-rendering). You can configure the individual `fetch` [`options`](/docs/app/api-reference/functions/fetch.md) or route segments [options](/docs/app/api-reference/file-conventions/route-segment-config.md#revalidate) to change this behavior.

```tsx filename="app/posts/[slug]/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'

export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}
export const contentType = 'image/png'

export default async function Image({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await fetch(`https://.../posts/${slug}`).then((res) =>
    res.json()
  )

  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 48,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {post.title}
      </div>
    ),
    {
      ...size,
    }
  )
}
```

```jsx filename="app/posts/[slug]/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'

export const alt = 'About Acme'
export const size = {
  width: 1200,
  height: 630,
}
export const contentType = 'image/png'

export default async function Image({ params }) {
  const { slug } = await params
  const post = await fetch(`https://.../posts/${slug}`).then((res) =>
    res.json()
  )

  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 48,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {post.title}
      </div>
    ),
    {
      ...size,
    }
  )
}
```

#### Using Node.js runtime with local assets

These examples use the Node.js runtime to fetch a local image from the file system and pass it to the `<img>` `src` attribute, either as a base64 string or an `ArrayBuffer`. Place the local asset relative to the project root, not the example source file.

```tsx filename="app/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'), 'base64')
  const logoSrc = `data:image/png;base64,${logoData}`

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```

```jsx filename="app/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'), 'base64')
  const logoSrc = `data:image/png;base64,${logoData}`

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```

Passing an `ArrayBuffer` to the `src` attribute of an `<img>` element is not part of the HTML spec. The rendering engine used by `next/og` supports it, but because TypeScript definitions follow the spec, you need a `@ts-expect-error` directive or similar to use this [feature](https://github.com/vercel/satori/issues/606#issuecomment-2144000453).

```tsx filename="app/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'))
  const logoSrc = Uint8Array.from(logoData).buffer

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        {/* @ts-expect-error Satori accepts ArrayBuffer/typed arrays for <img src> at runtime */}
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```

```jsx filename="app/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'
import { join } from 'node:path'
import { readFile } from 'node:fs/promises'

export default async function Image() {
  const logoData = await readFile(join(process.cwd(), 'logo.png'))
  const logoSrc = Uint8Array.from(logoData).buffer

  return new ImageResponse(
    (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <img src={logoSrc} height="100" />
      </div>
    )
  )
}
```

## Version History

| Version   | Changes                                              |
| --------- | ---------------------------------------------------- |
| `v16.0.0` | `params` is now a promise that resolves to an object |
| `v13.3.0` | `opengraph-image` and `twitter-image` introduced.    |


--------------------------------------------------------------------------------
title: "robots.txt"
description: "API Reference for robots.txt file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots"
--------------------------------------------------------------------------------

# robots.txt

Add or generate a `robots.txt` file that matches the [Robots Exclusion Standard](https://en.wikipedia.org/wiki/Robots.txt#Standard) in the **root** of `app` directory to tell search engine crawlers which URLs they can access on your site.

## Static `robots.txt`

```txt filename="app/robots.txt"
User-Agent: *
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
```

## Generate a Robots file

Add a `robots.js` or `robots.ts` file that returns a [`Robots` object](#robots-object).

> **Good to know**: `robots.js` is a special Route Handlers that is cached by default unless it uses a [Dynamic API](/docs/app/guides/caching.md#dynamic-apis) or [dynamic config](/docs/app/guides/caching.md#segment-config-options) option.

```ts filename="app/robots.ts" switcher
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/private/',
    },
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

```js filename="app/robots.js" switcher
export default function robots() {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: '/private/',
    },
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:

```txt
User-Agent: *
Allow: /
Disallow: /private/

Sitemap: https://acme.com/sitemap.xml
```

### Customizing specific user agents

You can customise how individual search engine bots crawl your site by passing an array of user agents to the `rules` property. For example:

```ts filename="app/robots.ts" switcher
import type { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: 'Googlebot',
        allow: ['/'],
        disallow: '/private/',
      },
      {
        userAgent: ['Applebot', 'Bingbot'],
        disallow: ['/'],
      },
    ],
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

```js filename="app/robots.js" switcher
export default function robots() {
  return {
    rules: [
      {
        userAgent: 'Googlebot',
        allow: ['/'],
        disallow: ['/private/'],
      },
      {
        userAgent: ['Applebot', 'Bingbot'],
        disallow: ['/'],
      },
    ],
    sitemap: 'https://acme.com/sitemap.xml',
  }
}
```

Output:

```txt
User-Agent: Googlebot
Allow: /
Disallow: /private/

User-Agent: Applebot
Disallow: /

User-Agent: Bingbot
Disallow: /

Sitemap: https://acme.com/sitemap.xml
```

### Robots object

```tsx
type Robots = {
  rules:
    | {
        userAgent?: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }
    | Array<{
        userAgent: string | string[]
        allow?: string | string[]
        disallow?: string | string[]
        crawlDelay?: number
      }>
  sitemap?: string | string[]
  host?: string
}
```

## Version History

| Version   | Changes              |
| --------- | -------------------- |
| `v13.3.0` | `robots` introduced. |


--------------------------------------------------------------------------------
title: "sitemap.xml"
description: "API Reference for the sitemap.xml file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap"
--------------------------------------------------------------------------------

# sitemap.xml

`sitemap.(xml|js|ts)` is a special file that matches the [Sitemaps XML format](https://www.sitemaps.org/protocol.html) to help search engine crawlers index your site more efficiently.

### Sitemap files (.xml)

For smaller applications, you can create a `sitemap.xml` file and place it in the root of your `app` directory.

```xml filename="app/sitemap.xml"
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://acme.com</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### Generating a sitemap using code (.js, .ts)

You can use the `sitemap.(js|ts)` file convention to programmatically **generate** a sitemap by exporting a default function that returns an array of URLs. If using TypeScript, a [`Sitemap`](#returns) type is available.

> **Good to know**: `sitemap.js` is a special Route Handler that is cached by default unless it uses a [Dynamic API](/docs/app/guides/caching.md#dynamic-apis) or [dynamic config](/docs/app/guides/caching.md#segment-config-options) option.

```ts filename="app/sitemap.ts" switcher
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.5,
    },
  ]
}
```

```js filename="app/sitemap.js" switcher
export default function sitemap() {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      changeFrequency: 'yearly',
      priority: 1,
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      changeFrequency: 'monthly',
      priority: 0.8,
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.5,
    },
  ]
}
```

Output:

```xml filename="acme.com/sitemap.xml"
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://acme.com</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>yearly</changefreq>
    <priority>1</priority>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### Image Sitemaps

You can use `images` property to create image sitemaps. Learn more details in the [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps).

```ts filename="app/sitemap.ts" switcher
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://example.com',
      lastModified: '2021-01-01',
      changeFrequency: 'weekly',
      priority: 0.5,
      images: ['https://example.com/image.jpg'],
    },
  ]
}
```

Output:

```xml filename="acme.com/sitemap.xml"
<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
>
  <url>
    <loc>https://example.com</loc>
    <image:image>
      <image:loc>https://example.com/image.jpg</image:loc>
    </image:image>
    <lastmod>2021-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### Video Sitemaps

You can use `videos` property to create video sitemaps. Learn more details in the [Google Developer Docs](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps).

```ts filename="app/sitemap.ts" switcher
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://example.com',
      lastModified: '2021-01-01',
      changeFrequency: 'weekly',
      priority: 0.5,
      videos: [
        {
          title: 'example',
          thumbnail_loc: 'https://example.com/image.jpg',
          description: 'this is the description',
        },
      ],
    },
  ]
}
```

Output:

```xml filename="acme.com/sitemap.xml"
<?xml version="1.0" encoding="UTF-8"?>
<urlset
  xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
  xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"
>
  <url>
    <loc>https://example.com</loc>
    <video:video>
      <video:title>example</video:title>
      <video:thumbnail_loc>https://example.com/image.jpg</video:thumbnail_loc>
      <video:description>this is the description</video:description>
    </video:video>
    <lastmod>2021-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
</urlset>
```

### Generate a localized Sitemap

```ts filename="app/sitemap.ts" switcher
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es',
          de: 'https://acme.com/de',
        },
      },
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es/about',
          de: 'https://acme.com/de/about',
        },
      },
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es/blog',
          de: 'https://acme.com/de/blog',
        },
      },
    },
  ]
}
```

```js filename="app/sitemap.js" switcher
export default function sitemap() {
  return [
    {
      url: 'https://acme.com',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es',
          de: 'https://acme.com/de',
        },
      },
    },
    {
      url: 'https://acme.com/about',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es/about',
          de: 'https://acme.com/de/about',
        },
      },
    },
    {
      url: 'https://acme.com/blog',
      lastModified: new Date(),
      alternates: {
        languages: {
          es: 'https://acme.com/es/blog',
          de: 'https://acme.com/de/blog',
        },
      },
    },
  ]
}
```

Output:

```xml filename="acme.com/sitemap.xml"
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://acme.com</loc>
    <xhtml:link
      rel="alternate"
      hreflang="es"
      href="https://acme.com/es"/>
    <xhtml:link
      rel="alternate"
      hreflang="de"
      href="https://acme.com/de"/>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  </url>
  <url>
    <loc>https://acme.com/about</loc>
    <xhtml:link
      rel="alternate"
      hreflang="es"
      href="https://acme.com/es/about"/>
    <xhtml:link
      rel="alternate"
      hreflang="de"
      href="https://acme.com/de/about"/>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  </url>
  <url>
    <loc>https://acme.com/blog</loc>
    <xhtml:link
      rel="alternate"
      hreflang="es"
      href="https://acme.com/es/blog"/>
    <xhtml:link
      rel="alternate"
      hreflang="de"
      href="https://acme.com/de/blog"/>
    <lastmod>2023-04-06T15:02:24.021Z</lastmod>
  </url>
</urlset>
```

### Generating multiple sitemaps

While a single sitemap will work for most applications. For large web applications, you may need to split a sitemap into multiple files.

There are two ways you can create multiple sitemaps:

* By nesting `sitemap.(xml|js|ts)` inside multiple route segments e.g. `app/sitemap.xml` and `app/products/sitemap.xml`.
* By using the [`generateSitemaps`](/docs/app/api-reference/functions/generate-sitemaps.md) function.

For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.

```ts filename="app/product/sitemap.ts" switcher
import type { MetadataRoute } from 'next'
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props: {
  id: Promise<number>
}): Promise<MetadataRoute.Sitemap> {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

```js filename="app/product/sitemap.js" switcher
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props) {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

Your generated sitemaps will be available at `/.../sitemap/[id]`. For example, `/product/sitemap/1.xml`.

See the [`generateSitemaps` API reference](/docs/app/api-reference/functions/generate-sitemaps.md) for more information.

## Returns

The default function exported from `sitemap.(xml|ts|js)` should return an array of objects with the following properties:

```tsx
type Sitemap = Array<{
  url: string
  lastModified?: string | Date
  changeFrequency?:
    | 'always'
    | 'hourly'
    | 'daily'
    | 'weekly'
    | 'monthly'
    | 'yearly'
    | 'never'
  priority?: number
  alternates?: {
    languages?: Languages<string>
  }
}>
```

## Version History

| Version    | Changes                                                      |
| ---------- | ------------------------------------------------------------ |
| `v16.0.0`  | `id` is now a promise that resolves to a number.             |
| `v14.2.0`  | Add localizations support.                                   |
| `v13.4.14` | Add `changeFrequency` and `priority` attributes to sitemaps. |
| `v13.3.0`  | `sitemap` introduced.                                        |
## Next Steps

Learn how to use the generateSitemaps function.

- [generateSitemaps](/docs/app/api-reference/functions/generate-sitemaps.md)
  - Learn how to use the generateSiteMaps function to create multiple sitemaps for your application.


--------------------------------------------------------------------------------
title: "Functions"
description: "API Reference for Next.js Functions and Hooks."
source: "https://nextjs.org/docs/app/api-reference/functions"
--------------------------------------------------------------------------------

# Functions



 - [after](/docs/app/api-reference/functions/after.md)
 - [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
 - [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
 - [connection](/docs/app/api-reference/functions/connection.md)
 - [cookies](/docs/app/api-reference/functions/cookies.md)
 - [draftMode](/docs/app/api-reference/functions/draft-mode.md)
 - [fetch](/docs/app/api-reference/functions/fetch.md)
 - [forbidden](/docs/app/api-reference/functions/forbidden.md)
 - [generateImageMetadata](/docs/app/api-reference/functions/generate-image-metadata.md)
 - [generateMetadata](/docs/app/api-reference/functions/generate-metadata.md)
 - [generateSitemaps](/docs/app/api-reference/functions/generate-sitemaps.md)
 - [generateStaticParams](/docs/app/api-reference/functions/generate-static-params.md)
 - [generateViewport](/docs/app/api-reference/functions/generate-viewport.md)
 - [headers](/docs/app/api-reference/functions/headers.md)
 - [ImageResponse](/docs/app/api-reference/functions/image-response.md)
 - [NextRequest](/docs/app/api-reference/functions/next-request.md)
 - [NextResponse](/docs/app/api-reference/functions/next-response.md)
 - [notFound](/docs/app/api-reference/functions/not-found.md)
 - [permanentRedirect](/docs/app/api-reference/functions/permanentRedirect.md)
 - [redirect](/docs/app/api-reference/functions/redirect.md)
 - [refresh](/docs/app/api-reference/functions/refresh.md)
 - [revalidatePath](/docs/app/api-reference/functions/revalidatePath.md)
 - [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
 - [unauthorized](/docs/app/api-reference/functions/unauthorized.md)
 - [unstable_cache](/docs/app/api-reference/functions/unstable_cache.md)
 - [unstable_noStore](/docs/app/api-reference/functions/unstable_noStore.md)
 - [unstable_rethrow](/docs/app/api-reference/functions/unstable_rethrow.md)
 - [updateTag](/docs/app/api-reference/functions/updateTag.md)
 - [useLinkStatus](/docs/app/api-reference/functions/use-link-status.md)
 - [useParams](/docs/app/api-reference/functions/use-params.md)
 - [usePathname](/docs/app/api-reference/functions/use-pathname.md)
 - [useReportWebVitals](/docs/app/api-reference/functions/use-report-web-vitals.md)
 - [useRouter](/docs/app/api-reference/functions/use-router.md)
 - [useSearchParams](/docs/app/api-reference/functions/use-search-params.md)
 - [useSelectedLayoutSegment](/docs/app/api-reference/functions/use-selected-layout-segment.md)
 - [useSelectedLayoutSegments](/docs/app/api-reference/functions/use-selected-layout-segments.md)
 - [userAgent](/docs/app/api-reference/functions/userAgent.md)

--------------------------------------------------------------------------------
title: "after"
description: "API Reference for the after function."
source: "https://nextjs.org/docs/app/api-reference/functions/after"
--------------------------------------------------------------------------------

# after

`after` allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.

It can be used in [Server Components](/docs/app/getting-started/server-and-client-components.md) (including [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata.md)), [Server Actions](/docs/app/getting-started/updating-data.md), [Route Handlers](/docs/app/api-reference/file-conventions/route.md), and [Proxy](/docs/app/api-reference/file-conventions/proxy.md).

The function accepts a callback that will be executed after the response (or prerender) is finished:

```tsx filename="app/layout.tsx" switcher
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'

export default function Layout({ children }: { children: React.ReactNode }) {
  after(() => {
    // Execute after the layout is rendered and sent to the user
    log()
  })
  return <>{children}</>
}
```

```jsx filename="app/layout.jsx" switcher
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'

export default function Layout({ children }) {
  after(() => {
    // Execute after the layout is rendered and sent to the user
    log()
  })
  return <>{children}</>
}
```

> **Good to know:** `after` is not a [Dynamic API](/docs/app/guides/caching.md#dynamic-rendering) and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.

## Reference

### Parameters

* A callback function which will be executed after the response (or prerender) is finished.

### Duration

`after` will run for the platform's default or configured max duration of your route. If your platform supports it, you can configure the timeout limit using the [`maxDuration`](/docs/app/api-reference/file-conventions/route-segment-config.md#maxduration) route segment config.

## Good to know

* `after` will be executed even if the response didn't complete successfully. Including when an error is thrown or when `notFound` or `redirect` is called.
* You can use React `cache` to deduplicate functions called inside `after`.
* `after` can be nested inside other `after` calls, for example, you can create utility functions that wrap `after` calls to add additional functionality.

## Examples

### With request APIs

You can use request APIs such as [`cookies`](/docs/app/api-reference/functions/cookies.md) and [`headers`](/docs/app/api-reference/functions/headers.md) inside `after` in [Server Actions](/docs/app/getting-started/updating-data.md) and [Route Handlers](/docs/app/api-reference/file-conventions/route.md). This is useful for logging activity after a mutation. For example:

```ts filename="app/api/route.ts" highlight={2,7-9} switcher
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export async function POST(request: Request) {
  // Perform mutation
  // ...

  // Log user activity for analytics
  after(async () => {
    const userAgent = (await headers().get('user-agent')) || 'unknown'
    const sessionCookie =
      (await cookies().get('session-id'))?.value || 'anonymous'

    logUserAction({ sessionCookie, userAgent })
  })

  return new Response(JSON.stringify({ status: 'success' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}
```

```js filename="app/api/route.js" highlight={2,7-9} switcher
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export async function POST(request) {
  // Perform mutation
  // ...

  // Log user activity for analytics
  after(async () => {
    const userAgent = (await headers().get('user-agent')) || 'unknown'
    const sessionCookie =
      (await cookies().get('session-id'))?.value || 'anonymous'

    logUserAction({ sessionCookie, userAgent })
  })

  return new Response(JSON.stringify({ status: 'success' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}
```

However, you cannot use these request APIs inside `after` in [Server Components](/docs/app/getting-started/server-and-client-components.md). This is because Next.js needs to know which part of the tree access the request APIs to support [Cache Components](/docs/app/getting-started/cache-components.md), but `after` runs after React's rendering lifecycle.

## Platform Support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure `after`](/docs/app/guides/self-hosting.md#after) when self-hosting Next.js.

<details>
<summary>Reference: supporting `after` for serverless platforms</summary>

Using `after` in a serverless context requires waiting for asynchronous tasks to finish after the response has been sent. In Next.js and Vercel, this is achieved using a primitive called `waitUntil(promise)`, which extends the lifetime of a serverless invocation until all promises passed to [`waitUntil`](https://vercel.com/docs/functions/functions-api-reference#waituntil) have settled.

If you want your users to be able to run `after`, you will have to provide your implementation of `waitUntil` that behaves in an analogous way.

When `after` is called, Next.js will access `waitUntil` like this:

```jsx
const RequestContext = globalThis[Symbol.for('@next/request-context')]
const contextValue = RequestContext?.get()
const waitUntil = contextValue?.waitUntil
```

Which means that `globalThis[Symbol.for('@next/request-context')]` is expected to contain an object like this:

```tsx
type NextRequestContext = {
  get(): NextRequestContextValue | undefined
}

type NextRequestContextValue = {
  waitUntil?: (promise: Promise<any>) => void
}
```

Here is an example of the implementation.

```tsx
import { AsyncLocalStorage } from 'node:async_hooks'

const RequestContextStorage = new AsyncLocalStorage<NextRequestContextValue>()

// Define and inject the accessor that next.js will use
const RequestContext: NextRequestContext = {
  get() {
    return RequestContextStorage.getStore()
  },
}
globalThis[Symbol.for('@next/request-context')] = RequestContext

const handler = (req, res) => {
  const contextValue = { waitUntil: YOUR_WAITUNTIL }
  // Provide the value
  return RequestContextStorage.run(contextValue, () => nextJsHandler(req, res))
}
```

</details>

## Version History

| Version History | Description                  |
| --------------- | ---------------------------- |
| `v15.1.0`       | `after` became stable.       |
| `v15.0.0-rc`    | `unstable_after` introduced. |


--------------------------------------------------------------------------------
title: "cacheLife"
description: "Learn how to use the cacheLife function to set the cache expiration time for a cached function or component."
source: "https://nextjs.org/docs/app/api-reference/functions/cacheLife"
--------------------------------------------------------------------------------

# cacheLife

The `cacheLife` function is used to set the cache lifetime of a function or component. It should be used alongside the [`use cache`](/docs/app/api-reference/directives/use-cache.md) directive, and within the scope of the function or component.

## Usage

### Basic setup

To use `cacheLife`, first enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents.md) in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

### Using preset profiles

Next.js provides preset cache profiles that cover common caching needs. Each profile balances three factors:

* How long users see cached content without checking for updates (client-side)
* How often fresh content is generated on the server
* When old content expires completely

Choose a profile based on how frequently your content changes:

* **`seconds`** - Real-time data (stock prices, live scores)
* **`minutes`** - Frequently updated (social feeds, news)
* **`hours`** - Multiple daily updates (product inventory, weather)
* **`days`** - Daily updates (blog posts, articles)
* **`weeks`** - Weekly updates (podcasts, newsletters)
* **`max`** - Rarely changes (legal pages, archived content)

Import `cacheLife` and pass a profile name:

```tsx filename="app/blog/page.tsx" highlight={1,5}
'use cache'
import { cacheLife } from 'next/cache'

export default async function BlogPage() {
  cacheLife('days') // Blog content updated daily

  const posts = await getBlogPosts()
  return <div>{/* render posts */}</div>
}
```

The profile name tells Next.js how to cache the entire function's output. If you need more control over timing values, see the [Reference](#reference) section below.

> **Good to know**: The `use cache` directive can be placed at the file level or at the top of a function or component, and `cacheLife` must be called within its scope.

## Reference

### Cache profile properties

Cache profiles control caching behavior through three timing properties:

* **[`stale`](#stale)**: How long the client can use cached data without checking the server
* **[`revalidate`](#revalidate)**: After this time, the next request will trigger a background refresh
* **[`expire`](#expire)**: After this time with no requests, the next one waits for fresh content

#### `stale`

**Client-side:** How long the client can use cached data without checking the server.

During this time, the client-side router displays cached content immediately without any network request. After this period expires, the router must check with the server on the next navigation or request. This provides instant page loads from the client cache, but data may be outdated.

```tsx
cacheLife({ stale: 300 }) // 5 minutes
```

#### `revalidate`

How often the server regenerates cached content in the background.

* When a request arrives after this period, the server:
  1. Serves the cached version immediately (if available)
  2. Regenerates content in the background
  3. Updates the cache with fresh content
* Similar to [Incremental Static Regeneration (ISR)](/docs/app/guides/incremental-static-regeneration.md)

```tsx
cacheLife({ revalidate: 900 }) // 15 minutes
```

#### `expire`

Maximum time before the server must regenerate cached content.

* After this period with no traffic, the server regenerates content synchronously on the next request
* When you set both `revalidate` and `expire`, `expire` must be longer than `revalidate`. Next.js validates this and raises an error for invalid configurations.

```tsx
cacheLife({ expire: 3600 }) // 1 hour
```

### Preset cache profiles

If you don't specify a profile, Next.js uses the `default` profile. We recommend explicitly setting a profile to make caching behavior clear.

| **Profile** | **Use Case**                           | `stale`    | `revalidate` | `expire` |
| ----------- | -------------------------------------- | ---------- | ------------ | -------- |
| `default`   | Standard content                       | 5 minutes  | 15 minutes   | 1 year   |
| `seconds`   | Real-time data                         | 30 seconds | 1 second     | 1 minute |
| `minutes`   | Frequently updated content             | 5 minutes  | 1 minute     | 1 hour   |
| `hours`     | Content updated multiple times per day | 5 minutes  | 1 hour       | 1 day    |
| `days`      | Content updated daily                  | 5 minutes  | 1 day        | 1 week   |
| `weeks`     | Content updated weekly                 | 5 minutes  | 1 week       | 30 days  |
| `max`       | Stable content that rarely changes     | 5 minutes  | 30 days      | 1 year   |

### Custom cache profiles

Define reusable cache profiles in your `next.config.ts` file:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    biweekly: {
      stale: 60 * 60 * 24 * 14, // 14 days
      revalidate: 60 * 60 * 24, // 1 day
      expire: 60 * 60 * 24 * 14, // 14 days
    },
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    biweekly: {
      stale: 60 * 60 * 24 * 14, // 14 days
      revalidate: 60 * 60 * 24, // 1 day
      expire: 60 * 60 * 24 * 14, // 14 days
    },
  },
}

module.exports = nextConfig
```

The example above caches for 14 days, checks for updates daily, and expires the cache after 14 days. You can then reference this profile throughout your application by its name:

```tsx filename="app/page.tsx" highlight={5}
'use cache'
import { cacheLife } from 'next/cache'

export default async function Page() {
  cacheLife('biweekly')
  return <div>Page</div>
}
```

### Overriding the default cache profiles

While the default cache profiles provide a useful way to think about how fresh or stale any given part of cacheable output can be, you may prefer different named profiles to better align with your applications caching strategies.

You can override the default named cache profiles by creating a new configuration with the same name as the defaults.

The example below shows how to override the default `"days"` cache profile:

```ts filename="next.config.ts"
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    days: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}

export default nextConfig
```

You can also override the preset profiles by using the same name:

```ts filename="next.config.ts"
const nextConfig = {
  cacheComponents: true,
  cacheLife: {
    // Override the 'days' profile
    days: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}
```

### Inline cache profiles

For one-off cases, pass a profile object directly to `cacheLife`:

```tsx filename="app/page.tsx"
'use cache'
import { cacheLife } from 'next/cache'

export default async function Page() {
  cacheLife({
    stale: 3600,
    revalidate: 900,
    expire: 86400,
  })

  return <div>Page</div>
}
```

Inline profiles apply only to the specific function or component. For reusable configurations, define custom profiles in `next.config.ts`.

Using `cacheLife({})` with an empty object applies the `default` profile values.

### Client router cache behavior

The `stale` property controls the client-side router cache, not the `Cache-Control` header:

* The server sends the stale time via the `x-nextjs-stale-time` response header
* The client router uses this value to determine when to revalidate
* **Minimum of 30 seconds is enforced** to ensure prefetched links remain usable

This 30-second minimum prevents prefetched data from expiring before users can click on links. It only applies to time-based expiration.

When you call revalidation functions from a Server Action ([`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md), [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md), [`updateTag`](/docs/app/api-reference/functions/updateTag.md), or [`refresh`](/docs/app/api-reference/functions/refresh.md)), the entire client cache is immediately cleared, bypassing the stale time.

> **Good to know**: The `stale` property in `cacheLife` differs from [`staleTimes`](/docs/app/api-reference/config/next-config-js/staleTimes.md). While `staleTimes` is a global setting affecting all routes, `cacheLife` allows per-function or per-route configuration. Updating `staleTimes.static` also updates the `stale` value of the `default` cache profile.

## Examples

### Using preset profiles

The simplest way to configure caching is using preset profiles. Choose one that matches your content's update pattern:

```tsx filename="app/blog/[slug]/page.tsx"
import { cacheLife } from 'next/cache'

export default async function BlogPost() {
  'use cache'
  cacheLife('days') // Blog posts updated daily

  const post = await fetchBlogPost()
  return <article>{post.content}</article>
}
```

```tsx filename="app/products/[id]/page.tsx"
import { cacheLife } from 'next/cache'

export default async function ProductPage() {
  'use cache'
  cacheLife('hours') // Product data updated multiple times per day

  const product = await fetchProduct()
  return <div>{product.name}</div>
}
```

### Custom profiles for specific needs

Define custom profiles when preset options don't match your requirements:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    editorial: {
      stale: 600, // 10 minutes
      revalidate: 3600, // 1 hour
      expire: 86400, // 1 day
    },
    marketing: {
      stale: 300, // 5 minutes
      revalidate: 1800, // 30 minutes
      expire: 43200, // 12 hours
    },
  },
}

export default nextConfig
```

Then use these profiles throughout your application:

```tsx filename="app/editorial/page.tsx"
import { cacheLife } from 'next/cache'

export default async function EditorialPage() {
  'use cache'
  cacheLife('editorial')
  // ...
}
```

### Inline profiles for unique cases

Use inline profiles when a specific function needs one-off caching behavior:

```tsx filename="app/api/limited-offer/route.ts"
import { cacheLife } from 'next/cache'
import { getDb } from '@lib/db'

async function getLimitedOffer() {
  'use cache'

  cacheLife({
    stale: 60, // 1 minute
    revalidate: 300, // 5 minutes
    expire: 3600, // 1 hour
  })

  const offer = await getDb().offer.findFirst({
    where: { type: 'limited' },
    orderBy: { created_at: 'desc' },
  })

  return offer
}

export async function GET() {
  const offer = await getLimitedOffer()

  return Response.json(offer)
}
```

### Caching individual functions

Apply caching to utility functions for granular control:

```tsx filename="lib/api.ts"
import { cacheLife } from 'next/cache'

export async function getSettings() {
  'use cache'
  cacheLife('max') // Settings rarely change

  return await fetchSettings()
}
```

```tsx filename="lib/stats.ts"
import { cacheLife } from 'next/cache'

export async function getRealtimeStats() {
  'use cache'
  cacheLife('seconds') // Stats update constantly

  return await fetchStats()
}
```

### Nested caching behavior

When components with different cache profiles are nested, Next.js respects the shortest duration among them:

```tsx filename="app/dashboard/page.tsx"
import { cacheLife } from 'next/cache'
import { RealtimeWidget } from './realtime-widget'

export default async function Dashboard() {
  'use cache'
  cacheLife('hours') // Dashboard cached for hours

  return (
    <div>
      <h1>Dashboard</h1>
      <RealtimeWidget />
    </div>
  )
}
```

```tsx filename="app/dashboard/realtime-widget.tsx"
import { cacheLife } from 'next/cache'

export async function RealtimeWidget() {
  'use cache'
  cacheLife('seconds') // Widget needs fresh data

  const data = await fetchRealtimeData()
  return <div>{data.value}</div>
}
```

In this example, the outer `Dashboard` component specifies the `hours` profile, but it contains `RealtimeWidget` which uses the `seconds` profile. The shortest duration from the nested profiles takes precedence, ensuring the widget gets fresh data while the rest of the dashboard can be cached longer.

> **Good to know**: This shortest-duration behavior ensures that no part of your page serves stale data longer than its most frequently updated component requires.
## Related

View related API references.

- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [use cache](/docs/app/api-reference/directives/use-cache.md)
  - Learn how to use the use cache directive to cache data in your Next.js application.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.
- [cacheTag](/docs/app/api-reference/functions/cacheTag.md)
  - Learn how to use the cacheTag function to manage cache invalidation in your Next.js application.


--------------------------------------------------------------------------------
title: "cacheTag"
description: "Learn how to use the cacheTag function to manage cache invalidation in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/functions/cacheTag"
--------------------------------------------------------------------------------

# cacheTag

The `cacheTag` function allows you to tag cached data for on-demand invalidation. By associating tags with cache entries, you can selectively purge or revalidate specific cache entries without affecting other cached data.

## Usage

To use `cacheTag`, enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents.md) in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
const nextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

The `cacheTag` function takes one or more string values.

```tsx filename="app/data.ts" switcher
import { cacheTag } from 'next/cache'

export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

```jsx filename="app/data.js" switcher
import { cacheTag } from 'next/cache'

export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

You can then purge the cache on-demand using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) API in another function, for example, a [route handler](/docs/app/api-reference/file-conventions/route.md) or [Server Action](/docs/app/getting-started/updating-data.md):

```tsx filename="app/action.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

```jsx filename="app/action.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```

## Good to know

* **Idempotent Tags**: Applying the same tag multiple times has no additional effect.
* **Multiple Tags**: You can assign multiple tags to a single cache entry by passing multiple string values to `cacheTag`.

```tsx
cacheTag('tag-one', 'tag-two')
```

* **Limits**: The max length for a custom tag is 256 characters and the max tag items is 128.

## Examples

### Tagging components or functions

Tag your cached data by calling `cacheTag` within a cached function or component:

```tsx filename="app/components/bookings.tsx" switcher
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  cacheTag('bookings-data')

  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }

  return //...
}
```

```jsx filename="app/components/bookings.js" switcher
import { cacheTag } from 'next/cache'

export async function Bookings({ type = 'haircut' }) {
  'use cache'
  cacheTag('bookings-data')

  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }

  return //...
}
```

### Creating tags from external data

You can use the data returned from an async function to tag the cache entry.

```tsx filename="app/components/bookings.tsx" switcher
import { cacheTag } from 'next/cache'

interface BookingsProps {
  type: string
}

export async function Bookings({ type = 'haircut' }: BookingsProps) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

```jsx filename="app/components/bookings.js" switcher
import { cacheTag } from 'next/cache'

export async function Bookings({ type = 'haircut' }) {
  async function getBookingsData() {
    'use cache'
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    cacheTag('bookings-data', data.id)
    return data
  }
  return //...
}
```

### Invalidating tagged cache

Using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md), you can invalidate the cache for a specific tag when needed:

```tsx filename="app/actions.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```

```jsx filename="app/actions.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateBookings() {
  await updateBookingData()
  revalidateTag('bookings-data')
}
```
## Related

View related API references.

- [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
  - Learn how to enable the cacheComponents flag in Next.js.
- [use cache](/docs/app/api-reference/directives/use-cache.md)
  - Learn how to use the use cache directive to cache data in your Next.js application.
- [revalidateTag](/docs/app/api-reference/functions/revalidateTag.md)
  - API Reference for the revalidateTag function.
- [cacheLife](/docs/app/api-reference/functions/cacheLife.md)
  - Learn how to use the cacheLife function to set the cache expiration time for a cached function or component.


--------------------------------------------------------------------------------
title: "connection"
description: "API Reference for the connection function."
source: "https://nextjs.org/docs/app/api-reference/functions/connection"
--------------------------------------------------------------------------------

# connection

The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.

It's useful when a component doesn't use [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering), but you want it to be dynamically rendered at runtime and not statically rendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.

```ts filename="app/page.tsx" switcher
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  // Everything below will be excluded from prerendering
  const rand = Math.random()
  return <span>{rand}</span>
}
```

```jsx filename="app/page.js" switcher
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  // Everything below will be excluded from prerendering
  const rand = Math.random()
  return <span>{rand}</span>
}
```

## Reference

### Type

```jsx
function connection(): Promise<void>
```

### Parameters

* The function does not accept any parameters.

### Returns

* The function returns a `void` Promise. It is not meant to be consumed.

## Good to know

* `connection` replaces [`unstable_noStore`](/docs/app/api-reference/functions/unstable_noStore.md) to better align with the future of Next.js.
* The function is only necessary when dynamic rendering is required and common Dynamic APIs are not used.

### Version History

| Version      | Changes                  |
| ------------ | ------------------------ |
| `v15.0.0`    | `connection` stabilized. |
| `v15.0.0-RC` | `connection` introduced. |


--------------------------------------------------------------------------------
title: "cookies"
description: "API Reference for the cookies function."
source: "https://nextjs.org/docs/app/api-reference/functions/cookies"
--------------------------------------------------------------------------------

# cookies

`cookies` is an **async** function that allows you to read the HTTP incoming request cookies in [Server Components](/docs/app/getting-started/server-and-client-components.md), and read/write outgoing request cookies in [Server Actions](/docs/app/getting-started/updating-data.md) or [Route Handlers](/docs/app/api-reference/file-conventions/route.md).

```tsx filename="app/page.tsx" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

```js filename="app/page.js" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

## Reference

### Methods

The following methods are available:

| Method                      | Return Type      | Description                                                                     |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------- |
| `get('name')`               | Object           | Accepts a cookie name and returns an object with the name and value.            |
| `getAll()`                  | Array of objects | Returns a list of all the cookies with a matching name.                         |
| `has('name')`               | Boolean          | Accepts a cookie name and returns a boolean based on if the cookie exists.      |
| `set(name, value, options)` | -                | Accepts a cookie name, value, and options and sets the outgoing request cookie. |
| `delete(name)`              | -                | Accepts a cookie name and deletes the cookie.                                   |
| `clear()`                   | -                | Deletes all cookies.                                                            |
| `toString()`                | String           | Returns a string representation of the cookies.                                 |

### Options

When setting a cookie, the following properties from the `options` object are supported:

| Option        | Type                                   | Description                                                                        |
| ------------- | -------------------------------------- | ---------------------------------------------------------------------------------- |
| `name`        | String                                 | Specifies the name of the cookie.                                                  |
| `value`       | String                                 | Specifies the value to be stored in the cookie.                                    |
| `expires`     | Date                                   | Defines the exact date when the cookie will expire.                                |
| `maxAge`      | Number                                 | Sets the cookie’s lifespan in seconds.                                             |
| `domain`      | String                                 | Specifies the domain where the cookie is available.                                |
| `path`        | String, default: `'/'`                 | Limits the cookie's scope to a specific path within the domain.                    |
| `secure`      | Boolean                                | Ensures the cookie is sent only over HTTPS connections for added security.         |
| `httpOnly`    | Boolean                                | Restricts the cookie to HTTP requests, preventing client-side access.              |
| `sameSite`    | Boolean, `'lax'`, `'strict'`, `'none'` | Controls the cookie's cross-site request behavior.                                 |
| `priority`    | String (`"low"`, `"medium"`, `"high"`) | Specifies the cookie's priority                                                    |
| `partitioned` | Boolean                                | Indicates whether the cookie is [partitioned](https://github.com/privacycg/CHIPS). |

The only option with a default value is `path`.

To learn more about these options, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies).

## Good to know

* `cookies` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access cookies.
  * In version 14 and earlier, `cookies` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* `cookies` is a [Dynamic API](/docs/app/guides/caching.md#dynamic-rendering) whose returned values cannot be known ahead of time. Using it in a layout or page will opt a route into [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering).
* The `.delete` method can only be called:
  * In a [Server Action](/docs/app/getting-started/updating-data.md) or [Route Handler](/docs/app/api-reference/file-conventions/route.md).
  * If it belongs to the same domain from which `.set` is called. For wildcard domains, the specific subdomain must be an exact match. Additionally, the code must be executed on the same protocol (HTTP or HTTPS) as the cookie you want to delete.
* HTTP does not allow setting cookies after streaming starts, so you must use `.set` in a [Server Action](/docs/app/getting-started/updating-data.md) or [Route Handler](/docs/app/api-reference/file-conventions/route.md).

## Understanding Cookie Behavior in Server Components

When working with cookies in Server Components, it's important to understand that cookies are fundamentally a client-side storage mechanism:

* **Reading cookies** works in Server Components because you're accessing the cookie data that the client's browser sends to the server in the HTTP request headers.
* **Setting cookies** cannot be done directly in a Server Component, even when using a Route Handler or Server Action. This is because cookies are actually stored by the browser, not the server.

The server can only send instructions (via `Set-Cookie` headers) to tell the browser to store cookies - the actual storage happens on the client side. This is why cookie operations that modify state (`.set`, `.delete`, `.clear`) must be performed in a Route Handler or Server Action where the response headers can be properly set.

## Understanding Cookie Behavior in Server Actions

After you set or delete a cookie in a Server Action, Next.js re-renders the current page and its layouts on the server so the UI reflects the new cookie value. See the [Caching guide](/docs/app/guides/caching.md#cookies).

The UI is not unmounted, but effects that depend on data coming from the server will re-run.

To refresh cached data too, call [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md) or [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) inside the action.

## Examples

### Getting a cookie

You can use the `(await cookies()).get('name')` method to get a single cookie:

```tsx filename="app/page.tsx" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

```jsx filename="app/page.js" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

### Getting all cookies

You can use the `(await cookies()).getAll()` method to get all cookies with a matching name. If `name` is unspecified, it returns all the available cookies.

```tsx filename="app/page.tsx" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  return cookieStore.getAll().map((cookie) => (
    <div key={cookie.name}>
      <p>Name: {cookie.name}</p>
      <p>Value: {cookie.value}</p>
    </div>
  ))
}
```

```jsx filename="app/page.js" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  return cookieStore.getAll().map((cookie) => (
    <div key={cookie.name}>
      <p>Name: {cookie.name}</p>
      <p>Value: {cookie.value}</p>
    </div>
  ))
}
```

### Setting a cookie

You can use the `(await cookies()).set(name, value, options)` method in a [Server Action](/docs/app/getting-started/updating-data.md) or [Route Handler](/docs/app/api-reference/file-conventions/route.md) to set a cookie. The [`options` object](#options) is optional.

```tsx filename="app/actions.ts" switcher
'use server'

import { cookies } from 'next/headers'

export async function create(data) {
  const cookieStore = await cookies()

  cookieStore.set('name', 'lee')
  // or
  cookieStore.set('name', 'lee', { secure: true })
  // or
  cookieStore.set({
    name: 'name',
    value: 'lee',
    httpOnly: true,
    path: '/',
  })
}
```

```js filename="app/actions.js" switcher
'use server'

import { cookies } from 'next/headers'

export async function create(data) {
  const cookieStore = await cookies()

  cookieStore.set('name', 'lee')
  // or
  cookieStore.set('name', 'lee', { secure: true })
  // or
  cookieStore.set({
    name: 'name',
    value: 'lee',
    httpOnly: true,
    path: '/',
  })
}
```

### Checking if a cookie exists

You can use the `(await cookies()).has(name)` method to check if a cookie exists:

```tsx filename="app/page.ts" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const hasCookie = cookieStore.has('theme')
  return '...'
}
```

```jsx filename="app/page.js" switcher
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const hasCookie = cookieStore.has('theme')
  return '...'
}
```

### Deleting cookies

There are three ways you can delete a cookie.

Using the `delete()` method:

```tsx filename="app/actions.ts" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).delete('name')
}
```

```js filename="app/actions.js" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).delete('name')
}
```

Setting a new cookie with the same name and an empty value:

```tsx filename="app/actions.ts" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).set('name', '')
}
```

```js filename="app/actions.js" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).set('name', '')
}
```

Setting the `maxAge` to 0 will immediately expire a cookie. `maxAge` accepts a value in seconds.

```tsx filename="app/actions.ts" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).set('name', 'value', { maxAge: 0 })
}
```

```js filename="app/actions.js" switcher
'use server'

import { cookies } from 'next/headers'

export async function delete(data) {
  (await cookies()).set('name', 'value', { maxAge: 0 })
``
}
```

## Version History

| Version      | Changes                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| `v15.0.0-RC` | `cookies` is now an async function. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available. |
| `v13.0.0`    | `cookies` introduced.                                                                                  |


--------------------------------------------------------------------------------
title: "draftMode"
description: "API Reference for the draftMode function."
source: "https://nextjs.org/docs/app/api-reference/functions/draft-mode"
--------------------------------------------------------------------------------

# draftMode

`draftMode` is an **async** function allows you to enable and disable [Draft Mode](/docs/app/guides/draft-mode.md), as well as check if Draft Mode is enabled in a [Server Component](/docs/app/getting-started/server-and-client-components.md).

```tsx filename="app/page.ts" switcher
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
}
```

```jsx filename="app/page.js" switcher
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
}
```

## Reference

The following methods and properties are available:

| Method      | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| `isEnabled` | A boolean value that indicates if Draft Mode is enabled.                          |
| `enable()`  | Enables Draft Mode in a Route Handler by setting a cookie (`__prerender_bypass`). |
| `disable()` | Disables Draft Mode in a Route Handler by deleting a cookie.                      |

## Good to know

* `draftMode` is an **asynchronous** function that returns a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function.
  * In version 14 and earlier, `draftMode` was a synchronous function. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* A new bypass cookie value will be generated each time you run `next build`. This ensures that the bypass cookie can’t be guessed.
* To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.

## Examples

### Enabling Draft Mode

To enable Draft Mode, create a new [Route Handler](/docs/app/api-reference/file-conventions/route.md) and call the `enable()` method:

```tsx filename="app/draft/route.ts" switcher
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

```js filename="app/draft/route.js" switcher
import { draftMode } from 'next/headers'

export async function GET(request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

### Disabling Draft Mode

By default, the Draft Mode session ends when the browser is closed.

To disable Draft Mode manually, call the `disable()` method in your [Route Handler](/docs/app/api-reference/file-conventions/route.md):

```tsx filename="app/draft/route.ts" switcher
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
  const draft = await draftMode()
  draft.disable()
  return new Response('Draft mode is disabled')
}
```

```js filename="app/draft/route.js" switcher
import { draftMode } from 'next/headers'

export async function GET(request) {
  const draft = await draftMode()
  draft.disable()
  return new Response('Draft mode is disabled')
}
```

Then, send a request to invoke the Route Handler. If calling the route using the [`<Link>` component](/docs/app/api-reference/components/link.md), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.

### Checking if Draft Mode is enabled

You can check if Draft Mode is enabled in a Server Component with the `isEnabled` property:

```tsx filename="app/page.ts" switcher
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
  return (
    <main>
      <h1>My Blog Post</h1>
      <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
    </main>
  )
}
```

```jsx filename="app/page.js" switcher
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
  return (
    <main>
      <h1>My Blog Post</h1>
      <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
    </main>
  )
}
```

## Version History

| Version      | Changes                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| `v15.0.0-RC` | `draftMode` is now an async function. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available. |
| `v13.4.0`    | `draftMode` introduced.                                                                                  |
## Next Steps

Learn how to use Draft Mode with this step-by-step guide.

- [Draft Mode](/docs/app/guides/draft-mode.md)
  - Next.js has draft mode to toggle between static and dynamic pages. You can learn how it works with App Router here.


--------------------------------------------------------------------------------
title: "fetch"
description: "API reference for the extended fetch function."
source: "https://nextjs.org/docs/app/api-reference/functions/fetch"
--------------------------------------------------------------------------------

# fetch

Next.js extends the [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API) to allow each request on the server to set its own persistent caching and revalidation semantics.

In the browser, the `cache` option indicates how a fetch request will interact with the *browser's* HTTP cache. With this extension, `cache` indicates how a *server-side* fetch request will interact with the framework's persistent [Data Cache](/docs/app/guides/caching.md#data-cache).

You can call `fetch` with `async` and `await` directly within Server Components.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  let data = await fetch('https://api.vercel.app/blog')
  let posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  let data = await fetch('https://api.vercel.app/blog')
  let posts = await data.json()
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  )
}
```

## `fetch(url, options)`

Since Next.js extends the [Web `fetch()` API](https://developer.mozilla.org/docs/Web/API/Fetch_API), you can use any of the [native options available](https://developer.mozilla.org/docs/Web/API/fetch#parameters).

### `options.cache`

Configure how the request should interact with Next.js [Data Cache](/docs/app/guides/caching.md#data-cache).

```ts
fetch(`https://...`, { cache: 'force-cache' | 'no-store' })
```

* **`auto no cache`** (default): Next.js fetches the resource from the remote server on every request in development, but will fetch once during `next build` because the route will be statically prerendered. If [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) are detected on the route, Next.js will fetch the resource on every request.
* **`no-store`**: Next.js fetches the resource from the remote server on every request, even if Dynamic APIs are not detected on the route.
* **`force-cache`**: Next.js looks for a matching request in its Data Cache.
  * If there is a match and it is fresh, it will be returned from the cache.
  * If there is no match or a stale match, Next.js will fetch the resource from the remote server and update the cache with the downloaded resource.

### `options.next.revalidate`

```ts
fetch(`https://...`, { next: { revalidate: false | 0 | number } })
```

Set the cache lifetime of a resource (in seconds). [Data Cache](/docs/app/guides/caching.md#data-cache).

* **`false`** - Cache the resource indefinitely. Semantically equivalent to `revalidate: Infinity`. The HTTP cache may evict older resources over time.
* **`0`** - Prevent the resource from being cached.
* **`number`** - (in seconds) Specify the resource should have a cache lifetime of at most `n` seconds.

> **Good to know**:
>
> * If an individual `fetch()` request sets a `revalidate` number lower than the [default `revalidate`](/docs/app/api-reference/file-conventions/route-segment-config.md#revalidate) of a route, the whole route revalidation interval will be decreased.
> * If two fetch requests with the same URL in the same route have different `revalidate` values, the lower value will be used.
> * Conflicting options such as `{ revalidate: 3600, cache: 'no-store' }` are not allowed, both will be ignored, and in development mode a warning will be printed to the terminal.

### `options.next.tags`

```ts
fetch(`https://...`, { next: { tags: ['collection'] } })
```

Set the cache tags of a resource. Data can then be revalidated on-demand using [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md). The max length for a custom tag is 256 characters and the max tag items is 128.

## Troubleshooting

### Fetch default `auto no store` and `cache: 'no-store'` not showing fresh data in development

Next.js caches `fetch` responses in Server Components across Hot Module Replacement (HMR) in local development for faster responses and to reduce costs for billed API calls.

By default, the [HMR cache](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache.md) applies to all fetch requests, including those with the default `auto no cache` and `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

See the [`serverComponentsHmrCache`](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache.md) docs for more information.

### Hard refresh and caching in development

In development mode, if the request includes the `cache-control: no-cache` header, `options.cache`, `options.next.revalidate`, and `options.next.tags` are ignored, and the `fetch` request is served from the source.

Browsers typically include `cache-control: no-cache` when the cache is disabled in developer tools or during a hard refresh.

## Version History

| Version   | Changes             |
| --------- | ------------------- |
| `v13.0.0` | `fetch` introduced. |


--------------------------------------------------------------------------------
title: "forbidden"
description: "API Reference for the forbidden function."
source: "https://nextjs.org/docs/app/api-reference/functions/forbidden"
--------------------------------------------------------------------------------

# forbidden

> This feature is currently experimental and subject to change, it is not recommended for production.

The `forbidden` function throws an error that renders a Next.js 403 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`forbidden.js` file](/docs/app/api-reference/file-conventions/forbidden.md).

To start using `forbidden`, enable the experimental [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts.md) configuration option in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  experimental: {
    authInterrupts: true,
  },
}
```

`forbidden` can be invoked in [Server Components](/docs/app/getting-started/server-and-client-components.md), [Server Actions](/docs/app/getting-started/updating-data.md), and [Route Handlers](/docs/app/api-reference/file-conventions/route.md).

```tsx filename="app/auth/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
  const session = await verifySession()

  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }

  // Render the admin page for authorized users
  return <></>
}
```

```jsx filename="app/auth/page.js" switcher
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
  const session = await verifySession()

  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }

  // Render the admin page for authorized users
  return <></>
}
```

## Good to know

* The `forbidden` function cannot be called in the [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout).

## Examples

### Role-based route protection

You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.

```tsx filename="app/admin/page.tsx" switcher
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
  const session = await verifySession()

  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }

  // Render the admin page for authorized users
  return (
    <main>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </main>
  )
}
```

```jsx filename="app/admin/page.js" switcher
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
  const session = await verifySession()

  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }

  // Render the admin page for authorized users
  return (
    <main>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </main>
  )
}
```

### Mutations with Server Actions

When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.

```ts filename="app/actions/update-role.ts" switcher
'use server'

import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateRole(formData: FormData) {
  const session = await verifySession()

  // Ensure only admins can update roles
  if (session.role !== 'admin') {
    forbidden()
  }

  // Perform the role update for authorized users
  // ...
}
```

```js filename="app/actions/update-role.js" switcher
'use server'

import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateRole(formData) {
  const session = await verifySession()

  // Ensure only admins can update roles
  if (session.role !== 'admin') {
    forbidden()
  }

  // Perform the role update for authorized users
  // ...
}
```

## Version History

| Version   | Changes                 |
| --------- | ----------------------- |
| `v15.1.0` | `forbidden` introduced. |
- [forbidden.js](/docs/app/api-reference/file-conventions/forbidden.md)
  - API reference for the forbidden.js special file.


--------------------------------------------------------------------------------
title: "generateImageMetadata"
description: "Learn how to generate multiple images in a single Metadata API special file."
source: "https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata"
--------------------------------------------------------------------------------

# generateImageMetadata

You can use `generateImageMetadata` to generate different versions of one image or return multiple images for one route segment. This is useful for when you want to avoid hard-coding metadata values, such as for icons.

## Parameters

`generateImageMetadata` function accepts the following parameters:

#### `params` (optional)

An object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) object from the root segment down to the segment `generateImageMetadata` is called from.

```tsx filename="icon.tsx" switcher
export function generateImageMetadata({
  params,
}: {
  params: { slug: string }
}) {
  // ...
}
```

```jsx filename="icon.js" switcher
export function generateImageMetadata({ params }) {
  // ...
}
```

| Route                           | URL         | `params`                  |
| ------------------------------- | ----------- | ------------------------- |
| `app/shop/icon.js`              | `/shop`     | `undefined`               |
| `app/shop/[slug]/icon.js`       | `/shop/1`   | `{ slug: '1' }`           |
| `app/shop/[tag]/[item]/icon.js` | `/shop/1/2` | `{ tag: '1', item: '2' }` |

## Returns

The `generateImageMetadata` function should return an `array` of objects containing the image's metadata such as `alt` and `size`. In addition, each item **must** include an `id` value which will be passed as a promise to the props of the image generating function.

| Image Metadata Object | Type                                |
| --------------------- | ----------------------------------- |
| `id`                  | `string` (required)                 |
| `alt`                 | `string`                            |
| `size`                | `{ width: number; height: number }` |
| `contentType`         | `string`                            |

```tsx filename="icon.tsx" switcher
import { ImageResponse } from 'next/og'

export function generateImageMetadata() {
  return [
    {
      contentType: 'image/png',
      size: { width: 48, height: 48 },
      id: 'small',
    },
    {
      contentType: 'image/png',
      size: { width: 72, height: 72 },
      id: 'medium',
    },
  ]
}

export default async function Icon({ id }: { id: Promise<string | number> }) {
  const iconId = await id
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 88,
          background: '#000',
          color: '#fafafa',
        }}
      >
        Icon {iconId}
      </div>
    )
  )
}
```

```jsx filename="icon.js" switcher
import { ImageResponse } from 'next/og'

export function generateImageMetadata() {
  return [
    {
      contentType: 'image/png',
      size: { width: 48, height: 48 },
      id: 'small',
    },
    {
      contentType: 'image/png',
      size: { width: 72, height: 72 },
      id: 'medium',
    },
  ]
}

export default async function Icon({ id }) {
  const iconId = await id
  return new ImageResponse(
    (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: 88,
          background: '#000',
          color: '#fafafa',
        }}
      >
        Icon {iconId}
      </div>
    )
  )
}
```

## Image generation function props

When using `generateImageMetadata`, the default export image generation function receives the following props:

#### `id`

A promise that resolves to the `id` value from one of the items returned by `generateImageMetadata`. The `id` will be a `string` or `number` depending on what was returned from `generateImageMetadata`.

```tsx filename="icon.tsx" switcher
export default async function Icon({ id }: { id: Promise<string | number> }) {
  const iconId = await id
  // Use iconId to generate the image
}
```

```jsx filename="icon.js" switcher
export default async function Icon({ id }) {
  const iconId = await id
  // Use iconId to generate the image
}
```

#### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) from the root segment down to the segment the image is colocated in.

```tsx filename="icon.tsx" switcher
export default async function Icon({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // Use slug to generate the image
}
```

```jsx filename="icon.js" switcher
export default async function Icon({ params }) {
  const { slug } = await params
  // Use slug to generate the image
}
```

### Examples

#### Using external data

This example uses the `params` object and external data to generate multiple [Open Graph images](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md) for a route segment.

```tsx filename="app/products/[id]/opengraph-image.tsx" switcher
import { ImageResponse } from 'next/og'
import { getCaptionForImage, getOGImages } from '@/app/utils/images'

export async function generateImageMetadata({
  params,
}: {
  params: { id: string }
}) {
  const images = await getOGImages(params.id)

  return images.map((image, idx) => ({
    id: idx,
    size: { width: 1200, height: 600 },
    alt: image.text,
    contentType: 'image/png',
  }))
}

export default async function Image({
  params,
  id,
}: {
  params: Promise<{ id: string }>
  id: Promise<number>
}) {
  const productId = (await params).id
  const imageId = await id
  const text = await getCaptionForImage(productId, imageId)

  return new ImageResponse(
    (
      <div
        style={
          {
            // ...
          }
        }
      >
        {text}
      </div>
    )
  )
}
```

```jsx filename="app/products/[id]/opengraph-image.js" switcher
import { ImageResponse } from 'next/og'
import { getCaptionForImage, getOGImages } from '@/app/utils/images'

export async function generateImageMetadata({ params }) {
  const images = await getOGImages(params.id)

  return images.map((image, idx) => ({
    id: idx,
    size: { width: 1200, height: 600 },
    alt: image.text,
    contentType: 'image/png',
  }))
}

export default async function Image({ params, id }) {
  const productId = (await params).id
  const imageId = await id
  const text = await getCaptionForImage(productId, imageId)

  return new ImageResponse(
    (
      <div
        style={
          {
            // ...
          }
        }
      >
        {text}
      </div>
    )
  )
}
```

## Version History

| Version   | Changes                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `id` passed to the Image generation function is now a promise that resolves to `string` or `number` |
| `v16.0.0` | `params` passed to the Image generation function is now a promise that resolves to an object        |
| `v13.3.0` | `generateImageMetadata` introduced.                                                                 |
## Next Steps

View all the Metadata API options.

- [Metadata Files](/docs/app/api-reference/file-conventions/metadata.md)
  - API documentation for the metadata file conventions.


--------------------------------------------------------------------------------
title: "generateMetadata"
description: "Learn how to add Metadata to your Next.js application for improved search engine optimization (SEO) and web shareability."
source: "https://nextjs.org/docs/app/api-reference/functions/generate-metadata"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./07-link-component.md) | [Index](./index.md) | [Next →](./09-generatemetadata.md)
