---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `ScrapeElementFromWebsiteTool` uses the `requests` library to fetch the web page and `BeautifulSoup` to parse the HTML and extract the specified elements:

```python Code theme={null}
class ScrapeElementFromWebsiteTool(BaseTool):
    name: str = "Read a website content"
    description: str = "A tool that can be used to read a website content."
    
    # Implementation details...
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        css_element = kwargs.get("css_element", self.css_element)
        page = requests.get(
            website_url,
            headers=self.headers,
            cookies=self.cookies if self.cookies else {},
        )
        parsed = BeautifulSoup(page.content, "html.parser")
        elements = parsed.select(css_element)
        return "\n".join([element.get_text() for element in elements])
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task through a crew](./1307-run-the-task-through-a-crew.md)

**Next:** [Conclusion →](./1309-conclusion.md)
