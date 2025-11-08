---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Haystack and Cohere (Integration Guide)

> Build custom LLM applications with Haystack, now integrated with Cohere for embedding, generation, chat, and retrieval.

<img src="file:337f97c4-151f-4676-9604-6385c43de815" width="200px" height="auto" class="light-bg" />

[Haystack](https://github.com/deepset-ai/haystack) is an open source LLM framework in Python by [deepset](https://www.deepset.ai/) for building customizable, production-ready LLM applications. You can use Cohere's `/embed`, `/generate`, `/chat`, and `/rerank` models with Haystack.

Cohere's Haystack integration provides four components that can be used in various Haystack pipelines, including retrieval augmented generation, chat, indexing, and so forth:

* The `CohereDocumentEmbedder`: To use Cohere embedding models to [index documents](https://docs.haystack.deepset.ai/v2.0/docs/coheredocumentembedder) into vector databases.
* The `CohereTextEmbedder` : To use Cohere embedding models to do [embedding retrieval](https://docs.haystack.deepset.ai/v2.0/docs/coheretextembedder).
* The `CohereGenerator` : To use Cohere’s [text generation models](https://docs.haystack.deepset.ai/v2.0/docs/coheregenerator).
* The `CohereChatGenerator` : To use Cohere’s [chat completion](https://docs.haystack.deepset.ai/v2.0/docs/coherechatgenerator) endpoints.

### Prerequisites

To use Cohere and Haystack you will need:

* The `cohere-haystack` integration installed. To install it, run `pip install cohere-haystack` If you run into any issues or want more details, [see these docs.](https://haystack.deepset.ai/integrations/cohere)
* A Cohere API Key. For more details on pricing [see this page](https://cohere.com/pricing). When you create an account with Cohere, we automatically create a trial API key for you. This key will be available on the dashboard where you can copy it, and it's in the dashboard section called "API Keys" as well.

### Cohere Chat with Haystack

Haystack’s `CohereChatGenerator` component enables chat completion using Cohere's large language models (LLMs). For the latest information on Cohere Chat [see these docs](/docs/chat-api).

In the example below, you will need to add your Cohere API key. We suggest using an environment variable, `COHERE_API_KEY`. Don’t commit API keys to source control!
```python PYTHON
from haystack import Pipeline
from haystack.components.builders import DynamicChatPromptBuilder
from haystack.dataclasses import ChatMessage
from haystack_integrations.components.generators.cohere import (
    CohereChatGenerator,
)
from haystack.utils import Secret
import os

COHERE_API_KEY = os.environ.get("COHERE_API_KEY")

pipe = Pipeline()
pipe.add_component("prompt_builder", DynamicChatPromptBuilder())
pipe.add_component(
    "llm", CohereChatGenerator(Secret.from_token(COHERE_API_KEY))
)
pipe.connect("prompt_builder", "llm")

location = "Berlin"
system_message = ChatMessage.from_system(
    "You are an assistant giving out valuable information to language learners."
)
messages = [
    system_message,
    ChatMessage.from_user("Tell me about {{location}}"),
]

res = pipe.run(
    data={
        "prompt_builder": {
            "template_variables": {"location": location},
            "prompt_source": messages,
        }
    }
)
print(res)
```
You can pass additional dynamic variables to the LLM, like so:
```python PYTHON
messages = [
    system_message,
    ChatMessage.from_user(
        "What's the weather forecast for {{location}} in the next {{day_count}} days?"
    ),
]

res = pipe.run(
    data={
        "prompt_builder": {
            "template_variables": {
                "location": location,
                "day_count": "5",
            },
            "prompt_source": messages,
        }
    }
)

print(res)
```

### Cohere Chat with Retrieval Augmentation

This Haystack [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG) pipeline passes Cohere’s documentation to a Cohere model, so it can better explain Cohere’s capabilities. In the example below, you can see the `LinkContentFetcher` replacing a classic retriever. The contents of the URL are passed to our generator.
```python PYTHON
from haystack import Document
from haystack import Pipeline
from haystack.components.builders import DynamicChatPromptBuilder
from haystack.components.generators.utils import print_streaming_chunk
from haystack.components.fetchers import LinkContentFetcher
from haystack.components.converters import HTMLToDocument
from haystack.dataclasses import ChatMessage
from haystack.utils import Secret

from haystack_integrations.components.generators.cohere import (
    CohereChatGenerator,
)

fetcher = LinkContentFetcher()
converter = HTMLToDocument()
prompt_builder = DynamicChatPromptBuilder(
    runtime_variables=["documents"]
)
llm = CohereChatGenerator(Secret.from_token(COHERE_API_KEY))

message_template = """Answer the following question based on the contents of the article: {{query}}\n
               Article: {{documents[0].content}} \n
           """
messages = [ChatMessage.from_user(message_template)]

rag_pipeline = Pipeline()
rag_pipeline.add_component(name="fetcher", instance=fetcher)
rag_pipeline.add_component(name="converter", instance=converter)
rag_pipeline.add_component("prompt_builder", prompt_builder)
rag_pipeline.add_component("llm", llm)

rag_pipeline.connect("fetcher.streams", "converter.sources")
rag_pipeline.connect(
    "converter.documents", "prompt_builder.documents"
)
rag_pipeline.connect("prompt_builder.prompt", "llm.messages")

question = "What are the capabilities of Cohere?"

result = rag_pipeline.run(
    {
        "fetcher": {"urls": ["/reference/about"]},
        "prompt_builder": {
            "template_variables": {"query": question},
            "prompt_source": messages,
        },
        "llm": {"generation_kwargs": {"max_tokens": 165}},
    },
)
print(result)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
