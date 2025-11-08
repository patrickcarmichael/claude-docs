---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Paste in your Together AI API Key or load it

TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")

import json

with open("./datasets/movies.json", "r") as file:
    movies_data = json.load(file)

movies_data[:1]
```
This dataset consists of movie information as below:
```py
[
    {
        "title": "Minions",
        "overview": "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.",
        "director": "Kyle Balda",
        "genres": "Family Animation Adventure Comedy",
        "tagline": "Before Gru, they had a history of bad bosses",
    },
    {
        "title": "Interstellar",
        "overview": "Interstellar chronicles the adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
        "director": "Christopher Nolan",
        "genres": "Adventure Drama Science Fiction",
        "tagline": "Mankind was born on Earth. It was never meant to die here.",
    },
    {
        "title": "Deadpool",
        "overview": "Deadpool tells the origin story of former Special Forces operative turned mercenary Wade Wilson, who after being subjected to a rogue experiment that leaves him with accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life.",
        "director": "Tim Miller",
        "genres": "Action Adventure Comedy",
        "tagline": "Witness the beginning of a happy ending",
    },
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
