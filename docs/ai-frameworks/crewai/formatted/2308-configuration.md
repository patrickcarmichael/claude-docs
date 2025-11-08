---
title: "Crewai: Configuration"
description: "Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Configuration


The `ApifyActorsTool` requires these inputs to work:

* **`actor_name`**
  The ID of the Apify Actor to run, e.g., `"apify/rag-web-browser"`. Browse all Actors on [Apify Store](https://apify.com/store).
* **`run_input`**
  A dictionary of input parameters for the Actor when running the tool manually.
  * For example, for the `apify/rag-web-browser` Actor: `{"query": "search term", "maxResults": 5}`
  * See the Actor's [input schema](https://apify.com/apify/rag-web-browser/input-schema) for the list of input parameters.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Process the results](./2307-process-the-results.md)

**Next:** [Resources →](./2309-resources.md)
