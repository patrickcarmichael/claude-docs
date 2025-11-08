---
title: "Use the Google Auth Platform to authenticate users"
source: https://docs.streamlit.io/develop/tutorials/authentication/google
section: 237
---

# Use the Google Auth Platform to authenticate users

Source: https://docs.streamlit.io/develop/tutorials/authentication/google


Google is one of the most popular identity providers for social logins. You can use the Google Auth Platform with both private and organizational Google accounts. This tutorial configures authentication for anyone with a Google account. For more information, see Google's overview of the [Google Auth Platform](https://support.google.com/cloud/topic/15540269?hl=en=3473162=576431444945556851-NC) and [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect#discovery).

## Prerequisites

- This tutorial requires the following Python libraries:

  ```text
  streamlit&gt;=1.42.0
  Authlib&gt;=1.3.2
  ```python
- You should have a clean working directory called `your-repository`.
- You must have a Google account and accept the terms of [Google Cloud](https://console.cloud.google.com/) to use their authentication service.
- You must have a project in Google Cloud within which to create your application.
  For more information about managing your projects in Google Cloud, see [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in Google's documentation.

## Summary

In this tutorial, you'll build an app that users can log in to with their Google accounts. When they log in, they'll see a personalized greeting with their name and have the option to log out.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

`.streamlit/secrets.toml`

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```python
`app.py`

```python
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)
```python
</Collapse>

---

[← Previous](236-authenticate-users-and-personalize-your-app.md) | [Index](index.md) | [Next →](index.md)
