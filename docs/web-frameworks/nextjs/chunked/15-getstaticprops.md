**Navigation:** [← Previous](./14-static-exports.md) | [Index](./index.md) | [Next →](./16-instrumentationjs.md)

---

# getStaticProps

@router: Pages Router

If you export a function called `getStaticProps` (Static Site Generation) from a page, Next.js will pre-render this page at build time using the props returned by `getStaticProps`.

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

> Note that irrespective of rendering type, any `props` will be passed to the page component and can be viewed on the client-side in the initial HTML. This is to allow the page to be [hydrated](https://react.dev/reference/react-dom/hydrate) correctly. Make sure that you don't pass any sensitive information that shouldn't be available on the client in `props`.

The [`getStaticProps` API reference](/docs/pages/api-reference/functions/get-static-props.md) covers all parameters and props that can be used with `getStaticProps`.

## When should I use getStaticProps?

You should use `getStaticProps` if:

* The data required to render the page is available at build time ahead of a user’s request
* The data comes from a headless CMS
* The page must be pre-rendered (for SEO) and be very fast — `getStaticProps` generates `HTML` and `JSON` files, both of which can be cached by a CDN for performance
* The data can be publicly cached (not user-specific). This condition can be bypassed in certain specific situation by using a Proxy to rewrite the path.

## When does getStaticProps run

`getStaticProps` always runs on the server and never on the client. You can validate code written inside `getStaticProps` is removed from the client-side bundle [with this tool](https://next-code-elimination.vercel.app/).

* `getStaticProps` always runs during `next build`
* `getStaticProps` runs in the background when using [`fallback: true`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true)
* `getStaticProps` is called before initial render when using [`fallback: blocking`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-blocking)
* `getStaticProps` runs in the background when using `revalidate`
* `getStaticProps` runs on-demand in the background when using [`revalidate()`](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath)

When combined with [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md), `getStaticProps` will run in the background while the stale page is being revalidated, and the fresh page served to the browser.

`getStaticProps` does not have access to the incoming request (such as query parameters or HTTP headers) as it generates static HTML. If you need access to the request for your page, consider using [Proxy](/docs/pages/api-reference/file-conventions/proxy.md) in addition to `getStaticProps`.

## Using getStaticProps to fetch data from a CMS

The following example shows how you can fetch a list of blog posts from a CMS.

```tsx filename="pages/blog.tsx" switcher
// posts will be populated at build time by getStaticProps()
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}
```

```jsx filename="pages/blog.js" switcher
// posts will be populated at build time by getStaticProps()
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}

// This function gets called at build time on server-side.
// It won't be called on client-side, so you can even do
// direct database queries.
export async function getStaticProps() {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // By returning { props: { posts } }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}
```

The [`getStaticProps` API reference](/docs/pages/api-reference/functions/get-static-props.md) covers all parameters and props that can be used with `getStaticProps`.

## Write server-side code directly

As `getStaticProps` runs only on the server-side, it will never run on the client-side. It won’t even be included in the JS bundle for the browser, so you can write direct database queries without them being sent to browsers.

This means that instead of fetching an **API route** from `getStaticProps` (that itself fetches data from an external source), you can write the server-side code directly in `getStaticProps`.

Take the following example. An API route is used to fetch some data from a CMS. That API route is then called directly from `getStaticProps`. This produces an additional call, reducing performance. Instead, the logic for fetching the data from the CMS can be shared by using a `lib/` directory. Then it can be shared with `getStaticProps`.

```js filename="lib/load-posts.js"
// The following function is shared
// with getStaticProps and API routes
// from a `lib/` directory
export async function loadPosts() {
  // Call an external API endpoint to get posts
  const res = await fetch('https://.../posts/')
  const data = await res.json()

  return data
}
```

```jsx filename="pages/blog.js"
// pages/blog.js
import { loadPosts } from '../lib/load-posts'

// This function runs only on the server side
export async function getStaticProps() {
  // Instead of fetching your `/api` route you can call the same
  // function directly in `getStaticProps`
  const posts = await loadPosts()

  // Props returned will be passed to the page component
  return { props: { posts } }
}
```

Alternatively, if you are **not** using API routes to fetch data, then the [`fetch()`](https://developer.mozilla.org/docs/Web/API/Fetch_API) API *can* be used directly in `getStaticProps` to fetch data.

To verify what Next.js eliminates from the client-side bundle, you can use the [next-code-elimination tool](https://next-code-elimination.vercel.app/).

## Statically generates both HTML and JSON

When a page with `getStaticProps` is pre-rendered at build time, in addition to the page HTML file, Next.js generates a JSON file holding the result of running `getStaticProps`.

This JSON file will be used in client-side routing through [`next/link`](/docs/pages/api-reference/components/link.md) or [`next/router`](/docs/pages/api-reference/functions/use-router.md). When you navigate to a page that’s pre-rendered using `getStaticProps`, Next.js fetches this JSON file (pre-computed at build time) and uses it as the props for the page component. This means that client-side page transitions will **not** call `getStaticProps` as only the exported JSON is used.

When using Incremental Static Generation, `getStaticProps` will be executed in the background to generate the JSON needed for client-side navigation. You may see this in the form of multiple requests being made for the same page, however, this is intended and has no impact on end-user performance.

## Where can I use getStaticProps

`getStaticProps` can only be exported from a **page**. You **cannot** export it from non-page files, `_app`, `_document`, or `_error`.

One of the reasons for this restriction is that React needs to have all the required data before the page is rendered.

Also, you must use export `getStaticProps` as a standalone function — it will **not** work if you add `getStaticProps` as a property of the page component.

> **Good to know**: if you have created a [custom app](/docs/pages/building-your-application/routing/custom-app.md), ensure you are passing the `pageProps` to the page component as shown in the linked document, otherwise the props will be empty.

## Runs on every request in development

In development (`next dev`), `getStaticProps` will be called on every request.

## Preview Mode

You can temporarily bypass static generation and render the page at **request time** instead of build time using [**Preview Mode**](/docs/pages/guides/preview-mode.md). For example, you might be using a headless CMS and want to preview drafts before they're published.


--------------------------------------------------------------------------------
title: "getStaticPaths"
description: "Fetch data and generate static pages with `getStaticPaths`. Learn more about this API for data fetching in Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths"
--------------------------------------------------------------------------------

# getStaticPaths

@router: Pages Router

If a page has [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md) and uses `getStaticProps`, it needs to define a list of paths to be statically generated.

When you export a function called `getStaticPaths` (Static Site Generation) from a page that uses dynamic routes, Next.js will statically pre-render all the paths specified by `getStaticPaths`.

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

The [`getStaticPaths` API reference](/docs/pages/api-reference/functions/get-static-paths.md) covers all parameters and props that can be used with `getStaticPaths`.

## When should I use getStaticPaths?

You should use `getStaticPaths` if you’re statically pre-rendering pages that use dynamic routes and:

* The data comes from a headless CMS
* The data comes from a database
* The data comes from the filesystem
* The data can be publicly cached (not user-specific)
* The page must be pre-rendered (for SEO) and be very fast — `getStaticProps` generates `HTML` and `JSON` files, both of which can be cached by a CDN for performance

## When does getStaticPaths run

`getStaticPaths` will only run during build in production, it will not be called during runtime. You can validate code written inside `getStaticPaths` is removed from the client-side bundle [with this tool](https://next-code-elimination.vercel.app/).

### How does getStaticProps run with regards to getStaticPaths

* `getStaticProps` runs during `next build` for any `paths` returned during build
* `getStaticProps` runs in the background when using `fallback: true`
* `getStaticProps` is called before initial render when using `fallback: blocking`

## Where can I use getStaticPaths

* `getStaticPaths` **must** be used with `getStaticProps`
* You **cannot** use `getStaticPaths` with [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md)
* You can export `getStaticPaths` from a [Dynamic Route](/docs/pages/building-your-application/routing/dynamic-routes.md) that also uses `getStaticProps`
* You **cannot** export `getStaticPaths` from non-page file (e.g. your `components` folder)
* You must export `getStaticPaths` as a standalone function, and not a property of the page component

## Runs on every request in development

In development (`next dev`), `getStaticPaths` will be called on every request.

## Generating paths on-demand

`getStaticPaths` allows you to control which pages are generated during the build instead of on-demand with [`fallback`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-blocking). Generating more pages during a build will cause slower builds.

You can defer generating all pages on-demand by returning an empty array for `paths`. This can be especially helpful when deploying your Next.js application to multiple environments. For example, you can have faster builds by generating all pages on-demand for previews (but not production builds). This is helpful for sites with hundreds/thousands of static pages.

```jsx filename="pages/posts/[id].js"
export async function getStaticPaths() {
  // When this is true (in preview environments) don't
  // prerender any static pages
  // (faster builds, but slower initial page load)
  if (process.env.SKIP_BUILD_STATIC_GENERATION) {
    return {
      paths: [],
      fallback: 'blocking',
    }
  }

  // Call an external API endpoint to get posts
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  // Get the paths we want to prerender based on posts
  // In production environments, prerender all pages
  // (slower builds, but faster initial page load)
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }))

  // { fallback: false } means other routes should 404
  return { paths, fallback: false }
}
```


--------------------------------------------------------------------------------
title: "Forms and Mutations"
description: "Learn how to handle form submissions and data mutations with Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations"
--------------------------------------------------------------------------------

# Forms and Mutations

@router: Pages Router

Forms enable you to create and update data in web applications. Next.js provides a powerful way to handle form submissions and data mutations using **API Routes**.

> **Good to know:**
>
> * We will soon recommend [incrementally adopting](/docs/app/guides/migrating/app-router-migration.md) the App Router and using [Server Actions](/docs/app/getting-started/updating-data.md) for handling form submissions and data mutations. Server Actions allow you to define asynchronous server functions that can be called directly from your components, without needing to manually create an API Route.
> * API Routes [do not specify CORS headers](https://developer.mozilla.org/docs/Web/HTTP/CORS), meaning they are same-origin only by default.
> * Since API Routes run on the server, we're able to use sensitive values (like API keys) through [Environment Variables](/docs/pages/guides/environment-variables.md) without exposing them to the client. This is critical for the security of your application.

## Examples

### Redirecting

If you would like to redirect the user to a different route after a mutation, you can [`redirect`](/docs/pages/building-your-application/routing/api-routes.md#response-helpers) to any absolute or relative URL:

```ts filename="pages/api/submit.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const id = await addPost()
  res.redirect(307, `/post/${id}`)
}
```

```js filename="pages/api/submit.js" switcher
export default async function handler(req, res) {
  const id = await addPost()
  res.redirect(307, `/post/${id}`)
}
```

### Setting cookies

You can set cookies inside an API Route using the `setHeader` method on the response:

```ts filename="pages/api/cookie.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  res.setHeader('Set-Cookie', 'username=lee; Path=/; HttpOnly')
  res.status(200).send('Cookie has been set.')
}
```

```js filename="pages/api/cookie.js" switcher
export default async function handler(req, res) {
  res.setHeader('Set-Cookie', 'username=lee; Path=/; HttpOnly')
  res.status(200).send('Cookie has been set.')
}
```

### Reading cookies

You can read cookies inside an API Route using the [`cookies`](/docs/pages/building-your-application/routing/api-routes.md#request-helpers) request helper:

```ts filename="pages/api/cookie.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const auth = req.cookies.authorization
  // ...
}
```

```js filename="pages/api/cookie.js" switcher
export default async function handler(req, res) {
  const auth = req.cookies.authorization
  // ...
}
```

### Deleting cookies

You can delete cookies inside an API Route using the `setHeader` method on the response:

```ts filename="pages/api/cookie.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  res.setHeader('Set-Cookie', 'username=; Path=/; HttpOnly; Max-Age=0')
  res.status(200).send('Cookie has been deleted.')
}
```

```js filename="pages/api/cookie.js" switcher
export default async function handler(req, res) {
  res.setHeader('Set-Cookie', 'username=; Path=/; HttpOnly; Max-Age=0')
  res.status(200).send('Cookie has been deleted.')
}
```


--------------------------------------------------------------------------------
title: "getServerSideProps"
description: "Fetch data on each request with `getServerSideProps`."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props"
--------------------------------------------------------------------------------

# getServerSideProps

@router: Pages Router

`getServerSideProps` is a Next.js function that can be used to fetch data and render the contents of a page at request time.

## Example

You can use `getServerSideProps` by exporting it from a Page Component. The example below shows how you can fetch data from a 3rd party API in `getServerSideProps`, and pass the data to the page as props:

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

## When should I use `getServerSideProps`?

You should use `getServerSideProps` if you need to render a page that relies on personalized user data, or information that can only be known at request time. For example, `authorization` headers or a geolocation.

If you do not need to fetch the data at request time, or would prefer to cache the data and pre-rendered HTML, we recommend using [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md).

## Behavior

* `getServerSideProps` runs on the server.
* `getServerSideProps` can only be exported from a **page**.
* `getServerSideProps` returns JSON.
* When a user visits a page, `getServerSideProps` will be used to fetch data at request time, and the data is used to render the initial HTML of the page.
* `props` passed to the page component can be viewed on the client as part of the initial HTML. This is to allow the page to be [hydrated](https://react.dev/reference/react-dom/hydrate) correctly. Make sure that you don't pass any sensitive information that shouldn't be available on the client in `props`.
* When a user visits the page through [`next/link`](/docs/pages/api-reference/components/link.md) or [`next/router`](/docs/pages/api-reference/functions/use-router.md), Next.js sends an API request to the server, which runs `getServerSideProps`.
* You do not have to call a Next.js [API Route](/docs/pages/building-your-application/routing/api-routes.md) to fetch data when using `getServerSideProps` since the function runs on the server. Instead, you can call a CMS, database, or other third-party APIs directly from inside `getServerSideProps`.

> **Good to know:**
>
> * See [`getServerSideProps` API reference](/docs/pages/api-reference/functions/get-server-side-props.md) for parameters and props that can be used with `getServerSideProps`.
> * You can use the [next-code-elimination tool](https://next-code-elimination.vercel.app/) to verify what Next.js eliminates from the client-side bundle.

## Error Handling

If an error is thrown inside `getServerSideProps`, it will show the `pages/500.js` file. Check out the documentation for [500 page](/docs/pages/building-your-application/routing/custom-error.md#500-page) to learn more on how to create it. During development, this file will not be used and the development error overlay will be shown instead.

## Edge Cases

### Caching with Server-Side Rendering (SSR)

You can use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using [`stale-while-revalidate`](https://web.dev/stale-while-revalidate/).

```jsx
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

However, before reaching for `cache-control`, we recommend seeing if [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) with [ISR](/docs/pages/guides/incremental-static-regeneration.md) is a better fit for your use case.


--------------------------------------------------------------------------------
title: "Client-side Fetching"
description: "Learn about client-side data fetching, and how to use SWR, a data fetching React Hook library that handles caching, revalidation, focus tracking, refetching on interval and more."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side"
--------------------------------------------------------------------------------

# Client-side Fetching

@router: Pages Router

Client-side data fetching is useful when your page doesn't require SEO indexing, when you don't need to pre-render your data, or when the content of your pages needs to update frequently. Unlike the server-side rendering APIs, you can use client-side data fetching at the component level.

If done at the page level, the data is fetched at runtime, and the content of the page is updated as the data changes. When used at the component level, the data is fetched at the time of the component mount, and the content of the component is updated as the data changes.

It's important to note that using client-side data fetching can affect the performance of your application and the load speed of your pages. This is because the data fetching is done at the time of the component or pages mount, and the data is not cached.

## Client-side data fetching with useEffect

The following example shows how you can fetch data on the client side using the useEffect hook.

```jsx
import { useState, useEffect } from 'react'

function Profile() {
  const [data, setData] = useState(null)
  const [isLoading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/profile-data')
      .then((res) => res.json())
      .then((data) => {
        setData(data)
        setLoading(false)
      })
  }, [])

  if (isLoading) return <p>Loading...</p>
  if (!data) return <p>No profile data</p>

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.bio}</p>
    </div>
  )
}
```

## Client-side data fetching with SWR

The team behind Next.js has created a React Hook library for data fetching called [**SWR**](https://swr.vercel.app/). It is **highly recommended** if you are fetching data on the client-side. It handles caching, revalidation, focus tracking, refetching on intervals, and more.

Using the same example as above, we can now use SWR to fetch the profile data. SWR will automatically cache the data for us and will revalidate the data if it becomes stale.

For more information on using SWR, check out the [SWR docs](https://swr.vercel.app/docs/getting-started).

```jsx
import useSWR from 'swr'

const fetcher = (...args) => fetch(...args).then((res) => res.json())

function Profile() {
  const { data, error } = useSWR('/api/profile-data', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.bio}</p>
    </div>
  )
}
```


--------------------------------------------------------------------------------
title: "Configuring"
description: "Learn how to configure your Next.js application."
source: "https://nextjs.org/docs/pages/building-your-application/configuring"
--------------------------------------------------------------------------------

# Configuring

@router: Pages Router

Next.js allows you to customize your project to meet specific requirements. This includes integrations with TypeScript, ESlint, and more, as well as internal configuration options such as Absolute Imports and Environment Variables.

 - [Error Handling](/docs/pages/building-your-application/configuring/error-handling.md)

--------------------------------------------------------------------------------
title: "Error Handling"
description: "Handle errors in your Next.js app."
source: "https://nextjs.org/docs/pages/building-your-application/configuring/error-handling"
--------------------------------------------------------------------------------

# Error Handling

@router: Pages Router

This documentation explains how you can handle development, server-side, and client-side errors.

## Handling Errors in Development

When there is a runtime error during the development phase of your Next.js application, you will encounter an **overlay**. It is a modal that covers the webpage. It is **only** visible when the development server runs using `next dev` via `pnpm dev`, `npm run dev`, `yarn dev`, or `bun dev` and will not be shown in production. Fixing the error will automatically dismiss the overlay.

Here is an example of an overlay:

![Example of an overlay when in development mode](https://assets.vercel.com/image/upload/v1645118290/docs-assets/static/docs/error-handling/overlay.png)

## Handling Server Errors

Next.js provides a static 500 page by default to handle server-side errors that occur in your application. You can also [customize this page](/docs/pages/building-your-application/routing/custom-error.md#customizing-the-500-page) by creating a `pages/500.js` file.

Having a 500 page in your application does not show specific errors to the app user.

You can also use [404 page](/docs/pages/building-your-application/routing/custom-error.md#404-page) to handle specific runtime error like `file not found`.

## Handling Client Errors

React [Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) is a graceful way to handle a JavaScript error on the client so that the other parts of the application continue working. In addition to preventing the page from crashing, it allows you to provide a custom fallback component and even log error information.

To use Error Boundaries for your Next.js application, you must create a class component `ErrorBoundary` and wrap the `Component` prop in the `pages/_app.js` file. This component will be responsible to:

* Render a fallback UI after an error is thrown
* Provide a way to reset the Application's state
* Log error information

You can create an `ErrorBoundary` class component by extending `React.Component`. For example:

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)

    // Define a state variable to track whether is an error or not
    this.state = { hasError: false }
  }
  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI

    return { hasError: true }
  }
  componentDidCatch(error, errorInfo) {
    // You can use your own error logging service here
    console.log({ error, errorInfo })
  }
  render() {
    // Check if the error is thrown
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return (
        <div>
          <h2>Oops, there is an error!</h2>
          <button
            type="button"
            onClick={() => this.setState({ hasError: false })}
          >
            Try again?
          </button>
        </div>
      )
    }

    // Return children components in case of no error

    return this.props.children
  }
}

export default ErrorBoundary
```

The `ErrorBoundary` component keeps track of an `hasError` state. The value of this state variable is a boolean. When the value of `hasError` is `true`, then the `ErrorBoundary` component will render a fallback UI. Otherwise, it will render the children components.

After creating an `ErrorBoundary` component, import it in the `pages/_app.js` file to wrap the `Component` prop in your Next.js application.

```jsx
// Import the ErrorBoundary component
import ErrorBoundary from '../components/ErrorBoundary'

function MyApp({ Component, pageProps }) {
  return (
    // Wrap the Component prop with ErrorBoundary component
    <ErrorBoundary>
      <Component {...pageProps} />
    </ErrorBoundary>
  )
}

export default MyApp
```

You can learn more about [Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary) in React's documentation.

### Reporting Errors

To monitor client errors, use a service like [Sentry](https://github.com/vercel/next.js/tree/canary/examples/with-sentry), Bugsnag or Datadog.



--------------------------------------------------------------------------------
title: "API Reference"
description: "Next.js API Reference for the Pages Router."
source: "https://nextjs.org/docs/pages/api-reference"
--------------------------------------------------------------------------------

# API Reference

@router: Pages Router



 - [Components](/docs/pages/api-reference/components.md)
 - [File-system conventions](/docs/pages/api-reference/file-conventions.md)
 - [Functions](/docs/pages/api-reference/functions.md)
 - [Configuration](/docs/pages/api-reference/config.md)
 - [CLI](/docs/pages/api-reference/cli.md)
 - [Edge Runtime](/docs/pages/api-reference/edge.md)
 - [Turbopack](/docs/pages/api-reference/turbopack.md)

--------------------------------------------------------------------------------
title: "Components"
description: "API Reference for Next.js built-in components."
source: "https://nextjs.org/docs/pages/api-reference/components"
--------------------------------------------------------------------------------

# Components

@router: Pages Router



 - [Font](/docs/pages/api-reference/components/font.md)
 - [Form](/docs/pages/api-reference/components/form.md)
 - [Head](/docs/pages/api-reference/components/head.md)
 - [Image](/docs/pages/api-reference/components/image.md)
 - [Image (Legacy)](/docs/pages/api-reference/components/image-legacy.md)
 - [Link](/docs/pages/api-reference/components/link.md)
 - [Script](/docs/pages/api-reference/components/script.md)

--------------------------------------------------------------------------------
title: "Font Module"
description: "Optimizing loading web fonts with the built-in `next/font` loaders."
source: "https://nextjs.org/docs/pages/api-reference/components/font"
--------------------------------------------------------------------------------

# Font

@router: Pages Router

[`next/font`](/docs/app/api-reference/components/font.md) automatically optimizes your fonts (including custom fonts) and removes external network requests for improved privacy and performance.

It includes **built-in automatic self-hosting** for any font file. This means you can optimally load web fonts with no [layout shift](https://web.dev/articles/cls).

You can also conveniently use all [Google Fonts](https://fonts.google.com/). CSS and font files are downloaded at build time and self-hosted with the rest of your static assets. **No requests are sent to Google by the browser.**

To use the font in all your pages, add it to [`_app.js` file](/docs/pages/building-your-application/routing/custom-app.md) under `/pages` as shown below:

```jsx filename="pages/_app.js"
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

> **🎥 Watch:** Learn more about using `next/font` → [YouTube (6 minutes)](https://www.youtube.com/watch?v=L8_98i_bMMA).

## Reference

| Key                                         | `font/google`       | `font/local`        | Type                       | Required          |
| ------------------------------------------- | ------------------- | ------------------- | -------------------------- | ----------------- |
| [`src`](#src)                               |  |  | String or Array of Objects | Yes               |
| [`weight`](#weight)                         |  |  | String or Array            | Required/Optional |
| [`style`](#style)                           |  |  | String or Array            | -                 |
| [`subsets`](#subsets)                       |  |  | Array of Strings           | -                 |
| [`axes`](#axes)                             |  |  | Array of Strings           | -                 |
| [`display`](#display)                       |  |  | String                     | -                 |
| [`preload`](#preload)                       |  |  | Boolean                    | -                 |
| [`fallback`](#fallback)                     |  |  | Array of Strings           | -                 |
| [`adjustFontFallback`](#adjustfontfallback) |  |  | Boolean or String          | -                 |
| [`variable`](#variable)                     |  |  | String                     | -                 |
| [`declarations`](#declarations)             |  |  | Array of Objects           | -                 |

### `src`

The path of the font file as a string or an array of objects (with type `Array<{path: string, weight?: string, style?: string}>`) relative to the directory where the font loader function is called.

Used in `next/font/local`

* Required

Examples:

* `src:'./fonts/my-font.woff2'` where `my-font.woff2` is placed in a directory named `fonts` inside the `app` directory
* `src:[{path: './inter/Inter-Thin.ttf', weight: '100',},{path: './inter/Inter-Regular.ttf',weight: '400',},{path: './inter/Inter-Bold-Italic.ttf', weight: '700',style: 'italic',},]`
* if the font loader function is called in `app/page.tsx` using `src:'../styles/fonts/my-font.ttf'`, then `my-font.ttf` is placed in `styles/fonts` at the root of the project

### `weight`

The font [`weight`](https://fonts.google.com/knowledge/glossary/weight) with the following possibilities:

* A string with possible values of the weights available for the specific font or a range of values if it's a [variable](https://fonts.google.com/variablefonts) font
* An array of weight values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Required if the font being used is **not** [variable](https://fonts.google.com/variablefonts)

Examples:

* `weight: '400'`: A string for a single weight value - for the font [`Inter`](https://fonts.google.com/specimen/Inter?query=inter), the possible values are `'100'`, `'200'`, `'300'`, `'400'`, `'500'`, `'600'`, `'700'`, `'800'`, `'900'` or `'variable'` where `'variable'` is the default)
* `weight: '100 900'`: A string for the range between `100` and `900` for a variable font
* `weight: ['100','400','900']`: An array of 3 possible values for a non variable font

### `style`

The font [`style`](https://developer.mozilla.org/docs/Web/CSS/font-style) with the following possibilities:

* A string [value](https://developer.mozilla.org/docs/Web/CSS/font-style#values) with default value of `'normal'`
* An array of style values if the font is not a [variable google font](https://fonts.google.com/variablefonts). It applies to `next/font/google` only.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `style: 'italic'`: A string - it can be `normal` or `italic` for `next/font/google`
* `style: 'oblique'`: A string - it can take any value for `next/font/local` but is expected to come from [standard font styles](https://developer.mozilla.org/docs/Web/CSS/font-style)
* `style: ['italic','normal']`: An array of 2 values for `next/font/google` - the values are from `normal` and `italic`

### `subsets`

The font [`subsets`](https://fonts.google.com/knowledge/glossary/subsetting) defined by an array of string values with the names of each subset you would like to be [preloaded](/docs/app/api-reference/components/font.md#specifying-a-subset). Fonts specified via `subsets` will have a link preload tag injected into the head when the [`preload`](#preload) option is true, which is the default.

Used in `next/font/google`

* Optional

Examples:

* `subsets: ['latin']`: An array with the subset `latin`

You can find a list of all subsets on the Google Fonts page for your font.

### `axes`

Some variable fonts have extra `axes` that can be included. By default, only the font weight is included to keep the file size down. The possible values of `axes` depend on the specific font.

Used in `next/font/google`

* Optional

Examples:

* `axes: ['slnt']`: An array with value `slnt` for the `Inter` variable font which has `slnt` as additional `axes` as shown [here](https://fonts.google.com/variablefonts?vfquery=inter#font-families). You can find the possible `axes` values for your font by using the filter on the [Google variable fonts page](https://fonts.google.com/variablefonts#font-families) and looking for axes other than `wght`

### `display`

The font [`display`](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display) with possible string [values](https://developer.mozilla.org/docs/Web/CSS/@font-face/font-display#values) of `'auto'`, `'block'`, `'swap'`, `'fallback'` or `'optional'` with default value of `'swap'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `display: 'optional'`: A string assigned to the `optional` value

### `preload`

A boolean value that specifies whether the font should be [preloaded](/docs/app/api-reference/components/font.md#preloading) or not. The default is `true`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `preload: false`

### `fallback`

The fallback font to use if the font cannot be loaded. An array of strings of fallback fonts with no default.

* Optional

Used in `next/font/google` and `next/font/local`

Examples:

* `fallback: ['system-ui', 'arial']`: An array setting the fallback fonts to `system-ui` or `arial`

### `adjustFontFallback`

* For `next/font/google`: A boolean value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The default is `true`.
* For `next/font/local`: A string or boolean `false` value that sets whether an automatic fallback font should be used to reduce [Cumulative Layout Shift](https://web.dev/cls/). The possible values are `'Arial'`, `'Times New Roman'` or `false`. The default is `'Arial'`.

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `adjustFontFallback: false`: for `next/font/google`
* `adjustFontFallback: 'Times New Roman'`: for `next/font/local`

### `variable`

A string value to define the CSS variable name to be used if the style is applied with the [CSS variable method](#css-variables).

Used in `next/font/google` and `next/font/local`

* Optional

Examples:

* `variable: '--my-font'`: The CSS variable `--my-font` is declared

### `declarations`

An array of font face [descriptor](https://developer.mozilla.org/docs/Web/CSS/@font-face#descriptors) key-value pairs that define the generated `@font-face` further.

Used in `next/font/local`

* Optional

Examples:

* `declarations: [{ prop: 'ascent-override', value: '90%' }]`

## Examples

## Google Fonts

To use a Google font, import it from `next/font/google` as a function. We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility.

To use the font in all your pages, add it to [`_app.js` file](/docs/pages/building-your-application/routing/custom-app.md) under `/pages` as shown below:

```jsx filename="pages/_app.js"
import { Inter } from 'next/font/google'

// If loading a variable font, you don't need to specify the font weight
const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you can't use a variable font, you will **need to specify a weight**:

```jsx filename="pages/_app.js"
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={roboto.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

You can specify multiple weights and/or styles by using an array:

```jsx filename="app/layout.js"
const roboto = Roboto({
  weight: ['400', '700'],
  style: ['normal', 'italic'],
  subsets: ['latin'],
  display: 'swap',
})
```

> **Good to know**: Use an underscore (\_) for font names with multiple words. E.g. `Roboto Mono` should be imported as `Roboto_Mono`.

### Apply the font in `<head>`

You can also use the font without a wrapper and `className` by injecting it inside the `<head>` as follows:

```jsx filename="pages/_app.js"
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <style jsx global>{`
        html {
          font-family: ${inter.style.fontFamily};
        }
      `}</style>
      <Component {...pageProps} />
    </>
  )
}
```

### Single page usage

To use the font on a single page, add it to the specific page as shown below:

```jsx filename="pages/index.js"
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <div className={inter.className}>
      <p>Hello World</p>
    </div>
  )
}
```

### Specifying a subset

Google Fonts are automatically [subset](https://fonts.google.com/knowledge/glossary/subsetting). This reduces the size of the font file and improves performance. You'll need to define which of these subsets you want to preload. Failing to specify any subsets while [`preload`](/docs/app/api-reference/components/font.md#preload) is `true` will result in a warning.

This can be done by adding it to the function call:

```jsx filename="pages/_app.js"
const inter = Inter({ subsets: ['latin'] })
```

View the [Font API Reference](/docs/app/api-reference/components/font.md) for more information.

## Using Multiple Fonts

You can import and use multiple fonts in your application. There are two approaches you can take.

The first approach is to create a utility function that exports a font, imports it, and applies its `className` where needed. This ensures the font is preloaded only when it's rendered:

```ts filename="app/fonts.ts" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
})
```

```js filename="app/fonts.js" switcher
import { Inter, Roboto_Mono } from 'next/font/google'

export const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
})

export const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
})
```

In the example above, `Inter` will be applied globally, and `Roboto Mono` can be imported and applied as needed.

Alternatively, you can create a [CSS variable](/docs/app/api-reference/components/font.md#variable) and use it with your preferred CSS solution:

```css filename="app/global.css"
html {
  font-family: var(--font-inter);
}

h1 {
  font-family: var(--font-roboto-mono);
}
```

In the example above, `Inter` will be applied globally, and any `<h1>` tags will be styled with `Roboto Mono`.

> **Recommendation**: Use multiple fonts conservatively since each new font is an additional resource the client has to download.

### Local Fonts

Import `next/font/local` and specify the `src` of your local font file. We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility.

```jsx filename="pages/_app.js"
import localFont from 'next/font/local'

// Font files can be colocated inside of `pages`
const myFont = localFont({ src: './my-font.woff2' })

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
```

If you want to use multiple files for a single font family, `src` can be an array:

```js
const roboto = localFont({
  src: [
    {
      path: './Roboto-Regular.woff2',
      weight: '400',
      style: 'normal',
    },
    {
      path: './Roboto-Italic.woff2',
      weight: '400',
      style: 'italic',
    },
    {
      path: './Roboto-Bold.woff2',
      weight: '700',
      style: 'normal',
    },
    {
      path: './Roboto-BoldItalic.woff2',
      weight: '700',
      style: 'italic',
    },
  ],
})
```

View the [Font API Reference](/docs/app/api-reference/components/font.md) for more information.

### With Tailwind CSS

`next/font` integrates seamlessly with [Tailwind CSS](https://tailwindcss.com/) using [CSS variables](/docs/app/api-reference/components/font.md#css-variables).

In the example below, we use the `Inter` and `Roboto_Mono` fonts from `next/font/google` (you can use any Google Font or Local Font). Use the `variable` option to define a CSS variable name, such as `inter` and `roboto_mono` for these fonts, respectively. Then, apply `inter.variable` and `roboto_mono.variable` to include the CSS variables in your HTML document.

> **Good to know**: You can add these variables to the `<html>` or `<body>` tag, depending on your preference, styling needs or project requirements.

```jsx filename="pages/_app.js"
import { Inter } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
})

const roboto_mono = Roboto_Mono({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-roboto-mono',
})

export default function MyApp({ Component, pageProps }) {
  return (
    <main className={`${inter.variable} ${roboto_mono.variable} font-sans`}>
      <Component {...pageProps} />
    </main>
  )
}
```

Finally, add the CSS variable to your [Tailwind CSS config](/docs/app/getting-started/css.md#tailwind-css):

```css filename="global.css"
@import 'tailwindcss';

@theme inline {
  --font-sans: var(--font-inter);
  --font-mono: var(--font-roboto-mono);
}
```

### Tailwind CSS v3

```js filename="tailwind.config.js"
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        mono: ['var(--font-roboto-mono)'],
      },
    },
  },
  plugins: [],
}
```

You can now use the `font-sans` and `font-mono` utility classes to apply the font to your elements.

```html
<p class="font-sans ...">The quick brown fox ...</p>
<p class="font-mono ...">The quick brown fox ...</p>
```

### Applying Styles

You can apply the font styles in three ways:

* [`className`](#classname)
* [`style`](#style-1)
* [CSS Variables](#css-variables)

#### `className`

Returns a read-only CSS `className` for the loaded font to be passed to an HTML element.

```tsx
<p className={inter.className}>Hello, Next.js!</p>
```

#### `style`

Returns a read-only CSS `style` object for the loaded font to be passed to an HTML element, including `style.fontFamily` to access the font family name and fallback fonts.

```tsx
<p style={inter.style}>Hello World</p>
```

#### CSS Variables

If you would like to set your styles in an external style sheet and specify additional options there, use the CSS variable method.

In addition to importing the font, also import the CSS file where the CSS variable is defined and set the variable option of the font loader object as follows:

```tsx filename="app/page.tsx" switcher
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
  variable: '--font-inter',
})
```

```jsx filename="app/page.js" switcher
import { Inter } from 'next/font/google'
import styles from '../styles/component.module.css'

const inter = Inter({
  variable: '--font-inter',
})
```

To use the font, set the `className` of the parent container of the text you would like to style to the font loader's `variable` value and the `className` of the text to the `styles` property from the external CSS file.

```tsx filename="app/page.tsx" switcher
<main className={inter.variable}>
  <p className={styles.text}>Hello World</p>
</main>
```

```jsx filename="app/page.js" switcher
<main className={inter.variable}>
  <p className={styles.text}>Hello World</p>
</main>
```

Define the `text` selector class in the `component.module.css` CSS file as follows:

```css filename="styles/component.module.css"
.text {
  font-family: var(--font-inter);
  font-weight: 200;
  font-style: italic;
}
```

In the example above, the text `Hello World` is styled using the `Inter` font and the generated font fallback with `font-weight: 200` and `font-style: italic`.

### Using a font definitions file

Every time you call the `localFont` or Google font function, that font will be hosted as one instance in your application. Therefore, if you need to use the same font in multiple places, you should load it in one place and import the related font object where you need it. This is done using a font definitions file.

For example, create a `fonts.ts` file in a `styles` folder at the root of your app directory.

Then, specify your font definitions as follows:

```ts filename="styles/fonts.ts" switcher
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non-variable font
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

```js filename="styles/fonts.js" switcher
import { Inter, Lora, Source_Sans_3 } from 'next/font/google'
import localFont from 'next/font/local'

// define your variable fonts
const inter = Inter()
const lora = Lora()
// define 2 weights of a non-variable font
const sourceCodePro400 = Source_Sans_3({ weight: '400' })
const sourceCodePro700 = Source_Sans_3({ weight: '700' })
// define a custom local font where GreatVibes-Regular.ttf is stored in the styles folder
const greatVibes = localFont({ src: './GreatVibes-Regular.ttf' })

export { inter, lora, sourceCodePro400, sourceCodePro700, greatVibes }
```

You can now use these definitions in your code as follows:

```tsx filename="app/page.tsx" switcher
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
  return (
    <div>
      <p className={inter.className}>Hello world using Inter font</p>
      <p style={lora.style}>Hello world using Lora font</p>
      <p className={sourceCodePro700.className}>
        Hello world using Source_Sans_3 font with weight 700
      </p>
      <p className={greatVibes.className}>My title in Great Vibes font</p>
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
import { inter, lora, sourceCodePro700, greatVibes } from '../styles/fonts'

export default function Page() {
  return (
    <div>
      <p className={inter.className}>Hello world using Inter font</p>
      <p style={lora.style}>Hello world using Lora font</p>
      <p className={sourceCodePro700.className}>
        Hello world using Source_Sans_3 font with weight 700
      </p>
      <p className={greatVibes.className}>My title in Great Vibes font</p>
    </div>
  )
}
```

To make it easier to access the font definitions in your code, you can define a path alias in your `tsconfig.json` or `jsconfig.json` files as follows:

```json filename="tsconfig.json"
{
  "compilerOptions": {
    "paths": {
      "@/fonts": ["./styles/fonts"]
    }
  }
}
```

You can now import any font definition as follows:

```tsx filename="app/about/page.tsx" switcher
import { greatVibes, sourceCodePro400 } from '@/fonts'
```

```jsx filename="app/about/page.js" switcher
import { greatVibes, sourceCodePro400 } from '@/fonts'
```

### Preloading

When a font function is called on a page of your site, it is not globally available and preloaded on all routes. Rather, the font is only preloaded on the related route/s based on the type of file where it is used:

* if it's a [unique page](/docs/pages/building-your-application/routing/pages-and-layouts.md), it is preloaded on the unique route for that page
* if it's in the [custom App](/docs/pages/building-your-application/routing/custom-app.md), it is preloaded on all the routes of the site under `/pages`

## Version Changes

| Version   | Changes                                                               |
| --------- | --------------------------------------------------------------------- |
| `v13.2.0` | `@next/font` renamed to `next/font`. Installation no longer required. |
| `v13.0.0` | `@next/font` was added.                                               |


--------------------------------------------------------------------------------
title: "Form Component"
description: "Learn how to use the `<Form>` component to handle form submissions and search params updates with client-side navigation."
source: "https://nextjs.org/docs/pages/api-reference/components/form"
--------------------------------------------------------------------------------

# Form

@router: Pages Router

The `<Form>` component extends the HTML `<form>` element to provide  **client-side navigation** on submission, and **progressive enhancement**.

It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.

Basic usage:

```tsx filename="/ui/search.js" switcher
import Form from 'next/form'

export default function Page() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

```jsx filename="/ui/search.js" switcher
import Form from 'next/form'

export default function Search() {
  return (
    <Form action="/search">
      {/* On submission, the input value will be appended to
          the URL, e.g. /search?query=abc */}
      <input name="query" />
      <button type="submit">Submit</button>
    </Form>
  )
}
```

## Reference

The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.

* When `action` is a **string**, the `<Form>` behaves like a native HTML form that uses a **`GET`** method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
  * Performs a [client-side navigation](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions) instead of a full page reload when the form is submitted. This retains shared UI and client-side state.

### `action` (string) Props

When `action` is a string, the `<Form>` component supports the following props:

| Prop      | Example            | Type                            | Required |
| --------- | ------------------ | ------------------------------- | -------- |
| `action`  | `action="/search"` | `string` (URL or relative path) | Yes      |
| `replace` | `replace={false}`  | `boolean`                       | -        |
| `scroll`  | `scroll={true}`    | `boolean`                       | -        |

* **`action`**: The URL or path to navigate to when the form is submitted.
  * An empty string `""` will navigate to the same route with updated search params.
* **`replace`**: Replaces the current history state instead of pushing a new one to the [browser's history](https://developer.mozilla.org/en-US/docs/Web/API/History_API) stack. Default is `false`.
* **`scroll`**: Controls the scroll behavior during navigation. Defaults to `true`, this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.

### Caveats

* **`onSubmit`**: Can be used to handle form submission logic. However, calling `event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
* **[`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#method), [`encType`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#enctype), [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#target)**: Are not supported as they override `<Form>` behavior.
  * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
  * If you need to use these props, use the HTML `<form>` element instead.
* **`<input type="file">`**: Using this input type when the `action` is a string will match browser behavior by submitting the filename instead of the file object.


--------------------------------------------------------------------------------
title: "Head"
description: "Add custom elements to the `head` of your page with the built-in Head component."
source: "https://nextjs.org/docs/pages/api-reference/components/head"
--------------------------------------------------------------------------------

# Head

@router: Pages Router

We expose a built-in component for appending elements to the `head` of the page:

```jsx
import Head from 'next/head'

function IndexPage() {
  return (
    <div>
      <Head>
        <title>My page title</title>
      </Head>
      <p>Hello world!</p>
    </div>
  )
}

export default IndexPage
```

## Avoid duplicated tags

To avoid duplicate tags in your `head` you can use the `key` property, which will make sure the tag is only rendered once, as in the following example:

```jsx
import Head from 'next/head'

function IndexPage() {
  return (
    <div>
      <Head>
        <title>My page title</title>
        <meta property="og:title" content="My page title" key="title" />
      </Head>
      <Head>
        <meta property="og:title" content="My new title" key="title" />
      </Head>
      <p>Hello world!</p>
    </div>
  )
}

export default IndexPage
```

In this case only the second `<meta property="og:title" />` is rendered. `meta` tags with duplicate `key` attributes are automatically handled.

> **Good to know**: `<title>` and `<base>` tags are automatically checked for duplicates by Next.js, so using key is not necessary for these tags.

> The contents of `head` get cleared upon unmounting the component, so make sure each page completely defines what it needs in `head`, without making assumptions about what other pages added.

## Use minimal nesting

`title`, `meta` or any other elements (e.g. `script`) need to be contained as **direct** children of the `Head` element,
or wrapped into maximum one level of `<React.Fragment>` or arrays—otherwise the tags won't be correctly picked up on client-side navigations.

## Use `next/script` for scripts

We recommend using [`next/script`](/docs/pages/guides/scripts.md) in your component instead of manually creating a `<script>` in `next/head`.

## No `html` or `body` tags

You **cannot** use `<Head>` to set attributes on `<html>` or `<body>` tags. This will result in an `next-head-count is missing` error. `next/head` can only handle tags inside the HTML `<head>` tag.


--------------------------------------------------------------------------------
title: "Image Component"
description: "Optimize Images in your Next.js Application using the built-in `next/image` Component."
source: "https://nextjs.org/docs/pages/api-reference/components/image"
--------------------------------------------------------------------------------

# Image

@router: Pages Router

The Next.js Image component extends the HTML `<img>` element for automatic image optimization.

```jsx filename="app/page.js"
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/profile.png"
      width={500}
      height={500}
      alt="Picture of the author"
    />
  )
}
```

> **Good to know**: If you are using a version of Next.js prior to 13, you'll want to use the [next/legacy/image](/docs/pages/api-reference/components/image-legacy.md) documentation since the component was renamed.

## Reference

### Props

The following props are available:

#### `src`

The source of the image. Can be one of the following:

An internal path string.

```jsx
<Image src="/profile.png" />
```

An absolute external URL (must be configured with [remotePatterns](#remotepatterns)).

```jsx
<Image src="https://example.com/profile.png" />
```

A static import.

```jsx
import profile from './profile.png'

export default function Page() {
  return <Image src={profile} />
}
```

> **Good to know**: For security reasons, the Image Optimization API using the default [loader](#loader) will *not* forward headers when fetching the `src` image.
> If the `src` image requires authentication, consider using the [unoptimized](#unoptimized) property to disable Image Optimization.

#### `alt`

The `alt` property is used to describe the image for screen readers and search engines. It is also the fallback text if images have been disabled or an error occurs while loading the image.

It should contain text that could replace the image [without changing the meaning of the page](https://html.spec.whatwg.org/multipage/images.html#general-guidelines). It is not meant to supplement the image and should not repeat information that is already provided in the captions above or below the image.

If the image is [purely decorative](https://html.spec.whatwg.org/multipage/images.html#a-purely-decorative-image-that-doesn't-add-any-information) or [not intended for the user](https://html.spec.whatwg.org/multipage/images.html#an-image-not-intended-for-the-user), the `alt` property should be an empty string (`alt=""`).

> Learn more about [image accessibility guidelines](https://html.spec.whatwg.org/multipage/images.html#alt).

#### `width` and `height`

The `width` and `height` properties represent the [intrinsic](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size) image size in pixels. This property is used to infer the correct **aspect ratio** used by browsers to reserve space for the image and avoid layout shift during loading. It does not determine the *rendered size* of the image, which is controlled by CSS.

```jsx
<Image src="/profile.png" width={500} height={500} />
```

You **must** set both `width` and `height` properties unless:

* The image is statically imported.
* The image has the [`fill` property](#fill)

If the height and width are unknown, we recommend using the [`fill` property](#fill).

#### `fill`

A boolean that causes the image to expand to the size of the parent element.

```js
<Image src="/profile.png" fill={true} />
```

**Positioning**:

* The parent element **must** assign `position: "relative"`, `"fixed"`, `"absolute"`.
* By default, the `<img>` element uses `position: "absolute"`.

**Object Fit**:

If no styles are applied to the image, the image will stretch to fit the container. You can use `objectFit` to control cropping and scaling.

* `"contain"`: The image will be scaled down to fit the container and preserve aspect ratio.
* `"cover"`: The image will fill the container and be cropped.

> Learn more about [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position) and [`object-fit`](https://developer.mozilla.org/docs/Web/CSS/object-fit).

#### `loader`

A custom function used to generate the image URL. The function receives the following parameters, and returns a URL string for the image:

* [`src`](#src)
* [`width`](#width-and-height)
* [`quality`](#quality)

```js
import Image from 'next/image'

const imageLoader = ({ src, width, quality }) => {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}

export default function Page() {
  return (
    <Image
      loader={imageLoader}
      src="me.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

Alternatively, you can use the [loaderFile](#loaderfile) configuration in `next.config.js` to configure every instance of `next/image` in your application, without passing a prop.

#### `sizes`

Define the sizes of the image at different breakpoints. Used by the browser to choose the most appropriate size from the generated `srcset`.

```jsx
import Image from 'next/image'

export default function Page() {
  return (
    <div className="grid-element">
      <Image
        fill
        src="/example.png"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
      />
    </div>
  )
}
```

`sizes` should be used when:

* The image is using the [`fill`](#fill) prop
* CSS is used to make the image responsive

If `sizes` is missing, the browser assumes the image will be as wide as the viewport (`100vw`). This can cause unnecessarily large images to be downloaded.

In addition, `sizes` affects how `srcset` is generated:

* Without `sizes`: Next.js generates a limited `srcset` (e.g. 1x, 2x), suitable for fixed-size images.
* With `sizes`: Next.js generates a full `srcset` (e.g. 640w, 750w, etc.), optimized for responsive layouts.

> Learn more about `srcset` and `sizes` on [web.dev](https://web.dev/learn/design/responsive-images/#sizes) and [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#sizes).

#### `quality`

An integer between `1` and `100` that sets the quality of the optimized image. Higher values increase file size and visual fidelity. Lower values reduce file size but may affect sharpness.

```jsx
// Default quality is 75
<Image quality={75} />
```

If you’ve configured [qualities](#qualities) in `next.config.js`, the value must match one of the allowed entries.

> **Good to know**: If the original image is already low quality, setting a high quality value will increase the file size without improving appearance.

#### `style`

Allows passing CSS styles to the underlying image element.

```jsx
const imageStyle = {
  borderRadius: '50%',
  border: '1px solid #fff',
  width: '100px',
  height: 'auto',
}

export default function ProfileImage() {
  return <Image src="..." style={imageStyle} />
}
```

> **Good to know**: If you’re using the `style` prop to set a custom width, be sure to also set `height: 'auto'` to preserve the image’s aspect ratio.

#### `preload`

A boolean that indicates if the image should be preloaded.

```jsx
// Default preload is false
<Image preload={false} />
```

* `true`: [Preloads](https://web.dev/preload-responsive-images/) the image by inserting a `<link>` in the `<head>`.
* `false`: Does not preload the image.

**When to use it:**

* The image is the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element.
* The image is above the fold, typically the hero image.
* You want to begin loading the image in the `<head>`, before its discovered later in the `<body>`.

**When not to use it:**

* When you have multiple images that could be considered the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element depending on the viewport.
* When the `loading` property is used.
* When the `fetchPriority` property is used.

In most cases, you should use `loading="eager"` or `fetchPriority="high"` instead of `preload`.

#### `priority`

Starting with Next.js 16, the `priority` property has been deprecated in favor of the [`preload`](#preload) property in order to make the behavior clear.

#### `loading`

Controls when the image should start loading.

```jsx
// Defaults to lazy
<Image loading="lazy" />
```

* `lazy`: Defer loading the image until it reaches a calculated distance from the viewport.
* `eager`: Load the image immediately, regardless of its position in the page.

Use `eager` only when you want to ensure the image is loaded immediately.

> Learn more about the [`loading` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#loading).

#### `placeholder`

Specifies a placeholder to use while the image is loading, improving the perceived loading performance.

```jsx
// defaults to empty
<Image placeholder="empty" />
```

* `empty`: No placeholder while the image is loading.
* `blur`: Use a blurred version of the image as a placeholder. Must be used with the [`blurDataURL`](#blurdataurl) property.
* `data:image/...`: Uses the [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) as the placeholder.

**Examples:**

* [`blur` placeholder](https://image-component.nextjs.gallery/placeholder)
* [Shimmer effect with data URL `placeholder` prop](https://image-component.nextjs.gallery/shimmer)
* [Color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

> Learn more about the [`placeholder` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#placeholder).

#### `blurDataURL`

A [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) to
be used as a placeholder image before the image successfully loads. Can be automatically set or used with the [`placeholder="blur"`](#placeholder) property.

```jsx
<Image placeholder="blur" blurDataURL="..." />
```

The image is automatically enlarged and blurred, so a very small image (10px or less) is recommended.

**Automatic**

If `src` is a static import of a `jpg`, `png`, `webp`, or `avif` file, `blurDataURL` is added automatically—unless the image is animated.

**Manually set**

If the image is dynamic or remote, you must provide `blurDataURL` yourself. To generate one, you can use:

* [A online tool like png-pixel.com](https://png-pixel.com)
* [A library like Plaiceholder](https://github.com/joe-bell/plaiceholder)

A large blurDataURL may hurt performance. Keep it small and simple.

**Examples:**

* [Default `blurDataURL` prop](https://image-component.nextjs.gallery/placeholder)
* [Color effect with `blurDataURL` prop](https://image-component.nextjs.gallery/color)

#### `onLoad`

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

```jsx
<Image onLoad={(e) => console.log(e.target.naturalWidth)} />
```

The callback function will be called with one argument, the event which has a `target` that references the underlying `<img>` element.

#### `onError`

A callback function that is invoked if the image fails to load.

```jsx
<Image onError={(e) => console.error(e.target.id)} />
```

#### `unoptimized`

A boolean that indicates if the image should be optimized. This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).

```js
import Image from 'next/image'

const UnoptimizedImage = (props) => {
  // Default is false
  return <Image {...props} unoptimized />
}
```

* `true`: The source image will be served as-is from the `src` instead of changing quality, size, or format.
* `false`: The source image will be optimized.

Since Next.js 12.3.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:

```js filename="next.config.js"
module.exports = {
  images: {
    unoptimized: true,
  },
}
```

#### `overrideSrc`

When providing the `src` prop to the `<Image>` component, both the `srcset` and `src` attributes are generated automatically for the resulting `<img>`.

```jsx filename="input.js"
<Image src="/profile.jpg" />
```

```html filename="output.html"
<img
  srcset="
    /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
    /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
  "
  src="/_next/image?url=%2Fprofile.jpg&w=828&q=75"
/>
```

In some cases, it is not desirable to have the `src` attribute generated and you may wish to override it using the `overrideSrc` prop.

For example, when upgrading an existing website from `<img>` to `<Image>`, you may wish to maintain the same `src` attribute for SEO purposes such as image ranking or avoiding recrawl.

```jsx filename="input.js"
<Image src="/profile.jpg" overrideSrc="/override.jpg" />
```

```html filename="output.html"
<img
  srcset="
    /_next/image?url=%2Fprofile.jpg&w=640&q=75 1x,
    /_next/image?url=%2Fprofile.jpg&w=828&q=75 2x
  "
  src="/override.jpg"
/>
```

#### `decoding`

A hint to the browser indicating if it should wait for the image to be decoded before presenting other content updates or not.

```jsx
// Default is async
<Image decoding="async" />
```

* `async`: Asynchronously decode the image and allow other content to be rendered before it completes.
* `sync`: Synchronously decode the image for atomic presentation with other content.
* `auto`: No preference. The browser chooses the best approach.

> Learn more about the [`decoding` attribute](https://developer.mozilla.org/docs/Web/HTML/Element/img#decoding).

### Other Props

Other properties on the `<Image />` component will be passed to the underlying `img` element with the exception of the following:

* `srcSet`: Use [Device Sizes](#devicesizes) instead.

### Deprecated props

#### `onLoadingComplete`

> **Warning**: Deprecated in Next.js 14, use [`onLoad`](#onload) instead.

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

The callback function will be called with one argument, a reference to the underlying `<img>` element.

```jsx
<Image onLoadingComplete={(img) => console.log(img.naturalWidth)} />
```

### Configuration options

You can configure the Image Component in `next.config.js`. The following options are available:

#### `localPatterns`

Use `localPatterns` in your `next.config.js` file to allow images from specific local paths to be optimized and block all others.

```js filename="next.config.js"
module.exports = {
  images: {
    localPatterns: [
      {
        pathname: '/assets/images/**',
        search: '',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `/assets/images/` and must not have a query string. Attempting to optimize any other path will respond with `400` Bad Request error.

> **Good to know**: Omitting the `search` property allows all search parameters which could allow malicious actors to optimize URLs you did not intend. Try using a specific value like `search: '?v=2'` to ensure an exact match.

#### `remotePatterns`

Use `remotePatterns` in your `next.config.js` file to allow images from specific external paths and block all others. This ensures that only external images from your account can be served.

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [new URL('https://example.com/account123/**')],
  },
}
```

You can also configure `remotePatterns` using the object:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '/account123/**',
        search: '',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `https://example.com/account123/` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with `400` Bad Request.

**Wildcard Patterns:**

Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:

* `*` match a single path segment or subdomain
* `**` match any number of path segments at the end or subdomains at the beginning. This syntax does not work in the middle of the pattern.

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
        port: '',
        search: '',
      },
    ],
  },
}
```

This allows subdomains like `image.example.com`. Query strings and custom ports are still blocked.

> **Good to know**: When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.

**Query Strings**:

You can also restrict query strings using the `search` property:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'assets.example.com',
        search: '?v=1727111025337',
      },
    ],
  },
}
```

The example above will ensure the `src` property of `next/image` must start with `https://assets.example.com` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with `400` Bad Request.

#### `loaderFile`

`loaderFiles` allows you to use a custom image optimization service instead of Next.js.

```js filename="next.config.js"
module.exports = {
  images: {
    loader: 'custom',
    loaderFile: './my/image/loader.js',
  },
}
```

The path must be relative to the project root. The file must export a default function that returns a URL string:

```js filename="my/image/loader.js"
export default function myImageLoader({ src, width, quality }) {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}
```

**Example:**

* [Custom Image Loader Configuration](/docs/app/api-reference/config/next-config-js/images.md#example-loader-configuration)

> Alternatively, you can use the [`loader` prop](#loader) to configure each instance of `next/image`.

#### `path`

If you want to change or prefix the default path for the Image Optimization API, you can do so with the `path` property. The default value for `path` is `/_next/image`.

```js filename="next.config.js"
module.exports = {
  images: {
    path: '/my-prefix/_next/image',
  },
}
```

#### `deviceSizes`

`deviceSizes` allows you to specify a list of device width breakpoints. These widths are used when the `next/image` component uses [`sizes`](#sizes) prop to ensure the correct image is served for the user's device.

If no configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },
}
```

#### `imageSizes`

`imageSizes` allows you to specify a list of image widths. These widths are concatenated with the array of [device sizes](#devicesizes) to form the full array of sizes used to generate image [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset).

If no configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    imageSizes: [32, 48, 64, 96, 128, 256, 384],
  },
}
```

`imageSizes` is only used for images which provide a [`sizes`](#sizes) prop, which indicates that the image is less than the full width of the screen. Therefore, the sizes in `imageSizes` should all be smaller than the smallest size in `deviceSizes`.

#### `qualities`

`qualities` allows you to specify a list of image quality values.

If not configuration is provided, the default below is used:

```js filename="next.config.js"
module.exports = {
  images: {
    qualities: [75],
  },
}
```

> **Good to know**: This field is required starting with Next.js 16 because unrestricted access could allow malicious actors to optimize more qualities than you intended.

You can add more image qualities to the allowlist, such as the following:

```js filename="next.config.js"
module.exports = {
  images: {
    qualities: [25, 50, 75, 100],
  },
}
```

In the example above, only four qualities are allowed: 25, 50, 75, and 100.

If the [`quality`](#quality) prop does not match a value in this array, the closest allowed value will be used.

If the REST API is visited directly with a quality that does not match a value in this array, the server will return a 400 Bad Request response.

#### `formats`

`formats` allows you to specify a list of image formats to be used.

```js filename="next.config.js"
module.exports = {
  images: {
    // Default
    formats: ['image/webp'],
  },
}
```

Next.js automatically detects the browser's supported image formats via the request's `Accept` header in order to determine the best output format.

If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is animated), it will use the original image's format.

You can enable AVIF support, which will fallback to the original format of the src image if the browser [does not support AVIF](https://caniuse.com/avif):

```js filename="next.config.js"
module.exports = {
  images: {
    formats: ['image/avif'],
  },
}
```

> **Good to know**:
>
> * We still recommend using WebP for most use cases.
> * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower, but subsequent requests that are cached will be faster.
> * If you self-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.

#### `minimumCacheTTL`

`minimumCacheTTL` allows you to configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a [Static Image Import](/docs/app/getting-started/images.md#local-images) which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 14400, // 4 hours
  },
}
```

You can increase the TTL to reduce the number of revalidations and potentially lower cost:

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 2678400, // 31 days
  },
}
```

The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.

If you need to change the caching behavior per image, you can configure [`headers`](/docs/app/api-reference/config/next-config-js/headers.md) to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).

There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the [`src`](#src) prop or delete the cached file `<distDir>/cache/images`.

#### `disableStaticImages`

`disableStaticImages` allows you to disable static image imports.

The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property. In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.

You can disable static image imports inside your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  images: {
    disableStaticImages: true,
  },
}
```

#### `maximumRedirects`

The default image optimization loader will follow HTTP redirects when fetching remote images up to 3 times.

```js filename="next.config.js"
module.exports = {
  images: {
    maximumRedirects: 3,
  },
}
```

You can configure the number of redirects to follow when fetching remote images. Setting the value to `0` will disable following redirects.

```js filename="next.config.js"
module.exports = {
  images: {
    maximumRedirects: 0,
  },
}
```

#### `dangerouslyAllowLocalIP`

In rare cases when self-hosting Next.js on a private network, you may want to allow optimizing images from local IP addresses on the same network. This is not recommended for most users because it could allow malicious users to access content on your internal network.

By default, the value is false.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowLocalIP: false,
  },
}
```

If you need to optimize remote images hosted elsewhere in your local network, you can set the value to true.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowLocalIP: true,
  },
}
```

#### `dangerouslyAllowSVG`

`dangerouslyAllowSVG` allows you to serve SVG images.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
  },
}
```

By default, Next.js does not optimize SVG images for a few reasons:

* SVG is a vector format meaning it can be resized losslessly.
* SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper [Content Security Policy (CSP) headers](/docs/app/api-reference/config/next-config-js/headers.md#content-security-policy).

We recommend using the [`unoptimized`](#unoptimized) prop when the [`src`](#src) prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.

```jsx
<Image src="/my-image.svg" unoptimized />
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

#### `contentDispositionType`

`contentDispositionType` allows you to configure the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header.

```js filename="next.config.js"
module.exports = {
  images: {
    contentDispositionType: 'inline',
  },
}
```

#### `contentSecurityPolicy`

`contentSecurityPolicy` allows you to configure the [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) header for images. This is particularly important when using [`dangerouslyAllowSVG`](#dangerouslyallowsvg) to prevent scripts embedded in the image from executing.

```js filename="next.config.js"
module.exports = {
  images: {
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

By default, the [loader](#loader) sets the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header to `attachment` for added protection since the API can serve arbitrary remote images.

The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when [`dangerouslyAllowSVG`](#dangerouslyallowsvg) is true.

You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.

### Deprecated configuration options

#### `domains`

> **Warning**: Deprecated since Next.js 14 in favor of strict [`remotePatterns`](#remotepatterns) in order to protect your application from malicious users.

Similar to [`remotePatterns`](#remotepatterns), the `domains` configuration can be used to provide a list of allowed hostnames for external images. However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.

Since most remote image servers are shared between multiple tenants, it's safer to use `remotePatterns` to ensure only the intended images are optimized.

Below is an example of the `domains` property in the `next.config.js` file:

```js filename="next.config.js"
module.exports = {
  images: {
    domains: ['assets.acme.com'],
  },
}
```

## Functions

### `getImageProps`

The `getImageProps` function can be used to get the props that would be passed to the underlying `<img>` element, and instead pass them to another component, style, canvas, etc.

```jsx
import { getImageProps } from 'next/image'

const { props } = getImageProps({
  src: 'https://example.com/image.jpg',
  alt: 'A scenic mountain view',
  width: 1200,
  height: 800,
})

function ImageWithCaption() {
  return (
    <figure>
      <img {...props} />
      <figcaption>A scenic mountain view</figcaption>
    </figure>
  )
}
```

This also avoid calling React `useState()` so it can lead to better performance, but it cannot be used with the [`placeholder`](#placeholder) prop because the placeholder will never be removed.

## Known browser bugs

This `next/image` component uses browser native [lazy loading](https://caniuse.com/loading-lazy-attr), which may fallback to eager loading for older browsers before Safari 15.4. When using the blur-up placeholder, older browsers before Safari 12 will fallback to empty placeholder. When using styles with `width`/`height` of `auto`, it is possible to cause [Layout Shift](https://web.dev/cls/) on older browsers before Safari 15 that don't [preserve the aspect ratio](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes). For more details, see [this MDN video](https://www.youtube.com/watch?v=4-d_SoCHeWE).

* [Safari 15 - 16.3](https://bugs.webkit.org/show_bug.cgi?id=243601) display a gray border while loading. Safari 16.4 [fixed this issue](https://webkit.org/blog/13966/webkit-features-in-safari-16-4/#:~:text=Now%20in%20Safari%2016.4%2C%20a%20gray%20line%20no%20longer%20appears%20to%20mark%20the%20space%20where%20a%20lazy%2Dloaded%20image%20will%20appear%20once%20it%E2%80%99s%20been%20loaded.). Possible solutions:
  * Use CSS `@supports (font: -apple-system-body) and (-webkit-appearance: none) { img[loading="lazy"] { clip-path: inset(0.6px) } }`
  * Use [`loading="eager"`](#loading) if the image is above the fold
* [Firefox 67+](https://bugzilla.mozilla.org/show_bug.cgi?id=1556156) displays a white background while loading. Possible solutions:
  * Enable [AVIF `formats`](#formats)
  * Use [`placeholder`](#placeholder)

## Examples

### Styling images

Styling the Image component is similar to styling a normal `<img>` element, but there are a few guidelines to keep in mind:

Use `className` or `style`, not `styled-jsx`. In most cases, we recommend using the `className` prop. This can be an imported [CSS Module](/docs/app/getting-started/css.md), a [global stylesheet](/docs/app/getting-started/css.md#global-css), etc.

```jsx
import styles from './styles.module.css'

export default function MyImage() {
  return <Image className={styles.image} src="/my-image.png" alt="My Image" />
}
```

You can also use the `style` prop to assign inline styles.

```jsx
export default function MyImage() {
  return (
    <Image style={{ borderRadius: '8px' }} src="/my-image.png" alt="My Image" />
  )
}
```

When using `fill`, the parent element must have `position: relative` or `display: block`. This is necessary for the proper rendering of the image element in that layout mode.

```jsx
<div style={{ position: 'relative' }}>
  <Image fill src="/my-image.png" alt="My Image" />
</div>
```

You cannot use [styled-jsx](/docs/app/guides/css-in-js.md) because it's scoped to the current component (unless you mark the style as `global`).

### Responsive images with a static export

When you import a static image, Next.js automatically sets its width and height based on the file. You can make the image responsive by setting the style:

![Responsive image filling the width and height of its parent container](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/responsive-image.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Responsive() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column' }}>
      <Image
        alt="Mountains"
        // Importing an image will
        // automatically set the width and height
        src={mountains}
        sizes="100vw"
        // Make the image display full width
        // and preserve its aspect ratio
        style={{
          width: '100%',
          height: 'auto',
        }}
      />
    </div>
  )
}
```

### Responsive images with a remote URL

If the source image is a dynamic or a remote URL, you must provide the width and height props so Next.js can calculate the aspect ratio:

```jsx filename="components/page.js"
import Image from 'next/image'

export default function Page({ photoUrl }) {
  return (
    <Image
      src={photoUrl}
      alt="Picture of the author"
      sizes="100vw"
      style={{
        width: '100%',
        height: 'auto',
      }}
      width={500}
      height={300}
    />
  )
}
```

Try it out:

* [Demo the image responsive to viewport](https://image-component.nextjs.gallery/responsive)

### Responsive image with `fill`

If you don't know the aspect ratio of the image, you can add the [`fill` prop](#fill) with the `objectFit` prop set to `cover`. This will make the image fill the full width of its parent container.

![Grid of images filling parent container width](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/fill-container.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Fill() {
  return (
    <div
      style={{
        display: 'grid',
        gridGap: '8px',
        gridTemplateColumns: 'repeat(auto-fit, minmax(400px, auto))',
      }}
    >
      <div style={{ position: 'relative', width: '400px' }}>
        <Image
          alt="Mountains"
          src={mountains}
          fill
          sizes="(min-width: 808px) 50vw, 100vw"
          style={{
            objectFit: 'cover', // cover, contain, none
          }}
        />
      </div>
      {/* And more images in the grid... */}
    </div>
  )
}
```

### Background Image

Use the `fill` prop to make the image cover the entire screen area:

![Background image taking full width and height of page](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/background-image.png)

```jsx
import Image from 'next/image'
import mountains from '../public/mountains.jpg'

export default function Background() {
  return (
    <Image
      alt="Mountains"
      src={mountains}
      placeholder="blur"
      quality={100}
      fill
      sizes="100vw"
      style={{
        objectFit: 'cover',
      }}
    />
  )
}
```

For examples of the Image component used with the various styles, see the [Image Component Demo](https://image-component.nextjs.gallery).

### Remote images

To use a remote image, the `src` property should be a URL string.

```jsx filename="app/page.js"
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="https://s3.amazonaws.com/my-bucket/profile.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

Since Next.js does not have access to remote files during the build process, you'll need to provide the [`width`](/docs/app/api-reference/components/image.md#width-and-height), [`height`](/docs/app/api-reference/components/image.md#width-and-height) and optional [`blurDataURL`](/docs/app/api-reference/components/image.md#blurdataurl) props manually.

The `width` and `height` attributes are used to infer the correct aspect ratio of image and avoid layout shift from the image loading in. The `width` and `height` do *not* determine the rendered size of the image file.

To safely allow optimizing images, define a list of supported URL patterns in `next.config.js`. Be as specific as possible to prevent malicious usage. For example, the following configuration will only allow images from a specific AWS S3 bucket:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 's3.amazonaws.com',
        port: '',
        pathname: '/my-bucket/**',
        search: '',
      },
    ],
  },
}
```

### Theme detection

If you want to display a different image for light and dark mode, you can create a new component that wraps two `<Image>` components and reveals the correct one based on a CSS media query.

```css filename="components/theme-image.module.css"
.imgDark {
  display: none;
}

@media (prefers-color-scheme: dark) {
  .imgLight {
    display: none;
  }
  .imgDark {
    display: unset;
  }
}
```

```tsx filename="components/theme-image.tsx" switcher
import styles from './theme-image.module.css'
import Image, { ImageProps } from 'next/image'

type Props = Omit<ImageProps, 'src' | 'preload' | 'loading'> & {
  srcLight: string
  srcDark: string
}

const ThemeImage = (props: Props) => {
  const { srcLight, srcDark, ...rest } = props

  return (
    <>
      <Image {...rest} src={srcLight} className={styles.imgLight} />
      <Image {...rest} src={srcDark} className={styles.imgDark} />
    </>
  )
}
```

```jsx filename="components/theme-image.js" switcher
import styles from './theme-image.module.css'
import Image from 'next/image'

const ThemeImage = (props) => {
  const { srcLight, srcDark, ...rest } = props

  return (
    <>
      <Image {...rest} src={srcLight} className={styles.imgLight} />
      <Image {...rest} src={srcDark} className={styles.imgDark} />
    </>
  )
}
```

> **Good to know**: The default behavior of `loading="lazy"` ensures that only the correct image is loaded. You cannot use `preload` or `loading="eager"` because that would cause both images to load. Instead, you can use [`fetchPriority="high"`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/fetchPriority).

Try it out:

* [Demo light/dark mode theme detection](https://image-component.nextjs.gallery/theme)

### Art direction

If you want to display a different image for mobile and desktop, sometimes called [Art Direction](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#art_direction), you can provide different `src`, `width`, `height`, and `quality` props to `getImageProps()`.

```jsx filename="app/page.js"
import { getImageProps } from 'next/image'

export default function Home() {
  const common = { alt: 'Art Direction Example', sizes: '100vw' }
  const {
    props: { srcSet: desktop },
  } = getImageProps({
    ...common,
    width: 1440,
    height: 875,
    quality: 80,
    src: '/desktop.jpg',
  })
  const {
    props: { srcSet: mobile, ...rest },
  } = getImageProps({
    ...common,
    width: 750,
    height: 1334,
    quality: 70,
    src: '/mobile.jpg',
  })

  return (
    <picture>
      <source media="(min-width: 1000px)" srcSet={desktop} />
      <source media="(min-width: 500px)" srcSet={mobile} />
      <img {...rest} style={{ width: '100%', height: 'auto' }} />
    </picture>
  )
}
```

### Background CSS

You can even convert the `srcSet` string to the [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/image/image-set) CSS function to optimize a background image.

```jsx filename="app/page.js"
import { getImageProps } from 'next/image'

function getBackgroundImage(srcSet = '') {
  const imageSet = srcSet
    .split(', ')
    .map((str) => {
      const [url, dpi] = str.split(' ')
      return `url("${url}") ${dpi}`
    })
    .join(', ')
  return `image-set(${imageSet})`
}

export default function Home() {
  const {
    props: { srcSet },
  } = getImageProps({ alt: '', width: 128, height: 128, src: '/img.png' })
  const backgroundImage = getBackgroundImage(srcSet)
  const style = { height: '100vh', width: '100vw', backgroundImage }

  return (
    <main style={style}>
      <h1>Hello World</h1>
    </main>
  )
}
```

## Version History

| Version    | Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `v16.0.0`  | `qualities` default configuration changed to `[75]`, `preload` prop added, `priority` prop deprecated, `dangerouslyAllowLocalIP` config added, `maximumRedirects` config added.                                                                                                                                                                                                                                                                                                            |
| `v15.3.0`  | `remotePatterns` added support for array of `URL` objects.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `v15.0.0`  | `contentDispositionType` configuration default changed to `attachment`.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `v14.2.23` | `qualities` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `v14.2.15` | `decoding` prop added and `localPatterns` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `v14.2.14` | `remotePatterns.search` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `v14.2.0`  | `overrideSrc` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `v14.1.0`  | `getImageProps()` is stable.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `v14.0.0`  | `onLoadingComplete` prop and `domains` config deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `v13.4.14` | `placeholder` prop support for `data:/image...`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `v13.2.0`  | `contentDispositionType` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `v13.0.6`  | `ref` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `v13.0.0`  | The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A [codemod is available](/docs/app/guides/upgrading/codemods.md#next-image-to-legacy-image) to safely and automatically rename your imports. `<span>` wrapper removed. `layout`, `objectFit`, `objectPosition`, `lazyBoundary`, `lazyRoot` props removed. `alt` is required. `onLoadingComplete` receives reference to `img` element. Built-in loader config removed. |
| `v12.3.0`  | `remotePatterns` and `unoptimized` configuration is stable.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `v12.2.0`  | Experimental `remotePatterns` and experimental `unoptimized` configuration added. `layout="raw"` removed.                                                                                                                                                                                                                                                                                                                                                                                  |
| `v12.1.1`  | `style` prop added. Experimental support for `layout="raw"` added.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `v12.1.0`  | `dangerouslyAllowSVG` and `contentSecurityPolicy` configuration added.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `v12.0.9`  | `lazyRoot` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `v12.0.0`  | `formats` configuration added.AVIF support added.Wrapper `<div>` changed to `<span>`.                                                                                                                                                                                                                                                                                                                                                                                            |
| `v11.1.0`  | `onLoadingComplete` and `lazyBoundary` props added.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `v11.0.0`  | `src` prop support for static import.`placeholder` prop added.`blurDataURL` prop added.                                                                                                                                                                                                                                                                                                                                                                                          |
| `v10.0.5`  | `loader` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `v10.0.1`  | `layout` prop added.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `v10.0.0`  | `next/image` introduced.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |


--------------------------------------------------------------------------------
title: "Image (Legacy)"
description: "Backwards compatible Image Optimization with the Legacy Image component."
source: "https://nextjs.org/docs/pages/api-reference/components/image-legacy"
--------------------------------------------------------------------------------

# Image (Legacy)

@router: Pages Router

> This is a legacy API and no longer recommended. It is still supported for backward compatibility.

Starting with Next.js 13, the `next/image` component was rewritten to improve both the performance and developer experience. In order to provide a backwards compatible upgrade solution, the old `next/image` was renamed to `next/legacy/image`.

> **Warning**: `next/legacy/image` is deprecated and will be removed in a future version of Next.js. Please use [`next/image`](/docs/app/api-reference/components/image.md) instead.

## Comparison

Compared to `next/legacy/image`, the new `next/image` component has the following changes:

* Removes `<span>` wrapper around `<img>` in favor of [native computed aspect ratio](https://caniuse.com/mdn-html_elements_img_aspect_ratio_computed_from_attributes)
* Adds support for canonical `style` prop
  * Removes `layout` prop in favor of `style` or `className`
  * Removes `objectFit` prop in favor of `style` or `className`
  * Removes `objectPosition` prop in favor of `style` or `className`
* Removes `IntersectionObserver` implementation in favor of [native lazy loading](https://caniuse.com/loading-lazy-attr)
  * Removes `lazyBoundary` prop since there is no native equivalent
  * Removes `lazyRoot` prop since there is no native equivalent
* Removes `loader` config in favor of [`loader`](#loader) prop
* Changed `alt` prop from optional to required
* Changed `onLoadingComplete` callback to receive reference to `<img>` element

## Required Props

The `<Image />` component requires the following properties.

### src

Must be one of the following:

* A [statically imported](/docs/pages/api-reference/components/image.md#src) image file
* A path string. This can be either an absolute external URL, or an internal path depending on the [loader](#loader) prop or [loader configuration](#loader-configuration).

When using the default [loader](#loader), also consider the following for source images:

* When src is an external URL, you must also configure [remotePatterns](#remote-patterns)
* When src is [animated](#animated-images) or not a known format (JPEG, PNG, WebP, AVIF, GIF, TIFF) the image will be served as-is
* When src is SVG format, it will be blocked unless `unoptimized` or `dangerouslyAllowSVG` is enabled

### width

The `width` property can represent either the *rendered* width or *original* width in pixels, depending on the [`layout`](#layout) and [`sizes`](#sizes) properties.

When using `layout="intrinsic"` or `layout="fixed"` the `width` property represents the *rendered* width in pixels, so it will affect how large the image appears.

When using `layout="responsive"`, `layout="fill"`, the `width` property represents the *original* width in pixels, so it will only affect the aspect ratio.

The `width` property is required, except for [statically imported images](/docs/pages/api-reference/components/image.md#src), or those with `layout="fill"`.

### height

The `height` property can represent either the *rendered* height or *original* height in pixels, depending on the [`layout`](#layout) and [`sizes`](#sizes) properties.

When using `layout="intrinsic"` or `layout="fixed"` the `height` property represents the *rendered* height in pixels, so it will affect how large the image appears.

When using `layout="responsive"`, `layout="fill"`, the `height` property represents the *original* height in pixels, so it will only affect the aspect ratio.

The `height` property is required, except for [statically imported images](/docs/pages/api-reference/components/image.md#src), or those with `layout="fill"`.

## Optional Props

The `<Image />` component accepts a number of additional properties beyond those which are required. This section describes the most commonly-used properties of the Image component. Find details about more rarely-used properties in the [Advanced Props](#advanced-props) section.

### layout

The layout behavior of the image as the viewport changes size.

| `layout`              | Behavior                                                 | `srcSet`                                                                                                    | `sizes` | Has wrapper and sizer |
| --------------------- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------- | --------------------- |
| `intrinsic` (default) | Scale *down* to fit width of container, up to image size | `1x`, `2x` (based on [imageSizes](#image-sizes))                                                            | N/A     | yes                   |
| `fixed`               | Sized to `width` and `height` exactly                    | `1x`, `2x` (based on [imageSizes](#image-sizes))                                                            | N/A     | yes                   |
| `responsive`          | Scale to fit width of container                          | `640w`, `750w`, ... `2048w`, `3840w` (based on [imageSizes](#image-sizes) and [deviceSizes](#device-sizes)) | `100vw` | yes                   |
| `fill`                | Grow in both X and Y axes to fill container              | `640w`, `750w`, ... `2048w`, `3840w` (based on [imageSizes](#image-sizes) and [deviceSizes](#device-sizes)) | `100vw` | yes                   |

* [Demo the `intrinsic` layout (default)](https://image-legacy-component.nextjs.gallery/layout-intrinsic)
  * When `intrinsic`, the image will scale the dimensions down for smaller viewports, but maintain the original dimensions for larger viewports.
* [Demo the `fixed` layout](https://image-legacy-component.nextjs.gallery/layout-fixed)
  * When `fixed`, the image dimensions will not change as the viewport changes (no responsiveness) similar to the native `img` element.
* [Demo the `responsive` layout](https://image-legacy-component.nextjs.gallery/layout-responsive)
  * When `responsive`, the image will scale the dimensions down for smaller viewports and scale up for larger viewports.
  * Ensure the parent element uses `display: block` in their stylesheet.
* [Demo the `fill` layout](https://image-legacy-component.nextjs.gallery/layout-fill)
  * When `fill`, the image will stretch both width and height to the dimensions of the parent element, provided the parent element is relative.
  * This is usually paired with the [`objectFit`](#objectfit) property.
  * Ensure the parent element has `position: relative` in their stylesheet.
* [Demo background image](https://image-legacy-component.nextjs.gallery/background)

### loader

A custom function used to resolve URLs. Setting the loader as a prop on the Image component overrides the default loader defined in the [`images` section of `next.config.js`](#loader-configuration).

A `loader` is a function returning a URL string for the image, given the following parameters:

* [`src`](#src)
* [`width`](#width)
* [`quality`](#quality)

Here is an example of using a custom loader:

```js
import Image from 'next/legacy/image'

const myLoader = ({ src, width, quality }) => {
  return `https://example.com/${src}?w=${width}&q=${quality || 75}`
}

const MyImage = (props) => {
  return (
    <Image
      loader={myLoader}
      src="me.png"
      alt="Picture of the author"
      width={500}
      height={500}
    />
  )
}
```

### sizes

A string that provides information about how wide the image will be at different breakpoints. The value of `sizes` will greatly affect performance for images using `layout="responsive"` or `layout="fill"`. It will be ignored for images using `layout="intrinsic"` or `layout="fixed"`.

The `sizes` property serves two important purposes related to image performance:

First, the value of `sizes` is used by the browser to determine which size of the image to download, from `next/legacy/image`'s automatically-generated source set. When the browser chooses, it does not yet know the size of the image on the page, so it selects an image that is the same size or larger than the viewport. The `sizes` property allows you to tell the browser that the image will actually be smaller than full screen. If you don't specify a `sizes` value, a default value of `100vw` (full screen width) is used.

Second, the `sizes` value is parsed and used to trim the values in the automatically-created source set. If the `sizes` property includes sizes such as `50vw`, which represent a percentage of the viewport width, then the source set is trimmed to not include any values which are too small to ever be necessary.

For example, if you know your styling will cause an image to be full-width on mobile devices, in a 2-column layout on tablets, and a 3-column layout on desktop displays, you should include a sizes property such as the following:

```js
import Image from 'next/legacy/image'
const Example = () => (
  <div className="grid-element">
    <Image
      src="/example.png"
      layout="fill"
      sizes="(max-width: 768px) 100vw,
              (max-width: 1200px) 50vw,
              33vw"
    />
  </div>
)
```

This example `sizes` could have a dramatic effect on performance metrics. Without the `33vw` sizes, the image selected from the server would be 3 times as wide as it needs to be. Because file size is proportional to the square of the width, without `sizes` the user would download an image that's 9 times larger than necessary.

Learn more about `srcset` and `sizes`:

* [web.dev](https://web.dev/learn/design/responsive-images/#sizes)
* [mdn](https://developer.mozilla.org/docs/Web/HTML/Element/img#attr-sizes)

### quality

The quality of the optimized image, an integer between `1` and `100` where `100` is the best quality. Defaults to `75`.

### priority

When true, the image will be considered high priority and
[preload](https://web.dev/preload-responsive-images/). Lazy loading is automatically disabled for images using `priority`.

You should use the `priority` property on any image detected as the [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp) element. It may be appropriate to have multiple priority images, as different images may be the LCP element for different viewport sizes.

Should only be used when the image is visible above the fold. Defaults to `false`.

### placeholder

A placeholder to use while the image is loading. Possible values are `blur` or `empty`. Defaults to `empty`.

When `blur`, the [`blurDataURL`](#blurdataurl) property will be used as the placeholder. If `src` is an object from a [static import](/docs/pages/api-reference/components/image.md#src) and the imported image is `.jpg`, `.png`, `.webp`, or `.avif`, then `blurDataURL` will be automatically populated.

For dynamic images, you must provide the [`blurDataURL`](#blurdataurl) property. Solutions such as [Plaiceholder](https://github.com/joe-bell/plaiceholder) can help with `base64` generation.

When `empty`, there will be no placeholder while the image is loading, only empty space.

Try it out:

* [Demo the `blur` placeholder](https://image-legacy-component.nextjs.gallery/placeholder)
* [Demo the shimmer effect with `blurDataURL` prop](https://image-legacy-component.nextjs.gallery/shimmer)
* [Demo the color effect with `blurDataURL` prop](https://image-legacy-component.nextjs.gallery/color)

## Advanced Props

In some cases, you may need more advanced usage. The `<Image />` component optionally accepts the following advanced properties.

### style

Allows [passing CSS styles](https://developer.mozilla.org/docs/Web/HTML/Element/style) to the underlying image element.

Note that all `layout` modes apply their own styles to the image element, and these automatic styles take precedence over the `style` prop.

Also keep in mind that the required `width` and `height` props can interact with your styling. If you use styling to modify an image's `width`, you must set the `height="auto"` style as well, or your image will be distorted.

### objectFit

Defines how the image will fit into its parent container when using `layout="fill"`.

This value is passed to the [object-fit CSS property](https://developer.mozilla.org/docs/Web/CSS/object-fit) for the `src` image.

### objectPosition

Defines how the image is positioned within its parent element when using `layout="fill"`.

This value is passed to the [object-position CSS property](https://developer.mozilla.org/docs/Web/CSS/object-position) applied to the image.

### onLoadingComplete

A callback function that is invoked once the image is completely loaded and the [placeholder](#placeholder) has been removed.

The `onLoadingComplete` function accepts one parameter, an object with the following properties:

* [`naturalWidth`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/naturalWidth)
* [`naturalHeight`](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/naturalHeight)

### loading

The loading behavior of the image. Defaults to `lazy`.

When `lazy`, defer loading the image until it reaches a calculated distance from
the viewport.

When `eager`, load the image immediately.

[Learn more](https://developer.mozilla.org/docs/Web/HTML/Element/img#attr-loading)

### blurDataURL

A [Data URL](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs) to
be used as a placeholder image before the `src` image successfully loads. Only takes effect when combined
with [`placeholder="blur"`](#placeholder).

Must be a base64-encoded image. It will be enlarged and blurred, so a very small image (10px or
less) is recommended. Including larger images as placeholders may harm your application performance.

Try it out:

* [Demo the default `blurDataURL` prop](https://image-legacy-component.nextjs.gallery/placeholder)
* [Demo the shimmer effect with `blurDataURL` prop](https://image-legacy-component.nextjs.gallery/shimmer)
* [Demo the color effect with `blurDataURL` prop](https://image-legacy-component.nextjs.gallery/color)

You can also [generate a solid color Data URL](https://png-pixel.com) to match the image.

### lazyBoundary

A string (with similar syntax to the margin property) that acts as the bounding box used to detect the intersection of the viewport with the image and trigger lazy [loading](#loading). Defaults to `"200px"`.

If the image is nested in a scrollable parent element other than the root document, you will also need to assign the [lazyRoot](#lazyroot) prop.

[Learn more](https://developer.mozilla.org/docs/Web/API/IntersectionObserver/rootMargin)

### lazyRoot

A React [Ref](https://react.dev/learn/referencing-values-with-refs) pointing to the scrollable parent element. Defaults to `null` (the document viewport).

The Ref must point to a DOM element or a React component that [forwards the Ref](https://react.dev/reference/react/forwardRef) to the underlying DOM element.

**Example pointing to a DOM element**

```jsx
import Image from 'next/legacy/image'
import React from 'react'

const Example = () => {
  const lazyRoot = React.useRef(null)

  return (
    <div ref={lazyRoot} style={{ overflowX: 'scroll', width: '500px' }}>
      <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
      <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
    </div>
  )
}
```

**Example pointing to a React component**

```jsx
import Image from 'next/legacy/image'
import React from 'react'

const Container = React.forwardRef((props, ref) => {
  return (
    <div ref={ref} style={{ overflowX: 'scroll', width: '500px' }}>
      {props.children}
    </div>
  )
})

const Example = () => {
  const lazyRoot = React.useRef(null)

  return (
    <Container ref={lazyRoot}>
      <Image lazyRoot={lazyRoot} src="/one.jpg" width="500" height="500" />
      <Image lazyRoot={lazyRoot} src="/two.jpg" width="500" height="500" />
    </Container>
  )
}
```

[Learn more](https://developer.mozilla.org/docs/Web/API/IntersectionObserver/root)

### unoptimized

When true, the source image will be served as-is from the `src` instead of changing quality, size, or format. Defaults to `false`.

This is useful for images that do not benefit from optimization such as small images (less than 1KB), vector images (SVG), or animated images (GIF).

```js
import Image from 'next/image'

const UnoptimizedImage = (props) => {
  return <Image {...props} unoptimized />
}
```

Since Next.js 12.3.0, this prop can be assigned to all images by updating `next.config.js` with the following configuration:

```js filename="next.config.js"
module.exports = {
  images: {
    unoptimized: true,
  },
}
```

## Other Props

Other properties on the `<Image />` component will be passed to the underlying
`img` element with the exception of the following:

* `srcSet`. Use
  [Device Sizes](#device-sizes)
  instead.
* `ref`. Use [`onLoadingComplete`](#onloadingcomplete) instead.
* `decoding`. It is always `"async"`.

## Configuration Options

### Remote Patterns

To protect your application from malicious users, configuration is required in order to use external images. This ensures that only external images from your account can be served from the Next.js Image Optimization API. These external images can be configured with the `remotePatterns` property in your `next.config.js` file, as shown below:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'example.com',
        port: '',
        pathname: '/account123/**',
        search: '',
      },
    ],
  },
}
```

> **Good to know**: The example above will ensure the `src` property of `next/legacy/image` must start with `https://example.com/account123/` and must not have a query string. Any other protocol, hostname, port, or unmatched path will respond with 400 Bad Request.

Below is an example of the `remotePatterns` property in the `next.config.js` file using a wildcard pattern in the `hostname`:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.example.com',
        port: '',
        search: '',
      },
    ],
  },
}
```

> **Good to know**: The example above will ensure the `src` property of `next/legacy/image` must start with `https://img1.example.com` or `https://me.avatar.example.com` or any number of subdomains. It cannot have a port or query string. Any other protocol or unmatched hostname will respond with 400 Bad Request.

Wildcard patterns can be used for both `pathname` and `hostname` and have the following syntax:

* `*` match a single path segment or subdomain
* `**` match any number of path segments at the end or subdomains at the beginning

The `**` syntax does not work in the middle of the pattern.

> **Good to know**: When omitting `protocol`, `port`, `pathname`, or `search` then the wildcard `**` is implied. This is not recommended because it may allow malicious actors to optimize urls you did not intend.

Below is an example of the `remotePatterns` property in the `next.config.js` file using `search`:

```js filename="next.config.js"
module.exports = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'assets.example.com',
        search: '?v=1727111025337',
      },
    ],
  },
}
```

> **Good to know**: The example above will ensure the `src` property of `next/legacy/image` must start with `https://assets.example.com` and must have the exact query string `?v=1727111025337`. Any other protocol or query string will respond with 400 Bad Request.

### Domains

> **Warning**: Deprecated since Next.js 14 in favor of strict [`remotePatterns`](#remote-patterns) in order to protect your application from malicious users. Only use `domains` if you own all the content served from the domain.

Similar to [`remotePatterns`](#remote-patterns), the `domains` configuration can be used to provide a list of allowed hostnames for external images.

However, the `domains` configuration does not support wildcard pattern matching and it cannot restrict protocol, port, or pathname.

Below is an example of the `domains` property in the `next.config.js` file:

```js filename="next.config.js"
module.exports = {
  images: {
    domains: ['assets.acme.com'],
  },
}
```

### Loader Configuration

If you want to use a cloud provider to optimize images instead of using the Next.js built-in Image Optimization API, you can configure the `loader` and `path` prefix in your `next.config.js` file. This allows you to use relative URLs for the Image [`src`](#src) and automatically generate the correct absolute URL for your provider.

```js filename="next.config.js"
module.exports = {
  images: {
    loader: 'imgix',
    path: 'https://example.com/myaccount/',
  },
}
```

#### Customizing the Built-in Image Path

If you want to change or prefix the default path for the built-in Next.js image optimization, you can do so with the `path` property. The default value for `path` is `/_next/image`.

```js filename="next.config.js"
module.exports = {
  images: {
    path: '/my-prefix/_next/image',
  },
}
```

### Built-in Loaders

The following Image Optimization cloud providers are included:

* Default: Works automatically with `next dev`, `next start`, or a custom server
* [Vercel](https://vercel.com): Works automatically when you deploy on Vercel, no configuration necessary. [Learn more](https://vercel.com/docs/concepts/image-optimization?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website)
* [Imgix](https://www.imgix.com): `loader: 'imgix'`
* [Cloudinary](https://cloudinary.com): `loader: 'cloudinary'`
* [Akamai](https://www.akamai.com): `loader: 'akamai'`
* Custom: `loader: 'custom'` use a custom cloud provider by implementing the [`loader`](#loader) prop on the `next/legacy/image` component

If you need a different provider, you can use the [`loader`](#loader) prop with `next/legacy/image`.

> Images can not be optimized at build time using [`output: 'export'`](/docs/pages/guides/static-exports.md), only on-demand. To use `next/legacy/image` with `output: 'export'`, you will need to use a different loader than the default. [Read more in the discussion.](https://github.com/vercel/next.js/discussions/19065)

## Advanced

The following configuration is for advanced use cases and is usually not necessary. If you choose to configure the properties below, you will override any changes to the Next.js defaults in future updates.

### Device Sizes

If you know the expected device widths of your users, you can specify a list of device width breakpoints using the `deviceSizes` property in `next.config.js`. These widths are used when the `next/legacy/image` component uses `layout="responsive"` or `layout="fill"` to ensure the correct image is served for user's device.

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
  },
}
```

### Image Sizes

You can specify a list of image widths using the `images.imageSizes` property in your `next.config.js` file. These widths are concatenated with the array of [device sizes](#device-sizes) to form the full array of sizes used to generate image [srcset](https://developer.mozilla.org/docs/Web/API/HTMLImageElement/srcset)s.

The reason there are two separate lists is that imageSizes is only used for images which provide a [`sizes`](#sizes) prop, which indicates that the image is less than the full width of the screen. **Therefore, the sizes in imageSizes should all be smaller than the smallest size in deviceSizes.**

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    imageSizes: [32, 48, 64, 96, 128, 256, 384],
  },
}
```

### Acceptable Formats

The default [Image Optimization API](#loader-configuration) will automatically detect the browser's supported image formats via the request's `Accept` header in order to determine the best output format.

If the `Accept` header matches more than one of the configured formats, the first match in the array is used. Therefore, the array order matters. If there is no match (or the source image is [animated](#animated-images)), the Image Optimization API will fallback to the original image's format.

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    formats: ['image/webp'],
  },
}
```

You can enable AVIF support, which will fallback to the original format of the src image if the browser [does not support AVIF](https://caniuse.com/avif):

```js filename="next.config.js"
module.exports = {
  images: {
    formats: ['image/avif'],
  },
}
```

> **Good to know**:
>
> * We still recommend using WebP for most use cases.
> * AVIF generally takes 50% longer to encode but it compresses 20% smaller compared to WebP. This means that the first time an image is requested, it will typically be slower and then subsequent requests that are cached will be faster.
> * If you self-host with a Proxy/CDN in front of Next.js, you must configure the Proxy to forward the `Accept` header.

## Caching Behavior

The following describes the caching algorithm for the default [loader](#loader). For all other loaders, please refer to your cloud provider's documentation.

Images are optimized dynamically upon request and stored in the `<distDir>/cache/images` directory. The optimized image file will be served for subsequent requests until the expiration is reached. When a request is made that matches a cached but expired file, the expired image is served stale immediately. Then the image is optimized again in the background (also called revalidation) and saved to the cache with the new expiration date.

The cache status of an image can be determined by reading the value of the `x-nextjs-cache` (`x-vercel-cache` when deployed on Vercel) response header. The possible values are the following:

* `MISS` - the path is not in the cache (occurs at most once, on the first visit)
* `STALE` - the path is in the cache but exceeded the revalidate time so it will be updated in the background
* `HIT` - the path is in the cache and has not exceeded the revalidate time

The expiration (or rather Max Age) is defined by either the [`minimumCacheTTL`](#minimum-cache-ttl) configuration or the upstream image `Cache-Control` header, whichever is larger. Specifically, the `max-age` value of the `Cache-Control` header is used. If both `s-maxage` and `max-age` are found, then `s-maxage` is preferred. The `max-age` is also passed-through to any downstream clients including CDNs and browsers.

* You can configure [`minimumCacheTTL`](#minimum-cache-ttl) to increase the cache duration when the upstream image does not include `Cache-Control` header or the value is very low.
* You can configure [`deviceSizes`](#device-sizes) and [`imageSizes`](#image-sizes) to reduce the total number of possible generated images.
* You can configure [formats](#acceptable-formats) to disable multiple formats in favor of a single image format.

### Minimum Cache TTL

You can configure the Time to Live (TTL) in seconds for cached optimized images. In many cases, it's better to use a [Static Image Import](/docs/pages/api-reference/components/image.md#src) which will automatically hash the file contents and cache the image forever with a `Cache-Control` header of `immutable`.

If no configuration is provided, the default below is used.

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 14400, // 4 hours
  },
}
```

You can increase the TTL to reduce the number of revalidations and potentially lower cost:

```js filename="next.config.js"
module.exports = {
  images: {
    minimumCacheTTL: 2678400, // 31 days
  },
}
```

The expiration (or rather Max Age) of the optimized image is defined by either the `minimumCacheTTL` or the upstream image `Cache-Control` header, whichever is larger.

If you need to change the caching behavior per image, you can configure [`headers`](/docs/pages/api-reference/config/next-config-js/headers.md) to set the `Cache-Control` header on the upstream image (e.g. `/some-asset.jpg`, not `/_next/image` itself).

There is no mechanism to invalidate the cache at this time, so its best to keep `minimumCacheTTL` low. Otherwise you may need to manually change the [`src`](#src) prop or delete `<distDir>/cache/images`.

### Disable Static Imports

The default behavior allows you to import static files such as `import icon from './icon.png'` and then pass that to the `src` property.

In some cases, you may wish to disable this feature if it conflicts with other plugins that expect the import to behave differently.

You can disable static image imports inside your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  images: {
    disableStaticImages: true,
  },
}
```

### Dangerously Allow SVG

The default [loader](#loader) does not optimize SVG images for a few reasons. First, SVG is a vector format meaning it can be resized losslessly. Second, SVG has many of the same features as HTML/CSS, which can lead to vulnerabilities without proper [Content Security Policy (CSP) headers](/docs/app/api-reference/config/next-config-js/headers.md#content-security-policy).

Therefore, we recommended using the [`unoptimized`](#unoptimized) prop when the [`src`](#src) prop is known to be SVG. This happens automatically when `src` ends with `".svg"`.

However, if you need to serve SVG images with the default Image Optimization API, you can set `dangerouslyAllowSVG` inside your `next.config.js`:

```js filename="next.config.js"
module.exports = {
  images: {
    dangerouslyAllowSVG: true,
    contentDispositionType: 'attachment',
    contentSecurityPolicy: "default-src 'self'; script-src 'none'; sandbox;",
  },
}
```

In addition, it is strongly recommended to also set `contentDispositionType` to force the browser to download the image, as well as `contentSecurityPolicy` to prevent scripts embedded in the image from executing.

### `contentDispositionType`

The default [loader](#loader) sets the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition#as_a_response_header_for_the_main_body) header to `attachment` for added protection since the API can serve arbitrary remote images.

The default value is `attachment` which forces the browser to download the image when visiting directly. This is particularly important when [`dangerouslyAllowSVG`](#dangerously-allow-svg) is true.

You can optionally configure `inline` to allow the browser to render the image when visiting directly, without downloading it.

```js filename="next.config.js"
module.exports = {
  images: {
    contentDispositionType: 'inline',
  },
}
```

### Animated Images

The default [loader](#loader) will automatically bypass Image Optimization for animated images and serve the image as-is.

Auto-detection for animated files is best-effort and supports GIF, APNG, and WebP. If you want to explicitly bypass Image Optimization for a given animated image, use the [unoptimized](#unoptimized) prop.

## Version History

| Version   | Changes                                                                                                             |
| --------- | ------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | `next/legacy/image` deprecated and will be removed in a future version of Next.js. Please use `next/image` instead. |
| `v13.0.0` | `next/image` renamed to `next/legacy/image`                                                                         |


--------------------------------------------------------------------------------
title: "Link Component"
description: "Enable fast client-side navigation with the built-in `next/link` component."
source: "https://nextjs.org/docs/pages/api-reference/components/link"
--------------------------------------------------------------------------------

# Link

@router: Pages Router

`<Link>` is a React component that extends the HTML `<a>` element to provide [prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching) and client-side navigation between routes. It is the primary way to navigate between routes in Next.js.

Basic usage:

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return <Link href="/dashboard">Dashboard</Link>
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return <Link href="/dashboard">Dashboard</Link>
}
```

## Reference

The following props can be passed to the `<Link>` component:

| Prop                        | Example                  | Type              | Required |
| --------------------------- | ------------------------ | ----------------- | -------- |
| [`href`](#href-required)    | `href="/dashboard"`      | String or Object  | Yes      |
| [`as`](#as)                 | `as="/post/abc"`         | String or Object  | -        |
| [`replace`](#replace)       | `replace={false}`        | Boolean           | -        |
| [`scroll`](#scroll)         | `scroll={false}`         | Boolean           | -        |
| [`prefetch`](#prefetch)     | `prefetch={false}`       | Boolean           | -        |
| [`shallow`](#shallow)       | `shallow={false}`        | Boolean           | -        |
| [`locale`](#locale)         | `locale="fr"`            | String or Boolean | -        |
| [`onNavigate`](#onnavigate) | `onNavigate={(e) => {}}` | Function          | -        |

> **Good to know**: `<a>` tag attributes such as `className` or `target="_blank"` can be added to `<Link>` as props and will be passed to the underlying `<a>` element.

### `href` (required)

The path or URL to navigate to.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

// Navigate to /about?name=test
export default function Home() {
  return (
    <Link
      href={{
        pathname: '/about',
        query: { name: 'test' },
      }}
    >
      About
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

// Navigate to /about?name=test
export default function Home() {
  return (
    <Link
      href={{
        pathname: '/about',
        query: { name: 'test' },
      }}
    >
      About
    </Link>
  )
}
```

### `replace`

**Defaults to `false`.** When `true`, `next/link` will replace the current history state instead of adding a new URL into the [browser's history](https://developer.mozilla.org/docs/Web/API/History_API) stack.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

### `scroll`

**Defaults to `true`.** The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position**, similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](/docs/app/api-reference/file-conventions/page.md), scroll position will stay the same as long as the Page is visible in the viewport. However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element.

When `scroll = {false}`, Next.js will not attempt to scroll to the first Page element.

> **Good to know**: Next.js checks if `scroll: false` before managing scroll behavior. If scrolling is enabled, it identifies the relevant DOM node for navigation and inspects each top-level element. All non-scrollable elements and those without rendered HTML are bypassed, this includes sticky or fixed positioned elements, and non-visible elements such as those calculated with `getBoundingClientRect`. Next.js then continues through siblings until it identifies a scrollable element that is visible in the viewport.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

### `prefetch`

Prefetching happens when a `<Link />` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and data in the background to improve the performance of client-side navigation's. **Prefetching is only enabled in production**.

The following values can be passed to the `prefetch` prop:

* **`true` (default)**: The full route and its data will be prefetched.
* `false`: Prefetching will not happen when entering the viewport, but will happen on hover. If you want to completely remove fetching on hover as well, consider using an `<a>` tag or [incrementally adopting](/docs/app/guides/migrating/app-router-migration.md) the App Router, which enables disabling prefetching on hover too.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

### `shallow`

Update the path of the current page without rerunning [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md), [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md) or [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md). Defaults to `false`.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" shallow={false}>
      Dashboard
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/dashboard" shallow={false}>
      Dashboard
    </Link>
  )
}
```

### `locale`

The active locale is automatically prepended. `locale` allows for providing a different locale. When `false` `href` has to include the locale as the default behavior is disabled.

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <>
      {/* Default behavior: locale is prepended */}
      <Link href="/dashboard">Dashboard (with locale)</Link>

      {/* Disable locale prepending */}
      <Link href="/dashboard" locale={false}>
        Dashboard (without locale)
      </Link>

      {/* Specify a different locale */}
      <Link href="/dashboard" locale="fr">
        Dashboard (French)
      </Link>
    </>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <>
      {/* Default behavior: locale is prepended */}
      <Link href="/dashboard">Dashboard (with locale)</Link>

      {/* Disable locale prepending */}
      <Link href="/dashboard" locale={false}>
        Dashboard (without locale)
      </Link>

      {/* Specify a different locale */}
      <Link href="/dashboard" locale="fr">
        Dashboard (French)
      </Link>
    </>
  )
}
```

### `as`

Optional decorator for the path that will be shown in the browser URL bar. Before Next.js 9.5.3 this was used for dynamic routes, check our [previous docs](https://github.com/vercel/next.js/blob/v9.5.2/docs/api-reference/next/link.md#dynamic-routes) to see how it worked.

When this path differs from the one provided in `href` the previous `href`/`as` behavior is used as shown in the [previous docs](https://github.com/vercel/next.js/blob/v9.5.2/docs/api-reference/next/link.md#dynamic-routes).

### `onNavigate`

An event handler called during client-side navigation. The handler receives an event object that includes a `preventDefault()` method, allowing you to cancel the navigation if needed.

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link
      href="/dashboard"
      onNavigate={(e) => {
        // Only executes during SPA navigation
        console.log('Navigating...')

        // Optionally prevent navigation
        // e.preventDefault()
      }}
    >
      Dashboard
    </Link>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link
      href="/dashboard"
      onNavigate={(e) => {
        // Only executes during SPA navigation
        console.log('Navigating...')

        // Optionally prevent navigation
        // e.preventDefault()
      }}
    >
      Dashboard
    </Link>
  )
}
```

> **Good to know**: While `onClick` and `onNavigate` may seem similar, they serve different purposes. `onClick` executes for all click events, while `onNavigate` only runs during client-side navigation. Some key differences:
>
> * When using modifier keys (`Ctrl`/`Cmd` + Click), `onClick` executes but `onNavigate` doesn't since Next.js prevents default navigation for new tabs.
> * External URLs won't trigger `onNavigate` since it's only for client-side and same-origin navigations.
> * Links with the `download` attribute will work with `onClick` but not `onNavigate` since the browser will treat the linked URL as a download.

## Examples

The following examples demonstrate how to use the `<Link>` component in different scenarios.

### Linking to dynamic route segments

For [dynamic route segments](/docs/pages/building-your-application/routing/dynamic-routes.md#convention), it can be handy to use template literals to create the link's path.

For example, you can generate a list of links to the dynamic route `pages/blog/[slug].js`

```tsx filename="pages/blog/index.tsx" switcher
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}
```

```jsx filename="pages/blog/index.js" switcher
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}

export default Posts
```

### Scrolling to an `id`

If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `<Link>` renders to an `<a>` element.

```jsx
<Link href="/dashboard#settings">Settings</Link>

// Output
<a href="/dashboard#settings">Settings</a>
```

### Passing a URL Object

`Link` can also receive a URL object and it will automatically format it to create the URL string:

```tsx filename="pages/index.ts" switcher
import Link from 'next/link'

function Home() {
  return (
    <ul>
      <li>
        <Link
          href={{
            pathname: '/about',
            query: { name: 'test' },
          }}
        >
          About us
        </Link>
      </li>
      <li>
        <Link
          href={{
            pathname: '/blog/[slug]',
            query: { slug: 'my-post' },
          }}
        >
          Blog Post
        </Link>
      </li>
    </ul>
  )
}

export default Home
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

function Home() {
  return (
    <ul>
      <li>
        <Link
          href={{
            pathname: '/about',
            query: { name: 'test' },
          }}
        >
          About us
        </Link>
      </li>
      <li>
        <Link
          href={{
            pathname: '/blog/[slug]',
            query: { slug: 'my-post' },
          }}
        >
          Blog Post
        </Link>
      </li>
    </ul>
  )
}

export default Home
```

The above example has a link to:

* A predefined route: `/about?name=test`
* A [dynamic route](/docs/pages/building-your-application/routing/dynamic-routes.md#convention): `/blog/my-post`

You can use every property as defined in the [Node.js URL module documentation](https://nodejs.org/api/url.html#url_url_strings_and_url_objects).

### Replace the URL instead of push

The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:

```tsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

### Disable scrolling to the top of the page

The default behavior of `Link` is to scroll to the top of the page. When there is a hash defined it will scroll to the specific id, like a normal `<a>` tag. To prevent scrolling to the top / hash `scroll={false}` can be added to `Link`:

```jsx filename="pages/index.js" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

```tsx filename="pages/index.tsx" switcher
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

### Prefetching links in Proxy

It's common to use [Proxy](/docs/app/api-reference/file-conventions/proxy.md) for authentication or other purposes that involve rewriting the user to a different page. In order for the `<Link />` component to properly prefetch links with rewrites via Proxy, you need to tell Next.js both the URL to display and the URL to prefetch. This is required to avoid un-necessary fetches to proxy to know the correct route to prefetch.

For example, if you want to serve a `/dashboard` route that has authenticated and visitor views, you can add the following in your Proxy to redirect the user to the correct page:

```ts filename="proxy.ts" switcher
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  const nextUrl = request.nextUrl
  if (nextUrl.pathname === '/dashboard') {
    if (request.cookies.authToken) {
      return NextResponse.rewrite(new URL('/auth/dashboard', request.url))
    } else {
      return NextResponse.rewrite(new URL('/public/dashboard', request.url))
    }
  }
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  const nextUrl = request.nextUrl
  if (nextUrl.pathname === '/dashboard') {
    if (request.cookies.authToken) {
      return NextResponse.rewrite(new URL('/auth/dashboard', request.url))
    } else {
      return NextResponse.rewrite(new URL('/public/dashboard', request.url))
    }
  }
}
```

In this case, you would want to use the following code in your `<Link />` component:

```tsx filename="pages/index.tsx" switcher
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Home() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

```js filename="pages/index.js" switcher
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Home() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

> **Good to know**: If you're using [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md#convention), you'll need to adapt your `as` and `href` props. For example, if you have a Dynamic Route like `/dashboard/authed/[user]` that you want to present differently via proxy, you would write: `<Link href={{ pathname: '/dashboard/authed/[user]', query: { user: username } }} as="/dashboard/[user]">Profile</Link>`.

## Version history

| Version   | Changes                                                                                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v15.4.0` | Add `auto` as an alias to the default `prefetch` behavior.                                                                                                                   |
| `v15.3.0` | Add `onNavigate` API                                                                                                                                                         |
| `v13.0.0` | No longer requires a child `<a>` tag. A [codemod](/docs/app/guides/upgrading/codemods.md#remove-a-tags-from-link-components) is provided to automatically update your codebase. |
| `v10.0.0` | `href` props pointing to a dynamic route are automatically resolved and no longer require an `as` prop.                                                                      |
| `v8.0.0`  | Improved prefetching performance.                                                                                                                                            |
| `v1.0.0`  | `next/link` introduced.                                                                                                                                                      |


--------------------------------------------------------------------------------
title: "Script Component"
description: "Optimize third-party scripts in your Next.js application using the built-in `next/script` Component."
source: "https://nextjs.org/docs/pages/api-reference/components/script"
--------------------------------------------------------------------------------

# Script

@router: Pages Router

This API reference will help you understand how to use [props](#props) available for the Script Component. For features and usage, please see the [Optimizing Scripts](/docs/app/guides/scripts.md) page.

```tsx filename="app/dashboard/page.tsx" switcher
import Script from 'next/script'

export default function Dashboard() {
  return (
    <>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import Script from 'next/script'

export default function Dashboard() {
  return (
    <>
      <Script src="https://example.com/script.js" />
    </>
  )
}
```

## Props

Here's a summary of the props available for the Script Component:

| Prop                    | Example                           | Type     | Required                              |
| ----------------------- | --------------------------------- | -------- | ------------------------------------- |
| [`src`](#src)           | `src="http://example.com/script"` | String   | Required unless inline script is used |
| [`strategy`](#strategy) | `strategy="lazyOnload"`           | String   | -                                     |
| [`onLoad`](#onload)     | `onLoad={onLoadFunc}`             | Function | -                                     |
| [`onReady`](#onready)   | `onReady={onReadyFunc}`           | Function | -                                     |
| [`onError`](#onerror)   | `onError={onErrorFunc}`           | Function | -                                     |

## Required Props

The `<Script />` component requires the following properties.

### `src`

A path string specifying the URL of an external script. This can be either an absolute external URL or an internal path. The `src` property is required unless an inline script is used.

## Optional Props

The `<Script />` component accepts a number of additional properties beyond those which are required.

### `strategy`

The loading strategy of the script. There are four different strategies that can be used:

* `beforeInteractive`: Load before any Next.js code and before any page hydration occurs.
* `afterInteractive`: (**default**) Load early but after some hydration on the page occurs.
* `lazyOnload`: Load during browser idle time.
* `worker`: (experimental) Load in a web worker.

### `beforeInteractive`

Scripts that load with the `beforeInteractive` strategy are injected into the initial HTML from the server, downloaded before any Next.js module, and executed in the order they are placed.

Scripts denoted with this strategy are preloaded and fetched before any first-party code, but their execution **does not block page hydration from occurring**.

`beforeInteractive` scripts must be placed inside the `Document` Component (`pages/_document.js`) and are designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server-side).

**This strategy should only be used for critical scripts that need to be fetched as soon as possible.**

```jsx filename="pages/_document.js"
import { Html, Head, Main, NextScript } from 'next/document'
import Script from 'next/script'

export default function Document() {
  return (
    <Html>
      <Head />
      <body>
        <Main />
        <NextScript />
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        />
      </body>
    </Html>
  )
}
```

> **Good to know**: Scripts with `beforeInteractive` will always be injected inside the `head` of the HTML document regardless of where it's placed in the component.

Some examples of scripts that should be fetched as soon as possible with `beforeInteractive` include:

* Bot detectors
* Cookie consent managers

### `afterInteractive`

Scripts that use the `afterInteractive` strategy are injected into the HTML client-side and will load after some (or all) hydration occurs on the page. **This is the default strategy** of the Script component and should be used for any script that needs to load as soon as possible but not before any first-party Next.js code.

`afterInteractive` scripts can be placed inside of any page or layout and will only load and execute when that page (or group of pages) is opened in the browser.

```jsx filename="app/page.js"
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="afterInteractive" />
    </>
  )
}
```

Some examples of scripts that are good candidates for `afterInteractive` include:

* Tag managers
* Analytics

### `lazyOnload`

Scripts that use the `lazyOnload` strategy are injected into the HTML client-side during browser idle time and will load after all resources on the page have been fetched. This strategy should be used for any background or low priority scripts that do not need to load early.

`lazyOnload` scripts can be placed inside of any page or layout and will only load and execute when that page (or group of pages) is opened in the browser.

```jsx filename="app/page.js"
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script src="https://example.com/script.js" strategy="lazyOnload" />
    </>
  )
}
```

Examples of scripts that do not need to load immediately and can be fetched with `lazyOnload` include:

* Chat support plugins
* Social media widgets

### `worker`

> **Warning:** The `worker` strategy is not yet stable and does not yet work with the App Router. Use with caution.

Scripts that use the `worker` strategy are off-loaded to a web worker in order to free up the main thread and ensure that only critical, first-party resources are processed on it. While this strategy can be used for any script, it is an advanced use case that is not guaranteed to support all third-party scripts.

To use `worker` as a strategy, the `nextScriptWorkers` flag must be enabled in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  experimental: {
    nextScriptWorkers: true,
  },
}
```

`worker` scripts can **only currently be used in the `pages/` directory**:

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

### `onLoad`

> **Warning:** `onLoad` does not yet work with Server Components and can only be used in Client Components. Further, `onLoad` can't be used with `beforeInteractive` – consider using `onReady` instead.

Some third-party scripts require users to run JavaScript code once after the script has finished loading in order to instantiate content or call a function. If you are loading a script with either `afterInteractive` or `lazyOnload` as a loading strategy, you can execute code after it has loaded using the `onLoad` property.

Here's an example of executing a lodash method only after the library has been loaded.

```tsx filename="app/page.tsx" switcher
'use client'

import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"
        onLoad={() => {
          console.log(_.sample([1, 2, 3, 4]))
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
        src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.20/lodash.min.js"
        onLoad={() => {
          console.log(_.sample([1, 2, 3, 4]))
        }}
      />
    </>
  )
}
```

### `onReady`

> **Warning:** `onReady` does not yet work with Server Components and can only be used in Client Components.

Some third-party scripts require users to run JavaScript code after the script has finished loading and every time the component is mounted (after a route navigation for example). You can execute code after the script's load event when it first loads and then after every subsequent component re-mount using the `onReady` property.

Here's an example of how to re-instantiate a Google Maps JS embed every time the component is mounted:

```jsx
import { useRef } from 'react'
import Script from 'next/script'

export default function Page() {
  const mapRef = useRef()

  return (
    <>
      <div ref={mapRef}></div>
      <Script
        id="google-maps"
        src="https://maps.googleapis.com/maps/api/js"
        onReady={() => {
          new google.maps.Map(mapRef.current, {
            center: { lat: -34.397, lng: 150.644 },
            zoom: 8,
          })
        }}
      />
    </>
  )
}
```

### `onError`

> **Warning:** `onError` does not yet work with Server Components and can only be used in Client Components. `onError` cannot be used with the `beforeInteractive` loading strategy.

Sometimes it is helpful to catch when a script fails to load. These errors can be handled with the `onError` property:

```jsx
import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onError={(e: Error) => {
          console.error('Script failed to load', e)
        }}
      />
    </>
  )
}
```

## Version History

| Version   | Changes                                                                   |
| --------- | ------------------------------------------------------------------------- |
| `v13.0.0` | `beforeInteractive` and `afterInteractive` is modified to support `app`.  |
| `v12.2.4` | `onReady` prop added.                                                     |
| `v12.2.2` | Allow `next/script` with `beforeInteractive` to be placed in `_document`. |
| `v11.0.0` | `next/script` introduced.                                                 |


--------------------------------------------------------------------------------
title: "File-system conventions"
description: "API Reference for Next.js file-system conventions."
source: "https://nextjs.org/docs/pages/api-reference/file-conventions"
--------------------------------------------------------------------------------

# File-system conventions

@router: Pages Router



 - [instrumentation.js](/docs/pages/api-reference/file-conventions/instrumentation.md)
 - [Proxy](/docs/pages/api-reference/file-conventions/proxy.md)
 - [public](/docs/pages/api-reference/file-conventions/public-folder.md)
 - [src Directory](/docs/pages/api-reference/file-conventions/src-folder.md)

--------------------------------------------------------------------------------
title: "instrumentation.js"
description: "API reference for the instrumentation.js file."
source: "https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./14-static-exports.md) | [Index](./index.md) | [Next →](./16-instrumentationjs.md)
