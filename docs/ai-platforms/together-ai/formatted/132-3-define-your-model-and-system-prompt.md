---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 3. Define your model and system prompt

In the following code snippet, we'll define our API keys, our model of choice, and our system prompt.

You can pick the model of your choice by uncommenting it. There are some recommended models that are great at code generation, but you can add a different one from [here](/docs/serverless-models#chat-models).

For the system prompt, we tell the model it's a data scientist and give it some information about the uploaded CSV. You can choose different data but will need to update the instructions accordingly.
````py
from dotenv import load_dotenv
import os
import json
import re
from together import Together
from e2b_code_interpreter import CodeInterpreter

load_dotenv()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
