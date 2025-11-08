**Navigation:** [← Previous](./06-videos.md) | [Index](./index.md) | [Next →](./08-routejs.md)

---

# Link Component

`<Link>` is a React component that extends the HTML `<a>` element to provide [prefetching](/docs/app/getting-started/linking-and-navigating.md#prefetching) and client-side navigation between routes. It is the primary way to navigate between routes in Next.js.

Basic usage:

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}
```

## Reference

The following props can be passed to the `<Link>` component:

| Prop                        | Example                  | Type             | Required |
| --------------------------- | ------------------------ | ---------------- | -------- |
| [`href`](#href-required)    | `href="/dashboard"`      | String or Object | Yes      |
| [`replace`](#replace)       | `replace={false}`        | Boolean          | -        |
| [`scroll`](#scroll)         | `scroll={false}`         | Boolean          | -        |
| [`prefetch`](#prefetch)     | `prefetch={false}`       | Boolean or null  | -        |
| [`onNavigate`](#onnavigate) | `onNavigate={(e) => {}}` | Function         | -        |

> **Good to know**: `<a>` tag attributes such as `className` or `target="_blank"` can be added to `<Link>` as props and will be passed to the underlying `<a>` element.

### `href` (required)

The path or URL to navigate to.

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

// Navigate to /about?name=test
export default function Page() {
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

```jsx filename="app/page.js" switcher
import Link from 'next/link'

// Navigate to /about?name=test
export default function Page() {
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

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" replace>
      Dashboard
    </Link>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
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

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" scroll={false}>
      Dashboard
    </Link>
  )
}
```

### `prefetch`

Prefetching happens when a `<Link />` component enters the user's viewport (initially or through scroll). Next.js prefetches and loads the linked route (denoted by the `href`) and its data in the background to improve the performance of client-side navigations. If the prefetched data has expired by the time the user hovers over a `<Link />`, Next.js will attempt to prefetch it again. **Prefetching is only enabled in production**.

The following values can be passed to the `prefetch` prop:

* **`"auto"` or `null` (default)**: Prefetch behavior depends on whether the route is static or dynamic. For static routes, the full route will be prefetched (including all its data). For dynamic routes, the partial route down to the nearest segment with a [`loading.js`](/docs/app/api-reference/file-conventions/loading.md#instant-loading-states) boundary will be prefetched.
* `true`: The full route will be prefetched for both static and dynamic routes.
* `false`: Prefetching will never happen both on entering the viewport and on hover.

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/dashboard" prefetch={false}>
      Dashboard
    </Link>
  )
}
```

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

When linking to [dynamic segments](/docs/app/api-reference/file-conventions/dynamic-routes.md), you can use [template literals and interpolation](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Template_literals) to generate a list of links. For example, to generate a list of blog posts:

```tsx filename="app/blog/post-list.tsx" switcher
import Link from 'next/link'

interface Post {
  id: number
  title: string
  slug: string
}

export default function PostList({ posts }: { posts: Post[] }) {
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

```jsx filename="app/blog/post-list.js" switcher
import Link from 'next/link'

export default function PostList({ posts }) {
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

### Checking active links

You can use [`usePathname()`](/docs/app/api-reference/functions/use-pathname.md) to determine if a link is active. For example, to add a class to the active link, you can check if the current `pathname` matches the `href` of the link:

```tsx filename="app/ui/nav-links.tsx" switcher
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function Links() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>

      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

```jsx filename="app/ui/nav-links.js" switcher
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function Links() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>

      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

### Scrolling to an `id`

If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `<Link>` renders to an `<a>` element.

```jsx
<Link href="/dashboard#settings">Settings</Link>

// Output
<a href="/dashboard#settings">Settings</a>
```

> **Good to know**:
>
> * Next.js will scroll to the [Page](/docs/app/api-reference/file-conventions/page.md) if it is not visible in the viewport upon navigation.

### Replace the URL instead of push

The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:

```tsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

### Disable scrolling to the top of the page

The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position**, similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](/docs/app/api-reference/file-conventions/page.md), scroll position will stay the same as long as the Page is visible in the viewport.

However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element. If you'd like to disable this behavior, you can pass `scroll={false}` to the `<Link>` component, or `scroll: false` to `router.push()` or `router.replace()`.

```jsx filename="app/page.js" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

```tsx filename="app/page.tsx" switcher
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

Using `router.push()` or `router.replace()`:

```jsx
// useRouter
import { useRouter } from 'next/navigation'

const router = useRouter()

router.push('/dashboard', { scroll: false })
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

```tsx filename="app/page.tsx" switcher
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Page() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

```js filename="app/page.js" switcher
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Page() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

### Blocking navigation

You can use the `onNavigate` prop to block navigation when certain conditions are met, such as when a form has unsaved changes. When you need to block navigation across multiple components in your app (like preventing navigation from any link while a form is being edited), React Context provides a clean way to share this blocking state. First, create a context to track the navigation blocking state:

```tsx filename="app/contexts/navigation-blocker.tsx" switcher
'use client'

import { createContext, useState, useContext } from 'react'

interface NavigationBlockerContextType {
  isBlocked: boolean
  setIsBlocked: (isBlocked: boolean) => void
}

export const NavigationBlockerContext =
  createContext<NavigationBlockerContextType>({
    isBlocked: false,
    setIsBlocked: () => {},
  })

export function NavigationBlockerProvider({
  children,
}: {
  children: React.ReactNode
}) {
  const [isBlocked, setIsBlocked] = useState(false)

  return (
    <NavigationBlockerContext.Provider value={{ isBlocked, setIsBlocked }}>
      {children}
    </NavigationBlockerContext.Provider>
  )
}

export function useNavigationBlocker() {
  return useContext(NavigationBlockerContext)
}
```

```jsx filename="app/contexts/navigation-blocker.js" switcher
'use client'

import { createContext, useState, useContext } from 'react'

export const NavigationBlockerContext = createContext({
  isBlocked: false,
  setIsBlocked: () => {},
})

export function NavigationBlockerProvider({ children }) {
  const [isBlocked, setIsBlocked] = useState(false)

  return (
    <NavigationBlockerContext.Provider value={{ isBlocked, setIsBlocked }}>
      {children}
    </NavigationBlockerContext.Provider>
  )
}

export function useNavigationBlocker() {
  return useContext(NavigationBlockerContext)
}
```

Create a form component that uses the context:

```tsx filename="app/components/form.tsx" switcher
'use client'

import { useNavigationBlocker } from '../contexts/navigation-blocker'

export default function Form() {
  const { setIsBlocked } = useNavigationBlocker()

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        setIsBlocked(false)
      }}
      onChange={() => setIsBlocked(true)}
    >
      <input type="text" name="name" />
      <button type="submit">Save</button>
    </form>
  )
}
```

```jsx filename="app/components/form.js" switcher
'use client'

import { useNavigationBlocker } from '../contexts/navigation-blocker'

export default function Form() {
  const { setIsBlocked } = useNavigationBlocker()

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        setIsBlocked(false)
      }}
      onChange={() => setIsBlocked(true)}
    >
      <input type="text" name="name" />
      <button type="submit">Save</button>
    </form>
  )
}
```

Create a custom Link component that blocks navigation:

```tsx filename="app/components/custom-link.tsx" switcher
'use client'

import Link from 'next/link'
import { useNavigationBlocker } from '../contexts/navigation-blocker'

interface CustomLinkProps extends React.ComponentProps<typeof Link> {
  children: React.ReactNode
}

export function CustomLink({ children, ...props }: CustomLinkProps) {
  const { isBlocked } = useNavigationBlocker()

  return (
    <Link
      onNavigate={(e) => {
        if (
          isBlocked &&
          !window.confirm('You have unsaved changes. Leave anyway?')
        ) {
          e.preventDefault()
        }
      }}
      {...props}
    >
      {children}
    </Link>
  )
}
```

```jsx filename="app/components/custom-link.js" switcher
'use client'

import Link from 'next/link'
import { useNavigationBlocker } from '../contexts/navigation-blocker'

export function CustomLink({ children, ...props }) {
  const { isBlocked } = useNavigationBlocker()

  return (
    <Link
      onNavigate={(e) => {
        if (
          isBlocked &&
          !window.confirm('You have unsaved changes. Leave anyway?')
        ) {
          e.preventDefault()
        }
      }}
      {...props}
    >
      {children}
    </Link>
  )
}
```

Create a navigation component:

```tsx filename="app/components/nav.tsx" switcher
'use client'

import { CustomLink as Link } from './custom-link'

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
    </nav>
  )
}
```

```jsx filename="app/components/nav.js" switcher
'use client'

import { CustomLink as Link } from './custom-link'

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
    </nav>
  )
}
```

Finally, wrap your app with the `NavigationBlockerProvider` in the root layout and use the components in your page:

```tsx filename="app/layout.tsx" switcher
import { NavigationBlockerProvider } from './contexts/navigation-blocker'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <NavigationBlockerProvider>{children}</NavigationBlockerProvider>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { NavigationBlockerProvider } from './contexts/navigation-blocker'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <NavigationBlockerProvider>{children}</NavigationBlockerProvider>
      </body>
    </html>
  )
}
```

Then, use the `Nav` and `Form` components in your page:

```tsx filename="app/page.tsx" switcher
import Nav from './components/nav'
import Form from './components/form'

export default function Page() {
  return (
    <div>
      <Nav />
      <main>
        <h1>Welcome to the Dashboard</h1>
        <Form />
      </main>
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
import Nav from './components/nav'
import Form from './components/form'

export default function Page() {
  return (
    <div>
      <Nav />
      <main>
        <h1>Welcome to the Dashboard</h1>
        <Form />
      </main>
    </div>
  )
}
```

When a user tries to navigate away using `CustomLink` while the form has unsaved changes, they'll be prompted to confirm before leaving.

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
source: "https://nextjs.org/docs/app/api-reference/components/script"
--------------------------------------------------------------------------------

# Script Component

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

`beforeInteractive` scripts must be placed inside the root layout (`app/layout.tsx`) and are designed to load scripts that are needed by the entire site (i.e. the script will load when any page in the application has been loaded server-side).

**This strategy should only be used for critical scripts that need to be fetched as soon as possible.**

```tsx filename="app/layout.tsx" switcher
import Script from 'next/script'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {children}
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        />
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import Script from 'next/script'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}
        <Script
          src="https://example.com/script.js"
          strategy="beforeInteractive"
        />
      </body>
    </html>
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

```tsx filename="app/page.tsx" switcher
'use client'

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

```jsx filename="app/page.js" switcher
'use client'

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

```tsx filename="app/page.tsx" switcher
'use client'

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

```jsx filename="app/page.js" switcher
'use client'

import Script from 'next/script'

export default function Page() {
  return (
    <>
      <Script
        src="https://example.com/script.js"
        onError={(e) => {
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
source: "https://nextjs.org/docs/app/api-reference/file-conventions"
--------------------------------------------------------------------------------

# File-system conventions



 - [default.js](/docs/app/api-reference/file-conventions/default.md)
 - [Dynamic Segments](/docs/app/api-reference/file-conventions/dynamic-routes.md)
 - [error.js](/docs/app/api-reference/file-conventions/error.md)
 - [forbidden.js](/docs/app/api-reference/file-conventions/forbidden.md)
 - [instrumentation.js](/docs/app/api-reference/file-conventions/instrumentation.md)
 - [instrumentation-client.js](/docs/app/api-reference/file-conventions/instrumentation-client.md)
 - [Intercepting Routes](/docs/app/api-reference/file-conventions/intercepting-routes.md)
 - [layout.js](/docs/app/api-reference/file-conventions/layout.md)
 - [loading.js](/docs/app/api-reference/file-conventions/loading.md)
 - [mdx-components.js](/docs/app/api-reference/file-conventions/mdx-components.md)
 - [not-found.js](/docs/app/api-reference/file-conventions/not-found.md)
 - [page.js](/docs/app/api-reference/file-conventions/page.md)
 - [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md)
 - [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
 - [public](/docs/app/api-reference/file-conventions/public-folder.md)
 - [route.js](/docs/app/api-reference/file-conventions/route.md)
 - [Route Groups](/docs/app/api-reference/file-conventions/route-groups.md)
 - [Route Segment Config](/docs/app/api-reference/file-conventions/route-segment-config.md)
 - [src](/docs/app/api-reference/file-conventions/src-folder.md)
 - [template.js](/docs/app/api-reference/file-conventions/template.md)
 - [unauthorized.js](/docs/app/api-reference/file-conventions/unauthorized.md)
 - [Metadata Files](/docs/app/api-reference/file-conventions/metadata.md)

--------------------------------------------------------------------------------
title: "default.js"
description: "API Reference for the default.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/default"
--------------------------------------------------------------------------------

# default.js

The `default.js` file is used to render a fallback within [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md) when Next.js cannot recover a [slot's](/docs/app/api-reference/file-conventions/parallel-routes.md#slots) active state after a full-page load.

During [soft navigation](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions), Next.js keeps track of the active *state* (subpage) for each slot. However, for hard navigations (full-page load), Next.js cannot recover the active state. In this case, a `default.js` file can be rendered for subpages that don't match the current URL.

Consider the following folder structure. The `@team` slot has a `settings` page, but `@analytics` does not.

![Parallel Routes unmatched routes](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-unmatched-routes.png)

When navigating to `/settings`, the `@team` slot will render the `settings` page while maintaining the currently active page for the `@analytics` slot.

On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, an error is returned for named slots (`@team`, `@analytics`, etc) and requires you to define a `default.js` in order to continue. If you want to preserve the old behavior of returning a 404 in these situations, you can create a `default.js` that contains:

```tsx filename="app/@team/default.js"
import { notFound } from 'next/navigation'

export default function Default() {
  notFound()
}
```

Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page. If you don't create a `default.js` for the `children` slot, it will return a 404 page for the route.

## Reference

### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) from the root segment down to the slot's subpages. For example:

```tsx filename="app/[artist]/@sidebar/default.js" switcher
export default async function Default({
  params,
}: {
  params: Promise<{ artist: string }>
}) {
  const { artist } = await params
}
```

```jsx filename="app/[artist]/@sidebar/default.js" switcher
export default async function Default({ params }) {
  const { artist } = await params
}
```

| Example                                    | URL          | `params`                                     |
| ------------------------------------------ | ------------ | -------------------------------------------- |
| `app/[artist]/@sidebar/default.js`         | `/zack`      | `Promise<{ artist: 'zack' }>`                |
| `app/[artist]/[album]/@sidebar/default.js` | `/zack/next` | `Promise<{ artist: 'zack', album: 'next' }>` |

* Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
  * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
## Learn more about Parallel Routes- [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md)
  - Simultaneously render one or more pages in the same view that can be navigated independently. A pattern for highly dynamic applications.


--------------------------------------------------------------------------------
title: "Dynamic Route Segments"
description: "Dynamic Route Segments can be used to programmatically generate route segments from dynamic data."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes"
--------------------------------------------------------------------------------

# Dynamic Segments

When you don't know the exact route segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or prerendered at build time.

## Convention

A Dynamic Segment can be created by wrapping a folder's name in square brackets: `[folderName]`. For example, a blog could include the following route `app/blog/[slug]/page.js` where `[slug]` is the Dynamic Segment for blog posts.

```tsx filename="app/blog/[slug]/page.tsx" switcher
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <div>My Post: {slug}</div>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export default async function Page({ params }) {
  const { slug } = await params
  return <div>My Post: {slug}</div>
}
```

Dynamic Segments are passed as the `params` prop to [`layout`](/docs/app/api-reference/file-conventions/layout.md), [`page`](/docs/app/api-reference/file-conventions/page.md), [`route`](/docs/app/api-reference/file-conventions/route.md), and [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata.md#generatemetadata-function) functions.

| Route                     | Example URL | `params`        |
| ------------------------- | ----------- | --------------- |
| `app/blog/[slug]/page.js` | `/blog/a`   | `{ slug: 'a' }` |
| `app/blog/[slug]/page.js` | `/blog/b`   | `{ slug: 'b' }` |
| `app/blog/[slug]/page.js` | `/blog/c`   | `{ slug: 'c' }` |

### In Client Components

In a Client Component **page**, dynamic segments from props can be accessed using the [`use`](https://react.dev/reference/react/use) hook.

```tsx filename="app/blog/[slug]/page.tsx" switcher
'use client'
import { use } from 'react'

export default function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)

  return (
    <div>
      <p>{slug}</p>
    </div>
  )
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
'use client'
import { use } from 'react'
import { useParams } from 'next/navigation'

export default function BlogPostPage({ params }) {
  const { slug } = use(params)

  return (
    <div>
      <p>{slug}</p>
    </div>
  )
}
```

Alternatively Client Components can use the [`useParams`](/docs/app/api-reference/functions/use-params.md) hook to access the `params` anywhere in the Client Component tree.

### Catch-all Segments

Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...folderName]`.

For example, `app/shop/[...slug]/page.js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.

| Route                        | Example URL   | `params`                    |
| ---------------------------- | ------------- | --------------------------- |
| `app/shop/[...slug]/page.js` | `/shop/a`     | `{ slug: ['a'] }`           |
| `app/shop/[...slug]/page.js` | `/shop/a/b`   | `{ slug: ['a', 'b'] }`      |
| `app/shop/[...slug]/page.js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |

### Optional Catch-all Segments

Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...folderName]]`.

For example, `app/shop/[[...slug]]/page.js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.

The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).

| Route                          | Example URL   | `params`                    |
| ------------------------------ | ------------- | --------------------------- |
| `app/shop/[[...slug]]/page.js` | `/shop`       | `{ slug: undefined }`       |
| `app/shop/[[...slug]]/page.js` | `/shop/a`     | `{ slug: ['a'] }`           |
| `app/shop/[[...slug]]/page.js` | `/shop/a/b`   | `{ slug: ['a', 'b'] }`      |
| `app/shop/[[...slug]]/page.js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |

### TypeScript

When using TypeScript, you can add types for `params` depending on your configured route segment — use [`PageProps<'/route'>`](/docs/app/api-reference/file-conventions/page.md#page-props-helper), [`LayoutProps<'/route'>`](/docs/app/api-reference/file-conventions/layout.md#layout-props-helper), or [`RouteContext<'/route'>`](/docs/app/api-reference/file-conventions/route.md#route-context-helper) to type `params` in `page`, `layout`, and `route` respectively.

Route `params` values are typed as `string`, `string[]`, or `undefined` (for optional catch-all segments), because their values aren't known until runtime. Users can enter any URL into the address bar, and these broad types help ensure that your application code handles all these possible cases.

| Route                               | `params` Type Definition                 |
| ----------------------------------- | ---------------------------------------- |
| `app/blog/[slug]/page.js`           | `{ slug: string }`                       |
| `app/shop/[...slug]/page.js`        | `{ slug: string[] }`                     |
| `app/shop/[[...slug]]/page.js`      | `{ slug?: string[] }`                    |
| `app/[categoryId]/[itemId]/page.js` | `{ categoryId: string, itemId: string }` |

If you're working on a route where `params` can only have a fixed number of valid values, such as a `[locale]` param with a known set of language codes, you can use runtime validation to handle any invalid params a user may enter, and let the rest of your application work with the narrower type from your known set.

```tsx filename="/app/[locale]/page.tsx"
import { notFound } from 'next/navigation'
import type { Locale } from '@i18n/types'
import { isValidLocale } from '@i18n/utils'

function assertValidLocale(value: string): asserts value is Locale {
  if (!isValidLocale(value)) notFound()
}

export default async function Page(props: PageProps<'/[locale]'>) {
  const { locale } = await props.params // locale is typed as string
  assertValidLocale(locale)
  // locale is now typed as Locale
}
```

## Behavior

* Since the `params` prop is a promise. You must use `async`/`await` or React's use function to access the values.
  * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

## Examples

### With `generateStaticParams`

The [`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) function can be used to [statically generate](/docs/app/guides/caching.md#static-rendering) routes at build time instead of on-demand at request time.

```tsx filename="app/blog/[slug]/page.tsx" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}
```

When using `fetch` inside the `generateStaticParams` function, the requests are [automatically deduplicated](/docs/app/guides/caching.md#request-memoization). This avoids multiple network calls for the same data Layouts, Pages, and other `generateStaticParams` functions, speeding up build time.
## Next Steps

For more information on what to do next, we recommend the following sections

- [generateStaticParams](/docs/app/api-reference/functions/generate-static-params.md)
  - API reference for the generateStaticParams function.


--------------------------------------------------------------------------------
title: "error.js"
description: "API reference for the error.js special file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/error"
--------------------------------------------------------------------------------

# error.js

An **error** file allows you to handle unexpected runtime errors and display fallback UI.

![error.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/error-special-file.png)

```tsx filename="app/dashboard/error.tsx" switcher
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

```jsx filename="app/dashboard/error.js" switcher
'use client' // Error boundaries must be Client Components

import { useEffect } from 'react'

export default function Error({ error, reset }) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])

  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

`error.js` wraps a route segment and its nested children in a [React Error Boundary](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary). When an error throws within the boundary, the `error` component shows as the fallback UI.

![How error.js works](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/error-overview.png)

> **Good to know**:
>
> * The [React DevTools](https://react.dev/learn/react-developer-tools) allow you to toggle error boundaries to test error states.
> * If you want errors to bubble up to the parent error boundary, you can `throw` when rendering the `error` component.

## Reference

### Props

#### `error`

An instance of an [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) object forwarded to the `error.js` Client Component.

> **Good to know:** During development, the `Error` object forwarded to the client will be serialized and include the `message` of the original error for easier debugging. However, **this behavior is different in production** to avoid leaking potentially sensitive details included in the error to the client.

#### `error.message`

* Errors forwarded from Client Components show the original `Error` message.
* Errors forwarded from Server Components show a generic message with an identifier. This is to prevent leaking sensitive details. You can use the identifier, under `errors.digest`, to match the corresponding server-side logs.

#### `error.digest`

An automatically generated hash of the error thrown. It can be used to match the corresponding error in server-side logs.

#### `reset`

The cause of an error can sometimes be temporary. In these cases, trying again might resolve the issue.

An error component can use the `reset()` function to prompt the user to attempt to recover from the error. When executed, the function will try to re-render the error boundary's contents. If successful, the fallback error component is replaced with the result of the re-render.

```tsx filename="app/dashboard/error.tsx" switcher
'use client' // Error boundaries must be Client Components

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```

```jsx filename="app/dashboard/error.js" switcher
'use client' // Error boundaries must be Client Components

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={() => reset()}>Try again</button>
    </div>
  )
}
```

## Examples

### Global Error

While less common, you can handle errors in the root layout or template using `global-error.jsx`, located in the root app directory, even when leveraging [internationalization](/docs/app/guides/internationalization.md). Global error UI must define its own `<html>` and `<body>` tags, global styles, fonts, or other dependencies that your error page requires. This file replaces the root layout or template when active.

> **Good to know**: Error boundaries must be [Client Components](/docs/app/getting-started/server-and-client-components.md#using-client-components), which means that [`metadata` and `generateMetadata`](/docs/app/getting-started/metadata-and-og-images.md) exports are not supported in `global-error.jsx`. As an alternative, you can use the React [`<title>`](https://react.dev/reference/react-dom/components/title) component.

```tsx filename="app/global-error.tsx" switcher
'use client' // Error boundaries must be Client Components

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```

```jsx filename="app/global-error.js" switcher
'use client' // Error boundaries must be Client Components

export default function GlobalError({ error, reset }) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```

### Graceful error recovery with a custom error boundary

When rendering fails on the client, it can be useful to show the last known server rendered UI for a better user experience.

The `GracefullyDegradingErrorBoundary` is an example of a custom error boundary that captures and preserves the current HTML before an error occurs. If a rendering error happens, it re-renders the captured HTML and displays a persistent notification bar to inform the user.

```tsx filename="app/dashboard/error.tsx" switcher
'use client'

import React, { Component, ErrorInfo, ReactNode } from 'react'

interface ErrorBoundaryProps {
  children: ReactNode
  onError?: (error: Error, errorInfo: ErrorInfo) => void
}

interface ErrorBoundaryState {
  hasError: boolean
}

export class GracefullyDegradingErrorBoundary extends Component<
  ErrorBoundaryProps,
  ErrorBoundaryState
> {
  private contentRef: React.RefObject<HTMLDivElement | null>

  constructor(props: ErrorBoundaryProps) {
    super(props)
    this.state = { hasError: false }
    this.contentRef = React.createRef()
  }

  static getDerivedStateFromError(_: Error): ErrorBoundaryState {
    return { hasError: true }
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    if (this.props.onError) {
      this.props.onError(error, errorInfo)
    }
  }

  render() {
    if (this.state.hasError) {
      // Render the current HTML content without hydration
      return (
        <>
          <div
            ref={this.contentRef}
            suppressHydrationWarning
            dangerouslySetInnerHTML={{
              __html: this.contentRef.current?.innerHTML || '',
            }}
          />
          <div className="fixed bottom-0 left-0 right-0 bg-red-600 text-white py-4 px-6 text-center">
            <p className="font-semibold">
              An error occurred during page rendering
            </p>
          </div>
        </>
      )
    }

    return <div ref={this.contentRef}>{this.props.children}</div>
  }
}

export default GracefullyDegradingErrorBoundary
```

```jsx filename="app/dashboard/error.js" switcher
'use client'

import React, { Component, createRef } from 'react'

class GracefullyDegradingErrorBoundary extends Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
    this.contentRef = createRef()
  }

  static getDerivedStateFromError(_) {
    return { hasError: true }
  }

  componentDidCatch(error, errorInfo) {
    if (this.props.onError) {
      this.props.onError(error, errorInfo)
    }
  }

  render() {
    if (this.state.hasError) {
      // Render the current HTML content without hydration
      return (
        <>
          <div
            ref={this.contentRef}
            suppressHydrationWarning
            dangerouslySetInnerHTML={{
              __html: this.contentRef.current?.innerHTML || '',
            }}
          />
          <div className="fixed bottom-0 left-0 right-0 bg-red-600 text-white py-4 px-6 text-center">
            <p className="font-semibold">
              An error occurred during page rendering
            </p>
          </div>
        </>
      )
    }

    return <div ref={this.contentRef}>{this.props.children}</div>
  }
}

export default GracefullyDegradingErrorBoundary
```

## Version History

| Version   | Changes                                     |
| --------- | ------------------------------------------- |
| `v15.2.0` | Also display `global-error` in development. |
| `v13.1.0` | `global-error` introduced.                  |
| `v13.0.0` | `error` introduced.                         |
## Learn more about error handling- [Error Handling](/docs/app/getting-started/error-handling.md)
  - Learn how to display expected errors and handle uncaught exceptions.


--------------------------------------------------------------------------------
title: "forbidden.js"
description: "API reference for the forbidden.js special file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/forbidden"
--------------------------------------------------------------------------------

# forbidden.js

> This feature is currently experimental and subject to change, it is not recommended for production.

The **forbidden** file is used to render UI when the [`forbidden`](/docs/app/api-reference/functions/forbidden.md) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.

```tsx filename="app/forbidden.tsx" switcher
import Link from 'next/link'

export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

```jsx filename="app/forbidden.jsx" switcher
import Link from 'next/link'

export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

## Reference

### Props

`forbidden.js` components do not accept any props.

## Version History

| Version   | Changes                    |
| --------- | -------------------------- |
| `v15.1.0` | `forbidden.js` introduced. |
- [forbidden](/docs/app/api-reference/functions/forbidden.md)
  - API Reference for the forbidden function.


--------------------------------------------------------------------------------
title: "instrumentation.js"
description: "API reference for the instrumentation.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation"
--------------------------------------------------------------------------------

# instrumentation.js

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
title: "instrumentation-client.js"
description: "Learn how to add client-side instrumentation to track and monitor your Next.js application's frontend performance."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client"
--------------------------------------------------------------------------------

# instrumentation-client.js

The `instrumentation-client.js|ts` file allows you to add monitoring, analytics code, and other side-effects that run before your application becomes interactive. This is useful for setting up performance tracking, error monitoring, polyfills, or any other client-side observability tools.

To use it, place the file in the **root** of your application or inside a `src` folder.

## Usage

Unlike [server-side instrumentation](/docs/app/guides/instrumentation.md), you do not need to export any specific functions. You can write your monitoring code directly in the file:

```ts filename="instrumentation-client.ts" switcher
// Set up performance monitoring
performance.mark('app-init')

// Initialize analytics
console.log('Analytics initialized')

// Set up error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

```js filename="instrumentation-client.js" switcher
// Set up performance monitoring
performance.mark('app-init')

// Initialize analytics
console.log('Analytics initialized')

// Set up error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

**Error handling:** Implement try-catch blocks around your instrumentation code to ensure robust monitoring. This prevents individual tracking failures from affecting other instrumentation features.

## Router navigation tracking

You can export an `onRouterTransitionStart` function to receive notifications when navigation begins:

```ts filename="instrumentation-client.ts" switcher
performance.mark('app-init')

export function onRouterTransitionStart(
  url: string,
  navigationType: 'push' | 'replace' | 'traverse'
) {
  console.log(`Navigation started: ${navigationType} to ${url}`)
  performance.mark(`nav-start-${Date.now()}`)
}
```

```js filename="instrumentation-client.js" switcher
performance.mark('app-init')

export function onRouterTransitionStart(url, navigationType) {
  console.log(`Navigation started: ${navigationType} to ${url}`)
  performance.mark(`nav-start-${Date.now()}`)
}
```

The `onRouterTransitionStart` function receives two parameters:

* `url: string` - The URL being navigated to
* `navigationType: 'push' | 'replace' | 'traverse'` - The type of navigation

## Performance considerations

Keep instrumentation code lightweight.

Next.js monitors initialization time in development and will log warnings if it takes longer than 16ms, which could impact smooth page loading.

## Execution timing

The `instrumentation-client.js` file executes at a specific point in the application lifecycle:

1. **After** the HTML document is loaded
2. **Before** React hydration begins
3. **Before** user interactions are possible

This timing makes it ideal for setting up error tracking, analytics, and performance monitoring that needs to capture early application lifecycle events.

## Examples

### Error tracking

Initialize error tracking before React starts and add navigation breadcrumbs for better debugging context.

```ts filename="instrumentation-client.ts" switcher
import Monitor from './lib/monitoring'

Monitor.initialize()

export function onRouterTransitionStart(url: string) {
  Monitor.pushEvent({
    message: `Navigation to ${url}`,
    category: 'navigation',
  })
}
```

```js filename="instrumentation-client.js" switcher
import Monitor from './lib/monitoring'

Monitor.initialize()

export function onRouterTransitionStart(url) {
  Monitor.pushEvent({
    message: `Navigation to ${url}`,
    category: 'navigation',
  })
}
```

### Analytics tracking

Initialize analytics and track navigation events with detailed metadata for user behavior analysis.

```ts filename="instrumentation-client.ts" switcher
import { analytics } from './lib/analytics'

analytics.init()

export function onRouterTransitionStart(url: string, navigationType: string) {
  analytics.track('page_navigation', {
    url,
    type: navigationType,
    timestamp: Date.now(),
  })
}
```

```js filename="instrumentation-client.js" switcher
import { analytics } from './lib/analytics'

analytics.init()

export function onRouterTransitionStart(url, navigationType) {
  analytics.track('page_navigation', {
    url,
    type: navigationType,
    timestamp: Date.now(),
  })
}
```

### Performance monitoring

Track Time to Interactive and navigation performance using the Performance Observer API and performance marks.

```ts filename="instrumentation-client.ts" switcher
const startTime = performance.now()

const observer = new PerformanceObserver(
  (list: PerformanceObserverEntryList) => {
    for (const entry of list.getEntries()) {
      if (entry instanceof PerformanceNavigationTiming) {
        console.log('Time to Interactive:', entry.loadEventEnd - startTime)
      }
    }
  }
)

observer.observe({ entryTypes: ['navigation'] })

export function onRouterTransitionStart(url: string) {
  performance.mark(`nav-start-${url}`)
}
```

```js filename="instrumentation-client.js" switcher
const startTime = performance.now()

const observer = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    if (entry instanceof PerformanceNavigationTiming) {
      console.log('Time to Interactive:', entry.loadEventEnd - startTime)
    }
  }
})

observer.observe({ entryTypes: ['navigation'] })

export function onRouterTransitionStart(url) {
  performance.mark(`nav-start-${url}`)
}
```

### Polyfills

Load polyfills before application code runs. Use static imports for immediate loading and dynamic imports for conditional loading based on feature detection.

```ts filename="instrumentation-client.ts" switcher
import './lib/polyfills'

if (!window.ResizeObserver) {
  import('./lib/polyfills/resize-observer').then((mod) => {
    window.ResizeObserver = mod.default
  })
}
```

```js filename="instrumentation-client.js" switcher
import './lib/polyfills'

if (!window.ResizeObserver) {
  import('./lib/polyfills/resize-observer').then((mod) => {
    window.ResizeObserver = mod.default
  })
}
```

## Version history

| Version | Changes                             |
| ------- | ----------------------------------- |
| `v15.3` | `instrumentation-client` introduced |


--------------------------------------------------------------------------------
title: "Intercepting Routes"
description: "Use intercepting routes to load a new route within the current layout while masking the browser URL, useful for advanced routing patterns such as modals."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes"
--------------------------------------------------------------------------------

# Intercepting Routes

Intercepting routes allows you to load a route from another part of your application within the current layout. This routing paradigm can be useful when you want to display the content of a route without the user switching to a different context.

For example, when clicking on a photo in a feed, you can display the photo in a modal, overlaying the feed. In this case, Next.js intercepts the `/photo/123` route, masks the URL, and overlays it over `/feed`.

![Intercepting routes soft navigation](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/intercepting-routes-soft-navigate.png)

However, when navigating to the photo by clicking a shareable URL or by refreshing the page, the entire photo page should render instead of the modal. No route interception should occur.

![Intercepting routes hard navigation](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/intercepting-routes-hard-navigate.png)

## Convention

Intercepting routes can be defined with the `(..)` convention, which is similar to relative path convention `../` but for route segments.

You can use:

* `(.)` to match segments on the **same level**
* `(..)` to match segments **one level above**
* `(..)(..)` to match segments **two levels above**
* `(...)` to match segments from the **root** `app` directory

For example, you can intercept the `photo` segment from within the `feed` segment by creating a `(..)photo` directory.

![Intercepting routes folder structure](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/intercepted-routes-files.png)

> **Good to know:** The `(..)` convention is based on *route segments*, not the file-system. For example, it does not consider `@slot` folders in [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md).

## Examples

### Modals

Intercepting Routes can be used together with [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md) to create modals. This allows you to solve common challenges when building modals, such as:

* Making the modal content **shareable through a URL**.
* **Preserving context** when the page is refreshed, instead of closing the modal.
* **Closing the modal on backwards navigation** rather than going to the previous route.
* **Reopening the modal on forwards navigation**.

Consider the following UI pattern, where a user can open a photo modal from a gallery using client-side navigation, or navigate to the photo page directly from a shareable URL:

![Intercepting routes modal example](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/intercepted-routes-modal-example.png)

In the above example, the path to the `photo` segment can use the `(..)` matcher since `@modal` is a slot and **not** a segment. This means that the `photo` route is only one segment level higher, despite being two file-system levels higher.

See the [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md#modals) documentation for a step-by-step example, or see our [image gallery example](https://github.com/vercel-labs/nextgram).

> **Good to know:**
>
> * Other examples could include opening a login modal in a top navbar while also having a dedicated `/login` page, or opening a shopping cart in a side modal.
## Next Steps

Learn how to create modals with Intercepted and Parallel Routes.

- [Parallel Routes](/docs/app/api-reference/file-conventions/parallel-routes.md)
  - Simultaneously render one or more pages in the same view that can be navigated independently. A pattern for highly dynamic applications.


--------------------------------------------------------------------------------
title: "layout.js"
description: "API reference for the layout.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/layout"
--------------------------------------------------------------------------------

# layout.js

The `layout` file is used to define a layout in your Next.js application.

```tsx filename="app/dashboard/layout.tsx" switcher
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return <section>{children}</section>
}
```

```jsx filename="app/dashboard/layout.js" switcher
export default function DashboardLayout({ children }) {
  return <section>{children}</section>
}
```

A **root layout** is the top-most layout in the root `app` directory. It is used to define the `<html>` and `<body>` tags and other globally shared UI.

```tsx filename="app/layout.tsx" switcher
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
export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
```

## Reference

### Props

#### `children` (required)

Layout components should accept and use a `children` prop. During rendering, `children` will be populated with the route segments the layout is wrapping. These will primarily be the component of a child [Layout](/docs/app/api-reference/file-conventions/page.md) (if it exists) or [Page](/docs/app/api-reference/file-conventions/page.md), but could also be other special files like [Loading](/docs/app/api-reference/file-conventions/loading.md) or [Error](/docs/app/getting-started/error-handling.md) when applicable.

#### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) object from the root segment down to that layout.

```tsx filename="app/dashboard/[team]/layout.tsx" switcher
export default async function Layout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params
}
```

```jsx filename="app/dashboard/[team]/layout.js" switcher
export default async function Layout({ children, params }) {
  const { team } = await params
}
```

| Example Route                     | URL            | `params`                           |
| --------------------------------- | -------------- | ---------------------------------- |
| `app/dashboard/[team]/layout.js`  | `/dashboard/1` | `Promise<{ team: '1' }>`           |
| `app/shop/[tag]/[item]/layout.js` | `/shop/1/2`    | `Promise<{ tag: '1', item: '2' }>` |
| `app/blog/[...slug]/layout.js`    | `/blog/1/2`    | `Promise<{ slug: ['1', '2'] }>`    |

* Since the `params` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
  * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

### Layout Props Helper

You can type layouts with `LayoutProps` to get a strongly typed `params` and named slots inferred from your directory structure. `LayoutProps` is a globally available helper.

```tsx filename="app/dashboard/layout.tsx"
export default function Layout(props: LayoutProps<'/dashboard'>) {
  return (
    <section>
      {props.children}
      {/* If you have app/dashboard/@analytics, it appears as a typed slot: */}
      {/* {props.analytics} */}
    </section>
  )
}
```

> **Good to know**:
>
> * Types are generated during `next dev`, `next build` or `next typegen`.
> * After type generation, the `LayoutProps` helper is globally available. It doesn't need to be imported.

### Root Layout

The `app` directory **must** include a **root layout**, which is the top-most layout in the root `app` directory. Typically, the root layout is `app/layout.js`.

```tsx filename="app/layout.tsx" switcher
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  )
}
```

* The root layout **must** define `<html>` and `<body>` tags.
  * You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, you should use the [Metadata API](/docs/app/getting-started/metadata-and-og-images.md) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
* You can use [route groups](/docs/app/api-reference/file-conventions/route-groups.md) to create **multiple root layouts**.
  * Navigating **across multiple root layouts** will cause a **full page load** (as opposed to a client-side navigation). For example, navigating from `/cart` that uses `app/(shop)/layout.js` to `/blog` that uses `app/(marketing)/layout.js` will cause a full page load. This **only** applies to multiple root layouts.
* The root layout can be under a **dynamic segment**, for example when implementing [internationalization](/docs/app/guides/internationalization.md) with `app/[lang]/layout.js`.

## Caveats

### Request Object

Layouts are cached in the client during navigation to avoid unnecessary server requests.

[Layouts](/docs/app/api-reference/file-conventions/layout.md) do not rerender. They can be cached and reused to avoid unnecessary computation when navigating between pages. By restricting layouts from accessing the raw request, Next.js can prevent the execution of potentially slow or expensive user code within the layout, which could negatively impact performance.

To access the request object, you can use [`headers`](/docs/app/api-reference/functions/headers.md) and [`cookies`](/docs/app/api-reference/functions/cookies.md) APIs in [Server Components](/docs/app/getting-started/server-and-client-components.md) and Functions.

```tsx filename="app/shop/layout.tsx" switcher
import { cookies } from 'next/headers'

export default async function Layout({ children }) {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

```jsx filename="app/shop/layout.js" switcher
import { cookies } from 'next/headers'

export default async function Layout({ children }) {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

### Query params

Layouts do not rerender on navigation, so they cannot access search params which would otherwise become stale.

To access updated query parameters, you can use the Page [`searchParams`](/docs/app/api-reference/file-conventions/page.md#searchparams-optional) prop, or read them inside a Client Component using the [`useSearchParams`](/docs/app/api-reference/functions/use-search-params.md) hook. Since Client Components re-render on navigation, they have access to the latest query parameters.

```tsx filename="app/ui/search.tsx" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function Search() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  return '...'
}
```

```jsx filename="app/ui/search.js" switcher
'use client'

import { useSearchParams } from 'next/navigation'

export default function Search() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  return '...'
}
```

```tsx filename="app/shop/layout.tsx" switcher
import Search from '@/app/ui/search'

export default function Layout({ children }) {
  return (
    <>
      <Search />
      {children}
    </>
  )
}
```

```jsx filename="app/shop/layout.js" switcher
import Search from '@/app/ui/search'

export default function Layout({ children }) {
  return (
    <>
      <Search />
      {children}
    </>
  )
}
```

### Pathname

Layouts do not re-render on navigation, so they do not access pathname which would otherwise become stale.

To access the current pathname, you can read it inside a Client Component using the [`usePathname`](/docs/app/api-reference/functions/use-pathname.md) hook. Since Client Components re-render during navigation, they have access to the latest pathname.

```tsx filename="app/ui/breadcrumbs.tsx" switcher
'use client'

import { usePathname } from 'next/navigation'

// Simplified breadcrumbs logic
export default function Breadcrumbs() {
  const pathname = usePathname()
  const segments = pathname.split('/')

  return (
    <nav>
      {segments.map((segment, index) => (
        <span key={index}>
          {' > '}
          {segment}
        </span>
      ))}
    </nav>
  )
}
```

```jsx filename="app/ui/breadcrumbs.js" switcher
'use client'

import { usePathname } from 'next/navigation'

// Simplified breadcrumbs logic
export default function Breadcrumbs() {
  const pathname = usePathname()
  const segments = pathname.split('/')

  return (
    <nav>
      {segments.map((segment, index) => (
        <span key={index}>
          {' > '}
          {segment}
        </span>
      ))}
    </nav>
  )
}
```

```tsx filename="app/docs/layout.tsx" switcher
import { Breadcrumbs } from '@/app/ui/Breadcrumbs'

export default function Layout({ children }) {
  return (
    <>
      <Breadcrumbs />
      <main>{children}</main>
    </>
  )
}
```

```jsx filename="app/docs/layout.js" switcher
import { Breadcrumbs } from '@/app/ui/Breadcrumbs'

export default function Layout({ children }) {
  return (
    <>
      <Breadcrumbs />
      <main>{children}</main>
    </>
  )
}
```

### Fetching Data

Layouts cannot pass data to their `children`. However, you can fetch the same data in a route more than once, and use React [`cache`](https://react.dev/reference/react/cache) to dedupe the requests without affecting performance.

Alternatively, when using [`fetch`](/docs/app/api-reference/functions/fetch.md)in Next.js, requests are automatically deduped.

```tsx filename="app/lib/data.ts" switcher
export async function getUser(id: string) {
  const res = await fetch(`https://.../users/${id}`)
  return res.json()
}
```

```tsx filename="app/dashboard/layout.tsx" switcher
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Layout({ children }) {
  const user = await getUser('1')

  return (
    <>
      <nav>
        {/* ... */}
        <UserName user={user.name} />
      </nav>
      {children}
    </>
  )
}
```

```jsx filename="app/dashboard/layout.js" switcher
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Layout({ children }) {
  const user = await getUser('1')

  return (
    <>
      <nav>
        {/* ... */}
        <UserName user={user.name} />
      </nav>
      {children}
    </>
  )
}
```

```tsx filename="app/dashboard/page.tsx" switcher
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Page() {
  const user = await getUser('1')

  return (
    <div>
      <h1>Welcome {user.name}</h1>
    </div>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Page() {
  const user = await getUser('1')

  return (
    <div>
      <h1>Welcome {user.name}</h1>
    </div>
  )
}
```

### Accessing child segments

Layouts do not have access to the route segments below itself. To access all route segments, you can use [`useSelectedLayoutSegment`](/docs/app/api-reference/functions/use-selected-layout-segment.md) or [`useSelectedLayoutSegments`](/docs/app/api-reference/functions/use-selected-layout-segments.md) in a Client Component.

```tsx filename="app/ui/nav-link.tsx" switcher
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

export default function NavLink({
  slug,
  children,
}: {
  slug: string
  children: React.ReactNode
}) {
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

```jsx filename="app/ui/nav-link.js" switcher
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

export default function NavLinks({ slug, children }) {
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment

  return (
    <Link
      href={`/blog/${slug}`}
      style={{ fontWeight: isActive ? 'bold' : 'normal' }}
    >
      {children}
    </Link>
  )
}
```

```tsx filename="app/blog/layout.tsx" switcher
import { NavLink } from './nav-link'
import getPosts from './get-posts'

export default async function Layout({
  children,
}: {
  children: React.ReactNode
}) {
  const featuredPosts = await getPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <NavLink slug={post.slug}>{post.title}</NavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```

```jsx filename="app/blog/layout.js" switcher
import { NavLink } from './nav-link'
import getPosts from './get-posts'

export default async function Layout({ children }) {
  const featuredPosts = await getPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <NavLink slug={post.slug}>{post.title}</NavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```

## Examples

### Metadata

You can modify the `<head>` HTML elements such as `title` and `meta` using the [`metadata` object](/docs/app/api-reference/functions/generate-metadata.md#the-metadata-object) or [`generateMetadata` function](/docs/app/api-reference/functions/generate-metadata.md#generatemetadata-function).

```tsx filename="app/layout.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Next.js',
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return '...'
}
```

```jsx filename="app/layout.js" switcher
export const metadata = {
  title: 'Next.js',
}

export default function Layout({ children }) {
  return '...'
}
```

> **Good to know**: You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, use the [Metadata APIs](/docs/app/api-reference/functions/generate-metadata.md) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.

### Active Nav Links

You can use the [`usePathname`](/docs/app/api-reference/functions/use-pathname.md) hook to determine if a nav link is active.

Since `usePathname` is a client hook, you need to extract the nav links into a Client Component, which can be imported into your layout:

```tsx filename="app/ui/nav-links.tsx" switcher
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function NavLinks() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>

      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

```jsx filename="app/ui/nav-links.js" switcher
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function Links() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>

      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

```tsx filename="app/layout.tsx" switcher
import { NavLinks } from '@/app/ui/nav-links'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <NavLinks />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { NavLinks } from '@/app/ui/nav-links'

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>
        <NavLinks />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

### Displaying content based on `params`

Using [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes.md), you can display or fetch specific content based on the `params` prop.

```tsx filename="app/dashboard/layout.tsx" switcher
export default async function DashboardLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params

  return (
    <section>
      <header>
        <h1>Welcome to {team}'s Dashboard</h1>
      </header>
      <main>{children}</main>
    </section>
  )
}
```

```jsx filename="app/dashboard/layout.js" switcher
export default async function DashboardLayout({ children, params }) {
  const { team } = await params

  return (
    <section>
      <header>
        <h1>Welcome to {team}'s Dashboard</h1>
      </header>
      <main>{children}</main>
    </section>
  )
}
```

### Reading `params` in Client Components

To use `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

```tsx filename="app/page.tsx" switcher
'use client'

import { use } from 'react'

export default function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)
}
```

```js filename="app/page.js" switcher
'use client'

import { use } from 'react'

export default function Page({ params }) {
  const { slug } = use(params)
}
```

## Version History

| Version      | Changes                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------- |
| `v15.0.0-RC` | `params` is now a promise. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available. |
| `v13.0.0`    | `layout` introduced.                                                                          |


--------------------------------------------------------------------------------
title: "loading.js"
description: "API reference for the loading.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/loading"
--------------------------------------------------------------------------------

# loading.js

The special file `loading.js` helps you create meaningful Loading UI with [React Suspense](https://react.dev/reference/react/Suspense). With this convention, you can show an [instant loading state](#instant-loading-states) from the server while the content of a route segment streams in. The new content is automatically swapped in once complete.

![Loading UI](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-ui.png)

```tsx filename="app/feed/loading.tsx" switcher
export default function Loading() {
  // Or a custom loading skeleton component
  return <p>Loading...</p>
}
```

```jsx filename="app/feed/loading.js" switcher
export default function Loading() {
  // Or a custom loading skeleton component
  return <p>Loading...</p>
}
```

Inside the `loading.js` file, you can add any light-weight loading UI. You may find it helpful to use the [React Developer Tools](https://react.dev/learn/react-developer-tools) to manually toggle Suspense boundaries.

By default, this file is a [Server Component](/docs/app/getting-started/server-and-client-components.md) - but can also be used as a Client Component through the `"use client"` directive.

## Reference

### Parameters

Loading UI components do not accept any parameters.

## Behavior

### Navigation

* The Fallback UI is [prefetched](/docs/app/getting-started/linking-and-navigating.md#prefetching), making navigation immediate unless prefetching hasn't completed.
* Navigation is interruptible, meaning changing routes does not need to wait for the content of the route to fully load before navigating to another route.
* Shared layouts remain interactive while new route segments load.

### Instant Loading States

An instant loading state is fallback UI that is shown immediately upon navigation. You can pre-render loading indicators such as skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc. This helps users understand the app is responding and provides a better user experience.

Create a loading state by adding a `loading.js` file inside a folder.

![loading.js special file](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-special-file.png)

```tsx filename="app/dashboard/loading.tsx" switcher
export default function Loading() {
  // You can add any UI inside Loading, including a Skeleton.
  return <LoadingSkeleton />
}
```

```jsx filename="app/dashboard/loading.js" switcher
export default function Loading() {
  // You can add any UI inside Loading, including a Skeleton.
  return <LoadingSkeleton />
}
```

In the same folder, `loading.js` will be nested inside `layout.js`. It will automatically wrap the `page.js` file and any children below in a `<Suspense>` boundary.

![loading.js overview](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/loading-overview.png)

### SEO

* For bots that only scrape static HTML, and cannot execute JavaScript like a full browser, such as Twitterbot, Next.js resolves [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata.md) before streaming UI, and metadata is placed in the `<head>` of the initial HTML.
* Otherwise, [streaming metadata](/docs/app/api-reference/functions/generate-metadata.md#streaming-metadata) may be used. Next.js automatically detects user agents to choose between blocking and streaming behavior.
* Since streaming is server-rendered, it does not impact SEO. You can use the [Rich Results Test](https://search.google.com/test/rich-results) tool from Google to see how your page appears to Google's web crawlers and view the serialized HTML ([source](https://web.dev/rendering-on-the-web/#seo-considerations)).

### Status Codes

When streaming, a `200` status code will be returned to signal that the request was successful.

The server can still communicate errors or issues to the client within the streamed content itself, for example, when using [`redirect`](/docs/app/api-reference/functions/redirect.md) or [`notFound`](/docs/app/api-reference/functions/not-found.md). Because the response headers have already been sent to the client, the status code of the response cannot be updated.

For example, when a 404 page is streamed to the client, Next.js includes a `<meta name="robots" content="noindex">` tag in the streamed HTML. This prevents search engines from indexing that URL even if the HTTP status is 200. See Google’s guidance on the [`robots` meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag).

Some crawlers may label these responses as “soft 404s”. In the streaming case, this does not lead to indexation because the page is explicitly marked `noindex` in the HTML.

If you need a 404 status, for compliance or analytics, ensure the resource exists before the response body is streamed, so that the server can set the HTTP status code.

You can run this check in [`proxy`](/docs/app/api-reference/file-conventions/proxy.md) to rewrite missing slugs to a not-found route, or [produce a 404 response](/docs/app/api-reference/file-conventions/proxy.md#producing-a-response). Keep proxy checks fast, and avoid fetching full content there.

<details>
<summary>When is the response body streamed?</summary>

The response body starts streaming when a Suspense fallback renders (for example, a `loading.tsx`) or when a Server Component suspends under a `Suspense` boundary. Place `notFound()` before those boundaries and before any `await` that may suspend.

To start streaming, the response headers must be set. This is why it is not possible to change the status code after streaming started.

</details>

### Browser limits

[Some browsers](https://bugs.webkit.org/show_bug.cgi?id=252413) buffer a streaming response. You may not see the streamed response until the response exceeds 1024 bytes. This typically only affects “hello world” applications, but not real applications.

## Platform Support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure streaming](/docs/app/guides/self-hosting.md#streaming-and-suspense) when self-hosting Next.js.

## Examples

### Streaming with Suspense

In addition to `loading.js`, you can also manually create Suspense Boundaries for your own UI components. The App Router supports streaming with [Suspense](https://react.dev/reference/react/Suspense).

`<Suspense>` works by wrapping a component that performs an asynchronous action (e.g. fetch data), showing fallback UI (e.g. skeleton, spinner) while it's happening, and then swapping in your component once the action completes.

```tsx filename="app/dashboard/page.tsx" switcher
import { Suspense } from 'react'
import { PostFeed, Weather } from './Components'

export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  )
}
```

```jsx filename="app/dashboard/page.js" switcher
import { Suspense } from 'react'
import { PostFeed, Weather } from './Components'

export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  )
}
```

By using Suspense, you get the benefits of:

1. **Streaming Server Rendering** - Progressively rendering HTML from the server to the client.
2. **Selective Hydration** - React prioritizes what components to make interactive first based on user interaction.

For more Suspense examples and use cases, please see the [React Documentation](https://react.dev/reference/react/Suspense).

## Version History

| Version   | Changes               |
| --------- | --------------------- |
| `v13.0.0` | `loading` introduced. |


--------------------------------------------------------------------------------
title: "mdx-components.js"
description: "API reference for the mdx-components.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components"
--------------------------------------------------------------------------------

# mdx-components.js

The `mdx-components.js|tsx` file is **required** to use [`@next/mdx` with App Router](/docs/app/guides/mdx.md) and will not work without it. Additionally, you can use it to [customize styles](/docs/app/guides/mdx.md#using-custom-styles-and-components).

Use the file `mdx-components.tsx` (or `.js`) in the root of your project to define MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

```tsx filename="mdx-components.tsx" switcher
import type { MDXComponents } from 'mdx/types'

const components: MDXComponents = {}

export function useMDXComponents(): MDXComponents {
  return components
}
```

```js filename="mdx-components.js" switcher
const components = {}

export function useMDXComponents() {
  return components
}
```

## Exports

### `useMDXComponents` function

The file must export a single function named `useMDXComponents`. This function does not accept any arguments.

```tsx filename="mdx-components.tsx" switcher
import type { MDXComponents } from 'mdx/types'

const components: MDXComponents = {}

export function useMDXComponents(): MDXComponents {
  return components
}
```

```js filename="mdx-components.js" switcher
const components = {}

export function useMDXComponents() {
  return components
}
```

## Version History

| Version   | Changes              |
| --------- | -------------------- |
| `v13.1.2` | MDX Components added |
## Learn more about MDX Components- [MDX](/docs/app/guides/mdx.md)
  - Learn how to configure MDX and use it in your Next.js apps.


--------------------------------------------------------------------------------
title: "not-found.js"
description: "API reference for the not-found.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/not-found"
--------------------------------------------------------------------------------

# not-found.js

Next.js provides two conventions to handle not found cases:

* **`not-found.js`**: Used when you call the [`notFound`](/docs/app/api-reference/functions/not-found.md) function in a route segment.
* **`global-not-found.js`**: Used to define a global 404 page for unmatched routes across your entire app. This is handled at the routing level and doesn't depend on rendering a layout or page.

## `not-found.js`

The **not-found** file is used to render UI when the [`notFound`](/docs/app/api-reference/functions/not-found.md) function is thrown within a route segment. Along with serving a custom UI, Next.js will return a `200` HTTP status code for streamed responses, and `404` for non-streamed responses.

```tsx filename="app/not-found.tsx" switcher
import Link from 'next/link'

export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

```jsx filename="app/blog/not-found.js" switcher
import Link from 'next/link'

export default function NotFound() {
  return (
    <div>
      <h2>Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

## `global-not-found.js` (experimental)

The `global-not-found.js` file lets you define a 404 page for your entire application. Unlike `not-found.js`, which works at the route level, this is used when a requested URL doesn't match any route at all. Next.js **skips rendering** and directly returns this global page.

The `global-not-found.js` file bypasses your app's normal rendering, which means you'll need to import any global styles, fonts, or other dependencies that your 404 page requires.

> **Good to know**: A smaller version of your global styles, and a simpler font family could improve performance of this page.

`global-not-found.js` is useful when you can't build a 404 page using a combination of `layout.js` and `not-found.js`. This can happen in two cases:

* Your app has multiple root layouts (e.g. `app/(admin)/layout.tsx` and `app/(shop)/layout.tsx`), so there's no single layout to compose a global 404 from.
* Your root layout is defined using top-level dynamic segments (e.g. `app/[country]/layout.tsx`), which makes composing a consistent 404 page harder.

To enable it, add the `globalNotFound` flag in `next.config.ts`:

```tsx filename="next.config.ts"
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    globalNotFound: true,
  },
}

export default nextConfig
```

Then, create a file in the root of the `app` directory: `app/global-not-found.js`:

```tsx filename="app/global-not-found.tsx" switcher
// Import global styles and fonts
import './globals.css'
import { Inter } from 'next/font/google'
import type { Metadata } from 'next'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: '404 - Page Not Found',
  description: 'The page you are looking for does not exist.',
}

export default function GlobalNotFound() {
  return (
    <html lang="en" className={inter.className}>
      <body>
        <h1>404 - Page Not Found</h1>
        <p>This page does not exist.</p>
      </body>
    </html>
  )
}
```

```jsx filename="app/global-not-found.js" switcher
// Import global styles and fonts
import './globals.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: '404 - Page Not Found',
  description: 'The page you are looking for does not exist.',
}

export default function GlobalNotFound() {
  return (
    <html lang="en" className={inter.className}>
      <body>
        <h1>404 - Page Not Found</h1>
        <p>This page does not exist.</p>
      </body>
    </html>
  )
}
```

Unlike `not-found.js`, this file must return a full HTML document, including `<html>` and `<body>` tags.

## Reference

### Props

`not-found.js` or `global-not-found.js` components do not accept any props.

> **Good to know**: In addition to catching expected `notFound()` errors, the root `app/not-found.js` and `app/global-not-found.js` files handle any unmatched URLs for your whole application. This means users that visit a URL that is not handled by your app will be shown the exported UI.

## Examples

### Data Fetching

By default, `not-found` is a Server Component. You can mark it as `async` to fetch and display data:

```tsx filename="app/not-found.tsx" switcher
import Link from 'next/link'
import { headers } from 'next/headers'

export default async function NotFound() {
  const headersList = await headers()
  const domain = headersList.get('host')
  const data = await getSiteData(domain)
  return (
    <div>
      <h2>Not Found: {data.name}</h2>
      <p>Could not find requested resource</p>
      <p>
        View <Link href="/blog">all posts</Link>
      </p>
    </div>
  )
}
```

```jsx filename="app/not-found.jsx" switcher
import Link from 'next/link'
import { headers } from 'next/headers'

export default async function NotFound() {
  const headersList = await headers()
  const domain = headersList.get('host')
  const data = await getSiteData(domain)
  return (
    <div>
      <h2>Not Found: {data.name}</h2>
      <p>Could not find requested resource</p>
      <p>
        View <Link href="/blog">all posts</Link>
      </p>
    </div>
  )
}
```

If you need to use Client Component hooks like `usePathname` to display content based on the path, you must fetch data on the client-side instead.

### Metadata

For `global-not-found.js`, you can export a `metadata` object or a [`generateMetadata`](/docs/app/api-reference/functions/generate-metadata.md) function to customize the `<title>`, `<meta>`, and other head tags for your 404 page:

> **Good to know**: Next.js automatically injects `<meta name="robots" content="noindex" />` for pages that return a 404 status code, including `global-not-found.js` pages.

```tsx filename="app/global-not-found.tsx" switcher
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Not Found',
  description: 'The page you are looking for does not exist.',
}

export default function GlobalNotFound() {
  return (
    <html lang="en">
      <body>
        <div>
          <h1>Not Found</h1>
          <p>The page you are looking for does not exist.</p>
        </div>
      </body>
    </html>
  )
}
```

```jsx filename="app/global-not-found.js" switcher
export const metadata = {
  title: 'Not Found',
  description: 'The page you are looking for does not exist.',
}

export default function GlobalNotFound() {
  return (
    <html lang="en">
      <body>
        <div>
          <h1>Not Found</h1>
          <p>The page you are looking for does not exist.</p>
        </div>
      </body>
    </html>
  )
}
```

## Version History

| Version   | Changes                                             |
| --------- | --------------------------------------------------- |
| `v15.4.0` | `global-not-found.js` introduced (experimental).    |
| `v13.3.0` | Root `app/not-found` handles global unmatched URLs. |
| `v13.0.0` | `not-found` introduced.                             |


--------------------------------------------------------------------------------
title: "page.js"
description: "API reference for the page.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/page"
--------------------------------------------------------------------------------

# page.js

The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:

```tsx filename="app/blog/[slug]/page.tsx" switcher
export default function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  return <h1>My Page</h1>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export default function Page({ params, searchParams }) {
  return <h1>My Page</h1>
}
```

## Good to know

* The `.js`, `.jsx`, or `.tsx` file extensions can be used for `page`.
* A `page` is always the **leaf** of the route subtree.
* A `page` file is required to make a route segment **publicly accessible**.
* Pages are [Server Components](https://react.dev/reference/rsc/server-components) by default, but can be set to a [Client Component](https://react.dev/reference/rsc/use-client).

## Reference

### Props

#### `params` (optional)

A promise that resolves to an object containing the [dynamic route parameters](/docs/app/api-reference/file-conventions/dynamic-routes.md) from the root segment down to that page.

```tsx filename="app/shop/[slug]/page.tsx" switcher
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
}
```

```jsx filename="app/shop/[slug]/page.js" switcher
export default async function Page({ params }) {
  const { slug } = await params
}
```

| Example Route                        | URL         | `params`                                |
| ------------------------------------ | ----------- | --------------------------------------- |
| `app/shop/[slug]/page.js`            | `/shop/1`   | `Promise<{ slug: '1' }>`                |
| `app/shop/[category]/[item]/page.js` | `/shop/1/2` | `Promise<{ category: '1', item: '2' }>` |
| `app/shop/[...slug]/page.js`         | `/shop/1/2` | `Promise<{ slug: ['1', '2'] }>`         |

* Since the `params` prop is a promise, you must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
  * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.

#### `searchParams` (optional)

A promise that resolves to an object containing the [search parameters](https://developer.mozilla.org/docs/Learn/Common_questions/What_is_a_URL#parameters) of the current URL. For example:

```tsx filename="app/shop/page.tsx" switcher
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = (await searchParams).filters
}
```

```jsx filename="app/shop/page.js" switcher
export default async function Page({ searchParams }) {
  const filters = (await searchParams).filters
}
```

Client Component **pages** can also access `searchParams` using React’s [`use`](https://react.dev/reference/react/use) hook:

```tsx filename="app/shop/page.tsx" switcher
'use client'
import { use } from 'react'

export default function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const filters = use(searchParams).filters
}
```

```jsx filename="app/page.jsx" switcher
'use client'
import { use } from 'react'

export default function Page({ searchParams }) {
  const filters = use(searchParams).filters
}
```

| Example URL     | `searchParams`                |
| --------------- | ----------------------------- |
| `/shop?a=1`     | `Promise<{ a: '1' }>`         |
| `/shop?a=1&b=2` | `Promise<{ a: '1', b: '2' }>` |
| `/shop?a=1&a=2` | `Promise<{ a: ['1', '2'] }>`  |

* Since the `searchParams` prop is a promise. You must use `async/await` or React's [`use`](https://react.dev/reference/react/use) function to access the values.
  * In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
* `searchParams` is a **[Dynamic API](/docs/app/guides/caching.md#dynamic-rendering)** whose values cannot be known ahead of time. Using it will opt the page into **[dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering)** at request time.
* `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.

### Page Props Helper

You can type pages with `PageProps` to get strongly typed `params` and `searchParams` from the route literal. `PageProps` is a globally available helper.

```tsx filename="app/blog/[slug]/page.tsx"
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  const query = await props.searchParams
  return <h1>Blog Post: {slug}</h1>
}
```

> **Good to know**
>
> * Using a literal route (e.g. `'/blog/[slug]'`) enables autocomplete and strict keys for `params`.
> * Static routes resolve `params` to `{}`.
> * Types are generated during `next dev`, `next build`, or with `next typegen`.
> * After type generation, the `PageProps` helper is globally available. It doesn't need to be imported.

## Examples

### Displaying content based on `params`

Using [dynamic route segments](/docs/app/api-reference/file-conventions/dynamic-routes.md), you can display or fetch specific content for the page based on the `params` prop.

```tsx filename="app/blog/[slug]/page.tsx" switcher
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  return <h1>Blog Post: {slug}</h1>
}
```

```jsx filename="app/blog/[slug]/page.js" switcher
export default async function Page({ params }) {
  const { slug } = await params
  return <h1>Blog Post: {slug}</h1>
}
```

### Handling filtering with `searchParams`

You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.

```tsx filename="app/shop/page.tsx" switcher
export default async function Page({
  searchParams,
}: {
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const { page = '1', sort = 'asc', query = '' } = await searchParams

  return (
    <div>
      <h1>Product Listing</h1>
      <p>Search query: {query}</p>
      <p>Current page: {page}</p>
      <p>Sort order: {sort}</p>
    </div>
  )
}
```

```jsx filename="app/shop/page.js" switcher
export default async function Page({ searchParams }) {
  const { page = '1', sort = 'asc', query = '' } = await searchParams

  return (
    <div>
      <h1>Product Listing</h1>
      <p>Search query: {query}</p>
      <p>Current page: {page}</p>
      <p>Sort order: {sort}</p>
    </div>
  )
}
```

### Reading `searchParams` and `params` in Client Components

To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's [`use`](https://react.dev/reference/react/use) function to read the promise:

```tsx filename="app/page.tsx" switcher
'use client'

import { use } from 'react'

export default function Page({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [key: string]: string | string[] | undefined }>
}) {
  const { slug } = use(params)
  const { query } = use(searchParams)
}
```

```js filename="app/page.js" switcher
'use client'

import { use } from 'react'

export default function Page({ params, searchParams }) {
  const { slug } = use(params)
  const { query } = use(searchParams)
}
```

## Version History

| Version      | Changes                                                                                                          |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| `v15.0.0-RC` | `params` and `searchParams` are now promises. A [codemod](/docs/app/guides/upgrading/codemods.md#150) is available. |
| `v13.0.0`    | `page` introduced.                                                                                               |


--------------------------------------------------------------------------------
title: "Parallel Routes"
description: "Simultaneously render one or more pages in the same view that can be navigated independently. A pattern for highly dynamic applications."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes"
--------------------------------------------------------------------------------

# Parallel Routes

Parallel Routes allows you to simultaneously or conditionally render one or more pages within the same layout. They are useful for highly dynamic sections of an app, such as dashboards and feeds on social sites.

For example, considering a dashboard, you can use parallel routes to simultaneously render the `team` and `analytics` pages:

![Parallel Routes Diagram](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes.png)

## Convention

### Slots

Parallel routes are created using named **slots**. Slots are defined with the `@folder` convention. For example, the following file structure defines two slots: `@analytics` and `@team`:

![Parallel Routes File-system Structure](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-file-system.png)

Slots are passed as props to the shared parent layout. For the example above, the component in `app/layout.js` now accepts the `@analytics` and `@team` slots props, and can render them in parallel alongside the `children` prop:

```tsx filename="app/layout.tsx" switcher
export default function Layout({
  children,
  team,
  analytics,
}: {
  children: React.ReactNode
  analytics: React.ReactNode
  team: React.ReactNode
}) {
  return (
    <>
      {children}
      {team}
      {analytics}
    </>
  )
}
```

```jsx filename="app/layout.js" switcher
export default function Layout({ children, team, analytics }) {
  return (
    <>
      {children}
      {team}
      {analytics}
    </>
  )
}
```

However, slots are **not** route segments and do not affect the URL structure. For example, for `/@analytics/views`, the URL will be `/views` since `@analytics` is a slot. Slots are combined with the regular [Page](/docs/app/api-reference/file-conventions/page.md) component to form the final page associated with the route segment. Because of this, you cannot have separate [static](/docs/app/guides/caching.md#static-rendering) and [dynamic](/docs/app/guides/caching.md#dynamic-rendering) slots at the same route segment level. If one slot is dynamic, all slots at that level must be dynamic.

> **Good to know**:
>
> * The `children` prop is an implicit slot that does not need to be mapped to a folder. This means `app/page.js` is equivalent to `app/@children/page.js`.

### `default.js`

You can define a `default.js` file to render as a fallback for unmatched slots during the initial load or full-page reload.

Consider the following folder structure. The `@team` slot has a `/settings` page, but `@analytics` does not.

![Parallel Routes unmatched routes](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-unmatched-routes.png)

When navigating to `/settings`, the `@team` slot will render the `/settings` page while maintaining the currently active page for the `@analytics` slot.

On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.

Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.

## Behavior

By default, Next.js keeps track of the active *state* (or subpage) for each slot. However, the content rendered within a slot will depend on the type of navigation:

* [**Soft Navigation**](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions): During client-side navigation, Next.js will perform a [partial render](/docs/app/getting-started/linking-and-navigating.md#client-side-transitions), changing the subpage within the slot, while maintaining the other slot's active subpages, even if they don't match the current URL.
* **Hard Navigation**: After a full-page load (browser refresh), Next.js cannot determine the active state for the slots that don't match the current URL. Instead, it will render a [`default.js`](#defaultjs) file for the unmatched slots, or `404` if `default.js` doesn't exist.

> **Good to know**:
>
> * The `404` for unmatched routes helps ensure that you don't accidentally render a parallel route on a page that it was not intended for.

## Examples

### With `useSelectedLayoutSegment(s)`

Both [`useSelectedLayoutSegment`](/docs/app/api-reference/functions/use-selected-layout-segment.md) and [`useSelectedLayoutSegments`](/docs/app/api-reference/functions/use-selected-layout-segments.md) accept a `parallelRoutesKey` parameter, which allows you to read the active route segment within a slot.

```tsx filename="app/layout.tsx" switcher
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function Layout({ auth }: { auth: React.ReactNode }) {
  const loginSegment = useSelectedLayoutSegment('auth')
  // ...
}
```

```jsx filename="app/layout.js" switcher
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function Layout({ auth }) {
  const loginSegment = useSelectedLayoutSegment('auth')
  // ...
}
```

When a user navigates to `app/@auth/login` (or `/login` in the URL bar), `loginSegment` will be equal to the string `"login"`.

### Conditional Routes

You can use Parallel Routes to conditionally render routes based on certain conditions, such as user role. For example, to render a different dashboard page for the `/admin` or `/user` roles:

![Conditional routes diagram](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/conditional-routes-ui.png)

```tsx filename="app/dashboard/layout.tsx" switcher
import { checkUserRole } from '@/lib/auth'

export default function Layout({
  user,
  admin,
}: {
  user: React.ReactNode
  admin: React.ReactNode
}) {
  const role = checkUserRole()
  return role === 'admin' ? admin : user
}
```

```jsx filename="app/dashboard/layout.js" switcher
import { checkUserRole } from '@/lib/auth'

export default function Layout({ user, admin }) {
  const role = checkUserRole()
  return role === 'admin' ? admin : user
}
```

### Tab Groups

You can add a `layout` inside a slot to allow users to navigate the slot independently. This is useful for creating tabs.

For example, the `@analytics` slot has two subpages: `/page-views` and `/visitors`.

![Analytics slot with two subpages and a layout](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-tab-groups.png)

Within `@analytics`, create a [`layout`](/docs/app/api-reference/file-conventions/layout.md) file to share the tabs between the two pages:

```tsx filename="app/@analytics/layout.tsx" switcher
import Link from 'next/link'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Link href="/page-views">Page Views</Link>
        <Link href="/visitors">Visitors</Link>
      </nav>
      <div>{children}</div>
    </>
  )
}
```

```jsx filename="app/@analytics/layout.js" switcher
import Link from 'next/link'

export default function Layout({ children }) {
  return (
    <>
      <nav>
        <Link href="/page-views">Page Views</Link>
        <Link href="/visitors">Visitors</Link>
      </nav>
      <div>{children}</div>
    </>
  )
}
```

### Modals

Parallel Routes can be used together with [Intercepting Routes](/docs/app/api-reference/file-conventions/intercepting-routes.md) to create modals that support deep linking. This allows you to solve common challenges when building modals, such as:

* Making the modal content **shareable through a URL**.
* **Preserving context** when the page is refreshed, instead of closing the modal.
* **Closing the modal on backwards navigation** rather than going to the previous route.
* **Reopening the modal on forwards navigation**.

Consider the following UI pattern, where a user can open a login modal from a layout using client-side navigation, or access a separate `/login` page:

![Parallel Routes Diagram](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-auth-modal.png)

To implement this pattern, start by creating a `/login` route that renders your **main** login page.

![Parallel Routes Diagram](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-modal-login-page.png)

```tsx filename="app/login/page.tsx" switcher
import { Login } from '@/app/ui/login'

export default function Page() {
  return <Login />
}
```

```jsx filename="app/login/page.js" switcher
import { Login } from '@/app/ui/login'

export default function Page() {
  return <Login />
}
```

Then, inside the `@auth` slot, add [`default.js`](/docs/app/api-reference/file-conventions/default.md) file that returns `null`. This ensures that the modal is not rendered when it's not active.

```tsx filename="app/@auth/default.tsx" switcher
export default function Default() {
  return null
}
```

```jsx filename="app/@auth/default.js" switcher
export default function Default() {
  return null
}
```

Inside your `@auth` slot, intercept the `/login` route by importing the `<Modal>` component and its children into the `@auth/(.)login/page.tsx` file, and updating the folder name to `/@auth/(.)login/page.tsx`.

```tsx filename="app/@auth/(.)login/page.tsx" switcher
import { Modal } from '@/app/ui/modal'
import { Login } from '@/app/ui/login'

export default function Page() {
  return (
    <Modal>
      <Login />
    </Modal>
  )
}
```

```jsx filename="app/@auth/(.)login/page.js" switcher
import { Modal } from '@/app/ui/modal'
import { Login } from '@/app/ui/login'

export default function Page() {
  return (
    <Modal>
      <Login />
    </Modal>
  )
}
```

> **Good to know:**
>
> * The convention `(.)` is used for intercepting routes. See [Intercepting Routes](/docs/app/api-reference/file-conventions/intercepting-routes.md#convention) docs for more information.
> * By separating the `<Modal>` functionality from the modal content (`<Login>`), you can ensure any content inside the modal, e.g. [forms](/docs/app/guides/forms.md), are Server Components. See [Interleaving Client and Server Components](/docs/app/getting-started/server-and-client-components.md#examples#supported-pattern-passing-server-components-to-client-components-as-props) for more information.

#### Opening the modal

Now, you can leverage the Next.js router to open and close the modal. This ensures the URL is correctly updated when the modal is open, and when navigating backwards and forwards.

To open the modal, pass the `@auth` slot as a prop to the parent layout and render it alongside the `children` prop.

```tsx filename="app/layout.tsx" switcher
import Link from 'next/link'

export default function Layout({
  auth,
  children,
}: {
  auth: React.ReactNode
  children: React.ReactNode
}) {
  return (
    <>
      <nav>
        <Link href="/login">Open modal</Link>
      </nav>
      <div>{auth}</div>
      <div>{children}</div>
    </>
  )
}
```

```jsx filename="app/layout.js" switcher
import Link from 'next/link'

export default function Layout({ auth, children }) {
  return (
    <>
      <nav>
        <Link href="/login">Open modal</Link>
      </nav>
      <div>{auth}</div>
      <div>{children}</div>
    </>
  )
}
```

When the user clicks the `<Link>`, the modal will open instead of navigating to the `/login` page. However, on refresh or initial load, navigating to `/login` will take the user to the main login page.

#### Closing the modal

You can close the modal by calling `router.back()` or by using the `Link` component.

```tsx filename="app/ui/modal.tsx" switcher
'use client'

import { useRouter } from 'next/navigation'

export function Modal({ children }: { children: React.ReactNode }) {
  const router = useRouter()

  return (
    <>
      <button
        onClick={() => {
          router.back()
        }}
      >
        Close modal
      </button>
      <div>{children}</div>
    </>
  )
}
```

```jsx filename="app/ui/modal.js" switcher
'use client'

import { useRouter } from 'next/navigation'

export function Modal({ children }) {
  const router = useRouter()

  return (
    <>
      <button
        onClick={() => {
          router.back()
        }}
      >
        Close modal
      </button>
      <div>{children}</div>
    </>
  )
}
```

When using the `Link` component to navigate away from a page that shouldn't render the `@auth` slot anymore, we need to make sure the parallel route matches to a component that returns `null`. For example, when navigating back to the root page, we create a `@auth/page.tsx` component:

```tsx filename="app/ui/modal.tsx" switcher
import Link from 'next/link'

export function Modal({ children }: { children: React.ReactNode }) {
  return (
    <>
      <Link href="/">Close modal</Link>
      <div>{children}</div>
    </>
  )
}
```

```jsx filename="app/ui/modal.js" switcher
import Link from 'next/link'

export function Modal({ children }) {
  return (
    <>
      <Link href="/">Close modal</Link>
      <div>{children}</div>
    </>
  )
}
```

```tsx filename="app/@auth/page.tsx" switcher
export default function Page() {
  return null
}
```

```jsx filename="app/@auth/page.js" switcher
export default function Page() {
  return null
}
```

Or if navigating to any other page (such as `/foo`, `/foo/bar`, etc), you can use a catch-all slot:

```tsx filename="app/@auth/[...catchAll]/page.tsx" switcher
export default function CatchAll() {
  return null
}
```

```jsx filename="app/@auth/[...catchAll]/page.js" switcher
export default function CatchAll() {
  return null
}
```

> **Good to know:**
>
> * We use a catch-all route in our `@auth` slot to close the modal because of how parallel routes behave. Since client-side navigations to a route that no longer match the slot will remain visible, we need to match the slot to a route that returns `null` to close the modal.
> * Other examples could include opening a photo modal in a gallery while also having a dedicated `/photo/[id]` page, or opening a shopping cart in a side modal.
> * [View an example](https://github.com/vercel-labs/nextgram) of modals with Intercepted and Parallel Routes.

### Loading and Error UI

Parallel Routes can be streamed independently, allowing you to define independent error and loading states for each route:

![Parallel routes enable custom error and loading states](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/parallel-routes-cinematic-universe.png)

See the [Loading UI](/docs/app/api-reference/file-conventions/loading.md) and [Error Handling](/docs/app/getting-started/error-handling.md) documentation for more information.
- [default.js](/docs/app/api-reference/file-conventions/default.md)
  - API Reference for the default.js file.


--------------------------------------------------------------------------------
title: "proxy.js"
description: "API reference for the proxy.js file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/proxy"
--------------------------------------------------------------------------------

# proxy.js

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

1. `rewrite` to a route ([Page](/docs/app/api-reference/file-conventions/page.md) or [Route Handler](/docs/app/api-reference/file-conventions/route.md)) that produces a response
2. return a `NextResponse` directly. See [Producing a Response](#producing-a-response)

> **Good to know**: For redirects, you can also use `Response.redirect` instead of `NextResponse.redirect`.

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

> **Good to know:** You can configure CORS headers for individual routes in [Route Handlers](/docs/app/api-reference/file-conventions/route.md#cors).

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
source: "https://nextjs.org/docs/app/api-reference/file-conventions/public-folder"
--------------------------------------------------------------------------------

# public

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

For static metadata files, such as `robots.txt`, `favicon.ico`, etc, you should use [special metadata files](/docs/app/api-reference/file-conventions/metadata.md) inside the `app` folder.


--------------------------------------------------------------------------------
title: "route.js"
description: "API reference for the route.js special file."
source: "https://nextjs.org/docs/app/api-reference/file-conventions/route"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./06-videos.md) | [Index](./index.md) | [Next →](./08-routejs.md)
