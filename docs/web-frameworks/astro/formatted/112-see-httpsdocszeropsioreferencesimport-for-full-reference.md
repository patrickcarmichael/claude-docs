---
title: "see https://docs.zerops.io/references/import for full reference"
section: 112
---

# see https://docs.zerops.io/references/import for full reference
project:
  name: recipe-astro
services:
  - hostname: app
    type: nodejs@20
```jsx
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
  ```jsx
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
  ```jsx
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
  ```jsx
Now you can [trigger the build & deploy pipeline using the Zerops CLI](#trigger-the-pipeline-using-zerops-cli-zcli) or by connecting the `app` service with your [GitHub](https://docs.zerops.io/references/github-integration/) / [GitLab](https://docs.zerops.io/references/gitlab-integration) repository from inside the service detail.

## Trigger the pipeline using Zerops CLI (zcli)

[Section titled “Trigger the pipeline using Zerops CLI (zcli)”](#trigger-the-pipeline-using-zerops-cli-zcli)

1. Install the Zerops CLI.

   ```shell
   # To download the zcli binary directly,
   # use https://github.com/zeropsio/zcli/releases
   npm i -g @zerops/zcli
   ```jsx
2. Open [`Settings > Access Token Management`](https://app.zerops.io/settings/token-management) in the Zerops app and generate a new access token.

3. Log in using your access token with the following command:

   ```shell
   zcli login <token>
   ```jsx
4. Navigate to the root of your app (where `zerops.yml` is located) and run the following command to trigger the deploy:

   ```shell
   zcli push
   ```jsx
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

---

[← Previous](111-see-httpsdocszeropsioreferencesimport-for-full-reference.md) | [Index](index.md) | [Next →](index.md)
