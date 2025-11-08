**Navigation:** [← Previous](./07-amplitude.md) | [Index](./index.md) | [Next →](./09-pages.md)

# PDF exports
Source: https://mintlify.com/docs/optimize/pdf-exports

Export your docs as a single PDF file

export const DownloadPDFButton = () => {
  return <a download="mintlify-example.pdf" href="/files/mint-full-docs.pdf" className="border border-zinc-200 dark:border-zinc-800 hover:bg-zinc-100 dark:hover:bg-zinc-700 transition-colors w-fit text-sm font-medium flex items-center gap-2 rounded-lg px-3.5 py-1.5 not-prose">
            <Icon icon="download" size={16} />
            View Example PDF
        </a>;
};


<Info>
  PDF exports are available on [Custom plans](https://mintlify.com/pricing).
</Info>

You can export your docs as a single PDF file for offline viewing. The PDF will contain all the content in the docs, including images and links, and a navigable table of contents.


## Exporting a PDF

1. Navigate to the [General](https://dashboard.mintlify.com/settings/deployment/general) page in the Project Settings section of your dashboard.
2. Select the **Export all content** button.
3. Optionally, customize the export options:
   * **Page format**: Choose the page size of the PDF.
   * **Scale percentage**: Adjust the scale of the PDF.
   * **Include footer**: Include a footer with the page number and total pages.
4. Select **Export** to start the export process.
5. Once the export is complete, you will receive an email with a download link.
6. Click the download link to download the PDF file.

<DownloadPDFButton />



# SEO
Source: https://mintlify.com/docs/optimize/seo

SEO best practices and meta tag configuration for better search visibility

Mintlify automatically handles many SEO best practices, including:

* Meta tag generation
* Sitemap and `robots.txt` file generation
* Semantic HTML structure
* Mobile optimization

You can fully customize your site's meta tags by adding the `metatags` field to your `docs.json` or a page's frontmatter.


## Global meta tags

To set default meta tags for all pages, add the `metatags` field to your `docs.json`.

```json  theme={null}
"seo": {
    "metatags": {
        "og:image": "link to your default meta tag image"
    }
}
```

### Set a canonical URL

If you're using a custom domain, set the `canonical` meta tag to ensure search engines index your preferred domain. A canonical URL tells search engines which version of your documentation is the primary one. This improves SEO when your documentation is accessible from multiple URLs and prevents issues with duplicate content.

```json  theme={null}
"seo": {
    "metatags": {
        "canonical": "https://www.your-custom-domain-here.com"
    }
}
```


## Page-specific meta tags

To set page-specific meta tags, add them to a page's frontmatter.

```mdx  theme={null}
---
title: "Your example page title"
"og:image": "link to your meta tag image"
---
```

<Note>
  Meta tags with colons must be wrapped in quotes.
</Note>


## Common meta tags reference

Below is a comprehensive list of meta tags you can add to your `docs.json`. These meta tags help improve your site's SEO, social sharing, and browser compatibility.

<Note>
  The `og:image` adds a background image that Mintlify automatically overlays with your logo, page title, and description when generating social media previews.
</Note>

You can preview how your meta tags will appear on different platforms using [metatags.io](https://metatags.io/).

```json expandable theme={null}
"seo": {
    "metatags": {
      "robots": "noindex",
      "charset": "UTF-8",
      "viewport": "width=device-width, initial-scale=1.0",
      "description": "Page description",
      "keywords": "keyword1, keyword2, keyword3",
      "author": "Author Name",
      "robots": "index, follow",
      "googlebot": "index, follow",
      "google": "notranslate",
      "google-site-verification": "verification_token",
      "generator": "Mintlify",
      "theme-color": "#000000",
      "color-scheme": "light dark",
      "canonical": "https://your-custom-domain-here.com",
      "format-detection": "telephone=no",
      "referrer": "origin",
      "refresh": "30",
      "rating": "general",
      "revisit-after": "7 days",
      "language": "en",
      "copyright": "Copyright 2024",
      "reply-to": "email@example.com",
      "distribution": "global",
      "coverage": "Worldwide",
      "category": "Technology",
      "target": "all",
      "HandheldFriendly": "True",
      "MobileOptimized": "320",
      "apple-mobile-web-app-capable": "yes",
      "apple-mobile-web-app-status-bar-style": "black",
      "apple-mobile-web-app-title": "App Title",
      "application-name": "App Name",
      "msapplication-TileColor": "#000000",
      "msapplication-TileImage": "path/to/tile.png",
      "msapplication-config": "path/to/browserconfig.xml",
      "og:title": "Open Graph Title",
      "og:type": "website",
      "og:url": "https://example.com",
      "og:image": "https://example.com/image.jpg",
      "og:description": "Open Graph Description",
      "og:site_name": "Site Name",
      "og:locale": "en_US",
      "og:video": "https://example.com/video.mp4",
      "og:audio": "https://example.com/audio.mp3",
      "twitter:card": "summary",
      "twitter:site": "@username",
      "twitter:creator": "@username",
      "twitter:title": "Twitter Title",
      "twitter:description": "Twitter Description",
      "twitter:image": "https://example.com/image.jpg",
      "twitter:image:alt": "Image Description",
      "twitter:player": "https://example.com/player",
      "twitter:player:width": "480",
      "twitter:player:height": "480",
      "twitter:app:name:iphone": "App Name",
      "twitter:app:id:iphone": "12345",
      "twitter:app:url:iphone": "app://",
      "article:published_time": "2024-01-01T00:00:00+00:00",
      "article:modified_time": "2024-01-02T00:00:00+00:00",
      "article:expiration_time": "2024-12-31T00:00:00+00:00",
      "article:author": "Author Name",
      "article:section": "Technology",
      "article:tag": "tag1, tag2, tag3",
      "book:author": "Author Name",
      "book:isbn": "1234567890",
      "book:release_date": "2024-01-01",
      "book:tag": "tag1, tag2, tag3",
      "profile:first_name": "John",
      "profile:last_name": "Doe",
      "profile:username": "johndoe",
      "profile:gender": "male",
      "music:duration": "205",
      "music:album": "Album Name",
      "music:album:disc": "1",
      "music:album:track": "1",
      "music:musician": "Artist Name",
      "music:song": "Song Name",
      "music:song:disc": "1",
      "music:song:track": "1",
      "video:actor": "Actor Name",
      "video:actor:role": "Role Name",
      "video:director": "Director Name",
      "video:writer": "Writer Name",
      "video:duration": "120",
      "video:release_date": "2024-01-01",
      "video:tag": "tag1, tag2, tag3",
      "video:series": "Series Name"
  }
}
```


## Sitemaps and robots.txt files

Mintlify automatically generates a `sitemap.xml` file and a `robots.txt` file. You can view your sitemap by appending `/sitemap.xml` to your documentation site's URL.

Only pages included in your `docs.json` are included by default. To include hidden links, add `seo.indexing` to your `docs.json`:

```json  theme={null}
"seo": {
    "indexing": "all"
}
```

### Custom sitemaps and robots.txt files

To add a custom `sitemap.xml` or `robots.txt` file, create a `sitemap.xml` or `robots.txt` file at the root of your project. Adding a custom file will override the automatically generated file of the same name. If you delete a custom file, the default file will be used again.


## Disabling indexing

If you want to stop a page from being indexed by search engines, you can include the following in the [frontmatter](/organize/pages) of your page:

```
---
noindex: true
---
```

You can also specify `noindex` for all pages in your docs by setting the `metatags.robots` field to `"noindex"` in your `docs.json`:

```json  theme={null}
"seo": {
    "metatags": {
      "robots": "noindex"
    }
  }
```


## SEO best practices

<AccordionGroup>
  <Accordion title="Write descriptive titles and descriptions">
    * Use clear, descriptive page titles (50-60 characters)
    * Write compelling descriptions (150-160 characters)
    * Include relevant keywords
    * Make each page title and description unique
  </Accordion>

  <Accordion title="Optimize your content structure">
    * Use proper heading hierarchy (H1 → H2 → H3)
    * Write for humans first, search engines second
    * Include relevant keywords in headings and content
    * Keep URLs short, descriptive, and organized hierarchically
    * Break up long content with subheadings and lists
  </Accordion>

  <Accordion title="Internal linking strategy">
    * Link to related pages within your documentation
    * Use descriptive anchor text instead of "click here"
    * Create topic clusters by linking related concepts
    * Use the automatic cross-referencing features
  </Accordion>

  <Accordion title="Image SEO">
    * Use descriptive file names for images
    * Always include alt text for accessibility and SEO
    * Optimize image file sizes for faster loading
    * Use relevant images that support your content
  </Accordion>
</AccordionGroup>



# Hidden pages
Source: https://mintlify.com/docs/organize/hidden-pages

Exclude pages from your navigation

Hidden pages are removed from your site's navigation but remain publicly accessible to anyone who knows their URL.

Use hidden pages for content that you want to be accessible on your site or referenced as context for AI tools, but not discoverable through the navigation.

For content requiring strict access control, you must configure [authentication](/deploy/authentication-setup).

If you want to hide pages for specific groups of users, use personalization to control [page visibility](/authentication-personalization/overview#page-visibility).


## Hiding a page

A page is hidden if it is not included in your `docs.json` navigation. To hide a page, remove it from your navigation structure.

Hidden pages use the same URL structure as regular pages based on their file path. For example,  `guides/hidden-page.mdx` would be accessible at `docs.yoursite.com/guides/hidden-page`.

See an [example of a hidden page](/organize/hidden-page-example).

<Note>
  Some navigation elements like sidebars, dropdowns, and tabs may appear empty or shift layout on hidden pages.
</Note>


## Hiding a group of pages

A group of pages is hidden if the `hidden` property is set to `true` in your `docs.json` file:

```json highlight={4} theme={null}
"groups": [
  {
    "group": "Getting started",
    "hidden": true,
    "pages": [
      "index",
      "quickstart"
    ]
  },
  {
    "group": "Guides",
    "pages": [
      "guides/hidden-page.mdx",
      "guides/hidden-groups.mdx"
    ]
  }
]
```

In this example, the `Getting started` group is hidden, but the `Guides` group is visible.

### Hiding a tab

You can also hide a tab by adding the `hidden` property to your `docs.json` file:

```json highlight={4} theme={null}
"tabs": [
  {
    "tab": "Home",
    "hidden": true,
    "pages": [
      "index",
      "quickstart"
    ]
  }
]
```


## Search, SEO, and AI indexing

By default, hidden pages are excluded from indexing for search engines, internal search within your docs, and as context for the AI assistant. To include hidden pages in search results and as context for the assistant, add the `seo` property to your `docs.json`:

```json  theme={null}
"seo": {
    "indexing": "all"
}
```

To exclude a specific page, add `noindex: true` to its frontmatter.



# Navigation
Source: https://mintlify.com/docs/organize/navigation

Structure and customize your documentation's navigation hierarchy

The [navigation](/organize/settings#param-navigation) property in `docs.json` controls the structure and information hierarchy of your documentation.

With proper navigation configuration, you can organize your content so that users can find exactly what they're looking for.


## Pages

Pages are the most fundamental navigation component. Pages map to the MDX files that make up your documentation.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=d9531be8cc28553992a6513ff09fc6ed" alt="Decorative graphic of pages." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/pages-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2db8f5216fadbc2529e0ec8a743265fd 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=09dc67755d46ceb3ff911a45d95058c4 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=5749283323eb0c3208abe91a5a14e96c 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e73de07a1cbb558c6ff95bf97b6bc207 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=8ad884255a152beafea0322628bac7db 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=bf21f5b898cb841789f22af13036bed7 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ec51691241465e13d49afafcd30748f8" alt="Decorative graphic of pages." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/pages-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f8dff2891983f25a79a40bc3f63de2f9 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1f774800d8d7d836752108d9a926cf61 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=432a25d6688814580c3394da4d2b6bec 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=846592b3661ae28ea096e1dc04adba5c 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=99dadd626309bc4e84c980683b695fc6 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/pages-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f0c4200e87a8a6d9e33909e069f87709 2500w" />

In the `navigation` object, `pages` is an array where each entry must reference the path to a [page file](/organize/pages).

```json  theme={null}
{
  "navigation": {
    "pages": [
      "settings",
      "pages",
      "navigation",
      "themes",
      "custom-domain"
    ]
  }
}
```


## Groups

Use groups to organize your sidebar navigation into sections. Groups can be nested within each other, labeled with tags, and styled with icons.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=393243b71cd60407c0ea883359592699" alt="Decorative graphic of groups." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/groups-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=74dbceb9ce6466142c566504f13308ea 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a497f8d624e78db7163b87bcdcd725ed 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=486ed936edbcd3f3c82fd41112b29795 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a564870b1080b14bce2956e5fb21bfb7 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=aa090b3dcc5e7615be9403f5a96176df 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3f36a5e50324061e25c1a4b5623f1e5d 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=834d116249fcd1484808f1a534ea2892" alt="Decorative graphic of groups." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/groups-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c500fba607a47351c01156cab3f33588 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f18b00a1000374cf1f081f711c12bddf 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2153226cd1a1f161c0acdeb9cc5b9a9b 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=785a70ef27c7445fc32cef464a9470a3 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=54ce58ea6498d8ccdcdda831244a7174 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/groups-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4cb4198b9ee2a646880d84085a79e5f0 2500w" />

In the `navigation` object, `groups` is an array where each entry is an object that requires a `group` field and a `pages` field. The `icon`, `tag`, and `expanded` fields are optional.

```json  theme={null}
{
  "navigation": {
    "groups": [
      {
        "group": "Getting started",
        "icon": "play",
        "expanded": false,
        "pages": [
          "quickstart",
          {
            "group": "Editing",
            "icon": "pencil",
            "pages": [
              "installation",
              "editor"
            ]
          }
        ]
      },
      {
        "group": "Writing content",
        "icon": "notebook-text",
        "tag": "NEW",
        "pages": [
          "writing-content/page",
          "writing-content/text"
        ]
      }
    ]
  }
}
```

### Default expanded state

Set `expanded: true` on a group to make it expanded by default in the navigation sidebar. This is useful for highlighting important sections or improving discoverability of key content.

```json  theme={null}
{
  "group": "Getting started",
  "expanded": true,
  "pages": ["quickstart", "installation"]
}
```


## Tabs

Tabs create distinct sections of your documentation with separate URL paths. Tabs create a horizontal navigation bar at the top of your documentation that lets users switch between sections.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=aeec785d0771a3a7a87d941e318bf8e7" alt="Decorative graphic of a tab navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/tabs-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=44db3a117e4dadba2812ed026293ec4c 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=95d524a76d02b4dd6e4b9c2e5157910a 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a5e0660b664cabb23a4188a1b2099279 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=5d043ab331323f717bf74f8ac50bc837 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dc1e6dc28cd92f5daf912a41cad7efe0 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2571ac691b6b25902b7e4805f2b1f2ad 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=20637c7abbe07ee7b2c41c4df26d2ffd" alt="Decorative graphic of a tab navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/tabs-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=65ff357d8274ee8832b87ad372277d22 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=60521760176a9858cdda38e996527977 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3d92566559ae7a0242f70c15b07b3b4e 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e920865af94c8b1818fe99e8e5479373 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=86077985af94418f2ed9d00ed0bf5c5e 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/tabs-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=49df42625a3ed21b24af7c0a1669b020 2500w" />

In the `navigation` object, `tabs` is an array where each entry is an object that requires a `tab` field and can contain other navigation fields such as groups, pages, icons, or links to external pages.

```json  theme={null}
{
  "navigation": {
    "tabs": [
      {
        "tab": "API reference",
        "icon": "square-terminal",
        "pages": [
          "api-reference/get",
          "api-reference/post",
          "api-reference/delete"
        ]
      },
      {
        "tab": "SDKs",
        "icon": "code",
        "pages": [
          "sdk/fetch",
          "sdk/create",
          "sdk/delete"
        ]
      },
      {
        "tab": "Blog",
        "icon": "newspaper",
        "href": "https://external-link.com/blog"
      }
    ]
  }
}
```

### Menus

Menus add dropdown navigation items to a tab. Use menus to help users go directly to specific pages within a tab.

In the `navigation` object, `menu` is an array where each entry is an object that requires an `item` field and can contain other navigation fields such as groups, pages, icons, or links to external pages.

```json  theme={null}
{
  "navigation": {
    "tabs": [
      {
        "tab": "Developer tools",
        "icon": "square-terminal",
        "menu": [
          {
            "item": "API reference",
            "icon": "rocket",
            "groups": [
              {
                "group": "Core endpoints",
                "icon": "square-terminal",
                "pages": [
                  "api-reference/get",
                  "api-reference/post",
                  "api-reference/delete"
                ]
              }
            ]
          },
          {
            "item": "SDKs",
            "icon": "code",
            "description": "SDKs are used to interact with the API.",
            "pages": [
              "sdk/fetch",
              "sdk/create",
              "sdk/delete"
            ]
          }
        ]
      }
    ]
  }
}
```


## Anchors

Anchors add persistent navigation items to the top of your sidebar. Use anchors to section your content, provide quick access to external resources, or create prominent calls to action.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e66255f62fc5d17ca135f21f84ed9325" alt="Decorative graphic of an anchor navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/anchors-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b90cb42b0ef8075f692d641b220088ed 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f077f98104937faf380d95b78d7ab8d8 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=96d89000a37a0d340f83a4c86148b7ac 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=810ae36f9529585b203c24017b6e7c62 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c39bf3a59a82449b6edc0a42861fa57f 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ff075ec9fa56e20fc0ce20ab33363ba2 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=734e33b5fd52071d6f4019b273f2a0e8" alt="Decorative graphic of an anchor navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/anchors-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=804138b1020a62c366c8c9046a7a177f 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9f1af6862f67c1cf5f574ffd5965b2e1 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3923b75a837e054f951db502674a6405 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b7ecfdff230eb3bcaa6d9b533ccbf7eb 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=49605385448f433f5574fb14465aceed 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/anchors-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=099c378f13564d1546543d2ff480d64f 2500w" />

In the `navigation` object, `anchors` is an array where each entry is an object that requires an `anchor` field and can contain other navigation fields such as groups, pages, icons, or links to external pages.

```json  theme={null}
{
  "navigation": {
    "anchors": [
      {
        "anchor": "Documentation",
        "icon": "book-open",
        "pages": [
          "quickstart",
          "development",
          "navigation"
        ]
      },
      {
        "anchor": "API reference",
        "icon": "square-terminal",
        "pages": [
          "api-reference/get",
          "api-reference/post",
          "api-reference/delete"
        ]
      },
      {
        "anchor": "Blog",
        "href": "https://external-link.com/blog"
      }
    ]
  }
}
```

For anchors that direct to external links only, use the `global` keyword. Anchors in a `global` object must have an `href` field and cannot point to a relative path.

Global anchors are particularly useful for linking to resources that are not part of your documentation, but should be readily accessible to your users like a blog or support portal.

```json  theme={null}
{
  "navigation": {
    "global":  {
      "anchors": [
        {
          "anchor": "Community",
          "icon": "house",
          "href": "https://slack.com"
        },
        {
          "anchor": "Blog",
          "icon": "pencil",
          "href": "https://mintlify.com/blog"
        }
      ]
    },
    "tabs": /*...*/
  }
}
```


## Dropdowns

Dropdowns are contained in an expandable menu at the top of your sidebar navigation. Each item in a dropdown directs to a section of your documentation.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f04faa13e4a15c6866b8ceee98362018" alt="Decorative graphic of a dropdown navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/dropdowns-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4f76a3334a021376fa3703230756af7f 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=46d76650848da47b6894b38d2ee09d67 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=62f1fa1374af947e513865fb759cce18 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=266e5e1d0f27c3f97609bc032e88c5f6 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e952ce2feffff6b8df559c071d82797b 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=aeba010d1750c1fa480dc32c2e797fa1 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4ee16248cae08fee00fe98952b599041" alt="Decorative graphic of a dropdown navigation." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/dropdowns-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=beeffd3bc490ceaaf9a237720af031c3 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9c4af73b3edc62f679088374b3723e67 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ba5f681e6c738465482317465f784c83 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=18631bc961347d5b7df58ccc96ef395b 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2db34a0c9628cfa8078b7e7783bae65e 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/dropdowns-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=599243e7328fc167f6cb3a30a5d89dca 2500w" />

In the `navigation` object, `dropdowns` is an array where each entry is an object that requires a `dropdown` field and can contain other navigation fields such as groups, pages, icons, or links to external pages.

```json  theme={null}
{
  "navigation": {
    "dropdowns": [
      {
        "dropdown": "Documentation",
        "icon": "book-open",
        "pages": [
          "quickstart",
          "development",
          "navigation"
        ]
      },
      {
        "dropdown": "API reference",
        "icon": "square-terminal",
        "pages": [
          "api-reference/get",
          "api-reference/post",
          "api-reference/delete"
        ]
      },
      {
        "dropdown": "Blog",
        "href": "https://external-link.com/blog"
      }
    ]
  }
}
```


## Products

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=ab051b15c6e533eb2d723fed8f400704" alt="Decorative graphic of a product switcher." data-og-width="2368" width="2368" data-og-height="640" height="640" data-path="images/navigation/product-switcher-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=280&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=ab0cab024ea2ba147c709581fe05593e 280w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=560&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=2f99b0edb5713eb3ce9e9810613b918d 560w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=840&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=a9de96b748368e9c2a651d4767dca8de 840w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=1100&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=d0e118dc2a52723c807a9f25e4bca7fa 1100w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=1650&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=4a246f9af58fa9872aa9d9ecd5f814c9 1650w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-light.png?w=2500&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=c260adc6ec6a1cb96c4f34918f954247 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=4827f6913945eeadb2c54362ee0f748d" alt="Decorative graphic of a product switcher." data-og-width="2368" width="2368" data-og-height="640" height="640" data-path="images/navigation/product-switcher-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=280&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=1edb6aab64d778cc2d10b6a1c72b12e3 280w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=560&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=1c874eba389a7ad3ef7634fee0ded793 560w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=840&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=2c9437698f48abc836011225f11eb6e8 840w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=1100&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=b702859f95c5cf07af8a4c8bf7e9005f 1100w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=1650&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=99dc0116c85aeaf30cca5857e6fa8d21 1650w, https://mintcdn.com/mintlify/uTIQZECUoznwRp7Y/images/navigation/product-switcher-dark.png?w=2500&fit=max&auto=format&n=uTIQZECUoznwRp7Y&q=85&s=7da59a7b3a1e4c24f27a23eba89728af 2500w" />

Products create a dedicated navigation division for organizing product-specific documentation. Use products to separate different offerings, services, or major feature sets within your documentation.

In the `navigation` object, `products` is an array where each entry is an object that requires a `product` field and can contain other navigation fields such as groups, pages, icons, or links to external pages.

```json  theme={null}
{
  "navigation": {
    "products": [
      {
        "product": "Core API",
        "description": "Core API description",    
        "icon": "api",
        "groups": [
          {
            "group": "Getting started",
            "pages": [
              "core-api/quickstart",
              "core-api/authentication"
            ]
          },
          {
            "group": "Endpoints",
            "pages": [
              "core-api/users",
              "core-api/orders"
            ]
          }
        ]
      },
      {
        "product": "Analytics Platform",
        "description": "Analytics Platform description",
        "icon": "chart-bar",
        "pages": [
          "analytics/overview",
          "analytics/dashboard",
          "analytics/reports"
        ]
      },
      {
        "product": "Mobile SDK",
        "description": "Mobile SDK description",
        "icon": "smartphone",
        "href": "https://mobile-sdk-docs.example.com"
      }
    ]
  }
}
```


## OpenAPI

Integrate OpenAPI specifications directly into your navigation structure to automatically generate API documentation. Create dedicated API sections or place endpoint pages within other navigation components.

Set a default OpenAPI specification at any level of your navigation hierarchy. Child elements will inherit this specification unless they define their own specification.

```json  theme={null}
{
  "navigation": {
    "groups": [
      {
        "group": "API reference",
        "openapi": "/path/to/openapi-v1.json",
        "pages": [
          "overview",
          "authentication",
          "GET /users",
          "POST /users",
          {
            "group": "Products",
            "openapi": "/path/to/openapi-v2.json",
            "pages": [
              "GET /products",
              "POST /products"
            ]
          }
        ]
      }
    ]
  }
}
```

For more information about referencing OpenAPI endpoints in your docs, see the [OpenAPI setup](/api-playground/openapi-setup).


## Versions

Partition your navigation into different versions. Versions are selectable from a dropdown menu.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=85e9cca71a814be044a285028cf9a2a1" alt="Decorative graphic of a version switcher." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/versions-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=ac805634940d94b93cc01a83a3415dd2 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=13947eced5db93445dde66307c3d3e16 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=21f433086887df65435159f7670f866b 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f8790919d989067244f4d665b336f25c 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1594a9a194f551f2f4405c03081128e4 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e68f97860eff952ff6ae1df1bf8f6edc 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fdb637aea218b4035afdaca14dae7d38" alt="Decorative graphic of a version switcher." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/versions-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e356cb4cda5308acb74d38dcbbae20b3 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cbcd2c50c462bd4cb4a5d1317bdbabeb 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=2dcd524d9a5fd747e2e116762f39aab7 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=b9c98a5dd0ba5b89a3949cc661b5b7e1 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0fa61ac6d2bfba325311cf4b74d0b2e8 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/navigation/versions-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5bc24be7ca5c34fe22bf06cf2b731bfd 2500w" />

In the `navigation` object, `versions` is an array where each entry is an object that requires a `version` field and can contain any other navigation fields.

```json  theme={null}
{
  "navigation": {
    "versions": [
      {
        "version": "1.0.0",
        "groups": [
          {
            "group": "Getting started",
            "pages": ["v1/overview", "v1/quickstart", "v1/development"]
          }
        ]
      },
      {
        "version": "2.0.0",
        "groups": [
          {
            "group": "Getting started",
            "pages": ["v2/overview", "v2/quickstart", "v2/development"]
          }
        ]
      }
    ]
  }
}
```


## Languages

Partition your navigation into different languages. Languages are selectable from a dropdown menu.

<img className="block dark:hidden pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e451ef6550588674e26e264ce2cbe399" alt="Decorative graphic of a language switcher." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/languages-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=730e80df21d3d766d12500a4a4db02bf 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3a6020f155b338b2dcb0f559c1deee70 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4c95cc19da42b4d689fcbe302c1245e4 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2fe4a55a4099d7262803494ea394e653 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6d6d1d80dda01c1f877fc3a8cfda52d4 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a61d49e3f45e2fe237afc311edf3eec0 2500w" />

<img className="hidden dark:block pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=99a90032d57cfefe2b46fb0d191391c7" alt="Decorative graphic of a language switcher." data-og-width="1184" width="1184" data-og-height="320" height="320" data-path="images/navigation/languages-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=956fc78d0e5662ae6bd067980858ad9e 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b1c776d783a92c7051b683b2bdbafd05 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=57963c4b57d0db62470034130bc1ed97 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=5c3f84e653fbe81a2ed81f706e71a7d9 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=604f830763dd441731d828ed13f106c3 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6574b753a6501b38f8c5455ab1482ec5 2500w" />

In the `navigation` object, `languages` is an array where each entry is an object that requires a `language` field and can contain any other navigation fields.

We currently support the following languages for localization:

<CardGroup cols={2}>
  <Card title="Arabic (ar)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3d848d9025b508f338803a8ec6e0cfcf" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/ar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=8dfdeb41f11bd5d87dd9d71b352b37a9 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=cc4f66252c7c561a081f5a8b7894810a 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a32ea32bf9c25371d931e5f8314244ad 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=508093f20eac309932e4c0e7b11d7d52 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=768d6d7cea317bc3b1f9de9865c4b8ca 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ar.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=0bc0f2586122ee278f4668a42fef52f7 2500w" />

  <Card title="Chinese (cn)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=77d74a80d5ef3abcbef683a48c26c799" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/cn.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=7cb7ff85b0e1c5a75565d9d7b1b6712e 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=53ef4b2cf40db6adb541f3f872345ac6 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=85e97e67d9c09ad6b82a6f6322a8d823 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9166562056e9f317b652ff1f5f0581e1 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=fc158ef1bf896dd095691baf59dbf9f7 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=60a98106733e83cdee438dbf838f60b6 2500w" />

  <Card title="Chinese (zh-Hant)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=77d74a80d5ef3abcbef683a48c26c799" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/cn.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=7cb7ff85b0e1c5a75565d9d7b1b6712e 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=53ef4b2cf40db6adb541f3f872345ac6 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=85e97e67d9c09ad6b82a6f6322a8d823 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9166562056e9f317b652ff1f5f0581e1 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=fc158ef1bf896dd095691baf59dbf9f7 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/cn.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=60a98106733e83cdee438dbf838f60b6 2500w" />

  <Card title="Dutch (nl)" icon="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=da927dcce7501df5f80aba862868355b" horizontal data-og-width="480" width="480" data-og-height="480" height="480" data-path="images/navigation/languages/nl.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=280&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=2954f43a3433008f1f41d8212b52fe0c 280w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=560&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=4603169369caecb169581b0b198579aa 560w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=840&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=c293b8cca82bc6882466ba28ae13d42f 840w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=1100&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=3298bd1eee26212480821e128e12b56c 1100w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=1650&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=adabb0f5148fd14fa653828d79d970a1 1650w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/nl.png?w=2500&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=58306cdd89068e5c4ba996b72922e5c0 2500w" />

  <Card title="English (en)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=25d8b8c6c7473091d33c16b602eb381a" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/en.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=43106e4828f671a2d331c4299c9f0d12 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=cb8a3627918c9b91d97701a13fa48752 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f2f0129cf09f2f42b1438c41677c20b5 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=eb307cc1a7c16c269210dd3e4a4c1c84 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=26f3353ea1d6d00513952b4ef1318080 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/en.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=8232059d9a40f4b1f5295ad0a1e9b162 2500w" />

  <Card title="French (fr)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ccf6b50a06031c5961d642aeb92d87b1" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/fr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b5bf15c776c532cb02cf1224c09d7ac8 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=7bf1aefa07fc7eb8a5a535129acab6b9 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f1be5f66929a98c8afe99cd5f0f17c5d 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dd7fe27741fd9e388ee5fa359c8dff59 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=725fe0c93f776c6296409757af0b51a5 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/fr.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3ebaece21b7ca56dc078eb1eeadfee99 2500w" />

  <Card title="German (de)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=831c61a2dfd61b73164938b664507542" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/de.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9774c0f321e007df81b72a8502ae77f7 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c4247e53a88be8ebdbe11288e35efd11 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=72683cee9d5b6b8c6b32cb3f9560b01e 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1e518b486fd0ab639fbd3d2205b18cef 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a89ab9b85bf0ee3310e6f65e8e2192f8 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/de.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a02a775133711263b19637fce28aed17 2500w" />

  <Card title="Indonesian (id)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=8fbde287fb60df0d0712f3d0db7aba1b" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=d4f6a0d243652adba7712da0c0618c6d 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f11703204f6d568383ae42954cbf5a02 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c029de7357afc5b6b0b9d24c766f0568 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=79c20714c86b9121ef8f8d179488f498 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=00fe1fd6c1bfb206be0e0e819f58052d 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/id.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=bac23dc437ac6442cb8e71b32069818c 2500w" />

  <Card title="Italian (it)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dc39bd6cd67e91394e03842e588681df" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/it.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c2363c4e60de0cbf8882217ee1d493cd 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=9c893803ca199432fb048f668d5b508c 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6131d392d9ca9f1697b8c01c607a187e 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1d0af0f39688bb30d672ae07216769e0 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=61192618f5a18aa1ed7c612d09385f4e 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/it.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=cae2ebab5f04bf39ca71676879f98bda 2500w" />

  <Card title="Japanese (jp)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=69b17ac2f3202e4bf28945e8408f67e3" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/jp.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=515b8cd6c9cc4d0c2fbdcda9e4d03566 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e224c98305cd827c29922ecef85f073b 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dc46b21d09daf0296566fef11893a6a8 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=37dbe287e55ba730932e6e51b1178612 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=676675bbdab27bce259d02c27ef1a295 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/jp.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b527890f1d528856b2af89329eeba943 2500w" />

  <Card title="Korean (ko)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a555f0a68a4beb076b3556a7f0264b5e" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/ko.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f0049a59c540b61522bf373767c2ec4f 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=06a5563faecb730441bef9d6bf4e145e 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e0e89730373372e99b93524e3a98d9e5 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=7b74ae76e0562908eb0949c117ecc0a1 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f72a3a03edb5c859805223e0b59e3762 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ko.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b57dae2cf9913209850e392eec1f4896 2500w" />

  <Card title="Latvian (lv)" icon="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=61c384db51dc61621e62f4c565935b02" horizontal data-og-width="480" width="480" data-og-height="480" height="480" data-path="images/navigation/languages/lv.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=280&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=f137bcc24a4cb7e590d507e14ef5d48b 280w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=560&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=09f96fe2b02bff20f93a5e2f82d8eea4 560w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=840&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=49549c2dcc9941724797a7a2d4411a25 840w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=1100&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=89cd30014733c980364048f6965a8ffd 1100w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=1650&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=47ff00cd21608e3a50a74019084ae142 1650w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/lv.png?w=2500&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=7380e95741cc0b4916f2942480554df1 2500w" />

  <Card title="Norwegian (no)" icon="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=993784e6321e0da6be58d4b8451a9425" horizontal data-og-width="480" width="480" data-og-height="480" height="480" data-path="images/navigation/languages/no.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=280&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=4c01e553f1d016c8127f79e8f992d098 280w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=560&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=82fa617b7244c3ef905b505aebdf184d 560w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=840&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=6aff9976cbe49416c96aab2f0bbc5fea 840w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=1100&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=1eee250237671f18cf908e62a8eb0d5a 1100w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=1650&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=71ef4c5e51afceccf983bad349800140 1650w, https://mintcdn.com/mintlify/4vDiMoxdniYs_vyk/images/navigation/languages/no.png?w=2500&fit=max&auto=format&n=4vDiMoxdniYs_vyk&q=85&s=856db890494c6af2b60031de5b5a12fa 2500w" />

  <Card title="Portuguese (pt-BR)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=96a015424865291e54cefc8633cc8d78" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/pt-br.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3525bfcf2bb95304c1ed63022a1c37b6 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=616f16566a7b664cec324ee891855397 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dde63286da0a42f62a9df1f00ab72743 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4b6c453f871ec5d10fc52430f62fbb3b 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=0df8d0132693370190cccb03f18a76e9 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/pt-br.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e416cc093a778465f1d02cf304ad9c57 2500w" />

  <Card title="Russian (ru)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=0f52006163f89fe293525925000eb554" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/ru.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=070e0ec6bebb4a79dffa3e2f2d187dbc 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=a40c6f0973c34293655ebbeba57e31a4 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=263c30bbc1658f720d23b73851560734 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=32a6f903bce0cf5df373f229668fad94 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=66997201548c8095cfd3986891f8f7a8 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/ru.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=4326c6ce2649805214ea8615f23d05de 2500w" />

  <Card title="Spanish (es)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=14af4f5bf5e19c20d2062465ca6b9011" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/es.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=89d7f6c2106f2e8b70c0e66c53fad279 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=96210753a16d61705cd67a5df2d4bb3c 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ca7be75f469bec964e90a7a0e2750415 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=2bc2d75129f3846646a00cb0cf30d662 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c57b12eb043a297b953cd1dae38db985 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/es.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=497a3d025fdebd8f839241fd28fa2abd 2500w" />

  <Card title="Swedish (sv)" icon="https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=b62a991d880845b46daa65220ca451b5" horizontal data-og-width="480" width="480" data-og-height="480" height="480" data-path="images/navigation/languages/sv.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=280&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=d186128df23f1fa94917eeaf3c0a31f2 280w, https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=560&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=a61e5c8032736d15638b29d2069c4303 560w, https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=840&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=8e969cc3f2efc135938aeaabe552f4c3 840w, https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=1100&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=b48089ab9a10516117eff6d6a33c3fd0 1100w, https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=1650&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=00c8309ae0fdf8020576b1593c01f0bb 1650w, https://mintcdn.com/mintlify/bbYdWMDGyp4158HR/images/navigation/languages/sv.png?w=2500&fit=max&auto=format&n=bbYdWMDGyp4158HR&q=85&s=76ef53b965bb4069e4e19f922908b0f1 2500w" />

  <Card title="Turkish (tr)" icon="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e52a73a891fa250497c853c557b0a91f" horizontal data-og-width="60" width="60" data-og-height="60" height="60" data-path="images/navigation/languages/tr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1c866ff160da61a0f05b563a5c615ce6 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=827c78ee57518688cc09b77dff22083f 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=b65aa07cd206d1081afe8d9684cbd06d 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=768ca64d1cc99b5f242219beeb9e3aa2 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=17dee5e3bb9056e1f4b4ca5aadcda720 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/navigation/languages/tr.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=7479495e964c43795d15871fcb23268d 2500w" />
</CardGroup>

```json  theme={null}
{
  "navigation": {
    "languages": [
      {
        "language": "en",
        "groups": [
          {
            "group": "Getting started",
            "pages": ["en/overview", "en/quickstart", "en/development"]
          }
        ]
      },
      {
        "language": "es",
        "groups": [
          {
            "group": "Getting started",
            "pages": ["es/overview", "es/quickstart", "es/development"]
          }
        ]
      }
    ]
  }
}
```

For automated translations, [contact our sales team](mailto:gtm@mintlify.com) to discuss solutions.


## Nesting

You can use any combination of anchors, tabs, dropdowns, and products. The components can be nested within each other interchangeably to create your desired navigation structure.

<CodeGroup>
  ```json Anchors theme={null}
  {
    "navigation": {
      "anchors": [
        {
          "anchor": "Anchor 1",
          "groups": [
            {
              "group": "Group 1",
              "pages": [
                "some-folder/file-1",
                "another-folder/file-2",
                "just-a-file"
              ]
            }
          ]
        },
        {
          "anchor": "Anchor 2",
          "groups": [
            {
              "group": "Group 2",
              "pages": [
                "some-other-folder/file-1",
                "various-different-folders/file-2",
                "another-file"
              ]
            }
          ]
        }
      ]
    }
  }
  ```

  ```json Tabs theme={null}
  {
    "navigation": {
      "tabs": [
        {
          "tab": "Tab 1",
          "groups": [
            {
              "group": "Group 1",
              "pages": [
                "some-folder/file-1",
                "another-folder/file-2",
                "just-a-file"
              ]
            }
          ]
        },
        {
          "tab": "Tab 2",
          "groups": [
            {
              "group": "Group 2",
              "pages": [
                "some-other-folder/file-1",
                "various-different-folders/file-2",
                "another-file"
              ]
            }
          ]
        }
      ]
    }
  }
  ```

  ```json Tabs with external anchor theme={null}
  {
    "navigation": {
      "global": {
        "anchors": [
          {
            "anchor": "Anchor 1",
            "href": "https://mintlify.com/docs"
          }
        ]
      },
      "tabs": [
        {
          "tab": "Tab 1",
          "groups": [
            {
              "group": "Group 1",
              "pages": [
                "some-folder/file-1",
                "another-folder/file-2",
                "just-a-file"
              ]
            }
          ]
        },
        {
          "tab": "Tab 2",
          "groups": [
            {
              "group": "Group 2",
              "pages": [
                "some-other-folder/file-1",
                "various-different-folders/file-2",
                "another-file"
              ]
            }
          ]
        }
      ]
    }
  }
  ```
</CodeGroup>


## Breadcrumbs

Breadcrumbs display the full navigation path at the top of pages. Some themes have breadcrumbs enabled by default and others do not. You can control whether breadcrumbs are enabled for your site using the `styling` property in your `docs.json`.

<CodeGroup>
  ```json Display full breadcrumbs theme={null}
  "styling": {
    "eyebrows": "breadcrumbs"
  }
  ```

  ```json Display parent section only theme={null}
  "styling": {
    "eyebrows": "section"
  }
  ```
</CodeGroup>


## Interaction configuration

Control how users interact with navigation elements using the `interaction` property in your `docs.json`.

### Enable auto-navigation for groups

When a user expands a navigation group, some themes will automatically navigate to the first page in the group. You can override a theme's default behavior using the `drilldown` option.

* Set to `true` to force automatic navigation to the first page when a navigation group is selected.
* Set to `false` to prevent navigation and only expand or collapse the group when it is selected.
* Leave unset to use the theme's default behavior.

<CodeGroup>
  ```json Force navigation theme={null}
  "interaction": {
    "drilldown": true  // Force navigation to first page when a user expands a dropdown
  }
  ```

  ```json Prevent navigation theme={null}
  "interaction": {
    "drilldown": false // Never navigate, only expand or collapse the group
  }
  ```
</CodeGroup>



---
**Navigation:** [← Previous](./07-amplitude.md) | [Index](./index.md) | [Next →](./09-pages.md)
