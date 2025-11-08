---
title: "How to download a Pandas DataFrame as a CSV?"
source: https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv
section: 335
---

# How to download a Pandas DataFrame as a CSV?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv


Use the [`st.download_button`](/develop/api-reference/widgets/st.download_button) widget that is natively built into Streamlit. Check out a [sample app](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/) demonstrating how you can use `st.download_button` to download common file formats.

## Example usage

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("dir/file.csv")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
```python
Additional resources:

- [https://blog.streamlit.io/0-88-0-release-notes/](https://blog.streamlit.io/0-88-0-release-notes/)
- [https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/)
- [https://docs.streamlit.io/develop/api-reference/widgets/st.download_button](/develop/api-reference/widgets/st.download_button)

---

[← Previous](334-how-to-download-a-file-in-streamlit.md) | [Index](index.md) | [Next →](index.md)
