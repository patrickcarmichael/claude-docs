**Navigation:** [← Previous](./04-after.md) | [Index](./index.md) | [Next →](./06-build-an-onboarding-assistant-with-cohere.md)

---

# Display the reranked search results
print("Reranked Search Results:")
for obj in rerank_response.objects:
    title = obj.properties.get("title")
    description = obj.properties.get("description")
    rerank_score = getattr(
        obj.metadata, "rerank_score", None
    )  # Get the rerank score metadata
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Rerank Score: {rerank_score}")
    print("-" * 50)
```

Here's what the output looks like:

```
Reranked Search Results:
Title: Bankruptcy Law Overview
Description: Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.
Rerank Score: 0.8951567
--------------------------------------------------
Title: Tax Law for Businesses
Description: Detailed guide to tax laws affecting businesses, including corporate income tax, payroll taxes, sales and use taxes, and tax deductions. Explores tax planning strategies, such as deferring income and accelerating expenses, as well as compliance requirements and penalties for non-compliance with tax laws.
Rerank Score: 7.071895e-06
--------------------------------------------------
Title: Consumer Protection Laws
Description: Comprehensive guide to consumer protection laws, including truth in advertising, product safety, and debt collection practices. Discusses the rights of consumers under federal and state laws, such as the right to sue for damages and the right to cancel certain contracts, as well as the role of government agencies in enforcing consumer protection laws.
Rerank Score: 6.4895394e-06
--------------------------------------------------
```

Based on the rerank scores, it's clear that the Bankruptcy Law Overview is the most relevant result, while the other two documents (Tax Law for Businesses and Consumer Protection Laws) have significantly lower scores, indicating they are less relevant to the query. Therefore, we should focus only on the most relevant result and can skip the other two.

## Embed + Rerank + Command

Finally, we'll add Command into the mix. This handles imports and creates a fresh `"Legal_Docs"` in the Weaviate database.

```python PYTHON
from weaviate.classes.config import Configure
from weaviate.classes.generate import GenerativeConfig

# Create a new collection named "Legal_Docs" in the Weaviate database
client.collections.create(
    name="Legal_Docs_RAG",
    properties=[
        # Define a property named "title" with data type TEXT
        Property(name="title", data_type=DataType.TEXT),
    ],
    # Configure the vectorizer to use Cohere's text2vec model
    vectorizer_config=Configure.Vectorizer.text2vec_cohere(
        model="embed-english-v3.0"  # Specify the Cohere model to use for vectorization
    ),
    # Configure the reranker to use Cohere's rerank model
    reranker_config=Configure.Reranker.cohere(
        model="rerank-english-v3.0"  # Specify the Cohere model to use for reranking
    ),
    # Configure the generative model to use Cohere's command r plus model
    generative_config=Configure.Generative.cohere(
        model="command-r-plus"
    ),
)
```

You should see something like that:

```
<weaviate.collections.collection.sync.Collection at 0x7f48afc06410>
```

This retrieves `"Legal_Docs_RAG"` from Weaviate:

```python PYTHON
# Retrieve the "Legal_Docs_RAG" collection from the Weaviate client
collection = client.collections.get("Legal_Docs_RAG")

# Use a dynamic batch process to add multiple documents to the collection efficiently
with collection.batch.dynamic() as batch:
    for src_obj in legal_documents:
        # Add each document to the batch, specifying the "title" and "description" properties
        batch.add_object(
            properties={
                "title": src_obj["title"],
                "description": src_obj["description"],
            },
        )
```

As before, we'll iterate over the object and print the result:

```python PYTHON
from weaviate.classes.config import Configure
from weaviate.classes.generate import GenerativeConfig

# To generate text for each object in the search results, use the single prompt method.
# The example below generates outputs for each of the n search results, where n is specified by the limit parameter.

collection = client.collections.get("Legal_Docs_RAG")
response = collection.generate.near_text(
    query=search_query,
    limit=1,
    single_prompt="Translate this into French -  {title}: {description}",
)

for obj in response.objects:
    print("Retrieved results")
    print("-----------------")
    print(obj.properties["title"])
    print(obj.properties["description"])
    print("Generated output")
    print("-----------------")
    print(obj.generated)
```

You'll see something like this:

```
Retrieved results
-----------------
Bankruptcy Law Overview
Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.
Generated output
-----------------
Voici une traduction possible :

Aperçu du droit des faillites : Introduction complète au droit des faillites, y compris les procédures de faillite en vertu des chapitres 7 et 13. Discute des conditions d'admissibilité pour déposer une demande de faillite, du processus de liquidation des actifs et de libération des dettes, ainsi que de l'impact de la faillite sur les cotes de crédit et les opportunités financières futures.
```

## Conclusion

This integration guide has demonstrated how to effectively combine Cohere's powerful AI capabilities with Weaviate's vector database to create sophisticated search and retrieval systems. We've covered three key approaches:

1. **Basic Vector Search**: Using Cohere's Embed model with Weaviate to perform semantic search, enabling natural language queries to find relevant documents based on meaning rather than just keywords.

2. **Enhanced Search with Rerank**: Adding Cohere's Rerank model to improve search results by reordering them based on relevance, ensuring the most pertinent documents appear first.

3. **Full RAG Pipeline**: Implementing a complete Retrieval-Augmented Generation (RAG) system that combines embedding, reranking, and Cohere's Command model to not only find relevant information but also generate contextual responses.

The integration showcases how these technologies work together to create more intelligent and accurate search systems. Whether you're building a healthcare compliance database, legal document system, or any other knowledge base, this combination provides a powerful foundation for semantic search and AI-powered content generation.

The flexibility of this integration allows you to adapt it to various use cases while maintaining high performance and accuracy in your search and retrieval operations.


# Open Search and Cohere (Integration Guide)

> Unlock the power of search and analytics with OpenSearch, enhanced by ML connectors like Cohere and Amazon Bedrock.

<img src="file:1b864022-d972-4d36-9f80-bd9b4bdda778" width="200px" height="auto" class="light-bg" />

[OpenSearch](https://opensearch.org/platform/search/vector-database.html) is an open-source, distributed search and analytics engine platform that allows users to search, analyze, and visualize large volumes of data in real time. When it comes to text search, OpenSearch is well-known for powering keyword-based (also called lexical) search methods. OpenSearch supports Vector Search and integrates with Cohere through [3rd-Party ML Connectors](https://opensearch.org/docs/latest/ml-commons-plugin/remote-models/connectors/) as well as Amazon Bedrock.


# Vespa and Cohere (Integration Guide)

> This page describes how to integrate Cohere with the Vespa database.

<img src="file:62002a1c-d72a-4003-80cc-e34b4e03030f" width="200px" height="auto" class="light-bg" />

[Vespa](https://vespa.ai/) is a fully featured search engine and vector database. It supports vector search (ANN), lexical search, and search in structured data, all in the same query. Integrated machine-learned model inference allows you to apply AI to make sense of your data in real time.

Check out [this post](https://blog.vespa.ai/scaling-large-vector-datasets-with-cohere-binary-embeddings-and-vespa/) to find more information about working with Cohere's embeddings on Vespa.


# Qdrant and Cohere (Integration Guide)

> This page describes how to integrate Cohere with the Qdrant vector database.

<img src="file:9c606218-169c-46aa-a91c-da6406e3a3dd" width="200px" height="auto" class="light-bg" />

[Qdrant](https://qdrant.tech/) is an open-source vector similarity search engine and vector database. It provides a production-ready service with a convenient API to store, search, and manage points - vectors with an additional payload. Qdrant is tailored to extended filtering support. It makes it useful for all sorts of neural-network or semantic-based matching, faceted search, and other applications.

Qdrant is written in Rust, which makes it fast and reliable even under high load.

To learn more about how to work with Cohere's embeddings on Qdrant, [read this guide](https://qdrant.tech/documentation/embeddings/cohere/)


# Milvus and Cohere (Integration Guide)

> This page describes integrating Cohere with the Milvus vector database.

<img src="file:b960d250-0b67-489a-840b-466fc2d8d0e9" width="200px" height="auto" class="light-bg" />

[Milvus](https://milvus.io/) is a highly flexible, reliable, and blazing-fast cloud-native, open-source vector database. It powers embedding similarity search and AI applications and strives to make vector databases accessible to every organization. Milvus is a graduated-stage project of the LF AI & Data Foundation.

The following [guide](https://milvus.io/docs/integrate_with_cohere.md) walks through how to integrate [Cohere embeddings](/docs/embeddings) with Milvus.


# Zilliz and Cohere (Integration Guide)

> This page describes how to integrate Cohere with the Zilliz database.

<img src="file:9fb53ec2-0eaa-4b6c-b274-f6daa0f2e74e" width="200px" height="auto" class="light-bg" />

[Zilliz Cloud](https://zilliz.com/cloud) is a cloud-native vector database that stores, indexes, and searches for billions of embedding vectors to power enterprise-grade similarity search, recommender systems, anomaly detection, and more. Zilliz Cloud provides a fully-managed Milvus service, made by the creators of Milvus that allows for easy integration with vectorizers from Cohere and other popular models. Purpose-built to solve the challenge of managing billions of embeddings, Zilliz Cloud makes it easy to build applications for scale.

The following [guide](https://docs.zilliz.com/docs/question-answering-using-zilliz-cloud-and-cohere) walks through how to integrate [Cohere embeddings](/docs/embeddings) with Zilliz. You might also find this [quickstart guide](https://docs.zilliz.com/docs/quick-start) helpful.


# Chroma and Cohere (Integration Guide)

> This page describes how to integrate Cohere and Chroma.

<img src="file:b005a9c7-7cee-4541-be93-fd6b8d6068b7" width="200px" height="auto" class="light-bg" />

Chroma is an open-source vector search engine that's quick to install and start building with using Python or Javascript.

You can get started with [Chroma here](https://trychroma.com).


# Cohere and LangChain (Integration Guide)

> Integrate Cohere with LangChain for advanced chat features, RAG, embeddings, and reranking; this guide includes code examples for each feature.

Cohere [has first class support for LangChain](https://python.langchain.com/docs/integrations/providers/cohere), a framework which enables you to quickly create LLM powered applications. This doc will guide you through how to leverage different Cohere features with LangChain.

### Prerequisite

To use LangChain and Cohere you will need:

* LangChain package. To install it, run `pip install langchain`.

* LangChain Package. To install it, run:
  * `pip install langchain`
  * `pip install langchain-cohere` (to use the Cohere integrations in LangChain)
  * Optional: `pip install langchain-community` (to access third-party integrations such as web search APIs)

* Cohere's SDK. To install it, run `pip install cohere`. If you run into any issues or want more details on Cohere's SDK, [see this wiki](https://github.com/cohere-ai/cohere-python).

* A Cohere API Key. For more details on pricing [see this page](https://cohere.com/pricing). When you create an account with Cohere, we automatically create a trial API key for you. This key will be available on the dashboard where you can copy it, and it's in the dashboard section called "API Keys" as well.

### Integrating LangChain with Cohere Models

The following guides contain technical details on the many ways in which Cohere and LangChain can be used in tandem:

* [Chat on LangChain](/docs/chat-on-langchain)
* [Embed on LangChain](/docs/embed-on-langchain)
* [Rerank on LangChain](/docs/rerank-on-langchain)
* [Tools on LangChain](/docs/tools-on-langchain)


# Cohere Chat on LangChain (Integration Guide)

> Integrate Cohere with LangChain to build applications using Cohere's models and LangChain tools.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage Cohere Chat with LangChain.

### Prerequisites

Running Cohere Chat with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere Chat with LangChain

To use [Cohere chat](/docs/chat-api) with LangChain, simply create a [ChatCohere](https://python.langchain.com/docs/integrations/chat/cohere/) object and pass in the message or message history. In the example below, you will need to add your Cohere API key.

```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.messages import AIMessage, HumanMessage

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Send a chat message without chat history
current_message = [HumanMessage(content="knock knock")]
print(llm.invoke(current_message))

# Send a chat message with chat history, note the last message is the current user message
current_message_and_history = [
    HumanMessage(content="knock knock"),
    AIMessage(content="Who's there?"),
    HumanMessage(content="Tank"),
]
print(llm.invoke(current_message_and_history))
```

### Cohere Agents with LangChain

LangChain [Agents](https://python.langchain.com/docs/how_to/#agents) use a language model to choose a sequence of actions to take.

To use Cohere's multi hop agent create a `create_cohere_react_agent` and pass in the LangChain tools you would like to use.

For example, using an internet search tool to get essay writing advice from Cohere with citations:

```python PYTHON
from langchain_cohere import ChatCohere
from langchain_cohere.react_multi_hop.agent import (
    create_cohere_react_agent,
)
from langchain.agents import AgentExecutor
from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from langchain_core.prompts import ChatPromptTemplate

# Internet search tool - you can use any tool, and there are lots of community tools in LangChain.
# To use the Tavily tool you will need to set an API key in the TAVILY_API_KEY environment variable.
os.environ["TAVILY_API_KEY"] = "TAVILY_API_KEY"
internet_search = TavilySearchResults()

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Create an agent
agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search],
    prompt=ChatPromptTemplate.from_template("{question}"),
)

# Create an agent executor
agent_executor = AgentExecutor(
    agent=agent, tools=[internet_search], verbose=True
)

# Generate a response
response = agent_executor.invoke(
    {
        "question": "I want to write an essay. Any tips?",
    }
)

# See Cohere's response
print(response.get("output"))
# Cohere provides exact citations for the sources it used
print(response.get("citations"))
```

### Cohere Chat and RAG with LangChain

To use Cohere's [retrieval augmented generation (RAG)](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) functionality with LangChain, create a [CohereRagRetriever](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/retrievers/cohere_rag_retriever.py) object. Then there are a few RAG uses, discussed in the next few sections.

#### Using LangChain's Retrievers

In this example, we use the [wikipedia retriever](https://python.langchain.com/docs/integrations/retrievers/wikipedia) but any [retriever supported by LangChain](https://python.langchain.com/docs/integrations/retrievers) can be used here.  In order to set up the wikipedia retriever you need to install the wikipedia python package using `%pip install --upgrade --quiet  wikipedia`. With that done, you can execute this code to see how a retriever works:

```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain.retrievers import WikipediaRetriever
from langchain_cohere import ChatCohere

# User query we will use for the generation
user_query = "What is cohere?"
# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)
# Create the Cohere rag retriever using the chat model
rag = CohereRagRetriever(llm=llm, connectors=[])
# Create the wikipedia retriever
wiki_retriever = WikipediaRetriever()
# Get the relevant documents from wikipedia
wiki_docs = wiki_retriever.invoke(user_query)
# Get the cohere generation from the cohere rag retriever
docs = rag.invoke(user_query, documents=wiki_docs)
# Print the documents
print("Documents:")
for doc in docs[:-1]:
    print(doc.metadata)
    print("\n\n" + doc.page_content)
    print("\n\n" + "-" * 30 + "\n\n")
# Print the final generation
answer = docs[-1].page_content
print("Answer:")
print(answer)
# Print the final citations
citations = docs[-1].metadata["citations"]
print("Citations:")
print(docs[-1].__dict__)
```

#### Using Documents

In this example, we take documents (which might be generated in other parts of your application) and pass them into the [CohereRagRetriever](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/retrievers/cohere_rag_retriever.py) object:

```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain_cohere import ChatCohere
from langchain_core.documents import Document

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Create the Cohere rag retriever using the chat model
rag = CohereRagRetriever(llm=llm, connectors=[])
docs = rag.invoke(
    "Does LangChain support cohere RAG?",
    documents=[
        Document(
            page_content="LangChain supports cohere RAG!",
            metadata={"id": "id-1"},
        ),
        Document(
            page_content="The sky is blue!", metadata={"id": "id-2"}
        ),
    ],
)

# Print the documents
print("Documents:")
for doc in docs[:-1]:
    print(doc.metadata)
    print("\n\n" + doc.page_content)
    print("\n\n" + "-" * 30 + "\n\n")
# Print the final generation
answer = docs[-1].page_content
print("Answer:")
print(answer)
# Print the final citations
citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

#### Using a Connector

In this example, we create a generation with a [connector](https://docs.cohere.com/v1/docs/overview-rag-connectors) which allows us to get a generation with citations to results from the connector. We use the "web-search" connector, which is available to everyone. But if you have created your own connector in your org you can pass in its id, like so: `rag = CohereRagRetriever(llm=cohere_chat_model, connectors=[{"id": "example-connector-id"}])`

Here's a code sample illustrating how to use a connector:

```python PYTHON
from langchain_cohere import CohereRagRetriever
from langchain_cohere import ChatCohere
from langchain_core.documents import Document

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Create the Cohere rag retriever using the chat model with the web search connector
rag = CohereRagRetriever(llm=llm, connectors=[{"id": "web-search"}])
docs = rag.invoke("Who founded Cohere?")
# Print the documents
print("Documents:")
for doc in docs[:-1]:
    print(doc.metadata)
    print("\n\n" + doc.page_content)
    print("\n\n" + "-" * 30 + "\n\n")
# Print the final generation
answer = docs[-1].page_content
print("Answer:")
print(answer)
# Print the final citations
citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

#### Using the `create_stuff_documents_chain` Chain

This chain takes a list of documents and formats them all into a prompt, then passes that prompt to an LLM. It passes ALL documents, so you should make sure it fits within the context window of the LLM you are using.

Note: this feature is currently in beta.

```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)

prompt = ChatPromptTemplate.from_messages(
    [("human", "What are everyone's favorite colors:\n\n{context}")]
)

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

chain = create_stuff_documents_chain(llm, prompt)

docs = [
    Document(page_content="Jesse loves red but not yellow"),
    Document(
        page_content="Jamal loves green but not as much as he loves orange"
    ),
]

chain.invoke({"context": docs})
```

### Structured Output Generation

Cohere supports generating JSON objects to structure and organize the model’s responses in a way that can be used in downstream applications.

You can specify the `response_format` parameter to indicate that you want the response in a JSON object format.

```python PYTHON
from langchain_cohere import ChatCohere

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

res = llm.invoke(
    "John is five years old",
    response_format={
        "type": "json_object",
        "schema": {
            "title": "Person",
            "description": "Identifies the age and name of a person",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the person",
                },
                "age": {
                    "type": "number",
                    "description": "Age of the person",
                },
            },
            "required": [
                "name",
                "age",
            ],
        },
    },
)

print(res)
```

### Text Summarization

You can use the `load_summarize_chain` chain to perform text summarization.

```python PYTHON
from langchain_cohere import ChatCohere
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.cohere.com/docs/cohere-toolkit")
docs = loader.load()

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

chain = load_summarize_chain(llm, chain_type="stuff")

chain.invoke({"input_documents": docs})
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.

```python PYTHON
llm = ChatCohere(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```


# Cohere Embed on LangChain (Integration Guide)

> This page describes how to work with Cohere's embeddings models and LangChain.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage different Cohere embeddings with LangChain.

### Prerequisites

Running Cohere embeddings with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere Embeddings with LangChain

To use [Cohere's Embeddings](/docs/embeddings) with LangChain, create a [CohereEmbedding](https://github.com/langchain-ai/langchain-community/blob/main/libs/community/langchain_community/embeddings/cohere.py) object as follows (the available cohere embedding models [are listed here](/reference/embed)):

```python PYTHON
from langchain_cohere import CohereEmbeddings

# Define the Cohere embedding model
embeddings = CohereEmbeddings(
    cohere_api_key="COHERE_API_KEY", model="embed-v4.0"
)

# Embed a document
text = "This is a test document."
query_result = embeddings.embed_query(text)
print(query_result[:5], "...")
doc_result = embeddings.embed_documents([text])
print(doc_result[0][:5], "...")
```

To use these embeddings with Cohere's RAG functionality, you will need to use one of the vector DBs [from this list](https://python.langchain.com/docs/integrations/vectorstores). In this example we use chroma, so in order to run it you will need to install chroma using `pip install chromadb`.

```python PYTHON
from langchain_cohere import (
    ChatCohere,
    CohereEmbeddings,
    CohereRerank,
    CohereRagRetriever,
)
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader

user_query = "what is Cohere Toolkit?"

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

embeddings = CohereEmbeddings(
    cohere_api_key="COHERE_API_KEY", model="embed-v4.0"
)

# Load text files and split into chunks, you can also use data gathered elsewhere in your application
raw_documents = WebBaseLoader(
    "https://docs.cohere.com/docs/cohere-toolkit"
).load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
# Create a vector store from the documents
db = Chroma.from_documents(documents, embeddings)
input_docs = db.as_retriever().invoke(user_query)

# Create the cohere rag retriever using the chat model
rag = CohereRagRetriever(llm=llm)
docs = rag.invoke(
    user_query,
    documents=input_docs,
)
# Print the documents
print("Documents:")
for doc in docs[:-1]:
    print(doc.metadata)
    print("\n\n" + doc.page_content)
    print("\n\n" + "-" * 30 + "\n\n")
# Print the final generation
answer = docs[-1].page_content
print("Answer:")
print(answer)
# Print the final citations
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

# Replace the profile name with the one created in the setup.
embeddings = BedrockEmbeddings(
    credentials_profile_name="{PROFILE-NAME}",
    region_name="us-east-1",
    model_id="cohere.embed-english-v3",
)

embeddings.embed_query("This is a content of the document")
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.

```python PYTHON
llm = CohereEmbeddings(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```


# Cohere Rerank on LangChain (Integration Guide)

> This page describes how to integrate Cohere's ReRank models with LangChain.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage Rerank with LangChain.

### Prerequisites

Running Cohere Rerank with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

### Cohere ReRank with LangChain

To use Cohere's [rerank functionality ](/docs/reranking) with LangChain, start with instantiating a [CohereRerank](https://github.com/langchain-ai/langchain/blob/master/libs/langchain/langchain/retrievers/document_compressors/cohere_rerank.py) object as follows: `cohere_rerank = CohereRerank(cohere_api_key="{API_KEY}")`.

You can then use it with LangChain retrievers, embeddings, and RAG. The example below uses the vector DB chroma, for which you will need to install `pip install chromadb`. Other vector DB's [from this list](https://python.langchain.com/docs/integrations/vectorstores) can also be used.

```python PYTHON
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereEmbeddings
from langchain_cohere import ChatCohere
from langchain_cohere import CohereRerank, CohereRagRetriever
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import WebBaseLoader

user_query = "what is Cohere Toolkit?"

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Define the Cohere embedding model
embeddings = CohereEmbeddings(
    cohere_api_key="COHERE_API_KEY", model="embed-english-light-v3.0"
)

# Load text files and split into chunks, you can also use data gathered elsewhere in your application
raw_documents = WebBaseLoader(
    "https://docs.cohere.com/docs/cohere-toolkit"
).load()
text_splitter = CharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0
)
documents = text_splitter.split_documents(raw_documents)

# Create a vector store from the documents
db = Chroma.from_documents(documents, embeddings)

# Create Cohere's reranker with the vector DB using Cohere's embeddings as the base retriever
reranker = CohereRerank(
    cohere_api_key="COHERE_API_KEY", model="rerank-english-v3.0"
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker, base_retriever=db.as_retriever()
)
compressed_docs = compression_retriever.get_relevant_documents(
    user_query
)
# Print the relevant documents from using the embeddings and reranker
print(compressed_docs)

# Create the cohere rag retriever using the chat model
rag = CohereRagRetriever(llm=llm, connectors=[])
docs = rag.get_relevant_documents(
    user_query,
    documents=compressed_docs,
)
# Print the documents
print("Documents:")
for doc in docs[:-1]:
    print(doc.metadata)
    print("\n\n" + doc.page_content)
    print("\n\n" + "-" * 30 + "\n\n")
# Print the final generation
answer = docs[-1].page_content
print("Answer:")
print(answer)
# Print the final citations
citations = docs[-1].metadata["citations"]
print("Citations:")
print(citations)
```

### Using LangChain on Private Deployments

You can use LangChain with privately deployed Cohere models. To use it, specify your model deployment URL in the `base_url` parameter.

```python PYTHON
llm = CohereRerank(
    base_url="<YOUR_DEPLOYMENT_URL>",
    cohere_api_key="COHERE_API_KEY",
    model="MODEL_NAME",
)
```


# Cohere Tools on LangChain (Integration Guide)

> Explore code examples for multi-step and single-step tool usage in chatbots, harnessing internet search and vector storage.

Cohere supports various integrations with LangChain, a large language model (LLM) framework which allows you to quickly create applications based on Cohere's models. This doc will guide you through how to leverage [Cohere tools](/docs/tool-use) with LangChain.

### Prerequisites

Running Cohere tools with LangChain doesn't require many prerequisites, consult the [top-level document](/docs/cohere-and-langchain) for more information.

## Multi-Step Tool Use

Multi-step is enabled by default. Here's an example of using it to put together a simple agent:

```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import (
    create_cohere_react_agent,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere

from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from pydantic import BaseModel, Field

os.environ["TAVILY_API_KEY"] = "TAVILY_API_KEY"

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


class TavilySearchInput(BaseModel):
    query: str = Field(
        description="Query to search the internet with"
    )


internet_search.args_schema = TavilySearchInput

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)
# Preamble
preamble = """
You are an expert who answers the user's question with the most relevant datasource. You are equipped with an internet search tool and a special vectorstore of information about how to write good essays.
"""

# Prompt template
prompt = ChatPromptTemplate.from_template("{input}")

# Create the ReAct agent
agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search],
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent, tools=[internet_search], verbose=True
)

response = agent_executor.invoke(
    {
        "input": "Who is the mayor of the capital of Ontario",
        "preamble": preamble,
    }
)

print(response["output"])
```

## Single-Step Tool Use

In order to utilize single-step mode, you have to set `force_single_step=True`. Here's an example of using it to answer a few questions:

```python PYTHON
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field


# Data model
class web_search(BaseModel):
    """
    The internet. Use web_search for questions that are related to anything else than agents, prompt engineering, and adversarial attacks.
    """

    query: str = Field(
        description="The query to use when searching the internet."
    )


class vectorstore(BaseModel):
    """
    A vectorstore containing documents related to agents, prompt engineering, and adversarial attacks. Use the vectorstore for questions on these topics.
    """

    query: str = Field(
        description="The query to use when searching the vectorstore."
    )


# Preamble
preamble = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. Otherwise, use web-search."""

# LLM with tool use and preamble
# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

llm_with_tools = llm.bind_tools(
    tools=[web_search, vectorstore], preamble=preamble
)

messages = [
    HumanMessage("Who will the Bears draft first in the NFL draft?")
]
response = llm_with_tools.invoke(messages, force_single_step=True)
print(response.response_metadata["tool_calls"])

messages = [HumanMessage("What are the types of agent memory?")]
response = llm_with_tools.invoke(messages, force_single_step=True)
print(response.response_metadata["tool_calls"])

messages = [HumanMessage("Hi, How are you?")]
response = llm_with_tools.invoke(messages, force_single_step=True)
print("tool_calls" in response.response_metadata)
```

## SQL Agent

LangChain's SQL Agent abstraction provides a flexible way of interacting with SQL Databases. This can be accessed via the `create_sql_agent` constructor.

```python PYTHON
from langchain_cohere import ChatCohere, create_sql_agent
from langchain_community.utilities import SQLDatabase
import urllib.request
import pandas as pd
import sqlite3

# Download the Chinook SQLite database
url = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
urllib.request.urlretrieve(url, "Chinook.db")
print("Chinook database downloaded successfully.")

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

agent_executor = create_sql_agent(llm, db=db, verbose=True)

resp = agent_executor.invoke(
    "Show me the first 5 rows of the Album table."
)
print(resp)
```

## CSV Agent

LangChain's CSV Agent abstraction enables building agents that can interact with CSV files. This can be accessed via the `create_csv_agent` constructor.

```python PYTHON
from langchain_cohere import ChatCohere, create_csv_agent

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

agent_executor = create_csv_agent(
    llm,
    "titanic.csv",  # https://github.com/langchain-ai/langchain/blob/master/templates/csv-agent/titanic.csv
)

resp = agent_executor.invoke(
    {"input": "How many people were on the titanic?"}
)
print(resp.get("output"))
```

## Streaming for Tool Calling

When tools are called in a streaming context, message chunks will be populated with tool call chunk objects in a list via the `.tool_call_chunks` attribute.

```python PYTHON
from langchain_core.tools import tool
from langchain_cohere import ChatCohere


@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b


tools = [add, multiply]

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

llm_with_tools = llm.bind_tools(tools)

query = "What is 3 * 12? Also, what is 11 + 49?"

for chunk in llm_with_tools.stream(query):
    if chunk.tool_call_chunks:
        print(chunk.tool_call_chunks)
```

## LangGraph Agents

LangGraph is a stateful, orchestration framework that brings added control to agent workflows.

To use LangGraph with Cohere, you need to install the LangGraph package. To install it, run `pip install langgraph`.

### Basic Chatbot

This simple chatbot example will illustrate the core concepts of building with LangGraph.

```python PYTHON
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_cohere import ChatCohere


# Create a state graph
class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

# Define the Cohere LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)


# Add nodes
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# Compile the graph
graph = graph_builder.compile()

# Run the chatbot
while True:
    user_input = input("User: ")
    print("User: " + user_input)
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
```

### Enhancing the Chatbot with Tools

To handle queries our chatbot can't answer "from memory", we'll integrate a web search tool. Our bot can use this tool to find relevant information and provide better responses.

```python PYTHON
from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from langchain_cohere import ChatCohere
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_core.messages import ToolMessage
from langchain_core.messages import BaseMessage
from typing import Annotated, Literal
from typing_extensions import TypedDict
import json


# Create a tool
tool = TavilySearchResults(max_results=2)
tools = [tool]


# Create a state graph
class State(TypedDict):
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)

# Define the LLM
llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

# Bind the tools to the LLM
llm_with_tools = llm.bind_tools(tools)


# Add nodes
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)


class BasicToolNode:
    """A node that runs the tools requested in the last AIMessage."""

    def __init__(self, tools: list) -> None:
        self.tools_by_name = {tool.name: tool for tool in tools}

    def __call__(self, inputs: dict):
        if messages := inputs.get("messages", []):
            message = messages[-1]
        else:
            raise ValueError("No message found in input")
        outputs = []
        for tool_call in message.tool_calls:
            tool_result = self.tools_by_name[
                tool_call["name"]
            ].invoke(tool_call["args"])
            outputs.append(
                ToolMessage(
                    content=json.dumps(tool_result),
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
        return {"messages": outputs}


tool_node = BasicToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)


def route_tools(
    state: State,
) -> Literal["tools", "__end__"]:
    """
    Use in the conditional_edge to route to the ToolNode if the last message
    has tool calls. Otherwise, route to the end.
    """
    if isinstance(state, list):
        ai_message = state[-1]
    elif messages := state.get("messages", []):
        ai_message = messages[-1]
    else:
        raise ValueError(
            f"No messages found in input state to tool_edge: {state}"
        )
    if (
        hasattr(ai_message, "tool_calls")
        and len(ai_message.tool_calls) > 0
    ):
        return "tools"
    return "__end__"


graph_builder.add_conditional_edges(
    "chatbot",
    route_tools,
    {"tools": "tools", "__end__": "__end__"},
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")

# Compile the graph
graph = graph_builder.compile()

# Run the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            if isinstance(value["messages"][-1], BaseMessage):
                print("Assistant:", value["messages"][-1].content)
```


# LlamaIndex and Cohere's Models

> Learn how to use Cohere and LlamaIndex together to generate responses based on data.

### Prerequisite

To use LlamaIndex and Cohere, you will need:

* LlamaIndex Package. To install it, run:
  * `pip install llama-index`
  * `pip install llama-index-llms-cohere` (to use the Command models)
  * `pip install llama-index-embeddings-cohere` (to use the Embed models)
  * `pip install llama-index-postprocessor-cohere-rerank` (to use the Rerank models)
* Cohere's SDK. To install it, run `pip install cohere`. If you run into any issues or want more details on Cohere's SDK, [see this wiki](https://github.com/cohere-ai/cohere-python).
* A Cohere API Key. For more details on pricing [see this page](https://cohere.com/pricing). When you create an account with Cohere, we automatically create a trial API key for you. This key will be available on the dashboard where you can copy it, and it's in the dashboard section called "API Keys" as well.

### Cohere Chat with LlamaIndex

To use Cohere's chat functionality with LlamaIndex create a [Cohere model object](https://docs.llamaindex.ai/en/stable/examples/llm/cohere.html) and call the `chat` function.

```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.core.llms import ChatMessage

cohere_model = Cohere(
    api_key="COHERE_API_KEY", model="command-a-03-2025"
)

message = ChatMessage(role="user", content="What is 2 + 3?")

response = cohere_model.chat([message])
print(response)
```

### Cohere Embeddings with LlamaIndex

To use Cohere's embeddings with LlamaIndex create a [Cohere Embeddings object](https://docs.llamaindex.ai/en/stable/examples/embeddings/cohereai.html) with an embedding model [from this list](/reference/embed) and call `get_text_embedding`.

```python PYTHON
from llama_index.embeddings.cohere import CohereEmbedding

embed_model = CohereEmbedding(
    api_key="COHERE_API_KEY",
    model_name="embed-english-v3.0",
    input_type="search_document",  # Use search_query for queries, search_document for documents
    max_tokens=8000,
    embedding_types=["float"],
)

# Generate Embeddings
embeddings = embed_model.get_text_embedding("Welcome to Cohere!")

# Print embeddings
print(len(embeddings))
print(embeddings[:5])
```

### Cohere Rerank with LlamaIndex

To use Cohere's rerank functionality with LlamaIndex create a [ Cohere Rerank object ](https://docs.llamaindex.ai/en/latest/examples/node_postprocessor/CohereRerank.html#) and use as a [node post processor.](https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.html)

```python PYTHON
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.readers.web import (
    SimpleWebPageReader,
)  # first, run `pip install llama-index-readers-web`

# create index (we are using an example page from Cohere's docs)
documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://docs.cohere.com/v2/docs/cohere-embed"]
)  # you can replace this with any other reader or documents
index = VectorStoreIndex.from_documents(documents=documents)

# create reranker
cohere_rerank = CohereRerank(
    api_key="COHERE_API_KEY", model="rerank-english-v3.0", top_n=2
)

# query the index
query_engine = index.as_query_engine(
    similarity_top_k=10,
    node_postprocessors=[cohere_rerank],
)

print(query_engine)

# generate a response
response = query_engine.query(
    "What is Cohere's Embed Model?",
)

print(response)

# To view the source documents
from llama_index.core.response.pprint_utils import pprint_response

pprint_response(response, show_source=True)
```

### Cohere RAG with LlamaIndex

The following example uses Cohere's chat model, embeddings and rerank functionality to generate a response based on your data.

```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from llama_index.postprocessor.cohere_rerank import CohereRerank
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.readers.web import (
    SimpleWebPageReader,
)  # first, run `pip install llama-index-readers-web`

# Create the embedding model
embed_model = CohereEmbedding(
    api_key="COHERE_API_KEY",
    model="embed-english-v3.0",
    input_type="search_document",
    max_tokens=8000,
    embedding_types=["float"],
)

# Create the service context with the cohere model for generation and embedding model
Settings.llm = Cohere(
    api_key="COHERE_API_KEY", model="command-a-03-2025"
)
Settings.embed_model = embed_model

# create index (we are using an example page from Cohere's docs)
documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://docs.cohere.com/v2/docs/cohere-embed"]
)  # you can replace this with any other reader or documents
index = VectorStoreIndex.from_documents(documents=documents)

# Create a cohere reranker
cohere_rerank = CohereRerank(
    api_key="COHERE_API_KEY", model="rerank-english-v3.0", top_n=2
)

# Create the query engine
query_engine = index.as_query_engine(
    node_postprocessors=[cohere_rerank]
)

# Generate the response
response = query_engine.query("What is Cohere's Embed model?")
print(response)
```

### Cohere Tool Use (Function Calling) with LlamaIndex

To use Cohere's tool use functionality with LlamaIndex, you can use the `FunctionTool` class to create a tool that uses Cohere's API.

```python PYTHON
from llama_index.llms.cohere import Cohere
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgent


# Define tools
def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

# Define LLM
llm = Cohere(api_key="COHERE_API_KEY", model="command-a-03-2025")

# Create agent
agent = FunctionCallingAgent.from_tools(
    [multiply_tool, add_tool],
    llm=llm,
    verbose=True,
    allow_parallel_tool_calls=True,
)

# Run agent
response = await agent.achat("What is (121 * 3) + (5 * 8)?")
```


# Deployment Options - Overview

> This page provides an overview of the available options for deploying Cohere's models.

The most common way to access Cohere’s large language models (LLMs) is through the Cohere platform, which is fully managed by Cohere and accessible through an API.

But that’s not the only way to access Cohere’s models. In an enterprise setting, organizations might require more control over where and how the models are hosted.

Specifically, Cohere offers four types of deployment options.

1. **Cohere Platform**
2. **Cloud AI Services**
3. **Private Deployments - Cloud**
4. **Private Deployments - On-Premises**

## Cohere platform

This is the fastest and easiest way to start using Cohere’s models. The models are hosted on Cohere infrastructure and available on our public SaaS platform (which provides an API data opt-out), which is fully managed by Cohere.

## Cloud AI services

These managed services enable enterprises to access Cohere’s models on cloud AI services. In this scenario, Cohere’s models are hosted on the cloud provider’s infrastructure. Cohere is cloud-agnostic, meaning you can deploy our models through any cloud provider.

### AWS

Developers can access a range of Cohere’s language models in a private environment via Amazon’s AWS Cloud platform. Cohere’s models are supported on two Amazon services: **Amazon Bedrock** and **Amazon SageMaker**.

#### Amazon Bedrock

Amazon Bedrock is a fully managed service where foundational models from Cohere are made available through a single, serverless API. [Read about Bedrock here](http://docs.aws.amazon.com/bedrock).

[View Cohere’s models on Amazon Bedrock](https://aws.amazon.com/bedrock/cohere/).

#### Amazon SageMaker

Amazon SageMaker is a service that allows customers to prepare data and build, train, and deploy machine learning (ML) models for any use case with fully managed infrastructure, tools, and workflows. [Read about SageMaker here.](https://aws.amazon.com/pm/sagemaker/)

Cohere offers a comprehensive suite of generative and embedding models through SageMaker on a range of hardware options, many of which support finetuning for deeper customization and performance.

[View Cohere's model listing on the AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0).

### Azure AI Foundry

Azure AI Foundry is a platform that is designed for developers to build generative AI applications on an enterprise-grade platform. Developers can explore a wide range of models, services, and capabilities to build AI applications that meet their specific goals.

[View Cohere’s models on Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command).

### OCI Generative AI Service

Oracle Cloud Infrastructure Generative AI is a fully managed service that enables you to use Cohere's [generative](https://docs.oracle.com/en-us/iaas/Content/generative-ai/generate-models.htm) and [embedding models](https://docs.oracle.com/en-us/iaas/Content/generative-ai/embed-models.htm) through an API.

## Private deployments

### Cloud (VPC)

Private deployments (cloud) allow enterprises to deploy the Cohere stack privately on cloud platforms. With AWS, Cohere’s models can be deployed in an enterprise’s AWS Cloud environment via their own VPC (EC2, EKS). Compared to managed cloud services, VPC deployments provide tighter control and compliance. No egress is another common reason for going with VPCs. Overall, the VPC option has a higher management burden but offers more flexibility.

### On-premises

Private deployments on-premises (on-prem) allow enterprises to deploy the Cohere stack privately on their own compute. This includes air-gapped environments where systems are physically isolated from unsecured networks, providing maximum security for sensitive workloads.


# Cohere SDK Cloud Platform Compatibility

> This page describes various places you can use Cohere's SDK.

To maximize convenience in building on and switching between Cohere-supported environments, we have developed SDKs that seamlessly support whichever backend you choose. This allows you to start developing your project with one backend while maintaining the flexibility to switch, should the need arise.

Note that the code snippets presented in this document should be more than enough to get you started, but if you end up switching from one environment to another there will be some small changes you need to make to how you import and initialize the SDK.

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

## Feature support

The most complete set of features is found on the cohere platform, while each of the cloud platforms support subsets of these features. Please consult the platform-specific documentation for more information about the parameters that they support.

| Feature          | Cohere Platform | Bedrock     | Sagemaker   | Azure       | OCI         | Private Deployment |
| ---------------- | --------------- | ----------- | ----------- | ----------- | ----------- | ------------------ |
| chat\_stream     | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| chat             | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| generate\_stream | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| generate         | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| embed            | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |
| rerank           | ✅               | ✅           | ✅           | ✅           | ⬜️          | ✅                  |
| classify         | ✅               | ⬜️          | ⬜️          | ⬜️          | ⬜️          | ✅                  |
| summarize        | ✅               | ⬜️          | ⬜️          | ⬜️          | ⬜️          | ✅                  |
| tokenize         | ✅               | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline)        |
| detokenize       | ✅               | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline) | ✅ (offline)        |
| check\_api\_key  | ✅               | ✅           | ✅           | ✅           | ✅           | ✅                  |

## Snippets

#### Cohere Platform

<CodeBlocks>
  ```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClient({
    token: 'Your API key',
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
      // perform web search before answering the question. You can also use your own custom connector.
      connectors: [{ id: 'web-search' }],
    });

    console.log(response);
  })();
  ```

  ```python PYTHON
  import cohere

  co = cohere.Client("Your API key")

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
      # perform web search before answering the question. You can also use your own custom connector.
      connectors=[{"id": "web-search"}],
  )

  print(response)
  ```

  ```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
  	co := client.NewClient(client.WithToken("Your API key"))

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  			Connectors: []*cohere.ChatConnector{
  				{Id: "web-search"},
  			},
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
  ```

  ```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("Your API key").clientName("snippet").build();

          NonStreamedChatResponse response = cohere.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
  ```
</CodeBlocks>

#### Private Deployment

<CodeBlocks>
  ```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClientV2({
    token: '',
    environment: '<YOUR_DEPLOYMENT_URL>'
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
      // perform web search before answering the question. You can also use your own custom connector.
      connectors: [{ id: 'web-search' }],
    });

    console.log(response);
  })();
  ```

  ```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="", base_url="<YOUR_DEPLOYMENT_URL>")

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
      # perform web search before answering the question. You can also use your own custom connector.
      connectors=[{"id": "web-search"}],
  )

  print(response)
  ```

  ```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
    co := client.NewClient(
  			  client.WithBaseURL("<YOUR_DEPLOYMENT_URL>"),
  		)

  	resp, err := co.V2.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  			Connectors: []*cohere.ChatConnector{
  				{Id: "web-search"},
  			},
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
  ```

  ```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().token("Your API key").clientName("snippet").build();
          Cohere cohere = Cohere.builder().environment(Environment.custom("<YOUR_DEPLOYMENT_URL>")).clientName("snippet").build();

          NonStreamedChatResponse response = cohere.v2.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
  ```
</CodeBlocks>

#### Bedrock

<Warning title="Rerank API Compatibility">
  Rerank v3.5 on Bedrock is only supported with Rerank API v2, via `BedrockClientV2()`
</Warning>

<CodeBlocks>
  ```typescript TS 
  const { BedrockClient } = require('cohere-ai');

  const cohere = new BedrockClient({
    awsRegion: "us-east-1",
    awsAccessKey: "...",
    awsSecretKey: "...",
    awsSessionToken: "...",
  });

  (async () => {
    const response = await cohere.chat({
      model: "cohere.command-r-plus-v1:0",
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
  ```

  ```python PYTHON
  import cohere

  co = cohere.BedrockClient(
      aws_region="us-east-1",
      aws_access_key="...",
      aws_secret_key="...",
      aws_session_token="...",
  )

  response = co.chat(
      model="cohere.command-r-plus-v1:0",
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
  ```

  ```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
    "github.com/cohere-ai/cohere-go/v2/core"
  )

  func main() {
  	co := client.NewBedrockClient([]core.RequestOption{}, []client.AwsRequestOption{
  		client.WithAwsRegion("us-east-1"),
  		client.WithAwsAccessKey(""),
  		client.WithAwsSecretKey(""),
  		client.WithAwsSessionToken(""),
  	})

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
  ```

  ```java JAVA
  //Coming Soon
  ```
</CodeBlocks>

#### Sagemaker

<CodeBlocks>
  ```typescript TS 
  const { SagemakerClient } = require('cohere-ai');

  const cohere = new SagemakerClient({
    awsRegion: "us-east-1",
    awsAccessKey: "...",
    awsSecretKey: "...",
    awsSessionToken: "...",
  });

  (async () => {
    const response = await cohere.chat({
      model: "my-endpoint-name",
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
  ```

  ```python PYTHON
  import cohere

  co = cohere.SagemakerClient(
      aws_region="us-east-1",
      aws_access_key="...",
      aws_secret_key="...",
      aws_session_token="...",
  )

  response = co.chat(
      model="my-endpoint-name",
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
  ```

  ```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
    "github.com/cohere-ai/cohere-go/v2/core"
  )

  func main() {
  	co := client.NewSagemakerClient([]core.RequestOption{}, []client.AwsRequestOption{
  		client.WithAwsRegion("us-east-1"),
  		client.WithAwsAccessKey(""),
  		client.WithAwsSecretKey(""),
  		client.WithAwsSessionToken(""),
  	})

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
        Model: cohere.String("my-endpoint-name"),
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
  ```

  ```java JAVA
  //Coming Soon
  ```
</CodeBlocks>

#### Azure

<CodeBlocks>
  ```typescript TS 
  const { CohereClient } = require('cohere-ai');

  const cohere = new CohereClient({
    token: "<azure token>",
    environment: "https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1",
  });

  (async () => {
    const response = await cohere.chat({
      chatHistory: [
        { role: 'USER', message: 'Who discovered gravity?' },
        {
          role: 'CHATBOT',
          message: 'The man who is widely credited with discovering gravity is Sir Isaac Newton',
        },
      ],
      message: 'What year was he born?',
    });

    console.log(response);
  })();
  ```

  ```python PYTHON
  import cohere

  co = cohere.Client(
      api_key="<azure token>",
      base_url="https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1",
  )

  response = co.chat(
      chat_history=[
          {"role": "USER", "message": "Who discovered gravity?"},
          {
              "role": "CHATBOT",
              "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton",
          },
      ],
      message="What year was he born?",
  )

  print(response)
  ```

  ```go GO
  package main

  import (
  	"context"
  	"log"

  	cohere "github.com/cohere-ai/cohere-go/v2"
  	client "github.com/cohere-ai/cohere-go/v2/client"
  )

  func main() {
  	client := client.NewClient(
  		client.WithToken("<azure token>"),
  		client.WithBaseURL("https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1"),
  	)

  	resp, err := co.Chat(
  		context.TODO(),
  		&cohere.ChatRequest{
  			ChatHistory: []*cohere.ChatMessage{
  				{
  					Role:    cohere.ChatMessageRoleUser,
  					Message: "Who discovered gravity?",
  				},
  				{
  					Role:    cohere.ChatMessageRoleChatbot,
  					Message: "The man who is widely credited with discovering gravity is Sir Isaac Newton",
  				}},
  			Message: "What year was he born?",
  		},
  	)

  	if err != nil {
  		log.Fatal(err)
  	}

  	log.Printf("%+v", resp)
  }
  ```

  ```java JAVA
  import com.cohere.api.Cohere;
  import com.cohere.api.requests.ChatRequest;
  import com.cohere.api.types.ChatMessage;
  import com.cohere.api.types.Message;
  import com.cohere.api.types.NonStreamedChatResponse;

  import java.util.List;


  public class ChatPost {
      public static void main(String[] args) {
          Cohere cohere = Cohere.builder().environment(Environment.custom("https://Cohere-command-r-plus-phulf-serverless.eastus2.inference.ai.azure.com/v1")).token("<azure token>").clientName("snippet").build();

          NonStreamedChatResponse response = cohere.chat(
                  ChatRequest.builder()
                          .message("What year was he born?")
                          .chatHistory(
                                  List.of(Message.user(ChatMessage.builder().message("Who discovered gravity?").build()),
                                          Message.chatbot(ChatMessage.builder().message("The man who is widely credited with discovering gravity is Sir Isaac Newton").build()))).build());

          System.out.println(response);
      }
  }
  ```
</CodeBlocks>


# Private Deployment Overview

> This page provides an overview of private deployments of Cohere's models.

## What is a Private Deployment?

Private deployments allow organizations to implement and run AI models within a controlled, internal environment.

In a private deployment, you manage the model deployment infrastructure (with Cohere's guidance and support). This includes ensuring hardware and driver compatibility as well as installing prerequisites to run the containers. These deployments typically run on Kubernetes, but it’s not a firm requirement.

Cohere supports two types of private deployments:

* On-premises (on-prem)
  <br />Gives you full control over both your data and the AI system on your own premises with your own hardware. You procure your own GPUs, servers and other hardware to insulate your environment from external threats.

* On the cloud, typically a virtual private cloud (VPC)
  <br />You use infrastructure needed to host AI models from a cloud provider (such as AWS, Azure, GCP, or OCI) while still retaining control of how the data is stored and processed. Cohere can support any VPC on any cloud environment, so long as the necessary hardware requirements are met.

## Why Private Deployment?

With private deployments, you maintain full control over your infrastructure while leveraging Cohere's state-of-the-art language models.

This enables you to deploy LLMs within your secure network, whether through your chosen cloud provider or your own environment. The data never leaves your environment, and the model can be fully network-isolated.

Here are some of the benefits of private deployments:

* **Data security**: On-prem deployments allow you to keep your data secure and compliant with data protection regulations. A VPC offers similar yet somewhat less rigorous protection.
* **Model customization**: Fine-tuning in a private environment allows enteprises to maintain strict control over their data, avoiding the risk of sensitive or proprietary data leaking.
* **Infrastructure needs**: Public cloud is fast and easily scalable in general. But when the necessary hardware is not available in a specific region, on-prem can provide a faster solution.

## Private Deployment Components

Cohere’s platform container consists of several key components:

* **Endpoints**: API endpoints for model interaction
* **Models**: AI model management and storage
* **Serving Framework**: Manages model serving and request handling
* **Fine-tuning Framework**: Handles model fine-tuning


# Private Deployment – Setting Up

> This page describes the setup required for private deployments of Cohere's models.

## Getting Access

When you [sign up for private deployment](https://cohere.com/contact-sales), you will receive two key pieces of information:

1. A license key for authenticating and pulling model containers
2. A list of artifacts (docker containers) that you can pull using the license key

You can then use the license to pull and run the images, as described in the [provisioning guide](https://docs.cohere.com/docs/single-container-on-private-clouds).

## Infrastructure Requirements

Different models require different hardware requirements, depending on the model types (for example, Command, Embed, and Rerank) and their different versions.

During the engagement, you will be provided with the specific requirements, which will include:

* GPU model, count, and interconnect requirements
* System requirements
* Software and driver versions


# Deploying Models in Private Environments

> Learn how to pull and test Cohere's container images using a license with Docker and Kubernetes.

This document walks through how to pull Cohere's container images using a license, and provides steps for testing both Docker and Kubernetes images.

Before starting, ensure you have a license and image tag provided by Cohere.

## Pull Container Images with A License

Cohere provides access to container images through a registry authenticated with a license. Users can pull these images and replicate them in their environment, as needed, to avoid runtime network access from inside the cluster.

Images will come through the `proxy.replicated.com` registry. Pulling the images will require firewall access open to `proxy.replicated.com` and `proxy-auth.replicated.com`. More information on these endpoints may be found [here](https://docs.replicated.com/enterprise/installing-general-requirements#firewall-openings-for-online-installations).

To test pulling images with a license, modify your docker CLI configuration to include authentication details for the registry. Note: `docker login` will not work.

The docker CLI is only an example; any tool which can pull images with credentials will work with the license ID configured as both username and password. Skopeo is another popular tool for copying images between registries which will work with this flow.

<Info>
  The following commands will overwrite your existing docker CLI configuration with authentication details for Cohere’s registry. If preferred, you can manually add the authentication details to preserve your existing configuration.
</Info>

```
LICENSE_ID="<YOUR LICENSE ID>"

cat <<EOF > ~/.docker/config.json 
{
    "auths": {
        "proxy.replicated.com": {
            "auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"
        }
    }
}
EOF
```

If you prefer to update your docker CLI configuration only for the current terminal session you can export an environment variable instead:

```
LICENSE_ID="<YOUR LICENSE ID>"

export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json"
{
    "auths": {
        "proxy.replicated.com": {
            "auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"
        }
    }
}
EOF
```

Validate that the authenticated image pull works correctly using the docker CLI:

```
CUSTOMER_TAG=image_tag_from_cohere # provided by Cohere
docker pull $CUSTOMER_TAG
```

You can now re-tag and replicate this image anywhere you want, using workflows appropriate to your air-gapped environment.

## Validate Workload Infrastructure

Once you can pull the image from the registry, run a test workload to validate the container's functionality.

### Docker/Containerd

To test the container image with Docker, you should have a machine with the following installed:

* [Nvidia drivers](https://github.com/NVIDIA/open-gpu-kernel-modules) installed on host (the latest tested version is 545).
* [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and corresponding configuration for docker/containerd.

#### Example Usage

Different models have different inputs.

* Embed models expect an array of texts and return the embeddings as output.
* Rerank models expect a list of documents and a query, returning relevance scores for the top `n` results (the `n` parameter is configurable).
* Command models expect a prompt and return the model response.

This section provides simple examples of using each primary Cohere model in a Docker container. Note that if you try these out and get an error like `curl: (7) Failed to connect to localhost port 8080: Connection refused`, the container has not yet fully started up. Wait a few more seconds and then try again.

**Bash Commands for Running Cohere Models Through Docker**

Here are the `bash` commands you can run to use the Embed v4, Embed Multilingual, Rerank English, Rerank Multilingual, and Command models through Docker.

<CodeBlocks>
  ```Text Embed English
  docker run -d --rm --name embed-v4 --gpus=1 --net=host $IMAGE_TAG

  # wait 5-10 seconds for the container to start
  # you can use `curl http://localhost:8080/ping` to check for readiness
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"input_type": "search_query", "texts":["Why are embeddings good"], "embedding_types": ["float"]}'

  {"id":"6d54d453-f2c8-44da-aab8-39e3c11d29d5","texts":["Why are embeddings good"],"embeddings":{"float":[[0.033935547,0.06347656,0.020263672,-0.020507812,0.014160156,0.0038757324,-0.07421875,-0.05859375,...

  docker stop embed-v4
  ```

  ```Text Embed Multilingual
  docker run -d --rm --name multilingual --gpus=1 --net=host $IMAGE_TAG

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing multilingual embeddings"], "input_type": "classification"}'

  {"id":"2eab88e7-5906-44e1-9644-01893a70f1e7","texts":["testing multilingual embeddings"],"embeddings":[[-0.022094727,-0.0121154785,0.037628174,-0.0026988983,-0.0129776,0.013305664,0.005458832,-0.03161621,-0.019744873,-0.026290894,0.017333984,-0.02444458,0.01953125...

  docker stop multilingual
  ```

  ```Text Rerank English
  docker run -d --rm --name rerank-english --gpus=1 --net=host $IMAGE_TAG

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  {"id":"a547bcc5-a243-42dd-8617-d12a7944c164","results":[{"index":1,"relevance_score":0.9734939},{"index":2,"relevance_score":0.73772544}]}

  docker stop rerank-english
  ```

  ```Text Rerank Multilingual
  docker run -d --rm --name rerank-multilingual --gpus=1 --net=host $IMAGE_TAG

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  {"id":"8abeacf2-e657-415c-bab3-ac593e67e8e5","results":[{"index":1,"relevance_score":0.6124835},{"index":2,"relevance_score":0.5305253}],"meta":{"api_version":{"version":"2022-12-06"},"billed_units":{"search_units":1}}}

  docker stop rerank-multilingual
  ```

  ```Text Command
  docker run -d --rm --name command --gpus=2 --net=host $IMAGE_TAG # Number of GPUs may be different depending on the target model

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{"query":"Docker is good because"}'

  {
    "response_id": "dc182f8d-2db1-4b13-806c-e1bcea17f864",
    "text": "Docker is a powerful tool for developing,..."
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "chat_history": [
          {"role": "USER", "message": "Who discovered gravity?"},
          {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
      ],
      "message": "What year was he born?"
  }'

  {
    "response_id": "7938d788-f800-4f9b-a12c-72a96b76a6d6",
    "text": "Sir Isaac Newton was born in Woolsthorpe, England, on January 4, 1643. He was an English physicist, mathematician, astronomer, and natural philosopher who is widely recognized as one of the most...",
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "message": "tell me about penguins",
      "return_chatlog": true,
      "documents": [
        {
          "title": "Tall penguins",
          "snippet": "Emperor penguins are the tallest",
          "url": "http://example.com/foo"
        },
        {
          "title": "Tall penguins",
          "snippet": "Baby penguins are the tallest",
          "url": "https://example.com/foo"
        }
      ],
      "mode": "augmented_generation"
  }'

  {
    "response_id": "8a9f55f6-26aa-455e-bc4c-3e93d4b0d9e6",
    "text": "Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins?",
    "generation_id": "65ef2270-46bb-427d-b54c-2e5f4d7daa90",
    "chatlog": "User: tell me about penguins\nChatbot: Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins? ",
    "token_count": {
      "prompt_tokens": 435,
      "response_tokens": 68,
      "total_tokens": 503
    },
    "meta": {
      "api_version": {
        "version": "2022-12-06"
      },
      "billed_units": {
        "input_tokens": 4,
        "output_tokens": 68
      }
    },
    "citations": [
      {
        "start": 15,
        "end": 40,
        "text": "group of flightless birds",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 58,
        "end": 78,
        "text": "Southern Hemisphere.",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 137,
        "end": 152,
        "text": "Emperor penguin",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 167,
        "end": 174,
        "text": "tallest",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 238,
        "end": 265,
        "text": "tallest species of penguin.",
        "document_ids": [
          "doc_1"
        ]
      }
    ],
    "documents": [
      {
        "id": "doc_1",
        "snippet": "Baby penguins are the tallest",
        "title": "Tall penguins",
        "url": "https://example.com/foo"
      },
      {
        "id": "doc_0",
        "snippet": "Emperor penguins are the tallest",
        "title": "Tall penguins",
        "url": "http://example.com/foo"
      }
    ]
  }

  docker stop command
  ```
</CodeBlocks>

You'll note that final example includes documents that the Command model can use to ground its replies. This functionality falls under [retrieval augmented generation](/docs/retrieval-augmented-generation-rag).

### Kubernetes

Deploying to Kubernetes requires nodes with the following installed:

* [Nvidia drivers](https://github.com/NVIDIA/open-gpu-kernel-modules) - latest tested version is currently 545.
* [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and corresponding configuration for docker/containerd.
* [nvidia-device-plugin](https://github.com/NVIDIA/k8s-device-plugin) to make GPUs available to Kubernetes.

To deploy the same image on Kubernetes, we must first convert the docker configuration into an image pull secret (see the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials) for more detail).

```yaml YAML
kubectl create secret generic cohere-pull-secret \
    --from-file=.dockerconfigjson="~/.docker/config.json" \
    --type=kubernetes.io/dockerconfigjson
```

With that done, fill in the environment variables and generate the application manifest:

```
APP=cohere # or any other name you want to use
IMAGE= <IMAGE_TAG_FROM_COHERE> # replace with the image cohere provided
GPUS= <Number of GPUs for the target model> 

cat <<EOF > cohere.yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: ${APP}
  name: ${APP}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ${APP}
  strategy: {}
  template:
    metadata:
      labels:
        app: ${APP}
    spec:
      imagePullSecrets:
        - name: cohere-pull-secret
      containers:
      - image: ${IMAGE}
        name: ${APP}
        resources:
          limits:
            nvidia.com/gpu: ${GPUS}
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: ${APP}
  name: ${APP}
spec:
  ports:
  - name: http
    port: 8080
    protocol: TCP
    targetPort: 8080
  selector:
    app: ${APP}
  type: ClusterIP
---
EOF
```

<Warning title="The manifest above does not account for air-gapped environments">
  Change this to the registry where you replicated the image previously pulled for an air-gapped deployment. Alternatively, to test in an internet-connected environment, create an image pull secret using the license ID as username/password as in the earlier step for the docker CLI for testing. Keep in mind you will need the firewall rules open mentioned in the image pull steps
</Warning>

Use the following to deploy the containers and run inference requests:

```
kubectl apply -f cohere.yaml
```

Be aware that this is a multi-gigabyte image, so it may take some time to download.

Once the pod is up and running, you should expect to see something like the following:

```
# once the pod is running
kubectl port-forward svc/${APP} 8080:8080

# Forwarding from 127.0.0.1:8080 -> 8080
# Forwarding from [::1]:8080 -> 8080
# Handling connection for 8080
```

Leave that running in the background, and up a new terminal session to execute a test request. In the next few sections, we'll include examples of appropriate requests for the major Cohere models.

**Example Usage**

Here are the `bash` commands you can run to use the Embed English, Embed Multilingual, Rerank English, Rerank Multilingual, and Command models through Kubernetes.

<CodeBlocks>
  ```Text Embed English
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing embeddings in english"], "input_type": "classification"}'

  # {"id":"2ffe4bca-8664-4456-b858-1b3b15411f2c","embeddings":[[-0.5019531,-2.0917969,-1.6220703,-1.2919922,-0.80029297,1.3173828,1.4677734,-1.7763672,0.03869629,1.9033203...}
  ```

  ```Text Embed Multilingual
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing multilingual embeddings"], "input_type": "classification"}'

  # {"id":"2eab88e7-5906-44e1-9644-01893a70f1e7","texts":["testing multilingual embeddings"],"embeddings":[[-0.022094727,-0.0121154785,0.037628174,-0.0026988983,-0.0129776,0.013305664,0.005458832,-0.03161621,-0.019744873,-0.026290894,0.017333984,-0.02444458,0.01953125...
  ```

  ```Text Rerank English
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  # {"id":"a547bcc5-a243-42dd-8617-d12a7944c164","results":[{"index":1,"relevance_score":0.9734939},{"index":2,"relevance_score":0.73772544}]}
  ```

  ```Text Rerank Multilingual
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  # {"id":"8abeacf2-e657-415c-bab3-ac593e67e8e5","results":[{"index":1,"relevance_score":0.6124835},{"index":2,"relevance_score":0.5305253}],"meta":{"api_version":{"version":"2022-12-06"},"billed_units":{"search_units":1}}}
  ```

  ```Text Command
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{"query":"Docker is good because"}'

  {
    "response_id": "dc182f8d-2db1-4b13-806c-e1bcea17f864",
    "text": "Docker is a powerful tool for developing,..."
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "chat_history": [
          {"role": "USER", "message": "Who discovered gravity?"},
          {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
      ],
      "message": "What year was he born?"
  }'

  {
    "response_id": "7938d788-f800-4f9b-a12c-72a96b76a6d6",
    "text": "Sir Isaac Newton was born in Woolsthorpe, England, on January 4, 1643. He was an English physicist, mathematician, astronomer, and natural philosopher who is widely recognized as one of the most...",
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "message": "tell me about penguins",
      "return_chatlog": true,
      "documents": [
        {
          "title": "Tall penguins",
          "snippet": "Emperor penguins are the tallest",
          "url": "http://example.com/foo"
        },
        {
          "title": "Tall penguins",
          "snippet": "Baby penguins are the tallest",
          "url": "https://example.com/foo"
        }
      ],
      "mode": "augmented_generation"
  }'

  {
    "response_id": "8a9f55f6-26aa-455e-bc4c-3e93d4b0d9e6",
    "text": "Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins?",
    "generation_id": "65ef2270-46bb-427d-b54c-2e5f4d7daa90",
    "chatlog": "User: tell me about penguins\nChatbot: Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins? ",
    "token_count": {
      "prompt_tokens": 435,
      "response_tokens": 68,
      "total_tokens": 503
    },
    "meta": {
      "api_version": {
        "version": "2022-12-06"
      },
      "billed_units": {
        "input_tokens": 4,
        "output_tokens": 68
      }
    },
    "citations": [
      {
        "start": 15,
        "end": 40,
        "text": "group of flightless birds",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 58,
        "end": 78,
        "text": "Southern Hemisphere.",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 137,
        "end": 152,
        "text": "Emperor penguin",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 167,
        "end": 174,
        "text": "tallest",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 238,
        "end": 265,
        "text": "tallest species of penguin.",
        "document_ids": [
          "doc_1"
        ]
      }
    ],
    "documents": [
      {
        "id": "doc_1",
        "snippet": "Baby penguins are the tallest",
        "title": "Tall penguins",
        "url": "https://example.com/foo"
      },
      {
        "id": "doc_0",
        "snippet": "Emperor penguins are the tallest",
        "title": "Tall penguins",
        "url": "http://example.com/foo"
      }
    ]
  }
  ```
</CodeBlocks>

Remember that this is only an illustrative deployment. Feel free to modify it as needed to accommodate your environment.

## A Note on Air-gapped Environments

All images in the `proxy.replicated.com` registry are available to pull and copy into an air-gapped environment. These can be pulled using the license ID and steps previously provided by Cohere.


# AWS Private Deployment Guide (EC2 and EKS)

> Deploying Cohere models in AWS via EC2 or EKS for enhanced security, compliance, and control.

## Introduction

This guide walks you through the process of setting up a production-ready environment for deploying Cohere models in AWS.

Private deployment in AWS offers enhanced security, compliance, and control over your infrastructure and applications while leveraging AWS’s reliable and scalable cloud services.

## What this guide will cover

This guide provides comprehensive instructions for deploying applications in a private AWS environment using EC2 instances and Amazon EKS (Elastic Kubernetes Service).

Note: This guide uses an example of deploying the Embed Multilingual 3 model. If you are deploying a different model, the instance sizing will differ – please [contact sales](emailto:team@cohere.com) for further information.

## Prerequisites

Before beginning this deployment, you should have:

* An AWS account with appropriate permissions
* Basic familiarity with AWS services and the AWS console
* Understanding of Linux command line operations
* Knowledge of containerization concepts if deploying containerized applications
* The licence ID and model tag for the model you want to deploy. Please reach out to the [Cohere team](mailto:team@cohere.com) to get these.

Follow this guide sequentially to ensure all components are properly configured for a secure and efficient private deployment in AWS.

## Deploying via EC2 instances

Amazon Elastic Compute Cloud (EC2) provides scalable computing capacity in the AWS cloud and forms the foundation of your private deployment.

In this section, we’ll walk through launching an appropriate GPU-enabled EC2 instance, connecting to it securely, and installing the necessary NVIDIA drivers to utilize the GPU hardware.

The following sections provide a step by step guide to deploy the Embed Multilingual 3 model on EC2.

### Launch EC2 instance

First, launch an EC2 instance with the following specifications:

* Application and OS images - Ubuntu
* Instance Type - g5.2xlarge - 8vCPU
* Storage - 512 GB - root volume

<img src="file:cc24daff-1325-4308-aca3-a267352ebf15" />

<img src="file:1dc1231b-fc1a-4766-9168-e0971de7615c" />

### SSH to the EC2 instance using AWS console - ‘EC2 Instance Connect’ option.

Next, connect to your EC2 instance using the “EC2 Instance Connect” option. This allows you to access the instance through a browser-based client using the default username “ubuntu.” Ensure your instance has a public IPv4 address for successful connection.

<img src="file:c0024b8b-36a6-4df9-915e-99ff32e48690" />

### Install Nvidia drivers

Next, install the NVIDIA drivers on your EC2 instance to enable GPU support. Use the following commands to install the necessary drivers and the NVIDIA CUDA toolkit.

* Nvidia drivers

  ```bash
  sudo apt install -y ubuntu-drivers-common
  sudo ubuntu-drivers install
  sudo apt install nvidia-cuda-toolkit
  ```

  [Further reference](https://documentation.ubuntu.com/aws/en/latest/aws-how-to/instances/install-nvidia-drivers/)

* Nvidia container toolkit

  ```bash
  curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
  sed -i -e '/experimental/ s/^#//g' /etc/apt/sources.list.d/nvidia-container-toolkit.list
  sudo apt-get update
  sudo apt-get install -y nvidia-container-toolkit
  ```

  [Further reference](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

* Reboot the system
  This is often necessary after installing drivers or making significant system changes to ensure all components are properly initialized and running with the latest configurations.

  Before rebooting, restart any mentioned services after running the above commands.

  ```bash
  sudo reboot
  ```

* Verify that the GPU is correctly installed

  ```bash
  nvidia-smi
  ```

<img src="file:03acd401-cc4d-4fe6-8634-cd69e9a19c5f" />

### **Install docker on the instance**

Next, install Docker on your instance. This involves updating the package list, installing Docker, starting the Docker service, and verifying the installation by running a test container.

```bash
sudo apt-get update
sudo apt-get install docker.io -ysudo systemctl start docker
sudo docker run hello-world
sudo systemctl enable docker
docker --version
```

[Further reference](https://medium.com/@srijaanaparthy/step-by-step-guide-to-install-docker-on-ubuntu-in-aws-a39746e5a63d)

### **Define environment variables**

```bash
export CUSTOMER_TAG=proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>
export LICENSE_ID="<YOUR_LICENSE_ID>"
export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json" { "auths": { "proxy.replicated.com": {"auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"}}EOF
```

[Further reference](https://docs.cohere.com/v2/docs/single-container-on-private-clouds)

### **Pull container image**

Next, prepare the environment by obtaining the required software components for deployment.

```bash
sudo docker pull $CUSTOMER_TAG
```

If you encounter an error “permission denied while trying to connect to the Docker daemon socket at”, run the following command:

```bash
sudo chmod 666 /var/run/docker.sock
```

[Further reference](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)

Then, verify that the image has been pulled successfully:

```bash
sudo docker images
```

<img src="file:88861793-4e89-4a71-90cf-17fb897788af" />

### **Start container**

Next, run the Docker container. This starts the container in detached mode with GPU support.

```bash
sudo docker run -d --rm --name embed-english --gpus=1 --net=host proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>

sudo docker ps
```

<img src="file:18a55437-ce7b-43e2-8d07-b33d60c299d2" />

### **Call the model**

Next, test calling the model by executing the `curl` command to send a `POST` request to the local server. This tests the model’s functionality by providing input data for processing.

```bash
curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing multilingual embeddings"], "input_type": "classification"}'
```

## Deploying via EKS (Elastic Kubernetes Service)

Amazon Elastic Kubernetes Service (EKS) provides a managed Kubernetes environment, allowing you to run containerized applications at scale. It leverages Kubernetes’ orchestration capabilities for efficient resource management and scalability.

In this section, we’ll walk through setting up an EKS cluster, configuring it for GPU support, and deploying your application.

### **Launch EKS cluster**

First, launch an EKS cluster by following the steps in the [AWS documentation](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html), and in particular, the steps in Prerequisites and Step 1-4.

The steps in summary:

* Install AWS CLI and Kubectl
* Create the Amazon EKS cluster
* As part of adding nodes to the cluster in step3, use the following
  * AMI type - Amazon Linux 2023 - Nvidia (nvidia drivers pre-installed)
  * Instance Type - g5.2xlarge - 8vCPU
  * Storage - 512 GB

<img src="file:4d84fd66-c540-4b5b-aa84-fc7290639886" />

You can then view the cluster information in the AWS console.

<img src="file:e740810d-ec82-4288-856f-5deeec8d8f48" />

### **Define environment variables**

Next, set environment variables from the machine where the AWS CLI and Kubectl are installed.

```bash
export CUSTOMER_TAG=proxy.replicated.com/proxy/cohere/us-docker.pkg.dev/cohere-artifacts/replicated/single-serving-embed-multilingual-03:<YOUR_MODEL_TAG>
export LICENSE_ID="<YOUR_LICENSE_ID>"
export DOCKER_CONFIG=$(mktemp -d)
cat <<EOF > "${DOCKER_CONFIG}/config.json" { "auths": { "proxy.replicated.com": {"auth": "$(echo -n "${LICENSE_ID}:${LICENSE_ID}" | base64 | tr -d '\n')"}}EOF
kubectl create secret generic cohere-pull-secret --from-file=.dockerconfigjson="{$DOCKER_CONFIG}/config.json" --type=kubernetes.io/dockerconfigjson
```

[Further reference](https://docs.cohere.com/v2/docs/single-container-on-private-clouds)

### **Generate application manifest**

Next, generate an application manifest by creating a file named `cohere.yaml`. The file contents should be copied from [this link](https://docs.cohere.com/v2/docs/single-container-on-private-clouds).

### **Start deployment**

Next, start the deployment by applying the configuration file. Then, check the status and monitor the logs of your pods.

```bash
kubectl apply -f cohere.yaml
kubectl get pods
kubectl logs -f <pod-name-from-above-command>
```

### **Call the model**

Next, run the model by first setting up port forwarding.

```bash
kubectl port-forward svc/cohere 8080:8080
```

Then, open a second window and send a test request using the curl command.

```bash
curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing embeddings in english"], "input_type": "classification"}'
```


# Private Deployment Usage

> This page describes how to use Cohere's SDK to access privately deployed Cohere models.

You can use Cohere's SDK to access privately deployed Cohere models.

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

## Getting Started

The only difference between using Cohere's models on private deployments and the Cohere platform is how you set up the client. With private deployments, you need to pass the following parameters:

* `api_key` - Pass a blank value
* `base_url` - Pass the URL of your private deployment

```python PYTHON
import cohere

co = cohere.ClientV2(
    api_key="",  # Leave this blank
    base_url="<YOUR_DEPLOYMENT_URL>",
)
```

To get started with example use cases, refer to the following quickstart examples:

* [Text Generation (Command model)](https://docs.cohere.com/docs/text-gen-quickstart)
* [RAG (Command model)](https://docs.cohere.com/docs/rag-quickstart)
* [Tool Use (Command model)](https://docs.cohere.com/docs/tool-use-quickstart)
* [Semantic Search (Embed model)](https://docs.cohere.com/docs/sem-search-quickstart)
* [Reranking (Rerank model)](https://docs.cohere.com/docs/reranking-quickstart)

## Integrations

You can use the LangChain library with privately deployed Cohere models. Refer to the [LangChain section](https://docs.cohere.com/docs/chat-on-langchain#using-langchain-on-private-deployments) for more information on setting up LangChain for private deployments.


# Cohere on Amazon Web Services (AWS)

> Access Cohere's language models on AWS with customization options through Amazon SageMaker and Amazon Bedrock.

Developers can access a range of Cohere language models in a private environment via Amazon’s AWS Cloud platform. Cohere’s models are supported on two Amazon services: **Amazon SageMaker** and **Amazon Bedrock**.

### Amazon SageMaker

Amazon SageMaker is a service that allows customers to prepare data and build, train, and deploy machine learning (ML) models for any use case with fully managed infrastructure, tools, and workflows. [Read about SageMaker here.](https://aws.amazon.com/pm/sagemaker/)

Cohere offers a comprehensive suite of generative and embedding models through SageMaker on a range of hardware options, many of which support finetuning for deeper customization and performance.

[View Cohere's products on Amazon SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0).

### Amazon Bedrock

**Amazon Bedrock** is a fully managed service where foundational models from Cohere and other LLM providers are made available through a single, serverless API. [Read about Amazon Bedrock here](http://docs.aws.amazon.com/bedrock).

Cohere has three flagship offerings available on-demand through Amazon Bedrock: Command, the Embed v3 family of models, and Rerank v3.5. Finetuning is also supported for the Command and Command-Light models. Cohere will continue to add products and services to Amazon Bedrock in the coming months.

[View Cohere’s products on Amazon Bedrock](https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/providers?model=command)

### Python SDK

The Cohere Python SDK supports both Amazon SageMaker and Amazon Bedrock. The SDK provides a simple and consistent interface for interacting with Cohere models across platforms.

[cohere-aws SDK on Github](https://github.com/cohere-ai/cohere-aws)

### Pricing

The latest pricing for Cohere models can all be viewed directly from from the listing pages on our Amazon Bedrock and Amazon SageMaker marketplaces. If you have any questions about pricing or deployment options, [please contact our sales team.](https://cohere.com/contact-sales)


# Cohere Models on Amazon Bedrock

> This document provides a guide for using Cohere's models on Amazon Bedrock.

<Note title="Note">
  The code examples in this section use the Cohere v1 API. The v2 API is not yet supported for cloud deployments and will be coming soon.
</Note>

In an effort to make our language-model capabilities more widely available, we've partnered with a few major platforms to create hosted versions of our offerings.

Here, you'll learn how to use Amazon Bedrock to deploy both the Cohere Command and the Cohere Embed models on the AWS cloud computing platform. The following models are available on Bedrock:

* Command R
* Command R+
* Command Light
* Command
* Embed - English
* Embed - Multilingual

Note that the code snippets below are in Python, but you can find the equivalent code for other languages (if they're supported) [here](https://docs.cohere.com/docs/cohere-works-everywhere)

## Prerequisites

Here are the steps you'll need to get set up in advance of running Cohere models on Amazon Bedrock.

* Subscribe to Cohere's models on Amazon Bedrock. For more details, [see here](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
* You'll also have to configure your authentication credentials for AWS. This [document](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) has more information.

## Embeddings

## Embeddings

You can use this code to invoke Cohere’s Embed English v3 model (`cohere.embed-english-v3`) or Embed Multilingual v3 model (`cohere.embed-multilingual-v3`) on Amazon Bedrock:

```python PYTHON
import cohere

co = cohere.BedrockClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

# Input parameters for embed. In this example we are embedding hacker news post titles.
texts = [
    "Interesting (Non software) books?",
    "Non-tech books that have helped you grow professionally?",
    "I sold my company last month for $5m. What do I do with the money?",
    "How are you getting through (and back from) burning out?",
    "I made $24k over the last month. Now what?",
    "What kind of personal financial investment do you do?",
    "Should I quit the field of software development?",
]
input_type = "clustering"
truncate = "NONE"  # optional
model_id = (
    "cohere.embed-english-v3"  # or "cohere.embed-multilingual-v3"
)


# Invoke the model and print the response
result = co.embed(
    model=model_id,
    input_type=input_type,
    texts=texts,
    truncate=truncate,
)  # aws_client.invoke_model(**params)

print(result)
```

Note that we've released multimodal embeddings models that are able to handle images in addition to text. Find [more information here](https://docs.cohere.com/docs/multimodal-embeddings).

## Text Generation

You can use this code to invoke either Command R (`cohere.command-r-v1:0`), Command R+ (`cohere.command-r-plus-v1:0`) on Amazon Bedrock:

```python PYTHON
import cohere

co = cohere.BedrockClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

result = co.chat(
    message="Write a LinkedIn post about starting a career in tech:",
    model="cohere.command-r-plus-v1:0",  # or 'cohere.command-r-v1:0'
)

print(result)
```

## Rerank

You can use this code to invoke our latest Rerank models on Bedrock

```python PYTHON
import cohere

co = cohere.BedrockClientV2(
    aws_region="us-west-2",  # pick a region where the model is available
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

docs = [
    "Carson City is the capital city of the American state of Nevada.",
    "The Commonwealth of the Northern Mariana Islands is a group of islands in the Pacific Ocean. Its capital is Saipan.",
    "Capitalization or capitalisation in English grammar is the use of a capital letter at the start of a word. English usage varies from capitalization in other languages.",
    "Washington, D.C. (also known as simply Washington or D.C., and officially as the District of Columbia) is the capital of the United States. It is a federal district.",
    "Capital punishment has existed in the United States since beforethe United States was a country. As of 2017, capital punishment is legal in 30 of the 50 states.",
]

response = co.rerank(
    model="cohere.rerank-v3-5:0",
    query="What is the capital of the United States?",
    documents=docs,
    top_n=3,
)

print(response)
```


# An Amazon SageMaker Setup Guide

> This document will guide you through enabling development teams to access Cohere’s offerings on Amazon SageMaker.

<Note title="Note">
  The code examples in this section use the Cohere v1 API. The v2 API is not yet supported for cloud deployments and will be coming soon.
</Note>

In an effort to make our language-model capabilities more widely available, we've partnered with a few major platforms to create hosted versions of our offerings.

This document will guide you through enabling development teams to access [Cohere’s offerings on Amazon SageMaker](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0).

## Prerequisites

In order to successfully subscribe to Cohere’s offerings on Amazon SageMaker, the user will need the following **Identity and Access Management (IAM)** permissions:

* **AmazonSageMakerFullAccess**
* **aws-marketplace:ViewSubscriptions**
* **aws-marketplace:Subscribe**
* **aws-marketplace:Unsubscribe**

These permissions allow a user to manage your organization’s Amazon SageMaker subscriptions. Learn more about [managing Amazon’s IAM Permissions here](https://aws.amazon.com/iam/?trk=cf28fddb-12ed-4ffd-981b-b89c14793bf1\&sc_channel=ps\&ef_id=CjwKCAjwsvujBhAXEiwA_UXnAJ4JEQ3KgW0eFBzr5nuwt9L5S7w3A0f3wqensQJgUQ7Mf_ZEdArZRxoCjKQQAvD_BwE:G:s\&s_kwcid=AL!4422!3!652240143562!e!!g!!amazon%20iam!19878797467!148973348604). Contact your AWS administrator if you have questions about account permissions.

## Cohere with Amazon SageMaker Setup

First, navigate to [Cohere’s SageMaker Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=87af0c85-6cf9-4ed8-bee0-b40ce65167e0) to view the available product offerings. Select the product offering to which you are interested in subscribing.

Next, explore the tools on the **Product Detail** page to evaluate how you want to configure your subscription. It contains information related to:

* Pricing: This section allows you to estimate the cost of running inference on different types of instances.
* Usage: This section contains the technical details around supported data formats for each model, and offers links to documentation and notebooks that will help developers scope out the effort required to integrate with Cohere’s models.
* Subscribing: This section will once again present you with both the pricing details and the EULA for final review before you accept the offer. This information is identical to the information on Product Detail page.
* Configuration: The primary goal of this section is to retrieve the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) for the product you have subscribed to.

<Warning>
  For any Cohere 

  *software*

   version after 1.0.5 (or 

  *model*

   version after 3.0.5), the parameter 

  `InferenceAmiVersion=al2-ami-sagemaker-inference-gpu-2`

   must be specified during endpoint configuration (as a variant option) to avoid deployment errors.
</Warning>

## Embeddings

You can use this code to invoke Cohere's embed model on Amazon SageMaker:

```python PYTHON
import cohere

co = cohere.SagemakerClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

# Input parameters for embed. In this example we are embedding hacker news post titles.
texts = [
    "Interesting (Non software) books?",
    "Non-tech books that have helped you grow professionally?",
    "I sold my company last month for $5m. What do I do with the money?",
    "How are you getting through (and back from) burning out?",
    "I made $24k over the last month. Now what?",
    "What kind of personal financial investment do you do?",
    "Should I quit the field of software development?",
]
input_type = "clustering"
truncate = "NONE"  # optional
model_id = "<YOUR ENDPOINT NAME>"  # On SageMaker, you create a model name that you'll pass here.


# Invoke the model and print the response
result = co.embed(
    model=model_id,
    input_type=input_type,
    texts=texts,
    truncate=truncate,
)

print(result)
```

<Warning>
  Cohere's embed models don't support batch transform operations.
</Warning>

Note that we've released multimodal embeddings models that are able to handle images in addition to text. Find [more information here](https://docs.cohere.com/docs/multimodal-embeddings).

## Text Generation

You can use this code to invoke Cohere's Command models on Amazon SageMaker:

```python PYTHON 
import cohere

co = cohere.SagemakerClient(
    aws_region="us-east-1",
    aws_access_key="...",
    aws_secret_key="...",
    aws_session_token="...",
)

# Invoke the model and print the response
result = co.chat(message="Write a LinkedIn post about starting a career in tech:",
                 model="<YOUR ENDPOINT NAME>") # On SageMaker, you create a model name that you'll pass here. 

print(result)
```

## Access Via Amazon SageMaker Jumpstart

Cohere's models are also available on Amazon SageMaker Jumpstart, which makes it easy to access the models with just a few clicks.

To access Cohere's models on SageMaker Jumpstart, follow these steps:

* In the AWS Console, go to Amazon SageMaker and click `Studio`.
* Then, click `Open Studio`. If you don't see this option, you first need to create a user profile.
* This will bring you to the SageMaker Studio page. Look for `Prebuilt and automated solutions` and select `JumpStart`.
* A list of models will appear. To look for Cohere models, type "cohere" in the search bar.
* Select any Cohere model and you will find details about the model and links to further resources.
* You can try out the model by going to the `Notebooks` tab, where you can launch the notebook in JupyterLab.

If you have any questions about this process, reach out to [support@cohere.com](mailto:support@cohere.com).

## Optimize your Inference Latencies

By default, SageMaker endpoints have a random routing strategy. This means that requests coming to the model endpoints are forwarded to the machine learning instances randomly, which can cause latency issues in applications focused on generative AI. In 2023, the SageMaker platform introduced a `RoutingStrategy` parameter allowing you to use the ‘least outstanding requests’ (LOR) approach to routing. With LOR, SageMaker monitors the load of the instances behind your endpoint as well as the models or inference components that are deployed on each instance, then optimally routes requests to the instance that is best suited to serve it.

LOR has shown an improvement in latency under various conditions, and you can find more details [here](https://aws.amazon.com/blogs/machine-learning/minimize-real-time-inference-latency-by-using-amazon-sagemaker-routing-strategies/).

## Next Steps

With your selected configuration and Product ARN available, you now have everything you need to integrate with Cohere’s model offerings on SageMaker.

Cohere recommends your next step be to find the appropriate notebook in [Cohere's list of Amazon SageMaker notebooks](https://github.com/cohere-ai/cohere-aws/tree/main/notebooks/sagemaker), and follow the instructions there, or provide the link to Cohere’s SageMaker notebooks to your development team to implement. The notebooks are thorough, developer-centric guides that will enable your team to begin leveraging Cohere’s endpoints in production for live inference.

If you have further questions about subscribing or configuring Cohere’s product offerings on Amazon SageMaker, please contact our team at [support+aws@cohere.com](mailto:support+aws@cohere.com).


# Deploy Finetuned Command Models from AWS Marketplace

> This document provides a guide for bringing your own finetuned models to Amazon SageMaker.

This document shows you how to deploy your own finetuned [HuggingFace Command-R model](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) using Amazon SageMaker. More specifically, assuming you already have the adapter weights or merged weights from your own finetuned Command model, we will show you how to:

* Merge the adapter weights with the weights of the base model if you only bring the adapter weights;
* Export the merged weights to the TensorRT-LLM inference engine using Amazon SageMaker;
* Deploy the engine as a SageMaker endpoint to serve your business use cases;

You can also find a [companion notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/finetuning/Deploy%20your%20own%20finetuned%20command-r-0824.ipynb) with working code samples.

## Prerequisites

* Ensure that IAM role used has `AmazonSageMakerFullAccess`
* To deploy your model successfully, ensure that either:
  * Your IAM role has these three permissions, and you have authority to make AWS Marketplace subscriptions in the relevant AWS account:
    * `aws-marketplace:ViewSubscriptions`
    * `aws-marketplace:Unsubscribe`
    * `aws-marketplace:Subscribe`
  * Or, your AWS account has a subscription to the packages for [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6). If so, you can skip the "subscribe to the bring your own finetuning algorithm" step below.

**NOTE:** If you're running the companion notebook, know that it contains elements which render correctly in Jupyter interface, so you should open it from an Amazon SageMaker Notebook Instance or Amazon SageMaker Studio.

## Step 1: Subscribe to the bring your own finetuning algorithm

To subscribe to the algorithm:

* Open the algorithm listing page for [Cohere Bring Your Own Fine-tuning](https://aws.amazon.com/marketplace/pp/prodview-5wt5pdnw3bbq6).
* On the AWS Marketplace listing, click on the **Continue to Subscribe** button.
* On the **Subscribe to this software** page, review and click on **Accept Offer** if you and your organization agrees with EULA, pricing, and support terms. On the **Configure and launch** page, make sure the ARN displayed in your region match with the ARN you will use below.

## Step 2: Preliminary setup

First, let's install the Python packages and import them.

```TEXT
pip install "cohere>=5.11.0"
```

```Python PYTHON 
import cohere
import os
import sagemaker as sage

from sagemaker.s3 import S3Uploader
```

Make sure you have access to the resources in your AWS account. For example, you can configure an AWS profile by the command `aws configure sso` (see [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-configure)) and run the command below to set the environment variable `AWS_PROFILE` as your profile name.

```Python PYTHON 
# Change "<aws_profile>" to your own AWS profile name
os.environ["AWS_PROFILE"] = "<aws_profile>"
```

Finally, you need to set all the following variables using your own information. It's best not to add a trailing slash to these paths, as that could mean some parts won't work correctly. You can use either `ml.p4de.24xlarge` or `ml.p5.48xlarge` as the `instance_type` for Cohere Bring Your Own Fine-tuning, but the `instance_type` used for export and inference (endpoint creation) must be identical.

```Python PYTHON 
# The AWS region
region = "<region>"

# Get the arn of the bring your own finetuning algorithm by region
cohere_package = "cohere-command-r-v2-byoft-8370167e649c32a1a5f00267cd334c2c"
algorithm_map = {
    "us-east-1": f"arn:aws:sagemaker:us-east-1:865070037744:algorithm/{cohere_package}",
    "us-east-2": f"arn:aws:sagemaker:us-east-2:057799348421:algorithm/{cohere_package}",
    "us-west-2": f"arn:aws:sagemaker:us-west-2:594846645681:algorithm/{cohere_package}",
    "eu-central-1": f"arn:aws:sagemaker:eu-central-1:446921602837:algorithm/{cohere_package}",
    "ap-southeast-1": f"arn:aws:sagemaker:ap-southeast-1:192199979996:algorithm/{cohere_package}",
    "ap-southeast-2": f"arn:aws:sagemaker:ap-southeast-2:666831318237:algorithm/{cohere_package}",
    "ap-northeast-1": f"arn:aws:sagemaker:ap-northeast-1:977537786026:algorithm/{cohere_package}",
    "ap-south-1": f"arn:aws:sagemaker:ap-south-1:077584701553:algorithm/{cohere_package}",
}
if region not in algorithm_map:
    raise Exception(f"Current region {region} is not supported.")
arn = algorithm_map[region]

# The local directory of your adapter weights. No need to specify this, if you bring your own merged weights
adapter_weights_dir = "<adapter_weights_dir>"

# The local directory you want to save the merged weights. Or the local directory of your own merged weights, if you bring your own merged weights
merged_weights_dir = "<merged_weights_dir>"

# The S3 directory you want to save the merged weights
s3_checkpoint_dir = "<s3_checkpoint_dir>"

# The S3 directory you want to save the exported TensorRT-LLM engine. Make sure you do not reuse the same S3 directory across multiple runs
s3_output_dir = "<s3_output_dir>"

# The name of the export
export_name = "<export_name>"

# The name of the SageMaker endpoint
endpoint_name = "<endpoint_name>"

# The instance type for export and inference. Now "ml.p4de.24xlarge" and "ml.p5.48xlarge" are supported
instance_type = "<instance_type>"
```

## Step 3: Get the merged weights

Assuming you use HuggingFace's [PEFT](https://github.com/huggingface/peft) to finetune [Cohere Command](https://huggingface.co/CohereForAI/c4ai-command-r-08-2024) and get the adapter weights, you can then merge your adapter weights to the base model weights to get the merged weights as shown below. Skip this step if you have already got the merged weights.

```Python PYTHON 
import torch

from peft import PeftModel
from transformers import CohereForCausalLM


def load_and_merge_model(base_model_name_or_path: str, adapter_weights_dir: str):
    """
    Load the base model and the model finetuned by PEFT, and merge the adapter weights to the base weights to get a model with merged weights
    """
    base_model = CohereForCausalLM.from_pretrained(base_model_name_or_path)
    peft_model = PeftModel.from_pretrained(base_model, adapter_weights_dir)
    merged_model = peft_model.merge_and_unload()
    return merged_model


def save_hf_model(output_dir: str, model, tokenizer=None, args=None):
    """
    Save a HuggingFace model (and optionally tokenizer as well as additional args) to a local directory
    """
    os.makedirs(output_dir, exist_ok=True)
    model.save_pretrained(output_dir, state_dict=None, safe_serialization=True)
    if tokenizer is not None:
        tokenizer.save_pretrained(output_dir)
    if args is not None:
        torch.save(args, os.path.join(output_dir, "training_args.bin"))

# Get the merged model from adapter weights
merged_model = load_and_merge_model("CohereForAI/c4ai-command-r-08-2024", adapter_weights_dir)

# Save the merged weights to your local directory
save_hf_model(merged_weights_dir, merged_model)
```

## Step 4. Upload the merged weights to S3

```Python PYTHON
sess = sage.Session()
merged_weights = S3Uploader.upload(merged_weights_dir, s3_checkpoint_dir, sagemaker_session=sess)
print("merged_weights", merged_weights)
```

## Step 5. Export the merged weights to the TensorRT-LLM inference engine

Create Cohere client and use it to export the merged weights to the TensorRT-LLM inference engine. The exported TensorRT-LLM engine will be stored in a tar file `{s3_output_dir}/{export_name}.tar.gz` in S3, where the file name is the same as the `export_name`.

```Python PYTHON 
co = cohere.SagemakerClient(aws_region=region)
co.sagemaker_finetuning.export_finetune(
    arn=arn,
    name=export_name,
    s3_checkpoint_dir=s3_checkpoint_dir,
    s3_output_dir=s3_output_dir,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

## Step 6. Create an endpoint for inference from the exported engine

The Cohere client provides a built-in method to create an endpoint for inference, which will automatically deploy the model from the TensorRT-LLM engine you just exported.

```Python PYTHON 
co.sagemaker_finetuning.create_endpoint(
    arn=arn,
    endpoint_name=endpoint_name,
    s3_models_dir=s3_output_dir,
    recreate=True,
    instance_type=instance_type,
    role="ServiceRoleSagemaker",
)
```

## Step 7. Perform real-time inference by calling the endpoint

Now, you can perform real-time inference by calling the endpoint you just deployed.

```Python PYTHON
# If the endpoint is already deployed, you can directly connect to it
co.sagemaker_finetuning.connect_to_endpoint(endpoint_name=endpoint_name)

message = "Classify the following text as either very negative, negative, neutral, positive or very positive: mr. deeds is , as comedy goes , very silly -- and in the best way."
result = co.sagemaker_finetuning.chat(message=message)
print(result)
```

You can also evaluate your finetuned model using an evaluation dataset. The following is an example with the [ScienceQA](https://scienceqa.github.io/) evaluation using these [data](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/data/scienceQA_eval.jsonl):

```Python PYTHON
import json
from tqdm import tqdm

eval_data_path = "<path_to_scienceQA_eval.jsonl>"

total = 0
correct = 0
for line in tqdm(open(eval_data_path).readlines()):
    total += 1
    question_answer_json = json.loads(line)
    question = question_answer_json["messages"][0]["content"]
    answer = question_answer_json["messages"][1]["content"]
    model_ans = co.sagemaker_finetuning.chat(message=question, temperature=0).text
    if model_ans == answer:
        correct += 1

print(f"Accuracy of finetuned model is %.3f" % (correct / total))
```

## Step 8. Delete the endpoint (optional)

After you successfully performed the inference, you can delete the deployed endpoint to avoid being charged continuously.

```Python PYTHON
co.sagemaker_finetuning.delete_endpoint()
co.sagemaker_finetuning.close()
```

## Step 9. Unsubscribe to the listing (optional)

If you would like to unsubscribe to the model package, follow these steps. Before you cancel the subscription, ensure that you do not have any [deployable models](https://console.aws.amazon.com/sagemaker/home#/models) created from the model package or using the algorithm.

**Note:** You can find this information by looking at the container name associated with the model.

Here's how you do that:

* Navigate to **Machine Learning** tab on the [Your Software subscriptions](https://aws.amazon.com/marketplace/ai/library?productType=ml\&ref_=mlmp_gitdemo_indust) page;
* Locate the listing that you want to cancel the subscription for, and then choose **Cancel Subscription** to cancel the subscription.


# Cohere on the Microsoft Azure Platform

> This page describes how to work with Cohere models on Microsoft Azure.

In an effort to make our language-model capabilities more widely available, we've partnered with a few major platforms to create hosted versions of our offerings.

In this article, you learn how to use [Azure AI Foundry](https://ai.azure.com/) to deploy both the Cohere Command models and the Cohere Embed models on Microsoft's Azure cloud computing platform. You can read more about Azure AI Foundry in its documentation[here](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry).

The following models are available through Azure AI Foundry with pay-as-you-go, token-based billing:

* Command A
* Embed v4
* Embed v3 - English
* Embed v3 - Multilingual
* Cohere Rerank V3.5
* Cohere Rerank V3 (English)
* Cohere Rerank V3 (multilingual)

## Prerequisites

Whether you're using Command or Embed, the initial set up is the same. You'll need:

* An Azure subscription with a valid payment method. Free or trial Azure subscriptions won't work. If you don't have an Azure subscription, create a [paid Azure account](https://azure.microsoft.com/pricing/purchase-options/pay-as-you-go) to begin.
* An [Azure AI hub resource](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-azure-ai-resource). Note: for Cohere models, the pay-as-you-go deployment offering is only available with AI hubs created in the `East US`, `East US 2`, `North Central US`, `South Central US`, `Sweden Central`, `West US` or `West US 3` regions.
* An [Azure AI project](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-projects) in Azure AI Studio.
* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure AI Studio. To perform the required steps, your user account must be assigned the Azure AI Developer role on the resource group. For more information on permissions, see [Role-based access control in Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/rbac-ai-studio).

For workflows based around Command, Embed, or Rerank, you'll also need to create a deployment and consume the model. Here are links for more information:

* **Command:** [create a Command deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#create-a-new-deployment) and then [consume the Command model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#create-a-new-deployment).
* **Embed:** [create an Embed deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#create-a-new-deployment) and [consume the Embed model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#consume-the-cohere-embed-models-as-a-service).
* **Rerank**: [create a Rerank deployment](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-rerank) and [consume the Rerank model](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-rerank#consume-the-cohere-rerank-models-as-a-service).

## Text Generation

We expose two routes for Command R and Command R+ inference:

* `v1/chat/completions` adheres to the Azure AI Generative Messages API schema;
* ` v1/chat` supports Cohere's native API schema.

You can find more information about Azure's API [here](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command#chat-api-reference-for-cohere-models-deployed-as-a-service).

Here's a code snippet demonstrating how to programmatically interact with a Cohere model on Azure:

```python PYTHON
import urllib.request
import json

# Configure payload data sending to API endpoint
data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is good about Wuhan?"},
    ],
    "max_tokens": 500,
    "temperature": 0.3,
    "stream": "True",
}

body = str.encode(json.dumps(data))

# Replace the url with your API endpoint
url = (
    "https://your-endpoint.inference.ai.azure.com/v1/chat/completions"
)

# Replace this with the key for the endpoint
api_key = "your-auth-key"
if not api_key:
    raise Exception("API Key is missing")

headers = {
    "Content-Type": "application/json",
    "Authorization": (api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
```

You can find more code snippets, including examples of how to stream responses, in this [notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/webrequests.ipynb).

Though this section is called "Text Generation", it's worth pointing out that these models are capable of much more. Specifically, you can use Azure-hosted Cohere models for both retrieval augmented generation and [multi-step tool use](/docs/multi-step-tool-use). Check the linked pages for much more information.

Finally, we released refreshed versions of Command R and Command R+ in August 2024, both of which are now available on Azure. Check [these Microsoft docs](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-command?tabs=cohere-command-r-08-2024\&pivots=programming-language-python#:~:text=the%20model%20catalog.-,Cohere%20Command%20chat%20models,-The%20Cohere%20Command) for more information (select the Cohere Command R 08-2024 or Cohere Command R+ 08-2024 tabs).

## Embeddings

We expose two routes for Embed v4 and Embed v3 inference:

* `v1/embeddings` adheres to the Azure AI Generative Messages API schema;
* ` v1/embed` supports Cohere's native API schema.

You can find more information about Azure's API [here](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-embed#embed-api-reference-for-cohere-embed-models-deployed-as-a-service).

```python PYTHON
import urllib.request
import json

# Configure payload data sending to API endpoint
data = {"input": ["hi"]}

body = str.encode(json.dumps(data))

# Replace the url with your API endpoint
url = "https://your-endpoint.inference.ai.azure.com/v1/embedding"

# Replace this with the key for the endpoint
api_key = "your-auth-key"
if not api_key:
    raise Exception("API Key is missing")

headers = {
    "Content-Type": "application/json",
    "Authorization": (api_key),
}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))
    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", "ignore"))
```

## Rerank

We currently exposes the `v1/rerank` endpoint for inference with both Rerank 3 - English and Rerank 3 - Multilingual. For more information on using the APIs, see the [reference](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-cohere-rerank#rerank-api-reference-for-cohere-rerank-models-deployed-as-a-service) section.

```python PYTHON
import cohere

co = cohere.Client(
    base_url="https://<endpoint>.<region>.inference.ai.azure.com/v1",
    api_key="<key>",
)

documents = [
    {
        "Title": "Incorrect Password",
        "Content": "Hello, I have been trying to access my account for the past hour and it keeps saying my password is incorrect. Can you please help me?",
    },
    {
        "Title": "Confirmation Email Missed",
        "Content": "Hi, I recently purchased a product from your website but I never received a confirmation email. Can you please look into this for me?",
    },
    {
        "Title": "Questions about Return Policy",
        "Content": "Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
    {
        "Title": "Customer Support is Busy",
        "Content": "Good morning, I have been trying to reach your customer support team for the past week but I keep getting a busy signal. Can you please help me?",
    },
    {
        "Title": "Received Wrong Item",
        "Content": "Hi, I have a question about my recent order. I received the wrong item and I need to return it.",
    },
    {
        "Title": "Customer Service is Unavailable",
        "Content": "Hello, I have been trying to reach your customer support team for the past hour but I keep getting a busy signal. Can you please help me?",
    },
    {
        "Title": "Return Policy for Defective Product",
        "Content": "Hi, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
    {
        "Title": "Wrong Item Received",
        "Content": "Good morning, I have a question about my recent order. I received the wrong item and I need to return it.",
    },
    {
        "Title": "Return Defective Product",
        "Content": "Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
]

response = co.rerank(
    documents=documents,
    query="What emails have been about returning items?",
    rank_fields=["Title", "Content"],
    top_n=5,
)
```

## Using the Cohere SDK

You can use the Cohere SDK client to consume Cohere models that are deployed via Azure AI Foundry. This means you can leverage the SDK's features such as RAG, tool use, structured outputs, and more.

The following are a few examples on how to use the SDK for the different models.

### Setup

```python PYTHON
# pip install cohere

import cohere

# For Command models
co_chat = cohere.Client(
    api_key="AZURE_INFERENCE_CREDENTIAL",
    base_url="AZURE_MODEL_ENDPOINT",  # Example - https://Cohere-command-r-plus-08-2024-xyz.eastus.models.ai.azure.com/
)

# For Embed models
co_embed = cohere.Client(
    api_key="AZURE_INFERENCE_CREDENTIAL",
    base_url="AZURE_MODEL_ENDPOINT",  # Example - https://cohere-embed-v4-xyz.eastus.models.ai.azure.com/
)

# For Rerank models
co_rerank = cohere.Client(
    api_key="AZURE_INFERENCE_CREDENTIAL",
    base_url="AZURE_MODEL_ENDPOINT",  # Example - https://cohere-rerank-v3-multilingual-xyz.eastus.models.ai.azure.com/
)
```

### Chat

```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates."

response = co_chat.chat(message=message)

print(response)
```

### RAG

```python PYTHON
faqs_short = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
]

query = "Are there fitness-related perks?"

response = co_chat.chat(message=query, documents=faqs_short)

print(response)
```

### Embed

```python PYTHON
docs = [
    "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
    "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee.",
]

doc_emb = co_embed.embed(
    input_type="search_document",
    texts=docs,
).embeddings
```

### Rerank

```python PYTHON
faqs_short = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
]

query = "Are there fitness-related perks?"

results = co_rerank.rerank(
    query=query,
    documents=faqs_short,
    top_n=2,
    model="rerank-english-v3.0",
)
```

Here are some other examples for [Command](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/cohere-cmdR.ipynb) and [Embed](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/cohere/cohere-embed.ipynb).

The important thing to understand is that our new and existing customers can call the models from Azure while still leveraging their integration with the Cohere SDK.


# Cohere on Oracle Cloud Infrastructure (OCI)

> This page describes how to work with Cohere models on Oracle Cloud Infrastructure (OCI)

In an effort to make our language-model capabilities more widely available, we've partnered with a few major platforms to create hosted versions of our offerings.

Here, you'll learn how to use Oracle Cloud Infrastructure (OCI) to deploy both the Cohere Command and the Cohere Embed models on the AWS cloud computing platform. The following models are available on OCI:

* Command R+
* Command R
* Embed English v3
* Embed English v3 light
* Embed Multilingual v3
* Embed Multilingual v3 light
* Cohere Rerank 3.5

We also support fine-tuning for Command R (`command-r-04-2024` and `command-r-08-2024`) on OCI.

For the most updated list of available models, see the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm).

## Working With Cohere Models on OCI

* [Embeddings generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed)

And OCI offers three ways to perform these workloads:

* The console
* The CLI
* The API

In the sections that follow, we'll briefly outline how to use each, and link out to other documentation to fill in any remaining gaps.

### The Console

OCI offers a console through which you can perform many generative AI tasks. It allows you to select your region and the model you wish to use, then pass a prompt to the underlying model, configuring parameters as you wish.

![](file:39ae4ed5-5e48-4ec5-be66-93c1e5112abc)

If you want to use the console for [chat](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-chat.htm), [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "console."

![](file:e12a694e-5281-4700-89c4-b2c0740d18fc)

### The CLI

With OCI's command line interface (CLI), it's possible to use Cohere models to generate text, get embeddings, or extract information.

![](file:a04f2ab5-1976-4ce6-8ab6-3548a9321b77)

If you want to use the console for [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "CLI."

![](file:f447de40-6b8b-41b3-a1a1-7d2f64189a1a)

### The API

If you're trying to use Cohere models on OCI programmatically -- i.e. as part of software development, or while building an application -- you'll likely want to use the API.

![](file:0264654f-b24e-4d43-825a-59844ee53e80)

If you want to use the console for [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "API."

![](file:0030ccb2-b76a-4a9c-b554-c58321f77286)


# Cohere Cookbooks: Build AI Agents and Solutions

> Get started with Cohere's cookbooks to build agents, QA bots, perform searches, and more, all organized by category.

In order to help developers get up and running on using Cohere's functionality, we've put together [some cookbooks](/page/cookbooks) that work through common use cases.

They're organized by categories like "Agents," "Cloud," and "Summarization" to allow you to quickly find what you're looking for. To jump to a particular use-case category, click one of the links below:

* [Agents](/page/cookbooks#agents)
* [Open Source Software Integrations](/page/cookbooks#oss)
* [Search and Embeddings](/page/cookbooks#search)
* [Cloud](/page/cookbooks#cloud)
* [RAG](/page/cookbooks#rag)
* [Summarization](/page/cookbooks#summarization)

<Info title="Note">
  The code examples in this section use the Cohere v1 API. The v2 API counterparts will be published at a later time.
</Info>

Here are some of the ones we think are most exciting!

* [A Data Analyst Agent Built with Cohere and Langchain](/page/data-analyst-agent) - Build a data analyst agent with Python and Cohere's Command R+ mode and Langchain.
* [Creating a QA Bot From Technical Documentation](/page/creating-a-qa-bot) - Create a chatbot that answers user questions based on technical documentation using Cohere embeddings and LlamaIndex.
* [Multilingual Search with Cohere and Langchain](/page/multilingual-search) - Perform searches across a corpus of mixed-language documents with Cohere and Langchain.
* [Using Redis with Cohere](/docs/redis-and-cohere#building-a-retrieval-pipeline-with-cohere-and-redis) - Learn how to use Cohere's text vectorizer with Redis to create a semantic search index.
* [Wikipedia Semantic Search with Cohere + Weaviate](/page/wikipedia-search-with-weaviate) - Search 10 million Wikipedia vectors with Cohere's multilingual model and Weaviate's public dataset.
* [Long Form General Strategies](/page/long-form-general-strategies) - Techniques to address lengthy documents exceeding the context window of LLMs.


# Welcome to LLM University!

> LLM University (LLMU) offers in-depth, practical NLP and LLM training. Ideal for all skill levels. Learn, build, and deploy Language AI with Cohere.

<a target="_blank" href="https://cohere.com/llmu?_gl=1*1ofvam2*_gcl_au*MTQ4NTk2Mzc4Mi4xNzE5OTMzNjE3*_ga*NDY1MzI1MTIxLjE3MTk5MzM2MTc.*_ga_CRGS116RZS*MTcyMzQwMDg1OC4zMi4xLjE3MjM0MDA5MDUuMTMuMC4w">
  <img src="file:7e5a5ada-1323-4131-b521-374ebb51fd02" />
</a>

#### Welcome to LLM University by Cohere!

We’re so happy you’ve chosen to learn Natural Language Processing (NLP) and large language models (LLMs) with us. Please follow [this link](https://cohere.com/llmu) to view the full course.



---

**Navigation:** [← Previous](./04-after.md) | [Index](./index.md) | [Next →](./06-build-an-onboarding-assistant-with-cohere.md)
