---
title: "Data elements"
source: https://docs.streamlit.io/develop/api-reference/data
section: 81
---

# Data elements

Source: https://docs.streamlit.io/develop/api-reference/data


When you're working with data, it is extremely valuable to visualize that
data quickly, interactively, and from multiple different angles. That's what
Streamlit is actually built and optimized for.

You can display data via [charts](#display-charts), and you can display it in
raw form. These are the Streamlit commands you can use to display and interact with raw data.

<TileContainer>
<RefCard href="/develop/api-reference/data/st.dataframe">
<Image>alt="screenshot" src="/images/api/dataframe.jpg" /&gt;

<h4>Dataframes</h4>

Display a dataframe as an interactive table.

```python
st.dataframe(my_data_frame)
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
<RefCard href="/develop/api-reference/data/st.column_config">
<Image>alt="screenshot" src="/images/api/column_config.jpg" /&gt;

<h4>Column configuration</h4>

Configure the display and editing behavior of dataframes and data editors.

```python
st.column_config.NumberColumn("Price (in USD)", min_value=0, format="$%d")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.table">
<Image>alt="screenshot" src="/images/api/table.jpg" /&gt;

<h4>Static tables</h4>

Display a static table.

```python
st.table(my_data_frame)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.metric">
<Image>alt="screenshot" src="/images/api/metric.jpg" /&gt;

<h4>Metrics</h4>

Display a metric in big bold font, with an optional indicator of how the metric changed.

```python
st.metric("My metric", 42, 2)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.json">
<Image>alt="screenshot" src="/images/api/json.jpg" /&gt;

<h4>Dicts and JSON</h4>

Display object or string as a pretty-printed JSON string.

```python
st.json(my_dict)
```python
</Image></RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/PablocFonseca/streamlit-aggrid">
<Image>alt="screenshot" src="/images/api/components/aggrid.jpg" /&gt;

<h4>Streamlit Aggrid</h4>

Implementation of Ag-Grid component for Streamlit. Created by [@PablocFonseca](https://github.com/PablocFonseca).

```python
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)

new_df = grid_return['data']
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">
<Image>alt="screenshot" src="/images/api/components/folium.jpg" /&gt;

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker([39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

st_data = st_folium(m, width=725)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/okld/streamlit-pandas-profiling">
<Image>alt="screenshot" src="/images/api/components/pandas-profiling.jpg" /&gt;

<h4>Pandas Profiling</h4>

Pandas profiling component for Streamlit. Created by [@okld](https://github.com/okld/).

```python
df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-image-coordinates">
<Image>alt="screenshot" src="/images/api/components/image-coordinates.jpg" /&gt;

<h4>Image Coordinates</h4>

Get the coordinates of clicks on an image. Created by [@blackary](https://github.com/blackary/).

```python
from streamlit_image_coordinates import streamlit_image_coordinates
value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)
```python
</Image></ComponentCard>
<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">
<Image>alt="screenshot" src="/images/api/components/plotly-events.jpg" /&gt;

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
from streamlit_plotly_events import plotly_events
fig = px.line(x=[1], y=[1])

selected_points = plotly_events(fig)
```python
</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-metric-cards.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.metric_cards import style_metric_cards
col3.metric(label="No Change", value=5000, delta=0)

style_metric_cards()
```python
</Image></ComponentCard>
</ComponentSlider>

---

[← Previous](67-text-elements.md) | [Index](index.md) | [Next →](index.md)
