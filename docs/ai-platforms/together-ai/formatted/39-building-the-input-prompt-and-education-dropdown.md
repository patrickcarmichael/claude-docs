---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building the input prompt and education dropdown

LlamaTutor’s core interaction is a text field where the user can enter a topic, and a dropdown that lets the user choose which education level the material should be taught at:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e733787a865a226113fd4ee32bbc2564" alt="" data-og-width="1702" width="1702" data-og-height="594" height="594" data-path="images/guides/27.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=68c2c80515b7366f4e8928c4f3a12378 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6f67f53a4bb34ef494b17799e6916850 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b6b62437b9c4c20802cb3bbc9be7b9a4 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=95d5812431e5f8619a9681860960ffc3 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f4d0fe1a1aa6bdd5d7bb18aaac552f1d 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/27.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=0595d07bd5a1f93a153780e5a0250428 2500w" />
</Frame>

In the main page component, we’ll render an `<input>` and `<select>`, and control both using some new React state:
```jsx
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  return (
    <form>
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

When the user submits our form, our submit handler ultimately needs to do three things:

1. Use the Bing API to fetch six different websites related to the topic
2. Parse the text from each website
3. Pass all the parsed text, as well as the education level, to Together AI to kick off the tutoring session

Let’s start by fetching the websites with Bing. We’ll wire up a submit handler to our form that makes a POST request to a new `/getSources` endpoint:
```jsx
// app/page.tsx
function Page() {
  const [topic, setTopic] = useState('');
  const [grade, setGrade] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();

    let response = await fetch('/api/getSources', {
      method: 'POST',
      body: JSON.stringify({ topic }),
    });

    let sources = await response.json();

    // This fetch() will 404 for now
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

If we submit the form, we see our React app makes a request to `/getSources` :

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=92e5573388f6bd84d025eb6c79eaf062" alt="" data-og-width="2048" width="2048" data-og-height="1152" height="1152" data-path="images/guides/28.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=389685cd22e9ea862c9616ef008192e4 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=67d635e8aad971b7e176a3421ee180a7 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=98d8c6499377bc73ee90a4b7a599efb7 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=e7b0f22ae781414574d25cf7387d5518 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=252aabc3fd77d01dd242684d383c0be6 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/28.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8498d782d2dde8ef09b7ee987bcf1066 2500w" />
</Frame>

Let’s go implement this API route.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
