---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## (truncated for brevity)

[Citation(start=36, 
          end=81, 
          text='huge in the US at the turn of the millennium.', 
          sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'snippet': "↓ Skip to Main Content\n\nMusic industry – One step closer ...", 'title': 'CSPC: NSYNC Popularity Analysis - ChartMasters'})]),
Citation(start=107, 
          end=154, 
          text='achieved a greater level of success than NSYNC.', 
          sources=[DocumentSource(type='document', id='doc:2', document={'id': 'doc:2', 'snippet': ' 1997, 1998, 2000 and 2001 also rank amongst some of the very best ...', 'title': 'CSPC: Backstreet Boys Popularity Analysis - ChartMasters'})]),
Citation(start=160, 
        end=223,
        ...
...]
```typescript
Not only will we discover that the Backstreet Boys were the more popular band, but the model can also *Tell Me Why*, by providing details [supported by citations](https://docs.cohere.com/docs/documents-and-citations).

For a more in-depth RAG example that leverages the Embed and Rerank endpoints for retrieval, see [End-to-end example of RAG with Chat, Embed, and Rerank](https://docs.cohere.com/v2/docs/rag-complete-example).

### Caveats

It’s worth underscoring that RAG does not guarantee accuracy. It involves giving a model context which informs its replies, but if the provided documents are themselves out-of-date, inaccurate, or biased, whatever the model generates might be as well. What’s more, RAG doesn’t guarantee that a model won’t hallucinate. It greatly reduces the risk, but doesn’t necessarily eliminate it altogether. This is why we put an emphasis on including inline citations, which allow users to verify the information.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
