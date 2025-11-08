**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-define-multipage-apps-with-stpage-and-stnavigation.md)

---

# Get started with Streamlit

Source: https://docs.streamlit.io/get-started


This Get Started guide explains how Streamlit works, how to install Streamlit on your preferred
operating system, and how to create your first Streamlit app!

<InlineCalloutContainer>
<InlineCallout bold="Installation" color="orange-70" href="/get-started/installation" icon="downloading">helps you set up your development environment. Walk through installing Streamlit on Windows, macOS, or Linux. Alternatively, code right in your browser with GitHub Codespaces or Streamlit in Snowflake.</InlineCallout>
<InlineCallout bold="Fundamentals" color="orange-70" href="/get-started/fundamentals" icon="description">introduces you to Streamlit's data model and development flow. You'll learn what makes Streamlit the most powerful way to build data apps, including the ability to display and style data, draw charts and maps, add interactive widgets, customize app layouts, cache computation, and define themes.</InlineCallout>
<InlineCallout bold="First steps" color="orange-70" href="/get-started/tutorials" icon="auto_awesome">walks you through creating apps using core features to fetch and cache data, draw charts, plot information on a map, and use interactive widgets to filter results.</InlineCallout>
<InlineCallout bold="Use GitHub Codespaces" color="orange-70" href="/get-started/installation/community-cloud" icon="rocket_launch">if you want to skip past local installation and code right in your browser. This guide uses Streamlit Community Cloud to help you automatically configure a codespace.</InlineCallout>
</InlineCalloutContainer>
<NoteSplit background="gray-20" copy="30 Days of Streamlit 🎈 is a free, self-paced 30 day challenge that teaches you how to build and deploy data apps with Streamlit. Complete the daily challenges, share your solutions with us on Twitter and LinkedIn, and stop by the forum with any questions!" title="30 Days of Streamlit 🎈">{{
        text: "Start the challenge",
        link: "https://30days.streamlit.app/",
        target: "_blank",
      }}
image="/30days.png"
/&gt;</NoteSplit>

---

# Install Streamlit

Source: https://docs.streamlit.io/get-started/installation


There are multiple ways to set up your development environment and install Streamlit.
Developing locally with Python installed on your own computer is the most
common scenario.

<Tip>

Try a Streamlit Playground that runs in your browser  no installation required.
(Note that this is not how Streamlit is meant to be used, because it has many downsides. That's why it's a
_playground_!)

<IconLink cssModuleClassName="Indigo" cssModuleIconClassName="IconRight" href="/get-started/installation/streamlit-playground" icon="arrow_forward" label="Instructions for the playground"/>
</Tip>

## Summary for experienced Python developers

1. To set up your Python environment and test your installation, execute the following terminal commands:

   ```bash
   pip install streamlit
   streamlit hello
   ```

1. Jump to our [Basic concepts](/get-started/fundamentals/main-concepts).

## Install Streamlit on your machine

### Option 1: I like the command line

Install Streamlit on your own machine using tools like `venv` and `pip`.

<IconLink cssModuleClassName="Orange" cssModuleIconClassName="IconRight" href="/get-started/installation/command-line" icon="arrow_forward" label="Instructions for the command line"/>

### Option 2: I prefer a graphical interface

Install Streamlit using the Anaconda Distribution graphical user interface. This is also the best
approach if you're on Windows or don't have Python set up.

<IconLink cssModuleClassName="Orange" cssModuleIconClassName="IconRight" href="/get-started/installation/anaconda-distribution" icon="arrow_forward" label="Instructions for Anaconda Distribution"/>

## Create an app in the cloud

### Option 1: I want a free cloud environment

Use Streamlit Community Cloud with GitHub Codespaces so you don't have to go through the trouble
of installing Python and setting up an environment.

<IconLink cssModuleClassName="Orange" cssModuleIconClassName="IconRight" href="/get-started/installation/community-cloud" icon="arrow_forward" label="Instructions for GitHub Codespaces"/>

### Option 2: I need something secure, controlled, and in the cloud

Use Streamlit in Snowflake to code your apps in the cloud, right alongside your
data with role-based access controls.

<IconLink cssModuleClassName="Orange" cssModuleIconClassName="IconRight" href="/get-started/installation/streamlit-in-snowflake" icon="arrow_forward" label="Instructions for Snowflake"/>

---

# Use Streamlit Playground in your browser

Source: https://docs.streamlit.io/get-started/installation/streamlit-playground


The fastest way to try out Streamlit is to try out our Playground! Streamlit Playground runs in your browser. Just visit the Playground, and a _limited_ version of Streamlit loads as browser scripts.

Enjoy the following conveniences:

- Start playing with code right away, completely in your browser.
- No configuration.
- No command line.
- No application installations in your OS.

<Important>

Although the Playground has everything you need to get started, it doesn't contain the full version of Streamlit. To access the full awesomeness of Streamlit, see [Install Streamlit using command line](/get-started/installation/command-line) or [Install Streamlit using Anaconda Distribution](/get-started/installation/anaconda-distribution).

</Important>

## Prerequisites

Because the Playground runs Streamlit _locally_ in your browser, you should visit the Playground from a personal computer, not a mobile device.

## Go to the Playground

1. Go to [streamlit.io/playground](https://streamlit.io/playground).

1. Wait for the playground to load.

   Behind the scenes, the site installs a browser-based version of Python and Streamlit. This can take as little as a few seconds. The setup time can vary depending on your machine and internet connection. When Streamlit is done loading, an example app is displayed in the right panel.

   ![Streamlit Playground is fully loaded and ready to accept code edits](/images/get-started/Playground-1-loaded.png)

1. Optional: To view different examples, above the editor, select them from the examples list.

## Create a `Hello World` app

1. From the "EXAMPLES" list, select "**Blank**."

1. On the left, update the contents of the code editor to contain the following code:

   ```python
   import streamlit as st

   st.write("Hello World")
   ```

   A second or two after typing or pasting the code into the editor, the right panel will display the updated app. The code editor saves your edits whenever you pause from typing. Therefore, if you pause between keystrokes as you type a new line of code, you may see an error on the right because Streamlit executed an incomplete line. If this happens, just keep typing to complete the line(s) you are writing. When you pause again at the end of the line, Streamlit reruns the app.

1. On the left, change `st.write` to `st.title` so the code editor has the following code:

   ```python
   import streamlit as st

   st.title("Hello World")
   ```

   A second after you stop typing, Streamlit reruns the app and updates the display on the right.

1. Keep making changes! Watch as your edits are automatically saved and the new result is displayed on the right.

## What's next?

- Option 1: If you're already intrigued and ready to install Streamlit on your computer, see one of the options to [Install Streamlit on your machine](/get-started/installation#install-on-your-machine).

- Option 2: Otherwise, you can keep using the playground while you read about our [Basic concepts](/get-started/fundamentals/main-concepts) and try out more commands in your app.

  When you use the Streamlit Playground to work through the basic concepts, you can skip over any instructions to save your file or to select "**Rerun on save**." Streamlit Playground automatically saves your code when you pause from editing, as described above. Also, it is already configured to rerun on save.

---

# Install Streamlit using command line

Source: https://docs.streamlit.io/get-started/installation/command-line


This page will walk you through creating an environment with `venv` and installing Streamlit with `pip`. These are our recommended tools, but if you are familiar with others you can use your favorite ones too. At the end, you'll build a simple "Hello world" app and run it. If you prefer to have a graphical interface to manage your Python environments, check out how to [Install Streamlit using Anaconda Distribution](/get-started/installation/anaconda-distribution).

## Prerequisites

As with any programming tool, in order to install Streamlit you first need to make sure your
computer is properly set up. More specifically, you’ll need:

1. **Python**

   We support [version 3.9 to 3.13](https://www.python.org/downloads/).

1. **A Python environment manager** (recommended)

   Environment managers create virtual environments to isolate Python package installations between
   projects.

   We recommend using virtual environments because installing or upgrading a Python package may
   cause unintentional effects on another package. For a detailed introduction to Python
   environments, check out
   [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

   For this guide, we'll be using `venv`, which comes with Python.

1. **A Python package manager**

   Package managers handle installing each of your Python packages, including Streamlit.

   For this guide, we'll be using `pip`, which comes with Python.

1. **Only on MacOS: Xcode command line tools**

   Download Xcode command line tools using [these instructions](https://mac.install.guide/commandlinetools/4.html)
   in order to let the package manager install some of Streamlit's dependencies.

1. **A code editor**

   Our favorite editor is [VS Code](https://code.visualstudio.com/download), which is also what we use in
   all our tutorials.

## Create an environment using `venv`

1. Open a terminal and navigate to your project folder.

   ```bash
   cd myproject
   ```

2. In your terminal, type:

   ```bash
   python -m venv .venv
   ```

3. A folder named ".venv" will appear in your project. This directory is where your virtual environment and its dependencies are installed.

## Activate your environment

4. In your terminal, activate your environment with one of the following commands, depending on your operating system.

   ```bash
   # Windows command prompt
   .venv\Scripts\activate.bat

   # Windows PowerShell
   .venv\Scripts\Activate.ps1

   # macOS and Linux
   source .venv/bin/activate
   ```

5. Once activated, you will see your environment name in parentheses before your prompt. "(.venv)"

## Install Streamlit in your environment

6. In the terminal with your environment activated, type:

   ```bash
   pip install streamlit
   ```

7. Test that the installation worked by launching the Streamlit Hello example app:

   ```bash
   streamlit hello
   ```

   If this doesn't work, use the long-form command:

   ```bash
   python -m streamlit hello
   ```

8. Streamlit's Hello app should appear in a new tab in your web browser!
   <Cloud height="700px" name="doc-mpa-hello"/>
9. Close your terminal when you are done.

## Create a "Hello World" app and run it

10. Create a file named `app.py` in your project folder.

```python
import streamlit as st

st.write("Hello world")
```

11. Any time you want to use your new environment, you first need to go to your project folder (where the `.venv` directory lives) and run the command to activate it:

```bash
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

12. Once activated, you will see your environment's name in parentheses at the beginning of your terminal prompt. "(.venv)"

13. Run your Streamlit app.

```bash
streamlit run app.py
```

If this doesn't work, use the long-form command:

```bash
python -m streamlit run app.py
```

14. To stop the Streamlit server, press `Ctrl+C` in the terminal.

15. When you're done using this environment, return to your normal shell by typing:

```bash
deactivate
```

## What's next?

Read about our [Basic concepts](/get-started/fundamentals/main-concepts) to understand Streamlit's dataflow model.

---

# Install Streamlit using Anaconda Distribution

Source: https://docs.streamlit.io/get-started/installation/anaconda-distribution


This page walks you through installing Streamlit locally using Anaconda Distribution. At the end, you'll build a simple "Hello world" app and run it. You can read more about [Getting started with Anaconda Distribution](https://docs.anaconda.com/free/anaconda/getting-started/) in Anaconda's docs. If you prefer to manage your Python environments via command line, check out how to [Install Streamlit using command line](/get-started/installation/command-line).

## Prerequisites

1. **A code editor**

   Anaconda Distribution includes Python and basically everything you need to get started.
   The only thing left for you to choose is a code editor.

   Our favorite editor is [VS Code](https://code.visualstudio.com/download), which is also what we
   use in all our tutorials.

1. **Knowledge about environment managers**

   Environment managers create virtual environments to isolate Python package installations between
   projects. For a detailed introduction to Python environments, check out
   [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

   But don't worry! In this guide we'll teach you how to install and use an environment manager
   (Anaconda).

## Install Anaconda Distribution

1. Go to [anaconda.com/download](https://www.anaconda.com/download).

2. Install Anaconda Distribution for your OS.

## Create an environment using Anaconda Navigator

3. Open Anaconda Navigator (the graphical interface included with Anaconda Distribution).

4. You can decline signing in to Anaconda if prompted.

5. In the left menu, click "**Environments**."
   ![Open your environments list in Anaconda Navigator](/images/get-started/Anaconda-Navigator-environment-1.png)

6. At the bottom of your environments list, click "**Create**."
   ![Click "Create" to open the Create new environment dialog](/images/get-started/Anaconda-Navigator-environment-2-create.png)

7. Enter "streamlitenv" for the name of your environment.

8. Click "**Create**."
<div>{{ maxWidth: '50%', margin: 'auto' }}&gt;
    <Image alt="Finalize your new conda environment" src="/images/get-started/Anaconda-Navigator-environment-3-name.png"/>
</div>

---

# Use Community Cloud to develop with GitHub Codespaces

Source: https://docs.streamlit.io/get-started/installation/community-cloud


To use GitHub Codespaces for Streamlit development, you need a properly configured `devcontainer.json` file to set up the environment. Fortunately, Streamlit Community Cloud is here to help! Although Community Cloud is primarily used to deploy and share apps with the rest of the world, we've built in some handy features to make it easy to use GitHub Codespaces. This guide explains how to create a Community Cloud account and use an automated workflow to get you into a GitHub codespace and live-editing a Streamlit app. All this happens right in your browser, no installation required.

If you already created a Community Cloud account and connected GitHub, jump ahead to [Create a new app from a template](/get-started/installation/community-cloud#create-a-new-app-from-a-template).

## Prerequisites

- You must have a GitHub account.

## Sign up for Streamlit Community Cloud

1. Go to <a href="https://share.streamlit.io" target="_blank">share.streamlit.io</a>.
1. Click "**Continue to sign-in**."
1. Click "**Continue with GitHub**."
1. Enter your GitHub credentials and follow GitHub's authentication prompts.
1. Fill in your account information, and click "**I accept**" at the bottom.

## Add access to your public repositories

1. In the upper-left corner, click on "**Workspaces <i>{{ verticalAlign: "-.25em", color: "#ff8700" }} className={{ class: "material-icons-sharp" }}&gt;warning</i>

---

# Use Streamlit in Snowflake to code in a secure environment

Source: https://docs.streamlit.io/get-started/installation/streamlit-in-snowflake


Snowflake is a single, global platform that powers the Data Cloud. If you want to use a secure platform with role-based access control, this is the option for you! This page walks you through creating a trial Snowflake account and building a "Hello world" app. Your trial account comes with an account credit so you can try out the service without entering any payment information.

<Note>

For more information, see [Limitations and unsupported features](https://docs.snowflake.com/en/developer-guide/streamlit/limitations) in the Snowflake documentation.

</Note>

## Prerequisites

All you need is an email address! Everything else happens in your 30-day trial account.

## Create an account

1. Go to <SnowflakeTrial/>. (This link will open in a new tab.)

1. Fill in your information, and click "**CONTINUE**."

1. Select "**Standard**" for your Snowflake edition and "**Amazon Web Services**" for your cloud provider.

1. Choose the region nearest you, accept the terms, and click "**GET STARTED**."

<div>{{ maxWidth: '50%', margin: 'auto' }}&gt;
    <Image alt="Choose your Snowflake edition, provider, and region" src="/images/get-started/SiS-region.png"/>
</div>

---

# Fundamental concepts

Source: https://docs.streamlit.io/get-started/fundamentals


Are you new to Streamlit and want the grand tour? If so, you're in the right place!

<InlineCalloutContainer>
<InlineCallout bold="Basic concepts." color="orange-70" href="/get-started/fundamentals/main-concepts" icon="description">Learn the fundamental concepts of Streamlit. How is a Streamlit app structured? How does it run? How does it magically get your data on a webpage?</InlineCallout>
<InlineCallout bold="Advanced concepts." color="orange-70" href="/get-started/fundamentals/advanced-concepts" icon="description">After you understand the rerun logic of Streamlit, learn how to make efficient and dynamic apps with caching and Session State. Get introduced to handling database connections.</InlineCallout>
<InlineCallout bold="Additional features." color="orange-70" href="/get-started/fundamentals/additional-features" icon="description">Learn about Streamlit's additional features. You don't need to know these concepts for your first app, but check it out to know what's available.</InlineCallout>
</InlineCalloutContainer>

---

# Basic concepts of Streamlit

Source: https://docs.streamlit.io/get-started/fundamentals/main-concepts


Working with Streamlit is simple. First you sprinkle a few Streamlit commands
into a normal Python script, then you run it with `streamlit run`:

```bash
streamlit run your_script.py [-- script args]
```

As soon as you run the script as shown above, a local Streamlit server will
spin up and your app will open in a new tab in your default web browser. The app
is your canvas, where you'll draw charts, text, widgets, tables, and more.

What gets drawn in the app is up to you. For example
[`st.text`](/develop/api-reference/text/st.text) writes raw text to your app, and
[`st.line_chart`](/develop/api-reference/charts/st.line_chart) draws — you guessed it — a
line chart. Refer to our [API documentation](/develop/api-reference) to see all commands that
are available to you.

<Note>

When passing your script some custom arguments, they must be passed after two dashes. Otherwise the
arguments get interpreted as arguments to Streamlit itself.

</Note>

Another way of running Streamlit is to run it as a Python module. This can be
useful when configuring an IDE like PyCharm to work with Streamlit:

```bash
# Running
python -m streamlit run your_script.py

# is equivalent to:
streamlit run your_script.py
```

<Tip>

You can also pass a URL to `streamlit run`! This is great when combined with
GitHub Gists. For example:

```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

</Tip>

## Development flow

Every time you want to update your app, save the source file. When you do
that, Streamlit detects if there is a change and asks you whether you want to
rerun your app. Choose "Always rerun" at the top-right of your screen to
automatically update your app every time you change its source code.

This allows you to work in a fast interactive loop: you type some code, save
it, try it out live, then type some more code, save it, try it out, and so on
until you're happy with the results. This tight loop between coding and viewing
results live is one of the ways Streamlit makes your life easier.

<Tip>

While developing a Streamlit app, it's recommended to lay out your editor and
browser windows side by side, so the code and the app can be seen at the same
time. Give it a try!

</Tip>

As of Streamlit version 1.10.0 and higher, Streamlit apps cannot be run from the root directory of Linux distributions. If you try to run a Streamlit app from the root directory, Streamlit will throw a `FileNotFoundError: [Errno 2] No such file or directory` error. For more information, see GitHub issue [#5239](https://github.com/streamlit/streamlit/issues/5239).

If you are using Streamlit version 1.10.0 or higher, your main script should live in a directory other than the root directory. When using Docker, you can use the `WORKDIR` command to specify the directory where your main script lives. For an example of how to do this, read [Create a Dockerfile](/deploy/tutorials/docker#create-a-dockerfile).

## Data flow

Streamlit's architecture allows you to write apps the same way you write plain
Python scripts. To unlock this, Streamlit apps have a unique data flow: any
time something must be updated on the screen, Streamlit reruns your entire
Python script from top to bottom.

This can happen in two situations:

- Whenever you modify your app's source code.

- Whenever a user interacts with widgets in the app. For example, when dragging
  a slider, entering text in an input box, or clicking a button.

Whenever a callback is passed to a widget via the `on_change` (or `on_click`) parameter, the callback will always run before the rest of your script. For details on the Callbacks API, please refer to our [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state).

And to make all of this fast and seamless, Streamlit does some heavy lifting
for you behind the scenes. A big player in this story is the
[`@st.cache_data`](#caching) decorator, which allows developers to skip certain
costly computations when their apps rerun. We'll cover caching later in this
page.

## Display and style data

There are a few ways to display data (tables, arrays, data frames) in Streamlit
apps. [Below](#use-magic), you will be introduced to _magic_
and [`st.write()`](/develop/api-reference/write-magic/st.write), which can be used to write
anything from text to tables. After that, let's take a look at methods designed
specifically for visualizing data.

### Use magic

You can also write to your app without calling any Streamlit methods.
Streamlit supports "[magic commands](/develop/api-reference/write-magic/magic)," which means you don't have to use
[`st.write()`](/develop/api-reference/write-magic/st.write) at all! To see this in action try this snippet:

```python
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
```

Any time that Streamlit sees a variable or a literal
value on its own line, it automatically writes that to your app using
[`st.write()`](/develop/api-reference/write-magic/st.write). For more information, refer to the
documentation on [magic commands](/develop/api-reference/write-magic/magic).

### Write a data frame

Along with [magic commands](/develop/api-reference/write-magic/magic),
[`st.write()`](/develop/api-reference/write-magic/st.write) is Streamlit's "Swiss Army knife". You
can pass almost anything to [`st.write()`](/develop/api-reference/write-magic/st.write):
text, data, Matplotlib figures, Altair charts, and more. Don't worry, Streamlit
will figure it out and render things the right way.

```python
import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
```

There are other data specific functions like
[`st.dataframe()`](/develop/api-reference/data/st.dataframe) and
[`st.table()`](/develop/api-reference/data/st.table) that you can also use for displaying
data. Let's understand when to use these features and how to add colors and styling to your data frames.

You might be asking yourself, "why wouldn't I always use `st.write()`?" There are
a few reasons:

1. _Magic_ and [`st.write()`](/develop/api-reference/write-magic/st.write) inspect the type of
   data that you've passed in, and then decide how to best render it in the
   app. Sometimes you want to draw it another way. For example, instead of
   drawing a dataframe as an interactive table, you may want to draw it as a
   static table by using `st.table(df)`.
2. The second reason is that other methods return an object that can be used
   and modified, either by adding data to it or replacing it.
3. Finally, if you use a more specific Streamlit method you can pass additional
   arguments to customize its behavior.

For example, let's create a data frame and change its formatting with a Pandas
`Styler` object. In this example, you'll use Numpy to generate a random sample,
and the [`st.dataframe()`](/develop/api-reference/data/st.dataframe) method to draw an
interactive table.

<Note>

This example uses Numpy to generate a random sample, but you can use Pandas
DataFrames, Numpy arrays, or plain Python arrays.

</Note>

```python
import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
```

Let's expand on the first example using the Pandas `Styler` object to highlight
some elements in the interactive table.

```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))
```

Streamlit also has a method for static table generation:
[`st.table()`](/develop/api-reference/data/st.table).

```python
import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)
```

### Draw charts and maps

Streamlit supports several popular data charting libraries like [Matplotlib,
Altair, deck.gl, and more](/develop/api-reference#chart-elements). In this section, you'll
add a bar chart, line chart, and a map to your app.

### Draw a line chart

You can easily add a line chart to your app with
[`st.line_chart()`](/develop/api-reference/charts/st.line_chart). We'll generate a random
sample using Numpy and then chart it.

```python
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
```

### Plot a map

With [`st.map()`](/develop/api-reference/charts/st.map) you can display data points on a map.
Let's use Numpy to generate some sample data and plot it on a map of
San Francisco.

```python
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
```

## Widgets

When you've got the data or model into the state that you want to explore, you
can add in widgets like [`st.slider()`](/develop/api-reference/widgets/st.slider),
[`st.button()`](/develop/api-reference/widgets/st.button) or
[`st.selectbox()`](/develop/api-reference/widgets/st.selectbox). It's really straightforward
— treat widgets as variables:

```python
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
```

On first run, the app above should output the text "0 squared is 0". Then
every time a user interacts with a widget, Streamlit simply reruns your script
from top to bottom, assigning the current state of the widget to your variable
in the process.

For example, if the user moves the slider to position `10`, Streamlit will
rerun the code above and set `x` to `10` accordingly. So now you should see the
text "10 squared is 100".

Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget:

```python
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
```

Every widget with a key is automatically added to Session State. For more information about Session State, its association with widget state, and its limitations, see [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state).

### Use checkboxes to show/hide data

One use case for checkboxes is to hide or show a specific chart or section in
an app. [`st.checkbox()`](/develop/api-reference/widgets/st.checkbox) takes a single argument,
which is the widget label. In this sample, the checkbox is used to toggle a
conditional statement.

```python
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
```

### Use a selectbox for options

Use [`st.selectbox`](/develop/api-reference/widgets/st.selectbox) to choose from a series. You
can write in the options you want, or pass through an array or data frame
column.

Let's use the `df` data frame we created earlier.

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
```

## Layout

Streamlit makes it easy to organize your widgets in a left panel sidebar with
[`st.sidebar`](/develop/api-reference/layout/st.sidebar). Each element that's passed to
[`st.sidebar`](/develop/api-reference/layout/st.sidebar) is pinned to the left, allowing
users to focus on the content in your app while still having access to UI
controls.

For example, if you want to add a selectbox and a slider to a sidebar,
use `st.sidebar.slider` and `st.sidebar.selectbox` instead of `st.slider` and
`st.selectbox`:

```python
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
```

Beyond the sidebar, Streamlit offers several other ways to control the layout
of your app. [`st.columns`](/develop/api-reference/layout/st.columns) lets you place widgets side-by-side, and
[`st.expander`](/develop/api-reference/layout/st.expander) lets you conserve space by hiding away large content.

```python
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
```

<Note>

`st.echo` and `st.spinner` are not currently supported inside the sidebar
or layout options. Rest assured, though, we're currently working on adding support for those too!

</Note>

### Show progress

When adding long running computations to an app, you can use
[`st.progress()`](/develop/api-reference/status/st.progress) to display status in real time.

First, let's import time. We're going to use the `time.sleep()` method to
simulate a long running computation:

```python
import time
```

Now, let's create a progress bar:

```python
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
```

---

# Advanced concepts of Streamlit

Source: https://docs.streamlit.io/get-started/fundamentals/advanced-concepts


Now that you know how a Streamlit app runs and handles data, let's talk about being efficient. Caching allows you to save the output of a function so you can skip over it on rerun. Session State lets you save information for each user that is preserved between reruns. This not only allows you to avoid unecessary recalculation, but also allows you to create dynamic pages and handle progressive processes.

## Caching

Caching allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

The basic idea behind caching is to store the results of expensive function calls and return the cached result when the same inputs occur again. This avoids repeated execution of a function with the same input values.

To cache a function in Streamlit, you need to apply a caching decorator to it. You have two choices:

- `st.cache_data` is the recommended way to cache computations that return data. Use `st.cache_data` when you use a function that returns a serializable data object (e.g. str, int, float, DataFrame, dict, list). **It creates a new copy of the data at each function call**, making it safe against [mutations and race conditions](/develop/concepts/architecture/caching#mutation-and-concurrency-issues). The behavior of `st.cache_data` is what you want in most cases – so if you're unsure, start with `st.cache_data` and see if it works!
- `st.cache_resource` is the recommended way to cache global resources like ML models or database connections. Use `st.cache_resource` when your function returns unserializable objects that you don’t want to load multiple times. **It returns the cached object itself**, which is shared across all reruns and sessions without copying or duplication. If you mutate an object that is cached using `st.cache_resource`, that mutation will exist across all reruns and sessions.

Example:

```python
@st.cache_data
def long_running_function(param1, param2):
    return …
```

In the above example, `long_running_function` is decorated with `@st.cache_data`. As a result, Streamlit notes the following:

- The name of the function (`"long_running_function"`).
- The value of the inputs (`param1`, `param2`).
- The code within the function.

Before running the code within `long_running_function`, Streamlit checks its cache for a previously saved result. If it finds a cached result for the given function and input values, it will return that cached result and not rerun function's code. Otherwise, Streamlit executes the function, saves the result in its cache, and proceeds with the script run. During development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache.

<Image alt="Streamlit's two caching decorators and their use cases. Use st.cache_data for anything you'd store in a database. Use st.cache_resource for anything you can't store in a database, like a connection to a database or a machine learning model." caption="Streamlit's two caching decorators and their use cases." src="/images/caching-high-level-diagram.png"/>

For more information about the Streamlit caching decorators, their configuration parameters, and their limitations, see [Caching](/develop/concepts/architecture/caching).

## Session State

Session State provides a dictionary-like interface where you can save information that is preserved between script reruns. Use `st.session_state` with key or attribute notation to store and recall values. For example, `st.session_state["my_key"]` or `st.session_state.my_key`. Remember that widgets handle their statefulness all by themselves, so you won't always need to use Session State!

### What is a session?

A session is a single instance of viewing an app. If you view an app from two different tabs in your browser, each tab will have its own session. So each viewer of an app will have a Session State tied to their specific view. Streamlit maintains this session as the user interacts with the app. If the user refreshes their browser page or reloads the URL to the app, their Session State resets and they begin again with a new session.

### Examples of using Session State

Here's a simple app that counts the number of times the page has been run. Every time you click the button, the script will rerun.

```python
import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")
```

- **First run:** The first time the app runs for each user, Session State is empty. Therefore, a key-value pair is created (`"counter":0`). As the script continues, the counter is immediately incremented (`"counter":1`) and the result is displayed: "This page has run 1 times." When the page has fully rendered, the script has finished and the Streamlit server waits for the user to do something. When that user clicks the button, a rerun begins.

- **Second run:** Since "counter" is already a key in Session State, it is not reinitialized. As the script continues, the counter is incremented (`"counter":2`) and the result is displayed: "This page has run 2 times."

There are a few common scenarios where Session State is helpful. As demonstrated above, Session State is used when you have a progressive process that you want to build upon from one rerun to the next. Session State can also be used to prevent recalculation, similar to caching. However, the differences are important:

- Caching associates stored values to specific functions and inputs. Cached values are accessible to all users across all sessions.
- Session State associates stored values to keys (strings). Values in session state are only available in the single session where it was saved.

If you have random number generation in your app, you'd likely use Session State. Here's an example where data is generated randomly at the beginning of each session. By saving this random information in Session State, each user gets different random data when they open the app but it won't keep changing on them as they interact with it. If you select different colors with the picker you'll see that the data does not get re-randomized with each rerun. (If you open the app in a new tab to start a new session, you'll see different data!)

```python
import streamlit as st
import pandas as pd
import numpy as np

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.header("Choose a datapoint color")
color = st.color_picker("Color", "#FF0000")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)
```

If you are pulling the same data for all users, you'd likely cache a function that retrieves that data. On the other hand, if you pull data specific to a user, such as querying their personal information, you may want to save that in Session State. That way, the queried data is only available in that one session.

As mentioned in [Basic concepts](/get-started/fundamentals/main-concepts#widgets), Session State is also related to widgets. Widgets are magical and handle statefulness quietly on their own. As an advanced feature however, you can manipulate the value of widgets within your code by assigning keys to them. Any key assigned to a widget becomes a key in Session State tied to the value of the widget. This can be used to manipulate the widget. After you finish understanding the basics of Streamlit, check out our guide on [Widget behavior](/develop/concepts/architecture/widget-behavior) to dig in the details if you're interested.

## Connections

As hinted above, you can use `@st.cache_resource` to cache connections. This is the most general solution which allows you to use almost any connection from any Python library. However, Streamlit also offers a convenient way to handle some of the most popular connections, like SQL! `st.connection` takes care of the caching for you so you can enjoy fewer lines of code. Getting data from your database can be as easy as:

```python
import streamlit as st

conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)
```

Of course, you may be wondering where your username and password go. Streamlit has a convenient mechanism for [Secrets management](/develop/concepts/connections/secrets-management). For now, let's just see how `st.connection` works very nicely with secrets. In your local project directory, you can save a `.streamlit/secrets.toml` file. You save your secrets in the toml file and `st.connection` just uses them! For example, if you have an app file `streamlit_app.py` your project directory may look like this:

```bash
your-LOCAL-repository/
├── .streamlit/
│   └── secrets.toml # Make sure to gitignore this!
└── streamlit_app.py
```

For the above SQL example, your `secrets.toml` file might look like the following:

```toml
[connections.my_database]
    type="sql"
    dialect="mysql"
    username="xxx"
    password="xxx"
    host="example.com" # IP or URL
    port=3306 # Port number
    database="mydb" # Database name
```

Since you don't want to commit your `secrets.toml` file to your repository, you'll need to learn how your host handles secrets when you're ready to publish your app. Each host platform may have a different way for you to pass your secrets. If you use Streamlit Community Cloud for example, each deployed app has a settings menu where you can load your secrets. After you've written an app and are ready to deploy, you can read all about how to [Deploy your app](/deploy/streamlit-community-cloud/deploy-your-app) on Community Cloud.

---

# Additional Streamlit features

Source: https://docs.streamlit.io/get-started/fundamentals/additional-features


So you've read all about Streamlit's [Basic concepts](/get-started/fundamentals/main-concepts) and gotten a taste of caching and Session State in [Advanced concepts](/get-started/fundamentals/advanced-concepts). But what about the bells and whistles? Here's a quick look at some extra features to take your app to the next level.

## Theming

Streamlit supports Light and Dark themes out of the box. Streamlit will first
check if the user viewing an app has a Light or Dark mode preference set by
their operating system and browser. If so, then that preference will be used.
Otherwise, the Light theme is applied by default.

You can also change the active theme from "⋮" → "Settings".

![Changing Themes](/images/change_theme.gif)

Want to add your own theme to an app? The "Settings" menu has a theme editor
accessible by clicking on "Edit active theme". You can use this editor to try
out different colors and see your app update live.

![Editing Themes](/images/edit_theme.gif)

When you're happy with your work, themes can be saved by
[setting config options](/develop/concepts/configuration)
in the `[theme]` config section. After you've defined a theme for your app, it
will appear as "Custom Theme" in the theme selector and will be applied by
default instead of the included Light and Dark themes.

More information about the options available when defining a theme can be found
in the [theme option documentation](/develop/concepts/configuration/theming).

<Note>

The theme editor menu is available only in local development. If you've deployed your app using
Streamlit Community Cloud, the "Edit active theme" button will no longer be displayed in the "Settings"
menu.

</Note>
<Tip>

Another way to experiment with different theme colors is to turn on the "Run on save" option, edit
your config.toml file, and watch as your app reruns with the new theme colors applied.

</Tip>

## Pages

As apps grow large, it becomes useful to organize them into multiple pages. This makes the app easier to manage as a developer and easier to navigate as a user. Streamlit provides a powerful way to create multipage apps using [`st.Page`](/develop/api-reference/navigation/st.page) and [`st.navigation`](/develop/api-reference/navigation/st.navigation). Just create your pages and connect them with navigation as follows:

1. Create an entry point script that defines and connects your pages
2. Create separate Python files for each page's content
3. Use [`st.Page`](/develop/api-reference/navigation/st.page) to define your pages and [`st.navigation`](/develop/api-reference/navigation/st.navigation) to connect them

Here's an example of a three-page app:

<details>
<summary><code>streamlit_app.py</code></summary>

```python
import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()
```

</details>
<details>
<summary><code>main_page.py</code></summary>

```python
import streamlit as st

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
```

</details>
<details>
<summary><code>page_2.py</code></summary>

```python
import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")
```

</details>
<details>
<summary><code>page_3.py</code></summary>

```python
import streamlit as st

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
```

</details>
<br/>

Now run `streamlit run streamlit_app.py` and view your shiny new multipage app! The navigation menu will automatically appear, allowing users to switch between pages.

<Image src="/images/mpa-v2-main-concepts.gif"/>

Our documentation on [Multipage apps](/develop/concepts/multipage-apps) teaches you how to add pages to your app, including how to define pages, structure and run multipage apps, and navigate between pages. Once you understand the basics, [create your first multipage app](/get-started/tutorials/create-a-multipage-app)!

## Custom components

If you can't find the right component within the Streamlit library, try out custom components to extend Streamlit's built-in functionality. Explore and browse through popular, community-created components in the [Components gallery](https://streamlit.io/components). If you dabble in frontend development, you can build your own custom component with Streamlit's [components API](/develop/concepts/custom-components/intro).

## Static file serving

As you learned in Streamlit fundamentals, Streamlit runs a server that clients connect to. That means viewers of your app don't have direct access to the files which are local to your app. Most of the time, this doesn't matter because Streamlt commands handle that for you. When you use `st.image(<path-to-image>)` your Streamlit server will access the file and handle the necessary hosting so your app viewers can see it. However, if you want a direct URL to an image or file you'll need to host it. This requires setting the correct configuration and placing your hosted files in a directory named `static`. For example, your project could look like:

```bash
your-project/
├── static/
│   └── my_hosted-image.png
└── streamlit_app.py
```

To learn more, read our guide on [Static file serving](/develop/concepts/configuration/serving-static-files).

## App testing

Good development hygiene includes testing your code. Automated testing allows you to write higher quality code, faster! Streamlit has a built-in testing framework that let's you build tests easily. Use your favorite testing framework to run your tests. We like [`pytest`](https://pypi.org/project/pytest/). When you test a Streamlit app, you simulate running the app, declare user input, and inspect the results. You can use GitHub workflows to automate your tests and get instant alerts about breaking changes. Learn more in our guide to [App testing](/develop/concepts/app-testing).</path-to-image>

---

# App model summary

Source: https://docs.streamlit.io/get-started/fundamentals/summary


Now that you know a little more about all the individual pieces, let's close
the loop and review how it works together:

1. Streamlit apps are Python scripts that run from top to bottom.
1. Every time a user opens a browser tab pointing to your app, the script is executed and a new session starts.
1. As the script executes, Streamlit draws its output live in a browser.
1. Every time a user interacts with a widget, your script is re-executed and Streamlit redraws its output in the browser.
   - The output value of that widget matches the new value during that rerun.
1. Scripts use the Streamlit cache to avoid recomputing expensive functions, so updates happen very fast.
1. Session State lets you save information that persists between reruns when you need more than a simple widget.
1. Streamlit apps can contain multiple pages, which are defined in separate `.py` files in a `pages` folder.

![The Streamlit app model](/images/app_model.png)

---

# First steps building Streamlit apps

Source: https://docs.streamlit.io/get-started/tutorials


If you've just read through our [Basic concepts](/get-started/fundamentals/main-concepts) and want to get your hands on Streamlit. Check out these tutorials. Make sure you have [installed Streamlit](/get-started/installation) so you can execute the code yourself.

<InlineCalloutContainer>
<InlineCallout bold="Create an app" color="orange-70" href="/get-started/tutorials/create-an-app" icon="description">uses the concepts learned in Fundamentals along with caching to walk through making your first app.</InlineCallout>
<InlineCallout bold="Create a multipage app" color="orange-70" href="/get-started/tutorials/create-a-multipage-app" icon="auto_stories">walks through the easy steps to add pages to your app.</InlineCallout>
</InlineCalloutContainer>

---

# Create an app

Source: https://docs.streamlit.io/get-started/tutorials/create-an-app


If you've made it this far, chances are you've [installed Streamlit](/get-started/installation) and run through the basics in [Basic concepts](/get-started/fundamentals/main-concepts) and [Advanced concepts](/get-started/fundamentals/advanced-concepts). If not, now is a good time to take a look.

The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit's UI will ask if you'd like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you're happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code.

In this guide, you're going to use Streamlit's core features to
create an interactive app; exploring a public Uber dataset for pickups and
drop-offs in New York City. When you're finished, you'll know how to fetch
and cache data, draw charts, plot information on a map, and use interactive
widgets, like a slider, to filter results.

<Tip>

If you'd like to skip ahead and see everything at once, the [complete script
is available below](#lets-put-it-all-together).

</Tip>

## Create your first app

Streamlit is more than just a way to make data apps, it’s also a community of creators that share their apps and ideas and help each other make their work better. Please come join us on the community forum. We love to hear your questions, ideas, and help you work through your bugs — stop by today!

1. The first step is to create a new Python script. Let's call it
   `uber_pickups.py`.

2. Open `uber_pickups.py` in your favorite IDE or text editor, then add these
   lines:

   ```python
   import streamlit as st
   import pandas as pd
   import numpy as np
   ```

3. Every good app has a title, so let's add one:

   ```python
   st.title('Uber pickups in NYC')
   ```

4. Now it's time to run Streamlit from the command line:

   ```bash
   streamlit run uber_pickups.py
   ```

   Running a Streamlit app is no different than any other Python script. Whenever you need to view the app, you can use this command.

   <Tip>

   Did you know you can also pass a URL to `streamlit run`? This is great when combined with GitHub Gists. For example:

   ```bash
   streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
   ```

   </Tip>

5. As usual, the app should automatically open in a new tab in your
   browser.

## Fetch some data

Now that you have an app, the next thing you'll need to do is fetch the Uber
dataset for pickups and drop-offs in New York City.

1. Let's start by writing a function to load the data. Add this code to your
   script:

   ```python
   DATE_COLUMN = 'date/time'
   DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

   def load_data(nrows):
       data = pd.read_csv(DATA_URL, nrows=nrows)
       lowercase = lambda x: str(x).lower()
       data.rename(lowercase, axis='columns', inplace=True)
       data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
       return data
   ```

   You'll notice that `load_data` is a plain old function that downloads some
   data, puts it in a Pandas dataframe, and converts the date column from text
   to datetime. The function accepts a single parameter (`nrows`), which
   specifies the number of rows that you want to load into the dataframe.

2. Now let's test the function and review the output. Below your function, add
   these lines:

   ```python
   # Create a text element and let the reader know the data is loading.
   data_load_state = st.text('Loading data...')
   # Load 10,000 rows of data into the dataframe.
   data = load_data(10000)
   # Notify the reader that the data was successfully loaded.
   data_load_state.text('Loading data...done!')
   ```

   You'll see a few buttons in the upper-right corner of your app asking if
   you'd like to rerun the app. Choose **Always rerun**, and you'll see your
   changes automatically each time you save.

Ok, that's underwhelming...

It turns out that it takes a long time to download data, and load 10,000 lines
into a dataframe. Converting the date column into datetime isn’t a quick job
either. You don’t want to reload the data each time the app is updated –
luckily Streamlit allows you to cache the data.

## Effortless caching

1. Try adding `@st.cache_data` before the `load_data` declaration:

   ```python
   @st.cache_data
   def load_data(nrows):
   ```

2. Then save the script, and Streamlit will automatically rerun your app. Since
   this is the first time you’re running the script with `@st.cache_data`, you won't
   see anything change. Let’s tweak your file a little bit more so that you can
   see the power of caching.

3. Replace the line `data_load_state.text('Loading data...done!')` with this:

   ```python
   data_load_state.text("Done! (using st.cache_data)")
   ```

4. Now save. See how the line you added appeared immediately? If you take a
   step back for a second, this is actually quite amazing. Something magical is
   happening behind the scenes, and it only takes one line of code to activate
   it.

### How's it work?

Let's take a few minutes to discuss how `@st.cache_data` actually works.

When you mark a function with Streamlit’s cache annotation, it tells Streamlit
that whenever the function is called that it should check two things:

1. The input parameters you used for the function call.
2. The code inside the function.

If this is the first time Streamlit has seen both these items, with these exact
values, and in this exact combination, it runs the function and stores the
result in a local cache. The next time the function is called, if the two
values haven't changed, then Streamlit knows it can skip executing the function
altogether. Instead, it reads the output from the local cache and passes it on
to the caller -- like magic.

"But, wait a second," you’re saying to yourself, "this sounds too good to be
true. What are the limitations of all this awesomesauce?"

Well, there are a few:

1. Streamlit will only check for changes within the current working directory.
   If you upgrade a Python library, Streamlit's cache will only notice this if
   that library is installed inside your working directory.
2. If your function is not deterministic (that is, its output depends on random
   numbers), or if it pulls data from an external time-varying source (for
   example, a live stock market ticker service) the cached value will be
   none-the-wiser.
3. Lastly, you should avoid mutating the output of a function cached with `st.cache_data` since cached
   values are stored by reference.

While these limitations are important to keep in mind, they tend not to be an
issue a surprising amount of the time. Those times, this cache is really
transformational.

<Tip>

Whenever you have a long-running computation in your code, consider
refactoring it so you can use `@st.cache_data`, if possible. Please read [Caching](/develop/concepts/architecture/caching) for more details.

</Tip>

Now that you know how caching with Streamlit works, let’s get back to the Uber
pickup data.

## Inspect the raw data

It's always a good idea to take a look at the raw data you're working with
before you start working with it. Let's add a subheader and a printout of the
raw data to the app:

```python
st.subheader('Raw data')
st.write(data)
```

In the [Basic concepts](/get-started/fundamentals/main-concepts) guide you learned that
[`st.write`](/develop/api-reference/write-magic/st.write) will render almost anything you pass
to it. In this case, you're passing in a dataframe and it's rendering as an
interactive table.

[`st.write`](/develop/api-reference/write-magic/st.write) tries to do the right thing based on
the data type of the input. If it isn't doing what you expect you can use a
specialized command like [`st.dataframe`](/develop/api-reference/data/st.dataframe)
instead. For a full list, see [API reference](/develop/api-reference).

## Draw a histogram

Now that you've had a chance to take a look at the dataset and observe what's
available, let's take things a step further and draw a histogram to see what
Uber's busiest hours are in New York City.

1. To start, let's add a subheader just below the raw data section:

   ```python
   st.subheader('Number of pickups by hour')
   ```

2. Use NumPy to generate a histogram that breaks down pickup times binned by
   hour:

   ```python
   hist_values = np.histogram(
       data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
   ```

3. Now, let's use Streamlit's
   [`st.bar_chart()`](/develop/api-reference/charts/st.bar_chart) method to draw this
   histogram.

   ```python
   st.bar_chart(hist_values)
   ```

4. Save your script. This histogram should show up in your app right away.
   After a quick review, it looks like the busiest time is 17:00 (5 P.M.).

To draw this diagram we used Streamlit's native `bar_chart()` method, but it's
important to know that Streamlit supports more complex charting libraries like
Altair, Bokeh, Plotly, Matplotlib and more. For a full list, see
[supported charting libraries](/develop/api-reference/charts).

## Plot data on a map

Using a histogram with Uber's dataset helped us determine what the busiest
times are for pickups, but what if we wanted to figure out where pickups were
concentrated throughout the city. While you could use a bar chart to show this
data, it wouldn't be easy to interpret unless you were intimately familiar with
latitudinal and longitudinal coordinates in the city. To show pickup
concentration, let's use Streamlit [`st.map()`](/develop/api-reference/charts/st.map)
function to overlay the data on a map of New York City.

1. Add a subheader for the section:

   ```python
   st.subheader('Map of all pickups')
   ```

2. Use the `st.map()` function to plot the data:

   ```python
   st.map(data)
   ```

3. Save your script. The map is fully interactive. Give it a try by panning or
   zooming in a bit.

After drawing your histogram, you determined that the busiest hour for Uber
pickups was 17:00. Let's redraw the map to show the concentration of pickups
at 17:00.

1. Locate the following code snippet:

   ```python
   st.subheader('Map of all pickups')
   st.map(data)
   ```

2. Replace it with:

   ```python
   hour_to_filter = 17
   filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
   st.subheader(f'Map of all pickups at {hour_to_filter}:00')
   st.map(filtered_data)
   ```

3. You should see the data update instantly.

To draw this map we used the [`st.map`](/develop/api-reference/charts/st.map) function that's built into Streamlit, but
if you'd like to visualize complex map data, we encourage you to take a look at
the [`st.pydeck_chart`](/develop/api-reference/charts/st.pydeck_chart).

## Filter results with a slider

In the last section, when you drew the map, the time used to filter results was
hardcoded into the script, but what if we wanted to let a reader dynamically
filter the data in real time? Using Streamlit's widgets you can. Let's add a
slider to the app with the `st.slider()` method.

1. Locate `hour_to_filter` and replace it with this code snippet:

   ```python
   hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
   ```

2. Use the slider and watch the map update in real time.

## Use a button to toggle data

Sliders are just one way to dynamically change the composition of your app.
Let's use the [`st.checkbox`](/develop/api-reference/widgets/st.checkbox) function to add a
checkbox to your app. We'll use this checkbox to show/hide the raw data
table at the top of your app.

1. Locate these lines:

   ```python
   st.subheader('Raw data')
   st.write(data)
   ```

2. Replace these lines with the following code:

   ```python
   if st.checkbox('Show raw data'):
       st.subheader('Raw data')
       st.write(data)
   ```

We're sure you've got your own ideas. When you're done with this tutorial, check out all the widgets that Streamlit exposes in our [API Reference](/develop/api-reference).

## Let's put it all together

That's it, you've made it to the end. Here's the complete script for our interactive app.

<Tip>

If you've skipped ahead, after you've created your script, the command to run
Streamlit is `streamlit run [app name]`.

</Tip>

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
```

## Share your app

After you’ve built a Streamlit app, it's time to share it! To show it off to the world you can use **Streamlit Community Cloud** to deploy, manage, and share your app for free.

It works in 3 simple steps:

1. Put your app in a public GitHub repo (and make sure it has a requirements.txt!)
2. Sign into [share.streamlit.io](https://share.streamlit.io)
3. Click 'Deploy an app' and then paste in your GitHub URL

That's it! 🎈 You now have a publicly deployed app that you can share with the world. Click to learn more about [how to use Streamlit Community Cloud](/deploy/streamlit-community-cloud).

## Get help

That's it for getting started, now you can go and build your own apps! If you
run into difficulties here are a few things you can do.

- Check out our [community forum](https://discuss.streamlit.io/) and post a question
- Quick help from command line with `streamlit help`
- Go through our [Knowledge Base](/knowledge-base) for tips, step-by-step tutorials, and articles that answer your questions about creating and deploying Streamlit apps.
- Read more documentation! Check out:
  - [Concepts](/develop/concepts) for things like caching, theming, and adding statefulness to apps.
  - [API reference](/develop/api-reference/) for examples of every Streamlit command.

---

# Create a multipage app

Source: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app


In [Additional features](/get-started/fundamentals/additional-features), we introduced multipage apps, including how to define pages, structure and run multipage apps, and navigate between pages in the user interface. You can read more details in our guide to [Multipage apps](/develop/concepts/multipage-apps)

In this guide, let’s put our understanding of multipage apps to use by converting the previous version of our `streamlit hello` app to a multipage app!

## Motivation

Before Streamlit 1.10.0, the streamlit hello command was a large single-page app. As there was no support for multiple pages, we resorted to splitting the app's content using `st.selectbox` in the sidebar to choose what content to run. The content is comprised of three demos for plotting, mapping, and dataframes.

Here's what the code and single-page app looked like:

<details>
<summary><b><code>hello.py</code></b>  (👈 Toggle to expand)</summary>
<br/>

```python
import streamlit as st

def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart)
to display geospatial data.
"""
    )

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def plotting_demo():
    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")


def data_frame_demo():
    import streamlit as st
    import pandas as pd
    import altair as alt

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
"""
    )

    @st.cache_data
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

page_names_to_funcs = {
    "—": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
```

</details>
<Cloud height="700px" name="doc-hello"/>

Notice how large the file is! Each app “page" is written as a function, and the selectbox is used to pick which page to display. As our app grows, maintaining the code requires a lot of additional overhead. Moreover, we’re limited by the `st.selectbox` UI to choose which “page" to run, we cannot customize individual page titles with `st.set_page_config`, and we’re unable to navigate between pages using URLs.

## Convert an existing app into a multipage app

Now that we've identified the limitations of a single-page app, what can we do about it? Armed with our knowledge from the previous section, we can convert the existing app to be a multipage app, of course! At a high level, we need to perform the following steps:

1. Create a new `pages` folder in the same folder where the “entrypoint file" (`hello.py`) lives
2. Rename our entrypoint file to `Hello.py` , so that the title in the sidebar is capitalized
3. Create three new files inside of `pages`:
   - `pages/1_📈_Plotting_Demo.py`
   - `pages/2_🌍_Mapping_Demo.py`
   - `pages/3_📊_DataFrame_Demo.py`
4. Move the contents of the `plotting_demo`, `mapping_demo`, and `data_frame_demo` functions into their corresponding new files from Step 3
5. Run `streamlit run Hello.py` to view your newly converted multipage app!

Now, let’s walk through each step of the process and view the corresponding changes in code.

## Create the entrypoint file

<details>
<summary><code>Hello.py</code></summary>

```python
import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
```

</details>
<br/>

We rename our entrypoint file to `Hello.py` , so that the title in the sidebar is capitalized and only the code for the intro page is included. Additionally, we’re able to customize the page title and favicon — as it appears in the browser tab with `st.set_page_config`. We can do so for each of our pages too!

<Image src="/images/mpa-hello.png"/>

Notice how the sidebar does not contain page labels as we haven’t created any pages yet.

## Create multiple pages

A few things to remember here:

1. We can change the ordering of pages in our MPA by adding numbers to the beginning of each Python file. If we add a 1 to the front of our file name, Streamlit will put that file first in the list.
2. The name of each Streamlit app is determined by the file name, so to change the app name you need to change the file name!
3. We can add some fun to our app by adding emojis to our file names that will render in our Streamlit app.
4. Each page will have its own URL, defined by the name of the file.

Check out how we do all this below! For each new page, we create a new file inside the pages folder, and add the appropriate demo code into it.

<br/>
<details>
<summary><code>pages/1_📈_Plotting_Demo.py</code></summary>

```python
import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
```

</details>
<Image src="/images/mpa-plotting-demo.png"/>
<details>
<summary><code>pages/2_🌍_Mapping_Demo.py</code></summary>

```python
import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)


@st.cache_data
def from_data_file(filename):
    url = (
        "http://raw.githubusercontent.com/streamlit/"
        "example-data/master/hello/v1/%s" % filename
    )
    return pd.read_json(url)


try:
    ALL_LAYERS = {
        "Bike Rentals": pdk.Layer(
            "HexagonLayer",
            data=from_data_file("bike_rental_stats.json"),
            get_position=["lon", "lat"],
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            extruded=True,
        ),
        "Bart Stop Exits": pdk.Layer(
            "ScatterplotLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_color=[200, 30, 0, 160],
            get_radius="[exits]",
            radius_scale=0.05,
        ),
        "Bart Stop Names": pdk.Layer(
            "TextLayer",
            data=from_data_file("bart_stop_stats.json"),
            get_position=["lon", "lat"],
            get_text="name",
            get_color=[0, 0, 0, 200],
            get_size=15,
            get_alignment_baseline="'bottom'",
        ),
        "Outbound Flow": pdk.Layer(
            "ArcLayer",
            data=from_data_file("bart_path_stats.json"),
            get_source_position=["lon", "lat"],
            get_target_position=["lon2", "lat2"],
            get_source_color=[200, 30, 0, 160],
            get_target_color=[200, 30, 0, 160],
            auto_highlight=True,
            width_scale=0.0001,
            get_width="outbound",
            width_min_pixels=3,
            width_max_pixels=30,
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": 37.76,
                    "longitude": -122.4,
                    "zoom": 11,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
```

</details>
<Image src="/images/mpa-mapping-demo.png"/>
<details>
<summary><code>pages/3_📊_DataFrame_Demo.py</code></summary>

```python
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)


@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    df = get_UN_data()
    countries = st.multiselect(
        "Choose countries", list(df.index), ["China", "United States of America"]
    )
    if not countries:
        st.error("Please select at least one country.")
    else:
        data = df.loc[countries]
        data /= 1000000.0
        st.write("### Gross Agricultural Production ($B)", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
```

</details>
<Image src="/images/mpa-dataframe-demo.png"/>

With our additional pages created, we can now put it all together in the final step below.

## Run the multipage app

To run your newly converted multipage app, run:

```bash
streamlit run Hello.py
```

That’s it! The `Hello.py` script now corresponds to the main page of your app, and other scripts that Streamlit finds in the pages folder will also be present in the new page selector that appears in the sidebar.

<Cloud height="700px" name="doc-mpa-hello"/>

## Next steps

Congratulations! 🎉 If you've read this far, chances are you've learned to create both single-page and multipage apps. Where you go from here is entirely up to your creativity! We’re excited to see what you’ll build now that adding additional pages to your apps is easier than ever. Try adding more pages to the app we've just built as an exercise. Also, stop by the forum to show off your multipage apps with the Streamlit community! 🎈

Here are a few resources to help you get started:

- Deploy your app for free on Streamlit's [Community Cloud](/deploy/streamlit-community-cloud).
- Post a question or share your multipage app on our [community forum](https://discuss.streamlit.io/c/streamlit-examples/9).
- Check out our documentation on [Multipage apps](/develop/concepts/multipage-apps).
- Read through [Concepts](/develop/concepts) for things like caching, theming, and adding statefulness to apps.
- Browse our [API reference](/develop/api-reference/) for examples of every Streamlit command.

---

# Develop

Source: https://docs.streamlit.io/develop


Get all the information you need to build beautiful, performant web apps with Streamlit!

<InlineCalloutContainer>
<InlineCallout bold="Concepts." color="indigo-70" href="/develop/concepts" icon="book">Learn how Streamlit works with in-depth guides to our execution model and features.</InlineCallout>
<InlineCallout bold="API reference." color="indigo-70" href="/develop/api-reference" icon="list">Learn about our API with function definitions and examples.</InlineCallout>
<InlineCallout bold="Tutorials." color="indigo-70" href="/develop/tutorials" icon="auto_awesome">Follow step-by-step instructions to build example apps and useful snippets.</InlineCallout>
<InlineCallout bold="Quick references." color="indigo-70" href="/develop/quick-reference" icon="bolt">Check out our quick references for easy access to convenient information like our changelog, cheat sheet, pre-release features, and roadmap.</InlineCallout>
</InlineCalloutContainer>

---

# Development concepts

Source: https://docs.streamlit.io/develop/concepts


This section gives you background on how different parts of Streamlit work.

<TileContainer>
<RefCard href="/develop/concepts/architecture" size="half">
<h5>Streamlit's architecture and execution model</h5>

Streamlit's execution model makes it easy to turn your scripts into beautiful, interactive web apps.

- Understand how to run your app.
- Understand Streamlit's execution and client-server model.
- Understand the primary tools to work with Streamlit reruns.

</RefCard>
<RefCard href="/develop/concepts/multipage-apps" size="half">
<h5>Multipage apps</h5>

Streamlit provides an automated way to build multipage apps through directory structure.

- Learn how to structure and configure your multipage app.

</RefCard>
<RefCard href="/develop/concepts/design" size="half">
<h5>App design considerations</h5>

Bring together Streamlit's architecture and execution model to design your app. Work with Streamlit commands to render dynamic and
interactic content for your users.

- Learn how to make your apps performant and easy-to-manage.
- Learn how to structure and design your project.

</RefCard>
<RefCard href="/develop/concepts/connections" size="half">
<h5>Connections and secrets</h5>

- Learn how to manage connections and secrets with Streamlit's convenient, built-in features.

</RefCard>
<RefCard href="/develop/concepts/custom-components" size="half">
<h5>Creating custom components</h5>

Custom components extend Streamlit's functionality.

- Learn how to build your own custom component.
- Learn how install a third-party component.

</RefCard>
<RefCard href="/develop/concepts/configuration" size="half">
<h5>Configuration and theming</h5>

Streamlit provides a variety options to customize and configure your app.

- Learn how to work with configuration options, including server settings, client settings, and theming.

</RefCard>
<RefCard href="/develop/concepts/app-testing" size="half">
<h5>App testing</h5>

Streamlit app testing enables developers to build and run automated tests. Bring your favorite test automation software and enjoy simple syntax to simulate user input and inspect rendered output.

</RefCard>
</TileContainer>

---

# Working with Streamlit's execution model

Source: https://docs.streamlit.io/develop/concepts/architecture


<TileContainer layout="list">
<RefCard href="/develop/concepts/architecture/run-your-app">
<h5>Run your app</h5>

Understand how to start your Streamlit app.

</RefCard>
<RefCard href="/develop/concepts/architecture/architecture">
<h5>Streamlit's architecture</h5>

Understand Streamlit's client-server architecture and related considerations.

</RefCard>
<RefCard href="/develop/concepts/architecture/app-chrome">
<h5>The app chrome</h5>

Every Streamlit app has a few widgets in the top right to help you as you develop your app and help your users as they view your app. This is called the app chrome.

</RefCard>
<RefCard href="/develop/concepts/architecture/caching">
<h5>Caching</h5>

Make your app performant by caching results to avoid unecessary recomputation with each rerun.

</RefCard>
<RefCard href="/develop/concepts/architecture/session-state">
<h5>Session State</h5>

Manage your app's statefulness with Session State.

</RefCard>
<RefCard href="/develop/concepts/architecture/forms">
<h5>Forms</h5>

Use forms to isolate user input and prevent unnecessary app reruns.

</RefCard>
<RefCard href="/develop/concepts/architecture/widget-behavior">
<h5>Widget behavior</h5>

Understand how widgets work in detail.

</RefCard>
</TileContainer>

---

# Run your Streamlit app

Source: https://docs.streamlit.io/develop/concepts/architecture/run-your-app


Working with Streamlit is simple. First you sprinkle a few Streamlit commands into a normal Python script, and then you run it. We list few ways to run your script, depending on your use case.

## Use streamlit run

Once you've created your script, say `your_script.py`, the easiest way to run it is with `streamlit run`:

```bash
streamlit run your_script.py
```

As soon as you run the script as shown above, a local Streamlit server will spin up and your app will open in a new tab in your default web browser.

### Pass arguments to your script

When passing your script some custom arguments, they must be passed after two dashes. Otherwise the arguments get interpreted as arguments to Streamlit itself:

```bash
streamlit run your_script.py [-- script args]
```

### Pass a URL to streamlit run

You can also pass a URL to `streamlit run`! This is great when your script is hosted remotely, such as a GitHub Gist. For example:

```bash
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## Run Streamlit as a Python module

Another way of running Streamlit is to run it as a Python module. This is useful when configuring an IDE like PyCharm to work with Streamlit:

```bash
# Running
python -m streamlit run your_script.py
```

```bash
# is equivalent to:
streamlit run your_script.py
```

---

# Understanding Streamlit's client-server architecture

Source: https://docs.streamlit.io/develop/concepts/architecture/architecture


Streamlit apps have a client-server structure. The Python backend of your app is the server. The frontend you view through a browser is the client. When you develop an app locally, your computer runs both the server and the client. If someone views your app across a local or global network, the server and client run on different machines. If you intend to share or deploy your app, it's important to understand this client-server structure to avoid common pitfalls.

## Python backend (server)

When you execute the command `streamlit run your_app.py`, your computer uses Python to start up a Streamlit server. This server is the brains of your app and performs the computations for all users who view your app. Whether users view your app across a local network or the internet, the Streamlit server runs on the one machine where the app was initialized with `streamlit run`. The machine running your Streamlit server is also called a host.

## Browser frontend (client)

When someone views your app through a browser, their device is a Streamlit client. When you view your app from the same computer where you are running or developing your app, then server and client are coincidentally running on the same machine. However, when users view your app across a local network or the internet, the client runs on a different machine from the server.

## Server-client impact on app design

Keep in mind the following considerations when building your Streamlit app:

- The computer running or hosting your Streamlit app is responsible for providing the compute and storage necessary to run your app for all users and must be sized appropriately to handle concurrent users.
- Your app will not have access to a user's files, directories, or OS. Your app can only work with specific files a user has uploaded to your app through a widget like `st.file_uploader`.
- If your app communicates with any peripheral devices (like cameras), you must use Streamlit commands or custom components that will access those devices _through the user's browser_ and correctly communicate between the client (frontend) and server (backend).
- If your app opens or uses any program or process outside of Python, they will run on the server. For example, you may want to use `webrowser` to open a browser for the user, but this will not work as expected when viewing your app over a network; it will open a browser on the Streamlit server, unseen by the user.
- If you use load balancing or replication in your deployment, some Streamlit features won't work without session affinity or stickiness. For more information, continue reading.

## WebSockets and session management

While most Streamlit app developers don’t need to interact directly with WebSockets, understanding their role is important for advanced deployments, custom components, or managing connections at scale.

Streamlit’s server is built on the Tornado web framework, which uses WebSockets to maintain a persistent, two-way communication channel between the client and server. This persistent connection allows the server to push real-time updates to the client and maintain session context for each user. Each browser tab or window creates its own WebSocket connection, resulting in a separate session within your app.

In large-scale or production deployments, load balancing and server replication are common. However, the way Streamlit handles sessions and local (server) files requires special consideration in these environments. When a client requests media (such as an image or audio file) via HTTP, there is no session context attached to that request. In deployments with multiple server replicas or load balancers, the HTTP request for the media file might be routed to a different server than the one handling the user’s WebSocket connection and session information. If the media file isn’t available on all replicas, you may encounter errors like `MediaFileStorageError: Bad filename`. Any command that allows the user to upload files can also be impacted and may raise HTTP status code 400.

### Session affinity or stickiness

In general, you can do one of the following to resolve or reduce this limitation:

- Enable session affinity (also known as stickiness) in your proxy. This ensures that all requests from a user’s session are handled by the same server instance.
- Convert media to a Base64 encoded data URI before passing it to a Streamlit command. This passes the media data through the WebSocket instead of using Streamlit's media storage which is accessed through HTTP requests.
- Save dynamically generated files to a stable location outside of your server replicas (e.g. S3 storage), and pass the external URLs to Streamlit commands. This avoids Streamlit's media storage.

Enabling session affinity is a general solution which resolves the limitation for both media files and uploaded files. For configuration details, consult your deployment platform’s documentation.

Using Base64 encoded data URIs or external file storage can straightforwardly resolve the limitation for media files, but are not complete solutions to resolve the limitation for file uploads. For more information, see GitHub issue [#4173](https://github.com/streamlit/streamlit/issues/4173).

---

# The app chrome

Source: https://docs.streamlit.io/develop/concepts/architecture/app-chrome


Your Streamlit app has a few widgets in the top right to help you as you develop. These widgets also help your viewers as they use your app. We call this things “the app chrome”. The chrome includes a status area, toolbar, and app menu.

Your app menu is configurable. By default, you can access developer options from the app menu when viewing an app locally or on Streamlit Community Cloud while logged into an account with administrative access. While viewing an app, click the icon in the upper-right corner to access the menu.

![App menu](/images/app-menu/app-menu-developer.png)

## Menu options

The menu is split into two sections. The upper section contains options available to all viewers and the lower section contains options for developers. Read more about [customizing this menu](#customize-the-menu) at the end of this page.

### Rerun

You can manually trigger a rerun of your app by clicking "**Rerun**" from the app menu. This rerun will not reset your session. Your widget states and values stored in [`st.session_state`](/develop/concepts/architecture/session-state) will be preserved. As a shortcut, without opening the app menu, you can rerun your app by pressing "**R**" on your keyboard (if you aren't currently focused on an input element).

### Settings

With the "**Settings**" option, you can control the appearance of your app while it is running. If viewing the app locally, you can set how your app responds to changes in your source code. See more about development flow in [Basic concepts](/get-started/fundamentals/main-concepts#development-flow). You can also force your app to appear in wide mode, even if not set within the script using [`st.set_page_config`](/develop/api-reference/configuration/st.set_page_config).

#### Theme settings

After clicking "**Settings**" from the app menu, you can choose between "**Light**", "**Dark**", or "**Use system setting**" for the app's base theme. Click "**Edit active theme**" to modify the theme, color-by-color.

<div>{{ maxWidth: '90%', margin: '0 2em 0 2em' }}&gt;
    <Image alt="Settings" src="/images/app-menu/app-menu-settings-modal.png"/>
</div>

---

# Caching overview

Source: https://docs.streamlit.io/develop/concepts/architecture/caching


Streamlit runs your script from top to bottom at every user interaction or code change. This execution model makes development super easy. But it comes with two major challenges:

1. Long-running functions run again and again, which slows down your app.
2. Objects get recreated again and again, which makes it hard to persist them across reruns or sessions.

But don't worry! Streamlit lets you tackle both issues with its built-in caching mechanism. Caching stores the results of slow function calls, so they only need to run once. This makes your app much faster and helps with persisting objects across reruns. Cached values are available to all users of your app. If you need to save results that should only be accessible within a session, use [Session State](/develop/concepts/architecture/session-state) instead.

<Collapse title="Table of contents">{true}&gt;

1. [Minimal example](#minimal-example)
2. [Basic usage](#basic-usage)
3. [Advanced usage](#advanced-usage)
4. [Migrating from st.cache](#migrating-from-stcache)

</Collapse>

---

# Add statefulness to apps

Source: https://docs.streamlit.io/develop/concepts/architecture/session-state


## What is State?

We define access to a Streamlit app in a browser tab as a **session**. For each browser tab that connects to the Streamlit server, a new session is created. Streamlit reruns your script from top to bottom every time you interact with your app. Each reruns takes place in a blank slate: no variables are shared between runs.

Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across pages inside a [multipage app](/develop/concepts/multipage-apps).

In this guide, we will illustrate the usage of **Session State** and **Callbacks** as we build a stateful Counter app.

For details on the Session State and Callbacks API, please refer to our [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state).

Also, check out this Session State basics tutorial video by Streamlit Developer Advocate Dr. Marisa Smith to get started:

<YouTube videoId="92jUAXBmZyU"/>

## Build a Counter

Let's call our script `counter.py`. It initializes a `count` variable and has a button to increment the value stored in the `count` variable:

```python
import streamlit as st

st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)
```

No matter how many times we press the **_Increment_** button in the above app, the `count` remains at 1. Let's understand why:

- Each time we press the **_Increment_** button, Streamlit reruns `counter.py` from top to bottom, and with every run, `count` gets initialized to `0` .
- Pressing **_Increment_** subsequently adds 1 to 0, thus `count=1` no matter how many times we press **_Increment_**.

As we'll see later, we can avoid this issue by storing `count` as a Session State variable. By doing so, we're indicating to Streamlit that it should maintain the value stored inside a Session State variable across app reruns.

Let's learn more about the API to use Session State.

### Initialization

The Session State API follows a field-based API, which is very similar to Python dictionaries:

```python
import streamlit as st

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports the attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### Reads and updates

Read the value of an item in Session State by passing the item to `st.write` :

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Reads
st.write(st.session_state.key)

# Outputs: value
```

Update an item in Session State by assigning it a value:

```python
import streamlit as st

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Updates
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
```

Streamlit throws an exception if an uninitialized variable is accessed:

```python
import streamlit as st

st.write(st.session_state['value'])

# Throws an exception!
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

Let's now take a look at a few examples that illustrate how to add Session State to our Counter app.

### Example 1: Add Session State

Now that we've got a hang of the Session State API, let's update our Counter app to use Session State:

```python
import streamlit as st

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Increment')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)
```

As you can see in the above example, pressing the **_Increment_** button updates the `count` each time.

### Example 2: Session State and Callbacks

Now that we've built a basic Counter app using Session State, let's move on to something a little more complex. The next example uses Callbacks with Session State.

**Callbacks**: A callback is a Python function which gets called when an input widget changes. Callbacks can be used with widgets using the parameters `on_change` (or `on_click`), `args`, and `kwargs`. The full Callbacks API can be found in our [Session State API Reference Guide](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state).

```python
import streamlit as st

st.title('Counter Example using Callbacks')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)
```

Now, pressing the **_Increment_** button updates the count each time by calling the `increment_counter()` function.

### Example 3: Use args and kwargs in Callbacks

Callbacks also support passing arguments using the `args` parameter in a widget:

```python
import streamlit as st

st.title('Counter Example using Callbacks with args')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment_value = st.number_input('Enter a value', value=0, step=1)

def increment_counter(increment_value):
    st.session_state.count += increment_value

increment = st.button('Increment', on_click=increment_counter,
    args=(increment_value, ))

st.write('Count = ', st.session_state.count)
```

Additionally, we can also use the `kwargs` parameter in a widget to pass named arguments to the callback function as shown below:

```python
import streamlit as st

st.title('Counter Example using Callbacks with kwargs')
if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter(increment_value=0):
    st.session_state.count += increment_value

def decrement_counter(decrement_value=0):
    st.session_state.count -= decrement_value

st.button('Increment', on_click=increment_counter,
	kwargs=dict(increment_value=5))

st.button('Decrement', on_click=decrement_counter,
	kwargs=dict(decrement_value=1))

st.write('Count = ', st.session_state.count)
```

### Example 4: Forms and Callbacks

Say we now want to not only increment the `count`, but also store when it was last updated. We illustrate doing this using Callbacks and `st.form`:

```python
import streamlit as st
import datetime

st.title('Counter Example')
if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count)
st.write('Last Updated = ', st.session_state.last_updated)
```

## Advanced concepts

### Session State and Widget State association

Session State provides the functionality to store variables across reruns. Widget state (i.e. the value of a widget) is also stored in a session.

For simplicity, we have _unified_ this information in one place. i.e. the Session State. This convenience feature makes it super easy to read or write to the widget's state anywhere in the app's code. Session State variables mirror the widget value using the `key` argument.

We illustrate this with the following example. Let's say we have an app with a slider to represent temperature in Celsius. We can **set** and **get** the value of the temperature widget by using the Session State API, as follows:

```python
import streamlit as st

if "celsius" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.celsius = 50.0

st.slider(
    "Temperature in Celsius",
    min_value=-100.0,
    max_value=100.0,
    key="celsius"
)

# This will get the value of the slider widget
st.write(st.session_state.celsius)
```

There is a limitation to setting widget values using the Session State API.

<Important>

Streamlit **does not allow** setting widget values via the Session State API for `st.button` and `st.file_uploader`.

</Important>

The following example will raise a `StreamlitAPIException` on trying to set the state of `st.button` via the Session State API:

```python
import streamlit as st

if 'my_button' not in st.session_state:
    st.session_state.my_button = True
    # Streamlit will raise an Exception on trying to set the state of button

st.button('Submit', key='my_button')
```

<Image alt="state-button-exception" src="/images/state_button_exception.png"/>

### Serializable Session State

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
<Warning>

When `runner.enforceSerializableSessionState` is set to `true`, Session State implicitly uses the `pickle` module, which is known to be insecure. Ensure all data saved and retrieved from Session State is trusted because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

### Caveats and limitations

Here are some limitations to keep in mind when using Session State:

- Session State exists for as long as the tab is open and connected to the Streamlit server. As soon as you close the tab, everything stored in Session State is lost.
- Session State is not persisted. If the Streamlit server crashes, then everything stored in Session State gets wiped
- For caveats and limitations with the Session State API, please see the [API limitations](/develop/api-reference/caching-and-state/st.session_state#caveats-and-limitations).

---

# Using forms

Source: https://docs.streamlit.io/develop/concepts/architecture/forms


When you don't want to rerun your script with each input made by a user, [`st.form`](/develop/api-reference/execution-flow/st.form) is here to help! Forms make it easy to batch user input into a single rerun. This guide to using forms provides examples and explains how users interact with forms.

## Example

In the following example, a user can set multiple parameters to update the map. As the user changes the parameters, the script will not rerun and the map will not update. When the user submits the form with the button labeled "**Update map**", the script reruns and the map updates.

If at any time the user clicks "**Generate new points**" which is outside of the form, the script will rerun. If the user has any unsubmitted changes within the form, these will _not_ be sent with the rerun. All changes made to a form will only be sent to the Python backend when the form itself is submitted.

<Collapse title="View source code">{false} &gt;

```python
import streamlit as st
import pandas as pd
import numpy as np

def get_data():
    df = pd.DataFrame({
        "lat": np.random.randn(200) / 50 + 37.76,
        "lon": np.random.randn(200) / 50 + -122.4,
        "team": ['A','B']*100
    })
    return df

if st.button('Generate new points'):
    st.session_state.df = get_data()
if 'df' not in st.session_state:
    st.session_state.df = get_data()
df = st.session_state.df

with st.form("my_form"):
    header = st.columns([1,2,2])
    header[0].subheader('Color')
    header[1].subheader('Opacity')
    header[2].subheader('Size')

    row1 = st.columns([1,2,2])
    colorA = row1[0].color_picker('Team A', '#0000FF')
    opacityA = row1[1].slider('A opacity', 20, 100, 50, label_visibility='hidden')
    sizeA = row1[2].slider('A size', 50, 200, 100, step=10, label_visibility='hidden')

    row2 = st.columns([1,2,2])
    colorB = row2[0].color_picker('Team B', '#FF0000')
    opacityB = row2[1].slider('B opacity', 20, 100, 50, label_visibility='hidden')
    sizeB = row2[2].slider('B size', 50, 200, 100, step=10, label_visibility='hidden')

    st.form_submit_button('Update map')

alphaA = int(opacityA*255/100)
alphaB = int(opacityB*255/100)

df['color'] = np.where(df.team=='A',colorA+f'{alphaA:02x}',colorB+f'{alphaB:02x}')
df['size'] = np.where(df.team=='A',sizeA, sizeB)

st.map(df, size='size', color='color')
```

</Collapse>

---

# Working with fragments

Source: https://docs.streamlit.io/develop/concepts/architecture/fragments


Reruns are a central part of every Streamlit app. When users interact with widgets, your script reruns from top to bottom, and your app's frontend is updated. Streamlit provides several features to help you develop your app within this execution model. Streamlit version 1.37.0 introduced fragments to allow rerunning a portion of your code instead of your full script. As your app grows larger and more complex, these fragment reruns help your app be efficient and performant. Fragments give you finer, easy-to-understand control over your app's execution flow.

Before you read about fragments, we recommend having a basic understanding of [caching](/develop/concepts/architecture/caching), [Session State](/concepts/architecture/session-state), and [forms](/develop/concepts/architecture/forms).

## Use cases for fragments

Fragments are versatile and applicable to a wide variety of circumstances. Here are just a few, common scenarios where fragments are useful:

- Your app has multiple visualizations and each one takes time to load, but you have a filter input that only updates one of them.
- You have a dynamic form that doesn't need to update the rest of your app (until the form is complete).
- You want to automatically update a single component or group of components to stream data.

## Defining and calling a fragment

Streamlit provides a decorator ([`st.fragment`](/develop/api-reference/execution-flow/st.fragment)) to turn any function into a fragment function. When you call a fragment function that contains a widget function, a user triggers a _fragment rerun_ instead of a full rerun when they interact with that fragment's widget. During a fragment rerun, only your fragment function is re-executed. Anything within the main body of your fragment is updated on the frontend, while the rest of your app remains the same. We'll describe fragments written across multiple containers later on.

Here is a basic example of defining and calling a fragment function. Just like with caching, remember to call your function after defining it.

```python
import streamlit as st

@st.fragment
def fragment_function():
    if st.button("Hi!"):
        st.write("Hi back!")

fragment_function()
```

If you want the main body of your fragment to appear in the sidebar or another container, call your fragment function inside a context manager.

```python
with st.sidebar:
    fragment_function()
```

### Fragment execution flow

Consider the following code with the explanation and diagram below.

```python
import streamlit as st

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter text")

@st.fragment()
def filter_and_file():
    cols = st.columns(2)
    cols[0].checkbox("Filter")
    cols[1].file_uploader("Upload image")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()
```

When a user interacts with an input widget inside a fragment, only the fragment reruns instead of the full script. When a user interacts with an input widget outside a fragment, the full script reruns as usual.

If you run the code above, the full script will run top to bottom on your app's initial load. If you flip the toggle button in your running app, the first fragment (`toggle_and_text()`) will rerun, redrawing the toggle and text area while leaving everything else unchanged. If you click the checkbox, the second fragment (`filter_and_file()`) will rerun and consequently redraw the checkbox and file uploader. Everything else remains unchanged. Finally, if you click the update button, the full script will rerun, and Streamlit will redraw everything.

![Diagram of fragment execution flow](/images/concepts/fragment_diagram.png)

## Fragment return values and interacting with the rest of your app

Streamlit ignores fragment return values during fragment reruns, so defining return values for your fragment functions is not recommended. Instead, if your fragment needs to share data with the rest of your app, use Session State. Fragments are just functions in your script, so they can access Session State, imported modules, and other Streamlit elements like containers. If your fragment writes to any container created outside of itself, note the following difference in behavior:

- Elements drawn in the main body of your fragment are cleared and redrawn in place during a fragment rerun. Repeated fragment reruns will not cause additional elements to appear.
- Elements drawn to containers outside the main body of fragment will not be cleared with each fragment rerun. Instead, Streamlit will draw them additively and these elements will accumulate until the next full-script rerun.
- A fragment can't draw widgets in containers outside of the main body of the fragment. Widgets can only go in the main body of a fragment.

To prevent elements from accumulating in outside containers, use [`st.empty`](/develop/api-reference/layout/st.empty) containers. For a related tutorial, see [Create a fragment across multiple containers](/develop/tutorials/execution-flow/create-a-multiple-container-fragment).

If you need to trigger a full-script rerun from inside a fragment, call [`st.rerun`](/develop/api-reference/execution-flow/st.rerun). For a related tutorial, see [Trigger a full-script rerun from inside a fragment](/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment).

## Automate fragment reruns

`st.fragment` includes a convenient `run_every` parameter that causes the fragment to rerun automatically at the specified time interval. These reruns are in addition to any reruns (fragment or full-script) triggered by your user. The automatic fragment reruns will continue even if your user is not interacting with your app. This is a great way to show a live data stream or status on a running background job, efficiently updating your rendered data and _only_ your rendered data.

```python
@st.fragment(run_every="10s")
def auto_function():
		# This will update every 10 seconds!
		df = get_latest_updates()
		st.line_chart(df)

auto_function()
```

For a related tutorial, see [Start and stop a streaming fragment](/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns).

## Compare fragments to other Streamlit features

### Fragments vs forms

Here is a comparison between fragments and forms:

- **Forms** allow users to interact with widgets without rerunning your app. Streamlit does not send user actions within a form to your app's Python backend until the form is submitted. Widgets within a form can not dynamically update other widgets (in or out of the form) in real-time.
- **Fragments** run independently from the rest of your code. As your users interact with fragment widgets, their actions are immediately processed by your app's Python backend and your fragment code is rerun. Widgets within a fragment can dynamically update other widgets within the same fragment in real-time.

A form batches user input without interaction between any widgets. A fragment immediately processes user input but limits the scope of the rerun.

### Fragments vs callbacks

Here is a comparison between fragments and callbacks:

- **Callbacks** allow you to execute a function at the beginning of a script rerun. A callback is a _single prefix_ to your script rerun.
- **Fragments** allow you to rerun a portion of your script. A fragment is a _repeatable postfix_ to your script, running each time a user interacts with a fragment widget, or automatically in sequence when `run_every` is set.

When callbacks render elements to your page, they are rendered before the rest of your page elements. When fragments render elements to your page, they are updated with each fragment rerun (unless they are written to containers outside of the fragment, in which case they accumulate there).

### Fragments vs custom components

Here is a comparison between fragments and custom components:

- **Components** are custom frontend code that can interact with the Python code, native elements, and widgets in your Streamlit app. Custom components extend what’s possible with Streamlit. They follow the normal Streamlit execution flow.
- **Fragments** are parts of your app that can rerun independently of the full app. Fragments can be composed of multiple Streamlit elements, widgets, or any Python code.

A fragment can include one or more custom components. A custom component could not easily include a fragment!

### Fragments vs caching

Here is a comparison between fragments and caching:

- **Caching:** allows you to skip over a function and return a previously computed value. When you use caching, you execute everything except the cached function (if you've already run it before).
- **Fragments:** allow you to freeze most of your app and just execute the fragment. When you use fragments, you execute only the fragment (when triggering a fragment rerun).

Caching saves you from unnecessarily running a piece of your app while the rest runs. Fragments save you from running your full app when you only want to run one piece.

## Limitations and unsupported behavior

- Fragments can't detect a change in input values. It is best to use Session State for dynamic input and output for fragment functions.
- Using caching and fragments on the same function is unsupported.
- Fragments can't render widgets in externally-created containers; widgets can only be in the main body of a fragment.

---

# Understanding widget behavior

Source: https://docs.streamlit.io/develop/concepts/architecture/widget-behavior


Widgets (like `st.button`, `st.selectbox`, and `st.text_input`) are at the heart of Streamlit apps. They are the interactive elements of Streamlit that pass information from your users into your Python code. Widgets are magical and often work how you want, but they can have surprising behavior in some situations. Understanding the different parts of a widget and the precise order in which events occur helps you achieve your desired results.

This guide covers advanced concepts about widgets. Generally, it begins with simpler concepts and increases in complexity. For most beginning users, these details won't be important to know right away. When you want to dynamically change widgets or preserve widget information between pages, these concepts will be important to understand. We recommend having a basic understanding of [Session State](/develop/api-reference/caching-and-state/st.session_state) before reading this guide.

<Collapse title="🎈 TL;DR">{false}&gt;

1. The actions of one user do not affect the widgets of any other user.
2. A widget function call returns the widget's current value, which is a simple Python type. (e.g. `st.button` returns a boolean value.)
3. Widgets return their default values on their first call before a user interacts with them.
4. A widget's identity depends on the arguments passed to the widget function. Changing a widget's label, min or max value, default value, placeholder text, help text, or key will cause it to reset.
5. If you don't call a widget function in a script run, Streamlit will delete the widget's information_including its key-value pair in Session State_. If you call the same widget function later, Streamlit treats it as a new widget.

The last two points (widget identity and widget deletion) are the most relevant when dynamically changing widgets or working with multi-page applications. This is covered in detail later in this guide: [Statefulness of widgets](#statefulness-of-widgets) and [Widget life cycle](#widget-life-cycle).

</Collapse>

---

# Multipage apps

Source: https://docs.streamlit.io/develop/concepts/multipage-apps


<TileContainer layout="list">
<RefCard href="/develop/concepts/multipage-apps/overview">
<h5>Overview of multipage apps</h5>

Streamlit provides multiple ways to define multipage apps. Understand the terminology and basic comparison between methods.

</RefCard>
<RefCard href="/develop/concepts/multipage-apps/page-and-navigation">
<h5>Define multipage apps with <code>st.Page</code> and <code>st.navigation</code></h5>

Learn about the preferred method for defining multipage apps. `st.Page` and `st.navigation` give you flexibility to organize your project directory and label your pages as you please.

</RefCard>
<RefCard href="/develop/concepts/multipage-apps/pages-directory">
<h5>Creating multipage apps using the <code>pages/</code> directory</h5>

Define your multipage apps through directory structure. Place additional Python files in a `pages/` directory alongside your entrypoint file and pages are automatically shown in a navigation widget inside your app's sidebar.

</RefCard>
<RefCard href="/develop/concepts/multipage-apps/widgets">
<h5>Working with widgets in multipage apps</h5>

Understand how widget identity is tied to pages. Learn strategies to get the behavior you want out of widgets.

</RefCard>
</TileContainer>

---

# Overview of multipage apps

Source: https://docs.streamlit.io/develop/concepts/multipage-apps/overview


Streamlit provides two built-in mechanisms for creating multipage apps. The simplest method is to use a `pages/` directory. However, the preferred and more customizable method is to use `st.navigation`.

## `st.Page` and `st.navigation`

If you want maximum flexibility in defining your multipage app, we recommend using `st.Page` and `st.navigation`. With `st.Page` you can declare any Python file or `Callable` as a page in your app. Furthermore, you can define common elements for your pages in your entrypoint file (the file you pass to `streamlit run`). With these methods, your entrypoint file becomes like a picture frame shared by all your pages.

You must include `st.navigation` in your entrypoint file to configure your app's navigation menu. This is also how your entrypoint file serves as the router between your pages.

## `pages/` directory

If you're looking for a quick and simple solution, just place a `pages/` directory next to your entrypoint file. For every Python file in your `pages/` directory, Streamlit will create an additional page for your app. Streamlit determines the page labels and URLs from the file name and automatically populates a navigation menu at the top of your app's sidebar.

```
your_working_directory/
├── pages/
│   ├── a_page.py
│   └── another_page.py
└── your_homepage.py
```

Streamlit determines the page order in navigation from the filenames. You can use numerical prefixes in the filenames to adjust page order. For more information, see [How pages are sorted in the sidebar](/develop/concepts/multipage-apps/pages-directory#how-pages-are-sorted-in-the-sidebar). If you want to customize your navigation menu with this option, you can deactivate the default navigation through [configuration](/develop/api-reference/configuration/config.toml) (`client.showSidebarNavigation = false`). Then, you can use `st.page_link` to manually contruct a custom navigation menu. With `st.page_link`, you can change the page label and icon in your navigation menu, but you can't change the URLs of your pages.

## Page terminology

A page has four identifying pieces as follows:

- **Page source**: This is a Python file or callable function with the page's source code.
- **Page label**: This is how the page is identified within the navigation menu. See <i>{{ verticalAlign: "-.25em" }} class="material-icons-sharp"&gt;looks_one</i>

---


---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-define-multipage-apps-with-stpage-and-stnavigation.md)
