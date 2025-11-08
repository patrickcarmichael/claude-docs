**Navigation:** [← Previous](./05-bottom-panel-is-a-bar-chart-of-weather-type.md) | [Index](./index.md) | [Next →](./07-streamlitconfigtoml.md)

---

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)
```

<Cloud height="400px" name="doc-text-input1"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.audio_input


* Function signature:

   st.audio_input(label, *, sample_rate=16000, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this widget is used for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | sample_rate | int or None | 16000 | The target sample rate for the audio recording in Hz. This defaults to 16000 Hz, which is optimal for speech recognition. The following sample rates are supported: 8000, 11025, 16000, 22050, 24000, 32000, 44100, or 48000. If this is None, the widget uses the browser's default sample rate (typically 44100 or 48000 Hz). |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this audio input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the audio input if set to True. Default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the audio input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: None or UploadedFile

    The UploadedFile class is a subclass of BytesIO, and
therefore is "file-like". This means you can pass an instance of it
anywhere a file is expected. The MIME type for the audio data is
audio/wav.

Note
The resulting UploadedFile is subject to the size
limitation configured in server.maxUploadSize. If you
expect large sound files, update the configuration option
appropriately.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.camera_input


* Function signature:

   st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this widget is used for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this camera_input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the camera input if set to True. Default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the camera input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: None or UploadedFile

    The UploadedFile class is a subclass of BytesIO, and therefore is
"file-like". This means you can pass an instance of it anywhere a
file is expected.



To read the image file buffer as bytes, you can use `getvalue()` on the `UploadedFile` object.

```python
import streamlit as st

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class>'bytes'&gt;
    st.write(type(bytes_data))
```

<Important>

`st.camera_input` returns an object of the `UploadedFile` class, which a subclass of BytesIO. Therefore it is a "file-like" object. This means you can pass it anywhere where a file is expected, similar to `st.file_uploader`.

</Important>

## Image processing examples

You can use the output of `st.camera_input` for various downstream tasks, including image processing. Below, we demonstrate how to use the `st.camera_input` widget with popular image and data processing libraries such as [Pillow](https://pillow.readthedocs.io/en/stable/installation.html), [NumPy](https://numpy.org/), [OpenCV](https://pypi.org/project/opencv-python-headless/), [TensorFlow](https://www.tensorflow.org/), [torchvision](https://pytorch.org/vision/stable/index.html), and [PyTorch](https://pytorch.org/).

While we provide examples for the most popular use-cases and libraries, you are welcome to adapt these examples to your own needs and favorite libraries.

### Pillow (PIL) and NumPy

Ensure you have installed [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) and [NumPy](https://numpy.org/).

To read the image file buffer as a PIL Image and convert it to a NumPy array:

```python
import streamlit as st
from PIL import Image
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class>'numpy.ndarray'&gt;
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)
```

### OpenCV (cv2)

Ensure you have installed [OpenCV](https://pypi.org/project/opencv-python-headless/) and [NumPy](https://numpy.org/).

To read the image file buffer with OpenCV:

```python
import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Check the type of cv2_img:
    # Should output: <class>'numpy.ndarray'&gt;
    st.write(type(cv2_img))

    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)
```

### TensorFlow

Ensure you have installed [TensorFlow](https://www.tensorflow.org/install/).

To read the image file buffer as a 3 dimensional uint8 tensor with TensorFlow:

```python
import streamlit as st
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class>'tensorflow.python.framework.ops.EagerTensor'&gt;
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)
```

### Torchvision

Ensure you have installed [Torchvision](https://pypi.org/project/torchvision/) (it is not bundled with PyTorch) and [PyTorch](https://pytorch.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with `torchvision.io`:

```python
import streamlit as st
import torch
import torchvision

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with `torchvision.io`:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torchvision.io.decode_image(
        torch.frombuffer(bytes_data, dtype=torch.uint8)
    )

    # Check the type of torch_img:
    # Should output: <class>'torch.Tensor'&gt;
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```

### PyTorch

Ensure you have installed [PyTorch](https://pytorch.org/) and [NumPy](https://numpy.org/).

To read the image file buffer as a 3 dimensional uint8 tensor with PyTorch:

```python
import streamlit as st
import torch
import numpy as np

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with PyTorch:
    bytes_data = img_file_buffer.getvalue()
    torch_img = torch.ops.image.decode_image(
        torch.from_numpy(np.frombuffer(bytes_data, np.uint8)), 3
    )

    # Check the type of torch_img:
    # Should output: <class>'torch.Tensor'&gt;
    st.write(type(torch_img))

    # Check the shape of torch_img:
    # Should output shape: torch.Size([channels, height, width])
    st.write(torch_img.shape)
```</class></class></class></class></class></class>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader


* Function signature:

   st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this file uploader is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | type | str, list of str, or None |  | The allowed file extension(s) for uploaded files. This can be one of the following types:  None (default): All file extensions are allowed. A string: A single file extension is allowed. For example, to only accept CSV files, use "csv". A sequence of strings: Multiple file extensions are allowed. For example, to only accept JPG/JPEG and PNG files, use ["jpg", "jpeg", "png"].   Note This is a best-effort check, but doesn't provide a security guarantee against users uploading files of other types or type extensions. The correct handling of uploaded files is part of the app developer's responsibility. |
   | accept_multiple_files | bool or "directory" |  | Whether to accept more than one file in a submission. This can be one of the following values:  False (default): The user can only submit one file at a time. True: The user can upload multiple files at the same time. "directory": The user can select a directory to upload all files in the directory and its subdirectories. If type is set, only files matching those type(s) will be uploaded.  When this is True or "directory", the return value will be a list and a user can additively select files if they click the browse button on the widget multiple times. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this file_uploader's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the file uploader if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the file uploader widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: None, UploadedFile, or list of UploadedFile

    If accept_multiple_files is False, returns either None or
an UploadedFile object.
If accept_multiple_files is True or "directory", returns
a list with the uploaded files as UploadedFile objects. If no
files were uploaded, returns an empty list.

The UploadedFile class is a subclass of BytesIO, and
therefore is "file-like". This means you can pass an instance of it
anywhere a file is expected.



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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.logo">
<Image>alt="screenshot" src="/images/api/logo.jpg" /&gt;

<h4>Logo</h4>

Display a logo in the upper-left corner of your app and its sidebar.

```python
st.logo("logo.jpg")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/media/st.pdf">
<Image>alt="screenshot" src="/images/api/pdf.jpg" /&gt;

<h4>PDF</h4>

Display a PDF file.

```python
st.pdf("my_document.pdf")
```

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
```

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
```

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
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">
<Image>alt="screenshot" src="/images/api/components/drawable-canvas.jpg" /&gt;

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_drawable_canvas import st_canvas

st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/fcakyon/streamlit-image-comparison">
<Image>alt="screenshot" src="/images/api/components/image-comparison.jpg" /&gt;

<h4>Image Comparison</h4>

Compare images with a slider using [JuxtaposeJS](https://juxtapose.knightlab.com/). Created by [@fcakyon](https://github.com/fcakyon).

```python
from streamlit_image_comparison import image_comparison

image_comparison(img1="image1.jpg", img2="image2.jpg",)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/turner-anderson/streamlit-cropper">
<Image>alt="screenshot" src="/images/api/components/cropper.jpg" /&gt;

<h4>Streamlit Cropper</h4>

A simple image cropper for Streamlit. Created by [@turner-anderson](https://github.com/turner-anderson).

```python
from streamlit_cropper import st_cropper

st_cropper(img, realtime_update=realtime_update, box_color=box_color, aspect_ratio=aspect_ratio)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">
<Image>alt="screenshot" src="/images/api/components/image-coordinates.jpg" /&gt;

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates

streamlit_image_coordinates("https://placekitten.com/200/300")
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-lottie">
<Image>alt="screenshot" src="/images/api/components/lottie.jpg" /&gt;

<h4>Streamlit Lottie</h4>

Integrate [Lottie](https://lottiefiles.com/) animations inside your Streamlit app. Created by [@andfanilo](https://github.com/andfanilo).

```python
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

st_lottie(lottie_hello, key="hello")
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/media/st.audio


* Function signature:

   st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None, end_time=None, loop=False, autoplay=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | str, Path, bytes, BytesIO, numpy.ndarray, or file | channel | The audio to play. This can be one of the following:  A URL (string) for a hosted audio file. A path to a local audio file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run). Raw audio data. Raw data formats must include all necessary file headers to match the file format specified via format.  If data is a NumPy array, it must either be a 1D array of the waveform or a 2D array of shape (C, S) where C is the number of channels and S is the number of samples. See the default channel order at http://msdn.microsoft.com/en-us/library/windows/hardware/dn653308(v=vs.85).aspx |
   | format | str | s | The MIME type for the audio file. This defaults to "audio/wav". For more information about MIME types, see https://www.iana.org/assignments/media-types/media-types.xhtml. |
   | start_time | int, float, timedelta, str, or None |  | The time from which the element should start playing. This can be one of the following:  None (default): The element plays from the beginning. An int or float specifying the time in seconds. float values are rounded down to whole seconds. A string specifying the time in a format supported by Pandas' Timedelta constructor, e.g. "2 minute", "20s", or "1m14s". A timedelta object from Python's built-in datetime library, e.g. timedelta(seconds=70). |
   | sample_rate | int or None |  | The sample rate of the audio data in samples per second. This is only required if data is a NumPy array. |
   | end_time | int, float, timedelta, str, or None |  | The time at which the element should stop playing. This can be one of the following:  None (default): The element plays through to the end. An int or float specifying the time in seconds. float values are rounded down to whole seconds. A string specifying the time in a format supported by Pandas' Timedelta constructor, e.g. "2 minute", "20s", or "1m14s". A timedelta object from Python's built-in datetime library, e.g. timedelta(seconds=70). |
   | loop | bool |  | Whether the audio should loop playback. |
   | autoplay | bool |  | Whether the audio file should start playing automatically. This is False by default. Browsers will not autoplay audio files if the user has not interacted with the page by clicking somewhere. |
   | width | "stretch" or int |  | The width of the audio player element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/media/st.image


* Function signature:

   st.image(image, caption=None, width="content", use_column_width=None, clamp=False, channels="RGB", output_format="auto", *, use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | image | numpy.ndarray, BytesIO, str, Path, or list of these |  | The image to display. This can be one of the following:  A URL (string) for a hosted image. A path to a local image file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run). An SVG string like xmlns=.... A byte array defining an image. This includes monochrome images of shape (w,h) or (w,h,1), color images of shape (w,h,3), or RGBA images of shape (w,h,4), where w and h are the image width and height, respectively. A list of any of the above. Streamlit displays the list as a row of images that overflow to additional rows as needed. |
   | caption | str or list of str |  | Image caption(s). If this is None (default), no caption is displayed. If image is a list of multiple images, caption must be a list of captions (one caption for each image) or None. Captions can optionally contain GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | width | "content", "stretch", or int | width | The width of the image element. This can be one of the following:  "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.  When using an SVG image without a default width, use "stretch" or an integer. |
   | use_column_width | "auto", "always", "never", or bool |  | If "auto", set the image's width to its natural size, but do not exceed the width of the column. If "always" or True, set the image's width to the column width. If "never" or False, set the image's width to its natural size. Note: if set, use_column_width takes precedence over the width parameter. |
   | clamp | bool |  | Whether to clamp image pixel values to a valid range (0-255 per channel). This is only used for byte array images; the parameter is ignored for image URLs and files. If this is False (default) and an image has an out-of-range value, a RuntimeError will be raised. |
   | channels | "RGB" or "BGR" |  | The color format when image is an nd.array. This is ignored for other image types. If this is "RGB" (default), image[:, :, 0] is the red channel, image[:, :, 1] is the green channel, and image[:, :, 2] is the blue channel. For images coming from libraries like OpenCV, you should set this to "BGR" instead. |
   | output_format | "JPEG", "PNG", or "auto" |  | The output format to use when transferring the image data. If this is "auto" (default), Streamlit identifies the compression type based on the type and format of the image. Photos should use the "JPEG" format for lossy compression while diagrams should use the "PNG" format for lossless compression. |
   | use_container_width | bool |  | Whether to override width with the width of the parent container. If use_container_width is False (default), Streamlit sets the image's width according to width. If use_container_width is True, Streamlit sets the width of the image to match the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/media/st.logo


* Function signature:

   st.logo(image, *, size="medium", link=None, icon_image=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | image | Anything supported by st.image (except list) |  | The image to display in the upper-left corner of your app and its sidebar. This can be any of the types supported by st.image except a list. If icon_image is also provided, then Streamlit will only display image in the sidebar. Streamlit scales the image to a max height set by size and a max width to fit within the sidebar. |
   | size | "small", "medium", or "large" |  | The size of the image displayed in the upper-left corner of the app and its sidebar. The possible values are as follows:  "small": 20px max height "medium" (default): 24px max height "large": 32px max height |
   | link | str or None |  | The external URL to open when a user clicks on the logo. The URL must start with "http://" or "https://". If link is None (default), the logo will not include a hyperlink. |
   | icon_image | Anything supported by st.image (except list) or None |  | An optional, typically smaller image to replace image in the upper-left corner when the sidebar is closed. This can be any of the types supported by st.image except a list. If icon_image is None (default), Streamlit will always display image in the upper-left corner, regardless of whether the sidebar is open or closed. Otherwise, Streamlit will render icon_image in the upper-left corner of the app when the sidebar is closed. Streamlit scales the image to a max height set by size and a max width to fit within the sidebar. If the sidebar is closed, the max width is retained from when it was last open. For best results, pass a wide or horizontal image to image and a square image to icon_image. Or, pass a square image to image and leave icon_image=None. |



---

Source: https://docs.streamlit.io/develop/api-reference/media/st.pdf


* Function signature:

   st.pdf(data, *, height=500, key=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | str, Path, BytesIO, or bytes |  | The PDF file to show. This can be one of the following:  A URL (string) for a hosted PDF file. A path to a local PDF file. If you use a relative path, it must be relative to the current working directory. A file-like object. For example, this can be an UploadedFile from st.file_uploader, or this can be a local file opened with open(). Raw bytes data. |
   | height | int or "stretch" |  | The height of the PDF viewer. This can be one of the following:  An integer specifying the height in pixels: The viewer has a fixed height. If the content is larger than the specified height, scrolling is enabled. This is 500 by default. "stretch": The height of the viewer matches the height of its content or the height of the parent container, whichever is larger. If the viewer is not in a parent container, the height of the viewer matches the height of its content. |



---

Source: https://docs.streamlit.io/develop/api-reference/media/st.video


* Function signature:

   st.video(data, format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | str, Path, bytes, io.BytesIO, numpy.ndarray, or file |  | The video to play. This can be one of the following:  A URL (string) for a hosted video file, including YouTube URLs. A path to a local video file. The path can be a str or Path object. Paths can be absolute or relative to the working directory (where you execute streamlit run). Raw video data. Raw data formats must include all necessary file headers to match the file format specified via format. |
   | format | str | s | The MIME type for the video file. This defaults to "video/mp4". For more information about MIME types, see https://www.iana.org/assignments/media-types/media-types.xhtml. |
   | start_time | int, float, timedelta, str, or None |  | The time from which the element should start playing. This can be one of the following:  None (default): The element plays from the beginning. An int or float specifying the time in seconds. float values are rounded down to whole seconds. A string specifying the time in a format supported by Pandas' Timedelta constructor, e.g. "2 minute", "20s", or "1m14s". A timedelta object from Python's built-in datetime library, e.g. timedelta(seconds=70). |
   | subtitles | str, bytes, Path, io.BytesIO, or dict |  | Optional subtitle data for the video, supporting several input types:  None (default): No subtitles. A string, bytes, or Path: File path to a subtitle file in .vtt or .srt formats, or the raw content of subtitles conforming to these formats. Paths can be absolute or relative to the working directory (where you execute streamlit run). If providing raw content, the string must adhere to the WebVTT or SRT format specifications. io.BytesIO: A BytesIO stream that contains valid .vtt or .srt formatted subtitle data. A dictionary: Pairs of labels and file paths or raw subtitle content in .vtt or .srt formats to enable multiple subtitle tracks. The label will be shown in the video player. Example: {"English": "path/to/english.vtt", "French": "path/to/french.srt"}  When provided, subtitles are displayed by default. For multiple tracks, the first one is displayed by default. If you don't want any subtitles displayed by default, use an empty string for the value in a dictrionary's first pair: {"None": "", "English": "path/to/english.vtt"} Not supported for YouTube videos. |
   | end_time | int, float, timedelta, str, or None |  | The time at which the element should stop playing. This can be one of the following:  None (default): The element plays through to the end. An int or float specifying the time in seconds. float values are rounded down to whole seconds. A string specifying the time in a format supported by Pandas' Timedelta constructor, e.g. "2 minute", "20s", or "1m14s". A timedelta object from Python's built-in datetime library, e.g. timedelta(seconds=70). |
   | loop | bool |  | Whether the video should loop playback. |
   | autoplay | bool |  | Whether the video should start playing automatically. This is False by default. Browsers will not autoplay unmuted videos if the user has not interacted with the page by clicking somewhere. To enable autoplay without user interaction, you must also set muted=True. |
   | muted | bool |  | Whether the video should play with the audio silenced. This is False by default. Use this in conjunction with autoplay=True to enable autoplay without user interaction. |
   | width | "stretch" or int |  | The width of the video player element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

# Layouts and Containers

Source: https://docs.streamlit.io/develop/api-reference/layout


## Complex layouts

Streamlit provides several options for controlling how different elements are laid out on the screen.

<TileContainer>
<RefCard href="/develop/api-reference/layout/st.columns">
<Image>alt="screenshot" src="/images/api/columns.jpg" /&gt;

<h4>Columns</h4>

Insert containers laid out as side-by-side columns.

```python
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.container">
<Image>alt="screenshot" src="/images/api/container.jpg" /&gt;

<h4>Container</h4>

Insert a multi-element container.

```python
c = st.container()
st.write("This will show last")
c.write("This will show first")
c.write("This will show second")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.dialog">
<Image>alt="screenshot" src="/images/api/dialog.jpg" /&gt;

<h4>Modal dialog</h4>

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.empty">
<Image>alt="screenshot" src="/images/api/empty.jpg" /&gt;

<h4>Empty</h4>

Insert a single-element container.

```python
c = st.empty()
st.write("This will show last")
c.write("This will be replaced")
c.write("This will show first")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.expander">
<Image>alt="screenshot" src="/images/api/expander.jpg" /&gt;

<h4>Expander</h4>

Insert a multi-element container that can be expanded/collapsed.

```python
with st.expander("Open to see more"):
  st.write("This is more content")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.popover">
<Image>alt="screenshot" src="/images/api/popover.svg" /&gt;

<h4>Popover</h4>

Insert a multi-element popover container that can be opened/closed.

```python
with st.popover("Settings"):
  st.checkbox("Show completed")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.sidebar">
<Image>alt="screenshot" src="/images/api/sidebar.jpg" /&gt;

<h4>Sidebar</h4>

Display items in a sidebar.

```python
st.sidebar.write("This lives in the sidebar")
st.sidebar.button("Click me!")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.space">
<Image>alt="screenshot" src="/images/api/space.jpg" /&gt;

<h4>Space</h4>

Add vertical or horizontal space.

```python
st.space("small")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/layout/st.tabs">
<Image>alt="screenshot" src="/images/api/tabs.jpg" /&gt;

<h4>Tabs</h4>

Insert containers separated into tabs.

```python
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
```

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
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">
<Image>alt="screenshot" src="/images/api/components/pydantic.jpg" /&gt;

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/st_pages">
<Image>alt="screenshot" src="/images/api/components/pages.jpg" /&gt;

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.columns


* Function signature:

   st.columns(spec, *, gap="small", vertical_alignment="top", border=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | spec | int or Iterable of numbers |  | Controls the number and width of columns to insert. Can be one of:  An integer that specifies the number of columns. All columns have equal width in this case. An Iterable of numbers (int or float) that specify the relative width of each column. E.g. [0.7, 0.3] creates two columns where the first one takes up 70% of the available with and the second one takes up 30%. Or [1, 2, 3] creates three columns where the second one is two times the width of the first one, and the third one is three times that width. |
   | gap | "small", "medium", "large", or None |  | The size of the gap between the columns. This can be one of the following:  "small" (default): 1rem gap between the columns. "medium": 2rem gap between the columns. "large": 4rem gap between the columns. None: No gap between the columns.  The rem unit is relative to the theme.baseFontSize configuration option. |
   | vertical_alignment | "top", "center", or "bottom" | is | The vertical alignment of the content inside the columns. The default is "top". |
   | border | bool |  | Whether to show a border around the column containers. If this is False (default), no border is shown. If this is True, a border is shown around each column. |
   | width | "stretch" or int |  | The width of the column group. This can be one of the following:  "stretch" (default): The width of the column group matches the width of the parent container. An integer specifying the width in pixels: The column group has a fixed width. If the specified width is greater than the width of the parent container, the width of the column group matches the width of the parent container. |

* Returns: list of containers

    A list of container objects.



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.container


* Function signature:

   st.container(*, border=None, key=None, width="stretch", height="content", horizontal=False, horizontal_alignment="left", vertical_alignment="top", gap="small")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | border | bool or None |  | Whether to show a border around the container. If None (default), a border is shown if the container is set to a fixed height and not shown otherwise. |
   | key | str or None |  | An optional string to give this container a stable identity. Additionally, if key is provided, it will be used as CSS class name prefixed with st-key-. |
   | width | "stretch", "content", or int |  | The width of the container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. "content": The width of the container matches the width of its content. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |
   | height | "content", "stretch", or int |  | The height of the container. This can be one of the following:  "content" (default): The height of the container matches the height of its content. "stretch": The height of the container matches the height of its content or the height of the parent container, whichever is larger. If the container is not in a parent container, the height of the container matches the height of its content. An integer specifying the height in pixels: The container has a fixed height. If the content is larger than the specified height, scrolling is enabled.   Note Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. |
   | horizontal | bool |  | Whether to use horizontal flexbox layout. If this is False (default), the container's elements are laid out vertically. If this is True, the container's elements are laid out horizontally and will overflow to the next line if they don't fit within the container's width. |
   | horizontal_alignment | "left", "center", "right", or "distribute" |  | The horizontal alignment of the elements inside the container. This can be one of the following:  "left" (default): Elements are aligned to the left side of the container.  "center": Elements are horizontally centered inside the container.  "right": Elements are aligned to the right side of the container.  "distribute": Elements are distributed evenly in the container. This increases the horizontal gap between elements to fill the width of the container. A standalone element is aligned to the left. When horizontal is False, "distribute" aligns the elements the same as "left". |
   | vertical_alignment | "top", "center", "bottom", or "distribute" |  | The vertical alignment of the elements inside the container. This can be one of the following:  "top" (default): Elements are aligned to the top of the container.  "center": Elements are vertically centered inside the container.  "bottom": Elements are aligned to the bottom of the container.  "distribute": Elements are distributed evenly in the container. This increases the vertical gap between elements to fill the height of the container. A standalone element is aligned to the top. When horizontal is True, "distribute" aligns the elements the same as "top". |
   | gap | "small", "medium", "large", or None |  | The minimum gap size between the elements inside the container. This can be one of the following:  "small" (default): 1rem gap between the elements. "medium": 2rem gap between the elements. "large": 4rem gap between the elements. None: No gap between the elements.  The rem unit is relative to the theme.baseFontSize configuration option. The minimum gap applies to both the vertical and horizontal gaps between the elements. Elements may have larger gaps in one direction if you use a distributed horizontal alignment or fixed height. |



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.empty


* Function signature:

   st.empty()



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.expander


* Function signature:

   st.expander(label, expanded=False, *, icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A string to use as the header for the expander. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | expanded | bool | s | If True, initializes the expander in "expanded" state. Defaults to False (collapsed). |
   | icon | str, None |  | An optional emoji or icon to display next to the expander label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | width | "stretch" or int |  | The width of the expander container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.popover


* Function signature:

   st.popover(label, *, type="secondary", help=None, icon=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | The label of the button that opens the popover container. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | help | str or None |  | A tooltip that gets displayed when the popover button is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | type | "primary", "secondary", or "tertiary" |  | An optional string that specifies the button type. This can be one of the following:  "primary": The button's background is the app's primary color for additional emphasis. "secondary" (default): The button's background coordinates with the app's background color for normal emphasis. "tertiary": The button is plain text without a border or background for subtlety. |
   | icon | str |  | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | disabled | bool | is | An optional boolean that disables the popover button if set to True. The default is False. |
   | use_container_width | bool |  | Whether to expand the button's width to fill its parent container. If use_container_width is False (default), Streamlit sizes the button to fit its content. If use_container_width is True, the width of the button matches its parent container. In both cases, if the content of the button is wider than the parent container, the content will line wrap. The popover container's minimum width matches the width of its button. The popover container may be wider than its button to fit the container's content. |
   | width | int, "stretch", or "content" |  | The width of the button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container.  The popover container's minimum width matches the width of its button. The popover container may be wider than its button to fit the container's contents. |



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.sidebar

## st.sidebar

## Add widgets to sidebar

Not only can you add interactivity to your app with widgets, you can organize them into a sidebar. Elements can be passed to `st.sidebar` using object notation and `with` notation.

The following two snippets are equivalent:

```python
# Object notation
st.sidebar.[element_name]
```

```python
# "with" notation
with st.sidebar:
    st.[element_name]
```

Each element that's passed to `st.sidebar` is pinned to the left, allowing users to focus on the content in your app.

<Tip>

The sidebar is resizable! Drag and drop the right border of the sidebar to resize it! ↔️

</Tip>

Here's an example of how you'd add a selectbox and a radio button to your sidebar:

```python
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
```

<Important>

The only elements that aren't supported using object notation are `st.echo`, `st.spinner`, and `st.toast`. To use these elements, you must use `with` notation.

</Important>

Here's an example of how you'd add [`st.echo`](/develop/api-reference/text/st.echo) and [`st.spinner`](/develop/api-reference/status/st.spinner) to your sidebar:

```python
import streamlit as st
import time

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")
```

---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.space


* Function signature:

   st.space(size="small")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | size | "small", "medium", "large", "stretch", or int |  | The size of the space. This can be one of the following values:  "small" (default): 0.75rem, which is the height of a widget label. This is useful for aligning buttons with labeled widgets. "medium": 2.5rem, which is the height of a button or (unlabeled) input field. "large": 4.25rem, which is the height of a labeled input field or unlabeled media widget, like st.file_uploader. "stretch": Expands to fill remaining space in the container. An integer: Fixed size in pixels. |



---

Source: https://docs.streamlit.io/develop/api-reference/layout/st.tabs


* Function signature:

   st.tabs(tabs, *, width="stretch", default=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | tabs | list of str |  | Creates a tab for each string in the list. The first tab is selected by default. The string is used as the name of the tab and can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | width | "stretch" or int |  | The width of the tab container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |
   | default | str or None | tab | The default tab to select. If this is None (default), the first tab is selected. If this is a string, it must be one of the tab labels. If two tabs have the same label as default, the first one is selected. |

* Returns: list of containers

    A list of container objects.



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
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.status">
<Image>alt="screenshot" src="/images/api/status.jpg" /&gt;

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</Image></RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">
<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/chat/st.chat_input

<Tip>

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

</Tip>

* Function signature:

   st.chat_input(placeholder="Your message", *, key=None, max_chars=None, accept_file=False, file_type=None, disabled=False, on_submit=None, args=None, kwargs=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | placeholder | str | s | A placeholder text shown when the chat input is empty. This defaults to "Your message". For accessibility reasons, you should not use an empty string. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | max_chars | int or None |  | The maximum number of characters that can be entered. If this is None (default), there will be no maximum. |
   | accept_file | bool, "multiple", or "directory" |  | Whether the chat input should accept files. This can be one of the following values:  False (default): No files are accepted and the user can only submit a message. True: The user can add a single file to their submission. "multiple": The user can add multiple files to their submission. "directory": The user can add multiple files to their submission by selecting a directory. If file_type is set, only files matching those type(s) will be uploaded.  By default, uploaded files are limited to 200 MB each. You can configure this using the server.maxUploadSize config option. For more information on how to set config options, see config.toml. |
   | file_type | str, Sequence[str], or None |  | The allowed file extension(s) for uploaded files. This can be one of the following types:  None (default): All file extensions are allowed. A string: A single file extension is allowed. For example, to only accept CSV files, use "csv". A sequence of strings: Multiple file extensions are allowed. For example, to only accept JPG/JPEG and PNG files, use ["jpg", "jpeg", "png"].   Note This is a best-effort check, but doesn't provide a security guarantee against users uploading files of other types or type extensions. The correct handling of uploaded files is part of the app developer's responsibility. |
   | disabled | bool | s | Whether the chat input should be disabled. This defaults to False. |
   | on_submit | callable |  | An optional callback invoked when the chat input's value is submitted. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | width | "stretch" or int |  | The width of the chat input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: None, str, or dict-like

    The user's submission. This is one of the following types:

None: If the user didn't submit a message or file in the last
rerun, the widget returns None.
A string: When the widget is not configured to accept files and
the user submitted a message in the last rerun, the widget
returns the user's message as a string.
A dict-like object: When the widget is configured to accept files
and the user submitted a message and/or file(s) in the last
rerun, the widget returns a dict-like object with two attributes,
text and files.

When the widget is configured to accept files and the user submits
something in the last rerun, you can access the user's submission
with key or attribute notation from the dict-like object. This is
shown in Example 3 below.
The text attribute holds a string, which is the user's message.
This is an empty string if the user only submitted one or more
files.
The files attribute holds a list of UploadedFile objects.
The list is empty if the user only submitted a message. Unlike
st.file_uploader, this attribute always returns a list, even
when the widget is configured to accept only one file at a time.
The UploadedFile class is a subclass of BytesIO, and therefore is
"file-like". This means you can pass an instance of it anywhere a
file is expected.



For an overview of the `st.chat_input` and `st.chat_message` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk"/>

---

Source: https://docs.streamlit.io/develop/api-reference/chat/st.chat_message

<Tip>

Read the [Build a basic LLM chat app](/develop/tutorials/llms/build-conversational-apps) tutorial to learn how to use `st.chat_message` and `st.chat_input` to build chat-based apps.

</Tip>

* Function signature:

   st.chat_message(name, *, avatar=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | name | "user", "assistant", "ai", "human", or str |  | The name of the message author. Can be "human"/"user" or "ai"/"assistant" to enable preset styling and avatars. Currently, the name is not shown in the UI but is only set as an accessibility label. For accessibility reasons, you should not use an empty string. |
   | avatar | Anything supported by st.image (except list), str, or None | user | The avatar shown next to the message. If avatar is None (default), the icon will be determined from name as follows:  If name is "user" or "human", the message will have a default user icon. If name is "ai" or "assistant", the message will have a default bot icon. For all other values of name, the message will show the first letter of the name.  In addition to the types supported by st.image (except list), the following strings are valid:  A single-character emoji. For example, you can set avatar="🧑‍💻" or avatar="🦖". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | width | "stretch", "content", or int |  | The width of the chat message container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. "content": The width of the container matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |

* Returns: Container

    A single container that can hold multiple elements.



For an overview of the `st.chat_message` and `st.chat_input` API, check out this video tutorial by Chanin Nantasenamat ([@dataprofessor](https://www.youtube.com/dataprofessor)), a Senior Developer Advocate at Streamlit.

<YouTube videoId="4sPnOqeUDmk"/>

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.spinner">
<Image>alt="screenshot" src="/images/api/spinner.jpg" /&gt;

<h4>Spinner</h4>

Temporarily displays a message while executing a block of code.

```python
with st.spinner("Please wait..."):
  do_something_slow()
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.status">
<Image>alt="screenshot" src="/images/api/status.jpg" /&gt;

<h4>Status container</h4>

Display output of long-running tasks in a container.

```python
with st.status('Running'):
  do_something_slow()
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.toast">
<Image>alt="screenshot" src="/images/api/toast.jpg" /&gt;

<h4>Toast</h4>

Briefly displays a toast message in the bottom-right corner.

```python
st.toast('Butter!', icon='🧈')
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.balloons">
<Image>alt="screenshot" src="/images/api/balloons.jpg" /&gt;

<h4>Balloons</h4>

Display celebratory balloons!

```python
st.balloons()
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.snow">
<Image>alt="screenshot" src="/images/api/snow.jpg" /&gt;

<h4>Snowflakes</h4>

Display celebratory snowflakes!

```python
st.snow()
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.info">
<Image>alt="screenshot" src="/images/api/info.jpg" /&gt;

<h4>Info box</h4>

Display an informational message.

```python
st.info("Dataset is updated every day at midnight.")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.warning">
<Image>alt="screenshot" src="/images/api/warning.jpg" /&gt;

<h4>Warning box</h4>

Display warning message.

```python
st.warning("Unable to fetch image. Skipping...")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.error">
<Image>alt="screenshot" src="/images/api/error.jpg" /&gt;

<h4>Error box</h4>

Display error message.

```python
st.error("We encountered an error")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/status/st.exception">
<Image>alt="screenshot" src="/images/api/exception.jpg" /&gt;

<h4>Exception output</h4>

Display an exception.

```python
e = RuntimeError("This is an exception of type RuntimeError")
st.exception(e)
```

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
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/Socvest/streamlit-custom-notification-box">
<Image>alt="screenshot" src="/images/api/components/custom-notification-box.jpg" /&gt;

<h4>Custom notification box</h4>

A custom notification box with the ability to close it out. Created by [@Socvest](https://github.com/Socvest).

```python
from streamlit_custom_notification_box import custom_notification_box

styles = {'material-icons':{'color': 'red'}, 'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}, 'notification-text': {'':''}, 'close-button':{'':''}, 'link':{'':''}}
custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
```

</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-emojis.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.let_it_rain import rain

rain(emoji="🎈", font_size=54,
  falling_speed=5, animation_length="infinite",)
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/status/st.success


* Function signature:

   st.success(body, *, icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str, None |  | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | width | "stretch" or int |  | The width of the success element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.info


* Function signature:

   st.info(body, *, icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str, None |  | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | width | "stretch" or int |  | The width of the info element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.warning


* Function signature:

   st.warning(body, *, icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str, None |  | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | width | "stretch" or int |  | The width of the warning element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.error


* Function signature:

   st.error(body, *, icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The text to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str, None |  | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | width | "stretch" or int |  | The width of the alert element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.exception


* Function signature:

   st.exception(exception, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | exception | Exception |  | The exception to display. |
   | width | "stretch" or int |  | The width of the exception element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.progress


* Function signature:

   st.progress(value, text=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | value | int or float |  | 0  0.0 |
   | text | str or None |  | A message to display above the progress bar. The text can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | width | "stretch" or int |  | The width of the progress element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.spinner


* Function signature:

   st.spinner(text="In progress...", *, show_time=False, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | text | str | s | The text to display next to the spinner. This defaults to "In progress...". The text can optionally contain GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | show_time | bool |  | Whether to show the elapsed time next to the spinner text. If this is False (default), no time is displayed. If this is True, elapsed time is displayed with a precision of 0.1 seconds. The time format is not configurable. |
   | width | "content", "stretch", or int |  | The width of the spinner element. This can be one of the following:  "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.status


* Function signature:

   st.status(label, *, expanded=False, state="running", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | The initial label of the status container. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | expanded | bool | s | If True, initializes the status container in "expanded" state. Defaults to False (collapsed). |
   | state | "running", "complete", or "error" |  | The initial state of the status container which determines which icon is shown:  running (default): A spinner icon is shown. complete: A checkmark icon is shown. error: An error icon is shown. |
   | width | "stretch" or int |  | The width of the status container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |

* Returns: StatusContainer

    A mutable status container that can hold multiple elements. The label, state,
and expanded state can be updated after creation via .update().



* Function signature:

   StatusContainer.update(*, label=None, expanded=None, state=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | A new label of the status container. If None, the label is not changed. |
   | expanded | bool or None |  | The new expanded state of the status container. If None, the expanded state is not changed. |
   | state | "running", "complete", "error", or None |  | The new state of the status container. This mainly changes the icon. If None, the state is not changed. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.toast


* Function signature:

   st.toast(body, *, icon=None, duration="short")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | str |  | The string to display as GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str, None |  | An optional emoji or icon to display next to the alert. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | duration | "short", "long", "infinite", or int |  | The time to display the toast message. This can be one of the following:  "short" (default): Displays for 4 seconds. "long": Displays for 10 seconds. "infinite": Shows the toast until the user dismisses it. An integer: Displays for the specified number of seconds. |



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.balloons


* Function signature:

   st.balloons()



---

Source: https://docs.streamlit.io/develop/api-reference/status/st.snow


* Function signature:

   st.snow()



---

# Authentication and user info

Source: https://docs.streamlit.io/develop/api-reference/user


Streamlit provides native support for user authentication so you can personalize your apps. You can also directly read headers and cookies.

<TileContainer>
<RefCard href="/develop/api-reference/user/st.login">
<h4>Log in a user</h4>

`st.login()` starts an authentication flow with an identity provider.

```python
st.login()
```

</RefCard>
<RefCard href="/develop/api-reference/user/st.logout">
<h4>Log out a user</h4>

`st.logout()` removes a user's identity information.

```python
st.logout()
```

</RefCard>
<RefCard href="/develop/api-reference/user/st.user">
<h4>User info</h4>

`st.user` returns information about a logged-in user.

```python
if st.user.is_logged_in:
  st.write(f"Welcome back, {st.user.name}!")
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/user/st.login

<Tip>

Learn more in [User authentication and information](/develop/concepts/connections/authentication).

</Tip>

* Function signature:

   st.login(provider=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | provider | str or None |  | The name of your provider configuration to use for login. If provider is None (default), Streamlit will use all settings in the [auth] dictionary within your app's secrets.toml file. Otherwise, use an [auth.{provider}] dictionary for the named provider, as shown in the examples that follow. When you pass a string to provider, Streamlit will use redirect_uri and cookie_secret, while ignoring any other values in the [auth] dictionary. Due to internal implementation details, Streamlit does not support using an underscore within provider at this time. |



---

Source: https://docs.streamlit.io/develop/api-reference/user/st.logout

<Tip>

Learn more in [User authentication and information](/develop/concepts/connections/authentication).

</Tip>

* Function signature:

   st.logout()



---

Source: https://docs.streamlit.io/develop/api-reference/user/st.user


* Function signature:

   st.user()

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | is_logged_in | bool |  | Whether a user is logged in. For a locally running app, this attribute is only available when authentication (st.login()) is configured in secrets.toml. Otherwise, it does not exist. |



### Community Cloud

Starting from Streamlit version 1.42.0, you can't use `st.user` to retrieve a user's Community Cloud account email. To access user information, you must set up an identity provider and configure authentication (`[auth]`) in your app's secrets. Remember to update your identity provider's configuration and your app's secrets to allow your new domain. A list of [IP addresses](/deploy/streamlit-community-cloud/status#ip-addresses) used by Community Cloud is available if needed. An authentication-configured app counts as your single allowed private app.


* Function signature:

   st.user.to_dict()

* Returns: Dict[str,str]

    A dictionary of the current user's information.



---

# Navigation and pages

Source: https://docs.streamlit.io/develop/api-reference/navigation


<TileContainer>
<RefCard href="/develop/api-reference/navigation/st.navigation">
<Image>alt="screenshot" src="/images/api/navigation.jpg" /&gt;

<h4>Navigation</h4>

Configure the available pages in a multipage app.

```python
st.navigation({
    "Your account" : [log_out, settings],
    "Reports" : [overview, usage],
    "Tools" : [search]
})
```

</Image></RefCard>
<RefCard href="/develop/api-reference/navigation/st.page">
<Image>alt="screenshot" src="/images/api/page.jpg" /&gt;

<h4>Page</h4>

Define a page in a multipage app.

```python
home = st.Page(
    "home.py",
    title="Home",
    icon=":material/home:"
)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">
<Image>alt="screenshot" src="/images/api/page_link.jpg" /&gt;

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="Profile")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/navigation/st.switch_page">
<h4>Switch page</h4>

Programmatically navigates to a specified page.

```python
st.switch_page("pages/my_page.py")
```

</RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/navigation/st.navigation


* Function signature:

   st.navigation(pages, *, position="sidebar", expanded=False)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | pages | Sequence[page-like], Mapping[str, Sequence[page-like]] | title | The available pages for the app. To create a navigation menu with no sections or page groupings, pages must be a list of page-like objects. Page-like objects are anything that can be passed to st.Page or a StreamlitPage object returned by st.Page. To create labeled sections or page groupings within the navigation menu, pages must be a dictionary. Each key is the label of a section and each value is the list of page-like objects for that section. If you use position="top", each grouping will be a collapsible item in the navigation menu. For top navigation, if you use an empty string as a section header, the pages in that section will be displayed at the beginning of the menu before the collapsible sections. When you use a string or path as a page-like object, they are internally passed to st.Page and converted to StreamlitPage objects. In this case, the page will have the default title, icon, and path inferred from its path or filename. To customize these attributes for your page, initialize your page with st.Page. |
   | position | "sidebar", "top", or "hidden" |  | The position of the navigation menu. If this is "sidebar" (default), the navigation widget appears at the top of the sidebar. If this is "top", the navigation appears in the top header of the app. If this is "hidden", the navigation widget is not displayed. If there is only one page in pages, the navigation will be hidden for any value of position. |
   | expanded | bool |  | Whether the navigation menu should be expanded. If this is False (default), the navigation menu will be collapsed and will include a button to view more options when there are too many pages to display. If this is True, the navigation menu will always be expanded; no button to collapse the menu will be displayed. If st.navigation changes from expanded=True to expanded=False on a rerun, the menu will stay expanded and a collapse button will be displayed. The parameter is only used when position="sidebar". |

* Returns: StreamlitPage

    The current page selected by the user. To run the page, you must use
the .run() method on it.



---

Source: https://docs.streamlit.io/develop/api-reference/navigation/st.page


* Function signature:

   st.Page(page, *, title=None, icon=None, url_path=None, default=False)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | page | str, Path, or callable |  | The page source as a Callable or path to a Python file. If the page source is defined by a Python file, the path can be a string or pathlib.Path object. Paths can be absolute or relative to the entrypoint file. If the page source is defined by a Callable, the Callable can't accept arguments. |
   | title | str or None |  | The title of the page. If this is None (default), the page title (in the browser tab) and label (in the navigation menu) will be inferred from the filename or callable name in page. For more information, see Overview of multipage apps. |
   | icon | str or None |  | An optional emoji or icon to display next to the page title and label. If icon is None (default), no icon is displayed next to the page label in the navigation menu, and a Streamlit icon is displayed next to the title (in the browser tab). If icon is a string, the following options are valid:   A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.     An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | url_path | str or None | page | The page's URL pathname, which is the path relative to the app's root URL. If this is None (default), the URL pathname will be inferred from the filename or callable name in page. For more information, see Overview of multipage apps. The default page will have a pathname of "", indicating the root URL of the app. If you set default=True, url_path is ignored. url_path can't include forward slashes; paths can't include subdirectories. |
   | default | bool | page | Whether this page is the default page to be shown when the app is loaded. If default is False (default), the page will have a nonempty URL pathname. However, if no default page is passed to st.navigation and this is the first page, this page will become the default page. If default is True, then the page will have an empty pathname and url_path will be ignored. |

* Returns: StreamlitPage

    The page object associated to the given script.



* Function signature:

   StreamlitPage(page, *, title=None, icon=None, url_path=None, default=False)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | icon | str |  | The icon of the page. If no icon was declared in st.Page, this property returns "". |
   | title | str |  | The title of the page. Unless declared otherwise in st.Page, the page title is inferred from the filename or callable name. For more information, see Overview of multipage apps. |
   | url_path | str | page | The page's URL pathname, which is the path relative to the app's root URL. Unless declared otherwise in st.Page, the URL pathname is inferred from the filename or callable name. For more information, see Overview of multipage apps. The default page will always have a url_path of "" to indicate the root URL (e.g. homepage). |



* Function signature:

   StreamlitPage.run()



---

Source: https://docs.streamlit.io/develop/api-reference/navigation/st.switch_page


* Function signature:

   st.switch_page(page)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | page | str, Path, or st.Page |  | The file path (relative to the main script) or an st.Page indicating the page to switch to. |



---

# Execution flow

Source: https://docs.streamlit.io/develop/api-reference/execution-flow


## Change execution

By default, Streamlit apps execute the script entirely, but we allow some functionality to handle control flow in your applications.

<TileContainer>
<RefCard href="/develop/api-reference/execution-flow/st.dialog" size="full">
<Image>alt="screenshot" src="/images/api/dialog.jpg" /&gt;

<h4>Modal dialog</h4>

Insert a modal dialog that can rerun independently from the rest of the script.

```python
@st.dialog("Sign up")
def email_form():
    name = st.text_input("Name")
    email = st.text_input("Email")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.fragment">
<h4>Fragments</h4>

Define a fragment to rerun independently from the rest of the script.

```python
@st.fragment(run_every="10s")
def fragment():
    df = get_data()
    st.line_chart(df)
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.rerun">
<h4>Rerun script</h4>

Rerun the script immediately.

```python
st.rerun()
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.stop">
<h4>Stop execution</h4>

Stops execution immediately.

```python
st.stop()
```

</RefCard>
</TileContainer>

## Group multiple widgets

By default, Streamlit reruns your script everytime a user interacts with your app.
However, sometimes it's a better user experience to wait until a group of related
widgets is filled before actually rerunning the script. That's what `st.form` is for!

<TileContainer>
<RefCard href="/develop/api-reference/execution-flow/st.form" size="half">
<h4>Forms</h4>

Create a form that batches elements together with a “Submit" button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button" size="half">
<h4>Form submit button</h4>

Display a form submit button.

```python
with st.form(key='my_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    st.form_submit_button("Sign up")
```

</RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/kmcgrady/streamlit-autorefresh">
<Image>alt="screenshot" src="/images/api/components/autorefresh.jpg" /&gt;

<h4>Autorefresh</h4>

Force a refresh without tying up a script. Created by [@kmcgrady](https://github.com/kmcgrady).

```python
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=2000, limit=100,
  key="fizzbuzzcounter")
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/lukasmasuch/streamlit-pydantic">
<Image>alt="screenshot" src="/images/api/components/pydantic.jpg" /&gt;

<h4>Pydantic</h4>

Auto-generate Streamlit UI from Pydantic Models and Dataclasses. Created by [@lukasmasuch](https://github.com/lukasmasuch).

```python
import streamlit_pydantic as sp

sp.pydantic_form(key="my_form",
  model=ExampleModel)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/st_pages">
<Image>alt="screenshot" src="/images/api/components/pages.jpg" /&gt;

<h4>Streamlit Pages</h4>

An experimental version of Streamlit Multi-Page Apps. Created by [@blackary](https://github.com/blackary).

```python
from st_pages import Page, show_pages, add_page_title

show_pages([ Page("streamlit_app.py", "Home", "🏠"),
  Page("other_pages/page2.py", "Page 2", ":books:"), ])
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog


* Function signature:

   st.dialog(title, *, width="small", dismissible=True, on_dismiss="ignore")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | title | str |  | The title to display at the top of the modal dialog. It cannot be empty. The title can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | width | "small", "medium", "large" |  | The width of the modal dialog. This can be one of the following:  "small" (default): The modal dialog will be a maximum of 500 pixels wide. "medium": The modal dialog will be up to 750 pixels wide. "large": The modal dialog will be up to 1280 pixels wide. |
   | dismissible | bool |  | Whether the modal dialog can be dismissed by the user. If this is True (default), the user can dismiss the dialog by clicking outside of it, clicking the "X" in its upper-right corner, or pressing ESC on their keyboard. If this is False, the "X" in the upper-right corner is hidden and the dialog must be closed programmatically by calling st.rerun() inside the dialog function.  Note Setting dismissible to False does not guarantee that all interactions in the main app are blocked. Don't rely on dismissible for security-critical checks. |
   | on_dismiss | "ignore", "rerun", or callable |  | How the dialog should respond to dismissal events. This can be one of the following:  "ignore" (default): Streamlit will not rerun the app when the user dismisses the dialog. "rerun": Streamlit will rerun the app when the user dismisses the dialog. A callable: Streamlit will rerun the app when the user dismisses the dialog and execute the callable as a callback function before the rest of the app. |



---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.form

<Tip>

This page only contains information on the `st.forms` API. For a deeper dive into creating and using forms within Streamlit apps, read our guide on [Using forms](/develop/concepts/architecture/forms).

</Tip>

* Function signature:

   st.form(key, clear_on_submit=False, *, enter_to_submit=True, border=True, width="stretch", height="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | key | str |  | A string that identifies the form. Each form must have its own key. (This key is not displayed to the user in the interface.) |
   | clear_on_submit | bool | values | If True, all widgets inside the form will be reset to their default values after the user presses the Submit button. Defaults to False. (Note that Custom Components are unaffected by this flag, and will not be reset to their defaults on form submission.) |
   | enter_to_submit | bool |  | Whether to submit the form when a user presses Enter while interacting with a widget inside the form. If this is True (default), pressing Enter while interacting with a form widget is equivalent to clicking the first st.form_submit_button in the form. If this is False, the user must click an st.form_submit_button to submit the form. If the first st.form_submit_button in the form is disabled, the form will override submission behavior with enter_to_submit=False. |
   | border | bool | True | Whether to show a border around the form. Defaults to True.  Note Not showing a border can be confusing to viewers since interacting with a widget in the form will do nothing. You should only remove the border if there's another border (e.g. because of an expander) or the form is small (e.g. just a text input and a submit button). |
   | width | "stretch", "content", or int |  | The width of the form container. This can be one of the following:  "stretch" (default): The width of the container matches the width of the parent container. "content": The width of the container matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The container has a fixed width. If the specified width is greater than the width of the parent container, the width of the container matches the width of the parent container. |
   | height | "content", "stretch", or int |  | The height of the form container. This can be one of the following:  "content" (default): The height of the container matches the height of its content. "stretch": The height of the container matches the height of its content or the height of the parent container, whichever is larger. If the container is not in a parent container, the height of the container matches the height of its content. An integer specifying the height in pixels: The container has a fixed height. If the content is larger than the specified height, scrolling is enabled.   Note Use scrolling containers sparingly. If you use scrolling containers, avoid heights that exceed 500 pixels. Otherwise, the scroll surface of the container might cover the majority of the screen on mobile devices, which makes it hard to scroll the rest of the app. |



---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button


* Function signature:

   st.form_submit_button(label="Submit", help=None, on_click=None, args=None, kwargs=None, *, key=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str | s | A short label explaining to the user what this button is for. This defaults to "Submit". The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | help | str or None |  | A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_click | callable |  | An optional callback invoked when this button is clicked. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | type | "primary", "secondary", or "tertiary" |  | An optional string that specifies the button type. This can be one of the following:  "primary": The button's background is the app's primary color for additional emphasis. "secondary" (default): The button's background coordinates with the app's background color for normal emphasis. "tertiary": The button is plain text without a border or background for subtlety. |
   | icon | str or None |  | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols font library. |
   | disabled | bool |  | Whether to disable the button. If this is False (default), the user can interact with the button. If this is True, the button is grayed-out and can't be clicked. If the first st.form_submit_button in the form is disabled, the form will override submission behavior with enter_to_submit=False. |
   | use_container_width | bool |  | Whether to expand the button's width to fill its parent container. If use_container_width is False (default), Streamlit sizes the button to fit its contents. If use_container_width is True, the width of the button matches its parent container. In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
   | width | "content", "stretch", or int |  | The width of the button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |

* Returns: bool

    True if the button was clicked.



---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.fragment


* Function signature:

   st.fragment(func=None, *, run_every=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | func | callable |  | The function to turn into a fragment. |
   | run_every | int, float, timedelta, str, or None |  | The time interval between automatic fragment reruns. This can be one of the following:   None (default). An int or float specifying the interval in seconds. A string specifying the time in a format supported by Pandas' Timedelta constructor, e.g. "1d", "1.5 days", or "1h23s". A timedelta object from Python's built-in datetime library, e.g. timedelta(days=1).   If run_every is None, the fragment will only rerun from user-triggered events. |



---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun


* Function signature:

   st.rerun(*, scope="app")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | scope | "app" or "fragment" |  | Specifies what part of the app should rerun. If scope is "app" (default), the full app reruns. If scope is "fragment", Streamlit only reruns the fragment from which this command is called. Setting scope="fragment" is only valid inside a fragment during a fragment rerun. If st.rerun(scope="fragment") is called during a full-app rerun or outside of a fragment, Streamlit will raise a StreamlitAPIException. |



### Caveats for `st.rerun`

`st.rerun` is one of the tools to control the logic of your app. While it is great for prototyping, there can be adverse side effects:

- Additional script runs may be inefficient and slower.
- Excessive reruns may complicate your app's logic and be harder to follow.
- If misused, infinite looping may crash your app.

In many cases where `st.rerun` works, [callbacks](/develop/api-reference/caching-and-state/st.session_state#use-callbacks-to-update-session-state) may be a cleaner alternative. [Containers](/develop/api-reference/layout) may also be helpful.

### A simple example in three variations

###### Using `st.rerun` to update an earlier header

```python
import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = "Title"

##### Option using st.rerun #####
st.header(st.session_state.value)

if st.button("Foo"):
    st.session_state.value = "Foo"
    st.rerun()
```

###### Using a callback to update an earlier header

```python
##### Option using a callback #####
st.header(st.session_state.value)

def update_value():
    st.session_state.value = "Bar"

st.button("Bar", on_click=update_value)
```

###### Using containers to update an earlier header

```python
##### Option using a container #####
container = st.container()

if st.button("Baz"):
    st.session_state.value = "Baz"

container.header(st.session_state.value)
```

---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.stop


* Function signature:

   st.stop()



---

Source: https://docs.streamlit.io/develop/api-reference/execution-flow/st.experimental_rerun

[Function 'streamlit.experimental_rerun' not found]

---

# Caching and state

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state


Optimize performance and add statefulness to your app!

## Caching

Streamlit provides powerful [cache primitives](/develop/concepts/architecture/caching) for data and global resources. They allow your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.cache_data" size="half">
<h4>Cache data</h4>

Function decorator to cache functions that return data (e.g. dataframe transforms, database queries, ML inference).

```python
@st.cache_data
def long_function(param1, param2):
  # Perform expensive computation here or
  # fetch data from the web here
  return data
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.cache_resource" size="half">
<h4>Cache resource</h4>

Function decorator to cache functions that return global resources (e.g. database connections, ML models).

```python
@st.cache_resource
def init_model():
  # Return a global resource here
  return pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
  )
```

</RefCard>
</TileContainer>

## Browser and server state

Streamlit re-executes your script with each user interaction. Widgets have built-in statefulness between reruns, but Session State lets you do more!

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.context">
<h4>Context</h4>

`st.context` provides a read-only interface to access cookies, headers, locale, and other browser-session information.

```python
st.context.cookies
st.context.headers
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.session_state">
<h4>Session State</h4>

Save data between reruns and across pages.

```python
st.session_state["foo"] = "bar"
```

</RefCard>
<RefCard href="/develop/api-reference/caching-and-state/st.query_params">
<h4>Query parameters</h4>

Get, set, or clear the query parameters that are shown in the browser's URL bar.

```python
st.query_params[key] = value
st.query_params.clear()
```

</RefCard>
</TileContainer>

## Deprecated commands

<TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_get_query_params" size="half">{true}&gt;

<h4>Get query parameters</h4>

Get query parameters that are shown in the browser's URL bar.

```python
param_dict = st.experimental_get_query_params()
```

</RefCard></TileContainer>
<RefCard href="/develop/api-reference/caching-and-state/st.experimental_set_query_params" size="half">{true}&gt;

<h4>Set query parameters</h4>

Set query parameters that are shown in the browser's URL bar.

```python
st.experimental_set_query_params(
  {"show_all"=True, "selected"=["asia", "america"]}
)
```

</RefCard>

---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data

<Tip>

This page only contains information on the `st.cache_data` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

</Tip>

* Function signature:

   st.cache_data(func=None, *, ttl, max_entries, show_spinner, show_time=False, persist, hash_funcs=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | func | callable |  | The function to cache. Streamlit hashes the function's source code. |
   | ttl | float, timedelta, str, or None |  | The maximum time to keep an entry in the cache. Can be one of:  None if cache entries should never expire (default). A number specifying the time in seconds. A string specifying the time in a format supported by Pandas's Timedelta constructor, e.g. "1d", "1.5 days", or "1h23s". A timedelta object from Python's built-in datetime library, e.g. timedelta(days=1).  Note that ttl will be ignored if persist="disk" or persist=True. |
   | max_entries | int or None | None | The maximum number of entries to keep in the cache, or None for an unbounded cache. When a new entry is added to a full cache, the oldest cached entry will be removed. Defaults to None. |
   | show_spinner | bool or str | True | Enable the spinner. Default is True to show a spinner when there is a "cache miss" and the cached data is being created. If string, value of show_spinner param will be used for spinner text. |
   | show_time | bool |  | Whether to show the elapsed time next to the spinner text. If this is False (default), no time is displayed. If this is True, elapsed time is displayed with a precision of 0.1 seconds. The time format is not configurable. |
   | persist | "disk", bool, or None | None | Optional location to persist cached data to. Passing "disk" (or True) will persist the cached data to the local disk. None (or False) will disable persistence. The default is None. |
   | hash_funcs | dict or None |  | Mapping of types or fully qualified names to hash functions. This is used to override the behavior of the hasher inside Streamlit's caching mechanism: when the hasher encounters an object, it will first check to see if its type matches a key in this dict and, if so, will use the provided function to generate a hash for it. See below for an example of how this can be used. |


<Warning>

`st.cache_data` implicitly uses the `pickle` module, which is known to be insecure. Anything your cached function returns is pickled and stored, then unpickled on retrieval. Ensure your cached functions return trusted values because it is possible to construct malicious pickle data that will execute arbitrary code during unpickling. Never load data that could have come from an untrusted source in an unsafe mode or that could have been tampered with. **Only load data you trust**.

</Warning>

* Function signature:

   st.cache_data.clear()



#### Example

In the example below, pressing the "Clear All" button will clear memoized values from all functions decorated with `@st.cache_data`.

```python
import streamlit as st

@st.cache_data
def square(x):
    return x**2

@st.cache_data
def cube(x):
    return x**3

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()
```


* Function signature:

   CachedFunc.clear(*args, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | *args | Any |  | Arguments of the cached functions. |
   | **kwargs | Any |  | Keyword arguments of the cached function. |



## Using Streamlit commands in cached functions

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
@st.cache_data
def get_api_data():
    data = api.get(...)
    st.success("Fetched data from API!")  # 👈 Show a success message
    return data
```

As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_data
def show_data():
    st.header("Data analysis")
    data = api.get(...)
    st.success("Fetched data from API!")
    st.write("Here is a plot of the data:")
    st.line_chart(data)
    st.write("And here is the raw data:")
    st.dataframe(data)
```

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

```python
@st.cache_data(experimental_allow_widgets=True)  # 👈 Set the parameter
def get_data():
    num_rows = st.slider("Number of rows to get")  # 👈 Add a slider
    data = api.get(..., num_rows)
    return data
```

Streamlit treats the slider like an additional input parameter to the cached function. If you change the slider position, Streamlit will see if it has already cached the function for this slider value. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for _every permutation_ of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

<Warning>

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!
</Warning>
<Note>

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!
</Note>

---

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource

<Tip>

This page only contains information on the `st.cache_resource` API. For a deeper dive into caching and how to use it, check out [Caching](/develop/concepts/architecture/caching).

</Tip>

* Function signature:

   st.cache_resource(func, *, ttl, max_entries, show_spinner, show_time=False, validate, hash_funcs=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | func | callable |  | The function that creates the cached resource. Streamlit hashes the function's source code. |
   | ttl | float, timedelta, str, or None |  | The maximum time to keep an entry in the cache. Can be one of:  None if cache entries should never expire (default). A number specifying the time in seconds. A string specifying the time in a format supported by Pandas's Timedelta constructor, e.g. "1d", "1.5 days", or "1h23s". A timedelta object from Python's built-in datetime library, e.g. timedelta(days=1). |
   | max_entries | int or None | None | The maximum number of entries to keep in the cache, or None for an unbounded cache. When a new entry is added to a full cache, the oldest cached entry will be removed. Defaults to None. |
   | show_spinner | bool or str | True | Enable the spinner. Default is True to show a spinner when there is a "cache miss" and the cached resource is being created. If string, value of show_spinner param will be used for spinner text. |
   | show_time | bool |  | Whether to show the elapsed time next to the spinner text. If this is False (default), no time is displayed. If this is True, elapsed time is displayed with a precision of 0.1 seconds. The time format is not configurable. |
   | validate | callable or None |  | An optional validation function for cached data. validate is called each time the cached value is accessed. It receives the cached value as its only parameter and it must return a boolean. If validate returns False, the current cached value is discarded, and the decorated function is called to compute a new value. This is useful e.g. to check the health of database connections. |
   | hash_funcs | dict or None |  | Mapping of types or fully qualified names to hash functions. This is used to override the behavior of the hasher inside Streamlit's caching mechanism: when the hasher encounters an object, it will first check to see if its type matches a key in this dict and, if so, will use the provided function to generate a hash for it. See below for an example of how this can be used. |



* Function signature:

   st.cache_resource.clear()



#### Example

In the example below, pressing the "Clear All" button will clear _all_ cache_resource caches. i.e. Clears cached global resources from all functions decorated with `@st.cache_resource`.

```python
import streamlit as st
from transformers import BertModel

@st.cache_resource
 def get_database_session(url):
     # Create a database session object that points to the URL.
     return session

@st.cache_resource
def get_model(model_type):
    # Create a model of the specified type.
    return BertModel.from_pretrained(model_type)

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()
```


* Function signature:

   CachedFunc.clear(*args, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | *args | Any |  | Arguments of the cached functions. |
   | **kwargs | Any |  | Keyword arguments of the cached function. |



## Using Streamlit commands in cached functions

### Static elements

Since version 1.16.0, cached functions can contain Streamlit commands! For example, you can do this:

```python
from transformers import pipeline

@st.cache_resource
def load_model():
    model = pipeline("sentiment-analysis")
    st.success("Loaded NLP model from Hugging Face!")  # 👈 Show a success message
    return model
```

As we know, Streamlit only runs this function if it hasn’t been cached before. On this first run, the `st.success` message will appear in the app. But what happens on subsequent runs? It still shows up! Streamlit realizes that there is an `st.` command inside the cached function, saves it during the first run, and replays it on subsequent runs. Replaying static elements works for both caching decorators.

You can also use this functionality to cache entire parts of your UI:

```python
@st.cache_resource
def load_model():
    st.header("Data analysis")
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT)
    st.success("Loaded model!")
    st.write("Turning on evaluation mode...")
    model.eval()
    st.write("Here's the model:")
    return model
```

### Input widgets

You can also use [interactive input widgets](/develop/api-reference/widgets) like `st.slider` or `st.text_input` in cached functions. Widget replay is an experimental feature at the moment. To enable it, you need to set the `experimental_allow_widgets` parameter:

```python
@st.cache_resource(experimental_allow_widgets=True)  # 👈 Set the parameter
def load_model():
    pretrained = st.checkbox("Use pre-trained model:")  # 👈 Add a checkbox
    model = torchvision.models.resnet50(weights=ResNet50_Weights.DEFAULT, pretrained=pretrained)
    return model
```

Streamlit treats the checkbox like an additional input parameter to the cached function. If you uncheck it, Streamlit will see if it has already cached the function for this checkbox state. If yes, it will return the cached value. If not, it will rerun the function using the new slider value.

Using widgets in cached functions is extremely powerful because it lets you cache entire parts of your app. But it can be dangerous! Since Streamlit treats the widget value as an additional input parameter, it can easily lead to excessive memory usage. Imagine your cached function has five sliders and returns a 100 MB DataFrame. Then we’ll add 100 MB to the cache for _every permutation_ of these five slider values – even if the sliders do not influence the returned data! These additions can make your cache explode very quickly. Please be aware of this limitation if you use widgets in cached functions. We recommend using this feature only for isolated parts of your UI where the widgets directly influence the cached return value.

<Warning>

Support for widgets in cached functions is currently experimental. We may change or remove it anytime without warning. Please use it with care!
</Warning>
<Note>

Two widgets are currently not supported in cached functions: `st.file_uploader` and `st.camera_input`. We may support them in the future. Feel free to [open a GitHub issue](https://github.com/streamlit/streamlit/issues) if you need them!
</Note>

---

# Session State

Source: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state


Session State is a way to share variables between reruns, for each user session. In addition to the ability to store and persist state, Streamlit also exposes the ability to manipulate state using Callbacks. Session state also persists across apps inside a [multipage app](/develop/concepts/multipage-apps).

Check out this Session State basics tutorial video by Streamlit Developer Advocate Dr. Marisa Smith to get started:

<YouTube videoId="92jUAXBmZyU"/>

### Initialize values in Session State

The Session State API follows a field-based API, which is very similar to Python dictionaries:

```python
# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
```

### Reads and updates

Read the value of an item in Session State and display it by passing to `st.write` :

```python
# Read
st.write(st.session_state.key)

# Outputs: value
```

Update an item in Session State by assigning it a value:

```python
st.session_state.key = 'value2'     # Attribute API
st.session_state['key'] = 'value2'  # Dictionary like API
```

Curious about what is in Session State? Use `st.write` or magic:

```python
st.write(st.session_state)

# With magic:
st.session_state
```

Streamlit throws a handy exception if an uninitialized variable is accessed:

```python
st.write(st.session_state['value'])

# Throws an exception!
```

![state-uninitialized-exception](/images/state_uninitialized_exception.png)

### Delete items

Delete items in Session State using the syntax to delete items in any Python dictionary:

```python
# Delete a single key-value pair
del st.session_state[key]

# Delete all the items in Session state
for key in st.session_state.keys():
    del st.session_state[key]
```

Session State can also be cleared by going to Settings → Clear Cache, followed by Rerunning the app.

![state-clear-cache](/images/clear_cache.png)

### Session State and Widget State association

Every widget with a key is automatically added to Session State:

```python
st.text_input("Your name", key="name")

# This exists now:
st.session_state.name
```

### Use Callbacks to update Session State

A callback is a python function which gets called when an input widget changes.

**Order of execution**: When updating Session state in response to **events**, a callback function gets executed first, and then the app is executed from top to bottom.

Callbacks can be used with widgets using the parameters `on_change` (or `on_click`), `args`, and `kwargs`:

**Parameters**

- **on_change** or **on_click** - The function name to be used as a callback
- **args** (_tuple_) - List of arguments to be passed to the callback function
- **kwargs** (_dict_) - Named arguments to be passed to the callback function

Widgets which support the `on_change` event:

- `st.checkbox`
- `st.color_picker`
- `st.date_input`
- `st.data_editor`
- `st.file_uploader`
- `st.multiselect`
- `st.number_input`
- `st.radio`
- `st.select_slider`
- `st.selectbox`
- `st.slider`
- `st.text_area`
- `st.text_input`
- `st.time_input`
- `st.toggle`

Widgets which support the `on_click` event:

- `st.button`
- `st.download_button`
- `st.form_submit_button`

To add a callback, define a callback function **above** the widget declaration and pass it to the widget via the `on_change` (or `on_click` ) parameter.

### Forms and Callbacks

Widgets inside a form can have their values be accessed and set via the Session State API. `st.form_submit_button` can have a callback associated with it. The callback gets executed upon clicking on the submit button. For example:

```python
def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
```

### Serializable Session State

Serialization refers to the process of converting an object or data structure into a format that can be persisted and shared, and allowing you to recover the data’s original structure. Python’s built-in [pickle](https://docs.python.org/3/develop/pickle.html) module serializes Python objects to a byte stream ("pickling") and deserializes the stream into an object ("unpickling").

By default, Streamlit’s [Session State](/develop/concepts/architecture/session-state) allows you to persist any Python object for the duration of the session, irrespective of the object’s pickle-serializability. This property lets you store Python primitives such as integers, floating-point numbers, complex numbers and booleans, dataframes, and even [lambdas](https://docs.python.org/3/reference/expressions.html#lambda) returned by functions. However, some execution environments may require serializing all data in Session State, so it may be useful to detect incompatibility during development, or when the execution environment will stop supporting it in the future.

To that end, Streamlit provides a `runner.enforceSerializableSessionState` [configuration option](/develop/concepts/configuration) that, when set to `true`, only allows pickle-serializable objects in Session State. To enable the option, either create a global or project config file with the following or use it as a command-line flag:

```toml

---

**Navigation:** [← Previous](./05-bottom-panel-is-a-bar-chart-of-weather-type.md) | [Index](./index.md) | [Next →](./07-streamlitconfigtoml.md)
