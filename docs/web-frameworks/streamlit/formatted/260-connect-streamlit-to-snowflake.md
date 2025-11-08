---
title: "Connect Streamlit to Snowflake"
source: https://docs.streamlit.io/develop/tutorials/databases/snowflake
section: 260
---

# Connect Streamlit to Snowflake

Source: https://docs.streamlit.io/develop/tutorials/databases/snowflake


## Introduction

This guide explains how to securely access a Snowflake database from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), the [Snowpark library](https://docs.snowflake.com/en/developer-guide/snowpark/python/index), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

### Prerequisites

- The following packages must be installed in your Python environment:

  ```txt
  streamlit&gt;=1.28
  snowflake-snowpark-python&gt;=0.9.0
  snowflake-connector-python&gt;=2.8.0
  ```python
    <Note>
        Use the correct version of Python required by `snowflake-snowpark-python`. For example, if you use `snowflake-snowpark-python==1.23.0`, you must use Python version \&gt;=3.8, \</Note>

---

[← Previous](259-connect-streamlit-to-a-public-google-sheet.md) | [Index](index.md) | [Next →](index.md)
