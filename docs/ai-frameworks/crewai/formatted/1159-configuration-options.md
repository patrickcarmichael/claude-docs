---
title: "Crewai: Configuration Options"
description: "Configuration Options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration Options


The `TavilyExtractorTool` accepts the following arguments:

* `urls` (Union\[List\[str], str]): **Required**. A single URL string or a list of URL strings to extract data from.
* `include_images` (Optional\[bool]): Whether to include images in the extraction results. Defaults to `False`.
* `extract_depth` (Literal\["basic", "advanced"]): The depth of extraction. Use `"basic"` for faster, surface-level extraction or `"advanced"` for more comprehensive extraction. Defaults to `"basic"`.
* `timeout` (int): The maximum time in seconds to wait for the extraction request to complete. Defaults to `60`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create and run the crew](./1158-create-and-run-the-crew.md)

**Next:** [Advanced Usage →](./1160-advanced-usage.md)
