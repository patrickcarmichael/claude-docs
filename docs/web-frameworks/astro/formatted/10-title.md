---
title: "Title"
section: 10
---

# Title


This is my page, written in **Markdown.**
```jsx
Read more about [Markdown](/en/guides/markdown-content/) in Astro.

## HTML Pages

[Section titled “HTML Pages”](#html-pages)

Files with the `.html` file extension can be placed in the `src/pages/` directory and used directly as pages on your site. Note that some key Astro features are not supported in [HTML Components](/en/basics/astro-components/#html-components).

## Custom 404 Error Page

[Section titled “Custom 404 Error Page”](#custom-404-error-page)

For a custom 404 error page, you can create a `404.astro` or `404.md` file in `src/pages`.

This will build to a `404.html` page. Most [deploy services](/en/guides/deploy/) will find and use it.

## Custom 500 Error Page

[Section titled “Custom 500 Error Page”](#custom-500-error-page)

For a custom 500 error page to show for pages that are [rendered on demand](/en/guides/on-demand-rendering/), create the file `src/pages/500.astro`. This custom page is not available for prerendered pages.

If an error occurs rendering this page, your host’s default 500 error page will be shown to your visitor.

**Added in:** `astro@4.10.3`

During development, if you have a `500.astro`, the error thrown at runtime is logged in your terminal, as opposed to being shown in the error overlay.

### `error`

[Section titled “error”](#error)

**Added in:** `astro@4.11.0`

`src/pages/500.astro` is a special page that is automatically passed an `error` prop for any error thrown during rendering. This allows you to use the details of an error (e.g. from a page, from middleware, etc.) to display information to your visitor.

The `error` prop’s data type can be anything, which may affect how you type or use the value in your code:

src/pages/500.astro

```astro
---
interface Props {
  error: unknown;
}


const { error } = Astro.props;
---
<div>{error instanceof Error ? error.message : "Unknown error"}</div>
```jsx
To avoid leaking sensitive information when displaying content from the `error` prop, consider evaluating the error first, and returning appropriate content based on the error thrown. For example, you should avoid displaying the error’s stack as it contains information about how your code is structured on the server.

## Page Partials

[Section titled “Page Partials”](#page-partials)

**Added in:** `astro@3.4.0`

Caution

Page partials are intended to be used in conjunction with a front-end library, such as [htmx](https://htmx.org/) or [Unpoly](https://unpoly.com/). You can also use them if you are comfortable writing low-level front-end JavaScript. For this reason they are an advanced feature.

Additionally, partials should not be used if the component contains scoped styles or scripts, as these elements will be stripped from the HTML output. If you need scoped styles, it is better to use regular, non-partial pages along with a frontend library that knows how to merge the contents into the head.

Partials are page components located within `src/pages/` that are not intended to render as full pages.

Like components located outside of this folder, these files do not automatically include the `<!DOCTYPE html>` declaration, nor any `<head>` content such as scoped styles and scripts.

However, because they are located in the special `src/pages/` directory, the generated HTML is available at a URL corresponding to its file path. This allows a rendering library (e.g. [htmx](https://htmx.org/), [Stimulus](https://stimulus.hotwired.dev/), [jQuery](https://jquery.com/)) to access it on the client and load sections of HTML dynamically on a page without a browser refresh or page navigation.

Partials, when combined with a rendering library, provide an alternative to [Astro islands](/en/concepts/islands/) and [`<script>` tags](/en/guides/client-side-scripts/) for building dynamic content in Astro.

Page files that can export a value for [`partial`](/en/reference/routing-reference/#partial) (e.g. `.astro` and `.mdx`, but not `.md`) can be marked as partials.

src/pages/partial.astro

```diff
---
+export const partial = true;
---
<li>I'm a partial!</li>
```jsx
### Using with a library

[Section titled “Using with a library”](#using-with-a-library)

Partials are used to dynamically update a section of a page using a library such as [htmx](https://htmx.org/).

The following example shows an `hx-post` attribute set to a partial’s URL. The content from the partial page will be used to update the targeted HTML element on this page.

src/pages/index.astro

```astro
<html>
  <head>
    <title>My page</title>
    <script src="https://unpkg.com/htmx.org@1.9.6"
      integrity="sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni"
      crossorigin="anonymous"></script>
  </head>
  <body>
    <section>
      <div id="parent-div">Target here</div>


      <button hx-post="/partials/clicked/"
        hx-trigger="click"
        hx-target="#parent-div"
        hx-swap="innerHTML"
      >
        Click Me!
      </button>
    </section>
  </body>
</html>
```jsx
The `.astro` partial must exist at the corresponding file path, and include an export defining the page as a partial:

src/pages/partials/clicked.astro

```astro
---
export const partial = true;
---
<div>I was clicked!</div>
```jsx
See the [htmx documentation](https://htmx.org/docs/) for more details on using htmx.

---

[← Previous](09-pages.md) | [Index](index.md) | [Next →](index.md)
