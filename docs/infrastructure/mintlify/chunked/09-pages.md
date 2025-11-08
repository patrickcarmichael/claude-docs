**Navigation:** [← Previous](./08-pdf-exports.md) | [Index](./index.md) | [Next →](./10-create-agent-job.md)

# Pages
Source: https://mintlify.com/docs/organize/pages

Pages are the building blocks of your documentation

Each page is an MDX file, which combines Markdown content with React components to let you create rich, interactive documentation.


## Page metadata

Every page starts with frontmatter, the YAML metadata enclosed by `---` at the beginning of a file. This metadata defines how your page appears and behaves.

Use frontmatter to control:

* Page titles and descriptions
* Sidebar titles, icons, and tags
* Page layouts
* SEO meta tags
* Custom metadata

<ResponseField name="title" type="string" required>
  The title of your page that appears in navigation and browser tabs.
</ResponseField>

<ResponseField name="description" type="string">
  A brief description of what this page covers. Appears under the title and improves SEO.
</ResponseField>

<ResponseField name="sidebarTitle" type="string">
  A short title that displays in the sidebar navigation.
</ResponseField>

<ResponseField name="icon" type="string">
  The icon to display.

  Options:

  * [Font Awesome icon](https://fontawesome.com/icons) name
  * [Lucide icon](https://lucide.dev/icons) name
  * URL to an externally hosted icon
  * Path to an icon file in your project
</ResponseField>

<ResponseField name="iconType" type="string">
  The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

  Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
</ResponseField>

<ResponseField name="tag" type="string">
  A tag that appears next to your page title in the sidebar.
</ResponseField>

<ResponseField name="<custom>" type="string">
  Any valid YAML frontmatter. For example, `product: "API"` or `version: "1.0.0"`.
</ResponseField>

```yaml Example YAML frontmatter wrap theme={null}
---
title: "About frontmatter"
description: "Frontmatter is the metadata that controls how your page appears and behaves"
sidebarTitle: "Frontmatter"
icon: "book"
tag: "NEW"
---
```


## Page mode

Control how your page displays with the `mode` setting.

### Default

If no mode is defined, defaults to a standard layout with a sidebar navigation and table of contents.

```yaml  theme={null}
---
title: "Default page title"
---
```

### Wide

Wide mode hides the table of contents. This is useful for pages that do not have any headings or if you prefer to use the extra horizontal space. Wide mode is available for all themes.

```yaml  theme={null}
---
title: "Wide page title"
mode: "wide"
---
```

### Custom

Custom mode provides a minimalist layout that removes all elements except for the top navbar. Custom mode is a blank canvas to create landing pages or any other unique layouts that you want to have minimal navigation elements for. Custom mode is available for all themes.

```yaml  theme={null}
---
title: "Custom page title"
mode: "custom"
---
```

### Frame

Frame mode provides a layout similar to custom mode, but preserves the sidebar navigation. This page mode allows for custom HTML and components while maintaining the default navigation experience. Frame mode is only available for Aspen and Almond themes.

```yaml  theme={null}
---
title: "Frame page title"
mode: "frame"
---
```

### Center

Center mode removes the sidebar and table of contents, centering the content. This is useful for changelogs or other pages where you want to emphasize the content. Center mode is available for Mint and Linden themes.

```yaml  theme={null}
---
title: "Center page title"
mode: "center"
---
```


## API pages

Create interactive API playgrounds by adding an API specification to your frontmatter, `api` or `openapi`.

```yaml  theme={null}
---
openapi: "GET /endpoint"
---
```

Learn more about building [API documentation](/api-playground/overview).


## External links

Link to external sites directly from your navigation with the `url` metadata.

```yaml  theme={null}
---
title: "npm Package"
url: "https://www.npmjs.com/package/mint"
---
```


## Search engine optimization

Most SEO meta tags are automatically generated. You can set SEO meta tags manually to improve your site's SEO, social sharing, and browser compatibility.

<Note>
  Meta tags with colons must be wrapped in quotes.
</Note>

```yaml  theme={null}
---
"twitter:image": "/images/social-preview.jpg"
---
```

See [SEO](/optimize/seo) for complete SEO metadata options.


## Internal search keywords

Enhance a specific page's discoverability in the built-in search by providing `keywords` in your metadata. These keywords won't appear as part of the page content or in search results, but users that search for them will be shown the page as a result.

```yaml  theme={null}
---
keywords: ['configuration', 'setup', 'getting started']
---
```



# Global settings
Source: https://mintlify.com/docs/organize/settings

Configure site-wide settings with the `docs.json` file

The `docs.json` file lets you turn a collection of Markdown files into a navigable, customized documentation site. This required configuration file controls styling, navigation, integrations, and more. Think of it as the blueprint for your documentation.

Settings in `docs.json` apply globally to all pages.


## Setting up your `docs.json`

To get started, you only need to specify `theme`, `name`, `colors.primary`, and `navigation`. Other fields are optional and you can add them as your documentation needs grow.

For the best editing experience, include the schema reference at the top of your `docs.json` file. This enables autocomplete, validation, and helpful tooltips in most code editors:

```json  theme={null}
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "Your Docs",
  "colors": {
    "primary": "#ff0000"
  },
  "navigation": {
    // Your navigation structure
  }
  // The rest of your configuration
}
```


## Reference

This section contains the full reference for the `docs.json` file.

### Customization

<ResponseField name="theme" required>
  The layout theme of your site.

  One of the following: `mint`, `maple`, `palm`, `willow`, `linden`, `almond`, `aspen`.

  See [Themes](/customize/themes) for more information.
</ResponseField>

<ResponseField name="name" type="string" required>
  The name of your project, organization, or product.
</ResponseField>

<ResponseField name="colors" type="object" required>
  The colors used in your documentation. Colors are applied differently across themes. If you only provide a primary color, it will be used for all color elements.

  <Expandable title="Colors">
    <ResponseField name="primary" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$" required>
      The primary color for your documentation. Generally used for emphasis in light mode, with some variation by theme.

      Must be a hex code beginning with `#`.
    </ResponseField>

    <ResponseField name="light" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
      The color used for emphasis in dark mode.

      Must be a hex code beginning with `#`.
    </ResponseField>

    <ResponseField name="dark" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
      The color used for buttons and hover states across both light and dark modes, with some variation by theme.

      Must be a hex code beginning with `#`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="description" type="string">
  Description of your site for SEO and AI indexing.
</ResponseField>

<ResponseField name="logo" type="string or object">
  Set your logo for both light and dark mode.

  <Expandable title="Logo">
    <ResponseField name="light" type="string" required>
      Path pointing to your logo file for light mode. Include the file extension. Example: `/logo.png`
    </ResponseField>

    <ResponseField name="dark" type="string" required>
      Path pointing to your logo file for dark mode. Include the file extension. Example: `/logo-dark.png`
    </ResponseField>

    <ResponseField name="href" type="string (uri)">
      The URL to redirect to when clicking the logo. If not provided, the logo will link to your homepage. Example: `https://mintlify.com`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="favicon" type="string or object">
  Path to your favicon file, including the file extension. Automatically resized to appropriate favicon sizes. Can be a single file or separate files for light and dark mode. Example: `/favicon.png`

  <Expandable title="Favicon">
    <ResponseField name="light" type="string" required>
      Path to your favicon file for light mode. Include the file extension. Example: `/favicon.png`
    </ResponseField>

    <ResponseField name="dark" type="string" required>
      Path to your favicon file for dark mode. Include the file extension. Example: `/favicon-dark.png`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="thumbnails" type="object">
  Thumbnail customization for social media and page previews.

  <Expandable title="Thumbnails">
    <ResponseField name="appearance" type="&#x22;light&#x22; | &#x22;dark&#x22;">
      The visual theme of your thumbnails. If not specified, thumbnails use your site's color scheme defined by the `colors` field.
    </ResponseField>

    <ResponseField name="background" type="string">
      Background image for your thumbnails. Can be a relative path or absolute URL.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="styling" type="object">
  Visual styling configurations.

  <Expandable title="Styling">
    <ResponseField name="eyebrows" type="&#x22;section&#x22; | &#x22;breadcrumbs&#x22;">
      The style of the page eyebrow. Choose `section` to show the section name or `breadcrumbs` to show the full navigation path. Defaults to `section`.
    </ResponseField>

    <ResponseField name="codeblocks" type="&#x22;system&#x22; | &#x22;dark&#x22; | string | object">
      Code block theme configuration. Defaults to `"system"`.

      **Simple configuration:**

      * `"system"`: Match current site mode (light or dark)
      * `"dark"`: Always use dark mode

      **Custom theme configuration:**

      * Use a string to specify a single [Shiki theme](https://shiki.style/themes) for all code blocks
      * Use an object to specify separate [Shiki themes](https://shiki.style/themes) for light and dark modes

      <ResponseField name="theme" type="string">
        A single Shiki theme name to use for both light and dark modes.

        ```json  theme={null}
        "styling": {
          "codeblocks": {
            "theme": "dracula"
          }
        }
        ```
      </ResponseField>

      <ResponseField name="theme" type="object">
        Separate themes for light and dark modes.

        <Expandable title="theme">
          <ResponseField name="light" type="string" required>
            A Shiki theme name for light mode.
          </ResponseField>

          <ResponseField name="dark" type="string" required>
            A Shiki theme name for dark mode.
          </ResponseField>

          ```json  theme={null}
          "styling": {
            "codeblocks": {
              "theme": {
                "light": "github-light",
                "dark": "github-dark"
              }
            }
          }
          ```
        </Expandable>
      </ResponseField>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="icons" type="object">
  Icon library settings.

  <Expandable title="Icons">
    <ResponseField name="library" type="&#x22;fontawesome&#x22; | &#x22;lucide&#x22;" required>
      Icon library to use throughout your documentation. Defaults to `fontawesome`.

      <Note>
        You can specify a URL to an externally hosted icon, path to an icon file in your project, or JSX-compatible SVG code for any individual icon, regardless of the library setting.
      </Note>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="fonts" type="object">
  Set custom fonts for your documentation. The default font varies by theme.

  <Expandable title="Fonts">
    <ResponseField name="family" type="string" required>
      Font family, such as "Open Sans." [Google Fonts](https://fonts.google.com) family names are supported.
    </ResponseField>

    <ResponseField name="weight" type="number">
      Font weight, such as 400 or 700. Variable fonts support precise weights such as 550.
    </ResponseField>

    <ResponseField name="source" type="string (uri)">
      One of:

      * URL to a hosted font, such as [https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2](https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2).
      * Path to a local font file, such as `/fonts/Hubot-Sans.woff2`.

      [Google Fonts](https://fonts.google.com) are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
    </ResponseField>

    <ResponseField name="format" type="&#x22;woff&#x22; | &#x22;woff2&#x22;">
      Font file format. Required when using the `source` field.
    </ResponseField>

    <ResponseField name="heading" type="object">
      Override font settings specifically for headings.

      <Expandable title="Heading">
        <ResponseField name="family" type="string" required>
          Font family, such as "Open Sans", "Playfair Display." [Google Fonts](https://fonts.google.com) family names are supported.
        </ResponseField>

        <ResponseField name="weight" type="number">
          Font weight, such as 400, 700. Variable fonts support precise weights such as 550.
        </ResponseField>

        <ResponseField name="source" type="string (uri)">
          One of:

          * URL to a hosted font, such as [https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2](https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2).
          * Path to a local font file, such as `/fonts/Hubot-Sans.woff2`.

          [Google Fonts](https://fonts.google.com) are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
        </ResponseField>

        <ResponseField name="format" type="&#x22;woff&#x22; | &#x22;woff2&#x22;">
          Font file format. Required when using the `source` field.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="body" type="object">
      Override font settings specifically for body text.

      <Expandable title="Body">
        <ResponseField name="family" type="string" required>
          Font family, such as "Open Sans", "Playfair Display." [Google Fonts](https://fonts.google.com) family names are supported.
        </ResponseField>

        <ResponseField name="weight" type="number">
          Font weight, such as 400, 700. Variable fonts support precise weights such as 550.
        </ResponseField>

        <ResponseField name="source" type="string (uri)">
          One of:

          * URL to a hosted font, such as [https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2](https://mintlify-assets.b-cdn.net/fonts/Hubot-Sans.woff2).
          * Path to a local font file, such as `/fonts/Hubot-Sans.woff2`.

          [Google Fonts](https://fonts.google.com) are loaded automatically when you specify a Google Font `family` name, so no source URL is needed.
        </ResponseField>

        <ResponseField name="format" type="&#x22;woff&#x22; | &#x22;woff2&#x22;">
          Font file format. Required when using the `source` field.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="appearance" type="object">
  Light/dark mode toggle settings.

  <Expandable title="Appearance">
    <ResponseField name="default" type="&#x22;system&#x22; | &#x22;light&#x22; | &#x22;dark&#x22;">
      Default theme mode. Choose `system` to match users' OS settings, or `light` or `dark` to force a specific mode. Defaults to `system`.
    </ResponseField>

    <ResponseField name="strict" type="boolean">
      Whether to hide the light/dark mode toggle. Defaults to `true`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="background" type="object">
  Background color and decoration settings.

  <Expandable title="Background">
    <ResponseField name="image" type="string or object">
      Background image for your site. Can be a single file or separate files for light and dark mode.

      <Expandable title="Image">
        <ResponseField name="light" type="string" required>
          Path to your background image for light mode. Include the file extension. Example: `/background.png`.
        </ResponseField>

        <ResponseField name="dark" type="string" required>
          Path to your background image for dark mode. Include the file extension. Example: `/background-dark.png`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="decoration" type="&#x22;gradient&#x22; | &#x22;grid&#x22; | &#x22;windows&#x22;">
      Background decoration for your theme.
    </ResponseField>

    <ResponseField name="color" type="object">
      Custom background colors for light and dark modes.

      <Expandable title="Color">
        <ResponseField name="light" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
          Background color for light mode.

          Must be a hex code beginning with `#`.
        </ResponseField>

        <ResponseField name="dark" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
          Background color for dark mode.

          Must be a hex code beginning with `#`.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

### Structure

<ResponseField name="navbar" type="object">
  Navigation bar items to external links.

  <Expandable title="Navbar">
    <ResponseField name="links" type="array of object">
      Links to display in the navbar

      <Expandable title="Links">
        <ResponseField name="label" type="string" required>
          Text for the link.
        </ResponseField>

        <ResponseField name="href" type="string (uri)" required>
          Link destination. Must be a valid external URL.
        </ResponseField>

        <ResponseField name="icon" type="string">
          The icon to display.

          Options:

          * [Font Awesome icon](https://fontawesome.com/icons) name
          * [Lucide icon](https://lucide.dev/icons) name
          * JSX-compatible SVG code wrapped in curly braces
          * URL to an externally hosted icon
          * Path to an icon file in your project

          For custom SVG icons:

          1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
          2. Paste your SVG code into the SVG input field.
          3. Copy the complete `<svg>...</svg>` element from the JSX output field.
          4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
          5. Adjust `height` and `width` as needed.
        </ResponseField>

        <ResponseField name="iconType" type="string">
          The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

          Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="primary" type="object">
      Primary button in the navbar.

      <Expandable title="Primary">
        <ResponseField name="type" type="&#x22;button&#x22; | &#x22;github&#x22;" required>
          Button style. Choose `button` for a standard button with a label or `github` for a link to a GitHub repository with icon.
        </ResponseField>

        <ResponseField name="label" type="string" required>
          Button text. Only applies when `type` is `button`.
        </ResponseField>

        <ResponseField name="href" type="string (uri)" required>
          Button destination. Must be an external URL. If `type` is `github`, must be a GitHub repository URL.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="navigation" type="object" required>
  The navigation structure of your content.

  <Expandable title="Navigation">
    <ResponseField name="global" type="object">
      Global navigation elements that appear across all pages and sections.

      <Expandable title="Global">
        <ResponseField name="languages" type="array of object">
          Language switcher configuration for localized sites.

          <Expandable title="Languages">
            <ResponseField name="language" type="&#x22;en&#x22; | &#x22;cn&#x22; | &#x22;zh&#x22; | &#x22;zh-Hans&#x22; | &#x22;zh-Hant&#x22; | &#x22;es&#x22; | &#x22;fr&#x22; | &#x22;ja&#x22; | &#x22;jp&#x22; | &#x22;pt&#x22; | &#x22;pt-BR&#x22; | &#x22;de&#x22; | &#x22;ko&#x22; | &#x22;it&#x22; | &#x22;ru&#x22; | &#x22;id&#x22; | &#x22;ar&#x22; | &#x22;tr&#x22;" required>
              Language code in ISO 639-1 format
            </ResponseField>

            <ResponseField name="default" type="boolean">
              Whether this is the default language.
            </ResponseField>

            <ResponseField name="hidden" type="boolean">
              Whether to hide this language option by default.
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              A valid path or external link to this language version of your documentation.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="versions" type="array of object">
          Version switcher configuration for multi-version sites.

          <Expandable title="Versions">
            <ResponseField name="version" type="string" required>
              Display name of the version.

              Minimum length: 1
            </ResponseField>

            <ResponseField name="default" type="boolean">
              Whether this is the default version.
            </ResponseField>

            <ResponseField name="hidden" type="boolean">
              Whether to hide this version option by default.
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              URL or path to this version of your documentation.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="tabs" type="array of object">
          Top-level navigation tabs for organizing major sections.

          <Expandable title="Tabs">
            <ResponseField name="tab" type="string" required>
              Display name of the tab.

              Minimum length: 1
            </ResponseField>

            <ResponseField name="icon" type="string">
              The icon to display.

              Options:

              * [Font Awesome icon](https://fontawesome.com/icons) name
              * [Lucide icon](https://lucide.dev/icons) name
              * JSX-compatible SVG code wrapped in curly braces
              * URL to an externally hosted icon
              * Path to an icon file in your project

              For custom SVG icons:

              1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
              2. Paste your SVG code into the SVG input field.
              3. Copy the complete `<svg>...</svg>` element from the JSX output field.
              4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
              5. Adjust `height` and `width` as needed.
            </ResponseField>

            <ResponseField name="iconType" type="string">
              The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

              Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
            </ResponseField>

            <ResponseField name="hidden" type="boolean">
              Whether to hide this tab by default.
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              URL or path for the tab destination.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="anchors" type="array of object">
          Anchored links that appear prominently in the sidebar navigation.

          <Expandable title="Anchors">
            <ResponseField name="anchor" type="string" required>
              Display name of the anchor.

              Minimum length: 1
            </ResponseField>

            <ResponseField name="icon" type="string">
              The icon to display.

              Options:

              * [Font Awesome icon](https://fontawesome.com/icons) name
              * [Lucide icon](https://lucide.dev/icons) name
              * JSX-compatible SVG code wrapped in curly braces
              * URL to an externally hosted icon
              * Path to an icon file in your project

              For custom SVG icons:

              1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
              2. Paste your SVG code into the SVG input field.
              3. Copy the complete `<svg>...</svg>` element from the JSX output field.
              4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
              5. Adjust `height` and `width` as needed.
            </ResponseField>

            <ResponseField name="iconType" type="string">
              The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

              Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
            </ResponseField>

            <ResponseField name="color" type="object">
              Custom colors for the anchor.

              <Expandable title="Color">
                <ResponseField name="light" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
                  Anchor color for light mode.

                  Must be a hex code beginning with `#`.
                </ResponseField>

                <ResponseField name="dark" type="string matching ^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$">
                  Anchor color for dark mode.

                  Must be a hex code beginning with `#`.
                </ResponseField>
              </Expandable>
            </ResponseField>

            <ResponseField name="hidden" type="boolean">
              Whether to hide this anchor by default.
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              URL or path for the anchor destination.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="dropdowns" type="array of object">
          Dropdown menus for organizing related content.

          <Expandable title="Dropdowns">
            <ResponseField name="dropdown" type="string" required>
              Display name of the dropdown.

              Minimum length: 1
            </ResponseField>

            <ResponseField name="icon" type="string">
              The icon to display.

              Options:

              * [Font Awesome icon](https://fontawesome.com/icons) name
              * [Lucide icon](https://lucide.dev/icons) name
              * JSX-compatible SVG code wrapped in curly braces
              * URL to an externally hosted icon
              * Path to an icon file in your project

              For custom SVG icons:

              1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
              2. Paste your SVG code into the SVG input field.
              3. Copy the complete `<svg>...</svg>` element from the JSX output field.
              4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
              5. Adjust `height` and `width` as needed.
            </ResponseField>

            <ResponseField name="iconType" type="string">
              The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

              Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
            </ResponseField>

            <ResponseField name="hidden" type="boolean">
              Whether to hide this dropdown by default.
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              URL or path for the dropdown destination.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="products" type="array of object">
          Products for organizing content into sections.

          <Expandable title="Products">
            <ResponseField name="product" type="string" required>
              Display name of the product.
            </ResponseField>

            <ResponseField name="description" type="string">
              Description of the product.
            </ResponseField>

            <ResponseField name="icon" type="string">
              The icon to display.

              Options:

              * [Font Awesome icon](https://fontawesome.com/icons) name
              * [Lucide icon](https://lucide.dev/icons) name
              * JSX-compatible SVG code wrapped in curly braces
              * URL to an externally hosted icon
              * Path to an icon file in your project

              For custom SVG icons:

              1. Convert your SVG using the [SVGR converter](https://react-svgr.com/playground/).
              2. Paste your SVG code into the SVG input field.
              3. Copy the complete `<svg>...</svg>` element from the JSX output field.
              4. Wrap the JSX-compatible SVG code in curly braces: `icon={<svg ...> ... </svg>}`.
              5. Adjust `height` and `width` as needed.
            </ResponseField>

            <ResponseField name="iconType" type="string">
              The [Font Awesome](https://fontawesome.com/icons) icon style. Only used with Font Awesome icons.

              Options: `regular`, `solid`, `light`, `thin`, `sharp-solid`, `duotone`, `brands`.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="languages" type="array of object">
      Language switcher for [multi-language](/organize/navigation#languages) sites.
    </ResponseField>

    <ResponseField name="versions" type="array of object">
      Version switcher for sites with multiple [versions](/organize/navigation#versions).
    </ResponseField>

    <ResponseField name="tabs" type="array of object">
      Top-level navigation [tabs](/organize/navigation#tabs).
    </ResponseField>

    <ResponseField name="anchors" type="array of object">
      Sidebar [anchors](/organize/navigation#anchors).
    </ResponseField>

    <ResponseField name="dropdowns" type="array of object">
      [Dropdowns](/organize/navigation#dropdowns) for grouping related content.
    </ResponseField>

    <ResponseField name="products" type="array of object">
      Product switcher for sites with multiple [products](/organize/navigation#products).
    </ResponseField>

    <ResponseField name="groups" type="array of object">
      [Groups](/organize/navigation#groups) for organizing content into sections.
    </ResponseField>

    <ResponseField name="pages" type="array of string or object">
      Individual [pages](/organize/navigation#pages) that make up your documentation.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="interaction" type="object">
  User interaction settings for navigation elements.

  <Expandable title="Interaction">
    <ResponseField name="drilldown" type="boolean">
      Control automatic navigation behavior when selecting navigation groups. Set to `true` to force navigation to the first page when a navigation group is expanded. Set to `false` to prevent navigation and only expand or collapse the group. Leave unset to use the theme's default behavior.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="footer" type="object">
  Footer content and social media links.

  <Expandable title="Footer">
    <ResponseField name="socials" type="object">
      Social media profiles to display in the footer. Each key is a platform name and each value is your profile URL. For example:

      ```json  theme={null}
      {
        "x": "https://x.com/mintlify"
      }
      ```

      Valid property names: `x`, `website`, `facebook`, `youtube`, `discord`, `slack`, `github`, `linkedin`, `instagram`, `hacker-news`, `medium`, `telegram`, `twitter`, `x-twitter`, `earth-americas`, `bluesky`, `threads`, `reddit`, `podcast`
    </ResponseField>

    <ResponseField name="links" type="array of object">
      Links to display in the footer.

      <Expandable title="Links">
        <ResponseField name="header" type="string">
          Header title for the column.

          Minimum length: 1
        </ResponseField>

        <ResponseField name="items" type="array of object" required>
          Links to display in the column.

          <Expandable title="Items">
            <ResponseField name="label" type="string" required>
              Link text.

              Minimum length: 1
            </ResponseField>

            <ResponseField name="href" type="string (uri)" required>
              Link destination URL.
            </ResponseField>
          </Expandable>
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="banner" type="object">
  Site-wide banner displayed at the top of pages.

  <Expandable title="Banner">
    <ResponseField name="content" type="string">
      The content of the banner. Supports plain text and Markdown formatting. For example:

      ```json  theme={null}
      {
        "content": "🚀 Banner is live! [Learn more](mintlify.com)"
      }
      ```
    </ResponseField>

    <ResponseField name="dismissible" type="boolean">
      Whether users can dismiss the banner. Defaults to `false`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="redirects" type="array of object">
  Redirects for moved, renamed, or deleted pages.

  <Expandable title="Redirects">
    <ResponseField name="source" type="string" required>
      Source path to redirect from. Example: `/old-page`
    </ResponseField>

    <ResponseField name="destination" type="string" required>
      Destination path to redirect to. Example: `/new-page`
    </ResponseField>

    <ResponseField name="permanent" type="boolean">
      Whether to use a permanent redirect (301). Defaults to `true`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="contextual" type="object">
  Contextual menu for AI-optimized content and integrations.

  <Expandable title="Contextual">
    <ResponseField name="options" type="array of &#x22;copy&#x22; | &#x22;view&#x22; | &#x22;chatgpt&#x22; | &#x22;claude&#x22; | &#x22;perplexity&#x22; | &#x22;mcp&#x22; | &#x22;cursor&#x22; | &#x22;vscode&#x22;" required>
      Actions available in the contextual menu. The first option appears as the default.

      * `copy`: Copy the current page as Markdown to the clipboard.
      * `view`: View the current page as Markdown in a new tab.
      * `chatgpt`: Send the current page content to ChatGPT.
      * `claude`: Send the current page content to Claude.
      * `perplexity`: Send the current page content to Perplexity.
      * `mcp`: Copies your MCP server URL to the clipboard.
      * `cursor`: Installs your hosted MCP server in Cursor.
      * `vscode`: Installs your hosted MCP server in VSCode.

      <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=8833b554020642ceb0495df962ae833b" alt="Contextual Menu" className="rounded-xl" data-og-width="1348" width="1348" data-og-height="824" height="824" data-path="images/page-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=7a0efdfd96e69fa3c8ebd6e9f99f4b00 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=47d1dbd6083d226fed80f4b72f4222c9 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=41ba28c312c712498667ec1ccefe19dc 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=88343286a1eefd010a309e6d0149c1f6 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9aa4f98ec00564bfd1411d94185a5942 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/page-context-menu.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=47ed706ae17656ec0f2ad1d58d024a0b 2500w" />

      <Note>
        The contextual menu is only available on preview and production deployments.
      </Note>
    </ResponseField>
  </Expandable>
</ResponseField>

### API Configurations

<ResponseField name="api" type="object">
  API documentation and interactive playground settings.

  <Expandable title="Api">
    <ResponseField name="openapi" type="string or array or object">
      OpenAPI specification files for generating API documentation. Can be a single URL/path or an array of URLs/paths.

      <Expandable title="Openapi">
        <ResponseField name="source" type="string">
          URL or path to your OpenAPI specification file.

          Minimum length: 1
        </ResponseField>

        <ResponseField name="directory" type="string">
          Directory to search for OpenAPI files.

          Do not include a leading slash.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="asyncapi" type="string or array or object">
      AsyncAPI specification files for generating API documentation. Can be a single URL/path or an array of URLs/paths.

      <Expandable title="Asyncapi">
        <ResponseField name="source" type="string">
          URL or path to your AsyncAPI specification file.

          Minimum length: 1
        </ResponseField>

        <ResponseField name="directory" type="string">
          Directory to search for AsyncAPI files.

          Do not include a leading slash.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="params" type="object">
      Display settings for API parameters.

      <Expandable title="Params">
        <ResponseField name="expanded" type="&#x22;all&#x22; | &#x22;closed&#x22;">
          Whether to expand all parameters by default. Defaults to `closed`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="playground" type="object">
      API playground settings.

      <Expandable title="Playground">
        <ResponseField name="display" type="&#x22;interactive&#x22; | &#x22;simple&#x22; | &#x22;none&#x22;">
          The display mode of the API playground. Defaults to `interactive`.
        </ResponseField>

        <ResponseField name="proxy" type="boolean">
          Whether to pass API requests through a proxy server. Defaults to `true`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="examples" type="object">
      Configurations for the autogenerated API examples.

      <Expandable title="Examples">
        <ResponseField name="languages" type="array of string">
          Example languages for the autogenerated API snippets
        </ResponseField>

        <ResponseField name="defaults" type="&#x22;required&#x22; | &#x22;all&#x22;">
          Whether to show optional parameters in API examples. Defaults to `all`.
        </ResponseField>

        <ResponseField name="prefill" type="boolean">
          Whether to prefill the API playground with data from schema examples. When enabled, the playground automatically populates request fields with example values from your OpenAPI specification. Defaults to `false`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="mdx" type="object">
      Configurations for API pages generated from `MDX` files.

      <Expandable title="Mdx">
        <ResponseField name="auth" type="object">
          Authentication configuration for MDX-based API requests.

          <Expandable title="Auth">
            <ResponseField name="method" type="&#x22;bearer&#x22; | &#x22;basic&#x22; | &#x22;key&#x22; | &#x22;cobo&#x22;">
              Authentication method for API requests.
            </ResponseField>

            <ResponseField name="name" type="string">
              Authentication name for API requests.
            </ResponseField>
          </Expandable>
        </ResponseField>

        <ResponseField name="server" type="string or array">
          Server configuration for API requests.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

### SEO and search

<ResponseField name="seo" type="object">
  SEO indexing configurations.

  <Expandable title="Seo">
    <ResponseField name="metatags" type="object">
      Meta tags added to every page. Must be a valid key-value pair. See [common meta tags reference](/optimize/seo#common-meta-tags-reference) for options.
    </ResponseField>

    <ResponseField name="indexing" type="&#x22;navigable&#x22; | &#x22;all&#x22;">
      Specify which pages search engines should index. Choose `navigable` to index only pages that are in your `docs.json` navigation or choose `all` to index every page. Defaults to `navigable`.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="search" type="object">
  Search display settings.

  <Expandable title="Search">
    <ResponseField name="prompt" type="string">
      Placeholder text to display in the search bar.
    </ResponseField>
  </Expandable>
</ResponseField>

### Integrations

<ResponseField name="integrations" type="object">
  Third-party integrations.

  <Expandable title="Integrations">
    <ResponseField name="amplitude" type="object">
      Amplitude analytics integration.

      <Expandable title="Amplitude">
        <ResponseField name="apiKey" type="string" required>
          Your Amplitude API key.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="clearbit" type="object">
      Clearbit data enrichment integration.

      <Expandable title="Clearbit">
        <ResponseField name="publicApiKey" type="string" required>
          Your Clearbit API key.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="fathom" type="object">
      Fathom analytics integration.

      <Expandable title="Fathom">
        <ResponseField name="siteId" type="string" required>
          Your Fathom site ID.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="frontchat" type="object">
      Front chat integration.

      <Expandable title="Frontchat">
        <ResponseField name="snippetId" type="string" required>
          Your Front chat snippet ID.

          Minimum length: 6
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="ga4" type="object">
      Google Analytics 4 integration.

      <Expandable title="Ga4">
        <ResponseField name="measurementId" type="string matching ^G" required>
          Your Google Analytics 4 measurement ID.

          Must match pattern: ^G
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="gtm" type="object">
      Google Tag Manager integration.

      <Expandable title="Gtm">
        <ResponseField name="tagId" type="string matching ^G" required>
          Your Google Tag Manager tag ID.

          Must match pattern: ^G
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="heap" type="object">
      Heap analytics integration.

      <Expandable title="Heap">
        <ResponseField name="appId" type="string" required>
          Your Heap app ID.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="hotjar" type="object">
      Hotjar integration.

      <Expandable title="Hotjar">
        <ResponseField name="hjid" type="string" required>
          Your Hotjar ID.
        </ResponseField>

        <ResponseField name="hjsv" type="string" required>
          Your Hotjar script version.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="intercom" type="object">
      Intercom integration.

      <Expandable title="Intercom">
        <ResponseField name="appId" type="string" required>
          Your Intercom app ID.

          Minimum length: 6
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="logrocket" type="object">
      LogRocket integration.

      <Expandable title="Logrocket">
        <ResponseField name="appId" type="string" required>
          Your LogRocket app ID.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="mixpanel" type="object">
      Mixpanel integration.

      <Expandable title="Mixpanel">
        <ResponseField name="projectToken" type="string" required>
          Your Mixpanel project token.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="osano" type="object">
      Osano integration.

      <Expandable title="Osano">
        <ResponseField name="scriptSource" type="string" required>
          Your Osano script source.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="pirsch" type="object">
      Pirsch analytics integration.

      <Expandable title="Pirsch">
        <ResponseField name="id" type="string" required>
          Your Pirsch ID.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="posthog" type="object">
      PostHog integration.

      <Expandable title="Posthog">
        <ResponseField name="apiKey" type="string matching ^phc\_" required>
          Your PostHog API key.

          Must match pattern: ^phc\_
        </ResponseField>

        <ResponseField name="apiHost" type="string (uri)">
          Your PostHog API host.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="plausible" type="object">
      Plausible analytics integration.

      <Expandable title="Plausible">
        <ResponseField name="domain" type="string" required>
          Your Plausible domain.
        </ResponseField>

        <ResponseField name="server" type="string">
          Your Plausible server.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segment" type="object">
      Segment integration.

      <Expandable title="Segment">
        <ResponseField name="key" type="string" required>
          Your Segment key.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="telemetry" type="object">
      Telemetry settings.

      <Expandable title="Telemetry">
        <ResponseField name="enabled" type="boolean">
          Whether to enable telemetry.

          <Note>
            When set to `false`, feedback features are also disabled and do not appear on your documentation pages.
          </Note>
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="cookies" type="object">
      Cookie settings.

      <Expandable title="Cookies">
        <ResponseField name="key" type="string">
          Key for cookies.
        </ResponseField>

        <ResponseField name="value" type="string">
          Value for cookies.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

### Errors

<ResponseField name="errors" type="object">
  Error handling settings.

  <Expandable title="Errors">
    <ResponseField name="404" type="object">
      404 "Page not found" error handling.

      <Expandable title="404">
        <ResponseField name="redirect" type="boolean">
          Whether to automatically redirect to the home page when a page is not found.
        </ResponseField>

        <ResponseField name="title" type="string">
          Custom title for the 404 error page.
        </ResponseField>

        <ResponseField name="description" type="string">
          Custom description for the 404 error page. Supports Markdown formatting.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>


## Examples

<Tabs>
  <Tab title="Basic example">
    ```json docs.json lines wrap theme={null}
    {
      "$schema": "https://mintlify.com/docs.json",
      "theme": "maple",
      "name": "Example Co.",
      "description": "Example Co. is a company that provides example content and placeholder text.",
      "colors": {
        "primary": "#3B82F6",
        "light": "#F8FAFC",
        "dark": "#0F172A"
      },
      "navigation": {
        "dropdowns": [
          {
            "dropdown": "Documentation",
            "icon": "book",
            "description": "How to use the Example Co. product",
            "groups": [
              {
                "group": "Getting started",
                "pages": [
                  "index",
                  "quickstart"
                ]
              },
              {
                "group": "Customization",
                "pages": [
                  "settings",
                  "users",
                  "features"
                ]
              },
              {
                "group": "Billing",
                "pages": [
                  "billing/overview",
                  "billing/payments",
                  "billing/subscriptions"
                ]
              }
            ]
          },
          {
            "dropdown": "Changelog",
            "icon": "history",
            "description": "Updates and changes",
            "pages": [
              "changelog"
            ]
          }
        ]
      },
      "logo": {
        "light": "/logo-light.svg",
        "dark": "/logo-dark.svg",
        "href": "https://example.com"
      },
      "navbar": {
        "links": [
          {
            "label": "Community",
            "href": "https://example.com/community"
          }
        ],
        "primary": {
          "type": "button",
          "label": "Get Started",
          "href": "https://example.com/start"
        }
      },
      "footer": {
        "socials": {
          "x": "https://x.com/example",
          "linkedin": "https://www.linkedin.com/company/example",
          "github": "https://github.com/example",
          "slack": "https://example.com/community"
        },
        "links": [
          {
            "header": "Resources",
            "items": [
              {
                "label": "Customers",
                "href": "https://example.com/customers"
              },
              {
                "label": "Enterprise",
                "href": "https://example.com/enterprise"
              },
              {
                "label": "Request Preview",
                "href": "https://example.com/preview"
              }
            ]
          },
          {
            "header": "Company",
            "items": [
              {
                "label": "Careers",
                "href": "https://example.com/careers"
              },
              {
                "label": "Blog",
                "href": "https://example.com/blog"
              },
              {
                "label": "Privacy Policy",
                "href": "https://example.com/legal/privacy"
              }
            ]
          }
        ]
      },
      "integrations": {
        "ga4": {
          "measurementId": "G-XXXXXXXXXX"
        },
        "telemetry": {
          "enabled": true
        },
        "cookies": {
          "key": "example_cookie_key",
          "value": "example_cookie_value"
        }
      },
      "contextual": {
        "options": [
          "copy",
          "view",
          "chatgpt",
          "claude"
        ]
      },
      "errors": {
        "404": {
          "redirect": false,
          "title": "I can't be found",
          "description": "What ever **happened** to this _page_?"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Interactive API example">
    ```json docs.json {43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,72,73,74,75,76,77,78,79} lines wrap theme={null}
    {
      "$schema": "https://mintlify.com/docs.json",
      "theme": "maple",
      "name": "Example Co.",
      "description": "Example Co. is a company that provides example content and placeholder text.",
      "colors": {
        "primary": "#3B82F6",
        "light": "#F8FAFC",
        "dark": "#0F172A"
      },
      "navigation": {
        "dropdowns": [
          {
            "dropdown": "Documentation",
            "icon": "book",
            "description": "How to use the Example Co. product",
            "groups": [
              {
                "group": "Getting started",
                "pages": [
                  "index",
                  "quickstart"
                ]
              },
              {
                "group": "Customization",
                "pages": [
                  "settings",
                  "users",
                  "features"
                ]
              },
              {
                "group": "Billing",
                "pages": [
                  "billing/overview",
                  "billing/payments",
                  "billing/subscriptions"
                ]
              }
            ]
          },
          {
            "dropdown": "API reference",
            "icon": "terminal",
            "description": "How to use the Example Co. API",
            "groups": [
              {
                "group": "API reference",
                "pages": [
                  "api-reference/introduction"
                ]
              },
              {
                "group": "Endpoints",
                "openapi": {
                  "source": "openapi.json"
                }
              }
            ]
          },
          {
            "dropdown": "Changelog",
            "icon": "history",
            "description": "Updates and changes",
            "pages": [
              "changelog"
            ]
          }
        ]
      },
      "api": {
        "playground": {
          "display": "interactive"
        },
        "examples": {
          "languages": ["javascript", "curl", "python"]
        }
      },
      "logo": {
        "light": "/logo-light.svg",
        "dark": "/logo-dark.svg",
        "href": "https://example.com"
      },
      "navbar": {
        "links": [
          {
            "label": "Community",
            "href": "https://example.com/community"
          }
        ],
        "primary": {
          "type": "button",
          "label": "Get Started",
          "href": "https://example.com/start"
        }
      },
      "footer": {
        "socials": {
          "x": "https://x.com/example",
          "linkedin": "https://www.linkedin.com/company/example",
          "github": "https://github.com/example",
          "slack": "https://example.com/community"
        },
        "links": [
          {
            "header": "Resources",
            "items": [
              {
                "label": "Customers",
                "href": "https://example.com/customers"
              },
              {
                "label": "Enterprise",
                "href": "https://example.com/enterprise"
              },
              {
                "label": "Request Preview",
                "href": "https://example.com/preview"
              }
            ]
          },
          {
            "header": "Company",
            "items": [
              {
                "label": "Careers",
                "href": "https://example.com/careers"
              },
              {
                "label": "Blog",
                "href": "https://example.com/blog"
              },
              {
                "label": "Privacy Policy",
                "href": "https://example.com/legal/privacy"
              }
            ]
          }
        ]
      },
      "integrations": {
        "ga4": {
          "measurementId": "G-XXXXXXXXXX"
        },
        "telemetry": {
          "enabled": true
        },
        "cookies": {
          "key": "example_cookie_key",
          "value": "example_cookie_value"
        }
      },
      "contextual": {
        "options": [
          "copy",
          "view",
          "chatgpt",
          "claude"
        ]
      },
      "errors": {
        "404": {
          "redirect": false,
          "title": "I can't be found",
          "description": "What ever **happened** to this _page_?"
        }
      }
    }
    ```
  </Tab>

  <Tab title="Multi-language example">
    ```json docs.json lines wrap theme={null}
    {
      "$schema": "https://mintlify.com/docs.json",
      "theme": "maple",
      "name": "Example Co.",
      "description": "Example Co. is a company that provides example content and placeholder text.",
      "colors": {
        "primary": "#3B82F6",
        "light": "#F8FAFC",
        "dark": "#0F172A"
      },
      "navigation": {
        "global": {
          "anchors": [
            {
              "anchor": "Documentation",
              "href": "https://mintlify.com/docs"
            },
            {
              "anchor": "Changelog",
              "href": "https://mintlify.com/docs/changelog"
            }
          ]
        },
        "languages": [ // [!code highlight:3]
          {
            "language": "en",
            "dropdowns": [
              {
                "dropdown": "Documentation",
                "icon": "book",
                "description": "How to use the Example Co. product",
                "pages": [
                  {
                    "group": "Getting started",
                    "pages": ["index", "quickstart"]
                  },
                  {
                    "group": "Customization",
                    "pages": ["settings", "users", "features"]
                  },
                  {
                    "group": "Billing",
                    "pages": [
                      "billing/overview",
                      "billing/payments",
                      "billing/subscriptions"
                    ]
                  }
                ]
              },
              {
                "dropdown": "Changelog",
                "icon": "history",
                "description": "Updates and changes",
                "pages": ["changelog"]
              }
            ]
          },
          {
            "language": "es",// [!code highlight]
            "dropdowns": [
              {
                "dropdown": "Documentación",
                "icon": "book",
                "description": "Cómo usar el producto de Example Co.",
                "pages": [
                  {
                    "group": "Comenzando",
                    "pages": ["es/index", "es/quickstart"]
                  },
                  {
                    "group": "Personalización",
                    "pages": ["es/settings", "es/users", "es/features"]
                  },
                  {
                    "group": "Billing",
                    "pages": [
                      "es/billing/overview",
                      "es/billing/payments",
                      "es/billing/subscriptions"
                    ]
                  }
                ]
              },
              {
                "dropdown": "Changelog",
                "icon": "history",
                "description": "Actualizaciones y cambios",
                "pages": ["es/changelog"]
              }
            ]
          }
        ]
      },
      "logo": {
        "light": "/logo-light.svg",
        "dark": "/logo-dark.svg",
        "href": "https://example.com"
      },
      "navbar": {
        "links": [
          {
            "label": "Community",
            "href": "https://example.com/community"
          }
        ],
        "primary": {
          "type": "button",
          "label": "Get Started",
          "href": "https://example.com/start"
        }
      },
      "footer": {
        "socials": {
          "x": "https://x.com/example",
          "linkedin": "https://www.linkedin.com/company/example",
          "github": "https://github.com/example",
          "slack": "https://example.com/community"
        },
        "links": [
          {
            "header": "Resources",
            "items": [
              {
                "label": "Customers",
                "href": "https://example.com/customers"
              },
              {
                "label": "Enterprise",
                "href": "https://example.com/enterprise"
              },
              {
                "label": "Request Preview",
                "href": "https://example.com/preview"
              }
            ]
          },
          {
            "header": "Company",
            "items": [
              {
                "label": "Careers",
                "href": "https://example.com/careers"
              },
              {
                "label": "Blog",
                "href": "https://example.com/blog"
              },
              {
                "label": "Privacy Policy",
                "href": "https://example.com/legal/privacy"
              }
            ]
          }
        ]
      },
      "integrations": {
        "ga4": {
          "measurementId": "G-XXXXXXXXXX"
        },
        "telemetry": {
          "enabled": true
        },
        "cookies": {
          "key": "example_cookie_key",
          "value": "example_cookie_value"
        }
      },
      "contextual": {
        "options": ["copy", "view", "chatgpt", "claude"]
      },
      "errors": {
        "404": {
          "redirect": false,
          "title": "I can't be found",
          "description": "What ever **happened** to this _page_?"
        }
      }
    }
    ```
  </Tab>
</Tabs>


## Upgrading from `mint.json`

If your docs project uses the deprecated `mint.json` file, follow these steps to upgrade to `docs.json`.

<Steps>
  <Step title="Install or update the CLI">
    If you haven't installed the [CLI](/installation), install it now:

    <CodeGroup>
      ```bash npm theme={null}
      npm i -g mint
      ```

      ```bash yarn theme={null}
      yarn global add mint
      ```

      ```bash pnpm theme={null}
      pnpm add -g mint
      ```
    </CodeGroup>

    If you already have the CLI installed, make sure it is up to date:

    ```bash  theme={null}
    mint update
    ```
  </Step>

  <Step title="Create your docs.json file">
    In your docs repository, run:

    ```bash  theme={null}
    mint upgrade
    ```

    This command will create a `docs.json` file from your existing `mint.json`. Review the generated file to ensure all settings are correct.
  </Step>

  <Step title="Delete your mint.json file">
    After verifying your `docs.json` is configured properly, you can safely delete your old `mint.json` file.
  </Step>
</Steps>



# Quickstart
Source: https://mintlify.com/docs/quickstart

Deploy your documentation in minutes

This quickstart guide shows you how to set up and deploy your documentation site in minutes.

After completing this guide, you will have a live documentation site ready to customize and expand.

<Info>
  **Prerequisites**: Before you begin, [create an account](https://mintlify.com/start) and complete onboarding.
</Info>


## Getting started

After you complete the onboarding process, your documentation site automatically deploys to a unique URL with this format:

```
https://<your-project-name>.mintlify.app
```

Find your URL on the Overview page of your [dashboard](https://dashboard.mintlify.com/).

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=282a86eda5f3ab5d9723b62a330ea2af" alt="Mintlify Domain" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1372" height="1372" data-path="images/quickstart/mintlify-domain-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c4933a71649fc4bb51e8dcf04acd2b24 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0584bdd9f07c8474f288d09cf95422f5 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9ab37f154b08aa9745b80f90513575c6 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0a8096fe65863b7329d7cfa3e4906af1 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=09bd9e97fd49c725767972ff64ef687b 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=7dd2acf06a84d72eb3fbb3bfcecf3d2a 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cd2c945d8bb3c8deb4c655816e72d134" alt="Mintlify Domain" className="hidden dark:block" data-og-width="3008" width="3008" data-og-height="1368" height="1368" data-path="images/quickstart/mintlify-domain-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=16b7491bafd93b20460428137a42786c 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a0f2b6d6c4c4f14c6a0c5477496ca5df 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=58dadc6099408743417376066aff5be9 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f20cfe683670a53e226232593b5c3e21 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a50c22e99c515703cce5aa3ca72a053d 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-domain-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=d480538faf8fde8e3f1955b7e966b0e2 2500w" />
</Frame>

Your site's URL is available immediately. Use this URL for testing and sharing with your team while you are setting up your docs site.

### Install the GitHub App

Mintlify provides a GitHub App that automates deployment when you push changes to your repository.

Install the GitHub App by following the instructions from the onboarding checklist or your dashboard.

1. Navigate to **Settings** in your Mintlify dashboard.
2. Select **GitHub App** from the sidebar.
3. Select **Install GitHub App**. This opens a new tab to the GitHub App installation page.
4. Select the organization or user account where you want to install the app.
5. Select the repositories that you want to connect.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=47bff992030035a04156279e05e419a4" alt="GitHub App Installation" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="910" height="910" data-path="images/quickstart/github-app-installation-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=2f19d0e03136827cb200a81627561d5f 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=54002d522c6325755f480ab2d0d70d47 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a68861931564125105d5cb227d13f87a 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=94bf8837cd595aec5b8325c8932a5c6c 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=5689a6c72f0fe3e384469e4a313f74cd 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=40f4c04a13a6084630ecdd560219e5ca 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=bf9a57882cce0e8ab797adde7e9727f8" alt="GitHub App Installation" className="hidden dark:block" data-og-width="3016" width="3016" data-og-height="906" height="906" data-path="images/quickstart/github-app-installation-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c94c4b055edf403844283dc340df29d0 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=906fff49f4d1b984cfaad5b18f588597 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=6b4545e0325c44a3503a3f3c65c86e12 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=36ed35bfa53cda29a40b12c430c830e8 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4656677dad775a44bff41fc6e072cec3 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/github-app-installation-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=804d257a8efe260cd04511fa3d5b21cb 2500w" />
</Frame>

<Info>
  Update the GitHub App permissions if you move your documentation to a different repository.
</Info>

### Authorize your GitHub account

1. Navigate to **Settings** in your Mintlify dashboard.
2. Select **My Profile** from the sidebar.
3. Select **Authorize GitHub account**. This opens a new tab to the GitHub authorization page.

<Info>
  An admin for your GitHub organization may need to authorize your account depending on your organization settings.
</Info>


## Editing workflows

Mintlify offers two workflows for creating and maintaining your documentation:

<Card title="Code-based workflow" icon="terminal" horizontal href="#code-based-workflow">
  For users who prefer working with existing tools in their local environment. Click to jump to this section.
</Card>

<Card title="Web editor workflow" icon="mouse-pointer-2" horizontal href="#web-editor-workflow">
  For users who prefer a visual interface in their web browser. Click to jump to this section.
</Card>


## Code-based workflow

The code-based workflow integrates with your existing development environment and Git repositories. This workflow is best for technical teams who want to manage documentation alongside code.

### Install the CLI

<Info>
  **Prerequisite**: The CLI requires [Node.js](https://nodejs.org/en) v19 or higher.
</Info>

To work locally with your documentation, install the Command Line Interface (CLI), called [mint](https://www.npmjs.com/package/mint), by running this command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npm i -g mint
  ```

  ```bash pnpm theme={null}
  pnpm add -g mint
  ```
</CodeGroup>

### Create a new project

Run `mint new` to create a new documentation project. See the [CLI installation guide](/installation#create-a-new-project) for details on the command and flags.

### Edit the documentation

After setting up your project, you can start editing your documentation files. For example, update the title of the introduction page:

1. Navigate to your documentation repository.
2. Open `index.mdx` and locate the top of the file:

```mdx index.mdx theme={null}
---
title: "Introduction"
description: "This is the introduction to the documentation"
---
```

3. Update the `title` field to `"Hello World"`.

```mdx index.mdx {2} theme={null}
---
title: "Hello World"
description: "This is the introduction to the documentation"
---
```

### Preview the changes

To preview the changes locally, run the following command:

```bash  theme={null}
mint dev
```

Your preview is available at `localhost:3000`.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=469e00f62b8ec5d64b78aed203819e8d" alt="Mintlify Dev" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1518" height="1518" data-path="images/quickstart/mintlify-dev-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=626c9e9f708040cb0e1854f3bb9a84a6 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=77b2f24de1c2cf450211ca348212300c 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=8c4db5516b5e724c769b8ebf0f1b268d 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=fe77b1fc62d5c3744ddbd3b7bb586629 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=7e91a5c3fa5ad6e4e972a36ba40dadd1 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=8d5bb8f0446788210c1819474b8db008 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=14c30ad3671f2dc7663aefcdf04a78a9" alt="Mintlify Dev" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1518" height="1518" data-path="images/quickstart/mintlify-dev-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=62357e55e3256ec972a2b8f2827278ad 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=caccef9bafe020aa707a0a1b3a5656e1 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c7bf6b3f6fd30be1a64a33e484441ed4 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=3f43419a98a8c298bdbea2d04352dfda 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f7ddf0e7aeed666ca15c83fe18c8b61a 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/mintlify-dev-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e07593be35d411829cdcc8e5df78e09e 2500w" />
</Frame>

### Push the changes

When you are ready to publish your changes, push them to your repository.

Mintlify automatically detects the changes, builds your documentation, and deploys the updates to your site. Monitor the deployment status in your GitHub repository commit history or the [dashboard](https://dashboard.mintlify.com).

After the deployment completes, your latest update will be available at `<your-project-name>.mintlify.app`.

<Card title="Jump to adding a custom domain" icon="arrow-down" href="#adding-a-custom-domain" horizontal>
  Optionally, skip the web editor workflow and jump to adding a custom domain.
</Card>


## Web editor workflow

The web editor workflow provides a what-you-see-is-what-you-get (WYSIWYG) interface for creating and editing documentation. This workflow is best for people who want to work in their web browser without additional local development tools.

### Access the web editor

1. Log in to your [dashboard](https://dashboard.mintlify.com).
2. Select **Editor** on the left sidebar.

<Info>
  If you have not installed the GitHub App, you will be prompted to install the app when you open the web editor.
</Info>

<Frame>
  <img alt="The Mintlify web editor in the visual editor mode" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=55ec9c2a242cf56c2b99c0c4ebdc1e20" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1404" height="1404" data-path="images/quickstart/web-editor-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=af9d42a6c1e419866beefadb00bb4e51 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=64a8cf37238cb409c51c84d1288186eb 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e10c0d7bab08a20fd57118eb1dc5545d 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cce783da931e49536cd6eeeb9001e4dc 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a3f263f08b80905e68056d20cc1e9f70 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c864ecf9f3d349e256c682812f9a85f0 2500w" />

  <img alt="The Mintlify web editor in the visual editor mode" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9cc658981729d4a754b002dc681ce49a" className="hidden dark:block" data-og-width="3011" width="3011" data-og-height="1402" height="1402" data-path="images/quickstart/web-editor-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f800da212280fdf0083042b476b9f6e6 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e465e3a62aa47022d663488ffb8a7419 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=952ed4ab597e0ef686187ae252bdb8b1 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=6218a5a8f1f859c28beb32a483febc69 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c260516766e7f5a7f0c5737684cd7e74 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=cdbcbf887a6f01165d7c6ad2ea015763 2500w" />
</Frame>

### Edit the documentation

In the web editor, you can navigate through your documentation files in the sidebar. Let's update the introduction page:

Find and select `index.mdx` in the file explorer.

Then, in the editor, update the title field to "Hello World".

<Frame>
  <img alt="Editing in Web Editor" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=a65976d79df7d1c2d6e230ef5b1e9912" className="block dark:hidden" data-og-width="3022" width="3022" data-og-height="1130" height="1130" data-path="images/quickstart/web-editor-editing-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=3e67e4e8658db49ae787d4661db1eb46 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=9a7f1989c3013f82865f45b653831f1f 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f0f3e55c6694c7fd09e31151db68cdfc 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=c34eefd1c72bea7a4d0f1728f4eb9e68 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=f4fefa97bd8dfcc4b02ec5803881e207 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4ca29de1822c4541c1885c2f64c2b563 2500w" />

  <img alt="Editing in Web Editor" src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=720832290f7fd70c6bbc2b9dcf1f9d66" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1127" height="1127" data-path="images/quickstart/web-editor-editing-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4306b6d20ea579b0e0a0090409b20118 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=df3e8c4b2e4d8baf5a8d60271c6fb6fe 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=80431291b792c7d9b62a091ab4eae0be 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=0bbee26abdb83c77f0644534395bc484 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=026b397b851f093058eb87f938bf5afa 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/web-editor-editing-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=64ee164c0433f2b086ce4f34b2603d59 2500w" />
</Frame>

<Tip>
  The editor provides a rich set of formatting tools and components. Type <kbd>/</kbd> in the editor to open the command menu and access these tools.
</Tip>

### Publish your changes

When you're satisfied with your edits, select the **Publish** button in the top-right corner. Your changes are immediately deployed to your documentation site.

<Tip>
  Use branches to preview and review changes through pull requests before deploying to your live site.
</Tip>

For more details about using the web editor, including using branches and pull requests to collaborate and preview changes, see our [web editor documentation](/editor).


## Adding a custom domain

While your `<your-project-name>.mintlify.app` subdomain works well for testing and development, most teams prefer using a custom domain for production documentation.

To add a custom domain, navigate to the [Domain Setup](https://dashboard.mintlify.com/settings/deployment/custom-domain) page in your dashboard.

<Frame>
  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=aac0c0fa17f686ffdd99b3052b00987e" alt="Custom Domain" className="block dark:hidden" data-og-width="3024" width="3024" data-og-height="1142" height="1142" data-path="images/quickstart/custom-domain-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=35566c610b9a7104695cf3c1d4d6bb86 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=583db431865eb430468c8bfdeb01330b 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=afd8d17ad542ec01d94d50b3ea32128f 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4eae6e98ed9fef062c92277dabf8b186 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=1fa5bbea13a96f90c2bce380e3503184 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-light.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=793e2c40aba3078492b2eb2320081fb1 2500w" />

  <img src="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=b233a8964e60cd635ca33b22db0c2584" alt="Custom Domain" className="hidden dark:block" data-og-width="3018" width="3018" data-og-height="1140" height="1140" data-path="images/quickstart/custom-domain-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=280&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=eaad48b5f62b5e183becc31565ecacb0 280w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=560&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e0eacda33ed8dd929e48b0fee67c8b68 560w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=840&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=e130fb02bc93220474e0e137ced30966 840w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=1100&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=442aee44f1110303c9753f01fb487b97 1100w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=1650&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=4d10f4f74b67ff1deceb5e6200823cfa 1650w, https://mintcdn.com/mintlify/f7fo9pnTEtzBD70_/images/quickstart/custom-domain-dark.png?w=2500&fit=max&auto=format&n=f7fo9pnTEtzBD70_&q=85&s=179b9771777c2eea4e3035d94e1bb9ab 2500w" />
</Frame>

Enter your domain (for example, `docs.yourcompany.com`) and follow the provided instructions to configure DNS settings with your domain provider.

<Table>
  | Record Type | Name                | Value                | TTL  |
  | ----------- | ------------------- | -------------------- | ---- |
  | CNAME       | docs (or subdomain) | cname.vercel-dns.com | 3600 |
</Table>

<Info>
  DNS changes can take up to 48 hours to propagate, though changes often complete much sooner.
</Info>


## Next steps

Congratulations! You have successfully deployed your documentation site with Mintlify. Here are suggested next steps to enhance your documentation:

<Card title="Configure your global settings" icon="settings" href="organize/settings" horizontal>
  Configure site-wide styling, navigation, integrations, and more with the `docs.json` file.
</Card>

<Card title="Customize your theme" icon="paintbrush" href="customize/themes" horizontal>
  Learn how to customize colors, fonts, and the overall appearance of your documentation site.
</Card>

<Card title="Organize navigation" icon="map" href="organize/navigation" horizontal>
  Structure your documentation with intuitive navigation to help users find what they need.
</Card>

<Card title="Add interactive components" icon="puzzle" href="/components/accordions" horizontal>
  Enhance your documentation with interactive components like accordions, tabs, and code samples.
</Card>

<Card title="Set up API references" icon="code" href="/api-playground/overview" horizontal>
  Create interactive API references with OpenAPI and AsyncAPI specifications.
</Card>


## Troubleshooting

If you encounter issues during the setup process, check these common troubleshooting solutions:

<AccordionGroup>
  <Accordion title="Local preview not working">
    Make sure you have Node.js v19+ installed and that you run the `mint dev` command from the directory containing your `docs.json` file.
  </Accordion>

  <Accordion title="Changes not reflecting on live site">
    Deployment can take upwards to a few minutes. Check your GitHub Actions (for code-based workflow) or deployment logs in the Mintlify dashboard to ensure there are no build errors.
  </Accordion>

  <Accordion title="Custom domain not connecting">
    Verify that your DNS records are set up correctly and allow sufficient time for DNS propagation (up to 48 hours). You can use tools like [DNSChecker](https://dnschecker.org) to verify your CNAME record.
  </Accordion>
</AccordionGroup>



---
**Navigation:** [← Previous](./08-pdf-exports.md) | [Index](./index.md) | [Next →](./10-create-agent-job.md)
