---
title: "Input widgets"
source: https://docs.streamlit.io/develop/api-reference/widgets
section: 119
---

# Input widgets

Source: https://docs.streamlit.io/develop/api-reference/widgets


With widgets, Streamlit allows you to bake interactivity directly into your apps with buttons, sliders, text inputs, and more.

## Button elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.button">
<Image>alt="screenshot" src="/images/api/button.svg" /&gt;

<h4>Button</h4>

Display a button widget.

```python
clicked = st.button("Click me")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.download_button">
<Image>alt="screenshot" src="/images/api/download_button.svg" /&gt;

<h4>Download button</h4>

Display a download button widget.

```python
st.download_button("Download file", file)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">
<Image>alt="screenshot" src="/images/api/form_submit_button.svg" /&gt;

<h4>Form button</h4>

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.link_button">
<Image>alt="screenshot" src="/images/api/link_button.svg" /&gt;

<h4>Link button</h4>

Display a link button.

```python
st.link_button("Go to gallery", url)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">
<Image>alt="screenshot" src="/images/api/page_link.jpg" /&gt;

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```python
</Image></RefCard>
</TileContainer>

## Selection elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.checkbox">
<Image>alt="screenshot" src="/images/api/checkbox.jpg" /&gt;

<h4>Checkbox</h4>

Display a checkbox widget.

```python
selected = st.checkbox("I agree")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">
<Image>alt="screenshot" src="/images/api/color_picker.jpg" /&gt;

<h4>Color picker</h4>

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.feedback">
<Image>alt="screenshot" src="/images/api/feedback.jpg" /&gt;

<h4>Feedback</h4>

Display a rating or sentiment button group.

```python
st.feedback("stars")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">
<Image>alt="screenshot" src="/images/api/multiselect.jpg" /&gt;

<h4>Multiselect</h4>

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.pills">
<Image>alt="screenshot" src="/images/api/pills.jpg" /&gt;

<h4>Pills</h4>

Display a pill-button selection widget.

```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">
<Image>alt="screenshot" src="/images/api/radio.jpg" /&gt;

<h4>Radio</h4>

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.segmented_control">
<Image>alt="screenshot" src="/images/api/segmented_control.jpg" /&gt;

<h4>Segmented control</h4>

Display a segmented-button selection widget.

```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">
<Image>alt="screenshot" src="/images/api/select_slider.jpg" /&gt;

<h4>Select slider</h4>

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">
<Image>alt="screenshot" src="/images/api/selectbox.jpg" /&gt;

<h4>Selectbox</h4>

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">
<Image>alt="screenshot" src="/images/api/toggle.jpg" /&gt;

<h4>Toggle</h4>

Display a toggle widget.

```python
activated = st.toggle("Activate")
```python
</Image></RefCard>
</TileContainer>

## Numeric input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.number_input">
<Image>alt="screenshot" src="/images/api/number_input.jpg" /&gt;

<h4>Number input</h4>

Display a numeric input widget.

```python
choice = st.number_input("Pick a number", 0, 10)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">
<Image>alt="screenshot" src="/images/api/slider.jpg" /&gt;

<h4>Slider</h4>

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```python
</Image></RefCard>
</TileContainer>

## Date and time input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.date_input">
<Image>alt="screenshot" src="/images/api/date_input.jpg" /&gt;

<h4>Date input</h4>

Display a date input widget.

```python
date = st.date_input("Your birthday")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">
<Image>alt="screenshot" src="/images/api/time_input.jpg" /&gt;

<h4>Time input</h4>

Display a time input widget.

```python
time = st.time_input("Meeting time")
```python
</Image></RefCard>
</TileContainer>

## Text input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.text_input">
<Image>alt="screenshot" src="/images/api/text_input.jpg" /&gt;

<h4>Text input</h4>

Display a single-line text input widget.

```python
name = st.text_input("First name")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">
<Image>alt="screenshot" src="/images/api/text_area.jpg" /&gt;

<h4>Text area</h4>

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```python
</Image></RefCard>
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
</TileContainer>

## Other input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.audio_input">
<Image>alt="screenshot" src="/images/api/audio_input.jpg" /&gt;

<h4>Audio input</h4>

Display a widget that allows users to record with their microphone.

```python
speech = st.audio_input("Record a voice message")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">
<Image>alt="screenshot" src="/images/api/data_editor.jpg" /&gt;

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">
<Image>alt="screenshot" src="/images/api/file_uploader.jpg" /&gt;

<h4>File uploader</h4>

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">
<Image>alt="screenshot" src="/images/api/camera_input.jpg" /&gt;

<h4>Camera input</h4>

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
```python
</Image></RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/okld/streamlit-elements">
<Image>alt="screenshot" src="/images/api/components/elements.jpg" /&gt;

<h4>Streamlit Elements</h4>

Create a draggable and resizable dashboard in Streamlit. Created by [@okls](https://github.com/okls).

```python
from streamlit_elements import elements, mui, html

with elements("new_element"):
  mui.Typography("Hello world")
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/gagan3012/streamlit-tags">
<Image>alt="screenshot" src="/images/api/components/tags.jpg" /&gt;

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/Wirg/stqdm">
<Image>alt="screenshot" src="/images/api/components/stqdm.jpg" /&gt;

<h4>Stqdm</h4>

The simplest way to handle a progress bar in streamlit app. Created by [@Wirg](https://github.com/Wirg).

```python
from stqdm import stqdm

for _ in stqdm(range(50)):
    sleep(0.5)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">
<Image>alt="screenshot" src="/images/api/components/timeline.jpg" /&gt;

<h4>Timeline</h4>

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">
<Image>alt="screenshot" src="/images/api/components/camera-live.jpg" /&gt;

<h4>Camera input live</h4>

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/okld/streamlit-ace">
<Image>alt="screenshot" src="/images/api/components/ace.jpg" /&gt;

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/AI-Yash/st-chat">
<Image>alt="screenshot" src="/images/api/components/chat.jpg" /&gt;

<h4>Streamlit Chat</h4>

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">
<Image>alt="screenshot" src="/images/api/components/option-menu.jpg" /&gt;

<h4>Streamlit Option Menu</h4>

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```python
</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-toggle.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """🥷 Surprise! Here's some additional content""",)
```python
</Image></ComponentCard>
</ComponentSlider>

---

[← Previous](106-chart-elements.md) | [Index](index.md) | [Next →](index.md)
