---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building the audio recording interface

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=56a54a41ccd4f317e72f7046cf3aaee0" alt="Recording modal UI" data-og-width="699" width="699" data-og-height="384" height="384" data-path="images/guides/whisper/recording-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=f08d68857caa9d4155de1ee64ea8213c 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=ab8b211d7ffb16cff04aaadc37eb1207 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=92778c223fed6d1e7fe9f67928ded434 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bc84a97166e1c8d7c5b8ed2eaabf37f1 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=67878551dfe6fdb7b029545c64e085aa 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=96a49d291ecfa1cbf99bed6a01ca3ed4 2500w" />

Whisper's core interaction is a recording modal where users can capture audio directly in the browser:
```tsx
function RecordingModal({ onClose }: { onClose: () => void }) {
  const { recording, audioBlob, startRecording, stopRecording } =
    useAudioRecording();

  const handleRecordingToggle = async () => {
    if (recording) {
      stopRecording();
    } else {
      await startRecording();
    }
  };

  // Auto-process when we get an audio blob
  useEffect(() => {
    if (audioBlob) {
      handleSaveRecording();
    }
  }, [audioBlob]);

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent>
        <Button onClick={handleRecordingToggle}>
          {recording ? "Stop Recording" : "Start Recording"}
        </Button>
      </DialogContent>
    </Dialog>
  );
}
```

The magic happens in our custom `useAudioRecording` hook, which handles all the browser audio recording logic.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
