---
title: "Deploy your Astro Site to Kinsta Application Hosting"
section: 98
---

# Deploy your Astro Site to Kinsta Application Hosting

> How to deploy your Astro site to the web on Kinsta Application Hosting.

You can use [Kinsta Application Hosting](https://kinsta.com/application-hosting/) to host an Astro site on their cloud hosting.

## Configuring your Astro project

[Section titled “Configuring your Astro project”](#configuring-your-astro-project)

### Static hosting

[Section titled “Static hosting”](#static-hosting)

Looking for an example?

Check out [the official Kinsta Application Hosting Starter project for Astro](https://github.com/kinsta/hello-world-astro)!

To host your project on **Kinsta Application Hosting**, you need to:

* Include a `name` field in your `package.json`. (This can be anything, and will not affect your deployment.)
* Include a `build` script in your `package.json`. (Your Astro project should already include this.)
* Install the [`serve`](https://www.npmjs.com/package/serve) package and set the `start` script to `serve dist/`.

Here are the necessary lines in your `package.json` file:

package.json

```diff
{
  "name": "anything", // This is required, but the value does not matter.
  "scripts": {
    "dev": "astro dev",
    "start": "serve dist/",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^2.2.0",
    +"serve": "^14.0.1"
  },
}
```jsx
### SSR

[Section titled “SSR”](#ssr)

Looking for an example?

Check out [the official Kinsta Application Hosting Starter project for Astro SSR](https://github.com/kinsta/hello-world-astro-ssr)!

To host your project on **Kinsta Application Hosting**, you need to:

* Include a `name` field in your `package.json`. (This can be anything, and will not affect your deployment.)
* Include a `build` script in your `package.json`. (Your Astro project should already include this.)
* Install the [`@astrojs/node`](https://www.npmjs.com/package/@astrojs/node) package and set the `start` script to `node ./dist/server/entry.mjs`.
* Set the `astro.config.mjs` to use `@astrojs/node` and to use `host: true`.

Here are the necessary lines in your `package.json` file:

package.json

```diff
{
  "name": "anything", // This is required, but the value does not matter.
  "scripts": {
    "dev": "astro dev",
    "start": "node ./dist/server/entry.mjs",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "astro": "^2.2.0",
    +"@astrojs/node": "^5.1.1"
  },
}
```jsx
Here are the necessary lines in your `astro.config.mjs` file:

astro.config.mjs

```js
  import { defineConfig } from 'astro/config';
  import node from "@astrojs/node";


  export default defineConfig({
    output: 'server',
    adapter: node({
      mode: "standalone"
    }),
    server: {
      host: true
    }
  });
```jsx
## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

Once your project’s GitHub repository is connected, you can trigger manual deploys to Kinsta Application Hosting in the **MyKinsta Admin Panel**. You can also set up automatic deployments in your admin panel.

### Configuring a new Kinsta application

[Section titled “Configuring a new Kinsta application”](#configuring-a-new-kinsta-application)

1. Go to the [My Kinsta](https://my.kinsta.com/) admin panel.

2. Go to the **Applications** tab.

3. Connect your GitHub repository.

4. Press the **Add service** > **Application** button.

5. Follow the wizard steps.

6. Your application is deployed.

---

[← Previous](97-deploy-your-astro-site-to-heroku.md) | [Index](index.md) | [Next →](index.md)
