---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Imports

from reward_kit import reward_function, EvaluateResult, MetricResult
from typing import List, Dict, Optional
from fireworks import LLM
from rouge_score import rouge_scorer
import math, torch
import os

FIREWORKS_API_KEY = os.getenv("FIREWORKS_API_KEY")

from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
