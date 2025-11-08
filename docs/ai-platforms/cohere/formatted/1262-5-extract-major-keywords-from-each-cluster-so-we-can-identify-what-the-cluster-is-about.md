---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 5- Extract major keywords from each cluster so we can identify what the cluster is about

```python PYTHON
documents =  df['title']
documents = pd.DataFrame({"Document": documents,
                          "ID": range(len(documents)),
                          "Topic": None})
documents['Topic'] = classes
documents_per_topic = documents.groupby(['Topic'], as_index=False).agg({'Document': ' '.join})
count_vectorizer = CountVectorizer(stop_words="english").fit(documents_per_topic.Document)
count = count_vectorizer.transform(documents_per_topic.Document)
words = count_vectorizer.get_feature_names_out()
```
```python PYTHON
ctfidf = ClassTfidfTransformer().fit_transform(count).toarray()
words_per_class = {label: [words[index] for index in ctfidf[label].argsort()[-10:]] for label in documents_per_topic.Topic}
df['cluster'] = classes
df['keywords'] = df['cluster'].map(lambda topic_num: ", ".join(np.array(words_per_class[topic_num])[:]))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
