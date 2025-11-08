---
title: "Langgraph: Create a tool for each company and store it in a registry with a unique UUID as the key"
description: "Create a tool for each company and store it in a registry with a unique UUID as the key section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Create a tool for each company and store it in a registry with a unique UUID as the key

tool_registry = {
    str(uuid.uuid4()): create_tool(company) for company in s_and_p_500_companies
}
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Abbreviated list of S&P 500 companies for demonstration](./191-abbreviated-list-of-sp-500-companies-for-demonstra.md)

**Next:** [Define the graph →](./193-define-the-graph.md)
