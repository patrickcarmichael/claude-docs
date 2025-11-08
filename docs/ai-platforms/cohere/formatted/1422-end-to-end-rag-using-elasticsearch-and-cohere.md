---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## End-to-end RAG using Elasticsearch and Cohere

> This page contains a basic tutorial on how to get Cohere and ElasticSearch to work well together.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Cohere_Elastic_Guide.ipynb" />

Learn how to use the [Inference API](https://www.elastic.co/guide/en/elasticsearch/reference/current/inference-apis.html) for semantic search and use [Cohere's APIs](https://docs.cohere.com/docs/the-cohere-platform) for RAG.

For this example, you will need:

* An Elastic Serverless account through [Elastic Cloud](https://www.elastic.co/guide/en/cloud/current/ec-getting-started.html), available with a [free trial](https://cloud.elastic.co/registration?utm_source=github\&utm_content=elasticsearch-labs-notebook)

* A [Cohere account](https://cohere.com/) with a production API key

* Python 3.7 or higher

Note: While this tutorial integrates Cohere with an Elastic Cloud serverless project, you can also integrate with your self-managed Elasticsearch deployment or Elastic Cloud deployment by simply switching from using a Serverless endpoint in the Elasticsearch client.

If you don't have an Elastic Cloud deployment, sign up [here](https://cloud.elastic.co/registration?utm_source=github\&utm_content=elasticsearch-labs-notebook) for a free trial and request access to Elastic Serverless

To get started, we'll need to connect to our Elastic Serverless deployment using the Python client.

First we need to `pip` install the following packages:

* `elasticsearch_serverless`
* `cohere`

After installing, in the Serverless dashboard, find your endpoint URL, and create your API key.
```python PYTHON
pip install elasticsearch_serverless cohere
```
Next, we need to import the modules we need. 🔐 NOTE: getpass enables us to securely prompt the user for credentials without echoing them to the terminal, or storing it in memory.
```python PYTHON
from elasticsearch_serverless import Elasticsearch, helpers
from getpass import getpass
import cohere
import json
import requests
```
Now we can instantiate the Python Elasticsearch client.

First we prompt the user for their endpoint and encoded API key.
Then we create a `client` object that instantiates an instance of the `Elasticsearch` class.

When creating your Elastic Serverless API key make sure to turn on Control security privileges, and edit cluster privileges to specify `"cluster": ["all"]`
```python PYTHON
ELASTICSEARCH_ENDPOINT = getpass("Elastic Endpoint: ")
ELASTIC_API_KEY = getpass("Elastic encoded API key: ") # Use the encoded API key

client = Elasticsearch(
  ELASTICSEARCH_ENDPOINT,
  api_key=ELASTIC_API_KEY
)
```
Confirm that the client has connected with this test:
```python PYTHON
print(client.info())
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
