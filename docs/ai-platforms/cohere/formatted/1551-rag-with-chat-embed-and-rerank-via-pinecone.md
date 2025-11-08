---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## RAG With Chat Embed and Rerank via Pinecone

> This page contains a basic tutorial on how to build a RAG-powered chatbot.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/RAG_with_Chat_Embed_and_Rerank_via_Pinecone.ipynb" />

This notebook shows how to build a RAG-powered chatbot with Cohere's Chat endpoint. The chatbot can extract relevant information from external documents and produce verifiable, inline citations in its responses.

This application will use several Cohere API endpoints:

* Chat: For handling the main logic of the chatbot, including turning a user message into queries, generating responses, and producing citations
* Embed: For turning textual documents into their embeddings representation, later to be used in retrieval (we’ll use the latest, state-of-the-art Embed v4 model)
* Rerank: For reranking the retrieved documents according to their relevance to a query

The diagram below provides an overview of what we’ll build.

Here is a summary of the steps involved.

Initial phase:

* **Step 0**: Ingest the documents – get documents, chunk, embed, and index.

For each user-chatbot interaction:

* **Step 1**: Get the user message
* **Step 2**: Call the Chat endpoint in query-generation mode
* If at least one query is generated
  * **Step 3**: Retrieve and rerank relevant documents
  * **Step 4**: Call the Chat endpoint in document mode to generate a grounded response with citations
* If no query is generated
  * **Step 4**: Call the Chat endpoint in normal mode to generate a response
```python PYTHON
! pip install cohere hnswlib unstructured python-dotenv -q
```
```python PYTHON
import cohere
from pinecone import Pinecone, PodSpec
import uuid
import hnswlib
from typing import List, Dict
from unstructured.partition.html import partition_html
from unstructured.chunking.title import chunk_by_title

co = cohere.Client("COHERE_API_KEY") # Get your API key here: https://dashboard.cohere.com/api-keys

pc = Pinecone(api_key="PINECONE_API_KEY") # (get API key at app.pinecone.io)

```
```python PYTHON
import cohere
import os
import dotenv

dotenv.load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)
```
First, we define the list of documents we want to ingest and make available for retrieval. As an example, we'll use the contents from the first module of Cohere's *LLM University: What are Large Language Models?*.
```python PYTHON
raw_documents = [
    {
        "title": "Text Embeddings",
        "url": "https://docs.cohere.com/docs/text-embeddings"},
    {
        "title": "Similarity Between Words and Sentences",
        "url": "https://docs.cohere.com/docs/similarity-between-words-and-sentences"},
    {
        "title": "The Attention Mechanism",
        "url": "https://docs.cohere.com/docs/the-attention-mechanism"},
    {
        "title": "Transformer Models",
        "url": "https://docs.cohere.com/docs/transformer-models"}
]
```
Usually the number of documents for practical applications is vast, and so we'll need to be able to search documents efficiently. This involves breaking the documents into chunks, generating embeddings, and indexing the embeddings, as shown in the image below.

We implement this in the `Vectorstore` class below, which takes the `raw_documents` list as input. Three methods are immediately called when creating an object of the `Vectorstore` class:

`load_and_chunk()`\
This method uses the `partition_html()` method from the `unstructured` library to load the documents from URL and break them into smaller chunks. Each chunk is turned into a dictionary object with three fields:

* `title` - the web page’s title,
* `text` - the textual content of the chunk, and
* `url` - the web page’s URL.

`embed()`\
This method uses Cohere's `embed-v4.0` model to generate embeddings of the chunked documents. Since our documents will be used for retrieval, we set `input_type="search_document"`. We send the documents to the Embed endpoint in batches, because the endpoint has a limit of 96 documents per call.

`index()`\
This method uses the `hsnwlib` package to index the document chunk embeddings. This will ensure efficient similarity search during retrieval. Note that `hnswlib` uses a vector library, and we have chosen it for its simplicity.
```python PYTHON
class Vectorstore:
    """
    A class representing a collection of documents indexed into a vectorstore.

    Parameters:
    raw_documents (list): A list of dictionaries representing the sources of the raw documents. Each dictionary should have 'title' and 'url' keys.

    Attributes:
    raw_documents (list): A list of dictionaries representing the raw documents.
    docs (list): A list of dictionaries representing the chunked documents, with 'title', 'text', and 'url' keys.
    docs_embs (list): A list of the associated embeddings for the document chunks.
    docs_len (int): The number of document chunks in the collection.
    idx (hnswlib.Index): The index used for document retrieval.

    Methods:
    load_and_chunk(): Loads the data from the sources and partitions the HTML content into chunks.
    embed(): Embeds the document chunks using the Cohere API.
    index(): Indexes the document chunks for efficient retrieval.
    retrieve(): Retrieves document chunks based on the given query.
    """

    def __init__(self, raw_documents: List[Dict[str, str]]):
        self.raw_documents = raw_documents
        self.docs = []
        self.docs_embs = []
        self.retrieve_top_k = 10
        self.rerank_top_k = 3
        self.load_and_chunk()
        self.embed()
        self.index()


    def load_and_chunk(self) -> None:
        """
        Loads the text from the sources and chunks the HTML content.
        """
        print("Loading documents...")

        for raw_document in self.raw_documents:
            elements = partition_html(url=raw_document["url"])
            chunks = chunk_by_title(elements)
            for chunk in chunks:
                self.docs.append(
                    {
                        "title": raw_document["title"],
                        "text": str(chunk),
                        "url": raw_document["url"],
                    }
                )

    def embed(self) -> None:
        """
        Embeds the document chunks using the Cohere API.
        """
        print("Embedding document chunks...")

        batch_size = 90
        self.docs_len = len(self.docs)
        for i in range(0, self.docs_len, batch_size):
            batch = self.docs[i : min(i + batch_size, self.docs_len)]
            texts = [item["text"] for item in batch]
            docs_embs_batch = co.embed(
                texts=texts, model="embed-v4.0", input_type="search_document"
            ).embeddings
            self.docs_embs.extend(docs_embs_batch)

    def index(self) -> None:
        """
        Indexes the documents for efficient retrieval.
        """
        print("Indexing documents...")

        index_name = 'rag-01'

        # If the index does not exist, we create it

        if index_name not in pc.list_indexes().names():
            pc.create_index(
                name=index_name,
                dimension=len(self.docs_embs[0]),
                metric="cosine",
                spec=PodSpec(
                    environment="gcp-starter"
                )
                )

        # connect to index

        self.idx = pc.Index(index_name)

        batch_size = 128

        ids = [str(i) for i in range(len(self.docs))]
        # create list of metadata dictionaries

        meta = self.docs

        # create list of (id, vector, metadata) tuples to be upserted

        to_upsert = list(zip(ids, self.docs_embs, meta))

        for i in range(0, len(self.docs), batch_size):
            i_end = min(i+batch_size, len(self.docs))
            self.idx.upsert(vectors=to_upsert[i:i_end])

        # let's view the index statistics

        print("Indexing complete")


    def retrieve(self, query: str) -> List[Dict[str, str]]:
        """
        Retrieves document chunks based on the given query.

        Parameters:
        query (str): The query to retrieve document chunks for.

        Returns:
        List[Dict[str, str]]: A list of dictionaries representing the retrieved document chunks, with 'title', 'text', and 'url' keys.
        """

        docs_retrieved = []
        query_emb = co.embed(
            texts=[query], model="embed-v4.0", input_type="search_query"
        ).embeddings


        res = self.idx.query(vector=query_emb, top_k=self.retrieve_top_k, include_metadata=True)
        docs_to_rerank = [match['metadata']['text'] for match in res['matches']]

        rerank_results = co.rerank(
            query=query,
            documents=docs_to_rerank,
            top_n=self.rerank_top_k,
            model="rerank-english-v2.0",
        )

        docs_reranked = [res['matches'][result.index] for result in rerank_results.results]

        for doc in docs_reranked:
            docs_retrieved.append(doc['metadata'])

        return docs_retrieved
```
In the code cell below, we initialize an instance of the `Vectorstore` class and pass in the `raw_documents` list as input.
```python PYTHON
vectorstore = Vectorstore(raw_documents)
```
```
Loading documents...
Embedding document chunks...
Indexing documents...
Indexing complete
```
The `Vectorstore` class also has a `retrieve()` method, which we'll use to retrieve relevant document chunks given a query (as in Step 3 in the diagram shared at the beginning of this notebook). This method has two components: (1) dense retrieval, and (2) reranking.

### Dense retrieval

First, we embed the query using the same `embed-v4.0` model we used to embed the document chunks, but this time we set `input_type="search_query"`.

Search is performed by the `knn_query()` method from the `hnswlib` library. Given a query, it returns the document chunks most similar to the query. We can define the number of document chunks to return using the attribute `self.retrieve_top_k=10`.

### Reranking

After semantic search, we implement a reranking step. While our semantic search component is already highly capable of retrieving relevant sources, the [Rerank endpoint](https://cohere.com/rerank) provides an additional boost to the quality of the search results, especially for complex and domain-specific queries. It takes the search results and sorts them according to their relevance to the query.

We call the Rerank endpoint with the `co.rerank()` method and define the number of top reranked document chunks to retrieve using the attribute `self.rerank_top_k=3`. The model we use is `rerank-english-v2.0`.

This method returns the top retrieved document chunks `chunks_retrieved` so that they can be passed to the chatbot.

In the code cell below, we check the document chunks that are retrieved for the query `"multi-head attention definition"`.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
