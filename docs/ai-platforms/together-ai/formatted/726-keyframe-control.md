---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Keyframe Control

Control specific frames in your video for precise transitions.

**Single Keyframe:** Set a single(for the example below this is the first frame) frame to a specific image.

Depending on the model you can also specify to set multiple keyframes please refer to the [models table](/docs/videos-overview#supported-model-details) for details.
```py
  import base64
  import requests
  import time
  from together import Together

  client = Together()

  # Download image and encode to base64

  image_url = (
      "https://cdn.pixabay.com/photo/2020/05/20/08/27/cat-5195431_1280.jpg"
  )
  response = requests.get(image_url)
  base64_image = base64.b64encode(response.content).decode("utf-8")

  # Single keyframe at start

  job = client.videos.create(
      prompt="Smooth transition from day to night",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      fps=24,
      frame_images=[{"input_image": base64_image, "frame": 0}],  # Starting frame

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
  import * as fs from 'fs';
  import Together from "together-ai";

  const together = new Together();

  async function main() {
    // Load and encode your image
    const imageBuffer = fs.readFileSync('keyframe.jpg');
    const base64Image = imageBuffer.toString('base64');

    // Single keyframe at start
    const job = await together.videos.create({
      prompt: "Smooth transition from day to night",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      fps: 24,
      frame_images: [
        {
          input_image: base64Image,
          frame: 0  // Starting frame
        }
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

**💡 Tip:** Frame number = seconds × fps

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
