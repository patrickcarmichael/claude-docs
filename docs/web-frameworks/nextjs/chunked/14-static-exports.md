**Navigation:** [← Previous](./13-app-router.md) | [Index](./index.md) | [Next →](./15-getstaticprops.md)

---

# Static Exports

@router: Pages Router

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

You can utilize [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) and [`getStaticPaths`](/docs/pages/building-your-application/data-fetching/get-static-paths.md) to generate an HTML file for each page in your `pages` directory (or more for [dynamic routes](/docs/app/api-reference/file-conventions/dynamic-routes.md)).

## Supported Features

The majority of core Next.js features needed to build a static site are supported, including:

* [Dynamic Routes when using `getStaticPaths`](/docs/app/api-reference/file-conventions/dynamic-routes.md)
* Prefetching with `next/link`
* Preloading JavaScript
* [Dynamic Imports](/docs/pages/guides/lazy-loading.md)
* Any styling options (e.g. CSS Modules, styled-jsx)
* [Client-side data fetching](/docs/pages/building-your-application/data-fetching/client-side.md)
* [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md)
* [`getStaticPaths`](/docs/pages/building-your-application/data-fetching/get-static-paths.md)

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

## Unsupported Features

Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are **not** supported:

* [Internationalized Routing](/docs/pages/guides/internationalization.md)
* [API Routes](/docs/pages/building-your-application/routing/api-routes.md)
* [Rewrites](/docs/pages/api-reference/config/next-config-js/rewrites.md)
* [Redirects](/docs/pages/api-reference/config/next-config-js/redirects.md)
* [Headers](/docs/pages/api-reference/config/next-config-js/headers.md)
* [Proxy](/docs/pages/api-reference/file-conventions/proxy.md)
* [Incremental Static Regeneration](/docs/pages/guides/incremental-static-regeneration.md)
* [Image Optimization](/docs/pages/api-reference/components/image.md) with the default `loader`
* [Draft Mode](/docs/pages/guides/draft-mode.md)
* [`getStaticPaths` with `fallback: true`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-true)
* [`getStaticPaths` with `fallback: 'blocking'`](/docs/pages/api-reference/functions/get-static-paths.md#fallback-blocking)
* [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md)

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
source: "https://nextjs.org/docs/pages/guides/tailwind-v3-css"
--------------------------------------------------------------------------------

# Tailwind CSS

@router: Pages Router

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
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Add the Tailwind directives to your global CSS file:

```css filename="styles/globals.css"
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Import the CSS file in your `pages/_app.js` file:

```jsx filename="pages/_app.js"
import '@/styles/globals.css'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

## Using classes

After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.

```tsx filename="pages/index.tsx" switcher
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

```jsx filename="pages/index.js" switcher
export default function Page() {
  return <h1 className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

## Usage with Turbopack

As of Next.js 13.1, Tailwind CSS and PostCSS are supported with [Turbopack](https://turbo.build/pack/docs/features/css#tailwind-css).


--------------------------------------------------------------------------------
title: "Testing"
description: "Learn how to set up Next.js with four commonly used testing tools — Cypress, Playwright, Vitest, and Jest."
source: "https://nextjs.org/docs/pages/guides/testing"
--------------------------------------------------------------------------------

# Testing

@router: Pages Router

In React and Next.js, there are a few different types of tests you can write, each with its own purpose and use cases. This page provides an overview of types and commonly used tools you can use to test your application.

## Types of tests

* **Unit Testing** involves testing individual units (or blocks of code) in isolation. In React, a unit can be a single function, hook, or component.
  * **Component Testing** is a more focused version of unit testing where the primary subject of the tests is React components. This may involve testing how components are rendered, their interaction with props, and their behavior in response to user events.
  * **Integration Testing** involves testing how multiple units work together. This can be a combination of components, hooks, and functions.
* **End-to-End (E2E) Testing** involves testing user flows in an environment that simulates real user scenarios, like the browser. This means testing specific tasks (e.g. signup flow) in a production-like environment.
* **Snapshot Testing** involves capturing the rendered output of a component and saving it to a snapshot file. When tests run, the current rendered output of the component is compared against the saved snapshot. Changes in the snapshot are used to indicate unexpected changes in behavior.

## Guides

See the guides below to learn how to set up Next.js with these commonly used testing tools:

 - [Cypress](/docs/pages/guides/testing/cypress.md)
 - [Jest](/docs/pages/guides/testing/jest.md)
 - [Playwright](/docs/pages/guides/testing/playwright.md)
 - [Vitest](/docs/pages/guides/testing/vitest.md)

--------------------------------------------------------------------------------
title: "How to set up Cypress with Next.js"
description: "Learn how to set up Cypress with Next.js for End-to-End (E2E) and Component Testing."
source: "https://nextjs.org/docs/pages/guides/testing/cypress"
--------------------------------------------------------------------------------

# Cypress

@router: Pages Router

[Cypress](https://www.cypress.io/) is a test runner used for **End-to-End (E2E)** and **Component Testing**. This page will show you how to set up Cypress with Next.js and write your first tests.

> **Warning:**
>
> * Cypress versions below 13.6.3 do not support [TypeScript version 5](https://github.com/cypress-io/cypress/issues/27731) with `moduleResolution:"bundler"`. However, this issue has been resolved in Cypress version 13.6.3 and later. [cypress v13.6.3](https://docs.cypress.io/guides/references/changelog#13-6-3)

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

```jsx filename="pages/index.js"
import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```jsx filename="pages/about.js"
import Link from 'next/link'

export default function About() {
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

```jsx filename="cypress/component/about.cy.js"
import AboutPage from '../../pages/about'

describe('<AboutPage />', () => {
  it('should render and display expected content', () => {
    // Mount the React component for the About page
    cy.mount(<AboutPage />)

    // The new page should contain an h1 with "About page"
    cy.get('h1').contains('About')

    // Validate that a link with the expected URL is present
    // *Following* the link is better suited to an E2E test
    cy.get('a[href="/"]').should('be.visible')
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
source: "https://nextjs.org/docs/pages/guides/testing/jest"
--------------------------------------------------------------------------------

# Jest

@router: Pages Router

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

## Setting up Jest (with Babel)

If you opt out of the [Next.js Compiler](/docs/architecture/nextjs-compiler.md) and use Babel instead, you will need to manually configure Jest and install `babel-jest` and `identity-obj-proxy` in addition to the packages above.

Here are the recommended options to configure Jest for Next.js:

```js filename="jest.config.js"
module.exports = {
  collectCoverage: true,
  // on node 14.x coverage provider v8 offers good speed and more or less good report
  coverageProvider: 'v8',
  collectCoverageFrom: [
    '**/*.{js,jsx,ts,tsx}',
    '!**/*.d.ts',
    '!**/node_modules/**',
    '!<rootDir>/out/**',
    '!<rootDir>/.next/**',
    '!<rootDir>/*.config.js',
    '!<rootDir>/coverage/**',
  ],
  moduleNameMapper: {
    // Handle CSS imports (with CSS modules)
    // https://jestjs.io/docs/webpack#mocking-css-modules
    '^.+\\.module\\.(css|sass|scss)$': 'identity-obj-proxy',

    // Handle CSS imports (without CSS modules)
    '^.+\\.(css|sass|scss)$': '<rootDir>/__mocks__/styleMock.js',

    // Handle image imports
    // https://jestjs.io/docs/webpack#handling-static-assets
    '^.+\\.(png|jpg|jpeg|gif|webp|avif|ico|bmp|svg)$': `<rootDir>/__mocks__/fileMock.js`,

    // Handle module aliases
    '^@/components/(.*)$': '<rootDir>/components/$1',

    // Handle @next/font
    '@next/font/(.*)': `<rootDir>/__mocks__/nextFontMock.js`,
    // Handle next/font
    'next/font/(.*)': `<rootDir>/__mocks__/nextFontMock.js`,
    // Disable server-only
    'server-only': `<rootDir>/__mocks__/empty.js`,
  },
  // Add more setup options before each test is run
  // setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  testPathIgnorePatterns: ['<rootDir>/node_modules/', '<rootDir>/.next/'],
  testEnvironment: 'jsdom',
  transform: {
    // Use babel-jest to transpile tests with the next/babel preset
    // https://jestjs.io/docs/configuration#transform-objectstring-pathtotransformer--pathtotransformer-object
    '^.+\\.(js|jsx|ts|tsx)$': ['babel-jest', { presets: ['next/babel'] }],
  },
  transformIgnorePatterns: [
    '/node_modules/',
    '^.+\\.module\\.(css|sass|scss)$',
  ],
}
```

You can learn more about each configuration option in the [Jest docs](https://jestjs.io/docs/configuration). We also recommend reviewing [`next/jest` configuration](https://github.com/vercel/next.js/blob/e02fe314dcd0ae614c65b505c6daafbdeebb920e/packages/next/src/build/jest/jest.ts) to see how Next.js configures Jest.

### Handling stylesheets and image imports

Stylesheets and images aren't used in the tests but importing them may cause errors, so they will need to be mocked.

Create the mock files referenced in the configuration above - `fileMock.js` and `styleMock.js` - inside a `__mocks__` directory:

```js filename="__mocks__/fileMock.js"
module.exports = 'test-file-stub'
```

```js filename="__mocks__/styleMock.js"
module.exports = {}
```

For more information on handling static assets, please refer to the [Jest Docs](https://jestjs.io/docs/webpack#handling-static-assets).

## Handling Fonts

To handle fonts, create the `nextFontMock.js` file inside the `__mocks__` directory, and add the following configuration:

```js filename="__mocks__/nextFontMock.js"
module.exports = new Proxy(
  {},
  {
    get: function getter() {
      return () => ({
        className: 'className',
        variable: 'variable',
        style: { fontFamily: 'fontFamily' },
      })
    },
  }
)
```

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

For example, we can add a test to check if the `<Home />` component successfully renders a heading:

```jsx filename="pages/index.js
export default function Home() {
  return <h1>Home</h1>
}
```

```jsx filename="__tests__/index.test.js"
import '@testing-library/jest-dom'
import { render, screen } from '@testing-library/react'
import Home from '../pages/index'

describe('Home', () => {
  it('renders a heading', () => {
    render(<Home />)

    const heading = screen.getByRole('heading', { level: 1 })

    expect(heading).toBeInTheDocument()
  })
})
```

Optionally, add a [snapshot test](https://jestjs.io/docs/snapshot-testing) to keep track of any unexpected changes in your component:

```jsx filename="__tests__/snapshot.js"
import { render } from '@testing-library/react'
import Home from '../pages/index'

it('renders homepage unchanged', () => {
  const { container } = render(<Home />)
  expect(container).toMatchSnapshot()
})
```

> **Good to know**: Test files should not be included inside the Pages Router because any files inside the Pages Router are considered routes.

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
source: "https://nextjs.org/docs/pages/guides/testing/playwright"
--------------------------------------------------------------------------------

# Playwright

@router: Pages Router

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

```tsx filename="pages/index.ts"
import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Home</h1>
      <Link href="/about">About</Link>
    </div>
  )
}
```

```tsx filename="pages/about.ts"
import Link from 'next/link'

export default function About() {
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
source: "https://nextjs.org/docs/pages/guides/testing/vitest"
--------------------------------------------------------------------------------

# Vitest

@router: Pages Router

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

```tsx filename="pages/index.tsx" switcher
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

```jsx filename="pages/index.jsx" switcher
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

```tsx filename="__tests__/index.test.tsx" switcher
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../pages/index'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
})
```

```jsx filename="__tests__/index.test.jsx" switcher
import { expect, test } from 'vitest'
import { render, screen } from '@testing-library/react'
import Page from '../pages/index'

test('Page', () => {
  render(<Page />)
  expect(screen.getByRole('heading', { level: 1, name: 'Home' })).toBeDefined()
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
source: "https://nextjs.org/docs/pages/guides/third-party-libraries"
--------------------------------------------------------------------------------

# Third Party Libraries

@router: Pages Router

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

To load Google Tag Manager for all routes, include the component directly in your custom `_app` and
pass in your GTM container ID:

```jsx filename="pages/_app.js"
import { GoogleTagManager } from '@next/third-parties/google'

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <GoogleTagManager gtmId="GTM-XYZ" />
    </>
  )
}
```

To load Google Tag Manager for a single route, include the component in your page file:

```jsx filename="pages/index.js"
import { GoogleTagManager } from '@next/third-parties/google'

export default function Page() {
  return <GoogleTagManager gtmId="GTM-XYZ" />
}
```

#### Sending Events

The `sendGTMEvent` function can be used to track user interactions on your page by sending events
using the `dataLayer` object. For this function to work, the `<GoogleTagManager />` component must be
included in either a parent layout, page, or component, or directly in the same file.

```jsx filename="pages/index.js"
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

To load Google Analytics for all routes, include the component directly in your custom `_app` and
pass in your measurement ID:

```jsx filename="pages/_app.js"
import { GoogleAnalytics } from '@next/third-parties/google'

export default function MyApp({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <GoogleAnalytics gaId="G-XYZ" />
    </>
  )
}
```

To load Google Analytics for a single route, include the component in your page file:

```jsx filename="pages/index.js"
import { GoogleAnalytics } from '@next/third-parties/google'

export default function Page() {
  return <GoogleAnalytics gaId="G-XYZ" />
}
```

#### Sending Events

The `sendGAEvent` function can be used to measure user interactions on your page by sending events
using the `dataLayer` object. For this function to work, the `<GoogleAnalytics />` component must be
included in either a parent layout, page, or component, or directly in the same file.

```jsx filename="pages/index.js"
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

```jsx filename="pages/index.js"
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

```jsx filename="pages/index.js"
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
title: "Upgrading"
description: "Learn how to upgrade to the latest versions of Next.js."
source: "https://nextjs.org/docs/pages/guides/upgrading"
--------------------------------------------------------------------------------

# Upgrading

@router: Pages Router

Learn how to upgrade to the latest versions of Next.js following the versions-specific guides:

 - [Codemods](/docs/pages/guides/upgrading/codemods.md)
 - [Version 10](/docs/pages/guides/upgrading/version-10.md)
 - [Version 11](/docs/pages/guides/upgrading/version-11.md)
 - [Version 12](/docs/pages/guides/upgrading/version-12.md)
 - [Version 13](/docs/pages/guides/upgrading/version-13.md)
 - [Version 14](/docs/pages/guides/upgrading/version-14.md)
 - [Version 9](/docs/pages/guides/upgrading/version-9.md)

--------------------------------------------------------------------------------
title: "Codemods"
description: "Use codemods to upgrade your Next.js codebase when new features are released."
source: "https://nextjs.org/docs/pages/guides/upgrading/codemods"
--------------------------------------------------------------------------------

# Codemods

@router: Pages Router

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

Remove `<a>` tags inside [Link Components](/docs/pages/api-reference/components/link.md).

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
title: "How to upgrade to version 10"
description: "Upgrade your Next.js Application from Version 9 to Version 10."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-10"
--------------------------------------------------------------------------------

# Version 10

@router: Pages Router

There were no breaking changes between versions 9 and 10.

To upgrade to version 10, run the following command:

```bash filename="Terminal"
npm i next@10
```

```bash filename="Terminal"
yarn add next@10
```

```bash filename="Terminal"
pnpm up next@10
```

```bash filename="Terminal"
bun add next@10
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their corresponding versions.


--------------------------------------------------------------------------------
title: "How to upgrade to version 11"
description: "Upgrade your Next.js Application from Version 10 to Version 11."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-11"
--------------------------------------------------------------------------------

# Version 11

@router: Pages Router

To upgrade to version 11, run the following command:

```bash filename="Terminal"
npm i next@11 react@17 react-dom@17
```

```bash filename="Terminal"
yarn add next@11 react@17 react-dom@17
```

```bash filename="Terminal"
pnpm up next@11 react@17 react-dom@17
```

```bash filename="Terminal"
bun add next@11 react@17 react-dom@17
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their corresponding versions.

### Webpack 5

Webpack 5 is now the default for all Next.js applications. If you did not have a custom webpack configuration, your application is already using webpack 5. If you do have a custom webpack configuration, you can refer to the [Next.js webpack 5 documentation](/docs/messages/webpack5.md) for upgrade guidance.

### Cleaning the `distDir` is now a default

The build output directory (defaults to `.next`) is now cleared by default except for the Next.js caches. You can refer to [the cleaning `distDir` RFC](https://github.com/vercel/next.js/discussions/6009) for more information.

If your application was relying on this behavior previously you can disable the new default behavior by adding the `cleanDistDir: false` flag in `next.config.js`.

### `PORT` is now supported for `next dev` and `next start`

Next.js 11 supports the `PORT` environment variable to set the port the application runs on. Using `-p`/`--port` is still recommended but if you were prohibited from using `-p` in any way you can now use `PORT` as an alternative:

Example:

```
PORT=4000 next start
```

### `next.config.js` customization to import images

Next.js 11 supports static image imports with `next/image`. This new feature relies on being able to process image imports. If you previously added the `next-images` or `next-optimized-images` packages you can either move to the new built-in support using `next/image` or disable the feature:

```js filename="next.config.js"
module.exports = {
  images: {
    disableStaticImages: true,
  },
}
```

### Remove `super.componentDidCatch()` from `pages/_app.js`

The `next/app` component's `componentDidCatch` was deprecated in Next.js 9 as it's no longer needed and has since been a no-op. In Next.js 11, it was removed.

If your `pages/_app.js` has a custom `componentDidCatch` method you can remove `super.componentDidCatch` as it is no longer needed.

### Remove `Container` from `pages/_app.js`

This export was deprecated in Next.js 9 as it's no longer needed and has since been a no-op with a warning during development. In Next.js 11 it was removed.

If your `pages/_app.js` imports `Container` from `next/app` you can remove `Container` as it was removed. Learn more in [the documentation](/docs/messages/app-container-deprecated.md).

### Remove `props.url` usage from page components

This property was deprecated in Next.js 4 and has since shown a warning during development. With the introduction of `getStaticProps` / `getServerSideProps` these methods already disallowed the usage of `props.url`. In Next.js 11, it was removed completely.

You can learn more in [the documentation](/docs/messages/url-deprecated.md).

### Remove `unsized` property on `next/image`

The `unsized` property on `next/image` was deprecated in Next.js 10.0.1. You can use `layout="fill"` instead. In Next.js 11 `unsized` was removed.

### Remove `modules` property on `next/dynamic`

The `modules` and `render` option for `next/dynamic` were deprecated in Next.js 9.5. This was done in order to make the `next/dynamic` API closer to `React.lazy`. In Next.js 11, the `modules` and `render` options were removed.

This option hasn't been mentioned in the documentation since Next.js 8 so it's less likely that your application is using it.

If your application does use `modules` and `render` you can refer to [the documentation](/docs/messages/next-dynamic-modules.md).

### Remove `Head.rewind`

`Head.rewind` has been a no-op since Next.js 9.5, in Next.js 11 it was removed. You can safely remove your usage of `Head.rewind`.

### Moment.js locales excluded by default

Moment.js includes translations for a lot of locales by default. Next.js now automatically excludes these locales by default to optimize bundle size for applications using Moment.js.

To load a specific locale use this snippet:

```js
import moment from 'moment'
import 'moment/locale/ja'

moment.locale('ja')
```

You can opt-out of this new default by adding `excludeDefaultMomentLocales: false` to `next.config.js` if you do not want the new behavior, do note it's highly recommended to not disable this new optimization as it significantly reduces the size of Moment.js.

### Update usage of `router.events`

In case you're accessing `router.events` during rendering, in Next.js 11 `router.events` is no longer provided during pre-rendering. Ensure you're accessing `router.events` in `useEffect`:

```js
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
```

If your application uses `router.router.events` which was an internal property that was not public please make sure to use `router.events` as well.

## React 16 to 17

React 17 introduced a new [JSX Transform](https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html) that brings a long-time Next.js feature to the wider React ecosystem: Not having to `import React from 'react'` when using JSX. When using React 17 Next.js will automatically use the new transform. This transform does not make the `React` variable global, which was an unintended side-effect of the previous Next.js implementation. A [codemod is available](/docs/pages/guides/upgrading/codemods.md#add-missing-react-import) to automatically fix cases where you accidentally used `React` without importing it.

Most applications already use the latest version of React, with Next.js 11 the minimum React version has been updated to 17.0.2.

To upgrade you can run the following command:

```
npm install react@latest react-dom@latest
```

Or using `yarn`:

```
yarn add react@latest react-dom@latest
```


--------------------------------------------------------------------------------
title: "How to upgrade to version 12"
description: "Upgrade your Next.js Application from Version 11 to Version 12."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-12"
--------------------------------------------------------------------------------

# Version 12

@router: Pages Router

To upgrade to version 12, run the following command:

```bash filename="Terminal"
npm i next@12 react@17 react-dom@17 eslint-config-next@12
```

```bash filename="Terminal"
yarn add next@12 react@17 react-dom@17 eslint-config-next@12
```

```bash filename="Terminal"
pnpm up next@12 react@17 react-dom@17 eslint-config-next@12
```

```bash filename="Terminal"
bun add next@12 react@17 react-dom@17 eslint-config-next@12
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their corresponding versions.

### Upgrading to 12.2

[Middleware](/docs/messages/middleware-upgrade-guide.md) - If you were using Middleware prior to `12.2`, please see the [upgrade guide](/docs/messages/middleware-upgrade-guide.md) for more information.

### Upgrading to 12.0

[Minimum Node.js Version](https://nodejs.org/en/) - The minimum Node.js version has been bumped from `12.0.0` to `12.22.0` which is the first version of Node.js with native ES Modules support.

[Minimum React Version](https://react.dev/learn/add-react-to-an-existing-project) - The minimum required React version is `17.0.2`. To upgrade you can run the following command in the terminal:

```bash filename="Terminal"
npm install react@latest react-dom@latest

yarn add react@latest react-dom@latest

pnpm update react@latest react-dom@latest

bun add react@latest react-dom@latest
```

#### SWC replacing Babel

Next.js now uses the Rust-based compiler [SWC](https://swc.rs/) to compile JavaScript/TypeScript. This new compiler is up to 17x faster than Babel when compiling individual files and up to 5x faster Fast Refresh.

Next.js provides full backward compatibility with applications that have [custom Babel configuration](/docs/pages/guides/babel.md). All transformations that Next.js handles by default like styled-jsx and tree-shaking of `getStaticProps` / `getStaticPaths` / `getServerSideProps` have been ported to Rust.

When an application has a custom Babel configuration, Next.js will automatically opt-out of using SWC for compiling JavaScript/Typescript and will fall back to using Babel in the same way that it was used in Next.js 11.

Many of the integrations with external libraries that currently require custom Babel transformations will be ported to Rust-based SWC transforms in the near future. These include but are not limited to:

* Styled Components
* Emotion
* Relay

In order to prioritize transforms that will help you adopt SWC, please provide your `.babelrc` on [this feedback thread](https://github.com/vercel/next.js/discussions/30174).

#### SWC replacing Terser for minification

You can opt-in to replacing Terser with SWC for minifying JavaScript up to 7x faster using a flag in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  swcMinify: true,
}
```

Minification using SWC is an opt-in flag to ensure it can be tested against more real-world Next.js applications before it becomes the default in Next.js 12.1. If you have feedback about minification, please leave it on [this feedback thread](https://github.com/vercel/next.js/discussions/30237).

#### Improvements to styled-jsx CSS parsing

On top of the Rust-based compiler we've implemented a new CSS parser based on the one used for the styled-jsx Babel transform. This new parser has improved handling of CSS and now errors when invalid CSS is used that would previously slip through and cause unexpected behavior.

Because of this change invalid CSS will throw an error during development and `next build`. This change only affects styled-jsx usage.

#### `next/image` changed wrapping element

`next/image` now renders the `<img>` inside a `<span>` instead of `<div>`.

If your application has specific CSS targeting span such as `.container span`, upgrading to Next.js 12 might incorrectly match the wrapping element inside the `<Image>` component. You can avoid this by restricting the selector to a specific class such as `.container span.item` and updating the relevant component with that className, such as `<span className="item" />`.

If your application has specific CSS targeting the `next/image` `<div>` tag, for example `.container div`, it may not match anymore. You can update the selector `.container span`, or preferably, add a new `<div className="wrapper">` wrapping the `<Image>` component and target that instead such as `.container .wrapper`.

The `className` prop is unchanged and will still be passed to the underlying `<img>` element.

See the [documentation](/docs/pages/api-reference/components/image.md#styling-images) for more info.

#### HMR connection now uses a WebSocket

Previously, Next.js used a [server-sent events](https://developer.mozilla.org/docs/Web/API/Server-sent_events) connection to receive HMR events. Next.js 12 now uses a WebSocket connection.

In some cases when proxying requests to the Next.js dev server, you will need to ensure the upgrade request is handled correctly. For example, in `nginx` you would need to add the following configuration:

```nginx
location /_next/webpack-hmr {
    proxy_pass http://localhost:3000/_next/webpack-hmr;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
}
```

If you are using Apache (2.x), you can add the following configuration to enable web sockets to the server. Review the port, host name and server names.

```
<VirtualHost *:443>
 # ServerName yourwebsite.local
 ServerName "${WEBSITE_SERVER_NAME}"
 ProxyPass / http://localhost:3000/
 ProxyPassReverse / http://localhost:3000/
 # Next.js 12 uses websocket
 <Location /_next/webpack-hmr>
    RewriteEngine On
    RewriteCond %{QUERY_STRING} transport=websocket [NC]
    RewriteCond %{HTTP:Upgrade} websocket [NC]
    RewriteCond %{HTTP:Connection} upgrade [NC]
    RewriteRule /(.*) ws://localhost:3000/_next/webpack-hmr/$1 [P,L]
    ProxyPass ws://localhost:3000/_next/webpack-hmr retry=0 timeout=30
    ProxyPassReverse ws://localhost:3000/_next/webpack-hmr
 </Location>
</VirtualHost>
```

For custom servers, such as `express`, you may need to use `app.all` to ensure the request is passed correctly, for example:

```js
app.all('/_next/webpack-hmr', (req, res) => {
  nextjsRequestHandler(req, res)
})
```

#### Webpack 4 support has been removed

If you are already using webpack 5 you can skip this section.

Next.js has adopted webpack 5 as the default for compilation in Next.js 11. As communicated in the [webpack 5 upgrading documentation](/docs/messages/webpack5.md) Next.js 12 removes support for webpack 4.

If your application is still using webpack 4 using the opt-out flag, you will now see an error linking to the [webpack 5 upgrading documentation](/docs/messages/webpack5.md).

#### `target` option deprecated

If you do not have `target` in `next.config.js` you can skip this section.

The target option has been deprecated in favor of built-in support for tracing what dependencies are needed to run a page.

During `next build`, Next.js will automatically trace each page and its dependencies to determine all of the files that are needed for deploying a production version of your application.

If you are currently using the `target` option set to `serverless`, please read the [documentation on how to leverage the new output](/docs/pages/api-reference/config/next-config-js/output.md).


--------------------------------------------------------------------------------
title: "How to upgrade to version 13"
description: "Upgrade your Next.js Application from Version 12 to 13."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-13"
--------------------------------------------------------------------------------

# Version 13

@router: Pages Router

## Upgrading from 12 to 13

To update to Next.js version 13, run the following command using your preferred package manager:

```bash filename="Terminal"
npm i next@13 react@latest react-dom@latest eslint-config-next@13
```

```bash filename="Terminal"
yarn add next@13 react@latest react-dom@latest eslint-config-next@13
```

```bash filename="Terminal"
pnpm i next@13 react@latest react-dom@latest eslint-config-next@13
```

```bash filename="Terminal"
bun add next@13 react@latest react-dom@latest eslint-config-next@13
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

### v13 Summary

* The [Supported Browsers](/docs/architecture/supported-browsers.md) have been changed to drop Internet Explorer and target modern browsers.
* The minimum Node.js version has been bumped from 12.22.0 to 16.14.0, since 12.x and 14.x have reached end-of-life.
* The minimum React version has been bumped from 17.0.2 to 18.2.0.
* The `swcMinify` configuration property was changed from `false` to `true`. See [Next.js Compiler](/docs/architecture/nextjs-compiler.md) for more info.
* The `next/image` import was renamed to `next/legacy/image`. The `next/future/image` import was renamed to `next/image`. A [codemod is available](/docs/pages/guides/upgrading/codemods.md#next-image-to-legacy-image) to safely and automatically rename your imports.
* The `next/link` child can no longer be `<a>`. Add the `legacyBehavior` prop to use the legacy behavior or remove the `<a>` to upgrade. A [codemod is available](/docs/pages/guides/upgrading/codemods.md#new-link) to automatically upgrade your code.
* The `target` configuration property has been removed and superseded by [Output File Tracing](/docs/pages/api-reference/config/next-config-js/output.md).

## Migrating shared features

Next.js 13 introduces a new [`app` directory](/docs/app.md) with new features and conventions. However, upgrading to Next.js 13 does **not** require using the new `app` Router.

You can continue using `pages` with new features that work in both directories, such as the updated [Image component](#image-component), [Link component](#link-component), [Script component](#script-component), and [Font optimization](#font-optimization).

### `<Image/>` Component

Next.js 12 introduced many improvements to the Image Component with a temporary import: `next/future/image`. These improvements included less client-side JavaScript, easier ways to extend and style images, better accessibility, and native browser lazy loading.

Starting in Next.js 13, this new behavior is now the default for `next/image`.

There are two codemods to help you migrate to the new Image Component:

* [next-image-to-legacy-image](/docs/pages/guides/upgrading/codemods.md#next-image-to-legacy-image): This codemod will safely and automatically rename `next/image` imports to `next/legacy/image` to maintain the same behavior as Next.js 12. We recommend running this codemod to quickly update to Next.js 13 automatically.
* [next-image-experimental](/docs/pages/guides/upgrading/codemods.md#next-image-experimental): After running the previous codemod, you can optionally run this experimental codemod to upgrade `next/legacy/image` to the new `next/image`, which will remove unused props and add inline styles. Please note this codemod is experimental and only covers static usage (such as `<Image src={img} layout="responsive" />`) but not dynamic usage (such as `<Image {...props} />`).

Alternatively, you can manually update by following the [migration guide](/docs/pages/guides/upgrading/codemods.md#next-image-experimental) and also see the [legacy comparison](/docs/pages/api-reference/components/image-legacy.md#comparison).

### `<Link>` Component

The [`<Link>` Component](/docs/pages/api-reference/components/link.md) no longer requires manually adding an `<a>` tag as a child. This behavior was added as an experimental option in [version 12.2](https://nextjs.org/blog/next-12-2) and is now the default. In Next.js 13, `<Link>` always renders `<a>` and allows you to forward props to the underlying tag.

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

To upgrade your links to Next.js 13, you can use the [`new-link` codemod](/docs/pages/guides/upgrading/codemods.md#new-link).

### `<Script>` Component

The behavior of [`next/script`](/docs/pages/api-reference/components/script.md) has been updated to support both `pages` and `app`. If incrementally adopting `app`, read the [upgrade guide](/docs/pages/guides/upgrading.md).

### Font Optimization

Previously, Next.js helped you optimize fonts by inlining font CSS. Version 13 introduces the new [`next/font`](/docs/pages/api-reference/components/font.md) module which gives you the ability to customize your font loading experience while still ensuring great performance and privacy.

See [Optimizing Fonts](/docs/pages/api-reference/components/font.md) to learn how to use `next/font`.


--------------------------------------------------------------------------------
title: "How to upgrade to version 14"
description: "Upgrade your Next.js Application from Version 13 to 14."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-14"
--------------------------------------------------------------------------------

# Version 14

@router: Pages Router

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
title: "How to upgrade to version 9"
description: "Upgrade your Next.js Application from Version 8 to Version 9."
source: "https://nextjs.org/docs/pages/guides/upgrading/version-9"
--------------------------------------------------------------------------------

# Version 9

@router: Pages Router

To upgrade to version 9, run the following command:

```bash filename="Terminal"
npm i next@9
```

```bash filename="Terminal"
yarn add next@9
```

```bash filename="Terminal"
pnpm up next@9
```

```bash filename="Terminal"
bun add next@9
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their corresponding versions.

## Check your Custom App File (`pages/_app.js`)

If you previously copied the [Custom `<App>`](/docs/pages/building-your-application/routing/custom-app.md) example, you may be able to remove your `getInitialProps`.

Removing `getInitialProps` from `pages/_app.js` (when possible) is important to leverage new Next.js features!

The following `getInitialProps` does nothing and may be removed:

```js
class MyApp extends App {
  // Remove me, I do nothing!
  static async getInitialProps({ Component, ctx }) {
    let pageProps = {}

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx)
    }

    return { pageProps }
  }

  render() {
    // ... etc
  }
}
```

## Breaking Changes

### `@zeit/next-typescript` is no longer necessary

Next.js will now ignore usage `@zeit/next-typescript` and warn you to remove it. Please remove this plugin from your `next.config.js`.

Remove references to `@zeit/next-typescript/babel` from your custom `.babelrc` (if present).

The usage of [`fork-ts-checker-webpack-plugin`](https://github.com/Realytics/fork-ts-checker-webpack-plugin/issues) should also be removed from your `next.config.js`.

TypeScript Definitions are published with the `next` package, so you need to uninstall `@types/next` as they would conflict.

The following types are different:

> This list was created by the community to help you upgrade, if you find other differences please send a pull-request to this list to help other users.

From:

```tsx
import { NextContext } from 'next'
import { NextAppContext, DefaultAppIProps } from 'next/app'
import { NextDocumentContext, DefaultDocumentIProps } from 'next/document'
```

to

```tsx
import { NextPageContext } from 'next'
import { AppContext, AppInitialProps } from 'next/app'
import { DocumentContext, DocumentInitialProps } from 'next/document'
```

### The `config` key is now an export on a page

You may no longer export a custom variable named `config` from a page (i.e. `export { config }` / `export const config ...`).
This exported variable is now used to specify page-level Next.js configuration like Opt-in AMP and API Route features.

You must rename a non-Next.js-purposed `config` export to something different.

### `next/dynamic` no longer renders "loading..." by default while loading

Dynamic components will not render anything by default while loading. You can still customize this behavior by setting the `loading` property:

```jsx
import dynamic from 'next/dynamic'

const DynamicComponentWithCustomLoading = dynamic(
  () => import('../components/hello2'),
  {
    loading: () => <p>Loading</p>,
  }
)
```

### `withAmp` has been removed in favor of an exported configuration object

Next.js now has the concept of page-level configuration, so the `withAmp` higher-order component has been removed for consistency.

This change can be **automatically migrated by running the following commands in the root of your Next.js project:**

```bash filename="Terminal"
curl -L https://github.com/vercel/next-codemod/archive/master.tar.gz | tar -xz --strip=2 next-codemod-master/transforms/withamp-to-config.js npx jscodeshift -t ./withamp-to-config.js pages/**/*.js
```

To perform this migration by hand, or view what the codemod will produce, see below:

**Before**

```jsx
import { withAmp } from 'next/amp'

function Home() {
  return <h1>My AMP Page</h1>
}

export default withAmp(Home)
// or
export default withAmp(Home, { hybrid: true })
```

**After**

```jsx
export default function Home() {
  return <h1>My AMP Page</h1>
}

export const config = {
  amp: true,
  // or
  amp: 'hybrid',
}
```

### `next export` no longer exports pages as `index.html`

Previously, exporting `pages/about.js` would result in `out/about/index.html`. This behavior has been changed to result in `out/about.html`.

You can revert to the previous behavior by creating a `next.config.js` with the following content:

```js filename="next.config.js"
module.exports = {
  trailingSlash: true,
}
```

### `pages/api/` is treated differently

Pages in `pages/api/` are now considered [API Routes](https://nextjs.org/blog/next-9#api-routes).
Pages in this directory will no longer contain a client-side bundle.

## Deprecated Features

### `next/dynamic` has deprecated loading multiple modules at once

The ability to load multiple modules at once has been deprecated in `next/dynamic` to be closer to React's implementation (`React.lazy` and `Suspense`).

Updating code that relies on this behavior is relatively straightforward! We've provided an example of a before/after to help you migrate your application:

**Before**

```jsx
import dynamic from 'next/dynamic'

const HelloBundle = dynamic({
  modules: () => {
    const components = {
      Hello1: () => import('../components/hello1').then((m) => m.default),
      Hello2: () => import('../components/hello2').then((m) => m.default),
    }

    return components
  },
  render: (props, { Hello1, Hello2 }) => (
    <div>
      <h1>{props.title}</h1>
      <Hello1 />
      <Hello2 />
    </div>
  ),
})

function DynamicBundle() {
  return <HelloBundle title="Dynamic Bundle" />
}

export default DynamicBundle
```

**After**

```jsx
import dynamic from 'next/dynamic'

const Hello1 = dynamic(() => import('../components/hello1'))
const Hello2 = dynamic(() => import('../components/hello2'))

function HelloBundle({ title }) {
  return (
    <div>
      <h1>{title}</h1>
      <Hello1 />
      <Hello2 />
    </div>
  )
}

function DynamicBundle() {
  return <HelloBundle title="Dynamic Bundle" />
}

export default DynamicBundle
```



--------------------------------------------------------------------------------
title: "Building Your Application"
description: "Learn how to use Next.js features to build your application."
source: "https://nextjs.org/docs/pages/building-your-application"
--------------------------------------------------------------------------------

# Building Your Application

@router: Pages Router



 - [Routing](/docs/pages/building-your-application/routing.md)
 - [Rendering](/docs/pages/building-your-application/rendering.md)
 - [Data Fetching](/docs/pages/building-your-application/data-fetching.md)
 - [Configuring](/docs/pages/building-your-application/configuring.md)

--------------------------------------------------------------------------------
title: "Routing"
description: "Learn the fundamentals of routing for front-end applications with the Pages Router."
source: "https://nextjs.org/docs/pages/building-your-application/routing"
--------------------------------------------------------------------------------

# Routing

@router: Pages Router

The Pages Router has a file-system based router built on concepts of pages. When a file is added to the `pages` directory it's automatically available as a route. Learn more about routing in the Pages Router:

 - [Pages and Layouts](/docs/pages/building-your-application/routing/pages-and-layouts.md)
 - [Dynamic Routes](/docs/pages/building-your-application/routing/dynamic-routes.md)
 - [Linking and Navigating](/docs/pages/building-your-application/routing/linking-and-navigating.md)
 - [Custom App](/docs/pages/building-your-application/routing/custom-app.md)
 - [Custom Document](/docs/pages/building-your-application/routing/custom-document.md)
 - [API Routes](/docs/pages/building-your-application/routing/api-routes.md)
 - [Custom Errors](/docs/pages/building-your-application/routing/custom-error.md)

--------------------------------------------------------------------------------
title: "Pages and Layouts"
description: "Create your first page and shared layout with the Pages Router."
source: "https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts"
--------------------------------------------------------------------------------

# Pages and Layouts

@router: Pages Router

The Pages Router has a file-system based router built on the concept of pages.

When a file is added to the `pages` directory, it's automatically available as a route.

In Next.js, a **page** is a [React Component](https://react.dev/learn/your-first-component) exported from a `.js`, `.jsx`, `.ts`, or `.tsx` file in the `pages` directory. Each page is associated with a route based on its file name.

**Example**: If you create `pages/about.js` that exports a React component like below, it will be accessible at `/about`.

```jsx
export default function About() {
  return <div>About</div>
}
```

## Index routes

The router will automatically route files named `index` to the root of the directory.

* `pages/index.js` → `/`
* `pages/blog/index.js` → `/blog`

## Nested routes

The router supports nested files. If you create a nested folder structure, files will automatically be routed in the same way still.

* `pages/blog/first-post.js` → `/blog/first-post`
* `pages/dashboard/settings/username.js` → `/dashboard/settings/username`

## Pages with Dynamic Routes

Next.js supports pages with dynamic routes. For example, if you create a file called `pages/posts/[id].js`, then it will be accessible at `posts/1`, `posts/2`, etc.

> To learn more about dynamic routing, check the [Dynamic Routing documentation](/docs/pages/building-your-application/routing/dynamic-routes.md).

## Layout Pattern

The React model allows us to deconstruct a [page](/docs/pages/building-your-application/routing/pages-and-layouts.md) into a series of components. Many of these components are often reused between pages. For example, you might have the same navigation bar and footer on every page.

```jsx filename="components/layout.js"
import Navbar from './navbar'
import Footer from './footer'

export default function Layout({ children }) {
  return (
    <>
      <Navbar />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```

## Examples

### Single Shared Layout with Custom App

If you only have one layout for your entire application, you can create a [Custom App](/docs/pages/building-your-application/routing/custom-app.md) and wrap your application with the layout. Since the `<Layout />` component is re-used when changing pages, its component state will be preserved (e.g. input values).

```jsx filename="pages/_app.js"
import Layout from '../components/layout'

export default function MyApp({ Component, pageProps }) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}
```

### Per-Page Layouts

If you need multiple layouts, you can add a property `getLayout` to your page, allowing you to return a React component for the layout. This allows you to define the layout on a *per-page basis*. Since we're returning a function, we can have complex nested layouts if desired.

```jsx filename="pages/index.js"

import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'

export default function Page() {
  return (
    /** Your content */
  )
}

Page.getLayout = function getLayout(page) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}
```

```jsx filename="pages/_app.js"
export default function MyApp({ Component, pageProps }) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
```

When navigating between pages, we want to *persist* page state (input values, scroll position, etc.) for a Single-Page Application (SPA) experience.

This layout pattern enables state persistence because the React component tree is maintained between page transitions. With the component tree, React can understand which elements have changed to preserve state.

> **Good to know**: This process is called [reconciliation](https://react.dev/learn/preserving-and-resetting-state), which is how React understands which elements have changed.

### With TypeScript

When using TypeScript, you must first create a new type for your pages which includes a `getLayout` function. Then, you must create a new type for your `AppProps` which overrides the `Component` property to use the previously created type.

```tsx filename="pages/index.tsx" switcher
import type { ReactElement } from 'react'
import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'
import type { NextPageWithLayout } from './_app'

const Page: NextPageWithLayout = () => {
  return <p>hello world</p>
}

Page.getLayout = function getLayout(page: ReactElement) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}

export default Page
```

```jsx filename="pages/index.js" switcher
import Layout from '../components/layout'
import NestedLayout from '../components/nested-layout'

const Page = () => {
  return <p>hello world</p>
}

Page.getLayout = function getLayout(page) {
  return (
    <Layout>
      <NestedLayout>{page}</NestedLayout>
    </Layout>
  )
}

export default Page
```

```tsx filename="pages/_app.tsx" switcher
import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

export default function MyApp({ Component, pageProps }: AppPropsWithLayout) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
```

```jsx filename="pages/_app.js" switcher
export default function MyApp({ Component, pageProps }) {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
```

### Data Fetching

Inside your layout, you can fetch data on the client-side using `useEffect` or a library like [SWR](https://swr.vercel.app/). Because this file is not a [Page](/docs/pages/building-your-application/routing/pages-and-layouts.md), you cannot use `getStaticProps` or `getServerSideProps` currently.

```jsx filename="components/layout.js"
import useSWR from 'swr'
import Navbar from './navbar'
import Footer from './footer'

export default function Layout({ children }) {
  const { data, error } = useSWR('/api/navigation', fetcher)

  if (error) return <div>Failed to load</div>
  if (!data) return <div>Loading...</div>

  return (
    <>
      <Navbar links={data.links} />
      <main>{children}</main>
      <Footer />
    </>
  )
}
```


--------------------------------------------------------------------------------
title: "Dynamic Routes"
description: "Dynamic Routes are pages that allow you to add custom params to your URLs. Start creating Dynamic Routes and learn more here."
source: "https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes"
--------------------------------------------------------------------------------

# Dynamic Routes

@router: Pages Router

When you don't know the exact segment names ahead of time and want to create routes from dynamic data, you can use Dynamic Segments that are filled in at request time or [prerendered](/docs/pages/building-your-application/data-fetching/get-static-paths.md) at build time.

## Convention

A Dynamic Segment can be created by wrapping a file or folder name in square brackets: `[segmentName]`. For example, `[id]` or `[slug]`.

Dynamic Segments can be accessed from [`useRouter`](/docs/pages/api-reference/functions/use-router.md).

## Example

For example, a blog could include the following route `pages/blog/[slug].js` where `[slug]` is the Dynamic Segment for blog posts.

```jsx
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()
  return <p>Post: {router.query.slug}</p>
}
```

| Route                  | Example URL | `params`        |
| ---------------------- | ----------- | --------------- |
| `pages/blog/[slug].js` | `/blog/a`   | `{ slug: 'a' }` |
| `pages/blog/[slug].js` | `/blog/b`   | `{ slug: 'b' }` |
| `pages/blog/[slug].js` | `/blog/c`   | `{ slug: 'c' }` |

## Catch-all Segments

Dynamic Segments can be extended to **catch-all** subsequent segments by adding an ellipsis inside the brackets `[...segmentName]`.

For example, `pages/shop/[...slug].js` will match `/shop/clothes`, but also `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`, and so on.

| Route                     | Example URL   | `params`                    |
| ------------------------- | ------------- | --------------------------- |
| `pages/shop/[...slug].js` | `/shop/a`     | `{ slug: ['a'] }`           |
| `pages/shop/[...slug].js` | `/shop/a/b`   | `{ slug: ['a', 'b'] }`      |
| `pages/shop/[...slug].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |

## Optional Catch-all Segments

Catch-all Segments can be made **optional** by including the parameter in double square brackets: `[[...segmentName]]`.

For example, `pages/shop/[[...slug]].js` will **also** match `/shop`, in addition to `/shop/clothes`, `/shop/clothes/tops`, `/shop/clothes/tops/t-shirts`.

The difference between **catch-all** and **optional catch-all** segments is that with optional, the route without the parameter is also matched (`/shop` in the example above).

| Route                       | Example URL   | `params`                    |
| --------------------------- | ------------- | --------------------------- |
| `pages/shop/[[...slug]].js` | `/shop`       | `{ slug: undefined }`       |
| `pages/shop/[[...slug]].js` | `/shop/a`     | `{ slug: ['a'] }`           |
| `pages/shop/[[...slug]].js` | `/shop/a/b`   | `{ slug: ['a', 'b'] }`      |
| `pages/shop/[[...slug]].js` | `/shop/a/b/c` | `{ slug: ['a', 'b', 'c'] }` |
## Next Steps

For more information on what to do next, we recommend the following sections

- [Linking and Navigating](/docs/pages/building-your-application/routing/linking-and-navigating.md)
  - Learn how navigation works in Next.js, and how to use the Link Component and `useRouter` hook.
- [useRouter](/docs/pages/api-reference/functions/use-router.md)
  - Learn more about the API of the Next.js Router, and access the router instance in your page with the useRouter hook.


--------------------------------------------------------------------------------
title: "Linking and Navigating"
description: "Learn how navigation works in Next.js, and how to use the Link Component and `useRouter` hook."
source: "https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating"
--------------------------------------------------------------------------------

# Linking and Navigating

@router: Pages Router

The Next.js router allows you to do client-side route transitions between pages, similar to a single-page application.

A React component called `Link` is provided to do this client-side route transition.

```jsx
import Link from 'next/link'

function Home() {
  return (
    <ul>
      <li>
        <Link href="/">Home</Link>
      </li>
      <li>
        <Link href="/about">About Us</Link>
      </li>
      <li>
        <Link href="/blog/hello-world">Blog Post</Link>
      </li>
    </ul>
  )
}

export default Home
```

The example above uses multiple links. Each one maps a path (`href`) to a known page:

* `/` → `pages/index.js`
* `/about` → `pages/about.js`
* `/blog/hello-world` → `pages/blog/[slug].js`

Any `<Link />` in the viewport (initially or through scroll) will be prefetched by default (including the corresponding data) for pages using [Static Generation](/docs/pages/building-your-application/data-fetching/get-static-props.md). The corresponding data for [server-rendered](/docs/pages/building-your-application/data-fetching/get-server-side-props.md) routes is fetched *only when* the `<Link />` is clicked.

## Linking to dynamic paths

You can also use interpolation to create the path, which comes in handy for [dynamic route segments](/docs/pages/building-your-application/routing/dynamic-routes.md). For example, to show a list of posts which have been passed to the component as a prop:

```jsx
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${encodeURIComponent(post.slug)}`}>
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}

export default Posts
```

> [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) is used in the example to keep the path utf-8 compatible.

Alternatively, using a URL Object:

```jsx
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link
            href={{
              pathname: '/blog/[slug]',
              query: { slug: post.slug },
            }}
          >
            {post.title}
          </Link>
        </li>
      ))}
    </ul>
  )
}

export default Posts
```

Now, instead of using interpolation to create the path, we use a URL object in `href` where:

* `pathname` is the name of the page in the `pages` directory. `/blog/[slug]` in this case.
* `query` is an object with the dynamic segment. `slug` in this case.

## Injecting the router

To access the [`router` object](/docs/pages/api-reference/functions/use-router.md#router-object) in a React component you can use [`useRouter`](/docs/pages/api-reference/functions/use-router.md) or [`withRouter`](/docs/pages/api-reference/functions/use-router.md#withrouter).

In general we recommend using [`useRouter`](/docs/pages/api-reference/functions/use-router.md).

## Imperative Routing

[`next/link`](/docs/pages/api-reference/components/link.md) should be able to cover most of your routing needs, but you can also do client-side navigations without it, take a look at the [documentation for `next/router`](/docs/pages/api-reference/functions/use-router.md).

The following example shows how to do basic page navigations with [`useRouter`](/docs/pages/api-reference/functions/use-router.md):

```jsx
import { useRouter } from 'next/router'

export default function ReadMore() {
  const router = useRouter()

  return (
    <button onClick={() => router.push('/about')}>
      Click here to read more
    </button>
  )
}
```

## Shallow Routing

<details>
<summary>Examples</summary>

* [Shallow Routing](https://github.com/vercel/next.js/tree/canary/examples/with-shallow-routing)

</details>

Shallow routing allows you to change the URL without running data fetching methods again, that includes [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md), [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md), and [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md).

You'll receive the updated `pathname` and the `query` via the [`router` object](/docs/pages/api-reference/functions/use-router.md#router-object) (added by [`useRouter`](/docs/pages/api-reference/functions/use-router.md) or [`withRouter`](/docs/pages/api-reference/functions/use-router.md#withrouter)), without losing state.

To enable shallow routing, set the `shallow` option to `true`. Consider the following example:

```jsx
import { useEffect } from 'react'
import { useRouter } from 'next/router'

// Current URL is '/'
function Page() {
  const router = useRouter()

  useEffect(() => {
    // Always do navigations after the first render
    router.push('/?counter=10', undefined, { shallow: true })
  }, [])

  useEffect(() => {
    // The counter changed!
  }, [router.query.counter])
}

export default Page
```

The URL will get updated to `/?counter=10` and the page won't get replaced, only the state of the route is changed.

You can also watch for URL changes via [`componentDidUpdate`](https://react.dev/reference/react/Component#componentdidupdate) as shown below:

```jsx
componentDidUpdate(prevProps) {
  const { pathname, query } = this.props.router
  // verify props have changed to avoid an infinite loop
  if (query.counter !== prevProps.router.query.counter) {
    // fetch data based on the new query
  }
}
```

### Caveats

Shallow routing **only** works for URL changes in the current page. For example, let's assume we have another page called `pages/about.js`, and you run this:

```js
router.push('/?counter=10', '/about?counter=10', { shallow: true })
```

Since that's a new page, it'll unload the current page, load the new one and wait for data fetching even though we asked to do shallow routing.

When shallow routing is used with proxy it will not ensure the new page matches the current page like previously done without proxy. This is due to proxy being able to rewrite dynamically and can't be verified client-side without a data fetch which is skipped with shallow, so a shallow route change must always be treated as shallow.


--------------------------------------------------------------------------------
title: "Custom App"
description: "Control page initialization and add a layout that persists for all pages by overriding the default App component used by Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/routing/custom-app"
--------------------------------------------------------------------------------

# Custom App

@router: Pages Router

Next.js uses the `App` component to initialize pages. You can override it and control the page initialization and:

* Create a shared layout between page changes
* Inject additional data into pages
* [Add global CSS](/docs/app/getting-started/css.md)

## Usage

To override the default `App`, create the file `pages/_app` as shown below:

```tsx filename="pages/_app.tsx" switcher
import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

```jsx filename="pages/_app.jsx" switcher
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

The `Component` prop is the active `page`, so whenever you navigate between routes, `Component` will change to the new `page`. Therefore, any props you send to `Component` will be received by the `page`.

`pageProps` is an object with the initial props that were preloaded for your page by one of our [data fetching methods](/docs/pages/building-your-application/data-fetching.md), otherwise it's an empty object.

> **Good to know**:
>
> * If your app is running and you added a custom `App`, you'll need to restart the development server. Only required if `pages/_app.js` didn't exist before.
> * `App` does not support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching.md) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md).

## `getInitialProps` with `App`

Using [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md) in `App` will disable [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md) for pages without [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md).

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](/docs/app/guides/migrating/app-router-migration.md) the App Router, which allows you to more easily fetch data for pages and layouts.

```tsx filename="pages/_app.tsx" switcher
import App, { AppContext, AppInitialProps, AppProps } from 'next/app'

type AppOwnProps = { example: string }

export default function MyApp({
  Component,
  pageProps,
  example,
}: AppProps & AppOwnProps) {
  return (
    <>
      <p>Data: {example}</p>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (
  context: AppContext
): Promise<AppOwnProps & AppInitialProps> => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, example: 'data' }
}
```

```jsx filename="pages/_app.jsx" switcher
import App from 'next/app'

export default function MyApp({ Component, pageProps, example }) {
  return (
    <>
      <p>Data: {example}</p>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (context) => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, example: 'data' }
}
```


--------------------------------------------------------------------------------
title: "Custom Document"
description: "Extend the default document markup added by Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/routing/custom-document"
--------------------------------------------------------------------------------

# Custom Document

@router: Pages Router

A custom `Document` can update the `<html>` and `<body>` tags used to render a [Page](/docs/pages/building-your-application/routing/pages-and-layouts.md).

To override the default `Document`, create the file `pages/_document` as shown below:

```tsx filename="pages/_document.tsx" switcher
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

```jsx filename="pages/_document.jsx" switcher
import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
```

> **Good to know**:
>
> * `_document` is only rendered on the server, so event handlers like `onClick` cannot be used in this file.
> * `<Html>`, `<Head />`, `<Main />` and `<NextScript />` are required for the page to be properly rendered.

## Caveats

* The `<Head />` component used in `_document` is not the same as [`next/head`](/docs/pages/api-reference/components/head.md). The `<Head />` component used here should only be used for any `<head>` code that is common for all pages. For all other cases, such as `<title>` tags, we recommend using [`next/head`](/docs/pages/api-reference/components/head.md) in your pages or components.
* React components outside of `<Main />` will not be initialized by the browser. Do *not* add application logic here or custom CSS (like `styled-jsx`). If you need shared components in all your pages (like a menu or a toolbar), read [Layouts](/docs/pages/building-your-application/routing/pages-and-layouts.md#layout-pattern) instead.
* `Document` currently does not support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching.md) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md).

## Customizing `renderPage`

Customizing `renderPage` is advanced and only needed for libraries like CSS-in-JS to support server-side rendering. This is not needed for built-in `styled-jsx` support.

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](/docs/app/guides/migrating/app-router-migration.md) the App Router, which allows you to more easily fetch data for pages and layouts.

```tsx filename="pages/_document.tsx" switcher
import Document, {
  Html,
  Head,
  Main,
  NextScript,
  DocumentContext,
  DocumentInitialProps,
} from 'next/document'

class MyDocument extends Document {
  static async getInitialProps(
    ctx: DocumentContext
  ): Promise<DocumentInitialProps> {
    const originalRenderPage = ctx.renderPage

    // Run the React rendering logic synchronously
    ctx.renderPage = () =>
      originalRenderPage({
        // Useful for wrapping the whole react tree
        enhanceApp: (App) => App,
        // Useful for wrapping in a per-page basis
        enhanceComponent: (Component) => Component,
      })

    // Run the parent `getInitialProps`, it now includes the custom `renderPage`
    const initialProps = await Document.getInitialProps(ctx)

    return initialProps
  }

  render() {
    return (
      <Html lang="en">
        <Head />
        <body>
          <Main />
          <NextScript />
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
    const originalRenderPage = ctx.renderPage

    // Run the React rendering logic synchronously
    ctx.renderPage = () =>
      originalRenderPage({
        // Useful for wrapping the whole react tree
        enhanceApp: (App) => App,
        // Useful for wrapping in a per-page basis
        enhanceComponent: (Component) => Component,
      })

    // Run the parent `getInitialProps`, it now includes the custom `renderPage`
    const initialProps = await Document.getInitialProps(ctx)

    return initialProps
  }

  render() {
    return (
      <Html lang="en">
        <Head />
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    )
  }
}

export default MyDocument
```

> **Good to know**:
>
> * `getInitialProps` in `_document` is not called during client-side transitions.
> * The `ctx` object for `_document` is equivalent to the one received in [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props.md#context-object), with the addition of `renderPage`.


--------------------------------------------------------------------------------
title: "API Routes"
description: "Next.js supports API Routes, which allow you to build your API without leaving your Next.js app. Learn how it works here."
source: "https://nextjs.org/docs/pages/building-your-application/routing/api-routes"
--------------------------------------------------------------------------------

# API Routes

@router: Pages Router

<details>
<summary>Examples</summary>

* [API Routes Request Helpers](https://github.com/vercel/next.js/tree/canary/examples/api-routes-proxy)
* [API Routes with GraphQL](https://github.com/vercel/next.js/tree/canary/examples/api-routes-graphql)
* [API Routes with REST](https://github.com/vercel/next.js/tree/canary/examples/api-routes-rest)
* [API Routes with CORS](https://github.com/vercel/next.js/tree/canary/examples/api-routes-cors)

</details>

> **Good to know**: If you are using the App Router, you can use [Server Components](/docs/app/getting-started/server-and-client-components.md) or [Route Handlers](/docs/app/api-reference/file-conventions/route.md) instead of API Routes.

API routes provide a solution to build a **public API** with Next.js.

Any file inside the folder `pages/api` is mapped to `/api/*` and will be treated as an API endpoint instead of a `page`. They are server-side only bundles and won't increase your client-side bundle size.

For example, the following API route returns a JSON response with a status code of `200`:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

```js filename="pages/api/hello.js" switcher
export default function handler(req, res) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

> **Good to know**:
>
> * API Routes [do not specify CORS headers](https://developer.mozilla.org/docs/Web/HTTP/CORS), meaning they are **same-origin only** by default. You can customize such behavior by wrapping the request handler with the [CORS request helpers](https://github.com/vercel/next.js/tree/canary/examples/api-routes-cors).

* API Routes can't be used with [static exports](/docs/pages/guides/static-exports.md). However, [Route Handlers](/docs/app/api-reference/file-conventions/route.md) in the App Router can.
  > * API Routes will be affected by [`pageExtensions` configuration](/docs/pages/api-reference/config/next-config-js/pageExtensions.md) in `next.config.js`.

## Parameters

```tsx
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // ...
}
```

* `req`: An instance of [http.IncomingMessage](https://nodejs.org/api/http.html#class-httpincomingmessage)
* `res`: An instance of [http.ServerResponse](https://nodejs.org/api/http.html#class-httpserverresponse)

## HTTP Methods

To handle different HTTP methods in an API route, you can use `req.method` in your request handler, like so:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    // Process a POST request
  } else {
    // Handle any other HTTP method
  }
}
```

```js filename="pages/api/hello.js" switcher
export default function handler(req, res) {
  if (req.method === 'POST') {
    // Process a POST request
  } else {
    // Handle any other HTTP method
  }
}
```

## Request Helpers

API Routes provide built-in request helpers which parse the incoming request (`req`):

* `req.cookies` - An object containing the cookies sent by the request. Defaults to `{}`
* `req.query` - An object containing the [query string](https://en.wikipedia.org/wiki/Query_string). Defaults to `{}`
* `req.body` - An object containing the body parsed by `content-type`, or `null` if no body was sent

### Custom config

Every API Route can export a `config` object to change the default configuration, which is the following:

```js
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '1mb',
    },
  },
  // Specifies the maximum allowed duration for this function to execute (in seconds)
  maxDuration: 5,
}
```

`bodyParser` is automatically enabled. If you want to consume the body as a `Stream` or with [`raw-body`](https://www.npmjs.com/package/raw-body), you can set this to `false`.

One use case for disabling the automatic `bodyParsing` is to allow you to verify the raw body of a **webhook** request, for example [from GitHub](https://docs.github.com/en/developers/webhooks-and-events/webhooks/securing-your-webhooks#validating-payloads-from-github).

```js
export const config = {
  api: {
    bodyParser: false,
  },
}
```

`bodyParser.sizeLimit` is the maximum size allowed for the parsed body, in any format supported by [bytes](https://github.com/visionmedia/bytes.js), like so:

```js
export const config = {
  api: {
    bodyParser: {
      sizeLimit: '500kb',
    },
  },
}
```

`externalResolver` is an explicit flag that tells the server that this route is being handled by an external resolver like *express* or *connect*. Enabling this option disables warnings for unresolved requests.

```js
export const config = {
  api: {
    externalResolver: true,
  },
}
```

`responseLimit` is automatically enabled, warning when an API Routes' response body is over 4MB.

If you are not using Next.js in a serverless environment, and understand the performance implications of not using a CDN or dedicated media host, you can set this limit to `false`.

```js
export const config = {
  api: {
    responseLimit: false,
  },
}
```

`responseLimit` can also take the number of bytes or any string format supported by `bytes`, for example `1000`, `'500kb'` or `'3mb'`.
This value will be the maximum response size before a warning is displayed. Default is 4MB. (see above)

```js
export const config = {
  api: {
    responseLimit: '8mb',
  },
}
```

## Response Helpers

The [Server Response object](https://nodejs.org/api/http.html#http_class_http_serverresponse), (often abbreviated as `res`) includes a set of Express.js-like helper methods to improve the developer experience and increase the speed of creating new API endpoints.

The included helpers are:

* `res.status(code)` - A function to set the status code. `code` must be a valid [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* `res.json(body)` - Sends a JSON response. `body` must be a [serializable object](https://developer.mozilla.org/docs/Glossary/Serialization)
* `res.send(body)` - Sends the HTTP response. `body` can be a `string`, an `object` or a `Buffer`
* `res.redirect([status,] path)` - Redirects to a specified path or URL. `status` must be a valid [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). If not specified, `status` defaults to "307" "Temporary redirect".
* `res.revalidate(urlPath)` - [Revalidate a page on demand](/docs/pages/guides/incremental-static-regeneration.md#on-demand-revalidation-with-revalidatepath) using `getStaticProps`. `urlPath` must be a `string`.

### Setting the status code of a response

When sending a response back to the client, you can set the status code of the response.

The following example sets the status code of the response to `200` (`OK`) and returns a `message` property with the value of `Hello from Next.js!` as a JSON response:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

```js filename="pages/api/hello.js" switcher
export default function handler(req, res) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

### Sending a JSON response

When sending a response back to the client you can send a JSON response, this must be a [serializable object](https://developer.mozilla.org/docs/Glossary/Serialization).
In a real world application you might want to let the client know the status of the request depending on the result of the requested endpoint.

The following example sends a JSON response with the status code `200` (`OK`) and the result of the async operation. It's contained in a try catch block to handle any errors that may occur, with the appropriate status code and error message caught and sent back to the client:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const result = await someAsyncOperation()
    res.status(200).json({ result })
  } catch (err) {
    res.status(500).json({ error: 'failed to load data' })
  }
}
```

```js filename="pages/api/hello.js" switcher
export default async function handler(req, res) {
  try {
    const result = await someAsyncOperation()
    res.status(200).json({ result })
  } catch (err) {
    res.status(500).json({ error: 'failed to load data' })
  }
}
```

### Sending a HTTP response

Sending an HTTP response works the same way as when sending a JSON response. The only difference is that the response body can be a `string`, an `object` or a `Buffer`.

The following example sends a HTTP response with the status code `200` (`OK`) and the result of the async operation.

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const result = await someAsyncOperation()
    res.status(200).send({ result })
  } catch (err) {
    res.status(500).send({ error: 'failed to fetch data' })
  }
}
```

```js filename="pages/api/hello.js" switcher
export default async function handler(req, res) {
  try {
    const result = await someAsyncOperation()
    res.status(200).send({ result })
  } catch (err) {
    res.status(500).send({ error: 'failed to fetch data' })
  }
}
```

### Redirects to a specified path or URL

Taking a form as an example, you may want to redirect your client to a specified path or URL once they have submitted the form.

The following example redirects the client to the `/` path if the form is successfully submitted:

```ts filename="pages/api/hello.ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { name, message } = req.body

  try {
    await handleFormInputAsync({ name, message })
    res.redirect(307, '/')
  } catch (err) {
    res.status(500).send({ error: 'Failed to fetch data' })
  }
}
```

```js filename="pages/api/hello.js" switcher
export default async function handler(req, res) {
  const { name, message } = req.body

  try {
    await handleFormInputAsync({ name, message })
    res.redirect(307, '/')
  } catch (err) {
    res.status(500).send({ error: 'failed to fetch data' })
  }
}
```

### Adding TypeScript types

You can make your API Routes more type-safe by importing the `NextApiRequest` and `NextApiResponse` types from `next`, in addition to those, you can also type your response data:

```ts
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

> **Good to know**: The body of `NextApiRequest` is `any` because the client may include any payload. You should validate the type/shape of the body at runtime before using it.

## Dynamic API Routes

API Routes support [dynamic routes](/docs/pages/building-your-application/routing/dynamic-routes.md), and follow the same file naming rules used for `pages/`.

```ts filename="pages/api/post/[pid].ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { pid } = req.query
  res.end(`Post: ${pid}`)
}
```

```js filename="pages/api/post/[pid].js" switcher
export default function handler(req, res) {
  const { pid } = req.query
  res.end(`Post: ${pid}`)
}
```

Now, a request to `/api/post/abc` will respond with the text: `Post: abc`.

### Catch all API routes

API Routes can be extended to catch all paths by adding three dots (`...`) inside the brackets. For example:

* `pages/api/post/[...slug].js` matches `/api/post/a`, but also `/api/post/a/b`, `/api/post/a/b/c` and so on.

> **Good to know**: You can use names other than `slug`, such as: `[...param]`

Matched parameters will be sent as a query parameter (`slug` in the example) to the page, and it will always be an array, so, the path `/api/post/a` will have the following `query` object:

```json
{ "slug": ["a"] }
```

And in the case of `/api/post/a/b`, and any other matching path, new parameters will be added to the array, like so:

```json
{ "slug": ["a", "b"] }
```

For example:

```ts filename="pages/api/post/[...slug].ts" switcher
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { slug } = req.query
  res.end(`Post: ${slug.join(', ')}`)
}
```

```js filename="pages/api/post/[...slug].js" switcher
export default function handler(req, res) {
  const { slug } = req.query
  res.end(`Post: ${slug.join(', ')}`)
}
```

Now, a request to `/api/post/a/b/c` will respond with the text: `Post: a, b, c`.

### Optional catch all API routes

Catch all routes can be made optional by including the parameter in double brackets (`[[...slug]]`).

For example, `pages/api/post/[[...slug]].js` will match `/api/post`, `/api/post/a`, `/api/post/a/b`, and so on.

The main difference between catch all and optional catch all routes is that with optional, the route without the parameter is also matched (`/api/post` in the example above).

The `query` objects are as follows:

```json
{ } // GET `/api/post` (empty object)
{ "slug": ["a"] } // `GET /api/post/a` (single-element array)
{ "slug": ["a", "b"] } // `GET /api/post/a/b` (multi-element array)
```

### Caveats

* Predefined API routes take precedence over dynamic API routes, and dynamic API routes over catch all API routes. Take a look at the following examples:
  * `pages/api/post/create.js` - Will match `/api/post/create`
  * `pages/api/post/[pid].js` - Will match `/api/post/1`, `/api/post/abc`, etc. But not `/api/post/create`
  * `pages/api/post/[...slug].js` - Will match `/api/post/1/2`, `/api/post/a/b/c`, etc. But not `/api/post/create`, `/api/post/abc`

## Streaming responses

While the Pages Router does support streaming responses with API Routes, we recommend incrementally adopting the App Router and using [Route Handlers](/docs/app/api-reference/file-conventions/route.md) if you are on Next.js 14+.

Here's how you can stream a response from an API Route with `writeHead`:

```ts filename="pages/api/hello.ts" switcher
import { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-store',
  })
  let i = 0
  while (i < 10) {
    res.write(`data: ${i}\n\n`)
    i++
    await new Promise((resolve) => setTimeout(resolve, 1000))
  }
  res.end()
}
```

```js filename="pages/api/hello.js" switcher
export default async function handler(req, res) {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-store',
  })
  let i = 0
  while (i < 10) {
    res.write(`data: ${i}\n\n`)
    i++
    await new Promise((resolve) => setTimeout(resolve, 1000))
  }
  res.end()
}
```


--------------------------------------------------------------------------------
title: "Custom Errors"
description: "Override and extend the built-in Error page to handle custom errors."
source: "https://nextjs.org/docs/pages/building-your-application/routing/custom-error"
--------------------------------------------------------------------------------

# Custom Errors

@router: Pages Router

## 404 Page

A 404 page may be accessed very often. Server-rendering an error page for every visit increases the load of the Next.js server. This can result in increased costs and slow experiences.

To avoid the above pitfalls, Next.js provides a static 404 page by default without having to add any additional files.

### Customizing The 404 Page

To create a custom 404 page you can create a `pages/404.js` file. This file is statically generated at build time.

```jsx filename="pages/404.js"
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>
}
```

> **Good to know**: You can use [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) inside this page if you need to fetch data at build time.

## 500 Page

Server-rendering an error page for every visit adds complexity to responding to errors. To help users get responses to errors as fast as possible, Next.js provides a static 500 page by default without having to add any additional files.

### Customizing The 500 Page

To customize the 500 page you can create a `pages/500.js` file. This file is statically generated at build time.

```jsx filename="pages/500.js"
export default function Custom500() {
  return <h1>500 - Server-side error occurred</h1>
}
```

> **Good to know**: You can use [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) inside this page if you need to fetch data at build time.

### More Advanced Error Page Customizing

500 errors are handled both client-side and server-side by the `Error` component. If you wish to override it, define the file `pages/_error.js` and add the following code:

```jsx
function Error({ statusCode }) {
  return (
    <p>
      {statusCode
        ? `An error ${statusCode} occurred on server`
        : 'An error occurred on client'}
    </p>
  )
}

Error.getInitialProps = ({ res, err }) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404
  return { statusCode }
}

export default Error
```

> `pages/_error.js` is only used in production. In development you’ll get an error with the call stack to know where the error originated from.

### Reusing the built-in error page

If you want to render the built-in error page you can by importing the `Error` component:

```jsx
import Error from 'next/error'

export async function getServerSideProps() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js')
  const errorCode = res.ok ? false : res.status
  const json = await res.json()

  return {
    props: { errorCode, stars: json.stargazers_count },
  }
}

export default function Page({ errorCode, stars }) {
  if (errorCode) {
    return <Error statusCode={errorCode} />
  }

  return <div>Next stars: {stars}</div>
}
```

The `Error` component also takes `title` as a property if you want to pass in a text message along with a `statusCode`.

If you have a custom `Error` component be sure to import that one instead. `next/error` exports the default component used by Next.js.

### Caveats

* `Error` does not currently support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching.md) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md).
* `_error`, like `_app`, is a reserved pathname. `_error` is used to define the customized layouts and behaviors of the error pages. `/_error` will render 404 when accessed directly via [routing](/docs/pages/building-your-application/routing.md) or rendering in a [custom server](/docs/pages/guides/custom-server.md).


--------------------------------------------------------------------------------
title: "Rendering"
description: "Learn the fundamentals of rendering in React and Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/rendering"
--------------------------------------------------------------------------------

# Rendering

@router: Pages Router

By default, Next.js **pre-renders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Pre-rendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive (this process is called [hydration](https://react.dev/reference/react-dom/client/hydrateRoot) in React).

### Pre-rendering

Next.js has two forms of pre-rendering: **Static Generation** and **Server-side Rendering**. The difference is in **when** it generates the HTML for a page.

* Static Generation: The HTML is generated at **build time** and will be reused on each request.
* Server-side Rendering: The HTML is generated on **each request**.

Importantly, Next.js lets you choose which pre-rendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

We recommend using Static Generation over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use client-side data fetching along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by clientside JavaScript. To learn more, take a look at the [Data Fetching](/docs/pages/building-your-application/data-fetching/client-side.md) documentation.

 - [Server-side Rendering (SSR)](/docs/pages/building-your-application/rendering/server-side-rendering.md)
 - [Static Site Generation (SSG)](/docs/pages/building-your-application/rendering/static-site-generation.md)
 - [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization.md)
 - [Client-side Rendering (CSR)](/docs/pages/building-your-application/rendering/client-side-rendering.md)

--------------------------------------------------------------------------------
title: "Server-side Rendering (SSR)"
description: "Use Server-side Rendering to render pages on each request."
source: "https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering"
--------------------------------------------------------------------------------

# Server-side Rendering (SSR)

@router: Pages Router

> Also referred to as "SSR" or "Dynamic Rendering".

If a page uses **Server-side Rendering**, the page HTML is generated on **each request**.

To use Server-side Rendering for a page, you need to `export` an `async` function called `getServerSideProps`. This function will be called by the server on every request.

For example, suppose that your page needs to pre-render frequently updated data (fetched from an external API). You can write `getServerSideProps` which fetches this data and passes it to `Page` like below:

```jsx
export default function Page({ data }) {
  // Render data...
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}
```

As you can see, `getServerSideProps` is similar to `getStaticProps`, but the difference is that `getServerSideProps` is run on every request instead of on build time.

To learn more about how `getServerSideProps` works, check out our [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/get-server-side-props.md).


--------------------------------------------------------------------------------
title: "Static Site Generation (SSG)"
description: "Use Static Site Generation (SSG) to pre-render pages at build time."
source: "https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation"
--------------------------------------------------------------------------------

# Static Site Generation (SSG)

@router: Pages Router

<details>
<summary>Examples</summary>

* [Agility CMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-agilitycms) ([Demo](https://next-blog-agilitycms.vercel.app/))
* [Builder.io Example](https://github.com/vercel/next.js/tree/canary/examples/cms-builder-io) ([Demo](https://cms-builder-io.vercel.app/))
* [ButterCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-buttercms) ([Demo](https://next-blog-buttercms.vercel.app/))
* [Contentful Example](https://github.com/vercel/next.js/tree/canary/examples/cms-contentful) ([Demo](https://app-router-contentful.vercel.app/))
* [Cosmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-cosmic) ([Demo](https://next-blog-cosmic.vercel.app/))
* [DatoCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-datocms) ([Demo](https://next-blog-datocms.vercel.app/))
* [DotCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-dotcms) ([Demo](https://nextjs-dotcms-blog.vercel.app/))
* [Drupal Example](https://github.com/vercel/next.js/tree/canary/examples/cms-drupal) ([Demo](https://cms-drupal.vercel.app/))
* [Enterspeed Example](https://github.com/vercel/next.js/tree/canary/examples/cms-enterspeed) ([Demo](https://next-blog-demo.enterspeed.com/))
* [GraphCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-graphcms) ([Demo](https://next-blog-graphcms.vercel.app/))
* [Keystone Example](https://github.com/vercel/next.js/tree/canary/examples/cms-keystonejs-embedded) ([Demo](https://nextjs-keystone-demo.vercel.app/))
* [Kontent.ai Example](https://github.com/vercel/next.js/tree/canary/examples/cms-kontent-ai) ([Demo](https://next-blog-kontent-ai.vercel.app/))
* [Makeswift Example](https://github.com/vercel/next.js/tree/canary/examples/cms-makeswift) ([Demo](https://nextjs-makeswift-example.vercel.app/))
* [Plasmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-plasmic) ([Demo](https://nextjs-plasmic-example.vercel.app/))
* [Prepr Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prepr) ([Demo](https://next-blog-prepr.vercel.app/))
* [Prismic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prismic) ([Demo](https://next-blog-prismic.vercel.app/))
* [Sanity Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sanity) ([Demo](https://next-blog.sanity.build/))
* [Sitecore XM Cloud Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sitecore-xmcloud) ([Demo](https://vercel-sitecore-xmcloud-demo.vercel.app/))
* [Storyblok Example](https://github.com/vercel/next.js/tree/canary/examples/cms-storyblok) ([Demo](https://next-blog-storyblok.vercel.app/))
* [Strapi Example](https://github.com/vercel/next.js/tree/canary/examples/cms-strapi) ([Demo](https://next-blog-strapi.vercel.app/))
* [TakeShape Example](https://github.com/vercel/next.js/tree/canary/examples/cms-takeshape) ([Demo](https://next-blog-takeshape.vercel.app/))
* [Tina Example](https://github.com/vercel/next.js/tree/canary/examples/cms-tina) ([Demo](https://cms-tina-example.vercel.app/))
* [Umbraco Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco) ([Demo](https://nextjs-umbraco-sample-blog.vercel.app/))
* [Umbraco Heartcore Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco-heartcore) ([Demo](https://next-blog-umbraco-heartcore.vercel.app/))
* [Webiny Example](https://github.com/vercel/next.js/tree/canary/examples/cms-webiny) ([Demo](https://webiny-headlesscms-nextjs-example.vercel.app/))
* [WordPress Example](https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress) ([Demo](https://next-blog-wordpress.vercel.app/))
* [Blog Starter Example](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([Demo](https://next-blog-starter.vercel.app/))
* [Static Tweet (Demo)](https://react-tweet.vercel.app/)

</details>

If a page uses **Static Generation**, the page HTML is generated at **build time**. That means in production, the page HTML is generated when you run `next build`. This HTML will then be reused on each request. It can be cached by a CDN.

In Next.js, you can statically generate pages **with or without data**. Let's take a look at each case.

### Static Generation without data

By default, Next.js pre-renders pages using Static Generation without fetching data. Here's an example:

```jsx
function About() {
  return <div>About</div>
}

export default About
```

Note that this page does not need to fetch any external data to be pre-rendered. In cases like this, Next.js generates a single HTML file per page during build time.

### Static Generation with data

Some pages require fetching external data for pre-rendering. There are two scenarios, and one or both might apply. In each case, you can use these functions that Next.js provides:

1. Your page **content** depends on external data: Use `getStaticProps`.
2. Your page **paths** depend on external data: Use `getStaticPaths` (usually in addition to `getStaticProps`).

#### Scenario 1: Your page content depends on external data

**Example**: Your blog page might need to fetch the list of blog posts from a CMS (content management system).

```jsx
// TODO: Need to fetch `posts` (by calling some API endpoint)
//       before this page can be pre-rendered.
export default function Blog({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li>{post.title}</li>
      ))}
    </ul>
  )
}
```

To fetch this data on pre-render, Next.js allows you to `export` an `async` function called `getStaticProps` from the same file. This function gets called at build time and lets you pass fetched data to the page's `props` on pre-render.

```jsx
export default function Blog({ posts }) {
  // Render posts...
}

// This function gets called at build time
export async function getStaticProps() {
  // Call an external API endpoint to get posts
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

To learn more about how `getStaticProps` works, check out the [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/get-static-props.md).

#### Scenario 2: Your page paths depend on external data

Next.js allows you to create pages with **dynamic routes**. For example, you can create a file called `pages/posts/[id].js` to show a single blog post based on `id`. This will allow you to show a blog post with `id: 1` when you access `posts/1`.

> To learn more about dynamic routing, check the [Dynamic Routing documentation](/docs/pages/building-your-application/routing/dynamic-routes.md).

However, which `id` you want to pre-render at build time might depend on external data.

**Example**: suppose that you've only added one blog post (with `id: 1`) to the database. In this case, you'd only want to pre-render `posts/1` at build time.

Later, you might add the second post with `id: 2`. Then you'd want to pre-render `posts/2` as well.

So your page **paths** that are pre-rendered depend on external data. To handle this, Next.js lets you `export` an `async` function called `getStaticPaths` from a dynamic page (`pages/posts/[id].js` in this case). This function gets called at build time and lets you specify which paths you want to pre-render.

```jsx
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
```

Also in `pages/posts/[id].js`, you need to export `getStaticProps` so that you can fetch the data about the post with this `id` and use it to pre-render the page:

```jsx
export default function Post({ post }) {
  // Render post...
}

export async function getStaticPaths() {
  // ...
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
```

To learn more about how `getStaticPaths` works, check out the [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/get-static-paths.md).

### When should I use Static Generation?

We recommend using **Static Generation** (with and without data) whenever possible because your page can be built once and served by CDN, which makes it much faster than having a server render the page on every request.

You can use Static Generation for many types of pages, including:

* Marketing pages
* Blog posts and portfolios
* E-commerce product listings
* Help and documentation

You should ask yourself: "Can I pre-render this page **ahead** of a user's request?" If the answer is yes, then you should choose Static Generation.

On the other hand, Static Generation is **not** a good idea if you cannot pre-render a page ahead of a user's request. Maybe your page shows frequently updated data, and the page content changes on every request.

In cases like this, you can do one of the following:

* Use Static Generation with **Client-side data fetching:** You can skip pre-rendering some parts of a page and then use client-side JavaScript to populate them. To learn more about this approach, check out the [Data Fetching documentation](/docs/pages/building-your-application/data-fetching/client-side.md).
* Use **Server-Side Rendering:** Next.js pre-renders a page on each request. It will be slower because the page cannot be cached by a CDN, but the pre-rendered page will always be up-to-date. We'll talk about this approach below.


--------------------------------------------------------------------------------
title: "Automatic Static Optimization"
description: "Next.js automatically optimizes your app to be static HTML whenever possible. Learn how it works here."
source: "https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization"
--------------------------------------------------------------------------------

# Automatic Static Optimization

@router: Pages Router

Next.js automatically determines that a page is static (can be prerendered) if it has no blocking data requirements. This determination is made by the absence of `getServerSideProps` and `getInitialProps` in the page.

This feature allows Next.js to emit hybrid applications that contain **both server-rendered and statically generated pages**.

> **Good to know**: Statically generated pages are still reactive. Next.js will hydrate your application client-side to give it full interactivity.

One of the main benefits of this feature is that optimized pages require no server-side computation, and can be instantly streamed to the end-user from multiple CDN locations. The result is an *ultra fast* loading experience for your users.

## How it works

If `getServerSideProps` or `getInitialProps` is present in a page, Next.js will switch to render the page on-demand, per-request (meaning [Server-Side Rendering](/docs/pages/building-your-application/rendering/server-side-rendering.md)).

If the above is not the case, Next.js will **statically optimize** your page automatically by prerendering the page to static HTML.

During prerendering, the router's `query` object will be empty since we do not have `query` information to provide during this phase. After hydration, Next.js will trigger an update to your application to provide the route parameters in the `query` object.

The cases where the query will be updated after hydration triggering another render are:

* The page is a [dynamic-route](/docs/pages/building-your-application/routing/dynamic-routes.md).
* The page has query values in the URL.
* [Rewrites](/docs/pages/api-reference/config/next-config-js/rewrites.md) are configured in your `next.config.js` since these can have parameters that may need to be parsed and provided in the `query`.

To be able to distinguish if the query is fully updated and ready for use, you can leverage the `isReady` field on [`next/router`](/docs/pages/api-reference/functions/use-router.md#router-object).

> **Good to know**: Parameters added with [dynamic routes](/docs/pages/building-your-application/routing/dynamic-routes.md) to a page that's using [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) will always be available inside the `query` object.

`next build` will emit `.html` files for statically optimized pages. For example, the result for the page `pages/about.js` would be:

```bash filename="Terminal"
.next/server/pages/about.html
```

And if you add `getServerSideProps` to the page, it will then be JavaScript, like so:

```bash filename="Terminal"
.next/server/pages/about.js
```

## Caveats

* If you have a [custom `App`](/docs/pages/building-your-application/routing/custom-app.md) with `getInitialProps` then this optimization will be turned off in pages without [Static Generation](/docs/pages/building-your-application/data-fetching/get-static-props.md).
* If you have a [custom `Document`](/docs/pages/building-your-application/routing/custom-document.md) with `getInitialProps` be sure you check if `ctx.req` is defined before assuming the page is server-side rendered. `ctx.req` will be `undefined` for pages that are prerendered.
* Avoid using the `asPath` value on [`next/router`](/docs/pages/api-reference/functions/use-router.md#router-object) in the rendering tree until the router's `isReady` field is `true`. Statically optimized pages only know `asPath` on the client and not the server, so using it as a prop may lead to mismatch errors. The [`active-class-name` example](https://github.com/vercel/next.js/tree/canary/examples/active-class-name) demonstrates one way to use `asPath` as a prop.


--------------------------------------------------------------------------------
title: "Client-side Rendering (CSR)"
description: "Learn how to implement client-side rendering in the Pages Router."
source: "https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering"
--------------------------------------------------------------------------------

# Client-side Rendering (CSR)

@router: Pages Router

In Client-Side Rendering (CSR) with React, the browser downloads a minimal HTML page and the JavaScript needed for the page. The JavaScript is then used to update the DOM and render the page. When the application is first loaded, the user may notice a slight delay before they can see the full page, this is because the page isn't fully rendered until all the JavaScript is downloaded, parsed, and executed.

After the page has been loaded for the first time, navigating to other pages on the same website is typically faster, as only necessary data needs to be fetched, and JavaScript can re-render parts of the page without requiring a full page refresh.

In Next.js, there are two ways you can implement client-side rendering:

1. Using React's `useEffect()` hook inside your pages instead of the server-side rendering methods ([`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props.md) and [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props.md)).
2. Using a data fetching library like [SWR](https://swr.vercel.app/) or [TanStack Query](https://tanstack.com/query/latest/) to fetch data on the client (recommended).

Here's an example of using `useEffect()` inside a Next.js page:

```jsx filename="pages/index.js"
import React, { useState, useEffect } from 'react'

export function Page() {
  const [data, setData] = useState(null)

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('https://api.example.com/data')
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      const result = await response.json()
      setData(result)
    }

    fetchData().catch((e) => {
      // handle the error as needed
      console.error('An error occurred while fetching the data: ', e)
    })
  }, [])

  return <p>{data ? `Your data: ${data}` : 'Loading...'}</p>
}
```

In the example above, the component starts by rendering `Loading...`. Then, once the data is fetched, it re-renders and displays the data.

Although fetching data in a `useEffect` is a pattern you may see in older React Applications, we recommend using a data-fetching library for better performance, caching, optimistic updates, and more. Here's a minimum example using [SWR](https://swr.vercel.app/) to fetch data on the client:

```jsx filename="pages/index.js"
import useSWR from 'swr'

export function Page() {
  const { data, error, isLoading } = useSWR(
    'https://api.example.com/data',
    fetcher
  )

  if (error) return <p>Failed to load.</p>
  if (isLoading) return <p>Loading...</p>

  return <p>Your Data: {data}</p>
}
```

> **Good to know**:
>
> Keep in mind that CSR can impact SEO. Some search engine crawlers might not execute JavaScript and therefore only see the initial empty or loading state of your application. It can also lead to performance issues for users with slower internet connections or devices, as they need to wait for all the JavaScript to load and run before they can see the full page. Next.js promotes a hybrid approach that allows you to use a combination of [server-side rendering](/docs/pages/building-your-application/rendering/server-side-rendering.md), [static site generation](/docs/pages/building-your-application/rendering/static-site-generation.md), and client-side rendering, **depending on the needs of each page** in your application. In the App Router, you can also use [Loading UI with Suspense](/docs/app/api-reference/file-conventions/loading.md) to show a loading indicator while the page is being rendered.


Learn about the alternative rendering methods in Next.js.

- [Server-side Rendering (SSR)](/docs/pages/building-your-application/rendering/server-side-rendering.md)
  - Use Server-side Rendering to render pages on each request.
- [Static Site Generation (SSG)](/docs/pages/building-your-application/rendering/static-site-generation.md)
  - Use Static Site Generation (SSG) to pre-render pages at build time.
- [ISR](/docs/pages/guides/incremental-static-regeneration.md)
  - Learn how to create or update static pages at runtime with Incremental Static Regeneration.


--------------------------------------------------------------------------------
title: "Data Fetching"
description: "Next.js allows you to fetch data in multiple ways, with pre-rendering, server-side rendering or static-site generation, and incremental static regeneration. Learn how to manage your application data in Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching"
--------------------------------------------------------------------------------

# Data Fetching

@router: Pages Router

Data fetching in Next.js allows you to render your content in different ways, depending on your application's use case. These include pre-rendering with **Server-side Rendering** or **Static Generation**, and updating or creating content at runtime with **Incremental Static Regeneration**.

## Examples

* [Agility CMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-agilitycms) ([Demo](https://next-blog-agilitycms.vercel.app/))
* [Builder.io Example](https://github.com/vercel/next.js/tree/canary/examples/cms-builder-io) ([Demo](https://cms-builder-io.vercel.app/))
* [ButterCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-buttercms) ([Demo](https://next-blog-buttercms.vercel.app/))
* [Contentful Example](https://github.com/vercel/next.js/tree/canary/examples/cms-contentful) ([Demo](https://app-router-contentful.vercel.app/))
* [Cosmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-cosmic) ([Demo](https://next-blog-cosmic.vercel.app/))
* [DatoCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-datocms) ([Demo](https://next-blog-datocms.vercel.app/))
* [DotCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-dotcms) ([Demo](https://nextjs-dotcms-blog.vercel.app/))
* [Drupal Example](https://github.com/vercel/next.js/tree/canary/examples/cms-drupal) ([Demo](https://cms-drupal.vercel.app/))
* [Enterspeed Example](https://github.com/vercel/next.js/tree/canary/examples/cms-enterspeed) ([Demo](https://next-blog-demo.enterspeed.com/))
* [GraphCMS Example](https://github.com/vercel/next.js/tree/canary/examples/cms-graphcms) ([Demo](https://next-blog-graphcms.vercel.app/))
* [Keystone Example](https://github.com/vercel/next.js/tree/canary/examples/cms-keystonejs-embedded) ([Demo](https://nextjs-keystone-demo.vercel.app/))
* [Kontent.ai Example](https://github.com/vercel/next.js/tree/canary/examples/cms-kontent-ai) ([Demo](https://next-blog-kontent-ai.vercel.app/))
* [Makeswift Example](https://github.com/vercel/next.js/tree/canary/examples/cms-makeswift) ([Demo](https://nextjs-makeswift-example.vercel.app/))
* [Plasmic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-plasmic) ([Demo](https://nextjs-plasmic-example.vercel.app/))
* [Prepr Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prepr) ([Demo](https://next-blog-prepr.vercel.app/))
* [Prismic Example](https://github.com/vercel/next.js/tree/canary/examples/cms-prismic) ([Demo](https://next-blog-prismic.vercel.app/))
* [Sanity Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sanity) ([Demo](https://next-blog.sanity.build/))
* [Sitecore XM Cloud Example](https://github.com/vercel/next.js/tree/canary/examples/cms-sitecore-xmcloud) ([Demo](https://vercel-sitecore-xmcloud-demo.vercel.app/))
* [Storyblok Example](https://github.com/vercel/next.js/tree/canary/examples/cms-storyblok) ([Demo](https://next-blog-storyblok.vercel.app/))
* [Strapi Example](https://github.com/vercel/next.js/tree/canary/examples/cms-strapi) ([Demo](https://next-blog-strapi.vercel.app/))
* [TakeShape Example](https://github.com/vercel/next.js/tree/canary/examples/cms-takeshape) ([Demo](https://next-blog-takeshape.vercel.app/))
* [Tina Example](https://github.com/vercel/next.js/tree/canary/examples/cms-tina) ([Demo](https://cms-tina-example.vercel.app/))
* [Umbraco Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco) ([Demo](https://nextjs-umbraco-sample-blog.vercel.app/))
* [Umbraco Heartcore Example](https://github.com/vercel/next.js/tree/canary/examples/cms-umbraco-heartcore) ([Demo](https://next-blog-umbraco-heartcore.vercel.app/))
* [Webiny Example](https://github.com/vercel/next.js/tree/canary/examples/cms-webiny) ([Demo](https://webiny-headlesscms-nextjs-example.vercel.app/))
* [WordPress Example](https://github.com/vercel/next.js/tree/canary/examples/cms-wordpress) ([Demo](https://next-blog-wordpress.vercel.app/))
* [Blog Starter Example](https://github.com/vercel/next.js/tree/canary/examples/blog-starter) ([Demo](https://next-blog-starter.vercel.app/))
* [Static Tweet (Demo)](https://react-tweet.vercel.app/)

 - [getStaticProps](/docs/pages/building-your-application/data-fetching/get-static-props.md)
 - [getStaticPaths](/docs/pages/building-your-application/data-fetching/get-static-paths.md)
 - [Forms and Mutations](/docs/pages/building-your-application/data-fetching/forms-and-mutations.md)
 - [getServerSideProps](/docs/pages/building-your-application/data-fetching/get-server-side-props.md)
 - [Client-side Fetching](/docs/pages/building-your-application/data-fetching/client-side.md)

--------------------------------------------------------------------------------
title: "getStaticProps"
description: "Fetch data and generate static pages with `getStaticProps`. Learn more about this API for data fetching in Next.js."
source: "https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./13-app-router.md) | [Index](./index.md) | [Next →](./15-getstaticprops.md)
