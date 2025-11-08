---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting web sources with Exa

To create our API route, we’ll make a new`app/api/getSources/route.js`file:
```jsx
// app/api/getSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.question` has the user's question
}
```

We’re ready to send our question to Exa API to return back nine sources from the web.

The [Exa API SDK](https://exa.ai/) lets you make a fetch request to get back search results including content, so we’ll use it to build up our list of sources:
```jsx
// app/api/getSources/route.js
import Exa from "exa-js";
import { NextResponse } from "next/server";

const exaClient = new Exa(process.env.EXA_API_KEY);

export async function POST(req) {
  const json = await req.json();

    const response = await exaClient.searchAndContents(json.question, {
      numResults: 9,
      type: "auto",
    });

  return NextResponse.json(
    response.results.map((result) => ({
      title: result.title || undefined,
      url: result.url,
      content: result.text
    })),
  );
}
```

In order to make a request to Exa API, you’ll need to get an [API key from Exa](https://exa.ai/). Once you have it, set it in `.env.local`:
```jsx
// .env.local
EXA_API_KEY=xxxxxxxxxxxx
```

and our API handler should work.

Let’s try it out from our React app! We’ll log the sources in our event handler:
```jsx
// app/page.tsx
function Page() {
  let [question, setQuestion] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    let sources = await response.json();

    // log the response from our new endpoint
    console.log(sources);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything"
      />
    </form>
  );
}
```

and if we try submitting a question, we’ll see an array of pages logged in the console!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9f509e066e9b0850ae3b9e8c50e9c8b2" alt="" data-og-width="2548" width="2548" data-og-height="1818" height="1818" data-path="images/guides/7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=d5f09992ac5c172193d08cc6a124984f 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5af9b84ef4a479cc6dec8cf96ed79d13 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=451744827a48d6472cf46c9b3ba71465 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=34a292ad4bcd1d4002dab6a3cb1bfc5a 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=4ac75159cd6221c32e55c9be29d8ee49 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/7.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=291ecdc1aaad00b7acc9be5dd99e2c97 2500w" />
</Frame>

Let’s create some new React state to store the responses and display them in our UI:
```jsx
function Page() {
  let [question, setQuestion] = useState("");
  let [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    let sources = await response.json();

    // Update the sources with our API response
    setSources(sources);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask anything"
        />
      </form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.title}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
}
```

If we try it out, our app is working great so far! We’re taking the user’s question, fetching nine relevant web sources from Exa, and displaying them in our UI.

Next, let’s work on summarizing the sources.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
