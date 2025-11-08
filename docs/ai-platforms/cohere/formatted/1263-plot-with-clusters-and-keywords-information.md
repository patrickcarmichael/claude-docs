---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Plot with clusters and keywords information

We can now plot the documents with their clusters and keywords
```python PYTHON
selection = alt.selection_multi(fields=['keywords'], bind='legend')

chart = alt.Chart(df).transform_calculate(
    url='https://news.ycombinator.com/item?id=' + alt.datum.id
).mark_circle(size=60, stroke='#666', strokeWidth=1, opacity=0.3).encode(
    x=#'x',
    alt.X('x',
        scale=alt.Scale(zero=False),
        axis=alt.Axis(labels=False, ticks=False, domain=False)
    ),
    y=
    alt.Y('y',
        scale=alt.Scale(zero=False),
        axis=alt.Axis(labels=False, ticks=False, domain=False)
    ),
    href='url:N',
    color=alt.Color('keywords:N',
                    legend=alt.Legend(columns=1, symbolLimit=0, labelFontSize=14)
                   ),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
    tooltip=['title', 'keywords', 'cluster', 'score', 'descendants']
).properties(
    width=800,
    height=500
).add_selection(
    selection
).configure_legend(labelLimit= 0).configure_view(
    strokeWidth=0
).configure(background="#FDF7F0").properties(
    title='Ask HN: Top 3,000 Posts'
)
chart.interactive()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
