---
title: "Understanding widget behavior"
source: https://docs.streamlit.io/develop/concepts/architecture/widget-behavior
section: 26
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

[← Previous](25-working-with-fragments.md) | [Index](index.md) | [Next →](index.md)
