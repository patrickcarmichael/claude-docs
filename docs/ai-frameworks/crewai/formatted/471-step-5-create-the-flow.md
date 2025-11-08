---
title: "Crewai: Step 5: Create the Flow"
description: "Step 5: Create the Flow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Step 5: Create the Flow


Now comes the exciting part - creating the flow that will orchestrate the entire guide creation process. This is where we'll combine regular Python code, direct LLM calls, and our content creation crew into a cohesive system.

Our flow will:

1. Get user input for a topic and audience level
2. Make a direct LLM call to create a structured guide outline
3. Process each section sequentially using the content writer crew
4. Combine everything into a final comprehensive document

Let's create our flow in the `main.py` file:

```python  theme={null}
#!/usr/bin/env python
import json
import os
from typing import List, Dict
from pydantic import BaseModel, Field
from crewai import LLM
from crewai.flow.flow import Flow, listen, start
from guide_creator_flow.crews.content_crew.content_crew import ContentCrew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← src/guide_creator_flow/crews/content_crew/content_crew.py](./470-srcguide_creator_flowcrewscontent_crewcontent_crew.md)

**Next:** [Define our models for structured data →](./472-define-our-models-for-structured-data.md)
