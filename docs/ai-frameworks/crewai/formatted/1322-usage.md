---
title: "Crewai: Usage"
description: "Usage section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Usage


When using the `ScrapegraphScrapeTool` with an agent, the agent will need to provide the following parameters (unless they were specified during initialization):

* **website\_url**: The URL of the website to scrape.
* **user\_prompt**: Optional. Custom instructions for content extraction. Default is "Extract the main content of the webpage".

The tool will return the extracted content based on the provided prompt.

```python Code theme={null}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parameters](./1321-parameters.md)

**Next:** [Example of using the tool with an agent →](./1323-example-of-using-the-tool-with-an-agent.md)
