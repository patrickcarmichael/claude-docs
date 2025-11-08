---
title: "Checkpoints"
source: "https://docs.cursor.com/en/agent/chat/checkpoints"
language: "en"
language_name: "English"
---

# Checkpoints
Source: https://docs.cursor.com/en/agent/chat/checkpoints

Save and restore previous states after Agent changes

Checkpoints are automatic snapshots of Agent's changes to your codebase. They let you undo Agent modifications if needed.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

## Restoring checkpoints

Two ways to restore:

1. **From input box**: Click `Restore Checkpoint` button on previous requests
2. **From message**: Click the + button when hovering over a message

<Warning>
  Checkpoints are not version control. Use Git for permanent history.
</Warning>

## How they work

* Stored locally, separate from Git
* Track only Agent changes (not manual edits)
* Cleaned up automatically

<Note>
  Manual edits aren't tracked. Only use checkpoints for Agent changes.
</Note>

## FAQ

<AccordionGroup>
  <Accordion title="Do checkpoints affect Git?">
    No. They're separate from Git history.
  </Accordion>

  {" "}

  <Accordion title="How long are they kept?">
    For the current session and recent history. Automatically cleaned up.
  </Accordion>

  <Accordion title="Can I create them manually?">
    No. They're created automatically by Cursor.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Commands](./commands.md) →