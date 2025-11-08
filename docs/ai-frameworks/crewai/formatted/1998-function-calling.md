---
title: "Crewai: Function Calling"
description: "Function Calling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Function Calling


If your LLM supports function calling, implement the complete flow:

```python  theme={null}
import json

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    # Convert string to message format
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    
    # Make API call
    response = self._make_api_call(messages, tools)
    message = response["choices"][0]["message"]
    
    # Check for function calls
    if "tool_calls" in message and available_functions:
        return self._handle_function_calls(
            message["tool_calls"], messages, tools, available_functions
        )
    
    return message["content"]

def _handle_function_calls(self, tool_calls, messages, tools, available_functions):
    """Handle function calling with proper message flow."""
    for tool_call in tool_calls:
        function_name = tool_call["function"]["name"]
        
        if function_name in available_functions:
            # Parse and execute function
            function_args = json.loads(tool_call["function"]["arguments"])
            function_result = available_functions[function_name](**function_args)
            
            # Add function call and result to message history
            messages.append({
                "role": "assistant",
                "content": None,
                "tool_calls": [tool_call]
            })
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "name": function_name,
                "content": str(function_result)
            })
            
            # Call LLM again with updated context
            return self.call(messages, tools, None, available_functions)
    
    return "Function call failed"
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Common Patterns](./1997-common-patterns.md)

**Next:** [Troubleshooting →](./1999-troubleshooting.md)
