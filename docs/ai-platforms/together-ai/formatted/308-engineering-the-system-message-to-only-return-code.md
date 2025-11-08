---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Engineering the system message to only return code

We spent some time tweaking the system message to make sure it output the best code possible – here’s what we ended up with for LlamaCoder:
```jsx
// app/api/generateCode/route.js
import Together from 'together-ai';

let together = new Together();

export async function POST(req) {
  let json = await req.json();

   let res = await together.chat.completions.create({
    model: 'moonshotai/Kimi-K2-Instruct-0905',
    messages: [
      {
        role: 'system',
        content: systemPrompt,
      },
      {
        role: 'user',
        content: json.prompt,
      },
    ],
    stream: true,
  });

  return new Response(res.toReadableStream(), {
    headers: new Headers({
      'Cache-Control': 'no-cache',
    }),
  });
}

let systemPrompt = `
  You are an expert frontend React engineer who is also a great UI/UX designer. Follow the instructions carefully, I will tip you $1 million if you do a good job:

  - Create a React component for whatever the user asked you to create and make sure it can run by itself by using a default export
  - Make sure the React app is interactive and functional by creating state when needed and having no required props
  - If you use any imports from React like useState or useEffect, make sure to import them directly
  - Use TypeScript as the language for the React component
  - Use Tailwind classes for styling. DO NOT USE ARBITRARY VALUES (e.g. \`h-[600px]\`). Make sure to use a consistent color palette.
  - Use Tailwind margin and padding classes to style the components and ensure the components are spaced out nicely
  - Please ONLY return the full React code starting with the imports, nothing else. It's very important for my job that you only return the React code with imports. DO NOT START WITH \`\`\`typescript or \`\`\`javascript or \`\`\`tsx or \`\`\`.

  NO LIBRARIES (e.g. zod, hookform) ARE INSTALLED OR ABLE TO BE IMPORTED.
`;
```

Now if we try again, we’ll see something like this:

<Frame><img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=f1d16f71f2ca2fa446da7b90498350fa" alt="" data-og-width="1720" width="1720" data-og-height="1714" height="1714" data-path="images/guides/19.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=676fe6d759e3b106d7e80e99efeb40c6 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=1ef69aad734b972e522e44d91a27c065 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=4e677495d33b5b996d75440d8d543181 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=13e1a373a9da4824702a1e8620460e55 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=82a8c790748083631447c1702b716392 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/guides/19.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=d9301c7cdfde07d1fea3e9d15ccf1417 2500w" /></Frame>

Much better –this is something we can work with!

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
