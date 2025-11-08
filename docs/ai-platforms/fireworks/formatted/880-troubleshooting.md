---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Troubleshooting

<AccordionGroup>
  <Accordion title="Model isn't calling tools when expected">
    * Check that your tool descriptions are clear and detailed
    * Ensure the user query clearly indicates a need for the tool
    * Try using `tool_choice="required"` to force tool usage
    * Verify your model supports tool calling (check `supportsTools` field)
  </Accordion>

  <Accordion title="Tool arguments are incorrect or malformed">
    * Add more detailed parameter descriptions
    * Use lower temperature (0.0-0.3) for more deterministic outputs
    * Provide examples in parameter descriptions
    * Use `enum` to constrain values to specific options
  </Accordion>

  <Accordion title="Getting JSON parsing errors">
    * Always validate tool call arguments before parsing
    * Handle partial or malformed JSON gracefully in production
    * Use try-catch blocks when parsing `tool_call.function.arguments`
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
