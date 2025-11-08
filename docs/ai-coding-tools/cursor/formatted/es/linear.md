---
title: "Linear"
source: "https://docs.cursor.com/es/integrations/linear"
language: "es"
language_name: "Spanish"
---

# Linear
Source: https://docs.cursor.com/es/integrations/linear

Trabaja con Background Agents desde Linear

Usa [Background Agents](/es/background-agent) directamente desde Linear delegando tareas a Cursor o mencionando `@Cursor` en los comentarios.

<Frame>
  <video src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-agent.mp4?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ac4bacf6bf42c541f45325ba72f8c25f" controls autoPlay muted loop playsInline data-path="images/integrations/linear/linear-agent.mp4" />
</Frame>

<div id="get-started">
  ## Empezá
</div>

<div id="installation">
  ### Instalación
</div>

<Note>
  Tenés que ser admin de Cursor para conectar la integración con Linear. Otras configuraciones del equipo están disponibles para miembros que no son admins.
</Note>

1. Andá a [Integraciones de Cursor](https://www.cursor.com/en/dashboard?tab=integrations)
2. Hacé clic en *Connect* junto a Linear
3. Conectá tu workspace de Linear y seleccioná el team
4. Hacé clic en *Authorize*
5. Completá cualquier configuración pendiente del Background Agent en Cursor:
   * Conectá GitHub y seleccioná el repositorio predeterminado
   * Activá el pricing basado en uso
   * Confirmá la configuración de privacidad

<div id="account-linking">
  ### Vinculación de cuenta
</div>

En el primer uso se te pide vincular las cuentas entre Cursor y Linear. Se requiere la conexión a GitHub para crear PR.

<div id="how-to-use">
  ## Cómo usar
</div>

Delegá issues a Cursor o mencioná `@Cursor` en los comentarios. Cursor analiza los issues y filtra automáticamente el trabajo que no es de desarrollo.

<div id="delegating-issues">
  ### Delegar issues
</div>

1. Abrí el issue en Linear
2. Hacé clic en el campo de asignación
3. Seleccioná "Cursor"

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=c9a6536a083cfe4a7798c626360e53cc" alt="Delegar un issue a Cursor en Linear" data-og-width="1637" width="1637" data-og-height="1046" height="1046" data-path="images/integrations/linear/linear-delegate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b30e2ccb68c4a15b921cf86721878676 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1ac5dfd75e06451de0e688ff87e1ce4c 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=7393e80c07e1fe5c33690a970029fe31 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=2a07cc74a1d65581a341cf2225b51a37 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=5684841fe823ef85472f74748730278c 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-delegate.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f7818cae47a652e14557eb20f20b04e 2500w" />
</Frame>

<div id="mentioning-cursor">
  ### Mencionar a Cursor
</div>

Mencioná `@Cursor` en un comentario para asignar un nuevo agente o dar instrucciones adicionales, por ejemplo: `@Cursor, solucioná el bug de autenticación descrito arriba`.

<div id="workflow">
  ## Flujo de trabajo
</div>

Los Background Agents muestran el estado en tiempo real en Linear y crean PR automáticamente cuando finalizan. Seguí el progreso en el [dashboard de Cursor](https://www.cursor.com/dashboard?tab=background-agents).

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=eecf562be6db4d44c397f4786b8ef273" alt="Actualizaciones de estado de Background Agent en Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-activity.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=238da245aee71392f22644cb85f7cee4 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=e21f515fbd2e5917fcf63b8801f66307 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=9f88441301e6d614ba47756cb886e023 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=4927a8d00768a3dbbc0bd5be1faad80e 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1707f8223126480c46639428ad5fc85a 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-activity.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=74ca2ad37e8158bbb86188821bf96299 2500w" />
</Frame>

<div id="follow-up-instructions">
  ### Instrucciones de seguimiento
</div>

Podés responder en la sesión del agente y se enviará como un seguimiento al propio agente. Simplemente mencioná `@Cursor` en un comentario de Linear para darle indicaciones adicionales a un Background Agent en ejecución.

<div id="configuration">
  ## Configuración
</div>

Configurá los ajustes de Background Agents desde [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div className="full-width-table">
  | Setting                | Location         | Description                                                                |
  | :--------------------- | :--------------- | :------------------------------------------------------------------------- |
  | **Default Repository** | Cursor Dashboard | Repositorio principal cuando no hay un repositorio de proyecto configurado |
  | **Default Model**      | Cursor Dashboard | Modelo de IA para Background Agents                                        |
  | **Base Branch**        | Cursor Dashboard | Rama desde la que crear PR (normalmente `main` o `develop`)                |
</div>

<div id="configuration-options">
  ### Opciones de configuración
</div>

Podés configurar el comportamiento de Background Agents usando varios métodos:

**Descripción del issue o comentarios**: Usá la sintaxis `[key=value]`, por ejemplo:

* `@cursor please fix [repo=anysphere/everysphere]`
* `@cursor implement feature [model=claude-3.5-sonnet] [branch=feature-branch]`

**Etiquetas del issue**: Usá una estructura de etiquetas padre-hijo donde la etiqueta padre es la clave de configuración y la etiqueta hija es el valor.

**Etiquetas del proyecto**: Misma estructura padre-hijo que las etiquetas del issue, aplicada a nivel de proyecto.

Claves de configuración admitidas:

* `repo`: Especificá el repositorio de destino (p. ej., `owner/repository`)
* `branch`: Especificá la rama base para la creación del PR
* `model`: Especificá el modelo de IA a usar

<div id="repository-selection">
  ### Selección de repositorio
</div>

Cursor determina en qué repositorio trabajar usando este orden de prioridad:

1. **Descripción/comentarios del issue**: Sintaxis `[repo=owner/repository]` en el texto del issue o comentarios
2. **Etiquetas del issue**: Etiquetas de repositorio asociadas al issue específico de Linear
3. **Etiquetas del proyecto**: Etiquetas de repositorio asociadas al proyecto de Linear
4. **Repositorio predeterminado**: Repositorio especificado en la configuración del dashboard de Cursor

<div id="setting-up-repository-labels">
  #### Configuración de etiquetas de repositorio
</div>

Para crear etiquetas de repositorio en Linear:

1. Andá a **Settings** en tu espacio de trabajo de Linear
2. Hacé clic en **Labels**
3. Hacé clic en **New group**
4. Nombrá el grupo "repo" (no distingue mayúsculas/minúsculas; debe ser exactamente "repo", no "Repository" ni otras variaciones)
5. Dentro de ese grupo, creá etiquetas para cada repositorio usando el formato `owner/repo`

Después podés asignar estas etiquetas a issues o proyectos para especificar en qué repositorio debería trabajar el Background Agent.

<Frame>
  <img src="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=6e2b90ce09957a72fdef3c1ed4ef93aa" alt="Configuring repository labels in Linear" data-og-width="3456" width="3456" data-og-height="2158" height="2158" data-path="images/integrations/linear/linear-project-labels.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=280&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=1933d2112631527116bd1d817f1a6153 280w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=560&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=93f344ff848172ce6bd97ef652ab03de 560w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=840&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=ea9f19d7248f39086a20606c6ec14ac6 840w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1100&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=55bfa5cf5b87def6cbe51c3345579eee 1100w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=1650&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=d99c0f06c5fbf33794408350b143f655 1650w, https://mintcdn.com/cursor/E7JVsKUF5L-IiJRB/images/integrations/linear/linear-project-labels.png?w=2500&fit=max&auto=format&n=E7JVsKUF5L-IiJRB&q=85&s=b1f731d1978dc5e60c545b745bb9d8ad 2500w" />
</Frame>

{/* ### Getting help

  Check [agent activity](https://www.cursor.com/dashboard?tab=background-agents) and include request IDs when contacting support.

  ## Feedback

  Share feedback through Linear comments or your Cursor dashboard support channels. */}

---

← Previous: [GitHub](./github.md) | [Index](./index.md) | Next: [Slack](./slack.md) →