---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Define the Tool and the Agent \[#sec\_step2]

Here we create a tool which implements the deterministic function to extract alphanumeric strings
from the user's query and match them to the right parameter.
```python PYTHON
@tool
def regex_extractor(user_query: str) -> dict:
    """Function which, given the query from the user, returns a dictionary parameter:value."""
    uuid = re.findall("\s([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})", user_query)
    nmgs = re.findall("(0000[A-Z0-9]{21})", user_query)
    objref = re.findall("\s([A-Z]{5,9}\d{3,4}[A-Z]{3,8})", user_query)
    urn = re.findall("urn:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",user_query,)
    d = {"uuid": uuid,
         "nmgs": nmgs,
         "objref": objref,
         "urn": urn}
    d_filtered = {k: v for k, v in d.items() if v != []}
    return d_filtered

class extract_code_v1productssearch(BaseModel):
    user_query: str = Field(
        description="This is the full input query as received from the user. Do not truncate or modify the query in any way."
    )
regex_extractor.name = "regex_extractor"
regex_extractor.args_schema = extract_code_v1productssearch
tools=[regex_extractor]
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
