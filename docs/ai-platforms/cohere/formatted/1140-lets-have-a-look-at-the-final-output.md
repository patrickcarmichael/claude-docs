---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## let's have a look at the final output

convert_to_json(response_1['output'])
```
```python title="Output"
[{'urn': ['urn:75f2b737-06dd-4399-9206-a6c11b65138e'],
  'objref': ['GLCMS004AGTCAMIS', 'GLCHL000CGUCHALE'],
  'nmgs': ['0000234GLCMS0100ANORAKCAA']}]
```
As mentioned above, the Agent can use the tool when specific alphanumeric patterns have to be extracted from the query; however, it can also generate the output based on its semantic understanding of the query. For example:
```python PYTHON
query_2 = "I need tennis products"

response_2 = agent_executor.invoke(
    {
        "input": query_2,
        "preamble": preamble,
    }
)
```
````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the relevant information from the user request.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'I need tennis products'}}
[0m[36;1m[1;3m{}[0m[32;1m[1;3mRelevant Documents: None
Cited Documents: None
Answer: ```json JSON
[
    {
        "taxonomies": [
            "SPORT"
        ]
    }
]
```
Grounded answer: ```json JSON
  [
  {
  "taxonomies": [
  "SPORT"
  ]
  }
]
```[0m

[1m> Finished chain.[0m
````
The Agent runs the tool to check if any target string was in the query, then it generated the request body based on its understanding.
```python PYTHON
convert_to_json(response_2['output'])
```
```python title="Output"
[{'taxonomies': ['SPORT']}]
```
Finally, the two paths to generation - deterministic and semantic - can be applied in parallel by the Agent, as shown below:
```python PYTHON
query_3 = "Look for GLBRL0000GACHALE, nmg 0000234GLCZD0000GUREDTOAA and car products"

response_3 = agent_executor.invoke(
    {
        "input": query_3,
        "preamble": preamble,
    }
)
```
````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3m
I will use the regex_extractor tool to extract the codes from the user query. Then, I will create a JSON for each of the key-value pairs in the dictionary.
{'tool_name': 'regex_extractor', 'parameters': {'user_query': 'Look for GLBRL0000GACHALE, nmg 0000234GLCZD0000GUREDTOAA and car products'}}
[0m[36;1m[1;3m{'nmgs': ['0000234GLCZD0000GUREDTOAA'], 'objref': ['GLBRL0000GACHALE']}[0m[32;1m[1;3mRelevant Documents: 0
Cited Documents: 0
Answer: ```json JSON
[
    {
        "objref": ["GLBRL0000GACHALE"],
        "nmgs": ["0000234GLCZD0000GUREDTOAA"]
    },
    {
        "taxonomies": ["CARS"]
    }
]
```
Grounded answer: ```json JSON
  [
    {
        "objref": [<co: 0>"GLBRL0000GACHALE</co: 0>"],
        "nmgs": [<co: 0>"0000234GLCZD0000GUREDTOAA</co: 0>"]
    },
    {
        "taxonomies": ["CARS"]
    }
]
```[0m

[1m> Finished chain.[0m
````
```python PYTHON
convert_to_json(response_3['output'])
```
```python title="Output"
[{'objref': ['GLBRL0000GACHALE'], 'nmgs': ['0000234GLCZD0000GUREDTOAA']},
  {'taxonomies': ['CARS']}]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
