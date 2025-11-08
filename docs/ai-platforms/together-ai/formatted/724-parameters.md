---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Parameters

| Parameter         | Type    | Description                                                                                                                                                              | Default      |
| ----------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| `prompt`          | string  | Text description of the video to generate                                                                                                                                | **Required** |
| `model`           | string  | Model identifier                                                                                                                                                         | **Required** |
| `width`           | integer | Video width in pixels                                                                                                                                                    | 1366         |
| `height`          | integer | Video height in pixels                                                                                                                                                   | 768          |
| `seconds`         | integer | Length of video (1-10)                                                                                                                                                   | 6            |
| `fps`             | integer | Frames per second                                                                                                                                                        | 15-60        |
| `steps`           | integer | Diffusion steps (higher = better quality, slower)                                                                                                                        | 10-50        |
| `guidance_scale`  | float   | How closely to follow prompt                                                                                                                                             | 6.0-10.0     |
| `seed`            | integer | Random seed for reproducibility                                                                                                                                          | any          |
| `output_format`   | string  | Video format (MP4, GIF)                                                                                                                                                  | MP4          |
| `output_quality`  | integer | Bitrate/quality (lower = higher quality)                                                                                                                                 | 20           |
| `negative_prompt` | string  | What to avoid in generation                                                                                                                                              | -            |
| `frame_images`    | Array   | Array of images to guide video generation, like keyframes.  If size 1, starting frame, if size 2, starting and ending frame, if more than 2 then frame must be specified |              |

* `prompt` is required for all models except Kling
* `width` and `height` will rely on defaults unless otherwise specified - options for dimensions vary by model

These parameters vary by model, please refer to the [models table](/docs/videos-overview#supported-model-details) for details.

Generate customized videos using the above parameters:
```py
  import time
  from together import Together

  client = Together()

  job = client.videos.create(
      prompt="A futuristic city at night with neon lights reflecting on wet streets",
      model="minimax/hailuo-02",
      width=1366,
      height=768,
      seconds=6,
      fps=30,
      steps=30,
      guidance_scale=8.0,
      output_format="MP4",
      output_quality=20,
      seed=42,
      negative_prompt="blurry, low quality, distorted",
  )

  print(f"Job ID: {job.id}")

  # Poll until completion

  while True:
      status = client.videos.retrieve(job.id)
      print(f"Status: {status.status}")

      if status.status == "completed":
          print(f"Video URL: {status.outputs.video_url}")
          print(f"Cost: ${status.outputs.cost}")
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
      prompt: "A futuristic city at night with neon lights reflecting on wet streets",
      model: "minimax/hailuo-02",
      width: 1366,
      height: 768,
      seconds: 6,
      fps: 30,
      steps: 30,
      guidance_scale: 8.0,
      output_format: "MP4",
      output_quality: 20,
      seed: 42,
      negative_prompt: "blurry, low quality, distorted"
    });

    console.log(`Job ID: ${job.id}`);

    // Poll until completion
    while (true) {
      const status = await together.videos.retrieve(job.id);
      console.log(`Status: ${status.status}`);

      if (status.status === "completed") {
        console.log(`Video URL: ${status.outputs.video_url}`);
        console.log(`Cost: $${status.outputs.cost}`);
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
