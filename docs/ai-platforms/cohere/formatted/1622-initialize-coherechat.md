---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Initialize CohereChat

chat = CohereChat(
    co,
    system="You are a helpful assistant taking on the role of an Asset Manager focused on tech companies.",
    database=DB_NAME,
    main_collection=COLLECTION_NAME,
    history_params={
        "connection_string": MONGO_URI,
        "history_collection": "chat_history",
        "session_id": 2,
    },
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
