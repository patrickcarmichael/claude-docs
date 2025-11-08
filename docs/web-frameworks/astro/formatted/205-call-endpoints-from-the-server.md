---
title: "Call endpoints from the server"
section: 205
---

# Call endpoints from the server

> Learn how to call endpoints from the server in Astro.

Endpoints can be used to serve many kinds of data. This recipe calls a server endpoint from a page’s component script to display a greeting, without requiring an additional fetch request.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* A project with [SSR](/en/guides/on-demand-rendering/) (output: ‘server’) enabled

## Recipe

[Section titled “Recipe”](#recipe)

1. Create an endpoint in a new file `src/pages/api/hello.ts` that returns some data:

   src/pages/api/hello.ts

   ```ts
   import type { APIRoute } from 'astro'


   export const GET: APIRoute = () => {
     return new Response(
       JSON.stringify({
         greeting: 'Hello',
       }),
     )
   }
   ```jsx
2. On any Astro page, import the `GET()` method from the endpoint. Call it with the [`Astro` global](/en/reference/api-reference/) to provide the request context, and use the response on the page:

   src/pages/index.astro

   ```astro
   ---
   import { GET } from './api/hello.ts'


   let response = await GET(Astro)
   const data = await response.json()
   ---


   <h1>{data.greeting} world!</h1>
   ```

---

[← Previous](204-create-a-new-project-based-on-a-github-repositorys-main-branch.md) | [Index](index.md) | [Next →](index.md)
