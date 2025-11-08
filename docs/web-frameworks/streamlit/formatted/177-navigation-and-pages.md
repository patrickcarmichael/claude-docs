---
title: "Navigation and pages"
source: https://docs.streamlit.io/develop/api-reference/navigation
section: 177
---

# Navigation and pages

Source: https://docs.streamlit.io/develop/api-reference/navigation


<TileContainer>
<RefCard href="/develop/api-reference/navigation/st.navigation">
<Image>alt="screenshot" src="/images/api/navigation.jpg" /&gt;

<h4>Navigation</h4>

Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account" : [log_out, settings],
    "Reports" : [overview, usage],
    "Tools" : [search]
})
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/navigation/st.page">
<Image>alt="screenshot" src="/images/api/page.jpg" /&gt;

<h4>Page</h4>

Define a page in a multipage app.

```python
home = st.Page(
    "home.py",
    title="Home",
    icon=":material/home:"
)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">
<Image>alt="screenshot" src="/images/api/page_link.jpg" /&gt;

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/navigation/st.switch_page">
<h4>Switch page</h4>

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```python
</RefCard>
</TileContainer>

---

[← Previous](173-authentication-and-user-info.md) | [Index](index.md) | [Next →](index.md)
