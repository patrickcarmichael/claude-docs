---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Getting web sources with Bing

To create our API route, we’ll make a new`app/api/getSources/route.js`file:
```jsx
// app/api/getSources/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.topic` has the user's text
}
```

The [Bing API](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) lets you make a fetch request to get back search results, so we’ll use it to build up our list of sources:
```jsx
// app/api/getSources/route.js
import { NextResponse } from 'next/server';

export async function POST(req) {
  const json = await req.json();

  const params = new URLSearchParams({
    q: json.topic,
    mkt: 'en-US',
    count: '6',
    safeSearch: 'Strict',
  });

  const response = await fetch(
    `https://api.bing.microsoft.com/v7.0/search?${params}`,
    {
      method: 'GET',
      headers: {
        'Ocp-Apim-Subscription-Key': process.env['BING_API_KEY'],
      },
    }
  );
  const { webPages } = await response.json();

  return NextResponse.json(
    webPages.value.map((result) => ({
      name: result.name,
      url: result.url,
    }))
  );
}
```

In order to make a request to Bing’s API, you’ll need to [get an API key from Microsoft](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api). Once you have it, set it in `.env.local`:
```jsx
// .env.local
BING_API_KEY=xxxxxxxxxxxx
```

and our API handler should work.

Let’s try it out from our React app! We’ll log the sources in our submit handler:
```jsx
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // log the response from our new endpoint
    console.log(sources);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Teach me about..."
      />
      <select value={grade} onChange={(e) => setGrade(e.target.value)}>
        <option>Elementary School</option>
        <option>Middle School</option>
        <option>High School</option>
        <option>College</option>
        <option>Undergrad</option>
        <option>Graduate</option>
      </select>
    </form>
  );
}
```

and if we try submitting a topic, we’ll see an array of pages logged in the console!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=9f0c9b3b0f6228e07bea418c5353b3b5" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/29.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=71267f03b11f23ca5c4d6841380463c8 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=752048c898c16e84fc018bd6b2f8df43 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bf06784ebc7460e70694a0d3ffdd15a4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=36280e757e39d56f41f5f3aadb1902b6 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=74f1ee456b358140613075ad522a1705 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/29.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e7e90678cf50a7f622bedb40e84b804d 2500w" />
</Frame>

Let’s create some new React state to store the responses and display them in our UI:
```jsx
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    const sources = await response.json();

    // Update the sources with our API response
    setSources(sources);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>{/* ... */}</form>

      {/* Display the sources */}
      {sources.length > 0 && (
        <div>
          <p>Sources</p>
          <ul>
            {sources.map((source) => (
              <li key={source.url}>
                <a href={source.url}>{source.name}</a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </>
  );
}
```

If we try it out, our app is working great so far!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ce32b4be67a3087fd6e054e52b65d231" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/30.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2eb346313c648876d8ec3b728c9c9a77 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b72dba4a26148e3f28cccf1e403e6bf3 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e5e6dcce61dc11e0a27b05a00b31f8f4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=184c5642e435463d02be2001e2f27f82 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=85827f1fff733e27a87d463e2da2bbd5 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/30.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a4bfb2bca435c8251660ea11275176e9 2500w" />
</Frame>

We’re taking the user’s topic, fetching six relevant web sources from Bing, and displaying them in our UI.

Next, let’s get the text content from each website so that our AI model has some context for its first response.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
