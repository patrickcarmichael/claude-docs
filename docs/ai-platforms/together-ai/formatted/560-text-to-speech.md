---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Text-to-Speech

```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  speech_file_path = "speech.mp3"

  response = client.audio.speech.create(
      model="hexgrad/Kokoro-82M",
      input="Today is a wonderful day to build something people love!",
      voice="helpful woman",
  )

  response.stream_to_file(speech_file_path)
```
```typescript
  import OpenAI from 'openai';
  import { createWriteStream } from 'fs';
  import { pipeline } from 'stream/promises';

  const client = new OpenAI({
      apiKey: process.env.TOGETHER_API_KEY,
      baseURL: 'https://api.together.xyz/v1',
    });

  const speechFilePath = 'speech.mp3';

  async function main() {
      const response = await client.audio.speech.create({
        model: 'hexgrad/Kokoro-82M',
        input: 'Today is a wonderful day to build!',
        voice: 'helpful woman',
      });

      const buffer = Buffer.from(await response.arrayBuffer());
      await require('fs').promises.writeFile(speechFilePath, buffer);
    }

  main();
```

Output:

<iframe src="https://drive.google.com/file/d/1zpUdy_UlCeveGJP1z4ddj_Uh3uKnSovT/preview" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
