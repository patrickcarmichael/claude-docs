**Navigation:** [← Previous](./09-invalid-request-method.md) | [Index](./index.md) | [Next →](./11-supported-frameworks-on-vercel.md)

---

# Frameworks on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Vercel has first-class support for [a wide range of the most popular frameworks](/docs/frameworks/more-frameworks). You can build and deploy using frontend, backend, and full-stack frameworks ranging from SvelteKit to Nitro, often without any upfront configuration.

Learn how to [get started with Vercel](/docs/getting-started-with-vercel) or clone one of our example repos to your favorite git provider and deploy it on Vercel using one of the templates below:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your project.

Deploying on Vercel with one of our [supported frameworks](/docs/frameworks/more-frameworks) gives you access to many features, such as:

*   [Vercel Functions](/docs/functions) enable developers to write functions that scale based on traffic demands, preventing failures during peak hours and reducing costs during low activity.
*   [Middleware](/docs/routing-middleware) is code that executes before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Middleware is an effective way to personalize statically generated content.
*   [Multi-runtime Support](/docs/functions/runtimes) allows the use of various runtimes for your functions, each with unique libraries, APIs, and features tailored to different technical requirements.
*   [Incremental Static Regeneration](/docs/incremental-static-regeneration) enables content updates without redeployment. Vercel caches the page to serve it statically and rebuilds it on a specified interval.
*   [Speed Insights](/docs/speed-insights) provide data on your project's Core Web Vitals performance in the Vercel dashboard, helping you improve loading speed, responsiveness, and visual stability.
*   [Analytics](/docs/analytics) offer detailed insights into your website's performance over time, including metrics like top pages, top referrers, and user demographics.
*   [Skew Protection](/docs/skew-protection) uses version locking to ensure that the client and server use the same version of your application, preventing version skew and related errors.

## [Frameworks infrastructure support matrix](#frameworks-infrastructure-support-matrix)

The following table shows which features are supported by each framework on Vercel. The framework list represents the most popular frameworks deployed on Vercel.

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

## [Build Output API](#build-output-api)

The [Build Output API](/docs/build-output-api/v3) is a file-system-based specification for a directory structure that produces a Vercel deployment. It is primarily targeted at framework authors who want to integrate their frameworks with Vercel's platform features. By implementing this directory structure as the output of their build command, framework authors can utilize all Vercel platform features, such as Vercel Functions, Routing, and Caching.

If you are not using a framework, you can still use these features by manually creating and populating the `.vercel/output` directory according to this specification. Complete examples of Build Output API directories can be found in [vercel/examples](https://github.com/vercel/examples/tree/main/build-output-api), and you can read our [blog post](/blog/build-your-own-web-framework) on using the Build Output API to build your own framework with Vercel.

## [More resources](#more-resources)

Learn more about deploying your preferred framework on Vercel with the following resources:

*   [See a full list of supported frameworks](/docs/frameworks/more-frameworks)
*   [Explore our template marketplace](/templates)
*   [Learn about our deployment features](/docs/deployments)

--------------------------------------------------------------------------------
title: "Backends on Vercel"
description: "Vercel supports a wide range of the most popular backend frameworks, optimizing how your application builds and runs no matter what tooling you use."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend"
--------------------------------------------------------------------------------

# Backends on Vercel

Copy page

Ask AI about this page

Last updated October 21, 2025

Backends deployed to Vercel receive the benefits of Vercel's infrastructure, including:

*   [Fluid compute](/docs/fluid-compute): Zero-configuration, optimized concurrency, dynamic scaling, background processing, automatic cold-start prevention, region failover, and more
*   [Active CPU pricing](/docs/functions/usage-and-pricing): Only pay for the CPU you use, not waiting for I/O (e.g. calling AI models, database queries)
*   [Instant Rollback](/docs/instant-rollback): Quickly revert to a previous production deployment
*   [Vercel Firewall](/docs/vercel-firewall): A robust, multi-layered security system designed to protect your applications
*   [Preview deployments with Deployment Protection](/docs/deployments/environments#preview-environment-pre-production): Secure your preview environments and test changes safely before production
*   [Rolling releases](/docs/rolling-releases): Gradually roll out backends to detect errors early

## [Zero-configuration backends](#zero-configuration-backends)

Deploy the following backends to Vercel with zero-configuration.

![Express](https://api-frameworks.vercel.sh/framework-logos/express.svg)![Express](https://api-frameworks.vercel.sh/framework-logos/express.svg)

### Express

Fast, unopinionated, minimalist web framework for Node.js

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/express)[View Demo](https://express-vercel-example-demo.vercel.app/)

![FastAPI](https://api-frameworks.vercel.sh/framework-logos/fastapi.svg)

### FastAPI

FastAPI framework, high performance, easy to learn, fast to code, ready for production

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fastapi)[View Demo](https://vercel-fastapi-gamma-smoky.vercel.app/)

![Fastify](https://api-frameworks.vercel.sh/framework-logos/fastify.svg)![Fastify](https://api-frameworks.vercel.sh/framework-logos/fastify-dark.svg)

### Fastify

Fast and low overhead web framework, for Node.js

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fastify)View Demo

![Flask](https://api-frameworks.vercel.sh/framework-logos/flask.svg)

### Flask

The Python micro web framework

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/flask)View Demo

![Hono](https://api-frameworks.vercel.sh/framework-logos/hono.svg)

### Hono

Web framework built on Web Standards

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/hono)[View Demo](https://hono.vercel.dev)

![NestJS](https://api-frameworks.vercel.sh/framework-logos/nestjs.svg)

### NestJS

Framework for building efficient, scalable Node.js server-side applications

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nestjs)View Demo

![Nitro](https://api-frameworks.vercel.sh/framework-logos/nitro.svg)

### Nitro

Nitro is a next generation server toolkit.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nitro)[View Demo](https://nitro-template.vercel.app)

![xmcp](https://api-frameworks.vercel.sh/framework-logos/xmcp.svg)

### xmcp

The MCP framework for building AI-powered tools

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/xmcp)[View Demo](https://xmcp-template.vercel.app/)

## [Adapting to Serverless and Fluid compute](#adapting-to-serverless-and-fluid-compute)

If you are transitioning from a fully managed server or containerized environment to Vercel’s serverless architecture, you may need to rethink a few concepts in your application since there is no longer a server always running in the background.

The following are generally applicable to serverless, and therefore Vercel Functions (running with or without Fluid compute).

### [Websockets](#websockets)

Serverless functions have maximum execution limits and should respond as quickly as possible. They should not subscribe to data events. Instead, we need a client that subscribes to data events and a serverless functions that publishes new data. Consider using a serverless friendly realtime data provider.

### [Database Connections](#database-connections)

To manage database connections efficiently, [use the `attachDatabasePool` function from `@vercel/functions`](/docs/functions/functions-api-reference/vercel-functions-package#database-connection-pool-management).

--------------------------------------------------------------------------------
title: "Express on Vercel"
description: "Deploy Express applications to Vercel with zero configuration. Learn about middleware and Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/express"
--------------------------------------------------------------------------------

# Express on Vercel

Copy page

Ask AI about this page

Last updated October 15, 2025

Express is a fast, unopinionated, minimalist web framework for Node.js. You can deploy an Express app to Vercel with zero configuration.

Express applications on Vercel benefit from:

*   [Fluid compute](/docs/fluid-compute): Active CPU billing, automatic cold start prevention, optimized concurrency, background processing, and more
*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production): Test your changes on a copy of your production infrastructure
*   [Instant Rollback](/docs/instant-rollback): Recover from unintended changes or bugs in milliseconds
*   [Vercel Firewall](/docs/vercel-firewall): Protect your applications from a wide range of threats with a multi-layered security system
*   [Secure Compute](/docs/secure-compute): Create private links between your Vercel-hosted backend and other clouds

## [Get started with Express on Vercel](#get-started-with-express-on-vercel)

You can quickly deploy an Express application to Vercel by creating an Express app or using an existing one:

[Deploy Express to Vercel](https://vercel.com/templates/backend/express-js-on-vercel)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fexpress&template=express)[Live Example](https://express-vercel-example-demo.vercel.app)

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new Express project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init express
```

This will clone the [Express example repository](https://github.com/vercel/vercel/tree/main/examples/express) in a directory called `express`.

## [Exporting the Express application](#exporting-the-express-application)

To run an Express application on Vercel, create a file that imports the `express` package at any one of the following locations:

*   `app.{js,cjs,mjs,ts,cts,mts}`
*   `index.{js,cjs,mjs,ts,cts,mts}`
*   `server.{js,cjs,mjs,ts,cts,mts}`
*   `src/app.{js,cjs,mjs,ts,cts,mts}`
*   `src/index.{js,cjs,mjs,ts,cts,mts}`
*   `src/server.{js,mjs,cjs,ts,cts,mts}`

The file must also export the application as a default export of the module or use a port listener.

### [Using a default export](#using-a-default-export)

For example, use the following code that exports your Express app:

Express.js

src/index.ts

TypeScript

TypeScriptJavaScript

```
// Use "type: module" in package.json to use ES modules
import express from 'express';
const app = express();
 
// Define your routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Express on Vercel!' });
});
 
// Export the Express app
export default app;
```

### [Using a port listener](#using-a-port-listener)

You may also run your application using the `app.listen` pattern that exposes the server on a port.

Express.js

src/index.ts

TypeScript

TypeScriptJavaScript

```
// Use "type: module" in package.json to use ES modules
import express from 'express';
const app = express();
const port = 3000;
 
// Define your routes
app.get('/', (req, res) => {
  res.json({ message: 'Hello from Express on Vercel!' });
});
 
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
```

### [Local development](#local-development)

Use `vercel dev` to run your application locally

terminal

```
vercel dev
```

Minimum CLI version required: 47.0.5

### [Deploying the application](#deploying-the-application)

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli/deploy):

terminal

```
vc deploy
```

Minimum CLI version required: 47.0.5

## [Serving static assets](#serving-static-assets)

To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](/docs/cdn) using default [headers](/docs/headers) unless otherwise specified in `vercel.json`.

`express.static()` will be ignored and will not serve static assets.

## [Vercel Functions](#vercel-functions)

When you deploy an Express app to Vercel, your Express application becomes a single [Vercel Function](/docs/functions) and uses [Fluid compute](/docs/fluid-compute) by default. This means your Express app will automatically scale up and down based on traffic.

## [Limitations](#limitations)

*   `express.static()` will not serve static assets. You must use [the `public/**` directory](#serving-static-assets).

Additionally, all [Vercel Functions limitations](/docs/functions/limitations) apply to the Express application, including:

*   Application size: The Express application becomes a single bundle, which must fit within the 250MB limit of Vercel Functions. Our bundling process removes all unneeded files from the deployment's bundle to reduce size, but does not perform application bundling (e.g., Webpack or Rollup).
*   Error handling: Express.js will swallow errors that can put the main function into an undefined state unless properly handled. Express.js will render its own error pages (500), which prevents Vercel from discarding the function and resetting its state. Implement robust error handling to ensure errors are properly managed and do not interfere with the serverless function's lifecycle.

## [More resources](#more-resources)

Learn more about deploying Express projects on Vercel with the following resources:

*   [Express official documentation](https://expressjs.com/)
*   [Vercel Functions documentation](/docs/functions)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)
*   [Express middleware guide](https://expressjs.com/en/guide/using-middleware.html)

--------------------------------------------------------------------------------
title: "FastAPI on Vercel"
description: "Deploy FastAPI applications to Vercel with zero configuration. Learn about the Python runtime, ASGI, static assets, and Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/fastapi"
--------------------------------------------------------------------------------

# FastAPI on Vercel

Copy page

Ask AI about this page

Last updated October 15, 2025

FastAPI is a modern, high-performance, web framework for building APIs with Python based on standard Python type hints. You can deploy a FastAPI app to Vercel with zero configuration.

## [Get started with FastAPI on Vercel](#get-started-with-fastapi-on-vercel)

You can quickly deploy a FastAPI application to Vercel by creating a FastAPI app or using an existing one:

[Deploy FastAPI to Vercel](https://vercel.com/templates/python/fastapi-python-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Ffastapi&template=fastapi)[Live Example](https://vercel-plus-fastapi.vercel.app/)

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new FastAPI project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init fastapi
```

This will clone the [FastAPI example repository](https://github.com/vercel/vercel/tree/main/examples/fastapi) in a directory called `fastapi`.

## [Exporting the FastAPI application](#exporting-the-fastapi-application)

To run a FastAPI application on Vercel, define an `app` instance that initializes `FastAPI` at any of the following entrypoints:

*   `app.py`
*   `index.py`
*   `server.py`
*   `src/app.py`
*   `src/index.py`
*   `src/server.py`
*   `app/app.py`
*   `app/index.py`
*   `app/server.py`

For example:

src/index.py

```
from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"Python": "on Vercel"}
```

### [Local development](#local-development)

Use `vercel dev` to run your application locally.

terminal

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
vercel dev
```

Minimum CLI version required: 48.1.8

### [Deploying the application](#deploying-the-application)

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli/deploy):

terminal

```
vc deploy
```

Minimum CLI version required: 48.1.8

## [Serving static assets](#serving-static-assets)

To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](/docs/cdn) using default [headers](/docs/headers) unless otherwise specified in `vercel.json`.

app.py

```
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
 
app = FastAPI()
 
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # /vercel.svg is automatically served when included in the public/** directory.
    return RedirectResponse("/vercel.svg", status_code=307)
```

`app.mount("/public", ...)` is not needed and should not be used.

## [Vercel Functions](#vercel-functions)

When you deploy a FastAPI app to Vercel, the application becomes a single [Vercel Function](/docs/functions) and uses [Fluid compute](/docs/fluid-compute) by default. This means your FastAPI app will automatically scale up and down based on traffic.

## [Limitations](#limitations)

All [Vercel Functions limitations](/docs/functions/limitations) apply to FastAPI applications, including:

*   Application size: The FastAPI application becomes a single bundle, which must fit within the 250MB limit of Vercel Functions. Our bundling process removes `__pycache__` and `.pyc` files from the deployment's bundle to reduce size, but does not perform application bundling.

## [More resources](#more-resources)

Learn more about deploying FastAPI projects on Vercel with the following resources:

*   [FastAPI official documentation](https://fastapi.tiangolo.com/)
*   [Vercel Functions documentation](/docs/functions)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "Fastify on Vercel"
description: "Deploy Fastify applications to Vercel with zero configuration."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/fastify"
--------------------------------------------------------------------------------

# Fastify on Vercel

Copy page

Ask AI about this page

Last updated October 28, 2025

Fastify is a web framework highly focused on providing the best developer experience with the least overhead and a powerful plugin architecture. You can deploy a Fastify app to Vercel with zero configuration using [Vercel Functions](/docs/functions).

Fastify applications on Vercel benefit from:

*   [Fluid compute](/docs/fluid-compute): Pay for the CPU you use, automatic cold start reduction, optimized concurrency, background processing, and more
*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production): Test your changes in a copy of your production infrastructure
*   [Instant Rollback](/docs/instant-rollback): Recover from breaking changes or bugs in milliseconds
*   [Vercel Firewall](/docs/vercel-firewall): Protect your applications from a wide range of threats with a robust, multi-layered security system
*   [Secure Compute](/docs/secure-compute): Create private links between your Vercel-hosted backend and other clouds

## [Get started with Fastify on Vercel](#get-started-with-fastify-on-vercel)

You can quickly deploy a Fastify application to Vercel by creating a Fastify app or using an existing one:

[Deploy Fastify to Vercel](https://vercel.com/templates/backend/fastify-on-vercel)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Ffastify&template=fastify)[Live Example](https://fastify-vercel-example-demo.vercel.app)

## [Fastify entrypoint detection](#fastify-entrypoint-detection)

To allow Vercel to deploy your Fastify application and process web requests, your server entrypoint file should be named one of the following:

*   `src/app.{js,mjs,cjs,ts,cts,mts}`
*   `src/index.{js,mjs,cjs,ts,cts,mts}`
*   `src/server.{js,mjs,cjs,ts,cts,mts}`
*   `app.{js,mjs,cjs,ts,cts,mts}`
*   `index.{js,mjs,cjs,ts,cts,mts}`
*   `server.{js,mjs,cjs,ts,cts,mts}`

For example, use the following code as an entrypoint:

src/index.ts

```
import Fastify from 'fastify'
 
const fastify = Fastify({ logger: true })
 
fastify.get('/', async (request, reply) => {
  return { hello: 'world' }
})
 
fastify.listen({ port: 3000 })
```

### [Local development](#local-development)

Use `vercel dev` to run your application locally

terminal

```
vercel dev
```

Minimum CLI version required: 48.6.0

### [Deploying the application](#deploying-the-application)

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli/deploy):

terminal

```
vc deploy
```

Minimum CLI version required: 48.6.0

## [Vercel Functions](#vercel-functions)

When you deploy a Fastify app to Vercel, your Fastify application becomes a single [Vercel Function](/docs/functions) and uses [Fluid compute](/docs/fluid-compute) by default. This means your Fastify app will automatically scale up and down based on traffic.

## [Limitations](#limitations)

All [Vercel Functions limitations](/docs/functions/limitations) apply to the Fastify application, including the size of the application being limited to 250MB.

## [More resources](#more-resources)

Learn more about deploying Fastify projects on Vercel with the following resources:

*   [Fastify official documentation](https://fastify.dev/docs/latest/)
*   [Vercel Functions documentation](/docs/functions)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "Flask on Vercel"
description: "Deploy Flask applications to Vercel with zero configuration. Learn about the Python runtime, WSGI, static assets, and Vercel Functions."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/flask"
--------------------------------------------------------------------------------

# Flask on Vercel

Copy page

Ask AI about this page

Last updated October 15, 2025

Flask is a lightweight WSGI web application framework for Python. It's designed with simplicity and flexibility in mind, making it easy to get started while remaining powerful for building web applications. You can deploy a Flask app to Vercel with zero configuration.

## [Get started with Flask on Vercel](#get-started-with-flask-on-vercel)

You can quickly deploy a Flask application to Vercel by creating a Flask app or using an existing one:

[Deploy Flask to Vercel](https://vercel.com/templates/python/flask-python-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fflask&template=flask)[Live Example](https://vercel-plus-flask.vercel.app/)

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new Flask project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init flask
```

This will clone the [Flask example repository](https://github.com/vercel/vercel/tree/main/examples/flask) in a directory called `flask`.

## [Exporting the Flask application](#exporting-the-flask-application)

To run a Flask application on Vercel, define an `app` instance that initializes `Flask` at any of the following entrypoints:

*   `app.py`
*   `index.py`
*   `server.py`
*   `src/app.py`
*   `src/index.py`
*   `src/server.py`
*   `app/app.py`
*   `app/index.py`
*   `app/server.py`

For example:

src/index.py

```
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def hello_world():
    return {"message": "Hello, World!"}
```

### [Local development](#local-development)

Use `vercel dev` to run your application locally.

terminal

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
vercel dev
```

Minimum CLI version required: 48.2.10

### [Deploying the application](#deploying-the-application)

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli/deploy):

terminal

```
vc deploy
```

Minimum CLI version required: 48.2.10

## [Serving static assets](#serving-static-assets)

To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](/docs/cdn) using default [headers](/docs/headers) unless otherwise specified in `vercel.json`.

app.py

```
from flask import Flask, redirect
 
app = Flask(__name__)
 
@app.route("/favicon.ico")
def favicon():
    # /vercel.svg is automatically served when included in the public/** directory.
    return redirect("/vercel.svg", code=307)
```

Flask's `app.static_folder` should not be used for static files on Vercel. Use the `public/**` directory instead.

## [Vercel Functions](#vercel-functions)

When you deploy a Flask app to Vercel, the application becomes a single [Vercel Function](/docs/functions) and uses [Fluid compute](/docs/fluid-compute) by default. This means your Flask app will automatically scale up and down based on traffic.

## [Limitations](#limitations)

All [Vercel Functions limitations](/docs/functions/limitations) apply to Flask applications, including:

*   Application size: The Flask application becomes a single bundle, which must fit within the 250MB limit of Vercel Functions. Our bundling process removes `__pycache__` and `.pyc` files from the deployment's bundle to reduce size, but does not perform application bundling.

## [More resources](#more-resources)

Learn more about deploying Flask projects on Vercel with the following resources:

*   [Flask official documentation](https://flask.palletsprojects.com/)
*   [Vercel Functions documentation](/docs/functions)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "Hono on Vercel"
description: "Deploy Hono applications to Vercel with zero configuration. Learn about observability, ISR, and custom build configurations."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/hono"
--------------------------------------------------------------------------------

# Hono on Vercel

Copy page

Ask AI about this page

Last updated October 15, 2025

Hono is a fast and lightweight web application framework built on Web Standards. You can deploy a Hono app to Vercel with zero configuration.

## [Get started with Hono on Vercel](#get-started-with-hono-on-vercel)

Start with Hono on Vercel by using the following Hono template to deploy to Vercel with zero configuration:

[Deploy Hono to Vercel](https://vercel.com/templates/backend/hono-starter)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fhono&template=hono)[Live Example](https://hono.vercel.dev/)

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Hono project.

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new Hono project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init hono
```

This will clone the [Hono example repository](https://github.com/vercel/vercel/tree/main/examples/hono) in a directory called `hono`.

## [Exporting the Hono application](#exporting-the-hono-application)

To run a Hono application on Vercel, create a file that imports the `hono` package at any one of the following locations:

*   `app.{js,cjs,mjs,ts,cts,mts}`
*   `index.{js,cjs,mjs,ts,cts,mts}`
*   `server.{js,cjs,mjs,ts,cts,mts}`
*   `src/app.{js,cjs,mjs,ts,cts,mts}`
*   `src/index.{js,cjs,mjs,ts,cts,mts}`
*   `src/server.{js,mjs,cjs,ts,cts,mts}`

server.ts

```
import { Hono } from 'hono';
 
const app = new Hono();
 
// ...
 
export default app;
```

### [Local development](#local-development)

To run your Hono application locally, use [Vercel CLI](https://vercel.com/docs/cli/dev):

```
vc dev
```

This ensures that the application will use the default export to run the same as when deployed to Vercel. The application will be available on your `localhost`.

## [Middleware](#middleware)

Hono has the concept of "Middleware" as a part of the framework. This is different from [Vercel Routing Middleware](/docs/routing-middleware), though they can be used together.

### [Hono Middleware](#hono-middleware)

In Hono, [Middleware](https://hono.dev/docs/concepts/middleware) runs before a request handler in the framework's router. This is commonly used for loggers, CORS handling, or authentication. The code in the Hono application might look like this:

src/index.ts

```
app.use(logger());
app.use('/posts/*', cors());
app.post('/posts/*', basicAuth());
```

More examples of Hono Middleware can be found in [the Hono documentation](https://hono.dev/docs/middleware/builtin/basic-auth).

### [Vercel Routing Middleware](#vercel-routing-middleware)

In Vercel, [Routing Middleware](/docs/routing-middleware) executes code before a request is processed by the application. This gives you a way to handle rewrites, redirects, headers, and more, before returning a response. See [the Routing Middleware documentation](/docs/routing-middleware) for examples.

## [Serving static assets](#serving-static-assets)

To serve static assets, place them in the `public/**` directory. They will be served as a part of our [CDN](/docs/cdn) using default [headers](/docs/headers) unless otherwise specified in `vercel.json`.

[Hono's `serveStatic()`](https://hono.dev/docs/getting-started/nodejs#serve-static-files) will be ignored and will not serve static assets.

## [Vercel Functions](#vercel-functions)

When you deploy a Hono app to Vercel, your server routes automatically become [Vercel Functions](/docs/functions) and use [Fluid compute](/docs/fluid-compute) by default.

### [Streaming](#streaming)

Vercel Functions support streaming which can be used with [Hono's `stream()` function](https://hono.dev/docs/helpers/streaming).

src/index.ts

```
app.get('/stream', (c) => {
  return stream(c, async (stream) => {
    // Write a process to be executed when aborted.
    stream.onAbort(() => {
      console.log('Aborted!');
    });
    // Write a Uint8Array.
    await stream.write(new Uint8Array([0x48, 0x65, 0x6c, 0x6c, 0x6f]));
    // Pipe a readable stream.
    await stream.pipe(anotherReadableStream);
  });
});
```

## [More resources](#more-resources)

Learn more about deploying Hono projects on Vercel with the following resources:

*   [Hono templates on Vercel](https://vercel.com/templates/hono)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "NestJS on Vercel"
description: "Deploy NestJS applications to Vercel with zero configuration."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/nestjs"
--------------------------------------------------------------------------------

# NestJS on Vercel

Copy page

Ask AI about this page

Last updated October 28, 2025

NestJS is a progressive Node.js framework for building efficient, reliable and scalable server-side applications. You can deploy a NestJS app to Vercel with zero configuration using [Vercel Functions](/docs/functions).

NestJS applications on Vercel benefit from:

*   [Fluid compute](/docs/fluid-compute): Pay for the CPU you use, automatic cold start reduction, optimized concurrency, background processing, and more
*   [Preview deployments](/docs/deployments/environments#preview-environment-pre-production): Test your changes in a copy of your production infrastructure
*   [Instant Rollback](/docs/instant-rollback): Recover from breaking changes or bugs in milliseconds
*   [Vercel Firewall](/docs/vercel-firewall): Protect your applications from a wide range of threats with a robust, multi-layered security system
*   [Secure Compute](/docs/secure-compute): Create private links between your Vercel-hosted backend and other clouds

## [Get started with NestJS on Vercel](#get-started-with-nestjs-on-vercel)

You can quickly deploy a NestJS application to Vercel by creating a NestJS app or using an existing one:

[Deploy NestJS to Vercel](https://vercel.com/templates/backend/nestjs-on-vercel)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnestjs&template=nestjs)[Live Example](https://nestjs-vercel-example-demo.vercel.app)

## [NestJS entrypoint detection](#nestjs-entrypoint-detection)

To allow Vercel to deploy your NestJS application and process web requests, your server entrypoint file should be named one of the following:

*   `src/main.{js,mjs,cjs,ts,cts,mts}`
*   `src/app.{js,mjs,cjs,ts,cts,mts}`
*   `src/index.{js,mjs,cjs,ts,cts,mts}`
*   `src/server.{js,mjs,cjs,ts,cts,mts}`
*   `app.{js,mjs,cjs,ts,cts,mts}`
*   `index.{js,mjs,cjs,ts,cts,mts}`
*   `server.{js,mjs,cjs,ts,cts,mts}`

For example, use the following code as an entrypoint:

src/app.ts

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
 
async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(process.env.PORT ?? 3000);
}
bootstrap();
```

### [Local development](#local-development)

Use `vercel dev` to run your application locally

terminal

```
vercel dev
```

Minimum CLI version required: 48.4.0

### [Deploying the application](#deploying-the-application)

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli/deploy):

terminal

```
vc deploy
```

Minimum CLI version required: 48.4.0

## [Vercel Functions](#vercel-functions)

When you deploy a NestJS app to Vercel, your NestJS application becomes a single [Vercel Function](/docs/functions) and uses [Fluid compute](/docs/fluid-compute) by default. This means your NestJS app will automatically scale up and down based on traffic.

## [Limitations](#limitations)

All [Vercel Functions limitations](/docs/functions/limitations) apply to the NestJS application, including the size of the application being limited to 250MB.

## [More resources](#more-resources)

Learn more about deploying NestJS projects on Vercel with the following resources:

*   [NestJS official documentation](https://docs.nestjs.com/)
*   [Vercel Functions documentation](/docs/functions)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "Nitro on Vercel"
description: "Deploy Nitro applications to Vercel with zero configuration. Learn about observability, ISR, and custom build configurations."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/nitro"
--------------------------------------------------------------------------------

# Nitro on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Nitro is a full-stack framework with TypeScript-first support. It includes filesystem routing, code-splitting for fast startup, built-in caching, and multi-driver storage. It enables deployments from the same codebase to any platform with output sizes under 1MB.

You can deploy a Nitro app to Vercel with zero configuration.

## [Get started with Nitro on Vercel](#get-started-with-nitro-on-vercel)

To get started with Nitro on Vercel, use the following Nitro template to deploy to Vercel with zero configuration:

[Deploy Nitro to Vercel](https://vercel.com/templates/backend/nitro-starter)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnitro&template=nitro)[Live Example](https://nitro-template.vercel.app/)

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Nitro project.

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new Nitro project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init nitro
```

This will clone the [Nitro example repository](https://github.com/vercel/vercel/tree/main/examples/nitro) in a directory called `nitro`.

## [Using Vercel's features with Nitro](#using-vercel's-features-with-nitro)

When you deploy a Nitro app to Vercel, you can use Vercel specific features such as [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr), [preview deployments](/docs/deployments/environments#preview-environment-pre-production), [Fluid compute](/docs/fluid-compute), [Observability](#observability), and [Vercel firewall](/docs/vercel-firewall) with zero or minimum configuration.

## [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)

[ISR](/docs/incremental-static-regeneration) allows you to create or update content without redeploying your site. ISR has three main benefits for developers: better performance, improved security, and faster build times.

### [On-demand revalidation](#on-demand-revalidation)

With [on-demand revalidation](/docs/incremental-static-regeneration/quickstart#on-demand-revalidation), you can purge the cache for an ISR route whenever you want, foregoing the time interval required with background revalidation.

To revalidate a path to a prerendered function:

1.  ### [Create an Environment Variable](#create-an-environment-variable)
    
    Create an [Environment Variable](/docs/environment-variables) to store a revalidation secret by:
    
    *   Using the command:
    
    terminal
    
    ```
    openssl rand -base64 32
    ```
    
    *   Or [generating a secret](https://generate-secret.vercel.app/32) to create a random value.
2.  ### [Update your configuration](#update-your-configuration)
    
    Update your configuration to use the revalidation secret as follows:
    
    NitroNuxt
    
    nitro.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    export default defineNitroConfig({
      vercel: {
        config: {
          bypassToken: process.env.VERCEL_BYPASS_TOKEN,
        },
      },
    });
    ```
    
3.  ### [Trigger revalidation](#trigger-revalidation)
    
    You can revalidate a path to a prerendered function by making a `GET` or `HEAD` request to that path with a header of `x-prerender-revalidate: bypassToken`
    
    When the prerendered function endpoint is accessed with this header set, the cache will be revalidated. The next request to that function will return a fresh response.
    

### [Fine-grained ISR configuration](#fine-grained-isr-configuration)

To have more control over ISR caching, you can pass an options object to the `isr` route rule as shown below:

nitro.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNitroConfig({
  routeRules: {
    '/products/**': {
      isr: {
        allowQuery: ['q'],
        passQuery: true,
      },
    },
  },
});
```

By default, query parameters are ignored by cache unless you specify them in the `allowQuery` array.

The following options are available:

| Option | Type | Description |
| --- | --- | --- |
| `expiration` | `number | false` | The expiration time, in seconds, before the cached asset is re-generated by invoking the serverless function. Setting the value to `false` (or `isr: true` in the route rule) will cause it to never expire. |
| `group` | `number` | Group number of the asset. Use this to revalidate multiple assets at the same time. |
| `allowQuery` | `string[] | undefined` | List of query string parameter names that will be cached independently. If you specify an empty array, query values are not considered for caching. If `undefined`, each unique query value is cached independently. For wildcard `/**` route rules, `url` is always added. |
| `passQuery` | `boolean` | When `true`, the query string will be present on the request argument passed to the invoked function. The `allowQuery` filter still applies. |

## [Observability](#observability)

With [Vercel Observability](/docs/observability), you can view detailed performance insights broken down by route and monitor function execution performance. This can help you identify bottlenecks and optimization opportunities.

Nitro (>=2.12) generates routing hints for [functions observability insights](/docs/observability/insights#vercel-functions), providing a detailed view of performance broken down by route.

To enable this feature, ensure you are using a compatibility date of `2025-07-15` or later.

NitroNuxt

nitro.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNitroConfig({
  compatibilityDate: '2025-07-15', // or "latest"
});
```

Framework integrations can use the `ssrRoutes` configuration to declare SSR routes. For more information, see [#3475](https://github.com/unjs/nitro/pull/3475).

## [Vercel Functions](#vercel-functions)

When you deploy a Nitro app to Vercel, your server routes automatically become [Vercel Functions](/docs/functions) and use [Fluid compute](/docs/fluid-compute) by default.

## [More resources](#more-resources)

Learn more about deploying Nitro projects on Vercel with the following resources:

*   [Getting started with Nitro guide](https://nitro.build/guide)
*   [Deploy Nitro to Vercel guide](https://nitro.build/deploy/providers/vercel)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "xmcp on Vercel"
description: "Build MCP-compatible backends with xmcp and deploy to Vercel. Learn the project structure, tool format, middleware, and how to run locally and in production."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/backend/xmcp"
--------------------------------------------------------------------------------

# xmcp on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

`xmcp` is a TypeScript-first framework for building MCP-compatible backends. It provides an opinionated project structure, automatic tool discovery, and a streamlined middleware layer for request/response processing. You can deploy an xmcp app to Vercel with zero configuration.

## [Get started with xmcp on Vercel](#get-started-with-xmcp-on-vercel)

Start with xmcp on Vercel by creating a new xmcp project:

terminal

```
npx create-xmcp-app@latest
```

This scaffolds a project with a `src/tools/` directory for tools, optional `src/middleware.ts`, and an `xmcp.config.ts` file.

To deploy, [connect your Git repository](/new) or [use Vercel CLI](/docs/cli):

terminal

```
vc deploy
```

### [Get started with Vercel CLI](#get-started-with-vercel-cli)

Get started by initializing a new Xmcp project using [Vercel CLI init command](/docs/cli/init):

terminal

```
vc init xmcp
```

This will clone the [Xmcp example repository](https://github.com/vercel/vercel/tree/main/examples/xmcp) in a directory called `xmcp`.

## [Local development](#local-development)

To run your xmcp application locally, you can use [Vercel CLI](https://vercel.com/docs/cli/dev):

terminal

```
vc dev
```

Alternatively, use your project's dev script:

terminal

```
npm run dev
yarn dev
pnpm run dev
```

## [Middleware](#middleware)

### [xmcp Middleware](#xmcp-middleware)

In xmcp, an optional `middleware.ts` lets you run code before and after tool execution. This is commonly used for logging, auth, or request shaping:

src/middleware.ts

```
import { type Middleware } from 'xmcp';
 
const middleware: Middleware = async (req, res, next) => {
  // Custom processing
  next();
};
 
export default middleware;
```

### [Vercel Routing Middleware](#vercel-routing-middleware)

In Vercel, [Routing Middleware](/docs/routing-middleware) executes before a request is processed by your application. Use it for rewrites, redirects, headers, or personalization, and combine it with xmcp's own middleware as needed.

## [Vercel Functions](#vercel-functions)

When you deploy an xmcp app to Vercel, your server endpoints automatically run as [Vercel Functions](/docs/functions) and use [Fluid compute](/docs/fluid-compute) by default.

## [More resources](#more-resources)

*   [xmcp documentation](https://xmcp.dev/docs)
*   [Backend templates on Vercel](https://vercel.com/templates?type=backend)

--------------------------------------------------------------------------------
title: "Frontends on Vercel"
description: "Vercel supports a wide range of the most popular frontend frameworks, optimizing how your application builds and runs no matter what tooling you use."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend"
--------------------------------------------------------------------------------

# Frontends on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

The following frontend frameworks are supported with zero-configuration.

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

![FastHTML](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Ffasthtml.png&w=48&q=75)

### FastHTML

The fastest way to create an HTML app

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/fasthtml)[View Demo](https://fasthtml-template.vercel.app)

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

![Zola](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2Fapi-frameworks.vercel.sh%2Fframework-logos%2Fzola.png&w=48&q=75)

### Zola

Everything you need to make a static site engine in one binary.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/zola)[View Demo](https://zola-template.vercel.app)

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

--------------------------------------------------------------------------------
title: "Astro on Vercel"
description: "Learn how to use Vercel's features with Astro"
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend/astro"
--------------------------------------------------------------------------------

# Astro on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Astro is an all-in-one web framework that enables you to build performant static websites. People choose Astro when they want to build content-rich experiences with as little JavaScript as possible.

You can deploy a static Astro app to Vercel with zero configuration.

## [Get Started with Astro on Vercel](#get-started-with-astro-on-vercel)

To get started with Astro on Vercel:

*   If you already have a project with Astro, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Astro example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Astro template, or view a live example.](/templates/astro/astro-boilerplate)

[Deploy](/new/clone?demo-description=An%20Astro%20site%2C%20using%20the%20basics%20starter%20kit.&demo-image=%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F7s4Lxeg0kZof4ZuZfA7sjV%2F20eac2ba6e52426a62b3c0e4b1dbb412%2FCleanShot_2022-05-23_at_22.09.38_2x.png&demo-title=Astro%20Boilerplate&demo-url=https%3A%2F%2Fastro-template.vercel.app%2F&from=templates&project-name=Astro%20Boilerplate&repository-name=astro-boilerplate&repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fastro&skippable-integrations=1)[Live Example](https://astro-template.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Astro project.

## [Using Vercel's features with Astro](#using-vercel's-features-with-astro)

To deploy a server-rendered Astro app, or a static Astro site with Vercel features like Web Analytics and Image Optimization, you must:

1.  Add [Astro's Vercel adapter](https://docs.astro.build/en/guides/integrations-guide/vercel) to your project. There are two ways to do so:
    
    *   Using `astro add`, which configures the adapter for you with default settings. Using `astro add` will generate a preconfigured `astro.config.ts` with opinionated default settings
        
        pnpmyarnnpmbun
        
        ```
        pnpm astro add vercel
        ```
        
    *   Or, manually installing the [`@astrojs/vercel`](https://www.npmjs.com/package/@astrojs/vercel) package. You should manually install the adapter if you don't want an opinionated initial configuration
        
        pnpmyarnnpmbun
        
        ```
        pnpm i @astrojs/vercel
        ```
        
2.  Configure your project. In your `astro.config.ts` file, import either the `serverless` or `static` plugin, and set the output to `server` or `static` respectively:
    
    Serverless SSRStatic
    
    astro.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { defineConfig } from 'astro/config';
    // Import /serverless for a Serverless SSR site
    import vercelServerless from '@astrojs/vercel/serverless';
     
    export default defineConfig({
      output: 'server',
      adapter: vercelServerless(),
    });
    ```
    
    astro.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { defineConfig } from 'astro/config';
    // Import /static for a static site
    import vercelStatic from '@astrojs/vercel/static';
     
    export default defineConfig({
      // Must be 'static' or 'hybrid'
      output: 'static',
      adapter: vercelStatic(),
    });
    ```
    
3.  Enable Vercel's features using Astro's [configuration options](#configuration-options). The following example `astro.config.ts` enables Web Analytics and adds a maximum duration to Vercel Function routes:
    
    astro.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { defineConfig } from 'astro/config';
    // Also can be @astrojs/vercel/static
    import vercel from '@astrojs/vercel/serverless';
     
    export default defineConfig({
      // Also can be 'static' or 'hybrid'
      output: 'server',
      adapter: vercel({
        webAnalytics: {
          enabled: true,
        },
        maxDuration: 8,
      }),
    });
    ```
    

### [Configuration options](#configuration-options)

The following configuration options enable Vercel's features for Astro deployments.

| Option | type | Rendering | Purpose |
| --- | --- | --- | --- |
| [`maxDuration`](/docs/functions/runtimes#max-duration) | `number` | Serverless | Extends or limits the maximum duration (in seconds) that Vercel functions can run before timing out. |
| [`webAnalytics`](/docs/analytics) | `{enabled: boolean}` | Static, Serverless | Enables Vercel's [Web Analytics](/docs/analytics). See [the quickstart](/docs/analytics/quickstart) to set up analytics on your account. |
| [`imageService`](https://docs.astro.build/en/guides/integrations-guide/vercel/#imageservice) | `boolean` | Static, Serverless | For astro versions `3` and up. Enables an automatically [configured service](https://docs.astro.build/en/reference/image-service-reference/#what-is-an-image-service) to optimize your images. |
| [`devImageService`](https://docs.astro.build/en/guides/integrations-guide/vercel/#devimageservice) | `string` | Static, Serverless | For astro versions `3` and up. Configure the [image service](https://docs.astro.build/en/reference/image-service-reference/#what-is-an-image-service) used to optimize your images in your dev environment. |
| [`imagesConfig`](/docs/build-output-api/v3/configuration#images) | `VercelImageConfig` | Static, Serverless | Defines the behavior of the Image Optimization API, allowing on-demand optimization at runtime. See [the Build Output API docs](/docs/build-output-api/v3/configuration#images) for required options. |
| [`functionPerRoute`](https://docs.astro.build/en/guides/integrations-guide/vercel/#function-bundling-configuration) | `boolean` | Serverless | API routes are bundled into one function by default. Set this to true to split each route into separate functions. |
| [`edgeMiddleware`](https://docs.astro.build/en/guides/integrations-guide/vercel/#vercel-edge-middleware-with-astro-middleware) | `boolean` | Serverless | Set to `true` to automatically convert Astro middleware to Routing Middleware, eliminating the need for a `middleware.ts` file. |
| [`includeFiles`](https://docs.astro.build/en/guides/integrations-guide/vercel/#includefiles) | `string[]` | Serverless | Force files to be bundled with your Vercel functions. |
| [`excludeFiles`](https://docs.astro.build/en/guides/integrations-guide/vercel/#excludefiles) | `string[]` | Serverless | Exclude files from being bundled with your Vercel functions. Also available with [`.vercelignore`](/docs/deployments/vercel-ignore#) |

For more details on the configuration options, see [Astro's docs](https://docs.astro.build/en/guides/integrations-guide/vercel/#configuration).

## [Server-Side Rendering](#server-side-rendering)

Using SSR, or [on-demand rendering](https://docs.astro.build/en/guides/server-side-rendering/) as Astro calls it, enables you to deploy your routes as Vercel functions on Vercel. This allows you to add dynamic elements to your app, such as user logins and personalized content.

You can enable SSR by [adding the Vercel adapter to your project](#using-vercel's-features-with-astro).

If your Astro project is statically rendered, you can opt individual routes. To do so:

1.  Set your `output` option to `hybrid` in your `<PreferredExtension filename="astro.config" mjs />`:
    
    astro.config.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import { defineConfig } from 'astro/config';
    import vercel from '@astrojs/vercel/serverless';
     
    export default defineConfig({
      output: 'hybrid',
      adapter: vercel({
        edgeMiddleware: true,
      }),
    });
    ```
    
2.  Add `export const prerender = false;` to your components:
    
    src/pages/mypage.astro
    
    ```
    ---
    export const prerender = false;
    // ...
    ---
    <html>
      <!-- Server-rendered page here... -->
    </html>
    ```
    

SSR with Astro on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has zero-configuration support for [`Cache-Control` headers](/docs/edge-cache), including `stale-while-revalidate`

[Learn more about Astro SSR](https://docs.astro.build/en/guides/server-side-rendering/)

### [Static rendering](#static-rendering)

Statically rendered, or pre-rendered, Astro apps can be deployed to Vercel with zero configuration. To enable Vercel features like Image Optimization or Web Analytics, see [Using Vercel's features with Astro](#using-vercel's-features-with-astro).

You can opt individual routes into static rendering with `export const prerender = true` as shown below:

src/pages/mypage.astro

```
---
export const prerender = true;
// ...
---
<html>
  <!-- Static, pre-rendered page here... -->
</html>
```

Statically rendered Astro sites on Vercel:

*   Require zero configuration to deploy
*   Can use Vercel features with `astro.config.ts`

[Learn more about Astro Static Rendering](https://docs.astro.build/en/core-concepts/rendering-modes/#pre-rendered)

## [Incremental Static Regeneration](#incremental-static-regeneration)

[Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) allows you to create or update content without redeploying your site. ISR has two main benefits for developers: better performance and faster build times.

To enable ISR in Astro, you need to use the [Vercel adapter](https://docs.astro.build/en/guides/integrations-guide/vercel/) and set `isr` to `true` in your configuration in `astro.config.mjs`:

ISR function requests do not include search params, similar to requests in static mode.

Using ISR with Astro on Vercel offers:

*   Better performance with our global [CDN](/docs/cdn)
*   Zero-downtime rollouts to previously statically generated pages
*   Global content updates in 300ms
*   Generated pages are both cached and persisted to durable storage

[Learn more about ISR with Astro.](https://docs.astro.build/en/guides/integrations-guide/vercel/#isr)

## [Vercel Functions](#vercel-functions)

[Vercel Functions](/docs/functions) use resources that scale up and down based on traffic demands. This makes them reliable during peak hours, but low cost during slow periods.

When you [enable SSR with Astro's Vercel adapter](#using-vercel's-features-with-astro), all of your routes will be server-rendered as Vercel functions by default. Astro's [Server Endpoints](https://docs.astro.build/en/core-concepts/endpoints/#server-endpoints-api-routes) are the best way to define API routes with Astro on Vercel.

When defining an Endpoint, you must name each function after the HTTP method it represents. The following example defines basic HTTP methods in a Server Endpoint:

src/pages/methods.json.ts

TypeScript

TypeScriptJavaScript

```
import { APIRoute } from 'astro/dist/@types/astro';
 
export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a GET!',
    }),
  );
};
 
export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a POST!',
    }),
  );
};
 
export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a DELETE!',
    }),
  );
};
 
// ALL matches any method that you haven't implemented.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `This was a ${request.method}!`,
    }),
  );
};
```

Astro removes the final file during the build process, so the name of the file should include the extension of the data you want serve (for example `example.png.js` will become `/example.png`).

Vercel Functions with Astro on Vercel:

*   Scale to zero when not in use
*   Scale automatically as traffic increases

[Learn more about Vercel Functions](/docs/functions)

## [Image Optimization](#image-optimization)

[Image Optimization](/docs/image-optimization) helps you achieve faster page loads by reducing the size of images and using modern image formats. When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained).

Image Optimization with Astro on Vercel is supported out of the box with Astro's `Image` component. See [the Image Optimization quickstart](/docs/image-optimization/quickstart) to learn more.

Image Optimization with Astro on Vercel:

*   Requires zero-configuration for Image Optimization when using Astro's `Image` component
*   Helps your team ensure great performance by default
*   Keeps your builds fast by optimizing images on-demand

[Learn more about Image Optimization](/docs/image-optimization)

## [Middleware](#middleware)

[Middleware](/docs/routing-middleware) is a function that execute before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Middleware is an effective way to personalize statically generated content.

[Astro middleware](https://docs.astro.build/en/guides/middleware/#basic-usage) allows you to set and share information across your endpoints and pages with a `middleware.ts` file in your `src` directory. The following example edits the global `locals` object, adding data which will be available in any `.astro` file:

src/middleware.ts

TypeScript

TypeScriptJavaScript

```
// This helper automatically types middleware params
import { defineMiddleware } from 'astro:middleware';
 
export const onRequest = defineMiddleware(({ locals }, next) => {
  // intercept data from a request
  // optionally, modify the properties in `locals`
  locals.title = 'New title';
 
  // return a Response or the result of calling `next()`
  return next();
});
```

**

Astro middleware is not the same as Vercel's Routing Middleware

**

, which has to be placed at the root directory of your project, outside `src`.

To add custom properties to `locals` in `middleware.ts`, you must declare a global namespace in your `env.d.ts` file:

src/env.d.ts

```
declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

You can then access the data you added to `locals` in any `.astro` file, like so:

src/pages/middleware-title.astro

```
---
const { title } = Astro.locals;
---
<h1>{title}</h1>
<p>The name of this page is from middleware.</p>
```

### [Deploying middleware at the Edge](#deploying-middleware-at-the-edge)

You can deploy Astro's middleware at the Edge, giving you access to data in the `RequestContext` and `Request`, and enabling you to use [Vercel's Routing Middleware helpers](/docs/routing-middleware/api#routing-middleware-helper-methods), such as [`geolocation()`](/docs/routing-middleware/api#geolocation) or [`ipAddress()`](/docs/routing-middleware/api#geolocation).

To use Astro's middleware at the Edge, set `edgeMiddleware: true` in your `astro.config.ts` file:

astro.config.ts

TypeScript

TypeScriptJavaScript

```
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';
 
export default defineConfig({
  output: 'server',
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

If you're using [Vercel's Routing Middleware](#using-vercel's-edge-middleware), you do not need to set `edgeMiddleware: true` in your `astro.config.ts` file.

See Astro's docs on [the limitations and constraints](https://docs.astro.build/en/guides/integrations-guide/vercel/#limitations-and-constraints) for using middleware at the Edge, as well as [their troubleshooting tips](https://docs.astro.build/en/guides/integrations-guide/vercel/#troubleshooting).

#### [Using `Astro.locals` in Routing Middleware](#using-astro.locals-in-routing-middleware)

The `Astro.locals` object exposes data to your `.astro` components, allowing you to dynamically modify your content with middleware. To make changes to `Astro.locals` in Astro's middleware at the edge:

1.  Add a new middleware file next to your `src/middleware.ts` and name it `src/vercel-edge-middleware.ts`. This file name is required to make changes to [`Astro.locals`](https://docs.astro.build/en/reference/api-reference/#astrolocals). If you don't want to update `Astro.locals`, this step is not required
    
2.  Return an object with the properties you want to add to `Astro.locals`. :
    
    For TypeScript, you must install [the `@vercel/functions` package](/docs/routing-middleware/api#routing-middleware-helper-methods):
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @vercel/functions
    ```
    
    Then, type your middleware function like so:
    
    src/vercel-edge-middleware.ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import type { RequestContext } from '@vercel/functions';
     
    // Note the parameters are different from standard Astro middleware
    export default function ({
      request,
      context,
    }: {
      request: Request;
      context: RequestContext;
    }) {
      // Return an Astro.locals object with a title property
      return {
        title: "Spider-man's blog",
      };
    }
    ```
    

### [Using Vercel's Routing Middleware](#using-vercel's-routing-middleware)

Astro's middleware, which should be in `src/middleware.ts`, is distinct from Vercel Routing Middleware, which should be a `middleware.ts` file at the root of your project.

Vercel recommends using framework-native solutions. You should use Astro's middleware over Vercel's Routing Middleware wherever possible.

If you still want to use Vercel's Routing Middleware, see [the Quickstart](/docs/routing-middleware/getting-started) to learn how.

### [Rewrites](#rewrites)

Rewrites only work for static files with Astro. You must use [Vercel's Routing Middleware](/docs/routing-middleware/api#match-paths-based-on-conditional-statements) for rewrites. You should not use `vercel.json` to rewrite URL paths with astro projects; doing so produces inconsistent behavior, and is not officially supported.

### [Redirects](#redirects)

In general, Vercel recommends using framework-native solutions, and Astro has [built-in support for redirects](https://docs.astro.build/en/core-concepts/routing/#redirects). That said, you can also do redirects with [Vercel's Routing Middleware](/docs/routing-middleware/getting-started).

#### [Redirects in your Astro config](#redirects-in-your-astro-config)

You can do redirects on Astro with `astro.config.ts` the `redirects` config option as shown below:

astro.config.ts

TypeScript

TypeScriptJavaScript

```
import { defineConfig } from 'astro/config';
 
export default defineConfig({
  redirects: {
    '/old-page': '/new-page',
  },
});
```

#### [Redirects in Server Endpoints](#redirects-in-server-endpoints)

You can also return a redirect from a Server Endpoint using the [`redirect`](https://docs.astro.build/en/core-concepts/endpoints/#redirects) utility:

src/pages/links/\[id\].ts

TypeScript

TypeScriptJavaScript

```
export async function GET({ params, redirect }): APIRoute {
  return redirect('/redirect-path', 307);
}
```

#### [Redirects in components](#redirects-in-components)

You can redirect from within Astro components with [`Astro.redirect()`](https://docs.astro.build/en/reference/api-reference/#astroredirect):

src/pages/account.astro

```
---
import { isLoggedIn } from '../utils';
 
const cookie = Astro.request.headers.get('cookie');
 
// If the user is not logged in, redirect them to the login page
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}
---
 
<h1>You can only see this page while logged in</h1>
```

Astro Middleware on Vercel:

*   Executes before a request is processed on a site, allowing you to modify responses to user requests
*   Runs on _all_ requests, but can be scoped to specific paths [through a `matcher` config](/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config)
*   Uses Vercel's lightweight Edge Runtime to keep costs low and responses fast

[Learn more about Routing Middleware](/docs/routing-middleware)

## [Caching](#caching)

Vercel automatically caches static files at the edge after the first request, and stores them for up to 31 days on Vercel's CDN. Dynamic content can also be cached, and both dynamic and static caching behavior can be configured with [Cache-Control headers](/docs/headers#cache-control-header).

The following Astro component will show a new time every 10 seconds. It does by setting a 10 second max age on the contents of the page, then serving stale content while new content is being rendered on the server when that age is exceeded.

[Learn more about Cache Control options](/docs/headers#cache-control-header).

src/pages/ssr-with-swr-caching.astro

```
---
Astro.response.headers.set('Cache-Control', 's-maxage=10, stale-while-revalidate');
const time = new Date().toLocaleTimeString();
---
 
<h1>{time}</h1>
```

### [CDN Cache-Control headers](#cdn-cache-control-headers)

You can also control how the cache behaves on any CDNs you may be using outside of Vercel's CDN with CDN Cache-Control Headers.

The following example tells downstream CDNs to cache the content for 60 seconds, and Vercel's CDN to cache it for 3600 seconds:

src/pages/ssr-with-swr-caching.astro

```
---
Astro.response.headers.set('Vercel-CDN-Cache-Control', 'max-age=3600',);
Astro.response.headers.set('CDN-Cache-Control', 'max-age=60',);
const time = new Date().toLocaleTimeString();
---
 
<h1>{time}</h1>
```

[Learn more about CDN Cache-Control headers](/docs/headers/cache-control-headers#cdn-cache-control-header).

Caching on Vercel:

*   Automatically optimizes and caches assets for the best performance
*   Requires no additional services to procure or set up
*   Supports zero-downtime rollouts

## [Speed Insights](#speed-insights)

[Vercel Speed Insights](/docs/speed-insights) provides you with a detailed view of your website's performance metrics, facilitating informed decisions for its optimization. By [enabling Speed Insights](/docs/speed-insights/quickstart), you gain access to the Speed Insights dashboard, which offers in-depth information about scores and individual metrics without the need for code modifications or leaving the dashboard.

To enable Speed Insights with Astro, see [the Speed Insights quickstart](/docs/speed-insights/quickstart).

To summarize, using Speed Insights with Astro on Vercel:

*   Enables you to track traffic performance metrics, such as [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](/docs/speed-insights/metrics#first-input-delay-fid)
*   Enables you to view performance metrics by page name and URL for more granular analysis
*   Shows you [a score for your app's performance](/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](/docs/speed-insights)

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying Astro projects on Vercel with the following resources:

*   [Vercel CLI](/docs/cli)
*   [Vercel Function docs](/docs/functions)
*   [Astro docs](https://docs.astro.build/en/guides/integrations-guide/vercel)

--------------------------------------------------------------------------------
title: "Create React App on Vercel"
description: "Learn how to use Vercel's features with Create React App"
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend/create-react-app"
--------------------------------------------------------------------------------

# Create React App on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Create React App (CRA) is a development environment for building single-page applications with the React framework. It sets up and configures a new React project with the latest JavaScript features, and optimizes your app for production.

## [Get Started with CRA on Vercel](#get-started-with-cra-on-vercel)

To get started with CRA on Vercel:

*   If you already have a project with CRA, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our CRA example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our CRA template, or view a live example.](/templates/react/create-react-app)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fcreate-react-app&template=create-react-app)[Live Example](https://create-react-template.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your CRA project.

## [Static file caching](#static-file-caching)

On Vercel, static files are [replicated and deployed to every region in our global CDN after the first request](/docs/edge-cache#static-files-caching). This ensures that static files are served from the closest location to the visitor, improving performance and reducing latency.

Static files are cached for up to 31 days. If a file is unchanged, it can persist across deployments, as their hash caches static files. However, the cache is effectively invalidated when you redeploy, so we always serve the latest version.

To summarize, using Static Files with CRA on Vercel:

*   Automatically optimizes and caches assets for the best performance
*   Makes files easily accessible through the `public` folder
*   Supports zero-downtime rollouts
*   Requires no additional services needed to procure or set up

[Learn more about static files caching](/docs/edge-cache#static-files-caching)

## [Preview Deployments](#preview-deployments)

When you deploy your CRA app to Vercel and connect your git repo, every pull request will generate a [Preview Deployment](/docs/deployments/environments#preview-environment-pre-production).

Preview Deployments allow you to preview changes to your app in a live deployment. They are available by default for all projects, and are generated when you commit changes to a Git branch with an open pull request, or you create a deployment [using Vercel CLI](/docs/cli/deploy#usage).

### [Comments](#comments)

You can use the comments feature to receive feedback on your Preview Deployments from Vercel Team members and [people you share the Preview URL with](/docs/comments/how-comments-work#sharing).

Comments allow you to start discussion threads, share screenshots, send notifications, and more.

To summarize, Preview Deployments with CRA on Vercel:

*   Enable you to share previews of pull request changes in a live environment
*   Come with a comment feature for improved collaboration and feedback
*   Experience changes to your product without merging them to your deployment branch

[Learn more about Preview Deployments](/docs/deployments/environments#preview-environment-pre-production)

## [Web Analytics](#web-analytics)

Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Web Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package.

You can then import the `inject` function from the package, which will add the tracking script to your app. This should only be called once in your app.

Add the following code to your main app file:

main.ts

TypeScript

TypeScriptJavaScript

```
import { inject } from '@vercel/analytics';
 
inject();
```

Then, [ensure you've enabled Web Analytics in your dashboard on Vercel](/docs/analytics/quickstart). You should start seeing usage data in your Vercel dashboard.

To summarize, using Web Analytics with CRA on Vercel:

*   Enables you to track traffic and see your top-performing pages
*   Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation and more

[Learn more about Web Analytics](/docs/analytics)

## [Speed Insights](#speed-insights)

You can see data about your CRA project's [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained) performance in your dashboard on Vercel. Doing so will allow you to track your web application's loading speed, responsiveness, and visual stability so you can improve the overall user experience.

On Vercel, you can track your app's Core Web Vitals in your project's dashboard by enabling Speed Insights.

To summarize, using Speed Insights with CRA on Vercel:

*   Enables you to track traffic performance metrics, such as [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](/docs/speed-insights/metrics#first-input-delay-fid)
*   Enables you to view performance analytics by page name and URL for more granular analysis
*   Shows you [a score for your app's performance](/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](/docs/speed-insights)

## [Observability](#observability)

Vercel's observability features help you monitor, analyze, and manage your projects. From your project's dashboard on Vercel, you can track website usage and performance, record team members' activities, and visualize real-time data from logs.

[Activity Logs](/docs/observability/activity-log), which you can see in the Activity tab of your project dashboard, are available on all account plans. The following observability products are available for Enterprise teams:

*   [Monitoring](/docs/observability/monitoring): A query editor that allows you to visualize, explore, and monitor your usage and traffic
*   [Runtime Logs](/docs/runtime-logs): An interface that allows you to search and filter logs from static requests and Function invocations
*   [Audit Logs](/docs/observability/audit-log): An interface that enables your team owners to track and analyze their team members' activity

For Pro (and Enterprise) accounts:

*   [Log Drains](/docs/drains): Export your log data for better debugging and analyzing, either from the dashboard, or using one of [our integrations](/integrations#logging)
*   [OpenTelemetry (OTEL) collector](/docs/observability/audit-log): Send OTEL traces from your Vercel functions to application performance monitoring (APM) vendors

To summarize, using Vercel's observability features with CRA enable you to:

*   Visualize website usage data, performance metrics, and logs
*   Search and filter logs for static, and Function requests
*   Use queries to see in-depth information about your website's usage and traffic
*   Send your metrics and data to other observability services through our integrations
*   Track and analyze team members' activity

[Learn more about Observability](/docs/observability)

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying CRA projects on Vercel with the following resources:

*   [Remote caching docs](/docs/monorepos/remote-caching)
*   [React with Formspree](/guides/deploying-react-forms-using-formspree-with-vercel)
*   [React Turborepo template](/templates/react/turborepo-design-system)

--------------------------------------------------------------------------------
title: "Gatsby on Vercel"
description: "Learn how to use Vercel's features with Gatsby."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend/gatsby"
--------------------------------------------------------------------------------

# Gatsby on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Gatsby is an open-source static-site generator. It enables developers to build fast and secure websites that integrate different content, APIs, and services.

Gatsby also has a large ecosystem of plugins and tools that improve the development experience. Vercel supports many Gatsby features, including [Server-Side Rendering](#server-side-rendering), [Deferred Static Generation](#deferred-static-generation), [API Routes](#api-routes), and more.

## [Get started with Gatsby on Vercel](#get-started-with-gatsby-on-vercel)

To get started with Gatsby on Vercel:

*   If you already have a project with Gatsby, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Gatsby example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Gatsby template, or view a live example.](/templates/gatsby/gatsbyjs-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fgatsby&template=gatsby)[Live Example](https://gatsby.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Gatsby project.

## [Using the Gatsby Vercel Plugin](#using-the-gatsby-vercel-plugin)

[Gatsby v4+](https://www.gatsbyjs.com/gatsby-4/) sites deployed to Vercel will automatically detect Gatsby usage and install the `@vercel/gatsby-plugin-vercel-builder` plugin.

To deploy your Gatsby site to Vercel, do not install the `@vercel/gatsby-plugin-vercel-builder` plugin yourself, or add it to your `gatsby-config.js` file.

[Gatsby v5](https://www.gatsbyjs.com/gatsby-5/) sites require Node.js 20 or higher.

Vercel persists your Gatsby project's `.cache` directory across builds.

## [Server-Side Rendering](#server-side-rendering)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, verifying authentication or checking the geolocation of an incoming request.

Vercel offers SSR that scales down resource consumption when traffic is low, and scales up with traffic surges. This protects your site from accruing costs during periods of no traffic or losing business during high-traffic periods.

### [Using Gatsby's SSR API with Vercel](#using-gatsby's-ssr-api-with-vercel)

You can server-render pages in your Gatsby application on Vercel [using Gatsby's native Server-Side Rendering API](https://www.gatsbyjs.com/docs/reference/rendering-options/server-side-rendering/). These pages will be deployed to Vercel as [Vercel functions](/docs/functions).

To server-render a Gatsby page, you must export an `async` function called `getServerData`. The function can return an object with several optional keys, [as listed in the Gatsby docs](https://www.gatsbyjs.com/docs/reference/rendering-options/server-side-rendering/#creating-server-rendered-pages). The `props` key will be available in your page's props in the `serverData` property.

The following example demonstrates a server-rendered Gatsby page using `getServerData`:

pages/example.tsx

TypeScript

TypeScriptJavaScript

```
import type { GetServerDataProps, GetServerDataReturn } from 'gatsby';
 
type ServerDataProps = {
  hello: string;
};
 
const Page = (props: PageProps) => {
  const { name } = props.serverData;
  return <div>Hello, {name}</div>;
};
 
export async function getServerData(
  props: GetServerDataProps,
): GetServerDataReturn<ServerDataProps> {
  try {
    const res = await fetch(`https://example-data-source.com/api/some-data`);
    return {
      props: await res.json(),
    };
  } catch (error) {
    return {
      status: 500,
      headers: {},
      props: {},
    };
  }
}
 
export default Page;
```

To summarize, SSR with Gatsby on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has zero-configuration support for [`Cache-Control` headers](/docs/edge-cache), including `stale-while-revalidate`
*   Framework-aware infrastructure enables switching rendering between Edge/Node.js runtimes

[Learn more about SSR](https://www.gatsbyjs.com/docs/how-to/rendering-options/using-server-side-rendering/)

## [Deferred Static Generation](#deferred-static-generation)

Deferred Static Generation (DSG) allows you to defer the generation of static pages until they are requested for the first time.

To use DSG, you must set the `defer` option to `true` in the `createPages()` function in your `gatsby-node` file.

pages/index.tsx

TypeScript

TypeScriptJavaScript

```
import type { GatsbyNode } from 'gatsby';
 
export const createPages: GatsbyNode['createPages'] = async ({ actions }) => {
  const { createPage } = actions;
  createPage({
    defer: true,
    path: '/using-dsg',
    component: require.resolve('./src/templates/using-dsg.js'),
    context: {},
  });
};
```

[See the Gatsby docs on DSG to learn more](https://www.gatsbyjs.com/docs/how-to/rendering-options/using-deferred-static-generation/#introduction).

To summarize, DSG with Gatsby on Vercel:

*   Allows you to defer non-critical page generation to user request, speeding up build times
*   Works out of the box when you deploy on Vercel
*   Can yield dramatic speed increases for large sites with content that is infrequently visited

[Learn more about DSG](https://www.gatsbyjs.com/docs/how-to/rendering-options/using-deferred-static-generation/)

## [Incremental Static Regeneration](#incremental-static-regeneration)

Gatsby supports [Deferred Static Generation](#deferred-static-generation).

The static rendered fallback pages are not generated at build time. This differentiates it from incremental static regeneration (ISR). Instead, a Vercel Function gets invoked upon page request. And the resulting response gets cached for 10 minutes. This is hard-coded and currently not configurable.

See the documentation for [Deferred Static Generation](#deferred-static-generation).

## [API routes](#api-routes)

You can add API Routes to your Gatsby site using the framework's native support for the `src/api` directory. Doing so will deploy your routes as [Vercel functions](/docs/functions). These Vercel functions can be used to fetch data from external sources, or to add custom endpoints to your application.

The following example demonstrates a basic API Route using Vercel functions:

src/api/handler.ts

TypeScript

TypeScriptJavaScript

```
import type { VercelRequest, VercelResponse } from '@vercel/node';
 
export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

To view your route locally, run the following command in your terminal:

terminal

```
gatsby develop
```

Then navigate to `http://localhost:8000/api/handler` in your web browser.

### [Dynamic API routes](#dynamic-api-routes)

Vercel does not currently have first-class support for dynamic API routes in Gatsby. For now, using them requires the workaround described in this section.

To use Gatsby's Dynamic API routes on Vercel, you must:

1.  Define your dynamic routes in a `vercel.json` file at the root directory of your project, as shown below:
    
    vercel.json
    
    ```
    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "rewrites": [
        {
          "source": "/api/blog/:id",
          "destination": "/api/blog/[id]"
        }
      ]
    }
    ```
    
2.  Read your dynamic parameters from `req.query`, as shown below:
    
    api/blog/\[id\].ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import type { VercelRequest, VercelResponse } from '@vercel/node';
     
    export default function handler(
      request: VercelRequest & { params: { id: string } },
      response: VercelResponse,
    ) {
      console.log(`/api/blog/${request.query.id}`);
      response.status(200).json({
        body: request.body,
        query: request.query,
        cookies: request.cookies,
      });
    }
    ```
    

Although typically you'd access the dynamic parameter with `request.param` when using Gatsby, you must use `request.query` on Vercel.

### [Splat API routes](#splat-api-routes)

Splat API routes are dynamic wildcard routes that will match anything after the splat (`[...]`). Vercel does not currently have first-class support for splat API routes in Gatsby. For now, using them requires the workaround described in this section.

To use Gatsby's splat API routes on Vercel, you must:

1.  Define your splat routes in a `vercel.json` file at the root directory of your project, as shown below:
    
    vercel.json
    
    ```
    {
      "$schema": "https://openapi.vercel.sh/vercel.json",
      "rewrites": [
        {
          "source": "/api/products/:path*",
          "destination": "/api/products/[...]"
        }
      ]
    }
    ```
    
2.  Read your dynamic parameters from `req.query.path`, as shown below:
    
    api/products/\[...\].ts
    
    TypeScript
    
    TypeScriptJavaScript
    
    ```
    import type { VercelRequest, VercelResponse } from '@vercel/node';
     
    export default function handler(
      request: VercelRequest & { params: { path: string } },
      response: VercelResponse,
    ) {
      console.log(`/api/products/${request.query.path}`);
      response.status(200).json({
        body: request.body,
        query: request.query,
        cookies: request.cookies,
      });
    }
    ```
    

To summarize, API Routes with Gatsby on Vercel:

*   Scale to zero when not in use
*   Scale automatically with traffic increases
*   Can be tested as Vercel Functions in your local environment

[Learn more about Gatsby API Routes](https://www.gatsbyjs.com/docs/reference/routing/creating-routes/)

## [Routing Middleware](#routing-middleware)

Gatsby does not have native framework support for using [Routing Middleware](/docs/routing-middleware).

However, you can still use Routing Middleware with your Gatsby site by creating a `middeware.js` or `middeware.ts` file in your project's root directory.

The following example demonstrates middleware that adds security headers to responses sent to users who visit the `/example` route in your Gatsby application:

middleware.ts

TypeScript

TypeScriptJavaScript

```
import { next } from '@vercel/functions';
 
export const config = {
  // Only run the middleware on the example route
  matcher: '/example',
};
 
export default function middleware(request: Request): Response {
  return next({
    headers: {
      'Referrer-Policy': 'origin-when-cross-origin',
      'X-Frame-Options': 'DENY',
      'X-Content-Type-Options': 'nosniff',
      'X-DNS-Prefetch-Control': 'on',
      'Strict-Transport-Security':
        'max-age=31536000; includeSubDomains; preload',
    },
  });
}
```

To summarize, Routing Middleware with Gatsby on Vercel:

*   Executes before a request is processed on a site, allowing you to modify responses to user requests
*   Runs on _all_ requests, but can be scoped to specific paths [through a `matcher` config](/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config)
*   Uses our lightweight Edge Runtime to keep costs low and responses fast

[Learn more about Routing Middleware](/docs/routing-middleware)

## [Speed Insights](#speed-insights)

[Core Web Vitals](/docs/speed-insights) are supported for Gatsby v4+ projects with no initial configuration necessary.

When you deploy a Gatsby v4+ site on Vercel, we automatically install the `@vercel/gatsby-plugin-vercel-analytics` package and add it to the `plugins` array in your `gatsby-config.js` file.

We do not recommend installing the Gatsby analytics plugin yourself.

To access your Core Web Vitals data, you must enable Vercel analytics in your project's dashboard. [See our quickstart guide to do so now](/docs/analytics/quickstart).

To summarize, using Speed Insights with Gatsby on Vercel:

*   Enables you to track traffic performance metrics, such as [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](/docs/speed-insights/metrics#first-input-delay-fid)
*   Enables you to view performance analytics by page name and URL for more granular analysis
*   Shows you [a score for your app's performance](/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](/docs/speed-insights)

## [Image Optimization](#image-optimization)

While Gatsby [does provide an Image plugin](https://www.gatsbyjs.com/plugins/gatsby-plugin-image), it is not currently compatible with Vercel Image Optimization.

If this is something your team is interested in, [please contact our sales team](/contact/sales).

[Learn more about Image Optimization](/docs/image-optimization)

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

*   [Build Output API](/docs/build-output-api/v3)

--------------------------------------------------------------------------------
title: "React Router on Vercel"
description: "Learn how to use Vercel's features with React Router as a framework."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend/react-router"
--------------------------------------------------------------------------------

# React Router on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

React Router is a multi-strategy router for React. When used [as a framework](https://reactrouter.com/home#react-router-as-a-framework), React Router enables fullstack, [server-rendered](#server-side-rendering-ssr) React applications. Its built-in features for nested pages, error boundaries, transitions between loading states, and more, enable developers to create modern web apps.

With Vercel, you can deploy React Router applications with server-rendering or static site generation (using [SPA mode](https://reactrouter.com/how-to/spa)) to Vercel with zero configuration.

It is highly recommended that your application uses the [Vercel Preset](#vercel-react-router-preset) when deploying to Vercel.

## [`@vercel/react-router`](#@vercel/react-router)

The optional `@vercel/react-router` package contains Vercel specific utilities for use in React Router applications. The package contains various entry points for specific use cases:

*   `@vercel/react-router/vite` import
    *   Contains the [Vercel Preset](#vercel-react-router-preset) to enhance React Router functionality on Vercel
*   `@vercel/react-router/entry.server` import
    *   For situations where you need to [define a custom `entry.server` file](#using-a-custom-app/entry.server-file).

To get started, navigate to the root directory of your React Router project with your terminal and install `@vercel/react-router` with your preferred package manager:

pnpmyarnnpmbun

```
pnpm i @vercel/react-router
```

## [Vercel React Router Preset](#vercel-react-router-preset)

When using the [React Router](https://reactrouter.com/start/framework/installation) as a framework, you should configure the Vercel Preset to enable the full feature set that Vercel offers.

To configure the Preset, add the following lines to your `react-router.config` file:

/react-router.config.ts

```
import { vercelPreset } from '@vercel/react-router/vite';
import type { Config } from '@react-router/dev/config';
 
export default {
  // Config options...
  // Server-side render by default, to enable SPA mode set this to `false`
  ssr: true,
  presets: [vercelPreset()],
} satisfies Config;
```

When this Preset is configured, your React Router application is enhanced with Vercel-specific functionality:

*   Allows function-level configuration (i.e. `memory`, `maxDuration`, etc.) on a per-route basis
*   Allows Vercel to understand the routing structure of the application, which allows for bundle splitting
*   Accurate "Deployment Summary" on the deployment details page

## [Server-Side Rendering (SSR)](#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request. Server-Side Rendering is invoked using [Vercel Functions](/docs/functions).

[Routes](https://reactrouter.com/start/framework/routing) defined in your application are deployed with server-side rendering by default.

The following example demonstrates a basic route that renders with SSR:

/app/routes.ts

TypeScript

TypeScriptJavaScript

```
import { type RouteConfig, index } from '@react-router/dev/routes';
 
export default [index('routes/home.tsx')] satisfies RouteConfig;
```

/app/routes/home.tsx

TypeScript

TypeScriptJavaScript

```
import type { Route } from './+types/home';
import { Welcome } from '../welcome/welcome';
 
export function meta({}: Route.MetaArgs) {
  return [
    { title: 'New React Router App' },
    { name: 'description', content: 'Welcome to React Router!' },
  ];
}
 
export default function Home() {
  return <Welcome />;
}
```

To summarize, Server-Side Rendering (SSR) with React Router on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has framework-aware infrastructure to generate Vercel Functions
*   Supports the use of Vercel's [Fluid compute](/docs/fluid-compute) for enhanced performance

## [Response streaming](#response-streaming)

[Streaming HTTP responses](/docs/functions/streaming-functions)

with React Router on Vercel is supported with Vercel Functions. See the [Streaming with Suspense](https://reactrouter.com/how-to/suspense) page in the React Router docs for general instructions.

Streaming with React Router on Vercel:

*   Offers faster Function response times, improving your app's user experience
*   Allows you to return large amounts of data without exceeding Vercel Function response size limits
*   Allows you to display Instant Loading UI from the server with React Router's `<Await>`

[Learn more about Streaming](/docs/functions/streaming)

## [`Cache-Control` headers](#cache-control-headers)

Vercel's [CDN](/docs/cdn) caches your content at the edge in order to serve data to your users as fast as possible. [Static caching](/docs/edge-cache#static-files-caching) works with zero configuration.

By adding a `Cache-Control` header to responses returned by your React Router routes, you can specify a set of caching rules for both client (browser) requests and server responses. A cache must obey the requirements defined in the Cache-Control header.

React Router supports defining response headers by exporting a [headers](https://reactrouter.com/how-to/headers) function within a route.

The following example demonstrates a route that adds `Cache-Control` headers which instruct the route to:

*   Return cached content for requests repeated within 1 second without revalidating the content
*   For requests repeated after 1 second, but before 60 seconds have passed, return the cached content and mark it as stale. The stale content will be revalidated in the background with a fresh value from your [`loader`](https://reactrouter.com/start/framework/route-module#loader) function

/app/routes/example.tsx

TypeScript

TypeScriptJavaScript

```
import { Route } from './+types/some-route';
 
export function headers(_: Route.HeadersArgs) {
  return {
    'Cache-Control': 's-maxage=1, stale-while-revalidate=59',
  };
}
 
export async function loader() {
  // Fetch data necessary to render content
}
```

See [our docs on cache limits](/docs/edge-cache#limits) to learn the max size and lifetime of caches stored on Vercel.

To summarize, using `Cache-Control` headers with React Router on Vercel:

*   Allow you to cache responses for server-rendered React Router apps using Vercel Functions
*   Allow you to serve content from the cache _while updating the cache in the background_ with `stale-while-revalidate`

[Learn more about caching](/docs/edge-cache#how-to-cache-responses)

## [Analytics](#analytics)

[Vercel's Analytics](/docs/analytics) features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your React Router project:

pnpmyarnnpmbun

```
pnpm i @vercel/analytics
```

Then, follow the instructions below to add the `Analytics` component to your app. The `Analytics` component is a wrapper around Vercel's tracking script, offering a seamless integration with React Router.

Add the following component to your `root` file:

app/root.tsx

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/react';
 
export default function App() {
  return (
    <html lang="en">
      <body>
        <Analytics />
      </body>
    </html>
  );
}
```

To summarize, Analytics with React Router on Vercel:

*   Enables you to track traffic and see your top-performing pages
*   Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation and more

[Learn more about Analytics](/docs/analytics)

## [Using a custom server entrypoint](#using-a-custom-server-entrypoint)

Your React Router application may define a custom server entrypoint, which is useful for supplying a "load context" for use by the application's loaders and actions.

The server entrypoint file is expected to export a Web API-compatible function that matches the following signature:

```
export default async function (request: Request) => Response | Promise<Response>;
```

To implement a server entrypoint using the [Hono web framework](https://hono.dev), follow these steps:

First define the `build.rollupOptions.input` property in your Vite config file:

/vite.config.ts

TypeScript

TypeScriptJavaScript

```
import { reactRouter } from '@react-router/dev/vite';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';
 
export default defineConfig(({ isSsrBuild }) => ({
  build: {
    rollupOptions: isSsrBuild
      ? {
          input: './server/app.ts',
        }
      : undefined,
  },
  plugins: [tailwindcss(), reactRouter(), tsconfigPaths()],
}));
```

Then, create the server entrypoint file:

/server/app.ts

TypeScript

TypeScriptJavaScript

```
import { Hono } from 'hono';
import { createRequestHandler } from 'react-router';
 
// @ts-expect-error - virtual module provided by React Router at build time
import * as build from 'virtual:react-router/server-build';
 
declare module 'react-router' {
  interface AppLoadContext {
    VALUE_FROM_HONO: string;
  }
}
 
const app = new Hono();
 
// Add any additional Hono middleware here
 
const handler = createRequestHandler(build);
app.mount('/', (req) =>
  handler(req, {
    // Add your "load context" here based on the current request
    VALUE_FROM_HONO: 'Hello from Hono',
  }),
);
 
export default app.fetch;
```

To summarize, using a custom server entrypoint with React Router on Vercel allows you to:

*   Supply a "load context" for use in your `loader` and `action` functions
*   Use a Web API-compatible framework alongside your React Router application

## [Using a custom `app/entry.server` file](#using-a-custom-app/entry.server-file)

By default, Vercel supplies an implementation of the `entry.server` file which is configured for streaming to work with Vercel Functions. This version will be used when no `entry.server` file is found in the project.

However, your application may define a customized `app/entry.server.jsx` or `app/entry.server.tsx` file if necessary. When doing so, your custom `entry.server` file should use the `handleRequest` function exported by `@vercel/react-router/entry.server`.

For example, to supply the `nonce` option and set the corresponding `Content-Security-Policy` response header:

/app/entry.server.tsx

TypeScript

TypeScriptJavaScript

```
import { handleRequest } from '@vercel/react-router/entry.server';
import type { AppLoadContext, EntryContext } from 'react-router';
 
export default async function (
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  routerContext: EntryContext,
  loadContext?: AppLoadContext,
): Promise<Response> {
  const nonce = crypto.randomUUID();
  const response = await handleRequest(
    request,
    responseStatusCode,
    responseHeaders,
    routerContext,
    loadContext,
    { nonce },
  );
  response.headers.set(
    'Content-Security-Policy',
    `script-src 'nonce-${nonce}'`,
  );
  return response;
}
```

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying React Router projects on Vercel with the following resources:

*   [Explore the React Router docs](https://reactrouter.com/home)

--------------------------------------------------------------------------------
title: "Vite on Vercel"
description: "Learn how to use Vercel's features with Vite."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/frontend/vite"
--------------------------------------------------------------------------------

# Vite on Vercel

Copy page

Ask AI about this page

Last updated October 1, 2025

Vite is an opinionated build tool that aims to provide a faster and leaner development experience for modern web projects. Vite provides a dev server with rich feature enhancements such as pre-bundling NPM dependencies and hot module replacement, and a build command that bundles your code and outputs optimized static assets for production.

These features make Vite more desirable than out-of-the-box CLIs when building larger projects with frameworks for many developers.

Vite powers popular frameworks like [SvelteKit](/docs/frameworks/sveltekit), and is often used in large projects built with [Vue](/guides/deploying-vuejs-to-vercel), [Svelte](/docs/frameworks/sveltekit), [React](/docs/frameworks/create-react-app), [Preact](/guides/deploying-preact-with-vercel), [and more](https://github.com/vitejs/vite/tree/main/packages/create-vite).

## [Getting started](#getting-started)

To get started with Vite on Vercel:

*   If you already have a project with Vite, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Vite example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Vite template, or view a live example.](/templates/vue/vite-vue)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fvite&template=vite)[Live Example](https://vite-vue-template.vercel.app)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Vite project.

## [Using Vite community plugins](#using-vite-community-plugins)

Although Vite offers modern features like [SSR](#server-side-rendering-ssr) and [Vercel functions](#vercel-functions) out of the box, implementing those features can sometimes require complex configuration steps. Because of this, many Vite users prefer to use [popular community plugins](https://github.com/vitejs/awesome-vite#readme).

Vite's plugins are based on [Rollup's plugin interface](https://rollupjs.org/javascript-api/), giving Vite users access to [many tools from the Rollup ecosystem](https://vite-rollup-plugins.patak.dev/) as well as the [Vite-specific ecosystem](https://github.com/vitejs/awesome-vite#readme).

We recommend using Vite plugins to configure your project when possible.

### [`vite-plugin-vercel`](#vite-plugin-vercel)

[`vite-plugin-vercel`](https://github.com/magne4000/vite-plugin-vercel#readme) is a popular community Vite plugin that implements [the Build Output API spec](/docs/build-output-api/v3). It enables your Vite apps to use the following Vercel features:

*   [Server-Side Rendering (SSR)](#server-side-rendering-ssr)
*   [Vercel functions](#vercel-functions)
*   [Incremental Static Regeneration](/docs/incremental-static-regeneration)
*   [Static Site Generation](/docs/build-output-api/v3/primitives#static-files)

When using the Vercel CLI, set the port as an environment variable. To allow Vite to access this, include the environment variable in your `vite.config` file:

vite.config.ts

TypeScript

TypeScriptJavaScript

```
import { defineConfig } from 'vite';
import vercel from 'vite-plugin-vercel';
 
export default defineConfig({
  server: {
    port: process.env.PORT as unknown as number,
  },
  plugins: [vercel()],
});
```

### [`vite-plugin-ssr`](#vite-plugin-ssr)

[`vite-plugin-ssr`](https://vite-plugin-ssr.com/) is another popular community Vite plugin that implements [the Build Output API spec](/docs/build-output-api/v3). It enables your Vite apps to do the following:

*   [Server-Side Rendering (SSR)](#server-side-rendering-ssr)
*   [Vercel functions](#vercel-functions)
*   [Static Site Generation](/docs/build-output-api/v3/primitives#static-files)

## [Environment Variables](#environment-variables)

Vercel provides a set of [System Environment Variables](/docs/environment-variables/system-environment-variables) that our platform automatically populates. For example, the `VERCEL_GIT_PROVIDER` variable exposes the Git provider that triggered your project's deployment on Vercel.

These environment variables will be available to your project automatically, and you can enable or disable them in your project settings on Vercel. See [our Environment Variables docs](/docs/environment-variables) to learn how.

To access Vercel's System Environment Variables in Vite during the build process, prefix the variable name with `VITE`. For example, `VITE_VERCEL_ENV` will return `preview`, `production`, or `development` depending on which environment the app is running in.

The following example demonstrates a Vite config file that sets `VITE_VERCEL_ENV` as a global constant available throughout the app:

vite.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineConfig(() => {
  return {
    define: {
      __APP_ENV__: process.env.VITE_VERCEL_ENV,
    },
  };
});
```

If you want to read environment variables from a `.env` file, additional configuration is required. See [the Vite config docs](https://vitejs.dev/config/#using-environment-variables-in-config) to learn more.

To summarize, the benefits of using System Environment Variables with Vite on Vercel include:

*   Access to Vercel deployment information, dynamically or statically, with our preconfigured System Environment Variables
*   Access to automatically-configured environment variables provided by [integrations for your preferred services](/docs/environment-variables#integration-environment-variables)
*   Searching and filtering environment variables by name and environment in Vercel's dashboard

[Learn more about System Environment Variables](/docs/environment-variables/system-environment-variables)

## [Vercel Functions](#vercel-functions)

Vercel Functions scale up and down their resource consumption based on traffic demands. This scaling prevents them from failing during peak hours, but keeps them from running up high costs during periods of low activity.

If your project uses [a Vite community plugin](#using-vite-community-plugins), such as [`vite-plugin-ssr`](https://vite-plugin-ssr.com/), you should follow that plugin's documentation for using Vercel Functions.

If you're using a framework built on Vite, check that framework's official documentation or [our dedicated framework docs](/docs/frameworks). Some frameworks built on Vite, such as [SvelteKit](/docs/frameworks/sveltekit), support Functions natively. We recommend using that framework's method for implementing Functions.

If you're not using a framework or plugin that supports Vercel Functions, you can still use them in your project by creating routes in an `api` directory at the root of your project.

The following example demonstrates a basic Vercel Function defined in an `api` directory:

api/handler.ts

TypeScript

TypeScriptJavaScript

```
import type { VercelRequest, VercelResponse } from '@vercel/node';
 
export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

To summarize, Vercel Functions on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Support standard [Web APIs](https://developer.mozilla.org/docs/Web/API), such as `URLPattern`, `Response`, and more

[Learn more about Vercel Functions](/docs/functions)

## [Server-Side Rendering (SSR)](#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

Vite exposes [a low-level API for implementing SSR](https://vitejs.dev/guide/ssr.html#server-side-rendering), but in most cases, we recommend [using a Vite community plugin](#using-vite-community-plugins).

See [the SSR section of Vite's plugin repo](https://github.com/vitejs/awesome-vite#ssr) for a more comprehensive list of SSR plugins.

To summarize, SSR with Vite on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has zero-configuration support for [`Cache-Control`](/docs/edge-cache) headers, including `stale-while-revalidate`

[Learn more about SSR](https://vitejs.dev/guide/ssr.html)

## [Using Vite to make SPAs](#using-vite-to-make-spas)

If your Vite app is [configured to deploy as a Single Page Application (SPA)](https://vitejs.dev/config/shared-options.html#apptype), deep linking won't work out of the box.

To enable deep linking in SPA Vite apps, create a `vercel.json` file at the root of your project, and add the following code:

vercel.json

```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

If [`cleanUrls`](/docs/project-configuration#cleanurls) is set to `true` in your project's `vercel.json`, do not include the file extension in the source or destination path. For example, `/index.html` would be `/`

Deploying your app in Multi-Page App mode is recommended for production builds.

Learn more about [Mutli-Page App mode](https://vitejs.dev/guide/build.html#multi-page-app) in the Vite docs.

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying Vite projects on Vercel with the following resources:

*   [Explore Vite's template repo](https://github.com/vitejs/vite/tree/main/packages/create-vite)

--------------------------------------------------------------------------------
title: "Full-stack frameworks on Vercel"
description: "Vercel supports a wide range of the most popular backend frameworks, optimizing how your application builds and runs no matter what tooling you use."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack"
--------------------------------------------------------------------------------

# Full-stack frameworks on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

The following full-stack frameworks are supported with zero-configuration.

![Next.js](https://api-frameworks.vercel.sh/framework-logos/next.svg)

### Next.js

Next.js makes you productive with React instantly — whether you want to build static or dynamic sites.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nextjs)[View Demo](https://nextjs-template.vercel.app)

![Nuxt](https://api-frameworks.vercel.sh/framework-logos/nuxt.svg)

### Nuxt

Nuxt is the open source framework that makes full-stack development with Vue.js intuitive.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/nuxtjs)[View Demo](https://nuxtjs-template.vercel.app)

![RedwoodJS](https://api-frameworks.vercel.sh/framework-logos/redwoodjs.svg)

### RedwoodJS

RedwoodJS is a full-stack framework for the Jamstack.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/redwoodjs)[View Demo](https://redwood-template.vercel.app)

![Remix](https://api-frameworks.vercel.sh/framework-logos/remix-no-shadow.svg)

### Remix

Build Better Websites

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/remix)[View Demo](https://remix-run-template.vercel.app)

![SvelteKit](https://api-frameworks.vercel.sh/framework-logos/svelte.svg)

### SvelteKit

SvelteKit is a framework for building web applications of all sizes.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/sveltekit-1)[View Demo](https://sveltekit-1-template.vercel.app)

![TanStack Start](https://api-frameworks.vercel.sh/framework-logos/tanstack-start.svg)![TanStack Start](https://api-frameworks.vercel.sh/framework-logos/tanstack-start-dark.svg)

### TanStack Start

Full-stack Framework powered by TanStack Router for React and Solid.

[Deploy](https://vercel.com/new/clone?repository-url=https://github.com/vercel/vercel/tree/main/examples/tanstack-start)View Demo

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

--------------------------------------------------------------------------------
title: "Next.js on Vercel"
description: "Vercel is the native Next.js platform, designed to enhance the Next.js experience."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack/nextjs"
--------------------------------------------------------------------------------

# Next.js on Vercel

Copy page

Ask AI about this page

Last updated October 9, 2025

[Next.js](https://nextjs.org/) is a fullstack React framework for the web, maintained by Vercel.

While Next.js works when self-hosting, deploying to Vercel is zero-configuration and provides additional enhancements for scalability, availability, and performance globally.

## [Getting started](#getting-started)

To get started with Next.js on Vercel:

*   If you already have a project with Next.js, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Next.js example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Next.js template, or view a live example.](/templates/next.js/nextjs-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnextjs&template=nextjs)[Live Example](https://nextjs-template.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Next.js project.

## [Incremental Static Regeneration](#incremental-static-regeneration)

[Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) allows you to create or update content _without_ redeploying your site. ISR has three main benefits for developers: better performance, improved security, and faster build times.

When self-hosting, (ISR) is limited to a single region workload. Statically generated pages are not distributed closer to visitors by default, without additional configuration or vendoring of a CDN. By default, self-hosted ISR does _not_ persist generated pages to durable storage. Instead, these files are located in the Next.js cache (which expires).

To enable ISR with Next.js in the `app` router, add an options object with a `revalidate` property to your `fetch` requests:

Next.js (/app)Next.js (/pages)

apps/example/page.tsx

TypeScript

TypeScriptJavaScript

```
export default async function Page() {
  const res = await fetch('https://api.vercel.app/blog', {
    next: { revalidate: 10 }, // Seconds
  });
 
  const data = await res.json();
 
  return (
    <main>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}
```

To summarize, using ISR with Next.js on Vercel:

*   Better performance with our global [CDN](/docs/cdn)
*   Zero-downtime rollouts to previously statically generated pages
*   Framework-aware infrastructure enables global content updates in 300ms
*   Generated pages are both cached and persisted to durable storage

[Learn more about Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration)

## [Server-Side Rendering (SSR)](#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

On Vercel, you can server-render Next.js applications through [Vercel Functions](/docs/functions).

To summarize, SSR with Next.js on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has zero-configuration support for [`Cache-Control` headers](/docs/edge-cache), including `stale-while-revalidate`
*   Framework-aware infrastructure enables automatic creation of Functions for SSR

[Learn more about SSR](https://nextjs.org/docs/app/building-your-application/rendering#static-and-dynamic-rendering-on-the-server)

## [Streaming](#streaming)

Vercel supports streaming in Next.js projects with any of the following:

*   [Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/router-handlers)
*   [Vercel Functions](/docs/functions/streaming-functions)
*   React Server Components

Streaming data allows you to fetch information in chunks rather than all at once, speeding up Function responses. You can use streams to improve your app's user experience and prevent your functions from failing when fetching large files.

#### [Streaming with `loading` and `Suspense`](#streaming-with-loading-and-suspense)

In the Next.js App Router, you can use the `loading` file convention or a `Suspense` component to show an instant loading state from the server while the content of a route segment loads.

The `loading` file provides a way to show a loading state for a whole route or route-segment, instead of just particular sections of a page. This file affects all its child elements, including layouts and pages. It continues to display its contents until the data fetching process in the route segment completes.

The following example demonstrates a basic `loading` file:

loading.tsx

TypeScript

TypeScriptJavaScript

```
export default function Loading() {
  return <p>Loading...</p>;
}
```

Learn more about loading in the [Next.js docs](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming).

The `Suspense` component, introduced in React 18, enables you to display a fallback until components nested within it have finished loading. Using `Suspense` is more granular than showing a loading state for an entire route, and is useful when only sections of your UI need a loading state.

You can specify a component to show during the loading state with the `fallback` prop on the `Suspense` component as shown below:

app/dashboard/page.tsx

TypeScript

TypeScriptJavaScript

```
import { Suspense } from 'react';
import { PostFeed, Weather } from './components';
 
export default function Posts() {
  return (
    <section>
      <Suspense fallback={<p>Loading feed...</p>}>
        <PostFeed />
      </Suspense>
      <Suspense fallback={<p>Loading weather...</p>}>
        <Weather />
      </Suspense>
    </section>
  );
}
```

To summarize, using Streaming with Next.js on Vercel:

*   Speeds up Function response times, improving your app's user experience
*   Display initial loading UI with incremental updates from the server as new data becomes available

Learn more about [Streaming](/docs/functions/streaming-functions) with Vercel Functions.

## [Partial Prerendering](#partial-prerendering)

Partial Prerendering as an experimental feature. It is currently **not suitable for production** environments.

Partial Prerendering (PPR) is an experimental feature in Next.js that allows the static portions of a page to be pre-generated and served from the cache, while the dynamic portions are streamed in a single HTTP request.

When a user visits a route:

*   A static route _shell_ is served immediately, this makes the initial load fast.
*   The shell leaves _holes_ where dynamic content will be streamed in to minimize the perceived overall page load time.
*   The async holes are loaded in parallel, reducing the overall load time of the page.

This approach is useful for pages like dashboards, where unique, per-request data coexists with static elements such as sidebars or layouts. This is different from how your application behaves today, where entire routes are either fully static or dynamic.

See the [Partial Prerendering docs](https://nextjs.org/docs/app/api-reference/next-config-js/partial-prerendering) to learn more.

## [Image Optimization](#image-optimization)

[Image Optimization](/docs/image-optimization) helps you achieve faster page loads by reducing the size of images and using modern image formats.

When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and [Core Web Vitals](/docs/speed-insights).

When self-hosting, Image Optimization uses the default Next.js server for optimization. This server manages the rendering of pages and serving of static files.

To use Image Optimization with Next.js on Vercel, import the `next/image` component into the component you'd like to add an image to, as shown in the following example:

Next.js (/app)Next.js (/pages)

components/ExampleComponent.tsx

TypeScript

TypeScriptJavaScript

```
import Image from 'next/image';
 
interface ExampleProps {
  name: string;
}
 
const ExampleComponent = ({ name }: ExampleProps) => {
  return (
    <>
      <Image
        src="example.png"
        alt="Example picture"
        width={500}
        height={500}
      />
      <span>{name}</span>
    </>
  );
};
 
export default ExampleComponent;
```

To summarize, using Image Optimization with Next.js on Vercel:

*   Zero-configuration Image Optimization when using `next/image`
*   Helps your team ensure great performance by default
*   Keeps your builds fast by optimizing images on-demand
*   Requires No additional services needed to procure or set up

[Learn more about Image Optimization](/docs/image-optimization)

## [Font Optimization](#font-optimization)

[`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) enables built-in automatic self-hosting for any font file. This means you can optimally load web fonts with zero [layout shift](/docs/speed-insights/metrics#cumulative-layout-shift-cls), thanks to the underlying CSS [`size-adjust`](https://developer.mozilla.org/docs/Web/CSS/@font-face/size-adjust) property.

This also allows you to use all [Google Fonts](https://fonts.google.com/) with performance and privacy in mind. CSS and font files are downloaded at build time and self-hosted with the rest of your static files. No requests are sent to Google by the browser.

Next.js (/app)Next.js (/pages)

app/layout.tsx

TypeScript

TypeScriptJavaScript

```
import { Inter } from 'next/font/google';
 
// If loading a variable font, you don't need to specify the font weight
const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
});
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.className}>
      <body>{children}</body>
    </html>
  );
}
```

To summarize, using Font Optimization with Next.js on Vercel:

*   Enables built-in, automatic self-hosting for font files
*   Loads web fonts with zero layout shift
*   Allows for CSS and font files to be downloaded at build time and self-hosted with the rest of your static files
*   Ensures that no requests are sent to Google by the browser

[Learn more about Font Optimization](https://nextjs.org/docs/app/building-your-application/optimizing/fonts)

## [Open Graph Images](#open-graph-images)

Dynamic social card images (using the [Open Graph protocol](/docs/og-image-generation)) allow you to create a unique image for every page of your site. This is useful when sharing links on the web through social platforms or through text message.

The [Vercel OG](/docs/og-image-generation) image generation library allows you generate fast, dynamic social card images using Next.js API Routes.

The following example demonstrates using OG image generation in both the Next.js Pages and App Router:

Next.js (/app)Next.js (/pages)

app/api/og/route.tsx

TypeScript

TypeScriptJavaScript

```
import { ImageResponse } from 'next/og';
// App router includes @vercel/og.
// No need to install it.
 
export async function GET(request: Request) {
  return new ImageResponse(
    (
      <div
        style={{
          fontSize: 128,
          background: 'white',
          width: '100%',
          height: '100%',
          display: 'flex',
          textAlign: 'center',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        Hello world!
      </div>
    ),
    {
      width: 1200,
      height: 600,
    },
  );
}
```

To see your generated image, run `npm run dev` in your terminal and visit the `/api/og` route in your browser (most likely `http://localhost:3000/api/og`).

To summarize, the benefits of using Vercel OG with Next.js include:

*   Instant, dynamic social card images without needing headless browsers
*   Generated images are automatically cached on the Vercel CDN
*   Image generation is co-located with the rest of your frontend codebase

[Learn more about OG Image Generation](/docs/og-image-generation)

## [Middleware](#middleware)

[Middleware](/docs/routing-middleware) is code that executes before a request is processed. Because Middleware runs before the cache, it's an effective way of providing personalization to statically generated content.

When deploying middleware with Next.js on Vercel, you get access to built-in helpers that expose each request's geolocation information. You also get access to the `NextRequest` and `NextResponse` objects, which enable rewrites, continuing the middleware chain, and more.

See [the Middleware API docs](/docs/routing-middleware/api) for more information.

To summarize, Middleware with Next.js on Vercel:

*   Runs using [Middleware](/docs/routing-middleware) which are deployed globally
*   Replaces needing additional services for customizable routing rules
*   Helps you achieve the best performance for serving content globally

[Learn more about Middleware](/docs/routing-middleware)

## [Draft Mode](#draft-mode)

[Draft Mode](/docs/draft-mode) enables you to view draft content from your [Headless CMS](/docs/solutions/cms) immediately, while still statically generating pages in production.

See [our Draft Mode docs](/docs/draft-mode#getting-started) to learn how to use it with Next.js.

### [Self-hosting Draft Mode](#self-hosting-draft-mode)

When self-hosting, every request using Draft Mode hits the Next.js server, potentially incurring extra load or cost. Further, by spoofing the cookie, malicious users could attempt to gain access to your underlying Next.js server.

### [Draft Mode security](#draft-mode-security)

Deployments on Vercel automatically secure Draft Mode behind the same authentication used for Preview Comments. In order to enable or disable Draft Mode, the viewer must be logged in as a member of the [Team](/docs/teams-and-accounts). Once enabled, Vercel's CDN will bypass the ISR cache automatically and invoke the underlying [Vercel Function](/docs/functions).

### [Enabling Draft Mode in Preview Deployments](#enabling-draft-mode-in-preview-deployments)

You and your team members can toggle Draft Mode in the Vercel Toolbar in [production](/docs/vercel-toolbar/in-production-and-localhost/add-to-production), [localhost](/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost), and [Preview Deployments](/docs/deployments/environments#preview-environment-pre-production#comments). When you do so, the toolbar will become purple to indicate Draft Mode is active.

![The Vercel toolbar when Draft Mode is enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-light.png&w=828&q=75)![The Vercel toolbar when Draft Mode is enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-dark.png&w=828&q=75)

The Vercel toolbar when Draft Mode is enabled.

Users outside your Vercel team cannot toggle Draft Mode.

To summarize, the benefits of using Draft Mode with Next.js on Vercel include:

*   Easily server-render previews of static pages
*   Adds additional security measures to prevent malicious usage
*   Integrates with any headless provider of your choice
*   You can enable and disable Draft Mode in [the comments toolbar](/docs/comments/how-comments-work) on Preview Deployments

[Learn more about Draft Mode](/docs/draft-mode)

## [Web Analytics](#web-analytics)

Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Web Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your Next.js project:

pnpmyarnnpmbun

```
pnpm i @vercel/analytics
```

Then, follow the instructions below to add the `Analytics` component to your app either using the `pages` directory or the `app` directory.

The `Analytics` component is a wrapper around the tracking script, offering more seamless integration with Next.js, including route support.

Add the following code to the root layout:

Next.js (/app)Next.js (/pages)

app/layout.tsx

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/next';
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

To summarize, Web Analytics with Next.js on Vercel:

*   Enables you to track traffic and see your top-performing pages
*   Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation, and more

[Learn more about Web Analytics](/docs/analytics)

## [Speed Insights](#speed-insights)

You can see data about your project's [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained) performance in your dashboard on Vercel. Doing so will allow you to track your web application's loading speed, responsiveness, and visual stability so you can improve the overall user experience.

On Vercel, you can track your Next.js app's Core Web Vitals in your project's dashboard.

### [reportWebVitals](#reportwebvitals)

If you're self-hosting your app, you can use the [`useWebVitals`](https://nextjs.org/docs/advanced-features/measuring-performance#build-your-own) hook to send metrics to any analytics provider. The following example demonstrates a custom `WebVitals` component that you can use in your app's root `layout` file:

app/\_components/web-vitals.tsx

TypeScript

TypeScriptJavaScript

```
'use client';
 
import { useReportWebVitals } from 'next/web-vitals';
 
export function WebVitals() {
  useReportWebVitals((metric) => {
    console.log(metric);
  });
}
```

You could then reference your custom `WebVitals` component like this:

app/layout.ts

TypeScript

TypeScriptJavaScript

```
import { WebVitals } from './_components/web-vitals';
 
export default function Layout({ children }) {
  return (
    <html>
      <body>
        <WebVitals />
        {children}
      </body>
    </html>
  );
}
```

Next.js uses [Google's `web-vitals` library](https://github.com/GoogleChrome/web-vitals#web-vitals) to measure the Web Vitals metrics available in `reportWebVitals`.

To summarize, tracking Web Vitals with Next.js on Vercel:

*   Enables you to track traffic performance metrics, such as [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](/docs/speed-insights/metrics#first-input-delay-fid)
*   Enables you to view performance analytics by page name and URL for more granular analysis
*   Shows you [a score for your app's performance](/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](/docs/speed-insights)

## [Service integrations](#service-integrations)

Vercel has partnered with popular service providers, such as MongoDB and Sanity, to create integrations that make using those services with Next.js easier. There are many integrations across multiple categories, such as [Commerce](/integrations#commerce), [Databases](/integrations#databases), and [Logging](/integrations#logging).

To summarize, Integrations on Vercel:

*   Simplify the process of connecting your preferred services to a Vercel project
*   Help you achieve the optimal setup for a Vercel project using your preferred service
*   Configure your environment variables for you

[Learn more about Integrations](/integrations)

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying Next.js projects on Vercel with the following resources:

*   [Build a fullstack Next.js app](/guides/nextjs-prisma-postgres)
*   [Build a multi-tenant app](/docs/multi-tenant)
*   [Next.js with Contenful](/guides/integrating-next-js-and-contentful-for-your-headless-cms)
*   [Next.js with Stripe Checkout and Typescript](/guides/getting-started-with-nextjs-typescript-stripe)
*   [Next.js with Magic.link](/guides/add-auth-to-nextjs-with-magic)
*   [Generate a sitemap with Next.js](/guides/how-do-i-generate-a-sitemap-for-my-nextjs-app-on-vercel)
*   [Next.js ecommerce with Shopify](/guides/deploying-locally-built-nextjs)
*   [Deploy a locally built Next.js app](/guides/deploying-locally-built-nextjs)
*   [Deploying Next.js to Vercel](https://www.youtube.com/watch?v=AiiGjB2AxqA)
*   [Learn about combining static and dynamic rendering on the same page in Next.js 14](https://www.youtube.com/watch?v=wv7w_Zx-FMU)
*   [Learn about suspense boundaries and streaming when loading your UI](https://nextjs.org/docs/app/building-your-application/routing/loading-ui-and-streaming)

--------------------------------------------------------------------------------
title: "Nuxt on Vercel"
description: "Learn how to use Vercel's features with Nuxt."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack/nuxt"
--------------------------------------------------------------------------------

# Nuxt on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Nuxt is an open-source framework that streamlines the process of creating modern Vue apps. It offers server-side rendering, SEO features, automatic code splitting, prerendering, and more out of the box. It also has [an extensive catalog of community-built modules](https://nuxt.com/modules), which allow you to integrate popular tools with your projects.

You can deploy Nuxt static and server-side rendered sites on Vercel with no configuration required.

## [Getting started](#getting-started)

To get started with Nuxt on Vercel:

*   If you already have a project with Nuxt, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Nuxt example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Nuxt template, or view a live example.](/templates/nuxt/nuxtjs-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fnuxtjs&template=nuxtjs)[Live Example](https://nuxtjs-template.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Nuxt project.

### [Choosing a build command](#choosing-a-build-command)

The following table outlines the differences between `nuxt build` and `nuxt generate` on Vercel:

| Feature | `nuxt build` | `nuxt generate` |
| --- | --- | --- |
| Default build command | Yes | No |
| Supports all Vercel features out of the box | Yes | Yes |
| [Supports SSR](#server-side-rendering-ssr) | Yes | No |
| [Supports SSG](#static-rendering) | Yes, [with nuxt config](#static-rendering) | Yes |
| [Supports ISR](#incremental-static-regeneration-isr) | Yes | No |

In general, `nuxt build` is likely best for most use cases. Consider using `nuxt generate` to build [fully static sites](#static-rendering).

## [Editing your Nuxt config](#editing-your-nuxt-config)

You can configure your Nuxt deployment by creating a Nuxt config file in your project's root directory. It can be a TypeScript, JavaScript, or MJS file, but [the Nuxt team recommends using TypeScript](https://nuxt.com/docs/getting-started/configuration#nuxt-configuration). Using TypeScript will allow your editor to suggest the correct names for configuration options, which can help mitigate typos.

Your Nuxt config file should default export `defineNuxtConfig` by default, which you can add an options object to.

The following is an example of a Nuxt config file with no options defined:

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  // Config options here
});
```

[See the Nuxt Configuration Reference docs for a list of available options](https://nuxt.com/docs/api/configuration/nuxt-config/#nuxt-configuration-reference).

### [Using `routeRules`](#using-routerules)

With the `routeRules` config option, you can:

*   Create redirects
*   Modify a route's response headers
*   Enable ISR
*   Deploy specific routes statically
*   Deploy specific routes with SSR
*   and more

At the moment, there is no way to configure route deployment options within your page components, but development of this feature is in progress.

The following is an example of a Nuxt config that:

*   Creates a redirect
*   Modifies a route's response headers
*   Opts a set of routes into client-side rendering

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  routeRules: {
    '/examples/*': { redirect: '/redirect-route' },
    '/modify-headers-route': { headers: { 'x-magic-of': 'nuxt and vercel' } },
    // Enables client-side rendering
    '/spa': { ssr: false },
  },
});
```

To learn more about `routeRules`:

*   [Read Nuxt's reference docs to learn more about the available route options](https://nuxt.com/docs/guide/concepts/rendering#route-rules)
*   [Read the Nitro Engine's Cache API docs to learn about cacheing individual routes](https://nitro.unjs.io/guide/cache)

## [Vercel Functions](#vercel-functions)

[Vercel Functions](/docs/functions) enable developers to write functions that uses resources that scale up and down based on traffic demands. This prevents them from failing during peak hours, but keeps them from running up high costs during periods of low activity.

Nuxt deploys routes defined in `/server/api`, `/server/routes`, and `/server/middleware` as one server-rendered Function by default. Nuxt Pages, APIs, and Middleware routes get bundled into a single Vercel Function.

The following is an example of a basic API Route in Nuxt:

server/api/hello.ts

TypeScript

TypeScriptJavaScript

```
export default defineEventHandler(() => 'Hello World!');
```

You can test your API Routes with `nuxt dev`.

## [Reading and writing files](#reading-and-writing-files)

You can read and write server files with Nuxt on Vercel. One way to do this is by using Nitro with Vercel Functions and the [Vercel KV driver](https://unstorage.unjs.io/drivers/vercel). Use Nitro's [server assets](https://nitro.unjs.io/guide/assets#server-assets) to include files in your project deployment. Assets within `server/assets` get included by default.

To access server assets, you can use Nitro's [storage API](https://nitro.unjs.io/guide/storage):

server/api/storage.ts

TypeScript

TypeScriptJavaScript

```
export default defineEventHandler(async () => {
  // https://nitro.unjs.io/guide/assets#server-assets
  const assets = useStorage('assets:server');
  const users = await assets.getItem('users.json');
  return {
    users,
  };
});
```

To write files, mount [KV storage](https://nitro.unjs.io/guide/storage) with the [Vercel KV driver](https://unstorage.unjs.io/drivers/vercel):

Update your `nuxt.config.ts` file.

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  $production: {
    nitro: {
      storage: {
        data: { driver: 'vercelKV' },
      },
    },
  },
});
```

Use with the storage API.

server/api/storage.ts

TypeScript

TypeScriptJavaScript

```
export default defineEventHandler(async (event) => {
  const dataStorage = useStorage('data');
  await dataStorage.setItem('hello', 'world');
  return {
    hello: await dataStorage.getItem('hello'),
  };
});
```

[See an example code repository](https://github.com/pi0/nuxt-server-assets/tree/main).

## [Middleware](#middleware)

Middleware is code that executes before a request gets processed. Because Middleware runs before the cache, it's an effective way of providing personalization to statically generated content.

Nuxt has two forms of Middleware:

*   [Server middleware](#nuxt-server-middleware-on-vercel)
*   [Route middleware](#nuxt-route-middleware-on-vercel)

### [Nuxt server middleware on Vercel](#nuxt-server-middleware-on-vercel)

In Nuxt, modules defined in `/server/middleware` will get deployed as [server middleware](https://nuxt.com/docs/guide/directory-structure/server#server-middleware). Server middleware should not have a return statement or send a response to the request.

Server middleware is best used to read data from or add data to a request's `context`. Doing so allows you to handle authentication or check a request's params, headers, url, [and more](https://www.w3schools.com/nodejs/obj_http_incomingmessage.asp).

The following example demonstrates Middleware that:

*   Checks for a cookie
*   Tries to fetch user data from a database based on the request
*   Adds the user's data and the cookie data to the request's context

server/middleware/auth.ts

TypeScript

TypeScriptJavaScript

```
import { getUserFromDBbyCookie } from 'some-orm-package';
 
export default defineEventHandler(async (event) => {
  // The getCookie method is available to all
  // Nuxt routes by default. No need to import.
  const token = getCookie(event, 'session_token');
 
  // getUserFromDBbyCookie is a placeholder
  // made up for this example. You can fetch
  // data from wherever you want here
  const { user } = await getUserFromDBbyCookie(event.request);
 
  if (user) {
    event.context.user = user;
    event.context.session_token = token;
  }
});
```

You could then access that data in a page on the frontend with the [`useRequestEvent`](https://nuxt.com/docs/api/composables/use-request-event) hook. This hook is only available in routes deployed with SSR. If your page renders in the browser, `useRequestEvent` will return `undefined`.

The following example demonstrates a page fetching data with `useRequestEvent`:

example.vue

TypeScript

TypeScriptJavaScript

```
<script>
  const event = useRequestEvent();
  const user = ref(event.context?.user);
</script>
 
<template>
    <div v-if="user">
      <h1>Hello, {{ user.name }}!</h1>
    </div>
    <div v-else>
      <p>Authentication failed!</p>
    </div>
</template>
```

### [Nuxt route middleware on Vercel](#nuxt-route-middleware-on-vercel)

Nuxt's route middleware runs before navigating to a particular route. While server middleware runs in Nuxt's [Nitro engine](https://nitro.unjs.io/), route middleware runs in Vue.

Route middleware is best used when you want to do things that server middleware can't, such as redirecting users, or preventing them from navigating to a route.

The following example demonstrates route middleware that redirects users to a secret route:

middleware/redirect.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtRouteMiddleware((to) => {
  console.log(
    `Heading to ${to.path} - but I think we should go somewhere else...`,
  );
 
  return navigateTo('/secret');
});
```

By default, route middleware code will only run on pages that specify them. To do so, within the `<script>` tag for a page, you must call the `definePageMeta` method, passing an object with `middleware: 'middleware-filename'` set as an option.

The following example demonstrates a page that runs the above redirect middleware:

redirect.vue

TypeScript

TypeScriptJavaScript

```
<script>
definePageMeta({
  middleware: 'redirect'
})
</script>
 
<template>
  <div>
    You should never see this page
  </div>
</template>
```

To make a middleware global, add the `.global` suffix before the file extension. The following is an example of a basic global middleware file:

example-middleware.global.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtRouteMiddleware(() => {
  console.log('running global middleware');
});
```

[See a detailed example of route middleware in Nuxt's Middleware example docs](https://nuxt.com/docs/examples/routing/middleware).

Middleware with Nuxt on Vercel enables you to:

*   Redirect users, and prevent navigation to routes
*   Run authentication checks on the server, and pass results to the frontend
*   Scope middleware to specific routes, or run it on all routes

[Learn more about Middleware](https://nuxt.com/docs/guide/directory-structure/middleware)

## [Server-Side Rendering (SSR)](#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

Nuxt allows you to deploy your projects with a strategy called [Universal Rendering](https://nuxt.com/docs/guide/concepts/rendering#universal-rendering). In concrete terms, this allows you to deploy your routes with SSR by default and opt specific routes out [in your Nuxt config](#editing-your-nuxt-config).

When you deploy your app with Universal Rendering, it renders on the server once, then your client-side JavaScript code gets interpreted in the browser again once the page loads.

On Vercel, Nuxt apps are server-rendered by default

SSR with Nuxt on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Allows you to opt individual routes out of SSR [with your Nuxt config](https://nuxt.com/docs/getting-started/deployment#client-side-only-rendering)

[Learn more about SSR](https://nuxt.com/docs/guide/concepts/rendering#universal-rendering)

## [Client-side rendering](#client-side-rendering)

If you deploy with `nuxt build`, you can opt nuxt routes into client-side rendering using `routeRules` by setting `ssr: false` as demonstrated below:

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  routeRules: {
    // Use client-side rendering for this route
    '/client-side-route-example': { ssr: false },
  },
});
```

## [Static rendering](#static-rendering)

To deploy a fully static site on Vercel, build your project with `nuxt generate`.

Alternatively, you can statically generate some Nuxt routes at build time using the `prerender` route rule in your `nuxt.config.ts`:

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  routeRules: {
    // prerender index route by default
    '/': { prerender: true },
    // prerender this route and all child routes
    '/prerender-multiple/**': { prerender: true },
  },
});
```

To verify that a route is prerendered at build time, check `useNuxtApp().payload.prerenderedAt`.

## [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)

[Incremental Static Regeneration (ISR)](/docs/incremental-static-regeneration) allows you to create or update content _without_ redeploying your site. ISR has two main benefits for developers: better performance and faster build times.

To enable ISR in a Nuxt route, add a `routeRules` option to your `nuxt.config.ts`, as shown in the example below:

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  routeRules: {
    // all routes (by default) will be revalidated every 60 seconds, in the background
    '/**': { isr: 60 },
    // this page will be generated on demand and then cached permanently
    '/static': { isr: true },
    // this page is statically generated at build time and cached permanently
    '/prerendered': { prerender: true },
    // this page will be always fresh
    '/dynamic': { isr: false },
  },
});
```

You should use the `isr` option rather than `swr` to enable ISR in a route. The `isr` option enables Nuxt to use Vercel's Cache.

using ISR with Nuxt on Vercel offers:

*   Better performance with our global [CDN](/docs/cdn)
*   Zero-downtime rollouts to previously statically generated pages
*   Global content updates in 300ms
*   Generated pages are both cached and persisted to durable storage

[Learn more about ISR with Nuxt](https://nuxt.com/docs/guide/concepts/rendering#hybrid-rendering).

## [Redirects and Headers](#redirects-and-headers)

You can define redirects and response headers with Nuxt on Vercel in your `nuxt.config.ts`:

nuxt.config.ts

TypeScript

TypeScriptJavaScript

```
export default defineNuxtConfig({
  routeRules: {
    '/examples/*': { redirect: '/redirect-route' },
    '/modify-headers-route': { headers: { 'x-magic-of': 'nuxt and vercel' } },
  },
});
```

## [Image Optimization](#image-optimization)

[Image Optimization](/docs/image-optimization) helps you achieve faster page loads by reducing the size of images and using modern image formats.

When deploying to Vercel, images are automatically optimized on demand, keeping your build times fast while improving your page load performance and [Core Web Vitals](/docs/speed-insights).

To use Image Optimization with Nuxt on Vercel, follow [the Image Optimization quickstart](/docs/image-optimization/quickstart) by selecting Nuxt from the dropdown.

Using Image Optimization with Nuxt on Vercel:

*   Requires zero-configuration for Image Optimization when using `@nuxt/image`
*   Helps your team ensure great performance by default
*   Keeps your builds fast by optimizing images on-demand

[Learn more about Image Optimization](/docs/image-optimization)

## [Open Graph Images](#open-graph-images)

Dynamic social card images allow you to create a unique image for pages of your site. This is great for sharing links on the web through social platforms or text messages.

To generate dynamic social card images for Nuxt projects, you can use [`nuxt-og-image`](https://nuxtseo.com/og-image/getting-started/installation). It uses the main Nuxt/Nitro [Server-side rendering(SSR)](#server-side-rendering-ssr) function.

The following example demonstrates using Open Graph (OG) image generation with [`nuxt-og-image`](https://nuxtseo.com/og-image/getting-started/installation):

1.  Create a new OG template

components/OgImage/Template.vue

TypeScript

TypeScriptJavaScript

```
<script setup lang="ts">
  withDefaults(defineProps<{
    title?: string
  }>(), {
    title: 'title',
  })
</script>
<template>
  <div class="h-full w-full flex items-start justify-start border border-blue-500 border-12 bg-gray-50">
    <div class="flex items-start justify-start h-full">
      <div class="flex flex-col justify-between w-full h-full">
        <h1 class="text-[80px] p-20 font-black text-left">
          {{ title }}
        </h1>
        <p class="text-2xl pb-10 px-20 font-bold mb-0">
          acme.com
        </p>
      </div>
    </div>
  </div>
</template>
```

1.  Use that OG image in your pages. Props passed get used in your open graph images.

pages/index.vue

TypeScript

TypeScriptJavaScript

```
<script lang="ts" setup>
defineOgImageComponent('Template', {
  title: 'Is this thing on?'
})
</script>
```

To see your generated image, run your project and use Nuxt DevTools. Or you can visit the image at its URL `/__og-image__/image/og.png`.

[Learn more about OG Image Generation with Nuxt](https://nuxtseo.com/og-image/getting-started/installation).

## [Deploying legacy Nuxt projects on Vercel](#deploying-legacy-nuxt-projects-on-vercel)

The Nuxt team [does not recommend deploying legacy versions of Nuxt (such as Nuxt 2) on Vercel](https://github.com/nuxt/vercel-builder#readme), except as static sites. If your project uses a legacy version of Nuxt, you should either:

*   Implement [Nuxt Bridge](https://github.com/nuxt/bridge#readme)
*   Or [upgrade with the Nuxt team's migration guide](https://nuxt.com/docs/migration/overview)

If you still want to use legacy Nuxt versions with Vercel, you should only do so by building a static site with `nuxt generate`. We do not recommend deploying legacy Nuxt projects with server-side rendering.

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying Nuxt projects on Vercel with the following resources:

*   [Deploy our Nuxt Alpine template](/templates/nuxt/alpine)
*   [See an example of Nuxt Image](/docs/image-optimization/quickstart)

--------------------------------------------------------------------------------
title: "Remix on Vercel"
description: "Learn how to use Vercel's features with Remix."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack/remix"
--------------------------------------------------------------------------------

# Remix on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

Remix is a fullstack, [server-rendered](#server-side-rendering-ssr) React framework. Its built-in features for nested pages, error boundaries, transitions between loading states, and more, enable developers to create modern web apps.

With Vercel, you can deploy server-rendered Remix and Remix V2 applications to Vercel with zero configuration. When using the [Remix Vite plugin](https://remix.run/docs/en/main/future/vite), static site generation using [SPA mode](https://remix.run/docs/en/main/future/spa-mode) is also supported.

It is highly recommended that your application uses the Remix Vite plugin, in conjunction with the [Vercel Preset](#vercel-vite-preset), when deploying to Vercel.

## [Getting started](#getting-started)

To get started with Remix on Vercel:

*   If you already have a project with Remix, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our Remix example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our Remix template, or view a live example.](/templates/remix/remix-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fremix&template=remix)[Live Example](https://remix-run-template.vercel.app)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your Remix project.

## [`@vercel/remix`](#@vercel/remix)

The [`@vercel/remix`](https://www.npmjs.com/package/@vercel/remix) package exposes useful types and utilities for Remix apps deployed on Vercel, such as:

*   [`json`](https://remix.run/docs/en/main/utils/json)
*   [`defer`](https://remix.run/docs/en/main/utils/defer)
*   [`createCookie`](https://remix.run/docs/en/main/utils/cookies#createcookie)

To best experience Vercel features such as [streaming](#response-streaming), [Vercel Functions](#vercel-functions), and more, we recommend importing utilities from `@vercel/remix` rather than from standard Remix packages such as `@remix-run/node`.

`@vercel/remix` should be used anywhere in your code that you normally would import utility functions from the following packages:

*   [`@remix-run/node`](https://www.npmjs.com/package/@remix-run/node)
*   [`@remix-run/cloudflare`](https://www.npmjs.com/package/@remix-run/cloudflare)
*   [`@remix-run/server-runtime`](https://www.npmjs.com/package/@remix-run/server-runtime)

To get started, navigate to the root directory of your Remix project with your terminal and install `@vercel/remix` with your preferred package manager:

pnpmyarnnpmbun

```
pnpm i @vercel/remix
```

## [Vercel Vite Preset](#vercel-vite-preset)

When using the [Remix Vite plugin](https://remix.run/docs/en/main/future/vite) (highly recommended), you should configure the Vercel Preset to enable the full feature set that Vercel offers.

To configure the Preset, add the following lines to your `vite.config` file:

/vite.config.ts

```
import { vitePlugin as remix } from '@remix-run/dev';
import { installGlobals } from '@remix-run/node';
import { defineConfig } from 'vite';
import tsconfigPaths from 'vite-tsconfig-paths';
import { vercelPreset } from '@vercel/remix/vite';
 
installGlobals();
 
export default defineConfig({
  plugins: [
    remix({
      presets: [vercelPreset()],
    }),
    tsconfigPaths(),
  ],
});
```

Using this Preset enables Vercel-specific functionality such as rendering your Remix application with Vercel Functions.

## [Server-Side Rendering (SSR)](#server-side-rendering-ssr)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.

Remix routes defined in `app/routes` are deployed with server-side rendering by default.

The following example demonstrates a basic route that renders with SSR:

/app/routes/\_index.tsx

TypeScript

TypeScriptJavaScript

```
export default function IndexRoute() {
  return (
    <div style={{ fontFamily: 'system-ui, sans-serif', lineHeight: '1.4' }}>
      <h1>This route is rendered on the server</h1>
    </div>
  );
}
```

### [Vercel Functions](#vercel-functions)

Vercel Functions execute using Node.js. They enable developers to write functions that use resources that scale up and down based on traffic demands. This prevents them from failing during peak hours, but keeps them from running up high costs during periods of low activity.

Remix API routes in `app/routes` are deployed as Vercel Functions by default.

The following example demonstrates a basic route that renders a page with the heading, "Welcome to Remix with Vercel":

/app/routes/serverless-example.tsx

TypeScript

TypeScriptJavaScript

```
export default function Serverless() {
  return <h1>Welcome to Remix with Vercel</h1>;
}
```

To summarize, Server-Side Rendering (SSR) with Remix on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has framework-aware infrastructure to generate Vercel Functions

## [Response streaming](#response-streaming)

[Streaming HTTP responses](/docs/functions/streaming-functions)

with Remix on Vercel is supported with Vercel Functions. See the [Streaming](https://remix.run/docs/en/main/guides/streaming) page in the Remix docs for general instructions.

The following example demonstrates a route that simulates a throttled network by delaying a promise's result, and renders a loading state until the promise is resolved:

/app/routes/defer-route.tsx

TypeScript

TypeScriptJavaScript

```
import { Suspense } from 'react';
import { Await, useLoaderData } from '@remix-run/react';
import { defer } from '@vercel/remix';
 
function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
 
export async function loader({ request }) {
  const version = process.versions.node;
 
  return defer({
    // Don't let the promise resolve for 1 second
    version: sleep(1000).then(() => version),
  });
}
 
export default function DeferredRoute() {
  const { version } = useLoaderData();
 
  return (
    <Suspense fallback={'Loading…'}>
      <Await resolve={version}>{(version) => <strong>{version}</strong>}</Await>
    </Suspense>
  );
}
```

To summarize, Streaming with Remix on Vercel:

*   Offers faster Function response times, improving your app's user experience
*   Allows you to return large amounts of data without exceeding Vercel Function response size limits
*   Allows you to display Instant Loading UI from the server with Remix's `defer()` and `Await`

[Learn more about Streaming](/docs/functions/streaming-functions)

## [`Cache-Control` headers](#cache-control-headers)

Vercel's [CDN](/docs/cdn) caches your content at the edge in order to serve data to your users as fast as possible. [Static caching](/docs/edge-cache#static-files-caching) works with zero configuration.

By adding a `Cache-Control` header to responses returned by your Remix routes, you can specify a set of caching rules for both client (browser) requests and server responses. A cache must obey the requirements defined in the Cache-Control header.

Remix supports header modifications with the [`headers`](https://remix.run/docs/en/main/route/headers) function, which you can export in your routes defined in `app/routes`.

The following example demonstrates a route that adds `Cache Control` headers which instruct the route to:

*   Return cached content for requests repeated within 1 second without revalidating the content
*   For requests repeated after 1 second, but before 60 seconds have passed, return the cached content and mark it as stale. The stale content will be revalidated in the background with a fresh value from your [`loader`](https://remix.run/docs/en/1.14.0/route/loader) function

/app/routes/example.tsx

TypeScript

TypeScriptJavaScript

```
import type { HeadersFunction } from '@vercel/remix';
 
export const headers: HeadersFunction = () => ({
  'Cache-Control': 's-maxage=1, stale-while-revalidate=59',
});
 
export async function loader() {
  // Fetch data necessary to render content
}
```

See [our docs on cache limits](/docs/edge-cache#limits) to learn the max size and lifetime of caches stored on Vercel.

To summarize, using `Cache-Control` headers with Remix on Vercel:

*   Allow you to cache responses for server-rendered Remix apps using Vercel Functions
*   Allow you to serve content from the cache _while updating the cache in the background_ with `stale-while-revalidate`

[Learn more about caching](/docs/edge-cache#how-to-cache-responses)

## [Analytics](#analytics)

Vercel's Analytics features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your Remix project:

pnpmyarnnpmbun

```
pnpm i @vercel/analytics
```

Then, follow the instructions below to add the `Analytics` component to your app. The `Analytics` component is a wrapper around Vercel's tracking script, offering a seamless integration with Remix.

Add the following component to your `root` file:

app/root.tsx

TypeScript

TypeScriptJavaScript

```
import { Analytics } from '@vercel/analytics/react';
 
export default function App() {
  return (
    <html lang="en">
      <body>
        <Analytics />
      </body>
    </html>
  );
}
```

To summarize, Analytics with Remix on Vercel:

*   Enables you to track traffic and see your top-performing pages
*   Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation and more

[Learn more about Analytics](/docs/analytics)

## [Using a custom `app/entry.server` file](#using-a-custom-app/entry.server-file)

By default, Vercel supplies an implementation of the `entry.server` file which is configured for streaming to work with Vercel Functions. This version will be used when no `entry.server` file is found in the project, or when the existing `entry.server` file has not been modified from the base Remix template.

However, if your application requires a customized `app/entry.server.jsx` or `app/entry.server.tsx` file (for example, to wrap the `<RemixServer>` component with a React context), you should base it off of this template:

/app/entry.server.tsx

TypeScript

TypeScriptJavaScript

```
import { RemixServer } from '@remix-run/react';
import { handleRequest, type EntryContext } from '@vercel/remix';
 
export default async function (
  request: Request,
  responseStatusCode: number,
  responseHeaders: Headers,
  remixContext: EntryContext,
) {
  let remixServer = <RemixServer context={remixContext} url={request.url} />;
  return handleRequest(
    request,
    responseStatusCode,
    responseHeaders,
    remixServer,
  );
}
```

## [Using a custom `server` file](#using-a-custom-server-file)

Defining a custom `server` file is not supported when using the Remix Vite plugin on Vercel.

It's usually not necessary to define a custom server.js file within your Remix application when deploying to Vercel. In general, we do not recommend it.

If your project requires a custom [`server`](https://remix.run/docs/en/main/file-conventions/remix-config#md-server) file, you will need to [install `@vercel/remix`](#@vercel/remix) and import `createRequestHandler` from `@vercel/remix/server`. The following example demonstrates a basic `server.js` file:

server.ts

TypeScript

TypeScriptJavaScript

```
import { createRequestHandler } from '@vercel/remix/server';
import * as build from '@remix-run/dev/server-build';
 
export default createRequestHandler({
  build,
  mode: process.env.NODE_ENV,
  getLoadContext() {
    return {
      nodeLoadContext: true,
    };
  },
});
```

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying Remix projects on Vercel with the following resources:

*   [Explore Remix in a monorepo](/templates/remix/turborepo-kitchensink)
*   [Deploy our Product Roadmap template](/templates/remix/roadmap-voting-app-rowy)
*   [Explore the Remix docs](https://remix.run/docs/en/main)

--------------------------------------------------------------------------------
title: "SvelteKit on Vercel"
description: "Learn how to use Vercel's features with SvelteKit"
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack/sveltekit"
--------------------------------------------------------------------------------

# SvelteKit on Vercel

Copy page

Ask AI about this page

Last updated September 24, 2025

SvelteKit is a frontend framework that enables you to build Svelte applications with modern techniques, such as Server-Side Rendering, automatic code splitting, and advanced routing.

You can deploy your SvelteKit projects to Vercel with zero configuration, enabling you to use [Preview Deployments](/docs/deployments/environments#preview-environment-pre-production), [Web Analytics](#web-analytics), [Vercel functions](/docs/functions), and more.

## [Get started with SvelteKit on Vercel](#get-started-with-sveltekit-on-vercel)

To get started with SvelteKit on Vercel:

*   If you already have a project with SvelteKit, install [Vercel CLI](/docs/cli) and run the `vercel` command from your project's root directory
*   Clone one of our SvelteKit example repos to your favorite git provider and deploy it on Vercel with the button below:

[Deploy our SvelteKit template, or view a live example.](/templates/svelte/sveltekit-boilerplate)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Fsveltekit-1&template=sveltekit-1)[Live Example](https://sveltekit-template.vercel.app/)

*   Or, choose a template from Vercel's marketplace:

Vercel deployments can [integrate with your git provider](/docs/git) to [generate preview URLs](/docs/deployments/environments#preview-environment-pre-production) for each pull request you make to your SvelteKit project.

## [Use Vercel features with Svelte](#use-vercel-features-with-svelte)

When you create a new SvelteKit project with `npm create svelte@latest`, it installs `adapter-auto` by default. This adapter detects that you're deploying on Vercel and installs the `@sveltejs/adapter-vercel` plugin for you at build time.

We recommend installing the `@sveltejs/adapter-vercel` package yourself. Doing so will ensure version stability, slightly speed up your CI process, and [allows you to configure default deployment options for all routes in your project](#configure-your-sveltekit-deployment).

The following instructions will guide you through adding the Vercel adapter to your SvelteKit project.

1.  ### [Install SvelteKit's Vercel adapter plugin](#install-sveltekit's-vercel-adapter-plugin)
    
    You can add [the Vercel adapter](https://kit.svelte.dev/docs/adapter-vercel) to your SvelteKit project by running the following command:
    
    pnpmyarnnpmbun
    
    ```
    pnpm i @sveltejs/adapter-vercel
    ```
    
2.  ### [Add the Vercel adapter to your Svelte config](#add-the-vercel-adapter-to-your-svelte-config)
    
    Add the Vercel adapter to your `svelte.config.js` file, [which should be at the root of your project directory](https://kit.svelte.dev/docs/configuration).
    
    You cannot use [TypeScript for your SvelteKit config file](https://github.com/sveltejs/kit/issues/2576).
    
    In your `svelte.config.js` file, import `adapter` from `@sveltejs/adapter-vercel`, and add your preferred options. The following example shows the default configuration, which uses the Node.js runtime (which run on Vercel functions).
    
    svelte.config.js
    
    ```
    import adapter from '@sveltejs/adapter-vercel';
     
    export default {
      kit: {
        adapter: adapter(),
      },
    };
    ```
    
    [Learn more about configuring your Vercel deployment in our configuration section below](#configure-your-sveltekit-deployment).
    

## [Configure your SvelteKit deployment](#configure-your-sveltekit-deployment)

You can configure how your SvelteKit project gets deployed to Vercel at the project-level and at the route-level.

Changes to the `config` object you define in `svelte.config.js` will affect the default settings for routes across your whole project. To override this, you can export a `config` object in any route file.

The following is an example of a `svelte.config.js` file that will deploy using server-side rendering in Vercel's Node.js serverless runtime:

svelte.config.js

```
import adapter from '@sveltejs/adapter-vercel';
 
/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter({
      runtime: 'nodejs20.x',
    }),
  },
};
 
export default config;
```

You can also configure how individual routes deploy by exporting a `config` object. The following is an example of a route that will deploy on Vercel's Edge runtime:

+page.server.ts

TypeScript

TypeScriptJavaScript

```
import { PageServerLoad } from './$types';
 
export const config = {
  runtime: 'edge',
};
 
export const load = ({ cookies }): PageServerLoad<any> => {
  // Load function code here
};
```

[Learn about all the config options available in the SvelteKit docs](https://kit.svelte.dev/docs/adapter-vercel#deployment-configuration). You can also see the type definitions for config object properties in [the SvelteKit source code](https://github.com/sveltejs/kit/blob/master/packages/adapter-vercel/index.d.ts#L38).

### [Configuration options](#configuration-options)

SvelteKit's docs have [a comprehensive list of all config options available to you](https://kit.svelte.dev/docs/adapter-vercel#deployment-configuration). This section will cover a select few options which may be easier to use with more context.

#### [`split`](#split)

By default, your SvelteKit routes get bundled into one Function when you deploy your project to Vercel. This configuration typically reduces how often your users encounter [cold starts](/docs/infrastructure/compute#cold-and-hot-boots).

In most cases, there is no need to modify this option.

Setting `split: true` in your Svelte config will cause your SvelteKit project's routes to get split into separate Vercel Functions.

Splitting your Functions is not typically better than bundling them. You may want to consider setting `split: true` if you're experiencing either of the following issues:

*   You have exceeded the Function size limit for the runtime you're using. Batching too many routes into a single Function could cause you to exceed Function size limits for your Vercel account. See our [Function size limits](/docs/functions/limitations#bundle-size-limits) to learn more.
*   Your app is experiencing abnormally long cold start times. Batching Vercel functions into one Function will reduce how often users experience cold starts. It can also increase the latency they experience when a cold start is required, since larger functions tend to require more resources. This can result in slower responses to user requests that occur after your Function spins down.

#### [`regions`](#regions)

Choosing a region allows you to reduce latency for requests to functions. If you choose a Function region geographically near dependencies, or nearest to your visitor, you can reduce your Functions' latency.

By default, your Vercel Functions will be deployed in _Washington, D.C., USA_, or `iad1`. Adding a region ID to the `regions` array will deploy your Vercel functions there. [See our Vercel Function regions docs to learn how to override this settings](/docs/functions/regions#select-a-default-serverless-region).

## [Streaming](#streaming)

Vercel supports streaming API responses over time with SvelteKit, allowing you to render parts of the UI early, then render the rest as data becomes available. Doing so lets users interact with your app before the full page loads, improving their perception of your app's speed. Here's how it works:

*   SvelteKit enables you to use a `+page.server.ts` file to fetch data on the server, which you can access from a `+page.svelte` file located in the same folder
*   You fetch data in a [`load`](https://kit.svelte.dev/docs/load) function defined in `+page.server.ts`. This function returns an object
    *   Top-level properties that return a promise will resolve before the page renders
    *   Nested properties that return a promise [will stream](https://kit.svelte.dev/docs/load#streaming-with-promises)

The following example demonstrates a `load` function that will stream its response to the client. To simulate delayed data returned from a promise, it uses a `sleep` method.

src/routes/streaming-example/+page.server.ts

TypeScript

TypeScriptJavaScript

```
function sleep(value: any, ms: number) {
  // Use this sleep function to simulate
  // a delayed API response.
  return new Promise((fulfill) => {
    setTimeout(() => {
      fulfill(value);
    }, ms);
  });
}
export function load(event): PageServerLoad<any> {
  // Get some location data about the visitor
  const ip = event.getClientAddress();
  const city = decodeURIComponent(
    event.request.headers.get('x-vercel-ip-city') ?? 'unknown',
  );
  return {
    topLevelExample: sleep({ data: "This won't be streamed" }, 2000)
    // Stream the location data to the client
    locationData: {
      details: sleep({ ip, city }, 1000),
    },
  };
}
```

You could then display this data by creating the following `+page.svelte` file in the same directory:

src/routes/streaming-example/+page.svelte

TypeScript

TypeScriptJavaScript

```
<script lang="ts">
  import type { PageData } from './$types'
  export let data: PageData;
</script>
 
<h1><span>Hello!</span></h1>
 
<div class="info">
  {#await data.locationData.details}
    <p>streaming delayed data from the server...</p>
  {:then details}
    <div>
      <p>City is {details.city}</p>
      <p>And IP is: {details.ip} </p>
    </div>
  {/await}
</div>
```

To summarize, Streaming with SvelteKit on Vercel:

*   Enables you to stream UI elements as data loads
*   Supports streaming through Vercel Functions
*   Improves perceived speed of your app

[Learn more about Streaming on Vercel](/docs/functions/streaming-functions).

## [Server-Side Rendering](#server-side-rendering)

Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, verifying authentication or checking the geolocation of an incoming request.

Vercel offers SSR that scales down resource consumption when traffic is low, and scales up with traffic surges. This protects your site from accruing costs during periods of no traffic or losing business during high-traffic periods.

SvelteKit projects are server-side rendered by default. You can configure individual routes to prerender with the `prerender` page option, or use the same option in your app's root `+layout.js` or `+layout.server.js` file to make all your routes prerendered by default.

While server-side rendered SvelteKit apps do support middleware, SvelteKit does not support URL rewrites from middleware.

[See the SvelteKit docs on prerendering to learn more](https://kit.svelte.dev/docs/page-options#prerender).

To summarize, SSR with SvelteKit on Vercel:

*   Scales to zero when not in use
*   Scales automatically with traffic increases
*   Has zero-configuration support for [`Cache-Control` headers](/docs/edge-cache), including `stale-while-revalidate`

[Learn more about SSR](https://kit.svelte.dev/docs/page-options#ssr)

## [Environment variables](#environment-variables)

Vercel provides a set of System Environment Variables that our platform automatically populates. For example, the `VERCEL_GIT_PROVIDER` variable exposes the Git provider that triggered your project's deployment on Vercel.

These environment variables will be available to your project automatically, and you can enable or disable them in your project settings on Vercel. [See our Environment Variables docs to learn how](/docs/environment-variables/system-environment-variables).

### [Use Vercel environment variables with SvelteKit](#use-vercel-environment-variables-with-sveltekit)

SvelteKit allows you to import environment variables, but separates them into different modules based on whether they're dynamic or static, and whether they're private or public. For example, the `'$env/static/private'` module exposes environment variables that don't change, and that you should not share publicly.

[System Environment Variables](/docs/environment-variables/system-environment-variables) are private and you should never expose them to the frontend client. This means you can only import them from `'$env/static/private'` or `'$env/dynamic/private'`.

The example below exposes `VERCEL_COMMIT_REF`, a variable that exposes the name of the branch associated with your project's deployment, to [a `load` function](https://kit.svelte.dev/docs/load) for a Svelte layout:

+layout.server.ts

TypeScript

TypeScriptJavaScript

```
import { LayoutServerLoad } from './types';
import { VERCEL_COMMIT_REF } from '$env/static/private';
 
type DeploymentInfo = {
  deploymentGitBranch: string;
};
 
export function load(): LayoutServerLoad<DeploymentInfo> {
  return {
    deploymentGitBranch: 'Test',
  };
}
```

You could reference that variable in [a corresponding layout](https://kit.svelte.dev/docs/load#layout-data) as shown below:

+layout.svelte

```
<script>
  /** @type {import('./$types').LayoutData} */
  export let data;
</script>
 
<p>This staging environment was deployed from {data.deploymentGitBranch}.</p>
```

To summarize, the benefits of using Environment Variables with SvelteKit on Vercel include:

*   Access to vercel deployment information, dynamically or statically, with our preconfigured System Environment Variables
*   Access to automatically-configured environment variables provided by [integrations for your preferred services](/docs/environment-variables#integration-environment-variables)
*   Searching and filtering environment variables by name and environment in Vercel's dashboard

[Learn more about Environment Variables](/docs/environment-variables)

## [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)

Incremental Static Regeneration allows you to create or update content without redeploying your site. When you deploy a route with ISR, Vercel caches the page to serve it to visitors statically, and rebuilds it on a time interval of your choice. ISR has three main benefits for developers: better performance, improved security, and faster build times.

[See our ISR docs to learn more](/docs/incremental-static-regeneration).

To deploy a SvelteKit route with ISR:

*   Export a `config` object with an `isr` property. Its value will be the number of seconds to wait before revalidating
*   To enable on-demand revalidation, add the `bypassToken` property to the `config` object. Its value gets checked when `GET` or `HEAD` requests get sent to the route. If the request has a `x-prerender-revalidate` header with the same value as `bypassToken`, the cache will be revalidated immediately

The following example demonstrates a SvelteKit route that Vercel will deploy with ISR, revalidating the page every 60 seconds, with on-demand revalidation enabled:

example-route/+page.server.ts

TypeScript

TypeScriptJavaScript

```
export const config = {
  isr: {
    expiration: 60,
    bypassToken: 'REPLACE_ME_WITH_SECRET_VALUE',
  },
};
```

[Learn more about ISR with SvelteKit](https://kit.svelte.dev/docs/adapter-vercel#incremental-static-regeneration).

To summarize, the benefits of using ISR with SvelteKit on Vercel include:

*   Better performance with our global [CDN](/docs/cdn)
*   Zero-downtime rollouts to previously statically generated pages
*   Framework-aware infrastructure enables global content updates in 300ms
*   Generated pages are both cached and persisted to durable storage

[Learn more about ISR](/docs/incremental-static-regeneration)

## [Skew Protection](#skew-protection)

New project deployments can lead to version skew. This can happen when your users are using your app and a new version gets deployed. Their deployment version requests assets from an older version. And those assets from the previous version got replaced. This can cause errors when those active users navigate or interact with your project.

SvelteKit has a skew protection solution. When it detects version skew, it triggers a hard reload of a page to sync to the latest version. This does mean the client-side state gets lost. With Vercel skew protection, client requests get routed to their original deployment. No client-side state gets lost. To enable it, visit the Advanced section of your project settings on Vercel.

[Learn more about skew protection with SvelteKit](https://kit.svelte.dev/docs/adapter-vercel#skew-protection).

To summarize, the benefits of using ISR with SvelteKit on Vercel include:

*   Mitigates the risk of your active users encountering version skew
*   Avoids hard reloads for current active users on your project

[Learn more about skew protection on Vercel](/docs/skew-protection).

## [Image Optimization](#image-optimization)

[Image Optimization](/docs/image-optimization) helps you achieve faster page loads by reducing the size of images and using modern image formats.

When deploying to Vercel, you can optimize your images on demand, keeping your build times fast while improving your page load performance and [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained).

To use Image Optimization with SvelteKit on Vercel, use the [`@sveltejs/adapter-vercel`](#use-vercel-features-with-svelte) within your `svelte.config.ts` file.

svelte.config.ts

TypeScript

TypeScriptJavaScript

```
import adapter from '@sveltejs/adapter-vercel';
 
export default {
  kit: {
    adapter({
      images: {
        sizes: [640, 828, 1200, 1920, 3840],
        formats: ['image/avif', 'image/webp'],
        minimumCacheTTL: 300,
        domains: ['example-app.vercel.app'],
      }
    })
  }
};
```

This allows you to specify [configuration options](https://vercel.com/docs/build-output-api/v3/configuration#images) for Vercel's native image optimization API.

To use image optimization with SvelteKit, you have to construct your own `srcset` URLs. You can create a library function that will optimize `srcset` URLs in production for you like this:

src/lib/image.ts

TypeScript

TypeScriptJavaScript

```
import { dev } from '$app/environment';
 
export function optimize(src: string, widths = [640, 960, 1280], quality = 90) {
  if (dev) return src;
 
  return widths
    .slice()
    .sort((a, b) => a - b)
    .map((width, i) => {
      const url = `/_vercel/image?url=${encodeURIComponent(src)}&w=${width}&q=${quality}`;
      const descriptor = i < widths.length - 1 ? ` ${width}w` : '';
      return url + descriptor;
    })
    .join(', ');
}
```

Use an `img` or any other image component with an optimized `srcset` generated by the `optimize` function:

src/components/image.svelte

TypeScript

TypeScriptJavaScript

```
<script lang="ts">
  import { optimize } from '$lib/image';
  import type { Photo } from '$lib/types';
 
  export let photo: Photo;
</script>
 
<img
  class="absolute left-0 top-0 w-full h-full"
  srcset={optimize(photo.url)}
  alt={photo.description}
/>
```

To summarize, using Image Optimization with SvelteKit on Vercel:

*   Configure image optimization with `@sveltejs/adapter-vercel`
*   Optimize for production with a function that constructs optimized `srcset` for your images
*   Helps your team ensure great performance by default
*   Keeps your builds fast by optimizing images on-demand

[Learn more about Image Optimization](/docs/image-optimization)

## [Web Analytics](#web-analytics)

Vercel's Web Analytics features enable you to visualize and monitor your application's performance over time. The Analytics tab in your project's dashboard offers detailed insights into your website's visitors, with metrics like top pages, top referrers, and user demographics.

To use Web Analytics, navigate to the Analytics tab of your project dashboard on Vercel and select Enable in the modal that appears.

To track visitors and page views, we recommend first installing our `@vercel/analytics` package by running the terminal command below in the root directory of your SvelteKit project:

pnpmyarnnpmbun

```
pnpm i @vercel/analytics
```

In your SvelteKit project's main `+layout.svelte` file, add the following `<script>`:

With the above script added to your project, you'll be able to view detailed user insights in your dashboard on Vercel under the Analytics tab. [See our docs to learn more about the user metrics you can track with Vercel's Web Analytics](/docs/analytics).

Your project must be deployed on Vercel to take advantage of the Web Analytics feature. Work on making this feature more broadly available is in progress.

To summarize, using Web Analytics with SvelteKit on Vercel:

*   Enables you to track traffic and see your top-performing pages
*   Offers you detailed breakdowns of visitor demographics, including their OS, browser, geolocation, and more

[Learn more about Web Analytics](/docs/analytics)

## [Speed Insights](#speed-insights)

You can see data about your project's [Core Web Vitals](/docs/speed-insights/metrics#core-web-vitals-explained) performance in your dashboard on Vercel. Doing so will allow you to track your web application's loading speed, responsiveness, and visual stability so you can improve the user experience.

[See our Speed Insights docs to learn more](/docs/speed-insights).

To summarize, using Speed Insights with SvelteKit on Vercel:

*   Enables you to track traffic performance metrics, such as [First Contentful Paint](/docs/speed-insights/metrics#first-contentful-paint-fcp), or [First Input Delay](/docs/speed-insights/metrics#first-input-delay-fid)
*   Enables you to view performance metrics by page name and URL for more granular analysis
*   Shows you [a score for your app's performance](/docs/speed-insights/metrics#how-the-scores-are-determined) on each recorded metric, which you can use to track improvements or regressions

[Learn more about Speed Insights](/docs/speed-insights)

## [Draft Mode](#draft-mode)

[Draft Mode](/docs/draft-mode) enables you to view draft content from your [Headless CMS](/docs/solutions/cms) immediately, while still statically generating pages in production.

To use a SvelteKit route in Draft Mode, you must:

1.  Export a `config` object [that enables Incremental Static Regeneration](https://kit.svelte.dev/docs/adapter-vercel#incremental-static-regeneration) from the route's `+page.server` file:

blog/\[slug\]/+page.server.ts

TypeScript

TypeScriptJavaScript

```
import { BYPASS_TOKEN } from '$env/static/private';
 
export const config = {
  isr: {
    // Random token that can be provided to bypass the cached version of the page with a __prerender_bypass=<token> cookie. Allows rendering content at request time for this route.
    bypassToken: BYPASS_TOKEN,
 
    // Expiration time (in seconds) before the cached asset will be re-generated by invoking the Vercel Function.
    // Setting the value to `false` means it will never expire.
    expiration: 60,
  },
};
```

1.  Send a `__prerender_bypass` cookie with the same value as `bypassToken` in your config.

To render the draft content, SvelteKit will check for `__prerender_bypass`. If its value matches the value of `bypassToken`, it will render content fetched at request time rather than prebuilt content.

We recommend using a cryptographically secure random number generator at build time as your `bypassToken` value. If a malicious actor guesses your `bypassToken`, they can view your pages in Draft Mode.

### [Draft Mode security](#draft-mode-security)

Deployments on Vercel automatically secure Draft Mode behind the same authentication used for Preview Comments. In order to enable or disable Draft Mode, the viewer must be logged in as a member of the [Team](/docs/teams-and-accounts). Once enabled, Vercel's CDN will bypass the ISR cache automatically and invoke the underlying [Vercel Function](/docs/functions).

### [Enabling Draft Mode in Preview Deployments](#enabling-draft-mode-in-preview-deployments)

You and your team members can toggle Draft Mode in the Vercel Toolbar in [production](/docs/vercel-toolbar/in-production-and-localhost/add-to-production), [localhost](/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost), and [Preview Deployments](/docs/deployments/environments#preview-environment-pre-production#comments). When you do so, the toolbar will become purple to indicate Draft Mode is active.

![The Vercel toolbar when Draft Mode is enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-light.png&w=828&q=75)![The Vercel toolbar when Draft Mode is enabled.](/vc-ap-vercel-docs/_next/image?url=https%3A%2F%2F7nyt0uhk7sse4zvn.public.blob.vercel-storage.com%2Fdocs-assets%2Fstatic%2Fdocs%2Fworkflow-collaboration%2Fdraft-mode%2Fdraft-toolbar1-dark.png&w=828&q=75)

The Vercel toolbar when Draft Mode is enabled.

Users outside your Vercel team cannot toggle Draft Mode.

To summarize, the benefits of using Draft Mode with SvelteKit on Vercel include:

*   Easily server-render previews of static pages
*   Adds security measures to prevent malicious usage
*   Integrates with any headless provider of your choice
*   You can enable and disable Draft Mode in [the comments toolbar](/docs/comments/how-comments-work) on Preview Deployments

[Learn more about Draft Mode](/docs/draft-mode)

## [Routing Middleware](#routing-middleware)

Routing Middleware is useful for modifying responses before they're sent to a user. We recommend [using SvelteKit's server hooks](https://kit.svelte.dev/docs/hooks) to modify responses. Due to SvelteKit's client-side rendering, you cannot use Vercel's Routing Middleware with SvelteKit.

## [Rewrites](#rewrites)

Adding a [`vercel.json`](/docs/project-configuration) file to the root directory of your project enables you to rewrite your app's routes.

We do not recommend using `vercel.json` rewrites with SvelteKit.

Rewrites from `vercel.json` only apply to the Vercel proxy. At runtime, SvelteKit doesn't have access to the rewritten URL, which means it has no way of rendering the intended rewritten route.

## [More benefits](#more-benefits)

See [our Frameworks documentation page](/docs/frameworks) to learn about the benefits available to all frameworks when you deploy on Vercel.

## [More resources](#more-resources)

Learn more about deploying SvelteKit projects on Vercel with the following resources:

*   [Learn about the Build Output API](/docs/build-output-api/v3)
*   [SvelteKit's official docs](https://kit.svelte.dev/docs/adapter-vercel)

--------------------------------------------------------------------------------
title: "TanStack Start on Vercel"
description: "Learn how to use Vercel's features with TanStack Start."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/full-stack/tanstack-start"
--------------------------------------------------------------------------------

# TanStack Start on Vercel

Copy page

Ask AI about this page

Last updated October 31, 2025

TanStack Start is a fullstack framework powered by TanStack Router for React and Solid. It has support for full-document SSR, streaming, server functions, bundling and more. TanStack Start works great on Vercel when paired with [Nitro](https://v3.nitro.build/).

## [Getting started](#getting-started)

You can quickly deploy a TanStack Start application to Vercel by creating a new one below or configuring an existing one with Nitro:

[Deploy our TanStack Start template, or view a live example.](https://vercel.com/templates/starter/tanstack-start-on-vercel)

[Deploy](/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fvercel%2Ftree%2Fmain%2Fexamples%2Ftanstack-start&template=tanstack-start)[Live Example](https://tanstack-start-vercel-example-demo.vercel.app/)

## [Nitro Configuration](#nitro-configuration)

The [Nitro Vite plugin](https://v3.nitro.build/) allows deploying TanStack Start apps on Vercel, and integrates with Vercel's features.

To set up Nitro in your TanStack app, navigate to the root directory of your TanStack Start project with your terminal and install `nitro` with your preferred package manager:

pnpmyarnnpmbun

```
pnpm i nitro
```

To configure Nitro with TanStack Start, add the following lines to your `vite.config` file:

/vite.config.ts

```
import { tanstackStart } from '@tanstack/react-start/plugin/vite'
import { defineConfig } from 'vite'
import viteReact from '@vitejs/plugin-react'
import { nitro } from 'nitro/vite'
 
export default defineConfig({
  plugins: [
    tanstackStart(),
    nitro(),
    viteReact(),
  ],
})
```

### [Vercel Functions](#vercel-functions)

TanStack Start apps on Vercel benefit from the advantages of [Vercel Functions](/docs/functions) and use [Fluid Compute](/docs/fluid-compute) by default. This means your TanStack Start app will automatically scale up and down based on traffic.

## [More resources](#more-resources)

Learn more about deploying TanStack Start projects on Vercel with the following resources:

*   [Explore the TanStack docs](https://tanstack.com/start/latest/docs/framework/react/overview)
*   [Learn to use Vercel specific features with Nitro](https://v3.nitro.build/deploy/providers/vercel)

--------------------------------------------------------------------------------
title: "Supported Frameworks on Vercel"
description: "Learn about the frameworks that can be deployed to Vercel."
last_updated: "null"
source: "https://vercel.com/docs/frameworks/more-frameworks"
--------------------------------------------------------------------------------


---

**Navigation:** [← Previous](./09-invalid-request-method.md) | [Index](./index.md) | [Next →](./11-supported-frameworks-on-vercel.md)
