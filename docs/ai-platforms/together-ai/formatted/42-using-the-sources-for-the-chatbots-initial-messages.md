---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Using the sources for the chatbot’s initial messages

Back in our React app, we now have the text from each source in our submit handler:
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

    const parsedSourcesRes = await fetch('/api/getParsedSources', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sources }),
    });

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();
  }

  // ...
}
```

We’re ready to kick off our chatbot. We’ll use the selected grade level and the parsed sources to write a system prompt, and pass in the selected topic as the user’s first message:
```jsx
// app/page.tsx
function Page() {
  const [messages, setMessages] = useState([]);
  // ...

  async function handleSubmit(e) {
    // ...

    // The text from each source
    const parsedSources = await parsedSourcesRes.json();

    // Start our chatbot
    const systemPrompt = `
      You're an interactive personal tutor who is an expert at explaining topics. Given a topic and the information to teach, please educate the user about it at a ${grade} level.

      Here's the information to teach:

      <teaching_info>
      ${parsedSources.map(
        (result, index) =>
          `## Webpage #${index}:\\n ${result.fullContent} \\n\\n`

      )}
      </teaching_info>
    `;

    const initialMessages = [
      { role: 'system', content: systemPrompt },
      { role: 'user', content: topic },
    ];
    setMessages(initialMessages);

    // This will 404 for now
    const chatRes = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ messages: initialMessages }),
    });
  }

  // ...
}
```

We also created some new React state to store all the messages so that we can display and update the chat history as the user sends new messages.

We’re ready to implement our final API endpoint at `/chat`!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
