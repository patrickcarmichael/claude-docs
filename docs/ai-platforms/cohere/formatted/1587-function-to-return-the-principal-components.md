---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Function to return the principal components

def get_pc(arr,n):
  pca = PCA(n_components=n)
  embeds_transform = pca.fit_transform(arr)
  return embeds_transform

def make_clusters(df,n_clusters):

    # Get the embeddings for the text column

    df_clust = df.copy()
    df_clust['text_embeds'] = df_clust['texts'].apply(get_embeddings) # We've defined this function above.

    # Convert the embeddings list to a numpy array

    embeddings_array = np.array(df_clust['text_embeds'].tolist())
    # Cluster the embeddings

    kmeans_model = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto')
    classes = kmeans_model.fit_predict(embeddings_array).tolist()
    df_clust['cluster'] = (list(map(str,classes)))

    df_clust.columns.astype(str)
    return df_clust

def create_cluster_names(essences_dict):
    cluster_names = {}
    for cluster_num, description in essences_dict.items():
        # Take the first sentence and limit to first N characters

        short_name = description.split('.')[0][:30].strip() + '...'
        cluster_names[cluster_num] = short_name
    return cluster_names
```

### Get Topic Essences

Then, the `get_essence` function calls out to a Cohere [Command endpoint](https://docs.cohere.com/reference/chat) to create an 'essentialized' description of the papers in a given cluster. Like the 'short names' from above this will improve the readibility of our plot, because otherwise it would be of limited use.
```python PYTHON
def get_essence(df):

    clusters = sorted(df['cluster'].unique())
    cluster_descriptions = {}

    for cluster_num in clusters:
        
        cluster_df = df[df['cluster'] == cluster_num]
        # Combine titles and texts

        titles = ' '.join(cluster_df['titles'].fillna(''))
        texts = ' '.join(cluster_df['texts'].fillna(''))
        combined_text = f"Titles: {titles}\n\nTexts: {texts}"

        system_message = """
        ## Task & Context

        You are a world-class language model that's especially good at capturing the essence of complex text.

        ## Style Guide

        Unless the user asks for a different style of answer, you should answer in concise text with proper grammar and spelling.
        """

        message=f"""Based on the following titles and texts from academic papers, provide 3-4 words that describe what this category of papers is about. Think of this like a word cloud.
        Focus on the main theme or topic that unifies these papers.
        Please do not use the words 'AI', 'Artificial Intelligence,' 'Machine Learning,' or 'ML' in your response.
        
        {combined_text}
        
        Description:"""

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": message},
        ]

        essence = co.chat(
            model="command-a-03-2025,
            messages=messages
        )

        description = essence.message.content[0].text.strip() + "."
        cluster_descriptions[cluster_num] = description     

    return cluster_descriptions
```

### Generating a Topic Plot

Finally, this `generate_chart` ties together the processing we've defined so far to create a beautiful Altair chart displaying the papers in our topics.
```python PYTHON
import altair as alt

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
