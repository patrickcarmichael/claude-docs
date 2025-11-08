---
title: "Crewai: Store text and embeddings in Qdrant"
description: "Store text and embeddings in Qdrant section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Store text and embeddings in Qdrant

def load_pdf_to_qdrant(pdf_path, qdrant, collection_name):
    # Extract text from PDF
    text_chunks = extract_text_from_pdf(pdf_path)

    # Create Qdrant collection
    if qdrant.collection_exists(collection_name):
        qdrant.delete_collection(collection_name)
    qdrant.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=3072, distance=Distance.COSINE)
    )

    # Store embeddings
    points = []
    for chunk in text_chunks:
        embedding = get_openai_embedding(chunk)
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={"text": chunk}
        ))
    qdrant.upsert(collection_name=collection_name, points=points)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Generate OpenAI embeddings](./832-generate-openai-embeddings.md)

**Next:** [Initialize Qdrant client and load data →](./834-initialize-qdrant-client-and-load-data.md)
