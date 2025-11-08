**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-coheres-command-r-model.md)

---

# Cohere Documentation

> Cohere's API documentation helps developers easily integrate natural language processing and generation into their products.

export const LandingPageCard = ({ href, title, imgSrc, description }) => (
  <div className="rounded-lg bg-[#F5F4F2] dark:bg-[#0F0F0F] px-6 py-5 hover:bg-[#E9E6DE] dark:hover:bg-[#292929] md:p-8">
    <a
      href={href}
      target="_self"
      className="flex h-full flex-col justify-between"
      style={{ textDecoration: 'none' }}
    >
      <div className="mb-5 flex flex-col justify-between gap-5">
        <h2 className="lg:min-h-20 [@media(min-width:1181px)]:min-h-0">
          {title}
        </h2>
        <img src={imgSrc} alt={title} />
        <p className="p-lg">{description}</p>
      </div>
      <div className="mt-2 text-sm text-[#2D4CB9] dark:text-[#4C6EE6] md:mt-0 md:self-end">
        {"GET STARTED"}
        <div className="ml-2 inline-block group-hover:no-underline">
          <svg
            width="12"
            height="11"
            viewBox="0 0 12 11"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            style={{ transform: "rotate(-90deg)" }}
          >
            <path
              d="M6 10.75L0.75 5.31686L1.74907 4.27907L5.2556 8.00291L5.2556 0.25L6.7444 0.25L6.7444 8.00291L10.2509 4.27907L11.25 5.31686L6 10.75Z"
              fill="currentColor"
            ></path>
          </svg>
        </div>
      </div>
    </a>
  </div>
);

export const EndpointLink = ({ href, title }) => (
  <a
    href={href}
    className="group flex cursor-pointer flex-row text-sm !font-normal text-[#2D4CB9] dark:text-[#4C6EE6]"
    rel="noreferrer"
    target="_self"
  >
    {title}
    <span className="duration-400 flex items-center transition-all ease-in-out group-hover:pl-1 group-hover:pr-2">
      <div className="ml-2 inline-block text-sm !text-[#2D4CB9] group-hover:no-underline">
        <svg
          width="12"
          height="11"
          viewBox="0 0 12 11"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
          style={{ transform: "rotate(-90deg)" }}
        >
          <path
            d="M6 10.75L0.75 5.31686L1.74907 4.27907L5.2556 8.00291L5.2556 0.25L6.7444 0.25L6.7444 8.00291L10.2509 4.27907L11.25 5.31686L6 10.75Z"
            fill="currentColor"
          ></path>
        </svg>
      </div>
    </span>
  </a>
);

export const cards = [
  {
    href: "/docs",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8da77c9-Frame_138972.png",
    title: "Guides and concepts",
    description:
      "Understand how to use our API on a deeper level. Train and customize the model to work for you.",
  },
  {
    href: "/reference/about",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/8ff146a-Group_138977.png",
    title: "API reference",
    description:
      "Integrate natural language processing and generation into your products with a few lines of code.",
  },
  {
    href: "/release-notes",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/d51d176-Group_138977_1.png",
    title: "Release notes",
    description:
      "Keep up with the latest releases and platform updates from Cohere.",
  },
  {
    href: "/page/cookbooks",
    imgSrc: "https://fern-image-hosting.s3.amazonaws.com/cohere/7fca92c-Group_138977_2.png",
    title: "Cookbooks",
    description:
      "A collection of resources to help developers get up and running with Cohere.",
  },
];

export const endpoints = [
  {
    href: "/reference/chat",
    title: "/CHAT",
  },
  {
    href: "/reference/embed",
    title: "/EMBED",
  },
  {
    href: "/reference/rerank",
    title: "/RERANK",
  },
];

<div>
  <div>
    {cards.map((card) => (
          <LandingPageCard
            key={card.href}
            href={card.href}
            imgSrc={card.imgSrc}
            title={card.title}
            description={card.description}
          />
        ))}

    <div>
      <div>
        <div>
          <h2>
            Endpoints
          </h2>

          <p>
            Our endpoints offer different ways to interact with our models and
            offer additional value on top of them
          </p>
        </div>

        <div>
          {endpoints.map((endpoint) => (
                      <EndpointLink key={endpoint.href} {...endpoint} />
                    ))}
        </div>
      </div>

      <div>
        <a href="https://cohere.com/llmu" target="_blank">
          <div>
            <div>
              <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/9d0694c-Symbol.svg" alt="" />

              <h2>
                LLM University
              </h2>
            </div>

            <p>
              Join our learning hub to master Enterprise AI with expert-led
              courses and step-by-step guides
            </p>
          </div>

          <div>
            <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/64d7b4f-Group_138975.png" alt="" />
          </div>
        </a>
      </div>
    </div>
  </div>

  <div>
    <a href="https://cohere.com/llmu" target="_blank">
      <div>
        <div>
          <img src="https://fern-image-hosting.s3.amazonaws.com/cohere/9d0694c-Symbol.svg" alt="" />

          <h2>
            LLM University
          </h2>
        </div>

        <p>
          New to NLP? Learn about Natural Language processing and Large Language
          Models through our structured curriculum.
        </p>
      </div>
    </a>
  </div>
</div>


# An Overview of The Cohere Platform

> Cohere offers world-class Large Language Models (LLMs) like Command, Rerank, and Embed. These help developers and enterprises build LLM-powered applications.

## Large Language Models (LLMs)

Language is important. It’s how we learn about the world (e.g. news, searching the web or Wikipedia), and also how we shape it (e.g. agreements, laws, or messages). Language is also how we connect and communicate — as people, and as groups and companies.

Despite the rapid evolution of software, computers remain limited in their ability to deal with language. Software is great at searching for exact matches in text, but often fails at more advanced uses of language — ones that humans employ on a daily basis.

There’s a clear need for more intelligent tools that better understand language.

A recent breakthrough in artificial intelligence (AI) is the introduction of language processing technologies that enable us to build more intelligent systems with a richer understanding of language than ever before. Large pre-trained Transformer language models, or simply large language models, vastly extend the capabilities of what systems are able to do with text.

<img src="file:ade85ef0-9caf-4a52-bcc7-2a0c3afb0ed2" alt="systems." />

Consider this: adding language models to empower Google Search was <a href="https://blog.google/products/search/search-language-understanding-bert/" target="_blank">noted</a> as “representing the biggest leap forward in the past five years, and one of the biggest leaps forward in the history of Search“. Microsoft also <a href="https://azure.microsoft.com/en-us/blog/bing-delivers-its-largest-improvement-in-search-experience-using-azure-gpus/" target="_blank">uses</a> such models for every query in the Bing search engine.

Despite the utility of these models, training and deploying them effectively is resource intensive, requiring a large investment of data, compute, and engineering resources.

## Cohere's LLMs

Cohere allows developers and enterprises to build LLM-powered applications. We do that by creating world-class models, along with the supporting platform required to deploy them securely and privately.

The Command family of models includes [Command A](https://docs.cohere.com/docs/command-a), [Command R7B](https://docs.cohere.com/docs/command-r7b), [Command R+](/docs/command-r-plus), and [Command R](/docs/command-r). Together, they are the text-generation LLMs powering conversational agents, summarization, copywriting, and similar use cases. They work through the [Chat](/reference/chat) endpoint, which can be used with or without [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) RAG.

[Rerank](https://cohere.com/blog/rerank/) is the fastest way to inject the intelligence of a language model into an existing search system. It can be accessed via the [Rerank](/reference/rerank-1) endpoint.

[Embed](https://cohere.com/models/embed) improves the accuracy of search, classification, clustering, and RAG results. It also powers the [Embed](/reference/embed) and [Classify](/reference/classify) endpoints.

<img src="file:71947505-690b-4327-b8a2-b2feac6fa780" />

[Click here](/docs/foundation-models) to learn more about Cohere foundation models.

## Example Applications

Try [the playground](https://dashboard.cohere.com/playground) to see what an LLM-powered conversational agent can look like. It is able to converse, summarize text, and write emails and articles.

<img src="file:ae2c54eb-7e06-4587-83ff-1baf15bbb8ff" />

Our goal, however, is to enable you to build your own LLM-powered applications. The [Chat endpoint](/docs/chat-api), for example, can be used to build a conversational agent powered by the Command family of models.

<img src="file:190c8a21-ae98-40af-9cc6-e1e814043d5c" alt="A diagram of a conversational agent." />

### Retrieval-Augmented Generation (RAG)

“Grounding” refers to the practice of allowing an LLM to access external data sources – like the internet or a company’s internal technical documentation – which leads to better, more factual generations.

Chat is being used with grounding enabled in the screenshot below, and you can see how accurate and information-dense its reply is.

<img src="file:1a0b5f30-bae0-4d4e-b369-4edbc74d1d23" />

What’s more, advanced RAG capabilities allow you to see what underlying query the model generates when completing its tasks, and its output includes [citations](/docs/documents-and-citations) pointing you to where it found the information it uses. Both the query and the citations can be leveraged alongside the Cohere Embed and Rerank models to build a remarkably powerful RAG system, such as the one found in [this guide](https://cohere.com/llmu/rag-chatbot).

<img src="file:b0b67642-d519-4cec-bf98-1bde60f2adcc" />

[Click here](/docs/serving-platform) to learn more about the Cohere serving platform.

### Advanced Search & Retrieval

Embeddings enable you to search based on what a phrase *means* rather than simply what keywords it *contains*, leading to search systems that incorporate context and user intent better than anything that has come before.

<img src="file:19f1d300-01fe-4315-b15e-4a1b276012b4" alt="How a query returns results." />

Learn more about semantic search [here](https://cohere.com/llmu/what-is-semantic-search).

## Fine-Tuning

To [create a fine-tuned model](/docs/fine-tuning), simply upload a dataset and hold on while we train a custom model and then deploy it for you. Fine-tuning can be done with [generative models](/docs/generate-fine-tuning), [multi-label classification models](/docs/classify-fine-tuning), [rerank models](/docs/rerank-fine-tuning), and [chat models](/docs/chat-fine-tuning).

<img src="file:99d52202-128b-4aa2-9857-6d97e404042f" alt="A diagram of fine-tuning." />

## Accessing Cohere Models

Depending on your privacy/security requirements there are a number of ways to access Cohere:

* [Cohere API](/reference/about): this is the easiest option, simply grab an API key from [the dashboard](https://dashboard.cohere.com/) and start using the models hosted by Cohere.
* Cloud AI platforms: this option offers a balance of ease-of-use and security. you can access Cohere on various cloud AI platforms such as [Oracle's GenAI Service](https://www.oracle.com/uk/artificial-intelligence/generative-ai/large-language-models/), AWS' [Bedrock](https://aws.amazon.com/bedrock/cohere-command-embed/) and [Sagemaker](https://aws.amazon.com/blogs/machine-learning/cohere-brings-language-ai-to-amazon-sagemaker/) platforms, [Google Cloud](https://console.cloud.google.com/marketplace/product/cohere-id-public/cohere-public?ref=txt.cohere.com), and [Azure's AML service](https://cohere.com/blog/coheres-enterprise-ai-models-coming-soon-to-microsoft-azure-ai-as-a-managed-service/).
* Private cloud deploy deployments: Cohere's models can be deployed privately in most virtual private cloud (VPC) environments, offering enhanced security and highest degree of customization. Please [contact sales](emailto:team@cohere.com) for information.

<img src="file:bd47f0eb-b2fc-4b60-883d-6d60019e715b" alt="The major cloud providers." />

### On-Premise and Air Gapped Solutions

* On-premise: if your organization deals with sensitive data that cannot live on a cloud we also offer the option for fully-private deployment on your own infrastructure. Please [contact sales](emailto:team@cohere.com) for information.

## Let us Know What You’re Making

We hope this overview has whetted your appetite for building with our generative AI models. Reach out to us on [Discord](https://discord.com/invite/co-mmunity) with any questions or to showcase your projects – we love hearing from the Cohere community!


# Installation

> A guide for installing the Cohere SDK, supported in 4 different languages – Python, TypeScript, Java, and Go.

## Platform options

To be able to use Cohere’s models, first choose the platform where you want to access the model from. Cohere's models are available on the following platforms:

| Platform            | Description                                                                                                                | Setup Guide                                                                                                                                                                                                                                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cohere Platform     | The fastest way to start using Cohere’s models. Hosted on Cohere infrastructure and available on our public SaaS platform. | [Sign up](https://dashboard.cohere.com/welcome/register) and get an [API key](https://dashboard.cohere.com/api-keys) (trial key available)                                                                                                                                                                                                                         |
| Private Deployments | For enterprises looking to deploy the Cohere stack privately on the cloud or on-prem.                                      | [Setup guide](https://docs.cohere.com/docs/single-container-on-private-clouds)                                                                                                                                                                                                                                                                                     |
| Cloud deployments   | Managed services from cloud providers that enable access to Cohere's models.                                               | • [Amazon Bedrock](https://docs.cohere.com/docs/amazon-bedrock#prerequisites)<br />• [Amazon SageMaker](https://docs.cohere.com/docs/amazon-sagemaker-setup-guide#prerequisites)<br />• [Azure AI Foundry](https://docs.cohere.com/docs/cohere-on-microsoft-azure#prerequisites)<br />• [Oracle OCI](https://docs.cohere.com/docs/oracle-cloud-infrastructure-oci) |

## Model usage

You can then use the models via these options:

* [SDK](https://docs.cohere.com/v1/reference/about#sdks). We support the following SDKs:
  * [Python](https://github.com/cohere-ai/cohere-python)
  * [TypeScript](https://github.com/cohere-ai/cohere-typescript)
  * [Java](https://github.com/cohere-ai/cohere-java)
  * [Go](https://github.com/cohere-ai/cohere-go)
* [Playground](https://docs.cohere.com/v1/docs/playground-overview)

## Installation

To install the Cohere SDK, choose from the following 4 languages:

<Tabs>
  <Tab title="Python">
    ```bash
    pip install -U cohere
    ```

    [Source](https://github.com/cohere-ai/cohere-python)
  </Tab>

  <Tab title="TypeScript">
    ```bash
    npm i -s cohere-ai
    ```

    [Source](https://github.com/cohere-ai/cohere-typescript)
  </Tab>

  <Tab title="Java">
    ```gradle
    implementation 'com.cohere:cohere-java:1.x.x'
    ```

    [Source](https://github.com/cohere-ai/cohere-java)
  </Tab>

  <Tab title="Go">
    ```bash
    go get github.com/cohere-ai/cohere-go/v2
    ```

    [Source](https://github.com/cohere-ai/cohere-go)
  </Tab>
</Tabs>


# Creating a client

> A guide for creating Cohere API client using Cohere SDK, supported in 4 different languages – Python, TypeScript, Java, and Go.

## Creating Cohere API Client

To start using all features available in the Cohere SDK, you should create a client first.

<Tabs>
  <Tab title="Python">
    ```python
    import cohere

    co = cohere.ClientV2(api_key="YOUR_API_KEY")
    ```

    [Source](https://github.com/cohere-ai/cohere-python)

    The Cohere API client initializes with the following parameters:

    | Parameter              | Type                 | Default                        | Description                                                                 |
    | ---------------------- | -------------------- | ------------------------------ | --------------------------------------------------------------------------- |
    | `api_key`              | `str/callable`       | `None`                         | API key for authenticating requests to the Cohere V2 API.                   |
    | `base_url`             | `str`                | `os.getenv("CO_API_URL")`      | Base URL for the Cohere API.                                                |
    | `environment`          | `ClientEnvironment`  | `ClientEnvironment.PRODUCTION` | Specifies the API environment (e.g., production, staging).                  |
    | `client_name`          | `str`                | `None`                         | Optional name for the client instance, useful for logging.                  |
    | `timeout`              | `float`              | `None`                         | Timeout in seconds for API requests.                                        |
    | `httpx_client`         | `httpx.Client`       | `None`                         | Optional pre-configured `httpx.Client` for making HTTP requests.            |
    | `thread_pool_executor` | `ThreadPoolExecutor` | `ThreadPoolExecutor(64)`       | Thread pool executor for concurrent operations, with 64 threads by default. |
    | `log_experimental`     | `bool`               | `True`                         | Enables/disables warnings for experimental features.                        |
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    import { CohereClientV2 } from 'cohere-ai';

    const cohere = new CohereClientV2({ token: 'YOUR_API_KEY' });
    ```

    [Source](https://github.com/cohere-ai/cohere-typescript)

    The Cohere API client initializes with the following parameters:

    | Parameter    | Type                    | Default                      | Description                                                               |
    | ------------ | ----------------------- | ---------------------------- | ------------------------------------------------------------------------- |
    | `token`      | `string`                | `undefined`                  | **Required.** API key used for authenticating requests to the Cohere API. |
    | `baseUrl`    | `string`                | `"https://api.cohere.ai/v1"` | Base URL endpoint for the Cohere API.                                     |
    | `clientName` | `string`                | `undefined`                  | Optional identifier for the client instance, useful for logging.          |
    | `timeout`    | `number` (milliseconds) | `120000` (120 seconds)       | Request timeout in milliseconds.                                          |
    | `fetch`      | `typeof fetch`          | Global `fetch`               | Custom fetch implementation for HTTP requests.                            |
  </Tab>

  <Tab title="Java">
    ```java
    import com.cohere.api.Cohere;

    Cohere cohere = Cohere.builder()
                          .token("YOUR_API_KEY")
                          .clientName("your-client-name")
                          .build();

    ```

    [Source](https://github.com/cohere-ai/cohere-java)

    The Cohere API client initializes with the following parameters:

    | Parameter      | Type           | Default                      | Description                                                    |
    | -------------- | -------------- | ---------------------------- | -------------------------------------------------------------- |
    | `token`        | `String`       | `null`                       | **Required.** Your Cohere API key for authenticating requests. |
    | `baseUrl`      | `String`       | `"https://api.cohere.ai/v1"` | The base URL for the Cohere API.                               |
    | `clientName`   | `String`       | `null`                       | Optional identifier for your client application.               |
    | `timeout`      | `Duration`     | `null`                       | Timeout duration for API requests.                             |
    | `okHttpClient` | `OkHttpClient` | `null`                       | Custom `OkHttpClient` instance for making HTTP requests.       |
  </Tab>

  <Tab title="Go">
    ```go
    import (
        client "github.com/cohere-ai/cohere-go/v2/client"
    )

    co := client.NewClient(client.WithToken("YOUR_API_KEY"))
    ```

    [Source](https://github.com/cohere-ai/cohere-go)

    The Cohere API client initializes with the following parameters:

    | Parameter    | Type           | Default                      | Description                                                    |
    | ------------ | -------------- | ---------------------------- | -------------------------------------------------------------- |
    | `token`      | `string`       | `""` (empty string)          | **Required.** Your Cohere API key for authenticating requests. |
    | `baseURL`    | `string`       | `"https://api.cohere.ai/v1"` | The base URL for the Cohere API.                               |
    | `httpClient` | `*http.Client` | `http.DefaultClient`         | Custom HTTP client for making requests.                        |
  </Tab>
</Tabs>


# Text generation - quickstart

> A quickstart guide for performing text generation with Cohere's Command models (v2 API).

Cohere's Command family of LLMs are available via the Chat endpoint. This endpoint enables you to build generative AI applications and facilitates a conversational interface for building chatbots.

This quickstart guide shows you how to perform text generation with the Chat endpoint.

<Steps>
  ### Setup

  First, install the Cohere Python SDK with the following command.

  ```bash
  pip install -U cohere
  ```

  Next, import the library and create a client.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank
          base_url="<YOUR_DEPLOYMENT_URL>",
      )
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      import cohere

      co = cohere.BedrockClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )

      # Get the model name: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      import cohere

      co = cohere.SagemakerClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="AZURE_API_KEY",
          base_url="AZURE_ENDPOINT",
      )
      ```
    </Tab>
  </Tabs>

  ### Basic Text Generation

  To perform a basic text generation, call the Chat endpoint by passing the `messages` parameter containing the `user` message.

  <Info>
    The `model` parameter definition for private deployments is the same as the Cohere platform, as shown below. Find more details on private deployments usage [here](https://docs.cohere.com/docs/private-deployment-usage#getting-started).
  </Info>

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      response = co.chat(
          model="command-a-03-2025",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      response = co.chat(
          model="command-a-03-2025",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      response = co.chat(
          model="YOUR_MODEL_NAME",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      response = co.chat(
          model="YOUR_ENDPOINT_NAME",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      response = co.chat(
          model="model",  # Pass a dummy string
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      print(response.message.content[0].text)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  "Excited to be part of the Co1t team, I'm [Your Name], a [Your Role], passionate about [Your Area of Expertise] and looking forward to contributing to the company's success."
  ```

  ### State Management

  To maintain the state of a conversation, such as for building chatbots, append a sequence of `user` and `assistant` messages to the `messages` list. You can also include a `system` message at the start of the list to set the context of the conversation.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      messages = [
          {
              "role": "system",
              "content": "You respond in concise sentences.",
          },
          {"role": "user", "content": "Hello"},
      ]

      # User sends a message
      response = co.chat(
          model="command-a-03-2025",
          messages=messages,
      )

      # The model responds
      print(
          response.message.content[0].text
      )  # Hi, how can I help you today?

      # Append the model's response to the messages
      messages.append(response.message)

      # append another user message to the messages
      messages.append(
          {
              "role": "user",
              "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
          }
      )

      # get the model's second response
      response = co.chat(
          model="command-a-03-2025",
          messages=messages,
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      messages = [
          {
              "role": "system",
              "content": "You respond in concise sentences.",
          },
          {"role": "user", "content": "Hello"},
      ]

      # User sends a message
      response = co.chat(
          model="command-a-03-2025",
          messages=messages,
      )

      # The model responds
      print(
          response.message.content[0].text
      )  # Hi, how can I help you today?

      # Append the model's response to the messages
      messages.append(response.message)

      # append another user message to the messages
      messages.append(
          {
              "role": "user",
              "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
          }
      )

      # get the model's second response
      response = co.chat(
          model="command-a-03-2025",
          messages=messages,
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      messages = [
          {
              "role": "system",
              "content": "You respond in concise sentences.",
          },
          {"role": "user", "content": "Hello"},
      ]

      # User sends a message
      response = co.chat(
          model="YOUR_MODEL_NAME",
          messages=messages,
      )

      # The model responds
      print(
          response.message.content[0].text
      )  # Hi, how can I help you today?

      # Append the model's response to the messages
      messages.append(response.message)

      # append another user message to the messages
      messages.append(
          {
              "role": "user",
              "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
          }
      )

      # get the model's second response
      response = co.chat(
          model="YOUR_MODEL_NAME",
          messages=messages,
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      messages = [
          {
              "role": "system",
              "content": "You respond in concise sentences.",
          },
          {"role": "user", "content": "Hello"},
      ]

      # User sends a message
      response = co.chat(
          model="YOUR_ENDPOINT_NAME",
          messages=messages,
      )

      # The model responds
      print(
          response.message.content[0].text
      )  # Hi, how can I help you today?

      # Append the model's response to the messages
      messages.append(response.message)

      # append another user message to the messages
      messages.append(
          {
              "role": "user",
              "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
          }
      )

      # get the model's second response
      response = co.chat(
          model="YOUR_ENDPOINT_NAME",
          messages=messages,
      )

      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      messages = [
          {
              "role": "system",
              "content": "You respond in concise sentences.",
          },
          {"role": "user", "content": "Hello"},
      ]

      # User sends a message
      response = co.chat(
          model="model",  # Pass a dummy string
          messages=messages,
      )

      # The model responds
      print(
          response.message.content[0].text
      )  # Hi, how can I help you today?

      # Append the model's response to the messages
      messages.append(response.message)

      # append another user message to the messages
      messages.append(
          {
              "role": "user",
              "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
          }
      )

      # get the model's second response
      response = co.chat(
          model="model",  # Pass a dummy string
          messages=messages,
      )

      print(response.message.content[0].text)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  "Excited to join the team at Co1t, looking forward to contributing my skills and collaborating with everyone!"
  ```

  ### Streaming

  To stream text generation, call the Chat endpoint using `chat_stream` instead of `chat`. This returns a generator that yields `chunk` objects, which you can access the generated text from.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      res = co.chat_stream(
          model="command-a-03-2025",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      for chunk in res:
          if chunk.type == "content-delta":
              print(chunk.delta.message.content.text, end="")
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      res = co.chat_stream(
          model="command-a-03-2025",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      for chunk in res:
          if chunk.type == "content-delta":
              print(chunk.delta.message.content.text, end="")
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      res = co.chat_stream(
          model="YOUR_MODEL_NAME",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      for chunk in res:
          if chunk.type == "content-delta":
              print(chunk.delta.message.content.text, end="")
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      res = co.chat_stream(
          model="YOUR_ENDPOINT_NAME",
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      for chunk in res:
          if chunk.type == "content-delta":
              print(chunk.delta.message.content.text, end="")
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      res = co.chat_stream(
          model="model",  # Pass a dummy string
          messages=[
              {
                  "role": "user",
                  "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
              }
          ],
      )

      for chunk in res:
          if chunk.type == "content-delta":
              print(chunk.delta.message.content.text, end="")
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  "Excited to be part of the Co1t team, I'm [Your Name], a [Your Role/Position], looking forward to contributing my skills and collaborating with this talented group to drive innovation and success."
  ```
</Steps>

## Further Resources

* [Chat endpoint API reference](https://docs.cohere.com/reference/chat)
* [Documentation on text generation](https://docs.cohere.com/docs/introduction-to-text-generation-at-cohere)
* [LLM University module on text generation](https://cohere.com/llmu#text-generation)


# Retrieval augmented generation (RAG) - quickstart

> A quickstart guide for performing retrieval augmented generation (RAG) with Cohere's Command models (v2 API).

Retrieval Augmented Generation (RAG) enables an LLM to ground its responses on external documents, thus improving the accuracy of its responses and minimizing hallucinations.

The Chat endpoint comes with built-in RAG capabilities such as document grounding and citation generation.

This quickstart guide shows you how to perform RAG with the Chat endpoint.

<Steps>
  ### Setup

  First, install the Cohere Python SDK with the following command.

  ```bash
  pip install -U cohere
  ```

  Next, import the library and create a client.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank
          base_url="<YOUR_DEPLOYMENT_URL>",
      )
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      import cohere

      co = cohere.BedrockClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )

      # Get the model name: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      import cohere

      co = cohere.SagemakerClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="AZURE_API_KEY",
          base_url="AZURE_ENDPOINT",
      )
      ```
    </Tab>
  </Tabs>

  ### Documents

  First, define the documents that will passed as the context for RAG. These documents are typically retrieved from sources such as vector databases via semantic search, or any system that can retrieve unstructured data given a user query.

  Each document is a `data` object that can take any number of fields e.g. `title`, `url`, `text`, etc.

  ```python PYTHON
  documents = [
      {
          "data": {
              "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
          }
      },
      {
          "data": {
              "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
          }
      },
      {
          "data": {
              "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
          }
      },
  ]
  ```

  ### Response Generation

  Next, call the Chat API by passing the documents in the `documents` parameter. This tells the model to run in RAG-mode and use these documents as the context in its response.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      # Add the user query
      query = "Are there health benefits?"

      # Generate the response
      response = co.chat(
          model="command-a-03-2025",
          messages=[{"role": "user", "content": query}],
          documents=documents,
      )

      # Display the response
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      # Add the user query
      query = "Are there health benefits?"

      # Generate the response
      response = co.chat(
          model="command-a-03-2025",
          messages=[{"role": "user", "content": query}],
          documents=documents,
      )

      # Display the response
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      # Add the user query
      query = "Are there health benefits?"

      # Generate the response
      response = co.chat(
          model="YOUR_MODEL_NAME",
          messages=[{"role": "user", "content": query}],
          documents=documents,
      )

      # Display the response
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      # Add the user query
      query = "Are there health benefits?"

      # Generate the response
      response = co.chat(
          model="YOUR_ENDPOINT_NAME",
          messages=[{"role": "user", "content": query}],
          documents=documents,
      )

      # Display the response
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      # Add the user query
      query = "Are there health benefits?"

      # Generate the response
      response = co.chat(
          model="model",  # Pass a dummy string
          messages=[{"role": "user", "content": query}],
          documents=documents,
      )

      # Display the response
      print(response.message.content[0].text)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  Yes, there are health benefits. We offer gym memberships, on-site yoga classes, and comprehensive health insurance.
  ```

  ### Citation Generation

  The response object contains a `citations` field, which contains specific text spans from the documents on which the response is grounded.

  ```python PYTHON
  if response.message.citations:
      for citation in response.message.citations:
          print(citation, "\n")
  ```

  ```mdx wordWrap
  start=14 end=88 text='gym memberships, on-site yoga classes, and comprehensive health insurance.' document_ids=['doc_1'] 

  ```
</Steps>

## Further Resources

* [Chat endpoint API reference](https://docs.cohere.com/reference/chat)
* [Documentation on RAG](https://docs.cohere.com/docs/retrieval-augmented-generation-rag)
* [LLM University module on RAG](https://cohere.com/llmu#rag)


# Tool use & agents - quickstart

> A quickstart guide for using tool use and building agents with Cohere's Command models (v2 API).

Tool use enables developers to build agentic applications that connect to external tools, do reasoning, and perform actions.

The Chat endpoint comes with built-in tool use capabilities such as function calling, multi-step reasoning, and citation generation.

This quickstart guide shows you how to utilize tool use with the Chat endpoint.

<Steps>
  ### Setup

  First, install the Cohere Python SDK with the following command.

  ```bash
  pip install -U cohere
  ```

  Next, import the library and create a client.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank
          base_url="<YOUR_DEPLOYMENT_URL>",
      )
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      import cohere

      co = cohere.BedrockClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )

      # Get the model name: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      import cohere

      co = cohere.SagemakerClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="AZURE_API_KEY",
          base_url="AZURE_ENDPOINT",
      )
      ```
    </Tab>
  </Tabs>

  ### Tool Definition

  First, we need to set up the tools. A tool can be any function or service that can receive and send objects.

  We also need to define the tool schemas in a format that can be passed to the Chat endpoint. The schema must contain the following fields: `name`, `description`, and `parameters`.

  ```python PYTHON
  def get_weather(location):
      # Implement your tool calling logic here
      return [{"temperature": "20C"}]
      # Return a list of objects e.g. [{"url": "abc.com", "text": "..."}, {"url": "xyz.com", "text": "..."}]


  functions_map = {"get_weather": get_weather}

  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "gets the weather of a given location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "the location to get weather, example: San Fransisco, CA",
                      }
                  },
                  "required": ["location"],
              },
          },
      },
  ]
  ```

  ### Tool Calling

  Next, pass the tool schema to the Chat endpoint together with the user message.

  The LLM will then generate the tool calls (if any) and return the `tool_plan` and `tool_calls` objects.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      messages = [
          {"role": "user", "content": "What's the weather in Toronto?"}
      ]

      response = co.chat(
          model="command-a-03-2025", messages=messages, tools=tools
      )

      if response.message.tool_calls:
          messages.append(response.message)
          print(response.message.tool_calls)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      messages = [
          {"role": "user", "content": "What's the weather in Toronto?"}
      ]

      response = co.chat(
          model="command-a-03-2025", messages=messages, tools=tools
      )

      if response.message.tool_calls:
          messages.append(
              {
                  "role": "assistant",
                  "tool_calls": response.message.tool_calls,
                  "tool_plan": response.message.tool_plan,
              }
          )
          print(response.message.tool_calls)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      messages = [
          {"role": "user", "content": "What's the weather in Toronto?"}
      ]

      response = co.chat(
          model="YOUR_MODEL_NAME", messages=messages, tools=tools
      )

      if response.message.tool_calls:
          messages.append(response.message)
          print(response.message.tool_calls)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      messages = [
          {"role": "user", "content": "What's the weather in Toronto?"}
      ]

      response = co.chat(
          model="YOUR_ENDPOINT_NAME", messages=messages, tools=tools
      )

      if response.message.tool_calls:
          messages.append(response.message)
          print(response.message.tool_calls)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      messages = [
          {"role": "user", "content": "What's the weather in Toronto?"}
      ]

      response = co.chat(
          model="model",  # Pass a dummy string
          messages=messages,
          tools=tools,
      )

      if response.message.tool_calls:
          messages.append(response.message)
          print(response.message.tool_calls)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  [ToolCallV2(id='get_weather_776n8ctsgycn', type='function', function=ToolCallV2Function(name='get_weather', arguments='{"location":"Toronto"}'))]
  ```

  ### Tool Execution

  Next, the tools called will be executed based on the arguments generated in the tool calling step earlier.

  ```python PYTHON
  import json

  if response.message.tool_calls:
      for tc in response.message.tool_calls:
          tool_result = functions_map[tc.function.name](
              **json.loads(tc.function.arguments)
          )
          tool_content = []
          for data in tool_result:
              tool_content.append(
                  {
                      "type": "document",
                      "document": {"data": json.dumps(data)},
                  }
              )
              # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
          messages.append(
              {
                  "role": "tool",
                  "tool_call_id": tc.id,
                  "content": tool_content,
              }
          )
  ```

  ### Response Generation

  The results are passed back to the LLM, which generates the final response.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      response = co.chat(
          model="command-a-03-2025", messages=messages, tools=tools
      )
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      response = co.chat(
          model="command-a-03-2025", messages=messages, tools=tools
      )
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      response = co.chat(
          model="YOUR_MODEL_NAME", messages=messages, tools=tools
      )
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      response = co.chat(
          model="YOUR_ENDPOINT_NAME", messages=messages, tools=tools
      )
      print(response.message.content[0].text)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      response = co.chat(
          model="model",  # Pass a dummy string
          messages=messages,
          tools=tools,
      )
      print(response.message.content[0].text)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  It is 20C in Toronto.
  ```

  ### Citation Generation

  The response object contains a `citations` field, which contains specific text spans from the documents on which the response is grounded.

  ```python PYTHON
  if response.message.citations:
      for citation in response.message.citations:
          print(citation, "\n")
  ```

  ```mdx wordWrap
  start=6 end=9 text='20C' sources=[ToolSource(type='tool', id='get_weather_776n8ctsgycn:0', tool_output={'temperature': '20C'})] 
  ```
</Steps>

## Further Resources

* [Chat endpoint API reference](https://docs.cohere.com/reference/chat)
* [Documentation on tool use](https://docs.cohere.com/docs/tools)
* [LLM University module on tool use](https://cohere.com/llmu#tool-use)


# Semantic search - quickstart

> A quickstart guide for performing text semantic search with Cohere's Embed models (v2 API).

Cohere's embedding models are available via the Embed endpoint. This endpoint enables you to embed text documents (multilingual) and images into a vector space.

Semantic search, powered by embeddings, enables applications to perform information retrieval based on the context or meaning of a document.

This quickstart guide shows you how to perform semantic search with the Embed endpoint.

<Steps>
  ### Setup

  First, install the Cohere Python SDK with the following command.

  ```bash
  pip install -U cohere
  ```

  Next, import the library and create a client.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank
          base_url="<YOUR_DEPLOYMENT_URL>",
      )
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      import cohere

      co = cohere.BedrockClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )

      # Get the model name: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      import cohere

      co = cohere.SagemakerClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="AZURE_API_KEY",
          base_url="AZURE_ENDPOINT",
      )
      ```
    </Tab>
  </Tabs>

  ### Document Embeddings

  First, embed the list of available documents using the Embed endpoint by specifying the `input_type` as `search_document`.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      # Define the documents
      documents = [
          "Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.",
          "Finding Coffee Spots: For your caffeine fix, cross the street to the café for artisan coffee.",
          "Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      ]

      # Embed the documents
      doc_emb = co.embed(
          model="embed-v4.0",
          input_type="search_document",
          texts=documents,
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      # Define the documents
      documents = [
          "Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.",
          "Finding Coffee Spots: For your caffeine fix, cross the street to the café for artisan coffee.",
          "Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      ]

      # Embed the documents
      doc_emb = co.embed(
          model="embed-v4.0",
          input_type="search_document",
          texts=documents,
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      # Define the documents
      documents = [
          "Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.",
          "Finding Coffee Spots: For your caffeine fix, cross the street to the café for artisan coffee.",
          "Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      ]

      # Embed the documents
      doc_emb = co.embed(
          model="YOUR_MODEL_NAME",
          input_type="search_document",
          texts=documents,
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      # Define the documents
      documents = [
          "Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.",
          "Finding Coffee Spots: For your caffeine fix, cross the street to the café for artisan coffee.",
          "Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      ]

      # Embed the documents
      doc_emb = co.embed(
          model="YOUR_ENDPOINT_NAME",
          input_type="search_document",
          texts=documents,
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      # Define the documents
      documents = [
          "Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.",
          "Finding Coffee Spots: For your caffeine fix, cross the street to the café for artisan coffee.",
          "Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      ]

      # Embed the documents
      doc_emb = co.embed(
          input_type="search_document",
          texts=documents,
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>
  </Tabs>

  ### Query Embedding

  Next, embed the user query using the Embed endpoint by specifying the `input_type` as `search_query`.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      # Add the user query
      query = "Ways to connect with my teammates"

      # Embed the query
      query_emb = co.embed(
          model="embed-v4.0",
          input_type="search_query",
          texts=[query],
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      # Add the user query
      query = "Ways to connect with my teammates"

      # Embed the query
      query_emb = co.embed(
          model="embed-v4.0",
          input_type="search_query",
          texts=[query],
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      # Add the user query
      query = "Ways to connect with my teammates"

      # Embed the query
      query_emb = co.embed(
          model="YOUR_MODEL_NAME",
          input_type="search_query",
          texts=[query],
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      # Add the user query
      query = "Ways to connect with my teammates"

      query_emb = co.embed(
          model="embed-v4.0",
          input_type="search_query",
          texts=[query],
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      # Add the user query
      query = "Ways to connect with my teammates"

      query_emb = co.embed(
          model="embed-v4.0",
          input_type="search_query",
          texts=[query],
          embedding_types=["float"],
      ).embeddings.float
      ```
    </Tab>
  </Tabs>

  ### Semantic Search

  Then, perform semantic search by computing the similarity between the query embedding and the document embeddings, and then returning the most similar documents.

  ```python PYTHON
  import numpy as np


  # Compute dot product similarity and display results
  def return_results(query_emb, doc_emb, documents):
      n = 2  # customize your top N results
      scores = np.dot(query_emb, np.transpose(doc_emb))[0]
      max_idx = np.argsort(-scores)[:n]

      for rank, idx in enumerate(max_idx):
          print(f"Rank: {rank+1}")
          print(f"Score: {scores[idx]}")
          print(f"Document: {documents[idx]}\n")


  return_results(query_emb, doc_emb, documents)
  ```

  ```mdx wordWrap
  Rank: 1
  Score: 0.262197161387274
  Document: Joining Slack Channels: Be sure to join relevant channels to stay informed and engaged.

  Rank: 2
  Score: 0.1266074257723145
  Document: Working Hours Flexibility: While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.
  ```
</Steps>

## Further Resources

* [Embed endpoint API reference](https://docs.cohere.com/reference/embed)
* [Documentation on embeddings](https://docs.cohere.com/docs/embeddings)
* [LLM University module on semantic search](https://cohere.com/llmu#semantic-search)


# Reranking - quickstart

> A quickstart guide for performing reranking with Cohere's Reranking models (v2 API).

Cohere's reranking models are available via the Rerank endpoint. This endpoint provides a powerful semantic boost to the search quality of any keyword or vector search system.

This quickstart guide shows you how to perform reranking with the Rerank endpoint.

<Steps>
  ### Setup

  First, install the Cohere Python SDK with the following command.

  ```bash
  pip install -U cohere
  ```

  Next, import the library and create a client.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          "COHERE_API_KEY"
      )  # Get your free API key here: https://dashboard.cohere.com/api-keys
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="",  # Leave this blank
          base_url="<YOUR_DEPLOYMENT_URL>",
      )
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      import cohere

      co = cohere.BedrockClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )

      # Get the model name: https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      import cohere

      co = cohere.SagemakerClientV2(
          aws_region="AWS_REGION",
          aws_access_key="AWS_ACCESS_KEY_ID",
          aws_secret_key="AWS_SECRET_ACCESS_KEY",
          aws_session_token="AWS_SESSION_TOKEN",
      )
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      import cohere

      co = cohere.ClientV2(
          api_key="AZURE_API_KEY",
          base_url="AZURE_ENDPOINT",
      )
      ```
    </Tab>
  </Tabs>

  ### Retrieved Documents

  First, define the list of documents to be reranked.

  ```python PYTHON
  documents = [
      "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward.",
      "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.",
      "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.",
      "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.",
  ]
  ```

  ### Reranking

  Then, perform reranking by passing the documents and the user query to the Rerank endpoint.

  <Tabs>
    <Tab title="Cohere Platform">
      ```python PYTHON
      # Add the user query
      query = "Are there fitness-related perks?"

      # Rerank the documents
      results = co.rerank(
          model="rerank-v3.5", query=query, documents=documents, top_n=2
      )

      for result in results.results:
          print(result)
      ```
    </Tab>

    <Tab title="Private Deployment">
      ```python PYTHON
      # Add the user query
      query = "Are there fitness-related perks?"

      # Rerank the documents
      results = co.rerank(
          model="rerank-v3.5", query=query, documents=documents, top_n=2
      )

      for result in results.results:
          print(result)
      ```
    </Tab>

    <Tab title="Bedrock">
      ```python PYTHON
      # Add the user query
      query = "Are there fitness-related perks?"

      # Rerank the documents
      results = co.rerank(
          model="YOUR_MODEL_NAME", query=query, documents=documents, top_n=2
      )

      for result in results.results:
          print(result)
      ```
    </Tab>

    <Tab title="SageMaker">
      ```python PYTHON
      # Add the user query
      query = "Are there fitness-related perks?"

      # Rerank the documents
      results = co.rerank(
          model="YOUR_ENDPOINT_NAME",
          query=query,
          documents=documents,
          top_n=2,
      )

      for result in results.results:
          print(result)
      ```
    </Tab>

    <Tab title="Azure AI">
      ```python PYTHON
      # Add the user query
      query = "Are there fitness-related perks?"

      # Rerank the documents
      results = co.rerank(
          model="model",  # Pass a dummy string
          query=query,
          documents=documents,
          top_n=2,
      )

      for result in results.results:
          print(result)
      ```
    </Tab>
  </Tabs>

  ```mdx wordWrap
  document=None index=2 relevance_score=0.115670934
  document=None index=1 relevance_score=0.01729751
  ```
</Steps>

## Further Resources

* [Rerank endpoint API reference](https://docs.cohere.com/reference/rerank)
* [Documentation on reranking](https://docs.cohere.com/docs/rerank-overview)
* [LLM University chapter on reranking](https://cohere.com/llmu/reranking)


# An Overview of the Developer Playground

> The Cohere Playground is a powerful visual interface for testing Cohere's generation and embedding language models without coding.

The [Cohere Playground](https://dashboard.cohere.com/playground) is a visual interface supporting two models:

* [Chat](https://docs.cohere.com/reference/chat)
* [Embed](https://docs.cohere.com/reference/embed)

It's a great way to test our models for specific use cases without writing code; when you're ready to start building, simply click `View Code` to get the underlying logic to add to your application.

## Using the Playground

In the next few sections, we'll walk through how to interact with both supported models via the Playground.

### Chat

The [Chat endpoint](https://docs.cohere.com/reference/chat) provides a response (i.e. language or code) to a prompt. You can use the Chat Playground to generate text or code, answer a question, or create content. It looks like this:

<img src="file:b7ccf357-724b-4ff4-9fb1-8debf3e75066" />

Your message goes in the `Message...` box at the bottom, and you can pass a message by hitting `Enter` or by clicking the `Send` button.

You can customize the model's behavior with the `System message`, which is a prompt that guides the model as it generates output. You can learn more about how to craft an effective system message in our [dedicated guide](https://docs.cohere.com/docs/preambles).

To customize further *within* the Playground, you can use the panel on the right:

<img src="file:e91b179d-e1da-4e80-b87d-05c90f0883e6" />

Here's what's available:

* `Model`: Choose from a list of our generation models (we recommend `command-a-03-2025`, the default).
* `Functions`: Function calling allows developers to connect models to external functions like APIs, databases, etc., take actions in them, and return results for users to interact with. Learn more in [tool use](https://docs.cohere.com/docs/tool-use) docs.
* `JSON Mode`: This is part of Cohere's [structured output](https://docs.cohere.com/docs/structured-outputs) functionality. When enabled, the model's response will be a JSON object that matched the schema that you have supplied. Learn more in [JSON mode](https://docs.cohere.com/docs/parameter-types-in-json).
* Under `Advanced Parameters`, you can customize the `temperature` and `seed`. A higher temperature will make the model more creative, while a lower temperature will make the model more focused and deterministic, and seed can help you keep outputs consistent. Learn more [here](https://docs.cohere.com/docs/predictable-outputs).
* Under `Advanced Parameters`, you'll also see the ability to turn on reasoning. This will cause the model to consider the implications of its response and provide a justification for its output. More information will be available as we continue to roll out this feature.

### Embed

The [Embed](https://docs.cohere.com/reference/embed) model enables users to create numerical representations for strings, which comes in handy for semantic search, topic modeling, classification tasks, and many other workflows. You can use the Embed Playground to test this functionality, and it looks like this:

<img src="file:15e519bc-ef61-4273-b6ab-badaf8db8ae6" />

To create embeddings through the Playground, you can either use `Add input` to feed the model your own strings, or you can use `Upload a file`. If you select `Run`, you'll see the two-dimensional visualization of the strings in the `OUTPUT` box.

As with Chat, the Playground's Embed model interface offers a side panel where you can further customize the model:

<img src="file:422d1062-10bc-42ea-81af-fd56ff82c80d" />

Here's what's available:

* `Model`: Choose from a list of our embedding models (we recommend `embed-v4.0`, the default).
* `Truncate`: This allows you to specify how the API will handle inputs longer than the maximum token length.

## Next Steps

As mentioned, once you've roughed out an idea you can use `View Code` to get the logic. If you want to explore further, check out our:

* [Models page](https://docs.cohere.com/docs/models)
* [Text Generation](https://docs.cohere.com/docs/introduction-to-text-generation-at-cohere) docs
* [Embeddings](https://docs.cohere.com/docs/embeddings) docs
* [API](https://docs.cohere.com/reference/about) reference
* [Integrations](https://docs.cohere.com/docs/integrations) page
* [Cookbooks](https://docs.cohere.com/docs/cookbooks)


# Frequently Asked Questions About Cohere

> Cohere is a powerful platform for using Large Language Models (LLMs). This page covers FAQs related to functionality, pricing, troubleshooting, and more.

Here, we'll walk through some common questions we get about how Cohere's models work, what pricing options there are, and more!

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

## Model Deployment

<AccordionGroup>
  <Accordion title="What Cohere models can I access via my cloud provider?">
    You can find the updated cloud support listed in our [documentation](https://docs.cohere.com/v1/docs/cohere-works-everywhere). Check out links to our models on [AWS Bedrock](https://aws.amazon.com/bedrock/cohere-command-embed/), [AWS SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0), [Azure AI](https://ai.azure.com/explore/models?selectedCollection=cohere), and [OCI Generative AI](https://www.oracle.com/artificial-intelligence/generative-ai/generative-ai-service/features/#models).
  </Accordion>

  <Accordion title="What are the options and availability for on-premises deployment of Cohere's models?">
    We have the ability to deploy all of our models privately. To learn more, please reach out to the sales team [using this form](https://cohere.com/contact-sales).
  </Accordion>

  <Accordion title="Can I get an enterprise license for on-premise deployment of Cohere models for commercial use, and are there any options for self-deployment?">
    Please reach out to the sales team to learn more.
  </Accordion>

  <Accordion title="What are the deployment options and considerations for Cohere models?">
    To learn more, please reach out to the sales team [using this form](https://cohere.com/contact-sales).
  </Accordion>

  <Accordion title="Is the licensing for self-deployed models non-commercial or research-only?">
    The default license for our open weights is for non-commercial use. For information about licensing please reach out to the sales team [using this form](https://cohere.com/contact-sales).
  </Accordion>

  <Accordion title="What are the requirements, resources, and methods needed to deploy Cohere models, especially when dealing with specific use cases, confidentiality, and resource constraints?">
    Please check our deployment options [here](https://cohere.com/deployment-options) and contact our sales team [with this form](https://cohere.com/contact-sales) to learn more.
  </Accordion>
</AccordionGroup>

## Platform & API

<AccordionGroup>
  <Accordion title="How can I monitor and manage my API usage limits, and what steps can I take if I need higher limits or encounter issues with my current limits?">
    We offer two kinds of API keys: trial keys (with a variety of attendant limitations), and production keys (which have no such limitations). You can learn about them in [this section](https://docs.cohere.com/docs/rate-limits) of our documentation.
  </Accordion>

  <Accordion title="How can I access Cohere API for personal projects and prototyping?">
    We make a distinction between “trial” and “production” usage of an API key.

    Trial API key usage is free, [but limited](https://docs.cohere.com/docs/rate-limits). You can test different applications or build proofs of concept using all of Cohere’s models and APIs with a trial key by simply signing up for a Cohere account [here](https://dashboard.cohere.com/welcome/register).
  </Accordion>

  <Accordion title="What are the rate limits for different Cohere API endpoints and plan types, and are there any differences in response times?">
    Please refer to [API Keys and Rate Limits section](https://docs.cohere.com/v1/docs/rate-limits) of our documentation.
  </Accordion>

  <Accordion title="Is there a way to provide feedback, ask questions, or report issues directly to the Cohere team or community?">
    You can contact our support team at [support@cohere.com](mailto:support@cohere.com) and get help and share your feedback with our team and developer community via the [Cohere Discord server](https://discord.gg/co-mmunity).
  </Accordion>
</AccordionGroup>

## Getting Started

<AccordionGroup>
  <Accordion title="How do I use the Cohere API?">
    The Cohere API can be accessed through the SDK. We support SDKs in 4 different languages, Python, Typescript, Java, and Go.

    Visit the [API docs](https://docs.cohere.com/reference/about) for further details.
  </Accordion>

  <Accordion title="Where can I access Cohere's Chatbot Playground or Dashboard?">
    Here are the relevant links:

    * [Dashboard](https://dashboard.cohere.com/)
  </Accordion>

  <Accordion title="Where can I find a comprehensive overview and resources about Cohere's products, use cases, and various offerings?">
    You can find the resources as follows:

    * Model pages: [Command](https://cohere.com/command), [Embed](https://cohere.com/embed), and [Rerank](https://cohere.com/rerank).
    * [For business](https://cohere.com/business)
    * [Cohere documentation](https://docs.cohere.com/)
  </Accordion>

  <Accordion title="Where can I find resources to start learning and building on Cohere?">
    For learning, we recommend our [LLM University](https://cohere.com/llmu) hub resources, which have been prepared by Cohere experts. These include a number of very high-quality, step-by-step guides to help you start building quickly.

    For building, we recommend checking out our [Github Notebooks](https://github.com/cohere-ai/notebooks), as well as the [Get Started](https://docs.cohere.com/docs/the-cohere-platform) and [Cookbooks](https://docs.cohere.com/page/cookbooks) sections in our documentation.
  </Accordion>

  <Accordion title="Where can I access and try out Cohere's Command model and its related tools?">
    You can access Command with tools using our [Chat](https://chat.cohere.com/) demo environment, [Developer Playground](https://dashboard.cohere.com/playground/chat), and [Chat API](https://docs.cohere.com/docs/chat-api).
  </Accordion>

  <Accordion title="What are some best practices and techniques for prompt engineering, specifically when incorporating documents into a chat model's response?">
    For general recommendations on prompt engineering check the following resources:

    * [Prompt Engineering Basics](https://cohere.com/llmu/prompt-engineering-basics) Guide
    * Tips on [Crafting Effective Prompts](https://docs.cohere.com/v1/docs/crafting-effective-prompts)
    * Techniques of [Advanced Prompt Engineering](https://docs.cohere.com/v1/docs/advanced-prompt-engineering-techniques).

    For the most reliable results when working with external document sources, we recommend using a technique called Retrieval-Augmented Generation (RAG). You can learn about it here:

    * [Getting Started With Retrieval-Augmented Generation](https://cohere.com/llmu/rag-start)
    * [Cohere documentation](https://docs.cohere.com/v1/docs/retrieval-augmented-generation-rag) on RAG
  </Accordion>

  <Accordion title="Where can I find code examples and tutorials for using the Cohere API with various programming languages and frameworks?">
    You can find a list of comprehensive tutorials and code examples in our [LLM University](https://cohere.com/llmu) hub and the [Cookbook](https://docs.cohere.com/v1/page/cookbooks) guides.
  </Accordion>

  <Accordion title="What are some project ideas or suggestions for developers using Cohere models?">
    Check out our [Cookbooks](https://docs.cohere.com/v1/page/cookbooks), which include step-by-step guides and project examples, and the [Cohere Discord server](https://discord.gg/co-mmunity) for inspiration from our developer community.
  </Accordion>

  <Accordion title="How can I access LLM University?">
    LLMU can be accessed directly from the [Cohere website](https://cohere.com/llmu). We periodically add more content and highly recommend you follow us on our socials to stay up to date.
  </Accordion>

  <Accordion title="Where can I find the documentation for Cohere's models and features?">
    You can find the documentation with the full Cohere model and feature overview [here](https://docs.cohere.com/).
  </Accordion>
</AccordionGroup>

## Troubleshooting Errors

<AccordionGroup>
  <Accordion title="When using Cohere's API, why am I encountering errors related to dataset creation, API key limitations, or missing artifacts, and how can these issues be resolved?">
    Here are some common errors and potential solutions for dealing with errors related to API key limitations or missing artifacts.

    #### API Key Limitations

    Cohere's API keys have certain limitations and permissions associated with them. If you are encountering errors related to API key limitations, it could be due to the following reasons:

    * Rate Limits: Cohere's API has rate limits in place to ensure fair usage. If you exceed the allowed number of requests within a specific time frame, you may receive an error. To resolve this, double check the rate limits for your API plan and ensure your usage is within the specified limits. You can also implement a rate-limiting mechanism in your code to control the frequency of API requests.
    * API Key Expiration: API keys may have an expiration date. If your key has expired, it will no longer work.Check the validity period of your API key and renew it if necessary. Contact Cohere's support team if you need assistance with key renewal.

    #### Missing Artifacts

    Cohere's dataset creation process involves generating artifacts, which are essential components for training models. If you receive errors about missing artifacts, consider the following:

    * Incorrect Dataset Format: Ensure your dataset is in the correct format required by Cohere's API. Different tasks (e.g., classification, generation) may have specific formatting requirements. Review the documentation for dataset formatting guidelines and ensure your data adheres to the specified structure.
    * File Upload Issues: Artifacts are generated after successfully uploading your dataset files. Issues with file uploads can lead to missing artifacts. Verify that your dataset files are accessible and not corrupted. You should also check file size limits to ensure your files meet the requirements.
    * Synchronization Delay: Sometimes, there might be a slight delay in generating artifacts after uploading the dataset. Wait for a few minutes and refresh the dataset status to see if the artifacts are generated.

    #### General Troubleshooting Steps

    If your problem doesn't fall into these buckets, here are a few other things you can try:

    * Check API Documentation: Review the Cohere [API documentation](https://docs.cohere.com/reference/about) for dataset creation to ensure you are following the correct steps and parameters.
    * Inspect API Responses: Carefully examine the error responses returned by the API. They often contain valuable information about the issue. Cohere uses conventional HTTP response codes to indicate the success or failure of an API request. In general:
      * Codes in the 2xx range indicate success.
      * Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.).
      * Codes in the 5xx range indicate an error with Cohere’s servers (these are rare).

    Review the [Errors page](https://docs.cohere.com/reference/errors) to learn more about how to deal with non-2xx response code.

    #### Reach Out to Cohere Support

    If the issue persists, contact Cohere's support team. They can provide personalized assistance and help identify any specific problems with your API integration.
  </Accordion>

  <Accordion title="Why am I unable to access and log in to the Cohere dashboard?">
    If you're encountering difficulties logging into your Cohere dashboard, there could be a few reasons.

    First, check our status page at status.cohere.com to see if any known issues or maintenance activities might impact your access.

    If the status page doesn't indicate any ongoing issues, the next step would be to reach out to our support teams. They're always ready to assist and can be contacted at [support@cohere.com](mailto:support@cohere.com). Our support team will be able to investigate further and provide you with the necessary guidance to resolve the login issue.
  </Accordion>

  <Accordion title="How can I resolve issues with logging in and authentication?">
    We understand that login and authentication issues can be frustrating. Here are some steps you can take to troubleshoot and resolve these problems:

    * Check Your Credentials: Ensure you use the correct username and password. It's easy to make a typo, so double-check your credentials before logging in again.
    * Clear Cache and Cookies: Sometimes, issues with logging in can be caused by cached data or cookies on your device. Try clearing your browser's cache and cookies, then attempt to log in again.
    * Contact Support: If none of the above steps resolve the issue, it's time to contact our support team. We are equipped to handle a wide range of login and authentication issues and can provide further assistance. You can contact us at [support@cohere.com](mailto:support@cohere.com).
  </Accordion>

  <Accordion title="What troubleshooting steps would you suggest for an issue suddenly occurring in a previously functional system or script?">
    If you're facing any technical challenges or need guidance, our support team is here to help. Contact us at [support@cohere.com](mailto:support@cohere.com), and our technical support engineers will provide the necessary assistance and expertise to resolve your issues.
  </Accordion>
</AccordionGroup>

## Billing, Pricing, Licensing, Account Management

<AccordionGroup>
  <Accordion title="How can I get in touch with Cohere's support team?">
    Please reach out to our support team at [support@cohere.com](mailto:support@cohere.com). When reaching out to the support team, please keep the following questions in mind:

    * What model are you referring to?
    * Copy paste the error message
      * Please note that this is our error message information:
        * 400 - invalid combination of parameters
        * 422 - request is malformed (eg: unsupported enum value, unknown param)
        * 499 - request is canceled by the user
        * 401 - invalid api token (not relevant on AWS)
        * 404 - model not found (not relevant on AWS)
        * 429 - rate limit reached (not relevant on AWS)
    * What is the request seq length you are passing in?
    * What are the generation max tokens you are requesting?
    * Are all the requests of various input/output shapes failing?
    * Share any logs
  </Accordion>

  <Accordion title="Where can I find information about Cohere's pricing?">
    Please refer to our dedicated pricing page for most up-to-date [pricing](https://cohere.com/pricing).
  </Accordion>

  <Accordion title="How can I manage and understand the rate limits and usage of my API key?">
    Cohere offers two types of API keys: trial keys and production keys.

    *Trial Key Limitations*

    Trial keys are rate-limited depending on the endpoint you want to use. For example, the Embed endpoint is limited to 5 calls per minute, while the Chat endpoint is limited to 20 calls per minute. All other endpoints on trail keys are 1,000 calls per month.
    If you want to use Cohere endpoints in a production application or require higher throughput, you can upgrade to a production key.

    *Production Key Specifications*

    Production keys for all endpoints are rate-limited at 1,000 calls per minute, with unlimited monthly use and are intended for serving Cohere in a public-facing application and testing purposes. Usage of production keys is metered at price points which can be found on the Cohere [pricing page](https://cohere.com/pricing).

    To get a production key, you'll need to be the admin of your organization or ask your organization's admin to create one. Please visit your [API Keys](https://dashboard.cohere.com/api-keys) > [Dashboard](https://dashboard.cohere.com/), where the process should take less than three minutes and will generate a production key that you can use to serve Cohere APIs in production.
  </Accordion>

  <Accordion title="How can I monitor and manage my token usage and API calls for personal projects within the limitations of a free plan?">
    Cohere offers a convenient way to keep track of your usage and billing information. All our endpoints provide this data as metadata for each conversation, which is directly accessible via the API. This ensures you can easily monitor your usage.
    Our Dashboard provides an additional layer of control for standard accounts. You can set a monthly spending limit to manage your expenses effectively. To learn more about this feature and how to enable it, please visit the Billing & Usage section on the Dashboard, specifically the [Spending Limit](https://dashboard.cohere.com/billing?tab=spending-limit) tab.
  </Accordion>

  <Accordion title="What is the process for making changes to my account, and who should I contact for specific requests?">
    If you need to make changes to your account or have specific requests, Cohere has a straightforward process. All the essential details about your account can be found under the [Dashboard](https://dashboard.cohere.com). This is a great starting point for any account-related queries.

    However, if you have a request that requires further assistance or if the changes you wish to make are not covered by the Dashboard, our support team is here to help. Please feel free to reach out directly at [support@cohere.com](mailto:support@cohere.com) or ask your question in our [Discord community](https://discord.gg/co-mmunity).
  </Accordion>

  <Accordion title="How can I get in touch with Cohere support to discuss plan options and pricing?">
    Please reach out to our Sales team at [sales@cohere.com](mailto:sales@cohere.com)
  </Accordion>

  <Accordion title="How is the cost of using Cohere's API calculated and what factors influence the number of billed tokens?">
    Cohere's API pricing is based on a simple and transparent token-based model. The cost of using the API is calculated based on the number of tokens consumed during the API calls.

    Check our [pricing page](https://cohere.com/pricing) for more information.
  </Accordion>

  <Accordion title="What are the rate limits for the free trial API, and how is the monthly limit calculated?">
    Trial keys are rate-limited depending on the endpoint you want to use, and the monthly limit is 1000 calls per month.

    Check our [free trial documentation](https://docs.cohere.com/docs/rate-limits#trial-key-limitations) for more information.
  </Accordion>

  <Accordion title="Is it possible for a small startup or any commercial entity to use Cohere's technology for production or commercial purposes, and if so, what licenses or permissions are required?">
    Absolutely! Cohere's platform empowers businesses, including startups, to leverage our technology for production and commercial purposes.

    In terms of usage guidelines, we've compiled a comprehensive set of resources to ensure a smooth and compliant experience. You can access these guidelines [here](https://docs.cohere.com/docs/usage-guidelines).

    We're excited to support your business and its unique needs. If you have any further questions or require additional assistance, please don't hesitate to reach out to our team at [sales@cohere.com](mailto:sales@cohere.com) or [support@cohere.com](mailto:support@cohere.com) for more details.
  </Accordion>

  <Accordion title="How can I manage my Cohere account, specifically regarding deletion, team invitations, and account merging?">
    You can access all the necessary tools and information through your account's dashboard [here](https://dashboard.cohere.com/team).

    If you're unable to find the specific feature or information regarding merging accounts, our support team is always eager to help.

    Simply start a new chat with them using the chat bubble on our website or reach out via email to [support@cohere.com](mailto:support@cohere.com).
  </Accordion>

  <Accordion title="How does the token limit work for multiple documents in a single query?">
    The token limit for multiple documents in a single query can vary depending on the model or service you're using. For instance, our Chat Model has a long-context window of 128k tokens. This means that as long as the combined length of your input and output tokens stays within this limit, the number of documents you include in your query shouldn't be an issue.

    It's important to note that different models may have different token and document limits. To ensure you're working within the appropriate parameters, we've provided detailed information about these limits for each model in [this](https://docs.cohere.com/docs/models) model overview section.

    We understand that managing token limits can be a crucial aspect of your work, and we're here to support you in navigating these considerations effectively. If you have any further questions or require additional assistance, please don't hesitate to reach out to our team at [support@cohere.com](mailto:support@cohere.com)
  </Accordion>

  <Accordion title="What are the pricing plans and models available for Cohere's API endpoints, and are there any additional costs associated with specific features or workflows?">
    Please find the pricing information about our model and services [here](https://cohere.com/pricing).

    Should you have any further questions please feel free to reach out to our sales team at [sales@cohere.com](mailto:sales@cohere.com) or [support@cohere.com](mailto:support@cohere.com) for more details.
  </Accordion>
</AccordionGroup>

## Legal, Security, Data Privacy

<AccordionGroup>
  <Accordion title="Is my data private and secure when using Cohere platform, or is it accessible to others?">
    When you’re using Cohere models via our Platform, we segment your data using logical segmentation. When using Cohere models via a private or cloud deployment from one of our partners, your data is not shared with Cohere.
  </Accordion>

  <Accordion title="Could you provide more specific information about your GDPR compliance practices and policies, including any relevant documentation, so that I can forward the details to our legal team for review?">
    We support our enterprise customers’ privacy and data security compliance needs by offering multiple deployment options so customers can control access to data and personal information under their control. Seamlessly complete your privacy and security compliance reviews by visiting Cohere’s [Trust Center](https://cohere-inc.secureframetrust.com/) where you can request a copy of our SOC 2 Type II Report, and review our privacy documentation and other compliance resources.
  </Accordion>

  <Accordion title="How can we ensure we follow best practices to secure our system using Cohere, and how can we communicate that to our clients when they raise concerns about potential vulnerabilities associated with using AI?">
    When it comes to using AI models securely, two important areas stand out.

    #### 1. Model Security and Safety

    This responsibility lies primarily with the model provider, and at Cohere, we are deeply committed to ensuring responsible AI development. Our team includes some of the top experts in AI security and safety. We lead through various initiatives, including governance and compliance frameworks, safety and security protocols, strict data controls for model training, and industry thought leadership.

    #### 2. Secure Application Development with Cohere Models:

    While Cohere ensures the model's security, customers are responsible for building and deploying applications using these models securely. A strong focus on a Secure Product Lifecycle is essential, and our models integrate seamlessly into this process. Core security principles remain as relevant in the AI space as elsewhere. For example, robust authentication protocols should exist for all users, services, and micro-services. Secrets, tokens, and credentials must be tightly controlled and regularly monitored.

    #### Our recommendations:

    * Implement responsible AI and governance policies in your AI development process, focusing on customer safety and security.
    * Continuously monitor the performance of your applications and promptly address any issues that arise.

    We also regularly share insights and best practices on AI security on our blog. Here are a few examples: [1](https://cohere.com/blog/how-generative-ai-has-changed-security-2), [2](https://cohere.com/blog/tackling-ai-security-risks-with-eyes-wide-open), [3](https://cohere.com/blog/building-robust-enterprise-ai-solutions-insights-on-llm-performance-safety-and-future-trends).
  </Accordion>

  <Accordion title="What if I have more questions?">
    If there's anything not covered in this document, you're welcome to reach to us with [this form](https://forms.gle/Mwbn42rrv5vokwFg6).
  </Accordion>
</AccordionGroup>


# An Overview of Cohere's Models

> Cohere has a variety of models that cover many different use cases. If you need more customization, you can train a model to tune it to your specific use case.

Cohere has a variety of models that cover many different use cases. If you need more customization, you can [train a model](/docs/fine-tuning) to tune it to your specific use case.

Cohere models are currently available on the following platforms:

* [Cohere’s proprietary platform](https://dashboard.cohere.com/playground/chat)
* [Amazon SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0)
* [Amazon Bedrock](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#/providers?model=cohere.command-r-plus-v1:0)
* [Microsoft Azure](https://ai.azure.com/explore/models/?tid=694fed05-7f6d-4ab2-8c38-9afb438eab6f\&selectedCollection=cohere)
* [Oracle GenAI Service](https://www.oracle.com/artificial-intelligence/generative-ai/generative-ai-service/)

At the end of each major section below, you'll find technical details about how to call a given model on a particular platform.

## What can These Models Be Used For?

In this section, we'll provide some high-level context on Cohere's offerings, and what the strengths of each are.

* The Command family of models includes [Command A](https://docs.cohere.com/docs/command-a), [Command R7B](https://docs.cohere.com/docs/command-r7b), [Command A Translate](https://docs.cohere.com/docs/command-a-translate), [Command A Reasoning](https://docs.cohere.com/docs/command-a-reasoning), [Command A Vision](https://docs.cohere.com/docs/command-a-vision), [Command R+](/docs/command-r-plus), [Command R](/docs/command-r), and [Command](https://cohere.com/models/command?_gl=1*15hfaqm*_ga*MTAxNTg1NTM1MS4xNjk1MjMwODQw*_ga_CRGS116RZS*MTcxNzYwMzYxMy4zNTEuMS4xNzE3NjAzNjUxLjIyLjAuMA..). Together, they are the text-generation LLMs powering tool-using agents, [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG), translation, copywriting, and similar use cases. They work through the [Chat](/reference/chat) endpoint, which can be used with or without RAG.
* [Rerank](https://cohere.com/blog/rerank/?_gl=1*1t6ls4x*_ga*MTAxNTg1NTM1MS4xNjk1MjMwODQw*_ga_CRGS116RZS*MTcxNzYwMzYxMy4zNTEuMS4xNzE3NjAzNjUxLjIyLjAuMA..) is the fastest way to inject the intelligence of a language model into an existing search system. It can be accessed via the [Rerank](/reference/rerank-1) endpoint.
* [Embed](https://cohere.com/models/embed?_gl=1*1t6ls4x*_ga*MTAxNTg1NTM1MS4xNjk1MjMwODQw*_ga_CRGS116RZS*MTcxNzYwMzYxMy4zNTEuMS4xNzE3NjAzNjUxLjIyLjAuMA..) improves the accuracy of search, classification, clustering, and RAG results. It powers the [Embed](/reference/embed) endpoint.
* The [Aya](https://cohere.com/research/aya) family of models are aimed at expanding the number of languages covered by generative AI. Aya Expanse covers 23 languages, and Aya Vision is fully multimodal, allowing you to pass in images and text and get a single coherent response. Both are available on the [Chat](/reference/chat) endpoint.

## Command

Command is Cohere's default generation model that takes a user instruction (or command) and generates text following the instruction. Our Command models also have conversational capabilities, meaning they are well-suited for chat applications, and Command A Vision can interact with [image inputs](https://docs.cohere.com/docs/image-inputs).

| Model Name                    | Status                   | Description                                                                                                                                                                                                                                                                                                                                            | Modality     | Context Length | Maximum Output Tokens | Endpoints               |
| ----------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------------- | --------------------- | ----------------------- |
| `command-a-03-2025`           | Live                     | Command A is our most performant model to date, excelling at tool use, agents, retrieval augmented generation (RAG), and multilingual use cases. Command A has a context length of 256K, only requires two GPUs to run, and has 150% higher throughput compared to Command R+ 08-2024.                                                                 | Text         | 256k           | 8k                    | [Chat](/reference/chat) |
| `command-r7b-12-2024`         | Live                     | `command-r7b-12-2024` is a small, fast update delivered in December 2024. It excels at RAG, tool use, agents, and similar tasks requiring complex reasoning and multiple steps.                                                                                                                                                                        | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-a-translate-08-2025` | Live                     | Command A Translate is Cohere’s state of the art machine translation model, excelling at a variety of translation tasks on 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Chinese, Arabic, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian. | Text         | 8K             | 8k                    | [Chat](/reference/chat) |
| `command-a-reasoning-08-2025` | Live                     | Command A Reasoning is Cohere's first reasoning model, able to 'think' before generating an output in a way that allows it to perform well in certain kinds of nuanced problem-solving and agent-based tasks in 23 languages.                                                                                                                          | Text         | 256k           | 32k                   | [Chat](/reference/chat) |
| `command-a-vision-07-2025`    | Live                     | Command A Vision is our first model capable of processing images, excelling in enterprise use cases such as analyzing charts, graphs, and diagrams, table understanding, OCR, document Q\&A, and object detection. It officially supports English, Portuguese, Italian, French, German, and Spanish.                                                   | Text, Images | 128K           | 8K                    | [Chat](/reference/chat) |
| `command-r-08-2024`           | Live                     | `command-r-08-2024` is an update of the Command R model, delivered in August 2024. Find more information [here](https://docs.cohere.com/changelog/command-gets-refreshed)                                                                                                                                                                              | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-r-plus-08-2024`      | Live                     | `command-r-plus-08-2024` is an update of the Command R+ model, delivered in August 2024. Find more information [here](https://docs.cohere.com/changelog/command-gets-refreshed)                                                                                                                                                                        | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-r-03-2024`           | Deprecated Sept 15, 2025 | Command R is an instruction-following conversational model that performs language tasks at a higher quality, more reliably, and with a longer context than previous models. It can be used for complex workflows like code generation, retrieval augmented generation (RAG), tool use, and agents.                                                     | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-r-plus-04-2024`      | Deprecated Sept 15, 2025 | Command R+ is an instruction-following conversational model that performs language tasks at a higher quality, more reliably, and with a longer context than previous models. It is best suited for complex RAG workflows and multi-step tool use.                                                                                                      | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-r-plus`              | Deprecated Sept 15, 2025 | Alias for `command-r-plus-04-2024`                                                                                                                                                                                                                                                                                                                     | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-r`                   | Deprecated Sept 15, 2025 | Alias for `command-r-03-2024`                                                                                                                                                                                                                                                                                                                          | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `command-light`               | Deprecated Sept 15, 2025 | A smaller, faster version of `command`. Almost as capable, but a lot faster.                                                                                                                                                                                                                                                                           | Text         | 4k             | 4k                    | [Chat](/reference/chat) |
| `command`                     | Deprecated Sept 15, 2025 | An instruction-following conversational model that performs language tasks with high quality, more reliably and with a longer context than our base generative models.                                                                                                                                                                                 | Text         | 4k             | 4k                    | [Chat](/reference/chat) |

### Using Command Models on Different Platforms

In this table, we provide some important context for using Cohere Command models on Amazon Bedrock, Amazon SageMaker, and more.

| Model Name              | Amazon Bedrock Model ID         | Amazon SageMaker      | Azure AI Foundry      | Oracle OCI Generative AI Service |
| :---------------------- | :------------------------------ | :-------------------- | :-------------------- | :------------------------------- |
| `command-a-03-2025`     | (Coming Soon)                   | Unique per deployment | Unique per deployment | `cohere.command-a-03-2025`       |
| `command-r7b-12-2024`   | N/A                             | N/A                   | N/A                   | N/A                              |
| `command-r-plus`        | `cohere.command-r-plus-v1:0`    | Unique per deployment | Unique per deployment | `cohere.command-r-plus v1.2`     |
| `command-r`             | `cohere.command-r-v1:0`         | Unique per deployment | Unique per deployment | `cohere.command-r-16k v1.2`      |
| `command`               | `cohere.command-text-v14`       | N/A                   | N/A                   | `cohere.command v15.6`           |
| `command-nightly`       | N/A                             | N/A                   | N/A                   | N/A                              |
| `command-light`         | `cohere.command-light-text-v14` | N/A                   | N/A                   | `cohere.command-light v15.6`     |
| `command-light-nightly` | N/A                             | N/A                   | N/A                   | N/A                              |

## Embed

These models can be used to generate embeddings from text or classify it based on various parameters. Embeddings can be used for estimating semantic similarity between two sentences, choosing a sentence which is most likely to follow another sentence, or categorizing user feedback. The Representation model comes with a variety of helper functions, such as for detecting the language of an input.

| Model Name                      | Description                                                                                                               | Modalities                                   | Dimensions                                 | Context Length | Similarity Metric                                             | Endpoints                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------ | -------------- | ------------------------------------------------------------- | --------------------------------------------------------------------- |
| `embed-v4.0`                    | A model that allows for text and images to be classified or turned into embeddings                                        | Text, Images, Mixed texts/images (i.e. PDFs) | One of '\[256, 512, 1024, 1536 (default)]' | 128k           | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-v3.0`            | A model that allows for text to be classified or turned into embeddings. English only.                                    | Text, Images                                 | 1024                                       | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-light-v3.0`      | A smaller, faster version of `embed-english-v3.0`. Almost as capable, but a lot faster. English only.                     | Text, Images                                 | 384                                        | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-multilingual-v3.0`       | Provides multilingual classification and embedding support. [See supported languages here.](/docs/supported-languages)    | Text, Images                                 | 1024                                       | 512            | Cosine Similarity                                             | [Embed](/reference/embed), [Embed Jobs](/reference/embed-jobs)        |
| `embed-multilingual-light-v3.0` | A smaller, faster version of `embed-multilingual-v3.0`. Almost as capable, but a lot faster. Supports multiple languages. | Text, Images                                 | 384                                        | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |

### Using Embed Models on Different Platforms

In this table, we provide some important context for using Cohere Embed models on Amazon Bedrock, Amazon SageMaker, and more.

| Model Name                      | Amazon Bedrock Model ID        | Amazon SageMaker      | Azure AI Foundry        | Oracle OCI Generative AI Service                                                                             |
| :------------------------------ | :----------------------------- | :-------------------- | :---------------------- | :----------------------------------------------------------------------------------------------------------- |
| `embed-v4.0`                    | (Coming Soon)                  | Unique per deployment | `cohere-embed-v-4-plan` | (Coming Soon)                                                                                                |
| `embed-english-v3.0`            | `cohere.embed-english-v3`      | Unique per deployment | Unique per deployment   | `cohere.embed-english-image-v3.0` (for images), `cohere.embed-english-v3.0` (for text)                       |
| `embed-english-light-v3.0`      | N/A                            | Unique per deployment | N/A                     | `cohere.embed-english-light-image-v3.0` (for images), `cohere.embed-english-light-v3.0` (for text)           |
| `embed-multilingual-v3.0`       | `cohere.embed-multilingual-v3` | Unique per deployment | Unique per deployment   | `cohere.embed-multilingual-image-v3.0` (for images), `cohere.embed-multilingual-v3.0` (for text)             |
| `embed-multilingual-light-v3.0` | N/A                            | Unique per deployment | N/A                     | `cohere.embed-multilingual-light-image-v3.0` (for images), `cohere.embed-multilingual-light-v3.0` (for text) |
| `embed-english-v2.0`            | N/A                            | Unique per deployment | N/A                     | N/A                                                                                                          |
| `embed-english-light-v2.0`      | N/A                            | Unique per deployment | N/A                     | `cohere.embed-english-light-v2.0`                                                                            |
| `embed-multilingual-v2.0`       | N/A                            | Unique per deployment | N/A                     | N/A                                                                                                          |

## Rerank

The Rerank model can improve created models by re-organizing their results based on certain parameters. This can be used to improve search algorithms.

| Model Name                 | Description                                                                                                                                                                           | Modalities | Context Length | Endpoints                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------- | --------------------------- |
| `rerank-v3.5`              | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                        | Text       | 4k             | [Rerank](/reference/rerank) |
| `rerank-english-v3.0`      | A model that allows for re-ranking English Language documents and semi-structured data (JSON). This model has a context length of 4096 tokens.                                        | Text       | 4k             | [Rerank](/reference/rerank) |
| `rerank-multilingual-v3.0` | A model for documents and semi-structure data (JSON) that are not in English. Supports the same languages as embed-multilingual-v3.0. This model has a context length of 4096 tokens. | Text       | 4k             | [Rerank](/reference/rerank) |

### Using Rerank Models on Different Platforms

In this table, we provide some important context for using Cohere Rerank models on Amazon Bedrock, SageMaker, and more.

| Model Name                 | Amazon Bedrock Model ID | Amazon SageMaker      | Azure AI Foundry                | Oracle OCI Generative AI Service |
| :------------------------- | :---------------------- | :-------------------- | :------------------------------ | :------------------------------- |
| `rerank-v3.5`              | `cohere.rerank-v3-5:0`  | Unique per deployment | `Cohere-rerank-v3.5`            | `cohere.rerank.3-5`              |
| `rerank-english-v3.0`      | N/A                     | Unique per deployment | `Cohere-rerank-v3-english`      | N/A                              |
| `rerank-multilingual-v3.0` | N/A                     | Unique per deployment | `Cohere-rerank-v3-multilingual` | N/A                              |

<br />

<Note>
  Rerank accepts full strings rather than tokens, so the token limit works a little differently. Rerank will automatically chunk documents longer than 510 tokens, and there is therefore no explicit limit to how long a document can be when using rerank. See our [best practice guide](/docs/reranking-best-practices) for more info about formatting documents for the Rerank endpoint.
</Note>

## Aya

[Aya](https://cohere.com/research/aya) is a family of multilingual large language models designed to expand the number of languages covered by generative AI for purposes of research and to better-serve minority linguistic communities.

Its 8-billion and 32-billion parameter “Expanse” offerings are optimized to perform well in these 23 languages: Arabic, Chinese (simplified & traditional), Czech, Dutch, English, French, German, Greek, Hebrew, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Turkish, Ukrainian, and Vietnamese.

Its 8-billion and 32-billion parameter "Vision" models are state-of-the-art multimodal models excelling at a variety of critical benchmarks for language, text, and image capabilities.

| Model Name             | Description                                                                                                                                                                                                                                             | Modality     | Context Length | Maximum Output Tokens | Endpoints               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------- | --------------------- | ----------------------- |
| `c4ai-aya-expanse-8b`  | Aya Expanse is a highly performant 8B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages.                         | Text         | 8k             | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-expanse-32b` | Aya Expanse is a highly performant 32B multilingual model, designed to rival monolingual performance through innovations in instruction tuning with data arbitrage, preference training, and model merging. Serves 23 languages.                        | Text         | 128k           | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-vision-8b`   | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. This 8 billion parameter variant is focused on low latency and best-in-class performance.                   | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |
| `c4ai-aya-vision-32b`  | Aya Vision is a state-of-the-art multimodal model excelling at a variety of critical benchmarks for language, text, and image capabilities. Serves 23 languages. This 32 billion parameter variant is focused on state-of-art multilingual performance. | Text, Images | 16k            | 4k                    | [Chat](/reference/chat) |

### Using Aya Models on Different Platforms

Aya isn't available on other platforms, but it can be used with WhatsApp. Find more information [here](https://docs.cohere.com/docs/aya#aya-expanse-integration-with-whatsapp).


# Command A

> Command A is a performant mode good at tool use, RAG, agents, and multilingual use cases. It has 111 billion parameters and a 256k context length.

<ModelShowcase
  model={{
  name: 'Command A',
  id: 'command-a-03-2025',
  capabilities: [
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 2.50, output: 10.0 },
  specs: {
    contextWindow: '256,000',
    maxOutputTokens: '8,000',
    knowledgeCutoff: 'June 1, 2024',
    customSpecs: [
      {
        name: "Hardware",
        value: "Requires two GPUs to run (A100s / H100s)"
      }
    ]
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

Command A is Cohere's most performant model to date, excelling at real world enterprise tasks including tool use, retrieval augmented generation (RAG), agents, and multilingual use cases. At 111B parameters, Command A has a context length of 256K and only requires two GPUs (A100s / H100s) to run, while being significantly more efficient at inference time with 150% higher throughput compared to its predecessor, Command R+ 08-2024.

## What Can Command A Be Used For?

Command A is excellent for:

* Tool use - With [tool use](https://docs.cohere.com/docs/tool-use), Command models can be given tools such as search engines, APIs, vector databases, etc., which can expand their baseline functionality. Command A excels at tool use, exhibiting particular strength in using tools in real-world, diverse, and dynamic environments. In addition, Command A is good at avoiding unnecessarily calling tools, which is an important aspect of tool-use in practical applications.
* Agents - As this is being written, [agents](https://docs.cohere.com/docs/multi-step-tool-use) are among the most exciting frontiers for large language models. Command A’s multistep tool use capabilities allow it to power fast and capable REACT agents. When set up as an internet-augmented research agent, for example, Command A ably completes tasks that require breaking down complex questions into subgoals, and also performs favorably in domains that utilize complex reasoning and active information seeking.
* Retrieval augmented generation - [Retrieval Augmented Generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) refers to the practice of ‘grounding’ model outputs in external data sources, which can increase accuracy. Command A is exceptionally good at generating responses in conversational tasks, attending over long inputs, and extracting and manipulating numerical information in financial settings.
* Multilingual use cases - The model is trained to perform well in 23 languages: English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Chinese, Arabic, Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian. It has been trained to respond in the language of the user, or follow instructions to output a response in a different language. It also excels at performing cross-lingual tasks, such as translation or answering questions about content in other languages.

### Command A is Chatty

By default, the model is interactive and optimized for conversation, meaning it is verbose and uses markdown to highlight code. To override this behavior, developers should use a system instruction which asks the model to simply provide the answer and to not use markdown or code block markers. To learn more, consult our documentation on [system instructions](https://docs.cohere.com/docs/system-instructions).


# Cohere's Command A Reasoning Model

> Command A Reasoning excels in tool use, agentic workflows, and complex problem-solving. It has 111 billion parameters and a 256k context length.

<ModelShowcase
  model={{
  name: 'Command A Reasoning',
  id: 'command-a-reasoning-08-2025',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  specs: {
    contextWindow: '256,000',
    maxOutputTokens: '32,000',
    knowledgeCutoff: 'June 1, 2024',
    
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

Command A Reasoning is Cohere's first reasoning model to date, excelling at real world enterprise tasks including tool use, retrieval augmented generation (RAG), agents, and multilingual use cases. At 111B parameters, Command A has a context length of 256K, and can run on one or two GPUs (A100s / H100s).

## What Can Command A Reasoning Be Used For?

Command A is excellent for:

* **Agentic Use Cases**: Taking autonomous actions and interacting with the environment to solve problems.
* **Tool Use**: Able to leverage a variety of tools, such as search engines and APIs.
* **Multilingual**: Able to reason over multilingual inputs, providing support to user queries in 23 different languages.

There's more to be said about token budgets, enabling and disabling the `thinking` operation, etc., which can be found in our dedicated [Reasoning guide](/docs/reasoning).


# Cohere's Command A Translate Model

> Command A Translate is a state of the art model performant in 23 languages. It has a context length of 16K tokens and 111B parameters.

<ModelShowcase
  model={{
  name: 'Command A Translate',
  id: 'command-a-translate-08-2025',
  capabilities: [
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  specs: {
    contextWindow: '8,000',
    maxOutputTokens: '8,000',
    knowledgeCutoff: 'June 1, 2024',
    
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

Automated translation from one language to another is one of the oldest applications of machine learning. Today's LLMs have proven remarkably effective for these kinds of tasks, and Command A Translate is Cohere’s state of the art entry into the machine translation field. It delivers industry-leading performance on a variety of translation tasks across 23 languages, while offering enterprises full control of their data through private deployment options.

Command A Translate has a context length of 16K tokens (8K for input and 8K for output), 111B parameters, and can run on one or two GPUs (A100s / H100s).

## What Can Command A Translate be Used For?

Command A Translate is excellent for translation tasks where you need answers that combine high quality and a low error rate. When utilized as part of our [private deployment](https://docs.cohere.com/docs/private-deployment-overview) options, it is the best choice for enterprises wanting to translate data *securely*.

## Getting Started

You can perform translation of a text into another language with a simple prompt asking the model to translate a piece of text. In the sample below, we are doing this 'programmatically' by passing both the target language and content to translate as variables, but you can also just pass in a `message` saying `"Please translate this into <target_language> for me."`

```python PYTHON 
from cohere import ClientV2

co = ClientV2(api_key="<YOUR API KEY>")

target_language = "Spanish"
content_to_translate = "Enterprises rely on translation for some of their most sensitive and business-critical documents and cannot risk data leakage, compliance violations, or misunderstandings. Mistranslated documents can reduce trust and have strategic implications."

message = f"Translate everything that follows into {target_language}:\n\n{content_to_translate}"
response = co.chat(
    model="command-a-translate-08-2025",
    messages=[{"role": "user", "content": message}],
)
print(response.message.content[0].text)
```

Here’s a sample output:

```mdx
Las empresas dependen de la traducción para algunos de sus documentos más sensibles y críticos para su negocio y no pueden permitirse el riesgo de fugas de datos, incumplimientos normativos o malentendidos. Los documentos mal traducidos pueden reducir la confianza y tener implicaciones estratégicas.
```

## Conclusion

Command A Translate is great for one-shot translations but can also be embedded into more complicated workflows, such as translating long texts. Check out [our cookbook](https://docs.cohere.com/page/command-a-translate) for an example implementation.

Cohere enterprise clients may be interested in Deep Translation, our agentic approach to reaching the highest-quality translations. You can reach out to our sales team for more information.


# Cohere's Command A Vision Model

> Command A Vision is a powerful visual language model capable of interacting with image inputs. This document contains information about its capabilities.

<ModelShowcase
  model={{
  name: 'Command A Vision',
  id: 'command-a-vision-07-2025',
  capabilities: [
    Capability.SafetyModes,
    Capability.Citations,
    Capability.StructuredOutputs,
    Capability.Multilingual,
    Capability.ImageInputs
  ],
  specs: {
    contextWindow: '128,000',
    maxOutputTokens: '8,000',
    knowledgeCutoff: 'June 1, 2024',
    
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

Command A Vision is Cohere's first multimodal model capable of understanding and interpreting visual data alongside text. With a 128K context length and support for up to 20 images per request, Command Vision excels at enterprise use cases including document analysis, chart interpretation, optical character recognition (OCR), and processing images featuring multiple languages. The model maintains the same API interface as other Command models, making it easy to integrate vision capabilities into existing applications.

## What Can Command A Vision be Used For?

Command A Vision is excellent in enterprise use cases such as:

* Analysis of charts, graphs, and diagrams;
* Extracting and understanding in-image tables;
* Document optical character recognition (OCR) and question answering;
* Natural-language image processing.

## Limitations

Be aware that [tool use](https://docs.cohere.com/docs/tools) isn't supported with this model.

Also, it's important to mention that Command A Vision can accept images as input, but doesn't generate them.

For more detailed breakdowns of these and other applications, check out [our cookbooks](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/guides/vision). To learn more about how token counts work, the maximum number of images, and so on, check out our dedicated [Image Inputs](https://docs.cohere.com/docs/image-inputs) document.


# Cohere's Command R7B Model

> Command R7B is the smallest, fastest, and final model in our R family of enterprise-focused large language models. It excels at RAG, tool use, and agents.

<ModelShowcase
  model={{
  name: 'Command R7B',
  id: 'command-r7b-12-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.Multilingual,
    Capability.ToolUse,
    Capability.Citation,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.StructuredOutputs,

  ],
  pricing: { input: 0.0375, output: 0.15 },
  specs: {
    contextWindow: '128,000',
    maxOutputTokens: '4,000',
    knowledgeCutoff: 'June 1, 2024',
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

Command R7B is the smallest and fastest model in our R family of enterprise-focused [large language models](https://docs.cohere.com/v1/docs/the-cohere-platform#large-language-models-llms) (LLMs). With a context window of 128K and a compact architecture, Command R7B offers state-of-the-art performance across a variety of real-world tasks, and it is especially good at high throughput, latency-sensitive applications like chatbots and code assistants. What's more, it's small size also unlocks dramatically cheaper deployment infrastructure--such as consumer GPUs and CPUs--which means it can be used for on-device inference.

Command R7B is available today on the Cohere Platform as well as accessible on [HuggingFace](https://huggingface.co/CohereForAI/c4ai-command-r7b-12-2024), or you can access it in the SDK with `command-r7b-12-2024`. For more information, check out our [dedicated blog post](https://cohere.com/blog/command-r7b).

## What Can Command R7B Be Used For?

Command R7B is excellent for:

* RAG - [Retrieval Augmented Generation](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) (RAG) refers to the practice of ‘grounding’ model outputs in external data sources, which can increase accuracy. Command R7B is exceptionally good at generating responses in conversational tasks, attending over long inputs, and extracting and manipulating numerical information in financial settings.
* Tool-use - With [tool use](https://docs.cohere.com/docs/tool-use), Command models can be given tools such as search engines, APIs, vector databases, etc., which can expand their baseline functionality. Command R7B excels at tool use, exhibiting particular strength in using tools in real-world, diverse, and dynamic environments. In addition, Command R7B is good at avoiding unnecessarily calling tools, which is an important aspect of tool-use in practical applications.
* Agents - As this is being written, [agents](https://docs.cohere.com/docs/multi-step-tool-use) are among the most exciting frontiers for large language models. Command R7B’s multistep tool use capabilities allow it to power fast and capable REACT agents. When set up as an internet-augmented research agent, for example, Command R7B ably completes tasks that require breaking down complex questions into subgoals, and also performs favorably in domains that utilize complex reasoning and active information seeking.


# Cohere's Command R+ Model

> Command R+ is Cohere's optimized for conversational interaction and long-context tasks, best suited for complex RAG workflows and multi-step tool use.

<ModelShowcase
  model={{
  name: 'Command R+',
  id: 'command-r-plus-08-2024',
  capabilities: [
    Capability.Reasoning,
    Capability.SafetyModes,
    Capability.Citations,
    Capability.ToolUse,
    Capability.StructuredOutputs,
    Capability.Multilingual,
  ],
  pricing: { input: 2.50, output: 10.0 },
  specs: {
    contextWindow: '128,000',
    maxOutputTokens: '4,000',
    knowledgeCutoff: 'June 1, 2024',
  },
  endpoints: [
    Endpoint.ChatV2,
    Endpoint.ChatV1,
    Endpoint.ChatCompletions,
  ],
}}
/>

## Description

<Info title="Note">
  For most use cases we recommend our latest model [Command A](/docs/command-a) instead.
</Info>

Command R+ is a large language model, optimized for conversational interaction and long-context tasks. It aims at being extremely performant, enabling companies to move beyond proof of concept and into production.

We recommend using Command R+ for workflows that lean on complex RAG functionality and [multi-step tool use (agents)](/docs/multi-hop-tool-use). Command R, on the other hand, is great for simpler [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG) and [single-step tool use](/docs/tool-use) tasks, as well as applications where price is a major consideration.

For information on toxicity, safety, and using this model responsibly check out our [Command model card](https://docs.cohere.com/docs/responsible-use).

## Command R+ August 2024 Release

Cohere's flagship text-generation models, Command R and Command R+, received a substantial update in August 2024. We chose to designate these models with time stamps, so in the API Command R+ 08-2024 is accesible with `command-r-plus-08-2024`.

With the release, both models include the following feature improvements:

* For tool use, Command R and Command R+ have demonstrated improved decision-making around whether or not to use a tool.
* The updated models are better able to follow instructions included in the request's system message.
* Better structured data analysis for structured data manipulation.
* Improved robustness to non-semantic prompt changes like white space or new lines.
* Models will decline unanswerable questions and are now able to execute RAG workflows without citations

`command-r-plus-08-2024` in particular delivers roughly 50% higher throughput and 25% lower latencies as compared to the previous Command R+ version, while keeping the hardware footprint the same. Read more in the relevant blog post.

What's more, both these updated models can now operate in one of several safety modes, which gives developers more granular control over how models generate output in a variety of different contexts. Find more in these [safety modes docs](https://docs.cohere.com/docs/safety-modes).

Finally, these refreshed models were trained with data through February 2023, which means if you ask them questions requiring information from after this date their answers will likely be incorrect. But our RAG functionality can connect to the internet or other sources of information, which gives the models access to more timely facts and can improve the quality of their output.

## Unique Command R+ Model Capabilities

Command R+ has been trained on a massive corpus of diverse texts in multiple languages, and can perform a wide array of text-generation tasks. Moreover, Command R+ has been trained with a particular focus on excelling in some of the most critical business use-cases.

### Multilingual Capabilities

The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.

Additionally, pre-training data has been included for the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.

The model has been trained to respond in the language of the user. Here's an example:

*Prompt*

```Text
Écris une description de produit pour une voiture électrique en 50 à 75 mots
```

*Generation*

```text TEXT
Découvrez la voiture électrique qui va révolutionner votre façon de conduire.
Avec son design élégant, cette voiture offre une expérience de conduite unique
avec une accélération puissante et une autonomie impressionnante. Sa
technologie avancée vous garantit une charge rapide et une fiabilité inégalée.
Avec sa conception innovante et durable, cette voiture est parfaite pour les 
trajets urbains et les longues distances. Profitez d'une conduite silencieuse
et vivez l'expérience de la voiture électrique!
```

Command R+ can also perform cross-lingual tasks, such as translation or answering questions about content in other languages.

### Retrieval Augmented Generation

Command R+ has the ability to ground its English-language generations. This means that it can generate responses based on a list of supplied document snippets, and it will include citations in its response indicating the source of the information.

For more information, check out our dedicated guide on [retrieval augmented generation](/docs/retrieval-augmented-generation-rag).

### Multi-Step Tool Use

[Tool use](/docs/tool-use) is a technique which allows developers to connect Cohere's models to external tools--search engines, APIs, functions, databases, etc.--and use them to perform various actions.

Tool use comes in single-step and multi-step variants. In the former, the model has access to a bevy of tools to generate a response, and it can call multiple tools, but it must do all of this in a single step. The model cannot execute a sequence of steps, and it cannot use the results from one tool call in a subsequent step. In the latter, however, the model can call more than one tool in a sequence of steps, using the results from one tool call in a subsequent step. This process allows the language model to reason, perform dynamic actions, and quickly adapt on the basis of information coming from external sources.

Command R+ has been trained with multi-step tool use capabilities, with which it is possible to build simple agents. This functionality takes a conversation as input (with an optional user-system preamble), along with a list of available tools. The model will then generate a json-formatted list of actions to execute on a subset of those tools. For more information, check out our dedicated [multi-step tool use](/docs/multi-hop-tool-use) guide.

***

Congrats on reaching the end of this page! Get an extra \$1 API credit by entering the `CommandR+Docs` credit code in [your Cohere dashboard](https://dashboard.cohere.com/billing?tab=payment)



---

**Navigation:** ← Previous | [Index](./index.md) | [Next →](./02-coheres-command-r-model.md)
