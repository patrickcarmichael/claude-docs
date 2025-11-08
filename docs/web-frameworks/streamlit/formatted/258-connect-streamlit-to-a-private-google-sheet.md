---
title: "Connect Streamlit to a private Google Sheet"
source: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet
section: 258
---

# Connect Streamlit to a private Google Sheet

Source: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet


## Introduction

This guide explains how to securely access a private Google Sheet from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

If you are fine with enabling link sharing for your Google Sheet (i.e. everyone with the link can view it), the guide [Connect Streamlit to a public Google Sheet](/develop/tutorials/databases/public-gsheet) shows a simpler method of doing this. If your Sheet contains sensitive information and you cannot enable link sharing, keep on reading.

### Prerequisites

This tutorial requires `streamlit&gt;=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet

If you already have a Sheet that you want to use, you can [skip to the next step](#enable-the-sheets-api).

Create a spreadsheet with this example data.

<div>{{ maxWidth: '200px', margin: 'auto' }}&gt;

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

---

[← Previous](257-connect-streamlit-to-postgresql.md) | [Index](index.md) | [Next →](index.md)
