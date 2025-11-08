---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranker To improve Quality

Now we add a retrieval quality improvement step here to make sure only the highest and most semantically similar chunks get sent to our LLM.
```py
query = "What are 'skip-level' meetings?"  # we keep the same query - can change if we want

response = client.rerank.create(
    model="Salesforce/Llama-Rank-V1",
    query=query,
    documents=hybrid_top_k_docs,
    top_n=3,  # we only want the top 3 results but this can be alot higher

)

for result in response.results:
    retreived_chunks += hybrid_top_k_docs[result.index] + "\n\n"

print(retreived_chunks)
```

This will produce the following three chunks from our essay:
```
This chunk refers to "skip-level" meetings, which are a key characteristic of founder mode, where the CEO engages directly with the company beyond their direct reports. This contrasts with the "manager mode" of addressing company issues, where decisions are made perfunctorily via a hierarchical system, to which founders instinctively rebel. that there's a name for it. And once you abandon that constraint there are a huge number of permutations to choose from.For example, Steve Jobs used to run an annual retreat for what he considered the 100 most important people at Apple, and these wer

This chunk discusses the shift in company management away from the "manager mode" that most companies follow, where CEOs engage with the company only through their direct reports, to "founder mode", where CEOs engage more directly with even higher-level employees and potentially skip over direct reports, potentially leading to "skip-level" meetings. ts of, it's pretty clear that it's going to break the principle that the CEO should engage with the company only via his or her direct reports. "Skip-level" meetings will become the norm instead of a practice so unusual that there's a name for it. An

This chunk explains that founder mode, a hypothetical approach to running a company by its founders, will differ from manager mode in that founders will engage directly with the company, rather than just their direct reports, through "skip-level" meetings, disregarding the traditional principle that CEOs should only interact with their direct reports, as managers do.  can already guess at some of the ways it will differ.The way managers are taught to run companies seems to be like modular design in the sense that you treat subtrees of the org chart as black boxes. You tell your direct reports what to do, and it's
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
