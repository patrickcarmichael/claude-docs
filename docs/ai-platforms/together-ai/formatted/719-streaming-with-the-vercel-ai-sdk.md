---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming with the Vercel AI SDK

To stream from Together AI models using the Vercel AI SDK, simply use `streamText` as seen below.
```js
import { streamText } from "ai";
import { createTogetherAI } from '@ai-sdk/togetherai';

const together = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

async function main() {
  const result = await streamText({
    model: together("moonshotai/Kimi-K2-Instruct-0905"),
    prompt: "Invent a new holiday and describe its traditions.",
  });

  for await (const textPart of result.textStream) {
    process.stdout.write(textPart);
  }
}

main();
```

### Output

```
Introducing "Luminaria Day" - a joyous holiday celebrated on the spring equinox, marking the return of warmth and light to the world. This festive occasion is a time for family, friends, and community to come together, share stories, and bask in the radiance of the season.

**Date:** Luminaria Day is observed on the spring equinox, typically around March 20th or 21st.

**Traditions:**

1. **The Lighting of the Lanterns:** As the sun rises on Luminaria Day, people gather in their neighborhoods, parks, and public spaces to light lanterns made of paper, wood, or other sustainable materials. These lanterns are adorned with intricate designs, symbols, and messages of hope and renewal.
2. **The Storytelling Circle:** Families and friends gather around a central fire or candlelight to share stories of resilience, courage, and triumph. These tales are passed down through generations, serving as a reminder of the power of human connection and the importance of learning from the past.
3. **The Luminaria Procession:** As the sun sets, communities come together for a vibrant procession, carrying their lanterns and sharing music, dance, and laughter. The procession winds its way through the streets, symbolizing the return of light and life to the world.
4. **The Feast of Renewal:** After the procession, people gather for a festive meal, featuring dishes made with seasonal ingredients and traditional recipes. The feast is a time for gratitude, reflection, and celebration of the cycle of life.
5. **The Gift of Kindness:** On Luminaria Day, people are encouraged to perform acts of kindness and generosity for others. This can take the form of volunteering, donating to charity, or simply offering a helping hand to a neighbor in need.

**Symbolism:**

* The lanterns represent the light of hope and guidance, illuminating the path forward.
* The storytelling circle symbolizes the power of shared experiences and the importance of learning from one another.
* The procession represents the return of life and energy to the world, as the seasons shift from winter to spring.
* The feast of renewal celebrates the cycle of life, death, and rebirth.
* The gift of kindness embodies the spirit of generosity and compassion that defines Luminaria Day.

**Activities:**

* Create your own lanterns using recycled materials and decorate them with symbols, messages, or stories.
* Share your own stories of resilience and triumph with family and friends.
* Participate in the Luminaria Procession and enjoy the music, dance, and laughter.
* Prepare traditional dishes for the Feast of Renewal and share them with loved ones.
* Perform acts of kindness and generosity for others, spreading joy and positivity throughout your community.

Luminaria Day is a time to come together, celebrate the return of light and life, and honor the power of human connection.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
