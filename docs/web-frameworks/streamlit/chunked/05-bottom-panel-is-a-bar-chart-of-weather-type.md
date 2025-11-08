**Navigation:** [← Previous](./04-column-configuration.md) | [Index](./index.md) | [Next →](./06-store-the-initial-value-of-widgets-in-session-stat.md)

---

# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=source, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
```

</Collapse>

Notice how the custom colors are still reflected in the chart, even when the Streamlit theme is enabled 👇

<Cloud height="675px" name="doc-altair-custom-colors"/>

For many more examples of Altair charts with and without the Streamlit theme, check out the [altair.streamlit.app](https://altair.streamlit.app).

---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.bokeh_chart


* Function signature:

   st.bokeh_chart(figure, use_container_width=True)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | figure | bokeh.plotting.figure.Figure |  | A Bokeh figure to plot. |
   | use_container_width | bool |  | Whether to override the figure's native width with the width of the parent container. If use_container_width is True (default), Streamlit sets the width of the figure to match the width of the parent container. If use_container_width is False, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.graphviz_chart


* Function signature:

   st.graphviz_chart(figure_or_dot, use_container_width=None, *, width="content", height="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | figure_or_dot | graphviz.dot.Graph, graphviz.dot.Digraph, graphviz.sources.Source, str |  | The Graphlib graph object or dot string to display |
   | use_container_width | bool |  | Whether to override the figure's native width with the width of the parent container. If use_container_width is False (default), Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. If use_container_width is True, Streamlit sets the width of the figure to match the width of the parent container. |
   | width | "content", "stretch", or int |  | The width of the chart element. This can be one of the following:  "content" (default): The width of the element matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "content", "stretch", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart


* Function signature:

   st.plotly_chart(figure_or_data, use_container_width=None, *, width="stretch", theme="streamlit", key=None, on_select="ignore", selection_mode=('points', 'box', 'lasso'), config=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | figure_or_data | plotly.graph_objs.Figure, plotly.graph_objs.Data,            or dict/list of plotly.graph_objs.Figure/Data |  | The Plotly Figure or Data object to render. See https://plot.ly/python/ for examples of graph descriptions.  Note If your chart contains more than 1000 data points, Plotly will use a WebGL renderer to display the chart. Different browsers have different limits on the number of WebGL contexts per page. If you have multiple WebGL contexts on a page, you may need to switch to SVG rendering mode. You can do this by setting render_mode="svg" within the figure. For example, the following code defines a Plotly Express line chart that will render in SVG mode when passed to st.plotly_chart: px.line(df, x="x", y="y", render_mode="svg"). |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | use_container_width | bool or None |  | Whether to override the figure's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the value of width. True: Streamlit sets the width of the figure to match the width of the parent container. False: Streamlit sets the width of the figure to fit its contents according to the plotting library, up to the width of the parent container. |
   | theme | "streamlit" or None | behavior | The theme of the chart. If theme is "streamlit" (default), Streamlit uses its own design default. If theme is None, Streamlit falls back to the default behavior of the library. The "streamlit" theme can be partially customized through the configuration options theme.chartCategoricalColors and theme.chartSequentialColors. Font configuration options are also applied. |
   | key | str |  | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters. Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |
   | on_select | "ignore" or "rerun" or callable |  | How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget. on_select can be one of the following:  "ignore" (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget. "rerun": Streamlit will rerun the app when the user selects data in the chart. In this case, st.plotly_chart will return the selection data as a dictionary. A callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.plotly_chart will return the selection data as a dictionary. |
   | selection_mode | "points", "box", "lasso" or an Iterable of these |  | The selection mode of the chart. This can be one of the following:  "points": The chart will allow selections based on individual data points. "box": The chart will allow selections based on rectangular areas. "lasso": The chart will allow selections based on freeform areas. An Iterable of the above options: The chart will allow selections based on the modes specified.  All selections modes are activated by default. |
   | config | dict or None |  | A dictionary of Plotly configuration options. This is passed to Plotly's show() function. For more information about Plotly configuration options, see Plotly's documentation on Configuration in Python. |
   | **kwargs | None |  | Additional arguments accepted by Plotly's plot() function. This supports config, a dictionary of Plotly configuration options. For more information about Plotly configuration options, see Plotly's documentation on Configuration in Python. |

* Returns: element or dict

    If on_select is "ignore" (default), this command returns an
internal placeholder for the chart element. Otherwise, this command
returns a dictionary-like object that supports both key and
attribute notation. The attributes are described by the
PlotlyState dictionary schema.



## Chart selections


* Function signature:

   PlotlyState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | selection | dict |  | The state of the on_select event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the PlotlySelectionState dictionary schema. |



* Function signature:

   PlotlySelectionState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | points | list[dict[str, Any]] |  | The selected data points in the chart, including the data points selected by the box and lasso mode. The data includes the values associated to each point and a point index used to populate point_indices. If additional information has been assigned to your points, such as size or legend group, this is also included. |
   | point_indices | list[int] |  | The numerical indices of all selected data points in the chart. The details of each identified point are included in points. |
   | box | list[dict[str, Any]] |  | The metadata related to the box selection. This includes the coordinates of the selected area. |
   | lasso | list[dict[str, Any]] |  | The metadata related to the lasso selection. This includes the coordinates of the selected area. |



## Theming

Plotly charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Plotly's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Plotly theme:

```python
import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud height="525px" name="doc-plotly-chart-theme"/>

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Plotly chart where a custom color scale is defined and reflected:

```python
import plotly.express as px
import streamlit as st

st.subheader("Define a custom colorscale")
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
```

Notice how the custom color scale is still reflected in the chart, even when the Streamlit theme is enabled 👇

<Cloud height="650px" name="doc-plotly-custom-colors"/>

For many more examples of Plotly charts with and without the Streamlit theme, check out the [plotly.streamlit.app](https://plotly.streamlit.app).

---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.pydeck_chart


* Function signature:

   st.pydeck_chart(pydeck_obj=None, *, width="stretch", use_container_width=None, height=500, selection_mode="single-object", on_select="ignore", key=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | pydeck_obj | pydeck.Deck or None |  | Object specifying the PyDeck chart to draw. |
   | width | "stretch" or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | use_container_width | bool or None | behavior | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the chart's default behavior. True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
   | height | "stretch" or int |  | The height of the chart element. This can be one of the following:  An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. This is 500 by default. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. |
   | on_select | "ignore" or "rerun" or callable |  | How the figure should respond to user selection events. This controls whether or not the chart behaves like an input widget. on_select can be one of the following:  "ignore" (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget. "rerun": Streamlit will rerun the app when the user selects data in the chart. In this case, st.pydeck_chart will return the selection data as a dictionary. A callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.pydeck_chart will return the selection data as a dictionary.  If on_select is not "ignore", all layers must have a declared id to keep the chart stateful across reruns. |
   | selection_mode | "single-object" or "multi-object" |  | The selection mode of the chart. This can be one of the following:  "single-object" (default): Only one object can be selected at a time. "multi-object": Multiple objects can be selected at a time. |
   | key | str |  | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters. Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |

* Returns: element or dict

    If on_select is "ignore" (default), this command returns an
internal placeholder for the chart element. Otherwise, this method
returns a dictionary-like object that supports both key and
attribute notation. The attributes are described by the
PydeckState dictionary schema.



## Chart selections


* Function signature:

   PydeckState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | selection | dict |  | The state of the on_select event. This attribute returns a dictionary-like object that supports both key and attribute notation. The attributes are described by the PydeckSelectionState dictionary schema. |



* Function signature:

   PydeckSelectionState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | indices | dict[str, list[int]] |  | A dictionary of selected objects by layer. Each key in the dictionary is a layer id, and each value is a list of object indices within that layer. |
   | objects | dict[str, list[dict[str, Any]]] |  | A dictionary of object attributes by layer. Each key in the dictionary is a layer id, and each value is a list of metadata dictionaries for the selected objects in that layer. |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.pyplot


* Function signature:

   st.pyplot(fig=None, clear_figure=None, *, width="stretch", use_container_width=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | fig | Matplotlib Figure |  | The Matplotlib Figure object to render. See https://matplotlib.org/stable/gallery/index.html for examples.  Note When this argument isn't specified, this function will render the global Matplotlib figure object. However, this feature is deprecated and will be removed in a later version. |
   | clear_figure | bool | based | If True, the figure will be cleared after being rendered. If False, the figure will not be cleared after being rendered. If left unspecified, we pick a default based on the value of fig.  If fig is set, defaults to False. If fig is not set, defaults to True. This simulates Jupyter's approach to matplotlib rendering. |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | use_container_width | bool |  | Whether to override the figure's native width with the width of the parent container. If use_container_width is True (default), Streamlit sets the width of the figure to match the width of the parent container. If use_container_width is False, Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
   | **kwargs | any |  | Arguments to pass to Matplotlib's savefig function. |


<Warning>
    Matplotlib [doesn't work well with threads](https://matplotlib.org/3.3.2/faq/howto_faq.html#working-with-threads). So if you're using Matplotlib you should wrap your code with locks. This Matplotlib bug is more prominent when you deploy and share your apps because you're more likely to get concurrent users then. The following example uses [`Rlock`](https://docs.python.org/3/library/threading.html#rlock-objects) from the `threading` module.

    ```python
    import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np
    from threading import RLock

    _lock = RLock()

    x = np.random.normal(1, 1, 100)
    y = np.random.normal(1, 1, 100)

    with _lock:
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        st.pyplot(fig)
    ```

</Warning>

---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.vega_lite_chart


* Function signature:

   st.vega_lite_chart(data=None, spec=None, *, width=None, height="content", use_container_width=None, theme="streamlit", key=None, on_select="ignore", selection_mode=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | Either the data to be plotted or a Vega-Lite spec containing the data (which more closely follows the Vega-Lite API). |
   | spec | dict or None |  | The Vega-Lite spec for the chart. If spec is None (default), Streamlit uses the spec passed in data. You cannot pass a spec to both data and spec. See https://vega.github.io/vega-lite/docs/ for more info. |
   | width | "stretch", "content", int, or None |  | The width of the chart element. This can be one of the following:  "stretch": The width of the element matches the width of the parent container.  "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.  An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.  None (default): Streamlit uses "stretch" for most charts, and uses "content" for the following multi-view charts:   Facet charts: the spec contains "facet" or encodings for "row", "column", or "facet". Horizontal concatenation charts: the spec contains "hconcat". Repeat charts: the spec contains "repeat". |
   | height | "content", "stretch", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None |  | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the parent container's width for all charts except those with known incompatibility (altair.Facet, altair.HConcatChart, and altair.RepeatChart). True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
   | theme | "streamlit" or None | behavior | The theme of the chart. If theme is "streamlit" (default), Streamlit uses its own design default. If theme is None, Streamlit falls back to the default behavior of the library. The "streamlit" theme can be partially customized through the configuration options theme.chartCategoricalColors and theme.chartSequentialColors. Font configuration options are also applied. |
   | key | str |  | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters. Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |
   | on_select | "ignore", "rerun", or callable |  | How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget. on_select can be one of the following:  "ignore" (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget. "rerun": Streamlit will rerun the app when the user selects data in the chart. In this case, st.vega_lite_chart will return the selection data as a dictionary. A callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.vega_lite_chart will return the selection data as a dictionary.  To use selection events, the Vega-Lite spec defined in data or spec must include selection parameters from the charting library. To learn about defining interactions in Vega-Lite, see Dynamic Behaviors with Parameters in Vega-Lite's documentation. |
   | selection_mode | str or Iterable of str |  | The selection parameters Streamlit should use. If selection_mode is None (default), Streamlit will use all selection parameters defined in the chart's Vega-Lite spec. When Streamlit uses a selection parameter, selections from that parameter will trigger a rerun and be included in the selection state. When Streamlit does not use a selection parameter, selections from that parameter will not trigger a rerun and not be included in the selection state. Selection parameters are identified by their name property. |
   | **kwargs | any |  | The Vega-Lite spec for the chart as keywords. This is an alternative to spec. |

* Returns: element or dict

    If on_select is "ignore" (default), this command returns an
internal placeholder for the chart element that can be used with
the .add_rows() method. Otherwise, this command returns a
dictionary-like object that supports both key and attribute
notation. The attributes are described by the VegaLiteState
dictionary schema.



## Chart selections


* Function signature:

   VegaLiteState

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | selection | dict |  | The state of the on_select event. This attribute returns a dictionary-like object that supports both key and attribute notation. The name of each Vega-Lite selection parameter becomes an attribute in the selection dictionary. The format of the data within each attribute is determined by the selection parameter definition within Vega-Lite. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



## Theming

Vega-Lite charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Vega-Lite's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Vega-Lite theme:

```python
import streamlit as st
from vega_datasets import data

source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud height="500px" name="doc-vega-lite-theme"/>

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.download_button">
<Image>alt="screenshot" src="/images/api/download_button.svg" /&gt;

<h4>Download button</h4>

Display a download button widget.

```python
st.download_button("Download file", file)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/execution-flow/st.form_submit_button">
<Image>alt="screenshot" src="/images/api/form_submit_button.svg" /&gt;

<h4>Form button</h4>

Display a form submit button. For use with `st.form`.

```python
st.form_submit_button("Sign up")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.link_button">
<Image>alt="screenshot" src="/images/api/link_button.svg" /&gt;

<h4>Link button</h4>

Display a link button.

```python
st.link_button("Go to gallery", url)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.page_link">
<Image>alt="screenshot" src="/images/api/page_link.jpg" /&gt;

<h4>Page link</h4>

Display a link to another page in a multipage app.

```python
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/profile.py", label="My profile")
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.color_picker">
<Image>alt="screenshot" src="/images/api/color_picker.jpg" /&gt;

<h4>Color picker</h4>

Display a color picker widget.

```python
color = st.color_picker("Pick a color")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.feedback">
<Image>alt="screenshot" src="/images/api/feedback.jpg" /&gt;

<h4>Feedback</h4>

Display a rating or sentiment button group.

```python
st.feedback("stars")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.multiselect">
<Image>alt="screenshot" src="/images/api/multiselect.jpg" /&gt;

<h4>Multiselect</h4>

Display a multiselect widget. The multiselect widget starts as empty.

```python
choices = st.multiselect("Buy", ["milk", "apples", "potatoes"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.pills">
<Image>alt="screenshot" src="/images/api/pills.jpg" /&gt;

<h4>Pills</h4>

Display a pill-button selection widget.

```python
st.pills("Tags", ["Sports", "AI", "Politics"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.radio">
<Image>alt="screenshot" src="/images/api/radio.jpg" /&gt;

<h4>Radio</h4>

Display a radio button widget.

```python
choice = st.radio("Pick one", ["cats", "dogs"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.segmented_control">
<Image>alt="screenshot" src="/images/api/segmented_control.jpg" /&gt;

<h4>Segmented control</h4>

Display a segmented-button selection widget.

```python
st.segmented_control("Filter", ["Open", "Closed", "All"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.select_slider">
<Image>alt="screenshot" src="/images/api/select_slider.jpg" /&gt;

<h4>Select slider</h4>

Display a slider widget to select items from a list.

```python
size = st.select_slider("Pick a size", ["S", "M", "L"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.selectbox">
<Image>alt="screenshot" src="/images/api/selectbox.jpg" /&gt;

<h4>Selectbox</h4>

Display a select widget.

```python
choice = st.selectbox("Pick one", ["cats", "dogs"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.toggle">
<Image>alt="screenshot" src="/images/api/toggle.jpg" /&gt;

<h4>Toggle</h4>

Display a toggle widget.

```python
activated = st.toggle("Activate")
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.slider">
<Image>alt="screenshot" src="/images/api/slider.jpg" /&gt;

<h4>Slider</h4>

Display a slider widget.

```python
number = st.slider("Pick a number", 0, 100)
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.time_input">
<Image>alt="screenshot" src="/images/api/time_input.jpg" /&gt;

<h4>Time input</h4>

Display a time input widget.

```python
time = st.time_input("Meeting time")
```

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.text_area">
<Image>alt="screenshot" src="/images/api/text_area.jpg" /&gt;

<h4>Text area</h4>

Display a multi-line text input widget.

```python
text = st.text_area("Text to translate")
```

</Image></RefCard>
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
</TileContainer>

## Other input elements

<TileContainer>
<RefCard href="/develop/api-reference/widgets/st.audio_input">
<Image>alt="screenshot" src="/images/api/audio_input.jpg" /&gt;

<h4>Audio input</h4>

Display a widget that allows users to record with their microphone.

```python
speech = st.audio_input("Record a voice message")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.data_editor">
<Image>alt="screenshot" src="/images/api/data_editor.jpg" /&gt;

<h4>Data editor</h4>

Display a data editor widget.

```python
edited = st.data_editor(df, num_rows="dynamic")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.file_uploader">
<Image>alt="screenshot" src="/images/api/file_uploader.jpg" /&gt;

<h4>File uploader</h4>

Display a file uploader widget.

```python
data = st.file_uploader("Upload a CSV")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/widgets/st.camera_input">
<Image>alt="screenshot" src="/images/api/camera_input.jpg" /&gt;

<h4>Camera input</h4>

Display a widget that allows users to upload images directly from a camera.

```python
image = st.camera_input("Take a picture")
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
<ComponentCard href="https://github.com/gagan3012/streamlit-tags">
<Image>alt="screenshot" src="/images/api/components/tags.jpg" /&gt;

<h4>Tags</h4>

Add tags to your Streamlit apps. Created by [@gagan3012](https://github.com/gagan3012).

```python
from streamlit_tags import st_tags

st_tags(label='# Enter Keywords:', text='Press enter to add more', value=['Zero', 'One', 'Two'],
suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'], maxtags = 4, key='1')
```

</Image></ComponentCard>
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
<ComponentCard href="https://github.com/innerdoc/streamlit-timeline">
<Image>alt="screenshot" src="/images/api/components/timeline.jpg" /&gt;

<h4>Timeline</h4>

Display a Timeline in Streamlit apps using [TimelineJS](https://timeline.knightlab.com/). Created by [@innerdoc](https://github.com/innerdoc).

```python
from streamlit_timeline import timeline

with open('example.json', "r") as f:
  timeline(f.read(), height=800)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/blackary/streamlit-camera-input-live">
<Image>alt="screenshot" src="/images/api/components/camera-live.jpg" /&gt;

<h4>Camera input live</h4>

Alternative for st.camera_input which returns the webcam images live. Created by [@blackary](https://github.com/blackary).

```python
from camera_input_live import camera_input_live

image = camera_input_live()
st.image(value)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/okld/streamlit-ace">
<Image>alt="screenshot" src="/images/api/components/ace.jpg" /&gt;

<h4>Streamlit Ace</h4>

Ace editor component for Streamlit. Created by [@okld](https://github.com/okld).

```python
from streamlit_ace import st_ace

content = st_ace()
content
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/AI-Yash/st-chat">
<Image>alt="screenshot" src="/images/api/components/chat.jpg" /&gt;

<h4>Streamlit Chat</h4>

Streamlit Component for a Chatbot UI. Created by [@AI-Yash](https://github.com/AI-Yash).

```python
from streamlit_chat import message

message("My message")
message("Hello bot!", is_user=True)  # align's the message to the right
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/victoryhb/streamlit-option-menu">
<Image>alt="screenshot" src="/images/api/components/option-menu.jpg" /&gt;

<h4>Streamlit Option Menu</h4>

Select a single item from a list of options in a menu. Created by [@victoryhb](https://github.com/victoryhb).

```python
from streamlit_option_menu import option_menu

option_menu("Main Menu", ["Home", 'Settings'],
  icons=['house', 'gear'], menu_icon="cast", default_index=1)
```

</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-toggle.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
from streamlit_extras.stoggle import stoggle

stoggle(
    "Click me!", """🥷 Surprise! Here's some additional content""",)
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.button


* Function signature:

   st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_click | callable |  | An optional callback invoked when this button is clicked. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | type | "primary", "secondary", or "tertiary" |  | An optional string that specifies the button type. This can be one of the following:  "primary": The button's background is the app's primary color for additional emphasis. "secondary" (default): The button's background coordinates with the app's background color for normal emphasis. "tertiary": The button is plain text without a border or background for subtlety. |
   | icon | str or None |  | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | disabled | bool | is | An optional boolean that disables the button if set to True. The default is False. |
   | use_container_width | bool |  | Whether to expand the button's width to fill its parent container. If use_container_width is False (default), Streamlit sizes the button to fit its contents. If use_container_width is True, the width of the button matches its parent container. In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
   | width | "content", "stretch", or int |  | The width of the button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |

* Returns: bool

    True if the button was clicked on the last run of the app,
False otherwise.



### Advanced functionality

Although a button is the simplest of input widgets, it's very common for buttons to be deeply tied to the use of [`st.session_state`](/develop/api-reference/caching-and-state/st.session_state). Check out our advanced guide on [Button behavior and examples](/develop/concepts/design/buttons).

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the button!

<YouTube videoId="JSeQSnGovSE"/>

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)!

<YouTube videoId="EnXJBsCIl_A"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.download_button


* Function signature:

   st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click="rerun", args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | data | str, bytes, or file |  | The contents of the file to be downloaded. To prevent unncecessary recomputation, use caching when converting your data for download. For more information, see the Example 1 below. |
   | file_name | str |  | An optional string to use as the name of the file to be downloaded, such as "my_file.csv". If not specified, the name will be automatically generated. |
   | mime | str or None |  | The MIME type of the data. If this is None (default), Streamlit sets the MIME type depending on the value of data as follows:  If data is a string or textual file (i.e. str or io.TextIOWrapper object), Streamlit uses the "text/plain" MIME type. If data is a binary file or bytes (i.e. bytes, io.BytesIO, io.BufferedReader, or io.RawIOBase object), Streamlit uses the "application/octet-stream" MIME type.  For more information about MIME types, see https://www.iana.org/assignments/media-types/media-types.xhtml. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_click | callable, "rerun", "ignore", or None |  | How the button should respond to user interaction. This controls whether or not the button triggers a rerun and if a callback function is called. This can be one of the following values:  "rerun" (default): The user downloads the file and the app reruns. No callback function is called. "ignore": The user downloads the file and the app doesn't rerun. No callback function is called. A callable: The user downloads the file and app reruns. The callable is called before the rest of the app. None: This is same as on_click="rerun". This value exists for backwards compatibility and shouldn't be used. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | type | "primary", "secondary", or "tertiary" |  | An optional string that specifies the button type. This can be one of the following:  "primary": The button's background is the app's primary color for additional emphasis. "secondary" (default): The button's background coordinates with the app's background color for normal emphasis. "tertiary": The button is plain text without a border or background for subtlety. |
   | icon | str or None |  | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | disabled | bool | is | An optional boolean that disables the download button if set to True. The default is False. |
   | use_container_width | bool |  | Whether to expand the button's width to fill its parent container. If use_container_width is False (default), Streamlit sizes the button to fit its contents. If use_container_width is True, the width of the button matches its parent container. In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
   | width | "content", "stretch", or int |  | The width of the download button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |

* Returns: bool

    True if the button was clicked on the last run of the app,
False otherwise.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.link_button


* Function signature:

   st.link_button(label, url, *, help=None, type="secondary", icon=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this button is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | url | str |  | The url to be opened on user click |
   | help | str or None |  | A tooltip that gets displayed when the button is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | type | "primary", "secondary", or "tertiary" |  | An optional string that specifies the button type. This can be one of the following:  "primary": The button's background is the app's primary color for additional emphasis. "secondary" (default): The button's background coordinates with the app's background color for normal emphasis. "tertiary": The button is plain text without a border or background for subtlety. |
   | icon | str or None |  | An optional emoji or icon to display next to the button label. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | disabled | bool | is | An optional boolean that disables the link button if set to True. The default is False. |
   | use_container_width | bool |  | Whether to expand the button's width to fill its parent container. If use_container_width is False (default), Streamlit sizes the button to fit its contents. If use_container_width is True, the width of the button matches its parent container. In both cases, if the contents of the button are wider than the parent container, the contents will line wrap. |
   | width | "content", "stretch", or int |  | The width of the link button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.page_link

<Tip>

Check out our [tutorial](/develop/tutorials/multipage/st.page_link-nav) to learn about building custom, dynamic menus with `st.page_link`.

</Tip>

* Function signature:

   st.page_link(page, *, label=None, icon=None, help=None, disabled=False, use_container_width=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | page | str, Path, or StreamlitPage |  | The file path (relative to the main script) or a StreamlitPage indicating the page to switch to. Alternatively, this can be the URL to an external page (must start with "http://" or "https://"). |
   | label | str |  | The label for the page link. Labels are required for external pages. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | icon | str or None |  | An optional emoji or icon to display next to the button label. If icon is None (default), the icon is inferred from the StreamlitPage object or no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | help | str or None |  | A tooltip that gets displayed when the link is hovered over. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool | is | An optional boolean that disables the page link if set to True. The default is False. |
   | use_container_width | bool | is | Whether to expand the link's width to fill its parent container. The default is True for page links in the sidebar and False for those in the main app. |
   | width | "content", "stretch", or int |  | The width of the page-link button. This can be one of the following:  "content" (default): The width of the button matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the button matches the width of the parent container. An integer specifying the width in pixels: The button has a fixed width. If the specified width is greater than the width of the parent container, the width of the button matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox


* Function signature:

   st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this checkbox is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | bool |  | Preselect the checkbox when it first renders. This will be cast to bool internally. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this checkbox's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the checkbox if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the checkbox widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: bool

    Whether or not the checkbox is checked.



### Featured videos

Check out our video on how to use one of Streamlit's core functions, the checkbox! ☑

<YouTube videoId="Jte0Reue7z8"/>

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and [radio button](/develop/api-reference/widgets/st.radio)!

<YouTube videoId="EnXJBsCIl_A"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker


* Function signature:

   st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | str | black | The hex value of this widget when it first renders. If None, defaults to black. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this color_picker's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the color picker if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the color picker widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: str

    The selected color as a hex string.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.feedback


* Function signature:

   st.feedback(options="thumbs", *, key=None, default=None, disabled=False, on_change=None, args=None, kwargs=None, width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | options | "thumbs", "faces", or "stars" |  | The feedback options displayed to the user. options can be one of the following:  "thumbs" (default): Streamlit displays a thumb-up and thumb-down button group. "faces": Streamlit displays a row of five buttons with facial expressions depicting increasing satisfaction from left to right. "stars": Streamlit displays a row of star icons, allowing the user to select a rating from one to five stars. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | default | int or None | feedback | Default feedback value. This must be consistent with the feedback type in options:  0 or 1 if options="thumbs". Between 0 and 4, inclusive, if options="faces" or options="stars". |
   | disabled | bool | is | An optional boolean that disables the feedback widget if set to True. The default is False. |
   | on_change | callable |  | An optional callback invoked when this feedback widget's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | width | "content", "stretch", or int |  | The width of the feedback widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: int or None

    An integer indicating the user's selection, where 0 is the
lowest feedback. Higher values indicate more positive feedback.
If no option was selected, the widget returns None.

For options="thumbs", a return value of 0 indicates
thumbs-down, and 1 indicates thumbs-up.
For options="faces" and options="stars", return values
range from 0 (least satisfied) to 4 (most satisfied).



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect


* Function signature:

   st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, max_selections=None, placeholder=None, disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable |  | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default. |
   | default | Iterable of V, V, or None | values | List of default values. Can also be a single value. |
   | format_func | function |  | Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this widget's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | max_selections | int |  | The max selections that can be selected at a time. |
   | placeholder | str or  None |  | A string to display when no options are selected. If this is None (default), the widget displays placeholder text based on the widget's configuration:  "Choose options" is displayed when options are available and accept_new_options=False. "Choose or add options" is displayed when options are available and accept_new_options=True. "Add options" is displayed when no options are available and accept_new_options=True. "No options to select" is displayed when no options are available and accept_new_options=False. The widget is also disabled in this case. |
   | disabled | bool | is | An optional boolean that disables the multiselect widget if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | accept_new_options | bool |  | Whether the user can add selections that aren't included in options. If this is False (default), the user can only select from the items in options. If this is True, the user can enter new items that don't exist in options. When a user enters and selects a new item, it is included in the widget's returned list as a string. The new item is not added to the widget's drop-down menu. Streamlit will use a case-insensitive match from options before adding a new item, and a new item can't be added if a case-insensitive match is already selected. The max_selections argument is still enforced. |
   | width | "stretch" or int |  | The width of the multiselect widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: list

    A list of the selected options.
The list contains copies of the selected options, not the originals.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.pills


* Function signature:

   st.pills(label, options, *, selection_mode="single", default=None, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable of V | and | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default and can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | selection_mode | "single" or "multi" |  | The selection mode for the widget. If this is "single" (default), only one option can be selected. If this is "multi", multiple options can be selected. |
   | default | Iterable of V, V, or None |  | The value of the widget when it first renders. If the selection_mode is multi, this can be a list of values, a single value, or None. If the selection_mode is "single", this can be a single value or None. |
   | format_func | function |  | Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. The output can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this widget's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the widget if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the pills widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: list of V, V, or None

    If the selection_mode is multi, this is a list of selected
options or an empty list. If the selection_mode is
"single", this is a selected option or None.
This contains copies of the selected options, not the originals.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.radio


* Function signature:

   st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this radio group is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable |  | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default. Labels can include markdown as described in the label parameter and will be cast to str internally by default. |
   | index | int or None | 0 | The index of the preselected option on first render. If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option). |
   | format_func | function |  | Function to modify the display of radio options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the radio. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this radio's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the radio button if set to True. The default is False. |
   | horizontal | bool | false | An optional boolean, which orients the radio group horizontally. The default is false (vertical buttons). |
   | captions | iterable of str or None |  | A list of captions to show below each radio button. If None (default), no captions are shown. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the radio button widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: any

    The selected option or None if no option is selected.
This is a copy of the selected option, not the original.


<br/>

Widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Radio buttons can also be disabled with the `disabled` parameter, and oriented horizontally with the `horizontal` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
```

<Cloud height="300px" name="doc-radio1"/>

### Featured videos

Check out our video on how to use one of Streamlit's core functions, the radio button! 🔘

<YouTube videoId="CVHIMGVAzwA"/>

In the video below, we'll take it a step further and learn how to combine a [button](/develop/api-reference/widgets/st.button), [checkbox](/develop/api-reference/widgets/st.checkbox) and radio button!

<YouTube videoId="EnXJBsCIl_A"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.segmented_control


* Function signature:

   st.segmented_control(label, options, *, selection_mode="single", default=None, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable of V | and | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default and can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | selection_mode | "single" or "multi" |  | The selection mode for the widget. If this is "single" (default), only one option can be selected. If this is "multi", multiple options can be selected. |
   | default | Iterable of V, V, or None |  | The value of the widget when it first renders. If the selection_mode is multi, this can be a list of values, a single value, or None. If the selection_mode is "single", this can be a single value or None. |
   | format_func | function |  | Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. The output can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. Multiple widgets of the same type may not share the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this widget's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the widget if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the segmented control widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: list of V, V, or None

    If the selection_mode is multi, this is a list of selected
options or an empty list. If the selection_mode is
"single", this is a selected option or None.
This contains copies of the selected options, not the originals.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox


* Function signature:

   st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", accept_new_options=False, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this select widget is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable |  | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default. |
   | index | int or None | 0 | The index of the preselected option on first render. If None, will initialize empty and return None until the user selects an option. Defaults to 0 (the first option). |
   | format_func | function |  | Function to modify the display of the options. It receives the raw option as an argument and should output the label to be shown for that option. This has no impact on the return value of the command. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this selectbox's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | placeholder | str or None |  | A string to display when no options are selected. If this is None (default), the widget displays placeholder text based on the widget's configuration:  "Choose an option" is displayed when options are available and accept_new_options=False. "Choose or add an option" is displayed when options are available and accept_new_options=True. "Add an option" is displayed when no options are available and accept_new_options=True. "No options to select" is displayed when no options are available and accept_new_options=False. The widget is also disabled in this case. |
   | disabled | bool | is | An optional boolean that disables the selectbox if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | accept_new_options | bool |  | Whether the user can add a selection that isn't included in options. If this is False (default), the user can only select from the items in options. If this is True, the user can enter a new item that doesn't exist in options. When a user enters a new item, it is returned by the widget as a string. The new item is not added to the widget's drop-down menu. Streamlit will use a case-insensitive match from options before adding a new item. |
   | width | "stretch" or int |  | The width of the selectbox widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: any

    The selected option or None if no option is selected.
This is a copy of the selected option, not the original.


<br/>

Select widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Select widgets can also be disabled with the `disabled` parameter:

```python
import streamlit as st

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
```

<Cloud height="300px" name="doc-selectbox1"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.select_slider


* Function signature:

   st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this slider is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | options | Iterable |  | Labels for the select options in an Iterable. This can be a list, set, or anything supported by st.dataframe. If options is dataframe-like, the first column will be used. Each label will be cast to str internally by default. |
   | value | a supported type or a tuple/list of supported types or None | first | The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered. For example, if set to (1, 10) the slider will have a selectable range between 1 and 10. Defaults to first option. |
   | format_func | function |  | Function to modify the display of the labels from the options. argument. It receives the option as an argument and its output will be cast to str. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this select_slider's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the select slider if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the slider widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: any value or tuple of any value

    The current value of the slider widget. The return type will match
the data type of the value parameter.
This contains copies of the selected options, not the originals.



### Featured videos

Check out our video on how to use one of Streamlit's core functions, the select slider! 🎈
<YouTube videoId="MTaL_1UCb2g"/>

In the video below, we'll take it a step further and make a double-ended slider.
<YouTube videoId="sCvdt79asrE"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.toggle


* Function signature:

   st.toggle(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="content")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this toggle is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | bool |  | Preselect the toggle when it first renders. This will be cast to bool internally. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this toggle's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the toggle if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "content", "stretch", or int |  | The width of the toggle widget. This can be one of the following:  "content" (default): The width of the widget matches the width of its content, but doesn't exceed the width of the parent container. "stretch": The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: bool

    Whether or not the toggle is checked.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.number_input


* Function signature:

   st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | min_value | int, float, or None |  | The minimum permitted value. If this is None (default), there will be no minimum for float values and a minimum of - (1 + 1 for integer values. |
   | max_value | int, float, or None |  | The maximum permitted value. If this is None (default), there will be no maximum for float values and a maximum of (1 - 1 for integer values. |
   | value | int, float, "min" or None |  | The value of this widget when it first renders. If this is "min" (default), the initial value is min_value unless min_value is None. If min_value is None, the widget initializes with a value of 0.0 or 0. If value is None, the widget will initialize with no value and return None until the user provides input. |
   | step | int, float, or None | 1 | The stepping interval. Defaults to 1 if the value is an int, 0.01 otherwise. If the value is not specified, the format parameter will be used. |
   | format | str or None |  | A printf-style format string controlling how the interface should display numbers. The output must be purely numeric. This does not impact the return value of the widget. For more information about the formatting specification, see sprintf.js. For example, format="%0.1f" adjusts the displayed decimal precision to only show one digit after the decimal. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this number_input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | placeholder | str or None |  | An optional string displayed when the number input is empty. If None, no placeholder is displayed. |
   | disabled | bool | is | An optional boolean that disables the number input if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | icon | str, None |  | An optional emoji or icon to display within the input field to the left of the value. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | width | "stretch" or int |  | The width of the number input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: int or float or None

    The current value of the numeric input widget or None if the widget
is empty. The return type will match the data type of the value parameter.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.slider


* Function signature:

   st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this slider is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | min_value | a supported type or None |  | The minimum permitted value. If this is None (default), the minimum value depends on the type as follows:  integer: 0 float: 0.0 date or datetime: value - timedelta(days=14) time: time.min |
   | max_value | a supported type or None |  | The maximum permitted value. If this is None (default), the maximum value depends on the type as follows:  integer: 100 float: 1.0 date or datetime: value + timedelta(days=14) time: time.max |
   | value | a supported type or a tuple/list of supported types or None | s | The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered. For example, if set to (1, 10) the slider will have a selectable range between 1 and 10. This defaults to min_value. If the type is not otherwise specified in any of the numeric parameters, the widget will have an integer value. |
   | step | int, float, timedelta, or None | 1 | The stepping interval. Defaults to 1 if the value is an int, 0.01 if a float, timedelta(days=1) if a date/datetime, timedelta(minutes=15) if a time (or if max_value - min_value |
   | format | str or None |  | A printf-style format string controlling how the interface should display numbers. This does not impact the return value. For information about formatting integers and floats, see sprintf.js. For example, format="%0.1f" adjusts the displayed decimal precision to only show one digit after the decimal. For information about formatting datetimes, dates, and times, see momentJS. For example, format="ddd ha" adjusts the displayed datetime to show the day of the week and the hour ("Tue 8pm"). |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this slider's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the slider if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the slider widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: int/float/date/time/datetime or tuple of int/float/date/time/datetime

    The current value of the slider widget. The return type will match
the data type of the value parameter.



### Featured videos

Check out our video on how to use one of Streamlit's core functions, the slider!
<YouTube videoId="tzAdd-MuWPw"/>

In the video below, we'll take it a step further and make a double-ended slider.
<YouTube videoId="sCvdt79asrE"/>

---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.date_input


* Function signature:

   st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this date input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | "today", datetime.date, datetime.datetime, str, list/tuple of these, or None |  | The value of this widget when it first renders. This can be one of the following:  "today" (default): The widget initializes with the current date. A datetime.date or datetime.datetime object: The widget initializes with the given date, ignoring any time if included. An ISO-formatted date ("YYYY-MM-DD") or datetime ("YYYY-MM-DD hh:mm:ss") string: The widget initializes with the given date, ignoring any time if included. A list or tuple with up to two of the above: The widget will initialize with the given date interval and return a tuple of the selected interval. You can pass an empty list to initialize the widget with an empty interval or a list with one value to initialize only the beginning date of the iterval. None: The widget initializes with no date and returns None until the user selects a date. |
   | min_value | "today", datetime.date, datetime.datetime, str, or None |  | The minimum selectable date. This can be any of the date types accepted by value, except list or tuple. If this is None (default), the minimum selectable date is ten years before the initial value. If the initial value is an interval, the minimum selectable date is ten years before the start date of the interval. If no initial value is set, the minimum selectable date is ten years before today. |
   | max_value | "today", datetime.date, datetime.datetime, str, or None |  | The maximum selectable date. This can be any of the date types accepted by value, except list or tuple. If this is None (default), the maximum selectable date is ten years after the initial value. If the initial value is an interval, the maximum selectable date is ten years after the end date of the interval. If no initial value is set, the maximum selectable date is ten years after today. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this date_input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | format | str |  | A format string controlling how the interface should display dates. Supports "YYYY/MM/DD" (default), "DD/MM/YYYY", or "MM/DD/YYYY". You may also use a period (.) or hyphen (-) as separators. |
   | disabled | bool | is | An optional boolean that disables the date input if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the date input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: datetime.date or a tuple with 0-2 dates or None

    The current value of the date input widget or None if no date has been
selected.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.time_input


* Function signature:

   st.time_input(label, value="now", key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", step=0:15:00, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this time input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | "now", datetime.time, datetime.datetime, str, or None |  | The value of this widget when it first renders. This can be one of the following:  "now" (default): The widget initializes with the current time. A datetime.time or datetime.datetime object: The widget initializes with the given time, ignoring any date if included. An ISO-formatted time ("hh:mm", "hh:mm:ss", or "hh:mm:ss.sss") or datetime ("YYYY-MM-DD hh:mm:ss") string: The widget initializes with the given time, ignoring any date if included. None: The widget initializes with no time and returns None until the user selects a time. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this time_input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | disabled | bool | is | An optional boolean that disables the time input if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | step | int or timedelta | 900 | The stepping interval in seconds. Defaults to 900, i.e. 15 minutes. You can also pass a datetime.timedelta object. |
   | width | "stretch" or int |  | The width of the time input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: datetime.time or None

    The current value of the time input widget or None if no time has been
selected.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.text_area


* Function signature:

   st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | object or None | empty | The text value of this widget when it first renders. This will be cast to str internally. If None, will initialize empty and return None until the user provides input. Defaults to empty string. |
   | height | "content", "stretch", int, or None |  | The height of the text area widget. This can be one of the following:  None (default): The height of the widget fits three lines. "content": The height of the widget matches the height of its content. "stretch": The height of the widget matches the height of its content or the height of the parent container, whichever is larger. If the widget is not in a parent container, the height of the widget matches the height of its content. An integer specifying the height in pixels: The widget has a fixed height. If the content is larger than the specified height, scrolling is enabled.  The widget's height can't be smaller than the height of two lines. When label_visibility="collapsed", the minimum height is 68 pixels. Otherwise, the minimum height is 98 pixels. |
   | max_chars | int or None |  | Maximum number of characters allowed in text area. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | on_change | callable |  | An optional callback invoked when this text_area's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | placeholder | str or None |  | An optional string displayed when the text area is empty. If None, no text is displayed. |
   | disabled | bool | is | An optional boolean that disables the text area if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | width | "stretch" or int |  | The width of the text area widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: str or None

    The current value of the text area widget or None if no value has been
provided by the user.



---

Source: https://docs.streamlit.io/develop/api-reference/widgets/st.text_input


* Function signature:

   st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | A short label explaining to the user what this input is for. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. For accessibility reasons, you should never set an empty label, but you can hide it with label_visibility if needed. In the future, we may disallow empty labels by raising an exception. |
   | value | object or None | empty | The text value of this widget when it first renders. This will be cast to str internally. If None, will initialize empty and return None until the user provides input. Defaults to empty string. |
   | max_chars | int or None |  | Max number of characters allowed in text input. |
   | key | str or int |  | An optional string or integer to use as the unique key for the widget. If this is omitted, a key will be generated for the widget based on its content. No two widgets may have the same key. |
   | type | "default" or "password" | s | The type of the text input. This can be either "default" (for a regular text input), or "password" (for a text input that masks the user's typed value). Defaults to "default". |
   | help | str or None |  | A tooltip that gets displayed next to the widget label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | autocomplete | str |  | An optional value that will be passed to the  element's autocomplete property. If unspecified, this value will be set to "new-password" for "password" inputs, and the empty string for "default" inputs. For more details, see https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete |
   | on_change | callable |  | An optional callback invoked when this text input's value changes. |
   | args | list or tuple |  | An optional list or tuple of args to pass to the callback. |
   | kwargs | dict |  | An optional dict of kwargs to pass to the callback. |
   | placeholder | str or None |  | An optional string displayed when the text input is empty. If None, no text is displayed. |
   | disabled | bool | is | An optional boolean that disables the text input if set to True. The default is False. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. |
   | icon | str, None |  | An optional emoji or icon to display within the input field to the left of the value. If icon is None (default), no icon is displayed. If icon is a string, the following options are valid:  A single-character emoji. For example, you can set icon="🚨" or icon="🔥". Emoji short codes are not supported.  An icon from the Material Symbols library (rounded style) in the format ":material/icon_name:" where "icon_name" is the name of the icon in snake case. For example, icon=":material/thumb_up:" will display the Thumb Up icon. Find additional icons in the Material Symbols  font library. |
   | width | "stretch" or int |  | The width of the text input widget. This can be one of the following:  "stretch" (default): The width of the widget matches the width of the parent container. An integer specifying the width in pixels: The widget has a fixed width. If the specified width is greater than the width of the parent container, the width of the widget matches the width of the parent container. |

* Returns: str or None

    The current value of the text input widget or None if no value has been
provided by the user.


<br/>

Text input widgets can customize how to hide their labels with the `label_visibility` parameter. If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to `label=""`). If "collapsed", both the label and the space are removed. Default is "visible". Text input widgets can also be disabled with the `disabled` parameter, and can display an optional placeholder text when the text input is empty using the `placeholder` parameter:

```python
import streamlit as st


---

**Navigation:** [← Previous](./04-column-configuration.md) | [Index](./index.md) | [Next →](./06-store-the-initial-value-of-widgets-in-session-stat.md)
