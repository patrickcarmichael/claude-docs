---
title: "Crewai: Response Format"
description: "Response Format section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Response Format


The tool returns a JSON string representing the structured data extracted from the provided URL(s). The exact structure depends on the content of the pages and the `extract_depth` used.

Common response elements include:

* **Title**: The page title
* **Content**: Main text content of the page
* **Images**: Image URLs and metadata (when `include_images=True`)
* **Metadata**: Additional page information like author, description, etc.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Features](./1164-features.md)

**Next:** [Use Cases →](./1166-use-cases.md)
