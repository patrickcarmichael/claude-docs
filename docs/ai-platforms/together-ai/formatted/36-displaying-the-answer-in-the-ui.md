---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Displaying the answer in the UI

Back in our page, let’s create some new React state called `answer` to store the text from our LLM:
```jsx
// app/page.tsx
function Page() {
  const [answer, setAnswer] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const response = await fetch("/api/getSources", {
      method: "POST",
      body: JSON.stringify({ question }),
    });

    const sources = await response.json();
    setSources(sources);

    // Send the question and sources to a new endpoint
    const answerStream = await fetch("/api/getAnswer", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question, sources }),
    });
  }

  // ...
}
```

We can use the `ChatCompletionStream` helper from Together’s SDK to read the stream and update our `answer` state with each new chunk:
```jsx
// app/page.tsx
import { ChatCompletionStream } from "together-ai/lib/ChatCompletionStream";

function Page() {
  const [answer, setAnswer] = useState("");

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

    const runner = ChatCompletionStream.fromReadableStream(answerResponse.body);
    runner.on("content", (delta) => setAnswer((prev) => prev + delta));
  }

  // ...
}
```

Our new React state is ready!

Let’s update our UI to display it:
```jsx
function Page() {
  let [question, setQuestion] = useState("");
  let [sources, setSources] = useState([]);

  async function handleSubmit(e) {
    //
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

      {/* Display the answer */}
      {answer && <p>{answer}</p>}
    </>
  );
}
```

If we try submitting a question, we’ll see the sources come in, and once our `getAnswer` endpoint responds with the first chunk, we’ll see the answer text start streaming into our UI!

The core features of our app are working great.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
