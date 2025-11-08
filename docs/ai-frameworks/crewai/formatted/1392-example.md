---
title: "Crewai: Example"
description: "Example section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Example


This example shows you how you can use the `SpiderTool` to enable your agent to scrape and crawl websites.
The data returned from the Spider API is already LLM-ready, so no need to do any cleaning there.

```python Code theme={null}
from crewai_tools import SpiderTool

def main():
    spider_tool = SpiderTool()

    searcher = Agent(
        role="Web Research Expert",
        goal="Find related information from specific URL's",
        backstory="An expert web researcher that uses the web extremely well",
        tools=[spider_tool],
        verbose=True,
    )

    return_metadata = Task(
        description="Scrape https://spider.cloud with a limit of 1 and enable metadata",
        expected_output="Metadata and 10 word summary of spider.cloud",
        agent=searcher
    )

    crew = Crew(
        agents=[searcher],
        tasks=[
            return_metadata,
        ],
        verbose=2
    )

    crew.kickoff()

if __name__ == "__main__":
    main()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Installation](./1391-installation.md)

**Next:** [Arguments →](./1393-arguments.md)
