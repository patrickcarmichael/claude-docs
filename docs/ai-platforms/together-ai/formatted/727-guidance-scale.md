---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Guidance Scale

Controls how closely the model follows your prompt:

* **6.0-7.0**: More creative, less literal
* **7.0-9.0**: Sweet spot for most use cases
* **9.0-10.0**: Strict adherence to prompt
* **>12.0**: Avoid - may cause artifacts
```py
  from together import Together

  client = Together()

  # Low guidance - more creative interpretation

  job_creative = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=6.0,
      seed=100,
  )

  # High guidance - closer to literal prompt

  job_literal = client.videos.create(
      prompt="an astronaut riding a horse on the moon",
      model="minimax/hailuo-02",
      guidance_scale=10.0,
      seed=100,
  )
```
```ts
  // Low guidance - more creative interpretation
  import Together from "together-ai";

  const together = new Together();

  const jobCreative = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 6.0,
    seed: 100
  });

  // High guidance - closer to literal prompt
  const jobLiteral = await together.videos.create({
    prompt: "an astronaut riding a horse on the moon",
    model: "minimax/hailuo-02",
    guidance_scale: 10.0,
    seed: 100
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
