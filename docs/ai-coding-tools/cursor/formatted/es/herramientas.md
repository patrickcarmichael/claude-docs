---
title: "Herramientas"
source: "https://docs.cursor.com/es/agent/tools"
language: "es"
language_name: "Spanish"
---

# Herramientas
Source: https://docs.cursor.com/es/agent/tools

Herramientas disponibles para que los agentes busquen, editen y ejecuten código

Una lista de todas las herramientas disponibles para los modos dentro de [Agent](/es/agent/overview), que podés habilitar o deshabilitar al crear tus propios [modos personalizados](/es/agent/modes#custom).

<Note>
  No hay límite en la cantidad de llamadas a herramientas que Agent puede hacer durante una tarea. Agent seguirá usando herramientas según sea necesario para completar tu pedido.
</Note>

<div id="search">
  ## Búsqueda
</div>

Herramientas para buscar en tu código y en la web y encontrar información relevante.

<AccordionGroup>
  <Accordion title="Read File" icon="file-lines">
    Lee hasta 250 líneas (750 en modo máximo) de un archivo.
  </Accordion>

  <Accordion title="List Directory" icon="folder-open">
    Lee la estructura de un directorio sin leer el contenido de los archivos.
  </Accordion>

  <Accordion title="Codebase" icon="database">
    Realiza búsquedas semánticas en tu [código
    indexado](/es/context/codebase-indexing).
  </Accordion>

  <Accordion title="Grep" icon="magnifying-glass">
    Busca palabras clave o patrones exactos dentro de archivos.
  </Accordion>

  <Accordion title="Search Files" icon="file-magnifying-glass">
    Encuentra archivos por nombre usando coincidencia difusa.
  </Accordion>

  <Accordion title="Web" icon="globe">
    Genera consultas y realiza búsquedas en la web.
  </Accordion>

  <Accordion title="Fetch Rules" icon="gavel">
    Obtén [reglas](/es/context/rules) específicas según el tipo y la descripción.
  </Accordion>
</AccordionGroup>

<div id="edit">
  ## Editar
</div>

Herramientas para hacer cambios específicos en tus archivos y tu código.

<AccordionGroup>
  <Accordion title="Editar y reaplicar" icon="pencil">
    Sugiere cambios en archivos y [aplícalos](/es/agent/apply) automáticamente.
  </Accordion>

  <Accordion title="Eliminar archivo" icon="trash">
    Elimina archivos de forma autónoma (puedes desactivarlo en la configuración).
  </Accordion>
</AccordionGroup>

<div id="run">
  ## Ejecutar
</div>

Chat puede interactuar con tu terminal.

<AccordionGroup>
  <Accordion title="Terminal" icon="terminal">
    Ejecuta comandos en la terminal y monitorea la salida.
  </Accordion>
</AccordionGroup>

<Note>De forma predeterminada, Cursor usa el primer perfil de terminal disponible.</Note>

Para establecer tu perfil de terminal preferido:

1. Abre la paleta de comandos (`Cmd/Ctrl+Shift+P`)
2. Busca "Terminal: Select Default Profile"
3. Elige el perfil que quieras

<div id="mcp">
  ## MCP
</div>

Chat puede usar servidores MCP configurados para interactuar con servicios externos, como bases de datos o API de terceros.

<AccordionGroup>
  <Accordion title="Activar/desactivar servidores MCP" icon="server">
    Activa o desactiva los servidores MCP disponibles. Respeta la configuración de ejecución automática.
  </Accordion>
</AccordionGroup>

Aprende más sobre el [Model Context Protocol](/es/context/model-context-protocol) y explora los servidores disponibles en el [directorio de MCP](/es/tools).

<div id="advanced-options">
  ## Opciones avanzadas
</div>

<AccordionGroup>
  <Accordion title="Aplicar ediciones automáticamente" icon="check">
    Aplica las ediciones automáticamente sin confirmación manual.
  </Accordion>

  <Accordion title="Ejecución automática" icon="play">
    Ejecuta automáticamente comandos de terminal y acepta ediciones. Útil para ejecutar suites de pruebas y verificar cambios.

    <Frame>
      <img src="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=3135722076a5aa636d27dbedec665bae" data-og-width="1624" width="1624" data-og-height="1012" height="1012" data-path="images/agent/auto-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=280&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9f2e2bed8f634201adc51ccb2bd96cd2 280w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=560&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=51704cac2f270a04856fffbeaccf9700 560w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=840&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=01a5034975497a8dff4f41dca0d19f2e 840w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1100&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=5f19026a0c6e5fb28c935ce795edb706 1100w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=1650&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=a108fc86f8ee7c0db6e5b7ab80ede738 1650w, https://mintcdn.com/cursor/M0haYabx4OPGBjqe/images/agent/auto-run.png?w=2500&fit=max&auto=format&n=M0haYabx4OPGBjqe&q=85&s=9ce5f45879c29049640bb5a1494db11e 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Guardrails" icon="shield">
    Configura listas de permitidos para especificar qué herramientas pueden ejecutarse automáticamente. Estas listas mejoran la seguridad al definir explícitamente las operaciones permitidas.
  </Accordion>

  <Accordion title="Corregir errores automáticamente" icon="wrench">
    Resuelve automáticamente los errores y advertencias del linter cuando el Agent los encuentre.
  </Accordion>
</AccordionGroup>

---

← Previous: [Terminal](./terminal.md) | [Index](./index.md) | Next: [Agentes en segundo plano](./agentes-en-segundo-plano.md) →