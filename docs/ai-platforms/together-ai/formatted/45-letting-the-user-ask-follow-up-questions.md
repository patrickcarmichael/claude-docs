---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Letting the user ask follow-up questions

To let the user ask our tutor follow-up questions, let’s make a new form that only shows up once we have some messages in our React state:
```jsx
// app/page.tsx
function Page() {
  // ...
  const [newMessageText, setNewMessageText] = useState('');

  return (
    <>
      {/* Form for initial messages */}
      {messages.length === 0 && (
        <form onSubmit={handleSubmit}>{/* ... */}</form>
      )}

      {sources.length > 0 && <>{/* ... */}</>}

      {messages.map((message, i) => (
        <p key={i}>{message.content}</p>
      ))}

      {/* Form for follow-up messages */}
      {messages.length > 0 && (
        <form>
          <input
            value={newMessageText}
            onChange={(e) => setNewMessageText(e.target.value)}
            type="text"
          />
        </form>
      )}
    </>
  );
}
```

We’ll make a new submit handler called `handleMessage` that will look a lot like the end of our first `handleSubmit` function:
```jsx
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleMessage(e) {
    e.preventDefault();

    const newMessages = [
      ...messages,
      {
        role: 'user',
        content: newMessageText,
      },
    ];

    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: newMessages }),
    });
    setMessages(newMessages);

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

Because we have all the messages in React state, we can just create a new object for the user’s latest message, send it over to our existing `chat` endpoint, and reuse the same logic to update our app’s state as the latest response streams in.

The core features of our app are working great!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
