---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Extract out the titles and overviews of the top 10 most similar movies

titles = [movies_data[index]["title"] for index in indices[0]][:10]
overviews = [movies_data[index]["overview"] for index in indices[0]][:10]

client = Together(api_key=TOGETHER_API_KEY)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
