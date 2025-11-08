---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

**Video doesn't match prompt well:**

* Increase `guidance_scale` to 8-10
* Make prompt more descriptive and specific
* Add `negative_prompt` to exclude unwanted elements

**Video has artifacts:**

* Reduce `guidance_scale` (keep below 12)
* Increase `steps` to 30-40
* Adjust `fps` if motion looks unnatural

**Generation is too slow:**

* Reduce `steps` (try 10-20 for testing)
* Use shorter `seconds` during development
* Lower `fps` for slower-paced scenes

**URLs expire:**

* Download videos immediately after completion
* Don't rely on URLs for long-term storage


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
