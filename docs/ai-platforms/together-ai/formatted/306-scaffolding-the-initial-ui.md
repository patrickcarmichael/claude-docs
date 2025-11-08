---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Scaffolding the initial UI

The core interaction of LlamaCoder is a text field where the user can enter a prompt for an app they’d like to build. So to start, we need that text field:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f04cf018c8b1314eedcbd166ba252a78" alt="" data-og-width="2000" width="2000" data-og-height="383" height="383" data-path="images/guides/16.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=26f25c6234027a94051904f4a76a864b 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=65dbb32b01f68aec98515d5b33d112f1 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=83162a8f5385e1e608bdc5f0c1803e20 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6b435353883cb0bd7772e576422b10fd 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=88c163011541a34e75fd2e4b56bdcd5f 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/16.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b477727dd46b647ebe3793d782b1ed58 2500w" /></Frame>

We’ll render a text input inside of a form, and use some new React state to control the input’s value:
```jsx
function Page() {
  let [prompt, setPrompt] = useState('');

  return (
    <form>
      <input
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder='Build me a calculator app...'
        required
      />

      <button type='submit'>
        <ArrowLongRightIcon />
      </button>
    </form>
  );
}
```

Next, let’s wire up a submit handler to the form. We’ll call it `createApp`, since it’s going to take the user’s prompt and generate the corresponding app code:
```jsx
function Page() {
  let [prompt, setPrompt] = useState('');

  function createApp(e) {
    e.preventDefault();

    // TODO:
    // 1. Generate the code
    // 2. Render the app
  }

  return <form onSubmit={createApp}>{/* ... */}</form>;
}
```

To generate the code, we’ll have our React app query a new API endpoint. Let’s put it at `/api/generateCode` , and we’ll make it a POST endpoint so we can send along the `prompt` in the request body:
```jsx
async function createApp(e) {
  e.preventDefault();

  // TODO:
  // 1. Generate the code
  await fetch('/api/generateCode', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt }),
  });

  // 2. Render the app
}
```

Looks good – let’s go implement it!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
