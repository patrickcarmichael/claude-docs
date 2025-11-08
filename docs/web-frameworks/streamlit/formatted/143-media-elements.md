---
title: "Media elements"
source: https://docs.streamlit.io/develop/api-reference/media
section: 143
---

# Media elements

Source: https://docs.streamlit.io/develop/api-reference/media


It's easy to embed images, videos, and audio files directly into your Streamlit apps.

<TileContainer>
<RefCard href="/develop/api-reference/media/st.image">
<Image>alt="screenshot" src="/images/api/image.jpg" /&gt;

<h4>Image</h4>

Display an image or list of images.

```python
st.image(numpy_array)
st.image(image_bytes)
st.image(file)
st.image("https://example.com/myimage.jpg")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.logo">
<Image>alt="screenshot" src="/images/api/logo.jpg" /&gt;

<h4>Logo</h4>

Display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.pdf">
<Image>alt="screenshot" src="/images/api/pdf.jpg" /&gt;

<h4>PDF</h4>

Display a PDF file.

```python
st.pdf("my_document.pdf")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.audio">
<Image>alt="screenshot" src="/images/api/audio.jpg" /&gt;

<h4>Audio</h4>

Display an audio player.

```python
st.audio(numpy_array)
st.audio(audio_bytes)
st.audio(file)
st.audio("https://example.com/myaudio.mp3", format="audio/mp3")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.video">
<Image>alt="screenshot" src="/images/api/video.jpg" /&gt;

<h4>Video</h4>

Display a video player.

```python
st.video(numpy_array)
st.video(video_bytes)
st.video(file)
st.video("https://example.com/myvideo.mp4", format="video/mp4")
```python
</Image></RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/whitphx/streamlit-webrtc">
<Image>alt="screenshot" src="/images/api/components/webrtc.jpg" /&gt;

<h4>Streamlit Webrtc</h4>

Handling and transmitting real-time video/audio streams with Streamlit. Created by [@whitphx](https://github.com/whitphx).

```python
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample")
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">
<Image>alt="screenshot" src="/images/api/components/drawable-canvas.jpg" /&gt;

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">
<Image>alt="screenshot" src="/images/api/components/image-comparison.jpg" /&gt;

<h4>Image Comparison</h4>

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">
<Image>alt="screenshot" src="/images/api/components/cropper.jpg" /&gt;

<h4>Streamlit Cropper</h4>

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">
<Image>alt="screenshot" src="/images/api/components/image-coordinates.jpg" /&gt;

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">
<Image>alt="screenshot" src="/images/api/components/lottie.jpg" /&gt;

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```python
</Image></ComponentCard>
</ComponentSlider>

---

[← Previous](119-input-widgets.md) | [Index](index.md) | [Next →](index.md)
