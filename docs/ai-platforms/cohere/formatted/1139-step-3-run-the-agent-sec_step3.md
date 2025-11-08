---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 3: Run the Agent \[#sec\_step3]

Let's now test the Agent we just defined!
```python PYTHON
query_1 = "Look for urn:75f2b737-06dd-4399-9206-a6c11b65138e, GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE"
response_1 = agent_executor.invoke(
            {
                "input": query_1,
                "preamble": preamble,
            }
        )
```
````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the codes from the user query.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'Look for urn:75f2b737-06dd-4399-9206-a6c11b65138e, GLCMS004AGTCAMIS; 0000234GLCMS0100ANORAKCAA, GLCHL000CGUCHALE'}}
[0m[36;1m[1;3m{'nmgs': ['0000234GLCMS0100ANORAKCAA'], 'objref': ['GLCMS004AGTCAMIS', 'GLCHL000CGUCHALE'], 'urn': ['urn:75f2b737-06dd-4399-9206-a6c11b65138e']}[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: ```json JSON
[
    {
        "urn": ["urn:75f2b737-06dd-4399-9206-a6c11b65138e"],
        "objref": ["GLCMS004AGTCAMIS", "GLCHL000CGUCHALE"],
        "nmgs": ["0000234GLCMS0100ANORAKCAA"]
    }
]
```
Grounded answer: ```json JSON
  [
    {
        "urn": [<co: 0>"urn:75f2b737-06dd-4399-9206-a6c11b65138e</co: 0>"],
        "objref": [<co: 0>"GLCMS004AGTCAMIS</co: 0>", <co: 0>"GLCHL000CGUCHALE</co: 0>"],
        "nmgs": [<co: 0>"0000234GLCMS0100ANORAKCAA</co: 0>"]
    }
]
```[0m

[1m> Finished chain.[0m
````
In the reasoning chain above, we can see that the Agent uses the tool we provided it to extract the strings in the query.
The output of the tool is then used to generate the request.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
