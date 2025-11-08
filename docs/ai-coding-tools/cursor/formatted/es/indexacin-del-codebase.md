---
title: "Indexación del codebase"
source: "https://docs.cursor.com/es/context/codebase-indexing"
language: "es"
language_name: "Spanish"
---

# Indexación del codebase
Source: https://docs.cursor.com/es/context/codebase-indexing

Cómo Cursor aprende tu codebase para entenderla mejor

Cursor indexa tu codebase calculando embeddings para cada archivo. Esto mejora las respuestas generadas por IA sobre tu código. Cuando abres un proyecto, Cursor empieza a indexar automáticamente. Los archivos nuevos se indexan de forma incremental.
Revisa el estado de la indexación en: `Cursor Settings` > `Indexing & Docs`

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=47c946c1a46c8047feda127ef84faa9d" alt="Indicador de progreso de la indexación del codebase" data-og-width="2048" width="2048" data-og-height="1183" height="1183" data-path="images/get-started/codebase-indexing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=3d628d1692d4cc512f4a81ece7e4a2c5 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d5e20a24a9f38c97eb83249cd063ae41 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea26f1d9bf65ae5093333d15035ec96d 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1d532fe92021c50bee36b97e541419df 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=01c4cfe42a58ac06f6ac18e6e565782e 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/get-started/codebase-indexing.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=41d02dff523bfa3a33c6d4e86e79732a 2500w" />
</Frame>

<div id="configuration">
  ## Configuración
</div>

Cursor indexa todos los archivos excepto los que estén en [archivos de ignorados](/es/context/ignore-files) (p. ej., `.gitignore`, `.cursorignore`).

Haz clic en `Show Settings` para:

* Habilitar la indexación automática para repositorios nuevos
* Configurar qué archivos ignorar

<Tip>
  [Ignorar archivos de contenido grandes](/es/context/ignore-files) mejora la
  precisión de las respuestas.
</Tip>

<div id="view-indexed-files">
  ### Ver archivos indexados
</div>

Para ver las rutas de los archivos indexados: `Cursor Settings` > `Indexing & Docs` > `View included files`

Esto abre un archivo `.txt` con el listado de todos los archivos indexados.

<div id="multi-root-workspaces">
  ## Espacios de trabajo de múltiples raíces
</div>

Cursor admite [espacios de trabajo de múltiples raíces](https://code.visualstudio.com/docs/editor/workspaces#_multiroot-workspaces), lo que te permite trabajar con varias bases de código:

* Todas las bases de código se indexan automáticamente
* El contexto de cada base de código está disponible para la IA
* `.cursor/rules` funciona en todas las carpetas

<div id="pr-search">
  ## Búsqueda de PR
</div>

La búsqueda de PR te ayuda a entender la evolución de tu base de código al hacer que los cambios históricos sean consultables y accesibles con IA.

<div id="how-it-works">
  ### Cómo funciona
</div>

Cursor **indexa automáticamente todos los PR mergeados** del historial de tu repositorio. Los resúmenes aparecen en los resultados de búsqueda semántica, con filtrado inteligente para priorizar los cambios recientes.

Agent puede **traer PR, commits, issues o ramas** al contexto usando `@[PR number]`, `@[commit hash]` o `@[branch name]`. Incluye comentarios de GitHub y revisiones de Bugbot cuando está conectado.

**Compatibilidad de la plataforma**: GitHub, GitHub Enterprise y Bitbucket. GitLab no está actualmente disponible.

<Note>
  Usuarios de GitHub Enterprise: La herramienta de fetch recurre a comandos de git debido a
  limitaciones de autenticación de VSCode.
</Note>

<div id="using-pr-search">
  ### Uso de la búsqueda de PR
</div>

Haz preguntas como "¿Cómo se implementan los servicios en otros PR?" y Agent traerá automáticamente PR relevantes al contexto para ofrecer respuestas completas basadas en el historial de tu repositorio.

<div id="faq">
  ## Preguntas frecuentes
</div>

<AccordionGroup>
  <Accordion title="Where can I see all indexed codebases?">
    Aún no existe una lista global. Revisa cada proyecto por separado abriéndolo en
    Cursor y consultando la configuración de Codebase Indexing.
  </Accordion>

  <Accordion title="How do I delete all indexed codebases?">
    Elimina tu cuenta de Cursor desde Settings para borrar todas las bases de código indexadas.
    Si no, elimina las bases de código individualmente desde la configuración de Codebase Indexing
    de cada proyecto.
  </Accordion>

  <Accordion title="How long are indexed codebases retained?">
    Las bases de código indexadas se eliminan tras 6 semanas de inactividad. Al reabrir el
    proyecto, se vuelve a indexar.
  </Accordion>

  <Accordion title="Is my source code stored on Cursor servers?">
    No. Cursor crea embeddings sin almacenar nombres de archivo ni código fuente. Los nombres de archivo se ofuscan y los fragmentos de código se cifran.

    Cuando Agent busca en la base de código, Cursor recupera los embeddings del servidor y descifra los fragmentos.
  </Accordion>
</AccordionGroup>

---

← Previous: [/command](./command.md) | [Index](./index.md) | Next: [Ignorar archivos](./ignorar-archivos.md) →