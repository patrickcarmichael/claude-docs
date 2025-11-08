---
title: "Trigger a full-script rerun from inside a fragment"
source: https://docs.streamlit.io/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment
section: 270
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
  ```python
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.rerun`.

## Summary

In this example, you'll build an app to display sales data. The app has two sets of elements that depend on a date selection. One set of elements displays information for the selected day. The other set of elements displays information for the associated month. If the user changes days within a month, Streamlit only needs to update the first set of elements. If the user selects a day in a different month, Streamlit needs to update all the elements.

You'll collect the day-specific elements into a fragment to avoid rerunning the full app when a user changes days within the same month. If you want to jump ahead to the fragment function definition, see [Build a function to show daily sales data](#build-a-function-to-show-daily-sales-data).

<div>{{ maxWidth: '60%', margin: 'auto' }}&gt;
<Image alt="Execution flow of example Streamlit app showing daily sales on the left and monthly sales on the right" src="/images/tutorials/fragment-rerun-tutorial-execution-flow.png"/>
</div>

---

[← Previous](269-use-core-features-to-work-with-streamlits-execution-model.md) | [Index](index.md) | [Next →](index.md)
