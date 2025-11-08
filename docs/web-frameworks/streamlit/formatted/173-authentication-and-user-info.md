---
title: "Authentication and user info"
source: https://docs.streamlit.io/develop/api-reference/user
section: 173
---

# Authentication and user info

Source: https://docs.streamlit.io/develop/api-reference/user


Streamlit provides native support for user authentication so you can personalize your apps. You can also directly read headers and cookies.

<TileContainer>
<RefCard href="/develop/api-reference/user/st.login">
<h4>Log in a user</h4>

`st.login()` starts an authentication flow with an identity provider.

```python
st.login()
```python
</RefCard>
<RefCard href="/develop/api-reference/user/st.logout">
<h4>Log out a user</h4>

`st.logout()` removes a user's identity information.

```python
st.logout()
```python
</RefCard>
<RefCard href="/develop/api-reference/user/st.user">
<h4>User info</h4>

`st.user` returns information about a logged-in user.

```python
if st.user.is_logged_in:
  st.write(f"Welcome back, {st.user.name}!")
```python
</RefCard>
</TileContainer>

---

[← Previous](161-display-progress-and-status.md) | [Index](index.md) | [Next →](index.md)
