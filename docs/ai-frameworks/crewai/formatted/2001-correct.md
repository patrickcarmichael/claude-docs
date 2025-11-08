---
title: "Crewai: ✅ Correct"
description: "✅ Correct section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# ✅ Correct

def __init__(self, model: str, api_key: str, temperature: Optional[float] = None):
    super().__init__(model=model, temperature=temperature)
```

**Function Calling Not Working**

* Ensure `supports_function_calling()` returns `True`
* Check that you handle `tool_calls` in the response
* Verify `available_functions` parameter is used correctly

**Authentication Failures**

* Verify API key format and permissions
* Check authentication header format
* Ensure endpoint URLs are correct

**Response Parsing Errors**

* Validate response structure before accessing nested fields
* Handle cases where content might be None
* Add proper error handling for malformed responses

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← ❌ Wrong - missing required parameters](./2000-wrong-missing-required-parameters.md)

**Next:** [Testing Your Custom LLM →](./2002-testing-your-custom-llm.md)
