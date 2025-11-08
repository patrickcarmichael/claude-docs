---
title: "Deploy your Astro Site with Deno"
section: 86
---

# Deploy your Astro Site with Deno

> How to deploy your Astro site to the web using Deno.

You can deploy a static or on-demand rendered Astro site using Deno, either on your own server, or to [Deno Deploy](https://deno.com/deploy), a distributed system that runs JavaScript, TypeScript, and WebAssembly at the edge, worldwide.

This guide includes instructions for running your Astro site on your own server with Deno, and deploying to Deno Deploy through GitHub Actions or the Deno Deploy CLI.

## Requirements

[Section titled “Requirements”](#requirements)

This guide assumes you already have [Deno](https://deno.com/) installed.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed as a static site, or as an on-demand rendered site.

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site with Deno, or to Deno Deploy.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

To enable on-demand rendering in your Astro project using Deno, and to deploy on Deno Deploy:

1. Install [the `@deno/astro-adapter` adapter](https://github.com/denoland/deno-astro-adapter) to your project’s dependencies using your preferred package manager:

   * npm

     ```shell
     npm install @deno/astro-adapter
     ```jsx
   * pnpm

     ```shell
     pnpm install @deno/astro-adapter
     ```jsx
   * Yarn

     ```shell
     yarn add @deno/astro-adapter
     ```jsx
2. Update your `astro.config.mjs` project configuration file with the changes below.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import deno from '@deno/astro-adapter';


   export default defineConfig({
   +  output: 'server',
   +  adapter: deno(),
   });
   ```jsx
3. Update your `preview` script in `package.json` with the change below.

   package.json

   ```diff
   {
     // ...
     "scripts": {
       "dev": "astro dev",
       "start": "astro dev",
       "build": "astro build",
       -"preview": "astro preview"
       +"preview": "deno run --allow-net --allow-read --allow-env ./dist/server/entry.mjs"
     }
   }
   ```jsx
   You can now use this command to preview your production Astro site locally with Deno.

   * npm

     ```shell
     npm run preview
     ```jsx
   * pnpm

     ```shell
     pnpm run preview
     ```jsx
   * Yarn

     ```shell
     yarn run preview
     ```jsx
## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can run your Astro site on your own server, or deploy to Deno Deploy through GitHub Actions or using Deno Deploy’s CLI (command line interface).

### On your own server

[Section titled “On your own server”](#on-your-own-server)

1. Copy your project onto your server.

2. Install the project dependencies using your preferred package manager:

   * npm

     ```shell
     npm install
     ```jsx
   * pnpm

     ```shell
     pnpm install
     ```jsx
   * Yarn

     ```shell
     yarn
     ```jsx
3. Build your Astro site with your preferred package manager:

   * npm

     ```shell
     npm run build
     ```jsx
   * pnpm

     ```shell
     pnpm run build
     ```jsx
   * Yarn

     ```shell
     yarn run build
     ```jsx
4. Start your application with the following command:

   * Static

     ```bash
     deno run -A jsr:@std/http/file-server dist
     ```jsx
   * On demand

     ```bash
     deno run -A ./dist/server/entry.mjs
     ```jsx
### GitHub Actions Deployment

[Section titled “GitHub Actions Deployment”](#github-actions-deployment)

If your project is stored on GitHub, the [Deno Deploy website](https://dash.deno.com/) will guide you through setting up GitHub Actions to deploy your Astro site.

1. Push your code to a public or private GitHub repository.

2. Sign in on [Deno Deploy](https://dash.deno.com/) with your GitHub account, and click on [New Project](https://dash.deno.com).

3. Select your repository, the branch you want to deploy from, and select **GitHub Action** mode. (Your Astro site requires a build step, and cannot use Automatic mode.)

4. In your Astro project, create a new file at `.github/workflows/deploy.yml` and paste in the YAML below. This is similar to the YAML given by Deno Deploy, with the additional steps needed for your Astro site.

   * Static

     .github/workflows/deploy.yml

     ```yaml
     name: Deploy
     on: [push]


     jobs:
       deploy:
         name: Deploy
         runs-on: ubuntu-latest
         permissions:
           id-token: write # Needed for auth with Deno Deploy
           contents: read # Needed to clone the repository


         steps:
           - name: Clone repository
             uses: actions/checkout@v4


           # Not using npm? Change `npm ci` to `yarn install` or `pnpm i`
           - name: Install dependencies
             run: npm ci


           # Not using npm? Change `npm run build` to `yarn build` or `pnpm run build`
           - name: Build Astro
             run: npm run build


           - name: Upload to Deno Deploy
             uses: denoland/deployctl@v1
             with:
               project: my-deno-project # TODO: replace with Deno Deploy project name
               entrypoint: jsr:@std/http/file-server
               root: dist
     ```jsx
   * On demand

     .github/workflows/deploy.yml

     ```yaml
     name: Deploy
     on: [push]


     jobs:
       deploy:
         name: Deploy
         runs-on: ubuntu-latest
         permissions:
           id-token: write # Needed for auth with Deno Deploy
           contents: read # Needed to clone the repository


         steps:
           - name: Clone repository
             uses: actions/checkout@v4


           # Not using npm? Change `npm ci` to `yarn install` or `pnpm i`
           - name: Install dependencies
             run: npm ci


           # Not using npm? Change `npm run build` to `yarn build` or `pnpm run build`
           - name: Build Astro
             run: npm run build


           - name: Upload to Deno Deploy
             uses: denoland/deployctl@v1
             with:
               project: my-deno-project # TODO: replace with Deno Deploy project name
               entrypoint: dist/server/entry.mjs
     ```jsx
5. After committing this YAML file, and pushing to GitHub on your configured deploy branch, the deploy should begin automatically!

   You can track the progress using the “Actions” tab on your GitHub repository page, or on [Deno Deploy](https://dash.deno.com).

### CLI Deployment

[Section titled “CLI Deployment”](#cli-deployment)

1. Install the [Deno Deploy CLI](https://docs.deno.com/deploy/manual/deployctl).

   ```bash
   deno install -gArf jsr:@deno/deployctl
   ```jsx
2. Build your Astro site with your preferred package manager:

   * npm

     ```shell
     npm run build
     ```jsx
   * pnpm

     ```shell
     pnpm run build
     ```jsx
   * Yarn

     ```shell
     yarn run build
     ```jsx
3. Run `deployctl` to deploy!

   * Static

     ```bash
     cd dist && deployctl deploy jsr:@std/http/file-server
     ```jsx
   * On demand

     ```bash
     deployctl deploy ./dist/server/entry.mjs
     ```jsx
   You can track all your deploys on [Deno Deploy](https://dash.deno.com).

4. (Optional) To simplify the build and deploy into one command, add a `deploy-deno` script in `package.json`.

   * Static

     package.json

     ```diff
     {
       // ...
       "scripts": {
       "dev": "astro dev",
       "start": "astro dev",
       "build": "astro build",
       "preview": "astro preview",
       +"deno-deploy": "npm run build && cd dist && deployctl deploy jsr:@std/http/file-server"
       }
     }
     ```jsx
   * On demand

     package.json

     ```diff
     {
       // ...
       "scripts": {
         "dev": "astro dev",
         "start": "astro dev",
         "build": "astro build",
         "preview": "deno run --allow-net --allow-read --allow-env ./dist/server/entry.mjs",
         +"deno-deploy": "npm run build && deployctl deploy ./dist/server/entry.mjs"
       }
     }
     ```jsx
   Then you can use this command to build and deploy your Astro site in one step.

   ```bash
   npm run deno-deploy
   ```

---

[← Previous](85-deploy-your-astro-site-with-cloudray.md) | [Index](index.md) | [Next →](index.md)
