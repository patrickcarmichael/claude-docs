---
title: "Checkpoints"
source: "https://docs.cursor.com/de/agent/chat/checkpoints"
language: "de"
language_name: "German"
---

# Checkpoints
Source: https://docs.cursor.com/de/agent/chat/checkpoints

Frühere Zustände nach Agent-Änderungen speichern und wiederherstellen

Checkpoints sind automatische Snapshots der Änderungen des Agents an deinem Codebase. Damit kannst du Agent-Änderungen bei Bedarf rückgängig machen.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Checkpoints wiederherstellen
</div>

Zwei Möglichkeiten zur Wiederherstellung:

1. **Über das Eingabefeld**: Klicke bei vorherigen Anfragen auf den Button „Restore Checkpoint“
2. **Über die Nachricht**: Klicke auf den „+“-Button, wenn du mit der Maus über eine Nachricht fährst

<Warning>
  Checkpoints sind keine Versionsverwaltung. Nutze Git für dauerhafte Historie.
</Warning>

<div id="how-they-work">
  ## So funktionieren sie
</div>

* Lokal gespeichert, getrennt von Git
* Es werden nur Agent-Änderungen nachverfolgt (keine manuellen Änderungen)
* Wird automatisch bereinigt

<Note>
  Manuelle Änderungen werden nicht nachverfolgt. Verwende Checkpoints nur für Agent-Änderungen.
</Note>

<div id="faq">
  ## FAQ
</div>

<AccordionGroup>
  <Accordion title="Beeinflussen Checkpoints Git?">
    Nein. Sie sind getrennt vom Git-Verlauf.
  </Accordion>

  {" "}

  <Accordion title="Wie lange werden sie aufbewahrt?">
    Für die aktuelle Sitzung und die jüngste Historie. Wird automatisch bereinigt.
  </Accordion>

  <Accordion title="Kann ich sie manuell erstellen?">
    Nein. Sie werden automatisch von Cursor erstellt.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Commands](./commands.md) →