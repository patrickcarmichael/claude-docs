---
title: "Create a fragment across multiple containers"
source: https://docs.streamlit.io/develop/tutorials/execution-flow/create-a-multiple-container-fragment
section: 271
---

# Create a fragment across multiple containers

Source: https://docs.streamlit.io/develop/tutorials/execution-flow/create-a-multiple-container-fragment


Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. If your fragment doesn't write to outside containers, Streamlit will clear and redraw all the fragment elements with each fragment rerun. However, if your fragment _does_ write elements to outside containers, Streamlit will not clear those elements during a fragment rerun. Instead, those elements accumulate with each fragment rerun until the next full-script rerun. If you want a fragment to update multiple containers in your app, use [`st.empty()`](/develop/api-reference/layout/st.empty) containers to prevent accumulating elements.

## Applied concepts

- Use fragments to run two independent processes separately.
- Distribute a fragment across multiple containers.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.37.0
  ```python
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.empty()`.

## Summary

In this toy example, you'll build an app with six containers. Three containers will have orange cats. The other three containers will have black cats. You'll have three buttons in the sidebar: "**Herd the black cats**," "**Herd the orange cats**," and "**Herd all the cats**." Since herding cats is slow, you'll use fragments to help Streamlit run the associated processes efficiently. You'll create two fragments, one for the black cats and one for the orange cats. Since the buttons will be in the sidebar and the fragments will update containers in the main body, you'll use a trick with `st.empty()` to ensure you don't end up with too many cats in your app (if it's even possible to have too many cats). 😻

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import time

st.title("Cats!")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]


def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")


def orange_cats():
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")


@st.fragment
def herd_black_cats(card_a, card_b, card_c):
    st.button("Herd the black cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()


@st.fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("Herd the orange cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()


with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
    herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
    st.button("Herd all the cats")
```python
</Collapse>

---

[← Previous](270-trigger-a-full-script-rerun-from-inside-a-fragment.md) | [Index](index.md) | [Next →](index.md)
