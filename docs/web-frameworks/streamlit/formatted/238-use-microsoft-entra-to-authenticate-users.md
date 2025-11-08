---
title: "Use Microsoft Entra to authenticate users"
source: https://docs.streamlit.io/develop/tutorials/authentication/microsoft
section: 238
---

# Use Microsoft Entra to authenticate users

Source: https://docs.streamlit.io/develop/tutorials/authentication/microsoft


[Microsoft Identity Platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview) is a service within Microsoft Entra that lets you build applications to authenticate users. Your applications can use personal, work, and school accounts managed by Microsoft.

## Prerequisites

- This tutorial requires the following Python libraries:

  ```text
  streamlit&gt;=1.42.0
  Authlib&gt;=1.3.2
  ```python
- You should have a clean working directory called `your-repository`.
- You must have a Microsoft Azure account, which includes Microsoft Entra ID.

## Summary

In this tutorial, you'll build an app that users can log in to with their personal Microsoft accounts. When they log in, they'll see a personalized greeting with their name and have the option to log out.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

`.streamlit/secrets.toml`

```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://login.microsoftonline.com/consumers/v2.0/.well-known/openid-configuration"
```python
`app.py`

```python
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Microsoft", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)
```python
</Collapse>

---

[← Previous](237-use-the-google-auth-platform-to-authenticate-users.md) | [Index](index.md) | [Next →](index.md)
