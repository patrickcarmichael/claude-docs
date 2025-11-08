---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating a video

Video generation is asynchronous. You create a job, receive a job ID, and poll for completion.
```py
  import time
  from together import Together

  client = Together()

  # Create a video generation job

  job = client.videos.create(
      prompt="A serene sunset over the ocean with gentle waves",
      model="minimax/video-01-director",
      width=1366,
      height=768,
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
    // Create a video generation job
    const job = await together.videos.create({
      prompt: "A serene sunset over the ocean with gentle waves",
      model: "minimax/video-01-director",
      width: 1366,
      height: 768,
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

Example output when the job is complete:
```json
{
  "id": "019a0068-794a-7213-90f6-cc4eb62e3da7",
  "model": "minimax/video-01-director",
  "status": "completed",
  "info": {
    "user_id": "66f0bd504fb9511df3489b9a",
    "errors": null
  },
  "inputs": {
    "fps": null,
    "guidance_scale": null,
    "height": 768,
    "metadata": {},
    "model": "minimax/video-01-director",
    "output_quality": null,
    "prompt": "A serene sunset over the ocean with gentle waves",
    "seconds": null,
    "seed": null,
    "steps": null,
    "width": 1366
  },
  "outputs": {
    "cost": 0.28,
    "video_url": "https://api.together.ai/shrt/DwlaBdSakNRFlBxN"
  },
  "created_at": "2025-10-20T06:57:18.154804Z",
  "claimed_at": "0001-01-01T00:00:00Z",
  "done_at": "2025-10-20T07:00:12.234472Z"
}
```
**Job Status Reference:**

| Status        | Description                            |
| ------------- | -------------------------------------- |
| `queued`      | Job is waiting in queue                |
| `in_progress` | Video is being generated               |
| `completed`   | Generation successful, video available |
| `failed`      | Generation failed, check `info.errors` |
| `cancelled`   | Job was cancelled                      |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
