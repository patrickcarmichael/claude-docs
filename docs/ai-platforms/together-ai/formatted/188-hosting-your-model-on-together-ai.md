---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Hosting your model on Together AI

If you select your model in [the models dashboard](https://api.together.xyz/models) you can click `CREATE DEDICATED ENDPOINT` to create a [dedicated endpoint](/docs/dedicated-endpoints-ui) for the fine-tuned model.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=25985393a46001b7f6caa2411fa8e4a6" alt="" data-og-width="1441" width="1441" data-og-height="610" height="610" data-path="images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=17e27d488b8d6e3fd914545e6b6d1789 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5a2ea92e185cf8c2e772224eb0582aa0 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=001d316edb86a022e617c15fe4ecf3e4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=58c1a074a925e8ffffa4f7cce8dd2020 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=98b3988e1d12c18e16ab95d7256ba6ab 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/b17fd6bd03dcfb26b91389b864cf0ce3a275a2f22db2b56a975b1ffdba3c7789-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=665ebc29b8ba34334e78f17feb47e93f 2500w" />
</Frame>

Once it's deployed, you can use the ID to query your new model using any of our APIs:
```bash
  together chat.completions \
    --model "[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17" \
    --message "user" "What are some fun things to do in New York?"
```
```python
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  stream = client.chat.completions.create(
      model="[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17",
      messages=[
          {
              "role": "user",
              "content": "What are some fun things to do in New York?",
          }
      ],
      stream=True,
  )

  for chunk in stream:
      print(chunk.choices[0].delta.content or "", end="", flush=True)
```
```typescript
  import Together from 'together-ai';

  const together = new Together({
    apiKey: process.env['TOGETHER_API_KEY'],
  });

  const stream = await together.chat.completions.create({
    model: '[email protected]/Meta-Llama-3-8B-2024-07-11-22-57-17',
    messages: [
      { role: 'user', content: 'What are some fun things to do in New York?' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
```

Hosting your fine-tuned model is charged per minute hosted. You can see the hourly pricing for fine-tuned model inference in [the pricing table](https://www.together.ai/pricing).

When you're not using the model, be sure to stop the endpoint from the [the models dashboard](https://api.together.xyz/models).

Read more about dedicated inference [here](/docs/dedicated-inference).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
