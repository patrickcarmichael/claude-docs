**Navigation:** [← Previous](./03-customize-colors-and-borders-in-your-streamlit-app.md) | [Index](./index.md) | [Next →](./05-bottom-panel-is-a-bar-chart-of-weather-type.md)

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
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.textcolumn">
<Image>alt="screenshot" src="/images/api/column_config.textcolumn.jpg" /&gt;

<h4>Text column</h4>

Configure a text column.

```python
TextColumn("Widgets", max_chars=50, validate="^st\.[a-z_]+$")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.numbercolumn">
<Image>alt="screenshot" src="/images/api/column_config.numbercolumn.jpg" /&gt;

<h4>Number column</h4>

Configure a number column.

```python
NumberColumn("Price (in USD)", min_value=0, format="$%d")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn">
<Image>alt="screenshot" src="/images/api/column_config.checkboxcolumn.jpg" /&gt;

<h4>Checkbox column</h4>

Configure a checkbox column.

```python
CheckboxColumn("Your favorite?", help="Select your **favorite** widgets")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn">
<Image>alt="screenshot" src="/images/api/column_config.selectboxcolumn.jpg" /&gt;

<h4>Selectbox column</h4>

Configure a selectbox column.

```python
SelectboxColumn("App Category", options=["🤖 LLM", "📈 Data Viz"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn">
<Image>alt="screenshot" src="/images/api/column_config.multiselectcolumn.jpg" /&gt;

<h4>Multiselect column</h4>

Configure a multiselect column.

```python
MultiselectColumn("App Category", options=["LLM", "Visualization"])
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn">
<Image>alt="screenshot" src="/images/api/column_config.datetimecolumn.jpg" /&gt;

<h4>Datetime column</h4>

Configure a datetime column.

```python
DatetimeColumn("Appointment", min_value=datetime(2023, 6, 1), format="D MMM YYYY, h:mm a")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.datecolumn">
<Image>alt="screenshot" src="/images/api/column_config.datecolumn.jpg" /&gt;

<h4>Date column</h4>

Configure a date column.

```python
DateColumn("Birthday", max_value=date(2005, 1, 1), format="DD.MM.YYYY")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.timecolumn">
<Image>alt="screenshot" src="/images/api/column_config.timecolumn.jpg" /&gt;

<h4>Time column</h4>

Configure a time column.

```python
TimeColumn("Appointment", min_value=time(8, 0, 0), format="hh:mm a")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn">
<Image>alt="screenshot" src="/images/api/column_config.jsoncolumn.jpg" /&gt;

<h4>JSON column</h4>

Configure a JSON column.

```python
JSONColumn("Properties", width="medium")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.listcolumn">
<Image>alt="screenshot" src="/images/api/column_config.listcolumn.jpg" /&gt;

<h4>List column</h4>

Configure a list column.

```python
ListColumn("Sales (last 6 months)", width="medium")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linkcolumn">
<Image>alt="screenshot" src="/images/api/column_config.linkcolumn.jpg" /&gt;

<h4>Link column</h4>

Configure a link column.

```python
LinkColumn("Trending apps", max_chars=100, validate="^https://.*$")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.imagecolumn">
<Image>alt="screenshot" src="/images/api/column_config.imagecolumn.jpg" /&gt;

<h4>Image column</h4>

Configure an image column.

```python
ImageColumn("Preview Image", help="The preview screenshots")
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.areachartcolumn.jpg" /&gt;

<h4>Area chart column</h4>

Configure an area chart column.

```python
AreaChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.linechartcolumn.jpg" /&gt;

<h4>Line chart column</h4>

Configure a line chart column.

```python
LineChartColumn("Sales (last 6 months)" y_min=0, y_max=100)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn">
<Image>alt="screenshot" src="/images/api/column_config.barchartcolumn.jpg" /&gt;

<h4>Bar chart column</h4>

Configure a bar chart column.

```python
BarChartColumn("Marketing spend" y_min=0, y_max=100)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/data/st.column_config/st.column_config.progresscolumn">
<Image>alt="screenshot" src="/images/api/column_config.progresscolumn.jpg" /&gt;

<h4>Progress column</h4>

Configure a progress column.

```python
ProgressColumn("Sales volume", min_value=0, max_value=1000, format="$%f")
```

</Image></RefCard>
</TileContainer>

---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.column


* Function signature:

   st.column_config.Column(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.textcolumn


* Function signature:

   st.column_config.TextColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, max_chars=None, validate=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | str or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | max_chars | int or None |  | The maximum number of characters that can be entered. If this is None (default), there will be no maximum. |
   | validate | str or None |  | A JS-flavored regular expression (e.g. "^[a-z]+$") that edited values are validated against. If the user input is invalid, it will not be submitted. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.numbercolumn


* Function signature:

   st.column_config.NumberColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, format=None, min_value=None, max_value=None, step=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | int, float, or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | format | str, "plain", "localized", "percent", "dollar", "euro", "yen", "accounting", "compact", "scientific", "engineering", or None | locale | A format string controlling how numbers are displayed. This can be one of the following values:  None (default): Streamlit infers the formatting from the data. "plain": Show the full number without any formatting (e.g. "1234.567"). "localized": Show the number in the default locale format (e.g. "1,234.567"). "percent": Show the number as a percentage (e.g. "123456.70%"). "dollar": Show the number as a dollar amount (e.g. "$1,234.57"). "euro": Show the number as a euro amount (e.g. "€1,234.57"). "yen": Show the number as a yen amount (e.g. "¥1,235"). "accounting": Show the number in an accounting format (e.g. "1,234.00"). "bytes": Show the number in a byte format (e.g. "1.2KB"). "compact": Show the number in a compact format (e.g. "1.2K"). "scientific": Show the number in scientific notation (e.g. "1.235E3"). "engineering": Show the number in engineering notation (e.g. "1.235E3"). printf-style format string: Format the number with a printf specifier, like "%d" to show a signed integer (e.g. "1234") or "%X" to show an unsigned hexadecimal integer (e.g. "4D2"). You can also add prefixes and suffixes. To show British pounds, use "£ %.2f" (e.g. "£ 1234.57"). For more information, see sprint-js.  Formatting from column_config always takes precedence over formatting from pandas.Styler. The formatting does not impact the return value when used in st.data_editor. |
   | min_value | int, float, or None |  | The minimum value that can be entered. If this is None (default), there will be no minimum. |
   | max_value | int, float, or None |  | The maximum value that can be entered. If this is None (default), there will be no maximum. |
   | step | int, float, or None |  | The precision of numbers that can be entered. If this None (default), integer columns will have a step of 1 and float columns will have unrestricted precision. In this case, some floats may display like integers. Setting step for float columns will ensure a consistent number of digits after the decimal are displayed. If format is a predefined format like "dollar", step overrides the display precision. If format is a printf-style format string, step will not change the display precision. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.checkboxcolumn


* Function signature:

   st.column_config.CheckboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | bool or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.selectboxcolumn


* Function signature:

   st.column_config.SelectboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, options=None, format_func=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | str, int, float, bool, or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | options | Iterable[str, int, float, bool] or None |  | The options that can be selected during editing. If this is None (default), the options will be inferred from the underlying dataframe column if its dtype is "category". For more information, see Pandas docs). |
   | format_func | function or None |  | Function to modify the display of the options. It receives the raw option defined in options as an argument and should output the label to be shown for that option. If this is None (default), the raw option is used as the label. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.multiselectcolumn


* Function signature:

   st.column_config.MultiselectColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, options=None, accept_new_options=None, color=None, format_func=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If None (default), the column name is used. |
   | width | "small", "medium", "large", or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None | False | Whether editing should be disabled for this column. Defaults to False. |
   | required | bool or None | False | Whether edited cells in the column need to have a value. If True, an edited cell can only be submitted if it has a value other than None. Defaults to False. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | Iterable of str or None | value | Specifies the default value in this column when a new row is added by the user. |
   | options | Iterable of str or None |  | The options that can be selected during editing. |
   | accept_new_options | bool or None |  | Whether the user can add selections that aren't included in options. If this is False (default), the user can only select from the items in options. If this is True, the user can enter new items that don't exist in options. When a user enters and selects a new item, it is included in the returned cell list value as a string. The new item is not added to the options drop-down menu. |
   | color | str, Iterable of str, or None |  | The color to use for different options. This can be:  None (default): The options are displayed without color.  "auto": The options are colored based on the configured categorical chart colors.  A single color value that is used for all options. This can be one of the following strings:   "primary" to use the primary theme color. A CSS named color name like "darkBlue" or "maroon". A hex color code like "#483d8b" or "#6A5ACD80". An RGB or RGBA color code like "rgb(255,0,0)" or "RGB(70, 130, 180, .7)". An HSL or HSLA color code like "hsl(248, 53%, 58%)" or "HSL(147, 50%, 47%, .3)".    An iterable of color values that are mapped to the options. The colors are applied in sequence, cycling through the iterable if there are more options than colors. |
   | format_func | function or None |  | Function to modify the display of the options. It receives the raw option defined in options as an argument and should output the label to be shown for that option. When used in st.data_editor, this has no impact on the returned value. If this is None (default), the raw option is used as the label. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.datetimecolumn


* Function signature:

   st.column_config.DatetimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, format=None, min_value=None, max_value=None, step=None, timezone=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | datetime.datetime or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | format | str, "localized", "distance", "calendar", "iso8601", or None | locale | A format string controlling how datetimes are displayed. This can be one of the following values:  None (default): Show the datetime in "YYYY-MM-DD HH:mm:ss" format (e.g. "2025-03-04 20:00:00"). "localized": Show the datetime in the default locale format (e.g. "Mar 4, 2025, 12:00:00 PM" in the America/Los_Angeles timezone). "distance": Show the datetime in a relative format (e.g. "a few seconds ago"). "calendar": Show the datetime in a calendar format (e.g. "Today at 8:00 PM"). "iso8601": Show the datetime in ISO 8601 format (e.g. "2025-03-04T20:00:00.000Z"). A momentJS format string: Format the datetime with a string, like "ddd ha" to show "Tue 8pm". For available formats, see momentJS.  Formatting from column_config always takes precedence over formatting from pandas.Styler. The formatting does not impact the return value when used in st.data_editor. |
   | min_value | datetime.datetime or None |  | The minimum datetime that can be entered. If this is None (default), there will be no minimum. |
   | max_value | datetime.datetime or None |  | The maximum datetime that can be entered. If this is None (default), there will be no maximum. |
   | step | int, float, datetime.timedelta, or None |  | The stepping interval in seconds. If this is None (default), the step will be 1 second. |
   | timezone | str or None |  | The timezone of this column. If this is None (default), the timezone is inferred from the underlying data. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.datecolumn


* Function signature:

   st.column_config.DateColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, format=None, min_value=None, max_value=None, step=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | datetime.date or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | format | str, "localized", "distance", "iso8601", or None | locale | A format string controlling how dates are displayed. This can be one of the following values:  None (default): Show the date in "YYYY-MM-DD" format (e.g. "2025-03-04"). "localized": Show the date in the default locale format (e.g. "Mar 4, 2025" in the America/Los_Angeles timezone). "distance": Show the date in a relative format (e.g. "a few seconds ago"). "iso8601": Show the date in ISO 8601 format (e.g. "2025-03-04"). A momentJS format string: Format the date with a string, like "ddd, MMM Do" to show "Tue, Mar 4th". For available formats, see momentJS.  Formatting from column_config always takes precedence over formatting from pandas.Styler. The formatting does not impact the return value when used in st.data_editor. |
   | min_value | datetime.date or None |  | The minimum date that can be entered. If this is None (default), there will be no minimum. |
   | max_value | datetime.date or None |  | The maximum date that can be entered. If this is None (default), there will be no maximum. |
   | step | int or None |  | The stepping interval in days. If this is None (default), the step will be 1 day. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.timecolumn


* Function signature:

   st.column_config.TimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, format=None, min_value=None, max_value=None, step=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | datetime.time or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | format | str, "localized", "iso8601", or None | locale | A format string controlling how times are displayed. This can be one of the following values:  None (default): Show the time in "HH:mm:ss" format (e.g. "20:00:00"). "localized": Show the time in the default locale format (e.g. "12:00:00 PM" in the America/Los_Angeles timezone). "iso8601": Show the time in ISO 8601 format (e.g. "20:00:00.000Z"). A momentJS format string: Format the time with a string, like "ha" to show "8pm". For available formats, see momentJS.  Formatting from column_config always takes precedence over formatting from pandas.Styler. The formatting does not impact the return value when used in st.data_editor. |
   | min_value | datetime.time or None |  | The minimum time that can be entered. If this is None (default), there will be no minimum. |
   | max_value | datetime.time or None |  | The maximum time that can be entered. If this is None (default), there will be no maximum. |
   | step | int, float, datetime.timedelta, or None |  | The stepping interval in seconds. If this is None (default), the step will be 1 second. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.jsoncolumn


* Function signature:

   st.column_config.JsonColumn(label=None, *, width=None, help=None, pinned=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.listcolumn


* Function signature:

   st.column_config.ListColumn(label=None, *, width=None, help=None, pinned=None, disabled=None, required=None, default=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | default | Iterable of str or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.linkcolumn


* Function signature:

   st.column_config.LinkColumn(label=None, *, width=None, help=None, disabled=None, required=None, pinned=None, default=None, max_chars=None, validate=None, display_text=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | disabled | bool or None |  | Whether editing should be disabled for this column. If this is None (default), Streamlit will enable editing wherever possible. If a column has mixed types, it may become uneditable regardless of disabled. |
   | required | bool or None |  | Whether edited cells in the column need to have a value. If this is False (default), the user can submit empty values for this column. If this is True, an edited cell in this column can only be submitted if its value is not None, and a new row will only be submitted after the user fills in this column. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | default | str or None | value | Specifies the default value in this column when a new row is added by the user. This defaults to None. |
   | max_chars | int or None |  | The maximum number of characters that can be entered. If this is None (default), there will be no maximum. |
   | validate | str or None |  | A JS-flavored regular expression (e.g. "^https://.+$") that edited values are validated against. If the user input is invalid, it will not be submitted. |
   | display_text | str or None |  | The text that is displayed in the cell. This can be one of the following:  None (default) to display the URL itself. A string that is displayed in every cell, e.g. "Open link". A Material icon that is displayed in every cell, e.g. ":material/open_in_new:". A JS-flavored regular expression (detected by usage of parentheses) to extract a part of the URL via a capture group. For example, use "https://(.*?)\.example\.com" to extract the display text "foo" from the URL "https://foo.example.com".   For more complex cases, you may use Pandas Styler's format function on the underlying dataframe. Note that this makes the app slow, doesn't work with editable columns, and might be removed in the future. Text formatting from column_config always takes precedence over text formatting from pandas.Styler. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.imagecolumn


* Function signature:

   st.column_config.ImageColumn(label=None, *, width=None, help=None, pinned=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.areachartcolumn


* Function signature:

   st.column_config.AreaChartColumn(label=None, *, width=None, help=None, pinned=None, y_min=None, y_max=None, color=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | y_min | int, float, or None |  | The minimum value on the y-axis for all cells in the column. If this is None (default), every cell will use the minimum of its data. |
   | y_max | int, float, or None |  | The maximum value on the y-axis for all cells in the column. If this is None (default), every cell will use the maximum of its data. |
   | color | "auto", "auto-inverse", str, or None |  | The color to use for the chart. This can be one of the following:  None (default): The primary color is used. "auto": If the data is increasing, the chart is green; if the data is decreasing, the chart is red. "auto-inverse": If the data is increasing, the chart is red; if the data is decreasing, the chart is green. A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like "#483d8b".  The basic color palette can be configured in the theme settings. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.linechartcolumn


* Function signature:

   st.column_config.LineChartColumn(label=None, *, width=None, help=None, pinned=None, y_min=None, y_max=None, color=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | y_min | int, float, or None |  | The minimum value on the y-axis for all cells in the column. If this is None (default), every cell will use the minimum of its data. |
   | y_max | int, float, or None |  | The maximum value on the y-axis for all cells in the column. If this is None (default), every cell will use the maximum of its data. |
   | color | "auto", "auto-inverse", str, or None |  | The color to use for the chart. This can be one of the following:  None (default): The primary color is used. "auto": If the data is increasing, the chart is green; if the data is decreasing, the chart is red. "auto-inverse": If the data is increasing, the chart is red; if the data is decreasing, the chart is green. A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like "#483d8b". |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.barchartcolumn


* Function signature:

   st.column_config.BarChartColumn(label=None, *, width=None, help=None, pinned=None, y_min=None, y_max=None, color=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | y_min | int, float, or None |  | The minimum value on the y-axis for all cells in the column. If this is None (default), every cell will use the minimum of its data. |
   | y_max | int, float, or None |  | The maximum value on the y-axis for all cells in the column. If this is None (default), every cell will use the maximum of its data. |
   | color | "auto", "auto-inverse", str, or None |  | The color to use for the chart. This can be one of the following:  None (default): The primary color is used. "auto": If the data is increasing, the chart is green; if the data is decreasing, the chart is red. "auto-inverse": If the data is increasing, the chart is red; if the data is decreasing, the chart is green. A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like "#483d8b". |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.progresscolumn


* Function signature:

   st.column_config.ProgressColumn(label=None, *, width=None, help=None, pinned=None, format=None, min_value=None, max_value=None, step=None, color=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str or None |  | The label shown at the top of the column. If this is None (default), the column name is used. |
   | width | "small", "medium", "large", int, or None |  | The display width of the column. If this is None (default), the column will be sized to fit the cell contents. Otherwise, this can be one of the following:  "small": 75px wide "medium": 200px wide "large": 400px wide An integer specifying the width in pixels  If the total width of all columns is less than the width of the dataframe, the remaining space will be distributed evenly among all columns. |
   | help | str or None |  | A tooltip that gets displayed when hovering over the column label. If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | format | str, "plain", "localized", "percent", "dollar", "euro", "yen", "accounting", "compact", "scientific", "engineering", or None | locale | A format string controlling how the numbers are displayed. This can be one of the following values:  None (default): Streamlit infers the formatting from the data. "plain": Show the full number without any formatting (e.g. "1234.567"). "localized": Show the number in the default locale format (e.g. "1,234.567"). "percent": Show the number as a percentage (e.g. "123456.70%"). "dollar": Show the number as a dollar amount (e.g. "$1,234.57"). "euro": Show the number as a euro amount (e.g. "€1,234.57"). "yen": Show the number as a yen amount (e.g. "¥1,235"). "accounting": Show the number in an accounting format (e.g. "1,234.00"). "bytes": Show the number in a byte format (e.g. "1.2KB"). "compact": Show the number in a compact format (e.g. "1.2K"). "scientific": Show the number in scientific notation (e.g. "1.235E3"). "engineering": Show the number in engineering notation (e.g. "1.235E3"). printf-style format string: Format the number with a printf specifier, like "%d" to show a signed integer (e.g. "1234") or "%X" to show an unsigned hexadecimal integer (e.g. "4D2"). You can also add prefixes and suffixes. To show British pounds, use "£ %.2f" (e.g. "£ 1234.57"). For more information, see sprint-js.  Number formatting from column_config always takes precedence over number formatting from pandas.Styler. The number formatting does not impact the return value when used in st.data_editor. |
   | pinned | bool or None |  | Whether the column is pinned. A pinned column will stay visible on the left side no matter where the user scrolls. If this is None (default), Streamlit will decide: index columns are pinned, and data columns are not pinned. |
   | min_value | int, float, or None |  | The minimum value of the progress bar. If this is None (default), the minimum will be 0. |
   | max_value | int, float, or None |  | The maximum value of the progress bar. If this is None (default), the maximum will be 100 for integer values and 1.0 for float values. |
   | step | int, float, or None |  | The precision of numbers. If this is None (default), integer columns will have a step of 1 and float columns will have a step of 0.01. Setting step for float columns will ensure a consistent number of digits after the decimal are displayed. |
   | color | "auto", "auto-inverse", str, or None |  | The color to use for the chart. This can be one of the following:  None (default): The primary color is used. "auto": If the value is more than half, the bar is green; if the value is less than half, the bar is red. "auto-inverse": If the value is more than half, the bar is red; if the value is less than half, the bar is green. A single color value that is applied to all charts in the column. In addition to the basic color palette (red, orange, yellow, green, blue, violet, gray/grey, and primary), this supports hex codes like "#483d8b". |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.table

<Tip>

Static tables with `st.table` are the most basic way to display dataframes. For the majority of cases, we recommend using [`st.dataframe`](/develop/api-reference/data/st.dataframe) to display interactive dataframes, and [`st.data_editor`](/develop/api-reference/data/st.data_editor) to let users edit dataframes.

</Tip>

* Function signature:

   st.table(data=None, *, border=True)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | The table data. All cells including the index and column headers can optionally contain GitHub-flavored Markdown. Syntax information can be found at: https://github.github.com/gfm. See the body parameter of st.markdown for additional, supported Markdown directives. |
   | border | bool or "horizontal" |  | Whether to show borders around the table and between cells. This can be one of the following:  True (default): Show borders around the table and between cells. False: Don't show any borders. "horizontal": Show only horizontal borders between rows. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.metric


* Function signature:

   st.metric(label, value, delta=None, delta_color="normal", *, help=None, label_visibility="visible", border=False, width="stretch", height="content", chart_data=None, chart_type="line")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | label | str |  | The header or title for the metric. The label can optionally contain GitHub-flavored Markdown of the following types: Bold, Italics, Strikethroughs, Inline Code, Links, and Images. Images display like icons, with a max height equal to the font height. Unsupported Markdown elements are unwrapped so only their children (text contents) render. Display unsupported elements as literal characters by backslash-escaping them. E.g., "1\. Not an ordered list". See the body parameter of st.markdown for additional, supported Markdown directives. |
   | value | int, float, decimal.Decimal, str, or None |  | Value of the metric. None is rendered as a long dash. |
   | delta | int, float, decimal.Decimal, str, or None |  | Indicator of how the metric changed, rendered with an arrow below the metric. If delta is negative (int/float) or starts with a minus sign (str), the arrow points down and the text is red; else the arrow points up and the text is green. If None (default), no delta indicator is shown. |
   | delta_color | "normal", "inverse", or "off" |  | If "normal" (default), the delta indicator is shown as described above. If "inverse", it is red when positive and green when negative. This is useful when a negative change is considered good, e.g. if cost decreased. If "off", delta is  shown in gray regardless of its value. |
   | help | str or None |  | A tooltip that gets displayed next to the metric label. Streamlit only displays the tooltip when label_visibility="visible". If this is None (default), no tooltip is displayed. The tooltip can optionally contain GitHub-flavored Markdown, including the Markdown directives described in the body parameter of st.markdown. |
   | label_visibility | "visible", "hidden", or "collapsed" | is | The visibility of the label. The default is "visible". If this is "hidden", Streamlit displays an empty spacer instead of the label, which can help keep the widget aligned with other widgets. If this is "collapsed", Streamlit displays no label or spacer. |
   | border | bool |  | Whether to show a border around the metric container. If this is False (default), no border is shown. If this is True, a border is shown. |
   | height | "content", "stretch", or int |  | The height of the metric element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | width | "stretch", "content", or int |  | The width of the metric element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | chart_data | Iterable or None |  | A sequence of numeric values to display as a sparkline chart. If this is None (default), no chart is displayed. The sequence can be anything supported by st.dataframe, including a list or set. If the sequence is dataframe-like, the first column will be used. Each value will be cast to float internally by default. |
   | chart_type | "line", "bar", or "area" |  | The type of sparkline chart to display. This can be one of the following:  "line" (default): A simple sparkline. "area": A sparkline with area shading. "bar": A bar chart. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.json


* Function signature:

   st.json(body, *, expanded=True, width="stretch")

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | body | object or str |  | The object to print as JSON. All referenced objects should be serializable to JSON as well. If object is a string, we assume it contains serialized JSON. |
   | expanded | bool or int |  | The initial expansion state of the JSON element. This can be one of the following:  True (default): The element is fully expanded. False: The element is fully collapsed. An integer: The element is expanded to the depth specified. The integer must be non-negative. expanded=0 is equivalent to expanded=False.  Regardless of the initial expansion state, users can collapse or expand any key-value pair to show or hide any part of the object. |
   | width | "stretch" or int |  | The width of the JSON element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |



---

Source: https://docs.streamlit.io/develop/api-reference/data/st.experimental_data_editor

[Function 'streamlit.experimental_data_editor' not found]

---

# Chart elements

Source: https://docs.streamlit.io/develop/api-reference/charts


Streamlit supports several different charting libraries, and our goal is to
continually add support for more. Right now, the most basic library in our
arsenal is [Matplotlib](https://matplotlib.org/). Then there are also
interactive charting libraries like [Vega
Lite](https://vega.github.io/vega-lite/) (2D charts) and
[deck.gl](https://github.com/uber/deck.gl) (maps and 3D charts). And
finally we also provide a few chart types that are "native" to Streamlit,
like `st.line_chart` and `st.area_chart`.

## Simple chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.area_chart">
<Image>alt="screenshot" src="/images/api/area_chart.jpg" /&gt;

<h4>Simple area charts</h4>

Display an area chart.

```python
st.area_chart(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.bar_chart">
<Image>alt="screenshot" src="/images/api/bar_chart.jpg" /&gt;

<h4>Simple bar charts</h4>

Display a bar chart.

```python
st.bar_chart(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.line_chart">
<Image>alt="screenshot" src="/images/api/line_chart.jpg" /&gt;

<h4>Simple line charts</h4>

Display a line chart.

```python
st.line_chart(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.scatter_chart">
<Image>alt="screenshot" src="/images/api/scatter_chart.svg" /&gt;

<h4>Simple scatter charts</h4>

Display a line chart.

```python
st.scatter_chart(my_data_frame)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.map">
<Image>alt="screenshot" src="/images/api/map.jpg" /&gt;

<h4>Scatterplots on maps</h4>

Display a map with points on it.

```python
st.map(my_data_frame)
```

</Image></RefCard>
</TileContainer>

## Advanced chart elements

<TileContainer>
<RefCard href="/develop/api-reference/charts/st.pyplot">
<Image>alt="screenshot" src="/images/api/pyplot.jpg" /&gt;

<h4>Matplotlib</h4>

Display a matplotlib.pyplot figure.

```python
st.pyplot(my_mpl_figure)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.altair_chart">
<Image>alt="screenshot" src="/images/api/vega_lite_chart.jpg" /&gt;

<h4>Altair</h4>

Display a chart using the Altair library.

```python
st.altair_chart(my_altair_chart)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.vega_lite_chart">
<Image>alt="screenshot" src="/images/api/vega_lite_chart.jpg" /&gt;

<h4>Vega-Lite</h4>

Display a chart using the Vega-Lite library.

```python
st.vega_lite_chart(my_vega_lite_chart)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.plotly_chart">
<Image>alt="screenshot" src="/images/api/plotly_chart.jpg" /&gt;

<h4>Plotly</h4>

Display an interactive Plotly chart.

```python
st.plotly_chart(my_plotly_chart)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.bokeh_chart">
<Image>alt="screenshot" src="/images/api/bokeh_chart.jpg" /&gt;

<h4>Bokeh</h4>

Display an interactive Bokeh chart.

```python
st.bokeh_chart(my_bokeh_chart)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.pydeck_chart">
<Image>alt="screenshot" src="/images/api/pydeck_chart.jpg" /&gt;

<h4>PyDeck</h4>

Display a chart using the PyDeck library.

```python
st.pydeck_chart(my_pydeck_chart)
```

</Image></RefCard>
<RefCard href="/develop/api-reference/charts/st.graphviz_chart">
<Image>alt="screenshot" src="/images/api/graphviz_chart.jpg" /&gt;

<h4>GraphViz</h4>

Display a graph using the dagre-d3 library.

```python
st.graphviz_chart(my_graphviz_spec)
```

</Image></RefCard>
</TileContainer>
<ComponentSlider>
<ComponentCard href="https://github.com/tvst/plost">
<Image>alt="screenshot" src="/images/api/components/plost.jpg" /&gt;

<h4>Plost</h4>

A deceptively simple plotting library for Streamlit. Created by [@tvst](https://github.com/tvst).

```python
import plost
plost.line_chart(my_dataframe, x='time', y='stock_value', color='stock_name',)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/facebookresearch/hiplot">
<Image>alt="screenshot" src="/images/api/components/hiplot.jpg" /&gt;

<h4>HiPlot</h4>

High dimensional Interactive Plotting. Created by [@facebookresearch](https://github.com/facebookresearch).

```python
data = [{'dropout':0.1, 'lr': 0.001, 'loss': 10.0, 'optimizer': 'SGD'}, {'dropout':0.15, 'lr': 0.01, 'loss': 3.5, 'optimizer': 'Adam'}, {'dropout':0.3, 'lr': 0.1, 'loss': 4.5, 'optimizer': 'Adam'}]
hip.Experiment.from_iterable(data).display()
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/andfanilo/streamlit-echarts">
<Image>alt="screenshot" src="/images/api/components/echarts.jpg" /&gt;

<h4>ECharts</h4>

High dimensional Interactive Plotting. Created by [@andfanilo](https://github.com/andfanilo).

```python
from streamlit_echarts import st_echarts
st_echarts(options=options)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/randyzwitch/streamlit-folium">
<Image>alt="screenshot" src="/images/api/components/folium.jpg" /&gt;

<h4>Streamlit Folium</h4>

Streamlit Component for rendering Folium maps. Created by [@randyzwitch](https://github.com/randyzwitch).

```python
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
st_data = st_folium(m, width=725)
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/explosion/spacy-streamlit">
<Image>alt="screenshot" src="/images/api/components/spacy.jpg" /&gt;

<h4>Spacy-Streamlit</h4>

spaCy building blocks and visualizers for Streamlit apps. Created by [@explosion](https://github.com/explosion).

```python
models = ["en_core_web_sm", "en_core_web_md"]
spacy_streamlit.visualize(models, "Sundar Pichai is the CEO of Google.")
```

</Image></ComponentCard>
<ComponentCard href="https://github.com/ChrisDelClea/streamlit-agraph">
<Image>alt="screenshot" src="/images/api/components/agraph.jpg" /&gt;

<h4>Streamlit Agraph</h4>

A Streamlit Graph Vis, based on [react-grah-vis](https://github.com/crubier/react-graph-vis). Created by [@ChrisDelClea](https://github.com/ChrisDelClea).

```python
from streamlit_agraph import agraph, Node, Edge, Config
agraph(nodes=nodes, edges=edges, config=config)
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
<ComponentCard href="https://github.com/null-jones/streamlit-plotly-events">
<Image>alt="screenshot" src="/images/api/components/plotly-events.jpg" /&gt;

<h4>Plotly Events</h4>

Make Plotly charts interactive!. Created by [@null-jones](https://github.com/null-jones/).

```python
fig = px.line(x=[1], y=[1])
selected_points = plotly_events(fig)
```

</Image></ComponentCard>
<ComponentCard href="https://extras.streamlit.app/">
<Image>alt="screenshot" src="/images/api/components/extras-chart-annotations.jpg" /&gt;

<h4>Streamlit Extras</h4>

A library with useful Streamlit extras. Created by [@arnaudmiribel](https://github.com/arnaudmiribel/).

```python
chart += get_annotations_chart(annotations=[("Mar 01, 2008", "Pretty good day for GOOG"), ("Dec 01, 2007", "Something's going wrong for GOOG  AAPL"), ("Nov 01, 2008", "Market starts again thanks to..."), ("Dec 01, 2009", "Small crash for GOOG after..."),],)
st.altair_chart(chart, use_container_width=True)
```

</Image></ComponentCard>
</ComponentSlider>

---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.area_chart


* Function signature:

   st.area_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width="stretch", height="content", use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | Data to be plotted. |
   | x | str or None |  | Column name or key associated to the x-axis data. If x is None (default), Streamlit uses the data index for the x-axis values. |
   | y | str, Sequence of str, or None |  | Column name(s) or key(s) associated to the y-axis data. If this is None (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes. |
   | x_label | str or None |  | The label for the x-axis. If this is None (default), Streamlit will use the column name specified in x if available, or else no label will be displayed. |
   | y_label | str or None |  | The label for the y-axis. If this is None (default), Streamlit will use the column name(s) specified in y if available, or else no label will be displayed. |
   | color | str, tuple, Sequence of str, Sequence of tuple, or None | color | The color to use for different series in this chart. For an area chart with just 1 series, this can be:  None, to use the default color. A hex string like "#ffaa00" or "#ffaa0088". An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.  For an area chart with multiple series, where the dataframe is in long format (that is, y is None or just one column), this can be:  None, to use the default colors.  The name of a column in the dataset. Data points will be grouped into series of the same color based on the value of this column. In addition, if the values in this column match one of the color formats above (hex string or color tuple), then that color will be used. For example: if the dataset has 1000 rows, but this column only contains the values "adult", "child", and "baby", then those 1000 datapoints will be grouped into three series whose colors will be automatically selected from the default palette. But, if for the same 1000-row dataset, this column contained the values "#ffaa00", "#f0f", "#0000ff", then then those 1000 datapoints would still be grouped into 3 series, but their colors would be "#ffaa00", "#f0f", "#0000ff" this time around.   For an area chart with multiple series, where the dataframe is in wide format (that is, y is a Sequence of columns), this can be:  None, to use the default colors. A list of string colors or color tuples to be used for each of the series in the chart. This list should have the same length as the number of y values (e.g. color=["#fd0", "#f0f", "#04f"] for three lines).  You can set the default colors in the theme.chartCategoryColors configuration option. |
   | stack | bool, "normalize", "center", or None |  | Whether to stack the areas. If this is None (default), Streamlit uses Vega's default. Other values can be as follows:  True: The areas form a non-overlapping, additive stack within the chart. False: The areas overlap each other without stacking. "normalize": The areas are stacked and the total height is normalized to 100% of the height of the chart. "center": The areas are stacked and shifted to center their baseline, which creates a steamgraph. |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "stretch", "content", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None | behavior | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the chart's default behavior. True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart


* Function signature:

   st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, sort=True, stack=None, width="stretch", height="content", use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | Data to be plotted. |
   | x | str or None |  | Column name or key associated to the x-axis data. If x is None (default), Streamlit uses the data index for the x-axis values. |
   | y | str, Sequence of str, or None |  | Column name(s) or key(s) associated to the y-axis data. If this is None (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes. |
   | x_label | str or None |  | The label for the x-axis. If this is None (default), Streamlit will use the column name specified in x if available, or else no label will be displayed. |
   | y_label | str or None |  | The label for the y-axis. If this is None (default), Streamlit will use the column name(s) specified in y if available, or else no label will be displayed. |
   | color | str, tuple, Sequence of str, Sequence of tuple, or None | color | The color to use for different series in this chart. For a bar chart with just one series, this can be:  None, to use the default color. A hex string like "#ffaa00" or "#ffaa0088". An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.  For a bar chart with multiple series, where the dataframe is in long format (that is, y is None or just one column), this can be:  None, to use the default colors.  The name of a column in the dataset. Data points will be grouped into series of the same color based on the value of this column. In addition, if the values in this column match one of the color formats above (hex string or color tuple), then that color will be used. For example: if the dataset has 1000 rows, but this column only contains the values "adult", "child", and "baby", then those 1000 datapoints will be grouped into three series whose colors will be automatically selected from the default palette. But, if for the same 1000-row dataset, this column contained the values "#ffaa00", "#f0f", "#0000ff", then then those 1000 datapoints would still be grouped into 3 series, but their colors would be "#ffaa00", "#f0f", "#0000ff" this time around.   For a bar chart with multiple series, where the dataframe is in wide format (that is, y is a Sequence of columns), this can be:  None, to use the default colors. A list of string colors or color tuples to be used for each of the series in the chart. This list should have the same length as the number of y values (e.g. color=["#fd0", "#f0f", "#04f"] for three lines).  You can set the default colors in the theme.chartCategoryColors configuration option. |
   | horizontal | bool |  | Whether to make the bars horizontal. If this is False (default), the bars display vertically. If this is True, Streamlit swaps the x-axis and y-axis and the bars display horizontally. |
   | sort | bool or str | sorting | How to sort the bars. This can be one of the following:  True (default): The bars are sorted automatically along the independent/categorical axis with Altair's default sorting. This also correctly sorts ordered categorical columns (pd.Categorical). False: The bars are shown in data order without sorting. The name of a column (e.g. "col1"): The bars are sorted by that column in ascending order. The name of a column with a minus-sign prefix (e.g. "-col1"): The bars are sorted by that column in descending order. |
   | stack | bool, "normalize", "center", "layered", or None |  | Whether to stack the bars. If this is None (default), Streamlit uses Vega's default. Other values can be as follows:  True: The bars form a non-overlapping, additive stack within the chart. False: The bars display side by side. "layered": The bars overlap each other without stacking. "normalize": The bars are stacked and the total height is normalized to 100% of the height of the chart. "center": The bars are stacked and shifted to center the total height around an axis. |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "stretch", "content", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None | behavior | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the chart's default behavior. True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.line_chart


* Function signature:

   st.line_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, width="stretch", height="content", use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | Data to be plotted. |
   | x | str or None |  | Column name or key associated to the x-axis data. If x is None (default), Streamlit uses the data index for the x-axis values. |
   | y | str, Sequence of str, or None |  | Column name(s) or key(s) associated to the y-axis data. If this is None (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes. |
   | x_label | str or None |  | The label for the x-axis. If this is None (default), Streamlit will use the column name specified in x if available, or else no label will be displayed. |
   | y_label | str or None |  | The label for the y-axis. If this is None (default), Streamlit will use the column name(s) specified in y if available, or else no label will be displayed. |
   | color | str, tuple, Sequence of str, Sequence of tuple, or None | color | The color to use for different lines in this chart. For a line chart with just one line, this can be:  None, to use the default color. A hex string like "#ffaa00" or "#ffaa0088". An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.  For a line chart with multiple lines, where the dataframe is in long format (that is, y is None or just one column), this can be:  None, to use the default colors.  The name of a column in the dataset. Data points will be grouped into lines of the same color based on the value of this column. In addition, if the values in this column match one of the color formats above (hex string or color tuple), then that color will be used. For example: if the dataset has 1000 rows, but this column only contains the values "adult", "child", and "baby", then those 1000 datapoints will be grouped into three lines whose colors will be automatically selected from the default palette. But, if for the same 1000-row dataset, this column contained the values "#ffaa00", "#f0f", "#0000ff", then then those 1000 datapoints would still be grouped into three lines, but their colors would be "#ffaa00", "#f0f", "#0000ff" this time around.   For a line chart with multiple lines, where the dataframe is in wide format (that is, y is a Sequence of columns), this can be:  None, to use the default colors. A list of string colors or color tuples to be used for each of the lines in the chart. This list should have the same length as the number of y values (e.g. color=["#fd0", "#f0f", "#04f"] for three lines).  You can set the default colors in the theme.chartCategoryColors configuration option. |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "content", "stretch", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None | behavior | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the chart's default behavior. True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.map


* Function signature:

   st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, width="stretch", height=500, use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | The data to be plotted. |
   | latitude | str or None |  | The name of the column containing the latitude coordinates of the datapoints in the chart. If None, the latitude data will come from any column named 'lat', 'latitude', 'LAT', or 'LATITUDE'. |
   | longitude | str or None |  | The name of the column containing the longitude coordinates of the datapoints in the chart. If None, the longitude data will come from any column named 'lon', 'longitude', 'LON', or 'LONGITUDE'. |
   | color | str or tuple or None | color | The color of the circles representing each datapoint. Can be:  None, to use the default color. A hex string like "#ffaa00" or "#ffaa0088". An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0. The name of the column to use for the color. Cells in this column should contain colors represented as a hex string or color tuple, as described above. |
   | size | str or float or None | size | The size of the circles representing each point, in meters. This can be:  None, to use the default size. A number like 100, to specify a single size to use for all datapoints. The name of the column to use for the size. This allows each datapoint to be represented by a circle of a different size. |
   | zoom | int |  | Zoom level as specified in https://wiki.openstreetmap.org/wiki/Zoom_levels. |
   | width | "stretch" or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "stretch" or int |  | The height of the chart element. This can be one of the following:  An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. This is 500 by default. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. |
   | use_container_width | bool or None | behavior | Whether to override the map's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the map's default behavior. True: Streamlit sets the width of the map to match the width of the parent container. False: Streamlit sets the width of the map to fit its contents according to the plotting library, up to the width of the parent container. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart


* Function signature:

   st.scatter_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, size=None, width="stretch", height="content", use_container_width=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | Anything supported by st.dataframe |  | Data to be plotted. |
   | x | str or None |  | Column name or key associated to the x-axis data. If x is None (default), Streamlit uses the data index for the x-axis values. |
   | y | str, Sequence of str, or None |  | Column name(s) or key(s) associated to the y-axis data. If this is None (default), Streamlit draws the data of all remaining columns as data series. If this is a Sequence of strings, Streamlit draws several series on the same chart by melting your wide-format table into a long-format table behind the scenes. |
   | x_label | str or None |  | The label for the x-axis. If this is None (default), Streamlit will use the column name specified in x if available, or else no label will be displayed. |
   | y_label | str or None |  | The label for the y-axis. If this is None (default), Streamlit will use the column name(s) specified in y if available, or else no label will be displayed. |
   | color | str, tuple, Sequence of str, Sequence of tuple, or None | color | The color of the circles representing each datapoint. This can be:  None, to use the default color.  A hex string like "#ffaa00" or "#ffaa0088".  An RGB or RGBA tuple with the red, green, blue, and alpha components specified as ints from 0 to 255 or floats from 0.0 to 1.0.  The name of a column in the dataset where the color of that datapoint will come from. If the values in this column are in one of the color formats above (hex string or color tuple), then that color will be used. Otherwise, the color will be automatically picked from the default palette. For example: if the dataset has 1000 rows, but this column only contains the values "adult", "child", and "baby", then those 1000 datapoints be shown using three colors from the default palette. But if this column only contains floats or ints, then those 1000 datapoints will be shown using a colors from a continuous color gradient. Finally, if this column only contains the values "#ffaa00", "#f0f", "#0000ff", then then each of those 1000 datapoints will be assigned "#ffaa00", "#f0f", or "#0000ff" as appropriate.   If the dataframe is in wide format (that is, y is a Sequence of columns), this can also be:  A list of string colors or color tuples to be used for each of the series in the chart. This list should have the same length as the number of y values (e.g. color=["#fd0", "#f0f", "#04f"] for three series). |
   | size | str, float, int, or None |  | The size of the circles representing each point. This can be:  A number like 100, to specify a single size to use for all datapoints. The name of the column to use for the size. This allows each datapoint to be represented by a circle of a different size. |
   | width | "stretch", "content", or int |  | The width of the chart element. This can be one of the following:  "stretch" (default): The width of the element matches the width of the parent container. "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container. An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container. |
   | height | "stretch", "content", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None | behavior | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the chart's default behavior. True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |



* Function signature:

   element.add_rows(data=None, **kwargs)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | data | pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, Iterable, dict, or None |  | Table to concat. Optional. |
   | **kwargs | pandas.DataFrame, numpy.ndarray, Iterable, dict, or None |  | The named dataset to concat. Optional. You can only pass in 1 dataset (including the one in the data parameter). |



---

Source: https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart


* Function signature:

   st.altair_chart(altair_chart, *, width=None, height="content", use_container_width=None, theme="streamlit", key=None, on_select="ignore", selection_mode=None)

* Parameters:

   | name | type | default | description |
   |---|---|---|---|
   | altair_chart | altair.Chart |  | The Altair chart object to display. See https://altair-viz.github.io/gallery/ for examples of graph descriptions. |
   | width | "stretch", "content", int, or None |  | The width of the chart element. This can be one of the following:  "stretch": The width of the element matches the width of the parent container.  "content": The width of the element matches the width of its content, but doesn't exceed the width of the parent container.  An integer specifying the width in pixels: The element has a fixed width. If the specified width is greater than the width of the parent container, the width of the element matches the width of the parent container.  None (default): Streamlit uses "stretch" for most charts, and uses "content" for the following multi-view charts:   Facet charts: the spec contains "facet" or encodings for "row", "column", or "facet". Horizontal concatenation charts: the spec contains "hconcat". Repeat charts: the spec contains "repeat". |
   | height | "content", "stretch", or int |  | The height of the chart element. This can be one of the following:  "content" (default): The height of the element matches the height of its content. "stretch": The height of the element matches the height of its content or the height of the parent container, whichever is larger. If the element is not in a parent container, the height of the element matches the height of its content. An integer specifying the height in pixels: The element has a fixed height. If the content is larger than the specified height, scrolling is enabled. |
   | use_container_width | bool or None |  | Whether to override the chart's native width with the width of the parent container. This can be one of the following:  None (default): Streamlit will use the parent container's width for all charts except those with known incompatibility (altair.Facet, altair.HConcatChart, and altair.RepeatChart). True: Streamlit sets the width of the chart to match the width of the parent container. False: Streamlit sets the width of the chart to fit its contents according to the plotting library, up to the width of the parent container. |
   | theme | "streamlit" or None | behavior | The theme of the chart. If theme is "streamlit" (default), Streamlit uses its own design default. If theme is None, Streamlit falls back to the default behavior of the library. The "streamlit" theme can be partially customized through the configuration options theme.chartCategoricalColors and theme.chartSequentialColors. Font configuration options are also applied. |
   | key | str |  | An optional string to use for giving this element a stable identity. If key is None (default), this element's identity will be determined based on the values of the other parameters. Additionally, if selections are activated and key is provided, Streamlit will register the key in Session State to store the selection state. The selection state is read-only. |
   | on_select | "ignore", "rerun", or callable |  | How the figure should respond to user selection events. This controls whether or not the figure behaves like an input widget. on_select can be one of the following:  "ignore" (default): Streamlit will not react to any selection events in the chart. The figure will not behave like an input widget. "rerun": Streamlit will rerun the app when the user selects data in the chart. In this case, st.altair_chart will return the selection data as a dictionary. A callable: Streamlit will rerun the app and execute the callable as a callback function before the rest of the app. In this case, st.altair_chart will return the selection data as a dictionary.  To use selection events, the object passed to altair_chart must include selection parameters. To learn about defining interactions in Altair and how to declare selection-type parameters, see Interactive Charts in Altair's documentation. |
   | selection_mode | str or Iterable of str |  | The selection parameters Streamlit should use. If selection_mode is None (default), Streamlit will use all selection parameters defined in the chart's Altair spec. When Streamlit uses a selection parameter, selections from that parameter will trigger a rerun and be included in the selection state. When Streamlit does not use a selection parameter, selections from that parameter will not trigger a rerun and not be included in the selection state. Selection parameters are identified by their name property. |

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

Altair charts are displayed using the Streamlit theme by default. This theme is sleek, user-friendly, and incorporates Streamlit's color palette. The added benefit is that your charts better integrate with the rest of your app's design.

The Streamlit theme is available from Streamlit 1.16.0 through the `theme="streamlit"` keyword argument. To disable it, and use Altair's native theme, use `theme=None` instead.

Let's look at an example of charts with the Streamlit theme and the native Altair theme:

```python
import altair as alt
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
```

Click the tabs in the interactive app below to see the charts with the Streamlit theme enabled and disabled.

<Cloud height="500px" name="doc-altair-chart"/>

If you're wondering if your own customizations will still be taken into account, don't worry! You can still make changes to your chart configurations. In other words, although we now enable the Streamlit theme by default, you can overwrite it with custom colors or fonts. For example, if you want a chart line to be green instead of the default red, you can do it!

Here's an example of an Altair chart where manual color passing is done and reflected:

<Collapse title="See the code">

```python
import altair as alt
import streamlit as st
from vega_datasets import data

source = data.seattle_weather()

scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(date):T", title="Date"),
        alt.Y(
            "temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)


---

**Navigation:** [← Previous](./03-customize-colors-and-borders-in-your-streamlit-app.md) | [Index](./index.md) | [Next →](./05-bottom-panel-is-a-bar-chart-of-weather-type.md)
