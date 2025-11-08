---
title: "Chat elements"
source: https://docs.streamlit.io/develop/api-reference/chat
section: 158
---

# Chat elements

Source: https://docs.streamlit.io/develop/api-reference/chat


Streamlit provides a few commands to help you build conversational apps. These chat elements are designed to be used in conjunction with each other, but you can also use them separately.

`st.chat_message` lets you insert a chat message container into the app so you can display messages from the user or the app. Chat containers can contain other Streamlit elements, including charts, tables, text, and more. `st.chat_input` lets you display a chat input widget so the user can type in a message. Remember to check out `st.status` to display output from long-running processes and external API calls.

<TileContainer>
<RefCard href="/develop/api-reference/chat/st.chat_input">
<Image>alt="screenshot" src="/images/api/chat_input.jpg" /&gt;

<h4>Chat input</h4>

Display a chat input widget.

```python
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"The user has sent: {prompt}")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/chat/st.chat_message">
<Image>alt="screenshot" src="/images/api/chat_message.jpg" /&gt;

<h4>Chat message</h4>

Insert a chat message container.

```python
import numpy as np
with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.status">
<Image>alt="screenshot" src="/images/api/status.jpg" /&gt;

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">
<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```python
</RefCard>
</TileContainer>

---

[← Previous](149-layouts-and-containers.md) | [Index](index.md) | [Next →](index.md)
