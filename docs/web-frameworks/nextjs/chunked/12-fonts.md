**Navigation:** [← Previous](./11-staticgeneration.md) | [Index](./index.md) | [Next →](./13-app-router.md)

---

# Fonts

@router: Pages Router

The [`next/font`](/docs/app/api-reference/components/font.md) module automatically optimizes your fonts and removes external network requests for improved privacy and performance.

It includes **built-in self-hosting** for any font file. This means you can optimally load web fonts with no layout shift.

To start using `next/font`, import it from [`next/font/local`](#local-fonts) or [`next/font/google`](#google-fonts), call it as a function with the appropriate options, and set the `className` of the element you want to apply the font to. For example:

```tsx filename="app/layout.tsx" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" highlight={1,3-5,9} switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function Layout({ children }) {
  return (
    <html className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

Fonts are scoped to the component they're used in. To apply a font to your entire application, add it to the [Root Layout](/docs/app/api-reference/file-conventions/layout.md#root-layout).

## Google fonts

You can automatically self-host any Google Font. Fonts are included stored as static assets and served from the same domain as your deployment, meaning no requests are sent to Google by the browser when the user visits your site.

To start using a Google Font, import your chosen font from `next/font/google`:

```tsx filename="app/layout.tsx" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import { Geist } from 'next/font/google'

const geist = Geist({
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={geist.className}>
      <body>{children}</body>
    </html>
  )
}
```

We recommend using [variable fonts](https://fonts.google.com/variablefonts) for the best performance and flexibility. But if you can't use a variable font, you will need to specify a weight:

```tsx filename="app/layout.tsx" highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js"  highlight={4} switcher
import { Roboto } from 'next/font/google'

const roboto = Roboto({
  weight: '400',
  subsets: ['latin'],
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={roboto.className}>
      <body>{children}</body>
    </html>
  )
}
```

## Local fonts

To use a local font, import your font from `next/font/local` and specify the [`src`](/docs/app/api-reference/components/font.md#src) of your local font file. Fonts can be stored in the [`public`](/docs/app/api-reference/file-conventions/public-folder.md) folder or co-located inside the `app` folder. For example:

```tsx filename="app/layout.tsx" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import localFont from 'next/font/local'

const myFont = localFont({
  src: './my-font.woff2',
})

export default function RootLayout({ children }) {
  return (
    <html lang="en" className={myFont.className}>
      <body>{children}</body>
    </html>
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
## API Reference

See the API Reference for the full feature set of Next.js Font

- [Font](/docs/app/api-reference/components/font.md)
  - Optimizing loading web fonts with the built-in `next/font` loaders.


--------------------------------------------------------------------------------
title: "CSS"
description: "Learn about the different ways to add CSS to your application, including Tailwind CSS, CSS Modules, Global CSS, and more."
source: "https://nextjs.org/docs/pages/getting-started/css"
--------------------------------------------------------------------------------

# CSS

@router: Pages Router

Next.js provides several ways to style your application using CSS, including:

* [Tailwind CSS](#tailwind-css)
* [CSS Modules](#css-modules)
* [Global CSS](#global-css)
* [External Stylesheets](#external-stylesheets)
* [Sass](/docs/app/guides/sass.md)
* [CSS-in-JS](/docs/app/guides/css-in-js.md)

## Tailwind CSS

[Tailwind CSS](https://tailwindcss.com/) is a utility-first CSS framework that provides low-level utility classes to build custom designs.

Install Tailwind CSS:

```bash package="pnpm"
pnpm add -D tailwindcss @tailwindcss/postcss
```

```bash package="npm"
npm install -D tailwindcss @tailwindcss/postcss
```

```bash package="yarn"
yarn add -D tailwindcss @tailwindcss/postcss
```

```bash package="bun"
bun add -D tailwindcss @tailwindcss/postcss
```

Add the PostCSS plugin to your `postcss.config.mjs` file:

```js filename="postcss.config.mjs"
export default {
  plugins: {
    '@tailwindcss/postcss': {},
  },
}
```

Import Tailwind in your global CSS file:

```css filename="styles/globals.css"
@import 'tailwindcss';
```

Import the CSS file in your `pages/_app.js` file:

```jsx filename="pages/_app.js"
import '@/styles/globals.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Now you can start using Tailwind's utility classes in your application:

```tsx filename="pages/index.tsx" switcher
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

```jsx filename="pages/index.js" switcher
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="text-4xl font-bold">Welcome to Next.js!</h1>
    </main>
  )
}
```

> **Good to know:** If you need broader browser support for very old browsers, see the [Tailwind CSS v3 setup instructions](/docs/app/guides/tailwind-v3-css.md).

## CSS Modules

CSS Modules locally scope CSS by generating unique class names. This allows you to use the same class in different files without worrying about naming collisions.

To start using CSS Modules, create a new file with the extension `.module.css` and import it into any component inside the `pages` directory:

```css filename="/styles/blog.module.css"
.blog {
  padding: 24px;
}
```

```tsx filename="pages/blog/index.tsx" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

```jsx filename="pages/blog/index.js" switcher
import styles from './blog.module.css'

export default function Page() {
  return <main className={styles.blog}></main>
}
```

## Global CSS

You can use global CSS to apply styles across your application.

Import the stylesheet in the `pages/_app.js` file to apply the styles to **every route** in your application:

```tsx filename="pages/_app.js"
import '@/styles/global.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

Due to the global nature of stylesheets, and to avoid conflicts, you should import them inside [`pages/_app.js`](/docs/pages/building-your-application/routing/custom-app.md).

## External stylesheets

Next.js allows you to import CSS files from a JavaScript file. This is possible because Next.js extends the concept of [`import`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/import) beyond JavaScript.

### Import styles from `node_modules`

Since Next.js **9.5.4**, importing a CSS file from `node_modules` is permitted anywhere in your application.

For global stylesheets, like `bootstrap` or `nprogress`, you should import the file inside `pages/_app.js`. For example:

```jsx filename="pages/_app.js"
import 'bootstrap/dist/css/bootstrap.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

To import CSS required by a third-party component, you can do so in your component. For example:

```jsx filename="components/example-dialog.js"
import { useState } from 'react'
import { Dialog } from '@reach/dialog'
import VisuallyHidden from '@reach/visually-hidden'
import '@reach/dialog/styles.css'

function ExampleDialog(props) {
  const [showDialog, setShowDialog] = useState(false)
  const open = () => setShowDialog(true)
  const close = () => setShowDialog(false)

  return (
    <div>
      <button onClick={open}>Open Dialog</button>
      <Dialog isOpen={showDialog} onDismiss={close}>
        <button className="close-button" onClick={close}>
          <VisuallyHidden>Close</VisuallyHidden>
          <span aria-hidden>×</span>
        </button>
        <p>Hello there. I am a dialog</p>
      </Dialog>
    </div>
  )
}
```

## Ordering and Merging

Next.js optimizes CSS during production builds by automatically chunking (merging) stylesheets. The **order of your CSS** depends on the **order you import styles in your code**.

For example, `base-button.module.css` will be ordered before `page.module.css` since `<BaseButton>` is imported before `page.module.css`:

```tsx filename="page.tsx" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```jsx filename="page.js" switcher
import { BaseButton } from './base-button'
import styles from './page.module.css'

export default function Page() {
  return <BaseButton className={styles.primary} />
}
```

```tsx filename="base-button.tsx" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

```jsx filename="base-button.js" switcher
import styles from './base-button.module.css'

export function BaseButton() {
  return <button className={styles.primary} />
}
```

### Recommendations

To keep CSS ordering predictable:

* Try to contain CSS imports to a single JavaScript or TypeScript entry file
* Import global styles and Tailwind stylesheets in the root of your application.
* **Use Tailwind CSS** for most styling needs as it covers common design patterns with utility classes.
* Use CSS Modules for component-specific styles when Tailwind utilities aren't sufficient.
* Use a consistent naming convention for your CSS modules. For example, using `<name>.module.css` over `<name>.tsx`.
* Extract shared styles into shared components to avoid duplicate imports.
* Turn off linters or formatters that auto-sort imports like ESLint’s [`sort-imports`](https://eslint.org/docs/latest/rules/sort-imports).
* You can use the [`cssChunking`](/docs/app/api-reference/config/next-config-js/cssChunking.md) option in `next.config.js` to control how CSS is chunked.

## Development vs Production

* In development (`next dev`), CSS updates apply instantly with [Fast Refresh](/docs/architecture/fast-refresh.md).
* In production (`next build`), all CSS files are automatically concatenated into **many minified and code-split** `.css` files, ensuring the minimal amount of CSS is loaded for a route.
* CSS still loads with JavaScript disabled in production, but JavaScript is required in development for Fast Refresh.
* CSS ordering can behave differently in development, always ensure to check the build (`next build`) to verify the final CSS order.
## Next Steps

Learn more about the alternatives ways you can use CSS in your application.

- [Tailwind CSS v3](/docs/app/guides/tailwind-v3-css.md)
  - Style your Next.js Application using Tailwind CSS v3 for broader browser support.
- [Sass](/docs/app/guides/sass.md)
  - Style your Next.js application using Sass.
- [CSS-in-JS](/docs/app/guides/css-in-js.md)
  - Use CSS-in-JS libraries with Next.js


--------------------------------------------------------------------------------
title: "Deploying"
description: "Learn how to deploy your Next.js application."
source: "https://nextjs.org/docs/pages/getting-started/deploying"
--------------------------------------------------------------------------------

# Deploying

@router: Pages Router

Next.js can be deployed as a Node.js server, Docker container, static export, or adapted to run on different platforms.

| Deployment Option                | Feature Support   |
| -------------------------------- | ----------------- |
| [Node.js server](#nodejs-server) | All               |
| [Docker container](#docker)      | All               |
| [Static export](#static-export)  | Limited           |
| [Adapters](#adapters)            | Platform-specific |

## Node.js server

Next.js can be deployed to any provider that supports Node.js. Ensure your `package.json` has the `"build"` and `"start"` scripts:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

Then, run `npm run build` to build your application and `npm run start` to start the Node.js server. This server supports all Next.js features. If needed, you can also eject to a [custom server](/docs/app/guides/custom-server.md).

Node.js deployments support all Next.js features. Learn how to [configure them](/docs/app/guides/self-hosting.md) for your infrastructure.

### Templates

* [Flightcontrol](https://github.com/nextjs/deploy-flightcontrol)
* [Railway](https://github.com/nextjs/deploy-railway)
* [Replit](https://github.com/nextjs/deploy-replit)

## Docker

Next.js can be deployed to any provider that supports [Docker](https://www.docker.com/) containers. This includes container orchestrators like Kubernetes or a cloud provider that runs Docker.

Docker deployments support all Next.js features. Learn how to [configure them](/docs/app/guides/self-hosting.md) for your infrastructure.

> **Note for development:** While Docker is excellent for production deployments, consider using local development (`npm run dev`) instead of Docker during development on Mac and Windows for better performance. [Learn more about optimizing local development](/docs/app/guides/local-development.md).

### Templates

* [Docker](https://github.com/vercel/next.js/tree/canary/examples/with-docker)
* [Docker Multi-Environment](https://github.com/vercel/next.js/tree/canary/examples/with-docker-multi-env)
* [DigitalOcean](https://github.com/nextjs/deploy-digitalocean)
* [Fly.io](https://github.com/nextjs/deploy-fly)
* [Google Cloud Run](https://github.com/nextjs/deploy-google-cloud-run)
* [Render](https://github.com/nextjs/deploy-render)
* [SST](https://github.com/nextjs/deploy-sst)

## Static export

Next.js enables starting as a static site or [Single-Page Application (SPA)](/docs/app/guides/single-page-applications.md), then later optionally upgrading to use features that require a server.

Since Next.js supports [static exports](/docs/app/guides/static-exports.md), it can be deployed and hosted on any web server that can serve HTML/CSS/JS static assets. This includes tools like AWS S3, Nginx, or Apache.

Running as a [static export](/docs/app/guides/static-exports.md) **does not** support Next.js features that require a server. [Learn more](/docs/app/guides/static-exports.md#unsupported-features).

### Templates

* [GitHub Pages](https://github.com/nextjs/deploy-github-pages)

## Adapters

Next.js can be adapted to run on different platforms to support their infrastructure capabilities.

Refer to each provider's documentation for information on supported Next.js features:

* [AWS Amplify Hosting](https://docs.amplify.aws/nextjs/start/quickstart/nextjs-app-router-client-components)
* [Cloudflare](https://developers.cloudflare.com/workers/frameworks/framework-guides/nextjs)
* [Deno Deploy](https://docs.deno.com/examples/next_tutorial)
* [Netlify](https://docs.netlify.com/frameworks/next-js/overview/#next-js-support-on-netlify)
* [Vercel](https://vercel.com/docs/frameworks/nextjs)

> **Note:** We are working on a [Deployment Adapters API](https://github.com/vercel/next.js/discussions/77740) for all platforms to adopt. After completion, we will add documentation on how to write your own adapters.



--------------------------------------------------------------------------------
title: "Guides"
description: "Learn how to implement common UI patterns and use cases using Next.js"
source: "https://nextjs.org/docs/pages/guides"
--------------------------------------------------------------------------------

# Guides

@router: Pages Router



 - [Analytics](/docs/pages/guides/analytics.md)
 - [Authentication](/docs/pages/guides/authentication.md)
 - [Babel](/docs/pages/guides/babel.md)
 - [CI Build Caching](/docs/pages/guides/ci-build-caching.md)
 - [Content Security Policy](/docs/pages/guides/content-security-policy.md)
 - [CSS-in-JS](/docs/pages/guides/css-in-js.md)
 - [Custom Server](/docs/pages/guides/custom-server.md)
 - [Debugging](/docs/pages/guides/debugging.md)
 - [Draft Mode](/docs/pages/guides/draft-mode.md)
 - [Environment Variables](/docs/pages/guides/environment-variables.md)
 - [Forms](/docs/pages/guides/forms.md)
 - [ISR](/docs/pages/guides/incremental-static-regeneration.md)
 - [Instrumentation](/docs/pages/guides/instrumentation.md)
 - [Internationalization](/docs/pages/guides/internationalization.md)
 - [Lazy Loading](/docs/pages/guides/lazy-loading.md)
 - [MDX](/docs/pages/guides/mdx.md)
 - [Migrating](/docs/pages/guides/migrating.md)
 - [Multi-Zones](/docs/pages/guides/multi-zones.md)
 - [OpenTelemetry](/docs/pages/guides/open-telemetry.md)
 - [Package Bundling](/docs/pages/guides/package-bundling.md)
 - [PostCSS](/docs/pages/guides/post-css.md)
 - [Preview Mode](/docs/pages/guides/preview-mode.md)
 - [Production](/docs/pages/guides/production-checklist.md)
 - [Redirecting](/docs/pages/guides/redirecting.md)
 - [Sass](/docs/pages/guides/sass.md)
 - [Scripts](/docs/pages/guides/scripts.md)
 - [Self-Hosting](/docs/pages/guides/self-hosting.md)
 - [Static Exports](/docs/pages/guides/static-exports.md)
 - [Tailwind CSS](/docs/pages/guides/tailwind-v3-css.md)
 - [Testing](/docs/pages/guides/testing.md)
 - [Third Party Libraries](/docs/pages/guides/third-party-libraries.md)
 - [Upgrading](/docs/pages/guides/upgrading.md)

--------------------------------------------------------------------------------
title: "How to add analytics to your Next.js application"
description: "Measure and track page performance using Next.js Speed Insights"
source: "https://nextjs.org/docs/pages/guides/analytics"
--------------------------------------------------------------------------------

# Analytics

@router: Pages Router

Next.js has built-in support for measuring and reporting performance metrics. You can either use the [`useReportWebVitals`](/docs/app/api-reference/functions/use-report-web-vitals.md) hook to manage reporting yourself, or alternatively, Vercel provides a [managed service](https://vercel.com/analytics?utm_source=next-site\&utm_medium=docs\&utm_campaign=next-website) to automatically collect and visualize metrics for you.

## Client Instrumentation

For more advanced analytics and monitoring needs, Next.js provides a `instrumentation-client.js|ts` file that runs before your application's frontend code starts executing. This is ideal for setting up global analytics, error tracking, or performance monitoring tools.

To use it, create an `instrumentation-client.js` or `instrumentation-client.ts` file in your application's root directory:

```js filename="instrumentation-client.js"
// Initialize analytics before the app starts
console.log('Analytics initialized')

// Set up global error tracking
window.addEventListener('error', (event) => {
  // Send to your error tracking service
  reportError(event.error)
})
```

## Build Your Own

```jsx filename="pages/_app.js"
import { useReportWebVitals } from 'next/web-vitals'

function MyApp({ Component, pageProps }) {
  useReportWebVitals((metric) => {
    console.log(metric)
  })

  return <Component {...pageProps} />
}
```

View the [API Reference](/docs/pages/api-reference/functions/use-report-web-vitals.md) for more information.

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

function MyApp({ Component, pageProps }) {
  useReportWebVitals((metric) => {
    switch (metric.name) {
      case 'FCP': {
        // handle FCP results
      }
      case 'LCP': {
        // handle LCP results
      }
      // ...
    }
  })

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

```js
export function reportWebVitals(metric) {
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
```

These metrics work in all browsers that support the [User Timing API](https://caniuse.com/#feat=user-timing).

## Sending results to external systems

You can send results to any endpoint to measure and track
real user performance on your site. For example:

```js
useReportWebVitals((metric) => {
  const body = JSON.stringify(metric)
  const url = 'https://example.com/analytics'

  // Use `navigator.sendBeacon()` if available, falling back to `fetch()`.
  if (navigator.sendBeacon) {
    navigator.sendBeacon(url, body)
  } else {
    fetch(url, { body, method: 'POST', keepalive: true })
  }
})
```

> **Good to know**: If you use [Google Analytics](https://analytics.google.com/analytics/web/), using the
> `id` value can allow you to construct metric distributions manually (to calculate percentiles,
> etc.)

> ```js
> useReportWebVitals((metric) => {
>   // Use `window.gtag` if you initialized Google Analytics as this example:
>   // https://github.com/vercel/next.js/blob/canary/examples/with-google-analytics
>   window.gtag('event', metric.name, {
>     value: Math.round(
>       metric.name === 'CLS' ? metric.value * 1000 : metric.value
>     ), // values must be integers
>     event_label: metric.id, // id unique to current page load
>     non_interaction: true, // avoids affecting bounce rate.
>   })
> })
> ```
>
> Read more about [sending results to Google Analytics](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics).


--------------------------------------------------------------------------------
title: "How to implement authentication in Next.js"
description: "Learn how to implement authentication in your Next.js application."
source: "https://nextjs.org/docs/pages/guides/authentication"
--------------------------------------------------------------------------------

# Authentication

@router: Pages Router

Understanding authentication is crucial for protecting your application's data. This page will guide you through what React and Next.js features to use to implement auth.

Before starting, it helps to break down the process into three concepts:

1. **[Authentication](#authentication)**: Verifies if the user is who they say they are. It requires the user to prove their identity with something they have, such as a username and password.
2. **[Session Management](#session-management)**: Tracks the user's auth state across requests.
3. **[Authorization](#authorization)**: Decides what routes and data the user can access.

This diagram shows the authentication flow using React and Next.js features:

![Diagram showing the authentication flow with React and Next.js features](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/authentication-overview.png)

The examples on this page walk through basic username and password auth for educational purposes. While you can implement a custom auth solution, for increased security and simplicity, we recommend using an authentication library. These offer built-in solutions for authentication, session management, and authorization, as well as additional features such as social logins, multi-factor authentication, and role-based access control. You can find a list in the [Auth Libraries](#auth-libraries) section.

## Authentication

Here are the steps to implement a sign-up and/or login form:

1. The user submits their credentials through a form.
2. The form sends a request that is handled by an API route.
3. Upon successful verification, the process is completed, indicating the user's successful authentication.
4. If verification is unsuccessful, an error message is shown.

Consider a login form where users can input their credentials:

```tsx filename="pages/login.tsx" switcher
import { FormEvent } from 'react'
import { useRouter } from 'next/router'

export default function LoginPage() {
  const router = useRouter()

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const formData = new FormData(event.currentTarget)
    const email = formData.get('email')
    const password = formData.get('password')

    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    })

    if (response.ok) {
      router.push('/profile')
    } else {
      // Handle errors
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" placeholder="Email" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  )
}
```

```jsx filename="pages/login.jsx" switcher
import { FormEvent } from 'react'
import { useRouter } from 'next/router'

export default function LoginPage() {
  const router = useRouter()

  async function handleSubmit(event) {
    event.preventDefault()

    const formData = new FormData(event.currentTarget)
    const email = formData.get('email')
    const password = formData.get('password')

    const response = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    })

    if (response.ok) {
      router.push('/profile')
    } else {
      // Handle errors
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" placeholder="Email" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  )
}
```

The form above has two input fields for capturing the user's email and password. On submission, it triggers a function that sends a POST request to an API route (`/api/auth/login`).

You can then call your Authentication Provider's API in the API route to handle authentication:

```ts filename="pages/api/auth/login.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'
import { signIn } from '@/auth'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const { email, password } = req.body
    await signIn('credentials', { email, password })

    res.status(200).json({ success: true })
  } catch (error) {
    if (error.type === 'CredentialsSignin') {
      res.status(401).json({ error: 'Invalid credentials.' })
    } else {
      res.status(500).json({ error: 'Something went wrong.' })
    }
  }
}
```

```js filename="pages/api/auth/login.js" switcher
import { signIn } from '@/auth'

export default async function handler(req, res) {
  try {
    const { email, password } = req.body
    await signIn('credentials', { email, password })

    res.status(200).json({ success: true })
  } catch (error) {
    if (error.type === 'CredentialsSignin') {
      res.status(401).json({ error: 'Invalid credentials.' })
    } else {
      res.status(500).json({ error: 'Something went wrong.' })
    }
  }
}
```

## Session Management

Session management ensures that the user's authenticated state is preserved across requests. It involves creating, storing, refreshing, and deleting sessions or tokens.

There are two types of sessions:

1. [**Stateless**](#stateless-sessions): Session data (or a token) is stored in the browser's cookies. The cookie is sent with each request, allowing the session to be verified on the server. This method is simpler, but can be less secure if not implemented correctly.
2. [**Database**](#database-sessions): Session data is stored in a database, with the user's browser only receiving the encrypted session ID. This method is more secure, but can be complex and use more server resources.

> **Good to know:** While you can use either method, or both, we recommend using a session management library such as [iron-session](https://github.com/vvo/iron-session) or [Jose](https://github.com/panva/jose).

### Stateless Sessions

#### Setting and deleting cookies

You can use [API Routes](/docs/pages/building-your-application/routing/api-routes.md) to set the session as a cookie on the server:

```ts filename="pages/api/login.ts" switcher
import { serialize } from 'cookie'
import type { NextApiRequest, NextApiResponse } from 'next'
import { encrypt } from '@/app/lib/session'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const sessionData = req.body
  const encryptedSessionData = encrypt(sessionData)

  const cookie = serialize('session', encryptedSessionData, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    maxAge: 60 * 60 * 24 * 7, // One week
    path: '/',
  })
  res.setHeader('Set-Cookie', cookie)
  res.status(200).json({ message: 'Successfully set cookie!' })
}
```

```js filename="pages/api/login.js" switcher
import { serialize } from 'cookie'
import { encrypt } from '@/app/lib/session'

export default function handler(req, res) {
  const sessionData = req.body
  const encryptedSessionData = encrypt(sessionData)

  const cookie = serialize('session', encryptedSessionData, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    maxAge: 60 * 60 * 24 * 7, // One week
    path: '/',
  })
  res.setHeader('Set-Cookie', cookie)
  res.status(200).json({ message: 'Successfully set cookie!' })
}
```

### Database Sessions

To create and manage database sessions, you'll need to follow these steps:

1. Create a table in your database to store session and data (or check if your Auth Library handles this).
2. Implement functionality to insert, update, and delete sessions
3. Encrypt the session ID before storing it in the user's browser, and ensure the database and cookie stay in sync (this is optional, but recommended for optimistic auth checks in [Proxy](#optimistic-checks-with-proxy-optional)).

**Creating a Session on the Server**:

```ts filename="pages/api/create-session.ts" switcher
import db from '../../lib/db'
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const user = req.body
    const sessionId = generateSessionId()
    await db.insertSession({
      sessionId,
      userId: user.id,
      createdAt: new Date(),
    })

    res.status(200).json({ sessionId })
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' })
  }
}
```

```js filename="pages/api/create-session.js" switcher
import db from '../../lib/db'

export default async function handler(req, res) {
  try {
    const user = req.body
    const sessionId = generateSessionId()
    await db.insertSession({
      sessionId,
      userId: user.id,
      createdAt: new Date(),
    })

    res.status(200).json({ sessionId })
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' })
  }
}
```

## Authorization

Once a user is authenticated and a session is created, you can implement authorization to control what the user can access and do within your application.

There are two main types of authorization checks:

1. **Optimistic**: Checks if the user is authorized to access a route or perform an action using the session data stored in the cookie. These checks are useful for quick operations, such as showing/hiding UI elements or redirecting users based on permissions or roles.
2. **Secure**: Checks if the user is authorized to access a route or perform an action using the session data stored in the database. These checks are more secure and are used for operations that require access to sensitive data or actions.

For both cases, we recommend:

* Creating a [Data Access Layer](#creating-a-data-access-layer-dal) to centralize your authorization logic
* Using [Data Transfer Objects (DTO)](#using-data-transfer-objects-dto) to only return the necessary data
* Optionally use [Proxy](#optimistic-checks-with-proxy-optional) to perform optimistic checks.

### Optimistic checks with Proxy (Optional)

There are some cases where you may want to use [Proxy](/docs/app/api-reference/file-conventions/proxy.md) and redirect users based on permissions:

* To perform optimistic checks. Since Proxy runs on every route, it's a good way to centralize redirect logic and pre-filter unauthorized users.
* To protect static routes that share data between users (e.g. content behind a paywall).

However, since Proxy runs on every route, including [prefetched](/docs/app/getting-started/linking-and-navigating.md#prefetching) routes, it's important to only read the session from the cookie (optimistic checks), and avoid database checks to prevent performance issues.

For example:

```tsx filename="proxy.ts" switcher
import { NextRequest, NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']

export default async function proxy(req: NextRequest) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)

  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  // 4. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 5. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']

export default async function proxy(req) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)

  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  // 5. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 6. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

While Proxy can be useful for initial checks, it should not be your only line of defense in protecting your data. The majority of security checks should be performed as close as possible to your data source, see [Data Access Layer](#creating-a-data-access-layer-dal) for more information.

> **Tips**:
>
> * In Proxy, you can also read cookies using `req.cookies.get('session').value`.
> * Proxy uses the Node.js runtime, check if your Auth library and session management library are compatible. You may need to use [Middleware](https://github.com/vercel/next.js/blob/v15.5.6/docs/01-app/03-api-reference/03-file-conventions/middleware.mdx) if your Auth library only supports [Edge Runtime](/docs/app/api-reference/edge.md)
> * You can use the `matcher` property in the Proxy to specify which routes Proxy should run on. Although, for auth, it's recommended Proxy runs on all routes.

### Creating a Data Access Layer (DAL)

#### Protecting API Routes

API Routes in Next.js are essential for handling server-side logic and data management. It's crucial to secure these routes to ensure that only authorized users can access specific functionalities. This typically involves verifying the user's authentication status and their role-based permissions.

Here's an example of securing an API Route:

```ts filename="pages/api/route.ts" switcher
import { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const session = await getSession(req)

  // Check if the user is authenticated
  if (!session) {
    res.status(401).json({
      error: 'User is not authenticated',
    })
    return
  }

  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    res.status(401).json({
      error: 'Unauthorized access: User does not have admin privileges.',
    })
    return
  }

  // Proceed with the route for authorized users
  // ... implementation of the API Route
}
```

```js filename="pages/api/route.js" switcher
export default async function handler(req, res) {
  const session = await getSession(req)

  // Check if the user is authenticated
  if (!session) {
    res.status(401).json({
      error: 'User is not authenticated',
    })
    return
  }

  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    res.status(401).json({
      error: 'Unauthorized access: User does not have admin privileges.',
    })
    return
  }

  // Proceed with the route for authorized users
  // ... implementation of the API Route
}
```

This example demonstrates an API Route with a two-tier security check for authentication and authorization. It first checks for an active session, and then verifies if the logged-in user is an 'admin'. This approach ensures secure access, limited to authenticated and authorized users, maintaining robust security for request processing.

## Resources

Now that you've learned about authentication in Next.js, here are Next.js-compatible libraries and resources to help you implement secure authentication and session management:

### Auth Libraries

* [Auth0](https://auth0.com/docs/quickstart/webapp/nextjs/01-login)
* [Better Auth](https://www.better-auth.com/docs/integrations/next)
* [Clerk](https://clerk.com/docs/quickstarts/nextjs)
* [Descope](https://docs.descope.com/getting-started/nextjs)
* [Kinde](https://kinde.com/docs/developer-tools/nextjs-sdk)
* [Logto](https://docs.logto.io/quick-starts/next-app-router)
* [NextAuth.js](https://authjs.dev/getting-started/installation?framework=next.js)
* [Ory](https://www.ory.sh/docs/getting-started/integrate-auth/nextjs)
* [Stack Auth](https://docs.stack-auth.com/getting-started/setup)
* [Supabase](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
* [Stytch](https://stytch.com/docs/guides/quickstarts/nextjs)
* [WorkOS](https://workos.com/docs/user-management/nextjs)

### Session Management Libraries

* [Iron Session](https://github.com/vvo/iron-session)
* [Jose](https://github.com/panva/jose)

## Further Reading

To continue learning about authentication and security, check out the following resources:

* [How to think about security in Next.js](/blog/security-nextjs-server-components-actions)
* [Understanding XSS Attacks](https://vercel.com/guides/understanding-xss-attacks)
* [Understanding CSRF Attacks](https://vercel.com/guides/understanding-csrf-attacks)
* [The Copenhagen Book](https://thecopenhagenbook.com/)


--------------------------------------------------------------------------------
title: "How to configure Babel in Next.js"
description: "Extend the babel preset added by Next.js with your own configs."
source: "https://nextjs.org/docs/pages/guides/babel"
--------------------------------------------------------------------------------

# Babel

@router: Pages Router

<details>
<summary>Examples</summary>

* [Customizing babel configuration](https://github.com/vercel/next.js/tree/canary/examples/with-custom-babel-config)

</details>

Next.js includes the `next/babel` preset to your app, which includes everything needed to compile React applications and server-side code. But if you want to extend the default Babel configs, it's also possible.

## Adding Presets and Plugins

To start, you only need to define a `.babelrc` file (or `babel.config.js`) in the root directory of your project. If such a file is found, it will be considered as the *source of truth*, and therefore it needs to define what Next.js needs as well, which is the `next/babel` preset.

Here's an example `.babelrc` file:

```json filename=".babelrc"
{
  "presets": ["next/babel"],
  "plugins": []
}
```

You can [take a look at this file](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/babel/preset.ts) to learn about the presets included by `next/babel`.

To add presets/plugins **without configuring them**, you can do it this way:

```json filename=".babelrc"
{
  "presets": ["next/babel"],
  "plugins": ["@babel/plugin-proposal-do-expressions"]
}
```

## Customizing Presets and Plugins

To add presets/plugins **with custom configuration**, do it on the `next/babel` preset like so:

```json filename=".babelrc"
{
  "presets": [
    [
      "next/babel",
      {
        "preset-env": {},
        "transform-runtime": {},
        "styled-jsx": {},
        "class-properties": {}
      }
    ]
  ],
  "plugins": []
}
```

To learn more about the available options for each config, visit babel's [documentation](https://babeljs.io/docs/) site.

> **Good to know**:
>
> * Next.js uses the [**current** Node.js version](https://github.com/nodejs/release#release-schedule) for server-side compilations.
> * The `modules` option on `"preset-env"` should be kept to `false`, otherwise webpack code splitting is turned off.


--------------------------------------------------------------------------------
title: "How to configure Continuous Integration (CI) build caching"
description: "Learn how to configure CI to cache Next.js builds"
source: "https://nextjs.org/docs/pages/guides/ci-build-caching"
--------------------------------------------------------------------------------

# CI Build Caching

@router: Pages Router

To improve build performance, Next.js saves a cache to `.next/cache` that is shared between builds.

To take advantage of this cache in Continuous Integration (CI) environments, your CI workflow will need to be configured to correctly persist the cache between builds.

> If your CI is not configured to persist `.next/cache` between builds, you may see a [No Cache Detected](/docs/messages/no-cache.md) error.

Here are some example cache configurations for common CI providers:

## Vercel

Next.js caching is automatically configured for you. There's no action required on your part. If you are using Turborepo on Vercel, [learn more here](https://vercel.com/docs/monorepos/turborepo).

## CircleCI

Edit your `save_cache` step in `.circleci/config.yml` to include `.next/cache`:

```yaml
steps:
  - save_cache:
      key: dependency-cache-{{ checksum "yarn.lock" }}
      paths:
        - ./node_modules
        - ./.next/cache
```

If you do not have a `save_cache` key, please follow CircleCI's [documentation on setting up build caching](https://circleci.com/docs/2.0/caching/).

## Travis CI

Add or merge the following into your `.travis.yml`:

```yaml
cache:
  directories:
    - $HOME/.cache/yarn
    - node_modules
    - .next/cache
```

## GitLab CI

Add or merge the following into your `.gitlab-ci.yml`:

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .next/cache/
```

## Netlify CI

Use [Netlify Plugins](https://www.netlify.com/products/build/plugins/) with [`@netlify/plugin-nextjs`](https://www.npmjs.com/package/@netlify/plugin-nextjs).

## AWS CodeBuild

Add (or merge in) the following to your `buildspec.yml`:

```yaml
cache:
  paths:
    - 'node_modules/**/*' # Cache `node_modules` for faster `yarn` or `npm i`
    - '.next/cache/**/*' # Cache Next.js for faster application rebuilds
```

## GitHub Actions

Using GitHub's [actions/cache](https://github.com/actions/cache), add the following step in your workflow file:

```yaml
uses: actions/cache@v4
with:
  # See here for caching with `yarn`, `bun` or other package managers https://github.com/actions/cache/blob/main/examples.md or you can leverage caching with actions/setup-node https://github.com/actions/setup-node
  path: |
    ~/.npm
    ${{ github.workspace }}/.next/cache
  # Generate a new cache whenever packages or source files change.
  key: ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-${{ hashFiles('**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx') }}
  # If source files changed but packages didn't, rebuild from a prior cache.
  restore-keys: |
    ${{ runner.os }}-nextjs-${{ hashFiles('**/package-lock.json') }}-
```

## Bitbucket Pipelines

Add or merge the following into your `bitbucket-pipelines.yml` at the top level (same level as `pipelines`):

```yaml
definitions:
  caches:
    nextcache: .next/cache
```

Then reference it in the `caches` section of your pipeline's `step`:

```yaml
- step:
    name: your_step_name
    caches:
      - node
      - nextcache
```

## Heroku

Using Heroku's [custom cache](https://devcenter.heroku.com/articles/nodejs-support#custom-caching), add a `cacheDirectories` array in your top-level package.json:

```javascript
"cacheDirectories": [".next/cache"]
```

## Azure Pipelines

Using Azure Pipelines' [Cache task](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/utility/cache), add the following task to your pipeline yaml file somewhere prior to the task that executes `next build`:

```yaml
- task: Cache@2
  displayName: 'Cache .next/cache'
  inputs:
    key: next | $(Agent.OS) | yarn.lock
    path: '$(System.DefaultWorkingDirectory)/.next/cache'
```

## Jenkins (Pipeline)

Using Jenkins' [Job Cacher](https://www.jenkins.io/doc/pipeline/steps/jobcacher/) plugin, add the following build step to your `Jenkinsfile` where you would normally run `next build` or `npm install`:

```yaml
stage("Restore npm packages") {
    steps {
        // Writes lock-file to cache based on the GIT_COMMIT hash
        writeFile file: "next-lock.cache", text: "$GIT_COMMIT"

        cache(caches: [
            arbitraryFileCache(
                path: "node_modules",
                includes: "**/*",
                cacheValidityDecidingFile: "package-lock.json"
            )
        ]) {
            sh "npm install"
        }
    }
}
stage("Build") {
    steps {
        // Writes lock-file to cache based on the GIT_COMMIT hash
        writeFile file: "next-lock.cache", text: "$GIT_COMMIT"

        cache(caches: [
            arbitraryFileCache(
                path: ".next/cache",
                includes: "**/*",
                cacheValidityDecidingFile: "next-lock.cache"
            )
        ]) {
            // aka `next build`
            sh "npm run build"
        }
    }
}
```


--------------------------------------------------------------------------------
title: "How to set a Content Security Policy (CSP) for your Next.js application"
description: "Learn how to set a Content Security Policy (CSP) for your Next.js application."
source: "https://nextjs.org/docs/pages/guides/content-security-policy"
--------------------------------------------------------------------------------

# Content Security Policy

@router: Pages Router

[Content Security Policy (CSP)](https://developer.mozilla.org/docs/Web/HTTP/CSP) is important to guard your Next.js application against various security threats such as cross-site scripting (XSS), clickjacking, and other code injection attacks.

By using CSP, developers can specify which origins are permissible for content sources, scripts, stylesheets, images, fonts, objects, media (audio, video), iframes, and more.

<details>
<summary>Examples</summary>

* [Strict CSP](https://github.com/vercel/next.js/tree/canary/examples/with-strict-csp)

</details>

## Nonces

A [nonce](https://developer.mozilla.org/docs/Web/HTML/Global_attributes/nonce) is a unique, random string of characters created for a one-time use. It is used in conjunction with CSP to selectively allow certain inline scripts or styles to execute, bypassing strict CSP directives.

### Why use a nonce?

CSP can block both inline and external scripts to prevent attacks. A nonce lets you safely allow specific scripts to run—only if they include the matching nonce value.

If an attacker wanted to load a script into your page, they'd need to guess the nonce value. That's why the nonce must be unpredictable and unique for every request.

### Adding a nonce with Proxy

[Proxy](/docs/app/api-reference/file-conventions/proxy.md) enables you to add headers and generate nonces before the page renders.

Every time a page is viewed, a fresh nonce should be generated. This means that you **must use [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering) to add nonces**.

For example:

```ts filename="proxy.ts" switcher
import { NextRequest, NextResponse } from 'next/server'

export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`
  // Replace newline characters and spaces
  const contentSecurityPolicyHeaderValue = cspHeader
    .replace(/\s{2,}/g, ' ')
    .trim()

  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)

  requestHeaders.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )

  const response = NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  })
  response.headers.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )

  return response
}
```

```js filename="proxy.js" switcher
import { NextResponse } from 'next/server'

export function proxy(request) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic';
    style-src 'self' 'nonce-${nonce}';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`
  // Replace newline characters and spaces
  const contentSecurityPolicyHeaderValue = cspHeader
    .replace(/\s{2,}/g, ' ')
    .trim()

  const requestHeaders = new Headers(request.headers)
  requestHeaders.set('x-nonce', nonce)
  requestHeaders.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )

  const response = NextResponse.next({
    request: {
      headers: requestHeaders,
    },
  })
  response.headers.set(
    'Content-Security-Policy',
    contentSecurityPolicyHeaderValue
  )

  return response
}
```

By default, Proxy runs on all requests. You can filter Proxy to run on specific paths using a [`matcher`](/docs/app/api-reference/file-conventions/proxy.md#matcher).

We recommend ignoring matching prefetches (from `next/link`) and static assets that don't need the CSP header.

```ts filename="proxy.ts" switcher
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    {
      source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },
  ],
}
```

```js filename="proxy.js" switcher
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    {
      source: '/((?!api|_next/static|_next/image|favicon.ico).*)',
      missing: [
        { type: 'header', key: 'next-router-prefetch' },
        { type: 'header', key: 'purpose', value: 'prefetch' },
      ],
    },
  ],
}
```

### How nonces work in Next.js

To use a nonce, your page must be **dynamically rendered**. This is because Next.js applies nonces during **server-side rendering**, based on the CSP header present in the request. Static pages are generated at build time, when no request or response headers exist—so no nonce can be injected.

Here’s how nonce support works in a dynamically rendered page:

1. **Proxy generates a nonce**: Your proxy creates a unique nonce for the request, adds it to your `Content-Security-Policy` header, and also sets it in a custom `x-nonce` header.
2. **Next.js extracts the nonce**: During rendering, Next.js parses the `Content-Security-Policy` header and extracts the nonce using the `'nonce-{value}'` pattern.
3. **Nonce is applied automatically**: Next.js attaches the nonce to:
   * Framework scripts (React, Next.js runtime)
   * Page-specific JavaScript bundles
   * Inline styles and scripts generated by Next.js
   * Any `<Script>` components using the `nonce` prop

Because of this automatic behavior, you don’t need to manually add a nonce to each tag.

### Forcing dynamic rendering

If you're using nonces, you may need to explicitly opt pages into dynamic rendering:

```tsx filename="app/page.tsx" switcher
import { connection } from 'next/server'

export default async function Page() {
  // wait for an incoming request to render this page
  await connection()
  // Your page content
}
```

```jsx filename="app/page.jsx" switcher
import { connection } from 'next/server'

export default async function Page() {
  // wait for an incoming request to render this page
  await connection()
  // Your page content
}
```

### Reading the nonce

You can provide the nonce to your page using
[`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md):

```tsx filename="pages/index.tsx" switcher
import Script from 'next/script'

import type { GetServerSideProps } from 'next'

export default function Page({ nonce }) {
  return (
    <Script
      src="https://www.googletagmanager.com/gtag/js"
      strategy="afterInteractive"
      nonce={nonce}
    />
  )
}

export const getServerSideProps: GetServerSideProps = async ({ req }) => {
  const nonce = req.headers['x-nonce']
  return { props: { nonce } }
}
```

```jsx filename="pages/index.jsx" switcher
import Script from 'next/script'
export default function Page({ nonce }) {
  return (
    <Script
      src="https://www.googletagmanager.com/gtag/js"
      strategy="afterInteractive"
      nonce={nonce}
    />
  )
}

export async function getServerSideProps({ req }) {
  const nonce = req.headers['x-nonce']
  return { props: { nonce } }
}
```

You can also access the nonce in `_document.tsx` for Pages Router applications:

```tsx filename="pages/_document.tsx" switcher
import Document, {
  Html,
  Head,
  Main,
  NextScript,
  DocumentContext,
  DocumentInitialProps,
} from 'next/document'

interface ExtendedDocumentProps extends DocumentInitialProps {
  nonce?: string
}

class MyDocument extends Document<ExtendedDocumentProps> {
  static async getInitialProps(
    ctx: DocumentContext
  ): Promise<ExtendedDocumentProps> {
    const initialProps = await Document.getInitialProps(ctx)
    const nonce = ctx.req?.headers?.['x-nonce'] as string | undefined

    return {
      ...initialProps,
      nonce,
    }
  }

  render() {
    const { nonce } = this.props

    return (
      <Html lang="en">
        <Head nonce={nonce} />
        <body>
          <Main />
          <NextScript nonce={nonce} />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

```jsx filename="pages/_document.jsx" switcher
import Document, { Html, Head, Main, NextScript } from 'next/document'

class MyDocument extends Document {
  static async getInitialProps(ctx) {
    const initialProps = await Document.getInitialProps(ctx)
    const nonce = ctx.req?.headers?.['x-nonce']

    return {
      ...initialProps,
      nonce,
    }
  }

  render() {
    const { nonce } = this.props

    return (
      <Html lang="en">
        <Head nonce={nonce} />
        <body>
          <Main />
          <NextScript nonce={nonce} />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

## Static vs Dynamic Rendering with CSP

Using nonces has important implications for how your Next.js application renders:

### Dynamic Rendering Requirement

When you use nonces in your CSP, **all pages must be dynamically rendered**. This means:

* Pages will build successfully but may encounter runtime errors if not properly configured for dynamic rendering
* Each request generates a fresh page with a new nonce
* Static optimization and Incremental Static Regeneration (ISR) are disabled
* Pages cannot be cached by CDNs without additional configuration
* **Partial Prerendering (PPR) is incompatible** with nonce-based CSP since static shell scripts won't have access to the nonce

### Performance Implications

The shift from static to dynamic rendering affects performance:

* **Slower initial page loads**: Pages must be generated on each request
* **Increased server load**: Every request requires server-side rendering
* **No CDN caching**: Dynamic pages cannot be cached at the edge by default
* **Higher hosting costs**: More server resources needed for dynamic rendering

### When to use nonces

Consider nonces when:

* You have strict security requirements that prohibit `'unsafe-inline'`
* Your application handles sensitive data
* You need to allow specific inline scripts while blocking others
* Compliance requirements mandate strict CSP

## Without Nonces

For applications that do not require nonces, you can set the CSP header directly in your [`next.config.js`](/docs/app/api-reference/config/next-config-js.md) file:

```js filename="next.config.js"
const cspHeader = `
    default-src 'self';
    script-src 'self' 'unsafe-eval' 'unsafe-inline';
    style-src 'self' 'unsafe-inline';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

module.exports = {
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'Content-Security-Policy',
            value: cspHeader.replace(/\n/g, ''),
          },
        ],
      },
    ]
  },
}
```

## Development vs Production Considerations

CSP implementation differs between development and production environments:

### Development Environment

In development, you will need to enable `'unsafe-eval'` to support APIs that provide additional debugging information:

```ts filename="proxy.ts" switcher
export function proxy(request: NextRequest) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const isDev = process.env.NODE_ENV === 'development'

  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${isDev ? "'unsafe-eval'" : ''};
    style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`};
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

  // Rest of proxy implementation
}
```

```js filename="proxy.js" switcher
export function proxy(request) {
  const nonce = Buffer.from(crypto.randomUUID()).toString('base64')
  const isDev = process.env.NODE_ENV === 'development'

  const cspHeader = `
    default-src 'self';
    script-src 'self' 'nonce-${nonce}' 'strict-dynamic' ${isDev ? "'unsafe-eval'" : ''};
    style-src 'self' ${isDev ? "'unsafe-inline'" : `'nonce-${nonce}'`};
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

  // Rest of proxy implementation
}
```

### Production Deployment

Common issues in production:

* **Nonce not applied**: Ensure your proxy runs on all necessary routes
* **Static assets blocked**: Verify your CSP allows Next.js static assets
* **Third-party scripts**: Add necessary domains to your CSP policy

## Troubleshooting

### Third-party Scripts

When using third-party scripts with CSP, ensure you add the necessary domains and pass the nonce:

```tsx filename="pages/_app.tsx" switcher
import type { AppProps } from 'next/app'
import Script from 'next/script'

export default function App({ Component, pageProps }: AppProps) {
  const nonce = pageProps.nonce

  return (
    <>
      <Component {...pageProps} />
      <Script
        src="https://www.googletagmanager.com/gtag/js"
        strategy="afterInteractive"
        nonce={nonce}
      />
    </>
  )
}
```

```jsx filename="pages/_app.jsx" switcher
import Script from 'next/script'

export default function App({ Component, pageProps }) {
  const nonce = pageProps.nonce

  return (
    <>
      <Component {...pageProps} />
      <Script
        src="https://www.googletagmanager.com/gtag/js"
        strategy="afterInteractive"
        nonce={nonce}
      />
    </>
  )
}
```

Update your CSP to allow third-party domains:

```ts filename="proxy.ts" switcher
const cspHeader = `
  default-src 'self';
  script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
  connect-src 'self' https://www.google-analytics.com;
  img-src 'self' data: https://www.google-analytics.com;
`
```

```js filename="proxy.js" switcher
const cspHeader = `
  default-src 'self';
  script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com;
  connect-src 'self' https://www.google-analytics.com;
  img-src 'self' data: https://www.google-analytics.com;
`
```

### Common CSP Violations

1. **Inline styles**: Use CSS-in-JS libraries that support nonces or move styles to external files
2. **Dynamic imports**: Ensure dynamic imports are allowed in your script-src policy
3. **WebAssembly**: Add `'wasm-unsafe-eval'` if using WebAssembly
4. **Service workers**: Add appropriate policies for service worker scripts

## Version History

| Version    | Changes                                                       |
| ---------- | ------------------------------------------------------------- |
| `v14.0.0`  | Experimental SRI support added for hash-based CSP             |
| `v13.4.20` | Recommended for proper nonce handling and CSP header parsing. |
- [proxy.js](/docs/app/api-reference/file-conventions/proxy.md)
  - API reference for the proxy.js file.
- [headers](/docs/app/api-reference/functions/headers.md)
  - API reference for the headers function.


--------------------------------------------------------------------------------
title: "How to use CSS-in-JS libraries"
description: "Use CSS-in-JS libraries with Next.js"
source: "https://nextjs.org/docs/pages/guides/css-in-js"
--------------------------------------------------------------------------------

# CSS-in-JS

@router: Pages Router

<details>
<summary>Examples</summary>

* [Styled JSX](https://github.com/vercel/next.js/tree/canary/examples/with-styled-jsx)
* [Styled Components](https://github.com/vercel/next.js/tree/canary/examples/with-styled-components)
* [Emotion](https://github.com/vercel/next.js/tree/canary/examples/with-emotion)
* [Linaria](https://github.com/vercel/next.js/tree/canary/examples/with-linaria)
* [Styletron](https://github.com/vercel/next.js/tree/canary/examples/with-styletron)
* [Cxs](https://github.com/vercel/next.js/tree/canary/examples/with-cxs)
* [Fela](https://github.com/vercel/next.js/tree/canary/examples/with-fela)
* [Stitches](https://github.com/vercel/next.js/tree/canary/examples/with-stitches)

</details>

It's possible to use any existing CSS-in-JS solution. The simplest one is inline styles:

```jsx
function HiThere() {
  return <p style={{ color: 'red' }}>hi there</p>
}

export default HiThere
```

We bundle [styled-jsx](https://github.com/vercel/styled-jsx) to provide support for isolated scoped CSS.
The aim is to support "shadow CSS" similar to Web Components, which unfortunately [do not support server-rendering and are JS-only](https://github.com/w3c/webcomponents/issues/71).

See the above examples for other popular CSS-in-JS solutions (like Styled Components).

A component using `styled-jsx` looks like this:

```jsx
function HelloWorld() {
  return (
    <div>
      Hello world
      <p>scoped!</p>
      <style jsx>{`
        p {
          color: blue;
        }
        div {
          background: red;
        }
        @media (max-width: 600px) {
          div {
            background: blue;
          }
        }
      `}</style>
      <style global jsx>{`
        body {
          background: black;
        }
      `}</style>
    </div>
  )
}

export default HelloWorld
```

Please see the [styled-jsx documentation](https://github.com/vercel/styled-jsx) for more examples.

### Disabling JavaScript

Yes, if you disable JavaScript the CSS will still be loaded in the production build (`next start`). During development, we require JavaScript to be enabled to provide the best developer experience with [Fast Refresh](https://nextjs.org/blog/next-9-4#fast-refresh).


--------------------------------------------------------------------------------
title: "How to set up a custom server in Next.js"
description: "Start a Next.js app programmatically using a custom server."
source: "https://nextjs.org/docs/pages/guides/custom-server"
--------------------------------------------------------------------------------

# Custom Server

@router: Pages Router

Next.js includes its own server with `next start` by default. If you have an existing backend, you can still use it with Next.js (this is not a custom server). A custom Next.js server allows you to programmatically start a server for custom patterns. The majority of the time, you will not need this approach. However, it's available if you need to eject.

> **Good to know**:
>
> * Before deciding to use a custom server, keep in mind that it should only be used when the integrated router of Next.js can't meet your app requirements. A custom server will remove important performance optimizations, like **[Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md).**
> * When using standalone output mode, it does not trace custom server files. This mode outputs a separate minimal `server.js` file, instead. These cannot be used together.

Take a look at the [following example](https://github.com/vercel/next.js/tree/canary/examples/custom-server) of a custom server:

```ts filename="server.ts" switcher
import { createServer } from 'http'
import { parse } from 'url'
import next from 'next'

const port = parseInt(process.env.PORT || '3000', 10)
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer((req, res) => {
    const parsedUrl = parse(req.url!, true)
    handle(req, res, parsedUrl)
  }).listen(port)

  console.log(
    `> Server listening at http://localhost:${port} as ${
      dev ? 'development' : process.env.NODE_ENV
    }`
  )
})
```

```js filename="server.js" switcher
import { createServer } from 'http'
import { parse } from 'url'
import next from 'next'

const port = parseInt(process.env.PORT || '3000', 10)
const dev = process.env.NODE_ENV !== 'production'
const app = next({ dev })
const handle = app.getRequestHandler()

app.prepare().then(() => {
  createServer((req, res) => {
    const parsedUrl = parse(req.url, true)
    handle(req, res, parsedUrl)
  }).listen(port)

  console.log(
    `> Server listening at http://localhost:${port} as ${
      dev ? 'development' : process.env.NODE_ENV
    }`
  )
})
```

> `server.js` does not run through the Next.js Compiler or bundling process. Make sure the syntax and source code this file requires are compatible with the current Node.js version you are using. [View an example](https://github.com/vercel/next.js/tree/canary/examples/custom-server).

To run the custom server, you'll need to update the `scripts` in `package.json` like so:

```json filename="package.json"
{
  "scripts": {
    "dev": "node server.js",
    "build": "next build",
    "start": "NODE_ENV=production node server.js"
  }
}
```

Alternatively, you can set up `nodemon` ([example](https://github.com/vercel/next.js/tree/canary/examples/custom-server)). The custom server uses the following import to connect the server with the Next.js application:

```js
import next from 'next'

const app = next({})
```

The above `next` import is a function that receives an object with the following options:

| Option       | Type               | Description                                                                         |
| ------------ | ------------------ | ----------------------------------------------------------------------------------- |
| `conf`       | `Object`           | The same object you would use in `next.config.js`. Defaults to `{}`                 |
| `dev`        | `Boolean`          | (*Optional*) Whether or not to launch Next.js in dev mode. Defaults to `false`      |
| `dir`        | `String`           | (*Optional*) Location of the Next.js project. Defaults to `'.'`                     |
| `quiet`      | `Boolean`          | (*Optional*) Hide error messages containing server information. Defaults to `false` |
| `hostname`   | `String`           | (*Optional*) The hostname the server is running behind                              |
| `port`       | `Number`           | (*Optional*) The port the server is running behind                                  |
| `httpServer` | `node:http#Server` | (*Optional*) The HTTP Server that Next.js is running behind                         |
| `turbopack`  | `Boolean`          | (*Optional*) Enable Turbopack (enabled by default)                                  |
| `webpack`    | `Boolean`          | (*Optional*) Enable webpack                                                         |

The returned `app` can then be used to let Next.js handle requests as required.

## Disabling file-system routing

By default, `Next` will serve each file in the `pages` folder under a pathname matching the filename. If your project uses a custom server, this behavior may result in the same content being served from multiple paths, which can present problems with SEO and UX.

To disable this behavior and prevent routing based on files in `pages`, open `next.config.js` and disable the `useFileSystemPublicRoutes` config:

```js filename="next.config.js"
module.exports = {
  useFileSystemPublicRoutes: false,
}
```

> Note that `useFileSystemPublicRoutes` disables filename routes from SSR; client-side routing may still access those paths. When using this option, you should guard against navigation to routes you do not want programmatically.

> You may also wish to configure the client-side router to disallow client-side redirects to filename routes; for that refer to [`router.beforePopState`](/docs/pages/api-reference/functions/use-router.md#routerbeforepopstate).


--------------------------------------------------------------------------------
title: "How to use debugging tools with Next.js"
description: "Learn how to debug your Next.js application with VS Code, Chrome DevTools, or Firefox DevTools."
source: "https://nextjs.org/docs/pages/guides/debugging"
--------------------------------------------------------------------------------

# Debugging

@router: Pages Router

This documentation explains how you can debug your Next.js frontend and backend code with full source maps support using the [VS Code debugger](https://code.visualstudio.com/docs/editor/debugging), [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), or [Firefox DevTools](https://firefox-source-docs.mozilla.org/devtools-user/).

Any debugger that can attach to Node.js can also be used to debug a Next.js application. You can find more details in the Node.js [Debugging Guide](https://nodejs.org/en/docs/guides/debugging-getting-started/).

## Debugging with VS Code

Create a file named `.vscode/launch.json` at the root of your project with the following content:

```json filename="launch.json"
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Next.js: debug server-side",
      "type": "node-terminal",
      "request": "launch",
      "command": "npm run dev -- --inspect"
    },
    {
      "name": "Next.js: debug client-side",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:3000"
    },
    {
      "name": "Next.js: debug client-side (Firefox)",
      "type": "firefox",
      "request": "launch",
      "url": "http://localhost:3000",
      "reAttach": true,
      "pathMappings": [
        {
          "url": "webpack://_N_E",
          "path": "${workspaceFolder}"
        }
      ]
    },
    {
      "name": "Next.js: debug full stack",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/node_modules/next/dist/bin/next",
      "runtimeArgs": ["--inspect"],
      "skipFiles": ["<node_internals>/**"],
      "serverReadyAction": {
        "action": "debugWithEdge",
        "killOnServerStop": true,
        "pattern": "- Local:.+(https?://.+)",
        "uriFormat": "%s",
        "webRoot": "${workspaceFolder}"
      }
    }
  ]
}
```

> **Note**: To use Firefox debugging in VS Code, you'll need to install the [Firefox Debugger extension](https://marketplace.visualstudio.com/items?itemName=firefox-devtools.vscode-firefox-debug).

`npm run dev` can be replaced with `yarn dev` if you're using Yarn or `pnpm dev` if you're using pnpm.

In the "Next.js: debug full stack" configuration, `serverReadyAction.action` specifies which browser to open when the server is ready. `debugWithEdge` means to launch the Edge browser. If you are using Chrome, change this value to `debugWithChrome`.

If you're [changing the port number](/docs/pages/api-reference/cli/next.md#next-dev-options) your application starts on, replace the `3000` in `http://localhost:3000` with the port you're using instead.

If you're running Next.js from a directory other than root (for example, if you're using Turborepo) then you need to add `cwd` to the server-side and full stack debugging tasks. For example, `"cwd": "${workspaceFolder}/apps/web"`.

Now go to the Debug panel (`Ctrl+Shift+D` on Windows/Linux, `⇧+⌘+D` on macOS), select a launch configuration, then press `F5` or select **Debug: Start Debugging** from the Command Palette to start your debugging session.

## Using the Debugger in Jetbrains WebStorm

Click the drop down menu listing the runtime configuration, and click `Edit Configurations...`. Create a `JavaScript Debug` debug configuration with `http://localhost:3000` as the URL. Customize to your liking (e.g. Browser for debugging, store as project file), and click `OK`. Run this debug configuration, and the selected browser should automatically open. At this point, you should have 2 applications in debug mode: the NextJS node application, and the client/browser application.

## Debugging with Browser DevTools

### Client-side code

Start your development server as usual by running `next dev`, `npm run dev`, or `yarn dev`. Once the server starts, open `http://localhost:3000` (or your alternate URL) in your preferred browser.

For Chrome:

* Open Chrome's Developer Tools (`Ctrl+Shift+J` on Windows/Linux, `⌥+⌘+I` on macOS)
* Go to the **Sources** tab

For Firefox:

* Open Firefox's Developer Tools (`Ctrl+Shift+I` on Windows/Linux, `⌥+⌘+I` on macOS)
* Go to the **Debugger** tab

In either browser, any time your client-side code reaches a [`debugger`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/debugger) statement, code execution will pause and that file will appear in the debug area. You can also search for files to set breakpoints manually:

* In Chrome: Press `Ctrl+P` on Windows/Linux or `⌘+P` on macOS
* In Firefox: Press `Ctrl+P` on Windows/Linux or `⌘+P` on macOS, or use the file tree in the left panel

Note that when searching, your source files will have paths starting with `webpack://_N_E/./`.

### React Developer Tools

For React-specific debugging, install the [React Developer Tools](https://react.dev/learn/react-developer-tools) browser extension. This essential tool helps you:

* Inspect React components
* Edit props and state
* Identify performance problems

### Server-side code

To debug server-side Next.js code with browser DevTools, you need to pass the `--inspect` flag:

```bash filename="Terminal"
next dev --inspect
```

The value of `--inspect` is passed to the underlying Node.js process. Check out the [`--inspect` docs for advanced use cases](https://nodejs.org/api/cli.html#--inspecthostport).

> **Good to know**: Use `--inspect=0.0.0.0` to allow remote debugging access outside localhost, such as when running the app in a Docker container.

Launching the Next.js dev server with the `--inspect` flag will look something like this:

```bash filename="Terminal"
Debugger listening on ws://127.0.0.1:9229/0cf90313-350d-4466-a748-cd60f4e47c95
For help, see: https://nodejs.org/en/docs/inspector
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

For Chrome:

1. Open a new tab and visit `chrome://inspect`
2. Look for your Next.js application in the **Remote Target** section
3. Click **inspect** to open a separate DevTools window
4. Go to the **Sources** tab

For Firefox:

1. Open a new tab and visit `about:debugging`
2. Click **This Firefox** in the left sidebar
3. Under **Remote Targets**, find your Next.js application
4. Click **Inspect** to open the debugger
5. Go to the **Debugger** tab

Debugging server-side code works similarly to client-side debugging. When searching for files (`Ctrl+P`/`⌘+P`), your source files will have paths starting with `webpack://{application-name}/./` (where `{application-name}` will be replaced with the name of your application according to your `package.json` file).

To use `--inspect-brk` or `--inspect-wait`, you have to specify `NODE_OPTIONS` instead. e.g. `NODE_OPTIONS=--inspect-brk next dev`.

### Inspect Server Errors with Browser DevTools

When you encounter an error, inspecting the source code can help trace the root cause of errors.

Next.js will display a Node.js icon underneath the Next.js version indicator on the error overlay. By clicking that icon, the DevTools URL is copied to your clipboard. You can open a new browser tab with that URL to inspect the Next.js server process.

### Debugging on Windows

Ensure Windows Defender is disabled on your machine. This external service will check *every file read*, which has been reported to greatly increase Fast Refresh time with `next dev`. This is a known issue, not related to Next.js, but it does affect Next.js development.

## More information

To learn more about how to use a JavaScript debugger, take a look at the following documentation:

* [Node.js debugging in VS Code: Breakpoints](https://code.visualstudio.com/docs/nodejs/nodejs-debugging#_breakpoints)
* [Chrome DevTools: Debug JavaScript](https://developers.google.com/web/tools/chrome-devtools/javascript)
* [Firefox DevTools: Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/)


--------------------------------------------------------------------------------
title: "How to preview content with Draft Mode in Next.js"
description: "Next.js has draft mode to toggle between static and dynamic pages. You can learn how it works with Pages Router."
source: "https://nextjs.org/docs/pages/guides/draft-mode"
--------------------------------------------------------------------------------

# Draft Mode

@router: Pages Router

In the [Pages documentation](/docs/pages/building-your-application/routing/pages-and-layouts.md) and the [Data Fetching documentation](/docs/pages/building-your-application/data-fetching.md), we talked about how to pre-render a page at build time (**Static Generation**) using `getStaticProps` and `getStaticPaths`.

Static Generation is useful when your pages fetch data from a headless CMS. However, it’s not ideal when you’re writing a draft on your headless CMS and want to view the draft immediately on your page. You’d want Next.js to render these pages at **request time** instead of build time and fetch the draft content instead of the published content. You’d want Next.js to bypass Static Generation only for this specific case.

Next.js has a feature called **Draft Mode** which solves this problem. Here are instructions on how to use it.

## Step 1: Create and access the API route

> Take a look at the [API Routes documentation](/docs/pages/building-your-application/routing/api-routes.md) first if you’re not familiar with Next.js API Routes.

First, create the **API route**. It can have any name - e.g. `pages/api/draft.ts`

In this API route, you need to call `setDraftMode` on the response object.

```js
export default function handler(req, res) {
  // ...
  res.setDraftMode({ enable: true })
  // ...
}
```

This will set a **cookie** to enable draft mode. Subsequent requests containing this cookie will trigger **Draft Mode** changing the behavior for statically generated pages (more on this later).

You can test this manually by creating an API route like below and accessing it from your browser manually:

```ts filename="pages/api/draft.ts"
// simple example for testing it manually from your browser.
export default function handler(req, res) {
  res.setDraftMode({ enable: true })
  res.end('Draft mode is enabled')
}
```

If you open your browser’s developer tools and visit `/api/draft`, you’ll notice a `Set-Cookie` response header with a cookie named `__prerender_bypass`.

### Securely accessing it from your Headless CMS

In practice, you’d want to call this API route *securely* from your headless CMS. The specific steps will vary depending on which headless CMS you’re using, but here are some common steps you could take.

These steps assume that the headless CMS you’re using supports setting **custom draft URLs**. If it doesn’t, you can still use this method to secure your draft URLs, but you’ll need to construct and access the draft URL manually.

**First**, you should create a **secret token string** using a token generator of your choice. This secret will only be known by your Next.js app and your headless CMS. This secret prevents people who don’t have access to your CMS from accessing draft URLs.

**Second**, if your headless CMS supports setting custom draft URLs, specify the following as the draft URL. This assumes that your draft API route is located at `pages/api/draft.ts`.

```bash filename="Terminal"
https://<your-site>/api/draft?secret=<token>&slug=<path>
```

* `<your-site>` should be your deployment domain.
* `<token>` should be replaced with the secret token you generated.
* `<path>` should be the path for the page that you want to view. If you want to view `/posts/foo`, then you should use `&slug=/posts/foo`.

Your headless CMS might allow you to include a variable in the draft URL so that `<path>` can be set dynamically based on the CMS’s data like so: `&slug=/posts/{entry.fields.slug}`

**Finally**, in the draft API route:

* Check that the secret matches and that the `slug` parameter exists (if not, the request should fail).
*
* Call `res.setDraftMode`.
* Then redirect the browser to the path specified by `slug`. (The following example uses a [307 redirect](https://developer.mozilla.org/docs/Web/HTTP/Status/307)).

```js
export default async (req, res) => {
  // Check the secret and next parameters
  // This secret should only be known to this API route and the CMS
  if (req.query.secret !== 'MY_SECRET_TOKEN' || !req.query.slug) {
    return res.status(401).json({ message: 'Invalid token' })
  }

  // Fetch the headless CMS to check if the provided `slug` exists
  // getPostBySlug would implement the required fetching logic to the headless CMS
  const post = await getPostBySlug(req.query.slug)

  // If the slug doesn't exist prevent draft mode from being enabled
  if (!post) {
    return res.status(401).json({ message: 'Invalid slug' })
  }

  // Enable Draft Mode by setting the cookie
  res.setDraftMode({ enable: true })

  // Redirect to the path from the fetched post
  // We don't redirect to req.query.slug as that might lead to open redirect vulnerabilities
  res.redirect(post.slug)
}
```

If it succeeds, then the browser will be redirected to the path you want to view with the draft mode cookie.

## Step 2: Update `getStaticProps`

The next step is to update `getStaticProps` to support draft mode.

If you request a page which has `getStaticProps` with the cookie set (via `res.setDraftMode`), then `getStaticProps` will be called at **request time** (instead of at build time).

Furthermore, it will be called with a `context` object where `context.draftMode` will be `true`.

```js
export async function getStaticProps(context) {
  if (context.draftMode) {
    // dynamic data
  }
}
```

We used `res.setDraftMode` in the draft API route, so `context.draftMode` will be `true`.

If you’re also using `getStaticPaths`, then `context.params` will also be available.

### Fetch draft data

You can update `getStaticProps` to fetch different data based on `context.draftMode`.

For example, your headless CMS might have a different API endpoint for draft posts. If so, you can modify the API endpoint URL like below:

```js
export async function getStaticProps(context) {
  const url = context.draftMode
    ? 'https://draft.example.com'
    : 'https://production.example.com'
  const res = await fetch(url)
  // ...
}
```

That’s it! If you access the draft API route (with `secret` and `slug`) from your headless CMS or manually, you should now be able to see the draft content. And if you update your draft without publishing, you should be able to view the draft.

Set this as the draft URL on your headless CMS or access manually, and you should be able to see the draft.

```bash filename="Terminal"
https://<your-site>/api/draft?secret=<token>&slug=<path>
```

## More Details

### Clear the Draft Mode cookie

By default, the Draft Mode session ends when the browser is closed.

To clear the Draft Mode cookie manually, create an API route that calls `setDraftMode({ enable: false })`:

```ts filename="pages/api/disable-draft.ts"
export default function handler(req, res) {
  res.setDraftMode({ enable: false })
}
```

Then, send a request to `/api/disable-draft` to invoke the API Route. If calling this route using [`next/link`](/docs/pages/api-reference/components/link.md), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.

### Works with `getServerSideProps`

Draft Mode works with `getServerSideProps`, and is available as a `draftMode` key in the [`context`](/docs/pages/api-reference/functions/get-server-side-props.md#context-parameter) object.

> **Good to know**: You shouldn't set the `Cache-Control` header when using Draft Mode because it cannot be bypassed. Instead, we recommend using [ISR](/docs/pages/guides/incremental-static-regeneration.md).

### Works with API Routes

API Routes will have access to `draftMode` on the request object. For example:

```js
export default function myApiRoute(req, res) {
  if (req.draftMode) {
    // get draft data
  }
}
```

### Unique per `next build`

A new bypass cookie value will be generated each time you run `next build`.

This ensures that the bypass cookie can’t be guessed.

> **Good to know**: To test Draft Mode locally over HTTP, your browser will need to allow third-party cookies and local storage access.


--------------------------------------------------------------------------------
title: "How to use environment variables in Next.js"
description: "Learn to add and access environment variables in your Next.js application."
source: "https://nextjs.org/docs/pages/guides/environment-variables"
--------------------------------------------------------------------------------

# Environment Variables

@router: Pages Router

Next.js comes with built-in support for environment variables, which allows you to do the following:

* [Use `.env` to load environment variables](#loading-environment-variables)
* [Bundle environment variables for the browser by prefixing with `NEXT_PUBLIC_`](#bundling-environment-variables-for-the-browser)

> **Warning:** The default `create-next-app` template ensures all `.env` files are added to your `.gitignore`. You almost never want to commit these files to your repository.

## Loading Environment Variables

Next.js has built-in support for loading environment variables from `.env*` files into `process.env`.

```txt filename=".env"
DB_HOST=localhost
DB_USER=myuser
DB_PASS=mypassword
```

This loads `process.env.DB_HOST`, `process.env.DB_USER`, and `process.env.DB_PASS` into the Node.js environment automatically allowing you to use them in [Next.js data fetching methods](/docs/pages/building-your-application/data-fetching.md) and [API routes](/docs/pages/building-your-application/routing/api-routes.md).

For example, using [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md):

```js filename="pages/index.js"
export async function getStaticProps() {
  const db = await myDB.connect({
    host: process.env.DB_HOST,
    username: process.env.DB_USER,
    password: process.env.DB_PASS,
  })
  // ...
}
```

### Loading Environment Variables with `@next/env`

If you need to load environment variables outside of the Next.js runtime, such as in a root config file for an ORM or test runner, you can use the `@next/env` package.

This package is used internally by Next.js to load environment variables from `.env*` files.

To use it, install the package and use the `loadEnvConfig` function to load the environment variables:

```bash
npm install @next/env
```

```tsx filename="envConfig.ts" switcher
import { loadEnvConfig } from '@next/env'

const projectDir = process.cwd()
loadEnvConfig(projectDir)
```

```jsx filename="envConfig.js" switcher
import { loadEnvConfig } from '@next/env'

const projectDir = process.cwd()
loadEnvConfig(projectDir)
```

Then, you can import the configuration where needed. For example:

```tsx filename="orm.config.ts" switcher
import './envConfig.ts'

export default defineConfig({
  dbCredentials: {
    connectionString: process.env.DATABASE_URL!,
  },
})
```

```jsx filename="orm.config.js" switcher
import './envConfig.js'

export default defineConfig({
  dbCredentials: {
    connectionString: process.env.DATABASE_URL,
  },
})
```

### Referencing Other Variables

Next.js will automatically expand variables that use `$` to reference other variables e.g. `$VARIABLE` inside of your `.env*` files. This allows you to reference other secrets. For example:

```txt filename=".env"
TWITTER_USER=nextjs
TWITTER_URL=https://x.com/$TWITTER_USER
```

In the above example, `process.env.TWITTER_URL` would be set to `https://x.com/nextjs`.

> **Good to know**: If you need to use variable with a `$` in the actual value, it needs to be escaped e.g. `\$`.

## Bundling Environment Variables for the Browser

Non-`NEXT_PUBLIC_` environment variables are only available in the Node.js environment, meaning they aren't accessible to the browser (the client runs in a different *environment*).

In order to make the value of an environment variable accessible in the browser, Next.js can "inline" a value, at build time, into the js bundle that is delivered to the client, replacing all references to `process.env.[variable]` with a hard-coded value. To tell it to do this, you just have to prefix the variable with `NEXT_PUBLIC_`. For example:

```txt filename="Terminal"
NEXT_PUBLIC_ANALYTICS_ID=abcdefghijk
```

This will tell Next.js to replace all references to `process.env.NEXT_PUBLIC_ANALYTICS_ID` in the Node.js environment with the value from the environment in which you run `next build`, allowing you to use it anywhere in your code. It will be inlined into any JavaScript sent to the browser.

> **Note**: After being built, your app will no longer respond to changes to these environment variables. For instance, if you use a Heroku pipeline to promote slugs built in one environment to another environment, or if you build and deploy a single Docker image to multiple environments, all `NEXT_PUBLIC_` variables will be frozen with the value evaluated at build time, so these values need to be set appropriately when the project is built. If you need access to runtime environment values, you'll have to setup your own API to provide them to the client (either on demand or during initialization).

```js filename="pages/index.js"
import setupAnalyticsService from '../lib/my-analytics-service'

// 'NEXT_PUBLIC_ANALYTICS_ID' can be used here as it's prefixed by 'NEXT_PUBLIC_'.
// It will be transformed at build time to `setupAnalyticsService('abcdefghijk')`.
setupAnalyticsService(process.env.NEXT_PUBLIC_ANALYTICS_ID)

function HomePage() {
  return <h1>Hello World</h1>
}

export default HomePage
```

Note that dynamic lookups will *not* be inlined, such as:

```js
// This will NOT be inlined, because it uses a variable
const varName = 'NEXT_PUBLIC_ANALYTICS_ID'
setupAnalyticsService(process.env[varName])

// This will NOT be inlined, because it uses a variable
const env = process.env
setupAnalyticsService(env.NEXT_PUBLIC_ANALYTICS_ID)
```

### Runtime Environment Variables

Next.js can support both build time and runtime environment variables.

**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.

To read runtime environment variables, we recommend using `getServerSideProps` or [incrementally adopting the App Router](/docs/app/guides/migrating/app-router-migration.md).

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.

**Good to know:**

* You can run code on server startup using the [`register` function](/docs/app/guides/instrumentation.md).

## Test Environment Variables

Apart from `development` and `production` environments, there is a 3rd option available: `test`. In the same way you can set defaults for development or production environments, you can do the same with a `.env.test` file for the `testing` environment (though this one is not as common as the previous two). Next.js will not load environment variables from `.env.development` or `.env.production` in the `testing` environment.

This one is useful when running tests with tools like `jest` or `cypress` where you need to set specific environment vars only for testing purposes. Test default values will be loaded if `NODE_ENV` is set to `test`, though you usually don't need to do this manually as testing tools will address it for you.

There is a small difference between `test` environment, and both `development` and `production` that you need to bear in mind: `.env.local` won't be loaded, as you expect tests to produce the same results for everyone. This way every test execution will use the same env defaults across different executions by ignoring your `.env.local` (which is intended to override the default set).

> **Good to know**: similar to Default Environment Variables, `.env.test` file should be included in your repository, but `.env.test.local` shouldn't, as `.env*.local` are intended to be ignored through `.gitignore`.

While running unit tests you can make sure to load your environment variables the same way Next.js does by leveraging the `loadEnvConfig` function from the `@next/env` package.

```js
// The below can be used in a Jest global setup file or similar for your testing set-up
import { loadEnvConfig } from '@next/env'

export default async () => {
  const projectDir = process.cwd()
  loadEnvConfig(projectDir)
}
```

## Environment Variable Load Order

Environment variables are looked up in the following places, in order, stopping once the variable is found.

1. `process.env`
2. `.env.$(NODE_ENV).local`
3. `.env.local` (Not checked when `NODE_ENV` is `test`.)
4. `.env.$(NODE_ENV)`
5. `.env`

For example, if `NODE_ENV` is `development` and you define a variable in both `.env.development.local` and `.env`, the value in `.env.development.local` will be used.

> **Good to know**: The allowed values for `NODE_ENV` are `production`, `development` and `test`.

## Good to know

* If you are using a [`/src` directory](/docs/app/api-reference/file-conventions/src-folder.md), `.env.*` files should remain in the root of your project.
* If the environment variable `NODE_ENV` is unassigned, Next.js automatically assigns `development` when running the `next dev` command, or `production` for all other commands.

## Version History

| Version  | Changes                                       |
| -------- | --------------------------------------------- |
| `v9.4.0` | Support `.env` and `NEXT_PUBLIC_` introduced. |


--------------------------------------------------------------------------------
title: "How to create forms with API Routes"
description: "Learn how to handle form submissions and data mutations with Next.js."
source: "https://nextjs.org/docs/pages/guides/forms"
--------------------------------------------------------------------------------

# Forms

@router: Pages Router

Forms enable you to create and update data in web applications. Next.js provides a powerful way to handle data mutations using **API Routes**. This guide will walk you through how to handle form submission on the server.

## Server Forms

To handle form submissions on the server, create an API endpoint that securely mutates data.

```ts filename="pages/api/submit.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const data = req.body
  const id = await createItem(data)
  res.status(200).json({ id })
}
```

```js filename="pages/api/submit.js" switcher
export default function handler(req, res) {
  const data = req.body
  // call your database, etc.
  // const id = await createItem(data)
  // ...
  res.status(200).json({ data })
}
```

Then, call the API Route from the client with an event handler:

```tsx filename="pages/index.tsx" switcher
import { FormEvent } from 'react'

export default function Page() {
  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const formData = new FormData(event.currentTarget)
    const response = await fetch('/api/submit', {
      method: 'POST',
      body: formData,
    })

    // Handle response if necessary
    const data = await response.json()
    // ...
  }

  return (
    <form onSubmit={onSubmit}>
      <input type="text" name="name" />
      <button type="submit">Submit</button>
    </form>
  )
}
```

```jsx filename="pages/index.jsx" switcher
export default function Page() {
  async function onSubmit(event) {
    event.preventDefault()

    const formData = new FormData(event.target)
    const response = await fetch('/api/submit', {
      method: 'POST',
      body: formData,
    })

    // Handle response if necessary
    const data = await response.json()
    // ...
  }

  return (
    <form onSubmit={onSubmit}>
      <input type="text" name="name" />
      <button type="submit">Submit</button>
    </form>
  )
}
```

> **Good to know:**
>
> * API Routes [do not specify CORS headers](https://developer.mozilla.org/docs/Web/HTTP/CORS), meaning they are same-origin only by default.
> * Since API Routes run on the server, we're able to use sensitive values (like API keys) through [Environment Variables](/docs/pages/guides/environment-variables.md) without exposing them to the client. This is critical for the security of your application.

## Form validation

We recommend using HTML validation like `required` and `type="email"` for basic client-side form validation.

For more advanced server-side validation, you can use a schema validation library like [zod](https://zod.dev/) to validate the form fields before mutating the data:

```ts filename="pages/api/submit.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'
import { z } from 'zod'

const schema = z.object({
  // ...
})

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const parsed = schema.parse(req.body)
  // ...
}
```

```js filename="pages/api/submit.js" switcher
import { z } from 'zod'

const schema = z.object({
  // ...
})

export default async function handler(req, res) {
  const parsed = schema.parse(req.body)
  // ...
}
```

### Error handling

You can use React state to show an error message when a form submission fails:

```tsx filename="pages/index.tsx" switcher
import React, { useState, FormEvent } from 'react'

export default function Page() {
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsLoading(true)
    setError(null) // Clear previous errors when a new request starts

    try {
      const formData = new FormData(event.currentTarget)
      const response = await fetch('/api/submit', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Failed to submit the data. Please try again.')
      }

      // Handle response if necessary
      const data = await response.json()
      // ...
    } catch (error) {
      // Capture the error message to display to the user
      setError(error.message)
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <form onSubmit={onSubmit}>
        <input type="text" name="name" />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Submit'}
        </button>
      </form>
    </div>
  )
}
```

```jsx filename="pages/index.jsx" switcher
import React, { useState } from 'react'

export default function Page() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  async function onSubmit(event) {
    event.preventDefault()
    setIsLoading(true)
    setError(null) // Clear previous errors when a new request starts

    try {
      const formData = new FormData(event.currentTarget)
      const response = await fetch('/api/submit', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Failed to submit the data. Please try again.')
      }

      // Handle response if necessary
      const data = await response.json()
      // ...
    } catch (error) {
      // Capture the error message to display to the user
      setError(error.message)
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div>
      {error && <div style={{ color: 'red' }}>{error}</div>}
      <form onSubmit={onSubmit}>
        <input type="text" name="name" />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Submit'}
        </button>
      </form>
    </div>
  )
}
```

## Displaying loading state

You can use React state to show a loading state when a form is submitting on the server:

```tsx filename="pages/index.tsx" switcher
import React, { useState, FormEvent } from 'react'

export default function Page() {
  const [isLoading, setIsLoading] = useState<boolean>(false)

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setIsLoading(true) // Set loading to true when the request starts

    try {
      const formData = new FormData(event.currentTarget)
      const response = await fetch('/api/submit', {
        method: 'POST',
        body: formData,
      })

      // Handle response if necessary
      const data = await response.json()
      // ...
    } catch (error) {
      // Handle error if necessary
      console.error(error)
    } finally {
      setIsLoading(false) // Set loading to false when the request completes
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <input type="text" name="name" />
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Loading...' : 'Submit'}
      </button>
    </form>
  )
}
```

```jsx filename="pages/index.jsx" switcher
import React, { useState } from 'react'

export default function Page() {
  const [isLoading, setIsLoading] = useState(false)

  async function onSubmit(event) {
    event.preventDefault()
    setIsLoading(true) // Set loading to true when the request starts

    try {
      const formData = new FormData(event.currentTarget)
      const response = await fetch('/api/submit', {
        method: 'POST',
        body: formData,
      })

      // Handle response if necessary
      const data = await response.json()
      // ...
    } catch (error) {
      // Handle error if necessary
      console.error(error)
    } finally {
      setIsLoading(false) // Set loading to false when the request completes
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <input type="text" name="name" />
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Loading...' : 'Submit'}
      </button>
    </form>
  )
}
```

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


--------------------------------------------------------------------------------
title: "How to implement Incremental Static Regeneration (ISR)"
description: "Learn how to create or update static pages at runtime with Incremental Static Regeneration."
source: "https://nextjs.org/docs/pages/guides/incremental-static-regeneration"
--------------------------------------------------------------------------------

# ISR

@router: Pages Router

<details>
<summary>Examples</summary>

* [Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce)
* [On-Demand ISR](https://on-demand-isr.vercel.app)
* [Next.js Forms](https://github.com/vercel/next.js/tree/canary/examples/next-forms)

</details>

Incremental Static Regeneration (ISR) enables you to:

* Update static content without rebuilding the entire site
* Reduce server load by serving prerendered, static pages for most requests
* Ensure proper `cache-control` headers are automatically added to pages
* Handle large amounts of content pages without long `next build` times

Here's a minimal example:

```tsx filename="pages/blog/[id].tsx" switcher
import type { GetStaticPaths, GetStaticProps } from 'next'

interface Post {
  id: string
  title: string
  content: string
}

interface Props {
  post: Post
}

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  const paths = posts.map((post: Post) => ({
    params: { id: String(post.id) },
  }))

  return { paths, fallback: 'blocking' }
}

export const getStaticProps: GetStaticProps<Props> = async ({
  params,
}: {
  params: { id: string }
}) => {
  const post = await fetch(`https://api.vercel.app/blog/${params.id}`).then(
    (res) => res.json()
  )

  return {
    props: { post },
    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    revalidate: 60,
  }
}

export default function Page({ post }: Props) {
  return (
    <main>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </main>
  )
}
```

```jsx filename="pages/blog/[id].jsx" switcher
export async function getStaticPaths() {
  const posts = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  const paths = posts.map((post) => ({
    params: { id: post.id },
  }))

  return { paths, fallback: 'blocking' }
}

export async function getStaticProps({ params }) {
  const post = await fetch(`https://api.vercel.app/blog/${params.id}`).then(
    (res) => res.json()
  )

  return {
    props: { post },
    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    revalidate: 60,
  }
}

export default function Page({ post }) {
  return (
    <main>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </main>
  )
}
```

Here's how this example works:

1. During `next build`, all known blog posts are generated
2. All requests made to these pages (e.g. `/blog/1`) are cached and instantaneous
3. After 60 seconds has passed, the next request will still return the cached (now stale) page
4. The cache is invalidated and a new version of the page begins generating in the background
5. Once generated successfully, the next request will return the updated page and cache it for subsequent requests
6. If `/blog/26` is requested, and it exists, the page will be generated on-demand. This behavior can be changed by using a different [fallback](/docs/pages/api-reference/functions/get-static-paths.md#fallback-false) value. However, if the post does not exist, then 404 is returned.

## Reference

### Functions

* [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md)
* [`res.revalidate`](/docs/pages/building-your-application/routing/api-routes.md#response-helpers)

## Examples

### On-demand validation with `res.revalidate()`

For a more precise method of revalidation, use `res.revalidate` to generate a new page on-demand from an API Router.

For example, this API Route can be called at `/api/revalidate?secret=<token>` to revalidate a given blog post. Create a secret token only known by your Next.js app. This secret will be used to prevent unauthorized access to the revalidation API Route.

```ts filename="pages/api/revalidate.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  // Check for secret to confirm this is a valid request
  if (req.query.secret !== process.env.MY_SECRET_TOKEN) {
    return res.status(401).json({ message: 'Invalid token' })
  }

  try {
    // This should be the actual path not a rewritten path
    // e.g. for "/posts/[id]" this should be "/posts/1"
    await res.revalidate('/posts/1')
    return res.json({ revalidated: true })
  } catch (err) {
    // If there was an error, Next.js will continue
    // to show the last successfully generated page
    return res.status(500).send('Error revalidating')
  }
}
```

```js filename="pages/api/revalidate.js" switcher
export default async function handler(req, res) {
  // Check for secret to confirm this is a valid request
  if (req.query.secret !== process.env.MY_SECRET_TOKEN) {
    return res.status(401).json({ message: 'Invalid token' })
  }

  try {
    // This should be the actual path not a rewritten path
    // e.g. for "/posts/[id]" this should be "/posts/1"
    await res.revalidate('/posts/1')
    return res.json({ revalidated: true })
  } catch (err) {
    // If there was an error, Next.js will continue
    // to show the last successfully generated page
    return res.status(500).send('Error revalidating')
  }
}
```

If you are using on-demand revalidation, you do not need to specify a `revalidate` time inside of `getStaticProps`. Next.js will use the default value of `false` (no revalidation) and only revalidate the page on-demand when `res.revalidate()` is called.

### Handling uncaught exceptions

If there is an error inside `getStaticProps` when handling background regeneration, or you manually throw an error, the last successfully generated page will continue to show. On the next subsequent request, Next.js will retry calling `getStaticProps`.

```tsx filename="pages/blog/[id].tsx" switcher
import type { GetStaticProps } from 'next'

interface Post {
  id: string
  title: string
  content: string
}

interface Props {
  post: Post
}

export const getStaticProps: GetStaticProps<Props> = async ({
  params,
}: {
  params: { id: string }
}) => {
  // If this request throws an uncaught error, Next.js will
  // not invalidate the currently shown page and
  // retry getStaticProps on the next request.
  const res = await fetch(`https://api.vercel.app/blog/${params.id}`)
  const post: Post = await res.json()

  if (!res.ok) {
    // If there is a server error, you might want to
    // throw an error instead of returning so that the cache is not updated
    // until the next successful request.
    throw new Error(`Failed to fetch posts, received status ${res.status}`)
  }

  return {
    props: { post },
    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    revalidate: 60,
  }
}
```

```jsx filename="pages/blog/[id].jsx" switcher
export async function getStaticProps({ params }) {
  // If this request throws an uncaught error, Next.js will
  // not invalidate the currently shown page and
  // retry getStaticProps on the next request.
  const res = await fetch(`https://api.vercel.app/blog/${params.id}`)
  const post = await res.json()

  if (!res.ok) {
    // If there is a server error, you might want to
    // throw an error instead of returning so that the cache is not updated
    // until the next successful request.
    throw new Error(`Failed to fetch posts, received status ${res.status}`)
  }

  return {
    props: { post },
    // Next.js will invalidate the cache when a
    // request comes in, at most once every 60 seconds.
    revalidate: 60,
  }
}
```

### Customizing the cache location

You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application. [Learn more](/docs/app/guides/self-hosting.md#caching-and-isr).

## Troubleshooting

### Debugging cached data in local development

If you are using the `fetch` API, you can add additional logging to understand which requests are cached or uncached. [Learn more about the `logging` option](/docs/app/api-reference/config/next-config-js/logging.md).

```jsx filename="next.config.js"
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

### Verifying correct production behavior

To verify your pages are cached and revalidated correctly in production, you can test locally by running `next build` and then `next start` to run the production Next.js server.

This will allow you to test ISR behavior as it would work in a production environment. For further debugging, add the following environment variable to your `.env` file:

```bash filename=".env"
NEXT_PRIVATE_DEBUG_CACHE=1
```

This will make the Next.js server console log ISR cache hits and misses. You can inspect the output to see which pages are generated during `next build`, as well as how pages are updated as paths are accessed on-demand.

## Caveats

* ISR is only supported when using the Node.js runtime (default).
* ISR is not supported when creating a [Static Export](/docs/app/guides/static-exports.md).
* Proxy won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Proxy will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.

## Platform Support

| Deployment Option                                                   | Supported         |
| ------------------------------------------------------------------- | ----------------- |
| [Node.js server](/docs/app/getting-started/deploying.md#nodejs-server) | Yes               |
| [Docker container](/docs/app/getting-started/deploying.md#docker)      | Yes               |
| [Static export](/docs/app/getting-started/deploying.md#static-export)  | No                |
| [Adapters](/docs/app/getting-started/deploying.md#adapters)            | Platform-specific |

Learn how to [configure ISR](/docs/app/guides/self-hosting.md#caching-and-isr) when self-hosting Next.js.

## Version history

| Version   | Changes                                                                             |
| --------- | ----------------------------------------------------------------------------------- |
| `v14.1.0` | Custom `cacheHandler` is stable.                                                    |
| `v13.0.0` | App Router is introduced.                                                           |
| `v12.2.0` | Pages Router: On-Demand ISR is stable                                               |
| `v12.0.0` | Pages Router: [Bot-aware ISR fallback](/blog/next-12#bot-aware-isr-fallback) added. |
| `v9.5.0`  | Pages Router: [Stable ISR introduced](/blog/next-9-5).                              |


--------------------------------------------------------------------------------
title: "How to set up instrumentation"
description: "Learn how to use instrumentation to run code at server startup in your Next.js app"
source: "https://nextjs.org/docs/pages/guides/instrumentation"
--------------------------------------------------------------------------------

# Instrumentation

@router: Pages Router

Instrumentation is the process of using code to integrate monitoring and logging tools into your application. This allows you to track the performance and behavior of your application, and to debug issues in production.

## Convention

To set up instrumentation, create `instrumentation.ts|js` file in the **root directory** of your project (or inside the [`src`](/docs/app/api-reference/file-conventions/src-folder.md) folder if using one).

Then, export a `register` function in the file. This function will be called **once** when a new Next.js server instance is initiated.

For example, to use Next.js with [OpenTelemetry](https://opentelemetry.io/) and [@vercel/otel](https://vercel.com/docs/observability/otel-overview):

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

See the [Next.js with OpenTelemetry example](https://github.com/vercel/next.js/tree/canary/examples/with-opentelemetry) for a complete implementation.

> **Good to know**:
>
> * The `instrumentation` file should be in the root of your project and not inside the `app` or `pages` directory. If you're using the `src` folder, then place the file inside `src` alongside `pages` and `app`.
> * If you use the [`pageExtensions` config option](/docs/app/api-reference/config/next-config-js/pageExtensions.md) to add a suffix, you will also need to update the `instrumentation` filename to match.

## Examples

### Importing files with side effects

Sometimes, it may be useful to import a file in your code because of the side effects it will cause. For example, you might import a file that defines a set of global variables, but never explicitly use the imported file in your code. You would still have access to the global variables the package has declared.

We recommend importing files using JavaScript `import` syntax within your `register` function. The following example demonstrates a basic usage of `import` in a `register` function:

```ts filename="instrumentation.ts" switcher
export async function register() {
  await import('package-with-side-effect')
}
```

```js filename="instrumentation.js" switcher
export async function register() {
  await import('package-with-side-effect')
}
```

> **Good to know:**
>
> We recommend importing the file from within the `register` function, rather than at the top of the file. By doing this, you can colocate all of your side effects in one place in your code, and avoid any unintended consequences from importing globally at the top of the file.

### Importing runtime-specific code

Next.js calls `register` in all environments, so it's important to conditionally import any code that doesn't support specific runtimes (e.g. [Edge or Node.js](/docs/app/api-reference/edge.md)). You can use the `NEXT_RUNTIME` environment variable to get the current environment:

```ts filename="instrumentation.ts" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation-node')
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./instrumentation-edge')
  }
}
```

```js filename="instrumentation.js" switcher
export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./instrumentation-node')
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./instrumentation-edge')
  }
}
```
## Learn more about Instrumentation- [instrumentation.js](/docs/app/api-reference/file-conventions/instrumentation.md)
  - API reference for the instrumentation.js file.


--------------------------------------------------------------------------------
title: "How to implement internationalization in Next.js"
description: "Next.js has built-in support for internationalized routing and language detection. Learn more here."
source: "https://nextjs.org/docs/pages/guides/internationalization"
--------------------------------------------------------------------------------

# Internationalization

@router: Pages Router

<details>
<summary>Examples</summary>

* [i18n routing](https://github.com/vercel/next.js/tree/canary/examples/i18n-routing-pages)

</details>

Next.js has built-in support for internationalized ([i18n](https://en.wikipedia.org/wiki/Internationalization_and_localization#Naming)) routing since `v10.0.0`. You can provide a list of locales, the default locale, and domain-specific locales and Next.js will automatically handle the routing.

The i18n routing support is currently meant to complement existing i18n library solutions like [`react-intl`](https://formatjs.io/docs/getting-started/installation), [`react-i18next`](https://react.i18next.com/), [`lingui`](https://lingui.dev/), [`rosetta`](https://github.com/lukeed/rosetta), [`next-intl`](https://github.com/amannn/next-intl), [`next-translate`](https://github.com/aralroca/next-translate), [`next-multilingual`](https://github.com/Avansai/next-multilingual), [`tolgee`](https://tolgee.io/integrations/next), [`paraglide-next`](https://inlang.com/m/osslbuzt/paraglide-next-i18n), [`next-intlayer`](https://intlayer.org/doc/environment/nextjs/next-with-page-router), [`gt-react`](https://generaltranslation.com/en/docs/react) and others by streamlining the routes and locale parsing.

## Getting started

To get started, add the `i18n` config to your `next.config.js` file.

Locales are [UTS Locale Identifiers](https://www.unicode.org/reports/tr35/tr35-59/tr35.html#Identifiers), a standardized format for defining locales.

Generally a Locale Identifier is made up of a language, region, and script separated by a dash: `language-region-script`. The region and script are optional. An example:

* `en-US` - English as spoken in the United States
* `nl-NL` - Dutch as spoken in the Netherlands
* `nl` - Dutch, no specific region

If user locale is `nl-BE` and it is not listed in your configuration, they will be redirected to `nl` if available, or to the default locale otherwise.
If you don't plan to support all regions of a country, it is therefore a good practice to include country locales that will act as fallbacks.

```js filename="next.config.js"
module.exports = {
  i18n: {
    // These are all the locales you want to support in
    // your application
    locales: ['en-US', 'fr', 'nl-NL'],
    // This is the default locale you want to be used when visiting
    // a non-locale prefixed path e.g. `/hello`
    defaultLocale: 'en-US',
    // This is a list of locale domains and the default locale they
    // should handle (these are only required when setting up domain routing)
    // Note: subdomains must be included in the domain value to be matched e.g. "fr.example.com".
    domains: [
      {
        domain: 'example.com',
        defaultLocale: 'en-US',
      },
      {
        domain: 'example.nl',
        defaultLocale: 'nl-NL',
      },
      {
        domain: 'example.fr',
        defaultLocale: 'fr',
        // an optional http field can also be used to test
        // locale domains locally with http instead of https
        http: true,
      },
    ],
  },
}
```

## Locale Strategies

There are two locale handling strategies: Sub-path Routing and Domain Routing.

### Sub-path Routing

Sub-path Routing puts the locale in the url path.

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['en-US', 'fr', 'nl-NL'],
    defaultLocale: 'en-US',
  },
}
```

With the above configuration `en-US`, `fr`, and `nl-NL` will be available to be routed to, and `en-US` is the default locale. If you have a `pages/blog.js` the following urls would be available:

* `/blog`
* `/fr/blog`
* `/nl-nl/blog`

The default locale does not have a prefix.

### Domain Routing

By using domain routing you can configure locales to be served from different domains:

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['en-US', 'fr', 'nl-NL', 'nl-BE'],
    defaultLocale: 'en-US',

    domains: [
      {
        // Note: subdomains must be included in the domain value to be matched
        // e.g. www.example.com should be used if that is the expected hostname
        domain: 'example.com',
        defaultLocale: 'en-US',
      },
      {
        domain: 'example.fr',
        defaultLocale: 'fr',
      },
      {
        domain: 'example.nl',
        defaultLocale: 'nl-NL',
        // specify other locales that should be redirected
        // to this domain
        locales: ['nl-BE'],
      },
    ],
  },
}
```

For example if you have `pages/blog.js` the following urls will be available:

* `example.com/blog`
* `www.example.com/blog`
* `example.fr/blog`
* `example.nl/blog`
* `example.nl/nl-BE/blog`

## Automatic Locale Detection

When a user visits the application root (generally `/`), Next.js will try to automatically detect which locale the user prefers based on the [`Accept-Language`](https://developer.mozilla.org/docs/Web/HTTP/Headers/Accept-Language) header and the current domain.

If a locale other than the default locale is detected, the user will be redirected to either:

* **When using Sub-path Routing:** The locale prefixed path
* **When using Domain Routing:** The domain with that locale specified as the default

When using Domain Routing, if a user with the `Accept-Language` header `fr;q=0.9` visits `example.com`, they will be redirected to `example.fr` since that domain handles the `fr` locale by default.

When using Sub-path Routing, the user would be redirected to `/fr`.

### Prefixing the Default Locale

With Next.js 12 and [Proxy](/docs/pages/api-reference/file-conventions/proxy.md), we can add a prefix to the default locale with a [workaround](https://github.com/vercel/next.js/discussions/18419).

For example, here's a `next.config.js` file with support for a few languages. Note the `"default"` locale has been added intentionally.

```js filename="next.config.js"
module.exports = {
  i18n: {
    locales: ['default', 'en', 'de', 'fr'],
    defaultLocale: 'default',
    localeDetection: false,
  },
  trailingSlash: true,
}
```

Next, we can use [Proxy](/docs/pages/api-reference/file-conventions/proxy.md) to add custom routing rules:

```ts filename="proxy.ts"
import { NextRequest, NextResponse } from 'next/server'

const PUBLIC_FILE = /\.(.*)$/

export async function proxy(req: NextRequest) {
  if (
    req.nextUrl.pathname.startsWith('/_next') ||
    req.nextUrl.pathname.includes('/api/') ||
    PUBLIC_FILE.test(req.nextUrl.pathname)
  ) {
    return
  }

  if (req.nextUrl.locale === 'default') {
    const locale = req.cookies.get('NEXT_LOCALE')?.value || 'en'

    return NextResponse.redirect(
      new URL(`/${locale}${req.nextUrl.pathname}${req.nextUrl.search}`, req.url)
    )
  }
}
```

This [Proxy](/docs/pages/api-reference/file-conventions/proxy.md) skips adding the default prefix to [API Routes](/docs/pages/building-your-application/routing/api-routes.md) and [public](/docs/pages/api-reference/file-conventions/public-folder.md) files like fonts or images. If a request is made to the default locale, we redirect to our prefix `/en`.

### Disabling Automatic Locale Detection

The automatic locale detection can be disabled with:

```js filename="next.config.js"
module.exports = {
  i18n: {
    localeDetection: false,
  },
}
```

When `localeDetection` is set to `false` Next.js will no longer automatically redirect based on the user's preferred locale and will only provide locale information detected from either the locale based domain or locale path as described above.

## Accessing the locale information

You can access the locale information via the Next.js router. For example, using the [`useRouter()`](/docs/pages/api-reference/functions/use-router.md) hook the following properties are available:

* `locale` contains the currently active locale.
* `locales` contains all configured locales.
* `defaultLocale` contains the configured default locale.

When [pre-rendering](/docs/pages/building-your-application/rendering/static-site-generation.md) pages with `getStaticProps` or `getServerSideProps`, the locale information is provided in [the context](/docs/pages/building-your-application/data-fetching/get-static-props.md) provided to the function.

When leveraging `getStaticPaths`, the configured locales are provided in the context parameter of the function under `locales` and the configured defaultLocale under `defaultLocale`.

## Transition between locales

You can use `next/link` or `next/router` to transition between locales.

For `next/link`, a `locale` prop can be provided to transition to a different locale from the currently active one. If no `locale` prop is provided, the currently active `locale` is used during client-transitions. For example:

```jsx
import Link from 'next/link'

export default function IndexPage(props) {
  return (
    <Link href="/another" locale="fr">
      To /fr/another
    </Link>
  )
}
```

When using the `next/router` methods directly, you can specify the `locale` that should be used via the transition options. For example:

```jsx
import { useRouter } from 'next/router'

export default function IndexPage(props) {
  const router = useRouter()

  return (
    <div
      onClick={() => {
        router.push('/another', '/another', { locale: 'fr' })
      }}
    >
      to /fr/another
    </div>
  )
}
```

Note that to handle switching only the `locale` while preserving all routing information such as [dynamic route](/docs/pages/building-your-application/routing/dynamic-routes.md) query values or hidden href query values, you can provide the `href` parameter as an object:

```jsx
import { useRouter } from 'next/router'
const router = useRouter()
const { pathname, asPath, query } = router
// change just the locale and maintain all other route information including href's query
router.push({ pathname, query }, asPath, { locale: nextLocale })
```

See [here](/docs/pages/api-reference/functions/use-router.md#with-url-object) for more information on the object structure for `router.push`.

If you have a `href` that already includes the locale you can opt-out of automatically handling the locale prefixing:

```jsx
import Link from 'next/link'

export default function IndexPage(props) {
  return (
    <Link href="/fr/another" locale={false}>
      To /fr/another
    </Link>
  )
}
```

## Leveraging the `NEXT_LOCALE` cookie

Next.js allows setting a `NEXT_LOCALE=the-locale` cookie, which takes priority over the accept-language header. This cookie can be set using a language switcher and then when a user comes back to the site it will leverage the locale specified in the cookie when redirecting from `/` to the correct locale location.

For example, if a user prefers the locale `fr` in their accept-language header but a `NEXT_LOCALE=en` cookie is set the `en` locale when visiting `/` the user will be redirected to the `en` locale location until the cookie is removed or expired.

## Search Engine Optimization

Since Next.js knows what language the user is visiting it will automatically add the `lang` attribute to the `<html>` tag.

Next.js doesn't know about variants of a page so it's up to you to add the `hreflang` meta tags using [`next/head`](/docs/pages/api-reference/components/head.md). You can learn more about `hreflang` in the [Google Webmasters documentation](https://support.google.com/webmasters/answer/189077).

## How does this work with Static Generation?

> Note that Internationalized Routing does not integrate with [`output: 'export'`](/docs/pages/guides/static-exports.md) as it does not leverage the Next.js routing layer. Hybrid Next.js applications that do not use `output: 'export'` are fully supported.

### Dynamic Routes and `getStaticProps` Pages

For pages using `getStaticProps` with [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md), all locale variants of the page desired to be prerendered need to be returned from [`getStaticPaths`](/docs/pages/building-your-application/data-fetching/get-static-paths.md). Along with the `params` object returned for `paths`, you can also return a `locale` field specifying which locale you want to render. For example:

```jsx filename="pages/blog/[slug].js"
export const getStaticPaths = ({ locales }) => {
  return {
    paths: [
      // if no `locale` is provided only the defaultLocale will be generated
      { params: { slug: 'post-1' }, locale: 'en-US' },
      { params: { slug: 'post-1' }, locale: 'fr' },
    ],
    fallback: true,
  }
}
```

For [Automatically Statically Optimized](/docs/pages/building-your-application/rendering/automatic-static-optimization.md) and non-dynamic `getStaticProps` pages, **a version of the page will be generated for each locale**. This is important to consider because it can increase build times depending on how many locales are configured inside `getStaticProps`.

For example, if you have 50 locales configured with 10 non-dynamic pages using `getStaticProps`, this means `getStaticProps` will be called 500 times. 50 versions of the 10 pages will be generated during each build.

To decrease the build time of dynamic pages with `getStaticProps`, use a [`fallback` mode](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true). This allows you to return only the most popular paths and locales from `getStaticPaths` for prerendering during the build. Then, Next.js will build the remaining pages at runtime as they are requested.

### Automatically Statically Optimized Pages

For pages that are [automatically statically optimized](/docs/pages/building-your-application/rendering/automatic-static-optimization.md), a version of the page will be generated for each locale.

### Non-dynamic getStaticProps Pages

For non-dynamic `getStaticProps` pages, a version is generated for each locale like above. `getStaticProps` is called with each `locale` that is being rendered. If you would like to opt-out of a certain locale from being pre-rendered, you can return `notFound: true` from `getStaticProps` and this variant of the page will not be generated.

```js
export async function getStaticProps({ locale }) {
  // Call an external API endpoint to get posts.
  // You can use any data fetching library
  const res = await fetch(`https://.../posts?locale=${locale}`)
  const posts = await res.json()

  if (posts.length === 0) {
    return {
      notFound: true,
    }
  }

  // By returning { props: posts }, the Blog component
  // will receive `posts` as a prop at build time
  return {
    props: {
      posts,
    },
  }
}
```

## Limits for the i18n config

* `locales`: 100 total locales
* `domains`: 100 total locale domain items

> **Good to know**: These limits have been added initially to prevent potential [performance issues at build time](#dynamic-routes-and-getstaticprops-pages). You can workaround these limits with custom routing using [Proxy](/docs/pages/api-reference/file-conventions/proxy.md) in Next.js 12.


--------------------------------------------------------------------------------
title: "How to lazy load Client Components and libraries"
description: "Lazy load imported libraries and React Components to improve your application's loading performance."
source: "https://nextjs.org/docs/pages/guides/lazy-loading"
--------------------------------------------------------------------------------

# Lazy Loading

@router: Pages Router

[Lazy loading](https://developer.mozilla.org/docs/Web/Performance/Lazy_loading) in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.

## `next/dynamic`

`next/dynamic` is a composite of [`React.lazy()`](https://react.dev/reference/react/lazy) and [Suspense](https://react.dev/reference/react/Suspense). It behaves the same way in the `app` and `pages` directories to allow for incremental migration.

In the example below, by using `next/dynamic`, the header component will not be included in the page's initial JavaScript bundle. The page will render the Suspense `fallback` first, followed by the `Header` component when the `Suspense` boundary is resolved.

```jsx
import dynamic from 'next/dynamic'

const DynamicHeader = dynamic(() => import('../components/header'), {
  loading: () => <p>Loading...</p>,
})

export default function Home() {
  return <DynamicHeader />
}
```

> **Good to know**: In `import('path/to/component')`, the path must be explicitly written. It can't be a template string nor a variable. Furthermore the `import()` has to be inside the `dynamic()` call for Next.js to be able to match webpack bundles / module ids to the specific `dynamic()` call and preload them before rendering. `dynamic()` can't be used inside of React rendering as it needs to be marked in the top level of the module for preloading to work, similar to `React.lazy`.

## Examples

### With named exports

To dynamically import a named export, you can return it from the [Promise](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) returned by [`import()`](https://github.com/tc39/proposal-dynamic-import#example):

```jsx filename="components/hello.js"
export function Hello() {
  return <p>Hello!</p>
}

// pages/index.js
import dynamic from 'next/dynamic'

const DynamicComponent = dynamic(() =>
  import('../components/hello').then((mod) => mod.Hello)
)
```

### With no SSR

To dynamically load a component on the client side, you can use the `ssr` option to disable server-rendering. This is useful if an external dependency or component relies on browser APIs like `window`.

```jsx
'use client'

import dynamic from 'next/dynamic'

const DynamicHeader = dynamic(() => import('../components/header'), {
  ssr: false,
})
```

### With external libraries

This example uses the external library `fuse.js` for fuzzy search. The module is only loaded in the browser after the user types in the search input.

```jsx
import { useState } from 'react'

const names = ['Tim', 'Joe', 'Bel', 'Lee']

export default function Page() {
  const [results, setResults] = useState()

  return (
    <div>
      <input
        type="text"
        placeholder="Search"
        onChange={async (e) => {
          const { value } = e.currentTarget
          // Dynamically load fuse.js
          const Fuse = (await import('fuse.js')).default
          const fuse = new Fuse(names)

          setResults(fuse.search(value))
        }}
      />
      <pre>Results: {JSON.stringify(results, null, 2)}</pre>
    </div>
  )
}
```


--------------------------------------------------------------------------------
title: "How to use markdown and MDX in Next.js"
description: "Learn how to configure MDX and use it in your Next.js apps."
source: "https://nextjs.org/docs/pages/guides/mdx"
--------------------------------------------------------------------------------

# MDX

@router: Pages Router

[Markdown](https://daringfireball.net/projects/markdown/syntax) is a lightweight markup language used to format text. It allows you to write using plain text syntax and convert it to structurally valid HTML. It's commonly used for writing content on websites and blogs.

You write...

```md
I **love** using [Next.js](https://nextjs.org/)
```

Output:

```html
<p>I <strong>love</strong> using <a href="https://nextjs.org/">Next.js</a></p>
```

[MDX](https://mdxjs.com/) is a superset of markdown that lets you write [JSX](https://react.dev/learn/writing-markup-with-jsx) directly in your markdown files. It is a powerful way to add dynamic interactivity and embed React components within your content.

Next.js can support both local MDX content inside your application, as well as remote MDX files fetched dynamically on the server. The Next.js plugin handles transforming markdown and React components into HTML, including support for usage in Server Components (the default in App Router).

> **Good to know**: View the [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) template for a complete working example.

## Install dependencies

The `@next/mdx` package, and related packages, are used to configure Next.js so it can process markdown and MDX. **It sources data from local files**, allowing you to create pages with a `.md` or `.mdx` extension, directly in your `/pages` or `/app` directory.

Install these packages to render MDX with Next.js:

```bash filename="Terminal"
npm install @next/mdx @mdx-js/loader @mdx-js/react @types/mdx
```

## Configure `next.config.mjs`

Update the `next.config.mjs` file at your project's root to configure it to use MDX:

```js filename="next.config.mjs"
import createMDX from '@next/mdx'

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Configure `pageExtensions` to include markdown and MDX files
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  // Optionally, add any other Next.js config below
}

const withMDX = createMDX({
  // Add markdown plugins here, as desired
})

// Merge MDX config with Next.js config
export default withMDX(nextConfig)
```

This allows `.mdx` files to act as pages, routes, or imports in your application.

### Handling `.md` files

By default, `next/mdx` only compiles files with the `.mdx` extension. To handle `.md` files with webpack, update the `extension` option:

```js filename="next.config.mjs"
const withMDX = createMDX({
  extension: /\.(md|mdx)$/,
})
```

## Add an `mdx-components.tsx` file

Create an `mdx-components.tsx` (or `.js`) file in the root of your project to define global MDX Components. For example, at the same level as `pages` or `app`, or inside `src` if applicable.

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

> **Good to know**:
>
> * `mdx-components.tsx` is **required** to use `@next/mdx` with App Router and will not work without it.
> * Learn more about the [`mdx-components.tsx` file convention](/docs/app/api-reference/file-conventions/mdx-components.md).
> * Learn how to [use custom styles and components](#using-custom-styles-and-components).

## Rendering MDX

You can render MDX using Next.js's file based routing or by importing MDX files into other pages.

### Using file based routing

When using file based routing, you can use MDX pages like any other page.

Create a new MDX page within the `/pages` directory:

```txt
  my-project
  |── mdx-components.(tsx/js)
  ├── pages
  │   └── mdx-page.(mdx/md)
  └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:

```mdx
import { MyComponent } from 'my-component'

# Welcome to my MDX page!

This is some **bold** and _italics_ text.

This is a list in markdown:

- One
- Two
- Three

Checkout my React component:

<MyComponent />
```

Navigating to the `/mdx-page` route should display your rendered MDX page.

### Using imports

Create a new page within the `/pages` directory and an MDX file wherever you'd like:

```txt
  .
  ├── markdown/
  │   └── welcome.(mdx/md)
  ├── pages/
  │   └── mdx-page.(tsx/js)
  ├── mdx-components.(tsx/js)
  └── package.json
```

You can use MDX in these files, and even import React components, directly inside your MDX page:

```mdx filename="markdown/welcome.mdx" switcher
import { MyComponent } from 'my-component'

# Welcome to my MDX page!

This is some **bold** and _italics_ text.

This is a list in markdown:

- One
- Two
- Three

Checkout my React component:

<MyComponent />
```

Import the MDX file inside the page to display the content:

```tsx filename="pages/mdx-page.tsx" switcher
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

```jsx filename="pages/mdx-page.js" switcher
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

Navigating to the `/mdx-page` route should display your rendered MDX page.

## Using custom styles and components

Markdown, when rendered, maps to native HTML elements. For example, writing the following markdown:

```md
## This is a heading

This is a list in markdown:

- One
- Two
- Three
```

Generates the following HTML:

```html
<h2>This is a heading</h2>

<p>This is a list in markdown:</p>

<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>
```

To style your markdown, you can provide custom components that map to the generated HTML elements. Styles and components can be implemented globally, locally, and with shared layouts.

### Global styles and components

Adding styles and components in `mdx-components.tsx` will affect *all* MDX files in your application.

```tsx filename="mdx-components.tsx" switcher
import type { MDXComponents } from 'mdx/types'
import Image, { ImageProps } from 'next/image'

// This file allows you to provide custom React components
// to be used in MDX files. You can import and use any
// React component you want, including inline styles,
// components from other libraries, and more.

const components = {
  // Allows customizing built-in components, e.g. to add styling.
  h1: ({ children }) => (
    <h1 style={{ color: 'red', fontSize: '48px' }}>{children}</h1>
  ),
  img: (props) => (
    <Image
      sizes="100vw"
      style={{ width: '100%', height: 'auto' }}
      {...(props as ImageProps)}
    />
  ),
} satisfies MDXComponents

export function useMDXComponents(): MDXComponents {
  return components
}
```

```js filename="mdx-components.js" switcher
import Image from 'next/image'

// This file allows you to provide custom React components
// to be used in MDX files. You can import and use any
// React component you want, including inline styles,
// components from other libraries, and more.

const components = {
  // Allows customizing built-in components, e.g. to add styling.
  h1: ({ children }) => (
    <h1 style={{ color: 'red', fontSize: '48px' }}>{children}</h1>
  ),
  img: (props) => (
    <Image sizes="100vw" style={{ width: '100%', height: 'auto' }} {...props} />
  ),
}

export function useMDXComponents() {
  return components
}
```

### Local styles and components

You can apply local styles and components to specific pages by passing them into imported MDX components. These will merge with and override [global styles and components](#global-styles-and-components).

```tsx filename="pages/mdx-page.tsx" switcher
import Welcome from '@/markdown/welcome.mdx'

function CustomH1({ children }) {
  return <h1 style={{ color: 'blue', fontSize: '100px' }}>{children}</h1>
}

const overrideComponents = {
  h1: CustomH1,
}

export default function Page() {
  return <Welcome components={overrideComponents} />
}
```

```jsx filename="pages/mdx-page.js" switcher
import Welcome from '@/markdown/welcome.mdx'

function CustomH1({ children }) {
  return <h1 style={{ color: 'blue', fontSize: '100px' }}>{children}</h1>
}

const overrideComponents = {
  h1: CustomH1,
}

export default function Page() {
  return <Welcome components={overrideComponents} />
}
```

### Shared layouts

To share a layout around MDX pages, create a layout component:

```tsx filename="components/mdx-layout.tsx" switcher
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return <div style={{ color: 'blue' }}>{children}</div>
}
```

```jsx filename="components/mdx-layout.js" switcher
export default function MdxLayout({ children }) {
  // Create any shared layout or styles here
  return <div style={{ color: 'blue' }}>{children}</div>
}
```

Then, import the layout component into the MDX page, wrap the MDX content in the layout, and export it:

```mdx
import MdxLayout from '../components/mdx-layout'

# Welcome to my MDX page!

export default function MDXPage({ children }) {
  return <MdxLayout>{children}</MdxLayout>

}
```

### Using Tailwind typography plugin

If you are using [Tailwind](https://tailwindcss.com) to style your application, using the [`@tailwindcss/typography` plugin](https://tailwindcss.com/docs/plugins#typography) will allow you to reuse your Tailwind configuration and styles in your markdown files.

The plugin adds a set of `prose` classes that can be used to add typographic styles to content blocks that come from sources, like markdown.

[Install Tailwind typography](https://github.com/tailwindlabs/tailwindcss-typography?tab=readme-ov-file#installation) and use with [shared layouts](#shared-layouts) to add the `prose` you want.

To share a layout around MDX pages, create a layout component:

```tsx filename="components/mdx-layout.tsx" switcher
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return (
    <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
      {children}
    </div>
  )
}
```

```jsx filename="components/mdx-layout.js" switcher
export default function MdxLayout({ children }) {
  // Create any shared layout or styles here
  return (
    <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
      {children}
    </div>
  )
}
```

Then, import the layout component into the MDX page, wrap the MDX content in the layout, and export it:

```mdx
import MdxLayout from '../components/mdx-layout'

# Welcome to my MDX page!

export default function MDXPage({ children }) {
  return <MdxLayout>{children}</MdxLayout>

}
```

## Frontmatter

Frontmatter is a YAML like key/value pairing that can be used to store data about a page. `@next/mdx` does **not** support frontmatter by default, though there are many solutions for adding frontmatter to your MDX content, such as:

* [remark-frontmatter](https://github.com/remarkjs/remark-frontmatter)
* [remark-mdx-frontmatter](https://github.com/remcohaszing/remark-mdx-frontmatter)
* [gray-matter](https://github.com/jonschlinkert/gray-matter)

`@next/mdx` **does** allow you to use exports like any other JavaScript component:

```mdx filename="content/blog-post.mdx" switcher
export const metadata = {
  author: 'John Doe',
}

# Blog post
```

Metadata can now be referenced outside of the MDX file:

```tsx filename="pages/blog.tsx" switcher
import BlogPost, { metadata } from '@/content/blog-post.mdx'

export default function Page() {
  console.log('metadata: ', metadata)
  //=> { author: 'John Doe' }
  return <BlogPost />
}
```

```jsx filename="pages/blog.js" switcher
import BlogPost, { metadata } from '@/content/blog-post.mdx'

export default function Page() {
  console.log('metadata: ', metadata)
  //=> { author: 'John Doe' }
  return <BlogPost />
}
```

A common use case for this is when you want to iterate over a collection of MDX and extract data. For example, creating a blog index page from all blog posts. You can use packages like [Node's `fs` module](https://nodejs.org/api/fs.html) or [globby](https://www.npmjs.com/package/globby) to read a directory of posts and extract the metadata.

> **Good to know**:
>
> * Using `fs`, `globby`, etc. can only be used server-side.
> * View the [Portfolio Starter Kit](https://vercel.com/templates/next.js/portfolio-starter-kit) template for a complete working example.

## remark and rehype Plugins

You can optionally provide remark and rehype plugins to transform the MDX content.

For example, you can use [`remark-gfm`](https://github.com/remarkjs/remark-gfm) to support GitHub Flavored Markdown.

Since the remark and rehype ecosystem is ESM only, you'll need to use `next.config.mjs` or `next.config.ts` as the configuration file.

```js filename="next.config.mjs"
import remarkGfm from 'remark-gfm'
import createMDX from '@next/mdx'

/** @type {import('next').NextConfig} */
const nextConfig = {
  // Allow .mdx extensions for files
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  // Optionally, add any other Next.js config below
}

const withMDX = createMDX({
  // Add markdown plugins here, as desired
  options: {
    remarkPlugins: [remarkGfm],
    rehypePlugins: [],
  },
})

// Combine MDX and Next.js config
export default withMDX(nextConfig)
```

### Using Plugins with Turbopack

To use plugins with [Turbopack](/docs/app/api-reference/turbopack.md), upgrade to the latest `@next/mdx` and specify plugin names using a string:

```js filename="next.config.mjs"
import createMDX from '@next/mdx'

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
}

const withMDX = createMDX({
  options: {
    remarkPlugins: [
      // Without options
      'remark-gfm',
      // With options
      ['remark-toc', { heading: 'The Table' }],
    ],
    rehypePlugins: [
      // Without options
      'rehype-slug',
      // With options
      ['rehype-katex', { strict: true, throwOnError: true }],
    ],
  },
})

export default withMDX(nextConfig)
```

> **Good to know**:
>
> remark and rehype plugins without serializable options cannot be used yet with [Turbopack](/docs/app/api-reference/turbopack.md), because JavaScript functions can't be passed to Rust.

## Remote MDX

If your MDX files or content lives *somewhere else*, you can fetch it dynamically on the server. This is useful for content stored in a CMS, database, or anywhere else. A community package for this use is [`next-mdx-remote-client`](https://github.com/ipikuka/next-mdx-remote-client?tab=readme-ov-file#the-part-associated-with-nextjs-app-router).

> **Good to know**: Please proceed with caution. MDX compiles to JavaScript and is executed on the server. You should only fetch MDX content from a trusted source, otherwise this can lead to remote code execution (RCE).

The following example uses `next-mdx-remote-client`:

```tsx filename="pages/mdx-page-remote.tsx" switcher
import {
  serialize,
  type SerializeResult,
} from 'next-mdx-remote-client/serialize'
import { MDXClient } from 'next-mdx-remote-client'

type Props = {
  mdxSource: SerializeResult
}

export default function RemoteMdxPage({ mdxSource }: Props) {
  if ('error' in mdxSource) {
    // either render error UI or throw `mdxSource.error`
  }
  return <MDXClient {...mdxSource} />
}

export async function getStaticProps() {
  // MDX text - can be from a database, CMS, fetch, anywhere...
  const res = await fetch('https:...')
  const mdxText = await res.text()
  const mdxSource = await serialize({ source: mdxText })
  return { props: { mdxSource } }
}
```

```jsx filename="pages/mdx-page-remote.js" switcher
import { serialize } from 'next-mdx-remote-client/serialize'
import { MDXClient } from 'next-mdx-remote-client'

export default function RemoteMdxPage({ mdxSource }) {
  if ('error' in mdxSource) {
    // either render error UI or throw `mdxSource.error`
  }
  return <MDXClient {...mdxSource} />
}

export async function getStaticProps() {
  // MDX text - can be from a database, CMS, fetch, anywhere...
  const res = await fetch('https:...')
  const mdxText = await res.text()
  const mdxSource = await serialize({ source: mdxText })
  return { props: { mdxSource } }
}
```

Navigating to the `/mdx-page-remote` route should display your rendered MDX.

## Deep Dive: How do you transform markdown into HTML?

React does not natively understand markdown. The markdown plaintext needs to first be transformed into HTML. This can be accomplished with `remark` and `rehype`.

`remark` is an ecosystem of tools around markdown. `rehype` is the same, but for HTML. For example, the following code snippet transforms markdown into HTML:

```js
import { unified } from 'unified'
import remarkParse from 'remark-parse'
import remarkRehype from 'remark-rehype'
import rehypeSanitize from 'rehype-sanitize'
import rehypeStringify from 'rehype-stringify'

main()

async function main() {
  const file = await unified()
    .use(remarkParse) // Convert into markdown AST
    .use(remarkRehype) // Transform to HTML AST
    .use(rehypeSanitize) // Sanitize HTML input
    .use(rehypeStringify) // Convert AST into serialized HTML
    .process('Hello, Next.js!')

  console.log(String(file)) // <p>Hello, Next.js!</p>
}
```

The `remark` and `rehype` ecosystem contains plugins for [syntax highlighting](https://github.com/atomiks/rehype-pretty-code), [linking headings](https://github.com/rehypejs/rehype-autolink-headings), [generating a table of contents](https://github.com/remarkjs/remark-toc), and more.

When using `@next/mdx` as shown above, you **do not** need to use `remark` or `rehype` directly, as it is handled for you. We're describing it here for a deeper understanding of what the `@next/mdx` package is doing underneath.

## Using the Rust-based MDX compiler (experimental)

Next.js supports a new MDX compiler written in Rust. This compiler is still experimental and is not recommended for production use. To use the new compiler, you need to configure `next.config.js` when you pass it to `withMDX`:

```js filename="next.config.js"
module.exports = withMDX({
  experimental: {
    mdxRs: true,
  },
})
```

`mdxRs` also accepts an object to configure how to transform mdx files.

```js filename="next.config.js"
module.exports = withMDX({
  experimental: {
    mdxRs: {
      jsxRuntime?: string            // Custom jsx runtime
      jsxImportSource?: string       // Custom jsx import source,
      mdxType?: 'gfm' | 'commonmark' // Configure what kind of mdx syntax will be used to parse & transform
    },
  },
})
```

## Helpful Links

* [MDX](https://mdxjs.com)
* [`@next/mdx`](https://www.npmjs.com/package/@next/mdx)
* [remark](https://github.com/remarkjs/remark)
* [rehype](https://github.com/rehypejs/rehype)
* [Markdoc](https://markdoc.dev/docs/nextjs)


--------------------------------------------------------------------------------
title: "Migrating"
description: "Learn how to migrate from popular frameworks to Next.js"
source: "https://nextjs.org/docs/pages/guides/migrating"
--------------------------------------------------------------------------------

# Migrating

@router: Pages Router



 - [App Router](/docs/pages/guides/migrating/app-router-migration.md)
 - [Create React App](/docs/pages/guides/migrating/from-create-react-app.md)
 - [Vite](/docs/pages/guides/migrating/from-vite.md)

--------------------------------------------------------------------------------
title: "How to migrate from Pages to the App Router"
description: "Learn how to upgrade your existing Next.js application from the Pages Router to the App Router."
source: "https://nextjs.org/docs/pages/guides/migrating/app-router-migration"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./11-staticgeneration.md) | [Index](./index.md) | [Next →](./13-app-router.md)
