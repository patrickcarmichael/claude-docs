---
title: "Crewai: Configuration Options"
description: "Configuration Options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Options


The `TavilySearchTool` accepts the following arguments during initialization or when calling the `run` method:

* `query` (str): **Required**. The search query string.
* `search_depth` (Literal\["basic", "advanced"], optional): The depth of the search. Defaults to `"basic"`.
* `topic` (Literal\["general", "news", "finance"], optional): The topic to focus the search on. Defaults to `"general"`.
* `time_range` (Literal\["day", "week", "month", "year"], optional): The time range for the search. Defaults to `None`.
* `days` (int, optional): The number of days to search back. Relevant if `time_range` is not set. Defaults to `7`.
* `max_results` (int, optional): The maximum number of search results to return. Defaults to `5`.
* `include_domains` (Sequence\[str], optional): A list of domains to prioritize in the search. Defaults to `None`.
* `exclude_domains` (Sequence\[str], optional): A list of domains to exclude from the search. Defaults to `None`.
* `include_answer` (Union\[bool, Literal\["basic", "advanced"]], optional): Whether to include a direct answer synthesized from the search results. Defaults to `False`.
* `include_raw_content` (bool, optional): Whether to include the raw HTML content of the searched pages. Defaults to `False`.
* `include_images` (bool, optional): Whether to include image results. Defaults to `False`.
* `timeout` (int, optional): The request timeout in seconds. Defaults to `60`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Form the crew and kick it off](./1175-form-the-crew-and-kick-it-off.md)

**Next:** [Advanced Usage →](./1177-advanced-usage.md)
