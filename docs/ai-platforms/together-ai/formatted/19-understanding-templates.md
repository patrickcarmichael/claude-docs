---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Understanding Templates

Templates are used throughout the Evaluations API to dynamically inject data from your dataset into prompts. Both `system_template` and `input_template` parameters support Jinja2 templating syntax.

[Jinja2](https://datascience.fm/creating-dynamic-prompts-with-jinja2-for-llm-queries/) templates allow you to inject columns from the dataset into the `system_template` or `input_template` for either the judge or the generation model.

### Examples

* You can specify a reference answer for the judge:
  * `"Please use the reference answer: {{reference_answer_column_name}}"`
* You can provide a separate instruction for generation for each example:
  * `"Please use the following guidelines: {{guidelines_column_name}}"`
* You can specify any column(s) as input for the model being evaluated:
  * `"Continue: {{prompt_column_name}}"`
* You can also reference nested fields from your JSON input:
  * `"{{column_name.field_name}}"`
* And many more options are supported.

### Basic Example

If your dataset contains:
```json
{ "prompt": "What is the capital of France?" }
```

And you set:
```python
input_template = "Please answer the following question: {{prompt}}"
```

The final input becomes:
```text
Please answer the following question: What is the capital of France?
```

### Nested Data Example

For complex structures:
```json
{ "info": { "question": "What is the capital of France?", "answer": "Paris" } }
```

You can access nested fields:
```python
input_template = "Please answer: {{info.question}}"
```

For more Jinja2 functionality, see:

* [Interactive Playground](https://huggingface.co/spaces/huggingfacejs/chat-template-playground)
* [Hugging Face Guide](https://huggingface.co/blog/chat-templates)
* [Jinja2 Documentation](https://www.devdoc.net/python/jinja-2.10.1-doc/)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
