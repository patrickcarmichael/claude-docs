---
title: "Crewai: Snippet: … as ChatGPT, have the potential to play a critical role in advancing our understanding of climate"
description: "Snippet: … as ChatGPT, have the potential to play a critical role in advancing our understanding of climate section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Snippet: … as ChatGPT, have the potential to play a critical role in advancing our understanding of climate

# ---

```

```python Code theme={null}
from crewai_tools import SerperDevTool

tool = SerperDevTool(
    country="fr",
    locale="fr",
    location="Paris, Paris, Ile-de-France, France",
    n_results=2,
)

print(tool.run(search_query="Jeux Olympiques"))

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Title: Potential use of chat gpt in global warming](./1143-title-potential-use-of-chat-gpt-in-global-warming.md)

**Next:** [Using Tool: Search the internet →](./1145-using-tool-search-the-internet.md)
