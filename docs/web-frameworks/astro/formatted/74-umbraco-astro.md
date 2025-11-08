---
title: "Umbraco & Astro"
section: 74
---

# Umbraco & Astro

> Add content to your Astro project using Umbraco as a CMS

[Umbraco CMS](https://umbraco.com/) is an open-source ASP.NET Core CMS. By default, Umbraco uses Razor pages for its front-end, but can be used as a headless CMS.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section you will use Umbraco’s native [Content Delivery API](https://docs.umbraco.com/umbraco-cms/reference/content-delivery-api) to provide content to your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2. **An Umbraco (v12+) project** - If you don’t have an Umbraco project yet, please see this [Installation guide](https://docs.umbraco.com/umbraco-cms/fundamentals/setup/install/).

### Setting up the Content Delivery API

[Section titled “Setting up the Content Delivery API”](#setting-up-the-content-delivery-api)

To enable the Content Delivery API, update your Umbraco project’s `appsettings.json` file:

appsettings.json

```json
{
  "Umbraco": {
    "CMS": {
      "DeliveryApi": {
        "Enabled": true,
        "PublicAccess": true
      }
    }
  }
}
```jsx
You can configure additional options as needed such as public access, API keys, allowed content types, membership authorisation, and more. See the [Umbraco Content Delivery API documentation](https://docs.umbraco.com/umbraco-cms/reference/content-delivery-api) for more information.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

Use a `fetch()` call to the Content Delivery API to access your content and make it available to your Astro components.

The following example displays a list of fetched articles, including properties such as the article date and content.

src/pages/index.astro

```astro
---
const res = await fetch('http://localhost/umbraco/delivery/api/v2/content?filter=contentType:article');
const articles = await res.json();
---
<h1>Astro + Umbraco 🚀</h1>
{
  articles.items.map((article) => (
      <h1>{article.name}</h1>
      <p>{article.properties.articleDate}</p>
      <div set:html={article.properties.content?.markup}></div>
  ))
}
```jsx
Read more about [data fetching in Astro](/en/guides/data-fetching/).

## Building a blog with Umbraco and Astro

[Section titled “Building a blog with Umbraco and Astro”](#building-a-blog-with-umbraco-and-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

* **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

* **An Umbraco project (v12+)** with the Content Delivery API enabled - Follow this [Installation guide](https://docs.umbraco.com/umbraco-cms/fundamentals/setup/install/) to create a new project.

### Creating blog posts in Umbraco

[Section titled “Creating blog posts in Umbraco”](#creating-blog-posts-in-umbraco)

From the [Umbraco backoffice](https://docs.umbraco.com/umbraco-cms/fundamentals/backoffice), create a Document Type for a simple blog article called ‘Article’.

1. Configure your ‘Article’ Document Type with the following properties:

   * Title (DataType: Textstring)
   * Article Date (DataType: Date Picker)
   * Content (DataType: Richtext Editor)

2. Toggle “Allow as root” to `true` on the ‘Article’ document type.

3. From the “Content” section in the Umbraco backoffice, [create and publish your first blog post](https://docs.umbraco.com/umbraco-cms/fundamentals/data/defining-content). Repeat the process as many times as you like.

For more information, watch a [video guide on creating Document Types](https://www.youtube.com/watch?v=otRuIkN80qM).

### Displaying a list of blog posts in Astro

[Section titled “Displaying a list of blog posts in Astro”](#displaying-a-list-of-blog-posts-in-astro)

Create a `src/layouts/` folder, then add a new file `Layout.astro` with the following code:

src/layouts/Layout.astro

```astro
---
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Blog with Astro and Umbraco</title>
</head>
<body>
    <main>
        <slot />
    </main>
</body>
</html>
```jsx
Your project should now contain the following files:

* src/

  * **layouts/**

    * **Layout.astro**

  * pages/

    * index.astro

To create a list of blog posts, first `fetch` to call the Content Delivery API `content` endpoint and filter by contentType of ‘article’. The article objects will include the properties and content set in the CMS. You can then loop through the articles and display a each title with a link to its article.

Replace the default contents of `index.astro` with the following code:

src/pages/index.astro

```astro
---
import Layout from '../layouts/Layout.astro';
const res = await fetch('http://localhost/umbraco/delivery/api/v2/content?filter=contentType:article');
const articles = await res.json();
---
<Layout>
  <h2>Blog Articles</h2>
  {
        articles.items.map((article: any) => (
            <div>
                <h3>{article.properties.title}</h3>
                <p>{article.properties.articleDate}</p>
                <a href={article.route.path}>Read more</a>
            </div>
        ))
    }
</Layout>
```jsx
### Generating individual blog posts

[Section titled “Generating individual blog posts”](#generating-individual-blog-posts)

Create the file `[...slug].astro` at the root of the `/pages/` directory. This file will be used to [generate the individual blog pages dynamically](/en/guides/routing/#dynamic-routes).

Note that the `params` property, which generates the URL path of the page, contains `article.route.path` from the API fetch. Similarly, the `props` property must include the entire `article` itself so that you can access all the information in your CMS entry.

Add the following code to `[...slug].astro` which will create your individual blog post pages:

\[...slug].astro

```astro
---
import Layout from '../layouts/Layout.astro';


export async function getStaticPaths() {
    let data = await fetch("http://localhost/umbraco/delivery/api/v2/content?filter=contentType:article");
    let articles = await data.json();


    return articles.items.map((article: any) => ({
        params: { slug: article.route.path },
        props: { article: article },
    }));
}


const { article } = Astro.props;
---


<Layout>
  <h1>{article.properties.title}</h1>
  <p>{article.properties.articleDate}</p>
  <div set:html={article.properties.content?.markup}></div>
</Layout>
```jsx
Your project should now contain the following files:

* src/

  * layouts/

    * Layout.astro

  * pages/

    * index.astro
    * **\[…slug].astro**

With the dev server running, you should now be able to view your Umbraco-created content in your browser preview of your Astro project. Congratulations! 🚀

## Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Local dev, HTTPS and self-signed SSL certificates

[Section titled “Local dev, HTTPS and self-signed SSL certificates”](#local-dev-https-and-self-signed-ssl-certificates)

If you are using the Umbraco HTTPS endpoint locally, any `fetch` queries will result in `fetch failed` with code `DEPTH_ZERO_SELF_SIGNED_CERT`. This is because Node (upon which Astro is built) won’t accept self-signed certificates by default. To avoid this, use the Umbraco HTTP endpoint for local dev.

Alternatively, you can set `NODE_TLS_REJECT_UNAUTHORIZED=0` in an `env.development` file and update `astro.config.js` as shown:

.env.development

```ini
NODE_TLS_REJECT_UNAUTHORIZED=0
```jsx
astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import { loadEnv } from "vite";


const { NODE_TLS_REJECT_UNAUTHORIZED } = loadEnv(process.env.NODE_ENV, process.cwd(), "");
process.env.NODE_TLS_REJECT_UNAUTHORIZED = NODE_TLS_REJECT_UNAUTHORIZED;
// https://astro.build/config
export default defineConfig({});
```jsx
This method is described in more detail in this [blog post showing how to configure your project for self-signed certificates](https://kjac.dev/posts/jamstack-for-free-with-azure-and-cloudflare/), with an [accompanying repo](https://github.com/kjac/UmbracoAzureCloudflare).

## Official Documentation

[Section titled “Official Documentation”](#official-documentation)

* [Content Delivery API - Umbraco Documentation](https://docs.umbraco.com/umbraco-cms/reference/content-delivery-api)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Astro-nomically Performant Websites using the Content Delivery API - Louis Richardson](https://24days.in/umbraco-cms/2023/sustainable-performant/astronomically-performant/)
* [Generating a TypeScript OpenAPI client from Umbraco’s Content Delivery API - Rick Butterfield](https://rickbutterfield.dev/blog/typescript-openapi-umbraco-content-delivery/)
* [Jamstack For Free With Azure And CloudFlare - Kenn Jacobsen](https://kjac.dev/posts/jamstack-for-free-with-azure-and-cloudflare/)
* [Quick n’ dirty blog with Astro and Umbraco - Kenn Jacobsen](https://kjac.dev/posts/quick-n-dirty-blog-with-astro-and-umbraco/)
* [Talk: Bake, Don’t Fry - Astro & The Content Delivery API - Adam Prendergast](https://www.youtube.com/watch?v=zNxqI25dtx4)

---

[← Previous](73-tina-cms-astro.md) | [Index](index.md) | [Next →](index.md)
