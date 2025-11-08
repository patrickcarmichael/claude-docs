---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an Elasticsearch client

Now we can instantiate the Python Elasticsearch client.

First we prompt the user for their endpoint and encoded API key. Then we create a client object that instantiates an instance of the Elasticsearch class.

When creating your Elastic Serverless API key make sure to turn on Control security privileges, and edit cluster privileges to specify `"cluster": ["all"]`.
```python PYTHON
ELASTICSEARCH_ENDPOINT = getpass("Elastic Endpoint: ")
ELASTIC_API_KEY = getpass(
    "Elastic encoded API key: "
)  # Use the encoded API key

client = Elasticsearch(
    ELASTICSEARCH_ENDPOINT, api_key=ELASTIC_API_KEY
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
