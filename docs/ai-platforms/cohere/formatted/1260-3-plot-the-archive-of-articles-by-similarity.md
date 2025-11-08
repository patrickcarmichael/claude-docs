---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3- Plot the archive of articles by similarity

What if we want to browse the archive instead of only searching it? Let's plot all the questions in a 2D chart so you're able to visualize the posts in the archive and their similarities.
```python PYTHON
reducer = umap.UMAP(n_neighbors=100)
umap_embeds = reducer.fit_transform(embeds)
```
```python PYTHON
df['x'] = umap_embeds[:,0]
df['y'] = umap_embeds[:,1]

chart = alt.Chart(df).mark_circle(size=60).encode(
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
    tooltip=['title']
    ).configure(background="#FDF7F0"
    ).properties(
        width=700,
        height=400,
        title='Ask HN: top 3,000 posts'
        )

chart.interactive()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
