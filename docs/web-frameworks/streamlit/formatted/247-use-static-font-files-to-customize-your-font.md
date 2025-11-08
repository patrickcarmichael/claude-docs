---
title: "Use static font files to customize your font"
source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/static-fonts
section: 247
---

# Use static font files to customize your font

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/static-fonts


Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses static font files and is a walkthrough of Example 2 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-2-define-an-alternative-font-with-static-font-files). For an example that uses variable font files, see [Use variable font files to customize your font](/develop/tutorials/configuration-and-theming/variable-fonts).

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.45.0
  ```python
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of [static file serving](/develop/concepts/configuration/serving-static-files).
- You should have a basic understanding of working with font files in web development. Otherwise, start by reading [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts) up to Example 2.

## Summary

The following example uses [Tuffy](https://fonts.google.com/specimen/Tuffy) font. The font has four static font files which cover the four following weight-style pairs:

- normal normal
- normal bold
- italic normal
- italic bold

Here's a look at what you'll build:

<Collapse title="Complete config.toml file">{false}&gt;

Directory structure:

```none
your_repository/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── Tuffy-Bold.ttf
│   ├── Tuffy-BoldItalic.ttf
│   ├── Tuffy-Italic.ttf
│   └── Tuffy-Regular.ttf
└── streamlit_app.py
```python
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
```python
`streamlit_app.py`:

```python
import streamlit as st

st.write("Normal ABCabc123")
st.write("*Italic ABCabc123*")
st.write("**Bold ABCabc123**")
st.write("***Bold-italic ABCabc123***")
st.write("`Code ABCabc123`")
```python
</Collapse>

---

[← Previous](246-use-externally-hosted-fonts-and-fallbacks-to-customize-your-font-streamlit.md) | [Index](index.md) | [Next →](index.md)
