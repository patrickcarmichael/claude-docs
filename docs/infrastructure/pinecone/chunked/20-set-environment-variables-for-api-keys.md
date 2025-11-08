**Navigation:** [← Previous](./19-datadog.md) | [Index](./index.md) | [Next →](./21-integrations.md)

# Set environment variables for API keys
export PINECONE_API_KEY=<your Pinecone API key available at app.pinecone.io>
export OPENAI_API_KEY=<your OpenAI API key, available at platform.openai.com/api-keys>
```

```Python Python theme={null}
import os
pinecone_api_key = os.environ.get('PINECONE_API_KEY')
openai_api_key = os.environ.get('OPENAI_API_KEY')
```

### 2. Build the knowledge base

1. Load a [sample Pinecone dataset](/guides/data/use-public-pinecone-datasets) into memory:

   ```Python Python theme={null}
   import pinecone_datasets  
   dataset = pinecone_datasets.load_dataset('wikipedia-simple-text-embedding-ada-002-100K')  
   len(dataset)  

   # Response:
   # 100000
   ```

2. Reduce the dataset and format it for upserting into Pinecone:

   ```Python Python theme={null}
   # we will use rows of the dataset up to index 30_000
   dataset.documents.drop(dataset.documents.index[30_000:], inplace=True)
   # we drop sparse_values as they are not needed for this example  
   dataset.documents.drop(['metadata'], axis=1, inplace=True)  
   dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)  
   ```

### 3. Index the data in Pinecone

1. Initialize your client connection to Pinecone and create an index. This step uses the Pinecone API key you set as an environment variable [earlier](#1-set-up-your-environment).

   ```Python Python theme={null}
   from pinecone.grpc import PineconeGRPC as Pinecone
   from pinecone import ServerlessSpec, PodSpec  
   import time  
   # configure client  
   pc = Pinecone(api_key=pinecone_api_key)  
   spec = ServerlessSpec(cloud='aws', region='us-east-1')  
   # check for and delete index if already exists  
   index_name = 'langchain-retrieval-augmentation-fast'  
   if pc.has_index(index_name):  
       pc.delete_index(name=index_name)  
   # create a new index  
   pc.create_index(  
       index_name,  
       dimension=1536,  # dimensionality of text-embedding-ada-002  
       metric='dotproduct',  
       spec=spec  
   )  
   ```

2. Target the index and check its current stats:

   ```Python Python theme={null}
   index = pc.Index(index_name)  
   index.describe_index_stats()  

   # Response:
   # {'dimension': 1536,  
   # 'index_fullness': 0.0,  
   # 'namespaces': {},  
   # 'total_vector_count': 0}  
   ```

   You'll see that the index has a `total_vector_count` of `0`, as you haven't added any vectors yet.

3. Now upsert the data to Pinecone:

   ```Python Python theme={null}
   for batch in dataset.iter_documents(batch_size=100):  
       index.upsert(batch)  
   ```

4. Once the data is indexed, check the index stats once again:

   ```Python Python theme={null}
   index.describe_index_stats()  

   # Response:
   # {'dimension': 1536,  
   # 'index_fullness': 0.0,  
   # 'namespaces': {},  
   # 'total_vector_count': 70000} 
   ```

### 4. Initialize a LangChain vector store

Now that you've built your Pinecone index, you need to initialize a LangChain vector store using the index. This step uses the OpenAI API key you set as an environment variable [earlier](#1-set-up-your-environment). Note that OpenAI is a paid service and so running the remainder of this tutorial may incur some small cost.

1. Initialize a LangChain embedding object:

   ```Python Python theme={null}
   from langchain_openai import OpenAIEmbeddings  
   # get openai api key from platform.openai.com  
   model_name = 'text-embedding-ada-002'  
   embeddings = OpenAIEmbeddings(  
       model=model_name,  
       openai_api_key=openai_api_key  
   )  
   ```

2. Initialize the LangChain vector store:

   The `text_field` parameter sets the name of the metadata field that stores the raw text when you upsert records using a LangChain operation such as `vectorstore.from_documents` or `vectorstore.add_texts`.
   This metadata field is used as the `page_content` in the `Document` objects retrieved from query-like LangChain operations such as `vectorstore.similarity_search`.
   If you do not specify a value for `text_field`, it will default to `"text"`.

   ```Python Python theme={null}
   from langchain_pinecone import PineconeVectorStore  
   text_field = "text"  
   vectorstore = PineconeVectorStore(  
       index, embeddings, text_field  
   )  
   ```

3. Now you can query the vector store directly using `vectorstore.similarity_search`:

   ```Python Python theme={null}
   query = "who was Benito Mussolini?"  
   vectorstore.similarity_search(  
       query,  # our search query  
       k=3  # return 3 most relevant docs  
   )  

   # Response:
   # [Document(page_content='Benito Amilcare Andrea Mussolini KSMOM GCTE (29 July 1883 – 28 April 1945) was an Italian politician and journalist...', metadata={'chunk': 0.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
   # Document(page_content='Fascism as practiced by Mussolini\nMussolini\'s form of Fascism, "Italian Fascism"- unlike Nazism, the racist ideology...', metadata={'chunk': 1.0, 'source': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini', 'title': 'Benito Mussolini', 'wiki-id': '6754'}),  
   # Document(page_content='Veneto was made part of Italy in 1866 after a war with Austria. Italian soldiers won Latium in 1870. That was when...', metadata={'chunk': 5.0, 'source': 'https://simple.wikipedia.org/wiki/Italy', 'title': 'Italy', 'wiki-id': '363'})]
   ```

All of these sample results are good and relevant. But what else can you do with this? There are many tasks, one of the most interesting (and well supported by LangChain) is called "Generative Question-Answering" or GQA.

### 5. Use Pinecone and LangChain for RAG

In RAG, you take the query as a question that is to be answered by a LLM, but the LLM must answer the question based on the information it is seeing from the vectorstore.

1. To do this, initialize a `RetrievalQA` object like so:

   ```Python Python theme={null}
   from langchain_openai import ChatOpenAI  
   from langchain.chains import RetrievalQA  
   # completion llm  
   llm = ChatOpenAI(  
       openai_api_key=OPENAI_API_KEY,  
       model_name='gpt-3.5-turbo',  
       temperature=0.0  
   )  
   qa = RetrievalQA.from_chain_type(  
       llm=llm,  
       chain_type="stuff",  
       retriever=vectorstore.as_retriever()  
   )  
   qa.invoke(query)  

   # Response:
   # Benito Mussolini was an Italian politician and journalist who served as the Prime Minister of Italy from 1922 until 1943. He was the leader of the National Fascist Party and played a significant role in the rise of fascism in Italy...
   ```

2. You can also include the sources of information that the LLM is using to answer your question using a slightly different version of `RetrievalQA` called `RetrievalQAWithSourcesChain`:

   ```Python Python theme={null}
   from langchain.chains import RetrievalQAWithSourcesChain  
   qa_with_sources = RetrievalQAWithSourcesChain.from_chain_type(  
       llm=llm,  
       chain_type="stuff",  
       retriever=vectorstore.as_retriever()  
   )  
   qa_with_sources.invoke(query)

   # Response:
   # {'question': 'who was Benito Mussolini?',  
   # 'answer': "Benito Mussolini was an Italian politician and journalist who served as the Prime Minister of Italy from 1922 until 1943. He was the leader of the National Fascist Party and played a significant role in the rise of fascism in Italy...",  
   # 'sources': 'https://simple.wikipedia.org/wiki/Benito%20Mussolini'}  
   ```

### 6. Clean up

When you no longer need the index, use the `delete_index` operation to delete it:

```Python Python theme={null}
pc.delete_index(name=index_name)
```


## Related articles

* [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/)



# Langtrace
Source: https://docs.pinecone.io/integrations/langtrace



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Scale3 Labs recently launched Langtrace AI, an open-source monitoring and evaluation platform for LLM-powered applications. Langtrace is built based on Open Telemetry(OTEL) standards and supports native tracing for the most popular LLM vendors, VectorDBs, and frameworks(like Langchain and LlamaIndex).

Langtrace AI supports tracing Pinecone natively, which means the Langtrace SDK can generate OTEL standard traces with automatic instrumentation in just 2 lines of code. These traces can be ingested by an observability tool that supports OTEL, such as Datadog, Grafana/Prometheus, SigNoz, Sentry, etc. Langtrace also has a visualization client that is optimized for visualizing the traces generated in an LLM stack.

By having a Pinecone integration, Pinecone users can get access to rich and high cardinal tracing for the Pinecone API calls using Langtrace, which they can ingest into their observability tool of choice. This helps customers gain insights into the DB calls and help with debugging and troubleshooting applications in case of incidents.

<PrimarySecondaryCTA primaryHref={"https://langtrace.ai/blog/tracing-pinecone-using-langtrace"} primaryLabel={"Get started"} secondaryHref={"https://www.youtube.com/watch?v=9BM0M8lwTBg"} secondaryLabel={"View video tutorial"} />



# LlamaIndex
Source: https://docs.pinecone.io/integrations/llamaindex

Using LlamaIndex and Pinecone to build semantic search and RAG applications

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

LlamaIndex is a framework for connecting data sources to LLMs, with its chief use case being the end-to-end development of retrieval augmented generation (RAG) applications. LlamaIndex provides the essential abstractions to more easily ingest, structure, and access private or domain-specific data in order to inject these safely and reliably into LLMs for more accurate text generation. It’s available in Python and Typescript.

Seamlessly integrate Pinecone vector database with LlamaIndex to build semantic search and RAG applications.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

[View source](https://github.com/pinecone-io/examples/blob/master/learn/generation/llama-index/using-llamaindex-with-pinecone.ipynb)

[Open in Colab](https://colab.research.google.com/github/pinecone-io/examples/blob/master/learn/generation/llama-index/using-llamaindex-with-pinecone.ipynb)

[LlamaIndex](https://www.llamaindex.ai/) is a framework for connecting data sources to LLMs, with its chief use case being the end-to-end development of [RAG applications](https://www.pinecone.io/learn/retrieval-augmented-generation/). Compared to other similar frameworks, LlamaIndex offers a wide variety of tools for pre- and post-processing your data.

This guide shows you how to use LlamaIndex and Pinecone to both perform traditional semantic search and build a RAG pipeline. Specifically, you will:

* Load, transform, and vectorize sample data with LlamaIndex
* Index and store the vectorized data in Pinecone
* Search the data in Pinecone and use the results to augment an LLM call
* Evaluate the answer you get back from the LLM

<Note>
  This guide demonstrates only one way out of many that you can use LlamaIndex as part of a RAG pipeline. See LlamaIndex's section on [Advanced RAG](https://docs.llamaindex.ai/en/stable/optimizing/advanced%5Fretrieval/advanced%5Fretrieval.html) to learn more about what's possible.
</Note>

### Set up your environment

Before you begin, install some necessary libraries and set environment variables for your Pinecone and OpenAI API keys:

```Shell Shell theme={null}

# Install libraries
pip install -qU \
    "pinecone[grpc]"==5.1.0 \
    llama-index==0.11.4 \
    llama-index-vector-stores-pinecone==0.2.1 \
    llama-index-readers-file==0.2.0 \
    arxiv==2.1.3 \
    setuptools  # (Optional)
```

```Shell Shell theme={null}

# Set environment variables for API keys
export PINECONE_API_KEY=<your Pinecone API key available at app.pinecone.io>
export OPENAI_API_KEY=<your OpenAI API key, available at platform.openai.com/api-keys>
pinecone_api_key = os.environ.get('PINECONE_API_KEY')
openai_api_key = os.environ.get('OPENAI_API_KEY')
```

Also note that all code on this page is run on Python 3.11.

### Load the data

In this guide, you will use the [canonical HNSW paper](https://arxiv.org/pdf/1603.09320.pdf) by Yuri Malkov (PDF) as your sample dataset. Your first step is to download the PDF from arXiv.org and load it into a LlamaIndex loader called [PDF Loader](https://llamahub.ai/l/file-pdf?from=all). This Loader is available (along with many more) on the [LlamaHub](https://llamahub.ai/), which is a directory of data loaders.

```Python Python theme={null}
import arxiv
from pathlib import Path
from llama_index.readers.file import PDFReader


# Download paper to local file system (LFS)

# `id_list` contains 1 item that matches our PDF's arXiv ID
paper = next(arxiv.Client().results(arxiv.Search(id_list=["1603.09320"])))
paper.download_pdf(filename="hnsw.pdf")


# Instantiate `PDFReader` from LlamaHub
loader = PDFReader()


# Load HNSW PDF from LFS
documents = loader.load_data(file=Path('./hnsw.pdf'))


# Preview one of our documents
documents[0]

# Response:

# Document(id_='e25106d2-bde5-41f0-83fa-5cbfa8234bef', embedding=None, metadata={'page_label': '1', 'file_name': 'hnsw.pdf'}, excluded_embed_metadata_keys=[], excluded_llm_metadata_keys=[], relationships={}, text="IEEE TRANSACTIONS ON  JOURNAL NAME,  MANUS CRIPT ID  1 \n Efficient and robust approximate nearest \nneighbor search using Hierarchical Navigable \nSmall World graphs  \nYu. A. Malkov,  D. A. Yashunin  \nAbstract  — We present a new approach for the approximate K -nearest neighbor search based on navigable small world \ngraphs with controllable hierarchy (Hierarchical NSW , HNSW ) and tree alg o-\nrithms", start_char_idx=None, end_char_idx=None, text_template='{metadata_str}\n\n{content}', metadata_template='{key}: {value}', metadata_seperator='\n')
```

You can see above that each `Document` has a ton of useful information, but depending on which Loader you choose, you may have to clean your data. In this case, you need to remove things like remaining `\n` characters and broken, hyphenated words (e.g., `alg o-\nrithms` → `algorithms`).

```Python Python theme={null}

# Clean up our Documents' content
import re

def clean_up_text(content: str) -> str:
    """
    Remove unwanted characters and patterns in text input.

    :param content: Text input.
    
    :return: Cleaned version of original text input.
    """

    # Fix hyphenated words broken by newline
    content = re.sub(r'(\w+)-\n(\w+)', r'\1\2', content)

    # Remove specific unwanted patterns and characters
    unwanted_patterns = [
        "\\n", "  —", "——————————", "—————————", "—————",
        r'\\u[\dA-Fa-f]{4}', r'\uf075', r'\uf0b7'
    ]
    for pattern in unwanted_patterns:
        content = re.sub(pattern, "", content)

    # Fix improperly spaced hyphenated words and normalize whitespace
    content = re.sub(r'(\w)\s*-\s*(\w)', r'\1-\2', content)
    content = re.sub(r'\s+', ' ', content)

    return content


# Call function
cleaned_docs = []
for d in documents: 
    cleaned_text = clean_up_text(d.text)
    d.text = cleaned_text
    cleaned_docs.append(d)


# Inspect output
cleaned_docs[0].get_content()

# Response:

# "IEEE TRANSACTIONS ON JOURNAL NAME, MANUS CRIPT ID 1 Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs Yu. A. Malkov, D. A. Yashunin Abstract We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW , HNSW ) and tree algorithms."


# Great!
```

The value-add of using a file loader from LlamaHub is that your PDF is already broken down into LlamaIndex [Documents](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/documents%5Fand%5Fnodes/root.html#documents-nodes). Along with each Document object comes a [customizable](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/documents%5Fand%5Fnodes/usage%5Fdocuments.html#metadata) metadata dictionary and a hash ID, among other useful artifacts.

### Transform the data

#### Metadata

Now, if you look at one of your cleaned Document objects, you'll see that the default values in your metadata dictionary are not particularly useful.

```Python Python theme={null}
cleaned_docs[0].metadata

# Response:

# {'page_label': '1', 'file_name': 'hnsw.pdf'}
```

To add some metadata that would be more helpful, let's add author name and the paper's title. Note that whatever metadata you add to the metadata dictionary will apply to all [Nodes](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/documents%5Fand%5Fnodes/root.html#nodes), so you want to keep your additions high-level.

<Note>
  LlamaIndex also provides [advanced customizations](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/documents%5Fand%5Fnodes/usage%5Fdocuments.html#advanced-metadata-customization) for what metadata the LLM can see vs the embedding, etc.
</Note>

```Python Python theme={null}

# Iterate through `documents` and add our new key:value pairs
metadata_additions = {"authors": ["Yu. A. Malkov", "D. A. Yashunin"],
  "title": "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"}

 # Update dict in place
[cd.metadata.update(metadata_additions) for cd in cleaned_docs]
 

# Let\'s confirm everything worked:
cleaned_docs[0].metadata

# Response:

# {'page_label': '1',

#      'file_name': 'hnsw.pdf',

#      'authors': ['Yu. A. Malkov', 'D. A. Yashunin'],

#      'title': 'Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs'}


# Great!
```

#### Ingestion pipeline

The easiest way to turn your data into indexable vectors and put those into Pinecone is to make what's called an [Ingestion Pipeline](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/ingestion%5Fpipeline/root.html). Ingestion Pipelines are how you will build a pipeline that will take your list of Documents, parse them into Nodes (or “[chunks](https://www.pinecone.io/learn/chunking-strategies/)” in non-LlamaIndex contexts), vectorize each Node's content, and upsert them into Pinecone.

In the following pipeline, you'll use one of LlamaIndex's newer parsers: the [SemanticSplitterNodeParser](https://docs.llamaindex.ai/en/stable/module%5Fguides/loading/node%5Fparsers/modules.html#semanticsplitternodeparser), which uses OpenAI's [ada-002 embedding model](https://github.com/run-llama/llama%5Findex/blob/47b34d1fdfde2ded134a373b620c3e7a694e8380/llama%5Findex/embeddings/openai.py#L216) to split Documents into semantically coherent Nodes.

This step uses the OpenAI API key you set as an environment variable [earlier](#set-up-your-environment).

```Python Python theme={null}
import os

from llama_index.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings import OpenAIEmbedding
from llama_index.ingestion import IngestionPipeline


# This will be the model we use both for Node parsing and for vectorization
embed_model = OpenAIEmbedding(api_key=openai_api_key)


# Define the initial pipeline
pipeline = IngestionPipeline(
    transformations=[
        SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95, 
            embed_model=embed_model,
            ),
        embed_model,
        ],
    )
```

Hold off on running this pipeline; you will modify it below.

### Upsert the data

Above, you defined an Ingestion Pipeline. There's one thing missing, though: a vector database into which you can upsert your transformed data.

LlamaIndex lets you declare a [VectorStore](https://docs.llamaindex.ai/en/stable/examples/vector%5Fstores/pinecone%5Fmetadata%5Ffilter.html) and add that right into the pipeline for super easy ingestion. Let's do that with Pinecone below.

This step uses the Pinecone API key you set as an environment variable [earlier](#set-up-your-environment).

```Python Python theme={null}
from pinecone.grpc import PineconeGRPC
from pinecone import ServerlessSpec

from llama_index.vector_stores.pinecone import PineconeVectorStore


# Initialize connection to Pinecone
pc = PineconeGRPC(api_key=pinecone_api_key)
index_name = "llama-integration-example"


# Create your index (can skip this step if your index already exists)
pc.create_index(
    index_name,
    dimension=1536,
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)


# Initialize your index 
pinecone_index = pc.Index(index_name)


# Initialize VectorStore
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
```

With your PineconeVectorStore now initialized, you can pop that into your `pipeline` and run it.

```Python Python theme={null}

# Our pipeline with the addition of our PineconeVectorStore
pipeline = IngestionPipeline(
    transformations=[
        SemanticSplitterNodeParser(
            buffer_size=1,
            breakpoint_percentile_threshold=95, 
            embed_model=embed_model,
            ),
        embed_model,
        ],
        vector_store=vector_store  # Our new addition
    )


# Now we run our pipeline!
pipeline.run(documents=cleaned_docs)
```

Now ensure your index is up and running with some Pinecone-native methods like `.describe_index_stats()`:

```Python Python theme={null}
pinecone_index.describe_index_stats()


# Response:

# {'dimension': 1536,

# 'index_fullness': 0.0,

# 'namespaces': {'': {'vector_count': 46}},

# 'total_vector_count': 46}
```

Awesome, your index now has vectors in it. Since you have 46 vectors, you can infer that your `SemanticSplitterNodeParser` split your list of Documents into 46 Nodes.

#### Query the data

To fetch search results from Pinecone itself, you need to make a [VectorStoreIndex](https://docs.llamaindex.ai/en/stable/module%5Fguides/indexing/vector%5Fstore%5Findex.html) object and a [VectorIndexRetriever](https://github.com/run-llama/llama%5Findex/blob/main/llama%5Findex/indices/vector%5Fstore/retrievers/retriever.py#L21) object. You can then pass natural language queries to your Pinecone index and receive results.

```Python Python theme={null}
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever


# Instantiate VectorStoreIndex object from your vector_store object
vector_index = VectorStoreIndex.from_vector_store(vector_store=vector_store)


# Grab 5 search results
retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=5)


# Query vector DB
answer = retriever.retrieve('How does logarithmic complexity affect graph construction?')


# Inspect results
print([i.get_content() for i in answer])


# Response:

# ['some relevant search result 1', 'some relevant search result 1'...]
```

These search results can now be plugged into any downstream task you want.

One of the most common ways to use vector database search results is as additional context to augment a query sent to an LLM. This workflow is what's commonly referred to as a [RAG application](https://www.pinecone.io/learn/retrieval-augmented-generation/).

### Build a RAG app with the data

Building a RAG app with LlamaIndex is very simple.

In theory, you could create a simple [Query Engine](https://docs.llamaindex.ai/en/stable/module%5Fguides/deploying/query%5Fengine/usage%5Fpattern.html#usage-pattern) out of your `vector_index` object by calling `vector_index.as_query_engine().query(‘some query')`, but then you wouldn't be able to specify the number of Pinecone search results you'd like to use as context.

To control how many search results your RAG app uses from your Pinecone index, you will instead create your Query Engine using the [RetrieverQueryEngine](https://github.com/run-llama/llama%5Findex/blob/main/llama%5Findex/query%5Fengine/retriever%5Fquery%5Fengine.py#L21) class. This class allows you to pass in the `retriever` created above, which you configured to retrieve the top 5 search results.

```Python Python theme={null}
from llama_index.core.query_engine import RetrieverQueryEngine


# Pass in your retriever from above, which is configured to return the top 5 results
query_engine = RetrieverQueryEngine(retriever=retriever)


# Now you query:
llm_query = query_engine.query('How does logarithmic complexity affect graph construction?')

llm_query.response

# Response:

# 'Logarithmic complexity in graph construction affects the construction process by organizing the graph into different layers based on their length scale. This separation of links into layers allows for efficient and scalable routing in the graph. The construction algorithm starts from the top layer, which contains the longest links, and greedily traverses through the elements until a local minimum is reached. Then, the search switches to the lower layer with shorter links, and the process repeats. By keeping the maximum number of connections per element constant in all layers, the routing complexity in the graph scales logarithmically. This logarithmic complexity is achieved by assigning an integer level to each element, determining the maximum layer it belongs to. The construction algorithm incrementally builds a proximity graph for each layer, consisting of "short" links that approximate the Delaunay graph. Overall, logarithmic complexity in graph construction enables efficient and robust approximate nearest neighbor search.'
```

You can even inspect the context (Nodes) that informed your LLM's answer using the `.source_nodes` attribute. Let's inspect the first Node:

```Python Python theme={null}
llm_response_source_nodes = [i.get_content() for i in llm_query.source_nodes]

llm_response_source_nodes

# Response:

# ["AUTHOR ET AL.: TITL E 7 be auto-configured by using sample data. The construction process can be easily and efficiently parallelized with only few synchronization points (as demonstrated in Fig. 9) and no measurable effect on index quality. Construction speed/index q uality tradeoff is co ntrolled via the efConstruction parameter. The tradeoff between the search time and the index construction time is presented in Fig. 10 for a 10M SIFT dataset and shows that a reasonable quality index can be constructed for efConstruct ion=100 on a 4X 2.4 GHz 10-core X..."]
```

### Evaluate the data

Now that you've made a RAG app and queried your LLM, you need to evaluate its response.

With LlamaIndex, there are [many ways](https://docs.llamaindex.ai/en/module%5Fguides/evaluating/usage%5Fpattern.html#) to evaluate the results your RAG app generates. A great way to get started with evaluation is to confirm (or deny) that your LLM's responses are relevant, given the context retrieved from your vector database. To do this, you can use LlamaIndex's [RelevancyEvaluator](https://docs.llamaindex.ai/en/stable/examples/evaluation/relevancy%5Feval.html#relevancy-evaluator) class.

The great thing about this type of evaluation is that there is no need for [ground truth data](https://dtunkelang.medium.com/evaluating-search-using-human-judgement-fbb2eeba37d9) (i.e., labeled datasets to compare answers with).

```Python Python theme={null}
from llama_index.core.evaluation import RelevancyEvaluator


# (Need to avoid peripheral asyncio issues)
import nest_asyncio
nest_asyncio.apply()


# Define evaluator
evaluator = RelevancyEvaluator()


# Issue query
llm_response = query_engine.query(
    "How does logarithmic complexity affect graph construction?"
)


# Grab context used in answer query & make it pretty
llm_response_source_nodes = [i.get_content() for i in llm_response.source_nodes]


# # Take your previous question and pass in the response youwe got above
eval_result = evaluator.evaluate_response(query="How does logarithmic complexity affect graph construction?", response=llm_response)


# Print response
print(f'\nGiven the {len(llm_response_source_nodes)} chunks of content (below), is your \     
        LLM\'s response relevant? {eval_result.passing}\n \
        \n ----Contexts----- \n \
        \n{llm_response_source_nodes}')

# Response:

# "Given the 5 chunks of content (below), is your LLM's response relevant? True
         

#  ----Contexts----- 
         

# ['AUTHOR ET AL.: TITL E 7 be auto-configured by using sample data. The construction process can be easily and efficiently parallelized with only few synchronization points (as demonstrated in Fig...']"
```

You can see that there are various attributes you can inspect on your evaluator's result in order to ascertain what's going on behind the scenes. To get a quick binary True/False signal as to whether your LLM is producing relevant results given your context, inspect the `.passing` attribute.

Let's see what happens when we send a totally out of scope query through your RAG app. Issue a random query you know your RAG app won't be able to answer, given what's in your index:

```Python Python theme={null}
query = "Why did the chicken cross the road?"
response = query_engine.query(query)

print(response.response)

# Response:

# "I'm sorry, but I cannot answer that question based on the given context information."


# Evaluate
eval_result = evaluator.evaluate_response(query=query, response=response)

print(str(eval_result.passing))

# Response:

# False  # Our LLM is not taking our context into account, as expected :)
```

As expected, when you send an out-of-scope question through your RAG pipeline, your evaluator says the LLM's answer is not relevant to the retrieved context.

### Summary

As you have seen, LlamaIndex is a powerful framework to use when building semantic search and RAG applications – and we have only gotten to the tip of the iceberg! [Explore more](https://docs.llamaindex.ai/en/index.html) on your own and [let us know how it goes](https://community.pinecone.io/).



# Matillion
Source: https://docs.pinecone.io/integrations/matillion



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Matillion Data Productivity Cloud](https://www.matillion.com/) is a unified platform that helps your team move faster with one central place to build and manage graphical, low-code data pipelines. It allows data teams to use structured, semi-structured, and unstructured data in analytics; build AI pipelines for new use cases; and be more productive.

Matillion Data Productivity Cloud and Pinecone can be used together for retrieval augmented generation (RAG) use cases, helping to contextualize business insights without code.

Matillion supports 150+ pre-built data source connectors, as well as the ability to build custom connectors to any REST API source system, making it easy to chunk unstructured datasets, create embeddings, and upsert to Pinecone.
Matillion's graphical AI Prompt Components integrate with large language models (LLM) running in OpenAI, Amazon Bedrock, Azure OpenAI, and Snowpark Container Services. They enable no-code lookup of external knowledge stored in Pinecone, enabling data engineers to enrich GenAI answers with contextualized and proprietary data.

<PrimarySecondaryCTA primaryLabel={"Get started"} primaryHref={"https://docs.matillion.com/data-productivity-cloud/designer/docs/pinecone-vector-upsert/"} />


## Additional resources

* Video: [Use RAG with a Pinecone Vector database on the Data Productivity Cloud](https://www.youtube.com/watch?v=BsH7WlJdoFs)
* Video: [How to upsert to your Pinecone Vector database](https://www.youtube.com/watch?v=l9qt-EzLkgY)
* [Unlock the power of AI in Data Engineering](https://www.matillion.com/blog/matillion-new-ai-capabilities-for-data-engineering)



# Microsoft Marketplace
Source: https://docs.pinecone.io/integrations/microsoft-marketplace



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Access Pinecone through our Microsoft Marketplace listing. Microsoft Marketplace allows you to manage Pinecone and other third-party software from a centralized location, and simplifies software licensing and procurement with flexible pricing options and multiple deployment methods.

You can set up pay-as-you-go billing for a Pinecone organization through the Microsoft Marketplace

<PrimarySecondaryCTA primaryLabel="Get started" primaryHref="https://marketplace.microsoft.com/product/saas/pineconesystemsinc1688761585469.pineconesaas" />



# New Relic
Source: https://docs.pinecone.io/integrations/new-relic



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

New Relic is an all-in-one observability platform and provides the industry’s first APM solution for AI-powered applications. New Relic is pioneering AI observability with AIM to provide engineers unprecedented visibility and insights across the AI application stack, making it easier to troubleshoot and optimize their AI applications for performance, quality, cost, and responsible use of AI.

Implement monitoring and integrate your Pinecone application with New Relic for performance analysis and insights. The New Relic for Pinecone (Prometheus) quickstart contains one dashboard. These interactive visualizations let you easily explore your data, understand context, and resolve problems faster. It also includes three alerts to detect changes in key performance metrics. Integrate these alerts with your favorite tools (like Slack, PagerDuty, etc.) and New Relic will let you know when something needs your attention.

<PrimarySecondaryCTA primaryLabel={"Get started"} primaryHref={"https://newrelic.com/instant-observability/pinecone-prometheus"} />



# Nexla
Source: https://docs.pinecone.io/integrations/nexla



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Nexla is a Data + AI Integration Platform that makes it easy for users to build data pipelines in a no-code/low-code manner.

The Pinecone integration with Nexla makes it easy for enterprise users to ingest data from systems like Sharepoint, OneDrive, Cloud Storage, Data Warehouses, and 500+ other connectors that Nexla supports natively.

<PrimarySecondaryCTA primaryHref={"https://docs.nexla.com/tutorials/write-to-vector-db/"} primaryLabel={"Get started"} secondaryHref={"https://nexla.com/free-trial/"} secondaryLabel={"Sign up for Nexla"} />



# Nuclia
Source: https://docs.pinecone.io/integrations/nuclia



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

[Nuclia](https://nuclia.com/) RAG-as-a-Service automatically indexes files and documents from both internal and external sources, powering diverse company use cases with large language models (LLMs). This comprehensive indexing capability ensures that organizations can leverage unstructured data effectively, transforming it into actionable insights. With Nuclia's modular Retrieval-Augmented Generation (RAG) system, you can deploy solutions tailored to various operational needs across different deployment options, enhancing flexibility and efficiency.

The modular RAG system from Nuclia is designed to fit specific use cases, allowing you to customize your RAG pipeline to meet your unique requirements. Whether it's defining your own retrieval and chunking strategies or choosing from various embedding models, Nuclia's RAG-as-a-Service makes it easy to bring your tailored solutions into production. This customization not only improves the value of your products but also helps you stay competitive by automating tasks and making your data smarter with LLMs, saving hundreds of hours in the process.

When you create a knowledge box at Nuclia, choose to store the index in Pinecone. This is especially useful for large datasets where full text search is not key on the retrieval phase.

<PrimarySecondaryCTA primaryLabel={"Get started"} primaryHref={"https://docs.nuclia.dev/docs/management/third-party-vector-databases/pinecone/"} />



# OctoAI
Source: https://docs.pinecone.io/integrations/octoai



export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

Harness value from the latest AI innovations by delievering efficient, reliable, and customizable AI systems for your apps. Run your models or checkpoints on OctoAI's cost-effective API endpoints, or run OctoAI's optimized GenAI stack in your environment.

Choose from the best models that OctoAI has to offer, including GTE Large embedding model, the best foundational open source LLMs such as Mixtral-8x7B from Mistral AI, Llama2 from Meta, and highly capable model fine tunes like Nous Hermes 2 Pro Mistral from Nous Research.

As a fully open source solution, Pinecone Canopy and OctoAI is one of the fastest ways and more affordable ways to get started on your RAG journey. Canopy uses Pinecone vector database for storage and retrieval, which is free to use for up to 100k vectors (that's about 30k pages of text).

<PrimarySecondaryCTA primaryLabel={"Get started"} primaryHref={"https://octo.ai/docs/integrations/pinecone"} />



# OpenAI
Source: https://docs.pinecone.io/integrations/openai

Using OpenAI and Pinecone to combine deep learning capabilities for embedding generation with efficient vector storage and retrieval

export const PrimarySecondaryCTA = ({primaryLabel, primaryHref, primaryTarget, secondaryLabel, secondaryHref, secondaryTarget}) => <div style={{
  display: 'flex',
  alignItems: 'center',
  gap: 16
}}>
   {primaryLabel && primaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  background: 'var(--brand-blue)',
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex'
}}>
      <a href={primaryHref} target={primaryTarget} style={{
  paddingLeft: 22,
  paddingRight: 22,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 4,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
        <div style={{
  textAlign: 'justify',
  color: 'var(--text-contrast)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
          {primaryLabel}
        </div>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" style={{
  marginLeft: 2
}}>
          <path d="M9.70492 6L8.29492 7.41L12.8749 12L8.29492 16.59L9.70492 18L15.7049 12L9.70492 6Z" fill="white" style={{
  fille: "var(--text-contrast)"
}} />
        </svg>
      </a>
    </div>}

    {secondaryLabel && secondaryHref && <div style={{
  width: 'fit-content',
  height: 42,
  borderRadius: 4,
  overflow: 'hidden',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  display: 'inline-flex',
  textDecoration: 'none'
}}>
        <a href={secondaryHref} target={secondaryTarget} style={{
  paddingLeft: 11,
  paddingRight: 11,
  paddingTop: 8,
  paddingBottom: 8,
  justifyContent: 'center',
  alignItems: 'center',
  gap: 8,
  display: 'inline-flex',
  textDecoration: 'none',
  borderBottom: 'none'
}}>
          <div style={{
  textAlign: 'justify',
  color: 'var(--brand-blue)',
  fontSize: 15,
  fontWeight: '600',
  letterSpacing: 0.46,
  wordWrap: 'break-word'
}}>
            {secondaryLabel}
          </div>
        </a>
      </div>}

  </div>;

OpenAI's large language models (LLMs) enhance semantic search or “long-term memory” for LLMs. This combo utilizes LLMs' embedding and completion (or generation) endpoints alongside Pinecone's vector search capabilities for nuanced information retrieval.

By integrating OpenAI's LLMs with Pinecone, you can combine deep learning capabilities for embedding generation with efficient vector storage and retrieval. This approach surpasses traditional keyword-based search, offering contextually-aware, precise results.

<PrimarySecondaryCTA secondaryHref={"#setup-guide"} secondaryLabel={"View setup guide"} />


## Setup guide

[View source](https://github.com/pinecone-io/examples/blob/master/integrations/openai/)

[Open in Colab](https://colab.research.google.com/github/pinecone-io/examples/blob/master/integrations/openai/semantic_search_openai.ipynb)

This guide covers the integration of OpenAI's Large Language Models (LLMs) with Pinecone (referred to as the **OP stack**), enhancing semantic search or 'long-term memory' for LLMs. This combo utilizes LLMs' embedding and completion (or generation) endpoints alongside Pinecone's vector search capabilities for nuanced information retrieval.

LLMs like OpenAI's `text-embedding-ada-002` generate vector embeddings, i.e., numerical representations of text semantics. These embeddings facilitate semantic-based rather than literal textual matches. Additionally, LLMs like `gpt-4` or `gpt-3.5-turbo` can predict text completions based on information provided from these contexts.

Pinecone is a vector database designed for storing and querying high-dimensional vectors. It provides fast, efficient semantic search over these vector embeddings.

By integrating OpenAI's LLMs with Pinecone, we combine deep learning capabilities for embedding generation with efficient vector storage and retrieval. This approach surpasses traditional keyword-based search, offering contextually-aware, precise results.

There are many ways of integrating these two tools and we have several guides focusing on specific use-cases. If you already know what you'd like to do you can jump to these specific materials:

* [ChatGPT Plugins Walkthrough](https://youtu.be/hpePPqKxNq8)
* [Ask Lex ChatGPT Plugin](https://github.com/pinecone-io/examples/tree/master/learn/generation/openai/chatgpt/plugins/ask-lex)
* [Generative Question-Answering](https://github.com/pinecone-io/examples/blob/master/docs/gen-qa-openai.ipynb)
* [Retrieval Augmentation using LangChain](https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb)

### Introduction to Embeddings

At the core of the OP stack we have embeddings which are supported via the [OpenAI Embedding API](https://beta.openai.com/docs/guides/embeddings). We index those embeddings in the [Pinecone vector database](https://www.pinecone.io) for fast and scalable retrieval augmentation of our LLMs or other information retrieval use-cases.

*This example demonstrates the core OP stack. It is the simplest workflow and is present in each of the other workflows, but is not the only way to use the stack. Please see the links above for more advanced usage.*

The OP stack is built for semantic search, question-answering, threat-detection, and other applications that rely on language models and a large corpus of text data.

The basic workflow looks like this:

* Embed and index
  * Use the OpenAI Embedding API to generate vector embeddings of your documents (or any text data).
  * Upload those vector embeddings into Pinecone, which can store and index millions/billions of these vector embeddings, and search through them at ultra-low latencies.
* Search
  * Pass your query text or document through the OpenAI Embedding API again.
  * Take the resulting vector embedding and send it as a [query](/guides/search/search-overview) to Pinecone.
  * Get back semantically similar documents, even if they don't share any keywords with the query.

<img src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=7bb594ae2f7a2c13846b2993cd1b3899" alt="Basic workflow of OpenAI and Pinecone" data-og-width="1902" width="1902" data-og-height="864" height="864" data-path="images/6a3ea5a-pinecone-openai-overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=dc5a682918633d319dbeeecb46e50d85 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=16c2456e6c25afe985222aaf7c7945a4 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=405832c780b51b5f471c934d4bf12a58 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=9c0f212e45a2a47423a2ade78d2d533e 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bbd84486e6e4bbb88effa28075301d9c 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/6a3ea5a-pinecone-openai-overview.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=86a650955b6d155da093e7c20ceccb8d 2500w" />

Let's get started...

### Environment Setup

We start by installing the OpenAI and Pinecone clients, we will also need HuggingFace *Datasets* for downloading the TREC dataset that we will use in this guide.

```Bash Bash theme={null}
!pip install -qU \
    pinecone[grpc]==7.3.0 \
    openai==1.93.0 \
    datasets==3.6.0
```

#### Creating Embeddings

To create embeddings we must first initialize our connection to OpenAI Embeddings, we sign up for an API key at [OpenAI](https://beta.openai.com/signup).

```Python Python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="OPENAI_API_KEY"
)  # get API key from platform.openai.com
```

We can now create embeddings with the OpenAI v3 small embedding model like so:

```Python Python theme={null}
MODEL = "text-embedding-3-small"

res = client.embeddings.create(
    input=[
        "Sample document text goes here",
        "there will be several phrases in each batch"
    ], model=MODEL
)
```

In `res` we should find a JSON-like object containing two 1536-dimensional embeddings, these are the vector representations of the two inputs provided above. To access the embeddings directly we can write:

```Python Python theme={null}

# we can extract embeddings to a list
embeds = [record.embedding for record in res.data]
len(embeds)
```

We will use this logic when creating our embeddings for the **T**ext **RE**trieval **C**onference (TREC) question classification dataset later.

#### Initializing a Pinecone Index

Next, we initialize an index to store the vector embeddings. For this we need a Pinecone API key, [sign up for one here](https://app.pinecone.io).

```Python Python theme={null}
import time
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key="...")

spec = ServerlessSpec(cloud="aws", region="us-east-1")

index_name = 'semantic-search-openai'


# check if index already exists (it shouldn't if this is your first run)
if index_name not in pc.list_indexes().names():
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=len(embeds[0]),  # dimensionality of text-embed-3-small
        metric='dotproduct',
        spec=spec
    )


# connect to index
index = pc.Index(index_name)
time.sleep(1)

# view index stats
index.describe_index_stats()
```

#### Populating the Index

With both OpenAI and Pinecone connections initialized, we can move onto populating the index. For this, we need the TREC dataset.

```Python Python theme={null}
from datasets import load_dataset


# load the first 1K rows of the TREC dataset
trec = load_dataset('trec', split='train[:1000]')
```

Then we create a vector embedding for each question using OpenAI (as demonstrated earlier), and `upsert` the ID, vector embedding, and original text for each phrase to Pinecone.

<Warning>
  High-cardinality metadata values (like the unique text values we use here)\
  can reduce the number of vectors that fit on a single pod. See\
  [Known limitations](/reference/api/known-limitations) for more.
</Warning>

```Python Python theme={null}
from tqdm.auto import tqdm

count = 0  # we'll use the count to create unique IDs
batch_size = 32  # process everything in batches of 32
for i in tqdm(range(0, len(trec['text']), batch_size)):
    # set end position of batch
    i_end = min(i+batch_size, len(trec['text']))
    # get batch of lines and IDs
    lines_batch = trec['text'][i: i+batch_size]
    ids_batch = [str(n) for n in range(i, i_end)]
    # create embeddings
    res = client.embeddings.create(input=lines_batch, model=MODEL)
    embeds = [record.embedding for record in res.data]
    # prep metadata and upsert batch
    meta = [{'text': line} for line in lines_batch]
    to_upsert = zip(ids_batch, embeds, meta)
    # upsert to Pinecone
    index.upsert(vectors=list(to_upsert))
```

#### Querying

With our data indexed, we're now ready to move onto performing searches. This follows a similar process to indexing. We start with a text `query`, that we would like to use to find similar sentences. As before we encode this with OpenAI's text similarity Babbage model to create a *query vector* `xq`. We then use `xq` to query the Pinecone index.

```Python Python theme={null}
query = "What caused the 1929 Great Depression?"

xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding
```

Now we query.

```Python Python theme={null}
res = index.query(vector=xq, top_k=5, include_metadata=True)
```

The response from Pinecone includes our original text in the `metadata` field, let's print out the `top_k` most similar questions and their respective similarity scores.

```Python Python theme={null}
for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]:  theme={null}
0.75: Why did the world enter a global depression in 1929 ?
0.60: When was `` the Great Depression '' ?
0.37: What crop failure caused the Irish Famine ?
0.32: What were popular songs and types of songs in the 1920s ?
0.32: When did World War I start ?
```

Looks good, let's make it harder and replace *"depression"* with the incorrect term *"recession"*.

```Python Python theme={null}
query = "What was the cause of the major recession in the early 20th century?"


# create the query embedding
xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding


# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]:  theme={null}
0.63: Why did the world enter a global depression in 1929 ?
0.55: When was `` the Great Depression '' ?
0.34: What were popular songs and types of songs in the 1920s ?
0.33: What crop failure caused the Irish Famine ?
0.29: What is considered the costliest disaster the insurance industry has ever faced ?
```

Let's perform one final search using the definition of depression rather than the word or related words.

```Python Python theme={null}
query = "Why was there a long-term economic downturn in the early 20th century?"


# create the query embedding
xq = client.embeddings.create(input=query, model=MODEL).data[0].embedding


# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)

for match in res['matches']:
    print(f"{match['score']:.2f}: {match['metadata']['text']}")
```

```[Out]:  theme={null}
0.62: Why did the world enter a global depression in 1929 ?
0.54: When was `` the Great Depression '' ?
0.34: What were popular songs and types of songs in the 1920s ?
0.33: What crop failure caused the Irish Famine ?
0.32: What do economists do ?
```

It's clear from this example that the semantic search pipeline is clearly able to identify the meaning between each of our queries. Using these embeddings with Pinecone allows us to return the most semantically similar questions from the already indexed TREC dataset.

Once we're finished with the index we delete it to save resources.

```Python Python theme={null}
pc.delete_index(name=index_name)
```


## Related articles

* [Generative Question-Answering with Long-Term Memory](https://www.pinecone.io/learn/openai-gen-qa)
* [OpenAI's Text Embeddings v3](https://www.pinecone.io/learn/openai-embeddings-v3/)



---
**Navigation:** [← Previous](./19-datadog.md) | [Index](./index.md) | [Next →](./21-integrations.md)
