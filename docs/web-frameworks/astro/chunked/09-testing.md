**Navigation:** [← Previous](./08-migrating-from-nextjs.md) | [Index](./index.md) | [Next →](./10-upgrade-to-astro-v5.md)

---

# Testing

> An intro to testing in Astro

Testing helps you write and maintain working Astro code. Astro supports many popular tools for unit tests, component tests, and end-to-end tests including Jest, Mocha, Jasmine, [Cypress](https://cypress.io) and [Playwright](https://playwright.dev). You can even install framework-specific testing libraries such as React Testing Library to test your UI framework components.

Testing frameworks allow you to state **assertions** or **expectations** about how your code should behave in specific situations, then compare these to the actual behavior of your current code.

## Unit and integration tests

[Section titled “Unit and integration tests”](#unit-and-integration-tests)

### Vitest

[Section titled “Vitest”](#vitest)

A Vite-native unit test framework with ESM, TypeScript and JSX support powered by esbuild.

Use Astro’s `getViteConfig()` helper in your [`vitest.config.ts` configuration file](https://vitest.dev/config/) to set up Vitest with your Astro project’s settings:

vitest.config.ts

```js
/// <reference types="vitest/config" />
import { getViteConfig } from 'astro/config';


export default getViteConfig({
  test: {
    // Vitest configuration options
  },
});
```

By default, `getViteConfig()` will try to load an Astro config file in your project and apply it to the test environment. As of Astro 4.8, if you need to customize the Astro configuration applied in your tests, pass a second argument to `getViteConfig()`:

```js
export default getViteConfig(
  { test: { /* Vitest configuration options */ } },
  {
    site: 'https://example.com/',
    trailingSlash: 'always',
  },
);
```

See the [Astro + Vitest starter template](https://github.com/withastro/astro/tree/latest/examples/with-vitest) on GitHub.

#### Vitest and Container API

[Section titled “Vitest and Container API”](#vitest-and-container-api)

**Added in:** `astro@4.9.0`

You can natively test Astro components using the [container API](/en/reference/container-reference/). First, setup [`vitest` as explained above](#vitest), then create a `.test.js` file to test your component:

example.test.js

```js
import { experimental_AstroContainer as AstroContainer } from 'astro/container';
import { expect, test } from 'vitest';
import Card from '../src/components/Card.astro';


test('Card with slots', async () => {
  const container = await AstroContainer.create();
  const result = await container.renderToString(Card, {
    slots: {
      default: 'Card content',
    },
  });


  expect(result).toContain('This is a card');
  expect(result).toContain('Card content');
});
```

## End-to-end tests

[Section titled “End-to-end tests”](#end-to-end-tests)

### Playwright

[Section titled “Playwright”](#playwright)

Playwright is an end-to-end testing framework for modern web apps. Use the Playwright API in JavaScript or TypeScript to test your Astro code on all modern rendering engines including Chromium, WebKit, and Firefox.

#### Installation

[Section titled “Installation”](#installation)

You can get started and run your tests using the [VS Code Extension](https://playwright.dev/docs/getting-started-vscode).

Alternatively, you can install Playwright within your Astro project using the package manager of your choice. Follow the CLI steps to choose JavaScript/TypeScript, name your test folder, and add an optional GitHub Actions workflow.

* npm

  ```shell
  npm init playwright@latest
  ```

* pnpm

  ```shell
  pnpm create playwright
  ```

* Yarn

  ```shell
  yarn create playwright
  ```

#### Create your first Playwright test

[Section titled “Create your first Playwright test”](#create-your-first-playwright-test)

1. Choose a page to test. This example will test the example page `index.astro` below.

   src/pages/index.astro

   ```html
   ---
   ---
   <html lang="en">
     <head>
       <title>Astro is awesome!</title>
       <meta name="description" content="Pull content from anywhere and serve it fast with Astro's next-gen islands architecture." />
     </head>
     <body></body>
   </html>
   ```

2. Create a new folder and add the following test file in `src/test`. Copy and paste the following test into the file to verify that the page meta information is correct. Update the value of the page `<title>` to match the page you are testing.

   src/test/index.spec.ts

   ```jsx
   import { test, expect } from '@playwright/test';


   test('meta is correct', async ({ page }) => {
     await page.goto("http://localhost:4321/");


     await expect(page).toHaveTitle('Astro is awesome!');
   });
   ```

   Set a `baseUrl`

   You can set [`"baseURL": "http://localhost:4321"`](https://playwright.dev/docs/api/class-testoptions#test-options-base-url) in the `playwright.config.ts` configuration file to use `page.goto("/")` instead of `page.goto("http://localhost:4321/")` for a more convenient URL.

#### Running your Playwright tests

[Section titled “Running your Playwright tests”](#running-your-playwright-tests)

You can run a single test or several tests at once, testing one or multiple browsers. By default, your test results will be shown in the terminal. Optionally, you can open the HTML Test Reporter to show a full report and filter test results.

1. To run our test from the previous example using the command line, use the `test` command. Optionally, include the file name to run just the single test:

   ```sh
   npx playwright test index.spec.ts
   ```

2. To see the full HTML Test Report, open it using the following command:

   ```sh
   npx playwright show-report
   ```

Tip

Run your tests against your production code to more closely resemble your live, deployed site.

##### Advanced: Launching a development web server during the tests

[Section titled “Advanced: Launching a development web server during the tests”](#advanced-launching-a-development-web-server-during-the-tests)

You can also have Playwright start your server when you run your testing script by using the [`webServer`](https://playwright.dev/docs/test-advanced#launching-a-development-web-server-during-the-tests) option in the Playwright configuration file.

Here is an example of the configuration and commands required when using npm:

1. Add a test script to your `package.json` file in the project root, such as `"test:e2e": "playwright test"`.

2. In `playwright.config.ts`, add the `webServer` object and update the command value to `npm run preview`.

   playwright.config.ts

   ```diff
   import { defineConfig } from '@playwright/test';


   export default defineConfig({
   +  webServer: {
   +    command: 'npm run preview',
   +    url: 'http://localhost:4321/',
   +    timeout: 120 * 1000,
   +    reuseExistingServer: !process.env.CI,
   +  },
     use: {
       baseURL: 'http://localhost:4321/',
     },
   });
   ```

3. Run `npm run build`, then run `npm run test:e2e` to run the Playwright tests.

More information about Playwright can be found in the links below:

* [Getting started with Playwright](https://playwright.dev/docs/intro)
* [Use a development server](https://playwright.dev/docs/test-webserver#configuring-a-web-server)

### Cypress

[Section titled “Cypress”](#cypress)

Cypress is a front-end testing tool built for the modern web. Cypress enables you to write end-to-end tests for your Astro site.

#### Installation

[Section titled “Installation”](#installation-1)

You can install Cypress using the package manager of your choice. This will install Cypress locally as a dev dependency for your project.

* npm

  ```shell
  npm install cypress --save-dev
  ```

* pnpm

  ```shell
  pnpm add --save-dev cypress
  ```

* Yarn

  ```shell
  yarn add cypress --dev
  ```

#### Configuration

[Section titled “Configuration”](#configuration)

In the root of your project, create a `cypress.config.js` file with the following content:

cypress.config.js

```js
import { defineConfig } from 'cypress'


export default defineConfig({
  e2e: {
    supportFile: false
  }
})
```

#### Create your first Cypress test

[Section titled “Create your first Cypress test”](#create-your-first-cypress-test)

1. Choose a page to test. This example will test the example page `index.astro` below.

   src/pages/index.astro

   ```html
   ---
   ---
   <html lang="en">
     <head>
       <title>Astro is awesome!</title>
       <meta name="description" content="Pull content from anywhere and serve it fast with Astro's next-gen islands architecture." />
     </head>
     <body>
     <h1>Hello world from Astro</h1>
     </body>
   </html>
   ```

2. Create an `index.cy.js` file in the `cypress/e2e` folder. Use the following test in the file to verify that the page title and header are correct.

   cypress/e2e/index.cy.js

   ```js
   it('titles are correct', () => {
     const page = cy.visit('http://localhost:4321');


     page.get('title').should('have.text', 'Astro is awesome!')
     page.get('h1').should('have.text', 'Hello world from Astro');
   });
   ```

   Set a `baseUrl`

   You can set [`"baseUrl": "http://localhost:4321"`](https://docs.cypress.io/guides/end-to-end-testing/testing-your-app#Step-3-Configure-Cypress) in the `cypress.config.js` configuration file to use `cy.visit("/")` instead of `cy.visit("http://localhost:4321/")` for a more convenient URL.

#### Running your Cypress tests

[Section titled “Running your Cypress tests”](#running-your-cypress-tests)

Cypress can be run from the command line or from the Cypress App. The App provides a visual interface for running and debugging your tests.

First, start the dev server so Cypress can access your live site.

To run our test from the previous example using the command line, execute the following command:

```shell
npx cypress run
```

Alternatively, to run the test using the Cypress App, execute the following command:

```shell
npx cypress open
```

Once the Cypress App is launched, choose **E2E Testing**, then select the browser to be used to run tests.

Once the test run is finished, you should see green check marks in the output confirming that your test passed:

Output from npx cypress run

```shell
Running:  index.cy.js                                                                     (1 of 1)


✓ titles are correct (107ms)


1 passing (1s)
```

Fail the test

To check that your test really does work, you can change the following line in the `index.astro` file:

src/pages/index.astro

```diff
 <body>
   <h1>Hello world from Astro</h1>
   <h1>Hello from Astro</h1>
 </body>
```

Then run the test again. You should see a red “x” in the output confirming that your test failed.

#### Next steps

[Section titled “Next steps”](#next-steps)

More information about Cypress can be found in the links below:

* [Introduction to Cypress](https://docs.cypress.io/guides/core-concepts/introduction-to-cypress)
* [Testing Your App](https://docs.cypress.io/guides/end-to-end-testing/testing-your-app)

### NightwatchJS

[Section titled “NightwatchJS”](#nightwatchjs)

Nightwatch.js is a test automation framework with a powerful set of tools to write, run, and debug your tests across the web with built-in support for all major browsers and their mobile equivalents, as well as native mobile applications.

#### Installation

[Section titled “Installation”](#installation-2)

You can install NightwatchJS within your Astro project using the package manager of your choice. Follow the CLI steps to choose JavaScript/TypeScript, name your test folder, and select whether or not to include component testing and testing on mobile browsers.

* npm

  ```shell
  npm init nightwatch@latest
  ```

* pnpm

  ```shell
  pnpm create nightwatch
  ```

* Yarn

  ```shell
  yarn create nightwatch
  ```

#### Create your first Nightwatch test

[Section titled “Create your first Nightwatch test”](#create-your-first-nightwatch-test)

1. Choose a page to test. This example will test the example page `index.astro` below.

   src/pages/index.astro

   ```html
   ---
   ---
   <html lang="en">
     <head>
       <title>Astro is awesome!</title>
       <meta name="description" content="Pull content from anywhere and serve it fast with Astro's next-gen islands architecture." />
     </head>
     <body></body>
   </html>
   ```

2. Create a new folder `src/test/` and add the following test file:

   src/test/index.js

   ```js
   describe('Astro testing with Nightwatch', function () {
       before(browser => browser.navigateTo('http://localhost:4321/'));


       it("check that the title is correct", function (browser) {
           browser.assert.titleEquals('Astro is awesome!')
       });


       after(browser => browser.end());
   });
   ```

   Set a `baseUrl`

   You can set [`"baseURL": "http://localhost:4321"`](https://nightwatchjs.org/guide/reference/settings.html#setting-the-baseurl-property) in the `nightwatch.conf.js` configuration file to use `browser.navigateTo("/")` instead of `browser.navigateTo("http://localhost:4321/")` for a more convenient URL.

#### Running your NightwatchJS tests

[Section titled “Running your NightwatchJS tests”](#running-your-nightwatchjs-tests)

You can run a single test or several tests at once, testing one or multiple browsers. By default, your test results will be shown in the terminal. Optionally, you can open the HTML Test Reporter to show a full report and filter test results.

You can run the tests with the [NightwatchJS VSCode Extension](https://marketplace.visualstudio.com/items?itemName=browserstackcom.nightwatch) or using the CLI steps below:

1. To run all tests, enter the following command in the terminal. Optionally, include the file name to run just the single test:

   ```sh
   npx nightwatch test/index.js
   ```

   Additionally, you can run the tests against a specific browser using the `--environment` or `-e` CLI argument. If you don’t have the relevant browser installed, Nightwatch will attempt to set it up for you using [Selenium Manager](https://www.selenium.dev/blog/2022/introducing-selenium-manager/):

   ```sh
   npx nightwatch test/index.ts -e firefox
   ```

2. To see the full HTML Test Report, open it using the following command:

   ```sh
   npx nightwatch test/index.ts --open
   ```

Tip

Run your tests against your production code to more closely resemble your live, deployed site.

More information about NightwatchJS can be found in the links below:

* [Intro to Nightwatch](https://nightwatchjs.org/guide/overview/what-is-nightwatch.html)
* [Testing with Nightwatch](https://nightwatchjs.org/guide/writing-tests/introduction.html)

# Troubleshooting

> Need help? Stuck on something? We've got you covered.

Astro provides several different tools to help you troubleshoot and debug your code.

## Tips and tricks

[Section titled “Tips and tricks”](#tips-and-tricks)

### Debugging with `console.log()`

[Section titled “Debugging with console.log()”](#debugging-with-consolelog)

`console.log()` is a simple-but-popular method of debugging your Astro code. Where you write your `console.log()` statement will determine where your debugging output is printed:

```astro
---
console.log('Hi! I’m the server. This is logged in the terminal where Astro is running.');
---


<script>
console.log('Hi! I’m the client. This is logged in browser dev console.');
</script>
```

A `console.log()` statement in Astro frontmatter will always output to the **terminal** running the Astro CLI. This is because Astro runs on the server, and never in the browser.

Code that is written or imported inside of an Astro `<script>` tag is run in the browser. Any `console.log()` statements or other debug output will be printed to the **console in your browser**.

### Debugging framework components

[Section titled “Debugging framework components”](#debugging-framework-components)

[Framework components](/en/guides/framework-components/) (like React and Svelte) are unique: They render server-side by default, meaning that `console.log()` debug output will be visible in the terminal. However, they can also be hydrated for the browser, which may cause your debug logs to also appear in the browser.

This can be useful for debugging differences between the server output and the hydrated components in the browser.

### Astro `<Debug />` component

[Section titled “Astro \<Debug /> component”](#astro-debug--component)

To help you debug your Astro components, Astro provides a built-in `<Debug />` component which renders any value directly into your component HTML template.

This component provides a way to inspect values on the client-side, without any JavaScript. It can be useful for quick debugging in the browser without having to flip back-and-forth between your terminal and your browser.

```astro
---
import { Debug } from 'astro:components';
const sum = (a, b) => a + b;
---


<!-- Example: Outputs {answer: 6} to the browser -->
<Debug answer={sum(2, 4)} />
```

The Debug component supports a variety of syntax options for even more flexible and concise debugging:

```astro
---
import { Debug } from 'astro:components';
const sum = (a, b) => a + b;
const answer = sum(2, 4);
---
<!-- Example: All three examples are equivalent. -->
<Debug answer={sum(2, 4)} />
<Debug {{answer: sum(2, 4)}} />
<Debug {answer} />
```

## Common Error Messages

[Section titled “Common Error Messages”](#common-error-messages)

Here are some common error messages you might see in the terminal, what they might mean, and what to do about them. See our [full error reference guide](/en/reference/error-reference/) for a complete list of Astro errors you may encounter.

### Cannot use import statement outside a module

[Section titled “Cannot use import statement outside a module”](#cannot-use-import-statement-outside-a-module)

In Astro components, `<script>` tags are loaded as [JS modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) by default. If you have included the [`is:inline` directive](/en/reference/directives-reference/#isinline) or any other attribute in your tag, this default behavior is removed.

**Solution**: If you have added any attributes to your `<script>` tag, you must also add the `type="module"` attribute to be able to use import statements.

**Status**: Expected Astro behavior, as intended.

**Not sure that this is your problem?**\
Check to see if anyone else has reported [this issue](https://github.com/withastro/astro/issues?q=is%3Aissue+is%3Aopen+Cannot+use+import+statement)!

### `document` (or `window`) is not defined

[Section titled “document (or window) is not defined”](#document-or-window-is-not-defined)

This error occurs when trying to access `document` or `window` on the server.

Astro components run on the server, so you can’t access these browser-specific objects within the frontmatter.

Framework components run on the server by default, so this error can occur when accessing `document` or `window` during rendering.

**Solution**: Determine the code that calls `document` or `window`. If you aren’t using `document` or `window` directly and still getting this error, check to see if any packages you’re importing are meant to run on the client.

* If the code is in an Astro component, move it to a `<script>` tag outside of the frontmatter. This tells Astro to run this code on the client, where `document` and `window` are available.

* If the code is in a framework component, try to access these objects after rendering using lifecycle methods (e.g. [`useEffect()`](https://react.dev/reference/react/useEffect) in React, [`onMounted()`](https://vuejs.org/api/composition-api-lifecycle.html#onmounted) in Vue, and [`onMount()`](https://svelte.dev/docs#run-time-svelte-onmount) in Svelte). Tell the framework component to hydrate client-side by using a [client:](/en/reference/directives-reference/#client-directives) directive, like `client:load`, to run these lifecycle methods. You can also prevent the component from rendering on the server at all by adding the [`client:only`](/en/reference/directives-reference/#clientonly) directive.

**Status**: Expected Astro behavior, as intended.

### Expected a default export

[Section titled “Expected a default export”](#expected-a-default-export)

This error can be thrown when trying to import or render an invalid component, or one that is not working properly. (This particular message occurs because of the way importing a UI component works in Astro.)

**Solution**: Try looking for errors in any component you are importing and rendering, and make sure it’s working correctly. Consider opening an Astro starter template from [astro.new](https://astro.new) and troubleshooting just your component in a minimal Astro project.

**Status**: Expected Astro behavior, as intended.

### Refused to execute inline script

[Section titled “Refused to execute inline script”](#refused-to-execute-inline-script)

You may see the following error logged in the browser console:

> Refused to execute inline script because it violates the following Content Security Policy directive: …

This means that your site’s [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) (CSP) disallows running inline `<script>` tags, which Astro outputs by default.

**Solution:** Update your CSP to include `script-src: 'unsafe-inline'` to allow inline scripts to run. Alternatively, you can use a third-party integration such as [`astro-shield`](https://github.com/KindSpells/astro-shield) to generate the CSP headers for you.

## Common gotchas

[Section titled “Common gotchas”](#common-gotchas)

### My component is not rendering

[Section titled “My component is not rendering”](#my-component-is-not-rendering)

First, check to see that you have **imported the component** in your [`.astro` component script](/en/basics/astro-components/#the-component-script) or [`.mdx` file](/en/guides/integrations-guide/mdx/#using-components-in-mdx).

Then check your import statement:

* Is your import linking to the wrong place? (Check your import path.)

* Does your import have the same name as the imported component? (Check your component name and that it [follows the `.astro` syntax](/en/reference/astro-syntax/#differences-between-astro-and-jsx).)

* Have you included the extension in the import? (Check that your imported file contains an extension. e.g. `.astro`, `.md`, `.vue`, `.svelte`. Note: File extensions are **not** required for `.js(x)` and `.ts(x)` files only.)

### My component is not interactive

[Section titled “My component is not interactive”](#my-component-is-not-interactive)

If your component is rendering (see above) but is not responding to user interaction, then you may be missing a [`client:*` directive](/en/reference/directives-reference/#client-directives) to hydrate your component.

By default, a [UI Framework component is not hydrated in the client](/en/guides/framework-components/#hydrating-interactive-components). If no `client:*` directive is provided, its HTML is rendered onto the page without JavaScript.

Tip

[Astro components](/en/basics/astro-components/) are HTML-only templating components with no client-side runtime. But, you can use a `<script>` tag in your Astro component template to send JavaScript to the browser that executes in the global scope.

### Cannot find package ‘X’

[Section titled “Cannot find package ‘X’”](#cannot-find-package-x)

If you see a `"Cannot find package 'react'"` (or similar) warning when you start up Astro, that means that you need to install that package into your project. Not all package managers will install peer dependencies for you automatically. If you are on Node v16+ and using npm, you should not need to worry about this section.

React, for example, is a peer dependency of the `@astrojs/react` integration. That means that you should install the official `react` and `react-dom` packages alongside your integration. The integration will then pull from these packages automatically.

```shell
# Example: Install integrations and frameworks together
npm install @astrojs/react react react-dom
```

See [Astro’s integration guide](/en/guides/integrations-guide/) for instructions on adding framework renderers, CSS tools and other packages to Astro.

### Using Astro with Yarn 2+ (Berry)

[Section titled “Using Astro with Yarn 2+ (Berry)”](#using-astro-with-yarn-2-berry)

Yarn 2+, a.k.a. Berry, uses a technique called [Plug’n’Play (PnP)](https://yarnpkg.com/features/pnp) to store and manage Node modules, which can [cause problems](https://github.com/withastro/astro/issues/3450) while initializing a new Astro project using `create astro` or while working with Astro. A workaround is to set the [`nodeLinker` property](https://yarnpkg.com/configuration/yarnrc#nodeLinker) in `.yarnrc.yml` to `node-modules`:

.yarnrc.yml

```yaml
nodeLinker: "node-modules"
```

### Adding dependencies to Astro in a monorepo

[Section titled “Adding dependencies to Astro in a monorepo”](#adding-dependencies-to-astro-in-a-monorepo)

When working with Astro in a monorepo setup, project dependencies should be added in each project’s own `package.json` file.

However, you may also want to use Astro in the root of the monorepo (e.g. [Nx projects recommend installing dependencies at the root](https://github.com/nrwl/nx/issues/3023#issuecomment-630558318)). In this case, manually add Astro-related dependencies (e.g. `@astrojs/vue`, `astro-component-lib`) to the `vite.ssr.noExternal` part of Astro’s config to ensure that these dependencies are properly installed and bundled:

astro.config.mjs

```js
import { defineConfig } from 'astro/config'
export default defineConfig({
  vite: {
    ssr: {
      noExternal: [
        '@astrojs/vue',
        'astro-component-lib',
      ]
    }
  }
})
```

### Using `<head>` in a component

[Section titled “Using \<head> in a component”](#using-head-in-a-component)

In Astro, using a `<head>` tag works like any other HTML tag: it does not get moved to the top of the page or merged with the existing `<head>`. Because of this, you usually only want to include one `<head>` tag throughout a page. We recommend writing that single `<head>` and its contents in a [layout component](/en/basics/layouts/).

### An unexpected `<style>` is included

[Section titled “An unexpected \<style> is included”](#an-unexpected-style-is-included)

You may notice an imported component’s `<style>` tag included in your HTML source even if that component doesn’t appear in the final output. For example, this will occur with [conditionally rendered](/en/reference/astro-syntax/#dynamic-html) components that are not displayed.

Astro’s build process works on the module graph: once a component is included in the template, its `<style>` tag is processed, optimized, and bundled, whether it appears in the final output or not.

### Escaping special characters in Markdown

[Section titled “Escaping special characters in Markdown”](#escaping-special-characters-in-markdown)

Certain characters have a special meaning in Markdown. You may need to use a different syntax if you want to display them. To do this, you can use [HTML entities](https://developer.mozilla.org/en-US/docs/Glossary/Entity) for these characters instead.

For example, to prevent `<` being interpreted as the beginning of an HTML element, write `&lt;`.

## Creating minimal reproductions

[Section titled “Creating minimal reproductions”](#creating-minimal-reproductions)

When troubleshooting your code, it can be helpful to create a **minimal reproduction** of the issue that you can share. This is a smaller, simplified Astro project that demonstrates your issue. Having a working reproduction in a new project helps to confirm that this is a repeatable problem, and is not caused by something else in your personal environment or existing project.

Sharing a minimal reproduction is helpful when asking for help in our support threads and is often required when filing a bug report to Astro.

### Create a StackBlitz via [astro.new](https://astro.new/repro)

[Section titled “Create a StackBlitz via astro.new”](#create-a-stackblitz-via-astronew)

You can use [astro.new](https://astro.new/repro) to create a new Astro project with a single click. For minimal reproductions, we strongly recommend starting from the minimal (empty) example running in [StackBlitz](https://stackblitz.com), with as little extra code as possible.

StackBlitz will run this Astro project in the browser, outside of your local environment. It will also provide you with a shareable link so that any Astro maintainer or support squad member can view your minimal reproduction outside of their own local environment. This means that everyone is viewing the exact same project, with the same configuration and dependencies. This makes it easy for someone else to help troubleshoot your code. If the issue is reproducible, it allows you to verify that the issue lies within the Astro code itself and you can feel confident submitting a bug report.

Note that not every issue is reproducible in StackBlitz. For example, your issue might be dependent on a specific environment or package manager, or it may involve HTML Streaming, which isn’t supported in StackBlitz. In this case, create a new minimal (empty) Astro project using the CLI, reproduce the issue, and upload it to a GitHub repository. Instead of sharing a StackBlitz URL, provide a link to the GitHub repository of your minimal reproduction.

### Minimal code

[Section titled “Minimal code”](#minimal-code)

Once your empty project is set up, go through the steps to reproduce the issue. This can include adding packages, changing configuration, and writing code.

You should only add the minimum amount of code necessary to reproduce the issue. Do not reproduce other elements of your existing project, and remove all code that is not directly related to the issue.

### Create an issue

[Section titled “Create an issue”](#create-an-issue)

If your issue can be reproduced, then it is time to create an issue and file a bug report!

Go to the appropriate Astro repository on GitHub and open a new issue. Most repositories have an issue template that will ask questions or require information in order to submit. It’s important that you follow these templates because if you don’t provide the information we need, then we have to ask you for it… and no one is working on your issue!

Include the link to your minimal reproduction on StackBlitz (or GitHub repository, if necessary). Start with a description of the expected versus actual behavior to provide context for the issue. Then, include clear, step-by-step instructions on how to replicate the issue in an Astro project.

## Need more?

[Section titled “Need more?”](#need-more)

Come and chat with us on [Discord](https://astro.build/chat) and explain your issue in the `#support` forum channel. We’re always happy to help!

Visit the current [open Issues in Astro](https://github.com/withastro/astro/issues/) to see if you are encountering a known problem or file a bug report.

You can also visit [RFC Discussions](https://github.com/withastro/rfcs/discussions/) to see whether you’ve found a known limitation of Astro, and check to see whether there are current proposals related to your use case.

# TypeScript

> Learn how to use Astro's built-in TypeScript support.

Astro ships with built-in support for [TypeScript](https://www.typescriptlang.org/). You can import `.ts` and `.tsx` files in your Astro project, write TypeScript code directly inside your [Astro component](/en/basics/astro-components/#the-component-script), and even use an [`astro.config.ts`](/en/guides/configuring-astro/#the-astro-config-file) file for your Astro configuration if you like.

Using TypeScript, you can prevent errors at runtime by defining the shapes of objects and components in your code. For example, if you use TypeScript to [type your component’s props](#component-props), you’ll get an error in your editor if you set a prop that your component doesn’t accept.

You don’t need to write TypeScript code in your Astro projects to benefit from it. Astro always treats your component code as TypeScript, and the [Astro VS Code Extension](/en/editor-setup/) will infer as much as it can to provide autocompletion, hints, and errors in your editor.

The Astro dev server won’t perform any type checking, but you can use a [separate script](#type-checking) to check for type errors from the command line.

## Setup

[Section titled “Setup”](#setup)

Astro starter projects include a `tsconfig.json` file in your project. Even if you don’t write TypeScript code, this file is important so that tools like Astro and VS Code know how to understand your project. Some features (like npm package imports) aren’t fully supported in the editor without a `tsconfig.json` file. If you install Astro manually, be sure to create this file yourself.

### TSConfig templates

[Section titled “TSConfig templates”](#tsconfig-templates)

Three extensible `tsconfig.json` templates are included in Astro: `base`, `strict`, and `strictest`. The `base` template enables support for modern JavaScript features and is also used as a basis for the other templates. We recommend using `strict` or `strictest` if you plan to write TypeScript in your project. You can view and compare the three template configurations at [astro/tsconfigs/](https://github.com/withastro/astro/blob/main/packages/astro/tsconfigs/).

To inherit from one of the templates, use [the `extends` setting](https://www.typescriptlang.org/tsconfig#extends):

tsconfig.json

```json
{
  "extends": "astro/tsconfigs/base"
}
```

Additionally, we recommend setting `include` and `exclude` as follows to benefit from Astro types and avoid checking built files:

tsconfig.json

```diff
{
  "extends": "astro/tsconfigs/base",
  +"include": [".astro/types.d.ts", "**/*"],
  +"exclude": ["dist"]
}
```

### TypeScript editor plugin

[Section titled “TypeScript editor plugin”](#typescript-editor-plugin)

The [Astro TypeScript plugin](https://www.npmjs.com/package/@astrojs/ts-plugin) can be installed separately when you are not using the [official Astro VS Code extension](https://marketplace.visualstudio.com/items?itemName=astro-build.astro-vscode). This plugin is automatically installed and configured by the VS Code extension, and you do not need to install both.

This plugin runs only in the editor. When running `tsc` in the terminal, `.astro` files are ignored entirely. Instead, you can use [the `astro check` CLI command](/en/reference/cli-reference/#astro-check) to check both `.astro` and `.ts` files.

This plugin also supports importing `.astro` files from `.ts` files (which can be useful for re-exporting).

* npm

  ```shell
  npm install @astrojs/ts-plugin
  ```

* pnpm

  ```shell
  pnpm add @astrojs/ts-plugin
  ```

* Yarn

  ```shell
  yarn add @astrojs/ts-plugin
  ```

Then, add the following to your `tsconfig.json`:

tsconfig.json

```json
{
  "compilerOptions": {
    "plugins": [
      {
        "name": "@astrojs/ts-plugin"
      },
    ],
  }
}
```

To check that the plugin is working, create a `.ts` file and import an Astro component into it. You should have no warning messages from your editor.

### UI Frameworks

[Section titled “UI Frameworks”](#ui-frameworks)

If your project uses a [UI framework](/en/guides/framework-components/), additional settings depending on the framework might be needed. Please see your framework’s TypeScript documentation for more information. ([Vue](https://vuejs.org/guide/typescript/overview.html#using-vue-with-typescript), [React](https://react-typescript-cheatsheet.netlify.app/docs/basic/setup), [Preact](https://preactjs.com/guide/v10/typescript), [Solid](https://www.solidjs.com/guides/typescript), [Svelte](https://svelte.dev/docs/svelte/typescript))

## Type Imports

[Section titled “Type Imports”](#type-imports)

Use explicit type imports and exports whenever possible.

```diff
-import { SomeType } from "./script";
+import type { SomeType } from "./script";
```

This way, you avoid edge cases where Astro’s bundler may try to incorrectly bundle your imported types as if they were JavaScript.

You can configure TypeScript to enforce type imports in your `tsconfig.json` file. Set [`verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig#verbatimModuleSyntax) to `true`. TypeScript will check your imports and tell you when `import type` should be used. This setting is enabled by default in all our presets.

tsconfig.json

```diff
{
  "compilerOptions": {
    +"verbatimModuleSyntax": true
  }
}
```

## Import Aliases

[Section titled “Import Aliases”](#import-aliases)

Astro supports import aliases that you define in your `tsconfig.json` `paths` configuration. [Read our imports guide](/en/guides/imports/#aliases) to learn more.

src/pages/about/nate.astro

```astro
---
import HelloWorld from "@components/HelloWorld.astro";
import Layout from "@layouts/Layout.astro";
---
```

tsconfig.json

```json
{
  "compilerOptions": {
    "paths": {
      "@components/*": ["./src/components/*"],
      "@layouts/*": ["./src/layouts/*"]
    }
  }
}
```

## Extending global types

[Section titled “Extending global types”](#extending-global-types)

You can create `src/env.d.ts` as a convention for adding custom types declarations, or to benefit from Astro types if you don’t have a `tsconfig.json`:

src/env.d.ts

```ts
// Custom types declarations
declare var myString: string;


// Astro types, not necessary if you already have a `tsconfig.json`
/// <reference path="../.astro/types.d.ts" />
```

### `window` and `globalThis`

[Section titled “window and globalThis”](#window-and-globalthis)

You may want to add a property to the global object. You can do this by adding top-level declarations using the `declare` keyword to your `env.d.ts` file:

src/env.d.ts

```ts
declare var myString: string;
declare function myFunction(): boolean;
```

This will provide typing to `globalThis.myString` and `globalThis.myFunction`, as well as `window.myString` and `window.myFunction`.

Note that `window` is only available in client-side code. `globalThis` is available both server-side and client-side, but its server-side value won’t be shared with the client.

If you only want to type a property on the `window` object, provide a `Window` interface instead:

src/env.d.ts

```ts
interface Window {
  myFunction(): boolean;
}
```

### Add non-standard attributes

[Section titled “Add non-standard attributes”](#add-non-standard-attributes)

You may want to define a type for custom attributes or CSS properties. You can extend the default JSX definitions to add non-standard attributes by redeclaring the `astroHTML.JSX` namespace in a `.d.ts` file.

src/env.d.ts

```ts
declare namespace astroHTML.JSX {
  interface HTMLAttributes {
    "data-count"?: number;
    "data-label"?: string;
  }


  // Add a CSS custom property to the style object
  interface CSSProperties {
    "--theme-color"?: "black" | "white";
  }
}
```

Note

`astroHTML` is injected globally inside `.astro` components. To use it in TypeScript files, use a [triple-slash directive](https://www.typescriptlang.org/docs/handbook/triple-slash-directives.html):

```ts
/// <reference types="astro/astro-jsx" />


type MyAttributes = astroHTML.JSX.ImgHTMLAttributes;
```

### Using imports

[Section titled “Using imports”](#using-imports)

You may want to extend global types by reusing types declared elsewhere in your project or from an external library. To do this, use [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import):

src/env.d.ts

```ts
type Product = {
  id: string;
  name: string;
  price: number;
};


declare namespace App {
  interface Locals {
    orders: Map<string, Product[]>
    session: import("./lib/server/session").Session | null;
    user: import("my-external-library").User;
  }
}
```

A `.d.ts` file is an [ambient module](https://www.typescriptlang.org/docs/handbook/modules/reference.html#ambient-modules) declaration. While its syntax is similar to ES modules, these files do not allow top-level imports/exports. If Typescript encounters one, the file will be considered a [module augmentation](https://www.typescriptlang.org/docs/handbook/declaration-merging.html#module-augmentation) and this will break your global types.

## Component Props

[Section titled “Component Props”](#component-props)

Astro supports typing your component props via TypeScript. To enable, add a TypeScript `Props` interface to your component frontmatter. An `export` statement may be used, but is not necessary. The [Astro VS Code Extension](/en/editor-setup/) will automatically look for the `Props` interface and give you proper TS support when you use that component inside another template.

src/components/HelloProps.astro

```diff
---
+interface Props {
+  name: string;
+  greeting?: string;
+}


const { greeting = "Hello", name } = Astro.props;
---
<h2>{greeting}, {name}!</h2>
```

### Common prop type patterns

[Section titled “Common prop type patterns”](#common-prop-type-patterns)

* If your component takes no props or slotted content, you can use `type Props = Record<string, never>`.
* If your component must be passed children to its default slot, you can enforce this by using `type Props = { children: any; };`.

## Type Utilities

[Section titled “Type Utilities”](#type-utilities)

**Added in:** `astro@1.6.0`

Astro comes with some built-in utility types for common prop type patterns. These are available under the `astro/types` entrypoint.

### Built-in HTML attributes

[Section titled “Built-in HTML attributes”](#built-in-html-attributes)

Astro provides the `HTMLAttributes` type to check that your markup is using valid HTML attributes. You can use these types to help build component props.

For example, if you were building a `<Link>` component, you could do the following to mirror the default HTML attributes for `<a>` tags in your component’s prop types.

src/components/Link.astro

```astro
---
import type { HTMLAttributes } from "astro/types";


// use a `type`
type Props = HTMLAttributes<"a">;


// or extend with an `interface`
interface Props extends HTMLAttributes<"a"> {
  myProp?: boolean;
}


const { href, ...attrs } = Astro.props;
---
<a href={href} {...attrs}>
  <slot />
</a>
```

### `ComponentProps` type

[Section titled “ComponentProps type”](#componentprops-type)

**Added in:** `astro@4.3.0`

This type export allows you to reference the `Props` accepted by another component, even if that component doesn’t export that `Props` type directly.

The following example shows using the `ComponentProps` utility from `astro/types` to reference a `<Button />` component’s `Props` types:

src/pages/index.astro

```astro
---
import type { ComponentProps } from "astro/types";
import Button from "./Button.astro";


type ButtonProps = ComponentProps<typeof Button>;
---
```

### Polymorphic type

[Section titled “Polymorphic type”](#polymorphic-type)

**Added in:** `astro@2.5.0`

Astro includes a helper to make it easier to build components that can render as different HTML elements with full type safety. This is useful for components like `<Link>` that can render as either `<a>` or `<button>` depending on the props passed to it.

The example below implements a fully-typed, polymorphic component that can render as any HTML element. The [`HTMLTag`](#built-in-html-attributes) type is used to ensure that the `as` prop is a valid HTML element.

```astro
---
import type { HTMLTag, Polymorphic } from "astro/types";


type Props<Tag extends HTMLTag> = Polymorphic<{ as: Tag }>;


const { as: Tag, ...props } = Astro.props;
---
<Tag {...props} />
```

### Infer `getStaticPaths()` types

[Section titled “Infer getStaticPaths() types”](#infer-getstaticpaths-types)

**Added in:** `astro@2.1.0`

Astro includes helpers for working with the types returned by your [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) function for dynamic routes.

You can get the type of [`Astro.params`](/en/reference/api-reference/#params) with `InferGetStaticParamsType` and the type of [`Astro.props`](/en/reference/api-reference/#props) with `InferGetStaticPropsType` or you can use `GetStaticPaths` to infer both at once:

src/pages/posts/\[...id].astro

```astro
---
import type {
  InferGetStaticParamsType,
  InferGetStaticPropsType,
  GetStaticPaths,
} from "astro";


export const getStaticPaths = (async () => {
  const posts = await getCollection("blog");
  return posts.map((post) => {
    return {
      params: { id: post.id },
      props: { draft: post.data.draft, title: post.data.title },
    };
  });
}) satisfies GetStaticPaths;


type Params = InferGetStaticParamsType<typeof getStaticPaths>;
type Props = InferGetStaticPropsType<typeof getStaticPaths>;


const { id } = Astro.params as Params;
//                   ^? { id: string; }


const { title } = Astro.props;
//                      ^? { draft: boolean; title: string; }
---
```

## Type checking

[Section titled “Type checking”](#type-checking)

To see type errors in your editor, please make sure that you have the [Astro VS Code extension](/en/editor-setup/) installed. Please note that the `astro start` and `astro build` commands will transpile the code with esbuild, but will not run any type checking. To prevent your code from building if it contains TypeScript errors, change your “build” script in `package.json` to the following:

package.json

```diff
{
  "scripts": {
    -"build": "astro build",
    +"build": "astro check && astro build",
  },
}
```

Note

`astro check` checks all the files included in your TypeScript project. To check types within Svelte and Vue files, you can use the [`svelte-check`](https://www.npmjs.com/package/svelte-check) and the [`vue-tsc`](https://www.npmjs.com/package/vue-tsc) packages respectively.

Read more about [`.ts` file imports](/en/guides/imports/#typescript) in Astro.

Read more about [TypeScript Configuration](https://www.typescriptlang.org/tsconfig/).

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Errors typing multiple JSX frameworks at the same time

[Section titled “Errors typing multiple JSX frameworks at the same time”](#errors-typing-multiple-jsx-frameworks-at-the-same-time)

An issue may arise when using multiple JSX frameworks in the same project, as each framework requires different, sometimes conflicting, settings inside `tsconfig.json`.

**Solution**: Set the [`jsxImportSource` setting](https://www.typescriptlang.org/tsconfig#jsxImportSource) to `react` (default), `preact` or `solid-js` depending on your most-used framework. Then, use a [pragma comment](https://www.typescriptlang.org/docs/handbook/jsx.html#configuring-jsx) inside any conflicting file from a different framework.

For the default setting of `jsxImportSource: react`, you would use:

```jsx
// For Preact
/** @jsxImportSource preact */


// For Solid
/** @jsxImportSource solid-js */
```

# Legacy v0.x Upgrade Guide

> Archived guide documenting changes between pre-v1 versions of Astro

This guide will help you upgrade through breaking changes in pre-v1 versions of Astro.

You can update your project’s version of Astro to the latest version using your package manager. If you’re using Astro integrations, you’ll also want to update those to the latest version.

* npm

  ```shell
  # updates the astro dependency:
  npm upgrade astro
  # or, to update all dependencies:
  npm upgrade
  ```

* pnpm

  ```shell
  # updates the astro dependency:
  pnpm upgrade astro
  # or, to update all dependencies:
  pnpm upgrade
  ```

* Yarn

  ```shell
  # updates the astro dependency:
  yarn upgrade astro
  # or, to update all dependencies:
  yarn upgrade
  ```

Read the guide below for major highlights and instructions on how to handle breaking changes.

## Astro 1.0

[Section titled “Astro 1.0”](#astro-10)

Astro v1.0 introduces some changes that you should be aware of when migrating from v0.x and v1.0-beta releases. See below for more details.

### Updated: Vite 3

[Section titled “Updated: Vite 3”](#updated-vite-3)

Astro v1.0 has upgraded from Vite 2 to [Vite 3](https://vite.dev/). We’ve handled most of the upgrade for you inside of Astro; however, some subtle Vite behaviors may still change between versions. Refer to the official [Vite Migration Guide](https://vite.dev/guide/migration.html#general-changes) if you run into trouble.

### Deprecated: `Astro.canonicalURL`

[Section titled “Deprecated: Astro.canonicalURL”](#deprecated-astrocanonicalurl)

You can now use the new [`Astro.url`](/en/reference/api-reference/#url) helper to construct your own canonical URL from the current page/request URL.

```js
// Before:
const canonicalURL = Astro.canonicalURL;
// After:
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
```

### Changed: Scoped CSS specificity

[Section titled “Changed: Scoped CSS specificity”](#changed-scoped-css-specificity)

[Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) will now be preserved in scoped CSS styles. This change will cause most scoped styles to *happen* to take precedence over global styles. But, this behavior is no longer explicitly guaranteed.

Technically, this is accomplished using [the `:where()` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:where) instead of using classes directly in Astro’s CSS output.

Let’s use the following style block in an Astro component as an example:

```astro
<style>
  div { color: red; } /* 0-0-1 specificity */
</style>
```

Previously, Astro would transform this into the following CSS, which has a specificity of `0-1-1` — a higher specificity than the source CSS:

```css
div.astro-XXXXXX { color: red; } /* 0-1-1 specificity */
```

Now, Astro wraps the class selector with `:where()`, maintaining the authored specificity:

```css
div:where(.astro-XXXXXX) { color: red; } /* 0-0-1 specificity */
```

The previous specificity increase made it hard to combine scoped styles in Astro with other CSS files or styling libraries (e.g. Tailwind, CSS Modules, Styled Components, Stitches). This change will allow Astro’s scoped styles to work consistently alongside them while still preserving the exclusive boundaries that prevent styles from applying outside the component.

Caution

When upgrading, please visually inspect your site output to make sure everything is styled as expected. If not, find your scoped style and increase the selector specificity manually to match the old behavior.

### Deprecated: Components and JSX in Markdown

[Section titled “Deprecated: Components and JSX in Markdown”](#deprecated-components-and-jsx-in-markdown)

Astro no longer supports components or JSX expressions in Markdown pages by default. For long-term support you should migrate to the [`@astrojs/mdx`](/en/guides/integrations-guide/mdx/) integration.

To make migrating easier, a new `legacy.astroFlavoredMarkdown` flag (removed in v2.0) can be used to re-enable previous Markdown features.

### Converting existing `.md` files to `.mdx`

[Section titled “Converting existing .md files to .mdx”](#converting-existing-md-files-to-mdx)

If you’re not familiar with MDX, here are some steps you can follow to quickly convert an existing “Astro Flavored Markdown” file to MDX. As you learn more about MDX, feel free to explore other ways of writing your pages!

1. Install the [`@astrojs/mdx`](/en/guides/integrations-guide/mdx/) integration.

2. Change your existing `.md` file extensions to `.mdx`

3. Remove any `setup:` properties from your frontmatter, and write any import statements below the frontmatter instead.

   src/pages/posts/my-post.mdx

   ```diff
   ---
   layout: '../../layouts/BaseLayout.astro'
   -setup: |
     import ReactCounter from '../../components/ReactCounter.jsx'
   title: 'Migrating to MDX'
   date: 2022-07-26
   tags: ["markdown", "mdx", "astro"]
   ---
   +import ReactCounter from '../../components/ReactCounter.jsx'


   # {frontmatter.title}


   Here is my counter component, working in MDX:


   <ReactCounter client:load />
   ```

4. Update any `Astro.glob()` statements that currently return `.md` files so that they will now return your `.mdx` files.

   Caution

   The object returned when importing `.mdx` files (including using Astro.glob) differs from the object returned when importing `.md` files. However, `frontmatter`, `file`, and `url` work identically.

5. Update any use of the `<Content />` component to use the default export when importing MDX:

   src/pages/index.astro

   ```astro
   ---
   // Multiple imports with Astro.glob
   const mdxPosts = await Astro.glob('./posts/*.mdx');
   ---


   {mdxPosts.map(Post => <Post.default />)}
   ```

   src/pages/index.astro

   ```astro
   ---
   // Import a single page
   import { default as About } from './about.mdx';
   ---


   <About />
   ```

Tip

While you are transitioning to MDX, you may wish to enable the `legacy.astroFlavoredMarkdown` flag (removed in v2.0) and include both **`.md` and `.mdx`** files, so that your site continues to function normally even before all your files have been converted. Here is one way you can do that:

```astro
---
const mdPosts = await Astro.glob('../pages/posts/*.md');
const mdxPosts = await Astro.glob('../pages/posts/*.mdx');
const allPosts = [...mdxPosts, ...mdPosts];
---
```

### `<Markdown />` Component Removed

[Section titled “\<Markdown /> Component Removed”](#markdown--component-removed)

Astro’s built-in `<Markdown />` component has been moved to a separate package. To continue using this component, you will now need to install `@astrojs/markdown-component` and update your imports accordingly. For more details, see [the `@astrojs/markdown` README](https://github.com/withastro/astro/tree/main/packages/markdown/component).

Tip

Astro now has support for [MDX](https://mdxjs.com/) through our [MDX integration](https://github.com/withastro/astro/tree/main/packages/integrations/mdx). MDX gives you the ability to include both Markdown and imported components in the same file. MDX can be good alternative for the `<Markdown />` component due to its large community and stable APIs.

## Migrate to v1.0.0-beta

[Section titled “Migrate to v1.0.0-beta”](#migrate-to-v100-beta)

On April 4, 2022 we released the Astro 1.0 Beta! 🎉

If you are coming from v0.25 or earlier, make sure you have read and followed the [v0.26 Migration Guide](#migrate-to-v026) below, which contained several major breaking changes.

The `v1.0.0-beta.0` release of Astro contained no breaking changes. Below are small changes that were introduced during the beta period.

### Changed: RSS Feeds

[Section titled “Changed: RSS Feeds”](#changed-rss-feeds)

RSS feeds should now be generated using the `@astrojs/rss` package, as described in our [RSS guide](/en/recipes/rss/).

## Migrate to v0.26

[Section titled “Migrate to v0.26”](#migrate-to-v026)

### New Configuration API

[Section titled “New Configuration API”](#new-configuration-api)

Our Configuration API has been redesigned to solve a few glaring points of confusion that had built up over the last year. Most of the configuration options have just been moved or renamed, which will hopefully be a quick update for most users. A few options have been refactored more heavily, and may require a few additional changes:

* `.buildOptions.site` has been replaced with `.site` (your deployed domain) and a new `.base` (your deployed subpath) option.
* `.markdownOptions` has been replaced with `.markdown`, a mostly similar config object with some small changes to simplify Markdown configuration.
* `.sitemap` has been moved into the [@astrojs/sitemap](https://www.npmjs.com/package/@astrojs/sitemap) integration.

If you run Astro with legacy configuration, you will see a warning with instructions on how to update. See our updated [Configuration Reference](/en/reference/configuration-reference/) for more information on upgrading.

Read [RFC0019](https://github.com/withastro/rfcs/blob/main/proposals/0019-config-finalization.md) for more background on these changes.

### New Markdown API

[Section titled “New Markdown API”](#new-markdown-api)

Astro v0.26 releases a brand new Markdown API for your content. This included three major user-facing changes:

* You can now `import`/`import()` markdown content directly using an ESM import.
* A new `Astro.glob()` API, for easier glob imports (especially for Markdown).
* **BREAKING CHANGE:** `Astro.fetchContent()` has been removed and replaced by `Astro.glob()`
* **BREAKING CHANGE:** Markdown objects have an updated interface.

```diff
// v0.25
-let allPosts = Astro.fetchContent('./posts/*.md');
// v0.26+
+let allPosts = await Astro.glob('./posts/*.md');
```

When migrating, be careful about the new Markdown object interface. Frontmatter, for example, has been moved to the `.frontmatter` property, so references like `post.title` should change to `post.frontmatter.title`.

This should solve many issues for Markdown users, including some nice performance boosts for larger sites.

Read [RFC0017](https://github.com/withastro/rfcs/blob/main/proposals/0017-markdown-content-redesign.md) for more background on these changes.

### New Default Script Behavior

[Section titled “New Default Script Behavior”](#new-default-script-behavior)

`<script>` tags in Astro components are now built, bundled and optimized by default. This completes a long-term move to make our Astro component syntax more consistent, matching the default-optimized behavior our `<style>` tags have today.

This includes a few changes to be aware of:

* **BREAKING:** `<script hoist>` is the new default `<script>` behavior. The `hoist` attribute has been removed. To use the new default behaviour, make sure there are no other attributes on the `<script>` tag. For example, remove `type="module"` if you were using it before.
* New `<script is:inline>` directive, to revert a `<script>` tag to previous default behavior (unbuilt, unbundled, untouched by Astro).
* New `<style is:inline>` directive, to leave a style tag inline in the page template (similar to previous `<script>` behavior).
* New `<style is:global>` directive to replace `<style global>` in a future release.

```diff
// v0.25
<script hoist type="module">
// v0.26+
<script>
```

See how to use [client-side scripts](/en/guides/client-side-scripts/) in Astro for full details.

Read [RFC0016](https://github.com/withastro/rfcs/blob/main/proposals/0016-style-script-defaults.md) for more background on these changes.

### Updated `Astro.request` API

[Section titled “Updated Astro.request API”](#updated-astrorequest-api)

`Astro.request` has been changed from our custom object to a standard `Request` object. This is part of a project to use more web standard APIs, especially where SSR is concerned.

This includes a few changes to be aware of:

* Change `Astro.request` to become a [Request](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.
* Move `Astro.request.params` to `Astro.params`.
* Move `Astro.request.canonicalURL` to `Astro.canonicalURL`.

Read [RFC0018](https://github.com/withastro/rfcs/blob/main/proposals/0018-astro-request.md) for more background on these changes.

### Other Changes

[Section titled “Other Changes”](#other-changes)

* Improve `Astro.slots` API to support passing arguments to function-based slots. This allows for more ergonomic utility components that accept a callback function as a child.
* Update CLI output formatting, especially around error reporting.
* Update `@astrojs/compiler`, fixing some bugs related to RegExp usage in frontmatter

## Migrate to v0.25

[Section titled “Migrate to v0.25”](#migrate-to-v025)

### Astro Integrations

[Section titled “Astro Integrations”](#astro-integrations)

The `renderers` config has been replaced by a new, official integration system! This unlocks some really exciting new features for Astro. You can read our [Using Integrations](/en/guides/integrations-guide/) guide for more details on how to use this new system.

Integrations replace our original `renderers` concept, and come with a few breaking changes and new defaults for existing users. These changes are covered below.

#### Removed: Built-in Framework Support

[Section titled “Removed: Built-in Framework Support”](#removed-built-in-framework-support)

Previously, React, Preact, Svelte, and Vue were all included with Astro by default. Starting in v0.25.0, Astro no longer comes with any built-in renderers. If you did not have a `renderers` configuration entry already defined for your project, you will now need to install those frameworks yourself.

Read our [step-by-step walkthrough](/en/guides/integrations-guide/) to learn how to add a new Astro integration for the framework(s) that you currently use.

#### Deprecated: Renderers

[Section titled “Deprecated: Renderers”](#deprecated-renderers)

Note

Read this section if you have custom “renderers” already defined in your configuration file.

The new integration system replaces the previous `renderers` system, including the published `@astrojs/renderer-*` packages on npm. Going forward, `@astrojs/renderer-react` becomes `@astrojs/react`, `@astrojs/renderer-vue` becomes `@astrojs/vue`, and so on.

**To migrate:** update Astro to `v0.25.0` and then run `astro dev` or `astro build` with your old configuration file containing the outdated `"renderers"` config. You will immediately see a notice telling you the exact changes you need to make to your `astro.config.mjs` file, based on your current config. You can also update your packages yourself, using the table below.

For a deeper walkthrough, read our [step-by-step guide](/en/guides/integrations-guide/) to learn how to replace existing renderers with a new Astro framework integration.

```diff
# Install your new integrations and frameworks:
# (Read the full walkthrough: https://docs.astro.build/en/guides/integrations-guide)
+npm install @astrojs/lit lit
+npm install @astrojs/react react react-dom
```

```diff
// Then, update your `astro.config.mjs` file:
// (Read the full walkthrough: https://docs.astro.build/en/guides/integrations-guide)
+import lit from '@astrojs/lit';
+import react from '@astrojs/react';


export default {
-  renderers: ['@astrojs/renderer-lit', '@astrojs/renderer-react'],
+  integrations: [lit(), react()],
}
```

| Deprecated Renderers on npm | v0.25+ Integrations on npm |
| --------------------------- | -------------------------- |
| @astrojs/renderer-react     | @astrojs/react             |
| @astrojs/renderer-preact    | @astrojs/preact            |
| @astrojs/renderer-solid     | @astrojs/solid-js          |
| @astrojs/renderer-vue       | @astrojs/vue               |
| @astrojs/renderer-svelte    | @astrojs/svelte            |

#### Handling Peer Dependencies

[Section titled “Handling Peer Dependencies”](#handling-peer-dependencies)

Note

Read this section if: You are on Node v14 **or** if you use any package manager other than npm.

Unlike the old renderers, integrations no longer mark the frameworks themselves (“react”, “svelte”, “vue”, etc.) as direct dependencies of the integration. Instead, you should now install your framework packages *in addition to* your integrations.

```shell
# Example: Install integrations and frameworks together
npm install @astrojs/react react react-dom
```

If you see a `"Cannot find package 'react'"` (or similar) warning when you start up Astro, that means that you need to install that package into your project. See our [note on peer dependencies](/en/guides/troubleshooting/#cannot-find-package-x) in the troubleshooting guide for more information.

If you are using `npm` & Node v16+, then this may be automatically handled for you by `npm`, since the latest version of `npm` (v7+) installs peer dependencies like this for you automatically. In that case, installing a framework like “react” into your project is an optional but still recommended step.

### Updated: Syntax Highlighting

[Section titled “Updated: Syntax Highlighting”](#updated-syntax-highlighting)

We love to find sensible defaults that “just work” out-of-the-box. As part of this, we decided to make [Shiki](https://github.com/shikijs/shiki) our new default syntax highlighter. This comes pre-configured with the `github-dark` theme, providing zero-config highlighting in your code blocks without extraneous CSS classes, stylesheets, or client-side JS.

Check our new syntax highlighting docs for full details. **If you prefer to keep Prism as your syntax highlighter,** set the `syntaxHighlight` option to `'prism'` in your project’s markdown configuration.

#### The `<Prism />` component has a new home

[Section titled “The \<Prism /> component has a new home”](#the-prism--component-has-a-new-home)

As part of our mission to keep Astro core as lean as possible, we’ve moved the built-in `Prism` component out of `astro/components` and into the `@astrojs/prism` package. You can now import this component from `@astrojs/prism` like so:

```astro
---
import { Prism } from '@astrojs/prism';
---
```

Since the `@astrojs/prism` package is still bundled with `astro` core, you won’t need to install anything new, nor add Prism as an integration! However, note that we *do* plan to extract `@astrojs/prism` (and Prism syntax highlighting in general) to a separate, installable package in the future. See the `<Prism />` component API reference for more details.

### CSS Parser Upgrade

[Section titled “CSS Parser Upgrade”](#css-parser-upgrade)

Our internal CSS parser has been updated, and comes with better support for advanced CSS syntax, like container queries. This should be a mostly invisible change for most users, but hopefully advanced users will enjoy the new CSS feature support.

## Migrate to v0.24

[Section titled “Migrate to v0.24”](#migrate-to-v024)

Note

The new build strategy is on by default on 0.24. If you run into a problem you can continue using the old build strategy by passing the `--legacy-build` flag. Please [open an issue](https://github.com/withastro/astro/issues/new/choose) so that we can resolve problems with the new build strategy.

0.24 introduced a new *static build* strategy that changes the behavior of a few features. In previous versions of Astro this was available behavior with an opt-in flag: `--experimental-static-build`.

To migrate for the transition, be aware of the following changes that will be required to move to this new build engine. You can make these changes to your codebase at any time so that you are ready ahead of schedule.

### Deprecated: `Astro.resolve()`

[Section titled “Deprecated: Astro.resolve()”](#deprecated-astroresolve)

`Astro.resolve()` allows you to get resolved URLs to assets that you might want to reference in the browser. This was most commonly used inside of `<link>` and `<img>` tags to load CSS files and images as needed. Unfortunately, this will no longer work due to Astro now building assets at *build time* rather than at *render time*. You’ll want to upgrade your asset references to one of the following future-proof options available going forward:

#### How to Resolve CSS Files

[Section titled “How to Resolve CSS Files”](#how-to-resolve-css-files)

**1. ESM Import (Recommended)**

**Example:** `import './style.css';` **When to use this:** If your CSS file lives inside of the `src/` directory, and you want automatic CSS build and optimization features.

Use an ESM import to add some CSS onto the page. Astro detects these CSS imports and then builds, optimizes, and adds the CSS to the page automatically. This is the easiest way to migrate from `Astro.resolve()` while keeping the automatic building/bundling that Astro provides.

```astro
---
// Example: Astro will include and optimize this CSS for you automatically
import './style.css';
---
<html><!-- Your page here --></html>
```

Importing CSS files should work anywhere that ESM imports are supported, including:

* JavaScript files
* TypeScript files
* Astro component frontmatter
* non-Astro components like React, Svelte, and others

When a CSS file is imported using this method, any `@import` statements are also resolved and inlined into the imported CSS file. All `url()` references are also resolved relative to the source file, and any `url()` referenced assets will be included in the final build.

**2. Absolute URL Path**

**Example:** `<link href="/style.css">` **When to use this:** If your CSS file lives inside of `public/`, and you prefer to create your HTML `link` element yourself.

You can reference any file inside of the `public/` directory by absolute URL path in your component template. This is a good option if you want to control the `<link>` tag on the page yourself. However, this approach also skips the CSS processing, bundling and optimizations that are provided by Astro when you use the `import` method described above.

We recommend using the `import` approach over the absolute URL approach since it provides the best possible CSS performance and features by default.

#### How to Resolve JavaScript Files

[Section titled “How to Resolve JavaScript Files”](#how-to-resolve-javascript-files)

**1. Absolute URL Path**

**Example:** `<script src="/some-external-script.js" />` **When to use this:** If your JavaScript file lives inside of `public/`.

You can reference any file inside of the `public/` directory by absolute URL path in your Astro component templates. This is a good default option for external scripts because it lets you control the `<script>` tag on the page yourself.

Note that this approach skips the JavaScript processing, bundling and optimizations that are provided by Astro when you use the `import` method described below. However, this may be preferred for any external scripts that have already been published and minified separately from Astro. If your script was downloaded from an external source, then this method is probably preferred.

**2. ESM Import via `<script hoist>`**

**Example:** `<script hoist>import './some-external-script.js';</script>` **When to use this:** If your external script lives inside of `src/` *and* it supports the ESM module type.

Use an ESM import inside of a `<script hoist>` element in your Astro template, and Astro will include the JavaScript file in your final build. Astro detects these JavaScript client-side imports and then builds, optimizes, and adds the JavaScript to the page automatically. This is the easiest way to migrate from `Astro.resolve()` while keeping the automatic building/bundling that Astro provides.

```astro
<script hoist>
  import './some-external-script.js';
</script>
```

Note that Astro will bundle this external script with the rest of your client-side JavaScript, and load it in the `type="module"` script context. Some older JavaScript files may not be written for the `module` context, in which case they may need to be updated to use this method.

#### How to Resolve Images & Other Assets

[Section titled “How to Resolve Images & Other Assets”](#how-to-resolve-images--other-assets)

**1. Absolute URL Path (Recommended)**

**Example:** `<img src="/penguin.png">` **When to use this:** If your asset lives inside of `public/`.

If you place your images inside of `public/` you can safely reference them by absolute URL path directly in your component templates. This is the simplest way to reference an asset that you can use today, and it is recommended for most users who are getting started with Astro.

**2. ESM Import**

**Example:** `import imgUrl from './penguin.png'` **When to use this:** If your asset lives inside of the `src/` directory, and you want automatic optimization features like filename hashing.

This works inside of any JavaScript or Astro component, and returns a resolved URL to the final image. Once you have the resolved URL, you can use it anywhere inside of the component template.

```astro
---
// Example: Astro will include this image file in your final build
import imgUrl from './penguin.png';
---
<img src={imgUrl} />
```

Similar to how Astro handles CSS, the ESM import allows Astro to perform some simple build optimizations for you automatically. For example, any asset inside of `src/` that is imported using an ESM import (ex: `import imgUrl from './penguin.png'`) will have its filename hashed automatically. This can let you cache the file more aggressively on the server, improving user performance. In the future, Astro may add more optimizations like this.

**Tip:** If you dislike static ESM imports, Astro also supports dynamic ESM imports. We only recommend this option if you prefer this syntax: `<img src={(await import('./penguin.png')).default} />`.

### Deprecated: `<script>` Default Processing

[Section titled “Deprecated: \<script> Default Processing”](#deprecated-script-default-processing)

Previously, all `<script>` elements were read from the final HTML output and processed + bundled automatically. This behavior is no longer the default. Starting in 0.24, you must opt-in to `<script>` element processing via the `hoist` attribute. The `type="module"` is also required for hoisted modules.

```astro
<script>
  // Will be rendered into the HTML exactly as written!
  // ESM imports will not be resolved relative to the file.
</script>
<script type="module" hoist>
  // Processed! Bundled! ESM imports work, even to npm packages.
</script>
```

## Migrate to v0.23

[Section titled “Migrate to v0.23”](#migrate-to-v023)

### Missing Sass Error

[Section titled “Missing Sass Error”](#missing-sass-error)

```plaintext
Preprocessor dependency "sass" not found. Did you install it?
```

In our quest to reduce npm install size, we’ve moved [Sass](https://sass-lang.com/) out to an optional dependency. If you use Sass in your project, you’ll want to make sure that you run `npm install sass --save-dev` to save it as a dependency.

### Deprecated: Unescaped HTML

[Section titled “Deprecated: Unescaped HTML”](#deprecated-unescaped-html)

In Astro v0.23+, unescaped HTML content in expressions is now deprecated. In future releases, content within expressions will have strings escaped to protect against unintended HTML injection.

```diff
<h1>{title}</h1> <!-- <h1>Hello <strong>World</strong></h1> -->
<h1>{title}</h1> <!-- <h1>Hello &lt;strong&gt;World&lt;/strong&gt;</h1> -->
```

To continue injecting unescaped HTML, you can now use `set:html`.

```diff
<h1>{title}</h1>
<h1 set:html={title} />
```

To avoid a wrapper element, `set:html` can work alongside `<Fragment>`.

```diff
<h1>{title}!</h1>
<h1><Fragment set:html={title}>!</h1>
```

You can also protect against unintended HTML injection with `set:text`.

```astro
<h1 set:text={title} /> <!-- <h1>Hello &lt;strong&gt;World&lt;/strong&gt;</h1> -->
```

## Migrate to v0.21

[Section titled “Migrate to v0.21”](#migrate-to-v021)

### Vite

[Section titled “Vite”](#vite)

Starting in v0.21, Astro is built with [Vite](https://vite.dev). As a result, configurations written in `snowpack.config.mjs` should be moved into `astro.config.mjs`.

```js
// @ts-check


/** @type {import('astro').AstroUserConfig} */
export default {
  renderers: [],
  vite: {
    plugins: [],
  },
};
```

To learn more about configuring Vite, please visit their [configuration guide](https://vite.dev/config/).

#### Vite Plugins

[Section titled “Vite Plugins”](#vite-plugins)

In Astro v0.21+, Vite plugins may be configured within `astro.config.mjs`.

```diff
import { imagetools } from 'vite-imagetools';


export default {
+  vite: {
+    plugins: [imagetools()],
+  },
};
```

To learn more about Vite plugins, please visit their [plugin guide](https://vite.dev/guide/using-plugins.html).

#### Vite Changes to Renderers

[Section titled “Vite Changes to Renderers”](#vite-changes-to-renderers)

In Astro v0.21+, plugins should now use `viteConfig()`.

renderer-svelte/index.js

```diff
+import { svelte } from '@sveltejs/vite-plugin-svelte';


export default {
  name: '@astrojs/renderer-svelte',
  client: './client.js',
  server: './server.js',
-  snowpackPlugin: '@snowpack/plugin-svelte',
-  snowpackPluginOptions: { compilerOptions: { hydratable: true } },
  +viteConfig() {
    +return {
+      optimizeDeps: {
+        include: ['@astrojs/renderer-svelte/client.js', 'svelte', 'svelte/internal'],
+        exclude: ['@astrojs/renderer-svelte/server.js'],
+      },
+      plugins: [
        +svelte({
+          emitCss: true,
+          compilerOptions: { hydratable: true },
+        }),
+      ],
+    };
+  },
}
```

To learn more about Vite plugins, please visit their [plugin guide](https://vite.dev/guide/using-plugins.html).

Note

In prior releases, these were configured with `snowpackPlugin` or `snowpackPluginOptions`.

### Aliasing

[Section titled “Aliasing”](#aliasing)

In Astro v0.21+, import aliases can be added in `tsconfig.json`.

```diff
{
  "compilerOptions": {
    "baseUrl": ".",
    +"paths": {
      +"@/components/*": ["src/components/*"]
+    }
  }
}
```

### File Extensions in Imports

[Section titled “File Extensions in Imports”](#file-extensions-in-imports)

In Astro v0.21+, files need to be referenced by their actual extension, exactly as it is on disk. In this example, `Div.tsx` would need to be referenced as `Div.tsx`, not `Div.jsx`.

```diff
-import Div from './Div.jsx' // Astro v0.20
+import Div from './Div.tsx' // Astro v0.21
```

This same change applies to a compile-to-css file like `Div.scss`:

```diff
<link rel="stylesheet" href={Astro.resolve('./Div.css')}>
<link rel="stylesheet" href={Astro.resolve('./Div.scss')}>
```

### Removed: Components in Frontmatter

[Section titled “Removed: Components in Frontmatter”](#removed-components-in-frontmatter)

Previously, you could create mini Astro Components inside of the Astro Frontmatter, using JSX syntax instead of Astro’s component syntax. This was always a bit of a hack, but in the new compiler it became impossible to support. We hope to re-introduce this feature in a future release of Astro using a different, non-JSX API.

To migrate to v0.21+, please convert all JSX Astro components (that is, any Astro components created inside of another component’s frontmatter) to standalone components.

### Styling Changes

[Section titled “Styling Changes”](#styling-changes)

#### Autoprefixer

[Section titled “Autoprefixer”](#autoprefixer)

Autoprefixer is no longer run by default. To enable:

1. Install the latest version (`npm install autoprefixer`)

2. Create a `postcss.config.cjs` file at the root of your project with:

   ```js
   module.exports = {
     plugins: {
       autoprefixer: {},
     },
   };
   ```

#### Tailwind CSS

[Section titled “Tailwind CSS”](#tailwind-css)

Ensure you have PostCSS installed. This was optional in previous releases, but is required now:

1. Install the latest version of postcss (`npm install -D postcss`)

2. Create a `postcss.config.cjs` file at the root of your project with:

   ```js
   module.exports = {
     plugins: {
       tailwindcss: {},
     },
   };
   ```

   For more information, read the [Tailwind CSS documentation](https://tailwindcss.com/docs/installation#add-tailwind-as-a-post-css-plugin)

### Known Issues

[Section titled “Known Issues”](#known-issues)

#### Imports on top

[Section titled “Imports on top”](#imports-on-top)

In Astro v0.21+, a bug has been introduced that requires imports inside components to be at the top of your frontmatter.

```astro
---
import Component from '../components/Component.astro'
const whereShouldIPutMyImports = "on top!"
---
```

# Upgrade to Astro v2

> How to upgrade your project to the latest version of Astro.

This guide will help you migrate from Astro v1 to Astro v2.

Need to upgrade an older project to v1? See our [older migration guide](/en/guides/upgrade-to/v1/).

## Upgrade Astro

[Section titled “Upgrade Astro”](#upgrade-astro)

Update your project’s version of Astro to the latest version using your package manager. If you’re using Astro integrations, please also update those to the latest version.

* npm

  ```shell
  # Upgrade to Astro v2.x
  npm install astro@latest


  # Example: upgrade React and Tailwind integrations
  npm install @astrojs/react@latest @astrojs/tailwind@latest
  ```

* pnpm

  ```shell
  # Upgrade to Astro v2.x
  pnpm add astro@latest


  # Example: upgrade React and Tailwind integrations
  pnpm add @astrojs/react@latest @astrojs/tailwind@latest
  ```

* Yarn

  ```shell
  # Upgrade to Astro v2.x
  yarn add astro@latest


  # Example: upgrade React and Tailwind integrations
  yarn add @astrojs/react@latest @astrojs/tailwind@latest
  ```

## Astro v2.0 Breaking Changes

[Section titled “Astro v2.0 Breaking Changes”](#astro-v20-breaking-changes)

Astro v2.0 includes some breaking changes, as well as the removal of some previously deprecated features. If your project doesn’t work as expected after upgrading to v2.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See [the changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for full release notes.

### Removed: Support for Node 14

[Section titled “Removed: Support for Node 14”](#removed-support-for-node-14)

Node 14 is scheduled to reach its End of Life in April 2023.

Astro v2.0 drops Node 14 support entirely, so that all Astro users can take advantage of Node’s more modern features.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do)

Check that both your development environment and your deployment environment are using **Node `16.12.0` or later**.

1. Check your local version of Node using:

   ```sh
   node -v
   ```

   If your local development environment needs upgrading, [install Node](https://nodejs.org/en/download/).

2. Check your [deployment environment’s](/en/guides/deploy/) own documentation to verify that they support Node 16.

   You can specify Node `16.12.0` for your Astro project either in a dashboard configuration setting, or a `.nvmrc` file.

### Reserved: `src/content/`

[Section titled “Reserved: src/content/”](#reserved-srccontent)

Astro v2.0 now includes the Collections API for organizing your Markdown and MDX files into [content collections](/en/guides/content-collections/). This API reserves `src/content/` as a special folder.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-1)

Rename an existing `src/content/` folder to avoid conflicts. This folder, if it exists, can now only be used for [content collections](/en/guides/content-collections/).

### Changed: `Astro.site` trailing slash

[Section titled “Changed: Astro.site trailing slash”](#changed-astrosite-trailing-slash)

In v1.x, Astro ensured the URL you set as `site` in `astro.config.mjs` always had a trailing slash when accessed using `Astro.site`.

Astro v2.0 no longer modifies the value of `site`. `Astro.site` will use the exact value defined, and a trailing slash must be specified if desired.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-2)

In `astro.config.mjs`, add a trailing slash to the URL set in `site`.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
-  site: 'https://example.com',
+  site: 'https://example.com/',
});
```

### Changed: `_astro/` folder for build assets

[Section titled “Changed: \_astro/ folder for build assets”](#changed-_astro-folder-for-build-assets)

In v1.x, assets were built to various locations, including `assets/`, `chunks/`, and to the root of the build output.

Astro v2.0 moves and unifies the location of all build output assets to a new `_astro/` folder.

* dist/

  * \_astro

    * client.9218e799.js
    * index.df3f880e0.css

You can control this location with the [new `build.assets` configuration option](/en/reference/configuration-reference/#buildassets).

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-3)

Update your deployment platform configuration if it relies on the location of these assets.

### Changed: Markdown plugin configuration

[Section titled “Changed: Markdown plugin configuration”](#changed-markdown-plugin-configuration)

#### Removed: `extendDefaultPlugins`

[Section titled “Removed: extendDefaultPlugins”](#removed-extenddefaultplugins)

In v1.x, Astro used `markdown.extendDefaultPlugins` to re-enable Astro’s default plugins when adding your own Markdown plugins.

Astro v2.0 removes this configuration option entirely because its behavior is now the default.

Applying remark and rehype plugins in your Markdown configuration **no longer disables Astro’s default plugins**. GitHub-Flavored Markdown and Smartypants are now applied whether or not custom `remarkPlugins` or `rehypePlugins` are configured.

##### What should I do?

[Section titled “What should I do?”](#what-should-i-do-4)

Remove `extendDefaultPlugins` in your configuration. This is now Astro’s default behavior in v2.0, and you can delete this line without any replacement.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
-    extendDefaultPlugins,
  }
});
```

#### Added: `gfm` and `smartypants`

[Section titled “Added: gfm and smartypants”](#added-gfm-and-smartypants)

In v1.x, you could choose to disable both of Astro’s default Markdown plugins (GitHub-Flavored Markdown and SmartyPants) by setting `markdown.extendDefaultPlugins: false`.

Astro v2.0 replaces `markdown.extendDefaultPlugins: false` with separate Boolean options to individually control each of Astro’s built-in default Markdown plugins. These are enabled by default and can be set to `false` independently.

##### What should I do?

[Section titled “What should I do?”](#what-should-i-do-5)

Remove `extendDefaultPlugins: false` and add the flags to disable each plugin individually instead.

* `markdown.gfm: false` disables GitHub-Flavored Markdown
* `markdown.smartypants: false` disables SmartyPants

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
  markdown: {
-    extendDefaultPlugins: false,
+    smartypants: false,
+    gfm: false,
  }
});
```

### Changed: MDX plugin configuration

[Section titled “Changed: MDX plugin configuration”](#changed-mdx-plugin-configuration)

#### Replaced: `extendPlugins` changed to `extendMarkdownConfig`

[Section titled “Replaced: extendPlugins changed to extendMarkdownConfig”](#replaced-extendplugins-changed-to-extendmarkdownconfig)

In v1.x, the MDX integration’s `extendPlugins` option managed how your MDX files should inherit your Markdown configuration: all your Markdown configuration (`markdown`), or Astro’s default plugins only (`default`).

Astro v2.0 replaces the behavior controlled by `mdx.extendPlugins` with three new, independently-configurable options that are `true` by default:

* **[`mdx.extendMarkdownConfig`](/en/guides/integrations-guide/mdx/#extendmarkdownconfig)** to inherit all or none of your Markdown configuration
* **`mdx.gfm`** to enable or disable GitHub-Flavored Markdown in MDX
* **`mdx.smartypants`** to enable or disable SmartyPants in MDX

##### What should I do?

[Section titled “What should I do?”](#what-should-i-do-6)

Delete `extendPlugins: 'markdown'` in your configuration. This is now the default behavior.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  integrations: [
    mdx({
-      extendPlugins: 'markdown',
    }),
  ],
});
```

Replace `extendPlugins: 'defaults'` with `extendMarkdownConfig: false` and add the separate options for GitHub-Flavored Markdown and SmartyPants to enable these default plugins individually in MDX.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  integrations: [
    mdx({
-      extendPlugins: 'defaults',
+      extendMarkdownConfig: false,
+      smartypants: true,
+      gfm: true,
    }),
  ],
});
```

#### Added: More MDX config options to match Markdown

[Section titled “Added: More MDX config options to match Markdown”](#added-more-mdx-config-options-to-match-markdown)

Astro v2.0 allows you to now individually set [every available Markdown configuration option](/en/reference/configuration-reference/#markdown-options) (except `drafts`) separately in your MDX integration configuration.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';


export default defineConfig({
  markdown: {
    remarkPlugins: [remarkPlugin1],
    gfm: true,
  },
  integrations: [
    mdx({
      remarkPlugins: [remarkPlugin2],
      gfm: false,
    })
  ]
});
```

##### What should I do?

[Section titled “What should I do?”](#what-should-i-do-7)

Revisit your Markdown and MDX configuration and compare your existing config with the new options available.

### Changed: Plugin access to frontmatter

[Section titled “Changed: Plugin access to frontmatter”](#changed-plugin-access-to-frontmatter)

In v1.x, remark and rehype plugins did not have access to user frontmatter. Astro merged plugin frontmatter with your file’s frontmatter, without passing the file frontmatter to your plugins.

Astro v2.0 gives remark and rehype plugins access to user frontmatter via frontmatter injection. This allows plugin authors to modify a user’s existing frontmatter, or compute new properties based on other properties.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-8)

Check any remark and rehype plugins you have written to see whether their behavior has changed. Note that `data.astro.frontmatter` is now the *complete* Markdown or MDX document’s frontmatter, rather than an empty object.

### Changed: RSS Configuration

[Section titled “Changed: RSS Configuration”](#changed-rss-configuration)

In v1.x, Astro’s RSS package allowed you to use `items: import.meta.glob(...)` to generate a list of RSS feed items. This usage is now deprecated and will eventually be removed.

Astro v2.0 introduces a `pagesGlobToRssItems()` wrapper to the `items` property.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-9)

Import, then wrap your existing function containing `import.meta.glob()` with the `pagesGlobToRssItems()` helper.

src/pages/rss.xml.js

```diff
import rss, {
+  pagesGlobToRssItems
} from '@astrojs/rss';


export async function get(context) {
  return rss({
+    items: await pagesGlobToRssItems(
      import.meta.glob('./blog/*.{md,mdx}'),
+    ),
  });
}
```

### Changed: Svelte IDE support

[Section titled “Changed: Svelte IDE support”](#changed-svelte-ide-support)

Astro v2.0 requires a `svelte.config.js` file in your project if you are using [the `@astrojs/svelte` integration](/en/guides/integrations-guide/svelte/). This is needed to provide IDE autocompletion.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-10)

Add a `svelte.config.js` file to the root of your project:

svelte.config.js

```js
import { vitePreprocess } from '@astrojs/svelte';


export default {
  preprocess: vitePreprocess(),
};
```

For new users, this file will be added automatically when running `astro add svelte`.

### Removed: `legacy.astroFlavoredMarkdown`

[Section titled “Removed: legacy.astroFlavoredMarkdown”](#removed-legacyastroflavoredmarkdown)

In v1.0, Astro moved the old Astro-Flavored Markdown (also known as Components in Markdown) to a legacy feature.

Astro v2.0 removes the `legacy.astroFlavoredMarkdown` option completely. Importing and using components in `.md` files will no longer work.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-11)

Remove this legacy flag. It is no longer available in Astro.

astro.config.mjs

```diff
export default defineConfig({
-  legacy: {
-    astroFlavoredMarkdown: true,
-  },
})
```

If you were using this feature in v1.x, we recommend [using the MDX integration](/en/guides/integrations-guide/mdx/) which allows you to combine components and JSX expressions with Markdown syntax.

### Removed: `Astro.resolve()`

[Section titled “Removed: Astro.resolve()”](#removed-astroresolve)

In v0.24, Astro deprecated `Astro.resolve()` for getting resolved URLs to assets that you might want to reference in the browser.

Astro v2.0 removes this option entirely. `Astro.resolve()` in your code will cause an error.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-12)

Resolve asset paths using `import` instead. For example:

src/pages/index.astro

```astro
---
import 'style.css';
import imageUrl from './image.png';
---


<img src={imageUrl} />
```

### Removed: `Astro.fetchContent()`

[Section titled “Removed: Astro.fetchContent()”](#removed-astrofetchcontent)

In v0.26, Astro deprecated `Astro.fetchContent()` for fetching data from your local Markdown files.

Astro v2.0 removes this option entirely. `Astro.fetchContent()` in your code will cause an error.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-13)

Use `Astro.glob()` to fetch Markdown files, or convert to the [Content Collections](/en/guides/content-collections/) feature.

src/pages/index.astro

```astro
---
const allPosts = await Astro.glob('./posts/*.md');
---
```

### Removed: `Astro.canonicalURL`

[Section titled “Removed: Astro.canonicalURL”](#removed-astrocanonicalurl)

In v1.0, Astro deprecated `Astro.canonicalURL` for constructing a canonical URL.

Astro v2.0 removes this option entirely. `Astro.canonicalURL` in your code will cause an error.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-14)

Use `Astro.url` to construct a canonical URL.

src/pages/index.astro

```astro
---
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
---
```

### Updated: Vite 4

[Section titled “Updated: Vite 4”](#updated-vite-4)

Astro v2.0 upgrades from Vite 3 to [Vite 4](https://vite.dev/), released in December 2022.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-15)

There should be no changes to your code necessary! We’ve handled most of the upgrade for you inside of Astro; however, some subtle Vite behaviors may still change between versions.

Refer to the official [Vite Migration Guide](https://vite.dev/guide/migration.html) if you run into trouble.

## Astro v2.0 Experimental Flags Removed

[Section titled “Astro v2.0 Experimental Flags Removed”](#astro-v20-experimental-flags-removed)

Remove the following experimental flags from `astro.config.mjs`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
-  experimental: {
-    contentCollections: true,
-    prerender: true,
-    errorOverlay: true,
-  },
})
```

These features are now available by default:

* [Content collections](/en/guides/content-collections/) as a way to manage your Markdown and MDX files with type-safety.
* [Prerendering individual pages to static HTML](/en/guides/on-demand-rendering/) when using SSR to improve speed and cacheability.
* A redesigned error message overlay.

## Known Issues

[Section titled “Known Issues”](#known-issues)

There are currently no known issues.

# Upgrade to Astro v3

> How to upgrade your project to the latest version of Astro (v3.0).

This guide will help you migrate from Astro v2 to Astro v3.

Need to upgrade an older project to v2? See our [older migration guide](/en/guides/upgrade-to/v2/).

## Upgrade Astro

[Section titled “Upgrade Astro”](#upgrade-astro)

Update your project’s version of Astro to the latest version using your package manager. If you’re using Astro integrations, please also update those to the latest version.

* npm

  ```shell
  # Upgrade to Astro v3.x
  npm install astro@latest


  # Example: upgrade React and Tailwind integrations
  npm install @astrojs/react@latest @astrojs/tailwind@latest
  ```

* pnpm

  ```shell
  # Upgrade to Astro v3.x
  pnpm add astro@latest


  # Example: upgrade React and Tailwind integrations
  pnpm add @astrojs/react@latest @astrojs/tailwind@latest
  ```

* Yarn

  ```shell
  # Upgrade to Astro v3.x
  yarn add astro@latest


  # Example: upgrade React and Tailwind integrations
  yarn add @astrojs/react@latest @astrojs/tailwind@latest
  ```

Need to continue?

After upgrading Astro to the latest version, you may not need to make any changes to your project at all!

But, if you notice errors or unexpected behavior, please check below for what has changed that might need updating in your project.

## Astro v3.0 Experimental Flags Removed

[Section titled “Astro v3.0 Experimental Flags Removed”](#astro-v30-experimental-flags-removed)

Remove the following experimental flags from `astro.config.mjs`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
-  experimental: {
-    assets: true,
-    viewTransitions: true,
-  },
})
```

These features are now available by default:

* View Transitions for animated page transitions and persistent islands. See [view transitions API breaking changes and upgrading advice](#upgrade-view-transitions-to-v3) if you were using this experimental flag.
* A new image services API `astro:assets` for using images in Astro, including a new `<Image />` component and `getImage()` function. Please read the detailed [image upgrade advice](#upgrade-images-to-v3) **whether or not you were using this experimental flag** to see how this might affect your project.

Read more about these two exciting features and more in [the 3.0 Blog post](https://astro.build/blog/astro-3/)!

## Astro v3.0 Breaking Changes

[Section titled “Astro v3.0 Breaking Changes”](#astro-v30-breaking-changes)

Astro v3.0 includes some breaking changes, as well as the removal of some previously deprecated features. If your project doesn’t work as expected after upgrading to v3.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See [the changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for full release notes.

### Removed: Support for Node 16

[Section titled “Removed: Support for Node 16”](#removed-support-for-node-16)

Node 16 is scheduled to reach its End of Life in September 2023.

Astro v3.0 drops Node 16 support entirely so that all Astro users can take advantage of Node’s more modern features.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do)

Check that both your development environment and your deployment environment are using **Node `18.14.1` or higher**.

1. Check your local version of Node using:

   ```sh
   node -v
   ```

2. Check your [deployment environment’s](/en/guides/deploy/) own documentation to verify that they support Node 18.

   You can specify Node `18.14.1` for your Astro project either in a dashboard configuration setting or a `.nvmrc` file.

   .nvmrc

   ```bash
   18.14.1
   ```

### Removed: Support for TypeScript 4

[Section titled “Removed: Support for TypeScript 4”](#removed-support-for-typescript-4)

In Astro v2.x, the `tsconfig.json` presets include support for both TypeScript 4.x and 5.x.

Astro v3.0 updates the `tsconfig.json` presets to only support TypeScript 5.x. Astro now assumes that you use TypeScript 5.0 (March 2023), or that your editor includes it (e.g. VS Code 1.77).

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-1)

If you have installed TypeScript locally, update to at least v5.0.

```bash
npm install typescript@latest --save-dev
```

### Removed: `@astrojs/image`

[Section titled “Removed: @astrojs/image”](#removed-astrojsimage)

In Astro v2.x, Astro offered an official image integration that included Astro `<Image />` and `<Picture />` components.

Astro v3.0 removes this integration from the codebase entirely. Astro’s new solution for images is a built-in image services API: `astro:assets`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-2)

Remove the `@astrojs/image` integration from your project. You will need to not only uninstall the integration but also update or remove any import statements and existing `<Image />` and `<Picture />` components. You might also need to configure a preferred default image processing service.

You will find [complete, step-by-step instructions for removing the old image integration](#remove-astrojsimage) in our Images guide.

Migrating to `astro:assets` will also bring some new image options and features that you may now wish to use. Please see the full [v3.0 Image Upgrade Advice](#upgrade-images-to-v3) for full details!

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
-import image from '@astrojs/image';


export default defineConfig({
  integrations: [
    -image(),
  ]
})
```

### Removed: `<Markdown />` component

[Section titled “Removed: \<Markdown /> component”](#removed-markdown--component)

In Astro v1.x, Astro deprecated the `<Markdown />` component and moved it to an external package.

Astro v3.0 completely removes the package `@astrojs/markdown-component`. Astro’s `<Markdown />` component will no longer work in your project.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-3)

Remove all instances of the `@astrojs/markdown-component`.

src/components/MyAstroComponent.astro

```diff
---
-import Markdown from '@astrojs/markdown-component';
---
```

To continue using a similar `<Markdown />` component in your code, consider using [community integrations](https://astro.build/integrations/) such as [`astro-remote`](https://github.com/natemoo-re/astro-remote). Be sure to update your `<Markdown />` component imports and attributes as necessary, according to the integration’s own documentation.

Otherwise, delete all references to importing Astro’s `<Markdown />` component and the component itself in your `.astro` files. You will need to rewrite your content as HTML directly or [import Markdown](/en/guides/markdown-content/#importing-markdown) from a `.md` file.

### Removed: deprecated 1.x APIs

[Section titled “Removed: deprecated 1.x APIs”](#removed-deprecated-1x-apis)

In Astro v1.x, Astro deprecated our original configuration settings as well as `<style global>` and `<script hoist>` support. However, these were still supported for backwards compatibility.

Astro v3.0 removes these deprecated APIs entirely. The officially supported [configuration settings](/en/reference/configuration-reference/) and modern `<style is:global>` and `<script>` syntax should be used instead.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-4)

If you are continuing to use v1.x APIs, use the new APIs for each feature instead:

* Deprecated config options: See [the 0.26 migration guide](/en/guides/upgrade-to/v1/#new-configuration-api)
* Deprecated script/style attribute types: See [the 0.26 migration guide](/en/guides/upgrade-to/v1/#new-default-script-behavior)

### Removed: Partial shims for Web APIs in server code

[Section titled “Removed: Partial shims for Web APIs in server code”](#removed-partial-shims-for-web-apis-in-server-code)

In Astro v2.x, Astro provided partial shims for Web APIs such as `document` or `localStorage` in server-rendered code. These shims were often incomplete and unreliable.

Astro v3.0 removes these partial shims entirely. Web APIs are no longer available in server-rendered code.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-5)

If you are using Web APIs in server-rendered components, you will need to either make the usage of those APIs conditional or use [the `client:only` client directive](/en/reference/directives-reference/#clientonly).

### Removed: `image` from `astro:content` in content collections schema

[Section titled “Removed: image from astro:content in content collections schema”](#removed-image-from-astrocontent-in-content-collections-schema)

In Astro v2.x, the content collections API deprecated an `image` export from `astro:content` for use in your content collections schemas.

Astro v3.0 removes this export entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-6)

If you are using the deprecated `image()` from `astro:content`, remove it as this no longer exists. Validate images through [the `image` helper from `schema`](#update-content-collections-schemas) instead:

src/content/config.ts

```diff
-import { defineCollection, z, image } from "astro:content";
+import { defineCollection, z } from "astro:content";


defineCollection({
  schema: ({ image }) =>
    z.object({
      image: image(),
   }),
});
```

### Removed: pre-0.14 Shiki theme names

[Section titled “Removed: pre-0.14 Shiki theme names”](#removed-pre-014-shiki-theme-names)

In Astro v2.x, some Shiki theme names had been renamed, but the original names were kept for backwards compatibility.

Astro v3.0 removes the original names in favor of the renamed theme names.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-7)

If your project uses any of the themes below, rename them to their updated name:

* `material-darker` -> `material-theme-darker`
* `material-default` -> `material-theme`
* `material-lighter` -> `material-theme-lighter`
* `material-ocean` -> `material-theme-ocean`
* `material-palenight` -> `material-theme-palenight`

### Removed: `class:list` features

[Section titled “Removed: class:list features”](#removed-classlist-features)

In Astro v2.x, the [`class:list` directive](/en/reference/directives-reference/#classlist) used a custom implementation inspired by [`clsx`](https://github.com/lukeed/clsx) with a few extra features like deduplication and `Set` support.

Astro v3.0 now uses `clsx` directly for `class:list`, which does not support deduplication or `Set` values.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-8)

Replace any `Set` elements passed to the `class:list` directive with a plain `Array`.

src/components/MyAstroComponent.astro

```diff
<Component class:list={[
  'a',
  'b',
  -new Set(['c', 'd'])
+  ['c', 'd']
]} />
```

### Removed: passing `class:list` as a prop

[Section titled “Removed: passing class:list as a prop”](#removed-passing-classlist-as-a-prop)

In Astro v2.x, [`class:list` values](/en/reference/directives-reference/#classlist) were sent to components via [`Astro.props['class:list']`](/en/reference/api-reference/#props).

Astro v3.0 normalizes `class:list` values into a string before being sent to components via `Astro.props['class']`

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-9)

Remove any code that expects to receive the `class:list` prop.

src/components/MyAstroComponent.astro

```diff
---
-import { clsx } from 'clsx';
-const { class: className, 'class:list': classList } = Astro.props;
+const { class: className } = Astro.props;
---
<div
  -class:list={[className, classList]}
  +class:list={[className]}
/>
```

### Removed: kebab-case transform for camelCase CSS variables

[Section titled “Removed: kebab-case transform for camelCase CSS variables”](#removed-kebab-case-transform-for-camelcase-css-variables)

In Astro v2.x, camelCase [CSS variables](/en/guides/styling/#css-variables) passed to the `style` attribute were rendered as both camelCase (as written) and kebab-case (kept for backwards compatibility).

Astro v3.0 removes the kebab-case transform for these camelCase CSS variable names, and only the original camelCase CSS variable is rendered.

src/components/MyAstroComponent.astro

```astro
---
const myValue = "red"
---
<!-- input -->
<div style={{ "--myValue": myValue }}></div>


<!-- output (Astro 2.x) -->
<div style="--my-value:var(--myValue);--myValue:red"></div>
<!-- output (Astro 3.0) -->
<div style="--myValue:red"></div>
```

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-10)

If you were relying on Astro to transform kebab-case in your styles, update your existing styles to camelCase to prevent missing styles. For example:

src/components/MyAstroComponent.astro

```diff
<style>
  div {
   -color: var(--my-value);
   +color: var(--myValue);
  }
</style>
```

### Removed: automatic flattening of `getStaticPaths()`’s return value

[Section titled “Removed: automatic flattening of getStaticPaths()’s return value”](#removed-automatic-flattening-of-getstaticpathss-return-value)

In Astro v2.x, the return value of [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) was automatically flattened to allow you to return an array of arrays without errors.

Astro v3.0 removes automatic flattening of `getStaticPaths()`’s result.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-11)

If you’re returning an array of arrays instead of an array of *objects* (as is expected), `.flatMap` and `.flat` should now be used to ensure that you are returning a flat array.

An [error message indicating that `getStaticPath()`’s return value must be an array of objects](/en/reference/errors/invalid-get-static-paths-entry/#what-went-wrong) will be provided if you need to update your code.

### Moved: `astro check` now requires an external package

[Section titled “Moved: astro check now requires an external package”](#moved-astro-check-now-requires-an-external-package)

In Astro v2.x, [`astro check`](/en/reference/cli-reference/#astro-check) was included in Astro by default, and its dependencies were bundled in Astro. This meant a larger package whether or not you ever used `astro check`. This also prevented you from having control over the version of TypeScript and the Astro Language Server to use.

Astro v3.0 moves the `astro check` command out of Astro core and now requires an external package `@astrojs/check`. Additionally, you must install `typescript` in your project to use the `astro check` command.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-12)

Run the `astro check` command after upgrading to Astro v3.0 and follow the prompts to install the required dependencies, or manually install `@astrojs/check` and `typescript` into your project.

### Deprecated: `build.excludeMiddleware` and `build.split`

[Section titled “Deprecated: build.excludeMiddleware and build.split”](#deprecated-buildexcludemiddleware-and-buildsplit)

In Astro v2.x, `build.excludeMiddleware` and `build.split` were used to change how specific files were emitted when using an adapter in SSR mode.

Astro v3.0 replaces these build config options with new [SSR adapter configuration options](/en/guides/integrations-guide/#official-integrations) to perform the same tasks: `edgeMiddleware` and `functionPerRoute`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-13)

Update the Astro config file to now use the new options **in the adapter configuration** directly.

astro.config.mjs

```diff
import { defineConfig } from "astro/config";
import vercel from "@astrojs/vercel/serverless";


export default defineConfig({
-    build: {
-      excludeMiddleware: true
-    },
    adapter: vercel({
+      edgeMiddleware: true
    }),
});
```

astro.config.mjs

```diff
import { defineConfig } from "astro/config";
import netlify from "@astrojs/netlify/functions";


export default defineConfig({
-     build: {
-        split: true
-     },
     adapter: netlify({
+        functionPerRoute: true
     }),
});
```

### Deprecated: `markdown.drafts`

[Section titled “Deprecated: markdown.drafts”](#deprecated-markdowndrafts)

In Astro v2.x, the `markdown.drafts` configuration allowed you to have draft pages that were available in when running the dev server, but not built in production.

Astro v3.0 deprecates this feature in favor of the content collections method of handling draft pages by filtering manually instead, which gives more control over the feature.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-14)

To continue to mark some pages in your project as drafts, [migrate to content collections](/en/guides/content-collections/) and manually filter out pages with the `draft: true` frontmatter property instead.

### Deprecated: returning simple object in endpoints

[Section titled “Deprecated: returning simple object in endpoints”](#deprecated-returning-simple-object-in-endpoints)

In Astro v2.x, endpoints could return a simple object, which would be converted to a JSON response.

Astro v3.0 deprecates this behavior in favor of returning a `Response` object directly.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-15)

Update your endpoints to return a `Response` object directly.

endpoint.json.ts

```diff
export async function GET() {
  -return { body: { "title": "Bob's blog" }};
  +return new Response(JSON.stringify({ "title": "Bob's blog" }));
}
```

If you really need to keep the previous format, you can use the `ResponseWithEncoding` object but will be deprecated in the future.

endpoint.json.ts

```diff
export async function GET() {
  -return { body: { "title": "Bob's blog" } };
  +return new ResponseWithEncoding({ body: { "title": "Bob's blog" }});
}
```

### Changed default: `verbatimModuleSyntax` in tsconfig.json presets

[Section titled “Changed default: verbatimModuleSyntax in tsconfig.json presets”](#changed-default-verbatimmodulesyntax-in-tsconfigjson-presets)

In Astro v2.x, the [`verbatimModuleSyntax`](https://www.typescriptlang.org/tsconfig#verbatimModuleSyntax) setting was off by default, with its TypeScript 4.x equivalent `importsNotUsedAsValues` being enabled in the `strict` preset.

In Astro v3.0, `verbatimModuleSyntax` is enabled in every preset.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-16)

This option requires that types are imported using the `import type` syntax.

src/components/MyAstroComponent.astro

```astro
---
import { type CollectionEntry, getEntry } from "astro:content";
---
```

While we recommend keeping it on and properly making your type imports with `type` (as shown above), you can disable it by setting `verbatimModuleSyntax: false` in your `tsconfig.json` file if it causes any issues.

tsconfig.json

```json
{
  "compilerOptions": {
    "verbatimModuleSyntax": false
  }
}
```

### Changed default: port `3000`

[Section titled “Changed default: port 3000”](#changed-default-port-3000)

In Astro v2.x, Astro ran on port `3000` by default.

Astro v3.0 changes the [default port](/en/reference/cli-reference/#--port-number) to `4321`. 🚀

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-17)

Update any existing references to `localhost:3000`, for example in tests or in your `README`, to reflect the new port `localhost:4321`.

### Changed default: import.meta.env.BASE\_URL `trailingSlash`

[Section titled “Changed default: import.meta.env.BASE\_URL trailingSlash”](#changed-default-importmetaenvbase_url-trailingslash)

In Astro v2.x, `import.meta.env.BASE_URL` appended your [`base`](/en/reference/configuration-reference/#base) setting with a [trailingSlash](/en/reference/configuration-reference/#trailingslash) by default. `trailingSlash: "ignore"` also appended a trailing slash.

Astro v3.0 no longer appends `import.meta.env.BASE_URL` with a trailing slash by default, nor when `trailingSlash: "ignore"` is set. (The existing behavior of `base` in combination with `trailingSlash: "always"` or `trailingSlash: "never"` is unchanged.)

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-18)

If your `base` already has a trailing slash, no change is needed.

If your `base` does not have a trailing slash, add one if you wish to preserve the previous default (or `trailingSlash: "ignore"`) behavior:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
-  base: 'my-base',
+  base: 'my-base/',
});
```

### Changed default: `compressHTML`

[Section titled “Changed default: compressHTML”](#changed-default-compresshtml)

In Astro v2.x, Astro only compressed your emitted HTML when [`compressHTML`](/en/reference/configuration-reference/#compresshtml) was explicitly set to `true`. The default value was `false`.

Astro v3.0 now compresses emitted HTML by default.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-19)

You can now remove `compressHTML: true` from your configuration as this is the new default behavior.

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
-  compressHTML: true
})
```

You must now set `compressHTML: false` to opt out of HTML compression.

### Changed default: `scopedStyleStrategy`

[Section titled “Changed default: scopedStyleStrategy”](#changed-default-scopedstylestrategy)

In Astro v2.x, the default value of [`scopedStyleStrategy`](/en/reference/configuration-reference/#scopedstylestrategy) was `"where"`.

Astro v3.0 introduces a new, default value: `"attribute"`. By default, styles are now applied using `data-*` attributes.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-20)

To retain your project’s current [style scoping](/en/guides/styling/#scoped-styles), update the configuration file to the previous default value:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
+  scopedStyleStrategy: "where"
})
```

### Changed default: `inlineStyleSheets`

[Section titled “Changed default: inlineStyleSheets”](#changed-default-inlinestylesheets)

In Astro v2.x, all project stylesheets were sent as link tags by default. You could opt in to inlining them into `<style>` tags every time with `"always"`, or to inlining only stylesheets below a certain size with `"auto"` by setting the [`build.inlineStylesheets`](/en/reference/configuration-reference/#buildinlinestylesheets) configuration. The default setting was `"never"`.

Astro v3.0 changes the default value of `inlineStylesheets` to `"auto"`. Stylesheets smaller than `ViteConfig.build.assetsInlineLimit` (default: 4kb) are inlined by default. Otherwise, project styles are sent in external stylesheets.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-21)

If you want to keep your project’s current behavior, set `build.inlineStylesheets` to the previous default, `"never"`:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
+   build: {
+    inlineStylesheets: "never"
+  }
})
```

### Changed default: image service

[Section titled “Changed default: image service”](#changed-default-image-service)

In Astro v2.x, Squoosh was the [default image processing service](/en/guides/images/#default-image-service).

Astro v3.0 now includes Sharp as the default image processing service and instead provides a configuration option to use Squoosh.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-22)

Note

When using a [strict package manager](https://pnpm.io/pnpm-vs-npm#npms-flat-tree) like `pnpm`, you may need to manually install Sharp into your project even though it is an Astro dependency:

```bash
pnpm add sharp
```

If you would prefer to continue to use Squoosh to transform your images, update your config with the following:

astro.config.mjs

```diff
import { defineConfig, squooshImageService } from "astro/config";


export default defineConfig({
+  image: {
+    service: squooshImageService(),
+  }
})
```

### Changed: HTTP request methods case

[Section titled “Changed: HTTP request methods case”](#changed-http-request-methods-case)

In Astro v2.x, [HTTP request methods](/en/guides/endpoints/#http-methods) were written using lowercase function names: `get`, `post`, `put`, `all`, and `del`.

Astro v3.0 uses uppercase function names, including `DELETE` instead of `del`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-23)

Rename all functions to their uppercase equivalent:

* `get` to `GET`
* `post` to `POST`
* `put` to `PUT`
* `all` to `ALL`
* `del` to `DELETE`

endpoint.ts

```diff
-export function get() {
+export function GET() {
    return new Response(JSON.stringify({ "title": "Bob's blog" }));
}
```

### Changed: Multiple JSX framework configuration

[Section titled “Changed: Multiple JSX framework configuration”](#changed-multiple-jsx-framework-configuration)

In Astro v2.x, you could use [multiple JSX framework integrations](/en/guides/integrations-guide/#official-integrations) (React, Solid, Preact) in the same project without needing to identify which files belonged to which framework.

Astro v3.0 now requires you to specify which framework to use for your files with new `include` and `exclude` integration config options when you have multiple JSX framework integrations installed. This allows Astro to better support single-framework usage, as well as advanced features like React Fast Refresh.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-24)

If you are using multiple JSX frameworks in the same project, set `include` (and optionally `exclude`) to an array of files and/or folders. Wildcards may be used to include multiple file paths.

We recommend placing common framework components in the same folder (e.g. `/components/react/` and `/components/solid/`) to make specifying your includes easier, but this is not required:

```diff
import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';
import react from '@astrojs/react';
import svelte from '@astrojs/svelte';
import vue from '@astrojs/vue';
import solid from '@astrojs/solid-js';


export default defineConfig({
  // Enable many frameworks to support all different kinds of components.
  // No `include` is needed if you are only using a single framework!
  integrations: [
    preact({
+      include: ['**/preact/*']
    }),
    react({
+      include: ['**/react/*']
    }),
    solid({
+      include: ['**/solid/*'],
    }),
  ]
});
```

### Changed: `Astro.cookies.get(key)` can return `undefined`

[Section titled “Changed: Astro.cookies.get(key) can return undefined”](#changed-astrocookiesgetkey-can-return-undefined)

In Astro v2.x, `Astro.cookies.get(key)` would always return an `AstroCookie` object, even if the cookie did not exist. To check for its existence, you needed to use `Astro.cookies.has(key)`.

Astro v3.0 returns `undefined` for `Astro.cookies.get(key)` if the cookie does not exist.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-25)

This change will not break any code that checks for the existence of the `Astro.cookie` object before using `Astro.cookies.get(key)`, but is now no longer required.

You can safely remove any code that uses `has()` to check if the value of `Astro.cookies` is `undefined`:

```diff
-if (Astro.cookies.has(id)) {
  -const id = Astro.cookies.get(id)!;
-}


+const id = Astro.cookies.get(id);
+if (id) {
+}
```

### Changed: running the Astro CLI programmatically

[Section titled “Changed: running the Astro CLI programmatically”](#changed-running-the-astro-cli-programmatically)

In Astro v2.x, the `"astro"` package entrypoint exported and ran the Astro CLI directly. It is not recommended to run Astro this way in practice.

Astro v3.0 removes the CLI from the entrypoint, and exports a new set of experimental JavaScript APIs, including `dev()`, `build()`, `preview()`, and `sync()`.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-26)

To [run the Astro CLI programmatically](/en/reference/programmatic-reference/), use the new experimental JavaScript APIs:

```js
import { dev, build } from "astro";


// Start the Astro dev server
const devServer = await dev();
await devServer.stop();


// Build your Astro project
await build();
```

### Changed: internal Astro API entry point export paths

[Section titled “Changed: internal Astro API entry point export paths”](#changed-internal-astro-api-entry-point-export-paths)

In Astro v2.x, you could import internal Astro APIs from `astro/internal/*` and `astro/runtime/server/*`.

Astro v3.0 removes the two entry points in favor of the existing `astro/runtime/*` entrypoint. Additionally, a new `astro/compiler-runtime` export has been added for compiler-specific runtime code.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-27)

These are entry points for Astro’s internal API and should not affect your project. But if you do use these entrypoints, update as shown below:

```diff
-import 'astro/internal/index.js';
+import 'astro/runtime/server/index.js';


-import 'astro/server/index.js';
+import 'astro/runtime/server/index.js';
```

```diff
import { transform } from '@astrojs/compiler';


const result = await transform(source, {
  internalURL: 'astro/runtime/server/index.js',
  internalURL: 'astro/compiler-runtime',
  // ...
});
```

## Feature Upgrades

[Section titled “Feature Upgrades”](#feature-upgrades)

### Upgrade images to v3

[Section titled “Upgrade images to v3”](#upgrade-images-to-v3)

`astro:assets` is no longer behind an experimental flag in Astro v3.0.

`<Image />` is now a built-in component and the previous `@astrojs/image` integration has been removed.

These and other accompanying changes to using images in Astro may cause some breaking changes when you upgrade your Astro project from an earlier version.

Please follow the instructions below as appropriate to upgrade an Astro v2.x project to v3.0.

#### Upgrade from `experimental.assets`

[Section titled “Upgrade from experimental.assets”](#upgrade-from-experimentalassets)

If you had previously enabled the experimental flag for `astro:assets`, you will need to update your project for Astro v3.0 which now includes assets features by default.

##### Remove `experimental.assets` flag

[Section titled “Remove experimental.assets flag”](#remove-experimentalassets-flag)

Remove the experimental flag:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
-  experimental: {
-    assets: true
-  }
});
```

If necessary, also update your `src/env.d.ts` file to replace the `astro/client-image` reference with `astro/client`:

src/env.d.ts

```diff
-/// <reference types="astro/client-image" />
+/// <reference types="astro/client" />
```

##### Remove the `~/assets` import alias

[Section titled “Remove the \~/assets import alias”](#remove-the-assets-import-alias)

This import alias is no longer included by default with `astro:assets`. If you were using this alias with experimental assets, you must convert them to relative file paths, or [create your own import aliases](/en/guides/imports/#aliases).

src/pages/posts/post-1.astro

```diff
---
-import rocket from '~/assets/rocket.png';
+import rocket from '../../assets/rocket.png';
---
```

##### Add simple asset support for Cloudflare, Deno, Vercel Edge and Netlify Edge

[Section titled “Add simple asset support for Cloudflare, Deno, Vercel Edge and Netlify Edge”](#add-simple-asset-support-for-cloudflare-deno-vercel-edge-and-netlify-edge)

Astro v3.0 allows `astro:assets` to work without errors in Cloudflare, Deno, Vercel Edge and Netlify Edge, which do not support Astro’s built-in Squoosh and Sharp image optimization. Note that Astro does not perform any image transformation and processing in these environments. However, you can still enjoy the other benefits of using `astro:assets`, including no Cumulative Layout Shift (CLS), the enforced `alt` attribute, and a consistent authoring experience.

If you previously avoided using `astro:assets` because of these constraints, you can now use them without issues. You can configure the no-op image service to explicitly opt-in to this behavior:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  image: {
+    service: {
+      entrypoint: 'astro/assets/services/noop'
+    }
+  }
});
```

#### Decide where to store your images

[Section titled “Decide where to store your images”](#decide-where-to-store-your-images)

See the Images guide to help you decide [where to store your images](/en/guides/images/#where-to-store-images). You may wish to take advantage of new options for storing your images with the added flexibility `astro:assets` brings. For example, relative images from your project `src/` can now be referenced in Markdown, MDX, and Markdoc using standard Markdown `![alt](src)` syntax.

#### Update existing `<img>` tags

[Section titled “Update existing \<img> tags”](#update-existing-img-tags)

Previously, importing an image would return a simple `string` with the path of the image. Now, imported image assets match the following signature:

```ts
interface ImageMetadata {
  src: string;
  width: number;
  height: number;
  format: string;
}
```

You must update the `src` attribute of any existing `<img>` tags (including any [images in UI framework components](/en/guides/images/#images-in-ui-framework-components)) and you may also update other attributes that are now available to you from the imported image.

src/components/MyComponent.astro

```diff
---
import rocket from '../images/rocket.svg';
---
<img src={rocket} width="250" height="250" alt="A rocketship in space." />


<img src={rocket.src} width={rocket.width} height={rocket.height} alt="A rocketship in space." />
```

#### Update your Markdown, MDX, and Markdoc files

[Section titled “Update your Markdown, MDX, and Markdoc files”](#update-your-markdown-mdx-and-markdoc-files)

Relative images from your project `src/` can now be referenced in Markdown, MDX, and Markdoc using standard Markdown `![alt](src)` syntax.

This allows you to move your images from the `public/` directory to your project `src/` where they will now be processed and optimized. Your existing images in `public/` and remote images are still valid but are not optimized by Astro’s build process.

src/pages/posts/post-1.md

```md
# My Markdown Page


<!-- Local images now possible! -->
![A starry night sky.](../../images/stars.png)


<!-- Keep your images next to your content! -->
![A starry night sky.](./stars.png)
```

If you require more control over your image attributes, we recommend using the `.mdx` file format, which allows you to include Astro’s `<Image />` component or a JSX `<img />` tag in addition to the Markdown syntax. Use the [MDX integration](/en/guides/integrations-guide/mdx/) to add support for MDX to Astro.

#### Remove `@astrojs/image`

[Section titled “Remove @astrojs/image”](#remove-astrojsimage)

If you were using the image integration in Astro v2.x, complete the following steps:

1. Remove the `@astrojs/image` integration.

   You must [remove the integration](/en/guides/integrations-guide/#removing-an-integration) by uninstalling and then removing it from your `astro.config.mjs` file.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   -import image from '@astrojs/image';


   export default defineConfig({
     integrations: [
       -image(),
     ]
   })
   ```

2. Update types (if required).

   If you had special types configured for `@astrojs/image` in `src/env.d.ts`, you may need to change them back to the default Astro types if your upgrade to v3 did not complete this step for you.

   src/env.d.ts

   ```diff
    -/// <reference types="@astrojs/image/client" />
    +/// <reference types="astro/client" />
   ```

   Similarly, update `tsconfig.json` if necessary:

   tsconfig.json

   ```diff
   {
     "compilerOptions": {
       -"types": ["@astrojs/image/client"]
       +"types": ["astro/client"]
     }
   }
   ```

3. Migrate any existing `<Image />` components.

   Change all `import` statements from `@astrojs/image/components` to `astro:assets` in order to use the new built-in `<Image />` component.

   Remove any component attributes that are not [currently supported image asset properties](/en/reference/modules/astro-assets/#image-properties).

   For example, `aspectRatio` is no longer supported, as it is now automatically inferred from the `width` and `height` attributes.

   src/components/MyComponent.astro

   ```diff
   ---
   -import { Image } from '@astrojs/image/components';
   +import { Image } from 'astro:assets';
   import localImage from '../assets/logo.png';
   const localAlt = 'The Astro Logo';
   ---


   <Image
     src={localImage}
     width={300}
     -aspectRatio="16:9"
     alt={localAlt}
   />
   ```

4. Choose a default image service.

   [Sharp](https://github.com/lovell/sharp) is now the default image service used for `astro:assets`. If you would like to use Sharp, no configuration is required.

   If you would prefer to use [Squoosh](https://github.com/GoogleChromeLabs/squoosh) to transform your images, update your config with the following `image.service` option:

   astro.config.mjs

   ```diff
   import { defineConfig, squooshImageService } from 'astro/config';


   export default defineConfig({
   +  image: {
   +    service: squooshImageService(),
   +  },
   });
   ```

#### Update Content Collections schemas

[Section titled “Update Content Collections schemas”](#update-content-collections-schemas)

You can now declare an associated image for a content collections entry, such as a blog post’s cover image, in your frontmatter using its path relative to the current folder.

The new `image` helper for content collections lets you validate the image metadata using Zod. Learn more about [how to use images in content collections](/en/guides/images/#images-in-content-collections)

#### Navigating Image Imports in Astro v3.0

[Section titled “Navigating Image Imports in Astro v3.0”](#navigating-image-imports-in-astro-v30)

In Astro v3.0, if you have to preserve the old import behavior for images and require a string representation of the image’s URL, append `?url` to the end of your image path when importing it. For example:

src/pages/blog/MyImages.astro

```astro
---
import Sprite from '../assets/logo.svg?url';
---


<svg>
  <use xlink:href={Sprite + '#cart'} />
</svg>
```

This approach ensures you obtain the URL string. Keep in mind that during development, Astro uses a `src/` path, but upon building, it generates hashed paths like `/_astro/cat.a6737dd3.png`.

If you prefer to work directly with the image object itself, you can access the `.src` property. This approach is best for tasks like managing image dimensions for Core Web Vitals metrics and preventing CLS.

If you are transitioning into the new import behavior, combining `?url` and `.src` methods might be the right method for seamless image handling.

### Upgrade view transitions to v3

[Section titled “Upgrade view transitions to v3”](#upgrade-view-transitions-to-v3)

View transitions are no longer behind an experimental flag in Astro v3.0.

If you had **not** enabled this experimental flag in Astro 2.x, this will not cause any breaking changes to your project. The new View Transitions API has no effect on your existing code.

If you were previously using experimental view transitions, there may be some breaking changes when you upgrade your Astro project from an earlier version.

Please follow the instructions below as appropriate to upgrade **an Astro v2.x project configured with `experimental.viewTransitions: true`** to v3.0.

#### Upgrade from `experimental.viewTransitions`

[Section titled “Upgrade from experimental.viewTransitions”](#upgrade-from-experimentalviewtransitions)

If you had previously enabled the experimental flag for view transitions, you will need to update your project for Astro v3.0 which now allows view transitions by default.

##### Remove `experimental.viewTransitions` flag

[Section titled “Remove experimental.viewTransitions flag”](#remove-experimentalviewtransitions-flag)

Remove the experimental flag:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
-  experimental: {
-   viewTransitions: true
-  }
});
```

##### Update import source

[Section titled “Update import source”](#update-import-source)

The `<ViewTransitions />` component has been moved from `astro:components` to `astro:transitions`. Update the import source across all occurrences in your project.

src/layouts/BaseLayout.astro

```astro
---
import { ViewTransitions } from "astro:components astro:transitions"
---
<html lang="en">
  <head>
    <title>My Homepage</title>
    <ViewTransitions />
  </head>
  <body>
    <h1>Welcome to my website!</h1>
  </body>
</html>
```

#### Update `transition:animate` directives

[Section titled “Update transition:animate directives”](#update-transitionanimate-directives)

**Changed:** The `transition:animate` value `morph` has been renamed to `initial`. Also, this is no longer the default animation. If no `transition:animate` directive is specified, your animations will now default to `fade`.

1. Rename any `morph` animations to `initial`.

   src/components/MyComponent.astro

   ```astro
   <div transition:name="name" transition:animate="morph initial" />
   ```

2. To keep any animations that were previously using `morph` by default, explicitly add `transition:animate="initial"`

   src/components/MyComponent.astro

   ```astro
   <div transition:name="name" transition:animate="initial" />
   ```

3. You can safely remove any animations explicitly set to `fade`. This is now the default behavior:

   src/components/MyComponent.astro

   ```astro
   <div transition:name="name" transition:animate="fade" />
   ```

**Added:** Astro also supports a new `transition:animate` value, `none`. This value can be used on a page’s `<html>` element to disable animated full-page transitions on an entire page. This will only override **default animation behavior** on page elements without an animation directive. You can still set animations on individual elements, and these specific animations will occur.

4. You may now disable all default transitions on an individual page, animating only elements that explicitly use a `transition:animate` directive:

   ```astro
   <html transition:animate="none">
     <head></head>
     <body>
       <h1>Hello world!</h1>
     </body>
   </html>
   ```

##### Update event names

[Section titled “Update event names”](#update-event-names)

The event `astro:load` has been renamed to `astro:page-load`. Rename all occurrences in your project.

src/components/MyComponent.astro

```astro
<script>
document.addEventListener('astro:load astro:page-load', runSetupLogic);
</script>
```

The event `astro:beforeload` has been renamed to `astro:after-swap`. Rename all occurrences in your project.

src/components/MyComponent.astro

```astro
<script>
document.addEventListener('astro:beforeload astro:after-swap', setDarkMode);
</script>
```

## Community Resources

[Section titled “Community Resources”](#community-resources)

Know a good resource for Astro v3.0? [Edit this page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/upgrade-to/v3.mdx) and add a link below!

## Known Issues

[Section titled “Known Issues”](#known-issues)

There are currently no known issues.

# Upgrade to Astro v4

> How to upgrade your project to the latest version of Astro (v4.0).

This guide will help you migrate from Astro v3 to Astro v4.

Need to upgrade an older project to v3? See our [older migration guide](/en/guides/upgrade-to/v3/).

Need to see the v3 docs? Visit this [older version of the docs site (unmaintained v3.6 snapshot)](https://docs-git-v3-docs-unmaintained-astrodotbuild.vercel.app/).

## Upgrade Astro

[Section titled “Upgrade Astro”](#upgrade-astro)

Update your project’s version of Astro and all official integrations to the latest versions using your package manager.

* npm

  ```shell
  # Upgrade Astro and official integrations together
  npx @astrojs/upgrade
  ```

* pnpm

  ```shell
  # Upgrade Astro and official integrations together
  pnpm dlx @astrojs/upgrade
  ```

* Yarn

  ```shell
  # Upgrade Astro and official integrations together
  yarn dlx @astrojs/upgrade
  ```

You can also [upgrade your Astro integrations manually](/en/guides/integrations-guide/#manual-upgrading) if needed, and you may also need to upgrade other dependencies in your project.

Need to continue?

After upgrading Astro to the latest version, you may not need to make any changes to your project at all!

But, if you notice errors or unexpected behavior, please check below for what has changed that might need updating in your project.

Astro v4.0 includes [potentially breaking changes](#breaking-changes), as well as the [removal of some previously deprecated features](#previously-deprecated-features-now-removed).

If your project doesn’t work as expected after upgrading to v4.0, check this guide for an overview of all breaking changes and instructions on how to update your codebase.

See [the changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) for full release notes.

## Astro v4.0 Experimental Flags Removed

[Section titled “Astro v4.0 Experimental Flags Removed”](#astro-v40-experimental-flags-removed)

Remove the `devOverlay` experimental flag and move any `i18n` config to the top level in `astro.config.mjs`:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
-    devOverlay: true,
-    i18n: {
-      locales: ["en", "fr", "pt-br", "es"],
-      defaultLocale: "en",
-    }
  },
+  i18n: {
+    locales: ["en", "fr", "pt-br", "es"],
+    defaultLocale: "en",
+  },
})
```

These configurations, `i18n` and the renamed `devToolbar`, are now available in Astro v4.0.

Read more about these two exciting features and more in [the v4.0 Blog post](https://astro.build/blog/astro-4/)!

## Upgrades

[Section titled “Upgrades”](#upgrades)

Any major upgrades to Astro’s dependencies may cause breaking changes in your project.

### Upgraded: Vite 5.0

[Section titled “Upgraded: Vite 5.0”](#upgraded-vite-50)

In Astro v3.0, Vite 4 was used as the development server and production bundler.

Astro v4.0 upgrades from Vite 4 to Vite 5.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do)

If you are using Vite-specific plugins, configuration, or APIs, check the [Vite migration guide](https://vite.dev/guide/migration) for their breaking changes and upgrade your project as needed. There are no breaking changes to Astro itself.

### Upgraded: unified, remark, and rehype dependencies

[Section titled “Upgraded: unified, remark, and rehype dependencies”](#upgraded-unified-remark-and-rehype-dependencies)

In Astro v3.x, unified v10 and its related compatible remark/rehype packages were used to process Markdown and MDX.

Astro v4.0 upgrades [unified to v11](https://github.com/unifiedjs/unified/releases/tag/11.0.0) and the other remark/rehype packages to the latest version.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-1)

If you used custom remark/rehype packages, update all of them to the latest version using your package manager to ensure they support unified v11. The packages you are using can be found in `astro.config.mjs`.

There should not be any significant breaking changes if you use actively updated packages, but some packages may not yet be compatible with unified v11. Visually inspect your Markdown/MDX pages before deploying to ensure your site is functioning as intended.

## Breaking Changes

[Section titled “Breaking Changes”](#breaking-changes)

The following changes are considered breaking changes in Astro. Breaking changes may or may not provide temporary backwards compatibility, and all documentation is updated to refer to only the current, supported code.

If you need to refer to the documentation for a v3.x project, you can browse this [(unmaintained) snapshot of the docs from before v4.0 was released](https://docs-git-v3-docs-unmaintained-astrodotbuild.vercel.app/).

### Renamed: `entrypoint` (Integrations API)

[Section titled “Renamed: entrypoint (Integrations API)”](#renamed-entrypoint-integrations-api)

In Astro v3.x, the property of the `injectRoute` integrations API that specified the route entry point was named `entryPoint`.

Astro v4.0 renames this property to `entrypoint` to be consistent with other Astro APIs. The `entryPoint` property is deprecated but will continue to work and logs a warning prompting you to update your code.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-2)

If you have integrations that use the `injectRoute` API, rename the `entryPoint` property to `entrypoint`. If you’re a library author who wants to support both Astro 3 and 4, you can specify both `entryPoint` and `entrypoint`, in which case, a warning will not be logged.

```diff
injectRoute({
  pattern: '/fancy-dashboard',
-  entryPoint: '@fancy/dashboard/dashboard.astro'
+  entrypoint: '@fancy/dashboard/dashboard.astro'
});
```

### Changed: `app.render` signature in Integrations API

[Section titled “Changed: app.render signature in Integrations API”](#changed-apprender-signature-in-integrations-api)

In Astro v3.0, the `app.render()` method accepted `routeData` and `locals` as separate, optional arguments.

Astro v4.0 changes the `app.render()` signature. These two properties are now available in a single object. Both the object and these two properties are still optional.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-3)

If you are maintaining an adapter, the current signature will continue to work until the next major version. To migrate to the new signature, pass `routeData` and `locals` as properties of an object instead of as multiple independent arguments.

```diff
-app.render(request, routeData, locals)
+app.render(request, { routeData, locals })
```

### Changed: adapters must now specify supported features

[Section titled “Changed: adapters must now specify supported features”](#changed-adapters-must-now-specify-supported-features)

In Astro v3.x, adapters were not required to specify the features they support.

Astro v4.0 requires adapters to pass the `supportedAstroFeatures{}` property to specify a list of features they support. This property is no longer optional.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-4)

Adapter authors need to pass the `supportedAstroFeatures{}` option to specify a list of features they support.

my-adapter.mjs

```diff
export default function createIntegration() {
  return {
    name: '@matthewp/my-adapter',
    hooks: {
      'astro:config:done': ({ setAdapter }) => {
        setAdapter({
          name: '@matthewp/my-adapter',
          serverEntrypoint: '@matthewp/my-adapter/server.js',
+          supportedAstroFeatures: {
+              staticOutput: 'stable'
+          }
        });
      },
    },
  };
}
```

### Removed: Shiki language `path` property

[Section titled “Removed: Shiki language path property”](#removed-shiki-language-path-property)

In Astro v3.x, a Shiki language passed to `markdown.shikiConfig.langs` was automatically converted to a Shikiji-compatible language. Shikiji is the internal tooling used by Astro for syntax highlighting.

Astro v4.0 removes support for the `path` property of a Shiki language, which was confusing to configure. It is replaced by an import which can be passed to `langs` directly.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-5)

The language JSON file should be imported and passed to the option instead.

astro.config.js

```diff
 +import customLang from './custom.tmLanguage.json'


export default defineConfig({
  markdown: {
    shikiConfig: {
      langs: [
-       { path: '../../custom.tmLanguage.json' },
+       customLang,
      ],
    },
  },
})
```

## Deprecated

[Section titled “Deprecated”](#deprecated)

The following deprecated features are no longer supported and are no longer documented. Please update your project accordingly.

Some deprecated features may temporarily continue to function until they are completely removed. Others may silently have no effect, or throw an error prompting you to update your code.

### Deprecated: `handleForms` for View Transitions `submit` events

[Section titled “Deprecated: handleForms for View Transitions submit events”](#deprecated-handleforms-for-view-transitions-submit-events)

In Astro v3.x, projects using the `<ViewTransitions />` component were required to opt-in to handling `submit` events for `form` elements. This was done by passing a `handleForms` prop.

Astro v4.0 handles `submit` events for `form` elements by default when `<ViewTransitions />` are used. The `handleForms` prop has been deprecated and no longer has any effect.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-6)

Remove the `handleForms` property from your `ViewTransitions` component. It is no longer necessary.

src/pages/index.astro

```astro
---
import { ViewTransitions } from "astro:transitions";
---
<html>
  <head>
    <ViewTransitions handleForms />
  </head>
  <body>
    <!-- stuff here -->
  </body>
</html>
```

To opt out of `submit` event handling, add the `data-astro-reload` attribute to relevant `form` elements.

src/components/Form.astro

```astro
<form action="/contact" data-astro-reload>
  <!-- -->
</form>
```

## Previously deprecated features now removed

[Section titled “Previously deprecated features now removed”](#previously-deprecated-features-now-removed)

The following deprecated features have now been entirely removed from the code base and can no longer be used. Some of these features may have continued to work in your project even after deprecation. Others may have silently had no effect.

Projects now containing these removed features will be unable to build, and there will no longer be any supporting documentation prompting you to remove these features.

### Removed: returning simple objects from endpoints

[Section titled “Removed: returning simple objects from endpoints”](#removed-returning-simple-objects-from-endpoints)

In Astro v3.x, returning simple objects from endpoints was deprecated, but was still supported to maintain compatibility with Astro v2. A `ResponseWithEncoding` utility was also provided to ease the migration.

Astro v4.0 removes support for simple objects and requires endpoints to always return a `Response`. The `ResponseWithEncoding` utility is also removed in favor of a proper `Response` type.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-7)

Update your endpoints to return a `Response` object directly.

```diff
export async function GET() {
  -return { body: { "title": "Bob's blog" }};
  +return new Response(JSON.stringify({ "title": "Bob's blog" }));
}
```

To remove usage of `ResponseWithEncoding`, refactor your code to use an `ArrayBuffer` instead:

```diff
export async function GET() {
  const file = await fs.readFile('./bob.png');
  -return new ResponseWithEncoding(file.toString('binary'), undefined, 'binary');
  +return new Response(file.buffer);
}
```

### Removed: `build.split` and `build.excludeMiddleware`

[Section titled “Removed: build.split and build.excludeMiddleware”](#removed-buildsplit-and-buildexcludemiddleware)

In Astro v3.0, `build.split` and `build.excludeMiddleware` build config options were deprecated and replaced with [adapter configuration options](/en/reference/adapter-reference/#adapter-features) to perform the same tasks.

Astro v4.0 removes these properties entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-8)

If you are using the deprecated `build.split` or `build.excludeMiddleware`, you must now remove them as these no longer exist.

Please see the v3 migration guide to [update these deprecated middleware properties](/en/guides/upgrade-to/v3/#deprecated-buildexcludemiddleware-and-buildsplit) with adapter configurations.

### Removed: `Astro.request.params`

[Section titled “Removed: Astro.request.params”](#removed-astrorequestparams)

In Astro v3.0, the `Astro.request.params` API was deprecated, but preserved for backwards compatibility.

Astro v4.0 removes this option entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-9)

Update all occurrences to [`Astro.params`](/en/reference/api-reference/#params), which is the supported replacement.

```diff
-const { id } = Astro.request.params;
+const { id } = Astro.params;
```

### Removed: `markdown.drafts`

[Section titled “Removed: markdown.drafts”](#removed-markdowndrafts)

In Astro v3.0, using `markdown.drafts` to control the building of draft posts was deprecated.

Astro v4.0 removes this option entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-10)

If you are using the deprecated `markdown.drafts`, you must now remove it as it no longer exists.

To continue to mark some pages in your project as drafts, [migrate to content collections](/en/guides/content-collections/) and manually filter out pages with the `draft: true` frontmatter property instead.

### Removed: `getHeaders()`

[Section titled “Removed: getHeaders()”](#removed-getheaders)

In Astro v3.0, the `getHeaders()` Markdown export was deprecated and replaced with `getHeadings()`.

Astro v4.0 removes this option entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-11)

If you are using the deprecated `getHeaders()`, you must now remove it as it no longer exists. Replace any instances with `getHeadings()`, which is the supported replacement.

```diff
const posts = await Astro.glob('../content/blog/*.mdx');
-const firstPostHeadings = posts.at(0).getHeaders();
+const firstPostHeadings = posts.at(0).getHeadings();
```

### Removed: using `rss` in `getStaticPaths()`

[Section titled “Removed: using rss in getStaticPaths()”](#removed-using-rss-in-getstaticpaths)

In Astro v3.0, using the deprecated `rss` helper in `getStaticPaths()` would throw an error.

Astro v4.0 removes this helper entirely.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-12)

If you are using the unsupported method for generating RSS feeds, you must now use the [`@astrojs/rss` integration](/en/recipes/rss/) for a complete RSS setup.

### Removed: lowercase HTTP method names

[Section titled “Removed: lowercase HTTP method names”](#removed-lowercase-http-method-names)

In Astro v3.0, using lowercase HTTP request method names (`get`, `post`, `put`, `all`, `del`) was deprecated.

Astro v4.0 removes support for lowercase names entirely. All HTTP request methods must now be written using uppercase.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-13)

If you are using the deprecated lowercase names, you must now replace them with their uppercase equivalents.

Please see the v3 migration guide [for guidance using uppercase HTTP request methods](/en/guides/upgrade-to/v3/#changed-http-request-methods-case).

### Removed: 301 redirects when missing a `base` prefix

[Section titled “Removed: 301 redirects when missing a base prefix”](#removed-301-redirects-when-missing-a-base-prefix)

In Astro v3.x, the Astro preview server returned a 301 redirect when accessing public directory assets without a base path.

Astro v4.0 returns a 404 status without a base path prefix for public directory assets when the preview server is running, matching the behavior of the dev server.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-14)

When using the Astro preview server, all of your static asset imports and URLs from the public directory must have [the base value](/en/reference/configuration-reference/#base) prefixed to the path.

The following example shows the `src` attribute required to display an image from the public folder when `base: '/docs'` is configured:

src/pages/index.astro

```astro
// To access public/images/my-image.png:


<img src="/docs/images/my-image.png" alt="">
```

### Removed: `astro/client-image` auto-conversion

[Section titled “Removed: astro/client-image auto-conversion”](#removed-astroclient-image-auto-conversion)

In Astro v3.x, the `astro/client-image` type (used for the deprecated image integration) was removed but was auto-converted to the default Astro type `astro/client` if found in your `env.d.ts` file.

Astro v4.0 ignores `astro/client-image` and will no longer update `env.d.ts` for you automatically.

#### What should I do?

[Section titled “What should I do?”](#what-should-i-do-15)

If you had types configured for `@astrojs/image` in `src/env.d.ts` and upgrading to v3.0 did not automatically convert the type for you, replace the `astro/client-image` type manually with `astro/client`.

src/env.d.ts

```diff
  -/// <reference types="astro/client-image" />
  +/// <reference types="astro/client" />
```

## Community Resources

[Section titled “Community Resources”](#community-resources)

Know a good resource for Astro v4.0? [Edit this page](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/upgrade-to/v4.mdx) and add a link below!

## Known Issues

[Section titled “Known Issues”](#known-issues)

Please check [Astro’s issues on GitHub](https://github.com/withastro/astro/issues/) for any reported issues, or to file an issue yourself.


---

**Navigation:** [← Previous](./08-migrating-from-nextjs.md) | [Index](./index.md) | [Next →](./10-upgrade-to-astro-v5.md)
