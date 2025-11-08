**Navigation:** [← Previous](./02-define-multipage-apps-with-stpage-and-stnavigation.md) | [Index](./index.md) | [Next →](./04-column-configuration.md)

---

# Customize colors and borders in your Streamlit app

Source: https://docs.streamlit.io/develop/concepts/configuration/theming-customize-colors-and-borders


## Color values

For all configuration options that accept a color, you can specify the value with one of the following strings:

- A CSS [`<named-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color) like `"darkBlue"` or `"maroon"`.
- A HEX string like `"#483d8b"` or `"#6A5ACD"`.
- An RGB string like `"rgb(106, 90, 205)"` or `"RGB(70, 130, 180)"`.
- An HSL string like `"hsl(248, 53%, 58%)"` or `"HSL(147, 50%, 47%)"`.

<Tip>

Although you can specify an alpha value for your colors, this isn't necessary for most options. Streamlit adjusts the alpha value of colors to ensure contextually appropriate shading between background and foreground.

</Tip>

## Default Streamlit colors

Streamlit comes with two preconfigured themes: light and dark. If you don't specify any theme configuration options, Streamlit will attempt to use the preconfigured theme that best matches each user's browser settings. These themes feature a red primary color in addition to a basic color palette (red, orange, yellow, green, blue, violet, and gray/grey) for elements like colored Markdown text.

## Color and border configuration options

Most theme configuration options can be set for your whole app, but you can override some with a different value for the sidebar. For example, your app's primary color (`primaryColor`) is used to highlight interactive elements and show focus. If you set `theme.primaryColor`, this will change the primary color for your whole app. However, if you set `theme.sidebar.primaryColor`, this will override `theme.primaryColor` in the sidebar, allowing you to use two different primary colors.

The following two configuration options can only be applied to the whole app:

- `theme.base` sets the default colors for your app's theme to match one of Streamlit's two default themes (`"light"` or `"dark"`). If any theme configuation option is used and `theme.base` is not set, then Streamlit will use `"light"`.
- `theme.showSidebarBorder` sets the visibility of the border between the sidebar and the main body of your app.
- `theme.chartCategoricalColors` and `theme.chartSequentialColors` set the series colors for Plotly, Altair, and Vega-Lite charts.

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `theme.primaryColor`
- `theme.backgroundColor`
- `theme.secondaryBackgroundColor`
- `theme.textColor`
- `theme.linkColor`
- `theme.linkUnderline`
- `theme.codeTextColor`
- `theme.codeBackgroundColor`
- `theme.baseRadius`
- `theme.buttonRadius`
- `theme.borderColor`
- `theme.dataframeBorderColor`
- `theme.dataframeHeaderBackgroundColor`
- `theme.showWidgetBorder`
- All color palette options

For brevity, on the rest of this page, theming configuration options will not include the `theme.` or `theme.sidebar.` prefix.

### Basic color palette

Various elements in Streamlit use or let you choose from a predefined palette of colors: red, orange, yellow, green, blue, violet, and gray/grey. These are some of the elements that use this basic color palette:

- Markdown text and background color (including `st.badge`).
- `st.metric` sparklines and deltas.
- Dataframe chart columns.
- Chat message avatars.
- Alert elements like `st.success` and `st.warning`.

For each color in the palette, you can define a base color, background color, and text color. If you only define a base color, Streamlit adjusts lightness/darkness and opacity to automatically provide a corresponding background and text color. However, you can manually define each of them, too. These are the color palette options:

- `redColor`, `redBackgroundColor`, `redTextColor`
- `orangeColor`, `orangeBackgroundColor`, `orangeTextColor`
- `yellowColor`, `yellowBackgroundColor`, `yellowTextColor`
- `greenColor`, `greenBackgroundColor`, `greenTextColor`
- `blueColor`, `blueBackgroundColor`, `blueTextColor`
- `violetColor`, `violetBackgroundColor`, `violetTextColor`
- `grayColor`, `grayBackgroundColor`, `grayTextColor`

### `primaryColor`

`primaryColor` defines the accent color most often used throughout your Streamlit
app. The following features and effects use your primary color:

- Button hover effects
- Elements in focus
- Selected elements

<Tip>

When your primary color is used as a background, Streamlit changes the text color to white. For example, this happens for `type="primary"` buttons and for selected items in `st.multiselect`.

For legibility, always choose a primary color that is dark enough to contrast well with white text.

</Tip>

#### Example 1: Primary color

The following configuration example has a `"forestGreen"` primary color. In the sidebar, the configuration overrides the primary color to `"darkGoldenrod"`. If you click inside a widget to give it focus, Streamlit displays a primary-color border around the widget. Additionally, if you hover over the secondary and tertiary buttons, the hover color matches the primary color.

```toml
[theme]
base="dark"
primaryColor="forestGreen"

[theme.sidebar]
primaryColor="darkGoldrod"
```

<Cloud height="350px" name="doc-theming-color-primarycolor"/>

### `backgroundColor`, `secondaryBackgroundColor`, `codeBackgroundColor`, and `dataframeHeaderBackgroundColor`

- `backgroundColor` defines the background color of your app.
- `secondaryBackgroundColor` is used for contrast in the following places:
  - The background of input or selection regions for widgets
  - Headers within elements like `st.help` and `st.dataframe` (if `dataframeHeaderBackgroundColor` isn't set)
  - Code blocks and inline code (if `codeBackgroundColor` isn't set)
- `codeBackgroundColor` sets the background for code blocks and line code. If `codeBackgroundColor` is not set, Streamlit uses `secondaryBackgroundColor` instead.
- `dataframeHeaderBackgroundColor` sets the background for dataframe headers (including the cells used for row selection and addition, if present).

<Note>

If you do not define background colors for the sidebar, Streamlit will swap `backgroundColor` and `secondaryBackgroundColor` in the sidebar:

- If `theme.sidebar.backgroundColor` is not defined, Streamlit uses `theme.secondaryBackgroundColor`.
- If `theme.sidebar.secondaryBackgroundColor` is not defined, Streamlit uses `theme.backgroundColor`.

</Note>

#### Example 2: Background colors

The following configuration example has a `"white"` background, with a lavender-tinted `"ghostWhite"` sidebar background. The secondary color for the whole app is `"lavender"` and the code background color is `"powderBlue"`. The code background color is configured once in `[theme]` and inherited in the sidebar. However, because Streamlit swaps background colors when the sidebar inherits them, the secondary background color is set in both `[theme]` and `[theme.sidebar]`. To see the secondary color used for a hover effect, hover over a dataframe cell or open the multiselect drop-down menu.

```toml
[theme]
base="light"
backgroundColor="white"
secondaryBackgroundColor="lavender"
codeBackgroundColor="powderBlue"

[theme.sidebar]
backgroundColor="ghostWhite"
secondaryBackgroundColor="lavender"
```

<Cloud height="450px" name="doc-theming-color-backgroundcolor"/>

### `textColor`, `codeTextColor`, `linkColor`, and `linkUnderline`

You can configure the color of body, code, and link text.

`textColor` sets the default text color for all text in the app except language-highlighting in code blocks, inline code, and links.
`codeTextColor` sets the default text color for inline code, but doesn't affect code blocks.
`linkColor` sets the default font color for all Markdown links in the app. If `linkUnderline` is set to true (default), the link underline color matches `linkColor`.

The following elements are impacted by `textColor`:

- Markdown text, except links
- Text in code blocks that's not colored otherwise from language highlighting
- App-chrome and sidebar menu icons
- Widget labels, icons, option text, and placeholder text
- Dataframe and table text
- Non-Markdown links, like `st.page_link`, `st.link_button`, and the navigation menu

As noted previously, Streamlit changes the text color to white when text is displayed against your primary color.

#### Example 3: Text colors

The following configuration example has `"darkGoldenrod"` text and `"darkOrchid"` links on a `"dark"` base. Buttons (including `st.link_button`) use the `"darkGoldenrod"` text color. In the multiselect widget, the placeholder text, drop-down menu, and tooltip all have `"darkGoldenrod"` text. If you hover over the sidebar, the scrollbar and collapse icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;chevron_left</i></named-color>) are `"darkGoldenrod"`.

```toml
[theme]
base="dark"
textColor="darkGoldenrod"
linkColor="darkOrchid"
```

<Cloud height="400px" name="doc-theming-color-textcolor"/>

### `baseRadius` and `buttonRadius`

`baseRadius` defines the radius of borders and backgrounds for the following elements:

- Buttons and input areas on widgets
- Selected items, including items in `st.multiselect` and the navigation menu
- Code blocks and inline code
- Dataframes (exterior)
- Badges and Markdown-text backgrounds
- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- Tooltips, including tooltips within charts
- Status and exception message blocks
- Images, including `st.graphviz` and `st.pyplot`, which display as static images

`buttonRadius` overrides `baseRadius` for buttons and `st.segmented_control`.

A few elements are notably not fully affected by `baseRadius`. Interactive charts and videos, which have a more complex underlying HTML, will always have square corners. This includes `st.video`, `st.map`, and `st.pydeck_chart`. Conversely, `st.chat_input` and `st.audio_input` will always be fully rounded. Sub-elements like tooltips are still affected by `baseRadius`.

#### Example 4: Border radius

In the following configuration example, the main body of the app uses a `"full"` (1rem) base radius, and the sidebar uses `"none"` (0rem). To better highlight this difference, the example includes contrasting primary and background colors.

```toml
[theme]
base="light"
primaryColor="slateBlue"
backgroundColor="mintCream"
secondaryBackgroundColor="darkSeaGreen"
baseRadius="full"

[theme.sidebar]
backgroundColor="aliceBlue"
secondaryBackgroundColor="skyBlue"
baseRadius="none"
```

<Cloud height="500px" name="doc-theming-color-baseradius"/>

### `borderColor`, `dataframeBorderColor`, and `showWidgetBorder`

Streamlit does not display borders for unfocused widgets by default (except for buttons). When a user focuses on a widget, Streamlit displays a border around the input area in your `primaryColor`. When the user removes focus, Streamlit hides the border.

If you set `showWidgetBorder=true`, Streamlit will display widget borders when the widget is not in focus. For those widgets, the border color is set by `borderColor`. If `borderColor` is not set, Streamlit infers a color by adding transparency to your `textColor`.

The following elements have borders that you can modify:

- Containers with borders, including expanders, forms, dialogs, popovers, and toasts
- The sidebar, including the right edge and the boundary below the navigation menu
- Dataframes and tables
- `st.tabs` (bottom border)
- Buttons, including `st.button`, `st.pills`, and `st.segmented_control`
- Borders on input regions

`dataframeBorderColor` overrides `borderColor` for dataframes and tables.

#### Example 5: Border color and visibility

The following configuration example uses a `"mediumSlateBlue"` border color throughout the app. In the sidebar, widget borders are shown. In the main body of the app, widget borders are not shown, and there is no border around the multiselect, text, or chat input regions except when they are in focus. However, many other elements, like buttons and dataframes, have always-visible borders.

```toml
[theme]
base="dark"
borderColor="mediumSlateBlue"
showWidgetBorder=false

[theme.sidebar]
showWidgetBorder=true
```

<Cloud height="420px" name="doc-theming-color-bordercolor"/>

---

# Customize fonts in your Streamlit app

Source: https://docs.streamlit.io/develop/concepts/configuration/theming-customize-fonts


Streamlit lets you change and customize the fonts in your app. You can load font files from a public URL or host them with your app using [static file serving](/develop/concepts/configuration/serving-static-files).

## Default Streamlit fonts

Streamlit comes with [Source Sans](https://fonts.adobe.com/fonts/source-sans), [Source Serif](https://fonts.adobe.com/fonts/source-serif), and [Source Code](https://fonts.adobe.com/fonts/source-code-pro) fonts. These font files are included with the Streamlit library so clients don't download them from a third party. By default, Streamlit uses Source Sans for all text except inline code and code blocks, which use Source Code instead.

To use these default faults, you can set each of the following configuration options to `"sans-serif"` (Source Sans), `"serif"` (Source Serif), or `"monospace"` (Source Code) in `config.toml`:

```toml
[theme]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
[theme.sidebar]
font = "sans-serif"
headingFont = "sans-serif"
codeFont = "monospace"
```

You can set the base font weight and size in the `[theme]` table in `config.toml`. These can't be configured separately in the sidebar.

- `theme.baseFontSize` sets the root font size for your app.
- `theme.baseFontWeight` sets the root font weight for your app.

The following configuration options can be set separately for the sidebar by using the `[theme.sidebar]` table instead of the `[theme]` table in `config.toml`:

- `theme.font` sets the default font for all text in the app (except inline code and code blocks). This is `"sans-serif"` (Source Sans) by default.
- `theme.headingFont` sets the default font for all headings in the app. If this is not set, Streamlit uses `theme.font` instead.
- `theme.headingFontSizes` sets the font sizes for `<h1>`-`<h6>` headings.
- `theme.headingFontWeights` sets the font sizes for `<h1>`-`<h6>` headings.
- `theme.codeFont` sets the default font for all inline code and code blocks. This is `"monospace"` (Source Code) by default.
- `theme.codeFontSize` sets the size of code text in code blocks, `st.json`, and `st.help` (but not inline code).
- `theme.codeFontWeight` sets the weight of code text in code blocks, `st.json`, and `st.help` (but not inline code).

When fonts are not declared in `[theme.sidebar]`, Streamlit will inherit each option from `[theme]` before defaulting to less specific options. For example, if `theme.sidebar.headingFont` is not set, Streamlit uses (in order of precedence) `theme.headingFont`, `theme.sidebar.font`, or `theme.font` instead.

In the following `config.toml` example, Streamlit uses Source Serif in the main body of the app and Source Sans in the sidebar.

```toml
[theme]
font = "serif"
[theme.sidebar]
font = "sans-serif"
```

## Externally hosted fonts

If you use a font service like Google Fonts or Adobe Fonts, you can use those fonts directly by encoding their font family (name) and CSS URL into a single string of the form `{font_name}:{css_url}`. If your font family includes a space, use inner quotes on the font family. In the following `config.toml` example, Streamlit uses Nunito font for all text except code, which is Space Mono instead. Space Mono has inner quotes because it has a space.

```toml
[theme]
font = "Nunito:https://fonts.googleapis.com/css2?family=Nunito=swap"
codeFont = "'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono=swap"
```

<Important>

If you configure your app to include any third-party integrations, including externally hosted fonts, your app may transmit user data (for example, IP addresses) to external servers. As the app developer, you are solely responsible for notifying your users about these third-party integrations, providing access to relevant privacy policies, and ensuring compliance with all applicable data protection laws and regulations.

</Important>

## Hosting alternative fonts

If you have font files that you want to host with your app, you must declare the font in `config.toml` under `[[theme.fontFaces]]`. For multiple alternative fonts, declare multiple `[[theme.fontFaces]]` tables in your configuration file. You can self-host your font by using Streamlit static file serving, or you can point to a publicly hosted font file.

<Important>

Streamlit supports self-hosting for OTF, TTF, WOFF, and WOFF2 font file formats. Other font file formats must be hosted externally.

</Important>

Fonts are defined with the following attributes in their `[[theme.fontFaces]]` tables:

- `family`: This is the name of the font and is used to identify the font for use by other configuration options.
- `url`: This is the location of the font file. If you are self-hosting the font file with your app, the value will be similar to `"app/static/font_file.woff"`.
- `weight` (optional): This declares the weight of the font within the font file (e.g., `400`, `"200 800"`, or `"bold"`). For more information, see the [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-weight) CSS `@font-face` descriptor.
- `style` (optional): This declares the style of the font within the font file (e.g., `"normal"`, `"italic"`, or `"oblique"`). For more information, see the [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-style) CSS `@font-face` descriptor.
- `unicodeRange` (optional): This declares the specific range of characters within the font file (e.g. `"U+0025-00FF, U+4??"`) For more information, see the [`unicode-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range) CSS `@font-face descriptor.

<Note>

Font files can be static or variable. A static font file contains a single weight and style of font. If you use static font files, it is common to load multiple files to fully support the font across different weights (normal, bold) and styles (normal, italic). Variable font files parameterize one or more font attributes, which means a single font file can support multiple weights and styles.

</Note>

### Example 1: Define an alternative font with variable font files

The following example uses static file serving to host Google's [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) and [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono) fonts and configures the app to use them. Both of these fonts are defined with variable font files that include a parameterized weight. However, because font style is not parameterized, Noto Sans requires two files to define the normal and italic styles separately. Noto Sans Mono does not include a separate file for its italic style. Per [CSS rules](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style#italic), if no italic style is explicitly provided, it will be simulated by skewing the normal-style font.

A line-by-line explanation of this example is available in a [tutorial](/develop/tutorials/configuration-and-theming/variable-fonts).

`.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
style="italic"
[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
style="normal"
[[theme.fontFaces]]
family="noto-mono"
url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"

[theme]
font="noto-sans"
codeFont="noto-mono"
```

Directory structure:

```none
project_directory/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│   ├── NotoSans-VariableFont_wdth,wght.ttf
│   └── NotoSansMono-VariableFont_wdth,wght.ttf
└── streamlit_app.py
```

### Example 2: Define an alternative font with static font files

In this configuration example, an alternative font is declared with multiple static font files. To cover basic Markdown formatting, each font should have at least four static files to define the following weight-style pairs:

- normal normal
- normal bold
- italic normal
- italic bold

If your app uses a font without a matching weight-style definition, the user's browser will use the closest font that is available. The default weight for `<h2>`-`<h6>` headings is semibold (600). For completeness, include additional font files to cover the semibold weight and all the font weights in your app. The following example uses [Tuffy](https://fonts.google.com/specimen/Tuffy) font. The font has four static font files that cover the four weight-style pairs.

A line-by-line explanation of this example is available in a [tutorial](/develop/tutorials/configuration-and-theming/static-fonts).

`.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Regular.ttf"
style="normal"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Bold.ttf"
style="normal"
weight=700
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Italic.ttf"
style="italic"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-BoldItalic.ttf"
style="italic"
weight=700

[theme]
font="tuffy"
```

Directory structure:

```none
project_directory/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── Tuffy-Bold.ttf
│   ├── Tuffy-BoldItalic.ttf
│   ├── Tuffy-Italic.ttf
│   └── Tuffy-Regular.ttf
└── streamlit_app.py
```

## Font fallbacks

If you use complicated font that might not be compatible with all browsers, or if you are using externally hosted fonts, it's best practice to include font fallbacks.

### Example 3: Define an alternative font with fallbacks

In your configuration file, wherever you declare a default font, you can use a comma-separated list of fonts instead. The font (or comma-separated list of fonts) is passed to the CSS [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property.

You can always include one of Streamlit's default fonts as a final fallback. The following example uses [Nunito](https://fonts.google.com/specimen/Nunito) and [Space Mono](https://fonts.google.com/specimen/Space+Mono) fonts. The configuration file points to the Google-hosted font files and identifies Streamlit's built-in font as the backup.

A line-by-line explanation of this example is available in a [tutorial](/develop/tutorials/configuration-and-theming/external-fonts).

`.streamlit/config.toml`:

```toml
[theme]
font="Nunito:https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000, sans-serif"
codeFont="'Space Mono':https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700=swap, monospace"
```

<Tip>

If any of your font family names contain spaces and you are declaring a fallback sequence, use inner quotes around the names. For example, if you name the font `"Nunito Sans"`, use `font="'Nunito Sans', sans-serif"` instead.

</Tip>

## Font size

You can set the base font size for your app in pixels. You must specify the base font size as an integer. The following configuration is equivalent to the default base font size of 16 pixels:

```toml
[theme]
baseFontSize=16
```

Additionally, you can set the font size for code blocks. The font size can be declared in pixels or rem. The following configuration is equivalent to the default code font size of 0.875rem.

```toml
[theme]
codeFontSize="0.875rem"
```

<Note>

Inline code in Markdown is not impacted by `theme.codeFontSize`. Inline code is set at 0.75em.

</Note>

## Font colors

Font color options are described in [Customize colors and borders in your Streamlit app](/develop/concepts/configuration/theming-customize-colors-and-borders#textcolor-and-linkcolor).

## Design tips

When using alternative fonts in your Streamlit app, keep good design practices in mind. The legibility of a font is strongly influenced by its size, contrast with its background, and shape. Streamlit lets you declare a different font for your headers from the rest of your text. If you introduce a more elaborate font, limit it to your headers. Because `theme.font` and `theme.sidebar.font` are used to set the font in widget labels, tooltips, column headers, and dataframe cells, they should always be a highly readable font.

For inspiration, see [Fonts in Use](https://fontsinuse.com/).</h6></h2></h6></h1></h6></h1>

---

# Streamlit's native app testing framework

Source: https://docs.streamlit.io/develop/concepts/app-testing


Streamlit app testing enables developers to build and run automated tests. Bring your favorite test automation software and enjoy simple syntax to simulate user input and inspect rendered output.

The provided class, AppTest, simulates a running app and provides methods to set up, manipulate, and inspect the app contents via API instead of a browser UI. AppTest provides similar functionality to browser automation tools like Selenium or Playwright, but with less overhead to write and execute tests. Use our testing framework with a tool like [pytest](https://docs.pytest.org/) to execute or automate your tests. A typical pattern is to build a suite of tests for an app to ensure consistent functionality as the app evolves. The tests run locally and/or in a CI environment like GitHub Actions.

<InlineCalloutContainer>
<InlineCallout bold="Get started" color="indigo-70" href="/develop/concepts/app-testing/get-started" icon="science">introduces you to the app testing framework and how to execute tests using <code>pytest</code>. Learn how to initialize and run simulated apps, including how to retrieve, manipulate, and inspect app elements.</InlineCallout>
<InlineCallout bold="Beyond the basics" color="indigo-70" href="/develop/concepts/app-testing/beyond-the-basics" icon="password">explains how to work with secrets and Session State within app tests, including how to test multipage apps.</InlineCallout>
<InlineCallout bold="Automate your tests" color="indigo-70" href="/develop/concepts/app-testing/automate-tests" icon="play_circle">with Continuous Integration (CI) to validate app changes over time.</InlineCallout>
<InlineCallout bold="Example" color="indigo-70" href="/develop/concepts/app-testing/examples" icon="quiz">puts together the concepts explained above. Check out an app with multiple tests in place.</InlineCallout>
<InlineCallout bold="Cheat sheet" color="indigo-70" href="/develop/concepts/app-testing/cheat-sheet" icon="saved_search">is a compact reference summarizing the available syntax.</InlineCallout>
</InlineCalloutContainer>

---

# Get started with app testing

Source: https://docs.streamlit.io/develop/concepts/app-testing/get-started


This guide will cover a simple example of how tests are structured within a project and how to execute them with `pytest`. After seeing the big picture, keep reading to learn about the [Fundamentals of app testing](#fundamentals-of-app-testing):

- Initializing and running a simulated app
- Retrieving elements
- Manipulating widgets
- Inspecting the results

Streamlit's app testing framework is not tied to any particular testing tool, but we'll use `pytest` for our examples since it is one of the most common Python test frameworks. To try out the examples in this guide, be sure to install `pytest` into your Streamlit development environment before you begin:

```bash
pip install pytest
```

## A simple testing example with `pytest`

This section explains how a simple test is structured and executed with `pytest`. For a comprehensive introduction to `pytest`, check out Real Python's guide to [Effective Python testing with pytest](https://realpython.com/pytest-python-testing/).

### How `pytest` is structured

`pytest` uses a naming convention for files and functions to execute tests conveniently. Name your test scripts of the form `test_<name>.py` or `<name>_test.py`. For example, you can use `test_myapp.py` or `myapp_test.py`. Within your test scripts, each test is written as a function. Each function is named to begin or end with `test`. We will prefix all our test scripts and test functions with `test_` for our examples in this guide.

You can write as many tests (functions) within a single test script as you want. When calling `pytest` in a directory, all `test_<name>.py` files within it will be used for testing. This includes files within subdirectories. Each `test_<something>` function within those files will be executed as a test. You can place test files anywhere in your project directory, but it is common to collect tests into a designated `tests/` directory. For other ways to structure and execute tests, check out [How to invoke pytest](https://docs.pytest.org/how-to/usage.html) in the `pytest` docs.

### Example project with app testing

Consider the following project:

```none
myproject/
├── app.py
└── tests/
    └── test_app.py
```

Main app file:

```python
"""app.py"""
import streamlit as st

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10)
if st.button("Add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")
```

Testing file:

```python
"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"
```

Let's take a quick look at what's in this app and test before we run it. The main app file (`app.py`) contains four elements when rendered: `st.title`, `st.number_input`, `st.button`, and `st.markdown`. The test script (`test_app.py`) includes a single test (the function named `test_increment_and_add`). We'll cover test syntax in more detail in the latter half of this guide, but here's a brief explanation of what this test does:

1. Initialize the simulated app and execute the first script run.
   ```python
   at = AppTest.from_file("app.py").run()
   ```
2. Simulate a user clicking the plus icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;add</i></something>) to increment the number input (and the resulting script rerun).
   ```python
   at.number_input[0].increment().run()
   ```
3. Simulate a user clicking the "**Add**" button (and the resulting script rerun).
   ```python
   at.button[0].click().run()
   ```
4. Check if the correct message is displayed at the end.
   ```python
   assert at.markdown[0].value == "Beans counted: 1"
   ```

Assertions are the heart of tests. When the assertion is true, the test passes. When the assertion is false, the test fails. A test can have multiple assertions, but keeping tests tightly focused is good practice. When tests focus on a single behavior, it is easier to understand and respond to failure.

### Try out a simple test with `pytest`

1. Copy the files above into a new "myproject" directory.
2. Open a terminal and change directory to your project.
   ```bash
   cd myproject
   ```
3. Execute `pytest`:
   ```bash
   pytest
   ```

The test should execute successfully. Your terminal should show something like this:

![A successfully completed test using pytest](/images/app-testing-pytest-intro.png)

By executing `pytest` at the root of your project directory, all Python files with the test prefix (`test_<name>.py`) will be scanned for test functions. Within each test file, each function with the test prefix will be executed as a test. `pytest` then counts successes and itemizes failures. You can also direct `pytest` to only scan your testing directory. For example, from the root of your project directory, execute:

```bash
pytest tests/
```

### Handling file paths and imports with `pytest`

Imports and paths within a test script should be relative to the directory where `pytest` is called. That is why the test function uses the path `app.py` instead of `../app.py` even though the app file is one directory up from the test script. You'll usually call `pytest` from the directory containing your main app file. This is typically the root of your project directory.

Additionally, if `.streamlit/` is present in the directory where you call `pytest`, any `config.toml` and `secrets.toml` within it will be accessible to your simulated app. For example, your simulated app will have access to the `config.toml` and `secrets.toml` files in this common setup:

Project structure:

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

Initialization within `test_app.py`:

```python
# Path to app file is relative to myproject/
at = AppTest.from_file("app.py").run()
```

Command to execute tests:

```bash
cd myproject
pytest tests/
```

## Fundamentals of app testing

Now that you understand the basics of `pytest` let's dive into using Streamlit's app testing framework. Every test begins with initializing and running your simulated app. Additional commands are used to retrieve, manipulate, and inspect elements.

On the next page, we'll go [Beyond the basics](/develop/concepts/app-testing/beyond-the-basics) and cover more advanced scenarios like working with secrets, Session State, or multipage apps.

### How to initialize and run a simulated app

To test a Streamlit app, you must first initialize an instance of [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) with the code for one page of your app. There are three methods for initializing a simulated app. These are provided as class methods to `AppTest`. We will focus on `AppTest.from_file()` which allows you to provide a path to a page of your app. This is the most common scenario for building automated tests during app development. `AppTest.from_string()` and `AppTest.from_function()` may be helpful for some simple or experimental scenarios.

Let's continue with the [example from above](#example-project-with-app-testing).

Recall the testing file:

```python
"""test_app.py"""
from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    """A user increments the number input, then clicks Add"""
    at = AppTest.from_file("app.py").run()
    at.number_input[0].increment().run()
    at.button[0].click().run()
    assert at.markdown[0].value == "Beans counted: 1"
```

Look at the first line in the test function:

```python
at = AppTest.from_file("app.py").run()
```

This is doing two things and is equivalent to:

```python
# Initialize the app.
at = AppTest.from_file("app.py")
# Run the app.
at.run()
```

`AppTest.from_file()` returns an instance of `AppTest`, initialized with the contents of `app.py`. The `.run()` method is used to run the app for the first time. Looking at the test, notice that the `.run()` method manually executes each script run. A test must explicitly run the app each time. This applies to the app's first run and any rerun resulting from simulated user input.

### How to retrieve elements

The attributes of the `AppTest` class return sequences of elements. The elements are sorted according to display order in the rendered app. Specific elements can be retrieved by index. Additionally, widgets with keys can be retrieved by key.

#### Retrieve elements by index

Each attribute of `AppTest` returns a sequence of the associated element type. Specific elements can be retrieved by index. In the above example, `at.number_input` returns a sequence of all `st.number_input` elements in the app. Thus, `at.number_input[0]` is the first such element in the app. Similarly, `at.markdown` returns a collection of all `st.markdown` elements where `at.markdown[0]` is the first such element.

Check out the current list of supported elements in the "Attributes" section of the [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest) class or the [App testing cheat sheet](/develop/concepts/app-testing/cheat-sheet). You can also use the `.get()` method and pass the attribute's name. `at.get("number_input")` and `at.get("markdown")` are equivalent to `at.number_input` and `at.markdown`, respectively.

The returned sequence of elements is ordered by appearance on the page. If containers are used to insert elements in a different order, these sequences may not match the order within your code. Consider the following example where containers are used to switch the order of two buttons on the page:

```python
import streamlit as st

first = st.container()
second = st.container()

second.button("A")
first.button("B")
```

If the above app was tested, the first button (`at.button[0]`) would be labeled "B" and the second button (`at.button[1]`) would be labeled "A." As true assertions, these would be:

```python
assert at.button[0].label == "B"
assert at.button[1].label == "A"
```

#### Retrieve widgets by key

You can retrieve keyed widgets by their keys instead of their order on the page. The key of the widget is passed as either an arg or kwarg. For example, look at this app and the following (true) assertions:

```python
import streamlit as st

st.button("Next", key="submit")
st.button("Back", key="cancel")
```

```python
assert at.button(key="submit").label == "Next"
assert at.button("cancel").label == "Back"
```

#### Retrieve containers

You can also narrow down your sequences of elements by retrieving specific containers. Each retrieved container has the same attributes as `AppTest`. For example, `at.sidebar.checkbox` returns a sequence of all checkboxes in the sidebar. `at.main.selectbox` returns the sequence of all selectboxes in the main body of the app (not in the sidebar).

For `AppTest.columns` and `AppTest.tabs`, a sequence of containers is returned. So `at.columns[0].button` would be the sequence of all buttons in the first column appearing in the app.

### How to manipulate widgets

All widgets have a universal `.set_value()` method. Additionally, many widgets have specific methods for manipulating their value. The names of [Testing element classes](/develop/api-reference/app-testing/testing-element-classes) closely match the names of the `AppTest` attributes. For example, look at the return type of [`AppTest.button`](/develop/api-reference/app-testing/st.testing.v1.apptest#apptestbutton) to see the corresponding class of [`Button`](/develop/api-reference/app-testing/testing-element-classes#sttestingv1element_treebutton). Aside from setting the value of a button with `.set_value()`, you can also use `.click()`. Check out each testing element class for its specific methods.

### How to inspect elements

All elements, including widgets, have a universal `.value` property. This returns the contents of the element. For widgets, this is the same as the return value or value in Session State. For non-input elements, this will be the value of the primary contents argument. For example, `.value` returns the value of `body` for `st.markdown` or `st.error`. It returns the value of `data` for `st.dataframe` or `st.table`.

Additionally, you can check many other details for widgets like labels or disabled status. Many parameters are available for inspection, but not all. Use linting software to see what is currently supported. Here's an example:

```python
import streamlit as st

st.selectbox("A", [1,2,3], None, help="Pick a number", placeholder="Pick me")
```

```python
assert at.selectbox[0].value == None
assert at.selectbox[0].label == "A"
assert at.selectbox[0].options == ["1","2","3"]
assert at.selectbox[0].index == None
assert at.selectbox[0].help == "Pick a number"
assert at.selectbox[0].placeholder == "Pick me"
assert at.selectbox[0].disabled == False
```

<Tip>

Note that the `options` for `st.selectbox` were declared as integers but asserted as strings. As noted in the documentation for [`st.selectbox`](/develop/api-reference/widgets/st.selectbox), options are cast internally to strings. If you ever find yourself getting unexpected results, check the documentation carefully for any notes about recasting types internally.

</Tip></name></name></name></name>

---

# Beyond the basics of app testing

Source: https://docs.streamlit.io/develop/concepts/app-testing/beyond-the-basics


Now that you're comfortable with executing a basic test for a Streamlit app let's cover the mutable attributes of [`AppTest`](/develop/api-reference/app-testing/st.testing.v1.apptest):

- `AppTest.secrets`
- `AppTest.session_state`
- `AppTest.query_params`

You can read and update values using dict-like syntax for all three attributes. For `.secrets` and `.query_params`, you can use key notation but not attribute notation. For example, the `.secrets` attribute for `AppTest` accepts `at.secrets["my_key"]` but **_not_** `at.secrets.my_key`. This differs from how you can use the associated command in the main library. On the other hand, `.session_state` allows both key notation and attribute notation.

For these attributes, the typical pattern is to declare any values before executing the app's first run. Values can be inspected at any time in a test. There are a few extra considerations for secrets and Session State, which we'll cover now.

## Using secrets with app testing

Be careful not to include secrets directly in your tests. Consider this simple project with `pytest` executed in the project's root directory:

```none
myproject/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── app.py
└── tests/
    └── test_app.py
```

```bash
cd myproject
pytest tests/
```

In the above scenario, your simulated app will have access to your `secrets.toml` file. However, since you don't want to commit your secrets to your repository, you may need to write tests where you securely pull your secrets into memory or use dummy secrets.

### Example: declaring secrets in a test

Within a test, declare each secret after initializing your `AppTest` instance but before the first run. (A missing secret may result in an app that doesn't run!) For example, consider the following secrets file and corresponding test initialization to assign the same secrets manually:

Secrets file:

```toml
db_username = "Jane"
db_password = "mypassword"

[my_other_secrets]
things_i_like = ["Streamlit", "Python"]
```

Testing file with equivalent secrets:

```python
# Initialize an AppTest instance.
at = AppTest.from_file("app.py")
# Declare the secrets.
at.secrets["db_username"] = "Jane"
at.secrets["db_password"] = "mypassword"
at.secrets["my_other_secrets.things_i_like"] = ["Streamlit", "Python"]
# Run the app.
at.run()
```

Generally, you want to avoid typing your secrets directly into your test. If you don't need your real secrets for your test, you can declare dummy secrets as in the example above. If your app uses secrets to connect to an external service like a database or API, consider mocking that service in your app tests. If you need to use the real secrets and actually connect, you should use an API to pass them securely and anonymously. If you are automating your tests with GitHub actions, check out their [Security guide](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).

```python
at.secrets["my_key"] = <value>through API&gt;
```

## Working with Session State in app testing

The `.session_state` attribute for `AppTest` lets you read and update Session State values using key notation (`at.session_state["my_key"]`) and attribute notation (`at.session_state.my_key`). By manually declaring values in Session State, you can directly jump to a specific state instead of simulating many steps to get there. Additionally, the testing framework does not provide native support for multipage apps. An instance of `AppTest` can only test one page. You must manually declare Session State values to simulate a user carrying data from another page.

### Example: testing a multipage app

Consider a simple multipage app where the first page can modify a value in Session State. To test the second page, set Session State manually and run the simulated app within the test:

Project structure:

```none
myproject/
├── pages/
│   └── second.py
├── first.py
└── tests/
    └── test_second.py
```

First app page:

```python
"""first.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

new_word = st.text_input("Magic word:")

if st.button("Set the magic word"):
    st.session_state.magic_word = new_word
```

Second app page:

```python
"""second.py"""
import streamlit as st

st.session_state.magic_word = st.session_state.get("magic_word", "Streamlit")

if st.session_state.magic_word == "Balloons":
    st.markdown(":balloon:")
```

Testing file:

```python
"""test_second.py"""
from streamlit.testing.v1 import AppTest

def test_balloons():
    at = AppTest.from_file("pages/second.py")
    at.session_state["magic_word"] = "Balloons"
    at.run()
    assert at.markdown[0].value == ":balloon:"
```

By setting the value `at.session_state["magic_word"] = "Balloons"` within the test, you can simulate a user navigating to `second.py` after entering and saving "Balloons" on `first.py`.</value>

---

# Automate your tests with CI

Source: https://docs.streamlit.io/develop/concepts/app-testing/automate-tests


One of the key benefits of app testing is that tests can be automated using Continuous Integration (CI). By running tests automatically during development, you can validate that changes to your app don't break existing functionality. You can verify app code as you commit, catch bugs early, and prevent accidental breaks before deployment.

There are many popular CI tools, including GitHub Actions, Jenkins, GitLab CI, Azure DevOps, and Circle CI. Streamlit app testing will integrate easily with any of them similar to any other Python tests.

## GitHub Actions

Since many Streamlit apps (and all Community Cloud apps) are built in GitHub, this page uses examples from [GitHub Actions](https://docs.github.com/en/actions). For more information about GitHub Actions, see:

- [Quickstart for GitHub Actions](https://docs.github.com/en/actions/quickstart)
- [GitHub Actions: About continuous integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
- [GitHub Actions: Build  test Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## Streamlit App Action

[Streamlit App Action](https://github.com/marketplace/actions/streamlit-app-action) provides an easy way to add automated testing to your app repository in GitHub. It also includes basic smoke testing for each page of your app without you writing any test code.

To install Streamlit App Action, add a workflow `.yml` file to your repository's `.github/workflows/` folder. For example:

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit app

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: streamlit_app.py
```

Let's take a look in more detail at what this action workflow is doing.

### Triggering the workflow

```yaml
on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]
```

This workflow will be triggered and execute tests on pull requests targeting the `main` branch, as well as any new commits pushed to the `main` branch. Note that it will also execute the tests on subsequent commits to any open pull requests. See [GitHub Actions: Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow) for more information and examples.

### Setting up the test environment

```yaml
jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
```

The workflow has a `streamlit` job that executes a series of steps. The job runs on a Docker container with the `ubuntu-latest` image.

- `actions/checkout@v4` checks out the current repository code from GitHub and copies the code to the job environment.
- `actions/setup-python@v5` installs Python version 3.11.

### Running the app tests

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
```

Streamlit App Action does the following:

- Install `pytest` and install any dependencies specified in `requirements.txt`.
- Run the built-in app smoke tests.
- Run any other Python tests found in the repository.

<Tip>

If your app doesn't include `requirements.txt` in the repository root directory, you will need to add a step to install dependencies with your chosen package manager before running Streamlit App Action.

</Tip>

The built-in smoke tests have the following behavior:

- Run the app specified at `app-path` as an AppTest.
- Validate that it completes successfully and does not result in an uncaught exception.
- Do the same for any additional `pages/` of the app relative to `app-path`.

If you want to run Streamlit App Action without the smoke tests, you can set `skip-smoke: true`.

### Linting your app code

Linting is the automated checking of source code for programmatic and stylistic errors. This is done by using a lint tool (otherwise known as a linter). Linting is important to reduce errors and improve the overall quality of your code, especially for repositories with multiple developers or public repositories.

You can add automated linting with [Ruff](https://docs.astral.sh/ruff/) by passing `ruff: true` to Streamlit App Action.

```yaml
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    ruff: true
```

<Tip>

You may want to add a pre-commit hook like [ruff-pre-commit](https://github.com/astral-sh/ruff-pre-commit) in your local development environment to fix linting errors before they get to CI.

</Tip>

### Viewing results

If tests fail, the CI workflow will fail and you will see the results in GitHub. Console logs are available by clicking into the workflow run [as described here](https://docs.github.com/en/actions/using-workflows/about-workflows#viewing-the-activity-for-a-workflow-run).

![](/images/test-results-logs.png)

For higher-level test results, you can use [pytest-results-action](https://github.com/marketplace/actions/pytest-results-actions). You can combine this with Streamlit App Action as follows:

```yaml
# ... setup as above ...
- uses: streamlit/streamlit-app-action@v0.0.3
  with:
    app-path: streamlit_app.py
    # Add pytest-args to output junit xml
    pytest-args: -v --junit-xml=test-results.xml
- if: always()
  uses: pmeier/pytest-results-action@v0.6.0
  with:
    path: test-results.xml
    summary: true
    display-options: fEX
```

![](/images/test-results-summary.png)

## Writing your own actions

The above is just provided as an example. Streamlit App Action is a quick way to get started. Once you learn the basics of your CI tool of choice, it's easy to build and customize your own automated workflows. This is a great way to improve your overall productivity as a developer and the quality of your apps.

## Working example

As a final working example example, take a look at our [`streamlit/llm-examples` Actions](https://github.com/streamlit/llm-examples/actions), defined in [this workflow file](https://github.com/streamlit/llm-examples/blob/main/.github/workflows/app-testing.yml).

---

# App testing example

Source: https://docs.streamlit.io/develop/concepts/app-testing/examples


## Testing a login page

Let's consider a login page. In this example, `secrets.toml` is not present. We'll manually declare dummy secrets directly in the tests. To avoid [timing attacks](https://en.wikipedia.org/wiki/Timing_attack), the login script uses `hmac` to compare a user's password to the secret value as a security best practice.

### Project summary

#### Login page behavior

Before diving into the app's code, let's think about what this page is supposed to do. Whether you use test-driven development or you write unit tests after your code, it's a good idea to think about the functionality that needs to be tested. The login page should behave as follows:

- Before a user interacts with the app:
  - Their status is "unverified."
  - A password prompt is displayed.
- If a user types an incorrect password:
  - Their status is "incorrect."
  - An error message is displayed.
  - The password attempt is cleared from the input.
- If a user types a correct password:
  - Their status is "verified."
  - A confirmation message is displayed.
  - A logout button is displayed (without a login prompt).
- If a logged-in user clicks the **Log out** button:
  - Their status is "unverified."
  - A password prompt is displayed.

#### Login page project structure

```none
myproject/
├── app.py
└── tests/
    └── test_app.py
```

#### Login page Python file

The user's status mentioned in the page's specifications are encoded in `st.session_state.status`. This value is initialized at the beginning of the script as "unverified" and is updated through a callback when the password prompt receives a new entry.

```python
"""app.py"""
import streamlit as st
import hmac

st.session_state.status = st.session_state.get("status", "unverified")
st.title("My login page")


def check_password():
    if hmac.compare_digest(st.session_state.password, st.secrets.password):
        st.session_state.status = "verified"
    else:
        st.session_state.status = "incorrect"
    st.session_state.password = ""

def login_prompt():
    st.text_input("Enter password:", key="password", on_change=check_password)
    if st.session_state.status == "incorrect":
        st.warning("Incorrect password. Please try again.")

def logout():
    st.session_state.status = "unverified"

def welcome():
    st.success("Login successful.")
    st.button("Log out", on_click=logout)


if st.session_state.status != "verified":
    login_prompt()
    st.stop()
welcome()
```

#### Login page test file

These tests closely follow the app's specifications above. In each test, a dummy secret is set before running the app and proceeding with further simulations and checks.

```python
from streamlit.testing.v1 import AppTest

def test_no_interaction():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""

def test_incorrect_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("balloon").run()
    assert at.session_state["status"] == "incorrect"
    assert len(at.text_input) == 1
    assert len(at.warning) == 1
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
    assert "Incorrect password" in at.warning[0].value

def test_correct_password():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.run()
    at.text_input[0].input("streamlit").run()
    assert at.session_state["status"] == "verified"
    assert len(at.text_input) == 0
    assert len(at.warning) == 0
    assert len(at.success) == 1
    assert len(at.button) == 1
    assert "Login successful" in at.success[0].value
    assert at.button[0].label == "Log out"

def test_log_out():
    at = AppTest.from_file("app.py")
    at.secrets["password"] = "streamlit"
    at.session_state["status"] = "verified"
    at.run()
    at.button[0].click().run()
    assert at.session_state["status"] == "unverified"
    assert len(at.text_input) == 1
    assert len(at.warning) == 0
    assert len(at.success) == 0
    assert len(at.button) == 0
    assert at.text_input[0].value == ""
```

See how Session State was modified in the last test? Instead of fully simulating a user logging in, the test jumps straight to a logged-in state by setting `at.session_state["status"] = "verified"`. After running the app, the test proceeds to simulate the user logging out.

### Automating your tests

If `myproject/` was pushed to GitHub as a repository, you could add GitHub Actions test automation with [Streamlit App Action](https://github.com/marketplace/actions/streamlit-app-action). This is as simple as adding a workflow file at `myproject/.github/workflows/`:

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit app

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: app.py
```

---

# App testing cheat sheet

Source: https://docs.streamlit.io/develop/concepts/app-testing/cheat-sheet


## Text elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# Headers
assert "My app" in at.title[0].value
assert "New topic" in at.header[0].value
assert "Interesting sub-topic" in at.subheader[0].value
assert len(at.divider) == 2

# Body / code
assert "Hello, world!" in at.markdown[0].value
assert "import streamlit as st" in at.code[0].value
assert "A cool diagram" in at.caption[0].value
assert "Hello again, world!" in at.text[0].value
assert "\int a x^2 \,dx" in at.latex[0].value
```

## Input widgets

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# button
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# checkbox
assert at.checkbox[0].value == False
at.checkbox[0].check().run() # uncheck() is also supported
assert at.checkbox[0].value == True

# color_picker
assert at.color_picker[0].value == "#FFFFFF"
at.color_picker[0].pick("#000000").run()

# date_input
assert at.date_input[0].value == datetime.date(2019, 7, 6)
at.date_input[0].set_value(datetime.date(2022, 12, 21)).run()

# form_submit_button - shows up just like a button
assert at.button[0].value == False
at.button[0].click().run()
assert at.button[0].value == True

# multiselect
assert at.multiselect[0].value == ["foo", "bar"]
at.multiselect[0].select("baz").unselect("foo").run()

# number_input
assert at.number_input[0].value == 5
at.number_input[0].increment().run()

# radio
assert at.radio[0].value == "Bar"
assert at.radio[0].index == 3
at.radio[0].set_value("Foo").run()

# selectbox
assert at.selectbox[0].value == "Bar"
assert at.selectbox[0].index == 3
at.selectbox[0].set_value("Foo").run()

# select_slider
assert at.select_slider[0].value == "Feb"
at.select_slider[0].set_value("Mar").run()
at.select_slider[0].set_range("Apr", "Jun").run()

# slider
assert at.slider[0].value == 2
at.slider[0].set_value(3).run()
at.slider[0].set_range(4, 6).run()

# text_area
assert at.text_area[0].value == "Hello, world!"
at.text_area[0].set_value("Hello, yourself!").run()

# text_input
assert at.text_input[0].value == "Hello, world!")
at.text_input[0].set_value("Hello, yourself!").run()

# time_input
assert at.time_input[0].value == datetime.time(8, 45)
at.time_input[0].set_value(datetime.time(12, 30))

# toggle
assert at.toggle[0].value == False
assert at.toggle[0].label == "Debug mode"
at.toggle[0].set_value(True).run()
assert at.toggle[0].value == True
```

## Data elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# dataframe
expected_df = pd.DataFrame([1, 2, 3])
assert at.dataframe[0].value.equals(expected_df)

# metric
assert at.metric[0].value == "9500"
assert at.metric[0].delta == "1000"

# json
assert at.json[0].value == '["hi", {"foo": "bar"}]'

# table
table_df = pd.DataFrame([1, 2, 3])
assert at.table[0].value.equals(table_df)
```

## Layouts and containers

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# sidebar
at.sidebar.text_input[0].set_value("Jane Doe")

# columns
at.columns[1].markdown[0].value == "Hello, world!"

# tabs
at.tabs[2].markdown[0].value == "Hello, yourself!"
```

## Chat elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# chat_input
at.chat_input[0].set_value("Do you know any jokes?").run()
# Note: chat_input value clears after every re-run (like in a real app)

# chat_message
assert at.chat_message[0].markdown[0].value == "Do you know any jokes?"
assert at.chat_message[0].avatar == "user"
```

## Status elements

```python
from streamlit.testing.v1 import AppTest

at = AppTest.from_file("cheatsheet_app.py")

# exception
assert len(at.exception) == 1
assert "TypeError" in at.exception[0].value

# Other in-line alerts: success, info, warning, error
assert at.success[0].value == "Great job!"
assert at.info[0].value == "Please enter an API key to continue"
assert at.warning[0].value == "Sorry, the passwords didn't match"
assert at.error[0].value == "Something went wrong :("

# toast
assert at.toast[0].value == "That was lit!" and at.toast[0].icon == "🔥"
```

## Limitations

As of Streamlit 1.28, the following Streamlit features are not natively supported by `AppTest`. However, workarounds are possible for many of them by inspecting the underlying proto directly using `AppTest.get()`. We plan to regularly add support for missing elements until all features are supported.

- Chart elements (`st.bar_chart`, `st.line_chart`, etc)
- Media elements (`st.image`, `st.video`, `st.audio`)
- `st.file_uploader`
- `st.data_editor`
- `st.expander`
- `st.status`
- `st.camera_input`
- `st.download_button`
- `st.link_button`

---

# API reference

Source: https://docs.streamlit.io/develop/api-reference


Streamlit makes it easy for you to visualize, mutate, and share data. The API
reference is organized by activity type, like displaying data or optimizing
performance. Each section includes methods associated with the activity type,
including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

## Display almost anything

### Write and magic

<br/>
<TileContainer>
<RefCard href="/develop/api-reference/write-magic/st.write">
<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">
<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">
<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

### Text elements

<br/>
<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">
<Image>alt="screenshot" src="/images/api/markdown.jpg" /&gt;

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.title">
<Image>alt="screenshot" src="/images/api/title.jpg" /&gt;

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.header">
<Image>alt="screenshot" src="/images/api/header.jpg" /&gt;

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">
<Image>alt="screenshot" src="/images/api/subheader.jpg" /&gt;

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.badge">
<Image>alt="screenshot" src="/images/api/badge.jpg" /&gt;

<h4>Badge</h4>

Display a small, colored badge.

```python
st.badge("New")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.caption">
<Image>alt="screenshot" src="/images/api/caption.jpg" /&gt;

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.code">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.echo">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Echo</h4>

Display some code in the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.latex">
<Image>alt="screenshot" src="/images/api/latex.jpg" /&gt;

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.text">
<Image>alt="screenshot" src="/images/api/text.jpg" /&gt;

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.divider">
<Image>alt="screenshot" src="/images/api/divider.jpg" /&gt;

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.help">
<h4>Get help</h4>

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.html">
<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```

</RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">
<Image>alt="screenshot" src="/images/api/components/annotated-text.jpg" /&gt;

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">
<Image>alt="screenshot" src="/images/api/components/drawable-canvas.jpg" /&gt;

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/gagan3012/streamlit-tags">
<Image>alt="screenshot" src="/images/api/components/tags.jpg" /&gt;

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/JohnSnowLabs/nlu">
<Image>alt="screenshot" src="/images/api/components/nlu.jpg" /&gt;

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load("sentiment").predict("I love NLU! </Image></ComponentCard></ComponentSlider>

---

# st.write and magic commands

Source: https://docs.streamlit.io/develop/api-reference/write-magic


Streamlit has two easy ways to display information into your app, which should typically be the
first thing you try: `st.write` and magic.

<TileContainer>
<RefCard href="/develop/api-reference/write-magic/st.write">
<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">
<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">
<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/write-magic/st.write


* Function signature:

   st.write(*args, unsafe_allow_html=False)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | *args | any |  | One or many objects to display in the app.  Each type of argument is handled as follows:      Type Handling    str Uses st.markdown().  dataframe-like, dict, or list Uses st.dataframe().  Exception Uses st.exception().  function, module, or class Uses st.help().  DeltaGenerator Uses st.help().  Altair chart Uses st.altair_chart().  Bokeh figure Uses st.bokeh_chart().  Graphviz graph Uses st.graphviz_chart().  Keras model Converts model and uses st.graphviz_chart().  Matplotlib figure Uses st.pyplot().  Plotly figure Uses st.plotly_chart().  PIL.Image Uses st.image().  generator or stream (like openai.Stream) Uses st.write_stream().  SymPy expression Uses st.latex().  An object with ._repr_html() Uses st.html().  Database cursor Displays DB API 2.0 cursor results in a table.  Any Displays str(arg) as inline code. |
   | unsafe_allow_html | bool |  | Whether to render HTML within *args. This only applies to strings or objects falling back on _repr_html_(). If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered. Adding custom HTML to your app impacts safety, styling, and maintainability.  Note If you only want to insert HTML or CSS without Markdown text, we recommend using st.html instead. |

* Returns: None



### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

<YouTube videoId="wpDuY9I2fDg"/>

---

Source: https://docs.streamlit.io/develop/api-reference/write-magic/st.write_stream


* Function signature:

   st.write_stream(stream, *, cursor=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | stream | Callable, Generator, Iterable, OpenAI Stream, or LangChain Stream |  | The generator or iterable to stream. If you pass an async generator, Streamlit will internally convert it to a sync generator. If the generator depends on a cached object with async references, this can raise an error.  Note To use additional LLM libraries, you can create a wrapper to manually define a generator function and include custom output parsing. |
   | cursor | str or None |  | A string to append to text as it's being written. If this is None (default), no cursor is shown. Otherwise, the string is rendered as Markdown and appears as a cursor at the end of the streamed text. For example, you can use an emoji, emoji shortcode, or Material icon. The first line of the cursor string can contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. If you pass a multiline string, additional lines display after the text with the full Markdown rendering capabilities of st.markdown. See the body parameter of st.markdown for additional, supported Markdown directives. |

* Returns: str or list

    The full response. If the streamed output only contains text, this
is a string. Otherwise, this is a list of all the streamed objects.
The return value is fully compatible as input for st.write.


<Tip>

If your stream object is not compatible with `st.write_stream`, define a wrapper around your stream object to create a compatible generator function.

```python
for chunk in unsupported_stream:
    yield preprocess(chunk)
```

For an example, see how we use [Replicate](https://replicate.com/docs/get-started/python) with [Snowflake Arctic](https://www.snowflake.com/en/data-cloud/arctic/) in [this code](https://github.com/streamlit/snowflake-arctic-st-demo/blob/0f0d8b49f328f72ae58ced2e9000790fb5e56e6f/simple_app.py#L58).

</Tip>

---

Source: https://docs.streamlit.io/develop/api-reference/write-magic/magic

## Magic

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data,
charts) without having to type an explicit command at all. Just put the thing you want to show on
its own line of code, and it will appear in your app. Here's an example:

```python
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
```

### How Magic works

Any time Streamlit sees either a variable or literal
value on its own line, it automatically writes that to your app using
[`st.write`](/develop/api-reference/write-magic/st.write) (which you'll learn about later).

Also, magic is smart enough to ignore docstrings. That is, it ignores the
strings at the top of files and functions.

If you prefer to call Streamlit commands more explicitly, you can always turn
magic off in your `~/.streamlit/config.toml` with the following setting:

```toml
[runner]
magicEnabled = false
```

<Important>
<p>Right now, Magic only works in the main Python app file, not in imported files. See GitHub issue #288 for a discussion of the issues.</p>
</Important>

### Featured video

Learn what the [`st.write`](/develop/api-reference/write-magic/st.write) and [magic](/develop/api-reference/write-magic/magic) commands are and how to use them.

<YouTube videoId="wpDuY9I2fDg"/>

---

# Text elements

Source: https://docs.streamlit.io/develop/api-reference/text


Streamlit apps usually start with a call to `st.title` to set the
app's title. After that, there are 2 heading levels you can use:
`st.header` and `st.subheader`.

Pure text is entered with `st.text`, and Markdown with
`st.markdown`.

We also offer a "swiss-army knife" command called `st.write`, which accepts
multiple arguments, and multiple data types. And as described above, you can
also use [magic commands](/develop/api-reference/write-magic/magic) in place of `st.write`.

## Headings and body text

<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">
<Image>alt="screenshot" src="/images/api/markdown.jpg" /&gt;

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.title">
<Image>alt="screenshot" src="/images/api/title.jpg" /&gt;

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.header">
<Image>alt="screenshot" src="/images/api/header.jpg" /&gt;

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">
<Image>alt="screenshot" src="/images/api/subheader.jpg" /&gt;

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```

</Image></RefCard>
</TileContainer>

## Formatted text

<TileContainer>
<RefCard href="/develop/api-reference/text/st.badge">
<Image>alt="screenshot" src="/images/api/badge.jpg" /&gt;

<h4>Badge</h4>

Display a small, colored badge.

```python
st.badge("New")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.caption">
<Image>alt="screenshot" src="/images/api/caption.jpg" /&gt;

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.code">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.echo">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Echo</h4>

Display some code on the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.text">
<Image>alt="screenshot" src="/images/api/text.jpg" /&gt;

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.latex">
<Image>alt="screenshot" src="/images/api/latex.jpg" /&gt;

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.divider">
<Image>alt="screenshot" src="/images/api/divider.jpg" /&gt;

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```

</Image></RefCard>
</TileContainer>

## Utilities

<TileContainer>
<RefCard href="/develop/api-reference/text/st.help" size="half">
<h4>Get help</h4>

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```

</RefCard>
<RefCard href="/develop/api-reference/text/st.html" size="half">
<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```

</RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">
<Image>alt="screenshot" src="/images/api/components/annotated-text.jpg" /&gt;

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">
<Image>alt="screenshot" src="/images/api/components/drawable-canvas.jpg" /&gt;

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/gagan3012/streamlit-tags">
<Image>alt="screenshot" src="/images/api/components/tags.jpg" /&gt;

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/JohnSnowLabs/nlu">
<Image>alt="screenshot" src="/images/api/components/nlu.jpg" /&gt;

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load('sentiment').predict('I love NLU! </Image></ComponentCard></ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.title


* Function signature:

   st.title(body, anchor=None, *, help=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | anchor | str or False |  | The anchor name of the header that can be accessed with #anchor in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI. |
   | help | str or None |  | A tooltip that gets displayed next to the title. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | width | "stretch", "content", or int |  | The width of the title element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.header


* Function signature:

   st.header(body, anchor=None, *, help=None, divider=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | anchor | str or False |  | The anchor name of the header that can be accessed with #anchor in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI. |
   | help | str or None |  | A tooltip that gets displayed next to the header. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | divider | bool, "blue", "green", "orange", "red", "violet", "yellow", "gray"/"grey", or "rainbow" |  | Shows a colored divider below the header. If this is True, successive headers will cycle through divider colors, except gray and rainbow. That is, the first header will have a blue line, the second header will have a green line, and so on. If this is a string, the color can be set to one of the following: blue, green, orange, red, violet, yellow, gray/grey, or rainbow. |
   | width | "stretch", "content", or int |  | The width of the header element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.subheader


* Function signature:

   st.subheader(body, anchor=None, *, help=None, divider=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | anchor | str or False |  | The anchor name of the header that can be accessed with #anchor in the URL. If omitted, it generates an anchor using the body. If False, the anchor is not shown in the UI. |
   | help | str or None |  | A tooltip that gets displayed next to the subheader. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | divider | bool, "blue", "green", "orange", "red", "violet", "yellow", "gray"/"grey", or "rainbow" |  | Shows a colored divider below the header. If this is True, successive headers will cycle through divider colors, except gray and rainbow. That is, the first header will have a blue line, the second header will have a green line, and so on. If this is a string, the color can be set to one of the following: blue, green, orange, red, violet, yellow, gray/grey, or rainbow. |
   | width | "stretch", "content", or int |  | The width of the subheader element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.markdown


* Function signature:

   st.markdown(body, unsafe_allow_html=False, *, help=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | any | primary | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. If anything other than a string is passed, it will be converted into a string behind the scenes using str(body). This also supports:  Emoji shortcodes, such as :+1:  and :sunglasses:. For a list of all supported codes, see https://share.streamlit.io/streamlit/emoji-shortcodes. Streamlit logo shortcode. Use :streamlit: to add a little Streamlit flair to your text. A limited set of typographical symbols. "-&gt;  -- &gt;=  becomes "← → ↔ — ≥ ≤ ≈" when parsed as Markdown. Google Material Symbols (rounded style), using the syntax :material/icon_name:, where "icon_name" is the name of the icon in snake case. For a complete list of icons, see Google's Material Symbols font library. LaTeX expressions, by wrapping them in "$" or "$$" (the "$$" must be on their own lines). Supported LaTeX functions are listed at https://katex.org/docs/supported.html. Colored text and background colors for text, using the syntax :color[text to be colored] and :color-background[text to be colored], respectively. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, rainbow, or primary. For example, you can use :orange[your text here] or :blue-background[your text here]. If you use "primary" for color, Streamlit will use the default primary accent color unless you set the theme.primaryColor configuration option. Colored badges, using the syntax :color-badge[text in the badge]. color must be replaced with any of the following supported colors: red, orange, yellow, green, blue, violet, gray/grey, or primary. For example, you can use :orange-badge[your text here] or :blue-badge[your text here]. Small text, using the syntax :small[text to show small]. |
   | unsafe_allow_html | bool |  | Whether to render HTML within body. If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered. Adding custom HTML to your app impacts safety, styling, and maintainability.  Note If you only want to insert HTML or CSS without Markdown text, we recommend using st.html instead. |
   | help | str or None |  | A tooltip that gets displayed next to the Markdown. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | width | "stretch", "content", or int |  | The width of the Markdown element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



```python
import streamlit as st

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)
```

<Cloud height="500px" name="doc-markdown1"/>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.badge


* Function signature:

   st.badge(label, *, icon=None, color="blue", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | The label to display in the badge. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code. See the body parameter of st.markdown for additional, supported Markdown directives. Because this command escapes square brackets ([ ]) in this parameter, any directive requiring square brackets is not supported. |
   | icon | str or None |  | An optional emoji or icon to display next to the badge label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | color | str | s | The color to use for the badge. This defaults to "blue". This can be one of the following supported colors: red, orange, yellow, blue, green, violet, gray/grey, or primary. If you use "primary", Streamlit will use the default primary accent color unless you set the theme.primaryColor configuration option. |
   | width | "content", "stretch", or int |  | The width of the badge element. This can be one of the following:  "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.caption


* Function signature:

   st.caption(body, unsafe_allow_html=False, *, help=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | unsafe_allow_html | bool |  | Whether to render HTML within body. If this is False (default), any HTML tags found in body will be escaped and therefore treated as raw text. If this is True, any HTML expressions within body will be rendered. Adding custom HTML to your app impacts safety, styling, and maintainability.  Note If you only want to insert HTML or CSS without Markdown text, we recommend using st.html instead. |
   | help | str or None |  | A tooltip that gets displayed next to the caption. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | width | "stretch", "content", or int |  | The width of the caption element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |


<Image src="/images/api/st.caption.png"/>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.code


* Function signature:

   st.code(body, language="python", *, line_numbers=False, wrap_lines=False, height="content", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The string to display as code or monospace text. |
   | language | str or None | s | The language that the code is written in, for syntax highlighting. This defaults to "python". If this is None, the code will be plain, monospace text. For a list of available language values, see react-syntax-highlighter on GitHub. |
   | line_numbers | bool | s | An optional boolean indicating whether to show line numbers to the left of the code block. This defaults to False. |
   | wrap_lines | bool | s | An optional boolean indicating whether to wrap lines. This defaults to False. |
   | height | "content", "stretch", or int |  | The height of the code block element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled.   Note Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. |
   | width | "stretch", "content", or int |  | The width of the code block element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.divider


* Function signature:

   st.divider(*, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | width | "stretch" or int |  | The width of the divider element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



Here's what it looks like in action when you have multiple elements in the app:

```python
import streamlit as st

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule
```

<Image src="/images/api/st.divider.png"/>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.echo


* Function signature:

   st.echo(code_location="above")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | code_location | "above" or "below" |  | Whether to show the echoed code before or after the results of the executed code block. |



### Display code

Sometimes you want your Streamlit app to contain _both_ your usual
Streamlit graphic elements _and_ the code that generated those elements.
That's where `st.echo()` comes in.

Ok so let's say you have the following file, and you want to make its
app a little bit more self-explanatory by making that middle section
visible in the Streamlit app:

```python
import streamlit as st

def get_user_name():
    return 'John'

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')
```

The file above creates a Streamlit app containing the words "Hi there,
`John`", and then "Done!".

Now let's use `st.echo()` to make that middle section of the code visible
in the app:

```python
import streamlit as st

def get_user_name():
    return 'John'

with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
```

It's _that_ simple!

<Note>

You can have multiple `st.echo()` blocks in the same file.
Use it as often as you wish!

</Note>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.latex


* Function signature:

   st.latex(body, *, help=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str or SymPy expression |  | The string or SymPy expression to display as LaTeX. If str, it's a good idea to use raw Python strings since LaTeX uses backslashes a lot. |
   | help | str or None |  | A tooltip that gets displayed next to the LaTeX expression. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | width | "stretch", "content", or int |  | The width of the LaTeX element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |


<Image src="/images/api/st.latex.png"/>

---

Source: https://docs.streamlit.io/develop/api-reference/text/st.text


* Function signature:

   st.text(body, *, help=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The string to display. |
   | help | str or None |  | A tooltip that gets displayed next to the text. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | width | "content", "stretch", or int |  | The width of the text element. This can be one of the following:  "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.help


* Function signature:

   st.help(obj=&lt;module 'streamlit' from '/Users/dmatthews/Documents/GitHub/streamlit/lib/streamlit/__init__.py'&gt;, *, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | obj | any |  | The object whose information should be displayed. If left unspecified, this call will display help for Streamlit itself. |
   | width | "stretch" or int |  | The width of the help element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/text/st.html


* Function signature:

   st.html(body, *, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | any |  | The HTML code to insert. This can be one of the following:  A string of HTML code. A path to a local file with HTML code. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run). Any object. If body is not a string or path, Streamlit will convert the object to a string. body._repr_html_() takes precedence over str(body) when available.  If the resulting HTML content is empty, Streamlit will raise an error. If body is a path to a CSS file, Streamlit will wrap the CSS content in  tags automatically. When the resulting HTML content only contains style tags, Streamlit will send the content to the event container instead of the main container to avoid taking up space in the app. |
   | width | "stretch", "content", or int |  | The width of the HTML element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

# Data elements

Source: https://docs.streamlit.io/develop/api-reference/data


When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

<TileContainer>
<RefCard href="/develop/api-reference/data/st.dataframe">
<Image>alt="screenshot" src="/images/api/dataframe.jpg" /&gt;

<h4>Dataframes</h4>

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">
<Image>alt="screenshot" src="/images/api/data_editor.jpg" /&gt;

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config">
<Image>alt="screenshot" src="/images/api/column_config.jpg" /&gt;

<h4>Column configuration</h4>

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.table">
<Image>alt="screenshot" src="/images/api/table.jpg" /&gt;

<h4>Static tables</h4>

Display a static table.

```python
st.table(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.metric">
<Image>alt="screenshot" src="/images/api/metric.jpg" /&gt;

<h4>Metrics</h4>

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.json">
<Image>alt="screenshot" src="/images/api/json.jpg" /&gt;

<h4>Dicts and JSON</h4>

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```

</Image></RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">
<Image>alt="screenshot" src="/images/api/components/aggrid.jpg" /&gt;

<h4>Streamlit Aggrid</h4>

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">
<Image>alt="screenshot" src="/images/api/components/folium.jpg" /&gt;

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">
<Image>alt="screenshot" src="/images/api/components/pandas-profiling.jpg" /&gt;

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">
<Image>alt="screenshot" src="/images/api/components/image-coordinates.jpg" /&gt;

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">
<Image>alt="screenshot" src="/images/api/components/plotly-events.jpg" /&gt;

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```

</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/data/st.dataframe

<Tip>

Learn more in our [Dataframes](/develop/concepts/design/dataframes) guide and check out our tutorial, [Get dataframe row-selections from users](/develop/tutorials/elements/dataframe-row-selections).

</Tip>

* Function signature:

   st.dataframe(data=None, width="stretch", height="auto", *, use_container_width=None, hide_index=None, column_order=None, column_config=None, key=None, on_select="ignore", selection_mode="multi-row", row_height=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | dataframe-like, collection-like, or None |  | The data to display. Dataframe-like objects include dataframe and series objects from popular libraries like Dask, Modin, Numpy, pandas, Polars, PyArrow, Snowpark, Xarray, and more. You can use database cursors and clients that comply with the Python Database API Specification v2.0 (PEP 249). Additionally, you can use anything that supports the Python dataframe interchange protocol. For example, you can use the following:  pandas.DataFrame, pandas.Series, pandas.Index, pandas.Styler, and pandas.Array polars.DataFrame, polars.LazyFrame, and polars.Series snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table  If a data type is not recognized, Streamlit will convert the object to a pandas.DataFrame or pyarrow.Table using a .to_pandas() or .to_arrow() method, respectively, if available. If data is a pandas.Styler, it will be used to style its underlying pandas.DataFrame. Streamlit supports custom cell values, colors, and font weights. It does not support some of the more exotic styling options, like bar charts, hovering, and captions. For these styling options, use column configuration instead. Text and number formatting from column_config always takes precedence over text and number formatting from pandas.Styler. Collection-like objects include all Python-native Collection types, such as dict, list, and set. If data is None, Streamlit renders an empty table. |
   | width | "stretch", "content", or int |  | The width of the dataframe element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "auto", "stretch", or int |  | The height of the dataframe element. This can be one of the following:  "auto" (default): Streamlit sets the height to show at most ten rows. "stretch": The height of the element expands to fill the available vertical space in its parent container. When multiple elements with stretch height are in the same container, they share the available vertical space evenly. The dataframe will maintain a minimum height to display up to three rows, but otherwise won't exceed the available height in its parent container. An integer specifying the height in pixels: The element has a fixed height.  Vertical scrolling within the dataframe element is enabled when the height does not accommodate all rows. |
   | use_container_width | bool |  | Whether to override width with the width of the parent container. If this is True (default), Streamlit sets the width of the dataframe to match the width of the parent container. If this is False, Streamlit sets the dataframe's width according to width. |
   | hide_index | bool or None |  | Whether to hide the index column(s). If hide_index is None (default), the visibility of index columns is automatically determined based on the data and other configurations. |
   | column_order | Iterable[str] or None |  | The ordered list of columns to display. If this is None (default), Streamlit displays all columns in the order inherited from the underlying data structure. If this is a list, the indicated columns will display in the order they appear within the list. Columns may be omitted or repeated within the list. For example, column_order=("col2", "col1") will display "col2" first, followed by "col1", and will hide all other non-index columns. column_order does not accept positional column indices and can't move the index column(s). |
   | column_config | dict or None |  | Configuration to customize how columns are displayed. If this is None (default), columns are styled based on the underlying data type of each column. Column configuration can modify column names, visibility, type, width, format, and more. If this is a dictionary, the keys are column names (strings) and/or positional column indices (integers), and the values are one of the following:  None to hide the column. A string to set the display label of the column. One of the column types defined under st.column_config. For example, to show a column as dollar amounts, use st.column_config.NumberColumn("Dollar values", format="$ %d"). See more info on the available column types and config options here.  To configure the index column(s), use "_index" as the column name, or use a positional column index where 0 refers to the first index column. |
   | key | str |  | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters. Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |
   | on_select | "ignore" or "rerun" or callable |  | How the dataframe should respond to user selection events. This controls whether or not the dataframe behaves like an input widget. on_select can be one of the following:  "ignore" (default): Streamlit will not react to any selection events in the dataframe. The dataframe will not behave like an input widget. "rerun": Streamlit will rerun the app when the user selects rows, columns, or cells in the dataframe. In this case, st.dataframe will return the selection data as a dictionary. A callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.dataframe will return the selection data as a dictionary. |
   | selection_mode | "single-row", "multi-row", "single-column",             "multi-column", "single-cell", "multi-cell", or Iterable of these |  | The types of selections Streamlit should allow when selections are enabled with on_select. This can be one of the following:  "multi-row" (default): Multiple rows can be selected at a time. "single-row": Only one row can be selected at a time. "multi-column": Multiple columns can be selected at a time. "single-column": Only one column can be selected at a time. "multi-cell": A rectangular range of cells can be selected. "single-cell": Only one cell can be selected at a time. An Iterable of the above options: The table will allow selection based on the modes specified. For example, to allow the user to select multiple rows and multiple cells, use ["multi-row", "multi-cell"].  When column selections are enabled, column sorting is disabled. |
   | row_height | int or None | row | The height of each row in the dataframe in pixels. If row_height is None (default), Streamlit will use a default row height, which fits one line of text. |

* Returns: element or dict

    If on_select is "ignore" (default), this command returns an
internal placeholder for the dataframe element that can be used
with the .add_rows() method. Otherwise, this command returns a
dictionary-like object that supports both key and attribute
notation. The attributes are described by the DataframeState
dictionary schema.



## Dataframe selections


* Function signature:

   DataframeState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | selection | dict |  | The state of the on_select event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the DataframeSelectionState dictionary schema. |



* Function signature:

   DataframeSelectionState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | rows | list[int] |  | The selected rows, identified by their integer position. The integer positions match the original dataframe, even if the user sorts the dataframe in their browser. For a pandas.DataFrame, you can retrieve data from its integer position using methods like .iloc[] or .iat[]. |
   | columns | list[str] |  | The selected columns, identified by their names. |
   | cells | list[tuple[int, str]] |  | The selected cells, provided as a tuple of row integer position and column name. For example, the first cell in a column named "col 1" is represented as (0, "col 1"). Cells within index columns are not returned. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



## Interactivity

Dataframes displayed with `st.dataframe` are interactive. End users can sort, resize, search, and copy data to their clipboard. For on overview of features, read our [Dataframes](/develop/concepts/design/dataframes#additional-ui-features) guide.

## Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud height="480px" name="doc-column-config-overview" query="embed_options=disable_scrolling"/>

---

Source: https://docs.streamlit.io/develop/api-reference/data/st.data_editor

<Tip>

This page only contains information on the `st.data_editor` API. For an overview of working with dataframes and to learn more about the data editor's capabilities and limitations, read [Dataframes](/develop/concepts/design/dataframes).

</Tip>

* Function signature:

   st.data_editor(data, *, width="stretch", height="auto", use_container_width=None, hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, on_change=None, args=None, kwargs=None, row_height=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe | to | The data to edit in the data editor.  Note  Styles from pandas.Styler will only be applied to non-editable columns. Text and number formatting from column_config always takes precedence over text and number formatting from pandas.Styler. If your dataframe starts with an empty column, you should set the column datatype in the underlying dataframe to ensure your intended datatype, especially for integers versus floats. Mixing data types within a column can make the column uneditable. Additionally, the following data types are not yet supported for editing: complex, tuple, bytes, bytearray, memoryview, dict, set, frozenset, fractions.Fraction, pandas.Interval, and pandas.Period. To prevent overflow in JavaScript, columns containing datetime.timedelta and pandas.Timedelta values will default to uneditable, but this can be changed through column configuration. |
   | width | "stretch", "content", or int |  | The width of the data editor. This can be one of the following:  "stretch" (default): The width of the editor matches the width of the parent container. "content": The width of the editor matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The editor has a fixed width. If the specified width is greater than the width of the parent container, the width of the editor matches the width of the parent container. |
   | height | int, "auto", or "stretch" |  | The height of the editor. This can be one of the following:  "auto" (default): Streamlit sets the height to show at most ten rows. "stretch": The height of the editor expands to fill the available vertical space in its parent container. When multiple elements with stretch height are in the same container, they share the available vertical space evenly. The editor will maintain a minimum height to display up to three rows, but otherwise won't exceed the available height in its parent container. An integer specifying the height in pixels: The editor has a fixed height.  Vertical scrolling within the editor is enabled when the height does not accommodate all rows. |
   | use_container_width | bool |  | Whether to override width with the width of the parent container. If this is True (default), Streamlit sets the width of the data editor to match the width of the parent container. If this is False, Streamlit sets the data editor's width according to width. |
   | hide_index | bool or None |  | Whether to hide the index column(s). If hide_index is None (default), the visibility of index columns is automatically determined based on the data. |
   | column_order | Iterable[str] or None |  | The ordered list of columns to display. If this is None (default), Streamlit displays all columns in the order inherited from the underlying data structure. If this is a list, the indicated columns will display in the order they appear within the list. Columns may be omitted or repeated within the list. For example, column_order=("col2", "col1") will display "col2" first, followed by "col1", and will hide all other non-index columns. column_order does not accept positional column indices and can't move the index column(s). |
   | column_config | dict or None |  | Configuration to customize how columns are displayed. If this is None (default), columns are styled based on the underlying data type of each column. Column configuration can modify column names, visibility, type, width, format, editing properties like min/max, and more. If this is a dictionary, the keys are column names (strings) and/or positional column indices (integers), and the values are one of the following:  None to hide the column. A string to set the display label of the column. One of the column types defined under st.column_config. For example, to show a column as dollar amounts, use st.column_config.NumberColumn("Dollar values", format="$ %d"). See more info on the available column types and config options here.  To configure the index column(s), use "_index" as the column name, or use a positional column index where 0 refers to the first index column. |
   | num_rows | "fixed" or "dynamic" | s | Specifies if the user can add and delete rows in the data editor. If "fixed", the user cannot add or delete rows. If "dynamic", the user can add and delete rows in the data editor, but column sorting is disabled. Defaults to "fixed". |
   | disabled | bool or Iterable[str | int] |  | Controls the editing of columns. This can be one of the following:  False (default): All columns that support editing are editable. True: All columns are disabled for editing. An Iterable of column names and/or positional indices: The specified columns are disabled for editing while the remaining columns are editable where supported. For example, disabled=["col1", "col2"] will disable editing for the columns named "col1" and "col2".  To disable editing for the index column(s), use "_index" as the column name, or use a positional column index where 0 refers to the first index column. |
   | key | str |  | An optional string to use as the unique key for this widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | on_change | callable |  | An optional callback invoked when this data_editor's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | row_height | int or None | row | The height of each row in the data editor in pixels. If row_height is None (default), Streamlit will use a default row height, which fits one line of text. |

* Returns: pandas.DataFrame, pandas.Series, pyarrow.Table, numpy.ndarray, list, set, tuple, or dict.

    The edited data. The edited data is returned in its original data type if
it corresponds to any of the supported return types. All other data types
are returned as a pandas.DataFrame.



### Configuring columns

You can configure the display and editing behavior of columns in `st.dataframe` and `st.data_editor` via the [Column configuration API](/develop/api-reference/data/st.column_config). We have developed the API to let you add images, charts, and clickable URLs in dataframe and data editor columns. Additionally, you can make individual columns editable, set columns as categorical and specify which options they can take, hide the index of the dataframe, and much more.

<Cloud height="480px" name="doc-column-config-overview" query="embed_options=disable_scrolling"/>

---


---

**Navigation:** [← Previous](./02-define-multipage-apps-with-stpage-and-stnavigation.md) | [Index](./index.md) | [Next →](./04-column-configuration.md)
