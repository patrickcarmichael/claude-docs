**Navigation:** [← Previous](./04-optimizely-cms-astro.md) | [Index](./index.md) | [Next →](./06-add-integrations.md)

---

# Deploy your Astro Site to Fly.io

> How to deploy your Astro site to the web using Fly.io.

You can deploy your Astro project to [Fly.io](https://fly.io/), a platform for running full stack apps and databases close to your users.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Fly.io as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Fly.io.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable on-demand rendering in your Astro project and deploy on Fly.io, add [the Node.js adapter](/en/guides/integrations-guide/node/).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. [Sign up for Fly.io](https://fly.io/docs/getting-started/log-in-to-fly/#first-time-or-no-fly-account-sign-up-for-fly) if you haven’t already.

2. [Install `flyctl`](https://fly.io/docs/hands-on/install-flyctl/), your Fly.io app command center.

3. Run the following command in your terminal.

   ```bash
   fly launch
   ```

   `flyctl` will automatically detect Astro, configure the correct settings, build your image, and deploy it to the Fly.io platform.

## Generating your Astro Dockerfile

[Section titled “Generating your Astro Dockerfile”](#generating-your-astro-dockerfile)

If you don’t already have a Dockerfile, `fly launch` will generate one for you, as well as prepare a `fly.toml` file. For pages rendered on demand, this Dockerfile will include the appropriate start command and environment variables.

You can instead create your own Dockerfile using [Dockerfile generator](https://www.npmjs.com/package/@flydotio/dockerfile) and then run using the command `npx dockerfile` for Node applications or `bunx dockerfile` for Bun applications.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out [the official Fly.io docs](https://fly.io/docs/js/frameworks/astro/)

# Deploy your Astro Site to GitHub Pages

> How to deploy your Astro site to the web using GitHub Pages.

You can use [GitHub Pages](https://pages.github.com/) to host a static, prerendered Astro website directly from a repository on [GitHub.com](https://github.com/) using [GitHub Actions](https://github.com/features/actions).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

Astro maintains an [official Astro GitHub Action to deploy your project to a GitHub Pages](https://github.com/withastro/action) with very little configuration and is the recommended way to deploy to GitHub Pages.

Follow the instructions below to use the GitHub Action to deploy your Astro site to GitHub Pages. This will create a website from your repository at a GitHub URL (e.g. `https://<username>.github.io/<my-repo>`). Once deployed, you can optionally [configure a custom domain](#change-your-github-url-to-a-custom-domain) to deploy your GitHub Pages site at your preferred domain (e.g. `https://example.com`).

1. Create a new file in your project at `.github/workflows/deploy.yml` and paste in the YAML below.

   deploy.yml

   ```yaml
   name: Deploy to GitHub Pages


   on:
     # Trigger the workflow every time you push to the `main` branch
     # Using a different branch name? Replace `main` with your branch’s name
     push:
       branches: [ main ]
     # Allows you to run this workflow manually from the Actions tab on GitHub.
     workflow_dispatch:


   # Allow this job to clone the repo and create a page deployment
   permissions:
     contents: read
     pages: write
     id-token: write


   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout your repository using git
           uses: actions/checkout@v5
         - name: Install, build, and upload your site
           uses: withastro/action@v5
           # with:
             # path: . # The root location of your Astro project inside the repository. (optional)
             # node-version: 24 # The specific version of Node that should be used to build your site. Defaults to 22. (optional)
             # package-manager: pnpm@latest # The Node package manager that should be used to install dependencies and build your site. Automatically detected based on your lockfile. (optional)
             # build-cmd: pnpm run build # The command to run to build your site. Runs the package build script/task by default. (optional)
           # env:
             # PUBLIC_POKEAPI: 'https://pokeapi.co/api/v2' # Use single quotation marks for the variable value. (optional)


     deploy:
       needs: build
       runs-on: ubuntu-latest
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       steps:
         - name: Deploy to GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v4
   ```

   The Astro action can be configured with optional inputs. Provide these by uncommenting the `with:` line and the input you want to use.

   If your site requires any public environment variables, uncomment the `env:` line and add them there. (See the [GitHub documentation on setting secrets](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/store-information-in-variables#creating-configuration-variables-for-a-repository) for adding private environment variables.)

   Caution

   The official Astro [action](https://github.com/withastro/action) scans for a lockfile to detect your preferred package manager (`npm`, `yarn`, `pnpm`, or `bun`). You should commit your package manager’s automatically generated `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, or `bun.lockb` file to your repository.

2. In your Astro config file, set [`site`](/en/reference/configuration-reference/#site) to the GitHub URL of your deployed site.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config'


   export default defineConfig({
   +  site: 'https://astronaut.github.io',
   })
   ```

   The value for `site` must be one of the following:

   * The following URL based on your username: `https://<username>.github.io`
   * The random URL autogenerated for a [GitHub Organization’s private page](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site): `https://<random-string>.pages.github.io/`

3. In `astro.config.mjs`, configure a value for [`base`](/en/reference/configuration-reference/#base) (usually required).

   GitHub Pages will publish your website at an address that depends on both your username and your repository name (e.g. `https://<username>/github.io/<my-repo>/`). Set a value for `base` that specifies the repository for your website. This is so that Astro understands your website’s root is `/my-repo`, rather than the default `/`. You can skip this if your repository name matches the special `<username>.github.io` pattern (e.g. `https://github.com/username/username.github.io/`)

   Configure `base` as the repository’s name starting with a forward slash ( e.g. `/my-repo`):

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config'


   export default defineConfig({
   +  site: 'https://astronaut.github.io',
   +  base: '/my-repo',
   })
   ```

   Internal links with `base` configured

   When this value is configured, all of your internal page links must be prefixed with your `base` value:

   ```astro
   <a href="/my-repo/about">About</a>
   ```

   See more about [configuring a `base` value](/en/reference/configuration-reference/#base).

4. On GitHub, go to your repository’s **Settings** tab and find the **Pages** section of the settings.

5. Choose **GitHub Actions** as the **Source** of your site.

When you push changes to your Astro project’s repository, the GitHub Action will automatically deploy them for you at your GitHub URL.

## Change your GitHub URL to a custom domain

[Section titled “Change your GitHub URL to a custom domain”](#change-your-github-url-to-a-custom-domain)

Once your Astro project is [deployed to GitHub pages at a GitHub URL](#how-to-deploy) following the previous instructions, you can configure a custom domain. This means that users can visit your site at your custom domain `https://example.com` instead of `https://<username>.github.io`.

1. [Configure DNS for your domain provider](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain).

2. Add a `./public/CNAME` record to your project.

   Create the following file in your `public/` folder with a single line of text that specifies your custom domain:

   public/CNAME

   ```js
   sub.example.com
   ```

   This will deploy your site at your custom domain instead of `user.github.io`.

3. In your Astro config, update the value for `site` with your custom domain. Do not set a value for `base`, and remove one if it exists:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config'


   export default defineConfig({
   +  site: 'https://example.com',
   -  base: '/my-repo'
   })
   ```

4. If necessary, update all your page internal links to remove the `base` prefix:

   ```astro
   <a href="/my-repo/about">About</a>
   ```

## Examples

[Section titled “Examples”](#examples)

* [Github Pages Deployment starter template](https://github.com/hkbertoson/github-pages)
* [Starlight Flexoki Theme (production site)](https://delucis.github.io/starlight-theme-flexoki/)
* [Expressive Code Color Chips (production site)](https://delucis.github.io/expressive-code-color-chips/)
* [Starlight Markdown Blocks (production site)](https://delucis.github.io/starlight-markdown-blocks/)

# Deploy your Astro Site to GitLab Pages

> How to deploy your Astro site to the web using GitLab Pages.

You can use [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) to host an Astro site for your [GitLab](https://about.gitlab.com/) projects, groups, or user account.

Looking for an example?

Check out [the official GitLab Pages Astro example project](https://gitlab.com/pages/astro)!

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy an Astro site to GitLab Pages by using GitLab CI/CD to automatically build and deploy your site. To do this, your source code must be hosted on GitLab and you need to make the following changes to your Astro project:

1. Set up [`site`](/en/reference/configuration-reference/#site) and [`base`](/en/reference/configuration-reference/#base) options in `astro.config.mjs`.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';


   export default defineConfig({
   +  site: 'https://<username>.gitlab.io',
   +  base: '/<my-repo>',
     outDir: 'public',
     publicDir: 'static',
   });
   ```

   `site`

   The value for `site` must be one of the following:

   * The following URL based on your username: `https://<username>.gitlab.io`
   * The following URL based on your group name: `https://<groupname>.gitlab.io`
   * Your custom domain if you have it configured in your GitLab project’s settings: `https://example.com`

   For GitLab self-managed instances, replace `gitlab.io` with your instance’s Pages domain.

   `base`

   A value for `base` may be required so that Astro will treat your repository name (e.g. `/my-repo`) as the root of your website.

   Note

   Don’t set a `base` parameter if your page is served from the root folder.

   The value for `base` should be your repository’s name starting with a forward slash, for example `/my-blog`. This is so that Astro understands your website’s root is `/my-repo`, rather than the default `/`.

   Caution

   When this value is configured, all of your internal page links must be prefixed with your `base` value:

   ```astro
   <a href="/my-repo/about">About</a>
   ```

   See more about [configuring a `base` value](/en/reference/configuration-reference/#base)

2. Rename the `public/` directory to `static/`.

3. Set `outDir: 'public'` in `astro.config.mjs`. This setting instructs Astro to put the static build output in a folder called `public`, which is the folder required by GitLab Pages for exposed files.

   If you were using the [`public/` directory](/en/basics/project-structure/#public) as a source of static files in your Astro project, rename it and use that new folder name in `astro.config.mjs` for the value of `publicDir`.

   For example, here are the correct `astro.config.mjs` settings when the `public/` directory is renamed to `static/`:

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';


   export default defineConfig({
   +  outDir: 'public',
   +  publicDir: 'static',
   });
   ```

4. Change the build output in `.gitignore`. In our example we need to change `dist/` to `public/`:

   .gitignore

   ```diff
   # build output
   dist/
   public/
   ```

5. Create a file called `.gitlab-ci.yml` in the root of your project with the content below. This will build and deploy your site whenever you make changes to your content:

   .gitlab-ci.yml

   ```yaml
   pages:
     # The Docker image that will be used to build your app
     image: node:lts


     before_script:
       - npm ci


     script:
       # Specify the steps involved to build your app here
       - npm run build


     artifacts:
       paths:
         # The folder that contains the built files to be published.
         # This must be called "public".
         - public


     only:
       # Trigger a new build and deploy only when there is a push to the
       # branch(es) below
       - main
   ```

6. Commit your changes and push them to GitLab.

7. On GitLab, go to your repository’s **Deploy** menu and select **Pages**. Here you will see the full URL of your GitLab Pages website. To make sure you are using the URL format `https://username.gitlab.io/my-repo`, uncheck the **Use unique domain** setting on this page.

Your site should now be published! When you push changes to your Astro project’s repository, the GitLab CI/CD pipeline will automatically deploy them for you.

# Deploy your Astro Site to Google Cloud

> How to deploy your Astro site to the web using Google Cloud.

[Google Cloud](https://cloud.google.com/) is a full-featured web app hosting platform that can be used to deploy an Astro site.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

### Cloud Storage (static only)

[Section titled “Cloud Storage (static only)”](#cloud-storage-static-only)

1. [Create a new GCP project](https://console.cloud.google.com/projectcreate), or select one you already have.

2. Create a new bucket under [Cloud Storage](https://cloud.google.com/storage).

3. Give it a name and the other required settings.

4. Upload your `dist` folder into it or upload using [Cloud Build](https://cloud.google.com/build).

5. Enable public access by adding a new permission to `allUsers` called `Storage Object Viewer`.

6. Edit the website configuration and add `ìndex.html` as the entrypoint and `404.html` as the error page.

### Cloud Run (SSR and static)

[Section titled “Cloud Run (SSR and static)”](#cloud-run-ssr-and-static)

Cloud Run is a serverless platform that allows you to run a container without having to manage any infrastructure. It can be used to deploy both static and SSR sites.

#### Prepare the Service

[Section titled “Prepare the Service”](#prepare-the-service)

1. [Create a new GCP project](https://console.cloud.google.com/projectcreate), or select one you already have.

2. Make sure the [Cloud Run API](https://console.cloud.google.com/apis/library/run.googleapis.com) is enabled.

3. Create a new service.

#### Create Dockerfile & Build the Container

[Section titled “Create Dockerfile & Build the Container”](#create-dockerfile--build-the-container)

Before you can deploy your Astro site to Cloud Run, you need to create a Dockerfile that will be used to build the container. Find more information about [how to use Docker with Astro](/en/recipes/docker/#creating-a-dockerfile) in our recipe section.

Once the Dockerfile is created, build it into an image and push it to Google Cloud. There are a few ways to accomplish this:

**Build locally using Docker**:

Use the `docker build` command to build the image, `docker tag` to give it a tag, then `docker push` to push it to a registry. In the case of Google Cloud, [`Artifact Registry`](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling) is the easiest option, but you can also use [Docker Hub](https://hub.docker.com/).

```bash
# build your container
docker build .


docker tag SOURCE_IMAGE HOSTNAME/PROJECT-ID/TARGET-IMAGE:TAG


# Push your image to a registry
docker push HOSTNAME/PROJECT-ID/IMAGE:TAG
```

Change the following values in the commands above to match your project:

* `SOURCE_IMAGE`: the local image name or image ID.
* `HOSTNAME`: the registry host (`gcr.io`, `eu.gcr.io`, `asia.gcr.io`, `us.gcr.io`, `docker.io`).
* `PROJECT`: your Google Cloud project ID.
* `TARGET-IMAGE`: the name for the image when it’s stored in the registry.
* `TAG` is the version associated with the image.

[Read more in the Google Cloud docs.](https://cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling)

**Using another tool**:

You can use a CI/CD tool that supports Docker, like [GitHub Actions](https://github.com/marketplace/actions/push-to-gcr-github-action).

**Build using [Cloud Build](https://cloud.google.com/build)**:

Instead of building the Dockerfile locally, you can instruct Google Cloud to build the image remotely. See the [Google Cloud Build documentation here](https://cloud.google.com/build/docs/build-push-docker-image).

#### Deploying the container

[Section titled “Deploying the container”](#deploying-the-container)

Deployment can be handled manually in your terminal [using `gcloud`](https://cloud.google.com/run/docs/deploying#service) or automatically using [Cloud Build](https://cloud.google.com/build) or any other CI/CD system.

Need public access?

Don’t forget to add the permission `Cloud Run Invoker` to the `allUsers` group in the Cloud Run permissions settings!

# Deploy your Astro Site to Google’s Firebase Hosting

> How to deploy your Astro site to the web using Google’s Firebase Hosting.

[Firebase Hosting](https://firebase.google.com/products/hosting) is a service provided by Google’s [Firebase](https://firebase.google.com/) app development platform, which can be used to deploy an Astro site.

See our separate guide for [adding Firebase backend services](/en/guides/backend/google-firebase/) such as databases, authentication, and storage.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Firebase as a static site, or as a server-side rendered site (SSR).

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Firebase.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Firebase add the [Node.js adapter](/en/guides/integrations-guide/node/).

Note

Deploying an SSR Astro site to Firebase requires the [Blaze plan](https://firebase.google.com/pricing) or higher.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install the [Firebase CLI](https://github.com/firebase/firebase-tools). This is a command-line tool that allows you to interact with Firebase from the terminal.

   * npm

     ```shell
     npm install firebase-tools
     ```

   * pnpm

     ```shell
     pnpm add firebase-tools
     ```

   * Yarn

     ```shell
     yarn add firebase-tools
     ```

2. Authenticate the Firebase CLI with your Google account. This will open a browser window where you can log in to your Google account.

   * npm

     ```shell
     npx firebase login
     ```

   * pnpm

     ```shell
     pnpm exec firebase login
     ```

   * Yarn

     ```shell
     yarn firebase login
     ```

3. Enable experimental web frameworks support. This is an experimental feature that allows the Firebase CLI to detect and configure your deployment settings for Astro.

   * npm

     ```shell
     npx firebase experiments:enable webframeworks
     ```

   * pnpm

     ```shell
     pnpm exec firebase experiments:enable webframeworks
     ```

   * Yarn

     ```shell
     yarn firebase experiments:enable webframeworks
     ```

4. Initialize Firebase Hosting in your project. This will create a `firebase.json` and `.firebaserc` file in your project root.

   * npm

     ```shell
     npx firebase init hosting
     ```

   * pnpm

     ```shell
     pnpm exec firebase init hosting
     ```

   * Yarn

     ```shell
     yarn firebase init hosting
     ```

5. Deploy your site to Firebase Hosting. This will build your Astro site and deploy it to Firebase.

   * npm

     ```shell
     npx firebase deploy --only hosting
     ```

   * pnpm

     ```shell
     pnpm exec firebase deploy --only hosting
     ```

   * Yarn

     ```shell
     yarn firebase deploy --only hosting
     ```

# Deploy your Astro Site to Heroku

> How to deploy your Astro site to the web using Heroku.

[Heroku](https://www.heroku.com/) is a platform-as-a-service for building, running, and managing modern apps in the cloud. You can deploy an Astro site to Heroku using this guide.

Danger

The following instructions use [the deprecated `heroku-static-buildpack`](https://github.com/heroku/heroku-buildpack-static#warning-heroku-buildpack-static-is-deprecated). Please see [Heroku’s documentation for using `heroku-buildpack-nginx`](https://github.com/dokku/heroku-buildpack-nginx) instead.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

2. Create a Heroku account by [signing up](https://signup.heroku.com/).

3. Run `heroku login` and fill in your Heroku credentials:

   ```bash
   $ heroku login
   ```

4. Create a file called `static.json` in the root of your project with the below content:

   static.json

   ```json
   {
     "root": "./dist"
   }
   ```

   This is the configuration of your site; read more at [heroku-buildpack-static](https://github.com/heroku/heroku-buildpack-static).

5. Set up your Heroku git remote:

   ```bash
   # version change
   $ git init
   $ git add .
   $ git commit -m "My site ready for deployment."


   # creates a new app with a specified name
   $ heroku apps:create example


   # set buildpack for static sites
   $ heroku buildpacks:set https://github.com/heroku/heroku-buildpack-static.git
   ```

6. Deploy your site:

   ```bash
   # publish site
   $ git push heroku master


   # opens a browser to view the Dashboard version of Heroku CI
   $ heroku open
   ```

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
```

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
```

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
```

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

# Deploy your Astro Site to Microsoft Azure

> How to deploy your Astro site to the web using Microsoft Azure.

[Azure](https://azure.microsoft.com/) is a cloud platform from Microsoft. You can deploy your Astro site with Microsoft Azure’s [Static Web Apps](https://aka.ms/staticwebapps) service.

This guide takes you through deploying your Astro site stored in GitHub using Visual Studio Code. Please see Microsoft guides for using an [Azure Pipelines Task](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/azure-static-web-app-v0?view=azure-pipelines) for other setups.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To follow this guide, you will need:

* An Azure account and a subscription key. You can create a [free Azure account here](https://azure.microsoft.com/free).
* Your app code pushed to [GitHub](https://github.com/).
* The [SWA Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps) in [Visual Studio Code](https://code.visualstudio.com/).

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Open your project in VS Code.

2. Open the Static Web Apps extension, sign in to Azure, and click the **+** button to create a new Static Web App. You will be prompted to designate which subscription key to use.

3. Follow the wizard started by the extension to give your app a name, choose a framework preset, and designate the app root (usually `/`) and built file location (use `/dist`). Astro is not listed in the built-in templates in Azure so you will need to select `custom`. The wizard will run and will create a [GitHub Action](https://github.com/features/actions) in the `.github` folder of your repo. (This folder will be automatically created if it does not already exist.)

The GitHub Action will deploy your app (you can see its progress in your repo’s Actions tab on GitHub). When successfully completed, you can view your app at the address shown in the SWA Extension’s progress window by clicking the **Browse Website** button (this will appear after the GitHub Action has run).

## Known Issues

[Section titled “Known Issues”](#known-issues)

The GitHub action yaml that is created for you assumes the use of node 14. This means the Astro build fails. To resolve this update your projects package.json file with this snippet.

```plaintext
  "engines": {
    "node": ">=18.0.0"
  },
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Microsoft Azure Static Web Apps documentation](https://learn.microsoft.com/en-us/azure/static-web-apps/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Deploying an Astro Website to Azure Static Web Apps](https://www.blueboxes.co.uk/deploying-an-astro-website-to-azure-static-web-apps)
* [Deploying a Static Astro Site to Azure Static Web Apps using GitHub Actions](https://agramont.net/blog/create-static-site-astro-azure-ssg/#automate-deployment-with-github-actions)
* [Astro site deployment to Azure Static Web Apps with the CLI from GitHub Actions](https://www.eliostruyf.com/deploy-astro-azure-static-web-apps-github-cli/)

# Deploy your Astro Site to Netlify

> How to deploy your Astro site to the web on Netlify.

[Netlify](https://netlify.com) offers hosting and serverless backend services for web applications and static websites. Any Astro site can be hosted on Netlify!

This guide includes instructions for deploying to Netlify through the website UI or Netlify’s CLI.

## Project configuration

[Section titled “Project configuration”](#project-configuration)

Your Astro project can be deployed to Netlify in three different ways: as a static site, a server-rendered site, or an edge-rendered site.

### Static site

[Section titled “Static site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Netlify.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

Add [the Netlify adapter](/en/guides/integrations-guide/netlify/) to enable on-demand rendering in your Astro project and deploy to Netlify with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

```bash
npx astro add netlify
```

See the [Netlify adapter guide](/en/guides/integrations-guide/netlify/) to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Netlify’s Edge Functions.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Netlify through the website UI or using Netlify’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment

[Section titled “Website UI deployment”](#website-ui-deployment)

If your project is stored in GitHub, GitLab, BitBucket, or Azure DevOps, you can use the Netlify website UI to deploy your Astro site.

1. Click `Add a new site` in your [Netlify dashboard](https://app.netlify.com/)

2. Choose `Import an existing project`

   When you import your Astro repository from your Git provider, Netlify should automatically detect and pre-fill the correct configuration settings for you.

3. Make sure that the following settings are entered, then press the `Deploy` button:

   * **Build Command:** `astro build` or `npm run build`
   * **Publish directory:** `dist`

   After deploying, you will be redirected to the site overview page. There, you can edit the details of your site.

Any future changes to your source repository will trigger preview and production deploys based on your deployment configuration.

#### `netlify.toml` file

[Section titled “netlify.toml file”](#netlifytoml-file)

You can optionally create a new `netlify.toml` file at the top level of your project repository to configure your build command and publish directory, as well as other project settings including environment variables and redirects. Netlify will read this file and automatically configure your deployment.

To configure the default settings, create a `netlify.toml` file with the following contents:

```toml
[build]
  command = "npm run build"
  publish = "dist"
```

More info at [“Deploying an existing Astro Git repository”](https://www.netlify.com/blog/how-to-deploy-astro/#deploy-an-existing-git-repository-to-netlify) on Netlify’s blog

### CLI deployment

[Section titled “CLI deployment”](#cli-deployment)

You can also create a new site on Netlify and link up your Git repository by installing and using the [Netlify CLI](https://cli.netlify.com/).

1. Install Netlify’s CLI globally

   ```bash
   npm install --global netlify-cli
   ```

2. Run `netlify login` and follow the instructions to log in and authorize Netlify

3. Run `netlify init` and follow the instructions

4. Confirm your build command (`astro build`)

   The CLI will automatically detect the build settings (`astro build`) and deploy directory (`dist`), and will offer to automatically generate [a `netlify.toml` file](#netlifytoml-file) with those settings.

5. Build and deploy by pushing to Git

   The CLI will add a deploy key to the repository, which means your site will be automatically rebuilt on Netlify every time you `git push`.

More details from Netlify on [Deploy an Astro site using the Netlify CLI](https://www.netlify.com/blog/how-to-deploy-astro/#link-your-astro-project-and-deploy-using-the-netlify-cli)

### Set a Node.js version

[Section titled “Set a Node.js version”](#set-a-nodejs-version)

If you are using a legacy [build image](https://docs.netlify.com/configure-builds/get-started/#build-image-selection) (Xenial) on Netlify, make sure that your Node.js version is set. Astro requires `v18.20.8` or `v20.3.0` or higher.

You can [specify your Node.js version in Netlify](https://docs.netlify.com/configure-builds/manage-dependencies/#node-js-and-javascript) using:

* a [`.nvmrc`](https://github.com/nvm-sh/nvm#nvmrc) file in your base directory.
* a `NODE_VERSION` environment variable in your site’s settings using the Netlify project dashboard.

## Using Netlify Functions

[Section titled “Using Netlify Functions”](#using-netlify-functions)

No special configuration is required to use Netlify Functions with Astro. Add a `netlify/functions` directory to your project root and follow [the Netlify Functions documentation](https://docs.netlify.com/functions/overview/) to get started!

## Examples

[Section titled “Examples”](#examples)

* [Deploy An Astro site with Forms, Serverless Functions, and Redirects](https://www.netlify.com/blog/deploy-an-astro-site-with-forms-serverless-functions-and-redirects/) — Netlify Blog
* [Deployment Walkthrough Video](https://youtu.be/GrSLYq6ZTes) — Netlify YouTube channel

# Deploy your Astro Site with Railway

> How to deploy your Astro site using the Railway web interface.

[Railway](https://railway.com?utm_medium=integration\&utm_source=button\&utm_campaign=astro) is a deployment platform built to simplify your infrastructure stack from servers to observability with a unified developer experience.

This guide is for deploying an Astro static site to Railway using either the web interface or Railway CLI tool.

Tip

To deploy an Astro site with on-demand rendering (SSR) using the Node adapter, you can follow [Railway’s guide to deploying an Astro site](https://docs.railway.com/guides/astro?utm_medium=integration\&utm_source=button\&utm_campaign=astro).

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Railway’s default build system, [Railpack](https://docs.railway.com/reference/railpack), automatically builds your Astro project as a static site.

## Deploy via a Railway template

[Section titled “Deploy via a Railway template”](#deploy-via-a-railway-template)

If you do not already have an Astro project, and are starting from scratch:

1. Go to the Astro template on Railway: [railway.com/deploy/astro-starter](https://railway.com/deploy/astro-starter?utm_medium=integration\&utm_source=docs\&utm_campaign=astro).

2. Click “Deploy Now” and sign in with your GitHub account to authorize Railway. This will deploy the Astro template into your new Railway account.

3. Eject the service code into your own Github repository by following [this guide](https://docs.railway.com/guides/deploy#eject-from-template-repository?utm_medium=integration\&utm_source=docs\&utm_campaign=astro). This will allow you to keep the repo deployed but customize it with your own code.

## Deploy via the web interface

[Section titled “Deploy via the web interface”](#deploy-via-the-web-interface)

If you have an existing Astro project you would like to deploy but not a Railway account yet:

1. Create a [Railway account](https://railway.com/dashboard) and sign in.

2. From the Railway dashboard, create a new [project](https://docs.railway.com/guides/projects).

3. Select the option to deploy from a GitHub repository, and select your Astro project.

4. Generate or add a custom domain from your project’s [network settings](https://docs.railway.com/guides/public-networking#railway-provided-domain).

## Deploy via Railway CLI

[Section titled “Deploy via Railway CLI”](#deploy-via-railway-cli)

If you have an existing Astro project you would like to deploy and an existing Railway account:

1. [Install](https://docs.railway.com/guides/cli#installing-the-cli) the Railway CLI tool.

2. Login with the command `railway login`.

3. From within your Astro project, run `railway init` and choose a workspace and project name.

4. Run `railway up` to deploy your project on Railway.

5. Run `railway domain` to generate a Railway provided service domain.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Railway guide to deploying an Astro app](https://docs.railway.com/guides/astro?utm_medium=integration\&utm_source=docs\&utm_campaign=astro)
* [Railway Astro starter template](https://railway.com/deploy/astro-starter?utm_medium=integration\&utm_source=docs\&utm_campaign=astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

[How to host an Astro site on Railway](https://jacksmith.xyz/blog/how-to-host-astro-site-on-railway)

# Deploy your Astro Site to Render

> How to deploy your Astro site to the web using Render.

You can deploy your Astro project to [Render](https://render.com/), a service to build websites with free TLS certificates, a global CDN, DDoS protection, private networks, and auto deploys from Git.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Create a [render.com account](https://dashboard.render.com/) and sign in

2. Click the **New +** button from your dashboard and select **Static Site**

3. Connect your [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/) repository or alternatively enter the public URL of a public repository

4. Give your website a name, select the branch and specify the build command and publish directory

   * **Build Command:** `npm run build`
   * **Publish Directory:** `dist`, for static sites; `dist/client` if you have any pages rendered on demand.

5. Click the **Create Static Site** button

# Deploy your Astro Site to Seenode

> How to deploy your Astro site to the web on Seenode.

[Seenode](https://seenode.com) is a deployment platform for building and deploying web applications with databases, built-in observability, and auto-scaling. Astro sites can be deployed to Seenode using server-side rendering (SSR).

This guide includes instructions for deploying to Seenode through the web interface.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable on-demand rendering in your Astro project and deploy to Seenode, add [the Node.js adapter](/en/guides/integrations-guide/node/) with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

* npm

  ```shell
  npx astro add node
  ```

* pnpm

  ```shell
  pnpm astro add node
  ```

* Yarn

  ```shell
  yarn astro add node
  ```

After installing the adapter, update your `astro.config.mjs` to configure the server for Seenode’s requirements:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';


export default defineConfig({
  output: 'server',
+  adapter: node({
+    mode: 'standalone'
+  }),
+  server: {
+    port: process.env.NODE_ENV === 'production' ? (Number(process.env.PORT) || 80) : 4321,
+    host: true
  }
});
```

Update your `package.json` to include a start script that runs the built server:

package.json

```diff
{
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    +"start": "NODE_ENV=production node ./dist/server/entry.mjs"
  }
}
```

See [Seenode’s Astro deployment guide](https://seenode.com/docs/frameworks/javascript/astro/) for more configuration options and troubleshooting.

## How to Deploy

[Section titled “How to Deploy”](#how-to-deploy)

You can deploy to Seenode through the web interface by connecting your Git repository.

### Web Interface Deployment

[Section titled “Web Interface Deployment”](#web-interface-deployment)

1. Create a [Seenode account](https://cloud.seenode.com) and sign in.

2. Push your code to your Git repository (GitHub or GitLab).

3. From the [Seenode Dashboard](https://cloud.seenode.com/dashboard/applications/web/create), create a new **Web Service** and connect your repository.

4. Seenode will automatically detect your Astro project. Configure the deployment settings:

   * **Build Command:** `npm ci && npm run build` (or use `pnpm` / `yarn` equivalents)
   * **Start Command:** `npm start`
   * **Port:** `80` (required for web services)

5. Select your preferred instance size and click **Create Web Service**.

6. Your application will be built and deployed. Once complete, you’ll receive a URL to access your live Astro site after which you can link your domain.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Seenode Cloud](https://cloud.seenode.com) — Seenode dashboard
* [Seenode Documentation](https://seenode.com/docs) — complete platform documentation
* [Seenode Astro Guide](https://seenode.com/docs/frameworks/javascript/astro/) — detailed deployment guide and troubleshooting
* [Seenode Astro Template](https://github.com/seenode/example-astro) — pre-configured starter template

# Deploy your Astro Site to AWS with SST

> How to deploy your Astro site to AWS with SST

You can deploy an Astro site to AWS using [SST](https://sst.dev), an open-source framework for deploying modern full-stack applications with SSG and SSR support.

You can also use any additional SST components like cron jobs, Buckets, Queues, etc while maintaining type-safety.

## Quickstart

[Section titled “Quickstart”](#quickstart)

1. Create an astro project.

2. Run `npx sst@latest init`.

3. It should detect that you are using Astro and ask you to confirm.

4. Once you’re ready for deployment you can run `npx sst deploy --stage production`.

You can also read [the full Astro on AWS with SST tutorial](https://sst.dev/docs/start/aws/astro) that will guide you through the steps.

### SST components

[Section titled “SST components”](#sst-components)

To use any [additional SST components](https://sst.dev/docs/), add them to `sst.config.ts`.

sst.config.ts

```ts
const bucket = new sst.aws.Bucket("MyBucket", {
  access: "public",
});
new sst.aws.Astro("MyWeb", {
  link: [bucket],
});
```

And then access them in your `.astro` file.

```astro
---
import { Resource } from "sst"
console.log(Resource.MyBucket.name)
---
```

Consult the [SST docs on linking resources](https://sst.dev/docs/linking) to learn more.

If you have any questions, you can [ask in the SST Discord](https://discord.gg/sst).

# Deploy your Astro Site to Stormkit

> Deploy your Astro site to Stormkit

You can deploy your Astro project to [Stormkit](https://stormkit.io/), a deployment platform for static websites, single-page applications (SPAs), and serverless functions.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. [Log in to Stormkit](https://app.stormkit.io/auth).

2. Using the user interface, import your Astro project from one of the three supported Git providers (GitHub, GitLab, or Bitbucket).

3. Navigate to the project’s production environment in Stormkit or create a new environment if needed.

4. Verify the build command in your [Stormkit configuration](https://stormkit.io/docs/deployments/configuration). By default, Stormkit CI will run `npm run build` but you can specify a custom build command on this page.

5. Click the “Deploy Now” button to deploy your site.

Read more in the [Stormkit Documentation](https://stormkit.io/docs).

# Deploy your Astro Site to Surge

> How to deploy your Astro site to the web using Surge

You can deploy your Astro project to [Surge](https://surge.sh/), a single-command web publishing platform designed for front-end developers.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. Install [the Surge CLI](https://www.npmjs.com/package/surge) globally from the terminal, if you haven’t already.

   ```shell
   npm install -g surge
   ```

2. Build your Astro site from your project’s root directory.

   ```shell
   npm run build
   ```

3. Deploy to Surge using the CLI.

   ```shell
   surge dist
   ```

   You can [use a custom domain with Surge](http://surge.sh/help/adding-a-custom-domain) when deploying by running `surge dist yourdomain.com`.

# Deploy your Astro Site to Vercel

> How to deploy your Astro site to the web on Vercel.

You can use [Vercel](http://vercel.com/) to deploy an Astro site to their global edge network with zero configuration.

This guide includes instructions for deploying to Vercel through the website UI or Vercel’s CLI.

## Project configuration

[Section titled “Project configuration”](#project-configuration)

Your Astro project can be deployed to Vercel as a static site, or a server-rendered site.

### Static site

[Section titled “Static site”](#static-site)

Your Astro project is a static site by default. You don’t need any extra configuration to deploy a static Astro site to Vercel.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

Add [the Vercel adapter](/en/guides/integrations-guide/vercel/) to enable [on-demand rendering](/en/guides/on-demand-rendering/) in your Astro project with the following `astro add` command. This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

* npm

  ```shell
  npx astro add vercel
  ```

* pnpm

  ```shell
  pnpm astro add vercel
  ```

* Yarn

  ```shell
  yarn astro add vercel
  ```

See the [Vercel adapter guide](/en/guides/integrations-guide/vercel/) to install manually instead, or for more configuration options, such as deploying your project’s Astro middleware using Vercel Edge Functions.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Vercel through the website UI or using Vercel’s CLI (command line interface). The process is the same for both static and on-demand rendered Astro sites.

### Website UI deployment

[Section titled “Website UI deployment”](#website-ui-deployment)

1. Push your code to your online Git repository (GitHub, GitLab, BitBucket).

2. [Import your project](https://vercel.com/new) into Vercel.

3. Vercel will automatically detect Astro and configure the right settings.

4. Your application is deployed! (e.g. [astro.vercel.app](https://astro.vercel.app/))

After your project has been imported and deployed, all subsequent pushes to branches will generate [Preview Deployments](https://vercel.com/docs/concepts/deployments/preview-deployments), and all changes made to the Production Branch (commonly “main”) will result in a [Production Deployment](https://vercel.com/docs/concepts/deployments/environments#production).

Learn more about Vercel’s [Git Integration](https://vercel.com/docs/concepts/git).

### CLI deployment

[Section titled “CLI deployment”](#cli-deployment)

1. Install the [Vercel CLI](https://vercel.com/cli) and run `vercel` to deploy.

   * npm

     ```shell
     npm install -g vercel
     vercel
     ```

   * pnpm

     ```shell
     pnpm add -g vercel
     vercel
     ```

   * Yarn

     ```shell
     yarn global add vercel
     vercel
     ```

2. Vercel will automatically detect Astro and configure the right settings.

3. When asked `Want to override the settings? [y/N]`, choose `N`.

4. Your application is deployed! (e.g. [astro.vercel.app](https://astro.vercel.app/))

### Project config with `vercel.json`

[Section titled “Project config with vercel.json”](#project-config-with-verceljson)

You can use `vercel.json` to override the default behavior of Vercel and to configure additional settings. For example, you may wish to attach headers to HTTP responses from your Deployments.

Learn more about [Vercel’s project configuration](https://vercel.com/docs/project-configuration).

# Deploy your Astro Site to Zeabur

> How to deploy your Astro site to the web on Zeabur.

[Zeabur](https://zeabur.com) offers hosting for full-stack web applications. Astro sites can be hosted as both SSR or static output.

This guide includes instructions for deploying to Zeabur through the website UI.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

### Static Site

[Section titled “Static Site”](#static-site)

Astro outputs a static site by default. There is no need for any extra configuration to deploy a static Astro site to Zeabur.

### Adapter for SSR

[Section titled “Adapter for SSR”](#adapter-for-ssr)

To enable SSR in your Astro project and deploy on Zeabur:

1. Install [the `@zeabur/astro-adapter` adapter](https://www.npmjs.com/package/@zeabur/astro-adapter) to your project’s dependencies using your preferred package manager. If you’re using npm or aren’t sure, run this in the terminal:

   ```bash
     npm install @zeabur/astro-adapter
   ```

2. Add two new lines to your `astro.config.mjs` project configuration file.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import zeabur from '@zeabur/astro-adapter/serverless';


   export default defineConfig({
   +  output: 'server',
   +  adapter: zeabur(),
   });
   ```

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy your Astro site to Zeabur if the project is stored in GitHub.

1. Click `Create new project` in the [Zeabur dashboard](https://dash.zeabur.com).

2. Configure GitHub installation and import the repository.

3. Zeabur will automatically detect that your project is an Astro project and will build it using the `astro build` command.

4. Once the build is complete, you can bind a domain to your site and visit it.

After your project has been imported and deployed, all subsequent pushes to branches will generate new builds.

Learn more about Zeabur’s [Deployment Guide](https://zeabur.com/docs/get-started/).

# Deploy your Astro Site to Zephyr Cloud

> How to deploy your Astro site to the web using Zephyr Cloud.

You can use [Zephyr Cloud](https://zephyr-cloud.io) to deploy an Astro site with intelligent asset management, comprehensive build analytics, and first-class support for Module Federation architectures.

Zephyr operates on a **Bring Your Own Cloud (BYOC)** model, deploy to your choice of [supported clouds](https://docs.zephyr-cloud.io/cloud) through a unified interface without vendor lock-in. Switch providers anytime without changing your deployment workflow.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

### Automatic Installation

[Section titled “Automatic Installation”](#automatic-installation)

1. Add the Zephyr integration to your Astro project with the following command. This will install the integration and update your `astro.config.mjs` file automatically:

   * npm

     ```shell
     npx with-zephyr@latest
     ```

   * pnpm

     ```shell
     pnpm dlx with-zephyr@latest
     ```

   * Yarn

     ```shell
     yarn dlx with-zephyr@latest
     ```

2. Build and deploy your Astro site:

   * npm

     ```shell
     npm run build
     ```

   * pnpm

     ```shell
     pnpm run build
     ```

   * Yarn

     ```shell
     yarn run build
     ```

3. Your application is deployed! Zephyr will provide a deployment URL and comprehensive build analytics.

### Manual Installation

[Section titled “Manual Installation”](#manual-installation)

1. Install the Zephyr Astro integration:

   * npm

     ```shell
     npm install zephyr-astro-integration
     ```

   * pnpm

     ```shell
     pnpm add zephyr-astro-integration
     ```

   * Yarn

     ```shell
     yarn add zephyr-astro-integration
     ```

2. Add the integration to your `astro.config.mjs`:

   ```js
   import { defineConfig } from 'astro/config';
   import { withZephyr } from 'zephyr-astro-integration';


   export default defineConfig({
     integrations: [
       withZephyr(),
     ],
   });
   ```

3. Build and deploy your Astro site:

   * npm

     ```shell
     npm run build
     ```

   * pnpm

     ```shell
     pnpm run build
     ```

   * Yarn

     ```shell
     yarn run build
     ```

4. Your application is deployed! Zephyr will provide a deployment URL and comprehensive build analytics.

### More details

[Section titled “More details”](#more-details)

For more detailed information refer to the [Zephyr Cloud documentation on deploying with Astro](https://docs.zephyr-cloud.io/meta-frameworks/astro).

## What happens during deployment

[Section titled “What happens during deployment”](#what-happens-during-deployment)

When you build your Astro site with the Zephyr integration, the following process occurs:

1. **Build Context Extraction**: Zephyr captures Git information (commit, branch, author) and package metadata
2. **Asset Hashing**: All build outputs are hashed using SHA-256 for content-addressable storage
3. **Delta Detection**: Zephyr queries the CDN edge to identify which assets already exist
4. **Optimized Upload**: Only new or modified assets are uploaded
5. **Snapshot Creation**: An immutable deployment snapshot is created with all asset references
6. **Analytics Upload**: Build statistics, module graphs, and dependency information are sent to the dashboard
7. **CDN Deployment**: Assets are published to your configured CDN with permanent cache headers

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Zephyr Cloud Documentation](https://docs.zephyr-cloud.io)
* [Zephyr Astro Integration on GitHub](https://github.com/ZephyrCloudIO/zephyr-packages/tree/main/libs/zephyr-astro-integration)
* [Zephyr Cloud Platform](https://zephyr-cloud.io)

# Deploy your Astro Site to Zerops

> How to deploy your Astro site to the web using Zerops.

[Zerops](https://zerops.io/) is a dev-first cloud platform that can be used to deploy both Static and SSR Astro site.

This guide will walk you through setting up and deploying both Static and SSR Astro sites on Zerops.

Astro x Zerops Quickrun

Want to test running Astro on Zerops without installing or setting up anything? Using repositories [Zerops x Astro - Static](https://github.com/zeropsio/recipe-astro-static) or [Zerops x Astro - SSR on Node.js](https://github.com/zeropsio/recipe-astro-nodejs) you can deploy example Astro site with a single click.

Running apps on Zerops requires two steps:

1. Creating a project
2. Triggering build & deploy pipeline

Note

One Zerops project can contain multiple Astro sites.

## Astro Static site on Zerops

[Section titled “Astro Static site on Zerops”](#astro-static-site-on-zerops)

### Creating a project and a service for Astro Static

[Section titled “Creating a project and a service for Astro Static”](#creating-a-project-and-a-service-for-astro-static)

Projects and services can be added either through a [`Project add`](https://app.zerops.io/dashboard/project-add) wizard or imported using a yaml structure:

```yaml
# see https://docs.zerops.io/references/import for full reference
project:
  name: recipe-astro
services:
  - hostname: app
    type: static
```

This will create a project called `recipe-astro` with a Zerops Static service called `app`.

### Deploying your Astro Static site

[Section titled “Deploying your Astro Static site”](#deploying-your-astro-static-site)

To tell Zerops how to build and run your site, add a `zerops.yml` to your repository:

* npm

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - npm i
          - npm build
        deployFiles:
          - dist/~
      run:
        base: static
  ```

* pnpm

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - pnpm i
          - pnpm build
        deployFiles:
          - dist/~
      run:
        base: static
  ```

* Yarn

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - yarn
          - yarn build
        deployFiles:
          - dist/~
      run:
        base: static
  ```

Now you can [trigger the build & deploy pipeline using the Zerops CLI](#trigger-the-pipeline-using-zerops-cli-zcli) or by connecting the `app` service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## Astro SSR site on Zerops

[Section titled “Astro SSR site on Zerops”](#astro-ssr-site-on-zerops)

### Update scripts

[Section titled “Update scripts”](#update-scripts)

Update your `start` script to run the server output from the Node adapter.

package.json

```json
"scripts": {
  "start": "node ./dist/server/entry.mjs",
}
```

### Creating a project and a service for Astro SSR (Node.js)

[Section titled “Creating a project and a service for Astro SSR (Node.js)”](#creating-a-project-and-a-service-for-astro-ssr-nodejs)

Projects and services can be added either through a [`Project add`](https://app.zerops.io/dashboard/project-add) wizard or imported using a yaml structure:

```yaml
# see https://docs.zerops.io/references/import for full reference
project:
  name: recipe-astro
services:
  - hostname: app
    type: nodejs@20
```

This will create a project called `recipe-astro` with Zerops Node.js service called `app`.

### Deploying your Astro SSR site

[Section titled “Deploying your Astro SSR site”](#deploying-your-astro-ssr-site)

To tell Zerops how to build and run your site using the official [Astro Node.js adapter](/en/guides/integrations-guide/node/) in `standalone` mode, add a `zerops.yml` file to your repository:

* npm

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - npm i
          - npm run build
        deployFiles:
          - dist
          - package.json
          - node_modules
      run:
        base: nodejs@20
        ports:
          - port: 3000
            httpSupport: true
        envVariables:
          PORT: 3000
          HOST: 0.0.0.0
        start: npm start
  ```

* pnpm

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - pnpm i
          - pnpm run build
        deployFiles:
          - dist
          - package.json
          - node_modules
      run:
        base: nodejs@20
        ports:
          - port: 3000
            httpSupport: true
        envVariables:
          PORT: 3000
          HOST: 0.0.0.0
        start: pnpm start
  ```

* Yarn

  zerops.yml

  ```yaml
  # see https://docs.zerops.io/zerops-yml/specification for full reference
  zerops:
    - setup: app
      build:
        base: nodejs@20
        buildCommands:
          - yarn
          - yarn build
        deployFiles:
          - dist
          - package.json
          - node_modules
      run:
        base: nodejs@20
        ports:
          - port: 3000
            httpSupport: true
        envVariables:
          PORT: 3000
          HOST: 0.0.0.0
        start: yarn start
  ```

Now you can [trigger the build & deploy pipeline using the Zerops CLI](#trigger-the-pipeline-using-zerops-cli-zcli) or by connecting the `app` service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## Trigger the pipeline using Zerops CLI (zcli)

[Section titled “Trigger the pipeline using Zerops CLI (zcli)”](#trigger-the-pipeline-using-zerops-cli-zcli)

1. Install the Zerops CLI.

   ```shell
   # To download the zcli binary directly,
   # use https://github.com/zeropsio/zcli/releases
   npm i -g @zerops/zcli
   ```

2. Open [`Settings > Access Token Management`](https://app.zerops.io/settings/token-management) in the Zerops app and generate a new access token.

3. Log in using your access token with the following command:

   ```shell
   zcli login <token>
   ```

4. Navigate to the root of your app (where `zerops.yml` is located) and run the following command to trigger the deploy:

   ```shell
   zcli push
   ```

## Resources

[Section titled “Resources”](#resources)

### Official

[Section titled “Official”](#official)

* [Create Zerops account](https://app.zerops.io/registration)
* [Zerops Documentation](https://docs.zerops.io)
* [Zerops Astro recipe](https://app.zerops.io/recipe/astro)

### Community

[Section titled “Community”](#community)

* [Deploying Astro to Zerops in 3 mins](https://medium.com/@arjunaditya/how-to-deploy-astro-to-zerops-4230816a62b4)
* [Deploying Astro SSG with Node.js on Zerops with One Click Deploy](https://youtu.be/-4KTa4VWtBE)
* [Deploying Astro SSR with Node.js on Zerops with One Click Deploy](https://youtu.be/eR6b_JnDH6g)

# Dev toolbar

> A guide to using the dev toolbar in Astro

While the dev server is running, Astro includes a dev toolbar at the bottom of every page in your local browser preview.

This toolbar includes a number of useful tools for debugging and inspecting your site during development and can be [extended with more dev toolbar apps](#extending-the-dev-toolbar) found in the integrations directory. You can even [build your own toolbar apps](/en/recipes/making-toolbar-apps/) using the [Dev Toolbar API](/en/reference/dev-toolbar-app-reference/)!

This toolbar is enabled by default and appears when you hover over the bottom of the page. It is a development tool only and will not appear on your published site.

## Built-in apps

[Section titled “Built-in apps”](#built-in-apps)

### Astro Menu

[Section titled “Astro Menu”](#astro-menu)

The Astro Menu app provides easy access to various information about the current project and links to extra resources. Notably, it provides one-click access to the Astro documentation, GitHub repository, and Discord server.

This app also includes a “Copy debug info” button which will run the [`astro info`](/en/reference/cli-reference/#astro-info) command and copy the output to your clipboard. This can be useful when asking for help or reporting issues.

### Inspect

[Section titled “Inspect”](#inspect)

The Inspect app provides information about any [islands](/en/concepts/islands/) on the current page. This will show you the properties passed to each island, and the client directive that is being used to render them.

### Audit

[Section titled “Audit”](#audit)

The Audit app automatically runs a series of audits on the current page, checking for the most common performance and accessibility issues. When an issue is found, a red dot will appear in the toolbar. Clicking on the app will pop up a list of results from the audit and will highlight the related elements directly in the page.

Note

The basic performance and accessibility audits performed by the dev toolbar are not a replacement for dedicated tools like [Pa11y](https://pa11y.org/) or [Lighthouse](https://developers.google.com/web/tools/lighthouse), or even better, humans!

The dev toolbar aims to provide a quick and easy way to catch common issues during development, without needing to context-switch to a different tool.

### Settings

[Section titled “Settings”](#settings)

The Settings app allows you to configure options for the dev toolbar, such as verbose logging, disabling notifications, and adjusting its placement on your screen.

## Extending the dev toolbar

[Section titled “Extending the dev toolbar”](#extending-the-dev-toolbar)

Astro integrations can add new apps to the dev toolbar, allowing you to extend it with custom tools that are specific to your project. You can find [more dev tool apps to install in the integrations directory](https://astro.build/integrations/?search=\&categories%5B%5D=toolbar) or using the [Astro Menu](#astro-menu).

Install additional dev toolbar app integrations in your project just like any other [Astro integration](/en/guides/integrations-guide/) according to its own installation instructions.

![](/houston_chef.webp) **Related recipe:** [Create a dev toolbar app](/en/recipes/making-toolbar-apps/)

## Disabling the dev toolbar

[Section titled “Disabling the dev toolbar”](#disabling-the-dev-toolbar)

The dev toolbar is enabled by default for every site. You can choose to disable it for individual projects and/or users as needed.

### Per-project

[Section titled “Per-project”](#per-project)

To disable the dev toolbar for everyone working on a project, set `devToolbar: false` in the [Astro config file](/en/reference/configuration-reference/#devtoolbarenabled).

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
+  devToolbar: {
+    enabled: false
+  }
});
```

To enable the dev toolbar again, remove these lines from your configuration, or set `enabled: true`.

### Per-user

[Section titled “Per-user”](#per-user)

To disable the dev toolbar for yourself on a specific project, run the [`astro preferences`](/en/reference/cli-reference/#astro-preferences) command.

```shell
astro preferences disable devToolbar
```

To disable the dev toolbar in all Astro projects for a user on the current machine, add the `--global` flag when running `astro-preferences`:

```shell
astro preferences disable --global devToolbar
```

The dev toolbar can later be enabled with:

```shell
astro preferences enable devToolbar
```

# E-commerce

> An introduction to adding e-commerce options to your Astro site

With Astro, you can build several e-commerce options, from checkout links to hosted payment pages to building an entire storefront using a payment service API.

## Payment processing overlays

[Section titled “Payment processing overlays”](#payment-processing-overlays)

Some payment processing services (e.g. [Lemon Squeezy](#lemon-squeezy), [Paddle](#paddle)) add a payment form to allow your customer to purchase from your site. These can be hosted overlays or embedded in a page on your site. These may offer some basic customization or site branding, and may be added to your Astro project as scripts, buttons, or external links.

### Lemon Squeezy

[Section titled “Lemon Squeezy”](#lemon-squeezy)

[Lemon Squeezy](https://www.lemonsqueezy.com/) is an all-in-one platform for payments and subscriptions with multi-currency support, global tax compliance, PayPal integration and more. It allows you to create and manage digital products and services through your account dashboard and provides product URLs for the checkout process.

The basic [Lemon.js JavaScript library](https://docs.lemonsqueezy.com/help/lemonjs/what-is-lemonjs) allows you to sell your Lemon Squeezy products with a checkout link.

#### Basic Usage

[Section titled “Basic Usage”](#basic-usage)

The following is an example of adding a Lemon Squeezy “Buy now” element to an Astro page. Clicking this link will open a checkout and allow the visitor to complete a single purchase.

1. Add the following `<script>` tag to your page `head` or `body`:

   src/pages/my-product-page.astro

   ```html
   <script src="https://app.lemonsqueezy.com/js/lemon.js" defer></script>
   ```

2. Create an anchor tag on the page linking to your product URL. Include the class `lemonsqueezy-button` to open a checkout overlay when clicked.

   src/pages/my-product-page.astro

   ```html
   <a class="lemonsqueezy-button" href="https://demo.lemonsqueezy.com/checkout/...">
     Buy Now
   </a>
   ```

#### Lemon.js

[Section titled “Lemon.js”](#lemonjs)

Lemon.js also provides additional behavior such as [programmatically opening overlays](https://docs.lemonsqueezy.com/help/lemonjs/opening-overlays) and [handling overlay events](https://docs.lemonsqueezy.com/help/lemonjs/handling-events).

Read the [Lemon Squeezy developer getting started guide](https://docs.lemonsqueezy.com/guides/developer-guide) for more information.

### Paddle

[Section titled “Paddle”](#paddle)

[Paddle](https://www.paddle.com/) is a billing solution for digital products and services. It handles payments, taxes, and subscription management through an overlay or inline checkout.

[Paddle.js](https://developer.paddle.com/paddlejs/overview) is a lightweight JavaScript library that lets you build rich, integrated subscription billing experiences using Paddle.

#### Basic Usage

[Section titled “Basic Usage”](#basic-usage-1)

The following is an example of adding a Paddle “Buy Now” element to an Astro page. Clicking this link will open a checkout and allow the visitor to complete a single purchase.

After your default payment link domain (your own website) is approved by Paddle, you can turn any element on your page into a trigger for a checkout overlay using HTML data attributes.

1. Add the following two `<script>` tags to your page `head` or `body`:

   src/pages/my-product-page.astro

   ```html
   <script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
   <script type="text/javascript">
     Paddle.Setup({
       token: '7d279f61a3499fed520f7cd8c08' // replace with a client-side token
     });
   </script>
   ```

2. Turn any element on your page into a Paddle Checkout button by adding the `paddle_button` class:

   src/pages/my-product-page.astro

   ```html
   <a href="#" class="paddle_button">Buy Now</a>
   ```

3. Add a `data-items` attribute to specify your product’s Paddle `priceId` and `quantity`. You can also optionally pass additional [supported HTML data attributes](https://developer.paddle.com/paddlejs/html-data-attributes) to prefill data, handle checkout success, or style your button and checkout overlay:

   src/pages/my-product-page.astro

   ```html
   <a
     href="#"
     class="paddle_button"
     data-display-mode="overlay"
     data-theme="light"
     data-locale="en"
     data-success-url="https://example.com/thankyou"
     data-items='[
       {
         "priceId": "pri_01gs59hve0hrz6nyybj56z04eq",
         "quantity": 1
       }
     ]'
   >
     Buy now
   </a>
   ```

#### Paddle.js

[Section titled “Paddle.js”](#paddlejs)

Instead of passing HTML data attributes, you can send data to the checkout overlay using JavaScript for passing multiple attributes and even greater customization. You can also create upgrade workflows using an inline checkout.

Read more about [using Paddle.js to build an inline checkout](https://developer.paddle.com/build/checkout/build-branded-inline-checkout).

## Full-featured e-commerce solutions

[Section titled “Full-featured e-commerce solutions”](#full-featured-e-commerce-solutions)

For more customization over your site’s shopping cart and checkout process, you can connect a more fully-featured financial service provider (e.g. [Snipcart](#snipcart)) to your Astro project. These e-commerce platforms may also integrate with other third-party services for user account management, personalization, inventory and analytics.

### Snipcart

[Section titled “Snipcart”](#snipcart)

[Snipcart](https://snipcart.com/) is a powerful, developer-first HTML/JavaScript shopping cart platform.

Snipcart also allows you to integrate with third-party services such as shipping providers, enable webhooks for an advanced e-commerce integration between your shopping cart and other systems, choose from several payment gateways (e.g. Stripe, Paypal, and Square), customize email templates, and even provides live testing environments.

Tip

Want a pre-built Snipcart solution instead? Check out [`astro-snipcart`](https://astro-snipcart.vercel.app/), a fully functional Astro community template including an optional design system, ready for you to integrate with your existing Snipcart account.

#### Basic Usage

[Section titled “Basic Usage”](#basic-usage-2)

The following is an example of configuring a Snipcart checkout and adding button elements for “Add to cart” and “Check out now” to an Astro page. This will allow your visitors to add products to a cart without being immediately sent to a checkout page.

For complete instructions, including setting up your Snipcart store, please see [the Snipcart installation documentation](https://docs.snipcart.com/v3/setup/installation).

1. Add the script [as shown in the Snipcart installation instructions](https://docs.snipcart.com/v3/setup/installation) on your page after the `<body>` element.

   src/pages/my-product-page.astro

   ```html
   <body></body>
   <script>
     window.SnipcartSettings = {
       publicApiKey: "YOUR_API_KEY",
       loadStrategy: "on-user-interaction",
     };


     (function()...); // available from the Snipcart documentation
   </script>
   ```

2. Customize `window.SnipcartSettings` with any of the [available Snipcart settings](https://docs.snipcart.com/v3/setup/installation#settings) to control the behavior and appearance of your cart.

   src/pages/my-product-page.astro

   ```html
   <script>
     window.SnipcartSettings = {
       publicApiKey: "YOUR_API_KEY",
       loadStrategy: "manual",
       version: "3.7.1",
       addProductBehavior: "none",
       modalStyle: "side",
     };


     (function()...); // available from the Snipcart documentation
   </script>
   ```

3. Add `class="snipcart-add-item"` to any HTML element, such as a `<button>`, to add an item to the cart when clicked on. Also include any other data elements for [common Snipcart product attributes](https://docs.snipcart.com/v3/setup/products) such as price and description, and any optional fields.

   src/pages/my-product-page.astro

   ```html
   <button
     class="snipcart-add-item"
     data-item-id="astro-print"
     data-item-price="39.99"
     data-item-description="A framed print of the Astro logo."
     data-item-image="/assets/images/astro-print.jpg"
     data-item-name="Astro Print"
     data-item-custom1-name="Frame color"
     data-item-custom1-options="Brown|Silver[+10.00]|Gold[+20.00]"
     data-item-custom2-name="Delivery instructions"
     data-item-custom2-type="textarea"
   >
     Add to cart
   </button>
   ```

4. Add a Snipcart checkout button with the `snipcart-checkout` class to open the cart and allow guests to complete their purchase with a checkout modal.

   src/pages/my-product-page.astro

   ```html
   <button class="snipcart-checkout">Click here to checkout</button>
   ```

#### Snipcart JavaScript SDK

[Section titled “Snipcart JavaScript SDK”](#snipcart-javascript-sdk)

The [Snipcart JavaScript SDK](https://docs.snipcart.com/v3/sdk/basics) lets you configure, customize and manage your Snipcart cart programmatically.

This allows you to perform actions such as:

* Retrieve relevant information about the current Snipcart session and apply certain operations to the cart.
* Listen to incoming events and trigger callbacks dynamically.
* Listen to state changes and receive a full snapshot of the state of the cart.

See the [Snipcart documentation](https://docs.snipcart.com/v3/) for more information about all the options to integrate Snipcart with your Astro Project.

#### `astro-snipcart`

[Section titled “astro-snipcart”](#astro-snipcart)

There are two `astro-snipcart` community packages that can simplify using Snipcart.

* [`@lloydjatkinson/astro-snipcart` Astro template](https://astro-snipcart.vercel.app/): This Astro template includes an optional design system for a complete e-commerce solution out of the box. Learn more on its own extensive documentation site, including [the motivation behind building `astro-snipcart`](https://astro-snipcart.vercel.app/motivation) as providing a convenient, Astro-native way for you to interact with the Snipcart API.

* [`@Adammatthiesen/astro-snipcart` integration](https://github.com/Adammatthiesen/astro-snipcart): This integration was heavily inspired by the `astro-snipcart` theme and provides Astro components (or Vue components) that you can add to your existing Astro project for creating products, controlling the cart, and more. See the [full tutorial](https://matthiesen.xyz/blog/getting-started-with-my-astro-snipcart-addon) for more information.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Hands-On Experience: eCommerce Store with Astro?](https://crystallize.com/blog/building-ecommerce-with-astro)
* [Collecting Payments with Stripe using Astro](https://zellwk.com/blog/stripe-astro-recipe/)

# Endpoints

> Learn how to create endpoints that serve any kind of data

Astro lets you create custom endpoints to serve any kind of data. You can use this to generate images, expose an RSS document, or use them as API Routes to build a full API for your site.

In statically-generated sites, your custom endpoints are called at build time to produce static files. If you opt in to [SSR](/en/guides/on-demand-rendering/) mode, custom endpoints turn into live server endpoints that are called on request. Static and SSR endpoints are defined similarly, but SSR endpoints support additional features.

## Static File Endpoints

[Section titled “Static File Endpoints”](#static-file-endpoints)

To create a custom endpoint, add a `.js` or `.ts` file to the `/pages` directory. The `.js` or `.ts` extension will be removed during the build process, so the name of the file should include the extension of the data you want to create. For example, `src/pages/data.json.ts` will build a `/data.json` endpoint.

Endpoints export a `GET` function (optionally `async`) that receives a [context object](/en/reference/api-reference/) with properties similar to the `Astro` global. Here, it returns a [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) object with a `name` and `url`, and Astro will call this at build time and use the contents of the body to generate the file.

src/pages/builtwith.json.ts

```ts
// Outputs: /builtwith.json
export function GET({ params, request }) {
  return new Response(
    JSON.stringify({
      name: "Astro",
      url: "https://astro.build/",
    }),
  );
}
```

Since Astro v3.0, the returned `Response` object doesn’t have to include the `encoding` property anymore. For example, to produce a binary `.png` image:

src/pages/astro-logo.png.ts

```ts
export async function GET({ params, request }) {
  const response = await fetch(
    "https://docs.astro.build/assets/full-logo-light.png",
  );


  return new Response(await response.arrayBuffer());
}
```

You can also type your endpoint functions using the `APIRoute` type:

```ts
import type { APIRoute } from "astro";


export const GET: APIRoute = async ({ params, request }) => {...}
```

### `params` and Dynamic routing

[Section titled “params and Dynamic routing”](#params-and-dynamic-routing)

Endpoints support the same [dynamic routing](/en/guides/routing/#dynamic-routes) features that pages do. Name your file with a bracketed parameter name and export a [`getStaticPaths()` function](/en/reference/routing-reference/#getstaticpaths). Then, you can access the parameter using the `params` property passed to the endpoint function:

src/pages/api/\[id].json.ts

```ts
import type { APIRoute } from "astro";


const usernames = ["Sarah", "Chris", "Yan", "Elian"];


export const GET: APIRoute = ({ params, request }) => {
  const id = params.id;


  return new Response(
    JSON.stringify({
      name: usernames[id],
    }),
  );
};


export function getStaticPaths() {
  return [
    { params: { id: "0" } },
    { params: { id: "1" } },
    { params: { id: "2" } },
    { params: { id: "3" } },
  ];
}
```

This will generate four JSON endpoints at build time: `/api/0.json`, `/api/1.json`, `/api/2.json` and `/api/3.json`. Dynamic routing with endpoints works the same as it does with pages, but because the endpoint is a function and not a component, [props](/en/reference/routing-reference/#data-passing-with-props) aren’t supported.

### `request`

[Section titled “request”](#request)

All endpoints receive a `request` property, but in static mode, you only have access to `request.url`. This returns the full URL of the current endpoint and works the same as [Astro.request.url](/en/reference/api-reference/#request) does for pages.

src/pages/request-path.json.ts

```ts
import type { APIRoute } from "astro";


export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      path: new URL(request.url).pathname,
    }),
  );
};
```

## Server Endpoints (API Routes)

[Section titled “Server Endpoints (API Routes)”](#server-endpoints-api-routes)

Everything described in the static file endpoints section can also be used in SSR mode: files can export a `GET` function which receives a [context object](/en/reference/api-reference/) with properties similar to the `Astro` global.

But, unlike in `static` mode, when you enable on-demand rendering for a route, the endpoint will be built when it is requested. This unlocks new features that are unavailable at build time, and allows you to build API routes that listen for requests and securely execute code on the server at runtime.

Your routes will be rendered on demand by default in `server` mode. In `static` mode, you must opt out of prerendering for each custom endpoint with `export const prerender = false`.

![](/houston_chef.webp) **Related recipe:** [Call endpoints from the server](/en/recipes/call-endpoints/)

Note

Be sure to [enable an on-demand rendering mode](/en/guides/on-demand-rendering/) before trying these examples, and opt out of prerendering in `static` mode.

Server endpoints can access `params` without exporting `getStaticPaths`, and they can return a `Response` object, allowing you to set status codes and headers:

src/pages/\[id].json.js

```js
import { getProduct } from "../db";


export async function GET({ params }) {
  const id = params.id;
  const product = await getProduct(id);


  if (!product) {
    return new Response(null, {
      status: 404,
      statusText: "Not found",
    });
  }


  return new Response(JSON.stringify(product), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
    },
  });
}
```

This will respond to any request that matches the dynamic route. For example, if we navigate to `/helmet.json`, `params.id` will be set to `helmet`. If `helmet` exists in the mock product database, the endpoint will use a `Response` object to respond with JSON and return a successful [HTTP status code](https://developer.mozilla.org/en-US/docs/Web/API/Response/status). If not, it will use a `Response` object to respond with a `404`.

In SSR mode, certain providers require the `Content-Type` header to return an image. In this case, use a `Response` object to specify a `headers` property. For example, to produce a binary `.png` image:

src/pages/astro-logo.png.ts

```ts
export async function GET({ params, request }) {
  const response = await fetch(
    "https://docs.astro.build/assets/full-logo-light.png",
  );
  const buffer = Buffer.from(await response.arrayBuffer());


  return new Response(buffer, {
    headers: { "Content-Type": "image/png" },
  });
}
```

### HTTP methods

[Section titled “HTTP methods”](#http-methods)

In addition to the `GET` function, you can export a function with the name of any [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods). When a request comes in, Astro will check the method and call the corresponding function.

You can also export an `ALL` function to match any method that doesn’t have a corresponding exported function. If there is a request with no matching method, it will redirect to your site’s [404 page](/en/basics/astro-pages/#custom-404-error-page).

src/pages/methods.json.ts

```ts
export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: "This was a GET!",
    }),
  );
};


export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: "This was a POST!",
    }),
  );
};


export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: "This was a DELETE!",
    }),
  );
};


export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `This was a ${request.method}!`,
    }),
  );
};
```

If you define a `GET` function but no `HEAD` function, Astro will automatically handle `HEAD` requests by calling the `GET` function and stripping the body from the response.

![](/houston_chef.webp) **Related recipes**

* [Verify a Captcha](/en/recipes/captcha/)
* [Build forms with API routes](/en/recipes/build-forms-api/)

### `request`

[Section titled “request”](#request-1)

In SSR mode, the `request` property returns a fully usable [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object that refers to the current request. This allows you to accept data and check headers:

src/pages/test-post.json.ts

```ts
export const POST: APIRoute = async ({ request }) => {
  if (request.headers.get("Content-Type") === "application/json") {
    const body = await request.json();
    const name = body.name;


    return new Response(
      JSON.stringify({
        message: "Your name was: " + name,
      }),
      {
        status: 200,
      },
    );
  }


  return new Response(null, { status: 400 });
};
```

### Redirects

[Section titled “Redirects”](#redirects)

The endpoint context exports a `redirect()` utility similar to `Astro.redirect`:

src/pages/links/\[id].js

```js
import { getLinkUrl } from "../db";


export async function GET({ params, redirect }) {
  const { id } = params;
  const link = await getLinkUrl(id);


  if (!link) {
    return new Response(null, {
      status: 404,
      statusText: "Not found",
    });
  }


  return redirect(link, 307);
}
```

# Using environment variables

> Learn how to use environment variables in an Astro project.

Astro gives you access to [Vite’s built-in environment variables support](#vites-built-in-support) and includes some [default environment variables for your project](#default-environment-variables) that allow you to access configuration values for your current project (e.g. `site`, `base`), whether your project is running in development or production, and more.

Astro also provides a way to [use and organize your environment variables with type safety](#type-safe-environment-variables). It is available for use inside the Astro context (e.g. Astro components, routes and endpoints, UI framework components, middleware), and managed with [a schema in your Astro configuration](/en/reference/configuration-reference/#env).

## Vite’s built-in support

[Section titled “Vite’s built-in support”](#vites-built-in-support)

Astro uses Vite’s built-in support for environment variables, which are statically replaced at build time, and lets you [use any of its methods](https://vite.dev/guide/env-and-mode.html) to work with them.

Note that while *all* environment variables are available in server-side code, only environment variables prefixed with `PUBLIC_` are available in client-side code for security purposes.

.env

```ini
SECRET_PASSWORD=password123
PUBLIC_ANYBODY=there
```

In this example, `PUBLIC_ANYBODY` (accessible via `import.meta.env.PUBLIC_ANYBODY`) will be available in server or client code, while `SECRET_PASSWORD` (accessible via `import.meta.env.SECRET_PASSWORD`) will be server-side only.

Caution

`.env` files are not loaded inside [configuration files](#in-the-astro-config-file).

### IntelliSense for TypeScript

[Section titled “IntelliSense for TypeScript”](#intellisense-for-typescript)

By default, Astro provides a type definition for `import.meta.env` in `astro/client.d.ts`.

While you can define more custom env variables in `.env.[mode]` files, you may want to get TypeScript IntelliSense for user-defined env variables which are prefixed with `PUBLIC_`.

To achieve this, you can create an `env.d.ts` in `src/` to [extend the global types](/en/guides/typescript/#extending-global-types) and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly DB_PASSWORD: string;
  readonly PUBLIC_POKEAPI: string;
  // more env variables...
}


interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

## Default environment variables

[Section titled “Default environment variables”](#default-environment-variables)

Astro includes a few environment variables out of the box:

* `import.meta.env.MODE`: The mode your site is running in. This is `development` when running `astro dev` and `production` when running `astro build`.
* `import.meta.env.PROD`: `true` if your site is running in production; `false` otherwise.
* `import.meta.env.DEV`: `true` if your site is running in development; `false` otherwise. Always the opposite of `import.meta.env.PROD`.
* `import.meta.env.BASE_URL`: The base URL your site is being served from. This is determined by the [`base` config option](/en/reference/configuration-reference/#base).
* `import.meta.env.SITE`: This is set to [the `site` option](/en/reference/configuration-reference/#site) specified in your project’s `astro.config`.
* `import.meta.env.ASSETS_PREFIX`: The prefix for Astro-generated asset links if the [`build.assetsPrefix` config option](/en/reference/configuration-reference/#buildassetsprefix) is set. This can be used to create asset links not handled by Astro.

Use them like any other environment variable.

```ts
const isProd = import.meta.env.PROD;
const isDev = import.meta.env.DEV;
```

## Setting environment variables

[Section titled “Setting environment variables”](#setting-environment-variables)

### `.env` files

[Section titled “.env files”](#env-files)

Environment variables can be loaded from `.env` files in your project directory.

Just create a `.env` file in the project directory and add some variables to it.

.env

```ini
# This will only be available when run on the server!
DB_PASSWORD="foobar"


# This will be available everywhere!
PUBLIC_POKEAPI="https://pokeapi.co/api/v2"
```

You can also add `.production`, `.development` or a custom mode name to the filename itself (e.g `.env.testing`, `.env.staging`). This allows you to use different sets of environment variables at different times.

The `astro dev` and `astro build` commands default to `"development"` and `"production"` modes, respectively. You can run these commands with the [`--mode` flag](/en/reference/cli-reference/#--mode-string) to pass a different value for `mode` and load the matching `.env` file.

This allows you to run the dev server or build your site connecting to different APIs:

* npm

  ```shell
  # Run the dev server connected to a "staging" API
  npm run astro dev -- --mode staging


  # Build a site that connects to a "production" API with additional debug information
  npm run astro build -- --devOutput


  # Build a site that connects to a "testing" API
  npm run astro build -- --mode testing
  ```

* pnpm

  ```shell
  # Run the dev server connected to a "staging" API
  pnpm astro dev --mode staging


  # Build a site that connects to a "production" API with additional debug information
  pnpm astro build --devOutput


  # Build a site that connects to a "testing" API
  pnpm astro build --mode testing
  ```

* Yarn

  ```shell
  # Run the dev server connected to a "staging" API
  yarn astro dev --mode staging


  # Build a site that connects to a "production" API with additional debug information
  yarn astro build --devOutput


  # Build a site that connects to a "testing" API
  yarn astro build --mode testing
  ```

For more on `.env` files, [see the Vite documentation](https://vite.dev/guide/env-and-mode.html#env-files).

### In the Astro config file

[Section titled “In the Astro config file”](#in-the-astro-config-file)

Astro evaluates configuration files before it loads your other files. This means that you cannot use `import.meta.env` in `astro.config.mjs` to access environment variables that were set in `.env` files.

You can use `process.env` in a configuration file to access other environment variables, like those [set by the CLI](#using-the-cli).

You can also use [Vite’s `loadEnv` helper](https://main.vite.dev/config/#using-environment-variables-in-config) to manually load `.env` files.

astro.config.mjs

```js
import { loadEnv } from "vite";


const { SECRET_PASSWORD } = loadEnv(process.env.NODE_ENV, process.cwd(), "");
```

Note

`pnpm` does not allow you to import modules that are not directly installed in your project. If you are using `pnpm`, you will need to install `vite` to use the `loadEnv` helper.

```sh
pnpm add -D vite
```

### Using the CLI

[Section titled “Using the CLI”](#using-the-cli)

You can also add environment variables as you run your project:

* npm

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 npm run dev
  ```

* pnpm

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 pnpm run dev
  ```

* Yarn

  ```shell
  PUBLIC_POKEAPI=https://pokeapi.co/api/v2 yarn run dev
  ```

## Getting environment variables

[Section titled “Getting environment variables”](#getting-environment-variables)

Environment variables in Astro are accessed with `import.meta.env`, using the [`import.meta` feature added in ES2020](https://tc39.es/ecma262/2020/#prod-ImportMeta), instead of `process.env`.

For example, use `import.meta.env.PUBLIC_POKEAPI` to get the `PUBLIC_POKEAPI` environment variable.

```js
// When import.meta.env.SSR === true
const data = await db(import.meta.env.DB_PASSWORD);


// When import.meta.env.SSR === false
const data = fetch(`${import.meta.env.PUBLIC_POKEAPI}/pokemon/squirtle`);
```

When using SSR, environment variables can be accessed at runtime based on the SSR adapter being used. With most adapters you can access environment variables with `process.env`, but some adapters work differently. For the Deno adapter, you will use `Deno.env.get()`. See how to [access the Cloudflare runtime](/en/guides/integrations-guide/cloudflare/#cloudflare-runtime) to handle environment variables when using the Cloudflare adapter. Astro will first check the server environment for variables, and if they don’t exist, Astro will look for them in `.env` files.

## Type safe environment variables

[Section titled “Type safe environment variables”](#type-safe-environment-variables)

The `astro:env` API lets you configure a type-safe schema for [environment variables you have set](#setting-environment-variables). This allows you to indicate whether they should be available on the server or the client, and define their data type and additional properties.

Developing an adapter? See how to [make an adapter compatible with `astro:env`](/en/reference/adapter-reference/#envgetsecret).

### Basic Usage

[Section titled “Basic Usage”](#basic-usage)

#### Define your schema

[Section titled “Define your schema”](#define-your-schema)

To configure a schema, add the `env.schema` option to your Astro config:

astro.config.mjs

```diff
import { defineConfig } from "astro/config";


export default defineConfig({
+  env: {
+    schema: {
      +// ...
+    }
+  }
})
```

You can then [register variables as a string, number, enum, or boolean](#data-types) using the `envField` helper. Define the [kind of environment variable](#variable-types) by providing a `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) for each variable, and pass any additional properties such as `optional` or `default` in an object:

astro.config.mjs

```js
import { defineConfig, envField } from "astro/config";


export default defineConfig({
  env: {
    schema: {
      API_URL: envField.string({ context: "client", access: "public", optional: true }),
      PORT: envField.number({ context: "server", access: "public", default: 4321 }),
      API_SECRET: envField.string({ context: "server", access: "secret" }),
    }
  }
})
```

Types will be generated for you when running `astro dev` or `astro build`, but you can run `astro sync` to generate types only.

#### Use variables from your schema

[Section titled “Use variables from your schema”](#use-variables-from-your-schema)

Import and use your defined variables from the appropriate `/client` or `/server` module:

```astro
---
import { API_URL } from "astro:env/client";
import { API_SECRET_TOKEN } from "astro:env/server";


const data = await fetch(`${API_URL}/users`, {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${API_SECRET_TOKEN}`
  },
})
---


<script>
  import { API_URL } from "astro:env/client";


  fetch(`${API_URL}/ping`)
</script>
```

### Variable types

[Section titled “Variable types”](#variable-types)

There are three kinds of environment variables, determined by the combination of `context` (`"client"` or `"server"`) and `access` (`"secret"` or `"public"`) settings defined in your schema:

* **Public client variables**: These variables end up in both your final client and server bundles, and can be accessed from both client and server through the `astro:env/client` module:

  ```js
  import { API_URL } from "astro:env/client";
  ```

* **Public server variables**: These variables end up in your final server bundle and can be accessed on the server through the `astro:env/server` module:

  ```js
  import { PORT } from "astro:env/server";
  ```

* **Secret server variables**: These variables are not part of your final bundle and can be accessed on the server through the `astro:env/server` module:

  ```js
  import { API_SECRET } from "astro:env/server";
  ```

  By default, secrets are only validated at runtime. You can enable validating private variables on start by [configuring `validateSecrets: true`](/en/reference/configuration-reference/#envvalidatesecrets).

Note

**Secret client variables** are not supported because there is no safe way to send this data to the client. Therefore, it is not possible to configure both `context: "client"` and `access: "secret"` in your schema.

### Data types

[Section titled “Data types”](#data-types)

There are currently four data types supported: strings, numbers, enums, and booleans:

```js
import { envField } from "astro/config";


envField.string({
   // context & access
   optional: true,
   default: "foo",
})


envField.number({
   // context & access
   optional: true,
   default: 15,
})


envField.boolean({
   // context & access
   optional: true,
   default: true,
})


envField.enum({
   // context & access
   values: ["foo", "bar", "baz"],
   optional: true,
   default: "baz",
})
```

For a complete list of validation fields, see the [`envField` API reference](/en/reference/configuration-reference/#envschema).

### Retrieving secrets dynamically

[Section titled “Retrieving secrets dynamically”](#retrieving-secrets-dynamically)

Despite defining your schema, you may want to retrieve the raw value of a given secret or to retrieve secrets not defined in your schema. In this case, you can use `getSecret()` exported from `astro:env/server`:

```js
import {
   FOO, // boolean
   getSecret
} from "astro:env/server";


getSecret("FOO"); // string | undefined
```

Learn more in [the API reference](/en/reference/modules/astro-env/#getsecret).

### Limitations

[Section titled “Limitations”](#limitations)

`astro:env` is a virtual module which means it can only be used inside the Astro context. For example, you can use it in:

* Middlewares
* Astro routes and endpoints
* Astro components
* Framework components
* Modules

You cannot use it in the following and will have to resort to `process.env`:

* `astro.config.mjs`
* Scripts

# Using custom fonts

> Looking to add some custom typefaces to an Astro website? Use Google Fonts with Fontsource or add a font of your choice.

This guide will show you how to add web fonts to your project and use them in your components.

Experimental Fonts API

Learn about Astro’s [experimental Fonts API](/en/reference/experimental-flags/fonts/) that allows you to use fonts from your filesystem and various font providers through a unified, fully customizable, and type-safe API.

## Using a local font file

[Section titled “Using a local font file”](#using-a-local-font-file)

This example will demonstrate adding a custom font using the font file `DistantGalaxy.woff`.

1. Add your font file to `public/fonts/`.

2. Add the following `@font-face` statement to your CSS. This could be in a global `.css` file you import, a `<style is:global>` block, or a `<style>` block in a specific layout or component where you want to use this font.

   ```css
   /* Register your custom font family and tell the browser where to find it. */
   @font-face {
     font-family: 'DistantGalaxy';
     src: url('/fonts/DistantGalaxy.woff') format('woff');
     font-weight: normal;
     font-style: normal;
     font-display: swap;
   }
   ```

3. Use the `font-family` value from the `@font-face` statement to style elements in your component or layout. In this example, the `<h1>` heading will have the custom font applied, while the paragraph `<p>` will not.

   src/pages/example.astro

   ```astro
   ---
   ---


   <h1>In a galaxy far, far away...</h1>


   <p>Custom fonts make my headings much cooler!</p>


   <style>
   h1 {
     font-family: 'DistantGalaxy', sans-serif;
   }
   </style>
   ```

## Using Fontsource

[Section titled “Using Fontsource”](#using-fontsource)

The [Fontsource](https://fontsource.org/) project simplifies using Google Fonts and other open-source fonts. It provides npm modules you can install for the fonts you want to use.

1. Find the font you want to use in [Fontsource’s catalog](https://fontsource.org/). This example will use [Twinkle Star](https://fontsource.org/fonts/twinkle-star).

2. Install the package for your chosen font.

   * npm

     ```shell
     npm install @fontsource/twinkle-star
     ```

   * pnpm

     ```shell
     pnpm add @fontsource/twinkle-star
     ```

   * Yarn

     ```shell
     yarn add @fontsource/twinkle-star
     ```

   Tip

   You’ll find the correct package name in the “Quick Installation” section of each font page on Fontsource’s website. It will start with `@fontsource/` or `@fontsource-variable/` followed by the name of the font.

3. Import the font package in the component where you want to use the font. Usually, you will want to do this in a common layout component to make sure the font is available across your site.

   The import will automatically add the necessary `@font-face` rules needed to set up the font.

   src/layouts/BaseLayout.astro

   ```astro
   ---
   import '@fontsource/twinkle-star';
   ---
   ```

4. Use the font’s name as shown in the `body` example on its Fontsource page as the `font-family` value. This will work anywhere you can write CSS in your Astro project.

   ```css
   h1 {
     font-family: "Twinkle Star", cursive;
   }
   ```

To optimize your website’s rendering times, you may want to preload fonts that are essential for the initial page display. See the [Fontsource guide to preloading fonts](https://fontsource.org/docs/getting-started/preload) for more information and usage.

## Register fonts in Tailwind

[Section titled “Register fonts in Tailwind”](#register-fonts-in-tailwind)

If you are using [Tailwind](/en/guides/styling/#tailwind), you can use either of the previous methods on this page to install your font, with some modifications. You can either add an [`@font-face` statement for a local font](#using-a-local-font-file) or use [Fontsource’s `import` strategy](#using-fontsource) to install your font.

To register your font in Tailwind:

1. Follow either of the guides above, but skip the final step of adding `font-family` to your CSS.

2. Add the typeface name to `src/styles/global.css`.

   This example adds `Inter` to the sans-serif font stack.

   src/styles/global.css

   ```diff
   @import 'tailwindcss';


   +@theme {
     +--font-sans: 'Inter', 'sans-serif';
   +}
   ```

   Now, all sans-serif text (the default with Tailwind) in your project will use your chosen font and the `font-sans` class will also apply the Inter font.

See [Tailwind’s docs on adding custom font families](https://tailwindcss.com/docs/font-family#using-custom-values) for more information.

## More resources

[Section titled “More resources”](#more-resources)

* Learn how web fonts work in [MDN’s web fonts guide](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Web_fonts).
* Generate CSS for your font with [Font Squirrel’s Webfont Generator](https://www.fontsquirrel.com/tools/webfont-generator).

# Front-end frameworks

> Build your Astro website with React, Svelte, and more.

Build your Astro website without sacrificing your favorite component framework. Create Astro [islands](/en/concepts/islands/) with the UI frameworks of your choice.

## Official front-end framework integrations

[Section titled “Official front-end framework integrations”](#official-front-end-framework-integrations)

Astro supports a variety of popular frameworks including [React](https://react.dev/), [Preact](https://preactjs.com/), [Svelte](https://svelte.dev/), [Vue](https://vuejs.org/), [SolidJS](https://www.solidjs.com/), and [AlpineJS](https://alpinejs.dev/) with official integrations.

Find even more [community-maintained framework integrations](https://astro.build/integrations/?search=\&categories%5B%5D=frameworks) (e.g. Angular, Qwik, Elm) in our integrations directory.

### Front-end frameworks

* ![](/logos/alpine-js.svg)

  ### [@astrojs/​alpinejs](/en/guides/integrations-guide/alpinejs/)

* ![](/logos/preact.svg)

  ### [@astrojs/​preact](/en/guides/integrations-guide/preact/)

* ![](/logos/react.svg)

  ### [@astrojs/​react](/en/guides/integrations-guide/react/)

* ![](/logos/solid.svg)

  ### [@astrojs/​solid⁠-⁠js](/en/guides/integrations-guide/solid-js/)

* ![](/logos/svelte.svg)

  ### [@astrojs/​svelte](/en/guides/integrations-guide/svelte/)

* ![](/logos/vue.svg)

  ### [@astrojs/​vue](/en/guides/integrations-guide/vue/)

## Installing integrations

[Section titled “Installing integrations”](#installing-integrations)

One or several of these Astro integrations can be installed and configured in your project.

See the [Integrations Guide](/en/guides/integrations-guide/) for more details on installing and configuring Astro integrations.

Tip

Want to see an example for the framework of your choice? Visit [astro.new](https://astro.new/latest/frameworks) and select one of the framework templates.

## Using framework components

[Section titled “Using framework components”](#using-framework-components)

Use your JavaScript framework components in your Astro pages, layouts and components just like Astro components! All your components can live together in `/src/components`, or can be organized in any way you like.

To use a framework component, import it from its relative path in your Astro component script. Then, use the component alongside other components, HTML elements and JSX-like expressions in the component template.

src/pages/static-components.astro

```diff
---
+import MyReactComponent from '../components/MyReactComponent.jsx';
---
<html>
  <body>
    <h1>Use React components directly in Astro!</h1>
    +<MyReactComponent />
  </body>
</html>
```

By default, your framework components will only render on the server, as static HTML. This is useful for templating components that are not interactive and avoids sending any unnecessary JavaScript to the client.

## Hydrating interactive components

[Section titled “Hydrating interactive components”](#hydrating-interactive-components)

A framework component can be made interactive (hydrated) using a [`client:*` directive](/en/reference/directives-reference/#client-directives). These are component attributes that determine when your component’s JavaScript should be sent to the browser.

With all client directives except `client:only`, your component will first render on the server to generate static HTML. Component JavaScript will be sent to the browser according to the directive you chose. The component will then hydrate and become interactive.

src/pages/interactive-components.astro

```astro
---
// Example: hydrating framework components in the browser.
import InteractiveButton from '../components/InteractiveButton.jsx';
import InteractiveCounter from '../components/InteractiveCounter.jsx';
import InteractiveModal from '../components/InteractiveModal.svelte';
---
<!-- This component's JS will begin importing when the page loads -->
<InteractiveButton client:load />


<!-- This component's JS will not be sent to the client until
the user scrolls down and the component is visible on the page -->
<InteractiveCounter client:visible />


<!-- This component won't render on the server, but will render on the client when the page loads -->
<InteractiveModal client:only="svelte" />
```

The JavaScript framework (React, Svelte, etc.) needed to render the component will be sent to the browser along with the component’s own JavaScript. If two or more components on a page use the same framework, the framework will only be sent once.

Accessibility

Most framework-specific accessibility patterns should work the same when these components are used in Astro. Be sure to choose a client directive that will ensure any accessibility-related JavaScript is properly loaded and executed at the appropriate time!

### Available hydration directives

[Section titled “Available hydration directives”](#available-hydration-directives)

There are several hydration directives available for UI framework components: `client:load`, `client:idle`, `client:visible`, `client:media={QUERY}` and `client:only={FRAMEWORK}`.

See our [directives reference](/en/reference/directives-reference/#client-directives) page for a full description of these hydration directives, and their usage.

## Mixing frameworks

[Section titled “Mixing frameworks”](#mixing-frameworks)

You can import and render components from multiple frameworks in the same Astro component.

src/pages/mixing-frameworks.astro

```astro
---
// Example: Mixing multiple framework components on the same page.
import MyReactComponent from '../components/MyReactComponent.jsx';
import MySvelteComponent from '../components/MySvelteComponent.svelte';
import MyVueComponent from '../components/MyVueComponent.vue';
---
<div>
  <MySvelteComponent />
  <MyReactComponent />
  <MyVueComponent />
</div>
```

Astro will recognize and render your component based on its file extension. To distinguish between frameworks that use the same file extension, [additional configuration when rendering multiple JSX frameworks](/en/guides/integrations-guide/react/#combining-multiple-jsx-frameworks) (e.g. React and Preact) is required.

Caution

Only **Astro** components (`.astro`) can contain components from multiple frameworks.

## Passing props to framework components

[Section titled “Passing props to framework components”](#passing-props-to-framework-components)

You can pass props from Astro components to framework components:

src/pages/frameworks-props.astro

```astro
---
import TodoList from '../components/TodoList.jsx';
import Counter from '../components/Counter.svelte';
---
<div>
  <TodoList initialTodos={["learn Astro", "review PRs"]} />
  <Counter startingCount={1} />
</div>
```

Props that are passed to interactive framework components [using a `client:*` directive](/en/reference/directives-reference/#client-directives) must be [serialized](https://developer.mozilla.org/en-US/docs/Glossary/Serialization): translated into a format suitable for transfer over a network, or storage. However, Astro does not serialize every type of data structure. Therefore, there are some limitations on what can be passed as props to hydrated components.

The following prop types are supported: plain object, `number`, `string`, `Array`, `Map`, `Set`, `RegExp`, `Date`, `BigInt`, `URL`, `Uint8Array`, `Uint16Array`, `Uint32Array`, and `Infinity`

Non-supported data structures passed to components, such as functions, can only be used during the component’s server rendering and cannot be used to provide interactivity. For example, passing functions to hydrated components is not supported because Astro cannot pass functions from the server in a way that makes them executable on the client.

## Passing children to framework components

[Section titled “Passing children to framework components”](#passing-children-to-framework-components)

Inside of an Astro component, you **can** pass children to framework components. Each framework has its own patterns for how to reference these children: React, Preact, and Solid all use a special prop named `children`, while Svelte and Vue use the `<slot />` element.

src/pages/component-children.astro

```astro
---
import MyReactSidebar from '../components/MyReactSidebar.jsx';
---
<MyReactSidebar>
  <p>Here is a sidebar with some text and a button.</p>
</MyReactSidebar>
```

Additionally, you can use [Named Slots](/en/basics/astro-components/#named-slots) to group specific children together.

For React, Preact, and Solid, these slots will be converted to a top-level prop. Slot names using `kebab-case` will be converted to `camelCase`.

src/pages/named-slots.astro

```astro
---
import MySidebar from '../components/MySidebar.jsx';
---
<MySidebar>
  <h2 slot="title">Menu</h2>
  <p>Here is a sidebar with some text and a button.</p>
  <ul slot="social-links">
    <li><a href="https://twitter.com/astrodotbuild">Twitter</a></li>
    <li><a href="https://github.com/withastro">GitHub</a></li>
  </ul>
</MySidebar>
```

src/components/MySidebar.jsx

```jsx
export default function MySidebar(props) {
  return (
    <aside>
      <header>{props.title}</header>
      <main>{props.children}</main>
      <footer>{props.socialLinks}</footer>
    </aside>
  )
}
```

For Svelte and Vue these slots can be referenced using a `<slot>` element with the `name` attribute. Slot names using `kebab-case` will be preserved.

src/components/MySidebar.svelte

```jsx
<aside>
  <header><slot name="title" /></header>
  <main><slot /></main>
  <footer><slot name="social-links" /></footer>
</aside>
```

## Nesting framework components

[Section titled “Nesting framework components”](#nesting-framework-components)

Inside of an Astro file, framework component children can also be hydrated components. This means that you can recursively nest components from any of these frameworks.

src/pages/nested-components.astro

```astro
---
import MyReactSidebar from '../components/MyReactSidebar.jsx';
import MyReactButton from '../components/MyReactButton.jsx';
import MySvelteButton from '../components/MySvelteButton.svelte';
---
<MyReactSidebar>
  <p>Here is a sidebar with some text and a button.</p>
  <div slot="actions">
    <MyReactButton client:idle />
    <MySvelteButton client:idle />
  </div>
</MyReactSidebar>
```

Caution

Remember: framework component files themselves (e.g. `.jsx`, `.svelte`) cannot mix multiple frameworks.

This allows you to build entire “apps” in your preferred JavaScript framework and render them, via a parent component, to an Astro page.

Note

Astro components are always rendered to static HTML, even when they include framework components that are hydrated. This means that you can only pass props that don’t do any HTML rendering. Passing React’s “render props” to framework components from an Astro component will not work, because Astro components can’t provide the client runtime behavior that this pattern requires. Instead, use named slots.

## Can I use Astro components inside my framework components?

[Section titled “Can I use Astro components inside my framework components?”](#can-i-use-astro-components-inside-my-framework-components)

Any UI framework component becomes an “island” of that framework. These components must be written entirely as valid code for that framework, using only its own imports and packages. You cannot import `.astro` components in a UI framework component (e.g. `.jsx` or `.svelte`).

You can, however, use [the Astro `<slot />` pattern](/en/basics/astro-components/#slots) to pass static content generated by Astro components as children to your framework components **inside an `.astro` component**.

src/pages/astro-children.astro

```astro
---
import MyReactComponent from  '../components/MyReactComponent.jsx';
import MyAstroComponent from '../components/MyAstroComponent.astro';
---
<MyReactComponent>
  <MyAstroComponent slot="name" />
</MyReactComponent>
```

## Can I hydrate Astro components?

[Section titled “Can I hydrate Astro components?”](#can-i-hydrate-astro-components)

If you try to hydrate an Astro component with a `client:` modifier, you will get an error.

[Astro components](/en/basics/astro-components/) are HTML-only templating components with no client-side runtime. But, you can use a `<script>` tag in your Astro component template to send JavaScript to the browser that executes in the global scope.

Learn more about [client-side `<script>` tags in Astro components](/en/guides/client-side-scripts/)

# Images

> Learn how to use images in Astro.

Astro provides several ways for you to use images on your site, whether they are stored locally inside your project, linked to from an external URL, or managed in a CMS or CDN.

Astro provides built-in [`<Image />`](#image-) and [`<Picture />`](#picture-) Astro components, [Markdown image syntax](#images-in-markdown-files) (`![]()`) processing, [SVG components](#svg-components), and [an image generating function](#generating-images-with-getimage) to optimize and/or transform your images. Additionally, you can configure [automatically resizing responsive images](#responsive-image-behavior) by default, or set responsive properties on individual image and picture components.

You can always choose to use images and SVG files using native HTML elements in `.astro` or Markdown files, or the standard way for your file type (e.g. `<img />` in MDX and JSX). However, Astro does not perform any processing or optimization of these images.

There is also no native video support in Astro, and we recommend choosing a [hosted video service](/en/guides/media/) to handle the demands of optimizing and streaming video content.

See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components.

## Where to store images

[Section titled “Where to store images”](#where-to-store-images)

### `src/` vs `public/`

[Section titled “src/ vs public/”](#src-vs-public)

We recommend that local images are kept in `src/` when possible so that Astro can transform, optimize, and bundle them. Files in the `public/` directory are always served or copied into the build folder as-is, with no processing.

Your local images stored in `src/` can be used by all files in your project: `.astro`, `.md`, `.mdx`, `.mdoc`, and other UI frameworks as file imports. Images can be stored in any folder, including alongside your content.

Store your images in the `public/` folder if you want to avoid any processing. These images are available to your project files as URL paths on your domain and allow you to have a direct public link to them. For example, your site favicon will commonly be placed in the root of this folder where browsers can identify it.

### Remote images

[Section titled “Remote images”](#remote-images)

You can also choose to store your images remotely, in a [content management system (CMS)](/en/guides/cms/) or [digital asset management (DAM)](/en/guides/media/) platform. Astro can fetch your data remotely using APIs or display images from their full URL path.

For extra protection when dealing with external sources, Astro’s image components and helper function will only process (e.g. optimize, transform) images from [authorized image sources specified in your configuration](#authorizing-remote-images). Remote images from other sources will be displayed with no processing.

## Images in `.astro` files

[Section titled “Images in .astro files”](#images-in-astro-files)

**Options:** `<Image />`, `<Picture />`, `<img>`, `<svg>`, SVG components

Astro’s templating language allows you to render optimized images with the Astro [`<Image />`](/en/reference/modules/astro-assets/#image-) component and generate multiple sizes and formats with the Astro [`<Picture />`](/en/reference/modules/astro-assets/#picture-) component. Both components also accept [responsive image properties](#responsive-image-behavior) for resizing based on container size and responding to device screen size and resolution.

Additionally, you can import and use [SVG files as Astro components](#svg-components) in `.astro` components.

All native HTML tags, including `<img>` and `<svg>`, are also available in `.astro` components. [Images rendered with HTML tags](#display-unprocessed-images-with-the-html-img-tag) will not be processed (e.g. optimized, transformed) and will be copied into your build folder as-is.

For all images in `.astro` files, **the value of the image `src` attribute is determined by the location of your image file**:

* A local image from your project `src/` folder uses an import from the file’s relative path.

  The image and picture components use the named import directly (e.g. `src={rocket}`), while the `<img>` tag uses the `src` object property of the import (e.g. `src={rocket.src}`).

* Remote and `public/` images use a URL path.

  Provide a full URL for remote images (e.g. `src="https://www.example.com/images/my-remote-image.jpg"`), or a relative URL path on your site that corresponds to your file’s location in your `public/` folder (e.g. `src="/images/my-public-image.jpg"` for an image located in `public/images/my-public-image.jpg`).

src/pages/blog/my-images.astro

```astro
---
import { Image } from 'astro:assets';
import localBirdImage from '../../images/subfolder/localBirdImage.png';
---
<Image src={localBirdImage} alt="A bird sitting on a nest of eggs." />
<Image src="/images/bird-in-public-folder.jpg" alt="A bird." width="50" height="50" />
<Image src="https://example.com/remote-bird.jpg" alt="A bird." width="50" height="50" />


<img src={localBirdImage.src} alt="A bird sitting on a nest of eggs.">
<img src="/images/bird-in-public-folder.jpg" alt="A bird.">
<img src="https://example.com/remote-bird.jpg" alt="A bird.">
```

See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components including required and optional properties.

![](/houston_chef.webp) **Related recipe:** [Dynamically import images](/en/recipes/dynamically-importing-images/)

## Images in Markdown files

[Section titled “Images in Markdown files”](#images-in-markdown-files)

**Options:** `![]()`, `<img>` (with public or remote images)

Use standard Markdown `![alt](src)` syntax in your `.md` files. Your local images stored in `src/` and remote images will be processed and optimized. When you [configure responsive images globally](/en/reference/configuration-reference/#imagelayout), these images will also be [responsive](#responsive-image-behavior).

Images stored in the `public/` folder are never optimized.

src/pages/post-1.md

```md
# My Markdown Page


<!-- Local image stored in src/assets/ -->
<!-- Use a relative file path or import alias -->
![A starry night sky.](../assets/stars.png)


<!-- Image stored in public/images/ -->
<!-- Use the file path relative to public/ -->
![A starry night sky.](/images/stars.png)


<!-- Remote image on another server -->
<!-- Use the full URL of the image -->
![Astro](https://example.com/images/remote-image.png)
```

The HTML `<img>` tag can also be used to display images stored in `public/` or remote images without any image optimization or processing. However, `<img>` is not supported for your local images in `src`.

The `<Image />` and `<Picture />` components are unavailable in `.md` files. If you require more control over your image attributes, we recommend using [Astro’s MDX integration](/en/guides/integrations-guide/mdx/) to add support for `.mdx` file format. MDX allows additional [image options available in MDX](#images-in-mdx-files), including combining components with Markdown syntax.

## Images in MDX files

[Section titled “Images in MDX files”](#images-in-mdx-files)

**Options:** `<Image />`, `<Picture />`, `<img />`, `![]()`, SVG components

You can use Astro’s `<Image />` and `<Picture />` components in your `.mdx` files by importing both the component and your image. Use them just as they are [used in `.astro` files](#images-in-astro-files). The JSX `<img />` tag is also supported for unprocessed images and [uses the same image import as the HTML `<img>` tag](#display-unprocessed-images-with-the-html-img-tag).

Additionally, there is support for [standard Markdown `![alt](src)` syntax](#images-in-markdown-files) with no import required.

src/pages/post-1.mdx

```mdx
---
title: My Page title
---
import { Image } from 'astro:assets';
import rocket from '../assets/rocket.png';


# My MDX Page


// Local image stored in the the same folder
![Houston in the wild](houston.png)


// Local image stored in src/assets/
<Image src={rocket} alt="A rocketship in space." />
<img src={rocket.src} alt="A rocketship in space." />
![A rocketship in space](../assets/rocket.png)


// Image stored in public/images/
<Image src="/images/stars.png" alt="A starry night sky." />
<img src="/images/stars.png" alt="A starry night sky." />
![A starry night sky.](/images/stars.png)


// Remote image on another server
<Image src="https://example.com/images/remote-image.png" />
<img src="https://example.com/images/remote-image.png" />
![Astro](https://example.com/images/remote-image.png)
```

See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components.

## Images in UI framework components

[Section titled “Images in UI framework components”](#images-in-ui-framework-components)

**Image options:** the framework’s own image syntax (e.g. `<img />` in JSX, `<img>` in Svelte)

[Local images must first be imported](#display-unprocessed-images-with-the-html-img-tag) to access their image properties such as `src`. Then, they can be rendered as you normally would in that framework’s own image syntax:

src/components/ReactImage.jsx

```jsx
import stars from "../assets/stars.png";


export default function ReactImage() {
  return (
    <img src={stars.src} alt="A starry night sky." />
  )
}
```

src/components/SvelteImage.svelte

```svelte
<script>
  import stars from '../assets/stars.png';
</script>


<img src={stars.src} alt="A starry night sky." />
```

Astro components (e.g. `<Image />`, `<Picture />`, SVG components) are unavailable inside UI framework components because [a client island must contain only valid code for its own framework](/en/guides/framework-components/#can-i-use-astro-components-inside-my-framework-components).

But, you can pass the static content generated by these components to a framework component inside a `.astro` file [as children](/en/guides/framework-components/#passing-children-to-framework-components) or using a [named `<slot/>`](/en/guides/framework-components/#can-i-use-astro-components-inside-my-framework-components):

src/components/ImageWrapper.astro

```astro
---
import ReactComponent from './ReactComponent.jsx';
import { Image } from 'astro:assets';
import stars from '~/stars/docline.png';
---


<ReactComponent>
  <Image src={stars} alt="A starry night sky." />
</ReactComponent>
```

## Astro components for images

[Section titled “Astro components for images”](#astro-components-for-images)

Astro provides two built-in Astro components for images (`<Image />` and `<Picture />`) and also allows you to import SVG files and use them as Astro components. These components may be used in any files that can import and render `.astro` components.

### `<Image />`

[Section titled “\<Image />”](#image-)

Use the built-in `<Image />` Astro component to display optimized versions of:

* your local images located within the `src/` folder
* [configured remote images](#authorizing-remote-images) from authorized sources

`<Image />` can transform a local or authorized remote image’s dimensions, file type, and quality for control over your displayed image. This transformation happens at build time for prerendered pages. When your page is rendered on demand, this transformation will occur on the fly when the page is viewed. The resulting `<img>` tag includes `alt`, `loading`, and `decoding` attributes and infers image dimensions to avoid Cumulative Layout Shift (CLS).

What is Cumulative Layout Shift?

[Cumulative Layout Shift (CLS)](https://web.dev/cls/) is a Core Web Vital metric for measuring how much content shifted on your page during loading. The `<Image />` component optimizes for CLS by automatically setting the correct `width` and `height` for your images.

src/components/MyComponent.astro

```astro
---
// import the Image component and the image
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png'; // Image is 1600x900
---


<!-- `alt` is mandatory on the Image component -->
<Image src={myImage} alt="A description of my image." />
```

```html
<!-- Prerendered output -->
<!-- Image is optimized, proper attributes are enforced -->
<img
  src="/_astro/my_image.hash.webp"
  width="1600"
  height="900"
  decoding="async"
  loading="lazy"
  alt="A description of my image."
/>


<!-- Output rendered on demand-->
<!-- src will use an endpoint generated on demand-->
<img
  src="/_image?href=%2F_astro%2Fmy_image.hash.webp&amp;w=1600&amp;h=900&amp;f=webp"
  <!-- ... -->
/>
```

The `<Image />` component accepts [several component properties](/en/reference/modules/astro-assets/#image-properties) as well as any attributes accepted by the HTML `<img>` tag.

The following example provides a `class` to the image component which will apply to the final `<img>` element.

src/pages/index.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---


<!-- `alt` is mandatory on the Image component -->
<Image src={myImage} alt="" class="my-class" />
```

```html
<!-- Prerendered output -->
<img
  src="/_astro/my_image.hash.webp"
  width="1600"
  height="900"
  decoding="async"
  loading="lazy"
  class="my-class"
  alt=""
/>
```

Tip

You can also use the `<Image />` component for images in the `public/` folder, or remote images not specifically configured in your project, even though these images will not be optimized or processed. The resulting image will be the same as using the HTML `<img>`.

However, using the image component for all images provides a consistent authoring experience and prevents Cumulative Layout Shift (CLS) even for your unoptimized images.

### `<Picture />`

[Section titled “\<Picture />”](#picture-)

**Added in:** `astro@3.3.0`

Use the built-in `<Picture />` Astro component to generate a `<picture>` tag with multiple formats and/or sizes of your image. This allows you to specify preferred file formats to display and at the same time, provide a fallback format. Like the [`<Image />` component](#image-), images will be processed at build time for prerendered pages. When your page is rendered on demand, processing will occur on the fly when the page is viewed.

The following example uses the `<Picture />` component to transform a local `.png` file into a web-friendly `avif` and `webp` format as well as the `.png` `<img>` that can be displayed as a fallback when needed:

src/pages/index.astro

```astro
---
import { Picture } from 'astro:assets';
import myImage from '../assets/my_image.png'; // Image is 1600x900
---


<!-- `alt` is mandatory on the Picture component -->
<Picture src={myImage} formats={['avif', 'webp']} alt="A description of my image." />
```

```html
<!-- Prerendered output -->
<picture>
  <source srcset="/_astro/my_image.hash.avif" type="image/avif" />
  <source srcset="/_astro/my_image.hash.webp" type="image/webp" />
  <img
    src="/_astro/my_image.hash.png"
    width="1600"
    height="900"
    decoding="async"
    loading="lazy"
    alt="A description of my image."
  />
</picture>
```

See details about [the `<Picture />` component properties](/en/reference/modules/astro-assets/#picture-properties) in the `astro:assets` reference.

### Responsive image behavior

[Section titled “Responsive image behavior”](#responsive-image-behavior)

**Added in:** `astro@5.10.0`

Responsive images are images that adjust to improve performance across different devices. These images can resize to fit their container, and can be served in different sizes depending on your visitor’s screen size and resolution.

With [responsive image properties](/en/reference/modules/astro-assets/#responsive-image-properties) applied to the `<Image />` or `<Picture />` components, Astro will automatically generate the required `srcset` and `sizes` values for your images, and apply the necessary [styles to ensure they resize correctly](#responsive-image-styles).

When this responsive behavior is [configured globally with `image.layout`](/en/reference/configuration-reference/#imagelayout), it will apply to all image components and also to any local and remote images using [the Markdown `![]()` syntax](/en/guides/images/#images-in-markdown-files).

Images in your `public/` folder are never optimized, and responsive images are not supported.

Note

A single responsive image will generate multiple images of different sizes so that the browser can show the best one to your visitor.

For prerendered pages, this happens during the build and may increase the build time of your project, especially if you have a large number of images.

For pages rendered on-demand, the images are generated as-needed when a page is visited. This has no impact on build times but may increase the number of image transformations performed when an image is displayed. Depending on your image service this may incur additional costs.

Read more about [responsive images on MDN web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images).

#### Generated HTML output for responsive images

[Section titled “Generated HTML output for responsive images”](#generated-html-output-for-responsive-images)

When a layout is set, either by default or on an individual component, images have automatically generated `srcset` and `sizes` attributes based on the image’s dimensions and the layout type. Images with `constrained` and `full-width` layouts will have styles applied to ensure they resize according to their container.

src/components/MyComponent.astro

```astro
---
import { Image } from 'astro:assets';
import myImage from '../assets/my_image.png';
---
<Image src={myImage} alt="A description of my image." layout='constrained' width={800} height={600} />
```

This `<Image />` component will generate the following HTML output on a prerendered page:

```html
<img
  src="/_astro/my_image.hash3.webp"
  srcset="/_astro/my_image.hash1.webp 640w,
      /_astro/my_image.hash2.webp 750w,
      /_astro/my_image.hash3.webp 800w,
      /_astro/my_image.hash4.webp 828w,
      /_astro/my_image.hash5.webp 1080w,
      /_astro/my_image.hash6.webp 1280w,
      /_astro/my_image.hash7.webp 1600w"
  alt="A description of my image"
  sizes="(min-width: 800px) 800px, 100vw"
  loading="lazy"
  decoding="async"
  fetchpriority="auto"
  width="800"
  height="600"
  style="--fit: cover; --pos: center;"
  data-astro-image="constrained"
>
```

#### Responsive image styles

[Section titled “Responsive image styles”](#responsive-image-styles)

Setting [`image.responsiveStyles: true`](/en/reference/configuration-reference/#imageresponsivestyles) applies a small number of global styles to ensure that your images resize correctly. In most cases, you will want to enable these as a default; your images will not be responsive without additional styles.

However, if you prefer to handle responsive image styling yourself, or need to [override these defaults when using Tailwind 4](#responsive-images-with-tailwind-4), leave the default `false` value configured.

The global styles applied by Astro will depend on the layout type, and are designed to produce the best result for the generated `srcset` and `sizes` attributes. These are the default styles:

Responsive Image Styles

```css
:where([data-astro-image]) {
  object-fit: var(--fit);
  object-position: var(--pos);
}
:where([data-astro-image='full-width']) {
  width: 100%;
}
:where([data-astro-image='constrained']) {
  max-width: 100%;
}
```

The styles use the [`:where()` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:where), which has a [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity) of 0, meaning that it is easy to override with your own styles. Any CSS selector will have a higher specificity than `:where()`, so you can easily override the styles by adding your own styles to target the image.

You can override the `object-fit` and `object-position` styles on a per-image basis by setting the `fit` and `position` props on the `<Image />` or `<Picture />` component.

#### Responsive images with Tailwind 4

[Section titled “Responsive images with Tailwind 4”](#responsive-images-with-tailwind-4)

Tailwind 4 is compatible with Astro’s default responsive styles. However, Tailwind uses [cascade layers](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer), meaning that its rules are always lower specificity than rules that don’t use layers, including Astro’s responsive styles. Therefore, Astro’s styling will take precedence over Tailwind styling. To use Tailwind rules instead of Astro’s default styling, do not enable [Astro’s default responsive styles](/en/reference/configuration-reference/#imageresponsivestyles).

### SVG components

[Section titled “SVG components”](#svg-components)

**Added in:** `astro@5.7.0`

Astro allows you to import SVG files and use them as Astro components. Astro will inline the SVG content into your HTML output.

Reference the default import of any local `.svg` file. Since this import is treated as an Astro component, you must use the same conventions (e.g. capitalization) as when [using dynamic tags](/en/reference/astro-syntax/#dynamic-tags).

src/components/MyAstroComponent.astro

```astro
---
import Logo from './path/to/svg/file.svg';
---


<Logo />
```

Your SVG component, like `<Image />` or any other Astro component, is unavailable inside UI framework components, but can [be passed to a framework component](#images-in-ui-framework-components) inside a `.astro` component.

#### SVG component attributes

[Section titled “SVG component attributes”](#svg-component-attributes)

You can pass props such as `width`, `height`, `fill`, `stroke`, and any other attribute accepted by the [native `<svg>` element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg). These attributes will automatically be applied to the underlying `<svg>` element. If a property is present in the original `.svg` file and is passed to the component, the value passed to the component will override the original value.

src/components/MyAstroComponent.astro

```astro
---
import Logo from '../assets/logo.svg';
---


<Logo width={64} height={64} fill="currentColor" />
```

#### `SvgComponent` Type

[Section titled “SvgComponent Type”](#svgcomponent-type)

**Added in:** `astro@5.14.0`

You can also enforce type safety for your `.svg` assets using the `SvgComponent` type:

src/components/Logo.astro

```astro
---
import type { SvgComponent } from "astro/types";
import HomeIcon from './Home.svg'


interface Link {
  url: string
  text: string
  icon: SvgComponent
}


const links: Link[] = [
  {
    url: '/',
    text: 'Home',
    icon: HomeIcon
  }
]
---
```

### Creating custom image components

[Section titled “Creating custom image components”](#creating-custom-image-components)

You can create a custom, reusable image component by wrapping the `<Image />` or `<Picture/>` component in another Astro component. This allows you to set default attributes and styles only once.

For example, you could create a component for your blog post images that receives attributes as props and applies consistent styles to each image:

src/components/BlogPostImage.astro

```astro
---
import { Image } from 'astro:assets';


const { src, ...attrs } = Astro.props;
---
<Image src={src} {...attrs} />


<style>
  img {
    margin-block: 2.5rem;
    border-radius: 0.75rem;
  }
</style>
```

## Display unprocessed images with the HTML `<img>` tag

[Section titled “Display unprocessed images with the HTML \<img> tag”](#display-unprocessed-images-with-the-html-img-tag)

The [Astro template syntax](/en/reference/astro-syntax/) also supports writing an `<img>` tag directly, with full control over its final output. These images will not be processed and optimized. It accepts all HTML `<img>` tag properties, and the only required property is `src`. However, it is strongly recommended to include [the `alt` property for accessibility](#alt-text).

### images in `src/`

[Section titled “images in src/”](#images-in-src)

Local images must be imported from the relative path from the existing `.astro` file, or you can configure and use an [import alias](/en/guides/imports/#aliases). Then, you can access the image’s `src` and other properties to use in the `<img>` tag.

Imported image assets match the following signature:

```ts
interface ImageMetadata {
  src: string;
  width: number;
  height: number;
  format: string;
}
```

The following example uses the image’s own `height` and `width` properties to avoid Cumulative Layout Shift (CLS) and improve Core Web Vitals:

src/pages/posts/post-1.astro

```astro
---
// import local images
import myDog from '../../images/pets/local-dog.jpg';
---
// access the image properties
<img src={myDog.src} width={myDog.width} height={myDog.height} alt="A barking dog." />
```

### Images in `public/`

[Section titled “Images in public/”](#images-in-public)

For images located within `public/` use the image’s file path relative to the public folder as the `src` value:

```astro
<img src="/images/public-cat.jpg" alt="A sleeping cat." >
```

### Remote images

[Section titled “Remote images”](#remote-images-1)

For remote images, use the image’s full URL as the `src` value:

```astro
<img src="https://example.com/remote-cat.jpg" alt="A sleeping cat." >
```

### Choosing `<Image />` vs `<img>`

[Section titled “Choosing \<Image /> vs \<img>”](#choosing-image--vs-img)

The `<Image />` component optimizes your image and infers width and height (for images it can process) based on the original aspect ratio to avoid CLS. It is the preferred way to use images in `.astro` files whenever possible.

Use the HTML `<img>` element when you cannot use the `<Image />` component, for example:

* for unsupported image formats
* when you do not want your image optimized by Astro
* to access and change the `src` attribute dynamically client-side

## Using Images from a CMS or CDN

[Section titled “Using Images from a CMS or CDN”](#using-images-from-a-cms-or-cdn)

Image CDNs work with [all Astro image options](#images-in-astro-files). Use an image’s full URL as the `src` attribute in the `<Image />` component, an `<img>` tag, or in Markdown notation. For image optimization with remote images, also [configure your authorized domains or URL patterns](#authorizing-remote-images).

Alternatively, the CDN may provide its own SDKs to more easily integrate in an Astro project. For example, Cloudinary supports an [Astro SDK](https://astro.cloudinary.dev/) which allows you to easily drop in images with their `CldImage` component or a [Node.js SDK](https://cloudinary.com/documentation/node_integration) that can generate URLs to use with an `<img>` tag in a Node.js environment.

See the full API reference for the [`<Image />`](/en/reference/modules/astro-assets/#image-) and [`<Picture />`](/en/reference/modules/astro-assets/#picture-) components.

## Authorizing remote images

[Section titled “Authorizing remote images”](#authorizing-remote-images)

You can configure lists of authorized image source URL domains and patterns for image optimization using [`image.domains`](/en/reference/configuration-reference/#imagedomains) and [`image.remotePatterns`](/en/reference/configuration-reference/#imageremotepatterns). This configuration is an extra layer of safety to protect your site when showing images from an external source.

Remote images from other sources will not be optimized, but using the `<Image />` component for these images will prevent Cumulative Layout Shift (CLS).

For example, the following configuration will only allow remote images from `astro.build` to be optimized:

astro.config.mjs

```ts
export default defineConfig({
  image: {
    domains: ["astro.build"],
  }
});
```

The following configuration will only allow remote images from HTTPS hosts:

astro.config.mjs

```ts
export default defineConfig({
  image: {
    remotePatterns: [{ protocol: "https" }],
  }
});
```

## Images in content collections

[Section titled “Images in content collections”](#images-in-content-collections)

You can declare an associated image for a content collections entry, such as a blog post’s cover image, in your frontmatter using its path relative to the current folder:

src/content/blog/my-post.md

```md
---
title: "My first blog post"
cover: "./firstpostcover.jpeg" # will resolve to "src/content/blog/firstblogcover.jpeg"
coverAlt: "A photograph of a sunset behind a mountain range."
---


This is a blog post
```

The `image` helper for the content collections schema lets you validate and import the image.

src/content.config.ts

```ts
import { defineCollection, z } from "astro:content";


const blogCollection = defineCollection({
  schema: ({ image }) => z.object({
    title: z.string(),
    cover: image(),
    coverAlt: z.string(),
  }),
});


export const collections = {
  blog: blogCollection,
};
```

The image will be imported and transformed into metadata, allowing you to pass it as a `src` to `<Image/>`, `<img>`, or `getImage()` in an Astro component.

The example below shows a blog index page that renders the cover photo and title of each blog post from the previous schema:

src/pages/blog.astro

```astro
---
import { Image } from "astro:assets";
import { getCollection } from "astro:content";
const allBlogPosts = await getCollection("blog");
---


{
  allBlogPosts.map((post) => (
    <div>
      <Image src={post.data.cover} alt={post.data.coverAlt} />
      <h2>
        <a href={"/blog/" + post.slug}>{post.data.title}</a>
      </h2>
    </div>
  ))
}
```

## Generating images with `getImage()`

[Section titled “Generating images with getImage()”](#generating-images-with-getimage)

The `getImage()` function is intended for generating images destined to be used somewhere else than directly in HTML, for example in an [API Route](/en/guides/endpoints/#server-endpoints-api-routes). When you need options that the `<Picture>` and `<Image>` components do not currently support, you can use the `getImage()` function to create your own custom `<Image />` component.

See more in the [`getImage()` reference](/en/reference/modules/astro-assets/#getimage).

![](/houston_chef.webp) **Related recipe:** [Build a custom image component](/en/recipes/build-custom-img-component/)

## Alt Text

[Section titled “Alt Text”](#alt-text)

Not all users can see images in the same way, so accessibility is an especially important concern when using images. Use the `alt` attribute to provide [descriptive alt text](https://www.w3.org/WAI/tutorials/images/) for images.

This attribute is required for both the `<Image />` and `<Picture />` components. If no alt text is provided, a helpful error message will be provided reminding you to include the `alt` attribute.

If the image is merely decorative (i.e. doesn’t contribute to the understanding of the page), set `alt=""` so that screen readers know to ignore the image.

## Default image service

[Section titled “Default image service”](#default-image-service)

[Sharp](https://github.com/lovell/sharp) is the default image service used for `astro:assets`. You can further configure the image service using the [`image.service`](/en/reference/configuration-reference/#imageservice) option.

Note

When using a [strict package manager](https://pnpm.io/pnpm-vs-npm#npms-flat-tree) like `pnpm`, you may need to manually install Sharp into your project even though it is an Astro dependency:

```bash
pnpm add sharp
```

### Configure no-op passthrough service

[Section titled “Configure no-op passthrough service”](#configure-no-op-passthrough-service)

If your [adapter](https://astro.build/integrations/?search=\&categories%5B%5D=adapters) does not support Astro’s built-in Sharp image optimization (e.g. Deno, Cloudflare), you can configure a no-op image service to allow you to use the `<Image />` and `<Picture />` components. Note that Astro does not perform any image transformation and processing in these environments. However, you can still enjoy the other benefits of using `astro:assets`, including no Cumulative Layout Shift (CLS), the enforced `alt` attribute, and a consistent authoring experience.

Configure the `passthroughImageService()` to avoid Sharp image processing:

astro.config.mjs

```diff
import { defineConfig, passthroughImageService } from 'astro/config';


export default defineConfig({
+  image: {
+    service: passthroughImageService()
+  }
});
```

## Asset Caching

[Section titled “Asset Caching”](#asset-caching)

Astro stores processed image assets in a cache directory during site builds for both local and [remote images from authorized sources](#authorizing-remote-images). By preserving the cache directory between builds, processed assets are reused, improving build time and bandwidth usage.

The default cache directory is `./node_modules/.astro`, however this can be changed using the [`cacheDir`](/en/reference/configuration-reference/#cachedir) configuration setting.

### Remote Images

[Section titled “Remote Images”](#remote-images-2)

Remote images in the asset cache are managed based on [HTTP Caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching), and respect the [Cache-Control header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) returned by the remote server. Images are cached if the Cache-Control header allows, and will be used until they are no longer [fresh](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#fresh_and_stale_based_on_age).

#### Revalidation

[Section titled “Revalidation”](#revalidation)

**Added in:** `astro@5.1.0`

[Revalidation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#validation) reduces bandwidth usage and build time by checking with the remote server whether an expired cached image is still up-to-date. If the server indicates that the image is still fresh, the cached version is reused, otherwise the image is redownloaded.

Revalidation requires that the remote server send [Last-Modified](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified) and/or [Etag (entity tag)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) headers with its responses. This feature is available for remote servers that support the [If-Modified-Since](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since) and [If-None-Match](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match) headers.

## Community Integrations

[Section titled “Community Integrations”](#community-integrations)

There are several third-party [community image integrations](https://astro.build/integrations?search=images) for optimizing and working with images in your Astro project.

# Imports reference

> Learn how to import different file types into your Astro project.

Astro supports most static assets with zero configuration required. You can use the `import` statement anywhere in your project JavaScript (including your Astro frontmatter) and Astro will include a built, optimized copy of that static asset in your final build. `@import` is also supported inside of CSS & `<style>` tags.

## Supported File Types

[Section titled “Supported File Types”](#supported-file-types)

The following file types are supported out-of-the-box by Astro:

* Astro Components (`.astro`)
* Markdown (`.md`, `.markdown`, etc.)
* JavaScript (`.js`, `.mjs`)
* TypeScript (`.ts`)
* NPM Packages
* JSON (`.json`)
* CSS (`.css`)
* CSS Modules (`.module.css`)
* Images & Assets (`.svg`, `.jpg`, `.png`, etc.)

Additionally, you can extend Astro to add support for different [UI Frameworks](/en/guides/framework-components/) like React, Svelte and Vue components. You can also install the [Astro MDX integration](/en/guides/integrations-guide/mdx/) or the [Astro Markdoc integration](/en/guides/integrations-guide/markdoc/) to use `.mdx` or `.mdoc` files in your project.

### Files in `public/`

[Section titled “Files in public/”](#files-in-public)

You can place any static asset in the [`public/` directory](/en/basics/project-structure/#public) of your project, and Astro will copy it directly into your final build untouched. `public/` files are not built or bundled by Astro, which means that any type of file is supported.

You can reference a `public/` file by a URL path directly in your HTML templates.

```astro
// To link to /public/reports/annual/2024.pdf
Download the <a href="/reports/annual/2024.pdf">2024 annual statement as a PDF</a>.


// To display /public/assets/cats/ginger.jpg
<img src="/assets/cats/ginger.jpg" alt="An orange cat sleeping on a bed.">
```

## Import statements

[Section titled “Import statements”](#import-statements)

Astro uses ESM, the same [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#syntax) and [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) syntax supported in the browser.

### JavaScript

[Section titled “JavaScript”](#javascript)

```js
import { getUser } from './user.js';
```

JavaScript can be imported using normal ESM `import` & `export` syntax.

Importing JSX files

An appropriate [UI framework](/en/guides/framework-components/) ([React](/en/guides/integrations-guide/react/), [Preact](/en/guides/integrations-guide/preact/), or [Solid](/en/guides/integrations-guide/solid-js/)) is required to render JSX/TSX files. Use `.jsx`/`.tsx` extensions where appropriate, as Astro does not support JSX in `.js`/`.ts` files.

### TypeScript

[Section titled “TypeScript”](#typescript)

```js
import { getUser } from './user';
import type { UserType } from './user';
```

Astro includes built-in support for [TypeScript](https://www.typescriptlang.org/). You can import `.ts` and `.tsx` files directly in your Astro project, and even write TypeScript code directly inside your [Astro component script](/en/basics/astro-components/#the-component-script) and any [script tags](/en/guides/client-side-scripts/).

**Astro doesn’t perform any type checking itself.** Type checking should be taken care of outside of Astro, either by your IDE or through a separate script. For type checking Astro files, the [`astro check` command](/en/reference/cli-reference/#astro-check) is provided.

TypeScript and file extensions

Per [TypeScript’s module resolution rules](https://www.typescriptlang.org/docs/handbook/module-resolution.html), `.ts` and `.tsx` file extensions should not be used when importing TypeScript files. Instead, either use `.js`/`.jsx` file extensions or completely omit the file extension.

```ts
import { getUser } from './user.js'; // user.ts
import MyComponent from "./MyComponent"; // MyComponent.tsx
```

Read more about [TypeScript support in Astro](/en/guides/typescript/).

### NPM Packages

[Section titled “NPM Packages”](#npm-packages)

If you’ve installed an NPM package, you can import it in Astro.

```astro
---
import { Icon } from 'astro-icon';
---
```

If a package was published using a legacy format, Astro will try to convert the package to ESM so that `import` statements work. In some cases, you may need to adjust your [`vite` config](/en/reference/configuration-reference/#vite) for it to work.

Caution

Some packages rely on a browser environment. Astro components runs on the server, so importing these packages in the frontmatter may [lead to errors](/en/guides/troubleshooting/#document-or-window-is-not-defined).

### JSON

[Section titled “JSON”](#json)

```js
// Load the JSON object via the default export
import json from './data.json';
```

Astro supports importing JSON files directly into your application. Imported files return the full JSON object in the default import.

### CSS

[Section titled “CSS”](#css)

```js
// Load and inject 'style.css' onto the page
import './style.css';
```

Astro supports importing CSS files directly into your application. Imported styles expose no exports, but importing one will automatically add those styles to the page. This works for all CSS files by default, and can support compile-to-CSS languages like Sass & Less via plugins.

Read more about advanced CSS import use cases such as a direct URL reference for a CSS file, or importing CSS as a string in the [Styling guide](/en/guides/styling/#advanced).

### CSS Modules

[Section titled “CSS Modules”](#css-modules)

```jsx
// 1. Converts './style.module.css' classnames to unique, scoped values.
// 2. Returns an object mapping the original classnames to their final, scoped value.
import styles from './style.module.css';


// This example uses JSX, but you can use CSS Modules with any framework.
return <div className={styles.error}>Your Error Message</div>;
```

Astro supports CSS Modules using the `[name].module.css` naming convention. Like any CSS file, importing one will automatically apply that CSS to the page. However, CSS Modules export a special default `styles` object that maps your original classnames to unique identifiers.

CSS Modules help you enforce component scoping & isolation on the frontend with uniquely-generated class names for your stylesheets.

### Other Assets

[Section titled “Other Assets”](#other-assets)

```jsx
// Returns an object with `src` and other properties
import imgReference from './image.png';
import svgReference from './image.svg';


// HTML or UI Framework components use this to render the image
<img src={imgReference.src} alt="image description" />;


// The Astro `<Image />` and `<Picture />` components access `src` by default
<Image src={imgReference} alt="image description">
```

All other assets not explicitly mentioned above can be imported via ESM `import` and will return a URL reference to the final built asset (e.g. `/_astro/my-video.C7vXpQtF.mp4`) instead of an object.

This can be useful for referencing non-JS assets by URL, like creating a video element with a `src` attribute pointing to that image.

It can also be useful to place images and other assets in the `public/` folder as explained on the [project-structure page](/en/basics/project-structure/#public).

Read more about appending Vite import parameters (e.g. `?url`, `?raw`) in [Vite’s static asset handling guide](https://vite.dev/guide/assets.html).

Note

Adding **alt text** to `<img>` tags is encouraged for accessibility! Don’t forget to add an `alt="a helpful description"` attribute to your image elements. You can just leave the attribute empty if the image is purely decorative.

## Aliases

[Section titled “Aliases”](#aliases)

An **alias** is a way to create shortcuts for your imports.

Aliases can help improve the development experience in codebases with many directories or relative imports.

src/pages/about/company.astro

```astro
---
import Button from '../../components/controls/Button.astro';
import logoUrl from '../../assets/logo.png?url';
---
```

In this example, a developer would need to understand the tree relationship between `src/pages/about/company.astro`, `src/components/controls/Button.astro`, and `src/assets/logo.png`. And then, if the `company.astro` file were to be moved, these imports would also need to be updated.

You can add import aliases in `tsconfig.json`.

tsconfig.json

```diff
{
  "compilerOptions": {
    "paths": {
      +"@components/*": ["./src/components/*"],
      +"@assets/*": ["./src/assets/*"]
    }
  }
}
```

The development server will automatically restart after this configuration change. You can now import using the aliases anywhere in your project:

src/pages/about/company.astro

```astro
---
import Button from '@components/controls/Button.astro';
import logoUrl from '@assets/logo.png?url';
---
```

## `import.meta.glob()`

[Section titled “import.meta.glob()”](#importmetaglob)

[Vite’s `import.meta.glob()`](https://vite.dev/guide/features.html#glob-import) is a way to import many files at once using glob patterns to find matching file paths.

`import.meta.glob()` takes a relative [glob pattern](#glob-patterns) matching the local files you’d like to import as a parameter. It returns an array of each matching file’s exports. To load all matched modules up front, pass `{ eager: true }` as the second argument:

src/components/my-component.astro

```astro
---
// imports all files that end with `.md` in `./src/pages/post/`
const matches = import.meta.glob('../pages/post/*.md', { eager: true });
const posts = Object.values(matches);
---
<!-- Renders an <article> for the first 5 blog posts -->
<div>
{posts.slice(0, 4).map((post) => (
  <article>
    <h2>{post.frontmatter.title}</h2>
    <p>{post.frontmatter.description}</p>
    <a href={post.url}>Read more</a>
  </article>
))}
</div>
```

Astro components imported using `import.meta.glob` are of type [`AstroInstance`](#astro-files). You can render each component instance using its `default` property:

src/pages/component-library.astro

```astro
---
// imports all files that end with `.astro` in `./src/components/`
const components = Object.values(import.meta.glob('../components/*.astro', { eager: true }));
---
<!-- Display all of our components -->
{components.map((component) => (
  <div>
    <component.default size={24} />
  </div>
))}
```

### Supported Values

[Section titled “Supported Values”](#supported-values)

Vite’s `import.meta.glob()` function only supports static string literals. It does not support dynamic variables and string interpolation.

A common workaround is to instead import a larger set of files that includes all the files you need, then filter them:

src/components/featured.astro

```astro
---
const { postSlug } = Astro.props;
const pathToMyFeaturedPost = `src/pages/blog/${postSlug}.md`;


const posts = Object.values(import.meta.glob("../pages/blog/*.md", { eager: true }));
const myFeaturedPost = posts.find(post => post.file.includes(pathToMyFeaturedPost));
---


<p>
  Take a look at my favorite post, <a href={myFeaturedPost.url}>{myFeaturedPost.frontmatter.title}</a>!
</p>
```

### Import type utilities

[Section titled “Import type utilities”](#import-type-utilities)

#### Markdown files

[Section titled “Markdown files”](#markdown-files)

Markdown files loaded with `import.meta.glob()` return the following `MarkdownInstance` interface:

```ts
export interface MarkdownInstance<T extends Record<string, any>> {
  /* Any data specified in this file's YAML/TOML frontmatter */
  frontmatter: T;
  /* The absolute file path of this file */
  file: string;
  /* The rendered path of this file */
  url: string | undefined;
  /* Astro Component that renders the contents of this file */
  Content: AstroComponentFactory;
  /** (Markdown only) Raw Markdown file content, excluding layout HTML and YAML/TOML frontmatter */
  rawContent(): string;
  /** (Markdown only) Markdown file compiled to HTML, excluding layout HTML */
  compiledContent(): string;
  /* Function that returns an array of the h1...h6 elements in this file */
  getHeadings(): Promise<{ depth: number; slug: string; text: string }[]>;
  default: AstroComponentFactory;
}
```

You can optionally provide a type for the `frontmatter` variable using a TypeScript generic.

```astro
---
import type { MarkdownInstance } from 'astro';
interface Frontmatter {
    title: string;
    description?: string;
}


const posts = Object.values(import.meta.glob<MarkdownInstance<Frontmatter>>('./posts/**/*.md', { eager: true }));
---


<ul>
  {posts.map(post => <li>{post.frontmatter.title}</li>)}
</ul>
```

#### Astro files

[Section titled “Astro files”](#astro-files)

Astro files have the following interface:

```ts
export interface AstroInstance {
  /* The file path of this file */
  file: string;
  /* The URL for this file (if it is in the pages directory) */
  url: string | undefined;
  default: AstroComponentFactory;
}
```

#### Other files

[Section titled “Other files”](#other-files)

Other files may have various different interfaces, but `import.meta.glob()` accepts a TypeScript generic if you know exactly what an unrecognized file type contains.

```ts
---
interface CustomDataFile {
  default: Record<string, any>;
}
const data = import.meta.glob<CustomDataFile>('../data/**/*.js');
---
```

### Glob Patterns

[Section titled “Glob Patterns”](#glob-patterns)

A glob pattern is a file path that supports special wildcard characters. This is used to reference multiple files in your project at once.

For example, the glob pattern `./pages/**/*.{md,mdx}` starts within the pages subdirectory, looks through all of its subdirectories (`/**`), and matches any filename (`/*`) that ends in either `.md` or `.mdx` (`.{md,mdx}`).

#### Glob Patterns in Astro

[Section titled “Glob Patterns in Astro”](#glob-patterns-in-astro)

To use with `import.meta.glob()`, the glob pattern must be a string literal and cannot contain any variables.

Additionally, glob patterns must begin with one of the following:

* `./` (to start in the current directory)
* `../` (to start in the parent directory)
* `/` (to start at the root of the project)

[Read more about the glob pattern syntax](https://github.com/micromatch/picomatch#globbing-features).

### `import.meta.glob()` vs `getCollection()`

[Section titled “import.meta.glob() vs getCollection()”](#importmetaglob-vs-getcollection)

[Content collections](/en/guides/content-collections/) provide a [`getCollection()` API](/en/reference/modules/astro-content/#getcollection) for loading multiple files instead of `import.meta.glob()`. If your content files (e.g. Markdown, MDX, Markdoc) are located in collections within the `src/content/` directory, use `getCollection()` to [query a collection](/en/guides/content-collections/#querying-collections) and return content entries.

## WASM

[Section titled “WASM”](#wasm)

```js
// Loads and initializes the requested WASM file
const wasm = await WebAssembly.instantiateStreaming(fetch('/example.wasm'));
```

Astro supports loading WASM files directly into your application using the browser’s [`WebAssembly`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly) API.

## Node Builtins

[Section titled “Node Builtins”](#node-builtins)

Astro supports Node.js built-ins, with some limitations, using Node’s newer `node:` prefix. There may be differences between development and production, and some features may be incompatible with on-demand rendering. Some [adapters](/en/guides/on-demand-rendering/) may also be incompatible with these built-ins modules or require configuration to support a subset (e.g., [Cloudflare Workers](/en/guides/integrations-guide/cloudflare/) or [Deno](https://github.com/denoland/deno-astro-adapter)).

The following example imports the `util` module from Node to parse a media type (MIME):

src/components/MyComponent.astro

```astro
---
// Example: import the "util" built-in from Node.js
import util from 'node:util';


export interface Props {
  mimeType: string,
}


const mime = new util.MIMEType(Astro.props.mimeType)
---


<span>Type: {mime.type}</span>
<span>SubType: {mime.subtype}</span>
```

## Extending file type support

[Section titled “Extending file type support”](#extending-file-type-support)

With **Vite** and compatible **Rollup** plugins, you can import file types which aren’t natively supported by Astro. Learn where to find the plugins you need in the [Finding Plugins](https://vite.dev/guide/using-plugins.html#finding-plugins) section of the Vite Documentation.

Plugin configuration

Refer to your plugin’s documentation for configuration options, and how to correctly install it.

![](/houston_chef.webp) **Related recipe:** [Installing a Vite or Rollup plugin](/en/recipes/add-yaml-support/)


---

**Navigation:** [← Previous](./04-optimizely-cms-astro.md) | [Index](./index.md) | [Next →](./06-add-integrations.md)
