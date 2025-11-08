---
title: "Configuration"
source: https://docs.streamlit.io/develop/api-reference/configuration
section: 218
---

# Configuration

Source: https://docs.streamlit.io/develop/api-reference/configuration


<TileContainer>
<RefCard href="/develop/api-reference/configuration/config.toml">
<h4>Configuration file</h4>

Configures the default settings for your app.

```python
your-project/
├── .streamlit/
│   └── config.toml
└── your_app.py
```python
</RefCard>
<RefCard href="/develop/api-reference/configuration/st.get_option">
<h4>Get config option</h4>

Retrieve a single configuration option.

```python
st.get_option("theme.primaryColor")
```python
</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_option">
<h4>Set config option</h4>

Set a single configuration option. (This is very limited.)

```python
st.set_option("deprecation.showPyplotGlobalUse", False)
```python
</RefCard>
<RefCard href="/develop/api-reference/configuration/st.set_page_config">
<h4>Set page title, favicon, and more</h4>

Configures the default settings of the page.

```python
st.set_page_config(
  page_title="My app",
  page_icon=":shark:",
)
```python
</RefCard>
</TileContainer>

---

[← Previous](207-custom-components.md) | [Index](index.md) | [Next →](index.md)
