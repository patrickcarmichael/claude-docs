---
title: "Overview of multipage apps"
source: https://docs.streamlit.io/develop/concepts/multipage-apps/overview
section: 28
---

# Overview of multipage apps

Source: https://docs.streamlit.io/develop/concepts/multipage-apps/overview


Streamlit provides two built-in mechanisms for creating multipage apps. The simplest method is to use a `pages/` directory. However, the preferred and more customizable method is to use `st.navigation`.

## `st.Page` and `st.navigation`

If you want maximum flexibility in defining your multipage app, we recommend using `st.Page` and `st.navigation`. With `st.Page` you can declare any Python file or `Callable` as a page in your app. Furthermore, you can define common elements for your pages in your entrypoint file (the file you pass to `streamlit run`). With these methods, your entrypoint file becomes like a picture frame shared by all your pages.

You must include `st.navigation` in your entrypoint file to configure your app's navigation menu. This is also how your entrypoint file serves as the router between your pages.

## `pages/` directory

If you're looking for a quick and simple solution, just place a `pages/` directory next to your entrypoint file. For every Python file in your `pages/` directory, Streamlit will create an additional page for your app. Streamlit determines the page labels and URLs from the file name and automatically populates a navigation menu at the top of your app's sidebar.

```python
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```python
Streamlit determines the page order in navigation from the filenames. You can use numerical prefixes in the filenames to adjust page order. For more information, see [How pages are sorted in the sidebar](/develop/concepts/multipage-apps/pages-directory#how-pages-are-sorted-in-the-sidebar). If you want to customize your navigation menu with this option, you can deactivate the default navigation through [configuration](/develop/api-reference/configuration/config.toml) (`client.showSidebarNavigation = false`). Then, you can use `st.page_link` to manually contruct a custom navigation menu. With `st.page_link`, you can change the page label and icon in your navigation menu, but you can't change the URLs of your pages.

## Page terminology

A page has four identifying pieces as follows:

- **Page source**: This is a Python file or callable function with the page's source code.
- **Page label**: This is how the page is identified within the navigation menu. See <i>{{ verticalAlign: "-.25em" }} class="material-icons-sharp"&gt;looks_one</i>

---

[← Previous](27-multipage-apps.md) | [Index](index.md) | [Next →](index.md)
