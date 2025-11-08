---
title: "Experimental Intellisense for content collections"
section: 367
---

# Experimental Intellisense for content collections

**Type:** `boolean`\
**Default:** `false`

**Added in:** `astro@4.14.0`

Enables Intellisense features (e.g. code completion, quick hints) for your content collection entries in compatible editors.

When enabled, this feature will generate and add JSON schemas to the `.astro` directory in your project. These files can be used by the Astro language server to provide Intellisense inside content files (`.md`, `.mdx`, `.mdoc`).

```js
{
  experimental: {
    contentIntellisense: true,
  },
}
```jsx
To use this feature with the Astro VS Code extension, you must also enable the `astro.content-intellisense` option in your VS Code settings. For editors using the Astro language server directly, pass the `contentIntellisense: true` initialization parameter to enable this feature.

---

[← Previous](366-experimental-client-prerendering.md) | [Index](index.md) | [Next →](index.md)
