---
title: "Widget updating for every second input when using session state"
source: https://docs.streamlit.io/knowledge-base/using-streamlit/widget-updating-session-state
section: 345
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

[← Previous](344-where-does-stfile_uploader-store-uploaded-files-and-when-do-they-get-deleted.md) | [Index](index.md) | [Next →](index.md)
