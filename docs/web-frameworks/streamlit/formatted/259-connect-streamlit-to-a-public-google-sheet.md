---
title: "Connect Streamlit to a public Google Sheet"
source: https://docs.streamlit.io/develop/tutorials/databases/public-gsheet
section: 259
---

# Connect Streamlit to a public Google Sheet

Source: https://docs.streamlit.io/develop/tutorials/databases/public-gsheet


## Introduction

This guide explains how to securely access a public Google Sheet from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide to [Connect Streamlit to a private Google Sheet](private-gsheet).

### Prerequisites

This tutorial requires `streamlit&gt;=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet and turn on link sharing

If you already have a Sheet that you want to access, you can [skip to the next step](#add-the-sheets-url-to-your-local-app-secrets). See Google's documentation on how to [share spreadsheets](https://support.google.com/docs/answer/9331169?hl=en#6.1) for more information.

Create a spreadsheet with this example data and create a share link. The link should have "Anyone with the link" set as a "Viewer."

<div>{{ maxWidth: '200px', margin: 'auto' }}&gt;

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

---

[← Previous](258-connect-streamlit-to-a-private-google-sheet.md) | [Index](index.md) | [Next →](index.md)
