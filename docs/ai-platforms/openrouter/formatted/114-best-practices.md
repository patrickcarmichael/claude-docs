---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Best Practices

### File Size Considerations

Video files can be large, which affects both upload time and processing costs:

* **Compress videos** when possible to reduce file size without significant quality loss
* **Trim videos** to include only relevant segments
* **Consider resolution**: Lower resolutions (e.g., 720p vs 4K) reduce file size while maintaining usability for most analysis tasks
* **Frame rate**: Lower frame rates can reduce file size for videos where high temporal resolution isn't critical

### Optimal Video Length

Different models may have different limits on video duration:

* Check model-specific documentation for maximum video length
* For long videos, consider splitting into shorter segments
* Focus on key moments rather than sending entire long-form content

### Quality vs. Size Trade-offs

Balance video quality with practical considerations:

* **High quality** (1080p+, high bitrate): Best for detailed visual analysis, object detection, text recognition
* **Medium quality** (720p, moderate bitrate): Suitable for most general analysis tasks
* **Lower quality** (480p, lower bitrate): Acceptable for basic scene understanding and action recognition

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
