**Navigation:** [← Previous](./11-deploy-an-app-from-a-template.md) | [Index](./index.md) | Next →

---

# How do I increase the upload limit of st.file_uploader on Streamlit Community Cloud?

Source: https://docs.streamlit.io/knowledge-base/deploy/increase-file-uploader-limit-streamlit-cloud


## Overview

By default, files uploaded using [`st.file_uploader()`](/develop/api-reference/widgets/st.file_uploader) are limited to 200MB. You can configure this using the `server.maxUploadSize` config option.

Streamlit provides [four different ways to set configuration options](/develop/concepts/configuration):

1. In a **global config file** at `~/.streamlit/config.toml` for macOS/Linux or `%userprofile%/.streamlit/config.toml` for Windows:
   ```toml
   [server]
   maxUploadSize = 200
   ```
2. In a **per-project config file** at `$CWD/.streamlit/config.toml`, where `$CWD` is the folder you're running Streamlit from.
3. Through `STREAMLIT_*` **environment variables**, such as:
   ```bash
   export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
   ```
4. As **flags on the command line** when running `streamlit run`:
   ```bash
   streamlit run your_script.py --server.maxUploadSize 200
   ```

Which of the four options should you choose for an app deployed to [Streamlit Community Cloud](/deploy/streamlit-community-cloud)? 🤔

## Solution

When deploying your app to Streamlit Community Cloud, you should **use option 1**. Namely, set the `maxUploadSize` config option in a global config file (`.streamlit/config.toml`) uploaded to your app's GitHub repo. 🎈

For example, to increase the upload limit to 400MB, upload a `.streamlit/config.toml` file containing the following lines to your app's GitHub repo:

```toml
[server]
maxUploadSize = 400
```

## Relevant resources

- [Streamlit drag and drop capping at 200MB, need workaround](https://discuss.streamlit.io/t/streamlit-drag-and-drop-capping-at-200mb-need-workaround/19803/2)
- [File uploader widget API](/develop/api-reference/widgets/st.file_uploader)
- [How to set Streamlit configuration options](/develop/concepts/configuration)

---

# Invoking a Python subprocess in a deployed Streamlit app

Source: https://docs.streamlit.io/knowledge-base/deploy/invoking-python-subprocess-deployed-streamlit-app


## Problem

Let's suppose you want to invoke a subprocess to run a Python script `script.py` in your deployed Streamlit app `streamlit_app.py`. For example, the machine learning library [Ludwig](https://ludwig-ai.github.io/ludwig-docs/) is run using a command-line interface, or maybe you want to run a bash script or similar type of process from Python.

You have tried the following, but run into dependency issues for `script.py`, even though you have specified your Python dependencies in a requirements file:

```python
# streamlit_app.py
import streamlit as st
import subprocess

subprocess.run(["python", "script.py"])
```

## Solution

When you run the above code block, you will get the version of Python that is on the system path—not necessarily the Python executable installed in the virtual environment that the Streamlit code is running under.

The solution is to detect the Python executable directly with [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable):

```python
# streamlit_app.py
import streamlit as st
import subprocess
import sys

subprocess.run([f"{sys.executable}", "script.py"])
```

This ensures that `script.py` is running under the same Python executable as your Streamlit code—where your [Python dependencies](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#add-python-dependencies) are installed.

### Relevant links

- https://stackoverflow.com/questions/69947867/run-portion-of-python-code-in-parallel-from-a-streamlit-app/69948545#69948545
- https://discuss.streamlit.io/t/modulenotfounderror-no-module-named-cv2-streamlit/18319/3?u=snehankekre
- https://docs.python.org/3/library/sys.html#sys.executable

---

# App is not loading when running remotely

Source: https://docs.streamlit.io/knowledge-base/deploy/remote-start


Below are a few common errors that occur when users spin up their own solution
to host a Streamlit app remotely.

To learn about a deceptively simple way to host Streamlit apps that avoids all
the issues below, check out [Streamlit Community Cloud](https://streamlit.io/cloud).

### Symptom #1: The app never loads

When you enter the app's URL in a browser and all you see is a **blank page, a
"Page not found" error, a "Connection refused" error**, or anything like that,
first check that Streamlit is actually running on the remote server. On a Linux
server you can SSH into it and then run:

```bash
ps -Al | grep streamlit
```

If you see Streamlit running, the most likely culprit is the Streamlit port not
being exposed. The fix depends on your exact setup. Below are three example
fixes:

- **Try port 80:** Some hosts expose port 80 by default. To
  set Streamlit to use that port, start Streamlit with the `--server.port`
  option:

  ```bash
  streamlit run my_app.py --server.port=80
  ```

- **AWS EC2 server**: First, click on your instance in the [AWS Console](https://us-west-2.console.aws.amazon.com/ec2/v2/home).
  Then scroll down and click on _Security Groups_ → _Inbound_ → _Edit_. Next, add
  a _Custom TCP_ rule that allows the _Port Range_ `8501` with _Source_
  `0.0.0.0/0`.

- **Other types of server**: Check the firewall settings.

If that still doesn't solve the problem, try running a simple HTTP server
instead of Streamlit, and seeing if _that_ works correctly. If it does, then
you know the problem lies somewhere in your Streamlit app or configuration (in
which case you should ask for help in our
[forums](https://discuss.streamlit.io)!) If not, then it's definitely unrelated
to Streamlit.

How to start a simple HTTP server:

```bash
python -m http.server [port]
```

### Symptom #2: The app says "Please wait..." or shows skeleton elements forever

This symptom appears differently starting from version 1.29.0. For earlier
versions of Streamlit, a loading app shows a blue box in the center of the page
with a "Please wait..." message. Starting from version 1.29.0, a loading app
shows skeleton elements. If this loading screen does not go away, the
underlying cause is likely one of the following:

- Using port 3000 which is reserved for internal development.
- Misconfigured [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
  protection.
- Server is stripping headers from the Websocket connection, thereby breaking
  compression.

To diagnose the issue, first make sure you are not using port 3000. If in doubt,
try port 80 as described above.

Next, try temporarily disabling CORS protection by running Streamlit with the
`--server.enableCORS` flag set to `false`:

```bash
streamlit run my_app.py --server.enableCORS=false
```

If this fixes your issue, **you should re-enable CORS protection** and then set
`browser.serverAddress` to the URL of your Streamlit app.

If the issue persists, try disabling websocket compression by running Streamlit with the
`--server.enableWebsocketCompression` flag set to `false`

```bash
streamlit run my_app.py --server.enableWebsocketCompression=false
```

If this fixes your issue, your server setup is likely stripping the
`Sec-WebSocket-Extensions` HTTP header that is used to negotiate Websocket compression.

Compression is not required for Streamlit to work, but it's strongly recommended as it
improves performance. If you'd like to turn it back on, you'll need to find which part
of your infrastructure is stripping the `Sec-WebSocket-Extensions` HTTP header and
change that behavior.

### Symptom #3: Unable to upload files when running in multiple replicas

If the file uploader widget returns an error with status code 403, this is probably
due to a misconfiguration in your app's
[XSRF](https://en.wikipedia.org/wiki/Cross-site_request_forgery) protection logic.

To diagnose the issue, try temporarily disabling XSRF protection by running Streamlit
with the `--server.enableXsrfProtection` flag set to `false`:

```bash
streamlit run my_app.py --server.enableXsrfProtection=false
```

If this fixes your issue, **you should re-enable XSRF protection** and try one
or both of the following:

- Set `browser.serverAddress` and `browser.serverPort` to the URL and port of
  your Streamlit app.
- Configure your app to use the same secret across every replica by setting the
  `server.cookieSecret` config option to the same hard-to-guess string everywhere.

---

# Argh. This app has gone over its resource limits

Source: https://docs.streamlit.io/knowledge-base/deploy/resource-limits


Sorry! It means you've hit the [resource limits](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits) of your [Streamlit Community Cloud](https://streamlit.io/cloud) account.

There are a few things you can change in your app to make it less resource-hungry:

- Reboot your app (temporary fix)
- Use `st.cache_data` or `st.cache_resource` to load models or data only once
- Restrict the cache size with `ttl` or `max_entries`
- Move big datasets to a database
- Profile your app's memory usage

Check out our [blog post](https://blog.streamlit.io/common-app-problems-resource-limits/) on ["Common app problems: Resource limits"](https://blog.streamlit.io/common-app-problems-resource-limits/) for more in-depth tips prevent your app from hitting the [resource limits](/deploy/streamlit-community-cloud/manage-your-app#app-resources-and-limits) of the Streamlit Community Cloud.

Related forum posts:

- [https://discuss.streamlit.io/t/common-app-problems-resource-limits/16969](https://discuss.streamlit.io/t/common-app-problems-resource-limits/16969)
- [https://blog.streamlit.io/common-app-problems-resource-limits/](https://blog.streamlit.io/common-app-problems-resource-limits/)

We offer free resource increases only to support nonprofits or educational organizations on a case-by-case basis. If you are a nonprofit or educational organization, please complete [this form](https://info.snowflake.com/streamlit-resource-increase-request.html) and we will review your submission as soon as possible.

Once the increase is completed, you will receive an email from the Streamlit marketing team with a confirmation that the increase has been applied.

---

# Huh. This is isn't supposed to happen message after trying to log in

Source: https://docs.streamlit.io/knowledge-base/deploy/huh-this-isnt-supposed-to-happen-message-after-trying-to-log-in


This article helps to resolve the login issue caused by email mismatching between the GitHub and the Streamlit Community Cloud.

## Problem

You see the following message after signing in to your Streamlit Community Cloud account:

![Huh. This is isn't supposed to happen message](/images/knowledge-base/huh-this-isnt-supposed-to-happen.png)

This message usually indicates that our system has linked your GitHub username with an email address other than the email address you're currently logged in with.

## Solution

No worries – all you have to do is:

1. Log out of Streamlit Community Cloud completely (via both your email and GitHub accounts).
2. Log in first with your email account (you can do so via either ["Continue with Google"](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-google) or ["Continue with email"](/knowledge-base/deploy/sign-in-without-sso)).
3. Log in with your [GitHub account](/deploy/streamlit-community-cloud/manage-your-account/sign-in-sign-out#sign-in-with-email).

---

# Login attempt to Streamlit Community Cloud fails with error 403

Source: https://docs.streamlit.io/knowledge-base/deploy/login-attempt-to-streamlit-community-cloud-fails-with-error-403


## Problem

Streamlit Community Cloud has monitoring jobs to detect malicious users using the platform for crypto mining. These jobs sometimes result in false positives and a normal user starts getting error 403 against a login attempt.

## Solution

Please contact [Support](mailto:support@streamlit.io) by providing your **GitHub username** for help referring to this article.

---

# How to submit a support case for Streamlit Community Cloud

Source: https://docs.streamlit.io/knowledge-base/deploy/how-to-submit-a-support-case-for-streamlit-community-cloud


This article describes the steps to submit a support request to Snowflake for Streamlit Community Cloud.

<Note>

For Snowflake customers, a support case can be submitted via [the support portal on Snowsight](https://community.snowflake.com/s/article/How-To-Submit-a-Support-Case-in-Snowflake-Lodge#Option1).

</Note>

1. Navigate to [https://community.snowflake.com/s/](https://community.snowflake.com/s/) in your browser.
1. If you already have a Snowflake Community account, sign in. Otherwise, click "**CREATE ACCOUNT**," and follow the prompts.
1. At the top of the page, click "**SUPPORT**."
1. From the drop-down menu, select "**Submit A Case**."
1. Select the option "**I am a Streamlit Community Cloud user**."
1. Click "**Next**" to open the case description page.
1. Fill out your request and submit the support case.

You should receive a confirmation email with the case number. A Snowflake Support engineer will follow up directly with the next steps to resolve your case. All communication will be through email.

---


---

**Navigation:** [← Previous](./11-deploy-an-app-from-a-template.md) | [Index](./index.md) | Next →
