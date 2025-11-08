**Navigation:** [← Previous](./10-2023-release-notes.md) | [Index](./index.md) | [Next →](./12-how-do-i-increase-the-upload-limit-of-stfile-uploa.md)

---

# Deploy an app from a template

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/deploy-from-a-template


Streamlit Community Cloud makes it easy to get started with several convenient templates. Just pick a template, and Community Cloud will fork it to your account and deploy it. Any edits you push to your new fork will immediately show up in your deployed app. Additionally, if you don't want to use a local development environment, Community Cloud makes it easy to create a GitHub codespace that's fully configured for Streamlit app development.

## Access the template picker

There are two ways to begin deploying a template: the "**Create app**" button and the template gallery at the bottom of your workspace.

- If you click the "**Create app**" button, Community Cloud will ask you "Do you already have an app?" Select "**Nope, create one from a template**."
- If you scroll to the bottom of your workspace in the "**My apps**" section, you can see the most popular templates. Click on one directly, or select "**View all templates**."

The template picker shows a list of available templates on the left. A preview for the current, selected template shows on the right.

!["Deploy from a template" page on Community Cloud](/images/streamlit-community-cloud/deploy-template-picker.png)

## Select a template

1. From the list of templates on the left, select "**GDP dashboard**."
1. Optional: For "Name of new GitHub repository," enter a name for your new, forked repository.

   When you deploy a template, Community Cloud forks the template repository into your GitHub account. Community Cloud chooses a default name for this repository based on the selected template. If you have previously deployed the same template with its default name, Community Cloud will append an auto-incrementing number to the name.

   <Note>
       Even if you have another user's or organization's workspace selected, Community Cloud will always deploy a template app from your personal workspace. That is, Community Cloud will always fork a template into your GitHub user account. If you want to deploy a template app from an organization, manually fork the template in GitHub, and deploy it from your fork in the associated workspace.
   </Note>

1. Optional: In the "App URL" field, choose a subdomain for your new app.

   Every Community Cloud app is deployed to a subdomain on `streamlit.app`, but you can change your app's subdomain at any time. For more information, see [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings).

1. Optional: To edit the template in a GitHub codespace immediately, select the option to "**Open GitHub Codespaces...**"

   You can create a codespace for your app at any time. To learn how to create a codespace after you've deployed an app, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).

1. Optional: To change the version of Python, at the bottom of the screen, click "**Advanced settings**," select a Python version, and then click "**Save**."

   <Important>
       After an app is deployed, you can't change the version of Python without deleting and redeploying the app. 
   </Important>

1. At the bottom, click "**Deploy**."

## View your app

- If you didn't select the option to open GitHub Codespaces, you are redirected to your new app.

  ![GDP dashboard template app](/images/streamlit-community-cloud/deploy-template-GDP.png)

- If you selected the option to open GitHub Codespaces, you are redirected to your new codespace, which can take several minutes to be fully initialized. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.

  ![GDP dashboard template app in a codespace](/images/streamlit-community-cloud/deploy-template-GDP-codespace.png)

<Important>
    The app displayed in your codespace is not the same instance you deployed on Community Cloud. Your codespace is a self-contained development environment. When you make edits inside a codespace, those edits don't leave the codespace until you commit them to your repository. When you commit your changes to your repository, Community Cloud detects the changes and updates your deployed app. To learn more, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).
</Important>

---

# Fork and edit a public app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/fork-and-edit-a-public-app


Community Cloud is all about learning, sharing, and exploring the world of Streamlit. For apps with public repositories, you can quickly fork copies to your GitHub account, deploy your own version, and jump into a codespace on GitHub to start editing and exploring Streamlit code.

1. From a forkable app, in the upper-right corner, click "**Fork**."

   ![Click Fork in the upper-right corner of a public app](/images/streamlit-community-cloud/fork-public-hello.png)

1. Optional: In the "App URL" field, choose a custom subdomain for your app.

   Every Community Cloud app is deployed to a subdomain on `streamlit.app`, but you can change your app's subdomain at any time. For more information, see [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings).

1. Click "**Fork!**"

   The repository will be forked to your GitHub account. If you have already forked the repository, Community Cloud will use the existing fork. If your existing fork already has an associated codespace, the codespace will be reused.

   <Warning>
      Do not use this method in the following situations:
      - You have an existing repository that matches the fork name (but isn't a fork of this app).
      - You have an existing fork of this app, but you've changed the name of the repository.

   If you have an existing fork of this app and kept the original repository name, Community Cloud will use your existing fork. If you've previously deployed the app and opened a codespace, Community Cloud will open your existing codespace.
   </Warning>

   ![Click Fork to confirm and deploy your app](/images/streamlit-community-cloud/fork-public-hello-deploy.png)

1. Wait for GitHub to set up your codespace.

   It can take several minutes to fully initialize your codespace. After the Visual Studio Code editor appears in your codespace, it can take several minutes to install Python and start the Streamlit server. When complete, a split screen view displays a code editor on the left and a running app on the right. The code editor opens two tabs by default: the repository's readme file and the app's entrypoint file.

   ![Click Fork to confirm and deploy your app](/images/streamlit-community-cloud/fork-public-hello-codespace.png)

   <Important>
      The app displayed in your codespace is not the same instance you deployed on Community Cloud. Your codespace is a self-contained development environment. When you make edits inside a codespace, those edits don't leave the codespace until you commit them to your repository. When you commit your changes to your repository, Community Cloud detects the changes and updates your deployed app. To learn more, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).
   </Important>

1. Edit your newly forked app as desired. For more instructions on working with GitHub Codespaces, see [Edit your app](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app).

---

# Streamlit trust and security

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/trust-and-security


Streamlit is a framework that turns Python scripts into interactive apps, giving data scientists the ability to quickly create data and model-based apps for the entire company.

A simple Streamlit app is:

```python
import streamlit as st
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
```

When you `streamlit run my_app.py`, you start a web server that runs the interactive application on your local computer at `http://localhost:8501`. This is great for local development. When you want to share with your colleagues, Streamlit Community Cloud enables you to deploy and run these applications in the cloud. Streamlit Community Cloud handles the details of containerization and provides you an interface for easily managing your deployed apps.

This document provides an overview of the security safeguards we've implemented to protect you and your data. Security, however, is a shared responsibility and you are ultimately responsible for making appropriate use of Streamlit and the Streamlit Community Cloud, including implementation of appropriate user-configurable security safeguards and best practices.

## Product security

### Authentication

You must authenticate through GitHub to deploy or administer an app. Authentication through Google or single-use emailed links are required to view a private app when you don't have push or admin permissions on the associated GitHub repository. The single-use emailed links are valid for 15 minutes once requested.

### Permissions

Streamlit Community Cloud inherits the permissions you have assigned in GitHub. Users with write access to a GitHub repository for a given app will be able to make changes in the Streamlit administrative console. However, only users with _admin access_ to a repository are able to **deploy and delete apps**.

## Network and application security

### Data hosting

Our physical infrastructure is hosted and managed within secure data centers maintained by infrastructure-as-a-service cloud providers. Streamlit leverages many of these platforms' built-in security, privacy, and redundancy features. Our cloud providers continually monitor their data centers for risk and undergo assessments to ensure compliance with industry standards.

### Data deletion

Community Cloud users have the option to delete any apps they’ve deployed as well as their entire account.

When a user deletes their application from the admin console, we delete their source code, including any files copied from their GitHub repository or created within our system from the running app. However, we keep a record representing the application in our database. This record contains the coordinates of the application: the GitHub organization or user, the GitHub repository, the branch, and the path of the main module file.

When a user deletes their account, we perform a hard deletion of their data and a hard deletion of all the apps that belong to the GitHub identity associated with their account. In this case, we do not maintain the records of application coordinates described above. When an account is deleted, we also delete any HubSpot contact associated with the Community Cloud account.

### Virtual private cloud

All of our servers are within a virtual private cloud (VPC) with firewalls and network access control lists (ACLs) to allow external access to a select few API endpoints; all other internal services are only accessible within the VPC.

### Encryption

Streamlit apps are served entirely over HTTPS. We use only strong cipher suites and HTTP Strict Transport Security (HSTS) to ensure browsers interact with Streamlit apps over HTTPS.

All data sent to or from Streamlit over the public internet is encrypted in transit using 256-bit encryption. Our API and application endpoints use Transport Layer Security (TLS) 1.2 (or better). We also encrypt data at rest on disk using AES-256.

### Permissions and authentication

Access to Community Cloud user account data is limited to authorized personnel. We run a zero-trust corporate network, utilize single sign-on and multi-factor authentication (MFA), and enforce strong password policies to ensure access to cloud-related services is protected.

### Incident response

Our internal protocol for handling security events includes detection, analysis, response, escalation, and mitigation. Security advisories are made available at [https://streamlit.io/advisories](https://streamlit.io/advisories).

### Penetration testing

Streamlit uses third-party security tools to scan for vulnerabilities on a regular basis. Our security teams conduct periodic, intensive penetration tests on the Streamlit platform. Our product development team responds to any identified issues or potential vulnerabilities to ensure the quality, security, and availability of Streamlit applications.

### Vulnerability management

We keep our systems up-to-date with the latest security patches and continuously monitor for new vulnerabilities. This includes automated scanning of our code repositories for vulnerable dependencies.

If you discover a vulnerability in one of our products or websites, please report the issue to [HackerOne](https://hackerone.com/snowflake?type=team).

---

# Prep and deploy your app on Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app


Streamlit Community Cloud lets you deploy your apps in just one click, and most apps will be deployed in only a few minutes. If you don't have an app ready to deploy, you can fork or clone one from our <a href="https://streamlit.io/gallery" target="_blank">App gallery</a>you can find apps for machine learning, data visualization, data exploration, A/B testing, and more. You can also [Deploy an app from a template](/deploy/streamlit-community-cloud/get-started/deploy-from-a-template). After you've deployed your app, check out how you can [Edit your app with GitHub Codespaces](/deploy/streamlit-community-cloud/manage-your-app/edit-your-app#edit-your-app-with-github-codespaces).

<Note>

If you want to deploy your app on a different cloud service, see our [Deployment tutorials](/deploy/tutorials).

</Note>

## Summary

The pages that follow explain how to organize your app and provide complete information for Community Cloud to run it correctly.

When your app has everything it needs, deploying is easy. Just go to your workspace and click "**Create app**" in the upper-right corner. Follow the prompts to fill in your app's information, and then click "**Deploy**."

![Deploy a new app from your workspace](/images/streamlit-community-cloud/deploy-empty-new-app.png)

## Ready, set, go!

<InlineCalloutContainer>
<InlineCallout bold="File organization." color="lightBlue-70" href="/deploy/streamlit-community-cloud/deploy-your-app/file-organization" icon="description">Learn how Community Cloud initializes your app and interprets paths. Learn where to put your configuration files.</InlineCallout>
<InlineCallout bold="App dependencies." color="lightBlue-70" href="/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies" icon="build_circle">Learn how to install dependencies and other Python libraries into your deployment environment.</InlineCallout>
<InlineCallout bold="Secrets management." color="lightBlue-70" href="/deploy/streamlit-community-cloud/deploy-your-app/secrets-management" icon="password">Learn about the interface Community Cloud provides to securely upload your <code>secrets.toml</code> data.</InlineCallout>
<InlineCallout bold="Deploy your app" color="lightBlue-70" href="/deploy/streamlit-community-cloud/deploy-your-app/deploy" icon="flight_takeoff">Put it all together to deploy your app for the whole world to see.</InlineCallout>
</InlineCalloutContainer>

---

# File organization for your Community Cloud app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization


Streamlit Community Cloud copies all the files in your repository and executes `streamlit run` from its root directory. Because Community Cloud is creating a new Python environment to run your app, you need to include a declaration of any [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) in addition to any [Configuration](/develop/concepts/configuration) options.

You can have multiple apps in your repository, and their entrypoint files can be anywhere in your repository. However, you can only have one configuration file. This page explains how to correctly organize your app, configuration, and dependency files. The following examples assume you are using `requirements.txt` to declare your dependencies because it is the most common. As explained on the next page, Community Cloud supports other formats for configuring your Python environment.

## Basic example

In the following example, the entrypoint file (`your_app.py`) is in the root of the project directory alongside a `requirements.txt` file to declare the app's dependencies.

```
your_repository/
├── requirements.txt
└── your_app.py
```

If you are including custom configuration, your config file must be located at `.streamlit/config.toml` within your repository.

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── your_app.py
```

Additionally, any files that need to be locally available to your app should be included in your repository.

<Tip>

If you have really big or binary data that you change frequently, and git is running slowly, you might want to check out [Git Large File Store (LFS)](https://git-lfs.github.com/) as a better way to store large files in GitHub. You don't need to make any changes to your app to start using it. If your GitHub repository uses LFS, it will _just work_ with Streamlit Community Cloud.

</Tip>

## Use an entrypoint file in a subdirectory

When your entrypoint file is in a subdirectory, the configuration file must stay at the root. However, your dependency file may be either at the root or next to your entrypoint file.

Your dependency file can be at the root of your repository while your entrypoint file is in a subdirectory.

```
your_repository/
├── .streamlit/
│   └── config.toml
├── requirements.txt
└── subdirectory
    └── your_app.py
```

Alternatively, your dependency file can be in the same subdirectory as your entrypoint file.

```
your_repository/
├── .streamlit/
│   └── config.toml
└── subdirectory
    ├── requirements.txt
    └── your_app.py
```

Although most Streamlit commands interpret paths relative to the entrypoint file, some commands interpret paths relative to the working directory. On Community Cloud, the working directory is always the root of your repository. Therefore, when developing and testing your app locally, execute `streamlit run` from the root of your repository. This ensures that paths are interpreted consistently between your local environment and Community Cloud.

In the previous example, this would look something like this:

```bash
cd your_repository
streamlit run subdirectory/your_app.py
```

<Tip>
    Remember to always use forward-slash path separators in your paths. Community Cloud can't work with backslash-separated paths.
</Tip>

## Multiple apps in one repository

When you have multiple apps in one repository, they share the same configuration file (`.streamlit/config.toml`) at the root of your repository. A dependency file may be shared or configured separately for these multiple apps. To define separate dependency files for your apps, place each entrypoint file in its own subdirectory along with its own dependency file. To learn more about how Community Cloud prioritizes and parses dependency files, see [App dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies).

---

# App dependencies for your Community Cloud app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies


The main reason that apps fail to build properly is because Streamlit Community Cloud can't find your dependencies! There are two kinds of dependencies your app might have: Python dependencies and external dependencies. Python dependencies are other Python packages (just like Streamlit!) that you `import` into your script. External dependencies are less common, but they include any other software your script needs to function properly. Because Community Cloud runs on Linux, these will be Linux dependencies installed with `apt-get` outside the Python environment.

For your dependencies to be installed correctly, make sure you:

1. Add a [requirements file](#add-python-dependencies) for Python dependencies.
2. Optional: To manage any external dependencies, add a `packages.txt` file.

<Note>

Python requirements files should be placed either in the root of your repository or in the same
directory as your app's entrypoint file.

</Note>

## Add Python dependencies

With each `import` statement in your script, you are bringing in a Python dependency. You need to tell Community Cloud how to install those dependencies through a Python package manager. We recommend using a `requirements.txt` file, which is based on `pip`.

You should _not_ include <a href="https://docs.python.org/3/py-modindex.html" target="_blank">built-in Python libraries</a> like `math`, `random`, or `distutils` in your `requirements.txt` file. These are a part of Python and aren't installed separately. Also, Community Cloud has `streamlit` installed by default. You don't strictly need to include `streamlit` unless you want to pin or restrict the version. If you deploy an app without a `requirements.txt` file, your app will run in an environment with just `streamlit` (and its dependencies) installed.

<Important>

The version of Python you use is important! Built-in libraries change between versions of Python and other libraries may have specific version requirements, too. Whenever Streamlit supports a new version of Python, Community Cloud quickly follows to default to that new version of Python. Always develop your app in the same version of Python you will use to deploy it. For more information about setting the version of Python when you deploy your app, see [Optional: Configure secrets and Python version](/deploy/streamlit-community-cloud/deploy-your-app/deploy#optional-configure-secrets-and-python-version).

</Important>

If you have a script like the following, no extra dependencies would be needed since `pandas` and `numpy` are installed as direct dependencies of `streamlit`. Similarly, `math` and `random` are built into Python.

```python
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write("Hi!")
```

However, a valid `requirements.txt` file would be:

```none
streamlit
pandas
numpy
```

Alternatively, if you needed to specify certain versions, another valid example would be:

```none
streamlit==1.24.1
pandas&gt;2.0
numpy

---

# Secrets management for your Community Cloud app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management


## Introduction

If you are [connecting to data sources](/develop/tutorials/databases), you will likely need to handle credentials or secrets. Storing unencrypted secrets in a git repository is a bad practice. If your application needs access to sensitive credentials, the recommended solution is to store those credentials in a file that is not committed to the repository and to pass them as environment variables.

## How to use secrets management

Community Cloud lets you save your secrets within your app's settings. When developing locally, you can use `st.secrets` in your code to read secrets from a `.streamlit/secrets.toml` file. However, this `secrets.toml` file should never be committed to your repository. Instead, when you deploy your app, you can paste the contents of your `secrets.toml` file into the "**Advanced settings**" dialog. You can update your secrets at any time through your app's settings in your workspace.

### Prerequisites

- You should understand how to use `st.secrets` and `secrets.toml`. See [Secrets management](/develop/concepts/connections/secrets-management).

### Advanced settings

While deploying your app, you can access "**Advanced settings**" to set your secrets. After your app is deployed, you can view or update your secrets through the app's settings. The deployment workflow is fully described on the next page, but the "**Advanced settings**" dialog looks like this:

<div>{{ maxWidth: '70%', margin: 'auto' }}&gt;
<Image alt="Advanced settings for deploying your app" src="/images/streamlit-community-cloud/deploy-an-app-advanced.png"/>
</div>

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

# Manage your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app


You can manage your deployed app from your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> or directly from `<your-custom-subdomain>.streamlit.app`. You can view, deploy, delete, reboot, or favorite an app.

## Manage your app from your workspace

Streamlit Community Cloud is organized into workspaces, which automatically group your apps according to their repository's owner in GitHub. Your workspace is indicated in the upper-left corner. For more information, see [Switching workspaces](/deploy/streamlit-community-cloud/get-started/explore-your-workspace#switching-workspaces).

To deploy or manage any app, always switch to the workspace matching the repository's owner first.

### Sort your apps

If you have many apps in your workspace, you can pin apps to the top by marking them as favorite (<i>{{ verticalAlign: "-.25em", color: "#faca2b" }} className={{ class: "material-icons-sharp" }}&gt;star</i></your-custom-subdomain>). For more information, see [Favorite your app](/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app).

### App overflow menus

Each app has a menu accessible from the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# App analytics

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-analytics


Streamlit Community Cloud allows you to see the viewership of each of your apps. Specifically, you can see:

- The total viewers count of your app (counted from April 2022).
- The most recent unique viewers (capped at the last 20 viewers).
- A relative timestamp of each unique viewer's last visit.

![App analytics on Streamlit Community Cloud](/images/streamlit-community-cloud/workspace-app-analytics-viewers.png)

## Access your app analytics

You can get to your app's analytics:

- [From your workspace](#access-app-analytics-from-your-workspace).
- [From your Cloud logs](#access-app-analytics-from-your-cloud-logs).

### Access app analytics from your workspace

From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# App settings

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/app-settings


This page is about your app settings on Streamlit Community Cloud. From your app settings you can [view or change your app's URL](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url), manage [public or private access to your app](/deploy/streamlit-community-cloud/share-your-app), and update your saved [secrets for your apps](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

If you access "**Settings**" from your [app chrome](/develop/concepts/architecture/app-chrome) in the upper-right corner of your running app, you can access features to control the appearance of your app while it's running.

## Access your app settings

You can get to your app's settings:

- [From your workspace](#access-app-settings-from-your-workspace).
- [From your Cloud logs](#access-app-settings-from-your-cloud-logs).

### Access app settings from your workspace

From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# Delete your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/delete-your-app


If you need to delete your app, it's simple and easy. There are several cases where you may need to delete your app:

- You have finished playing around with an example app.
- You want to deploy from a private repository but already have a private app.
- You want to [change the Python version](/deploy/streamlit-community-cloud/manage-your-app/upgrade-python) for your app.
- You want to [rename your repository](/deploy/streamlit-community-cloud/manage-your-app/rename-your-app) or move your entrypoint file.

If you delete your app and intend to immediately redploy it, your custom subdomain should be immediately available for reuse. Read more about data deletion in [Streamlit trust and security](/deploy/streamlit-community-cloud/get-started/trust-and-security#data-deletion).

You can delete your app:

- [From your workspace](#delete-your-app-from-your-workspace).
- [From your Cloud logs](#delete-your-app-from-your-cloud-logs).

### Delete your app from your workspace

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# Edit your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/edit-your-app


You can edit your app from any development environment of your choice. Streamlit Community Cloud will monitor your repository and automatically copy any file changes you commit. You will immediately see commits reflected in your deployed app for most changes (such as edits to your app's Python files).

Community Cloud also makes it easy to skip the work of setting up a development environment. With a few simple clicks, you can configure a development environment using GitHub Codespaces.

## Edit your app with GitHub Codespaces

Spin up a cloud-based development environment for your deployed app in minutes. You can run your app within your codespace to enjoy experimenting in a safe, sandboxed environment. When you are done editing your code, you can commit your changes to your repo or just leave them in your codespace to return to later.

### Create a codespace for your deployed app

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# Favorite your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/favorite-your-app


Streamlit Community Cloud supports a "favorite" feature that lets you quickly access your apps from your workspace. Favorited apps appear at the top of their workspace with a yellow star (<i>{{ verticalAlign: "-.25em", color: "#faca2b" }} className={{ class: "material-icons-sharp" }}&gt;star</i>

---

# Reboot your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app


If you need to clear your app's memory or force a fresh build after modifying a file that Streamlit Community Cloud doesn't monitor, you may need to reboot your app. This will interrupt any user who may currently be using your app and may take a few minutes for your app to redeploy. Anyone visiting your app will see "Your app is in the oven" during a reboot.

Rebooting your app on Community Cloud is easy! You can reboot your app:

- [From your workspace](#reboot-your-app-from-your-workspace).
- [From your Cloud logs](#reboot-your-app-from-your-cloud-logs).

### Reboot your app from your workspace

1. From your workspace at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>, click the overflow icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# Rename or change your app's GitHub coordinates

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/rename-your-app


Streamlit Community Cloud identifies apps by their GitHub coordinates (owner, repository, branch, entrypoint file path). If you move or rename one of these coordinates without preparation, you will lose access to administer any associated app.

## Delete, rename, redeploy

If you need to rename your repository, move your entrypoint file, or otherwise change a deployed app's GitHub coordinates, do the following:

1. Delete your app.
1. Make your desired changes in GitHub.
1. Redeploy your app.

## Regain access when you've already made changes to your app's GitHub coordinates

If you have changed a repository so that Community Cloud can no longer find your app on GitHub, your app will be missing or shown as view-only. View-only means that you can't edit, reboot, delete, or view settings for your app. You can only access analytics.

You may be able to regain control as follows:

1. Revert the change you made to your app so that Community Cloud can see the owner, repository, branch, and entrypoint file it expects.
1. Sign out of Community Cloud and GitHub.
1. Sign back in to Community Cloud and GitHub.
1. If you have regained access, delete your app. Proceed with your original change, and redeploy your app.

   If this does not restore access to your app, please [contact Snowflake support](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud) for assistance. They can delete your disconnected apps so you can redeploy them. For the quickest help, please provide a complete list of your affected apps by URL.

---

# Upgrade your app's Python version on Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-python


Dependencies within Python can be upgraded in place by simply changing your environment configuration file (typically `requirements.txt`). However, Python itself can't be changed after deployment.

When you deploy an app, you can select the version of Python through the "**Advanced settings**" dialog. After you have deployed an app, you must delete it and redeploy it to change the version of Python it uses.

1. Take note of your app's settings:
   - Current, custom subdomain.
   - GitHub coordinates (repository, branch, and entrypoint file path).
   - Secrets.

   When you delete an app, its custom subdomain is immediately available for reuse.

1. [Delete your app](/deploy/streamlit-community-cloud/manage-your-app/delete-your-app).
1. [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app).
   1. On the deployment page, select your app's GitHub coordinates.
   1. Set your custom domain to match your deleted instance.
   1. Click "**Advanced settings**."
   1. Choose your desired version of Python.
   1. Optional: If your app had secrets, re-enter them.
   1. Click "**Save**."
   1. Click "**Deploy**."

In a few minutes, Community Cloud will redirect you to your redployed app.

---

# Upgrade your app's Streamlit version on Streamlit Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app/upgrade-streamlit


Want to use a cool new Streamlit feature but your app on Streamlit Community Cloud is running an old version of the Streamlit library? If that's you, don't worry! Here's how to upgrade your app's Streamlit version, based on how you manage your [app dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies):

## No dependency file

When there is no dependencies file in your repository, your app will use the lastest Streamlit version that existed when it was last rebooted. In this case, simply [reboot your app](/deploy/streamlit-community-cloud/manage-your-app/reboot-your-app) and Community Cloud will install the latest version.

You may want to avoid getting into this situation if your app depends on a specific version of Streamlit. That is why we encourage you to use a dependency file and pin your desired version of Streamlit.

## With a dependency file

When your app includes a dependency file, reboot your app or change your dependency file as follows:

- If Streamlit is not included in your dependency file, reboot the app as described above.

  Note that we don't recommend having an incomplete dependency file since `pip` won't be able to include `streamlit` when resolving compatible versions of your dependencies.

- If Streamlit is included in your dependency file, but the version is not pinned or capped, reboot the app as described above.

  When Community Cloud reboots your app, it will re-resolve your dependency file. Your app will then have the latest version of all dependencies that are consistent with your dependency file.

- If Streamlit is included in your dependency file, and the version is pinned (e.g., `streamlit==1.37.0`), update your dependency file.

  When you commit a change to your dependency file in your repository, Community Cloud will detect the change and automatically resolve the new dependencies. This is how you add, remove, or change all Python dependencies in general. You don't need to manually reboot your app, but you can if you want to.

---

# Share your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app


Now that your app is deployed you can easily share it and collaborate on it. But first, let's take a moment and do a little joy dance for getting that app deployed! 🕺💃

Your app is now live at a fixed URL, so go wild and share it with whomever you want. Your app will inherit permissions from your GitHub repo, meaning that if your repo is private your app will be private and if your repo is public your app will be public. If you want to change that you can simply do so from the app settings menu.

You are only allowed one private app at a time. If you've deployed from a private repository, you will have to make that app public or delete it before you can deploy another app from a private repository. Only developers can change your app between public and private.

- [Make your app public or private](#make-your-app-public-or-private)
- [Share your public app](#share-your-public-app)
- [Share your private app](#share-your-private-app)

## Make your app public or private

If you deployed your app from a public repository, your app will be public by default. If you deployed your app from a private repository, you will need to make the app public if you want to freely share it with the community at large.

### Set privacy from your app settings

1. Access your [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings) and go to the "**Sharing**" section.

   ![Share settings on Streamlit Community Cloud](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)

2. Set your app's privacy under "Who can view this app." Select "**This app is public and searchable**" to make your app public. Select "**Only specific people can view this app**" to make your app private.

   ![Set your app's privacy in share settings](/images/streamlit-community-cloud/workspace-app-settings-sharing-change.png)

### Set privacy from the share button

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.

   ![Access the share button from your app](/images/streamlit-community-cloud/share-open.png)

2. Toggle your app between public and private by clicking "**Make this app public**."

   ![Toggle your app between public and private from the share button](/images/streamlit-community-cloud/share-menu-public-toggle.png)

## Share your public app

Once your app is public, just give anyone your app's URL and they view it! Streamlit Community Cloud has several convenient shortcuts for sharing your app.

### Share your app on social media

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Click "**Social**" to access convenient social media share buttons.

   ![Social media sharing links from the share button](/images/streamlit-community-cloud/share-menu-social.png)

<Tip>

Use the social media sharing buttons to post your app on our forum! We'd love to see what you make and perhaps feature your app as our app of the month. 💖

</Tip>

### Invite viewers by email

Whether your app is public or private, you can send an email invite to your app directly from Streamlit Community Cloud. This grants the viewer access to analytics for all your public apps and the ability to invite other viewers to your workspace. Developers and invited viewers are identified by their email in analytics instead of appearing anonymously (if they view any of your apps while signed in). Read more about viewers in [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics).

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.
2. Enter an email address and click "**Invite**."

   ![Invite viewers from the share button](/images/streamlit-community-cloud/share-invite-public.png)

3. Invited users will get a direct link to your app in their inbox.

   ![Invitation email sent to viewers](/images/streamlit-community-cloud/share-invite-email.png)

### Copy your app's URL

From your app click "**Share**" in the upper-right corner then click "**Copy link**."

![Copy your app's URL from the share button](/images/streamlit-community-cloud/share-copy.png)

### Add a badge to your GitHub repository

To help others find and play with your Streamlit app, you can add Streamlit's GitHub badge to your repo. Below is an enlarged example of what the badge looks like. Clicking on the badge takes you toin this caseStreamlit's Roadmap.

<div>{{ marginBottom: '2em' }}&gt;
<div>{{ width: 'fit-content', margin: 'auto' }}&gt;
    <a href="https://roadmap.streamlit.app/" target="_blank">
<Image alt="Open in Streamlit badge for GitHub" src="/images/streamlit-community-cloud/github-badge.svg"/>
</a>
</div></div></your-custom-subdomain>
</your-custom-subdomain>

Once you deploy your app, you can embed this badge right into your GitHub README.md by adding the following Markdown:

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<your-custom-subdomain>.streamlit.app)
```

<Note>

Be sure to replace `https://<your-custom-subdomain>.streamlit.app` with the URL of your deployed app!

</your-custom-subdomain>

## Share your private app

By default an app deployed from a private repository will be private to the developers in the workspace. A private app will not be visible to anyone else unless you grant them explicit permission. You can grant permission by adding them as a developer on GitHub or by adding them as a viewer on Streamlit Community Cloud.

Once you have added someone's email address to your app's viewer list, that person will be able to sign in and view your private app. If their email is associated with a Google account, they will be able to sign in with Google OAuth. Otherwise, they will be able to sign in with single-use, emailed links. Streamlit sends an email invitation with a link to your app every time you invite someone.

<Important>

When you add a viewer to any app in your workspace, they are granted access to analytics for that app as well as analytics for all your public apps. They can also pass these permissions to others by inviting more viewers. All viewers and developers in your workspace are identified by their email in analytics. Furthermore, their emails show in analytics for every app in your workspace and not just apps they are explicitly invited to. Read more about viewers in [App analytics](/deploy/streamlit-community-cloud/manage-your-app/app-analytics)

</Important>

### Invite viewers from the share button

1. From your app at `<your-custom-subdomain>.streamlit.app`, click "**Share**" in the upper-right corner.

   ![Access the share button from your app](/images/streamlit-community-cloud/share-open.png)

2. Enter the email to send an invitation to and click "**Invite**."

   ![Invite viewers from the share button](/images/streamlit-community-cloud/share-invite.png)

3. Invited users appear in the list below.

   ![View invited users from the share button](/images/streamlit-community-cloud/share-invited.png)

4. Invited users will get a direct link to your app in their inbox.

   ![Invitation email sent to viewers](/images/streamlit-community-cloud/share-invite-email.png)

- To remove a viewer, simply access the share menu as above and click the <i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;close</i></your-custom-subdomain> next to their name.

  ![Remove viewers from the share button](/images/streamlit-community-cloud/share-remove.png)

### Invite viewers from your app settings

1. Access your [App settings](/deploy/streamlit-community-cloud/manage-your-app/app-settings) and go to the "**Sharing**" section.

   ![Access sharing settings from your app settings](/images/streamlit-community-cloud/workspace-app-settings-sharing.png)

2. Add or remove users from the list of viewers. Click "**Save**."

   ![Invite and remove viewers from your app settings](/images/streamlit-community-cloud/workspace-app-settings-sharing-invite.png)</Note></your-custom-subdomain></your-custom-subdomain>

---

# Embed your app

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/embed-your-app


Embedding Streamlit Community Cloud apps enriches your content by integrating interactive, data-driven applications directly within your pages. Whether you're writing a blog post, a technical document, or sharing resources on platforms like Medium, Notion, or even StackOverflow, embedding Streamlit apps adds a dynamic component to your content. This allows your audience to interact with your ideas, rather than merely reading about them or looking at screenshots.

Streamlit Community Cloud supports both [iframe](#embedding-with-iframes) and [oEmbed](#embedding-with-oembed) methods for embedding **public** apps. This flexibility enables you to share your apps across a wide array of platforms, broadening your app's visibility and impact. In this guide, we'll cover how to use both methods effectively to share your Streamlit apps with the world.

## Embedding with iframes

Streamlit Community Cloud supports embedding **public** apps using the subdomain scheme. To embed a public app, add the query parameter `/?embed=true` to the end of the `*.streamlit.app` URL.

For example, say you want to embed the <a href="https://30days.streamlit.app/" target="_blank">30DaysOfStreamlit app</a>. The URL to include in your iframe is: `https://30days.streamlit.app/?embed=true`:

```javascript
<iframe src="https://30days.streamlit.app?embed=true" style="height: 450px; width: 100%;"/>
```

<Cloud height="450px" name="30days"/>
<Important>

There will be no official support for embedding private apps.

</Important>

In addition to allowing you to embed apps via iframes, the `?embed=true` query parameter also does the following:

- Removes the toolbar with the app menu icon (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_vert</i>

---

# SEO and search indexability

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/indexability


When you deploy a public app to Streamlit Community Cloud, it is automatically indexed by search engines like Google and Bing on a weekly basis. 🎈 This means that anyone can find your app by <a href="https://www.google.com/search?q=traingenerator.streamlit.app" target="_blank">searching for its custom subdomain</a> (e.g. "traingenerator.streamlit.app") or by searching for the app's title.

## Get the most out of app indexability

Here are some tips to help you get the most out of app indexability:

1. [Make sure your app is public](#make-sure-your-app-is-public)
2. [Choose a custom subdomain early](#choose-a-custom-subdomain-early)
3. [Choose a descriptive app title](#choose-a-descriptive-app-title)
4. [Customize your app's meta description](#customize-your-apps-meta-description)

### Make sure your app is public

All public apps hosted on Community Cloud are indexed by search engines. If your app is private, it will not be indexed by search engines. To make your private app public, read [Share your app](/deploy/streamlit-community-cloud/share-your-app).

### Choose a custom subdomain early

Community Cloud automatically generates a subdomain for your app if you do not choose one. However, you can change your subdomain at any time! Custom subdomains modify your app URLs to reflect your app content, personal branding, or whatever you’d like. To learn how to change your app's subdomain, see [View or change your app's URL](/deploy/streamlit-community-cloud/manage-your-app/app-settings#view-or-change-your-apps-url).

By choosing a custom subdomain, you can use it to help people find your app. For example, if you're deploying an app that generates training data, you might choose a subdomain like `traingenerator.streamlit.app`. This makes it easy for people to find your app by searching for "training generator" or "train generator streamlit app."

We recommend choosing a custom subdomain when you deploy your app. This ensures that your app is indexed by search engines using your custom subdomain, rather than the automatically generated one. If you choose a custom subdomain later, your app may be indexed multiple timesonce using the default subdomain and once using your custom subdomain. In this case, your old URL will result in a 404 error which can confuse users who are searching for your app.

### Choose a descriptive app title

The meta title of your app is the text that appears in search engine results. It is also the text that appears in the browser tab when your app is open. By default, the meta title of your app is the same as the title of your app. However, you can customize the meta title of your app by setting the [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) parameter `page_title` to a custom string. For example:

```python
st.set_page_config(page_title="Traingenerator")
```

This will change the meta title of your app to "Traingenerator." This makes it easier for people to find your app by searching for "Traingenerator" or "train generator streamlit app":

<Image caption='Google search results for "train generator streamlit app"' src="/images/streamlit-community-cloud/indexability-app-title.png"/>

### Customize your app's meta description

Meta descriptions are the short descriptions that appear in search engine results. Search engines use the meta description to help users understand what your app is about.

From our observations, search engines seem to favor the content in both `st.header` and `st.text` over `st.title`. If you put a description at the top of your app under `st.header` or `st.text`, there’s a good chance search engines will use this for the meta description.

## What does my indexed app look like?

If you're curious about what your app looks like in search engine results, you can type the following into Google Search:

```
site:<your-custom-subdomain>.streamlit.app
```

Example: `site:traingenerator.streamlit.app`

<Image caption='Google search results for "site:traingenerator.streamlit.app"' src="/images/streamlit-community-cloud/indexability-search-result.png"/>

## What if I don't want my app to be indexed?

If you don't want your app to be indexed by search engines, you can make it private. Read [Share your app](/deploy/streamlit-community-cloud/share-your-app) to learn more about making your app private. Note: each workspace can only have one private app. If you want to make your app private, you must first delete any other private app in your workspace or make it public.

That said, Community Cloud is an open and free platform for the community to deploy, discover, and share Streamlit apps and code with each other. As such, we encourage you to make your app public so that it can be indexed by search engines and discovered by other Streamlit users and community members.</your-custom-subdomain>

---

# Share previews

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/share-your-app/share-previews


Social media sites generate a card with a title, preview image, and description when you share a link. This feature is called a "share preview." In the same way, when you share a link to a public Streamlit app on social media, a share preview is also generated. Here's an example of a share preview for a public Streamlit app posted on Twitter:

<div>{{ marginLeft: '3em' }}&gt;
    <Flex>
<Image caption="Share preview for a public Streamlit app" src="/images/streamlit-community-cloud/share-preview-twitter-annotated.png"/>
</Flex>
</div>

---

# Manage your account

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account


You can [Update your email](/deploy/streamlit-community-cloud/manage-your-account/update-your-email) or completely [Delete your account](/deploy/streamlit-community-cloud/manage-your-account/delete-your-account) through [Workspace settings](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings).

Your Streamlit Community Cloud account is identified by your email. When you sign in to Community Cloud, regardless of which method you use, you are providing Community Cloud with your email address. In particular, when you sign in to Community Cloud using GitHub, you are using the primary email on your GitHub account. You can view your email identity and source-control identity from your workspace settings, under "[**Linked accounts**](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings#linked-accounts)."

## Access your workspace settings

1. Sign in to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. In the upper-left corner, click on your workspace name.
1. In the drop-down menu, click "**Settings**."

<div>{{ maxWidth: '75%', marginLeft: '3em' }}&gt;
    <Image alt="Access your workspace settings from your workspace" src="/images/streamlit-community-cloud/account-settings-header.png"/>
</div>

---

# Sign in  sign out

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out


After you've created your account, you can sign in to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> as described by the following options.

![Sign in to Streamlit Community Cloud](/images/streamlit-community-cloud/account-sign-in.png)

## Sign in with Google

1. Click "**Continue to sign-in**."
1. Click "**Continue with Google**."
1. Enter your Google account credentials and follow the prompts.

If your account is already linked to GitHub, you may be immediately prompted to sign in with GitHub.

## Sign in with GitHub

1. Click "**Continue to sign-in**."
1. Click "**Continue with GitHub**."
1. Enter your GitHub credentials and follow the prompts.

<Important>
    When you sign in with GitHub, Community Cloud will look for an account that uses the same email you have on your GitHub account. If such an account doesn't exist, Community Cloud will look for an account that uses your GitHub account for source control. In this latter instance, Community Cloud will update the email on your Community Cloud account to match the email on your GitHub account.
</Important>

## Sign in with Email

1. Click "**Continue to sign-in**."
1. In the "Email" field, enter your email address.
1. Click "**Continue**." (If prompted, verify you are human.)
1. Go to your email inbox, and copy your one-time, six-digit code. The code is valid for ten minutes.
1. Return to the authentication page, and enter your code. (If prompted, verify you are human.)

If your account is already linked to GitHub, you may be immediately prompted to sign in with GitHub.

## Sign out of your account

From your workspace, click on your workspace name in the upper-left corner. Click "**Sign out**."

<div>{{ maxWidth: '80%', margin: 'auto' }}&gt;
<Image alt="Sign out of Streamlit Community Cloud" src="/images/streamlit-community-cloud/account-sign-out.png"/>
</div>

---

# Workspace settings

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/workspace-settings


From your workspace settings you can [Manage your account](/deploy/streamlit-community-cloud/manage-your-account), see your [App resources and limits](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits) and access support resources.

## Access your workspace settings

1. Sign in to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. In the upper-left corner, click on your workspace name.
1. In the drop-down menu, click "**Settings**."

   ![Access your workspace settings from your workspace](/images/streamlit-community-cloud/account-settings-header.png)

## Linked accounts

The "**Linked accounts**" section shows your current email identity and source control account. To learn more, see [Manage your account](/deploy/streamlit-community-cloud/manage-your-account).

![Manage your linked accounts in workspace settings](/images/streamlit-community-cloud/workspace-settings-linked-accounts.png)

## Limits

The "**Limits**" section shows your current resources and limits. To learn more, see [App resources and limits](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits).

![Resource limits displayed in workspace settings](/images/streamlit-community-cloud/workspace-settings-limits.png)

## Support

The "**Support**" section provides a convenient list of useful resources so you know where to go for help.

![Support options available through workspace settings](/images/streamlit-community-cloud/workspace-settings-support.png)

---

# Manage your GitHub connection

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/manage-your-github-connection


If you have created an account but not yet connected GitHub, see [Connect your GitHub account](/deploy/streamlit-community-cloud/get-started/connect-your-github-account).

If you have already connected your GitHub account but still need to allow Streamlit Community Cloud to access private repositories, see [Optional: Add access to private repositories](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#optional-add-access-to-private-repositories).

## Add access to an organization

If you are in an organization, you can grant or request access to that organization when you connect your GitHub account. For more information, see [Organization access](/deploy/streamlit-community-cloud/get-started/connect-your-github-account#organization-access).

If your GitHub account is already connected, you can remove permissions in your GitHub settings and force Streamlit to reprompt for GitHub authorization the next time you sign in to Community Cloud.

### Revoke and reauthorize

1. From your workspace, click on your workspace name in the upper-right corner. To sign out of Community Cloud, click "**Sign out**."

   ![Sign out of Streamlit Community Cloud](/images/streamlit-community-cloud/account-sign-out.png)

1. Go to your GitHub application settings at <a href="https://github.com/settings/applications" target="_blank">github.com/settings/applications</a>.
1. Find the "Streamlit" application, and click on the three dots (<i>{{ verticalAlign: "-.25em" }} className={{ class: "material-icons-sharp" }}&gt;more_horiz</i>

---

# Update your email

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/update-your-email


To update your email on Streamlit Community Cloud, you have two options: You can create a new account and merge your existing account into it, or you can use your GitHub account to update your email.

## Option 1: Create a new account and merge it

Two Community Cloud accounts can't have the same GitHub account for source control. When you connect a GitHub account to a new Community Cloud account for source control, Community Cloud will automatically merge any existing account with the same source control.

Therefore, you can create a new account with the desired email and connect the same GitHub account to merge them together.

1. Create a new account with your new email.
1. Connect your GitHub account.

Your old and new accounts are now merged, and you have effectively changed your email address.

## Option 2: Use your GitHub account

Alternatively, you can change the email on your GitHub account and then sign in to Community Cloud with GitHub.

1. Go to GitHub, and set your primary email address to your new email.
1. If you are currently signed in to Community Cloud, sign out.
1. Sign in to Community Cloud _using GitHub_.

   If you are redirected to your workspace and you see your existing apps, you're done! Your email has been changed. To confirm your current email and GitHub account, click on your workspace name in the upper-left corner, and look at the bottom of the drop-down menu.

   If you are redirected to an empty workspace and you see "**Workspaces <i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

# Delete your account

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-account/delete-your-account


Deleting your Streamlit Community Cloud account is just as easy as creating it. When you delete your account, your information, account, and all your hosted apps are deleted as well. Read more about data deletion in [Streamlit trust and security](/deploy/streamlit-community-cloud/get-started/trust-and-security#data-deletion).

<Warning>

Deleting your account is permanent and cannot be undone. Make sure you really want to delete your account and all hosted apps before proceeding. Any app you've deployed will be deleted, regardless of the workspace it was deployed from.

</Warning>

## How to delete your account

Follow these steps to delete your account:

1. Sign in to Streamlit Community Cloud at <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a> and access your [Workspace settings](/deploy/streamlit-community-cloud/manage-your-account/workspace-settings).

   ![Delete your Streamlit Community Cloud account from your workspace settings](/images/streamlit-community-cloud/workspace-settings-linked-accounts.png)

1. From the "**Linked accounts**" section, click "**Delete account**."
1. In the confirmation dialog, follow the prompt and click "**Delete account forever**."

   All your information and apps will be permanently deleted.

   ![Your Streamlit Community Cloud account has been deleted.](/images/streamlit-community-cloud/account-deleted.png)

It's that simple! If you have any questions or run into issues deleting your account, please reach out to us on <a href="https://discuss.streamlit.io/c/community-cloud/13" target="_blank">our forum</a>. We're happy to help! 🎈

---

# Status and limitations of Community Cloud

Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/status


## Community Cloud Status

You can view the current status of Community Cloud at [streamlitstatus.com](https://www.streamlitstatus.com/).

## GitHub OAuth scope

To deploy your app, Streamlit requires access to your app's source code in GitHub and the ability to manage the public keys associated with your repositories. The default GitHub OAuth scopes are sufficient to work with apps in public GitHub repositories. However, to access your private repositories, we create a read-only [GitHub Deploy Key](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys) and then access your repo using an SSH key. When we create this key, GitHub notifies repo admins of the creation as a security measure.

Streamlit requires the additional `repo` OAuth scope from GitHub to work with your private repos and manage deploy keys. We recognize that the `repo` scope provides Streamlit with extra permissions that we do not really need and which, as people who prize security, we'd rather not even be granted. This was the permission model available from GitHub when Community Cloud was created. However, we are working on adopting the new GitHub permission model to reduce uneeded permissions.

### Developer permissions

Because of the OAuth limitations noted above, a developer must have administrative permissions to a repository to deploy apps from it.

## Repository file structure

You can deploy multiple apps from your repository, and your entrypoint file(s) may be anywhere in your directory structure. However, Community Cloud initializes all apps from the root of your repository, even if the entrypoint file is in a subdirectory. This has the following consequences:

- Community Cloud only recognizes one `.streamlit/configuration.toml` file at the root (of each branch) of your repository.
- You must declare image, video, and audio file paths for Streamlit commands relative to the root of your repository. For example, `st.image`, `st.logo`, and the `page_icon` parameter in `st.set_page_config` expect file locations relative to your working directory (i.e. where you execute `streamlit run`).

## Linux environments

Community Cloud is built on Debian Linux.

- Community Cloud uses Debian 11 ("bullseye"). To browse available packages that can be installed, see the [package list](https://packages.debian.org/bullseye/).
- All file paths must use forward-slash path separators.

## Python environments

- You cannot mix and match Python package managers for a single app. Community Cloud configures your app's Python environment based on the first environment configuration file it finds. For more information, see [Other Python package managers](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#other-python-package-managers).
- We recommend that you use the latest version of Streamlit to ensure full Community Cloud functionality. Be sure to take note of Streamlit's [current requirements](https://github.com/streamlit/streamlit/blob/develop/lib/setup.py) for package compatibility when planning your environment, especially `protobuf&gt;=3.20,

---

# Deploy Streamlit apps in Snowflake

Source: https://docs.streamlit.io/deploy/snowflake


Host your apps alongside your data in a single, global platform. Snowflake provides industry-leading features that ensure the highest levels of security for your account, users, data, and apps. If you're looking for an enterprise hosting solution, try Snowflake!

<TileContainer>
<Tile background="lightBlue-70" icon="rocket_launch" link="/get-started/installation/streamlit-in-snowflake" text="Create a free trial account and deploy an app with Streamlit in Snowflake." title="Streamlit in Snowflake Quickstart"/>
<Tile background="lightBlue-70" icon="code" link="https://github.com/Snowflake-Labs/snowflake-demo-streamlit" text="Explore a wide variety of example apps in Snowflake Labs' snowflake-demo-streamlit repository." title="Examples"/>
<Tile background="lightBlue-70" icon="book" link="https://docs.snowflake.com/user-guide-getting-started" text="Learn more in Snowflake's documentation." title="Get started with Snowflake"/>
</TileContainer>

There are three ways to host Streamlit apps in Snowflake:

<InlineCalloutContainer>
<InlineCallout bold="Streamlit in Snowflake." color="lightBlue-70" href="https://docs.snowflake.com/developer-guide/streamlit/about-streamlit" icon="bolt">Run your Streamlit app as a native object in Snowflake. Enjoy an in-browser editor and minimal work to configure your environment. Share your app with other users in your Snowflake account through role-based access control (RBAC). This is a great way to deploy apps internally for your business. Check out Snowflake docs!</InlineCallout>
<InlineCallout bold="Snowflake Native Apps." color="lightBlue-70" href="https://docs.snowflake.com/en/developer-guide/native-apps/adding-streamlit" icon="ac_unit">Package your app with data and share it with other Snowflake accounts. This is a great way to share apps and their underlying data with other organizations who use Snowflake. Check out Snowflake docs!</InlineCallout>
<InlineCallout bold="Snowpark Container Services." color="lightBlue-70" href="https://docs.snowflake.com/en/developer-guide/snowpark-container-services/overview" icon="web_asset">Deploy your app in a container that's optimized to run in Snowflake. This is the most flexible option, where you can use any library and assign a public URL to your app. Manage your allowed viewers through your Snowflake account. Check out Snowflake docs!</InlineCallout>
</InlineCalloutContainer>
<Note>

    Using Snowpark Container Services to deploy a Streamlit app requires a compute pool, which is not available in a trial account at this time.

</Note>

---

# Deployment tutorials

Source: https://docs.streamlit.io/deploy/tutorials


This sections contains step-by-step guides on how to deploy Streamlit apps to various cloud platforms and services. We have deployment guides for:

<DataSourcesContainer>
<DataSourcesCard href="/deploy/streamlit-community-cloud/get-started">
<Image>alt="screenshot" src="/images/deploy/streamlit-cloud.png" /&gt;

<h5 align="center">Streamlit Community Cloud</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/deploy/tutorials/docker">
<Image>alt="screenshot" src="/images/deploy/docker.png" /&gt;

<h5 align="center">Docker</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/deploy/tutorials/kubernetes">
<Image>alt="screenshot" src="/images/deploy/kubernetes.png" /&gt;

<h5 align="center">Kubernetes</h5>
</Image></DataSourcesCard>
</DataSourcesContainer>

While we work on official Streamlit deployment guides for other hosting providers, here are some user-submitted tutorials for different cloud services:

- [How to deploy Streamlit apps to **Google App Engine**](https://dev.to/whitphx/how-to-deploy-streamlit-apps-to-google-app-engine-407o), by [Yuichiro Tachibana (Tsuchiya)](https://discuss.streamlit.io/u/whitphx/summary).
- [Host Streamlit on **Heroku**](https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83), by Maarten Grootendorst.
- [Deploy Streamlit on **Ploomber Cloud**](https://docs.cloud.ploomber.io/en/latest/apps/streamlit.html), by Ido Michael.
- [Host Streamlit on **21YunBox**](https://www.21yunbox.com/docs/#/deploy-streamlit), by Toby Lei.
- [Deploy a Streamlit App on **Koyeb**](https://www.koyeb.com/docs/deploy/streamlit), by Justin Ellingwood.
- [Community-supported deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099).

---

# Deploy Streamlit using Docker

Source: https://docs.streamlit.io/deploy/tutorials/docker


## Introduction

So you have an amazing app and you want to start sharing it with other people, what do you do? You have a few options. First, where do you want to run your Streamlit app, and how do you want to access it?

- **On your corporate network** - Most corporate networks are closed to the outside world. You typically use a VPN to log onto your corporate network and access resources there. You could run your Streamlit app on a server in your corporate network for security reasons, to ensure that only folks internal to your company can access it.
- **On the cloud** - If you'd like to access your Streamlit app from outside of a corporate network, or share your app with folks outside of your home network or laptop, you might choose this option. In this case, it'll depend on your hosting provider. We have [community-submitted guides](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) from Heroku, AWS, and other providers.

Wherever you decide to deploy your app, you will first need to containerize it. This guide walks you through using Docker to deploy your app. If you prefer Kubernetes see [Deploy Streamlit using Kubernetes](/deploy/tutorials/kubernetes).

## Prerequisites

1. [Install Docker Engine](#install-docker-engine)
2. [Check network port accessibility](#check-network-port-accessibility)

### Install Docker Engine

If you haven't already done so, install [Docker](https://docs.docker.com/engine/install/#server) on your server. Docker provides `.deb` and `.rpm` packages from many Linux distributions, including:

- [Debian](https://docs.docker.com/engine/install/debian/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verify that Docker Engine is installed correctly by running the `hello-world` Docker image:

```bash
sudo docker run hello-world
```

<Tip>

Follow Docker's official [post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker as a non-root user, so that you don't have to preface the `docker` command with `sudo`.

</Tip>

### Check network port accessibility

As you and your users are behind your corporate VPN, you need to make sure all of you can access a certain network port. Let's say port `8501`, as it is the default port used by Streamlit. Contact your IT team and request access to port `8501` for you and your users.

## Create a Dockerfile

Docker builds images by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Learn more in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/). The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile`. The [docker run](https://docs.docker.com/engine/reference/commandline/run/) command first creates a container over the specified image, and then starts it using the specified command.

Here's an example `Dockerfile` that you can add to the root of your directory. i.e. in `/app/`

```docker
# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update  apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
     rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Dockerfile walkthrough

Let’s walk through each line of the Dockerfile :

1. A `Dockerfile` must start with a [`FROM`](https://docs.docker.com/engine/reference/builder/#from) instruction. It sets the [Base Image](https://docs.docker.com/glossary/#base-image) (think OS) for the container:

   ```docker
   FROM python:3.9-slim
   ```

   Docker has a number of official Docker base images based on various Linux distributions. They also have base images that come with language-specific modules such as [Python](https://hub.docker.com/_/python). The `python` images come in many flavors, each designed for a specific use case. Here, we use the `python:3.9-slim` image which is a lightweight image that comes with the latest version of Python 3.9.

   <Tip>

   You can also use your own base image, provided the image you use contains a [supported version of Python](/knowledge-base/using-streamlit/sanity-checks#check-0-are-you-using-a-streamlit-supported-version-of-python) for Streamlit. There is no one-size-fits-all approach to using any specific base image, nor is there an official Streamlit-specific base image.

   </Tip>

2. The `WORKDIR` instruction sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the `Dockerfile` . Let’s set it to `app/` :

   ```docker
   WORKDIR /app
   ```

   <Important>

   As mentioned in [Development flow](/get-started/fundamentals/main-concepts#development-flow), for Streamlit version 1.10.0 and higher, Streamlit apps cannot be run from the root directory of Linux distributions. Your main script should live in a directory other than the root directory. If you try to run a Streamlit app from the root directory, Streamlit will throw a `FileNotFoundError: [Errno 2] No such file or directory` error. For more information, see GitHub issue [#5239](https://github.com/streamlit/streamlit/issues/5239).

   If you are using Streamlit version 1.10.0 or higher, you must set the `WORKDIR` to a directory other than the root directory. For example, you can set the `WORKDIR` to `/app` as shown in the example `Dockerfile` above.
   </Important>

3. Install `git` so that we can clone the app code from a remote repo:

   ```docker
   RUN apt-get update  apt-get install -y \
       build-essential \
       curl \
       software-properties-common \
       git \
        rm -rf /var/lib/apt/lists/*
   ```

4. Clone your code that lives in a remote repo to `WORKDIR`:

   a. If your code is in a public repo:

   ```docker
   RUN git clone https://github.com/streamlit/streamlit-example.git .
   ```

   Once cloned, the directory of `WORKDIR` will look like the following:

   ```bash
   app/
   - requirements.txt
   - streamlit_app.py
   ```

   where `requirements.txt` file contains all your [Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies). E.g

   ```
   altair
   pandas
   streamlit
   ```

   and `streamlit_app.py` is your main script. E.g.

   ```python
   from collections import namedtuple
   import altair as alt
   import math
   import pandas as pd
   import streamlit as st

   """
   # Welcome to Streamlit!

   Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

   If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
   forums](https://discuss.streamlit.io).

   In the meantime, below is an example of what you can do with just a few lines of code:
   """

   with st.echo(code_location='below'):
      total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
      num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

      Point = namedtuple('Point', 'x y')
      data = []

      points_per_turn = total_points / num_turns

      for curr_point_num in range(total_points):
         curr_turn, i = divmod(curr_point_num, points_per_turn)
         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
         radius = curr_point_num / total_points
         x = radius * math.cos(angle)
         y = radius * math.sin(angle)
         data.append(Point(x, y))

      st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
         .mark_circle(color='#0068c9', opacity=0.5)
         .encode(x='x:Q', y='y:Q'))
   ```

   b. If your code is in a private repo, please read [Using SSH to access private data in builds](https://docs.docker.com/develop/develop-images/build_enhancements/#using-ssh-to-access-private-data-in-builds) and modify the Dockerfile accordingly -- to install an SSH client, download the public key for [github.com](https://github.com), and clone your private repo. If you use an alternative VCS such as GitLab or Bitbucket, please consult the documentation for that VCS on how to copy your code to the `WORKDIR` of the Dockerfile.

   c. If your code lives in the same directory as the Dockerfile, copy all your app files from your server into the container, including `streamlit_app.py`, `requirements.txt`, etc, by replacing the `git clone` line with:

   ```docker
   COPY . .
   ```

   More generally, the idea is copy your app code from wherever it may live on your server into the container. If the code is not in the same directory as the Dockerfile, modify the above command to include the path to the code.

5. Install your app’s [Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) from the cloned `requirements.txt` in the container:

   ```docker
   RUN pip3 install -r requirements.txt
   ```

6. The [`EXPOSE`](https://docs.docker.com/engine/reference/builder/#expose) instruction informs Docker that the container listens on the specified network ports at runtime. Your container needs to listen to Streamlit’s (default) port 8501:

   ```docker
   EXPOSE 8501
   ```

7. The [`HEALTHCHECK`](https://docs.docker.com/engine/reference/builder/#expose) instruction tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501:

   ```docker
   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
   ```

8. An [`ENTRYPOINT`](https://docs.docker.com/engine/reference/builder/#entrypoint) allows you to configure a container that will run as an executable. Here, it also contains the entire `streamlit run` command for your app, so you don’t have to call it from the command line:

   ```docker
   ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

## Build a Docker image

The [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile` . Run the following command from the `app/` directory on your server to build the image:

```docker
docker build -t streamlit .
```

The `-t` flag is used to tag the image. Here, we have tagged the image `streamlit`. If you run:

```docker
docker images
```

You should see a `streamlit` image under the REPOSITORY column. For example:

```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
streamlit    latest    70b0759a094d   About a minute ago   1.02GB
```

## Run the Docker container

Now that you have built the image, you can run the container by executing:

```docker
docker run -p 8501:8501 streamlit
```

The `-p` flag publishes the container’s port 8501 to your server’s 8501 port.

If all went well, you should see an output similar to the following:

```
docker run -p 8501:8501 streamlit

  You can now view your Streamlit app in your browser.

  URL: http://0.0.0.0:8501
```

To view your app, users can browse to `http://0.0.0.0:8501` or `http://localhost:8501`

<Note>

Based on your server's network configuration, you could map to port 80/443 so that users can view your app using the server IP or hostname. For example: `http://your-server-ip:80` or `http://your-hostname:443`.

</Note>

---

# Deploy Streamlit using Kubernetes

Source: https://docs.streamlit.io/deploy/tutorials/kubernetes


## Introduction

So you have an amazing app and you want to start sharing it with other people, what do you do? You have a few options. First, where do you want to run your Streamlit app, and how do you want to access it?

- **On your corporate network** - Most corporate networks are closed to the outside world. You typically use a VPN to log onto your corporate network and access resources there. You could run your Streamlit app on a server in your corporate network for security reasons, to ensure that only folks internal to your company can access it.
- **On the cloud** - If you'd like to access your Streamlit app from outside of a corporate network, or share your app with folks outside of your home network or laptop, you might choose this option. In this case, it'll depend on your hosting provider. We have [community-submitted guides](/knowledge-base/deploy/deploy-streamlit-heroku-aws-google-cloud) from Heroku, AWS, and other providers.

Wherever you decide to deploy your app, you will first need to containerize it. This guide walks you through using Kubernetes to deploy your app. If you prefer Docker see [Deploy Streamlit using Docker](/deploy/tutorials/docker).

## Prerequisites

1. [Install Docker Engine](#install-docker-engine)
2. [Install the gcloud CLI](#install-the-gcloud-cli)

### Install Docker Engine

If you haven't already done so, install [Docker](https://docs.docker.com/engine/install/#server) on your server. Docker provides `.deb` and `.rpm` packages from many Linux distributions, including:

- [Debian](https://docs.docker.com/engine/install/debian/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

Verify that Docker Engine is installed correctly by running the `hello-world` Docker image:

```bash
sudo docker run hello-world
```

<Tip>

Follow Docker's official [post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/) to run Docker as a non-root user, so that you don't have to preface the `docker` command with `sudo`.

</Tip>

### Install the gcloud CLI

In this guide, we will orchestrate Docker containers with Kubernetes and host docker images on the Google Container Registry (GCR). As GCR is a Google-supported Docker registry, we need to register [`gcloud`](https://cloud.google.com/sdk/gcloud/reference) as the Docker credential helper.

Follow the official documentation to [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install) and initialize it.

## Create a Docker container

We need to create a docker container which contains all the dependencies and the application code. Below you can see the entrypoint, i.e. the command run when the container starts, and the Dockerfile definition.

### Create an entrypoint script

Create a `run.sh` script containing the following:

```bash
#!/bin/bash

APP_PID=
stopRunningProcess() {
    # Based on https://linuxconfig.org/how-to-propagate-a-signal-to-child-processes-from-a-bash-script
    if test ! "${APP_PID}" = ''  ps -p ${APP_PID} &gt; /dev/null ; then
       &gt; /proc/1/fd/1 echo "Stopping ${COMMAND_PATH} which is running with process ID ${APP_PID}"

       kill -TERM ${APP_PID}
       &gt; /proc/1/fd/1 echo "Waiting for ${COMMAND_PATH} to process SIGTERM signal"

        wait ${APP_PID}
        &gt; /proc/1/fd/1 echo "All processes have stopped running"
    else
        &gt; /proc/1/fd/1 echo "${COMMAND_PATH} was not started when the signal was sent or it has already been stopped"
    fi
}

trap stopRunningProcess EXIT TERM

source ${VIRTUAL_ENV}/bin/activate

streamlit run ${HOME}/app/streamlit_app.py 
APP_ID=${!}

wait ${APP_ID}
```

### Create a Dockerfile

Docker builds images by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Learn more in the [Dockerfile reference](https://docs.docker.com/engine/reference/builder/). The [docker build](https://docs.docker.com/engine/reference/commandline/build/) command builds an image from a `Dockerfile`. The [docker run](https://docs.docker.com/engine/reference/commandline/run/) command first creates a container over the specified image, and then starts it using the specified command.

Here's an example `Dockerfile` that you can add to the root of your directory.

```docker
FROM python:3.9-slim

RUN groupadd --gid 1000 appuser \
     useradd --uid 1000 --gid 1000 -ms /bin/bash appuser

RUN pip3 install --no-cache-dir --upgrade \
    pip \
    virtualenv

RUN apt-get update  apt-get install -y \
    build-essential \
    software-properties-common \
    git

USER appuser
WORKDIR /home/appuser

RUN git clone https://github.com/streamlit/streamlit-example.git app

ENV VIRTUAL_ENV=/home/appuser/venv
RUN virtualenv ${VIRTUAL_ENV}
RUN . ${VIRTUAL_ENV}/bin/activate  pip install -r app/requirements.txt

EXPOSE 8501

COPY run.sh /home/appuser
ENTRYPOINT ["./run.sh"]
```

<Important>

As mentioned in [Development flow](/get-started/fundamentals/main-concepts#development-flow), for Streamlit version 1.10.0 and higher, Streamlit apps cannot be run from the root directory of Linux distributions. Your main script should live in a directory other than the root directory. If you try to run a Streamlit app from the root directory, Streamlit will throw a `FileNotFoundError: [Errno 2] No such file or directory` error. For more information, see GitHub issue [#5239](https://github.com/streamlit/streamlit/issues/5239).

If you are using Streamlit version 1.10.0 or higher, you must set the `WORKDIR` to a directory other than the root directory. For example, you can set the `WORKDIR` to `/home/appuser` as shown in the example `Dockerfile` above.
</Important>

### Build a Docker image

Put the above files (`run.sh` and `Dockerfile`) in the same folder and build the docker image:

```docker
docker build --platform linux/amd64 -t gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test .
```

<Important>

Replace `<GCP_PROJECT_ID>` in the above command with the name of your Google Cloud project.

</GCP_PROJECT_ID>

### Upload the Docker image to a container registry

The next step is to upload the Docker image to a container registry. In this example, we will use the [Google Container Registry (GCR)](https://cloud.google.com/container-registry). Start by enabling the Container Registry API. Sign in to Google Cloud and navigate to your project’s **Container Registry** and click **Enable**.

We can now build the Docker image from the previous step and push it to our project’s GCR. Be sure to replace `<GCP_PROJECT_ID>` in the docker push command with the name of your project:

```bash
gcloud auth configure-docker
docker push gcr.io/<GCP_PROJECT_ID>/k8s-streamlit:test
```

## Create a Kubernetes deployment

For this step you will need a:

- Running Kubernetes service
- Custom domain for which you can generate a TLS certificate
- DNS service where you can configure your custom domain to point to the application IP

As the image was uploaded to the container registry in the previous step, we can run it in Kubernetes using the below configurations.

### Install and run Kubernetes

Make sure your [Kubernetes client](https://kubernetes.io/docs/tasks/tools/#kubectl), `kubectl`, is installed and running on your machine.

### Configure a Google OAuth Client and OAuth2-Proxy

For configuring the Google OAuth Client, please see [Google Auth Provider](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider#google-auth-provider). Configure OAuth2-Proxy to use the desired [OAuth Provider Configuration](https://oauth2-proxy.github.io/oauth2-proxy/docs/configuration/oauth_provider) and update the OAuth2-Proxy config in the config map.

The below configuration contains an OAuth2-Proxy sidecar container which handles the authentication with Google. You can learn more from the [`oauth2-proxy` repository](https://github.com/oauth2-proxy/oauth2-proxy).

### Create a Kubernetes configuration file

Create a [YAML](https://yaml.org/) [configuration file](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations) named `k8s-streamlit.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: streamlit-configmap
data:
  oauth2-proxy.cfg: |-
    http_address = "0.0.0.0:4180"
    upstreams = ["http://127.0.0.1:8501/"]
    email_domains = ["*"]
    client_id = "<GOOGLE_CLIENT_ID>"
    client_secret = "<GOOGLE_CLIENT_SECRET>"
    cookie_secret = "</GOOGLE_CLIENT_SECRET></GOOGLE_CLIENT_ID></GCP_PROJECT_ID></GCP_PROJECT_ID></Important></GCP_PROJECT_ID>

---

# Knowledge base

Source: https://docs.streamlit.io/knowledge-base


The knowledge base is a self-serve library of tips, step-by-step tutorials, and articles that answer your questions about creating and deploying Streamlit apps.

<InlineCalloutContainer>
<InlineCallout bold="FAQ" color="darkBlue-70" href="/knowledge-base/using-streamlit" icon="quiz">Here are some frequently asked questions about using Streamlit.</InlineCallout>
<InlineCallout bold="Installing dependencies." color="darkBlue-70" href="/knowledge-base/dependencies" icon="downloading">If you run into problems installing dependencies for your Streamlit apps, we've got you covered.</InlineCallout>
<InlineCallout bold="Deployment issues." color="darkBlue-70" href="/knowledge-base/deploy" icon="report">Have questions about deploying Streamlit apps to the cloud? This section covers deployment-related issues.</InlineCallout>
</InlineCalloutContainer>

---

# FAQ

Source: https://docs.streamlit.io/knowledge-base/using-streamlit


Here are some frequently asked questions about using Streamlit. If you feel something important is missing that everyone needs to know, please [open an issue](https://github.com/streamlit/docs/issues) or [submit a pull request](https://github.com/streamlit/docs/pulls) and we'll be happy to review it!

- [Sanity checks](/knowledge-base/using-streamlit/sanity-checks)
- [How can I make Streamlit watch for changes in other modules I'm importing in my app?](/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app)
- [What browsers does Streamlit support?](/knowledge-base/using-streamlit/supported-browsers)
- [Where does st.file_uploader store uploaded files and when do they get deleted?](/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted)
- [How do you retrieve the filename of a file uploaded with st.file_uploader?](/knowledge-base/using-streamlit/retrieve-filename-uploaded)
- [How to remove "· Streamlit" from the app title?](/knowledge-base/using-streamlit/remove-streamlit-app-title)
- [How to download a file in Streamlit?](/knowledge-base/using-streamlit/how-download-file-streamlit)
- [How to download a Pandas DataFrame as a CSV?](/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv)
- [How can I make `st.pydeck_chart` use custom Mapbox styles?](/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles)
- [How to insert elements out of order?](/knowledge-base/using-streamlit/insert-elements-out-of-order)
- [How do I upgrade to the latest version of Streamlit?](/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit)
- [Widget updating for every second input when using session state](/knowledge-base/using-streamlit/widget-updating-session-state)
- [How do I create an anchor link?](/knowledge-base/using-streamlit/create-anchor-link)
- [How do I enable camera access?](/knowledge-base/using-streamlit/enable-camera)
- [Why does Streamlit restrict nested `st.columns`?](/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns)
- [What is serializable session state?](/knowledge-base/using-streamlit/serializable-session-state)

---

# How do I create an anchor link?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/create-anchor-link


## Overview

Have you wanted to create anchors so that users of your app can directly navigate to specific sections by specifying `#anchor` in the URL? If so, let's find out how.

## Solution

Anchors are automatically added to header text.

For example, if you define a header text via the [st.header()](/develop/api-reference/text/st.header) command as follows:

```python
st.header("Section 1")
```

Then you can create a link to this header using:

```python
st.markdown("[Section 1](#section-1)")
```

## Examples

- Demo app: [https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/](https://dataprofessor-streamlit-anchor-app-80kk8w.streamlit.app/)
- GitHub repo: [https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py](https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py)

---

# Enabling camera or microphone access in your browser

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/enable-camera


Streamlit apps may include a widget to upload images from your camera or record sound with your microphone. To
safeguard the users' privacy and security, browsers require users to explicitly allow access to their
camera or microphone before those devices can be used.

To learn how to enable camera access, please check the documentation for your browser:

- [Chrome](https://support.google.com/chrome/answer/2693767)
- [Safari](https://support.apple.com/guide/safari/websites-ibrwe2159f50/mac)
- [Firefox](https://support.mozilla.org/en-US/kb/how-manage-your-camera-and-microphone-permissions)

---

# How to download a file in Streamlit?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-file-streamlit


Use the [`st.download_button`](/develop/api-reference/widgets/st.download_button) widget that is natively built into Streamlit. Check out a [sample app](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/) demonstrating how you can use `st.download_button` to download common file formats.

## Example usage

```python
import streamlit as st

# Text files

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API

st.download_button('Download CSV', text_contents, 'text/csv')
st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'

with open('myfile.csv') as f:
   st.download_button('Download CSV', f)  # Defaults to 'text/plain'

# ---
# Binary files

binary_contents = b'whatever'

# Different ways to use the API

st.download_button('Download file', binary_contents)  # Defaults to 'application/octet-stream'

with open('myfile.zip', 'rb') as f:
   st.download_button('Download Zip', f, file_name='archive.zip')  # Defaults to 'application/octet-stream'

# You can also grab the return value of the button,
# just like with any other button.

if st.download_button(...):
   st.write('Thanks for downloading!')
```

Additional resources:

- [https://blog.streamlit.io/0-88-0-release-notes/](https://blog.streamlit.io/0-88-0-release-notes/)
- [https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/)
- [https://docs.streamlit.io/develop/api-reference/widgets/st.download_button](/develop/api-reference/widgets/st.download_button)

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
```

Additional resources:

- [https://blog.streamlit.io/0-88-0-release-notes/](https://blog.streamlit.io/0-88-0-release-notes/)
- [https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/](https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/)
- [https://docs.streamlit.io/develop/api-reference/widgets/st.download_button](/develop/api-reference/widgets/st.download_button)

---

# How do I upgrade to the latest version of Streamlit?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/how-upgrade-latest-version-streamlit


We recommend upgrading to the latest official release of Streamlit so you have access to the newest, cutting-edge features. If you haven't installed Streamlit yet, please read our [Installation guide](/get-started/installation). It helps you set up your virtual environment and walks you through installing Streamlit on Windows, macOS, and Linux. Regardless of which package management tool and OS you're using, we recommend running the commands on this page in a virtual environment.

If you've previously installed Streamlit and want to upgrade to the latest version, here's how to do it based on your dependency manager.

## Pipenv

Streamlit's officially-supported environment manager for macOS and Linux is [Pipenv](https://pypi.org/project/pipenv/).

1. Navigate to the project folder containing your Pipenv environment:

```bash
cd myproject
```

2. Activate that environment, upgrade Streamlit, and verify you have the latest version:

```bash
pipenv shell
pip install --upgrade streamlit
streamlit version
```

Or if you want to use an easily-reproducible environment, replace `pip` with `pipenv`every time you install or update a package:

```bash
pipenv update streamlit
pipenv run streamlit version
```

## Conda

1. Activate the conda environment where Streamlit is installed:

```bash
conda activate $ENVIRONMENT_NAME
```

Be sure to replace`$ENVIRONMENT_NAME` ☝️ with the name your conda environment!

2. Update Streamlit within the active conda environment and verify you have the latest version:

```bash
conda update -c conda-forge streamlit -y
streamlit version
```

## Poetry

In order to get the latest version of Streamlit with [Poetry](https://python-poetry.org/) and verify you have the latest version, run:

```bash
poetry update streamlit
streamlit version
```

---

# How to insert elements out of order?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/insert-elements-out-of-order


You can use the [`st.empty`](/develop/api-reference/layout/st.empty) method as a placeholder,
to "save" a slot in your app that you can use later.

```python
st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.
```

---

# How can I make st.pydeck_chart use custom Mapbox styles?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/pydeck-chart-custom-mapbox-styles


If you are supplying a Mapbox token, but the resulting `pydeck_chart` doesn't show your custom Mapbox styles, please check that you are adding the Mapbox token to the Streamlit `config.toml` configuration file. Streamlit DOES NOT read Mapbox tokens from inside of a PyDeck specification (i.e. from inside of the Streamlit app). Please see this [forum thread](https://discuss.streamlit.io/t/deprecation-warning-deckgl-pydeck-maps-to-require-mapbox-token-for-production-usage/2982/10) for more information.

---

# How to remove "· Streamlit" from the app title?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/remove-streamlit-app-title


Using [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config) to assign the page title will not append "· Streamlit" to that title. E.g.:

```python
import streamlit as st

st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
```

---

# How do you retrieve the filename of a file uploaded with st.file_uploader?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/retrieve-filename-uploaded


If you upload a single file (i.e. `accept_multiple_files=False`), the filename can be retrieved by using the `.name` attribute on the returned UploadedFile object:

```python
import streamlit as st

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)
```

If you upload multiple files (i.e. `accept_multiple_files=True`), the individual filenames can be retrieved by using the `.name` attribute on each UploadedFile object in the returned list:

```python
import streamlit as st

uploaded_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)

if uploaded_files:
   for uploaded_file in uploaded_files:
       st.write("Filename: ", uploaded_file.name)
```

Related forum posts:

- https://discuss.streamlit.io/t/is-it-possible-to-get-uploaded-file-file-name/7586

---

# Sanity checks

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/sanity-checks


If you're having problems running your Streamlit app, here are a few things to try out.

## Check #0: Are you using a Streamlit-supported version of Python?

Streamlit will maintain backwards-compatibility with earlier Python versions as practical,
guaranteeing compatibility with _at least_ the last three minor versions of Python 3.

As new versions of Python are released, we will try to be compatible with the new version as soon
as possible, though frequently we are at the mercy of other Python packages to support these new versions as well.

Streamlit currently supports versions 3.9, 3.10, 3.11, 3.12, and 3.13 of Python.

## Check #1: Is Streamlit running?

On a Mac or Linux machine, type this on the terminal:

```bash
ps -Al | grep streamlit
```

If you don't see `streamlit run` in the output (or `streamlit hello`, if that's
the command you ran) then the Streamlit server is not running. So re-run your command and see if the bug goes away.

## Check #2: Is this an already-fixed Streamlit bug?

We try to fix bugs quickly, so many times a problem will go away when you
upgrade Streamlit. So the first thing to try when having an issue is upgrading
to the latest version of Streamlit:

```bash
pip install --upgrade streamlit
streamlit version
```

...and then verify that the version number printed corresponds to the version number displayed on [PyPI](https://pypi.org/project/streamlit/).

**Try reproducing the issue now.** If not fixed, keep reading on.

## Check #3: Are you running the correct Streamlit binary?

Let's check whether your Python environment is set up correctly. Edit the
Streamlit script where you're experiencing your issue, **comment everything
out, and add these lines instead:**

```python
import streamlit as st
st.write(st.__version__)
```

...then call `streamlit run` on your script and make sure it says the same
version as above. If not the same version, check out [these
instructions](/get-started/installation) for some sure-fire ways to set up your
environment.

## Check #4: Is your browser caching your app too aggressively?

There are two easy ways to check this:

1. Load your app in a browser then press `Ctrl-Shift-R` or `⌘-Shift-R` to do a
   hard refresh (Chrome/Firefox).

2. As a test, run Streamlit on another port. This way the browser starts the
   page with a brand new cache. For that, pass the `--server.port`
   argument to Streamlit on the command line:

   ```bash
   streamlit run my_app.py --server.port=9876
   ```

## Check #5: Is this a Streamlit regression?

If you've upgraded to the latest version of Streamlit and things aren't
working, you can downgrade at any time using this command:

```bash
pip install --upgrade streamlit==1.0.0
```

...where `1.0.0` is the version you'd like to downgrade to. See
[Release notes](/develop/quick-reference/release-notes) for a complete list of Streamlit versions.

## Check #6 [Windows]: Is Python added to your PATH?

When installed by downloading from [python.org](https://www.python.org/downloads/), Python is
not automatically added to the [Windows system PATH](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access). Because of this, you may get error messages
like the following:

Command Prompt:

```bash
C:\Users\streamlit&gt; streamlit hello
'streamlit' is not recognized as an internal or external command,
operable program or batch file.
```

PowerShell:

```bash
PS C:\Users\streamlit&gt; streamlit hello
streamlit : The term 'streamlit' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that
the path is correct and try again.
At line:1 char:1
+ streamlit hello
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (streamlit:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```

To resolve this issue, add [Python to the Windows system PATH](https://datatofish.com/add-python-to-windows-path/).

After adding Python to your Windows PATH, you should then be able to follow the instructions in our [Get Started](/get-started) section.

## Check #7 [Windows]: Do you need Build Tools for Visual Studio installed?

Streamlit includes [pyarrow](https://arrow.apache.org/docs/python/) as an install dependency. Occasionally, when trying to install Streamlit from PyPI, you may see errors such as the following:

```bash
Using cached pyarrow-1.0.1.tar.gz (1.3 MB)
  Installing build dependencies ... error
  ERROR: Command errored out with exit status 1:
   command: 'c:\users\streamlit\appdata\local\programs\python\python38-32\python.exe' 'c:\users\streamlit\appdata\local\programs\python\python38-32\lib\site-packages\pip' install --ignore-installed --no-user --prefix 'C:\Users\streamlit\AppData\Local\Temp\pip-build-env-s7owjrle\overlay' --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- 'cython &gt;= 0.29' 'numpy==1.14.5; python_version

---

# How can I make Streamlit watch for changes in other modules I'm importing in my app?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/streamlit-watch-changes-other-modules-importing-app


By default, Streamlit only watches modules contained in the current directory of the main app module. You can track other modules by adding the parent directory of each module to the `PYTHONPATH`.

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/module
streamlit run your_script.py
```

---

# What browsers does Streamlit support?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/supported-browsers


The latest version of Streamlit is compatible with the two most recent versions of the following browsers:

- [Google Chrome](https://www.google.com/chrome/browser)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Microsoft Edge](https://www.microsoft.com/windows/microsoft-edge)
- [Safari](https://www.apple.com/safari/)

<Note>

You may not be able to use all the latest features of Streamlit with unsupported browsers or older versions of the above browsers. Streamlit will not provide bug fixes for unsupported browsers.

</Note>

---

# Where does st.file_uploader store uploaded files and when do they get deleted?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/where-file-uploader-store-when-deleted


When you upload a file using [`st.file_uploader`](/develop/api-reference/widgets/st.file_uploader), the data are copied to the Streamlit backend via the browser, and contained in a BytesIO buffer in Python memory (i.e. RAM, not disk). The data will persist in RAM until the Streamlit app re-runs from top-to-bottom, which is on each widget interaction. If you need to save the data that was uploaded between runs, then you can [cache](/develop/concepts/architecture/caching) it so that Streamlit persists it across re-runs.

As files are stored in memory, they get deleted immediately as soon as they’re not needed anymore.

This means Streamlit removes a file from memory when:

- The user uploads another file, replacing the original one
- The user clears the file uploader
- The user closes the browser tab where they uploaded the file

Related forum posts:

- https://discuss.streamlit.io/t/streamlit-sharing-fileupload-where-does-it-go/9267
- https://discuss.streamlit.io/t/how-to-update-the-uploaded-file-using-file-uploader/13512/

---

# Widget updating for every second input when using session state

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/widget-updating-session-state


## Overview

You are using [session state](/develop/api-reference/caching-and-state/st.session_state) to store page interactions in your app. When users interact with a widget in your app (e.g., click a button), you expect your app to update its widget states and reflect the new values. However, you notice that it doesn't. Instead, users have to interact with the widget twice (e.g., click a button twice) for the app to show the correct values. What do you do now? 🤔 Let's walk through the solution in the section below.

## Solution

When using session state to update widgets or values in your script, you need to use the unique key you assigned to the widget, **not** the variable that you assigned your widget to. In the example code block below, the unique _key_ assigned to the slider widget is `slider`, and the _variable_ the widget is assigned to is `slide_val`.

Let's see this in an example. Say you want a user to click a button that resets a slider.

To have the slider's value update on the button click, you need to use a [callback function](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) with the `on_click` parameter of [`st.button`](/develop/api-reference/widgets/st.button):

```python
# the callback function for the button will add 1 to the
# slider value up to 10
def plus_one():
    if st.session_state["slider"] 

---

# Why does Streamlit restrict nested `st.columns`?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/why-streamlit-restrict-nested-columns


Starting in version 1.46.0, Streamlit removed explicit limits on nesting columns, expanders, popovers, and chat message containers. To follow best design practices and maintain a good appearance on all screen sizes, don't overuse nested layouts.

From version 1.18.0 to 1.45.0, Streamlit allows nesting [`st.columns`](/develop/api-reference/layout/st.columns) inside other
`st.columns` with the following restrictions:

- In the main area of the app, columns can be nested up to one level of nesting.
- In the sidebar, columns cannot be nested.

These restrictions were in place to make Streamlit apps look good on all device sizes. Nesting columns multiple times often leads to a bad UI.
You might be able to make it look good on one screen size but as soon as a user on a different screen views the app,
they will have a bad experience. Some columns will be tiny, others will be way too long, and complex layouts will look out of place.
Streamlit tries its best to automatically resize elements to look good across devices, without any help from the developer.
But for complex layouts with multiple levels of nesting, this is not possible.

---

# What is serializable session state?

Source: https://docs.streamlit.io/knowledge-base/using-streamlit/serializable-session-state


## Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the data’s original structure. Python’s built-in [pickle](https://docs.python.org/3/library/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, Streamlit’s [Session State](/develop/concepts/architecture/session-state) allows you to persist any Python object for the duration of the session, irrespective of the object’s pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](/develop/concepts/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml
# .streamlit/config.toml
[runner]
enforceSerializableSessionState = true
```

By "_pickle-serializable_", we mean calling `pickle.dumps(obj)` should not raise a [`PicklingError`](https://docs.python.org/3/library/pickle.html#pickle.PicklingError) exception. When the config option is enabled, adding unserializable data to session state should result in an exception. E.g.,

```python
import streamlit as st

def unserializable_data():
		return lambda x: x

#👇 results in an exception when enforceSerializableSessionState is on
st.session_state.unserializable = unserializable_data()
```

<Image alt="UnserializableSessionStateError" src="/images/unserializable-session-state-error.png"/>

---

# Installing dependencies

Source: https://docs.streamlit.io/knowledge-base/dependencies


- [ModuleNotFoundError: No module named](/knowledge-base/dependencies/module-not-found-error)
- [ImportError: libGL.so.1: cannot open shared object file: No such file or directory](/knowledge-base/dependencies/libgl)
- [ERROR: No matching distribution found for](/knowledge-base/dependencies/no-matching-distribution)
- [How to install a package not on PyPI/Conda but available on GitHub](/knowledge-base/dependencies/install-package-not-pypi-conda-available-github)

---

# How to install a package not on PyPI/Conda but available on GitHub

Source: https://docs.streamlit.io/knowledge-base/dependencies/install-package-not-pypi-conda-available-github


## Overview

Are you trying to deploy your app to [Streamlit Community Cloud](/deploy/streamlit-community-cloud), but don't know how to specify a [Python dependency](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) in your requirements file that is available on a public GitHub repo but not any package index like PyPI or Conda? If so, continue reading to find out how!

Let's suppose you want to install `SomePackage` and its Python dependencies from GitHub, a hosting service for the popular version control system (VCS) Git. And suppose `SomePackage` is found at the the following URL: `https://github.com/SomePackage.git`.

pip (via `requirements.txt`) [supports](https://pip.pypa.io/en/stable/topics/vcs-support/) installing from GitHub. This support requires a working executable to be available (for Git). It is used through a URL prefix: `git+`.

## Specify the GitHub web URL

To install `SomePackage`, innclude the following in your `requirements.txt` file:

```bash
git+https://github.com/SomePackage#egg=SomePackage
```

You can even specify a "git ref" such as branch name, a commit hash or a tag name, as shown in the examples below.

## Specify a Git branch name

Install `SomePackage` by specifying a branch name such as `main`, `master`, `develop`, etc, in `requirements.txt`:

```bash
git+https://github.com/SomePackage.git@main#egg=SomePackage
```

## Specify a commit hash

Install `SomePackage` by specifying a commit hash in `requirements.txt`:

```bash
git+https://github.com/SomePackage.git@eb40b4ff6f7c5c1e4366cgfg0671291bge918#egg=SomePackage
```

## Specify a tag

Install `SomePackage` by specifying a tag in `requirements.txt`:

```bash
git+https://github.com/SomePackage.git@v1.1.0#egg=SomePackage
```

## Limitations

It is currently **not possible** to install private packages from private GitHub repos using the URI form:

```bash
git+https://{token}@github.com/user/project.git@{version}
```

where `version` is a tag, a branch, or a commit. And `token` is a personal access token with read only permissions. Streamlit Community Cloud only supports installing public packages from public GitHub repos.

---

# ImportError libGL.so.1 cannot open shared object file No such file or directory

Source: https://docs.streamlit.io/knowledge-base/dependencies/libgl


## Problem

You receive the error `ImportError libGL.so.1 cannot open shared object file No such file or directory` when using OpenCV in your app deployed on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

If you use OpenCV in your app, include `opencv-python-headless` in your requirements file on Streamlit Community Cloud in place of `opencv_contrib_python` and `opencv-python`.

If `opencv-python` is a _required_ (non-optional) dependency of your app or a dependency of a library used in your app, the above solution is not applicable. Instead, you can use the following solution:

Create a `packages.txt` file in your repo with the following line to install the [apt-get dependency](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies) `libgl`:

```
libgl1
```

---

# ModuleNotFoundError: No module named

Source: https://docs.streamlit.io/knowledge-base/dependencies/module-not-found-error


## Problem

You receive the error `ModuleNotFoundError: No module named` when you deploy an app on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

This error occurs when you import a module on Streamlit Community Cloud that isn’t included in your requirements file. Any external [Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) that are not distributed with a [standard Python installation](https://docs.python.org/3/py-modindex.html) should be included in your requirements file.

E.g. You will see `ModuleNotFoundError: No module named 'sklearn'` if you don’t include `scikit-learn` in your requirements file and `import sklearn` in your app.

Related forum posts:

- https://discuss.streamlit.io/t/getting-error-modulenotfounderror-no-module-named-beautifulsoup/9126
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-vega-datasets/16354

---

# ERROR: No matching distribution found for

Source: https://docs.streamlit.io/knowledge-base/dependencies/no-matching-distribution


## Problem

You receive the error `ERROR: No matching distribution found for` when you deploy an app on [Streamlit Community Cloud](https://streamlit.io/cloud).

## Solution

This error occurs when you deploy an app on Streamlit Community Cloud and have one or more of the following issues with your [Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) in your requirements file:

1. The package is part of the [Python Standard Library](https://docs.python.org/3/py-modindex.html). E.g. You will see **`ERROR: No matching distribution found for base64`** if you include [`base64`](https://docs.python.org/3/library/base64.html) in your requirements file, as it is part of the Python Standard Library. The solution is to not include the package in your requirements file. Only include packages in your requirements file that are not distributed with a standard Python installation.
2. The package name in your requirements file is misspelled. Double-check the package name before including it in your requirements file.
3. The package does not support the operating system on which your Streamlit app is running. E.g. You see **`ERROR: No matching distribution found for pywin32`** while deploying to Streamlit Community Cloud. The `pywin32` module provides access to many of the Windows APIs from Python. Apps deployed to Streamlit Community Cloud are executed in a Linux environment. As such, `pywin32` fails to install on non-Windows systems, including on Streamlit Community Cloud. The solution is to either exclude `pywin32` from your requirements file, or deploy your app on a cloud service offering Windows machines.

Related forum posts:

- https://discuss.streamlit.io/t/error-no-matching-distribution-found-for-base64/15758
- https://discuss.streamlit.io/t/error-could-not-find-a-version-that-satisfies-the-requirement-pywin32-301-from-versions-none/15343/2

---

# Deployment-related questions and errors

Source: https://docs.streamlit.io/knowledge-base/deploy


- [How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?](/knowledge-base/deploy/deploy-streamlit-domain-port-80)
- [How can I deploy multiple Streamlit apps on different subdomains?](/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains)
- [Invoking a Python subprocess in a deployed Streamlit app](/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app)
- [Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)](/knowledge-base/deploy/does-streamlit-support-wsgi-protocol)
- [Argh. This app has gone over its resource limits.](/knowledge-base/deploy/resource-limits)
- [App is not loading when running remotely](/knowledge-base/deploy/remote-start)
- [Authentication without SSO](/knowledge-base/deploy/authentication-without-sso)
- [How do I increase the upload limit of `st.file_uploader` on Streamlit Community Cloud?](/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud)
- [Huh. This is isn't supposed to happen message after trying to log in](/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in)
- [Login attempt to Streamlit Community Cloud fails with error 403](/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403)
- [How to submit a support case for Streamlit Community Cloud](/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud)

---

# How can I deploy multiple Streamlit apps on different subdomains?

Source: https://docs.streamlit.io/knowledge-base/deploy/deploy-multiple-streamlit-apps-different-subdomains


## Problem

You want to deploy multiple Streamlit apps on different subdomains.

## Solution

Like running your Streamlit app on more common ports such as 80, subdomains are handled by a web server like Apache or Nginx:

- Set up a web server on a machine with a public IP address, then use a DNS server to point all desired subdomains to your webserver's IP address

- Configure your web server to route requests for each subdomain to the different ports that your Streamlit apps are running on

For example, let’s say you had two Streamlit apps called `Calvin` and `Hobbes`. App `Calvin` is running on port **8501**. You set up app `Hobbes` to run on port **8502**. Your webserver would then be set up to "listen" for requests on subdomains `calvin.somedomain.com` and `hobbes.subdomain.com`, and route requests to port **8501** and **8502**, respectively.

Check out these two tutorials for Apache2 and Nginx that deal with setting up a webserver to redirect subdomains to different ports:

- [Apache2 subdomains](https://stackoverflow.com/questions/8541182/apache-redirect-to-another-port)
- [NGinx subdomains](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)

---

# How do I deploy Streamlit on a domain so it appears to run on a regular port (i.e. port 80)?

Source: https://docs.streamlit.io/knowledge-base/deploy/deploy-streamlit-domain-port-80


## Problem

You want to deploy a Streamlit app on a domain so it appears to run on port 80.

## Solution

- You should use a **reverse proxy** to forward requests from a webserver like [Apache](https://httpd.apache.org/) or [Nginx](https://www.nginx.com/) to the port where your Streamlit app is running. You can accomplish this in several different ways. The simplest way is to [forward all requests sent to your domain](https://discuss.streamlit.io/t/permission-denied-in-ec2-port-80/798/3) so that your Streamlit app appears as the content of your website.

- Another approach is to configure your webserver to forward requests to designated subfolders (e.g. _http://awesomestuff.net/streamlitapp_) to different Streamlit apps on the same domain, as in this [example config for Nginx](https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/7) submitted by a Streamlit community member.

Related forum posts:

- https://discuss.streamlit.io/t/permission-denied-in-ec2-port-80/798/3
- https://discuss.streamlit.io/t/how-to-use-streamlit-with-nginx/378/7

---

# Does Streamlit support the WSGI Protocol? (aka Can I deploy Streamlit with gunicorn?)

Source: https://docs.streamlit.io/knowledge-base/deploy/does-streamlit-support-wsgi-protocol


## Problem

You're not sure whether your Streamlit app can be deployed with gunicorn.

## Solution

Streamlit does not support the WSGI protocol at this time, so deploying Streamlit with (for example) gunicorn is not currently possible. Check out this [forum thread regarding deploying Streamlit in a gunicorn-like manner](https://discuss.streamlit.io/t/how-do-i-set-the-server-to-0-0-0-0-for-deployment-using-docker/216) to see how other users have accomplished this.

---


---

**Navigation:** [← Previous](./10-2023-release-notes.md) | [Index](./index.md) | [Next →](./12-how-do-i-increase-the-upload-limit-of-stfile-uploa.md)
