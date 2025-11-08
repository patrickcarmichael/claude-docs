---
title: "Crewai: Define your own system template without default instructions"
description: "Define your own system template without default instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define your own system template without default instructions

custom_system_template = """You are {role}. {backstory}
Your goal is: {goal}

Respond naturally and conversationally. Focus on providing helpful, accurate information."""

custom_prompt_template = """Task: {input}

Please complete this task thoughtfully."""

agent = Agent(
    role="Research Assistant",
    goal="Help users find accurate information",
    backstory="You are a helpful research assistant.",
    system_template=custom_system_template,
    prompt_template=custom_prompt_template,
    use_system_prompt=True  # Use separate system/user messages
)
```

#### Option 2: Custom Prompt File

Create a `custom_prompts.json` file to override specific prompt slices:

```json  theme={null}
{
  "slices": {
    "no_tools": "\nProvide your best answer in a natural, conversational way.",
    "tools": "\nYou have access to these tools: {tools}\n\nUse them when helpful, but respond naturally.",
    "formatted_task_instructions": "Format your response as: {output_format}"
  }
}
```

Then use it in your crew:

```python  theme={null}
crew = Crew(
    agents=[agent],
    tasks=[task],
    prompt_file="custom_prompts.json",
    verbose=True
)
```

#### Option 3: Disable System Prompts for o1 Models

```python  theme={null}
agent = Agent(
    role="Analyst",
    goal="Analyze data",
    backstory="Expert analyst",
    use_system_prompt=False  # Disables system prompt separation
)
```

### Debugging with Observability Tools

For production transparency, integrate with observability platforms to monitor all prompts and LLM interactions. This allows you to see exactly what prompts (including default instructions) are being sent to your LLMs.

See our [Observability documentation](/en/observability/overview) for detailed integration guides with various platforms including Langfuse, MLflow, Weights & Biases, and custom logging solutions.

### Best Practices for Production

1. **Always inspect generated prompts** before deploying to production
2. **Use custom templates** when you need full control over prompt content
3. **Integrate observability tools** for ongoing prompt monitoring (see [Observability docs](/en/observability/overview))
4. **Test with different LLMs** as default instructions may work differently across models
5. **Document your prompt customizations** for team transparency

<Tip>
  The default instructions exist to ensure consistent agent behavior, but they can interfere with domain-specific requirements. Use the customization options above to maintain full control over your agent's behavior in production systems.
</Tip>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← You can also see how the task description gets formatted](./362-you-can-also-see-how-the-task-description-gets-for.md)

**Next:** [Best Practices for Managing Prompt Files →](./364-best-practices-for-managing-prompt-files.md)
