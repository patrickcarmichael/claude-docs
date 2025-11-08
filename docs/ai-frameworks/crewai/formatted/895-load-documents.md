---
title: "Crewai: Load documents"
description: "Load documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Load documents

docs_to_load = os.listdir("knowledge")
with test_docs.batch.dynamic() as batch:
    for d in docs_to_load:
        with open(os.path.join("knowledge", d), "r") as f:
            content = f.read()
        batch.add_object(
            {
                "content": content,
                "year": d.split("_")[0],
            }
        )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Get or create collection](./894-get-or-create-collection.md)

**Next:** [Initialize the tool →](./896-initialize-the-tool.md)
