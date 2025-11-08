---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic hallucination minimization strategies

* **Allow Claude to say "I don't know":** Explicitly give Claude permission to admit uncertainty. This simple technique can drastically reduce false information.

<Accordion title="Example: Analyzing a merger & acquisition report">
  | Role | Content                                                                                                                                                                                                                                                                                                                                                                                        |
  | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User | As our M\&A advisor, analyze this report on the potential acquisition of AcmeCo by ExampleCorp.<br /><br />\<report><br />\{\{REPORT}}<br />\</report><br /><br />Focus on financial projections, integration risks, and regulatory hurdles. If you're unsure about any aspect or if the report lacks necessary information, say "I don't have enough information to confidently assess this." |
</Accordion>

* **Use direct quotes for factual grounding:** For tasks involving long documents (>20K tokens), ask Claude to extract word-for-word quotes first before performing its task. This grounds its responses in the actual text, reducing hallucinations.

<Accordion title="Example: Auditing a data privacy policy">
  | Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User | As our Data Protection Officer, review this updated privacy policy for GDPR and CCPA compliance.<br />\<policy><br />\{\{POLICY}}<br />\</policy><br /><br />1. Extract exact quotes from the policy that are most relevant to GDPR and CCPA compliance. If you can't find relevant quotes, state "No relevant quotes found."<br /><br />2. Use the quotes to analyze the compliance of these policy sections, referencing the quotes by number. Only base your analysis on the extracted quotes. |
</Accordion>

* **Verify with citations**: Make Claude's response auditable by having it cite quotes and sources for each of its claims. You can also have Claude verify each claim by finding a supporting quote after it generates a response. If it can't find a quote, it must retract the claim.

<Accordion title="Example: Drafting a press release on a product launch">
  | Role | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | User | Draft a press release for our new cybersecurity product, AcmeSecurity Pro, using only information from these product briefs and market reports.<br />\<documents><br />\{\{DOCUMENTS}}<br />\</documents><br /><br />After drafting, review each claim in your press release. For each claim, find a direct quote from the documents that supports it. If you can't find a supporting quote for a claim, remove that claim from the press release and mark where it was removed with empty \[] brackets. |
</Accordion>

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
