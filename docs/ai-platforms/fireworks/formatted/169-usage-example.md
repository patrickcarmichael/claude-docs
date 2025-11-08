---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Usage example

async def main():
    messages = ["Hello!"] * 1000  # 1000 requests

    
    results = await make_concurrent_requests(
        messages=messages,
    )
    
    print(f"Completed {len(results)} requests")

if __name__ == "__main__":
    asyncio.run(main())
```
This implementation:

* Uses `asyncio.Semaphore` to control concurrency to avoid overwhelming the server
* Allows configuration of the maximum number of concurrent connections to the Fireworks API


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
