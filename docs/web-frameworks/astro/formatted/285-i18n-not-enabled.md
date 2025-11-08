---
title: "i18n Not Enabled"
section: 285
---

# i18n Not Enabled

> **i18nNotEnabled**: The `astro:i18n` module can not be used without enabling i18n in your Astro config.

## What went wrong?

[Section titled “What went wrong?”](#what-went-wrong)

The `astro:i18n` module can not be used without enabling i18n in your Astro config. To enable i18n, add a default locale and a list of supported locales to your Astro config:

```js
import { defineConfig } from 'astro'
export default defineConfig({
 i18n: {
   locales: ['en', 'fr'],
   defaultLocale: 'en',
  },
})
```jsx
For more information on internationalization support in Astro, see our [Internationalization guide](/en/guides/internationalization/).

**See Also:**

* [Internationalization](/en/guides/internationalization/)
* [`i18n` Configuration Reference](/en/reference/configuration-reference/#i18n)

---

[← Previous](284-the-path-doesnt-contain-any-locale.md) | [Index](index.md) | [Next →](index.md)
