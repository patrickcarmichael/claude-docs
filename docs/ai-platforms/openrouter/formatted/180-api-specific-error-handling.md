---
title: "OpenRouter Documentation"
description: "Formatted documentation for OpenRouter"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## API-Specific Error Handling

Different OpenRouter API endpoints handle errors in distinct ways:

### OpenAI Chat Completions API (`/api/v1/chat/completions`)

* **No tokens sent**: Returns standalone `ErrorResponse`
* **Some tokens sent**: Embeds error information within the `choices` array of the final response
* **Streaming**: Errors sent as SSE events with top-level error field

### OpenAI Responses API (`/api/alpha/responses`)

* **Error transformations**: Certain errors become successful responses with appropriate finish reasons
* **Streaming events**: Uses typed events (`response.failed`, `response.error`, `error`)
* **Graceful degradation**: Handles provider-specific errors with fallback behavior

### Error Response Type Definitions

```typescript
// Standard error response
interface ErrorResponse {
  error: {
    code: number;
    message: string;
    metadata?: Record<string, unknown>;
  };
}

// Mid-stream error with completion data
interface StreamErrorChunk {
  error: {
    code: string | number;
    message: string;
  };
  choices: Array<{
    delta: { content: string };
    finish_reason: 'error';
    native_finish_reason: string;
  }>;
}

// Responses API error event
interface ResponsesAPIErrorEvent {
  type: 'response.failed' | 'response.error' | 'error';
  error?: {
    code: string;
    message: string;
  };
  response?: {
    id: string;
    status: 'failed';
    error: {
      code: string;
      message: string;
    };
  };
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
