**Navigation:** [← Previous](./02-image-optimization.md) | [Index](./index.md) | [Next →](./04-app-router.md)

---

# Content Security Policy

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

You can read the nonce from a [Server Component](/docs/app/getting-started/server-and-client-components.md) using [`headers`](/docs/app/api-reference/functions/headers.md):

```tsx filename="app/page.tsx" switcher
import { headers } from 'next/headers'
import Script from 'next/script'

export default async function Page() {
  const nonce = (await headers()).get('x-nonce')

  return (
    <Script
      src="https://www.googletagmanager.com/gtag/js"
      strategy="afterInteractive"
      nonce={nonce}
    />
  )
}
```

```jsx filename="app/page.jsx" switcher
import { headers } from 'next/headers'
import Script from 'next/script'

export default async function Page() {
  const nonce = (await headers()).get('x-nonce')

  return (
    <Script
      src="https://www.googletagmanager.com/gtag/js"
      strategy="afterInteractive"
      nonce={nonce}
    />
  )
}
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

## Subresource Integrity (Experimental)

As an alternative to nonces, Next.js offers experimental support for hash-based CSP using Subresource Integrity (SRI). This approach allows you to maintain static generation while still having a strict CSP.

> **Good to know**: This feature is experimental and only available with webpack bundler in App Router applications.

### How SRI works

Instead of using nonces, SRI generates cryptographic hashes of your JavaScript files at build time. These hashes are added as `integrity` attributes to script tags, allowing browsers to verify that files haven't been modified during transit.

### Enabling SRI

Add the experimental SRI configuration to your `next.config.js`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    sri: {
      algorithm: 'sha256', // or 'sha384' or 'sha512'
    },
  },
}

module.exports = nextConfig
```

### CSP configuration with SRI

When SRI is enabled, you can continue using your existing CSP policies. SRI works independently by adding `integrity` attributes to your assets:

> **Good to know**: For dynamic rendering scenarios, you can still generate nonces with proxy if needed, combining both SRI integrity attributes and nonce-based CSP approaches.

```js filename="next.config.js"
const cspHeader = `
    default-src 'self';
    script-src 'self';
    style-src 'self';
    img-src 'self' blob: data:;
    font-src 'self';
    object-src 'none';
    base-uri 'self';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
`

module.exports = {
  experimental: {
    sri: {
      algorithm: 'sha256',
    },
  },
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

### Benefits of SRI over nonces

* **Static generation**: Pages can be statically generated and cached
* **CDN compatibility**: Static pages work with CDN caching
* **Better performance**: No server-side rendering required for each request
* **Build-time security**: Hashes are generated at build time, ensuring integrity

### Limitations of SRI

* **Experimental**: Feature may change or be removed
* **Webpack only**: Not available with Turbopack
* **App Router only**: Not supported in Pages Router
* **Build-time only**: Cannot handle dynamically generated scripts

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

When using third-party scripts with CSP:

```tsx filename="app/layout.tsx" switcher
import { GoogleTagManager } from '@next/third-parties/google'
import { headers } from 'next/headers'

export default async function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const nonce = (await headers()).get('x-nonce')

  return (
    <html lang="en">
      <body>
        {children}
        <GoogleTagManager gtmId="GTM-XYZ" nonce={nonce} />
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.jsx" switcher
import { GoogleTagManager } from '@next/third-parties/google'
import { headers } from 'next/headers'

export default async function RootLayout({ children }) {
  const nonce = (await headers()).get('x-nonce')

  return (
    <html lang="en">
      <body>
        {children}
        <GoogleTagManager gtmId="GTM-XYZ" nonce={nonce} />
      </body>
    </html>
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
source: "https://nextjs.org/docs/app/guides/css-in-js"
--------------------------------------------------------------------------------

# CSS-in-JS

> **Warning:** Using CSS-in-JS with newer React features like Server Components and Streaming requires library authors to support the latest version of React, including [concurrent rendering](https://react.dev/blog/2022/03/29/react-v18#what-is-concurrent-react).

The following libraries are supported in Client Components in the `app` directory (alphabetical):

* [`ant-design`](https://ant.design/docs/react/use-with-next#using-app-router)
* [`chakra-ui`](https://chakra-ui.com/getting-started/nextjs-app-guide)
* [`@fluentui/react-components`](https://react.fluentui.dev/?path=/docs/concepts-developer-server-side-rendering-next-js-appdir-setup--page)
* [`kuma-ui`](https://kuma-ui.com)
* [`@mui/material`](https://mui.com/material-ui/guides/next-js-app-router/)
* [`@mui/joy`](https://mui.com/joy-ui/integrations/next-js-app-router/)
* [`pandacss`](https://panda-css.com)
* [`styled-jsx`](#styled-jsx)
* [`styled-components`](#styled-components)
* [`stylex`](https://stylexjs.com)
* [`tamagui`](https://tamagui.dev/docs/guides/next-js#server-components)
* [`tss-react`](https://tss-react.dev/)
* [`vanilla-extract`](https://vanilla-extract.style)

The following are currently working on support:

* [`emotion`](https://github.com/emotion-js/emotion/issues/2928)

> **Good to know**: We're testing out different CSS-in-JS libraries and we'll be adding more examples for libraries that support React 18 features and/or the `app` directory.

## Configuring CSS-in-JS in `app`

Configuring CSS-in-JS is a three-step opt-in process that involves:

1. A **style registry** to collect all CSS rules in a render.
2. The new `useServerInsertedHTML` hook to inject rules before any content that might use them.
3. A Client Component that wraps your app with the style registry during initial server-side rendering.

### `styled-jsx`

Using `styled-jsx` in Client Components requires using `v5.1.0`. First, create a new registry:

```tsx filename="app/registry.tsx" switcher
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { StyleRegistry, createStyleRegistry } from 'styled-jsx'

export default function StyledJsxRegistry({
  children,
}: {
  children: React.ReactNode
}) {
  // Only create stylesheet once with lazy initial state
  // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
  const [jsxStyleRegistry] = useState(() => createStyleRegistry())

  useServerInsertedHTML(() => {
    const styles = jsxStyleRegistry.styles()
    jsxStyleRegistry.flush()
    return <>{styles}</>
  })

  return <StyleRegistry registry={jsxStyleRegistry}>{children}</StyleRegistry>
}
```

```jsx filename="app/registry.js" switcher
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { StyleRegistry, createStyleRegistry } from 'styled-jsx'

export default function StyledJsxRegistry({ children }) {
  // Only create stylesheet once with lazy initial state
  // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
  const [jsxStyleRegistry] = useState(() => createStyleRegistry())

  useServerInsertedHTML(() => {
    const styles = jsxStyleRegistry.styles()
    jsxStyleRegistry.flush()
    return <>{styles}</>
  })

  return <StyleRegistry registry={jsxStyleRegistry}>{children}</StyleRegistry>
}
```

Then, wrap your [root layout](/docs/app/api-reference/file-conventions/layout.md#root-layout) with the registry:

```tsx filename="app/layout.tsx" switcher
import StyledJsxRegistry from './registry'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <StyledJsxRegistry>{children}</StyledJsxRegistry>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import StyledJsxRegistry from './registry'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <StyledJsxRegistry>{children}</StyledJsxRegistry>
      </body>
    </html>
  )
}
```

[View an example here](https://github.com/vercel/next.js/tree/canary/examples/with-styled-jsx).

### Styled Components

Below is an example of how to configure `styled-components@6` or newer:

First, enable styled-components in `next.config.js`.

```js filename="next.config.js"
module.exports = {
  compiler: {
    styledComponents: true,
  },
}
```

Then, use the `styled-components` API to create a global registry component to collect all CSS style rules generated during a render, and a function to return those rules. Then use the `useServerInsertedHTML` hook to inject the styles collected in the registry into the `<head>` HTML tag in the root layout.

```tsx filename="lib/registry.tsx" switcher
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { ServerStyleSheet, StyleSheetManager } from 'styled-components'

export default function StyledComponentsRegistry({
  children,
}: {
  children: React.ReactNode
}) {
  // Only create stylesheet once with lazy initial state
  // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
  const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet())

  useServerInsertedHTML(() => {
    const styles = styledComponentsStyleSheet.getStyleElement()
    styledComponentsStyleSheet.instance.clearTag()
    return <>{styles}</>
  })

  if (typeof window !== 'undefined') return <>{children}</>

  return (
    <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>
      {children}
    </StyleSheetManager>
  )
}
```

```jsx filename="lib/registry.js" switcher
'use client'

import React, { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { ServerStyleSheet, StyleSheetManager } from 'styled-components'

export default function StyledComponentsRegistry({ children }) {
  // Only create stylesheet once with lazy initial state
  // x-ref: https://reactjs.org/docs/hooks-reference.html#lazy-initial-state
  const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet())

  useServerInsertedHTML(() => {
    const styles = styledComponentsStyleSheet.getStyleElement()
    styledComponentsStyleSheet.instance.clearTag()
    return <>{styles}</>
  })

  if (typeof window !== 'undefined') return <>{children}</>

  return (
    <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>
      {children}
    </StyleSheetManager>
  )
}
```

Wrap the `children` of the root layout with the style registry component:

```tsx filename="app/layout.tsx" switcher
import StyledComponentsRegistry from './lib/registry'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <StyledComponentsRegistry>{children}</StyledComponentsRegistry>
      </body>
    </html>
  )
}
```

```jsx filename="app/layout.js" switcher
import StyledComponentsRegistry from './lib/registry'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <StyledComponentsRegistry>{children}</StyledComponentsRegistry>
      </body>
    </html>
  )
}
```

[View an example here](https://github.com/vercel/next.js/tree/canary/examples/with-styled-components).

> **Good to know**:
>
> * During server rendering, styles will be extracted to a global registry and flushed to the `<head>` of your HTML. This ensures the style rules are placed before any content that might use them. In the future, we may use an upcoming React feature to determine where to inject the styles.
> * During streaming, styles from each chunk will be collected and appended to existing styles. After client-side hydration is complete, `styled-components` will take over as usual and inject any further dynamic styles.
> * We specifically use a Client Component at the top level of the tree for the style registry because it's more efficient to extract CSS rules this way. It avoids re-generating styles on subsequent server renders, and prevents them from being sent in the Server Component payload.
> * For advanced use cases where you need to configure individual properties of styled-components compilation, you can read our [Next.js styled-components API reference](/docs/architecture/nextjs-compiler.md#styled-components) to learn more.


--------------------------------------------------------------------------------
title: "How to set up a custom server in Next.js"
description: "Start a Next.js app programmatically using a custom server."
source: "https://nextjs.org/docs/app/guides/custom-server"
--------------------------------------------------------------------------------

# Custom Server

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


--------------------------------------------------------------------------------
title: "How to think about data security in Next.js"
description: "Learn the built-in data security features in Next.js and learn best practices for protecting your application's data."
source: "https://nextjs.org/docs/app/guides/data-security"
--------------------------------------------------------------------------------

# Data Security

[React Server Components](https://react.dev/reference/rsc/server-components) improve performance and simplify data fetching, but also shift where and how data is accessed, changing some of the traditional security assumptions for handling data in frontend apps.

This guide will help you understand how to think about data security in Next.js and how to implement best practices.

## Data fetching approaches

There are three main approaches we recommend for fetching data in Next.js, depending on the size and age of your project:

* [HTTP APIs](#external-http-apis): for existing large applications and organizations.
* [Data Access Layer](#data-access-layer): for new projects.
* [Component-Level Data Access](#component-level-data-access): for prototypes and learning.

We recommend choosing one data fetching approach and avoiding mixing them. This makes it clear for both developers working in your code base and security auditors what to expect.

### External HTTP APIs

You should follow a **Zero Trust** model when adopting Server Components in an existing project. You can continue calling your existing API endpoints such as REST or GraphQL from Server Components using [`fetch`](/docs/app/api-reference/functions/fetch.md), just as you would in Client Components.

```tsx filename="app/page.tsx"
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = cookies()
  const token = cookieStore.get('AUTH_TOKEN')?.value

  const res = await fetch('https://api.example.com/profile', {
    headers: {
      Cookie: `AUTH_TOKEN=${token}`,
      // Other headers
    },
  })

  // ....
}
```

This approach works well when:

* You already have security practices in place.
* Separate backend teams use other languages or manage APIs independently.

### Data Access Layer

For new projects, we recommend creating a dedicated **Data Access Layer (DAL)**. This is a internal library that controls how and when data is fetched, and what gets passed to your render context.

A Data Access Layer should:

* Only run on the server.
* Perform authorization checks.
* Return safe, minimal **Data Transfer Objects (DTOs)**.

This approach centralizes all data access logic, making it easier to enforce consistent data access and reduces the risk of authorization bugs. You also get the benefit of sharing an in-memory cache across different parts of a request.

```ts filename="data/auth.ts"
import { cache } from 'react'
import { cookies } from 'next/headers'

// Cached helper methods makes it easy to get the same value in many places
// without manually passing it around. This discourages passing it from Server
// Component to Server Component which minimizes risk of passing it to a Client
// Component.
export const getCurrentUser = cache(async () => {
  const token = cookies().get('AUTH_TOKEN')
  const decodedToken = await decryptAndValidate(token)
  // Don't include secret tokens or private information as public fields.
  // Use classes to avoid accidentally passing the whole object to the client.
  return new User(decodedToken.id)
})
```

```tsx filename="data/user-dto.tsx"
import 'server-only'
import { getCurrentUser } from './auth'

function canSeeUsername(viewer: User) {
  // Public info for now, but can change
  return true
}

function canSeePhoneNumber(viewer: User, team: string) {
  // Privacy rules
  return viewer.isAdmin || team === viewer.team
}

export async function getProfileDTO(slug: string) {
  // Don't pass values, read back cached values, also solves context and easier to make it lazy

  // use a database API that supports safe templating of queries
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const userData = rows[0]

  const currentUser = await getCurrentUser()

  // only return the data relevant for this query and not everything
  // <https://www.w3.org/2001/tag/doc/APIMinimization>
  return {
    username: canSeeUsername(currentUser) ? userData.username : null,
    phonenumber: canSeePhoneNumber(currentUser, userData.team)
      ? userData.phonenumber
      : null,
  }
}
```

```tsx filename="app/page.tsx"
import { getProfile } from '../../data/user'

export async function Page({ params: { slug } }) {
  // This page can now safely pass around this profile knowing
  // that it shouldn't contain anything sensitive.
  const profile = await getProfile(slug);
  ...
}
```

> **Good to know:** Secret keys should be stored in environment variables, but only the Data Access Layer should access `process.env`. This keeps secrets from being exposed to other parts of the application.

### Component-level data access

For quick prototypes and iteration, database queries can be placed directly in Server Components.

This approach, however, makes it easier to accidentally expose private data to the client, for example:

```tsx filename="app/page.tsx"
import Profile from './components/profile.tsx'

export async function Page({ params: { slug } }) {
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const userData = rows[0]
  // EXPOSED: This exposes all the fields in userData to the client because
  // we are passing the data from the Server Component to the Client.
  return <Profile user={userData} />
}
```

```tsx filename="app/ui/profile.tsx"
'use client'

// BAD: This is a bad props interface because it accepts way more data than the
// Client Component needs and it encourages server components to pass all that
// data down. A better solution would be to accept a limited object with just
// the fields necessary for rendering the profile.
export default async function Profile({ user }: { user: User }) {
  return (
    <div>
      <h1>{user.name}</h1>
      ...
    </div>
  )
}
```

You should sanitize the data before passing it to the Client Component:

```ts filename="data/user.ts"
import { sql } from './db'

export async function getUser(slug: string) {
  const [rows] = await sql`SELECT * FROM user WHERE slug = ${slug}`
  const user = rows[0]

  // Return only the public fields
  return {
    name: user.name,
  }
}
```

```tsx filename="app/page.tsx"
import { getUser } from '../data/user'
import Profile from './ui/profile'

export default async function Page({
  params: { slug },
}: {
  params: { slug: string }
}) {
  const publicProfile = await getUser(slug)
  return <Profile user={publicProfile} />
}
```

## Reading data

### Passing data from server to client

On the initial load, both Server and Client Components run on the server to generate HTML. However, they execute in isolated module systems. This ensures that Server Components can access private data and APIs, while Client Components cannot.

**Server Components:**

* Run only on the server.
* Can safely access environment variables, secrets, databases, and internal APIs.

**Client Components:**

* Run on the server during pre-rendering, but must follow the same security assumptions as code running in the browser.
* Must not access privileged data or server-only modules.

This ensures the app is secure by default, but it's possible to accidentally expose private data through how data is fetched or passed to components.

### Tainting

To prevent accidental exposure of private data to the client, you can use React Taint APIs:

* [`experimental_taintObjectReference`](https://react.dev/reference/react/experimental_taintObjectReference) for data objects.
* [`experimental_taintUniqueValue`](https://react.dev/reference/react/experimental_taintUniqueValue) for specific values.

You can enable usage in your Next.js app with the [`experimental.taint`](/docs/app/api-reference/config/next-config-js/taint.md) option in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  experimental: {
    taint: true,
  },
}
```

This prevents the tainted objects or values from being passed to the client. However, it's an additional layer of protection, you should still filter and sanitize the data in your [DAL](#data-access-layer) before passing it to React's render context.

> **Good to know:**
>
> * By default, environment variables are only available on the Server. Next.js exposes any environment variable prefixed with `NEXT_PUBLIC_` to the client. [Learn more](/docs/app/guides/environment-variables.md).
> * Functions and classes are already blocked from being passed to Client Components by default.

### Preventing client-side execution of server-only code

To prevent server-only code from being executed on the client, you can mark a module with the [`server-only`](https://www.npmjs.com/package/server-only) package:

```bash package="npm"
npm install server-only
```

```bash package="yarn"
yarn add server-only
```

```bash package="pnpm"
pnpm add server-only
```

```bash package="bun"
bun add server-only
```

```ts filename="lib/data.ts"
import 'server-only'

//...
```

This ensures that proprietary code or internal business logic stays on the server by causing a build error if the module is imported in the client environment.

## Mutating Data

Next.js handles mutations with [Server Actions](https://react.dev/reference/rsc/server-functions).

### Built-in Server Actions Security features

By default, when a Server Action is created and exported, it creates a public HTTP endpoint and should be treated with the same security assumptions and authorization checks. This means, even if a Server Action or utility function is not imported elsewhere in your code, it's still publicly accessible.

To improve security, Next.js has the following built-in features:

* **Secure action IDs:** Next.js creates encrypted, non-deterministic IDs to allow the client to reference and call the Server Action. These IDs are periodically recalculated between builds for enhanced security.
* **Dead code elimination:** Unused Server Actions (referenced by their IDs) are removed from client bundle to avoid public access.

> **Good to know**:
>
> The IDs are created during compilation and are cached for a maximum of 14 days. They will be regenerated when a new build is initiated or when the build cache is invalidated.
> This security improvement reduces the risk in cases where an authentication layer is missing. However, you should still treat Server Actions like public HTTP endpoints.

```jsx
// app/actions.js
'use server'

// If this action **is** used in our application, Next.js
// will create a secure ID to allow the client to reference
// and call the Server Action.
export async function updateUserAction(formData) {}

// If this action **is not** used in our application, Next.js
// will automatically remove this code during `next build`
// and will not create a public endpoint.
export async function deleteUserAction(formData) {}
```

### Validating client input

You should always validate input from client, as they can be easily modified. For example, form data, URL parameters, headers, and searchParams:

```tsx filename="app/page.tsx"
// BAD: Trusting searchParams directly
export default async function Page({ searchParams }) {
  const isAdmin = searchParams.get('isAdmin')
  if (isAdmin === 'true') {
    // Vulnerable: relies on untrusted client data
    return <AdminPanel />
  }
}

// GOOD: Re-verify every time
import { cookies } from 'next/headers'
import { verifyAdmin } from './auth'

export default async function Page() {
  const token = cookies().get('AUTH_TOKEN')
  const isAdmin = await verifyAdmin(token)

  if (isAdmin) {
    return <AdminPanel />
  }
}
```

### Authentication and authorization

You should always ensure that a user is authorized to perform an action. For example:

```tsx filename="app/actions.ts"
'use server'

import { auth } from './lib'

export function addItem() {
  const { user } = auth()
  if (!user) {
    throw new Error('You must be signed in to perform this action')
  }

  // ...
}
```

Learn more about [Authentication](/docs/app/guides/authentication.md) in Next.js.

### Closures and encryption

Defining a Server Action inside a component creates a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) where the action has access to the outer function's scope. For example, the `publish` action has access to the `publishVersion` variable:

```tsx filename="app/page.tsx" switcher
export default async function Page() {
  const publishVersion = await getLatestVersion();

  async function publish() {
    "use server";
    if (publishVersion !== await getLatestVersion()) {
      throw new Error('The version has changed since pressing publish');
    }
    ...
  }

  return (
    <form>
      <button formAction={publish}>Publish</button>
    </form>
  );
}
```

```jsx filename="app/page.js" switcher
export default async function Page() {
  const publishVersion = await getLatestVersion();

  async function publish() {
    "use server";
    if (publishVersion !== await getLatestVersion()) {
      throw new Error('The version has changed since pressing publish');
    }
    ...
  }

  return (
    <form>
      <button formAction={publish}>Publish</button>
    </form>
  );
}
```

Closures are useful when you need to capture a *snapshot* of data (e.g. `publishVersion`) at the time of rendering so that it can be used later when the action is invoked.

However, for this to happen, the captured variables are sent to the client and back to the server when the action is invoked. To prevent sensitive data from being exposed to the client, Next.js automatically encrypts the closed-over variables. A new private key is generated for each action every time a Next.js application is built. This means actions can only be invoked for a specific build.

> **Good to know:** We don't recommend relying on encryption alone to prevent sensitive values from being exposed on the client.

### Overwriting encryption keys (advanced)

When self-hosting your Next.js application across multiple servers, each server instance may end up with a different encryption key, leading to potential inconsistencies.

To mitigate this, you can overwrite the encryption key using the `process.env.NEXT_SERVER_ACTIONS_ENCRYPTION_KEY` environment variable. Specifying this variable ensures that your encryption keys are persistent across builds, and all server instances use the same key. This variable **must** be AES-GCM encrypted.

This is an advanced use case where consistent encryption behavior across multiple deployments is critical for your application. You should consider standard security practices such key rotation and signing.

> **Good to know:** Next.js applications deployed to Vercel automatically handle this.

### Allowed origins (advanced)

Since Server Actions can be invoked in a `<form>` element, this opens them up to [CSRF attacks](https://developer.mozilla.org/en-US/docs/Glossary/CSRF).

Behind the scenes, Server Actions use the `POST` method, and only this HTTP method is allowed to invoke them. This prevents most CSRF vulnerabilities in modern browsers, particularly with [SameSite cookies](https://web.dev/articles/samesite-cookies-explained) being the default.

As an additional protection, Server Actions in Next.js also compare the [Origin header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) to the [Host header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host) (or `X-Forwarded-Host`). If these don't match, the request will be aborted. In other words, Server Actions can only be invoked on the same host as the page that hosts it.

For large applications that use reverse proxies or multi-layered backend architectures (where the server API differs from the production domain), it's recommended to use the configuration option [`serverActions.allowedOrigins`](/docs/app/api-reference/config/next-config-js/serverActions.md) option to specify a list of safe origins. The option accepts an array of strings.

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

Learn more about [Security and Server Actions](https://nextjs.org/blog/security-nextjs-server-components-actions).

### Avoiding side-effects during rendering

Mutations (e.g. logging out users, updating databases, invalidating caches) should never be a side-effect, either in Server or Client Components. Next.js explicitly prevents setting cookies or triggering cache revalidation within render methods to avoid unintended side effects.

```tsx filename="app/page.tsx"
// BAD: Triggering a mutation during rendering
export default async function Page({ searchParams }) {
  if (searchParams.get('logout')) {
    cookies().delete('AUTH_TOKEN')
  }

  return <UserProfile />
}
```

Instead, you should use Server Actions to handle mutations.

```tsx filename="app/page.tsx"
// GOOD: Using Server Actions to handle mutations
import { logout } from './actions'

export default function Page() {
  return (
    <>
      <UserProfile />
      <form action={logout}>
        <button type="submit">Logout</button>
      </form>
    </>
  )
}
```

> **Good to know:** Next.js uses `POST` requests to handle mutations. This prevents accidental side-effects from GET requests, reducing Cross-Site Request Forgery (CSRF) risks.

## Auditing

If you're doing an audit of a Next.js project, here are a few things we recommend looking extra at:

* **Data Access Layer:** Is there an established practice for an isolated Data Access Layer? Verify that database packages and environment variables are not imported outside the Data Access Layer.
* **`"use client"` files:** Are the Component props expecting private data? Are the type signatures overly broad?
* **`"use server"` files:** Are the Action arguments validated in the action or inside the Data Access Layer? Is the user re-authorized inside the action?
* **`/[param]/.`** Folders with brackets are user input. Are params validated?
* **`proxy.ts` and `route.ts`:** Have a lot of power. Spend extra time auditing these using traditional techniques. Perform Penetration Testing or Vulnerability Scanning regularly or in alignment with your team's software development lifecycle.
## Next Steps

Learn more about the topics mentioned in this guide.

- [Authentication](/docs/app/guides/authentication.md)
  - Learn how to implement authentication in your Next.js application.
- [Content Security Policy](/docs/app/guides/content-security-policy.md)
  - Learn how to set a Content Security Policy (CSP) for your Next.js application.
- [Forms](/docs/app/guides/forms.md)
  - Learn how to create forms in Next.js with React Server Actions.


--------------------------------------------------------------------------------
title: "How to use debugging tools with Next.js"
description: "Learn how to debug your Next.js application with VS Code, Chrome DevTools, or Firefox DevTools."
source: "https://nextjs.org/docs/app/guides/debugging"
--------------------------------------------------------------------------------

# Debugging

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
description: "Next.js has draft mode to toggle between static and dynamic pages. You can learn how it works with App Router here."
source: "https://nextjs.org/docs/app/guides/draft-mode"
--------------------------------------------------------------------------------

# Draft Mode

**Draft Mode** allows you to preview draft content from your headless CMS in your Next.js application. This is useful for static pages that are generated at build time as it allows you to switch to [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering) and see the draft changes without having to rebuild your entire site.

This page walks through how to enable and use Draft Mode.

## Step 1: Create a Route Handler

Create a [Route Handler](/docs/app/api-reference/file-conventions/route.md). It can have any name, for example, `app/api/draft/route.ts`.

```ts filename="app/api/draft/route.ts" switcher
export async function GET(request: Request) {
  return new Response('')
}
```

```js filename="app/api/draft/route.js" switcher
export async function GET() {
  return new Response('')
}
```

Then, import the [`draftMode`](/docs/app/api-reference/functions/draft-mode.md) function and call the `enable()` method.

```ts filename="app/api/draft/route.ts" switcher
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

```js filename="app/api/draft/route.js" switcher
import { draftMode } from 'next/headers'

export async function GET(request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

This will set a **cookie** to enable draft mode. Subsequent requests containing this cookie will trigger draft mode and change the behavior of statically generated pages.

You can test this manually by visiting `/api/draft` and looking at your browser’s developer tools. Notice the `Set-Cookie` response header with a cookie named `__prerender_bypass`.

## Step 2: Access the Route Handler from your Headless CMS

> These steps assume that the headless CMS you’re using supports setting **custom draft URLs**. If it doesn’t, you can still use this method to secure your draft URLs, but you’ll need to construct and access the draft URL manually. The specific steps will vary depending on which headless CMS you’re using.

To securely access the Route Handler from your headless CMS:

1. Create a **secret token string** using a token generator of your choice. This secret will only be known by your Next.js app and your headless CMS.
2. If your headless CMS supports setting custom draft URLs, specify a draft URL (this assumes that your Route Handler is located at `app/api/draft/route.ts`). For example:

```bash filename="Terminal"
https://<your-site>/api/draft?secret=<token>&slug=<path>
```

> * `<your-site>` should be your deployment domain.
> * `<token>` should be replaced with the secret token you generated.
> * `<path>` should be the path for the page that you want to view. If you want to view `/posts/one`, then you should use `&slug=/posts/one`.
>
> Your headless CMS might allow you to include a variable in the draft URL so that `<path>` can be set dynamically based on the CMS’s data like so: `&slug=/posts/{entry.fields.slug}`

3. In your Route Handler, check that the secret matches and that the `slug` parameter exists (if not, the request should fail), call `draftMode.enable()` to set the cookie. Then, redirect the browser to the path specified by `slug`:

```ts filename="app/api/draft/route.ts" switcher
import { draftMode } from 'next/headers'
import { redirect } from 'next/navigation'

export async function GET(request: Request) {
  // Parse query string parameters
  const { searchParams } = new URL(request.url)
  const secret = searchParams.get('secret')
  const slug = searchParams.get('slug')

  // Check the secret and next parameters
  // This secret should only be known to this Route Handler and the CMS
  if (secret !== 'MY_SECRET_TOKEN' || !slug) {
    return new Response('Invalid token', { status: 401 })
  }

  // Fetch the headless CMS to check if the provided `slug` exists
  // getPostBySlug would implement the required fetching logic to the headless CMS
  const post = await getPostBySlug(slug)

  // If the slug doesn't exist prevent draft mode from being enabled
  if (!post) {
    return new Response('Invalid slug', { status: 401 })
  }

  // Enable Draft Mode by setting the cookie
  const draft = await draftMode()
  draft.enable()

  // Redirect to the path from the fetched post
  // We don't redirect to searchParams.slug as that might lead to open redirect vulnerabilities
  redirect(post.slug)
}
```

```js filename="app/api/draft/route.js" switcher
import { draftMode } from 'next/headers'
import { redirect } from 'next/navigation'

export async function GET(request) {
  // Parse query string parameters
  const { searchParams } = new URL(request.url)
  const secret = searchParams.get('secret')
  const slug = searchParams.get('slug')

  // Check the secret and next parameters
  // This secret should only be known to this Route Handler and the CMS
  if (secret !== 'MY_SECRET_TOKEN' || !slug) {
    return new Response('Invalid token', { status: 401 })
  }

  // Fetch the headless CMS to check if the provided `slug` exists
  // getPostBySlug would implement the required fetching logic to the headless CMS
  const post = await getPostBySlug(slug)

  // If the slug doesn't exist prevent draft mode from being enabled
  if (!post) {
    return new Response('Invalid slug', { status: 401 })
  }

  // Enable Draft Mode by setting the cookie
  const draft = await draftMode()
  draft.enable()

  // Redirect to the path from the fetched post
  // We don't redirect to searchParams.slug as that might lead to open redirect vulnerabilities
  redirect(post.slug)
}
```

If it succeeds, then the browser will be redirected to the path you want to view with the draft mode cookie.

## Step 3: Preview the Draft Content

The next step is to update your page to check the value of `draftMode().isEnabled`.

If you request a page which has the cookie set, then data will be fetched at **request time** (instead of at build time).

Furthermore, the value of `isEnabled` will be `true`.

```tsx filename="app/page.tsx" switcher
// page that fetches data
import { draftMode } from 'next/headers'

async function getData() {
  const { isEnabled } = await draftMode()

  const url = isEnabled
    ? 'https://draft.example.com'
    : 'https://production.example.com'

  const res = await fetch(url)

  return res.json()
}

export default async function Page() {
  const { title, desc } = await getData()

  return (
    <main>
      <h1>{title}</h1>
      <p>{desc}</p>
    </main>
  )
}
```

```jsx filename="app/page.js" switcher
// page that fetches data
import { draftMode } from 'next/headers'

async function getData() {
  const { isEnabled } = await draftMode()

  const url = isEnabled
    ? 'https://draft.example.com'
    : 'https://production.example.com'

  const res = await fetch(url)

  return res.json()
}

export default async function Page() {
  const { title, desc } = await getData()

  return (
    <main>
      <h1>{title}</h1>
      <p>{desc}</p>
    </main>
  )
}
```

If you access the draft Route Handler (with `secret` and `slug`) from your headless CMS or manually using the URL, you should now be able to see the draft content. And, if you update your draft without publishing, you should be able to view the draft.
## Next Steps

See the API reference for more information on how to use Draft Mode.

- [draftMode](/docs/app/api-reference/functions/draft-mode.md)
  - API Reference for the draftMode function.


--------------------------------------------------------------------------------
title: "How to use environment variables in Next.js"
description: "Learn to add and access environment variables in your Next.js application."
source: "https://nextjs.org/docs/app/guides/environment-variables"
--------------------------------------------------------------------------------

# Environment Variables

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

> **Note**: Next.js also supports multiline variables inside of your `.env*` files:
>
> ```bash
> # .env
>
> # you can write with line breaks
> PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----
> ...
> Kh9NV...
> ...
> -----END DSA PRIVATE KEY-----"
>
> # or with `\n` inside double quotes
> PRIVATE_KEY="-----BEGIN RSA PRIVATE KEY-----\nKh9NV...\n-----END DSA PRIVATE KEY-----\n"
> ```

> **Note**: If you are using a `/src` folder, please note that Next.js will load the .env files **only** from the parent folder and **not** from the `/src` folder.
> This loads `process.env.DB_HOST`, `process.env.DB_USER`, and `process.env.DB_PASS` into the Node.js environment automatically allowing you to use them in [Route Handlers](/docs/app/api-reference/file-conventions/route.md).

For example:

```js filename="app/api/route.js"
export async function GET() {
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

You can safely read environment variables on the server during dynamic rendering:

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
title: "How to create forms with Server Actions"
description: "Learn how to create forms in Next.js with React Server Actions."
source: "https://nextjs.org/docs/app/guides/forms"
--------------------------------------------------------------------------------

# Forms

React Server Actions are [Server Functions](https://react.dev/reference/rsc/server-functions) that execute on the server. They can be called in Server and Client Components to handle form submissions. This guide will walk you through how to create forms in Next.js with Server Actions.

## How it works

React extends the HTML [`<form>`](https://developer.mozilla.org/docs/Web/HTML/Element/form) element to allow Server Actions to be invoked with the [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action) attribute.

When used in a form, the function automatically receives the [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData/FormData) object. You can then extract the data using the native [`FormData` methods](https://developer.mozilla.org/en-US/docs/Web/API/FormData#instance_methods):

```tsx filename="app/invoices/page.tsx" switcher
export default function Page() {
  async function createInvoice(formData: FormData) {
    'use server'

    const rawFormData = {
      customerId: formData.get('customerId'),
      amount: formData.get('amount'),
      status: formData.get('status'),
    }

    // mutate data
    // revalidate the cache
  }

  return <form action={createInvoice}>...</form>
}
```

```jsx filename="app/invoices/page.js" switcher
export default function Page() {
  async function createInvoice(formData) {
    'use server'

    const rawFormData = {
      customerId: formData.get('customerId'),
      amount: formData.get('amount'),
      status: formData.get('status'),
    }

    // mutate data
    // revalidate the cache
  }

  return <form action={createInvoice}>...</form>
}
```

> **Good to know:** When working with forms that have multiple fields, use JavaScript's [`Object.fromEntries()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/fromEntries). For example: `const rawFormData = Object.fromEntries(formData)`. Note that this object will contain extra properties prefixed with `$ACTION_`.

## Passing additional arguments

Outside of form fields, you can pass additional arguments to a Server Function using the JavaScript [`bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) method. For example, to pass the `userId` argument to the `updateUser` Server Function:

```tsx filename="app/client-component.tsx" highlight={6} switcher
'use client'

import { updateUser } from './actions'

export function UserProfile({ userId }: { userId: string }) {
  const updateUserWithId = updateUser.bind(null, userId)

  return (
    <form action={updateUserWithId}>
      <input type="text" name="name" />
      <button type="submit">Update User Name</button>
    </form>
  )
}
```

```jsx filename="app/client-component.js" highlight={6} switcher
'use client'

import { updateUser } from './actions'

export function UserProfile({ userId }) {
  const updateUserWithId = updateUser.bind(null, userId)

  return (
    <form action={updateUserWithId}>
      <input type="text" name="name" />
      <button type="submit">Update User Name</button>
    </form>
  )
}
```

The Server Function will receive the `userId` as an additional argument:

```ts filename="app/actions.ts" switcher
'use server'

export async function updateUser(userId: string, formData: FormData) {}
```

```js filename="app/actions.js" switcher
'use server'

export async function updateUser(userId, formData) {}
```

> **Good to know**:
>
> * An alternative is to pass arguments as hidden input fields in the form (e.g. `<input type="hidden" name="userId" value={userId} />`). However, the value will be part of the rendered HTML and will not be encoded.
> * `bind` works in both Server and Client Components and supports progressive enhancement.

## Form validation

Forms can be validated on the client or server.

* For **client-side validation**, you can use the HTML attributes like `required` and `type="email"` for basic validation.
* For **server-side validation**, you can use a library like [zod](https://zod.dev/) to validate the form fields. For example:

```tsx filename="app/actions.ts" switcher
'use server'

import { z } from 'zod'

const schema = z.object({
  email: z.string({
    invalid_type_error: 'Invalid Email',
  }),
})

export default async function createUser(formData: FormData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })

  // Return early if the form data is invalid
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Mutate data
}
```

```jsx filename="app/actions.js" switcher
'use server'

import { z } from 'zod'

const schema = z.object({
  email: z.string({
    invalid_type_error: 'Invalid Email',
  }),
})

export default async function createsUser(formData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })

  // Return early if the form data is invalid
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    }
  }

  // Mutate data
}
```

## Validation errors

To display validation errors or messages, turn the component that defines the `<form>` into a Client Component and use React [`useActionState`](https://react.dev/reference/react/useActionState).

When using `useActionState`, the Server function signature will change to receive a new `prevState` or `initialState` parameter as its first argument.

```tsx filename="app/actions.ts" highlight={4} switcher
'use server'

import { z } from 'zod'

export async function createUser(initialState: any, formData: FormData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })
  // ...
}
```

```jsx filename="app/actions.ts" highlight={4} switcher
'use server'

import { z } from 'zod'

// ...

export async function createUser(initialState, formData) {
  const validatedFields = schema.safeParse({
    email: formData.get('email'),
  })
  // ...
}
```

You can then conditionally render the error message based on the `state` object.

```tsx filename="app/ui/signup.tsx" highlight={11,18-20} switcher
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

const initialState = {
  message: '',
}

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="email">Email</label>
      <input type="text" id="email" name="email" required />
      {/* ... */}
      <p aria-live="polite">{state?.message}</p>
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```

```jsx filename="app/ui/signup.js" highlight={11,18-20} switcher
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

const initialState = {
  message: '',
}

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      <label htmlFor="email">Email</label>
      <input type="text" id="email" name="email" required />
      {/* ... */}
      <p aria-live="polite">{state?.message}</p>
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```

## Pending states

The [`useActionState`](https://react.dev/reference/react/useActionState) hook exposes a `pending` boolean that can be used to show a loading indicator or disable the submit button while the action is being executed.

```tsx filename="app/ui/signup.tsx" highlight={7,12} switcher
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      {/* Other form elements */}
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```

```jsx filename="app/ui/signup.js" highlight={7,12} switcher
'use client'

import { useActionState } from 'react'
import { createUser } from '@/app/actions'

export function Signup() {
  const [state, formAction, pending] = useActionState(createUser, initialState)

  return (
    <form action={formAction}>
      {/* Other form elements */}
      <button disabled={pending}>Sign up</button>
    </form>
  )
}
```

Alternatively, you can use the [`useFormStatus`](https://react.dev/reference/react-dom/hooks/useFormStatus) hook to show a loading indicator while the action is being executed. When using this hook, you'll need to create a separate component to render the loading indicator. For example, to disable the button when the action is pending:

```tsx filename="app/ui/button.tsx" highlight={6} switcher
'use client'

import { useFormStatus } from 'react-dom'

export function SubmitButton() {
  const { pending } = useFormStatus()

  return (
    <button disabled={pending} type="submit">
      Sign Up
    </button>
  )
}
```

```jsx filename="app/ui/button.js" highlight={6} switcher
'use client'

import { useFormStatus } from 'react-dom'

export function SubmitButton() {
  const { pending } = useFormStatus()

  return (
    <button disabled={pending} type="submit">
      Sign Up
    </button>
  )
}
```

You can then nest the `SubmitButton` component inside the form:

```tsx filename="app/ui/signup.tsx" switcher
import { SubmitButton } from './button'
import { createUser } from '@/app/actions'

export function Signup() {
  return (
    <form action={createUser}>
      {/* Other form elements */}
      <SubmitButton />
    </form>
  )
}
```

```jsx filename="app/ui/signup.js" switcher
import { SubmitButton } from './button'
import { createUser } from '@/app/actions'

export function Signup() {
  return (
    <form action={createUser}>
      {/* Other form elements */}
      <SubmitButton />
    </form>
  )
}
```

> **Good to know:** In React 19, `useFormStatus` includes additional keys on the returned object, like data, method, and action. If you are not using React 19, only the `pending` key is available.

## Optimistic updates

You can use the React [`useOptimistic`](https://react.dev/reference/react/useOptimistic) hook to optimistically update the UI before the Server Function finishes executing, rather than waiting for the response:

```tsx filename="app/page.tsx" switcher
'use client'

import { useOptimistic } from 'react'
import { send } from './actions'

type Message = {
  message: string
}

export function Thread({ messages }: { messages: Message[] }) {
  const [optimisticMessages, addOptimisticMessage] = useOptimistic<
    Message[],
    string
  >(messages, (state, newMessage) => [...state, { message: newMessage }])

  const formAction = async (formData: FormData) => {
    const message = formData.get('message') as string
    addOptimisticMessage(message)
    await send(message)
  }

  return (
    <div>
      {optimisticMessages.map((m, i) => (
        <div key={i}>{m.message}</div>
      ))}
      <form action={formAction}>
        <input type="text" name="message" />
        <button type="submit">Send</button>
      </form>
    </div>
  )
}
```

```jsx filename="app/page.js" switcher
'use client'

import { useOptimistic } from 'react'
import { send } from './actions'

export function Thread({ messages }) {
  const [optimisticMessages, addOptimisticMessage] = useOptimistic(
    messages,
    (state, newMessage) => [...state, { message: newMessage }]
  )

  const formAction = async (formData) => {
    const message = formData.get('message')
    addOptimisticMessage(message)
    await send(message)
  }

  return (
    <div>
      {optimisticMessages.map((m) => (
        <div>{m.message}</div>
      ))}
      <form action={formAction}>
        <input type="text" name="message" />
        <button type="submit">Send</button>
      </form>
    </div>
  )
}
```

## Nested form elements

You can call Server Actions in elements nested inside `<form>` such as `<button>`, `<input type="submit">`, and `<input type="image">`. These elements accept the `formAction` prop or event handlers.

This is useful in cases where you want to call multiple Server Actions within a form. For example, you can create a specific `<button>` element for saving a post draft in addition to publishing it. See the [React `<form>` docs](https://react.dev/reference/react-dom/components/form#handling-multiple-submission-types) for more information.

## Programmatic form submission

You can trigger a form submission programmatically using the [`requestSubmit()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/requestSubmit) method. For example, when the user submits a form using the `⌘` + `Enter` keyboard shortcut, you can listen for the `onKeyDown` event:

```tsx filename="app/entry.tsx" switcher
'use client'

export function Entry() {
  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (
      (e.ctrlKey || e.metaKey) &&
      (e.key === 'Enter' || e.key === 'NumpadEnter')
    ) {
      e.preventDefault()
      e.currentTarget.form?.requestSubmit()
    }
  }

  return (
    <div>
      <textarea name="entry" rows={20} required onKeyDown={handleKeyDown} />
    </div>
  )
}
```

```jsx filename="app/entry.js" switcher
'use client'

export function Entry() {
  const handleKeyDown = (e) => {
    if (
      (e.ctrlKey || e.metaKey) &&
      (e.key === 'Enter' || e.key === 'NumpadEnter')
    ) {
      e.preventDefault()
      e.currentTarget.form?.requestSubmit()
    }
  }

  return (
    <div>
      <textarea name="entry" rows={20} required onKeyDown={handleKeyDown} />
    </div>
  )
}
```

This will trigger the submission of the nearest `<form>` ancestor, which will invoke the Server Function.


--------------------------------------------------------------------------------
title: "How to implement Incremental Static Regeneration (ISR)"
description: "Learn how to create or update static pages at runtime with Incremental Static Regeneration."
source: "https://nextjs.org/docs/app/guides/incremental-static-regeneration"
--------------------------------------------------------------------------------

# ISR

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

```tsx filename="app/blog/[id]/page.tsx" switcher
interface Post {
  id: string
  title: string
  content: string
}

// Next.js will invalidate the cache when a
// request comes in, at most once every 60 seconds.
export const revalidate = 60

export async function generateStaticParams() {
  const posts: Post[] = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  return posts.map((post) => ({
    id: String(post.id),
  }))
}

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post: Post = await fetch(`https://api.vercel.app/blog/${id}`).then(
    (res) => res.json()
  )
  return (
    <main>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </main>
  )
}
```

```jsx filename="app/blog/[id]/page.jsx" switcher
// Next.js will invalidate the cache when a
// request comes in, at most once every 60 seconds.
export const revalidate = 60

export async function generateStaticParams() {
  const posts = await fetch('https://api.vercel.app/blog').then((res) =>
    res.json()
  )
  return posts.map((post) => ({
    id: String(post.id),
  }))
}

export default async function Page({ params }) {
  const { id } = await params
  const post = await fetch(`https://api.vercel.app/blog/${id}`).then((res) =>
    res.json()
  )
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
6. If `/blog/26` is requested, and it exists, the page will be generated on-demand. This behavior can be changed by using a different [dynamicParams](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams) value. However, if the post does not exist, then 404 is returned.

## Reference

### Route segment config

* [`revalidate`](/docs/app/api-reference/file-conventions/route-segment-config.md#revalidate)
* [`dynamicParams`](/docs/app/api-reference/file-conventions/route-segment-config.md#dynamicparams)

### Functions

* [`revalidatePath`](/docs/app/api-reference/functions/revalidatePath.md)
* [`revalidateTag`](/docs/app/api-reference/functions/revalidateTag.md)

## Examples

### Time-based revalidation

This fetches and displays a list of blog posts on /blog. After an hour has passed, the next visitor will still receive the cached (stale) version of the page immediately for a fast response. Simultaneously, Next.js triggers regeneration of a fresh version in the background. Once the new version is successfully generated, it replaces the cached version, and subsequent visitors will receive the updated content.

```tsx filename="app/blog/page.tsx" switcher
interface Post {
  id: string
  title: string
  content: string
}

export const revalidate = 3600 // invalidate every hour

export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts: Post[] = await data.json()
  return (
    <main>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  )
}
```

```jsx filename="app/blog/page.js" switcher
export const revalidate = 3600 // invalidate every hour

export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()
  return (
    <main>
      <h1>Blog Posts</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </main>
  )
}
```

We recommend setting a high revalidation time. For instance, 1 hour instead of 1 second. If you need more precision, consider using on-demand revalidation. If you need real-time data, consider switching to [dynamic rendering](/docs/app/guides/caching.md#dynamic-rendering).

### On-demand revalidation with `revalidatePath`

For a more precise method of revalidation, invalidate cached pages on-demand with the `revalidatePath` function.

For example, this Server Action would get called after adding a new post. Regardless of how you retrieve your data in your Server Component, either using `fetch` or connecting to a database, this will invalidate the cache for the entire route. The next request to that route will trigger regeneration and serve fresh data, which will then be cached for subsequent requests.

> **Note:** `revalidatePath` invalidates the cache entries but regeneration happens on the next request. If you want to eagerly regenerate the cache entry immediately instead of waiting for the next request, you can use the Pages router [`res.revalidate`](docs/pages/guides/incremental-static-regeneration#on-demand-validation-with-resrevalidate) method. We're working on adding new methods to provide eager regeneration capabilities for the App Router.

```ts filename="app/actions.ts" switcher
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost() {
  // Invalidate the cache for the /posts route
  revalidatePath('/posts')
}
```

```js filename="app/actions.js" switcher
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost() {
  // Invalidate the cache for the /posts route
  revalidatePath('/posts')
}
```

[View a demo](https://on-demand-isr.vercel.app) and [explore the source code](https://github.com/vercel/on-demand-isr).

### On-demand revalidation with `revalidateTag`

For most use cases, prefer revalidating entire paths. If you need more granular control, you can use the `revalidateTag` function. For example, you can tag individual `fetch` calls:

```tsx filename="app/blog/page.tsx" switcher
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog', {
    next: { tags: ['posts'] },
  })
  const posts = await data.json()
  // ...
}
```

```jsx filename="app/blog/page.js" switcher
export default async function Page() {
  const data = await fetch('https://api.vercel.app/blog', {
    next: { tags: ['posts'] },
  })
  const posts = await data.json()
  // ...
}
```

If you are using an ORM or connecting to a database, you can use `unstable_cache`:

```tsx filename="app/blog/page.tsx" switcher
import { unstable_cache } from 'next/cache'
import { db, posts } from '@/lib/db'

const getCachedPosts = unstable_cache(
  async () => {
    return await db.select().from(posts)
  },
  ['posts'],
  { revalidate: 3600, tags: ['posts'] }
)

export default async function Page() {
  const posts = getCachedPosts()
  // ...
}
```

```jsx filename="app/blog/page.js" switcher
import { unstable_cache } from 'next/cache'
import { db, posts } from '@/lib/db'

const getCachedPosts = unstable_cache(
  async () => {
    return await db.select().from(posts)
  },
  ['posts'],
  { revalidate: 3600, tags: ['posts'] }
)

export default async function Page() {
  const posts = getCachedPosts()
  // ...
}
```

You can then use `revalidateTag` in a [Server Actions](/docs/app/getting-started/updating-data.md) or [Route Handler](/docs/app/api-reference/file-conventions/route.md):

```ts filename="app/actions.ts" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function createPost() {
  // Invalidate all data tagged with 'posts'
  revalidateTag('posts')
}
```

```js filename="app/actions.js" switcher
'use server'

import { revalidateTag } from 'next/cache'

export async function createPost() {
  // Invalidate all data tagged with 'posts'
  revalidateTag('posts')
}
```

### Handling uncaught exceptions

If an error is thrown while attempting to revalidate data, the last successfully generated data will continue to be served from the cache. On the next subsequent request, Next.js will retry revalidating the data. [Learn more about error handling](/docs/app/getting-started/error-handling.md).

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
* If you have multiple `fetch` requests in a statically rendered route, and each has a different `revalidate` frequency, the lowest time will be used for ISR. However, those revalidate frequencies will still be respected by the [Data Cache](/docs/app/guides/caching.md#data-cache).
* If any of the `fetch` requests used on a route have a `revalidate` time of `0`, or an explicit `no-store`, the route will be [dynamically rendered](/docs/app/guides/caching.md#dynamic-rendering).
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
source: "https://nextjs.org/docs/app/guides/instrumentation"
--------------------------------------------------------------------------------

# Instrumentation

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
title: "Internationalization"
description: "Add support for multiple languages with internationalized routing and localized content."
source: "https://nextjs.org/docs/app/guides/internationalization"
--------------------------------------------------------------------------------

# Internationalization

Next.js enables you to configure the routing and rendering of content to support multiple languages. Making your site adaptive to different locales includes translated content (localization) and internationalized routes.

## Terminology

* **Locale:** An identifier for a set of language and formatting preferences. This usually includes the preferred language of the user and possibly their geographic region.
  * `en-US`: English as spoken in the United States
  * `nl-NL`: Dutch as spoken in the Netherlands
  * `nl`: Dutch, no specific region

## Routing Overview

It’s recommended to use the user’s language preferences in the browser to select which locale to use. Changing your preferred language will modify the incoming `Accept-Language` header to your application.

For example, using the following libraries, you can look at an incoming `Request` to determine which locale to select, based on the `Headers`, locales you plan to support, and the default locale.

```js filename="proxy.js"
import { match } from '@formatjs/intl-localematcher'
import Negotiator from 'negotiator'

let headers = { 'accept-language': 'en-US,en;q=0.5' }
let languages = new Negotiator({ headers }).languages()
let locales = ['en-US', 'nl-NL', 'nl']
let defaultLocale = 'en-US'

match(languages, locales, defaultLocale) // -> 'en-US'
```

Routing can be internationalized by either the sub-path (`/fr/products`) or domain (`my-site.fr/products`). With this information, you can now redirect the user based on the locale inside [Proxy](/docs/app/api-reference/file-conventions/proxy.md).

```js filename="proxy.js"
import { NextResponse } from "next/server";

let locales = ['en-US', 'nl-NL', 'nl']

// Get the preferred locale, similar to the above or using a library
function getLocale(request) { ... }

export function proxy(request) {
  // Check if there is any supported locale in the pathname
  const { pathname } = request.nextUrl
  const pathnameHasLocale = locales.some(
    (locale) => pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
  )

  if (pathnameHasLocale) return

  // Redirect if there is no locale
  const locale = getLocale(request)
  request.nextUrl.pathname = `/${locale}${pathname}`
  // e.g. incoming request is /products
  // The new URL is now /en-US/products
  return NextResponse.redirect(request.nextUrl)
}

export const config = {
  matcher: [
    // Skip all internal paths (_next)
    '/((?!_next).*)',
    // Optional: only run on root (/) URL
    // '/'
  ],
}
```

Finally, ensure all special files inside `app/` are nested under `app/[lang]`. This enables the Next.js router to dynamically handle different locales in the route, and forward the `lang` parameter to every layout and page. For example:

```tsx filename="app/[lang]/page.tsx" switcher
// You now have access to the current locale
// e.g. /en-US/products -> `lang` is "en-US"
export default async function Page({
  params,
}: {
  params: Promise<{ lang: string }>
}) {
  const { lang } = await params
  return ...
}
```

```jsx filename="app/[lang]/page.js" switcher
// You now have access to the current locale
// e.g. /en-US/products -> `lang` is "en-US"
export default async function Page({ params }) {
  const { lang } = await params
  return ...
}
```

The root layout can also be nested in the new folder (e.g. `app/[lang]/layout.js`).

## Localization

Changing displayed content based on the user’s preferred locale, or localization, is not something specific to Next.js. The patterns described below would work the same with any web application.

Let’s assume we want to support both English and Dutch content inside our application. We might maintain two different “dictionaries”, which are objects that give us a mapping from some key to a localized string. For example:

```json filename="dictionaries/en.json"
{
  "products": {
    "cart": "Add to Cart"
  }
}
```

```json filename="dictionaries/nl.json"
{
  "products": {
    "cart": "Toevoegen aan Winkelwagen"
  }
}
```

We can then create a `getDictionary` function to load the translations for the requested locale:

```ts filename="app/[lang]/dictionaries.ts" switcher
import 'server-only'

const dictionaries = {
  en: () => import('./dictionaries/en.json').then((module) => module.default),
  nl: () => import('./dictionaries/nl.json').then((module) => module.default),
}

export const getDictionary = async (locale: 'en' | 'nl') =>
  dictionaries[locale]()
```

```js filename="app/[lang]/dictionaries.js" switcher
import 'server-only'

const dictionaries = {
  en: () => import('./dictionaries/en.json').then((module) => module.default),
  nl: () => import('./dictionaries/nl.json').then((module) => module.default),
}

export const getDictionary = async (locale) => dictionaries[locale]()
```

Given the currently selected language, we can fetch the dictionary inside of a layout or page.

```tsx filename="app/[lang]/page.tsx" switcher
import { getDictionary } from './dictionaries'

export default async function Page({
  params,
}: {
  params: Promise<{ lang: 'en' | 'nl' }>
}) {
  const { lang } = await params
  const dict = await getDictionary(lang) // en
  return <button>{dict.products.cart}</button> // Add to Cart
}
```

```jsx filename="app/[lang]/page.js" switcher
import { getDictionary } from './dictionaries'

export default async function Page({ params }) {
  const { lang } = await params
  const dict = await getDictionary(lang) // en
  return <button>{dict.products.cart}</button> // Add to Cart
}
```

Because all layouts and pages in the `app/` directory default to [Server Components](/docs/app/getting-started/server-and-client-components.md), we do not need to worry about the size of the translation files affecting our client-side JavaScript bundle size. This code will **only run on the server**, and only the resulting HTML will be sent to the browser.

## Static Rendering

To generate static routes for a given set of locales, we can use `generateStaticParams` with any page or layout. This can be global, for example, in the root layout:

```tsx filename="app/[lang]/layout.tsx" switcher
export async function generateStaticParams() {
  return [{ lang: 'en-US' }, { lang: 'de' }]
}

export default async function RootLayout({
  children,
  params,
}: Readonly<{
  children: React.ReactNode
  params: Promise<{ lang: 'en-US' | 'de' }>
}>) {
  return (
    <html lang={(await params).lang}>
      <body>{children}</body>
    </html>
  )
}
```

```jsx filename="app/[lang]/layout.js" switcher
export async function generateStaticParams() {
  return [{ lang: 'en-US' }, { lang: 'de' }]
}

export default async function RootLayout({ children, params }) {
  return (
    <html lang={(await params).lang}>
      <body>{children}</body>
    </html>
  )
}
```

## Resources

* [Minimal i18n routing and translations](https://github.com/vercel/next.js/tree/canary/examples/i18n-routing)
* [`next-intl`](https://next-intl.dev)
* [`next-international`](https://github.com/QuiiBz/next-international)
* [`next-i18n-router`](https://github.com/i18nexus/next-i18n-router)
* [`paraglide-next`](https://inlang.com/m/osslbuzt/paraglide-next-i18n)
* [`lingui`](https://lingui.dev)
* [`tolgee`](https://tolgee.io/apps-integrations/next)
* [`next-intlayer`](https://intlayer.org/doc/environment/nextjs)
* [`gt-next`](https://generaltranslation.com/en/docs/next)


--------------------------------------------------------------------------------
title: "How to implement JSON-LD in your Next.js application"
description: "Learn how to add JSON-LD to your Next.js application to describe your content to search engines and AI."
source: "https://nextjs.org/docs/app/guides/json-ld"
--------------------------------------------------------------------------------

# JSON-LD

[JSON-LD](https://json-ld.org/) is a format for structured data that can be used by search engines and AI to help them understand the structure of the page beyond pure content. For example, you can use it to describe a person, an event, an organization, a movie, a book, a recipe, and many other types of entities.

Our current recommendation for JSON-LD is to render structured data as a `<script>` tag in your `layout.js` or `page.js` components.

The following snippet uses `JSON.stringify`, which does not sanitize malicious strings used in XSS injection. To prevent this type of vulnerability, you can scrub `HTML` tags from the `JSON-LD` payload, for example, by replacing the character, `<`, with its unicode equivalent, `\u003c`.

Review your organization's recommended approach to sanitize potentially dangerous strings, or use community maintained alternatives for `JSON.stringify` such as, [serialize-javascript](https://www.npmjs.com/package/serialize-javascript).

```tsx filename="app/products/[id]/page.tsx" switcher
export default async function Page({ params }) {
  const { id } = await params
  const product = await getProduct(id)

  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    image: product.image,
    description: product.description,
  }

  return (
    <section>
      {/* Add JSON-LD to your page */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
        }}
      />
      {/* ... */}
    </section>
  )
}
```

```jsx filename="app/products/[id]/page.js" switcher
export default async function Page({ params }) {
  const { id } = await params
  const product = await getProduct(id)

  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    image: product.image,
    description: product.description,
  }

  return (
    <section>
      {/* Add JSON-LD to your page */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify(jsonLd).replace(/</g, '\\u003c'),
        }}
      />
      {/* ... */}
    </section>
  )
}
```

You can validate and test your structured data with the [Rich Results Test](https://search.google.com/test/rich-results) for Google or the generic [Schema Markup Validator](https://validator.schema.org/).

You can type your JSON-LD with TypeScript using community packages like [`schema-dts`](https://www.npmjs.com/package/schema-dts):

```tsx
import { Product, WithContext } from 'schema-dts'

const jsonLd: WithContext<Product> = {
  '@context': 'https://schema.org',
  '@type': 'Product',
  name: 'Next.js Sticker',
  image: 'https://nextjs.org/imgs/sticker.png',
  description: 'Dynamic at the speed of static.',
}
```


--------------------------------------------------------------------------------
title: "How to lazy load Client Components and libraries"
description: "Lazy load imported libraries and React Components to improve your application's loading performance."
source: "https://nextjs.org/docs/app/guides/lazy-loading"
--------------------------------------------------------------------------------

# Lazy Loading

[Lazy loading](https://developer.mozilla.org/docs/Web/Performance/Lazy_loading) in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.

It allows you to defer loading of **Client Components** and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.

There are two ways you can implement lazy loading in Next.js:

1. Using [Dynamic Imports](#nextdynamic) with `next/dynamic`
2. Using [`React.lazy()`](https://react.dev/reference/react/lazy) with [Suspense](https://react.dev/reference/react/Suspense)

By default, Server Components are automatically [code split](https://developer.mozilla.org/docs/Glossary/Code_splitting), and you can use [streaming](/docs/app/api-reference/file-conventions/loading.md) to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.

## `next/dynamic`

`next/dynamic` is a composite of [`React.lazy()`](https://react.dev/reference/react/lazy) and [Suspense](https://react.dev/reference/react/Suspense). It behaves the same way in the `app` and `pages` directories to allow for incremental migration.

## Examples

### Importing Client Components

```jsx filename="app/page.js"
'use client'

import { useState } from 'react'
import dynamic from 'next/dynamic'

// Client Components:
const ComponentA = dynamic(() => import('../components/A'))
const ComponentB = dynamic(() => import('../components/B'))
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })

export default function ClientComponentExample() {
  const [showMore, setShowMore] = useState(false)

  return (
    <div>
      {/* Load immediately, but in a separate client bundle */}
      <ComponentA />

      {/* Load on demand, only when/if the condition is met */}
      {showMore && <ComponentB />}
      <button onClick={() => setShowMore(!showMore)}>Toggle</button>

      {/* Load only on the client side */}
      <ComponentC />
    </div>
  )
}
```

> **Note:** When a Server Component dynamically imports a Client Component, automatic [code splitting](https://developer.mozilla.org/docs/Glossary/Code_splitting) is currently **not** supported.

### Skipping SSR

When using `React.lazy()` and Suspense, Client Components will be [prerendered](https://github.com/reactwg/server-components/discussions/4) (SSR) by default.

> **Note:** `ssr: false` option will only work for Client Components, move it into Client Components ensure the client code-splitting working properly.

If you want to disable pre-rendering for a Client Component, you can use the `ssr` option set to `false`:

```jsx
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
```

### Importing Server Components

If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself.
It will also help preload the static assets such as CSS when you're using it in Server Components.

```jsx filename="app/page.js"
import dynamic from 'next/dynamic'

// Server Component:
const ServerComponent = dynamic(() => import('../components/ServerComponent'))

export default function ServerComponentExample() {
  return (
    <div>
      <ServerComponent />
    </div>
  )
}
```

> **Note:** `ssr: false` option is not supported in Server Components. You will see an error if you try to use it in Server Components.
> `ssr: false` is not allowed with `next/dynamic` in Server Components. Please move it into a Client Component.

### Loading External Libraries

External libraries can be loaded on demand using the [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) function. This example uses the external library `fuse.js` for fuzzy search. The module is only loaded on the client after the user types in the search input.

```jsx filename="app/page.js"
'use client'

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

### Adding a custom loading component

```jsx filename="app/page.js"
'use client'

import dynamic from 'next/dynamic'

const WithCustomLoading = dynamic(
  () => import('../components/WithCustomLoading'),
  {
    loading: () => <p>Loading...</p>,
  }
)

export default function Page() {
  return (
    <div>
      {/* The loading component will be rendered while  <WithCustomLoading/> is loading */}
      <WithCustomLoading />
    </div>
  )
}
```

### Importing Named Exports

To dynamically import a named export, you can return it from the Promise returned by [`import()`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/import) function:

```jsx filename="components/hello.js"
'use client'

export function Hello() {
  return <p>Hello!</p>
}
```

```jsx filename="app/page.js"
import dynamic from 'next/dynamic'

const ClientComponent = dynamic(() =>
  import('../components/hello').then((mod) => mod.Hello)
)
```


--------------------------------------------------------------------------------
title: "How to optimize your local development environment"
description: "Learn how to optimize your local development environment with Next.js."
source: "https://nextjs.org/docs/app/guides/local-development"
--------------------------------------------------------------------------------

# Development Environment

Next.js is designed to provide a great developer experience. As your application grows, you might notice slower compilation times during local development. This guide will help you identify and fix common compile-time performance issues.

## Local dev vs. production

The development process with `next dev` is different than `next build` and `next start`.

`next dev` compiles routes in your application as you open or navigate to them. This enables you to start the dev server without waiting for every route in your application to compile, which is both faster and uses less memory. Running a production build applies other optimizations, like minifying files and creating content hashes, which are not needed for local development.

## Improving local dev performance

### 1. Check your computer's antivirus

Antivirus software can slow down file access. While this is more common on Windows machines, this can be an issue for any system with an antivirus tool installed.

On Windows, you can add your project to the [Microsoft Defender Antivirus exclusion list](https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e#bkmk_threat-protection-settings).

1. Open the **"Windows Security"** application and then select **"Virus & threat protection"** → **"Manage settings"** → **"Add or remove exclusions"**.
2. Add a **"Folder"** exclusion. Select your project folder.

On macOS, you can disable [Gatekeeper](https://support.apple.com/guide/security/gatekeeper-and-runtime-protection-sec5599b66df/web) inside of your terminal.

1. Run `sudo spctl developer-mode enable-terminal` in your terminal.
2. Open the **"System Settings"** app and then select **"Privacy & Security"** → **"Developer Tools"**.
3. Ensure your terminal is listed and enabled. If you're using a third-party terminal like iTerm or Ghostty, add that to the list.
4. Restart your terminal.

![Screenshot of macOS System Settings showing the Privacy & Security pane](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/macos-gatekeeper-privacy-and-security.png)

![Screenshot of macOS System Settings showing the Developer Tools options](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/macos-gatekeeper-developer-tools.png)

If you or your employer have configured any other Antivirus solutions on your system, you should inspect the relevant settings for those products.

### 2. Update Next.js and use Turbopack

Make sure you're using the latest version of Next.js. Each new version often includes performance improvements.

Turbopack is now the default bundler for Next.js development and provides significant performance improvements over webpack.

```bash
npm install next@latest
npm run dev  # Turbopack is used by default
```

If you need to use Webpack instead of Turbopack, you can opt-in:

```bash
npm run dev --webpack
```

[Learn more about Turbopack](/blog/turbopack-for-development-stable). See our [upgrade guides](/docs/app/guides/upgrading.md) and codemods for more information.

### 3. Check your imports

The way you import code can greatly affect compilation and bundling time. Learn more about [optimizing package bundling](/docs/app/guides/package-bundling.md) and explore tools like [Dependency Cruiser](https://github.com/sverweij/dependency-cruiser) or [Madge](https://github.com/pahen/madge).

#### Icon libraries

Libraries like `@material-ui/icons`, `@phosphor-icons/react`, or `react-icons` can import thousands of icons, even if you only use a few. Try to import only the icons you need:

```jsx
// Instead of this:
import { TriangleIcon } from '@phosphor-icons/react'

// Do this:
import { TriangleIcon } from '@phosphor-icons/react/dist/csr/Triangle'
```

You can often find what import pattern to use in the documentation for the icon library you're using. This example follows [`@phosphor-icons/react`](https://www.npmjs.com/package/@phosphor-icons/react#import-performance-optimization) recommendation.

Libraries like `react-icons` includes many different icon sets. Choose one set and stick with that set.

For example, if your application uses `react-icons` and imports all of these:

* `pi` (Phosphor Icons)
* `md` (Material Design Icons)
* `tb` (tabler-icons)
* `cg` (cssgg)

Combined they will be tens of thousands of modules that the compiler has to handle, even if you only use a single import from each.

#### Barrel files

"Barrel files" are files that export many items from other files. They can slow down builds because the compiler has to parse them to find if there are side-effects in the module scope by using the import.

Try to import directly from specific files when possible. [Learn more about barrel files](https://vercel.com/blog/how-we-optimized-package-imports-in-next-js) and the built-in optimizations in Next.js.

#### Optimize package imports

Next.js can automatically optimize imports for certain packages. If you are using packages that utilize barrel files, add them to your `next.config.js`:

```jsx
module.exports = {
  experimental: {
    optimizePackageImports: ['package-name'],
  },
}
```

Turbopack automatically analyzes imports and optimizes them. It does not require this configuration.

### 4. Check your Tailwind CSS setup

If you're using Tailwind CSS, make sure it's set up correctly.

A common mistake is configuring your `content` array in a way which includes `node_modules` or other large directories of files that should not be scanned.

Tailwind CSS version 3.4.8 or newer will warn you about settings that might slow down your build.

1. In your `tailwind.config.js`, be specific about which files to scan:

   ```jsx
   module.exports = {
     content: [
       './src/**/*.{js,ts,jsx,tsx}', // Good
       // This might be too broad
       // It will match `packages/**/node_modules` too
       // '../../packages/**/*.{js,ts,jsx,tsx}',
     ],
   }
   ```

2. Avoid scanning unnecessary files:

   ```jsx
   module.exports = {
     content: [
       // Better - only scans the 'src' folder
       '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
     ],
   }
   ```

### 5. Check custom webpack settings

If you've added custom webpack settings, they might be slowing down compilation.

Consider if you really need them for local development. You can optionally only include certain tools for production builds, or explore using the default Turbopack bundler and configuring [loaders](/docs/app/api-reference/config/next-config-js/turbopack.md#configuring-webpack-loaders) instead.

### 6. Optimize memory usage

If your app is very large, it might need more memory.

[Learn more about optimizing memory usage](/docs/app/guides/memory-usage.md).

### 7. Server Components and data fetching

Changes to Server Components cause the entire page to re-render locally in order to show the new changes, which includes fetching new data for the component.

The experimental `serverComponentsHmrCache` option allows you to cache `fetch` responses in Server Components across Hot Module Replacement (HMR) refreshes in local development. This results in faster responses and reduced costs for billed API calls.

[Learn more about the experimental option](/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache.md).

### 8. Consider local development over Docker

If you're using Docker for development on Mac or Windows, you may experience significantly slower performance compared to running Next.js locally.

Docker's filesystem access on Mac and Windows can cause Hot Module Replacement (HMR) to take seconds or even minutes, while the same application runs with fast HMR when developed locally.

This performance difference is due to how Docker handles filesystem operations outside of Linux environments. For the best development experience:

* Use local development (`npm run dev` or `pnpm dev`) instead of Docker during development
* Reserve Docker for production deployments and testing production builds
* If you must use Docker for development, consider using Docker on a Linux machine or VM

[Learn more about Docker deployment](/docs/app/getting-started/deploying.md#docker) for production use.

## Tools for finding problems

### Detailed fetch logging

Use the `logging.fetches` option in your `next.config.js` file, to see more detailed information about what's happening during development:

```js
module.exports = {
  logging: {
    fetches: {
      fullUrl: true,
    },
  },
}
```

[Learn more about fetch logging](/docs/app/api-reference/config/next-config-js/logging.md).

### Turbopack tracing

Turbopack tracing is a tool that helps you understand the performance of your application during local development.
It provides detailed information about the time taken for each module to compile and how they are related.

1. Make sure you have the latest version of Next.js installed.

2. Generate a Turbopack trace file:

   ```bash
   NEXT_TURBOPACK_TRACING=1 npm run dev
   ```

3. Navigate around your application or make edits to files to reproduce the problem.

4. Stop the Next.js development server.

5. A file called `trace-turbopack` will be available in the `.next/dev` folder.

6. You can interpret the file using `npx next internal trace [path-to-file]`:

   ```bash
   npx next internal trace .next/dev/trace-turbopack
   ```

   On versions where `trace` is not available, the command was named `turbo-trace-server`:

   ```bash
   npx next internal turbo-trace-server .next/dev/trace-turbopack
   ```

7. Once the trace server is running you can view the trace at https://trace.nextjs.org/.

8. By default the trace viewer will aggregate timings, in order to see each individual time you can switch from "Aggregated in order" to "Spans in order" at the top right of the viewer.

> **Good to know**: The trace file is place under the development server directory, which defaults to `.next/dev`. This is controllable using the [`isolatedDevBuild`](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md) flag in your Next config file.

### Still having problems?

Share the trace file generated in the [Turbopack Tracing](#turbopack-tracing) section and share it on [GitHub Discussions](https://github.com/vercel/next.js/discussions) or [Discord](https://nextjs.org/discord).


--------------------------------------------------------------------------------
title: "Enabling Next.js MCP Server for Coding Agents"
description: "Learn how to use Next.js MCP support to allow coding agents access to your application state"
source: "https://nextjs.org/docs/app/guides/mcp"
--------------------------------------------------------------------------------

# Next.js MCP Server

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open standard that allows AI agents and coding assistants to interact with your applications through a standardized interface.

Next.js 16+ includes MCP support that enables coding agents to access your application's internals in real-time. To use this functionality, install the [`next-devtools-mcp`](https://www.npmjs.com/package/next-devtools-mcp) package.

## Getting started

**Requirements:** Next.js 16 or above

Add `next-devtools-mcp` to the `.mcp.json` file at the root of your project:

```json filename=".mcp.json"
{
  "mcpServers": {
    "next-devtools": {
      "command": "npx",
      "args": ["-y", "next-devtools-mcp@latest"]
    }
  }
}
```

That's it! When you start your development server, `next-devtools-mcp` will automatically discover and connect to your running Next.js instance.

For more configuration options, see the [next-devtools-mcp repository](https://github.com/vercel/next-devtools-mcp).

## Capabilities

`next-devtools-mcp` provides coding agents with a growing set of capabilities:

### Application Runtime Access

* **Error Detection**: Retrieve current build errors, runtime errors, and type errors from your dev server
* **Live State Queries**: Access real-time application state and runtime information
* **Page Metadata**: Query page routes, components, and rendering details
* **Server Actions**: Inspect Server Actions and component hierarchies
* **Development Logs**: Access development server logs and console output

### Development Tools

* **Next.js Knowledge Base**: Query comprehensive Next.js documentation and best practices
* **Migration and Upgrade Tools**: Automated helpers for upgrading to Next.js 16 with codemods
* **Cache Components Guide**: Setup and configuration assistance for Cache Components
* **Browser Testing**: [Playwright MCP](https://github.com/microsoft/playwright-mcp) integration for verifying pages in the browser

> **Note:** The Next.js team is actively expanding these capabilities. New tools and features are added regularly to improve the agent development experience.

## Development workflow

1. Start your Next.js development server:

```bash filename="Terminal"
npm run dev
```

2. Your Coding Agent will automatically connect to the running Next.js instance via `next-devtools-mcp`

3. Open your application in the browser to view pages

4. Query your agent for insights and diagnostics (see examples below)

### Available tools

Through `next-devtools-mcp`, agents can use the following tools:

* **`get_errors`**: Retrieve current build errors, runtime errors, and type errors from your dev server
* **`get_logs`**: Get the path to the development log file containing browser console logs and server output
* **`get_page_metadata`**: Get metadata about specific pages including routes, components, and rendering information
* **`get_project_metadata`**: Retrieve project structure, configuration, and dev server URL
* **`get_server_action_by_id`**: Look up Server Actions by their ID to find the source file and function name

## Using with agents

MCP-compatible Coding Agents can automatically discover and connect to your Next.js development server, providing them with rich context about your project.

### Benefits for agent-assisted development

Agents can:

* **Make context-aware suggestions**: Recommend the right place to add new features based on your existing structure
* **Query live application state**: Check current configuration, routes, and middleware during development
* **Understand your app router pages layout**: Know exactly which page and layout are rendered
* **Provide accurate implementations**: Generate code that follows your project's patterns and conventions

## Examples

### Error detection and diagnosis

Ask your agent about errors in real-time:

```bash
User: "What errors are currently in my application?"
```

The agent will:

* Query your running Next.js application via `next-devtools-mcp`
* Retrieve current build errors, runtime errors, and type errors
* Analyze the errors and provide actionable fixes

<details>
<summary>Agent response (click to expand)</summary>

```bash
> fix errors on the page

⏺ I'll help you fix the errors on the page. Let me first check what errors exist by looking at the
  current state of the project.

⏺ next-devtools - nextjs_runtime (MCP)(action: "discover_servers")
⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")

⏺ I found a hydration error on the /about page. The error shows that the server is rendering
  "server" but the client is rendering "client", causing a mismatch. Let me create a todo list and fix
   this issue.

⏺ Perfect! Now let me check for errors on the page.           01:14 PM  claude-sonnet-4-5-20250929

⏺ next-devtools - nextjs_runtime (MCP)(action: "call_tool", toolName: "get_errors")
  ⎿ {
      "success": true,
      "port": 3000,
      "toolName": "get_errors",
      "result": {
        "content": [
          {
            "type": "text",
            "text": "# Found errors in 1 browser session(s)\n\n## Session: /about\n\n**1 error(s)
     found**\n\n### Runtime Errors\n\n#### Error 1 (Type: recoverable)\n\n**Error**: Hydration failed
```

</details>

### Upgrading and best practices

Get help with Next.js concepts and migrations:

```bash
User: "Help me upgrade my Next.js app to version 16"
```

The agent will analyze your current version, guide you through automated migrations with codemods, and provide step-by-step instructions for handling breaking changes.

Ask conceptual questions:

```bash
User: "When should I use 'use client' in App Router?"
```

The agent will query the Next.js knowledge base and provide documentation-backed explanations with examples from your codebase.

## How it works

Next.js 16+ includes a built-in MCP endpoint at `/_next/mcp` that runs within your development server. The `next-devtools-mcp` package automatically discovers and communicates with these endpoints, allowing it to:

* Connect to multiple Next.js instances running on different ports
* Forward tool calls to the appropriate Next.js dev server
* Provide a unified interface for coding agents

This architecture decouples the agent interface from the internal implementation, enabling `next-devtools-mcp` to work seamlessly across different Next.js projects.

## Troubleshooting

### MCP server not connecting

* Ensure you're using Next.js v16 or above
* Verify `next-devtools-mcp` is configured in your `.mcp.json`
* Start your development server: `npm run dev`
* Restart your development server if it was already running
* Check that your coding agent has loaded the MCP server configuration


--------------------------------------------------------------------------------
title: "How to use markdown and MDX in Next.js"
description: "Learn how to configure MDX and use it in your Next.js apps."
source: "https://nextjs.org/docs/app/guides/mdx"
--------------------------------------------------------------------------------

# MDX

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

In App Router apps, that includes being able to use [metadata](/docs/app/getting-started/metadata-and-og-images.md).

Create a new MDX page within the `/app` directory:

```txt
  my-project
  ├── app
  │   └── mdx-page
  │       └── page.(mdx/md)
  |── mdx-components.(tsx/js)
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

Create a new page within the `/app` directory and an MDX file wherever you'd like:

```txt
  .
  ├── app/
  │   └── mdx-page/
  │       └── page.(tsx/js)
  ├── markdown/
  │   └── welcome.(mdx/md)
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

```tsx filename="app/mdx-page/page.tsx" switcher
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

```jsx filename="app/mdx-page/page.js" switcher
import Welcome from '@/markdown/welcome.mdx'

export default function Page() {
  return <Welcome />
}
```

Navigating to the `/mdx-page` route should display your rendered MDX page.

### Using dynamic imports

You can import dynamic MDX components instead of using filesystem routing for MDX files.

For example, you can have a dynamic route segment which loads MDX components from a separate directory:

![Route segments for dynamic MDX components](https://h8DxKfmAPhn8O0p3.public.blob.vercel-storage.com/docs/light/mdx-files.png)

[`generateStaticParams`](/docs/app/api-reference/functions/generate-static-params.md) can be used to prerender the provided routes. By marking `dynamicParams` as `false`, accessing a route not defined in `generateStaticParams` will 404.

```tsx filename="app/blog/[slug]/page.tsx" switcher
export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const { default: Post } = await import(`@/content/${slug}.mdx`)

  return <Post />
}

export function generateStaticParams() {
  return [{ slug: 'welcome' }, { slug: 'about' }]
}

export const dynamicParams = false
```

```jsx filename="app/blog/[slug]/page.js" switcher
export default async function Page({ params }) {
  const { slug } = await params
  const { default: Post } = await import(`@/content/${slug}.mdx`)

  return <Post />
}

export function generateStaticParams() {
  return [{ slug: 'welcome' }, { slug: 'about' }]
}

export const dynamicParams = false
```

> **Good to know**: Ensure you specify the `.mdx` file extension in your import. While it is not required to use [module path aliases](/docs/app/getting-started/installation.md#set-up-absolute-imports-and-module-path-aliases) (e.g., `@/content`), it does simplify your import path.

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

```tsx filename="app/mdx-page/page.tsx" switcher
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

```jsx filename="app/mdx-page/page.js" switcher
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

To share a layout across MDX pages, you can use the [built-in layouts support](/docs/app/api-reference/file-conventions/layout.md) with the App Router.

```tsx filename="app/mdx-page/layout.tsx" switcher
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return <div style={{ color: 'blue' }}>{children}</div>
}
```

```jsx filename="app/mdx-page/layout.js" switcher
export default function MdxLayout({ children }) {
  // Create any shared layout or styles here
  return <div style={{ color: 'blue' }}>{children}</div>
}
```

### Using Tailwind typography plugin

If you are using [Tailwind](https://tailwindcss.com) to style your application, using the [`@tailwindcss/typography` plugin](https://tailwindcss.com/docs/plugins#typography) will allow you to reuse your Tailwind configuration and styles in your markdown files.

The plugin adds a set of `prose` classes that can be used to add typographic styles to content blocks that come from sources, like markdown.

[Install Tailwind typography](https://github.com/tailwindlabs/tailwindcss-typography?tab=readme-ov-file#installation) and use with [shared layouts](#shared-layouts) to add the `prose` you want.

```tsx filename="app/mdx-page/layout.tsx" switcher
export default function MdxLayout({ children }: { children: React.ReactNode }) {
  // Create any shared layout or styles here
  return (
    <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
      {children}
    </div>
  )
}
```

```jsx filename="app/mdx-page/layout.js" switcher
export default function MdxLayout({ children }) {
  // Create any shared layout or styles here
  return (
    <div className="prose prose-headings:mt-8 prose-headings:font-semibold prose-headings:text-black prose-h1:text-5xl prose-h2:text-4xl prose-h3:text-3xl prose-h4:text-2xl prose-h5:text-xl prose-h6:text-lg dark:prose-headings:text-white">
      {children}
    </div>
  )
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

```tsx filename="app/blog/page.tsx" switcher
import BlogPost, { metadata } from '@/content/blog-post.mdx'

export default function Page() {
  console.log('metadata: ', metadata)
  //=> { author: 'John Doe' }
  return <BlogPost />
}
```

```jsx filename="app/blog/page.js" switcher
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

```tsx filename="app/mdx-page-remote/page.tsx" switcher
import { MDXRemote } from 'next-mdx-remote-client/rsc'

export default async function RemoteMdxPage() {
  // MDX text - can be from a database, CMS, fetch, anywhere...
  const res = await fetch('https://...')
  const markdown = await res.text()
  return <MDXRemote source={markdown} />
}
```

```jsx filename="app/mdx-page-remote/page.js" switcher
import { MDXRemote } from 'next-mdx-remote-client/rsc'

export default async function RemoteMdxPage() {
  // MDX text - can be from a database, CMS, fetch, anywhere...
  const res = await fetch('https://...')
  const markdown = await res.text()
  return <MDXRemote source={markdown} />
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
title: "How to optimize memory usage"
description: "Optimize memory used by your application in development and production."
source: "https://nextjs.org/docs/app/guides/memory-usage"
--------------------------------------------------------------------------------

# Memory Usage

As applications grow and become more feature rich, they can demand more resources when developing locally or creating production builds.

Let's explore some strategies and techniques to optimize memory and address common memory issues in Next.js.

## Reduce number of dependencies

Applications with a large amount of dependencies will use more memory.

The [Bundle Analyzer](/docs/app/guides/package-bundling.md) can help you investigate large dependencies in your application that may be able to be removed to improve performance and memory usage.

## Try `experimental.webpackMemoryOptimizations`

Starting in `v15.0.0`, you can add `experimental.webpackMemoryOptimizations: true` to your `next.config.js` file to change behavior in Webpack that reduces max memory usage but may increase compilation times by a slight amount.

> **Good to know**: This feature is currently experimental to test on more projects first, but it is considered to be low-risk.

## Run `next build` with `--experimental-debug-memory-usage`

Starting in `14.2.0`, you can run `next build --experimental-debug-memory-usage` to run the build in a mode where Next.js will print out information about memory usage continuously throughout the build, such as heap usage and garbage collection statistics. Heap snapshots will also be taken automatically when memory usage gets close to the configured limit.

> **Good to know**: This feature is not compatible with the Webpack build worker option which is auto-enabled unless you have custom webpack config.

## Record a heap profile

To look for memory issues, you can record a heap profile from Node.js and load it in Chrome DevTools to identify potential sources of memory leaks.

In your terminal, pass the `--heap-prof` flag to Node.js when starting your Next.js build:

```sh
node --heap-prof node_modules/next/dist/bin/next build
```

At the end of the build, a `.heapprofile` file will be created by Node.js.

In Chrome DevTools, you can open the Memory tab and click on the "Load Profile" button to visualize the file.

## Analyze a snapshot of the heap

You can use an inspector tool to analyze the memory usage of the application.

When running the `next build` or `next dev` command, add `NODE_OPTIONS=--inspect` to the beginning of the command. This will expose the inspector agent on the default port.
If you wish to break before any user code starts, you can pass `--inspect-brk` instead. While the process is running, you can use a tool such as Chrome DevTools to connect to the debugging port to record and analyze a snapshot of the heap to see what memory is being retained.

Starting in `14.2.0`, you can also run `next build` with the `--experimental-debug-memory-usage` flag to make it easier to take heap snapshots.

While running in this mode, you can send a `SIGUSR2` signal to the process at any point, and the process will take a heap snapshot.

The heap snapshot will be saved to the project root of the Next.js application and can be loaded in any heap analyzer, such as Chrome DevTools, to see what memory is retained. This mode is not yet compatible with Webpack build workers.

See [how to record and analyze heap snapshots](https://developer.chrome.com/docs/devtools/memory-problems/heap-snapshots) for more information.

## Webpack build worker

The Webpack build worker allows you to run Webpack compilations inside a separate Node.js worker which will decrease memory usage of your application during builds.

This option is enabled by default if your application does not have a custom Webpack configuration starting in `v14.1.0`.

If you are using an older version of Next.js or you have a custom Webpack configuration, you can enable this option by setting `experimental.webpackBuildWorker: true` inside your `next.config.js`.

> **Good to know**: This feature may not be compatible with all custom Webpack plugins.

## Disable Webpack cache

The [Webpack cache](https://webpack.js.org/configuration/cache/) saves generated Webpack modules in memory and/or to disk to improve the speed of builds. This can
help with performance, but it will also increase the memory usage of your application to store the cached data.

You can disable this behavior by adding a [custom Webpack configuration](/docs/app/api-reference/config/next-config-js/webpack.md) to your application:

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (
    config,
    { buildId, dev, isServer, defaultLoaders, nextRuntime, webpack }
  ) => {
    if (config.cache && !dev) {
      config.cache = Object.freeze({
        type: 'memory',
      })
    }
    // Important: return the modified config
    return config
  },
}

export default nextConfig
```

## Disable static analysis

Typechecking may require a lot of memory, especially in large projects.
However, most projects have a dedicated CI runner that already handles these tasks.
When the build produces out-of-memory issues during the "Running TypeScript" step, you can disable this task during builds:

```js filename="next.config.mjs"
/** @type {import('next').NextConfig} */
const nextConfig = {
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

* [Ignoring TypeScript Errors](/docs/app/api-reference/config/typescript.md#disabling-typescript-errors-in-production)

Keep in mind that this may produce faulty deploys due to type errors.
We strongly recommend only promoting builds to production after static analysis has completed.
If you deploy to Vercel, you can check out the [guide for staging deployments](https://vercel.com/docs/deployments/managing-deployments#staging-and-promoting-a-production-deployment) to learn how to promote builds to production after custom tasks have succeeded.

## Disable source maps

Generating source maps consumes extra memory during the build process.

You can disable source map generation by adding `productionBrowserSourceMaps: false` and `experimental.serverSourceMaps: false` to your Next.js configuration.

When using the `cacheComponents` feature, Next.js will use source maps by default during the prerender phase of `next build`.
If you consistently encounter memory issues during that phase (after "Generating static pages"),
you can try disabling source maps in that phase by adding `enablePrerenderSourceMaps: false` to your Next.js configuration.

> **Good to know**: Some plugins may turn on source maps and may require custom configuration to disable.

## Edge memory issues

Next.js `v14.1.3` fixed a memory issue when using the Edge runtime. Please update to this version (or later) to see if it addresses your issue.

## Preloading Entries

When the Next.js server starts, it preloads each page's JavaScript modules into memory, rather than at request time.

This optimization allows for faster response times, in exchange for a larger initial memory footprint.

To disable this optimization, set the `experimental.preloadEntriesOnStart` flag to `false`.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  experimental: {
    preloadEntriesOnStart: false,
  },
}

export default config
```

```js filename="next.config.mjs" switcher
/** @type {import('next').NextConfig} */
const config = {
  experimental: {
    preloadEntriesOnStart: false,
  },
}

export default config
```

Next.js doesn't unload these JavaScript modules, meaning that even with this optimization disabled, the memory footprint of your Next.js server will eventually be the same if all pages are eventually requested.


--------------------------------------------------------------------------------
title: "Migrating"
description: "Learn how to migrate from popular frameworks to Next.js"
source: "https://nextjs.org/docs/app/guides/migrating"
--------------------------------------------------------------------------------

# Migrating



 - [App Router](/docs/app/guides/migrating/app-router-migration.md)
 - [Create React App](/docs/app/guides/migrating/from-create-react-app.md)
 - [Vite](/docs/app/guides/migrating/from-vite.md)

--------------------------------------------------------------------------------
title: "How to migrate from Pages to the App Router"
description: "Learn how to upgrade your existing Next.js application from the Pages Router to the App Router."
source: "https://nextjs.org/docs/app/guides/migrating/app-router-migration"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./02-image-optimization.md) | [Index](./index.md) | [Next →](./04-app-router.md)
