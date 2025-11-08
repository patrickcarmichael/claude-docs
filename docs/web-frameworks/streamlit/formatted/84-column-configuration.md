---
title: "Column configuration"
source: https://docs.streamlit.io/develop/api-reference/data/st.column_config
section: 84
---

# Column configuration

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config


When working with data in Streamlit, the `st.column_config` class is a powerful tool for configuring data display and interaction. Specifically designed for the `column_config` parameter in [`st.dataframe`](/develop/api-reference/data/st.dataframe) and [`st.data_editor`](/develop/api-reference/data/st.data_editor), it provides a suite of methods to tailor your columns to various data types - from simple text and numbers to lists, URLs, images, and more.

Whether it's translating temporal data into user-friendly formats or utilizing charts and progress bars for clearer data visualization, column configuration not only provides the user with an enriched data viewing experience but also ensures that you're equipped with the tools to present and interact with your data, just the way you want it.

<TileContainer>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.column">
<Image>alt="screenshot" src="/images/api/column_config.column.jpg" /&gt;

<h4>Column</h4>

Configure a generic column.

```python
Column("Streamlit Widgets", width="medium", help="Streamlit **widget** commands 🎈")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.textcolumn">
<Image>alt="screenshot" src="/images/api/column_config.textcolumn.jpg" /&gt;

<h4>Text column</h4>

Configure a text column.

```python
TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.numbercolumn">
<Image>alt="screenshot" src="/images/api/column_config.numbercolumn.jpg" /&gt;

<h4>Number column</h4>

Configure a number column.

```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn">
<Image>alt="screenshot" src="/images/api/column_config.checkboxcolumn.jpg" /&gt;

<h4>Checkbox column</h4>

Configure a checkbox column.

```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn">
<Image>alt="screenshot" src="/images/api/column_config.selectboxcolumn.jpg" /&gt;

<h4>Selectbox column</h4>

Configure a selectbox column.

```python
SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn">
<Image>alt="screenshot" src="/images/api/column_config.multiselectcolumn.jpg" /&gt;

<h4>Multiselect column</h4>

Configure a multiselect column.

```python
MultiselectColumn("App Category", options=["LLM", "Visualization"])
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn">
<Image>alt="screenshot" src="/images/api/column_config.datetimecolumn.jpg" /&gt;

<h4>Datetime column</h4>

Configure a datetime column.

```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datecolumn">
<Image>alt="screenshot" src="/images/api/column_config.datecolumn.jpg" /&gt;

<h4>Date column</h4>

Configure a date column.

```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.timecolumn">
<Image>alt="screenshot" src="/images/api/column_config.timecolumn.jpg" /&gt;

<h4>Time column</h4>

Configure a time column.

```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn">
<Image>alt="screenshot" src="/images/api/column_config.jsoncolumn.jpg" /&gt;

<h4>JSON column</h4>

Configure a JSON column.

```python
JSONColumn("Properties", width="medium")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.listcolumn">
<Image>alt="screenshot" src="/images/api/column_config.listcolumn.jpg" /&gt;

<h4>List column</h4>

Configure a list column.

```python
ListColumn("Sales (last 6 months)", width="medium")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linkcolumn">
<Image>alt="screenshot" src="/images/api/column_config.linkcolumn.jpg" /&gt;

<h4>Link column</h4>

Configure a link column.

```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.imagecolumn">
<Image>alt="screenshot" src="/images/api/column_config.imagecolumn.jpg" /&gt;

<h4>Image column</h4>

Configure an image column.

```python
ImageColumn("Preview Image", help="The preview screenshots")
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.areachartcolumn.jpg" /&gt;

<h4>Area chart column</h4>

Configure an area chart column.

```python
AreaChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.linechartcolumn.jpg" /&gt;

<h4>Line chart column</h4>

Configure a line chart column.

```python
LineChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.barchartcolumn.jpg" /&gt;

<h4>Bar chart column</h4>

Configure a bar chart column.

```python
BarChartColumn("Marketing spend" y_min=0, y_max=100)
```python
</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.progresscolumn">
<Image>alt="screenshot" src="/images/api/column_config.progresscolumn.jpg" /&gt;

<h4>Progress column</h4>

Configure a progress column.

```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")
```python
</Image></RefCard>
</TileContainer>

---

[← Previous](81-data-elements.md) | [Index](index.md) | [Next →](index.md)
