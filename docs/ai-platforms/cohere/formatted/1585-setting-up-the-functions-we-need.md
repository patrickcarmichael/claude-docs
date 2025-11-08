---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setting up the Functions We Need

In this section, we'll walk through some of the Python code we'll need for our topic modeling project.

### Getting and Processing ArXiv Papers.

This `make_raw_df` function scrapes paper data from a given URL, pulling out titles and abstracts. It uses `BeautifulSoup` to parse the HTML content, extracting titles from elements with class `"list-title mathjax"` and abstracts from paragraph elements with class `"mathjax"`. Finally, it organizes this data into a pandas dataframe with two columns - "titles" and "texts" - where each row represents the information from a single paper.
```python PYTHON
def make_raw_df(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, "html.parser")

    titles=list()
    texts=list()

    # Extract titles from <div class="list-title mathjax">

    title_tags = soup.find_all(class_="list-title mathjax")
    for title_tag in title_tags:
        titles.append(title_tag.text.strip())  # Remove leading/trailing whitespace

    # Extract abstracts from <p class="mathjax">

    abstract_tags = soup.find_all('p', class_="mathjax")#, tag="p")
    for abstract_tag in abstract_tags:
        texts.append(abstract_tag.text.strip())

    df = pd.DataFrame({"titles": titles, "texts": texts})
    return df
```

### Generating embeddings

[Word embedding](https://docs.cohere.com/docs/embeddings) is a technique for learning a numerical representation of words. You can use these embeddings to:

• Cluster large amounts of text\
• Match a query with other similar sentences\
• Perform classification tasks like sentiment classification

All of which we will do today.

Cohere’s platform provides an [Embed endpoint](https://docs.cohere.com/reference/embed) that returns text embeddings. An embedding is a list of floating-point numbers, and it captures the semantic meaning of the represented text. Models used to create these embeddings are available in several; small models are faster while large models offer better performance.

In the `get_embeddings`, `make_clusters`, and `create_cluster_names` functions defined below, we'll generate embeddings from the papers, use principal component analysis to create axes for later plotting efforts, use KMeans clustering to group the embedded papers into broad topics, and create a 'short name' that captures the essence of each cluster. This short name will make our Altair plot easier to read.
```python PYTHON
def get_embeddings(text,model='embed-v4.0'):
  output = co.embed(
                model=model,
                texts=[text],
                input_type="classification",
                embedding_types=["float"],)
  return output.embeddings.float_[0]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
