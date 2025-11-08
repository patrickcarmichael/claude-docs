---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Import packages

from datetime import datetime
from io import IOBase
from typing import List, Optional, Union
import pandas as pd
from pydantic import BaseModel, Field

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
)
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_core.tools import Tool, BaseTool
from langchain_core.prompts.chat import (
    BaseMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain_experimental.tools.python.tool import PythonAstREPLTool
from langchain_cohere.chat_models import ChatCohere
```
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
