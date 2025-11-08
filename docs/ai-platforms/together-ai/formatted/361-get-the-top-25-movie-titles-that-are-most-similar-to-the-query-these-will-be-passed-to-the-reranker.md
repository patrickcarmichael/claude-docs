---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Get the top 25 movie titles that are most similar to the query - these will be passed to the reranker

top_25_sorted_titles = [movies_data[index]["title"] for index in indices[0]][
    :25
]
```
```json
['The Dark Knight',
 'Watchmen',
 'Predator',
 'Despicable Me 2',
 'Night at the Museum: Secret of the Tomb',
 'Batman v Superman: Dawn of Justice',
 'Penguins of Madagascar',
 'Batman & Robin',
 'Batman Begins',
 'Super 8',
 'Megamind',
 'The Dark Knight Rises',
 'Batman Returns',
 'The Incredibles',
 'The Raid',
 'Die Hard: With a Vengeance',
 'Kick-Ass',
 'Fantastic Mr. Fox',
 'Commando',
 'Tremors',
 'The Peanuts Movie',
 'Kung Fu Panda 2',
 'Crank: High Voltage',
 'Men in Black 3',
 'ParaNorman']
```

Notice here that not all movies in our top 25 have to do with our query - super hero mystery action movie about bats. This is because semantic search capture the "approximate" meaning of the query and movies.

The reranker can more closely determine the similarity between these 25 candidates and rerank which ones deserve to be atop our list.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
