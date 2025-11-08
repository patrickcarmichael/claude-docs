---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Overview

>   **📝 Note**
>
> For a deep dive into the architecture and real-world applications of Agent Skills, read our engineering blog: [Equipping agents for the real world with Agent Skills](https://https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills-skills).

Skills integrate with the Messages API through the code execution tool. Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical—both require code execution and use the same `container` structure.

### Using Skills

Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.

**You can use Skills from two sources:**

| Aspect             | Anthropic Skills                           | Custom Skills                                                   |
| ------------------ | ------------------------------------------ | --------------------------------------------------------------- |
| **Type value**     | `anthropic`                                | `custom`                                                        |
| **Skill IDs**      | Short names: `pptx`, `xlsx`, `docx`, `pdf` | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`                     |
| **Version format** | Date-based: `20251013` or `latest`         | Epoch timestamp: `1759178010641129` or `latest`                 |
| **Management**     | Pre-built and maintained by Anthropic      | Upload and manage via [Skills API](/en/api/skills/create-skill) |
| **Availability**   | Available to all users                     | Private to your workspace                                       |

Both skill sources are returned by the [List Skills endpoint](/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical—the only difference is where the Skills come from and how they're managed.

### Prerequisites

To use Skills, you need:

1. **Anthropic API key** from the [Console](https://console.anthropic.com/settings/keys)
2. **Beta headers**:
   * `code-execution-2025-08-25` - Enables code execution (required for Skills)
   * `skills-2025-10-02` - Enables Skills API
   * `files-api-2025-04-14` - For uploading/downloading files to/from container
3. **Code execution tool** enabled in your requests

***

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
