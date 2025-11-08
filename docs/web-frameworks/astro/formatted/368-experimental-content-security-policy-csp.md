---
title: "Experimental Content Security Policy (CSP)"
section: 368
---

# Experimental Content Security Policy (CSP)

**Type:** `boolean | object`\
**Default:** `false`

**Added in:** `astro@5.9.0`

Enables support for [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) to help minimize certain types of security threats by controlling which resources a document is allowed to load. This provides additional protection against [cross-site scripting (XSS)](https://developer.mozilla.org/en-US/docs/Glossary/Cross-site_scripting) attacks.

Enabling this feature adds additional security to **Astro’s handling of processed and bundled scripts and styles** by default, and allows you to further configure these, and additional, content types.

This experimental CSP feature has some limitations. Inline scripts are not supported out of the box, but you can [provide your own hashes](#hashes) for external and inline scripts. [Astro’s view transitions](/en/guides/view-transitions/) using the `<ClientRouter />` are not supported, but you can [consider migrating to the browser native View Transition API](https://events-3bg.pages.dev/jotter/astro-view-transitions/) instead if you are not using Astro’s enhancements to the native View Transitions and Navigation APIs.

Note

Due to the nature of the Vite dev server, this feature isn’t supported while working in `dev` mode. Instead, you can test this in your Astro project using `build` and `preview`.

To enable this feature, add the experimental flag in your Astro config:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';


export default defineConfig({
+  experimental: {
+    csp: true
+  }
});
```jsx
When enabled, Astro will add a `<meta>` element inside the `<head>` element of each page.

This element will have the `http-equiv="content-security-policy"` attribute, and the `content` attribute will provide values for the `script-src` and `style-src` [directives](#directives) based on the script and styles used in the page.

```html
<head>
  <meta
    http-equiv="content-security-policy"
    content="
      script-src 'self' 'sha256-somehash';
      style-src 'self' 'sha256-somehash';
    "
  >
</head>
```jsx
## Configuration

[Section titled “Configuration”](#configuration)

You can further customize the `<meta>` element by enabling this feature with a configuration object that includes additional options.

### `algorithm`

[Section titled “algorithm”](#algorithm)

**Type:** `'SHA-256' | 'SHA-512' | 'SHA-384'`\
**Default:** `'SHA-256'`

**Added in:** `astro@5.9.0`

The [hash function](https://developer.mozilla.org/en-US/docs/Glossary/Hash_function) to use when generating the hashes of the styles and scripts emitted by Astro.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      algorithm: 'SHA-512'
    }
  }
});
```jsx
### `directives`

[Section titled “directives”](#directives)

**Type:** `CspDirective[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of [CSP directives](https://content-security-policy.com/#directive) that defines valid sources for specific content types.

While Astro needs to control the `script-src` and `style-src` directives, it is possible to control other CSP directives using the `csp.directives` field. These directives are added to all pages. It accepts a list of type-safe directives:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      directives: [
        "default-src 'self'",
        "img-src 'self' https://images.cdn.example.com"
      ]
    }
  }
});
```jsx
After the build, the `<meta>` element will add your directives into the `content` value alongside Astro’s default directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    default-src 'self';
    img-src 'self' 'https://images.cdn.example.com';
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```jsx
### `styleDirective` and `scriptDirective`

[Section titled “styleDirective and scriptDirective”](#styledirective-and-scriptdirective)

**Type:** `object`\
**Default:** `{}`

**Added in:** `astro@5.9.0`

Configuration objects that allow you to override the default sources for the `style-src` and `script-src` directives with the [`resources`](#resources) property, or to provide additional [hashes](#hashes) to be rendered.

These properties are added to all pages and **completely override Astro’s default resources**, not add to them. Therefore, you must explicitly specify any default values that you want to be included.

#### `resources`

[Section titled “resources”](#resources)

**Type:** `string[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of valid sources for the `script-src` and `style-src` directives.

The `script-src` and `style-src` directives are handled by Astro by default, and use the `'self'` resource. This means that scripts and styles can only be downloaded by the current host (usually the current website).

To override the default source, you can provide a list of resources instead. This will not include `'self'` by default, and must be included in this list if you wish to keep it. These resources are added to all pages.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      styleDirective: {
        resources: [
          "'self'",
          "https://styles.cdn.example.com"
        ]
      },
      scriptDirective: {
        resources: [
          "https://cdn.example.com"
        ]
      }
    }
  }
});
```jsx
After the build, the `<meta>` element will instead apply your sources to the `style-src` and `script-src` directives:

```html
<head>
  <meta
    http-equiv="content-security-policy"
    content="
      script-src https://cdn.example.com 'sha256-somehash';
      style-src 'self' https://styles.cdn.example.com 'sha256-somehash';
    "
  >
</head>
```jsx
#### `hashes`

[Section titled “hashes”](#hashes)

**Type:** `CspHash[]`\
**Default:** `[]`

**Added in:** `astro@5.9.0`

A list of additional hashes to be rendered.

If you have external scripts or styles that aren’t generated by Astro, or inline scripts, this configuration option allows you to provide additional hashes to be rendered.

You must provide hashes that start with `sha384-`, `sha512-` or `sha256-`. Other values will cause a validation error. These hashes are added to all pages.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      styleDirective: {
        hashes: [
          "sha384-styleHash",
          "sha512-styleHash",
          "sha256-styleHash"
        ]
      },
      scriptDirective: {
        hashes: [
          "sha384-scriptHash",
          "sha512-scriptHash",
          "sha256-scriptHash"
        ]
      }
    }
  }
});
```jsx
After the build, the `<meta>` element will include your additional hashes in the `script-src` and `style-src` directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha384-scriptHash' 'sha512-scriptHash' 'sha256-scriptHash' 'sha256-generatedByAstro';
    style-src 'self' 'sha384-styleHash' 'sha512-styleHash' 'sha256-styleHash' 'sha256-generatedByAstro';
  "
>
```jsx
#### `strictDynamic`

[Section titled “strictDynamic”](#strictdynamic)

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@5.9.0`

Enables [the `strict-dynamic` keyword](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP#the_strict-dynamic_keyword) to support the dynamic injection of scripts.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
  experimental: {
    csp: {
      scriptDirective: {
        strictDynamic: true
      }
    }
  }
});
```jsx
## Runtime APIs

[Section titled “Runtime APIs”](#runtime-apis)

You can customize the `<meta>` element per page via runtime APIs available from the `Astro` global inside `.astro` components, or the `APIContext` type in endpoints and middleware.

### `csp.insertDirective`

[Section titled “csp.insertDirective”](#cspinsertdirective)

**Type:** `(directive: CspDirective) => void`

**Added in:** `astro@5.9.0`

Adds a single directive to the current page. You can call this method multiple times to add additional directives.

```astro
---
Astro.csp.insertDirective("default-src 'self'");
Astro.csp.insertDirective("img-src 'self' https://images.cdn.example.com");
---
```jsx
After the build, the `<meta>` element for this individual page will incorporate your additional directives alongside the existing `script-src` and `style-src` directives:

```html
<meta
  http-equiv="content-security-policy"
  content="
    default-src 'self';
    img-src 'self' https://images.cdn.example.com;
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```jsx
### `csp.insertStyleResource`

[Section titled “csp.insertStyleResource”](#cspinsertstyleresource)

**Type:** `(resource: string) => void`

**Added in:** `astro@5.9.0`

Inserts a new resource to be used for the `style-src` directive.

```astro
---
Astro.csp.insertStyleResource("https://styles.cdn.example.com");
---
```jsx
After the build, the `<meta>` element for this individual page will add your source to the default `style-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash';
    style-src https://styles.cdn.example.com 'sha256-somehash';
  "
>
```jsx
### `csp.insertStyleHash`

[Section titled “csp.insertStyleHash”](#cspinsertstylehash)

**Type:** `(hash: CspHash) => void`

**Added in:** `astro@5.9.0`

Adds a new hash to the `style-src` directive.

```astro
---
Astro.csp.insertStyleHash("sha512-styleHash");
---
```jsx
After the build, the `<meta>` element for this individual page will add your hash to the default `style-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash';
    style-src 'self' 'sha256-somehash' 'sha512-styleHash';
  "
>
```jsx
### `csp.insertScriptResource`

[Section titled “csp.insertScriptResource”](#cspinsertscriptresource)

**Type:** `(resource: string) => void`

**Added in:** `astro@5.9.0`

Inserts a new valid source to be used for the `script-src` directive.

```astro
---
Astro.csp.insertScriptResource("https://scripts.cdn.example.com");
---
```jsx
After the build, the `<meta>` element for this individual page will add your source to the default `script-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src https://scripts.cdn.example.com 'sha256-somehash';
    style-src 'self' 'sha256-somehash';
  "
>
```jsx
### `csp.insertScriptHash`

[Section titled “csp.insertScriptHash”](#cspinsertscripthash)

**Type:** `(hash: CspHash) => void`

**Added in:** `astro@5.9.0`

Adds a new hash to the `script-src` directive.

```astro
---
Astro.csp.insertScriptHash("sha512-scriptHash");
---
```jsx
After the build, the `<meta>` element for this individual page will add your hash to the default `script-src` directive:

```html
<meta
  http-equiv="content-security-policy"
  content="
    script-src 'self' 'sha256-somehash' 'sha512-styleHash';
    style-src 'self' 'sha256-somehash';
  "
>
```

---

[← Previous](367-experimental-intellisense-for-content-collections.md) | [Index](index.md) | [Next →](index.md)
