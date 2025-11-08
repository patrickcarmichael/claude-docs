---
title: "Create a dynamic navigation menu"
source: https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation
section: 274
---

# Create a dynamic navigation menu

Source: https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation


`st.navigation` makes it easy to build dynamic navigation menus. You can change the set of pages passed to `st.navigation` with each rerun, which changes the navigation menu to match. This is a convenient feature for creating custom, role-based navigation menus.

This tutorial uses `st.navigation` and `st.Page`, which were introduced in Streamlit version 1.36.0. For an older workaround using the `pages/` directory and `st.page_link`, see [Build a custom navigation menu with `st.page_link`](/develop/tutorials/multipage/st.page_link-nav).

## Applied concepts

- Use `st.navigation` and `st.Page` to define a multipage app.
- Create a dynamic, role-based navigation menu.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```python
  streamlit&gt;=1.36.0
  ```python
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of `st.navigation` and `st.Page`.

## Summary

In this example, we'll build a dynamic navigation menu for a multipage app that depends on the current user's role. You'll abstract away the use of username and credentials to simplify the example. Instead, you'll use a selectbox to let users choose a role and log in.

The entrypoint file, `streamlit_app.py` will handle user authentication. The other pages will be stubs representing account management (`settings.py`) and specific pages associated to three roles: Requester, Responder, and Admin. Requesters can access the account and request pages. Responders can access the account and respond pages. Admins can access all pages.

Here's a look at what we'll build:

<Collapse title="Complete code">{false}&gt;

**Directory structure:**

```python
your-repository/
├── admin
│   ├── admin_1.py
│   └── admin_2.py
├── images
│   ├── horizontal_blue.png
│   └── icon_blue.png
├── request
│   ├── request_1.py
│   └── request_2.py
├── respond
│   ├── respond_1.py
│   └── respond_2.py
├── settings.py
└── streamlit_app.py
```python
**`streamlit_app.py`:**

```python
import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Requester", "Responder", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
request_1 = st.Page(
    "request/request_1.py",
    title="Request 1",
    icon=":material/help:",
    default=(role == "Requester"),
)
request_2 = st.Page(
    "request/request_2.py", title="Request 2", icon=":material/bug_report:"
)
respond_1 = st.Page(
    "respond/respond_1.py",
    title="Respond 1",
    icon=":material/healing:",
    default=(role == "Responder"),
)
respond_2 = st.Page(
    "respond/respond_2.py", title="Respond 2", icon=":material/handyman:"
)
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
admin_2 = st.Page("admin/admin_2.py", title="Admin 2", icon=":material/security:")

account_pages = [logout_page, settings]
request_pages = [request_1, request_2]
respond_pages = [respond_1, respond_2]
admin_pages = [admin_1, admin_2]

st.title("Request manager")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = request_pages
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages

if len(page_dict) &gt; 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
```python
</Collapse>

---

[← Previous](273-build-multipage-apps.md) | [Index](index.md) | [Next →](index.md)
