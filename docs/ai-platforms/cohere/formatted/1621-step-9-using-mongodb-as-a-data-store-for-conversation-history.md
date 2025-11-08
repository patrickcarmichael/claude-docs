---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 9: Using MongoDB as a Data Store for Conversation History

```python
from typing import Dict, Optional, List


class CohereChat:

    def __init__(
        self,
        cohere_client,
        system: str = "",
        database: str = "cohere_chat",
        main_collection: str = "main_collection",
        history_params: Optional[Dict[str, str]] = None,
    ):
        self.co = cohere_client
        self.system = system
        self.history_params = history_params or {}

        # Use the connection string from history_params

        self.client = pymongo.MongoClient(
            self.history_params.get(
                "connection_string", "mongodb://localhost:27017/"
            )
        )

        # Use the database parameter

        self.db = self.client[database]

        # Use the main_collection parameter

        self.main_collection = self.db[main_collection]

        # Use the history_collection from history_params, or default to "chat_history"

        self.history_collection = self.db[
            self.history_params.get(
                "history_collection", "chat_history"
            )
        ]

        # Use the session_id from history_params, or default to "default_session"

        self.session_id = self.history_params.get(
            "session_id", "default_session"
        )

    def add_to_history(self, message: str, prefix: str = ""):
        self.history_collection.insert_one(
            {
                "session_id": self.session_id,
                "message": message,
                "prefix": prefix,
            }
        )

    def get_chat_history(self) -> List[Dict[str, str]]:
        history = self.history_collection.find(
            {"session_id": self.session_id}
        ).sort("_id", 1)
        return [
            {
                "role": (
                    "user" if item["prefix"] == "USER" else "chatbot"
                ),
                "message": item["message"],
            }
            for item in history
        ]

    def rerank_documents(
        self, query: str, documents: List[Dict], top_n: int = 3
    ) -> List[Dict]:
        rerank_docs = [
            {
                "company": doc["company"],
                "combined_attributes": doc["combined_attributes"],
            }
            for doc in documents
            if doc["combined_attributes"].strip()
        ]

        if not rerank_docs:
            print("No valid documents to rerank.")
            return []

        try:
            response = self.co.rerank(
                query=query,
                documents=rerank_docs,
                top_n=top_n,
                model="rerank-english-v3.0",
                rank_fields=["company", "combined_attributes"],
            )

            top_documents_after_rerank = [
                {
                    "company": rerank_docs[result.index]["company"],
                    "combined_attributes": rerank_docs[result.index][
                        "combined_attributes"
                    ],
                    "relevance_score": result.relevance_score,
                }
                for result in response.results
            ]

            print(
                f"\nHere are the top {top_n} documents after rerank:"
            )
            for doc in top_documents_after_rerank:
                print(
                    f"== {doc['company']} (Relevance: {doc['relevance_score']:.4f})"
                )

            return top_documents_after_rerank

        except Exception as e:
            print(f"An error occurred during reranking: {e}")
            return documents[:top_n]

    def format_documents_for_chat(
        self, documents: List[Dict]
    ) -> List[Dict]:
        return [
            {
                "company": doc["company"],
                "combined_attributes": doc["combined_attributes"],
            }
            for doc in documents
        ]

    def send_message(self, message: str, vector_search_func) -> str:
        self.add_to_history(message, "USER")

        # Perform vector search

        search_results = vector_search_func(
            message, self.main_collection
        )

        # Rerank the search results

        reranked_documents = self.rerank_documents(
            message, search_results
        )

        # Format documents for chat

        formatted_documents = self.format_documents_for_chat(
            reranked_documents
        )

        # Generate response using Cohere chat

        response = self.co.chat(
            chat_history=self.get_chat_history(),
            message=message,
            documents=formatted_documents,
            model="command-a-03-2025",
            temperature=0.3,
        )

        result = response.text
        self.add_to_history(result, "CHATBOT")

        print("Final answer:")
        print(result)

        print("\nCitations:")
        for cite in response.citations:
            print(cite)

        return result

    def show_history(self):
        history = self.history_collection.find(
            {"session_id": self.session_id}
        ).sort("_id", 1)
        for item in history:
            print(f"{item['prefix']}: {item['message']}")
            print("-------------------------")
```
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
