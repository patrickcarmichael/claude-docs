---
title: "Seguridad del Agente"
source: "https://docs.cursor.com/es/account/agent-security"
language: "es"
language_name: "Spanish"
---

# Seguridad del Agente
Source: https://docs.cursor.com/es/account/agent-security

Consideraciones de seguridad para usar Cursor Agent

La inyección de prompts, las alucinaciones de IA y otros problemas pueden hacer que la IA se comporte de formas inesperadas y potencialmente maliciosas. Mientras seguimos trabajando para resolver la inyección de prompts a un nivel más fundamental, nuestra protección principal en los productos de Cursor son los rieles de seguridad sobre lo que un agente puede hacer, incluyendo exigir aprobación manual para acciones sensibles de forma predeterminada. El objetivo de este documento es explicar estos rieles de seguridad y qué pueden esperar los usuarios de ellos.

Todos los controles y comportamientos a continuación son nuestra configuración predeterminada y recomendada.

<div id="first-party-tool-calls">
  ## Llamadas a herramientas nativas
</div>

Cursor viene con herramientas integradas que le permiten al agente ayudarte a escribir código. Estas incluyen lectura de archivos, edición, ejecución de comandos de terminal, búsqueda de documentación en la web y otras.

Las herramientas de lectura no requieren aprobación (p. ej., leer archivos, buscar en el código). Puedes usar [.cursorignore](/es/context/ignore-files) para bloquear por completo el acceso del agente a archivos específicos, pero en caso contrario las lecturas generalmente están permitidas sin aprobación. Para acciones que conllevan riesgo de exfiltración de datos sensibles, requerimos aprobación explícita.

Modificar archivos dentro del espacio de trabajo actual no requiere aprobación explícita con algunas excepciones. Cuando un agente realiza cambios en archivos, estos se guardan inmediatamente en disco. Recomendamos ejecutar Cursor en espacios de trabajo con control de versiones, de modo que el contenido de los archivos pueda revertirse en cualquier momento. Requerimos aprobación explícita antes de cambiar archivos que modifiquen la configuración de nuestro IDE/CLI, como el archivo de configuración del espacio de trabajo del editor. Sin embargo, si tienes recarga automática al detectar cambios en archivos, ten en cuenta que los cambios del agente pueden activar ejecuciones automáticas antes de que hayas tenido oportunidad de revisarlos.

Cualquier comando de terminal sugerido por los agentes requiere aprobación de forma predeterminada. Recomendamos revisar cada comando antes de que el agente lo ejecute. Quienes acepten el riesgo pueden habilitar que el agente ejecute todos los comandos sin aprobación. Incluimos una [allowlist](/es/agent/tools) en Cursor, pero no la consideramos un control de seguridad. Algunas personas eligen permitir comandos específicos, pero es un sistema de mejor esfuerzo y pueden existir formas de eludirlo. No recomendamos "Run Everything", que omite cualquier allowlist configurada.

<div id="third-party-tool-calls">
  ## Llamadas a herramientas de terceros
</div>

Cursor permite conectar herramientas externas a través de [MCP](/es/context/mcp). Todas las conexiones MCP de terceros deben ser aprobadas explícitamente por el usuario. Una vez que el usuario aprueba un MCP, de forma predeterminada cada llamada de herramienta sugerida en Agent Mode para cualquier integración MCP externa debe ser aprobada explícitamente antes de su ejecución.

<div id="network-requests">
  ## Solicitudes de red
</div>

Un atacante podría usar las solicitudes de red para exfiltrar datos. Actualmente no admitimos que herramientas propias realicen solicitudes de red fuera de un conjunto muy selecto de hosts (p. ej., GitHub), la recuperación explícita de enlaces ni el uso de la búsqueda web más que con un conjunto selecto de proveedores. Con la configuración predeterminada se impiden las solicitudes de red arbitrarias por parte de agentes.

<div id="workspace-trust">
  ## Confianza del espacio de trabajo
</div>

El IDE de Cursor admite la función estándar de [workspace trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust), que está *desactivada* de forma predeterminada. Workspace trust te muestra un aviso al abrir un nuevo espacio de trabajo para elegir entre modo normal o restringido. El modo restringido inutiliza la IA y otras funciones por las que normalmente usas Cursor. Te recomendamos usar otras herramientas, como un editor de texto básico, para trabajar con repos en los que no confíes.

Puedes habilitar workspace trust en la configuración de usuario siguiendo estos pasos:

1. Abre tu archivo de usuario settings.json
2. Agrega la siguiente configuración:
   ```json  theme={null}
   "security.workspace.trust.enabled": true
   ```

Esta configuración también puede aplicarse a nivel de organización mediante soluciones de Mobile Device Management (MDM).

<div id="responsible-disclosure">
  ## Divulgación responsable
</div>

Si crees que has encontrado una vulnerabilidad en Cursor, sigue la guía en nuestra página de seguridad de GitHub y envía el informe ahí. Si no puedes usar GitHub, también puedes escribirnos a [security@cursor.com](mailto:security@cursor.com).

Nos comprometemos a acusar recibo de los informes de vulnerabilidades en un plazo de 5 días hábiles y a resolverlos tan pronto como podamos. Publicaremos los resultados en forma de avisos de seguridad en nuestra página de seguridad de GitHub. Los incidentes críticos se comunicarán tanto en la página de seguridad de GitHub como por correo electrónico a todos los usuarios.

---

← Previous: [Index](./index.md) | [Index](./index.md) | Next: [Facturación](./facturacin.md) →