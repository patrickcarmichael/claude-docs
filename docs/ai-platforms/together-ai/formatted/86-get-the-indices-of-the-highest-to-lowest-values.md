---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get the indices of the highest to lowest values

indices = np.argsort(-similarity_scores)

top_10_sorted_titles = [movies_data[index]["title"] for index in indices[0]][
    :10
]

top_10_sorted_titles
```
This produces the top ten most similar movie titles below:
```
['The Incredibles',
 'Watchmen',
 'Mr. Peabody & Sherman',
 'Due Date',
 'The Next Three Days',
 'Super 8',
 'Iron Man',
 'After Earth',
 'Men in Black 3',
 'Despicable Me 2']
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
