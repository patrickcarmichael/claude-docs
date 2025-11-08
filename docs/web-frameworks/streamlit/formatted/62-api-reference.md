---
title: "API reference"
source: https://docs.streamlit.io/develop/api-reference
section: 62
---

# API reference

Source: https://docs.streamlit.io/develop/api-reference


Streamlit makes it easy for you to visualize, mutate, and share data. The API
reference is organized by activity type, like displaying data or optimizing
performance. Each section includes methods associated with the activity type,
including examples.

Browse our API below and click to learn more about any of our available commands! 🎈

## Display almost anything

### Write and magic

<br/>
<TileContainer>
<RefCard href="/develop/api-reference/write-magic/st.write">
<h4>st.write</h4>

Write arguments to the app.

```python
st.write("Hello **world**!")
st.write(my_data_frame)
st.write(my_mpl_figure)
```python
</RefCard>
<RefCard href="/develop/api-reference/write-magic/st.write_stream">
<h4>st.write_stream</h4>

Write generators or streams to the app with a typewriter effect.

```python
st.write_stream(my_generator)
st.write_stream(my_llm_stream)
```python
</RefCard>
<RefCard href="/develop/api-reference/write-magic/magic">
<h4>Magic</h4>

Any time Streamlit sees either a variable or literal value on its own line, it automatically writes that to your app using `st.write`

```python
"Hello **world**!"
my_data_frame
my_mpl_figure
```python
</RefCard>
</TileContainer>

### Text elements

<br/>
<TileContainer>
<RefCard href="/develop/api-reference/text/st.markdown">
<Image>alt="screenshot" src="/images/api/markdown.jpg" /&gt;

<h4>Markdown</h4>

Display string formatted as Markdown.

```python
st.markdown("Hello **world**!")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.title">
<Image>alt="screenshot" src="/images/api/title.jpg" /&gt;

<h4>Title</h4>

Display text in title formatting.

```python
st.title("The app title")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.header">
<Image>alt="screenshot" src="/images/api/header.jpg" /&gt;

<h4>Header</h4>

Display text in header formatting.

```python
st.header("This is a header")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.subheader">
<Image>alt="screenshot" src="/images/api/subheader.jpg" /&gt;

<h4>Subheader</h4>

Display text in subheader formatting.

```python
st.subheader("This is a subheader")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.badge">
<Image>alt="screenshot" src="/images/api/badge.jpg" /&gt;

<h4>Badge</h4>

Display a small, colored badge.

```python
st.badge("New")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.caption">
<Image>alt="screenshot" src="/images/api/caption.jpg" /&gt;

<h4>Caption</h4>

Display text in small font.

```python
st.caption("This is written small caption text")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.code">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Code block</h4>

Display a code block with optional syntax highlighting.

```python
st.code("a = 1234")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.echo">
<Image>alt="screenshot" src="/images/api/code.jpg" /&gt;

<h4>Echo</h4>

Display some code in the app, then execute it. Useful for tutorials.

```python
with st.echo():
  st.write('This code will be printed')
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.latex">
<Image>alt="screenshot" src="/images/api/latex.jpg" /&gt;

<h4>LaTeX</h4>

Display mathematical expressions formatted as LaTeX.

```python
st.latex("\int a x^2 \,dx")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.text">
<Image>alt="screenshot" src="/images/api/text.jpg" /&gt;

<h4>Preformatted text</h4>

Write fixed-width and preformatted text.

```python
st.text("Hello world")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.divider">
<Image>alt="screenshot" src="/images/api/divider.jpg" /&gt;

<h4>Divider</h4>

Display a horizontal rule.

```python
st.divider()
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/text/st.help">
<h4>Get help</h4>

Display object’s doc string, nicely formatted.

```python
st.help(st.write)
st.help(pd.DataFrame)
```python
</RefCard>
<RefCard href="/develop/api-reference/text/st.html">
<h4>Render HTML</h4>

Renders HTML strings to your app.

```python
st.html("<p>Foo bar.</p>")
```python
</RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/tvst/st-annotated-text">
<Image>alt="screenshot" src="/images/api/components/annotated-text.jpg" /&gt;

<h4>Annotated text</h4>

Display annotated text in Streamlit apps. Created by [@tvst](https://github.com/tvst).

```python
annotated_text("This ", ("is", "verb"), " some ", ("annotated", "adj"), ("text", "noun"), " for those of ", ("you", "pronoun"), " who ", ("like", "verb"), " this sort of ", ("thing", "noun"), ".")
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-drawable-canvas">
<Image>alt="screenshot" src="/images/api/components/drawable-canvas.jpg" /&gt;

<h4>Drawable Canvas</h4>

Provides a sketching canvas using [Fabric.js](http://fabricjs.com/). Created by [@andfanilo](https://github.com/andfanilo).

```python
st_canvas(fill_color="rgba(255, 165, 0, 0.3)", stroke_width=stroke_width, stroke_color=stroke_color, background_color=bg_color, background_image=Image.open(bg_image) if bg_image else None, update_streamlit=realtime_update, height=150, drawing_mode=drawing_mode, point_display_radius=point_display_radius if drawing_mode == 'point' else 0, key="canvas",)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/gagan3012/streamlit-tags">
<Image>alt="screenshot" src="/images/api/components/tags.jpg" /&gt;

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'], suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/JohnSnowLabs/nlu">
<Image>alt="screenshot" src="/images/api/components/nlu.jpg" /&gt;

<h4>NLU</h4>

Apply text mining on a dataframe. Created by [@JohnSnowLabs](https://github.com/JohnSnowLabs/).

```python
nlu.load("sentiment").predict("I love NLU! </Image></ComponentCard></ComponentSlider>

---

[← Previous](61-app-testing-cheat-sheet.md) | [Index](index.md) | [Next →](index.md)
