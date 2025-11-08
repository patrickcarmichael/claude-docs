---
title: "Streamlit API cheat sheet"
source: https://docs.streamlit.io/develop/quick-reference/cheat-sheet
section: 277
---

# Streamlit API cheat sheet

Source: https://docs.streamlit.io/develop/quick-reference/cheat-sheet


This is a summary of the docs for the latest version of Streamlit, [v1.51.0](https://pypi.org/project/streamlit/1.51.0/).

<Masonry>
<CodeTile>

#### Install  Import

```python
pip install streamlit

streamlit run first_app.py

# Import convention
&gt;&gt;&gt; import streamlit as st
```python
</CodeTile>
<CodeTile>

#### Pre-release features

```python
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```python
Learn more about [experimental features](advanced-features/prerelease#experimental-features)

</CodeTile>
<CodeTile>

#### Command line

```python
streamlit cache clear
streamlit config show
streamlit docs
streamlit hello
streamlit help
streamlit init
streamlit run streamlit_app.py
streamlit version
```python
</CodeTile>
</Masonry>
<Masonry>
<CodeTile>

#### Magic commands

```python
# Magic commands implicitly
# call st.write().
"_This_ is some **Markdown**"
my_variable
"dataframe:", my_data_frame

```python
</CodeTile>
<CodeTile>

#### Display text

```python
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is </CodeTile></Masonry>

---

[← Previous](276-quick-reference.md) | [Index](index.md) | [Next →](index.md)
