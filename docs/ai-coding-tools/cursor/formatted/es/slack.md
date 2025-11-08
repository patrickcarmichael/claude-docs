---
title: "Slack"
source: "https://docs.cursor.com/es/integrations/slack"
language: "es"
language_name: "Spanish"
---

# Slack
Source: https://docs.cursor.com/es/integrations/slack

Trabajá con agentes en segundo plano desde Slack

export const SlackThread = ({messages = []}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg bg-neutral-50 dark:bg-neutral-900/50 py-4 overflow-hidden">
      {messages.map((msg, index) => <div key={index} className={`group hover:bg-[#f0f0f0] dark:hover:bg-[#333] px-6 py-2 -mx-2 -my-1 transition-colors`}>
          <div className="flex items-start gap-3">
            <div className="w-9 h-9 rounded-md bg-neutral-300 dark:bg-neutral-800 flex items-center justify-center text-white text-sm font-semibold flex-shrink-0">
              {msg.name ? msg.name.charAt(0).toUpperCase() : 'U'}
            </div>

            <div className="flex-1 min-w-0">
              <div className="flex items-baseline gap-2">
                <span className="font-semibold text-neutral-900 dark:text-neutral-100 text-sm">
                  {msg.name || 'User'}
                </span>
                <span className="text-xs text-neutral-500 dark:text-neutral-400">
                  {msg.timestamp || ''}
                </span>
              </div>
              <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
                <MessageWithMentions text={msg.message} />
              </div>

              {msg.reactions && msg.reactions.length > 0 && <div className="flex gap-1 mt-1">
                  {msg.reactions.map((reaction, rIndex) => <div key={rIndex} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded text-xs hover:bg-neutral-100 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
                      <span>{reaction.emoji}</span>
                      <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
                    </div>)}
                </div>}
            </div>
          </div>
        </div>)}
    </div>;
};

export const SlackInlineMessage = ({message}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] hover:bg-[#1264A3]/10 dark:hover:bg-[#1264A3]/25 px-0.5 rounded">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <span className="inline rounded p-0.5 bg-neutral-50 dark:bg-neutral-800/30">
      <MessageWithMentions text={message} />
    </span>;
};

export const SlackUserMessage = ({message, reactions = [], replies = null}) => {
  const MessageWithMentions = ({text}) => {
    const parts = text.split(/(@\w+)/g);
    return <>
        {parts.map((part, index) => {
      if (part.startsWith('@')) {
        return <span key={index} className="text-[#1264A3] bg-[#1264A3]/10 dark:bg-[#1264A3]/25 px-0.5 py-0.5 rounded hover:bg-[#1264A3]/20 cursor-pointer transition-colors">
                {part}
              </span>;
      }
      return <span key={index}>{part}</span>;
    })}
      </>;
  };
  return <div className="border border-neutral-200 dark:border-neutral-700 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-800/50 transition-colors px-5 py-3 group">
      <div className="text-neutral-900 dark:text-neutral-100 text-[15px] leading-relaxed">
        <MessageWithMentions text={message} />
      </div>

      {reactions.length > 0 && <div className="flex gap-1 mt-1">
          {reactions.map((reaction, index) => <div key={index} className="inline-flex items-center gap-0.5 px-1.5 py-0.5 bg-neutral-100 dark:bg-neutral-800 rounded text-xs hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-colors cursor-pointer">
              <span>{reaction.emoji}</span>
              <span className="text-neutral-600 dark:text-neutral-400">{reaction.count}</span>
            </div>)}
        </div>}

      {replies && <div className="flex items-center gap-1.5 mt-2 text-[#1264A3] hover:underline cursor-pointer">
          <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
            <path d="M7.707 10.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V6h5a2 2 0 012 2v7a2 2 0 01-2 2H4a2 2 0 01-2-2V8a2 2 0 012-2h5v5.586l-1.293-1.293z" />
          </svg>
          <span className="text-sm font-medium">{replies.count} {replies.count === 1 ? 'reply' : 'replies'}</span>
          {replies.lastReplyTime && <span className="text-xs text-neutral-500 dark:text-neutral-400">{replies.lastReplyTime}</span>}
        </div>}
    </div>;
};

Con la integración de Cursor para Slack, podés usar [Background Agents](/es/background-agent) para trabajar en tus tareas directamente desde Slack mencionando <SlackInlineMessage message="@Cursor" /> junto con un prompt.

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-agent.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=aa7aa2681db1e363047334c6a8e33f72" controls autoplay muted loop data-path="images/background-agent/slack/slack-agent.mp4" />
</Frame>

<div id="get-started">
  ## Empezá
</div>

<div id="installation">
  ### Instalación
</div>

1. Andá a [Cursor integrations](https://www.cursor.com/en/dashboard?tab=integrations)

2. Hacé clic en *Connect* junto a Slack o andá a la [installation page](https://cursor.com/api/install-slack-app) desde acá

3. Se te va a pedir que instales la app de Cursor para Slack en tu workspace.

4. Después de instalar en Slack, vas a ser redirigido a Cursor para finalizar la configuración

   1. Conectá GitHub (si todavía no está conectado) y elegí un repositorio predeterminado
   2. Activá el pricing basado en uso
   3. Confirmá la configuración de privacidad

5. Empezá a usar Background Agents en Slack mencionando <SlackInlineMessage message="@Cursor" />

<Frame>
  <video src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/cursor-slack-install.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bd5b3c65b1a0de08b46c90515b6056a6" controls autoplay muted loop data-path="images/background-agent/slack/cursor-slack-install.mp4" />
</Frame>

<div id="how-to-use">
  ## Cómo usar
</div>

Mencioná a <SlackInlineMessage message="@Cursor" /> y pasale tu prompt. Esto cubre la mayoría de los casos de uso, pero también podés usar los comandos de abajo para personalizar tu agente.

Por ejemplo, mencioná <SlackInlineMessage message="@Cursor fix the login bug" /> directamente en la conversación, o usá comandos específicos como <SlackInlineMessage message="@Cursor [repo=torvalds/linux] fix bug" /> para apuntar a un repositorio en particular.

<div id="commands">
  ### Comandos
</div>

Ejecutá <SlackInlineMessage message="@Cursor help" /> para ver una lista de comandos actualizada.

<div className="full-width-table">
  | Command                                                     | Description                                                                                      |
  | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
  | <SlackInlineMessage message="@Cursor [prompt]" />           | Inicia un Background Agent. En hilos con agentes existentes, agrega instrucciones de seguimiento |
  | <SlackInlineMessage message="@Cursor settings" />           | Configurá los valores predeterminados y el repositorio predeterminado del canal                  |
  | <SlackInlineMessage message="@Cursor [options] [prompt]" /> | Usá opciones avanzadas: `branch`, `model`, `repo`                                                |
  | <SlackInlineMessage message="@Cursor agent [prompt]" />     | Forzá la creación de un agente nuevo en un hilo                                                  |
  | <SlackInlineMessage message="@Cursor list my agents" />     | Mostrá tus agentes en ejecución                                                                  |
</div>

<div id="options">
  #### Opciones
</div>

Personalizá el comportamiento del Background Agent con estas opciones:

<div className="full-width-table">
  | Option   | Description                                       | Example           |
  | :------- | :------------------------------------------------ | :---------------- |
  | `branch` | Especificá la rama base                           | `branch=main`     |
  | `model`  | Elegí el modelo de IA                             | `model=o3`        |
  | `repo`   | Apuntá a un repositorio específico                | `repo=owner/repo` |
  | `autopr` | Habilitá/deshabilitá la creación automática de PR | `autopr=false`    |
</div>

<div id="syntax-formats">
  ##### Formatos de sintaxis
</div>

Podés usar las opciones de varias maneras:

1. **Formato con corchetes**

   <SlackInlineMessage message="@Cursor [branch=dev, model=o3, repo=owner/repo, autopr=false] Fix the login bug" />

2. **Formato inline**
   <SlackInlineMessage message="@Cursor branch=dev model=o3 repo=owner/repo autopr=false Fix the login bug" />

<div id="option-precedence">
  ##### Precedencia de opciones
</div>

Al combinar opciones:

* Los valores explícitos sobrescriben los predeterminados
* Los valores posteriores sobrescriben a los anteriores si están duplicados
* Las opciones inline tienen prioridad sobre los valores predeterminados del modal de configuración

El bot analiza opciones desde cualquier parte del mensaje, permitiendo escribir comandos de forma natural.

<div id="using-thread-context">
  #### Uso del contexto del hilo
</div>

Los Background Agents entienden y usan el contexto de las discusiones existentes en el hilo. Es útil cuando tu equipo está discutiendo un problema y querés que el agente implemente la solución basada en esa conversación.

<SlackThread
  messages={[
{
  message:
    "Hey team, we're getting reports that users can't log in after the latest deploy",
  timestamp: "2:30 PM",
  name: "Sarah",
},
{
  message:
    "I checked the logs - looks like the auth token validation is failing on line 247 of auth.js",
  timestamp: "2:32 PM",
  name: "Mike",
},
{
  message:
    "Oh, I think it's because we changed the token format but didn't update the validation regex",
  timestamp: "2:33 PM",
  name: "Alex",
},
{
  message:
    "Yeah, the regex still expects the old format. We need to update it to handle both old and new formats for backwards compatibility",
  timestamp: "2:35 PM",
  name: "Sarah",
},
{
  message: "@Cursor fix this",
  timestamp: "2:36 PM",
  name: "You",
  reactions: [{ emoji: "⏳", count: 1 }],
},
]}
/>

<Note>
  Los Background Agents leen el hilo completo para obtener contexto cuando se invocan,
  entendiendo e implementando soluciones basadas en la discusión del equipo.
</Note>

<div id="when-to-use-force-commands">
  #### Cuándo usar comandos forzados
</div>

**¿Cuándo necesito <SlackInlineMessage message="@Cursor agent" />?**

En hilos con agentes existentes, <SlackInlineMessage message="@Cursor [prompt]" /> agrega instrucciones de seguimiento (solo funciona si sos el dueño del agente). Usá <SlackInlineMessage message="@Cursor agent [prompt]" /> para lanzar un agente aparte.

**¿Cuándo necesito `Add follow-up` (desde el menú contextual)?**

Usá el menú contextual (⋯) en la respuesta de un agente para dar instrucciones de seguimiento. Es útil cuando hay varios agentes en un hilo y necesitás especificar a cuál darle seguimiento.

<div id="status-updates-handoff">
  ### Actualizaciones de estado y handoff
</div>

Cuando se ejecuta el Background Agent, primero vas a ver la opción *Open in Cursor*.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=496d3775ca5cc1e20dd1dc34952f76fd" style={{ backgroundColor: "#1b1d21" }} data-og-width="1236" width="1236" data-og-height="258" height="258" data-path="images/background-agent/slack/slack-open-in-cursor.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9136ecf72e3f7e75b2178a2922878fbd 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5d6977f43055c3e8cb69071fe7b48367 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=5264cb584c1160bd8ac3cdeaae320777 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a065e6c1a08d4413464e1251eab1b2a6 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=e067f0dc80ed77bce7843f777f2d7970 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-open-in-cursor.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=fbcb8e474fd1681219964c558ea2952d 2500w" />
</Frame>

Cuando Background Agent termina, recibes una notificación en Slack y la opción de ver el PR creado en GitHub.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=d0f5f15094f682a5617c936bea88db3d" style={{ backgroundColor: "#1b1d21" }} data-og-width="1272" width="1272" data-og-height="496" height="496" data-path="images/background-agent/slack/slack-view-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=a51c98f13fef794ba8f54a28ad42e99d 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=bbde7fe552a04a8ed44b1771bbc3f55c 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=616811c969184b9061435e9753f63ddb 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90fe4582797d75782019c7d0c3232ea8 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ffe4d6a78cad700f82e770418c7f6e13 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-view-pr.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=ec4dac244e5982d0150d058ddac0d205 2500w" />
</Frame>

<div id="managing-agents">
  ### Administración de agentes
</div>

Para ver todos los agentes en ejecución, ejecuta <SlackInlineMessage message="@Cursor list my agents" />.

Gestiona los Background Agents usando el menú contextual haciendo clic en los tres puntos (⋯) en cualquier mensaje del agente.

<Frame>
  <img className="p-2" src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=9a92748d0f4d3450d51a2c2cdd989eb1" style={{ backgroundColor: "#1b1d21" }} data-og-width="1982" width="1982" data-og-height="1498" height="1498" data-path="images/background-agent/slack/slack-context-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=280&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=6af034b2f0c1b510510622b111c8d4e7 280w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=560&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=7d28c9785328aa414eba66704d7f4f08 560w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=840&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=810f99ed15ec100cdfee183ef9b7f827 840w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1100&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=f4c00c380996793b50d31ef3ac95219c 1100w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=1650&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=94bccdd7d7a9f1301fdb4e832e008efa 1650w, https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/background-agent/slack/slack-context-menu.png?w=2500&fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=90e628735b628ec71d5a78547db2441c 2500w" />
</Frame>

Opciones disponibles:

* **Add follow-up**: agregar instrucciones a un agente existente
* **Delete**: detener y archivar el Background Agent
* **View request ID**: ver el ID de solicitud único para solucionar problemas (inclúyelo al contactar con soporte)
* **Give feedback**: enviar comentarios sobre el rendimiento del agente

<div id="configuration">
  ## Configuración
</div>

Administra la configuración predeterminada y las opciones de privacidad desde [Dashboard → Background Agents](https://www.cursor.com/dashboard?tab=background-agents).

<div id="settings">
  ### Configuración
</div>

<div id="default-model">
  #### Modelo predeterminado
</div>

Se usa cuando no se especifica explícitamente un modelo con <SlackInlineMessage message="@Cursor [model=...]" />. Consulta la [configuración](https://www.cursor.com/dashboard?tab=background-agents) para ver las opciones disponibles.

<div id="default-repository">
  #### Repositorio predeterminado
</div>

Se usa cuando no se especifica un repositorio. Usa estos formatos:

* `https://github.com/org/repository`
* `org/repository`

<Note>
  Si haces referencia a un repositorio que no existe, parecerá que no tienes
  acceso. Esto se muestra en el mensaje de error cuando Background Agent no logra iniciarse.
</Note>

<div id="base-branch">
  #### Rama base
</div>

Rama inicial para Background Agent. Déjalo en blanco para usar la rama predeterminada del repositorio (normalmente `main`)

<div id="channel-settings">
  ### Configuración del canal
</div>

Configura valores predeterminados a nivel de canal usando <SlackInlineMessage message="@Cursor settings" />. Estas configuraciones son por equipo y sustituyen tus valores predeterminados personales para ese canal.

Es especialmente útil cuando:

* Distintos canales trabajan en diferentes repositorios
* Los equipos quieren configuraciones coherentes para todos los miembros
* Quieres evitar especificar el repositorio en cada comando

Para configurar la configuración del canal:

1. Ejecuta <SlackInlineMessage message="@Cursor settings" /> en el canal deseado
2. Establece el repositorio predeterminado para ese canal
3. Todos los miembros del equipo que usen Background Agents en ese canal usarán estos valores predeterminados

<Note>
  La configuración del canal tiene prioridad sobre los valores predeterminados personales, pero puede sobrescribirse
  con opciones explícitas como{" "}

  <SlackInlineMessage message="@Cursor [repo=...] [prompt]" />
</Note>

<div id="privacy">
  ### Privacidad
</div>

Los Background Agents admiten el Modo de Privacidad.

Lee más sobre el [Modo de Privacidad](https://www.cursor.com/privacy-overview) o administra tu [configuración de privacidad](https://www.cursor.com/dashboard?tab=background-agents).

<Warning>
  El Modo de Privacidad (Legacy) no es compatible. Los Background Agents requieren
  almacenamiento temporal de código mientras se ejecutan.
</Warning>

<div id="display-agent-summary">
  #### Mostrar resumen del agente
</div>

Muestra resúmenes del agente e imágenes de diferencias. Puede contener rutas de archivos o fragmentos de código. Se puede activar/desactivar.

<div id="display-agent-summary-in-external-channels">
  #### Mostrar resumen del agente en canales externos
</div>

Para Slack Connect con otros espacios de trabajo o canales con miembros externos como invitados, elige si quieres mostrar resúmenes del agente en canales externos.

<div id="permissions">
  ## Permisos
</div>

Cursor solicita estos permisos de Slack para que los Background Agents funcionen en tu espacio de trabajo:

<div className="full-width-table">
  | Permission          | Description                                                                                                    |
  | :------------------ | :------------------------------------------------------------------------------------------------------------- |
  | `app_mentions:read` | Detecta @mentions para iniciar Background Agents y responder a solicitudes                                     |
  | `channels:history`  | Lee mensajes anteriores en hilos para aportar contexto al agregar instrucciones de seguimiento                 |
  | `channels:join`     | Se une automáticamente a canales públicos cuando lo invitan o lo solicitan                                     |
  | `channels:read`     | Accede a metadatos de canales (IDs y nombres) para publicar respuestas y actualizaciones                       |
  | `chat:write`        | Envía actualizaciones de estado, notificaciones de finalización y enlaces a PR cuando los agentes terminan     |
  | `files:read`        | Descarga archivos compartidos (logs, capturas de pantalla, ejemplos de código) para aportar contexto adicional |
  | `files:write`       | Sube resúmenes visuales de los cambios del agente para una revisión rápida                                     |
  | `groups:history`    | Lee mensajes anteriores en canales privados para contexto en conversaciones de varios turnos                   |
  | `groups:read`       | Accede a metadatos de canales privados para publicar respuestas y mantener el flujo de la conversación         |
  | `im:history`        | Accede al historial de mensajes directos para contexto en conversaciones continuadas                           |
  | `im:read`           | Lee metadatos de MD para identificar participantes y mantener el encadenamiento correcto                       |
  | `im:write`          | Inicia mensajes directos para notificaciones privadas o comunicación individual                                |
  | `mpim:history`      | Accede al historial de MD grupales para conversaciones con múltiples participantes                             |
  | `mpim:read`         | Lee metadatos de MD grupales para dirigirse a los participantes y asegurar una entrega adecuada                |
  | `reactions:read`    | Observa reacciones de emoji para feedback del usuario y señales de estado                                      |
  | `reactions:write`   | Agrega reacciones de emoji para marcar el estado: ⏳ en ejecución, ✅ completado, ❌ con error                    |
  | `team:read`         | Identifica detalles del espacio de trabajo para separar instalaciones y aplicar configuraciones                |
  | `users:read`        | Asocia usuarios de Slack con cuentas de Cursor para permisos y acceso seguro                                   |
</div>

---

← Previous: [Linear](./linear.md) | [Index](./index.md) | Next: [Modelos](./modelos.md) →