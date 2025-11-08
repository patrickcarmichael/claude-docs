---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Retrieve documents

For this example, we'll work with documents that have already been retrieved through an initial search stage (which could be semantic search, keyword matching, or another retrieval method).

Below is a list of nine documents representing the initial search results. Each document contains email data structured as a dictionary with two fields - Title and Content. This semi-structured format allows the Rerank endpoint to effectively process and reorder the results based on relevance.
```python PYTHON
documents = [
    {
        "Title": "Incorrect Password",
        "Content": "Hello, I have been trying to access my account for the past hour and it keeps saying my password is incorrect. Can you please help me?",
    },
    {
        "Title": "Confirmation Email Missed",
        "Content": "Hi, I recently purchased a product from your website but I never received a confirmation email. Can you please look into this for me?",
    },
    {
        "Title": "Questions about Return Policy",
        "Content": "Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
    {
        "Title": "Customer Support is Busy",
        "Content": "Good morning, I have been trying to reach your customer support team for the past week but I keep getting a busy signal. Can you please help me?",
    },
    {
        "Title": "Received Wrong Item",
        "Content": "Hi, I have a question about my recent order. I received the wrong item and I need to return it.",
    },
    {
        "Title": "Customer Service is Unavailable",
        "Content": "Hello, I have been trying to reach your customer support team for the past hour but I keep getting a busy signal. Can you please help me?",
    },
    {
        "Title": "Return Policy for Defective Product",
        "Content": "Hi, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
    {
        "Title": "Wrong Item Received",
        "Content": "Good morning, I have a question about my recent order. I received the wrong item and I need to return it.",
    },
    {
        "Title": "Return Defective Product",
        "Content": "Hello, I have a question about the return policy for this product. I purchased it a few weeks ago and it is defective.",
    },
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
