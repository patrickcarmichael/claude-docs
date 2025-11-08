---
title: "Crewai: Important Considerations and Best Practices"
description: "Important Considerations and Best Practices section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Important Considerations and Best Practices


### Security and Code Execution

* When using `allow_code_execution`, be cautious with user input and always validate it
* Use `code_execution_mode: "safe"` (Docker) in production environments
* Consider setting appropriate `max_execution_time` limits to prevent infinite loops

### Performance Optimization

* Use `respect_context_window: true` to prevent token limit issues
* Set appropriate `max_rpm` to avoid rate limiting
* Enable `cache: true` to improve performance for repetitive tasks
* Adjust `max_iter` and `max_retry_limit` based on task complexity

### Memory and Context Management

* Leverage `knowledge_sources` for domain-specific information
* Configure `embedder` when using custom embedding models
* Use custom templates (`system_template`, `prompt_template`, `response_template`) for fine-grained control over agent behavior

### Advanced Features

* Enable `reasoning: true` for agents that need to plan and reflect before executing complex tasks
* Set appropriate `max_reasoning_attempts` to control planning iterations (None for unlimited attempts)
* Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
* Customize the date format with `date_format` using standard Python datetime format codes
* Enable `multimodal: true` for agents that need to process both text and visual content

### Agent Collaboration

* Enable `allow_delegation: true` when agents need to work together
* Use `step_callback` to monitor and log agent interactions
* Consider using different LLMs for different purposes:
  * Main `llm` for complex reasoning
  * `function_calling_llm` for efficient tool usage

### Date Awareness and Reasoning

* Use `inject_date: true` to provide agents with current date awareness for time-sensitive tasks
* Customize the date format with `date_format` using standard Python datetime format codes
* Valid format codes include: %Y (year), %m (month), %d (day), %B (full month name), etc.
* Invalid date formats will be logged as warnings and will not modify the task description
* Enable `reasoning: true` for complex tasks that benefit from upfront planning and reflection

### Model Compatibility

* Set `use_system_prompt: false` for older models that don't support system messages
* Ensure your chosen `llm` supports the features you need (like function calling)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Access structured data](./27-access-structured-data.md)

**Next:** [Troubleshooting Common Issues →](./29-troubleshooting-common-issues.md)
