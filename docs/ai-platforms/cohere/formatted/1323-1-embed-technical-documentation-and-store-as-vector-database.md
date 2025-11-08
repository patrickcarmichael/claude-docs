---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## 1. Embed technical documentation and store as vector database

* Load the dataset from HuggingFace
* Compute embeddings using Cohere's implementation in LlamaIndex, `CohereEmbedding`
* Store inside a vector database, `VectorStoreIndex` from LlamaIndex

Because this process is lengthy (\~2h for all documents on a MacBookPro), we store the index to disc for future reuse. We also provide a (commented) code snippet to index only a subset of the data. If you use this snippet, bear in mind that many documents will become unavailable to the model and, as a result, performance will suffer!
```python PYTHON
data = datasets.load_dataset("sauravjoshi23/aws-documentation-chunked")
print(data)

map_id2index = {sample["id"]: index for index, sample in enumerate(data["train"])}
```
```txt title="Output"
/usr/local/lib/python3.10/dist-packages/huggingface_hub/utils/_token.py:88: UserWarning:
The secret `HF_TOKEN` does not exist in your Colab secrets.
To authenticate with the Hugging Face Hub, create a token in your settings tab (https://huggingface.co/settings/tokens), set it as secret in your Google Colab and restart your session.
You will be able to reuse this secret in all of your notebooks.
Please note that authentication is recommended but still optional to access public models or datasets.
    warnings.warn(


DatasetDict({
    train: Dataset({
        features: ['id', 'text', 'source'],
        num_rows: 187147
    })
})
```
```python PYTHON

overwrite = True # only compute index if it doesn't exist

path_index = Path(".") / "aws-documentation_index_cohere"

embed_model = CohereEmbedding(
    cohere_api_key=api_key,
    model_name="embed-v4.0",
)

if not path_index.exists() or overwrite:
    # Documents are prechunked. Keep them as-is for now

    stub_len = len("https://github.com/siagholami/aws-documentation/tree/main/documents/")
    documents = [
        # -- for indexing full dataset --

        TextNode(
            text=sample["text"],
            title=sample["source"][stub_len:], # save source minus stub

            id_=sample["id"],
        ) for sample in data["train"]
        # -- for testing on subset --

        # TextNode(

        #     text=data["train"][index]["text"],

        #     title=data["train"][index]["source"][stub_len:],

        #     id_=data["train"][index]["id"],

        # ) for index in range(1_000)

    ]
    index = VectorStoreIndex(documents, embed_model=embed_model)
    index.storage_context.persist(path_index)

else:
    storage_context = StorageContext.from_defaults(persist_dir=path_index)
    index = load_index_from_storage(storage_context, embed_model=embed_model)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
