---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Quality Control with Steps

Trade off between generation time and quality:

* **10 steps**: Quick testing, lower quality
* **20 steps**: Standard quality, good balance
* **30-40 steps**: Production quality, slower
* **>50 steps**: Diminishing returns
```py
  # Quick preview

  job_quick = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=10,
  )

  # Production quality

  job_production = client.videos.create(
      prompt="A person walking through a forest",
      model="minimax/hailuo-02",
      steps=40,
  )
```
```ts
  // Quick preview
  import Together from "together-ai";

  const together = new Together();

  const jobQuick = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 10
  });

  // Production quality
  const jobProduction = await together.videos.create({
    prompt: "A person walking through a forest",
    model: "minimax/hailuo-02",
    steps: 40
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
