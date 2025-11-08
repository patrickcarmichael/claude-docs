---
title: "see https://docs.zerops.io/references/import for full reference"
section: 111
---

# see https://docs.zerops.io/references/import for full reference
project:
  name: recipe-astro
services:
  - hostname: app
    type: static
```jsx
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
          - pnpm build
        deployFiles:
          - dist/~
      run:
        base: static
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
          - dist/~
      run:
        base: static
  ```jsx
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
```jsx
### Creating a project and a service for Astro SSR (Node.js)

[Section titled “Creating a project and a service for Astro SSR (Node.js)”](#creating-a-project-and-a-service-for-astro-ssr-nodejs)

Projects and services can be added either through a [`Project add`](https://app.zerops.io/dashboard/project-add) wizard or imported using a yaml structure:

```yaml

---

[← Previous](110-deploy-your-astro-site-to-zerops.md) | [Index](index.md) | [Next →](index.md)
