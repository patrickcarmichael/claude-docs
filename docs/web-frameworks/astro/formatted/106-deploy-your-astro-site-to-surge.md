---
title: "Deploy your Astro Site to Surge"
section: 106
---

# Deploy your Astro Site to Surge

> How to deploy your Astro site to the web using Surge

You can deploy your Astro project to [Surge](https://surge.sh/), a single-command web publishing platform designed for front-end developers.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install [the Surge CLI](https://www.npmjs.com/package/surge) globally from the terminal, if you haven’t already.

   ```shell
   npm install -g surge
   ```jsx
2. Build your Astro site from your project’s root directory.

   ```shell
   npm run build
   ```jsx
3. Deploy to Surge using the CLI.

   ```shell
   surge dist
   ```jsx
   You can [use a custom domain with Surge](http://surge.sh/help/adding-a-custom-domain) when deploying by running `surge dist yourdomain.com`.

---

[← Previous](105-deploy-your-astro-site-to-stormkit.md) | [Index](index.md) | [Next →](index.md)
