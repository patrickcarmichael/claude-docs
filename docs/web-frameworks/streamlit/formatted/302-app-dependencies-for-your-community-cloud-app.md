---
title: "App dependencies for your Community Cloud app"
source: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies
section: 302
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
```python
However, a valid `requirements.txt` file would be:

```none
streamlit
pandas
numpy
```python
Alternatively, if you needed to specify certain versions, another valid example would be:

```none
streamlit==1.24.1
pandas&gt;2.0
numpy

---

[← Previous](301-file-organization-for-your-community-cloud-app.md) | [Index](index.md) | [Next →](index.md)
