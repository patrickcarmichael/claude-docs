# RAG Application: LangChain + Pinecone + Anthropic

This example demonstrates a complete Retrieval-Augmented Generation (RAG) application that combines:
- **LangChain**: Framework for building LLM applications
- **Pinecone**: Vector database for semantic search
- **Anthropic Claude**: State-of-the-art language model for generation

## Overview

A RAG application retrieves relevant context from a vector database and uses it to augment the LLM's generation capabilities. This pattern is ideal for:
- Question-answering over custom documents
- Knowledge base systems
- Domain-specific chatbots
- Document analysis at scale

### Architecture Flow

```
User Query
    ↓
[1] Embedding Generation (Claude Embeddings or OpenAI)
    ↓
[2] Semantic Search (Pinecone Vector DB)
    ↓
[3] Retrieved Context
    ↓
[4] Context + Query → Claude API
    ↓
Generated Response
```

## Features

- Load documents from files or directories
- Generate embeddings using OpenAI or Anthropic models
- Store and index vectors in Pinecone
- Retrieve semantically similar documents
- Generate responses with Claude API
- Example with sample data (PDFs, markdown, text)

## Requirements

### System Requirements
- Python 3.9+
- pip or conda
- API keys for: Anthropic, Pinecone, OpenAI (for embeddings)

### Dependencies

```
langchain>=0.1.0
langchain-community>=0.0.10
langchain-anthropic>=0.1.0
pinecone-client>=3.0.0
python-dotenv>=1.0.0
pypdf>=3.0.0
```

See `requirements.txt` for complete list.

## Installation

### 1. Clone and Setup

```bash
cd examples/rag-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set Environment Variables

Create a `.env` file:

```env
# Anthropic API (for generation)
ANTHROPIC_API_KEY=sk-ant-...

# OpenAI API (for embeddings)
OPENAI_API_KEY=sk-...

# Pinecone Vector Database
PINECONE_API_KEY=pcsk_...
PINECONE_ENVIRONMENT=us-east1-aws
PINECONE_INDEX_NAME=rag-documents
```

### 3. Initialize Pinecone Index

```bash
python scripts/init_pinecone.py
```

This creates a Pinecone index with dimension 1536 (for OpenAI embeddings).

## Usage

### Quick Start

```bash
# Ingest documents into the vector store
python ingest.py --path ./data/documents

# Run interactive chat
python chat.py

# Query the RAG system
python query.py "What are the main features of Claude Code?"
```

### Advanced Usage

```bash
# Clear and reingest documents
python ingest.py --path ./data/documents --clear

# Use custom embedding model
EMBEDDING_MODEL=anthropic python chat.py

# Batch process queries
python batch_query.py --input queries.txt --output results.json
```

## File Structure

```
rag-app/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── config.py                # Configuration and constants
├── ingest.py                # Document ingestion pipeline
├── chat.py                  # Interactive chat interface
├── query.py                 # Single query execution
├── batch_query.py           # Batch query processing
├── retriever.py             # RAG retriever logic
├── scripts/
│   └── init_pinecone.py    # Initialize Pinecone index
├── data/
│   └── documents/          # Sample documents (PDF, MD, TXT)
└── utils/
    ├── document_loader.py  # Load various document types
    └── prompt_templates.py # LLM prompt templates
```

## Key Components

### 1. Document Ingestion (`ingest.py`)

Loads documents, chunks them, generates embeddings, and stores in Pinecone.

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone

loader = DirectoryLoader('./data/documents')
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
chunks = splitter.split_documents(docs)

# Store in Pinecone
vectorstore = Pinecone.from_documents(chunks, embeddings, index_name='rag-documents')
```

### 2. Retrieval (`retriever.py`)

Retrieves relevant documents based on semantic similarity.

```python
from langchain.chains import RetrievalQA
from langchain.llms import Anthropic

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
qa = RetrievalQA.from_chain_type(
    llm=Anthropic(),
    chain_type="stuff",
    retriever=retriever
)
```

### 3. Generation (`chat.py`)

Interactive chat with context from retrieved documents.

```python
query = "How do I set up Claude Code?"
result = qa.run(query)
print(f"Response: {result}")
```

## Documentation References

- **LangChain**: `/docs/ai-frameworks/langchain/` - Framework documentation
- **Pinecone**: `/docs/infrastructure/pinecone/` - Vector database docs
- **Anthropic Claude**: `/docs/ai-platforms/anthropic/` - Claude API reference
- **Claude Code**: `/docs/claude-code/` - Using Claude Code to build this

## Customization

### Change Embedding Model

```python
# Use Anthropic embeddings (optional)
from langchain.embeddings.anthropic import AnthropicEmbeddings
embeddings = AnthropicEmbeddings()

# Use OpenAI embeddings (default)
from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()
```

### Adjust Chunk Size and Overlap

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,      # Larger chunks for longer documents
    chunk_overlap=200,    # Overlap for context continuity
    separators=["\n\n", "\n", " ", ""]
)
```

### Use Different LLM Models

```python
from langchain.llms import Anthropic

# Use Claude 3 Opus
llm = Anthropic(model="claude-3-opus-20240229")

# Use Claude 3.5 Sonnet (recommended)
llm = Anthropic(model="claude-3-5-sonnet-20241022")
```

### Customize System Prompt

Edit `utils/prompt_templates.py` to change the system prompt and instructions.

## Performance Tips

1. **Chunk Size**: Larger chunks (2000-4000 tokens) for dense documents, smaller (500-1000) for web content
2. **Search Results**: Retrieve 4-8 documents (k=4 to k=8) - more is slower, fewer misses context
3. **Reranking**: Use CrossEncoder to rerank results before passing to LLM
4. **Caching**: Cache embeddings to avoid recomputing for identical queries
5. **Batching**: Process multiple queries together for efficiency

## Troubleshooting

### "Pinecone index not found"
```bash
python scripts/init_pinecone.py
```

### "Embedding dimension mismatch"
Ensure embedding model matches Pinecone index dimension (1536 for OpenAI, 768 for smaller models).

### "API key errors"
Check `.env` file and verify keys are correctly set:
```bash
echo $ANTHROPIC_API_KEY  # Should print your key
```

### "Out of context window"
Reduce chunk size or number of retrieved documents:
```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
```

## Next Steps

1. **Add more documents**: Place PDFs, markdown files in `data/documents/`
2. **Implement web search**: Add internet search capability via SearchAPIWrapper
3. **Add metadata filtering**: Filter documents by source, date, category
4. **Deploy to production**: Use LangServe for API, Vercel for UI
5. **Monitor and evaluate**: Track query quality, latency, token usage

## Related Examples

- [Chat Interface](../chat-interface/) - Build a Next.js frontend for this RAG app
- [Multi-Agent System](../multi-agent/) - Use RAG with CrewAI agents
- [Claude Code Automation](../claude-code-automation/) - Automate RAG setup with Claude Code

## Resources

- LangChain RAG Guide: https://docs.langchain.com/docs/use_cases/qa_structured_data
- Pinecone RAG Quickstart: https://docs.pinecone.io/guides/gen-ai/rag-complete-guide
- Anthropic Claude API: https://docs.anthropic.com/
- llms.txt Standard: https://llmstxt.org/

---

*Example demonstrates the integration of LangChain, Pinecone, and Anthropic Claude for building production-ready RAG applications.*
