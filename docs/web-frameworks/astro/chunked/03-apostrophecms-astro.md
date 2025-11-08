**Navigation:** [← Previous](./02-actions.md) | [Index](./index.md) | [Next →](./04-optimizely-cms-astro.md)

---

# ApostropheCMS & Astro

> Edit content on the page in your Astro project using Apostrophe as your CMS.

[ApostropheCMS](https://apostrophecms.com/) is a content management system supporting on-page editing in Astro.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you will use the [Apostrophe integration](https://apostrophecms.com/extensions/astro-integration) to connect ApostropheCMS to Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An on-demand rendered Astro project** with the [Node.js adapter](/en/guides/integrations-guide/node/) installed and `output: 'server'` configured - If you don’t have an Astro project yet, our [installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **An ApostropheCMS project with a configured environment variable called `APOS_EXTERNAL_FRONT_KEY`** - This environment variable can be set to any random string. If you don’t have an ApostropheCMS project yet, the [installation guide](https://docs.apostrophecms.org/guide/development-setup.html) will get one setup quickly. We highly recommend using the [Apostrophe CLI tool](https://apostrophecms.com/extensions/apos-cli) to facilitate this.

### Setting up project communication

[Section titled “Setting up project communication”](#setting-up-project-communication)

Your Astro project needs to have an `APOS_EXTERNAL_FRONT_KEY` environment variable set to the same value as the one in your ApostropheCMS project to allow communication between the two. This shared key acts as a means to verify requests between the frontend (Astro) and the backend (ApostropheCMS).

Create a `.env` file in the root of your Astro project with the following variable:

.env

```ini
APOS_EXTERNAL_FRONT_KEY='RandomStrongString'
```

Your root directory should now include this new file:

* src/

  * …

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect Astro with your ApostropheCMS project, install the official Apostrophe integration in your Astro project using the command below for your preferred package manager.

* npm

  ```shell
  npm install @apostrophecms/apostrophe-astro vite @astro/node
  ```

* pnpm

  ```shell
  pnpm add @apostrophecms/apostrophe-astro vite @astro/node
  ```

* Yarn

  ```shell
  yarn add @apostrophecms/apostrophe-astro vite @astro/node
  ```

### Configuring Astro

[Section titled “Configuring Astro”](#configuring-astro)

Configure both the `apostrophe-astro` integration and `vite` in your `astro.config.mjs` file.

The following example provides the base URL of your Apostrophe instance and paths to folders in your project to map between the ApostropheCMS [widgets](https://docs.apostrophecms.org/guide/core-widgets.html) and [page template](https://docs.apostrophecms.org/guide/pages.html) types and your Astro project. It also configures Vite’s server-side rendering.

astro.config.mjs

```js
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';
import apostrophe from '@apostrophecms/apostrophe-astro';
import { loadEnv } from 'vite';


const env = loadEnv("", process.cwd(), 'APOS');


export default defineConfig({
  output: 'server',
  adapter: node({
    mode: 'standalone'
  }),
  integrations: [
    apostrophe({
      aposHost: 'http://localhost:3000',
      widgetsMapping: './src/widgets',
      templatesMapping: './src/templates'
    })
  ],
  vite: {
    ssr: {
      // Do not externalize the @apostrophecms/apostrophe-astro plugin, we need
      // to be able to use virtual: URLs there
      noExternal: [ '@apostrophecms/apostrophe-astro' ],
    },
    define: {
      'process.env.APOS_EXTERNAL_FRONT_KEY': JSON.stringify(env.APOS_EXTERNAL_FRONT_KEY),
      'process.env.APOS_HOST': JSON.stringify(env.APOS_HOST)
    }
  }
});
```

For complete configuration options and explanations, see the [`apostrophe-astro` documentation](https://apostrophecms.com/extensions/astro-integration#configuration-astro).

### Connecting ApostropheCMS widgets to Astro components

[Section titled “Connecting ApostropheCMS widgets to Astro components”](#connecting-apostrophecms-widgets-to-astro-components)

ApostropheCMS widgets are blocks of structured content that can be added to the page such as layout columns, images, and text blocks. You will need to create an Astro component for each widget in your Apostrophe project, plus a file to map those components to the corresponding Apostrophe widget.

Create a new folder at `src/widgets/` for your Astro components and the mapping file, `index.js`.

Mapped components located in this folder receive a `widget` property containing your widget’s schema fields, and any custom props, through `Astro.props`. These values are then available for on-page editing.

The following example shows a `RichTextWidget.astro` component accessing the content from its corresponding ApostropheCMS widget to allow for in-context editing:

src/widgets/RichTextWidget.astro

```js
---
const { widget } = Astro.props;
const { content } = widget;
---
<Fragment set:html={ content }></Fragment>
```

Some standard Apostrophe widgets, such as images and videos, require **placeholders** because they do not contain editable content by default. The following example creates a standard `ImageWidget.astro` component that sets the `src` value conditionally to either the value of the `aposPlaceholder` image passed by the widget, a fallback image from the Astro project, or the image selected by the content manager using the Apostrophe `attachment` helper:

src/widgets/ImageWidget.astro

```js
---
const { widget } = Astro.props;
const placeholder = widget?.aposPlaceholder;
const src = placeholder ?
  '/images/image-widget-placeholder.jpg' :
  widget?._image[0]?.attachment?._urls['full'];
---
<style>
  .img-widget {
    width: 100%;
  }
</style>
<img class="img-widget" {src} />
```

For more examples, see [the `astro-frontend` starter project widget examples](https://github.com/apostrophecms/astro-frontend/tree/main/src/widgets).

Each `.astro` component must be mapped to the corresponding core Apostrophe widget in `src/widgets/index.js`.

The example below adds the previous two components to this file:

src/widgets/index.js

```js
import RichTextWidget from './RichTextWidget.astro';
import ImageWidget from './ImageWidget.astro';


const widgetComponents = {
  '@apostrophecms/rich-text': RichTextWidget,
  '@apostrophecms/image': ImageWidget
};


export default widgetComponents;
```

See [the ApostropheCMS documentation](https://apostrophecms.com/extensions/astro-integration) for naming conventions for standard, pro, and custom-project-level widgets

The project directory should now look like this:

* src/

  * widgets/

    * **index.js**
    * **ImageWidget.astro**
    * **RichTextWidget.astro**

* .env

* astro.config.mjs

* package.json

### Adding page types

[Section titled “Adding page types”](#adding-page-types)

Much like widgets, any page type template in your ApostropheCMS project needs to have a corresponding template component in your Astro project. You will also need a file that maps the Apostrophe page types to individual components.

Create a new folder at `src/templates/` for your Astro components and the mapping file, `index.js`. Mapped components located in this folder receive a `page` property containing the schema fields of your page, and any custom props, through `Astro.props`. These components can also access an `AposArea` component to render Apostrophe areas.

The following example shows a `HomePage.astro` component rendering a page template from its corresponding `home-page` ApostropheCMS page type, including an area schema field named `main`:

src/templates/HomePage.astro

```js
---
import AposArea from '@apostrophecms/apostrophe-astro/components/AposArea.astro';
const { page, user, query } = Astro.props.aposData;
const { main } = page;
---


<section class="bp-content">
  <h1>{ page.title }</h1>
  <AposArea area={main} />
</section>
```

Each `.astro` component must be mapped to the corresponding core Apostrophe page type in `src/templates/index.js`.

The example below adds the previous `HomePage.astro` component to this file:

src/templates/index.js

```js
import HomePage from './HomePage.astro';


const templateComponents = {
  '@apostrophecms/home-page': HomePage
};


export default templateComponents;
```

See [the ApostropheCMS documentation](https://apostrophecms.com/extensions/astro-integration/#how-apostrophe-template-names-work) for template naming conventions, including special pages and piece page types.

The project directory should now look like this:

* src/

  * widgets/

    * index.js
    * ImageWidget.astro
    * RichTextWidget.astro

  * templates/

    * **HomePage.astro**
    * **index.js**

* .env

* astro.config.mjs

* package.json

### Creating the \[…slug.astro] component and fetching Apostrophe data

[Section titled “Creating the \[…slug.astro\] component and fetching Apostrophe data”](#creating-the-slugastro-component-and-fetching-apostrophe-data)

Since Apostrophe is responsible for connecting URLs to content, including creating new content and pages on the fly, you will only need one top-level Astro page component: the `[...slug].astro` route.

The following example shows a minimal `[...slug].astro` component:

src/pages/\[...slug].astro

```js
---
import aposPageFetch from '@apostrophecms/apostrophe-astro/lib/aposPageFetch.js';
import AposLayout from '@apostrophecms/apostrophe-astro/components/layouts/AposLayout.astro';
import AposTemplate from '@apostrophecms/apostrophe-astro/components/AposTemplate.astro';


const aposData = await aposPageFetch(Astro.request);
const bodyClass = `myclass`;


if (aposData.redirect) {
  return Astro.redirect(aposData.url, aposData.status);
}
if (aposData.notFound) {
  Astro.response.status = 404;
}
---
<AposLayout title={aposData.page?.title} {aposData} {bodyClass}>
    <Fragment slot="standardHead">
      <meta name="description" content={aposData.page?.seoDescription} />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta charset="UTF-8" />
    </Fragment>
    <AposTemplate {aposData} slot="main"/>
</AposLayout>
```

See [the ApostropheCMS documentation](https://apostrophecms.com/extensions/astro-integration#creating-the-slugastro-component-and-fetching-apostrophe-data) for additional templating options, including slots available in the `AposTemplate` component.

## Making a blog with Astro and ApostropheCMS

[Section titled “Making a blog with Astro and ApostropheCMS”](#making-a-blog-with-astro-and-apostrophecms)

With the integration set up, you can now create a blog with Astro and ApostropheCMS. Your blog will use an Apostrophe piece, a stand-alone content type that can be included on any page, and a piece page type, a specialized page type that is used for displaying those pieces either individually or collectively.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. **An ApostropheCMS project with the Apostrophe CLI tool installed** - You can create a new project or use an existing one. However, this tutorial will only show how to create a blog piece and piece page type. You will have to integrate any other existing project code independently. If you don’t have the CLI tool installed, consult the [Apostrophe CLI installation instructions](https://docs.apostrophecms.org/guide/setting-up.html#the-apostrophe-cli-tool).
2. **An Astro project integrated with ApostropheCMS** - To create a project from scratch, see [integrating with Astro](#integrating-with-astro) for instructions on how to set up the integration, or use the [astro-frontend](https://github.com/apostrophecms/astro-frontend) starter project.

### Creating a blog piece and piece page type

[Section titled “Creating a blog piece and piece page type”](#creating-a-blog-piece-and-piece-page-type)

To create your blog piece and piece page type for their display, navigate to the root of your ApostropheCMS project in your terminal. Use the ApostropheCMS CLI tool to create the new piece and piece page type with the following command:

```sh
apos add piece blog --page
```

This will create two new modules in your project, one for the blog piece type and one for the corresponding piece page type. Next, open the `app.js` file at the root of your ApostropheCMS project in your code editor and add your new modules.

app.js

```js
require('apostrophe')({
  // other configuration options
  modules: {
    // other project modules
    blog: {},
    'blog-page': {}
  }
});
```

The `blog-page` module also needs to be added to the `@apostrophecms/page` module `types` option array so that it can be selected in the page creation modal. In your ApostropheCMS project, open the `modules/@apostrophecms/page/index.js` file and add the `blog-page`.

modules/@apostrophecms/page/index.js

```js
module.exports = {
  options: {
    types: [
      {
        name: '@apostrophecms/home-page',
        label: 'Home'
      },
      // Any other project pages
      {
        name: 'blog-page',
        label: 'Blog'
      }
    ]
  }
};
```

### Creating the blog schema

[Section titled “Creating the blog schema”](#creating-the-blog-schema)

In an ApostropheCMS project, editors are offered a set of input fields for adding content. Here is an example of a simple blog post that adds three input fields, an `authorName`, `publicationDate` and `content` area where content managers can add multiple widget instances. In this case, we are specifying they can add the image and rich-text widgets we created during the [integration setup](#connecting-apostrophecms-widgets-to-astro-components).

modules/blog/index.js

```js
module.exports = {
  extend: '@apostrophecms/piece-type',
  options: {
    label: 'Blog',
    // Additionally add a `pluralLabel` option if needed.
  },
  fields: {
    add: {
      authorName: {
        type: 'string',
        label: 'Author'
      },
      publicationDate: {
        type: 'date',
        label: 'Publication date'
      },
      content: {
        type: 'area',
        label: 'Content',
        options: {
          widgets: {
            '@apostrophecms/rich-text': {},
            '@apostrophecms/image': {}
          }
        }
      }
    },
    group: {
      basics: {
        label: 'Basic',
        fields: [ 'authorName', 'publicationDate', 'content' ]
      }
    }
  }
};
```

At this point, all the components coming from the ApostropheCMS project are set up. Start the local site from the command line using `npm run dev`, making sure to pass in the `APOS_EXTERNAL_FRONT_KEY` environment variable set to your selected string:

```bash
APOS_EXTERNAL_FRONT_KEY='MyRandomString' npm run dev
```

### Displaying the blog posts

[Section titled “Displaying the blog posts”](#displaying-the-blog-posts)

To display a page with all the blog posts create a `BlogIndex.astro` component file in the `src/templates` directory of your Astro project and add the following code:

After fetching both the page and pieces data from the `aposData` prop, this component creates markup using both fields from the blog piece schema we created, but also from the `piece.title` and `piece._url` that is added to each piece by Apostrophe.

src/templates/BlogIndex.astro

```js
---
import dayjs from 'dayjs';


const { page, pieces } = Astro.props.aposData;
---


<section class="bp-content">
  <h1>{ page.title }</h1>


  <h2>Blog Posts</h2>


  {pieces.map(piece => (
    <h4>
      Released On { dayjs(piece.publicationDate).format('MMMM D, YYYY') }
    </h4>
    <h3>
      <a href={ piece._url }>{ piece.title }</a>
    </h3>
    <h4>{ piece.authorName }</h4>
  ))}
</section>
```

To display individual blog posts, create a `BlogShow.astro` file in the Astro project `src/templates` folder with the following code:

This component uses the `<AposArea>` component to display any widgets added to the `content` area and the `authorName` and `publicationDate` content entered into the fields of the same names.

src/templates/BlogShow\.astro

```js
---
import AposArea from '@apostrophecms/apostrophe-astro/components/AposArea.astro';
import dayjs from 'dayjs';


const { page, piece } = Astro.props.aposData;
const { main } = piece;
---


<section class="bp-content">
  <h1>{ piece.title }</h1>
  <h3>Created by: { piece.authorName }
  <h4>
    Released On { dayjs(piece.publicationDate).format('MMMM D, YYYY') }
  </h4>
  <AposArea area={content} />
</section>
```

Finally, these Astro components must be mapped to the corresponding ApostropheCMS page types. Open the Astro project `src/templates/index.js` file and modify it to contain the following code:

src/templates/index.js

```js
import HomePage from './HomePage.astro';
import BlogIndexPage from './BlogIndexPage.astro';
import BlogShowPage from './BlogShowPage.astro';


const templateComponents = {
  '@apostrophecms/home-page': HomePage,
  '@apostrophecms/blog-page:index': BlogIndexPage,
  '@apostrophecms/blog-page:show': BlogShowPage
};


export default templateComponents;
```

### Creating blog posts

[Section titled “Creating blog posts”](#creating-blog-posts)

Adding blog posts to your site is accomplished by using the ApostropheCMS content and management tools to create those posts and by publishing at least one index page to display them.

With the Astro dev server running, navigate to the login page located at <http://localhost:4321/login> in your browser preview. Use the credentials that were added during the [creation of the ApostropheCMS project](https://docs.apostrophecms.org/guide/development-setup.html#creating-a-project) to log in as an administrator. Your ApostropheCMS project should still be running.

Once you are logged in, your browser will be redirected to the home page of your project and will display an admin bar at the top for editing content and managing your project.

To add your first blog post, click on the `Blogs` button in the admin bar to open the blog piece creation modal. Clicking on the `New Blog` button in the upper right will open an editing modal where you can add content. The `content` area field will allow you to add as many image and rich text widgets as you desire.

You can repeat this step and add as many posts as you want. You will also follow these steps every time you want to add a new post.

To publish a page for displaying all your posts, click on the `Pages` button in the admin bar. From the page tree modal click on the `New Page` button. In the `Type` dropdown in the right column select `Blog`. Add a title for the page and then click `Publish and View`. You will only need to do this once.

Any new blog posts that are created will be automatically displayed on this page. Individual blog posts can be displayed by clicking on the link created on the index page.

The `content` area of individual posts can be edited directly on the page by navigating to the post and clicking `edit` in the admin bar. Other fields can be edited by using the editing modal opened when clicking the `Blogs` menu item in the admin bar.

### Deploying your site

[Section titled “Deploying your site”](#deploying-your-site)

To deploy your website, you need to host both your Astro and ApostropheCMS projects.

For Astro, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

For the ApostropheCMS project, follow the instructions for your hosting type in our [hosting guide](https://docs.apostrophecms.org/guide/hosting.html). Finally, you’ll need to supply an `APOS_HOST` environment variable to the Astro project to reflect the correct URL where your ApostropheCMS site has been deployed.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro integration for ApostropheCMS](https://apostrophecms.com/extensions/astro-integration) - ApostropheCMS Astro plugin, integration guide and starter projects for both Apostrophe and Astro
* [Sample Astro project for use with ApostropheCMS](https://github.com/apostrophecms/astro-frontend) - A simple Astro project with several pages and Apostrophe widgets already created.
* [Sample ApostropheCMS starter-kit for use with Astro](https://apostrophecms.com/starter-kits/astro-integration-starter-kit) - An ApostropheCMS project with core page modifications for use with Astro.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Integrating ApostropheCMS with Astro, Pt. 1](https://apostrophecms.com/blog/how-to-integrate-astro-with-apostrophecms-pt-1) by Antonello Zaini
* [Integrating ApostropheCMS with Astro, Pt. 2](https://apostrophecms.com/blog/how-to-integrate-astro-with-apostrophecms-pt-2) by Antonello Zaini
* [Show & Tell Live | Astro & Apostrophe](https://youtu.be/cwJhtJhAhwA?si=6iUU9EjidfdnOdCh)

# Builder.io & Astro

> Add content to your Astro project using Builder.io’s visual CMS

[Builder.io](https://www.builder.io/) is a visual CMS that supports drag-and-drop content editing for building websites.

This recipe will show you how to connect your Builder space to Astro with zero client-side JavaScript.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

* **A Builder account and space** - If you don’t have an account yet, [sign up for free](https://www.builder.io/) and create a new space. If you already have a space with Builder, feel free to use it, but you will need to modify the code to match the model name (`blogpost`) and custom data fields.
* **A Builder API key** - This public key will be used to fetch your content from Builder. [Read Builder’s guide on how to find your key](https://www.builder.io/c/docs/using-your-api-key#finding-your-public-api-key).

## Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your Builder API key and your Builder model name to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variables:

.env

```ini
BUILDER_API_PUBLIC_KEY=YOUR_API_KEY
BUILDER_BLOGPOST_MODEL='blogpost'
```

Now, you should be able to use this API key in your project.

Note

At the time of writing, [this key is public](https://www.builder.io/c/docs/using-your-api-key#prerequisites), so you don’t have to worry about hiding or encrypting it.

If you would like to have IntelliSense for your environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly BUILDER_API_PUBLIC_KEY: string;
}
```

Your project should now include these files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

Learn more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

## Making a blog with Astro and Builder

[Section titled “Making a blog with Astro and Builder”](#making-a-blog-with-astro-and-builder)

### Creating a model for a blog post

[Section titled “Creating a model for a blog post”](#creating-a-model-for-a-blog-post)

The instructions below create an Astro blog using a Builder model (Type: “Section”) called `blogpost` that contains two required text fields: `title` and `slug`.

For visual types

You can find videos showing this procedure in one of [Builder’s official tutorials](https://www.builder.io/blog/creating-blog#creating-a-blog-article-model).

In the Builder app create the model that will represent a blog post: go to the **Models** tab and click the **+ Create Model** button to create model with the following fields and values:

* **Type:** Section
* **Name:** “blogpost”
* **Description:** “This model is for a blog post”

In your new model use the **+ New Custom Field** button to create 2 new fields:

1. Text field

   * **Name:** “title”
   * **Required:** Yes
   * **Default value** “I forgot to give this a title”

   (leave the other parameters as their defaults)

2. Text field

   * **Name:** “slug”
   * **Required:** Yes
   * **Default value** “some-slugs-take-their-time”

   (leave the other parameters as their defaults)

Then click the **Save** button in the upper right.

Slugs

There are some pitfalls with the `slug` field:

* Make sure your slug is not just a number. This seems to break the fetch request to Builder’s API.

* Make sure your slugs are unique, since your site’s routing will depend on that.

### Setting up the preview

[Section titled “Setting up the preview”](#setting-up-the-preview)

To use Builder’s visual editor, create the page `src/pages/builder-preview.astro` that will render the special `<builder-component>`:

* src/

  * pages/

    * **builder-preview\.astro**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

Then add the following content:

src/pages/builder-preview\.astro

```astro
---
const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;
const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;
---


<html lang="en">
  <head>
    <title>Preview for builder.io</title>
  </head>
  <body>
    <header>This is your header</header>


    <builder-component model={builderModel} api-key={builderAPIpublicKey}
    ></builder-component>
    <script async src="https://cdn.builder.io/js/webcomponents"></script>


    <footer>This is your footer</footer>
  </body>
</html>
```

In the above example, `<builder-component>` tells Builder where to insert the content from its CMS.

#### Setting the new route as the preview URL

[Section titled “Setting the new route as the preview URL”](#setting-the-new-route-as-the-preview-url)

1. Copy the full URL of your preview, including the protocol, to your clipboard (e.g. `https://{your host}/builder-preview`).

2. Go to the **Models** tab in your Builder space, pick the model you’ve created and paste the URL from step 1 into the **Preview URL** field. Make sure the URL is complete and includes the protocol, for example `https://`.

3. Click the **Save** button in the upper right.

Tip

When you deploy your site, change the preview URL to match your production URL, for example `https://myAwesomeAstroBlog.com/builder-preview`.

#### Testing the preview URL setup

[Section titled “Testing the preview URL setup”](#testing-the-preview-url-setup)

1. Make sure your site is live (e.g. your dev server is running) and the `/builder-preview` route is working.

2. In your Builder space under the **Content** tab, click on **New** to create a new content entry for your `blogpost` model.

3. In the Builder editor that just opened, you should be able to see the `builder-preview.astro` page with a big **Add Block** in the middle.

Troubleshooting

Things can sometimes go wrong when setting up the preview. If something’s not right, you can try one of these things:

* Make sure the site is live - for example, your dev server is running.
* Make sure that the URLs match exactly - the one in your Astro project and the one set in the Builder app.
* Make sure it’s the full URL including the protocol, for example `https://`.
* If you’re working in a virtual environment like [IDX](https://idx.dev), [StackBlitz](https://stackblitz.com/), or [Gitpod](https://www.gitpod.io/), you might have to copy and paste the URL again when you restart your workspace, since this usually generates a new URL for your project.

For more ideas, read [Builder’s troubleshooting guide](https://www.builder.io/c/docs/guides/preview-url-working).

### Creating a blog post

[Section titled “Creating a blog post”](#creating-a-blog-post)

1. In Builder’s visual editor, create a new content entry with the following values:

   * **title:** ‘First post, woohoo!’
   * **slug:** ‘first-post-woohoo’

2. Complete your post using the **Add Block** button and add a text field with some post content.

3. In the text field above the editor, give your entry a name. This is how it will be listed in the Builder app.

4. When you’re ready click the **Publish** button in the upper right corner.

5. Create as many posts as you like, ensuring that all content entries contain a `title` and a `slug` as well as some post content.

### Displaying a list of blog posts

[Section titled “Displaying a list of blog posts”](#displaying-a-list-of-blog-posts)

Add the following content to `src/pages/index.astro` in order to fetch and display a list of all post titles, each linking to its own page:

src/pages/index.astro

```astro
---


const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;
const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;


const { results: posts } = await fetch(
  `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams({
    apiKey: builderAPIpublicKey,
    fields: ["data.slug", "data.title"].join(","),
    cachebust: "true",
  }).toString()}`
)
  .then((res) => res.json())
  .catch();
---


<html lang="en">
  <head>
    <title>Blog Index</title>
  </head>
  <body>
    <ul>
      {
        posts.flatMap(({ data: { slug, title } }) => (
          <li>
            <a href={`/posts/${slug}`}>{title}</a>
          </li>
        ))
      }
    </ul>
  </body>
</html>
```

Fetching via the content API returns an array of objects containing data for each post. The `fields` query parameter tells Builder which data is included (see highlighted code). `slug` and `title` should match the names of the custom data fields you’ve added to your Builder model.

The `posts` array returned from the fetch displays a list of blog post titles on the home page. The individual page routes will be created in the next step.

Framework integrations

If you are using a JavaScript framework (e.g. Svelte, Vue, or React) in your Astro project you can use [one of Builder’s integrations](https://www.builder.io/m/integrations) as an alternative to making raw fetch calls through the REST API.

Go to your index route and you should be able to see a list of links each with the title of a blog post!

### Displaying a single blog post

[Section titled “Displaying a single blog post”](#displaying-a-single-blog-post)

Create the page `src/pages/posts/[slug].astro` that will [dynamically generate a page](/en/guides/routing/#dynamic-routes) for each post.

* src/

  * pages/

    * index.astro

    * posts/

      * **\[slug].astro**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

This file must contain:

* A [`getStaticPaths()`](/en/reference/routing-reference/#getstaticpaths) function to fetch `slug` information from Builder and create a static route for each blog post.
* A `fetch()` to the Builder API using the `slug` identifier to return post content and metadata (e.g. a `title`).
* A `<Fragment />` in the template to render the post content as HTML.

Each of these is highlighted in the following code snippet.

src/pages/posts/\[slug].astro

```diff
---
+export async function getStaticPaths() {
  const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;
  const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;
  const { results: posts } = await fetch(
    `https://cdn.builder.io/api/v3/content/${builderModel}?${new URLSearchParams(
      {
        apiKey: builderAPIpublicKey,
        fields: ["data.slug", "data.title"].join(","),
        cachebust: "true",
      }
    ).toString()}`
  )
    .then((res) => res.json())
    .catch
    // ...catch some errors...);
    ();
  return posts.map(({ data: { slug, title } }) => ({
    params: { slug },
    props: { title },
  }))
}
const { slug } = Astro.params;
const { title } = Astro.props;
const builderModel = import.meta.env.BUILDER_BLOGPOST_MODEL;
+const builderAPIpublicKey = import.meta.env.BUILDER_API_PUBLIC_KEY;
// Builder's API requires this field but for this use case the url doesn't seem to matter - the API returns the same HTML
const encodedUrl = encodeURIComponent("moot");
const { html: postHTML } = await fetch(
  `https://cdn.builder.io/api/v1/qwik/${builderModel}?${new URLSearchParams({
    apiKey: builderAPIpublicKey,
    url: encodedUrl,
    +"query.data.slug": slug,
    cachebust: "true",
  }).toString()}`
)
  .then((res) => res.json())
  .catch();
---
<html lang="en">
  <head>
    <title>{title}</title>
  </head>
  <body>
    <header>This is your header</header>
    <article>
      <Fragment set:html={postHTML} />
    </article>
    <footer>This is your footer</footer>
  </body>
</html>
```

Note

The variables `builderModel` and `builderAPIpublicKey` need to be created twice, since [`getStaticPaths()` runs in its own isolated scope](/en/reference/routing-reference/#getstaticpaths).

Now when you click on a link on your index route, you will be taken to the individual blog post page.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Builder changes

[Section titled “Rebuild on Builder changes”](#rebuild-on-builder-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build whenever you click **Publish** in the Builder editor.

##### Netlify

[Section titled “Netlify”](#netlify)

1. Go to your site dashboard, then **Site Settings** and click on **Build & deploy**.

2. Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.

3. Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.

##### Vercel

[Section titled “Vercel”](#vercel)

1. Go to your project dashboard and click on **Settings**.

2. Under the **Git** tab, find the **Deploy Hooks** section.

3. Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.

##### Adding a webhook to Builder

[Section titled “Adding a webhook to Builder”](#adding-a-webhook-to-builder)

Official resource

See [Builder’s guide on adding webhooks](https://www.builder.io/c/docs/webhooks) for more information.

1. In your Builder dashboard, go into your **`blogpost`** model. Under **Show More Options**, select **Edit Webhooks** at the bottom.

2. Add a new webhook by clicking on **Webhook**. Paste the URL generated by your hosting provider into the **Url** field.

3. Click on **Show Advanced** under the URL field and toggle the option to select **Disable Payload**. With the payload disabled, Builder sends a simpler POST request to your hosting provider, which can be helpful as your site grows. Click **Done** to save this selection.

With this webhook in place, whenever you click the **Publish** button in the Builder editor, your hosting provider rebuilds your site - and Astro fetches the newly published data for you. Nothing to do but lean back and pump out that sweet sweet content!

## Official resources

[Section titled “Official resources”](#official-resources)

* Check out [the official Builder.io starter project](https://github.com/BuilderIO/builder/tree/main/examples/astro-solidjs), which uses Astro and SolidJS.
* The [official Builder quickstart guide](https://www.builder.io/c/docs/quickstart#step-1-add-builder-as-a-dependency) covers both the use of the REST API as well as data fetching through an integration with a JavaScript framework like Qwik, React or Vue.
* [Builder’s API explorer](https://builder.io/api-explorer) can help if you need to troubleshoot your API calls.

## Community resources

[Section titled “Community resources”](#community-resources)

* Read [Connecting Builder.io’s Visual CMS to Astro](https://www.hamatoyogi.dev/blog/astro-log/connecting-builderio-to-astro) by Yoav Ganbar.

# ButterCMS & Astro

> Add content to your Astro project using ButterCMS

[ButterCMS](https://buttercms.com/) is a headless CMS and blog engine that allows you to publish structured content to use in your project.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

Note

For a full blog site example, see the [Astro + ButterCMS Starter Project](https://buttercms.com/starters/astro-starter-project/).

In this section, we’ll use the [ButterCMS SDK](https://www.npmjs.com/package/buttercms) to bring your data into your Astro project. To get started, you will need to have the following:

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A ButterCMS account**. If you don’t have an account, you can [sign up](https://buttercms.com/join/) for a free trial.

3. **Your ButterCMS API Token** - You can find your API Token on the [Settings](https://buttercms.com/settings/) page.

### Setup

[Section titled “Setup”](#setup)

1. Create a `.env` file in the root of your project and add your API token as an environment variable:

   .env

   ```ini
   BUTTER_TOKEN=YOUR_API_TOKEN_HERE
   ```

   Tip

   Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

2. Install the ButterCMS SDK as a dependency:

   * npm

     ```shell
     npm install buttercms
     ```

   * pnpm

     ```shell
     pnpm add buttercms
     ```

   * Yarn

     ```shell
     yarn add buttercms
     ```

3. Create a `buttercms.js` file in a new `src/lib/` directory in your project:

   src/lib/buttercms.js

   ```js
   import Butter from "buttercms";


   export const butterClient = Butter(import.meta.env.BUTTER_TOKEN);
   ```

**This authenticates the SDK using your API Token and exports it to be used across your project.**

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

To fetch content, import this client and use one of its `retrieve` functions.

In this example, we [retrieve a collection](https://buttercms.com/docs/api/#retrieve-a-collection) that has three fields: a short text `name`, a number `price`, and a WYSIWYG `description`.

src/pages/ShopItem.astro

```astro
---
import { butterClient } from "../lib/buttercms";
const response = await butterClient.content.retrieve(["shopitem"]);


interface ShopItem {
  name: string,
  price: number,
  description: string,
}


const items = response.data.data.shopitem as ShopItem[];
---
<body>
  {items.map(item => <div>
    <h2>{item.name} - ${item.price}</h2>
    <p set:html={item.description}></p>
  </div>)}
</body>
```

The interface mirrors the field types. The WYSIWYG `description` field loads as a string of HTML, and [`set:html`](/en/reference/directives-reference/#sethtml) lets you render it.

Similarly, you can [retrieve a page](https://buttercms.com/docs/api/#get-a-single-page) and display its fields:

src/pages/ShopItem.astro

```astro
---
import { butterClient } from "../lib/buttercms";
const response = await butterClient.page.retrieve("*", "simple-page");
const pageData = response.data.data;


interface Fields {
  seo_title: string,
  headline: string,
  hero_image: string,
}


const fields = pageData.fields as Fields;
---
<html>
  <title>{fields.seo_title}</title>
  <body>
    <h1>{fields.headline}</h1>
    <img src={fields.hero_image} />
  </body>
</html>
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro + ButterCMS Starter Project](https://buttercms.com/starters/astro-starter-project/)
* The [full ButterCMS API documentation](https://buttercms.com/docs/api/)
* ButterCMS’s [JavaScript Guide](https://buttercms.com/docs/api-client/javascript/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* Add yours!

# Caisy & Astro

> Add content to your Astro project using Caisy as a CMS

[Caisy](https://caisy.io/) is a headless CMS that exposes a GraphQL API to access content.

## Using Caisy CMS with Astro

[Section titled “Using Caisy CMS with Astro”](#using-caisy-cms-with-astro)

Use `graphql-request` and Caisy’s rich text renderer for Astro to fetch your CMS data and display your content on an Astro page:

src/pages/blog/\[...slug].astro

```astro
---
import RichTextRenderer from '@caisy/rich-text-astro-renderer';
import { gql, GraphQLClient } from 'graphql-request';


const params = Astro.params;


const client = new GraphQLClient(
  `https://cloud.caisy.io/api/v3/e/${import.meta.env.CAISY_PROJECT_ID}/graphql`,
  {
    headers: {
      'x-caisy-apikey': import.meta.env.CAISY_API_KEY
    }
  }
);
const gqlResponse = await client.request(
  gql`
    query allBlogArticle($slug: String) {
      allBlogArticle(where: { slug: { eq: $slug } }) {
        edges {
          node {
            text {
              json
            }
            title
            slug
            id
          }
        }
      }
    }
  `,
  { slug: params.slug }
);


const post = gqlResponse?.allBlogArticle?.edges?.[0]?.node;
---
<h1>{post.title}</h1>
<RichTextRenderer node={post.text.json} />
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out the Caisy + Astro example on [GitHub](https://github.com/caisy-io/caisy-example-astro) or [StackBlitz](https://stackblitz.com/github/caisy-io/caisy-example-astro?file=src%2Fpages%2Fblog%2F%5B...slug%5D.astro)
* Query your documents in [draft mode](https://caisy.io/developer/docs/external-api/localization-and-preview#preview-mode-15) and multiple [locales](https://caisy.io/developer/docs/external-api/localization-and-preview#localization-in-a-graphql-query-8).
* Use [pagination](https://caisy.io/developer/docs/external-api/queries-pagination) to query large numbers of documents.
* Use [filter](https://caisy.io/developer/docs/external-api/external-filter-and-sorting) in your queries and [order](https://caisy.io/developer/docs/external-api/external-filter-and-sorting#sorting-8) the results

# CloudCannon & Astro

> Add content to your Astro project using CloudCannon as a CMS

[CloudCannon](https://cloudcannon.com) is a Git-based headless content management system that provides a visual editor for your content.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Astro Starter Template](https://cloudcannon.com/templates/astro-starter/)
* [Astro Multilingual Starter Template](https://cloudcannon.com/templates/astro-multilingual-starter/)
* [Astro Starter Guide](https://cloudcannon.com/documentation/guides/astro-starter-guide/)
* [Bookshop & Astro Guide](https://cloudcannon.com/documentation/guides/bookshop-astro-guide/)
* [Astro Beginner Tutorial Series](https://cloudcannon.com/tutorials/astro-beginners-tutorial-series/)
* Blog: [How CloudCannon’s live editing works with Astro and Bookshop](https://cloudcannon.com/blog/how-cloudcannons-live-editing-works-with-astro-and-bookshop/)
* Blog: [Out-of-this-world support for all Astro users](https://cloudcannon.com/blog/out-of-this-world-support-for-all-astro-users/)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [CloudCannon announces official support for Astro](https://astro.build/blog/astro-cloudcannon-support/)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/sendit.Cu8vxERj_ZX2Pho.webp) Sendit](https://astro.build/themes/details/sendit/)

# Contentful & Astro

> Add content to your Astro project using Contentful as a CMS

[Contentful](https://www.contentful.com/) is a headless CMS that allows you to manage content, integrate with other services, and publish to multiple platforms.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, we’ll use the [Contentful SDK](https://github.com/contentful/contentful.js) to connect your Contentful space to Astro with zero client-side JavaScript.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A Contentful account and a Contentful space**. If you don’t have an account, you can [sign up](https://www.contentful.com/sign-up/) for a free account and create a new Contentful space. You can also use an existing space if you have one.

3. **Contentful credentials** - You can find the following credentials in your Contentful dashboard **Settings > API keys**. If you don’t have any API keys, create one by selecting **Add API key**.

   * **Contentful space ID** - The ID of your Contentful space.
   * **Contentful delivery access token** - The access token to consume *published* content from your Contentful space.
   * **Contentful preview access token** - The access token to consume *unpublished* content from your Contentful space.

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your Contentful space’s credentials to Astro, create an `.env` file in the root of your project with the following variables:

.env

```ini
CONTENTFUL_SPACE_ID=YOUR_SPACE_ID
CONTENTFUL_DELIVERY_TOKEN=YOUR_DELIVERY_TOKEN
CONTENTFUL_PREVIEW_TOKEN=YOUR_PREVIEW_TOKEN
```

Now, you can use these environment variables in your project.

If you would like to have IntelliSense for your Contentful environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly CONTENTFUL_SPACE_ID: string;
  readonly CONTENTFUL_DELIVERY_TOKEN: string;
  readonly CONTENTFUL_PREVIEW_TOKEN: string;
}
```

Tip

Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your root directory should now include these new files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect with your Contentful space, install both of the following using the single command below for your preferred package manager:

* [`contentful.js`](https://github.com/contentful/contentful.js), the official Contentful SDK for JavaScript
* [`rich-text-html-renderer`](https://github.com/contentful/rich-text/tree/master/packages/rich-text-html-renderer), a package to render Contentful’s rich text fields to HTML.

- npm

  ```shell
  npm install contentful @contentful/rich-text-html-renderer
  ```

- pnpm

  ```shell
  pnpm add contentful @contentful/rich-text-html-renderer
  ```

- Yarn

  ```shell
  yarn add contentful @contentful/rich-text-html-renderer
  ```

Next, create a new file called `contentful.ts` in the `src/lib/` directory of your project.

src/lib/contentful.ts

```ts
import * as contentful from "contentful";


export const contentfulClient = contentful.createClient({
  space: import.meta.env.CONTENTFUL_SPACE_ID,
  accessToken: import.meta.env.DEV
    ? import.meta.env.CONTENTFUL_PREVIEW_TOKEN
    : import.meta.env.CONTENTFUL_DELIVERY_TOKEN,
  host: import.meta.env.DEV ? "preview.contentful.com" : "cdn.contentful.com",
});
```

The above code snippet creates a new Contentful client, passing in credentials from the `.env` file.

Caution

While in development mode, your content will be fetched from the **Contentful preview API**. This means that you will be able to see unpublished content from the Contentful web app.

At build time, your content will be fetched from the **Contentful delivery API**. This means that only published content will be available at build time.

Finally, your root directory should now include these new files:

* src/

  * env.d.ts

  * lib/

    * **contentful.ts**

* .env

* astro.config.mjs

* package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

Astro components can fetch data from your Contentful account by using the `contentfulClient` and specifying the `content_type`.

For example, if you have a “blogPost” content type that has a text field for a title and a rich text field for content, your component might look like this:

```astro
---
import { contentfulClient } from "../lib/contentful";
import { documentToHtmlString } from "@contentful/rich-text-html-renderer";
import type { EntryFieldTypes } from "contentful";


interface BlogPost {
  contentTypeId: "blogPost",
  fields: {
    title: EntryFieldTypes.Text
    content: EntryFieldTypes.RichText,
  }
}


const entries = await contentfulClient.getEntries<BlogPost>({
  content_type: "blogPost",
});
---
<body>
  {entries.items.map((item) => (
    <section>
      <h2>{item.fields.title}</h2>
      <article set:html={documentToHtmlString(item.fields.content)}></article>
    </section>
  ))}
</body>
```

Tip

If you have an empty Contentful space, check out [setting up a Contentful model](#setting-up-a-contentful-model) to learn how to create a basic blog model for your content.

You can find more querying options in the [Contentful documentation](https://contentful.github.io/contentful.js/).

## Making a blog with Astro and Contentful

[Section titled “Making a blog with Astro and Contentful”](#making-a-blog-with-astro-and-contentful)

With the setup above, you are now able to create a blog that uses Contentful as the CMS.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. **A Contentful space** - For this tutorial we recommend starting with an empty space. If you already have a content model, feel free to use it, but you will need to modify our code snippets to match your content model.
2. **An Astro project integrated with the [Contentful SDK](https://github.com/contentful/contentful.js)** - See [integrating with Astro](#integrating-with-astro) for more details on how to set up an Astro project with Contentful.

### Setting up a Contentful model

[Section titled “Setting up a Contentful model”](#setting-up-a-contentful-model)

Inside your Contentful space, in the **Content model** section, create a new content model with the following fields and values:

* **Name:** Blog Post
* **API identifier:** `blogPost`
* **Description:** This content type is for a blog post

In your newly created content type, use the **Add Field** button to add 5 new fields with the following parameters:

1. Text field

   * **Name:** title
   * **API identifier:** `title` (leave the other parameters as their defaults)

2. Date and time field

   * **Name:** date
   * **API identifier:** `date`

3. Text field

   * **Name:** slug
   * **API identifier:** `slug` (leave the other parameters as their defaults)

4. Text field

   * **Name:** description
   * **API identifier:** `description`

5. Rich text field

   * **Name:** content
   * **API identifier:** `content`

Click **Save** to save your changes.

In the **Content** section of your Contentful space, create a new entry by clicking the **Add Entry** button. Then, fill in the fields:

* **Title:** `Astro is amazing!`
* **Slug:** `astro-is-amazing`
* **Description:** `Astro is a new static site generator that is blazing fast and easy to use.`
* **Date:** `2022-10-05`
* **Content:** `This is my first blog post!`

Click **Publish** to save your entry. You have just created your first blog post.

Feel free to add as many blog posts as you want, then switch to your favorite code editor to start hacking with Astro!

### Displaying a list of blog posts

[Section titled “Displaying a list of blog posts”](#displaying-a-list-of-blog-posts)

Create a new interface called `BlogPost` and add it to your `contentful.ts` file in `src/lib/`. This interface will match the fields of your blog post content type in Contentful. You will use it to type your blog post entries response.

src/lib/contentful.ts

```diff
import * as contentful from "contentful";
import type { EntryFieldTypes } from "contentful";


+export interface BlogPost {
+  contentTypeId: "blogPost",
+  fields: {
+    title: EntryFieldTypes.Text
+    content: EntryFieldTypes.RichText,
+    date: EntryFieldTypes.Date,
+    description: EntryFieldTypes.Text,
+    slug: EntryFieldTypes.Text
+  }
+}


export const contentfulClient = contentful.createClient({
  space: import.meta.env.CONTENTFUL_SPACE_ID,
  accessToken: import.meta.env.DEV
    ? import.meta.env.CONTENTFUL_PREVIEW_TOKEN
    : import.meta.env.CONTENTFUL_DELIVERY_TOKEN,
  host: import.meta.env.DEV ? "preview.contentful.com" : "cdn.contentful.com",
});
```

Next, go to the Astro page where you will fetch data from Contentful. We will use the home page `index.astro` in `src/pages/` in this example.

Import `BlogPost` interface and `contentfulClient` from `src/lib/contentful.ts`.

Fetch all the entries from Contentful with a content type of `blogPost` while passing the `BlogPost` interface to type your response.

src/pages/index.astro

```astro
---
import { contentfulClient } from "../lib/contentful";
import type { BlogPost } from "../lib/contentful";


const entries = await contentfulClient.getEntries<BlogPost>({
  content_type: "blogPost",
});
---
```

This fetch call will return an array of your blog posts at `entries.items`. You can use `map()` to create a new array (`posts`) that formats your returned data.

The example below returns the `items.fields` properties from our Content model to create a blog post preview, and at the same time, reformats the date to a more readable format.

src/pages/index.astro

```diff
---
import { contentfulClient } from "../lib/contentful";
import type { BlogPost } from "../lib/contentful";


const entries = await contentfulClient.getEntries<BlogPost>({
  content_type: "blogPost",
});


+const posts = entries.items.map((item) => {
  const { title, date, description, slug } = item.fields;
  return {
    +title,
    +slug,
    +description,
    date: new Date(date).toLocaleDateString()
  };
+});
---
```

Finally, you can use `posts` in your template to show a preview of each blog post.

src/pages/index.astro

```diff
---
import { contentfulClient } from "../lib/contentful";
import type { BlogPost } from "../lib/contentful";


const entries = await contentfulClient.getEntries<BlogPost>({
  content_type: "blogPost",
});


const posts = entries.items.map((item) => {
  const { title, date, description, slug } = item.fields;
  return {
    title,
    slug,
    description,
    date: new Date(date).toLocaleDateString()
  };
});
---
<html lang="en">
  <head>
    <title>My Blog</title>
  </head>
  <body>
    <h1>My Blog</h1>
    <ul>
      +{posts.map((post) => (
        <li>
          <a href={`/posts/${post.slug}/`}>
            <h2>{post.title}</h2>
          </a>
          <time>{post.date}</time>
          <p>{post.description}</p>
        </li>
+      ))}
    </ul>
  </body>
</html>
```

### Generating individual blog posts

[Section titled “Generating individual blog posts”](#generating-individual-blog-posts)

Use the same method to fetch your data from Contentful as above, but this time, on a page that will create a unique page route for each blog post.

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

If you’re using Astro’s default static mode, you’ll use [dynamic routes](/en/guides/routing/#dynamic-routes) and the `getStaticPaths()` function. This function will be called at build time to generate the list of paths that become pages.

Create a new file named `[slug].astro` in `src/pages/posts/`.

As you did on `index.astro`, import the `BlogPost` interface and `contentfulClient` from `src/lib/contentful.ts`.

This time, fetch your data inside a `getStaticPaths()` function.

src/pages/posts/\[slug].astro

```astro
---
import { contentfulClient } from "../../lib/contentful";
import type { BlogPost } from "../../lib/contentful";


export async function getStaticPaths() {
  const entries = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
  });
}
---
```

Then, map each item to an object with a `params` and `props` property. The `params` property will be used to generate the URL of the page and the `props` property will be passed to the page component as props.

src/pages/posts/\[slug].astro

```diff
---
import { contentfulClient } from "../../lib/contentful";
+import { documentToHtmlString } from "@contentful/rich-text-html-renderer";
import type { BlogPost } from "../../lib/contentful";


export async function getStaticPaths() {
  const entries = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
  });


  +const pages = entries.items.map((item) => ({
    params: { slug: item.fields.slug },
    props: {
      title: item.fields.title,
      content: documentToHtmlString(item.fields.content),
      date: new Date(item.fields.date).toLocaleDateString(),
    },
  }));
  +return pages;
}
---
```

The property inside `params` must match the name of the dynamic route. Since our filename is `[slug].astro`, we use `slug`.

In our example, the `props` object passes three properties to the page:

* title (a string)
* content (a rich text Document converted to HTML using `documentToHtmlString`)
* date (formatted using the `Date` constructor)

Finally, you can use the page `props` to display your blog post.

src/pages/posts/\[slug].astro

```diff
---
import { contentfulClient } from "../../lib/contentful";
import { documentToHtmlString } from "@contentful/rich-text-html-renderer";
import type { BlogPost } from "../../lib/contentful";


export async function getStaticPaths() {
  const { items } = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
  });
  const pages = items.map((item) => ({
    params: { slug: item.fields.slug },
    props: {
      title: item.fields.title,
      content: documentToHtmlString(item.fields.content),
      date: new Date(item.fields.date).toLocaleDateString(),
    },
  }));
  return pages;
}


+const { content, title, date } = Astro.props;
---
<html lang="en">
  <head>
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <time>{date}</time>
    <article set:html={content} />
  </body>
</html>
```

Navigate to <http://localhost:4321/> and click on one of your posts to make sure your dynamic route is working!

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If you’ve [opted into on-demand rendering with an adapter](/en/guides/on-demand-rendering/), you will use a dynamic route that uses a `slug` parameter to fetch the data from Contentful.

Create a `[slug].astro` page in `src/pages/posts`. Use [`Astro.params`](/en/reference/api-reference/#params) to get the slug from the URL, then pass that to `getEntries`:

src/pages/posts/\[slug].astro

```astro
---
import { contentfulClient } from "../../lib/contentful";
import type { BlogPost } from "../../lib/contentful";


const { slug } = Astro.params;


const data = await contentfulClient.getEntries<BlogPost>({
  content_type: "blogPost",
  "fields.slug": slug,
});
---
```

If the entry is not found, you can redirect the user to the 404 page using [`Astro.redirect`](/en/guides/routing/#dynamic-redirects).

src/pages/posts/\[slug].astro

```diff
---
import { contentfulClient } from "../../lib/contentful";
import type { BlogPost } from "../../lib/contentful";


const { slug } = Astro.params;


+try {
  const data = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
    "fields.slug": slug,
  });
+} catch (error) {
  +return Astro.redirect("/404");
+}
---
```

To pass post data to the template section, create a `post` object outside the `try/catch` block.

Use `documentToHtmlString` to convert `content` from a Document to HTML, and use the Date constructor to format the date. `title` can be left as-is. Then, add these properties to your `post` object.

src/pages/posts/\[slug].astro

```diff
---
import Layout from "../../layouts/Layout.astro";
import { contentfulClient } from "../../lib/contentful";
import { documentToHtmlString } from "@contentful/rich-text-html-renderer";
import type { BlogPost } from "../../lib/contentful";


+let post;
const { slug } = Astro.params;
try {
  const data = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
    "fields.slug": slug,
  });
  +const { title, date, content } = data.items[0].fields;
+  post = {
+    title,
+    date: new Date(date).toLocaleDateString(),
+    content: documentToHtmlString(content),
+  };
} catch (error) {
  return Astro.redirect("/404");
}
---
```

Finally, you can reference `post` to display your blog post in the template section.

src/pages/posts/\[slug].astro

```diff
---
import Layout from "../../layouts/Layout.astro";
import { contentfulClient } from "../../lib/contentful";
import { documentToHtmlString } from "@contentful/rich-text-html-renderer";
import type { BlogPost } from "../../lib/contentful";


let post;
const { slug } = Astro.params;
try {
  const data = await contentfulClient.getEntries<BlogPost>({
    content_type: "blogPost",
    "fields.slug": slug,
  });
  const { title, date, content } = data.items[0].fields;
  post = {
    title,
    date: new Date(date).toLocaleDateString(),
    content: documentToHtmlString(content),
  };
} catch (error) {
  return Astro.redirect("/404");
}
---
<html lang="en">
  <head>
    <title>{post?.title}</title>
  </head>
  <body>
    <h1>{post?.title}</h1>
    <time>{post?.date}</time>
    <article set:html={post?.content} />
  </body>
</html>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Contentful changes

[Section titled “Rebuild on Contentful changes”](#rebuild-on-contentful-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Contentful events.

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

##### Adding a webhook to Contentful

[Section titled “Adding a webhook to Contentful”](#adding-a-webhook-to-contentful)

In your Contentful space **settings**, click on the **Webhooks** tab and create a new webhook by clicking the **Add Webhook** button. Provide a name for your webhook and paste the webhook URL you copied in the previous section. Finally, hit **Save** to create the webhook.

Now, whenever you publish a new blog post in Contentful, a new build will be triggered and your blog will be updated.

# Cosmic & Astro

> Add content to your Astro project using Cosmic as a CMS

[Cosmic](https://www.cosmicjs.com/) is a [headless CMS](https://www.cosmicjs.com/headless-cms) that provides an admin dashboard to manage content and an API that can integrate with a diverse range of frontend tools.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

1. **An Astro project**- If you’d like to start with a fresh Astro project, read the [installation guide](/en/install-and-setup/). This guide follows a simplified version of the [Astro Headless CMS Theme](https://astro.build/themes/details/cosmic-cms-blog/) with [Tailwind CSS](https://tailwindcss.com/) for styling.
2. **A Cosmic account and Bucket** - [Create a free Cosmic account](https://app.cosmicjs.com/signup) if you don’t have one. After creating your account, you’ll be prompted to create a new empty project. There’s also a [Simple Astro Blog template](https://www.cosmicjs.com/marketplace/templates/simple-astro-blog) available (this is the same template as the Astro Headless CMS Theme) to automatically import all of the content used in this guide.
3. **Your Cosmic API keys** - From your Cosmic dashboard, you will need to locate both the **Bucket slug** and **Bucket read key** in order to connect to Cosmic.

## Integrating Cosmic with Astro

[Section titled “Integrating Cosmic with Astro”](#integrating-cosmic-with-astro)

### Installing Necessary Dependencies

[Section titled “Installing Necessary Dependencies”](#installing-necessary-dependencies)

Add the [Cosmic JavaScript SDK](https://www.npmjs.com/package/@cosmicjs/sdk) to fetch data from your Cosmic Bucket.

* npm

  ```shell
  npm install @cosmicjs/sdk
  ```

* pnpm

  ```shell
  pnpm add @cosmicjs/sdk
  ```

* Yarn

  ```shell
  yarn add @cosmicjs/sdk
  ```

### Configuring API Keys

[Section titled “Configuring API Keys”](#configuring-api-keys)

Create a `.env` file at the root of your Astro project (if it does not already exist). Add both the **Bucket slug** and **Bucket read key** available from your Cosmic dashboard as public environment variables.

.env

```ini
PUBLIC_COSMIC_BUCKET_SLUG=YOUR_BUCKET_SLUG
PUBLIC_COSMIC_READ_KEY=YOUR_READ_KEY
```

## Fetching Data from Cosmic

[Section titled “Fetching Data from Cosmic”](#fetching-data-from-cosmic)

1. Create a new file called `cosmic.js`. Place this file inside of the `src/lib` folder in your project.

2. Add the following code to fetch data from Cosmic using the SDK and your environment variables.

   The example below creates a function called `getAllPosts()` to fetch metadata from Cosmic `posts` objects:

   src/lib/cosmic.js

   ```js
   import { createBucketClient } from '@cosmicjs/sdk'


   const cosmic = createBucketClient({
     bucketSlug: import.meta.env.PUBLIC_COSMIC_BUCKET_SLUG,
     readKey: import.meta.env.PUBLIC_COSMIC_READ_KEY
   })


   export async function getAllPosts() {
     const data = await cosmic.objects
       .find({
         type: 'posts'
       })
       .props('title,slug,metadata,created_at')
     return data.objects
   }
   ```

   Read more about [queries in the Cosmic documentation](https://www.cosmicjs.com/docs/api/queries).

3. Import your query function in a `.astro` component. After fetching data, the results from the query can be used in your Astro template.

   The following example shows fetching metadata from Cosmic `posts` and passing these values as props to a `<Card />` component to create a list of blog posts:

   src/pages/index.astro

   ```astro
   ---
   import Card from '../components/Card.astro'
   import { getAllPosts } from '../lib/cosmic'


   const data = await getAllPosts()
   ---


   <section>
     <ul class="grid gap-8 md:grid-cols-2">
       {
         data.map((post) => (
           <Card
             title={post.title}
             href={post.slug}
             body={post.metadata.excerpt}
             tags={post.metadata.tags.map((tag) => tag)}
           />
         ))
       }
     </ul>
   </section>
   ```

   [View source code for the Card component](https://github.com/cosmicjs/simple-astro-blog/blob/main/src/components/Card.astro)

## Building a Blog with Astro and Cosmic

[Section titled “Building a Blog with Astro and Cosmic”](#building-a-blog-with-astro-and-cosmic)

You can manage your Astro blog’s content using Cosmic and create webhooks to automatically redeploy your website when you update or add new content.

### Cosmic Content Objects

[Section titled “Cosmic Content Objects”](#cosmic-content-objects)

The following instructions assume that you have an **Object Type** in Cosmic called **posts**. Each individual blog post is a `post` that is defined in the Cosmic dashboard with the following Metafields:

1. **Text input** - Author
2. **Image** - Cover Image
3. **Repeater** - Tags
   * **Text input** - Title
4. **Text area** - Excerpt
5. **Rich Text** - Content

### Displaying a List of Blog Posts in Astro

[Section titled “Displaying a List of Blog Posts in Astro”](#displaying-a-list-of-blog-posts-in-astro)

Using the same [data-fetching method](#fetching-data-from-cosmic) as above, import the `getAllPosts()` query from your script file and await the data. This function provides metadata about each `post` which can be displayed dynamically.

The example below passes these values to a `<Card />` component to display a formatted list of blog posts:

src/pages/index.astro

```astro
---
import Card from '../components/Card.astro'
import { getAllPosts } from '../lib/cosmic'


const data = await getAllPosts()
---


<section>
  <ul class="grid gap-8 md:grid-cols-2">
    {
      data.map((post) => (
        <Card
          title={post.title}
          href={post.slug}
          body={post.metadata.excerpt}
          tags={post.metadata.tags.map((tag) => tag)}
        />
      ))
    }
  </ul>
</section>
```

### Generating Individual Blog Posts with Astro

[Section titled “Generating Individual Blog Posts with Astro”](#generating-individual-blog-posts-with-astro)

To generate an individual page with full content for each blog post, create a [dynamic routing page](/en/guides/routing/#dynamic-routes) at `src/pages/blog/[slug].astro`.

This page will export a `getStaticPaths()` function to generate a page route at the `slug` returned from each `post` object. This function is called at build time and generates and renders all of your blog posts at once.

To access your data from Cosmic:

* Query Cosmic inside of `getStaticPaths()` to fetch data about each post and provide it to the function.
* Use each `post.slug` as a route parameter, creating the URLs for each blog post.
* Return each `post` inside of `Astro.props`, making the post data available to HTML template portion of the page component for rendering.

The HTML markup below uses various data from Cosmic, such as the post title, cover image, and the **rich text content** (full blog post content). Use [set:html](/en/reference/directives-reference/#sethtml) on the element displaying the rich text content from Cosmic to render HTML elements on the page exactly as fetched from Cosmic.

src/pages/blog/\[slug].astro

```astro
---
import { getAllPosts } from '../../lib/cosmic'
import { Image } from 'astro:assets'


export async function getStaticPaths() {
  const data = (await getAllPosts()) || []


  return data.map((post) => {
    return {
      params: { slug: post.slug },
      props: { post }
    }
  })
}


const { post } = Astro.props
---


<article class="mx-auto max-w-screen-md pt-20">
  <section class="border-b pb-8">
    <h1 class="text-4xl font-bold">{post.title}</h1>
    <div class="my-4"></div>
    <span class="text-sm font-semibold">{post.metadata.author?.title}</span>
  </section>
  {
    post.metadata.cover_image && (
      <Image
        src={post.metadata.cover_image.imgix_url}
        format="webp"
        width={1200}
        height={675}
        aspectRatio={16 / 9}
        quality={50}
        alt={`Cover image for the blog ${post.title}`}
        class={'my-12 rounded-md shadow-lg'}
      />
    )
  }
  <div set:html={post.metadata.content} />
</article>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit the [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Cosmic content updates

[Section titled “Rebuild on Cosmic content updates”](#rebuild-on-cosmic-content-updates)

You can set up a webhook in Cosmic directly to trigger a redeploy of your site on your hosting platform (e.g. Vercel) whenever you update or add content Objects.

Under “Settings” > “webhooks”, add the URL endpoint from Vercel and select the Object Type you would like to trigger the webhook. Click “Add webhook” to save it.

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

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/simple-astro-blog.Dl86rePH_ZijHC7.webp) Astro Headless CMS Blog](https://astro.build/themes/details/cosmic-cms-blog/)

# Craft CMS & Astro

> Add content to your Astro project using Craft CMS as a CMS

[Craft CMS](https://craftcms.com/) is a flexible open source CMS with an accessible authoring experience. It includes its own front end, but can also be used as a headless CMS to provide content to your Astro project.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out the official Craft CMS [GraphQL API guide](https://craftcms.com/docs/5.x/development/graphql.html)
* The official documentation for Craft’s [`headlessMode` config setting](https://craftcms.com/docs/5.x/reference/config/general.html#headlessmode)

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [SSG Astro with Headless Craft CMS Content Fetched At Build Time](https://www.olets.dev/posts/ssg-astro-with-headless-craft-cms-content-fetched-at-build-time/)
* [SSG Astro with Headless Craft CMS Content Fetched At Build Time Or Cached In Advance](https://www.olets.dev/posts/ssg-astro-with-headless-craft-cms-content-fetched-at-build-time-or-cached-in-advance/)
* [SSR Astro With Headless Craft CMS](https://www.olets.dev/posts/ssr-astro-with-headless-craft-cms/)

# Craft Cross CMS & Astro

> Add content to your Astro project using Craft Cross CMS

[Craft Cross CMS](https://ecosystem.plaid.co.jp/product/karte-craft/xcms) is an API-based headless CMS from the KARTE ecosystem.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Blog: [Build an Astro Website with Craft Cross CMS](https://solution.karte.io/blog/2025/10/build-website-with-astro-using-xcms/)
* Sample code (GitHub): [Craft Cross CMS with Astro (sample)](https://github.com/plaidev/craft-codes/tree/main/astro/cross-cms-astro-sample)

# Crystallize & Astro

> Add content to your Astro project using Crystallize as a CMS

[Crystallize](https://crystallize.com/) is a headless content management system for eCommerce that exposes a GraphQL API.

## Example

[Section titled “Example”](#example)

src/pages/index.astro

```astro
---
// Fetch your catalogue paths from Crystallize GraphQL API


import BaseLayout from '../../layouts/BaseLayout.astro';
import { createClient } from '@crystallize/js-api-client';


const apiClient = createClient({
  tenantIdentifier: 'furniture'
});


const query = `
  query getCataloguePaths{
    catalogue(language: "en", path: "/shop") {
      name
      children {
        name
        path
      }
    }
  }
`
const { data: { catalogue } } = await apiClient.catalogueApi(query)
---
<BaseLayout>
  <h1>{catalogue.name}</h1>
  <nav>
    <ul>
      {catalogue.children.map(child => (
        <li><a href={child.path}>{child.name}</a></li>
      ))}
    </ul>
  </nav>
</BaseLayout>
```

# DatoCMS & Astro

> Add content to your Astro project using DatoCMS

[DatoCMS](https://datocms.com/) is a web-based, headless CMS to manage digital content for your sites and apps.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this guide, you will fetch content data from DatoCMS in your Astro project, then display it on a page.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

* **An Astro project** - If you don’t have an Astro project yet, you can follow the instructions in our [Installation guide](/en/install-and-setup/).
* **A DatoCMS account and project** - If you don’t have an account, you can [sign up for a free account](https://dashboard.datocms.com/signup).
* **The read-only API Key for your DatoCMS project** - You can find it in the admin dashboard of your project, under “Settings” > “API Tokens”.

## Setting up the credentials

[Section titled “Setting up the credentials”](#setting-up-the-credentials)

Create a new file (if one does not already exist) named `.env` in the root of your Astro project. Add a new environment variable as follows, using the API key found in your DatoCMS admin dashboard:

.env

```ini
DATOCMS_API_KEY=YOUR_API_KEY
```

For TypeScript support, declare the typing of this environment variable in the `env.d.ts` file in the `src/` folder. If this file does not exist, you can create it and add the following:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly DATOCMS_API_KEY: string;
}
```

Your root directory should now include these files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

Learn more about [environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

## Create a Model in DatoCMS

[Section titled “Create a Model in DatoCMS”](#create-a-model-in-datocms)

In the DatoCMS admin dashboard of your project, navigate to “Settings” > “Models” and create a new Model called “Home” with the “Single Instance” toggle selected. This will create a home page for your project. In this model, add a new text field for the page title.

Navigate to the “Content” tab in your project and click on your newly-created home page. You can now add a title. Save the page, and continue.

## Fetching data

[Section titled “Fetching data”](#fetching-data)

In your Astro project, navigate to the page that will fetch and display your CMS content. Add the following query to fetch the content for `home` using the DatoCMS GraphQL API.

This example displays the page title from DatoCMS on `src/pages/index.astro`:

src/pages/index.astro

```astro
---
const response = await fetch('https://graphql.datocms.com/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    Authorization: `Bearer ${import.meta.env.DATOCMS_API_KEY}`,
  },
  body: JSON.stringify({
    query: `query Homepage {
          home {
            title
          }
        }
      `,
  }),
});


const json = await response.json();
const data = json.data.home;
---


<h1>{data.title}</h1>
```

This GraphQL query will fetch the `title` field in the `home` page from your DatoCMS Project. When you refresh your browser, you should see the title on your page.

## Adding Dynamic modular content blocks

[Section titled “Adding Dynamic modular content blocks”](#adding-dynamic-modular-content-blocks)

If your DatosCMS project includes [modular content](https://www.datocms.com/docs/content-modelling/modular-content), then you will need to build a corresponding `.astro` component for each block of content (e.g. a text section, a video, a quotation block, etc.) that the modular field allows in your project.

The example below is a `<Text />` Astro component for displaying a “Multiple-paragraph text” block from DatoCMS.

src/components/Text.astro

```astro
---
export interface TextProps {
  text: string
}


export interface Props {
  item: TextProps
}


const { item } = Astro.props;
---


<div set:html={item.text} />
```

To fetch these blocks, edit your GraphQL query to include the modular content block you created in DatoCMS.

In this example, the modular content block is named **content** in DatoCMS. This query also includes the unique `_modelApiKey` of each item to check which block should be displayed in the modular field, based on which block was chosen by the content author in the DatoCMS editor. Use a switch statement in the Astro template to allow for dynamic rendering based on the data received from the query.

The following example represents a DatoCMS modular content block that allows an author to choose between a text field (`<Text />`) and an image (`<Image />`) rendered on the home page:

src/pages/index.astro

```diff
---
+import Image from '../components/Image.astro';
+import Text from '../components/Text.astro';


const response = await fetch('https://graphql.datocms.com/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    Authorization: `Bearer ${import.meta.env.DATOCMS_API_KEY}`,
  },
  body: JSON.stringify({
    query: `query Homepage {
          home {
            title
            content {
              ... on ImageRecord {
                _modelApiKey
               image{
                url
               }
              }
              ... on TextRecord {
                _modelApiKey
                text(markdown: true)
              }
            }
          }
        }
      `,
  }),
});


const json = await response.json();
const data = json.data.home;
---


<h1>{data.title}</h1>
+{
+  data.content.map((item: any) => {
    +switch (item._modelApiKey) {
      +case 'image':
        +return <Image item={item} />;
      +case 'text':
        +return <Text item={item} />;
      +default:
        +return null;
+    }
+  })
+}
```

## Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Publish on DatoCMS content changes

[Section titled “Publish on DatoCMS content changes”](#publish-on-datocms-content-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build when you change content in DatoCMS.

### Netlify

[Section titled “Netlify”](#netlify)

To set up a webhook in Netlify:

1. Go to your site dashboard and click on **Build & deploy**.

2. Under the **Continuous Deployment** tab, find the **Build hooks** section and click on **Add build hook**.

3. Provide a name for your webhook and select the branch you want to trigger the build on. Click on **Save** and copy the generated URL.

### Vercel

[Section titled “Vercel”](#vercel)

To set up a webhook in Vercel:

1. Go to your project dashboard and click on **Settings**.

2. Under the **Git** tab, find the **Deploy Hooks** section.

3. Provide a name for your webhook and the branch you want to trigger the build on. Click **Add** and copy the generated URL.

### Adding a webhook to DatoCMS

[Section titled “Adding a webhook to DatoCMS”](#adding-a-webhook-to-datocms)

In your DatoCMS project admin dashboard, navigate to the **Settings** tab and click **Webhooks**. Click the plus icon to create a new webhook and give it a name. In the URL field, paste the URL generated by your preferred hosting service. As Trigger, select whichever option suits your needs. (For example: build every time a new record is published.)

## Starter project

[Section titled “Starter project”](#starter-project)

You can also check out the [Astro blog template](https://www.datocms.com/marketplace/starters/astro-template-blog) on the DatoCMS marketplace to learn how to create a blog with Astro and DatoCMS.

# Decap CMS & Astro

> Add content to your Astro project using Decap as a CMS

[Decap CMS](https://www.decapcms.org/) (formerly Netlify CMS) is an open-source, Git-based content management system.

Decap allows you to take full advantage of all of Astro’s features, including image optimization and content collections.

Decap adds a route (typically `/admin`) to your project that will load a React app to allow authorized users to manage content directly from the deployed website. Decap will commit changes directly to your Astro project’s source repository.

## Installing DecapCMS

[Section titled “Installing DecapCMS”](#installing-decapcms)

There are two options for adding Decap to Astro:

1. [Install Decap via a package manager](https://decapcms.org/docs/install-decap-cms/#installing-with-npm) with the following command:

   * npm

     ```shell
     npm install decap-cms-app
     ```

   * pnpm

     ```shell
     pnpm add decap-cms-app
     ```

   * Yarn

     ```shell
     yarn add decap-cms-app
     ```

2. Import the package into a `<script>` tag in your page `<body>`

   /admin

   ```html
   <body>
     <!-- Include the script that builds the page and powers Decap CMS -->
     <script src="https://unpkg.com/decap-cms@^3.1.2/dist/decap-cms.js"></script>
   </body>
   ```

## Configuration

[Section titled “Configuration”](#configuration)

1. Create a static admin folder at `public/admin/`

2. Add `config.yml` to `public/admin/`:

   * public

     * admin

       * config.yml

3. To add support for content collections, configure each schema in `config.yml`. The following example configures a `blog` collection, defining a `label` for each entry’s frontmatter property:

   /public/admin/config.yml

   ```yml
   collections:
     - name: "blog" # Used in routes, e.g., /admin/collections/blog
       label: "Blog" # Used in the UI
       folder: "src/content/blog" # The path to the folder where the documents are stored
       create: true # Allow users to create new documents in this collection
       fields: # The fields for each document, usually in frontmatter
         - { label: "Layout", name: "layout", widget: "hidden", default: "blog" }
         - { label: "Title", name: "title", widget: "string" }
         - { label: "Publish Date", name: "date", widget: "datetime" }
         - { label: "Featured Image", name: "thumbnail", widget: "image" }
         - { label: "Rating (scale of 1-5)", name: "rating", widget: "number" }
         - { label: "Body", name: "body", widget: "markdown" }
   ```

4. Add the `admin` route for your React app in `src/pages/admin.html`.

   * public

     * admin

       * config.yml

   * src

     * pages

       * admin.html

   /src/pages/admin.html

   ```html
   <!doctype html>
   <html lang="en">
     <head>
       <meta charset="utf-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <meta name="robots" content="noindex" />
       <link href="/admin/config.yml" type="text/yaml" rel="cms-config-url" />
       <title>Content Manager</title>
     </head>
     <body>
       <script src="https://unpkg.com/decap-cms@^3.1.2/dist/decap-cms.js"></script>
     </body>
   </html>
   ```

5. To enable media uploads to a specific folder via the Decap editor, add an appropriate path:

   /public/admin/config.yml

   ```yml
   media_folder: "src/assets/images" # Location where files will be stored in the repo
   public_folder: "src/assets/images" # The src attribute for uploaded media
   ```

See [the Decap CMS configuration documentation](https://decapcms.org/docs/configure-decap-cms/) for full instructions and options.

## Usage

[Section titled “Usage”](#usage)

Navigate to `yoursite.com/admin/` to use the Decap CMS editor.

## Authentication

[Section titled “Authentication”](#authentication)

### Decap CMS with Netlify Identity

[Section titled “Decap CMS with Netlify Identity”](#decap-cms-with-netlify-identity)

Decap CMS was originally developed by Netlify and has first class support for [Netlify Identity](https://docs.netlify.com/security/secure-access-to-sites/identity/).

When deploying to Netlify, configure Identity for your project via the Netlify dashboard and include the [Netlify Identity Widget](https://github.com/netlify/netlify-identity-widget) on the `admin` route of your project. Optionally include the Identity Widget on the homepage of your site if you plan to invite new users via email.

### Decap CMS with External OAuth Clients

[Section titled “Decap CMS with External OAuth Clients”](#decap-cms-with-external-oauth-clients)

When deploying to hosting providers other than Netlify, you must create your own OAuth routes.

In Astro, this can be done with on-demand rendered routes in your project configured with [an adapter](/en/guides/on-demand-rendering/) enabled.

See [Decap’s OAuth Docs](https://decapcms.org/docs/external-oauth-clients/) for a list of compatible community-maintained OAuth clients.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* Netlify Identity Template: [astro-decap-ssg-netlify](https://github.com/OliverSpeir/astro-decap-ssg-netlify-identity)

* On-demand rendering OAuth Routes with Astro Template: [astro-decap-starter-ssr](https://github.com/OliverSpeir/astro-decap-starter-ssr)

* Blog Post: [Author your Astro site’s content with Git-based CMSs](https://aalam.vercel.app/blog/astro-and-git-cms-netlify) by Aftab Alam

* Youtube Tutorial: [Create a Custom Blog with Astro & NetlifyCMS in MINUTES!](https://www.youtube.com/watch?v=3yip2wSRX_4) by Kumail Pirzada

## Production Sites

[Section titled “Production Sites”](#production-sites)

The following sites use Astro + Decap CMS in production:

* [yunielacosta.com](https://www.yunielacosta.com/) by Yuniel Acosta — [source code on GitHub](https://github.com/yacosta738/yacosta738.github.io) (Netlify CMS)
* [portfolioris.nl](https://www.portfolioris.nl/) by Joris Hulsbosch – [source code on GitHub](https://github.com/portfolioris/portfolioris.nl)

## Themes

[Section titled “Themes”](#themes)

* [![](/_astro/astros.CA8z6dbD_Z1fUXSm.webp) Astros](https://astro.build/themes/details/astros)
* [![](/_astro/enhanced-astro-starter.BDAzOMVv_ghcL4.webp) Enhanced Astro Starter](https://astro.build/themes/details/enhanced-astro-starter)
* [![](/_astro/astro-decap-starter.CuC8RtgM_IaqHQ.webp) Astro Decap CMS Starter](https://astro.build/themes/details/astro-decap-cms-starter)

# Directus & Astro

> Add content to your Astro project using Directus as a CMS

[Directus](https://directus.io/) is a backend-as-a-service which can be used to host data and content for your Astro project.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Getting Started with Directus and Astro](https://docs.directus.io/blog/getting-started-directus-astro.html).

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Using Directus CMS with Neon Postgres and Astro to build a blog ](https://neon.tech/guides/directus-cms)

Have a resource to share?

If you found (or made!) a helpful video or blog post about using Directus with Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/directus.mdx)!

# Drupal & Astro

> Add content to your Astro project using Drupal as a CMS

[Drupal](https://www.drupal.org/) is an open-source content management tool.

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A Drupal site** - If you haven’t set up a Drupal site, you can follow the official guidelines [Installing Drupal](https://www.drupal.org/docs/getting-started/installing-drupal).

## Integrating Drupal with Astro

[Section titled “Integrating Drupal with Astro”](#integrating-drupal-with-astro)

### Installing the JSON:API Drupal module

[Section titled “Installing the JSON:API Drupal module”](#installing-the-jsonapi-drupal-module)

To be able to get content from Drupal you need to enable the [Drupal JSON:API module](https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module).

1. Navigate to the Extend page `admin/modules` via the Manage administrative menu
2. Locate the JSON:API module and check the box next to it
3. Click Install to install the new module

Now you can make `GET` requests to your Drupal application through JSON:API.

### Adding the Drupal URL in `.env`

[Section titled “Adding the Drupal URL in .env”](#adding-the-drupal-url-in-env)

To add your Drupal URL to Astro, create a `.env` file in the root of your project (if one does not already exist) and add the following variable:

.env

```ini
DRUPAL_BASE_URL="https://drupal.ddev.site/"
```

Restart the dev server to use this environment variable in your Astro project.

### Setting up Credentials

[Section titled “Setting up Credentials”](#setting-up-credentials)

By default, the Drupal JSON:API endpoint is accessible for external data-fetching requests without requiring authentication. This allows you to fetch data for your Astro project without credentials but it does not permit users to modify your data or site settings.

However, if you wish to restrict access and require authentication, Drupal provides [several authentication methods](https://www.drupal.org/docs/contributed-modules/api-authentication) including:

* [Basic Authentication](https://www.drupal.org/docs/contributed-modules/api-authentication/setup-basic-authentication)
* [API Key-based authentication](https://www.drupal.org/docs/contributed-modules/api-authentication/api-key-authentication)
* [Access Token/OAuth-based authentication](https://www.drupal.org/docs/contributed-modules/api-authentication/setup-access-token-oauth-based-authentication)
* [JWT Token-based authentication](https://www.drupal.org/docs/contributed-modules/api-authentication/jwt-authentication)
* [Third-Party Provider token authentication](https://www.drupal.org/docs/contributed-modules/api-authentication/rest-api-authentication-using-external-identity-provider)

You can add your credentials to your `.env` file.

.env

```ini
DRUPAL_BASIC_USERNAME="editor"
DRUPAL_BASIC_PASSWORD="editor"
DRUPAL_JWT_TOKEN="abc123"
...
```

Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your root directory should now include this new files:

* **.env**
* astro.config.mjs
* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

JSON:API requests and responses can often be complex and deeply nested. To simplify working with them, you can use two npm packages that streamline both the requests and the handling of responses:

* [`JSONA`](https://www.npmjs.com/package/jsona): JSON API v1.0 specification serializer and deserializer for use on the server and in the browser.
* [`Drupal JSON-API Params`](https://www.npmjs.com/package/drupal-jsonapi-params): This module provides a helper Class to create the required query. While doing so, it also tries to optimise the query by using the short form, whenever possible.

- npm

  ```shell
  npm install jsona drupal-jsonapi-params
  ```

- pnpm

  ```shell
  pnpm add jsona drupal-jsonapi-params
  ```

- Yarn

  ```shell
  yarn add jsona drupal-jsonapi-params
  ```

## Fetching data from Drupal

[Section titled “Fetching data from Drupal”](#fetching-data-from-drupal)

Your content is fetched from a JSON:API URL.

### Drupal JSON:API URL structure

[Section titled “Drupal JSON:API URL structure”](#drupal-jsonapi-url-structure)

The basic URL structure is: `/jsonapi/{entity_type_id}/{bundle_id}`

The URL is always prefixed by `jsonapi`.

* The `entity_type_id` refers to the Entity Type, such as node, block, user, etc.
* The `bundle_id` refers to the Entity Bundles. In the case of a Node entity type, the bundle could be article.
* In this case, to get the list of all articles, the URL will be `[DRUPAL_BASE_URL]/jsonapi/node/article`.

To retrieve an individual entity, the URL structure will be `/jsonapi/{entity_type_id}/{bundle_id}/{uuid}`, where the uuid is the UUID of the entity. For example the URL to get a specific article will be of the form `/jsonapi/node/article/2ee9f0ef-1b25-4bbe-a00f-8649c68b1f7e`.

#### Retrieving only certain fields

[Section titled “Retrieving only certain fields”](#retrieving-only-certain-fields)

Retrieve only certain field by adding the Query String field to the request.

GET: `/jsonapi/{entity_type_id}/{bundle_id}?field[entity_type]=field_list`

Examples:

* `/jsonapi/node/article?fields[node--article]=title,created`
* `/jsonapi/node/article/2ee9f0ef-1b25-4bbe-a00f-8649c68b1f7e?fields[node--article]=title,created,body`

#### Filtering

[Section titled “Filtering”](#filtering)

Add a filter to your request by adding the filter Query String.

The simplest, most common filter is a key-value filter:

GET: `/jsonapi/{entity_type_id}/{bundle_id}?filter[field_name]=value&filter[field_other]=value`

Examples:

* `/jsonapi/node/article?filter[title]=Testing JSON:API&filter[status]=1`
* `/jsonapi/node/article/2ee9f0ef-1b25-4bbe-a00f-8649c68b1f7e?fields[node--article]=title&filter[title]=Testing JSON:API`

You can find more query options in the [JSON:API Documentation](https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module).

### Building a Drupal query

[Section titled “Building a Drupal query”](#building-a-drupal-query)

Astro components can fetch data from your Drupal site by using `drupal-jsonapi-params` package to build the query.

The following example shows a component with a query for an “article” content type that has a text field for a title and a rich text field for content:

```astro
---
import {Jsona} from "jsona";
import {DrupalJsonApiParams} from "drupal-jsonapi-params";
import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


// Get the Drupal base URL
export const baseUrl: string = import.meta.env.DRUPAL_BASE_URL;


// Generate the JSON:API Query. Get all title and body from published articles.
const params: DrupalJsonApiParams = new DrupalJsonApiParams();
params.addFields("node--article", [
        "title",
        "body",
    ])
    .addFilter("status", "1");
// Generates the query string.
const path: string = params.getQueryString();
const url: string = baseUrl + '/jsonapi/node/article?' + path;


// Get the articles
const request: Response = await fetch(url);
const json: string | TJsonApiBody = await request.json();
// Initiate Jsona.
const dataFormatter: Jsona = new Jsona();
// Deserialise the response.
const articles = dataFormatter.deserialize(json);
---
<body>
 {articles?.length ? articles.map((article: any) => (
    <section>
      <h2>{article.title}</h2>
      <article set:html={article.body.value}></article>
    </section>
 )): <div><h1>No Content found</h1></div> }
</body>
```

You can find more querying options in the [Drupal JSON:API Documentation](https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module/jsonapi)

## Making a blog with Astro and Drupal

[Section titled “Making a blog with Astro and Drupal”](#making-a-blog-with-astro-and-drupal)

With the setup above, you are now able to create a blog that uses Drupal as the CMS.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. **An Astro project** with [`JSONA`](https://www.npmjs.com/package/jsona) and [`Drupal JSON-API Params`](https://www.npmjs.com/package/drupal-jsonapi-params) installed.

2. **A Drupal site with at least one entry** - For this tutorial we recommend starting with a new Drupal site with Standard installation.

   In the **Content** section of your Drupal site, create a new entry by clicking the **Add** button. Then, choose Article and fill in the fields:

   * **Title:** `My first article for Astro!`
   * **Alias:** `/articles/first-article-for astro`
   * **Description:** `This is my first Astro article! Let's see what it will look like!`

   Click **Save** to create your first Article. Feel free to add as many articles as you want.

### Displaying a list of articles

[Section titled “Displaying a list of articles”](#displaying-a-list-of-articles)

1. Create `src/types.ts` if it does not already exist and add two new interfaces called `DrupalNode` and `Path` with the following code. These interfaces will match the fields of your article content type in Drupal and the Path fields. You will use it to type your article entries response.

   src/types.ts

   ```ts
   export interface Path {
       alias: string
       pid: number
       langcode: string
   }


   export interface DrupalNode extends Record<string, any> {
       id: string
       type: string
       langcode: string
       status: boolean
       drupal_internal__nid: number
       drupal_internal__vid: number
       changed: string
       created: string
       title: string
       default_langcode: boolean
       sticky: boolean
       path: Path
   }
   ```

   Your src directory should now include the new file:

   * .env

   * astro.config.mjs

   * package.json

   * src/

     * **types.ts**

2. Create a new file called `drupal.ts` under `src/api` and add the following code:

   src/api/drupal.ts

   ```ts
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {DrupalNode} from "../types.ts";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   // Get the Drupal Base Url.
   export const baseUrl: string = import.meta.env.DRUPAL_BASE_URL;
   ```

   This will import the required libraries such as `Jsona` to deserialize the response, `DrupalJsonApiParams` to format the request url and the Node and Jsona types. It will also get the `baseUrl` from the `.env` file.

   Your src/api directory should now include the new file:

   * .env

   * astro.config.mjs

   * package.json

   * src/

     * api/

       * **drupal.ts**

     * types.ts

3. In that same file, create the `fetchUrl` function to make the fetch request and deserialize the response.

   src/api/drupal.ts

   ```diff
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {DrupalNode} from "../types.ts";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   // Get the Drupal Base Url.
   export const baseUrl: string = import.meta.env.DRUPAL_BASE_URL;


   +/**
    * Fetch url from Drupal.
    *
    * @param url
    *
    * @return Promise<TJsonaModel | TJsonaModel[]> as Promise<any>
    */
   +export const fetchUrl = async (url: string): Promise<any> => {
       const request: Response = await fetch(url);
       const json: string | TJsonApiBody = await request.json();
       const dataFormatter: Jsona = new Jsona();
       return dataFormatter.deserialize(json);
   +}
   ```

4. Create the `getArticles()` function to get all published articles.

   src/api/drupal.ts

   ```diff
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {DrupalNode} from "../types.ts";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   // Get the Drupal Base Url.
   export const baseUrl: string = import.meta.env.DRUPAL_BASE_URL;


   /**
    * Fetch url from Drupal.
    *
    * @param url
    *
    * @return Promise<TJsonaModel | TJsonaModel[]> as Promise<any>
    */
   export const fetchUrl = async (url: string): Promise<any> => {
       const request: Response = await fetch(url);
       const json: string | TJsonApiBody = await request.json();
       const dataFormatter: Jsona = new Jsona();
       return dataFormatter.deserialize(json);
   }


   +/**
    * Get all published articles.
    *
    * @return Promise<DrupalNode[]>
    */
   +export const getArticles = async (): Promise<DrupalNode[]> => {
       const params: DrupalJsonApiParams = new DrupalJsonApiParams();
       +params
           .addFields("node--article", [
               +"title",
               +"path",
               +"body",
               +"created",
   +        ])
           .addFilter("status", "1");
       const path: string = params.getQueryString();
       return await fetchUrl(baseUrl + '/jsonapi/node/article?' + path);
   +}
   ```

   Now you can use the function `getArticles()` in an `.astro` component to get all published articles with data for each title, body, path and creation date.

5. Go to the Astro page where you will fetch data from Drupal. The following example creates an articles landing page at `src/pages/articles/index.astro`.

   Import the necessary dependencies and fetch all the entries from Drupal with a content type of `article` using `getArticles()` while passing the `DrupalNode` interface to type your response.

   src/pages/articles/index.astro

   ```astro
   ---
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   import type { DrupalNode } from "../../types";
   import {getArticles} from "../../api/drupal";


   // Get all published articles.
   const articles = await getArticles();
   ---
   ```

   This fetch call using getArticles() will return a typed array of entries that can be used in your page template.

   Your `src/pages/` directory should now include the new file, if you used the same page file:

   * .env

   * astro.config.mjs

   * package.json

   * src/

     * api/

       * drupal.ts

     * pages/

       * articles/

         * **index.astro**

     * types.ts

6. Add content to your page, such as a title. Use `articles.map()` to show your Drupal entries as line items in a list.

   src/pages/articles/index.astro

   ```diff
   ---
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   import type { DrupalNode } from "../types";
   import {getArticles} from "../api/drupal";


   // Get all published articles.
   const articles = await getArticles();
   ---
   <html lang="en">
     <head>
       <title>My news site</title>
     </head>
     <body>
       <h1>My news site</h1>
       <ul>
         +{articles.map((article: DrupalNode) => (
           <li>
             <a href={article.path.alias.replace("internal:en/", "")}>
               <h2>{article.title}</h2>
               <p>Published on {article.created}</p>
             </a>
           </li>
   +      ))}
       </ul>
     </body>
   </html>
   ```

### Generating individual blog posts

[Section titled “Generating individual blog posts”](#generating-individual-blog-posts)

Use the same method to fetch your data from Drupal as above, but this time, on a page that will create a unique page route for each article.

This example uses Astro’s default static mode, and creates [a dynamic routing page file](/en/guides/routing/#dynamic-routes) with the `getStaticPaths()` function. This function will be called at build time to generate the list of paths that become pages.

1. Create a new file `src/pages/articles/[path].astro` and import the `DrupalNode` interface and `getArticle()` from `src/api/drupal.ts`. Fetch your data inside a `getStaticPaths()` function to create routes for your blog.

   src/pages/articles/\[path].astro

   ```astro
   ---
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   import type { DrupalNode } from "../../types";
   import {getArticles} from "../../api/drupal";


   // Get all published articles.
   export async function getStaticPaths() {
     const articles = await getArticles();
   }
   ---
   ```

   Your src/pages/articles directory should now include the new file:

   * .env

   * astro.config.mjs

   * package.json

   * src/

     * api/

       * drupal.ts

     * pages/

       * articles/

         * index.astro
         * **\[path].astro**

     * types.ts

2. In the same file, map each Drupal entry to an object with a `params` and `props` property. The `params` property will be used to generate the URL of the page and the `props` values will be passed to the page component as props.

   src/pages/articles/\[path].astro

   ```diff
   ---
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   import type { DrupalNode } from "../../types";
   import {getArticles} from "../../api/drupal";


   // Get all published articles.
   export async function getStaticPaths() {
       const articles = await getArticles();
       +return articles.map((article: DrupalNode) => {
           +return {
   +            params: {
                   +// Choose `path` to match the `[path]` routing value
   +                path: article.path.alias.split('/')[2]
   +            },
   +            props: {
   +                title: article.title,
   +                body: article.body,
   +                date: new Date(article.created).toLocaleDateString('en-EN', {
   +                    day: "numeric",
   +                    month: "long",
   +                    year: "numeric"
   +                })
   +            }
   +        }
   +    });
   +}
   +---
   ```

   The property inside `params` must match the name of the dynamic route. Since the filename is `[path].astro`, the property name passed to `params` must be `path`.

   In our example, the `props` object passes three properties to the page:

   * `title`: a string, representing the title of your post.
   * `body`: a string, representing the content of your entry.
   * `date`: a timestamp, based on your file creation date.

3. Use the page `props` to display your blog post.

   src/pages/articles/\[path].astro

   ```diff
   ---
   import {Jsona} from "jsona";
   import {DrupalJsonApiParams} from "drupal-jsonapi-params";
   import type {TJsonApiBody} from "jsona/lib/JsonaTypes";


   import type { DrupalNode } from "../../types";
   import {getArticles} from "../../api/drupal";


   // Get all published articles.
   export async function getStaticPaths() {
       const articles = await getArticles();
       return articles.map((article: DrupalNode) => {
           return {
               params: {
                   path: article.path.alias.split('/')[2]
               },
               props: {
                   title: article.title,
                   body: article.body,
                   date: new Date(article.created).toLocaleDateString('en-EN', {
                       day: "numeric",
                       month: "long",
                       year: "numeric"
                   })
               }
           }
       });
   }


   +const {title, date, body} = Astro.props;
   ---
   <html lang="en">
     <head>
       <title>{title}</title>
     </head>
     <body>
       <h1>{title}</h1>
       <time>{date}</time>
       <article set:html={body.value} />
     </body>
   </html>
   ```

4. Navigate to your dev server preview and click on one of your posts to make sure your dynamic route is working.

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Create a web application with Astro and Drupal ](https://www.linkedin.com/pulse/create-web-application-astrojs-website-generator-using-gambino-kx6cf)

Have a resource to share?

If you found (or made!) a helpful video or blog post about using Drupal with Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/drupal.mdx)!

# Flotiq & Astro

> Add content to your Astro project using Flotiq as a CMS

[Flotiq](https://flotiq.com?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro) is a headless CMS designed for various frontends, such as static sites, mobile, and web applications. Developers and content creators manage and deliver content through REST and GraphQL-based APIs.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

This guide will use the Flotiq headless CMS API with an Astro project to display content on your website.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need:

1. **An Astro project** - You can create a new project using the `npm create astro@latest` command.
2. **A Flotiq account** - If you don’t have an account, [sign up for free](https://editor.flotiq.com/register?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro).
3. **Flotiq read-only API key** - Find out [how to obtain your key](https://flotiq.com/docs/API/?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro).

### Setting up the Environment variables

[Section titled “Setting up the Environment variables”](#setting-up-the-environment-variables)

Add the read-only API key from your Flotiq account to the `.env` file in the root of your Astro project:

.env

```ini
FLOTIQ_API_KEY=__YOUR_FLOTIQ_API_KEY__
```

### Defining a Content Type in Flotiq

[Section titled “Defining a Content Type in Flotiq”](#defining-a-content-type-in-flotiq)

First, you need to define an example [Content Type Definition](https://flotiq.com/docs/panel/content-types/?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro) in Flotiq to store data.

Log in to your Flotiq account and create a custom Content Type Definition with the following example `Blog Post` configuration:

* **Label**: Blog Post

* **API Name**: blogpost

* **Fields**:

  * **Title**: text, required
  * **Slug**: text, required
  * **Content**: rich text, required

Then, create one or more example [Content Objects](https://flotiq.com/docs/panel/content-objects/?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro) using this `Blog Post` type.

### Installing the Flotiq TypeScript SDK

[Section titled “Installing the Flotiq TypeScript SDK”](#installing-the-flotiq-typescript-sdk)

To connect your project with Flotiq, install the [Flotiq SDK](https://github.com/flotiq/flotiq-api-ts) using the package manager of your choice:

* npm

  ```sh
  npm install flotiq-api-ts
  ```

* pnpm

  ```sh
  pnpm add flotiq-api-ts
  ```

* Yarn

  ```sh
  yarn add flotiq-api-ts
  ```

Next, configure the SDK using your credentials. Create a new file named `flotiq.ts` inside the `src/lib` directory of your project:

src/lib/flotiq.ts

```ts
import { FlotiqApi } from "flotiq-api-ts";


export const flotiq = new FlotiqApi(import.meta.env.FLOTIQ_API_KEY);
```

This configuration can now be used throughout your project.

### Fetching and Displaying Data from Flotiq

[Section titled “Fetching and Displaying Data from Flotiq”](#fetching-and-displaying-data-from-flotiq)

1. Fetch the `Blog Post` data on an Astro page using your content’s custom API `BlogpostAPI`:

   src/pages/index.astro

   ```astro
   ---
   import { flotiq } from "../lib/flotiq";


   const posts = await flotiq.BlogpostAPI.list();
   ---
   ```

2. Display the content in your Astro template. You will have access to the `title`, `slug`, and `content` of your posts as well as other `internal` post data:

   src/pages/index.astro

   ```diff
   ---
   import { flotiq } from "../lib/flotiq";


   const posts = await flotiq.BlogpostAPI.list();
   ---
   <html lang="en">
     <head>
       <title>Astro</title>
     </head>
     <body>
       +{posts.data?.map((post) => (
         <section>
           <a href={`/posts/${post.slug}`}>
             <h2>{post.title}</h2>
           </a>
           <div>{post.internal?.createdAt}</div>
           <div set:html={post.content}/>
         </section>
   +    ))}
     </body>
   </html>
   ```

3. Start the dev server and visit your page preview at `http://localhost:4321` to see the list of your blog posts. Each post will link to a page that does not yet exist. These will be created in the next step.

### Generating Individual Pages

[Section titled “Generating Individual Pages”](#generating-individual-pages)

Astro supports both prerendering all your pages ahead of time, or creating routes on demand when they are requested. Follow the instructions for either [static site generation](#static-site-generation) or [on-demand rendering](#on-demand-rendering) to build the page routes for your blog posts.

#### Static Site Generation

[Section titled “Static Site Generation”](#static-site-generation)

In static site generation (SSG) mode, use the `getStaticPaths()` method to fetch all possible blog post paths from Flotiq.

1. Create a new file `[slug].astro` in the `/src/pages/posts/` directory. Fetch all blog posts and return them within the `getStaticPaths()` method:

   src/pages/posts/\[slug].astro

   ```astro
   ---
   import type { Blogpost } from "flotiq-api-ts";
   import { flotiq } from "../../lib/flotiq";


   export async function getStaticPaths() {
     const posts = await flotiq.BlogpostAPI.list();
     return posts.data?.map((post) => ({
       params: { slug: post.slug },
       props: post
     })) || []
   }
   ---
   ```

2. Add the templating to display an individual post:

   src/pages/posts/\[slug].astro

   ```diff
   ---
   import type { Blogpost } from "flotiq-api-ts";
   import { flotiq } from "../../lib/flotiq";


   export async function getStaticPaths() {
     const posts = await flotiq.BlogpostAPI.list();
     return posts.data?.map((post) => ({
       params: { slug: post.slug },
       props: post
     })) || []
   }
   +const post: Blogpost = Astro.props;
   +---
   <html lang="en">
     <title>{post.title}</title>
     <body>
       <h1>{post.title}</h1>
       <div set:html={post.content}/>
     </body>
   </html>
   ```

3. Visit `http://localhost:4321` and click on a linked blog post in your list. You will now be able to navigate to the individual post’s page.

#### On-demand Rendering

[Section titled “On-demand Rendering”](#on-demand-rendering)

If you are using [SSR](/en/guides/on-demand-rendering/) mode, you will need to fetch a single post based on its `slug`.

1. Create a new file `[slug].astro` in the `/src/pages/posts/` directory. Fetch the post by its `slug` field, including logic to display a 404 page when the route is not found:

   src/pages/posts/\[slug].astro

   ```astro
   ---
   import type { Blogpost } from "flotiq-api-ts";
   import { flotiq } from "../../lib/flotiq";


   const { slug } = Astro.params;
   let post: Blogpost;


   const blogpostList = await flotiq.BlogpostAPI.list({
     filters: JSON.stringify({
       slug: {
         type: 'equals',
         filter: slug,
       }
     }),
     limit: 1
   });


   if (blogpostList.data?.[0]) {
     post = blogpostList.data[0]
   } else {
     return Astro.redirect('/404');
   }
   ---
   ```

2. Add the templating to display an individual post:

   src/pages/posts/\[slug].astro

   ```diff
   ---
   import type { Blogpost } from "flotiq-api-ts";
   import { flotiq } from "../../lib/flotiq";


   const { slug } = Astro.params;
   let post: Blogpost;


   const blogpostList = await flotiq.BlogpostAPI.list({
     filters: JSON.stringify({
       slug: {
         type: 'equals',
         filter: slug,
       }
     }),
     limit: 1
   });


   if (blogpostList.data?.[0]) {
     post = blogpostList.data[0]
   } else {
     return Astro.redirect('/404');
   }
   ---
   <html lang="en">
     <title>{post.title}</title>
     <body>
       <h1>{post.title}</h1>
       <div set:html={post.content}/>
     </body>
   </html>
   ```

3. Visit `http://localhost:4321` and click on a linked blog post in your list. You will now be able to navigate to the individual post’s page.

### Refreshing the SDK After Content Type Changes

[Section titled “Refreshing the SDK After Content Type Changes”](#refreshing-the-sdk-after-content-type-changes)

When using the Flotiq TypeScript SDK (`flotiq-api-ts`), all your data types are accurately mapped into the Astro project.

If you make changes to the structure of your content types (such as adding a new field or modifying an existing one), you’ll need to refresh the SDK to ensure that your project reflects the latest model updates.

To do this, run the rebuild command for your package manager:

* npm

  ```sh
  npm rebuild flotiq-api-ts
  ```

* pnpm

  ```sh
  pnpm rebuild flotiq-api-ts
  ```

* Yarn

  ```sh
  yarn rebuild flotiq-api-ts
  // for yarn v1 (Classic):
  // yarn add flotiq-api-ts
  ```

This will update the SDK, aligning object types, fields, and API methods with your current data model.

## Publishing Your Site

[Section titled “Publishing Your Site”](#publishing-your-site)

To deploy your website, visit Astro’s [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

### Redeploy on Flotiq Changes

[Section titled “Redeploy on Flotiq Changes”](#redeploy-on-flotiq-changes)

To update your published site, configure Flotiq to send a webhook your hosting provider to trigger a rebuild whenever your content changes.

In Flotiq, you can define which Content Type and events it should trigger on, and configure it accordingly. See the [Flotiq Webhooks documentation](https://flotiq.com/docs/panel/webhooks/async-co-webhook/?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro) for more details.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Flotiq documentation](https://flotiq.com/docs/?utm_campaign=flotiq_at_astro_headless_cms\&utm_medium=referral\&utm_source=astro)

## Community resources

[Section titled “Community resources”](#community-resources)

* [Flotiq x Astro](https://maciekpalmowski.dev/blog/flotiq-cms-astro/) by Maciek Palmowski

# Front Matter CMS & Astro

> Add content to your Astro project using Front Matter CMS

[Front Matter CMS](https://frontmatter.codes/) brings the CMS to your editor, it runs within Visual Studio Code, Gitpod, and many more.

## Integration with Astro

[Section titled “Integration with Astro”](#integration-with-astro)

In this section, we’ll walk through how to add Front Matter CMS to your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* Visual Studio Code
* Use the [Astro Blog template](https://github.com/withastro/astro/tree/main/examples/blog) to provide the base configuration and sample content to start with Front Matter CMS.

### Install the Front Matter CMS extension

[Section titled “Install the Front Matter CMS extension”](#install-the-front-matter-cms-extension)

You can get the extension from the [Visual Studio Code Marketplace - Front Matter](https://marketplace.visualstudio.com/items?itemName=eliostruyf.vscode-front-matter) or by clicking on the following link: [open Front Matter CMS extension in VS Code](vscode:extension/eliostruyf.vscode-front-matter)

### Project initialization

[Section titled “Project initialization”](#project-initialization)

Once Front Matter CMS is installed, you will get a new icon in the Activity Bar. It will open the **Front Matter CMS** panel in the primary sidebar when you click on it. Follow the next steps to initialize your project:

* Click on the **Initialize project** button in the Front Matter panel

* The welcome screen will open, and you can start initializing the project

* Click on the first step to **Initialize project**

* As Astro is one of the supported frameworks, you can select it from the list

* Register your content folders, in this case, the `src/content/blog` folder.

  Note

  Folder registration is required to let Front Matter CMS know where it can find and create your content. You can have multiple types of folders like pages, blog, docs, and many more.

* You will be asked to enter the name of the folder. By default, it takes the folder name.

  Note

  The name gets used during the creation process of new content. For example, having multiple folder registrations allows you to choose the type of content you want to create.

* Click on **Show the dashboard** to open the content dashboard

  Tip

  Once Front Matter CMS is initialized, you can open the dashboard as follows:

  * Using the keyboard binding: `alt` + `d` (Windows & Linux) or `options` + `d` (macOS)
  * Open the command palette and search for `Front Matter: Open dashboard`
  * Click on the **Front Matter** icon on the panel’s title bar or files.

### Project configuration

[Section titled “Project configuration”](#project-configuration)

Once the project is initialized, you will get a `frontmatter.json` configuration file and a `.frontmatter` folder in the root of your project.

* .frontmatter/

  * database/

    * mediaDb.json

* src/

  * …

* astro.config.mjs

* **frontmatter.json**

* package.json

#### Content-type configuration

[Section titled “Content-type configuration”](#content-type-configuration)

Content-types are the way Front Matter CMS manages your content. Each content-type contains a set of fields, which can be defined per type of content you want to use for your website.

The fields correspond to the front matter of your page content.

You can configure the content-types in the `frontmatter.json` file.

* Open the `frontmatter.json` file
* Replace the `frontMatter.taxonomy.contentTypes` array with the following content-types configuration:

frontmatter.json

```json
"frontMatter.taxonomy.contentTypes": [
  {
    "name": "default",
    "pageBundle": false,
    "previewPath": "'blog'",
    "filePrefix": null,
    "fields": [
      {
        "title": "Title",
        "name": "title",
        "type": "string",
        "single": true
      },
      {
        "title": "Description",
        "name": "description",
        "type": "string"
      },
      {
        "title": "Publishing date",
        "name": "pubDate",
        "type": "datetime",
        "default": "{{now}}",
        "isPublishDate": true
      },
      {
        "title": "Content preview",
        "name": "heroImage",
        "type": "image",
        "isPreviewImage": true
      }
    ]
  }
]
```

Note

This configuration ensures that the Front Matter content-type matches the content collection schema from the Astro blog template.

Tip

You can find more information on content-types and the supported fields in the [content creation docs section](https://frontmatter.codes/docs/content-creation) from Front Matter CMS.

### Preview your articles in the editor

[Section titled “Preview your articles in the editor”](#preview-your-articles-in-the-editor)

From the **Front Matter CMS** panel, click on the **Start server** button. This action starts the Astro local dev server. Once running, you can open the content dashboard, select one of the articles and click on the **Open preview** button to open the article in the editor.

### Create new articles

[Section titled “Create new articles”](#create-new-articles)

Open the **Front Matter CMS Dashboard**; you can do this as follows:

* Open the Front Matter CMS’ content dashboard
* Click on the **Create content** button
* Front Matter will ask you for the title of the article. Fill it in and press enter
* Your new article will be created and opened in the editor. You can start writing your article.

### Using Markdoc with Front Matter CMS

[Section titled “Using Markdoc with Front Matter CMS”](#using-markdoc-with-front-matter-cms)

To use Markdoc with Front Matter CMS, you must configure this in the `frontMatter.content.supportedFileTypes`. This setting lets the CMS know which types of files it can progress.

You can configure the setting as follows:

frontmatter.json

```json
"frontMatter.content.supportedFileTypes": [ "md", "markdown", "mdx", "mdoc" ]
```

To allow your content to be created as Markdoc, specify the `fileType` property on the content-type.

frontmatter.json

```diff
"frontMatter.taxonomy.contentTypes": [
  {
    "name": "default",
    "pageBundle": false,
    "previewPath": "'blog'",
    "filePrefix": null,
    +"fileType": "mdoc",
    "fields": [
      {
        "title": "Title",
        "name": "title",
        "type": "string",
        "single": true
      },
      {
        "title": "Description",
        "name": "description",
        "type": "string"
      },
      {
        "title": "Publishing date",
        "name": "pubDate",
        "type": "datetime",
        "default": "{{now}}",
        "isPublishDate": true
      },
      {
        "title": "Content preview",
        "name": "heroImage",
        "type": "image",
        "isPreviewImage": true
      }
    ]
  }
]
```

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Front Matter CMS](https://frontmatter.codes/)
* [Front Matter CMS - Documentation](https://frontmatter.codes/docs/)
* [Getting started with Astro and Front Matter CMS](https://youtu.be/xb6pZiier_E)

# Ghost & Astro

> Add content to your Astro project using Ghost as a CMS

[Ghost](https://github.com/TryGhost/Ghost) is an open-source, headless content management system built on Node.js.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, we’ll use the [Ghost content API](https://ghost.org/docs/content-api/) to bring your data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A Ghost site** - It is assumed that you have a site set up with Ghost. If you don’t you can set one up on a [local environment.](https://ghost.org/docs/install/local/)

3. **Content API Key** - You can make an integration under your site’s `Settings > Integrations`. From there you can find your `Content API key`

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your site’s credentials to Astro, create an `.env` file in the root of your project with the following variable:

.env

```ini
CONTENT_API_KEY=YOUR_API_KEY
```

Now, you should be able to use this environment variable in your project.

If you would like to have IntelliSense for your environment variable, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly CONTENT_API_KEY: string;
}
```

Tip

Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your root directory should now include these new files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect with Ghost, install the official content API wrapper [`@tryghost/content-api`](https://www.npmjs.com/package/@tryghost/content-api) using the command below for your preferred package manager, and optionally, a helpful package containing type definitions if you are using TypeScript:

* npm

  ```shell
  npm install @tryghost/content-api
  npm install --save @types/tryghost__content-api
  ```

* pnpm

  ```shell
  pnpm add @tryghost/content-api
  pnpm add --save-dev @types/tryghost__content-api
  ```

* Yarn

  ```shell
  yarn add @tryghost/content-api
  yarn add --dev @types/tryghost__content-api
  ```

## Making a blog with Astro and Ghost

[Section titled “Making a blog with Astro and Ghost”](#making-a-blog-with-astro-and-ghost)

With the setup above, you are now able to create a blog that uses Ghost as the CMS.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. A Ghost blog
2. An Astro project integrated with the [Ghost content API](https://www.npmjs.com/package/@tryghost/content-api) - See [integrating with Astro](/en/guides/cms/ghost/#integrating-with-astro) for more details on how to set up an Astro project with Ghost.

This example will create an index page that lists posts with links to dynamically-generated individual post pages.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

You can fetch your site’s data with the Ghost content API package.

First, create a `ghost.ts` file under a `lib` directory.

* src/

  * lib/

    * **ghost.ts**

  * pages/

    * index.astro

* astro.config.mjs

* package.json

Initialize an API instance with the Ghost API using the API key from the Ghost dashboard’s Integrations page.

src/lib/ghost.ts

```ts
import GhostContentAPI from '@tryghost/content-api';


// Create API instance with site credentials
export const ghostClient = new GhostContentAPI({
    url: 'http://127.0.0.1:2368', // This is the default URL if your site is running on a local environment
    key: import.meta.env.CONTENT_API_KEY,
    version: 'v5.0',
});
```

### Displaying a list of posts

[Section titled “Displaying a list of posts”](#displaying-a-list-of-posts)

The page `src/pages/index.astro` will display a list of posts, each with a description and link to its own page.

* src/

  * lib/

    * ghost.ts

  * pages/

    * **index.astro**

* astro.config.mjs

* package.json

Import `ghostClient()` in the Astro frontmatter to use the `posts.browse()` method to access blog posts from Ghost. Set `limit: all` to retrieve all posts.

src/pages/index.astro

```astro
---
import { ghostClient } from '../lib/ghost';
const posts = await ghostClient.posts
    .browse({
        limit: 'all',
    })
    .catch((err) => {
        console.error(err);
    });
---
```

Fetching via the content API returns an array of objects containing the [properties for each post](https://ghost.org/docs/content-api/#posts) such as:

* `title` - the title of the post
* `html` - the HTML rendering of the content of the post
* `feature_image` - the source URL of the featured image of the post
* `slug` - the slug of the post

Use the `posts` array returned from the fetch to display a list of blog posts on the page.

src/pages/index.astro

```astro
---
import { ghostClient } from '../lib/ghost';
const posts = await ghostClient.posts
    .browse({
        limit: 'all',
    })
    .catch((err) => {
        console.error(err);
    });
---


<html lang="en">
    <head>
        <title>Astro + Ghost 👻</title>
    </head>
    <body>


        {
            posts.map((post) => (
                <a href={`/post/${post.slug}`}>
                    <h1> {post.title} </h1>
                </a>
            ))
        }
    </body>
</html>
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

The page `src/pages/post/[slug].astro` [dynamically generates a page](/en/guides/routing/#dynamic-routes) for each post.

* src/

  * lib/

    * ghost.ts

  * pages/

    * index.astro

    * post/

      * **\[slug].astro**

* astro.config.mjs

* package.json

Import `ghostClient()` to access blog posts using `posts.browse()` and return a post as props to each of your dynamic routes.

src/pages/post/\[slug].astro

```astro
---
import { ghostClient } from '../../lib/ghost';


export async function getStaticPaths() {
    const posts = await ghostClient.posts
        .browse({
            limit: 'all',
        })
        .catch((err) => {
            console.error(err);
        });


    return posts.map((post) => {
        return {
            params: {
                slug: post.slug,
            },
            props: {
                post: post,
            },
        };
    });
}


const { post } = Astro.props;
---
```

Create the template for each page using the properties of each `post` object.

src/pages/post/\[slug].astro

```diff
---
import { ghostClient } from '../../lib/ghost';
export async function getStaticPaths() {
    const posts = await ghostClient.posts
        .browse({
            limit: 'all',
        })
        .catch((err) => {
            console.error(err);
        });
    return posts.map((post) => {
        return {
            params: {
                slug: post.slug,
            },
            props: {
                post: post,
            },
        };
    });
}
const { post } = Astro.props;
---
+<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{post.title}</title>
    </head>
    <body>
        <img src={post.feature_image} alt={post.title} />


        <h1>{post.title}</h1>
        <p>{post.reading_time} min read</p>


        +<Fragment set:html={post.html} />
    </body>
</html>
```

Note

`<Fragment />` is a built-in Astro component which allows you to avoid an unnecessary wrapper element. This can be especially useful when fetching HTML from a CMS (e.g. Ghost or [WordPress](/en/guides/cms/wordpress/)).

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

[Ghost CMS & Astro Tutorial ](https://matthiesen.xyz/blog/astro-ghostcms)

[Astro + Ghost + Tailwind CSS ](https://andr.ec/posts/astro-ghost-blog/)

[Building a Corporate site with Astro and Ghost ](https://artabric.com/post/building-a-corporate-site-with-astro-and-ghost/)

[\`astro-starter-ghost\` ](https://github.com/PhilDL/astro-starter-ghost)

Have a resource to share?

If you found (or made!) a helpful video or blog post about using Ghost with Astro, [add it to this list](https://github.com/withastro/docs/edit/main/src/content/docs/en/guides/cms/ghost.mdx)!

# GitCMS & Astro

> Integrate GitCMS into your Astro project for seamless content management

[GitCMS](https://gitcms.blog) turns GitHub into a Git-based headless CMS, offering a Notion-like markdown editing experience right in your browser.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* [Introducing GitCMS](https://gitcms.blog/posts/introducing-gitcms/)
* [How to Configure GitCMS for an Astro Site](https://gitcms.blog/posts/how-to-configure-gitcms/)
* [Install GitCMS Chrome Extension](https://gitcms.blog/extension)

# Hashnode & Astro

> Add content to your Astro project using Hashnode as a CMS

[Hashnode](https://hashnode.com/) is a hosted CMS that allows you to create a blog or publication.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

The [Hashnode Public API](https://apidocs.hashnode.com/) is a GraphQL API that allows you to interact with Hashnode. This guide uses [`graphql-request`](https://github.com/jasonkuhrt/graphql-request), a minimal GraphQL client that works well with Astro, to bring your Hashnode data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started you will need to have the following:

1. **An Astro project** - If you don’t have an Astro project yet, our [Installation guide](/en/install-and-setup/) will get you up and running in no time.

2. **A Hashnode site** - You can create free personal site by visiting [Hashnode](https://hashnode.com/).

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Install the `graphql-request` package using the package manager of your choice:

* npm

  ```shell
  npm install graphql-request
  ```

* pnpm

  ```shell
  pnpm add graphql-request
  ```

* Yarn

  ```shell
  yarn add graphql-request
  ```

## Making a blog with Astro and Hashnode

[Section titled “Making a blog with Astro and Hashnode”](#making-a-blog-with-astro-and-hashnode)

This guide uses [`graphql-request`](https://github.com/jasonkuhrt/graphql-request), a minimal GraphQL client that works well with Astro, to bring your Hashnode data into your Astro project.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. A Hashnode Blog
2. An Astro project integrated with the [graphql-request](https://github.com/jasonkuhrt/graphql-request) package installed.

This example will create an index page that lists posts with links to dynamically-generated individual post pages.

### Fetching Data

[Section titled “Fetching Data”](#fetching-data)

1. To fetch your site’s data with the `graphql-request` package, make a `src/lib` directory and create two new files `client.ts` & `schema.ts`:

   * src/

     * lib/

       * **client.ts**
       * **schema.ts**

     * pages/

       * index.astro

   * astro.config.mjs

   * package.json

2. Initialize an API instance with the GraphQLClient using the URL from your Hashnode Website.

   src/lib/client.ts

   ```ts
   import { gql, GraphQLClient } from "graphql-request";
   import type { AllPostsData, PostData } from "./schema";


   export const getClient = () => {
     return new GraphQLClient("https://gql.hashnode.com")
   }


   const myHashnodeURL = "astroplayground.hashnode.dev";


   export const getAllPosts = async () => {
     const client = getClient();


     const allPosts = await client.request<AllPostsData>(
       gql`
         query allPosts {
           publication(host: "${myHashnodeURL}") {
             id
             title
             posts(first: 20) {
               pageInfo{
                 hasNextPage
                 endCursor
               }
               edges {
                 node {
                   id
                   author{
                     name
                     profilePicture
                   }
                   title
                   subtitle
                   brief
                   slug
                   coverImage {
                     url
                   }
                   tags {
                     name
                     slug
                   }
                   publishedAt
                   readTimeInMinutes
                 }
               }
             }
           }
         }
       `
     );


     return allPosts;
   };




   export const getPost = async (slug: string) => {
     const client = getClient();


     const data = await client.request<PostData>(
       gql`
         query postDetails($slug: String!) {
           publication(host: "${myHashnodeURL}") {
             id
             post(slug: $slug) {
               id
               author{
                 name
                 profilePicture
               }
               publishedAt
               title
               subtitle
               readTimeInMinutes
               content{
                 html
               }
               tags {
                 name
                 slug
               }
               coverImage {
                 url
               }
             }
           }
         }
       `,
       { slug: slug }
     );


     return data.publication.post;
   };
   ```

3. Configure `schema.ts` to define the shape of the data returned from the Hashnode API.

   src/lib/schema.ts

   ```ts
   import { z } from "astro/zod";


   export const PostSchema = z.object({
       id: z.string(),
       author: z.object({
           name: z.string(),
           profilePicture: z.string(),
           }),
       publishedAt: z.string(),
       title: z.string(),
       subtitle: z.string(),
       brief: z.string(),
       slug: z.string(),
       readTimeInMinutes: z.number(),
       content: z.object({
           html: z.string(),
       }),
       tags: z.array(z.object({
           name: z.string(),
           slug: z.string(),
       })),
       coverImage: z.object({
           url: z.string(),
       }),
   })


   export const AllPostsDataSchema = z.object({
       id: z.string(),
       publication: z.object({
           title: z.string(),
           posts: z.object({
               pageInfo: z.object({
                   hasNextPage: z.boolean(),
                   endCursor: z.string(),
               }),
               edges: z.array(z.object({
                   node: PostSchema,
               })),
           }),
       }),
   })


   export const PostDataSchema = z.object({
       id: z.string(),
       publication: z.object({
           title: z.string(),
           post: PostSchema,
       }),
   })


   export type Post = z.infer<typeof PostSchema>
   export type AllPostsData = z.infer<typeof AllPostsDataSchema>
   export type PostData = z.infer<typeof PostDataSchema>
   ```

### Displaying a list of posts

[Section titled “Displaying a list of posts”](#displaying-a-list-of-posts)

Fetching via `getAllPosts()` returns an array of objects containing the properties for each post such as:

* `title` - the title of the post
* `brief` - the HTML rendering of the content of the post
* `coverImage.url` - the source URL of the featured image of the post
* `slug` - the slug of the post

Use the `posts` array returned from the fetch to display a list of blog posts on the page.

src/pages/index.astro

```astro
---
import { getAllPosts } from '../lib/client';


const data = await getAllPosts();
const allPosts = data.publication.posts.edges;


---


<html lang="en">
    <head>
        <title>Astro + Hashnode</title>
    </head>
    <body>


        {
            allPosts.map((post) => (
                <div>
                    <h2>{post.node.title}</h2>
                    <p>{post.node.brief}</p>
                    <img src={post.node.coverImage.url} alt={post.node.title} />
                    <a href={`/post/${post.node.slug}`}>Read more</a>
                </div>
            ))
        }
    </body>
</html>
```

### Generating pages

[Section titled “Generating pages”](#generating-pages)

1. Create the page `src/pages/post/[slug].astro` to [dynamically generate a page](/en/guides/routing/#dynamic-routes) for each post.

   * src/

     * lib/

       * client.ts
       * schema.ts

     * pages/

       * index.astro

       * post/

         * **\[slug].astro**

   * astro.config.mjs

   * package.json

2. Import and use `getAllPosts()` and `getPost()` to fetch the data from Hashnode and generate individual page routes for each post.

   src/pages/post/\[slug].astro

   ```astro
   ---
   import { getAllPosts, getPost } from '../../lib/client';




   export async function getStaticPaths() {
     const data = await getAllPosts();
     const allPosts = data.publication.posts.edges;
     return allPosts.map((post) => {
       return {
         params: { slug: post.node.slug },
       }
     })
   }
   const { slug } = Astro.params;
   const post = await getPost(slug);


   ---
   ```

3. Create the template for each page using the properties of each `post` object. The example below shows the post title and reading time, then the full post content:

   src/pages/post/\[slug].astro

   ```astro
   ---
   import { getAllPosts, getPost } from '../../lib/client';




   export async function getStaticPaths() {
     const data = await getAllPosts();
     const allPosts = data.publication.posts.edges;
     return allPosts.map((post) => {
       return {
         params: { slug: post.node.slug },
       }
     })
   }
   const { slug } = Astro.params;
   const post = await getPost(slug);


   ---
   <!DOCTYPE html>
   <html lang="en">
       <head>
           <title>{post.title}</title>
       </head>
       <body>
           <img src={post.coverImage.url} alt={post.title} />


           <h1>{post.title}</h1>
           <p>{post.readTimeInMinutes} min read</p>


           <Fragment set:html={post.content.html} />
       </body>
   </html>
   ```

   Note

   `<Fragment />` is a built-in Astro component which allows you to avoid an unnecessary wrapper element. This can be especially useful when fetching HTML from a CMS (e.g. Hashnode or [WordPress](/en/guides/cms/wordpress/)).

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your site visit our [deployment guide](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [`astro-hashnode`](https://github.com/matthiesenxyz/astro-hashnode) on GitHub

# Hygraph & Astro

> Add content to your Astro project using Hygraph as a CMS

[Hygraph](https://hygraph.com/) is a federated content management platform. It exposes a GraphQL endpoint for fetching content.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you’ll create a [Hygraph](https://hygraph.com/) GraphQL endpoint to fetch with Astro.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you will need to have the following:

1. **A Hygraph account and project**. If you don’t have an account, you can [sign up for free](https://app.hygraph.com/signup) and create a new project.

2. **Hygraph access permissions** - In `Project Settings > API Access`, configure Public Content API permissions to allow read requests without authentication. If you haven’t set any permissions, you can click **Yes, initialize defaults** to add the required permissions to use the “High Performance Content API”.

### Setting up the endpoint

[Section titled “Setting up the endpoint”](#setting-up-the-endpoint)

To add your Hygraph endpoint to Astro, create a `.env` file in the root of your project with the following variable:

.env

```ini
HYGRAPH_ENDPOINT=YOUR_HIGH_PERFORMANCE_API
```

Now, you should be able to use this environment variable in your project.

If you would like to have IntelliSense for your environment variables, you can create a `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly HYGRAPH_ENDPOINT: string;
}
```

Note

Read more about [using environment variables](/en/guides/environment-variables/) and `.env` files in Astro.

Your root directory should now include these new files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

Fetch data from your Hygraph project by using the `HYGRAPH_ENDPOINT`.

For example, to fetch entries of a `blogPosts` content type that has a string field `title`, create a GraphQL query to fetch that content. Then, define the type of the content, and set it as the type of the response.

src/pages/index.astro

```astro
---
interface Post {
  title: string;
}


const query = {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    query: `
      {
        blogPosts {
          title
        }
      }`,
  }),
};


const response = await fetch(import.meta.env.HYGRAPH_ENDPOINT, query);
const json = await response.json();
const posts: Post[] = json.data.blogPosts;
---


<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width" />
    <meta name="generator" content={Astro.generator} />
    <title>Astro</title>
  </head>
  <body>
    <h1>Astro</h1>
    {
      posts.map((post) => (
        <div>
          <h2>{post.title}</h2>
        </div>
      ))
    }
  </body>
</html>
```

## Deploy

[Section titled “Deploy”](#deploy)

### Configuring Netlify Webhook

[Section titled “Configuring Netlify Webhook”](#configuring-netlify-webhook)

To set up a webhook in Netlify:

1. Deploy your site to Netlify with [this guide](/en/guides/deploy/netlify/). Remember to add your `HYGRAPH_ENDPOINT` to the environment variables.

2. Then Go to your Hygraph project dashboard and click on **Apps**.

3. Go to the marketplace and search for Netlify and follow the instructions provided.

4. If all went good, now you can deploy your website with a click in the Hygraph interface.

## Community Resources

[Section titled “Community Resources”](#community-resources)

* [Hygraph + Astro example with `marked` for markdown parsing](https://github.com/camunoz2/example-astrowithhygraph)

# Keystatic & Astro

> Add content to your Astro project using Keystatic as a CMS

[Keystatic](https://keystatic.com/) is an open source, headless content-management system that allows you to structure your content and sync it with GitHub.

Tip

If you’re starting a **new Astro + Keystatic project from scratch**, you can use the [Keystatic CLI](https://keystatic.com/docs/quick-start#keystatic-cli) to generate a new project in seconds:

* npm

  ```shell
  npm create @keystatic@latest
  ```

* pnpm

  ```shell
  pnpm create @keystatic@latest
  ```

* Yarn

  ```shell
  yarn create @keystatic
  ```

Select the Astro template, and you’ll be ready to [deploy](#deploying-keystatic--astro)!

## Prerequisites

[Section titled “Prerequisites”](#prerequisites)

* An existing Astro project [with an adapter configured](/en/guides/on-demand-rendering/).

Note

If you intend to sync Keystatic’s data with GitHub, you will also need **a GitHub account with `write` permissions** on the repository for this project.

## Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

Add both the Markdoc (for content entries) and the React (for the Keystatic Admin UI Dashboard) integrations to your Astro project, using the `astro add` command for your package manager.

* npm

  ```shell
  npx astro add react markdoc
  ```

* pnpm

  ```shell
  pnpm astro add react markdoc
  ```

* Yarn

  ```shell
  yarn astro add react markdoc
  ```

You will also need two Keystatic packages:

* npm

  ```shell
  npm install @keystatic/core @keystatic/astro
  ```

* pnpm

  ```shell
  pnpm add @keystatic/core @keystatic/astro
  ```

* Yarn

  ```shell
  yarn add @keystatic/core @keystatic/astro
  ```

## Adding the Astro integration

[Section titled “Adding the Astro integration”](#adding-the-astro-integration)

Add the Astro integration from `@keystatic/astro` in your Astro config file:

astro.config.mjs

```diff
import { defineConfig } from 'astro/config'


import react from '@astrojs/react'
import markdoc from '@astrojs/markdoc'
+import keystatic from '@keystatic/astro'


// https://astro.build/config
export default defineConfig({
  integrations: [react(), markdoc(), keystatic()],
  output: 'static',
})
```

## Creating a Keystatic config file

[Section titled “Creating a Keystatic config file”](#creating-a-keystatic-config-file)

A Keystatic config file is required to define your content schema. This file will also allow you to connect a project to a specific GitHub repository (if you decide to do so).

Create a file called `keystatic.config.ts` in the root of the project and add the following code to define both your storage type (`local`) and a single content collection (`posts`):

keystatic.config.ts

```ts
import { config, fields, collection } from '@keystatic/core';


export default config({
  storage: {
    kind: 'local',
  },


  collections: {
    posts: collection({
      label: 'Posts',
      slugField: 'title',
      path: 'src/content/posts/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Title' } }),
        content: fields.markdoc({
          label: 'Content',
        }),
      },
    }),
  },
});
```

Already using content collections?

If you are already using [content collections](/en/guides/content-collections/) in your Astro project, then update the schema above to exactly match the collection(s) defined in your existing schema.

Keystatic is now configured to manage your content based on your schema.

## Running Keystatic locally

[Section titled “Running Keystatic locally”](#running-keystatic-locally)

To launch your Keystatic Admin UI dashboard, start Astro’s dev server:

```bash
npm run dev
```

Visit `http://127.0.0.1:4321/keystatic` in the browser to see the Keystatic Admin UI running.

## Creating a new post

[Section titled “Creating a new post”](#creating-a-new-post)

1. In the Keystatic Admin UI dashboard, click on the “Posts” collection.

2. Use the button to create a new post. Add the title “My First Post” and some content, then save the post.

3. This post should now be visible from your “Posts” collection. You can view and edit your individual posts from this dashboard page.

4. Return to view your Astro project files. You will now find a new `.mdoc` file inside the `src/content/posts` directory for this new post:

   * src/

     * content/

       * posts/

         * **my-first-post.mdoc**

5. Navigate to that file in your code editor and verify that you can see the Markdown content you entered. For example:

   ```markdown
   ---
   title: My First Post
   ---


   This is my very first post. I am **super** excited!
   ```

## Rendering Keystatic content

[Section titled “Rendering Keystatic content”](#rendering-keystatic-content)

Use Astro’s Content Collections API to [query and display your posts and collections](/en/guides/content-collections/#querying-collections), just as you would in any Astro project.

### Displaying a collection list

[Section titled “Displaying a collection list”](#displaying-a-collection-list)

The following example displays a list of each post title, with a link to an individual post page.

```tsx
---
import { getCollection } from 'astro:content'


const posts = await getCollection('posts')
---
<ul>
  {posts.map(post => (
    <li>
      <a href={`/posts/${post.slug}`}>{post.data.title}</a>
    </li>
  ))}
</ul>
```

### Displaying a single entry

[Section titled “Displaying a single entry”](#displaying-a-single-entry)

To display content from an individual post, you can import and use the `<Content />` component to [render your content to HTML](/en/guides/content-collections/#rendering-body-content):

```tsx
---
import { getEntry } from 'astro:content'


const post = await getEntry('posts', 'my-first-post')
const { Content } = await post.render()
---


<main>
  <h1>{post.data.title}</h1>
  <Content />
</main>
```

For more information on querying, filtering, displaying your collections content and more, see the full content [collections documentation](/en/guides/content-collections/).

## Deploying Keystatic + Astro

[Section titled “Deploying Keystatic + Astro”](#deploying-keystatic--astro)

To deploy your website, visit our [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

You’ll also probably want to [connect Keystatic to GitHub](https://keystatic.com/docs/connect-to-github) so you can manage content on the deployed instance of the project.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out [the official Keystatic guide](https://keystatic.com/docs/installation-astro)
* [Keystatic starter template](https://github.com/Thinkmill/keystatic/tree/main/templates/astro)

# KeystoneJS & Astro

> Add content to your Astro project using KeystoneJS as a CMS

[KeystoneJS](https://keystonejs.com/) is an open source, headless content-management system that allows you to describe the structure of your schema.

# Kontent.ai & Astro

> Add content to your Astro project using Kontent.ai as CMS

[Kontent.ai](https://www.kontent.ai/) is a headless CMS that allows you to manage content in a structured and modular way, supported by AI capabilities.

## Integrating with Astro

[Section titled “Integrating with Astro”](#integrating-with-astro)

In this section, you’ll use the [Kontent.ai TypeScript SDK](https://github.com/kontent-ai/delivery-sdk-js) to connect your Kontent.ai project to your Astro application.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites)

To get started, you’ll need the following:

1. **Kontent.ai project** - If you don’t have a Kontent.ai account yet, [sign up for free](https://app.kontent.ai/sign-up) and create a new project.

2. **Delivery API keys** - You will need the Environment ID for published content and the Preview API key for fetching drafts (optional). Both keys are located in the **Environment Settings -> API keys** tab in Kontent.ai.

### Setting up credentials

[Section titled “Setting up credentials”](#setting-up-credentials)

To add your Kontent.ai credentials to Astro, create a `.env` file in the root of your project with the following variables:

.env

```ini
KONTENT_ENVIRONMENT_ID=YOUR_ENVIRONMENT_ID
KONTENT_PREVIEW_API_KEY=YOUR_PREVIEW_API_KEY
```

Now, these environment variables can be used in your Astro project.

If you would like to get [TypeScript IntelliSense for these environment variables](/en/guides/environment-variables/#intellisense-for-typescript), you can create a new `env.d.ts` file in the `src/` directory and configure `ImportMetaEnv` like this:

src/env.d.ts

```ts
interface ImportMetaEnv {
  readonly KONTENT_ENVIRONMENT_ID: string;
  readonly KONTENT_PREVIEW_API_KEY: string;
}
```

Your root directory should now include these new files:

* src/

  * **env.d.ts**

* **.env**

* astro.config.mjs

* package.json

### Installing dependencies

[Section titled “Installing dependencies”](#installing-dependencies)

To connect Astro with your Kontent.ai project, install the [Kontent.ai TypeScript SDK](https://github.com/kontent-ai/delivery-sdk-js):

* npm

  ```shell
    npm install @kontent-ai/delivery-sdk
  ```

* pnpm

  ```shell
    pnpm add @kontent-ai/delivery-sdk
  ```

* Yarn

  ```shell
    yarn add @kontent-ai/delivery-sdk
  ```

Next, create a new file called `kontent.ts` in the `src/lib/` directory of your Astro project.

src/lib/kontent.ts

```ts
import { createDeliveryClient } from "@kontent-ai/delivery-sdk";


export const deliveryClient = createDeliveryClient({
    environmentId: import.meta.env.KONTENT_ENVIRONMENT_ID,
    previewApiKey: import.meta.env.KONTENT_PREVIEW_API_KEY,
});
```

Note

Read more on [getting environment variables in Astro](/en/guides/environment-variables/#getting-environment-variables).

This implementation creates a new `DeliveryClient` object using credentials from the `.env` file.

Previews

The `previewApiKey` is optional. When used, you can [configure each query](https://github.com/kontent-ai/delivery-sdk-js#enable-preview-mode-per-query) to the Delivery API endpoint to return the latest versions of content items regardless of their state in the workflow. Otherwise, only published items are returned.

Finally, the root directory of your Astro project should now include these new files:

* src/

  * lib/

    * **kontent.ts**

  * env.d.ts

* .env

* astro.config.mjs

* package.json

### Fetching data

[Section titled “Fetching data”](#fetching-data)

The `DeliveryClient` is now available to all components. To fetch content, use the `DeliveryClient` and method chaining to define your desired items. This example shows a basic fetch of blog posts and renders their titles in a list:

src/pages/index.astro

```diff
---
+import { deliveryClient } from "../lib/kontent";


+const blogPosts = await deliveryClient
    +.items()
    +.type("blogPost")
    +.toPromise()
---
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Astro</title>
  </head>
  <body>
        <ul>
        +{blogPosts.data.items.map(blogPost => (
            <li>{blogPost.elements.title.value}</li>
+        ))}
        </ul>
    </body>
</html>
```

You can find more querying options in the [Kontent.ai documentation](https://kontent.ai/learn/develop/hello-world/get-content/javascript).

## Making a blog with Astro and Kontent.ai

[Section titled “Making a blog with Astro and Kontent.ai”](#making-a-blog-with-astro-and-kontentai)

With the setup above, you are now able to create a blog that uses Kontent.ai as the source of content.

### Prerequisites

[Section titled “Prerequisites”](#prerequisites-1)

1. **Kontent.ai project** - For this tutorial, using a blank project is recommended. If you already have some content types in your content model, you may use them, but you will need to modify the code snippets to match your content model.

2. **Astro project configured for content fetching from Kontent.ai** - see above for more details on how to set up an Astro project with Kontent.ai

### Setting up content model

[Section titled “Setting up content model”](#setting-up-content-model)

In Kontent.ai, navigate to **Content model** and create a new content type with the following fields and values:

* **Name:** Blog Post

* Elements:

  * Text field

    * **Name:** Title
    * **Element Required:** yes

  * Rich text field

    * **Name:** Teaser
    * **Element Required:** yes
    * **Allowed in this element:** only check Text

  * Rich text field

    * **Name:** Content
    * **Element Required:** yes

  * Date & time field
    * **Name:** Date

  * URL slug field

    * **Name:** URL slug
    * **Element Required:** yes
    * **Auto-generate from:** select “Title”

Then, click on **Save Changes**.

### Creating content

[Section titled “Creating content”](#creating-content)

Now, navigate to **Content & assets** tab and create a new content item of type **Blog Post**. Fill the fields using these values:

* **Content item name:** Astro
* **Title:** Astro is amazing
* **Teaser:** Astro is an all-in-one framework for building fast websites faster.
* **Content:** You can use JavaScript to implement the website functionality, but no client bundle is necessary.
* **Date & time:** select today
* **URL slug:** astro-is-amazing

When you’re finished, publish the blog post using the **Publish** button at the top.

*Note: Feel free to create as many blog posts as you like before moving to the next step.*

### Generating content model in TypeScript

[Section titled “Generating content model in TypeScript”](#generating-content-model-in-typescript)

Next, you’ll generate TypeScript types out of your content model.

Note

This step is optional but provides a much better developer experience and allows you to discover potential problems at build time rather than at runtime.

First, install the [Kontent.ai JS model generator](https://github.com/kontent-ai/model-generator-js), [ts-node](https://github.com/TypeStrong/ts-node), and [dotenv](https://github.com/motdotla/dotenv):

* npm

  ```shell
    npm install @kontent-ai/model-generator ts-node dotenv
  ```

* pnpm

  ```shell
    pnpm add @kontent-ai/model-generator ts-node dotenv
  ```

* Yarn

  ```shell
    yarn add @kontent-ai/model-generator ts-node dotenv
  ```

Then, add the following script to package.json:

package.json

```json
{
    ...
    "scripts": {
        ...
        "regenerate:models": "ts-node --esm ./generate-models.ts"
    },
}
```

Because the types require structural information about your project that is not available in the public API, you also need to add a Content Management API key to the `.env` file. You can generate the key under **Environment settings -> API keys -> Management API**.

.env

```diff
KONTENT_ENVIRONMENT_ID=YOUR_ENVIRONMENT_ID
KONTENT_PREVIEW_API_KEY=YOUR_PREVIEW_API_KEY
+KONTENT_MANAGEMENT_API_KEY=YOUR_MANAGEMENT_API_KEY
```

Finally, add the script `generate-models.ts` that configures the model generator to generate the models:

generate-models.ts

```ts
import { generateModelsAsync, textHelper } from '@kontent-ai/model-generator'
import { rmSync, mkdirSync } from 'fs'


import * as dotenv from 'dotenv'
dotenv.config()


const runAsync = async () => {
  rmSync('./src/models', { force: true, recursive: true })
  mkdirSync('./src/models')


  // change working directory to models
  process.chdir('./src/models')


  await generateModelsAsync({
    sdkType: 'delivery',
    apiKey: process.env.KONTENT_MANAGEMENT_API_KEY ?? '',
    environmentId: process.env.KONTENT_ENVIRONMENT_ID ?? '',
    addTimestamp: false,
    isEnterpriseSubscription: false,
  })
}


// Self-invocation async function
;(async () => {
  await runAsync()
})().catch(err => {
  console.error(err)
  throw err
})
```

Now, execute it:

* npm

  ```shell
    npm run regenerate:models
  ```

* pnpm

  ```shell
    pnpm run regenerate:models
  ```

* Yarn

  ```shell
    yarn run regenerate:models
  ```

### Displaying a list of blog posts

[Section titled “Displaying a list of blog posts”](#displaying-a-list-of-blog-posts)

Now you’re ready to fetch some content. Go to the Astro page where you want to display a list of all blog posts, for example, the homepage `index.astro` in `src/pages`.

Fetch all blog posts in the frontmatter of the Astro page:

src/pages/index.astro

```astro
---
import { deliveryClient } from '../lib/kontent';
import type { BlogPost } from '../models';
import { contentTypes } from '../models/project/contentTypes';


const blogPosts = await deliveryClient
    .items<BlogPost>
    .type(contentTypes.blog_post.codename)
    .toPromise()
---
```

If you skipped the model generation, you can also use an untyped object and string literal to define the type:

```ts
const blogPosts = await deliveryClient
    .items()
    .type("blogPost")
    .toPromise()
```

The fetch call will return a `response` object which contains a list of all blog posts in `data.items`. In the HTML section of the Astro page, you can use the `map()` function to list the blog posts:

src/pages/index.astro

```diff
---
import { deliveryClient } from '../lib/kontent';
import type { BlogPost } from '../models';
import { contentTypes } from '../models/project/contentTypes';


const blogPosts = await deliveryClient
    .items<BlogPost>
    .type(contentTypes.blogPost.codename)
    .toPromise()
---
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>Astro</title>
    </head>
    <body>
        <h1>Blog posts</h1>
        <ul>
            +{blogPosts.data.items.map(blogPost => (
                <li>
                    <a href={`/blog/${blogPost.elements.url_slug.value}/`} title={blogPost.elements.title.value}>
                        +{blogPost.elements.title.value}
                    </a>
                </li>
+            ))}
        </ul>
    </body>
</html>
```

### Generating individual blog posts

[Section titled “Generating individual blog posts”](#generating-individual-blog-posts)

The last step of the tutorial is to generate detailed blog post pages.

#### Static site generation

[Section titled “Static site generation”](#static-site-generation)

In this section, you’ll use the [Static (SSG) Mode](/en/guides/routing/#static-ssg-mode) with Astro.

First, create a file `[slug].astro` in `/src/pages/blog/` which needs to export a function `getStaticPaths` that collects all data from the CMS:

src/pages/blog/\[slug].astro

```astro
---
import { deliveryClient } from '../../lib/kontent';
import type { BlogPost } from '../../models';
import { contentTypes } from '../../models/project/contentTypes';


export async function getStaticPaths() {
    const blogPosts = await deliveryClient
        .items<BlogPost>()
        .type(contentTypes.blog_post.codename)
        .toPromise()
---
```

So far, the function fetches all blog posts from Kontent.ai. The code snippet is exactly the same as what you used on the home page.

Next, the function must export paths and data for each blog post. You named the file `[slug].astro`, so the param which represents the URL slug is called `slug`:

src/pages/blog/\[slug].astro

```diff
---
import { deliveryClient } from '../../lib/kontent';
import type { BlogPost } from '../../models';
import { contentTypes } from '../../models/project/contentTypes';


export async function getStaticPaths() {
    const blogPosts = await deliveryClient
        .items<BlogPost>()
        .type(contentTypes.blog_post.codename)
        .toPromise()


    +return blogPosts.data.items.map(blogPost => ({
+        params: { slug: blogPost.elements.url_slug.value },
+        props: { blogPost }
+    }))
}
---
```

The last part is to provide the HTML template and display each blog post:

src/pages/blog/\[slug].astro

```diff
---
import { deliveryClient } from '../../lib/kontent';
import type { BlogPost } from '../../models';
import { contentTypes } from '../../models/project/contentTypes';


export async function getStaticPaths() {
    const blogPosts = await deliveryClient
        .items<BlogPost>()
        .type(contentTypes.blog_post.codename)
        .toPromise()


    return blogPosts.data.items.map(blogPost => ({
        params: { slug: blogPost.elements.url_slug.value },
        props: { blogPost }
    }))
}


+const blogPost: BlogPost = Astro.props.blogPost
+---
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>{blogPost.elements.title.value}</title>
    </head>
    <body>
        <article>
            <h1>{blogPost.elements.title.value}</h1>
            +<Fragment set:html={blogPost.elements.teaser.value} />
            +<Fragment set:html={blogPost.elements.content.value} />
            <time>{new Date(blogPost.elements.date.value ?? "")}</time>
    </body>
</html>
```

Navigate to your Astro preview (<http://localhost:4321/blog/astro-is-amazing/> by default) to see the rendered blog post.

#### On-demand rendering

[Section titled “On-demand rendering”](#on-demand-rendering)

If your routes are [rendered on demand](/en/guides/on-demand-rendering/), you will use dynamic routes to fetch the page data from Kontent.ai.

Create a new file `[slug].astro` in `/src/pages/blog/` and add the following code. The data fetching is very similar to previous use cases but adds an `equalsFilter` that lets us find the right blog post based on the used URL:

src/pages/blog/\[slug].astro

```astro
---
import { deliveryClient } from '../../lib/kontent';
import type { BlogPost } from '../../models';
import { contentTypes } from '../../models/project/contentTypes';


const { slug } = Astro.params
let blogPost: BlogPost;
try {
    const data = await deliveryClient
        .items<BlogPost>()
        .equalsFilter(contentTypes.blog_post.elements.url_slug.codename, slug ?? '')
        .type(contentTypes.blog_post.codename)
        .limitParameter(1)
        .toPromise()
    blogPost = data.data.items[0]
} catch (error) {
    return Astro.redirect('/404')
}
---
```

If you’re not using generated types, you can instead use string literals to define the content item type and the filtered element codename:

```ts
const data = await deliveryClient
        .items()
        .equalsFilter("url_slug", slug ?? '')
        .type("blog_post")
        .limitParameter(1)
        .toPromise()
```

Lastly, add the HTML code to render the blog post. This part is the same as with static generation:

src/pages/blog/\[slug].astro

```diff
---
import { deliveryClient } from '../../lib/kontent';
import type { BlogPost } from '../../models';
import { contentTypes } from '../../models/project/contentTypes';


const { slug } = Astro.params
let blogPost: BlogPost;
try {
    const data = await deliveryClient
        .items<BlogPost>()
        .equalsFilter(contentTypes.blog_post.elements.url_slug.codename, slug ?? '')
        .type(contentTypes.blog_post.codename)
        .limitParameter(1)
        .toPromise()
    blogPost = data.data.items[0]
} catch (error) {
    return Astro.redirect('/404')
}
---
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        <title>{blogPost.elements.title.value}</title>
    </head>
    <body>
        <article>
            <h1>{blogPost.elements.title.value}</h1>
            +<Fragment set:html={blogPost.elements.teaser.value} />
            +<Fragment set:html={blogPost.elements.content.value} />
            <time>{new Date(blogPost.elements.date.value ?? '')}</time>
    </body>
</html>
```

### Publishing your site

[Section titled “Publishing your site”](#publishing-your-site)

To deploy your website, visit the [deployment guides](/en/guides/deploy/) and follow the instructions for your preferred hosting provider.

#### Rebuild on Kontent.ai changes

[Section titled “Rebuild on Kontent.ai changes”](#rebuild-on-kontentai-changes)

If your project is using Astro’s default static mode, you will need to set up a webhook to trigger a new build when your content changes. If you are using Netlify or Vercel as your hosting provider, you can use its webhook feature to trigger a new build from Kontent.ai events.

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

##### Adding a webhook to Kontent.ai

[Section titled “Adding a webhook to Kontent.ai”](#adding-a-webhook-to-kontentai)

In the [Kontent.ai app](https://kontent.ai/learn/docs/webhooks/javascript), go to **Environment settings -> Webhooks**. Click on **Create new webhook** and provide a name for your new webhook. Paste in the URL you copied from Netlify or Vercel and select which events should trigger the webhook. By default, for rebuilding your site when published content changes, you only need **Publish** and **Unpublish** events under **Delivery API triggers**. When you’re finished, click on Save.

Now, whenever you publish a new blog post in Kontent.ai, a new build will be triggered and your blog will be updated.

# microCMS & Astro

> Add content to your Astro project using microCMS

[microCMS](https://microcms.io/en) is an API-based headless CMS that lets you define content using schemas, and manage it using the dashboard.

## Official Resources

[Section titled “Official Resources”](#official-resources)

* Check out [the official microCMS document](https://document.microcms.io/tutorial/astro/astro-top)
* Blog: [Build a blog with microCMS](https://blog.microcms.io/astro-microcms-introduction/)


---

**Navigation:** [← Previous](./02-actions.md) | [Index](./index.md) | [Next →](./04-optimizely-cms-astro.md)
