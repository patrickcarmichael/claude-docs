---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Streaming the code for immediate UI feedback

Our app is working well –but we’re not showing our user any feedback while the LLM is generating the code. This makes our app feel broken and unresponsive, especially for more complex prompts.

To fix this, we can use Together AI’s support for streaming. With a streamed response, we can start displaying partial updates of the generated code as soon as the LLM responds with the first token.

To enable streaming, there’s two changes we need to make:

1. Update our API route to respond with a stream
2. Update our React app to read the stream

Let’s start with the API route.

To get Together to stream back a response, we need to pass the `stream: true` option into `together.chat.completions.create()` . We also need to update our response to call `res.toReadableStream()`, which turns the raw Together stream into a newline-separated ReadableStream of JSON stringified values.

Here’s what that looks like:
```jsx
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

  let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}
```

That’s it for the API route! Now, let’s update our React submit handler.

Currently, it looks like this:
```jsx
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });
  let json = await res.json();

  setGeneratedCode(json.choices[0].message.content);
}
```

Now that our response is a stream, we can’t just `res.json()` it. We need a small helper function to read the text from the actual bytes that are being streamed over from our API route.

Here’s the helper function. It uses an [AsyncGenerator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator) to yield out each chunk of the stream as it comes over the network. It also uses a TextDecoder to turn the stream’s data from the type Uint8Array (which is the default type used by streams for their chunks, since it’s more efficient and streams have broad applications) into text, which we then parse into a JSON object.

So let’s copy this function to the bottom of our page:
```jsx
async function* readStream(response) {
  let decoder = new TextDecoder();
  let reader = response.getReader();

  while (true) {
    let { done, value } = await reader.read();
    if (done) {
      break;
    }
    let text = decoder.decode(value, { stream: true });
    let parts = text.split('\\n');

    for (let part of parts) {
      if (part) {
        yield JSON.parse(part);
      }
    }
  }

  reader.releaseLock();
}
```

Now, we can update our `createApp` function to iterate over `readStream(res.body)`:
```jsx
async function createApp(e) {
  e.preventDefault();

  let res = await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  for await (let result of readStream(res.body)) {
    setGeneratedCode(
      (prev) => prev + result.choices.map((c) => c.text ?? '').join('')
    );
  }
}
```

This is the cool thing about Async Generators –we can use `for...of` to iterate over each chunk right in our submit handler!

By setting `generatedCode` to the current text concatenated with the new chunk’s text, React automatically re-renders our app as the LLM’s response streams in, and we see `<Sandpack>` updating its UI as the generated app takes shape.

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=3b1cc77e62ae3caedb66c23dd6976460" alt="" data-og-width="1720" width="1720" data-og-height="1450" height="1450" data-path="images/guides/22.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5207bb61c14cd5b68db8ff05719cfdbd 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cec467f8f423b6583cfd29a57189c747 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=396ca8897ad1246ffec27b7dd57d541b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1c42b7a7b93d279c93d40d55f99ae204 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c073ae539f1cbea0c449c43c25eea923 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/22.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=29acec1c6fbf4dfdb19725b6ee9a6cd2 2500w" /></Frame>

Pretty nifty, and now our app is feeling much more responsive!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
