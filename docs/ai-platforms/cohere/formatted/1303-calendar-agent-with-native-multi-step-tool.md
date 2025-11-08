---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Calendar Agent with Native Multi Step Tool

> This page describes how to use cohere Chat API with list_calendar_events and create_calendar_event tools to book appointments.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Tool_Use.ipynb" />

In the example below, we demonstrate how to use the cohere Chat API with the `list_calendar_events` and `create_calendar_event` tools to book appointments. Booking the correct appointment requires the model to first check for an available slot by listing existing events, reasoning about the correct slot to book the new appointment and then finally invoking the right tool to create the calendar event. To learn more about Tool Use, read the official [multi-step tool use guide](https://docs.cohere.com/docs/multi-step-tool-use).
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
