---
title: "Langgraph: Call the graph: here we call it to generate a list of jokes"
description: "Call the graph: here we call it to generate a list of jokes section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Call the graph: here we call it to generate a list of jokes

for step in graph.stream({"topic": "animals"}):
    print(step)
```

```json
{'generate_topics': {'subjects': ['lions', 'elephants', 'penguins']}}
{'generate_joke': {'jokes': ["Why don't lions like fast food? Because they can't catch it!"]}}
{'generate_joke': {'jokes': ["Why don't elephants use computers? They're afraid of the mouse!"]}}
{'generate_joke': {'jokes': ['Why don't penguins like talking to strangers at parties? Because they find it hard to break the ice.']}}
{'best_joke': {'best_selected_joke': 'penguins'}}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Map-Reduce and the Send API](./63-map-reduce-and-the-send-api.md)

**Next:** [Create and control loops →](./65-create-and-control-loops.md)
