---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Code example: Optimal concurrent requests (Python)

Here's how to implement optimal concurrent requests using `asyncio` and the `LLM` class:
```python main.py theme={null}
import asyncio
from fireworks import LLM

async def make_concurrent_requests(
    messages: list[str],
    max_workers: int = 1000,
    max_connections: int = 1000, # this is the default value in the SDK

):
    """Make concurrent requests with optimized connection pooling"""
    
    llm = LLM(
        model="your-model-name",
        deployment_type="on-demand", 
        id="your-deployment-id",
        max_connections=max_connections
    )
    
    # Apply deployment configuration to Fireworks

    llm.apply()
    
    # Semaphore to limit concurrent requests

    semaphore = asyncio.Semaphore(max_workers)
    
    async def single_request(message: str):
        """Make a single request with semaphore control"""
        async with semaphore:
            response = await llm.chat.completions.acreate(
                messages=[{"role": "user", "content": message}],
                max_tokens=100
            )
            return response.choices[0].message.content
    
    # Create all request tasks

    tasks = [
        single_request(message) 
        for message in messages
    ]
    
    # Execute all requests concurrently

    results = await asyncio.gather(*tasks)
    return results

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
