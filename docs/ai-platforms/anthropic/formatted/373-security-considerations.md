---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Security considerations

>   **⚠️ Warning**
>
> Computer use is a beta feature with unique risks distinct from standard API features. These risks are heightened when interacting with the internet. To minimize risks, consider taking precautions such as:

  1. Use a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
  2. Avoid giving the model access to sensitive data, such as account login information, to prevent information theft.
  3. Limit internet access to an allowlist of domains to reduce exposure to malicious content.
  4. Ask a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service.

  In some circumstances, Claude will follow commands found in content even if it conflicts with the user's instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. We suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

  We've trained the model to resist these prompt injections and have added an extra layer of defense. If you use our computer use tools, we'll automatically run classifiers on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. We recognize that this extra protection won't be ideal for every use case (for example, use cases without a human in the loop), so if you'd like to opt out and turn it off, please [contact us](https://support.claude.com/en/).

  We still suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

  Finally, please inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.

<Card title="Computer use reference implementation" icon="computer" href="https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo">
  Get started quickly with our computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop.

  **Note:** The implementation has been updated to include new tools for both Claude 4 models and Claude Sonnet 3.7. Be sure to pull the latest version of the repo to access these new features.
</Card>

<Tip>
  Please use [this form](https://forms.gle/BT1hpBrqDPDUrCqo7) to provide
  feedback on the quality of the model responses, the API itself, or the quality
  of the documentation - we cannot wait to hear from you!
</Tip>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
