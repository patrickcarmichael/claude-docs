---
title: "Validate and edit chat responses"
source: https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/validate-and-edit-chat-responses
section: 243
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
  ```python
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

[← Previous](242-collect-user-feedback-about-llm-responses.md) | [Index](index.md) | [Next →](index.md)
