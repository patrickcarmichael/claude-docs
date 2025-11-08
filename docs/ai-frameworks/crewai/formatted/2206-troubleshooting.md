---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


### Common Issues

* **No traces appearing**: Ensure your API key and repository ID are correct
* Ensure you've **`called instrument_crewai()`** ***before*** running your crew. This initializes logging hooks correctly.
* Set `debug=True` in your `instrument_crewai()` call to surface any internal errors:

  ```python  theme={null}
  instrument_crewai(logger, debug=True)
  ```
* Configure your agents with `verbose=True` to capture detailed logs:

  ```python  theme={null}
  agent = CrewAgent(..., verbose=True)
  ```
* Double-check that `instrument_crewai()` is called **before** creating or executing agents. This might be obvious, but it's a common oversight.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Viewing Your Traces](./2205-viewing-your-traces.md)

**Next:** [Resources →](./2207-resources.md)
