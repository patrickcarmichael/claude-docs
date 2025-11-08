---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generating code in an API route

To create an API route in the Next.js 14 app directory, we can make a new `route.js` file:
```jsx
// app/api/generateCode/route.js
export async function POST(req) {
  let json = await req.json();

  console.log(json.prompt);
}
```

If we submit the form, we’ll see the user’s prompt logged to the console. Now we’re ready to send it off to our LLM and ask it to generate our user’s app! We tested many open source LLMs and found that Kimi K2 was the only one that did a good job at generating small apps, so that’s what we decided to use for the app.

We’ll install Together’s node SDK:
```bash
npm i together-ai
```

and use it to kick off a chat with Kimi K2.

Here’s what it looks like:
```jsx
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let completion = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: 'You are an expert frontend React engineer.',
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
  });

  return Response.json(completion);
}
```

We call `together.chat.completions.create` to get a new response from the LLM. We’ve supplied it with a “system” message telling the LLM that it should behave as if it’s an expert React engineer. Finally, we provide it with the user’s prompt as the second message.

Since we return a JSON object, let’s update our React code to read the JSON from the response:
```jsx
async function createApp(e) {
  e.preventDefault();

  // 1. Generate the code
  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  console.log(json);

  // 2. Render the app
}
```

And now let’s give it a shot!

We’ll use something simple for our prompt like “Build me a counter”:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ff79766604b0ecdf613528a6409e0736" alt="" data-og-width="1720" width="1720" data-og-height="305" height="305" data-path="images/guides/17.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8b151e6cca96d4f2e47a3df190700cdc 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=54794fd845d0c953bec237e67a7c89ad 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5e40a57ddd5d77a77eaa3cc66586a499 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=580fa4fc21f9a0f60359540893afc9be 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=abdba72d62968901ce00699ed9c06802 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/17.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6d3218731f4f3ffdb9cf3ab9558d16be 2500w" /></Frame>

When we submit the form, our API response takes several seconds, but then sends our React app the response.

If you take a look at your logs, you should see something like this:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aecf6247f32c6431afe963569c44f898" alt="" data-og-width="1720" width="1720" data-og-height="1800" height="1800" data-path="images/guides/18.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7accc4c3d05db2e182692f3104aeb848 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5d77c5e86c4143c85f677a67d71dea18 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88d849973cffa20dfe9bf77e45d42009 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b386cc1ca484905abdd2f1bf330b469d 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=324b5f21f1df81cb8411997c326c86c6 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/18.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=492b5d936cc82ff8c589871cd7036675 2500w" /></Frame>

Not bad – Kimi K2 has generated some code that looks pretty good and matches our user’s prompt!

However, for this app, we’re only interested in the code, since we’re going to be actually running it in our user’s browser. So we need to do some prompt engineering to get Llama to only return the code in a format we expect.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
