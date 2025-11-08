---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 4. Visualizing the archive

Finally, let's plot out all the questions onto a 2D chart so you're able to visualize the semantic similarities of this dataset!
```python PYTHON
##@title Plot the archive {display-mode: "form"}

reducer = umap.UMAP(n_neighbors=20)
umap_embeds = reducer.fit_transform(embeds)
df_explore = pd.DataFrame(data={'text': df['text']})
df_explore['x'] = umap_embeds[:,0]
df_explore['y'] = umap_embeds[:,1]

chart = alt.Chart(df_explore).mark_circle(size=60).encode(
    x=#'x',
    alt.X('x',
        scale=alt.Scale(zero=False)
    ),
    y=
    alt.Y('y',
        scale=alt.Scale(zero=False)
    ),
    tooltip=['text']
).properties(
    width=700,
    height=400
)
chart.interactive()
```
Hover over the points to read the text. Do you see some of the patterns in clustered points? Similar questions, or questions asking about similar topics?

This concludes this introductory guide to semantic search using sentence embeddings. As you continue the path of building a search product additional considerations arise (like dealing with long texts, or finetuning to better improve the embeddings for a specific use case).

We can’t wait to see what you start building! Share your projects or find support on [Discord](https://discord.com/invite/co-mmunity).


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
