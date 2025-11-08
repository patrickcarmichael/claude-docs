---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Compression Levels

The Cohere embeddings platform supports compression. The Embed API features an `embeddings_types` parameter which allows the user to specify various ways of compressing the output.

The following embedding types are supported:

* `float`
* `int8`
* `unint8`
* `binary`
* `ubinary`

We recommend being explicit about the `embedding type(s)`. To specify an embedding types, pass one of the types from the list above in as list containing a string:
```python PYTHON
res = co.embed(
    texts=["hello_world"],
    model="embed-v4.0",
    input_type="search_document",
    embedding_types=["int8"],
)
```
You can specify multiple embedding types in a single call. For example, the following call will return both `int8` and `float` embeddings:
```python PYTHON
res = co.embed(
    texts=phrases,
    model="embed-v4.0",
    input_type=input_type,
    embedding_types=["int8", "float"],
)

res.embeddings.int8  # This contains your int8 embeddings

res.embeddings.float  # This contains your float embeddings

```javascript

### A Note on Bits and Bytes

When doing binary compression, there's a subtlety worth pointing out: because Cohere packages *bits* as *bytes* under the hood, the actual length of the vector changes. This means that if you have a vector of 1024 binary embeddings, it will become `1024/8 => 128` bytes, and this might be confusing if you run `len(embeddings)`. This code shows how to unpack it so it works if you're using a vector database that does not take bytes for binary:
```python PYTHON
res = co.embed(
    model="embed-v4.0",
    texts=["hello"],
    input_type="search_document",
    embedding_types=["ubinary"],
    output_dimension=1024,
)
print(
    f"Embed v4 Binary at 1024 dimensions results in length {len(res.embeddings.ubinary[0])}"
)

query_emb_bin = np.asarray(res.embeddings.ubinary[0], dtype="uint8")
query_emb_unpacked = np.unpackbits(query_emb_bin, axis=-1).astype(
    "int"
)
query_emb_unpacked = 2 * query_emb_unpacked - 1
print(
    f"Embed v4 Binary at 1024 unpacked will have dimensions:{len(query_emb_unpacked)}"
)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
