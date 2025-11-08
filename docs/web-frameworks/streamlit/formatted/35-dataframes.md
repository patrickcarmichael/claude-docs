---
title: "Dataframes"
source: https://docs.streamlit.io/develop/concepts/design/dataframes
section: 35
---

# Dataframes

Source: https://docs.streamlit.io/develop/concepts/design/dataframes


Dataframes are a great way to display and edit data in a tabular format. Working with Pandas DataFrames and other tabular data structures is key to data science workflows. If developers and data scientists want to display this data in Streamlit, they have multiple options: `st.dataframe` and `st.data_editor`. If you want to solely display data in a table-like UI, [st.dataframe](/develop/api-reference/data/st.dataframe) is the way to go. If you want to interactively edit data, use [st.data_editor](/develop/api-reference/data/st.data_editor). We explore the use cases and advantages of each option in the following sections.

## Display dataframes with st.dataframe

Streamlit can display dataframes in a table-like UI via `st.dataframe` :

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
```python
<Cloud height="300px" name="doc-dataframe-basic"/>

## `st.dataframe` UI features

`st.dataframe` provides additional functionality by using [glide-data-grid](https://github.com/glideapps/glide-data-grid) under the hood:

- **Column sorting**: To sort columns, select their headers, or select "**Sort ascending**" or "**Sort descending**" from the header menu (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

[← Previous](34-button-behavior-and-examples.md) | [Index](index.md) | [Next →](index.md)
