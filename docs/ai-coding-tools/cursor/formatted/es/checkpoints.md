---
title: "Checkpoints"
source: "https://docs.cursor.com/es/agent/chat/checkpoints"
language: "es"
language_name: "Spanish"
---

# Checkpoints
Source: https://docs.cursor.com/es/agent/chat/checkpoints

Guarda y restaura estados anteriores después de cambios del Agent

Los checkpoints son instantáneas automáticas de los cambios que el Agent hace en tu base de código. Te permiten deshacer las modificaciones del Agent cuando lo necesites.

<Frame>
  <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/restore-checkpoint.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=7cededf7892f15a6342a81953ea0aa38" autoPlay loop muted playsInline controls data-path="images/chat/restore-checkpoint.mp4" />
</Frame>

<div id="restoring-checkpoints">
  ## Restaurar checkpoints
</div>

Dos formas de restaurar:

1. **Desde el cuadro de entrada**: haz clic en el botón `Restore Checkpoint` en solicitudes anteriores
2. **Desde el mensaje**: haz clic en el botón + al pasar el cursor sobre un mensaje

<Warning>
  Los checkpoints no son control de versiones. Usa Git para el historial permanente.
</Warning>

<div id="how-they-work">
  ## Cómo funcionan
</div>

* Se guardan localmente, aparte de Git
* Solo registran cambios del Agent (no ediciones manuales)
* Se limpian automáticamente

<Note>
  Las ediciones manuales no se registran. Usa checkpoints solo para cambios del Agent.
</Note>

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="¿Los checkpoints afectan a Git?">
    No. Son independientes del historial de Git.
  </Accordion>

  {" "}

  <Accordion title="¿Cuánto tiempo se conservan?">
    Solo durante la sesión actual y el historial reciente. Se eliminan automáticamente.
  </Accordion>

  <Accordion title="¿Puedo crearlos manualmente?">
    No. Cursor los crea automáticamente.
  </Accordion>
</AccordionGroup>

{" "}

---

← Previous: [Apply](./apply.md) | [Index](./index.md) | Next: [Comandos](./comandos.md) →