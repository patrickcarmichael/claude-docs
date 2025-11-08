---
title: "Testing element classes"
source: https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes
section: 225
---

# Testing element classes

Source: https://docs.streamlit.io/develop/api-reference/app-testing/testing-element-classes


## st.testing.v1.element_tree.Block

The `Block` class has the same methods and attributes as `AppTest`. A `Block` instance represents a container of elements just as `AppTest` represents the entire app. For example, `Block.button` will produce a `WidgetList` of `Button` in the same manner as [`AppTest.button`](/develop/api-reference/testing/st.testing.v1.apptest#apptestbutton).

`ChatMessage`, `Column`, and `Tab` all inherit from `Block`. For all container classes, parameters of the original element can be obtained as properties. For example, `ChatMessage.avatar` and `Tab.label`.


* Function signature:

   st.testing.v1.element_tree.Element(proto, root)



* Function signature:

   st.testing.v1.element_tree.Button(proto, root)



* Function signature:

   st.testing.v1.element_tree.ChatInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Checkbox(proto, root)



* Function signature:

   st.testing.v1.element_tree.ColorPicker(proto, root)



* Function signature:

   st.testing.v1.element_tree.DateInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Multiselect(proto, root)



* Function signature:

   st.testing.v1.element_tree.NumberInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Radio(proto, root)



* Function signature:

   st.testing.v1.element_tree.SelectSlider(proto, root)



* Function signature:

   st.testing.v1.element_tree.Selectbox(proto, root)



* Function signature:

   st.testing.v1.element_tree.Slider(proto, root)



* Function signature:

   st.testing.v1.element_tree.TextArea(proto, root)



* Function signature:

   st.testing.v1.element_tree.TextInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.TimeInput(proto, root)



* Function signature:

   st.testing.v1.element_tree.Toggle(proto, root)

---

[← Previous](223-app-testing.md) | [Index](index.md) | [Next →](index.md)
