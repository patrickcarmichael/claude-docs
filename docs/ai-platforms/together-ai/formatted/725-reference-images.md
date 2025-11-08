---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reference Images

Guide your video's visual style with reference images:
```py
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A cat dancing energetically",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      reference_images=[
          "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ],
  )

  print(f"Job ID: {job.id}")

  # Poll until completion

  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          break
      elif status.status == "failed":
          print("Video generation failed")
          break

      # Wait before checking again

      time.sleep(5)
```
```ts
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    const job = await together.videos.create({
      prompt: "A cat dancing energetically",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      reference_images: [
        "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg",
      ]
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        break;
      } else if (status.status === "failed") {
        console.log("Video generation failed");
        break;
      }

      // Wait before checking again
      await new Promise(resolve => setTimeout(resolve, 5000));
    }
  }

  main();
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
