---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cell to evaluate OpenAI and Anthropic models (with manual logging) - GPT-4o and Claude Sonnet 4

import openai
import anthropic
import os
import requests
import json
import time
import re
from tqdm.auto import tqdm
from dotenv import load_dotenv

load_dotenv()

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
