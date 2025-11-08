---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to build an AI audio transcription app with Whisper

Source: https://docs.together.ai/docs/how-to-build-real-time-audio-transcription-app

Learn how to build a real-time AI audio transcription app with Whisper, Next.js, and Together AI.

In this guide, we're going to go over how we built [UseWhisper.io](https://usewhisper.io), an open source audio transcription app that converts speech to text almost instantly & can transform it into summaries. It's built using the [Whisper Large v3 API](https://www.together.ai/models/openai-whisper-large-v3) on Together AI and supports both live recording and file uploads.

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=07a613b09568c0726911221011dbf694" alt="usewhisper.io" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/guides/whisper/cover.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=435f9e2add5d9864345b457d2031b96d 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=98c58ab6d675cb5a4157f3fb718fb391 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=580d414399cbf99b0c389e7586e001b5 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=925e8c16fce481e7d876a609b538a52a 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1b8d6614de2665aceff547559b9c7e5c 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=d3a58a13e57e1785423af5a19fd5e5eb 2500w" />

In this post, you'll learn how to build the core parts of UseWhisper.io. The app is open-source and built with Next.js, tRPC for type safety, and Together AI's API, but the concepts can be applied to any language or framework.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
