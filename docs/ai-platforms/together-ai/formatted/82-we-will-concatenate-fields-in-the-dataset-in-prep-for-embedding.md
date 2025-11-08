---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## We will concatenate fields in the dataset in prep for embedding

to_embed = []

for movie in movies_data:
    text = ""
    for field in ["title", "overview", "tagline"]:
        value = movie.get(field, "")
        text += str(value) + " "
    to_embed.append(text.strip())

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
