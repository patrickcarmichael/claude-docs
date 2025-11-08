---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Result

| Type                   | Question                                                  | Simple Rag                                                                                                                                                                                       | Agentic Rag                                                                                                                  |
| ---------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Single-stage retrieval | Is there a state level law for wearing helmets?           | There is currently no state law requiring the use of helmets when riding a bicycle. However, some cities and counties do require helmet use.                                                     | There is currently no state law requiring helmet use. However, some cities and counties do require helmet use with bicycles. |
| Multi-stage retrieval  | I live in orting, do I need to wear a helmet with a bike? | In the state of Washington, there is no law requiring you to wear a helmet when riding a bike. However, some cities and counties do require helmet use, so it is worth checking your local laws. | Yes, you do need to wear a helmet with a bike in Orting if you are under 17.                                                 |

As you will see more below, the multi-stage retrieval is achieved by adding a new function `reference_extractor()` that extracts other references in the documents and updating the instruction so the agent continues to retrieve more documents.
```python PYTHON
import os
from pprint import pprint

import cohere
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
