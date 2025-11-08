---
title: "Prepr CMS & Astro"
section: 63
---

# Prepr CMS & Astro

> Add content to your Astro project using Prepr as a CMS

[Prepr CMS](https://www.prepr.io/) is a headless CMS with built-in personalization.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Prepr CMS provides a [GraphQL API](https://docs.prepr.io/reference/graphql/v1/overview) to connect your data to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need the following:

* A new or existing Astro project configured for [on-demand rendering](/en/guides/on-demand-rendering/).
* [A free Prepr account](https://signup.prepr.io/)
* [A Prepr environment with existing blog posts](https://docs.prepr.io/account/set-up-environments#create-an-envirntonment). These posts must include a `title` and `content`. Other fields are optional.

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add the Prepr endpoint to your Astro project, create a `.env file` in the root of your project if one does not already exist and add the following variable:

.env

```ini
PREPR_ENDPOINT=YOUR_PREPR_API_URL
```jsx
You will find your `YOUR_PREPR_API_URL` value from your Prepr account settings:

1. Go to  **Settings > Access tokens** to view both your Preview and Production access tokens.

2. Use the **API URL** value from the **GraphQL Production** access token to only retrieve published content items for your Astro site.

### Configuring the Prepr endpoint

[Section titled “Configuring the Prepr endpoint”](#configuring-the-prepr-endpoint)

Create a new folder `src/lib/` and add a new file called `prepr.js`. This is where you will configure the Prepr endpoint. Add the following code to fetch your data from Prepr CMS:

src/lib/prepr.js

```js
export async function Prepr(query, variables) {
    const response = await fetch(import.meta.env.PREPR_ENDPOINT, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query, variables }),
    })
    return response
}
```jsx
Your root directory should now include these files:

* src/

  * lib/

    * **prepr.js**

* **.env**

* astro.config.mjs

* package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

You will fetch your data from Prepr by writing queries to interact with its GraphQL API.

#### Create a GraphQL query to retrieve your blog articles:

[Section titled “Create a GraphQL query to retrieve your blog articles:”](#create-a-graphql-query-to-retrieve-your-blog-articles)

1. Create a new folder `src/queries/` and add a file named `get-articles.js`.

2. Add the following query to this file to retrieve all articles:

   src/queries/get-articles.js

   ```js
   const GetArticles = `
   query {
       Articles {
         items {
           _id
           _slug
           title
       }
     }
   }
   `
   export default GetArticles
   ```jsx
3. To display a linked list of your blog posts on a page, import and execute your query, including the necessary Prepr endpoint. You will then have access to all your posts titles and their slugs to render to the page. (In the next step, you will [create individual pages for your blog posts](#creating-individual-blog-post-pages).)

   src/pages/index.astro

   ```diff
   ---
   import Layout from '../layouts/Layout.astro';
   +import { Prepr } from '../lib/prepr.js';
   +import GetArticles from '../queries/get-articles.js';


   +const response = await Prepr(GetArticles)
   +const { data } = await response.json()
   +const articles = data.Articles
   ---


   <Layout title="My blog site">
     <h1>
       My blog site
     </h1>
     <ul>
       +{
   +      articles.items.map((post) => (
           <li>
             <a href={post._slug}>{post.title}</a>
           </li>
   +      ))
       +}
     </ul>
   </Layout>
   ```jsx
Your root directory should include these new files:

* src/

  * lib/

    * prepr.js

  * pages/

    * index.astro

  * **queries** /

    * **get-articles.js**

* .env

* astro.config.mjs

* package.json

#### Creating individual blog post pages

[Section titled “Creating individual blog post pages”](#creating-individual-blog-post-pages)

To create a page for each blog post, you will execute a new GraphQL query on a [dynamic routing](/en/guides/routing/#on-demand-dynamic-routes) `.astro` page. This query will fetch a specific article by its slug and a new page will be created for each individual blog post.

1. Create a file called `get-article-by-slug.js` in the `queries` folder and add the following to query a specific article by its slug and return data such as the article `title` and `content`:

   src/lib/queries/get-article-by-slug.js

   ```js
   const GetArticleBySlug = `
   query ($slug: String) {
      Article (slug: $slug) {
        _id
        title
        content {
          __typename
          ... on Text {
            body
            text
          }
          ... on Assets {
            items {
              url
            }
          }
        }
      }
   }`


   export default GetArticleBySlug
   ```jsx
   Tip

   You can create and [test GraphQL queries](https://docs.prepr.io/reference/graphql/v1/test-queries) using the [Apollo explorer](https://studio.apollographql.com/sandbox/explorer) in Prepr. Open the API Explorer from the *Article* content item page in Prepr. The Article content is stored in a *Dynamic content field*. Check out the GraphQL docs for more details on [how to fetch the data within this field](https://docs.prepr.io/reference/graphql/v1/schema-field-types-dynamic-content-field).

2. Inside the `src/pages` folder, create a file called `[…slug].astro`. Add the following code to import and execute the query from the previous step and display the retrieved article:

   src/pages/\[...slug].astro

   ```astro
   ---
   import Layout from '../layouts/Layout.astro';
   import {Prepr} from '../lib/prepr.js';
   import GetArticleBySlug from '../queries/get-article-by-slug.js';


   const { slug } = Astro.params;
   const response = await Prepr(GetArticleBySlug, {slug})
   const { data } = await response.json()
   const article = data.Article
   ---


   <Layout title={article.title}>
     <main>
       <h1>{article.title}</h1>
       {
         article.content.map((content) => (
           <div>
             {
               content.__typename === "Assets" &&
               <img src={content.items[0].url} width="300" height="250"/>
             }
             {
               content.__typename === 'Text' &&
               <div set:html={content.body}></div>
             }
           </div>
         ))
       }
     </main>
   </Layout>
   ```jsx
Your root directory should now include these new files:

* src/

  * lib/

    * prepr.js

  * pages/

    * index.astro
    * **\[…slug].astro**

  * queries/

    * get-articles.js
    * **get-article-by-slug.js**

* .env

* astro.config.mjs

* package.json

Now, when you click an article link from the main list of blog posts, you will be taken to a page with its individual content.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your Prepr blog, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Follow the [Prepr CMS Astro quickstart](https://github.com/preprio/astro-quick-start) guide to make a simple blog with Astro and Prepr CMS. 
* Check out the [Connecting Prepr CMS to Astro](https://docs.prepr.io/connecting-front-end-apps/astro) for an overview of Astro and Prepr CMS resources.

---

[← Previous](62-payload-cms-astro.md) | [Index](index.md) | [Next →](index.md)
