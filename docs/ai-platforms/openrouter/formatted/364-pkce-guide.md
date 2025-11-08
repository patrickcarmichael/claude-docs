---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## PKCE Guide

### Step 1: Send your user to OpenRouter

To start the PKCE flow, send your user to OpenRouter's `/auth` URL with a `callback_url` parameter pointing back to your site:
```txt title="With S256 Code Challenge (Recommended)" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=S256
```
```txt title="With Plain Code Challenge" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>&code_challenge=<CODE_CHALLENGE>&code_challenge_method=plain
```
```txt title="Without Code Challenge" wordWrap
  https://openrouter.ai/auth?callback_url=<YOUR_SITE_URL>
```

The `code_challenge` parameter is optional but recommended.

Your user will be prompted to log in to OpenRouter and authorize your app. After authorization, they will be redirected back to your site with a `code` parameter in the URL:

![Alt text](file:22f4b2e3-1cfe-4419-a1c0-ae611c98040e)

<Tip title="Use SHA-256 for Maximum Security">
  For maximum security, set `code_challenge_method` to `S256`, and set `code_challenge` to the base64 encoding of the sha256 hash of `code_verifier`.

  For more info, [visit Auth0's docs](https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-authorization-code-flow-with-pkce#parameters).
</Tip>

#### How to Generate a Code Challenge

The following example leverages the Web Crypto API and the Buffer API to generate a code challenge for the S256 method. You will need a bundler to use the Buffer API in the web browser:
```typescript title="Generate Code Challenge"
  import { Buffer } from 'buffer';

  async function createSHA256CodeChallenge(input: string) {
    const encoder = new TextEncoder();
    const data = encoder.encode(input);
    const hash = await crypto.subtle.digest('SHA-256', data);
    return Buffer.from(hash).toString('base64url');
  }

  const codeVerifier = 'your-random-string';
  const generatedCodeChallenge = await createSHA256CodeChallenge(codeVerifier);
```

#### Localhost Apps

If your app is a local-first app or otherwise doesn't have a public URL, it is recommended to test with `http://localhost:3000` as the callback and referrer URLs.

When moving to production, replace the localhost/private referrer URL with a public GitHub repo or a link to your project website.

### Step 2: Exchange the code for a user-controlled API key

After the user logs in with OpenRouter, they are redirected back to your site with a `code` parameter in the URL:

![Alt text](file:dd2980ed-1eea-4ed7-b37e-e4cc5cfaff5b)

Extract this code using the browser API:
```typescript title="Extract Code"
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');
```

Then use it to make an API call to `https://openrouter.ai/api/v1/auth/keys` to exchange the code for a user-controlled API key:
```typescript title="Exchange Code"
  const response = await fetch('https://openrouter.ai/api/v1/auth/keys', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code: '<CODE_FROM_QUERY_PARAM>',
      code_verifier: '<CODE_VERIFIER>', // If code_challenge was used
      code_challenge_method: '<CODE_CHALLENGE_METHOD>', // If code_challenge was used
    }),
  });

  const { key } = await response.json();
```

And that's it for the PKCE flow!

### Step 3: Use the API key

Store the API key securely within the user's browser or in your own database, and use it to [make OpenRouter requests](/api-reference/completion).
```typescript title="TypeScript SDK"
  import { OpenRouter } from '@openrouter/sdk';

  const openRouter = new OpenRouter({
    apiKey: key, // The key from Step 2
  });

  const completion = await openRouter.chat.send({
    model: 'openai/gpt-4o',
    messages: [
      {
        role: 'user',
        content: 'Hello!',
      },
    ],
    stream: false,
  });

  console.log(completion.choices[0].message);
```
```typescript title="TypeScript (fetch)"
  fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${key}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-4o',
      messages: [
        {
          role: 'user',
          content: 'Hello!',
        },
      ],
    }),
  });
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
