---
title: "Planificación"
source: "https://docs.cursor.com/es/agent/planning"
language: "es"
language_name: "Spanish"
---

# Planificación
Source: https://docs.cursor.com/es/agent/planning

Cómo Agent planifica y gestiona tareas complejas con to-dos y colas

export const Kbd = ({children, tooltip, os}) => {
  const keysInput = typeof children === 'string' && children.trim() !== '' ? children : null;
  if (!keysInput) {
    return null;
  }
  const isModifier = key => {
    const modifiers = ['⌘', '⇧', '⌥', '⌃', '⏎', '⌫', '⌦', '⎋', '⇥', '⌁', '←', '→', '↑', '↓', 'Ctrl', 'Shift', 'Alt', 'Cmd', 'Opt', 'Return', 'Backspace', 'Delete', 'Escape', 'Tab', 'Space', 'Enter', 'Esc', 'ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down'];
    return modifiers.includes(key.trim());
  };
  const capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };
  const isMac = os ? os.toLowerCase() === 'mac' || os.toLowerCase() === 'macos' : typeof navigator !== 'undefined' && (navigator.platform.toUpperCase().indexOf('MAC') >= 0 || navigator.userAgent.toUpperCase().indexOf('MAC') >= 0);
  const convertToSymbols = shortcut => {
    if (isMac) {
      return shortcut.replace(/⌘|Cmd|CMD/gi, '⌘').replace(/⌥|Opt|OPT/gi, '⌥').replace(/⌃|Ctrl/gi, '⌃').replace(/⇧|Shift/gi, '⇧').replace(/⏎|Return/gi, '⏎').replace(/⌫|Backspace/gi, '⌫').replace(/⌦|Delete/gi, '⌦').replace(/␛|Escape/gi, '␛').replace(/⇥|Tab/gi, '⇥').replace(/⌁|Space/gi, '⌁').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, '←').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, '→').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, '↑').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, '↓');
    } else {
      const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Ctrl').replace(/⌥|Opt|OPT/gi, 'Alt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Enter').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Esc').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
      const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
      return keyList.join('+');
    }
  };
  const convertToReadableText = shortcut => {
    const converted = shortcut.replace(/⌘|Cmd|CMD/gi, 'Cmd').replace(/⌥|Opt|OPT/gi, 'Opt').replace(/⌃|Ctrl/gi, 'Ctrl').replace(/⇧|Shift/gi, 'Shift').replace(/⏎|Return/gi, 'Return').replace(/⌫|Backspace/gi, 'Backspace').replace(/⌦|Delete/gi, 'Delete').replace(/⎋|Escape/gi, 'Escape').replace(/⇥|Tab/gi, 'Tab').replace(/⌁|Space/gi, 'Space').replace(/←|Arrow\s*Left|ArrowLeft|Left/gi, 'Arrow-Left').replace(/→|Arrow\s*Right|ArrowRight|Right/gi, 'Arrow-Right').replace(/↑|Arrow\s*Up|ArrowUp|Up/gi, 'Arrow-Up').replace(/↓|Arrow\s*Down|ArrowDown|Down/gi, 'Arrow-Down');
    const keyList = converted.split(/[\+\s]+/).filter(key => key.trim());
    return keyList.map(key => {
      const trimmedKey = key.trim();
      return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
    }).join('+');
  };
  const displayShortcut = convertToSymbols(keysInput);
  const tooltipText = isMac ? tooltip ? `${convertToReadableText(keysInput)}: ${tooltip}` : convertToReadableText(keysInput) : tooltip || null;
  const processedKeys = isMac ? displayShortcut.split(/[\+\s]+/).filter(key => key.trim()).map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('') : displayShortcut.split('+').map(key => {
    const trimmedKey = key.trim();
    return isModifier(trimmedKey) ? trimmedKey : capitalizeFirstLetter(trimmedKey);
  }).join('+');
  return tooltipText ? <Tooltip tip={tooltipText}>
      <kbd>
        {processedKeys}
      </kbd>
    </Tooltip> : <kbd>
      {processedKeys}
    </kbd>;
};

Agent puede planificar con anticipación y gestionar tareas complejas con listas de tareas estructuradas y cola de mensajes, lo que facilita entender y hacer seguimiento de tareas de largo plazo.

<div id="agent-to-dos">
  ## Tareas pendientes de Agent
</div>

Agent puede dividir tareas largas en pasos manejables con dependencias, creando un plan estructurado que se actualiza conforme avanza el trabajo.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-todo.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=b0285913832a3ef123fe149516ee37ea" type="video/mp4" data-path="images/agent/planning/agent-todo.mp4" />
</video>

<div id="how-it-works">
  ### Cómo funciona
</div>

* Agent crea automáticamente listas de pendientes para tareas complejas
* Cada ítem puede depender de otras tareas
* La lista se actualiza en tiempo real a medida que avanza el trabajo
* Las tareas completadas se marcan automáticamente

<div id="visibility">
  ### Visibilidad
</div>

* Las tareas pendientes aparecen en la interfaz del chat
* Si la [integración con Slack](/es/slack) está configurada, las tareas también se ven ahí
* Podés ver el desglose completo de la tarea en cualquier momento

<Tip>
  Para planificar mejor, describí claramente tu objetivo final. Agent creará desgloses de tareas más
  precisos cuando entienda el alcance completo.
</Tip>

<Note>La planificación y las tareas pendientes no están disponibles actualmente en el modo auto.</Note>

<div id="queued-messages">
  ## Mensajes en cola
</div>

Pon mensajes de seguimiento en cola mientras Agent trabaja en la tarea actual. Tus instrucciones esperan su turno y se ejecutan automáticamente cuando estén listas.

<video autoPlay loop muted playsInline controls>
  <source src="https://mintcdn.com/cursor/GnTEh_6SKR7li-hM/images/agent/planning/agent-queue.mp4?fit=max&auto=format&n=GnTEh_6SKR7li-hM&q=85&s=4cdd6a7d1e12c67e520bc3ba67a42e0d" type="video/mp4" data-path="images/agent/planning/agent-queue.mp4" />
</video>

<div id="using-the-queue">
  ### Uso de la cola
</div>

1. Mientras Agent está trabajando, escribe tu siguiente instrucción
2. Pulsa <Kbd>Ctrl+Enter</Kbd> para añadirla a la cola
3. Los mensajes aparecen en orden debajo de la tarea activa
4. Reordena los mensajes en cola haciendo clic en la flecha
5. Agent los procesa secuencialmente al terminar

<div id="override-the-queue">
  ### Omitir la cola
</div>

Para poner tu mensaje en cola en lugar de usar la mensajería predeterminada, usa <Kbd>Ctrl+Enter</Kbd>. Para enviar un mensaje de inmediato sin ponerlo en cola, usa <Kbd>Cmd+Enter</Kbd>. Esto “empuja” tu mensaje a la fuerza, omitiendo la cola para ejecutarlo de inmediato.

<div id="default-messaging">
  ## Mensajería predeterminada
</div>

De forma predeterminada, los mensajes se envían lo más rápido posible, generalmente apareciendo justo después de que Agent complete una llamada a una herramienta. Esto ofrece la experiencia más ágil.

<div id="how-default-messaging-works">
  ### Cómo funciona la mensajería predeterminada
</div>

* Tu mensaje se añade al mensaje de usuario más reciente en el chat
* Los mensajes suelen adjuntarse a los resultados de las herramientas y se envían en cuanto están listos
* Esto crea un flujo de conversación más natural sin interrumpir el trabajo actual de Agent
* Por defecto, esto ocurre cuando presionas Enter mientras Agent está trabajando

---

← Previous: [Descripción general](./descripcin-general.md) | [Index](./index.md) | Next: [Diffs y revisión](./diffs-y-revisin.md) →