**Navigation:** [← Previous](./07-working-with-ssl-certificates.md) | [Index](./index.md) | [Next →](./09-invalid-request-method.md)

---

# Framework environment variables

Copy page

Ask AI about this page

Last updated July 18, 2025

Frameworks typically use a prefix in order to expose environment variables to the browser.

The following prefixed environment variables will be available during the build step, based on the project's selected [framework preset](/docs/deployments/configure-a-build#framework-preset).

## [Using prefixed framework environment variables locally](#using-prefixed-framework-environment-variables-locally)

Many frontend frameworks require prefixes on environment variable names to make them available to the client, such as `NEXT_PUBLIC_` for Next.js or `PUBLIC_` for SvelteKit. Vercel adds these prefixes automatically for your production and preview deployments, but not for your local development environment.

Framework environment variables are not prefixed when pulled into your local development environment with `vercel env pull`. For example, `VERCEL_ENV` will not be prefixed to `NEXT_PUBLIC_VERCEL_ENV`.

To use framework-prefixed environment variables locally:

1.  [Define them in your project settings](/docs/environment-variables#creating-environment-variables) with the appropriate prefix
2.  Scope them to `Development`
3.  Pull them into your local environment with Vercel CLI using the `vercel env pull` command

## [Framework environment variables](#framework-environment-variables)

Next.jsNuxtCreate React AppGatsby.jsSolidStart (v0)SvelteKit (v0)AstroSolidStart (v1)Vue.jsRedwoodJSHydrogen (v1)ViteSanity (v3)Sanity

### [NEXT\_PUBLIC\_VERCEL\_ENV](#NEXT_PUBLIC_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
NEXT_PUBLIC_VERCEL_ENV=production
```

### [NEXT\_PUBLIC\_VERCEL\_TARGET\_ENV](#NEXT_PUBLIC_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
NEXT_PUBLIC_VERCEL_TARGET_ENV=production
```

### [NEXT\_PUBLIC\_VERCEL\_URL](#NEXT_PUBLIC_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
NEXT_PUBLIC_VERCEL_URL=my-site.vercel.app
```

### [NEXT\_PUBLIC\_VERCEL\_BRANCH\_URL](#NEXT_PUBLIC_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
NEXT_PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [NEXT\_PUBLIC\_VERCEL\_PROJECT\_PRODUCTION\_URL](#NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
NEXT_PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_PROVIDER](#NEXT_PUBLIC_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
NEXT_PUBLIC_VERCEL_GIT_PROVIDER=github
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_REPO\_SLUG](#NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
NEXT_PUBLIC_VERCEL_GIT_REPO_SLUG=my-site
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_REPO\_OWNER](#NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
NEXT_PUBLIC_VERCEL_GIT_REPO_OWNER=acme
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_REPO\_ID](#NEXT_PUBLIC_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
NEXT_PUBLIC_VERCEL_GIT_REPO_ID=117716146
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_COMMIT\_REF](#NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
NEXT_PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_COMMIT\_SHA](#NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
NEXT_PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_COMMIT\_MESSAGE](#NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
NEXT_PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
NEXT_PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [NEXT\_PUBLIC\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
NEXT_PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [NUXT\_ENV\_VERCEL\_ENV](#NUXT_ENV_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
NUXT_ENV_VERCEL_ENV=production
```

### [NUXT\_ENV\_VERCEL\_TARGET\_ENV](#NUXT_ENV_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
NUXT_ENV_VERCEL_TARGET_ENV=production
```

### [NUXT\_ENV\_VERCEL\_URL](#NUXT_ENV_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
NUXT_ENV_VERCEL_URL=my-site.vercel.app
```

### [NUXT\_ENV\_VERCEL\_BRANCH\_URL](#NUXT_ENV_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
NUXT_ENV_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [NUXT\_ENV\_VERCEL\_PROJECT\_PRODUCTION\_URL](#NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
NUXT_ENV_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [NUXT\_ENV\_VERCEL\_GIT\_PROVIDER](#NUXT_ENV_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
NUXT_ENV_VERCEL_GIT_PROVIDER=github
```

### [NUXT\_ENV\_VERCEL\_GIT\_REPO\_SLUG](#NUXT_ENV_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
NUXT_ENV_VERCEL_GIT_REPO_SLUG=my-site
```

### [NUXT\_ENV\_VERCEL\_GIT\_REPO\_OWNER](#NUXT_ENV_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
NUXT_ENV_VERCEL_GIT_REPO_OWNER=acme
```

### [NUXT\_ENV\_VERCEL\_GIT\_REPO\_ID](#NUXT_ENV_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
NUXT_ENV_VERCEL_GIT_REPO_ID=117716146
```

### [NUXT\_ENV\_VERCEL\_GIT\_COMMIT\_REF](#NUXT_ENV_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
NUXT_ENV_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [NUXT\_ENV\_VERCEL\_GIT\_COMMIT\_SHA](#NUXT_ENV_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
NUXT_ENV_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [NUXT\_ENV\_VERCEL\_GIT\_COMMIT\_MESSAGE](#NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
NUXT_ENV_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [NUXT\_ENV\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [NUXT\_ENV\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
NUXT_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [NUXT\_ENV\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
NUXT_ENV_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [REACT\_APP\_VERCEL\_ENV](#REACT_APP_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
REACT_APP_VERCEL_ENV=production
```

### [REACT\_APP\_VERCEL\_TARGET\_ENV](#REACT_APP_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
REACT_APP_VERCEL_TARGET_ENV=production
```

### [REACT\_APP\_VERCEL\_URL](#REACT_APP_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
REACT_APP_VERCEL_URL=my-site.vercel.app
```

### [REACT\_APP\_VERCEL\_BRANCH\_URL](#REACT_APP_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
REACT_APP_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [REACT\_APP\_VERCEL\_PROJECT\_PRODUCTION\_URL](#REACT_APP_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
REACT_APP_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [REACT\_APP\_VERCEL\_GIT\_PROVIDER](#REACT_APP_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
REACT_APP_VERCEL_GIT_PROVIDER=github
```

### [REACT\_APP\_VERCEL\_GIT\_REPO\_SLUG](#REACT_APP_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
REACT_APP_VERCEL_GIT_REPO_SLUG=my-site
```

### [REACT\_APP\_VERCEL\_GIT\_REPO\_OWNER](#REACT_APP_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
REACT_APP_VERCEL_GIT_REPO_OWNER=acme
```

### [REACT\_APP\_VERCEL\_GIT\_REPO\_ID](#REACT_APP_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
REACT_APP_VERCEL_GIT_REPO_ID=117716146
```

### [REACT\_APP\_VERCEL\_GIT\_COMMIT\_REF](#REACT_APP_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
REACT_APP_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [REACT\_APP\_VERCEL\_GIT\_COMMIT\_SHA](#REACT_APP_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
REACT_APP_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [REACT\_APP\_VERCEL\_GIT\_COMMIT\_MESSAGE](#REACT_APP_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
REACT_APP_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [REACT\_APP\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [REACT\_APP\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
REACT_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [REACT\_APP\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#REACT_APP_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
REACT_APP_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [GATSBY\_VERCEL\_ENV](#GATSBY_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
GATSBY_VERCEL_ENV=production
```

### [GATSBY\_VERCEL\_TARGET\_ENV](#GATSBY_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
GATSBY_VERCEL_TARGET_ENV=production
```

### [GATSBY\_VERCEL\_URL](#GATSBY_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
GATSBY_VERCEL_URL=my-site.vercel.app
```

### [GATSBY\_VERCEL\_BRANCH\_URL](#GATSBY_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
GATSBY_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [GATSBY\_VERCEL\_PROJECT\_PRODUCTION\_URL](#GATSBY_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
GATSBY_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [GATSBY\_VERCEL\_GIT\_PROVIDER](#GATSBY_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
GATSBY_VERCEL_GIT_PROVIDER=github
```

### [GATSBY\_VERCEL\_GIT\_REPO\_SLUG](#GATSBY_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
GATSBY_VERCEL_GIT_REPO_SLUG=my-site
```

### [GATSBY\_VERCEL\_GIT\_REPO\_OWNER](#GATSBY_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
GATSBY_VERCEL_GIT_REPO_OWNER=acme
```

### [GATSBY\_VERCEL\_GIT\_REPO\_ID](#GATSBY_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
GATSBY_VERCEL_GIT_REPO_ID=117716146
```

### [GATSBY\_VERCEL\_GIT\_COMMIT\_REF](#GATSBY_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
GATSBY_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [GATSBY\_VERCEL\_GIT\_COMMIT\_SHA](#GATSBY_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
GATSBY_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [GATSBY\_VERCEL\_GIT\_COMMIT\_MESSAGE](#GATSBY_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
GATSBY_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [GATSBY\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
GATSBY_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [GATSBY\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
GATSBY_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [GATSBY\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#GATSBY_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
GATSBY_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [VITE\_VERCEL\_ENV](#VITE_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VITE_VERCEL_ENV=production
```

### [VITE\_VERCEL\_TARGET\_ENV](#VITE_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VITE_VERCEL_TARGET_ENV=production
```

### [VITE\_VERCEL\_URL](#VITE_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_URL=my-site.vercel.app
```

### [VITE\_VERCEL\_BRANCH\_URL](#VITE_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VITE\_VERCEL\_PROJECT\_PRODUCTION\_URL](#VITE_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VITE\_VERCEL\_GIT\_PROVIDER](#VITE_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_PROVIDER=github
```

### [VITE\_VERCEL\_GIT\_REPO\_SLUG](#VITE_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_SLUG=my-site
```

### [VITE\_VERCEL\_GIT\_REPO\_OWNER](#VITE_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_OWNER=acme
```

### [VITE\_VERCEL\_GIT\_REPO\_ID](#VITE_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_ID=117716146
```

### [VITE\_VERCEL\_GIT\_COMMIT\_REF](#VITE_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_SHA](#VITE_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VITE\_VERCEL\_GIT\_COMMIT\_MESSAGE](#VITE_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VITE\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#VITE_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VITE_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [VITE\_VERCEL\_ENV](#VITE_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VITE_VERCEL_ENV=production
```

### [VITE\_VERCEL\_TARGET\_ENV](#VITE_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VITE_VERCEL_TARGET_ENV=production
```

### [VITE\_VERCEL\_URL](#VITE_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_URL=my-site.vercel.app
```

### [VITE\_VERCEL\_BRANCH\_URL](#VITE_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VITE\_VERCEL\_PROJECT\_PRODUCTION\_URL](#VITE_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VITE\_VERCEL\_GIT\_PROVIDER](#VITE_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_PROVIDER=github
```

### [VITE\_VERCEL\_GIT\_REPO\_SLUG](#VITE_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_SLUG=my-site
```

### [VITE\_VERCEL\_GIT\_REPO\_OWNER](#VITE_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_OWNER=acme
```

### [VITE\_VERCEL\_GIT\_REPO\_ID](#VITE_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_ID=117716146
```

### [VITE\_VERCEL\_GIT\_COMMIT\_REF](#VITE_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_SHA](#VITE_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VITE\_VERCEL\_GIT\_COMMIT\_MESSAGE](#VITE_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VITE\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#VITE_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VITE_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [PUBLIC\_VERCEL\_ENV](#PUBLIC_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
PUBLIC_VERCEL_ENV=production
```

### [PUBLIC\_VERCEL\_TARGET\_ENV](#PUBLIC_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
PUBLIC_VERCEL_TARGET_ENV=production
```

### [PUBLIC\_VERCEL\_URL](#PUBLIC_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_URL=my-site.vercel.app
```

### [PUBLIC\_VERCEL\_BRANCH\_URL](#PUBLIC_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [PUBLIC\_VERCEL\_PROJECT\_PRODUCTION\_URL](#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [PUBLIC\_VERCEL\_GIT\_PROVIDER](#PUBLIC_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_PROVIDER=github
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_SLUG](#PUBLIC_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_SLUG=my-site
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_OWNER](#PUBLIC_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_OWNER=acme
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_ID](#PUBLIC_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_ID=117716146
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_REF](#PUBLIC_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_SHA](#PUBLIC_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_MESSAGE](#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [PUBLIC\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [VITE\_VERCEL\_ENV](#VITE_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VITE_VERCEL_ENV=production
```

### [VITE\_VERCEL\_TARGET\_ENV](#VITE_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VITE_VERCEL_TARGET_ENV=production
```

### [VITE\_VERCEL\_URL](#VITE_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_URL=my-site.vercel.app
```

### [VITE\_VERCEL\_BRANCH\_URL](#VITE_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VITE\_VERCEL\_PROJECT\_PRODUCTION\_URL](#VITE_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VITE\_VERCEL\_GIT\_PROVIDER](#VITE_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_PROVIDER=github
```

### [VITE\_VERCEL\_GIT\_REPO\_SLUG](#VITE_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_SLUG=my-site
```

### [VITE\_VERCEL\_GIT\_REPO\_OWNER](#VITE_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_OWNER=acme
```

### [VITE\_VERCEL\_GIT\_REPO\_ID](#VITE_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_ID=117716146
```

### [VITE\_VERCEL\_GIT\_COMMIT\_REF](#VITE_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_SHA](#VITE_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VITE\_VERCEL\_GIT\_COMMIT\_MESSAGE](#VITE_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VITE\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#VITE_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VITE_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [VUE\_APP\_VERCEL\_ENV](#VUE_APP_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VUE_APP_VERCEL_ENV=production
```

### [VUE\_APP\_VERCEL\_TARGET\_ENV](#VUE_APP_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VUE_APP_VERCEL_TARGET_ENV=production
```

### [VUE\_APP\_VERCEL\_URL](#VUE_APP_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VUE_APP_VERCEL_URL=my-site.vercel.app
```

### [VUE\_APP\_VERCEL\_BRANCH\_URL](#VUE_APP_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VUE_APP_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VUE\_APP\_VERCEL\_PROJECT\_PRODUCTION\_URL](#VUE_APP_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VUE_APP_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VUE\_APP\_VERCEL\_GIT\_PROVIDER](#VUE_APP_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
VUE_APP_VERCEL_GIT_PROVIDER=github
```

### [VUE\_APP\_VERCEL\_GIT\_REPO\_SLUG](#VUE_APP_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
VUE_APP_VERCEL_GIT_REPO_SLUG=my-site
```

### [VUE\_APP\_VERCEL\_GIT\_REPO\_OWNER](#VUE_APP_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
VUE_APP_VERCEL_GIT_REPO_OWNER=acme
```

### [VUE\_APP\_VERCEL\_GIT\_REPO\_ID](#VUE_APP_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
VUE_APP_VERCEL_GIT_REPO_ID=117716146
```

### [VUE\_APP\_VERCEL\_GIT\_COMMIT\_REF](#VUE_APP_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
VUE_APP_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VUE\_APP\_VERCEL\_GIT\_COMMIT\_SHA](#VUE_APP_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VUE_APP_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VUE\_APP\_VERCEL\_GIT\_COMMIT\_MESSAGE](#VUE_APP_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
VUE_APP_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VUE\_APP\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VUE\_APP\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
VUE_APP_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VUE\_APP\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#VUE_APP_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VUE_APP_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [REDWOOD\_ENV\_VERCEL\_ENV](#REDWOOD_ENV_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
REDWOOD_ENV_VERCEL_ENV=production
```

### [REDWOOD\_ENV\_VERCEL\_TARGET\_ENV](#REDWOOD_ENV_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
REDWOOD_ENV_VERCEL_TARGET_ENV=production
```

### [REDWOOD\_ENV\_VERCEL\_URL](#REDWOOD_ENV_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
REDWOOD_ENV_VERCEL_URL=my-site.vercel.app
```

### [REDWOOD\_ENV\_VERCEL\_BRANCH\_URL](#REDWOOD_ENV_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
REDWOOD_ENV_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [REDWOOD\_ENV\_VERCEL\_PROJECT\_PRODUCTION\_URL](#REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
REDWOOD_ENV_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_PROVIDER](#REDWOOD_ENV_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
REDWOOD_ENV_VERCEL_GIT_PROVIDER=github
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_REPO\_SLUG](#REDWOOD_ENV_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
REDWOOD_ENV_VERCEL_GIT_REPO_SLUG=my-site
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_REPO\_OWNER](#REDWOOD_ENV_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
REDWOOD_ENV_VERCEL_GIT_REPO_OWNER=acme
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_REPO\_ID](#REDWOOD_ENV_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
REDWOOD_ENV_VERCEL_GIT_REPO_ID=117716146
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_COMMIT\_REF](#REDWOOD_ENV_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
REDWOOD_ENV_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_COMMIT\_SHA](#REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
REDWOOD_ENV_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_COMMIT\_MESSAGE](#REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
REDWOOD_ENV_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
REDWOOD_ENV_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [REDWOOD\_ENV\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
REDWOOD_ENV_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [PUBLIC\_VERCEL\_ENV](#PUBLIC_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
PUBLIC_VERCEL_ENV=production
```

### [PUBLIC\_VERCEL\_TARGET\_ENV](#PUBLIC_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
PUBLIC_VERCEL_TARGET_ENV=production
```

### [PUBLIC\_VERCEL\_URL](#PUBLIC_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_URL=my-site.vercel.app
```

### [PUBLIC\_VERCEL\_BRANCH\_URL](#PUBLIC_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [PUBLIC\_VERCEL\_PROJECT\_PRODUCTION\_URL](#PUBLIC_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
PUBLIC_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [PUBLIC\_VERCEL\_GIT\_PROVIDER](#PUBLIC_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_PROVIDER=github
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_SLUG](#PUBLIC_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_SLUG=my-site
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_OWNER](#PUBLIC_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_OWNER=acme
```

### [PUBLIC\_VERCEL\_GIT\_REPO\_ID](#PUBLIC_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
PUBLIC_VERCEL_GIT_REPO_ID=117716146
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_REF](#PUBLIC_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_SHA](#PUBLIC_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_MESSAGE](#PUBLIC_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [PUBLIC\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
PUBLIC_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [PUBLIC\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#PUBLIC_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
PUBLIC_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [VITE\_VERCEL\_ENV](#VITE_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VITE_VERCEL_ENV=production
```

### [VITE\_VERCEL\_TARGET\_ENV](#VITE_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VITE_VERCEL_TARGET_ENV=production
```

### [VITE\_VERCEL\_URL](#VITE_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_URL=my-site.vercel.app
```

### [VITE\_VERCEL\_BRANCH\_URL](#VITE_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VITE\_VERCEL\_PROJECT\_PRODUCTION\_URL](#VITE_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VITE_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VITE\_VERCEL\_GIT\_PROVIDER](#VITE_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_PROVIDER=github
```

### [VITE\_VERCEL\_GIT\_REPO\_SLUG](#VITE_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_SLUG=my-site
```

### [VITE\_VERCEL\_GIT\_REPO\_OWNER](#VITE_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_OWNER=acme
```

### [VITE\_VERCEL\_GIT\_REPO\_ID](#VITE_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
VITE_VERCEL_GIT_REPO_ID=117716146
```

### [VITE\_VERCEL\_GIT\_COMMIT\_REF](#VITE_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_SHA](#VITE_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VITE\_VERCEL\_GIT\_COMMIT\_MESSAGE](#VITE_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
VITE_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VITE\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
VITE_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VITE\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#VITE_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VITE_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [SANITY\_STUDIO\_VERCEL\_ENV](#SANITY_STUDIO_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
SANITY_STUDIO_VERCEL_ENV=production
```

### [SANITY\_STUDIO\_VERCEL\_TARGET\_ENV](#SANITY_STUDIO_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
SANITY_STUDIO_VERCEL_TARGET_ENV=production
```

### [SANITY\_STUDIO\_VERCEL\_URL](#SANITY_STUDIO_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_URL=my-site.vercel.app
```

### [SANITY\_STUDIO\_VERCEL\_BRANCH\_URL](#SANITY_STUDIO_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [SANITY\_STUDIO\_VERCEL\_PROJECT\_PRODUCTION\_URL](#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_PROVIDER](#SANITY_STUDIO_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_PROVIDER=github
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_SLUG](#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_SLUG=my-site
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_OWNER](#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_OWNER=acme
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_ID](#SANITY_STUDIO_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_ID=117716146
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_REF](#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_SHA](#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_MESSAGE](#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID=23
```

### [SANITY\_STUDIO\_VERCEL\_ENV](#SANITY_STUDIO_VERCEL_ENV)

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
SANITY_STUDIO_VERCEL_ENV=production
```

### [SANITY\_STUDIO\_VERCEL\_TARGET\_ENV](#SANITY_STUDIO_VERCEL_TARGET_ENV)

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
SANITY_STUDIO_VERCEL_TARGET_ENV=production
```

### [SANITY\_STUDIO\_VERCEL\_URL](#SANITY_STUDIO_VERCEL_URL)

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_URL=my-site.vercel.app
```

### [SANITY\_STUDIO\_VERCEL\_BRANCH\_URL](#SANITY_STUDIO_VERCEL_BRANCH_URL)

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [SANITY\_STUDIO\_VERCEL\_PROJECT\_PRODUCTION\_URL](#SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL)

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
SANITY_STUDIO_VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_PROVIDER](#SANITY_STUDIO_VERCEL_GIT_PROVIDER)

The Git Provider the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_PROVIDER=github
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_SLUG](#SANITY_STUDIO_VERCEL_GIT_REPO_SLUG)

The origin repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_SLUG=my-site
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_OWNER](#SANITY_STUDIO_VERCEL_GIT_REPO_OWNER)

The account that owns the repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_OWNER=acme
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_REPO\_ID](#SANITY_STUDIO_VERCEL_GIT_REPO_ID)

The ID of the repository the deployment is triggered from.

.env

```
SANITY_STUDIO_VERCEL_GIT_REPO_ID=117716146
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_REF](#SANITY_STUDIO_VERCEL_GIT_COMMIT_REF)

The git branch of the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_SHA](#SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA)

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_MESSAGE](#SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE)

The message attached to the commit the deployment was triggered by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

The username attached to the author of the commit that the project was deployed by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME)

The name attached to the author of the commit that the project was deployed by.

.env

```
SANITY_STUDIO_VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [SANITY\_STUDIO\_VERCEL\_GIT\_PULL\_REQUEST\_ID](#SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID)

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
SANITY_STUDIO_VERCEL_GIT_PULL_REQUEST_ID=23
```

--------------------------------------------------------------------------------
title: "Managing environment variables"
description: "Learn how to create and manage environment variables for Vercel."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/managing-environment-variables"
--------------------------------------------------------------------------------

# Managing environment variables

Copy page

Ask AI about this page

Last updated September 15, 2025

Environment variables are key-value pairs configured outside your source code so that each value can change depending on the [Environment](/docs/deployments/environments).

Changes to environment variables are not applied to previous deployments, they only apply to new deployments. You must redeploy your project to update the value of any variables you change in the deployment.

## [Declare an Environment Variable](#declare-an-environment-variable)

To declare an Environment Variable for your deployment:

1.  From your [dashboard](/dashboard), select your project. If necessary, you can also set environment variables team-wide so that they will be available for all projects.
    
2.  Select the Settings tab.
    
3.  Go to the Environment Variables section of your Project Settings.
    
    ![The 'Add New' section of the Environment Variables page in the Project Settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-section-light.png&w=1920&q=75)![The 'Add New' section of the Environment Variables page in the Project Settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-section-dark.png&w=1920&q=75)
    
    The 'Add New' section of the Environment Variables page in the Project Settings.
    
4.  Enter the desired Name for your Environment Variable. For example, if you are using Node.js and you create an Environment Variable named `API_URL`, it will be available under `process.env.API_URL` in your code.
    
    Node.jsGoPythonRuby
    
    ```
    process.env.API_URL;
    ```
    
    ```
    os.Getenv("API_URL")
    ```
    
    ```
    os.environ.get('API_URL')
    ```
    
    ```
    ENV['API_URL']
    ```
    
5.  Then, enter the Value for your Environment Variable. The value is encrypted at rest so it is safe to add sensitive data like authentication tokens or private keys.
    
6.  Configure which [deployment environment(s)](/docs/deployments/environments) this variable should apply to.
    
7.  Click Save.
    
8.  To ensure that the new Environment Variable is applied to your deployment, you must [redeploy](/docs/deployments/managing-deployments#redeploy-a-project) your project.
    

## [Viewing, editing, or deleting an Environment Variable](#viewing-editing-or-deleting-an-environment-variable)

To find and view all environment variables.

1.  From your [dashboard](/dashboard), select your project. You can also view all team-wide environment variables through the Team Settings.
2.  Select the Settings tab.
3.  Go to the Environment Variables section of your Project Settings.
4.  Below the _Add New_ form is a list of all the environment variables for the Project.
5.  You can search for an existing Environment Variable by name using the search input and/or filter by [Environment](/docs/deployments/environments).
6.  To edit or delete the Environment Variable, click the three dots to the right of the Environment Variable name.
    
    ![An example of an Environment Variable with the search and filter inputs above.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fvariable-example-light.png&w=1920&q=75)![An example of an Environment Variable with the search and filter inputs above.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fvariable-example-dark.png&w=1920&q=75)
    
    An example of an Environment Variable with the search and filter inputs above.

--------------------------------------------------------------------------------
title: "Reserved environment variables"
description: "Reserved environment variables are reserved by Vercel Vercel Function runtimes."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/reserved-environment-variables"
--------------------------------------------------------------------------------

# Reserved environment variables

Copy page

Ask AI about this page

Last updated June 25, 2025

The following [environment variable](/docs/environment-variables) names are [reserved](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime) and therefore unavailable for use:

*   `AWS_SECRET_KEY`
*   `AWS_EXECUTION_ENV`
*   `AWS_LAMBDA_LOG_GROUP_NAME`
*   `AWS_LAMBDA_LOG_STREAM_NAME`
*   `AWS_LAMBDA_FUNCTION_NAME`
*   `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
*   `AWS_LAMBDA_FUNCTION_VERSION`
*   `NOW_REGION`
*   `TZ`
*   `LAMBDA_TASK_ROOT`
*   `LAMBDA_RUNTIME_DIR`

## [Allowed environment variables](#allowed-environment-variables)

The following [environment variable](/docs/environment-variables) names are [allowed](https://vercel.com/guides/how-can-i-use-aws-sdk-environment-variables-on-vercel) by Vercel Vercel Function runtimes:

*   `AWS_ACCESS_KEY_ID`
*   `AWS_SECRET_ACCESS_KEY`
*   `AWS_SESSION_TOKEN`
*   `AWS_REGION`
*   `AWS_DEFAULT_REGION`

--------------------------------------------------------------------------------
title: "Sensitive environment variables"
description: "Environment variables that cannot be decrypted once created."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/sensitive-environment-variables"
--------------------------------------------------------------------------------

# Sensitive environment variables

Copy page

Ask AI about this page

Last updated October 7, 2025

Sensitive environment variables are [environment variables](/docs/environment-variables) whose values are non-readable once created. They help protect sensitive information stored in environment variables, such as API keys.

To mark an existing environment variable as sensitive, remove and re-add it with the Sensitive option enabled. Once you mark it as sensitive, Vercel stores the variable in an unreadable format. This is only possible for environment variables in the [production](/docs/deployments/environments#production-environment) and [preview](/docs/deployments/environments#preview-environment-pre-production) environments.

Both [project environment variables](/docs/environment-variables) and [shared environment variables](/docs/environment-variables/shared-environment-variables) can be marked as sensitive.

## [Creating sensitive environment variables](#creating-sensitive-environment-variables)

You can only create sensitive environment variables in the preview and production environments.

DashboardcURLSDK

Sensitive environment variables can be created at the project or team level:

1.  Go to the Vercel [dashboard](/dashboard) and select your team from the scope selector. Click on the Settings tab and then select Environment Variables from the left navigation. To create sensitive environment variables at the project-level, select the project from your [dashboard](/dashboard) and then and click the Settings tab.
2.  At the top of the form, toggle the Sensitive switch to Enabled. If the Development environment is selected, you will be unable to enable the switch.
3.  Fill in the details to create a new environment variable.
4.  In the environment variable table, sensitive environment variables are marked with a "Sensitive" tag:
    
    ![Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Flisted-sev.png&w=3840&q=75)![Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Flisted-sev-dark.png&w=3840&q=75)
    
    Sensitive environment variables labeled with a 'Sensitive' tag on the dashboard.
    

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

cURL

```
curl --request POST \
  --url https://api.vercel.com/v10/projects/<project-id-or-name>/env \
  --header "Authorization: Bearer $VERCEL_TOKEN" \
  --header "Content-Type: application/json" \
  --data '[
    {
      "key": "<env-key-1>",
      "value": "<env-value-1>",
      "type": "sensitive",
      "target": ["<target-environment>"],
      "gitBranch": "<git-branch>",
      "comment": "<comment>",
      "customEnvironmentIds": ["<custom-env-id>"]
    }
  ]'
```

To create an Authorization Bearer token, see the [access token](/docs/rest-api/reference/welcome#creating-an-access-token) section of the API documentation.

createProjectEnv

```
import { Vercel } from '@vercel/sdk';
 
const vercel = new Vercel({
  bearerToken: '<YOUR_BEARER_TOKEN_HERE>',
});
 
async function run() {
  const result = await vercel.projects.createProjectEnv({
    idOrName: '<project-id-or-name>',
    requestBody: {
      key: '<env-key-1>',
      value: '<env-value-1>',
      type: 'sensitive',
      target: ['<target-environment>'],
      gitBranch: '<git-branch>',
      comment: '<comment>',
      customEnvironmentIds: ['<custom-env-id>'],
    },
  });
 
  // Handle the result
  console.log(result);
}
 
run();
```

## [Edit sensitive environment variables](#edit-sensitive-environment-variables)

You can edit the value and [environment](/docs/environment-variables#environments) for a sensitive environment variable. You cannot edit the key of a sensitive environment variable.

1.  From your dashboard, go to the team or project's Settings tab and select Environment Variables from the left navigation. Find your environment variable in the list.
2.  Click Edit from the three-dot menu in the environment variables list
3.  Provide a new value for the sensitive environment variable. The current value is hidden.
4.  Select the environment(s) for the sensitive environment variable.
5.  After making the change, click the Save button.

## [Environment variables policy](#environment-variables-policy)

Users with the [owner](/docs/rbac/access-roles#owner-role) role can set a team-wide environment variable policy for creating environment variables. Once enabled, all newly created environment variables in the [Production](/docs/deployments/environments#production-environment) and/or [Preview](/docs/deployments/environments#preview-environment-pre-production) environments will be sensitive environment variables.

1.  From the dashboard, ensure your team is selected in the scope selector and select the Settings tab.
2.  From the left navigation, click Security & Privacy.
3.  From the Environment Variable Policies section, toggle the Enforce Sensitive Environment Variables switch to Enabled:
    
    ![Set environment variable policy from your team's Security settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-policies-2.png&w=1920&q=75)![Set environment variable policy from your team's Security settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fenvironment-variables%2Fenv-var-policies-dark-2.png&w=1920&q=75)
    
    Set environment variable policy from your team's Security settings.

--------------------------------------------------------------------------------
title: "Shared environment variables"
description: "Learn how to use Shared environment variables, which are environment variables that you define at the Team level and can link to multiple projects."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/shared-environment-variables"
--------------------------------------------------------------------------------

# Shared environment variables

Copy page

Ask AI about this page

Last updated September 24, 2025

Shared Environment Variables are [environment variables](/docs/environment-variables) that you define at the team-level and can link to multiple projects. When a Shared Environment Variable is updated, the change is applied to all linked projects.

When a project-level and a Shared Environment Variable share the same key and environment, the project-level environment variable always overrides the Shared Environment Variable.

## [Creating shared environment variables](#creating-shared-environment-variables)

Shared Environment Variables are created on the [Team Settings page](/docs/accounts/create-a-team). To create a new Shared Environment Variable, follow these steps:

1.  Go to the Vercel [dashboard](/dashboard) and select your team from the scope selector. Click on the Settings tab and then select Environment Variables from the left navigation.
2.  Populate the form with your environment variable details or paste or import an `.env` file:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-form.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-form-dark.png&w=3840&q=75)
    
    *   Key: Fill in the key of the environment variable. - Value: Fill in the value of the environment variable. - Environment: Select the [Environments](/docs/environment-variables#environments) where you want to include it. The environment(s) chosen for the Shared Environment Variable is used when linked to a project. - Link to Projects: Select one or more [projects](/docs/projects/overview) in succession to link the new Shared Environment Variable by using the searchable drop-down. You can keep this empty and [link to projects](#linking-to-projects) later.
3.  Click Save to save your new Shared Environment Variable.

## [Linking to projects](#linking-to-projects)

A Shared Environment Variable is activated once it is linked to at least one project.

You can link an existing Shared Environment Variable to a project either at the project-level or the team-level.

### [Project level linking](#project-level-linking)

For project-level linking:

1.  From your [dashboard](/dashboard), select the Project you would like to link the Shared Environment Variable to and click the Settings tab.
2.  Select Environment Variables from the list, and click on the Link Shared Environment Variables tab.
3.  Select one or more Shared Environment Variables using the search box:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-project-search.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-project-search-dark.png&w=3840&q=75)
    
4.  Click the Link button

### [Team level linking](#team-level-linking)

1.  From your [dashboard](/dashboard), click the Settings tab and go to Environment Variables.
    
2.  Scroll down below the Shared Environment Variable creation form.
    
3.  Find the variable you would like to link. You can use the Search box, the Environments drop-down filter and sort by last updated date, name or type to more easily find the variable.
    
4.  Open the context menu for the specific Shared Environment Variable using the vertical ellipsis icon on the right hand side of the row, and click Edit:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-team-link.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-team-link-dark.png&w=3840&q=75)
    
5.  From the Environment Variable form, you can link additional projects using the Link to Projects field
    
6.  Click Save when you are done
    

## [Removing shared environment variables](#removing-shared-environment-variables)

There are two ways to remove a Shared Environment Variable from a project:

*   Unlinking: It is disassociated from the selected project(s) but continues to exist at the level of the team
*   Deleting: It is permanently removed from the team and disconnected from all projects it was previously linked to.

### [Unlinking at the project level](#unlinking-at-the-project-level)

1.  From your [dashboard](/dashboard), select the project you would like to unlink the Shared Environment Variable from and click the Settings tab.
2.  Select Environment Variables, and scroll down to the Shared Environment Variables section.
3.  Open the context menu for the specific shared environment variable you would like to unlink using the vertical ellipsis icon on the right hand side.
4.  Click Unlink from this Project:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-project-unlink.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-project-unlink-dark.png&w=3840&q=75)
    

### [Unlinking at the team level](#unlinking-at-the-team-level)

1.  From your [dashboard](/dashboard), click the Settings tab and go to Environment Variables.
2.  Scroll down below the Environment Variable creation form.
3.  Find the variable you would like to link. You can use the Search box, the Environments drop-down filter and sort by last updated date, name or type to more easily find the variable.
4.  Open the context menu for the specific shared environment variable using the vertical ellipsis icon on the right hand side of the row, and click Edit:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-team-link.png&w=3840&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fprojects%2Fshared-environment-variables%2Fshared-envs-team-link-dark.png&w=3840&q=75)
    
5.  From the Environment Variable form, click the minus icon to unlink existing projects
6.  When you are done, click the Save button.

### [Deleting environment variables from a team](#deleting-environment-variables-from-a-team)

1.  From your [dashboard](/dashboard), click the Settings tab and go to Environment Variables.
2.  Scroll down below the Environment Variable creation form
3.  Use the context menu on the specific Shared Environment Variable by clicking the vertical ellipsis icon on the right side of the row
4.  Click the Delete button

This action will remove the Shared Environment Variable from the Vercel Team. It will also unlink the Environment Variable from ALL previously linked projects.

## [Known limitations](#known-limitations)

[Branch-specific variables](/docs/environment-variables#preview-environment-variables) are not currently supported with Shared Environment Variables

--------------------------------------------------------------------------------
title: "System environment variables"
description: "System environment variables are automatically populated by Vercel, such as the URL of the deployment or the name of the Git branch deployed."
last_updated: "null"
source: "https://vercel.com/docs/environment-variables/system-environment-variables"
--------------------------------------------------------------------------------

# System environment variables

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel provides a set of environment variables that are automatically populated by the system, such as the URL of the deployment or the name of the Git branch deployed.

## [Automatically expose system environment variables](#automatically-expose-system-environment-variables)

To expose these environment variables to your deployments:

1.  Navigate to your project on your [dashboard](/dashboard).
2.  Go to the Settings tab and click on the Environment Variables section.
3.  Select the Automatically expose System Environment Variables checkbox.

If you disable this setting, no deployment ID will be made available for supported frameworks (like Next.js) to use, which means [Skew Protection](/docs/skew-protection) will also be disabled.

## [System environment variables](#system-environment-variables)

If you are using a framework for your project, Vercel provides the following prefixed environment variables:

When you choose to automatically expose system environment variables, some React warnings, such as those in a `create-react-app` will display as build errors. For more information on this error, see [How do I resolve a `process.env.CI = true` error?](/guides/how-do-i-resolve-a-process-env-ci-true-error)

### [VERCEL](#VERCEL)

**Available at:**Both build and runtime

An indicator to show that system environment variables have been exposed to your project's Deployments.

.env

```
VERCEL=1
```

### [CI](#CI)

**Available at:**Build time

An indicator that the code is running in a [Continuous Integration](https://en.wikipedia.org/wiki/Continuous_integration) environment.

.env

```
CI=1
```

### [VERCEL\_ENV](#VERCEL_ENV)

**Available at:**Both build and runtime

The [environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, or `development`.

.env

```
VERCEL_ENV=production
```

### [VERCEL\_TARGET\_ENV](#VERCEL_TARGET_ENV)

**Available at:**Both build and runtime

The [system or custom environment](/docs/environment-variables#environments) that the app is deployed and running on. The value can be either `production`, `preview`, `development`, or the name of a [custom environment](/docs/deployments/environments#custom-environments).

.env

```
VERCEL_TARGET_ENV=production
```

### [VERCEL\_URL](#VERCEL_URL)

**Available at:**Both build and runtime

The domain name of the [generated deployment URL](/docs/deployments/generated-urls). Example: `*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VERCEL_URL=my-site.vercel.app
```

### [VERCEL\_BRANCH\_URL](#VERCEL_BRANCH_URL)

**Available at:**Both build and runtime

The domain name of the [generated Git branch URL](/docs/deployments/generated-urls#url-with-git-branch). Example: `*-git-*.vercel.app`. The value **does not** include the protocol scheme `https://`.

.env

```
VERCEL_BRANCH_URL=my-site-git-improve-about-page.vercel.app
```

### [VERCEL\_PROJECT\_PRODUCTION\_URL](#VERCEL_PROJECT_PRODUCTION_URL)

**Available at:**Both build and runtime

A production domain name of the project. We select the shortest production custom domain, or vercel.app domain if no custom domain is available. Note, that this is always set, even in preview deployments. This is useful to reliably generate links that point to production such as OG-image URLs. The value **does not** include the protocol scheme `https://`.

.env

```
VERCEL_PROJECT_PRODUCTION_URL=my-site.com
```

### [VERCEL\_REGION](#VERCEL_REGION)

**Available at:**Runtime

The ID of the [Region](/docs/regions) where the app is running.

.env

```
VERCEL_REGION=cdg1
```

### [VERCEL\_DEPLOYMENT\_ID](#VERCEL_DEPLOYMENT_ID)

**Available at:**Both build and runtime

The unique identifier for the deployment, which can be used to implement [Skew Protection](/docs/skew-protection).

.env

```
VERCEL_DEPLOYMENT_ID=dpl_7Gw5ZMBpQA8h9GF832KGp7nwbuh3
```

### [VERCEL\_PROJECT\_ID](#VERCEL_PROJECT_ID)

**Available at:**Both build and runtime

The unique identifier for the project.

.env

```
VERCEL_PROJECT_ID=prj_Rej9WaMNRbffVm34MfDqa4daCEvZzzE
```

### [VERCEL\_SKEW\_PROTECTION\_ENABLED](#VERCEL_SKEW_PROTECTION_ENABLED)

**Available at:**Both build and runtime

When [Skew Protection](/docs/skew-protection) is enabled in Project Settings, this value is set to `1`.

.env

```
VERCEL_SKEW_PROTECTION_ENABLED=1
```

### [VERCEL\_AUTOMATION\_BYPASS\_SECRET](#VERCEL_AUTOMATION_BYPASS_SECRET)

**Available at:**Both build and runtime

The [Protection Bypass for Automation](/docs/security/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation) value, if the secret has been generated in the project's [Deployment Protection](/docs/security/deployment-protection) settings.

.env

```
VERCEL_AUTOMATION_BYPASS_SECRET=secret
```

### [VERCEL\_OIDC\_TOKEN](#VERCEL_OIDC_TOKEN)

**Available at:**Build time

When Secure Backend Access with [OpenID Connect (OIDC) Federation](/docs/oidc) is enabled in Project Settings, this value is set to a Vercel-issued OIDC token. At runtime, the token is set to the`x-vercel-oidc-token` header on your functions' `Request` object. In local development, you can download the token using the CLI command`vercel env pull`.

.env

```
VERCEL_OIDC_TOKEN=secret
```

### [VERCEL\_GIT\_PROVIDER](#VERCEL_GIT_PROVIDER)

**Available at:**Both build and runtime

The Git Provider the deployment is triggered from.

.env

```
VERCEL_GIT_PROVIDER=github
```

### [VERCEL\_GIT\_REPO\_SLUG](#VERCEL_GIT_REPO_SLUG)

**Available at:**Both build and runtime

The origin repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_SLUG=my-site
```

### [VERCEL\_GIT\_REPO\_OWNER](#VERCEL_GIT_REPO_OWNER)

**Available at:**Both build and runtime

The account that owns the repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_OWNER=acme
```

### [VERCEL\_GIT\_REPO\_ID](#VERCEL_GIT_REPO_ID)

**Available at:**Both build and runtime

The ID of the repository the deployment is triggered from.

.env

```
VERCEL_GIT_REPO_ID=117716146
```

### [VERCEL\_GIT\_COMMIT\_REF](#VERCEL_GIT_COMMIT_REF)

**Available at:**Both build and runtime

The git branch of the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_REF=improve-about-page
```

### [VERCEL\_GIT\_COMMIT\_SHA](#VERCEL_GIT_COMMIT_SHA)

**Available at:**Both build and runtime

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_SHA=fa1eade47b73733d6312d5abfad33ce9e4068081
```

### [VERCEL\_GIT\_COMMIT\_MESSAGE](#VERCEL_GIT_COMMIT_MESSAGE)

**Available at:**Both build and runtime

The message attached to the commit the deployment was triggered by.

.env

```
VERCEL_GIT_COMMIT_MESSAGE=Update about page
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_LOGIN](#VERCEL_GIT_COMMIT_AUTHOR_LOGIN)

**Available at:**Both build and runtime

The username attached to the author of the commit that the project was deployed by.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_LOGIN=johndoe
```

### [VERCEL\_GIT\_COMMIT\_AUTHOR\_NAME](#VERCEL_GIT_COMMIT_AUTHOR_NAME)

**Available at:**Both build and runtime

The name attached to the author of the commit that the project was deployed by.

.env

```
VERCEL_GIT_COMMIT_AUTHOR_NAME=John Doe
```

### [VERCEL\_GIT\_PREVIOUS\_SHA](#VERCEL_GIT_PREVIOUS_SHA)

**Available at:**Build time

The git [SHA](https://help.github.com/articles/github-glossary/#commit) of the last successful deployment for the project and branch.

.env

```
VERCEL_GIT_PREVIOUS_SHA=fa1eade47b73733d6312d5abfad33ce9e4068080
```

### [VERCEL\_GIT\_PULL\_REQUEST\_ID](#VERCEL_GIT_PULL_REQUEST_ID)

**Available at:**Both build and runtime

The pull request id the deployment was triggered by. If a deployment is created on a branch before a pull request is made, this value will be an empty string.

.env

```
VERCEL_GIT_PULL_REQUEST_ID=23
```

--------------------------------------------------------------------------------
title: "Error Codes"
description: "Use this guide to find specific solutions and insights for common Vercel errors."
last_updated: "null"
source: "https://vercel.com/docs/errors"
--------------------------------------------------------------------------------

# Error Codes

Copy page

Ask AI about this page

Last updated March 12, 2025

When developing your application with Vercel, you may encounter a variety of errors. They can reflect issues that happen with external providers such as domain services or internal problems at the level of your application's deployment or your usage of platform features.

For general error handling guidance, that covers dashboard related errors, see [General Errors](/docs/errors/error-list).

## [Application errors](#application-errors)

*   [
    
    ## BODY\_NOT\_A\_STRING\_FROM\_FUNCTION
    
    Function
    
    502
    
    
    
    ](/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION)
*   [
    
    ## DEPLOYMENT\_BLOCKED
    
    Deployment
    
    403
    
    
    
    ](/docs/errors/DEPLOYMENT_BLOCKED)
*   [
    
    ## DEPLOYMENT\_DELETED
    
    Deployment
    
    410
    
    
    
    ](/docs/errors/DEPLOYMENT_DELETED)
*   [
    
    ## DEPLOYMENT\_DISABLED
    
    Deployment
    
    402
    
    
    
    ](/docs/errors/DEPLOYMENT_DISABLED)
*   [
    
    ## DEPLOYMENT\_NOT\_FOUND
    
    Deployment
    
    404
    
    
    
    ](/docs/errors/DEPLOYMENT_NOT_FOUND)
*   [
    
    ## DEPLOYMENT\_NOT\_READY\_REDIRECTING
    
    Deployment
    
    303
    
    
    
    ](/docs/errors/DEPLOYMENT_NOT_READY_REDIRECTING)
*   [
    
    ## DEPLOYMENT\_PAUSED
    
    Deployment
    
    503
    
    
    
    ](/docs/errors/DEPLOYMENT_PAUSED)
*   [
    
    ## DNS\_HOSTNAME\_EMPTY
    
    DNS
    
    502
    
    
    
    ](/docs/errors/DNS_HOSTNAME_EMPTY)
*   [
    
    ## DNS\_HOSTNAME\_NOT\_FOUND
    
    DNS
    
    502
    
    
    
    ](/docs/errors/DNS_HOSTNAME_NOT_FOUND)
*   [
    
    ## DNS\_HOSTNAME\_RESOLVE\_FAILED
    
    DNS
    
    502
    
    
    
    ](/docs/errors/DNS_HOSTNAME_RESOLVE_FAILED)
*   [
    
    ## DNS\_HOSTNAME\_RESOLVED\_PRIVATE
    
    DNS
    
    404
    
    
    
    ](/docs/errors/DNS_HOSTNAME_RESOLVED_PRIVATE)
*   [
    
    ## DNS\_HOSTNAME\_SERVER\_ERROR
    
    DNS
    
    502
    
    
    
    ](/docs/errors/DNS_HOSTNAME_SERVER_ERROR)
*   [
    
    ## EDGE\_FUNCTION\_INVOCATION\_FAILED
    
    Function
    
    500
    
    
    
    ](/docs/errors/EDGE_FUNCTION_INVOCATION_FAILED)
*   [
    
    ## EDGE\_FUNCTION\_INVOCATION\_TIMEOUT
    
    Function
    
    504
    
    
    
    ](/docs/errors/EDGE_FUNCTION_INVOCATION_TIMEOUT)
*   [
    
    ## FALLBACK\_BODY\_TOO\_LARGE
    
    Cache
    
    502
    
    
    
    ](/docs/errors/FALLBACK_BODY_TOO_LARGE)
*   [
    
    ## FUNCTION\_INVOCATION\_FAILED
    
    Function
    
    500
    
    
    
    ](/docs/errors/FUNCTION_INVOCATION_FAILED)
*   [
    
    ## FUNCTION\_INVOCATION\_TIMEOUT
    
    Function
    
    504
    
    
    
    ](/docs/errors/FUNCTION_INVOCATION_TIMEOUT)
*   [
    
    ## FUNCTION\_PAYLOAD\_TOO\_LARGE
    
    Function
    
    413
    
    
    
    ](/docs/errors/FUNCTION_PAYLOAD_TOO_LARGE)
*   [
    
    ## FUNCTION\_RESPONSE\_PAYLOAD\_TOO\_LARGE
    
    Function
    
    500
    
    
    
    ](/docs/errors/FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE)
*   [
    
    ## FUNCTION\_THROTTLED
    
    Function
    
    503
    
    
    
    ](/docs/errors/FUNCTION_THROTTLED)
*   [
    
    ## INFINITE\_LOOP\_DETECTED
    
    Runtime
    
    508
    
    
    
    ](/docs/errors/INFINITE_LOOP_DETECTED)
*   [
    
    ## INVALID\_IMAGE\_OPTIMIZE\_REQUEST
    
    Image
    
    400
    
    
    
    ](/docs/errors/INVALID_IMAGE_OPTIMIZE_REQUEST)
*   [
    
    ## INVALID\_REQUEST\_METHOD
    
    Request
    
    405
    
    
    
    ](/docs/errors/INVALID_REQUEST_METHOD)
*   [
    
    ## MALFORMED\_REQUEST\_HEADER
    
    Request
    
    400
    
    
    
    ](/docs/errors/MALFORMED_REQUEST_HEADER)
*   [
    
    ## MICROFRONTENDS\_MIDDLEWARE\_ERROR
    
    Function
    
    500
    
    
    
    ](/docs/errors/MICROFRONTENDS_MIDDLEWARE_ERROR)
*   [
    
    ## MICROFRONTENDS\_MISSING\_FALLBACK\_ERROR
    
    Function
    
    400
    
    
    
    ](/docs/errors/MICROFRONTENDS_MISSING_FALLBACK_ERROR)
*   [
    
    ## MIDDLEWARE\_INVOCATION\_FAILED
    
    Function
    
    500
    
    
    
    ](/docs/errors/MIDDLEWARE_INVOCATION_FAILED)
*   [
    
    ## MIDDLEWARE\_INVOCATION\_TIMEOUT
    
    Function
    
    504
    
    
    
    ](/docs/errors/MIDDLEWARE_INVOCATION_TIMEOUT)
*   [
    
    ## MIDDLEWARE\_RUNTIME\_DEPRECATED
    
    Runtime
    
    503
    
    
    
    ](/docs/errors/MIDDLEWARE_RUNTIME_DEPRECATED)
*   [
    
    ## NO\_RESPONSE\_FROM\_FUNCTION
    
    Function
    
    502
    
    
    
    ](/docs/errors/NO_RESPONSE_FROM_FUNCTION)
*   [
    
    ## NOT\_FOUND
    
    Deployment
    
    404
    
    
    
    ](/docs/errors/NOT_FOUND)
*   [
    
    ## OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_FAILED
    
    Image
    
    502
    
    
    
    ](/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_FAILED)
*   [
    
    ## OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_INVALID
    
    Image
    
    502
    
    
    
    ](/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_INVALID)
*   [
    
    ## OPTIMIZED\_EXTERNAL\_IMAGE\_REQUEST\_UNAUTHORIZED
    
    Image
    
    502
    
    
    
    ](/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_REQUEST_UNAUTHORIZED)
*   [
    
    ## OPTIMIZED\_EXTERNAL\_IMAGE\_TOO\_MANY\_REDIRECTS
    
    Image
    
    502
    
    
    
    ](/docs/errors/OPTIMIZED_EXTERNAL_IMAGE_TOO_MANY_REDIRECTS)
*   [
    
    ## RANGE\_END\_NOT\_VALID
    
    Request
    
    416
    
    
    
    ](/docs/errors/RANGE_END_NOT_VALID)
*   [
    
    ## RANGE\_GROUP\_NOT\_VALID
    
    Request
    
    416
    
    
    
    ](/docs/errors/RANGE_GROUP_NOT_VALID)
*   [
    
    ## RANGE\_MISSING\_UNIT
    
    Request
    
    416
    
    
    
    ](/docs/errors/RANGE_MISSING_UNIT)
*   [
    
    ## RANGE\_START\_NOT\_VALID
    
    Request
    
    416
    
    
    
    ](/docs/errors/RANGE_START_NOT_VALID)
*   [
    
    ## RANGE\_UNIT\_NOT\_SUPPORTED
    
    Request
    
    416
    
    
    
    ](/docs/errors/RANGE_UNIT_NOT_SUPPORTED)
*   [
    
    ## REQUEST\_HEADER\_TOO\_LARGE
    
    Request
    
    431
    
    
    
    ](/docs/errors/REQUEST_HEADER_TOO_LARGE)
*   [
    
    ## RESOURCE\_NOT\_FOUND
    
    Request
    
    404
    
    
    
    ](/docs/errors/RESOURCE_NOT_FOUND)
*   [
    
    ## ROUTER\_CANNOT\_MATCH
    
    Routing
    
    502
    
    
    
    ](/docs/errors/ROUTER_CANNOT_MATCH)
*   [
    
    ## ROUTER\_EXTERNAL\_TARGET\_CONNECTION\_ERROR
    
    Routing
    
    502
    
    
    
    ](/docs/errors/ROUTER_EXTERNAL_TARGET_CONNECTION_ERROR)
*   [
    
    ## ROUTER\_EXTERNAL\_TARGET\_ERROR
    
    Routing
    
    502
    
    
    
    ](/docs/errors/ROUTER_EXTERNAL_TARGET_ERROR)
*   [
    
    ## ROUTER\_EXTERNAL\_TARGET\_HANDSHAKE\_ERROR
    
    Routing
    
    502
    
    
    
    ](/docs/errors/ROUTER_EXTERNAL_TARGET_HANDSHAKE_ERROR)
*   [
    
    ## ROUTER\_TOO\_MANY\_HAS\_SELECTIONS
    
    Routing
    
    502
    
    
    
    ](/docs/errors/ROUTER_TOO_MANY_HAS_SELECTIONS)
*   [
    
    ## SANDBOX\_NOT\_FOUND
    
    Sandbox
    
    404
    
    
    
    ](/docs/errors/SANDBOX_NOT_FOUND)
*   [
    
    ## SANDBOX\_NOT\_LISTENING
    
    Sandbox
    
    502
    
    
    
    ](/docs/errors/SANDBOX_NOT_LISTENING)
*   [
    
    ## SANDBOX\_STOPPED
    
    Sandbox
    
    410
    
    
    
    ](/docs/errors/SANDBOX_STOPPED)
*   [
    
    ## TOO\_MANY\_FILESYSTEM\_CHECKS
    
    Routing
    
    502
    
    
    
    ](/docs/errors/TOO_MANY_FILESYSTEM_CHECKS)
*   [
    
    ## TOO\_MANY\_FORKS
    
    Routing
    
    502
    
    
    
    ](/docs/errors/TOO_MANY_FORKS)
*   [
    
    ## TOO\_MANY\_RANGES
    
    Request
    
    416
    
    
    
    ](/docs/errors/TOO_MANY_RANGES)
*   [
    
    ## URL\_TOO\_LONG
    
    Request
    
    414
    
    
    
    ](/docs/errors/URL_TOO_LONG)

## [Platform errors](#platform-errors)

The following errors are related to the Vercel platform. If you encounter one of these errors, contact [Vercel support](/help).

*   [
    
    ## FUNCTION\_THROTTLED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/FUNCTION_THROTTLED)
*   [
    
    ## INTERNAL\_CACHE\_ERROR
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_CACHE_ERROR)
*   [
    
    ## INTERNAL\_CACHE\_KEY\_TOO\_LONG
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_CACHE_KEY_TOO_LONG)
*   [
    
    ## INTERNAL\_CACHE\_LOCK\_FULL
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_CACHE_LOCK_FULL)
*   [
    
    ## INTERNAL\_CACHE\_LOCK\_TIMEOUT
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_CACHE_LOCK_TIMEOUT)
*   [
    
    ## INTERNAL\_DEPLOYMENT\_FETCH\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_DEPLOYMENT_FETCH_FAILED)
*   [
    
    ## INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_EDGE_FUNCTION_INVOCATION_FAILED)
*   [
    
    ## INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_TIMEOUT
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_EDGE_FUNCTION_INVOCATION_TIMEOUT)
*   [
    
    ## INTERNAL\_FUNCTION\_INVOCATION\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_FUNCTION_INVOCATION_FAILED)
*   [
    
    ## INTERNAL\_FUNCTION\_INVOCATION\_TIMEOUT
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_FUNCTION_INVOCATION_TIMEOUT)
*   [
    
    ## INTERNAL\_FUNCTION\_NOT\_FOUND
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_FUNCTION_NOT_FOUND)
*   [
    
    ## INTERNAL\_FUNCTION\_NOT\_READY
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_FUNCTION_NOT_READY)
*   ## INTERNAL\_FUNCTION\_SERVICE\_UNAVAILABLE
    
    Internal
    
    500
    
*   [
    
    ## INTERNAL\_MICROFRONTENDS\_BUILD\_ERROR
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_MICROFRONTENDS_BUILD_ERROR)
*   [
    
    ## INTERNAL\_MICROFRONTENDS\_INVALID\_CONFIGURATION\_ERROR
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_MICROFRONTENDS_INVALID_CONFIGURATION_ERROR)
*   [
    
    ## INTERNAL\_MICROFRONTENDS\_UNEXPECTED\_ERROR
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_MICROFRONTENDS_UNEXPECTED_ERROR)
*   [
    
    ## INTERNAL\_MISSING\_RESPONSE\_FROM\_CACHE
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_MISSING_RESPONSE_FROM_CACHE)
*   [
    
    ## INTERNAL\_OPTIMIZED\_IMAGE\_REQUEST\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_OPTIMIZED_IMAGE_REQUEST_FAILED)
*   [
    
    ## INTERNAL\_ROUTER\_CANNOT\_PARSE\_PATH
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_ROUTER_CANNOT_PARSE_PATH)
*   [
    
    ## INTERNAL\_STATIC\_REQUEST\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_STATIC_REQUEST_FAILED)
*   [
    
    ## INTERNAL\_UNARCHIVE\_FAILED
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_UNARCHIVE_FAILED)
*   [
    
    ## INTERNAL\_UNEXPECTED\_ERROR
    
    Internal
    
    500
    
    
    
    ](/docs/errors/INTERNAL_UNEXPECTED_ERROR)

--------------------------------------------------------------------------------
title: "BODY_NOT_A_STRING_FROM_FUNCTION"
description: "The function returned a non-string body. This is a function error."
last_updated: "null"
source: "https://vercel.com/docs/errors/BODY_NOT_A_STRING_FROM_FUNCTION"
--------------------------------------------------------------------------------

# BODY\_NOT\_A\_STRING\_FROM\_FUNCTION

Copy page

Ask AI about this page

Last updated October 6, 2025

The `BODY_NOT_A_STRING_FROM_FUNCTION` error occurs when a function returns a body that is not a string. It's essential that functions return a string body to ensure that they can be correctly processed and executed.

502

BODY\_NOT\_A\_STRING\_FROM\_FUNCTION:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/BODY\_NOT\_A\_STRING\_FROM\_FUNCTION to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FBODY_NOT_A_STRING_FROM_FUNCTION+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check function return type: Ensure that the function is structured to return a string. If the function is returning a different data type, modify the function to return a string, using `JSON.stringify()` if necessary
2.  Review function code: Inspect the function code for any logic that might cause a non-string value to be returned
3.  Check data types: If the function is processing input data or retrieving data from external sources, ensure that the data is being correctly converted to a string before being returned
4.  Review function logs: Check the [function logs](/docs/runtime-logs#type) for any errors or warnings that might indicate why a non-string value is being returned

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_BLOCKED"
description: "The deployment was blocked due to certain conditions. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_BLOCKED"
--------------------------------------------------------------------------------

# DEPLOYMENT\_BLOCKED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_BLOCKED` error occurs when a deployment is blocked due to certain conditions that prevent it from proceeding. This could happen due to various reasons such as configuration errors, account limitations, or policy violations.

403

DEPLOYMENT\_BLOCKED:

Forbidden

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_BLOCKED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_BLOCKED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check configuration: Ensure that your deployment configuration is correct and complies with the platform's requirements
2.  Check your account plan: If you have recently downgraded to the [Hobby plan](/docs/plans/hobby), you may need to redeploy your projects to make them available once again
3.  Review email notifications: If you receive an email from Vercel about the pause, it may contain more details about the issue and next steps
4.  Verify account status: Ensure your account is in good standing and hasn't exceeded any [limits or quotas](/docs/limits)
5.  Review policies: Ensure that your deployment complies with all platform [policies](/legal/privacy-policy) and isn't in violation of any [terms](/legal/terms)
6.  Check for platform outages: Sometimes, platform-wide outages or issues can cause deployments to be blocked. Check the [status page](https://www.vercel-status.com/) for any ongoing incidents
7.  Contact support: If you've verified the above and are still experiencing the issue, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_DELETED"
description: "The deployment has been removed"
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_DELETED"
--------------------------------------------------------------------------------

# DEPLOYMENT\_DELETED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_DELETED` error occurs when a request is made for a deployment that has been removed based on the projects deployment retention policy.

410

DEPLOYMENT\_DELETED:

Deployment Deleted

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_DELETED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_DELETED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

Recently deleted deployments can be restored within 30 days of deletion.

To restore a deleted deployment, navigate to the Settings tab of your project:

1.  Select Security on the side panel of the project settings page
2.  Scroll down to the Recently Deleted section
3.  Find the deployment that needs to be restored, and click on the dropdown menu item Restore
4.  Complete the modal

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_DISABLED"
description: "The deployment is disabled. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_DISABLED"
--------------------------------------------------------------------------------

# DEPLOYMENT\_DISABLED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_DISABLED` error occurs when a deployment is disabled due to certain conditions or configurations. This might happen if there's a manual intervention required, or a specific condition is met that triggers the disabling of the deployment.

402

DEPLOYMENT\_DISABLED:

Payment required

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_DISABLED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_DISABLED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check your usage: Check the specific [usage limits](/dashboard/usage) you've exceeded in the [Vercel dashboard](/dashboard/usage)
2.  Check your account plan: If you have recently downgraded to the [Hobby plan](/docs/plans/hobby), you may need to redeploy your projects to make them available once again
3.  Review email notifications: If you receive an email from Vercel about the pause, it may contain more details about the issue and next steps
4.  Restore your site: The fastest solution is to [upgrade to the Pro plan](/docs/plans/pro). This plan offers more generous usage limits and pay-as-you-go options
5.  Contact support: If you've checked the above and are still unable to resolve the issue, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_NOT_FOUND"
description: "The deployment was not found. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_NOT_FOUND"
--------------------------------------------------------------------------------

# DEPLOYMENT\_NOT\_FOUND

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_NOT_FOUND` error occurs when a request is made for a deployment that doesn't exist. This could happen if the deployment ID or URL is incorrect, or if the deployment has been deleted.

404

DEPLOYMENT\_NOT\_FOUND:

Not Found

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_NOT\_FOUND to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_NOT_FOUND+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check the deployment URL: Ensure that the deployment URL you are using is correct and does not contain any typos or incorrect paths
2.  Check deployment existence: Verify that the [deployment exists](/docs/projects/project-dashboard#deployments) and has not been deleted
3.  Review deployment logs: If the deployment exists, review the [deployment logs](/docs/deployments/logs) to identify any issues that might have caused the deployment to be unavailable
4.  Verify permissions: Ensure you have the necessary [permissions](/docs/accounts/team-members-and-roles) to access the deployment
5.  Consult community resources: Visit our [community post on debugging 404 errors](https://community.vercel.com/t/debugging-404-errors/437) for additional tips and solutions shared by other developers.
6.  Contact support: If you've checked the above and are still unable to resolve the issue, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_NOT_READY_REDIRECTING"
description: "The deployment is not ready and is redirecting to another location. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_NOT_READY_REDIRECTING"
--------------------------------------------------------------------------------

# DEPLOYMENT\_NOT\_READY\_REDIRECTING

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_NOT_READY_REDIRECTING` error occurs when the requested deployment is not yet ready, and the request is redirected to the deployment status page.

303

DEPLOYMENT\_NOT\_READY\_REDIRECTING:

See Other

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_NOT\_READY\_REDIRECTING to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_NOT_READY_REDIRECTING+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check deployment status: Ensure that the [deployment process](/docs/projects/project-dashboard#deployments) has completed successfully and the deployment is ready to serve requests
2.  Inspect deployment logs: Review the [deployment logs](/docs/deployments/logs) for any indications as to why the deployment is not ready
3.  Verify Configuration: Check the configuration settings to ensure they are correct and that there are no misconfigurations
4.  Wait and refresh: If you encounter this error, wait for a few seconds and then refresh the page. In some cases, the deployment may still be in progress, and refreshing the page after a short interval can resolve the issue

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DEPLOYMENT_PAUSED"
description: "The deployment was paused. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DEPLOYMENT_PAUSED"
--------------------------------------------------------------------------------

# DEPLOYMENT\_PAUSED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DEPLOYMENT_PAUSED` error occurs when a deployment is paused due to certain conditions or configurations. This might happen if there's a manual intervention required, or a specific condition is met that triggers the pause.

503

DEPLOYMENT\_PAUSED:

Service Unavailable

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DEPLOYMENT\_PAUSED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDEPLOYMENT_PAUSED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check configuration: Ensure that your deployment configuration is correct and complies with the platform's requirements
2.  Review your spend management: You may have configured your deployments to pause once your spend amount is reached. Review your [spend management settings](/docs/spend-management#managing-your-spend-amount) to either adjust your limit or review your usage
3.  Verify account status: Ensure your account is in good standing and hasn't exceeded any [limits or quotas](/docs/limits)
4.  Review email notifications: If your account or deployment has been paused, Vercel will email you to share more details about the pause and outline next steps. Review the email for additional information about the pause and any necessary actions to resolve the issue
5.  Check for terms of service violations: If the pause is due to a breach of the [terms of service](/legal/terms) or [fair use guidelines](/docs/limits/fair-use-guidelines), review the specific usage limits and policies in the Vercel dashboard to understand the reasons for the pause
6.  Check for platform outages: Sometimes, platform-wide outages or issues can cause deployments to be blocked. Check the [status page](https://www.vercel-status.com/) for any ongoing incidents
7.  Contact support: If you've verified the above and are still experiencing the issue, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_EMPTY"
description: "An empty DNS record was received as part of the DNS response. This is a DNS error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_EMPTY"
--------------------------------------------------------------------------------

# DNS\_HOSTNAME\_EMPTY

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DNS_HOSTNAME_EMPTY` error occurs when an empty DNS record is received as part of the DNS response while attempting to connect to a private IP from an external rewrite.

502

DNS\_HOSTNAME\_EMPTY:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DNS\_HOSTNAME\_EMPTY to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDNS_HOSTNAME_EMPTY+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review DNS configuration: Check the [DNS configuration](/docs/domains/working-with-dns) to ensure that it's correctly set up and doesn't have any empty or incorrect entries
2.  Check for private IP addresses: Ensure that the request isn't attempting to connect to a private IP address from an external source
3.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_NOT_FOUND"
description: "The domain does not exist, resulting in an NXDOMAIN error during DNS resolution. This is a DNS error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_NOT_FOUND"
--------------------------------------------------------------------------------

# DNS\_HOSTNAME\_NOT\_FOUND

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DNS_HOSTNAME_NOT_FOUND` error occurs when there's an `NXDOMAIN` error during the DNS resolution while attempting to connect to a private IP from an external rewrite. This error indicates that the domain being requested does not exist.

502

DNS\_HOSTNAME\_NOT\_FOUND:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DNS\_HOSTNAME\_NOT\_FOUND to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDNS_HOSTNAME_NOT_FOUND+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review DNS configuration: Check the [DNS configuration](/docs/domains/working-with-dns) to ensure that the domain being requested is correctly set up and registered
2.  Verify domain registration: Ensure that the domain has been [registered](/docs/domains/working-with-domains/view-and-search-domains) and is currently active
3.  Check for private IP addresses: Ensure that the request isn't attempting to connect to a private IP address from an external source
4.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_RESOLVED_PRIVATE"
description: "The DNS hostname resolved to a private IP address or an IPv6 address during an external rewrite. This is a DNS error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_RESOLVED_PRIVATE"
--------------------------------------------------------------------------------

# DNS\_HOSTNAME\_RESOLVED\_PRIVATE

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DNS_HOSTNAME_RESOLVED_PRIVATE` error occurs when attempting to connect to a private IP from an external rewrite, or when trying to connect to an IPv6 address. The error indicates that the DNS hostname resolved to a private or inaccessible IP address.

Examples of such IPs would be:

*   `192.0.0.1`
*   `168.0.0.1`

404

DNS\_HOSTNAME\_RESOLVED\_PRIVATE:

Not Found

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DNS\_HOSTNAME\_RESOLVED\_PRIVATE to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDNS_HOSTNAME_RESOLVED_PRIVATE+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check the IP address: Ensure that the IP address you are trying to connect to is publicly accessible and not a private or reserved IP address
2.  Inspect network connectivity: Ensure that there are no network issues that could be affecting the DNS resolution
3.  Review application logs: Inspect the [application logs](/docs/deployments/logs) for any warnings or errors related to DNS or the attempted connections

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_RESOLVE_FAILED"
description: "No error with the DNS resolution but no IP was returned. This is a DNS error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_RESOLVE_FAILED"
--------------------------------------------------------------------------------

# DNS\_HOSTNAME\_RESOLVE\_FAILED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DNS_HOSTNAME_RESOLVE_FAILED` error occurs when attempting to connect to a private IP from an external rewrite. Although there's no error with the DNS resolution, no IP address is returned. This could be due to an issue with the domain name being queried, corrupted or malformed DNS responses, or network issues.

502

DNS\_HOSTNAME\_RESOLVE\_FAILED:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DNS\_HOSTNAME\_RESOLVE\_FAILED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDNS_HOSTNAME_RESOLVE_FAILED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check the domain name: Ensure that the [domain name](/docs/domains/working-with-domains/view-and-search-domains) you are trying to resolve is spelled correctly and is a valid domain. Typos or incorrect domain names can lead to DNS lookup failures
2.  Check DNS configuration: Verify the [configuration](/docs/domains/working-with-dns) of the DNS server and ensure it is set up correctly
3.  Firewall and security software: Check if any firewall or security software on your system is blocking DNS requests. Ensure that the DNS queries are allowed through your firewall
4.  Inspect network connectivity: Ensure that there are no network issues that could be affecting the DNS resolution

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "DNS_HOSTNAME_SERVER_ERROR"
description: "The DNS server was unable to fulfill the DNS request due to an internal issue or misconfiguration. This is a DNS error."
last_updated: "null"
source: "https://vercel.com/docs/errors/DNS_HOSTNAME_SERVER_ERROR"
--------------------------------------------------------------------------------

# DNS\_HOSTNAME\_SERVER\_ERROR

Copy page

Ask AI about this page

Last updated October 6, 2025

The `DNS_HOSTNAME_SERVER_ERROR` error occurs when attempting to connect to a private IP from an external rewrite. This error typically means that the DNS server was unable to fulfill the DNS request due to an internal issue or misconfiguration.

502

DNS\_HOSTNAME\_SERVER\_ERROR:

Bad Gateway

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/DNS\_HOSTNAME\_SERVER\_ERROR to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FDNS_HOSTNAME_SERVER_ERROR+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review DNS configuration: Check the [DNS configuration](/docs/domains/working-with-dns) to ensure it's correctly set up and doesn't contain any errors or misconfigurations
2.  Inspect network connectivity: Ensure that there are no network issues that could be affecting the DNS resolution
3.  Check DNS server logs: Review the logs of the DNS server for any warnings or errors that might indicate what's causing the issue
4.  Verify domain registration: Ensure that the domain has been [registered](/docs/domains/working-with-domains/view-and-search-domains) and is currently active

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "EDGE_FUNCTION_INVOCATION_FAILED"
description: "The request for a Edge Function was not completed successfully. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/EDGE_FUNCTION_INVOCATION_FAILED"
--------------------------------------------------------------------------------

# EDGE\_FUNCTION\_INVOCATION\_FAILED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `EDGE_FUNCTION_INVOCATION_FAILED` error occurs when there is an issue with the Edge Function being invoked on the CDN. This error can be caused by a variety of issues, including unhandled exceptions, timeouts, or malformed requests.

500

EDGE\_FUNCTION\_INVOCATION\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/EDGE\_FUNCTION\_INVOCATION\_FAILED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FEDGE_FUNCTION_INVOCATION_FAILED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Edge Function being invoked. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review deployment configuration: Double-check the deployment configuration to ensure that the Edge Function is being deployed correctly
3.  Investigate build errors: If the error occurs during the build process, troubleshoot any build errors that might be preventing the necessary resources from being deployed.
4.  Check function code: Ensure that the code for the Edge Function is correct and does not contain any errors or infinite loops
5.  Use Vercel's status page: If you have tried the steps above and are still experiencing the error, check Vercel's [status page](https://www.vercel-status.com/) for any reported outages in the CDN, which can sometimes cause this error

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "EDGE_FUNCTION_INVOCATION_TIMEOUT"
description: "The Edge Function invocation timed out. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/EDGE_FUNCTION_INVOCATION_TIMEOUT"
--------------------------------------------------------------------------------

# EDGE\_FUNCTION\_INVOCATION\_TIMEOUT

Copy page

Ask AI about this page

Last updated October 6, 2025

The `EDGE_FUNCTION_INVOCATION_TIMEOUT` error occurs when an Edge Function takes longer than the allowed execution time to complete or doesn't send a response chunk for a certain amount of time. This can be caused by long-running processes within the function or external dependencies that fail to respond in a timely manner.

If your backend API takes time to respond, we recommend [streaming the response](/docs/functions/streaming-functions) to avoid the idle timeout. For longer-running workloads, consider migrating to [Fluid compute](/docs/fluid-compute) which provides significantly longer durations and optimized performance.

504

EDGE\_FUNCTION\_INVOCATION\_TIMEOUT:

Gateway Timeout

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/EDGE\_FUNCTION\_INVOCATION\_TIMEOUT to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FEDGE_FUNCTION_INVOCATION_TIMEOUT+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Edge Function being invoked. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review function code: Inspect the Edge Function code for any long-running operations or infinite loops that could cause a timeout
3.  Verify return value: Ensure the function returns a response within the specified time limit of [25 seconds](/docs/functions/limitations#max-duration)
4.  Optimize external calls: If the function makes calls to external services or APIs, ensure they are optimized and responding quickly
5.  Consider streaming data: If the function is processing large amounts of data, consider using a [streaming approach](/docs/functions/streaming-functions) to avoid timeouts
6.  Implement error handling: Add error handling in the function to manage timeouts and other exceptions effectively

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FALLBACK_BODY_TOO_LARGE"
description: "The fallback body is too large for the cache. This is a cache error."
last_updated: "null"
source: "https://vercel.com/docs/errors/FALLBACK_BODY_TOO_LARGE"
--------------------------------------------------------------------------------

# FALLBACK\_BODY\_TOO\_LARGE

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FALLBACK_BODY_TOO_LARGE` error indicates that the size of the fallback body exceeds the maximum cache limit. This error typically occurs in prerendered pages when the response body of a fallback page is larger than the cache can accommodate. Notably, if the fallback exceeds 10MB, it cannot be cached.

502

FALLBACK\_BODY\_TOO\_LARGE:

Prerender fallback file is too big for cache

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FALLBACK\_BODY\_TOO\_LARGE to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFALLBACK_BODY_TOO_LARGE+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To resolve this error, consider the following steps:

1.  Review response size: Examine the size of the response body for the affected page. If it's too large, try to reduce the content size
2.  Optimize content: Minimize HTML, CSS, and JavaScript on the fallback page Remove unnecessary assets or data to reduce the page size
3.  Implement pagination: If the large response body is due to extensive datasets, consider using pagination. This divides the data into smaller, manageable sections
4.  Dynamic data loading: Where possible, load data dynamically on the client-side instead of sending all data in the initial server response

To prevent this error, ensure that the size of the fallback page is less than 10 MB.

[

### Not what you were looking for?

Explore different error codes by tag, code, or name on our Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FUNCTION_INVOCATION_FAILED"
description: "The invocation of a function failed. This is a function error."
last_updated: "null"
source: "https://vercel.com/docs/errors/FUNCTION_INVOCATION_FAILED"
--------------------------------------------------------------------------------

# FUNCTION\_INVOCATION\_FAILED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FUNCTION_INVOCATION_FAILED` error occurs when a function invocation fails. This could be due to an error within the function itself, or an issue with the environment in which the function is running.

500

FUNCTION\_INVOCATION\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FUNCTION\_INVOCATION\_FAILED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFUNCTION_INVOCATION_FAILED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the function invocation. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review function code: Ensure that the code for the function is correct and does not contain any errors or infinite loops. Use a `try/catch` block to catch any errors that might be occurring within the function code
3.  Check for unhandled exceptions: Look for any unhandled exceptions within the function code that might be causing the invocation to fail
4.  Verify function configuration: Double-check the function configuration to ensure that it's set up correctly, including any environment variables or other settings

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FUNCTION_INVOCATION_TIMEOUT"
description: "The request for a Vercel Function reached the timeout threshold. This is an application error."
last_updated: "null"
source: "https://vercel.com/docs/errors/FUNCTION_INVOCATION_TIMEOUT"
--------------------------------------------------------------------------------

# FUNCTION\_INVOCATION\_TIMEOUT

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FUNCTION_INVOCATION_TIMEOUT` error occurs when a function invocation takes longer than the [allowed execution time](/docs/functions/limitations#max-duration). This could be due to an error within the function itself, a slow network call, or an issue with the environment in which the function is running.

504

FUNCTION\_INVOCATION\_TIMEOUT:

Gateway Timeout

#### [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FUNCTION\_INVOCATION\_TIMEOUT to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFUNCTION_INVOCATION_TIMEOUT+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  The function is taking too long to process a request: Ensure that any API or database requests you make in your function respond within the [Vercel Function maximum duration](/docs/functions/limitations#max-duration) limit applicable to your plan. If you require a longer execution, consider enabling [Fluid compute](/docs/fluid-compute) which provides significantly longer durations and optimized performance for extended workloads.
2.  The function isn't returning a response: The function must return an HTTP response, even if that response is an error. If no response is returned, the function will time out
3.  You have an infinite loop within your function: Check that your function is not making an infinite loop at any stage of execution
4.  Upstream errors: Check that any external API or database that you are attempting to call doesn't have any errors
5.  A common cause for this issue is when the application contains an unhandled exception. Check the application logs, which can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view), for example:

logs-url

```
https://my-deployment-my-username.vercel.app/_logs
```

For more information on Vercel Functions timeouts, see [What can I do about Vercel Serverless Functions timing out?](/guides/what-can-i-do-about-vercel-serverless-functions-timing-out)

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FUNCTION_PAYLOAD_TOO_LARGE"
description: "The payload sent to the function is too large. This is a function error."
last_updated: "null"
source: "https://vercel.com/docs/errors/FUNCTION_PAYLOAD_TOO_LARGE"
--------------------------------------------------------------------------------

# FUNCTION\_PAYLOAD\_TOO\_LARGE

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FUNCTION_PAYLOAD_TOO_LARGE` error occurs when the payload sent to a function exceeds the maximum allowed size. This typically happens when the data sent in the request body to a serverless function is larger than the server can process.

413

FUNCTION\_PAYLOAD\_TOO\_LARGE:

Payload Too Large

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FUNCTION\_PAYLOAD\_TOO\_LARGE to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFUNCTION_PAYLOAD_TOO_LARGE+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review payload size: Check the size of the payload being sent to the function to ensure it's within the allowed limits, and does not exceed the [limit of 4.5MB](/docs/functions/runtimes#size-limits)
2.  Reduce payload size: If possible, reduce the size of the payload being sent to the function. This might include sending less data or compressing the data before sending it
3.  Client-side uploads: For large file uploads, consider using client-side uploads directly to [Vercel Blob](/docs/storage/vercel-blob#server-and-client-uploads), where the file is sent securely from the client to Vercel Blob without going through the server
4.  Split into multiple requests: If the payload data is too large to be sent in a single request, consider splitting the data into smaller chunks and sending multiple requests
5.  Use external storage: If the data is very large, consider using external storage solutions to handle the data instead of sending it directly in the request

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE"
description: "The function returned a response that is too large. This is a function error."
last_updated: "null"
source: "https://vercel.com/docs/errors/FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE"
--------------------------------------------------------------------------------

# FUNCTION\_RESPONSE\_PAYLOAD\_TOO\_LARGE

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FUNCTION_RESPONSE_PAYLOAD_TOO_LARGE` error occurs when the function returned a response that exceeds the maximum allowed size of 4.5 MB.

500

FUNCTION\_RESPONSE\_PAYLOAD\_TOO\_LARGE:

Response Payload Too Large

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FUNCTION\_RESPONSE\_PAYLOAD\_TOO\_LARGE to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFUNCTION_RESPONSE_PAYLOAD_TOO_LARGE+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Review response payload size: Check the size of the response payload being returned by the function to ensure it's within the allowed limits, and does not exceed the [limit of 4.5 MB](/docs/functions/runtimes#size-limits)
2.  Reduce response payload size: If possible, reduce the size of the response payload being returned by the function

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "FUNCTION_THROTTLED"
description: "The function you are trying to call has exceeded the rate limit."
last_updated: "null"
source: "https://vercel.com/docs/errors/FUNCTION_THROTTLED"
--------------------------------------------------------------------------------

# FUNCTION\_THROTTLED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `FUNCTION_THROTTLED` error occurs when your Vercel Functions exceed the concurrent execution limit, often due to a sudden request spike or backend API issues. For more information, see [What should I do if I receive a 503 error on Vercel?](/guides/what-should-i-do-if-i-receive-a-503-error-on-vercel).

Although this is a rare scenario, this error can also occur when Vercel's infrastructure encounters an abnormal system load and tries to mitigate the impact autonomously.

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/FUNCTION\_THROTTLED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FFUNCTION_THROTTLED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Vercel Function being invoked. For example, your function might be waiting for a slow backend API without a reasonable timeout. These information can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view), as well as the [Observability](/docs/observability) tab in the Vercel dashboard.
2.  Handle request spikes: If you're experiencing a sudden spike in requests, consider using the [Vercel Firewall](/docs/vercel-firewall) to block unwanted traffic, or enabling [Rate Limiting](/docs/security/vercel-waf/rate-limiting) to limit the number of requests per second.
3.  Optimize your function: Review your function code to ensure it's optimized for performance. For example, you can use [Vercel Edge Cache](/docs/edge-cache) to cache responses and reduce the number of invocations. You can also enable [fluid compute](/docs/fluid-compute) to handle more requests concurrently on a single function instance.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INFINITE_LOOP_DETECTED"
description: "An infinite loop was detected within the application."
last_updated: "null"
source: "https://vercel.com/docs/errors/INFINITE_LOOP_DETECTED"
--------------------------------------------------------------------------------

# INFINITE\_LOOP\_DETECTED

Copy page

Ask AI about this page

Last updated October 6, 2025

The `INFINITE_LOOP_DETECTED` error occurs when an infinite loop is detected within the application. This error can occur when the application is making an infinite number of requests to itself, or when the application is making an infinite number of requests to an external API or database.

508

INFINITE\_LOOP\_DETECTED:

Loop Detected

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/INFINITE\_LOOP\_DETECTED to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FINFINITE_LOOP_DETECTED+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check the application's source code: Look for any code that might cause an infinite loop, such as a looping fetch or an unconditional redirect
2.  Check the application's configuration: Review any [configuration](/docs/redirects#configuration-redirects) files, such as `next.config.js` or `vercel.json`, to ensure they are not causing the infinite loop
3.  Review external API or database calls: Ensure that any external API or database calls your application is making do not have errors or infinite loops
4.  Handle unhandled exceptions: Check the application logs for any unhandled exceptions that might be causing the infinite loop
5.  Use Vercel's status page: If you have tried the steps above and are still experiencing the error, check Vercel's [status page](https://www.vercel-status.com/) for any reported outages in the CDN, which can sometimes cause this error

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_CACHE_ERROR"
description: "An unexpected error happened when CDN is fetching data from the Vercel cache."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_CACHE_ERROR"
--------------------------------------------------------------------------------

# INTERNAL\_CACHE\_ERROR

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_CACHE_ERROR` error occurs during an unexpected issue in the CDN while retrieving data from the Vercel cache.

500

INTERNAL\_CACHE\_ERROR:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: If the error persists, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_CACHE_KEY_TOO_LONG"
description: "The CDN is failing to fetch from the internal cache due to a cache key being too long. This error can be caused by a request URL that is too long."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_CACHE_KEY_TOO_LONG"
--------------------------------------------------------------------------------

# INTERNAL\_CACHE\_KEY\_TOO\_LONG

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_CACHE_KEY_TOO_LONG` error occurs when the CDN is unable to fetch from the internal cache due to a cache key being too long. This error can be caused by a request URL that is too long.

500

INTERNAL\_CACHE\_KEY\_TOO\_LONG:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: If the error persists, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_CACHE_LOCK_FULL"
description: "An unexpected error happened when CDN is accessing internal cache."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_CACHE_LOCK_FULL"
--------------------------------------------------------------------------------

# INTERNAL\_CACHE\_LOCK\_FULL

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_CACHE_LOCK_FULL` error occurs when CDN is accessing internal cache. This error is usually caused by a temporary issue with the internal cache.

500

INTERNAL\_CACHE\_LOCK\_FULL:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: If the error persists, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_CACHE_LOCK_TIMEOUT"
description: "An unexpected error happened when CDN is accessing internal cache."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_CACHE_LOCK_TIMEOUT"
--------------------------------------------------------------------------------

# INTERNAL\_CACHE\_LOCK\_TIMEOUT

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_CACHE_LOCK_TIMEOUT` error occurs when CDN is accessing internal cache.

500

INTERNAL\_CACHE\_LOCK\_TIMEOUT:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: If the error persists, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_DEPLOYMENT_FETCH_FAILED"
description: "Failed to fetch the internal deployment. This is a deployment error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_DEPLOYMENT_FETCH_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_DEPLOYMENT\_FETCH\_FAILED

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_DEPLOYMENT_FETCH_FAILED` error occurs when the system is unable to fetch the deployment. This could happen due to network issues, misconfigurations, or other internal errors that prevent the deployment data from being retrieved.

414

INTERNAL\_DEPLOYMENT\_FETCH\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Check deployment status: Ensure that the [deployment exists](/docs/projects/project-dashboard#deployments) and is in a stable state
2.  Inspect deployment logs: Review the [deployment logs](/docs/deployments/logs) to identify any specific errors or issues that might have occurred during the fetching process
3.  Review deployment history: Check the deployment history to see if the deployment was deleted or [rolled back](/docs/instant-rollback)

[

### Not what you were looking for?

Return to the Errors documentation section

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_EDGE_FUNCTION_INVOCATION_FAILED"
description: "The request for a Edge Function was not completed successfully due to an internal error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_EDGE_FUNCTION_INVOCATION_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_FAILED

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_EDGE_FUNCTION_INVOCATION_FAILED` error occurs when there is an issue with the Edge Function being invoked on the CDN. This error can be caused by a variety of internal issues.

500

INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

While this error can be caused by a variety of issues, it's transient and retrying the request will succeed. If the error persists, [contact support](/help) along with the request ID on the error page.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_EDGE_FUNCTION_INVOCATION_TIMEOUT"
description: "The Edge Function invocation timed out unexpectedly."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_EDGE_FUNCTION_INVOCATION_TIMEOUT"
--------------------------------------------------------------------------------

# INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_TIMEOUT

Copy page

Ask AI about this page

Last updated August 22, 2025

The `INTERNAL_EDGE_FUNCTION_INVOCATION_TIMEOUT` error occurs when an Edge Function takes longer than the allowed execution time to complete. This can be caused by long-running processes within the function or external dependencies that fail to respond in a timely manner.

504

INTERNAL\_EDGE\_FUNCTION\_INVOCATION\_TIMEOUT:

Gateway Timeout

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the Edge Function being invoked. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review function code: Inspect the Edge Function code for any long-running operations or infinite loops that could cause a timeout
3.  Verify return value: Ensure the function begins responding within [25 seconds](/docs/functions/limitations#max-duration)
4.  Optimize external calls: If the function makes calls to external services or APIs, ensure they are optimized and responding quickly
5.  Consider streaming data: If the function is processing large amounts of data, consider using a [streaming approach](/docs/functions/streaming-functions) to avoid timeouts
6.  Implement error handling: Add error handling in the function to manage timeouts and other exceptions effectively

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_FUNCTION_INVOCATION_FAILED"
description: "The internal invocation of a function failed. This is Vercel's error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_INVOCATION_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_FUNCTION\_INVOCATION\_FAILED

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_FUNCTION_INVOCATION_FAILED` error occurs when a function invocation fails. This could be due to an error within the function itself, or an issue with the environment in which the function is running.

500

INTERNAL\_FUNCTION\_INVOCATION\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Check application logs: Review the application logs to identify any specific errors related to the internal function invocation. They can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view)
2.  Review function code: Ensure that the code for the function is correct and does not contain any errors or infinite loops
3.  Verify function configuration: Double-check the function configuration to ensure that it's set up correctly, including any environment variables or other settings
4.  Check external dependencies: If the function relies on external services or APIs, ensure they are responding in a timely manner

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_FUNCTION_INVOCATION_TIMEOUT"
description: "The internal invocation of a function timed out. This is Vercel's error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_INVOCATION_TIMEOUT"
--------------------------------------------------------------------------------

# INTERNAL\_FUNCTION\_INVOCATION\_TIMEOUT

Copy page

Ask AI about this page

Last updated June 25, 2025

The `INTERNAL_FUNCTION_INVOCATION_TIMEOUT` error occurs when a function invocation takes longer than the allowed execution time. This could be due to an error within the function itself, a slow network call, or an issue with the environment in which the function is running.

504

INTERNAL\_FUNCTION\_INVOCATION\_TIMEOUT:

Gateway Timeout

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  The function is taking too long to process a request: Ensure that any API or database requests you make in your function respond within the [Vercel Function maximum duration](/docs/functions/limitations#max-duration) limit applicable to your plan. If you require a longer execution, consider enabling [Fluid compute](/docs/fluid-compute), which provides significantly longer durations and optimized performance for extended workloads.
2.  The function isn't returning a response: The function must return an HTTP response, even if that response is an error. If no response is returned, the function will time out
3.  You have an infinite loop within your function: Check that your function is not making an infinite loop at any stage of execution
4.  Upstream errors: Check that any external API or database that you are attempting to call doesn't have any errors
5.  A common cause for this issue is when the application contains an unhandled exception. Check the application logs, which can be found at the host URL under [the `/_logs` path](/docs/deployments/build-features#logs-view), for example:

logs-url

```
https://my-deployment-my-username.vercel.app/_logs
```

For more information on Vercel Functions timeouts, see [What can I do about Vercel Serverless Functions timing out?](/guides/what-can-i-do-about-vercel-serverless-functions-timing-out)

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_FUNCTION_NOT_FOUND"
description: "The internal function could not be found. This is a Vercel's error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_NOT_FOUND"
--------------------------------------------------------------------------------

# INTERNAL\_FUNCTION\_NOT\_FOUND

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_FUNCTION_NOT_FOUND` error occurs when an attempt to invoke a function fails because the function could not be found. This could happen if the function was not properly deployed, or if there is a misconfiguration in the function's settings or environment.

500

INTERNAL\_FUNCTION\_NOT\_FOUND:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Verify function deployment: Ensure that the function has been successfully deployed and is available in the environment where it is being invoked
2.  Check function name: Verify that the function name being used in the invocation matches the deployed function name
3.  Review configuration: Check the function configuration in your project, including the function file name and the path where it is located
4.  Check for typos: Ensure that there are no typos or incorrect references in the function name or in the invocation command

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_FUNCTION_NOT_READY"
description: "The internal function is not ready to be invoked. This is a Vercel error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_FUNCTION_NOT_READY"
--------------------------------------------------------------------------------

# INTERNAL\_FUNCTION\_NOT\_READY

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_FUNCTION_NOT_READY` error occurs when an attempt is made to invoke a function before it is ready to accept requests. This might happen if the function is still being deployed, initialized, or if there is a misconfiguration preventing the function from becoming ready.

500

INTERNAL\_FUNCTION\_NOT\_READY:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Verify deployment status: Ensure that the function has been successfully deployed and the deployment process has completed
2.  Check initialization logs: Review the function's initialization logs to identify any errors or warnings that might indicate why the function is not ready
3.  Review configuration: Ensure that the function and environment configurations are correct and that there are no misconfigurations preventing the function from becoming ready
4.  Check dependencies: Verify that all dependencies required by the function are available and correctly configured

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_MICROFRONTENDS_BUILD_ERROR"
description: "The microfrontend build did not include the required data as expected."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_MICROFRONTENDS_BUILD_ERROR"
--------------------------------------------------------------------------------

# INTERNAL\_MICROFRONTENDS\_BUILD\_ERROR

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_MICROFRONTENDS_BUILD_ERROR` error occurs when the deployment is missing data that should have been included as part of the build.

This error should not occur because the build is designed to fail in such cases.

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  We have been notified of this error. For more information, check the [Vercel status page](https://www.vercel-status.com/) or [contact Vercel support](/help#issues)

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_MICROFRONTENDS_INVALID_CONFIGURATION_ERROR"
description: "The microfrontend configuration file is invalid."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_MICROFRONTENDS_INVALID_CONFIGURATION_ERROR"
--------------------------------------------------------------------------------

# INTERNAL\_MICROFRONTENDS\_INVALID\_CONFIGURATION\_ERROR

Copy page

Ask AI about this page

Last updated August 21, 2025

The `INTERNAL_MICROFRONTENDS_INVALID_CONFIGURATION_ERROR` error occurs when the configuration file for the deployment is invalid.

This error indicates that an invalid configuration file has been deployed.

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Ensure the config in your `microfrontends.json` file is valid, see the [documentation](/docs/microfrontends/quickstart).
2.  Ensure you are on the latest version of the [`@vercel/microfrontends`](https://www.npmjs.com/package/@vercel/microfrontends) package.
3.  We have been notified of this error. For more information, check the [Vercel status page](https://www.vercel-status.com/) or [contact Vercel support](/help#issues)

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_MICROFRONTENDS_UNEXPECTED_ERROR"
description: "An unexpected internal error occurred in the microfrontend."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_MICROFRONTENDS_UNEXPECTED_ERROR"
--------------------------------------------------------------------------------

# INTERNAL\_MICROFRONTENDS\_UNEXPECTED\_ERROR

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_MICROFRONTENDS_UNEXPECTED_ERROR` occurs due to unspecified internal issues, such as system faults or unhandled exceptions.

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  We have been notified of this error. For more information, check the [Vercel status page](https://www.vercel-status.com/) or [contact Vercel support](/help#issues)

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_MISSING_RESPONSE_FROM_CACHE"
description: "This error indicates a missing response from the cache during a deployment or build process."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_MISSING_RESPONSE_FROM_CACHE"
--------------------------------------------------------------------------------

# INTERNAL\_MISSING\_RESPONSE\_FROM\_CACHE

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_MISSING_RESPONSE_FROM_CACHE` error occurs when an unexpected error happened during the CDN accessing the internal cache.

500

INTERNAL\_MISSING\_RESPONSE\_FROM\_CACHE:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: If the error persists, [contact support](/help#issues) for further assistance

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_OPTIMIZED_IMAGE_REQUEST_FAILED"
description: "The request for an internally optimized image failed. This is a server error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_OPTIMIZED_IMAGE_REQUEST_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_OPTIMIZED\_IMAGE\_REQUEST\_FAILED

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_OPTIMIZED_IMAGE_REQUEST_FAILED` error occurs when the request for an internally optimized image fails.

502

INTERNAL\_OPTIMIZED\_IMAGE\_REQUEST\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Verify image path: Ensure that the image path is correct and the server can access the image
2.  Check logs: Review [logs](/docs/runtime-logs) for more details on the error
3.  Validate configuration: Ensure that the configuration for image optimization is correct

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_ROUTER_CANNOT_PARSE_PATH"
description: "The CDN has failed to parse application-specified URL, such as rewrite/redirection URLs."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_ROUTER_CANNOT_PARSE_PATH"
--------------------------------------------------------------------------------

# INTERNAL\_ROUTER\_CANNOT\_PARSE\_PATH

Copy page

Ask AI about this page

Last updated September 9, 2025

The `INTERNAL_ROUTER_CANNOT_PARSE_PATH` error occurs when the CDN has failed to parse application-specified URL, such as rewrite/redirection URLs.

500

INTERNAL\_ROUTER\_CANNOT\_PARSE\_PATH:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Check configuration: Check your configuration and make sure your app doesn't generate invalid URLs

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_STATIC_REQUEST_FAILED"
description: "This error occurs when a request for a static file in a project fails."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_STATIC_REQUEST_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_STATIC\_REQUEST\_FAILED

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_STATIC_REQUEST_FAILED` error is encountered when a request for a static file within the project cannot be completed. This can happen due to issues with the existence, deployment, or path of the static files.

500

INTERNAL\_STATIC\_REQUEST\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Check static files existence: Ensure that all static files exist in your project and are correctly deployed. Confirm that they are included in the deployment package
2.  Verify file paths: Check that the paths to your static files are correct and reachable. Path errors or misconfigurations can lead to this issue
3.  Rollback changes: If your project was working previously, consider reverting to a known working state. [Rollback](/docs/instant-rollback) your recent changes one by one and redeploy to see if the error resolves. This can help identify if recent changes are causing the issue

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_UNARCHIVE_FAILED"
description: "Unarchiving of the deployment or resource failed. This is an internal error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_UNARCHIVE_FAILED"
--------------------------------------------------------------------------------

# INTERNAL\_UNARCHIVE\_FAILED

Copy page

Ask AI about this page

Last updated July 18, 2025

The `INTERNAL_UNARCHIVE_FAILED` error typically occurs when the platform encounters a problem trying to extract your deployment's archive. This issue often can be related to one of the following:

*   The structure of your project or the contents within it
*   The size of your deployment bundle for Vercel functions exceeds the limit. For Vercel functions, the [maximum uncompressed size is 250 MB](/docs/functions/runtimes#bundle-size-limits)

500

INTERNAL\_UNARCHIVE\_FAILED:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

*   Check your project files: Check for any files or directories that have been unnecessarily included in the deployment. Removing unnecessary files or directories can help reduce the size of your deployment
*   Check bundle size: Looking into your `includeFiles` and `excludeFiles` configuration to specify items affecting the function size. See [bundle size limits](/docs/functions/runtimes#bundle-size-limits)

[

### Not what you were looking for?

Return to the Errors documentation section

](/docs/errors)

--------------------------------------------------------------------------------
title: "INTERNAL_UNEXPECTED_ERROR"
description: "An unexpected internal error occurred. This is a general internal error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INTERNAL_UNEXPECTED_ERROR"
--------------------------------------------------------------------------------

# INTERNAL\_UNEXPECTED\_ERROR

Copy page

Ask AI about this page

Last updated March 4, 2025

The `INTERNAL_UNEXPECTED_ERROR` error occurs when an unexpected and unspecified internal error happens within the system. This type of error can be due to a variety of reasons, including system faults, unhandled exceptions, or unforeseen issues in the application.

500

INTERNAL\_UNEXPECTED\_ERROR:

Internal Server Error

## [Troubleshoot](#troubleshoot)

To troubleshoot this error, follow these steps:

1.  Contact support: Since this error is general and could be due to a variety of reasons, [contact support](/help#issues) for further assistance, supplying your deployment ID

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INVALID_IMAGE_OPTIMIZE_REQUEST"
description: "The query string is using an invalid value for q, w, or url parameters. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INVALID_IMAGE_OPTIMIZE_REQUEST"
--------------------------------------------------------------------------------

# INVALID\_IMAGE\_OPTIMIZE\_REQUEST

Copy page

Ask AI about this page

Last updated October 6, 2025

The `INVALID_IMAGE_OPTIMIZE_REQUEST` error occurs when the query string is using an invalid value for `q` (quality) or `w` (width), or `url` returns a non-image response.

400

INVALID\_IMAGE\_OPTIMIZE\_REQUEST:

Bad Request

## [Troubleshoot](#troubleshoot)

I'm encountering an error and reviewing the docs at /flg~eyJhbGciOiJIUzI1NiJ9.\_v7-\_v39.f3M12-KAPZCzcefUX\_oPWq-I0u4iAhoJCQaxpxor\_bI/docs/errors/INVALID\_IMAGE\_OPTIMIZE\_REQUEST to understand what's happening. Please help me resolve this by: 1. \*\*Suggest the fix\*\*: Analyze my codebase context and propose what needs to be changed to resolve this error 2. \*\*Explain the root cause\*\*: Break down why this error occurred: - What was the code actually doing vs. what it needed to do? - What conditions triggered this specific error? - What misconception or oversight led to this? 3. \*\*Teach the concept\*\*: Help me understand the underlying principle: - Why does this error exist and what is it protecting me from? - What's the correct mental model for this concept? - How does this fit into the broader framework/language design? 4. \*\*Show warning signs\*\*: Help me recognize this pattern in the future: - What should I look out for that might cause this again? - Are there similar mistakes I might make in related scenarios? - What code smells or patterns indicate this issue? 5. \*\*Discuss alternatives\*\*: Explain if there are different valid approaches and their trade-offs My goal is to fix the immediate issue while building lasting understanding so I can avoid and resolve similar errors independently in the future.

[Open in Cursor](https://cursor.com/link/prompt?text=I%27m+encountering+an+error+and+reviewing+the+docs+at+https%3A%2F%2Fvercel.com%2Fflg%7EeyJhbGciOiJIUzI1NiJ9._v7-_v39.f3M12-KAPZCzcefUX_oPWq-I0u4iAhoJCQaxpxor_bI%2Fdocs%2Ferrors%2FINVALID_IMAGE_OPTIMIZE_REQUEST+to+understand+what%27s+happening.%0A%0APlease+help+me+resolve+this+by%3A%0A%0A1.+**Suggest+the+fix**%3A+Analyze+my+codebase+context+and+propose+what+needs+to+be+changed+to+resolve+this+error%0A2.+**Explain+the+root+cause**%3A+Break+down+why+this+error+occurred%3A%0A+++-+What+was+the+code+actually+doing+vs.+what+it+needed+to+do%3F%0A+++-+What+conditions+triggered+this+specific+error%3F%0A+++-+What+misconception+or+oversight+led+to+this%3F%0A3.+**Teach+the+concept**%3A+Help+me+understand+the+underlying+principle%3A%0A+++-+Why+does+this+error+exist+and+what+is+it+protecting+me+from%3F%0A+++-+What%27s+the+correct+mental+model+for+this+concept%3F%0A+++-+How+does+this+fit+into+the+broader+framework%2Flanguage+design%3F%0A4.+**Show+warning+signs**%3A+Help+me+recognize+this+pattern+in+the+future%3A%0A+++-+What+should+I+look+out+for+that+might+cause+this+again%3F%0A+++-+Are+there+similar+mistakes+I+might+make+in+related+scenarios%3F%0A+++-+What+code+smells+or+patterns+indicate+this+issue%3F%0A5.+**Discuss+alternatives**%3A+Explain+if+there+are+different+valid+approaches+and+their+trade-offs%0A%0AMy+goal+is+to+fix+the+immediate+issue+while+building+lasting+understanding+so+I+can+avoid+and+resolve+similar+errors+independently+in+the+future.)

To troubleshoot this error, follow these steps:

1.  Check for typos: Verify that there are no typos in the parameter names or values
2.  Review request format: Ensure that the request URL is correctly formatted and includes the required parameters
    *   The `q` parameter controls the quality of the image and must follow these rules:
        *   The `q` parameter must be an integer
        *   The `q` integer must be greater than or equal to 1
        *   The `q` integer must be less than or equal to 100
        *   The `q` integer must be the same as one specified in [`qualities`](https://nextjs.org/docs/app/api-reference/components/image#qualities), if defined
    *   The `w` parameter defines the width of the image and must follow these rules:
        *   The `w` parameter must be an integer
        *   The `w` integer must be the same as one specified in [`deviceSizes`](https://nextjs.org/docs/app/api-reference/components/image#devicesizes) or [`imageSizes`](https://nextjs.org/docs/app/api-reference/components/image#imagesizes) in your [`next.config.js`](https://nextjs.org/docs/app/api-reference/next-config-js).
    *   The `url` parameter specifies the image location and must follow these rules:
        *   The `url` parameter must start with `/`, `http://`, or `https://`
        *   The `url` parameter must match one of the configured [`remotePatterns`](https://nextjs.org/docs/app/api-reference/components/image#remotepatterns) or [`localPatterns`](https://nextjs.org/docs/app/api-reference/components/image#localpatterns) in your `next.config.js`
        *   The `url` parameter must have a `Content-Type` header that starts with `image/`
        *   The `url` parameter must have a response body less than 300 MB (or less than 100 MB for hobby), otherwise the image won't be optimized

Run `next dev` locally to reproduce the error and get additional details.

[

### Not what you were looking for?

Try filtering the errors by tag, code, or name on the Error Codes page.

](/docs/errors)

--------------------------------------------------------------------------------
title: "INVALID_REQUEST_METHOD"
description: "The request method used is invalid or not supported. This is a request error."
last_updated: "null"
source: "https://vercel.com/docs/errors/INVALID_REQUEST_METHOD"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./07-working-with-ssl-certificates.md) | [Index](./index.md) | [Next →](./09-invalid-request-method.md)
