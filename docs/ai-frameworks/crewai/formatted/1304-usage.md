---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


When using the `ScrapeElementFromWebsiteTool` with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: The URL of the website to scrape.
* **css\_element**: The CSS selector for the elements to extract.

The tool will return the text content of all elements matching the CSS selector, joined by newlines.

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./1303-parameters.md)

**Next:** [Example of using the tool with an agent →](./1305-example-of-using-the-tool-with-an-agent.md)
