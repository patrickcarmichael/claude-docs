---
title: "Diffs y revisión"
source: "https://docs.cursor.com/es/agent/review"
language: "es"
language_name: "Spanish"
---

# Diffs y revisión
Source: https://docs.cursor.com/es/agent/review

Revisa y gestiona los cambios de código generados por el agente de IA

Cuando Agent genera cambios de código, se muestran en una interfaz de revisión que marca adiciones y eliminaciones con líneas codificadas por color. Esto te permite revisar y controlar qué cambios se aplican a tu base de código.

La interfaz de revisión muestra los cambios de código en un formato diff familiar:

<div id="diffs">
  ## Diffs
</div>

<div className="full-width-table">
  | Tipo                   | Significado                      | Ejemplo                                                                                               |
  | :--------------------- | :------------------------------- | :---------------------------------------------------------------------------------------------------- |
  | **Líneas añadidas**    | Nuevas incorporaciones de código | <code className="bg-green-100 text-green-800 px-2 py-1 rounded">+ const newVariable = 'hello';</code> |
  | **Líneas eliminadas**  | Eliminaciones de código          | <code className="bg-red-100 text-red-800 px-2 py-1 rounded">- const oldVariable = 'goodbye';</code>   |
  | **Líneas de contexto** | Código circundante sin cambios   | <code className="bg-gray-100 text-gray-600 px-2 py-1 rounded"> function example() {}</code>           |
</div>

<div id="review">
  ## Revisión
</div>

Cuando termine la generación, vas a ver un aviso para revisar todos los cambios antes de continuar. Esto te da una vista general de lo que se va a modificar.

<Frame>
  <img src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=10633167c76c24c1e69748ef93dc3888" alt="Interfaz de revisión de entrada" data-og-width="2095" width="2095" data-og-height="1178" height="1178" data-path="images/chat/review/input-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=280&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=f462337898ca48f71cd2b570b140d30d 280w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=560&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=07c91dfc92110cce444da8bbf3d0b3b5 560w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=840&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=492522862dabae6243fa8d33f6fd77f2 840w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1100&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=c897e19ce7f508bad4e24fcf8efb2512 1100w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=1650&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=3956c2d2c5c9156181b19e262e301b5b 1650w, https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/input-review.png?w=2500&fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=907f90b1db432128964a7f4e59523bb6 2500w" />
</Frame>

<div id="file-by-file">
  ### Archivo por archivo
</div>

Aparece una barra de revisión flotante en la parte inferior de tu pantalla que te permite:

* **Aceptar** o **rechazar** cambios del archivo actual
* Ir al **siguiente archivo** con cambios pendientes
  <Frame>
    <video src="https://mintcdn.com/cursor/BfJOqJ1Wb8EvuXyr/images/chat/review/review-bar.mp4?fit=max&auto=format&n=BfJOqJ1Wb8EvuXyr&q=85&s=5dca0fe7aba3c79e6760cb264821a617" autoPlay loop muted playsInline controls data-path="images/chat/review/review-bar.mp4">
      Tu navegador no admite la etiqueta de video.
    </video>
  </Frame>

<div id="selective-acceptance">
  ### Aceptación selectiva
</div>

Para un control más preciso:

* Para aceptar la mayoría de los cambios: rechazá las líneas que no querés y después hacé clic en **Aceptar todo**
* Para rechazar la mayoría de los cambios: aceptá las líneas que sí querés y después hacé clic en **Rechazar todo**

<div id="review-changes">
  ## Revisar cambios
</div>

Al final de la respuesta del agente, haz clic en el botón **Revisar cambios** para ver el diff completo de las modificaciones.

<Frame>
  <video src="https://www.cursor.com/changelog/049/review-ui.mp4" autoPlay loop muted playsInline controls />
</Frame>

---

← Previous: [Planificación](./planificacin.md) | [Index](./index.md) | Next: [Terminal](./terminal.md) →