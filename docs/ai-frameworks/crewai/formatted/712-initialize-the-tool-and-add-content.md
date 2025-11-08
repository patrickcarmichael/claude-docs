---
title: "Crewai: Initialize the tool and add content"
description: "Initialize the tool and add content section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the tool and add content

rag_tool = RagTool()
rag_tool.add(data_type="web_page", url="https://docs.crewai.com")
rag_tool.add(data_type="file", path="company_data.pdf")

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Agent Integration Example](./711-agent-integration-example.md)

**Next:** [Define an agent with the RagTool →](./713-define-an-agent-with-the-ragtool.md)
