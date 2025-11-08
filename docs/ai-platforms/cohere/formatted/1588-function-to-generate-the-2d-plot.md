---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Function to generate the 2D plot

def generate_chart(df,xcol,ycol,lbl='off',color='basic',title='', cluster_names=None):

  ## IMPORTANT

  ## We're using this function to create the 'x' and 'y' columns for the chart.

  ## We don't actually use the principal components anywhere else in the code.

  embeds = np.array(df['text_embeds'].tolist())
  embeds_pc2 = get_pc(embeds,2)
  # Add the principal components to dataframe

  df = pd.concat([df, pd.DataFrame(embeds_pc2)], axis=1)
  ## END IMPORTANT

  # Add cluster names to the dataframe if provided

  if cluster_names:
      df['cluster_label'] = df['cluster'].map(cluster_names)
  else:
      df['cluster_label'] = df['cluster']
  
  # Plot the 2D embeddings on a chart

  df.columns = df.columns.astype(str)

  if color == 'basic':
      color_encode = alt.value('#333293')
  else:
      color_encode = alt.Color('cluster_label:N',
          scale=alt.Scale(scheme='category20'),
          legend=alt.Legend(
              title="Topics",
              symbolLimit=len(cluster_names) if cluster_names else None,
              orient='right',
              labelLimit=500,  # Increase label width limit (default is 200)

              columns=1  # Force single column layout

          ))


  chart = alt.Chart(df).mark_circle(size=500).encode(
        x=alt.X(xcol,
            scale=alt.Scale(zero=False),
            axis=alt.Axis(labels=False, ticks=False, domain=False)
        ),
        y=alt.Y(ycol,
            scale=alt.Scale(zero=False),
            axis=alt.Axis(labels=False, ticks=False, domain=False)
        ),
        color=color_encode,
        tooltip=['titles', 'cluster_label']  # Updated to show cluster label in tooltip

    )

  if lbl == 'on':
    text = chart.mark_text(align='left', baseline='middle',dx=15, size=13,color='black').encode(text='title', color= alt.value('black'))
  else:
    text = chart.mark_text(align='left', baseline='middle',dx=10).encode()

  result = (chart + text).configure(background="#FDF7F0"
      ).properties(
          width=800,
          height=500,
          title=title
      ).configure_legend(
          orient='right',
          titleFontSize=18,
          labelFontSize=10,
          padding=5,  # Add some padding around the legend

          offset=5,   # Move legend away from chart

          labelLimit=500  # Also need to set it here

      )
      
  return result
```

### Calling the Functions

Since we've defined our logic in the functions above, we now need only to call them in order.
```python PYTHON

### Creating the baseline dataframe.

df = make_raw_df("https://arxiv.org/list/cs.AI/new")

### Defining our cluster number and making a 'cluster' dataframe.

n_clusters = 12
df_clust = make_clusters(df,n_clusters)

### Get the topic essences and cluster names

overview = get_essence(df_clust)
cluster_names = create_cluster_names(overview)

### Generate the chart

generate_chart(df_clust,'0','1',lbl='off',color='cluster',title=f'Clustering with {n_clusters} Clusters', cluster_names=cluster_names)
```
Your chart will look different, but it should be similar to this one:
![Topic modeling chart](file:9bca598c-dd83-41bd-8e81-7a6287274f0c)

Congratulations! You have created the word embeddings and visualized them using a scatter plot, showing the overall structure of these papers.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
