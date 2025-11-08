**Navigation:** [← Previous](./10-frameworks-on-vercel.md) | [Index](./index.md) | [Next →](./12-add-a-domain.md)

---

# Supported Frameworks on Vercel

Copy page

Ask AI about this page

Last updated July 31, 2025

## [Frameworks infrastructure support matrix](#frameworks-infrastructure-support-matrix)

The following table shows which features are supported by each framework on Vercel. The framework list is not exhaustive, but a representation of the most popular frameworks deployed on Vercel.

We're committed to having support for all Vercel features across frameworks, and continue to work with framework authors on adding support. _This table is continually updated over time_.

Supported

Not Supported

Not Applicable

Framework feature matrix
| 
Feature

 | 

Next.js

 | 

SvelteKit

 | 

Nuxt

 | 

Astro

 | 

Remix

 | 

Vite

 | 

Gatsby

 | 

CRA

 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 

[Static Assets](/docs/edge-network/overview)

Support for static assets being served and cached directly from the edge

 |  |  |  |  |  |  |  |  |
| 

[Edge Routing Rules](/docs/edge-network/overview#edge-routing-rules)

Lets you configure incoming requests, set headers, and cache responses

 |  |  |  |  |  |  |  |  |
| 

[Routing Middleware](/docs/functions/edge-middleware)

Execute code before a request is processed

 |  |  |  |  |  |  |  |  |
| 

[Server-Side Rendering](/docs/functions)

Render pages dynamically on the server

 |  |  |  |  |  |  |  |  |
| 

[Streaming SSR](/docs/functions/streaming)

Stream responses and render parts of the UI as they become ready

 |  |  |  |  |  |  |  |  |
| 

[Incremental Static Regeneration](/docs/incremental-static-regeneration)

Create or update content on your site without redeploying

 |  |  |  |  |  |  |  |  |
| 

[Image Optimization](/docs/image-optimization)

Optimize and cache images at the edge

 |  |  |  |  |  |  |  |  |
| 

[Data Cache](/docs/infrastructure/data-cache)

A granular cache for storing responses from fetches

 |  |  |  |  |  |  |  |  |
| 

[Native OG Image Generation](/docs/functions/og-image-generation)

Generate dynamic open graph images using Vercel Functions

 |  |  |  |  |  |  |  |  |
| 

[Multi-runtime support (different routes)](/docs/functions/runtimes)

Customize runtime environments per route

 |  |  |  |  |  |  |  |  |
| 

[Multi-runtime support (entire app)](/docs/functions/runtimes)

Lets your whole application utilize different runtime environments

 |  |  |  |  |  |  |  |  |
| 

[Output File Tracing](/guides/how-can-i-use-files-in-serverless-functions)

Analyzes build artifacts to identify and include only necessary files for the runtime

 |  |  |  |  |  |  |  |  |
| 

[Skew Protection](/docs/deployments/skew-protection)

Ensure that only the latest deployment version serves your traffic by not serving older versions of code

 |  |  |  |  |  |  |  |  |
| 

[Routing Middleware](/docs/functions/edge-middleware)

Framework-native integrated middleware convention

 |  |  |  |  |  |  |  |  |

## [All frameworks](#all-frameworks)

The frameworks listed below can be deployed to Vercel with minimal configuration. See [our docs on framework presets](/docs/deployments/configure-a-build#framework-preset) to learn more about configuration.

![Angular](https://api-frameworks.vercel.sh/framework-logos/angular.svg)

### Angular

Angular is a TypeScript-based cross-platform framework from Google.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/angular)[View Demo](https://angular-template.vercel.app)

![Astro](https://api-frameworks.vercel.sh/framework-logos/astro.svg)![Astro](https://api-frameworks.vercel.sh/framework-logos/astro-dark.svg)

### Astro

Astro is a new kind of static site builder for the modern web. Powerful developer experience meets lightweight output.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/astro)[View Demo](https://astro-template.vercel.app)

![Brunch](https://api-frameworks.vercel.sh/framework-logos/brunch.svg)

### Brunch

Brunch is a fast and simple webapp build tool with seamless incremental compilation for rapid development.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/brunch)[View Demo](https://brunch-template.vercel.app)

![Create React App](https://api-frameworks.vercel.sh/framework-logos/react.svg)

### React

Create React App allows you to get going with React in no time.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/create-react-app)[View Demo](https://create-react-template.vercel.app)

![Docusaurus (v1)](https://api-frameworks.vercel.sh/framework-logos/docusaurus.svg)

### Docusaurus (v1)

Docusaurus makes it easy to maintain Open Source documentation websites.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/docusaurus)[View Demo](https://docusaurus-template.vercel.app)

![Docusaurus (v2+)](https://api-frameworks.vercel.sh/framework-logos/docusaurus.svg)

### Docusaurus (v2+)

Docusaurus makes it easy to maintain Open Source documentation websites.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/docusaurus-2)[View Demo](https://docusaurus-2-template.vercel.app)

![Dojo](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fdojo.png&w=48&q=75)

### Dojo

Dojo is a modern progressive, TypeScript first framework.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/dojo)[View Demo](https://dojo-template.vercel.app)

![Eleventy](https://api-frameworks.vercel.sh/framework-logos/eleventy.svg)

### Eleventy

11ty is a simpler static site generator written in JavaScript, created to be an alternative to Jekyll.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/eleventy)[View Demo](https://eleventy-template.vercel.app)

![Elysia](https://api-frameworks.vercel.sh/framework-logos/elysia.svg)

### Elysia

Ergonomic framework for humans

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/elysia)View Demo

![Ember.js](https://api-frameworks.vercel.sh/framework-logos/ember.svg)

### Ember.js

Ember.js helps webapp developers be more productive out of the box.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/ember)[View Demo](https://ember-template.vercel.app)

![Express](https://api-frameworks.vercel.sh/framework-logos/express.svg)![Express](https://api-frameworks.vercel.sh/framework-logos/express.svg)

### Express

Fast, unopinionated, minimalist web framework for Node.js

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/express)[View Demo](https://express-vercel-example-demo.vercel.app/)

![FastAPI](https://api-frameworks.vercel.sh/framework-logos/fastapi.svg)

### FastAPI

FastAPI framework, high performance, easy to learn, fast to code, ready for production

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fastapi)[View Demo](https://vercel-fastapi-gamma-smoky.vercel.app/)

![FastHTML](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Ffasthtml.png&w=48&q=75)

### FastHTML

The fastest way to create an HTML app

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fasthtml)[View Demo](https://fasthtml-template.vercel.app)

![Fastify](https://api-frameworks.vercel.sh/framework-logos/fastify.svg)![Fastify](https://api-frameworks.vercel.sh/framework-logos/fastify-dark.svg)

### Fastify

Fast and low overhead web framework, for Node.js

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fastify)View Demo

![Flask](https://api-frameworks.vercel.sh/framework-logos/flask.svg)

### Flask

The Python micro web framework

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/flask)View Demo

![Gatsby.js](https://api-frameworks.vercel.sh/framework-logos/gatsby.svg)

### Gatsby.js

Gatsby helps developers build blazing fast websites and apps with React.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/gatsby)[View Demo](https://gatsby.vercel.app)

![Gridsome](https://api-frameworks.vercel.sh/framework-logos/gridsome.svg)

### Gridsome

Gridsome is a Vue.js-powered framework for building websites & apps that are fast by default.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/gridsome)[View Demo](https://gridsome-template.vercel.app)

![H3](https://api-frameworks.vercel.sh/framework-logos/h3.svg)

### H3

Universal, Tiny, and Fast Servers

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/h3)View Demo

![Hexo](https://api-frameworks.vercel.sh/framework-logos/hexo.svg)

### Hexo

Hexo is a fast, simple & powerful blog framework powered by Node.js.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/hexo)[View Demo](https://hexo-template.vercel.app)

![Hono](https://api-frameworks.vercel.sh/framework-logos/hono.svg)

### Hono

Web framework built on Web Standards

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/hono)[View Demo](https://hono.vercel.dev)

![Hugo](https://api-frameworks.vercel.sh/framework-logos/hugo.svg)

### Hugo

Hugo is the world’s fastest framework for building websites, written in Go.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/hugo)[View Demo](https://hugo-template.vercel.app)

![Hydrogen (v1)](https://api-frameworks.vercel.sh/framework-logos/hydrogen.svg)

### Hydrogen (v1)

React framework for headless commerce

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/hydrogen)[View Demo](https://hydrogen-template.vercel.app)

![Ionic Angular](https://api-frameworks.vercel.sh/framework-logos/ionic.svg)

### Ionic Angular

Ionic Angular allows you to build mobile PWAs with Angular and the Ionic Framework.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/ionic-angular)[View Demo](https://ionic-angular-template.vercel.app)

![Ionic React](https://api-frameworks.vercel.sh/framework-logos/ionic.svg)

### Ionic React

Ionic React allows you to build mobile PWAs with React and the Ionic Framework.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/ionic-react)[View Demo](https://ionic-react-template.vercel.app)

![Jekyll](https://api-frameworks.vercel.sh/framework-logos/jekyll.svg)

### Jekyll

Jekyll makes it super easy to transform your plain text into static websites and blogs.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/jekyll)[View Demo](https://jekyll-template.vercel.app)

![Middleman](https://api-frameworks.vercel.sh/framework-logos/middleman.svg)

### Middleman

Middleman is a static site generator that uses all the shortcuts and tools in modern web development.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/middleman)[View Demo](https://middleman-template.vercel.app)

![NestJS](https://api-frameworks.vercel.sh/framework-logos/nestjs.svg)

### NestJS

Framework for building efficient, scalable Node.js server-side applications

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nestjs)View Demo

![Next.js](https://api-frameworks.vercel.sh/framework-logos/next.svg)

### Next.js

Next.js makes you productive with React instantly — whether you want to build static or dynamic sites.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nextjs)[View Demo](https://nextjs-template.vercel.app)

![Nitro](https://api-frameworks.vercel.sh/framework-logos/nitro.svg)

### Nitro

Nitro is a next generation server toolkit.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nitro)[View Demo](https://nitro-template.vercel.app)

![Nuxt](https://api-frameworks.vercel.sh/framework-logos/nuxt.svg)

### Nuxt

Nuxt is the open source framework that makes full-stack development with Vue.js intuitive.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nuxtjs)[View Demo](https://nuxtjs-template.vercel.app)

![Parcel](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fparcel.png&w=48&q=75)

### Parcel

Parcel is a zero configuration build tool for the web that scales to projects of any size and complexity.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/parcel)[View Demo](https://parcel-template.vercel.app)

![Polymer](https://api-frameworks.vercel.sh/framework-logos/polymer.svg)

### Polymer

Polymer is an open-source webapps library from Google, for building using Web Components.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/polymer)[View Demo](https://polymer-template.vercel.app)

![Preact](https://api-frameworks.vercel.sh/framework-logos/preact.svg)

### Preact

Preact is a fast 3kB alternative to React with the same modern API.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/preact)[View Demo](https://preact-template.vercel.app)

![React Router](https://api-frameworks.vercel.sh/framework-logos/react-router.svg)

### React Router

Declarative routing for React

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/react-router)[View Demo](https://react-router-v7-template.vercel.app)

![RedwoodJS](https://api-frameworks.vercel.sh/framework-logos/redwoodjs.svg)

### RedwoodJS

RedwoodJS is a full-stack framework for the Jamstack.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/redwoodjs)[View Demo](https://redwood-template.vercel.app)

![Remix](https://api-frameworks.vercel.sh/framework-logos/remix-no-shadow.svg)

### Remix

Build Better Websites

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/remix)[View Demo](https://remix-run-template.vercel.app)

![Saber](https://api-frameworks.vercel.sh/framework-logos/saber.svg)

### Saber

Saber is a framework for building static sites in Vue.js that supports data from any source.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/saber)View Demo

![Sanity](https://api-frameworks.vercel.sh/framework-logos/sanity.svg)

### Sanity

The structured content platform.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/sanity)[View Demo](https://sanity-studio-template.vercel.app)

![Sanity (v3)](https://api-frameworks.vercel.sh/framework-logos/sanity.svg)

### Sanity (v3)

The structured content platform.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/sanity-v3)[View Demo](https://sanity-studio-template.vercel.app)

![Scully](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fscullyio-logo.png&w=48&q=75)

### Scully

Scully is a static site generator for Angular.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/scully)[View Demo](https://scully-template.vercel.app)

![SolidStart (v0)](https://api-frameworks.vercel.sh/framework-logos/solid.svg)

### SolidStart (v0)

Simple and performant reactivity for building user interfaces.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/solidstart)[View Demo](https://solid-start-template.vercel.app)

![SolidStart (v1)](https://api-frameworks.vercel.sh/framework-logos/solid.svg)

### SolidStart (v1)

Simple and performant reactivity for building user interfaces.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/solidstart-1)[View Demo](https://solid-start-template.vercel.app)

![Stencil](https://api-frameworks.vercel.sh/framework-logos/stencil.svg)

### Stencil

Stencil is a powerful toolchain for building Progressive Web Apps and Design Systems.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/stencil)[View Demo](https://stencil.vercel.app)

![Storybook](https://api-frameworks.vercel.sh/framework-logos/storybook.svg)

### Storybook

Frontend workshop for UI development

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/storybook)View Demo

![SvelteKit](https://api-frameworks.vercel.sh/framework-logos/svelte.svg)

### SvelteKit

SvelteKit is a framework for building web applications of all sizes.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/sveltekit-1)[View Demo](https://sveltekit-1-template.vercel.app)

![TanStack Start](https://api-frameworks.vercel.sh/framework-logos/tanstack-start.svg)![TanStack Start](https://api-frameworks.vercel.sh/framework-logos/tanstack-start-dark.svg)

### TanStack Start

Full-stack Framework powered by TanStack Router for React and Solid.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/tanstack-start)View Demo

![UmiJS](https://api-frameworks.vercel.sh/framework-logos/umi.svg)

### UmiJS

UmiJS is an extensible enterprise-level React application framework.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/umijs)[View Demo](https://umijs-template.vercel.app)

![Vite](https://api-frameworks.vercel.sh/framework-logos/vite.svg)

### Vite

Vite is a new breed of frontend build tool that significantly improves the frontend development experience.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/vite)[View Demo](https://vite-vue-template.vercel.app)

![VitePress](https://api-frameworks.vercel.sh/framework-logos/vite.svg)

### VitePress

VitePress is VuePress' little brother, built on top of Vite.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/vitepress)[View Demo](https://vitepress-starter-template.vercel.app)

![Vue.js](https://api-frameworks.vercel.sh/framework-logos/vue.svg)

### Vue.js

Vue.js is a versatile JavaScript framework that is as approachable as it is performant.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/vue)[View Demo](https://vue-template.vercel.app)

![VuePress](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fvuepress.png&w=48&q=75)

### VuePress

Vue-powered Static Site Generator

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/vuepress)[View Demo](https://vuepress-starter-template.vercel.app)

![xmcp](https://api-frameworks.vercel.sh/framework-logos/xmcp.svg)

### xmcp

The MCP framework for building AI-powered tools

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/xmcp)[View Demo](https://xmcp-template.vercel.app/)

![Zola](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fzola.png&w=48&q=75)

### Zola

Everything you need to make a static site engine in one binary.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/zola)[View Demo](https://zola-template.vercel.app)

## [More resources](#more-resources)

Learn more about deploying your preferred framework on Vercel with the following resources:

*   [Next.js on Vercel](/docs/frameworks/nextjs)
*   [SvelteKit on Vercel](/docs/frameworks/sveltekit)
*   [Astro on Vercel](/docs/frameworks/astro)
*   [Nuxt on Vercel](/docs/frameworks/nuxt)

--------------------------------------------------------------------------------
title: "Vercel Functions"
description: "Vercel Functions allow you to run server-side code without managing a server."
last_updated: "null"
source: "https://vercel.com/docs/functions"
--------------------------------------------------------------------------------

# Vercel Functions

Copy page

Ask AI about this page

Last updated October 10, 2025

Vercel Functions lets you run server-side code without managing servers. They adapt automatically to user demand, handle connections to APIs and databases, and offer enhanced concurrency through [fluid compute](/docs/fluid-compute), which is useful for AI workloads or any I/O-bound tasks that require efficient scaling

When you deploy your application, Vercel automatically sets up the tools and optimizations for your chosen [framework](/docs/frameworks). It ensures low latency by routing traffic through Vercel's [CDN](/docs/cdn), and placing your functions in a specific region when you need more control over [data locality](/docs/functions#functions-and-your-data-source).

![Functions location within Vercel's managed infrastructure](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-functions%2Ffirst_image_light.png&w=3840&q=75)![Functions location within Vercel's managed infrastructure](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Fvercel-functions%2Ffirst_image_dark.png&w=3840&q=75)

Functions location within Vercel's managed infrastructure

## [Getting started](#getting-started)

To get started with creating your first function, copy the code below:

While using `fetch` is the recommended way to create a Vercel Function, you can still use HTTP methods like `GET` and `POST`.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/hello/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

To learn more, see the [quickstart](/docs/functions/quickstart) or [deploy a template](/templates).

## [Functions lifecycle](#functions-lifecycle)

Vercel Functions run in a single [region](/docs/functions/configuring-functions/region) by default, although you can configure them to run in multiple regions if you have globally replicated data. These functions let you add extra capabilities to your application, such as handling authentication, streaming data, or querying databases.

When a user sends a request to your site, Vercel can automatically run a function based on your application code. You do not need to manage servers, or handle scaling.

Vercel creates a new function invocation for each incoming request. If another request arrives soon after the previous one, Vercel [reuses the same function](/docs/fluid-compute#optimized-concurrency) instance to optimize performance and cost efficiency. Over time, Vercel only keeps as many active functions as needed to handle your traffic. Vercel scales your functions down to zero when there are no incoming requests.

By allowing concurrent execution within the same instance (and so using idle time for compute), fluid compute reduces cold starts, lowers latency, and saves on compute costs. It also prevents the need to spin up multiple isolated instances when tasks spend most of their time waiting for external operations.

### [Functions and your data source](#functions-and-your-data-source)

Functions should always execute close to where your data source is to reduce latency. By default, functions using the Node.js runtime execute in Washington, D.C., USA (`iad1`), a common location for external data sources. You can set a new region through your [project's settings on Vercel](/docs/functions/configuring-functions/region#setting-your-default-region).

## [Viewing Vercel Function metrics](#viewing-vercel-function-metrics)

You can view various performance and cost efficiency metrics using Vercel Observability:

1.  Choose your project from the [dashboard](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D&title=Go+to+dashboard).
2.  Click on the Observability tab and select the Vercel Functions section.
3.  Click on the chevron icon to expand and see all charts.

From here, you'll be able to see total consumed and saved GB-Hours, and the ratio of the saved usage. When you have [fluid](/docs/fluid-compute) enabled, you will also see the amount of cost savings from the [optimized concurrency model](/docs/fluid-compute#optimized-concurrency).

## [Pricing](#pricing)

Vercel Functions are priced based on active CPU, provisioned memory, and invocations. See the [fluid compute pricing](/docs/functions/usage-and-pricing) documentation for more information.

If your project is not using fluid compute, see the [legacy pricing documentation](/docs/functions/usage-and-pricing/legacy-pricing) for Vercel Functions.

## [Related](#related)

*   [What is compute?](/docs/fundamentals/what-is-compute)
*   [What is streaming?](/docs/fundamentals/what-is-streaming)
*   [Fluid compute](/docs/fluid-compute)
*   [Runtimes](/docs/functions/runtimes)
*   [Configuring functions](/docs/functions/configuring-functions)
*   [Streaming](/docs/functions/streaming-functions)
*   [Limits](/docs/functions/limitations)
*   [Functions logs](/docs/functions/logs)

--------------------------------------------------------------------------------
title: "Concurrency scaling"
description: "Learn how Vercel automatically scales your functions to handle traffic surges."
last_updated: "null"
source: "https://vercel.com/docs/functions/concurrency-scaling"
--------------------------------------------------------------------------------

# Concurrency scaling

Copy page

Ask AI about this page

Last updated September 5, 2025

Vercel automatically scales your functions to handle traffic surges, ensuring optimal performance during increased loads.

## [Automatic concurrency scaling](#automatic-concurrency-scaling)

The concurrency model on Vercel refers to how many instances of your [functions](/docs/functions) can run simultaneously. All functions on Vercel scale automatically based on demand to manage increased traffic loads.

With automatic concurrency scaling, your Vercel Functions can scale to a maximum of 30,000 on Pro or 100,000 on Enterprise, maintaining optimal performance during traffic surges. The scaling is based on the [burst concurrency limit](#burst-concurrency-limits) of 1000 concurrent executions per 10 seconds, per region. Additionally, Enterprise customers can purchase extended concurrency.

Vercel's infrastructure monitors your usage and preemptively adjusts the concurrency limit to cater to growing traffic, allowing your applications to scale without your intervention.

Automatic concurrency scaling is available on [all plans](/docs/plans).

## [Burst concurrency limits](#burst-concurrency-limits)

Burst concurrency refers to Vercel's ability to temporarily handle a sudden influx of traffic by allowing a higher concurrency limit.

Upon detecting a traffic spike, Vercel temporarily increases the concurrency limit to accommodate the additional load. The initial increase allows for a maximum of 1000 concurrent executions per 10 seconds. After the traffic burst subsides, the concurrency limit gradually returns to its previous state, ensuring a smooth scaling experience.

The scaling process may take several minutes during traffic surges, especially substantial ones. While this delay aligns with natural traffic curves to minimize potential impact on your application's performance, it's advisable to monitor the scaling process for optimal operation.

You can monitor burst concurrency events using [Log Drains](/docs/drains), or [Runtime Logs](/docs/runtime-logs) to help you understand and optimize your application's performance.

If you exceed the limit, a [`503 FUNCTION_THROTTLED`](/docs/errors/FUNCTION_THROTTLED) error will trigger.

--------------------------------------------------------------------------------
title: "Configuring Functions"
description: "Learn how to configure the runtime, region, maximum duration, and memory for Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions"
--------------------------------------------------------------------------------

# Configuring Functions

Copy page

Ask AI about this page

Last updated June 25, 2025

You can configure Vercel functions in many ways, including the runtime, region, maximum duration, and memory.

With different configurations, particularly the runtime configuration, there are a number of trade-offs and limits that you should be aware of. For more information, see the [runtimes](/docs/functions/runtimes) comparison.

## [Runtime](#runtime)

The runtime you select for your function determines the infrastructure, APIs, and other abilities of your function.

With Vercel, you can configure the runtime of a function in any of the following ways:

*   Node.js: When working with a TypeScript or JavaScript function, you can use the Node.js runtime by setting a config option within the function. For more information, see the [runtimes](/docs/functions/runtimes).
*   Ruby, Python, Go: These have similar functionality and limitations as Node.js functions. The configuration for these runtimes gets based on the file extension.
*   Community runtimes: You can specify any other [runtime](/docs/functions/runtimes#community-runtimes), by using the [`functions`](/docs/project-configuration#functions) property in your `vercel.json` file.

See [choosing a runtime](/docs/functions/runtimes) for more information.

## [Region](#region)

Your function should execute in a location close to your data source. This minimizes latency, or delay, thereby enhancing your app's performance. How you configure your function's region, depends on the runtime used.

See [configuring a function's region](/docs/functions/configuring-functions/region) for more information.

## [Maximum duration](#maximum-duration)

The maximum duration for your function defines how long a function can run for, allowing for more predictable billing.

Vercel Functions have a default duration that's dependent on your plan, but you can configure this as needed, [up to your plan's limit](/docs/functions/limitations#max-duration).

See [configuring a function's duration](/docs/functions/configuring-functions/duration) for more information.

## [Memory](#memory)

Vercel Functions use an infrastructure that allows you to adjust the memory size.

See [configuring a function's memory](/docs/functions/configuring-functions/memory) for more information.

--------------------------------------------------------------------------------
title: "Advanced Configuration"
description: "Learn how to add utility files to the /api directory, and bundle Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions/advanced-configuration"
--------------------------------------------------------------------------------

# Advanced Configuration

Copy page

Ask AI about this page

Last updated May 21, 2025

For an advanced configuration, you can create a `vercel.json` file to use [Runtimes](/docs/functions/runtimes) and other customizations. To view more about the properties you can customize, see the [Configuring Functions](/docs/functions/configuring-functions) and [Project config with vercel.json](/docs/project-configuration).

If your use case requires that you work asynchronously with the results of a function invocation, you may need to consider a queuing, pooling, or [streaming](/docs/functions/streaming-functions) approach because of how functions are created on Vercel.

## [Adding utility files to the `/api` directory](#adding-utility-files-to-the-/api-directory)

Sometimes, you need to place extra code files, such as `utils.js` or `my-types.d.ts`, inside the `/api` folder. To avoid turning these files into functions, Vercel ignores files with the following characters:

*   Files that start with an underscore, `_`
*   Files that start with `.`
*   Files that end with `.d.ts`

If your file uses any of the above, it will not be turned into a function.

## [Bundling Vercel Functions](#bundling-vercel-functions)

In order to optimize resources, Vercel uses a process to bundle as many routes as possible into a single Vercel Function.

To provide more control over the bundling process, you can use the [`functions` property](/docs/project-configuration#functions) in your `vercel.json` file to define the configuration for a route. If a configuration is present, Vercel will bundle functions based on the configuration first. Vercel will then bundle together the remaining routes, optimizing for how many functions are created.

This bundling process is currently only enabled for Next.js, but it will be enabled in other scenarios in the future.

In the following example, `app/api/hello/route.ts` will be bundled separately from `app/api/another/route.ts` since each has a different configuration:

Next.js (/app)Next.js (/pages)Other frameworks

vercel.json

TypeScript

TypeScriptJavaScript

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "app/api/hello/route.ts": {
      "memory": 3009,
      "maxDuration": 60
    },
    "app/api/another/route.ts": {
      "memory": 1024,
      "maxDuration": 30
    }
  }
}
```

--------------------------------------------------------------------------------
title: "Configuring Maximum Duration for Vercel Functions"
description: "Learn how to set the maximum duration of a Vercel Function."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions/duration"
--------------------------------------------------------------------------------

# Configuring Maximum Duration for Vercel Functions

Copy page

Ask AI about this page

Last updated October 9, 2025

The maximum duration configuration determines the longest time that a function can run. This guide will walk you through configuring the maximum duration for your Vercel Functions.

## [Consequences of changing the maximum duration](#consequences-of-changing-the-maximum-duration)

You are charged based on the amount of time your function has run, also known as its _duration_. It specifically refers to the _actual time_ elapsed during the entire invocation, regardless of whether that time was actively used for processing or spent waiting for a streamed response. To learn more see [Managing function duration](/docs/functions/usage-and-pricing#managing-function-duration).

For this reason, Vercel has set a [default maximum duration](/docs/functions/limitations#max-duration) for functions, which can be useful for preventing runaway functions from consuming resources indefinitely.

If a function runs for longer than its set maximum duration, Vercel will terminate it. Therefore, when setting this duration, it's crucial to strike a balance:

1.  Allow sufficient time for your function to complete its normal operations, including any necessary waiting periods (for example, streamed responses).
2.  Set a reasonable limit to prevent abnormally long executions.

## [Maximum duration for different runtimes](#maximum-duration-for-different-runtimes)

The method of configuring the maximum duration depends on your framework and runtime:

#### [Node.js, Next.js (>= 13.5 or higher), SvelteKit, Astro, Nuxt, and Remix](#node.js-next.js->=-13.5-or-higher-sveltekit-astro-nuxt-and-remix)

For these runtimes / frameworks, you can configure the number of seconds directly in your function:

app/api/my-function/route.ts

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixAstroOther frameworks

TypeScript

TypeScriptJavaScript

```
export const maxDuration = 5; // This function can run for a maximum of 5 seconds
 
export function GET(request: Request) {
  return new Response('Vercel', {
    status: 200,
  });
}
```

#### [Other Frameworks and runtimes, Next.js versions older than 13.5, Go, Python, or Ruby](#other-frameworks-and-runtimes-next.js-versions-older-than-13.5-go-python-or-ruby)

For these runtimes and frameworks, configure the `maxDuration` property of the [`functions` object](/docs/project-configuration#functions) in your `vercel.json` file:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/test.js": {
      "maxDuration": 30 // This function can run for a maximum of 30 seconds
    },
    "api/*.js": {
      "maxDuration": 15 // This function can run for a maximum of 15 seconds
    },
    "src/api/*.js": {
      "maxDuration": 25 // You must prefix functions in the src directory with /src/
    }
  }
}
```

If your Next.js project is configured to use [src directory](https://nextjs.org/docs/app/building-your-application/configuring/src-directory), you will need to prefix your function routes with `/src/` for them to be detected.

The order in which you specify file patterns is important. For more information, see [Glob pattern](/docs/project-configuration#glob-pattern-order).

## [Setting a default maximum duration](#setting-a-default-maximum-duration)

While Vercel specifies [defaults](/docs/functions/limitations#max-duration) for the maximum duration of a function, you can also override it in the following ways:

### [Dashboard](#dashboard)

1.  From your [dashboard](/dashboard), select your project and go to the Settings tab.
2.  From the left side, select the Functions tab and scroll to the Function Max Duration section.
3.  Update the Default Max Duration field value and select Save.

### [`vercel.json` file](#vercel.json-file)

vercel.json

Next.js (/app)

Next.js (/app)Next.js (/pages)SvelteKitNuxtRemixAstroOther frameworks

TypeScript

TypeScriptJavaScript

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "app/api/**/*": {
      "maxDuration": 5
    }
  }
}
```

This glob pattern will match _everything_ in the specified path, so you may wish to be more specific by adding a file type, such as `app/api/**/*.ts` instead.

## [Duration limits](#duration-limits)

Vercel Functions have the following defaults and maximum limits for the duration of a function with [fluid compute](/docs/fluid-compute) (enabled by default):

|  | Default | Maximum |
| --- | --- | --- |
| Hobby | 300s (5 minutes) | 300s (5 minutes) |
| Pro | 300s (5 minutes) | 800s (13 minutes) |
| Enterprise | 300s (5 minutes) | 800s (13 minutes) |

If you have disabled fluid compute, the following defaults and maximum limits apply:

|  | Default | Maximum |
| --- | --- | --- |
| Hobby | 10s | 60s (1 minute) |
| Pro | 15s | 300s (5 minutes) |
| Enterprise | 15s | 900s (15 minutes) |

--------------------------------------------------------------------------------
title: "Configuring Memory and CPU for Vercel Functions"
description: "Learn how to set the memory / CPU of a Vercel Function."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions/memory"
--------------------------------------------------------------------------------

# Configuring Memory and CPU for Vercel Functions

Copy page

Ask AI about this page

Last updated September 24, 2025

The memory configuration of a function determines how much memory and CPU a function can use while executing. By default, on Pro and Enterprise, functions execute with 2 GB (1 vCPU) of memory. On Hobby, they will always execute with 2 GB (1 vCPU). You can change the [default memory size for all functions](#setting-your-default-function-memory-/-cpu-size) in a project.

## [Memory configuration considerations](#memory-configuration-considerations)

You should consider the following points when changing the memory size of your functions:

*   Performance: Increasing memory size can improve the performance of your functions, allowing them to run faster
*   Cost: Vercel Functions are billed based on the function duration, which is affected by the memory size. While increasing the function CPU can increase costs if the function duration stays the same, the increase in CPU can also make functions execute faster. If your function executes faster, it is possible for it to incur less overall function duration usage. This is especially important if your function runs CPU-intensive tasks. See [Pricing](#pricing) for more information on how function duration is calculated

## [Setting your default function memory / CPU size](#setting-your-default-function-memory-/-cpu-size)

Those on the Pro or Enterprise plans can configure the default memory size for all functions in a project.

To change the default function memory size:

1.  Choose the appropriate project from your [dashboard](/dashboard)
2.  Navigate to the Settings tab
3.  Scroll to Functions
4.  Select Advanced Settings
5.  In the Function CPU section, select your preferred memory size option:
    
    ![The Function CPU setting in a Vercel project's dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fconfigure-mem-light.png&w=1920&q=75)![The Function CPU setting in a Vercel project's dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fconfigure-mem-dark.png&w=1920&q=75)
    
    The Function CPU setting in a Vercel project's dashboard
    
6.  The change will be applied to all future deployments made by your team. You must create a new deployment for your changes to take effect

You cannot set your memory size using `vercel.json`. If you try to do so, you will receive a warning at build time. Only Pro and Enterprise users can set the default memory size in the dashboard. Hobby users will always use the default memory size of 2 GB (1 vCPU).

### [Memory / CPU type](#memory-/-cpu-type)

The memory size you select will also determine the CPU allocated to your Vercel Functions. The following table shows the memory and CPU allocation for each type.

With [fluid compute enabled](/docs/fluid-compute) on Pro and Enterprise plans, the default memory size is 2 GB (1 vCPU) and can be upgraded to 4 GB / 2 vCPUs, for Hobby users, Vercel manages the CPU with a minimum of 1 vCPU.

| Type | Memory / CPU | Use |
| --- | --- | --- |
| Standard
Default

 | 2 GB / 1 vCPU | Predictable performance for production workloads. Default for [fluid compute](/docs/fluid-compute). |
| Performance | 4 GB / 2 vCPUs | Increased performance for latency-sensitive applications and SSR workloads. |

Users on the Hobby plan can only use the default memory size of 2 GB (1 vCPU). Hobby users cannot configure this size. If you are on the Hobby plan, and have enabled fluid compute, the memory size will be managed by Vercel with a minimum of 1 vCPU.

Project created before 2019-11-08 have the default function memory size set to 1024 MB/0.6 vCPU for Hobby plan, and 3008 MB/1.67 vCPU for Pro and Enterprise plan. Although the dashboard may not have any memory size option selected by default for those projects, you can start using the new memory size options by selecting your preferred memory size in the dashboard.

## [Viewing your function memory size](#viewing-your-function-memory-size)

To check the memory size of your functions in the [dashboard](/dashboard), follow these steps:

1.  Find the project you want to review and select the Deployments tab
2.  Go to the deployment you want to review
3.  Select the Resources tab
4.  Search for the function by name or find it in the Functions section
5.  Click on the name of the function to open it in Observability
6.  Hover over the information icon next to the function name to view its memory size

## [Memory limits](#memory-limits)

To learn more about the maximum size of your function's memory, see [Max memory size](/docs/functions/limitations#memory-size-limits).

## [Pricing](#pricing)

While memory / CPU size is not an explicitly billed metric, it is fundamental in how the billed metric of [Function Duration](/docs/functions/usage-and-pricing#managing-function-duration) is calculated.

Legacy Billing Model: This describes the legacy Function duration billing model based on wall-clock time. For new projects, we recommend [Fluid Compute](/docs/functions/usage-and-pricing) which bills separately for active CPU time and provisioned memory time for more cost-effective and transparent pricing.

You are charged based on the duration your Vercel functions have run. This is sometimes called "[wall-clock time](/guides/what-are-gb-hrs-for-serverless-function-execution)", which refers to the _actual time_ elapsed during a process, similar to how you would measure time passing on a wall clock. It includes all time spent from start to finish of the process, regardless of whether that time was actively used for processing or spent waiting for a streamed response. Function Duration is calculated in [GB-Hours](/guides/what-are-gb-hrs-for-serverless-function-execution), which is the memory allocated for each Function in GB x the time in hours they were running.

For example, if a function [has](/docs/functions/configuring-functions/memory) 1.7 GB (1769 MB) of memory and is executed 1 million times at a 1-second duration:

*   Total Seconds: 1M \* (1s) = 1,000,000 Seconds
*   Total GB-Seconds: 1769/1024 GB \* 1,000,000 Seconds = 1,727,539.06 GB-Seconds
*   Total GB-Hrs: 1,727,539.06 GB-Seconds / 3600 = 479.87 GB-Hrs
*   The total Vercel Function Execution is 479.87 GB-Hrs.

To see your current usage, navigate to the Usage tab on your team's [Dashboard](/dashboard) and go to Serverless Functions > Duration. You can use the Ratio option to see the total amount of execution time across all projects within your team, including the completions, errors, and timeouts.

You can also view [Invocations](/docs/functions/usage-and-pricing#managing-function-invocations) to see the number of times your Functions have been invoked. To learn more about the cost of Vercel Functions, see [Vercel Function Pricing](/docs/pricing/serverless-functions).

--------------------------------------------------------------------------------
title: "Configuring regions for Vercel Functions"
description: "Learn how to configure regions for Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions/region"
--------------------------------------------------------------------------------

# Configuring regions for Vercel Functions

Copy page

Ask AI about this page

Last updated September 15, 2025

The Vercel platform caches all static content at [the edge](/docs/edge-cache) by default. This means your users will always get static files like HTML, CSS, and JavaScript served from servers that are closest to them. See the [regions](/docs/regions) page for a full list of our regions.

In a globally distributed application, the physical distance between your function and its data source can impact latency and response times. Therefore, Vercel allows you to specify the region in which your functions execute, ideally close to your data source (such as your [database](/guides/using-databases-with-vercel)).

*   By default, Vercel Functions execute in [_Washington, D.C., USA_ (`iad1`)](/docs/pricing/regional-pricing/iad1) for all new projects to ensure they are located close to most external data sources, which are hosted on the East Coast of the USA. You can set a new default region through your [project's settings on Vercel](#setting-your-default-region)
*   You can define the region in your `vercel.json` using the [`regions` setting](/docs/functions/configuring-functions/region#project-configuration)
*   You can set your region in the [Vercel CLI](#vercel-cli)

## [Setting your default region](#setting-your-default-region)

The default Function region is [_Washington, D.C., USA_ (`iad1`)](/docs/pricing/regional-pricing/iad1) for all new projects.

### [Dashboard](#dashboard)

To change the default regions in the dashboard:

1.  Choose the appropriate project from your [dashboard](/dashboard) on Vercel
2.  Navigate to the Settings tab
3.  From the left side, select Functions
4.  Use the Function Regions accordion to select your project's default regions:
    
    ![The Function Regions setting in a Vercel project's dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fregions%2Ffunction-regions-selection-light.png&w=1920&q=75)![The Function Regions setting in a Vercel project's dashboard](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fedge-network%2Fregions%2Ffunction-regions-selection-dark.png&w=1920&q=75)
    
    The Function Regions setting in a Vercel project's dashboard
    

### [Project configuration](#project-configuration)

To change the default region in your `vercel.json` [configuration file](/docs/project-configuration#regions), add the region code(s) to the `"regions"` key:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "regions": ["sfo1"]
}
```

Additionally, Pro and Enterprise users can deploy Vercel Functions to multiple regions: Pro users can deploy to up to three regions, and Enterprise users can deploy to unlimited regions. To learn more, see [location limits](/docs/functions/runtimes#location).

Enterprise users can also use [`functionFailoverRegions`](/docs/project-configuration#functionfailoverregions) to specify regions that a Vercel Function should failover to if the default region is out of service.

### [Vercel CLI](#vercel-cli)

Use the `vercel --regions` command in your project's root directory to set a region. Learn more about setting regions with the `vercel --regions` command in the [CLI docs](/docs/cli/deploy#regions).

## [Available regions](#available-regions)

To learn more about the regions that you can set for your Functions, see the [region list](/docs/regions#region-list).

## [Automatic failover](#automatic-failover)

Vercel Functions have multiple availability zone redundancy by default. Multi-region redundancy is available depending on your runtime.

### [Node.js runtime failover](#node.js-runtime-failover)

Setting failover regions are available on [Enterprise plans](/docs/plans/enterprise)

Enterprise teams can enable multi-region redundancy for Vercel Functions using Node.js.

To automatically failover to closest region in the event of an outage:

1.  Select your project from your team's [dashboard](/dashboard)
2.  Navigate to the Settings tab and select Functions
3.  Enable the Function Failover toggle:
    
    ![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Ffunction-failover-light.png&w=1920&q=75)![](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Ffunction-failover-dark.png&w=1920&q=75)
    

To manually specify the fallback region, you can pass one or more regions to the [`functionFailoverRegions`](/docs/project-configuration#functionfailoverregions) property in your `vercel.json` file:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functionFailoverRegions": ["dub1", "fra1"]
}
```

The region(s) set in the `functionFailoverRegions` property must be different from the default region(s) specified in the [`regions`](/docs/project-configuration#regions) property.

During an automatic failover, Vercel will reroute application traffic to the next closest region, meaning the order of the regions in `functionFailoverRegions` does not matter. For more information on how failover routing works, see [`functionFailoverRegions`](/docs/project-configuration#functionfailoverregions).

You can view your default and failover regions through the [deployment summary](/docs/deployments#resources-tab-and-deployment-summary):

![Failover regions for your Vercel functions shown in the deployment summary.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Ffunction-failover-region-light.png&w=3840&q=75)![Failover regions for your Vercel functions shown in the deployment summary.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Ffunction-failover-region-dark.png&w=3840&q=75)

Failover regions for your Vercel functions shown in the deployment summary.

Region failover is supported with Secure Compute. See [Region Failover](/docs/secure-compute#region-failover) to learn more.

--------------------------------------------------------------------------------
title: "Configuring the Runtime for Vercel Functions"
description: "Learn how to configure the runtime for Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/configuring-functions/runtime"
--------------------------------------------------------------------------------

# Configuring the Runtime for Vercel Functions

Copy page

Ask AI about this page

Last updated May 21, 2025

The runtime of your function determines the environment in which your function will execute. Vercel supports various runtimes including Node.js, Python, Ruby, and Go. You can also configure [other runtimes](/docs/functions/runtimes#community-runtimes) using the `vercel.json` file. Here's how to set up each:

## [Node.js](#node.js)

By default, a function with no additional configuration will be deployed as a Vercel Function on the Node.js runtime.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/hello/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

## [Go](#go)

For Go, expose a single HTTP handler from a `.go` file within an `/api` directory at your project's root. For example:

/api/index.go

```
package handler
 
import (
  "fmt"
  "net/http"
)
 
func Handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "<h1>Hello from Go!</h1>")
}
```

## [Python](#python)

For Python, create a function by adding the following code to `api/index.py`:

api/index.py

```
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
```

## [Ruby](#ruby)

For Ruby, define an HTTP handler from `.rb` files within an `/api` directory at your project's root. Ruby files must have one of the following variables defined:

*   `Handler` proc that matches the `do |request, response|` signature
*   `Handler` class that inherits from the `WEBrick::HTTPServlet::AbstractServlet` class

For example:

api/index.rb

```
require 'cowsay'
 
Handler = Proc.new do |request, response|
  name = request.query['name'] || 'World'
 
  response.status = 200
  response['Content-Type'] = 'text/text; charset=utf-8'
  response.body = Cowsay.say("Hello #{name}", 'cow')
end
```

Don't forget to define your dependencies inside a `Gemfile`:

Gemfile

```
source "https://rubygems.org"
 
gem "cowsay", "~> 0.3.0"
```

## [Other runtimes](#other-runtimes)

You can configure other runtimes by using the `functions` property in your `vercel.json` file. For example:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/test.php": {
      "runtime": "vercel-php@0.5.2"
    }
  }
}
```

In this case, the function at `api/hello.ts` would use the custom runtime specified.

For more information, see [Community runtimes](/docs/functions/runtimes#community-runtimes)

--------------------------------------------------------------------------------
title: "Functions API Reference"
description: "Learn about available APIs when working with Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/functions-api-reference"
--------------------------------------------------------------------------------

# Functions API Reference

Copy page

Ask AI about this page

Last updated October 27, 2025

Functions are defined similar to a [Route Handler](https://nextjs.org/docs/app/building-your-application/routing/route-handlers) in Next.js. When using Next.js App Router, you can define a function in a file under `app/api/my-route/route.ts` in your project. Vercel will deploy any file under `app/api/` as a function.

## [Function signature](#function-signature)

Vercel Functions use a Web Handler, which consists of the `request` parameter that is an instance of the web standard [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) API. Next.js [extends](https://nextjs.org/docs/app/api-reference/functions/next-request) the standard `Request` object with additional properties and methods.

| Parameter | Description | Next.js | Other Frameworks |
| --- | --- | --- | --- |
| `request` | An instance of the `Request` object | [`NextRequest`](https://nextjs.org/docs/api-reference/next/server#nextrequest) | [`Request`](https://developer.mozilla.org/docs/Web/API/Request) |
| `context` | Deprecated, use [`@vercel/functions`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil) instead | N/A | [`{ waitUntil }`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil) |

Next.js (/app)Next.js (/pages)Other frameworks

app/api/hello/route.ts

TypeScript

TypeScriptJavaScript

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

### [Cancel requests](#cancel-requests)

This feature is only available in the Node.js runtime.

Cancelling requests is useful for cleaning up resources or stopping long-running tasks when the client aborts the request — for example, when a user hits stop on an AI chat or they close a browser tab.

To cancel requests in Vercel Functions

1.  In your `vercel.json` file, add `"supportsCancellation": true` to the [specific paths](/docs/project-configuration#key-definition) you want to opt-in to cancellation for your functions. For example, to enable everything, use `**/*` as the glob or `app/**/*` for app router:
    
    vercel.json
    
    ```
    {
      "regions": ["iad1"],
      "functions": {
        "api/*": {
          "supportsCancellation": true
        }
      }
    }
    ```
    
    When you have enabled cancellation, anything that must be completed in the event of request cancellation should be put in a `waitUntil` or `after` promise. If you don't, there is no guarantee that code will be executed after the request is cancelled.
    
2.  Use the `AbortController` API in your function to cancel the request. This will allow you to clean up resources or stop long-running tasks when the client aborts the request:
    
    api/abort-controller/route.ts
    
    ```
    export async function GET(request: Request) {
      const abortController = new AbortController();
     
      request.signal.addEventListener('abort', () => {
        console.log('request aborted');
        abortController.abort();
      });
     
      const response = await fetch('https://my-backend-service.example.com', {
        headers: {
          Authorization: `Bearer ${process.env.AUTH_TOKEN}`,
        },
        signal: abortController.signal,
      });
     
      return new Response(response.body, {
        status: response.status,
        headers: response.headers,
      });
    }
    ```
    

## [Route segment config](#route-segment-config)

To configure your function when using the App Router in Next.js, you use [segment options](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config), rather than a `config` object.

app/api/example/route.ts

TypeScript

TypeScriptJavaScript

```
export const runtime = 'nodejs';
export const maxDuration = 15;
```

The table below shows a highlight of the valid config options. For detailed information on all the config options, see the [Configuring Functions](/docs/functions/configuring-functions) docs.

| Property | Type | Description |
| --- | --- | --- |
| [`runtime`](/docs/functions/configuring-functions/runtime) | `string` | This optional property defines the runtime to use, and if not set the runtime will default to `nodejs`. |
| [`preferredRegion`](/docs/functions/configuring-functions/region) | `string` | This optional property and can be used to specify the [regions](/docs/regions#region-list) in which your function should execute. This can only be set when the `runtime` is set to `edge` |
| [`maxDuration`](/docs/functions/configuring-functions/duration) | `int` | This optional property can be used to specify the maximum duration in seconds that your function can run for. This can't be set when the `runtime` is set to `edge` |

## [`SIGTERM` signal](#sigterm-signal)

This feature is supported on the Node.js and Python runtimes.

A `SIGTERM` signal is sent to a function when it is about to be terminated, such as during scale-down events. This allows you to perform any necessary cleanup operations before the function instance is terminated.

Your code can run for up to 500 milliseconds after receiving a `SIGTERM` signal. After this period, the function instance will be terminated immediately.

api/hello.ts

TypeScript

TypeScriptJavaScript

```
process.on('SIGTERM', () => {
  // Perform cleanup operations here
});
```

## [The `@vercel/functions` package](#the-@vercel/functions-package)

The `@vercel/functions` package provides a set of helper methods and utilities for working with Vercel Functions.

### [Helper methods](#helper-methods)

*   [`waitUntil()`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil): This method allows you to extend the lifetime of a request handler for the duration of a given Promise . It's useful for tasks that can be performed after the response is sent, such as logging or updating a cache.
*   [`getEnv`](/docs/functions/functions-api-reference/vercel-functions-package#getenv): This function retrieves System Environment Variables exposed by Vercel.
*   [`geolocation()`](/docs/functions/functions-api-reference/vercel-functions-package#geolocation): Returns location information for the incoming request, including details like city, country, and coordinates.
*   [`ipAddress()`](/docs/functions/functions-api-reference/vercel-functions-package#ipaddress): Extracts the IP address of the request from the headers.
*   [`invalidateByTag()`](/docs/functions/functions-api-reference/vercel-functions-package#invalidatebytag): Marks a cache tag as stale, causing cache entries associated with that tag to be revalidated in the background on the next request.
*   [`dangerouslyDeleteByTag()`](/docs/functions/functions-api-reference/vercel-functions-package#dangerouslydeletebytag): Marks a cache tag as deleted, causing cache entries associated with that tag to be revalidated in the foreground on the next request.
*   [`getCache()`](/docs/functions/functions-api-reference/vercel-functions-package#getcache): Obtain a [`RuntimeCache`](/docs/functions/functions-api-reference/vercel-functions-package#getcache) object to interact with the [Vercel Data Cache](/docs/data-cache).

See the [`@vercel/functions`](/docs/functions/functions-api-reference/vercel-functions-package) documentation for more information.

## [The `@vercel/oidc` package](#the-@vercel/oidc-package)

The `@vercel/oidc` package was previously provided by `@vercel/functions/oidc`.

The `@vercel/oidc` package provides helper methods and utilities for working with OpenID Connect (OIDC) tokens.

### [OIDC Helper methods](#oidc-helper-methods)

*   [`getVercelOidcToken()`](/docs/functions/functions-api-reference/vercel-functions-package#getverceloidctoken): Retrieves the OIDC token from the request context or environment variable.

See the [`@vercel/oidc`](/docs/functions/functions-api-reference/vercel-functions-package) documentation for more information.

## [The `@vercel/oidc-aws-credentials-provider` package](#the-@vercel/oidc-aws-credentials-provider-package)

The `@vercel/oidc-aws-credentials-provider` package was previously provided by `@vercel/functions/oidc`.

The `@vercel/oidc-aws-credentials-provider` package provides helper methods and utilities for working with OpenID Connect (OIDC) tokens and AWS credentials.

### [AWS Helper methods](#aws-helper-methods)

*   [`awsCredentialsProvider()`](/docs/functions/functions-api-reference/vercel-functions-package#awscredentialsprovider): This function helps in obtaining AWS credentials using Vercel's OIDC token.

See the [`@vercel/oidc-aws-credentials-provider`](/docs/functions/functions-api-reference/vercel-functions-package) documentation for more information.

## [More resources](#more-resources)

*   [Streaming Data: Learn about streaming on Vercel](/docs/functions/streaming)

--------------------------------------------------------------------------------
title: "@vercel/functions API Reference (Node.js)"
description: "Learn about available APIs when working with Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/functions-api-reference/vercel-functions-package"
--------------------------------------------------------------------------------

# @vercel/functions API Reference (Node.js)

Copy page

Ask AI about this page

Last updated October 23, 2025

## [Install and use the package](#install-and-use-the-package)

1.  Install the `@vercel/functions` package:

pnpmyarnnpmbun

```
pnpm i @vercel/functions
```

1.  Import the `@vercel/functions` package (non-Next.js frameworks or Next.js versions below 15.1):

Other frameworks

api/hello.ts

TypeScript

TypeScriptJavaScript

```
import { waitUntil, attachDatabasePool } from '@vercel/functions';
 
export default {
  fetch(request: Request) {
    // ...
  },
};
```

For [OIDC](/docs/functions/functions-api-reference/vercel-functions-package#oidc-methods) methods, import `@vercel/oidc`

## [Usage with Next.js](#usage-with-next.js)

If you’re using Next.js 15.1 or above, we recommend using the built-in [`after()`](https://nextjs.org/docs/app/api-reference/functions/after) function from `next/server` instead of `waitUntil()`.

`after()` allows you to schedule work that runs after the response has been sent or the prerender has completed. This is especially useful to avoid blocking rendering for side effects such as logging, analytics, or other background tasks.

app/api/hello/route.ts

```
import { after } from 'next/server';
 
export async function GET(request: Request) {
  const country = request.headers.get('x-vercel-ip-country') || 'unknown';
 
  // Returns a response immediately
  const response = new Response(`You're visiting from ${country}`);
 
  // Schedule a side-effect after the response is sent
  after(async () => {
    // For example, log or increment analytics in the background
    await fetch(
      `https://my-analytics-service.example.com/log?country=${country}`,
    );
  });
 
  return response;
}
```

*   `after()` does not block the response. The callback runs once rendering or the response is finished.
*   `after()` is not a [Dynamic API](https://nextjs.org/docs/app/building-your-application/rendering/server-components#dynamic-apis); calling it does not cause a route to become dynamic.
*   If you need to configure or extend the timeout for tasks, you can use [`maxDuration`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#maxduration) in Next.js.
*   For more usage examples (including in Server Components, Server Actions, or Middleware), see [after() in the Next.js docs](https://nextjs.org/docs/app/api-reference/functions/after).

## [Helper methods (non-Next.js usage or older Next.js versions)](#helper-methods-non-next.js-usage-or-older-next.js-versions)

If you're not using Next.js 15.1 or above (or you are using other frameworks), you can use the methods from `@vercel/functions` below.

### [`waitUntil`](#waituntil)

Description: Extends the lifetime of the request handler for the lifetime of the given Promise. The `waitUntil()` method enqueues an asynchronous task to be performed during the lifecycle of the request. You can use it for anything that can be done after the response is sent, such as logging, sending analytics, or updating a cache, without blocking the response. `waitUntil()` is available in Node.js and in the [Edge Runtime](/docs/functions/runtimes/edge).

Promises passed to `waitUntil()` will have the same timeout as the function itself. If the function times out, the promises will be cancelled.

| Name | Type | Description |
| --- | --- | --- |
| `promise` | [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) | The promise to wait for. |

If you're using Next.js 15.1 or above, use [`after()`](#using-after-in-nextjs) from `next/server` instead. Otherwise, see below.

api/hello.ts

```
import { waitUntil } from '@vercel/functions';
 
async function getBlog() {
  const res = await fetch('https://my-analytics-service.example.com/blog/1');
  return res.json();
}
 
export default {
  fetch(request: Request) {
    waitUntil(getBlog().then((json) => console.log({ json })));
    return new Response(`Hello from ${request.url}, I'm a Vercel Function!`);
  },
};
```

### [`getEnv`](#getenv)

Description: Gets the [System Environment Variables](/docs/environment-variables/system-environment-variables#system-environment-variables) exposed by Vercel.

api/example.ts

```
import { getEnv } from '@vercel/functions';
 
export default {
  fetch(request) {
    const { VERCEL_REGION } = getEnv();
    return new Response(`Hello from ${VERCEL_REGION}`);
  },
};
```

### [`geolocation`](#geolocation)

Description: Returns the location information for the incoming request, in the following way:

```
{
  "city": "New York",
  "country": "US",
  "flag": "🇺🇸",
  "countryRegion": "NY",
  "region": "iad1",
  "latitude": "40.7128",
  "longitude": "-74.0060",
  "postalCode": "10001"
}
```

| Name | Type | Description |
| --- | --- | --- |
| `request` | [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) | The incoming request object which provides the IP |

api/example.ts

```
import { geolocation } from '@vercel/functions';
 
export default {
  fetch(request) {
    const details = geolocation(request);
    return Response.json(details);
  },
};
```

### [`ipAddress`](#ipaddress)

Description: Returns the IP address of the request from the headers.

| Name | Type | Description |
| --- | --- | --- |
| `request` | [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) | The incoming request object which provides the IP |

api/example.ts

```
import { ipAddress } from '@vercel/functions';
 
export default {
  fetch(request) {
    const ip = ipAddress(request);
    return new Response(`Your ip is ${ip}`);
  },
};
```

### [`invalidateByTag`](#invalidatebytag)

Description: Marks a cache tag as stale, causing cache entries associated with that tag to be revalidated in the background on the next request.

| Name | Type | Description |
| --- | --- | --- |
| `tag` | `string` or `string[]` | The cache tag (or multiple tags) to invalidate. |

api/example.ts

```
import { invalidateByTag } from '@vercel/functions';
 
export default {
  async fetch(request) {
    await invalidateByTag('my-tag-name');
    return new Response('Success');
  },
};
```

### [`dangerouslyDeleteByTag`](#dangerouslydeletebytag)

Description: Marks a cache tag as deleted, causing cache entries associated with that tag to be revalidated in the foreground on the next request. Use this method with caution because one tag can be associated with many paths and deleting the cache can cause many concurrent requests to the origin leading to [cache stampede problem](https://en.wikipedia.org/wiki/Cache_stampede). A good use case for deleting the cache is when the origin has also been deleted, for example it returns a `404` or `410` status code.

| Name | Type | Description |
| --- | --- | --- |
| `tag` | `string` or `string[]` | The cache tag (or multiple tags) to dangerously delete. |
| `options` | `{ revalidationDeadlineSeconds: number }` | The time in seconds before the delete deadline. If a request is made before the deadline, it will revalidate in the background. Otherwise it will be dangerously deleted and revalidate in the foreground. |

api/example.ts

```
import { dangerouslyDeleteByTag } from '@vercel/functions';
 
export default {
  async fetch(request) {
    await dangerouslyDeleteByTag('my-tag-name', {
      revalidationDeadlineSeconds: 10,
    });
    return new Response('Success');
  },
};
```

### [`getCache`](#getcache)

Description: Returns a `RuntimeCache` object that allows you to interact with the Vercel Runtime Cache in any Vercel region. Use this for storing and retrieving data across function, routing middleware, and build execution within a Vercel region.

| Name | Type | Description |
| --- | --- | --- |
| `keyHashFunction` | `(key: string) => string` | Optional custom hash function for generating keys. |
| `namespace` | `String` | Optional namespace to prefix cache keys. |
| `namespaceSeparator` | `String` | Optional separator string for the namespace. |

#### [Specification](#specification)

`RuntimeCache` provides the following methods:

| Method | Description | Parameters |
| --- | --- | --- |
| `get` | Retrieves a value from the Vercel Runtime Cache. | `key: string`: The cache key |
| `set` | Stores a value in the Vercel Runtime Cache with optional `ttl` and/or `tags`. The `name` option allows a human-readable label to be associated with the cache entry for observability purposes. | 
*   `key: string`: The cache key
*   `value: unknown`: The value to store
*   `options?: { name?: string; tags?: string[]; ttl?: number }`  
    Configuration object (not required)

 |
| `delete` | Removes a value from the Vercel Runtime Cache by key | `key: string`: The cache key to delete |
| `expireTag` | Expires all cache entries associated with one or more tags | `tag: string | string[]`: Tag or array of tags to expire |

api/example.ts

```
import { getCache } from '@vercel/functions';
 
export default {
  async fetch(request) {
    const cache = getCache();
 
    // Get a value from cache
    const value = await cache.get('somekey');
 
    if (value) {
      return new Response(JSON.stringify(value));
    }
 
    const res = await fetch('https://api.vercel.app/blog');
    const originValue = await res.json();
 
    // Set a value in cache with TTL and tags
    await cache.set('somekey', originValue, {
      ttl: 3600, // 1 hour in seconds
      tags: ['example-tag'],
    });
 
    return new Response(JSON.stringify(originValue));
  },
};
```

After assigning tags to your cached data, use the `expireTag` method to invalidate all cache entries associated with that tag. This operation is propagated globally across all Vercel regions within 300ms.

app/actions.ts

```
'use server';
 
import { getCache } from '@vercel/functions';
 
export default async function action() {
  await getCache().expireTag('blog');
}
```

#### [Limits and usage](#limits-and-usage)

The Runtime Cache is isolated per Vercel project and deployment environment (`preview` and `production`). Cached data is persisted across deployments and can be invalidated either through time-based expiration or by calling `expireTag`. However, TTL (time-to-live) and tag updates aren't reconciled between deployments. In those cases, we recommend either purging the runtime cache or modifying the cache key.

The Runtime Cache API does not have first class integration with [Incremental Static Regeneration](/docs/incremental-static-regeneration). This means that:

*   Runtime Cache entry tags will not apply to ISR pages, so you cannot use expireTag to invalidate both caches.
*   Runtime Cache entry TTLs will have no effect on the ISR revalidation time and
*   Next.js's `revalidatePath` and `revalidateTag`API does not invalidate the Runtime Cache.

The following Runtime Cache limits apply:

*   The maximum size of an item in the cache is 2 MB. Items larger than this will not be cached.
*   A cached item can have a maximum of 128 tags.
*   The maximum tag length is 256 bytes.

Usage of the Vercel Runtime Cache is charged, learn more about pricing in the [regional pricing docs](/docs/pricing/regional-pricing).

### [Database Connection Pool Management](#database-connection-pool-management)

#### [`attachDatabasePool`](#attachdatabasepool)

Call this function right after creating a database pool to ensure proper connection management in [Fluid Compute](/docs/fluid-compute). This function ensures that idle pool clients are properly released before functions suspend.

Supports PostgreSQL (pg), MySQL2, MariaDB, MongoDB, Redis (ioredis), Cassandra (cassandra-driver), and other compatible pool types.

| Name | Type | Description |
| --- | --- | --- |
| `dbPool` | `DbPool` | The database pool object. |

api/database.ts

TypeScript

TypeScriptJavaScript

```
import { Pool } from 'pg';
import { attachDatabasePool } from '@vercel/functions';
 
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});
 
attachDatabasePool(pool);
 
export default {
  async fetch() {
    const client = await pool.connect();
    try {
      const result = await client.query('SELECT NOW()');
      return Response.json(result.rows[0]);
    } finally {
      client.release();
    }
  },
};
```

### [OIDC methods](#oidc-methods)

#### [`awsCredentialsProvider`](#awscredentialsprovider)

This function has moved from @vercel/functions/oidc to @vercel/oidc-aws-credentials-provider. It is now deprecated from @vercel/functions and will be removed in a future release.

Description: Obtains the Vercel OIDC token and creates an AWS credential provider function that gets AWS credentials by calling the STS `AssumeRoleWithWebIdentity` API.

| Name | Type | Description |
| --- | --- | --- |
| `roleArn` | `string` | ARN of the role that the caller is assuming. |
| `clientConfig` | `Object` | Custom STS client configurations overriding the default ones. |
| `clientPlugins` | `Array` | Custom STS client middleware plugin to modify the client default behavior. |
| `roleAssumerWithWebIdentity` | `Function` | A function that assumes a role with web identity and returns a promise fulfilled with credentials for the assumed role. |
| `roleSessionName` | `string` | An identifier for the assumed role session. |
| `providerId` | `string` | The fully qualified host component of the domain name of the identity provider. |
| `policyArns` | `Array` | ARNs of the IAM managed policies that you want to use as managed session policies. |
| `policy` | `string` | An IAM policy in JSON format that you want to use as an inline session policy. |
| `durationSeconds` | `number` | The duration, in seconds, of the role session. Defaults to 3600 seconds. |

api/example.ts

```
import * as s3 from '@aws-sdk/client-s3';
import { awsCredentialsProvider } from '@vercel/oidc-aws-credentials-provider';
 
const s3Client = new s3.S3Client({
  credentials: awsCredentialsProvider({
    roleArn: process.env.AWS_ROLE_ARN,
  }),
});
```

#### [`getVercelOidcToken`](#getverceloidctoken)

This function has moved from @vercel/functions/oidc to @vercel/oidc. It is now deprecated from @vercel/functions and will be removed in a future release.

Description: Returns the OIDC token from the request context or the environment variable. This function first checks if the OIDC token is available in the environment variable `VERCEL_OIDC_TOKEN`. If it is not found there, it retrieves the token from the request context headers.

api/example.ts

```
import { ClientAssertionCredential } from '@azure/identity';
import { CosmosClient } from '@azure/cosmos';
import { getVercelOidcToken } from '@vercel/oidc';
 
const credentialsProvider = new ClientAssertionCredential(
  process.env.AZURE_TENANT_ID,
  process.env.AZURE_CLIENT_ID,
  getVercelOidcToken,
);
 
const cosmosClient = new CosmosClient({
  endpoint: process.env.COSMOS_DB_ENDPOINT,
  aadCredentials: credentialsProvider,
});
 
export const GET = () => {
  const container = cosmosClient
    .database(process.env.COSMOS_DB_NAME)
    .container(process.env.COSMOS_DB_CONTAINER);
  const items = await container.items.query('SELECT * FROM f').fetchAll();
  return Response.json({ items: items.resources });
};
```

--------------------------------------------------------------------------------
title: "vercel.functions API Reference (Python)"
description: "Learn about available APIs when working with Vercel Functions in Python."
last_updated: "null"
source: "https://vercel.com/docs/functions/functions-api-reference/vercel-sdk-python"
--------------------------------------------------------------------------------

# vercel.functions API Reference (Python)

Copy page

Ask AI about this page

Last updated October 23, 2025

## [Install and use the package](#install-and-use-the-package)

1.  Install the `vercel` package:
    
    ```
    pip install vercel
    ```
    
2.  Import the `vercel.functions` package:
    
    ```
    from vercel.functions import get_env
    ```
    

## [Helper methods](#helper-methods)

### [`get_env`](#get_env)

Description: Gets the [System Environment Variables](/docs/environment-variables/system-environment-variables#system-environment-variables) exposed by Vercel.

src/example.py

```
from vercel.functions import get_env
 
print(get_env().VERCEL_REGION)
```

### [`geolocation`](#geolocation)

Description: Returns the location information for the incoming request, in the following way:

```
{
  "city": "New York",
  "country": "US",
  "flag": "🇺🇸",
  "countryRegion": "NY",
  "region": "iad1",
  "latitude": "40.7128",
  "longitude": "-74.0060",
  "postalCode": "10001"
}
```

| Name | Type | Description |
| --- | --- | --- |
| `request_or_headers` | `RequestLike | HeadersLike` | The incoming request object which provides the IP |

src/main.py

```
from fastapi import FastAPI, Request
from vercel.functions import geolocation
 
app = FastAPI()
 
@app.get("/api/geo")
async def geo_info(request: Request):
    info = geolocation(request)
    return info
```

### [`ip_address`](#ip_address)

Description: Returns the IP address of the request from the headers.

| Name | Type | Description |
| --- | --- | --- |
| `request_or_headers` | `RequestLike | HeadersLike` | The incoming request object which provides the IP |

src/main.py

```
from fastapi import FastAPI, Request
from vercel.functions import ip_address
 
app = FastAPI()
 
@app.get("/api/ip")
async def get_ip_address(request: Request):
    ip = ip_address(request)  # you can also pass request.headers
    return {"ip": ip}
```

### [`RuntimeCache`](#runtimecache)

Description: Allows you to interact with the Vercel Runtime Cache in any Vercel region. Use this for storing and retrieving data across function, routing middleware, and build execution within a Vercel region.

| Name | Type | Description |
| --- | --- | --- |
| `key_hash_function` | `Callable[[str], str]` | Optional custom hash function for generating keys. |
| `namespace` | `str` | Optional namespace to prefix cache keys. |
| `namespace_separator` | `str` | Optional separator string for the namespace. |

#### [Specification](#specification)

`RuntimeCache | AsyncRuntimeCache` provide the following methods:

| Method | Description | Parameters |
| --- | --- | --- |
| `get` | Retrieves a value from the Vercel Runtime Cache. | `key: str`: The cache key |
| `set` | Stores a value in the Vercel Runtime Cache with optional `ttl` and/or `tags`. The `name` option allows a human-readable label to be associated with the cache entry for observability purposes. | 
*   `key: str`: The cache key
*   `value: object`: The value to store
*   `options?: { name?: str; tags?: list[str]; ttl?: int }`  
    Configuration object (not required)

 |
| `delete` | Removes a value from the Vercel Runtime Cache by key | `key: str`: The cache key to delete |
| `expire_tag` | Expires all cache entries associated with one or more tags | `tag: str | Sequence[str]`: Tag or sequence of tags to expire |

Use `AsyncRuntimeCache` in async code. It has the same API and uses the same underlying cache as `RuntimeCache`, and exposes awaitable methods.

src/main.py

```
import requests
import httpx
from fastapi import FastAPI, Request
from vercel.functions import RuntimeCache, AsyncRuntimeCache
 
app = FastAPI()
cache = RuntimeCache()
acache = AsyncRuntimeCache()
 
@app.get("/blog")
def get_blog(request: Request):
    key = "blog"
    value = cache.get(key)
    if value is not None:
        return value
 
    res = requests.get("https://api.vercel.app/blog")
    origin_value = res.json()
    cache.set(key, origin_value, {"ttl": 3600, "tags": ["blog"]})
 
    return origin_value
 
@app.get("/blog-async")
async def get_blog_async(request: Request):
    key = "blog"
    value = await acache.get(key)
    if value is not None:
        return value
 
    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.vercel.app/blog")
        origin_value = res.json()
    await acache.set(key, origin_value, {"ttl": 3600, "tags": ["blog"]})
    return origin_value
```

After assigning tags to your cached data, use the `expire_tag` method to invalidate all cache entries associated with that tag. This operation is propagated globally across all Vercel regions within 300ms.

src/main.py

```
from fastapi import FastAPI, Request
from vercel.functions import RuntimeCache
 
app = FastAPI()
cache = RuntimeCache()
 
@app.get("/expire-blog")
def expire_blog(request: Request):
    cache.expire_tag("blog")
    return {"ok": True}
```

#### [Limits and usage](#limits-and-usage)

The Runtime Cache is isolated per Vercel project and deployment environment (`preview` and `production`). Cached data is persisted across deployments and can be invalidated either through time-based expiration or by calling `expire_tag`. However, TTL (time-to-live) and tag updates aren't reconciled between deployments. In those cases, we recommend either purging the runtime cache or modifying the cache key.

The Runtime Cache API does not have first class integration with [Incremental Static Regeneration](/docs/incremental-static-regeneration). This means that:

*   Runtime Cache entry tags will not apply to ISR pages, so you cannot use `expire_tag` to invalidate both caches.
*   Runtime Cache entry TTLs will have no effect on the ISR revalidation time and

The following Runtime Cache limits apply:

*   The maximum size of an item in the cache is 2 MB. Items larger than this will not be cached.
*   A cached item can have a maximum of 128 tags.
*   The maximum tag length is 256 bytes.

Usage of the Vercel Runtime Cache is charged, learn more about pricing in the [regional pricing docs](/docs/pricing/regional-pricing).

--------------------------------------------------------------------------------
title: "Vercel Functions Limits"
description: "Learn about the limits and restrictions of using Vercel Functions with the Node.js runtime."
last_updated: "null"
source: "https://vercel.com/docs/functions/limitations"
--------------------------------------------------------------------------------

# Vercel Functions Limits

Copy page

Ask AI about this page

Last updated September 9, 2025

The table below outlines the limits and restrictions of using Vercel Functions with the Node.js runtime:

| Feature | Node.js |
| --- | --- |
| [Maximum memory](/docs/functions/limitations#memory-size-limits) | Hobby: 2 GB, Pro and Ent: 4 GB |
| [Maximum duration](/docs/functions/limitations#max-duration) | Hobby: 300s (default) - [configurable up to 300s](/docs/functions/configuring-functions/duration), Pro: 300s (default) - [configurable](/docs/functions/configuring-functions/duration) up to 800s, Ent: 300s (default) - [configurable](/docs/functions/configuring-functions/duration) up to 800s. If [fluid compute](/docs/fluid-compute) is enabled, these values are increased across plans. See [max durations](/docs/functions/limitations#max-duration) for more information. |
| [Size](/docs/functions/runtimes#bundle-size-limits) (after gzip compression) | 250 MB |
| [Concurrency](/docs/functions/concurrency-scaling#automatic-concurrency-scaling) | Auto-scales up to 30,000 (Hobby and Pro) or 100,000+ (Enterprise) concurrency |
| [Cost](/docs/functions/runtimes) | Pay for active CPU time and provisioned memory time |
| [Regions](/docs/functions/runtimes#location) | Executes region-first, [can customize location](/docs/functions/regions#select-a-default-serverless-region).  
Enterprise teams can set [multiple regions](/docs/functions/regions#set-multiple-serverless-regions) |
| [API Coverage](/docs/functions/limitations#api-support) | Full Node.js coverage |
| [File descriptors](/docs/functions/limitations#file-descriptors) | 1,024 shared across concurrent executions (including runtime usage) |

## [Functions name](#functions-name)

The following limits apply to the function's name when using [Node.js runtime](/docs/functions/runtimes/node-js):

*   Maximum length of 128 characters. This includes the extension of the file (e.g. `apps/admin/api/my-function.js` is 29 characters)
*   No spaces are allowed. Replace them with a `-` or `_` (e.g. `api/my function.js` isn't allowed)

## [Bundle size limits](#bundle-size-limits)

Vercel places restrictions on the maximum size of the deployment bundle for functions to ensure that they execute in a timely manner.

For Vercel Functions, the maximum uncompressed size is 250 MB including layers which are automatically used depending on [runtimes](/docs/functions/runtimes). These limits are [enforced by AWS](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).

You can use [`includeFiles` and `excludeFiles`](/docs/project-configuration#functions) to specify items which may affect the function size, however the limits cannot be configured. These configurations are not supported in Next.js, instead use [`outputFileTracingIncludes`](https://nextjs.org/docs/app/api-reference/next-config-js/output).

## [Max duration](#max-duration)

This refers to the longest time a function can process an HTTP request before responding.

While Vercel Functions have a default duration, this duration can be extended using the [maxDuration config](/docs/functions/configuring-functions/duration). If a Vercel Function doesn't respond within the duration, a 504 error code ([`FUNCTION_INVOCATION_TIMEOUT`](/docs/errors/FUNCTION_INVOCATION_TIMEOUT)) is returned.

With [fluid compute](/docs/fluid-compute) enabled, Vercel Functions have the following defaults and maximum limits (applies to the Node.js and Python runtimes):

### [Node.js and python runtimes](#node.js-and-python-runtimes)

|  | Default | Maximum |
| --- | --- | --- |
| Hobby | 300s (5 minutes) | 300s (5 minutes) |
| Pro | 300s (5 minutes) | 800s (13 minutes) |
| Enterprise | 300s (5 minutes) | 800s (13 minutes) |

Have an existing project not yet using Fluid compute?

Vercel Functions have the following defaults and maximum limits for the duration of a function:

|  | Default | Maximum |
| --- | --- | --- |
| Hobby | 10s | 60s (1 minute) |
| Pro | 15s | 300s (5 minutes) |
| Enterprise | 15s | 900s (15 minutes) |

### [Edge runtime](#edge-runtime)

Vercel Functions using the [Edge runtime](/docs/functions/runtimes/edge) must begin sending a response within 25 seconds to maintain streaming capabilities beyond this period, and can continue [streaming](/docs/functions/streaming-functions) data for up to 300 seconds.

## [Memory size limits](#memory-size-limits)

Vercel Functions have the following defaults and maximum limits:

|  | Default | Maximum |
| --- | --- | --- |
| Hobby | 2 GB / 1 vCPU | 2 GB / 1 vCPU |
| Pro /Enterprise | 2 GB / 1 vCPU | 4 GB / 2 vCPU |

Users on Pro and Enterprise plans can [configure the default memory size](/docs/functions/configuring-functions/memory#setting-your-default-function-memory-/-cpu-size) for all functions in the dashboard.

The maximum size for a Function includes your JavaScript code, imported libraries and files (such as fonts), and all files bundled in the function.

If you reach the limit, make sure the code you are importing in your function is used and is not too heavy. You can use a package size checker tool like [bundle](https://bundle.js.org/) to check the size of a package and search for a smaller alternative.

## [Request body size](#request-body-size)

In Vercel, the request body size is the maximum amount of data that can be included in the body of a request to a function.

The maximum payload size for the request body or the response body of a Vercel Function is 4.5 MB. If a Vercel Function receives a payload in excess of the limit it will return an error [413: `FUNCTION_PAYLOAD_TOO_LARGE`](/docs/errors/FUNCTION_PAYLOAD_TOO_LARGE). See [How do I bypass the 4.5MB body size limit of Vercel Functions](/guides/how-to-bypass-vercel-body-size-limit-serverless-functions) for more information.

## [File descriptors](#file-descriptors)

File descriptors are unique identifiers that the operating system uses to track and manage open resources like files, network connections, and I/O streams. Think of them as handles or references that your application uses to interact with these resources. Each time your code opens a file, establishes a network connection, or creates a socket, the system assigns a file descriptor to track that resource.

Vercel Functions have a limit of 1,024 file descriptors shared across all concurrent executions. This limit includes file descriptors used by the runtime itself, so the actual number available to your application code will be strictly less than 1,024.

File descriptors are used for:

*   Open files
*   Network connections (TCP sockets, HTTP requests)
*   Database connections
*   File system operations

If your function exceeds this limit, you might encounter errors related to "too many open files" or similar resource exhaustion issues.

To manage file descriptors effectively, consider the following:

*   Close files, database connections, and HTTP connections when they're no longer needed
*   Use connection pooling for database connections
*   Implement proper resource cleanup in your function code

## [API support](#api-support)

|  | Node.js runtime (and more) |
| --- | --- |
| Geolocation data | [Yes](/docs/headers/request-headers#x-vercel-ip-country) |
| Access request headers | Yes |
| Cache responses | [Yes](/docs/edge-cache#using-vercel-functions) |

## [Cost and usage](#cost-and-usage)

The Hobby plan offers functions for free, within [limits](/docs/limits). The Pro plan extends these limits, and charges usage based on active CPU time and provisioned memory time for Vercel Functions.

Active CPU time is based on the amount of CPU time your code actively consumes, measured in milliseconds. Waiting for I/O (e.g. calling AI models, database queries) does not count towards active CPU time. Provisioned memory time is based on the memory allocated to your function instances multiplied by the time they are running.

It is important to make sure you've set a reasonable [maximum duration](/docs/functions/configuring-functions/duration) for your function. See "Managing usage and pricing for [Vercel Functions](/docs/pricing/serverless-functions)" for more information.

## [Environment variables](#environment-variables)

If you have [fluid compute](/docs/fluid-compute) enabled, the following environment variables are not accessible you cannot log them:

*   `AWS_EXECUTION_ENV`
*   `AWS_LAMBDA_EXEC_WRAPPER`
*   `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
*   `AWS_LAMBDA_FUNCTION_NAME`
*   `AWS_LAMBDA_FUNCTION_VERSION`
*   `AWS_LAMBDA_INITIALIZATION_TYPE`
*   `AWS_LAMBDA_LOG_GROUP_NAME`
*   `AWS_LAMBDA_LOG_STREAM_NAME`
*   `AWS_LAMBDA_RUNTIME_API`
*   `AWS_XRAY_CONTEXT_MISSING`
*   `AWS_XRAY_DAEMON_ADDRESS`
*   `LAMBDA_RUNTIME_DIR`
*   `LAMBDA_TASK_ROOT`
*   `_AWS_XRAY_DAEMON_ADDRESS`
*   `_AWS_XRAY_DAEMON_PORT`
*   `_HANDLER`
*   `_LAMBDA_TELEMETRY_LOG_FD`

--------------------------------------------------------------------------------
title: "Vercel Function Logs"
description: "Use runtime logs to debug and monitor your Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/logs"
--------------------------------------------------------------------------------

# Vercel Function Logs

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel Functions allow you to debug and monitor your functions using runtime logs. Users on the Pro and Enterprise plans can use Vercel's support for [Log Drains](/docs/drains) to collect and analyze your logs using third-party providers. Functions have full support for the [`console`](https://developer.mozilla.org/docs/Web/API/Console) API, including `time`, `debug`, `timeEnd`, and more.

## [Runtime Logs](#runtime-logs)

You can view [runtime logs](/docs/runtime-logs#what-are-runtime-logs) for all Vercel Functions in real-time from [the Logs tab](/docs/runtime-logs#view-runtime-logs) of your project's dashboard. You can use the various filters and options to find specific log information. These logs are held for an [amount of time based on your plan](/docs/runtime-logs#limits).

When your function is [streaming](/docs/functions/streaming-functions), you'll get the following:

*   You can [view the logs](/docs/runtime-logs#view-runtime-logs) in real-time from the Logs tab of your project's dashboard.
*   Each action of writing to standard output, such as using `console.log`, results in a separate log entry.
*   Each of the logs are 256 KB per line.
*   The path in streaming logs will be prefixed with a forward slash (`/`).

For more information, see [Runtime Logs](/docs/runtime-logs).

These changes in the frequency and format of logs will affect Log Drains. If you are using Log Drains we recommend ensuring that your ingestion can handle both the new format and frequency.

### [Number of logs per request](#number-of-logs-per-request)

When a Function on a specific path receives a user request, you _may_ see more than one log when the application renders or regenerates the page.

This can occur in the following situations:

1.  When a new page is rendered
2.  When you are using [Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration)

In the case of ISR, multiple logs are the result of:

*   A [stale](/docs/edge-cache#cache-invalidation) page having to be regenerated. For stale pages, both HTML (for direct browser navigation) and JSON (for Single Page App (SPA) transitions) are rendered simultaneously to maintain consistency
*   On-demand ISR happening with `fallback` set as [`blocking`](/docs/incremental-static-regeneration/quickstart). During on-demand ISR, the page synchronously renders (e.g., HTML) upon request, followed by a background revalidation of both HTML and JSON versions

### [Next.js logs](#next.js-logs)

In Next.js projects, logged functions include API Routes (those defined in `pages/api/**/*.ts` or `app/**/route.ts`).

Pages that use SSR, such as those that call `getServerSideProps` or export [`revalidate`](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration), will also be available both in the filter dropdown and the real time logs.

--------------------------------------------------------------------------------
title: "Getting started with Vercel Functions"
description: "Build your first Vercel Function in a few steps."
last_updated: "null"
source: "https://vercel.com/docs/functions/quickstart"
--------------------------------------------------------------------------------

# Getting started with Vercel Functions

Copy page

Ask AI about this page

Last updated October 10, 2025

In this guide, you'll learn how to get started with Vercel Functions using your favorite [frontend framework](/docs/frameworks) (or no framework).

## [Prerequisites](#prerequisites)

*   You can use an existing project or create a new one. If you don't have one, you can run the following terminal command to create a Next.js project:
    
    terminal
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    npx create-next-app@latest --typescript
    ```
    

## [Create a Vercel Function](#create-a-vercel-function)

Open the code block in v0 for a walk through on creating a Vercel Function with the below code, or copy the code into your project. The function fetches data from the [Vercel API](https://api.vercel.app/products) and returns it as a JSON response.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/hello/route.ts

TypeScript

TypeScriptJavaScript

```
export async function GET(request: Request) {
  const response = await fetch('https://api.vercel.app/products');
  const products = await response.json();
  return Response.json(products);
}
```

While using `fetch` is the recommended way to create a Vercel Function, you can still use HTTP methods like `GET` and `POST`.

## [Next steps](#next-steps)

Now that you have set up a Vercel Function, you can explore the following topics to learn more:

*   [Explore the functions API reference](/docs/functions/functions-api-reference): Learn more about creating a Vercel Function.
*   [Learn about streaming functions](/docs/functions/streaming-functions): Learn how to fetch streamable data with Vercel Functions.
*   [Choosing a Runtime](/docs/functions/runtimes): Learn more about the differences between the Node.js and Edge runtimes.
*   [Configuring Functions](/docs/functions/configuring-functions): Learn about the different options for configuring a Vercel Function.

--------------------------------------------------------------------------------
title: "Runtimes"
description: "Runtimes transform your source code into Functions, which are served by our CDN. Learn about the official runtimes supported by Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes"
--------------------------------------------------------------------------------

# Runtimes

Copy page

Ask AI about this page

Last updated October 27, 2025

Vercel supports multiple runtimes for your functions. Each runtime has its own set of libraries, APIs, and functionality that provides different trade-offs and benefits.

Runtimes transform your source code into [Functions](/docs/functions), which are served by our [CDN](/docs/cdn).

## [Official runtimes](#official-runtimes)

Vercel Functions support the following official runtimes:

| Runtime | Description |
| --- | --- |
| [Node.js](/docs/functions/runtimes/node-js) | The Node.js runtime takes an entrypoint of a Node.js function, builds its dependencies (if any) and bundles them into a Vercel Function. |
| [Bun](/docs/functions/runtimes/bun) | The Bun runtime takes an entrypoint of a Bun function, builds its dependencies (if any) and bundles them into a Vercel Function. |
| [Go RuntimeGo](/docs/functions/runtimes/go) | The Go runtime takes in a Go program that defines a singular HTTP handler and outputs it as a Vercel Function. |
| [Python](/docs/functions/runtimes/python) | The Python runtime takes in a Python program that defines a singular HTTP handler and outputs it as a Vercel Function. |
| [Ruby](/docs/functions/runtimes/ruby) | The Ruby runtime takes in a Ruby program that defines a singular HTTP handler and outputs it as a Vercel Function. |
| [Edge](/docs/functions/runtimes/edge) | The Edge runtime is built on top of the V8 engine, allowing it to run in isolated execution environments that don't require a container or virtual machine. |

## [Community runtimes](#community-runtimes)

If you would like to use a language that Vercel does not support by default, you can use a community runtime by setting the [`functions` property](/docs/project-configuration#functions) in `vercel.json`. For more information on configuring other runtimes, see [Configuring your function runtime](/docs/functions/configuring-functions/runtime#other-runtimes).

The following community runtimes are recommended by Vercel:

| Runtime | Runtime Module | Docs |
| --- | --- | --- |
| Bash | `vercel-bash` | [https://github.com/importpw/vercel-bash](https://github.com/importpw/vercel-bash) |
| Deno | `vercel-deno` | [https://github.com/vercel-community/deno](https://github.com/vercel-community/deno) |
| PHP | `vercel-php` | [https://github.com/vercel-community/php](https://github.com/vercel-community/php) |
| Rust | `vercel-rust` | [https://github.com/vercel-community/rust](https://github.com/vercel-community/rust) |

You can create a community runtime by using the [Runtime API](https://github.com/vercel/vercel/blob/main/DEVELOPING_A_RUNTIME.md). Alternatively, you can use the [Build Output API](/docs/build-output-api/v3).

## [Features](#features)

*   Location: Deployed as region-first, [can customize location](/docs/functions/configuring-functions/region#setting-your-default-region). Pro and Enterprise teams can set [multiple regions](/docs/functions/configuring-functions/region#project-configuration)
*   [Failover](/docs/functions/runtimes#failover-mode): Automatic failover to [defined regions](/docs/functions/configuring-functions/region#node.js-runtime-failover)
*   [Automatic concurrency scaling](/docs/functions/concurrency-scaling#automatic-concurrency-scaling): Auto-scales up to 30,000 (Hobby and Pro) or 100,000+ (Enterprise) concurrency
*   [Isolation boundary](/docs/functions/runtimes#isolation-boundary): microVM
*   [File system support](/docs/functions/runtimes#file-system-support): Read-only filesystem with writable `/tmp` scratch space up to 500 MB
*   [Archiving](/docs/functions/runtimes#archiving): Functions are archived when not invoked
*   [Functions created per deployment](/docs/functions/runtimes#functions-created-per-deployment): Hobby: Framework-dependent, Pro and Enterprise: No limit

### [Location](#location)

Location refers to where your functions are executed. Vercel Functions are region-first, and can be [deployed](/docs/functions/configuring-functions/region#project-configuration) to up to 3 regions on Pro or 18 on Enterprise. Deploying to more regions than your plan allows for will cause your deployment to fail before entering the [build step](/docs/deployments/configure-a-build).

### [Failover mode](#failover-mode)

Vercel's failover mode refers to the system's behavior when a function fails to execute because of data center downtime.

Vercel provides [redundancy](/docs/regions#outage-resiliency) and automatic failover for Vercel Functions using the Edge runtime. For Vercel Functions on the Node.js runtime, you can use the [`functionFailoverRegions` configuration](/docs/project-configuration#functionfailoverregions) in your `vercel.json` file to specify which regions the function should automatically failover to.

### [Isolation boundary](#isolation-boundary)

In Vercel, the isolation boundary refers to the separation of individual instances of a function to ensure they don't interfere with each other. This provides a secure execution environment for each function.

With traditional serverless infrastructure, each function uses a microVM for isolation, which provides strong security but also makes them slower to start and more resource intensive.

### [File system support](#file-system-support)

Filesystem support refers to a function's ability to read and write to the filesystem. Vercel functions have a read-only filesystem with writable `/tmp` scratch space up to 500 MB.

### [Archiving](#archiving)

Vercel Functions are archived when they are not invoked:

*   Within 2 weeks for [Production Deployments](/docs/deployments)
*   Within 48 hours for [Preview Deployments](/docs/deployments/environments#preview-environment-pre-production)

Archived functions will be unarchived when they're invoked, which can make the initial [cold start](/docs/infrastructure/compute#cold-and-hot-boots) time at least 1 second longer than usual.

### [Functions created per deployment](#functions-created-per-deployment)

When using [Next.js](/docs/frameworks/nextjs) or [SvelteKit](/docs/frameworks/sveltekit) on Vercel, dynamic code (APIs, server-rendered pages, or dynamic `fetch` requests) will be bundled into the fewest number of Vercel Functions possible, to help reduce cold starts. Because of this, it's unlikely that you'll hit the limit of 12 bundled Vercel Functions per deployment.

When using other [frameworks](/docs/frameworks), or Vercel Functions [directly without a framework](/docs/functions), every API maps directly to one Vercel Function. For example, having five files inside `api/` would create five Vercel Functions. For Hobby, this approach is limited to 12 Vercel Functions per deployment.

## [Caching data](#caching-data)

A runtime can retain an archive of up to 100 MB of the filesystem at build time. The cache key is generated as a combination of:

*   Project name
*   [Team ID](/docs/accounts#find-your-team-id) or User ID
*   Entrypoint path (e.g., `api/users/index.go`)
*   Runtime identifier including version (e.g.: `@vercel/go@0.0.1`)

The cache will be invalidated if any of those items changes. You can bypass the cache by running `vercel -f`.

## [Environment variables](#environment-variables)

You can use [environment variables](/docs/environment-variables#environment-variable-size) to manage dynamic values and sensitive information affecting the operation of your functions. Vercel allows developers to define these variables either at deployment or during runtime.

You can use a total of 64 KB in environments variables per-deployment on Vercel. This limit is for all variables combined, and so no single variable can be larger than 64 KB.

## [Vercel features support](#vercel-features-support)

The following features are supported by Vercel Functions:

### [Secure Compute](#secure-compute)

Vercel's [Secure Compute](/docs/secure-compute) feature offers enhanced security for your Vercel Functions, including dedicated IP addresses and VPN options. This can be particularly important for functions that handle sensitive data.

### [Streaming](#streaming)

Streaming refers to the ability to send or receive data in a continuous flow.

The Node.js runtime supports streaming by default. Streaming is also supported when using the [Python runtime](/docs/functions/streaming-functions#streaming-python-functions).

Vercel Functions have a [maximum duration](/docs/functions/configuring-functions/duration), meaning that it isn't possible to stream indefinitely.

Node.js and Edge runtime streaming functions support the [`waitUntil` method](/docs/functions/functions-api-reference/vercel-functions-package#waituntil), which allows for an asynchronous task to be performed during the lifecycle of the request. This means that while your function will likely run for the same amount of time, your end-users can have a better, more interactive experience.

### [Cron jobs](#cron-jobs)

[Cron jobs](/docs/cron-jobs) are time-based scheduling tools used to automate repetitive tasks. When a cron job is triggered through the [cron expression](/docs/cron-jobs#cron-expressions), it calls a Vercel Function.

### [Vercel Storage](#vercel-storage)

From your function, you can communicate with a choice of [data stores](/docs/storage). To ensure low-latency responses, it's crucial to have compute close to your databases. Always deploy your databases in regions closest to your functions to avoid long network roundtrips. For more information, see our [best practices](/docs/storage#locate-your-data-close-to-your-functions) documentation.

### [Edge Config](#edge-config)

An [Edge Config](/docs/edge-config) is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers.

### [OTEL](#otel)

Vercel has an [OpenTelemetry (OTEL) collector](/docs/otel) that allows you to send OTEL traces from your Vercel Functions to application performance monitoring (APM) vendors such as New Relic.

--------------------------------------------------------------------------------
title: "Using the Bun Runtime with Vercel Functions"
description: "Learn how to use the Bun runtime with Vercel Functions to create fast, efficient functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/bun"
--------------------------------------------------------------------------------

# Using the Bun Runtime with Vercel Functions

Copy page

Ask AI about this page

Last updated October 27, 2025

The Bun runtime is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

Bun is a fast, all-in-one JavaScript runtime that serves as an alternative to Node.js.

Bun provides Node.js API compatibility and is generally faster than Node.js for CPU-bound tasks. It includes a bundler, test runner, and package manager.

## [Configuring the runtime](#configuring-the-runtime)

For all frameworks, including Next.js, you can configure the runtime in your `vercel.json` file using the [`bunVersion`](/docs/project-configuration#bunversion) property:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "bunVersion": "1.x"
}
```

## [Framework-specific considerations](#framework-specific-considerations)

### [Next.js](#next.js)

When using Next.js, and [ISR](/docs/incremental-static-regeneration), you must change your `build` and `dev` commands in your package.json file to use the Bun runtime:

Before:

package.json

```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build"
  }
}
```

After:

package.json

```
{
  "scripts": {
    "dev": "bun run --bun next dev",
    "build": "bun run --bun next build"
  }
}
```

### [Routing Middleware](#routing-middleware)

The Bun runtime works with [Routing Middleware](/docs/routing-middleware) the same way as the Node.js runtime once you set the `bunVersion` in your `vercel.json` file. Note that you'll also have to set the runtime config to `nodejs` in your `middleware.ts` file.

## [Feature support](#feature-support)

The Bun runtime on Vercel supports most Node.js features. The main differences relate to automatic source maps, bytecode caching, and request metrics on the `node:http` and `node:https` modules. Request metrics using `fetch` work with both runtimes.

See the table below for a detailed comparison:

Bun Runtime vs Node.js Runtime feature support comparison table
| 
Feature

 | 

Bun Runtime

 | 

Node.js Runtime

 |
| --- | --- | --- |
| Node.js APIs | 

 | 

 |
| 

[Fluid compute](/docs/fluid-compute)

 | 

 | 

 |
| 

[Active CPU](/docs/functions/usage-and-pricing#active-cpu)

 | 

 | 

 |
| 

[Streaming](/docs/functions/streaming-functions)

 | 

 | 

 |
| 

[`waitUntil`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil)

 | 

 | 

 |
| 

[Logs](/docs/functions/logs)

 | 

 | 

 |
| Automatic source maps | 

 | 

 |
| 

[Bytecode caching](/docs/fluid-compute#bytecode-caching)

 | 

 | 

 |
| Request metrics (node:http/https) | 

 | 

 |
| Request metrics (fetch) | 

 | 

 |

## [Supported APIs](#supported-apis)

Vercel Functions using the Bun runtime support [most Node.js APIs](https://bun.sh/docs/runtime/nodejs-apis), including standard Web APIs such as the [Request and Response Objects](/docs/functions/runtimes/node-js#node.js-request-and-response-objects).

## [Using TypeScript with Bun](#using-typescript-with-bun)

Bun has built-in TypeScript support with zero configuration required. The runtime supports files ending with `.ts` inside of the `/api` directory as TypeScript files to compile and serve when deploying.

api/hello.ts

```
export default {
  async fetch(request: Request) {
    const url = new URL(request.url);
    const name = url.searchParams.get('name') || 'World';
 
    return Response.json({ message: `Hello ${name}!` });
  },
};
```

## [Performance considerations](#performance-considerations)

Bun is generally faster than Node.js, especially for CPU-bound tasks. Performance varies by workload, and in some cases Node.js may be faster depending on the specific operations your function performs.

## [When to use Bun](#when-to-use-bun)

Bun is best suited for new workloads where you want a fast, all-in-one toolkit with built-in support for TypeScript, JSX, and modern JavaScript features. Consider using Bun when:

*   You want faster execution for CPU-bound tasks
*   You prefer zero-config TypeScript and JSX support
*   You're starting a new project and want to use modern tooling

Consider using Node.js instead if:

*   Node.js is already installed on your project and is working for you
*   You need automatic source maps for debugging
*   You need request metrics on the `node:http` or `node:https` modules

Both runtimes run on [Fluid compute](/docs/fluid-compute) and support the same core Vercel Functions features.

--------------------------------------------------------------------------------
title: "Edge Runtime"
description: "Learn about the Edge runtime, an environment in which Vercel Functions can run."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/edge"
--------------------------------------------------------------------------------

# Edge Runtime

Copy page

Ask AI about this page

Last updated October 27, 2025

We recommend migrating from edge to Node.js for improved performance and reliability. Both runtimes run on [Fluid compute](/docs/fluid-compute) with [Active CPU pricing](/docs/functions/usage-and-pricing).

To convert your Vercel Function to use the Edge runtime, add the following code to your function:

Next.js (/app)Next.js (/pages)Other frameworks

app/api/my-function/route.ts

TypeScript

TypeScriptJavaScript

```
export const runtime = 'edge'; // 'nodejs' is the default
 
export function GET(request: Request) {
  return new Response(`I am an Vercel Function!`, {
    status: 200,
  });
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

## [Region](#region)

By default, Vercel Functions using the Edge runtime execute in the region closest to the incoming request. You can set one or more preferred regions using the route segment [config](#setting-regions-in-your-function) `preferredRegion` or specify a `regions` key within a config object to set one or more regions for your functions to execute in.

### [Setting regions in your function](#setting-regions-in-your-function)

If your function depends on a data source, you may want it to be close to that source for fast responses.

To configure which region (or multiple regions) you want your function to execute in, pass the [ID of your preferred region(s)](/docs/regions#region-list) in the following way:

The `preferredRegion` option can be used to specify a single region using a string value, or multiple regions using a string array. See the [Next.js documentation](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#preferredregion) for more information.

Next.js (/app)Next.js (/pages)Other frameworks

app/api/regional-example/route.ts

TypeScript

TypeScriptJavaScript

```
export const runtime = 'edge'; // 'nodejs' is the default
// execute this function on iad1 or hnd1, based on the connecting client location
export const preferredRegion = ['iad1', 'hnd1'];
export const dynamic = 'force-dynamic'; // no caching
 
export function GET(request: Request) {
  return new Response(
    `I am an Vercel Function! (executed on ${process.env.VERCEL_REGION})`,
    {
      status: 200,
    },
  );
}
```

If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`

## [Failover mode](#failover-mode)

In the event of regional downtime, Vercel will automatically reroute traffic to the next closest CDN region on all plans. For more information on which regions Vercel routes traffic to, see [Outage Resiliency](/docs/regions#outage-resiliency).

## [Maximum duration](#maximum-duration)

Vercel Functions using the Edge runtime must begin sending a response within 25 seconds to maintain streaming capabilities beyond this period, and can continue [streaming](/docs/functions/streaming-functions) data for up to 300 seconds.

## [Concurrency](#concurrency)

Vercel automatically scales your functions to handle traffic surges, ensuring optimal performance during increased loads. For more information, see [Concurrency scaling](/docs/functions/concurrency-scaling).

## [Edge Runtime supported APIs](#edge-runtime-supported-apis)

The Edge runtime is built on top of the [V8 engine](https://v8.dev/), allowing it to run in isolated execution environments that don't require a container or virtual machine.

### [Supported APIs](#supported-apis)

The Edge runtime provides a subset of Web APIs such as [`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API), [`Request`](https://developer.mozilla.org/docs/Web/API/Request), and [`Response`](https://developer.mozilla.org/docs/Web/API/Response).

The following tables list the APIs that are available in the Edge runtime.

### [Network APIs](#network-apis)

| API | Description |
| --- | --- |
| [`fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API) | Fetches a resource |
| [`Request`](https://developer.mozilla.org/docs/Web/API/Request) | Represents an HTTP request |
| [`Response`](https://developer.mozilla.org/docs/Web/API/Response) | Represents an HTTP response |
| [`Headers`](https://developer.mozilla.org/docs/Web/API/Headers) | Represents HTTP headers |
| [`FormData`](https://developer.mozilla.org/docs/Web/API/FormData) | Represents form data |
| [`File`](https://developer.mozilla.org/docs/Web/API/File) | Represents a file |
| [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob) | Represents a blob |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Represents URL search parameters |
| [`Blob`](https://developer.mozilla.org/docs/Web/API/Blob) | Represents a blob |
| [`Event`](https://developer.mozilla.org/docs/Web/API/Event) | Represents an event |
| [`EventTarget`](https://developer.mozilla.org/docs/Web/API/EventTarget) | Represents an object that can handle events |
| [`PromiseRejectEvent`](https://developer.mozilla.org/docs/Web/API/PromiseRejectionEvent) | Represents an event that is sent to the global scope of a script when a JavaScript Promise is rejected |

### [Encoding APIs](#encoding-apis)

| API | Description |
| --- | --- |
| [`TextEncoder`](https://developer.mozilla.org/docs/Web/API/TextEncoder) | Encodes a string into a Uint8Array |
| [`TextDecoder`](https://developer.mozilla.org/docs/Web/API/TextDecoder) | Decodes a Uint8Array into a string |
| [`atob`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/atob) | Decodes a base-64 encoded string |
| [`btoa`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/btoa) | Encodes a string in base-64 |

### [Stream APIs](#stream-apis)

| API | Description |
| --- | --- |
| [`ReadableStream`](https://developer.mozilla.org/docs/Web/API/ReadableStream) | Represents a readable stream |
| [`WritableStream`](https://developer.mozilla.org/docs/Web/API/WritableStream) | Represents a writable stream |
| [`WritableStreamDefaultWriter`](https://developer.mozilla.org/docs/Web/API/WritableStreamDefaultWriter) | Represents a writer of a WritableStream |
| [`TransformStream`](https://developer.mozilla.org/docs/Web/API/TransformStream) | Represents a transform stream |
| [`ReadableStreamDefaultReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamDefaultReader) | Represents a reader of a ReadableStream |
| [`ReadableStreamBYOBReader`](https://developer.mozilla.org/docs/Web/API/ReadableStreamBYOBReader) | Represents a reader of a ReadableStream |

### [Crypto APIs](#crypto-apis)

| API | Description |
| --- | --- |
| [`crypto`](https://developer.mozilla.org/docs/Web/API/Window/crypto) | Provides access to the cryptographic functionality of the platform |
| [`SubtleCrypto`](https://developer.mozilla.org/docs/Web/API/SubtleCrypto) | Provides access to common cryptographic primitives, like hashing, signing, encryption or decryption |
| [`CryptoKey`](https://developer.mozilla.org/docs/Web/API/CryptoKey) | Represents a cryptographic key |

### [Other Web Standard APIs](#other-web-standard-apis)

| API | Description |
| --- | --- |
| [`AbortController`](https://developer.mozilla.org/docs/Web/API/AbortController) | Allows you to abort one or more DOM requests as and when desired |
| [`AbortSignal`](https://developer.mozilla.org/docs/Web/API/AbortSignal) | Represents a signal object that allows you to communicate with a DOM request (such as a [`Fetch`](https://developer.mozilla.org/docs/Web/API/Fetch_API) request) and abort it if required |
| [`DOMException`](https://developer.mozilla.org/docs/Web/API/DOMException) | Represents an error that occurs in the DOM |
| [`structuredClone`](https://developer.mozilla.org/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) | Creates a deep copy of a value |
| [`URLPattern`](https://developer.mozilla.org/docs/Web/API/URLPattern) | Represents a URL pattern |
| [`Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array) | Represents an array of values |
| [`ArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer) | Represents a generic, fixed-length raw binary data buffer |
| [`Atomics`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Atomics) | Provides atomic operations as static methods |
| [`BigInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt) | Represents a whole number with arbitrary precision |
| [`BigInt64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array) | Represents a typed array of 64-bit signed integers |
| [`BigUint64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array) | Represents a typed array of 64-bit unsigned integers |
| [`Boolean`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean) | Represents a logical entity and can have two values: `true` and `false` |
| [`clearInterval`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearInterval) | Cancels a timed, repeating action which was previously established by a call to `setInterval()` |
| [`clearTimeout`](https://developer.mozilla.org/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout) | Cancels a timed, repeating action which was previously established by a call to `setTimeout()` |
| [`console`](https://developer.mozilla.org/docs/Web/API/Console) | Provides access to the browser's debugging console |
| [`DataView`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/DataView) | Represents a generic view of an `ArrayBuffer` |
| [`Date`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date) | Represents a single moment in time in a platform-independent format |
| [`decodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) | Decodes a Uniform Resource Identifier (URI) previously created by `encodeURI` or by a similar routine |
| [`decodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) | Decodes a Uniform Resource Identifier (URI) component previously created by `encodeURIComponent` or by a similar routine |
| [`encodeURI`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) | Encodes a Uniform Resource Identifier (URI) by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character |
| [`encodeURIComponent`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) | Encodes a Uniform Resource Identifier (URI) component by replacing each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character |
| [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error) | Represents an error when trying to execute a statement or accessing a property |
| [`EvalError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/EvalError) | Represents an error that occurs regarding the global function `eval()` |
| [`Float32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float32Array) | Represents a typed array of 32-bit floating point numbers |
| [`Float64Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Float64Array) | Represents a typed array of 64-bit floating point numbers |
| [`Function`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Represents a function |
| [`Infinity`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Infinity) | Represents the mathematical Infinity value |
| [`Int8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int8Array) | Represents a typed array of 8-bit signed integers |
| [`Int16Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int16Array) | Represents a typed array of 16-bit signed integers |
| [`Int32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Int32Array) | Represents a typed array of 32-bit signed integers |
| [`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl) | Provides access to internationalization and localization functionality |
| [`isFinite`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isFinite) | Determines whether a value is a finite number |
| [`isNaN`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/isNaN) | Determines whether a value is `NaN` or not |
| [`JSON`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/JSON) | Provides functionality to convert JavaScript values to and from the JSON format |
| [`Map`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Map) | Represents a collection of values, where each value may occur only once |
| [`Math`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Math) | Provides access to mathematical functions and constants |
| [`Number`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number) | Represents a numeric value |
| [`Object`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object) | Represents the object that is the base of all JavaScript objects |
| [`parseFloat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) | Parses a string argument and returns a floating point number |
| [`parseInt`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/parseInt) | Parses a string argument and returns an integer of the specified radix |
| [`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise) | Represents the eventual completion (or failure) of an asynchronous operation, and its resulting value |
| [`Proxy`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Proxy) | Represents an object that is used to define custom behavior for fundamental operations (e.g. property lookup, assignment, enumeration, function invocation, etc) |
| [`RangeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RangeError) | Represents an error when a value is not in the set or range of allowed values |
| [`ReferenceError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) | Represents an error when a non-existent variable is referenced |
| [`Reflect`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Reflect) | Provides methods for interceptable JavaScript operations |
| [`RegExp`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RegExp) | Represents a regular expression, allowing you to match combinations of characters |
| [`Set`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Set) | Represents a collection of values, where each value may occur only once |
| [`setInterval`](https://developer.mozilla.org/docs/Web/API/setInterval) | Repeatedly calls a function, with a fixed time delay between each call |
| [`setTimeout`](https://developer.mozilla.org/docs/Web/API/setTimeout) | Calls a function or evaluates an expression after a specified number of milliseconds |
| [`SharedArrayBuffer`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) | Represents a generic, fixed-length raw binary data buffer |
| [`String`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String) | Represents a sequence of characters |
| [`Symbol`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Symbol) | Represents a unique and immutable data type that is used as the key of an object property |
| [`SyntaxError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError) | Represents an error when trying to interpret syntactically invalid code |
| [`TypeError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/TypeError) | Represents an error when a value is not of the expected type |
| [`Uint8Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) | Represents a typed array of 8-bit unsigned integers |
| [`Uint8ClampedArray`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray) | Represents a typed array of 8-bit unsigned integers clamped to 0-255 |
| [`Uint32Array`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array) | Represents a typed array of 32-bit unsigned integers |
| [`URIError`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/URIError) | Represents an error when a global URI handling function was used in a wrong way |
| [`URL`](https://developer.mozilla.org/docs/Web/API/URL) | Represents an object providing static methods used for creating object URLs |
| [`URLSearchParams`](https://developer.mozilla.org/docs/Web/API/URLSearchParams) | Represents a collection of key/value pairs |
| [`WeakMap`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakMap) | Represents a collection of key/value pairs in which the keys are weakly referenced |
| [`WeakSet`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WeakSet) | Represents a collection of objects in which each object may occur only once |
| [`WebAssembly`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly) | Provides access to WebAssembly |

## [Check if you're running on the Edge runtime](#check-if-you're-running-on-the-edge-runtime)

You can check if your function is running on the Edge runtime by checking the global `globalThis.EdgeRuntime` property. This can be helpful if you need to validate that your function is running on the Edge runtime in tests, or if you need to use a different API depending on the runtime.

```
if (typeof EdgeRuntime !== 'string') {
  // dead-code elimination is enabled for the code inside this block
}
```

## [Compatible Node.js modules](#compatible-node.js-modules)

The following modules can be imported with and without the `node:` prefix when using the `import` statement:

| Module | Description |
| --- | --- |
| [`async_hooks`](https://nodejs.org/api/async_hooks.html) | Manage asynchronous resources lifecycles with `AsyncLocalStorage`. Supports the [WinterCG subset](https://github.com/wintercg/proposal-common-minimum-api/blob/main/asynclocalstorage.md) of APIs |
| [`events`](https://nodejs.org/api/events.html) | Facilitate event-driven programming with custom event emitters and listeners. This API is fully supported |
| [`buffer`](https://nodejs.org/api/buffer.html) | Efficiently manipulate binary data using fixed-size, raw memory allocations with `Buffer`. Every primitive compatible with `Uint8Array` accepts `Buffer` too |
| [`assert`](https://nodejs.org/api/assert.html) | Provide a set of assertion functions for verifying invariants in your code |
| [`util`](https://nodejs.org/api/util.html) | Offer various utility functions where we include `promisify`/`callbackify` and `types` |

Also, `Buffer` is globally exposed to maximize compatibility with existing Node.js modules.

## [Unsupported APIs](#unsupported-apis)

The Edge runtime has some restrictions including:

*   Some Node.js APIs other than the ones listed above are not supported. For example, you can't read or write to the filesystem
*   `node_modules` _can_ be used, as long as they implement ES Modules and do not use native Node.js APIs
*   Calling `require` directly is not allowed. Use `import` instead

The following JavaScript language features are disabled, and will not work:

| API | Description |
| --- | --- |
| [`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval) | Evaluates JavaScript code represented as a string |
| [`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Creates a new function with the code provided as an argument |
| [`WebAssembly.compile`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/compile) | Compiles a WebAssembly module from a buffer source |
| [`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate) | Compiles and instantiates a WebAssembly module from a buffer source |

While `WebAssembly.instantiate` is supported in Edge Runtime, it requires the Wasm source code to be provided using the import statement. This means you cannot use a buffer or byte array to dynamically compile the module at runtime.

## [Environment Variables](#environment-variables)

You can use `process.env` to access [Environment Variables](/docs/environment-variables).

## [Many Node.js APIs are not available](#many-node.js-apis-are-not-available)

Middleware with the `edge` runtime configured is neither a Node.js nor browser application, which means it doesn't have access to all browser and Node.js APIs. Currently, our runtime offers a subset of browser APIs and some Node.js APIs and we plan to implement more functionality in the future.

In summary:

*   Use ES modules
*   Most libraries that use Node.js APIs as dependencies can't be used in Middleware with the `edge` runtime configured.
*   Dynamic code execution (such as `eval`) is not allowed (see the next section for more details)

## [Dynamic code execution leads to a runtime error](#dynamic-code-execution-leads-to-a-runtime-error)

Dynamic code execution is not available in Middleware with the `edge` runtime configured for security reasons. For example, the following APIs cannot be used:

| API | Description |
| --- | --- |
| [`eval`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/eval) | Evaluates JavaScript code represented as a string |
| [`new Function(evalString)`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Function) | Creates a new function with the code provided as an argument |
| [`WebAssembly.instantiate`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/WebAssembly/instantiate) | Compiles and instantiates a WebAssembly module from a buffer source |

You need to make sure libraries used in your Middleware with the `edge` runtime configured don't rely on dynamic code execution because it leads to a runtime error.

## [Maximum Execution Duration](#maximum-execution-duration)

Middleware with the `edge` runtime configured must begin sending a response within 25 seconds.

You may continue streaming a response beyond that time and you can continue with asynchronous workloads in the background, after returning the response.

## [Code size limit](#code-size-limit)

| Plan | Limit (after gzip compression) |
| --- | --- |
| Hobby | 1 MB |
| Pro | 2 MB |
| Enterprise | 4 MB |

The maximum size for an Vercel Function using the Edge runtime includes your JavaScript code, imported libraries and files (such as fonts), and all files bundled in the function.

If you reach the limit, make sure the code you are importing in your function is used and is not too heavy. You can use a package size checker tool like [bundle](https://bundle.js.org/) to check the size of a package and search for a smaller alternative.

## [Ignored Environment Variable Names](#ignored-environment-variable-names)

Environment Variables can be accessed through the `process.env` object. Since JavaScript objects have methods to allow some operations on them, there are limitations on the names of Environment Variables to avoid having ambiguous code.

The following names will be ignored as Environment Variables to avoid overriding the `process.env` object prototype:

*   `constructor`
*   `__defineGetter__`
*   `__defineSetter__`
*   `hasOwnProperty`
*   `__lookupGetter__`
*   `__lookupSetter__`
*   `isPrototypeOf`
*   `propertyIsEnumerable`
*   `toString`
*   `valueOf`
*   `__proto__`
*   `toLocaleString`

Therefore, your code will always be able to use them with their expected behavior:

```
// returns `true`, if `process.env.MY_VALUE` is used anywhere & defined in the Vercel dashboard
process.env.hasOwnProperty('MY_VALUE');
```

--------------------------------------------------------------------------------
title: "Using the Go Runtime with Vercel functions"
description: "Learn how to use the Go runtime to compile Go Vercel functions on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/go"
--------------------------------------------------------------------------------

# Using the Go Runtime with Vercel functions

Copy page

Ask AI about this page

Last updated October 27, 2025

The Go runtime is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

The Go runtime is used by Vercel to compile Go Vercel functions that expose a single HTTP handler, from a `.go` file within an `/api` directory at your project's root.

For example, define an `index.go` file inside an `/api` directory as follows:

/api/index.go

```
package handler
 
import (
  "fmt"
  "net/http"
)
 
func Handler(w http.ResponseWriter, r *http.Request) {
  fmt.Fprintf(w, "<h1>Hello from Go!</h1>")
}
```

An example `index.go` file inside an `/api` directory.

For advanced usage, such as using private packages with your Go projects, see the [Advanced Go Usage section](#advanced-go-usage).

The exported function needs to include the [`HandlerFunc`](https://golang.org/pkg/net/http/#HandlerFunc) signature type, but can use any valid Go exported function declaration as the function name.

## [Go Version](#go-version)

The Go runtime will automatically detect the `go.mod` file at the root of your Project to determine the version of Go to use.

If `go.mod` is missing or the version is not defined, the default version 1.20 will be used.

The first time the Go version is detected, it will be automatically downloaded and cached. Subsequent deployments using the same Go version will use the cached Go version instead of downloading it again.

## [Go Dependencies](#go-dependencies)

The Go runtime will automatically detect the `go.mod` file at the root of your Project to install dependencies.

## [Go Build Configuration](#go-build-configuration)

You can provide custom build flags by using the `GO_BUILD_FLAGS` [Environment Variable](/docs/environment-variables).

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "build": {
    "env": {
      "GO_BUILD_FLAGS": "-ldflags '-s -w'"
    }
  }
}
```

An example `-ldflags` flag with `-s -w`. This will remove debug information from the output file. This is the default value when no `GO_BUILD_FLAGS` are provided.

## [Advanced Go Usage](#advanced-go-usage)

In order to use this runtime, no configuration is needed. You only need to create a file inside the `api` directory.

The entry point of this runtime is a global matching `.go` files that export a function that implements the `http.HandlerFunc` signature.

### [Private Packages for Go](#private-packages-for-go)

To install private packages with `go get`, add an [Environment Variable](/docs/environment-variables) named `GIT_CREDENTIALS`.

The value should be the URL to the Git repo including credentials, such as `https://username:token@github.com`.

All major Git providers are supported including GitHub, GitLab, Bitbucket, as well as a self-hosted Git server.

With GitHub, you will need to [create a personal token](https://github.com/settings/tokens) with permission to access your private repository.

--------------------------------------------------------------------------------
title: "Using the Node.js Runtime with Vercel Functions"
description: "Learn how to use the Node.js runtime with Vercel Functions to create functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/node-js"
--------------------------------------------------------------------------------

# Using the Node.js Runtime with Vercel Functions

Copy page

Ask AI about this page

Last updated October 10, 2025

You can create Vercel Function in JavaScript or TypeScript by using the Node.js runtime. By default, the runtime builds and serves any function created within the `/api` directory of a project to Vercel.

[Node.js](/docs/functions/runtimes/node-js)\-powered functions are suited to computationally intense or large functions and provide benefits like:

*   More RAM and CPU power: For computationally intense workloads, or functions that have bundles up to 250 MB in size, this runtime is ideal
*   Complete Node.js compatibility: The Node.js runtime offers access to all Node.js APIs, making it a powerful tool for many applications

## [Creating a Node.js function](#creating-a-node.js-function)

In order to use the Node.js runtime, create a file inside the `api` directory with a function using the [`fetch` Web Standard export](/docs/functions/functions-api-reference?framework=other&language=ts#fetch-web-standard). No additional configuration is needed:

api/hello.ts

```
export default {
  fetch(request: Request) {
    return new Response('Hello from Vercel!');
  },
};
```

Alternatively, you can export each HTTP method as a separate export instead of using the `fetch` Web Standard export:

api/hello.ts

```
export function GET(request: Request) {
  return new Response('Hello from Vercel!');
}
```

To learn more about creating Vercel Functions, see the [Functions API Reference](/docs/functions/functions-api-reference). If you need more advanced behavior, such as a custom build step or private npm modules, see the [advanced Node.js usage page](/docs/functions/runtimes/node-js/advanced-node-configuration).

The entry point for `src` must be a glob matching `.js`, `.mjs`, or `.ts` files\*\* that export a default function.

## [Supported APIs](#supported-apis)

Vercel Functions using the Node.js runtime support [all Node.js APIs](https://nodejs.org/docs/latest/api/), including standard Web APIs such as the [Request and Response Objects](/docs/functions/runtimes/node-js#node.js-request-and-response-objects).

## [Node.js version](#node.js-version)

To learn more about the supported Node.js versions on Vercel, see [Supported Node.js Versions](/docs/functions/runtimes/node-js/node-js-versions).

## [Node.js dependencies](#node.js-dependencies)

For dependencies listed in a `package.json` file at the root of a project, the following behavior is used:

*   If `bun.lock` or `bun.lockb` is present, `bun install` is executed
*   If `yarn.lock` is present `yarn install` is executed
*   If `pnpm-lock.yaml` is present, `pnpm install` is executed
    *   See [supported package managers](/docs/package-managers#supported-package-managers) for pnpm detection details
*   If `package-lock.json` is present, `npm install` is executed
*   If `vlt-lock.json` is present, `vlt install` is executed
*   Otherwise, `npm install` is executed

If you need to select a specific version of a package manager, see [corepack](/docs/deployments/configure-a-build#corepack).

## [Using TypeScript with the Node.js runtime](#using-typescript-with-the-node.js-runtime)

The Node.js runtime supports files ending with `.ts` inside of the `/api` directory as TypeScript files to compile and serve when deploying.

An example TypeScript file that exports a Web signature handler is as follows:

api/hello.ts

```
export default {
  async fetch(request: Request) {
    const url = new URL(request.url);
    const name = url.searchParams.get('name') || 'World';
 
    return Response.json({ message: `Hello ${name}!` });
  },
};
```

You can use a `tsconfig.json` file at the root of your project to configure the TypeScript compiler. Most options are supported aside from ["Path Mappings"](https://www.typescriptlang.org/docs/handbook/module-resolution.html#path-mapping) and ["Project References"](https://www.typescriptlang.org/docs/handbook/project-references.html).

## [Node.js request and response objects](#node.js-request-and-response-objects)

Each request to a Node.js Vercel Function gives access to Request and Response objects. These objects are the [standard](https://nodejs.org/api/http.html#http_event_request) HTTP [Request](https://nodejs.org/api/http.html#http_class_http_incomingmessage) and [Response](https://nodejs.org/api/http.html#http_class_http_serverresponse) objects from Node.js.

### [Node.js helpers](#node.js-helpers)

Vercel additionally provides helper methods inside of the Request and Response objects passed to Node.js Vercel Functions. These methods are:

| method | description | object |
| --- | --- | --- |
| `request.query` | An object containing the request's [query string](https://en.wikipedia.org/wiki/Query_string), or `{}` if the request does not have a query string. | Request |
| `request.cookies` | An object containing the cookies sent by the request, or `{}` if the request contains no cookies. | Request |
| [`request.body`](#node.js-request-and-response-objects) | An object containing the body sent by the request, or `null` if no body is sent. | Request |
| `response.status(code)` | A function to set the status code sent with the response where `code` must be a valid [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Returns `response` for chaining. | Response |
| `response.send(body)` | A function to set the content of the response where `body` can be a `string`, an `object` or a `Buffer`. | Response |
| `response.json(obj)` | A function to send a JSON response where `obj` is the JSON object to send. | Response |
| `response.redirect(url)` | A function to redirect to the URL derived from the specified path with status code "307 Temporary Redirect". | Response |
| `response.redirect(statusCode, url)` | A function to redirect to the URL derived from the specified path, with specified [HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). | Response |

The following Node.js Vercel Function example showcases the use of `request.query`, `request.cookies` and `request.body` helpers:

api/hello.ts

```
import { VercelRequest, VercelResponse } from "@vercel/node";
 
module.exports = (request: VercelRequest, response: VercelResponse) => {
  let who = 'anonymous';
 
  if (request.body && request.body.who) {
    who = request.body.who;
  } else if (request.query.who) {
    who = request.query.who;
  } else if (request.cookies.who) {
    who = request.cookies.who;
  }
 
  response.status(200).send(`Hello ${who}!`);
};
```

Example Node.js Vercel Function using the `request.query`, `request.cookies`, and `request.body` helpers. It returns greetings for the user specified using `request.send()`.

If needed, you can opt-out of Vercel providing `helpers` using [advanced configuration](#disabling-helpers-for-node.js).

### [Request body](#request-body)

We populate the `request.body` property with a parsed version of the content sent with the request when possible.

We follow a set of rules on the `Content-type` header sent by the request to do so:

| `Content-Type` header | Value of `request.body` |
| --- | --- |
| No header | `undefined` |
| `application/json` | An object representing the parsed JSON sent by the request. |
| `application/x-www-form-urlencoded` | An object representing the parsed data sent by with the request. |
| `text/plain` | A string containing the text sent by the request. |
| `application/octet-stream` | A [Buffer](https://nodejs.org/api/buffer.html) containing the data sent by the request. |

With the `request.body` helper, you can build applications without extra dependencies or having to parse the content of the request manually.

The `request.body` helper is set using a [JavaScript getter](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Functions/get). In turn, it is only computed when it is accessed.

When the request body contains malformed JSON, accessing `request.body` will throw an error. You can catch that error by wrapping `request.body` with [`try...catch`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/try...catch):

api/hello.ts

```
try {
  request.body;
} catch (error) {
  return response.status(400).json({ error: 'My custom 400 error' });
}
```

Catching the error thrown by `request.body` with [`try...catch`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements/try...catch).

### [Cancelled Requests](#cancelled-requests)

Request cancellation must be enabled on a per-route basis. See [Functions API Reference](/docs/functions/functions-api-reference#cancel-requests) for more information.

You can listen for the `error` event on the request object to detect request cancellation:

api/cancel.ts

```
import { VercelRequest, VercelResponse } from '@vercel/node';
 
export default async (request: VercelRequest, response: VercelResponse) => {
  let cancelled = false;
  request.on('error', (error) => {
    if (error.message === 'aborted') {
      console.log('request aborted');
    }
    cancelled = true;
  });
 
  response.writeHead(200);
 
  for (let i = 1; i < 5; i++) {
    if (cancelled) {
      // the response must be explicitly ended
      response.end();
      return;
    }
 
    response.write(`Count: ${i}\n`);
 
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
 
  response.end('All done!');
};
```

## [Using Express with Vercel](#using-express-with-vercel)

Express.js is a popular framework used with Node.js. For information on how to use Express with Vercel, see the guide: [Using Express.js with Vercel](https://vercel.com/guides/using-express-with-vercel).

## [Using Node.js with middleware](#using-node.js-with-middleware)

The Node.js runtime can be used as an experimental feature to run middleware. To enable, add the flag to your `next.config.ts` file:

next.config.ts

TypeScript

TypeScriptJavaScript

```
import type { NextConfig } from 'next';
 
const nextConfig: NextConfig = {
  experimental: {
    nodeMiddleware: true,
  },
};
 
export default nextConfig;
```

Then in your middleware file, set the runtime to `nodejs` in the `config` object:

middleware.ts

TypeScript

TypeScriptJavaScript

```
export const config = {
  matcher: '/about/:path*',
  runtime: 'nodejs',
};
```

Running middleware on the Node.js runtime incurs charges under [Vercel Functions pricing](/docs/functions/usage-and-pricing#pricing). These functions only run using [Fluid compute](/docs/fluid-compute#fluid-compute).

--------------------------------------------------------------------------------
title: "Advanced Node.js Usage"
description: "Learn about advanced configurations for Vercel functions on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/node-js/advanced-node-configuration"
--------------------------------------------------------------------------------

# Advanced Node.js Usage

Copy page

Ask AI about this page

Last updated July 30, 2025

To use Node.js, create a file inside your project's `api` directory. No additional configuration is needed.

The entry point for `src` must be a glob matching `.js`, `.mjs`, or `.ts` files that export a default function.

### [Disabling helpers for Node.js](#disabling-helpers-for-node.js)

To disable [helpers](/docs/functions/runtimes/node-js#node.js-helpers):

1.  From the dashboard, select your project and go to the Settings tab.
2.  Select Environment Variables from the left side in settings.
3.  Add a new environment variable with the Key: `NODEJS_HELPERS` and the Value: `0`. You should ensure this is set for all environments you want to disable helpers for.
4.  Pull your env vars into your local project with the [following command](/docs/cli/env):
    
    terminal
    
    ```
    vercel env pull
    ```
    

For more information, see [Environment Variables](/docs/environment-variables).

### [Private npm modules for Node.js](#private-npm-modules-for-node.js)

To install private npm modules:

1.  From the dashboard, select your project and go to the Settings tab.
2.  Select Environment Variables from the left side in settings.
3.  Add a new environment variable with the Key: `NPM_TOKEN` and enter your [npm token](https://docs.npmjs.com/about-access-tokens) as the value. Alternatively, define `NPM_RC` as an [Environment Variable](/docs/environment-variables) with the contents of `~/.npmrc`.
4.  Pull your env vars into your local project with the [following command](/docs/cli/env):
    
    terminal
    
    ```
    vercel env pull
    ```
    

For more information, see [Environment Variables](/docs/environment-variables).

### [Custom build step for Node.js](#custom-build-step-for-node.js)

In some cases, you may wish to include build outputs inside your Vercel Function. To do this:

1.  Add a `vercel-build` script within your `package.json` file, in the same directory as your Vercel Function or any parent directory. The `package.json` nearest to the Vercel Function will be preferred and used for both installing and building:

package.json

```
{
  "scripts": {
    "vercel-build": "node ./build.js"
  }
}
```

1.  Create the build script named `build.js`:

build.js

```
const fs = require('fs');
fs.writeFile('built-time.js', `module.exports = '${new Date()}'`, (err) => {
  if (err) throw err;
  console.log('Build time file created successfully!');
});
```

1.  Finally, create a `.js` file for the built Vercel functions, `index.js` inside the `/api` directory:

api/index.js

```
const BuiltTime = require('./built-time');
module.exports = (request, response) => {
  response.setHeader('content-type', 'text/plain');
  response.send(`
    This Vercel Function was built at ${new Date(BuiltTime)}.
    The current time is ${new Date()}
  `);
};
```

### [SIGINT behavior](#sigint-behavior)

When a SIGINT signal is sent to a Node.js function, it will terminate every function running on that Fluid instance. When implementing graceful shutdown patterns in your Node.js functions, keep this instance-wide termination behavior in mind.

--------------------------------------------------------------------------------
title: "Supported Node.js versions"
description: "Learn about the supported Node.js versions on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/node-js/node-js-versions"
--------------------------------------------------------------------------------

# Supported Node.js versions

Copy page

Ask AI about this page

Last updated September 15, 2025

## [Default and available versions](#default-and-available-versions)

By default, a new project uses the latest Node.js LTS version available on Vercel.

Current available versions are:

*   22.x (default)
*   20.x

Only major versions are available. Vercel automatically rolls out minor and patch updates when needed, such as to fix a security issue.

## [Setting the Node.js version in project settings](#setting-the-node.js-version-in-project-settings)

To override the [default](#default-and-available-versions) version and set a different Node.js version for new deployments:

1.  From your dashboard, select your project.
2.  Select the Settings tab.
3.  On the Build and Deployment page, navigate to the Node.js Version section.
4.  Select the version you want to use from the dropdown. This Node.js version will be used for new deployments.

![Select your Node.js version in Project Settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fnode-version-light.png&w=1920&q=75)![Select your Node.js version in Project Settings.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Ffront%2Fdocs%2Ffunctions%2Fnode-version-dark.png&w=1920&q=75)

Select your Node.js version in Project Settings.

## [Version overrides in `package.json`](#version-overrides-in-package.json)

You can define the major Node.js version in the `engines#node` section of the `package.json` to override the one you have selected in the [Project Settings](#setting-the-node.js-version-in-project-settings):

package.json

```
{
  "engines": {
    "node": "22.x"
  }
}
```

For instance, when you set the Node.js version to 20.x in the Project Settings and you specify a valid [semver range](https://semver.org/) for Node.js 22 (e.g. `22.x`) in `package.json`, your project will be deployed with the latest 22.x version of Node.js.

The following table lists some example version ranges and the available Node.js version they map to:

| Version in `package.json` | Version deployed |
| --- | --- |
| `>=20.0.0`  
`>=18.0.0` | latest 22.x version |
| `22.x`  
`^22.0.0` | latest 22.x version |
| `20.x`  
`^20.0.0` | latest 20.x version |

## [Checking your deployment's Node.js version](#checking-your-deployment's-node.js-version)

To verify the Node.js version your Deployment is using, either run `node -v` in the Build Command or log `process.version`.

--------------------------------------------------------------------------------
title: "Using the Python Runtime with Vercel Functions"
description: "Learn how to use the Python runtime to compile Python Vercel Functions on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/python"
--------------------------------------------------------------------------------

# Using the Python Runtime with Vercel Functions

Copy page

Ask AI about this page

Last updated October 27, 2025

The Python runtime is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

The Python runtime enables you to write Python code, including using [FastAPI](https://vercel.com/new/git/external?repository-url=https://github.com/vercel/examples/tree/main/python/fastapi), [Django](https://vercel.com/new/git/external?repository-url=https://github.com/vercel/examples/tree/main/python/django), and [Flask](https://vercel.com/new/git/external?repository-url=https://github.com/vercel/examples/tree/main/python/flask), with Vercel Functions.

You can create your first function, available at the `/api` route, as follows:

api/index.py

```
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
```

A hello world Python API using Vercel functions.

## [Python version](#python-version)

The current available version is Python 3.12. This cannot be changed.

## [Dependencies](#dependencies)

You can install dependencies for your Python projects by defining them in a `pyproject.toml` with or without a corresponding `uv.lock`, `requirements.txt`, or a `Pipfile` with corresponding `Pipfile.lock`.

requirements.txt

```
fastapi==0.117.1
```

An example `requirements.txt` file that defines `FastAPI` as a dependency.

pyproject.toml

```
[project]
name = "my-python-api"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.117.1",
]
```

An example `pyproject.toml` file that defines `FastAPI` as a dependency.

## [Streaming Python functions](#streaming-python-functions)

Vercel Functions support streaming responses when using the Python runtime. This allows you to render parts of the UI as they become ready, letting users interact with your app before the entire page finishes loading.

## [Controlling what gets bundled](#controlling-what-gets-bundled)

By default, Python Vercel Functions include all files from your project that are reachable at build time. Unlike the Node.js runtime, there is no automatic tree-shaking to remove dead code or unused dependencies.

You should make sure your `pyproject.toml` or `requirements.txt` only lists packages necessary for runtime and you should also explicitly exclude files you don't need in your functions to keep bundles small and avoid hitting size limits.

Python functions have a maximum uncompressed bundle size of **250 MB**. See the [bundle size limits](/docs/functions/limitations#bundle-size-limits).

To exclude unnecessary files (for example: tests, static assets, and test data), configure `excludeFiles` in `vercel.json` under the `functions` key. The pattern is a [glob](https://github.com/isaacs/node-glob#glob-primer) relative to your project root.

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "functions": {
    "api/**/*.py": {
      "excludeFiles": "{tests/**,__tests__/**,**/*.test.py,**/test_*.py,fixtures/**,__fixtures__/**,testdata/**,sample-data/**,static/**,assets/**}"
    }
  }
}
```

Exclude common development and static folders from all Python functions to stay under the 250 MB bundle limit.

## [Using FastAPI with Vercel](#using-fastapi-with-vercel)

FastAPI is a modern, high-performance, web framework for building APIs with Python. For information on how to use FastAPI with Vercel, review this [guide](/docs/frameworks/backend/fastapi).

## [Using Flask with Vercel](#using-flask-with-vercel)

Flask is a lightweight WSGI web application framework. For information on how to use Flask with Vercel, review this [guide](/docs/frameworks/backend/flask).

## [Other Python Frameworks](#other-python-frameworks)

For FastAPI, Flask, or basic usage of the Python runtime, no configuration is required. Usage of the Python runtime with other frameworks, including Django, requires some configuration.

The entry point of this runtime is a glob matching `.py` source files with one of the following variables defined:

*   `handler` that inherits from the `BaseHTTPRequestHandler` class
*   `app` that exposes a WSGI or ASGI Application

### [Reading Relative Files in Python](#reading-relative-files-in-python)

Python uses the current working directory when a relative file is passed to [open()](https://docs.python.org/3/library/functions.html#open).

The current working directory is the base of your project, not the `api/` directory.

For example, the following directory structure:

directory

```
├── README.md
├── api
|  ├── user.py
├── data
|  └── file.txt
└── requirements.txt
```

With the above directory structure, your function in `api/user.py` can read the contents of `data/file.txt` in a couple different ways.

You can use the path relative to the project's base directory.

api/user.py

```
from http.server import BaseHTTPRequestHandler
from os.path import join
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        with open(join('data', 'file.txt'), 'r') as file:
          for line in file:
            self.wfile.write(line.encode())
        return
```

Or you can use the path relative to the current file's directory.

api/user.py

```
from http.server import BaseHTTPRequestHandler
from os.path import dirname, abspath, join
dir = dirname(abspath(__file__))
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        with open(join(dir, '..', 'data', 'file.txt'), 'r') as file:
          for line in file:
            self.wfile.write(line.encode())
        return
```

### [Web Server Gateway Interface](#web-server-gateway-interface)

The Web Server Gateway Interface (WSGI) is a calling convention for web servers to forward requests to web applications written in Python. You can use WSGI with frameworks such as Flask or Django.

*   [Deploy an example with Flask](https://vercel.com/new/git/external?repository-url=https://github.com/vercel/examples/tree/main/python/flask)
*   [Deploy an example with Django](https://vercel.com/new/git/external?repository-url=https://github.com/vercel/examples/tree/main/python/django)

### [Asynchronous Server Gateway Interface](#asynchronous-server-gateway-interface)

The Asynchronous Server Gateway Interface (ASGI) is a calling convention for web servers to forward requests to asynchronous web applications written in Python. You can use ASGI with frameworks such as [Sanic](https://sanic.readthedocs.io).

Instead of defining a `handler`, define an `app` variable in your Python file.

For example, define a `api/index.py` file as follows:

api/index.py

```
from sanic import Sanic
from sanic.response import json
app = Sanic()
 
 
@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
```

An example `api/index.py` file, using Sanic for a ASGI application.

Inside `requirements.txt` define:

requirements.txt

```
sanic==19.6.0
```

An example `requirements.txt` file, listing `sanic` as a dependency.

--------------------------------------------------------------------------------
title: "Using the Ruby Runtime with Vercel Functions"
description: "Learn how to use the Ruby runtime to compile Ruby Vercel Functions on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/ruby"
--------------------------------------------------------------------------------

# Using the Ruby Runtime with Vercel Functions

Copy page

Ask AI about this page

Last updated October 27, 2025

The Ruby runtime is available in [Beta](/docs/release-phases#beta) on [all plans](/docs/plans)

The Ruby runtime is used by Vercel to compile Ruby Vercel functions that define a singular HTTP handler from `.rb` files within an `/api` directory at your project's root.

Ruby files must have one of the following variables defined:

*   `Handler` proc that matches the `do |request, response|` signature.
*   `Handler` class that inherits from the `WEBrick::HTTPServlet::AbstractServlet` class.

For example, define a `index.rb` file inside a `/api` directory as follows:

api/index.rb

```
require 'cowsay'
 
Handler = Proc.new do |request, response|
  name = request.query['name'] || 'World'
 
  response.status = 200
  response['Content-Type'] = 'text/text; charset=utf-8'
  response.body = Cowsay.say("Hello #{name}", 'cow')
end
```

An example `index.rb` file inside an `/api` directory.

Inside a `Gemfile` define:

Gemfile

```
source "https://rubygems.org"
 
gem "cowsay", "~> 0.3.0"
```

An example `Gemfile` file that defines `cowsay` as a dependency.

## [Ruby Version](#ruby-version)

New deployments use Ruby 3.3.x as the default version.

You can specify the version of Ruby by defining `ruby` in a `Gemfile`, like so:

Gemfile

```
source "https://rubygems.org"
ruby "~> 3.3.x"
```

If the patch part of the version is defined, like `3.3.1` it will be ignored and assume the latest `3.3.x`.

## [Ruby Dependencies](#ruby-dependencies)

This runtime supports installing dependencies defined in the `Gemfile`. Alternatively, dependencies can be vendored with the `bundler install --deployment` command (useful for gems that require native extensions). In this case, dependencies are not built on deployment.

--------------------------------------------------------------------------------
title: "Using WebAssembly (Wasm)"
description: "Learn how to use WebAssembly (Wasm) to enable low-level languages to run on Vercel Functions and Routing Middleware."
last_updated: "null"
source: "https://vercel.com/docs/functions/runtimes/wasm"
--------------------------------------------------------------------------------

# Using WebAssembly (Wasm)

Copy page

Ask AI about this page

Last updated October 27, 2025

[WebAssembly](https://webassembly.org), or Wasm, is a portable, low-level, assembly-like language that can be used as a compilation target for languages like C, Go, and Rust. Wasm was built to run more efficiently on the web and _alongside_ JavaScript, so that it runs in most JavaScript virtual machines.

With Vercel, you can use Wasm in [Vercel Functions](/docs/functions) or [Routing Middleware](/docs/routing-middleware) when the runtime is set to [`edge`](/docs/functions/runtimes/edge), [`nodejs`](/docs/functions/runtimes/node-js), or [`bun`](/docs/functions/runtimes/bun#configuring-the-runtime).

Pre-compiled WebAssembly can be imported with the `?module` suffix. This will provide an array of the Wasm data that can be instantiated using `WebAssembly.instantiate()`.

While `WebAssembly.instantiate` is supported in Edge Runtime, it requires the Wasm source code to be provided using the import statement. This means you cannot use a buffer or byte array to dynamically compile the module at runtime.

## [Using a Wasm file](#using-a-wasm-file)

You can use Wasm in your production deployment or locally, using [`vercel dev`](/docs/cli/dev).

1.  ### [Get your Wasm file ready](#get-your-wasm-file-ready)
    
    *   Compile your existing C, Go, and Rust project to create a binary `.wasm` file. For this example, we use a [rust](https://github.com/vercel/next.js/blob/canary/examples/with-webassembly/src/add.rs) function that adds one to any number.
    *   Copy the compiled file (in our example, [`add.wasm`](https://github.com/vercel/next.js/blob/canary/examples/with-webassembly/add.wasm)) to the root of your Next.js project. If you're using Typescript, add a `ts` definition for the function such as [add.wasm.d.ts](https://github.com/vercel/next.js/blob/canary/examples/with-webassembly/add.wasm.d.ts).
2.  ### [Create an API route for calling the Wasm file](#create-an-api-route-for-calling-the-wasm-file)
    
    With `nodejs` runtime that uses [Fluid compute](/docs/fluid-compute) by default:
    
    api/wasm/route.ts
    
    ```
    import path from 'node:path';
    import fs from 'node:fs';
    import type * as addWasmModule from '../../../add.wasm'; // import type definitions at the root of your project
     
    const wasmBuffer = fs.readFileSync(path.resolve(process.cwd(), './add.wasm')); // path from root
    const wasmPromise = WebAssembly.instantiate(wasmBuffer);
     
    export async function GET(request: Request) {
      const url = new URL(request.url);
      const num = Number(url.searchParams.get('number') || 10);
      const { add_one: addOne } = (await wasmPromise).instance
        .exports as typeof addWasmModule;
     
      return new Response(`got: ${addOne(num)}`);
    }
    ```
    
3.  ### [Call the Wasm endpoint](#call-the-wasm-endpoint)
    
    *   Run the project locally with `vercel dev`
    *   Browse to `http://localhost:3000/api/wasm?number=12` which should return `got: 13`

--------------------------------------------------------------------------------
title: "Streaming"
description: "Learn how to stream responses from Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/streaming-functions"
--------------------------------------------------------------------------------

# Streaming

Copy page

Ask AI about this page

Last updated September 5, 2025

AI providers can be slow when producing responses, but many make their responses available in chunks as they're processed. Streaming enables you to show users those chunks of data as they arrive rather than waiting for the full response, improving the perceived speed of AI-powered apps.

Vercel recommends using [Vercel's AI SDK](https://sdk.vercel.ai/docs) to stream responses from LLMs and AI APIs. It reduces the boilerplate necessary for streaming responses from AI providers and allows you to change AI providers with a few lines of code, rather than rewriting your entire application.

## [Getting started](#getting-started)

The following example shows how to send a message to one of OpenAI's models and streams:

### [Prerequisites](#prerequisites)

1.  You should understand how to setup a Vercel Function. See the [Functions quickstart](/docs/functions/quickstart) for more information.
2.  You should also have a fundamental understanding of how streaming works on Vercel. To learn more see [What is streaming?](/docs/fundamentals/what-is-streaming).
3.  You should be using Node.js 20 or later and the [latest version](/docs/cli#updating-vercel-cli) of the Vercel CLI.
4.  You should copy your OpenAI API key in the `.env.local` file with name `OPENAI_API_KEY`. See the [AI SDK docs](https://sdk.vercel.ai/docs/getting-started#configure-openai-api-key) for more information on how to do this.
5.  Install the `ai` and `@ai-sdk/openai` packages:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i ai openai
    ```
    

Next.js (/app)Next.js (/pages)Other frameworks

app/api/streaming-example/route.ts

TypeScript

TypeScriptJavaScript

```
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';
 
// This method must be named GET
export async function GET() {
  // Make a request to OpenAI's API based on
  // a placeholder prompt
  const response = streamText({
    model: openai('gpt-4o-mini'),
    messages: [{ role: 'user', content: 'What is the capital of Australia?' }],
  });
  // Respond with the stream
  return response.toTextStreamResponse({
    headers: {
      'Content-Type': 'text/event-stream',
    },
  });
}
```

## [Function duration](#function-duration)

If your workload requires longer durations, you should consider enabling [fluid compute](/docs/fluid-compute), which has [higher default max durations and limits across plans](/docs/fluid-compute#default-settings-by-plan).

Maximum durations can be configured for Node.js functions to enable streaming responses for longer periods. See [max durations](/docs/functions/limitations#max-duration) for more information.

## [Streaming Python functions](#streaming-python-functions)

You can stream responses from Vercel Functions that use the Python runtime.

When your function is streaming, it will be able to take advantage of the extended [runtime logs](/docs/functions/logs#runtime-logs), which will show you the real-time output of your function, in addition to larger and more frequent log entries. Because of this potential increase in frequency and format, your [Log Drains](/docs/drains) may be affected. We recommend ensuring that your ingestion can handle both the new format and frequency.

## [More resources](#more-resources)

*   [What is streaming?](/docs/functions/streaming)
*   [AI SDK](https://sdk.vercel.ai/docs/getting-started)
*   [Vercel Functions](/docs/functions)
*   [Fluid compute](/docs/fluid-compute)
*   [Streaming and SEO: Does streaming affect SEO?](/guides/does-streaming-affect-seo)
*   [Processing data chunks: Learn how to process data chunks](/guides/processing-data-chunks)
*   [Handling backpressure: Learn how to handle backpressure](/guides/handling-backpressure)

--------------------------------------------------------------------------------
title: "Fluid compute pricing"
description: "Learn about usage and pricing for fluid compute on Vercel."
last_updated: "null"
source: "https://vercel.com/docs/functions/usage-and-pricing"
--------------------------------------------------------------------------------

# Fluid compute pricing

Copy page

Ask AI about this page

Last updated September 23, 2025

Vercel Functions on fluid compute are priced based on your plan and resource usage. Each plan includes a set amount of resources per month:

| Resource | Hobby | Pro |
| --- | --- | --- |
| [Active CPU](#active-cpu-1) | 4 hours included | N/A |
| _On-demand Active CPU_ | \- | Costs vary by [region](#regional-pricing) |
| [Provisioned Memory](#provisioned-memory-1) | 360 GB-hrs included | N/A |
| _On-demand Provisioned Memory_ | \- | Costs vary by [region](#regional-pricing) |
| [Invocations](#invocations-1) | 1 million included | N/A |
| _On-demand Invocations_ | \- | $0.60 per million |

Enterprise plans have custom terms. Speak to your Customer Success Manager (CSM) or Account Executive (AE) for details.

### [Resource Details](#resource-details)

#### [Active CPU](#active-cpu)

*   This is the CPU time your code actively consumes in milliseconds
*   You are only billed during actual code execution and not during I/O operations (database queries, ike AI model calls , etc.)
*   Billed per CPU-hour
*   Pauses billing when your code is waiting for external services

For example: If your function takes 100ms to process data but spends 400ms waiting for a database query, you're only billed for the 100ms of active CPU time. This means computationally intensive tasks (like image processing) will use more CPU time than I/O-heavy tasks (like making API calls).

#### [Provisioned Memory](#provisioned-memory)

*   Memory allocated to your function instances (in GB)
*   Billed for the entire instance lifetime in GB-hours
*   Continues billing while handling requests, even during I/O operations
*   Each instance can handle multiple requests with [optimized concurrency](/docs/fluid-compute#optimized-concurrency)
*   Memory is reserved for your function even when it's waiting for I/O
*   Billing continues until the last in-flight request completes

For example: If you have a 1GB function instance running for 1 hour handling multiple requests, you're billed for 1 GB-hour of provisioned memory, regardless of how many requests it processed or how much of that hour was spent waiting for I/O.

#### [Invocations](#invocations)

*   Counts each request to your function
*   Billed per incoming request
*   First million requests included in both Hobby and Pro plans
*   Counts regardless of request success or failure

For example: If your function receives 1.5 million requests on a Pro plan, you'll be billed for the 500,000 requests beyond your included million at $0.60 per million (approximately $0.30).

## [Regional pricing](#regional-pricing)

The following table shows the regional pricing for fluid compute resources on Vercel. The prices are per hour for CPU and per GB-hr for memory:

| Region | Active CPU time (per hour) | Provisioned Memory (GB-hr) |
| --- | --- | --- |
| Washington, D.C., USA (iad1) | $0.128 | $0.0106 |
| Cleveland, USA (cle1) | $0.128 | $0.0106 |
| San Francisco, USA (sfo1) | $0.177 | $0.0147 |
| Portland, USA (pdx1) | $0.128 | $0.0106 |
| Cape Town, South Africa (cpt1) | $0.200 | $0.0166 |
| Hong Kong (hkg1) | $0.176 | $0.0146 |
| Mumbai, India (bom1) | $0.140 | $0.0116 |
| Osaka, Japan (kix1) | $0.202 | $0.0167 |
| Seoul, South Korea (icn1) | $0.169 | $0.0140 |
| Singapore (sin1) | $0.160 | $0.0133 |
| Sydney, Australia (syd1) | $0.180 | $0.0149 |
| Tokyo, Japan (hnd1) | $0.202 | $0.0167 |
| Frankfurt, Germany (fra1) | $0.184 | $0.0152 |
| Dublin, Ireland (dub1) | $0.168 | $0.0139 |
| London, UK (lhr1) | $0.177 | $0.0146 |
| Paris, France (cdg1) | $0.177 | $0.0146 |
| Stockholm, Sweden (arn1) | $0.160 | $0.0133 |
| Dubai, UAE (dxb1) | $0.185 | $0.0153 |
| São Paulo, Brazil (gru1) | $0.221 | $0.0183 |

## [How pricing works](#how-pricing-works)

A function instance runs in a region, and its pricing is based on the resources it uses in that region. The cost for each invocation is calculated based on the Active CPU and Provisioned memory resources it uses in that region.

When the first request arrives, Vercel starts an instance with your configured memory. Provisioned memory is billed continuously until the last in-flight request finishes. Active CPU is billed only while your code is actually running. If the request is waiting on I/O, CPU billing pauses but memory billing continues.

After all requests complete, the instance is paused, and no CPU or memory charges apply until the next invocation. This means, you pay for memory whenever work is in progress, never for idle CPU, and nothing at all between requests.

### [Example](#example)

Suppose you deploy a function with 4 GB of memory in the São Paulo, Brazil region, where the rates are $0.221/hour for CPU and $0.0183/GB-hour for memory. If one request takes 4 seconds of active CPU time and the instance is alive for 10 seconds (including I/O), the cost will be:

*   CPU: (4 seconds / 3600) × $0.221 = $0.0002456
*   Memory: (4 GB × 10 seconds / 3600) × $0.0183 = $0.0002033
*   Total: $0.0002456 + $0.0002033 = $0.0004489 for each invocation.

--------------------------------------------------------------------------------
title: "Legacy Usage & Pricing for Functions"
description: "Learn about legacy usage and pricing for Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/functions/usage-and-pricing/legacy-pricing"
--------------------------------------------------------------------------------

# Legacy Usage & Pricing for Functions

Copy page

Ask AI about this page

Last updated September 24, 2025

Legacy Billing Model: This page describes the legacy billing model and relates to functions which **do not** use Fluid Compute. All new projects use [Fluid Compute](/docs/fluid-compute) by default, which bills separately for active CPU time and provisioned memory time for more cost-effective and transparent pricing.

Functions using the Node.js runtime are measured in [GB-hours](/docs/limits/usage#execution), which is the [memory allocated](/docs/functions/configuring-functions/memory) for each Function in GB, multiplied by the time in hours they were running. For example, a function [configured](/docs/functions/configuring-functions/memory) to use 3GB of memory that executes for 1 second, would be billed at 3 GB-s, requiring 1,200 executions to reach a full GB-Hr.

A function can use up to 50 ms of CPU time per execution unit. If a function uses more than 50 ms, it will be divided into multiple 50 ms units for billing purposes.

See [viewing function usage](#viewing-function-usage) for more information on how to track your usage.

## [Pricing](#pricing)

This information relates to functions which **do not** use Fluid Compute. Fluid Compute is the default for all new functions. To learn about pricing for functions that use Fluid Compute, see [Pricing](/docs/functions/usage-and-pricing).

The following table outlines the price for functions which do not use [Fluid Compute](/docs/fluid-compute).

Vercel Functions are available for free with the included usage limits:

| Resource | Hobby Included | Pro Included | On-demand with Pro |
| --- | --- | --- | --- |
| Function Duration | First 100 GB-Hours | N/A | $0.18 per 1 GB-Hour |
| Function Invocations | First 100,000 | N/A | $0.60 per 1,000,000 Invocations |

### [Hobby](#hobby)

Vercel will send you emails as you are nearing your usage limits. On the Hobby plan you will not pay for any additional usage. However, your account may be paused if you do exceed the limits.

When your [Hobby team](/docs/plans/hobby) is set to paused, it remains in this state indefinitely unless you take action. This means all new and existing [deployments](/docs/deployments) will be paused.

If you have reached this state, your application is likely a good candidate for a [Pro account](/docs/plans/pro).

To unpause your account, you have two main options:

*   Contact Support: You can reach out to our [support team](/help) to discuss the reason for the pause and potential resolutions
*   Transfer to a Pro team: If your Hobby team is paused, you won't have the option to initiate a [Pro trial](/docs/plans/pro-plan/trials). Instead, you can set up a Pro team:
    1.  [Create a Pro team account](/docs/accounts/create-a-team)
    2.  Add a valid credit card to this account. Select the Settings tab, then select Billing and Payment Method

Once set up, a transfer modal will appear, prompting you to [transfer your previous Hobby projects](/docs/projects/overview#transferring-a-project) to this new team. After transferring, you can continue with your projects as usual.

### [Pro](#pro)

For teams on a Pro trial, the [trial will end](/docs/plans/pro/trials#post-trial-decision) when your team reaches the [trial limits](/docs/plans/pro/trials#trial-limitations).

Once your team exceeds the included usage, you will continue to be charged the on-demand costs going forward.

Pro teams can [set up Spend Management](/docs/spend-management#managing-your-spend-amount) to get notified or to automatically take action, such as [using a webhook](/docs/spend-management#configuring-a-webhook) or pausing your projects when your usage hits a set spend amount.

### [Enterprise](#enterprise)

Enterprise agreements provide custom usage and pricing for Vercel Functions, including:

*   Custom [execution units](/docs/functions/runtimes/edge/edge-functions#managing-execution-units)
*   Increased [maximum duration](/docs/functions/configuring-functions/duration) up to 900 seconds
*   Multi-region deployments
*   [Vercel Function failover](/docs/functions/configuring-functions/region#automatic-failover)

See [Vercel Enterprise plans](/docs/plans/enterprise) for more information.

## [Viewing Function Usage](#viewing-function-usage)

Usage metrics can be found in the [Usage tab](/dashboard/usage) on your [dashboard](/dashboard). Functions are invoked for every request that is served.

You can see the usage for functions using the Node.js runtime on the Serverless Functions section of the Usage tab.

| Metric | Description | Priced | Optimize |
| --- | --- | --- | --- |
| Function Invocations | The number of times your Functions have been invoked | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](#optimizing-function-invocations) |
| Function Duration | The time your Vercel Functions have spent responding to requests | [Yes](/docs/pricing#managed-infrastructure-billable-resources) | [Learn More](#optimizing-function-duration) |
| Throttling | The number of instances where Functions did not execute due to concurrency limits being reached | No | N/A |

## [Managing function invocations](#managing-function-invocations)

You are charged based on the number of times your [functions](/docs/functions) are invoked, including both successful and errored invocations, excluding cache hits. The number of invocations is calculated by the number of times your function is called, regardless of the response status code.

When using [Incremental Static Regeneration](/docs/incremental-static-regeneration) with Next.js, both the `revalidate` option for `getStaticProps` and `fallback` for `getStaticPaths` will result in a Function invocation on revalidation, not for every user request.

When viewing your Functions Invocations graph, you can group by Ratio to see a total of all invocations across your team's projects that finished successfully, errored, or timed out.

Executing a Vercel Function will increase Edge Request usage as well. Caching your Vercel Function reduces the GB-hours of your functions but does not reduce the Edge Request usage that comes with executing it.

### [Optimizing function invocations](#optimizing-function-invocations)

*   Use the Projects option to identify which projects have the most invocations and where you can optimize.
*   Cache your responses using [edge caching](/docs/edge-network/caching#using-vercel-functions) and [Cache-Control headers](/docs/headers#cache-control-header) to reduce the number of invocations and speed up responses for users.
*   See [How can I reduce my Serverless Execution usage on Vercel?](https://vercel.com/guides/how-can-i-reduce-my-serverless-execution-usage-on-vercel) for more general information on how to reduce your Vercel functions usage.

## [Managing function duration](#managing-function-duration)

Legacy Billing Model: This describes the legacy Function duration billing model based on wall-clock time. For new projects, we recommend [Fluid Compute](/docs/functions/usage-and-pricing) which bills separately for active CPU time and provisioned memory time for more cost-effective and transparent pricing.

You are charged based on the duration your Vercel functions have run. This is sometimes called "[wall-clock time](/guides/what-are-gb-hrs-for-serverless-function-execution)", which refers to the _actual time_ elapsed during a process, similar to how you would measure time passing on a wall clock. It includes all time spent from start to finish of the process, regardless of whether that time was actively used for processing or spent waiting for a streamed response. Function Duration is calculated in [GB-Hours](/guides/what-are-gb-hrs-for-serverless-function-execution), which is the memory allocated for each Function in GB x the time in hours they were running.

For example, if a function [has](/docs/functions/configuring-functions/memory) 1.7 GB (1769 MB) of memory and is executed 1 million times at a 1-second duration:

*   Total Seconds: 1M \* (1s) = 1,000,000 Seconds
*   Total GB-Seconds: 1769/1024 GB \* 1,000,000 Seconds = 1,727,539.06 GB-Seconds
*   Total GB-Hrs: 1,727,539.06 GB-Seconds / 3600 = 479.87 GB-Hrs
*   The total Vercel Function Execution is 479.87 GB-Hrs.

To see your current usage, navigate to the Usage tab on your team's [Dashboard](/dashboard) and go to Serverless Functions > Duration. You can use the Ratio option to see the total amount of execution time across all projects within your team, including the completions, errors, and timeouts.

### [Optimizing function duration](#optimizing-function-duration)

Recommended: Upgrade to Fluid compute

*   Enable [Fluid compute](/docs/fluid-compute) for more cost-effective billing that separates active CPU time from provisioned memory time. This replaces the legacy wall-clock time billing model with transparent, usage-based pricing.

Legacy optimization strategies:

*   Use the Projects option to identify which projects have the most execution time and where you can optimize.
*   You can adjust the [maximum duration](/docs/functions/configuring-functions/duration) for your functions to prevent excessive run times.
*   To reduce the GB-hours (Execution) of your functions, ensure you are using [edge caching](/docs/edge-network/caching#using-vercel-functions) and Cache-Control headers. If using [Incremental Static Regeneration](/docs/incremental-static-regeneration), note that Vercel counts Function invocations on page revalidation towards both GB-hours and [Fast Origin Transfer](/docs/edge-network/manage-usage#fast-origin-transfer).
*   For troubleshooting issues causing functions to run longer than expected or timeout, see [What can I do about Vercel Serverless Functions timing out?](/guides/what-can-i-do-about-vercel-serverless-functions-timing-out)

## [Throttles](#throttles)

This counts the number of times that a request to your Functions could not be served because the [concurrency limit](/docs/functions/concurrency-scaling#automatic-concurrency-scaling) was hit.

While this is not a chargeable metric, it will cause a `503: FUNCTION_THROTTLED` error. To learn more, see [What should I do if I receive a 503 error on Vercel?](https://vercel.com/guides/what-should-i-do-if-i-receive-a-503-error-on-vercel).

--------------------------------------------------------------------------------
title: "Vercel fundamentals"
description: "Learn about the core concepts of Vercel"
last_updated: "null"
source: "https://vercel.com/docs/fundamentals"
--------------------------------------------------------------------------------

# Vercel fundamentals

Copy page

Ask AI about this page

Last updated July 18, 2025

The articles below outline key ideas that shape how Vercel handles computation and streaming:

*   [What is Compute?](/docs/fundamentals/what-is-compute): Explains how Vercel manages building, rendering, and on-demand tasks. Including:
    *   Dedicated servers vs. Vercel functions
    *   Cold starts, region models, and maximum durations
    *   Fluid compute
*   [What is Streaming?](/docs/fundamentals/what-is-streaming): Shows how to send data progressively from Vercel Functions using the Web Streams API. Including:
    *   Chunks, backpressure, and flow control
    *   Real-time use cases like AI responses or ecommerce updates
    *   Strategies to enhance perceived performance and responsiveness

--------------------------------------------------------------------------------
title: "What is Compute?"
description: "Learn about the different models for compute and how they can be used with Vercel."
last_updated: "null"
source: "https://vercel.com/docs/fundamentals/what-is-compute"
--------------------------------------------------------------------------------

# What is Compute?

Copy page

Ask AI about this page

Last updated September 15, 2025

## [Where does compute happen?](#where-does-compute-happen)

Traditionally with web applications, we talk about two main locations:

*   Client: This is the browser on your _user's_ device that sends a request to a server for your application code. It then turns the response it receives from the server into an interface the user can interact with. The term "client" could also be used for any device, including another server, that is making a request to a server.
*   Server: This is the computer in a data center that stores your application code. It receives requests from a client, does some computation, and sends back an appropriate response. This server does not sit in complete isolation; it is usually part of a bigger network designed to deliver your application to users around the world.
    *   Origin Server: The server that stores and runs the original version of your app code. When the origin server receives a request, it does some computation before sending a response. The result of this computation work may be cached by a CDN.
    *   CDN (Content Delivery Network): This stores static content, such as HTML, in multiple locations around the globe, placed between the client who is requesting and the origin server that is responding. When a user sends a request, the closest CDN will respond with its cached response.
    *   The Edge: The edge refers to the edge of the network, closest to the user. While CDNs could be part of the edge, which are also distributed around the world, some edge servers can also run code. This means that caching and code execution can be done at the edge, closer to the user. Vercel has its own [CDN](/docs/cdn), which runs middleware and stores build output assets globally.

![The request-response cycle between client and server.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Frequest-response.png&w=1200&q=75)![The request-response cycle between client and server.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Frequest-response-dark.png&w=1200&q=75)

The request-response cycle between client and server.

## [Compute in practice](#compute-in-practice)

To demonstrate an example of what this looks like in practice, we'll use the example of a Next.js app deployed to Vercel.

When you start a deployment of your Next.js app to Vercel, Vercel's [build process](/docs/deployments/builds#build-process) creates a build output, that contains artifacts such as [bundled Vercel Functions](/docs/functions/configuring-functions/advanced-configuration#bundling-vercel-functions) or static assets. It will then deploy either to Vercel's CDN or, in the case of a function, to a [specified region](/docs/functions/configuring-functions/region).

Now that the deployment is ready to serve traffic, a user can visit your site. When they do, the request is sent to the closest edge network region, which will then either serve the static assets or execute the function. The function will then run, and the response will be sent back to the user. At a very high-level this looks like:

1.  User Action: The user interacts with a website by clicking a link, submitting a form, or entering a URL.
2.  HTTP Request: The user's browser sends a request to the server, asking for the resources needed to display the webpage.
3.  Server Processing: The server receives the request, processes it, and prepares the necessary resources. For Vercel Functions, Vercel's [gateway](https://vercel.com/blog/behind-the-scenes-of-vercels-infrastructure) triggers a function execution in the region where the function was deployed.
4.  HTTP Response: The server sends back a response to the browser, which includes the requested resources and a status code indicating whether the request was successful. The browser then receives the response, interprets the resources, and displays the webpage to the user.

In this lifecycle, the "Server Processing" step can look very different depending on your needs, the artifacts being requested, and the model of compute that you use. In the next section we'll explore these models, each of which has their own tradeoffs.

## [Servers](#servers)

Servers provide a specific environment and resources for your applications. This means that you have control over the environment, but you also have to manage the infrastructure, provision servers, or upgrade hardware. How much control you have depends on the server option you choose. Some options might be: Amazon EC2, Azure Virtual Machines, or Google Compute Engine. All of these services provide you with a virtual machine that you'll configure through their site. You will be responsible for provisioning, and pay for the entire duration of the server's uptime. Other options such as Virtual Private Servers (VPS), dedicated physical servers in a data center, or your own on-premises servers are also considered traditional servers.

Managing your own servers can work well if you have a highly predictable workload. You don't have a need to scale up or down and you have a consistent amount of traffic. If you don't face peaks of traffic, the upside is predicable performance and cost, with complete control over the environment and security. The fact that the resource is always available means that you can run long-running processes.

### [Server advantages](#server-advantages)

Servers give you complete control to configure the environment to suit your needs. You can set the CPU power and RAM for consistent performance. They enable the execution of long-running processes and support applications that require persistent connections. Additionally, for businesses with predictable workloads, servers provide stable costs.

### [Server disadvantages](#server-disadvantages)

If you have peaks of traffic, you'll need to anticipate and provision additional resources in advance, which can lead to 2 possible scenarios:

*   Under provisioning: leads to degraded performance due to lack of compute availability.
*   Over provisioning: leads to increased costs due to wasted compute capacity.

Furthermore, because scaling resources can be slow, you will need to apply it in advance of the time where traffic peaks are expected.

## [Serverless](#serverless)

Serverless is a cloud computing model that allows you to build and run applications and services without having to manage your own servers. It addresses many of the disadvantages of traditional servers, and enables teams to have an infrastructure that is more elastic: resources that are scaled and available based on demand, and have a pricing structure that reflects that. Despite the name, servers are still used.

The term "Serverless" has been used by several cloud providers to describe the compute used for functions, such as AWS Lambda functions, Google Cloud Functions, Azure Functions, and Vercel Functions.

The difference between serverless and servers, is that there is no single server assigned to your application. Instead, when a request is made, a computing instance on a server is spun up to handle the request, and then spun down after the request is complete. This allows your app to handle unpredictable traffic with the benefit of only paying for what you use. You do not need to manage the infrastructure, provision servers, or upgrade hardware.

### [Serverless advantages](#serverless-advantages)

With serverless, applications are automatically scaled up or down based on demand, ensuring that resources are used efficiently and costs are optimized. Since this is done automatically, it reduces the complexity of infrastructure management. For workloads with unpredictable or variable traffic, the serverless model can be very cost-effective.

### [Serverless disadvantages](#serverless-disadvantages)

#### [Cold starts](#cold-starts)

When adding additional capacity to a serverless application there is a short period of initialization time that happens as the first request is received. This is called a _cold start_. When this capacity is reused the initialization no longer needs to happen and we refer to the function as _warm_.

Reusing a function means the underlying instance that hosts it does not get discarded. State, such as temporary files, memory caches, and sub-processes, are preserved. The developer is encouraged not just to minimize the time spent in the _booting_ process, but to also take advantage of caching data (in memory or filesystem) and [memoizing](https://en.wikipedia.org/wiki/Memoization) expensive computations.

By their very nature of being on-demand, serverless applications will always have the notion of cold starts.

With Vercel, pre-warmed instances are enabled for paid plans on production environments. This prevents cold starts by keeping a minimum of one active function instance running.

#### [Region model](#region-model)

Serverless compute typically happens in a single specified location (or [region](/docs/functions/regions)). Having a single region (or small number) makes it easier to increase the likelihood of a warm function as all of your users will be hitting the same instances. You'll likely also only have your data store in a single region, and so for latency reasons, it makes sense to have the trip between your compute and data be as short as possible.

However, a single region can be a disadvantage if you have user request coming from different region, as the response latency will be high.

All of this means that it's left up to teams to determine which region (or regions) they want Vercel to deploy their functions to. This requires taking into account latency between your compute and your data source, as well as latency to your users. In addition, region failover is not automatic, and requires [manual intervention](/docs/functions/configuring-functions/region#automatic-failover).

#### [High maximum duration](#high-maximum-duration)

AI-driven workloads have stretched the limits of serverless compute, through the requirement of long-running processes, data-intensive tasks, a requirement for streaming data, and the need for real-time interaction.

The maximum duration of a function describes the maximum amount of time that a function can run before it is terminated. As a user, you have to understand and configure the maximum duration, which is a balance between the cost of running the function and the time it takes to complete the task.

This can be a challenge, as you may not know how long a task will take to complete, and if you set the duration too low, the function will be terminated before it completes. If you set it too high, it can be a source of excessive execution costs.

## [Fluid compute](#fluid-compute)

Fluid compute is a hybrid approach between [serverless](#serverless) and [servers](#servers), and it builds upon the benefits of serverless computing, addresses its disadvantages and includes some of the strengths of servers, such as the ability to execute tasks concurrently within a single instance.

### [How does Fluid compute work](#how-does-fluid-compute-work)

In the serverless compute model, one serverless instance can process only one request at a time so that the number of instances needed can significantly increase if the traffic to a specific page increases. In many cases, the available resources in one instance are not fully used when processing a single request. This can lead to significant wasted resources that you still have to pay for.

![How multiple requests are processed in the traditional serverless compute model.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Fserverless-light.png&w=1920&q=75)![How multiple requests are processed in the traditional serverless compute model.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Fserverless-dark.png&w=1920&q=75)

How multiple requests are processed in the traditional serverless compute model.

In the Fluid compute model, when a request requires a function to be executed, a new compute instance is started if there are no existing instances processing this function. Additional requests will re-use the same instance as long as it is still processing existing requests and there is sufficient capacity available in the instance. We refer to this as _optimized concurrency_. It significantly decreases the number of instances that need to be running and increases the efficiency of an instance by fully utilising the available CPU, leading to reduced operational costs.

![How multiple requests are processed in the Fluid compute model with optimized concurrency.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Foptimized-concurrency-light.png&w=1920&q=75)![How multiple requests are processed in the Fluid compute model with optimized concurrency.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Ffluid%2Foptimized-concurrency-dark.png&w=1920&q=75)

How multiple requests are processed in the Fluid compute model with optimized concurrency.

### [Benefits of Fluid compute](#benefits-of-fluid-compute)

#### [Optimized concurrency](#optimized-concurrency)

Resource usage is optimized by handling multiple request with invocations in one function instance and dynamically routing traffic to instances based on load and availability. This can save significant costs compared to traditional serverless models.

#### [Reduction in cold starts](#reduction-in-cold-starts)

Optimized concurrency reduces the likelihood of [cold starts](#cold-starts), a disadvantage of serverless, as there is less chance that a new function instance needs to be initialized. However, it can still happen such as during periods of low traffic. Fluid compute improves cold start times with Bytecode caching and pre-warmed instances:

*   Bytecode caching: It automatically pre-compiles function code to minimize startup time during cold invocations.
*   Pre-warmed instances: It keeps functions ready to handle requests without cold start delays.

#### [Dynamic scaling](#dynamic-scaling)

Fluid compute includes one of the advantages of serverless with the ability of automatically adjusting the number of concurrent instances needed based on the demands of your traffic. Therefore, you don't have to worry about increased latency during high traffic events or pay for increased resource limits during low traffic times before and after high traffic events.

#### [Background processing](#background-processing)

Serverless computing is designed for quick tasks that are short-lived. With Fluid compute, you can execute background tasks with [`waitUntil`](/docs/functions/functions-api-reference/vercel-functions-package#waituntil) after having responded to the user's request, combining the ability to provide a responsive user experience with running time-consuming tasks like logging and analytics.

#### [Cross-region failover](#cross-region-failover)

Fluid compute includes backup regions where it can launch function instances and route traffic to in case of outages in the regions where your functions are normally executed. You also have the ability to specify multiple regions where your function instances should be deployed.

#### [Compute instance sharing](#compute-instance-sharing)

As opposed to traditional serverless where instances are completely isolated, Fluid compute allows multiple invocations to share the same physical instance (a global state/process) concurrently. With this approach, functions can share resources which improves performance and reduce costs.

### [Enabling Fluid compute](#enabling-fluid-compute)

You can enable Fluid compute from the [Functions Settings](https://vercel.com/d?to=/%5Bteam%5D/%5Bproject%5D/settings/functions%fluid-compute&title=Go+to+Function+Settings) section of your project. For more details, review [how to enable Fluid compute](/docs/fluid-compute).

--------------------------------------------------------------------------------
title: "Getting started with Vercel"
description: "This step-by-step tutorial will help you get started with Vercel, an end-to-end platform for developers that allows you to create and deploy your web application."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel"
--------------------------------------------------------------------------------

# Getting started with Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel is a platform for developers that provides the tools, workflows, and infrastructure you need to build and deploy your web apps faster, without the need for additional configuration.

Vercel supports [popular frontend frameworks](/docs/frameworks) out-of-the-box, and its scalable, secure infrastructure is globally distributed to serve content from data centers near your users for optimal speeds.

During development, Vercel provides tools for real-time collaboration on your projects such as automatic preview and production environments, and comments on preview deployments.

## [Before you begin](#before-you-begin)

To get started, create an account with Vercel. You can [select the plan](/docs/plans) that's right for you.

*   [Sign up for a new Vercel account](/signup)
*   [Log in to your existing Vercel account](/login)

Once you create an account, you can choose to authenticate either with a Git provider or by using an email. When using email authentication, you may need to confirm both your email address and a phone number.

## [Customizing your journey](#customizing-your-journey)

This tutorial is framework agnostic but Vercel supports many frontend [frameworks](/docs/frameworks/more-frameworks). As you go through the docs, the quickstarts will provide specific instructions for your framework. If you don't find what you need, give us feedback and we'll update them!

While many of our instructions use the dashboard, you can also use [Vercel CLI](/docs/cli) to carry out most tasks on Vercel. In this tutorial, look for the "Using CLI?" section for the CLI steps. To use the CLI, you'll need to install it:

pnpmyarnnpmbun

```
pnpm i -g vercel
```

[

Let's go

](/docs/getting-started-with-vercel/projects-deployments)

--------------------------------------------------------------------------------
title: "Buy a domain"
description: "Purchase your domain with Vercel. Expand your online reach and establish a memorable online identity."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/buy-domain"
--------------------------------------------------------------------------------

# Buy a domain

Copy page

Ask AI about this page

Last updated October 7, 2025

### Using CLI?

Use this snippet to purchase a new domain from Vercel:

terminal

```
vercel domains buy [domain]
```

Use Vercel to find and buy a domain that resonates with your brand, establishes credibility, and captures your visitors' attention.

All domains purchased on Vercel have WHOIS privacy enabled by default.

1.  ### [Find a domain](#find-a-domain)
    
    Go to [https://vercel.com/domains](/domains) and search for a domain that matches you or your brand. You could try "SuperDev"!
    
    ![Domains marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fbuy-domains-light.png&w=2048&q=75)![Domains marketplace](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fbuy-domains-dark.png&w=2048&q=75)
    
    Domains marketplace
    
    Depending on the TLD (top-level domain), you’ll see the purchase price. Domains with Premium badges are more expensive. You can sort the results by relevance (default), length, price, or alphabetical order.
    
2.  ### [Select your domain(s)](#select-your-domains)
    
    *   Select an address by clicking the button next to the available domain, or continue searching until you find the perfect one.
    *   When you click the button, Vercel adds the domain to your domains cart. You can continue to add more domains from the same results or search for new ones.
3.  ### [Purchase your domain(s)](#purchase-your-domains)
    
    *   Click on the Cart button on the top right and review the list of domains and prices that you added.
    *   Then, click Proceed to Checkout. You can also change the Team under which you are making this purchase at this stage.
4.  ### [Enter payment details and registrant information](#enter-payment-details-and-registrant-information)
    
    *   You'll need to enter your billing and credit card details to purchase the domain on the checkout page. These details are saved for [auto renewal](/docs/domains/renew-a-domain).
    *   You'll also need to enter your registrant information and confirm it for [ICANN](https://www.icann.org/) purposes.
    *   Click Buy to complete the purchase.
    
    For the ICANN registrant information:
    
    *   If you enter the same email address you use for your Vercel user account (or an email your [team Owner](/docs/rbac/access-roles#owner-role) uses), the information will be confirmed automatically.
        
    *   If you enter another email address, please follow the instructions you receive in an email to confirm your registrant information.
        
    
5.  ### [Configure your domain](#configure-your-domain)
    
    *   Once the purchase is complete, you can click Configure next to each purchased domain on the checkout page.
    *   You'll have the following options:
        *   Connect the domain to an existing project
        *   Create a new project to connect the domain to
        *   Manage the domain's DNS records
    
    You can also configure your domain from the [project's domains dashboard page](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fdomains&title=Go+to+your+project%27s+domain) by following the [Add and configure domain](/docs/domains/working-with-domains/add-a-domain) instructions.
    

## [Next steps](#next-steps)

Next, learn how to take advantage of Vercel's collaboration features as part of your developer workflow:

[

Use Vercel in your developer workflow

](/docs/getting-started-with-vercel/collaborate)

--------------------------------------------------------------------------------
title: "Collaborate on Vercel"
description: "Amplify collaboration and productivity with Vercel's CI/CD tools, such as Comments. Empower your team to build and deploy together seamlessly."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/collaborate"
--------------------------------------------------------------------------------

# Collaborate on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Collaboration is key in successful development projects, and Vercel offers robust features to enhance collaboration among developers. From seamless code collaboration to real-time previews with Comments, Vercel empowers your team to work together effortlessly.

## [Make Changes](#make-changes)

Now that your project is publicly available on your domain of choice, it’s time to begin making changes to it. With Vercel's automatic deployments, this won't require any extra effort. By default, when your Vercel project is connected to a Git repository, Vercel will deploy every commit that is pushed to the Git repository, regardless of which branch you're pushing it to.

A Production environment is one built from the `main` or development branch of your Git repository. A preview environment is created when you deploy from any other branch.

Vercel provides a [URL](/docs/deployments/generated-urls#generated-from-git) that reflects the latest pushes to that branch. You can find this either on your dashboard, or in a pull request, which you'll see in the next step

This connection was established for you automatically, so all you have to do is push commits, and you will start receiving links to deployments right on your Git provider.

## [Create a preview deployment](#create-a-preview-deployment)

1.  ### [Make your changes](#make-your-changes)
    
    Create a new branch in your project and make some changes
    
2.  ### [Commit your changes](#commit-your-changes)
    
    Commit those changes and create a pull request. After a few seconds, Vercel picks up the changes and starts to build and deploy your project. You can see the status of the build through the bot comment made on your PR:
    
    ![Vercel for GitHub deploying a pull request automatically.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fgithub-comment-light.png&w=1920&q=75)![Vercel for GitHub deploying a pull request automatically.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fgit%2Fgithub-comment-dark.png&w=1920&q=75)
    
    Vercel for GitHub deploying a pull request automatically.
    
3.  ### [Inspect your deployment information](#inspect-your-deployment-information)
    
    Select Inspect to explore the build within your dashboard. You can see the build is within the preview environment and additional information about the deployment including: [build information](/docs/deployments/builds), a [deployment summary](/docs/deployments#resources-tab-and-deployment-summary), checks, and [domain assignment](/docs/domains). These happen for every deployment
    
    ![Vercel dashboard showing the preview deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fpreview-dashboard-light.png&w=3840&q=75)![Vercel dashboard showing the preview deployment.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Fpreview-dashboard-dark.png&w=3840&q=75)
    
    Vercel dashboard showing the preview deployment.
    
4.  ### [View your deployment URL](#view-your-deployment-url)
    
    Return to your pull request. At this point your build should be deployed and you can select Visit Preview. You can now see your changes and share this preview URL with others.
    

## [Commenting on previews](#commenting-on-previews)

[Comments](/docs/comments) provide a way for your team [or friends](/docs/comments/how-comments-work#sharing) to give direct feedback on [preview deployments](/docs/deployments/environments#preview-environment-pre-production). Share with others by doing the following:

1.  ### [Open your deployment](#open-your-deployment)
    
    Open the preview deployment that you’d like to share by selecting the Domain from the deployment information as shown in step 3 above. Alternatively, you can find it by selecting your project from the [dashboard](/dashboard), and selecting the most recent commit under Active Branches:
    
    ![Active branch section showing all non-production branches](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Factive-branches-light.png&w=3840&q=75)![Active branch section showing all non-production branches](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fgetting-started-with-vercel%2Factive-branches-dark.png&w=3840&q=75)
    
    Active branch section showing all non-production branches
    
2.  ### [Authenticate with your Vercel account](#authenticate-with-your-vercel-account)
    
    From the Comments toolbar at the bottom of the screen, select Log in to comment and sign in with your Vercel account.
    
3.  ### [Adjust the share settings](#adjust-the-share-settings)
    
    Select Share in the [Toolbar](/docs/vercel-toolbar) menu. Add the emails of people you would like to share the preview with. If you are previewing a specific commit, you may have the option to share the preview for your branch instead. This option allows you to share a preview that updates with the latest commit to the branch.
    
    To learn more, including other ways to share, see [Sharing Deployments](/docs/deployments/sharing-deployments).
    
4.  ### [Collaborator needs to sign-in](#collaborator-needs-to-sign-in)
    
    The person you are sharing the preview with needs to have a Vercel account. To do so, they'll need to select Log in to comment and then enter their email address.
    
5.  ### [Collaborator can comment](#collaborator-can-comment)
    
    Once the person you are sharing the preview with goes through the security options, they'll be ready to comment. You'll be notified of new comments through email, or when you visit the deployment.
    

For more information on using Comments, see [Using comments](/docs/comments/using-comments).

[

What's next?

](/docs/getting-started-with-vercel/next-steps)

--------------------------------------------------------------------------------
title: "Add a domain"
description: "Easily add a custom domain to your Vercel project. Enhance your brand presence and optimize SEO with just a few clicks."
last_updated: "null"
source: "https://vercel.com/docs/getting-started-with-vercel/domains"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./10-frameworks-on-vercel.md) | [Index](./index.md) | [Next →](./12-add-a-domain.md)
