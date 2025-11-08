---
title: "Embed your app"
source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app
section: 316
---

# Embed your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app


Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both [iframe](#embedding-with-iframes) and [oEmbed](#embedding-with-oembed) methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

## Embedding with iframes

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the <a href="https://30days.streamlit.app/" target="_blank">30DaysOfStreamlit app</a>. The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

```javascript
<iframe src="https://30days.streamlit.app?embed=true" style="height: 450px; width: 100%;"/>
```python
<Cloud height="450px" name="30days"/>
<Important>

There will be no official support for embedding private apps.

</Important>

In addition to allowing you to embed apps via iframes, the `?embed=true` query parameter also does the following:

- Removes the toolbar with the app menu icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

[← Previous](315-share-your-app.md) | [Index](index.md) | [Next →](index.md)
