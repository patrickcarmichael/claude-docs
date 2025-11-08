---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Image Generation

```python
  from openai import OpenAI
  import os

  client = OpenAI(
      api_key=os.environ.get("TOGETHER_API_KEY"),
      base_url="https://api.together.xyz/v1",
  )

  prompt = """
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  """

  result = client.images.generate(
      model="black-forest-labs/FLUX.1-dev", prompt=prompt
  )

  print(result.data[0].url)
```
```typescript
  import OpenAI from 'openai';

  const client = new OpenAI({
    apiKey: process.env.TOGETHER_API_KEY,
    baseURL: 'https://api.together.xyz/v1',
  });

  const prompt = `
  A children's book drawing of a veterinarian using a stethoscope to 
  listen to the heartbeat of a baby otter.
  `;

  async function main() {
    const response = await client.images.create({
      model: "black-forest-labs/FLUX.1-dev",
      prompt: prompt,
    });

    console.log(response.data[0].url);
  }

  main();
```

Output:

<div style={{textAlign: 'center'}}>
  <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=840c30380735f6bad166e6fda2c0375b" style={{width: '300px'}} data-og-width="1024" width="1024" data-og-height="768" height="768" data-path="images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=12e0c9ecdac254c9a57ef97fe5136ad1 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95e37cf0394bbb531d4ed1123e2df599 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e3fcdaaa3da32ab990a7af7fa98228a0 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=23629c234356a16d96096fabb9a5f89f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d11281b1809e98b6c28e64139c550c 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/5b659e982c3eafbe43e93de7bbca7f90c10cd70f32fd0a3fb72ad01ba50b7489-3312a74fd566b22223f2769240efab92713e8031dbbbe044d37e8b29bc757132.jpg?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c1cf869e56065ef72ed5d1fd432a9c37 2500w" />
</div>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
