---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building the input prompt

TurboSeek’s core interaction is a text field where the user can enter a question:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5d3b06c25e24a4ed4f07a2c8ce3075f3" alt="" data-og-width="1928" width="1928" data-og-height="626" height="626" data-path="images/guides/5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=23934eb6e9483c7874bc5b5ef449f3b5 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=0e6214d9d62bb06bcaf8f90cc558c90f 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=ab028b219014620d5056400beed90d53 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=79d537237bdcf9eb9c89010d279bdfe8 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=fc6f3a0571227f15a302e44e59963144 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/5.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=7d565dbb6d003bbe62206d1e3db9019e 2500w" />
</Frame>

In our page, we’ll render an `<input>` and control it using some new React state:
```jsx
// app/page.tsx
function Page() {
  let [question, setQuestion] = useState('');

  return (
    <form>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask anything"
      />
    </form>
  );
}
```

When the user submits our form, we need to do two things:

1. Use the Exa API to fetch sources from the web, and
2. Pass the text from the sources to an LLM to summarize and generate an answer

Let’s start by fetching the sources. We’ll wire up a submit handler to our form that makes a POST request to a new endpoint, `/getSources` :
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

    // This fetch() will 404 for now
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

If we submit the form, we see our React app makes a request to `/getSources` :

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=5cf145f32811a6031de82c9f0e211e18" alt="" data-og-width="2048" width="2048" data-og-height="947" height="947" data-path="images/guides/6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=280&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=57c2f19cce2af500549b776f40611c3a 280w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=560&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=161562aa89174082131db94260d7d614 560w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=840&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=9c1adff8ef27eb1bf610ba270601a708 840w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=1100&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=c3ff90947b3ddb90323ba4a6eaa4f34a 1100w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=1650&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=b26b2d56ca9a40923483a563e2291d5d 1650w, https://mintcdn.com/togetherai-52386018/nzLwcAOIrJYyQhDB/images/guides/6.png?w=2500&fit=max&auto=format&n=nzLwcAOIrJYyQhDB&q=85&s=63479d93cc91f7993301b6933b6481dd 2500w" />
</Frame>

Our frontend is ready! Let’s add an API route to get the sources.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
