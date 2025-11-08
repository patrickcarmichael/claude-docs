---
title: "Crewai: Implementation Details"
description: "Implementation Details section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Implementation Details


The `SeleniumScrapingTool` uses Selenium WebDriver to automate browser interactions:

```python Code theme={null}
class SeleniumScrapingTool(BaseTool):
    name: str = "Read a website content"
    description: str = "A tool that can be used to read a website content."
    args_schema: Type[BaseModel] = SeleniumScrapingToolSchema
    
    def _run(self, **kwargs: Any) -> Any:
        website_url = kwargs.get("website_url", self.website_url)
        css_element = kwargs.get("css_element", self.css_element)
        return_html = kwargs.get("return_html", self.return_html)
        driver = self._create_driver(website_url, self.cookie, self.wait_time)

        content = self._get_content(driver, css_element, return_html)
        driver.close()

        return "\n".join(content)
```

The tool performs the following steps:

1. Creates a headless Chrome browser instance
2. Navigates to the specified URL
3. Waits for the specified time to allow the page to load
4. Adds any cookies if provided
5. Extracts content based on the CSS selector
6. Returns the extracted content as text or HTML
7. Closes the browser instance

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1384-run-the-task.md)

**Next:** [Handling Dynamic Content →](./1386-handling-dynamic-content.md)
