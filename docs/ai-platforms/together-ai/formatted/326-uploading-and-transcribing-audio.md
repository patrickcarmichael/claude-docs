---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Uploading and transcribing audio

Once we have our audio blob (from recording) or file (from upload), we need to send it to Together AI's Whisper model. We use S3 for temporary storage and tRPC for type-safe API calls:
```tsx
const handleSaveRecording = async () => {
  if (!audioBlob) return;

  try {
    // Upload to S3
    const file = new File([audioBlob], `recording-${Date.now()}.webm`, {
      type: "audio/webm",
    });
    const { url } = await uploadToS3(file);

    // Call our tRPC endpoint
    const { id } = await transcribeMutation.mutateAsync({
      audioUrl: url,
      language: selectedLanguage,
      durationSeconds: duration,
    });

    // Navigate to transcription page
    router.push(`/whispers/${id}`);
  } catch (err) {
    toast.error("Failed to transcribe audio. Please try again.");
  }
};
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
