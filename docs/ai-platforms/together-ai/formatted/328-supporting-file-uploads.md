---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Supporting file uploads

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=469a391f117228a11de74c751b49996c" alt="Upload modal UI" data-og-width="664" width="664" data-og-height="408" height="408" data-path="images/guides/whisper/upload-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=db453b15f4720d9fe62b6363a3667fc9 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1dddb61895e556c1a755541932cbd7a8 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=645f34df69928a02dbe627f36a05d464 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bddc420aecbd3b49437ab7a833f80c3b 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=25dc288c6b3a79e9dc3a5ae570ad0699 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=231d74b13ade1d1e94df0a37d1b79517 2500w" />

For users who want to upload existing audio files, we use react-dropzone and next-s3-upload.

Next-s3-upload handles the S3 upload in the backend and fully integrates with Next.js API routes in a simple 5 minute setup you can read more here: [https://next-s3-upload.codingvalue.com/](https://next-s3-upload.codingvalue.com/)
:
```tsx
import Dropzone from "react-dropzone";
import { useS3Upload } from "next-s3-upload";

function UploadModal({ onClose }: { onClose: () => void }) {
  const { uploadToS3 } = useS3Upload();

  const handleDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    try {
      // Get audio duration and upload in parallel
      const [duration, { url }] = await Promise.all([
        getDuration(file),
        uploadToS3(file),
      ]);

      // Transcribe using the same endpoint
      const { id } = await transcribeMutation.mutateAsync({
        audioUrl: url,
        language,
        durationSeconds: Math.round(duration),
      });

      router.push(`/whispers/${id}`);
    } catch (err) {
      toast.error("Failed to transcribe audio. Please try again.");
    }
  }, []);

  return (
    <Dropzone
      accept={{
        "audio/mpeg3": [".mp3"],
        "audio/wav": [".wav"],
        "audio/mp4": [".m4a"],
      }}
      onDrop={handleDrop}
    >
      {({ getRootProps, getInputProps }) => (
        <div {...getRootProps()}>
          <input {...getInputProps()} />
          <p>Drop audio files here or click to upload</p>
        </div>
      )}
    </Dropzone>
  );
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
