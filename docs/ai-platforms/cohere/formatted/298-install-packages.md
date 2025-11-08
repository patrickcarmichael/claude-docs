---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Install Packages:

Install and import the required Python Packages:

* `jsonlines`: for this example, the sample passages live in a `jsonl` file, and we will use jsonlines to load this data into our environment.
* `redisvl`: ensure you are on version `0.1.0` or later
* `cohere`: ensure you are on version `4.45` or later

To install the packages, use the following code
```shell SHELL
!pip install redisvl==0.1.0
!pip install cohere==4.45
!pip install jsonlines
```

### Import the required packages:

```python PYTHON
from redis import Redis
from redisvl.index import SearchIndex
from redisvl.schema import IndexSchema
from redisvl.utils.vectorize import CohereTextVectorizer
from redisvl.query import VectorQuery
from redisvl.query.filter import Tag, Text, Num
import jsonlines
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
