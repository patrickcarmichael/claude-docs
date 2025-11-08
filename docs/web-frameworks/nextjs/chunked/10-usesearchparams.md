**Navigation:** [← Previous](./09-generatemetadata.md) | [Index](./index.md) | [Next →](./11-staticgeneration.md)

---

# useSearchParams

`useSearchParams` is a **Client Component** hook that lets you read the current URL's **query string**.

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface.

```tsx filename="app/dashboard/search-bar.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```

```jsx filename="app/dashboard/search-bar.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```

## Parameters

```tsx
const searchParams = useSearchParams()
```

`useSearchParams` does not take any parameters.

## Returns

`useSearchParams` returns a **read-only** version of the [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) interface, which includes utility methods for reading the URL's query string:

* [`URLSearchParams.get()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/get): Returns the first value associated with the search parameter. For example:

  | URL                  | `searchParams.get("a")`                                                                                         |
  | -------------------- | --------------------------------------------------------------------------------------------------------------- |
  | `/dashboard?a=1`     | `'1'`                                                                                                           |
  | `/dashboard?a=`      | `''`                                                                                                            |
  | `/dashboard?b=3`     | `null`                                                                                                          |
  | `/dashboard?a=1&a=2` | `'1'` *- use [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll) to get all values* |

* [`URLSearchParams.has()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/has): Returns a boolean value indicating if the given parameter exists. For example:

  | URL              | `searchParams.has("a")` |
  | ---------------- | ----------------------- |
  | `/dashboard?a=1` | `true`                  |
  | `/dashboard?b=3` | `false`                 |

* Learn more about other **read-only** methods of [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams), including the [`getAll()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/getAll), [`keys()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/keys), [`values()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/values), [`entries()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/entries), [`forEach()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/forEach), and [`toString()`](https://developer.mozilla.org/docs/Web/API/URLSearchParams/toString).

> **Good to know**:
>
> * `useSearchParams` is a [Client Component](/docs/app/getting-started/server-and-client-components.md) hook and is **not supported** in [Server Components](/docs/app/getting-started/server-and-client-components.md) to prevent stale values during [partial rendering](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions).
> * If you want to fetch data in a Server Component based on search params, it's often a better option to read the [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) of the corresponding Page. You can then pass it down by props to any component (Server or Client) within that Page.
> * If an application includes the `/pages` directory, `useSearchParams` will return `ReadonlyURLSearchParams | null`. The `null` value is for compatibility during migration since search params cannot be known during pre-rendering of a page that doesn't use `getServerSideProps`

## Behavior

### Static Rendering

If a route is [statically rendered](/docs/app/guides/caching.md#static-rendering), calling `useSearchParams` will cause the Client Component tree up to the closest [`Suspense` boundary](/docs/app/api-reference/file-conventions/loading.md#examples) to be client-side rendered.

This allows a part of the route to be statically rendered while the dynamic part that uses `useSearchParams` is client-side rendered.

We recommend wrapping the Client Component that uses `useSearchParams` in a `<Suspense/>` boundary. This will allow any Client Components above it to be statically rendered and sent as part of initial HTML. [Example](/docs/app/api-reference/functions/use-search-params.md#static-rendering).

For example:

```tsx filename="app/dashboard/search-bar.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will not be logged on the server when using static rendering
  console.log(search)

  return <>Search: {search}</>
}
```

```jsx filename="app/dashboard/search-bar.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will not be logged on the server when using static rendering
  console.log(search)

  return <>Search: {search}</>
}
```

```tsx filename="app/dashboard/page.tsx" switcher
import { Suspense } from 'react'
import SearchBar from './search-bar'

// This component passed as a fallback to the Suspense boundary
// will be rendered in place of the search bar in the initial HTML.
// When the value is available during React hydration the fallback
// will be replaced with the `<SearchBar>` component.
function SearchBarFallback() {
  return <>placeholder</>
}

export default function Page() {
  return (
    <>
      <nav>
        <Suspense fallback={<SearchBarFallback />}>
          <SearchBar />
        </Suspense>
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import { Suspense } from 'react'
import SearchBar from './search-bar'

// This component passed as a fallback to the Suspense boundary
// will be rendered in place of the search bar in the initial HTML.
// When the value is available during React hydration the fallback
// will be replaced with the `<SearchBar>` component.
function SearchBarFallback() {
  return <>placeholder</>
}

export default function Page() {
  return (
    <>
      <nav>
        <Suspense fallback={<SearchBarFallback />}>
          <SearchBar />
        </Suspense>
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know**:
>
> * In development, routes are rendered on-demand, so `useSearchParams` doesn't suspend and things may appear to work without `Suspense`.
> * During production builds, a [static page](/docs/app/guides/caching.md#static-rendering) that calls `useSearchParams` from a Client Component must be wrapped in a `Suspense` boundary, otherwise the build fails with the [Missing Suspense boundary with useSearchParams](/docs/messages/missing-suspense-with-csr-bailout.md) error.
> * If you intend the route to be dynamically rendered, prefer using the [`connection`](/docs/app/api-reference/functions/connection.md) function first in a Server Component to wait for an incoming request, this excludes everything below from prerendering. See what makes a route dynamic in the [Dynamic Rendering guide](/docs/app/guides/caching.md#dynamic-rendering).
> * If you're already in a Server Component Page, consider using the [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) and passing the values to Client Components.
> * You can also pass the Page [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) directly to a Client Component and unwrap it with React's `use()`. Although this will suspend, so the Client Component should be wrapped with a `Suspense` boundary.

### Dynamic Rendering

If a route is [dynamically rendered](/docs/app/guides/caching.md#dynamic-rendering), `useSearchParams` will be available on the server during the initial server render of the Client Component.

For example:

```tsx filename="app/dashboard/search-bar.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will be logged on the server during the initial render
  // and on the client on subsequent navigations.
  console.log(search)

  return <>Search: {search}</>
}
```

```jsx filename="app/dashboard/search-bar.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will be logged on the server during the initial render
  // and on the client on subsequent navigations.
  console.log(search)

  return <>Search: {search}</>
}
```

```tsx filename="app/dashboard/page.tsx" switcher
import { connection } from 'next/server'
import SearchBar from './search-bar'

export default async function Page() {
  await connection()
  return (
    <>
      <nav>
        <SearchBar />
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import { connection } from 'next/server'
import SearchBar from './search-bar'

export default async function Page() {
  await connection()
  return (
    <>
      <nav>
        <SearchBar />
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know**:
>
> * Previously, setting `export const dynamic = 'force-dynamic'` on the page was used to force dynamic rendering. Prefer using [`connection()`](/docs/app/api-reference/functions/connection.md) instead, as it semantically ties dynamic rendering to the incoming request.

### Server Components

#### Pages

To access search params in [Pages](/docs/app/api-reference/file-conventions/page.md) (Server Components), use the [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) prop.

#### Layouts

Unlike Pages, [Layouts](/docs/app/api-reference/file-conventions/layout.md) (Server Components) **do not** receive the `searchParams` prop. This is because a shared layout is [not re-rendered during navigation](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions) which could lead to stale `searchParams` between navigations. View [detailed explanation](/docs/app/api-reference/file-conventions/layout.md#query-params).

Instead, use the Page [`searchParams`](/docs/app/api-reference/file-conventions/page.md) prop or the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params.md) hook in a Client Component, which is re-rendered on the client with the latest `searchParams`.

## Examples

### Updating `searchParams`

You can use [`useRouter`](/docs/app/api-reference/functions/use-router.md) or [`Link`](/docs/app/api-reference/components/link.md) to set new `searchParams`. After a navigation is performed, the current [`page.js`](/docs/app/api-reference/file-conventions/page.md) will receive an updated [`searchParams` prop](/docs/app/api-reference/file-conventions/page.md#searchparams-optional).

```tsx filename="app/example-client-component.tsx" switcher
'use client'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // Get a new searchParams string by merging the current
  // searchParams with a provided key/value pair
  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams.toString())
      params.set(name, value)

      return params.toString()
    },
    [searchParams]
  )

  return (
    <>
      <p>Sort By</p>

      {/* using useRouter */}
      <button
        onClick={() => {
          // <pathname>?sort=asc
          router.push(pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>

      {/* using <Link> */}
      <Link
        href={
          // <pathname>?sort=desc
          pathname + '?' + createQueryString('sort', 'desc')
        }
      >
        DESC
      </Link>
    </>
  )
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // Get a new searchParams string by merging the current
  // searchParams with a provided key/value pair
  const createQueryString = useCallback(
    (name, value) => {
      const params = new URLSearchParams(searchParams)
      params.set(name, value)

      return params.toString()
    },
    [searchParams]
  )

  return (
    <>
      <p>Sort By</p>

      {/* using useRouter */}
      <button
        onClick={() => {
          // <pathname>?sort=asc
          router.push(pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>

      {/* using <Link> */}
      <Link
        href={
          // <pathname>?sort=desc
          pathname + '?' + createQueryString('sort', 'desc')
        }
      >
        DESC
      </Link>
    </>
  )
}
```

## Version History

| Version   | Changes                       |
| --------- | ----------------------------- |
| `v13.0.0` | `useSearchParams` introduced. |


--------------------------------------------------------------------------------
title: "useSelectedLayoutSegment"
description: "API Reference for the useSelectedLayoutSegment hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment"
--------------------------------------------------------------------------------

# useSelectedLayoutSegment

`useSelectedLayoutSegment` is a **Client Component** hook that lets you read the active route segment **one level below** the Layout it is called from.

It is useful for navigation UI, such as tabs inside a parent layout that change style depending on the active child segment.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function ExampleClientComponent() {
  const segment = useSelectedLayoutSegment()

  return <p>Active segment: {segment}</p>
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function ExampleClientComponent() {
  const segment = useSelectedLayoutSegment()

  return <p>Active segment: {segment}</p>
}
```

> **Good to know**:
>
> * Since `useSelectedLayoutSegment` is a [Client Component](/docs/app/getting-started/server-and-client-components.md) hook, and Layouts are [Server Components](/docs/app/getting-started/server-and-client-components.md) by default, `useSelectedLayoutSegment` is usually called via a Client Component that is imported into a Layout.
> * `useSelectedLayoutSegment` only returns the segment one level down. To return all active segments, see [`useSelectedLayoutSegments`](/docs/app/api-reference/functions/use-selected-layout-segments.md)

## Parameters

```tsx
const segment = useSelectedLayoutSegment(parallelRoutesKey?: string)
```

`useSelectedLayoutSegment` *optionally* accepts a [`parallelRoutesKey`](/docs/app/api-reference/file-conventions/parallel-routes.md#with-useselectedlayoutsegments), which allows you to read the active route segment within that slot.

## Returns

`useSelectedLayoutSegment` returns a string of the active segment or `null` if one doesn't exist.

For example, given the Layouts and URLs below, the returned segment would be:

| Layout                    | Visited URL                    | Returned Segment |
| ------------------------- | ------------------------------ | ---------------- |
| `app/layout.js`           | `/`                            | `null`           |
| `app/layout.js`           | `/dashboard`                   | `'dashboard'`    |
| `app/dashboard/layout.js` | `/dashboard`                   | `null`           |
| `app/dashboard/layout.js` | `/dashboard/settings`          | `'settings'`     |
| `app/dashboard/layout.js` | `/dashboard/analytics`         | `'analytics'`    |
| `app/dashboard/layout.js` | `/dashboard/analytics/monthly` | `'analytics'`    |

## Examples

### Creating an active link component

You can use `useSelectedLayoutSegment` to create an active link component that changes style depending on the active segment. For example, a featured posts list in the sidebar of a blog:

```tsx filename="app/blog/blog-nav-link.tsx" switcher
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

// This *client* component will be imported into a blog layout
export default function BlogNavLink({
  slug,
  children,
}: {
  slug: string
  children: React.ReactNode
}) {
  // Navigating to `/blog/hello-world` will return 'hello-world'
  // for the selected layout segment
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment

  return (
    <Link
      href={`/blog/${slug}`}
      // Change style depending on whether the link is active
      style={{ fontWeight: isActive ? 'bold' : 'normal' }}
    >
      {children}
    </Link>
  )
}
```

```jsx filename="app/blog/blog-nav-link.js" switcher
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

// This *client* component will be imported into a blog layout
export default function BlogNavLink({ slug, children }) {
  // Navigating to `/blog/hello-world` will return 'hello-world'
  // for the selected layout segment
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment

  return (
    <Link
      href={`/blog/${slug}`}
      // Change style depending on whether the link is active
      style={{ fontWeight: isActive ? 'bold' : 'normal' }}
    >
      {children}
    </Link>
  )
}
```

```tsx filename="app/blog/layout.tsx" switcher
// Import the Client Component into a parent Layout (Server Component)
import { BlogNavLink } from './blog-nav-link'
import getFeaturedPosts from './get-featured-posts'

export default async function Layout({
  children,
}: {
  children: React.ReactNode
}) {
  const featuredPosts = await getFeaturedPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <BlogNavLink slug={post.slug}>{post.title}</BlogNavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```

```jsx filename="app/blog/layout.js" switcher
// Import the Client Component into a parent Layout (Server Component)
import { BlogNavLink } from './blog-nav-link'
import getFeaturedPosts from './get-featured-posts'

export default async function Layout({ children }) {
  const featuredPosts = await getFeaturedPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <BlogNavLink slug={post.slug}>{post.title}</BlogNavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```

## Version History

| Version   | Changes                                |
| --------- | -------------------------------------- |
| `v13.0.0` | `useSelectedLayoutSegment` introduced. |


--------------------------------------------------------------------------------
title: "useSelectedLayoutSegments"
description: "API Reference for the useSelectedLayoutSegments hook."
source: "https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments"
--------------------------------------------------------------------------------

# useSelectedLayoutSegments

`useSelectedLayoutSegments` is a **Client Component** hook that lets you read the active route segments **below** the Layout it is called from.

It is useful for creating UI in parent Layouts that need knowledge of active child segments such as breadcrumbs.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useSelectedLayoutSegments } from 'next/navigation'

export default function ExampleClientComponent() {
  const segments = useSelectedLayoutSegments()

  return (
    <ul>
      {segments.map((segment, index) => (
        <li key={index}>{segment}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useSelectedLayoutSegments } from 'next/navigation'

export default function ExampleClientComponent() {
  const segments = useSelectedLayoutSegments()

  return (
    <ul>
      {segments.map((segment, index) => (
        <li key={index}>{segment}</li>
      ))}
    </ul>
  )
}
```

> **Good to know**:
>
> * Since `useSelectedLayoutSegments` is a [Client Component](/docs/app/getting-started/server-and-client-components.md) hook, and Layouts are [Server Components](/docs/app/getting-started/server-and-client-components.md) by default, `useSelectedLayoutSegments` is usually called via a Client Component that is imported into a Layout.
> * The returned segments include [Route Groups](/docs/app/api-reference/file-conventions/route-groups.md), which you might not want to be included in your UI. You can use the [`filter`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) array method to remove items that start with a bracket.

## Parameters

```tsx
const segments = useSelectedLayoutSegments(parallelRoutesKey?: string)
```

`useSelectedLayoutSegments` *optionally* accepts a [`parallelRoutesKey`](/docs/app/api-reference/file-conventions/parallel-routes.md#with-useselectedlayoutsegments), which allows you to read the active route segment within that slot.

## Returns

`useSelectedLayoutSegments` returns an array of strings containing the active segments one level down from the layout the hook was called from. Or an empty array if none exist.

For example, given the Layouts and URLs below, the returned segments would be:

| Layout                    | Visited URL           | Returned Segments           |
| ------------------------- | --------------------- | --------------------------- |
| `app/layout.js`           | `/`                   | `[]`                        |
| `app/layout.js`           | `/dashboard`          | `['dashboard']`             |
| `app/layout.js`           | `/dashboard/settings` | `['dashboard', 'settings']` |
| `app/dashboard/layout.js` | `/dashboard`          | `[]`                        |
| `app/dashboard/layout.js` | `/dashboard/settings` | `['settings']`              |

## Version History

| Version   | Changes                                 |
| --------- | --------------------------------------- |
| `v13.0.0` | `useSelectedLayoutSegments` introduced. |


--------------------------------------------------------------------------------
title: "userAgent"
description: "The userAgent helper extends the Web Request API with additional properties and methods to interact with the user agent object from the request."
source: "https://nextjs.org/docs/app/api-reference/functions/userAgent"
--------------------------------------------------------------------------------

# userAgent

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
description: "Learn how to configure Next.js applications."
source: "https://nextjs.org/docs/app/api-reference/config"
--------------------------------------------------------------------------------

# Configuration



 - [next.config.js](/docs/app/api-reference/config/next-config-js.md)
 - [TypeScript](/docs/app/api-reference/config/typescript.md)
 - [ESLint](/docs/app/api-reference/config/eslint.md)

--------------------------------------------------------------------------------
title: "next.config.js"
description: "Learn how to configure your application with next.config.js."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js"
--------------------------------------------------------------------------------

# next.config.js

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

 - [experimental.adapterPath](/docs/app/api-reference/config/next-config-js/adapterPath.md)
 - [allowedDevOrigins](/docs/app/api-reference/config/next-config-js/allowedDevOrigins.md)
 - [appDir](/docs/app/api-reference/config/next-config-js/appDir.md)
 - [assetPrefix](/docs/app/api-reference/config/next-config-js/assetPrefix.md)
 - [authInterrupts](/docs/app/api-reference/config/next-config-js/authInterrupts.md)
 - [basePath](/docs/app/api-reference/config/next-config-js/basePath.md)
 - [browserDebugInfoInTerminal](/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal.md)
 - [cacheComponents](/docs/app/api-reference/config/next-config-js/cacheComponents.md)
 - [cacheLife](/docs/app/api-reference/config/next-config-js/cacheLife.md)
 - [compress](/docs/app/api-reference/config/next-config-js/compress.md)
 - [crossOrigin](/docs/app/api-reference/config/next-config-js/crossOrigin.md)
 - [cssChunking](/docs/app/api-reference/config/next-config-js/cssChunking.md)
 - [devIndicators](/docs/app/api-reference/config/next-config-js/devIndicators.md)
 - [distDir](/docs/app/api-reference/config/next-config-js/distDir.md)
 - [env](/docs/app/api-reference/config/next-config-js/env.md)
 - [expireTime](/docs/app/api-reference/config/next-config-js/expireTime.md)
 - [exportPathMap](/docs/app/api-reference/config/next-config-js/exportPathMap.md)
 - [generateBuildId](/docs/app/api-reference/config/next-config-js/generateBuildId.md)
 - [generateEtags](/docs/app/api-reference/config/next-config-js/generateEtags.md)
 - [headers](/docs/app/api-reference/config/next-config-js/headers.md)
 - [htmlLimitedBots](/docs/app/api-reference/config/next-config-js/htmlLimitedBots.md)
 - [httpAgentOptions](/docs/app/api-reference/config/next-config-js/httpAgentOptions.md)
 - [images](/docs/app/api-reference/config/next-config-js/images.md)
 - [cacheHandler](/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath.md)
 - [inlineCss](/docs/app/api-reference/config/next-config-js/inlineCss.md)
 - [isolatedDevBuild](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md)
 - [logging](/docs/app/api-reference/config/next-config-js/logging.md)
 - [mdxRs](/docs/app/api-reference/config/next-config-js/mdxRs.md)
 - [onDemandEntries](/docs/app/api-reference/config/next-config-js/onDemandEntries.md)
 - [optimizePackageImports](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md)
 - [output](/docs/app/api-reference/config/next-config-js/output.md)
 - [pageExtensions](/docs/app/api-reference/config/next-config-js/pageExtensions.md)
 - [poweredByHeader](/docs/app/api-reference/config/next-config-js/poweredByHeader.md)
 - [productionBrowserSourceMaps](/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps.md)
 - [proxyClientMaxBodySize](/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize.md)
 - [reactCompiler](/docs/app/api-reference/config/next-config-js/reactCompiler.md)
 - [reactMaxHeadersLength](/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength.md)
 - [reactStrictMode](/docs/app/api-reference/config/next-config-js/reactStrictMode.md)
 - [redirects](/docs/app/api-reference/config/next-config-js/redirects.md)
 - [rewrites](/docs/app/api-reference/config/next-config-js/rewrites.md)
 - [sassOptions](/docs/app/api-reference/config/next-config-js/sassOptions.md)
 - [serverActions](/docs/app/api-reference/config/next-config-js/serverActions.md)
 - [serverComponentsHmrCache](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache.md)
 - [serverExternalPackages](/docs/app/api-reference/config/next-config-js/serverExternalPackages.md)
 - [staleTimes](/docs/app/api-reference/config/next-config-js/staleTimes.md)
 - [staticGeneration*](/docs/app/api-reference/config/next-config-js/staticGeneration.md)
 - [taint](/docs/app/api-reference/config/next-config-js/taint.md)
 - [trailingSlash](/docs/app/api-reference/config/next-config-js/trailingSlash.md)
 - [transpilePackages](/docs/app/api-reference/config/next-config-js/transpilePackages.md)
 - [turbopack](/docs/app/api-reference/config/next-config-js/turbopack.md)
 - [turbopackFileSystemCache](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache.md)
 - [typedRoutes](/docs/app/api-reference/config/next-config-js/typedRoutes.md)
 - [typescript](/docs/app/api-reference/config/next-config-js/typescript.md)
 - [urlImports](/docs/app/api-reference/config/next-config-js/urlImports.md)
 - [useLightningcss](/docs/app/api-reference/config/next-config-js/useLightningcss.md)
 - [viewTransition](/docs/app/api-reference/config/next-config-js/viewTransition.md)
 - [webpack](/docs/app/api-reference/config/next-config-js/webpack.md)
 - [webVitalsAttribution](/docs/app/api-reference/config/next-config-js/webVitalsAttribution.md)

--------------------------------------------------------------------------------
title: "experimental.adapterPath"
description: "Configure a custom adapter for Next.js to hook into the build process with modifyConfig and onBuildComplete callbacks."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath"
--------------------------------------------------------------------------------

# experimental.adapterPath

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins"
--------------------------------------------------------------------------------

# allowedDevOrigins

Next.js does not automatically block cross-origin requests during development, but will block by default in a future major version of Next.js to prevent unauthorized requesting of internal assets/endpoints that are available in development mode.

To configure a Next.js application to allow requests from origins other than the hostname the server was initialized with (`localhost` by default) you can use the `allowedDevOrigins` config option.

`allowedDevOrigins` allows you to set additional origins that can be used in development mode. For example, to use `local-origin.dev` instead of only `localhost`, open `next.config.js` and add the `allowedDevOrigins` config:

```js filename="next.config.js"
module.exports = {
  allowedDevOrigins: ['local-origin.dev', '*.local-origin.dev'],
}
```


--------------------------------------------------------------------------------
title: "appDir"
description: "Enable the App Router to use layouts, streaming, and more."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir"
--------------------------------------------------------------------------------

# appDir

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

> **Good to know**: This option is **no longer** needed as of Next.js 13.4. The App Router is now stable.

The App Router ([`app` directory](/docs/app.md)) enables support for [layouts](/docs/app/api-reference/file-conventions/layout.md), [Server Components](/docs/app/getting-started/server-and-client-components.md), [streaming](/docs/app/api-reference/file-conventions/loading.md), and [colocated data fetching](/docs/app/getting-started/fetching-data.md).

Using the `app` directory will automatically enable [React Strict Mode](https://react.dev/reference/react/StrictMode). Learn how to [incrementally adopt `app`](/docs/app/guides/migrating/app-router-migration.md#migrating-from-pages-to-app).


--------------------------------------------------------------------------------
title: "assetPrefix"
description: "Learn how to use the assetPrefix config option to configure your CDN."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix"
--------------------------------------------------------------------------------

# assetPrefix

> **Attention**: [Deploying to Vercel](/docs/app/getting-started/deploying.md) automatically configures a global CDN for your Next.js project.
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

* Files in the [public](/docs/app/api-reference/file-conventions/public-folder.md) folder; if you want to serve those assets over a CDN, you'll have to introduce the prefix yourself


--------------------------------------------------------------------------------
title: "authInterrupts"
description: "Learn how to enable the experimental `authInterrupts` configuration option to use `forbidden` and `unauthorized`."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts"
--------------------------------------------------------------------------------

# authInterrupts

> This feature is currently available in the canary channel and subject to change.

The `authInterrupts` configuration option allows you to use [`forbidden`](/docs/app/api-reference/functions/forbidden.md) and [`unauthorized`](/docs/app/api-reference/functions/unauthorized.md) APIs in your application. While these functions are experimental, you must enable the `authInterrupts` option in your `next.config.js` file to use them:

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
- [forbidden](/docs/app/api-reference/functions/forbidden.md)
  - API Reference for the forbidden function.
- [unauthorized](/docs/app/api-reference/functions/unauthorized.md)
  - API Reference for the unauthorized function.
- [forbidden.js](/docs/app/api-reference/file-conventions/forbidden.md)
  - API reference for the forbidden.js special file.
- [unauthorized.js](/docs/app/api-reference/file-conventions/unauthorized.md)
  - API reference for the unauthorized.js special file.


--------------------------------------------------------------------------------
title: "basePath"
description: "Use `basePath` to deploy a Next.js application under a sub-path of a domain."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath"
--------------------------------------------------------------------------------

# basePath

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

When using the [`next/image`](/docs/app/api-reference/components/image.md) component, you will need to add the `basePath` in front of `src`.

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
title: "browserDebugInfoInTerminal"
description: "Forward browser console logs and errors to your terminal during development."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal"
--------------------------------------------------------------------------------

# browserDebugInfoInTerminal

> This feature is currently experimental and subject to change, it is not recommended for production.

The `experimental.browserDebugInfoInTerminal` option forwards console output and runtime errors originating in the browser to the dev server terminal.

This option is disabled by default. When enabled it only works in development mode.

## Usage

Enable forwarding:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    browserDebugInfoInTerminal: true,
  },
}

module.exports = nextConfig
```

### Serialization limits

Deeply nested objects/arrays are truncated using **sensible defaults**. You can tweak these limits:

* **depthLimit**: (optional) Limit stringification depth for nested objects/arrays. Default: 5
* **edgeLimit**: (optional) Max number of properties or elements to include per object or array. Default: 100

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      depthLimit: 5,
      edgeLimit: 100,
    },
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      depthLimit: 5,
      edgeLimit: 100,
    },
  },
}

module.exports = nextConfig
```

### Source location

Source locations are included by default when this feature is enabled.

```tsx filename="app/page.tsx" highlight={8}
'use client'

export default function Home() {
  return (
    <button
      type="button"
      onClick={() => {
        console.log('Hello World')
      }}
    >
      Click me
    </button>
  )
}
```

Clicking the button prints this message to the terminal.

```bash filename="Terminal"
[browser] Hello World (app/page.tsx:8:17)
```

To suppress them, set `showSourceLocation: false`.

* **showSourceLocation**: Include source location info when available.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      showSourceLocation: false,
    },
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    browserDebugInfoInTerminal: {
      showSourceLocation: false,
    },
  },
}

module.exports = nextConfig
```

| Version   | Changes                                              |
| --------- | ---------------------------------------------------- |
| `v15.4.0` | experimental `browserDebugInfoInTerminal` introduced |


--------------------------------------------------------------------------------
title: "cacheComponents"
description: "Learn how to enable the cacheComponents flag in Next.js."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents"
--------------------------------------------------------------------------------

# cacheComponents

The `cacheComponents` flag is a feature in Next.js that causes data fetching operations in the App Router to be excluded from pre-renders unless they are explicitly cached. This can be useful for optimizing the performance of dynamic data fetching in Server Components.

It is useful if your application requires fresh data fetching during runtime rather than serving from a pre-rendered cache.

It is expected to be used in conjunction with [`use cache`](/docs/app/api-reference/directives/use-cache.md) so that your data fetching happens at runtime by default unless you define specific parts of your application to be cached with `use cache` at the page, function, or component level.

## Usage

To enable the `cacheComponents` flag, set it to `true` in your `next.config.ts` file:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

When `cacheComponents` is enabled, you can use the following cache functions and configurations:

* The [`use cache` directive](/docs/app/api-reference/directives/use-cache.md)
* The [`cacheLife` function](/docs/app/api-reference/config/next-config-js/cacheLife.md) with `use cache`
* The [`cacheTag` function](/docs/app/api-reference/functions/cacheTag.md)

## Notes

* While `cacheComponents` can optimize performance by ensuring fresh data fetching during runtime, it may also introduce additional latency compared to serving pre-rendered content.

## Version History

| Version | Change                                                                                                                            |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 16.0.0  | `cacheComponents` introduced. This flag controls the `ppr`, `useCache`, and `dynamicIO` flags as a single, unified configuration. |


--------------------------------------------------------------------------------
title: "cacheLife"
description: "Learn how to set up cacheLife configurations in Next.js."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife"
--------------------------------------------------------------------------------

# cacheLife

The `cacheLife` option allows you to define **custom cache profiles** when using the [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md) function inside components or functions, and within the scope of the [`use cache` directive](/docs/app/api-reference/directives/use-cache.md).

## Usage

To define a profile, enable the [`cacheComponents` flag](/docs/app/api-reference/config/next-config-js/cacheComponents.md) and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    blog: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  cacheComponents: true,
  cacheLife: {
    blog: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}
```

You can now use this custom `blog` configuration in your component or function as follows:

```tsx filename="app/actions.ts" highlight={4,5} switcher
import { cacheLife } from 'next/cache'

export async function getCachedData() {
  'use cache'
  cacheLife('blog')
  const data = await fetch('/api/data')
  return data
}
```

```jsx filename="app/actions.js" highlight={4,5} switcher
import { cacheLife } from 'next/cache'

export async function getCachedData() {
  'use cache'
  cacheLife('blog')
  const data = await fetch('/api/data')
  return data
}
```

## Reference

The configuration object has key values with the following format:

| **Property** | **Value** | **Description**                                                                                           | **Requirement**                             |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `stale`      | `number`  | Duration the client should cache a value without checking the server.                                     | Optional                                    |
| `revalidate` | `number`  | Frequency at which the cache should refresh on the server; stale values may be served while revalidating. | Optional                                    |
| `expire`     | `number`  | Maximum duration for which a value can remain stale before switching to dynamic.                          | Optional - Must be longer than `revalidate` |


--------------------------------------------------------------------------------
title: "compress"
description: "Next.js provides gzip compression to compress rendered content and static files, it only works with the server target. Learn more about it here."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/compress"
--------------------------------------------------------------------------------

# compress

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin"
--------------------------------------------------------------------------------

# crossOrigin

Use the `crossOrigin` option to add a [`crossOrigin` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin) in all `<script>` tags generated by the [`next/script`](/docs/app/guides/scripts.md) component , and define how cross-origin requests should be handled.

```js filename="next.config.js"
module.exports = {
  crossOrigin: 'anonymous',
}
```

## Options

* `'anonymous'`: Adds [`crossOrigin="anonymous"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#anonymous) attribute.
* `'use-credentials'`: Adds [`crossOrigin="use-credentials"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin#use-credentials).


--------------------------------------------------------------------------------
title: "cssChunking"
description: "Use the `cssChunking` option to control how CSS files are chunked in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking"
--------------------------------------------------------------------------------

# cssChunking

> This feature is currently experimental and subject to change, it is not recommended for production.

CSS Chunking is a strategy used to improve the performance of your web application by splitting and re-ordering CSS files into chunks. This allows you to load only the CSS that is needed for a specific route, instead of loading all the application's CSS at once.

You can control how CSS files are chunked using the `experimental.cssChunking` option in your `next.config.js` file:

```tsx filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig = {
  experimental: {
    cssChunking: true, // default
  },
} satisfies NextConfig

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    cssChunking: true, // default
  },
}

module.exports = nextConfig
```

## Options

* **`true` (default)**: Next.js will try to merge CSS files whenever possible, determining explicit and implicit dependencies between files from import order to reduce the number of chunks and therefore the number of requests.
* **`false`**: Next.js will not attempt to merge or re-order your CSS files.
* **`'strict'`**: Next.js will load CSS files in the correct order they are imported into your files, which can lead to more chunks and requests.

You may consider using `'strict'` if you run into unexpected CSS behavior. For example, if you import `a.css` and `b.css` in different files using a different `import` order (`a` before `b`, or `b` before `a`), `true` will merge the files in any order and assume there are no dependencies between them. However, if `b.css` depends on `a.css`, you may want to use `'strict'` to prevent the files from being merged, and instead, load them in the order they are imported - which can result in more chunks and requests.

For most applications, we recommend `true` as it leads to fewer requests and better performance.


--------------------------------------------------------------------------------
title: "devIndicators"
description: "Configuration options for the on-screen indicator that gives context about the current route you're viewing during development."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators"
--------------------------------------------------------------------------------

# devIndicators

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

There are two reasons a route might opt out of static rendering:

* The presence of [Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering) which rely on runtime information.
* An [uncached data request](/docs/app/getting-started/fetching-data.md), like a call to an ORM or database driver.

Check your route for any of these conditions, and if you are not able to statically render the route, then consider using [`loading.js`](/docs/app/api-reference/file-conventions/loading.md) or [`<Suspense />`](https://react.dev/reference/react/Suspense) to leverage [streaming](/docs/app/getting-started/linking-and-navigating.md#streaming).

## Version History

| Version   | Changes                                                                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been removed.                                                             |
| `v15.2.0` | Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated. |
| `v15.0.0` | Static on-screen indicator added with `appIsrStatus` option.                                                                                        |


--------------------------------------------------------------------------------
title: "distDir"
description: "Set a custom build directory to use instead of the default .next directory."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir"
--------------------------------------------------------------------------------

# distDir

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/env"
--------------------------------------------------------------------------------

# env

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

> Since the release of [Next.js 9.4](https://nextjs.org/blog/next-9-4) we now have a more intuitive and ergonomic experience for [adding environment variables](/docs/app/guides/environment-variables.md). Give it a try!

> **Good to know**: environment variables specified in this way will **always** be included in the JavaScript bundle, prefixing the environment variable name with `NEXT_PUBLIC_` only has an effect when specifying them [through the environment or .env files](/docs/app/guides/environment-variables.md).

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
title: "expireTime"
description: "Customize stale-while-revalidate expire time for ISR enabled pages."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime"
--------------------------------------------------------------------------------

# expireTime

You can specify a custom `stale-while-revalidate` expire time for CDNs to consume in the `Cache-Control` header for ISR enabled pages.

Open `next.config.js` and add the `expireTime` config:

```js filename="next.config.js"
module.exports = {
  // one hour in seconds
  expireTime: 3600,
}
```

Now when sending the `Cache-Control` header the expire time will be calculated depending on the specific revalidate period.

For example, if you have a revalidate of 15 minutes on a path and the expire time is one hour the generated `Cache-Control` header will be `s-maxage=900, stale-while-revalidate=2700` so that it can stay stale for 15 minutes less than the configured expire time.


--------------------------------------------------------------------------------
title: "exportPathMap"
description: "Customize the pages that will be exported as HTML files when using `next export`."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap"
--------------------------------------------------------------------------------

# exportPathMap

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

[`next export`](/docs/app/guides/static-exports.md) will use `out` as the default output directory, you can customize this using the `-o` argument, like so:

```bash filename="Terminal"
next export -o outdir
```

> **Warning**: Using `exportPathMap` is deprecated and is overridden by `getStaticPaths` inside `pages`. We don't recommend using them together.


--------------------------------------------------------------------------------
title: "generateBuildId"
description: "Configure the build id, which is used to identify the current build in which your application is being served."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId"
--------------------------------------------------------------------------------

# generateBuildId

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags"
--------------------------------------------------------------------------------

# generateEtags

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/headers"
--------------------------------------------------------------------------------

# headers

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

When leveraging [`i18n` support](/docs/app/guides/internationalization.md) with headers each `source` is automatically prefixed to handle the configured `locales` unless you add `locale: false` to the header. If `locale: false` is used you must prefix the `source` with a locale for it to be matched correctly.

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

Learn more about [caching](/docs/app/guides/caching.md) with the App Router.

## Options

### CORS

[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/docs/Web/HTTP/CORS) is a security feature that allows you to control which sites can access your resources. You can set the `Access-Control-Allow-Origin` header to allow a specific origin to access your Route Handlers.

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
title: "htmlLimitedBots"
description: "Specify a list of user agents that should receive blocking metadata."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots"
--------------------------------------------------------------------------------

# htmlLimitedBots

The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of [streaming metadata](/docs/app/api-reference/functions/generate-metadata.md#streaming-metadata).

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
```

## Default list

Next.js includes a default list of HTML limited bots, including:

* Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
* Bingbot
* Twitterbot
* Slackbot

See the full list [here](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

```ts filename="next.config.ts" switcher
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
```

## Disabling

To fully disable streaming metadata:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /.*/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /.*/,
}
```

## Version History

| Version | Changes                              |
| ------- | ------------------------------------ |
| 15.2.0  | `htmlLimitedBots` option introduced. |


--------------------------------------------------------------------------------
title: "httpAgentOptions"
description: "Next.js will automatically use HTTP Keep-Alive by default. Learn more about how to disable HTTP Keep-Alive here."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions"
--------------------------------------------------------------------------------

# httpAgentOptions

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/images"
--------------------------------------------------------------------------------

# images

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
'use client'

export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

Alternatively, you can use the [`loader` prop](/docs/app/api-reference/components/image.md#loader) to pass the function to each instance of `next/image`.

> **Good to know**: Customizing the image loader file, which accepts a function, requires using [Client Components](/docs/app/getting-started/server-and-client-components.md) to serialize the provided function.

To learn more about configuring the behavior of the built-in [Image Optimization API](/docs/app/api-reference/components/image.md) and the [Image Component](/docs/app/api-reference/components/image.md), see [Image Configuration Options](/docs/app/api-reference/components/image.md#configuration-options) for available options.

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
title: "Custom Next.js Cache Handler"
description: "Configure the Next.js cache used for storing and revalidating data to use any external service like Redis, Memcached, or others."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath"
--------------------------------------------------------------------------------

# cacheHandler

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

> **Good to know**: The `cacheHandler` configuration is specifically used by Next.js for server cache operations such as storing and revalidating ISR and route handler responses. It is not used by `'use cache'`, `'use cache: remote'`, nor `'use cache: private'`, which manage their own cache independently.

```js filename="next.config.js"
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

View an example of a [custom cache handler](/docs/app/guides/self-hosting.md#configuring-caching) and learn more about the implementation.

## API Reference

The cache handler can implement the following methods: `get`, `set`, `revalidateTag`, and `resetRequestCache`.

### `get()`

| Parameter | Type     | Description                  |
| --------- | -------- | ---------------------------- |
| `key`     | `string` | The key to the cached value. |

Returns the cached value or `null` if not found.

### `set()`

| Parameter | Type           | Description                      |
| --------- | -------------- | -------------------------------- |
| `key`     | `string`       | The key to store the data under. |
| `data`    | Data or `null` | The data to be cached.           |
| `ctx`     | `{ tags: [] }` | The cache tags provided.         |

Returns `Promise<void>`.

### `revalidateTag()`

| Parameter | Type                   | Description                   |
| --------- | ---------------------- | ----------------------------- |
| `tag`     | `string` or `string[]` | The cache tags to revalidate. |

Returns `Promise<void>`. Learn more about [revalidating data](/docs/app/guides/incremental-static-regeneration.md) or the [`revalidateTag()`](/docs/app/api-reference/functions/revalidateTag.md) function.

### `resetRequestCache()`

This method resets the temporary in-memory cache for a single request before the next request.

Returns `void`.

**Good to know:**

* `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call your `revalidateTag` function, which you can then choose if you want to tag cache keys based on the path.

## Platform Support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure ISR](/docs/app/guides/self-hosting.md#caching-and-isr) when self-hosting Next.js.

## Version History

| Version   | Changes                                                      |
| --------- | ------------------------------------------------------------ |
| `v14.1.0` | Renamed to `cacheHandler` and became stable.                 |
| `v13.4.0` | `incrementalCacheHandlerPath` support for `revalidateTag`.   |
| `v13.4.0` | `incrementalCacheHandlerPath` support for standalone output. |
| `v12.2.0` | Experimental `incrementalCacheHandlerPath` added.            |


--------------------------------------------------------------------------------
title: "inlineCss"
description: "Enable inline CSS support."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss"
--------------------------------------------------------------------------------

# inlineCss

> This feature is currently experimental and subject to change, it is not recommended for production.

## Usage

Experimental support for inlining CSS in the `<head>`. When this flag is enabled, all places where we normally generate a `<link>` tag will instead have a generated `<style>` tag.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    inlineCss: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    inlineCss: true,
  },
}

module.exports = nextConfig
```

## Trade-Offs

### When to Use Inline CSS

Inlining CSS can be beneficial in several scenarios:

* **First-Time Visitors**: Since CSS files are render-blocking resources, inlining eliminates the initial download delay that first-time visitors experience, improving page load performance.

* **Performance Metrics**: By removing the additional network requests for CSS files, inlining can significantly improve key metrics like First Contentful Paint (FCP) and Largest Contentful Paint (LCP).

* **Slow Connections**: For users on slower networks where each request adds considerable latency, inlining CSS can provide a noticeable performance boost by reducing network roundtrips.

* **Atomic CSS Bundles (e.g., Tailwind)**: With utility-first frameworks like Tailwind CSS, the size of the styles required for a page is often O(1) relative to the complexity of the design. This makes inlining a compelling choice because the entire set of styles for the current page is lightweight and doesn’t grow with the page size. Inlining Tailwind styles ensures minimal payload and eliminates the need for additional network requests, which can further enhance performance.

### When Not to Use Inline CSS

While inlining CSS offers significant benefits for performance, there are scenarios where it may not be the best choice:

* **Large CSS Bundles**: If your CSS bundle is too large, inlining it may significantly increase the size of the HTML, resulting in slower Time to First Byte (TTFB) and potentially worse performance for users with slow connections.

* **Dynamic or Page-Specific CSS**: For applications with highly dynamic styles or pages that use different sets of CSS, inlining may lead to redundancy and bloat, as the full CSS for all pages may need to be inlined repeatedly.

* **Browser Caching**: In cases where visitors frequently return to your site, external CSS files allow browsers to cache styles efficiently, reducing data transfer for subsequent visits. Inlining CSS eliminates this benefit.

Evaluate these trade-offs carefully, and consider combining inlining with other strategies, such as critical CSS extraction or a hybrid approach, for the best results tailored to your site's needs.

> **Good to know**:
>
> This feature is currently experimental and has some known limitations:
>
> * CSS inlining is applied globally and cannot be configured on a per-page basis
> * Styles are duplicated during initial page load - once within `<style>` tags for SSR and once in the RSC payload
> * When navigating to statically rendered pages, styles will use `<link>` tags instead of inline CSS to avoid duplication
> * This feature is not available in development mode and only works in production builds


--------------------------------------------------------------------------------
title: "isolatedDevBuild"
description: "Use isolated build outputs for development server to prevent conflicts with production builds."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/isolatedDevBuild"
--------------------------------------------------------------------------------

# isolatedDevBuild

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
title: "logging"
description: "Configure how data fetches are logged to the console when running Next.js in development mode."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/logging"
--------------------------------------------------------------------------------

# logging

## Options

### Fetching

You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.

Currently, `logging` only applies to data fetching using the `fetch` API. It does not yet apply to other logs inside of Next.js.

```js filename="next.config.js"
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

Any `fetch` requests that are restored from the [Server Components HMR cache](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache.md) are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.

```js filename="next.config.js"
module.exports = {
  logging: {
    fetches: {
      hmrRefreshes: true,
    },
  },
}
```

### Incoming Requests

By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore.
Since this is only logged in development, this option doesn't affect production builds.

```js filename="next.config.js"
module.exports = {
  logging: {
    incomingRequests: {
      ignore: [/\api\/v1\/health/],
    },
  },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.

```js filename="next.config.js"
module.exports = {
  logging: {
    incomingRequests: false,
  },
}
```

### Disabling Logging

In addition, you can disable the development logging by setting `logging` to `false`.

```js filename="next.config.js"
module.exports = {
  logging: false,
}
```


--------------------------------------------------------------------------------
title: "mdxRs"
description: "Use the new Rust compiler to compile MDX files in the App Router."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs"
--------------------------------------------------------------------------------

# mdxRs

> This feature is currently experimental and subject to change, it is not recommended for production.

For experimental use with `@next/mdx`. Compiles MDX files using the new Rust compiler.

```js filename="next.config.js"
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['ts', 'tsx', 'mdx'],
  experimental: {
    mdxRs: true,
  },
}

module.exports = withMDX(nextConfig)
```


--------------------------------------------------------------------------------
title: "onDemandEntries"
description: "Configure how Next.js will dispose and keep in memory pages created in development."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries"
--------------------------------------------------------------------------------

# onDemandEntries

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports"
--------------------------------------------------------------------------------

# optimizePackageImports

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/output"
--------------------------------------------------------------------------------

# output

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions"
--------------------------------------------------------------------------------

# pageExtensions

By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).

```js filename="next.config.js"
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

module.exports = withMDX(nextConfig)
```


--------------------------------------------------------------------------------
title: "poweredByHeader"
description: "Next.js will add the `x-powered-by` header by default. Learn to opt-out of it here."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader"
--------------------------------------------------------------------------------

# poweredByHeader

By default Next.js will add the `x-powered-by` header. To opt-out of it, open `next.config.js` and disable the `poweredByHeader` config:

```js filename="next.config.js"
module.exports = {
  poweredByHeader: false,
}
```


--------------------------------------------------------------------------------
title: "productionBrowserSourceMaps"
description: "Enables browser source map generation during the production build."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps"
--------------------------------------------------------------------------------

# productionBrowserSourceMaps

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/proxyClientMaxBodySize"
--------------------------------------------------------------------------------

# proxyClientMaxBodySize

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
title: "reactCompiler"
description: "Enable the React Compiler to automatically optimize component rendering."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler"
--------------------------------------------------------------------------------

# reactCompiler

Next.js includes support for the [React Compiler](https://react.dev/learn/react-compiler/introduction), a tool designed to improve performance by automatically optimizing component rendering. This reduces the need for manual memoization using `useMemo` and `useCallback`.

Next.js includes a custom performance optimization written in SWC that makes the React Compiler more efficient. Instead of running the compiler on every file, Next.js analyzes your project and only applies the React Compiler to relevant files. This avoids unnecessary work and leads to faster builds compared to using the Babel plugin on its own.

## How It Works

The React Compiler runs through a Babel plugin. To keep builds fast, Next.js uses a custom SWC optimization that only applies the React Compiler to relevant files—like those with JSX or React Hooks.

This avoids compiling everything and keeps the performance cost minimal. You may still see slightly slower builds compared to the default Rust-based compiler, but the impact is small and localized.

To use it, install the `babel-plugin-react-compiler`:

```bash filename="Terminal"
npm install -D babel-plugin-react-compiler
```

Then, add `reactCompiler` option in `next.config.js`:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactCompiler: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactCompiler: true,
}

module.exports = nextConfig
```

## Annotations

You can configure the compiler to run in "opt-in" mode as follows:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  reactCompiler: {
    compilationMode: 'annotation',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactCompiler: {
    compilationMode: 'annotation',
  },
}

module.exports = nextConfig
```

Then, you can annotate specific components or hooks with the `"use memo"` directive from React to opt-in:

```ts filename="app/page.tsx" switcher
export default function Page() {
  'use memo'
  // ...
}
```

```js filename="app/page.js" switcher
export default function Page() {
  'use memo'
  // ...
}
```

> **Note:** You can also use the `"use no memo"` directive from React for the opposite effect, to opt-out a component or hook.


--------------------------------------------------------------------------------
title: "reactMaxHeadersLength"
description: "The maximum length of the headers that are emitted by React and added to the response."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength"
--------------------------------------------------------------------------------

# reactMaxHeadersLength

During static rendering, React can emit headers that can be added to the response. These can be used to improve performance by allowing the browser to preload resources like fonts, scripts, and stylesheets. The default value is `6000`, but you can override this value by configuring the `reactMaxHeadersLength` option in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  reactMaxHeadersLength: 1000,
}
```

> **Good to know**: This option is only available in App Router.

Depending on the type of proxy between the browser and the server, the headers can be truncated. For example, if you are using a reverse proxy that doesn't support long headers, you should set a lower value to ensure that the headers are not truncated.


--------------------------------------------------------------------------------
title: "reactStrictMode"
description: "The complete Next.js runtime is now Strict Mode-compliant, learn how to opt-in"
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode"
--------------------------------------------------------------------------------

# reactStrictMode

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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects"
--------------------------------------------------------------------------------

# redirects

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

When implementing redirects with internationalization in the App Router, you can include locales in `next.config.js` redirects, but only as hardcoded paths.

For dynamic or per-request locale handling, use [dynamic route segments and proxy](/docs/app/guides/internationalization.md), which can redirect based on the user's preferred language.

```js filename="next.config.js"
module.exports = {
  async redirects() {
    return [
      {
        // Manually handle locale prefixes for App Router
        source: '/en/old-path',
        destination: '/en/new-path',
        permanent: false,
      },
      {
        // Redirect for all locales using a parameter
        source: '/:locale/old-path',
        destination: '/:locale/new-path',
        permanent: false,
      },
      {
        // Redirect from one locale to another
        source: '/de/old-path',
        destination: '/en/new-path',
        permanent: false,
      },
      {
        // Catch-all redirect for multiple locales
        source: '/:locale(en|fr|de)/:path*',
        destination: '/:locale/new-section/:path*',
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
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites"
--------------------------------------------------------------------------------

# rewrites

Rewrites allow you to map an incoming request path to a different destination path.

Rewrites act as a URL proxy and mask the destination path, making it appear the user hasn't changed their location on the site. In contrast, [redirects](/docs/app/api-reference/config/next-config-js/redirects.md) will reroute to a new page and show the URL changes.

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

1. [headers](/docs/app/api-reference/config/next-config-js/headers.md) are checked/applied
2. [redirects](/docs/app/api-reference/config/next-config-js/redirects.md) are checked/applied
3. [proxy](/docs/app/api-reference/file-conventions/proxy.md)
4. `beforeFiles` rewrites are checked/applied
5. static files from the [public directory](/docs/app/api-reference/file-conventions/public-folder.md), `_next/static` files, and non-dynamic pages are checked/served
6. `afterFiles` rewrites are checked/applied, if one of these rewrites is matched we check dynamic routes/static files after each match
7. `fallback` rewrites are checked/applied, these are applied before rendering the 404 page and after dynamic routes/all static assets have been checked. If you use [fallback: true/'blocking'](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true) in `getStaticPaths`, the fallback `rewrites` defined in your `next.config.js` will *not* be run.

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

## Version History

| Version   | Changes          |
| --------- | ---------------- |
| `v13.3.0` | `missing` added. |
| `v10.2.0` | `has` added.     |
| `v9.5.0`  | Headers added.   |


--------------------------------------------------------------------------------
title: "sassOptions"
description: "Configure Sass options."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions"
--------------------------------------------------------------------------------

# sassOptions

`sassOptions` allow you to configure the Sass compiler.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const sassOptions = {
  additionalData: `
    $var: red;
  `,
}

const nextConfig: NextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const sassOptions = {
  additionalData: `
    $var: red;
  `,
}

const nextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}

module.exports = nextConfig
```

> **Good to know:**
>
> * `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
> * The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.


--------------------------------------------------------------------------------
title: "serverActions"
description: "Configure Server Actions behavior in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions"
--------------------------------------------------------------------------------

# serverActions

Options for configuring Server Actions behavior in your Next.js application.

## `allowedOrigins`

A list of extra safe origin domains from which Server Actions can be invoked. Next.js compares the origin of a Server Action request with the host domain, ensuring they match to prevent CSRF attacks. If not provided, only the same origin is allowed.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */

module.exports = {
  experimental: {
    serverActions: {
      allowedOrigins: ['my-proxy.com', '*.my-proxy.com'],
    },
  },
}
```

## `bodySizeLimit`

By default, the maximum size of the request body sent to a Server Action is 1MB, to prevent the consumption of excessive server resources in parsing large amounts of data, as well as potential DDoS attacks.

However, you can configure this limit using the `serverActions.bodySizeLimit` option. It can take the number of bytes or any string format supported by bytes, for example `1000`, `'500kb'` or `'3mb'`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */

module.exports = {
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
}
```

## Enabling Server Actions (v13)

Server Actions became a stable feature in Next.js 14, and are enabled by default. However, if you are using an earlier version of Next.js, you can enable them by setting `experimental.serverActions` to `true`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const config = {
  experimental: {
    serverActions: true,
  },
}

module.exports = config
```


--------------------------------------------------------------------------------
title: "serverComponentsHmrCache"
description: "Configure whether fetch responses in Server Components are cached across HMR refresh requests."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache"
--------------------------------------------------------------------------------

# serverComponentsHmrCache

> This feature is currently experimental and subject to change, it is not recommended for production.

The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

By default, the HMR cache applies to all `fetch` requests, including those with the `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.

You can disable the HMR cache by setting `serverComponentsHmrCache` to `false` in your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    serverComponentsHmrCache: false, // defaults to true
  },
}

module.exports = nextConfig
```

> **Good to know:** For better observability, we recommend using the [`logging.fetches`](/docs/app/api-reference/config/next-config-js/logging.md) option which logs fetch cache hits and misses in the console during development.


--------------------------------------------------------------------------------
title: "serverExternalPackages"
description: "Opt-out specific dependencies from the Server Components bundling and use native Node.js `require`."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages"
--------------------------------------------------------------------------------

# serverExternalPackages

Dependencies used inside [Server Components](/docs/app/getting-started/server-and-client-components.md) and [Route Handlers](/docs/app/api-reference/file-conventions/route.md) will automatically be bundled by Next.js.

If a dependency is using Node.js specific features, you can choose to opt-out specific dependencies from the Server Components bundling and use native Node.js `require`.

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

| Version   | Changes                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------- |
| `v15.0.0` | Moved from experimental to stable. Renamed from `serverComponentsExternalPackages` to `serverExternalPackages` |


--------------------------------------------------------------------------------
title: "staleTimes"
description: "Learn how to override the invalidation time of the Client Router Cache."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes"
--------------------------------------------------------------------------------

# staleTimes

> This feature is currently experimental and subject to change, it is not recommended for production.

`staleTimes` is an experimental feature that enables caching of page segments in the [client-side router cache](/docs/app/guides/caching.md#client-side-router-cache).

You can enable this experimental feature and provide custom revalidation times by setting the experimental `staleTimes` flag:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    staleTimes: {
      dynamic: 30,
      static: 180,
    },
  },
}

module.exports = nextConfig
```

The `static` and `dynamic` properties correspond with the time period (in seconds) based on different types of [link prefetching](/docs/app/api-reference/components/link.md#prefetch).

* The `dynamic` property is used when the page is neither statically generated nor fully prefetched (e.g. with `prefetch={true}`).
  * Default: 0 seconds (not cached)
* The `static` property is used for statically generated pages, or when the `prefetch` prop on `Link` is set to `true`, or when calling [`router.prefetch`](/docs/app/guides/caching.md#routerprefetch).
  * Default: 5 minutes

> **Good to know:**
>
> * [Loading boundaries](/docs/app/api-reference/file-conventions/loading.md) are considered reusable for the `static` period defined in this configuration.
> * This doesn't affect [partial rendering](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions), **meaning shared layouts won't automatically be refetched on every navigation, only the page segment that changes.**
> * This doesn't change [back/forward caching](/docs/app/guides/caching.md#client-side-router-cache) behavior to prevent layout shift and to prevent losing the browser scroll position.

You can learn more about the Client Router Cache [here](/docs/app/guides/caching.md#client-side-router-cache).

### Version History

| Version   | Changes                                                    |
| --------- | ---------------------------------------------------------- |
| `v15.0.0` | The `dynamic` `staleTimes` default changed from 30s to 0s. |
| `v14.2.0` | Experimental `staleTimes` introduced.                      |


--------------------------------------------------------------------------------
title: "staticGeneration*"
description: "Learn how to configure static generation in your Next.js application."
source: "https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./09-generatemetadata.md) | [Index](./index.md) | [Next →](./11-staticgeneration.md)
