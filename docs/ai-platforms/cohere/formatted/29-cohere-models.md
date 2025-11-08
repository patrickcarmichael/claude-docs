---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere Models

<AccordionGroup>
  <Accordion title="What is the difference between the Command R and Command R+ models?">
    Command R+ is most suitable for those workflows that lean on complex RAG functionality and multi-step tool use (agents). Command R, on the other hand, is great for simpler retrieval augmented generation (RAG) and single-step tool use tasks, as well as applications where price is a major consideration. We offer a full model overview in our [documentation](https://docs.cohere.com/docs/models).
  </Accordion>

  <Accordion title="What is the difference between Aya and Command R models?">
    Aya specializes in human-like multilingual text generation and conversations, ideal for content creation and chatbots. Command R excels at understanding and executing instructions, enabling interactive applications and data-driven tasks.This makes it more suitable for many enterprise use cases.

    You can check out [this link](https://cohere.com/research/aya) to learn more about Aya models, datasets and related research papers.
  </Accordion>

  <Accordion title="How do Cohere's models compare to other LLMs on the market?">
    Cohere’s Command models have strong performance across enterprise tasks such as summarization, multilingual use cases, and retrieval augmented generation. We also have the widest range of deployment options, you can check it [here](https://cohere.com/deployment-options).
  </Accordion>

  <Accordion title="How can I use Cohere's models for tasks like translation, text embedding, summarization, and custom tool development?">
    You can access Cohere’s models through our platform (cohere.com) or through various cloud platforms including, but not limited to, Sagemaker, Bedrock, Azure AI, and OCI Generatie AI. We also have private deployments. In terms of use case specific features, please reference the latest [API documentation](https://docs.cohere.com/reference/about) to learn more about the API features and [Cookbooks](https://docs.cohere.com/page/cookbooks) with starter code for various tasks to aid development.
  </Accordion>

  <Accordion title="What are some best practices, tips, and techniques for prompt engineering?">
    You can find our prompt engineering recommendations in the following resources:

    * [Prompt Engineering Basics](https://cohere.com/llmu/prompt-engineering-basics)
    * [Crafting Effective Prompts](https://docs.cohere.com/v1/docs/crafting-effective-prompts)
    * [Advanced Prompt Engineering](https://docs.cohere.com/v1/docs/advanced-prompt-engineering-techniques)
  </Accordion>

  <Accordion title="How can I effectively use and fine-tune models for specific tasks, like data extraction, question answering, and generating content within certain constraints?">
    To fine-tune models for tasks like data extraction, question answering, or content generation, it’s important to start by defining your goals and ensuring your data captures the task accurately.

    For generative models, fine-tuning involves training on input-output pairs, where the model learns to generate specific outputs based on given inputs. This is ideal for tasks like customizing responses or enforcing a particular writing style.

    For tasks like data extraction, fine-tuning helps the model identify relevant patterns and structure data as needed. High-quality, task-specific data is essential for achieving accurate results.

    For more details, you can refer to [Cohere’s fine-tuning guide](https://docs.cohere.com/docs/fine-tuning) for best practices.

    Fine tuning is a powerful capability, but takes some effort to get right. You should first understand what you are trying to achieve and then determine if the data you are planning to train on effectively captures that task. The generative models specifically learn off of input/output pairs and therefore need to see examples of the expected input for your task and the ideal output. For more information, see our [finetuning guide](https://docs.cohere.com/v1/docs/chat-improving-the-results).
  </Accordion>

  <Accordion title="What are the best practices for preparing and structuring fine-tuning data, and what are the supported file formats?">
    You can find the best practices for preparing and structuring fine-tuning data across these three modules. Data preparation for [chat fine-tuning](https://docs.cohere.com/docs/chat-preparing-the-data), [classify fine-tuning](https://docs.cohere.com/docs/classify-preparing-the-data) and [rerank fine-tuning](https://docs.cohere.com/docs/rerank-preparing-the-data). The primary file formats supported are jsonl and csv.
  </Accordion>

  <Accordion title="What models are available for fine-tuning using the Cohere platform?">
    On the generative side we support fine-tuning for Command R and Command R 082024. On the representation side, we support fine-tuning for Classify and Rerank models. You can learn more about it [in this section](https://docs.cohere.com/docs/fine-tuning) of our docs.
  </Accordion>

  <Accordion title="What specific models are being developed by Cohere and where can I find detailed information about them?">
    For the latest current offerings, you should reference our [models page](https://docs.cohere.com/v1/docs/models).
  </Accordion>

  <Accordion title="Which model should I choose for my specific use case?">
    This largely depends on your use case. In general, Cohere has both generative and representation models. The [models page](https://docs.cohere.com/v1/docs/models) has more information on each of these, but use cases can often use a combination of models.
  </Accordion>

  <Accordion title="What are the capabilities of Cohere's models?">
    Cohere models offer a wide range of capabilities, from advanced generative tasks to semantic search and other representation use cases. All of our models are multilingual and can support use cases from [RAG](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) to [Tool Use](https://docs.cohere.com/docs/tools) and much more.

    Our [Command](https://cohere.com/command) model family is our flagship series of generative models. These models excel at taking a user instruction (or command) and generating text following the instruction. They also have conversational capabilities which means that they are well-suited for chatbots and virtual assistants.

    For representation tasks, we offer two key models:

    * [Embed](https://cohere.com/embed): Embed models generate embeddings from text, allowing for tasks like classification, clustering, and semantic search.
    * [Rerank](https://cohere.com/rerank): Rerank models improve the output of search and ranking systems by re-organizing results according to specific parameters, improving the relevance and accuracy of search results.

    Our models perform best when used end-to-end in their intended workflows. For a detailed breakdown of each model, including their latest versions, check our [models page](https://docs.cohere.com/docs/models).
  </Accordion>

  <Accordion title="What are the best practices and resources for building a search system for large PDF documents, and how can I optimize the retrieval process using language models and embeddings?">
    While this depends on the document structure itself, the best rule of thumb would be to split the PDF into its pages and then split each page into chunks that fit our context length.

    From there, you should associate each chunk to a page and a doc id which will allow you to have various levels of granularity for retrieval.

    You can find further guides on [chunking strategies](https://docs.cohere.com/page/chunking-strategies) and [handling PDFs with mixed data](https://docs.cohere.com/docs/semantic-search-embed#multimodal-pdf-search).
  </Accordion>

  <Accordion title="How can I develop a multilingual chatbot that can understand and respond to user queries in different languages, incorporate external data, and perform tasks like text search, citation generation, and answer reranking?">
    Cohere’s models offer multilingual capabilities out of the box. You can reference our example notebooks such as this [RAG one](https://docs.cohere.com/page/basic-rag) to get a better idea of how to piece these models together to build a question answering application.
  </Accordion>

  <Accordion title="What are the implications and limitations of using an unsupported language in Command-R, and are there plans to expand language support?">
    We are always looking to expand multilingual support to other languages. Command R/R+ have been exposed to other languages during training and we encourage you to try it on your use case. If you would like to provide feedback or suggestions on additional languages, please don't hesitate to contact [support@cohere.com](mailto:support@cohere.com).
  </Accordion>

  <Accordion title="Which languages are supported by Cohere models?">
    Cohere’s command models are optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.

    Additionally, pre-training data has been included for the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.

    You can find a full list of languages that are supported by Cohere’s multilingual embedding model [here](https://docs.cohere.com/docs/supported-languages).
  </Accordion>

  <Accordion title="What kind of use case scenarios can Cohere models be useful in?">
    You can check the range of use cases based on our customer stories [here](https://cohere.com/use-cases).
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
