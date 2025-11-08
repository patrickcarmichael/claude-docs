# PIPELINE ARCHITECTURE

**Navigation:** [← Previous](./05-supported-llm-providers.md) | [Index](./index.md) | [Next →](./07-use-cases.md)

---

PIPELINE ARCHITECTURE
================================================================================

A Haystack pipeline connects components in a directed acyclic graph (DAG):

    Document Source
         ↓
    DocumentStore (Vector DB)
         ↓
    Retriever
         ↓
    Prompt + LLM
         ↓
    Output

Example Component Flow:
    1. Load documents from various sources
    2. Convert to embeddings
    3. Store in vector database
    4. Create retriever component
    5. Build prompt template
    6. Connect to LLM
    7. Execute pipeline

================================================================================

---

**Navigation:** [← Previous](./05-supported-llm-providers.md) | [Index](./index.md) | [Next →](./07-use-cases.md)
