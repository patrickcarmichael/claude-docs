---
title: "How do I create an anchor link?"
source: https://docs.streamlit.io/knowledge-base/using-streamlit/create-anchor-link
section: 332
---

# How do I create an anchor link?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/create-anchor-link


## Overview

Have you wanted to create anchors so that users of your app can directly navigate to specific sections by specifying `#anchor` in the URL? If so, let's find out how.

## Solution

Anchors are automatically added to header text.

For example, if you define a header text via the [st.header()](/develop/api-reference/text/st.header) command as follows:

```python
st.header("Section 1")
```python
Then you can create a link to this header using:

```python
st.markdown("[Section 1](#section-1)")
```python
## Examples

- Demo app: [https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/](https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/)
- GitHub repo: [https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py](https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py)

---

[← Previous](331-faq.md) | [Index](index.md) | [Next →](index.md)
