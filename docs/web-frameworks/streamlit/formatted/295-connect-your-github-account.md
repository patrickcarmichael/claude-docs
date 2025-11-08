---
title: "Connect your GitHub account"
source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account
section: 295
---

# Connect your GitHub account

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account


Connecting GitHub to your Streamlit Community Cloud account allows you to deploy apps directly from the files you store in your repositories. It also lets the system check for updates to those files and automatically update your apps. When you first connect your GitHub account to your Community Cloud account, you'll be able to deploy apps from your public repositories to Community Cloud. If you want to deploy from private repositories, you can give Community Cloud additional permissions to do so. For more information about these permissions, see [GitHub OAuth scope](/deploy/streamlit-community-cloud/status#github-oauth-scope).

<Important>
    In order to deploy an app, you must have **admin** permissions to its repository. If you don't have admin access, contact the repository's owner or fork the repository to create your own copy. For more help, see our <a href="https://discuss.streamlit.io/" target="_blank">community forum</a>.
</Important>

If you are a member of a GitHub organization, that organization is displayed at the bottom of each GitHub OAuth prompt. In this case, we recommend reading about [Organization access](#organization-access) at the end of this page before performing the steps to connect your GitHub account. You must be an organization's owner in GitHub to grant access to that organization.

## Prerequisites

- You must have a Community Cloud account. See [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).
- You must have a GitHub account.

## Add access to public repositories

1. In the upper-left corner, click "**Workspaces <i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

[← Previous](294-create-your-account.md) | [Index](index.md) | [Next →](index.md)
