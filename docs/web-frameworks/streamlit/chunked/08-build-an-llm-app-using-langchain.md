**Navigation:** [← Previous](./07-streamlitconfigtoml.md) | [Index](./index.md) | [Next →](./09-2025-release-notes.md)

---

# Build an LLM app using LangChain

Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/llm-quickstart


## OpenAI, LangChain, and Streamlit in 18 lines of code

In this tutorial, you will build a Streamlit LLM app that can generate text from a user-provided prompt. This Python app will use the LangChain framework and Streamlit. Optionally, you can deploy your app to [Streamlit Community Cloud](https://streamlit.io/cloud) when you're done.

_This tutorial is adapted from a blog post by Chanin Nantesanamat: [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/)._

<Cloud height="600px" name="doc-tutorial-llm-18-lines-of-code"/>

## Objectives

1. Get an OpenAI key from the end user.
2. Validate the user's OpenAI key.
3. Get a text prompt from the user.
4. Authenticate OpenAI with the user's key.
5. Send the user's prompt to OpenAI's API.
6. Get a response and display it.

Bonus: Deploy the app on Streamlit Community Cloud!

## Prerequisites

- Python 3.9+
- Streamlit
- LangChain
- [OpenAI API key](https://platform.openai.com/account/api-keys?ref=blog.streamlit.io)

## Setup coding environment

In your IDE (integrated coding environment), open the terminal and install the following two Python libraries:

```python
pip install streamlit langchain-openai
```

Create a `requirements.txt` file located in the root of your working directory and save these dependencies. This is necessary for deploying the app to the Streamlit Community Cloud later.

```python
streamlit
openai
langchain
```

## Building the app

The app is only 18 lines of code:

```python
import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)

```

To start, create a new Python file and save it as `streamlit_app.py` in the root of your working directory.

1. Import the necessary Python libraries.

   ```python
   import streamlit as st
   from langchain_openai.chat_models import ChatOpenAI
   ```

2. Create the app's title using `st.title`.

   ```python
   st.title("🦜🔗 Quickstart App")
   ```

3. Add a text input box for the user to enter their OpenAI API key.

   ```python
   openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
   ```

4. Define a function to authenticate to OpenAI API with the user's key, send a prompt, and get an AI-generated response. This function accepts the user's prompt as an argument and displays the AI-generated response in a blue box using `st.info`.

   ```python
   def generate_response(input_text):
       model = ChatOpenAI(temperature=0.7, api_key=openai_api_key)
       st.info(model.invoke(input_text))
   ```

5. Finally, use `st.form()` to create a text box (`st.text_area()`) for user input. When the user clicks `Submit`, the `generate-response()` function is called with the user's input as an argument.

   ```python
   with st.form("my_form"):
       text = st.text_area(
           "Enter text:",
           "What are the three key pieces of advice for learning how to code?",
       )
       submitted = st.form_submit_button("Submit")
       if not openai_api_key.startswith("sk-"):
           st.warning("Please enter your OpenAI API key!", icon="⚠")
       if submitted and openai_api_key.startswith("sk-"):
           generate_response(text)
   ```

6. Remember to save your file!
7. Return to your computer's terminal to run the app.

   ```bash
   streamlit run streamlit_app.py
   ```

## Deploying the app

To deploy the app to the Streamlit Cloud, follow these steps:

1. Create a GitHub repository for the app. Your repository should contain two files:

   ```
   your-repository/
   ├── streamlit_app.py
   └── requirements.txt
   ```

1. Go to [Streamlit Community Cloud](http://share.streamlit.io), click the `New app` button from your workspace, then specify the repository, branch, and main file path. Optionally, you can customize your app's URL by choosing a custom subdomain.
1. Click the `Deploy!` button.

Your app will now be deployed to Streamlit Community Cloud and can be accessed from around the world! 🌎

## Conclusion

Congratulations on building an LLM-powered Streamlit app in 18 lines of code! 🥳 You can use this app to generate text from any prompt that you provide. The app is limited by the capabilities of the OpenAI LLM, but it can still be used to generate some creative and interesting text.

We hope you found this tutorial helpful! Check out [more examples](https://streamlit.io/generative-ai) to see the power of Streamlit and LLM. 💖

Happy Streamlit-ing! 🎈

---

# Collect user feedback about LLM responses

Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/chat-response-feedback


A common task in a chat app is to collect user feedback about an LLM's responses. Streamlit includes `st.feedback` to conveniently collect user sentiment by displaying a group of selectable sentiment icons.

This tutorial uses Streamlit's chat commands and `st.feedback` to build a simple chat app that collects user feedback about each response.

## Applied concepts

- Use `st.chat_input` and `st.chat_message` to create a chat interface.
- Use `st.feedback` to collect user sentiment about chat responses.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.42.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of [Session State](/develop/concepts/architecture/session-state).

## Summary

In this example, you'll build a chat interface. To avoid API calls, the chat app will echo the user's prompt within a fixed response. Each chat response will be followed by a feedback widget where the user can vote "thumb up" or "thumb down." In the following code, a user can't change their feedback after it's given. If you want to let users change their rating, see the optional instructions at the end of this tutorial.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import time


def chat_stream(prompt):
    response = f'You said, "{prompt}" ...interesting.'
    for char in response:
        yield char
        time.sleep(0.02)


def save_feedback(index):
    st.session_state.history[index]["feedback"] = st.session_state[f"feedback_{index}"]


if "history" not in st.session_state:
    st.session_state.history = []

for i, message in enumerate(st.session_state.history):
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant":
            feedback = message.get("feedback", None)
            st.session_state[f"feedback_{i}"] = feedback
            st.feedback(
                "thumbs",
                key=f"feedback_{i}",
                disabled=feedback is not None,
                on_change=save_feedback,
                args=[i],
            )

if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("assistant"):
        response = st.write_stream(chat_stream(prompt))
        st.feedback(
            "thumbs",
            key=f"feedback_{len(st.session_state.history)}",
            on_change=save_feedback,
            args=[len(st.session_state.history)],
        )
    st.session_state.history.append({"role": "assistant", "content": response})
```

</Collapse>

---

# Validate and edit chat responses

Source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/validate-and-edit-chat-responses


As you train LLM models, you may want users to correct or improve chat responses. With Streamlit, you can build a chat app that lets users improve chat responses.

This tutorial uses Streamlit's chat commands to build a simple chat app that lets users modify chat responses to improve them.

## Applied concepts

- Use `st.chat_input` and `st.chat_message` to create a chat interface.
- Use Session State to manage stages of a process.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.24.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of [Session State](/develop/concepts/architecture/session-state).

## Summary

In this example, you'll build a chat interface. To avoid API calls, the app will include a generator function to simulate a chat stream object. When the simulated chat assistant responds, a function validates the response and highlights possible "errors" for the user to review. The user must accept, correct, or rewrite the response before proceeding.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import lorem
from random import randint
import time

if "stage" not in st.session_state:
    st.session_state.stage = "user"
    st.session_state.history = []
    st.session_state.pending = None
    st.session_state.validation = {}


def chat_stream():
    for i in range(randint(3, 9)):
        yield lorem.sentence() + " "
        time.sleep(0.2)


def validate(response):
    response_sentences = response.split(". ")
    response_sentences = [
        sentence.strip(". ") + "."
        for sentence in response_sentences
        if sentence.strip(". ") != ""
    ]
    validation_list = [
        True if sentence.count(" ") &gt; 4 else False for sentence in response_sentences
    ]
    return response_sentences, validation_list


def add_highlights(response_sentences, validation_list, bg="red", text="red"):
    return [
        f":{text}[:{bg}-background[" + sentence + "]]" if not is_valid else sentence
        for sentence, is_valid in zip(response_sentences, validation_list)
    ]


for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.stage == "user":
    if user_input := st.chat_input("Enter a prompt"):
        st.session_state.history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            response = st.write_stream(chat_stream())
            st.session_state.pending = response
            st.session_state.stage = "validate"
            st.rerun()

elif st.session_state.stage == "validate":
    st.chat_input("Accept, correct, or rewrite the answer above.", disabled=True)
    response_sentences, validation_list = validate(st.session_state.pending)
    highlighted_sentences = add_highlights(response_sentences, validation_list)
    with st.chat_message("assistant"):
        st.markdown(" ".join(highlighted_sentences))
        st.divider()
        cols = st.columns(3)
        if cols[0].button(
            "Correct errors", type="primary", disabled=all(validation_list)
        ):
            st.session_state.validation = {
                "sentences": response_sentences,
                "valid": validation_list,
            }
            st.session_state.stage = "correct"
            st.rerun()
        if cols[1].button("Accept"):
            st.session_state.history.append(
                {"role": "assistant", "content": st.session_state.pending}
            )
            st.session_state.pending = None
            st.session_state.validation = {}
            st.session_state.stage = "user"
            st.rerun()
        if cols[2].button("Rewrite answer", type="tertiary"):
            st.session_state.stage = "rewrite"
            st.rerun()

elif st.session_state.stage == "correct":
    st.chat_input("Accept, correct, or rewrite the answer above.", disabled=True)
    response_sentences = st.session_state.validation["sentences"]
    validation_list = st.session_state.validation["valid"]
    highlighted_sentences = add_highlights(
        response_sentences, validation_list, "gray", "gray"
    )
    if not all(validation_list):
        focus = validation_list.index(False)
        highlighted_sentences[focus] = ":red[:red" + highlighted_sentences[focus][11:]
    else:
        focus = None
    with st.chat_message("assistant"):
        st.markdown(" ".join(highlighted_sentences))
        st.divider()
        if focus is not None:
            new_sentence = st.text_input(
                "Replacement text:", value=response_sentences[focus]
            )
            cols = st.columns(2)
            if cols[0].button(
                "Update", type="primary", disabled=len(new_sentence.strip()) </Collapse>

---

# Customize your theme and configure your app

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming


<TileContainer layout="list">
<RefCard href="/develop/tutorials/configuration-and-theming/external-fonts">
<h5>Use external font files and fallbacks to customize your font</h5>

Make a new font available to your app. This tutorial uses externally hosted font files to define an alternative font and declares a built-in fallback.

</RefCard>
<RefCard href="/develop/tutorials/configuration-and-theming/static-fonts">
<h5>Use static font files to customize your font</h5>

Make a new font available to your app. This tutorial uses static font files to define an alternative font.

</RefCard>
<RefCard href="/develop/tutorials/configuration-and-theming/variable-fonts">
<h5>Use variable font files to customize your font</h5>

Make a new font available to your app. This tutorial uses variable font files to define an alternative font.

</RefCard>
</TileContainer>

---

# Use externally hosted fonts and fallbacks to customize your font

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/external-fonts


Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses variable font files and is a walkthrough of Example 3 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-1-define-an-alternative-font-with-variable-font-files). For an example that uses self-hosted variable font files, see [Use variable font files to customize your font](/develop/tutorials/configuration-and-theming/variable-fonts). For an example that uses self-hosted static font files, see [Use static font files to customize your font](/develop/tutorials/configuration-and-theming/static-fonts).

This tutorial uses inline font definitions, which were introduced in Streamlit version 1.50.0. For an older workaround, see [Use externally hosted fonts and fallbacks to customize your font (`streamlit

---

# Use externally hosted fonts and fallbacks to customize your font (`streamlit

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/external-fonts-old

---

# Use static font files to customize your font

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/static-fonts


Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses static font files and is a walkthrough of Example 2 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-2-define-an-alternative-font-with-static-font-files). For an example that uses variable font files, see [Use variable font files to customize your font](/develop/tutorials/configuration-and-theming/variable-fonts).

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.45.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of [static file serving](/develop/concepts/configuration/serving-static-files).
- You should have a basic understanding of working with font files in web development. Otherwise, start by reading [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts) up to Example 2.

## Summary

The following example uses [Tuffy](https://fonts.google.com/specimen/Tuffy) font. The font has four static font files which cover the four following weight-style pairs:

- normal normal
- normal bold
- italic normal
- italic bold

Here's a look at what you'll build:

<Collapse title="Complete config.toml file">{false}&gt;

Directory structure:

```none
your_repository/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── Tuffy-Bold.ttf
│   ├── Tuffy-BoldItalic.ttf
│   ├── Tuffy-Italic.ttf
│   └── Tuffy-Regular.ttf
└── streamlit_app.py
```

`.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Regular.ttf"
style="normal"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Bold.ttf"
style="normal"
weight=700
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-Italic.ttf"
style="italic"
weight=400
[[theme.fontFaces]]
family="tuffy"
url="app/static/Tuffy-BoldItalic.ttf"
style="italic"
weight=700

[theme]
font="tuffy"
```

`streamlit_app.py`:

```
import streamlit as st

st.write("Normal ABCabc123")
st.write("*Italic ABCabc123*")
st.write("**Bold ABCabc123**")
st.write("***Bold-italic ABCabc123***")
st.write("`Code ABCabc123`")
```

</Collapse>

---

# Use variable font files to customize your font

Source: https://docs.streamlit.io/develop/tutorials/configuration-and-theming/variable-fonts


Streamlit comes with Source Sans as the default font, but you can configure your app to use another font. This tutorial uses variable font files and is a walkthrough of Example 1 from [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts#example-1-define-an-alternative-font-with-variable-font-files). For an example that uses static font files, see [Use static font files to customize your font](/develop/tutorials/configuration-and-theming/static-fonts).

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.45.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of [static file serving](/develop/concepts/configuration/serving-static-files).
- You should have a basic understanding of working with font files in web development. Otherwise, start by reading [Customize fonts in your Streamlit app](/develop/concepts/configuration/theming-customize-fonts) up to Example 1.

## Summary

The following example uses static file serving to host Google's [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans) and [Noto Sans Mono](https://fonts.google.com/noto/specimen/Noto+Sans+Mono) fonts and configures the app to use them. Both of these fonts are defined with variable font files that include a parameterized weight. However, because font style is not parameterized, Noto Sans requires two files to define the normal and italic styles separately. Noto Sans Mono does not include a separate file for its italic style. Per [CSS rules](https://developer.mozilla.org/en-US/docs/Web/CSS/font-style#italic), because no italic style is explicitly provided, it will be simulated by skewing the normal-style font.

Here's a look at what you'll build:

<Collapse title="Complete config.toml file">{false}&gt;

Directory structure:

```none
your_repository/
├── .streamlit/
│   └── config.toml
├── static/
│   ├── NotoSans-Italic-VariableFont_wdth,wght.ttf
│   ├── NotoSans-VariableFont_wdth,wght.ttf
│   └── NotoSansMono-VariableFont_wdth,wght.ttf
└── streamlit_app.py
```

`.streamlit/config.toml`:

```toml
[server]
enableStaticServing = true

[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-Italic-VariableFont_wdth,wght.ttf"
style="italic"
[[theme.fontFaces]]
family="noto-sans"
url="app/static/NotoSans-VariableFont_wdth,wght.ttf"
style="normal"
[[theme.fontFaces]]
family="noto-mono"
url="app/static/NotoSansMono-VariableFont_wdth,wght.ttf"

[theme]
font="noto-sans"
codeFont="noto-mono"
```

`streamlit_app.py`:

```
import streamlit as st

st.write("Normal efg")
st.write("*Italic efg*")
st.write("**Bold efg**")
st.write("***Bold-italic efg***")
st.write("`Code normal efg`")
st.write("*`Code italic efg`*")
st.write("**`Code bold efg`**")
st.write("***`Code bold-italic efg`***")
```

</Collapse>

---

# Connect Streamlit to data sources

Source: https://docs.streamlit.io/develop/tutorials/databases


These step-by-step guides demonstrate how to connect Streamlit apps to various databases  APIs.
They use Streamlit's [Secrets management](/develop/concepts/connections/secrets-management) and
[caching](/develop/concepts/architecture/caching) to provide secure and fast data access.

<DataSourcesContainer>
<DataSourcesCard href="/develop/tutorials/databases/aws-s3">
<Image>alt="screenshot" src="/images/databases/s3.png" /&gt;

<h5>AWS S3</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/bigquery">
<Image>alt="screenshot" src="/images/databases/bigquery.png" /&gt;

<h5>BigQuery</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="https://blog.streamlit.io/streamlit-firestore/">
<Image>alt="screenshot" src="/images/databases/firestore.png" /&gt;

<h5>Firestore (blog)</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/gcs">
<Image>alt="screenshot" src="/images/databases/gcs.png" /&gt;

<h5>Google Cloud Storage</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/mssql">
<Image>alt="screenshot" src="/images/databases/mssql.png" /&gt;

<h5>Microsoft SQL Server</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/mongodb">
<Image>alt="screenshot" src="/images/databases/mongodb.png" /&gt;

<h5>MongoDB</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/mysql">
<Image>alt="screenshot" src="/images/databases/mysql.png" /&gt;

<h5>MySQL</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/neon">
<Image>alt="screenshot" src="/images/databases/neon-logo.png" /&gt;

<h5>Neon</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/postgresql">
<Image>alt="screenshot" src="/images/databases/postgresql.png" /&gt;

<h5>PostgreSQL</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/private-gsheet">
<Image>alt="screenshot" src="/images/databases/gsheet.png" /&gt;

<h5>Private Google Sheet</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/public-gsheet">
<Image>alt="screenshot" src="/images/databases/gsheet.png" /&gt;

<h5>Public Google Sheet</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/snowflake">
<Image>alt="screenshot" src="/images/databases/snowflake.png" /&gt;

<h5>Snowflake</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/supabase">
<Image>alt="screenshot" src="/images/databases/supabase.png" /&gt;

<h5>Supabase</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/tableau">
<Image>alt="screenshot" src="/images/databases/tableau.png" /&gt;

<h5>Tableau</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/tidb">
<Image>alt="screenshot" src="/images/databases/tidb.png" /&gt;

<h5>TiDB</h5>
</Image></DataSourcesCard>
<DataSourcesCard href="/develop/tutorials/databases/tigergraph">
<Image>alt="screenshot" src="/images/databases/tigergraph.png" /&gt;

<h5>TigerGraph</h5>
</Image></DataSourcesCard>
</DataSourcesContainer>

---

# Connect Streamlit to AWS S3

Source: https://docs.streamlit.io/develop/tutorials/databases/aws-s3


## Introduction

This guide explains how to securely access files on AWS S3 from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [s3fs](https://github.com/dask/s3fs) library and optionally Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create an S3 bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#create-access-keys).

</Note>

First, [sign up for AWS](https://aws.amazon.com/) or log in. Go to the [S3 console](https://s3.console.aws.amazon.com/s3/home) and create a new bucket:

<Flex>
<Image alt="AWS screenshot 1" src="/images/databases/aws-1.png"/>
<Image alt="AWS screenshot 2" src="/images/databases/aws-2.png"/>
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="AWS screenshot 3" src="/images/databases/aws-3.png"/>
<Image alt="AWS screenshot 4" src="/images/databases/aws-4.png"/>
</Flex>

And note down the "AWS Region" for later. In this example, it's `us-east-1`, but it may differ for you.

Next, upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Create access keys

Go to the [AWS console](https://console.aws.amazon.com/), create access keys as shown below and copy the "Access Key ID" and "Secret Access Key":

<Flex>
<Image alt="AWS screenshot 5" src="/images/databases/aws-5.png"/>
<Image alt="AWS screenshot 6" src="/images/databases/aws-6.png"/>
</Flex>
<Tip>

Access keys created as a root user have wide-ranging permissions. In order to make your AWS account
more secure, you should consider creating an IAM account with restricted permissions and using its
access keys. More information [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).

</Tip>

## Set up your AWS credentials locally

Streamlit FilesConnection and s3fs will read and use your existing [AWS credentials and configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) if available - such as from an `~/.aws/credentials` file or environment variables.

If you don't already have this set up, or plan to host the app on Streamlit Community Cloud, you should specify the credentials from a file `.streamlit/secrets.toml` in your app's root directory or your home directory. Create this file if it doesn't exist yet and add to it the access key ID, access key secret, and the AWS default region you noted down earlier, as shown below:

```toml
# .streamlit/secrets.toml
AWS_ACCESS_KEY_ID = "xxx"
AWS_SECRET_ACCESS_KEY = "xxx"
AWS_DEFAULT_REGION = "xxx"
```

<Important>

Be sure to replace `xxx` above with the values you noted down earlier, and add this file to `.gitignore` so you don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

To host your app on Streamlit Community Cloud, you will need to pass your credentials to your deployed app via secrets. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` above into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add FilesConnection and s3fs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [s3fs](https://github.com/dask/s3fs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
s3fs==x.x.x
st-files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables, where `s3fs` searches for them by default.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("testbucket-jrieke/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

---

# Connect Streamlit to Google BigQuery

Source: https://docs.streamlit.io/develop/tutorials/databases/bigquery


## Introduction

This guide explains how to securely access a BigQuery database from Streamlit Community Cloud. It uses the
[google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) library and
Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a BigQuery database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#enable-the-bigquery-api).

</Note>

For this example, we will use one of the [sample datasets](https://cloud.google.com/bigquery/public-data#sample_tables) from BigQuery (namely the `shakespeare` table). If you want to create a new dataset instead, follow [Google's quickstart guide](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui).

## Enable the BigQuery API

Programmatic access to BigQuery is controlled through [Google Cloud Platform](https://cloud.google.com). Create an account or sign in and head over to the [APIs  Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). As shown below, search for the BigQuery API and enable it:

<Flex>
<Image alt="Bigquery screenshot 1" src="/images/databases/big-query-1.png"/>
<Image alt="Bigquery screenshot 2" src="/images/databases/big-query-2.png"/>
<Image alt="Bigquery screenshot 3" src="/images/databases/big-query-3.png"/>
</Flex>

## Create a service account  key file

To use the BigQuery API from Streamlit Community Cloud, you need a Google Cloud Platform service account (a special account type for programmatic data access). Go to the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page and create an account with the **Viewer** permission (this will let the account access data but not change it):

<Flex>
<Image alt="Bigquery screenshot 4" src="/images/databases/big-query-4.png"/>
<Image alt="Bigquery screenshot 5" src="/images/databases/big-query-5.png"/>
<Image alt="Bigquery screenshot 6" src="/images/databases/big-query-6.png"/>
</Flex>
<Note>

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

<Flex>
<Image alt="Bigquery screenshot 7" src="/images/databases/big-query-7.png"/>
<Image alt="Bigquery screenshot 8" src="/images/databases/big-query-8.png"/>
<Image alt="Bigquery screenshot 9" src="/images/databases/big-query-9.png"/>
</Flex>

## Add the key file to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root
directory. Create this file if it doesn't exist yet and add the content of the key file you just
downloaded to it as shown below:

```toml
# .streamlit/secrets.toml

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add google-cloud-bigquery to your requirements file

Add the [google-cloud-bigquery](https://googleapis.dev/python/bigquery/latest/index.html) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version want installed):

```bash
# requirements.txt
google-cloud-bigquery==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the query if you don't use the sample table.

```python
# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# Print results.
st.write("Some wise words from Shakespeare:")
for row in rows:
    st.write("✍️ " + row['word'])
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

Alternatively, you can use pandas to read from BigQuery right into a dataframe! Follow all the above steps, install the [pandas-gbq](https://pandas-gbq.readthedocs.io/en/latest/index.html) library (don't forget to add it to `requirements.txt`!), and call `pandas.read_gbq(query, credentials=credentials)`. More info [in the pandas docs](https://pandas.pydata.org/docs/reference/api/pandas.read_gbq.html).

If everything worked out (and you used the sample table), your app should look like this:

![Final app screenshot](/images/databases/big-query-10.png)

---

# Connect Streamlit to Google Cloud Storage

Source: https://docs.streamlit.io/develop/tutorials/databases/gcs


## Introduction

This guide explains how to securely access files on Google Cloud Storage from Streamlit Community Cloud. It uses [Streamlit FilesConnection](https://github.com/streamlit/files-connection), the [gcsfs](https://github.com/fsspec/gcsfs) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a Google Cloud Storage bucket and add a file

<Note>

If you already have a bucket that you want to use, feel free
to [skip to the next step](#enable-the-google-cloud-storage-api).

</Note>

First, [sign up for Google Cloud Platform](https://console.cloud.google.com/) or log in. Go to the [Google Cloud Storage console](https://console.cloud.google.com/storage/) and create a new bucket.

<Flex>
<Image alt="GCS screenshot 1" src="/images/databases/gcs-1.png"/>
<Image alt="GCS screenshot 2" src="/images/databases/gcs-2.png"/>
</Flex>

Navigate to the upload section of your new bucket:

<Flex>
<Image alt="GCS screenshot 3" src="/images/databases/gcs-3.png"/>
<Image alt="GCS screenshot 4" src="/images/databases/gcs-4.png"/>
</Flex>

And upload the following CSV file, which contains some example data:

<Download href="/images/databases/myfile.csv">myfile.csv</Download>

## Enable the Google Cloud Storage API

The Google Cloud Storage API is [enabled by default](https://cloud.google.com/service-usage/docs/enabled-service#default) when you create a project through the Google Cloud Console or CLI. Feel free to [skip to the next step](#create-a-service-account-and-key-file).

If you do need to enable the API for programmatic access in your project, head over to the [APIs  Services dashboard](https://console.cloud.google.com/apis/dashboard) (select or create a project if asked). Search for the Cloud Storage API and enable it. The screenshot below has a blue "Manage" button and indicates the "API is enabled" which means no further action needs to be taken. This is very likely what you have since the API is enabled by default. However, if that is not what you see and you have an "Enable" button, you'll need to enable the API:

<Flex>
<Image alt="GCS screenshot 5" src="/images/databases/gcs-5.png"/>
<Image alt="GCS screenshot 6" src="/images/databases/gcs-6.png"/>
<Image alt="GCS screenshot 7" src="/images/databases/gcs-7.png"/>
</Flex>

## Create a service account and key file

To use the Google Cloud Storage API from Streamlit, you need a Google Cloud Platform service account (a special type for programmatic data access). Go to the Service Accounts page and create an account with <b>Viewer</b> permission.

<Flex>
<Image alt="GCS screenshot 8" src="/images/databases/gcs-8.png"/>
<Image alt="GCS screenshot 9" src="/images/databases/gcs-9.png"/>
<Image alt="GCS screenshot 10" src="/images/databases/gcs-10.png"/>
</Flex>
<Note>

If the button **CREATE SERVICE ACCOUNT** is gray, you don't have the correct permissions. Ask the
admin of your Google Cloud project for help.

</Note>

After clicking **DONE**, you should be back on the service accounts overview. Create a JSON key file for the new account and download it:

<Flex>
<Image alt="GCS screenshot 11" src="/images/databases/gcs-11.png"/>
<Image alt="GCS screenshot 12" src="/images/databases/gcs-12.png"/>
<Image alt="GCS screenshot 13" src="/images/databases/gcs-13.png"/>
</Flex>

## Add the key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the access key to it as shown below:

```toml
# .streamlit/secrets.toml

[connections.gcs]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "xxx"
client_email = "xxx"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add FilesConnection and gcsfs to your requirements file

Add the [FilesConnection](https://github.com/streamlit/files-connection) and [gcsfs](https://github.com/fsspec/gcsfs) packages to your `requirements.txt` file, preferably pinning the versions (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
gcsfs==x.x.x
st-files-connection
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your bucket and file. Note that Streamlit automatically turns the access keys from your secrets file into environment variables.

```python
# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, result caching and retries. By default, `read()` results are cached without expiring. In this case, we set `ttl=600` to ensure the file contents is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example file given above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

---

# Connect Streamlit to Microsoft SQL Server

Source: https://docs.streamlit.io/develop/tutorials/databases/mssql


## Introduction

This guide explains how to securely access a **_remote_** Microsoft SQL Server database from Streamlit Community Cloud. It uses the [pyodbc](https://github.com/mkleehammer/pyodbc/wiki) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create an SQL Server database

<Note>

If you already have a remote database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow the Microsoft documentation to install [SQL Server](https://docs.microsoft.com/en-gb/sql/sql-server/?view=sql-server-ver15) and the `sqlcmd` [Utility](https://docs.microsoft.com/en-gb/sql/tools/sqlcmd-utility?view=sql-server-ver15). They have detailed installation guides on how to:

- [Install SQL Server on Windows](https://docs.microsoft.com/en-gb/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver15)
- [Install on Red Hat Enterprise Linux](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-red-hat?view=sql-server-ver15)
- [Install on SUSE Linux Enterprise Server](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-suse?view=sql-server-ver15)
- [Install on Ubuntu](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15)
- [Run on Docker](https://docs.microsoft.com/en-gb/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15)
- [Provision a SQL VM in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sql/provision-sql-server-linux-virtual-machine?toc=/sql/toc/toc.json)

Once you have SQL Server installed, note down your SQL Server name, username, and password during setup.

## Connect locally

If you are connecting locally, use `sqlcmd` to connect to your new local SQL Server instance.

1. In your terminal, run the following command:

   ```bash
   sqlcmd -S localhost -U SA -P '<YourPassword>'
   ```

   As you are connecting locally, the SQL Server name is `localhost`, the username is `SA`, and the password is the one you provided during the SA account setup.

2. You should see a **sqlcmd** command prompt `1&gt;`, if successful.

3. If you run into a connection failure, review Microsoft's connection troubleshooting recommendations for your OS ([Linux](https://docs.microsoft.com/en-gb/sql/linux/sql-server-linux-troubleshooting-guide?view=sql-server-ver15#connection)  [Windows](https://docs.microsoft.com/en-gb/sql/linux/sql-server-linux-troubleshooting-guide?view=sql-server-ver15#connection)).

<Tip>

When connecting remotely, the SQL Server name is the machine name or IP address. You might also need to open the SQL Server TCP port (default 1433) on your firewall.

</Tip>

### Create a SQL Server database

By now, you have SQL Server running and have connected to it with `sqlcmd`! 🥳 Let's put it to use by creating a database containing a table with some example values.

1. From the `sqlcmd` command prompt, run the following Transact-SQL command to create a test database `mydb`:

   ```sql
   CREATE DATABASE mydb
   ```

2. To execute the above command, type `GO` on a new line:

   ```sql
   GO
   ```

### Insert some data

Next create a new table, `mytable`, in the `mydb` database with three columns and two rows.

1. Switch to the new `mydb` database:

   ```sql
   USE mydb
   ```

2. Create a new table with the following schema:

   ```sql
   CREATE TABLE mytable (name varchar(80), pet varchar(80))
   ```

3. Insert some data into the table:

   ```sql
   INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird')
   ```

4. Type `GO` to execute the above commands:

   ```sql
   GO
   ```

To end your **sqlcmd** session, type `QUIT` on a new line.

### Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the SQL Server name, database name, username, and password as shown below:

```toml
# .streamlit/secrets.toml

server = "localhost"
database = "mydb"
username = "SA"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **server**, **database**, **username**, and **password** with those of your _remote_ SQL Server!

And add this file to `.gitignore` and don't commit it to your GitHub repo.

</Important>

## Copy your app secrets to Streamlit Community Cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add pyodbc to your requirements file

To connect to SQL Server _locally_ with Streamlit, you need to `pip install pyodbc`, in addition to the Microsoft ODBC driver you installed during the SQL Server installation.

On _Streamlit Cloud_, we have built-in support for SQL Server. On popular demand, we directly added SQL Server tools including the ODBC drivers and the executables `sqlcmd` and `bcp` to the container image for Cloud apps, so you don't need to install them.

All you need to do is add the [`pyodbc`](https://github.com/mkleehammer/pyodbc) Python package to your `requirements.txt` file, and you're ready to go! 🎈

```bash
# requirements.txt
pyodbc==x.x.x
```

Replace `x.x.x` ☝️ with the version of pyodbc you want installed on Cloud.

<Note>

At this time, Streamlit Community Cloud does not support Azure Active Directory authentication. We will update this tutorial when we add support for Azure Active Directory.

</Note>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)</YourPassword>

---

# Connect Streamlit to MongoDB

Source: https://docs.streamlit.io/develop/tutorials/databases/mongodb


## Introduction

This guide explains how to securely access a **_remote_** MongoDB database from Streamlit Community Cloud. It uses the [PyMongo](https://github.com/mongodb/mongo-python-driver) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a MongoDB Database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow the official tutorials to [install MongoDB](https://docs.mongodb.com/guides/server/install/), [set up authentication](https://docs.mongodb.com/guides/server/auth/) (note down the username and password!), and [connect to the MongoDB instance](https://docs.mongodb.com/guides/server/drivers/). Once you are connected, open the `mongo` shell and enter the following two commands to create a collection with some example values:

```sql
use mydb
db.mycollection.insertMany([{"name" : "Mary", "pet": "dog"}, {"name" : "John", "pet": "cat"}, {"name" : "Robert", "pet": "bird"}])
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the database information as shown below:

```toml
# .streamlit/secrets.toml

[mongo]
host = "localhost"
port = 27017
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **username**, and **password** with those of your _remote_ MongoDB database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add PyMongo to your requirements file

Add the [PyMongo](https://github.com/mongodb/mongo-python-driver) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
pymongo==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your database and collection.

```python
# streamlit_app.py

import streamlit as st
import pymongo

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

---

# Connect Streamlit to MySQL

Source: https://docs.streamlit.io/develop/tutorials/databases/mysql


## Introduction

This guide explains how to securely access a **_remote_** MySQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version &gt;= 1.28**, when `st.connection` was added.

## Create a MySQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://dev.mysql.com/doc/mysql-getting-started/en/) to install MySQL and start the MySQL server (note down the username and password!). Once your MySQL server is up and running, connect to it with the `mysql` client and enter the following commands to create a database and a table with some example values:

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name varchar(80),
    pet varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add the database name, user, and password of your MySQL server as shown below:

```toml
# .streamlit/secrets.toml

[connections.mysql]
dialect = "mysql"
host = "localhost"
port = 3306
database = "xxx"
username = "xxx"
password = "xxx"
query = { charset = "xxx" }
```

If you use `query` when defining your connection, you must use `streamlit&gt;=1.35.0`.

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your _remote_ MySQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

---

# Connect Streamlit to Neon

Source: https://docs.streamlit.io/develop/tutorials/databases/neon


## Introduction

This guide explains how to securely access a [Neon database](https://neon.tech/) from Streamlit. Neon is a fully managed serverless PostgreSQL database that separates storage and compute to offer features such as instant branching and automatic scaling.

### Prerequisites

- The following packages must be installed in your Python environment:

  ```txt
  streamlit&gt;=1.28
  psycopg2-binary&gt;=2.9.6
  sqlalchemy&gt;=2.0.0
  ```

    <Note>
        You may use `psycopg2` instead of `psycopg2-binary`. However, building Psycopg requires a few prerequisites (like a C compiler). To use `psycopg2` on Community Cloud, you must include `libpq-dev` in a [`packages.txt`](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies#apt-get-dependencies) file in the root of your repository. `psycopg2-binary` is a stand-alone package that is practical for testing and development.
    </Note>

- You must have a Neon account.
- You should have a basic understanding of [`st.connection`](/develop/api-reference/connections/st.connection) and [Secrets management](/develop/concepts/connections/secrets-management).

## Create a Neon project

If you already have a Neon project that you want to use, you can [skip to the next step](#add-neon-connection-string-to-your-local-app-secrets).

1. Log in to the Neon console and navigate to the [Projects](https://console.neon.tech/app/projects) section.
1. If you see a prompt to enter your project name, skip to the next step. Otherwise, click the "**New Project**" button to create a new project.
1. Enter "Streamlit-Neon" for your project name, accept the othe default settings, and click "**Create Project**."

   After Neon creates your project with a ready-to-use `neondb` database, you will be redirected to your project's Quickstart.

1. Click on "**SQL Editor**" from the left sidebar.
1. Replace the text in the input area with the following code and click "**Run**" to add sample data to your project.

   ```sql
   CREATE TABLE home (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100),
       pet VARCHAR(100)
   );

   INSERT INTO home (name, pet)
   VALUES
       ('Mary', 'dog'),
       ('John', 'cat'),
       ('Robert', 'bird');
   ```

## Add the Neon connection string to your local app secrets

1. Within your Neon project, click "**Dashboard**" in the left sidebar.
1. Within the "Connection Details" tile, locate your database connection string. It should look similar to this:

   ```bash
   postgresql://neondb_owner:xxxxxxxxxxxx@ep-adjective-noun-xxxxxxxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```

1. If you do not already have a `.streamlit/secrets.toml` file in your app's root directory, create an empty secrets file.
1. Copy your connection string and add it to your app's `.streamlit/secrets.toml` file as follows:

   ```toml
   # .streamlit/secrets.toml

   [connections.neon]
   url="postgresql://neondb_owner:xxxxxxxxxxxx@ep-adjective-noun-xxxxxxxx.us-east-2.aws.neon.tech/neondb?sslmode=require"
   ```

   <Important>
       Add this file to `.gitignore` and don't commit it to your GitHub repo!
   </Important>

## Write your Streamlit app

1. Copy the code below to your Streamlit app and save it.

   ```python
   # streamlit_app.py

   import streamlit as st

   # Initialize connection.
   conn = st.connection("neon", type="sql")

   # Perform query.
   df = conn.query('SELECT * FROM home;', ttl="10m")

   # Print results.
   for row in df.itertuples():
       st.write(f"{row.name} has a :{row.pet}:")
   ```

   The `st.connection` object above handles secrets retrieval, setup, query caching and retries.

   By default, `query()` results are cached without expiring. Setting the `ttl` parameter to `"10m"` ensures the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

1. Run your Streamlit app.

   ```bash
   streamlit run streamlit_app.py
   ```

   If everything worked out (and you used the example table we created above), your app should look like this:

   ![Finished app screenshot](/images/databases/streamlit-app.png)

## Connecting to a Neon database from Community Cloud

This tutorial assumes a local Streamlit app, but you can also connect to a Neon database from apps hosted on Community Cloud. The additional steps are:

- Add a [`requirements.txt`](/deploy/streamlit-community-cloud/deploy-your-app/app-dependencies) file to your repo. Include all the packages listed in [Prequisites](#prerequisites) and any other dependencies.
- [Add your secrets](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management#deploy-an-app-and-set-up-secrets) to your app in Community Cloud.

---

# Connect Streamlit to PostgreSQL

Source: https://docs.streamlit.io/develop/tutorials/databases/postgresql


## Introduction

This guide explains how to securely access a **_remote_** PostgreSQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version &gt;= 1.28**, when `st.connection` was added.

## Create a PostgreSQL database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

First, follow [this tutorial](https://www.tutorialspoint.com/postgresql/postgresql_environment.htm) to install PostgreSQL and create a database (note down the database name, username, and password!). Open the SQL Shell (`psql`) and enter the following two commands to create a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the name, user, and password of your database as shown below:

```toml
# .streamlit/secrets.toml

[connections.postgresql]
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "xxx"
username = "xxx"
password = "xxx"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **port**, **database**, **username**, and **password** with those of your _remote_ PostgreSQL database!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [psycopg2-binary](https://www.psycopg.org/) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
psycopg2-binary==x.x.x
sqlalchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM mytable;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

---

# Connect Streamlit to a private Google Sheet

Source: https://docs.streamlit.io/develop/tutorials/databases/private-gsheet


## Introduction

This guide explains how to securely access a private Google Sheet from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

If you are fine with enabling link sharing for your Google Sheet (i.e. everyone with the link can view it), the guide [Connect Streamlit to a public Google Sheet](/develop/tutorials/databases/public-gsheet) shows a simpler method of doing this. If your Sheet contains sensitive information and you cannot enable link sharing, keep on reading.

### Prerequisites

This tutorial requires `streamlit&gt;=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet

If you already have a Sheet that you want to use, you can [skip to the next step](#enable-the-sheets-api).

Create a spreadsheet with this example data.

<div>{{ maxWidth: '200px', margin: 'auto' }}&gt;

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

---

# Connect Streamlit to a public Google Sheet

Source: https://docs.streamlit.io/develop/tutorials/databases/public-gsheet


## Introduction

This guide explains how to securely access a public Google Sheet from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit GSheetsConnection](https://github.com/streamlit/gsheets-connection), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

This method requires you to enable link sharing for your Google Sheet. While the sharing link will not appear in your code (and actually acts as sort of a password!), someone with the link can get all the data in the Sheet. If you don't want this, follow the (more complicated) guide to [Connect Streamlit to a private Google Sheet](private-gsheet).

### Prerequisites

This tutorial requires `streamlit&gt;=1.28` and `st-gsheets-connection` in your Python environment.

## Create a Google Sheet and turn on link sharing

If you already have a Sheet that you want to access, you can [skip to the next step](#add-the-sheets-url-to-your-local-app-secrets). See Google's documentation on how to [share spreadsheets](https://support.google.com/docs/answer/9331169?hl=en#6.1) for more information.

Create a spreadsheet with this example data and create a share link. The link should have "Anyone with the link" set as a "Viewer."

<div>{{ maxWidth: '200px', margin: 'auto' }}&gt;

| name   | pet  |
| :----- | :--- |
| Mary   | dog  |
| John   | cat  |
| Robert | bird |

</div>

---

# Connect Streamlit to Snowflake

Source: https://docs.streamlit.io/develop/tutorials/databases/snowflake


## Introduction

This guide explains how to securely access a Snowflake database from Streamlit. It uses [st.connection](/develop/api-reference/connections/st.connection), the [Snowpark library](https://docs.snowflake.com/en/developer-guide/snowpark/python/index), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

### Prerequisites

- The following packages must be installed in your Python environment:

  ```txt
  streamlit&gt;=1.28
  snowflake-snowpark-python&gt;=0.9.0
  snowflake-connector-python&gt;=2.8.0
  ```

    <Note>
        Use the correct version of Python required by `snowflake-snowpark-python`. For example, if you use `snowflake-snowpark-python==1.23.0`, you must use Python version \&gt;=3.8, \</Note>

---

# Connect Streamlit to Supabase

Source: https://docs.streamlit.io/develop/tutorials/databases/supabase


## Introduction

This guide explains how to securely access a Supabase instance from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main) (a community-built connection developed by [@SiddhantSadangi](https://github.com/SiddhantSadangi)) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). Supabase is the open source Firebase alternative and is based on PostgreSQL.

<Note>

Community-built connections, such as the [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main), extend and build on the `st.connection` interface and make it easier than ever to build Streamlit apps with a wide variety of data sources. These type of connections work exactly the same as [the ones built into Streamlit](/develop/api-reference/connections) and have access to all the same capabilities.

</Note>

## Sign in to Supabase and create a project

First, head over to [Supabase](https://app.supabase.io/) and sign up for a free account using your GitHub.

<Flex>
<Image caption="Sign in with GitHub" src="/images/databases/supabase-1.png"/>
<Image caption="Authorize Supabase" src="/images/databases/supabase-2.png"/>
</Flex>

Once you're signed in, you can create a project.

<Flex>
<Image caption="Your Supabase account" src="/images/databases/supabase-3.png"/>
<Image caption="Create a new project" src="/images/databases/supabase-4.png"/>
</Flex>

Your screen should look like this once your project has been created:

<Image src="/images/databases/supabase-5.png"/>
<Important>

Make sure to note down your Project API Key and Project URL highlighted in the above screenshot. ☝️

You will need these to connect to your Supabase instance from Streamlit.

</Important>

## Create a Supabase database

Now that you have a project, you can create a database and populate it with some sample data. To do so, click on the **SQL editor** button on the same project page, followed by the **New query** button in the SQL editor.

<Flex>
<Image caption="Open the SQL editor" src="/images/databases/supabase-6.png"/>
<Image caption="Create a new query" src="/images/databases/supabase-7.png"/>
</Flex>

In the SQL editor, enter the following queries to create a database and a table with some example values:

```sql
CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

Click **Run** to execute the queries. To verify that the queries were executed successfully, click on the **Table Editor** button on the left menu, followed by your newly created table `mytable`.

<Flex>
<Image caption="Write and run your queries" src="/images/databases/supabase-8.png"/>
<Image caption="View your table in the Table Editor" src="/images/databases/supabase-9.png"/>
</Flex>

With your Supabase database created, you can now connect to it from Streamlit!

### Add Supabase Project URL and API key to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

```toml
# .streamlit/secrets.toml

[connections.supabase]
SUPABASE_URL = "xxxx"
SUPABASE_KEY = "xxxx"
```

Replace `xxxx` above with your Project URL and API key from [Step 1](/develop/tutorials/databases/supabase#sign-in-to-supabase-and-create-a-project).

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add st-supabase-connection to your requirements file

Add the [`st-supabase-connection`](https://pypi.org/project/st-supabase-connection/) community-built connection library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
st-supabase-connection==x.x.x
```

<Tip>

We've used the `st-supabase-connection` library here in combination with `st.connection` to benefit from the ease of setting up the data connection, managing your credentials, and Streamlit's caching capabilities that native and community-built connections provide.

You can however still directly use the [Supabase Python Client Library](https://pypi.org/project/supabase/) library if you prefer, but you'll need to write more code to set up the connection and cache the results. See [Using the Supabase Python Client Library](/develop/tutorials/databases/supabase#using-the-supabase-python-client-library) below for an example.

</Tip>

## Write your Streamlit app

Copy the code below to your Streamlit app and run it.

```python
# streamlit_app.py

import streamlit as st
from st_supabase_connection import SupabaseConnection

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="mytable", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")

```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/supabase-10.png)

As Supabase uses PostgresSQL under the hood, you can also connect to Supabase by using the connection string Supabase provides under Settings &gt; Databases. From there, you can refer to the [PostgresSQL tutorial](/develop/tutorials/databases/postgresql) to connect to your database.

## Using the Supabase Python Client Library

If you prefer to use the [Supabase Python Client Library](https://pypi.org/project/supabase/) directly, you can do so by following the steps below.

1. Add your Supabase Project URL and API key to your local app secrets:

   Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the SUPABASE_URL and SUPABASE_KEY here:

   ```toml
   # .streamlit/secrets.toml

   SUPABASE_URL = "xxxx"
   SUPABASE_KEY = "xxxx"
   ```

2. Add `supabase` to your requirements file:

   Add the [`supabase`](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

   ```bash
   # requirements.txt
   supabase==x.x.x
   ```

3. Write your Streamlit app:

   Copy the code below to your Streamlit app and run it.

   ```python
   # streamlit_app.py

   import streamlit as st
   from supabase import create_client, Client

   # Initialize connection.
   # Uses st.cache_resource to only run once.
   @st.cache_resource
   def init_connection():
       url = st.secrets["SUPABASE_URL"]
       key = st.secrets["SUPABASE_KEY"]
       return create_client(url, key)

   supabase = init_connection()

   # Perform query.
   # Uses st.cache_data to only rerun when the query changes or after 10 min.
   @st.cache_data(ttl=600)
   def run_query():
       return supabase.table("mytable").select("*").execute()

   rows = run_query()

   # Print results.
   for row in rows.data:
       st.write(f"{row['name']} has a :{row['pet']}:")
   ```

   See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

---

# Connect Streamlit to Tableau

Source: https://docs.streamlit.io/develop/tutorials/databases/tableau


## Introduction

This guide explains how to securely access data on Tableau from Streamlit Community Cloud. It uses the [tableauserverclient](https://tableau.github.io/server-client-python/#) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a Tableau site

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#create-personal-access-tokens).

</Note>

For simplicity, we are using the cloud version of Tableau here but this guide works equally well for self-hosted deployments. First, sign up for [Tableau Online](https://www.tableau.com/products/cloud-bi) or log in. Create a workbook or run one of the example workbooks under "Dashboard Starters".

![Tableau screenshot 1](/images/databases/tableau-1.png)

## Create personal access tokens

While the Tableau API allows authentication via username and password, you should use [personal access tokens](https://help.tableau.com/current/server/en-us/security_personal_access_tokens.htm) for a production app.

Go to your [Tableau Online homepage](https://online.tableau.com/), create an access token and note down the token name and secret.

<Flex>
<Image alt="Tableau screenshot 2" src="/images/databases/tableau-2.png"/>
<Image alt="Tableau screenshot 3" src="/images/databases/tableau-3.png"/>
</Flex>
<Note>

Personal access tokens will expire if not used after 15 consecutive days.

</Note>

## Add token to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add your token, the site name you created during setup, and the URL of your Tableau server like below:

```toml
# .streamlit/secrets.toml

[tableau]
token_name = "xxx"
token_secret = "xxx"
server_url = "https://abc01.online.tableau.com/"
site_id = "streamlitexample"  # in your site's URL behind the server_url
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add tableauserverclient to your requirements file

Add the [tableauserverclient](https://tableau.github.io/server-client-python/#) package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
tableauserverclient==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Note that this code just shows a few options of data you can get – explore the [tableauserverclient](https://tableau.github.io/server-client-python/#) library to find more!

```python
# streamlit_app.py

import streamlit as st
import tableauserverclient as TSC


# Set up connection.
tableau_auth = TSC.PersonalAccessTokenAuth(
    st.secrets["tableau"]["token_name"],
    st.secrets["tableau"]["personal_access_token"],
    st.secrets["tableau"]["site_id"],
)
server = TSC.Server(st.secrets["tableau"]["server_url"], use_server_version=True)


# Get various data.
# Explore the tableauserverclient library for more options.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    with server.auth.sign_in(tableau_auth):

        # Get all workbooks.
        workbooks, pagination_item = server.workbooks.get()
        workbooks_names = [w.name for w in workbooks]

        # Get views for first workbook.
        server.workbooks.populate_views(workbooks[0])
        views_names = [v.name for v in workbooks[0].views]

        # Get image  CSV for first view of first workbook.
        view_item = workbooks[0].views[0]
        server.views.populate_image(view_item)
        server.views.populate_csv(view_item)
        view_name = view_item.name
        view_image = view_item.image
        # `view_item.csv` is a list of binary objects, convert to str.
        view_csv = b"".join(view_item.csv).decode("utf-8")

        return workbooks_names, views_names, view_name, view_image, view_csv

workbooks_names, views_names, view_name, view_image, view_csv = run_query()


# Print results.
st.subheader("📓 Workbooks")
st.write("Found the following workbooks:", ", ".join(workbooks_names))

st.subheader("👁️ Views")
st.write(
    f"Workbook *{workbooks_names[0]}* has the following views:",
    ", ".join(views_names),
)

st.subheader("🖼️ Image")
st.write(f"Here's what view *{view_name}* looks like:")
st.image(view_image, width=300)

st.subheader("📊 Data")
st.write(f"And here's the data for view *{view_name}*:")
st.write(pd.read_csv(StringIO(view_csv)))
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out, your app should look like this (can differ based on your workbooks):

![Tableau screenshot 4](/images/databases/tableau-4.png)

---

# Connect Streamlit to TiDB

Source: https://docs.streamlit.io/develop/tutorials/databases/tidb


## Introduction

This guide explains how to securely access a **_remote_** TiDB database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version &gt;= 1.28**, when `st.connection` was added.

[TiDB](https://www.pingcap.com/tidb/) is an open-source, MySQL-compatible database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads. TiDB introducs a [built-in vector search](https://www.pingcap.com/ai/) to the SQL database family, enabling support for your AI applications without requiring a new database or additional technical stacks. [TiDB Cloud](https://tidb.cloud/) is a fully managed cloud database service that simplifies the deployment and management of TiDB databases for developers.

## Sign in to TiDB Cloud and create a cluster

First, head over to [TiDB Cloud](https://tidbcloud.com/free-trial) and sign up for a free account, using either Google, GitHub, Microsoft or E-mail:

![Sign up TiDB Cloud](/images/databases/tidb-1.png)

Once you've signed in, you will already have a TiDB cluster:

![List clusters](/images/databases/tidb-2.png)

You can create more clusters if you want to. Click the cluster name to enter cluster overview page:

![Cluster overview](/images/databases/tidb-3.png)

Then click **Connect** to easily get the connection arguments to access the cluster. On the popup, click **Generate Password** to set the password.

![Get connection arguments](/images/databases/tidb-4.png)

<Important>

Make sure to note down the password. It won't be available on TiDB Cloud after this step.

</Important>

## Create a TiDB database

<Note>

If you already have a database that you want to use, feel free
to [skip to the next step](#add-username-and-password-to-your-local-app-secrets).

</Note>

Once your TiDB cluster is up and running, connect to it with the `mysql` client(or with **SQL Editor** tab on the console) and enter the following commands to create a database and a table with some example values:

```sql
CREATE DATABASE pets;

USE pets;

CREATE TABLE mytable (
    name            varchar(80),
    pet             varchar(80)
);

INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');
```

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add host, username and password of your TiDB cluster as shown below:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
```

<Important>

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **username** and **password** with those of your _remote_ TiDB cluster!

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('tidb', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connect with PyMySQL

Other than [mysqlclient](https://github.com/PyMySQL/mysqlclient), [PyMySQL](https://github.com/PyMySQL/PyMySQL) is another popular MySQL Python client. To use PyMySQL, first you need to adapt your requirements file:

```bash
# requirements.txt
PyMySQL==x.x.x
SQLAlchemy==x.x.x
```

Then adapt your secrets file:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
driver = "pymysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}
```</path_to_CA_store></TiDB_cluster_password></TiDB_cluster_user></TiDB_cluster_host></TiDB_cluster_password></TiDB_cluster_user></TiDB_cluster_host>

---

# Connect Streamlit to TigerGraph

Source: https://docs.streamlit.io/develop/tutorials/databases/tigergraph


## Introduction

This guide explains how to securely access a TigerGraph database from Streamlit Community Cloud. It uses the [pyTigerGraph](https://pytigergraph.github.io/pyTigerGraph/GettingStarted/) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create a TigerGraph Cloud Database

First, follow the official tutorials to create a TigerGraph instance in TigerGraph Cloud, either as a [blog](https://www.tigergraph.com/blog/getting-started-with-tigergraph-3-0/) or a [video](https://www.youtube.com/watch?v=NtNW2e8MfCQ). Note your username, password, and subdomain.

For this tutorial, we will be using the COVID-19 starter kit. When setting up your solution, select the “COVID-19 Analysis" option.

![TG_Cloud_COVID19](/images/databases/tigergraph-1.png)

Once it is started, ensure your data is downloaded and queries are installed.

![TG_Cloud_Schema](/images/databases/tigergraph-2.png)

## Add username and password to your local app secrets

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app’s root directory. Create this file if it doesn’t exist yet and add your TigerGraph Cloud instance username, password, graph name, and subdomain as shown below:

```toml
# .streamlit/secrets.toml

[tigergraph]
host = "https://xxx.i.tgcloud.io/"
username = "xxx"
password = "xxx"
graphname = "xxx"
```

<Important>

Add this file to `.gitignore` and don't commit it to your GitHub repo!

</Important>

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on Edit Secrets. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add PyTigerGraph to your requirements file

Add the pyTigerGraph package to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
pyTigerGraph==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt the name of your graph and query.

```python
# streamlit_app.py

import streamlit as st
import pyTigerGraph as tg

# Initialize connection.
conn = tg.TigerGraphConnection(**st.secrets["tigergraph"])
conn.apiToken = conn.getToken(conn.createSecret())

# Pull data from the graph by running the "mostDirectInfections" query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    most_infections = conn.runInstalledQuery("mostDirectInfections")[0]["Answer"][0]
    return most_infections["v_id"], most_infections["attributes"]

items = get_data()

# Print results.
st.title(f"Patient {items[0]} has the most direct infections")
for key, val in items[1].items():
    st.write(f"Patient {items[0]}'s {key} is {val}.")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example data we created above), your app should look like this:

![Final_App](/images/databases/tigergraph-3.png)

---

# Work with Streamlit elements

Source: https://docs.streamlit.io/develop/tutorials/elements


<TileContainer layout="list">
<RefCard href="/develop/tutorials/elements/annotate-an-altair-chart">
<h5>Annotate an Altair chart</h5>

Add annotations to an Altair chart.

</RefCard>
<RefCard href="/develop/tutorials/elements/dataframe-row-selections">
<h5>Get row selections from dataframes</h5>

Work with user row-selections in dataframes.

</RefCard>
</TileContainer>

---

# Annotate an Altair chart

Source: https://docs.streamlit.io/develop/tutorials/elements/annotate-an-altair-chart


Altair allows you to annotate your charts with text, images, and emojis. You can do this by overlaying two charts to create a [layered chart](https://altair-viz.github.io/user_guide/compound_charts.html#layered-charts).

## Applied concepts

- Use layered charts in Altair to create annotations.

## Prerequisites

- This tutorial requires the following Python libraries:

  ```txt
  streamlit
  altair&gt;=4.0.0
  vega_datasets
  ```

- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of the Vega-Altair charting library.

## Summary

In this example, you will create a time-series chart to track the evolution of stock prices. The chart will have two layers: a data layer and an
annotation layer. Each layer is an `altair.Chart` object. You will combine the two charts with the `+` opterator to create a layered chart.

Within the data layer, you'll add a multi-line tooltip to show information about datapoints. To learn more about multi-line tooltips, see this [example](https://altair-viz.github.io/gallery/multiline_tooltip.html) in Vega-Altair's documentation. You'll add another tooltip to the annotation layer.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data


@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source


stock_data = get_data()

hover = alt.selection_single(
    fields=["date"],
    nearest=True,
    on="mouseover",
    empty="none",
)

lines = (
    alt.Chart(stock_data, title="Evolution of stock prices")
    .mark_line()
    .encode(
        x="date",
        y="price",
        color="symbol",
    )
)

points = lines.transform_filter(hover).mark_circle(size=65)

tooltips = (
    alt.Chart(stock_data)
    .mark_rule()
    .encode(
        x="yearmonthdate(date)",
        y="price",
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=[
            alt.Tooltip("date", title="Date"),
            alt.Tooltip("price", title="Price (USD)"),
        ],
    )
    .add_selection(hover)
)

data_layer = lines + points + tooltips

ANNOTATIONS = [
    ("Sep 01, 2007", 450, "🙂", "Something's going well for GOOG  AAPL."),
    ("Nov 01, 2008", 220, "🙂", "The market is recovering."),
    ("Dec 01, 2007", 750, "😱", "Something's going wrong for GOOG  AAPL."),
    ("Dec 01, 2009", 680, "😱", "A hiccup for GOOG."),
]
annotations_df = pd.DataFrame(
    ANNOTATIONS, columns=["date", "price", "marker", "description"]
)
annotations_df.date = pd.to_datetime(annotations_df.date)

annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=20, dx=-10, dy=0, align="left")
    .encode(x="date:T", y=alt.Y("price:Q"), text="marker", tooltip="description")
)

combined_chart = data_layer + annotation_layer
st.altair_chart(combined_chart, use_container_width=True)
```

</Collapse>

---

# Get dataframe row-selections from users

Source: https://docs.streamlit.io/develop/tutorials/elements/dataframe-row-selections


Streamlit offers two commands for rendering beautiful, interactive dataframes in your app. If you need users to edit data, add rows, or delete rows, use `st.data_editor`. If you don't want users to change the data in your dataframe, use `st.dataframe`. Users can sort and search through data rendered with `st.dataframe`. Additionally, you can activate selections to work with users' row and column selections.

This tutorial uses row selections, which were introduced in Streamlit version 1.35.0. For an older workaround using `st.data_editor`, see [Get dataframe row-selections (`streamlit

---

# Get dataframe row-selections from users (`streamlit

Source: https://docs.streamlit.io/develop/tutorials/elements/dataframe-row-selections-old

---

# Use core features to work with Streamlit's execution model

Source: https://docs.streamlit.io/develop/tutorials/execution-flow


## Fragments

<TileContainer layout="list">
<RefCard href="/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment">
<h5>Trigger a full-script rerun from inside a fragment</h5>

Call `st.rerun` from inside a fragment to trigger a full-script rerun when a condition is met.

</RefCard>
<RefCard href="/develop/tutorials/execution-flow/create-a-multiple-container-fragment">
<h5>Create a fragment across multiple containers</h5>

Use a fragment to write to multiple containers across your app.

</RefCard>
<RefCard href="/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns">
<h5>Start and stop a streaming fragment</h5>

Use a fragment to live-stream data. Use a button to start and stop the live-streaming.

</RefCard>
</TileContainer>

---

# Trigger a full-script rerun from inside a fragment

Source: https://docs.streamlit.io/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment


Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. When a user interacts with a widget inside a fragment, only the fragment reruns. Sometimes, you may want to trigger a full-script rerun from inside a fragment. To do this, call [`st.rerun`](/develop/api-reference/execution-flow/st.rerun) inside the fragment.

## Applied concepts

- Use a fragment to rerun part or all of your app, depending on user input.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.37.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.rerun`.

## Summary

In this example, you'll build an app to display sales data. The app has two sets of elements that depend on a date selection. One set of elements displays information for the selected day. The other set of elements displays information for the associated month. If the user changes days within a month, Streamlit only needs to update the first set of elements. If the user selects a day in a different month, Streamlit needs to update all the elements.

You'll collect the day-specific elements into a fragment to avoid rerunning the full app when a user changes days within the same month. If you want to jump ahead to the fragment function definition, see [Build a function to show daily sales data](#build-a-function-to-show-daily-sales-data).

<div>{{ maxWidth: '60%', margin: 'auto' }}&gt;
<Image alt="Execution flow of example Streamlit app showing daily sales on the left and monthly sales on the right" src="/images/tutorials/fragment-rerun-tutorial-execution-flow.png"/>
</div>

---

# Create a fragment across multiple containers

Source: https://docs.streamlit.io/develop/tutorials/execution-flow/create-a-multiple-container-fragment


Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. If your fragment doesn't write to outside containers, Streamlit will clear and redraw all the fragment elements with each fragment rerun. However, if your fragment _does_ write elements to outside containers, Streamlit will not clear those elements during a fragment rerun. Instead, those elements accumulate with each fragment rerun until the next full-script rerun. If you want a fragment to update multiple containers in your app, use [`st.empty()`](/develop/api-reference/layout/st.empty) containers to prevent accumulating elements.

## Applied concepts

- Use fragments to run two independent processes separately.
- Distribute a fragment across multiple containers.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.37.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.empty()`.

## Summary

In this toy example, you'll build an app with six containers. Three containers will have orange cats. The other three containers will have black cats. You'll have three buttons in the sidebar: "**Herd the black cats**," "**Herd the orange cats**," and "**Herd all the cats**." Since herding cats is slow, you'll use fragments to help Streamlit run the associated processes efficiently. You'll create two fragments, one for the black cats and one for the orange cats. Since the buttons will be in the sidebar and the fragments will update containers in the main body, you'll use a trick with `st.empty()` to ensure you don't end up with too many cats in your app (if it's even possible to have too many cats). 😻

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import time

st.title("Cats!")

row1 = st.columns(3)
row2 = st.columns(3)

grid = [col.container(height=200) for col in row1 + row2]
safe_grid = [card.empty() for card in grid]


def black_cats():
    time.sleep(1)
    st.title("🐈‍⬛ 🐈‍⬛")
    st.markdown("🐾 🐾 🐾 🐾")


def orange_cats():
    time.sleep(1)
    st.title("🐈 🐈")
    st.markdown("🐾 🐾 🐾 🐾")


@st.fragment
def herd_black_cats(card_a, card_b, card_c):
    st.button("Herd the black cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        black_cats()
    with container_b:
        black_cats()
    with container_c:
        black_cats()


@st.fragment
def herd_orange_cats(card_a, card_b, card_c):
    st.button("Herd the orange cats")
    container_a = card_a.container()
    container_b = card_b.container()
    container_c = card_c.container()
    with container_a:
        orange_cats()
    with container_b:
        orange_cats()
    with container_c:
        orange_cats()


with st.sidebar:
    herd_black_cats(grid[0].empty(), grid[2].empty(), grid[4].empty())
    herd_orange_cats(grid[1].empty(), grid[3].empty(), grid[5].empty())
    st.button("Herd all the cats")
```

</Collapse>

---

# Start and stop a streaming fragment

Source: https://docs.streamlit.io/develop/tutorials/execution-flow/start-and-stop-fragment-auto-reruns


Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. Additionally, you can tell Streamlit to rerun a fragment at a set time interval. This is great for streaming data or monitoring processes. You may want the user to start and stop this live streaming. To do this, programmatically set the `run_every` parameter for your fragment.

## Applied concepts

- Use a fragment to stream live data.
- Start and stop a fragment from automatically rerunning.

## Prerequisites

- This tutorial requires the following version of Streamlit:

  ```text
  streamlit&gt;=1.37.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments.

## Summary

In this example, you'll build an app that streams two data series in a line chart. Your app will gather recent data on the first load of a session and statically display the line chart. Two buttons in the sidebar will allow users to start and stop data streaming to update the chart in real time. You'll use a fragment to manage the frequency and scope of the live updates.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def get_recent_data(last_timestamp):
    """Generate and return data from last timestamp to now, at most 60 seconds."""
    now = datetime.now()
    if now - last_timestamp &gt; timedelta(seconds=60):
        last_timestamp = now - timedelta(seconds=60)
    sample_time = timedelta(seconds=0.5)  # time between data points
    next_timestamp = last_timestamp + sample_time
    timestamps = np.arange(next_timestamp, now, sample_time)
    sample_values = np.random.randn(len(timestamps), 2)

    data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])
    return data


if "data" not in st.session_state:
    st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))

if "stream" not in st.session_state:
    st.session_state.stream = False


def toggle_streaming():
    st.session_state.stream = not st.session_state.stream


st.title("Data feed")
st.sidebar.slider(
    "Check for updates every: (seconds)", 0.5, 5.0, value=1.0, key="run_every"
)
st.sidebar.button(
    "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
)
st.sidebar.button(
    "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
)

if st.session_state.stream is True:
    run_every = st.session_state.run_every
else:
    run_every = None


@st.fragment(run_every=run_every)
def show_latest_data():
    last_timestamp = st.session_state.data.index[-1]
    st.session_state.data = pd.concat(
        [st.session_state.data, get_recent_data(last_timestamp)]
    )
    st.session_state.data = st.session_state.data[-100:]
    st.line_chart(st.session_state.data)


show_latest_data()
```

</Collapse>

---

# Build multipage apps

Source: https://docs.streamlit.io/develop/tutorials/multipage


<TileContainer layout="list">
<RefCard href="/develop/tutorials/multipage/dynamic-navigation">
<h5>Create a dynamic navigation menu</h5>

Create a dynamic, user-dependant navigation menu with `st.navigation`.

</RefCard>
</TileContainer>

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

  ```
  streamlit&gt;=1.36.0
  ```

- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of `st.navigation` and `st.Page`.

## Summary

In this example, we'll build a dynamic navigation menu for a multipage app that depends on the current user's role. You'll abstract away the use of username and credentials to simplify the example. Instead, you'll use a selectbox to let users choose a role and log in.

The entrypoint file, `streamlit_app.py` will handle user authentication. The other pages will be stubs representing account management (`settings.py`) and specific pages associated to three roles: Requester, Responder, and Admin. Requesters can access the account and request pages. Responders can access the account and respond pages. Admins can access all pages.

Here's a look at what we'll build:

<Collapse title="Complete code">{false}&gt;

**Directory structure:**

```
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
```

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
```

</Collapse>

---

# Build a custom navigation menu with `st.page_link`

Source: https://docs.streamlit.io/develop/tutorials/multipage/st.page_link-nav


Streamlit lets you build custom navigation menus and elements with `st.page_link`. Introduced in Streamlit version 1.31.0, `st.page_link` can link to other pages in your multipage app or to external sites. When linked to another page in your app, `st.page_link` will show a highlight effect to indicate the current page. When combined with the [`client.showSidebarNavigation`](/develop/concepts/configuration#client) configuration option, you can build sleek, dynamic navigation in your app.

## Prerequisites

Create a new working directory in your development environment. We'll call this directory `your-repository`.

## Summary

In this example, we'll build a dynamic navigation menu for a multipage app that depends on the current user's role. We've abstracted away the use of username and creditials to simplify the example. Instead, we'll use a selectbox on the main page of the app to switch between roles. Session State will carry this selection between pages. The app will have a main page (`app.py`) which serves as the abstracted log-in page. There will be three additional pages which will be hidden or accessible, depending on the current role. The file structure will be as follows:

```
your-repository/
├── .streamlit/
│   └── config.toml
├── pages/
│   ├── admin.py
│   ├── super-admin.py
│   └── user.py
├── menu.py
└── app.py
```

Here's a look at what we'll build:

<Cloud height="400px" name="doc-custom-navigation"/>

## Build the example

### Hide the default sidebar navigation

When creating a custom navigation menu, you need to hide the default sidebar navigation using `client.showSidebarNavigation`. Add the following `.streamlit/config.toml` file to your working directory:

```toml
[client]
showSidebarNavigation = false
```

### Create a menu function

You can write different menu logic for different pages or you can create a single menu function to call on multiple pages. In this example, we'll use the same menu logic on all pages, including a redirect to the main page when a user isn't logged in. We'll build a few helper functions to do this.

- `menu_with_redirect()` checks if a user is logged in, then either redirects them to the main page or renders the menu.
- `menu()` will call the correct helper function to render the menu based on whether the user is logged in or not.
- `authenticated_menu()` will display a menu based on an authenticated user's role.
- `unauthenticated_menu()` will display a menu for unauthenticated users.

We'll call `menu()` on the main page and call `menu_with_redirect()` on the other pages. `st.session_state.role` will store the current selected role. If this value does not exist or is set to `None`, then the user is not logged in. Otherwise, it will hold the user's role as a string: `"user"`, `"admin"`, or `"super-admin"`.

Add the following `menu.py` file to your working directory. (We'll describe the functions in more detail below.)

```python
import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()
```

Let's take a closer look at `authenticated_menu()`. When this function is called, `st.session_state.role` exists and has a value other than `None`.

```python
def authenticated_menu():
    # Show a navigation menu for authenticated users
```

The first two pages in the navigation menu are available to all users. Since we know a user is logged in when this function is called, we'll use the label "Switch accounts" for the main page. (If you don't use the `label` parameter, the page name will be derived from the file name like it is with the default sidebar navigation.)

```python
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
```

We only want to show the next two pages to admins. Furthermore, we've chosen to disablebut not hidethe super-admin page when the admin user is not a super-admin. We do this using the `disabled` parameter. (`disabled=True` when the role is not `"super-admin"`.)

```
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )
```

It's that simple! `unauthenticated_menu()` will only show a link to the main page of the app with the label "Log in." `menu()` does a simple inspection of `st.session_state.role` to switch between the two menu-rendering functions. Finally, `menu_with_redirect()` extends `menu()` to redirect users to `app.py` if they aren't logged in.

<Tip>

If you want to include emojis in your page labels, you can use the `icon` parameter. There's no need to include emojis in your file name or the `label` parameter.

</Tip>

### Create the main file of your app

The main `app.py` file will serve as a pseudo-login page. The user can choose a role from the `st.selectbox` widget. A few bits of logic will save that role into Session State to preserve it while navigating between pageseven when returning to `app.py`.

Add the following `app.py` file to your working directory:

```python
import streamlit as st
from menu import menu

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!
```

### Add other pages to your app

Add the following `pages/user.py` file:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("This page is available to all users")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

Session State resets if a user manually navigates to a page by URL. Therefore, if a user tries to access an admin page in this example, Session State will be cleared, and they will be redirected to the main page as an unauthenicated user. However, it's still good practice to include a check of the role at the top of each restricted page. You can use `st.stop` to halt an app if a role is not whitelisted.

`pages/admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to all admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

`pages/super-admin.py`:

```python
import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("This page is available to super-admins")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
```

As noted above, the redirect in `menu_with_redirect()` will prevent a user from ever seeing the warning messages on the admin pages. If you want to see the warning, just add another `st.page_link("pages/admin.py")` button at the bottom of `app.py` so you can navigate to the admin page after selecting the "user" role. 😉

---

# Quick reference

Source: https://docs.streamlit.io/develop/quick-reference


<TileContainer layout="list">
<RefCard href="/develop/quick-reference/cheat-sheet">
<h5>Cheatsheet</h5>

A dense list of Streamlit commands with example syntax.

</RefCard>
<RefCard href="/develop/quick-reference/release-notes">
<h5>Release notes</h5>

See how Streamlit has changed with each new version.

</RefCard>
<RefCard href="/develop/quick-reference/prerelease">
<h5>Pre-release features</h5>

Understand how we introduce new features and how you can get your hands on them sooner!

</RefCard>
<RefCard href="https://roadmap.streamlit.app/">
<h5>Roadmap</h5>

Get a sneak peek at what we have scheduled for the next year.

</RefCard>
</TileContainer>

---

# Streamlit API cheat sheet

Source: https://docs.streamlit.io/develop/quick-reference/cheat-sheet


This is a summary of the docs for the latest version of Streamlit, [v1.51.0](https://pypi.org/project/streamlit/1.51.0/).

<Masonry>
<CodeTile>

#### Install  Import

```python
pip install streamlit

streamlit run first_app.py

# Import convention
&gt;&gt;&gt; import streamlit as st
```

</CodeTile>
<CodeTile>

#### Pre-release features

```python
pip uninstall streamlit
pip install streamlit-nightly --upgrade
```

Learn more about [experimental features](advanced-features/prerelease#experimental-features)

</CodeTile>
<CodeTile>

#### Command line

```python
streamlit cache clear
streamlit config show
streamlit docs
streamlit hello
streamlit help
streamlit init
streamlit run streamlit_app.py
streamlit version
```

</CodeTile>
</Masonry>
<Masonry>
<CodeTile>

#### Magic commands

```python
# Magic commands implicitly
# call st.write().
"_This_ is some **Markdown**"
my_variable
"dataframe:", my_data_frame

```

</CodeTile>
<CodeTile>

#### Display text

```python
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is </CodeTile></Masonry>

---

# Release notes

Source: https://docs.streamlit.io/develop/quick-reference/release-notes


This page lists highlights, bug fixes, and known issues for the latest release of Streamlit. If you're looking for information about nightly releases or experimental features, see [Pre-release features](/develop/quick-reference/prerelease).

## Upgrade Streamlit

<Tip>

To upgrade to the latest version of Streamlit, run:

```bash
pip install --upgrade streamlit
```

</Tip>

## **Version 1.51.0 (latest)**

_Release date: October 29, 2025_

**Highlights**

- 🧩 Announcing [custom components](/develop/api-reference/custom-components/st.components.v2.component), version 2! Easily create frameless custom UI with bidirectional data flow.
- 🌗 Introducing custom [light and dark theme](/develop/concepts/configuration/theming) configuration! You can simultaneously define custom light and dark themes in your app.
- 🎨 Announcing [reusable themes](/develop/api-reference/configuration/config.toml#theme)! You can define a theme in a sharable file and use it as a base in other themes.
- 💫 Introducing [`st.space`](/develop/api-reference/layout/st.space) for adding vertical and horizontal spaces in your app.

**Notable Changes**

- 🔗 New configuration options, `theme.codeTextColor` and `theme.linkColor`, let you configure the color of code and link text.
- 📊 [`ProgressColumn`](/develop/api-reference/data/st.column_config/st.column_config.progresscolumn) has a new `color` parameter.
- 🌈 You can set `color="auto"` in [`MultiselectColumn`](/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn) to inherit colors from `theme.chartCategoricalColors`.
- 📌 `MultiselectColumn` has a `pinned` parameter to match other column types.
- ⭐ You can set a `default` value for [`st.feedback`](/develop/api-reference/widgets/st.feedback) ([#12578](https://github.com/streamlit/streamlit/pull/12578), [#9469](https://github.com/streamlit/streamlit/issues/9469)). Thanks, [andreasntr](https://github.com/andreasntr)!
- 👆 [`st.write_stream`](/develop/api-reference/write-magic/st.write_stream) has a `cursor` parameter to set a custom cursor for the typewriter effect.
- 🍿 [`st.popover`](/develop/api-reference/layout/st.popover) has a `type` parameter to match `st.button` styling options.
- 🔑 To prevent widgets from resetting when you change a parameter, widgets are transitioning to an identity based only on their keys (if provided). The following widgets use only their key for their identity:
  - `st.color_picker`
  - `st.segmented_control`
  - `st.radio`
  - `st.audio_input`
  - `st.slider`
  - `st.select_slider`
  - `st.chat_input`
  - `st.feedback`
  - `st.pills`
- ↕️ `st.dataframe`, `st.data_editor`, `st.altair_chart`, `st.pydeck_chart`, and all simple charts have height parameters to use with flex containers.
- ↔️ `st.plotly_chart`, `st.vega_lite_chart`, `st.altair_chart`, `st.pydeck_chart`, and all simple charts have width parameters to use with flex containers.
- 🐍 Due to end of life, Python 3.9 is no longer supported.

**Other Changes**

- ⚡ If you don't pass a file to `streamlit run`, it will try `streamlit_app.py` by default ([#12599](https://github.com/streamlit/streamlit/pull/12599)).
- 🥷 `st.dataframe` hides its index column by default when row selections are enabled ([#12448](https://github.com/streamlit/streamlit/pull/12448), [#12237](https://github.com/streamlit/streamlit/issues/12237)). Thanks, [plumol](https://github.com/plumol)!
- 👩‍🎨 For compatibility with new theming options, the app settings menu no longer supports theme editing ([#12648](https://github.com/streamlit/streamlit/pull/12648)).
- 👋 The Streamlit hello app preloads its Python packages on its home page for a faster user experience ([#12617](https://github.com/streamlit/streamlit/pull/12617)).
- 👍 Slider thumbs don't extend beyond the edge of their track ([#12549](https://github.com/streamlit/streamlit/pull/12549), [#4284](https://github.com/streamlit/streamlit/issues/4284)).
- ℹ️ Material icons and emojis were updated ([#12669](https://github.com/streamlit/streamlit/pull/12669)).
- 🦠 Bug fix: Pyplot charts render correctly in fragments, containers, and expanders ([#12807](https://github.com/streamlit/streamlit/pull/12807), [#12678](https://github.com/streamlit/streamlit/issues/12678), [#12763](https://github.com/streamlit/streamlit/issues/12763)).
- 🪰 Bug fix: Dataframes correctly resize and align when using `width="content"` ([#12682](https://github.com/streamlit/streamlit/pull/12682)).
- 🪳 Bug fix: Fuzzy search in select boxes is case insensitive ([#12849](https://github.com/streamlit/streamlit/pull/12849), [#11724](https://github.com/streamlit/streamlit/issues/11724)).
- 🕷️ Bug fix: 500 errors display correctly ([#12845](https://github.com/streamlit/streamlit/pull/12845)).
- 🐞 Bug fix: Deprecation warnings respect `client.showErrorDetails` ([#12794](https://github.com/streamlit/streamlit/pull/12794), [#12743](https://github.com/streamlit/streamlit/issues/12743)).
- 🐝 Bug fix: Path handling in the file watcher was improved to prevent a `ValueError` in Windows environments ([#12741](https://github.com/streamlit/streamlit/pull/12741), [#12731](https://github.com/streamlit/streamlit/issues/12731)).
- 🐜 Bug fix: `st.pills` shows its value when disabled ([#12555](https://github.com/streamlit/streamlit/pull/12555), [#12388](https://github.com/streamlit/streamlit/issues/12388)). Thanks, [davidsjoberg1](https://github.com/davidsjoberg1)!
- 🪲 Bug fix: Plotly charts hide overflow to prevent flickering behavior from scrollbars [(#12594](https://github.com/streamlit/streamlit/pull/12594)).
- 🐛 Bug fix: Streamlit's handling of Altair charts was improved for thread safety and prevention of an "Unrecognized data set" race condition ([#12673](https://github.com/streamlit/streamlit/pull/12673), [#11911](https://github.com/streamlit/streamlit/pull/11911), [#11342](https://github.com/streamlit/streamlit/issues/11342), [#11906](https://github.com/streamlit/streamlit/issues/11906)).

## Older versions of Streamlit

- [2025 release notes](/develop/quick-reference/release-notes/2025)
- [2024 release notes](/develop/quick-reference/release-notes/2024)
- [2023 release notes](/develop/quick-reference/release-notes/2023)
- [2022 release notes](/develop/quick-reference/release-notes/2022)
- [2021 release notes](/develop/quick-reference/release-notes/2021)
- [2020 release notes](/develop/quick-reference/release-notes/2020)
- [2019 release notes](/develop/quick-reference/release-notes/2019)

---


---

**Navigation:** [← Previous](./07-streamlitconfigtoml.md) | [Index](./index.md) | [Next →](./09-2025-release-notes.md)
