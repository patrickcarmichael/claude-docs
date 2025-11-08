---
title: "Crewai: Common Patterns"
description: "Common Patterns section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Common Patterns


### Error Handling

```python  theme={null}
import requests

def call(self, messages, tools=None, callbacks=None, available_functions=None):
    try:
        response = requests.post(
            self.endpoint,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
        
    except requests.Timeout:
        raise TimeoutError("LLM request timed out")
    except requests.RequestException as e:
        raise RuntimeError(f"LLM request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Invalid response format: {str(e)}")
```

### Custom Authentication

```python  theme={null}
from crewai import BaseLLM
from typing import Optional

class CustomAuthLLM(BaseLLM):
    def __init__(self, model: str, auth_token: str, endpoint: str, temperature: Optional[float] = None):
        super().__init__(model=model, temperature=temperature)
        self.auth_token = auth_token
        self.endpoint = endpoint
    
    def call(self, messages, tools=None, callbacks=None, available_functions=None):
        headers = {
            "Authorization": f"Custom {self.auth_token}",  # Custom auth format
            "Content-Type": "application/json"
        }
        # Rest of implementation...
```

### Stop Words Support

CrewAI automatically adds `"\nObservation:"` as a stop word to control agent behavior. If your LLM supports stop words:

```python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    payload = {
        "model": self.model,
        "messages": messages,
        "stop": self.stop  # Include stop words in API call
    }
    # Make API call...

def supports_stop_words(self) -> bool:
    return True  # Your LLM supports stop sequences
```

If your LLM doesn't support stop words natively:

```python  theme={null}
def call(self, messages, tools=None, callbacks=None, available_functions=None):
    response = self._make_api_call(messages, tools)
    content = response["choices"][0]["message"]["content"]
    
    # Manually truncate at stop words
    if self.stop:
        for stop_word in self.stop:
            if stop_word in content:
                content = content.split(stop_word)[0]
                break
    
    return content

def supports_stop_words(self) -> bool:
    return False  # Tell CrewAI we handle stop words manually
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Required Methods](./1996-required-methods.md)

**Next:** [Function Calling →](./1998-function-calling.md)
