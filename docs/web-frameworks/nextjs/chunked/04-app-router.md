**Navigation:** [← Previous](./03-content-security-policy.md) | [Index](./index.md) | [Next →](./05-scripts.md)

---

# App Router

This guide will help you:

* [Update your Next.js application from version 12 to version 13](#nextjs-version)
* [Upgrade features that work in both the `pages` and the `app` directories](#upgrading-new-features)
* [Incrementally migrate your existing application from `pages` to `app`](#migrating-from-pages-to-app)

## Upgrading

### Node.js Version

The minimum Node.js version is now **v18.17**. See the [Node.js documentation](https://nodejs.org/docs/latest-v18.x/api/) for more information.

### Next.js Version

To update to Next.js version 13, run the following command using your preferred package manager:

```bash filename="Terminal"
npm install next@latest react@latest react-dom@latest
```

### ESLint Version

If you're using ESLint, you need to upgrade your ESLint version:

```bash filename="Terminal"
npm install -D eslint-config-next@latest
```

> **Good to know**: You may need to restart the ESLint server in VS Code for the ESLint changes to take effect. Open the Command Palette (`cmd+shift+p` on Mac; `ctrl+shift+p` on Windows) and search for `ESLint: Restart ESLint Server`.

## Next Steps

After you've updated, see the following sections for next steps:

* [Upgrade new features](#upgrading-new-features): A guide to help you upgrade to new features such as the improved Image and Link Components.
* [Migrate from the `pages` to `app` directory](#migrating-from-pages-to-app): A step-by-step guide to help you incrementally migrate from the `pages` to the `app` directory.

## Upgrading New Features

Next.js 13 introduced the new [App Router](/docs/app.md) with new features and conventions. The new Router is available in the `app` directory and co-exists with the `pages` directory.

Upgrading to Next.js 13 does **not** require using the App Router. You can continue using `pages` with new features that work in both directories, such as the updated [Image component](#image-component), [Link component](#link-component), [Script component](#script-component), and [Font optimization](#font-optimization).

### `<Image/>` Component

Next.js 12 introduced new improvements to the Image Component with a temporary import: `next/future/image`. These improvements included less client-side JavaScript, easier ways to extend and style images, better accessibility, and native browser lazy loading.

In version 13, this new behavior is now the default for `next/image`.

There are two codemods to help you migrate to the new Image Component:

* [**`next-image-to-legacy-image` codemod**](/docs/app/guides/upgrading/codemods.md#next-image-to-legacy-image): Safely and automatically renames `next/image` imports to `next/legacy/image`. Existing components will maintain the same behavior.
* [**`next-image-experimental` codemod**](/docs/app/guides/upgrading/codemods.md#next-image-experimental): Dangerously adds inline styles and removes unused props. This will change the behavior of existing components to match the new defaults. To use this codemod, you need to run the `next-image-to-legacy-image` codemod first.

### `<Link>` Component

The [`<Link>` Component](/docs/app/api-reference/components/link.md) no longer requires manually adding an `<a>` tag as a child. This behavior was added as an experimental option in [version 12.2](https://nextjs.org/blog/next-12-2) and is now the default. In Next.js 13, `<Link>` always renders `<a>` and allows you to forward props to the underlying tag.

For example:

```jsx
import Link from 'next/link'

// Next.js 12: `<a>` has to be nested otherwise it's excluded
<Link href="/about">
  <a>About</a>
</Link>

// Next.js 13: `<Link>` always renders `<a>` under the hood
<Link href="/about">
  About
</Link>
```

To upgrade your links to Next.js 13, you can use the [`new-link` codemod](/docs/app/guides/upgrading/codemods.md#new-link).

### `<Script>` Component

The behavior of [`next/script`](/docs/app/api-reference/components/script.md) has been updated to support both `pages` and `app`, but some changes need to be made to ensure a smooth migration:

* Move any `beforeInteractive` scripts you previously included in `_document.js` to the root layout file (`app/layout.tsx`).
* The experimental `worker` strategy does not yet work in `app` and scripts denoted with this strategy will either have to be removed or modified to use a different strategy (e.g. `lazyOnload`).
* `onLoad`, `onReady`, and `onError` handlers will not work in Server Components so make sure to move them to a [Client Component](/docs/app/getting-started/server-and-client-components.md) or remove them altogether.

### Font Optimization

Previously, Next.js helped you optimize fonts by [inlining font CSS](/docs/app/api-reference/components/font.md). Version 13 introduces the new [`next/font`](/docs/app/api-reference/components/font.md) module which gives you the ability to customize your font loading experience while still ensuring great performance and privacy. `next/font` is supported in both the `pages` and `app` directories.

While [inlining CSS](/docs/app/api-reference/components/font.md) still works in `pages`, it does not work in `app`. You should use [`next/font`](/docs/app/api-reference/components/font.md) instead.

See the [Font Optimization](/docs/app/api-reference/components/font.md) page to learn how to use `next/font`.

## Migrating from `pages` to `app`

> **🎥 Watch:** Learn how to incrementally adopt the App Router → [YouTube (16 minutes)](https://www.youtube.com/watch?v=YQMSietiFm0).

Moving to the App Router may be the first time using React features that Next.js builds on top of such as Server Components, Suspense, and more. When combined with new Next.js features such as [special files](/docs/app/api-reference/file-conventions.md) and [layouts](/docs/app/api-reference/file-conventions/layout.md), migration means new concepts, mental models, and behavioral changes to learn.

We recommend reducing the combined complexity of these updates by breaking down your migration into smaller steps. The `app` directory is intentionally designed to work simultaneously with the `pages` directory to allow for incremental page-by-page migration.

* The `app` directory supports nested routes *and* layouts. [Learn more](/docs/app/getting-started/layouts-and-pages.md).
* Use nested folders to define routes and a special `page.js` file to make a route segment publicly accessible. [Learn more](#step-4-migrating-pages).
* [Special file conventions](/docs/app/api-reference/file-conventions.md) are used to create UI for each route segment. The most common special files are `page.js` and `layout.js`.
  * Use `page.js` to define UI unique to a route.
  * Use `layout.js` to define UI that is shared across multiple routes.
  * `.js`, `.jsx`, or `.tsx` file extensions can be used for special files.
* You can colocate other files inside the `app` directory such as components, styles, tests, and more. [Learn more](/docs/app.md).
* Data fetching functions like `getServerSideProps` and `getStaticProps` have been replaced with [a new API](/docs/app/getting-started/fetching-data.md) inside `app`. `getStaticPaths` has been replaced with [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md).
* `pages/_app.js` and `pages/_document.js` have been replaced with a single `app/layout.js` root layout. [Learn more](/docs/app/api-reference/file-conventions/layout.md#root-layout).
* `pages/_error.js` has been replaced with more granular `error.js` special files. [Learn more](/docs/app/getting-started/error-handling.md).
* `pages/404.js` has been replaced with the [`not-found.js`](/docs/app/api-reference/file-conventions/not-found.md) file.
* `pages/api/*` API Routes have been replaced with the [`route.js`](/docs/app/api-reference/file-conventions/route.md) (Route Handler) special file.

### Step 1: Creating the `app` directory

Update to the latest Next.js version (requires 13.4 or greater):

```bash
npm install next@latest
```

Then, create a new `app` directory at the root of your project (or `src/` directory).

### Step 2: Creating a Root Layout

Create a new `app/layout.tsx` file inside the `app` directory. This is a [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) that will apply to all routes inside `app`.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  // Layouts must accept a children prop.
  // This will be populated with nested layouts or pages
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
export default function RootLayout({
  // Layouts must accept a children prop.
  // This will be populated with nested layouts or pages
  children,
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

* The `app` directory **must** include a root layout.
* The root layout must define `<html>`, and `<body>` tags since Next.js does not automatically create them
* The root layout replaces the `pages/_app.tsx` and `pages/_document.tsx` files.
* `.js`, `.jsx`, or `.tsx` extensions can be used for layout files.

To manage `<head>` HTML elements, you can use the [built-in SEO support](/docs/app/getting-started/metadata-and-og-images.md):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Home',
  description: 'Welcome to Next.js',
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'Home',
  description: 'Welcome to Next.js',
}
```

#### Migrating `_document.js` and `_app.js`

If you have an existing `_app` or `_document` file, you can copy the contents (e.g. global styles) to the root layout (`app/layout.tsx`). Styles in `app/layout.tsx` will *not* apply to `pages/*`. You should keep `_app`/`_document` while migrating to prevent your `pages/*` routes from breaking. Once fully migrated, you can then safely delete them.

If you are using any React Context providers, they will need to be moved to a [Client Component](/docs/app/getting-started/server-and-client-components.md).

#### Migrating the `getLayout()` pattern to Layouts (Optional)

Next.js recommended adding a [property to Page components](/docs/pages/building-your-application/routing/pages-and-layouts.md#layout-pattern) to achieve per-page layouts in the `pages` directory. This pattern can be replaced with native support for [nested layouts](/docs/app/api-reference/file-conventions/layout.md) in the `app` directory.

<details>
<summary>See before and after example</summary>

**Before**

```jsx filename="components/DashboardLayout.js"
export default function DashboardLayout({ children }) {
  return (
    <div>
      <h2>My Dashboard</h2>
      {children}
    </div>
  )
}
```

```jsx filename="pages/dashboard/index.js"
import DashboardLayout from '../components/DashboardLayout'

export default function Page() {
  return <p>My Page</p>
}

Page.getLayout = function getLayout(page) {
  return <DashboardLayout>{page}</DashboardLayout>
}
```

**After**

* Remove the `Page.getLayout` property from `pages/dashboard/index.js` and follow the [steps for migrating pages](#step-4-migrating-pages) to the `app` directory.

  ```jsx filename="app/dashboard/page.js"
  export default function Page() {
    return <p>My Page</p>
  }
  ```

* Move the contents of `DashboardLayout` into a new [Client Component](/docs/app/getting-started/server-and-client-components.md) to retain `pages` directory behavior.

  ```jsx filename="app/dashboard/DashboardLayout.js"
  'use client' // this directive should be at top of the file, before any imports.

  // This is a Client Component
  export default function DashboardLayout({ children }) {
    return (
      <div>
        <h2>My Dashboard</h2>
        {children}
      </div>
    )
  }
  ```

* Import the `DashboardLayout` into a new `layout.js` file inside the `app` directory.

  ```jsx filename="app/dashboard/layout.js"
  import DashboardLayout from './DashboardLayout'

  // This is a Server Component
  export default function Layout({ children }) {
    return <DashboardLayout>{children}</DashboardLayout>
  }
  ```

* You can incrementally move non-interactive parts of `DashboardLayout.js` (Client Component) into `layout.js` (Server Component) to reduce the amount of component JavaScript you send to the client.

</details>

### Step 3: Migrating `next/head`

In the `pages` directory, the `next/head` React component is used to manage `<head>` HTML elements such as `title` and `meta` . In the `app` directory, `next/head` is replaced with the new [built-in SEO support](/docs/app/getting-started/metadata-and-og-images.md).

**Before:**

```tsx filename="pages/index.tsx" switcher
import Head from 'next/head'

export default function Page() {
  return (
    <>
      <Head>
        <title>My page title</title>
      </Head>
    </>
  )
}
```

```jsx filename="pages/index.js" switcher
import Head from 'next/head'

export default function Page() {
  return (
    <>
      <Head>
        <title>My page title</title>
      </Head>
    </>
  )
}
```

**After:**

```tsx filename="app/page.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My Page Title',
}

export default function Page() {
  return '...'
}
```

```jsx filename="app/page.js" switcher
export const metadata = {
  title: 'My Page Title',
}

export default function Page() {
  return '...'
}
```

[See all metadata options](/docs/app/api-reference/functions/generate-metadata.md).

### Step 4: Migrating Pages

* Pages in the [`app` directory](/docs/app.md) are [Server Components](/docs/app/getting-started/server-and-client-components.md) by default. This is different from the `pages` directory where pages are [Client Components](/docs/app/getting-started/server-and-client-components.md).
* [Data fetching](/docs/app/getting-started/fetching-data.md) has changed in `app`. `getServerSideProps`, `getStaticProps` and `getInitialProps` have been replaced with a simpler API.
* The `app` directory uses nested folders to define routes and a special `page.js` file to make a route segment publicly accessible.
* | `pages` Directory | `app` Directory       | Route          |
  | ----------------- | --------------------- | -------------- |
  | `index.js`        | `page.js`             | `/`            |
  | `about.js`        | `about/page.js`       | `/about`       |
  | `blog/[slug].js`  | `blog/[slug]/page.js` | `/blog/post-1` |

We recommend breaking down the migration of a page into two main steps:

* Step 1: Move the default exported Page Component into a new Client Component.
* Step 2: Import the new Client Component into a new `page.js` file inside the `app` directory.

> **Good to know**: This is the easiest migration path because it has the most comparable behavior to the `pages` directory.

**Step 1: Create a new Client Component**

* Create a new separate file inside the `app` directory (i.e. `app/home-page.tsx` or similar) that exports a Client Component. To define Client Components, add the `'use client'` directive to the top of the file (before any imports).
  * Similar to the Pages Router, there is an [optimization step](/docs/app/getting-started/server-and-client-components.md#on-the-client-first-load) to prerender Client Components to static HTML on the initial page load.
* Move the default exported page component from `pages/index.js` to `app/home-page.tsx`.

```tsx filename="app/home-page.tsx" switcher
'use client'

// This is a Client Component (same as components in the `pages` directory)
// It receives data as props, has access to state and effects, and is
// prerendered on the server during the initial page load.
export default function HomePage({ recentPosts }) {
  return (
    <div>
      {recentPosts.map((post) => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  )
}
```

```jsx filename="app/home-page.js" switcher
'use client'

// This is a Client Component. It receives data as props and
// has access to state and effects just like Page components
// in the `pages` directory.
export default function HomePage({ recentPosts }) {
  return (
    <div>
      {recentPosts.map((post) => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  )
}
```

**Step 2: Create a new page**

* Create a new `app/page.tsx` file inside the `app` directory. This is a Server Component by default.

* Import the `home-page.tsx` Client Component into the page.

* If you were fetching data in `pages/index.js`, move the data fetching logic directly into the Server Component using the new [data fetching APIs](/docs/app/getting-started/fetching-data.md). See the [data fetching upgrade guide](#step-6-migrating-data-fetching-methods) for more details.

  ```tsx filename="app/page.tsx" switcher
  // Import your Client Component
  import HomePage from './home-page'

  async function getPosts() {
    const res = await fetch('https://...')
    const posts = await res.json()
    return posts
  }

  export default async function Page() {
    // Fetch data directly in a Server Component
    const recentPosts = await getPosts()
    // Forward fetched data to your Client Component
    return <HomePage recentPosts={recentPosts} />
  }
  ```

  ```jsx filename="app/page.js" switcher
  // Import your Client Component
  import HomePage from './home-page'

  async function getPosts() {
    const res = await fetch('https://...')
    const posts = await res.json()
    return posts
  }

  export default async function Page() {
    // Fetch data directly in a Server Component
    const recentPosts = await getPosts()
    // Forward fetched data to your Client Component
    return <HomePage recentPosts={recentPosts} />
  }
  ```

* If your previous page used `useRouter`, you'll need to update to the new routing hooks. [Learn more](/docs/app/api-reference/functions/use-router.md).

* Start your development server and visit [`http://localhost:3000`](http://localhost:3000). You should see your existing index route, now served through the app directory.

### Step 5: Migrating Routing Hooks

A new router has been added to support the new behavior in the `app` directory.

In `app`, you should use the three new hooks imported from `next/navigation`: [`useRouter()`](/docs/app/api-reference/functions/use-router.md), [`usePathname()`](/docs/app/api-reference/functions/use-pathname.md), and [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md).

* The new `useRouter` hook is imported from `next/navigation` and has different behavior to the `useRouter` hook in `pages` which is imported from `next/router`.
  * The [`useRouter` hook imported from `next/router`](/docs/pages/api-reference/functions/use-router.md) is not supported in the `app` directory but can continue to be used in the `pages` directory.
* The new `useRouter` does not return the `pathname` string. Use the separate `usePathname` hook instead.
* The new `useRouter` does not return the `query` object. Search parameters and dynamic route parameters are now separate. Use the `useSearchParams` and `useParams` hooks instead.
* You can use `useSearchParams` and `usePathname` together to listen to page changes. See the [Router Events](/docs/app/api-reference/functions/use-router.md#router-events) section for more details.
* These new hooks are only supported in Client Components. They cannot be used in Server Components.

```tsx filename="app/example-client-component.tsx" switcher
'use client'

import { useRouter, usePathname, useSearchParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // ...
}
```

```jsx filename="app/example-client-component.js" switcher
'use client'

import { useRouter, usePathname, useSearchParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const router = useRouter()
  const pathname = usePathname()
  const searchParams = useSearchParams()

  // ...
}
```

In addition, the new `useRouter` hook has the following changes:

* `isFallback` has been removed because `fallback` has [been replaced](#replacing-fallback).
* The `locale`, `locales`, `defaultLocales`, `domainLocales` values have been removed because built-in i18n Next.js features are no longer necessary in the `app` directory. [Learn more about i18n](/docs/app/guides/internationalization.md).
* `basePath` has been removed. The alternative will not be part of `useRouter`. It has not yet been implemented.
* `asPath` has been removed because the concept of `as` has been removed from the new router.
* `isReady` has been removed because it is no longer necessary. During [static rendering](/docs/app/guides/caching.md#static-rendering), any component that uses the [`useSearchParams()`](/docs/app/api-reference/functions/use-search-params.md) hook will skip the prerendering step and instead be rendered on the client at runtime.
* `route` has been removed. `usePathname` or `useSelectedLayoutSegments()` provide an alternative.

[View the `useRouter()` API reference](/docs/app/api-reference/functions/use-router.md).

#### Sharing components between `pages` and `app`

To keep components compatible between the `pages` and `app` routers, refer to the [`useRouter` hook from `next/compat/router`](/docs/pages/api-reference/functions/use-router.md#the-nextcompatrouter-export).
This is the `useRouter` hook from the `pages` directory, but intended to be used while sharing components between routers. Once you are ready to use it only on the `app` router, update to the new [`useRouter` from `next/navigation`](/docs/app/api-reference/functions/use-router.md).

### Step 6: Migrating Data Fetching Methods

The `pages` directory uses `getServerSideProps` and `getStaticProps` to fetch data for pages. Inside the `app` directory, these previous data fetching functions are replaced with a [simpler API](/docs/app/getting-started/fetching-data.md) built on top of `fetch()` and `async` React Server Components.

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  // This request should be cached until manually invalidated.
  // Similar to `getStaticProps`.
  // `force-cache` is the default and can be omitted.
  const staticData = await fetch(`https://...`, { cache: 'force-cache' })

  // This request should be refetched on every request.
  // Similar to `getServerSideProps`.
  const dynamicData = await fetch(`https://...`, { cache: 'no-store' })

  // This request should be cached with a lifetime of 10 seconds.
  // Similar to `getStaticProps` with the `revalidate` option.
  const revalidatedData = await fetch(`https://...`, {
    next: { revalidate: 10 },
  })

  return <div>...</div>
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  // This request should be cached until manually invalidated.
  // Similar to `getStaticProps`.
  // `force-cache` is the default and can be omitted.
  const staticData = await fetch(`https://...`, { cache: 'force-cache' })

  // This request should be refetched on every request.
  // Similar to `getServerSideProps`.
  const dynamicData = await fetch(`https://...`, { cache: 'no-store' })

  // This request should be cached with a lifetime of 10 seconds.
  // Similar to `getStaticProps` with the `revalidate` option.
  const revalidatedData = await fetch(`https://...`, {
    next: { revalidate: 10 },
  })

  return <div>...</div>
}
```

#### Server-side Rendering (`getServerSideProps`)

In the `pages` directory, `getServerSideProps` is used to fetch data on the server and forward props to the default exported React component in the file. The initial HTML for the page is prerendered from the server, followed by "hydrating" the page in the browser (making it interactive).

```jsx filename="pages/dashboard.js"
// `pages` directory

export async function getServerSideProps() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return { props: { projects } }
}

export default function Dashboard({ projects }) {
  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

In the App Router, we can colocate our data fetching inside our React components using [Server Components](/docs/app/getting-started/server-and-client-components.md). This allows us to send less JavaScript to the client, while maintaining the rendered HTML from the server.

By setting the `cache` option to `no-store`, we can indicate that the fetched data should [never be cached](/docs/app/getting-started/fetching-data.md). This is similar to `getServerSideProps` in the `pages` directory.

```tsx filename="app/dashboard/page.tsx" switcher
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`, { cache: 'no-store' })
  const projects = await res.json()

  return projects
}

export default async function Dashboard() {
  const projects = await getProjects()

  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`, { cache: 'no-store' })
  const projects = await res.json()

  return projects
}

export default async function Dashboard() {
  const projects = await getProjects()

  return (
    <ul>
      {projects.map((project) => (
        <li key={project.id}>{project.name}</li>
      ))}
    </ul>
  )
}
```

#### Accessing Request Object

In the `pages` directory, you can retrieve request-based data based on the Node.js HTTP API.

For example, you can retrieve the `req` object from `getServerSideProps` and use it to retrieve the request's cookies and headers.

```jsx filename="pages/index.js"
// `pages` directory

export async function getServerSideProps({ req, query }) {
  const authHeader = req.getHeaders()['authorization'];
  const theme = req.cookies['theme'];

  return { props: { ... }}
}

export default function Page(props) {
  return ...
}
```

The `app` directory exposes new read-only functions to retrieve request data:

* [`headers`](/docs/app/api-reference/functions/headers.md): Based on the Web Headers API, and can be used inside [Server Components](/docs/app/getting-started/server-and-client-components.md) to retrieve request headers.
* [`cookies`](/docs/app/api-reference/functions/cookies.md): Based on the Web Cookies API, and can be used inside [Server Components](/docs/app/getting-started/server-and-client-components.md) to retrieve cookies.

```tsx filename="app/page.tsx" switcher
// `app` directory
import { cookies, headers } from 'next/headers'

async function getData() {
  const authHeader = (await headers()).get('authorization')

  return '...'
}

export default async function Page() {
  // You can use `cookies` or `headers` inside Server Components
  // directly or in your data fetching function
  const theme = (await cookies()).get('theme')
  const data = await getData()
  return '...'
}
```

```jsx filename="app/page.js" switcher
// `app` directory
import { cookies, headers } from 'next/headers'

async function getData() {
  const authHeader = (await headers()).get('authorization')

  return '...'
}

export default async function Page() {
  // You can use `cookies` or `headers` inside Server Components
  // directly or in your data fetching function
  const theme = (await cookies()).get('theme')
  const data = await getData()
  return '...'
}
```

#### Static Site Generation (`getStaticProps`)

In the `pages` directory, the `getStaticProps` function is used to pre-render a page at build time. This function can be used to fetch data from an external API or directly from a database, and pass this data down to the entire page as it's being generated during the build.

```jsx filename="pages/index.js"
// `pages` directory

export async function getStaticProps() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return { props: { projects } }
}

export default function Index({ projects }) {
  return projects.map((project) => <div>{project.name}</div>)
}
```

In the `app` directory, data fetching with [`fetch()`](/docs/app/api-reference/functions/fetch.md) will default to `cache: 'force-cache'`, which will cache the request data until manually invalidated. This is similar to `getStaticProps` in the `pages` directory.

```jsx filename="app/page.js"
// `app` directory

// This function can be named anything
async function getProjects() {
  const res = await fetch(`https://...`)
  const projects = await res.json()

  return projects
}

export default async function Index() {
  const projects = await getProjects()

  return projects.map((project) => <div>{project.name}</div>)
}
```

#### Dynamic paths (`getStaticPaths`)

In the `pages` directory, the `getStaticPaths` function is used to define the dynamic paths that should be pre-rendered at build time.

```jsx filename="pages/posts/[id].js"
// `pages` directory
import PostLayout from '@/components/post-layout'

export async function getStaticPaths() {
  return {
    paths: [{ params: { id: '1' } }, { params: { id: '2' } }],
  }
}

export async function getStaticProps({ params }) {
  const res = await fetch(`https://.../posts/${params.id}`)
  const post = await res.json()

  return { props: { post } }
}

export default function Post({ post }) {
  return <PostLayout post={post} />
}
```

In the `app` directory, `getStaticPaths` is replaced with [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md).

[`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) behaves similarly to `getStaticPaths`, but has a simplified API for returning route parameters and can be used inside [layouts](/docs/app/api-reference/file-conventions/layout.md). The return shape of `generateStaticParams` is an array of segments instead of an array of nested `param` objects or a string of resolved paths.

```jsx filename="app/posts/[id]/page.js"
// `app` directory
import PostLayout from '@/components/post-layout'

export async function generateStaticParams() {
  return [{ id: '1' }, { id: '2' }]
}

async function getPost(params) {
  const res = await fetch(`https://.../posts/${(await params).id}`)
  const post = await res.json()

  return post
}

export default async function Post({ params }) {
  const post = await getPost(params)

  return <PostLayout post={post} />
}
```

Using the name `generateStaticParams` is more appropriate than `getStaticPaths` for the new model in the `app` directory. The `get` prefix is replaced with a more descriptive `generate`, which sits better alone now that `getStaticProps` and `getServerSideProps` are no longer necessary. The `Paths` suffix is replaced by `Params`, which is more appropriate for nested routing with multiple dynamic segments.

***

#### Replacing `fallback`

In the `pages` directory, the `fallback` property returned from `getStaticPaths` is used to define the behavior of a page that isn't pre-rendered at build time. This property can be set to `true` to show a fallback page while the page is being generated, `false` to show a 404 page, or `blocking` to generate the page at request time.

```jsx filename="pages/posts/[id].js"
// `pages` directory

export async function getStaticPaths() {
  return {
    paths: [],
    fallback: 'blocking'
  };
}

export async function getStaticProps({ params }) {
  ...
}

export default function Post({ post }) {
  return ...
}
```

In the `app` directory the [`config.dynamicParams` property](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) controls how params outside of [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) are handled:

* **`true`**: (default) Dynamic segments not included in `generateStaticParams` are generated on demand.
* **`false`**: Dynamic segments not included in `generateStaticParams` will return a 404.

This replaces the `fallback: true | false | 'blocking'` option of `getStaticPaths` in the `pages` directory. The `fallback: 'blocking'` option is not included in `dynamicParams` because the difference between `'blocking'` and `true` is negligible with streaming.

```jsx filename="app/posts/[id]/page.js"
// `app` directory

export const dynamicParams = true;

export async function generateStaticParams() {
  return [...]
}

async function getPost(params) {
  ...
}

export default async function Post({ params }) {
  const post = await getPost(params);

  return ...
}
```

With [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) set to `true` (the default), when a route segment is requested that hasn't been generated, it will be server-rendered and cached.

#### Incremental Static Regeneration (`getStaticProps` with `revalidate`)

In the `pages` directory, the `getStaticProps` function allows you to add a `revalidate` field to automatically regenerate a page after a certain amount of time.

```jsx filename="pages/index.js"
// `pages` directory

export async function getStaticProps() {
  const res = await fetch(`https://.../posts`)
  const posts = await res.json()

  return {
    props: { posts },
    revalidate: 60,
  }
}

export default function Index({ posts }) {
  return (
    <Layout>
      <PostList posts={posts} />
    </Layout>
  )
}
```

In the `app` directory, data fetching with [`fetch()`](/docs/app/api-reference/functions/fetch.md) can use `revalidate`, which will cache the request for the specified amount of seconds.

```jsx filename="app/page.js"
// `app` directory

async function getPosts() {
  const res = await fetch(`https://.../posts`, { next: { revalidate: 60 } })
  const data = await res.json()

  return data.posts
}

export default async function PostList() {
  const posts = await getPosts()

  return posts.map((post) => <div>{post.name}</div>)
}
```

#### API Routes

API Routes continue to work in the `pages/api` directory without any changes. However, they have been replaced by [Route Handlers](/docs/app/api-reference/file-conventions/route.md) in the `app` directory.

Route Handlers allow you to create custom request handlers for a given route using the Web [Request](https://developer.mozilla.org/docs/Web/API/Request) and [Response](https://developer.mozilla.org/docs/Web/API/Response) APIs.

```ts filename="app/api/route.ts" switcher
export async function GET(request: Request) {}
```

```js filename="app/api/route.js" switcher
export async function GET(request) {}
```

> **Good to know**: If you previously used API routes to call an external API from the client, you can now use [Server Components](/docs/app/getting-started/server-and-client-components.md) instead to securely fetch data. Learn more about [data fetching](/docs/app/getting-started/fetching-data.md).

#### Single-Page Applications

If you are also migrating to Next.js from a Single-Page Application (SPA) at the same time, see our [documentation](/docs/app/guides/single-page-applications.md) to learn more.

### Step 7: Styling

In the `pages` directory, global stylesheets are restricted to only `pages/_app.js`. With the `app` directory, this restriction has been lifted. Global styles can be added to any layout, page, or component.

* [CSS Modules](/docs/app/getting-started/css.md#css-modules)
* [Tailwind CSS](/docs/app/getting-started/css.md#tailwind-css)
* [Global Styles](/docs/app/getting-started/css.md#global-css)
* [CSS-in-JS](/docs/app/guides/css-in-js.md)
* [External Stylesheets](/docs/app/getting-started/css.md#external-stylesheets)
* [Sass](/docs/app/guides/sass.md)

#### Tailwind CSS

If you're using Tailwind CSS, you'll need to add the `app` directory to your `tailwind.config.js` file:

```js filename="tailwind.config.js"
module.exports = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}', // <-- Add this line
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
}
```

You'll also need to import your global styles in your `app/layout.js` file:

```jsx filename="app/layout.js"
import '../styles/globals.css'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

Learn more about [styling with Tailwind CSS](/docs/app/getting-started/css.md#tailwind-css)

## Using App Router together with Pages Router

When navigating between routes served by the different Next.js routers, there will be a hard navigation. Automatic link prefetching with `next/link` will not prefetch across routers.

Instead, you can [optimize navigations](https://vercel.com/guides/optimizing-hard-navigations) between App Router and Pages Router to retain the prefetched and fast page transitions. [Learn more](https://vercel.com/guides/optimizing-hard-navigations).

## Codemods

Next.js provides Codemod transformations to help upgrade your codebase when a feature is deprecated. See [Codemods](/docs/app/guides/upgrading/codemods.md) for more information.


--------------------------------------------------------------------------------
title: "How to migrate from Create React App to Next.js"
description: "Learn how to migrate your existing React application from Create React App to Next.js."
source: "https://nextjs.org/docs/app/guides/migrating/from-create-react-app"
--------------------------------------------------------------------------------

# Create React App

This guide will help you migrate an existing Create React App (CRA) site to Next.js.

## Why Switch?

There are several reasons why you might want to switch from Create React App to Next.js:

### Slow initial page loading time

Create React App uses purely client-side rendering. Client-side only applications, also known as [single-page applications (SPAs)](/docs/app/guides/single-page-applications.md), often experience slow initial page loading time. This happens due to a couple of reasons:

1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load data.
2. Your application code grows with every new feature and dependency you add.

### No automatic code splitting

The previous issue of slow loading times can be somewhat mitigated with code splitting. However, if you try to do code splitting manually, you can inadvertently introduce network waterfalls. Next.js provides automatic code splitting and tree-shaking built into its router and build pipeline.

### Network waterfalls

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One pattern for data fetching in a [SPA](/docs/app/guides/single-page-applications.md) is to render a placeholder, and then fetch data after the component has mounted. Unfortunately, a child component can only begin fetching data after its parent has finished loading its own data, resulting in a “waterfall” of requests.

While client-side data fetching is supported in Next.js, Next.js also lets you move data fetching to the server. This often eliminates client-server waterfalls altogether.

### Fast and intentional loading states

With built-in support for [streaming through React Suspense](/docs/app/getting-started/linking-and-navigating.md#streaming), you can define which parts of your UI load first and in what order, without creating network waterfalls.

This enables you to build pages that are faster to load and eliminate [layout shifts](https://vercel.com/blog/how-core-web-vitals-affect-seo).

### Choose the data fetching strategy

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page or component-level basis. For example, you could fetch data from your CMS and render blog posts at build time (SSG) for quick load speeds, or fetch data at request time (SSR) when necessary.

### Proxy

[Next.js Proxy](/docs/app/api-reference/file-conventions/proxy.md) allows you to run code on the server before a request is completed. For instance, you can avoid a flash of unauthenticated content by redirecting a user to a login page in the proxy for authenticated-only pages. You can also use it for features like A/B testing, experimentation, and [internationalization](/docs/app/guides/internationalization.md).

### Built-in Optimizations

[Images](/docs/app/api-reference/components/image.md), [fonts](/docs/app/api-reference/components/font.md), and [third-party scripts](/docs/app/guides/scripts.md) often have a large impact on an application’s performance. Next.js includes specialized components and APIs that automatically optimize them for you.

## Migration Steps

Our goal is to get a working Next.js application as quickly as possible so that you can then adopt Next.js features incrementally. To begin with, we’ll treat your application as a purely client-side application ([SPA](/docs/app/guides/single-page-applications.md)) without immediately replacing your existing router. This reduces complexity and merge conflicts.

> **Note**: If you are using advanced CRA configurations such as a custom `homepage` field in your `package.json`, a custom service worker, or specific Babel/webpack tweaks, please see the **Additional Considerations** section at the end of this guide for tips on replicating or adapting these features in Next.js.

### Step 1: Install the Next.js Dependency

Install Next.js in your existing project:

```bash filename="Terminal"
npm install next@latest
```

### Step 2: Create the Next.js Configuration File

Create a `next.config.ts` at the root of your project (same level as your `package.json`). This file holds your [Next.js configuration options](/docs/app/api-reference/config/next-config-js.md).

```js filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA)
  distDir: 'build', // Changes the build output directory to `build`
}

export default nextConfig
```

> **Note**: Using `output: 'export'` means you’re doing a static export. You will **not** have access to server-side features like SSR or APIs. You can remove this line to leverage Next.js server features.

### Step 3: Create the Root Layout

A Next.js [App Router](/docs/app.md) application must include a [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) file, which is a [React Server Component](/docs/app/getting-started/server-and-client-components.md) that will wrap all your pages.

The closest equivalent of the root layout file in a CRA application is `public/index.html`, which includes your `<html>`, `<head>`, and `<body>` tags.

1. Create a new `app` directory inside your `src` folder (or at your project root if you prefer `app` at the root).
2. Inside the `app` directory, create a `layout.tsx` (or `layout.js`) file:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return '...'
}
```

Now copy the content of your old `index.html` into this `<RootLayout>` component. Replace `body div#root` (and `body noscript`) with `<div id="root">{children}</div>`.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

> **Good to know**: Next.js ignores CRA’s `public/manifest.json`, additional iconography, and [testing configuration](/docs/app/guides/testing.md) by default. If you need these, Next.js has support with its [Metadata API](/docs/app/getting-started/metadata-and-og-images.md) and [Testing](/docs/app/guides/testing.md) setup.

### Step 4: Metadata

Next.js automatically includes the `<meta charset="UTF-8" />` and `<meta name="viewport" content="width=device-width, initial-scale=1" />` tags, so you can remove them from `<head>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Any [metadata files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata) such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application `<head>` tag as long as you have them placed into the top level of the `app` directory. After moving [all supported files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata) into the `app` directory you can safely delete their `<link>` tags:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Finally, Next.js can manage your last `<head>` tags with the [Metadata API](/docs/app/getting-started/metadata-and-og-images.md). Move your final metadata info into an exported [`metadata` object](/docs/app/api-reference/functions/generate-metadata.md#metadata-object):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js' convention-based approach built into the framework ([Metadata API](/docs/app/getting-started/metadata-and-og-images.md)). This approach enables you to more easily improve your SEO and web shareability of your pages.

### Step 5: Styles

Like CRA, Next.js supports [CSS Modules](/docs/app/getting-started/css.md#css-modules) out of the box. It also supports [global CSS imports](/docs/app/getting-started/css.md#global-css).

If you have a global CSS file, import it into your `app/layout.tsx`:

```tsx filename="app/layout.tsx" switcher
import '../index.css'

export const metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

If you're using Tailwind CSS, see our [installation docs](/docs/app/getting-started/css.md#tailwind-css).

### Step 6: Create the Entrypoint Page

Create React App uses `src/index.tsx` (or `index.js`) as the entry point. In Next.js (App Router), each folder inside the `app` directory corresponds to a route, and each folder should have a `page.tsx`.

Since we want to keep the app as an SPA for now and intercept **all** routes, we’ll use an [optional catch-all route](/docs/app/api-reference/file-conventions/dynamic-routes.md#optional-catch-all-segments).

1. **Create a `[[...slug]]` directory inside `app`.**

```bash
app
 ┣ [[...slug]]
 ┃ ┗ page.tsx
 ┣ layout.tsx
```

2. **Add the following to `page.tsx`**:

```tsx filename="app/[[...slug]]/page.tsx" switcher
export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

This tells Next.js to generate a single route for the empty slug (`/`), effectively mapping **all** routes to the same page. This page is a [Server Component](/docs/app/getting-started/server-and-client-components.md), prerendered into static HTML.

### Step 7: Add a Client-Only Entrypoint

Next, we’ll embed your CRA’s root App component inside a [Client Component](/docs/app/getting-started/server-and-client-components.md) so that all logic remains client-side. If this is your first time using Next.js, it's worth knowing that clients components (by default) are still prerendered on the server. You can think about them as having the additional capability of running client-side JavaScript.

Create a `client.tsx` (or `client.js`) in `app/[[...slug]]/`:

```tsx filename="app/[[...slug]]/client.tsx" switcher
'use client'

import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

```jsx filename="app/[[...slug]]/client.js" switcher
'use client'

import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

* The `'use client'` directive makes this file a **Client Component**.
* The `dynamic` import with `ssr: false` disables server-side rendering for the `<App />` component, making it truly client-only (SPA).

Now update your `page.tsx` (or `page.js`) to use your new component:

```tsx filename="app/[[...slug]]/page.tsx" switcher
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

### Step 8: Update Static Image Imports

In CRA, importing an image file returns its public URL as a string:

```tsx
import image from './img.png'

export default function App() {
  return <img src={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the Next.js [`<Image>` component](/docs/app/api-reference/components/image.md), or you can use the object's `src` property with your existing `<img>` tag.

The `<Image>` component has the added benefits of [automatic image optimization](/docs/app/api-reference/components/image.md). The `<Image>` component automatically sets the `width` and `height` attributes of the resulting `<img>` based on the image's dimensions. This prevents layout shifts when the image loads. However, this can cause issues if your app contains images with only one of their dimensions being styled without the other styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension attribute's value, which can cause the image to appear distorted.

Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by [configuring a loader](/docs/app/api-reference/components/image.md#loader), or moving to the default Next.js server which has automatic image optimization.

**Convert absolute import paths for images imported from `/public` into relative imports:**

```tsx
// Before
import logo from '/logo.png'

// After
import logo from '../public/logo.png'
```

**Pass the image `src` property instead of the whole image object to your `<img>` tag:**

```tsx
// Before
<img src={logo} />

// After
<img src={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.

> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src` property. To fix them, you need to add `next-env.d.ts` to the [`include` array](https://www.typescriptlang.org/tsconfig#include) of your `tsconfig.json` file. Next.js will automatically generate this file when you run your application on step 9.

### Step 9: Migrate Environment Variables

Next.js supports [environment variables](/docs/app/guides/environment-variables.md) similarly to CRA but **requires** a `NEXT_PUBLIC_` prefix for any variable you want to expose in the browser.

The main difference is the prefix used to expose environment variables on the client-side. Change all environment variables with the `REACT_APP_` prefix to `NEXT_PUBLIC_`.

### Step 10: Update Scripts in `package.json`

Update your `package.json` scripts to use Next.js commands. Also, add `.next` and `next-env.d.ts` to your `.gitignore`:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "npx serve@latest ./build"
  }
}
```

```txt filename=".gitignore"
# ...
.next
next-env.d.ts
```

Now you can run:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000). You should see your application now running on Next.js (in SPA mode).

### Step 11: Clean Up

You can now remove artifacts that are specific to Create React App:

* `public/index.html`
* `src/index.tsx`
* `src/react-app-env.d.ts`
* The `reportWebVitals` setup
* The `react-scripts` dependency (uninstall it from `package.json`)

## Additional Considerations

### Using a Custom `homepage` in CRA

If you used the `homepage` field in your CRA `package.json` to serve the app under a specific subpath, you can replicate that in Next.js using the [`basePath` configuration](/docs/app/api-reference/config/next-config-js/basePath.md) in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  basePath: '/my-subpath',
  // ...
}

export default nextConfig
```

### Handling a Custom `Service Worker`

If you used CRA’s service worker (e.g., `serviceWorker.js` from `create-react-app`), you can learn how to create [Progressive Web Applications (PWAs)](/docs/app/guides/progressive-web-apps.md) with Next.js.

### Proxying API Requests

If your CRA app used the `proxy` field in `package.json` to forward requests to a backend server, you can replicate this with [Next.js rewrites](/docs/app/api-reference/config/next-config-js/rewrites.md) in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://your-backend.com/:path*',
      },
    ]
  },
}
```

### Custom Webpack

If you had a custom webpack or Babel configuration in CRA, you can extend Next.js’s config in `next.config.ts`:

```ts filename="next.config.ts"
import { NextConfig } from 'next'

const nextConfig: NextConfig = {
  webpack: (config, { isServer }) => {
    // Modify the webpack config here
    return config
  },
}

export default nextConfig
```

> **Note**: This will require using Webpack by adding `--webpack` to your `dev` script.

### TypeScript Setup

Next.js automatically sets up TypeScript if you have a `tsconfig.json`. Make sure `next-env.d.ts` is listed in your `tsconfig.json` `include` array:

```json
{
  "include": ["next-env.d.ts", "app/**/*", "src/**/*"]
}
```

## Bundler Compatibility

Create React App uses webpack for bundling. Next.js now defaults to [Turbopack](/docs/app/api-reference/config/next-config-js/turbopack.md) for faster local development:

```bash
next dev  # Uses Turbopack by default
```

To use Webpack instead (similar to CRA):

```bash
next dev --webpack
```

You can still provide a [custom webpack configuration](/docs/app/api-reference/config/next-config-js/webpack.md) if you need to migrate advanced webpack settings from CRA.

## Next Steps

If everything worked, you now have a functioning Next.js application running as a single-page application. You aren’t yet leveraging Next.js features like server-side rendering or file-based routing, but you can now do so incrementally:

* **Migrate from React Router** to the [Next.js App Router](/docs/app.md) for:
  * Automatic code splitting
  * [Streaming server rendering](/docs/app/api-reference/file-conventions/loading.md)
  * [React Server Components](/docs/app/getting-started/server-and-client-components.md)
* **Optimize images** with the [`<Image>` component](/docs/app/api-reference/components/image.md)
* **Optimize fonts** with [`next/font`](/docs/app/api-reference/components/font.md)
* **Optimize third-party scripts** with the [`<Script>` component](/docs/app/guides/scripts.md)
* **Enable ESLint** with Next.js [recommended rules](/docs/app/api-reference/config/eslint.md#setup-eslint)

> **Note**: Using a static export (`output: 'export'`) [does not currently support](https://github.com/vercel/next.js/issues/54393) the `useParams` hook or other server features. To use all Next.js features, remove `output: 'export'` from your `next.config.ts`.


--------------------------------------------------------------------------------
title: "How to migrate from Vite to Next.js"
description: "Learn how to migrate your existing React application from Vite to Next.js."
source: "https://nextjs.org/docs/app/guides/migrating/from-vite"
--------------------------------------------------------------------------------

# Vite

This guide will help you migrate an existing Vite application to Next.js.

## Why Switch?

There are several reasons why you might want to switch from Vite to Next.js:

### Slow initial page loading time

If you have built your application with the [default Vite plugin for React](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-react), your application is a purely client-side application. Client-side only applications, also known as single-page applications (SPAs), often experience slow initial page loading time. This happens due to a couple of reasons:

1. The browser needs to wait for the React code and your entire application bundle to download and run before your code is able to send requests to load some data.
2. Your application code grows with every new feature and extra dependency you add.

### No automatic code splitting

The previous issue of slow loading times can be somewhat managed with code splitting. However, if you try to do code splitting manually, you'll often make performance worse. It's easy to inadvertently introduce network waterfalls when code-splitting manually. Next.js provides automatic code splitting built into its router.

### Network waterfalls

A common cause of poor performance occurs when applications make sequential client-server requests to fetch data. One common pattern for data fetching in an SPA is to initially render a placeholder, and then fetch data after the component has mounted. Unfortunately, this means that a child component that fetches data can't start fetching until the parent component has finished loading its own data.

While fetching data on the client is supported with Next.js, it also gives you the option to shift data fetching to the server, which can eliminate client-server waterfalls.

### Fast and intentional loading states

With built-in support for [streaming through React Suspense](/docs/app/getting-started/linking-and-navigating.md#streaming), you can be more intentional about which parts of your UI you want to load first and in what order without introducing network waterfalls.

This enables you to build pages that are faster to load and eliminate [layout shifts](https://vercel.com/blog/how-core-web-vitals-affect-seo).

### Choose the data fetching strategy

Depending on your needs, Next.js allows you to choose your data fetching strategy on a page and component basis. You can decide to fetch at build time, at request time on the server, or on the client. For example, you can fetch data from your CMS and render your blog posts at build time, which can then be efficiently cached on a CDN.

### Proxy

[Next.js Proxy](/docs/app/api-reference/file-conventions/proxy.md) allows you to run code on the server before a request is completed. This is especially useful to avoid having a flash of unauthenticated content when the user visits an authenticated-only page by redirecting the user to a login page. The proxy is also useful for experimentation and [internationalization](/docs/app/guides/internationalization.md).

### Built-in Optimizations

[Images](/docs/app/api-reference/components/image.md), [fonts](/docs/app/api-reference/components/font.md), and [third-party scripts](/docs/app/guides/scripts.md) often have significant impact on an application's performance. Next.js comes with built-in components that automatically optimize those for you.

## Migration Steps

Our goal with this migration is to get a working Next.js application as quickly as possible, so that
you can then adopt Next.js features incrementally. To begin with, we'll keep it as a purely
client-side application (SPA) without migrating your existing router. This helps minimize the
chances of encountering issues during the migration process and reduces merge conflicts.

### Step 1: Install the Next.js Dependency

The first thing you need to do is to install `next` as a dependency:

```bash filename="Terminal"
npm install next@latest
```

### Step 2: Create the Next.js Configuration File

Create a `next.config.mjs` at the root of your project. This file will hold your
[Next.js configuration options](/docs/app/api-reference/config/next-config-js.md).

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA).
  distDir: './dist', // Changes the build output directory to `./dist/`.
}

export default nextConfig
```

> **Good to know:** You can use either `.js` or `.mjs` for your Next.js configuration file.

### Step 3: Update TypeScript Configuration

If you're using TypeScript, you need to update your `tsconfig.json` file with the following changes
to make it compatible with Next.js. If you're not using TypeScript, you can skip this step.

1. Remove the [project reference](https://www.typescriptlang.org/tsconfig#references) to `tsconfig.node.json`
2. Add `./dist/types/**/*.ts` and `./next-env.d.ts` to the [`include` array](https://www.typescriptlang.org/tsconfig#include)
3. Add `./node_modules` to the [`exclude` array](https://www.typescriptlang.org/tsconfig#exclude)
4. Add `{ "name": "next" }` to the [`plugins` array in `compilerOptions`](https://www.typescriptlang.org/tsconfig#plugins): `"plugins": [{ "name": "next" }]`
5. Set [`esModuleInterop`](https://www.typescriptlang.org/tsconfig#esModuleInterop) to `true`: `"esModuleInterop": true`
6. Set [`jsx`](https://www.typescriptlang.org/tsconfig#jsx) to `react-jsx`: `"jsx": "react-jsx"`
7. Set [`allowJs`](https://www.typescriptlang.org/tsconfig#allowJs) to `true`: `"allowJs": true`
8. Set [`forceConsistentCasingInFileNames`](https://www.typescriptlang.org/tsconfig#forceConsistentCasingInFileNames) to `true`: `"forceConsistentCasingInFileNames": true`
9. Set [`incremental`](https://www.typescriptlang.org/tsconfig#incremental) to `true`: `"incremental": true`

Here's an example of a working `tsconfig.json` with those changes:

```json filename="tsconfig.json"
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "allowJs": true,
    "forceConsistentCasingInFileNames": true,
    "incremental": true,
    "plugins": [{ "name": "next" }]
  },
  "include": ["./src", "./dist/types/**/*.ts", "./next-env.d.ts"],
  "exclude": ["./node_modules"]
}
```

You can find more information about configuring TypeScript on the
[Next.js docs](/docs/app/api-reference/config/typescript.md#ide-plugin).

### Step 4: Create the Root Layout

A Next.js [App Router](/docs/app.md) application must include a
[root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout)
file, which is a [React Server Component](/docs/app/getting-started/server-and-client-components.md)
that will wrap all pages in your application. This file is defined at the top level of the `app`
directory.

The closest equivalent to the root layout file in a Vite application is the
[`index.html` file](https://vitejs.dev/guide/#index-html-and-project-root), which contains your
`<html>`, `<head>`, and `<body>` tags.

In this step, you'll convert your `index.html` file into a root layout file:

1. Create a new `app` directory in your `src` folder.
2. Create a new `layout.tsx` file inside that `app` directory:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return '...'
}
```

> **Good to know**: `.js`, `.jsx`, or `.tsx` extensions can be used for Layout files.

3. Copy the content of your `index.html` file into the previously created `<RootLayout>` component while
   replacing the `body.div#root` and `body.script` tags with `<div id="root">{children}</div>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

4. Next.js already includes by default the
   [meta charset](https://developer.mozilla.org/docs/Web/HTML/Element/meta#charset) and
   [meta viewport](https://developer.mozilla.org/docs/Web/HTML/Viewport_meta_tag) tags, so you
   can safely remove those from your `<head>`:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" type="image/svg+xml" href="/icon.svg" />
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

5. Any [metadata files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata)
   such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application
   `<head>` tag as long as you have them placed into the top level of the `app` directory. After
   moving
   [all supported files](/docs/app/getting-started/metadata-and-og-images.md#file-based-metadata)
   into the `app` directory you can safely delete their `<link>` tags:

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>My App</title>
        <meta name="description" content="My App is a..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

6. Finally, Next.js can manage your last `<head>` tags with the
   [Metadata API](/docs/app/getting-started/metadata-and-og-images.md). Move your final metadata
   info into an exported
   [`metadata` object](/docs/app/api-reference/functions/generate-metadata.md#metadata-object):

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'My App',
  description: 'My App is a...',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'My App',
  description: 'My App is a...',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js'
convention-based approach built into the framework
([Metadata API](/docs/app/getting-started/metadata-and-og-images.md)). This approach enables you
to more easily improve your SEO and web shareability of your pages.

### Step 5: Create the Entrypoint Page

On Next.js you declare an entrypoint for your application by creating a `page.tsx` file. The
closest equivalent of this file on Vite is your `main.tsx` file. In this step, you’ll set up the
entrypoint of your application.

1. **Create a `[[...slug]]` directory in your `app` directory.**

Since in this guide we're aiming first to set up our Next.js as an SPA (Single Page Application), you need your page entrypoint to catch all possible routes of your application. For that, create a new `[[...slug]]` directory in your `app` directory.

This directory is what is called an [optional catch-all route segment](/docs/app/api-reference/file-conventions/dynamic-routes.md#optional-catch-all-segments). Next.js uses a file-system based router where folders are used to define routes. This special directory will make sure that all routes of your application will be directed to its containing `page.tsx` file.

2. **Create a new `page.tsx` file inside the `app/[[...slug]]` directory with the following content:**

```tsx filename="app/[[...slug]]/page.tsx" switcher
import '../../index.css'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import '../../index.css'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

> **Good to know**: `.js`, `.jsx`, or `.tsx` extensions can be used for Page files.

This file is a [Server Component](/docs/app/getting-started/server-and-client-components.md). When you run `next build`, the file is prerendered into a static asset. It does *not* require any dynamic code.

This file imports our global CSS and tells [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) we are only going to generate one route, the index route at `/`.

Now, let's move the rest of our Vite application which will run client-only.

```tsx filename="app/[[...slug]]/client.tsx" switcher
'use client'

import React from 'react'
import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

```jsx filename="app/[[...slug]]/client.js" switcher
'use client'

import React from 'react'
import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

This file is a [Client Component](/docs/app/getting-started/server-and-client-components.md), defined by the `'use client'`
directive. Client Components are still [prerendered to HTML](/docs/app/getting-started/server-and-client-components.md#how-do-server-and-client-components-work-in-nextjs) on the server before being sent to the client.

Since we want a client-only application to start, we can configure Next.js to disable prerendering from the `App` component down.

```tsx
const App = dynamic(() => import('../../App'), { ssr: false })
```

Now, update your entrypoint page to use the new component:

```tsx filename="app/[[...slug]]/page.tsx" switcher
import '../../index.css'
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

```jsx filename="app/[[...slug]]/page.js" switcher
import '../../index.css'
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

### Step 6: Update Static Image Imports

Next.js handles static image imports slightly different from Vite. With Vite, importing an image
file will return its public URL as a string:

```tsx filename="App.tsx"
import image from './img.png' // `image` will be '/assets/img.2d8efhg.png' in production

export default function App() {
  return <img src={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the
Next.js [`<Image>` component](/docs/app/api-reference/components/image.md), or you can use the object's
`src` property with your existing `<img>` tag.

The `<Image>` component has the added benefits of
[automatic image optimization](/docs/app/api-reference/components/image.md). The `<Image>`
component automatically sets the `width` and `height` attributes of the resulting `<img>` based on
the image's dimensions. This prevents layout shifts when the image loads. However, this can cause
issues if your app contains images with only one of their dimensions being styled without the other
styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension
attribute's value, which can cause the image to appear distorted.

Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above
issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by [configuring a loader](/docs/app/api-reference/components/image.md#loader), or moving to the default Next.js server which has automatic image optimization.

1. **Convert absolute import paths for images imported from `/public` into relative imports:**

```tsx
// Before
import logo from '/logo.png'

// After
import logo from '../public/logo.png'
```

2. **Pass the image `src` property instead of the whole image object to your `<img>` tag:**

```tsx
// Before
<img src={logo} />

// After
<img src={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.

> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src`
> property. You can safely ignore those for now. They will be fixed by the end of this guide.

### Step 7: Migrate the Environment Variables

Next.js has support for `.env`
[environment variables](/docs/app/guides/environment-variables.md)
similar to Vite. The main difference is the prefix used to expose environment variables on the
client-side.

* Change all environment variables with the `VITE_` prefix to `NEXT_PUBLIC_`.

Vite exposes a few built-in environment variables on the special `import.meta.env` object which
aren’t supported by Next.js. You need to update their usage as follows:

* `import.meta.env.MODE` ⇒ `process.env.NODE_ENV`
* `import.meta.env.PROD` ⇒ `process.env.NODE_ENV === 'production'`
* `import.meta.env.DEV` ⇒ `process.env.NODE_ENV !== 'production'`
* `import.meta.env.SSR` ⇒ `typeof window !== 'undefined'`

Next.js also doesn't provide a built-in `BASE_URL` environment variable. However, you can still
configure one, if you need it:

1. **Add the following to your `.env` file:**

```bash filename=".env"
# ...
NEXT_PUBLIC_BASE_PATH="/some-base-path"
```

2. **Set [`basePath`](/docs/app/api-reference/config/next-config-js/basePath.md) to `process.env.NEXT_PUBLIC_BASE_PATH` in your `next.config.mjs` file:**

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA).
  distDir: './dist', // Changes the build output directory to `./dist/`.
  basePath: process.env.NEXT_PUBLIC_BASE_PATH, // Sets the base path to `/some-base-path`.
}

export default nextConfig
```

3. **Update `import.meta.env.BASE_URL` usages to `process.env.NEXT_PUBLIC_BASE_PATH`**

### Step 8: Update Scripts in `package.json`

You should now be able to run your application to test if you successfully migrated to Next.js. But
before that, you need to update your `scripts` in your `package.json` with Next.js related commands,
and add `.next` and `next-env.d.ts` to your `.gitignore`:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

```txt filename=".gitignore"
# ...
.next
next-env.d.ts
dist
```

Now run `npm run dev`, and open [`http://localhost:3000`](http://localhost:3000). You should see your application now running on Next.js.

> **Example:** Check out [this pull request](https://github.com/inngest/vite-to-nextjs/pull/1) for a
> working example of a Vite application migrated to Next.js.

### Step 9: Clean Up

You can now clean up your codebase from Vite related artifacts:

* Delete `main.tsx`
* Delete `index.html`
* Delete `vite-env.d.ts`
* Delete `tsconfig.node.json`
* Delete `vite.config.ts`
* Uninstall Vite dependencies

## Next Steps

If everything went according to plan, you now have a functioning Next.js application running as a
single-page application. However, you aren't yet taking advantage of most of Next.js' benefits, but
you can now start making incremental changes to reap all the benefits. Here's what you might want to
do next:

* Migrate from React Router to the [Next.js App Router](/docs/app.md) to get:
  * Automatic code splitting
  * [Streaming Server-Rendering](/docs/app/api-reference/file-conventions/loading.md)
  * [React Server Components](/docs/app/getting-started/server-and-client-components.md)
* [Optimize images with the `<Image>` component](/docs/app/api-reference/components/image.md)
* [Optimize fonts with `next/font`](/docs/app/api-reference/components/font.md)
* [Optimize third-party scripts with the `<Script>` component](/docs/app/guides/scripts.md)
* [Update your ESLint configuration to support Next.js rules](/docs/app/api-reference/config/eslint.md)


--------------------------------------------------------------------------------
title: "How to build multi-tenant apps in Next.js"
description: "Learn how to build multi-tenant apps with the App Router."
source: "https://nextjs.org/docs/app/guides/multi-tenant"
--------------------------------------------------------------------------------

# Multi-tenant

If you are looking to build a single Next.js application that serves multiple tenants, we have [built an example](https://vercel.com/templates/next.js/platforms-starter-kit) showing our recommended architecture.


--------------------------------------------------------------------------------
title: "How to build micro-frontends using multi-zones and Next.js"
description: "Learn how to build micro-frontends using Next.js Multi-Zones to deploy multiple Next.js apps under a single domain."
source: "https://nextjs.org/docs/app/guides/multi-zones"
--------------------------------------------------------------------------------

# Multi-zones

<details>
<summary>Examples</summary>

* [With Zones](https://github.com/vercel/next.js/tree/canary/examples/with-zones)

</details>

Multi-Zones are an approach to micro-frontends that separate a large application on a domain into smaller Next.js applications that each serve a set of paths. This is useful when there are collections of pages unrelated to the other pages in the application. By moving those pages to a separate zone (i.e., a separate application), you can reduce the size of each application which improves build times and removes code that is only necessary for one of the zones. Since applications are decoupled, Multi-Zones also allows other applications on the domain to use their own choice of framework.

For example, let's say you have the following set of pages that you would like to split up:

* `/blog/*` for all blog posts
* `/dashboard/*` for all pages when the user is logged-in to the dashboard
* `/*` for the rest of your website not covered by other zones

With Multi-Zones support, you can create three applications that all are served on the same domain and look the same to the user, but you can develop and deploy each of the applications independently.

![Three zones: A, B, C. Showing a hard navigation between routes from different zones, and soft navigations between routes within the same zone.](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/multi-zones.png)

Navigating between pages in the same zone will perform soft navigations, a navigation that does not require reloading the page. For example, in this diagram, navigating from `/` to `/products` will be a soft navigation.

Navigating from a page in one zone to a page in another zone, such as from `/` to `/dashboard`, will perform a hard navigation, unloading the resources of the current page and loading the resources of the new page. Pages that are frequently visited together should live in the same zone to avoid hard navigations.

## How to define a zone

A zone is a normal Next.js application where you also configure an [assetPrefix](/docs/app/api-reference/config/next-config-js/assetPrefix.md) to avoid conflicts with pages and static files in other zones.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
}
```

Next.js assets, such as JavaScript and CSS, will be prefixed with `assetPrefix` to make sure that they don't conflict with assets from other zones. These assets will be served under `/assetPrefix/_next/...` for each of the zones.

The default application handling all paths not routed to another more specific zone does not need an `assetPrefix`.

In versions older than Next.js 15, you may also need an additional rewrite to handle the static assets. This is no longer necessary in Next.js 15.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  assetPrefix: '/blog-static',
  async rewrites() {
    return {
      beforeFiles: [
        {
          source: '/blog-static/_next/:path+',
          destination: '/_next/:path+',
        },
      ],
    }
  },
}
```

## How to route requests to the right zone

With the Multi Zones set-up, you need to route the paths to the correct zone since they are served by different applications. You can use any HTTP proxy to do this, but one of the Next.js applications can also be used to route requests for the entire domain.

To route to the correct zone using a Next.js application, you can use [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md). For each path served by a different zone, you would add a rewrite rule to send that path to the domain of the other zone, and you also need to rewrite the requests for the static assets. For example:

```js filename="next.config.js"
async rewrites() {
    return [
        {
            source: '/blog',
            destination: `${process.env.BLOG_DOMAIN}/blog`,
        },
        {
            source: '/blog/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog/:path+`,
        },
        {
            source: '/blog-static/:path+',
            destination: `${process.env.BLOG_DOMAIN}/blog-static/:path+`,
        }
    ];
}
```

`destination` should be a URL that is served by the zone, including scheme and domain. This should point to the zone's production domain, but it can also be used to route requests to `localhost` in local development.

> **Good to know**: URL paths should be unique to a zone. For example, two zones trying to serve `/blog` would create a routing conflict.

### Routing requests using proxy

Routing requests through [`rewrites`](/docs/app/api-reference/config/next-config-js/rewrites.md) is recommended to minimize latency overhead for the requests, but proxy can also be used when there is a need for a dynamic decision when routing. For example, if you are using a feature flag to decide where a path should be routed such as during a migration, you can use proxy.

```js filename="proxy.js"
export async function proxy(request) {
  const { pathname, search } = req.nextUrl;
  if (pathname === '/your-path' && myFeatureFlag.isEnabled()) {
    return NextResponse.rewrite(`${rewriteDomain}${pathname}${search});
  }
}
```

## Linking between zones

Links to paths in a different zone should use an `a` tag instead of the Next.js [`<Link>`](/docs/pages/api-reference/components/link.md) component. This is because Next.js will try to prefetch and soft navigate to any relative path in `<Link>` component, which will not work across zones.

## Sharing code

The Next.js applications that make up the different zones can live in any repository. However, it is often convenient to put these zones in a [monorepo](https://en.wikipedia.org/wiki/Monorepo) to more easily share code. For zones that live in different repositories, code can also be shared using public or private NPM packages.

Since the pages in different zones may be released at different times, feature flags can be useful for enabling or disabling features in unison across the different zones.

## Server Actions

When using [Server Actions](/docs/app/getting-started/updating-data.md) with Multi-Zones, you must explicitly allow the user-facing origin since your user facing domain may serve multiple applications. In your `next.config.js` file, add the following lines:

```js filename="next.config.js"
const nextConfig = {
  experimental: {
    serverActions: {
      allowedOrigins: ['your-production-domain.com'],
    },
  },
}
```

See [`serverActions.allowedOrigins`](/docs/app/api-reference/config/next-config-js/serverActions.md#allowedorigins) for more information.


--------------------------------------------------------------------------------
title: "How to set up instrumentation with OpenTelemetry"
description: "Learn how to instrument your Next.js app with OpenTelemetry."
source: "https://nextjs.org/docs/app/guides/open-telemetry"
--------------------------------------------------------------------------------

# OpenTelemetry

Observability is crucial for understanding and optimizing the behavior and performance of your Next.js app.

As applications become more complex, it becomes increasingly difficult to identify and diagnose issues that may arise. By leveraging observability tools, such as logging and metrics, developers can gain insights into their application's behavior and identify areas for optimization. With observability, developers can proactively address issues before they become major problems and provide a better user experience. Therefore, it is highly recommended to use observability in your Next.js applications to improve performance, optimize resources, and enhance user experience.

We recommend using OpenTelemetry for instrumenting your apps.
It's a platform-agnostic way to instrument apps that allows you to change your observability provider without changing your code.
Read [Official OpenTelemetry docs](https://opentelemetry.io/docs/) for more information about OpenTelemetry and how it works.

This documentation uses terms like *Span*, *Trace* or *Exporter* throughout this doc, all of which can be found in [the OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/).

Next.js supports OpenTelemetry instrumentation out of the box, which means that we already instrumented Next.js itself.

## Getting Started

OpenTelemetry is extensible but setting it up properly can be quite verbose.
That's why we prepared a package `@vercel/otel` that helps you get started quickly.

### Using `@vercel/otel`

To get started, install the following packages:

```bash filename="Terminal"
npm install @vercel/otel @opentelemetry/sdk-logs @opentelemetry/api-logs @opentelemetry/instrumentation
```

Next, create a custom [`instrumentation.ts`](/docs/app/guides/instrumentation.md) (or `.js`) file in the **root directory** of the project (or inside `src` folder if using one):

```ts filename="your-project/instrumentation.ts" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

```js filename="your-project/instrumentation.js" switcher
import { registerOTel } from '@vercel/otel'

export function register() {
  registerOTel({ serviceName: 'next-app' })
}
```

See the [`@vercel/otel` documentation](https://www.npmjs.com/package/@vercel/otel) for additional configuration options.

> **Good to know**:
>
> * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
> * If you use the [`pageExtensions` config option](/docs/app/api-reference/config/next-config-js/pageExtensions.md) to add a suffix, you will also need to update the `instrumentation` filename to match.
> * We have created a basic [with-opentelemetry](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry) example that you can use.

### Manual OpenTelemetry configuration

The `@vercel/otel` package provides many configuration options and should serve most of common use cases. But if it doesn't suit your needs, you can configure OpenTelemetry manually.

Firstly you need to install OpenTelemetry packages:

```bash filename="Terminal"
npm install @opentelemetry/sdk-node @opentelemetry/resources @opentelemetry/semantic-conventions @opentelemetry/sdk-trace-node @opentelemetry/exporter-trace-otlp-http
```

Now you can initialize `NodeSDK` in your `instrumentation.ts`.
Unlike `@vercel/otel`, `NodeSDK` is not compatible with edge runtime, so you need to make sure that you are importing them only when `process.env.NEXT_RUNTIME === 'nodejs'`. We recommend creating a new file `instrumentation.node.ts` which you conditionally import only when using node:

```ts filename="instrumentation.ts" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation.node.ts')
  }
}
```

```js filename="instrumentation.js" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation.node.js')
  }
}
```

```ts filename="instrumentation.node.ts" switcher
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { resourceFromAttributes } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'

const sdk = new NodeSDK({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'next-app',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
})
sdk.start()
```

```js filename="instrumentation.node.js" switcher
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http'
import { resourceFromAttributes } from '@opentelemetry/resources'
import { NodeSDK } from '@opentelemetry/sdk-node'
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-node'
import { ATTR_SERVICE_NAME } from '@opentelemetry/semantic-conventions'

const sdk = new NodeSDK({
  resource: resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'next-app',
  }),
  spanProcessor: new SimpleSpanProcessor(new OTLPTraceExporter()),
})
sdk.start()
```

Doing this is equivalent to using `@vercel/otel`, but it's possible to modify and extend some features that are not exposed by the `@vercel/otel`. If edge runtime support is necessary, you will have to use `@vercel/otel`.

## Testing your instrumentation

You need an OpenTelemetry collector with a compatible backend to test OpenTelemetry traces locally.
We recommend using our [OpenTelemetry dev environment](https://github.com/vercel/opentelemetry-collector-dev-setup).

If everything works well you should be able to see the root server span labeled as `GET /requested/pathname`.
All other spans from that particular trace will be nested under it.

Next.js traces more spans than are emitted by default.
To see more spans, you must set `NEXT_OTEL_VERBOSE=1`.

## Deployment

### Using OpenTelemetry Collector

When you are deploying with OpenTelemetry Collector, you can use `@vercel/otel`.
It will work both on Vercel and when self-hosted.

#### Deploying on Vercel

We made sure that OpenTelemetry works out of the box on Vercel.

Follow [Vercel documentation](https://vercel.com/docs/concepts/observability/otel-overview/quickstart) to connect your project to an observability provider.

#### Self-hosting

Deploying to other platforms is also straightforward. You will need to spin up your own OpenTelemetry Collector to receive and process the telemetry data from your Next.js app.

To do this, follow the [OpenTelemetry Collector Getting Started guide](https://opentelemetry.io/docs/collector/getting-started/), which will walk you through setting up the collector and configuring it to receive data from your Next.js app.

Once you have your collector up and running, you can deploy your Next.js app to your chosen platform following their respective deployment guides.

### Custom Exporters

OpenTelemetry Collector is not necessary. You can use a custom OpenTelemetry exporter with [`@vercel/otel`](#using-vercelotel) or [manual OpenTelemetry configuration](#manual-opentelemetry-configuration).

## Custom Spans

You can add a custom span with [OpenTelemetry APIs](https://opentelemetry.io/docs/instrumentation/js/instrumentation).

```bash filename="Terminal"
npm install @opentelemetry/api
```

The following example demonstrates a function that fetches GitHub stars and adds a custom `fetchGithubStars` span to track the fetch request's result:

```ts
import { trace } from '@opentelemetry/api'

export async function fetchGithubStars() {
  return await trace
    .getTracer('nextjs-example')
    .startActiveSpan('fetchGithubStars', async (span) => {
      try {
        return await getValue()
      } finally {
        span.end()
      }
    })
}
```

The `register` function will execute before your code runs in a new environment.
You can start creating new spans, and they should be correctly added to the exported trace.

## Default Spans in Next.js

Next.js automatically instruments several spans for you to provide useful insights into your application's performance.

Attributes on spans follow [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/). We also add some custom attributes under the `next` namespace:

* `next.span_name` - duplicates span name
* `next.span_type` - each span type has a unique identifier
* `next.route` - The route pattern of the request (e.g., `/[param]/user`).
* `next.rsc` (true/false) - Whether the request is an RSC request, such as prefetch.
* `next.page`
  * This is an internal value used by an app router.
  * You can think about it as a route to a special file (like `page.ts`, `layout.ts`, `loading.ts` and others)
  * It can be used as a unique identifier only when paired with `next.route` because `/layout` can be used to identify both `/(groupA)/layout.ts` and `/(groupB)/layout.ts`

### `[http.method] [next.route]`

* `next.span_type`: `BaseServer.handleRequest`

This span represents the root span for each incoming request to your Next.js application. It tracks the HTTP method, route, target, and status code of the request.

Attributes:

* [Common HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
  * `http.method`
  * `http.status_code`
* [Server HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-server-semantic-conventions)
  * `http.route`
  * `http.target`
* `next.span_name`
* `next.span_type`
* `next.route`

### `render route (app) [next.route]`

* `next.span_type`: `AppRender.getBodyResult`.

This span represents the process of rendering a route in the app router.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `fetch [http.method] [http.url]`

* `next.span_type`: `AppRender.fetch`

This span represents the fetch request executed in your code.

Attributes:

* [Common HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#common-attributes)
  * `http.method`
* [Client HTTP attributes](https://opentelemetry.io/docs/reference/specification/trace/semantic_conventions/http/#http-client)
  * `http.url`
  * `net.peer.name`
  * `net.peer.port` (only if specified)
* `next.span_name`
* `next.span_type`

This span can be turned off by setting `NEXT_OTEL_FETCH_DISABLED=1` in your environment. This is useful when you want to use a custom fetch instrumentation library.

### `executing api route (app) [next.route]`

* `next.span_type`: `AppRouteRouteHandlers.runHandler`.

This span represents the execution of an API Route Handler in the app router.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `getServerSideProps [next.route]`

* `next.span_type`: `Render.getServerSideProps`.

This span represents the execution of `getServerSideProps` for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `getStaticProps [next.route]`

* `next.span_type`: `Render.getStaticProps`.

This span represents the execution of `getStaticProps` for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `render route (pages) [next.route]`

* `next.span_type`: `Render.renderDocument`.

This span represents the process of rendering the document for a specific route.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `generateMetadata [next.page]`

* `next.span_type`: `ResolveMetadata.generateMetadata`.

This span represents the process of generating metadata for a specific page (a single route can have multiple of these spans).

Attributes:

* `next.span_name`
* `next.span_type`
* `next.page`

### `resolve page components`

* `next.span_type`: `NextNodeServer.findPageComponents`.

This span represents the process of resolving page components for a specific page.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.route`

### `resolve segment modules`

* `next.span_type`: `NextNodeServer.getLayoutOrPageModule`.

This span represents loading of code modules for a layout or a page.

Attributes:

* `next.span_name`
* `next.span_type`
* `next.segment`

### `start response`

* `next.span_type`: `NextNodeServer.startResponse`.

This zero-length span represents the time when the first byte has been sent in the response.


--------------------------------------------------------------------------------
title: "How to optimize package bundling"
description: "Learn how to optimize your application's server and client bundles."
source: "https://nextjs.org/docs/app/guides/package-bundling"
--------------------------------------------------------------------------------

# Package Bundling

Bundling external packages can significantly improve the performance of your application. By default, packages imported inside Server Components and Route Handlers are automatically bundled by Next.js. This page will guide you through how to analyze and further optimize package bundling.&#x20;

## Analyzing JavaScript bundles

[`@next/bundle-analyzer`](https://www.npmjs.com/package/@next/bundle-analyzer) is a plugin for Next.js that helps you manage the size of your application bundles. It generates a visual report of the size of each package and their dependencies. You can use the information to remove large dependencies, split, or [lazy-load](/docs/app/guides/lazy-loading.md) your code.

### Installation

Install the plugin by running the following command:

```bash
npm i @next/bundle-analyzer
# or
yarn add @next/bundle-analyzer
# or
pnpm add @next/bundle-analyzer
```

Then, add the bundle analyzer's settings to your `next.config.js`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {}

const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer(nextConfig)
```

### Generating a report

Run the following command to analyze your bundles:

```bash
ANALYZE=true npm run build
# or
ANALYZE=true yarn build
# or
ANALYZE=true pnpm build
```

The report will open three new tabs in your browser, which you can inspect. Periodically evaluating your application's bundles can help you maintain application performance over time.

## Optimizing package imports

Some packages, such as icon libraries, can export hundreds of modules, which can cause performance issues in development and production.

You can optimize how these packages are imported by adding the [`optimizePackageImports`](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md) option to your `next.config.js`. This option will only load the modules you *actually* use, while still giving you the convenience of writing import statements with many named exports.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    optimizePackageImports: ['icon-library'],
  },
}

module.exports = nextConfig
```

Next.js also optimizes some libraries automatically, thus they do not need to be included in the optimizePackageImports list. See the [full list](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md).

## Opting specific packages out of bundling

Since packages imported inside Server Components and Route Handlers are automatically bundled by Next.js, you can opt specific packages out of bundling using the [`serverExternalPackages`](/docs/app/api-reference/config/next-config-js/serverExternalPackages.md) option in your `next.config.js`.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  serverExternalPackages: ['package-name'],
}

module.exports = nextConfig
```

Next.js includes a list of popular packages that currently are working on compatibility and automatically opt-ed out. See the [full list](/docs/app/api-reference/config/next-config-js/serverExternalPackages.md).


Learn more about optimizing your application for production.

- [Production](/docs/app/guides/production-checklist.md)
  - Recommendations to ensure the best performance and user experience before taking your Next.js application to production.


--------------------------------------------------------------------------------
title: "Prefetching"
description: "Learn how to configure prefetching in Next.js"
source: "https://nextjs.org/docs/app/guides/prefetching"
--------------------------------------------------------------------------------

# Prefetching

Prefetching makes navigating between different routes in your application feel instant. Next.js tries to intelligently prefetch by default, based on the links used in your application code.

This guide will explain how prefetching works and show common implementation patterns:

* [Automatic prefetch](#automatic-prefetch)
* [Manual prefetch](#manual-prefetch)
* [Hover-triggered prefetch](#hover-triggered-prefetch)
* [Extending or ejecting link](#extending-or-ejecting-link)
* [Disabled prefetch](#disabled-prefetch)

## How does prefetching work?

When navigating between routes, the browser requests assets for the page like HTML and JavaScript files. Prefetching is the process of fetching these resources *ahead* of time, before you navigate to a new route.

Next.js automatically splits your application into smaller JavaScript chunks based on routes. Instead of loading all the code upfront like traditional SPAs, only the code needed for the current route is loaded. This reduces the initial load time while other parts of the app are loaded in the background. By the time you click the link, the resources for the new route have already been loaded into the browser cache.

When navigating to the new page, there's no full page reload or browser loading spinner. Instead, Next.js performs a [client-side transition](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions), making the page navigation feel instant.

## Prefetching static vs. dynamic routes

|                                                                   | **Static page** | **Dynamic page**                                                                |
| ----------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------- |
| **Prefetched**                                                    | Yes, full route | No, unless [`loading.js`](/docs/app/api-reference/file-conventions/loading.md)     |
| [**Client Cache TTL**](/docs/app/guides/caching.md#full-route-cache) | 5 min (default) | Off, unless [enabled](/docs/app/api-reference/config/next-config-js/staleTimes.md) |
| **Server roundtrip on click**                                     | No              | Yes, streamed after [shell](/docs/app/getting-started/cache-components.md)         |

> **Good to know:** During the initial navigation, the browser fetches the HTML, JavaScript, and React Server Components (RSC) Payload. For subsequent navigations, the browser will fetch the RSC Payload for Server Components and JS bundle for Client Components.

## Automatic prefetch

```tsx filename="app/ui/nav-link.tsx" switcher
import Link from 'next/link'

export default function NavLink() {
  return <Link href="/about">About</Link>
}
```

```jsx filename="app/ui/nav-link.js" switcher
import Link from 'next/link'

export default function NavLink() {
  return <Link href="/about">About</Link>
}
```

| **Context**       | **Prefetched payload**           | **Client Cache TTL**                                                           |
| ----------------- | -------------------------------- | ------------------------------------------------------------------------------ |
| No `loading.js`   | Entire page                      | Until app reload                                                               |
| With `loading.js` | Layout to first loading boundary | 30s ([configurable](/docs/app/api-reference/config/next-config-js/staleTimes.md)) |

Automatic prefetching runs only in production. Disable with `prefetch={false}` or use the wrapper in [Disabled Prefetch](#disabled-prefetch).

## Manual prefetch

To do manual prefetching, import the `useRouter` hook from `next/navigation`, and call `router.prefetch()` to warm routes outside the viewport or in response to analytics, hover, scroll, etc.

```tsx
'use client'

import { useRouter } from 'next/navigation'
import { CustomLink } from '@components/link'

export function PricingCard() {
  const router = useRouter()

  return (
    <div onMouseEnter={() => router.prefetch('/pricing')}>
      {/* other UI elements */}
      <CustomLink href="/pricing">View Pricing</CustomLink>
    </div>
  )
}
```

If the intent is to prefetch a URL when a component loads, see the extending or rejecting a link \[example].

## Hover-triggered prefetch

> **Proceed with caution:** Extending `Link` opts you into maintaining prefetching, cache invalidation, and accessibility concerns. Proceed only if defaults are insufficient.

Next.js tries to do the right prefetching by default, but power users can eject and modify based on their needs. You have the control between performance and resource consumption.

For example, you might have to only trigger prefetches on hover, instead of when entering the viewport (the default behavior):

```tsx
'use client'

import Link from 'next/link'
import { useState } from 'react'

export function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

`prefetch={null}` restores default (static) prefetching once the user shows intent.

## Extending or ejecting link

You can extend the `<Link>` component to create your own custom prefetching strategy. For example, using the [ForesightJS](https://foresightjs.com/docs/integrations/nextjs) library which prefetches links by predicting the direction of the user's cursor.

Alternatively, you can use [`useRouter`](/docs/app/api-reference/functions/use-router.md) to recreate some of the native `<Link>` behavior. However, be aware this opts you into maintaining prefetching and cache invalidation.

```tsx
'use client'

import { useRouter } from 'next/navigation'
import { useEffect } from 'react'

function ManualPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const router = useRouter()

  useEffect(() => {
    let cancelled = false
    const poll = () => {
      if (!cancelled) router.prefetch(href, { onInvalidate: poll })
    }
    poll()
    return () => {
      cancelled = true
    }
  }, [href, router])

  return (
    <a
      href={href}
      onClick={(event) => {
        event.preventDefault()
        router.push(href)
      }}
    >
      {children}
    </a>
  )
}
```

[`onInvalidate`](/docs/app/api-reference/functions/use-router.md#userouter) is invoked when Next.js suspects cached data is stale, allowing you to refresh the prefetch.

> **Good to know:** Using an `a` tag will cause a full page navigation to the destination route, you can use `onClick` to prevent the full page navigation, and then invoke `router.push` to navigate to the destination.

## Disabled prefetch

You can fully disable prefetching for certain routes for more fine-grained control over resource consumption.

```tsx
'use client'

import Link, { LinkProps } from 'next/link'

function NoPrefetchLink({
  prefetch,
  ...rest
}: LinkProps & { children: React.ReactNode }) {
  return <Link {...rest} prefetch={false} />
}
```

For example, you may still want to have consistent usage of `<Link>` in your application, but links in your footer might not need to be prefetched when entering the viewport.

## Prefetching optimizations

### Client cache

Next.js stores prefetched React Server Component payloads in memory, keyed by route segments. When navigating between sibling routes (e.g. `/dashboard/settings` → `/dashboard/analytics`), it reuses the parent layout and only fetches the updated leaf page. This reduces network traffic and improves navigation speed.

### Prefetch scheduling

Next.js maintains a small task queue, which prefetches in the following order:

1. Links in the viewport
2. Links showing user intent (hover or touch)
3. Newer links replace older ones
4. Links scrolled off-screen are discarded

The scheduler prioritizes likely navigations while minimizing unused downloads.

### Partial Prerendering (PPR)

When PPR is enabled, a page is divided into a static shell and a streamed dynamic section:

* The shell, which can be prefetched, streams immediately
* Dynamic data streams when ready
* Data invalidations (`revalidateTag`, `revalidatePath`) silently refresh associated prefetches

## Troubleshooting

### Triggering unwanted side-effects during prefetching

If your layouts or pages are not [pure](https://react.dev/learn/keeping-components-pure#purity-components-as-formulas) and have side-effects (e.g. tracking analytics), these might be triggered when the route is prefetched, not when the user visits the page.

To avoid this, you should move side-effects to a `useEffect` hook or a Server Action triggered from a Client Component.

**Before**:

```tsx filename="app/dashboard/layout.tsx" switcher
import { trackPageView } from '@/lib/analytics'

export default function Layout({ children }: { children: React.ReactNode }) {
  // This runs during prefetch
  trackPageView()

  return <div>{children}</div>
}
```

```jsx filename="app/dashboard/layout.js" switcher
import { trackPageView } from '@/lib/analytics'

export default function Layout({ children }) {
  // This runs during prefetch
  trackPageView()

  return <div>{children}</div>
}
```

**After**:

```tsx filename="app/ui/analytics-tracker.tsx" switcher
'use client'

import { useEffect } from 'react'
import { trackPageView } from '@/lib/analytics'

export function AnalyticsTracker() {
  useEffect(() => {
    trackPageView()
  }, [])

  return null
}
```

```jsx filename="app/ui/analytics-tracker.js" switcher
'use client'

import { useEffect } from 'react'
import { trackPageView } from '@/lib/analytics'

export function AnalyticsTracker() {
  useEffect(() => {
    trackPageView()
  }, [])

  return null
}
```

```tsx filename="app/dashboard/layout.tsx" switcher
import { AnalyticsTracker } from '@/app/ui/analytics-tracker'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <AnalyticsTracker />
      {children}
    </div>
  )
}
```

```jsx filename="app/dashboard/layout.js" switcher
import { AnalyticsTracker } from '@/app/ui/analytics-tracker'

export default function Layout({ children }) {
  return (
    <div>
      <AnalyticsTracker />
      {children}
    </div>
  )
}
```

### Preventing too many prefetches

Next.js automatically prefetches links in the viewport when using the `<Link>` component.

There may be cases where you want to prevent this to avoid unnecessary usage of resources, such as when rendering a large list of links (e.g. an infinite scroll table).

You can disable prefetching by setting the `prefetch` prop of the `<Link>` component to `false`.

```tsx filename="app/ui/no-prefetch-link.tsx" switcher
<Link prefetch={false} href={`/blog/${post.id}`}>
  {post.title}
</Link>
```

However, this means static routes will only be fetched on click, and dynamic routes will wait for the server to render before navigating.

To reduce resource usage without disabling prefetch entirely, you can defer prefetching until the user hovers over a link. This targets only links the user is likely to visit.

```tsx filename="app/ui/hover-prefetch-link.tsx" switcher
'use client'

import Link from 'next/link'
import { useState } from 'react'

export function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

```jsx filename="app/ui/hover-prefetch-link.js" switcher
'use client'

import Link from 'next/link'
import { useState } from 'react'

export function HoverPrefetchLink({ href, children }) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```


--------------------------------------------------------------------------------
title: "How to optimize your Next.js application for production"
description: "Recommendations to ensure the best performance and user experience before taking your Next.js application to production."
source: "https://nextjs.org/docs/app/guides/production-checklist"
--------------------------------------------------------------------------------

# Production

Before taking your Next.js application to production, there are some optimizations and patterns you should consider implementing for the best user experience, performance, and security.

This page provides best practices that you can use as a reference when [building your application](#during-development) and [before going to production](#before-going-to-production), as well as the [automatic Next.js optimizations](#automatic-optimizations) you should be aware of.

## Automatic optimizations

These Next.js optimizations are enabled by default and require no configuration:

* **[Server Components](/docs/app/getting-started/server-and-client-components.md):** Next.js uses Server Components by default. Server Components run on the server, and don't require JavaScript to render on the client. As such, they have no impact on the size of your client-side JavaScript bundles. You can then use [Client Components](/docs/app/getting-started/server-and-client-components.md) as needed for interactivity.
* **[Code-splitting](/docs/app/getting-started/linking-and-navigating.md#how-navigation-works):** Server Components enable automatic code-splitting by route segments. You may also consider [lazy loading](/docs/app/guides/lazy-loading.md) Client Components and third-party libraries, where appropriate.
* **[Prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching):** When a link to a new route enters the user's viewport, Next.js prefetches the route in background. This makes navigation to new routes almost instant. You can opt out of prefetching, where appropriate.
* **[Static Rendering](/docs/app/guides/caching.md#static-rendering):** Next.js statically renders Server and Client Components on the server at build time and caches the rendered result to improve your application's performance. You can opt into [Dynamic Rendering](/docs/app/guides/caching.md#dynamic-rendering) for specific routes, where appropriate.&#x20;
* **[Caching](/docs/app/guides/caching.md):** Next.js caches data requests, the rendered result of Server and Client Components, static assets, and more, to reduce the number of network requests to your server, database, and backend services. You may opt out of caching, where appropriate.

These defaults aim to improve your application's performance, and reduce the cost and amount of data transferred on each network request.

## During development

While building your application, we recommend using the following features to ensure the best performance and user experience:

### Routing and rendering

* **[Layouts](/docs/app/api-reference/file-conventions/layout.md):** Use layouts to share UI across pages and enable [partial rendering](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions) on navigation.
* **[`<Link>` component](/docs/app/api-reference/components/link.md):** Use the `<Link>` component for [client-side navigation and prefetching](/docs/app/getting-started/linking-and-navigating.md#how-navigation-works).
* **[Error Handling](/docs/app/getting-started/error-handling.md):** Gracefully handle [catch-all errors](/docs/app/getting-started/error-handling.md) and [404 errors](/docs/app/api-reference/file-conventions/not-found.md) in production by creating custom error pages.
* **[Client and Server Components](/docs/app/getting-started/server-and-client-components.md#examples):** Follow the recommended composition patterns for Server and Client Components, and check the placement of your [`"use client"` boundaries](/docs/app/getting-started/server-and-client-components.md#examples#moving-client-components-down-the-tree) to avoid unnecessarily increasing your client-side JavaScript bundle.
* **[Dynamic APIs](/docs/app/guides/caching.md#dynamic-rendering):** Be aware that Dynamic APIs like [`cookies`](/docs/app/api-reference/functions/cookies.md) and the [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) prop will opt the entire route into [Dynamic Rendering](/docs/app/guides/caching.md#dynamic-rendering) (or your whole application if used in the [Root Layout](/docs/app/api-reference/file-conventions/layout.md#root-layout)). Ensure Dynamic API usage is intentional and wrap them in `<Suspense>` boundaries where appropriate.

> **Good to know**: [Partial Prerendering (experimental)](/blog/next-14#partial-prerendering-preview) will allow parts of a route to be dynamic without opting the whole route into dynamic rendering.

### Data fetching and caching

* **[Server Components](/docs/app/getting-started/fetching-data.md):** Leverage the benefits of fetching data on the server using Server Components.
* **[Route Handlers](/docs/app/api-reference/file-conventions/route.md):** Use Route Handlers to access your backend resources from Client Components. But do not call Route Handlers from Server Components to avoid an additional server request.
* **[Streaming](/docs/app/api-reference/file-conventions/loading.md):** Use Loading UI and React Suspense to progressively send UI from the server to the client, and prevent the whole route from blocking while data is being fetched.
* **[Parallel Data Fetching](/docs/app/getting-started/fetching-data.md#parallel-data-fetching):** Reduce network waterfalls by fetching data in parallel, where appropriate. Also, consider [preloading data](/docs/app/getting-started/fetching-data.md#preloading-data) where appropriate.
* **[Data Caching](/docs/app/guides/caching.md#data-cache):** Verify whether your data requests are being cached or not, and opt into caching, where appropriate. Ensure requests that don't use `fetch` are [cached](/docs/app/api-reference/functions/unstable_cache.md).
* **[Static Images](/docs/app/api-reference/file-conventions/public-folder.md):** Use the `public` directory to automatically cache your application's static assets, e.g. images.

### UI and accessibility

* **[Forms and Validation](/docs/app/guides/forms.md):** Use Server Actions to handle form submissions, server-side validation, and handle errors.
* **[Global Error UI](/docs/app/api-reference/file-conventions/error.md#global-error):** Add `app/global-error.tsx` to provide consistent, accessible fallback UI and recovery for uncaught errors across your app.
* **[Global 404](/docs/app/api-reference/file-conventions/not-found.md#global-not-foundjs-experimental):** Add `app/global-not-found.tsx` to serve an accessible 404 for unmatched routes across your app.

- **[Font Module](/docs/app/api-reference/components/font.md):** Optimize fonts by using the Font Module, which automatically hosts your font files with other static assets, removes external network requests, and reduces [layout shift](https://web.dev/articles/cls).
- **[`<Image>` Component](/docs/app/api-reference/components/image.md):** Optimize images by using the Image Component, which automatically optimizes images, prevents layout shift, and serves them in modern formats like WebP.
- **[`<Script>` Component](/docs/app/guides/scripts.md):** Optimize third-party scripts by using the Script Component, which automatically defers scripts and prevents them from blocking the main thread.
- **[ESLint](/docs/architecture/accessibility.md#linting):** Use the built-in `eslint-plugin-jsx-a11y` plugin to catch accessibility issues early.

### Security

* **[Tainting](/docs/app/api-reference/config/next-config-js/taint.md):** Prevent sensitive data from being exposed to the client by tainting data objects and/or specific values.
* **[Server Actions](/docs/app/getting-started/updating-data.md):** Ensure users are authorized to call Server Actions. Review the recommended [security practices](/blog/security-nextjs-server-components-actions).

- **[Environment Variables](/docs/app/guides/environment-variables.md):** Ensure your `.env.*` files are added to `.gitignore` and only public variables are prefixed with `NEXT_PUBLIC_`.
- **[Content Security Policy](/docs/app/guides/content-security-policy.md):** Consider adding a Content Security Policy to protect your application against various security threats such as cross-site scripting, clickjacking, and other code injection attacks.

### Metadata and SEO

* **[Metadata API](/docs/app/getting-started/metadata-and-og-images.md):** Use the Metadata API to improve your application's Search Engine Optimization (SEO) by adding page titles, descriptions, and more.
* **[Open Graph (OG) images](/docs/app/api-reference/file-conventions/metadata/opengraph-image.md):** Create OG images to prepare your application for social sharing.
* **[Sitemaps](/docs/app/api-reference/functions/generate-sitemaps.md) and [Robots](/docs/app/api-reference/file-conventions/metadata/robots.md):** Help Search Engines crawl and index your pages by generating sitemaps and robots files.

### Type safety

* **TypeScript and [TS Plugin](/docs/app/api-reference/config/typescript.md):** Use TypeScript and the TypeScript plugin for better type-safety, and to help you catch errors early.

## Before going to production

Before going to production, you can run `next build` to build your application locally and catch any build errors, then run `next start` to measure the performance of your application in a production-like environment.

### Core Web Vitals

* **[Lighthouse](https://developers.google.com/web/tools/lighthouse):** Run lighthouse in incognito to gain a better understanding of how your users will experience your site, and to identify areas for improvement. This is a simulated test and should be paired with looking at field data (such as Core Web Vitals).

- **[`useReportWebVitals` hook](/docs/app/api-reference/functions/use-report-web-vitals.md):** Use this hook to send [Core Web Vitals](https://web.dev/articles/vitals) data to analytics tools.

### Analyzing bundles

Use the [`@next/bundle-analyzer` plugin](/docs/app/guides/package-bundling.md#analyzing-javascript-bundles) to analyze the size of your JavaScript bundles and identify large modules and dependencies that might be impacting your application's performance.

Additionally, the following tools can help you understand the impact of adding new dependencies to your application:

* [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
* [Package Phobia](https://packagephobia.com/)
* [Bundle Phobia](https://bundlephobia.com/)
* [bundlejs](https://bundlejs.com/)


--------------------------------------------------------------------------------
title: "How to build a Progressive Web Application (PWA) with Next.js"
description: "Learn how to build a Progressive Web Application (PWA) with Next.js."
source: "https://nextjs.org/docs/app/guides/progressive-web-apps"
--------------------------------------------------------------------------------

# PWAs

Progressive Web Applications (PWAs) offer the reach and accessibility of web applications combined with the features and user experience of native mobile apps. With Next.js, you can create PWAs that provide a seamless, app-like experience across all platforms without the need for multiple codebases or app store approvals.

PWAs allow you to:

* Deploy updates instantly without waiting for app store approval
* Create cross-platform applications with a single codebase
* Provide native-like features such as home screen installation and push notifications

## Creating a PWA with Next.js

### 1. Creating the Web App Manifest

Next.js provides built-in support for creating a [web app manifest](/docs/app/api-reference/file-conventions/metadata/manifest.md) using the App Router. You can create either a static or dynamic manifest file:

For example, create a `app/manifest.ts` or `app/manifest.json` file:

```tsx filename="app/manifest.ts" switcher
import type { MetadataRoute } from 'next'

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Next.js PWA',
    short_name: 'NextPWA',
    description: 'A Progressive Web App built with Next.js',
    start_url: '/',
    display: 'standalone',
    background_color: '#ffffff',
    theme_color: '#000000',
    icons: [
      {
        src: '/icon-192x192.png',
        sizes: '192x192',
        type: 'image/png',
      },
      {
        src: '/icon-512x512.png',
        sizes: '512x512',
        type: 'image/png',
      },
    ],
  }
}
```

```jsx filename="app/manifest.js" switcher
export default function manifest() {
  return {
    name: 'Next.js PWA',
    short_name: 'NextPWA',
    description: 'A Progressive Web App built with Next.js',
    start_url: '/',
    display: 'standalone',
    background_color: '#ffffff',
    theme_color: '#000000',
    icons: [
      {
        src: '/icon-192x192.png',
        sizes: '192x192',
        type: 'image/png',
      },
      {
        src: '/icon-512x512.png',
        sizes: '512x512',
        type: 'image/png',
      },
    ],
  }
}
```

This file should contain information about the name, icons, and how it should be displayed as an icon on the user's device. This will allow users to install your PWA on their home screen, providing a native app-like experience.

You can use tools like [favicon generators](https://realfavicongenerator.net/) to create the different icon sets and place the generated files in your `public/` folder.

### 2. Implementing Web Push Notifications

Web Push Notifications are supported with all modern browsers, including:

* iOS 16.4+ for applications installed to the home screen
* Safari 16 for macOS 13 or later
* Chromium based browsers
* Firefox

This makes PWAs a viable alternative to native apps. Notably, you can trigger install prompts without needing offline support.

Web Push Notifications allow you to re-engage users even when they're not actively using your app. Here's how to implement them in a Next.js application:

First, let's create the main page component in `app/page.tsx`. We'll break it down into smaller parts for better understanding. First, we’ll add some of the imports and utilities we’ll need. It’s okay that the referenced Server Actions do not yet exist:

```tsx switcher
'use client'

import { useState, useEffect } from 'react'
import { subscribeUser, unsubscribeUser, sendNotification } from './actions'

function urlBase64ToUint8Array(base64String: string) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
  const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/')

  const rawData = window.atob(base64)
  const outputArray = new Uint8Array(rawData.length)

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i)
  }
  return outputArray
}
```

```jsx switcher
'use client'

import { useState, useEffect } from 'react'
import { subscribeUser, unsubscribeUser, sendNotification } from './actions'

function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - (base64String.length % 4)) % 4)
  const base64 = (base64String + padding)
    .replace(/\\-/g, '+')
    .replace(/_/g, '/')

  const rawData = window.atob(base64)
  const outputArray = new Uint8Array(rawData.length)

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i)
  }
  return outputArray
}
```

Let’s now add a component to manage subscribing, unsubscribing, and sending push notifications.

```tsx switcher
function PushNotificationManager() {
  const [isSupported, setIsSupported] = useState(false)
  const [subscription, setSubscription] = useState<PushSubscription | null>(
    null
  )
  const [message, setMessage] = useState('')

  useEffect(() => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
      setIsSupported(true)
      registerServiceWorker()
    }
  }, [])

  async function registerServiceWorker() {
    const registration = await navigator.serviceWorker.register('/sw.js', {
      scope: '/',
      updateViaCache: 'none',
    })
    const sub = await registration.pushManager.getSubscription()
    setSubscription(sub)
  }

  async function subscribeToPush() {
    const registration = await navigator.serviceWorker.ready
    const sub = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(
        process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!
      ),
    })
    setSubscription(sub)
    const serializedSub = JSON.parse(JSON.stringify(sub))
    await subscribeUser(serializedSub)
  }

  async function unsubscribeFromPush() {
    await subscription?.unsubscribe()
    setSubscription(null)
    await unsubscribeUser()
  }

  async function sendTestNotification() {
    if (subscription) {
      await sendNotification(message)
      setMessage('')
    }
  }

  if (!isSupported) {
    return <p>Push notifications are not supported in this browser.</p>
  }

  return (
    <div>
      <h3>Push Notifications</h3>
      {subscription ? (
        <>
          <p>You are subscribed to push notifications.</p>
          <button onClick={unsubscribeFromPush}>Unsubscribe</button>
          <input
            type="text"
            placeholder="Enter notification message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button onClick={sendTestNotification}>Send Test</button>
        </>
      ) : (
        <>
          <p>You are not subscribed to push notifications.</p>
          <button onClick={subscribeToPush}>Subscribe</button>
        </>
      )}
    </div>
  )
}
```

```jsx switcher
function PushNotificationManager() {
  const [isSupported, setIsSupported] = useState(false);
  const [subscription, setSubscription] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    if ('serviceWorker' in navigator && 'PushManager' in window) {
      setIsSupported(true);
      registerServiceWorker();
    }
  }, []);

  async function registerServiceWorker() {
    const registration = await navigator.serviceWorker.register('/sw.js', {
      scope: '/',
      updateViaCache: 'none',
    });
    const sub = await registration.pushManager.getSubscription();
    setSubscription(sub);
  }

  async function subscribeToPush() {
    const registration = await navigator.serviceWorker.ready;
    const sub = await registration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey: urlBase64ToUint8Array(
        process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!
      ),
    });
    setSubscription(sub);
    await subscribeUser(sub);
  }

  async function unsubscribeFromPush() {
    await subscription?.unsubscribe();
    setSubscription(null);
    await unsubscribeUser();
  }

  async function sendTestNotification() {
    if (subscription) {
      await sendNotification(message);
      setMessage('');
    }
  }

  if (!isSupported) {
    return <p>Push notifications are not supported in this browser.</p>;
  }

  return (
    <div>
      <h3>Push Notifications</h3>
      {subscription ? (
        <>
          <p>You are subscribed to push notifications.</p>
          <button onClick={unsubscribeFromPush}>Unsubscribe</button>
          <input
            type="text"
            placeholder="Enter notification message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
          />
          <button onClick={sendTestNotification}>Send Test</button>
        </>
      ) : (
        <>
          <p>You are not subscribed to push notifications.</p>
          <button onClick={subscribeToPush}>Subscribe</button>
        </>
      )}
    </div>
  );
}
```

Finally, let’s create a component to show a message for iOS devices to instruct them to install to their home screen, and only show this if the app is not already installed.

```tsx switcher
function InstallPrompt() {
  const [isIOS, setIsIOS] = useState(false)
  const [isStandalone, setIsStandalone] = useState(false)

  useEffect(() => {
    setIsIOS(
      /iPad|iPhone|iPod/.test(navigator.userAgent) && !(window as any).MSStream
    )

    setIsStandalone(window.matchMedia('(display-mode: standalone)').matches)
  }, [])

  if (isStandalone) {
    return null // Don't show install button if already installed
  }

  return (
    <div>
      <h3>Install App</h3>
      <button>Add to Home Screen</button>
      {isIOS && (
        <p>
          To install this app on your iOS device, tap the share button
          <span role="img" aria-label="share icon">
            {' '}
            ⎋{' '}
          </span>
          and then "Add to Home Screen"
          <span role="img" aria-label="plus icon">
            {' '}
            ➕{' '}
          </span>
          .
        </p>
      )}
    </div>
  )
}

export default function Page() {
  return (
    <div>
      <PushNotificationManager />
      <InstallPrompt />
    </div>
  )
}
```

```jsx switcher
function InstallPrompt() {
  const [isIOS, setIsIOS] = useState(false);
  const [isStandalone, setIsStandalone] = useState(false);

  useEffect(() => {
    setIsIOS(
      /iPad|iPhone|iPod/.test(navigator.userAgent) && !(window as any).MSStream
    );

    setIsStandalone(window.matchMedia('(display-mode: standalone)').matches);
  }, []);

  if (isStandalone) {
    return null; // Don't show install button if already installed
  }

  return (
    <div>
      <h3>Install App</h3>
      <button>Add to Home Screen</button>
      {isIOS && (
        <p>
          To install this app on your iOS device, tap the share button
          <span role="img" aria-label="share icon">
            {' '}
            ⎋{' '}
          </span>
          and then "Add to Home Screen"
          <span role="img" aria-label="plus icon">
            {' '}
            ➕{' '}
          </span>
          .
        </p>
      )}
    </div>
  );
}

export default function Page() {
  return (
    <div>
      <PushNotificationManager />
      <InstallPrompt />
    </div>
  );
}
```

Now, let’s create the Server Actions which this file calls.

### 3. Implementing Server Actions

Create a new file to contain your actions at `app/actions.ts`. This file will handle creating subscriptions, deleting subscriptions, and sending notifications.

```tsx filename="app/actions.ts" switcher
'use server'

import webpush from 'web-push'

webpush.setVapidDetails(
  '<mailto:your-email@example.com>',
  process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!,
  process.env.VAPID_PRIVATE_KEY!
)

let subscription: PushSubscription | null = null

export async function subscribeUser(sub: PushSubscription) {
  subscription = sub
  // In a production environment, you would want to store the subscription in a database
  // For example: await db.subscriptions.create({ data: sub })
  return { success: true }
}

export async function unsubscribeUser() {
  subscription = null
  // In a production environment, you would want to remove the subscription from the database
  // For example: await db.subscriptions.delete({ where: { ... } })
  return { success: true }
}

export async function sendNotification(message: string) {
  if (!subscription) {
    throw new Error('No subscription available')
  }

  try {
    await webpush.sendNotification(
      subscription,
      JSON.stringify({
        title: 'Test Notification',
        body: message,
        icon: '/icon.png',
      })
    )
    return { success: true }
  } catch (error) {
    console.error('Error sending push notification:', error)
    return { success: false, error: 'Failed to send notification' }
  }
}
```

```jsx filename="app/actions.js" switcher
'use server';

import webpush from 'web-push';

webpush.setVapidDetails(
  '<mailto:your-email@example.com>',
  process.env.NEXT_PUBLIC_VAPID_PUBLIC_KEY!,
  process.env.VAPID_PRIVATE_KEY!
);

let subscription= null;

export async function subscribeUser(sub) {
  subscription = sub;
  // In a production environment, you would want to store the subscription in a database
  // For example: await db.subscriptions.create({ data: sub })
  return { success: true };
}

export async function unsubscribeUser() {
  subscription = null;
  // In a production environment, you would want to remove the subscription from the database
  // For example: await db.subscriptions.delete({ where: { ... } })
  return { success: true };
}

export async function sendNotification(message) {
  if (!subscription) {
    throw new Error('No subscription available');
  }

  try {
    await webpush.sendNotification(
      subscription,
      JSON.stringify({
        title: 'Test Notification',
        body: message,
        icon: '/icon.png',
      })
    );
    return { success: true };
  } catch (error) {
    console.error('Error sending push notification:', error);
    return { success: false, error: 'Failed to send notification' };
  }
}
```

Sending a notification will be handled by our service worker, created in step 5.

In a production environment, you would want to store the subscription in a database for persistence across server restarts and to manage multiple users' subscriptions.

### 4. Generating VAPID Keys

To use the Web Push API, you need to generate [VAPID](https://vapidkeys.com/) keys. The simplest way is to use the web-push CLI directly:

First, install web-push globally:

```bash filename="Terminal"
npm install -g web-push
```

Generate the VAPID keys by running:

```bash filename="Terminal"
web-push generate-vapid-keys
```

Copy the output and paste the keys into your `.env` file:

```
NEXT_PUBLIC_VAPID_PUBLIC_KEY=your_public_key_here
VAPID_PRIVATE_KEY=your_private_key_here
```

### 5. Creating a Service Worker

Create a `public/sw.js` file for your service worker:

```js filename="public/sw.js"
self.addEventListener('push', function (event) {
  if (event.data) {
    const data = event.data.json()
    const options = {
      body: data.body,
      icon: data.icon || '/icon.png',
      badge: '/badge.png',
      vibrate: [100, 50, 100],
      data: {
        dateOfArrival: Date.now(),
        primaryKey: '2',
      },
    }
    event.waitUntil(self.registration.showNotification(data.title, options))
  }
})

self.addEventListener('notificationclick', function (event) {
  console.log('Notification click received.')
  event.notification.close()
  event.waitUntil(clients.openWindow('<https://your-website.com>'))
})
```

This service worker supports custom images and notifications. It handles incoming push events and notification clicks.

* You can set custom icons for notifications using the `icon` and `badge` properties.
* The `vibrate` pattern can be adjusted to create custom vibration alerts on supported devices.
* Additional data can be attached to the notification using the `data` property.

Remember to test your service worker thoroughly to ensure it behaves as expected across different devices and browsers. Also, make sure to update the `'https://your-website.com'` link in the `notificationclick` event listener to the appropriate URL for your application.

### 6. Adding to Home Screen

The `InstallPrompt` component defined in step 2 shows a message for iOS devices to instruct them to install to their home screen.

To ensure your application can be installed to a mobile home screen, you must have:

1. A valid web app manifest (created in step 1)
2. The website served over HTTPS

Modern browsers will automatically show an installation prompt to users when these criteria are met. You can provide a custom installation button with [`beforeinstallprompt`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeinstallprompt_event), however, we do not recommend this as it is not cross browser and platform (does not work on Safari iOS).

### 7. Testing Locally

To ensure you can view notifications locally, ensure that:

* You are [running locally with HTTPS](/docs/app/api-reference/cli/next.md#using-https-during-development)
  * Use `next dev --experimental-https` for testing
* Your browser (Chrome, Safari, Firefox) has notifications enabled
  * When prompted locally, accept permissions to use notifications
  * Ensure notifications are not disabled globally for the entire browser
  * If you are still not seeing notifications, try using another browser to debug

### 8. Securing your application

Security is a crucial aspect of any web application, especially for PWAs. Next.js allows you to configure security headers using the `next.config.js` file. For example:

```js filename="next.config.js"
module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'Referrer-Policy',
            value: 'strict-origin-when-cross-origin',
          },
        ],
      },
      {
        source: '/sw.js',
        headers: [
          {
            key: 'Content-Type',
            value: 'application/javascript; charset=utf-8',
          },
          {
            key: 'Cache-Control',
            value: 'no-cache, no-store, must-revalidate',
          },
          {
            key: 'Content-Security-Policy',
            value: "default-src 'self'; script-src 'self'",
          },
        ],
      },
    ]
  },
}
```

Let’s go over each of these options:

1. Global Headers (applied to all routes):
   1. `X-Content-Type-Options: nosniff`: Prevents MIME type sniffing, reducing the risk of malicious file uploads.
   2. `X-Frame-Options: DENY`: Protects against clickjacking attacks by preventing your site from being embedded in iframes.
   3. `Referrer-Policy: strict-origin-when-cross-origin`: Controls how much referrer information is included with requests, balancing security and functionality.
2. Service Worker Specific Headers:
   1. `Content-Type: application/javascript; charset=utf-8`: Ensures the service worker is interpreted correctly as JavaScript.
   2. `Cache-Control: no-cache, no-store, must-revalidate`: Prevents caching of the service worker, ensuring users always get the latest version.
   3. `Content-Security-Policy: default-src 'self'; script-src 'self'`: Implements a strict Content Security Policy for the service worker, only allowing scripts from the same origin.

Learn more about defining [Content Security Policies](/docs/app/guides/content-security-policy.md) with Next.js.

## Extending your PWA

1. **Exploring PWA Capabilities**: PWAs can leverage various web APIs to provide advanced functionality. Consider exploring features like background sync, periodic background sync, or the File System Access API to enhance your application. For inspiration and up-to-date information on PWA capabilities, you can refer to resources like [What PWA Can Do Today](https://whatpwacando.today/).
2. **Static Exports:** If your application requires not running a server, and instead using a static export of files, you can update the Next.js configuration to enable this change. Learn more in the [Next.js Static Export documentation](/docs/app/guides/static-exports.md). However, you will need to move from Server Actions to calling an external API, as well as moving your defined headers to your proxy.
3. **Offline Support**: To provide offline functionality, one option is [Serwist](https://github.com/serwist/serwist) with Next.js. You can find an example of how to integrate Serwist with Next.js in their [documentation](https://github.com/serwist/serwist/tree/main/examples/next-basic). **Note:** this plugin currently requires webpack configuration.
4. **Security Considerations**: Ensure that your service worker is properly secured. This includes using HTTPS, validating the source of push messages, and implementing proper error handling.
5. **User Experience**: Consider implementing progressive enhancement techniques to ensure your app works well even when certain PWA features are not supported by the user's browser.
- [manifest.json](/docs/app/api-reference/file-conventions/metadata/manifest.md)
  - API Reference for manifest.json file.


--------------------------------------------------------------------------------
title: "How to handle redirects in Next.js"
description: "Learn the different ways to handle redirects in Next.js."
source: "https://nextjs.org/docs/app/guides/redirecting"
--------------------------------------------------------------------------------

# Redirecting

There are a few ways you can handle redirects in Next.js. This page will go through each available option, use cases, and how to manage large numbers of redirects.

| API                                                           | Purpose                                           | Where                                             | Status Code                            |
| ------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | -------------------------------------- |
| [`redirect`](#redirect-function)                              | Redirect user after a mutation or event           | Server Components, Server Actions, Route Handlers | 307 (Temporary) or 303 (Server Action) |
| [`permanentRedirect`](#permanentredirect-function)            | Redirect user after a mutation or event           | Server Components, Server Actions, Route Handlers | 308 (Permanent)                        |
| [`useRouter`](#userouter-hook)                                | Perform a client-side navigation                  | Event Handlers in Client Components               | N/A                                    |
| [`redirects` in `next.config.js`](#redirects-in-nextconfigjs) | Redirect an incoming request based on a path      | `next.config.js` file                             | 307 (Temporary) or 308 (Permanent)     |
| [`NextResponse.redirect`](#nextresponseredirect-in-proxy)     | Redirect an incoming request based on a condition | Proxy                                             | Any                                    |

## `redirect` function

The `redirect` function allows you to redirect the user to another URL. You can call `redirect` in [Server Components](/docs/app/getting-started/server-and-client-components.md), [Route Handlers](/docs/app/api-reference/file-conventions/route.md), and [Server Actions](/docs/app/getting-started/updating-data.md).

`redirect` is often used after a mutation or event. For example, creating a post:

```ts filename="app/actions.ts" switcher
'use server'

import { redirect } from 'next/navigation'
import { revalidatePath } from 'next/cache'

export async function createPost(id: string) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidatePath('/posts') // Update cached posts
  redirect(`/post/${id}`) // Navigate to the new post page
}
```

```js filename="app/actions.js" switcher
'use server'

import { redirect } from 'next/navigation'
import { revalidatePath } from 'next/cache'

export async function createPost(id) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidatePath('/posts') // Update cached posts
  redirect(`/post/${id}`) // Navigate to the new post page
}
```

> **Good to know**:
>
> * `redirect` returns a 307 (Temporary Redirect) status code by default. When used in a Server Action, it returns a 303 (See Other), which is commonly used for redirecting to a success page as a result of a POST request.
> * `redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.
> * `redirect` can be called in Client Components during the rendering process but not in event handlers. You can use the [`useRouter` hook](#userouter-hook) instead.
> * `redirect` also accepts absolute URLs and can be used to redirect to external links.
> * If you'd like to redirect before the render process, use [`next.config.js`](#redirects-in-nextconfigjs) or [Proxy](#nextresponseredirect-in-proxy).

See the [`redirect` API reference](/docs/app/api-reference/functions/redirect.md) for more information.

## `permanentRedirect` function

The `permanentRedirect` function allows you to **permanently** redirect the user to another URL. You can call `permanentRedirect` in [Server Components](/docs/app/getting-started/server-and-client-components.md), [Route Handlers](/docs/app/api-reference/file-conventions/route.md), and [Server Actions](/docs/app/getting-started/updating-data.md).

`permanentRedirect` is often used after a mutation or event that changes an entity's canonical URL, such as updating a user's profile URL after they change their username:

```ts filename="app/actions.ts" switcher
'use server'

import { permanentRedirect } from 'next/navigation'
import { revalidateTag } from 'next/cache'

export async function updateUsername(username: string, formData: FormData) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidateTag('username') // Update all references to the username
  permanentRedirect(`/profile/${username}`) // Navigate to the new user profile
}
```

```js filename="app/actions.js" switcher
'use server'

import { permanentRedirect } from 'next/navigation'
import { revalidateTag } from 'next/cache'

export async function updateUsername(username, formData) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidateTag('username') // Update all references to the username
  permanentRedirect(`/profile/${username}`) // Navigate to the new user profile
}
```

> **Good to know**:
>
> * `permanentRedirect` returns a 308 (permanent redirect) status code by default.
> * `permanentRedirect` also accepts absolute URLs and can be used to redirect to external links.
> * If you'd like to redirect before the render process, use [`next.config.js`](#redirects-in-nextconfigjs) or [Proxy](#nextresponseredirect-in-proxy).

See the [`permanentRedirect` API reference](/docs/app/api-reference/functions/permanentRedirect.md) for more information.

## `useRouter()` hook

If you need to redirect inside an event handler in a Client Component, you can use the `push` method from the `useRouter` hook. For example:

```tsx filename="app/page.tsx" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

```jsx filename="app/page.js" switcher
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

> **Good to know**:
>
> * If you don't need to programmatically navigate a user, you should use a [`<Link>`](/docs/app/api-reference/components/link.md) component.

See the [`useRouter` API reference](/docs/app/api-reference/functions/use-router.md) for more information.

## `redirects` in `next.config.js`

The `redirects` option in the `next.config.js` file allows you to redirect an incoming request path to a different destination path. This is useful when you change the URL structure of pages or have a list of redirects that are known ahead of time.

`redirects` supports [path](/docs/app/api-reference/config/next-config-js/redirects.md#path-matching), [header, cookie, and query matching](/docs/app/api-reference/config/next-config-js/redirects.md#header-cookie-and-query-matching), giving you the flexibility to redirect users based on an incoming request.

To use `redirects`, add the option to your `next.config.js` file:

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async redirects() {
    return [
      // Basic redirect
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      // Wildcard path matching
      {
        source: '/blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
    ]
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
module.exports = {
  async redirects() {
    return [
      // Basic redirect
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      // Wildcard path matching
      {
        source: '/blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
    ]
  },
}
```

See the [`redirects` API reference](/docs/app/api-reference/config/next-config-js/redirects.md) for more information.

> **Good to know**:
>
> * `redirects` can return a 307 (Temporary Redirect) or 308 (Permanent Redirect) status code with the `permanent` option.
> * `redirects` may have a limit on platforms. For example, on Vercel, there's a limit of 1,024 redirects. To manage a large number of redirects (1000+), consider creating a custom solution using [Proxy](/docs/app/api-reference/file-conventions/proxy.md). See [managing redirects at scale](#managing-redirects-at-scale-advanced) for more.
> * `redirects` runs **before** Proxy.

## `NextResponse.redirect` in Proxy

Proxy allows you to run code before a request is completed. Then, based on the incoming request, redirect to a different URL using `NextResponse.redirect`. This is useful if you want to redirect users based on a condition (e.g. authentication, session management, etc) or have [a large number of redirects](#managing-redirects-at-scale-advanced).

For example, to redirect the user to a `/login` page if they are not authenticated:

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { authenticate } from 'auth-provider'

export function proxy(request: NextRequest) {
  const isAuthenticated = authenticate(request)

  // If the user is authenticated, continue as normal
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Redirect to login page if not authenticated
  return NextResponse.redirect(new URL('/login', request.url))
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { authenticate } from 'auth-provider'

export function proxy(request) {
  const isAuthenticated = authenticate(request)

  // If the user is authenticated, continue as normal
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Redirect to login page if not authenticated
  return NextResponse.redirect(new URL('/login', request.url))
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

> **Good to know**:
>
> * Proxy runs **after** `redirects` in `next.config.js` and **before** rendering.

See the [Proxy](/docs/app/api-reference/file-conventions/proxy.md) documentation for more information.

## Managing redirects at scale (advanced)

To manage a large number of redirects (1000+), you may consider creating a custom solution using Proxy. This allows you to handle redirects programmatically without having to redeploy your application.

To do this, you'll need to consider:

1. Creating and storing a redirect map.
2. Optimizing data lookup performance.

> **Next.js Example**: See our [Proxy with Bloom filter](https://redirects-bloom-filter.vercel.app/) example for an implementation of the recommendations below.

### 1. Creating and storing a redirect map

A redirect map is a list of redirects that you can store in a database (usually a key-value store) or JSON file.

Consider the following data structure:

```json
{
  "/old": {
    "destination": "/new",
    "permanent": true
  },
  "/blog/post-old": {
    "destination": "/blog/post-new",
    "permanent": true
  }
}
```

In [Proxy](/docs/app/api-reference/file-conventions/proxy.md), you can read from a database such as Vercel's [Edge Config](https://vercel.com/docs/edge-config/get-started) or [Redis](https://vercel.com/docs/redis), and redirect the user based on the incoming request:

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { get } from '@vercel/edge-config'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export async function proxy(request: NextRequest) {
  const pathname = request.nextUrl.pathname
  const redirectData = await get(pathname)

  if (redirectData && typeof redirectData === 'string') {
    const redirectEntry: RedirectEntry = JSON.parse(redirectData)
    const statusCode = redirectEntry.permanent ? 308 : 307
    return NextResponse.redirect(redirectEntry.destination, statusCode)
  }

  // No redirect found, continue without redirecting
  return NextResponse.next()
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { get } from '@vercel/edge-config'

export async function proxy(request) {
  const pathname = request.nextUrl.pathname
  const redirectData = await get(pathname)

  if (redirectData) {
    const redirectEntry = JSON.parse(redirectData)
    const statusCode = redirectEntry.permanent ? 308 : 307
    return NextResponse.redirect(redirectEntry.destination, statusCode)
  }

  // No redirect found, continue without redirecting
  return NextResponse.next()
}
```

### 2. Optimizing data lookup performance

Reading a large dataset for every incoming request can be slow and expensive. There are two ways you can optimize data lookup performance:

* Use a database that is optimized for fast reads
* Use a data lookup strategy such as a [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) to efficiently check if a redirect exists **before** reading the larger redirects file or database.

Considering the previous example, you can import a generated bloom filter file into Proxy, then, check if the incoming request pathname exists in the bloom filter.

If it does, forward the request to a [Route Handler](/docs/app/api-reference/file-conventions/route.md)  which will check the actual file and redirect the user to the appropriate URL. This avoids importing a large redirects file into Proxy, which can slow down every incoming request.

```ts filename="proxy.ts" switcher
import { NextResponse, NextRequest } from 'next/server'
import { ScalableBloomFilter } from 'bloom-filters'
import GeneratedBloomFilter from './redirects/bloom-filter.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

// Initialize bloom filter from a generated JSON file
const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter as any)

export async function proxy(request: NextRequest) {
  // Get the path for the incoming request
  const pathname = request.nextUrl.pathname

  // Check if the path is in the bloom filter
  if (bloomFilter.has(pathname)) {
    // Forward the pathname to the Route Handler
    const api = new URL(
      `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
      request.nextUrl.origin
    )

    try {
      // Fetch redirect data from the Route Handler
      const redirectData = await fetch(api)

      if (redirectData.ok) {
        const redirectEntry: RedirectEntry | undefined =
          await redirectData.json()

        if (redirectEntry) {
          // Determine the status code
          const statusCode = redirectEntry.permanent ? 308 : 307

          // Redirect to the destination
          return NextResponse.redirect(redirectEntry.destination, statusCode)
        }
      }
    } catch (error) {
      console.error(error)
    }
  }

  // No redirect found, continue the request without redirecting
  return NextResponse.next()
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { ScalableBloomFilter } from 'bloom-filters'
import GeneratedBloomFilter from './redirects/bloom-filter.json'

// Initialize bloom filter from a generated JSON file
const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter)

export async function proxy(request) {
  // Get the path for the incoming request
  const pathname = request.nextUrl.pathname

  // Check if the path is in the bloom filter
  if (bloomFilter.has(pathname)) {
    // Forward the pathname to the Route Handler
    const api = new URL(
      `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
      request.nextUrl.origin
    )

    try {
      // Fetch redirect data from the Route Handler
      const redirectData = await fetch(api)

      if (redirectData.ok) {
        const redirectEntry = await redirectData.json()

        if (redirectEntry) {
          // Determine the status code
          const statusCode = redirectEntry.permanent ? 308 : 307

          // Redirect to the destination
          return NextResponse.redirect(redirectEntry.destination, statusCode)
        }
      }
    } catch (error) {
      console.error(error)
    }
  }

  // No redirect found, continue the request without redirecting
  return NextResponse.next()
}
```

Then, in the Route Handler:

```ts filename="app/api/redirects/route.ts" switcher
import { NextRequest, NextResponse } from 'next/server'
import redirects from '@/app/redirects/redirects.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export function GET(request: NextRequest) {
  const pathname = request.nextUrl.searchParams.get('pathname')
  if (!pathname) {
    return new Response('Bad Request', { status: 400 })
  }

  // Get the redirect entry from the redirects.json file
  const redirect = (redirects as Record<string, RedirectEntry>)[pathname]

  // Account for bloom filter false positives
  if (!redirect) {
    return new Response('No redirect', { status: 400 })
  }

  // Return the redirect entry
  return NextResponse.json(redirect)
}
```

```js filename="app/api/redirects/route.js" switcher
import { NextResponse } from 'next/server'
import redirects from '@/app/redirects/redirects.json'

export function GET(request) {
  const pathname = request.nextUrl.searchParams.get('pathname')
  if (!pathname) {
    return new Response('Bad Request', { status: 400 })
  }

  // Get the redirect entry from the redirects.json file
  const redirect = redirects[pathname]

  // Account for bloom filter false positives
  if (!redirect) {
    return new Response('No redirect', { status: 400 })
  }

  // Return the redirect entry
  return NextResponse.json(redirect)
}
```

> **Good to know:**
>
> * To generate a bloom filter, you can use a library like [`bloom-filters`](https://www.npmjs.com/package/bloom-filters).
> * You should validate requests made to your Route Handler to prevent malicious requests.
- [redirect](/docs/app/api-reference/functions/redirect.md)
  - API Reference for the redirect function.
- [permanentRedirect](/docs/app/api-reference/functions/permanentRedirect.md)
  - API Reference for the permanentRedirect function.
- [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
  - API reference for the proxy.js file.
- [redirects](/docs/app/api-reference/config/next-config-js/redirects.md)
  - Add redirects to your Next.js app.


--------------------------------------------------------------------------------
title: "How to use Sass"
description: "Style your Next.js application using Sass."
source: "https://nextjs.org/docs/app/guides/sass"
--------------------------------------------------------------------------------

# Sass

Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.

First, install [`sass`](https://github.com/sass/sass):

```bash filename="Terminal"
npm install --save-dev sass
```

> **Good to know**:
>
> Sass supports [two different syntaxes](https://sass-lang.com/documentation/syntax), each with their own extension.
> The `.scss` extension requires you use the [SCSS syntax](https://sass-lang.com/documentation/syntax#scss),
> while the `.sass` extension requires you use the [Indented Syntax ("Sass")](https://sass-lang.com/documentation/syntax#the-indented-syntax).
>
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the
> Indented Syntax ("Sass").

### Customizing Sass Options

If you want to configure your Sass options, use `sassOptions` in `next.config`.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const nextConfig = {
  sassOptions: {
    additionalData: `$var: red;`,
  },
}

module.exports = nextConfig
```

#### Implementation

You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the [`sass`](https://www.npmjs.com/package/sass) package.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const nextConfig = {
  sassOptions: {
    implementation: 'sass-embedded',
  },
}

module.exports = nextConfig
```

### Sass Variables

Next.js supports Sass variables exported from CSS Module files.

For example, using the exported `primaryColor` Sass variable:

```scss filename="app/variables.module.scss"
$primary-color: #64ff00;

:export {
  primaryColor: $primary-color;
}
```

```jsx filename="app/page.js"
// maps to root `/` URL

import variables from './variables.module.scss'

export default function Page() {
  return <h1 style={{ color: variables.primaryColor }}>Hello, Next.js!</h1>
}
```


--------------------------------------------------------------------------------
title: "How to load and optimize scripts"
description: "Optimize 3rd party scripts with the built-in Script component."
source: "https://nextjs.org/docs/app/guides/scripts"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./03-content-security-policy.md) | [Index](./index.md) | [Next →](./05-scripts.md)
