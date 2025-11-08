---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Fetching the content from each source

Now that our React app has the sources, we can send them to a second endpoint where we’ll use Together to summarize them into our final answer.

Let’s add that second request to a new endpoint we’ll call `/api/getAnswer`, passing along the question and sources in the request body:
```jsx
// app/page.tsx
function Page() {
  // ...

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the question and sources to a new endpoint
    const answerResponse = await fetch("/api/getAnswer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, sources }),
    });

    // The second fetch() will 404 for now
  }

  // ...
}
```

If we submit a new question, we’ll see our React app make a second request to `/api/getAnswer`. Let’s create the second route!

Make a new`app/api/getAnswer/route.js`file:
```jsx
// app/api/getAnswer/route.js
export async function POST(req) {
  let json = await req.json();

  // `json.question` and `json.sources` has our data
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
