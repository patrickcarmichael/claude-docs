---
title: "Collect user feedback about LLM responses"
source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/chat-response-feedback
section: 242
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
  ```python
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
```python
</Collapse>

---

[← Previous](241-build-an-llm-app-using-langchain.md) | [Index](index.md) | [Next →](index.md)
