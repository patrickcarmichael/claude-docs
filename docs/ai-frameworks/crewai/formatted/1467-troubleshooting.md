---
title: "Crewai: Troubleshooting"
description: "Troubleshooting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Troubleshooting


<Accordion title="Validation Always Fails">
  **Possible Causes:**

  * Context is too restrictive or unrelated to task output
  * Threshold is set too high for the content type
  * Reference context contains outdated information

  **Solutions:**

  * Review and update context to match task requirements
  * Lower threshold or use default verdict-based validation
  * Ensure context is current and accurate
</Accordion>

<Accordion title="False Positives (Valid Content Marked Invalid)">
  **Possible Causes:**

  * Threshold too high for creative or interpretive tasks
  * Context doesn't cover all valid aspects of the output
  * Evaluation model being overly conservative

  **Solutions:**

  * Lower threshold or use default validation
  * Expand context to include broader acceptable content
  * Test with different evaluation models
</Accordion>

<Accordion title="Evaluation Errors">
  **Possible Causes:**

  * Network connectivity issues
  * LLM model unavailable or rate limited
  * Malformed task output or context

  **Solutions:**

  * Check network connectivity and LLM service status
  * Implement retry logic for transient failures
  * Validate task output format before guardrail evaluation
</Accordion>

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with hallucination guardrail configuration or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Performance Considerations](./1466-performance-considerations.md)

**Next:** [Marketplace →](./1468-marketplace.md)
