---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Safety Checker

We have a built in safety checker that detects NSFW words but you can disable it by passing in `disable_safety_checker=True`. This works for every model except Flux Schnell Free and Flux Pro. If the safety checker is triggered and not disabled, it will return a `422 Unprocessable Entity`.
```py
  from together import Together

  client = Together()

  response = client.images.generate(
      prompt="a flying cat",
      model="black-forest-labs/FLUX.1-schnell",
      steps=4,
      disable_safety_checker=True,
  )

  print(response.data[0].url)
```
```typescript
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const response = await together.images.create({
      prompt: "a flying cat",
      model: "black-forest-labs/FLUX.1-schnell",
      steps: 4,
      disable_safety_checker: true,
    });

    console.log(response.data[0].url);
  }

  main();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
