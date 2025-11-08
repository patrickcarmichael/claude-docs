---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How To Build An Interactive AI Tutor With Llama 3.1

Source: https://docs.together.ai/docs/ai-tutor

Learn we built LlamaTutor from scratch – an open source AI tutor with 90k users.

[LlamaTutor](https://llamatutor.together.ai/) is an app that creates an interactive tutoring session for a given topic using [Together AI’s](https://www.together.ai/) open-source LLMs.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dd9838164e399ad4ba65028af3ce2793" alt="" data-og-width="2560" width="2560" data-og-height="1440" height="1440" data-path="images/guides/25.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=099549217905b28be8fd6fd69fc598d6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=40bcf62887f72184a8e70f381fad6039 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9100049250fea24d344c93c4f18c5ded 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cf02317b42669234501b78e5b12c6b21 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e6fab195cda8d130488064aec01ab88e 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/25.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e687740e621890360b8734aab8121b2d 2500w" />
</Frame>

It pulls multiple sources from the web with either Bing’s API or Serper's API, then uses the text from the sources to kick off an interactive tutoring session with the user.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=83d3d4d158ada52cab0ab2471f09faa2" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/26.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a009c2960b508f473deda879547a90cf 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e34dc07d84bd8fa01885111a84795382 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=72b1010a17883f6ae04cdeb91d5e18fa 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=77332c6c745f98c9118dcd22b34e1a2f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=05a81a2cba985db4c8f03f3cdbd3cf78 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/26.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=263ad9bbf395435ccb4c3f81ec139d63 2500w" />
</Frame>

In this post, you’ll learn how to build the core parts of LlamaTutor. The app is open-source and built with Next.js and Tailwind, but Together’s API work great with any language or framework.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
