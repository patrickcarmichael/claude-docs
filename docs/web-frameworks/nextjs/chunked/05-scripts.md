**Navigation:** [← Previous](./04-app-router.md) | [Index](./index.md) | [Next →](./06-videos.md)

---

# Scripts

### Layout Scripts

To load a third-party script for multiple routes, import `next/script` and include the script directly in your layout component:

```tsx filename="app/dashboard/layout.tsx" switcher
import Script from 'next/script'

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <>
      <section>{children}</section>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

```jsx filename="app/dashboard/layout.js" switcher
import Script from 'next/script'

export default function DashboardLayout({ children }) {
  return (
    <>
      <section>{children}</section>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

The third-party script is fetched when the folder route (e.g. `dashboard/page.js`) or any nested route (e.g. `dashboard/settings/page.js`) is accessed by the user. Next.js will ensure the script will **only load once**, even if a user navigates between multiple routes in the same layout.

### Application Scripts

To load a third-party script for all routes, import `next/script` and include the script directly in your root layout:

```tsx filename="app/layout.tsx" switcher
import Script from 'next/script'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <Script src="https://example.com/script.js" />
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import Script from 'next/script'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
      <Script src="https://example.com/script.js" />
    </html>
  )
}
```

This script will load and execute when *any* route in your application is accessed. Next.js will ensure the script will **only load once**, even if a user navigates between multiple pages.

> **Recommendation**: We recommend only including third-party scripts in specific pages or layouts in order to minimize any unnecessary impact to performance.

### Strategy

Although the default behavior of `next/script` allows you to load third-party scripts in any page or layout, you can fine-tune its loading behavior by using the `strategy` property:

* `beforeInteractive`: Load the script before any Next.js code and before any page hydration occurs.
* `afterInteractive`: (**default**) Load the script early but after some hydration on the page occurs.
* `lazyOnload`: Load the script later during browser idle time.
* `worker`: (experimental) Load the script in a web worker.

Refer to the [`next/script`](/docs/app/api-reference/components/script.md#strategy) API reference documentation to learn more about each strategy and their use cases.

### Offloading Scripts To A Web Worker (experimental)

> **Warning:** The `worker` strategy is not yet stable and does not yet work with the App Router. Use with caution.

Scripts that use the `worker` strategy are offloaded and executed in a web worker with [Partytown](https://partytown.builder.io/). This can improve the performance of your site by dedicating the main thread to the rest of your application code.

This strategy is still experimental and can only be used if the `nextScriptWorkers` flag is enabled in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  experimental: {
    nextScriptWorkers: true,
  },
}
```

Then, run `next` (normally `npm run dev` or `yarn dev`) and Next.js will guide you through the installation of the required packages to finish the setup:

```bash filename="Terminal"
npm run dev
```

You'll see instructions like these: Please install Partytown by running `npm install @builder.io/partytown`

Once setup is complete, defining `strategy="worker"` will automatically instantiate Partytown in your application and offload the script to a web worker.

```tsx filename="pages/home.tsx" switcher
import Script from 'next/script'

export default function Home() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="worker" />
    </>
  )
}
```

```jsx filename="pages/home.js" switcher
import Script from 'next/script'

export default function Home() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="worker" />
    </>
  )
}
```

There are a number of trade-offs that need to be considered when loading a third-party script in a web worker. Please see Partytown's [tradeoffs](https://partytown.builder.io/trade-offs) documentation for more information.

### Inline Scripts

Inline scripts, or scripts not loaded from an external file, are also supported by the Script component. They can be written by placing the JavaScript within curly braces:

```jsx
<Script id="show-banner">
  {`document.getElementById('banner').classList.remove('hidden')`}
</Script>
```

Or by using the `dangerouslySetInnerHTML` property:

```jsx
<Script
  id="show-banner"
  dangerouslySetInnerHTML={{
    __html: `document.getElementById('banner').classList.remove('hidden')`,
  }}
/>
```

> **Warning**: An `id` property must be assigned for inline scripts in order for Next.js to track and optimize the script.

### Executing Additional Code

Event handlers can be used with the Script component to execute additional code after a certain event occurs:

* `onLoad`: Execute code after the script has finished loading.
* `onReady`: Execute code after the script has finished loading and every time the component is mounted.
* `onError`: Execute code if the script fails to load.

These handlers will only work when `next/script` is imported and used inside of a [Client Component](/docs/app/getting-started/server-and-client-components.md) where `"use client"` is defined as the first line of code:

```tsx filename="app/page.tsx" switcher
'use client'

import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onLoad={() => {
          console.log('Script has loaded')
        }}
      />
    </>
  )
}
```

```jsx filename="app/page.js" switcher
'use client'

import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onLoad={() => {
          console.log('Script has loaded')
        }}
      />
    </>
  )
}
```

Refer to the [`next/script`](/docs/app/api-reference/components/script.md#onload) API reference to learn more about each event handler and view examples.

### Additional Attributes

There are many DOM attributes that can be assigned to a `<script>` element that are not used by the Script component, like [`nonce`](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce) or [custom data attributes](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/data-*). Including any additional attributes will automatically forward it to the final, optimized `<script>` element that is included in the HTML.

```tsx filename="app/page.tsx" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        id="example-script"
        nonce="XUENAJFW"
        data-test="script"
      />
    </>
  )
}
```

```jsx filename="app/page.js" switcher
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        id="example-script"
        nonce="XUENAJFW"
        data-test="script"
      />
    </>
  )
}
```
## API Reference

Learn more about the next/script API.

- [Script Component](/docs/app/api-reference/components/script.md)
  - Optimize third-party scripts in your Next.js application using the built-in `next/script` Component.


--------------------------------------------------------------------------------
title: "How to self-host your Next.js application"
description: "Learn how to self-host your Next.js application on a Node.js server, Docker image, or static HTML files (static exports)."
source: "https://nextjs.org/docs/app/guides/self-hosting"
--------------------------------------------------------------------------------

# Self-Hosting

When [deploying](/docs/app/getting-started/deploying.md) your Next.js app, you may want to configure how different features are handled based on your infrastructure.

> **🎥 Watch:** Learn more about self-hosting Next.js → [YouTube (45 minutes)](https://www.youtube.com/watch?v=sIVL4JMqRfc).

## Reverse Proxy

When self-hosting, it's recommended to use a reverse proxy (like nginx) in front of your Next.js server rather than exposing it directly to the internet. A reverse proxy can handle malformed requests, slow connection attacks, payload size limits, rate limiting, and other security concerns, offloading these tasks from the Next.js server. This allows the server to dedicate its resources to rendering rather than request validation.

## Image Optimization

[Image Optimization](/docs/app/api-reference/components/image.md) through `next/image` works self-hosted with zero configuration when deploying using `next start`. If you would prefer to have a separate service to optimize images, you can [configure an image loader](/docs/app/api-reference/components/image.md#loader).

Image Optimization can be used with a [static export](/docs/app/guides/static-exports.md#image-optimization) by defining a custom image loader in `next.config.js`. Note that images are optimized at runtime, not during the build.

> **Good to know:**
>
> * On glibc-based Linux systems, Image Optimization may require [additional configuration](https://sharp.pixelplumbing.com/install#linux-memory-allocator) to prevent excessive memory usage.
> * Learn more about the [caching behavior of optimized images](/docs/app/api-reference/components/image.md#minimumcachettl) and how to configure the TTL.
> * You can also [disable Image Optimization](/docs/app/api-reference/components/image.md#unoptimized) and still retain other benefits of using `next/image` if you prefer. For example, if you are optimizing images yourself separately.

## Proxy

[Proxy](/docs/app/api-reference/file-conventions/proxy.md) works self-hosted with zero configuration when deploying using `next start`. Since it requires access to the incoming request, it is not supported when using a [static export](/docs/app/guides/static-exports.md).

Proxy uses the [Edge runtime](/docs/app/api-reference/edge.md), a subset of all available Node.js APIs to help ensure low latency, since it may run in front of every route or asset in your application. If you do not want this, you can use the [full Node.js runtime](/blog/next-15-2#nodejs-middleware-experimental) to run Proxy.

If you are looking to add logic (or use an external package) that requires all Node.js APIs, you might be able to move this logic to a [layout](/docs/app/api-reference/file-conventions/layout.md) as a [Server Component](/docs/app/getting-started/server-and-client-components.md). For example, checking [headers](/docs/app/api-reference/functions/headers.md) and [redirecting](/docs/app/api-reference/functions/redirect.md). You can also use headers, cookies, or query parameters to [redirect](/docs/app/api-reference/config/next-config-js/redirects.md#header-cookie-and-query-matching) or [rewrite](/docs/app/api-reference/config/next-config-js/rewrites.md#header-cookie-and-query-matching) through `next.config.js`. If that does not work, you can also use a [custom server](/docs/pages/guides/custom-server.md).

## Environment Variables

Next.js can support both build time and runtime environment variables.

**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.

You safely read environment variables on the server during dynamic rendering.

```tsx filename="app/page.ts" switcher
import { connection } from 'next/server'

export default async function Component() {
  await connection()
  // cookies, headers, and other Dynamic APIs
  // will also opt into dynamic rendering, meaning
  // this env variable is evaluated at runtime
  const value = process.env.MY_VALUE
  // ...
}
```

```jsx filename="app/page.js" switcher
import { connection } from 'next/server'

export default async function Component() {
  await connection()
  // cookies, headers, and other Dynamic APIs
  // will also opt into dynamic rendering, meaning
  // this env variable is evaluated at runtime
  const value = process.env.MY_VALUE
  // ...
}
```

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.

> **Good to know:**
>
> * You can run code on server startup using the [`register` function](/docs/app/guides/instrumentation.md).

## Caching and ISR

Next.js can cache responses, generated static pages, build outputs, and other static assets like images, fonts, and scripts.

Caching and revalidating pages (with [Incremental Static Regeneration](/docs/app/guides/incremental-static-regeneration.md)) use the **same shared cache**. By default, this cache is stored to the filesystem (on disk) on your Next.js server. **This works automatically when self-hosting** using both the Pages and App Router.

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.

### Automatic Caching

* Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` to truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](/docs/app/getting-started/images.md#local-images). You can [configure the TTL](/docs/app/api-reference/components/image.md#minimumcachettl) for images.
* Incremental Static Regeneration (ISR) sets the `Cache-Control` header of `s-maxage: <revalidate in getStaticProps>, stale-while-revalidate`. This revalidation time is defined in your [`getStaticProps` function](/docs/pages/building-your-application/data-fetching/get-static-props.md) in seconds. If you set `revalidate: false`, it will default to a one-year cache duration.
* Dynamically rendered pages set a `Cache-Control` header of `private, no-cache, no-store, max-age=0, must-revalidate` to prevent user-specific data from being cached. This applies to both the App Router and Pages Router. This also includes [Draft Mode](/docs/app/guides/draft-mode.md).

### Static Assets

If you want to host static assets on a different domain or CDN, you can use the `assetPrefix` [configuration](/docs/app/api-reference/config/next-config-js/assetPrefix.md) in `next.config.js`. Next.js will use this asset prefix when retrieving JavaScript or CSS files. Separating your assets to a different domain does come with the downside of extra time spent on DNS and TLS resolution.

[Learn more about `assetPrefix`](/docs/app/api-reference/config/next-config-js/assetPrefix.md).

### Configuring Caching

By default, generated cache assets will be stored in memory (defaults to 50mb) and on disk. If you are hosting Next.js using a container orchestration platform like Kubernetes, each pod will have a copy of the cache. To prevent stale data from being shown since the cache is not shared between pods by default, you can configure the Next.js cache to provide a cache handler and disable in-memory caching.

To configure the ISR/Data Cache location when self-hosting, you can configure a custom handler in your `next.config.js` file:

```jsx filename="next.config.js"
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

Then, create `cache-handler.js` in the root of your project, for example:

```jsx filename="cache-handler.js"
const cache = new Map()

module.exports = class CacheHandler {
  constructor(options) {
    this.options = options
  }

  async get(key) {
    // This could be stored anywhere, like durable storage
    return cache.get(key)
  }

  async set(key, data, ctx) {
    // This could be stored anywhere, like durable storage
    cache.set(key, {
      value: data,
      lastModified: Date.now(),
      tags: ctx.tags,
    })
  }

  async revalidateTag(tags) {
    // tags is either a string or an array of strings
    tags = [tags].flat()
    // Iterate over all entries in the cache
    for (let [key, value] of cache) {
      // If the value's tags include the specified tag, delete this entry
      if (value.tags.some((tag) => tags.includes(tag))) {
        cache.delete(key)
      }
    }
  }

  // If you want to have temporary in memory cache for a single request that is reset
  // before the next request you can leverage this method
  resetRequestCache() {}
}
```

Using a custom cache handler will allow you to ensure consistency across all pods hosting your Next.js application. For instance, you can save the cached values anywhere, like [Redis](https://github.com/vercel/next.js/tree/canary/examples/cache-handler-redis) or AWS S3.

> **Good to know:**
>
> * `revalidatePath` is a convenience layer on top of cache tags. Calling `revalidatePath` will call the `revalidateTag` function with a special default tag for the provided page.

## Build Cache

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

## Version Skew

Next.js will automatically mitigate most instances of [version skew](https://www.industrialempathy.com/posts/version-skew/) and automatically reload the application to retrieve new assets when detected. For example, if there is a mismatch in the `deploymentId`, transitions between pages will perform a hard navigation versus using a prefetched value.

When the application is reloaded, there may be a loss of application state if it's not designed to persist between page navigations. For example, using URL state or local storage would persist state after a page refresh. However, component state like `useState` would be lost in such navigations.

## Streaming and Suspense

The Next.js App Router supports [streaming responses](/docs/app/api-reference/file-conventions/loading.md) when self-hosting. If you are using nginx or a similar proxy, you will need to configure it to disable buffering to enable streaming.

For example, you can disable buffering in nginx by setting `X-Accel-Buffering` to `no`:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*{/}?',
        headers: [
          {
            key: 'X-Accel-Buffering',
            value: 'no',
          },
        ],
      },
    ]
  },
}
```

## Cache Components

[Cache Components](/docs/app/getting-started/cache-components.md) works by default with Next.js and is not a CDN-only feature. This includes deployment as a Node.js server (through `next start`) and when used with a Docker container.

## Usage with CDNs

When using a CDN in front on your Next.js application, the page will include `Cache-Control: private` response header when dynamic APIs are accessed. This ensures that the resulting HTML page is marked as non-cacheable. If the page is fully prerendered to static, it will include `Cache-Control: public` to allow the page to be cached on the CDN.

If you don't need a mix of both static and dynamic components, you can make your entire route static and cache the output HTML on a CDN. This Automatic Static Optimization is the default behavior when running `next build` if dynamic APIs are not used.

As Partial Prerendering moves to stable, we will provide support through the Deployment Adapters API.

## `after`

[`after`](/docs/app/api-reference/functions/after.md) is fully supported when self-hosting with `next start`.

When stopping the server, ensure a graceful shutdown by sending `SIGINT` or `SIGTERM` signals and waiting. This allows the Next.js server to wait until after pending callback functions or promises used inside `after` have finished.


--------------------------------------------------------------------------------
title: "How to build single-page applications with Next.js"
description: "Next.js fully supports building Single-Page Applications (SPAs)."
source: "https://nextjs.org/docs/app/guides/single-page-applications"
--------------------------------------------------------------------------------

# SPAs

Next.js fully supports building Single-Page Applications (SPAs).

This includes fast route transitions with prefetching, client-side data fetching, using browser APIs, integrating with third-party client libraries, creating static routes, and more.

If you have an existing SPA, you can migrate to Next.js without large changes to your code. Next.js then allows you to progressively add server features as needed.

## What is a Single-Page Application?

The definition of a SPA varies. We’ll define a “strict SPA” as:

* **Client-side rendering (CSR)**: The app is served by one HTML file (e.g. `index.html`). Every route, page transition, and data fetch is handled by JavaScript in the browser.
* **No full-page reloads**: Rather than requesting a new document for each route, client-side JavaScript manipulates the current page’s DOM and fetches data as needed.

Strict SPAs often require large amounts of JavaScript to load before the page can be interactive. Further, client data waterfalls can be challenging to manage. Building SPAs with Next.js can address these issues.

## Why use Next.js for SPAs?

Next.js can automatically code split your JavaScript bundles, and generate multiple HTML entry points into different routes. This avoids loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.

The [`next/link`](/docs/app/api-reference/components/link.md) component automatically [prefetches](/docs/app/api-reference/components/link.md#prefetch) routes, giving you the fast page transitions of a strict SPA, but with the advantage of persisting application routing state to the URL for linking and sharing.

Next.js can start as a static site or even a strict SPA where everything is rendered client-side. If your project grows, Next.js allows you to progressively add more server features (e.g. [React Server Components](/docs/app/getting-started/server-and-client-components.md), [Server Actions](/docs/app/getting-started/updating-data.md), and more) as needed.

## Examples

Let's explore common patterns used to build SPAs and how Next.js solves them.

### Using React’s `use` within a Context Provider

We recommend fetching data in a parent component (or layout), returning the Promise, and then unwrapping the value in a Client Component with React’s [`use` hook](https://react.dev/reference/react/use).

Next.js can start data fetching early on the server. In this example, that’s the root layout — the entry point to your application. The server can immediately begin streaming a response to the client.

By “hoisting” your data fetching to the root layout, Next.js starts the specified requests on the server early before any other components in your application. This eliminates client waterfalls and prevents having multiple roundtrips between client and server. It can also significantly improve performance, as your server is closer (and ideally colocated) to where your database is located.

For example, update your root layout to call the Promise, but do *not* await it.

```tsx filename="app/layout.tsx" switcher
import { UserProvider } from './user-provider'
import { getUser } from './user' // some server-side function

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  let userPromise = getUser() // do NOT await

  return (
    <html lang="en">
      <body>
        <UserProvider userPromise={userPromise}>{children}</UserProvider>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { UserProvider } from './user-provider'
import { getUser } from './user' // some server-side function

export default function RootLayout({ children }) {
  let userPromise = getUser() // do NOT await

  return (
    <html lang="en">
      <body>
        <UserProvider userPromise={userPromise}>{children}</UserProvider>
      </body>
    </html>
  )
}
```

While you can [defer and pass a single Promise](/docs/app/getting-started/fetching-data.md#streaming-data-with-the-use-hook) as a prop to a Client Component, we generally see this pattern paired with a React context provider. This enables easier access from Client Components with a custom React Hook.

You can forward a Promise to the React context provider:

```ts filename="app/user-provider.ts" switcher
'use client';

import { createContext, useContext, ReactNode } from 'react';

type User = any;
type UserContextType = {
  userPromise: Promise<User | null>;
};

const UserContext = createContext<UserContextType | null>(null);

export function useUser(): UserContextType {
  let context = useContext(UserContext);
  if (context === null) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}

export function UserProvider({
  children,
  userPromise
}: {
  children: ReactNode;
  userPromise: Promise<User | null>;
}) {
  return (
    <UserContext.Provider value={{ userPromise }}>
      {children}
    </UserContext.Provider>
  );
}
```

```js filename="app/user-provider.js" switcher
'use client'

import { createContext, useContext, ReactNode } from 'react'

const UserContext = createContext(null)

export function useUser() {
  let context = useContext(UserContext)
  if (context === null) {
    throw new Error('useUser must be used within a UserProvider')
  }
  return context
}

export function UserProvider({ children, userPromise }) {
  return (
    <UserContext.Provider value={{ userPromise }}>
      {children}
    </UserContext.Provider>
  )
}
```

Finally, you can call the `useUser()` custom hook in any Client Component and unwrap the Promise:

```tsx filename="app/profile.tsx" switcher
'use client'

import { use } from 'react'
import { useUser } from './user-provider'

export function Profile() {
  const { userPromise } = useUser()
  const user = use(userPromise)

  return '...'
}
```

```jsx filename="app/profile.js" switcher
'use client'

import { use } from 'react'
import { useUser } from './user-provider'

export function Profile() {
  const { userPromise } = useUser()
  const user = use(userPromise)

  return '...'
}
```

The component that consumes the Promise (e.g. `Profile` above) will be suspended. This enables partial hydration. You can see the streamed and prerendered HTML before JavaScript has finished loading.

### SPAs with SWR

[SWR](https://swr.vercel.app) is a popular React library for data fetching.

With SWR 2.3.0 (and React 19+), you can gradually adopt server features alongside your existing SWR-based client data fetching code. This is an abstraction of the above `use()` pattern. This means you can move data fetching between the client and server-side, or use both:

* **Client-only:** `useSWR(key, fetcher)`
* **Server-only:** `useSWR(key)` + RSC-provided data
* **Mixed:** `useSWR(key, fetcher)` + RSC-provided data

For example, wrap your application with `<SWRConfig>` and a `fallback`:

```tsx filename="app/layout.tsx" switcher
import { SWRConfig } from 'swr'
import { getUser } from './user' // some server-side function

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <SWRConfig
      value={{
        fallback: {
          // We do NOT await getUser() here
          // Only components that read this data will suspend
          '/api/user': getUser(),
        },
      }}
    >
      {children}
    </SWRConfig>
  )
}
```

```js filename="app/layout.js" switcher
import { SWRConfig } from 'swr'
import { getUser } from './user' // some server-side function

export default function RootLayout({ children }) {
  return (
    <SWRConfig
      value={{
        fallback: {
          // We do NOT await getUser() here
          // Only components that read this data will suspend
          '/api/user': getUser(),
        },
      }}
    >
      {children}
    </SWRConfig>
  )
}
```

Because this is a Server Component, `getUser()` can securely read cookies, headers, or talk to your database. No separate API route is needed. Client components below the `<SWRConfig>` can call `useSWR()` with the same key to retrieve the user data. The component code with `useSWR` **does not require any changes** from your existing client-fetching solution.

```tsx filename="app/profile.tsx" switcher
'use client'

import useSWR from 'swr'

export function Profile() {
  const fetcher = (url) => fetch(url).then((res) => res.json())
  // The same SWR pattern you already know
  const { data, error } = useSWR('/api/user', fetcher)

  return '...'
}
```

```jsx filename="app/profile.js" switcher
'use client'

import useSWR from 'swr'

export function Profile() {
  const fetcher = (url) => fetch(url).then((res) => res.json())
  // The same SWR pattern you already know
  const { data, error } = useSWR('/api/user', fetcher)

  return '...'
}
```

The `fallback` data can be prerendered and included in the initial HTML response, then immediately read in the child components using `useSWR`. SWR’s polling, revalidation, and caching still run **client-side only**, so it preserves all the interactivity you rely on for an SPA.

Since the initial `fallback` data is automatically handled by Next.js, you can now delete any conditional logic previously needed to check if `data` was `undefined`. When the data is loading, the closest `<Suspense>` boundary will be suspended.

|                      | SWR                 | RSC                 | RSC + SWR           |
| -------------------- | ------------------- | ------------------- | ------------------- |
| SSR data             |  |  |  |
| Streaming while SSR  |  |  |  |
| Deduplicate requests |  |  |  |
| Client-side features |  |  |  |

### SPAs with React Query

You can use React Query with Next.js on both the client and server. This enables you to build both strict SPAs, as well as take advantage of server features in Next.js paired with React Query.

Learn more in the [React Query documentation](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr).

### Rendering components only in the browser

Client components are [prerendered](https://github.com/reactwg/server-components/discussions/4) during `next build`. If you want to disable prerendering for a Client Component and only load it in the browser environment, you can use [`next/dynamic`](/docs/app/guides/lazy-loading.md#nextdynamic):

```jsx
import dynamic from 'next/dynamic'

const ClientOnlyComponent = dynamic(() => import('./component'), {
  ssr: false,
})
```

This can be useful for third-party libraries that rely on browser APIs like `window` or `document`. You can also add a `useEffect` that checks for the existence of these APIs, and if they do not exist, return `null` or a loading state which would be prerendered.

### Shallow routing on the client

If you are migrating from a strict SPA like [Create React App](/docs/app/guides/migrating/from-create-react-app.md) or [Vite](/docs/app/guides/migrating/from-vite.md), you might have existing code which shallow routes to update the URL state. This can be useful for manual transitions between views in your application *without* using the default Next.js file-system routing.

Next.js allows you to use the native [`window.history.pushState`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) and [`window.history.replaceState`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) methods to update the browser's history stack without reloading the page.

`pushState` and `replaceState` calls integrate into the Next.js Router, allowing you to sync with [`usePathname`](/docs/app/api-reference/functions/use-pathname.md) and [`useSearchParams`](/docs/app/api-reference/functions/use-search-params.md).

```tsx fileName="app/ui/sort-products.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder: string) {
    const urlSearchParams = new URLSearchParams(searchParams.toString())
    urlSearchParams.set('sort', sortOrder)
    window.history.pushState(null, '', `?${urlSearchParams.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

```jsx fileName="app/ui/sort-products.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder) {
    const urlSearchParams = new URLSearchParams(searchParams.toString())
    urlSearchParams.set('sort', sortOrder)
    window.history.pushState(null, '', `?${urlSearchParams.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

Learn more about how [routing and navigation](/docs/app/getting-started/linking-and-navigating.md#how-navigation-works) work in Next.js.

### Using Server Actions in Client Components

You can progressively adopt Server Actions while still using Client Components. This allows you to remove boilerplate code to call an API route, and instead use React features like `useActionState` to handle loading and error states.

For example, create your first Server Action:

```tsx filename="app/actions.ts" switcher
'use server'

export async function create() {}
```

```js filename="app/actions.js" switcher
'use server'

export async function create() {}
```

You can import and use a Server Action from the client, similar to calling a JavaScript function. You do not need to create an API endpoint manually:

```tsx filename="app/button.tsx" switcher
'use client'

import { create } from './actions'

export function Button() {
  return <button onClick={() => create()}>Create</button>
}
```

```jsx filename="app/button.js" switcher
'use client'

import { create } from './actions'

export function Button() {
  return <button onClick={() => create()}>Create</button>
}
```

Learn more about [mutating data with Server Actions](/docs/app/getting-started/updating-data.md).

## Static export (optional)

Next.js also supports generating a fully [static site](/docs/app/guides/static-exports.md). This has some advantages over strict SPAs:

* **Automatic code-splitting**: Instead of shipping a single `index.html`, Next.js will generate an HTML file per route, so your visitors get the content faster without waiting for the client JavaScript bundle.
* **Improved user experience:** Instead of a minimal skeleton for all routes, you get fully rendered pages for each route. When users navigate client side, transitions remain instant and SPA-like.

To enable a static export, update your configuration:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'export',
}

export default nextConfig
```

After running `next build`, Next.js will create an `out` folder with the HTML/CSS/JS assets for your application.

> **Note:** Next.js server features are not supported with static exports. [Learn more](/docs/app/guides/static-exports.md#unsupported-features).

## Migrating existing projects to Next.js

You can incrementally migrate to Next.js by following our guides:

* [Migrating from Create React App](/docs/app/guides/migrating/from-create-react-app.md)
* [Migrating from Vite](/docs/app/guides/migrating/from-vite.md)

If you are already using a SPA with the Pages Router, you can learn how to [incrementally adopt the App Router](/docs/app/guides/migrating/app-router-migration.md).


--------------------------------------------------------------------------------
title: "How to create a static export of your Next.js application"
description: "Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server."
source: "https://nextjs.org/docs/app/guides/static-exports"
--------------------------------------------------------------------------------

# Static Exports

Next.js enables starting as a static site or Single-Page Application (SPA), then later optionally upgrading to use features that require a server.

When running `next build`, Next.js generates an HTML file per route. By breaking a strict SPA into individual HTML files, Next.js can avoid loading unnecessary JavaScript code on the client-side, reducing the bundle size and enabling faster page loads.

Since Next.js supports this static export, it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.

## Configuration

To enable a static export, change the output mode inside `next.config.js`:

```js filename="next.config.js" highlight={5}
/**
 * @type {import('next').NextConfig}
 */
const nextConfig = {
  output: 'export',

  // Optional: Change links `/me` -> `/me/` and emit `/me.html` -> `/me/index.html`
  // trailingSlash: true,

  // Optional: Prevent automatic `/me` -> `/me/`, instead preserve `href`
  // skipTrailingSlashRedirect: true,

  // Optional: Change the output directory `out` -> `dist`
  // distDir: 'dist',
}

module.exports = nextConfig
```

After running `next build`, Next.js will create an `out` folder with the HTML/CSS/JS assets for your application.

## Supported Features

The core of Next.js has been designed to support static exports.

### Server Components

When you run `next build` to generate a static export, Server Components consumed inside the `app` directory will run during the build, similar to traditional static-site generation.

The resulting component will be rendered into static HTML for the initial page load and a static payload for client navigation between routes. No changes are required for your Server Components when using the static export, unless they consume [dynamic server functions](#unsupported-features).

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  // This fetch will run on the server during `next build`
  const res = await fetch('https://api.example.com/...')
  const data = await res.json()

  return <main>...</main>
}
```

### Client Components

If you want to perform data fetching on the client, you can use a Client Component with [SWR](https://github.com/vercel/swr) to memoize requests.

```tsx filename="app/other/page.tsx" switcher
'use client'

import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then((r) => r.json())

export default function Page() {
  const { data, error } = useSWR(
    `https://jsonplaceholder.typicode.com/posts/1`,
    fetcher
  )
  if (error) return 'Failed to load'
  if (!data) return 'Loading...'

  return data.title
}
```

```jsx filename="app/other/page.js" switcher
'use client'

import useSWR from 'swr'

const fetcher = (url) => fetch(url).then((r) => r.json())

export default function Page() {
  const { data, error } = useSWR(
    `https://jsonplaceholder.typicode.com/posts/1`,
    fetcher
  )
  if (error) return 'Failed to load'
  if (!data) return 'Loading...'

  return data.title
}
```

Since route transitions happen client-side, this behaves like a traditional SPA. For example, the following index route allows you to navigate to different posts on the client:

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <>
      <h1>Index Page</h1>
      <hr />
      <ul>
        <li>
          <Link href="/post/1">Post 1</Link>
        </li>
        <li>
          <Link href="/post/2">Post 2</Link>
        </li>
      </ul>
    </>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <>
      <h1>Index Page</h1>
      <p>
        <Link href="/other">Other Page</Link>
      </p>
    </>
  )
}
```

### Image Optimization

[Image Optimization](/docs/app/api-reference/components/image.md) through `next/image` can be used with a static export by defining a custom image loader in `next.config.js`. For example, you can optimize images with a service like Cloudinary:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  images: {
    loader: 'custom',
    loaderFile: './my-loader.ts',
  },
}

module.exports = nextConfig
```

This custom loader will define how to fetch images from a remote source. For example, the following loader will construct the URL for Cloudinary:

```ts filename="my-loader.ts" switcher
export default function cloudinaryLoader({
  src,
  width,
  quality,
}: {
  src: string
  width: number
  quality?: number
}) {
  const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
  return `https://res.cloudinary.com/demo/image/upload/${params.join(
    ','
  )}${src}`
}
```

```js filename="my-loader.js" switcher
export default function cloudinaryLoader({ src, width, quality }) {
  const params = ['f_auto', 'c_limit', `w_${width}`, `q_${quality || 'auto'}`]
  return `https://res.cloudinary.com/demo/image/upload/${params.join(
    ','
  )}${src}`
}
```

You can then use `next/image` in your application, defining relative paths to the image in Cloudinary:

```tsx filename="app/page.tsx" switcher
import Image from 'next/image'

export default function Page() {
  return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
}
```

```jsx filename="app/page.js" switcher
import Image from 'next/image'

export default function Page() {
  return <Image alt="turtles" src="/turtles.jpg" width={300} height={300} />
}
```

### Route Handlers

Route Handlers will render a static response when running `next build`. Only the `GET` HTTP verb is supported. This can be used to generate static HTML, JSON, TXT, or other files from cached or uncached data. For example:

```ts filename="app/data.json/route.ts" switcher
export async function GET() {
  return Response.json({ name: 'Lee' })
}
```

```js filename="app/data.json/route.js" switcher
export async function GET() {
  return Response.json({ name: 'Lee' })
}
```

The above file `app/data.json/route.ts` will render to a static file during `next build`, producing `data.json` containing `{ name: 'Lee' }`.

If you need to read dynamic values from the incoming request, you cannot use a static export.

### Browser APIs

Client Components are pre-rendered to HTML during `next build`. Because [Web APIs](https://developer.mozilla.org/docs/Web/API) like `window`, `localStorage`, and `navigator` are not available on the server, you need to safely access these APIs only when running in the browser. For example:

```jsx
'use client';

import { useEffect } from 'react';

export default function ClientComponent() {
  useEffect(() => {
    // You now have access to `window`
    console.log(window.innerHeight);
  }, [])

  return ...;
}
```

## Unsupported Features

Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are **not** supported:

* [Dynamic Routes](/docs/app/api-reference/file-conventions/dynamic-routes.md) with `dynamicParams: true`
* [Dynamic Routes](/docs/app/api-reference/file-conventions/dynamic-routes.md) without `generateStaticParams()`
* [Route Handlers](/docs/app/api-reference/file-conventions/route.md) that rely on Request
* [Cookies](/docs/app/api-reference/functions/cookies.md)
* [Rewrites](/docs/app/api-reference/config/next-config-js/rewrites.md)
* [Redirects](/docs/app/api-reference/config/next-config-js/redirects.md)
* [Headers](/docs/app/api-reference/config/next-config-js/headers.md)
* [Proxy](/docs/app/api-reference/file-conventions/proxy.md)
* [Incremental Static Regeneration](/docs/app/guides/incremental-static-regeneration.md)
* [Image Optimization](/docs/app/api-reference/components/image.md) with the default `loader`
* [Draft Mode](/docs/app/guides/draft-mode.md)
* [Server Actions](/docs/app/getting-started/updating-data.md)
* [Intercepting Routes](/docs/app/api-reference/file-conventions/intercepting-routes.md)

Attempting to use any of these features with `next dev` will result in an error, similar to setting the [`dynamic`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamic) option to `error` in the root layout.

```jsx
export const dynamic = 'error'
```

## Deploying

With a static export, Next.js can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets.

When running `next build`, Next.js generates the static export into the `out` folder. For example, let's say you have the following routes:

* `/`
* `/blog/[id]`

After running `next build`, Next.js will generate the following files:

* `/out/index.html`
* `/out/404.html`
* `/out/blog/post-1.html`
* `/out/blog/post-2.html`

If you are using a static host like Nginx, you can configure rewrites from incoming requests to the correct files:

```nginx filename="nginx.conf"
server {
  listen 80;
  server_name acme.com;

  root /var/www/out;

  location / {
      try_files $uri $uri.html $uri/ =404;
  }

  # This is necessary when `trailingSlash: false`.
  # You can omit this when `trailingSlash: true`.
  location /blog/ {
      rewrite ^/blog/(.*)$ /blog/$1.html break;
  }

  error_page 404 /404.html;
  location = /404.html {
      internal;
  }
}
```

## Version History

| Version   | Changes                                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------------------- |
| `v14.0.0` | `next export` has been removed in favor of `"output": "export"`                                                      |
| `v13.4.0` | App Router (Stable) adds enhanced static export support, including using React Server Components and Route Handlers. |
| `v13.3.0` | `next export` is deprecated and replaced with `"output": "export"`                                                   |


--------------------------------------------------------------------------------
title: "How to install Tailwind CSS v3 in your Next.js application"
description: "Style your Next.js Application using Tailwind CSS v3 for broader browser support."
source: "https://nextjs.org/docs/app/guides/tailwind-v3-css"
--------------------------------------------------------------------------------

# Tailwind CSS v3

This guide will walk you through how to install [Tailwind CSS v3](https://v3.tailwindcss.com/) in your Next.js application.

> **Good to know:** For the latest Tailwind 4 setup, see the [Tailwind CSS setup instructions](/docs/app/getting-started/css.md#tailwind-css).

## Installing Tailwind v3

Install Tailwind CSS and its peer dependencies, then run the `init` command to generate both `tailwind.config.js` and `postcss.config.js` files:

```bash package="pnpm"
pnpm add -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p
```

```bash package="npm"
npm install -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p
```

```bash package="yarn"
yarn add -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p
```

```bash package="bun"
bun add -D tailwindcss@^3 postcss autoprefixer
bunx tailwindcss init -p
```

## Configuring Tailwind v3

Configure your template paths in your `tailwind.config.js` file:

```js filename="tailwind.config.js"
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Add the Tailwind directives to your global CSS file:

```css filename="app/globals.css"
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Import the CSS file in your root layout:

```tsx filename="app/layout.tsx" switcher
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import './globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

## Using classes

After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.

```tsx filename="app/page.tsx" switcher
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

```jsx filename="app/page.js" switcher
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

## Usage with Turbopack

As of Next.js 13.1, Tailwind CSS and PostCSS are supported with [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css).


--------------------------------------------------------------------------------
title: "Testing"
description: "Learn how to set up Next.js with four commonly used testing tools — Cypress, Playwright, Vitest, and Jest."
source: "https://nextjs.org/docs/app/guides/testing"
--------------------------------------------------------------------------------

# Testing

In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview of types and commonly used tools you can use to test your application.

## Types of tests

* **Unit Testing** involves testing individual units (or blocks of code) in isolation. In React, a unit can be a single function, hook, or component.
  * **Component Testing** is a more focused version of unit testing where the primary subject of the tests is React components. This may involve testing how components are rendered, their interaction with props, and their behavior in response to user events.
  * **Integration Testing** involves testing how multiple units work together. This can be a combination of components, hooks, and functions.
* **End-to-End (E2E) Testing** involves testing user flows in an environment that simulates real user scenarios, like the browser. This means testing specific tasks (e.g. signup flow) in a production-like environment.
* **Snapshot Testing** involves capturing the rendered output of a component and saving it to a snapshot file. When tests run, the current rendered output of the component is compared against the saved snapshot. Changes in the snapshot are used to indicate unexpected changes in behavior.

## Async Server Components

Since `async` Server Components are new to the React ecosystem, some tools do not fully support them. In the meantime, we recommend using **End-to-End Testing** over **Unit Testing** for `async` components.

## Guides

See the guides below to learn how to set up Next.js with these commonly used testing tools:

 - [Cypress](/docs/app/guides/testing/cypress.md)
 - [Jest](/docs/app/guides/testing/jest.md)
 - [Playwright](/docs/app/guides/testing/playwright.md)
 - [Vitest](/docs/app/guides/testing/vitest.md)

--------------------------------------------------------------------------------
title: "How to set up Cypress with Next.js"
description: "Learn how to set up Cypress with Next.js for End-to-End (E2E) and Component Testing."
source: "https://nextjs.org/docs/app/guides/testing/cypress"
--------------------------------------------------------------------------------

# Cypress

[Cypress](https://www.cypress.io/) is a test runner used for **End-to-End (E2E)** and **Component Testing**. This page will show you how to set up Cypress with Next.js and write your first tests.

> **Warning:**
>
> * Cypress versions below 13.6.3 do not support [TypeScript version 5](https://github.com/cypress-io/cypress/issues/27731) with `moduleResolution:"bundler"`. However, this issue has been resolved in Cypress version 13.6.3 and later. [cypress v13.6.3](https://docs.cypress.io/guides/references/changelog#13-6-3)

## Quickstart

You can use `create-next-app` with the [with-cypress example](https://github.com/vercel/next.js/tree/canary/examples/with-cypress) to quickly get started.

```bash filename="Terminal"
npx create-next-app@latest --example with-cypress with-cypress-app
```

## Manual setup

To manually set up Cypress, install `cypress` as a dev dependency:

```bash filename="Terminal"
npm install -D cypress
# or
yarn add -D cypress
# or
pnpm install -D cypress
```

Add the Cypress `open` command to the `package.json` scripts field:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "cypress:open": "cypress open"
  }
}
```

Run Cypress for the first time to open the Cypress testing suite:

```bash filename="Terminal"
npm run cypress:open
```

You can choose to configure **E2E Testing** and/or **Component Testing**. Selecting any of these options will automatically create a `cypress.config.js` file and a `cypress` folder in your project.

## Creating your first Cypress E2E test

Ensure your `cypress.config` file has the following configuration:

```ts filename="cypress.config.ts" switcher
import { defineConfig } from 'cypress'

export default defineConfig({
  e2e: {
    setupNodeEvents(on, config) {},
  },
})
```

```js filename="cypress.config.js" switcher
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {},
  },
})
```

Then, create two new Next.js files:

```jsx filename="app/page.js"
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```jsx filename="app/about/page.js"
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>About</h1>
      <Link href="/">Home</Link>
    </div>
  )
}
```

Add a test to check your navigation is working correctly:

```js filename="cypress/e2e/app.cy.js"
describe('Navigation', () => {
  it('should navigate to the about page', () => {
    // Start from the index page
    cy.visit('http://localhost:3000/')

    // Find a link with an href attribute containing "about" and click it
    cy.get('a[href*="about"]').click()

    // The new url should include "/about"
    cy.url().should('include', '/about')

    // The new page should contain an h1 with "About"
    cy.get('h1').contains('About')
  })
})
```

### Running E2E Tests

Cypress will simulate a user navigating your application, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.

Run `npm run build && npm run start` to build your Next.js application, then run `npm run cypress:open` in another terminal window to start Cypress and run your E2E Testing suite.

> **Good to know:**
>
> * You can use `cy.visit("/")` instead of `cy.visit("http://localhost:3000/")` by adding `baseUrl: 'http://localhost:3000'` to the `cypress.config.js` configuration file.
> * Alternatively, you can install the [`start-server-and-test`](https://www.npmjs.com/package/start-server-and-test) package to run the Next.js production server in conjunction with Cypress. After installation, add `"test": "start-server-and-test start http://localhost:3000 cypress"` to your `package.json` scripts field. Remember to rebuild your application after new changes.

## Creating your first Cypress component test

Component tests build and mount a specific component without having to bundle your whole application or start a server.

Select **Component Testing** in the Cypress app, then select **Next.js** as your front-end framework. A `cypress/component` folder will be created in your project, and a `cypress.config.js` file will be updated to enable Component Testing.

Ensure your `cypress.config` file has the following configuration:

```ts filename="cypress.config.ts" switcher
import { defineConfig } from 'cypress'

export default defineConfig({
  component: {
    devServer: {
      framework: 'next',
      bundler: 'webpack',
    },
  },
})
```

```js filename="cypress.config.js" switcher
const { defineConfig } = require('cypress')

module.exports = defineConfig({
  component: {
    devServer: {
      framework: 'next',
      bundler: 'webpack',
    },
  },
})
```

Assuming the same components from the previous section, add a test to validate a component is rendering the expected output:

```tsx filename="cypress/component/about.cy.tsx"
import Page from '../../app/page'

describe('<Page />', () => {
  it('should render and display expected content', () => {
    // Mount the React component for the Home page
    cy.mount(<Page />)

    // The new page should contain an h1 with "Home"
    cy.get('h1').contains('Home')

    // Validate that a link with the expected URL is present
    // Following the link is better suited to an E2E test
    cy.get('a[href="/about"]').should('be.visible')
  })
})
```

> **Good to know**:
>
> * Cypress currently doesn't support Component Testing for `async` Server Components. We recommend using E2E testing.
> * Since component tests do not require a Next.js server, features like `<Image />` that rely on a server being available may not function out-of-the-box.

### Running Component Tests

Run `npm run cypress:open` in your terminal to start Cypress and run your Component Testing suite.

## Continuous Integration (CI)

In addition to interactive testing, you can also run Cypress headlessly using the `cypress run` command, which is better suited for CI environments:

```json filename="package.json"
{
  "scripts": {
    //...
    "e2e": "start-server-and-test dev http://localhost:3000 \"cypress open --e2e\"",
    "e2e:headless": "start-server-and-test dev http://localhost:3000 \"cypress run --e2e\"",
    "component": "cypress open --component",
    "component:headless": "cypress run --component"
  }
}
```

You can learn more about Cypress and Continuous Integration from these resources:

* [Next.js with Cypress example](https://github.com/vercel/next.js/tree/canary/examples/with-cypress)
* [Cypress Continuous Integration Docs](https://docs.cypress.io/guides/continuous-integration/introduction)
* [Cypress GitHub Actions Guide](https://on.cypress.io/github-actions)
* [Official Cypress GitHub Action](https://github.com/cypress-io/github-action)
* [Cypress Discord](https://discord.com/invite/cypress)


--------------------------------------------------------------------------------
title: "How to set up Jest with Next.js"
description: "Learn how to set up Jest with Next.js for Unit Testing and Snapshot Testing."
source: "https://nextjs.org/docs/app/guides/testing/jest"
--------------------------------------------------------------------------------

# Jest

Jest and React Testing Library are frequently used together for **Unit Testing** and **Snapshot Testing**. This guide will show you how to set up Jest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Jest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using an **E2E tests** for `async` components.

## Quickstart

You can use `create-next-app` with the Next.js [with-jest](https://github.com/vercel/next.js/tree/canary/examples/with-jest) example to quickly get started:

```bash filename="Terminal"
npx create-next-app@latest --example with-jest with-jest-app
```

## Manual setup

Since the release of [Next.js 12](https://nextjs.org/blog/next-12), Next.js now has built-in configuration for Jest.

To set up Jest, install `jest` and the following packages as dev dependencies:

```bash filename="Terminal"
npm install -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
# or
yarn add -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
# or
pnpm install -D jest jest-environment-jsdom @testing-library/react @testing-library/dom @testing-library/jest-dom ts-node @types/jest
```

Generate a basic Jest configuration file by running the following command:

```bash filename="Terminal"
npm init jest@latest
# or
yarn create jest@latest
# or
pnpm create jest@latest
```

This will take you through a series of prompts to setup Jest for your project, including automatically creating a `jest.config.ts|js` file.

Update your config file to use `next/jest`. This transformer has all the necessary configuration options for Jest to work with Next.js:

```ts filename="jest.config.ts" switcher
import type { Config } from 'jest'
import nextJest from 'next/jest.js'

const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})

// Add any custom config to be passed to Jest
const config: Config = {
  coverageProvider: 'v8',
  testEnvironment: 'jsdom',
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
export default createJestConfig(config)
```

```js filename="jest.config.js" switcher
const nextJest = require('next/jest')

/** @type {import('jest').Config} */
const createJestConfig = nextJest({
  // Provide the path to your Next.js app to load next.config.js and .env files in your test environment
  dir: './',
})

// Add any custom config to be passed to Jest
const config = {
  coverageProvider: 'v8',
  testEnvironment: 'jsdom',
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.ts'],
}

// createJestConfig is exported this way to ensure that next/jest can load the Next.js config which is async
module.exports = createJestConfig(config)
```

Under the hood, `next/jest` is automatically configuring Jest for you, including:

* Setting up `transform` using the [Next.js Compiler](/docs/architecture/nextjs-compiler.md).
* Auto mocking stylesheets (`.css`, `.module.css`, and their scss variants), image imports and [`next/font`](/docs/app/api-reference/components/font.md).
* Loading `.env` (and all variants) into `process.env`.
* Ignoring `node_modules` from test resolving and transforms.
* Ignoring `.next` from test resolving.
* Loading `next.config.js` for flags that enable SWC transforms.

> **Good to know**: To test environment variables directly, load them manually in a separate setup script or in your `jest.config.ts` file. For more information, please see [Test Environment Variables](/docs/app/guides/environment-variables.md#test-environment-variables).

## Optional: Handling Absolute Imports and Module Path Aliases

If your project is using [Module Path Aliases](/docs/app/getting-started/installation.md#set-up-absolute-imports-and-module-path-aliases), you will need to configure Jest to resolve the imports by matching the paths option in the `jsconfig.json` file with the `moduleNameMapper` option in the `jest.config.js` file. For example:

```json filename="tsconfig.json or jsconfig.json"
{
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler",
    "baseUrl": "./",
    "paths": {
      "@/components/*": ["components/*"]
    }
  }
}
```

```js filename="jest.config.js"
moduleNameMapper: {
  // ...
  '^@/components/(.*)$': '<rootDir>/components/$1',
}
```

## Optional: Extend Jest with custom matchers

`@testing-library/jest-dom` includes a set of convenient [custom matchers](https://github.com/testing-library/jest-dom#custom-matchers) such as `.toBeInTheDocument()` making it easier to write tests. You can import the custom matchers for every test by adding the following option to the Jest configuration file:

```ts filename="jest.config.ts" switcher
setupFilesAfterEnv: ['<rootDir>/jest.setup.ts']
```

```js filename="jest.config.js" switcher
setupFilesAfterEnv: ['<rootDir>/jest.setup.js']
```

Then, inside `jest.setup`, add the following import:

```ts filename="jest.setup.ts" switcher
import '@testing-library/jest-dom'
```

```js filename="jest.setup.js" switcher
import '@testing-library/jest-dom'
```

> **Good to know:** [`extend-expect` was removed in `v6.0`](https://github.com/testing-library/jest-dom/releases/tag/v6.0.0), so if you are using `@testing-library/jest-dom` before version 6, you will need to import `@testing-library/jest-dom/extend-expect` instead.

If you need to add more setup options before each test, you can add them to the `jest.setup` file above.

## Add a test script to `package.json`

Finally, add a Jest `test` script to your `package.json` file:

```json filename="package.json" highlight={6-7}
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test": "jest",
    "test:watch": "jest --watch"
  }
}
```

`jest --watch` will re-run tests when a file is changed. For more Jest CLI options, please refer to the [Jest Docs](https://jestjs.io/docs/cli#reference).

### Creating your first test

Your project is now ready to run tests. Create a folder called `__tests__` in your project's root directory.

For example, we can add a test to check if the `<Page />` component successfully renders a heading:

```jsx filename="app/page.js"
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```jsx filename="__tests__/page.test.jsx"
import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'

describe('Page', () => {
  it('renders a heading', () => {
    render(<Page />)

    const heading = screen.getByRole('heading', { level: 1 })

    expect(heading).toBeInTheDocument()
  })
})
```

Optionally, add a [snapshot test](https://jestjs.io/docs/snapshot-testing) to keep track of any unexpected changes in your component:

```jsx filename="__tests__/snapshot.js"
import { render } from '@testing-library/react'
import Page from '../app/page'

it('renders homepage unchanged', () => {
  const { container } = render(<Page />)
  expect(container).toMatchSnapshot()
})
```

## Running your tests

Then, run the following command to run your tests:

```bash filename="Terminal"
npm run test
# or
yarn test
# or
pnpm test
```

## Additional Resources

For further reading, you may find these resources helpful:

* [Next.js with Jest example](https://github.com/vercel/next.js/tree/canary/examples/with-jest)
* [Jest Docs](https://jestjs.io/docs/getting-started)
* [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)
* [Testing Playground](https://testing-playground.com/) - use good testing practices to match elements.


--------------------------------------------------------------------------------
title: "How to set up Playwright with Next.js"
description: "Learn how to set up Playwright with Next.js for End-to-End (E2E) Testing."
source: "https://nextjs.org/docs/app/guides/testing/playwright"
--------------------------------------------------------------------------------

# Playwright

Playwright is a testing framework that lets you automate Chromium, Firefox, and WebKit with a single API. You can use it to write **End-to-End (E2E)** testing. This guide will show you how to set up Playwright with Next.js and write your first tests.

## Quickstart

The fastest way to get started is to use `create-next-app` with the [with-playwright example](https://github.com/vercel/next.js/tree/canary/examples/with-playwright). This will create a Next.js project complete with Playwright configured.

```bash filename="Terminal"
npx create-next-app@latest --example with-playwright with-playwright-app
```

## Manual setup

To install Playwright, run the following command:

```bash filename="Terminal"
npm init playwright
# or
yarn create playwright
# or
pnpm create playwright
```

This will take you through a series of prompts to setup and configure Playwright for your project, including adding a `playwright.config.ts` file. Please refer to the [Playwright installation guide](https://playwright.dev/docs/intro#installation) for the step-by-step guide.

## Creating your first Playwright E2E test

Create two new Next.js pages:

```tsx filename="app/page.tsx"
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```tsx filename="app/about/page.tsx"
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>About</h1>
      <Link href="/">Home</Link>
    </div>
  )
}
```

Then, add a test to verify that your navigation is working correctly:

```ts filename="tests/example.spec.ts"
import { test, expect } from '@playwright/test'

test('should navigate to the about page', async ({ page }) => {
  // Start from the index page (the baseURL is set via the webServer in the playwright.config.ts)
  await page.goto('http://localhost:3000/')
  // Find an element with the text 'About' and click on it
  await page.click('text=About')
  // The new URL should be "/about" (baseURL is used there)
  await expect(page).toHaveURL('http://localhost:3000/about')
  // The new page should contain an h1 with "About"
  await expect(page.locator('h1')).toContainText('About')
})
```

> **Good to know**: You can use `page.goto("/")` instead of `page.goto("http://localhost:3000/")`, if you add [`"baseURL": "http://localhost:3000"`](https://playwright.dev/docs/api/class-testoptions#test-options-base-url) to the `playwright.config.ts` [configuration file](https://playwright.dev/docs/test-configuration).

### Running your Playwright tests

Playwright will simulate a user navigating your application using three browsers: Chromium, Firefox and Webkit, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.

Run `npm run build` and `npm run start`, then run `npx playwright test` in another terminal window to run the Playwright tests.

> **Good to know**: Alternatively, you can use the [`webServer`](https://playwright.dev/docs/test-webserver/) feature to let Playwright start the development server and wait until it's fully available.

### Running Playwright on Continuous Integration (CI)

Playwright will by default run your tests in the [headless mode](https://playwright.dev/docs/ci#running-headed). To install all the Playwright dependencies, run `npx playwright install-deps`.

You can learn more about Playwright and Continuous Integration from these resources:

* [Next.js with Playwright example](https://github.com/vercel/next.js/tree/canary/examples/with-playwright)
* [Playwright on your CI provider](https://playwright.dev/docs/ci)
* [Playwright Discord](https://discord.com/invite/playwright-807756831384403968)


--------------------------------------------------------------------------------
title: "How to set up Vitest with Next.js"
description: "Learn how to set up Vitest with Next.js for Unit Testing."
source: "https://nextjs.org/docs/app/guides/testing/vitest"
--------------------------------------------------------------------------------

# Vitest

Vitest and React Testing Library are frequently used together for **Unit Testing**. This guide will show you how to setup Vitest with Next.js and write your first tests.

> **Good to know:** Since `async` Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using **E2E tests** for `async` components.

## Quickstart

You can use `create-next-app` with the Next.js [with-vitest](https://github.com/vercel/next.js/tree/canary/examples/with-vitest) example to quickly get started:

```bash filename="Terminal"
npx create-next-app@latest --example with-vitest with-vitest-app
```

## Manual Setup

To manually set up Vitest, install `vitest` and the following packages as dev dependencies:

```bash filename="Terminal"
# Using TypeScript
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom vite-tsconfig-paths
# Using JavaScript
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react @testing-library/dom
```

Create a `vitest.config.mts|js` file in the root of your project, and add the following options:

```ts filename="vitest.config.mts" switcher
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: {
    environment: 'jsdom',
  },
})
```

```js filename="vitest.config.js" switcher
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
  },
})
```

For more information on configuring Vitest, please refer to the [Vitest Configuration](https://vitest.dev/config/#configuration) docs.

Then, add a `test` script to your `package.json`:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "test": "vitest"
  }
}
```

When you run `npm run test`, Vitest will **watch** for changes in your project by default.

## Creating your first Vitest Unit Test

Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```jsx filename="app/page.jsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```tsx filename="__tests__/page.test.tsx" switcher
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```

```jsx filename="__tests__/page.test.jsx" switcher
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../app/page'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```

> **Good to know**: The example above uses the common `__tests__` convention, but test files can also be colocated inside the `app` router.

## Running your tests

Then, run the following command to run your tests:

```bash filename="Terminal"
npm run test
# or
yarn test
# or
pnpm test
# or
bun test
```

## Additional Resources

You may find these resources helpful:

* [Next.js with Vitest example](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
* [Vitest Docs](https://vitest.dev/guide/)
* [React Testing Library Docs](https://testing-library.com/docs/react-testing-library/intro/)


--------------------------------------------------------------------------------
title: "How to optimize third-party libraries"
description: "Optimize the performance of third-party libraries in your application with the `@next/third-parties` package."
source: "https://nextjs.org/docs/app/guides/third-party-libraries"
--------------------------------------------------------------------------------

# Third Party Libraries

**`@next/third-parties`** is a library that provides a collection of components and utilities that improve the performance and developer experience of loading popular third-party libraries in your Next.js application.

All third-party integrations provided by `@next/third-parties` have been optimized for performance and ease of use.

## Getting Started

To get started, install the `@next/third-parties` library:

```bash filename="Terminal"
npm install @next/third-parties@latest next@latest
```

`@next/third-parties` is currently an **experimental** library under active development. We recommend installing it with the **latest** or **canary** flags while we work on adding more third-party integrations.

## Google Third-Parties

All supported third-party libraries from Google can be imported from `@next/third-parties/google`.

### Google Tag Manager

The `GoogleTagManager` component can be used to instantiate a [Google Tag Manager](https://developers.google.com/tag-platform/tag-manager) container to your page. By default, it fetches the original inline script after hydration occurs on the page.

To load Google Tag Manager for all routes, include the component directly in your root layout and pass in your GTM container ID:

```tsx filename="app/layout.tsx" switcher
import { GoogleTagManager } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { GoogleTagManager } from '@next/third-parties/google'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <GoogleTagManager gtmId="GTM-XYZ" />
      <body>{children}</body>
    </html>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:

```jsx filename="app/page.js"
import { GoogleTagManager } from '@next/third-parties/google'

export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

#### Sending Events

The `sendGTMEvent` function can be used to track user interactions on your page by sending events
using the `dataLayer` object. For this function to work, the `<GoogleTagManager />` component must be
included in either a parent layout, page, or component, or directly in the same file.

```jsx filename="app/page.js"
'use client'

import { sendGTMEvent } from '@next/third-parties/google'

export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGTMEvent({ event: 'buttonClicked', value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Tag Manager [developer
documentation](https://developers.google.com/tag-platform/tag-manager/datalayer) to learn about the
different variables and events that can be passed into the function.

#### Server-side Tagging

If you're using a server-side tag manager and serving `gtm.js` scripts from your tagging server you can
use `gtmScriptUrl` option to specify the URL of the script.

#### Options

Options to pass to the Google Tag Manager. For a full list of options, read the [Google Tag Manager
docs](https://developers.google.com/tag-platform/tag-manager/datalayer).

| Name            | Type       | Description                                                              |
| --------------- | ---------- | ------------------------------------------------------------------------ |
| `gtmId`         | Required\* | Your GTM container ID. Usually starts with `GTM-`.                       |
| `gtmScriptUrl`  | Optional\* | GTM script URL. Defaults to `https://www.googletagmanager.com/gtm.js`.   |
| `dataLayer`     | Optional   | Data layer object to instantiate the container with.                     |
| `dataLayerName` | Optional   | Name of the data layer. Defaults to `dataLayer`.                         |
| `auth`          | Optional   | Value of authentication parameter (`gtm_auth`) for environment snippets. |
| `preview`       | Optional   | Value of preview parameter (`gtm_preview`) for environment snippets.     |

\*`gtmId` can be omitted when `gtmScriptUrl` is provided to support [Google tag gateway for advertisers](https://developers.google.com/tag-platform/tag-manager/gateway/setup-guide?setup=manual).

### Google Analytics

The `GoogleAnalytics` component can be used to include [Google Analytics
4](https://developers.google.com/analytics/devguides/collection/ga4) to your page via the Google tag
(`gtag.js`). By default, it fetches the original scripts after hydration occurs on the page.

> **Recommendation**: If Google Tag Manager is already included in your application, you can
> configure Google Analytics directly using it, rather than including Google Analytics as a separate
> component. Refer to the
> [documentation](https://developers.google.com/analytics/devguides/collection/ga4/tag-options#what-is-gtm)
> to learn more about the differences between Tag Manager and `gtag.js`.

To load Google Analytics for all routes, include the component directly in your root layout and pass
in your measurement ID:

```tsx filename="app/layout.tsx" switcher
import { GoogleAnalytics } from '@next/third-parties/google'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { GoogleAnalytics } from '@next/third-parties/google'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
      <GoogleAnalytics gaId="G-XYZ" />
    </html>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:

```jsx filename="app/page.js"
import { GoogleAnalytics } from '@next/third-parties/google'

export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

#### Sending Events

The `sendGAEvent` function can be used to measure user interactions on your page by sending events
using the `dataLayer` object. For this function to work, the `<GoogleAnalytics />` component must be
included in either a parent layout, page, or component, or directly in the same file.

```jsx filename="app/page.js"
'use client'

import { sendGAEvent } from '@next/third-parties/google'

export function EventButton() {
  return (
    <div>
      <button
        onClick={() => sendGAEvent('event', 'buttonClicked', { value: 'xyz' })}
      >
        Send Event
      </button>
    </div>
  )
}
```

Refer to the Google Analytics [developer
documentation](https://developers.google.com/analytics/devguides/collection/ga4/event-parameters) to learn
more about event parameters.

#### Tracking Pageviews

Google Analytics automatically tracks pageviews when the browser history state changes. This means
that client-side navigations between Next.js routes will send pageview data without any configuration.

To ensure that client-side navigations are being measured correctly, verify that the [*“Enhanced
Measurement”*](https://support.google.com/analytics/answer/9216061#enable_disable) property is
enabled in your Admin panel and the *“Page changes based on browser history events”* checkbox is
selected.

> **Note**: If you decide to manually send pageview events, make sure to disable the default
> pageview measurement to avoid having duplicate data. Refer to the Google Analytics [developer
> documentation](https://developers.google.com/analytics/devguides/collection/ga4/views?client_type=gtag#manual_pageviews)
> to learn more.

#### Options

Options to pass to the `<GoogleAnalytics>` component.

| Name            | Type     | Description                                                                                            |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------ |
| `gaId`          | Required | Your [measurement ID](https://support.google.com/analytics/answer/12270356). Usually starts with `G-`. |
| `dataLayerName` | Optional | Name of the data layer. Defaults to `dataLayer`.                                                       |
| `nonce`         | Optional | A [nonce](/docs/app/guides/content-security-policy.md#nonces).                                            |

### Google Maps Embed

The `GoogleMapsEmbed` component can be used to add a [Google Maps
Embed](https://developers.google.com/maps/documentation/embed/embedding-map) to your page. By
default, it uses the `loading` attribute to lazy-load the embed below the fold.

```jsx filename="app/page.js"
import { GoogleMapsEmbed } from '@next/third-parties/google'

export default function Page() {
  return (
    <GoogleMapsEmbed
      apiKey="XYZ"
      height={200}
      width="100%"
      mode="place"
      q="Brooklyn+Bridge,New+York,NY"
    />
  )
}
```

#### Options

Options to pass to the Google Maps Embed. For a full list of options, read the [Google Map Embed
docs](https://developers.google.com/maps/documentation/embed/embedding-map).

| Name              | Type     | Description                                                                                         |
| ----------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `apiKey`          | Required | Your api key.                                                                                       |
| `mode`            | Required | [Map mode](https://developers.google.com/maps/documentation/embed/embedding-map#choosing_map_modes) |
| `height`          | Optional | Height of the embed. Defaults to `auto`.                                                            |
| `width`           | Optional | Width of the embed. Defaults to `auto`.                                                             |
| `style`           | Optional | Pass styles to the iframe.                                                                          |
| `allowfullscreen` | Optional | Property to allow certain map parts to go full screen.                                              |
| `loading`         | Optional | Defaults to lazy. Consider changing if you know your embed will be above the fold.                  |
| `q`               | Optional | Defines map marker location. *This may be required depending on the map mode*.                      |
| `center`          | Optional | Defines the center of the map view.                                                                 |
| `zoom`            | Optional | Sets initial zoom level of the map.                                                                 |
| `maptype`         | Optional | Defines type of map tiles to load.                                                                  |
| `language`        | Optional | Defines the language to use for UI elements and for the display of labels on map tiles.             |
| `region`          | Optional | Defines the appropriate borders and labels to display, based on geo-political sensitivities.        |

### YouTube Embed

The `YouTubeEmbed` component can be used to load and display a YouTube embed. This component loads
faster by using [`lite-youtube-embed`](https://github.com/paulirish/lite-youtube-embed) under the
hood.

```jsx filename="app/page.js"
import { YouTubeEmbed } from '@next/third-parties/google'

export default function Page() {
  return <YouTubeEmbed videoid="ogfYd705cRs" height={400} params="controls=0" />
}
```

#### Options

| Name        | Type     | Description                                                                                                                                                                                                  |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `videoid`   | Required | YouTube video id.                                                                                                                                                                                            |
| `width`     | Optional | Width of the video container. Defaults to `auto`                                                                                                                                                             |
| `height`    | Optional | Height of the video container. Defaults to `auto`                                                                                                                                                            |
| `playlabel` | Optional | A visually hidden label for the play button for accessibility.                                                                                                                                               |
| `params`    | Optional | The video player params defined [here](https://developers.google.com/youtube/player_parameters#Parameters).  Params are passed as a query param string.  Eg: `params="controls=0&start=10&end=30"` |
| `style`     | Optional | Used to apply styles to the video container.                                                                                                                                                                 |


--------------------------------------------------------------------------------
title: "Upgrade Guides"
description: "Learn how to upgrade to the latest versions of Next.js."
source: "https://nextjs.org/docs/app/guides/upgrading"
--------------------------------------------------------------------------------

# Upgrading

Learn how to upgrade to the latest versions of Next.js following the versions-specific guides:

 - [Codemods](/docs/app/guides/upgrading/codemods.md)
 - [Version 14](/docs/app/guides/upgrading/version-14.md)
 - [Version 15](/docs/app/guides/upgrading/version-15.md)
 - [Version 16](/docs/app/guides/upgrading/version-16.md)

--------------------------------------------------------------------------------
title: "Codemods"
description: "Use codemods to upgrade your Next.js codebase when new features are released."
source: "https://nextjs.org/docs/app/guides/upgrading/codemods"
--------------------------------------------------------------------------------

# Codemods

Codemods are transformations that run on your codebase programmatically. This allows a large number of changes to be programmatically applied without having to manually go through every file.

Next.js provides Codemod transformations to help upgrade your Next.js codebase when an API is updated or deprecated.

## Usage

In your terminal, navigate (`cd`) into your project's folder, then run:

```bash filename="Terminal"
npx @next/codemod <transform> <path>
```

Replacing `<transform>` and `<path>` with appropriate values.

* `transform` - name of transform
* `path` - files or directory to transform
* `--dry` Do a dry-run, no code will be edited
* `--print` Prints the changed output for comparison

## Codemods

### 16.0

#### Remove `experimental_ppr` Route Segment Config from App Router pages and layouts

##### `remove-experimental-ppr`

```bash filename="Terminal"
npx @next/codemod@latest remove-experimental-ppr .
```

This codemod removes the `experimental_ppr` Route Segment Config from App Router pages and layouts.

```diff filename="app/page.tsx"
- export const experimental_ppr = true;
```

#### Remove `unstable_` prefix from stabilized API

##### `remove-unstable-prefix`

```bash filename="Terminal"
npx @next/codemod@latest remove-unstable-prefix .
```

This codemod removes the `unstable_` prefix from stabilized API.

For example:

```ts
import { unstable_cacheTag as cacheTag } from 'next/cache'

cacheTag()
```

Transforms into:

```ts
import { cacheTag } from 'next/cache'

cacheTag()
```

#### Migrate from deprecated `middleware` convention to `proxy`

##### `middleware-to-proxy`

```bash filename="Terminal"
npx @next/codemod@latest middleware-to-proxy .
```

This codemod migrates projects from using the deprecated `middleware` convention to using the `proxy` convention. It:

* Renames `middleware.<extension>` to `proxy.<extension>` (e.g. `middleware.ts` to `proxy.ts`)
* Renames named export `middleware` to `proxy`
* Renames Next.js config property `experimental.middlewarePrefetch` to `experimental.proxyPrefetch`
* Renames Next.js config property `experimental.middlewareClientMaxBodySize` to `experimental.proxyClientMaxBodySize`
* Renames Next.js config property `experimental.externalMiddlewareRewritesResolve` to `experimental.externalProxyRewritesResolve`
* Renames Next.js config property `skipMiddlewareUrlNormalize` to `skipProxyUrlNormalize`

For example:

```ts filename="middleware.ts"
import { NextResponse } from 'next/server'

export function middleware() {
  return NextResponse.next()
}
```

Transforms into:

```ts filename="proxy.ts"
import { NextResponse } from 'next/server'

export function proxy() {
  return NextResponse.next()
}
```

#### Migrate from `next lint` to ESLint CLI

##### `next-lint-to-eslint-cli`

```bash filename="Terminal"
npx @next/codemod@canary next-lint-to-eslint-cli .
```

This codemod migrates projects from using `next lint` to using the ESLint CLI with your local ESLint config. It:

* Creates an `eslint.config.mjs` file with Next.js recommended configurations
* Updates `package.json` scripts to use `eslint .` instead of `next lint`
* Adds necessary ESLint dependencies to `package.json`
* Preserves existing ESLint configurations when found

For example:

```json filename="package.json"
{
  "scripts": {
    "lint": "next lint"
  }
}
```

Becomes:

```json filename="package.json"
{
  "scripts": {
    "lint": "eslint ."
  }
}
```

And creates:

```js filename="eslint.config.mjs"
import { dirname } from 'path'
import { fileURLToPath } from 'url'
import { FlatCompat } from '@eslint/eslintrc'

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const compat = new FlatCompat({
  baseDirectory: __dirname,
})

const eslintConfig = [
  ...compat.extends('next/core-web-vitals', 'next/typescript'),
  {
    ignores: [
      'node_modules/**',
      '.next/**',
      'out/**',
      'build/**',
      'next-env.d.ts',
    ],
  },
]

export default eslintConfig
```

### 15.0

#### Transform App Router Route Segment Config `runtime` value from `experimental-edge` to `edge`

##### `app-dir-runtime-config-experimental-edge`

> **Note**: This codemod is App Router specific.

```bash filename="Terminal"
npx @next/codemod@latest app-dir-runtime-config-experimental-edge .
```

This codemod transforms [Route Segment Config `runtime`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#runtime) value `experimental-edge` to `edge`.

For example:

```ts
export const runtime = 'experimental-edge'
```

Transforms into:

```ts
export const runtime = 'edge'
```

#### Migrate to async Dynamic APIs

APIs that opted into dynamic rendering that previously supported synchronous access are now asynchronous. You can read more about this breaking change in the [upgrade guide](/docs/app/guides/upgrading/version-15.md).

##### `next-async-request-api`

```bash filename="Terminal"
npx @next/codemod@latest next-async-request-api .
```

This codemod will transform dynamic APIs (`cookies()`, `headers()` and `draftMode()` from `next/headers`) that are now asynchronous to be properly awaited or wrapped with `React.use()` if applicable.
When an automatic migration isn't possible, the codemod will either add a typecast (if a TypeScript file) or a comment to inform the user that it needs to be manually reviewed & updated.

For example:

```tsx
import { cookies, headers } from 'next/headers'
const token = cookies().get('token')

function useToken() {
  const token = cookies().get('token')
  return token
}

export default function Page() {
  const name = cookies().get('name')
}

function getHeader() {
  return headers().get('x-foo')
}
```

Transforms into:

```tsx
import { use } from 'react'
import {
  cookies,
  headers,
  type UnsafeUnwrappedCookies,
  type UnsafeUnwrappedHeaders,
} from 'next/headers'
const token = (cookies() as unknown as UnsafeUnwrappedCookies).get('token')

function useToken() {
  const token = use(cookies()).get('token')
  return token
}

export default async function Page() {
  const name = (await cookies()).get('name')
}

function getHeader() {
  return (headers() as unknown as UnsafeUnwrappedHeaders).get('x-foo')
}
```

When we detect property access on the `params` or `searchParams` props in the page / route entries (`page.js`, `layout.js`, `route.js`, or `default.js`) or the `generateMetadata` / `generateViewport` APIs,
it will attempt to transform the callsite from a sync to an async function, and await the property access. If it can't be made async (such as with a Client Component), it will use `React.use` to unwrap the promise .

For example:

```tsx
// page.tsx
export default function Page({
  params,
  searchParams,
}: {
  params: { slug: string }
  searchParams: { [key: string]: string | string[] | undefined }
}) {
  const { value } = searchParams
  if (value === 'foo') {
    // ...
  }
}

export function generateMetadata({ params }: { params: { slug: string } }) {
  const { slug } = params
  return {
    title: `My Page - ${slug}`,
  }
}
```

Transforms into:

```tsx
// page.tsx
export default async function Page(props: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const searchParams = await props.searchParams
  const { value } = searchParams
  if (value === 'foo') {
    // ...
  }
}

export async function generateMetadata(props: {
  params: Promise<{ slug: string }>
}) {
  const params = await props.params
  const { slug } = params
  return {
    title: `My Page - ${slug}`,
  }
}
```

> **Good to know:** When this codemod identifies a spot that might require manual intervention, but we aren't able to determine the exact fix, it will add a comment or typecast to the code to inform the user that it needs to be manually updated. These comments are prefixed with **@next/codemod**, and typecasts are prefixed with `UnsafeUnwrapped`.
> Your build will error until these comments are explicitly removed. [Read more](/docs/messages/sync-dynamic-apis.md).

#### Replace `geo` and `ip` properties of `NextRequest` with `@vercel/functions`

##### `next-request-geo-ip`

```bash filename="Terminal"
npx @next/codemod@latest next-request-geo-ip .
```

This codemod installs `@vercel/functions` and transforms `geo` and `ip` properties of `NextRequest` with corresponding `@vercel/functions` features.

For example:

```ts
import type { NextRequest } from 'next/server'

export function GET(req: NextRequest) {
  const { geo, ip } = req
}
```

Transforms into:

```ts
import type { NextRequest } from 'next/server'
import { geolocation, ipAddress } from '@vercel/functions'

export function GET(req: NextRequest) {
  const geo = geolocation(req)
  const ip = ipAddress(req)
}
```

### 14.0

#### Migrate `ImageResponse` imports

##### `next-og-import`

```bash filename="Terminal"
npx @next/codemod@latest next-og-import .
```

This codemod moves transforms imports from `next/server` to `next/og` for usage of [Dynamic OG Image Generation](/docs/app/getting-started/metadata-and-og-images.md#generated-open-graph-images).

For example:

```js
import { ImageResponse } from 'next/server'
```

Transforms into:

```js
import { ImageResponse } from 'next/og'
```

#### Use `viewport` export

##### `metadata-to-viewport-export`

```bash filename="Terminal"
npx @next/codemod@latest metadata-to-viewport-export .
```

This codemod migrates certain viewport metadata to `viewport` export.

For example:

```js
export const metadata = {
  title: 'My App',
  themeColor: 'dark',
  viewport: {
    width: 1,
  },
}
```

Transforms into:

```js
export const metadata = {
  title: 'My App',
}

export const viewport = {
  width: 1,
  themeColor: 'dark',
}
```

### 13.2

#### Use Built-in Font

##### `built-in-next-font`

```bash filename="Terminal"
npx @next/codemod@latest built-in-next-font .
```

This codemod uninstalls the `@next/font` package and transforms `@next/font` imports into the built-in `next/font`.

For example:

```js
import { Inter } from '@next/font/google'
```

Transforms into:

```js
import { Inter } from 'next/font/google'
```

### 13.0

#### Rename Next Image Imports

##### `next-image-to-legacy-image`

```bash filename="Terminal"
npx @next/codemod@latest next-image-to-legacy-image .
```

Safely renames `next/image` imports in existing Next.js 10, 11, or 12 applications to `next/legacy/image` in Next.js 13. Also renames `next/future/image` to `next/image`.

For example:

```jsx filename="pages/index.js"
import Image1 from 'next/image'
import Image2 from 'next/future/image'

export default function Home() {
  return (
    <div>
      <Image1 src="/test.jpg" width="200" height="300" />
      <Image2 src="/test.png" width="500" height="400" />
    </div>
  )
}
```

Transforms into:

```jsx filename="pages/index.js"
// 'next/image' becomes 'next/legacy/image'
import Image1 from 'next/legacy/image'
// 'next/future/image' becomes 'next/image'
import Image2 from 'next/image'

export default function Home() {
  return (
    <div>
      <Image1 src="/test.jpg" width="200" height="300" />
      <Image2 src="/test.png" width="500" height="400" />
    </div>
  )
}
```

#### Migrate to the New Image Component

##### `next-image-experimental`

```bash filename="Terminal"
npx @next/codemod@latest next-image-experimental .
```

Dangerously migrates from `next/legacy/image` to the new `next/image` by adding inline styles and removing unused props.

* Removes `layout` prop and adds `style`.
* Removes `objectFit` prop and adds `style`.
* Removes `objectPosition` prop and adds `style`.
* Removes `lazyBoundary` prop.
* Removes `lazyRoot` prop.

#### Remove `<a>` Tags From Link Components

##### `new-link`

```bash filename="Terminal"
npx @next/codemod@latest new-link .
```

Remove `<a>` tags inside [Link Components](/docs/app/api-reference/components/link.md).

For example:

```jsx
<Link href="/about">
  <a>About</a>
</Link>
// transforms into
<Link href="/about">
  About
</Link>

<Link href="/about">
  <a onClick={() => console.log('clicked')}>About</a>
</Link>
// transforms into
<Link href="/about" onClick={() => console.log('clicked')}>
  About
</Link>
```

### 11

#### Migrate from CRA

##### `cra-to-next`

```bash filename="Terminal"
npx @next/codemod cra-to-next
```

Migrates a Create React App project to Next.js; creating a Pages Router and necessary config to match behavior. Client-side only rendering is leveraged initially to prevent breaking compatibility due to `window` usage during SSR and can be enabled seamlessly to allow the gradual adoption of Next.js specific features.

Please share any feedback related to this transform [in this discussion](https://github.com/vercel/next.js/discussions/25858).

### 10

#### Add React imports

##### `add-missing-react-import`

```bash filename="Terminal"
npx @next/codemod add-missing-react-import
```

Transforms files that do not import `React` to include the import in order for the new [React JSX transform](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) to work.

For example:

```jsx filename="my-component.js"
export default class Home extends React.Component {
  render() {
    return <div>Hello World</div>
  }
}
```

Transforms into:

```jsx filename="my-component.js"
import React from 'react'
export default class Home extends React.Component {
  render() {
    return <div>Hello World</div>
  }
}
```

### 9

#### Transform Anonymous Components into Named Components

##### `name-default-component`

```bash filename="Terminal"
npx @next/codemod name-default-component
```

**Versions 9 and above.**

Transforms anonymous components into named components to make sure they work with [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh).

For example:

```jsx filename="my-component.js"
export default function () {
  return <div>Hello World</div>
}
```

Transforms into:

```jsx filename="my-component.js"
export default function MyComponent() {
  return <div>Hello World</div>
}
```

The component will have a camel-cased name based on the name of the file, and it also works with arrow functions.

### 8

> **Note**: Built-in AMP support and this codemod have been removed in Next.js 16.

#### Transform AMP HOC into page config

##### `withamp-to-config`

```bash filename="Terminal"
npx @next/codemod withamp-to-config
```

Transforms the `withAmp` HOC into Next.js 9 page configuration.

For example:

```js
// Before
import { withAmp } from 'next/amp'

function Home() {
  return <h1>My AMP Page</h1>
}

export default withAmp(Home)
```

```js
// After
export default function Home() {
  return <h1>My AMP Page</h1>
}

export const config = {
  amp: true,
}
```

### 6

#### Use `withRouter`

##### `url-to-withrouter`

```bash filename="Terminal"
npx @next/codemod url-to-withrouter
```

Transforms the deprecated automatically injected `url` property on top level pages to using `withRouter` and the `router` property it injects. Read more here: [https://nextjs.org/docs/messages/url-deprecated](/docs/messages/url-deprecated.md)

For example:

```js filename="From"
import React from 'react'
export default class extends React.Component {
  render() {
    const { pathname } = this.props.url
    return <div>Current pathname: {pathname}</div>
  }
}
```

```js filename="To"
import React from 'react'
import { withRouter } from 'next/router'
export default withRouter(
  class extends React.Component {
    render() {
      const { pathname } = this.props.router
      return <div>Current pathname: {pathname}</div>
    }
  }
)
```

This is one case. All the cases that are transformed (and tested) can be found in the [`__testfixtures__` directory](https://github.com/vercel/next.js/tree/canary/packages/next-codemod/transforms/__testfixtures__/url-to-withrouter).


--------------------------------------------------------------------------------
title: "How to upgrade to version 14"
description: "Upgrade your Next.js Application from Version 13 to 14."
source: "https://nextjs.org/docs/app/guides/upgrading/version-14"
--------------------------------------------------------------------------------

# Version 14

## Upgrading from 13 to 14

To update to Next.js version 14, run the following command using your preferred package manager:

```bash filename="Terminal"
npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

```bash filename="Terminal"
yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

```bash filename="Terminal"
pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

```bash filename="Terminal"
bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

### v14 Summary

* The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life.
* The `next export` command has been removed in favor of `output: 'export'` config. Please see the [docs](https://nextjs.org/docs/app/guides/static-exports) for more information.
* The `next/server` import for `ImageResponse` was renamed to `next/og`. A [codemod is available](/docs/app/guides/upgrading/codemods.md#next-og-import) to safely and automatically rename your imports.
* The `@next/font` package has been fully removed in favor of the built-in `next/font`. A [codemod is available](/docs/app/guides/upgrading/codemods.md#built-in-next-font) to safely and automatically rename your imports.
* The WASM target for `next-swc` has been removed.


--------------------------------------------------------------------------------
title: "How to upgrade to version 15"
description: "Upgrade your Next.js Application from Version 14 to 15."
source: "https://nextjs.org/docs/app/guides/upgrading/version-15"
--------------------------------------------------------------------------------

# Version 15

## Upgrading from 14 to 15

To update to Next.js version 15, you can use the `upgrade` codemod:

```bash filename="Terminal"
npx @next/codemod@canary upgrade latest
```

If you prefer to do it manually, ensure that you're installing the latest Next & React versions:

```bash filename="Terminal"
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

> **Good to know:**
>
> * If you see a peer dependencies warning, you may need to update `react` and `react-dom` to the suggested versions, or use the `--force` or `--legacy-peer-deps` flag to ignore the warning. This won't be necessary once both Next.js 15 and React 19 are stable.

## React 19

* The minimum versions of `react` and `react-dom` is now 19.
* `useFormState` has been replaced by `useActionState`. The `useFormState` hook is still available in React 19, but it is deprecated and will be removed in a future release. `useActionState` is recommended and includes additional properties like reading the `pending` state directly. [Learn more](https://react.dev/reference/react/useActionState).
* `useFormStatus` now includes additional keys like `data`, `method`, and `action`. If you are not using React 19, only the `pending` key is available. [Learn more](https://react.dev/reference/react-dom/hooks/useFormStatus).
* Read more in the [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide).

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

## Async Request APIs (Breaking change)

Previously synchronous Dynamic APIs that rely on runtime information are now **asynchronous**:

* [`cookies`](/docs/app/api-reference/functions/cookies.md)
* [`headers`](/docs/app/api-reference/functions/headers.md)
* [`draftMode`](/docs/app/api-reference/functions/draft-mode.md)
* `params` in [`layout.js`](/docs/app/api-reference/file-conventions/layout.md), [`page.js`](/docs/app/api-reference/file-conventions/page.md), [`route.js`](/docs/app/api-reference/file-conventions/route.md), [`default.js`](/docs/app/api-reference/file-conventions/default.md), [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md), [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md), [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md), and [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md).
* `searchParams` in [`page.js`](/docs/app/api-reference/file-conventions/page.md)

To ease the burden of migration, a [codemod is available](/docs/app/guides/upgrading/codemods.md#150) to automate the process and the APIs can temporarily be accessed synchronously.

### `cookies`

#### Recommended Async Usage

```tsx
import { cookies } from 'next/headers'

// Before
const cookieStore = cookies()
const token = cookieStore.get('token')

// After
const cookieStore = await cookies()
const token = cookieStore.get('token')
```

#### Temporary Synchronous Usage

```tsx filename="app/page.tsx" switcher
import { cookies, type UnsafeUnwrappedCookies } from 'next/headers'

// Before
const cookieStore = cookies()
const token = cookieStore.get('token')

// After
const cookieStore = cookies() as unknown as UnsafeUnwrappedCookies
// will log a warning in dev
const token = cookieStore.get('token')
```

```jsx filename="app/page.js" switcher
import { cookies } from 'next/headers'

// Before
const cookieStore = cookies()
const token = cookieStore.get('token')

// After
const cookieStore = cookies()
// will log a warning in dev
const token = cookieStore.get('token')
```

### `headers`

#### Recommended Async Usage

```tsx
import { headers } from 'next/headers'

// Before
const headersList = headers()
const userAgent = headersList.get('user-agent')

// After
const headersList = await headers()
const userAgent = headersList.get('user-agent')
```

#### Temporary Synchronous Usage

```tsx filename="app/page.tsx" switcher
import { headers, type UnsafeUnwrappedHeaders } from 'next/headers'

// Before
const headersList = headers()
const userAgent = headersList.get('user-agent')

// After
const headersList = headers() as unknown as UnsafeUnwrappedHeaders
// will log a warning in dev
const userAgent = headersList.get('user-agent')
```

```jsx filename="app/page.js" switcher
import { headers } from 'next/headers'

// Before
const headersList = headers()
const userAgent = headersList.get('user-agent')

// After
const headersList = headers()
// will log a warning in dev
const userAgent = headersList.get('user-agent')
```

### `draftMode`

#### Recommended Async Usage

```tsx
import { draftMode } from 'next/headers'

// Before
const { isEnabled } = draftMode()

// After
const { isEnabled } = await draftMode()
```

#### Temporary Synchronous Usage

```tsx filename="app/page.tsx" switcher
import { draftMode, type UnsafeUnwrappedDraftMode } from 'next/headers'

// Before
const { isEnabled } = draftMode()

// After
// will log a warning in dev
const { isEnabled } = draftMode() as unknown as UnsafeUnwrappedDraftMode
```

```jsx filename="app/page.js" switcher
import { draftMode } from 'next/headers'

// Before
const { isEnabled } = draftMode()

// After
// will log a warning in dev
const { isEnabled } = draftMode()
```

### `params` & `searchParams`

#### Asynchronous Layout

```tsx filename="app/layout.tsx" switcher
// Before
type Params = { slug: string }

export function generateMetadata({ params }: { params: Params }) {
  const { slug } = params
}

export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = params
}

// After
type Params = Promise<{ slug: string }>

export async function generateMetadata({ params }: { params: Params }) {
  const { slug } = await params
}

export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = await params
}
```

```jsx filename="app/layout.js" switcher
// Before
export function generateMetadata({ params }) {
  const { slug } = params
}

export default async function Layout({ children, params }) {
  const { slug } = params
}

// After
export async function generateMetadata({ params }) {
  const { slug } = await params
}

export default async function Layout({ children, params }) {
  const { slug } = await params
}
```

#### Synchronous Layout

```tsx filename="app/layout.tsx" switcher
// Before
type Params = { slug: string }

export default function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Params
}) {
  const { slug } = params
}

// After
import { use } from 'react'

type Params = Promise<{ slug: string }>

export default function Layout(props: {
  children: React.ReactNode
  params: Params
}) {
  const params = use(props.params)
  const slug = params.slug
}
```

```jsx filename="app/layout.js" switcher
// Before
export default function Layout({ children, params }) {
  const { slug } = params
}

// After
import { use } from 'react'
export default async function Layout(props) {
  const params = use(props.params)
  const slug = params.slug
}

```

#### Asynchronous Page

```tsx filename="app/page.tsx" switcher
// Before
type Params = { slug: string }
type SearchParams = { [key: string]: string | string[] | undefined }

export function generateMetadata({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

export default async function Page({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

// After
type Params = Promise<{ slug: string }>
type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>

export async function generateMetadata(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}

export default async function Page(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}
```

```jsx filename="app/page.js" switcher
// Before
export function generateMetadata({ params, searchParams }) {
  const { slug } = params
  const { query } = searchParams
}

export default function Page({ params, searchParams }) {
  const { slug } = params
  const { query } = searchParams
}

// After
export async function generateMetadata(props) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}

export async function Page(props) {
  const params = await props.params
  const searchParams = await props.searchParams
  const slug = params.slug
  const query = searchParams.query
}
```

#### Synchronous Page

```tsx
'use client'

// Before
type Params = { slug: string }
type SearchParams = { [key: string]: string | string[] | undefined }

export default function Page({
  params,
  searchParams,
}: {
  params: Params
  searchParams: SearchParams
}) {
  const { slug } = params
  const { query } = searchParams
}

// After
import { use } from 'react'

type Params = Promise<{ slug: string }>
type SearchParams = Promise<{ [key: string]: string | string[] | undefined }>

export default function Page(props: {
  params: Params
  searchParams: SearchParams
}) {
  const params = use(props.params)
  const searchParams = use(props.searchParams)
  const slug = params.slug
  const query = searchParams.query
}
```

```jsx
// Before
export default function Page({ params, searchParams }) {
  const { slug } = params
  const { query } = searchParams
}

// After
import { use } from "react"

export default function Page(props) {
  const params = use(props.params)
  const searchParams = use(props.searchParams)
  const slug = params.slug
  const query = searchParams.query
}

```

#### Route Handlers

```tsx filename="app/api/route.ts" switcher
// Before
type Params = { slug: string }

export async function GET(request: Request, segmentData: { params: Params }) {
  const params = segmentData.params
  const slug = params.slug
}

// After
type Params = Promise<{ slug: string }>

export async function GET(request: Request, segmentData: { params: Params }) {
  const params = await segmentData.params
  const slug = params.slug
}
```

```js filename="app/api/route.js" switcher
// Before
export async function GET(request, segmentData) {
  const params = segmentData.params
  const slug = params.slug
}

// After
export async function GET(request, segmentData) {
  const params = await segmentData.params
  const slug = params.slug
}
```

## `runtime` configuration (Breaking change)

The `runtime` [segment configuration](/docs/app/api-reference/file-conventions/route-segment-config.md#runtime) previously supported a value of `experimental-edge` in addition to `edge`. Both configurations refer to the same thing, and to simplify the options, we will now error if `experimental-edge` is used. To fix this, update your `runtime` configuration to `edge`. A [codemod](/docs/app/guides/upgrading/codemods.md#app-dir-runtime-config-experimental-edge) is available to automatically do this.

## `fetch` requests

[`fetch` requests](/docs/app/api-reference/functions/fetch.md) are no longer cached by default.

To opt specific `fetch` requests into caching, you can pass the `cache: 'force-cache'` option.

```js filename="app/layout.js"
export default async function RootLayout() {
  const a = await fetch('https://...') // Not Cached
  const b = await fetch('https://...', { cache: 'force-cache' }) // Cached

  // ...
}
```

To opt all `fetch` requests in a layout or page into caching, you can use the `export const fetchCache = 'default-cache'` [segment config option](/docs/app/api-reference/file-conventions/route-segment-config.md). If individual `fetch` requests specify a `cache` option, that will be used instead.

```js filename="app/layout.js"
// Since this is the root layout, all fetch requests in the app
// that don't set their own cache option will be cached.
export const fetchCache = 'default-cache'

export default async function RootLayout() {
  const a = await fetch('https://...') // Cached
  const b = await fetch('https://...', { cache: 'no-store' }) // Not cached

  // ...
}
```

## Route Handlers

`GET` functions in [Route Handlers](/docs/app/api-reference/file-conventions/route.md) are no longer cached by default. To opt `GET` methods into caching, you can use a [route config option](/docs/app/api-reference/file-conventions/route-segment-config.md) such as `export const dynamic = 'force-static'` in your Route Handler file.

```js filename="app/api/route.js"
export const dynamic = 'force-static'

export async function GET() {}
```

## Client-side Router Cache

When navigating between pages via `<Link>` or `useRouter`, [page](/docs/app/api-reference/file-conventions/page.md) segments are no longer reused from the client-side router cache. However, they are still reused during browser backward and forward navigation and for shared layouts.

To opt page segments into caching, you can use the [`staleTimes`](/docs/app/api-reference/config/next-config-js/staleTimes.md) config option:

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

[Layouts](/docs/app/api-reference/file-conventions/layout.md) and [loading states](/docs/app/api-reference/file-conventions/loading.md) are still cached and reused on navigation.

## `next/font`

The `@next/font` package has been removed in favor of the built-in [`next/font`](/docs/app/api-reference/components/font.md). A [codemod is available](/docs/app/guides/upgrading/codemods.md#built-in-next-font) to safely and automatically rename your imports.

```js filename="app/layout.js"
// Before
import { Inter } from '@next/font/google'

// After
import { Inter } from 'next/font/google'
```

## bundlePagesRouterDependencies

`experimental.bundlePagesExternals` is now stable and renamed to `bundlePagesRouterDependencies`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Before
  experimental: {
    bundlePagesExternals: true,
  },

  // After
  bundlePagesRouterDependencies: true,
}

module.exports = nextConfig
```

## serverExternalPackages

`experimental.serverComponentsExternalPackages` is now stable and renamed to `serverExternalPackages`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Before
  experimental: {
    serverComponentsExternalPackages: ['package-name'],
  },

  // After
  serverExternalPackages: ['package-name'],
}

module.exports = nextConfig
```

## Speed Insights

Auto instrumentation for Speed Insights was removed in Next.js 15.

To continue using Speed Insights, follow the [Vercel Speed Insights Quickstart](https://vercel.com/docs/speed-insights/quickstart) guide.

## `NextRequest` Geolocation

The `geo` and `ip` properties on `NextRequest` have been removed as these values are provided by your hosting provider. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available to automate this migration.

If you are using Vercel, you can alternatively use the `geolocation` and `ipAddress` functions from [`@vercel/functions`](https://vercel.com/docs/functions/vercel-functions-package) instead:

```ts filename="middleware.ts"
import { geolocation } from '@vercel/functions'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const { city } = geolocation(request)

  // ...
}
```

```ts filename="middleware.ts"
import { ipAddress } from '@vercel/functions'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const ip = ipAddress(request)

  // ...
}
```


--------------------------------------------------------------------------------
title: "How to upgrade to version 16"
description: "Upgrade your Next.js Application from Version 15 to 16."
source: "https://nextjs.org/docs/app/guides/upgrading/version-16"
--------------------------------------------------------------------------------

# Version 16

## Upgrading from 15 to 16

### Using AI Agents with Next.js DevTools MCP

If you're using an AI coding assistant that supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), you can use the **Next.js DevTools MCP** to automate the upgrade process and migration tasks.

#### Setup

Add the following configuration to your MCP client, example:

```json
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

For more information, visit the [`next-devtools-mcp`](https://www.npmjs.com/package/next-devtools-mcp) package on npm to configure with your MCP client.

> **Note:** Using `next-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Next.js DevTools MCP server.

#### Example Prompts

Once configured, you can use natural language prompts to upgrade your Next.js app:

**To upgrade to Next.js 16:**

Connect to your coding agent and then prompt:

```txt
Next Devtools, help me upgrade my Next.js app to version 16
```

**To migrate to Cache Components (after upgrading to v16):**

Connect to your coding agent and then prompt:

```txt
Next Devtools, migrate my Next.js app to cache components
```

Learn more in the documentation [here](/docs/app/guides/mcp.md).

### Using the Codemod

To update to Next.js version 16, you can use the `upgrade` [codemod](/docs/app/guides/upgrading/codemods.md#160):

```bash filename="Terminal"
npx @next/codemod@canary upgrade latest
```

The [codemod](/docs/app/guides/upgrading/codemods.md#160) is able to:

* Update `next.config.js` to use the new `turbopack` configuration
* Migrate from `next lint` to the ESLint CLI
* Migrate from deprecated `middleware` convention to `proxy`
* Remove `unstable_` prefix from stabilized APIs
* Remove `experimental_ppr` Route Segment Config from pages and layouts

If you prefer to do it manually, install the latest Next.js and React versions:

```bash filename="Terminal"
npm install next@latest react@latest react-dom@latest
```

If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

## Node.js runtime and browser support

| Requirement   | Change / Details                                                   |
| ------------- | ------------------------------------------------------------------ |
| Node.js 20.9+ | Minimum version now `20.9.0` (LTS); Node.js 18 no longer supported |
| TypeScript 5+ | Minimum version now `5.1.0`                                        |
| Browsers      | Chrome 111+, Edge 111+, Firefox 111+, Safari 16.4+                 |

## Turbopack by default

Starting with **Next.js 16**, Turbopack is stable and used by default with `next dev` and `next build`

Previously you had to enable Turbopack using `--turbopack`, or `--turbo`.

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build --turbopack",
    "start": "next start"
  }
}
```

This is no longer necessary. You can update your `package.json` scripts:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

If your project has a [custom `webpack`](/docs/app/api-reference/config/next-config-js/webpack.md) configuration and you run `next build` (which now uses Turbopack by default), the build will **fail** to prevent misconfiguration issues.

You have a few different ways to address this:

* **Use Turbopack anyway:** Run with `next build --turbopack` to build using Turbopack and ignore your `webpack` config.
* **Switch to Turbopack fully:** Migrate your `webpack` config to Turbopack-compatible options.
* **Keep using Webpack:** Use the `--webpack` flag to opt out of Turbopack and build with Webpack.

> **Good to know**: If you see failing builds because a `webpack` configuration was found, but you don't define one yourself, it is likely that a plugin is adding a `webpack` option

### Opting out of Turbopack

If you need to continue using Webpack, you can opt out with the `--webpack` flag. For example, to use Turbopack in development but Webpack for production builds:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build --webpack",
    "start": "next start"
  }
}
```

We recommend using Turbopack for development and production. Submit a comment to this [thread](https://github.com/vercel/next.js/discussions/77721), if you are unable to switch to Turbopack.

### Turbopack configuration location

The `experimental.turbopack` configuration is out of experimental.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

// Next.js 15 - experimental.turbopack
const nextConfig: NextConfig = {
  experimental: {
    turbopack: {
      // options
    },
  },
}

export default nextConfig
```

You can use it as a top-level `turbopack` option:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

// Next.js 16 - turbopack at the top level of nextConfig
const nextConfig: NextConfig = {
  turbopack: {
    // options
  },
}

export default nextConfig
```

Make sure to review the `Turbopack` configuration [options](/docs/app/api-reference/config/next-config-js/turbopack.md). **Next.js 16** introduces various improvements and new options, for example:

* [Advanced Webpack loader conditions](/docs/app/api-reference/config/next-config-js/turbopack.md#advanced-webpack-loader-conditions)
* [debugIds](/docs/app/api-reference/config/next-config-js/turbopack.md#debug-ids)

### Resolve alias fallback

In some projects, client-side code may import files containing Node.js native modules. This will cause `Module not found: Can't resolve 'fs'` type of errors.

When this happens, you should refactor your code so that your client-side bundles do not reference these Node.js native modules.

However, in some cases, this might not be possible. In Webpack the `resolve.fallback` option was typically used to **silence** the error. Turbopack offers a similar option, using `turbopack.resolveAlias`. In this case, tell Turbopack to load an empty module when `fs` is requested for the browser.

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  turbopack: {
    resolveAlias: {
      fs: {
        browser: './empty.ts', // We recommend to fix code imports before using this method
      },
    },
  },
}

export default nextConfig
```

It is preferable to refactor your modules so that client code doesn't ever import from modules using Node.js native modules.

### Sass node\_modules imports

Turbopack fully supports importing Sass files from `node_modules`. Note that while Webpack allowed the legacy tilde (`~`) prefix, Turbopack does not support this syntax.

In Webpack:

```scss filename="styles/globals.scss"
@import '~bootstrap/dist/css/bootstrap.min.css';
```

In Turbopack:

```scss filename="styles/globals.scss"
@import 'bootstrap/dist/css/bootstrap.min.css';
```

If changing the imports is not possible, you can use `turbopack.resolveAlias`. For example:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  turbopack: {
    resolveAlias: {
      '~*': '*',
    },
  },
}

export default nextConfig
```

### Turbopack File System Caching (beta)

Turbopack now supports filesystem caching in development, storing compiler artifacts on disk between runs for significantly faster compile times across restarts.

Enable filesystem caching in your configuration:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbopackFileSystemCacheForDev: true,
  },
}

module.exports = nextConfig
```

## Async Request APIs (Breaking change)

Version 15 introduced [Async Request APIs](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change) as a breaking change, with **temporary** synchronous compatibility.

Starting with **Next.js 16**, synchronous access is fully removed. These APIs can only be accessed asynchronously.

* [`cookies`](/docs/app/api-reference/functions/cookies.md)
* [`headers`](/docs/app/api-reference/functions/headers.md)
* [`draftMode`](/docs/app/api-reference/functions/draft-mode.md)
* `params` in [`layout.js`](/docs/app/api-reference/file-conventions/layout.md), [`page.js`](/docs/app/api-reference/file-conventions/page.md), [`route.js`](/docs/app/api-reference/file-conventions/route.md), [`default.js`](/docs/app/api-reference/file-conventions/default.md), [`opengraph-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#opengraph-image), [`twitter-image`](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md#twitter-image), [`icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#icon), and [`apple-icon`](/docs/app/api-reference/file-conventions/metadata/app-icons.md#apple-icon).
* `searchParams` in [`page.js`](/docs/app/api-reference/file-conventions/page.md)

Use the [codemod](/docs/app/guides/upgrading/codemods.md#migrate-to-async-dynamic-apis) to migrate to async Dynamic APIs.

### Migrating types for async Dynamic APIs

To help migrate to async `params` and `searchParams`, you can run [`npx next typegen`](/docs/app/api-reference/cli/next.md#next-typegen-options) to automatically generate these globally available types helpers:

* [`PageProps`](/docs/app/api-reference/file-conventions/page.md#page-props-helper)
* [`LayoutProps`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper)
* [`RouteContext`](/docs/app/api-reference/file-conventions/route.md#route-context-helper)

> **Good to know**: `typegen` was introduced in Next.js 15.5

This simplifies type-safe migration to the new async API pattern, and enables you to update your components with full type safety, for example:

```tsx filename="/app/blog/[slug]/page.tsx"
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  const query = await props.searchParams
  return <h1>Blog Post: {slug}</h1>
}
```

This approach gives you fully type-safe access to `props.params`, including the `slug`, and to `searchParams`, directly within your page.

## Async parameters for icon, and open-graph Image (Breaking change)

> The props passed to the image generating functions in `opengraph-image`, `twitter-image`, `icon`, and `apple-icon`, are now Promises.

In previous versions, both the `Image` (image generation function), and the `generateImageMetadata` received a `params` object. The `id` returned by `generateImageMetadata` was passed as a string to the image generation function.

```js filename="app/shop/[slug]/opengraph-image.js"
// Next.js 15 - synchronous params access
export function generateImageMetadata({ params }) {
  const { slug } = params
  return [{ id: '1' }, { id: '2' }]
}

// Next.js 15 - synchronous params and id access
export default function Image({ params, id }) {
  const slug = params.slug
  const imageId = id // string
  // ...
}
```

Starting with **Next.js 16**, to align with the [Async Request APIs](#async-request-apis-breaking-change) change, the image generating function now receives `params` and `id` as promises. The `generateImageMetadata` function continues to receive synchronous `params`.

```js filename="app/shop/[slug]/opengraph-image.js"
export async function generateImageMetadata({ params }) {
  const { slug } = params
  return [{ id: '1' }, { id: '2' }]
}

// Next.js 16 - asynchronous params and id access
export default async function Image({ params, id }) {
  const { slug } = await params // params now async
  const imageId = await id // id is now Promise<string> when using generateImageMetadata
  // ...
}
```

## Async `id` parameter for `sitemap` (Breaking change)

Previously, the `id` values returned from [`generateSitemaps`](/docs/app/api-reference/functions/generate-sitemaps.md) were passed directly to the `sitemap` generating function.

```js filename="app/product/sitemap.js"
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

// Next.js 15 - synchronous id access
export default async function sitemap({ id }) {
  const start = id * 50000 // id is a number
  // ...
}
```

Starting with **Next.js 16**, the `sitemap` generating function now receives `id` as a promise.

```js filename="app/product/sitemap.js"
export async function generateSitemaps() {
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

// Next.js 16 - asynchronous id access
export default async function sitemap({ id }) {
  const resolvedId = await id // id is now Promise<number>
  const start = resolvedId * 50000
  // ...
}
```

## React 19.2

The App Router in **Next.js 16** uses the latest React [Canary release](https://react.dev/blog/2023/05/03/react-canaries), which includes the newly released React 19.2 features and other features being incrementally stabilized. Highlights include:

* **[View Transitions](https://react.dev/reference/react/ViewTransition)**: Animate elements that update inside a Transition or navigation
* **[`useEffectEvent`](https://react.dev/reference/react/useEffectEvent)**: Extract non-reactive logic from Effects into reusable Effect Event functions
* **[Activity](https://react.dev/reference/react/Activity)**: Render "background activity" by hiding UI with `display: none` while maintaining state and cleaning up Effects

Learn more in the [React 19.2 announcement](https://react.dev/blog/2025/10/01/react-19-2).

## React Compiler Support

Built-in support for the React Compiler is now stable in **Next.js 16** following the React Compiler's 1.0 release. The React Compiler automatically memoizes components, reducing unnecessary re-renders with zero manual code changes.

The `reactCompiler` configuration option has been promoted from `experimental` to stable. It is not enabled by default as we continue gathering build performance data across different application types.

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

Install the latest version of the React Compiler plugin:

```bash filename="Terminal"
npm install -D babel-plugin-react-compiler
```

> **Good to know:** Expect compile times in development and during builds to be higher when enabling this option as the React Compiler relies on Babel.

## Caching APIs

### revalidateTag

[`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md) has a new function signature. You can pass a [`cacheLife`](/docs/app/api-reference/functions/cacheLife.md#reference) profile as the second argument.

```ts filename="app/actions.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateArticle(articleId: string) {
  // Mark article data as stale - article readers see stale data while it revalidates
  revalidateTag(`article-${articleId}`, 'max')
}
```

```js filename="app/actions.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function updateArticle(articleId) {
  // Mark article data as stale - article readers see stale data while it revalidates
  revalidateTag(`article-${articleId}`, 'max')
}
```

Use `revalidateTag` for content where a slight delay in updates is acceptable, such as blog posts, product catalogs, or documentation. Users receive stale content while fresh data loads in the background.

### updateTag

[`updateTag`](/docs/app/api-reference/functions/updateTag.md) is a new [Server Actions](/docs/app/getting-started/updating-data.md#what-are-server-functions)-only API that provides **read-your-writes** semantics, where a user makes a change and the UI immediately shows the change, rather than stale data.

It does this by expiring and immediately refreshing data within the same request.

```ts filename="app/actions.ts" switcher
'use server'

import { updateTag } from 'next/cache'

export async function updateUserProfile(userId: string, profile: Profile) {
  await db.users.update(userId, profile)

  // Expire cache and refresh immediately - user sees their changes right away
  updateTag(`user-${userId}`)
}
```

```js filename="app/actions.js" switcher
'use server'

import { updateTag } from 'next/cache'

export async function updateUserProfile(userId, profile) {
  await db.users.update(userId, profile)

  // Expire cache and refresh immediately - user sees their changes right away
  updateTag(`user-${userId}`)
}
```

This ensures interactive features reflect changes immediately. Perfect for forms, user settings, and any workflow where users expect to see their updates instantly.

Learn more about when to use `updateTag` or `revalidateTag` [here](/docs/app/api-reference/functions/updateTag.md#when-to-use-updatetag).

### refresh

[`refresh`](/docs/app/api-reference/functions/refresh.md) allows you to refresh the client router from within a Server Action.

```ts filename="app/actions.ts" switcher
'use server'

import { refresh } from 'next/cache'

export async function markNotificationAsRead(notificationId: string) {
  // Update the notification in the database
  await db.notifications.markAsRead(notificationId)

  // Refresh the notification count displayed in the header
  refresh()
}
```

```js filename="app/actions.js" switcher
'use server'

import { refresh } from 'next/cache'

export async function markNotificationAsRead(notificationId) {
  // Update the notification in the database
  await db.notifications.markAsRead(notificationId)

  // Refresh the notification count displayed in the header
  refresh()
}
```

Use it when you need to refresh the client router after performing an action.

### cacheLife and cacheTag

[`cacheLife`](/docs/app/api-reference/functions/cacheLife.md) and [`cacheTag`](/docs/app/api-reference/functions/cacheTag.md) are now stable. The `unstable_` prefix is no longer needed.

Wherever you had aliased imports like:

```ts
import {
  unstable_cacheLife as cacheLife,
  unstable_cacheTag as cacheTag,
} from 'next/cache'
```

You can update your imports to:

```ts
import { cacheLife, cacheTag } from 'next/cache'
```

## Enhanced Routing and Navigation

**Next.js 16** includes a complete overhaul of the routing and navigation system, making page transitions leaner and faster. This optimizes how Next.js prefetches and caches navigation data:

* **Layout deduplication**: When prefetching multiple URLs with a shared layout, the layout is downloaded once.
* **Incremental prefetching**: Next.js only prefetches parts not already in cache, rather than entire pages.

These changes require **no code modifications** and are designed to improve performance across all apps.

However, you may see more individual prefetch requests with much lower total transfer sizes. We believe this is the right trade-off for nearly all applications.

If the increased request count causes issues, please let us know by creating an [issue](https://github.com/vercel/next.js/issues) or [discussion](https://github.com/vercel/next.js/discussions) item.

## Partial Pre-Rendering (PPR)

**Next.js 16** removes the experimental **Partial Pre-Rendering (PPR)** flag and configuration options, including the route level segment `experimental_ppr`.

Starting with **Next.js 16**, you can opt into PPR using the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) configuration.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  cacheComponents: true,
}

module.exports = nextConfig
```

PPR in **Next.js 16** works differently than in **Next.js 15** canaries. If you are using PPR today, stay in the current Next.js 15 canary you are using. We will follow up with a guide to migrate to Cache Components.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  // If you are using PPR today
  // stay in the current Next.js 15 canary
  experimental: {
    ppr: true,
  },
}

module.exports = nextConfig
```

## `middleware` to `proxy`

The `middleware` filename is deprecated, and has been renamed to `proxy` to clarify network boundary and routing focus.

The `edge` runtime is **NOT** supported in `proxy`. The `proxy` runtime is `nodejs`, and it cannot be configured. If you want to continue using the `edge` runtime, keep using `middleware`. We will follow up on a minor release with further `edge` runtime instructions.

```bash filename="Terminal"
# Rename your middleware file
mv middleware.ts proxy.ts
# or
mv middleware.js proxy.js
```

The named export `middleware` is also deprecated. Rename your function to `proxy`.

```ts filename="proxy.ts" switcher
export function proxy(request: Request) {}
```

```js filename="proxy.js" switcher
export function proxy(request) {}
```

We recommend changing the function name to `proxy`, even if you are using a default export.

Configuration flags that contained the `middleware` name are also renamed. For example, `skipMiddlewareUrlNormalize` is now `skipProxyUrlNormalize`

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  skipProxyUrlNormalize: true,
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  skipProxyUrlNormalize: true,
}

module.exports = nextConfig
```

The version 16 [codemod](/docs/app/guides/upgrading/codemods.md#160) is able to update these flags too.

## `next/image` changes

### Local Images with Query Strings (Breaking change)

Local image sources with query strings now require `images.localPatterns.search` configuration to prevent enumeration attacks.

```tsx filename="app/page.tsx"
import Image from 'next/image'

export default function Page() {
  return <Image src="/assets/photo?v=1" alt="Photo" width="100" height="100" />
}
```

If you need to use query strings with local images, add the pattern to your configuration:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/**',
        search: '?v=1',
      },
    ],
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/**',
        search: '?v=1',
      },
    ],
  },
}

module.exports = nextConfig
```

### `minimumCacheTTL` Default (Breaking change)

The default value for `images.minimumCacheTTL` has changed from `60 seconds` to `4 hours` (14400 seconds). This reduces revalidation cost for images without cache-control headers.

For some Next.js users, image revalidation was happening frequently, often because the upstream source images missed a `cache-control` header. This caused revalidation to happen every `60` seconds, which increased CPU usage and cost.

Since most images do not change often, this short interval is not ideal. Setting the default to 4 hours offers a more durable cache by default, while still allowing images to update a few times per day if needed.

If you need the previous behavior, change `minimumCacheTTL` to a lower value, for example back to `60` seconds:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    minimumCacheTTL: 60,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    minimumCacheTTL: 60,
  },
}

module.exports = nextConfig
```

### `imageSizes` Default (Breaking change)

The value `16` has been removed from the default `images.imageSizes` array.

We have looked at request analytics and found out that very few projects ever serve 16 pixels width images. Removing this setting reduces the size of the `srcset` attribute shipped to the browser by `next/image`.

If you need to support 16px images:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
}

module.exports = nextConfig
```

Rather than lack of developer usage, we believe 16 pixels width images have become less common, because `devicePixelRatio: 2` actually fetches a 32px image to prevent blurriness in retina displays.

### `qualities` Default (Breaking change)

The default value for `images.qualities` has changed from allowing all qualities to only `[75]`.

If you need to support multiple quality levels:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    qualities: [50, 75, 100],
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    qualities: [50, 75, 100],
  },
}

module.exports = nextConfig
```

If you specify a `quality` prop not included in the `image.qualities` array, the quality will be coerced to the closest value in `images.qualities`. For example, given the configuration above, a `quality` prop of 80, is coerced to 75.

### Local IP Restriction (Breaking change)

A new security restriction blocks local IP optimization by default. Set `images.dangerouslyAllowLocalIP` to `true` only for private networks.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    dangerouslyAllowLocalIP: true, // Only for private networks
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    dangerouslyAllowLocalIP: true, // Only for private networks
  },
}

module.exports = nextConfig
```

### Maximum Redirects (Breaking change)

The default for `images.maximumRedirects` has changed from unlimited to 3 redirects maximum.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  images: {
    maximumRedirects: 0, // Disable redirects
    // or
    maximumRedirects: 5, // Increase for edge cases
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    maximumRedirects: 0, // Disable redirects
    // or
    maximumRedirects: 5, // Increase for edge cases
  },
}

module.exports = nextConfig
```

### `next/legacy/image` Component (deprecated)

The `next/legacy/image` component is deprecated. Use `next/image` instead:

```tsx
// Before
import Image from 'next/legacy/image'

// After
import Image from 'next/image'
```

### `images.domains` Configuration (deprecated)

The `images.domains` config is deprecated.

```js filename="next.config.js"
// image.domains is deprecated
module.exports = {
  images: {
    domains: ['example.com'],
  },
}
```

Use `images.remotePatterns` instead for improved security:

```js filename="next.config.js"
// Use image.remotePatterns instead
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
      },
    ],
  },
}
```

## Concurrent `dev` and `build`

`next dev` and `next build` now use separate output directories, enabling concurrent execution. The `next dev` command outputs to `.next/dev`. This is the new default behavior, controlled by [isolatedDevBuild](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md).

Additionally, a lockfile mechanism prevents multiple `next dev` or `next build` instances on the same project.

Since the development server outputs to `.next/dev`, the [Turbopack tracing command](/docs/app/guides/local-development.md#turbopack-tracing) should be:

```bash
npx next internal trace .next/dev/trace-turbopack
```

## Parallel Routes `default.js` requirement

All [parallel route](/docs/app/api-reference/file-conventions/parallel-routes.md) slots now require explicit `default.js` files. Builds will fail without them.

To maintain previous behavior, create a [`default.js`](/docs/app/api-reference/file-conventions/default.md) file that calls `notFound()` or returns `null`.

```tsx filename="app/@modal/default.tsx"
import { notFound } from 'next/navigation'

export default function Default() {
  notFound()
}
```

Or return `null`:

```tsx filename="app/@modal/default.tsx"
export default function Default() {
  return null
}
```

## ESLint Flat Config

`@next/eslint-plugin-next` now defaults to ESLint Flat Config format, aligning with ESLint v10 which will drop legacy config support.

Make sure to review our API reference for the [`@next/eslint-plugin-next`](/docs/app/api-reference/config/eslint.md#setup-eslint) plugin.

If you're using the legacy `.eslintrc` format, consider migrating to the flat config format. See the [ESLint migration guide](https://eslint.org/docs/latest/use/configure/migration-guide) for details.

## Scroll Behavior Override

In **previous versions of Next.js**, if you had set `scroll-behavior: smooth` globally on your `<html>` element via CSS, Next.js would override this during SPA route transitions, as follows:

1. Temporarily set `scroll-behavior` to `auto`
2. Perform the navigation (causing instant scroll to top)
3. Restore your original `scroll-behavior` value

This ensured that page navigation always felt snappy and instant, even when you had smooth scrolling enabled for in-page navigation. However, this manipulation could be expensive, especially at the start of every navigation.

In **Next.js 16**, this behavior has changed. By default, Next.js will **no longer override** your `scroll-behavior` setting during navigation.

**If you want Next.js to perform this override** (the previous default behavior), add the `data-scroll-behavior="smooth"` attribute to your `<html>` element:

```tsx filename="app/layout.tsx"
export default function RootLayout({ children }) {
  return (
    <html lang="en" data-scroll-behavior="smooth">
      <body>{children}</body>
    </html>
  )
}
```

## Performance Improvements

Significant performance optimizations for `next dev` and `next start` commands, along with improved terminal output with clearer formatting, better error messages, and improved performance metrics.

**Next.js 16** removes the `size` and `First Load JS` metrics from the `next build` output. We found these to be inaccurate in server-driven architectures using React Server Components. Both our Turbopack and Webpack implementations had issues, and disagreed on how to account for Client Components payload.

The most effective way to measure actual route performance is through tools such as [Chrome Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) or Vercel Analytics, which focus on Core Web Vitals and downloaded resource sizes.

### `next dev` config load

In previous versions the Next config file was loaded twice during development:

* When running the `next dev` command
* When the `next dev` command started the Next.js server

This was inefficient because the `next dev` command doesn't need the config file to start the Next.js server.

A consequence of this change is that, when running `next dev` checking if `process.argv` includes `'dev'`, in your Next.js config file, will return `false`.

> **Good to know**: The `typegen`, and `build` commands, are still visible in `process.argv`.

This is specially important for plugins that trigger side-effects on `next dev`. If that's the case, it might be enough to check if `NODE_ENV` is set to `development`.

```js filename="next.config.js"
import { startServer } from 'docs-lib/dev-server'

const isDev = process.env.NODE_ENV === 'development'

if (isDev) {
  startServer()
}

const nextConfig = {
  /* Your config options */
}

module.exports = nextConfig
```

Alternatively, use the [`phase`](/docs/app/api-reference/config/next-config-js.md#phase) in which the configuration is loaded.

## Build Adapters API (alpha)

Following the [Build Adapters RFC](https://github.com/vercel/next.js/discussions/77740), the first alpha version of the Build Adapters API is now available.

Build Adapters allow you to create custom adapters that hook into the build process, enabling deployment platforms and custom build integrations to modify Next.js configuration or process build output.

```js filename="next.config.js"
const nextConfig = {
  experimental: {
    adapterPath: require.resolve('./my-adapter.js'),
  },
}

module.exports = nextConfig
```

Share your feedback in the [RFC discussion](https://github.com/vercel/next.js/discussions/77740).

## Modern Sass API

`sass-loader` has been bumped to v16, which supports [modern Sass syntax](https://sass-lang.com/documentation/js-api/#md:usage) and new features.

## Removals

These features were previously deprecated and are now removed:

### AMP Support

AMP adoption has declined significantly, and maintaining this feature adds complexity to the framework. All AMP APIs and configurations have been removed:

* `amp` configuration from your Next config file
* `next/amp` hook imports and usage (`useAmp`)

```tsx
// Removed
import { useAmp } from 'next/amp'

// Removed
export const config = { amp: true }
```

* `export const config = { amp: true }` from pages

```js filename="next.config.js"
const nextConfig = {
  // Removed
  amp: {
    canonicalBase: 'https://example.com',
  },
}

export default nextConfig
```

Evaluate if AMP is still necessary for your use case. Most performance benefits can now be achieved through Next.js's built-in optimizations and modern web standards.

### `next lint` Command

The `next lint` command has been removed. Use Biome or ESLint directly. `next build` no longer runs linting.

A codemod is available to automate migration:

```bash filename="Terminal"
npx @next/codemod@canary next-lint-to-eslint-cli .
```

The `eslint` option in the Next.js config file is also removed.

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  // No longer supported
  // eslint: {},
}

export default nextConfig
```

### Runtime Configuration

`serverRuntimeConfig` and `publicRuntimeConfig` have been removed. Use environment variables instead.

**Before (Next.js 15):**

```js filename="next.config.js"
module.exports = {
  serverRuntimeConfig: {
    dbUrl: process.env.DATABASE_URL,
  },
  publicRuntimeConfig: {
    apiUrl: '/api',
  },
}
```

```tsx filename="pages/index.tsx"
import getConfig from 'next/config'

export default function Page() {
  const { publicRuntimeConfig } = getConfig()
  return <p>API URL: {publicRuntimeConfig.apiUrl}</p>
}
```

**After (Next.js 16):**

For server-only values, access environment variables directly in Server Components:

```tsx filename="app/page.tsx"
async function fetchData() {
  const dbUrl = process.env.DATABASE_URL
  // Use for server-side operations only
  return await db.query(dbUrl, 'SELECT * FROM users')
}

export default async function Page() {
  const data = await fetchData()
  return <div>{/* render data */}</div>
}
```

> **Good to know**: Use the [taint API](/docs/app/api-reference/config/next-config-js/taint.md) to prevent accidentally passing sensitive server values to Client Components.

For client-accessible values, use the `NEXT_PUBLIC_` prefix:

```bash filename=".env.local"
NEXT_PUBLIC_API_URL="/api"
```

```tsx filename="app/components/client-component.tsx"
'use client'

export default function ClientComponent() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL
  return <p>API URL: {apiUrl}</p>
}
```

To ensure environment variables are read at runtime (not bundled at build time), use the [`connection()`](/docs/app/api-reference/functions/connection.md) function before reading from `process.env`:

```tsx filename="app/page.tsx"
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  const config = process.env.RUNTIME_CONFIG
  return <p>{config}</p>
}
```

Learn more about [environment variables](/docs/app/guides/environment-variables.md).

### `devIndicators` Options

The following options have been removed from [`devIndicators`](/docs/app/api-reference/config/next-config-js/devIndicators.md):

* `appIsrStatus`
* `buildActivity`
* `buildActivityPosition`

The indicator itself remains available.

### `experimental.dynamicIO`

The `experimental.dynamicIO` flag has been renamed to `cacheComponents`:

Update your Next config file, by removing the `dynamicIO` flag.

```js filename="next.config.js"
// Next.js 15 - experimental.dynamicIO is now removed
module.exports = {
  experimental: {
    dynamicIO: true,
  },
}
```

Add the [`cacheComponents`](/docs/app/api-reference/config/next-config-js/cacheComponents.md) flag set to true.

```js filename="next.config.js"
// Next.js 16 - use cacheComponents instead
module.exports = {
  cacheComponents: true,
}
```

### `unstable_rootParams`

The `unstable_rootParams` function has been removed. We are working on an alternative API that we will ship in an upcoming minor release.


--------------------------------------------------------------------------------
title: "How to use and optimize videos"
description: "Recommendations and best practices for optimizing videos in your Next.js application."
source: "https://nextjs.org/docs/app/guides/videos"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./04-app-router.md) | [Index](./index.md) | [Next →](./06-videos.md)
