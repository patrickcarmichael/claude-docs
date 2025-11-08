---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate a story based on the top 10 most similar movies

query = "What are 'skip-level' meetings?"

response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful chatbot."},
        {
            "role": "user",
            "content": f"Answer the question: {query}. Here is relevant information: {retreived_chunks}",
        },
    ],
)
```

Which produces the following response:
```
'"Skip-level" meetings refer to a management practice where a CEO or high-level executive engages directly with employees who are not their direct reports, bypassing the traditional hierarchical structure of the organization. This approach is characteristic of "founder mode," where the CEO seeks to have a more direct connection with the company beyond their immediate team. In contrast to the traditional "manager mode," where decisions are made through a hierarchical system, skip-level meetings allow for more open communication and collaboration between the CEO and various levels of employees. This approach is often used by founders who want to stay connected to the company\'s operations and culture, and to foster a more flat and collaborative organizational structure.'
```

Above we implemented Contextual Retrieval as discussed in Anthropic's blog using fully open source models!

If you want to learn more about how to best use open models refer to our [docs here](/docs) !

***


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
