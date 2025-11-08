**Navigation:** [← Previous](./04-vercel-remove.md) | [Index](./index.md) | [Next →](./06-trusted-ips.md)

---

# NO\_CORS\_HEADERS

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Misconfiguring CORS ([Cross Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)) headers can introduce security risks, potentially exposing private and/or secure information such as API keys and user data.

This rule is not meant to block usage of CORS. Instead, it is designed to flag potentially risky configuration for review by the appropriate engineer(s) or team(s).

For more information around the risks associated with CORS, including testing for potential vulnerabilities, see:

*   [OWASP: HTML5 Security Cheat Sheet - Cross Origin Resource Sharing](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#cross-origin-resource-sharing)
*   [OWASP: Web Security Testing Guide - Testing Cross Origin Resource Sharing](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/07-Testing_Cross_Origin_Resource_Sharing)
*   [OWASP: CORS OriginHeaderScrutiny](https://owasp.org/www-community/attacks/CORS_OriginHeaderScrutiny)

## [Examples](#examples)

The examples below are common approaches to settings CORS headers in JavaScript applications. All of these examples will be caught by this rule.

```
response.headers.set('Access-Control-Allow-Origin', '*');
 
const headers = {
  'Access-Control-Allow-Credentials': true,
};
 
const options = {
  headers: [
    {
      key: 'Access-Control-Max-Age',
      value: 600,
    },
  ],
};
 
const headers = new Headers();
headers.append('Access-Control-Allow-Methods', '*');
```

Additionally, this rule will catch partial matches, such as a template literal. In this example, the rule will match the `"Access-Control-"` part of the template literal.

```
const headers = new Headers();
headers.append(`Access-Control-${HEADER_TYPE}`, '*');
```

## [How to fix](#how-to-fix)

Engineers should reach out to the appropriate engineer(s) or team(s) for a security review of the configuration.

When requesting a review, please provide as much information as possible around the proposed CORS configuration. Where applicable, include information around alternative approaches, and why this approach is preferable.

As there are many ways to configure CORS headers in applications, this rule will match any string that looks like a possible CORS header. We've tried to mitigate the risk of false-positives, but if they occur they will need to be added to the allowlists.

--------------------------------------------------------------------------------
title: "NO_DANGEROUS_HTML"
description: "Prevent the unsafe creation of DOM via HTML methods in your application."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_DANGEROUS_HTML"
--------------------------------------------------------------------------------

# NO\_DANGEROUS\_HTML

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Unsafe creation of DOM can be done a variety of ways:

*   `element.innerHTML`
*   `element.outerHTML`
*   `DOMParser.parseFromString()`
*   `element.insertAdjacentHTML()`
*   `srcdoc` on iframe elements
*   `dangerouslySetInnerHTML` prop in React apps

Usage of these methods is deemed an unsafe coding practice as the HTML might result in security vulnerabilities.

## [How to fix](#how-to-fix)

It is recommended to instead use alternative approaches for HTML construction - such as `document.createElement()` or a HTML sanitizer.

--------------------------------------------------------------------------------
title: "NO_DOCUMENT_WRITE"
description: "Prevent unsafe usage of document.write() in your application."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_DOCUMENT_WRITE"
--------------------------------------------------------------------------------

# NO\_DOCUMENT\_WRITE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Calls to `document.write()` or `document.writeln()` manipulate DOM directly without any sanitization and should be avoided.

Furthermore, these APIs can also cause performance issues and trigger will clear the page contents if used after page load.

## [How to fix](#how-to-fix)

Avoid usage of `document.write()` entirely in your application, and instead either use UI framework like React to handle writing to the document, or use safer DOM APIs, such as `document.createElement()` instead.

--------------------------------------------------------------------------------
title: "NO_EVAL"
description: "Prevent unsafe usage of eval() in your application."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_EVAL"
--------------------------------------------------------------------------------

# NO\_EVAL

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

JavaScript's `eval()` function is potentially dangerous, is often misused, and might cause security issues. Using `eval()` on untrusted code can open an application up to several different injection attacks.

This rule will also catch eval-like function usage (or _implied eval_), such as passing a string as the first argument to `setTimeout`.

This is especially dangerous when working with data from external sources.

```
const dontDoThis = req.body;
setTimeout(dontDoThis, 1000);
```

For more information on why you should never use evaluation, see the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#never_use_eval!).

## [Example](#example)

The lines below (and variations of those) will all be caught by this rule.

```
eval('() => console.log("DROP TABLE")');
 
setTimeout('() => console.log("DROP TABLE")', 1000);
 
window.setInterval('() => console.log("DROP TABLE")', 1000);
 
new Function('() => console.log("DROP TABLE")');
```

### [References](#references)

Conformance rules are not type-aware, but will follow variable references within the current module (or file).

```
import { importedVar } from 'foo';
 
// No error reported, as this rule doesn't have access to the value.
setTimeout(importedVar, 100);
 
const localVar = 'bar';
 
// An error will be reported, as the variable was declared in this file.
setTimeout(localVar, 100);
```

## [How to fix](#how-to-fix)

Avoid usage of this type of evaluation entirely in your application. Instead, you should write the same functionality as raw code (not within a string).

```
setTimeout(() => {
  console.log('Safe usage');
});
```

--------------------------------------------------------------------------------
title: "NO_EXTERNAL_CSS_AT_IMPORTS"
description: "Disallows @import at-rules that import from URLs."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_EXTERNAL_CSS_AT_IMPORTS"
--------------------------------------------------------------------------------

# NO\_EXTERNAL\_CSS\_AT\_IMPORTS

Copy page

Ask AI about this page

Last updated September 24, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Importing CSS through ([`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/@import)) is render blocking, causing browsers to sequentially download and parse the imported CSS (a [critical request chain](https://developer.chrome.com/en/docs/lighthouse/performance/critical-request-chains/)).

app.module.css

```
@import url('https://fonts.googleapis.com/css2?family=Inter');
```

This can result in a [flash of unstyled content (FOUC)](https://en.wikipedia.org/wiki/Flash_of_unstyled_content), where page content is briefly shown without complete styles until all required CSS has been downloaded and parsed, along with slower page load times.

Imports to relative paths are processed by frameworks like Next.js, and will not be affected by this issue.

app.module.css

```
/* This import is safe. */
@import './globals.css';
```

Note that this rule currently only parses CSS and not CSS written in Less, Sass, or other CSS preprocessor syntaxes.

## [How to fix](#how-to-fix)

If you're importing a font, you can use [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) which will automatically optimize your fonts (including custom fonts) and remove external network requests.

If you're importing CSS, such as Bootstrap, avoid loading it from external sources, such as a CDN or the [Next.js public folder](https://nextjs.org/docs/basic-features/static-file-serving). Instead, you can import that CSS relatively, or from a package.

layout.tsx

```
// CSS imported relatively from a local file.
import './globals.css';
// CSS from a package in `node_modules`.
import 'bootstrap/dist/css/bootstrap.css';
 
interface RootLayoutProps {
  children: React.ReactNode;
}
 
export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <head />
      <body>{children}</body>
    </html>
  );
}
```

--------------------------------------------------------------------------------
title: "NO_FETCH_FROM_MIDDLEWARE"
description: "Requires that any fetch call that is depended on transitively by Next.js middleware be reviewed and approved before use."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_FETCH_FROM_MIDDLEWARE"
--------------------------------------------------------------------------------

# NO\_FETCH\_FROM\_MIDDLEWARE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

[Next.js middleware](https://nextjs.org/docs/advanced-features/middleware) runs code at the Edge. This means that the code is globally distributed. When middleware makes a `fetch` call, it may be to a backend that is not globally distributed, in which case the latency of the middleware function will be really slow. To prevent this, `fetch` calls that can be made from middleware are flagged and reviewed to make sure that it looks like an appropriate use.

## [Example](#example)

This check will fail when a `fetch` call is detected from Next.js middleware or transitive dependencies used by the middleware file.

In this example, there are two files. An experiments file asynchronously fetches experiments using `fetch`. The middleware file uses the experiments library to fetch the experiments and then decide to rewrite the URL.

experiments.ts

```
export async function getExperiments() {
  const res = await fetch('/experiments');
  return res.json();
}
```

middleware.ts

```
export async function middleware(
  request: NextRequest,
  event: NextFetchEvent,
): Promise<Response> {
  const experiments = await getExperiments();
 
  if (experiments.includes('new-marketing-page)) {
    return NextResponse.rewrite(MARKETING_PAGE_URL);
  }
  return NextResponse.next();
}
```

## [How to fix](#how-to-fix)

The correct fix will depend on the specific situation. If the server that is being called is globally distributed, then this asynchronous call may be okay. If not, then the code should try to remove the `fetch` statement to avoid making a request that would add latency to middleware.

--------------------------------------------------------------------------------
title: "NO_INLINE_SVG"
description: "Prevent the use of `svg` tags inline."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_INLINE_SVG"
--------------------------------------------------------------------------------

# NO\_INLINE\_SVG

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.3.0.

Preventing the use of `<svg></svg>` inline improves the health of your codebase at the page level. Using inlined `svg` tags in excess can cause hydration issues, negatively impact the performance of both the browser and the server rendering.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

## [How to fix](#how-to-fix)

If you hit this issue, you can resolve it by using SVGs as an [`<Image>`](https://nextjs.org/docs/pages/api-reference/components/image) component. Don't forget to enable [`dangerouslyAllowSVG`](https://nextjs.org/docs/pages/api-reference/components/image#dangerouslyallowsvg) in your application's `next.config.js` file, and use the `unoptimized` component prop.

.app/page.js

```
import Image from 'next/image'

export default function Page() {
  return (
    <Image
      src="/logo.svg"
      width={100}
      height={100}
      alt="Logo of ACME"
      unoptimized
    />
  )
}
```

--------------------------------------------------------------------------------
title: "NO_INSTANCEOF_ERROR"
description: "Disallows using `error instanceof Error` comparisons due to risk of false negatives."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_INSTANCEOF_ERROR"
--------------------------------------------------------------------------------

# NO\_INSTANCEOF\_ERROR

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.5.0.

A common pattern for checking if an object is an error is to use `error instanceof Error`.

This pattern is problematic because errors can come from other [realms](https://tc39.es/ecma262/#realm). Errors from other realms are instantiated from the realm's global `Error` constructor, and are therefore not instances of the current realm's global `Error` constructor and will not pass the `instanceof` check.

Some examples of where you might hit this include:

*   In Node.js, errors from a workers are instances of `Error` from the worker's global environment.
*   In browser environments, errors from `iframe` are instances of `Error` from the `iframe`'s global environment (i.e. `iframe.contentWindow.Error`).

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

## [Examples](#examples)

In this example, an error is returned from a [`vm`](https://nodejs.org/api/vm.html) context. As this error was created in a different realm, `instanceof Error` returns false.

```
const vm = require('node:vm');
 
const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);
 
if (error instanceof Error) {
  // Returns `false` because `error` is from a different realm.
}
```

## [How to fix](#how-to-fix)

### [Node.js](#node.js)

You can use [`isNativeError`](https://nodejs.org/api/util.html#utiltypesisnativeerrorvalue) in Node.js environments, which will return `true` for errors from other realms.

```
import { isNativeError } from 'node:util/types';
const vm = require('node:vm');
 
const context = vm.createContext({});
const error = vm.runInContext('new Error()', context);
 
if (isNativeError(error)) {
  // ...
}
```

### [Browsers](#browsers)

Use a library like [`is-error`](https://www.npmjs.com/package/is-error) to ensure you cover errors from other realms.

You can also use `Object.prototype.toString.call(error) === '[object Error]'` in some cases. This method will not work for custom errors, and you'll need to traverse the prototype chain (i.e. `Object.getPrototypeOf(error)`)to handle those cases.

The following code is a simplified version of the code used in the `is-error` library:

```
function isError(error) {
  if (typeof error !== 'object') {
    return false;
  }
 
  if (error instanceof Error) {
    return true;
  }
 
  let currentError = error;
  while (currentError) {
    if (Object.prototype.toString.call(currentError) === '[object Error]') {
      return true;
    }
    currentError = Object.getPrototypeOf(currentError);
  }
 
  return false;
}
```

--------------------------------------------------------------------------------
title: "NO_MIXED_ASYNC_MODULES"
description: "Prevent imports to modules that contain top-level awaits in your applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_MIXED_ASYNC_MODULES"
--------------------------------------------------------------------------------

# NO\_MIXED\_ASYNC\_MODULES

Copy page

Ask AI about this page

Last updated July 18, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Top-level await expressions in modules that are imported by other modules in sync prevent possible lazy module optimizations from being deployed on the module containing the top-level await.

One such optimization this prevents is inline lazy imports. Inline lazy imports allow for modules to be lazily evaluated and executed when they're used, rather than at initialization time of the module that uses them, improving initialization performance.

This is particularly impactful for modules that might only be used conditionally or given a user's interaction which might happen much latter in an application. Without this optimization, the module initialization times, such as for cold boots on Vercel Functions, could be slowed down for every request.

## [How to fix](#how-to-fix)

Consider refactoring the import to a dynamic import instead, or removing the top-level await in favor of standard import.

If a top-level await is important, then it's important that any other modules importing the module with the top-level await do so dynamically, as to avoid affecting initialization performance.

For example, this can be refactored:

```
// Contains a top-level await
import { asyncConfig } from 'someModule';
 
function doSomething(data) {
  processData(data, asyncConfig);
}
```

To this:

```
function doSomething(data) {
  import('someModule').then(({ asyncConfig }) => {
    processData(data, asyncConfig);
  });
}
```

Or this:

```
import { asyncConfig } from 'someModule';
 
// Note the async keyword on the function
async function doSomething(data) {
  processData(data, asyncConfig);
}
```

--------------------------------------------------------------------------------
title: "NO_POSTINSTALL_SCRIPT"
description: "Prevent the use of `"postinstall"` script in packages."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_POSTINSTALL_SCRIPT"
--------------------------------------------------------------------------------

# NO\_POSTINSTALL\_SCRIPT

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.4.0.

Modifying, adding, or updating any dependencies in your application triggers the execution of the `"postinstall"` script. Consequently, incorporating a `"postinstall"` script in your application's package.json leads to increased installation times for all users.

## [How to fix](#how-to-fix)

If you hit this issue, you can resolve it by removing the `"postinstall"` script in the `package.json` file.

package.json

```
{
  "scripts": {
    "postinstall": "sleep 360"
  },
}
```

--------------------------------------------------------------------------------
title: "NO_SERIAL_ASYNC_CALLS"
description: "Prevent blocking serial async await calls in your applications."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_SERIAL_ASYNC_CALLS"
--------------------------------------------------------------------------------

# NO\_SERIAL\_ASYNC\_CALLS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Sequential execution of async/await calls can significantly impact performance because each await call prevents further execution until resolving its Promise. This rule aims to refactor sequential async/await calls into parallel executions to enhance performance.

You should note that this rule might not flag some async/await usage patterns. For example:

*   Patterns involving conditional statements
*   Call expressions
*   Patterns that await in a manner that suggests non-serial dependencies between calls

For instance, scenarios where async calls depend conditionally on each other or are part of complex expressions are not flagged. This includes cases where one async call's outcome is necessary for subsequent calls, requiring serial execution due to logical or dependency reasons.

The following example will not be flagged by this rule:

```
async function updateDatabase() {
  const result1 = await async1();
  const result2 = await async2();
  doSomething(result1, result2);
}
```

These patterns fall outside the scope of this rule because safely suggesting parallelization requires more context, and the rule uses conservative heuristics to avoid false positives.

## [How to fix](#how-to-fix)

Instead, of executing async logic sequentially, opt to refactor the logic so it can be run parallel.

This can be fixed using `Promise.all`:

```
export async function getStaticProps() {
  const firstThing = await getFirstThing();
  const secondThing = await getSecondThing();
 
  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```

We can extract both `await` expressions into a single `Promise.all`, as follows:

```
export async function getStaticProps() {
  const [firstThing, secondThing] = await Promise.all([
    getFirstThing(),
    getSecondThing(),
  ]);
 
  return {
    props: {
      firstThing,
      secondThing,
    },
  };
}
```

--------------------------------------------------------------------------------
title: "NO_UNNECESSARY_PROP_SPREADING"
description: "Disallows the usage of object spreading in a JSX component."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_UNNECESSARY_PROP_SPREADING"
--------------------------------------------------------------------------------

# NO\_UNNECESSARY\_PROP\_SPREADING

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.6.0.

This rule detects the usage of the spread operator when spreading an object as a prop within a JSX component.

When spreading an object in the component, the data types of the object's properties are not validated, potentially causing unexpected runtime errors or unintended behavior.

## [Examples](#examples)

In the following example, the `Header` component contains an object with the spread operator being applied to it.

We don't know if the props that the `Header` component reads will accept all the values contained in the `foo` object.

app/dashboard/page.tsx

```
function HomePage() {
  return <Header {...{ foo }}>Hello World</Header>;
}
 
export default HomePage;
```

## [How to fix](#how-to-fix)

You can remove the spread operator from the JSX component, and list all props explicitly.

app/dashboard/page.tsx

```
function HomePage() {
  return (
    <Header bar={foo.bar} baz={foo.baz}>
      Hello World
    </Header>
  );
}
 
export default HomePage;
```

In the example above, [TypeScript](https://www.typescriptlang.org/) will be able to type-check all props.

--------------------------------------------------------------------------------
title: "NO_VARIABLE_IMPORT_REFERENCES"
description: "import and require statements must be passed string literals to avoid arbitrary user access to code."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/NO_VARIABLE_IMPORT_REFERENCES"
--------------------------------------------------------------------------------

# NO\_VARIABLE\_IMPORT\_REFERENCES

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

`import` and `require` statements load code from another file. When the location of the import is influenced by user input, the user may be able to load code that would otherwise be inaccessible to them. Such imports should protect against this by adding guards to make sure that arbitrary code can not be loaded from the import statement.

## [Example](#example)

The following code would be flagged by this rule:

```
function loadDynamicCode(moduleName: string) {
  return import(moduleName);
}
```

In this example, it can not be guaranteed that the `moduleName` that is provided would not be arbitrary input that could load unintended code.

## [How to fix](#how-to-fix)

Instances of this rule should be reviewed by a knowledgeable security person. If user input is used to select which module is loaded, guards against arbitrary strings should be added, such as only allowing access to a list of valid options. If no user input is involved in the import, then this code could be allowlisted after being reviewed by a security team member, but developers should be careful to ensure that only the desired code can be loaded.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_DESCRIPTION_REQUIRED"
description: "Requires that every package.json file has the description field set."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_DESCRIPTION\_REQUIRED

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that every `package.json` has a `description` field. This field is used to describe the workspace's purpose within the monorepo.

See the [Node.js docs](https://nodejs.org/api/packages.html#description) for more information.

## [Related Rules](#related-rules)

*   [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
*   [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
*   [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
*   [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## [How to fix](#how-to-fix)

Add the `description` field to the `package.json` file that explains what the package does and when it should be used.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_DUPLICATE_DEPENDENCIES"
description: "Found duplicate dependencies between the list of dependencies and devDependencies or peerDependencies in a package.json file.."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_DUPLICATE_DEPENDENCIES"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_DUPLICATE\_DEPENDENCIES

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Packages that are listed in the `dependencies` section of `package.json` should not be listed in `devDependencies` or `peerDependencies`. A package in the `dependencies` section says that the package are required for the functionality of your workspace, in which case there is no reason to also list it in `devDependencies` or `peerDependencies`.

## [Example](#example)

This `package.json` file would cause the check to fail:

package.json

```
{
  "name": "workspace",
  "dependencies": {
    "@next/mdx": "13.1.5"
  },
  "devDependencies": {
    "@next/mdx": "13.1.5"
  }
}
```

## [How to fix](#how-to-fix)

If the package is needed to use the package from your workspace, you can remove the package from the `devDependencies` and `peerDependencies` sections. If the package is only needed for development of your workspace or if the package is only needed to express version compatibility requirements and it is not needed for the functionality of your workspace when people use your package, then it can be left in `devDependencies` or `peerDependencies` and be removed from `dependencies`.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_NAME_REQUIRED"
description: "Requires that every package.json file has the name field set to ensure each workspace has a unique identifier."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_NAME\_REQUIRED

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that every `package.json` has a `name` field. This field is important because it used to identify the workspace in the monorepo.

See the [Node.js docs](https://nodejs.org/api/packages.html#name) for more information.

## [Related Rules](#related-rules)

*   [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
*   [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
*   [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
*   [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## [How to fix](#how-to-fix)

Add the `name` field to the `package.json` file that contains a unique name for this package. The name should be understandable by someone viewing or using the package as to what it does.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_PRIVATE_REQUIRED"
description: "Requires that every package.json file has the private field set to prevent accidental publishing to npm."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_PRIVATE\_REQUIRED

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that every `package.json` has the `private` field set to true or false. This field ensures that the workspace is not accidentally published to npm. In a monorepo, this should be the default to prevent packages from being accidentally published and can be explicitly set to `false` to indicate that the package can be published.

## [Related Rules](#related-rules)

*   [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
*   [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
*   [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)
*   [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## [How to fix](#how-to-fix)

Packages should set `private` to `true` unless the package is intended to be published in which case it can be explicitly set to `false`.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_PRIVATE_REQUIREDPACKAGE_JSON_SIDE_EFFECTS_REQUIRED"
description: "Requires that every package.json file has the sideEffects field set to ensure tree-shaking works optimally."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_PRIVATE\_REQUIREDPACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that every `package.json` has a `sideEffects` field. The `sideEffects` field is required for shared packages. This field helps bundlers make assumptions about packages that improve tree shaking, or pruning files that aren't used and don't have any global side effects.

See [https://webpack.js.org/guides/tree-shaking/](https://webpack.js.org/guides/tree-shaking/) for more information.

## [Related Rules](#related-rules)

*   [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
*   [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
*   [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
*   [PACKAGE\_JSON\_TYPE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED)

## [How to fix](#how-to-fix)

The `sideEffects` field should be set to `false` unless the code in that workspace has global side effects, in which case it should be set to `true` or an array of glob patterns for files that do have side effects.

--------------------------------------------------------------------------------
title: "PACKAGE_JSON_TYPE_REQUIRED"
description: "Requires that every package.json file has the type field set to encourage using ES Modules since commonjs is the default."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_JSON_TYPE_REQUIRED"
--------------------------------------------------------------------------------

# PACKAGE\_JSON\_TYPE\_REQUIRED

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that every `package.json` has a `type` field. This field determines how files within the workspace are treated by default. Files are treated as [CommonJS](https://nodejs.org/api/modules.html) by default. However, the new recommendation is to use [ES Modules](https://nodejs.org/api/esm.html).

This field is required so that packages explicitly choose which module format to use, preferring ES Modules when possible.

See the [Node.js docs](https://nodejs.org/api/packages.html#type) for more information.

## [Related Rules](#related-rules)

*   [PACKAGE\_JSON\_NAME\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_NAME_REQUIRED)
*   [PACKAGE\_JSON\_DESCRIPTION\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_DESCRIPTION_REQUIRED)
*   [PACKAGE\_JSON\_PRIVATE\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_PRIVATE_REQUIRED)
*   [PACKAGE\_JSON\_SIDE\_EFFECTS\_REQUIRED](/docs/conformance/rules/PACKAGE_JSON_SIDE_EFFECTS_REQUIRED)

## [How to fix](#how-to-fix)

The `type` field should be set to `module` when possible, although there are still situations where `commonjs` has to be used.

--------------------------------------------------------------------------------
title: "PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS"
description: "Circular imports between two files are not allowed."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_CIRCULAR_IMPORTS"
--------------------------------------------------------------------------------

# PACKAGE\_MANAGEMENT\_NO\_CIRCULAR\_IMPORTS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This check ensures that there is no path through import statements back to the original file. This helps to keep dependencies between files clean, which aids in dependency analysis and refactoring.

## [Example](#example)

component-a.ts

```
import Badge from './component-b';
 
export function withHigherOrderComponent({ children }) {
  return <div>{children}</div>;
}
 
export function Page() {
  return (
    <div>
      <Badge />
    </div>
  );
}
```

component-b.ts

```
import { withHigherOrderComponent } from './component-a';
 
function Badge() {
  return <div>Badge</div>;
}
 
export default withHigherOrderComponent(Badge);
```

## [How to fix](#how-to-fix)

The exports in the file that has a circular import should be refactored so that the circular import doesn't exist anymore. This might be fixed by moving some of the exports in a file to a separate file so that the imports don't cause a circular import. In some cases, it may be necessary to refactor the code to avoid the circular import.

--------------------------------------------------------------------------------
title: "PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS"
description: "Import statements that can not be resolved to a local file or a package from package.json dependencies are not allowed."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_NO_UNRESOLVED_IMPORTS"
--------------------------------------------------------------------------------

# PACKAGE\_MANAGEMENT\_NO\_UNRESOLVED\_IMPORTS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

All imports must be able to be resolved to a file local to the workspace or a package declared as a dependency within the `package.json` file. This ensures that the workspace has not missed any dependencies and is not relying on global dependencies.

## [Example](#example)

component.ts

```
import { useState } from 'react';
import { useRouter } from 'next/router';
```

The `package.json` is missing a dependency on the `next` package.

package.json

```
{
  "name": "shared-component-pkg",
  "dependencies": {
    "react": "19.0.0-beta-4508873393-20240430"
  }
}
```

## [How to fix](#how-to-fix)

If the workspace is missing a package dependency, add the appropriate one to the `package.json` file of the workspace. In the example above, a dependency on the `next` package should be added.

--------------------------------------------------------------------------------
title: "PACKAGE_MANAGEMENT_REQUIRED_README"
description: "Every workspace is required to have a README.md file in the root of the workspace."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/PACKAGE_MANAGEMENT_REQUIRED_README"
--------------------------------------------------------------------------------

# PACKAGE\_MANAGEMENT\_REQUIRED\_README

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

A `README.md` file helps orient readers to the purpose of a workspace and instructions how to use it, which makes it straightforward for people browsing the code to understand its purpose, whether they should use it, and how to make changes to the code.

## [How to fix](#how-to-fix)

Add a `README.md` file in the workspace directory. This file can contain a description of the package, and any instructions for developers or users to build or use the package.

--------------------------------------------------------------------------------
title: "REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS"
description: "Prevent static imports that are referenced only in React event handlers from being eagerly loaded in React components."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS"
--------------------------------------------------------------------------------

# REACT\_NO\_STATIC\_IMPORTS\_IN\_EVENT\_HANDLERS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule has been deprecated as of version [1.8.0](/docs/conformance/changelog#1.8.0)and will be removed in 2.0.0.

React event handlers are async, and as such, this means we can defer loading the associated code until we interact with the UI, triggering that event handler. Specifically, this means we can improve initial code size and the overhead of loading the code until it is actually needed.

## [How to fix](#how-to-fix)

Instead of using static imports at the top of your module, you can use dynamic imports as needed in your React event handlers.

Before:

```
import foo from 'foo';
 
const onClick = () => {
  foo.doSomething();
};
```

After:

```
const onClick = () => {
  import('foo').then((foo) => {
    foo.doSomething();
  });
};
```

Additionally, you can [configure](/docs/conformance/customize) the rule for only specific React event handlers:

```
"REACT_NO_STATIC_IMPORTS_IN_EVENT_HANDLERS": {
  eventAllowList: ['onClick'],
}
```

--------------------------------------------------------------------------------
title: "REACT_STABLE_CONTEXT_PROVIDER_VALUE"
description: "Prevent non-stable values from being used in React Context providers that could cause unnecessary re-renders."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REACT_STABLE_CONTEXT_PROVIDER_VALUE"
--------------------------------------------------------------------------------

# REACT\_STABLE\_CONTEXT\_PROVIDER\_VALUE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

When non-stable values (i.e. object identities) are used as the `value` prop for `Context.Provider`, React will trigger cascading updates to all components that use this context value on each render, causing needless re-renders (affecting application performance) or causing unintended consequences that may negatively affect the user-experience.

## [Examples](#examples)

Examples of incorrect code for this rule:

```
return <SomeContext.Provider value={{ foo: 'bar' }}>...</SomeContext.Provider>;
```

Examples of correct code for this rule:

```
const foo = useMemo(() => ({ foo: 'bar' }), []);
 
return <SomeContext.Provider value={foo}>...</SomeContext.Provider>;
```

## [How to fix](#how-to-fix)

One way to fix this issue may be to wrap the value in a `useMemo()`. If the value is a function then `useCallback()` can be used as well. See the above examples for a reference on how you might fix this by wrapping with `useMemo`.

--------------------------------------------------------------------------------
title: "REQUIRE_CARET_DEPENDENCIES"
description: "Prevent the use of dependencies without a caret ("^") as a prefix."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_CARET_DEPENDENCIES"
--------------------------------------------------------------------------------

# REQUIRE\_CARET\_DEPENDENCIES

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.4.0.

Using a caret ("^") as a prefix in the version of your dependencies is recommended. [Caret Ranges](https://github.com/npm/node-semver?tab=readme-ov-file#caret-ranges-123-025-004) allows patch and minor updates for versions 1.0.0 and above, patch updates for versions 0.X >=0.1.0, and no updates for versions 0.0.X. This rule is applicable to `"dependencies"` and `"devDependencies"`, and it helps maintain the security and health of your codebase.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

## [Examples](#examples)

This rule will catch any `package.json` files:

*   Using `~` or `*` as a prefix of the version, like `~1.0.0`.
*   Version without a prefix, such as `1.0.0`.

package.json

```
{
  "dependencies": {
    "chalk": "~5.3.0",
    "ms": "*2.1.3",
  },
  "devDependencies": {
    "semver": "7.6.0"
  },
}
```

## [How to fix](#how-to-fix)

If you hit this issue, you can resolve it by adding a `"^"` to the version of your dependency. If you want to keep using a pinned version, or another prefix, you can include the dependency in the [Allowlist](https://vercel.com/docs/conformance/allowlist).

package.json

```
{
  "dependencies": {
    "semver": "^7.6.0"
  },
}
```

--------------------------------------------------------------------------------
title: "REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS"
description: "Requires that all exported functions have JSDoc comments."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_DOCS_ON_EXPORTED_FUNCTIONS"
--------------------------------------------------------------------------------

# REQUIRE\_DOCS\_ON\_EXPORTED\_FUNCTIONS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.8.0.

Adding JSDoc to exported functions helps engineers to quickly understand the purpose and application of those functions when reviewing or using them.

This is particularly important in packages where the source code may be minified and/or obfuscated, and can save users time by avoiding the need to find usage information in external documentation.

For more information on JSDoc, see [Getting started with JSDoc](https://jsdoc.app/about-getting-started).

Additionally, for non-TypeScript projects, JSDoc can be used to declare type information for function parameters and return values. For packages, these declarations can provide type information for both JavaScript and TypeScript consumers.

## [Examples](#examples)

The below function is a minimal example of a function that would be caught by this rule.

```
export function appendWorld(str: string): string {
  return str + ' world';
}
```

This rule will also catch references within the same file, and different ways of declaring functions. For example:

```
const appendWorld = function (str: string): string {
  return str + ' world';
};
 
export default appendWorld;
```

This rule non-function exports and re-exports of functions.

## [How to fix](#how-to-fix)

To resolve this issue, add a JSDoc comment to the exported function.

```
/**
 * Modifies a string by appending `' world'` to it.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

You can add additional information to the JSDoc comment, such as descriptions of the function's parameters and return value.

```
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param str - The string to modify.
 * @returns The modified string.
 */
export function appendWorld(str: string): string {
  return str + ' world';
}
```

The example above doesn't provide type information in the JSDoc comment, as this information is already provided by the function signature. When working without TypeScript, you can also provide this information using JSDoc.

```
/**
 * Modifies a string by appending `' world'` to it.
 *
 * @param {string} str - The string to modify.
 * @returns {string} The modified string.
 */
export function appendWorld(str) {
  return str + ' world';
}
```

--------------------------------------------------------------------------------
title: "REQUIRE_NODE_VERSION_FILE"
description: "Requires that workspaces have a valid Node.js version file (`.node-version` or `.nvmrc`) file defined."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_NODE_VERSION_FILE"
--------------------------------------------------------------------------------

# REQUIRE\_NODE\_VERSION\_FILE

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

This rule is available from version 1.2.0.

Using a Node.js version file (`.node-version` or `.nvmrc`) ensures that all developers and tooling (e.g., CI systems) use the same version of Node.js. This practice helps to avoid inconsistencies between environments and can even prevent bugs from being shipped to production.

As another benefit, committing a Node.js version file improves developer experience, as many Node.js version management tools can automatically detect and use the version defined in the file. This includes [GitHub Actions](https://docs.github.com/en/actions), and popular Node.js version managers such as [`fnm`](https://github.com/Schniz/fnm) and [`nvm`](https://github.com/nvm-sh/nvm).

This rule also validates to ensure that the version in the file is defined in a way that is compatible with common tooling.

By default, this rule is disabled. To enable it, refer to [customizing Conformance](/docs/conformance/customize).

## [How to fix](#how-to-fix)

If you hit this issue, you can resolve it by adding a Node.js version file at the root of your workspace.

The example `.node-version` file below requires that Node.js `20.9` is used in the workspace, allowing for any patch version (i.e. `20.9.1`). The level of strictness can be adjusted based on your teams needs.

.node-version

```
v20.9
```

--------------------------------------------------------------------------------
title: "REQUIRE_ONE_VERSION_POLICY"
description: "Requires all dependencies in a monorepo to have the same version policy."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/REQUIRE_ONE_VERSION_POLICY"
--------------------------------------------------------------------------------

# REQUIRE\_ONE\_VERSION\_POLICY

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Dependency mismatch is a common and easily preventable problem. When there are multiple versions of a single dependency, not only is there additional complexity in maintaining different versions of that dependency, there are also code size complications with bundling. Having multiple versions of a given dependency will likely result in bloated code size as each dependency version will need to be bundled independently. Having multiple versions might also leave developers confused and lead to possible security implications.

Additionally – keeping versions consistent reduces the possibility of type mismatches across the monorepo.

By default, this rule is disabled. Enable it by [customizing Conformance](/docs/conformance/customize).

## [How to fix](#how-to-fix)

Ensure all `package.json` files in your monorepo that have a `dependency` are aligned to all have the same version. Version ranges are not always reliable, so it's recommended that you pin all versions to the same given version to ensure consistency.

## [Exceptions](#exceptions)

Sometimes it is useful to temporarily have two or more versions of a dependency whilst incrementally migrating a monorepo to having the same version policy. In which case, it's acceptable to allowlist this rule on specific parts of the codebase using by [customizing Conformance](/docs/conformance/customize) until all packages have been successfully migrated.

--------------------------------------------------------------------------------
title: "SET_COOKIE_VALIDATION"
description: "Prevents usage of cookies that do not conform to the allowed cookie policy."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/SET_COOKIE_VALIDATION"
--------------------------------------------------------------------------------

# SET\_COOKIE\_VALIDATION

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

It's a good practice to enforce a cookie policy across a workspace to ensure only certain cookies are allowed to be set.

## [How to fix](#how-to-fix)

Engineers should reach out to the appropriate engineer(s) or team(s) for a review of the defined cookie and request the cookie name be added to the allowed cookie policy list. This can be set in the `conformance.config.jsonc` configuration file as follows:

conformance.config.jsonc

```
"SET_COOKIE_VALIDATION": {
  "cookieAllowList": ["some-cookie-name"]
}
```

--------------------------------------------------------------------------------
title: "TESTS_NO_CONDITIONAL_ASSERTIONS"
description: "Requires that assertions are not conditional, or that expect.assertions is used."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/TESTS_NO_CONDITIONAL_ASSERTIONS"
--------------------------------------------------------------------------------

# TESTS\_NO\_CONDITIONAL\_ASSERTIONS

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

When possible, conditional test assertions should be avoided as they can lead to false test passes if and when conditions are not evaluated as expected.

If you can't avoid using a condition in your test, you can satisfy this rule by using an `expect.assertions` statement.

## [Example](#example)

In this abstract example, there are two potential points of failure:

1.  The button could throw a ButtonError during `render(Button)`, causing the first (`try`) assertion to be skipped.
2.  The `throwError()` function could fail to throw, causing the second (`catch`) assertion to be skipped.

src/button/button.test.ts

```
describe('button', () => {
  it('should render', () => {
    try {
      const button = render(Button);
      expect(button).not.toBe(null);
      button.throwAnError();
    } catch (error) {
      expect(error).toBeInstanceOf(ButtonError);
    }
  });
});
```

## [How to fix](#how-to-fix)

There are two ways to resolve this error:

1.  Refactor the test code to ensure that assertions are no longer conditional.
2.  Use `expect.assertions` to inform the test runner that it should fail if the required number of assertions were not called during the test.

Taking our previous example, we can apply the second fix:

src/button/button.test.ts

```
describe('button', () => {
  it('should render', () => {
    try {
      const button = render(Button);
      expect(button).not.toBe(null);
      button.throwAnError();
    } catch (error) {
      expect(error).toBeInstanceOf(ButtonError);
    }
    expect.assertions(2);
  });
});
```

### [Using `expect.assertions`](#using-expect.assertions)

Most test frameworks and runners support `expect.assertions`, and this is the preferred approach to resolving this error if you can't refactor your test code.

To satisfy this rule, the test must not conditionally call `expect.assertions`. This rule doesn't count or report on the number of assertions.

### [What to do when you can't use `expect.assertions`](#what-to-do-when-you-can't-use-expect.assertions)

There may be cases where you can't use `expect.assertions` (i.e. your test framework or runner doesn't support it), and refactoring the test code is not a viable solution. In those cases, you have the following options:

1.  You can use allowlists to allow individual violations (see: [Conformance Allowlists](/docs/conformance/allowlist)).
2.  You can disable this test (see: [Customizing Conformance](/docs/conformance/customize)).

## [Customization](#customization)

The default pattern matches the default patterns for Jest and Vitest, however you can provide your own patterns through the `paths` property.

The default configuration is:

conformance.config.jsonc

```
{
  "configuration": [
    "testPatterns": ["**/unit-tests/**/*.{js,jsx}"]
  ]
}
```

--------------------------------------------------------------------------------
title: "TESTS_NO_ONLY"
description: "Requires that focused tests (i.e. it.only()) are unfocused."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/TESTS_NO_ONLY"
--------------------------------------------------------------------------------

# TESTS\_NO\_ONLY

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Focusing tests can help to write and debug test suites, but focused tests should be unfocused before committing changes.

This rule disallows focused tests so that they can't be committed without an allowlist entry.

## [Example](#example)

src/button/button.test.ts

```
describe('button', () => {
  it.only('should render', () => {
    // ...
  });
});
```

Note that the following patterns (and variants of these patterns) will be reported as errors by this test. These should cover popular test frameworks and runners, including:

*   [`jest`](https://jestjs.io/)
*   [`node:test`](https://nodejs.org/api/test.html#test-runner)
*   [`vitest`](https://vitest.dev/)
*   [`cypress`](https://www.cypress.io/)
*   [`@playwright/test`](https://playwright.dev/docs/api/class-test)

```
// Most test frameworks and runners
describe.only(/* ... */);
it.concurrent.only(/* ... */);
test.only.each([])(/* ... */);
// Jest - supported in addition to the above
fdescribe(/* ... */);
fit.each([])(/* ... */);
ftest(/* ... */);
```

## [How to fix](#how-to-fix)

This error will be resolved when debugging is complete and the test has been unfocused.

## [Customization](#customization)

The default pattern matches the default patterns for Jest and Vitest, however you can provide your own patterns through the `paths` property.

The default configuration is:

conformance.config.jsonc

```
{
  "configuration": [
    "testPatterns": ["**/unit-tests/**/*.{js,jsx}"]
  ]
}
```

--------------------------------------------------------------------------------
title: "TYPESCRIPT_CONFIGURATION"
description: "Requires that a workspace package that uses TypeScript files has configured TypeScript correctly for that workspace."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/TYPESCRIPT_CONFIGURATION"
--------------------------------------------------------------------------------

# TYPESCRIPT\_CONFIGURATION

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Using TypeScript in a workspace requires a few items to be set up correctly:

*   There should be a `tsconfig.json` file at the root of the workspace.
*   The `tsconfig.json` should extend from the repo's shared `tsconfig.json` file.
*   The `tsconfig.json` file should specify a `tsBuildInfoFile` to speed up incremental compilation.
*   The `tsconfig.json` file should have certain compiler options set for improved type safety.
*   The workspace should have a `type-check` command that runs the TypeScript compiler to check for type issues.

These changes will ensure that the TypeScript compiler picks up the right compiler settings for the project and that the TypeScript type checking will run when the `type-check` command is run for the entire repository.

## [Example](#example)

```
Conformance errors found!
 
A Conformance error occurred in test "TYPESCRIPT_CONFIGURATION".
 
package.json in "docs" should have a "type-check" script that runs TypeScript type checking.
 
To find out more information and how to fix this error, visit
/docs/conformance/rules/TYPESCRIPT_CONFIGURATION.
 
If this violation should be ignored, add the following entry to
/apps/docs/.allowlists/TYPESCRIPT_CONFIGURATION.allowlist.json
and get approval from the appropriate person.
 
{
  "testName": "TYPESCRIPT_CONFIGURATION",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "workspace": "docs"
  }
}
```

## [How To Fix](#how-to-fix)

The shared `tsconfig.json` should have at least the following defined:

tsconfig.json

```
{
  "compilerOptions": {
    "incremental": true,
    "noUncheckedIndexedAccess": true,
    "strict": true
  }
}
```

For other configuration issues, the project's `tsconfig.json` may need to be updated. Most files that don't require customization should look like:

tsconfig.json

```
{
  "extends": "your_shared_tsconfig/base.json",
  "exclude": ["dist", "node_modules"],
  "compilerOptions": {
    "tsBuildInfoFile": "node_modules/.cache/tsbuildinfo.json"
  }
}
```

Additionally, the project's `package.json` file may need to be updated. A `type-check` command needs to be added to the `scripts` section:

package.json

```
{
  "scripts": {
    ...,
    "type-check": "tsc -p tsconfig.json --noEmit"
  }
}
```

The dependency on the repository's shared TypeScript must also exist:

```
{
  "devDependencies": {
    "your_shared_tsconfig": "workspace:*"
  }
}
```

--------------------------------------------------------------------------------
title: "TYPESCRIPT_ONLY"
description: "Requires that a workspace package may only contain TypeScript files and no JavaScript or JSX files."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/TYPESCRIPT_ONLY"
--------------------------------------------------------------------------------

# TYPESCRIPT\_ONLY

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

[TypeScript](https://typescriptlang.org) is a superset of JavaScript that adds optional static typing. Using TypeScript in your codebase provides the following benefits:

*   Type Safety: TypeScript is a strongly-typed language, which means that it allows you to catch errors at compile-time rather than at runtime. This can help you catch bugs earlier in the development process, making your code more reliable and easier to maintain over time.
*   Tooling: TypeScript has excellent tooling support, including autocompletion, type checking, and refactoring tools. This can help you write code faster and with fewer errors.
*   JavaScript Compatibility: TypeScript is a superset of JavaScript, which means that any valid JavaScript code is also valid TypeScript code. This means that you can gradually introduce TypeScript into your project without having to rewrite your entire codebase.
*   Scalability: TypeScript is designed to work well with large-scale applications. With features like interfaces and classes, it allows you to write code that is easier to read and maintain, even as your project grows in complexity.

## [Example](#example)

```
Conformance errors found!
 
A Conformance error occurred in test "TYPESCRIPT_ONLY".
 
JavaScript files are not allowed. Please convert the file to TypeScript.
 
To find out more information and how to fix this error, visit
/docs/conformance/rules/TYPESCRIPT_ONLY.
 
If this violation should be ignored, add the following entry to
/apps/docs/.allowlists/TYPESCRIPT_ONLY.allowlist.json
and get approval from the appropriate person.
 
{
  "testName": "TYPESCRIPT_ONLY",
  "reason": "TODO: Add reason why this violation is allowed to be ignored.",
  "location": {
    "filePath": "apps/docs/src/add-numbers.js"
  }
}
```

## [How To Fix](#how-to-fix)

To fix this error, you must convert the JavaScript file to TypeScript. You can do this by changing the file extension from `.js` to `.ts` or `.jsx` to `.tsx` and adding the appropriate type annotations.

diff

```
--- a/apps/docs/src/add-numbers.js
+++ b/apps/docs/src/add-numbers.ts
-export function addNumbers(a, b) {
+export function addNumbers(a: number, b: number): number {
  return a + b;
}
```

## [Customization](#customization)

The check supports custom file globs and ignore file globs that can be specified on `conformance.config.jsonc`. The globs take effect from the root of the workspace package.

conformance.config.jsonc

```
{
  "rules": {
    "TYPESCRIPT_ONLY": {
      "files": ["**/*.js", "**/*.jsx"],
      "ignoreFiles": ["**/*.custom-config.js"]
    }
  }
}
```

The default configuration is:

conformance.config.jsonc

```
{
  "rules": {
    "TYPESCRIPT_ONLY": {
      "files": ["**/*.{cjs,mjs,js,jsx}"],
      "ignoreFiles": [
        "dist/**",
        "node_modules/**",
        ".next/**", // Next.js output
        ".eslintrc.{cjs,js}", // Common ESLint config file name
        "*.config.{cjs,mjs,js}", // Common config file name
        "*.setup.{cjs,mjs,js}", // Common setup file name
      ],
    },
  },
}
```

--------------------------------------------------------------------------------
title: "WORKSPACE_MISSING_CONFORMANCE_SCRIPT"
description: "All packages must define a conformance script that invokes the Conformance package."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/WORKSPACE_MISSING_CONFORMANCE_SCRIPT"
--------------------------------------------------------------------------------

# WORKSPACE\_MISSING\_CONFORMANCE\_SCRIPT

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

Conformance requires a script to exist in every workspace in the repository. This makes sure that Conformance rules are running on all code. This test throws an error if a workspace does not define a `conformance` script in the `package.json` file.

## [Example](#example)

A workspace contains a `package.json` file that looks like:

package.json

```
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b"
  }
}
```

It does not contain a `conformance` script, so this check will fail.

## [How to fix](#how-to-fix)

Install the `@vercel-private/conformance` package in this workspace and define a `conformance` script in the `package.json` file.

package.json

```
{
  "name": "test-workspace",
  "scripts": {
    "build": "tsc -b",
    "conformance": "vercel conformance"
  },
  "devDependencies": {
    "@vercel-private/conformance": "^1.0.0"
  }
}
```

--------------------------------------------------------------------------------
title: "WORKSPACE_MISSING_PACKAGE_JSON"
description: "All directories that match a workspace glob must include a package.json file."
last_updated: "null"
source: "https://vercel.com/docs/conformance/rules/WORKSPACE_MISSING_PACKAGE_JSON"
--------------------------------------------------------------------------------

# WORKSPACE\_MISSING\_PACKAGE\_JSON

Copy page

Ask AI about this page

Last updated March 4, 2025

Conformance is available on [Enterprise plans](/docs/plans/enterprise)

All directories that match a glob used to configure package manager workspaces must be defined as a package and contain a `package.json` file. This check prevents confusion where a new directory may be placed within a directory that is configured to be a workspace but the new directory is not actually a workspace.

## [Example](#example)

The repository configures pnpm workspaces in this file:

pnpm-workspace.yaml

```
packages:
  - 'apps/*'
  - 'packages/*'
```

If a directory is defined in `packages/not-a-package`, then this test will fail saying that the `not-a-package` directory must contain a `package.json` file.

## [How to fix](#how-to-fix)

Directories that match a workspace glob but do not have a `package.json` file should either be converted to a package, be moved to a different directory, or be excluded in the workspaces configuration.

--------------------------------------------------------------------------------
title: "Connectivity"
description: "Connect your Vercel projects to backend services with static IPs and secure networking options."
last_updated: "null"
source: "https://vercel.com/docs/connectivity"
--------------------------------------------------------------------------------

# Connectivity

Copy page

Ask AI about this page

Last updated October 2, 2025

Connect your projects to backend services that require IP allowlisting or private network access.

## [Static IPs (shared pool)](#static-ips-shared-pool)

When your database or API needs to see traffic from known IP addresses, Static IPs give you shared static egress IPs that won't change. Perfect for Pro and Enterprise teams who need IP allowlisting without the complexity.

*   Use case: IP allowlisting for databases, APIs, and legacy systems
*   Network: Shared VPC with subnet-level isolation
*   [Pricing](/docs/connectivity/static-ips#pricing): $100/month per project + $0.15/GB Private Data Transfer

[Learn more about Static IPs](/docs/connectivity/static-ips)

## [Secure Compute](#secure-compute)

For when you need your own private Virtual Private Cloud (VPC). Secure Compute gives you dedicated networks with VPC peering — your infrastructure stays completely isolated from other customers.

*   Use case: Full network isolation and VPC peering
*   Network: Dedicated VPC per customer

[Learn more about Secure Compute](/docs/connectivity/secure-compute)

## [Pricing](#pricing)

Both connectivity options are billed on Private Data Transfer priced regionally based on the [regional pricing documentation](/docs/pricing/regional-pricing).

| Feature | Static IPs (Pro) | Secure Compute (Enterprise) |
| --- | --- | --- |
| Monthly cost | $100/month per project | Custom |
| Private Data Transfer | [Regional pricing](/docs/pricing/regional-pricing) | Custom |
| Network isolation | Shared VPC with subnet-level isolation | Dedicated VPC and subnet per customer |

### [Understanding data transfer costs](#understanding-data-transfer-costs)

Data transfer costs kick in for all outbound traffic from your Vercel Functions to external services:

*   Database queries and responses
*   API calls to third-party services
*   File uploads and downloads
*   Any other outbound network traffic

Keep tabs on your usage in the Team Settings Usage tab under the Private Data Transfer section.

--------------------------------------------------------------------------------
title: "Secure Compute"
description: "Secure Compute provides dedicated private networks with VPC peering for Enterprise teams."
last_updated: "null"
source: "https://vercel.com/docs/connectivity/secure-compute"
--------------------------------------------------------------------------------

# Secure Compute

Copy page

Ask AI about this page

Last updated October 2, 2025

Secure Compute is available for purchase on [Enterprise plans](/docs/plans/enterprise)

Secure Compute creates private connections between your [Vercel Functions](/docs/functions) and your backend infrastructure like databases, APIs, or any private services you're running.

By default, Vercel deployments can come from [any IP address](/guides/how-to-allowlist-deployment-ip-address). Secure Compute gives you dedicated static IPs, so you can tighten your backend's access controls to only allow traffic from your specific Vercel infrastructure.

When you enable Secure Compute on your [project](/docs/projects), your deployments and build container get their own [dedicated network with static IP addresses](#secure-compute-networks-and-dedicated-ip-addresses) in a [region you choose](#specific-region). Your traffic stays completely separate from other customers.

## [How Secure Compute works](#how-secure-compute-works)

Here's what you get with Secure Compute:

*   Your own dedicated private network inside a VPC
*   Static IPs that won't change, plus a NAT Gateway
*   Complete isolation — only your specified resources can reach your Vercel Functions

## [Enabling Secure Compute](#enabling-secure-compute)

When you request access to Secure Compute, tell us your AWS region and optionally a CIDR block. We'll set up a Secure Compute network in that region with:

*   A pair of dedicated IP addresses
*   AWS account ID
*   AWS region based on your request
*   AWS VPC ID
*   CIDR block based on your request

![Secure Compute network settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fprivate-network-light.png&w=2048&q=75)![Secure Compute network settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fprivate-network-dark.png&w=2048&q=75)

Secure Compute network settings.

When you enable Secure Compute on a project, Vercel attaches your project's [build container](/docs/builds) and subsequent deployment inside a Secure Compute network with a specific IP address pair ([dedicated IP](#secure-compute-networks-and-dedicated-ip-addresses)). You can choose to [exclude the build container](#managing-the-build-container) from the private network.

## [Secure Compute networks and dedicated IP addresses](#secure-compute-networks-and-dedicated-ip-addresses)

Each private network has its own dedicated IP pair and is isolated from others, ensuring no sharing across teams. You can assign multiple projects to a Secure Compute network, but each project belongs to only one active and one passive network.

Need more networks for the same team? Hit the [Contact Sales](/contact/sales) button on the Connectivity page of your dashboard.

Once your IP pair is ready, add it to your backend's access control list. You'll still need to use a username/password or authentication key on top of the IP filtering — the IPs alone aren't enough.

## [Specific region](#specific-region)

When you request Secure Compute access, we'll create one network in your chosen [Vercel Function region](/docs/functions/configuring-functions/region). For the best performance, pick the same [region](/docs/functions/configuring-functions/region) where your backend runs.

Vercel applies Secure Compute to [Vercel Functions](/docs/functions) using the following runtimes:

*   [Node.js](/docs/functions/runtimes/node-js)
*   [Ruby](/docs/functions/runtimes/ruby)
*   [Go RuntimeGo](/docs/functions/runtimes/go)
*   [Python](/docs/functions/runtimes/python)

The [Edge Runtime](/docs/functions/runtimes/edge) is not supported meaning features like [Routing Middleware](/docs/routing-middleware) and Vercel Functions using the [`edge` runtime](/docs/functions/runtimes/edge) will not use the provided dedicated IP addresses.

### [Region failover](#region-failover)

For your failover region to use Secure Compute, you need to [contact sales](/contact/sales) to create an additional Secure Compute network in that region. Once created, you can connect a project to that network and enable passive failover.

When you enable passive failover, Vercel will automatically switch to the failover region if the primary region is unavailable. This ensures that your Vercel Functions continue to operate even if the primary region is down.

## [Add a project to your Secure Compute network](#add-a-project-to-your-secure-compute-network)

To add a project to your Secure Compute network:

1.  Navigate to your project's Settings page, and open the Connectivity section.
2.  For every environment you want to connect to Secure Compute:
    *   Select an Active Network.
    *   Optionally select a Passive Network to enable passive failover.
    *   Optionally enable Builds to include the project's build container in the network.
3.  Click Save to persist your changes.

![Adding a project to a Secure Compute network. One environment at a time.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fsecure-compute-connect-envs-light.png&w=1920&q=75)![Adding a project to a Secure Compute network. One environment at a time.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fsecure-compute-connect-envs-dark.png&w=1920&q=75)

Adding a project to a Secure Compute network. One environment at a time.

To change multiple environments at once:

1.  Select the environments using checkboxes or use the checkbox in the table header to select all environments.
2.  Click Edit Selected.
3.  In bulk edit modal:
    *   Select an Active Network.
    *   Optionally select a Passive Network to enable passive failover.
    *   Optionally check Include Builds to include the project's build container in the network.
    *   Click Apply to modify the selected environments.
4.  Click Save to persist your changes.

![Adding a project to a Secure Compute network. Multiple environments at once.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fsecure-compute-connect-envs-bulk-light.png&w=1200&q=75)![Adding a project to a Secure Compute network. Multiple environments at once.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fsecure-compute-connect-envs-bulk-dark.png&w=1200&q=75)

Adding a project to a Secure Compute network. Multiple environments at once.

### [Managing the build container](#managing-the-build-container)

When you add a project to a Secure Compute network, you can choose to include the project's build container in the network. This is useful if your application calls your data sources at build time.

You can opt the [build container](/docs/builds) out of using the dedicated IP addresses. This is useful if your application only calls your data sources at run time and not at build time.

By opting out of including the build container, you will not incur the 5s delay when provisioning a secure build container.

To manage the build container during the [project connection](#add-a-project-to-your-secure-compute-network) process select Include Builds.

To manage the build container _after_ the project is connected to the Secure Compute network:

1.  Navigate to your team's Settings page, and open the Connectivity section.
2.  Select a private network from the list.
3.  Select the Projects tab.
4.  Click the icon to the right of your connected project and click Edit.
5.  Check/uncheck Include Builds to include/exclude the project's build container in the network.
6.  Click Save.

![Exclude your build from the private network.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fmanage-build-container-light.png&w=1920&q=75)![Exclude your build from the private network.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fmanage-build-container-dark.png&w=1920&q=75)

Exclude your build from the private network.

## [Multiple Secure Compute networks](#multiple-secure-compute-networks)

You can use one network with multiple projects in the same team. In this case, the same IP pair is shared across multiple projects.

If you require additional security or have a large team, you can have one network for each project so that each project will have its own dedicated IP pair.

Connecting a project to multiple networks across different regions is currently not supported. Each project environment can only be linked to a single active network within a single region. A passive network in a different region may only be used for failover.

## [VPC peering](#vpc-peering)

Virtual private cloud (VPC) peering is a method of connecting two VPCs in the same or different region. When you use Secure Compute, Vercel accepts a VPC peering connection between your Vercel Secure Compute network and your AWS VPC.

To set up VPC peering:

1.  Request Secure Compute: [Contact Vercel](/contact/sales) and supply your desired region, and optionally CIDR block. The CIDR blocks of Secure Compute network and your VPC must not overlap.
2.  Set up peering in AWS: In your AWS VPC dashboard, configure the peering connection by copying the values from your Secure Compute network settings, and pasting in the AWS VPC peering connection settings:
    *   Requester VPC ID: Your VPC ID
    *   Account ID: The AWS account ID
    *   Accepter VPC ID: Your Vercel Secure Compute network's VPC Peering ID
    *   Region: Your Vercel Secure Compute network's region
3.  Create peering connection: In the AWS VPC peering connection settings, click Create Peering Connection to establish the connection.
4.  Accept peering connection: Go back to your Vercel dashboard and click Accept to accept the connection.
5.  Update route tables: Go to AWS's VPC dashboard, select Route Tables, and configure routing to allow traffic from Vercel's CIDR block.

![Secure Compute VPC peering settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fvpc-connection-light.png&w=1920&q=75)![Secure Compute VPC peering settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecure-compute%2Fvpc-connection-dark.png&w=1920&q=75)

Secure Compute VPC peering settings.

The connection can be deleted from either the Vercel dashboard, or the AWS VPC dashboard.

## [VPN Support](#vpn-support)

If your current security and compliance obligations require more than dedicated IP addresses, contact us for guidance related to your specific needs.

## [Pricing](#pricing)

Secure Compute starts at $6.5K/year for Enterprise teams, plus Secure Connect Data Transfer at $0.15/GB.

### [Understanding data transfer costs](#understanding-data-transfer-costs)

Data transfer costs apply to all outbound traffic from your Vercel Functions to external services:

*   Database queries and responses
*   API calls to third-party services
*   File uploads and downloads
*   Any other outbound network traffic

Monitor your usage in the Team Settings Usage tab under the Secure Connect Data Transfer section.

## [Limits](#limits)

### [Build delay](#build-delay)

When connected to a Secure Compute network, builds experience up to a 5s delay as they provision a secure build container. When this happens, your build is marked as Provisioning Container in the dashboard.

### [Max number of VPC peering connections](#max-number-of-vpc-peering-connections)

The maximum number of VPC peering connections that can be established per network is 50.

--------------------------------------------------------------------------------
title: "Static IPs"
description: "Access IP-restricted backend services through shared static egress IPs for Pro and Enterprise teams."
last_updated: "null"
source: "https://vercel.com/docs/connectivity/static-ips"
--------------------------------------------------------------------------------

# Static IPs

Copy page

Ask AI about this page

Last updated October 30, 2025

Static IPs are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

With Static IPs (shared pool), you can access backend services that require IP allowlisting through static egress IPs. It's designed for Pro and Enterprise teams who need static IP functionality without the advanced networking or security features of [Secure Compute](/docs/connectivity/secure-compute).

## [When to use Static IPs](#when-to-use-static-ips)

*   Connect to databases such as Amazon RDS, Google Cloud SQL, Azure SQL, and MongoDB Atlas
*   Connect to APIs such as Auth0, PayPal, Stripe, internal corporate APIs
*   Connect to systems such as on-premises databases and services behind firewalls
*   Support compliance and business requirements

## [When not to use Static IPs](#when-not-to-use-static-ips)

Static IP is a service provided by Vercel that assigns a set of fixed outbound IP addresses used for egress traffic from your deployments. It does not assign a fixed public IP that external users or services can use to directly access or initiate inbound (ingress) traffic to your app. Therefore, Static IPs should not be used if you need your app to be reachable through a fixed inbound IP or require ingress traffic support, as inbound connections do not route through the Static IP service.

### [Static IPs or Secure Compute](#static-ips-or-secure-compute)

| Feature | Static IPs (Pro & Enterprise) | Secure Compute (Enterprise only) |
| --- | --- | --- |
| IP type | Static in shared Virtual Private Cloud (VPC) | Static in dedicated VPC |
| Network isolation | Shared VPC for a small group of customers with subnet-level isolation | Dedicated VPC and subnet per customer |
| Use cases | IP allowlisting, database access | IP allowlisting, VPC Peering, full isolation |
| Pricing | $100/month per project, plus Private Data Transfer at $0.15/GB | Custom pricing |

### [Static IPs with Secure Compute](#static-ips-with-secure-compute)

If your project uses [Secure Compute](/docs/connectivity/secure-compute) and you have enabled Static IPs, Static IPs will be ignored.

## [Getting started](#getting-started)

Read our [getting started guide](/docs/connectivity/static-ips/getting-started) to learn how to set up Static IPs.

## [How it works](#how-it-works)

When you enable Static IPs, you get:

*   Shared infrastructure: Each VPC serves a small group of customers
*   Static egress: All outbound traffic routes through shared static IP pairs
*   Logical isolation: Subnet-level isolation maintains security between customers on the same VPC
*   NAT gateway: Traffic exits through a managed NAT gateway for consistent IPs
*   Build traffic: Traffic from both deployed functions and builds will route through the static IPs

## [Managing your static IPs](#managing-your-static-ips)

### [Routing build traffic](#routing-build-traffic)

If your application calls data sources at build time, you can route its build traffic through your static IPs to keep your data sources secure.

To enable this, go to your [project's connectivity settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fconnectivity&title=Go+to+Connectivity+Settings):

1.  Go to your project's Settings
2.  Navigate to Connectivity
3.  Toggle Use Static IPs for builds under Static IPs

This setting is disabled by default. When enabled, both your project's build and deployed function traffic will route through static IPs and count as [Private Data Transfer](#pricing).

### [Routing Middleware support](#routing-middleware-support)

Static IPs (region-specific) don't apply to [middleware](/docs/routing-middleware) (which are deployed at the [edge](/docs/glossary#edge)).

### [Checking usage](#checking-usage)

1.  Go to your Team and click the Usage tab
2.  Scroll down to the Content, Caching & Optimization section. Static IPs data transfer is metered by Private Data Transfer
3.  Click Private Data Transfer for more detail about direction, regions, and projects

### [Static IPs with deployment environments](#static-ips-with-deployment-environments)

When you configure static IPs in a project, they apply to all the [environments](/docs/deployments/environments) set up in this project.

### [Regional considerations](#regional-considerations)

*   Choose regions close to your backend services to reduce latency
*   Each configured region has its own static IP pair

## [Limits and pricing](#limits-and-pricing)

### [Limits](#limits)

*   Static IP addresses are shared across a small group of customers in the same region
*   Project-level configuration: You cannot isolate static IPs to specific deployment environments

### [Pricing](#pricing)

Static IPs are priced at $100/month per project for Pro plus Private Data Transfer priced regionally based on [regional pricing documentation](/docs/pricing/regional-pricing).

--------------------------------------------------------------------------------
title: "Getting Started with Static IPs"
description: "Learn how to set up Static IPs for your Vercel projects to connect to IP-restricted backend services."
last_updated: "null"
source: "https://vercel.com/docs/connectivity/static-ips/getting-started"
--------------------------------------------------------------------------------

# Getting Started with Static IPs

Copy page

Ask AI about this page

Last updated October 2, 2025

Static IPs are available on [Enterprise](/docs/plans/enterprise) and [Pro](/docs/plans/pro) plans

This guide walks you through setting up Static IPs so you can access backend services that require IP allowlisting.

## [Prerequisites](#prerequisites)

Before you dive in, make sure you have:

*   A project deployed on Vercel
*   A backend service that supports IP allowlisting
*   [Pro](/docs/plans/pro-plan) or [Enterprise](/docs/plans/enterprise) plan

1.  ### [Access the Connectivity settings](#access-the-connectivity-settings)
    
    1.  Go to your Project Dashboard
    2.  Navigate to Project Settings
    3.  Click the Connectivity section
2.  ### [Configure your region](#configure-your-region)
    
    1.  Click Manage Active Regions
    2.  Pick a region close to your backend services to keep latency down. You can pick up to 3 regions
    3.  Your project gets assigned static IPs within a shared VPC for each configured region
3.  ### [Get your static IP addresses and configure your backend service](#get-your-static-ip-addresses-and-configure-your-backend-service)
    
    1.  Copy the static IP addresses from the dashboard
    2.  Add the static IPs to your backend service's allowlist so it knows which IP addresses are allowed to connect
4.  ### [Verify your connection](#verify-your-connection)
    
    To test your connection, redeploy your project that connects to your backend service. All your outbound traffic will now go through those static IPs and be routed via the static IPs.
    

## [Next steps](#next-steps)

*   Learn how to [monitor usage and billing](/docs/connectivity/static-ips#managing-your-static-ips) for your Static IPs
*   Understand [how Static IPs work](/docs/connectivity/static-ips#how-it-works)
*   Review [limits and pricing](/docs/connectivity/static-ips#limits-and-pricing)

--------------------------------------------------------------------------------
title: "Cron Jobs"
description: "Learn about cron jobs, how they work, and how to use them on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/cron-jobs"
--------------------------------------------------------------------------------

# Cron Jobs

Copy page

Ask AI about this page

Last updated June 25, 2025

Cron Jobs are available on [all plans](/docs/plans)

Cron jobs are time-based scheduling tools used to automate repetitive tasks. By using a specific syntax called a [cron expression](#cron-expressions), you can define the frequency and timing of each task. This helps improve efficiency and ensures that important processes are performed consistently.

Some common use cases of cron jobs are:

*   Automating backups and archiving them
*   Sending email and Slack notifications
*   Updating Stripe subscription quantities

Vercel supports cron jobs for [Vercel Functions](/docs/functions). Cron jobs can be added through [`vercel.json`](/docs/project-configuration) or the [Build Output API](/docs/build-output-api/v3/configuration#crons).

See [Managing Cron Jobs](/docs/cron-jobs/manage-cron-jobs) for information on duration, error handling, deployments, concurrency control, and local execution. To learn about usage limits and pricing information, see the [Usage and Pricing](/docs/cron-jobs/usage-and-pricing) page.

## [Getting started with cron jobs](#getting-started-with-cron-jobs)

Learn how to set up and configure cron jobs for your project using our [Quickstart](/docs/cron-jobs/quickstart) guide.

## [How cron jobs work](#how-cron-jobs-work)

To trigger a cron job, Vercel makes an HTTP GET request to your project's production deployment URL, using the `path` provided in your project's `vercel.json` file. An example endpoint Vercel would make a request to in order to trigger a cron job might be: `https://*.vercel.app/api/cron`.

Vercel Functions triggered by a cron job on Vercel will always contain `vercel-cron/1.0` as the user agent.

## [Cron expressions](#cron-expressions)

Vercel supports the following cron expressions format:

| Field | Value Range | Example Expression | Description |
| --- | --- | --- | --- |
| Minute | 0 - 59 | `5 * * * *` | Triggers at 5 minutes past the hour |
| Hour | 0 - 23 | `* 5 * * *` | Triggers every minute, between 05:00 AM and 05:59 AM |
| Day of Month | 1 - 31 | `* * 5 * *` | Triggers every minute, on day 5 of the month |
| Month | 1 - 12 | `* * * 5 *` | Triggers every minute, only in May |
| Day of Week | 0 - 6 (Sun-Sat) | `* * * * 5` | Triggers every minute, only on Friday |

### [Validate cron expressions](#validate-cron-expressions)

To validate your cron expressions, you can use the following tool to quickly verify the syntax and timing of your scheduled tasks to ensure they run as intended.

Cron job validator

Use the input below to validate a cron expression. A human readable version of the expression will be displayed when submitted.

Cron expression

Your cron job will run:

Submit

You can also use [crontab guru](https://crontab.guru/) to validate your cron expressions.

### [Cron expression limitations](#cron-expression-limitations)

*   Cron jobs on Vercel do not support alternative expressions like `MON`, `SUN`, `JAN`, or `DEC`
*   You cannot configure both day of the month and day of the week at the same time. When one has a value, the other must be `*`
*   The timezone is always UTC

## [More resources](#more-resources)

*   [Managing Cron Jobs](/docs/cron-jobs/manage-cron-jobs)
*   [Usage and Pricing](/docs/cron-jobs/usage-and-pricing)

--------------------------------------------------------------------------------
title: "Managing Cron Jobs"
description: "Learn how to manage Cron Jobs effectively in Vercel. Explore cron job duration, error handling, deployments, concurrency control, local execution, and more to optimize your serverless workflows."
last_updated: "null"
source: "https://vercel.com/docs/cron-jobs/manage-cron-jobs"
--------------------------------------------------------------------------------

# Managing Cron Jobs

Copy page

Ask AI about this page

Last updated September 24, 2025

Cron Jobs are available on [all plans](/docs/plans)

## [Viewing cron jobs](#viewing-cron-jobs)

To view your active cron jobs:

1.  Select your project from the Vercel dashboard
2.  Select the Settings tab
3.  Select the Cron Jobs tab from the left sidebar

## [Cron jobs maintenance](#cron-jobs-maintenance)

*   Updating Cron Jobs: Change the [expression](/docs/cron-jobs#cron-expressions) in `vercel.json` file or the function's configuration, and then redeploy
*   Deleting Cron Jobs: Remove the configuration from the `vercel.json` file or the function's configuration, and then redeploy
*   Disabling Cron Jobs: Navigate to the Cron Jobs tab and then click the Disable Cron Jobs button

Disabled cron jobs will still be listed and will count towards your [cron jobs limits](/docs/cron-jobs/usage-and-pricing)

## [Securing cron jobs](#securing-cron-jobs)

It is possible to secure your cron job invocations by adding an environment variable called `CRON_SECRET` to your Vercel project. We recommend using a random string of at least 16 characters for the value of `CRON_SECRET`. A password generator, like [1Password](https://1password.com/password-generator/), can be used to create one.

The value of the variable will be automatically sent as an `Authorization` header when Vercel invokes your cron job. Your endpoint can then compare both values, the authorization header and the environment variable, to verify the authenticity of the request.

You can use App Router [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) to secure your cron jobs, even when using the Pages Router.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/cron/route.ts

TypeScript

TypeScriptJavaScript

```
import type { NextRequest } from 'next/server';
 
export function GET(request: NextRequest) {
  const authHeader = request.headers.get('authorization');
  if (authHeader !== `Bearer ${process.env.CRON_SECRET}`) {
    return new Response('Unauthorized', {
      status: 401,
    });
  }
 
  return Response.json({ success: true });
}
```

The `authorization` header will have the `Bearer` prefix for the value.

For those using TypeScript versions below 5.2, it's important to adapt the code to `import NextResponse from 'next/server'` and use `NextResponse.json` for the response. This ensures compatibility with earlier TypeScript versions in Next.js applications. In TypeScript 5.2 and above, the standard `new Response` pattern should be used.

## [Cron job duration](#cron-job-duration)

The duration limits for Cron jobs are identical to those of [Vercel Functions](/docs/functions#limits). See the [`maxDuration`](/docs/functions/runtimes#max-duration) documentation for more information.

In most cases, these limits are sufficient. However, if you need more processing time, it's recommended to split your cron jobs into different units or distribute your workload by combining cron jobs with regular HTTP requests with your API.

## [Cron job error handling](#cron-job-error-handling)

Vercel will not retry an invocation if a cron job fails. You can check for error [logs](/docs/runtime-logs) through the View Log button in the Cron Jobs tab.

## [Cron jobs with dynamic routes](#cron-jobs-with-dynamic-routes)

Cron jobs can be created for [dynamic routes](https://nextjs.org/docs/routing/dynamic-routes):

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "crons": [
    {
      "path": "/api/sync-slack-team/T0CAQ10TZ",
      "schedule": "0 5 * * *"
    },
    {
      "path": "/api/sync-slack-team/T4BOE34OP",
      "schedule": "0 5 * * *"
    }
  ]
}
```

## [Handling nonexistent paths](#handling-nonexistent-paths)

If you create a cron job for a path that doesn't exist, it generates a [404 error](/docs/errors/platform-error-codes#404:-not_found). However, Vercel still executes your cron job. You can analyze your logs to check if there are any issues.

## [Cron jobs and deployments](#cron-jobs-and-deployments)

Creating a new deployment will not interrupt your running cron jobs; they will continue until they finish.

## [Controlling cron job concurrency](#controlling-cron-job-concurrency)

When a cron job takes too long to run, you might encounter two concurrent cron job invocations, which could cause problems. Implementing a lock mechanism in your cron job, for example by using [Redis](https://redis.io/docs/manual/patterns/distributed-locks/), is recommended in such cases.

Alternatively, ensure your cron job is fast enough or set it to timeout if it runs for too long.

## [Running cron jobs locally](#running-cron-jobs-locally)

Cron jobs are API routes. You can run them locally by making a request to their endpoint. For example, if your cron job is in `/api/cron`, you could visit the following endpoint in your browser: `http://localhost:3000/api/cron`. You should be aware that while your browser may follow redirects, [cron job invocations in production will not](#cron-jobs-and-redirects) follow redirects.

There is currently no support for `vercel dev`, `next dev`, or other framework-native local development servers.

## [Cron jobs and redirects](#cron-jobs-and-redirects)

Cron jobs do not follow redirects. When a cron-triggered endpoint returns a 3xx redirect status code, the job completes without further requests. Redirect responses are treated as final for each invocation.

The view logs button on the cron job overview can be used to verify the response of the invocations and gain further insights.

## [Cron jobs logs](#cron-jobs-logs)

Cron jobs are logged as function invocations from the Logs tab of your projects [dashboard](/dashboard). You can view the logs for a cron job from the list on the [Cron jobs settings page](/docs/cron-jobs/manage-cron-jobs#viewing-cron-jobs) of the project:

1.  From the list of cron jobs, select View Logs.
2.  This will take you to the [runtime logs](/docs/runtime-logs#request-path) view with a `requestPath` filter to your cron job such as `requestPath:/api/my-cron-job`.

See [how to view runtime logs](/docs/runtime-logs#view-runtime-logs) for more information.

Note that when cron jobs respond with a redirect or a cached response, they will not be shown in the logs.

## [Cron jobs accuracy](#cron-jobs-accuracy)

Hobby users can only create cron jobs with [hourly accuracy](/docs/cron-jobs/usage-and-pricing#hobby-scheduling-limits). Vercel may invoke these cron jobs at any point within the specified hour to help distribute load across all accounts. For example, an expression like `* 8 * * *` could trigger an invocation anytime between `08:00:00` and `08:59:59`.

For all other teams, cron jobs will be invoked within the minute specified. For instance, the expression `5 8 * * *` would trigger an invocation between `08:05:00` and `08:05:59`.

## [Rollbacks with cron jobs](#rollbacks-with-cron-jobs)

If you [Instant Rollback](/docs/instant-rollback) to a previous deployment, active cron jobs will not be updated. They will continue to run as scheduled until they are manually disabled or updated.

--------------------------------------------------------------------------------
title: "Getting started with cron jobs"
description: "Learn how to schedule cron jobs to run at specific times or intervals."
last_updated: "null"
source: "https://vercel.com/docs/cron-jobs/quickstart"
--------------------------------------------------------------------------------

# Getting started with cron jobs

Copy page

Ask AI about this page

Last updated July 18, 2025

This guide will help you get started with using cron jobs on Vercel. Cron jobs are scheduled tasks that run at specific times or intervals. They are useful for automating tasks. You will learn how to create a cron job that runs every day at 5 am UTC by creating a Vercel Function and configuring it in your `vercel.json` file.

## [Prerequisites](#prerequisites)

*   [A Vercel account](/signup)
*   [A project](/docs/projects/overview#creating-a-project) with a [Vercel Function](/docs/functions)

1.  ### [Create a function](#create-a-function)
    
    This function contains the code that will be executed by the cron job. This example uses a simple function that returns the user's region.
    
    Next.js (/app)Next.js (/pages)Other frameworks
    
    app/api/hello/route.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    export function GET(request: Request) {
      return new Response('Hello from Vercel!');
    }
    ```
    
2.  ### [Create or update your `vercel.json` file](#create-or-update-your-vercel.json-file)
    
    Create or go to your [`vercel.json`](/docs/project-configuration#functions) file and add the following code:
    
    vercel.json
    
    ```
    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "crons": [
        {
          "path": "/api/hello",
          "schedule": "0 5 * * *"
        }
      ]
    }
    ```
    
    The `crons` property is an array of cron jobs. Each cron job has two properties:
    
    *   The `path`, which must start with `/`
    *   The `schedule` property, which must be a string that represents a [cron expression](/docs/cron-jobs#cron-expressions). In this example, the job is scheduled to execute every day at 5:00 am UTC
3.  ### [Deploy your project.](#deploy-your-project.)
    
    When you deploy your project, Vercel's build process creates the cron job. Vercel invokes cron jobs only for [production](/docs/deployments/environments#production-environment) deployments and not for [preview](/docs/deployments/environments#preview-environment-pre-production) deployments
    
    You can also deploy to your production domain using the CLI:
    
    terminal
    
    ```
    vercel deploy --prod
    ```
    

Your cron job is now active and will call the `/api/hello` path every day at 5:00 am UTC.

## [Next steps](#next-steps)

Now that you have created a cron job, you can learn more about how to manage and configure them:

*   [Learn about managing cron jobs](/docs/cron-jobs/manage-cron-jobs)
*   [Explore usage and pricing](/docs/cron-jobs/usage-and-pricing)

--------------------------------------------------------------------------------
title: "Usage & Pricing for Cron Jobs"
description: "Learn about cron jobs usage and pricing details."
last_updated: "null"
source: "https://vercel.com/docs/cron-jobs/usage-and-pricing"
--------------------------------------------------------------------------------

# Usage & Pricing for Cron Jobs

Copy page

Ask AI about this page

Last updated June 25, 2025

Cron Jobs are available on [all plans](/docs/plans)

Cron jobs invoke [Vercel Functions](/docs/functions). This means the same [usage](/docs/limits) and [pricing](/pricing) limits will apply.

|  | Number of cron jobs per account | Schedule |
| --- | --- | --- |
| Hobby | 2 cron jobs | Triggered once a day |
| Pro | 40 cron jobs | Unlimited cron invocations |
| Enterprise | 100 cron jobs | Unlimited cron invocations |

Each project has a hard limit of 20 cron jobs per project.

### [Hobby scheduling limits](#hobby-scheduling-limits)

On the Hobby plan, Vercel cannot assure a timely cron job invocation. For example, a cron job configured as `0 1 * * *` (every day at 1 am) will trigger anywhere between 1:00 am and 1:59 am.

For more specific cron job executions, upgrade to our [Pro](/docs/plans/pro) plan.

## [Pricing](#pricing)

Cron jobs are included in all plans.

You use a function to invoke a cron job, and therefore [usage](/docs/limits) and [pricing](/pricing) limits for these functions apply to all cron job executions:

*   [Functions limits and pricing](/docs/functions/usage-and-pricing)

--------------------------------------------------------------------------------
title: "Dashboard Overview"
description: "Learn how to use the Vercel dashboard to view and manage all aspects of the Vercel platform, including your Projects and Deployments."
last_updated: "null"
source: "https://vercel.com/docs/dashboard-features"
--------------------------------------------------------------------------------

# Dashboard Overview

Copy page

Ask AI about this page

Last updated September 24, 2025

You can use the [Vercel dashboard](/dashboard) to view and manage all aspects of the Vercel platform, including your [Projects](/docs/projects/overview) and [Deployments](/docs/deployments). What you see in each tab is dependant on the _scope_ that is selected.

![An overview of the Vercel dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fdash-light-3.png&w=1920&q=75)![An overview of the Vercel dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fdash-dark-3.png&w=1920&q=75)

An overview of the Vercel dashboard.

## [Scope selector](#scope-selector)

What you see in each tab is dependant on the _scope_ that is selected.

The scope selector allows you to switch between your Hobby team and any teams that you may be part of. To switch between accounts and teams, select the arrows next to the name:

![The scope selector in the Vercel dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fscope-selector-light.png&w=640&q=75)![The scope selector in the Vercel dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fscope-selector-dark.png&w=640&q=75)

The scope selector in the Vercel dashboard.

To go back to your Team dashboard at any time, click the Vercel logo or the scope selector.

## [Find](#find)

The Find bar allows you to search for:

*   Teams
*   Projects
*   Deployments (by branch)
*   Pages
*   Settings

Access this feature by clicking on the Find search input on the top right of the Vercel dashboard or pressing F on your keyboard.

## [Overview](#overview)

When you first create an account and log on to Vercel, you'll be greeted by your team overview. This shows information on all projects that you have on the selected Vercel team.

You can click on the button to filter by a specific Repository and to choose whether to sort by Activity (which projects you have most recently viewed in the dashboard or deployed to) or Name (alphabetically). Next to the button is a toggle you can use to switch between card view and list view. You can also filter to a certain repository by clicking the pill for that repository on any of its projects.

*   [My dashboard](/dashboard)

## [Integrations](#integrations)

Integrations allow you to extend the capabilities of Vercel and connect with third-party platforms or services. Users and Teams on all plans can use or create Integrations.

Through the Integrations section on the dashboard, you can [view and manage a list of all integrations](/docs/integrations/install-an-integration/product-integration#manage-native-integrations) on your account, browse the marketplace to [install integrations](/docs/integrations/create-integration), or go to the [Integrations Console](/dashboard/integrations/console) to [create your own Integration](/docs/integrations/create-integration).

*   [Integrations overview](/docs/integrations)
*   [My integrations](/dashboard/integrations)

## [Activity](#activity)

The Activity Log provides a list of all events on a Hobby team, chronologically organized since its creation. The [events](/docs/observability/activity-log#events-logged) that you will see are dependant on the type of account and [role within a Team](/docs/accounts/team-members-and-roles).

*   [Activity log overview](/docs/dashboard-features/activity-log)
*   [My activity log](/dashboard/activity)

## [Recent Previews](#recent-previews)

The recent previews panel gives you a quick way to access recently deployed and viewed previews within your teams. It's scoped to the team you are actively viewing.

Each listed preview shows the latest deployment ID and status. Any associated pull request to your git provider is also shown or the relevant git branch.

Selecting a preview from the list will navigate to the live preview.

You can also navigate to related items for a preview deployment:

*   The associated pull request or code repository page by clicking the label that will have the word "Code" or the pull request ID
*   The deployment details by clicking the label with the deployment ID and status icon

Each preview deployment item also has a context menu where you can see further details and also remove the listing.

## [Domains](#domains)

By default, all deployments are assigned a domain with the suffix: `.vercel.app`. This domain can be replaced with a Custom Domain of your choice.

The Domains section of the dashboard lets you view all domains related to your account or Team, and allows you to Buy, Add, or Transfer In a custom domain.

*   [Add a domain](/docs/domains/add-a-domain)
*   [My domains](/dashboard/domains)

## [Usage](#usage)

The Usage tab on the Dashboard provides detailed insight into the actual resource usage of all projects relating to your account or Team.

From the dashboard, you can filter the usage by billing cycle, date, project, or function.

*   [Usage overview](/docs/limits/usage)
*   [My usage](/dashboard/usage)

## [Settings](#settings)

There are two different types of settings pages:

*   Personal Account / Team Settings - These settings allow you to manage account details, billing, invoicing, membership, security, and tokens. The options you see will depend on the your scope and permissions.
    
*   Project Settings - You can view this by selecting a project in the dashboard and then selecting its settings. From there you can manage project details, domains, integrations, Git, functions, environment variables, and security.
    
*   [My settings dashboard](/account)
    

## [Command Menu](#command-menu)

Vercel provides a Command Menu that enables you to navigate through the dashboard and perform common actions using only the keyboard.

You can access the menu using by pressing ⌘ + K on macOS or Ctrl + K on Windows and Linux. Note that you must be logged in to access the Command Menu.

*   [Command Menu overview](/docs/dashboard-features/command-menu)

--------------------------------------------------------------------------------
title: "Using the Command Menu"
description: "Learn how to quickly navigate through the Vercel dashboard with your keyboard using the Command Menu."
last_updated: "null"
source: "https://vercel.com/docs/dashboard-features/command-menu"
--------------------------------------------------------------------------------

# Using the Command Menu

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel provides a menu with shortcuts, called the Command Menu, to navigate through the dashboard and perform common actions using only the keyboard.

You can access the menu by pressing ⌘ + K on macOS or Ctrl + K on Windows and Linux. Alternatively, you can access it by clicking on Command Menu in your personal menu at the top right of the dashboard:

![Opening the Command Menu using your cursor.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Funiversal-search%2Fdashboard-cmdk-light.png&w=1080&q=75)![Opening the Command Menu using your cursor.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Funiversal-search%2Fdashboard-cmdk-dark.png&w=1080&q=75)

Opening the Command Menu using your cursor.

Once opened, the Command Menu will offer you a list of commonly used shortcuts. For example, you can quickly navigate to a specific [Project](/docs/projects/overview) or [Team](/docs/accounts/create-a-team) right away, using your ↑ (arrow up), ↓ (arrow down) and ↵ (enter) keys.

The Command Menu is only available on desktop and tablet devices, but not on smartphones, as it provides the biggest efficiency advantage when used in combination with a keyboard, instead of your mouse or finger.

## [Recently Used Items](#recently-used-items)

By default, the list is comprised of shortcuts that the Vercel Team has found to be most useful for you. However, over time, the list will automatically adapt to your own usage of the Command Menu and begin to suggest recently used shortcuts at the top:

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fcommand-menu%2Frecents-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fcommand-menu%2Frecents-dark.png&w=1920&q=75)

An example of recently used items suggested by the Command Menu.

Up to 3 suggestions for recently used shortcuts will appear, and be ordered by the latest time you used them, with the most recently used item showing up at the very top.

When the dashboard is closed, the suggestions will reset.

## [Context-Based Items](#context-based-items)

Because the purpose of the Command Menu is to get you to your desired goal in the quickest way possible, it also changes its behavior based on your surrounding context on the dashboard.

If you're currently looking at the dashboard for a [Pro](/docs/plans/pro) or [Enterprise](/docs/plans/enterprise) Team, for example, you will be offered to copy a link for inviting new [Team Members](/docs/rbac/managing-team-members) if you're an [Owner](/docs/rbac/access-roles#owner-role) of that Team.

Whereas, if you're on a [Hobby plan](/docs/plans/hobby) instead, you will not be offered that option because Hobby plans don't support collaborating.

## [Additional Keyboard Shortcuts](#additional-keyboard-shortcuts)

In addition to ⌘ + K (instead of ⌘, use Ctrl on Windows or Linux) for opening the overview of the Command Menu, Vercel also offers direct keyboard shortcuts for some of the commonly used actions:

*   Search [Projects](/docs/projects/overview) with ⇧ + P
*   Search [Teams](/docs/accounts/create-a-team) with ⇧ + T
*   Switch between light and dark mode with T

They are also shown next to each of the supported items in the list.

Thanks to the shortcuts mentioned above, you often won't even have to navigate through the items offered by the Command Menu to get to your desired destination quickly.

Instead, you can use these shortcuts to skip the overview of items and perform the action directly. Therefore, it is recommended to embed these shortcuts into your workflow.

## [Searching documentation](#searching-documentation)

The Command Menu allows you to search through the documentation on the Vercel, [Next.js](https://nextjs.org/docs) and [Turborepo](https://turborepo.com) websites.

![Searching from the Vercel documentation.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Funiversal-search%2Funiversal-search-v1-light.png&w=1920&q=75)![Searching from the Vercel documentation.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Funiversal-search%2Funiversal-search-v1-dark.png&w=1920&q=75)

Searching from the Vercel documentation.

### [Searching from the Vercel documentation](#searching-from-the-vercel-documentation)

When on the Vercel documentation site:

1.  Open the command menu using ⌘ + K
2.  Begin typing a search query
3.  The results will then be shown from across all three websites where there is a query match
    *   Initially you will see the top three most relevant results
    *   Followed by the rest of the results split by website
4.  You can filter results by website using the following badges:
    *   All: Results from all three websites (default)
    *   Vercel: Results from the Vercel documentation site
    *   Next.js: Results from the Next.js documentation site
    *   Turborepo: Results from the Turborepo documentation site

### [Searching from the Vercel dashboard](#searching-from-the-vercel-dashboard)

When on the Vercel dashboard:

1.  Open the command menu using ⌘ + K
2.  Scroll down to Search Docs... and select, or use the shortcut Shift + D
3.  Begin typing a search query
4.  The results will then be shown from across all three websites where there is a query match
    *   Initially you will see the top three most relevant results
    *   Followed by the rest of the results split by website
5.  You can filter results by website using the following badges:
    *   All: Results from all three websites (default)
    *   Vercel: Results from the Vercel documentation site
    *   Next.js: Results from the Next.js documentation site
    *   Turborepo: Results from the Turborepo documentation site

## [What about regular menus?](#what-about-regular-menus)

If you want, the Command Menu can be a complete replacement for the traditional dashboard navigation.

Regular menus will continue to exist for the purpose of navigating the dashboard with your mouse or fingers (on touch-based devices), but if you're most efficient using your keyboard, you might prefer the Command Menu.

Over time, the Command Menu will offer increasingly intelligent suggestions and allow for performing more actions inline to increase your productivity.

--------------------------------------------------------------------------------
title: "Navigating the Dashboard"
description: "Learn how to select a scope, change the Project view, use search, or create a new project, all within the Vercel dashboard."
last_updated: "null"
source: "https://vercel.com/docs/dashboard-features/overview"
--------------------------------------------------------------------------------

# Navigating the Dashboard

Copy page

Ask AI about this page

Last updated September 24, 2025

When you sign in to Vercel through your browser, you'll be presented with the dashboard. Any subsequent visits to [vercel.com](https://vercel.com) will automatically direct you to the dashboard.

## [Projects and repositories](#projects-and-repositories)

Your dashboard view shows a list of all projects and repositories that belong to the [selected team](/docs/dashboard-features#scope-selector).

You can click on the button to filter by a specific Repository and to choose whether to sort by Activity (which projects you have most recently viewed in the dashboard or deployed to) or Name (alphabetically).

You can use the toggle to change the view between a grid view and list view. Your viewing preference is saved to your account, so if you access your account on another machine, you'll see the same view each time.

Each project in the view shows:

*   The deployed URL
*   Information about the last commit
*   The Real Experience Score for any deployments using Analytics

You can click on the button to:

*   Add the project to your Favorites
*   Visit the production deployment for the project with the [toolbar](/docs/vercel-toolbar)
*   View Logs
*   Manage Domains
*   Transfer the project
*   Go to Project Settings
*   Access pages for the repository or [Conformance](/docs/conformance)

### [Project Dashboard](#project-dashboard)

You can select any project to bring up its Project Dashboard, which allows you to view information about its deployments and configure its settings.

Learn more in [our project dashboard docs](/docs/projects/project-dashboard).

## [Search](#search)

Use the searchbar to search for the name of any deployed project.

## [Create](#create)

For accounts on a Hobby plan, you can either create a new team or a new project.

For members of a team, depending on your permissions, you can use the Add New… button to add a new project, domain, or team Member.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Foverview%2Fdropdown-light.png&w=750&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Foverview%2Fdropdown-dark.png&w=750&q=75)

The Add New drop-down to create a new project, domain, or team member.

--------------------------------------------------------------------------------
title: "Support Center"
description: "Learn how to communicate securely with the Vercel support team"
last_updated: "null"
source: "https://vercel.com/docs/dashboard-features/support-center"
--------------------------------------------------------------------------------

# Support Center

Copy page

Ask AI about this page

Last updated October 17, 2025

Support Center is available on [all plans](/docs/plans)

The Vercel Support Center provides a secure and streamlined way for you to submit support cases. The Support Center allows you to create and view all cases, their statuses, and any messages from the Customer Success team at Vercel. All cases are securely stored to safeguard your data.

## [Submit a ticket](#submit-a-ticket)

To submit a ticket to Vercel Support, do the following:

1.  From your team's dashboard, select the Support tab and then click the Contact Support button
2.  Select Start Chat, then select your team the issue is related to in the dropdown.
3.  Start a conversation with the AI support agent.
4.  If the AI is unable to resolve your issue, you can submit a ticket by clicking Create Case under the chat.
5.  The AI agent will create a case for you and fill out the initial details based on your conversation with it. You can view the proposed case by clicking the View Support Case Form button. Here you can edit any fields that need changing.
6.  Once you are happy with the case, click Submit Case.

The team aims to respond to tickets as described in the [Support Terms](/legal/support-terms#when).

## [Manage tickets](#manage-tickets)

You can see a list of all support cases, regardless of status, in the Support tab. This list shows the ticket name, number, and the status. To view more information about the ticket, click on the ticket name in the list.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fsupport-center.png&w=2048&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdashboard%2Fsupport-center-dark.png&w=2048&q=75)

Support ticket information.

### [Case correspondence](#case-correspondence)

Each ticket displays all correspondences with the support team. Correspondence on your case is handled both over email and within the case module in the Vercel dashboard. You'll receive notifications about Vercel support responses through email, not within the Vercel dashboard.

### [Manage a ticket status](#manage-a-ticket-status)

To manage the status of any ticket, do the following:

1.  From your team's dashboard, select the Support tab
2.  Find the ticket from the list and click the ticket name to open it
3.  If the ticket was closed, click Reopen case. If it was open, click Close case. In either scenario, you may want to provide additional information for the support team

### [Send attachments to the support team](#send-attachments-to-the-support-team)

The support team may request additional logs or other information from you that you'll need to attach to your support ticket. To upload a file, do the following:

1.  From your team's dashboard, select the Support tab
2.  Find the ticket from the list and click the ticket name to open it
3.  Click Attach a File to bring up your system file dialog. Select the relevant file and click Upload

--------------------------------------------------------------------------------
title: "Data Cache for Next.js"
description: "Vercel Data Cache is a specialized cache that stores responses from data fetches in Next.js App Router"
last_updated: "null"
source: "https://vercel.com/docs/data-cache"
--------------------------------------------------------------------------------

# Data Cache for Next.js

Copy page

Ask AI about this page

Last updated October 9, 2025

Data Cache is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

The Vercel Data Cache is a specialized, granular cache that was introduced with Next.js 13 for storing [segment-level data](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating) while using [Next.js App Router](/docs/frameworks/nextjs).

When using [Next.js caching APIs](https://nextjs.org/docs/app/getting-started/caching-and-revalidating) such as `fetch` or `unstable_cache`, Vercel automatically scaffolds globally distributed infrastructure for you with no additional configuration.

## [Features](#features)

*   Globally available, regional cache: Every region in which your function runs has an independent cache, so any data used in server side rendering or Next.js route handlers is cached close to where the function executes.
*   Time-based revalidation: All cached data can define a revalidation interval, after which the data will be marked as stale, triggering a re-fetch from origin.
*   On-demand revalidation: Any data can be triggered for revalidation on-demand, regardless of the revalidation interval. The revalidation propagates to all regions within 300ms.
*   Tag based revalidation: Next.js allows associating tags with data, which can be used to revalidate all data with the same tag at once with [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag). For example, you can revalidate all responses from a CMS with the same author ID tag.

## [Comparing with ISR and Vercel Cache](#comparing-with-isr-and-vercel-cache)

Next.js combines Vercel Data Cache with [Incremental Static Regeneration](/docs/incremental-static-regeneration) (ISR) to provide an optimized caching infrastructure for your pages.

When a page contains _entirely static data_, Vercel uses ISR to generate the whole page. However, when a page contains a _mix of static and dynamic data_, the dynamic data is re-fetched when rendering the page. In this scenario, Vercel Data Cache is used to cache the static part of the data to avoid slow origin fetches.

Both ISR and Vercel Data Cache support time-based revalidation, on-demand revalidation, and tag based revalidation.

[Vercel's Cache](/docs/edge-cache) is used for caching entire static assets at the edge, such as images, fonts, and JavaScript bundles. The Vercel Data Cache is used for caching data fetched during a function's execution, such as API responses.

## [Managing Data Cache](#managing-data-cache)

When you deploy a Next.js project that uses [App Router](https://nextjs.org/docs/app) to Vercel, the Vercel Data Cache is automatically enabled to cache [segment-level data](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating) alongside ISR in the app router.

### [Observing your Data Cache usage](#observing-your-data-cache-usage)

You can observe your project's Data Cache usage using the [Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F%7E%2Fobservability&title=Try+Observability) tab under your project in the Vercel dashboard. The Runtime Cache tab provides visibility into what's stored in your project's Data Cache along with insights like your cache hit rate and the number of cache reads, cache writes, and on-demand revalidations. To view your usage for Data Cache:

You can also track Data Cache usage per request in the [Logs](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Flogs&title=Logs+tab) tab under the log's request metrics section.

### [Manually purging Data Cache](#manually-purging-data-cache)

You need to have a [member](/docs/rbac/access-roles#member-role) role to perform this task.

In some circumstances, you may need to delete all cached data and force revalidation. You can do this by purging the Data Cache:

1.  Under your project, go to the Settings tab.
2.  In the left sidebar, select Caches.
3.  In the Data Cache section, click Purge Data Cache.
4.  In the dialog, confirm that you wish to delete and click the Continue & Purge Data Cache button.

Purging your Data Cache will create a temporary increase in request times for users as new data needs to be refetched.

## [Using Data Cache examples](#using-data-cache-examples)

These examples use the [Next.js App Router](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating).

### [Time-based revalidation](#time-based-revalidation)

Next.js (/app)Next.js (/pages)

app/page.tsx

TypeScript

TypeScriptJavaScript

```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: {
      revalidate: 3600, // 1 hour
    },
  });
  const data = await res.json();
 
  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

### [Tag-based revalidation](#tag-based-revalidation)

app/page.tsx

TypeScript

TypeScriptJavaScript

```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: {
      tags: ['blog'], // Invalidate with revalidateTag('blog') on-demand
    },
  });
  const data = await res.json();
 
  return '...';
}
```

app/actions.ts

TypeScript

TypeScriptJavaScript

```
'use server';
 
import { revalidateTag } from 'next/cache';
 
export default async function action() {
  revalidateTag('blog');
}
```

## [Revalidation behavior](#revalidation-behavior)

The Vercel Data Cache infrastructure isolates cached data per Vercel project and [deployment environment](/docs/deployments/environments) (`production` or `preview`).

Vercel persists cached data across deployments, unless you explicitly invalidate it using framework api's like `res.revalidate`, `revalidateTag` and `revalidatePath`, or by [manually purging Vercel Cache](/docs/edge-cache#manually-purging-vercel-cache). It is not updated at build time. When invalidated, Vercel updates the data at run time, triggered by the next request to the invalidated path.

When the system triggers a revalidation, Vercel marks the corresponding path or cache tag as stale in every Vercel CDN region. The next request to that path or tag, regardless of the region, initiates revalidation and updates the cache globally. Vercel purges and updates the regional cache in all regions within 300ms.

## [Limits](#limits)

| Data Cache property | Limit |
| --- | --- |
| Item size | 2 MB (items larger won't be cached) |
| Tags per item | 128 tags |
| Maximum tag length | 256 bytes |

## [More resources](#more-resources)

*   [Explore Vercel regions](/docs/regions)
*   [Next.js App Router template](/templates/next.js/app-directory)
*   [Usage of Data Cache with ISR](/docs/data-cache#comparing-with-isr-and-vercel-cache)
*   [Learn how Data Cache works in Next.js](https://nextjs.org/docs/app/deep-dive/caching#data-cache)

--------------------------------------------------------------------------------
title: "Working with the Deploy Button"
description: "Deploy public Git projects with the Deploy Button, and set up new projects with Vercel and GitHub, GitLab, or Bitbucket"
last_updated: "null"
source: "https://vercel.com/docs/deploy-button"
--------------------------------------------------------------------------------

# Working with the Deploy Button

Copy page

Ask AI about this page

Last updated March 12, 2025

The Deploy Button allows users to deploy a new project through the Vercel Project creation flow, while cloning the source Git repository to GitHub, GitLab, or Bitbucket.

You can [create your Deploy Button with the generator below](#generate-your-own).

The Vercel Project creation flow allows users to deploy a Git repository, create a project with Vercel, and clone the source repository into their GitHub, GitLab, or Bitbucket account.

## [Snippets](#snippets)

With the Vercel Project creation flow, you can add various URL query parameters to control the experience a user will have, depending on the requirements of your project.

[![Deploy button](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world)

An example Deploy Button using the following [HTML snippet](#snippets).

Use the snippets below in your Git repositories or your dashboards for users to deploy.

MarkdownHTMLURL

\[!\[Deploy with Vercel\](https://vercel.com/button)\](https://vercel.com/new/clone?**repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world**)

A Markdown snippet that shows a linked Deploy Button.

<a href="https://vercel.com/new/clone?**repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world**"><img src="https://vercel.com/button" alt="Deploy with Vercel"/></a>

A HTML snippet that shows a linked Deploy Button.

https://vercel.com/new/clone?**repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world**

A Deploy Button source URL.

### [Generate Your Own](#generate-your-own)

Customize the above Deploy Button [snippets](#snippets) starting with a public Git repository URL from GitHub, GitLab, or Bitbucket.

Git Repository

You can customize the Project creation flow and created project with the following additional settings:

*   [Environment Variables](#environment-variables)
*   [Defaults](#defaults)
*   [Redirect](#redirect)
*   [Integrations](#integrations)
*   [Products](#products)

### [Environment Variables](#environment-variables)

Define Environment Variable Keys that the Git repository needs to deploy successfully. The values will be filled in by the user. You can optionally provide default values for non-sensitive variables.

Default values should only be used for non-sensitive, non-secret values. For example, use them for configuration settings, feature flags, or public API endpoints. Never use default values for passwords, API keys, tokens, or any sensitive data.

Environment Variables Keys

Add Environment Variable

Add a description with additional information and a link to documentation that helps users understand what they are providing values for.

Environment Variables Description

Environment Variables Link

### [Defaults](#defaults)

If you're setting up a project on behalf of the user and already know what name the user likely wants, enter a default project name.

Set a default repository name for the new Git repository created by the user in the Project creation flow.

Default Project Name

Default Git Repository Name

### [Redirect](#redirect)

The Redirect URL parameter allows you to redirect the user back to your platform on the event of a successful deployment and receive information on the created project.

Redirect URL

Set a Developer ID to show a logo and name from an [Integration](/docs/integrations) by using its Client ID, found in the Integration Developer Console.

Developer ID

Set a name for a [Deploy Hook](/docs/deploy-hooks) to receive a Deploy Hook URL in return when redirecting the user from the Project creation flow.

Deploy Hook Name

### [Demo](#demo)

To showcase a successful deployment to the user clicking a Deploy Button, you can customize the Project creation flow's landing page with a **Demo Card**.

The Demo Card contains a title, a description, an image, and a link. All of them are required for the Demo Card to show on the page.

Demo Title

Demo Description

Demo URL

Demo Image

### [Integrations](#integrations)

Integrations let you connect your Vercel Project with third-party services to automate aspects of your workflow.

When Integrations IDs are specified, the corresponding [Integrations](/docs/integrations) are required to be installed for the Vercel Project. If needed, they can also be marked as optional using the [Optional Integrations parameter](#optional-integrations).

Integration IDs can be found in the [Integrations Console](/dashboard/integrations/console).

Integration IDs

Add Integration ID

Additionally, you can specify an external ID or reference that will be passed to the [Redirect URL](/docs/integrations#o-auth-integrations/hybrid-mode) of each of the required Integrations.

External ID

​Allow for skipping Integrations or adding only one of them

### [Products](#products)

You can define a default [product](/docs/integrations/marketplace-product#create-your-product) for your installed [native integration](/docs/integrations#native-integrations).

The `products` parameter expects a [JSON object](/docs/deploy-button/source#store-product-integration) with a `integrationSlug` key, a `productSlug` key and a `protocol`. Alternatively, you can set the product `protocol` and `group`.

integrationSlug

productSlug

Product Protocol

Group

--------------------------------------------------------------------------------
title: "Build Settings"
description: "Learn how to configure the Build & Development settings for your Vercel Deploy Button."
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/build-settings"
--------------------------------------------------------------------------------

# Build Settings

Copy page

Ask AI about this page

Last updated August 8, 2025

## [Build Command](#build-command)

| Parameter | Type | Description |
| --- | --- | --- |
| `build-command` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define a custom Build command that is normally automatically configured based on your Project's framework.

The example below shows a source URL using the `build-command` parameter to set the Build command to `npm run build`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&build-command=npm%20run%20build
```

## [Install Command](#install-command)

| Parameter | Type | Description |
| --- | --- | --- |
| `install-command` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define a custom Install command that is normally automatically configured based on the following:

| Lock File | Install Command | Package Manager Version |
| --- | --- | --- |
| `pnpm-lock.yaml` | `pnpm install` | `pnpm 6/7/8/9/10` See [supported package managers](/docs/package-managers#supported-package-managers) for pnpm detection details |
| `package-lock.json` | `npm install` | `npm` |
| `bun.lockb` | `bun install` | `bun 1` |
| `bun.lock` | `bun install` | `bun 1` |
| None | `npm install` | N/A |

The example below shows a source URL using the `install-command` parameter to set the Install command to `npm install`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&install-command=npm%20install
```

## [Development Command](#development-command)

| Parameter | Type | Description |
| --- | --- | --- |
| `dev-command` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define a custom development command if you are using `vercel dev` to test your project locally. Each framework has its own development command and this will be set automatically based on your selected framework.

The example below shows a source URL using the `dev-command` parameter to set the Development command to `next dev --port $PORT`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&dev-command=next%20dev%20--port%20%24PORT
```

## [Ignored Build Command](#ignored-build-command)

| Parameter | Type | Description |
| --- | --- | --- |
| `ignore-command` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define an Ignored Build Step to determine when your project should build and deploy.

The example below shows a source URL using the `ignore-command` parameter to set the Ignored Build Step command to `npx turbo-ignore`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&ignore-command=npx%20turbo-ignore
```

## [Root Directory](#root-directory)

| Parameter | Type | Description |
| --- | --- | --- |
| `root-directory` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define the path of the directory relative to the root of the Project folder where your source code is located. By default it is empty and equivalent to the root of the repository.

The example below shows a source URL using the `root-directory` parameter to set the Root Directory to `apps/frontend`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel-support%2Fyarn-ws-monorepo&root-directory=apps%2Ffrontend
```

## [Output Directory](#output-directory)

| Parameter | Type | Description |
| --- | --- | --- |
| `output-directory` | `string` | Setting this value is equivalent to enabling the Override toggle for that field in the dashboard. |

This allows you to define the output directory's path relative to the Project folder's root. Usually, this is automatically configured based on your Project's framework.

The example below shows a source URL using the `output-directory` parameter for a monorepo where the application output is generated to `dist/apps/app/.next`:

source url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&output-directory=dist%2Fapps%2Fapp%2F.next
```

--------------------------------------------------------------------------------
title: "Using Callbacks with the Deploy Button"
description: "Learn how to use the Deploy Button's callback parameters to redirect users to your application after a successful deployment."
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/callback"
--------------------------------------------------------------------------------

# Using Callbacks with the Deploy Button

Copy page

Ask AI about this page

Last updated March 17, 2025

## [Redirect URL](#redirect-url)

| Parameter | Type | Value |
| --- | --- | --- |
| `redirect-url` | `string` | The URL to redirect the user to in the event of a successful deployment. |

The Redirect URL parameter allows you to define a URL, other than the newly created Vercel project, to send the user to after a successful deployment.

This parameter is helpful if you are sending a user from an application, to deploy a project with Vercel, but want the user to continue with your application with a project created and deployed.

The example below shows a Deploy Button source URL using the Redirect URL parameter:

redirect url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&redirect-url=https%3A%2F%2Fmy-headless-application.com
```

Provide a custom name and logo for the redirect UI by using the [Developer ID](#developer-id) parameter.

### [Callback Parameters](#callback-parameters)

Vercel additionally attaches some "Callback Parameters" to the defined Redirect URL when the user is redirected. The following parameters give you access to information about the project the user has created and deployed, for you to integrate with Vercel after the user is sent back to you.

| Parameter | Description |
| --- | --- |
| `project-dashboard-url` | The URL to view the Project that was created through the Project creation flow on the Vercel Dashboard. |
| `project-name` | The Name of the Project that was created through the Project creation flow. |
| `deployment-dashboard-url` | The URL to view the Deployment that was created through the Project creation flow on the Vercel Dashboard. |
| `deployment-url` | The URL of the deployment that was created through the Project creation flow. This contains the default production domain that was automatically generated for the project that was created. |
| `repository-url` | The URL of the Git repository that was created through the Project creation flow, within the user's selected Git account (GitHub, GitLab, or Bitbucket). |
| `production-deploy-hook-url` ([conditional](#deploy-hook)) | The URL of a Deploy Hook. Requires [the `production-deploy-hook` parameter](#deploy-hook). |

## [Developer ID](#developer-id)

| Parameter | Type | Value |
| --- | --- | --- |
| `developer-id` | `string` | The Client ID of an Integration. |

The Developer ID parameter allows you to define a [Vercel Integration](/docs/integrations) Client ID which will then attach your logo and name to the UI when using the [Redirect URL](#redirect-url) parameter.

You can find the Developer ID listed as "Client ID" in your [Integrations Developer Console](/dashboard/integrations/console).

This parameter requires the [Redirect URL](#redirect-url) parameter to be set and also that the Integration website field matches the Redirect URL value.

The example below shows a Deploy Button source URL using the Redirect URL and Developer ID parameters:

redirect url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&redirect-url=https%3A%2F%2Fmy-headless-application.com&developer-id=oac_7rUTiCMow23Gyfao9RQQ3Es2
```

## [External ID](#external-id)

| Parameter | Type | Value |
| --- | --- | --- |
| `external-id` | `string` | An external ID or reference of your choice. |

This parameter allows you to pass the ID or reference of your choice to the Project creation flow.

The query parameter will be relayed to the [Redirect URL](/docs/integrations/create-integration) of each required [Integration](/docs/integrations/deploy-button/integrations) when the user adds them in the Project creation flow.

To use this parameter, you also need to specify at least one [Integration](/docs/integrations/deploy-button/integrations).

The example below shows a Deploy Button source URL using the Integration ID and External ID parameters:

external id

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re&external-id=1284210
```

## [Deploy Hook](#deploy-hook)

| Parameter | Type | Value |
| --- | --- | --- |
| `production-deploy-hook` | `string` | The name of the Deploy Hook to set up. |

The Deploy Hook parameter allows you to receive [a URL](/docs/deploy-hooks) when also using the Redirect URL parameter, which you can use to redeploy user's projects for them.

This is useful if you are directing a user to deploy a project that works with your application, for example a headless CMS, and you need to redeploy the user's project in case of a content change that needs to be rebuilt.

The value of this parameter should be the name of the [Deploy Hook](/docs/deploy-hooks) you want to create for the user.

When redirected back to your application upon a successful deployment for the user, you will get the `production-deploy-hook-url` callback parameter in addition to [the default callback parameters](#callback-parameters).

This parameter requires the [Redirect URL](#redirect-url) parameter to also be set.

The example below shows a Deploy Button source URL using the Redirect URL and production Deploy Hook URL parameters:

deploy hook

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&redirect-url=https%3A%2F%2Fmy-headless-application.com&production-deploy-hook=MyHeadlessProject
```

--------------------------------------------------------------------------------
title: "Deploy Button Demo"
description: "Learn how to use the Deploy Button Demo parameters to showcase an example of a successful deployment to the user when clicking the Deploy Button and entering the Project creation flow."
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/demo"
--------------------------------------------------------------------------------

# Deploy Button Demo

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Demo Title](#demo-title)

| Parameter | Type | Value | Required |
| --- | --- | --- | --- |
| `demo-title` | `string` | The title of an example deployment. | Yes |

This parameter allows you to specify the title of an example of a successful deployment.

The parameter is part of the Demo Card parameters. The Demo Card should showcase an example of a successful deployment to the user clicking the Deploy Button and entering the Project creation flow.

The Demo card is displayed only when all `demo-*` parameters are provided.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-title-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-title.png&w=1920&q=75)

The Demo Title parameter is displayed on the Demo Card.

The example below shows how to use the `demo-title` parameter in the Deploy Button source URL:

demo title

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&demo-title=APM%20Story
```

## [Demo Description](#demo-description)

| Parameter | Type | Value | Required |
| --- | --- | --- | --- |
| `demo-description` | `string` | The description of an example deployment. | Yes |

This parameter allows you to specify the description of an example of a successful deployment.

The parameter is part of the Demo Card parameters. The Demo Card should showcase an example of a successful deployment to the user clicking the Deploy Button and entering the Project creation flow.

The Demo card is displayed only when all `demo-*` parameters are provided.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-description-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-description.png&w=1920&q=75)

The Demo Description is displayed on the Demo Card.

The example below shows how to use the `demo-description` parameter in the Deploy Button source URL:

demo description

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&demo-description=A%20statically%20generated%20blog%20example%20using%20Next.js%20%and%20DatoCMS
```

## [Demo URL](#demo-url)

| Parameter | Type | Value | Required |
| --- | --- | --- | --- |
| `demo-url` | `string` | The URL of an example deployment. | Yes |

This parameter allows you to specify the URL of an example of a successful deployment.

The parameter is part of the Demo Card parameters. The Demo Card should showcase an example of a successful deployment to the user clicking the Deploy Button and entering the Project creation flow.

The Demo card is displayed only when all `demo-*` parameters are provided.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-url-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-url.png&w=1920&q=75)

Clicking on the Demo Card will link the user to the URL specified by Demo URL.

The example below shows how to use the `demo-url` parameter in the Deploy Button source URL:

demo url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&demo-url=https%3A%2F%2Fnextjs.org
```

## [Demo Image](#demo-image)

| Parameter | Type | Value | Required |
| --- | --- | --- | --- |
| `demo-image` | `string` | The URL of the screenshot of an example deployment. | Yes |

This parameter allows you to specify the URL of the screenshot of an example of a successful deployment.

The parameter is part of the Demo Card parameters. The Demo Card should showcase an example of a successful deployment to the user clicking the Deploy Button and entering the Project creation flow.

The Demo card is displayed only when all `demo-*` parameters are provided.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-image-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fdeploy-button%2Fdeploy-image.png&w=1920&q=75)

The image specified by Demo Image is displayed on the Demo Card.

The example below shows how to use the `demo-image` parameter in the Deploy Button source URL:

demo image

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&demo-image=https%3A%2F%2Fexample.com%2Fimage.png
```

--------------------------------------------------------------------------------
title: "Using Environment Variables with the Deploy Button"
description: "Learn how to use Environment Variables with the Vercel Deploy Button."
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/environment-variables"
--------------------------------------------------------------------------------

# Using Environment Variables with the Deploy Button

Copy page

Ask AI about this page

Last updated October 27, 2025

## [Required environment variables](#required-environment-variables)

| Parameter | Type | Value |
| --- | --- | --- |
| `env` | `string[]` | A comma-separated list of required environment variable keys. |

Use the `env` parameter to require users to fill in values for environment variables that your project needs to run.

The example below shows how to use the `env` parameter in a Deploy Button source URL:

env

```
https://vercel.com/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&env=PUBLIC_API_KEY,API_SECRET_KEY
```

You cannot pass environment variable values using this parameter because the URL is saved in the browser history, making it insecure.

## [Environment variables default values](#environment-variables-default-values)

| Parameter | Type | Value |
| --- | --- | --- |
| `envDefaults` | `string` | A JSON-encoded object mapping environment variable keys to default values. |

Set non-sensitive default values for required environment variables with the `envDefaults` parameter. When users click the Deploy Button, these defaults pre-populate the form so they can deploy faster or modify the values if needed.

Default values should only be used for non-sensitive configuration. Examples of appropriate use cases:

*   Feature flags (e.g., `ENABLE_ANALYTICS=true`)
*   Public API endpoints (e.g., `API_BASE_URL=https://api.example.com`)
*   Default configuration values (e.g., `MAX_ITEMS_PER_PAGE=10`)
*   Non-sensitive application settings

Never use default values for sensitive data like passwords, API keys, tokens, database credentials, or any secret values. Users should always enter these manually.

The parameter expects a JSON object where keys are the environment variable names (which must also be listed in the `env` parameter), and values are the default values. The JSON must be URI-encoded.

The example below shows how to use the `envDefaults` parameter:

envDefaults

```
https://vercel.com/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&env=NEXT_PUBLIC_API_URL,ENABLE_FEATURE_X&envDefaults=%7B%22NEXT_PUBLIC_API_URL%22%3A%22https%3A%2F%2Fapi.example.com%22%2C%22ENABLE_FEATURE_X%22%3A%22true%22%7D
```

The decoded JSON in this example is:

```
{
  "NEXT_PUBLIC_API_URL": "https://api.example.com",
  "ENABLE_FEATURE_X": "true"
}
```

Default values only apply if the environment variable is listed in the `env` parameter. Users can still modify or clear these values before deploying.

## [Environment variables description](#environment-variables-description)

| Parameter | Type | Value |
| --- | --- | --- |
| `envDescription` | `string` | A short description of the required environment variables |

Add a description that explains what the required environment variables are used for with the `envDescription` parameter. The description should be URL-encoded.

The description provided through this parameter only shows if required environment variables are set.

The example below shows how to use the `envDescription` parameter in a Deploy Button source URL:

envDescription

```
https://vercel.com/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&env=PUBLIC_API_KEY&envDescription=Enter%20your%20public%20API%20Key.
```

## [Environment variables link](#environment-variables-link)

| Parameter | Type | Value |
| --- | --- | --- |
| `envLink` | `string` | A link to an explanation of the required environment variables |

Attach a link to external documentation that helps users find the values they need with the `envLink` parameter. This link should point to specific documentation about your environment variables, not top-level docs.

The link provided through this parameter only shows if required environment variables are set.

The example below shows how to use the `envLink` parameter in a Deploy Button source URL. Make sure you provide users with a specific link instead of top-level documentation:

envLink

```
https://vercel.com/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&env=PUBLIC_API_KEY&envLink=https%3A%2F%2Fvercel.com%2Fdocs
```

--------------------------------------------------------------------------------
title: "Using Integrations with the Deploy Button"
description: "Learn how to use Integrations with the Vercel Deploy Button."
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/integrations"
--------------------------------------------------------------------------------

# Using Integrations with the Deploy Button

Copy page

Ask AI about this page

Last updated September 24, 2025

## [Required Integrations](#required-integrations)

| Parameter | Type | Value |
| --- | --- | --- |
| `integration-ids` | `string[]` | A comma-separated list of required Integrations IDs: `oac_4mkAfc68cuDV4suZRlgkn3R9, oac_JI9dt8xHo7UXmVV6mZTygMNZ` |

This parameter allows you to specify a list of Integration IDs. When specified, the corresponding Integrations will be required to be added before the Project can be imported. You can add up to 3 Integrations per Project.

You can find the IDs of your Integrations in the [Integrations Console](/dashboard/integrations/console).

The example below shows how to use the `integration-ids` parameter in a Deploy Button source URL:

integration id

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re
```

## [Skippable Integrations](#skippable-integrations)

| Parameter | Type | Value |
| --- | --- | --- |
| `skippable-integrations` | `number` | Mark the list of provided Integrations as optional |

If this parameter is present, the user will be able to add one of the provided Integrations or skip them entirely, instead of being forced to add all of them.

Because the user will only be able to select one (not multiple) of the optional Integrations, they should all serve the same purpose. For example, if the purpose is error tracking, the Integrations [Sentry](/integrations/sentry) and [Datadog](/integrations/datadog-logs) could be defined here.

To use this parameter, you also need to specify at least one Integration.

The example below shows how to use the `skippable-integrations` parameter in a Deploy Button source URL:

skippable integrations

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&integration-ids=oac_1mkAfc68cuDV4suZRlgkn3Re&skippable-integrations=1
```

--------------------------------------------------------------------------------
title: "Deploy Button Source"
description: "Learn how to use the Vercel Deploy Button source URL parameters.
  "
last_updated: "null"
source: "https://vercel.com/docs/deploy-button/source"
--------------------------------------------------------------------------------

# Deploy Button Source

Copy page

Ask AI about this page

Last updated March 4, 2025

## [Repository URL](#repository-url)

| Parameter | Type | Value |
| --- | --- | --- |
| `repository-url` | `string` | The source Git repository URL |

The Repository URL parameter allows you to define a Git repository URL, optionally including the subdirectory within a repository, that users will clone into their GitHub, GitLab, or Bitbucket account when going through the Vercel Project creation flow.

The example below shows how to use the Repository URL parameter to set the repository URL to `hello-world`:

repository url

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world
```

The Repository URL parameter is required when sending a user to the Vercel Project creation flow to set up a project from a GitHub, GitLab, or Bitbucket repository.

## [Project Name](#project-name)

| Parameter | Type | Value |
| --- | --- | --- |
| `project-name` | `string` | A default project name |

The Project Name parameter allows you to define a default project name.

This parameter is useful for cases where already know what the user would like to name their project. For example, if you are sending the user to the Project creation flow from an application that has already set up a project for the user that will connect to the created Vercel project.

If there is an existing project using the name passed with this parameter, the user will be required to define a new project name, and therefore the project is not guaranteed to have the specified name.

The example below shows how to use the Project Name parameter to set the project name to "my-awesome-project":

project name

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&project-name=my-awesome-project
```

## [Repository Name](#repository-name)

| Parameter | Type | Value |
| --- | --- | --- |
| `repository-name` | `string` | A default repository name (no spaces) |

The Repository Name parameter allows you to define a default repository name.

Similar to the [Project Name](#project-name) parameter, this parameter is useful in cases where you already know what the user wants to name their repository.

The example below shows how to use the Repository Name parameter to set the repository name to "my-awesome-project":

repository name

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Ftree%2Fcanary%2Fexamples%2Fhello-world&repository-name=my-awesome-project
```

## [Store product integration](#store-product-integration)

| Parameter | Type | Value |
| --- | --- | --- |
| `stores` | `string` | A default JSON object converted to a string |

The JSON object parameter allows you to define a default store product.

The example below shows how to set the parameter to the following JSON value:

```
{
  "type": "integration",
  "integrationSlug": "my-integration-slug",
  "productSlug": "my-product-slug",
  "protocol": "storage"
}
```

First, convert the parameter to a string:

```
const jsonParam = encodeURIComponent(
  JSON.stringify([
    {
      type: 'integration',
      integrationSlug: 'my-integration-slug',
      productSlug: 'my-product-slug',
      protocol: 'storage',
    },
  ]),
);
```

Then, use it as follows:

stores

```
https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnextjs&project-name=my-awesome-project&repository-name=my-awesome-project&stores=%5B%7B%22type%22%3A%22integration%22%2C%22integrationSlug%22%3A%22aws-marketplace-integration-demo%22%2C%22productSlug%22%3A%22vector%22%7D%5D
```

--------------------------------------------------------------------------------
title: "Creating & Triggering Deploy Hooks"
description: "Learn how to create and trigger deploy hooks to integrate Vercel deployments with other systems."
last_updated: "null"
source: "https://vercel.com/docs/deploy-hooks"
--------------------------------------------------------------------------------

# Creating & Triggering Deploy Hooks

Copy page

Ask AI about this page

Last updated September 24, 2025

Deploy Hooks allow you to create URLs that accept HTTP `POST` requests in order to trigger deployments and re-run the [Build Step](/docs/deployments/configure-a-build). These URLs are uniquely linked to your project, repository, and branch, so there is no need to use any authentication mechanism or provide any payload to the `POST` request.

This feature allows you to integrate Vercel deployments with other systems. For example, you can set up:

*   Automatic deployments on content changes from a Headless CMS
*   Scheduled deployments by configuring third-party cron job services to trigger the Deploy Hook
*   Forced deployments from the command line

## [Creating a Deploy Hook](#creating-a-deploy-hook)

To create a Deploy Hook for your project, make sure your project is [connected to a Git repository](/docs/projects/overview#git).

Once your project is connected, navigate to its Settings page and then select the Git menu item.

In the "Deploy Hooks" section, choose a name for your Deploy Hook and select the branch that will be deployed when the generated URL is requested.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hooks-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hooks-dark.png&w=1920&q=75)

Creating a new Deploy Hook.

We suggest you use a name that easily identifies the Deploy Hook so you will be able to understand when it triggers a deployment. We also suggest creating only one Deploy Hook per branch unless you’re using multiple data sources.

After submitting the form, you will see a URL that you can copy and use.

## [Triggering a Deploy Hook](#triggering-a-deploy-hook)

To trigger a Deploy Hook, send a GET or POST request to the provided URL.

Deploy Hooks will not be triggered if you have the `github.enabled = false` [configuration](/docs/project-configuration/git-configuration#github.enabled) present in your `vercel.json` file.

Here's an example request and response you can use for testing:

#### [Example Request](#example-request)

example-request

```
curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_98g22o5YUFVHlKOzj9vKPTyN2SDG/tKybBxqhQs
```

#### [Example Response](#example-response)

example-response

```
{
  "job": {
    "id": "okzCd50AIap1O31g0gne",
    "state": "PENDING",
    "createdAt": 1662825789999
  }
}
```

You do not need to add an authorization header. See [Security](#security) to learn more.

After sending a request, you can see that it triggered a deployment on your project dashboard.

![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hook-deployed-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fdeploy-hook-deployed-dark.png&w=3840&q=75)

Deployments triggered by a Deploy Hook are marked in the list.

## [Security](#security)

When you create a Deploy Hook, a unique identifier is generated in the URL. This allows anyone with the URL to deploy your project, so treat it with the same security as you would any other token or password.

If you believe your Deploy Hook URL has been compromised, you can revoke it and create a new one.

## [Build Cache](#build-cache)

Builds triggered by a Deploy Hook are automatically provided with an appropriate [Build Cache](/docs/deployments/troubleshoot-a-build#what-is-cached) by default, if it exists.

Caching helps speed up the [Build Step](/docs/deployments/configure-a-build), so we encourage you to keep the default behavior. However, if you explicitly want to opt out of using a Build Cache, you can disable it by appending `?buildCache=false` to the Deploy Hook URL.

Here is an example request that explicitly disables the Build Cache:

example-request

```
curl -X POST https://api.vercel.com/v1/integrations/deploy/prj_98g22o5YUFVHlKOzj9vKPTyN2SDG/tKybBxqhQs?buildCache=false
```

Deploy Hooks created before May 11th, 2021 do not have the Build Cache enabled by default. To change it, you can either explicitly append `?buildCache=true` to the Deploy Hook URL, or replace your existing Deploy Hook with a newly created one.

## [Other Optimizations](#other-optimizations)

If you send multiple requests to deploy the same version of your project, previous deployments for the same Deploy Hook will be canceled to reduce build times.

## [Limits](#limits)

*   Hobby and Pro accounts have a limit of 5 deploy hooks per project. Enterprise accounts have a limit of 10 deploy hooks per project.

## [Troubleshooting](#troubleshooting)

If your deploy hook fails to create a deployment, check the status check on the commit associated with the deploy hook to identify any failures. See [Troubleshooting project collaboration](/docs/deployments/troubleshoot-project-collaboration) for more information.

--------------------------------------------------------------------------------
title: "Deployment Checks"
description: "Set conditions that must be met before proceeding to the next phase of the deployment lifecycle."
last_updated: "null"
source: "https://vercel.com/docs/deployment-checks"
--------------------------------------------------------------------------------

# Deployment Checks

Copy page

Ask AI about this page

Last updated October 9, 2025

Deployment Checks are conditions that must be met before promoting a production build to your production environment.

When a project is connected to GitHub using [Vercel for GitHub](/docs/git/vercel-for-github), Vercel can automatically read the statuses of your commits and selected GitHub Action results. Using these statuses, Vercel can prevent production deployments from [promoting to production](/docs/deployments/promoting-a-deployment) until your checks have passed.

## [Understanding Deployment Checks](#understanding-deployment-checks)

Decoupling production builds and releases allows teams to move faster with higher confidence at scale.

*   Feature branches are worked on in isolation and merged to the default branch once the code passes required checks for merging.
*   Production deployments are created after new code is merged, but must pass a set of required checks before being released to end users.

By default, Vercel automatically promotes your most recent, successful production build to your custom production domains. This creates the following release workflow:

1.  Push or merge code to your default branch.
2.  Vercel creates a production build.
3.  Once the build is ready, release the build to production.

At scale, this can mean the set of code that is tested before merging is not the same as the code that would be released to end users. We want to maintain the safety of releases, while allowing developers and [agents](/docs/agents) to continue authoring and merging code at high velocity.

With Deployment Checks, you introduce a new step that ensures the safety of the production deployment before it's released, with the following workflow:

1.  Push or merge code to your default branch.
2.  Vercel creates a production deployment.
3.  Run safety checks to ensure that the build is safe for release.
4.  Once Deployment Checks are passing, release the build to production.

## [Enabling Deployment Checks](#enabling-deployment-checks)

1.  ### [Ensure prerequisites are enabled](#ensure-prerequisites-are-enabled)
    
    1.  Link your project to a Github repository using [Vercel for GitHub](/docs/git/vercel-for-github). This can be verified by navigating to your [projects settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fgit).
    2.  Visit [your project's production environment settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fenvironments%2Fproduction) and ensure automatic aliasing for production is turned on.
2.  ### [Select your Deployment Checks](#select-your-deployment-checks)
    
    Visit [your project's settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdeployment-checks), and select _Add Checks_ to select required Deployment Checks.
    
3.  ### [Update workflows (if necessary)](#update-workflows-if-necessary)
    
    If using GitHub Actions with a [`repository_dispatch`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch) trigger, update your workflows to set a status for Vercel using the [`vercel/repository-dispatch/actions/status@v1`](https://github.com/vercel/repository-dispatch/actions/status) action. This will ensure the commit that triggered the deployment is the one that is used to determine if the Deployment Checks are met.
    
    ```
    - name: 'Notify Vercel'
      uses: 'vercel/repository-dispatch/actions/status@v1'
      with:
        # The name of the check will be used to identify the check in the Deployment Checks settings and must be unique
        name: "Vercel - my-project: e2e-tests"
    ```
    
    If you are not using [`repository_dispatch`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch), you can still use the [`vercel/repository-dispatch/actions/status@v1`](https://github.com/vercel/repository-dispatch/actions/status), however it is not required and you can depend on the check directly.
    
4.  ### [Create a new production deployment](#create-a-new-production-deployment)
    
    Deployment Checks appear as part of a production deployment's lifecycle. Production deployments will still be created, but will not be automatically assigned to your custom domains until all Deployment Checks are met.
    
5.  ### [Run GitHub Actions to fulfill all Deployment Checks](#run-github-actions-to-fulfill-all-deployment-checks)
    
    To meet Deployment Checks, run their corresponding GitHub Actions.
    
    If you're using [`repository_dispatch`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch) to trigger a workflow in response to Vercel deployments, you must use the [`vercel.deployment.ready` event](/docs/git/vercel-for-github#repository-dispatch-events). This event triggers after the deployment is created, and before checks are run.
    
6.  ### [Promote to production once all Deployment Checks are met](#promote-to-production-once-all-deployment-checks-are-met)
    
    Once all of the Deployment Checks have passed, the deployment is aliased to your production domain(s) automatically.
    
    For additional release protection, enable [Rolling Releases](/docs/rolling-releases) to ensure your deployment is fractionally released before promoting to everyone.
    

## [Bypassing Deployment Checks](#bypassing-deployment-checks)

You can bypass Deployment Checks by selecting [Force Promote](/docs/deployments/promoting-a-deployment) from the deployment details page.

## [Limitations](#limitations)

GitHub and GitHub Actions have edge cases with status reporting. These behaviors are matched in GitHub-backed Deployment Checks.

*   To trigger a workflow in response to Vercel deployments using [`repository_dispatch`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch), use the [`vercel/repository-dispatch/actions/status@v1`](https://github.com/vercel/repository-dispatch/actions/status) action to set a status on the commit for Vercel Deployment Checks. This will ensure the commit that triggered the deployment is the one that is used to determine if the Deployment Checks are met.
*   GitHub uses the names of jobs to identify which checks are the same across instances. This means that:
    *   Changing the name of a job requires updating your Deployment Checks to align with the names
    *   Each run of a GitHub Workflow should result in only one commit status. For example, when using [`repository_dispatch`](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#repository_dispatch), ensure the commit status includes the environment name to avoid writing to the same status for each of the triggered workflow runs.
*   Avoid using the same name for actions across multiple workflows. Due to GitHub's implementation of Check Runs, these will collide and introduce race conditions when used with GitHub branch protection rules, GitHub rulesets, and Vercel Deployment Checks.

--------------------------------------------------------------------------------
title: "Deployment Protection on Vercel"
description: "Learn how to secure your Vercel project's preview and production URLs with Deployment Protection. Configure fine-grained access control at the project level for different deployment environments."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection"
--------------------------------------------------------------------------------

# Deployment Protection on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Deployment Protection safeguards both your preview and production URLs across various environments. Configured at the project level through your settings, Deployment Protection provides detailed access control for different deployment types.

Vercel offers the following Deployment Protection features:

*   [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication): Restricts access to your deployments to only Vercel users with suitable access rights. Vercel Authentication is available on all plans
*   [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection): Restricts access to your deployments to only users with the correct password. Password Protection is available on the Enterprise plan, or as a paid add-on for Pro plans
*   [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips): Restricts access to your deployments to only users with the correct IP address. Trusted IPs is available on the Enterprise plan

Deployment protection requires authentication for all requests, including those to Middleware.

## [Configuring Deployment Protection](#configuring-deployment-protection)

Deployment Protection is managed through your project settings. To configure Deployment Protection:

1.  From the [dashboard](/dashboard), select the project you wish to set Deployment Protection on
2.  Once selected, navigate to the Settings tab
3.  From the list, select the Deployment Protection tab

## [Understanding Deployment Protection by environment](#understanding-deployment-protection-by-environment)

You can configure the type of Deployment Protection for each environment in your project depending on your projects security needs. When choosing your protection method, you can select from three options:

*   [Standard Protection](#standard-protection): This option protects all domains except [Production Custom Domains](/docs/domains/working-with-domains/add-a-domain). Standard Protection is available on all plans
*   [All Deployments](#all-deployments): Protects all URLs. Protecting all deployments is available on Pro and Enterprise plans
*   [(Legacy) Standard Protection](#legacy-standard-protection): This option protects all preview URLs and [deployment URLs](/docs/deployments/generated-urls). All [up to date production URLs](/docs/deployments/generated-urls) are unprotected.
*   [(Legacy) Only Preview Deployments](#legacy-only-preview-deployments): This option protects only preview URLs. This does not protect past production deployments.

To protect [only production URLs](#only-production-deployments), you can use [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips). Note that this option is only available on the Enterprise plan.

### [Standard Protection](#standard-protection)

Standard Protection is available on [all plans](/docs/plans)

Standard Protection is the recommended way to secure your deployments, as it protects all domains except [Production Custom Domains](/docs/domains/working-with-domains/add-a-domain).

![Selecting Standard Protection in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fcontentful%2Fimage%2Fe5382hct74si%2F7LHNvuRkcDlKMWswY7c8xd%2F858a8627a82bcec2c456bcd42618b3f5%2FScreenshot_2025-07-09_at_5.05.58%25C3%25A2__pm.png&w=1920&q=75)![Selecting Standard Protection in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fcontentful%2Fimage%2Fe5382hct74si%2F7LHNvuRkcDlKMWswY7c8xd%2F858a8627a82bcec2c456bcd42618b3f5%2FScreenshot_2025-07-09_at_5.05.58%25C3%25A2__pm.png&w=1920&q=75)

Selecting Standard Protection in the Vercel Dashboard.

Standard Protection can be configured with the following Deployment Protection features:

*   [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication)
*   [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
*   [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)

#### [Migrating to Standard Protection](#migrating-to-standard-protection)

Enabling Standard Protection restricts public access to the production [generated deployment URL](/docs/deployments/generated-urls). This affects `VERCEL_URL` and `VERCEL_BRANCH_URL` from [System Environment Variables](/docs/environment-variables/system-environment-variables#system-environment-variables), making them unsuitable for fetch requests.

If you are using `VERCEL_URL` or `VERCEL_BRANCH_URL` to make fetch requests, you will need to update your requests to target the same domain the user has requested.

The Framework Environment Variable `VERCEL_URL` is prefixed with the name of the framework. For example, `VERCEL_URL` for Next.js is `NEXT_PUBLIC_VERCEL_URL`, and `VERCEL_URL` for Nuxt is `NUXT_ENV_VERCEL_URL`. See the [Framework Environment Variables](/docs/environment-variables/framework-environment-variables) documentation for more information.

For client-side requests, use relative paths in the fetch call to target the current domain, automatically including the user's authentication cookie for protected URLs.

```
// Before
fetch(`${process.env.VERCEL_URL}/some/path`);
 
// After
fetch('/some/path');
// Note: For operations requiring fully qualified URLs, such as generating OG images,
// replace '/some/path' with the actual domain (e.g. 'https://yourdomain.com/some/path').
```

For server-side requests, use the origin from the incoming request and manually add request cookies to pass the user's authentication cookie.

```
const headers = { cookie: <incoming request header cookies> };
fetch('<incoming request origin>/some/path', { headers });
```

Bypassing protection using [Protection Bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) is an option but not required for requests targeting the same domain.

### [All deployments](#all-deployments)

Protecting all deployments is available on [Enterprise plans](/docs/plans/enterprise) or with the [Advanced Deployment Protection](/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](/docs/plans/pro)

Selecting All Deployments secures all deployments, both preview and production, restricting public access entirely.

With this configuration, all URLs, including your production domain `example.com` and [generated URLs](/docs/deployments/generated-urls) like `my-project-1234.vercel.app`, are protected.

![Selecting All Deployments in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fall-deployments-light.png&w=1920&q=75)![Selecting All Deployments in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fall-deployments-dark.png&w=1920&q=75)

Selecting All Deployments in the Vercel Dashboard.

Protecting all deployments can be configured with the following Deployment Protection features:

*   [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication)
*   [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
*   [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)

### [Only production deployments](#only-production-deployments)

Protecting production deployments is available on [Enterprise plans](/docs/plans/enterprise)

Restrict access to protected deployments to a list of [Trusted IPs](/docs/deployment-protection/methods-to-protect-deployments/trusted-ips).

Preview deployment URLs remain publicly accessible. This feature is only available on the Enterprise plan.

![Selecting All Deployments in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fprod-deployments-light.png&w=1920&q=75)![Selecting All Deployments in the Vercel Dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fprod-deployments-dark.png&w=1920&q=75)

Selecting All Deployments in the Vercel Dashboard.

### [(Legacy) Standard Protection](#legacy-standard-protection)

(Legacy) Standard Protection is a legacy feature that protects all preview URLs and [deployment URLs](/docs/deployments/generated-urls). All [up to date production URLs](/docs/deployments/generated-urls) are unprotected.

### [(Legacy) Only Preview Deployments](#legacy-only-preview-deployments)

Selecting (Legacy) Only Preview Deployments protects preview URLs, while the production environment remains publicly accessible.

For example, Vercel generates a preview URL such as `my-preview-5678.vercel.app`, which will be protected. In contrast, all production URLs, including any past or current generated production branch URLs like `*-main.vercel.app`, remain accessible.

## [Advanced Deployment Protection](#advanced-deployment-protection)

Advanced Deployment Protection features are available to Enterprise customers by default. Customers on the Pro plan can access these features for an additional $150 per month, including:

*   [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection)
*   [Private Production Deployments](/docs/security/deployment-protection#configuring-deployment-protection)
*   [Deployment Protection Exceptions](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions)

### [Enabling Advanced Deployment Protection](#enabling-advanced-deployment-protection)

To opt-into Advanced Deployment Protection while on a Pro plan:

1.  Navigate to your Project Settings and select the Deployment Protection tab
2.  Then choose one of the above protection features
3.  You will then be prompted to upgrade to the Advanced Deployment Protection add-on through an Enable and Pay button before you can use the feature

When you enable Advanced Deployment Protection, you will be charged $150 per month for the add-on, and will have access to _all_ Advanced Deployment Protection features.

### [Disabling Advanced Deployment Protection](#disabling-advanced-deployment-protection)

To opt out of Advanced Deployment Protection:

1.  Navigate to your Team Settings, then the Billing page
2.  Press Edit on the feature you want to disable and follow the instructions to disable the add-on

In order to disable Advanced Deployment Protection, you must have been using the feature for a minimum of thirty days. After this time, once cancelled, all Advanced Deployment Protection features will be disabled.

## [More resources](#more-resources)

*   [Methods to protect deployments](/docs/deployment-protection/methods-to-protect-deployments)
*   [Methods to bypass deployment protection](/docs/deployment-protection/methods-to-bypass-deployment-protection)

--------------------------------------------------------------------------------
title: "Methods to bypass Deployment Protection"
description: "Learn how to bypass Deployment Protection for specific domains, or for all deployments in a project."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection"
--------------------------------------------------------------------------------

# Methods to bypass Deployment Protection

Copy page

Ask AI about this page

Last updated May 23, 2025

To test, share, or exclude specific domains from Deployment Protection, you can use the following methods to allow specific access while maintaining overall security:

*   [Shareable Links](#sharable-links): Shareable links enable external users to access specific branch deployments by appending a secure query parameter to the URL
*   [Protection Bypass for Automation](#protection-bypass-for-automation): Use a secret to bypass protection features for all deployments in a project, such as for end-to-end (E2E) testing
*   [Deployment Protection Exceptions](#deployment-protection-exceptions): Specify preview domains that should be exempt from deployment protection
*   [OPTIONS Allowlist](#options-allowlist): Specify paths to be unprotected for CORS preflight `OPTIONS` requests

## [Sharable Links](#sharable-links)

Shareable Links are available on [all plans](/docs/plans)

Sharable Links allow external access to specific branch deployments through a secure query parameter. Users with this link can see the latest deployment and leave [comments](/docs/comments) (if enabled and logged in with their Vercel account).

For example, if you generate a Sharable Link for the `feature-new-ui` branch. Users with this link can view the latest deployment and comment.

Learn more about [Sharable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links), and how to generate and revoke them.

## [Protection bypass for Automation](#protection-bypass-for-automation)

Protection Bypass for Automation is available on [all plans](/docs/plans)

For automated tasks like end-to-end (E2E) testing, you can use Protection bypass for Automation. When enabled, it generates a secret that can be used as a System Environment Variable (`VERCEL_AUTOMATION_BYPASS_SECRET`) to bypass protection features for all deployments in a project.

For example, you set up E2E tests that run on deployments. By using this feature and the generated secret, your tests can bypass the protection mechanisms.

Learn more about [Protection bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation), and how to enable and disable it.

## [Deployment Protection Exceptions](#deployment-protection-exceptions)

Deployment Protection Exceptions are available on [Enterprise plans](/docs/plans/enterprise) or with the [Advanced Deployment Protection](/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](/docs/plans/pro)

With Deployment Protection Exceptions you can specify preview domains that should be exempt from deployment protection. Adding a domain to Deployment Protection Exceptions makes it publicly accessible, bypassing features like [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips).

For example, if you add `preview-branch-name.vercel.app` to Deployment Protection Exceptions, this domain becomes publicly accessible, bypassing the project's deployment protection settings. When removed, it reverts to the default protection settings.

Learn more about [Deployment Protection Exceptions](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions), and how to add and remove domains.

## [OPTIONS Allowlist](#options-allowlist)

OPTIONS Allowlist is available on [all plans](/docs/plans)

With OPTIONS Allowlist you can specify paths to be unprotected for preflight OPTIONS requests. This can be used to enable [CORS preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) requests to your project's protected deployments, as browsers do not send authentication on preflight requests.

Incoming request paths will be compared with the paths in the allowlist, if a request path starts with one of the specified paths, and has the method `OPTIONS`, it will bypass Deployment Protection.

For example, if you specify `/api`, all requests to paths that start with `/api` (such as `/api/v1/users` and `/api/v2/projects`) will be unprotected for any `OPTIONS` request.

Learn more about [OPTIONS Allowlist](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist).

## [More resources](#more-resources)

*   [Understanding Deployment Protection by environment](/docs/deployment-protection#understanding-deployment-protection-by-environment)
*   [Methods to protect deployments](/docs/deployment-protection/methods-to-protect-deployments)

--------------------------------------------------------------------------------
title: "Deployment Protection Exception"
description: "Learn how to disable Deployment Protection for a list of preview domains."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions"
--------------------------------------------------------------------------------

# Deployment Protection Exception

Copy page

Ask AI about this page

Last updated September 15, 2025

Deployment Protection Exceptions are available on [Enterprise plans](/docs/plans/enterprise) or with the [Advanced Deployment Protection](/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](/docs/plans/pro)

You can use [Deployment Protection Exceptions](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/deployment-protection-exceptions#adding-a-deployment-protection-exception) to disable Deployment Protection (including [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)) for a list of preview domains.

When you add a domain to Deployment Protection Exceptions, it will automatically become publicly accessible and will no longer be covered by Deployment Protection features. When you remove a domain from Deployment Protection Exceptions, the domain becomes protected again with the project's Deployment Protection settings.

![Deployment Protection Exceptions.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-exception-light.png&w=3840&q=75)![Deployment Protection Exceptions.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-exception-dark.png&w=3840&q=75)

Deployment Protection Exceptions.

Deployment Protection Exceptions is designed for Preview Deployment domains, if you wish to make a Production Deployment domain public, see [Configuring Deployment Protection](/docs/security/deployment-protection#configuring-deployment-protection).

## [Adding a Deployment Protection Exception](#adding-a-deployment-protection-exception)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to the Settings tab, and then to Deployment Protection
2.  ### [Select Add Domain](#select-add-domain)
    
    From the Deployment Protection Exceptions section, select Add Domain:
    
    ![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-exception-no-domain-light.png&w=3840&q=75)![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-exception-no-domain-dark.png&w=3840&q=75)
    
    Add Deployment Protection Exception.
    
3.  ### [Specify domain](#specify-domain)
    
    From the Unprotect Domain modal:
    
    1.  Enter the domain that you wish to unprotect in the input
    2.  Select Continue
    
    ![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-add-domain-light.png&w=828&q=75)![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-add-domain-dark.png&w=828&q=75)
    
    Add Deployment Protection Exception.
    
4.  ### [Confirm domain](#confirm-domain)
    
    From the Unprotect Domain modal:
    
    1.  Confirm the domain by entering it again in the first input
    2.  Enter `unprotect my domain` in the second input
    3.  Select Confirm
    
    All your existing and future deployments for that domain will be unprotected.
    
    ![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-confirm-add-light.png&w=828&q=75)![Add Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-confirm-add-dark.png&w=828&q=75)
    
    Add Deployment Protection Exception.
    

## [Removing a Deployment Protection Exception](#removing-a-deployment-protection-exception)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to the Settings tab, and then to Deployment Protection
2.  ### [Select the Domain to Remove](#select-the-domain-to-remove)
    
    From the Deployment Protection Exceptions section:
    
    1.  From the domain row in the Unprotected Domains table
    2.  Select the dot menu at the end of the row
    3.  From the context menu, select Remove
    
    ![Removing Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fremove-deployment-exception-light.png&w=3840&q=75)![Removing Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fremove-deployment-exception-dark.png&w=3840&q=75)
    
    Removing Deployment Protection Exception.
    
3.  ### [Confirm the Domain to Remove](#confirm-the-domain-to-remove)
    
    From the Reprotect Domain modal:
    
    1.  In the modal, type the domain in the first input
    2.  Type `reprotect my domain` in the second input
    3.  Select Confirm
    
    All your existing and future deployments for that domain will be protected.
    
    ![Removing Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-remove-light.png&w=828&q=75)![Removing Deployment Protection Exception.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fdeployment-protection-exceptions-remove-dark.png&w=828&q=75)
    
    Removing Deployment Protection Exception.
    

## [Managing Deployment Protection Exceptions](#managing-deployment-protection-exceptions)

You can view and manage all the existing Deployment Protection Exceptions for your team in the following way

1.  From your [dashboard](/dashboard) go to the Settings tab
2.  Select Deployment Protection and then choose the Access tab
3.  Click the All Access button and select `Unprotected Previews`

![Dashboard > Settings > Deployment Protection > Access](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fdeployment-protection-exceptions-list.png&w=3840&q=75)![Dashboard > Settings > Deployment Protection > Access](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fdeployment-protection-exceptions-list-dark.png&w=3840&q=75)

Dashboard > Settings > Deployment Protection > Access

--------------------------------------------------------------------------------
title: "OPTIONS Allowlist"
description: "Learn how to disable Deployment Protection for CORS preflight requests for a list of paths."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/options-allowlist"
--------------------------------------------------------------------------------

# OPTIONS Allowlist

Copy page

Ask AI about this page

Last updated September 15, 2025

OPTIONS Allowlist is available on [all plans](/docs/plans)

You can use OPTIONS Allowlist to disable Deployment Protection (including [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)) on any incoming CORS preflight `OPTIONS` request for a list of paths.

When you add a path to OPTIONS Allowlist, any incoming request with the method `OPTIONS` that starts with the path will no longer be covered by Deployment Protection. When you remove a path from OPTIONS Allowlist, the path becomes protected again with the project's Deployment Protection settings.

For example, if you specify `/api`, all requests to paths that start with `/api` (such as `/api/v1/users` and `/api/v2/projects`) will be unprotected for any `OPTIONS` request.

![OPTIONS Allowlist.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-light.png&w=3840&q=75)![OPTIONS Allowlist.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-dark.png&w=3840&q=75)

OPTIONS Allowlist.

## [Enabling OPTIONS Allowlist](#enabling-options-allowlist)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to the Settings tab, and then to Deployment Protection
2.  ### [Enable OPTIONS Allowlist](#enable-options-allowlist)
    
    From the OPTIONS Allowlist section, enable the toggle labelled Disabled:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-disabled-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-disabled-dark.png&w=3840&q=75)
    
3.  ### [Specify a path](#specify-a-path)
    
    Specify a path to add to the OPTIONS Allowlist:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-path-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-path-dark.png&w=3840&q=75)
    
4.  ### [Add more paths](#add-more-paths)
    
    To add more paths, select Add path:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-another-path-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-add-another-path-dark.png&w=3840&q=75)
    
5.  ### [Save changes](#save-changes)
    
    Once all the paths are added, select Save
    

## [Disabling OPTIONS Allowlist](#disabling-options-allowlist)

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to the Settings tab, and then to Deployment Protection
2.  ### [Disable OPTIONS Allowlist](#disable-options-allowlist)
    
    From the OPTIONS Allowlist section, select the toggle labelled Enabled:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-light.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Foptions-allowlist-dark.png&w=3840&q=75)
    
3.  ### [Save changes](#save-changes)
    
    Once all the paths are added, select Save

--------------------------------------------------------------------------------
title: "Protection Bypass for Automation"
description: "Learn how to bypass Vercel Deployment Protection for automated tooling (e.g. E2E testing)."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation"
--------------------------------------------------------------------------------

# Protection Bypass for Automation

Copy page

Ask AI about this page

Last updated September 24, 2025

Protection Bypass for Automation is available on [all plans](/docs/plans)

The Protection Bypass for Automation feature lets you bypass Vercel Deployment Protection ([Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection), [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication), and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips)) for automated tooling (e.g. E2E testing).

The generated secret can be used to bypass deployment protection on all deployments in a project until it is revoked. This value will also be automatically added to your deployments as a [system environment variable](/docs/environment-variables/system-environment-variables#VERCEL_AUTOMATION_BYPASS_SECRET) `VERCEL_AUTOMATION_BYPASS_SECRET`.

The environment variable value is set when a deployment is built, so regenerating the secret in the project settings will invalidate previous deployments. You will need to redeploy your app if you update the secret in order to use the new value.

![Protection Bypass for Automation option](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fenable-bypass-protection-light.png&w=1920&q=75)![Protection Bypass for Automation option](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fsecurity%2Fenable-bypass-protection-dark.png&w=1920&q=75)

Protection Bypass for Automation option

## [Who can manage protection bypass for automation?](#who-can-manage-protection-bypass-for-automation)

*   [Team members](/docs/rbac/access-roles#team-level-roles) with at least the [member](/docs/rbac/access-roles#member-role) role
*   [Project members](/docs/rbac/access-roles#project-level-roles) with the [Project Administrator](/docs/rbac/access-roles#project-administrators) role

## [Using Protection Bypass for Automation](#using-protection-bypass-for-automation)

To use Protection Bypass for Automation, set an HTTP header (or query parameter) named `x-vercel-protection-bypass` with the value of the generated secret for the project.

Using a header is strongly recommended, however in cases where your automation tool is unable to specify a header, it is also possible to set the same name and value as a query parameter.

x-vercel-protection-bypass: your-generated-secret (required)

### [Advanced Configuration](#advanced-configuration)

To bypass authorization on follow-up requests (e.g. for in-browser testing) you can set an additional header or query parameter named `x-vercel-set-bypass-cookie` with the value `true`.

This will set the authorization bypass as a cookie using a redirect with a `Set-Cookie` header.

x-vercel-set-bypass-cookie: true (optional)

If you are accessing the deployment through a non-direct way (e.g. in an `iframe`) then you may need to further configure `x-vercel-set-bypass-cookie` by setting the value to `samesitenone`.

This will set `SameSite` to `None` on the `Set-Cookie` header, by default `SameSite` is set to `Lax`.

x-vercel-set-bypass-cookie: samesitenone (optional)

### [Examples](#examples)

#### [Playwright](#playwright)

playwright.config.ts

```
1const config: PlaywrightTestConfig = {2  use: {3    extraHTTPHeaders: {4      'x-vercel-protection-bypass': process.env.VERCEL_AUTOMATION_BYPASS_SECRET,5      'x-vercel-set-bypass-cookie': true | 'samesitenone' (optional)6    }7  }8}
```

--------------------------------------------------------------------------------
title: "Sharable Links"
description: "Learn how to share your deployments with external users."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/sharable-links"
--------------------------------------------------------------------------------

# Sharable Links

Copy page

Ask AI about this page

Last updated September 24, 2025

Shareable Links are available on [all plans](/docs/plans)

Shareable links allow external users to securely access your deployments through a query string parameter. Shareable links include the ability to leave [Comments](/docs/comments) on deployments which have them enabled.

## [Who can create Shareable Links?](#who-can-create-shareable-links)

*   Non-Production Domains:
    *   [Team members](/docs/rbac/access-roles#team-level-roles) with at least the [Developer](/docs/rbac/access-roles#developer-role) role
    *   [Project members](/docs/rbac/access-roles#project-level-roles) with at least the [Project Developer](/docs/rbac/access-roles#project-developer) role
*   Production Domains:
    *   [Team members](/docs/rbac/access-roles#team-level-roles) with at least the [Member](/docs/rbac/access-roles#member-role) role
    *   [Project members](/docs/rbac/access-roles#project-level-roles) with the [Project Administrator](/docs/rbac/access-roles#project-administrators) role

## [Creating Sharable Links](#creating-sharable-links)

Users with the Admin, Member, and Developer roles can create or revoke sharable links for their project's deployments. Personal accounts can also manage sharable links for their Hobby deployments.

Developers on the hobby plan can only create one shareable link in total per account.

To manage Sharable Links, do the following:

1.  ### [Select your project](#select-your-project)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Vercel Authentication for
    2.  Go to the Deployments tab
2.  ### [Select the deployment](#select-the-deployment)
    
    From the list of Preview Deployments, select the deployment you wish to share.
    
3.  ### [Click Share button](#click-share-button)
    
    From the Deployment page, click Share to display the Share popover. From the popover, select Anyone with the link from the dropdown.
    
    ![The Share settings modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fshareable-links-light.png&w=1200&q=75)![The Share settings modal.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fsharable-links-dark.png&w=1200&q=75)
    
    The Share settings modal.
    
4.  ### [Revoking a Sharable Link](#revoking-a-sharable-link)
    
    To revoke access for users, switch the dropdown option to Only people with access.
    
    If you have also [shared the deployment](/docs/deployments/sharing-deployments) with individual users, you will need to remove them from the Share popover.
    

## [Managing Shareable Links](#managing-shareable-links)

You can view and manage all the existing Shareable Links for your team in the following way

1.  From your [dashboard](/dashboard) go to the Settings tab
2.  Select Deployment Protection and then choose the Access tab
3.  Click the All Access button and select Shareable Links

![Dashboard > Settings > Deployment Protection > Access](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fshareable-links-list.png&w=3840&q=75)![Dashboard > Settings > Deployment Protection > Access](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fshareable-links-list-dark.png&w=3840&q=75)

Dashboard > Settings > Deployment Protection > Access

--------------------------------------------------------------------------------
title: "Methods to Protect Deployments"
description: "Learn about the different methods to protect your deployments on Vercel, including Vercel Authentication, Password Protection, and Trusted IPs."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-protect-deployments"
--------------------------------------------------------------------------------

# Methods to Protect Deployments

Copy page

Ask AI about this page

Last updated September 15, 2025

Vercel offers three methods for protecting your deployments. Depending on your use case, you can choose to protect a single environment, or multiple environments. See [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) for more information.

You can see an overview of your projects' protections in the following way

1.  From your [dashboard](/dashboard) go to the Settings tab
2.  Select Deployment Protection

![View your project protections on the Dashboard > Settings > Deployment Protection page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fdeployment-protection-projects-view.png&w=1080&q=75)![View your project protections on the Dashboard > Settings > Deployment Protection page.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fpreview-deployments%2Fdeployment-protection-projects-view-dark.png&w=1080&q=75)

View your project protections on the Dashboard > Settings > Deployment Protection page.

### [Vercel Authentication](#vercel-authentication)

Vercel Authentication is available on [all plans](/docs/plans)

With Vercel Authentication you can restrict access to all deployments (including non-public deployments), meaning only those with a Vercel account on your team, or those you share a [Sharable Link](/docs/security/deployment-protection/methods-to-bypass-deployment-protection#sharable-links) with, can access non-public urls, such as `my-project-1234-your-name.vercel.app`.

When a Vercel user visits your protected deployment, but they do not have permission to access it, they have the option to [request access](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication#access-requests) for their Vercel account. This request triggers an email and Vercel notification to the branch authors.

Learn more about [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and how to enable it.

### [Password Protection](#password-protection)

Password Protection is available on [Enterprise plans](/docs/plans/enterprise) or with the [Advanced Deployment Protection](/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](/docs/plans/pro)

Password Protection on Vercel lets you restrict access to both non-public, and public deployments depending on the type of [environment protection](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you choose.

Learn more about [Password Protection](/docs/security/deployment-protection/methods-to-protect-deployments/password-protection) and how to enable it.

### [Trusted IPs](#trusted-ips)

Trusted IPs are available on [Enterprise plans](/docs/plans/enterprise)

Trusted IPs restrict deployment access to specified IPv4 addresses and [CIDR ranges](https://www.ipaddressguide.com/cidr), returning a 404 for unauthorized IPs. This protection feature is suitable for limiting access through specific paths like VPNs or external proxies.

Learn more about [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) and how to enable it.

## [More resources](#more-resources)

*   [Understanding Deployment Protection by environment](/docs/deployment-protection#understanding-deployment-protection-by-environment)
*   [Methods to bypass deployment protection](/docs/deployment-protection/methods-to-bypass-deployment-protection)

--------------------------------------------------------------------------------
title: "Password Protection"
description: "Learn how to protect your deployments with a password."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/password-protection"
--------------------------------------------------------------------------------

# Password Protection

Copy page

Ask AI about this page

Last updated September 15, 2025

Password Protection is available on [Enterprise plans](/docs/plans/enterprise) or with the [Advanced Deployment Protection](/docs/security/deployment-protection#advanced-deployment-protection) add-on for [Pro plans](/docs/plans/pro)

Those with the [owner](/docs/rbac/access-roles#owner-role), [member](/docs/rbac/access-roles#member-role) and [admin](/docs/rbac/access-roles#admin-role) roles can manage Password Protection

With [Password Protection](#managing-password-protection) enabled, visitors to your deployment must enter the pre-defined password to gain access. You can set the desired password from your project settings when enabling the feature, and update it any time

![Deployment protected with Password Protection authentication screen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-screen.png&w=828&q=75)![Deployment protected with Password Protection authentication screen.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-screen.png&w=828&q=75)

Deployment protected with Password Protection authentication screen.

## [Password Protection security considerations](#password-protection-security-considerations)

The table below outlines key considerations and security implications when using Password Protection for your deployments on Vercel.

| Consideration | Description |
| --- | --- |
| Environment Configuration | Can be enabled for different environments. See [Understanding Deployment Protection by environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) |
| Compatibility | Compatible with [Vercel Authentication](/docs/security/deployment-protection/methods-to-protect-deployments/vercel-authentication) and [Trusted IPs](/docs/security/deployment-protection/methods-to-protect-deployments/trusted-ips) |
| Bypass Methods | Can be bypassed using [Shareable Links](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/sharable-links) and [Protection bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) |
| Password Persistence | Users only need to enter the password once per deployment, or when the password changes, due to cookie set by the feature being invalidated on password change |
| Password Changes | Users must re-enter a new password if you change the existing one |
| Disabling Protection | All existing deployments become unprotected if you disable the feature |
| Token Scope | JWT tokens set as cookies are valid only for the URL they were set for and can't be reused for different URLs, even if those URLs point to the same deployment |

## [Managing Password Protection](#managing-password-protection)

You can manage Password Protection through the dashboard, API, or Terraform:

1.  ### [Go to Project Deployment Protection Settings](#go-to-project-deployment-protection-settings)
    
    From your Vercel [dashboard](/dashboard):
    
    1.  Select the project that you wish to enable Password Protection for
    2.  Go to Settings then Deployment Protection
2.  ### [Manage Password Protection](#manage-password-protection)
    
    From the Password Protection section:
    
    1.  Use the toggle to enable the feature
    2.  Select the [deployment environment](/docs/security/deployment-protection#understanding-deployment-protection-by-environment) you want to protect
    3.  Enter a password of your choice
    4.  Finally, select Save
    
    All your existing and future deployments will be protected with a password for the project. Next time when you access a deployment, you will be asked to log in by entering the password, which takes you to the deployment. A cookie will then be set in your browser for the deployment URL so you don't need to enter the password every time.
    
    ![Enabling Password Protection.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-light.png&w=1920&q=75)![Enabling Password Protection.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fpassword-protection-dark.png&w=1920&q=75)
    
    Enabling Password Protection.
    

### [Manage using the API](#manage-using-the-api)

You can manage Password Protection using the Vercel API endpoint to [update an existing project](/docs/rest-api/reference/endpoints/projects/update-an-existing-project) with the following body

*   `deploymentType`
    *   `prod_deployment_urls_and_all_previews`: Standard Protection
    *   `all`: All Deployments
    *   `preview`: Only Preview Deployments
*   `password`: Password

```
// enable / update password protection
{
  "passwordProtection": {
    "deploymentType": "prod_deployment_urls_and_all_previews" | "all" | "preview",
    "password": "<password>"
  },
}
 
// disable password protection
{
  "passwordProtection": null
}
```

### [Manage using Terraform](#manage-using-terraform)

You can configure Password Protection using `password_protection` in the `vercel_project` data source in the [Vercel Terraform Provider](https://registry.terraform.io/providers/vercel/vercel/latest/docs/data-sources/project).

--------------------------------------------------------------------------------
title: "Trusted IPs"
description: "Learn how to restrict access to your deployments to a list of trusted IP addresses."
last_updated: "null"
source: "https://vercel.com/docs/deployment-protection/methods-to-protect-deployments/trusted-ips"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./04-vercel-remove.md) | [Index](./index.md) | [Next →](./06-trusted-ips.md)
