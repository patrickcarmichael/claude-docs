---
title: "Anthropic Documentation"
description: "Formatted documentation for Anthropic"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best practices

### For tool-based search (Method 1)

* **Dynamic content**: Use for real-time searches and dynamic RAG applications
* **Error handling**: Return appropriate messages when searches fail
* **Result limits**: Return only the most relevant results to avoid context overflow

### For top-level search (Method 2)

* **Pre-fetched content**: Use when you already have search results
* **Batch processing**: Ideal for processing multiple search results at once
* **Testing**: Great for testing citation behavior with known content

### General best practices

1. **Structure results effectively**
   * Use clear, permanent source URLs
   * Provide descriptive titles
   * Break long content into logical text blocks

2. **Maintain consistency**
   * Use consistent source formats across your application
   * Ensure titles accurately reflect content
   * Keep formatting consistent

3. **Handle errors gracefully**
```python
   def search_with_fallback(query):
       try:
           results = perform_search(query)
           if not results:
               return {"type": "text", "text": "No results found."}
           return format_as_search_results(results)
       except Exception as e:
           return {"type": "text", "text": f"Search error: {str(e)}"}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
