---
title: "Configuring experimental flags"
section: 364
---

# Configuring experimental flags

Experimental features are available only after enabling a flag in the Astro configuration file.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';


export default defineConfig({
    experimental: {
        // enable experimental flags
        // to try out new features
    },
});
```jsx
Astro offers experimental flags to give users early access to new features for testing and feedback.

These flags allow you to participate in feature development by reporting issues and sharing your opinions. These features are not guaranteed to be stable and may include breaking changes even in small `patch` releases while the feature is actively developed.

We recommend [updating Astro](/en/upgrade-astro/#upgrade-to-the-latest-version) frequently, and keeping up with release notes in the [Astro changelog](https://github.com/withastro/astro/blob/main/packages/astro/CHANGELOG.md) which will inform you of any changes needed to your project code. The experimental feature documentation will always be updated for the current released version only.

---

[← Previous](363-unsupported-image-format.md) | [Index](index.md) | [Next →](index.md)
