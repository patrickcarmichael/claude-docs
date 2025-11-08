---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fetching the content from each source

Let’s make a request to a second endpoint called `/api/getParsedSources`, passing along the sources in the request body:
```jsx
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the sources to a new endpoint
    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The second fetch() will 404 for now
  }

  // ...
}
```

We’ll create a file at`app/api/getParsedSources/route.js` for our new route:
```jsx
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.sources` has the websites from Bing
}
```

Now we’re ready to actually get the text from each one of our sources.

Let’s write a new `getTextFromURL` function and outline our general approach:
```jsx
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
}
```

Let’s implement this new function. We’ll start by installing the `jsdom` and `@mozilla/readability` libraries:
```jsx
npm i jsdom @mozilla/readability
```

Next, let’s implement the steps:
```jsx
async function getTextFromURL(url) {
  // 1. Use fetch() to get the HTML content
  const response = await fetch(url);
  const html = await response.text();

  // 2. Use the `jsdom` library to parse the HTML into a JavaScript object
  const virtualConsole = new jsdom.VirtualConsole();
  const dom = new JSDOM(html, { virtualConsole });

  // 3. Use `@mozilla/readability` to clean the document and
  //    return only the main text of the page
  const { textContent } = new Readability(doc).parse();
}
```

Looks good - let’s try it out!

We’ll run the first source through `getTextFromURL`:
```jsx
// app/api/getParsedSources/route.js
export async function POST(req) {
  let json = await req.json();

  let textContent = await getTextFromURL(json.sources[0].url);

  console.log(textContent);
}
```

If we submit our form , we’ll see the text show up in our server terminal from the first page!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aafd49af898764f983d6129e351e7f15" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/31.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ce319fc5d406d057766a14aec9e0a14c 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5df9013d584a2dda307539eaf3216341 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e64db884d0be3e1f4c34761fa73cba23 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=244ae2de9e5dfc66e052053f924139fe 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=97c39be74aae21fc58462bbcc4753044 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/31.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=472fc906cd1baf86f7e0c01c2c861887 2500w" />
</Frame>

Let’s update the code toget the text from all the sources.

Since each source is independent, we can use `Promise.all` to kick off our functions in parallel:
```jsx
// app/api/getAnswer/route.js
export async function POST(req) {
  let json = await req.json();

  let results = await Promise.all(
    json.sources.map((source) => getTextFromURL(source.url))
  );

  console.log(results);
}
```

If we try again, we’ll now see an array of each web page’s text logged to the console:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=5e5eb89322d2bde318831fc0891c9ea4" alt="" data-og-width="1682" width="1682" data-og-height="1744" height="1744" data-path="images/guides/32.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c722f26797085578aa77bb485c901b42 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7ba84e41a110fd3818dcbbf2734d3ea9 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ee6a3d7776bb5b00e806a8858c69468b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8ecbee1cf6e8ea751536fc79a6157cad 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=222c76e259759692a00cf3128e2226cd 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/32.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=aa4a811bb146c0d13168c3988c90eaca 2500w" />
</Frame>

We’re ready to use the parsed sources in our React frontend!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
