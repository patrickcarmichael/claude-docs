---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Print the final citations

citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

### Cohere with LangChain and Bedrock

#### Prerequisite

In addition to the prerequisites above, integrating Cohere with LangChain on Amazon Bedrock also requires:

* The LangChain AWS package. To install it, run `pip install langchain-aws`.
* AWS Python SDK. To install it, run `pip install boto3`. You can find [more details here ](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#install-boto3).
* Configured authentication credentials for AWS. For more details, [see this document](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).

#### Cohere Embeddings with LangChain and Amazon Bedrock

In this example, we create embeddings for a query using Bedrock and LangChain:
```python PYTHON
from langchain_aws import BedrockEmbeddings

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
