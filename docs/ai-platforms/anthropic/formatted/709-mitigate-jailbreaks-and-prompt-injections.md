---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Mitigate jailbreaks and prompt injections

Source: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks


Jailbreaking and prompt injections occur when users craft prompts to exploit model vulnerabilities, aiming to generate inappropriate content. While Claude is inherently resilient to such attacks, here are additional steps to strengthen your guardrails, particularly against uses that either violate our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) or [Usage Policy](https://www.anthropic.com/legal/aup).

<Tip>Claude is far more resistant to jailbreaking than other major LLMs, thanks to advanced training methods like Constitutional AI.</Tip>

* **Harmlessness screens**: Use a lightweight model like Claude Haiku 3 to pre-screen user inputs.

  <Accordion title="Example: Harmlessness screen for content moderation">
    | Role                | Content                                                                                                                                                                                             |
    | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | User                | A user submitted this content:<br />\<content><br />\{\{CONTENT}}<br />\</content><br /><br />Reply with (Y) if it refers to harmful, illegal, or explicit activities. Reply with (N) if it's safe. |
    | Assistant (prefill) | (                                                                                                                                                                                                   |
    | Assistant           | N)                                                                                                                                                                                                  |
  </Accordion>

* **Input validation**: Filter prompts for jailbreaking patterns. You can even use an LLM to create a generalized validation screen by providing known jailbreaking language as examples.

* **Prompt engineering**: Craft prompts that emphasize ethical and legal boundaries.

  <Accordion title="Example: Ethical system prompt for an enterprise chatbot">
    | Role   | Content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
    | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | System | You are AcmeCorp's ethical AI assistant. Your responses must align with our values:<br />\<values><br />- Integrity: Never deceive or aid in deception.<br />- Compliance: Refuse any request that violates laws or our policies.<br />- Privacy: Protect all personal and corporate data.<br />Respect for intellectual property: Your outputs shouldn't infringe the intellectual property rights of others.<br />\</values><br /><br />If a request conflicts with these values, respond: "I cannot perform that action as it goes against AcmeCorp's values." |
  </Accordion>

Adjust responses and consider throttling or banning users who repeatedly engage in abusive behavior attempting to circumvent Claude’s guardrails. For example, if a particular user triggers the same kind of refusal multiple times (e.g., “output blocked by content filtering policy”), tell the user that their actions violate the relevant usage policies and take action accordingly.

* **Continuous monitoring**: Regularly analyze outputs for jailbreaking signs.
  Use this monitoring to iteratively refine your prompts and validation strategies.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
