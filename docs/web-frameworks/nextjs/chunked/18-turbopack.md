**Navigation:** [← Previous](./17-images.md) | [Index](./index.md) | Next →

---

# Turbopack

@router: Pages Router

Turbopack is an **incremental bundler** optimized for JavaScript and TypeScript, written in Rust, and built into **Next.js**. You can use Turbopack with both the Pages and App Router for a **much faster** local development experience.

## Why Turbopack?

We built Turbopack to push the performance of Next.js, including:

* **Unified Graph:** Next.js supports multiple output environments (e.g., client and server). Managing multiple compilers and stitching bundles together can be tedious. Turbopack uses a **single, unified graph** for all environments.
* **Bundling vs Native ESM:** Some tools skip bundling in development and rely on the browser's native ESM. This works well for small apps but can slow down large apps due to excessive network requests. Turbopack **bundles** in dev, but in an optimized way to keep large apps fast.
* **Incremental Computation:** Turbopack parallelizes work across cores and **caches** results down to the function level. Once a piece of work is done, Turbopack won’t repeat it.
* **Lazy Bundling:** Turbopack only bundles what is actually requested by the dev server. This lazy approach can reduce initial compile times and memory usage.

## Getting started

Turbopack is now the **default bundler** in Next.js. No configuration is needed to use Turbopack:

```json filename="package.json" highlight={3}
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  }
}
```

### Using Webpack instead

If you need to use Webpack instead of Turbopack, you can opt-in with the `--webpack` flag:

```json filename="package.json"
{
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack",
    "start": "next start"
  }
}
```

## Supported features

Turbopack in Next.js has **zero-configuration** for the common use cases. Below is a summary of what is supported out of the box, plus some references to how you can configure Turbopack further when needed.

### Language features

| Feature                     | Status        | Notes                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JavaScript & TypeScript** | **Supported** | Uses SWC under the hood. Type-checking is not done by Turbopack (run `tsc --watch` or rely on your IDE for type checks).                                                                                                                                                                                                                                                                                                |
| **ECMAScript (ESNext)**     | **Supported** | Turbopack supports the latest ECMAScript features, matching SWC’s coverage.                                                                                                                                                                                                                                                                                                                                             |
| **CommonJS**                | **Supported** | `require()` syntax is handled out of the box.                                                                                                                                                                                                                                                                                                                                                                           |
| **ESM**                     | **Supported** | Static and dynamic `import` are fully supported.                                                                                                                                                                                                                                                                                                                                                                        |
| **Babel**                   | **Supported** | Starting in Next.js 16, Turbopack uses Babel automatically if it detects [a configuration file][babel-config]. Unlike in webpack, SWC is always used for Next.js's internal transforms and downleveling to older ECMAScript revisions. Next.js with webpack disables SWC if a Babel configuration file is present. Files in `node_modules` are excluded, unless you [manually configure `babel-loader`][manual-loader]. |

[babel-config]: https://babeljs.io/docs/config-files

[manual-loader]: /docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders

### Framework and React features

| Feature                           | Status        | Notes                                                                                                                  |
| --------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **JSX / TSX**                     | **Supported** | SWC handles JSX/TSX compilation.                                                                                       |
| **Fast Refresh**                  | **Supported** | No configuration needed.                                                                                               |
| **React Server Components (RSC)** | **Supported** | For the Next.js App Router. Turbopack ensures correct server/client bundling.                                          |
| **Root layout creation**          | Unsupported   | Automatic creation of a root layout in App Router is not supported. Turbopack will instruct you to create it manually. |

### CSS and styling

| Feature            | Status                  | Notes                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Global CSS**     | **Supported**           | Import `.css` files directly in your application.                                                                                                                                                                                                                                                                                                                     |
| **CSS Modules**    | **Supported**           | `.module.css` files work natively (Lightning CSS).                                                                                                                                                                                                                                                                                                                    |
| **CSS Nesting**    | **Supported**           | Lightning CSS supports [modern CSS nesting](https://lightningcss.dev/).                                                                                                                                                                                                                                                                                               |
| **@import syntax** | **Supported**           | Combine multiple CSS files.                                                                                                                                                                                                                                                                                                                                           |
| **PostCSS**        | **Supported**           | Automatically processes `postcss.config.js` in a Node.js worker pool. Useful for Tailwind, Autoprefixer, etc.                                                                                                                                                                                                                                                         |
| **Sass / SCSS**    | **Supported** (Next.js) | For Next.js, Sass is supported out of the box. Custom Sass functions (`sassOptions.functions`) are not supported because Turbopack's Rust-based architecture cannot directly execute JavaScript functions, unlike webpack's Node.js environment. Use webpack if you need this feature. In the future, Turbopack standalone usage will likely require a loader config. |
| **Less**           | Planned via plugins     | Not yet supported by default. Will likely require a loader config once custom loaders are stable.                                                                                                                                                                                                                                                                     |
| **Lightning CSS**  | **In Use**              | Handles CSS transformations. Some low-usage CSS Modules features (like `:local/:global` as standalone pseudo-classes) are not yet supported. [See below for more details.](#unsupported-and-unplanned-features)                                                                                                                                                       |

### Assets

| Feature                           | Status        | Notes                                                                                                                      |
| --------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Static Assets** (images, fonts) | **Supported** | Importing `import img from './img.png'` works out of the box. In Next.js, returns an object for the `<Image />` component. |
| **JSON Imports**                  | **Supported** | Named or default imports from `.json` are supported.                                                                       |

### Module resolution

| Feature               | Status              | Notes                                                                                                                                                           |
| --------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path Aliases**      | **Supported**       | Reads `tsconfig.json`'s `paths` and `baseUrl`, matching Next.js behavior.                                                                                       |
| **Manual Aliases**    | **Supported**       | [Configure `resolveAlias` in `next.config.js`](/docs/app/api-reference/config/next-config-js/turbopack.md#resolving-aliases) (similar to `webpack.resolve.alias`). |
| **Custom Extensions** | **Supported**       | [Configure `resolveExtensions` in `next.config.js`](/docs/app/api-reference/config/next-config-js/turbopack.md#resolving-custom-extensions).                       |
| **AMD**               | Partially Supported | Basic transforms work; advanced AMD usage is limited.                                                                                                           |

### Performance and Fast Refresh

| Feature                  | Status        | Notes                                                                                    |
| ------------------------ | ------------- | ---------------------------------------------------------------------------------------- |
| **Fast Refresh**         | **Supported** | Updates JavaScript, TypeScript, and CSS without a full refresh.                          |
| **Incremental Bundling** | **Supported** | Turbopack lazily builds only what’s requested by the dev server, speeding up large apps. |

## Known gaps with webpack

There are a number of non-trivial behavior differences between webpack and Turbopack that are important to be aware of when migrating an application. Generally, these are less of a concern for new applications.

### CSS Module Ordering

Turbopack will follow JS import order to order [CSS modules](/docs/app/getting-started/css.md#css-modules) which are not otherwise ordered. For example:

```jsx filename="components/BlogPost.jsx"
import utilStyles from './utils.module.css'
import buttonStyles from './button.module.css'
export default function BlogPost() {
  return (
    <div className={utilStyles.container}>
      <button className={buttonStyles.primary}>Click me</button>
    </div>
  )
}
```

In this example, Turbopack will ensure that `utils.module.css` will appear before `button.module.css` in the produced CSS chunk, following the import order

Webpack generally does this as well, but there are cases where it will ignore JS inferred ordering, for example if it infers the JS file is side-effect-free.

This can lead to subtle rendering changes when adopting Turbopack, if applications have come to rely on an arbitrary ordering. Generally, the solution is easy, e.g. have `button.module.css` `@import utils.module.css` to force the ordering, or identify the conflicting rules and change them to not target the same properties.

### Sass node\_modules imports

Turbopack supports importing `node_modules` Sass files out of the box. Webpack supports a legacy tilde `~` syntax for this, which is not supported by Turbopack.

From:

```scss filename="styles/globals.scss"
@import '~bootstrap/dist/css/bootstrap.min.css';
```

To:

```scss filename="styles/globals.scss"
@import 'bootstrap/dist/css/bootstrap.min.css';
```

If you can't update the imports, you can add a `turbopack.resolveAlias` configuration to map the `~` syntax to the actual path:

```js filename="next.config.js"
module.exports = {
  turbopack: {
    resolveAlias: {
      '~*': '*',
    },
  },
}
```

### Bundle Sizes

From our testing on production applications, we observed that Turbopack generally produces bundles that are similar in size to Webpack. However, the comparison can be difficult since turbopack tends to produce fewer but larger chunks. Our advice is to focus on higher level metrics like [Core Web Vitals](https://web.dev/articles/vitals) or your own application level metrics to compare performance across the two bundlers. We are however aware of one gap that can occasionally cause a large regression.

Turbopack does not yet have an equivalent to the [Inner Graph Optimization](https://webpack.js.org/configuration/optimization/#optimizationinnergraph) in webpack which is enabled by default. This optimization is useful to tree shake large modules. For example:

```js filename=large.module.js
import heavy from 'some-heavy-dependency.js'

export function usesHeavy() {
  return heavy.run()
}

export const CONSTANT_VALUE = 3
```

If an application only uses `CONSTANT_VALUE` Turbopack will detect this and delete the `usesHeavy` export but not the corresponding `import`. However, with the Inner Graph Optimization, webpack can delete the `import` too which can drop the dependency as well.

We are planning to offer an equivalent to the Inner Graph Optimization in Turbopack but it is still under development. If you are affected by this gap, consider manually splitting modules.

### Build Caching

Webpack supports [disk build caching](https://webpack.js.org/configuration/cache/#cache) to improve build performance. Turbopack provides a similar opt-in feature, currently in beta. Starting with Next 16, you can enable Turbopack’s filesystem cache by setting the following experimental flags:

* [`experimental.turbopackFileSystemCacheForDev`](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache.md)
* [`experimental.turbopackFileSystemCacheForBuild`](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache.md)

> **Good to know:** For this reason, when comparing webpack and Turbopack performance, make sure to delete the `.next` folder between builds to see a fair comparison or enable the turbopack filesystem cache feature.

### Webpack plugins

Turbopack does not support webpack plugins. This affects third-party tools that rely on webpack's plugin system for integration. We do support [webpack loaders](/docs/app/api-reference/config/next-config-js/turbopack.md#configuring-webpack-loaders). If you depend on webpack plugins, you'll need to find Turbopack-compatible alternatives or continue using webpack until equivalent functionality is available.

## Unsupported and unplanned features

Some features are not yet implemented or not planned:

* **Legacy CSS Modules features**
  * Standalone `:local` and `:global` pseudo-classes (only the function variant `:global(...)` is supported).
  * The `@value` rule (superseded by CSS variables).
  * `:import` and `:export` ICSS rules.
  * `composes` in `.module.css` composing a `.css` file. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `composes` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
  * `@import` in CSS Modules importing `.css` as a CSS Module. In webpack this would treat the `.css` file as a CSS Module, with Turbopack the `.css` file will always be global. This means that if you want to use `@import` in a CSS Module, you need to change the `.css` file to a `.module.css` file.
* **`sassOptions.functions`**
  Custom Sass functions defined in `sassOptions.functions` are not supported. This feature allows defining JavaScript functions that can be called from Sass code during compilation. Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through `sassOptions.functions`, unlike webpack's Node.js-based sass-loader which runs entirely in JavaScript. If you're using custom Sass functions, you'll need to use webpack instead of Turbopack.
* **`webpack()` configuration** in `next.config.js`
  Turbopack replaces webpack, so `webpack()` configs are not recognized. Use the [`turbopack` config](/docs/app/api-reference/config/next-config-js/turbopack.md) instead.
* **Yarn PnP**
  Not planned for Turbopack support in Next.js.
* **`experimental.urlImports`**
  Not planned for Turbopack.
* **`experimental.esmExternals`**
  Not planned. Turbopack does not support the legacy `esmExternals` configuration in Next.js.
* **Some Next.js Experimental Flags**
  * `experimental.nextScriptWorkers`
  * `experimental.sri.algorithm`
  * `experimental.fallbackNodePolyfills`
    We plan to implement these in the future.

For a full, detailed breakdown of each feature flag and its status, see the [Turbopack API Reference](/docs/app/api-reference/config/next-config-js/turbopack.md).

## Configuration

Turbopack can be configured via `next.config.js` (or `next.config.ts`) under the `turbopack` key. Configuration options include:

* **`rules`**
  Define additional [webpack loaders](/docs/app/api-reference/config/next-config-js/turbopack.md#configuring-webpack-loaders) for file transformations.
* **`resolveAlias`**
  Create manual aliases (like `resolve.alias` in webpack).
* **`resolveExtensions`**
  Change or extend file extensions for module resolution.

```js filename="next.config.js"
module.exports = {
  turbopack: {
    // Example: adding an alias and custom file extension
    resolveAlias: {
      underscore: 'lodash',
    },
    resolveExtensions: ['.mdx', '.tsx', '.ts', '.jsx', '.js', '.json'],
  },
}
```

For more in-depth configuration examples, see the [Turbopack config documentation](/docs/app/api-reference/config/next-config-js/turbopack.md).

## Generating trace files for performance debugging

If you encounter performance or memory issues and want to help the Next.js team diagnose them, you can generate a trace file by appending `NEXT_TURBOPACK_TRACING=1` to your dev command:

```bash
NEXT_TURBOPACK_TRACING=1 next dev
```

This will produce a `.next/dev/trace-turbopack` file. Include that file when creating a GitHub issue on the [Next.js repo](https://github.com/vercel/next.js) to help us investigate.

By default the development server outputs to `.next/dev`. Read more about [isolatedDevBuild](/docs/app/api-reference/config/next-config-js/isolatedDevBuild.md).

## Summary

Turbopack is a **Rust-based**, **incremental** bundler designed to make local development and builds fast—especially for large applications. It is integrated into Next.js, offering zero-config CSS, React, and TypeScript support.

## Version Changes

| Version   | Changes                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| `v16.0.0` | Turbopack becomes the default bundler for Next.js. Automatic support for Babel when a configuration file is found. |
| `v15.5.0` | Turbopack support for `build` beta                                                                                 |
| `v15.3.0` | Experimental support for `build`                                                                                   |
| `v15.0.0` | Turbopack for `dev` stable                                                                                         |



--------------------------------------------------------------------------------
title: "Architecture"
description: "How Next.js Works"
source: "https://nextjs.org/docs/architecture"
--------------------------------------------------------------------------------

# Architecture

Learn about the Next.js architecture and how it works under the hood.

 - [Accessibility](/docs/architecture/accessibility.md)
 - [Fast Refresh](/docs/architecture/fast-refresh.md)
 - [Next.js Compiler](/docs/architecture/nextjs-compiler.md)
 - [Supported Browsers](/docs/architecture/supported-browsers.md)

--------------------------------------------------------------------------------
title: "Accessibility"
description: "The built-in accessibility features of Next.js."
source: "https://nextjs.org/docs/architecture/accessibility"
--------------------------------------------------------------------------------

# Accessibility

The Next.js team is committed to making Next.js accessible to all developers (and their end-users). By adding accessibility features to Next.js by default, we aim to make the Web more inclusive for everyone.

## Route Announcements

When transitioning between pages rendered on the server (e.g. using the `<a href>` tag) screen readers and other assistive technology announce the page title when the page loads so that users understand that the page has changed.

In addition to traditional page navigations, Next.js also supports client-side transitions for improved performance (using `next/link`). To ensure that client-side transitions are also announced to assistive technology, Next.js includes a route announcer by default.

The Next.js route announcer looks for the page name to announce by first inspecting `document.title`, then the `<h1>` element, and finally the URL pathname. For the most accessible user experience, ensure that each page in your application has a unique and descriptive title.

## Linting

Next.js provides an [integrated ESLint experience](/docs/pages/api-reference/config/eslint.md) out of the box, including custom rules for Next.js. By default, Next.js includes `eslint-plugin-jsx-a11y` to help catch accessibility issues early, including warning on:

* [aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
* [aria-proptypes](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-proptypes.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
* [aria-unsupported-elements](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/aria-unsupported-elements.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
* [role-has-required-aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/role-has-required-aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)
* [role-supports-aria-props](https://github.com/jsx-eslint/eslint-plugin-jsx-a11y/blob/HEAD/docs/rules/role-supports-aria-props.md?rgh-link-date=2021-06-04T02%3A10%3A36Z)

For example, this plugin helps ensure you add alt text to `img` tags, use correct `aria-*` attributes, use correct `role` attributes, and more.

## Accessibility Resources

* [WebAIM WCAG checklist](https://webaim.org/standards/wcag/checklist)
* [WCAG 2.2 Guidelines](https://www.w3.org/TR/WCAG22/)
* [The A11y Project](https://www.a11yproject.com/)
* Check [color contrast ratios](https://developer.mozilla.org/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast) between foreground and background elements
* Use [`prefers-reduced-motion`](https://web.dev/prefers-reduced-motion/) when working with animations


--------------------------------------------------------------------------------
title: "Fast Refresh"
description: "Fast Refresh is a hot module reloading experience that gives you instantaneous feedback on edits made to your React components."
source: "https://nextjs.org/docs/architecture/fast-refresh"
--------------------------------------------------------------------------------

# Fast Refresh

Fast refresh is a React feature integrated into Next.js that allows you to live reload the browser page while maintaining temporary client-side state when you save changes to a file. It's enabled by default in all Next.js applications on **9.4 or newer**. With Fast Refresh enabled, most edits should be visible within a second.

## How It Works

* If you edit a file that **only exports React component(s)**, Fast Refresh will
  update the code only for that file, and re-render your component. You can edit
  anything in that file, including styles, rendering logic, event handlers, or
  effects.
* If you edit a file with exports that *aren't* React components, Fast Refresh
  will re-run both that file, and the other files importing it. So if both
  `Button.js` and `Modal.js` import `theme.js`, editing `theme.js` will update
  both components.
* Finally, if you **edit a file** that's **imported by files outside of the
  React tree**, Fast Refresh **will fall back to doing a full reload**. You
  might have a file which renders a React component but also exports a value
  that is imported by a **non-React component**. For example, maybe your
  component also exports a constant, and a non-React utility file imports it. In
  that case, consider migrating the constant to a separate file and importing it
  into both files. This will re-enable Fast Refresh to work. Other cases can
  usually be solved in a similar way.

## Error Resilience

### Syntax Errors

If you make a syntax error during development, you can fix it and save the file
again. The error will disappear automatically, so you won't need to reload the
app. **You will not lose component state**.

### Runtime Errors

If you make a mistake that leads to a runtime error inside your component,
you'll be greeted with a contextual overlay. Fixing the error will automatically
dismiss the overlay, without reloading the app.

Component state will be retained if the error did not occur during rendering. If
the error did occur during rendering, React will remount your application using
the updated code.

If you have [error boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary)
in your app (which is a good idea for graceful failures in production), they
will retry rendering on the next edit after a rendering error. This means having
an error boundary can prevent you from always getting reset to the root app
state. However, keep in mind that error boundaries shouldn't be *too* granular.
They are used by React in production, and should always be designed
intentionally.

## Limitations

Fast Refresh tries to preserve local React state in the component you're
editing, but only if it's safe to do so. Here's a few reasons why you might see
local state being reset on every edit to a file:

* Local state is not preserved for class components (only function components
  and Hooks preserve state).
* The file you're editing might have *other* exports in addition to a React
  component.
* Sometimes, a file would export the result of calling a higher-order component
  like `HOC(WrappedComponent)`. If the returned component is a
  class, its state will be reset.
* Anonymous arrow functions like `export default () => <div />;` cause Fast Refresh to not preserve local component state. For large codebases you can use our [`name-default-component` codemod](/docs/pages/guides/upgrading/codemods.md#name-default-component).

As more of your codebase moves to function components and Hooks, you can expect
state to be preserved in more cases.

## Tips

* Fast Refresh preserves React local state in function components (and Hooks) by
  default.
* Sometimes you might want to *force* the state to be reset, and a component to
  be remounted. For example, this can be handy if you're tweaking an animation
  that only happens on mount. To do this, you can add `// @refresh reset`
  anywhere in the file you're editing. This directive is local to the file, and
  instructs Fast Refresh to remount components defined in that file on every
  edit.
* You can put `console.log` or `debugger;` into the components you edit during
  development.
* Remember that imports are case sensitive. Both fast and full refresh can fail,
  when your import doesn't match the actual filename.
  For example, `'./header'` vs `'./Header'`.

## Fast Refresh and Hooks

When possible, Fast Refresh attempts to preserve the state of your component
between edits. In particular, `useState` and `useRef` preserve their previous
values as long as you don't change their arguments or the order of the Hook
calls.

Hooks with dependencies—such as `useEffect`, `useMemo`, and `useCallback`—will
*always* update during Fast Refresh. Their list of dependencies will be ignored
while Fast Refresh is happening.

For example, when you edit `useMemo(() => x * 2, [x])` to
`useMemo(() => x * 10, [x])`, it will re-run even though `x` (the dependency)
has not changed. If React didn't do that, your edit wouldn't reflect on the
screen!

Sometimes, this can lead to unexpected results. For example, even a `useEffect`
with an empty array of dependencies would still re-run once during Fast Refresh.

However, writing code resilient to occasional re-running of `useEffect` is a good practice even
without Fast Refresh. It will make it easier for you to introduce new dependencies to it later on
and it's enforced by [React Strict Mode](/docs/pages/api-reference/config/next-config-js/reactStrictMode.md),
which we highly recommend enabling.


--------------------------------------------------------------------------------
title: "Next.js Compiler"
description: "Next.js Compiler, written in Rust, which transforms and minifies your Next.js application."
source: "https://nextjs.org/docs/architecture/nextjs-compiler"
--------------------------------------------------------------------------------

# Next.js Compiler

The Next.js Compiler, written in Rust using [SWC](https://swc.rs/), allows Next.js to transform and minify your JavaScript code for production. This replaces Babel for individual files and Terser for minifying output bundles.

Compilation using the Next.js Compiler is 17x faster than Babel and enabled by default since Next.js version 12. If you have an existing Babel configuration or are using [unsupported features](#unsupported-features), your application will opt-out of the Next.js Compiler and continue using Babel.

## Why SWC?

[SWC](https://swc.rs/) is an extensible Rust-based platform for the next generation of fast developer tools.

SWC can be used for compilation, minification, bundling, and more – and is designed to be extended. It's something you can call to perform code transformations (either built-in or custom). Running those transformations happens through higher-level tools like Next.js.

We chose to build on SWC for a few reasons:

* **Extensibility:** SWC can be used as a Crate inside Next.js, without having to fork the library or workaround design constraints.
* **Performance:** We were able to achieve ~3x faster Fast Refresh and ~5x faster builds in Next.js by switching to SWC, with more room for optimization still in progress.
* **WebAssembly:** Rust's support for WASM is essential for supporting all possible platforms and taking Next.js development everywhere.
* **Community:** The Rust community and ecosystem are amazing and still growing.

## Supported Features

### Styled Components

We're working to port `babel-plugin-styled-components` to the Next.js Compiler.

First, update to the latest version of Next.js: `npm install next@latest`. Then, update your `next.config.js` file:

```js filename="next.config.js"
module.exports = {
  compiler: {
    styledComponents: true,
  },
}
```

For advanced use cases, you can configure individual properties for styled-components compilation.

> Note: `ssr` and `displayName` transforms are the main requirement for using `styled-components` in Next.js.

```js filename="next.config.js"
module.exports = {
  compiler: {
    // see https://styled-components.com/docs/tooling#babel-plugin for more info on the options.
    styledComponents: {
      // Enabled by default in development, disabled in production to reduce file size,
      // setting this will override the default for all environments.
      displayName?: boolean,
      // Enabled by default.
      ssr?: boolean,
      // Enabled by default.
      fileName?: boolean,
      // Empty by default.
      topLevelImportPaths?: string[],
      // Defaults to ["index"].
      meaninglessFileNames?: string[],
      // Enabled by default.
      minify?: boolean,
      // Enabled by default.
      transpileTemplateLiterals?: boolean,
      // Empty by default.
      namespace?: string,
      // Disabled by default.
      pure?: boolean,
      // Enabled by default.
      cssProp?: boolean,
    },
  },
}
```

### Jest

The Next.js Compiler transpiles your tests and simplifies configuring Jest together with Next.js including:

* Auto mocking of `.css`, `.module.css` (and their `.scss` variants), and image imports
* Automatically sets up `transform` using SWC
* Loading `.env` (and all variants) into `process.env`
* Ignores `node_modules` from test resolving and transforms
* Ignoring `.next` from test resolving
* Loads `next.config.js` for flags that enable experimental SWC transforms

First, update to the latest version of Next.js: `npm install next@latest`. Then, update your `jest.config.js` file:

```js filename="jest.config.js"
const nextJest = require('next/jest')

// Providing the path to your Next.js app which will enable loading next.config.js and .env files
const createJestConfig = nextJest({ dir: './' })

// Any custom config you want to pass to Jest
const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
}

// createJestConfig is exported in this way to ensure that next/jest can load the Next.js configuration, which is async
module.exports = createJestConfig(customJestConfig)
```

### Relay

To enable [Relay](https://relay.dev/) support:

```js filename="next.config.js"
module.exports = {
  compiler: {
    relay: {
      // This should match relay.config.js
      src: './',
      artifactDirectory: './__generated__',
      language: 'typescript',
      eagerEsModules: false,
    },
  },
}
```

> **Good to know**: In Next.js, all JavaScript files in `pages` directory are considered routes. So, for `relay-compiler` you'll need to specify `artifactDirectory` configuration settings outside of the `pages`, otherwise `relay-compiler` will generate files next to the source file in the `__generated__` directory, and this file will be considered a route, which will break production builds.

### Remove React Properties

Allows to remove JSX properties. This is often used for testing. Similar to `babel-plugin-react-remove-properties`.

To remove properties matching the default regex `^data-test`:

```js filename="next.config.js"
module.exports = {
  compiler: {
    reactRemoveProperties: true,
  },
}
```

To remove custom properties:

```js filename="next.config.js"
module.exports = {
  compiler: {
    // The regexes defined here are processed in Rust so the syntax is different from
    // JavaScript `RegExp`s. See https://docs.rs/regex.
    reactRemoveProperties: { properties: ['^data-custom$'] },
  },
}
```

### Remove Console

This transform allows for removing all `console.*` calls in application code (not `node_modules`). Similar to `babel-plugin-transform-remove-console`.

Remove all `console.*` calls:

```js filename="next.config.js"
module.exports = {
  compiler: {
    removeConsole: true,
  },
}
```

Remove `console.*` output except `console.error`:

```js filename="next.config.js"
module.exports = {
  compiler: {
    removeConsole: {
      exclude: ['error'],
    },
  },
}
```

### Legacy Decorators

Next.js will automatically detect `experimentalDecorators` in `jsconfig.json` or `tsconfig.json`. Legacy decorators are commonly used with older versions of libraries like `mobx`.

This flag is only supported for compatibility with existing applications. We do not recommend using legacy decorators in new applications.

First, update to the latest version of Next.js: `npm install next@latest`. Then, update your `jsconfig.json` or `tsconfig.json` file:

```js
{
  "compilerOptions": {
    "experimentalDecorators": true
  }
}
```

### importSource

Next.js will automatically detect `jsxImportSource` in `jsconfig.json` or `tsconfig.json` and apply that. This is commonly used with libraries like [Theme UI](https://theme-ui.com).

First, update to the latest version of Next.js: `npm install next@latest`. Then, update your `jsconfig.json` or `tsconfig.json` file:

```js
{
  "compilerOptions": {
    "jsxImportSource": "theme-ui"
  }
}
```

### Emotion

We're working to port `@emotion/babel-plugin` to the Next.js Compiler.

First, update to the latest version of Next.js: `npm install next@latest`. Then, update your `next.config.js` file:

```js filename="next.config.js"

module.exports = {
  compiler: {
    emotion: boolean | {
      // default is true. It will be disabled when build type is production.
      sourceMap?: boolean,
      // default is 'dev-only'.
      autoLabel?: 'never' | 'dev-only' | 'always',
      // default is '[local]'.
      // Allowed values: `[local]` `[filename]` and `[dirname]`
      // This option only works when autoLabel is set to 'dev-only' or 'always'.
      // It allows you to define the format of the resulting label.
      // The format is defined via string where variable parts are enclosed in square brackets [].
      // For example labelFormat: "my-classname--[local]", where [local] will be replaced with the name of the variable the result is assigned to.
      labelFormat?: string,
      // default is undefined.
      // This option allows you to tell the compiler what imports it should
      // look at to determine what it should transform so if you re-export
      // Emotion's exports, you can still use transforms.
      importMap?: {
        [packageName: string]: {
          [exportName: string]: {
            canonicalImport?: [string, string],
            styledBaseImport?: [string, string],
          }
        }
      },
    },
  },
}
```

### Minification

Next.js' swc compiler is used for minification by default since v13. This is 7x faster than Terser.

> **Good to know:** Starting with v15, minification cannot be customized using `next.config.js`. Support for the `swcMinify` flag has been removed.

### Module Transpilation

Next.js can automatically transpile and bundle dependencies from local packages (like monorepos) or from external dependencies (`node_modules`). This replaces the `next-transpile-modules` package.

```js filename="next.config.js"
module.exports = {
  transpilePackages: ['@acme/ui', 'lodash-es'],
}
```

### Modularize Imports

This option has been superseded by [`optimizePackageImports`](/docs/app/api-reference/config/next-config-js/optimizePackageImports.md) in Next.js 13.5. We recommend upgrading to use the new option that does not require manual configuration of import paths.

### Define (Replacing variables during build)

The `define` option allows you to statically replace variables in your code at build-time.
The option takes an object as key-value pairs, where the keys are the variables that should be replaced with the corresponding values.

Use the `compiler.define` field in `next.config.js` to define variables for all environments (server, edge, and client). Or, use `compiler.defineServer` to define variables only for server-side (server and edge) code:

```js filename="next.config.js"
module.exports = {
  compiler: {
    define: {
      MY_VARIABLE: 'my-string',
      'process.env.MY_ENV_VAR': 'my-env-var',
    },
    defineServer: {
      MY_SERVER_VARIABLE: 'my-server-var',
    },
  },
}
```

### Build Lifecycle Hooks

The Next.js Compiler supports lifecycle hooks that allow you to run custom code at specific points during the build process. Currently, the following hook is supported:

#### runAfterProductionCompile

A hook function that executes after production build compilation finishes, but before running post-compilation tasks such as type checking and static page generation. This hook provides access to project metadata including the project directory and build output directory, making it useful for third-party tools to collect build outputs like sourcemaps.

```js filename="next.config.js"
module.exports = {
  compiler: {
    runAfterProductionCompile: async ({ distDir, projectDir }) => {
      // Your custom code here
    },
  },
}
```

The hook receives an object with the following properties:

* `distDir`: The build output directory (defaults to `.next`)
* `projectDir`: The root directory of the project

## Experimental Features

### SWC Trace profiling

You can generate SWC's internal transform traces as chromium's [trace event format](https://docs.google.com/document/d/1CvAClvFfyA5R-PhYUmn5OOQtYMH4h6I0nSsKchNAySU/preview?mode=html#%21=).

```js filename="next.config.js"
module.exports = {
  experimental: {
    swcTraceProfiling: true,
  },
}
```

Once enabled, swc will generate trace named as `swc-trace-profile-${timestamp}.json` under `.next/`. Chromium's trace viewer (chrome://tracing/, https://ui.perfetto.dev/), or compatible flamegraph viewer (https://www.speedscope.app/) can load & visualize generated traces.

### SWC Plugins (experimental)

You can configure swc's transform to use SWC's experimental plugin support written in wasm to customize transformation behavior.

```js filename="next.config.js"
module.exports = {
  experimental: {
    swcPlugins: [
      [
        'plugin',
        {
          ...pluginOptions,
        },
      ],
    ],
  },
}
```

`swcPlugins` accepts an array of tuples for configuring plugins. A tuple for the plugin contains the path to the plugin and an object for plugin configuration. The path to the plugin can be an npm module package name or an absolute path to the `.wasm` binary itself.

## Unsupported Features

When your application has a `.babelrc` file, Next.js will automatically fall back to using Babel for transforming individual files. This ensures backwards compatibility with existing applications that leverage custom Babel plugins.

If you're using a custom Babel setup, [please share your configuration](https://github.com/vercel/next.js/discussions/30174). We're working to port as many commonly used Babel transformations as possible, as well as supporting plugins in the future.

## Version History

| Version   | Changes                                                                                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v13.1.0` | [Module Transpilation](https://nextjs.org/blog/next-13-1#built-in-module-transpilation-stable) and [Modularize Imports](https://nextjs.org/blog/next-13-1#import-resolution-for-smaller-bundles) stable. |
| `v13.0.0` | SWC Minifier enabled by default.                                                                                                                                                                         |
| `v12.3.0` | SWC Minifier [stable](https://nextjs.org/blog/next-12-3#swc-minifier-stable).                                                                                                                            |
| `v12.2.0` | [SWC Plugins](#swc-plugins-experimental) experimental support added.                                                                                                                                     |
| `v12.1.0` | Added support for Styled Components, Jest, Relay, Remove React Properties, Legacy Decorators, Remove Console, and jsxImportSource.                                                                       |
| `v12.0.0` | Next.js Compiler [introduced](https://nextjs.org/blog/next-12).                                                                                                                                          |


--------------------------------------------------------------------------------
title: "Supported Browsers"
description: "Browser support and which JavaScript features are supported by Next.js."
source: "https://nextjs.org/docs/architecture/supported-browsers"
--------------------------------------------------------------------------------

# Supported Browsers

Next.js supports **modern browsers** with zero configuration.

* Chrome 111+
* Edge 111+
* Firefox 111+
* Safari 16.4+

## Browserslist

If you would like to target specific browsers or features, Next.js supports [Browserslist](https://browsersl.ist) configuration in your `package.json` file. Next.js uses the following Browserslist configuration by default:

```json filename="package.json"
{
  "browserslist": ["chrome 111", "edge 111", "firefox 111", "safari 16.4"]
}
```

## Polyfills

We inject [widely used polyfills](https://github.com/vercel/next.js/blob/canary/packages/next-polyfill-nomodule/src/index.js), including:

* [**fetch()**](https://developer.mozilla.org/docs/Web/API/Fetch_API) — Replacing: `whatwg-fetch` and `unfetch`.
* [**URL**](https://developer.mozilla.org/docs/Web/API/URL) — Replacing: the [`url` package (Node.js API)](https://nodejs.org/api/url.html).
* [**Object.assign()**](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) — Replacing: `object-assign`, `object.assign`, and `core-js/object/assign`.

If any of your dependencies include these polyfills, they’ll be eliminated automatically from the production build to avoid duplication.

In addition, to reduce bundle size, Next.js will only load these polyfills for browsers that require them. The majority of the web traffic globally will not download these polyfills.

### Custom Polyfills

If your own code or any external npm dependencies require features not supported by your target browsers (such as IE 11), you need to add polyfills yourself.

#### In App Router

To include polyfills, you can import them into the [`instrumentation-client.js` file](/docs/app/api-reference/file-conventions/instrumentation-client.md).

```ts filename="instrumentation-client.ts"
import './polyfills'
```

#### In Pages Router

In this case, you should add a top-level import for the **specific polyfill** you need in your [Custom `<App>`](/docs/pages/building-your-application/routing/custom-app.md) or the individual component.

```tsx filename="pages/_app.tsx" switcher
import './polyfills'

import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

```jsx filename="pages/_app.jsx" switcher
import './polyfills'

export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

#### Conditionally loading polyfills

The best approach is to isolate unsupported features to specific UI sections and conditionally load the polyfill if needed.

```ts filename="hooks/analytics.ts" switcher
import { useCallback } from 'react'

export const useAnalytics = () => {
  const tracker = useCallback(async (data: unknown) => {
    if (!('structuredClone' in globalThis)) {
      import('polyfills/structured-clone').then((mod) => {
        globalThis.structuredClone = mod.default
      })
    }

    /* Do some work that uses structured clone */
  }, [])

  return tracker
}
```

```js filename="hooks/analytics.js" switcher
import { useCallback } from 'react'

export const useAnalytics = () => {
  const tracker = useCallback(async (data) => {
    if (!('structuredClone' in globalThis)) {
      import('polyfills/structured-clone').then((mod) => {
        globalThis.structuredClone = mod.default
      })
    }

    /* Do some work that uses structured clone */
  }, [])

  return tracker
}
```

## JavaScript Language Features

Next.js allows you to use the latest JavaScript features out of the box. In addition to [ES6 features](https://github.com/lukehoban/es6features), Next.js also supports:

* [Async/await](https://github.com/tc39/ecmascript-asyncawait) (ES2017)
* [Object Rest/Spread Properties](https://github.com/tc39/proposal-object-rest-spread) (ES2018)
* [Dynamic `import()`](https://github.com/tc39/proposal-dynamic-import) (ES2020)
* [Optional Chaining](https://github.com/tc39/proposal-optional-chaining) (ES2020)
* [Nullish Coalescing](https://github.com/tc39/proposal-nullish-coalescing) (ES2020)
* [Class Fields](https://github.com/tc39/proposal-class-fields) and [Static Properties](https://github.com/tc39/proposal-static-class-features) (ES2022)
* and more!

### TypeScript Features

Next.js has built-in TypeScript support. [Learn more here](/docs/pages/api-reference/config/typescript.md).

### Customizing Babel Config (Advanced)

You can customize babel configuration. [Learn more here](/docs/pages/guides/babel.md).



--------------------------------------------------------------------------------
title: "Next.js Community"
description: "Get involved in the Next.js community."
source: "https://nextjs.org/docs/community"
--------------------------------------------------------------------------------

# Community

With over 5 million weekly downloads, Next.js has a large and active community of developers across the world. Here's how you can get involved in our community:

## Contributing

There are a couple of ways you can contribute to the development of Next.js:

* [Documentation](/docs/community/contribution-guide.md): Suggest improvements or even write new sections to help our users understand how to use Next.js.
* [Examples](https://github.com/vercel/next.js/tree/canary/contributing/examples): Help developers integrate Next.js with other tools and services by creating a new example or improving an existing one.
* [Codebase](https://github.com/vercel/next.js/tree/canary/contributing/core): Learn more about the underlying architecture, contribute to bug fixes, errors, and suggest new features.

## Discussions

If you have a question about Next.js, or want to help others, you're always welcome to join the conversation:

* [GitHub Discussions](https://github.com/vercel/next.js/discussions)
* [Discord](https://discord.com/invite/bUG2bvbtHy)
* [Reddit](https://www.reddit.com/r/nextjs)

## Social Media

Follow Next.js on [Twitter](https://x.com/nextjs) for the latest updates, and subscribe to the [Vercel YouTube channel](https://www.youtube.com/@VercelHQ) for Next.js videos.

## Code of Conduct

We believe in creating an inclusive, welcoming community. As such, we ask all members to adhere to our [Code of Conduct](https://github.com/vercel/next.js/blob/canary/CODE_OF_CONDUCT.md). This document outlines our expectations for participant behavior. We invite you to read it and help us maintain a safe and respectful environment.

 - [Contribution Guide](/docs/community/contribution-guide.md)
 - [Rspack](/docs/community/rspack.md)

--------------------------------------------------------------------------------
title: "Docs Contribution Guide"
description: "Learn how to contribute to Next.js Documentation"
source: "https://nextjs.org/docs/community/contribution-guide"
--------------------------------------------------------------------------------

# Contribution Guide

Welcome to the Next.js Docs Contribution Guide! We're excited to have you here.

This page provides instructions on how to edit the Next.js documentation. Our goal is to ensure that everyone in the community feels empowered to contribute and improve our docs.

## Why Contribute?

Open-source work is never done, and neither is documentation. Contributing to docs is a good way for beginners to get involved in open-source and for experienced developers to clarify more complex topics while sharing their knowledge with the community.

By contributing to the Next.js docs, you're helping us build a more robust learning resource for all developers. Whether you've found a typo, a confusing section, or you've realized that a particular topic is missing, your contributions are welcomed and appreciated.

## How to Contribute

The docs content can be found on the [Next.js repo](https://github.com/vercel/next.js/tree/canary/docs). To contribute, you can edit the files directly on GitHub or clone the repo and edit the files locally.

### GitHub Workflow

If you're new to GitHub, we recommend reading the [GitHub Open Source Guide](https://opensource.guide/how-to-contribute/#opening-a-pull-request) to learn how to fork a repository, create a branch, and submit a pull request.

> **Good to know**: The underlying docs code lives in a private codebase that is synced to the Next.js public repo. This means that you can't preview the docs locally. However, you'll see your changes on [nextjs.org](https://nextjs.org/docs) after merging a pull request.

### Writing MDX

The docs are written in [MDX](https://mdxjs.com/), a markdown format that supports JSX syntax. This allows us to embed React components in the docs. See the [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) for a quick overview of markdown syntax.

### VSCode

#### Previewing Changes Locally

VSCode has a built-in markdown previewer that you can use to see your edits locally. To enable the previewer for MDX files, you'll need to add a configuration option to your user settings.

Open the command palette (`⌘ + ⇧ + P` on Mac or `Ctrl + Shift + P` on Windows) and search from `Preferences: Open User Settings (JSON)`.

Then, add the following line to your `settings.json` file:

```json filename="settings.json"
{
  "files.associations": {
    "*.mdx": "markdown"
  }
}
```

Next, open the command palette again, and search for `Markdown: Preview File` or `Markdown: Open Preview to the Side`. This will open a preview window where you can see your formatted changes.

#### Extensions

We also recommend the following extensions for VSCode users:

* [MDX](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx): Intellisense and syntax highlighting for MDX.
* [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Format MDX files on save.

### Review Process

Once you've submitted your contribution, the Next.js or Developer Experience teams will review your changes, provide feedback, and merge the pull request when it's ready.

Please let us know if you have any questions or need further assistance in your PR's comments. Thank you for contributing to the Next.js docs and being a part of our community!

> **Tip:** Run `pnpm prettier-fix` to run Prettier before submitting your PR.

## File Structure

The docs use **file-system routing**. Each folder and files inside [`/docs`](https://github.com/vercel/next.js/tree/canary/docs) represent a route segment. These segments are used to generate the URL paths, navigation, and breadcrumbs.

The file structure reflects the navigation that you see on the site, and by default, navigation items are sorted alphabetically. However, we can change the order of the items by prepending a two-digit number (`00-`) to the folder or file name.

For example, in the [functions API Reference](/docs/app/api-reference/functions.md), the pages are sorted alphabetically because it makes it easier for developers to find a specific function:

```txt
04-functions
├── after.mdx
├── cacheLife.mdx
├── cacheTag.mdx
└── ...
```

But, in the [routing section](/docs/app.md), the files are prefixed with a two-digit number, sorted in the order developers should learn these concepts:

```txt
01-routing
├── 01-defining-routes.mdx
├── 02-pages.mdx
├── 03-layouts-and-templates.mdx
└── ...
```

To quickly find a page, you can use `⌘ + P` (Mac) or `Ctrl + P` (Windows) to open the search bar on VSCode. Then, type the slug of the page you're looking for. E.g. `defining-routes`

> **Why not use a manifest?**
>
> We considered using a manifest file (another popular way to generate the docs navigation), but we found that a manifest would quickly get out of sync with the files. File-system routing forces us to think about the structure of the docs and feels more native to Next.js.

## Metadata

Each page has a metadata block at the top of the file separated by three dashes.

### Required Fields

The following fields are **required**:

| Field         | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| `title`       | The page's `<h1>` title, used for SEO and OG Images.                         |
| `description` | The page's description, used in the `<meta name="description">` tag for SEO. |

```yaml filename="required-fields.mdx"
---
title: Page Title
description: Page Description
---
```

It's good practice to limit the page title to 2-3 words (e.g. Optimizing Images) and the description to 1-2 sentences (e.g. Learn how to optimize images in Next.js).

### Optional Fields

The following fields are **optional**:

| Field       | Description                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `nav_title` | Overrides the page's title in the navigation. This is useful when the page's title is too long to fit. If not provided, the `title` field is used. |
| `source`    | Pulls content into a shared page. See [Shared Pages](#shared-pages).                                                                               |
| `related`   | A list of related pages at the bottom of the document. These will automatically be turned into cards. See [Related Links](#related-links).         |
| `version`   | A stage of development. e.g. `experimental`,`legacy`,`unstable`,`RC`                                                                               |

```yaml filename="optional-fields.mdx"
---
nav_title: Nav Item Title
source: app/building-your-application/optimizing/images
related:
  description: See the image component API reference.
  links:
    - app/api-reference/components/image
version: experimental
---
```

## `App` and `Pages` Docs

Since most of the features in the **App Router** and **Pages Router** are completely different, their docs for each are kept in separate sections (`02-app` and `03-pages`). However, there are a few features that are shared between them.

### Shared Pages

To avoid content duplication and risk the content becoming out of sync, we use the `source` field to pull content from one page into another. For example, the `<Link>` component behaves *mostly* the same in **App** and **Pages**. Instead of duplicating the content, we can pull the content from `app/.../link.mdx` into `pages/.../link.mdx`:

```mdx filename="app/.../link.mdx"
---
title: <Link>
description: API reference for the <Link> component.
---

This API reference will help you understand how to use the props
and configuration options available for the Link Component.
```

```mdx filename="pages/.../link.mdx"
---
title: <Link>
description: API reference for the <Link> component.
source: app/api-reference/components/link
---

{/* DO NOT EDIT THIS PAGE. */}
{/* The content of this page is pulled from the source above. */}
```

We can therefore edit the content in one place and have it reflected in both sections.

### Shared Content

In shared pages, sometimes there might be content that is **App Router** or **Pages Router** specific. For example, the `<Link>` component has a `shallow` prop that is only available in **Pages** but not in **App**.

To make sure the content only shows in the correct router, we can wrap content blocks in an `<AppOnly>` or `<PagesOnly>` components:

```mdx filename="app/.../link.mdx"
This content is shared between App and Pages.

<PagesOnly>

This content will only be shown on the Pages docs.

</PagesOnly>

This content is shared between App and Pages.
```

You'll likely use these components for examples and code blocks.

## Code Blocks

Code blocks should contain a minimum working example that can be copied and pasted. This means that the code should be able to run without any additional configuration.

For example, if you're showing how to use the `<Link>` component, you should include the `import` statement and the `<Link>` component itself.

```tsx filename="app/page.tsx"
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

Always run examples locally before committing them. This will ensure that the code is up-to-date and working.

### Language and Filename

Code blocks should have a header that includes the language and the `filename`. Add a `filename` prop to render a special Terminal icon that helps orientate users where to input the command. For example:

````mdx filename="code-example.mdx"
```bash filename="Terminal"
npx create-next-app
```
````

Most examples in the docs are written in `tsx` and `jsx`, and a few in `bash`. However, you can use any supported language, here's the [full list](https://github.com/shikijs/shiki/blob/main/docs/languages.md#all-languages).

When writing JavaScript code blocks, we use the following language and extension combinations.

|                                | Language | Extension |
| ------------------------------ | -------- | --------- |
| JavaScript files with JSX code | `jsx   | .js       |
| JavaScript files without JSX   | `js    | .js       |
| TypeScript files with JSX      | `tsx   | .tsx      |
| TypeScript files without JSX   | `ts    | .ts       |

> **Good to know**:
>
> * Make sure to use **`.js`** extension for JavaScript files with **JSX** code.
> * For example, \`\`\`jsx filename="app/layout.js"

### TS and JS Switcher

Add a language switcher to toggle between TypeScript and JavaScript. Code blocks should be TypeScript first with a JavaScript version to accommodate users.

Currently, we write TS and JS examples one after the other, and link them with `switcher` prop:

````mdx filename="code-example.mdx"
```tsx filename="app/page.tsx" switcher

```

```jsx filename="app/page.js" switcher

```
````

> **Good to know**: We plan to automatically compile TypeScript snippets to JavaScript in the future. In the meantime, you can use [transform.tools](https://transform.tools/typescript-to-javascript).

### Line Highlighting

Code lines can be highlighted. This is useful when you want to draw attention to a specific part of the code. You can highlight lines by passing a number to the `highlight` prop.

**Single Line:** `highlight={1}`

```tsx filename="app/page.tsx" {1}
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

**Multiple Lines:** `highlight={1,3}`

```tsx filename="app/page.tsx" highlight={1,3}
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

**Range of Lines:** `highlight={1-5}`

```tsx filename="app/page.tsx" highlight={1-5}
import Link from 'next/link'

export default function Page() {
  return <Link href="/about">About</Link>
}
```

## Icons

The following icons are available for use in the docs:

```mdx filename="mdx-icon.mdx"
<Check size={18} />
<Cross size={18} />
```

**Output:**

We do not use emojis in the docs.

## Notes

For information that is important but not critical, use notes. Notes are a good way to add information without distracting the user from the main content.

```mdx filename="notes.mdx"
> **Good to know**: This is a single line note.

> **Good to know**:
>
> - We also use this format for multi-line notes.
> - There are sometimes multiple items worth knowing or keeping in mind.
```

**Output:**

> **Good to know**: This is a single line note.

> **Good to know**:
>
> * We also use this format for multi-line notes.
> * There are sometimes multiple items worth knowing or keeping in mind.

## Related Links

Related Links guide the user's learning journey by adding links to logical next steps.

* Links will be displayed in cards under the main content of the page.
* Links will be automatically generated for pages that have child pages.

Create related links using the `related` field in the page's metadata.

```yaml filename="example.mdx"
---
related:
  description: Learn how to quickly get started with your first application.
  links:
    - app/building-your-application/routing/defining-routes
    - app/building-your-application/data-fetching
    - app/api-reference/file-conventions/page
---
```

### Nested Fields

| Field         | Required? | Description                                                                                                                                               |
| ------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | Optional  | The title of the card list. Defaults to **Next Steps**.                                                                                                   |
| `description` | Optional  | The description of the card list.                                                                                                                         |
| `links`       | Required  | A list of links to other doc pages. Each list item should be a relative URL path (without a leading slash) e.g. `app/api-reference/file-conventions/page` |

## Diagrams

Diagrams are a great way to explain complex concepts. We use [Figma](https://www.figma.com/) to create diagrams, following Vercel's design guide.

The diagrams currently live in the `/public` folder in our private Next.js site. If you'd like to update or add a diagram, please open a [GitHub issue](https://github.com/vercel/next.js/issues/new?assignees=\&labels=template%3A+documentation\&projects=\&template=4.docs_request.yml\&title=Docs%3A+) with your ideas.

## Custom Components and HTML

These are the React Components available for the docs: `<Image />` (next/image), `<PagesOnly />`, `<AppOnly />`, `<Cross />`, and `<Check />`. We do not allow raw HTML in the docs besides the `<details>` tag.

If you have ideas for new components, please open a [GitHub issue](https://github.com/vercel/next.js/issues/new/choose).

## Style Guide

This section contains guidelines for writing docs for those who are new to technical writing.

### Page Templates

While we don't have a strict template for pages, there are page sections you'll see repeated across the docs:

* **Overview:** The first paragraph of a page should tell the user what the feature is and what it's used for. Followed by a minimum working example or its API reference.
* **Convention:** If the feature has a convention, it should be explained here.
* **Examples**: Show how the feature can be used with different use cases.
* **API Tables**: API Pages should have an overview table at the of the page with jump-to-section links (when possible).
* **Next Steps (Related Links)**: Add links to related pages to guide the user's learning journey.

Feel free to add these sections as needed.

### Page Types

Docs pages are also split into two categories: Conceptual and Reference.

* **Conceptual** pages are used to explain a concept or feature. They are usually longer and contain more information than reference pages. In the Next.js docs, conceptual pages are found in the **Building Your Application** section.
* **Reference** pages are used to explain a specific API. They are usually shorter and more focused. In the Next.js docs, reference pages are found in the **API Reference** section.

> **Good to know**: Depending on the page you're contributing to, you may need to follow a different voice and style. For example, conceptual pages are more instructional and use the word *you* to address the user. Reference pages are more technical, they use more imperative words like "create, update, accept" and tend to omit the word *you*.

### Voice

Here are some guidelines to maintain a consistent style and voice across the docs:

* Write clear, concise sentences. Avoid tangents.
  * If you find yourself using a lot of commas, consider breaking the sentence into multiple sentences or use a list.
  * Swap out complex words for simpler ones. For example, *use* instead of *utilize*.
* Be mindful with the word *this*. It can be ambiguous and confusing, don't be afraid to repeat the subject of the sentence if unclear.
  * For example, *Next.js uses React* instead of *Next.js uses this*.
* Use an active voice instead of passive. An active sentence is easier to read.
  * For example, *Next.js uses React* instead of *React is used by Next.js*. If you find yourself using words like *was* and *by* you may be using a passive voice.
* Avoid using words like *easy*, *quick*, *simple*, *just*, etc. This is subjective and can be discouraging to users.
* Avoid negative words like *don't*, *can't*, *won't*, etc. This can be discouraging to readers.
  * For example, *"You can use the `Link` component to create links between pages"* instead of *"Don't use the `<a>` tag to create links between pages"*.
* Write in second person (you/your). This is more personal and engaging.
* Use gender-neutral language. Use *developers*, *users*, or *readers*, when referring to the audience.
* If adding code examples, ensure they are properly formatted and working.

While these guidelines are not exhaustive, they should help you get started. If you'd like to dive deeper into technical writing, check out the [Google Technical Writing Course](https://developers.google.com/tech-writing/overview).

***

Thank you for contributing to the docs and being part of the Next.js community!


--------------------------------------------------------------------------------
title: "Rspack Integration"
description: "Use the `next-rspack` plugin to bundle your Next.js with Rspack."
source: "https://nextjs.org/docs/community/rspack"
--------------------------------------------------------------------------------

# Rspack

> This feature is currently experimental and subject to change, it is not recommended for production.

The Rspack team has created a community plugin for Next.js, which is part of a [partnering effort](https://rspack.rs/blog/rspack-next-partner) with the Rspack team.

This plugin is currently experimental. Please use this [discussion thread](https://github.com/vercel/next.js/discussions/77800) to give feedback on any issues you encounter.

Learn more on the [Rspack docs](https://rspack.rs/guide/tech/next) and try out [this example](https://github.com/vercel/next.js/tree/canary/examples/with-rspack).


    
---

**Navigation:** [← Previous](./17-images.md) | [Index](./index.md) | Next →
