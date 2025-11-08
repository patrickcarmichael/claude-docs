---
title: "Crewai: Testing Your Custom LLM"
description: "Testing Your Custom LLM section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Testing Your Custom LLM


```python  theme={null}
from crewai import Agent, Task, Crew

def test_custom_llm():
    llm = CustomLLM(
        model="test-model",
        api_key="test-key",
        endpoint="https://api.test.com"
    )
    
    # Test basic call
    result = llm.call("Hello, world!")
    assert isinstance(result, str)
    assert len(result) > 0
    
    # Test with CrewAI agent
    agent = Agent(
        role="Test Agent",
        goal="Test custom LLM",
        backstory="A test agent.",
        llm=llm
    )
    
    task = Task(
        description="Say hello",
        expected_output="A greeting",
        agent=agent
    )
    
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    assert "hello" in result.raw.lower()
```

This guide covers the essentials of implementing custom LLMs in CrewAI.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ✅ Correct](./2001-correct.md)

**Next:** [Custom Manager Agent →](./2003-custom-manager-agent.md)
