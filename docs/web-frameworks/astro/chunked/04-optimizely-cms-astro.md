**Navigation:** [← Previous](./03-apostrophecms-astro.md) | [Index](./index.md) | [Next →](./05-deploy-your-astro-site-to-flyio.md)

---

# Optimizely CMS & Astro

> Add content to your Astro project using Optimizely CMS

[Optimizely CMS](https://www.optimizely.com/products/content-management/) is available as a headless CMS powered by GraphQL that provides a visual editor.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* The official [Optimizely SaaS CMS documentation](https://docs.developers.optimizely.com/content-management-system/v1.0.0-CMS-SaaS/docs/overview-saas)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Build a headless blog with Astro and Optimizely SaaS CMS](https://world.optimizely.com/blogs/jacob-pretorius/dates/2024/5/build-a-headless-blog-with-astro-and-optimizely-saas-cms/)
* [Sample Astro + Optimizely Graph starter project templates](https://github.com/jacobpretorius/Opti.SaaS.Astro.Demo/)

# Payload CMS & Astro

> Add content to your Astro project using Payload as a CMS

[PayloadCMS](https://payloadcms.com/) is a headless open-source content management system that can be used to provide content for your Astro project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2. **A MongoDB database** - PayloadCMS will ask you for a MongoDB connection string when creating a new project. You can set one up locally or use [MongoDBAtlas](https://www.mongodb.com/) to host a database on the web for free.
3. **A PayloadCMS REST API** - Create a [PayloadCMS](https://payloadcms.com/docs/getting-started/installation) project and connect it to your MongoDB database during the setup.

Choosing a template

During the PayloadCMS installation, you will be asked if you want to use a template.

Choosing any of the available templates at this step (such as ‘blog’) automatically generates additional collections for you to use. Otherwise, you will need to manually create your PayloadCMS collections.

### Configuring Astro for your PayloadCMS collection

[Section titled “Configuring Astro for your PayloadCMS collection”](#configuring-astro-for-your-payloadcms-collection)

Your Payload project template will contain a file called Posts.ts in `src/collections/`. If you did not choose a template during installation that created a content collection for you, you can create a new Payload CMS Collection by adding this configuration file manually. The example below shows this file for a collection called `posts` that requires `title`, `content`, and `slug` fields:

src/collections/Posts.ts

```ts
import { CollectionConfig } from "payload/types";


const Posts: CollectionConfig = {
  slug: "posts",
  admin: {
    useAsTitle: "title",
  },
  access: {
    read: () => true,
  },


  fields: [
    {
      name: "title",
      type: "text",
      required: true,
    },
    {
      name: "content",
      type: "text",
      required: true,
    },
    {
      name: "slug",
      type: "text",
      required: true,
    },
  ],
};


export default Posts;
```

1. Import and add both `Users` (available in all PayloadCMS projects) and any other collections (e.g. `Posts`) to the available collections in the `payload.config.ts` file.

   src/payload.config.ts

   ```diff
   import { buildConfig } from "payload/config";
   import path from "path";


   +import Users from "./collections/Users";
   +import Posts from "./collections/Posts";


   export default buildConfig({
     serverURL: "http://localhost:4321",
     admin: {
       user: Users.slug,
     },
   +  collections: [Users, Posts],
     typescript: {
       outputFile: path.resolve(__dirname, "payload-types.ts"),
     },
     graphQL: {
       schemaOutputFile: path.resolve(__dirname, "generated-schema.graphql"),
     },
   });
   ```

   This will make a new collection called “Posts” appear in your PayloadCMS Dashboard next to the “Users” collection.

2. Enter the “Posts” collection and create a new post. After saving it, you will notice the API URL appear in the bottom right corner.

3. With the dev server running, open `http://localhost:4321/api/posts` in your browser. You should see a JSON file containing the post you have created as an object.

   ```json
   {
     "docs":[
         {
           "id":"64098b16483b0f06a7e20ed4",
           "title":"Astro & PayloadCMS Title 🚀",
           "content":"Astro & PayloadCMS Content",
           "slug":"astro-payloadcms-slug",
           "createdAt":"2023-03-09T07:30:30.837Z",
           "updatedAt":"2023-03-09T07:30:30.837Z"
         }
     ],
     "totalDocs":1,
     "limit":10,
     "totalPages":1,
     "page":1,
     "pagingCounter":1,
     "hasPrevPage":false,
     "hasNextPage":false,
     "prevPage":null,
     "nextPage":null
   }
   ```

Tip

By default, both Astro and PayloadCMS will use port 4321. You might want to change the PayloadCMS port in the `src/server.ts` file. Don’t forget to update the `serverURL` in `src/payload.config.ts` as well.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

Fetch your PayloadCMS data through your site’s unique REST API URL and the route for your content. (By default, PayloadCMS will mount all routes through `/api`.) Then, you can render your data properties using Astro’s `set:html=""` directive.

Together with your post, PayloadCMS will return some top-level metadata. The actual documents are nested within the `docs` array.

For example, to display a list of post titles and their content:

src/pages/index.astro

```astro
---
import HomeLayout from "../layouts/HomeLayout.astro";


const res = await fetch("http://localhost:5000/api/posts") // http://localhost:4321/api/posts by default
const posts = await res.json()
---


<HomeLayout title='Astro Blog'>
  {
    posts.docs.map((post) => (
        <h2 set:html={post.title} />
        <p set:html={post.content} />
    ))
  }
</HomeLayout>
```

## Building a blog with PayloadCMS and Astro

[Section titled “Building a blog with PayloadCMS and Astro”](#building-a-blog-with-payloadcms-and-astro)

Create a blog index page `src/pages/index.astro` to list each of your posts with a link to its own page.

Fetching via the API returns an array of objects (posts) that include, among others, the following properties:

* `title`
* `content`
* `slug`

src/pages/index.astro

```astro
---
import HomeLayout from "../layouts/HomeLayout.astro";


const res = await fetch("http://localhost:5000/api/posts") // http://localhost:4321/api/posts by default
const posts = await res.json()
---


<HomeLayout title='Astro Blog'>
  <h1>Astro + PayloadCMS 🚀</h1>
  <h2>Blog posts list:</h2>
  <ul>
    {
      posts.docs.map((post) =>(
        <li>
          <a href={`posts/${post.slug}`} set:html={post.title} />
        </li>
      ))
    }
  </ul>
</HomeLayout>
```

### Using the PayloadCMS API to generate pages

[Section titled “Using the PayloadCMS API to generate pages”](#using-the-payloadcms-api-to-generate-pages)

Create a page `src/pages/posts/[slug].astro` to [dynamically generate a page](/en/guides/routing/#dynamic-routes) for each post.

src/pages/posts/\[slug].astro

```astro
---
import PostLayout from "../../layouts/PostLayout.astro"


const {title, content} = Astro.props


// The getStaticPaths() is required for static Astro sites.
// If using SSR, you will not need this function.
export async function getStaticPaths() {
    let data = await fetch("http://localhost:5000/api/posts")
    let posts = await data.json()


    return posts.docs.map((post) => {
        return {
            params: {slug: post.slug},
            props: {title: post.title, content: post.content},
        };
    });
}
---
<PostLayout title={title}>
    <article>
        <h1 set:html={title} />
        <p set:html={content} />
    </article>
</PostLayout>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* Check out the [official Astro Payload CMS integration](https://github.com/payloadcms/payload/tree/main/examples/astro).
* Try this [Payload CMS & Astro Template](https://github.com/Lambdo-Labs/payloadcms-astro-template).
* Check out [Astroad](https://github.com/mooxl/astroad) for easy development and VPS deployment with Docker.

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
```

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
```

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
   ```

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
   ```

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
   ```

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
   ```

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

# Prismic & Astro

> Add content to your Astro project using Prismic as a CMS

[Prismic](https://prismic.io/) is a headless content management system.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Building with Astro & Prismic - w/ Nate Moore](https://www.youtube.com/watch?v=qFUfuDSLdxM) (livestream) and the [repo from the show](https://github.com/natemoo-re/miles-of-code).

# Sanity & Astro

> Add content to your Astro project using Sanity as a CMS

[Sanity](https://www.sanity.io) is a headless content management system that focuses on [structured content](https://www.sanity.io/structured-content-platform).

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Official Sanity integration for Astro](https://www.sanity.io/plugins/sanity-astro)

* [Build your blog with Astro and Sanity](https://www.sanity.io/guides/sanity-astro-blog)

* [A minimal Astro site with a Sanity Studio](https://www.sanity.io/templates/astro-sanity-clean)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/astro-chef-project.CkjCJgM-_ZI34Cs.webp) The Balanced Chef](https://astro.build/themes/details/the-balanced-chef/)

# Sitecore Experience Manager & Astro

> Add content to your project using Sitecore as your CMS.

[Sitecore Experience Manager (XM)](https://www.sitecore.com/products/experience-manager) is an enterprise-level content management system built on ASP.NET.

## Getting started

[Section titled “Getting started”](#getting-started)

1. [Create a Sitecore Headless website](https://doc.sitecore.com/xp/en/developers/sxa/103/sitecore-experience-accelerator/create-a-headless-tenant-and-site.html) following Sitecore’s official documentation.

2. Run the following project initialization command in your terminal:

   ```shell
   npx @astro-sitecore-jss/create-astro-sitecore-jss@latest
   ```

3. Follow the instructions in the terminal to create your project.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Sitecore JavaScript Software Development Kit for Astro](https://github.com/exdst/jss-astro-public) on GitHub
* [Introduction to Sitecore with Astro](https://exdst.com/posts/20231002-sitecore-astro)
* [Starting Your First Sitecore Astro Project](https://exdst.com/posts/20240103-first-sitecore-astro-project)

# Sitepins & Astro

> Use Sitepins to manage content for your Astro project with a Git-based visual CMS.

[Sitepins](https://sitepins.com) is a Git-based, headless CMS for websites built with modern frameworks like Astro. It offers a clean WYSIWYG editor, a version-controlled content workflow, and seamless integration with Astro and other SSGs.

## Getting started

[Section titled “Getting started”](#getting-started)

1. [Create a Sitepins account](https://app.sitepins.com/register).

2. Connect your GitHub repository that contains your Astro project.

3. Configure your content, media and config folders and start editing in the visual editor.

Once connected, Sitepins will sync your content from the selected folder and provide a visual interface to manage and publish content with full Git version control.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Sitepins Website](https://sitepins.com)
* [Documentation](https://docs.sitepins.com)
* [Live Demo](https://demo.sitepins.com)

# Spinal & Astro

> Add content to your project using Spinal as your CMS.

[Spinal](https://spinalcms.com/cms-for-astro/) is a commercial, SaaS-focused, Git-based CMS.

## Getting started

[Section titled “Getting started”](#getting-started)

1. [Create a Spinal account](https://spinalcms.com/signup/).

2. Connect your GitHub account to Spinal.

3. Select your Astro repository when prompted.

All Markdown content from the selected folder will be imported into your Spinal account and is ready to be edited.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Documentation theme built for Astro with Tailwind CSS](https://spinalcms.com/resources/astro-documentation-theme-with-tailwind-css/)

## Production Sites

[Section titled “Production Sites”](#production-sites)

The following sites use Astro + Spinal in production:

* [spinalcms.com](https://spinalcms.com/) (all blog articles, documentation, changelog, feature pages, etc.)

# Headless Statamic & Astro

> Add content to your Astro project using Statamic as a CMS

[Statamic](https://statamic.com/) is a modern, flat-file CMS. It allows developers to easily create dynamic websites and applications while offering content editors an intuitive and user-friendly interface for managing content.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Statamic comes with a built-in [REST API](https://statamic.dev/rest-api) and [GraphQL API](https://statamic.dev/graphql) to connect your data to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. REST API and GraphQL API are only available in a pro version of Statamic. You can try the Pro version free on your [local machine](https://statamic.dev/tips/how-to-enable-statamic-pro#trial-mode).
2. **An Astro project** - If you still need an Astro project, our [Installation guide](/en/install-and-setup/) will get you up and running quickly.
3. **A Statamic site** - If you need a Statamic website, [this guide](https://statamic.dev/quick-start-guide) will help you get started. Remember to [enable REST API](https://statamic.dev/rest-api#enable-the-api) or [GraphQL API](https://statamic.dev/graphql#enable-graphql) by adding `STATAMIC_API_ENABLED=true` or `STATAMIC_GRAPHQL_ENABLED=true` in the `.env` file and enable required resources in the API configuration file.

Caution

All the examples assume that your website has a collection called `posts`, that has a blueprint called `post`, and this blueprint has a title field (fieldtype text) and content (fieldtype markdown).

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

Caution

If you are using Statamic and Astro on your local machine remember to use `127.0.0.1` instead of `localhost` when fetching the API.

When requesting from the Astro server `localhost` doesn’t resolve correctly like it does in the browser, and any fetch to either API will fail.

#### REST API

[Section titled “REST API”](#rest-api)

Fetch your Statamic data from your site’s REST API URL. By default, it’s `https://[YOUR-SITE]/api/`. Then, you can render your data properties using Astro’s `set:html={}` directive.

For example, to display a list of titles and their content from a selected [collection](https://statamic.dev/collections):

src/pages/index.astro

```astro
---
const res = await fetch("https://[YOUR-SITE]/api/collections/posts/entries?sort=-date")
const posts = await res.json()
---
<h1>Astro + Statamic 🚀</h1>
{
  posts.map((post) => (
      <h2 set:html={post.title} />
      <p set:html={post.content} />
  ))
}
```

#### GraphQL

[Section titled “GraphQL”](#graphql)

Fetch your Statamic data with your site’s GraphQL API URL. By default, it’s `https://[YOUR-SITE]/graphql/`. Then, you can render your data properties using Astro’s `set:html={}` directive.

For example, to display a list of titles and their content from a selected [collection](https://statamic.dev/collections):

src/pages/index.astro

```astro
---
const graphqlQuery = {
  query: `
    query Entries($page: Int, $locale: String) {
      entries(
        collection: "posts"
        sort: "date asc"
        limit: 20
        page: $page
        filter: { locale: $locale }
      ) {
        current_page
        has_more_pages
        data {
          title
          ... on Entry_Posts_Post {
              content
            }
        }
      }
    }
  `,
  variables: {
    page: page,
    locale: locale,
  },
};


const res = await fetch("https://[YOUR-SITE]/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(graphqlQuery),
})


const { data } = await res.json();
const entries = data?.entries;
---
<h1>Astro + Statamic 🚀</h1>
{
  entries.data.map((post) => (
      <h2 set:html={post.title} />
      <p set:html={post.content} />
  ))
}
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your Astro site visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [How to build a static site using Statamic as headless CMS](https://buddy.works/guides/statamic-rest-api)
* [Implementing Astro live previews in headless Statamic](https://maciekpalmowski.dev/implementing-live-previews-in-headless-statamic-when-using-astro/)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/creek.CgpBUanV_Z1gsxon.webp) Creek](https://astro.build/themes/details/creek/)

# Storyblok & Astro

> Add content to your Astro project using Storyblok as a CMS

[Storyblok](https://www.storyblok.com/) is a component-based headless CMS that allows you to manage your content using reusable components called Bloks.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you will use the [Storyblok integration](https://github.com/storyblok/monoblok/tree/main/packages/astro) to connect Storyblok to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A Storyblok account and space** - If you don’t have an account yet, [sign up for free](https://app.storyblok.com/#/signup) and create a new space.

3. **Storyblok Preview token** - This token will be used to fetch drafts and published versions of your content. You can find and generate your API token in the Access Tokens tab of your Storyblok space settings.

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your Storyblok credentials to Astro, create a `.env` file in the root of your project with the following variable:

.env

```ini
STORYBLOK_TOKEN=YOUR_PREVIEW_TOKEN
```

Now, you should be able to use these environment variables in your project.

Your root directory should now include this new file:

* src/

  * …

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect Astro with your Storyblok space, install the official [Storyblok integration](https://github.com/storyblok/monoblok/tree/main/packages/astro) using the command below for your preferred package manager:

* npm

  ```shell
  npm install @storyblok/astro vite
  ```

* pnpm

  ```shell
  pnpm add @storyblok/astro vite
  ```

* Yarn

  ```shell
  yarn add @storyblok/astro vite
  ```

### Configuring Storyblok

[Section titled “Configuring Storyblok”](#configuring-storyblok)

Modify your Astro config file to include the Storyblok integration:

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import { storyblok } from '@storyblok/astro';
import { loadEnv } from 'vite';


const env = loadEnv("", process.cwd(), 'STORYBLOK');


export default defineConfig({
  integrations: [
    storyblok({
      accessToken: env.STORYBLOK_TOKEN,
      components: {
        // Add your components here
      },
      apiOptions: {
        // Choose your Storyblok space region
        region: 'us', // optional,  or 'eu' (default)
      },
    })
  ],
});
```

The Storyblok integration requires an object with the following properties:

1. `accessToken` - This references the Storyblok API token that you added in the previous step.

   Tip

   Since the Astro config file does not normally support environment variables, use the `loadEnv` function from Vite to load them.

2. `components` - An object that maps Storyblok component names to paths to your local components. This is required to render your Storyblok Bloks in Astro.

   Note

   The component paths are relative to the `src` directory. For example, if your component is located at `src/storyblok/MyComponent.astro`, the path would be `storyblok/MyComponent` (without the `.astro` extension).

3. `apiOptions` - An object containing [Storyblok API options](https://www.storyblok.com/docs/packages/storyblok-astro#api).

   Caution

   By default, the region is `eu`. If your Storyblok space was created in the US region, you will need to set the region to `us`.

### Connecting Bloks to Astro components

[Section titled “Connecting Bloks to Astro components”](#connecting-bloks-to-astro-components)

To connect your Bloks to Astro, create a new folder named `storyblok` in the `src` directory. This folder will contain all the Astro components that will match your Bloks in your Storyblok Blok library.

In this example, you have a `blogPost` Blok content type in your Storyblok library with the following fields:

* `title` - A text field
* `description` - A text field
* `content` - A rich text field

Our goal is to create the equivalent Astro component that will use these fields to render its content. To do this, create a new file named `BlogPost.astro` inside `src/storyblok` with the following content:

src/storyblok/BlogPost.astro

```astro
---
import { storyblokEditable, renderRichText } from '@storyblok/astro'


const { blok } = Astro.props
const content = renderRichText(blok.content)
---


<article {...storyblokEditable(blok)}>
  <h1>{blok.title}</h1>
  <p>{blok.description}</p>
  <Fragment set:html={content} />
</article>
```

The `blok` property contains the data that you will receive from Storyblok. It also contains the fields that were defined in the `blogPost` content type Blok in Storyblok.

To render our content, the integration provides utility functions such as:

* `storyblokEditable` - it adds the necessary attributes to the elements so that you can edit them in Storyblok.
* `renderRichText` - it transforms the rich text field into HTML.

Your root directory should include this new file:

* src/

  * storyblok/

    * **BlogPost.astro**

* .env

* astro.config.mjs

* package.json

Finally, to connect the `blogPost` Blok to the `BlogPost` component, add a new property to your components object in your Astro config file.

* The key is the name of the Blok in Storyblok. In this case, it is `blogPost`.
* The value is the path to the component. In this case, it is `storyblok/BlogPost`.

Caution

The `key` should exactly match your Blok name in Storyblok to be referenced correctly. If these don’t match, or you’re trying to reference a component that doesn’t exist in Storyblok, you’ll get an error.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import { storyblok } from '@storyblok/astro';
import { loadEnv } from 'vite';


const env = loadEnv("", process.cwd(), 'STORYBLOK');


export default defineConfig({
  integrations: [
    storyblok({
      accessToken: env.STORYBLOK_TOKEN,
      components: {
+        blogPost: 'storyblok/BlogPost',
      },
      apiOptions: {
        region: 'us',
      },
    })
  ],
});
```

### Fetching data

[Section titled “Fetching data”](#fetching-data)

To test the setup, in Storyblok create a new story with the `blogPost` content type named `test-post`. In Astro, create a new page in the `src/pages/` directory named `test-post.astro` with the following content:

src/pages/test-post.astro

```astro
---
import { useStoryblokApi } from '@storyblok/astro'
import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'


const storyblokApi = useStoryblokApi()


const { data } = await storyblokApi.get("cdn/stories/test-post", {
  version: import.meta.env.DEV ? "draft" : "published",
});


const content = data.story.content;
---
<StoryblokComponent blok={content} />
```

To query your data, use the `useStoryblokApi` hook. This will initialize a new client instance using your integration configuration.

To render your content, pass the `content` property of the Story to the `StoryblokComponent` as a `blok` prop. This component will render the Bloks that are defined inside the `content` property. In this case, it will render the `BlogPost` component.

## Making a blog with Astro and Storyblok

[Section titled “Making a blog with Astro and Storyblok”](#making-a-blog-with-astro-and-storyblok)

With the integration set up, you can now create a blog with Astro and Storyblok.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. **A Storyblok space** - For this tutorial, we recommend using a new space. If you already have a space with Bloks, feel free to use them, but you will need to modify the code to match the Blok names and content types.

2. **An Astro project integrated with Storyblok** - See [integrating with Astro](#integrating-with-astro) for instructions on how to set up the integration.

### Creating a blok library

[Section titled “Creating a blok library”](#creating-a-blok-library)

To create Bloks, go to the Storyblok app and click on the **Block Library** tab. Click on the `+ New blok` button and create the following Bloks:

1. `blogPost` - A content type Blok with the following fields:

   * `title` - A text field
   * `description` - A text field
   * `content` - A rich text field

2. `blogPostList` - An empty nestable Blok

3. `page` - A content type Blok with the following fields:

   * `body` - A nestable Blok

### Creating content

[Section titled “Creating content”](#creating-content)

To add new content, go to the content section by clicking on the **Content** tab. Using the Blok library that you created in the previous step, create the following stories:

1. `home` - A content type story with the `page` Blok. Inside the `body` field, add a `blogPostList` Blok.

2. `blog/no-javascript` - A story with the `blogPost` content type inside the blog folder.

   ```yaml
   title: No JavaScript
   description: A sample blog post
   content: Hi there! This blog post doesn't use JavaScript.
   ```

3. `blog/astro-is-amazing` - A story with the `blogPost` content type inside the blog folder.

   ```yaml
   title: Astro is amazing
   description: We love Astro
   content: Hi there! This blog post was build with Astro.
   ```

Now that you have your content ready, return to your Astro project and start building your blog.

### Connecting Bloks to components

[Section titled “Connecting Bloks to components”](#connecting-bloks-to-components)

To connect your newly created Bloks to Astro components, create a new folder named `storyblok` in your `src` directory and add the following files:

`Page.astro` is a nestable Block content type component that will recursively render all the Bloks inside the `body` property of the `page` Blok. It also adds the `storyblokEditable` attributes to the parent element which will allow us to edit the page in Storyblok.

src/storyblok/Page.astro

```astro
---
import { storyblokEditable } from '@storyblok/astro'
import StoryblokComponent from "@storyblok/astro/StoryblokComponent.astro";
const { blok } = Astro.props
---


<main {...storyblokEditable(blok)}>
  {
    blok.body?.map((blok) => {
      return <StoryblokComponent blok={blok} />
    })
  }
</main>
```

`BlogPost.astro` will render the `title`, `description` and `content` properties of the `blogPost` Blok.

To transform the `content` property from a rich text field to HTML, you can use the `renderRichText` helper function.

src/storyblok/BlogPost.astro

```astro
---
import { storyblokEditable, renderRichText } from '@storyblok/astro'
const { blok } = Astro.props
const content = renderRichText(blok.content)
---
<article {...storyblokEditable(blok)}>
  <h1>{blok.title}</h1>
  <p>{blok.description}</p>
  <Fragment set:html={content} />
</article>
```

`BlogPostList.astro` is a nestable Blok content type component that will render a list of blog post previews.

It uses the `useStoryblokApi` hook to fetch all the stories with the content type of `blogPost`. It uses the `version` query parameter to fetch the draft versions of the stories when in development mode and the published versions when building for production.

`Astro.props` is used to set up the editor in Storyblok. Additional props can also be passed to your component here, if needed.

src/storyblok/BlogPostList.astro

```astro
---
import { storyblokEditable } from '@storyblok/astro'
import { useStoryblokApi } from '@storyblok/astro'


const storyblokApi = useStoryblokApi();


const { data } = await storyblokApi.get('cdn/stories', {
  version: import.meta.env.DEV ? "draft" : "published",
  content_type: 'blogPost',
})


const posts = data.stories.map(story => {
  return {
    title: story.content.title,
    date: new Date(story.published_at).toLocaleDateString("en-US", {dateStyle: "full"}),
    description: story.content.description,
    slug: story.full_slug,
  }
})


const { blok } = Astro.props
---


<ul {...storyblokEditable(blok)}>
  {posts.map(post => (
    <li>
      <time>{post.date}</time>
      <a href={post.slug}>{post.title}</a>
      <p>{post.description}</p>
    </li>
  ))}
</ul>
```

Finally, add your components to the `components` property of the `storyblok` config object in `astro.config.mjs`. The key is the name of the Blok in Storyblok, and the value is the path to the component relative to `src`.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
import { storyblok } from '@storyblok/astro';
import { loadEnv } from 'vite';


const env = loadEnv("", process.cwd(), 'STORYBLOK');


export default defineConfig({
  integrations: [
    storyblok({
      accessToken: env.STORYBLOK_TOKEN,
      components: {
+        blogPost: 'storyblok/BlogPost',
+        blogPostList: 'storyblok/BlogPostList',
+        page: 'storyblok/Page',
      },
      apiOptions: {
        region: 'us',
      },
    })
  ],
});
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

To create a route for a specific `page`, you can fetch its content directly from the Storyblok API and pass it to the `StoryblokComponent` component. Remember to make sure you have added the `Page` component to your astro.config.mjs.

Create an `index.astro` file in `src/pages/` to render the `home` page:

src/pages/index.astro

```astro
---
import { useStoryblokApi } from '@storyblok/astro'
import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'
import BaseLayout from '../layouts/BaseLayout.astro'


const storyblokApi = useStoryblokApi();
const { data } = await storyblokApi.get('cdn/stories/home', {
  version: import.meta.env.DEV ? "draft" : "published",
});
const content = data.story.content;
---
<html lang="en">
  <head>
    <title>Storyblok & Astro</title>
  </head>
  <body>
    <StoryblokComponent blok={content} />
  </body>
</html>
```

To generate pages for all of your blog posts, create a `.astro` page that will create dynamic routes. This approach varies depending on whether your routes are prerendered (the default in Astro) or [rendered on demand](/en/guides/on-demand-rendering/).

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

If you are using Astro’s default static site generation, you will use [dynamic routes](/en/guides/routing/#dynamic-routes) and the `getStaticPaths` function to generate your project pages.

Create a new directory `src/pages/blog/` and add a new file called `[...slug].astro` with the following code:

src/pages/blog/\[...slug].astro

```astro
---
import { useStoryblokApi } from '@storyblok/astro'
import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'


export async function getStaticPaths() {
  const sbApi = useStoryblokApi();


  const { data } = await sbApi.get("cdn/stories", {
    content_type: "blogPost",
    version: import.meta.env.DEV ? "draft" : "published",
  });


  const stories = Object.values(data.stories);


  return stories.map((story) => {
    return {
      params: { slug: story.slug },
    };
  });
}


const sbApi = useStoryblokApi();
const { slug } = Astro.params;
const { data } = await sbApi.get(`cdn/stories/blog/${slug}`, {
  version: import.meta.env.DEV ? "draft" : "published",
});


const story = data.story;
---


<html lang="en">
  <head>
    <title>Storyblok & Astro</title>
  </head>
  <body>
    <StoryblokComponent blok={story.content} />
  </body>
</html>
```

This file will generate a page for each story, with the slug and content fetched from the Storyblok API.

Note

When adding folders inside of Storyblok, include them in the slug when interacting with the Storyblok API. For example, in the GET request above we can use **cdn/stories/blog**, with a blog folder inside rather than using them at the root.

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If you are [rendering your routes on demand with an adapter](/en/guides/on-demand-rendering/), you will use dynamic routes to fetch the page data from Storyblok.

Create a new directory `src/pages/blog/` and add a new file called `[...slug].astro` with the following code:

src/pages/blog/\[...slug].astro

```astro
---
import { useStoryblokApi } from '@storyblok/astro'
import StoryblokComponent from '@storyblok/astro/StoryblokComponent.astro'
const storyblokApi = useStoryblokApi()
const slug = Astro.params.slug;
let content;
try {
  const { data } = await storyblokApi.get(`cdn/stories/blog/${slug}`, {
    version: import.meta.env.DEV ? "draft" : "published",
  });
  content = data.story.content
} catch (error) {
  return Astro.redirect('/404')
}
---
<html lang="en">
  <head>
    <title>Storyblok & Astro</title>
  </head>
  <body>
    <StoryblokComponent blok={content} />
  </body>
</html>
```

This file will fetch and render the page data from Storyblok that matches the dynamic `slug` parameter.

Since you are using a redirect to `/404`, create a 404 page in `src/pages`:

src/pages/404.astro

```astro
<html lang="en">
  <head>
    <title>Not found</title>
  </head>
  <body>
    <p>Sorry, this page does not exist.</p>
  </body>
</html>
```

If the story is not found, the request will be redirected to the 404 page.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Storyblok changes

[Section titled “Rebuild on Storyblok changes”](#rebuild-on-storyblok-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Storyblok events.

##### Netlify

[Section titled “Netlify”](#netlify)

To set up a webhook in Netlify:

1. Go to your site dashboard and click on **Build & deploy**.

2. Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.

3. Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.

##### Vercel

[Section titled “Vercel”](#vercel)

To set up a webhook in Vercel:

1. Go to your project dashboard and click on **Settings**.

2. Under the **Git** tab, find the **Deploy Hooks** section.

3. Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.

##### Adding a webhook to Storyblok

[Section titled “Adding a webhook to Storyblok”](#adding-a-webhook-to-storyblok)

In your Storyblok space **Settings**, click on the **Webhooks** tab. Paste the webhook URL you copied in the **Story published & unpublished** field and hit `Save` to create a webhook.

Now, whenever you publish a new story, a new build will be triggered and your blog will be updated.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Storyblok Astro Integration](https://www.storyblok.com/mp/announcing-storyblok-astro) to add Storyblok to your project.
* [Storyblok Astro guide](https://www.storyblok.com/docs/guides/astro/)
* [Storyblok Astro package reference](https://www.storyblok.com/docs/packages/storyblok-astro)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Getting the Visual Editor to work for Storyblok + Astro](https://dev.to/sandrarodgers/getting-the-visual-editor-to-work-for-storyblok-astro-2gja) by Sandra Rodgers
* [Astro + Storyblok: SSR preview for instant visual editing](https://dev.to/jgierer12/astro-storyblok-ssr-preview-for-instant-visual-editing-3g9m) by Jonas Gierer
* [Astro-Storyblok Previews Site with Netlify’s Branch Deploys Feature](https://dev.to/sandrarodgers/astro-storyblok-previews-site-with-netlifys-branch-deploys-feature-44dh) by Sandra Rodgers

# Strapi & Astro

> Add content to your Astro project using Strapi Headless CMS

[Strapi](https://strapi.io/) is an open-source, customizable, headless CMS.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

This guide will build a wrapper function to connect Strapi with Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2. **A Strapi CMS server** - You can [set up a Strapi server on a local environment](https://docs.strapi.io/dev-docs/quick-start).

### Adding the Strapi URL in `.env`

[Section titled “Adding the Strapi URL in .env”](#adding-the-strapi-url-in-env)

To add your Strapi URL to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variable:

.env

```ini
STRAPI_URL="http://127.0.0.1:1337" # or use your IP address
```

Restart the dev server to use this environment variable in your Astro project.

If you would like to have IntelliSense for your environment variable, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly STRAPI_URL: string;
}
```

Your root directory should now include the new file(s):

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

Learn more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

### Creating the API wrapper

[Section titled “Creating the API wrapper”](#creating-the-api-wrapper)

Create a new file at `src/lib/strapi.ts` and add the following wrapper function to interact with the Strapi API:

src/lib/strapi.ts

```ts
interface Props {
  endpoint: string;
  query?: Record<string, string>;
  wrappedByKey?: string;
  wrappedByList?: boolean;
}


/**
 * Fetches data from the Strapi API
 * @param endpoint - The endpoint to fetch from
 * @param query - The query parameters to add to the url
 * @param wrappedByKey - The key to unwrap the response from
 * @param wrappedByList - If the response is a list, unwrap it
 * @returns
 */
export default async function fetchApi<T>({
  endpoint,
  query,
  wrappedByKey,
  wrappedByList,
}: Props): Promise<T> {
  if (endpoint.startsWith('/')) {
    endpoint = endpoint.slice(1);
  }


  const url = new URL(`${import.meta.env.STRAPI_URL}/api/${endpoint}`);


  if (query) {
    Object.entries(query).forEach(([key, value]) => {
      url.searchParams.append(key, value);
    });
  }
  const res = await fetch(url.toString());
  let data = await res.json();


  if (wrappedByKey) {
    data = data[wrappedByKey];
  }


  if (wrappedByList) {
    data = data[0];
  }


  return data as T;
}
```

This function requires an object with the following properties:

1. `endpoint` - The endpoint you are fetching.
2. `query` - The query parameters to add to the end of URL
3. `wrappedByKey` - The `data` key in the object that wraps your `Response`.
4. `wrappedByList` - A parameter to “unwrap” the list returned by Strapi, and return only the first item.

### Optional: Creating the Article interface

[Section titled “Optional: Creating the Article interface”](#optional-creating-the-article-interface)

If you are using TypeScript, create the following Article interface to correspond to the Strapi content types at `src/interfaces/article.ts`:

src/interfaces/article.ts

```ts
export default interface Article {
  documentId: number;
  title: string;
  description: string;
  content: string;
  slug: string;
  createdAt: string;
  updatedAt: string;
  publishedAt: string;
}
```

Note

You can modify this interface, or create multiple interfaces, to correspond to your own project data.

* src/

  * interfaces/

    * **article.ts**

  * lib/

    * strapi.ts

  * env.d.ts

* .env

* astro.config.mjs

* package.json

### Displaying a list of articles

[Section titled “Displaying a list of articles”](#displaying-a-list-of-articles)

1. Update your home page `src/pages/index.astro` to display a list of blog posts, each with a description and a link to its own page.

2. Import the wrapper function and the interface. Add the following API call to fetch your articles and return a list:

   src/pages/index.astro

   ```astro
   ---
   import fetchApi from '../lib/strapi';
   import type Article from '../interfaces/article';


   const articles = await fetchApi<Article[]>({
     endpoint: 'articles', // the content type to fetch
     wrappedByKey: 'data', // the key to unwrap the response
   });
   ---
   ```

   The API call requests data from `http://localhost:1337/api/articles` and returns `articles`: an array of json objects representing your data:

   ```json
   [
     {
       documentId: 1,
       title: "What's inside a Black Hole",
       description: "Maybe the answer is in this article, or not...",
       content: "Well, we don't know yet...",
       slug: "what-s-inside-a-black-hole",
       createdAt: "2023-05-28T13:19:46.421Z",
       updatedAt: "2023-05-28T13:19:46.421Z",
       publishedAt: "2023-05-28T13:19:45.826Z"
     },
     // ...
   ]
   ```

3. Using data from the `articles` array returned by the API, display your Strapi blog posts in a list. These posts will link to their own individual pages, which you will create in the next step.

   src/pages/index.astro

   ```astro
   ---
   import fetchApi from '../lib/strapi';
   import type Article from '../interfaces/article';


   const articles = await fetchApi<Article[]>({
     endpoint: 'articles?populate=image',
     wrappedByKey: 'data',
   });
   ---


   <!DOCTYPE html>
   <html lang="en">
     <head>
       <title>Strapi & Astro</title>
     </head>


     <body>
       <main>
         <ul>
           {
             articles.map((article) => (
               <li>
                 <a href={`/blog/${article.slug}/`}>
                   {article.title}
                 </a>
               </li>
             ))
           }
         </ul>
       </main>
     </body>
   </html>
   ```

### Generating article pages

[Section titled “Generating article pages”](#generating-article-pages)

Create the file `src/pages/blog/[slug].astro` to [dynamically generate a page](/en/guides/routing/#dynamic-routes) for each article.

* src/

  * interfaces/

    * article.ts

  * lib/

    * strapi.ts

  * pages/

    * index.astro

    * blog/

      * **\[slug].astro**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

In Astro’s default static mode (SSG), use [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) to fetch your list of articles from Strapi.

src/pages/blog/\[slug].astro

```astro
---
import fetchApi from '../../lib/strapi';
import type Article from '../../interfaces/article';


export async function getStaticPaths() {
  const articles = await fetchApi<Article[]>({
    endpoint: 'articles',
    wrappedByKey: 'data',
  });


  return articles.map((article) => ({
    params: { slug: article.slug },
    props: article,
  }));
}
type Props = Article;


const article = Astro.props;
---
```

Create the template for each page using the properties of each post object.

src/pages/blog/\[slug].astro

```diff
---
import fetchApi from '../../lib/strapi';
import type Article from '../../interfaces/article';


export async function getStaticPaths() {
  const articles = await fetchApi<Article[]>({
    endpoint: 'articles',
    wrappedByKey: 'data',
  });


  return articles.map((article) => ({
    params: { slug: article.slug },
    props: article,
  }));
}
type Props = Article;


const article = Astro.props;
---


+<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{article.title}</title>
  </head>


  <body>
    <main>
      <img src={import.meta.env.STRAPI_URL + article.image.data.url} />


      <h1>{article.title}</h1>


      +<!-- Render plain text -->
      <p>{article.content}</p>
      +<!-- Render markdown -->
      +<MyMarkdownComponent>
        +{article.content}
      +</MyMarkdownComponent>
      +<!-- Render html -->
      +<Fragment set:html={article.content} />
    </main>
  </body>
</html>
```

Tip

Make sure to choose the right rendering for your content. For markdown check out our [markdown guide](/en/guides/markdown-content/). If you are rendering html refer to [this guide](/en/reference/directives-reference/#sethtml) for safety.

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If you’ve [opted into on-demand rendering with an adapter](/en/guides/on-demand-rendering/), [generate your dynamic routes](/en/guides/routing/#on-demand-dynamic-routes) using the following code:

Create the `src/pages/blog/[slug].astro` file:

src/pages/blog/\[slug].astro

```astro
---
import fetchApi from '../../../lib/strapi';
import type Article from '../../../interfaces/article';


const { slug } = Astro.params;


let article: Article;


try {
  article = await fetchApi<Article>({
    endpoint: 'articles',
    wrappedByKey: 'data',
    wrappedByList: true,
    query: {
      'filters[slug][$eq]': slug || '',
    },
  });
} catch (error) {
  return Astro.redirect('/404');
}
---


<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{article.title}</title>
  </head>


  <body>
    <main>
      <img src={import.meta.env.STRAPI_URL + article.image.data.url} />


      <h1>{article.title}</h1>


      <!-- Render plain text -->
      <p>{article.content}</p>
      <!-- Render markdown -->
      <MyMarkdownComponent>
        {article.content}
      </MyMarkdownComponent>
      <!-- Render html -->
      <Fragment set:html={article.content} />
    </main>
  </body>
</html>
```

This file will fetch and render the page data from Strapi that matches the dynamic `slug` parameter.

Since you are using a redirect to `/404`, create a 404 page in `src/pages`:

src/pages/404.astro

```astro
<html lang="en">
  <head>
    <title>Not found</title>
  </head>
  <body>
    <p>Sorry, this page does not exist.</p>
    <img src="https://http.cat/404" />
  </body>
</html>
```

If the article is not found, the user will be redirected to this 404 page and be greeted by a lovely cat.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on changes

[Section titled “Rebuild on changes”](#rebuild-on-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Strapi.

##### Netlify

[Section titled “Netlify”](#netlify)

To set up a webhook in Netlify:

1. Go to your site dashboard and click on **Build & deploy**.

2. Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.

3. Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.

##### Vercel

[Section titled “Vercel”](#vercel)

To set up a webhook in Vercel:

1. Go to your project dashboard and click on **Settings**.

2. Under the **Git** tab, find the **Deploy Hooks** section.

3. Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.

##### Adding a webhook to Strapi

[Section titled “Adding a webhook to Strapi”](#adding-a-webhook-to-strapi)

Follow [the Strapi webhooks guide](https://strapi.io/blog/webhooks) to create a webhook in your Strapi admin panel.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Strapi Blog Guide For React](https://strapi.io/blog/build-a-blog-with-next-react-js-strapi) by Strapi

# StudioCMS & Astro

> Build and manage content for your Astro project using StudioCMS, a headless CMS designed specifically for Astro.

[StudioCMS](https://studiocms.dev/) is a headless CMS for Astro, built with Astro, that provides a user-friendly and configurable dashboard for content management as well as a custom rendering system to display your Astro components.

## Official resources

[Section titled “Official resources”](#official-resources)

* [StudioCMS documentation](https://docs.studiocms.dev/)
* [StudioCMS GitHub repository](https://github.com/withstudiocms/studiocms)
* [StudioCMS Discord community](https://chat.studiocms.dev)

# Tina CMS & Astro

> Add content to your Astro project using Tina as a CMS

[Tina CMS](https://tina.io/) is a Git-backed headless content management system.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

To get started, you’ll need an existing Astro project.

1. Run the following command to install Tina into your Astro project.

   * npm

     ```shell
     npx @tinacms/cli@latest init
     ```

   * pnpm

     ```shell
     pnpm dlx @tinacms/cli@latest init
     ```

   * Yarn

     ```shell
     yarn dlx @tinacms/cli@latest init
     ```

   - When prompted for a Cloud ID, press `Enter` to skip. You’ll generate one later if you want to use Tina Cloud.
   - When prompted “What framework are you using”, choose **Other**.
   - When asked where public assets are stored, press `Enter`.

   After this has finished, you should now have a `.tina` folder in the root of your project and a generated `hello-world.md` file at `content/posts`.

2. Change the `dev` script in `package.json`:

   * npm

     package.json

     ```diff
     {
         "scripts": {
             -"dev": "astro dev",
             +"dev": "tinacms dev -c \"astro dev\""
         }
     }
     ```

   * pnpm

     package.json

     ```diff
     {
         "scripts": {
             -"dev": "astro dev",
             +"dev": "tinacms dev -c \"astro dev\""
         }
     }
     ```

   * Yarn

     package.json

     ```diff
     {
         "scripts": {
             -"dev": "astro dev",
             +"dev": "tinacms dev -c \"astro dev\""
         }
     }
     ```

3. TinaCMS is now set up in local mode. Test this by running the `dev` script, then navigating to `/admin/index.html#/collections/post`.

   Editing the “Hello, World!” post will update the `content/posts/hello-world.md` file in your project directory.

4. Set up your Tina collections by editing the `schema.collections` property in `.tina/config.ts`.

   For example, you can add a required “date posted” frontmatter property to our posts:

   .tina/config.ts

   ```diff
   import { defineConfig } from "tinacms";


   // Your hosting provider likely exposes this as an environment variable
   const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "main";


   export default defineConfig({
     branch,
     clientId: null, // Get this from tina.io
     token: null, // Get this from tina.io
     build: {
       outputFolder: "admin",
       publicFolder: "public",
     },
     media: {
       tina: {
         mediaRoot: "images",
         publicFolder: "public",
       },
     },
     schema: {
       collections: [
         {
           name: "posts",
           label: "Posts",
           path: "src/content/posts",
           format: 'mdx',
           fields: [
             {
               type: "string",
               name: "title",
               label: "Title",
               isTitle: true,
               required: true,
             },
   +          {
   +            type: "datetime",
   +            name: "posted",
   +            label: "Date Posted",
   +            required: true,
   +          },
             {
               type: "rich-text",
               name: "body",
               label: "Body",
               isBody: true,
             },
           ],
         },
       ],
     },
   });
   ```

   Learn more about Tina collections [in the Tina docs](https://tina.io/docs/reference/collections/).

5. In production, TinaCMS can commit changes directly to your GitHub repository. To set up TinaCMS for production, you can choose to use [Tina Cloud](https://tina.io/docs/tina-cloud/) or self-host the [Tina Data Layer](https://tina.io/docs/self-hosted/overview/). You can [read more about registering for Tina Cloud](https://app.tina.io/register) in the Tina Docs.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [TinaCMS Astro integration guide](https://tina.io/docs/frameworks/astro/).

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Astro Tina Starter with visual editing](https://github.com/dawaltconley/tina-astro) by Jeff See + Dylan Awalt-Conley
* [Astro Tina Starter with basic editing](https://github.com/tombennet/astro-tina-starter/tree/main) by Tom Bennet
* [Using Astro’s Image Optimization with Tina](https://joschua.io/posts/2023/08/16/how-to-use-astro-assets-with-tina-cms/)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/resume01.CAukhX1f_183P41.webp) Resume01](https://astro.build/themes/details/resume01/)
* [![](/_astro/qurno.Dxy77_Dt_vzmNt.webp) Qurno Blog](https://astro.build/themes/details/qurno-astro/)

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
```

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
```

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
```

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
```

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
```

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
```

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import { loadEnv } from "vite";


const { NODE_TLS_REJECT_UNAUTHORIZED } = loadEnv(process.env.NODE_ENV, process.cwd(), "");
process.env.NODE_TLS_REJECT_UNAUTHORIZED = NODE_TLS_REJECT_UNAUTHORIZED;
// https://astro.build/config
export default defineConfig({});
```

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

# Headless WordPress & Astro

> Add content to your Astro project using WordPress as a CMS

[WordPress](https://wordpress.org/) is a content management system that includes its own frontend, but can also be used as a headless CMS to provide content to your Astro project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

WordPress comes with a built-in [WordPress REST API](https://developer.wordpress.org/rest-api/) to connect your WordPress data to Astro. You can optionally install [WPGraphQL](https://wordpress.org/plugins/wp-graphql/) or [Gato GraphQL](https://wordpress.org/plugins/gatographql/) on your site to use GraphQL.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.
2. **A WordPress site** - Your site’s REST API is `[YOUR_SITE]/wp-json/wp/v2/` and is available by default with any WordPress site. It is also possible to [set up WordPress on a local environment](https://wordpress.org/support/article/installing-wordpress-on-your-own-computer/).

### Setting up Credentials

[Section titled “Setting up Credentials”](#setting-up-credentials)

Your WordPress REST API is available to external requests for data fetching without authentication by default. This does not allow users to modify your data or site settings and allows you to use your data in your Astro project without any credentials.

You may choose to [require authentication](https://developer.wordpress.org/rest-api/frequently-asked-questions/#require-authentication-for-all-requests) if necessary.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

Fetch your WordPress data through your site’s unique REST API URL and the route for your content. (For a blog, this will commonly be `posts`.) Then, you can render your data properties using Astro’s `set:html={}` directive.

For example, to display a list of post titles and their content:

src/pages/index.astro

```astro
---
const res = await fetch("https://[YOUR-SITE]/wp-json/wp/v2/posts");
const posts = await res.json();
---
<h1>Astro + WordPress 🚀</h1>
{
  posts.map((post) => (
      <h2 set:html={post.title.rendered} />
      <p set:html={post.content.rendered} />
  ))
}
```

The WordPress REST API includes [global parameters](https://developer.wordpress.org/rest-api/using-the-rest-api/global-parameters/) such as `_fields` and `_embed`.

A large quantity of data is available to you via this API, so you may wish to only fetch certain fields. You can restrict your response by adding the [`_fields`](https://developer.wordpress.org/rest-api/using-the-rest-api/global-parameters/#_fields) parameter to the API URL, for example: `[YOUR-SITE]/wp/v2/posts?_fields=author,id,excerpt,title,link`

The API can also return content related to your post, such as a link to the parent post, or to comments on the post. You can add the [`_embed`](https://developer.wordpress.org/rest-api/using-the-rest-api/global-parameters/#_embed) parameter to the API URL (e.g. `[YOUR-SITE]/wp/v2/posts?_embed`) to indicate to the server that the response should include these embedded resources.

## Building a blog with WordPress and Astro

[Section titled “Building a blog with WordPress and Astro”](#building-a-blog-with-wordpress-and-astro)

This example fetches data from the public WordPress API of <https://norian.studio/dinosaurs/>. This WordPress site stores information about individual dinosaurs under the `dinos` route, just as a blog would store individual blog posts under the `posts` route.

This example shows how to reproduce this site structure in Astro: an index page that lists dinosaurs with links to dynamically-generated individual dinosaur pages.

Note

To use [Custom Post Types (CPT)](https://learn.wordpress.org/lesson-plan/custom-post-types/) in your WordPress API (not just `post` and `page`), you will have to [configure them in your WordPress dashboard](https://stackoverflow.com/questions/48536646/how-can-i-get-data-from-custom-post-type-using-wp-rest-api) or [add REST API Support For Custom Content Types](https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-rest-api-support-for-custom-content-types/) in WordPress.

This example fetches data from a WordPress site whose content types have already been configured and exposed to the REST API.

### Displaying a list of WordPress posts

[Section titled “Displaying a list of WordPress posts”](#displaying-a-list-of-wordpress-posts)

The page `src/pages/index.astro` lists each dinosaur, with a description and link to its own page.

* src/

  * pages/

    * **index.astro**

    * dinos/

      * \[slug].astro

* astro.config.mjs

* package.json

Fetching via the API returns an object that includes the properties:

* `title.rendered` - Contains the HTML rendering of the title of the post.
* `content.rendered` - Contains the HTML rendering of the content of the post.
* `slug` - Contains the slug of the post. (This provides the link to the dynamically-generated individual dinosaur pages.)

/src/pages/index.astro

```astro
---
import Layout from "../layouts/Layout.astro";


let res = await fetch("https://norian.studio/wp-json/wp/v2/dinos");
let posts = await res.json();
---
<Layout title="Dinos!">
  <section>
    <h1>List of Dinosaurs</h1>
    {
      posts.map((post) => (
        <article>
          <h2>
            <a href={`/dinos/${post.slug}/`} set:html={post.title.rendered} />
          </h2>
          <Fragment set:html={post.content.rendered} />
        </article>
      ))
    }
  </section>
</Layout>
```

### Using the WordPress API to generate pages

[Section titled “Using the WordPress API to generate pages”](#using-the-wordpress-api-to-generate-pages)

The page `src/pages/dinos/[slug].astro` [dynamically generates a page](/en/guides/routing/#dynamic-routes) for each dinosaur.

/src/pages/dinos/\[slug].astro

```astro
---
import Layout from '../../layouts/Layout.astro';


const { slug } = Astro.params;


let res = await fetch(`https://norian.studio/wp-json/wp/v2/dinos?slug=${slug}`);
let [post] = await res.json();


// The getStaticPaths() is required for static Astro sites.
// If using SSR, you will not need this function.
export async function getStaticPaths() {
  let data = await fetch("https://norian.studio/wp-json/wp/v2/dinos");
  let posts = await data.json();


  return posts.map((post) => ({
    params: { slug: post.slug },
    props: { post: post },
  }));
}
---
<Layout title={post.title.rendered}>
  <article>
    <h1 set:html={post.title.rendered} />
    <Fragment set:html={post.content.rendered} />
  </article>
</Layout>
```

### Returning embedded resources

[Section titled “Returning embedded resources”](#returning-embedded-resources)

The `_embed` query parameter instructs the server to return related (embedded) resources.

src/pages/dinos/\[slug].astro

```astro
---
const { slug } = Astro.params;


let res = await fetch(`https://norian.studio/wp-json/wp/v2/dinos?slug=${slug}&_embed`);
let [post] = await res.json();
---
```

The `_embedded['wp:featuredmedia']['0'].media_details.sizes.medium.source_url` property is returned, and can be used to display the featured image on each dinosaur page. (Replace `medium` with your desired image size.)

/src/pages/dinos/\[slug].astro

```astro
<Layout title={post.title.rendered}>
  <article>
    <img src={post._embedded['wp:featuredmedia']['0'].media_details.sizes.medium.source_url} />
    <h1 set:html={post.title.rendered} />
    <Fragment set:html={post.content.rendered} />
  </article>
</Layout>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Building An Astro Website With WordPress As A Headless CMS](https://blog.openreplay.com/building-an-astro-website-with-wordpress-as-a-headless-cms/) by Chris Bongers.
* [Building with Astro x WordPress](https://www.youtube.com/watch?v=Jstqgklvfnc) on Ben Holmes’s stream.
* [Building a Headless WordPress Site with Astro](https://developers.wpengine.com/blog/building-a-headless-wordpress-site-with-astro) by Jeff Everhart.
* [Astro and WordPress as an API](https://darko.io/posts/wp-as-an-api/) by Darko Bozhinovski.

## Production Sites

[Section titled “Production Sites”](#production-sites)

The following sites use Astro + WordPress in production:

* [Dinos!](https://wc-dinos.netlify.app/) by Anindo Neel Dutta — [source code on GitHub](https://github.com/leen-neel/astro-wordpress)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/astro-wordpress-starter.DWg2-sU7_ZlvAh5.webp) Astro WordPress Starter](https://astro.build/themes/details/astro-wordpress-starter/)

## Community Resources

[Section titled “Community Resources”](#community-resources-1)

[Introduction to Astro + WordPress ](https://dev.to/bngmnn/leveraging-wordpress-as-a-headless-cms-for-your-astro-website-a-comprehensive-guide-a4d)

[Astro + WPGraphQL for more secure WordPress sites ](https://www.youtube.com/watch?v=fWxn-r83ygQ)

[Shattering Headless WordPress Build Times with Astro's Content Layer API ](https://andrewkepson.com/blog/headless-wordpress/build-time-astro-content-layer-api/)

[How to Set Up a Headless WordPress Site with Astro ](https://dev.to/mathiasahlgren/how-to-set-up-a-headless-wordpress-site-with-astro-3a2h)

[Build a static site with WordPress and Astro ](https://kinsta.com/blog/wordpress-astro/)

[Going Headless WordPress with Astro ](https://www.youtube.com/watch?v=MP2TR6Z_YTc)

[Leveraging WordPress as a Headless CMS for Your Astro Website: API Configuration & Data Fetching ](https://medium.com/@bangemann.dev/configure-wordpress-rest-api-setup-data-fetching-4af5161095f6)

[WordPress Headless with Astro - Installing Astro and Fetching posts with WP-GraphQL ](https://www.youtube.com/watch?v=2PSqABrME28)

[Make a Headless WordPress Site with Astro ](https://www.youtube.com/watch?v=54U7dVmhyxE)

[WPEngine Astro Headless WordPress Starter Demo ](https://www.youtube.com/watch?v=BcoxZZIfESI)

[Headless WordPress with Astro – Build a Simple Blog from Scratch with Tailwind CSS ](https://fullstackdigital.io/blog/headless-wordpress-with-astro-build-a-simple-blog/)

[Building an E-commerce Website with Headless WordPress and Astro ](https://shaxadd.medium.com/building-an-e-commerce-website-with-headless-wordpress-and-astro-2712d8c8b735)

[Building a Headless WordPress Site with Astro ](https://wpengine.com/builders/building-headless-wordpress-site-astro/)

[Building an Astro Website with WordPress as a Headless CMS ](https://blog.openreplay.com/building-an-astro-website-with-wordpress-as-a-headless-cms/)

Have a resource to share?

If you found (or made!) a helpful video or blog post about using headless WordPress with Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/wordpress.mdx)!

# Content collections

> Manage your content with type safety.

**Added in:** `astro@2.0.0`

**Content collections** are the best way to manage sets of content in any Astro project. Collections help to organize and query your documents, enable Intellisense and type checking in your editor, and provide automatic TypeScript type-safety for all of your content. Astro v5.0 introduced the Content Layer API for defining and querying content collections. This performant, scalable API provides built-in content loaders for your local collections. For remote content, you can use third-party and community-built loaders or create your own custom loader and pull in your data from any source.

Note

Projects may continue using the legacy Content Collections API introduced in Astro v2.0. However, we encourage you to [update any existing collections](/en/guides/upgrade-to/v5/#legacy-v20-content-collections-api) when you are able.

## What are Content Collections?

[Section titled “What are Content Collections?”](#what-are-content-collections)

You can define a **collection** from a set of data that is structurally similar. This can be a directory of blog posts, a JSON file of product items, or any data that represents multiple items of the same shape.

Collections stored locally in your project or on your filesystem can have entries of Markdown, MDX, Markdoc, YAML, TOML, or JSON files:

* src/

  * …

* **newsletter/** the “newsletter” collection

  * week-1.md a collection entry
  * week-2.md a collection entry
  * week-3.md a collection entry

* **authors/** the “author” collection

  * authors.json a single file containing all collection entries

With an appropriate collection loader, you can fetch remote data from any external source, such as a CMS, database, or headless payment system.

## TypeScript configuration for collections

[Section titled “TypeScript configuration for collections”](#typescript-configuration-for-collections)

Content collections rely on TypeScript to provide Zod validation, Intellisense and type checking in your editor. If you are not extending one of Astro’s `strict` or `strictest` TypeScript settings, you will need to ensure the following `compilerOptions` are set in your `tsconfig.json`:

tsconfig.json

```diff
{
  // Included with "astro/tsconfigs/strict" or "astro/tsconfigs/strictest"
  "extends": "astro/tsconfigs/base",
  "compilerOptions": {
    +"strictNullChecks": true, // add if using `base` template
    "allowJs": true // required, and included with all Astro templates
  }
}
```

## Defining Collections

[Section titled “Defining Collections”](#defining-collections)

Individual collections use `defineCollection()` to configure:

* a `loader` for a data source (required)
* a `schema` for type safety (optional, but highly recommended!)

### The collection config file

[Section titled “The collection config file”](#the-collection-config-file)

To define collections, you must create a `src/content.config.ts` file in your project (`.js` and `.mjs` extensions are also supported.) This is a special file that Astro will use to configure your content collections based on the following structure:

src/content.config.ts

```ts
// 1. Import utilities from `astro:content`
import { defineCollection, z } from 'astro:content';


// 2. Import loader(s)
import { glob, file } from 'astro/loaders';


// 3. Define your collection(s)
const blog = defineCollection({ /* ... */ });
const dogs = defineCollection({ /* ... */ });


// 4. Export a single `collections` object to register your collection(s)
export const collections = { blog, dogs };
```

### Defining the collection `loader`

[Section titled “Defining the collection loader”](#defining-the-collection-loader)

The Content Layer API allows you to fetch your content (whether stored locally in your project or remotely) and uses a `loader` property to retrieve your data.

#### Built-in loaders

[Section titled “Built-in loaders”](#built-in-loaders)

Astro provides [two built-in loader functions](/en/reference/content-loader-reference/#built-in-loaders) (`glob()` and `file()`) for fetching your local content, as well as access to the API to construct your own loader and fetch remote data.

The [`glob()` loader](/en/reference/content-loader-reference/#glob-loader) creates entries from directories of Markdown, MDX, Markdoc, JSON, YAML, or TOML files from anywhere on the filesystem. It accepts a `pattern` of entry files to match using glob patterns supported by [micromatch](https://github.com/micromatch/micromatch#matching-features), and a base file path of where your files are located. Each entry’s `id` will be automatically generated from its file name. Use this loader when you have one file per entry.

The [`file()` loader](/en/reference/content-loader-reference/#file-loader) creates multiple entries from a single local file. Each entry in the file must have a unique `id` key property. It accepts a `base` file path to your file and optionally a [`parser` function](#parser-function) for data files it cannot parse automatically. Use this loader when your data file can be parsed as an array of objects.

src/content.config.ts

```ts
import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders'; // Not available with legacy API


const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/data/blog" }),
  schema: /* ... */
});
const dogs = defineCollection({
  loader: file("src/data/dogs.json"),
  schema: /* ... */
});


const probes = defineCollection({
  // `loader` can accept an array of multiple patterns as well as string patterns
  // Load all markdown files in the space-probes directory, except for those that start with "voyager-"
  loader: glob({ pattern: ['*.md', '!voyager-*'], base: 'src/data/space-probes' }),
  schema: z.object({
    name: z.string(),
    type: z.enum(['Space Probe', 'Mars Rover', 'Comet Lander']),
    launch_date: z.date(),
    status: z.enum(['Active', 'Inactive', 'Decommissioned']),
    destination: z.string(),
    operator: z.string(),
    notable_discoveries: z.array(z.string()),
  }),
});


export const collections = { blog, dogs, probes };
```

##### `parser` function

[Section titled “parser function”](#parser-function)

The `file()` loader accepts a second argument that defines a `parser` function. This allows you to specify a custom parser (e.g. `csv-parse`) to create a collection from a file’s contents.

The `file()` loader will automatically detect and parse (based on their file extension) a single array of objects from JSON and YAML files, and will treat each top-level table as an independent entry in TOML files. Support for these file types is built-in, and there is no need for a `parser` unless you have a [nested JSON document](#nested-json-documents). To use other files, such as `.csv`, you will need to create a parser function.

The following example shows importing a CSV parser, then loading a `cats` collection into your project by passing both a file path and `parser` function to the `file()` loader:

src/content.config.ts

```typescript
import { defineCollection } from "astro:content";
import { file } from "astro/loaders";
import { parse as parseCsv } from "csv-parse/sync";


const cats = defineCollection({
  loader: file("src/data/cats.csv", { parser: (text) => parseCsv(text, { columns: true, skipEmptyLines: true })})
});
```

###### Nested `.json` documents

[Section titled “Nested .json documents”](#nested-json-documents)

The `parser` argument also allows you to load a single collection from a nested JSON document. For example, this JSON file contains multiple collections:

src/data/pets.json

```json
{"dogs": [{}], "cats": [{}]}
```

You can separate these collections by passing a custom `parser` to the `file()` loader for each collection:

src/content.config.ts

```typescript
const dogs = defineCollection({
  loader: file("src/data/pets.json", { parser: (text) => JSON.parse(text).dogs })
});
const cats = defineCollection({
  loader: file("src/data/pets.json", { parser: (text) => JSON.parse(text).cats })
});
```

#### Building a custom loader

[Section titled “Building a custom loader”](#building-a-custom-loader)

You can build a custom loader to fetch remote content from any data source, such as a CMS, a database, or an API endpoint.

Using a loader to fetch your data will automatically create a collection from your remote data. This gives you all the benefits of local collections, such as collection-specific API helpers such as `getCollection()` and `render()` to query and display your data, as well as schema validation.

Tip

Find community-built and third-party loaders in the [Astro integrations directory](https://astro.build/integrations/?search=\&categories%5B%5D=loaders).

##### Inline loaders

[Section titled “Inline loaders”](#inline-loaders)

You can define a loader inline, inside your collection, as an async function that returns an array of entries.

This is useful for loaders that don’t need to manually control how the data is loaded and stored. Whenever the loader is called, it will clear the store and reload all the entries.

src/content.config.ts

```ts
const countries = defineCollection({
  loader: async () => {
    const response = await fetch("https://restcountries.com/v3.1/all");
    const data = await response.json();
    // Must return an array of entries with an id property, or an object with IDs as keys and entries as values
    return data.map((country) => ({
      id: country.cca3,
      ...country,
    }));
  },
  schema: /* ... */
});
```

The returned entries are stored in the collection and can be queried using the `getCollection()` and `getEntry()` functions.

##### Loader objects

[Section titled “Loader objects”](#loader-objects)

For more control over the loading process, you can use the Content Loader API to create a loader object. For example, with access to the `load` method directly, you can create a loader that allows entries to be updated incrementally or clears the store only when necessary.

Similar to creating an Astro integration or Vite plugin, you can [distribute your loader as an NPM package](/en/reference/publish-to-npm/) that others can use in their projects.

See the full [Content Loader API](/en/reference/content-loader-reference/) and examples of how to build your own loader.

### Defining the collection schema

[Section titled “Defining the collection schema”](#defining-the-collection-schema)

Schemas enforce consistent frontmatter or entry data within a collection through Zod validation. A schema **guarantees** that this data exists in a predictable form when you need to reference or query it. If any file violates its collection schema, Astro will provide a helpful error to let you know.

Schemas also power Astro’s automatic TypeScript typings for your content. When you define a schema for your collection, Astro will automatically generate and apply a TypeScript interface to it. The result is full TypeScript support when you query your collection, including property autocompletion and type-checking.

Tip

In order for Astro to recognize a new or updated schema, you may need to restart the dev server or [sync the content layer](/en/reference/cli-reference/#astro-dev) (`s + enter`) to define the `astro:content` module.

Every frontmatter or data property of your collection entries must be defined using a Zod data type:

src/content.config.ts

```ts
import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders'; // Not available with legacy API


const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/data/blog" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
  })
});
const dogs = defineCollection({
  loader: file("src/data/dogs.json"),
  schema: z.object({
    id: z.string(),
    breed: z.string(),
    temperament: z.array(z.string()),
  }),
});


export const collections = { blog, dogs };
```

#### Defining datatypes with Zod

[Section titled “Defining datatypes with Zod”](#defining-datatypes-with-zod)

Astro uses [Zod](https://github.com/colinhacks/zod) to power its content schemas. With Zod, Astro is able to validate every file’s data within a collection *and* provide automatic TypeScript types when you go to query content from inside your project.

To use Zod in Astro, import the `z` utility from `"astro:content"`. This is a re-export of the Zod library, and it supports all of the features of Zod.

```ts
// Example: A cheatsheet of many common Zod datatypes
import { z, defineCollection } from 'astro:content';


defineCollection({
  schema: z.object({
    isDraft: z.boolean(),
    title: z.string(),
    sortOrder: z.number(),
    image: z.object({
      src: z.string(),
      alt: z.string(),
    }),
    author: z.string().default('Anonymous'),
    language: z.enum(['en', 'es']),
    tags: z.array(z.string()),
    footnote: z.string().optional(),


    // In YAML, dates written without quotes around them are interpreted as Date objects
    publishDate: z.date(), // e.g. 2024-09-17


    // Transform a date string (e.g. "2022-07-08") to a Date object
    updatedDate: z.string().transform((str) => new Date(str)),


    authorContact: z.string().email(),
    canonicalURL: z.string().url(),
  })
})
```

See [Zod’s README](https://github.com/colinhacks/zod) for complete documentation on how Zod works and what features are available.

##### Zod schema methods

[Section titled “Zod schema methods”](#zod-schema-methods)

All [Zod schema methods](https://zod.dev/?id=schema-methods) (e.g. `.parse()`, `.transform()`) are available, with some limitations. Notably, performing custom validation checks on images using `image().refine()` is unsupported.

#### Defining collection references

[Section titled “Defining collection references”](#defining-collection-references)

Collection entries can also “reference” other related entries.

With the [`reference()` function](/en/reference/modules/astro-content/#reference) from the Collections API, you can define a property in a collection schema as an entry from another collection. For example, you can require that every `space-shuttle` entry includes a `pilot` property which uses the `pilot` collection’s own schema for type checking, autocomplete, and validation.

A common example is a blog post that references reusable author profiles stored as JSON, or related post URLs stored in the same collection:

src/content.config.ts

```ts
import { defineCollection, reference, z } from 'astro:content';
import { glob } from 'astro/loaders';


const blog = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: "./src/data/blog" }),
  schema: z.object({
    title: z.string(),
    // Reference a single author from the `authors` collection by `id`
    author: reference('authors'),
    // Reference an array of related posts from the `blog` collection by `slug`
    relatedPosts: z.array(reference('blog')),
  })
});


const authors = defineCollection({
  loader: glob({ pattern: '**/[^_]*.json', base: "./src/data/authors" }),
  schema: z.object({
    name: z.string(),
    portfolio: z.string().url(),
  })
});


export const collections = { blog, authors };
```

This example blog post specifies the `id`s of related posts and the `id` of the post author:

src/data/blog/welcome.md

```yaml
---
title: "Welcome to my blog"
author: ben-holmes # references `src/data/authors/ben-holmes.json`
relatedPosts:
- about-me # references `src/data/blog/about-me.md`
- my-year-in-review # references `src/data/blog/my-year-in-review.md`
---
```

These references will be transformed into objects containing a `collection` key and an `id` key, allowing you to easily [query them in your templates](/en/guides/content-collections/#accessing-referenced-data).

### Defining custom IDs

[Section titled “Defining custom IDs”](#defining-custom-ids)

When using the `glob()` loader with Markdown, MDX, Markdoc, or JSON files, every content entry [`id`](/en/reference/modules/astro-content/#id) is automatically generated in an URL-friendly format based on the content filename. The `id` is used to query the entry directly from your collection. It is also useful when creating new pages and URLs from your content.

You can override an entry’s generated `id` by adding your own `slug` property to the file frontmatter or data object for JSON files. This is similar to the “permalink” feature of other web frameworks.

src/blog/1.md

```md
---
title: My Blog Post
slug: my-custom-id/supports/slashes
---
Your blog post content here.
```

src/categories/1.json

```json
{
  "title": "My Category",
  "slug": "my-custom-id/supports/slashes",
  "description": "Your category description here."
}
```

## Querying Collections

[Section titled “Querying Collections”](#querying-collections)

Astro provides helper functions to query a collection and return one (or more) content entries.

* [`getCollection()`](/en/reference/modules/astro-content/#getcollection) fetches an entire collection and returns an array of entries.
* [`getEntry()`](/en/reference/modules/astro-content/#getentry) fetches a single entry from a collection.

These return entries with a unique `id`, a `data` object with all defined properties, and will also return a `body` containing the raw, uncompiled body of a Markdown, MDX, or Markdoc document.

```js
import { getCollection, getEntry } from 'astro:content';


// Get all entries from a collection.
// Requires the name of the collection as an argument.
const allBlogPosts = await getCollection('blog');


// Get a single entry from a collection.
// Requires the name of the collection and `id`
const poodleData = await getEntry('dogs', 'poodle');
```

The sort order of generated collections is non-deterministic and platform-dependent. This means that if you are calling `getCollection()` and need your entries returned in a specific order (e.g. blog posts sorted by date), you must sort the collection entries yourself:

src/pages/blog.astro

```astro
---
import { getCollection } from 'astro:content';


const posts = (await getCollection('blog')).sort(
  (a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf(),
);
---
```

See the full list of properties returned by the [`CollectionEntry` type](/en/reference/modules/astro-content/#collectionentry).

### Using content in Astro templates

[Section titled “Using content in Astro templates”](#using-content-in-astro-templates)

After querying your collections, you can access each entry’s content directly inside of your Astro component template. For example, you can create a list of links to your blog posts, displaying information from your entry’s frontmatter using the `data` property.

src/pages/index.astro

```astro
---
import { getCollection } from 'astro:content';
const posts = await getCollection('blog');
---
<h1>My posts</h1>
<ul>
  {posts.map(post => (
    <li><a href={`/blog/${post.id}`}>{post.data.title}</a></li>
  ))}
</ul>
```

#### Rendering body content

[Section titled “Rendering body content”](#rendering-body-content)

Once queried, you can render Markdown and MDX entries to HTML using the [`render()`](/en/reference/modules/astro-content/#render) function property. Calling this function gives you access to rendered HTML content, including both a `<Content />` component and a list of all rendered headings.

src/pages/blog/post-1.astro

```astro
---
import { getEntry, render } from 'astro:content';


const entry = await getEntry('blog', 'post-1');
if (!entry) {
  // Handle Error, for example:
  throw new Error('Could not find blog post 1');
}
const { Content, headings } = await render(entry);
---
<p>Published on: {entry.data.published.toDateString()}</p>
<Content />
```

When working with MDX entries, you can also [pass your own components to `<Content />`](/en/guides/integrations-guide/mdx/#passing-components-to-mdx-content) to replace HTML elements with custom alternatives.

#### Passing content as props

[Section titled “Passing content as props”](#passing-content-as-props)

A component can also pass an entire collection entry as a prop.

You can use the [`CollectionEntry`](/en/reference/modules/astro-content/#collectionentry) utility to correctly type your component’s props using TypeScript. This utility takes a string argument that matches the name of your collection schema and will inherit all of the properties of that collection’s schema.

src/components/BlogCard.astro

```astro
---
import type { CollectionEntry } from 'astro:content';
interface Props {
  post: CollectionEntry<'blog'>;
}


// `post` will match your 'blog' collection schema type
const { post } = Astro.props;
---
```

### Filtering collection queries

[Section titled “Filtering collection queries”](#filtering-collection-queries)

`getCollection()` takes an optional “filter” callback that allows you to filter your query based on an entry’s `id` or `data` properties.

You can use this to filter by any content criteria you like. For example, you can filter by properties like `draft` to prevent any draft blog posts from publishing to your blog:

```js
// Example: Filter out content entries with `draft: true`
import { getCollection } from 'astro:content';
const publishedBlogEntries = await getCollection('blog', ({ data }) => {
  return data.draft !== true;
});
```

You can also create draft pages that are available when running the dev server, but not built in production:

```js
// Example: Filter out content entries with `draft: true` only when building for production
import { getCollection } from 'astro:content';
const blogEntries = await getCollection('blog', ({ data }) => {
  return import.meta.env.PROD ? data.draft !== true : true;
});
```

The filter argument also supports filtering by nested directories within a collection. Since the `id` includes the full nested path, you can filter by the start of each `id` to only return items from a specific nested directory:

```js
// Example: Filter entries by sub-directory in the collection
import { getCollection } from 'astro:content';
const englishDocsEntries = await getCollection('docs', ({ id }) => {
  return id.startsWith('en/');
});
```

### Accessing referenced data

[Section titled “Accessing referenced data”](#accessing-referenced-data)

Any [references defined in your schema](/en/guides/content-collections/#defining-collection-references) must be queried separately after first querying your collection entry. Since the [`reference()` function](/en/reference/modules/astro-content/#reference) transforms a reference to an object with `collection` and `id` as keys, you can use the `getEntry()` function to return a single referenced item, or `getEntries()` to retrieve multiple referenced entries from the returned `data` object.

src/pages/blog/welcome.astro

```astro
---
import { getEntry, getEntries } from 'astro:content';


const blogPost = await getEntry('blog', 'welcome');


// Resolve a singular reference (e.g. `{collection: "authors", id: "ben-holmes"}`)
const author = await getEntry(blogPost.data.author);
// Resolve an array of references
// (e.g. `[{collection: "blog", id: "about-me"}, {collection: "blog", id: "my-year-in-review"}]`)
const relatedPosts = await getEntries(blogPost.data.relatedPosts);
---


<h1>{blogPost.data.title}</h1>
<p>Author: {author.data.name}</p>


<!-- ... -->


<h2>You might also like:</h2>
{relatedPosts.map(post => (
  <a href={post.id}>{post.data.title}</a>
))}
```

## Generating Routes from Content

[Section titled “Generating Routes from Content”](#generating-routes-from-content)

Content collections are stored outside of the `src/pages/` directory. This means that no pages or routes are generated for your collection items by default.

You will need to manually create a new [dynamic route](/en/guides/routing/#dynamic-routes) if you want to generate HTML pages for each of your collection entries, such as individual blog posts. Your dynamic route will map the incoming request param (e.g. `Astro.params.slug` in `src/pages/blog/[...slug].astro`) to fetch the correct entry for each page.

The exact method for generating routes will depend on whether your pages are prerendered (default) or rendered on demand by a server.

### Building for static output (default)

[Section titled “Building for static output (default)”](#building-for-static-output-default)

If you are building a static website (Astro’s default behavior), use the [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) function to create multiple pages from a single page component (e.g. `src/pages/[slug]`) during your build.

Call `getCollection()` inside of `getStaticPaths()` to have your collection data available for building static routes. Then, create the individual URL paths using the `id` property of each content entry. Each page is passed the entire collection entry as a prop for [use in your page template](#using-content-in-astro-templates).

src/pages/posts/\[id].astro

```astro
---
import { getCollection, render } from 'astro:content';
// 1. Generate a new path for every collection entry
export async function getStaticPaths() {
  const posts = await getCollection('blog');
  return posts.map(post => ({
    params: { id: post.id },
    props: { post },
  }));
}
// 2. For your template, you can get the entry directly from the prop
const { post } = Astro.props;
const { Content } = await render(post);
---
<h1>{post.data.title}</h1>
<Content />
```

This will generate a page route for every entry in the `blog` collection. For example, an entry at `src/blog/hello-world.md` will have an `id` of `hello-world`, and therefore its final URL will be `/posts/hello-world/`.

Note

If your custom slugs contain the `/` character to produce URLs with multiple path segments, you must use a [rest parameter (e.g. `[...slug]`)](/en/guides/routing/#rest-parameters) in the `.astro` filename for this dynamic routing page.

### Building for server output (SSR)

[Section titled “Building for server output (SSR)”](#building-for-server-output-ssr)

If you are building a dynamic website (using Astro’s SSR support), you are not expected to generate any paths ahead of time during the build. Instead, your page should examine the request (using `Astro.request` or `Astro.params`) to find the `slug` on-demand, and then fetch it using [`getEntry()`](/en/reference/modules/astro-content/#getentry).

src/pages/posts/\[id].astro

```astro
---
import { getEntry, render } from "astro:content";
// 1. Get the slug from the incoming server request
const { id } = Astro.params;
if (id === undefined) {
  return Astro.redirect("/404");
}
// 2. Query for the entry directly using the request slug
const post = await getEntry("blog", id);
// 3. Redirect if the entry does not exist
if (post === undefined) {
  return Astro.redirect("/404");
}
// 4. Render the entry to HTML in the template
const { Content } = await render(post);
---
<h1>{post.data.title}</h1>
<Content />
```

Tip

Explore the `src/pages/` folder of the [blog tutorial demo code on GitHub](https://github.com/withastro/blog-tutorial-demo/tree/content-collections/src/pages) to see full examples of creating pages from your collections for blog features like a list of blog posts, tags pages, and more!

## Collection JSON Schemas

[Section titled “Collection JSON Schemas”](#collection-json-schemas)

**Added in:** `astro@4.13.0`

Astro auto-generates [JSON Schema](https://json-schema.org/) files for collections, which you can use in your editor to get IntelliSense and type-checking for data files.

A JSON Schema file is generated for each collection in your project and output to the `.astro/collections/` directory. For example, if you have two collections, one named `authors` and another named `posts`, Astro will generate `.astro/collections/authors.schema.json` and `.astro/collections/posts.schema.json`.

### Use JSON Schemas in JSON files

[Section titled “Use JSON Schemas in JSON files”](#use-json-schemas-in-json-files)

You can manually point to an Astro-generated schema by setting the `$schema` field in your JSON file. The value should be a relative file path from the data file to the schema. In the following example, a data file in `src/data/authors/` uses the schema generated for the `authors` collection:

src/data/authors/armand.json

```diff
{
  +"$schema": "../../../.astro/collections/authors.schema.json",
  "name": "Armand",
  "skills": ["Astro", "Starlight"]
}
```

#### Use a schema for a group of JSON files in VS Code

[Section titled “Use a schema for a group of JSON files in VS Code”](#use-a-schema-for-a-group-of-json-files-in-vs-code)

In VS Code, you can configure a schema to apply for all files in a collection using the [`json.schemas` setting](https://code.visualstudio.com/docs/languages/json#_json-schemas-and-settings). In the following example, all files in the `src/data/authors/` directory will use the schema generated for the `authors` collection:

```json
{
  "json.schemas": [
    {
      "fileMatch": ["/src/data/authors/**"],
      "url": "./.astro/collections/authors.schema.json"
    }
  ]
}
```

### Use schemas in YAML files in VS Code

[Section titled “Use schemas in YAML files in VS Code”](#use-schemas-in-yaml-files-in-vs-code)

In VS Code, you can add support for using JSON schemas in YAML files using the [Red Hat YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) extension. With this extension installed, you can reference a schema in a YAML file using a special comment syntax:

src/data/authors/armand.yml

```diff
+# yaml-language-server: $schema=../../../.astro/collections/authors.schema.json
name: Armand
skills:
  - Astro
  - Starlight
```

#### Use schemas for a group of YAML files in VS Code

[Section titled “Use schemas for a group of YAML files in VS Code”](#use-schemas-for-a-group-of-yaml-files-in-vs-code)

With the Red Hat YAML extension, you can configure a schema to apply for all YAML files in a collection using the `yaml.schemas` setting. In the following example, all YAML files in the `src/data/authors/` directory will use the schema generated for the `authors` collection:

```json
{
  "yaml.schemas": {
    "./.astro/collections/authors.schema.json": ["/src/content/authors/*.yml"]
  }
}
```

See [“Associating schemas”](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml#associating-schemas) in the Red Hat YAML extension documentation for more details.

## When to create a collection

[Section titled “When to create a collection”](#when-to-create-a-collection)

You can [create a collection](#defining-collections) any time you have a group of related data or content that shares a common structure.

Much of the benefit of using collections comes from:

* Defining a common data shape to validate that an individual entry is “correct” or “complete”, avoiding errors in production.
* Content-focused APIs designed to make querying intuitive (e.g. `getCollection()` instead of `import.meta.glob()`) when importing and rendering content on your pages.
* A [Content Loader API](/en/reference/content-loader-reference/) for retrieving your content that provides both built-in loaders and access to the low-level API. There are several third-party and community-built loaders available, and you can build your own custom loader to fetch data from anywhere.
* Performance and scalability. The Content Layer API allows data to be cached between builds and is suitable for tens of thousands of content entries.

[Define your data](#defining-collections) as a collection when:

* You have multiple files or data to organize that share the same overall structure (e.g. blog posts written in Markdown which all have the same frontmatter properties).
* You have existing content stored remotely, such as in a CMS, and want to take advantage of the collections helper functions and Content Layer API instead of using `fetch()` or SDKs.
* You need to fetch (tens of) thousands of related pieces of data, and need a querying and caching method that handles at scale.

### When not to create a collection

[Section titled “When not to create a collection”](#when-not-to-create-a-collection)

Collections provide excellent structure, safety, and organization when you have **multiple pieces of content that must share the same properties**.

Collections **may not be your solution** if:

* You have only one or a small number of different pages. Consider [making individual page components](/en/basics/astro-pages/) such as `src/pages/about.astro` with your content directly instead.
* You are displaying files that are not processed by Astro, such as PDFs. Place these static assets in the [`public/` directory](/en/basics/project-structure/#public) of your project instead.
* Your data source has its own SDK/client library for imports that is incompatible with or does not offer a content loader and you prefer to use it directly.
* You are using APIs that need to be updated in real time. Content collections are only updated at build time, so if you need live data, use other methods of [importing files](/en/guides/imports/#import-statements) or [fetching data](/en/guides/data-fetching/) with [on-demand rendering](/en/guides/on-demand-rendering/).

# Data fetching

> Learn how to fetch remote data with Astro using the fetch API.

`.astro` files can fetch remote data to help you generate your pages.

## `fetch()` in Astro

[Section titled “fetch() in Astro”](#fetch-in-astro)

All [Astro components](/en/basics/astro-components/) have access to the [global `fetch()` function](https://developer.mozilla.org/en-US/docs/Web/API/fetch) in their component script to make HTTP requests to APIs using the full URL (e.g. `https://example.com/api`). Additionally, you can construct a URL to your project’s pages and endpoints that are rendered on demand on the server using [`new URL("/api", Astro.url)`](/en/reference/api-reference/#url).

This fetch call will be executed at build time, and the data will be available to the component template for generating dynamic HTML. If [SSR](/en/guides/on-demand-rendering/) mode is enabled, any fetch calls will be executed at runtime.

💡 Take advantage of [**top-level `await`**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await#top_level_await) inside of your Astro component script.

💡 Pass fetched data to both Astro and framework components, as props.

src/components/User.astro

```astro
---
import Contact from "../components/Contact.jsx";
import Location from "../components/Location.astro";


const response = await fetch("https://randomuser.me/api/");
const data = await response.json();
const randomUser = data.results[0];
---
<!-- Data fetched at build can be rendered in HTML -->
<h1>User</h1>
<h2>{randomUser.name.first} {randomUser.name.last}</h2>


<!-- Data fetched at build can be passed to components as props -->
<Contact client:load email={randomUser.email} />
<Location city={randomUser.location.city} />
```

Note

Remember, all data in Astro components is fetched when a component is rendered.

Your deployed Astro site will fetch data **once, at build time**. In dev, you will see data fetches on component refreshes. If you need to re-fetch data multiple times client-side, use a [framework component](/en/guides/framework-components/) or a [client-side script](/en/guides/client-side-scripts/) in an Astro component.

## `fetch()` in Framework Components

[Section titled “fetch() in Framework Components”](#fetch-in-framework-components)

The `fetch()` function is also globally available to any [framework components](/en/guides/framework-components/):

src/components/Movies.tsx

```tsx
import type { FunctionalComponent } from 'preact';


const data = await fetch('https://example.com/movies.json').then((response) => response.json());


// Components that are build-time rendered also log to the CLI.
// When rendered with a `client:*` directive, they also log to the browser console.
console.log(data);


const Movies: FunctionalComponent = () => {
  // Output the result to the page
  return <div>{JSON.stringify(data)}</div>;
};


export default Movies;
```

## GraphQL queries

[Section titled “GraphQL queries”](#graphql-queries)

Astro can also use `fetch()` to query a GraphQL server with any valid GraphQL query.

src/components/Film.astro

```astro
---
const response = await fetch(
  "https://swapi-graphql.netlify.app/.netlify/functions/index",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query: `
        query getFilm ($id:ID!) {
          film(id: $id) {
            title
            releaseDate
          }
        }
      `,
      variables: {
        id: "ZmlsbXM6MQ==",
      },
    }),
  }
);




const json = await response.json();
const { film } = json.data;
---
<h1>Fetching information about Star Wars: A New Hope</h1>
<h2>Title: {film.title}</h2>
<p>Year: {film.releaseDate}</p>
```

## Fetch from a Headless CMS

[Section titled “Fetch from a Headless CMS”](#fetch-from-a-headless-cms)

Astro components can fetch data from your favorite CMS and then render it as your page content. Using [dynamic routes](/en/guides/routing/#dynamic-routes), components can even generate pages based on your CMS content.

See our [CMS Guides](/en/guides/cms/) for full details on integrating Astro with headless CMSes including Storyblok, Contentful, and WordPress.

## Community resources

[Section titled “Community resources”](#community-resources)

* [Creating a fullstack app with Astro + GraphQL](https://robkendal.co.uk/blog/how-to-build-astro-site-with-graphql/)

# Deploy your Astro Site

> How to deploy your Astro site to the web.

**Ready to build and deploy your Astro site?** Follow one of our guides to different deployment services or scroll down for general guidance about deploying an Astro site.

## Deployment Guides

[Section titled “Deployment Guides”](#deployment-guides)

* ![](/logos/netlify.svg)

  ### [Netlify](/en/guides/deploy/netlify/)

  On demand Static

* ![](/logos/vercel.svg)

  ### [Vercel](/en/guides/deploy/vercel/)

  On demand Static

* ![](/logos/deno.svg)

  ### [Deno Deploy](/en/guides/deploy/deno/)

  On demand Static

* ![](/logos/github.svg)

  ### [GitHub Pages](/en/guides/deploy/github/)

  Static

* ![](/logos/gitlab.svg)

  ### [GitLab Pages](/en/guides/deploy/gitlab/)

  Static

* ![](/logos/cloudflare-pages.svg)

  ### [Cloudflare Pages](/en/guides/deploy/cloudflare/)

  On demand Static

* ![](/logos/aws.svg)

  ### [AWS](/en/guides/deploy/aws/)

  On demand Static

* ![](/logos/flightcontrol.svg)

  ### [AWS via Flightcontrol](/en/guides/deploy/flightcontrol/)

  On demand Static

* ![](/logos/sst.svg)

  ### [AWS via SST](/en/guides/deploy/sst/)

  On demand Static

* ![](/logos/clever-cloud.svg)

  ### [Clever Cloud](/en/guides/deploy/clever-cloud/)

  On demand Static

* ![](/logos/azion.svg)

  ### [Azion](/en/guides/deploy/azion/)

  On demand Static

* ![](/logos/google-cloud.svg)

  ### [Google Cloud](/en/guides/deploy/google-cloud/)

  On demand Static

* ![](/logos/firebase.svg)

  ### [Google Firebase](/en/guides/deploy/google-firebase/)

  On demand Static

* ![](/logos/heroku.svg)

  ### [Heroku](/en/guides/deploy/heroku/)

  Static

* ![](/logos/microsoft-azure.svg)

  ### [Microsoft Azure](/en/guides/deploy/microsoft-azure/)

  Static

* ![](/logos/buddy.svg)

  ### [Buddy](/en/guides/deploy/buddy/)

  Static

* ![](/logos/deployhq.svg)

  ### [DeployHQ](/en/guides/deploy/deployhq/)

  Static

* ![](/logos/fleek.svg)

  ### [Fleek](/en/guides/deploy/fleek/)

  Static

* ![](/logos/flyio.svg)

  ### [Fly.io](/en/guides/deploy/flyio/)

  On demand Static

* ![](/logos/railway.svg)

  ### [Railway](/en/guides/deploy/railway/)

  On demand Static

* ![](/logos/render.svg)

  ### [Render](/en/guides/deploy/render/)

  Static

* ![](/logos/stormkit.svg)

  ### [Stormkit](/en/guides/deploy/stormkit/)

  Static

* ![](/logos/surge.svg)

  ### [Surge](/en/guides/deploy/surge/)

  Static

* ![](/logos/cleavr.svg)

  ### [Cleavr](/en/guides/deploy/cleavr/)

  On demand Static

* ![](/logos/kinsta.svg)

  ### [Kinsta](/en/guides/deploy/kinsta/)

  On demand Static

* ![](/logos/zeabur.svg)

  ### [Zeabur](/en/guides/deploy/zeabur/)

  On demand Static

* ![](/logos/zerops.svg)

  ### [Zerops](/en/guides/deploy/zerops/)

  On demand Static

* ![](/logos/cloudray.svg)

  ### [CloudRay](/en/guides/deploy/cloudray/)

  Static

* ![](/logos/seenode.svg)

  ### [Seenode](/en/guides/deploy/seenode/)

  On demand

* ![](/logos/zephyr.svg)

  ### [Zephyr](/en/guides/deploy/zephyr/)

  Static

## Quick Deploy Options

[Section titled “Quick Deploy Options”](#quick-deploy-options)

You can build and deploy an Astro site to a number of hosts quickly using either their website’s dashboard UI or a CLI.

### Website UI

[Section titled “Website UI”](#website-ui)

A quick way to deploy your website is to connect your Astro project’s online Git repository (e.g. GitHub, GitLab, Bitbucket) to a host provider and take advantage of continuous deployment using Git.

These host platforms automatically detect pushes to your Astro project’s source repository, build your site and deploy it to the web at a custom URL or your personal domain. Often, setting up a deployment on these platforms will follow steps something like the following:

1. Add your repository to an online Git provider (e.g. in GitHub, GitLab, Bitbucket)

2. Choose a host that supports **continuous deployment** (e.g. [Netlify](/en/guides/deploy/netlify/) or [Vercel](/en/guides/deploy/vercel/)) and import your Git repository as a new site/project.

   Many common hosts will recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy your site as shown below. (If not, these settings can be changed.)

   Deploy settings

   * **Build Command:** `astro build` or `npm run build`
   * **Publish directory:** `dist`

3. Click “Deploy” and your new website will be created at a unique URL for that host (e.g. `new-astro-site.netlify.app`).

The host will be automatically configured to watch your Git provider’s main branch for changes, and to rebuild and republish your site at each new commit. These settings can typically be configured in your host provider’s dashboard UI.

### CLI Deployment

[Section titled “CLI Deployment”](#cli-deployment)

Some hosts will have their own command line interface (CLI) you can install globally to your machine using npm. Often, using a CLI to deploy looks something like the following:

1. Install your host’s CLI globally, for example:

   * npm

     ```shell
     npm install --global netlify-cli
     ```

   * pnpm

     ```shell
     pnpm add --global netlify-cli
     ```

   * Yarn

     ```shell
     yarn global add netlify-cli
     ```

2. Run the CLI and follow any instructions for authorization, setup etc.

3. Build your site and deploy to your host

   Many common hosts will build and deploy your site for you. They will usually recognize your project as an Astro site, and should choose the appropriate configuration settings to build and deploy as shown below. (If not, these settings can be changed.)

   Deploy settings

   * **Build Command:** `astro build` or `npm run build`
   * **Publish directory:** `dist`

   Other hosts will require you to [build your site locally](#building-your-site-locally) and deploy using the command line.

## Building Your Site Locally

[Section titled “Building Your Site Locally”](#building-your-site-locally)

Many hosts like Netlify and Vercel will build your site for you and then publish that build output to the web. But, some sites will require you to build locally and then run a deploy command or upload your build output.

You may also wish to build locally to preview your site, or to catch any potential errors and warnings in your own environment.

Run the command `npm run build` to build your Astro site.

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

By default, the build output will be placed at `dist/`. This location can be changed using the [`outDir` configuration option](/en/reference/configuration-reference/#outdir).

## Adding an Adapter for on-demand rendering

[Section titled “Adding an Adapter for on-demand rendering”](#adding-an-adapter-for-on-demand-rendering)

Note

Before deploying your Astro site with [on-demand rendering](/en/guides/on-demand-rendering/) enabled, make sure you have:

* Installed the [appropriate adapter](/en/guides/on-demand-rendering/) to your project dependencies (either manually, or using the adapter’s `astro add` command, e.g. `npx astro add netlify`).
* [Added the adapter](/en/reference/configuration-reference/#integrations) to your `astro.config.mjs` file’s import and default export when installing manually. (The `astro add` command will take care of this step for you!)

# Deploy your Astro Site to AWS

> How to deploy your Astro site to the web using AWS.

[AWS](https://aws.amazon.com/) is a full-featured web app hosting platform that can be used to deploy an Astro site.

Deploying your project to AWS requires using the [AWS console](https://aws.amazon.com/console/). (Most of these actions can also be done using the [AWS CLI](https://aws.amazon.com/cli/)). This guide will walk you through the steps to deploy your site to AWS using [AWS Amplify](https://aws.amazon.com/amplify/), [S3 static website hosting](https://aws.amazon.com/s3/), and [CloudFront](https://aws.amazon.com/cloudfront/).

## AWS Amplify

[Section titled “AWS Amplify”](#aws-amplify)

AWS Amplify is a set of purpose-built tools and features that lets frontend web and mobile developers quickly and easily build full-stack applications on AWS. You can either deploy your Astro project as a static site, or as a server-rendered site.

### Static Site

[Section titled “Static Site”](#static-site)

Your Astro project is a static site by default.

1. Create a new Amplify Hosting project.

2. Connect your repository to Amplify.

3. Modify your build settings to match your project’s build process.

   * npm

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - npm ci
         build:
           commands:
             - npm run build
       artifacts:
         baseDirectory: /dist
         files:
           - '**/*'
       cache:
         paths:
           - node_modules/**/*
     ```

   * pnpm

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - npm i -g pnpm
             - pnpm config set store-dir .pnpm-store
             - pnpm i
         build:
           commands:
             - pnpm run build
       artifacts:
         baseDirectory: /dist
         files:
           - '**/*'
       cache:
         paths:
           - .pnpm-store/**/*
     ```

   * Yarn

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - yarn install
         build:
           commands:
             - yarn build
       artifacts:
         baseDirectory: /dist
         files:
           - '**/*'
       cache:
         paths:
           - node_modules/**/*
     ```

Amplify will automatically deploy your website and update it when you push a commit to your repository.

### Adapter for on-demand rendering

[Section titled “Adapter for on-demand rendering”](#adapter-for-on-demand-rendering)

In order to deploy your project as a server-rendered site, you will need to use the third-party, [community-maintained AWS Amplify adapter](https://github.com/alexnguyennz/astro-aws-amplify) and make some changes to your config.

First, install the Amplify adapter.

* npm

  ```shell
  npm install astro-aws-amplify
  ```

* pnpm

  ```shell
  pnpm add astro-aws-amplify
  ```

* Yarn

  ```shell
  yarn add astro-aws-amplify
  ```

Then, in your `astro.config.*` file, add the adapter and set the output to `server`.

astro.config.mjs

```diff
import { defineConfig } from 'astro/config';
+import awsAmplify from 'astro-aws-amplify';


export default defineConfig({
  // ...
+  output: "server",
+  adapter: awsAmplify(),
});
```

Once the adapter has been installed, you can set up your Amplify project.

1. Create a new Amplify Hosting project.

2. Connect your repository to Amplify.

3. Modify your build settings to match the adapter’s build process by either editing the build settings in the AWS console, or by adding an `amplify.yaml` in the root of your project.

   * npm

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - npm ci --cache .npm --prefer-offline
         build:
           commands:
             - npm run build
             - mv node_modules ./.amplify-hosting/compute/default
       artifacts:
         baseDirectory: .amplify-hosting
         files:
           - '**/*'
       cache:
         paths:
           - .npm/**/*
     ```

   * pnpm

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - npm i -g pnpm
             - pnpm config set store-dir .pnpm-store
             - pnpm i
         build:
           commands:
             - pnpm run build
             - mv node_modules ./.amplify-hosting/compute/default
       artifacts:
         baseDirectory: .amplify-hosting
         files:
           - '**/*'
       cache:
         paths:
           - .pnpm-store/**/*
     ```

   * Yarn

     ```yaml
     version: 1
     frontend:
       phases:
         preBuild:
           commands:
             - yarn install
         build:
           commands:
             - yarn build
             - mv node_modules ./.amplify-hosting/compute/default
       artifacts:
         baseDirectory: .amplify-hosting
         files:
           - '**/*'
       cache:
         paths:
           - node_modules/**/*
     ```

Amplify will automatically deploy your website and update it when you push a commit to your repository.

See [AWS’s Astro deployment guide](https://docs.aws.amazon.com/amplify/latest/userguide/get-started-astro.html) for more info.

## S3 static website hosting

[Section titled “S3 static website hosting”](#s3-static-website-hosting)

S3 is the starting point of any application. It is where your project files and other assets are stored. S3 charges for file storage and number of requests. You can find more information about S3 in the [AWS documentation](https://aws.amazon.com/s3/).

1. Create an S3 bucket with your project’s name.

   Tip

   The bucket name should be globally unique. We recommend a combination of your project name and the domain name of your site.

2. Disable **“Block all public access”**. By default, AWS sets all buckets to be private. To make it public, you need to uncheck the “Block public access” checkbox in the bucket’s properties.

3. Upload your built files located in `dist` to S3. You can do this manually in the console or use the AWS CLI. If you use the AWS CLI, use the following command after [authenticating with your AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html):

   ```plaintext
   aws s3 cp dist/ s3://<BUCKET_NAME>/ --recursive
   ```

4. Update your bucket policy to allow public access. You can find this setting in the bucket’s **Permissions > Bucket policy**.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::<BUCKET_NAME>/*"
       }
     ]
   }
   ```

   Caution

   Do not forget to replace `<BUCKET_NAME>` with the name of your bucket.

5. Enable website hosting for your bucket. You can find this setting in the bucket’s **Properties > Static website hosting**. Set your index document to `index.html` and your error document to `404.html`. Finally, you can find your new website URL in the bucket’s **Properties > Static website hosting**.

   Note

   If you are deploying a single-page application (SPA), set your error document to `index.html`.

## S3 with CloudFront

[Section titled “S3 with CloudFront”](#s3-with-cloudfront)

CloudFront is a web service that provides content delivery network (CDN) capabilities. It is used to cache content of a web server and distribute it to end users. CloudFront charges for the amount of data transferred. Adding CloudFront to your S3 bucket is more cost-effective and provides a faster delivery.

To connect S3 with CloudFront, create a CloudFront distribution with the following values:

* **Origin domain:** Your S3 bucket static website endpoint. You can find your endpoint in your S3 bucket’s **Properties > Static website hosting**. Alternative, you can select your s3 bucket and click on the callout to replace your bucket address with your bucket static endpoint.
* **Viewer protocol policy:** “Redirect to HTTPS”

This configuration will serve your site using the CloudFront CDN network. You can find your CloudFront distribution URL in the bucket’s **Distributions > Domain name**.

Note

When connecting CloudFront to an S3 static website endpoint, you rely on S3 bucket policies for access control. See [S3 static website hosting](#s3-static-website-hosting) section for more information about bucket policies.

## Continuous deployment with GitHub Actions

[Section titled “Continuous deployment with GitHub Actions”](#continuous-deployment-with-github-actions)

There are many ways to set up continuous deployment for AWS. One possibility for code hosted on GitHub is to use [GitHub Actions](https://github.com/features/actions) to deploy your website every time you push a commit.

1. Create a new policy in your AWS account using [IAM](https://aws.amazon.com/iam/) with the following permissions. This policy will allow you to upload built files to your S3 bucket and invalidate the CloudFront distribution files when you push a commit.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
         {
             "Sid": "VisualEditor0",
             "Effect": "Allow",
             "Action": [
                 "s3:PutObject",
                 "s3:ListBucket",
                 "s3:DeleteObject",
                 "cloudfront:CreateInvalidation"
             ],
             "Resource": [
                 "<DISTRIBUTION_ARN>",
                 "arn:aws:s3:::<BUCKET_NAME>/*",
                 "arn:aws:s3:::<BUCKET_NAME>"
             ]
         }
     ]
   }
   ```

   Caution

   Do not forget to replace `<DISTRIBUTION_ARN>` and `<BUCKET_NAME>`. You can find the DISTRIBUTION\_ARN in **CloudFront > Distributions > Details**.

2. Create a new IAM user and attach the policy to the user. This will provide your `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID`.

3. Add this sample workflow to your repository at `.github/workflows/deploy.yml` and push it to GitHub. You will need to add `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `BUCKET_ID`, and `DISTRIBUTION_ID` as “secrets” to your repository on GitHub under **Settings** > **Secrets** > **Actions**. Click `New repository secret` to add each one.

   ```yaml
   name: Deploy Website


   on:
     push:
       branches:
         - main


   jobs:
     deploy:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v4
         - name: Configure AWS Credentials
           uses: aws-actions/configure-aws-credentials@v1
           with:
             aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
             aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
             aws-region: us-east-1
         - name: Install modules
           run: npm ci
         - name: Build application
           run: npm run build
         - name: Deploy to S3
           run: aws s3 sync --delete ./dist/ s3://${{ secrets.BUCKET_ID }}
         - name: Create CloudFront invalidation
           run: aws cloudfront create-invalidation --distribution-id ${{ secrets.DISTRIBUTION_ID }} --paths "/*"
   ```

   Note

   Your `BUCKET_ID` is the name of your S3 bucket. Your `DISTRIBUTION_ID` is your CloudFront distribution ID. You can find your CloudFront distribution ID in **CloudFront > Distributions > ID**

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Deploy Astro to AWS Amplify](https://www.launchfa.st/blog/deploy-astro-aws-amplify)
* [Deploy Astro to AWS Elastic Beanstalk](https://www.launchfa.st/blog/deploy-astro-aws-elastic-beanstalk)
* [Deploy Astro to Amazon ECS on AWS Fargate](https://www.launchfa.st/blog/deploy-astro-aws-fargate)
* [Troubleshooting SSR Amplify Deployments](https://docs.aws.amazon.com/amplify/latest/userguide/troubleshooting-ssr-deployment.html)

# Deploy your Astro Site to Azion

> How to deploy your Astro site to the web using Azion.

You can deploy your Astro project on [Azion](https://console.azion.com/), a platform for frontend developers to collaborate and deploy static (JAMstack) and SSR websites.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* An [Azion account](https://www.azion.com/). If you don’t have one, you can sign up for a free account.
* Your app code stored in a [GitHub](https://github.com/) repository.
* [Azion CLI](https://www.azion.com/en/documentation/products/azion-cli/overview/) installed for faster project setup and deployment.

## How to Deploy through Azion Console Dashboard

[Section titled “How to Deploy through Azion Console Dashboard”](#how-to-deploy-through-azion-console-dashboard)

To start building, follow these steps:

1. Access [Azion Console](https://console.azion.com).

2. On the homepage, click the **+ Create** button.
   * This opens a modal with the options to create new applications and resources.

3. Select the **Import from GitHub** option and click the card.
   * This action opens the settings page.

4. Connect your Azion account with GitHub.
   * A pop-up window will appear asking for authorization.

5. Select the repository you want to import from GitHub.

6. Configure the build settings:

   * **Framework preset:** Select the appropriate framework (e.g., `Astro`).
   * **Root Directory:** This refers to the directory in which your code is located. Your code must be located at the root directory, not a subdirectory. A ./ symbol appears in this field, indicating it’s a root directory.
   * **Install Command:** the command that compiles your settings to build for production. Build commands are executed through scripts. For example: npm run build or npm install for an NPM package.

7. Click **Save and Deploy**.

8. Monitor the deployment using **Azion Real-Time Metrics** and verify your site is live on the edge.

## How to Deploy a Static Site Using the Azion CLI

[Section titled “How to Deploy a Static Site Using the Azion CLI”](#how-to-deploy-a-static-site-using-the-azion-cli)

1. **Install the Azion CLI:**

   * Download and install the [Azion CLI](https://www.azion.com/en/documentation/products/azion-cli/overview/) for easier management and deployment.

   Caution

   The Azion CLI does not currently support native Windows environments. However, you can use it on Windows through the Windows Subsystem for Linux (WSL). Follow the [WSL installation guide](https://docs.microsoft.com/en-us/windows/wsl/install) to set up a Linux environment on your Windows machine.

2. **Authenticate the CLI:**

   * Run the following command to authenticate your CLI with your Azion account.

   ```bash
   azion login
   ```

3. **Set Up Your Application:**

   * Use the following commands to initialize and configure your project:

   ```bash
   azion init
   ```

4. **Build Your Astro Project:**

   * Run your build command locally:

   ```bash
   azion build
   ```

5. **Deploy Your Static Files:**

   * Deploy your static files using the Azion CLI:

   ```bash
   azion deploy
   ```

This guide provides an overview of deploying static applications.

## Enabling Local Development Using Azion CLI

[Section titled “Enabling Local Development Using Azion CLI”](#enabling-local-development-using-azion-cli)

For the preview to work, you must execute the following command:

```bash
azion dev
```

Once you’ve initialized the local development server, the application goes through the `build` process.

```bash
Building your Edge Application. This process may take a few minutes
Running build step command:
...
```

Then, when the build is complete, the access to the application is prompted:

```bash
[Azion Bundler] [Server] › ✔  success   Function running on port http://localhost:3000
```

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### Node.js runtime APIs

[Section titled “Node.js runtime APIs”](#nodejs-runtime-apis)

A project using an NPM package fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

This means that a package or import you are using is not compatible with Azion’s runtime APIs.

If you are directly importing a Node.js runtime API, please refer to the [Azion Node.js compatibility](https://www.azion.com/en/documentation/products/azion-edge-runtime/compatibility/node/) for further steps on how to resolve this.

If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.

# Deploy your Astro Site with Buddy

> How to deploy your Astro site to the web using Buddy.

You can deploy your Astro project using [Buddy](https://buddy.works/), a CI/CD solution that can build your site and push it to many different deploy targets including FTP servers and cloud hosting providers.

Note

Buddy itself will not host your site. Instead, it helps you manage the build process and deliver the result to a deploy platform of your choice.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. [Create a **Buddy** account](https://buddy.works/sign-up).

2. Create a new project and connect it with a git repository (GitHub, GitLab, BitBucket, any private Git Repository or you can use Buddy Git Hosting).

3. Add a new pipeline.

4. In the newly created pipeline add a **[Node.js](https://buddy.works/actions/node-js)** action.

5. In this action add:

   ```bash
   npm install
   npm run build
   ```

6. Add a deployment action — there are many to choose from, you can browse them in [Buddy’s actions catalog](https://buddy.works/actions). Although their settings can differ, remember to set the **Source path** to `dist`.

7. Press the **Run** button.

# Deploy your Astro Site with Cleavr

> How to deploy your Astro site to your VPS server using Cleavr.

You can deploy your Astro project to your own Virtual Private Server (VPS) using [Cleavr](https://cleavr.io/), a server and app deployment management tool.

Tip

Check out [the Astro guide in Cleavr’s docs](https://docs.cleavr.io/guides/astro)!

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* A Cleavr account
* A server on your VPS provider using Cleavr

## Add your site

[Section titled “Add your site”](#add-your-site)

1. In Cleavr, navigate to the server you want to add your Astro project to.

2. Select **Add Site** and fill in the details for your application, such as domain name.

3. For **App Type**, select ‘NodeJS Static’ or ‘NodeJS SSR’ according to how you are setting up your Astro app.

4. For Static apps, set **Artifact Folder** to `dist`.

5. For SSR apps:

   * Set **Entry Point** to `entry.mjs`.
   * Set **Artifact Folder** to `dist/server`.

6. Select **Add** to add the site to your server.

## Setup and deploy

[Section titled “Setup and deploy”](#setup-and-deploy)

1. Once your new site is added, click **Setup and deploy**.

2. Select the **VC Profile**, **Repo**, and **Branch** for your Astro Project.

3. Make any additional configurations necessary for your project.

4. Click on the **Deployments** tab and then click on **Deploy**.

Congratulations, you’ve just deployed your Astro app!

# Deploy your Astro Site to Clever Cloud

> How to deploy your Astro site to the web on Clever Cloud.

[Clever Cloud](https://clever-cloud.com) is a European cloud platform that provides automated, scalable services.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

You can deploy both fully static and on-demand rendered Astro projects on Clever Cloud. Regardless of your `output` mode (pre-rendered or [on-demand](/en/guides/on-demand-rendering/)), you can choose to deploy as a **static application** which runs using a post-build hook, or as a **Node.js** application, which requires some manual configuration in your `package.json`.

### Scripts

[Section titled “Scripts”](#scripts)

If you’re running an on-demand Node.js application, update your `start` script to run the Node server. Applications on Clever Cloud listen on port **8080**.

package.json

```json
"scripts": {
  "start": "node ./dist/server/entry.mjs --host 0.0.0.0 --port 8080",
}
```

## Deploy Astro from the Console

[Section titled “Deploy Astro from the Console”](#deploy-astro-from-the-console)

To deploy your Astro project to Clever Cloud, you will need to **create a new application**. The application wizard will walk you through the necessary configuration steps.

1. From the lateral menubar, click **Create** > **An application**

2. Choose how to deploy:

   * **Create a brand new app**: to deploy from a local repository with Git

   or

   * **Select a GitHub repository**: to deploy from GitHub

3. Select a **Node.js** application, or a **static** one.

4. Set up the minimal size for your instance and scalability options. Astro sites can typically be deployed using the **Nano** instance. Depending on your project’s specifications and dependencies, you may need to adjust accordingly as you watch the metrics from the **Overview** page.

5. Select a **region** to deploy your instance.

6. Skip [connecting **Add-ons** to your Clever application](https://www.clever-cloud.com/developers/doc/addons/) unless you’re using a database or Keycloak.

7. Inject **environment variables**:

   * For **Node.js**, set the following environment variables based on your package manager:

   - npm

     ```shell
     CC_NODE_BUILD_TOOL="npm"
     CC_PRE_BUILD_HOOK="npm install && npm run astro telemetry disable && npm run build"
     ```

   - pnpm

     ```shell
     CC_NODE_BUILD_TOOL="custom"
     CC_PRE_BUILD_HOOK="npm install -g pnpm && pnpm install"
     CC_CUSTOM_BUILD_TOOL="pnpm run astro telemetry disable && pnpm build"
     ```

   - Yarn

     ```shell
     CC_NODE_BUILD_TOOL="yarn"
     CC_PRE_BUILD_HOOK="yarn && yarn run astro telemetry disable && yarn build"
     ```

   * For a **static** application, add these variables:

   - npm

     ```shell
     CC_POST_BUILD_HOOK="npm run build"
     CC_PRE_BUILD_HOOK="npm install && npm run astro telemetry disable"
     CC_WEBROOT="/dist"
     ```

   - pnpm

     ```shell
     CC_POST_BUILD_HOOK="pnpm build"
     CC_PRE_BUILD_HOOK="npm install -g pnpm && pnpm install && pnpm run astro telemetry disable"
     CC_WEBROOT="/dist"
     ```

   - Yarn

     ```shell
     CC_POST_BUILD_HOOK="yarn build"
     CC_PRE_BUILD_HOOK="yarn && yarn run astro telemetry disable"
     CC_WEBROOT="/dist"
     ```

8. **Deploy!** If you’re deploying from **GitHub**, your deployment should start automatically. If you’re using **Git**, copy the remote and push on the **master** branch.

Other Branches

To deploy from branches other than `master`, use `git push clever <branch>:master`.

For example, if you want to deploy your local `main` branch without renaming it, use `git push clever main:master`.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Clever Cloud documentation for deploying a Node.js application](https://www.clever-cloud.com/developers/doc/applications/javascript/nodejs/)
* [Clever Cloud documentation for deploying Astro as a static application](https://www.clever-cloud.com/developers/guides/astro/)

# Deploy your Astro Site to Cloudflare

> How to deploy your Astro site to the web using Cloudflare

You can deploy full-stack applications, including front-end static assets and back-end APIs, as well as on-demand rendered sites, to both [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/) and [Cloudflare Pages](https://pages.cloudflare.com/).

This guide includes:

* [How to deploy to Cloudflare Workers](#cloudflare-workers)
* [How to deploy to Cloudflare Pages](#cloudflare-pages)

Note

Cloudflare recommends using Cloudflare Workers for new projects. For existing Pages projects, refer to [Cloudflare’s migration guide](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/) and [compatibility matrix](https://developers.cloudflare.com/workers/static-assets/migration-guides/migrate-from-pages/#compatibility-matrix).

Read more about [using the Cloudflare runtime](/en/guides/integrations-guide/cloudflare/) in your Astro project.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* A Cloudflare account. If you don’t already have one, you can create a free Cloudflare account during the process.

## Cloudflare Workers

[Section titled “Cloudflare Workers”](#cloudflare-workers)

### How to deploy with Wrangler

[Section titled “How to deploy with Wrangler”](#how-to-deploy-with-wrangler)

1. Install [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/get-started/).

   ```bash
   npm install wrangler@latest --save-dev
   ```

2. If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](/en/guides/integrations-guide/cloudflare/).

   This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

   * npm

     ```sh
     npx astro add cloudflare
     ```

   * pnpm

     ```sh
     pnpm astro add cloudflare
     ```

   * Yarn

     ```sh
     yarn astro add cloudflare
     ```

   Read more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).

3. Create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

   Running `astro add cloudflare` will create this for you; if you are not using the adapter, you’ll need to create it yourself.

   * Static

     wrangler.jsonc

     ```jsonc
     {
       "name": "my-astro-app",
       "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy
       "assets": {
         "binding": "ASSETS",
         "directory": "./dist",
       }
     }
     ```

   * On demand

     wrangler.jsonc

     ```jsonc
     {
       "main": "dist/_worker.js/index.js",
       "name": "my-astro-app",
       "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy
       "compatibility_flags": [
         "nodejs_compat",
         "global_fetch_strictly_public"
       ],
       "assets": {
         "binding": "ASSETS",
         "directory": "./dist"
       },
       "observability": {
         "enabled": true
       }
     }
     ```

4. Preview your project locally with Wrangler.

   ```bash
   npx astro build && npx wrangler dev
   ```

5. Deploy using `npx wrangler deploy`.

   ```bash
   npx astro build && npx wrangler deploy
   ```

After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

Read more about using [Cloudflare runtime APIs](/en/guides/integrations-guide/cloudflare/) such as bindings.

### How to deploy with CI/CD

[Section titled “How to deploy with CI/CD”](#how-to-deploy-with-cicd)

You can also use a CI/CD system such as [Workers Builds (BETA)](https://developers.cloudflare.com/workers/ci-cd/builds/) to automatically build and deploy your site on push.

If you’re using Workers Builds:

1. Follow Steps 1-3 from the Wrangler section above.

2. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and navigate to `Workers & Pages`. Select `Create`.

3. Under `Import a repository`, select a Git account and then the repository containing your Astro project.

4. Configure your project with:

   * Build command: `npx astro build`
   * Deploy command: `npx wrangler deploy`

5. Click `Save and Deploy`. You can now preview your Worker at its provided `workers.dev` subdomain.

## Cloudflare Pages

[Section titled “Cloudflare Pages”](#cloudflare-pages)

### How to deploy with Wrangler

[Section titled “How to deploy with Wrangler”](#how-to-deploy-with-wrangler-1)

1. Install [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/get-started/).

   * npm

     ```sh
     npm install wrangler@latest --save-dev
     ```

   * pnpm

     ```sh
     pnpm add wrangler@latest --save-dev
     ```

   * Yarn

     ```sh
     yarn add wrangler@latest --dev
     ```

2. If your site uses on-demand rendering, install the [`@astrojs/cloudflare` adapter](/en/guides/integrations-guide/cloudflare/).

   This will install the adapter and make the appropriate changes to your `astro.config.mjs` file in one step.

   * npm

     ```sh
     npx astro add cloudflare
     ```

   * pnpm

     ```sh
     pnpm astro add cloudflare
     ```

   * Yarn

     ```sh
     yarn astro add cloudflare
     ```

3. Create a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

   Because Cloudflare recommends new projects use Workers instead of Pages, the `astro add cloudflare` command creates a `wrangler.jsonc` and `public/.assetsignore` file, which are specific to Workers projects. You will need to delete the `public/.assetsignore` file and change your `wrangler.jsonc` file. If you are not using the adapter you’ll need to create it yourself.

   Ensure your `wrangler.jsonc` file is structured like this:

   * Static

     wrangler.jsonc

     ```jsonc
     {
       "name": "my-astro-app",
       "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy
       "pages_build_output_dir": "./dist"
     }
     ```

   * On demand

     wrangler.jsonc

     ```jsonc
     {
       "name": "my-astro-app",
       "compatibility_date": "YYYY-MM-DD", // Update to the day you deploy
       "compatibility_flags": [
         "nodejs_compat",
         "disable_nodejs_process_v2"
       ],
       "pages_build_output_dir": "./dist"
     }
     ```

   Read more about [on-demand rendering in Astro](/en/guides/on-demand-rendering/).

4. Preview your project locally with Wrangler.

   * npm

     ```sh
     npx astro build && wrangler pages dev ./dist
     ```

   * pnpm

     ```sh
     pnpm astro build && wrangler pages dev ./dist
     ```

   * Yarn

     ```sh
     yarn astro build && wrangler pages dev ./dist
     ```

5. Deploy using `npx wrangler deploy`.

   * npm

     ```sh
     npx astro build && wrangler pages deploy ./dist
     ```

   * pnpm

     ```sh
     pnpm astro build && wrangler pages deploy ./dist
     ```

   * Yarn

     ```sh
     yarn astro build && wrangler pages deploy ./dist
     ```

After your assets are uploaded, Wrangler will give you a preview URL to inspect your site.

### How to deploy a site with CI/CD

[Section titled “How to deploy a site with CI/CD”](#how-to-deploy-a-site-with-cicd)

1. Push your code to your git repository (e.g. GitHub, GitLab).

2. Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and navigate to **Compute (Workers) > Workers & Pages**. Select **Create** and then select the **Pages** tab. Connect your git repository.

3. Configure your project with:

   * **Framework preset**: `Astro`
   * **Build command:** `npm run build`
   * **Build output directory:** `dist`

4. Click the **Save and Deploy** button.

## Troubleshooting

[Section titled “Troubleshooting”](#troubleshooting)

### 404 behavior

[Section titled “404 behavior”](#404-behavior)

For Workers projects, you will need to set `not_found_handling` if you want to serve a custom 404 page. You can read more about this in the [Routing behavior section](https://developers.cloudflare.com/workers/static-assets/#routing-behavior) of Cloudflare’s documentation.

wrangler.jsonc

```jsonc
{
  "assets": {
    "directory": "./dist",
    "not_found_handling": "404-page"
  }
}
```

For Pages projects, if you include a custom 404 page, it will be served by default. Otherwise, Pages will default to [Cloudflare’s single-page application rendering behavior](https://developers.cloudflare.com/pages/configuration/serving-pages/#single-page-application-spa-rendering) and redirect to the home page instead of showing a 404 page.

### Client-side hydration

[Section titled “Client-side hydration”](#client-side-hydration)

Client-side hydration may fail as a result of Cloudflare’s Auto Minify setting. If you see `Hydration completed but contains mismatches` in the console, make sure to disable Auto Minify under Cloudflare settings.

### Node.js runtime APIs

[Section titled “Node.js runtime APIs”](#nodejs-runtime-apis)

If you are building a project that is using on-demand rendering with [the Cloudflare adapter](/en/guides/integrations-guide/cloudflare/) and the server fails to build with an error message such as `[Error] Could not resolve "XXXX. The package "XXXX" wasn't found on the file system but is built into node.`:

* This means that a package or import you are using in the server-side environment is not compatible with the [Cloudflare runtime APIs](https://developers.cloudflare.com/workers/runtime-apis/nodejs/).

* If you are directly importing a Node.js runtime API, please refer to the Astro documentation on Cloudflare’s [Node.js compatibility](/en/guides/integrations-guide/cloudflare/#nodejs-compatibility) for further steps on how to resolve this.

* If you are importing a package that imports a Node.js runtime API, check with the author of the package to see if they support the `node:*` import syntax. If they do not, you may need to find an alternative package.

# Deploy your Astro Site with CloudRay

> How to deploy your Astro site to your Ubuntu Server using CloudRay

You can deploy your Astro project using [CloudRay](https://cloudray.io), a centralized platform that helps you manage your servers, organize Bash scripts, and automate deployment tasks across virtual machines and cloud servers.

Note

CloudRay itself does not host your site. Instead, it provides automation tools to run deployment scripts on your own infrastructure (e.g., Ubuntu servers) using a connected agent.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

* A [CloudRay Account](https://app.cloudray.io)
* Your app code stored in a [GitHub](https://github.com/) repository

## How to Deploy through CloudRay Dashboard

[Section titled “How to Deploy through CloudRay Dashboard”](#how-to-deploy-through-cloudray-dashboard)

Deploying with CloudRay typically involves three main steps:

1. Install the [CloudRay Agent](https://cloudray.io/docs/agent) on your server to securely register your machine and enable remote automation.

2. In your CloudRay Dashboard, write a reusable Bash script that clones your Astro repo, installs dependencies, builds your site, and configures a web server. Define any repo-specific values using [CloudRay’s variable groups](https://cloudray.io/docs/variable-groups).

3. Use CloudRay’s Runlog interface to execute your script on your connected server and monitor the deployment in real time.

## Official Resources

[Section titled “Official Resources”](#official-resources)

Check out [the Astro guide in CloudRay’s docs](https://cloudray.io/articles/how-to-deploy-your-astro-site).

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
     ```

   * pnpm

     ```shell
     pnpm install @deno/astro-adapter
     ```

   * Yarn

     ```shell
     yarn add @deno/astro-adapter
     ```

2. Update your `astro.config.mjs` project configuration file with the changes below.

   astro.config.mjs

   ```diff
   import { defineConfig } from 'astro/config';
   +import deno from '@deno/astro-adapter';


   export default defineConfig({
   +  output: 'server',
   +  adapter: deno(),
   });
   ```

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
   ```

   You can now use this command to preview your production Astro site locally with Deno.

   * npm

     ```shell
     npm run preview
     ```

   * pnpm

     ```shell
     pnpm run preview
     ```

   * Yarn

     ```shell
     yarn run preview
     ```

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
     ```

   * pnpm

     ```shell
     pnpm install
     ```

   * Yarn

     ```shell
     yarn
     ```

3. Build your Astro site with your preferred package manager:

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

4. Start your application with the following command:

   * Static

     ```bash
     deno run -A jsr:@std/http/file-server dist
     ```

   * On demand

     ```bash
     deno run -A ./dist/server/entry.mjs
     ```

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
     ```

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
     ```

5. After committing this YAML file, and pushing to GitHub on your configured deploy branch, the deploy should begin automatically!

   You can track the progress using the “Actions” tab on your GitHub repository page, or on [Deno Deploy](https://dash.deno.com).

### CLI Deployment

[Section titled “CLI Deployment”](#cli-deployment)

1. Install the [Deno Deploy CLI](https://docs.deno.com/deploy/manual/deployctl).

   ```bash
   deno install -gArf jsr:@deno/deployctl
   ```

2. Build your Astro site with your preferred package manager:

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

3. Run `deployctl` to deploy!

   * Static

     ```bash
     cd dist && deployctl deploy jsr:@std/http/file-server
     ```

   * On demand

     ```bash
     deployctl deploy ./dist/server/entry.mjs
     ```

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
     ```

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
     ```

   Then you can use this command to build and deploy your Astro site in one step.

   ```bash
   npm run deno-deploy
   ```

# Deploy your Astro Site with DeployHQ

> How to deploy your Astro site to the web using DeployHQ.

You can deploy your Astro project to your own servers using [DeployHQ](https://www.deployhq.com/), a deployment automation platform that builds your code and pushes it to SSH/SFTP servers, FTP servers, cloud storage (e.g. Amazon S3, Cloudflare R2), and modern hosting platforms (e.g. Netlify, Heroku).

Note

DeployHQ does not host your site. It automates building your Astro project and deploying the built files to your chosen hosting provider or server.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

1. If you do not already have one, sign up for a [DeployHQ account](https://www.deployhq.com/).

2. From the DeployHQ web interface, create a new project and connect the Git repository for your Astro project (GitHub, GitLab, Bitbucket, or any private repository). You will also need to authorize DeployHQ to access your repository.

3. Add a server and enter your server details:

   * Give your server a name.
   * Select your protocol (SSH/SFTP, FTP, or cloud platform).
   * Enter your server hostname, username, and password/SSH key.
   * Set **Deployment Path** to your web root (e.g. `public_html/`).

4. In your project settings, navigate to **Build Pipeline** and add your build commands:

   ```bash
   npm install
   npm run build
   ```

5. Click **Deploy Project**, then select your server and click **Deploy** to start your first deployment.

Your Astro site will be built and deployed to your server. You can enable automatic deployments to deploy on every Git push, or schedule deployments for specific times.

See [DeployHQ’s documentation](https://www.deployhq.com/support) for more info on advanced deployment features.

# Deploy your Astro Site to Fleek

> How to deploy your Astro site to the web on Fleek.

You can use [Fleek](http://fleek.xyz/) to deploy a static Astro site to their edge-optimized decentralized network.

This guide gives a complete walkthrough of deploying your Astro site to Fleek using the Fleek UI and CLI.

## Project Configuration

[Section titled “Project Configuration”](#project-configuration)

Your Astro project can be deployed to Fleek as a static site.

## How to deploy

[Section titled “How to deploy”](#how-to-deploy)

You can deploy to Fleek through the website UI or using Fleek’s CLI (command line interface).

### Platform UI Deployment

[Section titled “Platform UI Deployment”](#platform-ui-deployment)

1. Create a [Fleek](https://app.fleek.xyz) account.

2. Push your code to your online Git repository (GitHub).

3. Import your project into Fleek.

4. Fleek will automatically detect Astro and then you can configure the correct settings.

5. Your application is deployed!

### Fleek CLI

[Section titled “Fleek CLI”](#fleek-cli)

1. Install the Fleek CLI.

   ```bash
   # You need to have Nodejs >= 18.18.2
   npm install -g @fleek-platform/cli
   ```

2. Log in to your Fleek account from your terminal.

   ```bash
   fleek login
   ```

3. Run the build command to generate the static files. By default, these will be located in the `dist/` directory.

   ```bash
   npm run build
   ```

4. Initialize your project. This will generate a configuration file.

   ```bash
   fleek sites init
   ```

5. You will be prompted to either create a new Fleek Site or use an existing one. Give the site a name and select the directory where your project is located.

6. Deploy your site.

   ```bash
   fleek sites deploy
   ```

## Learn more

[Section titled “Learn more”](#learn-more)

[Deploy site from Fleek UI](https://fleek.xyz/docs/platform/deployments/)

[Deploy site from Fleek CLI](https://fleek.xyz/docs/cli/hosting/)

# Deploy your Astro Site to AWS with Flightcontrol

> How to deploy your Astro site to AWS with Flightcontrol

You can deploy an Astro site using [Flightcontrol](https://www.flightcontrol.dev?ref=astro), which provides fully-automated deployments to your AWS account.

Supports both static and SSR Astro sites.

## How to Deploy

[Section titled “How to Deploy”](#how-to-deploy)

1. Create a Flightcontrol account at [app.flightcontrol.dev/signup](https://app.flightcontrol.dev/signup?ref=astro)

2. Go to [app.flightcontrol.dev/projects/new/1](https://app.flightcontrol.dev/projects/new/1)

3. Connect your GitHub account and select your repo

4. Select your desired “Config Type”:

   * `GUI` (all config managed through Flightcontrol dashboard) where you will select the `Astro Static` or `Astro SSR` preset
   * `flightcontrol.json` (“infrastructure as code” option where all config is in your repo) where you will select an Astro example config, then add it to your codebase as `flightcontrol.json`

5. Adjust any configuration as needed

6. Click “Create Project” and complete any required steps (like linking your AWS account).

### SSR Setup

[Section titled “SSR Setup”](#ssr-setup)

To deploy with SSR support, make sure you first set up the [`@astrojs/node`](/en/guides/integrations-guide/node/) adapter. Then, follow the steps above, choosing the appropriate configurations for Astro SSR.


---

**Navigation:** [← Previous](./03-apostrophecms-astro.md) | [Index](./index.md) | [Next →](./05-deploy-your-astro-site-to-flyio.md)
