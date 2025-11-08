---
title: "Display progress and status"
source: https://docs.streamlit.io/develop/api-reference/status
section: 161
---

# Display progress and status

Source: https://docs.streamlit.io/develop/api-reference/status


Streamlit provides a few methods that allow you to add animation to your
apps. These animations include progress bars, status messages (like
warnings), and celebratory balloons.

## Animated status elements

<TileContainer>
<RefCard href="/develop/api-reference/status/st.progress">
<Image>alt="screenshot" src="/images/api/progress.jpg" /&gt;

<h4>Progress bar</h4>

Display a progress bar.

```python
for i in range(101):
  st.progress(i)
  do_something_slow()
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.spinner">
<Image>alt="screenshot" src="/images/api/spinner.jpg" /&gt;

<h4>Spinner</h4>

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
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
<RefCard href="/develop/api-reference/status/st.toast">
<Image>alt="screenshot" src="/images/api/toast.jpg" /&gt;

<h4>Toast</h4>

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.balloons">
<Image>alt="screenshot" src="/images/api/balloons.jpg" /&gt;

<h4>Balloons</h4>

Display celebratory balloons!

```python
st.balloons()
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.snow">
<Image>alt="screenshot" src="/images/api/snow.jpg" /&gt;

<h4>Snowflakes</h4>

Display celebratory snowflakes!

```python
st.snow()
```python
</Image></RefCard>
</TileContainer>

## Simple callout messages

<TileContainer>
<RefCard href="/develop/api-reference/status/st.success">
<Image>alt="screenshot" src="/images/api/success.jpg" /&gt;

<h4>Success box</h4>

Display a success message.

```python
st.success("Match found!")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.info">
<Image>alt="screenshot" src="/images/api/info.jpg" /&gt;

<h4>Info box</h4>

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.warning">
<Image>alt="screenshot" src="/images/api/warning.jpg" /&gt;

<h4>Warning box</h4>

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.error">
<Image>alt="screenshot" src="/images/api/error.jpg" /&gt;

<h4>Error box</h4>

Display error message.

```python
st.error("We encountered an error")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.exception">
<Image>alt="screenshot" src="/images/api/exception.jpg" /&gt;

<h4>Exception output</h4>

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```python
</Image></RefCard>
</TileContainer>
<ComponentSlider>
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
<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">
<Image>alt="screenshot" src="/images/api/components/custom-notification-box.jpg" /&gt;

<h4>Custom notification box</h4>

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```python
</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-emojis.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="🎈", font_size=54,
  falling_speed=5, animation_length="infinite",)
```python
</Image></ComponentCard>
</ComponentSlider>

---

[← Previous](158-chat-elements.md) | [Index](index.md) | [Next →](index.md)
