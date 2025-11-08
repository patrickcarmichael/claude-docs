---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Type safety with tRPC

One of the key benefits of using tRPC is the end-to-end type safety. When we call our API from the frontend:
```tsx
const transcribeMutation = useMutation(
  trpc.whisper.transcribeFromS3.mutationOptions()
);

// TypeScript knows the exact shape of the input and output
const result = await transcribeMutation.mutateAsync({
  audioUrl: "...",
  language: "en", // TypeScript validates this
  durationSeconds: 120,
});

// result.id is properly typed
router.push(`/whispers/${result.id}`);
```

This eliminates runtime errors and provides excellent developer experience with autocomplete and type checking.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
