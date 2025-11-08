---
title: "Crewai: Define templates for system, user (prompt), and assistant (response) messages"
description: "Define templates for system, user (prompt), and assistant (response) messages section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define templates for system, user (prompt), and assistant (response) messages

system_template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>{{ .System }}<|eot_id|>"""
prompt_template = """<|start_header_id|>user<|end_header_id|>{{ .Prompt }}<|eot_id|>"""
response_template = """<|start_header_id|>assistant<|end_header_id|>{{ .Response }}<|eot_id|>"""

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Optimizing for Specific Models](./369-optimizing-for-specific-models.md)

**Next:** [Create an Agent using Llama-specific layouts →](./371-create-an-agent-using-llama-specific-layouts.md)
