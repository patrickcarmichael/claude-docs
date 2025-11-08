---
title: "Deploy your app on Community Cloud"
source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
section: 304
---

# Deploy your app on Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy


After you've [organized your files](/deploy/streamlit-community-cloud/deploy-your-app/file-organization) and [added your dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) as described on the previous pages, you're ready to deploy your app to Community Cloud!

## Select your repository and entrypoint file

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, in the upper-right corner, click "**Create app**."

   ![Deploy a new app from your workspace](/images/streamlit-community-cloud/deploy-empty-new-app.png)

1. When asked "Do you already have an app?" click "**Yup, I have an app**."
1. Fill in your repository, branch, and file path. Alternatively, to paste a link directly to `your_app.py` on GitHub, click "**Paste GitHub URL**."
1. Optional: In the "App URL" field, choose a subdomain for your new app.

   Every Community Cloud app is deployed to a subdomain on `streamlit.app`, but you can change your app's subdomain at any time. For more information, see [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings). In the following example, Community Cloud will deploy an app to `https://red-balloon.streamlit.app/`.

   ![Fill in your app's information to deploy your app](/images/streamlit-community-cloud/deploy-an-app.png)

   Although Community Cloud attempts to suggest available repositories and files, these suggestions are not always complete. If the desired information is not listed for any field, enter it manually.

## Optional: Configure secrets and Python version

<Note>

Streamlit Community Cloud supports all released [versions of Python that are still receiving security updates](https://devguide.python.org/versions/). Streamlit Community Cloud defaults to version 3.12. You can select a version of your choice from the "Python version" dropdown in the "Advanced settings" modal. If an app is running a version of Python that becomes unsupported, it will be forcibly upgraded to the oldest supported version of Python and may break.

</Note>

1. Click "**Advanced settings**."
1. Select your desired version of Python.
1. To define environment variables and secrets, in the "Secrets" field, paste the contents of your `secrets.toml` file.

   For more information, see [Community Cloud secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

1. Click "**Save**."

<div>{{ maxWidth: '70%', margin: 'auto' }}&gt;
<Image alt="Advanced settings for deploying your app" src="/images/streamlit-community-cloud/deploy-an-app-advanced.png"/>
</div>

---

[← Previous](303-secrets-management-for-your-community-cloud-app.md) | [Index](index.md) | [Next →](index.md)
