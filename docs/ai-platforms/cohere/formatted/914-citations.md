---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Citations

* Citations access:
  * v1: `citations`
  * v2: `message.citations`
* Cited tools access:
  * v1: `documents`
  * v2: as part of `message.citations`, in the `sources` field

**v1**
```python PYTHON
print(res_v1.citations)
print(res_v1.documents)
```
```
[ChatCitation(start=16, end=20, text='20°C', document_ids=['get_weather:0:2:0'])]

[{'id': 'get_weather:0:2:0', 'temperature': '20C', 'tool_name': 'get_weather'}]
```
**v2**
```python PYTHON
print(res_v2.message.citations)
```
```
[Citation(start=5, end=9, text='20°C', sources=[ToolSource(type='tool', id='get_weather_k88p0m8504w5:0', tool_output={'temperature': '20C'})])]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
