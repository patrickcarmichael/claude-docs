---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supported Model Details

See our supported video models and relevant parameters below.

| **Organization** | **Name**             | **Model API String**          | **Duration** | **Dimensions**                                                                                      | **FPS** | **Keyframes** | **Prompt**  |
| :--------------- | :------------------- | :---------------------------- | :----------- | :-------------------------------------------------------------------------------------------------- | :------ | :------------ | :---------- |
| **MiniMax**      | MiniMax 01 Director  | `minimax/video-01-director`   | 5s           | 1366×768                                                                                            | 25      | First         | 2-3000 char |
| **MiniMax**      | MiniMax Hailuo 02    | `minimax/hailuo-02`           | 10s          | 1366×768, 1920×1080                                                                                 | 25      | First         | 2-3000 char |
| **Google**       | Veo 2.0              | `google/veo-2.0`              | 5s           | 1280×720, 720×1280                                                                                  | 24      | First, Last   | 2-3000 char |
| **Google**       | Veo 3.0              | `google/veo-3.0`              | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 + Audio      | `google/veo-3.0-audio`        | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast         | `google/veo-3.0-fast`         | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **Google**       | Veo 3.0 Fast + Audio | `google/veo-3.0-fast-audio`   | 8s           | 1280×720, 720×1280, 1920×1080, 1080×1920                                                            | 24      | First         | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Lite    | `ByteDance/Seedance-1.0-lite` | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **ByteDance**    | Seedance 1.0 Pro     | `ByteDance/Seedance-1.0-pro`  | 5s           | 864×480, 736×544, 640×640, 960×416, 416×960, 1248×704, 1120×832, 960×960, 1504×640, 640×1504        | 24      | First, Last   | 2-3000 char |
| **PixVerse**     | PixVerse v5          | `pixverse/pixverse-v5`        | 5s           | 640×360, 480×360, 360×360, 270×360, 360×640, 960×540, 720×540, 540×540, 405×540, 540×960, 1280×720, |         |               |             |
|                  |                      |                               |              | 960×720, 720×720, 540×720, 720×1280, 1920×1080, 1440×1080, 1080×1080, 810×1080, 1080×1920           | 16, 24  | First, Last   | 2-2048 char |
| **Kuaishou**     | Kling 2.1 Master     | `kwaivgI/kling-2.1-master`    | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 2.1 Standard   | `kwaivgI/kling-2.1-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Kuaishou**     | Kling 2.1 Pro        | `kwaivgI/kling-2.1-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | ❌           |
| **Kuaishou**     | Kling 2.0 Master     | `kwaivgI/kling-2.0-master`    | 5s           | 1280×720, 720×720, 720×1280                                                                         | 24      | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Standard   | `kwaivgI/kling-1.6-standard`  | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 30, 24  | First         | 2-2500 char |
| **Kuaishou**     | Kling 1.6 Pro        | `kwaivgI/kling-1.6-pro`       | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First         | ❌           |
| **Wan-AI**       | Wan 2.2 I2V          | `Wan-AI/Wan2.2-I2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Wan-AI**       | Wan 2.2 T2V          | `Wan-AI/Wan2.2-T2V-A14B`      | -            | -                                                                                                   | -       | -             | -           |
| **Vidu**         | Vidu 2.0             | `vidu/vidu-2.0`               | 8s           | 1920×1080, 1080×1080, 1080×1920, 1280×720, 720×720, 720×1280, 640×360, 360×360, 360×640             | 24      | First, Last   | 2-3000 char |
| **Vidu**         | Vidu Q1              | `vidu/vidu-q1`                | 5s           | 1920×1080, 1080×1080, 1080×1920                                                                     | 24      | First, Last   | 2-3000 char |
| **OpenAI**       | Sora 2               | `openai/sora-2`               | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |
| **OpenAI**       | Sora 2 Pro           | `openai/sora-2-pro`           | 8s           | 1280×720, 720×1280                                                                                  | -       | First         | 1-4000 char |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
