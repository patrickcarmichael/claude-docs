---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define Dialogue Schema with Pydantic

We need a way of telling the LLM what the structure of the podcast script between the guest and host will look like. We will do this using `pydantic` models.

Below we define the required classes:

* The overall conversation consists of lines said by either the host or the guest. The `DialogueItem` class specifies the structure of these lines.
* The full script is a combination of multiple lines performed by the speakers, here we also include a `scratchpad` field to allow the LLM to ideate and brainstorm the overall flow of the script prior to actually generating the lines. The `Dialogue` class specifies this.
```py
from pydantic import BaseModel
from typing import List, Literal, Tuple, Optional


class LineItem(BaseModel):
    """A single line in the script."""

    speaker: Literal["Host (Jane)", "Guest"]
    text: str


class Script(BaseModel):
    """The script between the host and guest."""

    scratchpad: str
    name_of_guest: str
    script: List[LineItem]
```

The inclusion of a scratchpad field is very important - it allows the LLM compute and tokens to generate an unstructured overview of the script prior to generating a structured line by line enactment.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
