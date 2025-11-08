---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Displaying the chatbot’s response in the UI

Back in our page, we’ll use the `ChatCompletionStream` helper from Together’s SDK to update our `messages` state as our API endpoint streams in text:
```jsx
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });

    ChatCompletionStream.fromReadableStream(chatRes.body).on(
      'content',
      (delta) => {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];

          if (lastMessage.role === 'assistant') {
            return [
              ...prev.slice(0, -1),
              { ...lastMessage, content: lastMessage.content + delta },
            ];
          } else {
            return [...prev, { role: 'assistant', content: delta }];
          }
        });
      }
    );
  }

  // ...
}
```

Note that because we’re storing the entire history of messages as an array, we check the last message’s `role` to determine whether to append the streamed text to it, or push a new object with the assistant’s initial text.

Now that our `messages` React state is ready, let’s update our UI to display it:
```jsx
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');
  const [sources, setSources] = useState([]);
  const [messages, setMessages] = useState([]);

  async function handleSubmit(e) {
    // ...
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

      {/* Display the messages */}
      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}
    </>
  );
}
```

If we try it out, we’ll see the sources come in, and once our `chat` endpoint responds with the first chunk, we’ll see the answer text start streaming into our UI!

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6524178a639503751c16dc713afb81a4" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/33.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=497d7dcf0114276fee30e72bad9272be 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b78e411455f4ccec95e2c5b2cf5362a8 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a6e08df04098a6feb2187b9a05969bed 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8b07f9b488780f752c4020c30f858a01 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ae918a63013689621da6d989ce6108ab 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/33.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=ac70bc939926bb197f99e86effe6b7bc 2500w" />
</Frame>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
