---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Specify the desired output format

Precisely define your desired output format using JSON, XML, or custom templates so that Claude understands every output formatting element you require.

<Accordion title="Example: Standardizing customer feedback">
  | Role      | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User      | You're a Customer Insights AI. Analyze this feedback and output in JSON format with keys: "sentiment" (positive/negative/neutral), "key\_issues" (list), and "action\_items" (list of dicts with "team" and "task").<br /><br />"I've been a loyal user for 3 years, but the recent UI update is a disaster. Finding basic features is now a scavenger hunt. Plus, the new 'premium' pricing is outrageous. I'm considering switching unless this is fixed ASAP."                                                                                                                                                                                                                                                                                                                                                |
  | Assistant | \{<br />  "sentiment": "negative",<br />  "key\_issues": \[<br />    "Poor UI/UX in recent update",<br />    "Difficulty finding basic features",<br />    "Perceived high pricing (new 'premium' tier)"<br />  ],<br />  "action\_items": \[<br />    \{<br />      "team": "Product",<br />      "task": "Conduct usability testing and iterate on UI based on findings"<br />    },<br />    \{<br />      "team": "UX",<br />      "task": "Create a feature discovery guide or onboarding flow"<br />    },<br />    \{<br />      "team": "Marketing",<br />      "task": "Review pricing strategy and communicate value proposition"<br />    },<br />    \{<br />      "team": "Customer Success",<br />      "task": "Reach out to user, offer concessions to prevent churn"<br />    }<br />  ]<br />} |
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
