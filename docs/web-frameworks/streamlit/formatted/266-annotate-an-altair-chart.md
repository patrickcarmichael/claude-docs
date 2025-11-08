---
title: "Annotate an Altair chart"
source: https://docs.streamlit.io/develop/tutorials/elements/annotate-an-altair-chart
section: 266
---

# Annotate an Altair chart

Source: https://docs.streamlit.io/develop/tutorials/elements/annotate-an-altair-chart


Altair allows you to annotate your charts with text, images, and emojis. You can do this by overlaying two charts to create a [layered chart](https://altair-viz.github.io/user_guide/compound_charts.html#layered-charts).

## Applied concepts

- Use layered charts in Altair to create annotations.

## Prerequisites

- This tutorial requires the following Python libraries:

  ```txt
  streamlit
  altair&gt;=4.0.0
  vega_datasets
  ```python
- This tutorial assumes you have a clean working directory called `your-repository`.
- You should have a basic understanding of the Vega-Altair charting library.

## Summary

In this example, you will create a time-series chart to track the evolution of stock prices. The chart will have two layers: a data layer and an
annotation layer. Each layer is an `altair.Chart` object. You will combine the two charts with the `+` opterator to create a layered chart.

Within the data layer, you'll add a multi-line tooltip to show information about datapoints. To learn more about multi-line tooltips, see this [example](https://altair-viz.github.io/gallery/multiline_tooltip.html) in Vega-Altair's documentation. You'll add another tooltip to the annotation layer.

Here's a look at what you'll build:

<Collapse title="Complete code">{false}&gt;

```python
import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data


@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source


stock_data = get_data()

hover = alt.selection_single(
    fields=["date"],
    nearest=True,
    on="mouseover",
    empty="none",
)

lines = (
    alt.Chart(stock_data, title="Evolution of stock prices")
    .mark_line()
    .encode(
        x="date",
        y="price",
        color="symbol",
    )
)

points = lines.transform_filter(hover).mark_circle(size=65)

tooltips = (
    alt.Chart(stock_data)
    .mark_rule()
    .encode(
        x="yearmonthdate(date)",
        y="price",
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=[
            alt.Tooltip("date", title="Date"),
            alt.Tooltip("price", title="Price (USD)"),
        ],
    )
    .add_selection(hover)
)

data_layer = lines + points + tooltips

ANNOTATIONS = [
    ("Sep 01, 2007", 450, "🙂", "Something's going well for GOOG  AAPL."),
    ("Nov 01, 2008", 220, "🙂", "The market is recovering."),
    ("Dec 01, 2007", 750, "😱", "Something's going wrong for GOOG  AAPL."),
    ("Dec 01, 2009", 680, "😱", "A hiccup for GOOG."),
]
annotations_df = pd.DataFrame(
    ANNOTATIONS, columns=["date", "price", "marker", "description"]
)
annotations_df.date = pd.to_datetime(annotations_df.date)

annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=20, dx=-10, dy=0, align="left")
    .encode(x="date:T", y=alt.Y("price:Q"), text="marker", tooltip="description")
)

combined_chart = data_layer + annotation_layer
st.altair_chart(combined_chart, use_container_width=True)
```python
</Collapse>

---

[← Previous](265-work-with-streamlit-elements.md) | [Index](index.md) | [Next →](index.md)
