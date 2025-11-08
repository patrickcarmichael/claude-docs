---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Running the generated code in the browser

Now that we’ve got a pure code response from our LLM, how can we actually execute it in the browser for our user?

This is where the phenomenal [Sandpack](https://sandpack.codesandbox.io/) library comes in.

Once we install it:
```bash
npm i @codesandbox/sandpack-react
```

we now can use the `<Sandpack>` component to render and execute any code we want!

Let’s give it a shot with some hard-coded sample code:
```jsx
<Sandpack
  template='react-ts'
  files={{
    'App.tsx': `export default function App() { return <p>Hello, world!</p> }`,
  }}
/>
```

If we save this and look in the browser, we’ll see that it works!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c6a9fec2cfc230edbb74d74604b97a22" alt="" data-og-width="1720" width="1720" data-og-height="1180" height="1180" data-path="images/guides/20.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bc0393627d946b795ac5ad6f0ef44d46 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=8c1db2a93b3625eba3c527c2a070df9c 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1f0cb64032a4a1c6a9db54ae0313fdaf 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=bac010968d019e4eb0d0c2ef5207a12f 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d2e26c93f30af40354488158f5c1348a 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/20.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=19fcf021a04807fde1414575958ed1ed 2500w" /></Frame>

All that’s left is to swap out our sample code with the code from our API route instead.

Let’s start by storing the LLM’s response in some new React state called `generatedCode`:
```jsx
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    e.preventDefault();

    let res = await fetch('/api/generateCode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt }),
    });
    let json = await res.json();

    setGeneratedCode(json.choices[0].message.content);
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>
    </div>
  );
}
```

Now, if `generatedCode` is not empty, we can render `<Sandpack>` and pass it in:
```jsx
function Page() {
  let [prompt, setPrompt] = useState('');
  let [generatedCode, setGeneratedCode] = useState('');

  async function createApp(e) {
    // ...
  }

  return (
    <div>
      <form onSubmit={createApp}>{/* ... */}</form>

      {generatedCode && (
        <Sandpack
          template='react-ts'
          files={{
            'App.tsx': generatedCode,
          }}
        />
      )}
    </div>
  );
}
```

Let’s give it a shot! We’ll try “Build me a calculator app” as the prompt, and submit the form.

Once our API endpoint responds, `<Sandpack>` renders our generated app!

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4e47962545fab91b857856e5c92c45db" alt="" data-og-width="1720" width="1720" data-og-height="1085" height="1085" data-path="images/guides/21.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4c398c3d3a4b3fc0d2a39843aa6763d2 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c37d3896bc9375074770efb19dfbc1bb 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=dceeab1b4725d90850b43c4ca9f5446b 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d71e5afd3726c523532b2dcd4ca5d546 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=c04f42f9ddc29f6d3c3cf123ded012a4 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/21.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=347a422de6a94c6f29d36f8d302c6f0e 2500w" /></Frame>

The basic functionality is working great! Together AI (with Kimi K2) + Sandpack have made it a breeze to run generated code right in our user’s browser.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
