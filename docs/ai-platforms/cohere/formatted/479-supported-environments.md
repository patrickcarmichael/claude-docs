---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported environments

The table below summarizes the environments in which Cohere models can be deployed. You'll notice it contains many links; the links in the "sdk" column take you to Github pages with more information on Cohere's language-specific SDKs, while all the others take you to relevant sections in this document.

<Note title="Note">
  The Cohere v2 API is not yet supported for cloud deployments (Bedrock, SageMaker, Azure, and OCI) and will be coming soon. The code examples shown for these cloud deployments use the v1 API.
</Note>

| sdk                                                          | [Cohere platform](/reference/about) | [Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-cohere.html) | Sagemaker             | Azure            | OCI          | Private Deployment            |
| ------------------------------------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------------- | --------------------- | ---------------- | ------------ | ----------------------------- |
| [Typescript](https://github.com/cohere-ai/cohere-typescript) | [✅ docs](#cohere-platform)          | [✅ docs](#bedrock)                                                                           | [✅ docs](#sagemaker)  | [✅ docs](#azure) | [🟠 soon]()  | [✅ docs](#private-deployment) |
| [Python](https://github.com/cohere-ai/cohere-python)         | [✅ docs](#cohere-platform)          | [✅ docs](#bedrock)                                                                           | [✅ docs](#sagemaker)  | [✅ docs](#azure) | [🟠 soon]()  | [✅ docs](#private-deployment) |
| [Go](https://github.com/cohere-ai/cohere-go)                 | [✅ docs](#cohere-platform)          | [🟠 soon](#bedrock)                                                                          | [🟠 soon](#sagemaker) | [✅ docs](#azure) | [🟠 soon](#) | [✅ docs](#private-deployment) |
| [Java](https://github.com/cohere-ai/cohere-java)             | [✅ docs](#cohere-platform)          | [🟠 soon](#bedrock)                                                                          | [🟠 soon](#sagemaker) | [✅ docs](#azure) | [🟠 soon]()  | [✅ docs](#private-deployment) |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
