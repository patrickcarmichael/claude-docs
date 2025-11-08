---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## getCurrentKeyMetadata

Get information on the API key associated with the current authentication session

### Example Usage

{/* UsageSnippet language="typescript" operationID="getCurrentKey" method="get" path="/key" */}
```typescript
import { OpenRouter } from "@openrouter/sdk";

const openRouter = new OpenRouter({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const result = await openRouter.apiKeys.getCurrentKeyMetadata();

  console.log(result);
}

run();
```

### Standalone function

The standalone function version of this method:
```typescript
import { OpenRouterCore } from "@openrouter/sdk/core.js";
import { apiKeysGetCurrentKeyMetadata } from "@openrouter/sdk/funcs/apiKeysGetCurrentKeyMetadata.js";

// Use `OpenRouterCore` for best tree-shaking performance.
// You can create one instance of it to use across an application.
const openRouter = new OpenRouterCore({
  apiKey: process.env["OPENROUTER_API_KEY"] ?? "",
});

async function run() {
  const res = await apiKeysGetCurrentKeyMetadata(openRouter);
  if (res.ok) {
    const { value: result } = res;
    console.log(result);
  } else {
    console.log("apiKeysGetCurrentKeyMetadata failed:", res.error);
  }
}

run();
```

### React hooks and utilities

This method can be used in React components through the following hooks and
associated utilities.

> Check out [this guide][hook-guide] for information about each of the utilities
> below and how to get started using React hooks.

[hook-guide]: ../../../REACT_QUERY.md
```tsx
import {
  // Query hooks for fetching data.
  useApiKeysGetCurrentKeyMetadata,
  useApiKeysGetCurrentKeyMetadataSuspense,

  // Utility for prefetching data during server-side rendering and in React
  // Server Components that will be immediately available to client components
  // using the hooks.
  prefetchApiKeysGetCurrentKeyMetadata,
  
  // Utility to invalidate the query cache for this query in response to
  // mutations and other user actions.
  invalidateAllApiKeysGetCurrentKeyMetadata,
} from "@openrouter/sdk/react-query/apiKeysGetCurrentKeyMetadata.js";
```

### Parameters

| Parameter              | Type                                                                                    | Required             | Description                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `options`              | RequestOptions                                                                          | :heavy\_minus\_sign: | Used to set various options for making HTTP requests.                                                                                                                          |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request#options) | :heavy\_minus\_sign: | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries`      | [RetryConfig](/docs/sdks/typescript/lib/retryconfig)                                    | :heavy\_minus\_sign: | Enables retrying HTTP requests under certain failure conditions.                                                                                                               |

### Response

**Promise\<[operations.GetCurrentKeyResponse](/docs/sdks/typescript/operations/getcurrentkeyresponse)>**

### Errors

| Error Type                         | Status Code | Content Type     |
| ---------------------------------- | ----------- | ---------------- |
| errors.UnauthorizedResponseError   | 401         | application/json |
| errors.InternalServerResponseError | 500         | application/json |
| errors.OpenRouterDefaultError      | 4XX, 5XX    | \*/\*            |


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
